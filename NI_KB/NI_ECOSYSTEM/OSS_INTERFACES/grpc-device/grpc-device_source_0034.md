# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviSwtch.h sha256=39bee3aa592ab70010c0a476cc19d808b4452d260fe66490aac428c8e3220ad3 bytes=34809 -->
## FILE: imports/include/IviSwtch.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviSwtch.h`
- sha256: `39bee3aa592ab70010c0a476cc19d808b4452d260fe66490aac428c8e3220ad3`
- bytes: 34809

````c
/****************************************************************************
 *                             I V I - S W T C H                             
 *---------------------------------------------------------------------------
 *    Copyright (c) 1998-2020 National Instruments.  All Rights Reserved.         
 *---------------------------------------------------------------------------
 *                                                                           
 * Title:       iviswtch.h                                                    
 * Purpose:     IviSwtch Class declarations for the Base and Extended  
 *              IviSwtch Capabilities.                                                 
 ****************************************************************************/

#ifndef IVISWTCH_HEADER
#define IVISWTCH_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVISWTCH_MAJOR_VERSION              (4L)
#define IVISWTCH_MINOR_VERSION              (0L)

#define IVISWTCH_CLASS_SPEC_MAJOR_VERSION   (4L)
#define IVISWTCH_CLASS_SPEC_MINOR_VERSION   (0L)

#define IVISWTCH_DRIVER_VENDOR              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVISWTCH_DRIVER_DESCRIPTION         "IviSwtch Class Driver [Compiled for 64-bit.]"
#else
#define IVISWTCH_DRIVER_DESCRIPTION         "IviSwtch Class Driver"
#endif

/*****************************************************************************
 *-------------------- IviSwtch Class Attribute Defines ---------------------*
 *****************************************************************************/

    /*- IVI Inherent Attributes -*/
        /*- User Options -*/
#define IVISWTCH_ATTR_CACHE                     IVI_ATTR_CACHE                         /* ViBoolean */
#define IVISWTCH_ATTR_RANGE_CHECK               IVI_ATTR_RANGE_CHECK                   /* ViBoolean */
#define IVISWTCH_ATTR_QUERY_INSTRUMENT_STATUS   IVI_ATTR_QUERY_INSTRUMENT_STATUS       /* ViBoolean */
#define IVISWTCH_ATTR_RECORD_COERCIONS          IVI_ATTR_RECORD_COERCIONS              /* ViBoolean */
#define IVISWTCH_ATTR_SIMULATE                  IVI_ATTR_SIMULATE                      /* ViBoolean */
#define IVISWTCH_ATTR_INTERCHANGE_CHECK         IVI_ATTR_INTERCHANGE_CHECK             /* ViBoolean */
#define IVISWTCH_ATTR_SPY                       IVI_ATTR_SPY                           /* ViBoolean */
#define IVISWTCH_ATTR_USE_SPECIFIC_SIMULATION   IVI_ATTR_USE_SPECIFIC_SIMULATION       /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVISWTCH_ATTR_GROUP_CAPABILITIES        IVI_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */
#define IVISWTCH_ATTR_FUNCTION_CAPABILITIES     IVI_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVISWTCH_ATTR_CLASS_DRIVER_PREFIX                         IVI_ATTR_CLASS_DRIVER_PREFIX                       /* ViString, read-only */
#define IVISWTCH_ATTR_CLASS_DRIVER_VENDOR                         IVI_ATTR_CLASS_DRIVER_VENDOR                       /* ViString, read-only */
#define IVISWTCH_ATTR_CLASS_DRIVER_DESCRIPTION                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION                  /* ViString, read-only */
#define IVISWTCH_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVISWTCH_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION     /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_PREFIX                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString, read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_LOCATOR                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR                   /* ViString, read-only */
#define IVISWTCH_ATTR_IO_RESOURCE_DESCRIPTOR                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR                    /* ViString, read-only */
#define IVISWTCH_ATTR_LOGICAL_NAME                                IVI_ATTR_LOGICAL_NAME                              /* ViString, read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_VENDOR                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString, read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString, read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVISWTCH_ATTR_INSTRUMENT_FIRMWARE_REVISION     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only */
#define IVISWTCH_ATTR_INSTRUMENT_MANUFACTURER          IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only */
#define IVISWTCH_ATTR_INSTRUMENT_MODEL                 IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only */
#define IVISWTCH_ATTR_SUPPORTED_INSTRUMENT_MODELS      IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

        /* Version Information */
#define IVISWTCH_ATTR_CLASS_DRIVER_REVISION            IVI_ATTR_CLASS_DRIVER_REVISION          /* ViString, read-only */

#define IVISWTCH_ATTR_SPECIFIC_DRIVER_REVISION         IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only */

        /*- Driver Setup information -*/
#define IVISWTCH_ATTR_DRIVER_SETUP                     IVI_ATTR_DRIVER_SETUP                   /* ViString */

    /*- IviSwtch Fundamental Attributes -*/
#define IVISWTCH_ATTR_CHANNEL_COUNT             IVI_ATTR_CHANNEL_COUNT              /* ViInt32,  read-only */
#define IVISWTCH_ATTR_IS_SOURCE_CHANNEL         (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)   /* ViBoolean, Channel-based */
#define IVISWTCH_ATTR_IS_DEBOUNCED              (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)   /* ViBoolean, Read-only */
#define IVISWTCH_ATTR_IS_CONFIGURATION_CHANNEL  (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)   /* ViBoolean, Channel-based */
#define IVISWTCH_ATTR_SETTLING_TIME             (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_BANDWIDTH                 (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_DC_VOLTAGE            (IVI_CLASS_PUBLIC_ATTR_BASE + 6L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_AC_VOLTAGE            (IVI_CLASS_PUBLIC_ATTR_BASE + 7L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_SWITCHING_DC_CURRENT  (IVI_CLASS_PUBLIC_ATTR_BASE + 8L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_SWITCHING_AC_CURRENT  (IVI_CLASS_PUBLIC_ATTR_BASE + 9L)   /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_CARRY_DC_CURRENT      (IVI_CLASS_PUBLIC_ATTR_BASE + 10L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_CARRY_AC_CURRENT      (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_SWITCHING_DC_POWER    (IVI_CLASS_PUBLIC_ATTR_BASE + 12L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_SWITCHING_AC_POWER    (IVI_CLASS_PUBLIC_ATTR_BASE + 13L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_CARRY_DC_POWER        (IVI_CLASS_PUBLIC_ATTR_BASE + 14L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_MAX_CARRY_AC_POWER        (IVI_CLASS_PUBLIC_ATTR_BASE + 15L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_CHARACTERISTIC_IMPEDANCE  (IVI_CLASS_PUBLIC_ATTR_BASE + 16L)  /* ViReal64, Read-only, Channel-based */
#define IVISWTCH_ATTR_WIRE_MODE                 (IVI_CLASS_PUBLIC_ATTR_BASE + 17L)  /* ViInt32,  Read-only, Channel-based */

    /*- IviSwtch Extended Attributes -*/
        /*- IviSwitchScanner Extension Group -*/
#define IVISWTCH_ATTR_NUM_OF_ROWS               (IVI_CLASS_PUBLIC_ATTR_BASE + 18L)  /* ViInt32, Read-only */
#define IVISWTCH_ATTR_NUM_OF_COLUMNS            (IVI_CLASS_PUBLIC_ATTR_BASE + 19L)  /* ViInt32, Read-only */
#define IVISWTCH_ATTR_SCAN_LIST                 (IVI_CLASS_PUBLIC_ATTR_BASE + 20L)  /* ViString */
#define IVISWTCH_ATTR_SCAN_MODE                 (IVI_CLASS_PUBLIC_ATTR_BASE + 21L)  /* ViInt32 */
#define IVISWTCH_ATTR_TRIGGER_INPUT             (IVI_CLASS_PUBLIC_ATTR_BASE + 22L)  /* ViInt32 */
#define IVISWTCH_ATTR_SCAN_ADVANCED_OUTPUT      (IVI_CLASS_PUBLIC_ATTR_BASE + 23L)  /* ViInt32 */
#define IVISWTCH_ATTR_IS_SCANNING               (IVI_CLASS_PUBLIC_ATTR_BASE + 24L)  /* ViBoolean, Read-only */
#define IVISWTCH_ATTR_SCAN_DELAY                (IVI_CLASS_PUBLIC_ATTR_BASE + 25L)  /* ViReal64 */
#define IVISWTCH_ATTR_CONTINUOUS_SCAN           (IVI_CLASS_PUBLIC_ATTR_BASE + 26L)  /* ViBoolean */

/*****************************************************************************
 *---------------- IviSwtch Class Attribute Value Defines -------------------*
 *****************************************************************************/

    /*- Defined values for attribute IVISWTCH_ATTR_SCAN_MODE -*/
#define IVISWTCH_VAL_NONE                                   (0L)
#define IVISWTCH_VAL_BREAK_BEFORE_MAKE                      (1L)
#define IVISWTCH_VAL_BREAK_AFTER_MAKE                       (2L)
#define IVISWTCH_VAL_SCAN_MODE_CLASS_EXT_BASE               (500L)
#define IVISWTCH_VAL_SCAN_MODE_SPECIFIC_EXT_BASE            (1000L)

    /*- Defined values for attribute IVISWTCH_ATTR_TRIGGER_INPUT -*/
#define IVISWTCH_VAL_IMMEDIATE                              (1L)
#define IVISWTCH_VAL_EXTERNAL                               (2L)
#define IVISWTCH_VAL_SOFTWARE_TRIG                          (3L)
#define IVISWTCH_VAL_TTL0                                   (111L)
#define IVISWTCH_VAL_TTL1                                   (112L)
#define IVISWTCH_VAL_TTL2                                   (113L)
#define IVISWTCH_VAL_TTL3                                   (114L)
#define IVISWTCH_VAL_TTL4                                   (115L)
#define IVISWTCH_VAL_TTL5                                   (116L)
#define IVISWTCH_VAL_TTL6                                   (117L)
#define IVISWTCH_VAL_TTL7                                   (118L)
#define IVISWTCH_VAL_ECL0                                   (119L)
#define IVISWTCH_VAL_ECL1                                   (120L)
#define IVISWTCH_VAL_PXI_STAR                               (125L)
#define IVISWTCH_VAL_RTSI_0                                 (140L)
#define IVISWTCH_VAL_RTSI_1                                 (141L)
#define IVISWTCH_VAL_RTSI_2                                 (142L)
#define IVISWTCH_VAL_RTSI_3                                 (143L)
#define IVISWTCH_VAL_RTSI_4                                 (144L)
#define IVISWTCH_VAL_RTSI_5                                 (145L)
#define IVISWTCH_VAL_RTSI_6                                 (146L)
#define IVISWTCH_VAL_TRIGGER_INPUT_CLASS_EXT_BASE           (500L)
#define IVISWTCH_VAL_TRIGGER_INPUT_SPECIFIC_EXT_BASE        (1000L)

    /*- Defined values for attribute IVISWTCH_ATTR_SCAN_ADVANCED_OUTPUT -*/
#define IVISWTCH_VAL_GPIB_SRQ                               (5L)
/* #define IVISWTCH_VAL_NONE                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_EXTERNAL                    DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL0                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL1                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL2                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL3                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL4                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL5                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL6                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_TTL7                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_ECL0                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_ECL1                        DEFINED ABOVE */
/* #define IVISWTCH_VAL_PXI_STAR                    DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_0                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_1                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_2                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_3                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_4                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_5                      DEFINED ABOVE */
/* #define IVISWTCH_VAL_RTSI_6                      DEFINED ABOVE */
#define IVISWTCH_VAL_SCAN_ADVANCED_OUTPUT_CLASS_EXT_BASE    (500L)
#define IVISWTCH_VAL_SCAN_ADVANCED_OUTPUT_SPECIFIC_EXT_BASE (1000L)

    /*- Defined values for IviSwtch_CanConnect path capability parameter -*/
#define IVISWTCH_VAL_PATH_AVAILABLE                         (1L)
#define IVISWTCH_VAL_PATH_EXISTS                            (2L)
#define IVISWTCH_VAL_PATH_UNSUPPORTED                       (3L)
#define IVISWTCH_VAL_RSRC_IN_USE                            (4L)
#define IVISWTCH_VAL_SOURCE_CONFLICT                        (5L)
#define IVISWTCH_VAL_CHANNEL_NOT_AVAILABLE                  (6L)
#define IVISWTCH_VAL_CAN_CONNECT_CLASS_EXT_BASE             (500L)
#define IVISWTCH_VAL_CAN_CONNECT_SPECIFIC_EXT_BASE          (1000L)

/*****************************************************************************
 *-------- IviSwtch Class Instrument Driver Function Declarations -----------*
 *****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviSwtch_init (ViRsrc logicalName, 
                                 ViBoolean idQuery, 
                                 ViBoolean resetDevice, 
                                 ViSession *vi);

ViStatus _VI_FUNC IviSwtch_close (ViSession vi);

ViStatus _VI_FUNC IviSwtch_reset (ViSession vi);

ViStatus _VI_FUNC IviSwtch_self_test (ViSession vi, 
                                      ViInt16 *selfTestResult, 
                                      ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviSwtch_error_query (ViSession vi, 
                                        ViInt32 *errorCode, 
                                        ViChar errorMessage[]);

ViStatus _VI_FUNC IviSwtch_error_message (ViSession vi, 
                                          ViStatus statusCode, 
                                          ViChar message[]);

ViStatus _VI_FUNC IviSwtch_revision_query (ViSession vi, 
                                           ViChar driverRev[], 
                                           ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviSwtch_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviSwtch_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviSwtch_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviSwtch_InitWithOptions (ViRsrc logicalName, 
                                            ViBoolean IDQuery,
                                            ViBoolean resetDevice, 
                                            ViConstString optionString, 
                                            ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviSwtch_GetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 *value);

ViStatus _VI_FUNC IviSwtch_SetAttributeViInt32 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt32 value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViInt32 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviSwtch_GetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 *value);

ViStatus _VI_FUNC IviSwtch_SetAttributeViInt64 (ViSession vi, 
                                                ViConstString channelName,
                                                ViAttr attributeId,
                                                ViInt64 value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViInt64 (ViSession vi, 
                                                  ViConstString channelName,
                                                  ViAttr attributeId,
                                                  ViInt64 value);
#endif

ViStatus _VI_FUNC IviSwtch_GetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 *value);

ViStatus _VI_FUNC IviSwtch_SetAttributeViReal64 (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViReal64 value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViReal64 (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViReal64 value);

ViStatus _VI_FUNC IviSwtch_GetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViInt32 bufferSize, 
                                                 ViChar value[]);

ViStatus _VI_FUNC IviSwtch_SetAttributeViString (ViSession vi, 
                                                 ViConstString channelName, 
                                                 ViAttr attributeId, 
                                                 ViConstString value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViString (ViSession vi, 
                                                   ViConstString channelName, 
                                                   ViAttr attributeId, 
                                                   ViConstString value); 

ViStatus _VI_FUNC IviSwtch_GetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean *value);

ViStatus _VI_FUNC IviSwtch_SetAttributeViBoolean (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViBoolean value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViBoolean (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViBoolean value);

ViStatus _VI_FUNC IviSwtch_GetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession *value);

ViStatus _VI_FUNC IviSwtch_SetAttributeViSession (ViSession vi, 
                                                  ViConstString channelName, 
                                                  ViAttr attributeId, 
                                                  ViSession value);

ViStatus _VI_FUNC IviSwtch_CheckAttributeViSession (ViSession vi, 
                                                    ViConstString channelName, 
                                                    ViAttr attributeId, 
                                                    ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviSwtch_LockSession (ViSession vi, 
                                        ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviSwtch_UnlockSession (ViSession vi, 
                                          ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviSwtch_GetError (ViSession vi, 
                                     ViStatus *errorCode, 
                                     ViInt32 bufferSize, 
                                     ViChar description[]);

ViStatus _VI_FUNC IviSwtch_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviSwtch_GetNextInterchangeWarning (ViSession vi, 
                                                      ViInt32 bufferSize,
                                                      ViChar warning[]);

ViStatus _VI_FUNC IviSwtch_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviSwtch_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviSwtch_GetNextCoercionRecord (ViSession vi,
                                                  ViInt32 bufferSize, 
                                                  ViChar record[]);

ViStatus _VI_FUNC IviSwtch_GetSpecificDriverCHandle (ViSession vi,
                                                     ViSession* specificDriverCHandle);
    /*- IviSwtchBase Capability Group Functions -*/
ViStatus _VI_FUNC IviSwtch_CanConnect (ViSession vi, 
                                       ViConstString channel1,
                                       ViConstString channel2, 
                                       ViInt32 *pathCapability);

ViStatus _VI_FUNC IviSwtch_Connect (ViSession vi, 
                                    ViConstString channel1,
                                    ViConstString channel2);

ViStatus _VI_FUNC IviSwtch_Disconnect (ViSession vi, 
                                       ViConstString channel1, 
                                       ViConstString channel2);

ViStatus _VI_FUNC IviSwtch_DisconnectAll (ViSession vi);

ViStatus _VI_FUNC IviSwtch_GetChannelName (ViSession vi,
                                           ViInt32 index,
                                           ViInt32 bufferSize,
                                           ViChar name[]);

ViStatus _VI_FUNC IviSwtch_GetPath (ViSession vi, 
                                    ViConstString channel1, 
                                    ViConstString channel2,
                                    ViInt32 bufferSize, 
                                    ViChar pathList[]);

ViStatus _VI_FUNC IviSwtch_IsDebounced (ViSession vi, 
                                        ViBoolean *isDebounced);

ViStatus _VI_FUNC IviSwtch_SetPath (ViSession vi, 
                                    ViConstString pathList);

ViStatus _VI_FUNC IviSwtch_WaitForDebounce (ViSession vi, 
                                            ViInt32 maxTime);

    /*- IviSwtchScanner Extension Group Functions -*/
ViStatus _VI_FUNC IviSwtch_AbortScan (ViSession vi);    

ViStatus _VI_FUNC IviSwtch_ConfigureScanList (ViSession vi, 
                                              ViConstString scanList, 
                                              ViInt32 scanMode);

ViStatus _VI_FUNC IviSwtch_ConfigureScanTrigger (ViSession vi, 
                                                 ViReal64 scanDelay, 
                                                 ViInt32 triggerInput, 
                                                 ViInt32 scanAdvancedOutput);

ViStatus _VI_FUNC IviSwtch_InitiateScan (ViSession vi);

ViStatus _VI_FUNC IviSwtch_IsScanning (ViSession vi, 
                                       ViBoolean *isScanning);

ViStatus _VI_FUNC IviSwtch_SetContinuousScan (ViSession vi, 
                                              ViBoolean status);

ViStatus _VI_FUNC IviSwtch_WaitForScanComplete (ViSession vi, 
                                                ViInt32 maxTime);

    /*- IviSwtchSoftwareTrigger Extension Group Functions -*/
ViStatus _VI_FUNC IviSwtch_SendSoftwareTrigger (ViSession vi);

/*****************************************************************************
 *---------------- IviSwtch Class Error And Completion Codes ----------------*
 *****************************************************************************/
#define IVISWTCH_WARN_PATH_REMAINS                  (IVI_CLASS_WARN_BASE +  1L)
#define IVISWTCH_WARN_IMPLICIT_CONNECTION_EXISTS    (IVI_CLASS_WARN_BASE +  2L)

#define IVISWTCH_ERROR_INVALID_SWITCH_PATH          (IVI_CLASS_ERROR_BASE + 1L)
#define IVISWTCH_ERROR_INVALID_SCAN_LIST            (IVI_CLASS_ERROR_BASE + 2L)
#define IVISWTCH_ERROR_RSRC_IN_USE                  (IVI_CLASS_ERROR_BASE + 3L)
#define IVISWTCH_ERROR_EMPTY_SCAN_LIST              (IVI_CLASS_ERROR_BASE + 4L)
#define IVISWTCH_ERROR_EMPTY_SWITCH_PATH            (IVI_CLASS_ERROR_BASE + 5L)
#define IVISWTCH_ERROR_SCAN_IN_PROGRESS             (IVI_CLASS_ERROR_BASE + 6L)
#define IVISWTCH_ERROR_NO_SCAN_IN_PROGRESS          (IVI_CLASS_ERROR_BASE + 7L)
#define IVISWTCH_ERROR_NO_SUCH_PATH                 (IVI_CLASS_ERROR_BASE + 8L)
#define IVISWTCH_ERROR_IS_CONFIGURATION_CHANNEL     (IVI_CLASS_ERROR_BASE + 9L)
#define IVISWTCH_ERROR_NOT_A_CONFIGURATION_CHANNEL  (IVI_CLASS_ERROR_BASE + 10L)
#define IVISWTCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES   (IVI_CLASS_ERROR_BASE + 11L)
#define IVISWTCH_ERROR_EXPLICIT_CONNECTION_EXISTS   (IVI_CLASS_ERROR_BASE + 12L)
#define IVISWTCH_ERROR_LEG_MISSING_FIRST_CHANNEL    (IVI_CLASS_ERROR_BASE + 13L)
#define IVISWTCH_ERROR_LEG_MISSING_SECOND_CHANNEL   (IVI_CLASS_ERROR_BASE + 14L)
#define IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_LEG    (IVI_CLASS_ERROR_BASE + 15L)
#define IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_PATH   (IVI_CLASS_ERROR_BASE + 16L)
#define IVISWTCH_ERROR_PATH_NOT_FOUND               (IVI_CLASS_ERROR_BASE + 17L)
#define IVISWTCH_ERROR_DISCONTINUOUS_PATH           (IVI_CLASS_ERROR_BASE + 18L)
#define IVISWTCH_ERROR_CANNOT_CONNECT_DIRECTLY      (IVI_CLASS_ERROR_BASE + 19L)
#define IVISWTCH_ERROR_CHANNELS_ALREADY_CONNECTED   (IVI_CLASS_ERROR_BASE + 20L)
#define IVISWTCH_ERROR_CANNOT_CONNECT_TO_ITSELF     (IVI_CLASS_ERROR_BASE + 21L)
#define IVISWTCH_ERROR_MAX_TIME_EXCEEDED            (IVI_CLASS_ERROR_BASE + 22L)

#define IVISWTCH_ERROR_TRIGGER_NOT_SOFTWARE         (IVI_CROSS_CLASS_ERROR_BASE + 1)

#define IVISWTCH_WARNMSG_PATH_REMAINS               "Some connections remain "\
                                                    "after disconnecting."
#define IVISWTCH_WARNMSG_IMPLICIT_CONNECTION_EXISTS "The implicit connection exists between the channels."

#define IVISWTCH_ERRMSG_INVALID_SWITCH_PATH         "Invalid switch path list string."
#define IVISWTCH_ERRMSG_INVALID_SCAN_LIST           "Invalid scan list. "\
                                                    "The given scan list string does not have the correct syntax, "\
                                                    "or the scan list syntax cannot be implemented by the switch."
#define IVISWTCH_ERRMSG_RSRC_IN_USE                 "One of the channels in the path is a "\
                                                    "configuration channel that is in use."
#define IVISWTCH_ERRMSG_EMPTY_SCAN_LIST             "No scan list specified."
#define IVISWTCH_ERRMSG_EMPTY_SWITCH_PATH           "The specified path list string is empty."
#define IVISWTCH_ERRMSG_SCAN_IN_PROGRESS            "The switch module is currently scanning through the scan list."
#define IVISWTCH_ERRMSG_NO_SCAN_IN_PROGRESS         "The switch module is not currently scanning through the scan list."
#define IVISWTCH_ERRMSG_NO_SUCH_PATH                "No explicit path exists "\
                                                    "between the two channels."
#define IVISWTCH_ERRMSG_IS_CONFIGURATION_CHANNEL    "An explicit connection to a configuration channel is not allowed."
#define IVISWTCH_ERRMSG_NOT_A_CONFIGURATION_CHANNEL "One of the non-terminal "\
                                                    "channels in the path is not a "\
                                                    "configuration channel."
#define IVISWTCH_ERRMSG_ATTEMPT_TO_CONNECT_SOURCES  "A connection between two different sources is not allowed."
#define IVISWTCH_ERRMSG_EXPLICIT_CONNECTION_EXISTS  "An explicit connection "\
                                                    "between the channels already exists."
#define IVISWTCH_ERRMSG_LEG_MISSING_FIRST_CHANNEL   "A leg in the path does "\
                                                    "not begin with a channel name."
#define IVISWTCH_ERRMSG_LEG_MISSING_SECOND_CHANNEL  "A leg in the path is "\
                                                    "missing the second channel."
#define IVISWTCH_ERRMSG_CHANNEL_DUPLICATED_IN_LEG   "The first and the second "\
                                                    "channels in the leg are the same."
#define IVISWTCH_ERRMSG_CHANNEL_DUPLICATED_IN_PATH  "A channel name is "\
                                                    "duplicated in the path string."
#define IVISWTCH_ERRMSG_PATH_NOT_FOUND              "No path was found "\
                                                    "between the two channels."
#define IVISWTCH_ERRMSG_DISCONTINUOUS_PATH          "The first channel of a "\
                                                    "leg in the path is not the same as "\
                                                    "the second channel in the previous leg."
#define IVISWTCH_ERRMSG_CANNOT_CONNECT_DIRECTLY     "The path contains a leg "\
                                                    "with two channels that cannot be "\
                                                    "directly connected."
#define IVISWTCH_ERRMSG_CHANNELS_ALREADY_CONNECTED  "A leg in the path "\
                                                    "contains two channels that are "\
                                                    "already directly connected."
#define IVISWTCH_ERRMSG_CANNOT_CONNECT_TO_ITSELF    "A channel cannot be "\
                                                    "connected to itself."

#define IVISWTCH_ERRMSG_TRIGGER_NOT_SOFTWARE        "The trigger source is not set to "\
                                                    "software trigger."

#define IVISWTCH_ERRMSG_MAX_TIME_EXCEEDED           "Maximum time exceeded before the operation completed."

#define IVISWTCH_ERROR_CODES_AND_MSGS                                                             \
    {IVISWTCH_WARN_PATH_REMAINS,                    IVISWTCH_WARNMSG_PATH_REMAINS},               \
    {IVISWTCH_WARN_IMPLICIT_CONNECTION_EXISTS,      IVISWTCH_WARNMSG_IMPLICIT_CONNECTION_EXISTS}, \
    {IVISWTCH_ERROR_INVALID_SWITCH_PATH,            IVISWTCH_ERRMSG_INVALID_SWITCH_PATH},         \
    {IVISWTCH_ERROR_INVALID_SCAN_LIST,              IVISWTCH_ERRMSG_INVALID_SCAN_LIST},           \
    {IVISWTCH_ERROR_RSRC_IN_USE,                    IVISWTCH_ERRMSG_RSRC_IN_USE},                 \
    {IVISWTCH_ERROR_EMPTY_SCAN_LIST,                IVISWTCH_ERRMSG_EMPTY_SCAN_LIST},             \
    {IVISWTCH_ERROR_EMPTY_SWITCH_PATH,              IVISWTCH_ERRMSG_EMPTY_SWITCH_PATH},           \
    {IVISWTCH_ERROR_SCAN_IN_PROGRESS,               IVISWTCH_ERRMSG_SCAN_IN_PROGRESS},            \
    {IVISWTCH_ERROR_NO_SCAN_IN_PROGRESS,            IVISWTCH_ERRMSG_NO_SCAN_IN_PROGRESS},         \
    {IVISWTCH_ERROR_NO_SUCH_PATH,                   IVISWTCH_ERRMSG_NO_SUCH_PATH},                \
    {IVISWTCH_ERROR_IS_CONFIGURATION_CHANNEL,       IVISWTCH_ERRMSG_IS_CONFIGURATION_CHANNEL},    \
    {IVISWTCH_ERROR_NOT_A_CONFIGURATION_CHANNEL,    IVISWTCH_ERRMSG_NOT_A_CONFIGURATION_CHANNEL}, \
    {IVISWTCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES,     IVISWTCH_ERRMSG_ATTEMPT_TO_CONNECT_SOURCES},  \
    {IVISWTCH_ERROR_EXPLICIT_CONNECTION_EXISTS,     IVISWTCH_ERRMSG_EXPLICIT_CONNECTION_EXISTS},  \
    {IVISWTCH_ERROR_LEG_MISSING_FIRST_CHANNEL,      IVISWTCH_ERRMSG_LEG_MISSING_FIRST_CHANNEL},   \
    {IVISWTCH_ERROR_LEG_MISSING_SECOND_CHANNEL,     IVISWTCH_ERRMSG_LEG_MISSING_SECOND_CHANNEL},  \
    {IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_LEG,      IVISWTCH_ERRMSG_CHANNEL_DUPLICATED_IN_LEG},   \
    {IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_PATH,     IVISWTCH_ERRMSG_CHANNEL_DUPLICATED_IN_PATH},  \
    {IVISWTCH_ERROR_PATH_NOT_FOUND,                 IVISWTCH_ERRMSG_PATH_NOT_FOUND},              \
    {IVISWTCH_ERROR_DISCONTINUOUS_PATH,             IVISWTCH_ERRMSG_DISCONTINUOUS_PATH},          \
    {IVISWTCH_ERROR_CANNOT_CONNECT_DIRECTLY,        IVISWTCH_ERRMSG_CANNOT_CONNECT_DIRECTLY},     \
    {IVISWTCH_ERROR_CHANNELS_ALREADY_CONNECTED,     IVISWTCH_ERRMSG_CHANNELS_ALREADY_CONNECTED},  \
    {IVISWTCH_ERROR_CANNOT_CONNECT_TO_ITSELF,       IVISWTCH_ERRMSG_CANNOT_CONNECT_TO_ITSELF},    \
    {IVISWTCH_ERROR_TRIGGER_NOT_SOFTWARE,           IVISWTCH_ERRMSG_TRIGGER_NOT_SOFTWARE},        \
	{IVISWTCH_ERROR_MAX_TIME_EXCEEDED,              IVISWTCH_ERRMSG_MAX_TIME_EXCEEDED}

/*- IviSwtchObsolete.h included for backwards compatibility -*/
#include "IviSwtchObsolete.h"

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* IVISWTCH_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviSwtchObsolete.h sha256=c59017788cf3919be5c5ba28f2eb5815a7e7dda7752707e45c6275f09b0933bf bytes=4831 -->
## FILE: imports/include/IviSwtchObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviSwtchObsolete.h`
- sha256: `c59017788cf3919be5c5ba28f2eb5815a7e7dda7752707e45c6275f09b0933bf`
- bytes: 4831

````c
/*****************************************************************************
 *                          I V I - S W T C H  1.0                           
 *----------------------------------------------------------------------------
 *    Copyright (c) 1999-2020 National Instruments.  All Rights Reserved.         
 *----------------------------------------------------------------------------
 *                                                                           
 * Title:       IviSwtchObsolete.h                                           
 * Purpose:     IviSwtch Class value and attribute Id declarations for the   
 *              now obsolete IviSwtch 1.0 specification.                      
 *              These macros are defined to keep backward compatibility with 
 *              previous versions of this file.  Swtich specific drivers     
 *              should no longer use these macros. Instead, the drivers must 
 *              use definitions from the current IviSwtch.h header file.     
 *****************************************************************************/

#ifndef IVISWTCH_HEADER_OBSOLETE
#define IVISWTCH_HEADER_OBSOLETE
#include <ivi.h>

    /*- Obsolete Inherent Attributes -*/
#define IVISWTCH_ATTR_CLASS_MAJOR_VERSION        IVI_ATTR_CLASS_MAJOR_VERSION
#define IVISWTCH_ATTR_CLASS_MINOR_VERSION        IVI_ATTR_CLASS_MINOR_VERSION
#define IVISWTCH_ATTR_CLASS_REVISION             IVI_ATTR_CLASS_REVISION

#define IVISWTCH_ATTR_CLASS_PREFIX               IVI_ATTR_CLASS_PREFIX
#define IVISWTCH_ATTR_SPECIFIC_PREFIX            IVI_ATTR_SPECIFIC_PREFIX
#define IVISWTCH_ATTR_MODULE_PATHNAME            IVI_ATTR_MODULE_PATHNAME

#define IVISWTCH_ATTR_DRIVER_MAJOR_VERSION       IVI_ATTR_DRIVER_MAJOR_VERSION
#define IVISWTCH_ATTR_DRIVER_MINOR_VERSION       IVI_ATTR_DRIVER_MINOR_VERSION
#define IVISWTCH_ATTR_DRIVER_REVISION            IVI_ATTR_DRIVER_REVISION

#define IVISWTCH_ATTR_ENGINE_MAJOR_VERSION       IVI_ATTR_ENGINE_MAJOR_VERSION        /* ViInt32,  read-only */
#define IVISWTCH_ATTR_ENGINE_MINOR_VERSION       IVI_ATTR_ENGINE_MINOR_VERSION        /* ViInt32,  read-only */
#define IVISWTCH_ATTR_ENGINE_REVISION            IVI_ATTR_ENGINE_REVISION             /* ViString, read-only */

#define IVISWTCH_ATTR_NUM_CHANNELS               IVI_ATTR_NUM_CHANNELS
#define IVISWTCH_ATTR_QUERY_INSTR_STATUS         IVI_ATTR_QUERY_INSTR_STATUS /* ViBoolean */
#define IVISWTCH_ATTR_RESOURCE_DESCRIPTOR        IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only */

#define IVISWTCH_ATTR_IO_SESSION_TYPE                  IVI_ATTR_IO_SESSION_TYPE
#define IVISWTCH_ATTR_IO_SESSION                       IVI_ATTR_IO_SESSION

#define IVISWTCH_ATTR_CLASS_DRIVER_MAJOR_VERSION       IVI_ATTR_CLASS_DRIVER_MAJOR_VERSION     /* ViInt32,  read-only */
#define IVISWTCH_ATTR_CLASS_DRIVER_MINOR_VERSION       IVI_ATTR_CLASS_DRIVER_MINOR_VERSION     /* ViInt32,  read-only */

#define IVISWTCH_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVISWTCH_ATTR_SPECIFIC_DRIVER_MINOR_VERSION    IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION  /* ViInt32,  read-only */

#define IVISWTCH_ATTR_ATTRIBUTE_CAPABILITIES    IVI_ATTR_ATTRIBUTE_CAPABILITIES        /* ViString, read-only */

        /*- Error Info -*/
#define IVISWTCH_ATTR_PRIMARY_ERROR                    IVI_ATTR_PRIMARY_ERROR                  /* ViInt32  */
#define IVISWTCH_ATTR_SECONDARY_ERROR                  IVI_ATTR_SECONDARY_ERROR                /* ViInt32  */
#define IVISWTCH_ATTR_ERROR_ELABORATION                IVI_ATTR_ERROR_ELABORATION              /* ViString */

    /*- IviSwtch Obsolete Macros -*/
#define IVISWTCH_VAL_1_WIRE       (1L)
#define IVISWTCH_VAL_2_WIRE       (2L)
#define IVISWTCH_VAL_3_WIRE       (3L)
#define IVISWTCH_VAL_4_WIRE       (4L)
#define IVISWTCH_VAL_GPIB_GET     (101L)
#define IVISWTCH_VAL_SW_TRIG_FUNC (3L)

#define IVISWTCH_VAL_TRIGGER_SPECIFIC_EXT_BASE        (1000L)

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviSwtch_GetErrorInfo (ViSession vi, 
                                         ViStatus *primaryError, 
                                         ViStatus *secondaryError, 
                                         ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC IviSwtch_ClearErrorInfo (ViSession vi);

    /*- IviSwtch Obsolete Functions -*/
ViStatus _VI_FUNC   IviSwtch_SendSWTrigger          (ViSession vi);

/*****************************************************************************
 *---------------------------- End Include File -----------------------------*
 *****************************************************************************/

#endif /* IVISWTCH_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviUpconverter_ni.h sha256=d17de8047212987a7c03956762b05d7b2be8fb8216db5d58fad5a8de9edc878f bytes=44349 -->
## FILE: imports/include/IviUpconverter_ni.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviUpconverter_ni.h`
- sha256: `d17de8047212987a7c03956762b05d7b2be8fb8216db5d58fad5a8de9edc878f`
- bytes: 44349

````c
/****************************************************************************
 *                              IVI - UPCONVERTER                               
 *---------------------------------------------------------------------------
 *    Copyright (c) 2009-2020 National Instruments.  All Rights Reserved.        
 *---------------------------------------------------------------------------
 *                                                                          
 * Title:       iviupconverter_ni.h                                                    
 * Purpose:     IviUpconverter Class declarations for the Base and Extended  
 *              IviUpconverter Capabilities.                                        
 ****************************************************************************/

#ifndef IVIUPCONVERTER_HEADER
#define IVIUPCONVERTER_HEADER

#include <ivi.h>

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/

#define IVIUPCONVERTER_MAJOR_VERSION		          (4L)
#define IVIUPCONVERTER_MINOR_VERSION	              (0L)

#define IVIUPCONVERTER_CLASS_SPEC_MAJOR_VERSION	      (2L)
#define IVIUPCONVERTER_CLASS_SPEC_MINOR_VERSION	      (0L)

#define IVIUPCONVERTER_DRIVER_VENDOR	              "National Instruments"
#ifdef	_IVI_mswin64_
#define IVIUPCONVERTER_DRIVER_DESCRIPTION			  "IviUpconverter Class Driver [Compiled for 64-bit.]"
#else
#define IVIUPCONVERTER_DRIVER_DESCRIPTION	          "IviUpconverter Class Driver"
#endif

/****************************************************************************
 *------------------------------ Useful Macros -----------------------------*
 ****************************************************************************/

  
/****************************************************************************
 *---------------- IviUpconverter Class Attribute Defines ------------------*
 ****************************************************************************/

    /*- IVI Inherent Attributes -*/

        /*- User Options -*/
#define IVIUPCONVERTER_ATTR_CACHE	                    IVI_ATTR_CACHE                       /* ViBoolean */
#define IVIUPCONVERTER_ATTR_RANGE_CHECK	                IVI_ATTR_RANGE_CHECK                 /* ViBoolean */
#define IVIUPCONVERTER_ATTR_QUERY_INSTRUMENT_STATUS		IVI_ATTR_QUERY_INSTRUMENT_STATUS     /* ViBoolean */
#define IVIUPCONVERTER_ATTR_RECORD_COERCIONS			IVI_ATTR_RECORD_COERCIONS            /* ViBoolean */
#define IVIUPCONVERTER_ATTR_SIMULATE					IVI_ATTR_SIMULATE                    /* ViBoolean */
#define IVIUPCONVERTER_ATTR_INTERCHANGE_CHECK			IVI_ATTR_INTERCHANGE_CHECK           /* ViBoolean */
#define IVIUPCONVERTER_ATTR_SPY							IVI_ATTR_SPY                         /* ViBoolean */
#define IVIUPCONVERTER_ATTR_USE_SPECIFIC_SIMULATION		IVI_ATTR_USE_SPECIFIC_SIMULATION     /* ViBoolean */

        /*- Instrument Capabilities -*/
#define IVIUPCONVERTER_ATTR_GROUP_CAPABILITIES			IVI_ATTR_GROUP_CAPABILITIES          /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_FUNCTION_CAPABILITIES		IVI_ATTR_FUNCTION_CAPABILITIES       /* ViString, read-only */

        /*- Class Driver Information -*/    
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_PREFIX						  IVI_ATTR_CLASS_DRIVER_PREFIX         			  /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_VENDOR		                  IVI_ATTR_CLASS_DRIVER_VENDOR         			  /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_DESCRIPTION	              IVI_ATTR_CLASS_DRIVER_DESCRIPTION    			  /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION	  IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION	  IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Specific Driver Information -*/    
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_PREFIX	                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX      				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_LOCATOR		                  IVI_ATTR_SPECIFIC_DRIVER_LOCATOR     				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_IO_RESOURCE_DESCRIPTOR	                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR      				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_LOGICAL_NAME	                              IVI_ATTR_LOGICAL_NAME                				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_VENDOR	                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR      				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_DESCRIPTION		              IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION 				 /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION	  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32,  read-only */
#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION	  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32,  read-only */

        /*- Instrument Information -*/    
#define IVIUPCONVERTER_ATTR_INSTRUMENT_FIRMWARE_REVISION	   IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_INSTRUMENT_MANUFACTURER		       IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_INSTRUMENT_MODEL	               IVI_ATTR_INSTRUMENT_MODEL             /* ViString, read-only */
#define IVIUPCONVERTER_ATTR_SUPPORTED_INSTRUMENT_MODELS		   IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS	 /* ViString, read-only */

        /*- Version Information -*/
#define IVIUPCONVERTER_ATTR_CLASS_DRIVER_REVISION		       IVI_ATTR_CLASS_DRIVER_REVISION        /* ViString, read-only */

#define IVIUPCONVERTER_ATTR_SPECIFIC_DRIVER_REVISION	       IVI_ATTR_SPECIFIC_DRIVER_REVISION     /* ViString, read-only */

        /*- Driver Setup Information -*/
#define IVIUPCONVERTER_ATTR_DRIVER_SETUP		         	   IVI_ATTR_DRIVER_SETUP                 /* ViString */

    /*- IviUpconverter Fundamental Attributes -*/
#define IVIUPCONVERTER_ATTR_ACTIVE_IF_INPUT                  			(IVI_CLASS_PUBLIC_ATTR_BASE + 0L)    /* ViString */
#define IVIUPCONVERTER_ATTR_ACTIVE_RF_OUTPUT				            (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)    /* ViString */
#define IVIUPCONVERTER_ATTR_ALC_ENABLED									(IVI_CLASS_PUBLIC_ATTR_BASE + 2L)	 /* ViBoolean*/	
#define IVIUPCONVERTER_ATTR_AUTO_CORRECTIONS_ENABLED				    (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_EXTERNAL_LO_ENABLED							(IVI_CLASS_PUBLIC_ATTR_BASE + 4L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_EXTERNAL_LO_FREQUENCY						(IVI_CLASS_PUBLIC_ATTR_BASE + 5L)	 /* ViReal64 */	
#define IVIUPCONVERTER_ATTR_IF_INPUT_ATTENUATION						(IVI_CLASS_PUBLIC_ATTR_BASE + 6L)	 /* ViReal64 */ 
#define IVIUPCONVERTER_ATTR_IF_INPUT_COUNT								(IVI_CLASS_PUBLIC_ATTR_BASE + 7L)	 /* ViInt32,  read-only */
#define IVIUPCONVERTER_ATTR_IF_INPUT_COUPLING							(IVI_CLASS_PUBLIC_ATTR_BASE + 8L)	 /* ViInt32  */	 
#define IVIUPCONVERTER_ATTR_IF_INPUT_FREQUENCY							(IVI_CLASS_PUBLIC_ATTR_BASE + 9L)	 /* ViReal64, read-only */
#define IVIUPCONVERTER_ATTR_IS_READY									(IVI_CLASS_PUBLIC_ATTR_BASE + 10L)	 /* ViBoolean,read-only */
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_BANDWIDTH							(IVI_CLASS_PUBLIC_ATTR_BASE + 11L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_COUNT								(IVI_CLASS_PUBLIC_ATTR_BASE + 12L)	 /* ViInt32,  read-only */
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_ENABLED							(IVI_CLASS_PUBLIC_ATTR_BASE + 13L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_FREQUENCY							(IVI_CLASS_PUBLIC_ATTR_BASE + 14L)	 /* ViReal64 */

    /*- IviUpconverterOutputGain Attributes -*/
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_GAIN								(IVI_CLASS_PUBLIC_ATTR_BASE + 100L)	 /* ViReal64 */	

    /*- IviUpconverterOutputPowerLevel Attributes -*/
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_LEVEL								(IVI_CLASS_PUBLIC_ATTR_BASE + 110L)	 /* ViReal64 */

	/*- IviUpconverterModulateAM Attributes -*/
#define IVIUPCONVERTER_ATTR_AM_DEPTH									(IVI_CLASS_PUBLIC_ATTR_BASE + 120L)	 /*	ViReal64 */
#define IVIUPCONVERTER_ATTR_AM_ENABLED									(IVI_CLASS_PUBLIC_ATTR_BASE + 121L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_AM_EXTERNAL_COUPLING						(IVI_CLASS_PUBLIC_ATTR_BASE + 122L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_AM_NOMINAL_VOLTAGE							(IVI_CLASS_PUBLIC_ATTR_BASE + 123L)	 /* ViReal64, read-only */
#define IVIUPCONVERTER_ATTR_AM_SCALING									(IVI_CLASS_PUBLIC_ATTR_BASE + 124L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_AM_SOURCE									(IVI_CLASS_PUBLIC_ATTR_BASE + 125L)	 /* ViString */

    /*- IviUpconverterModulateFM Attributes -*/
#define IVIUPCONVERTER_ATTR_FM_DEVIATION								(IVI_CLASS_PUBLIC_ATTR_BASE + 130L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FM_ENABLED									(IVI_CLASS_PUBLIC_ATTR_BASE + 131L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_FM_EXTERNAL_COUPLING						(IVI_CLASS_PUBLIC_ATTR_BASE + 132L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_FM_NOMINAL_VOLTAGE							(IVI_CLASS_PUBLIC_ATTR_BASE + 133L)	 /* ViReal64, read-only */
#define IVIUPCONVERTER_ATTR_FM_SOURCE									(IVI_CLASS_PUBLIC_ATTR_BASE + 134L)	 /* ViString */

	/*- IviUpconverterModulatePM Attributes -*/
#define IVIUPCONVERTER_ATTR_PM_DEVIATION								(IVI_CLASS_PUBLIC_ATTR_BASE + 140L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_PM_ENABLED									(IVI_CLASS_PUBLIC_ATTR_BASE + 141L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_PM_EXTERNAL_COUPLING						(IVI_CLASS_PUBLIC_ATTR_BASE + 142L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_PM_NOMINAL_VOLTAGE							(IVI_CLASS_PUBLIC_ATTR_BASE + 143L)	 /* ViReal64, read-only */
#define IVIUPCONVERTER_ATTR_PM_SOURCE									(IVI_CLASS_PUBLIC_ATTR_BASE + 144L)	 /* ViString */

    /*- IviUpconverterAnalogModulationSource Attributes -*/
#define IVIUPCONVERTER_ATTR_ANALOG_MODULATION_SOURCE_COUNT		        (IVI_CLASS_PUBLIC_ATTR_BASE + 150L)  /* ViInt32,  read-only */

	/*- IviUpconverterModulatePulse Attributes -*/
#define IVIUPCONVERTER_ATTR_PULSE_MODULATION_ENABLED					(IVI_CLASS_PUBLIC_ATTR_BASE + 160L)	 /* ViBoolean*/	
#define IVIUPCONVERTER_ATTR_PULSE_MODULATION_EXTERNAL_POLARITY			(IVI_CLASS_PUBLIC_ATTR_BASE + 161L)	 /* ViInt32  */

	/*- IviUpconverterBypass Attributes -*/
#define IVIUPCONVERTER_ATTR_BYPASS										(IVI_CLASS_PUBLIC_ATTR_BASE + 170L)	 /* ViBoolean*/

	/*- IviUpconverterOutputReadyTrigger Attributes -*/
#define IVIUPCONVERTER_ATTR_RF_OUTPUT_READY_TRIGGER						(IVI_CLASS_PUBLIC_ATTR_BASE + 180L)	 /* ViString */

	/*- IviUpconverterSweep Attributes -*/
#define IVIUPCONVERTER_ATTR_IS_SWEEPING									(IVI_CLASS_PUBLIC_ATTR_BASE + 200L)	 /* ViBoolean,read-only */
#define IVIUPCONVERTER_ATTR_SWEEP_MODE									(IVI_CLASS_PUBLIC_ATTR_BASE + 201L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_SWEEP_TRIGGER_SOURCE						(IVI_CLASS_PUBLIC_ATTR_BASE + 202L)  /* ViString */

    /*- IviUpconverterFrequencySweep Attributes -*/
#define IVIUPCONVERTER_ATTR_FREQUENCY_SWEEP_START						(IVI_CLASS_PUBLIC_ATTR_BASE + 210L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FREQUENCY_SWEEP_STOP						(IVI_CLASS_PUBLIC_ATTR_BASE + 211L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FREQUENCY_SWEEP_TIME						(IVI_CLASS_PUBLIC_ATTR_BASE + 212L)	 /* ViReal64 */

    /*- IviUpconverterPowerSweep Attributes -*/
#define IVIUPCONVERTER_ATTR_POWER_SWEEP_START							(IVI_CLASS_PUBLIC_ATTR_BASE + 220L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_POWER_SWEEP_STOP							(IVI_CLASS_PUBLIC_ATTR_BASE + 221L)  /* ViReal64 */
#define IVIUPCONVERTER_ATTR_POWER_SWEEP_TIME							(IVI_CLASS_PUBLIC_ATTR_BASE + 222L)	 /* ViReal64 */

    /*- IviUpconverterGainSweep Attributes -*/
#define IVIUPCONVERTER_ATTR_GAIN_SWEEP_START							(IVI_CLASS_PUBLIC_ATTR_BASE + 230L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_GAIN_SWEEP_STOP								(IVI_CLASS_PUBLIC_ATTR_BASE + 231L)  /* ViReal64 */
#define IVIUPCONVERTER_ATTR_GAIN_SWEEP_TIME								(IVI_CLASS_PUBLIC_ATTR_BASE + 232L)	 /* ViReal64 */

    /*- IviUpconverterFrequencyStep Attributes -*/
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_DWELL						(IVI_CLASS_PUBLIC_ATTR_BASE + 240L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_SCALING						(IVI_CLASS_PUBLIC_ATTR_BASE + 241L)	 /* ViInt32  */
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_SINGLE_STEP_ENABLED			(IVI_CLASS_PUBLIC_ATTR_BASE + 242L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_SIZE							(IVI_CLASS_PUBLIC_ATTR_BASE + 243L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_START						(IVI_CLASS_PUBLIC_ATTR_BASE + 244L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_FREQUENCY_STEP_STOP							(IVI_CLASS_PUBLIC_ATTR_BASE + 245L)	 /* ViReal64 */

    /*- IviUpconverterPowerStep Attributes -*/
#define IVIUPCONVERTER_ATTR_POWER_STEP_DWELL							(IVI_CLASS_PUBLIC_ATTR_BASE + 250L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_POWER_STEP_SINGLE_STEP_ENABLED				(IVI_CLASS_PUBLIC_ATTR_BASE + 251L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_POWER_STEP_SIZE								(IVI_CLASS_PUBLIC_ATTR_BASE + 252L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_POWER_STEP_START							(IVI_CLASS_PUBLIC_ATTR_BASE + 253L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_POWER_STEP_STOP								(IVI_CLASS_PUBLIC_ATTR_BASE + 254L)	 /* ViReal64 */

    /*- IviUpconverterGainStep Attributes -*/
#define IVIUPCONVERTER_ATTR_GAIN_STEP_DWELL								(IVI_CLASS_PUBLIC_ATTR_BASE + 260L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_GAIN_STEP_SINGLE_STEP_ENABLED				(IVI_CLASS_PUBLIC_ATTR_BASE + 261L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_GAIN_STEP_SIZE								(IVI_CLASS_PUBLIC_ATTR_BASE + 262L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_GAIN_STEP_START								(IVI_CLASS_PUBLIC_ATTR_BASE + 263L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_GAIN_STEP_STOP								(IVI_CLASS_PUBLIC_ATTR_BASE + 264L)	 /* ViReal64 */

    /*- IviUpconverterList Attributes -*/
#define IVIUPCONVERTER_ATTR_LIST_DWELL									(IVI_CLASS_PUBLIC_ATTR_BASE + 270L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_LIST_SELECTED_NAME							(IVI_CLASS_PUBLIC_ATTR_BASE + 271L)  /* ViString */
#define IVIUPCONVERTER_ATTR_LIST_SINGLE_STEP_ENABLED					(IVI_CLASS_PUBLIC_ATTR_BASE + 272L)	 /* ViBoolean*/

    /*- IviUpconverterALC Attributes -*/
#define IVIUPCONVERTER_ATTR_ALC_BANDWIDTH								(IVI_CLASS_PUBLIC_ATTR_BASE + 300L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_ALC_SOURCE									(IVI_CLASS_PUBLIC_ATTR_BASE + 301L)	 /* ViInt32  */

	/*- IviUpconverterAttenuatorHold Attributes -*/
#define IVIUPCONVERTER_ATTR_ATTENUATOR_HOLD_ENABLED						(IVI_CLASS_PUBLIC_ATTR_BASE + 310L)	 /* ViBoolean*/

    /*- IviUpconverterReferenceOscillator Attributes -*/
#define IVIUPCONVERTER_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY		(IVI_CLASS_PUBLIC_ATTR_BASE + 320L)  /* ViReal64 */
#define IVIUPCONVERTER_ATTR_REFERENCE_OSCILLATOR_SOURCE		            (IVI_CLASS_PUBLIC_ATTR_BASE + 321L)  /* ViInt32  */
#define IVIUPCONVERTER_ATTR_REFERENCE_OSCILLATOR_OUTPUT_ENABLED			(IVI_CLASS_PUBLIC_ATTR_BASE + 322L)	 /* ViBoolean*/

	/*- IviUpconverterModulateIQ Attributes -*/
#define IVIUPCONVERTER_ATTR_IQ_ENABLED									(IVI_CLASS_PUBLIC_ATTR_BASE + 330L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_IQ_NOMINAL_VOLTAGE							(IVI_CLASS_PUBLIC_ATTR_BASE + 331L)	 /* ViReal64, read-only */
#define IVIUPCONVERTER_ATTR_IQ_SWAP_ENABLED								(IVI_CLASS_PUBLIC_ATTR_BASE + 332L)	 /* ViBoolean*/

	/*- IviUpconverterIQImpairment Attributes -*/
#define IVIUPCONVERTER_ATTR_IQ_IMPAIRMENT_ENABLED						(IVI_CLASS_PUBLIC_ATTR_BASE + 340L)	 /* ViBoolean*/
#define IVIUPCONVERTER_ATTR_IQ_IMPAIRMENT_I_OFFSET						(IVI_CLASS_PUBLIC_ATTR_BASE + 341L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_IQ_IMPAIRMENT_Q_OFFSET						(IVI_CLASS_PUBLIC_ATTR_BASE + 342L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_IQ_IMPAIRMENT_RATIO							(IVI_CLASS_PUBLIC_ATTR_BASE + 343L)	 /* ViReal64 */
#define IVIUPCONVERTER_ATTR_IQ_IMPAIRMENT_SKEW							(IVI_CLASS_PUBLIC_ATTR_BASE + 344L)	 /* ViReal64 */

/****************************************************************************
 *--------------- IviUpconverter Class Attribute Value Defines -------------*
 ****************************************************************************/

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_ALC_SOURCE -*/
#define IVIUPCONVERTER_VAL_ALC_SOURCE_INTERNAL									(0L)
#define IVIUPCONVERTER_VAL_ALC_SOURCE_EXTERNAL									(1L)

#define IVIUPCONVERTER_VAL_ALC_SOURCE_CLASS_EXT_BASE							(100L)
#define IVIUPCONVERTER_VAL_ALC_SOURCE_SPECIFIC_EXT_BASE							(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_AM_EXTERNAL_COUPLING -*/
#define IVIUPCONVERTER_VAL_AM_EXTERNAL_COUPLING_AC								(0L)
#define IVIUPCONVERTER_VAL_AM_EXTERNAL_COUPLING_DC								(1L)

#define IVIUPCONVERTER_VAL_AM_EXTERNAL_COUPLING_CLASS_EXT_BASE					(100L)
#define IVIUPCONVERTER_VAL_AM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE				(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_AM_SCALING -*/
#define IVIUPCONVERTER_VAL_AM_SCALING_LINEAR									(0L)
#define IVIUPCONVERTER_VAL_AM_SCALING_LOGARITHMIC								(1L)

#define IVIUPCONVERTER_VAL_AM_SCALING_CLASS_EXT_BASE							(100L)
#define IVIUPCONVERTER_VAL_AM_SCALING_SPECIFIC_EXT_BASE							(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_FM_EXTERNAL_COUPLING -*/
#define IVIUPCONVERTER_VAL_FM_EXTERNAL_COUPLING_AC								(0L)
#define IVIUPCONVERTER_VAL_FM_EXTERNAL_COUPLING_DC								(1L)

#define IVIUPCONVERTER_VAL_FM_EXTERNAL_COUPLING_CLASS_EXT_BASE					(100L)
#define IVIUPCONVERTER_VAL_FM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE				(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_FREQUENCY_STEP_SCALING -*/
#define IVIUPCONVERTER_VAL_FREQUENCY_STEP_SCALING_LINEAR						(0L)
#define IVIUPCONVERTER_VAL_FREQUENCY_STEP_SCALING_LOGARITHMIC					(1L)

#define IVIUPCONVERTER_VAL_FREQUENCY_STEP_SCALING_CLASS_EXT_BASE				(100L)
#define IVIUPCONVERTER_VAL_FREQUENCY_STEP_SCALING_SPECIFIC_EXT_BASE				(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_PM_EXTERNAL_COUPLING -*/
#define IVIUPCONVERTER_VAL_PM_EXTERNAL_COUPLING_AC								(0L)
#define IVIUPCONVERTER_VAL_PM_EXTERNAL_COUPLING_DC								(1L)

#define IVIUPCONVERTER_VAL_PM_EXTERNAL_COUPLING_CLASS_EXT_BASE					(100L)
#define IVIUPCONVERTER_VAL_PM_EXTERNAL_COUPLING_SPECIFIC_EXT_BASE				(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_PULSE_MODULATION_EXTERNAL_POLARITY -*/
#define IVIUPCONVERTER_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_NORMAL			(0L)
#define IVIUPCONVERTER_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_INVERSE			(1L)

#define IVIUPCONVERTER_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_CLASS_EXT_BASE	(100L)
#define IVIUPCONVERTER_VAL_PULSE_MODULATION_EXTERNAL_POLARITY_SPECIFIC_EXT_BASE	(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_REFERENCE_OSCILLATOR_SOURCE -*/
#define IVIUPCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL					(0L)
#define IVIUPCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL					(1L)

#define IVIUPCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_CLASS_EXT_BASE			(100L)
#define IVIUPCONVERTER_VAL_REFERENCE_OSCILLATOR_SOURCE_SPECIFIC_EXT_BASE		(1000L)

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_SWEEP_MODE -*/
#define IVIUPCONVERTER_VAL_SWEEP_MODE_NONE										(0L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_FREQUENCY_SWEEP							(1L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_POWER_SWEEP								(2L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_GAIN_SWEEP								(3L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_FREQUENCY_STEP							(4L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_POWER_STEP								(5L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_GAIN_STEP									(6L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_LIST										(7L)

#define IVIUPCONVERTER_VAL_SWEEP_MODE_CLASS_EXT_BASE							(100L)
#define IVIUPCONVERTER_VAL_SWEEP_MODE_SPECIFIC_EXT_BASE							(1000L)

    /*- Defined values for attributes IVIUPCONVERTER_ATTR_RF_OUTPUT_READY_TRIGGER and IVIUPCONVERTER_ATTR_SWEEP_TRIGGER_SOURCE -*/
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_NONE									""
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_IMMEDIATE								"Immediate"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_EXTERNAL								"External"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_INTERNAL								"Internal"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_SOFTWARE								"Software"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN0									"LAN0"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN1									"LAN1"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN2									"LAN2"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN3									"LAN3"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN4									"LAN4"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN5									"LAN5"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN6									"LAN6"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LAN7									"LAN7"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI0									"LXI0"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI1									"LXI1"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI2									"LXI2"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI3									"LXI3"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI4									"LXI4"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI5									"LXI5"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI6									"LXI6"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_LXI7									"LXI7"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL0									"TTL0"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL1									"TTL1"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL2									"TTL2"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL3									"TTL3"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL4									"TTL4"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL5									"TTL5"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL6									"TTL6"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_TTL7									"TTL7"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_STAR								"PXI_STAR"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG0								"PXI_TRIG0"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG1								"PXI_TRIG1"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG2								"PXI_TRIG2"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG3								"PXI_TRIG3"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG4								"PXI_TRIG4"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG5								"PXI_TRIG5"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG6								"PXI_TRIG6"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXI_TRIG7								"PXI_TRIG7"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARA						    "PXIe_DSTARA"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARB						    "PXIe_DSTARB"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_PXIE_DSTARC						    "PXIe_DSTARC"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI0									"RTSI0"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI1									"RTSI1"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI2									"RTSI2"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI3									"RTSI3"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI4									"RTSI4"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI5									"RTSI5"
#define IVIUPCONVERTER_VAL_TRIGGER_SOURCE_RTSI6									"RTSI6"

    /*- Defined values for attribute IVIUPCONVERTER_ATTR_IF_INPUT_COUPLING -*/
#define IVIUPCONVERTER_VAL_IF_INPUT_COUPLING_AC			                       (0L)
#define IVIUPCONVERTER_VAL_IF_INPUT_COUPLING_DC	                       		   (1L)

#define IVIUPCONVERTER_VAL_INPUT_COUPLING_CLASS_EXT_BASE					   (100L)
#define IVIUPCONVERTER_VAL_INPUT_COUPLING_SPECIFIC_EXT_BASE					   (1000L)

#define IVIUPCONVERTER_VAL_CALIBRATION_COMPLETE		   						   (0L)
#define IVIUPCONVERTER_VAL_CALIBRATION_IN_PROGRESS							   (1L)
#define IVIUPCONVERTER_VAL_CALIBRATION_STATUS_UNKNOWN						   (2L)
#define IVIUPCONVERTER_VAL_CALIBRATION_FAILED	         					   (3L)

#define IVIUPCONVERTER_VAL_MAX_TIME_IMMEDIATE								   (IVI_VAL_MAX_TIME_IMMEDIATE)
#define IVIUPCONVERTER_VAL_MAX_TIME_INFINITE								   (IVI_VAL_MAX_TIME_INFINITE)

/****************************************************************************
 *------- IviUpconverter Class Instrument Driver Function Declarations -----*
 ****************************************************************************/
    /*- Required VXIplug&play Functions -*/
ViStatus _VI_FUNC IviUpconverter_init (ViRsrc logicalName, 
                               		   ViBoolean idQuery, 
                               		   ViBoolean resetDevice, 
                               		   ViSession *vi);

ViStatus _VI_FUNC IviUpconverter_close (ViSession vi);

ViStatus _VI_FUNC IviUpconverter_reset (ViSession vi);

ViStatus _VI_FUNC IviUpconverter_self_test (ViSession vi, 
                                    		ViInt16 *selfTestResult, 
                                    		ViChar selfTestMessage[]);

ViStatus _VI_FUNC IviUpconverter_error_query (ViSession vi, 
                                      		  ViInt32 *errorCode, 
                                      		  ViChar errorMessage[]);

ViStatus _VI_FUNC IviUpconverter_error_message (ViSession vi, 
                                        		ViStatus statusCode, 
                                        		ViChar message[]);

ViStatus _VI_FUNC IviUpconverter_revision_query (ViSession vi, 
                                         		 ViChar driverRev[], 
                                         		 ViChar instrRev[]);

    /*- Utility Functions -*/
ViStatus _VI_FUNC IviUpconverter_InvalidateAllAttributes (ViSession vi);

ViStatus _VI_FUNC IviUpconverter_ResetWithDefaults (ViSession vi);

ViStatus _VI_FUNC IviUpconverter_Disable (ViSession vi);

    /*- Required IVI Functions -*/
ViStatus _VI_FUNC IviUpconverter_InitWithOptions (ViRsrc logicalName, 
                                          		  ViBoolean IDQuery,
                                          		  ViBoolean resetDevice, 
                                          		  ViConstString optionString, 
                                          		  ViSession *vi);

    /*- Set, Get, and Check Attribute Functions -*/
ViStatus _VI_FUNC IviUpconverter_GetAttributeViInt32 (ViSession vi, 
                                              		  ViConstString channelName,
                                              		  ViAttr attributeId,
                                              		  ViInt32 *value);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViInt32 (ViSession vi, 
                                              		  ViConstString channelName,
                                              		  ViAttr attributeId,
                                              		  ViInt32 value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViInt32 (ViSession vi, 
                                                		ViConstString channelName,
                                                		ViAttr attributeId,
                                                		ViInt32 value);

#ifdef _IVI_64BIT_ATTR_DEFINED_
ViStatus _VI_FUNC IviUpconverter_GetAttributeViInt64 (ViSession vi, 
                                              		  ViConstString channelName,
                                              		  ViAttr attributeId,
                                              		  ViInt64 *value);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViInt64 (ViSession vi, 
                                              		  ViConstString channelName,
                                              		  ViAttr attributeId,
                                              		  ViInt64 value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViInt64 (ViSession vi, 
                                                		ViConstString channelName,
                                                		ViAttr attributeId,
                                                		ViInt64 value);
#endif

ViStatus _VI_FUNC IviUpconverter_GetAttributeViReal64 (ViSession vi, 
                                               		   ViConstString channelName, 
                                               		   ViAttr attributeId, 
                                               		   ViReal64 *value);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViReal64 (ViSession vi, 
                                               		   ViConstString channelName, 
                                               		   ViAttr attributeId, 
                                               		   ViReal64 value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViReal64 (ViSession vi, 
                                                 		 ViConstString channelName, 
                                                 		 ViAttr attributeId, 
                                                 		 ViReal64 value);

ViStatus _VI_FUNC IviUpconverter_GetAttributeViString (ViSession vi, 
                                               		   ViConstString channelName, 
                                               		   ViAttr attributeId, 
                                               		   ViInt32 bufferSize, 
                                               		   ViChar value[]);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViString (ViSession vi, 
                                               		   ViConstString channelName, 
                                               		   ViAttr attributeId, 
                                               		   ViConstString value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViString (ViSession vi, 
                                                 		 ViConstString channelName, 
                                                 		 ViAttr attributeId, 
                                                 		 ViConstString value); 

ViStatus _VI_FUNC IviUpconverter_GetAttributeViBoolean (ViSession vi, 
                                                		ViConstString channelName, 
                                                		ViAttr attributeId, 
                                                		ViBoolean *value);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViBoolean (ViSession vi, 
                                                		ViConstString channelName, 
                                                		ViAttr attributeId, 
                                                		ViBoolean value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViBoolean (ViSession vi, 
                                                  		  ViConstString channelName, 
                                                  		  ViAttr attributeId, 
                                                  		  ViBoolean value);

ViStatus _VI_FUNC IviUpconverter_GetAttributeViSession (ViSession vi, 
                                                		ViConstString channelName, 
                                                		ViAttr attributeId, 
                                                		ViSession *value);

ViStatus _VI_FUNC IviUpconverter_SetAttributeViSession (ViSession vi, 
                                                		ViConstString channelName, 
                                                		ViAttr attributeId, 
                                                		ViSession value);

ViStatus _VI_FUNC IviUpconverter_CheckAttributeViSession (ViSession vi, 
                                                  		  ViConstString channelName, 
                                                  		  ViAttr attributeId, 
                                                  		  ViSession value);

    /*- Lock and Unlock Functions -*/
ViStatus _VI_FUNC IviUpconverter_LockSession (ViSession vi, 
                                      		  ViBoolean *callerHasLock);

ViStatus _VI_FUNC IviUpconverter_UnlockSession (ViSession vi, 
                                        		ViBoolean *callerHasLock);

    /*- Error Information Functions -*/
ViStatus _VI_FUNC IviUpconverter_GetError (ViSession vi, 
                                   		   ViStatus *errorCode, 
                                   		   ViInt32 bufferSize, 
                                   		   ViChar description[]);

ViStatus _VI_FUNC IviUpconverter_ClearError (ViSession vi);

    /*- Interchangeability Checking Functions -*/
ViStatus _VI_FUNC IviUpconverter_GetNextInterchangeWarning (ViSession vi, 
                                                    		ViInt32 bufferSize,
                                                    		ViChar warning[]);

ViStatus _VI_FUNC IviUpconverter_ClearInterchangeWarnings (ViSession vi);
ViStatus _VI_FUNC IviUpconverter_ResetInterchangeCheck (ViSession vi);

ViStatus _VI_FUNC IviUpconverter_GetNextCoercionRecord (ViSession vi,
                                                		ViInt32 bufferSize, 
                                                		ViChar record[]);

ViStatus _VI_FUNC IviUpconverter_GetSpecificDriverCHandle (ViSession vi,
                                                   		   ViSession* specificDriverCHandle);

    /*- IviUpconverterBase Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureIFInputAttenuation (ViSession vi, 
                                                 			    ViReal64 attenuation);

ViStatus _VI_FUNC   IviUpconverter_ConfigureRFOutputEnabled (ViSession vi, 
															 ViBoolean enabled);

ViStatus _VI_FUNC   IviUpconverter_ConfigureRFOutputFrequency (ViSession vi, 
															   ViReal64 frequency);

ViStatus _VI_FUNC   IviUpconverter_GetIFInputName (ViSession vi, 
												   ViInt32 index,
												   ViInt32 nameBufferSize,
												   ViChar name[]);

ViStatus _VI_FUNC   IviUpconverter_GetRFOutputName (ViSession vi, 
													ViInt32 index,
													ViInt32 nameBufferSize,
													ViChar name[]);

ViStatus _VI_FUNC   IviUpconverter_SetActiveIFInput (ViSession vi, 
													 ViConstString name);

ViStatus _VI_FUNC	IviUpconverter_SetActiveRFOutput (ViSession vi, 
													  ViConstString name);

ViStatus _VI_FUNC	IviUpconverter_WaitUntilReady (ViSession vi,
												   ViInt32 maxTimeMilliseconds);

    /*- IviUpconverterOutputGain Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureRFOutputGain (ViSession vi, 
														  ViReal64 gain);
    
    /*- IviUpconverterOutputPowerLevel Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureRFOutputLevel (ViSession vi, 
														   ViReal64 level);

    /*- IviUpconverterModulateAM Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureAM (ViSession vi, 
												ViConstString source,
												ViInt32 scaling,
												ViReal64 depth);

ViStatus _VI_FUNC	IviUpconverter_ConfigureAMEnabled (ViSession vi,
													   ViBoolean enabled);

ViStatus _VI_FUNC	IviUpconverter_ConfigureAMExternalCoupling (ViSession vi,
																ViInt32 coupling);

    /*- IviUpconverterModulateFM Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureFM (ViSession vi, 
												ViConstString source,
												ViReal64 deviation);

ViStatus _VI_FUNC   IviUpconverter_ConfigureFMEnabled (ViSession vi, 
													   ViBoolean enabled);

ViStatus _VI_FUNC	IviUpconverter_ConfigureFMExternalCoupling (ViSession vi,
																ViInt32 coupling);

	/*- IviUpconverterModulatePM Functions -*/
ViStatus _VI_FUNC	IviUpconverter_ConfigurePM (ViSession vi,
												ViConstString source,
												ViReal64 deviation);

ViStatus _VI_FUNC   IviUpconverter_ConfigurePMEnabled (ViSession vi, 
													   ViBoolean enabled);

ViStatus _VI_FUNC	IviUpconverter_ConfigurePMExternalCoupling (ViSession vi,
																ViInt32 coupling);

    /*- IviUpconverterAnalogModulationSource Functions -*/
ViStatus _VI_FUNC   IviUpconverter_GetAnalogModulationSourceName (ViSession vi,
																  ViInt32 index,
																  ViInt32 nameBufferSize,
																  ViChar name[]);

	/*- IviUpconverterModulatePulse Functions -*/
ViStatus _VI_FUNC	IviUpconverter_ConfigurePulseModulationEnabled (ViSession vi,
																	ViBoolean enabled);

ViStatus _VI_FUNC	IviUpconverter_ConfigurePulseModulationExternalPolarity (ViSession vi,
																			 ViInt32 polarity);

	/*- IviUpconverterBypass Functions -*/
ViStatus _VI_FUNC	IviUpconverter_ConfigureBypass (ViSession vi,
													ViBoolean bypass);

    /*- IviUpconverterOutputReadyTrigger Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureRFOutputReadyTrigger (ViSession vi, 
																  ViConstString outputTrigger);

    /*- IviUpconverterSweep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureSweep (ViSession vi,
												   ViInt32 mode,
												   ViConstString triggerSource);

    /*- IviUpconverterFrequencySweep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureFrequencySweepCenterSpan (ViSession vi, 
																	  ViReal64 center,
																	  ViReal64 span);

ViStatus _VI_FUNC   IviUpconverter_ConfigureFrequencySweepStartStop (ViSession vi, 
																	 ViReal64 start,
																	 ViReal64 stop);

ViStatus _VI_FUNC   IviUpconverter_ConfigureFrequencySweepTime (ViSession vi, 
																ViReal64 sweepTime);

    /*- IviUpconverterPowerSweep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigurePowerSweepStartStop (ViSession vi, 
																 ViReal64 start,
																 ViReal64 stop);

ViStatus _VI_FUNC   IviUpconverter_ConfigurePowerSweepTime (ViSession vi, 
															ViReal64 sweepTime);

    /*- IviUpconverterGainSweep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureGainSweepStartStop (ViSession vi, 
																ViReal64 start,
																ViReal64 stop);

ViStatus _VI_FUNC   IviUpconverter_ConfigureGainSweepTime (ViSession vi, 
														   ViReal64 sweepTime);

	/*- IviUpconverterFrequencyStep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureFrequencyStepDwell (ViSession vi, 
																ViBoolean singleStepEnabled, 
																ViReal64 dwell);

ViStatus _VI_FUNC   IviUpconverter_ConfigureFrequencyStepStartStop (ViSession vi, 
																	ViReal64 start,
																	ViReal64 stop,
																	ViInt32 scaling,
																	ViReal64 stepSize);

ViStatus _VI_FUNC   IviUpconverter_ResetFrequencyStep (ViSession vi);

	/*- IviUpconverterPowerStep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigurePowerStepDwell (ViSession vi, 
															ViBoolean singleStepEnabled, 
															ViReal64 dwell);

ViStatus _VI_FUNC   IviUpconverter_ConfigurePowerStepStartStop (ViSession vi, 
																ViReal64 start,
																ViReal64 stop,
																ViReal64 stepSize);

ViStatus _VI_FUNC   IviUpconverter_ResetPowerStep (ViSession vi);

	/*- IviUpconverterGainStep Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureGainStepDwell (ViSession vi, 
														   ViBoolean singleStepEnabled, 
														   ViReal64 dwell);

ViStatus _VI_FUNC   IviUpconverter_ConfigureGainStepStartStop (ViSession vi, 
															   ViReal64 start,
															   ViReal64 stop,
															   ViReal64 stepSize);

ViStatus _VI_FUNC   IviUpconverter_ResetGainStep (ViSession vi);

	/*- IviUpconverterList Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ClearAllLists (ViSession vi);

ViStatus _VI_FUNC   IviUpconverter_ConfigureListDwell (ViSession vi,
													   ViBoolean singleStepEnabled,
													   ViReal64 dwell);

ViStatus _VI_FUNC   IviUpconverter_CreateFrequencyList (ViSession vi,
													    ViConstString name,
														ViInt32 frequencyBufferSize,
														ViReal64 frequency[]);

ViStatus _VI_FUNC   IviUpconverter_CreateFrequencyPowerList (ViSession vi,
															 ViConstString name,
															 ViInt32 bufferSize,
															 ViReal64 frequency[],
															 ViReal64 power[]);

ViStatus _VI_FUNC   IviUpconverter_CreateFrequencyGainList (ViSession vi,
															ViConstString name,
															ViInt32 bufferSize,
															ViReal64 frequency[],
															ViReal64 gain[]);

ViStatus _VI_FUNC   IviUpconverter_CreatePowerList (ViSession vi,
													ViConstString name,
													ViInt32 powerBufferSize,
													ViReal64 power[]);

ViStatus _VI_FUNC   IviUpconverter_CreateGainList (ViSession vi,
												   ViConstString name,
												   ViInt32 gainBufferSize,
												   ViReal64 gain[]);

ViStatus _VI_FUNC   IviUpconverter_ResetList (ViSession vi);

	/*- IviUpconverterALC Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureALC (ViSession vi,
												 ViInt32 source,
												 ViReal64 bandwidth);

    /*- IviUpconverterCalibration Functions -*/
ViStatus _VI_FUNC   IviUpconverter_Calibrate (ViSession vi);

ViStatus _VI_FUNC	IviUpconverter_IsCalibrationComplete (ViSession vi,
														  ViInt32* status);

	/*- IviUpconverterAttenuatorHold Functions -*/
ViStatus _VI_FUNC	IviUpconverter_ConfigureAttenuatorHoldEnabled (ViSession vi,
																   ViBoolean enabled);

	/*- IviUpconverterReferenceOscillator Functions -*/
ViStatus _VI_FUNC   IviUpconverter_ConfigureReferenceOscillator (ViSession vi, 
																 ViInt32 source,
																 ViReal64 frequency);

ViStatus _VI_FUNC	IviUpconverter_ConfigureReferenceOscillatorOutputEnabled (ViSession vi,
																			  ViBoolean enabled);

	/*- IviUpconverterSoftwareTrigger Functions -*/
ViStatus _VI_FUNC	IviUpconverter_SendSoftwareTrigger (ViSession vi);

	/*- IviUpconverterModulateIQ Functions -*/
ViStatus _VI_FUNC	IviUpconverter_CalibrateIQ (ViSession vi);

ViStatus _VI_FUNC	IviUpconverter_ConfigureIQEnabled (ViSession vi,
													   ViBoolean enabled);

	/*- IviUpconverterIQImpairment Functions -*/
ViStatus _VI_FUNC	IviUpconverter_ConfigureIQImpairment (ViSession vi,
														  ViReal64 IOffset,
														  ViReal64 QOffset,
														  ViReal64 ratio,
														  ViReal64 skew);

ViStatus _VI_FUNC	IviUpconverter_ConfigureIQImpairmentEnabled (ViSession vi,
																 ViBoolean enabled);
                                                
/****************************************************************************
 *------------- IviUpconverter Class Error And Completion Codes ------------*
 ****************************************************************************/
#define IVIUPCONVERTER_ERROR_LIST_UNKNOWN				(IVI_CLASS_ERROR_BASE + 2L) 
#define IVIUPCONVERTER_ERROR_MAX_TIME_EXCEEDED	      	(IVI_CLASS_ERROR_BASE + 1L)
#define IVIUPCONVERTER_ERROR_TRIGGER_NOT_SOFTWARE   	(IVI_CROSS_CLASS_ERROR_BASE + 1L)

#define IVIUPCONVERTER_ERRMSG_LIST_UNKNOWN				"The selected list is not defined."
#define IVIUPCONVERTER_ERRMSG_MAX_TIME_EXCEEDED     	"Maximum time exceeded before the operation completed."	
#define IVIUPCONVERTER_ERRMSG_TRIGGER_NOT_SOFTWARE  	"Trigger source is not set to software trigger."

#define IVIUPCONVERTER_ERROR_CODES_AND_MSGS \
        {IVIUPCONVERTER_ERROR_LIST_UNKNOWN,				IVIUPCONVERTER_ERRMSG_LIST_UNKNOWN}, \
        {IVIUPCONVERTER_ERROR_MAX_TIME_EXCEEDED,    	IVIUPCONVERTER_ERRMSG_MAX_TIME_EXCEEDED	  }, \
        {IVIUPCONVERTER_ERROR_TRIGGER_NOT_SOFTWARE, 	IVIUPCONVERTER_ERRMSG_TRIGGER_NOT_SOFTWARE  } 

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}                                                    
#endif

#endif /* IVIUPCONVERTER_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/IviVisaType.h sha256=3b8d1ccb0ba7a0149794e5554ce13060a90dd4eb1679dc5b19a53ce1b19f6196 bytes=7801 -->
## FILE: imports/include/IviVisaType.h

- repository: `ni/grpc-device`
- source_path: `imports/include/IviVisaType.h`
- sha256: `3b8d1ccb0ba7a0149794e5554ce13060a90dd4eb1679dc5b19a53ce1b19f6196`
- bytes: 7801

````c
/****************************************************************************
 * IviVisaType.h
 *
 * Copyright (c) Interchangeable Virtual Instruments Foundation 2006 - 2017.
 * All Rights Reserved.
 *
 ****************************************************************************/
#ifndef IVI_VISA_TYPE_H
#define IVI_VISA_TYPE_H
/* This defines the include guard of visatype.h for backward compatibility
 * reasons. Please ensure that changes in this ifndef block are reflected
 * in visatype.h when necessary.
 */
#ifndef __VISATYPE_HEADER__
#define __VISATYPE_HEADER__
#if defined(_WIN64)
#define _VI_FAR
#define _VI_FUNC            __fastcall
#define _VI_FUNCC           __fastcall
#define _VI_FUNCH           __fastcall
#define _VI_SIGNED          signed
#elif (defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)) && !defined(_NI_mswin16_)
#define _VI_FAR
#define _VI_FUNC            __stdcall
#define _VI_FUNCC           __cdecl
#define _VI_FUNCH           __stdcall
#define _VI_SIGNED          signed
#elif defined(_CVI_) && defined(_NI_i386_)
#define _VI_FAR
#define _VI_FUNC            _pascal
#define _VI_FUNCC
#define _VI_FUNCH           _pascal
#define _VI_SIGNED          signed
#elif (defined(_WINDOWS) || defined(_Windows)) && !defined(_NI_mswin16_)
#define _VI_FAR             _far
#define _VI_FUNC            _far _pascal _export
#define _VI_FUNCC           _far _cdecl  _export
#define _VI_FUNCH           _far _pascal
#define _VI_SIGNED          signed
#elif (defined(hpux) || defined(__hpux)) && (defined(__cplusplus) || defined(__cplusplus__))
#define _VI_FAR
#define _VI_FUNC
#define _VI_FUNCC
#define _VI_FUNCH
#define _VI_SIGNED
#else
#define _VI_FAR
#define _VI_FUNC
#define _VI_FUNCC
#define _VI_FUNCH
#define _VI_SIGNED          signed
#endif
#define _VI_ERROR           (-2147483647L-1)  /* 0x80000000 */
#define _VI_PTR             _VI_FAR *
/*- VISA Types --------------------------------------------------------------*/
#ifndef _VI_INT64_UINT64_DEFINED
#if defined(_WIN64) || ((defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)) && !defined(_NI_mswin16_))
#if (defined(_MSC_VER) && (_MSC_VER >= 1200)) || (defined(_CVI_) && (_CVI_ >= 700)) || (defined(__BORLANDC__) && (__BORLANDC__ >= 0x0520)) || defined(__LCC__) || (defined(__GNUC__) && (__GNUC__ >= 3)) || (defined(__clang__) && (__clang_major__ >= 3))
typedef unsigned   __int64  ViUInt64;
typedef _VI_SIGNED __int64  ViInt64;
#define _VI_INT64_UINT64_DEFINED
#if defined(_WIN64)
#define _VISA_ENV_IS_64_BIT
#else
/* This is a 32-bit OS, not a 64-bit OS */
#endif
#endif
#elif defined(__GNUC__) && (__GNUC__ >= 3)
#include <limits.h>
#include <sys/types.h>
typedef u_int64_t           ViUInt64;
typedef int64_t             ViInt64;
#define _VI_INT64_UINT64_DEFINED
#if defined(LONG_MAX) && (LONG_MAX > 0x7FFFFFFFL)
#define _VISA_ENV_IS_64_BIT
#else
/* This is a 32-bit OS, not a 64-bit OS */
#endif
#else
/* This platform does not support 64-bit types */
#endif
#endif
#if defined(_VI_INT64_UINT64_DEFINED)
typedef ViUInt64    _VI_PTR ViPUInt64;
typedef ViUInt64    _VI_PTR ViAUInt64;
typedef ViInt64     _VI_PTR ViPInt64;
typedef ViInt64     _VI_PTR ViAInt64;
#endif
#if defined(LONG_MAX) && (LONG_MAX > 0x7FFFFFFFL)
typedef unsigned int        ViUInt32;
typedef _VI_SIGNED int      ViInt32;
#else
typedef unsigned long       ViUInt32;
typedef _VI_SIGNED long     ViInt32;
#endif
typedef ViUInt32    _VI_PTR ViPUInt32;
typedef ViUInt32    _VI_PTR ViAUInt32;
typedef ViInt32     _VI_PTR ViPInt32;
typedef ViInt32     _VI_PTR ViAInt32;
typedef unsigned short      ViUInt16;
typedef ViUInt16    _VI_PTR ViPUInt16;
typedef ViUInt16    _VI_PTR ViAUInt16;
typedef _VI_SIGNED short    ViInt16;
typedef ViInt16     _VI_PTR ViPInt16;
typedef ViInt16     _VI_PTR ViAInt16;
typedef unsigned char       ViUInt8;
typedef ViUInt8     _VI_PTR ViPUInt8;
typedef ViUInt8     _VI_PTR ViAUInt8;
typedef _VI_SIGNED char     ViInt8;
typedef ViInt8      _VI_PTR ViPInt8;
typedef ViInt8      _VI_PTR ViAInt8;
typedef char                ViChar;
typedef ViChar      _VI_PTR ViPChar;
typedef ViChar      _VI_PTR ViAChar;
typedef unsigned char       ViByte;
typedef ViByte      _VI_PTR ViPByte;
typedef ViByte      _VI_PTR ViAByte;
typedef void        _VI_PTR ViAddr;
typedef ViAddr      _VI_PTR ViPAddr;
typedef ViAddr      _VI_PTR ViAAddr;
typedef float               ViReal32;
typedef ViReal32    _VI_PTR ViPReal32;
typedef ViReal32    _VI_PTR ViAReal32;
typedef double              ViReal64;
typedef ViReal64    _VI_PTR ViPReal64;
typedef ViReal64    _VI_PTR ViAReal64;
typedef ViPByte             ViBuf;
typedef const ViByte *      ViConstBuf;
typedef ViPByte             ViPBuf;
typedef ViPByte     _VI_PTR ViABuf;
typedef ViPChar             ViString;
#ifndef _VI_CONST_STRING_DEFINED
typedef const ViChar *      ViConstString;
#define _VI_CONST_STRING_DEFINED
#endif
typedef ViPChar             ViPString;
typedef ViPChar     _VI_PTR ViAString;
typedef ViString            ViRsrc;
typedef ViConstString       ViConstRsrc;
typedef ViString            ViPRsrc;
typedef ViString    _VI_PTR ViARsrc;
typedef ViUInt16            ViBoolean;
typedef ViBoolean   _VI_PTR ViPBoolean;
typedef ViBoolean   _VI_PTR ViABoolean;
typedef ViInt32             ViStatus;
typedef ViStatus    _VI_PTR ViPStatus;
typedef ViStatus    _VI_PTR ViAStatus;
typedef ViUInt32            ViVersion;
typedef ViVersion   _VI_PTR ViPVersion;
typedef ViVersion   _VI_PTR ViAVersion;
typedef ViUInt32            ViObject;
typedef ViObject    _VI_PTR ViPObject;
typedef ViObject    _VI_PTR ViAObject;
typedef ViObject            ViSession;
typedef ViSession   _VI_PTR ViPSession;
typedef ViSession   _VI_PTR ViASession;
typedef ViUInt32             ViAttr;
/*- Completion and Error Codes ----------------------------------------------*/
#define VI_SUCCESS          (0L)
/*- Other VISA Definitions --------------------------------------------------*/
#define VI_NULL             (0)
#define VI_TRUE             (1)
#define VI_FALSE            (0)
/*- Backward Compatibility Macros -------------------------------------------*/
#define VISAFN              _VI_FUNC
#define ViPtr               _VI_PTR
#endif /* __VISATYPE_HEADER__ */
/* This defines the include guard of vpptype.h for backward compatibility
 * reasons. Please ensure that changes in this ifndef block are reflected
 * in vpptype.h when necessary.
 */
#ifndef __VPPTYPE_HEADER__
#define __VPPTYPE_HEADER__
/*- Completion and Error Codes ----------------------------------------------*/
#define VI_WARN_NSUP_ID_QUERY     (          0x3FFC0101L)
#define VI_WARN_NSUP_RESET        (          0x3FFC0102L)
#define VI_WARN_NSUP_SELF_TEST    (          0x3FFC0103L)
#define VI_WARN_NSUP_ERROR_QUERY  (          0x3FFC0104L)
#define VI_WARN_NSUP_REV_QUERY    (          0x3FFC0105L)
#define VI_ERROR_PARAMETER1       (_VI_ERROR+0x3FFC0001L)
#define VI_ERROR_PARAMETER2       (_VI_ERROR+0x3FFC0002L)
#define VI_ERROR_PARAMETER3       (_VI_ERROR+0x3FFC0003L)
#define VI_ERROR_PARAMETER4       (_VI_ERROR+0x3FFC0004L)
#define VI_ERROR_PARAMETER5       (_VI_ERROR+0x3FFC0005L)
#define VI_ERROR_PARAMETER6       (_VI_ERROR+0x3FFC0006L)
#define VI_ERROR_PARAMETER7       (_VI_ERROR+0x3FFC0007L)
#define VI_ERROR_PARAMETER8       (_VI_ERROR+0x3FFC0008L)
#define VI_ERROR_FAIL_ID_QUERY    (_VI_ERROR+0x3FFC0011L)
#define VI_ERROR_INV_RESPONSE     (_VI_ERROR+0x3FFC0012L)
/*- Additional Definitions --------------------------------------------------*/
#define VI_ON               (1)
#define VI_OFF              (0)
#endif /* __VPPTYPE_HEADER__ */
#endif /* IVI_VISA_TYPE_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niBTGeneration.h sha256=278e32fe68803d93c893f9e5c2cee39eef5f3c63bb6257c43995fb42e39e5abc bytes=49811 -->
## FILE: imports/include/niBTGeneration.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niBTGeneration.h`
- sha256: `278e32fe68803d93c893f9e5c2cee39eef5f3c63bb6257c43995fb42e39e5abc`
- bytes: 49811

````c
/****************************************************************************
 *          National Instruments  BT Generation
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2011.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niBTGeneration.h
 * Purpose:  National Instruments BT Generator
 *           functions declarations.
 *
 ****************************************************************************/

#ifndef __NIBT_TOOLKIT_GENERATION_HEADER_DEFINED__
#define __NIBT_TOOLKIT_GENERATION_HEADER_DEFINED__

#ifdef __cplusplus
extern "C"
{
#endif

// NI-BT Typedefs 
#ifndef _NI_int8_DEFINED_
#define _NI_int8_DEFINED_
    typedef signed char        int8;
#endif
#ifndef _NI_uInt8_DEFINED_
#define _NI_uInt8_DEFINED_
    typedef unsigned char      uInt8;
#endif
#ifndef _NI_int16_DEFINED_
#define _NI_int16_DEFINED_
    typedef signed short       int16;
#endif
#ifndef _NI_uInt16_DEFINED_
#define _NI_uInt16_DEFINED_
    typedef unsigned short     uInt16;
#endif
#ifndef _NI_int32_DEFINED_
#define _NI_int32_DEFINED_
    typedef signed long       int32;
#endif
#ifndef _NI_uInt32_DEFINED_
#define _NI_uInt32_DEFINED_
    typedef unsigned long      uInt32;
#endif
#ifndef _NI_float32_DEFINED_
#define _NI_float32_DEFINED_
    typedef float              float32;
#endif
#ifndef _NI_float64_DEFINED_
#define _NI_float64_DEFINED_
    typedef double             float64;
#endif
#ifndef _NI_int64_DEFINED_
#define _NI_int64_DEFINED_
#ifdef __linux__
    typedef long long int      int64;
#else
    typedef __int64            int64;
#endif
#endif
#ifndef _NI_uInt64_DEFINED_
#define _NI_uInt64_DEFINED_
#ifdef __linux__
    typedef unsigned long long uInt64;
#else
    typedef unsigned __int64   uInt64;
#endif
#endif

#ifndef _NI_BT_GENERATION_SESSION_DEFINED_
#define _NI_BT_GENERATION_SESSION_DEFINED_
    typedef uInt64*            niBTSGSession;
#endif

#ifndef _NI_BT_GENERATION_ATTR_DEFINED_
#define _NI_BT_GENERATION_ATTR_DEFINED_
    typedef int32            niBTSG_Attr;
#endif

typedef uInt32 LVRefNum;
typedef uInt32 ViSession;

#if !defined(_NIComplexNumber)
#define _NIComplexNumber


#pragma pack(push, 8)
typedef struct NIComplexNumber_struct {
    float64 real;
    float64 imaginary;
} NIComplexNumber;
#pragma pack(pop)


#endif

/**********************************************************************************************************************/
/************************************ BT  Generation Attributes *******************************************************/
/**********************************************************************************************************************/

/* -- Properties ----------------------------------------------------------------------*/
#define NIBTSG_CARRIER_MODE										              0x01	/* readwrite, 	int32 */
#define NIBTSG_CARRIER_FREQUENCY                                              0x40    /* readwrite, 	float64 */
#define NIBTSG_OVERSAMPLING_FACTOR                                            0x46    /* readwrite, 	int32 */
#define NIBTSG_WAVEFORM_FILE_VERSION							              0x51    /* readwrite, 	int32 */

/* -- Hardware Settings --------------------------------------------------------------- */	
#define NIBTSG_MAXIMUM_HARDWARE_IQ_RATE                                       0x45	/* readwrite, 	float64 */ 
#define NIBTSG_AUTO_HEADROOM_ENABLED							              0x03	/* readwrite, 	int32 */
#define NIBTSG_HEADROOM											              0x04	/* readwrite, 	float64 */
#define NIBTSG_RUN_TIME_SCALING									              0x4F	/* readwrite, 	float64*/

/* -- Hardware Settings:Recommended Hardware Settings --------------------------------- */		
#define NIBTSG_IQ_RATE											              0x05	/* readonly, 	float64 */
#define NIBTSG_ACTUAL_HEADROOM									              0x06	/* readonly, 	float64 */
			                                                                  
#define NIBTSG_PACKET_TYPE										              0x07	/* readwrite, 	int32 */
#define NIBTSG_MODULATION_INDEX                                               0x44    /* readwrite, 	float64 */
	                                                                          
#define NIBTSG_BD_ADDRESS_LAP									              0x08	/* readwrite, 	int32 */
#define NIBTSG_BD_ADDRESS_UAP									              0x09	/* readwrite, 	int32 */
#define NIBTSG_BD_ADDRESS_NAP									              0x0A	/* readwrite, 	int32 */
			                                                                  
#define NIBTSG_PACKET_HEADER_LT_ADDRESS							              0x0B	/* readwrite, 	int32 */
#define NIBTSG_PACKET_HEADER_FLOW								              0x0C	/* readwrite, 	int32 */
#define NIBTSG_PACKET_HEADER_ARQN								              0x0D	/* readwrite, 	int32 */
#define NIBTSG_PACKET_HEADER_SEQN								              0x0E	/* readwrite, 	int32 */
			
#define NIBTSG_PAYLOAD_HEADER_ENABLED                                         0x42    /* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_HEADER_LLID								              0x0F	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_HEADER_FLOW								              0x10	/* readwrite, 	int32 */
			                                                                  
#define NIBTSG_PAYLOAD_LENGTH_MODE								              0x2B	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_LENGTH									              0x11	/* readwrite, 	int32 */
#define NIBTSG_ACTUAL_PAYLOAD_LENGTH							              0x2C	/* readonly, 	int32 */
#define NIBTSG_PAYLOAD_DATA_TYPE								              0x12	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_PN_ORDER									              0x29	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_PN_SEED									              0x2A	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_USER_DEFINED_BITS						              0x14	/* readwrite, 	int32[] */
			                                                                  
#define NIBTSG_FHS_PAYLOAD_LT_ADDRESS							              0x15	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_DEVICE_CLASS							              0x16	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_SCAN_REPETITION						              0x18	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_PAGE_SCAN_MODE						              0x19	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_DEVICE_CLOCK							              0x1A	/* readwrite, 	int32 */
			                                                                  
#define NIBTSG_FHS_PAYLOAD_BD_ADDRESS_LAP						              0x1B	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_BD_ADDRESS_UAP						              0x1C	/* readwrite, 	int32 */
#define NIBTSG_FHS_PAYLOAD_BD_ADDRESS_NAP						              0x1D	/* readwrite, 	int32 */
			                                                                  
#define NIBTSG_DV_VOICE_PAYLOAD_DATA_TYPE						              0x31	/* readwrite, 	int32 */
#define NIBTSG_DV_VOICE_PAYLOAD_PN_ORDER						              0x2E	/* readwrite, 	int32 */
#define NIBTSG_DV_VOICE_PAYLOAD_PN_SEED							              0x2F	/* readwrite, 	int32 */
#define NIBTSG_DV_VOICE_PAYLOAD_USER_DEFINED_BITS				              0x30	/* readwrite, 	int32[] */
                                                                              
#define NIBTSG_LE_TP_PAYLOAD_TYPE								              0x32	/* readwrite,	int32 */
#define NIBTSG_LE_TP_CORRUPT_ALTERNATE_CRC						              0x36	/* readwrite, 	int32 */

#define NIBTSG_DIRECTION_FINDING_MODE                                         0x4B    /* readwrite, 	int32 */
#define NIBTSG_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH               0x4D    /* readwrite, 	float64*/
#define NIBTSG_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION        0x4E    /* readwrite, 	float64*/
#define NIBTSG_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED                    0x56    /* readwrite, 	int32 */
#define NIBTSG_DIRECTION_FINDING_NUMBER_OF_ANTENNAS                           0x52    /* readwrite, 	int32 */
#define NIBTSG_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN                    0x55    /* readwrite, 	string */
#define NIBTSG_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION			          0x57    /* readwrite, 	float64*/
#define NIBTSG_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED	          0x58    /* readonly, 	 	float64*/
			
#define NIBTSG_WHITENING_ENABLED								              0x1F	/* readwrite, 	int32 */
#define NIBTSG_WHITENING_CLOCK									              0x20	/* readwrite, 	int32 */
#define NIBTSG_DIRTY_TX_ENABLED									              0x1E	/* readwrite, 	int32 */
#define NIBTSG_DIRTY_TX_MODE									              0x37	/* readwrite, 	int32 */
#define NIBTSG_DIRTY_TX_MODULATION_INDEX_TYPE                                 0x43    /* readwrite, 	int32 */
#define NIBTSG_DIRTY_TX_PARAMETERS_ENABLED_SET					              0x38	/* readwrite, 	int32[] */
#define NIBTSG_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET			              0x39	/* readwrite, 	int32[] */
#define NIBTSG_DIRTY_TX_MODULATION_INDEX_SET					              0x3A	/* readwrite, 	float64[] */
#define NIBTSG_DIRTY_TX_SYMBOL_TIMING_ERROR_SET					              0x3B	/* readwrite, 	int32[] */
#define NIBTSG_DIRTY_TX_RESIDUAL_FM_FREQUENCY                                 0x3F    /*readwrite,    float64 */
#define NIBTSG_DIRTY_TX_RESIDUAL_FM_DEVIATION                                 0x3E    /*readwrite,	float64 */
#define NIBTSG_NUMBER_OF_UNIQUE_PACKETS							              0x33	/* readwrite, 	int32 */
#define NIBTSG_NUMBER_OF_IDLE_SLOTS								              0x34	/* readwrite, 	int32 */
#define NIBTSG_PACKET_BIT_SEQUENCE_TRACE_ENABLED                              0x49    /* readwrite, 	int32 */
#define NIBTSG_POWER_RAMP_TIME                                                0x48    /* readwrite,   float64 */
#define NIBTSG_POWER_RAMP_SETTLING_TIME                                       0x47    /* readwrite,   float64 */
			                                                                  
#define NIBTSG_ALL_IQ_IMPAIRMENTS_ENABLED						              0x17	/* readwrite, 	int32 */
#define NIBTSG_IQ_GAIN_IMBALANCE								              0x21	/* readwrite, 	float64 */
#define NIBTSG_QUADRATURE_SKEW									              0x22	/* readwrite, 	float64 */
#define NIBTSG_I_DC_OFFSET										              0x23	/* readwrite, 	float64 */
#define NIBTSG_Q_DC_OFFSET										              0x24	/* readwrite, 	float64 */
#define NIBTSG_CARRIER_FREQUENCY_OFFSET							              0x25	/* readwrite, 	float64 */
#define NIBTSG_SAMPLE_CLOCK_OFFSET						              		  0x63	/* readwrite, 	float64 */
#define NIBTSG_TIME_DELAY							              			  0x64	/* readwrite, 	float64 */
			                                                                  																			  
#define NIBTSG_AWGN_ENABLED										              0x26	/* readwrite, 	int32 */
#define NIBTSG_CARRIER_TO_NOISE_RATIO							              0x27	/* readwrite, 	float64 */
			                                                                  
#define NIBTSG_TOOLKIT_COMPATIBILITY_VERSION					              0x28	/* readonly, 	int32 */
#define NIBTSG_IQ_WAVEFORM_SIZE									              0x2D	/* readonly, 	int32 */

#define NIBTSG_LE_ACCESS_ADDRESS                                              0x3D    /*readwrite,    int32  */

#define NIBTSG_BURST_START_LOCATIONS							              0x5A	/* readonly, 	int32[] */
#define NIBTSG_BURST_STOP_LOCATIONS								              0x5B	/* readonly, 	int32[] */

#define NIBTSG_CS_PACKET_FORMAT									              0x5C	/*readwrite, 	int32 */
#define NIBTSG_CS_SYNC_SEQUENCE									              0x5D	/*readwrite, 	int32 */
#define NIBTSG_CS_PHASE_MEASUREMENT_PERIOD						              0x5E	/*readwrite, 	float64 */
#define NIBTSG_SOUNDING_SEQUENCE_LENGTH							              0x5F	/*readwrite, 	int32 */
#define NIBTSG_SOUNDING_SEQUENCE_MARKER_SIGNALS					              0x60	/*readwrite, 	int32[] */
#define NIBTSG_SOUNDING_SEQUENCE_MARKER_POSITIONS				              0x61	/*readwrite, 	int32[] */
#define NIBTSG_CS_TONE_EXTENSION_SLOT_ENABLED					              0x62	/*readwrite, 	int32 */

#define NIBTSG_BANDWIDTH_BIT_PERIOD_PRODUCT  						          0x65  /* readwrite, 	float64 */

#define NIBTSG_DATA_RATE 					  						          0x66  /* readwrite, 	float64 */

#define NIBTSG_HDT_PACKET_FORMAT									          0x67	/* readwrite, 	int32 */
#define NIBTSG_HDT_PHY_INTERVAL						                          0x68	/* readwrite, 	float64 */
#define NIBTSG_ZADOFF_CHU_INDEX						                          0x69	/* readwrite, 	int32 */
#define NIBTSG_PHYSICAL_CHANNEL_ADDRESS						                  0x6A	/* readwrite, 	int64 */
#define NIBTSG_VHDT_MODE_ENABLED								              0x6B	/* readwrite, 	int32 */
#define NIBTSG_NUMBER_OF_BLOCK_REPETITION_SEQUENCES				              0x6C	/* readwrite, 	int32 */
#define NIBTSG_NUMBER_OF_PAYLOADS											  0x6D	/* readwrite, 	int32 */
#define NIBTSG_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE				   		  0x6E  /* readwrite, 	int32 */
#define NIBTSG_TXLEN_SEQUENCE_NUMBER							  			  0x6F	/* readwrite, 	int32 */
#define NIBTSG_NUMBER_OF_BLOCKS							              		  0x70	/* readwrite, 	int32 */	
#define NIBTSG_BLOCK_SIZE							              		  	  0x71	/* readwrite, 	int32 */
#define NIBTSG_LAST_BLOCK_SIZE						              		  	  0x72	/* readwrite, 	int32 */	
#define NIBTSG_TXBLOCK_MAP					              		  			  0x73	/* readwrite, 	int32 */
#define NIBTSG_PAYLOAD_ZONE_LENGTH								              0x75	/* readonly, 	int32 */
#define NIBTSG_PAYLOAD_CRC_SEED								                  0x76	/* readwrite, 	int64 */
                                                                              
#define NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_010000			               10000
#define NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_020000                        20000
                                                                              
#define NIBTSG_VAL_MAX_ERROR_MESSAGE_SIZE						               1024


/* Enum Values */                                                             
#define NIBTSG_VAL_FALSE										               0	
#define NIBTSG_VAL_TRUE											               1
                                                                              
#define NIBTSG_VAL_CARRIER_MODE_BURST							               0
#define NIBTSG_VAL_CARRIER_MODE_CONTINUOUS						               1
                                                                              
#define NIBTSG_VAL_PACKET_TYPE_NULL								               0
#define NIBTSG_VAL_PACKET_TYPE_POLL								               1
#define NIBTSG_VAL_PACKET_TYPE_FHS								               2
#define NIBTSG_VAL_PACKET_TYPE_DM1								               3
#define NIBTSG_VAL_PACKET_TYPE_DH1								               4
#define NIBTSG_VAL_PACKET_TYPE_2DH1								               5
#define NIBTSG_VAL_PACKET_TYPE_HV1								               6
#define NIBTSG_VAL_PACKET_TYPE_HV2								               7
#define NIBTSG_VAL_PACKET_TYPE_2EV3								               8
#define NIBTSG_VAL_PACKET_TYPE_HV3								               9
#define NIBTSG_VAL_PACKET_TYPE_EV3								               10
#define NIBTSG_VAL_PACKET_TYPE_3EV3								               11
#define NIBTSG_VAL_PACKET_TYPE_DV								               12
#define NIBTSG_VAL_PACKET_TYPE_3DH1								               13
#define NIBTSG_VAL_PACKET_TYPE_AUX1								               14
#define NIBTSG_VAL_PACKET_TYPE_DM3								               15
#define NIBTSG_VAL_PACKET_TYPE_2DH3								               16
#define NIBTSG_VAL_PACKET_TYPE_DH3								               17
#define NIBTSG_VAL_PACKET_TYPE_3DH3								               18
#define NIBTSG_VAL_PACKET_TYPE_EV4								               19
#define NIBTSG_VAL_PACKET_TYPE_2EV5								               20
#define NIBTSG_VAL_PACKET_TYPE_EV5								               21
#define NIBTSG_VAL_PACKET_TYPE_3EV5								               22
#define NIBTSG_VAL_PACKET_TYPE_DM5								               23
#define NIBTSG_VAL_PACKET_TYPE_2DH5								               24
#define NIBTSG_VAL_PACKET_TYPE_DH5								               25
#define NIBTSG_VAL_PACKET_TYPE_3DH5								               26
#define NIBTSG_VAL_PACKET_TYPE_LE_TP							               27
#define NIBTSG_VAL_PACKET_TYPE_LE_TP_EXT                                       28
#define NIBTSG_VAL_PACKET_TYPE_LE_ENHANCED                                     29
#define NIBTSG_VAL_PACKET_TYPE_LE_LR_125K                                      30
#define NIBTSG_VAL_PACKET_TYPE_LE_LR_500K                                      31
#define NIBTSG_VAL_PACKET_TYPE_LE_CS_1M							               32
#define NIBTSG_VAL_PACKET_TYPE_LE_CS_2M							               33
#define NIBTSG_VAL_PACKET_TYPE_LE_HDT										   34
#define NIBTSG_VAL_PACKET_TYPE_ID								               254
#define NIBTSG_VAL_PACKET_TYPE_IDLE								               255
                                                                               
#define NIBTSG_VAL_PACKET_HEADER_ARQN_NAK						               0
#define NIBTSG_VAL_PACKET_HEADER_ARQN_ACK						               1
                                                                               
#define NIBTSG_VAL_PAYLOAD_HEADER_ENABLED_FALSE                                0
#define NIBTSG_VAL_PAYLOAD_HEADER_ENABLED_TRUE                                 1
                                                                               
#define NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH			               0
#define NIBTSG_VAL_PAYLOAD_LENGTH_MODE_USER_DEFINED				               1
                                                                               
#define NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE				               0
#define NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS			               1
                                                                               
#define NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD                     0
#define NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE                       1
                                                                               
#define NIBTSG_VAL_DIRTY_TX_MODE_STANDARD						               0
#define NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED					               1
#define NIBTSG_VAL_DIRTY_TX_MODE_FREQUENCY_DRIFT				               2
                                                                               
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS9						               0	
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_11110000					               1
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_10101010					               2
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS15					               3
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_11111111					               4
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_00000000					               5
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_00001111					               6
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_01010101					               7
#define NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_USER_DEFINED_BITS			               8
                                                                               
#define NIBTSG_FILE_OPERATION_MODE_OPEN							               0
#define NIBTSG_FILE_OPERATION_MODE_OPEN_OR_CREATE				               1
#define NIBTSG_FILE_OPERATION_MODE_CREATE_OR_REPLACE			               2
#define NIBTSG_FILE_OPERATION_MODE_CREATE						               3
                                                                               
#define NIBTSG_STANDARD_BASIC_EDR								               0
#define NIBTSG_STANDARD_LE										               1
#define NIBTSG_STANDARD_LE_CS									               2

#define NIBTSG_VAL_DIRECTION_FINDING_MODE_DISABLED                             0
#define NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL                     1
#define NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE                   2

#define NIBTSG_VAL_CS_PACKET_FORMAT_SYNC						               0
#define NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE						               1
#define NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE_AFTER_SYNC			               2
#define NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE_BEFORE_SYNC			               3

#define NIBTSG_VAL_CS_SYNC_SEQUENCE_NONE						               0
#define NIBTSG_VAL_CS_SYNC_SEQUENCE_SOUNDING_SEQUENCE			               1
#define NIBTSG_VAL_CS_SYNC_SEQUENCE_PAYLOAD_PATTERN			               	   2

#define NIBTSG_VAL_SOUNDING_SEQUENCE_MARKER_SIGNALS_1100		               0
#define NIBTSG_VAL_SOUNDING_SEQUENCE_MARKER_SIGNALS_0011		               1

#define NIBTSG_VAL_HDT_PACKET_FORMAT_SHORT_FORMAT                              0
#define NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT0                            	   1
#define NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1                   				   2

/* Waveform File Version */
#define NIBTSG_VAL_WAVEFORM_FILE_VERSION_1_0					               0
#define NIBTSG_VAL_WAVEFORM_FILE_VERSION_2_0					               1

/****************************************************************************
*--------------------- BT Generation Function Declarations --------------*
****************************************************************************/

// BTSG Open Session
int32 __stdcall niBTSG_OpenSession(
	char sessionName[], 
	int32 toolkitCompatibilityVersion, 
	niBTSGSession *session, 
	int32 *isNewSession);

// Set Attribute Functions
int32 __stdcall niBTSG_SetAttributeString(
	niBTSGSession session,
	char channelString[], 
	int32 attributeID, 
	char attributeValue[]);

int32 __stdcall niBTSG_SetScalarAttributeF64(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID,                              
    float64 attributeValue);

int32 __stdcall niBTSG_SetScalarAttributeI32(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID, 
    int32 attributeValue);

int32 __stdcall niBTSG_SetScalarAttributeI64(
	niBTSGSession session,
	char channelString[], 
	niBTSG_Attr attributeID, 
	int64 attributeValue);

int32 __stdcall niBTSG_SetVectorAttributeI32(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID, 
    int32 dataArray[], 
    int32 dataArraySize);
	
int32 __stdcall niBTSG_SetVectorAttributeF64(
	niBTSGSession session,
	char channelString[], 
	niBTSG_Attr attributeID,
	float64 data[],
	int32 dataArraySize);	

// Get Attribute Functions
int32 __stdcall niBTSG_GetAttributeString(
	niBTSGSession session,
	char channelString[],
	int32 attributeID,
	char attributeValue[],
	int32 bufferSize,
	int32 *actualStringSize);

int32 __stdcall niBTSG_GetScalarAttributeF64(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID, 
    float64 *attributeValue);

int32 __stdcall niBTSG_GetScalarAttributeI32(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID, 
    int32 *attributeValue);

int32 __stdcall niBTSG_GetScalarAttributeI64(
	niBTSGSession session,
	char channelString[], 
	niBTSG_Attr attributeID, 
	int64 *attributeValue);
	
int32 __stdcall niBTSG_GetVectorAttributeI32(
    niBTSGSession session,
    char channelString[], 
    niBTSG_Attr attributeID,  
    int32 dataArray[], 
    int32 dataArraySize,
    int32 *actualNumDataArrayElements);
	
int32 __stdcall niBTSG_GetVectorAttributeF64(
	niBTSGSession session,
	char channelString[],
	niBTSG_Attr attributeID,
	float64 data[],
	int32 dataArraySize,
	int32* actualNumDataArrayElements);	

// Reset Attribute
int32 __stdcall niBTSG_ResetAttribute(
    niBTSGSession session,
    char channelString[],
    niBTSG_Attr attributeID);

// BTSG Create Waveform
int32 __stdcall niBTSG_CreateWaveformComplexF64(
	niBTSGSession session,
	int32 reset,
	float64 *t0, 
	float64 *dt, 
	NIComplexNumber waveform[], 
	int32 waveformSize, 
	int32 *actualWaveformSize,
	int32 *generationDone);

// BTSG Reset Session
int32 __stdcall niBTSG_ResetSession(
    niBTSGSession session);	
	
// BTSG Get Error String
int32 __stdcall niBTSG_GetErrorString(	
	niBTSGSession session, 
	int32 errorCode, 
	char errorMessage[], 
	int32 errorMessageLength);

int32 __stdcall niBTSG_SaveConfigurationToFile(
	niBTSGSession session, 
	char filePath[], 
	int32 operation);
	
// Loading and Saving Configuration 
int32 __stdcall niBTSG_LoadConfigurationFromFile(
	niBTSGSession session, 
	char filePath[], 
	int32 reset);

// Reading and Writing Waveforms
int32 __stdcall niBTSG_CreateAndWriteWaveformsToFile(
	niBTSGSession session,
	char filePath[],
	int32 fileOperation);	

int32 __stdcall niBTSG_ReadWaveformFromFile(
	char filePath[],
	char waveformName[],
	int64 offset,
	int64 count,
	float64 *t0, 
    float64 *dt, 
   	NIComplexNumber waveform[], 
   	int32 waveformSize, 
   	int32 *actualNumWaveformSamples,
	float64 *IQRate,
	float64 *headroom,
	int32 *eof);

// BTSG Channel Number To Carrier Frequency
int32 __stdcall niBTSG_ChannelNumberToCarrierFrequency(
	int32 channelNumber,
	int32 standard,
	float64 *carrierFrequency);

int32 __stdcall niBTSG_ChannelNumberToCarrierFrequencyV2(
	int32 channelNumber,
	int32 standard,
	int32 frequencyBand,
	float64 *carrierFrequency);
	
int32 __stdcall niBTSG_CarrierFrequencyToChannelNumber(
    float64 carrierFrequency,
	int32 standard,
	int32 *channelNumber);	
	
int32 __stdcall niBTSG_GetCurrentIterationPacketBitSequenceTrace(
    niBTSGSession session,
	int32 packetBitSequenceTrace[],
    int32 dataArraySize,
	int32 *actualArraySize); 	
	
// BTSG Close Session
int32 __stdcall niBTSG_CloseSession(
    niBTSGSession session);

// Set/Get Functions

int32 __stdcall niBTSG_SetCarrierFrequency(
	niBTSGSession session, 
	char channelString[],
	float64 value);
	
int32 __stdcall niBTSG_GetCarrierFrequency(
	niBTSGSession session, 
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetCarrierMode(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetCarrierMode(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetOversamplingFactor(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetOversamplingFactor(
	niBTSGSession session,
	char channelString[],
	int32 *value);
		
int32 __stdcall niBTSG_SetMaximumHardwareIQRate(
	niBTSGSession session,
	char channelString[],
	float64 value);
		
int32 __stdcall niBTSG_GetMaximumHardwareIQRate(
	niBTSGSession session,
	char channelString[],
	float64 *value);
			
int32 __stdcall niBTSG_SetAutoHeadroomEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetAutoHeadroomEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetHeadroom(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetHeadroom(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_GetIQRate(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_GetActualHeadroom(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetPacketType(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketType(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetModulationIndex(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetModulationIndex(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetBandwidthBitPeriodProduct(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetBandwidthBitPeriodProduct(
	niBTSGSession session,
	char channelString[],
	float64 *value);	

int32 __stdcall niBTSG_SetDataRate(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDataRate(
	niBTSGSession session,
	char channelString[],
	int32 *value);	
		
int32 __stdcall niBTSG_SetBDAddress(
	niBTSGSession session,
	char channelString[],
	int32 valueLAP,
	int32 valueUAP,
	int32 valueNAP);
	
int32 __stdcall niBTSG_GetBDAddress(
	niBTSGSession session,
	char channelString[],
	int32 *valueLAP,
	int32 *valueUAP,
	int32 *valueNAP);

int32 __stdcall niBTSG_SetPacketHeaderLTAddress(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketHeaderLTAddress(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPacketHeaderFLOW(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketHeaderFLOW(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPacketHeaderARQN(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketHeaderARQN(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPacketHeaderSEQN(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketHeaderSEQN(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadHeaderEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niBTSG_GetPayloadHeaderEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetPayloadHeaderLLID(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadHeaderLLID(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadHeaderFLOW(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadHeaderFLOW(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadLengthMode(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadLengthMode(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadLength(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadLength(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_GetActualPayloadLength(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadDataType(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadDataType(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadPNOrder(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadPNOrder(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadPNSeed(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPayloadPNSeed(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPayloadUserDefinedBits(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);

int32 __stdcall niBTSG_GetPayloadUserDefinedBits(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);

int32 __stdcall niBTSG_SetFHSPayloadLTAddress(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFHSPayloadLTAddress(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetFHSPayloadDeviceClass(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFHSPayloadDeviceClass(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetFHSPayloadScanRepetition(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFHSPayloadScanRepetition(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetFHSPayloadPageScanMode(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFHSPayloadPageScanMode(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetFHSPayloadDeviceClock(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFHSPayloadDeviceClock(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetFHSPayloadBDAddress(
	niBTSGSession session,
	char channelString[],
	int32 valueLAP,
	int32 valueUAP,
	int32 valueNAP);

int32 __stdcall niBTSG_GetFHSPayloadBDAddress(
	niBTSGSession session,
	char channelString[],
	int32 *valueLAP,
	int32 *valueUAP,
	int32 *avlueNAP);
	
int32 __stdcall niBTSG_SetDVVoicePayloadDataType(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDVVoicePayloadDataType(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetDVVoicePayloadPNOrder(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDVVoicePayloadPNOrder(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetDVVoicePayloadPNSeed(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDVVoicePayloadPNSeed(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetDVVoicePayloadUserDefinedBits(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);

int32 __stdcall niBTSG_GetDVVoicePayloadUserDefinedBits(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);
	
int32 __stdcall niBTSG_SetLE_TPPayloadType(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetLE_TPPayloadType(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetDirectionFindingMode(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDirectionFindingMode(
	niBTSGSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niBTSG_SetDirectionFindingConstantToneExtensionLength(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetDirectionFindingConstantToneExtensionLength(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetDirectionFindingConstantToneExtensionSlotDuration(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetDirectionFindingConstantToneExtensionSlotDuration(
	niBTSGSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niBTSG_SetDirectionFindingAntennaSwitchingEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDirectionFindingAntennaSwitchingEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niBTSG_SetDirectionFindingNumberOfAntennas(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDirectionFindingNumberOfAntennas(
	niBTSGSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niBTSG_SetDirectionFindingAntennaSwitchingPattern(
	niBTSGSession session,
	char channelString[],
	char attrVal[]);

int32 __stdcall niBTSG_GetDirectionFindingAntennaSwitchingPattern(
	niBTSGSession session,
	char channelString[],
	int32 arraySize,
	char attrVal[]);
	
int32 __stdcall niBTSG_SetDirectionFindingAntennaSwitchingDuration(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetDirectionFindingAntennaSwitchingDuration(
	niBTSGSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niBTSG_GetDirectionFindingAntennaSwitchingDurationUsed(
	niBTSGSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niBTSG_SetAntennaRelativePhaseAndAmplitude(
    niBTSGSession session,
	char channelString[],
	float64 relativeAmplitudeDB[], 
	float64 relativePhaseDeg[], 
	int32 arraySize);
	
int32 __stdcall niBTSG_SetWhiteningEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetWhiteningEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetWhiteningClock(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetWhiteningClock(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetDirtyTxEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetDirtyTxEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetDirtyTxMode(
	niBTSGSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niBTSG_GetDirtyTxMode(
	niBTSGSession session, 
	char channelString[], 
	int32 *value);
	
int32 __stdcall niBTSG_SetDirtyTxModulationIndexType(
	niBTSGSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niBTSG_GetDirtyTxModulationIndexType(
	niBTSGSession session, 
	char channelString[], 
	int32 *value);

int32 __stdcall niBTSG_SetDirtyTxParametersEnabledSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize);

int32 __stdcall niBTSG_GetDirtyTxParametersEnabledSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);

int32 __stdcall niBTSG_SetDirtyTxCarrierFrequencyOffsetSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize);

int32 __stdcall niBTSG_GetDirtyTxCarrierFrequencyOffsetSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);

int32 __stdcall niBTSG_SetDirtyTxModulationIndexSet(
	niBTSGSession session, 
	char channelString[], 
	float64 dataArray[], 
	int32 dataArraySize);

int32 __stdcall niBTSG_GetDirtyTxModulationIndexSet(
	niBTSGSession session, 
	char channelString[], 
	float64 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);

int32 __stdcall niBTSG_SetDirtyTxSymbolTimingErrorSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize);

int32 __stdcall niBTSG_GetDirtyTxSymbolTimingErrorSet(
	niBTSGSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);	

int32 __stdcall niBTSG_SetNumberOfUniquePackets(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetNumberOfUniquePackets(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetNumberOfIdleSlots(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetNumberOfIdleSlots(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetAllIQImpairmentsEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetPacketBitSequenceTraceEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetPacketBitSequenceTraceEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);	
	
int32 __stdcall niBTSG_SetPowerRampTime(
	niBTSGSession session,
	char channelString[],
	float64 value);	
	
int32 __stdcall niBTSG_GetPowerRampTime(	
	niBTSGSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niBTSG_SetPowerRampSettlingTime(
	niBTSGSession session,
	char channelString[],
	float64 value);	
	
int32 __stdcall niBTSG_GetPowerRampSettlingTime(	
	niBTSGSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niBTSG_GetAllIQImpairmentsEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetIQGainImbalance(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetIQGainImbalance(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetQuadratureSkew(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetQuadratureSkew(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetIDCOffset(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetIDCOffset(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetQDCOffset(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetQDCOffset(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetCarrierFrequencyOffset(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetCarrierFrequencyOffset(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetSampleClockOffset(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetSampleClockOffset(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetTimeDelay(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetTimeDelay(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetAWGNEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetAWGNEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetCarrierToNoiseRatio(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetCarrierToNoiseRatio(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_GetToolkitCompatibilityVersion(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_GetIQWaveformSize(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetDirtyTxResidualFMDeviation(
	niBTSGSession session,
	char channelString[],
	float64 value);
	
int32 __stdcall niBTSG_GetDirtyTxResidualFMDeviation(
	niBTSGSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niBTSG_SetDirtyTxResidualFMFrequency(
	niBTSGSession session,
	char channelString[],
	float64 value);	
	
int32 __stdcall niBTSG_GetDirtyTxResidualFMFrequency(
	niBTSGSession session,
	char channelString[],
	float64 *value);
	
	
int32 __stdcall niBTSG_SetLEAccessAddress(
    niBTSGSession session,
	char channelString[],
	int32 value);	
	
int32 __stdcall niBTSG_GetLEAccessAddress(
    niBTSGSession session,
	char channelString[],
	int32 *value);	
 	
int32 __stdcall niBTSG_GetBurstStartLocations(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);
	
int32 __stdcall niBTSG_GetBurstStopLocations(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);
	
int32 __stdcall niBTSG_SetRunTimeScaling(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetRunTimeScaling(
	niBTSGSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niBTSG_SetWaveformFileVersion(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetWaveformFileVersion(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetCSPacketFormat(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetCSPacketFormat(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetCSSyncSequence(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetCSSyncSequence(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetCSPhaseMeasurementPeriod(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetCSPhaseMeasurementPeriod(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetSoundingSequenceLength(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetSoundingSequenceLength(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetSoundingSequenceMarkerSignals(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);

int32 __stdcall niBTSG_GetSoundingSequenceMarkerSignals(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);
	
int32 __stdcall niBTSG_SetSoundingSequenceMarkerPositions(
	niBTSGSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);
	
int32 __stdcall niBTSG_GetSoundingSequenceMarkerPositions(
    niBTSGSession session,
    char channelString[],
    int32 dataArray[],
    int32 dataArraySize,
    int32* actualNumDataArrayElements);

int32 __stdcall niBTSG_SetCSToneExtensionSlotEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetCSToneExtensionSlotEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetHDTPacketFormat(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetHDTPacketFormat(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetHDTPHYInterval(
	niBTSGSession session,
	char channelString[],
	float64 value);

int32 __stdcall niBTSG_GetHDTPHYInterval(
	niBTSGSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niBTSG_SetZadoffChuIndex(
	niBTSGSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niBTSG_GetZadoffChuIndex(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_SetPhysicalChannelAddress(
	niBTSGSession session,
	char channelString[],
	int64 value);
	
int32 __stdcall niBTSG_GetPhysicalChannelAddress(
	niBTSGSession session,
	char channelString[],
	int64 *value);
	
int32 __stdcall niBTSG_SetVHDTModeEnabled(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetVHDTModeEnabled(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetNumberOfBlockRepetitionSequences(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetNumberOfBlockRepetitionSequences(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetNumberOfPayloads(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetNumberOfPayloads(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetFormat1PayloadZoneConfigurationMode(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetFormat1PayloadZoneConfigurationMode(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetTxLenSequenceNumber(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetTxLenSequenceNumber(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetNumberOfBlocks(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetNumberOfBlocks(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetBlockSize(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetBlockSize(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetLastBlockSize(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetLastBlockSize(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetTxBlockMap(
	niBTSGSession session,
	char channelString[],
	int32 value);

int32 __stdcall niBTSG_GetTxBlockMap(
	niBTSGSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niBTSG_GetPayloadZoneLength(
	niBTSGSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niBTSG_SetPayloadCRCSeed(
	niBTSGSession session,
	char channelString[],
	int64 value);

int32 __stdcall niBTSG_GetPayloadCRCSeed(
	niBTSGSession session,
	char channelString[],
	int64 *value);

	
#ifdef __cplusplus
}
#endif

#endif //__NIBT_TOOLKIT_GENERATION_HEADER_DEFINED__
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niBTGenerationRfsg.h sha256=e2c7c2e74b36b41c7fa7d0b291767d7c735888d21ef0c536b4731e663bf24aa0 bytes=2552 -->
## FILE: imports/include/niBTGenerationRfsg.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niBTGenerationRfsg.h`
- sha256: `e2c7c2e74b36b41c7fa7d0b291767d7c735888d21ef0c536b4731e663bf24aa0`
- bytes: 2552

````c
/****************************************************************************
 *          National Instruments BT Generation
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2011.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niBTGenerationRfsg.h
 * Purpose:  National Instruments BT Generator
 *           functions declarations.
 *
 ****************************************************************************/

#ifndef __NIBT_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__
#define __NIBT_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__

#include <niRFSG.h>
#include "niBTGeneration.h"

#ifdef __cplusplus
extern "C"
{
#endif

/*- RFSG Database ---------------------------------------------------------*/
// BTSG Create and download Waveform
int32 __stdcall niBTSG_RFSGCreateAndDownloadWaveform(
	niBTSGSession session, 
	ViSession RFSGHandle, 
    char channelString[],
	char waveformName[]);

// BTSG Store IQ Rate
int32 __stdcall niBTSG_RFSGStoreIQRate(
	ViSession RFSGHandle,
    char channelString[],
	char waveformName[], 
	float64 IQRate);

// BTSG Retrieve IQ Rate
int32 __stdcall niBTSG_RFSGRetrieveIQRate(
	ViSession RFSGHandle, 
    char channelString[],
	char waveformName[], 
	float64 *IQRate);

// BTSG Retrieve IQ Rate All Waveforms
int32 __stdcall niBTSG_RFSGRetrieveIQRateAllWaveforms(
	ViSession RFSGHandle, 
    char channelString[],
	char script[], 
	float64 *IQRate);
	
// BTSG Store Headroom                
int32 __stdcall niBTSG_RFSGStoreHeadroom(
	ViSession RFSGHandle, 
    char channelString[],
	char waveformName[], 
	float64 headroom);

// BTSG Retrieve Headroom
int32 __stdcall niBTSG_RFSGRetrieveHeadroom(
	ViSession RFSGHandle, 
    char channelString[],
	char waveformName[], 
	float64 *headroom);
	
// BTSG niBTSG_RFSGRetrieveMinimumHeadroomAllWaveforms
int32 __stdcall niBTSG_RFSGRetrieveMinimumHeadroomAllWaveforms(
	ViSession RFSGHandle, 
    char channelString[],
	char script[], 
	float64 *headroom);
	
// BTSG Configure Script
int32 __stdcall niBTSG_RFSGConfigureScript(
	ViSession RFSGHandle, 
    char channelString[],
	char script[], 
	float64 powerLevel);

// BTSG RFSG Clear Database	
int32 __stdcall niBTSG_RFSGClearDatabase(
 	ViSession RFSGHandle, 
    char channelString[],
	char waveformName[]);

#ifdef __cplusplus
}
#endif


#endif //__NIBT_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__
````
