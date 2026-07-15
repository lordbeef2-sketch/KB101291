# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niScope.h sha256=8e2f6f8b5047ec6725fa85419de55d7bed5236a48e0b3653a35416163a33293e bytes=128429 -->
## FILE: imports/include/niScope.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niScope.h`
- sha256: `8e2f6f8b5047ec6725fa85419de55d7bed5236a48e0b3653a35416163a33293e`
- bytes: 128429

````c
/****************************************************************************
 *                                niScope                                   *
 *--------------------------------------------------------------------------*
 *   Copyright (c) National Instruments 2004-2022.  All Rights Reserved.    *
 *--------------------------------------------------------------------------*
 *                                                                          *
 * Title:    niScope.h                                                      *
 * Purpose:  niScope                                                        *
 *           instrument driver declarations.                                *
 *                                                                          *
 ****************************************************************************/

#ifndef __NISCOPE_HEADER
#define __NISCOPE_HEADER

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "ivi.h"
#include "IviScope.h"
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <string.h>


#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif


/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NISCOPE_MAJOR_VERSION                                                  22                                                            // Instrument driver major version
#define NISCOPE_MINOR_VERSION                                                  500                                                           // Instrument driver minor version


/****************************************************************************
 *---------------------- Useful Macros and Defines -------------------------*
 ****************************************************************************/
/* Maximum length of a niscope function name */
#define MAX_FUNCTION_NAME_SIZE      55
/* Maximum size of an error message returned from niScope_errorHandler */
#define MAX_ERROR_DESCRIPTION       (IVI_MAX_MESSAGE_BUF_SIZE * 2 + MAX_FUNCTION_NAME_SIZE + 75)

/* This macro handles all errors and warnings returned from NI SCOPE.
   It requires two variables be declared:
      ViStatus error
      ViChar errorSource[MAX_FUNCTION_NAME_SIZE]
   and a line marked "Error:" that marks the beginning of cleanup code.
   If a function returns an error code, "error" is set to the error code
   and "errorSource" is set to the calling function's name, and execution
   skips to the "Error:" line.  Otherwise, "error" and "errorSource" store
   the location of warnings that occur, and execution proceeds normally.    */
#define handleErr(fCall) {                                           \
        int code = (fCall);                                          \
        if (code != 0) {                                             \
           const char* fCallSrc = #fCall;                            \
           const char* funcName = fCallSrc + strspn(fCallSrc, " ("); \
           size_t funcNameLen = strcspn(funcName, " (");             \
           if (funcNameLen > MAX_FUNCTION_NAME_SIZE - 1)             \
              funcNameLen = MAX_FUNCTION_NAME_SIZE - 1;              \
           if (code < 0) {                                           \
              error = code;                                          \
              strncpy(errorSource, funcName, funcNameLen);           \
              errorSource[funcNameLen] = '\0';                       \
              goto Error; }                                          \
           else if ((error == 0) && (code > 0)) {                    \
              error = code;                                          \
              strncpy(errorSource, funcName, funcNameLen);           \
              errorSource[funcNameLen] = '\0'; } } }

/* Use this macro to set a customized error elaboration for a particular function
   call.  The overwrite parameter in Ivi_SetErrorInfo is set to VI_TRUE so this
   macro will overwrite the default error elaboration that is on the error queue. */
#define niScopeCheckParm(fCall, paramPosition, errorElaboration)                        \
        if (error = (fCall), (error = (error < 0) ? (error) : VI_SUCCESS))              \
           {Ivi_SetErrorInfo(vi, VI_TRUE, error, Ivi_ParamPositionError(paramPosition), \
           errorElaboration); goto Error;} else

/* Use this macro in the same manner as above but for cases where it is not a user
   set parameter that is in error
   Let errors over-ride warnings, but if there's no error or warning don't clear the
   previous warning!  If there are TWO warnings, then the new one will take precedence. */
#define niScopeCheckErrElab(fCall,elab)                              \
   {  int tempErrorForElab = (fCall);                                \
      if (tempErrorForElab < 0)                                      \
      {                                                              \
         Ivi_SetErrorInfo(vi, VI_TRUE, tempErrorForElab, 0, elab);   \
         error = tempErrorForElab;                                   \
         goto Error;                                                 \
      }                                                              \
      else if (tempErrorForElab > 0)                                 \
      {                                                              \
         Ivi_SetErrorInfo(vi, VI_TRUE, tempErrorForElab, 0, elab);   \
         error = tempErrorForElab;                                   \
      }                                                              \
   }

/* WARNING: These are overrides of some of the IVI macros to preserve warnings.
   These changes should ONLY affect the way warnings are dealt with.  However,
   there are other functions that may erase warning messages. */
#ifdef viCheckErrElab
#undef viCheckErrElab
#define viCheckErrElab(fCall, elab)                            \
   {                                                           \
      int code = (fCall);                                      \
      if (code < 0)                                            \
      {                                                        \
         error = code;                                         \
         Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, elab);       \
         goto Error;                                           \
      }                                                        \
      if ((error == 0) && (code > 0))                          \
      {                                                        \
         error = code;                                         \
         Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, elab);       \
      }                                                        \
   }
#endif


/* checkErr shouldn't ignore warning messages, so this is an override of the IVI version. */
#ifdef checkErr
#undef checkErr
#define checkErr(fCall)                                        \
   {  int code = (fCall);                                      \
      if (code < 0)                                            \
      {                                                        \
         error = code;                                         \
         goto Error;                                           \
      }                                                        \
      else if ((error == 0) && (code > 0))                     \
      {                                                        \
         error = code;                                         \
      }                                                        \
   }
#endif


#ifdef viCheckErr
#undef viCheckErr
#define viCheckErr(fCall)                                      \
   {                                                           \
      int code = (fCall);                                      \
      if (code < 0)                                            \
      {                                                        \
         error = code;                                         \
         Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL);    \
         goto Error;                                           \
      }                                                        \
      if ((error == 0) && (code > 0))                          \
      {                                                        \
         error = code;                                         \
         Ivi_SetErrorInfo(vi, VI_FALSE, error, 0, VI_NULL);    \
      }                                                        \
   }
#endif


/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/
 /*- NOTE: multi channel denotes an attribute specified on a per channel basis -*/

// -- User Options --
#define NISCOPE_ATTR_CACHE                                                     IVI_ATTR_CACHE                                                // 1050004 (0x100594), ViBoolean
#define NISCOPE_ATTR_RANGE_CHECK                                               IVI_ATTR_RANGE_CHECK                                          // 1050002 (0x100592), ViBoolean
#define NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS                                   IVI_ATTR_QUERY_INSTRUMENT_STATUS                              // 1050003 (0x100593), ViBoolean
#define NISCOPE_ATTR_RECORD_COERCIONS                                          IVI_ATTR_RECORD_COERCIONS                                     // 1050006 (0x100596), ViBoolean
#define NISCOPE_ATTR_SIMULATE                                                  IVI_ATTR_SIMULATE                                             // 1050005 (0x100595), ViBoolean
#define NISCOPE_ATTR_INTERCHANGE_CHECK                                         IVI_ATTR_INTERCHANGE_CHECK                                    // 1050021 (0x1005a5), ViBoolean

// -- Instrument Capabilities --
#define NISCOPE_ATTR_CHANNEL_COUNT                                             IVI_ATTR_CHANNEL_COUNT                                        // 1050203 (0x10065b), ViInt32,    read-only
#define NISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS                               IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS                          // 1050327 (0x1006d7), ViString,   read-only
#define NISCOPE_ATTR_GROUP_CAPABILITIES                                        IVI_ATTR_GROUP_CAPABILITIES                                   // 1050401 (0x100721), ViString,   read-only

// -- Instrument Version And Identification --
#define NISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION                               IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION                          // 1050514 (0x100792), ViString,   read-only
#define NISCOPE_ATTR_SPECIFIC_DRIVER_PREFIX                                    IVI_ATTR_SPECIFIC_DRIVER_PREFIX                               // 1050302 (0x1006be), ViString,   read-only
#define NISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR                                    IVI_ATTR_SPECIFIC_DRIVER_VENDOR                               // 1050513 (0x100791), ViString,   read-only
#define NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION                  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION             // 1050515 (0x100793), ViInt32,    read-only
#define NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION                  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION             // 1050516 (0x100794), ViInt32,    read-only
#define NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION                                  IVI_ATTR_SPECIFIC_DRIVER_REVISION                             // 1050551 (0x1007b7), ViString,   read-only
#define NISCOPE_ATTR_INSTRUMENT_MANUFACTURER                                   IVI_ATTR_INSTRUMENT_MANUFACTURER                              // 1050511 (0x10078f), ViString,   read-only
#define NISCOPE_ATTR_INSTRUMENT_MODEL                                          IVI_ATTR_INSTRUMENT_MODEL                                     // 1050512 (0x100790), ViString,   read-only
#define NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION                              IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION                         // 1050510 (0x10078e), ViString,   read-only

// -- Advanced Session Information --
#define NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR                                    IVI_ATTR_IO_RESOURCE_DESCRIPTOR                               // 1050304 (0x1006c0), ViString,   read-only
#define NISCOPE_ATTR_LOGICAL_NAME                                              IVI_ATTR_LOGICAL_NAME                                         // 1050305 (0x1006c1), ViString,   read-only
#define NISCOPE_ATTR_DRIVER_SETUP                                              IVI_ATTR_DRIVER_SETUP                                         // 1050007 (0x100597), ViString,   read-only

// -- Acquisition Subsystem --
#define NISCOPE_ATTR_ACQUISITION_TYPE                                          IVISCOPE_ATTR_ACQUISITION_TYPE                                // 1250101 (0x131335), ViInt32
#define NISCOPE_ATTR_SAMPLE_MODE                                               IVISCOPE_ATTR_SAMPLE_MODE                                     // 1250106 (0x13133a), ViInt32,    read-only

// -- Vertical Subsystem --
#define NISCOPE_ATTR_CHANNEL_ENABLED                                           IVISCOPE_ATTR_CHANNEL_ENABLED                                 // 1250005 (0x1312d5), ViBoolean,  multi-channel
#define NISCOPE_ATTR_PROBE_ATTENUATION                                         IVISCOPE_ATTR_PROBE_ATTENUATION                               // 1250004 (0x1312d4), ViReal64,   multi-channel
#define NISCOPE_ATTR_VERTICAL_RANGE                                            IVISCOPE_ATTR_VERTICAL_RANGE                                  // 1250001 (0x1312d1), ViReal64,   multi-channel
#define NISCOPE_ATTR_VERTICAL_OFFSET                                           IVISCOPE_ATTR_VERTICAL_OFFSET                                 // 1250002 (0x1312d2), ViReal64,   multi-channel
#define NISCOPE_ATTR_VERTICAL_COUPLING                                         IVISCOPE_ATTR_VERTICAL_COUPLING                               // 1250003 (0x1312d3), ViInt32,    multi-channel
#define NISCOPE_ATTR_MAX_INPUT_FREQUENCY                                       IVISCOPE_ATTR_MAX_INPUT_FREQUENCY                             // 1250006 (0x1312d6), ViReal64,   multi-channel
#define NISCOPE_ATTR_INPUT_IMPEDANCE                                           IVISCOPE_ATTR_INPUT_IMPEDANCE                                 // 1250103 (0x131337), ViReal64,   multi-channel

// -- Horizontal Subsystem --
#define NISCOPE_ATTR_HORZ_TIME_PER_RECORD                                      IVISCOPE_ATTR_HORZ_TIME_PER_RECORD                            // 1250007 (0x1312d7), ViReal64
#define NISCOPE_ATTR_ACQUISITION_START_TIME                                    IVISCOPE_ATTR_ACQUISITION_START_TIME                          // 1250109 (0x13133d), ViReal64
#define NISCOPE_ATTR_HORZ_MIN_NUM_PTS                                          IVISCOPE_ATTR_HORZ_MIN_NUM_PTS                                // 1250009 (0x1312d9), ViInt32
#define NISCOPE_ATTR_HORZ_RECORD_LENGTH                                        IVISCOPE_ATTR_HORZ_RECORD_LENGTH                              // 1250008 (0x1312d8), ViInt32,    read-only
#define NISCOPE_ATTR_HORZ_RECORD_REF_POSITION                                  (IVI_CLASS_PUBLIC_ATTR_BASE + 11L)                            // 1250011 (0x1312db), ViReal64
#define NISCOPE_ATTR_HORZ_SAMPLE_RATE                                          IVISCOPE_ATTR_HORZ_SAMPLE_RATE                                // 1250010 (0x1312da), ViReal64,   read-only

// -- Trigger Subsystem --
#define NISCOPE_ATTR_TRIGGER_TYPE                                              IVISCOPE_ATTR_TRIGGER_TYPE                                    // 1250012 (0x1312dc), ViInt32
#define NISCOPE_ATTR_TRIGGER_SOURCE                                            IVISCOPE_ATTR_TRIGGER_SOURCE                                  // 1250013 (0x1312dd), ViString
#define NISCOPE_ATTR_TRIGGER_LEVEL                                             IVISCOPE_ATTR_TRIGGER_LEVEL                                   // 1250017 (0x1312e1), ViReal64
#define NISCOPE_ATTR_TRIGGER_DELAY_TIME                                        (IVI_CLASS_PUBLIC_ATTR_BASE + 15L)                            // 1250015 (0x1312df), ViReal64
#define NISCOPE_ATTR_TRIGGER_HOLDOFF                                           IVISCOPE_ATTR_TRIGGER_HOLDOFF                                 // 1250016 (0x1312e0), ViReal64
#define NISCOPE_ATTR_TRIGGER_COUPLING                                          IVISCOPE_ATTR_TRIGGER_COUPLING                                // 1250014 (0x1312de), ViInt32
#define NISCOPE_ATTR_TRIGGER_SLOPE                                             IVISCOPE_ATTR_TRIGGER_SLOPE                                   // 1250018 (0x1312e2), ViInt32

// -- Iviscopetvtrigger Extension --
#define NISCOPE_ATTR_TV_TRIGGER_EVENT                                          IVISCOPE_ATTR_TV_TRIGGER_EVENT                                // 1250205 (0x13139d), ViInt32
#define NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER                                    IVISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER                          // 1250206 (0x13139e), ViInt32
#define NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT                                  IVISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT                        // 1250201 (0x131399), ViInt32
#define NISCOPE_ATTR_TV_TRIGGER_POLARITY                                       IVISCOPE_ATTR_TV_TRIGGER_POLARITY                             // 1250204 (0x13139c), ViInt32

// -- Iviscopeglitchtrigger Extension --
#define NISCOPE_ATTR_GLITCH_CONDITION                                          IVISCOPE_ATTR_GLITCH_CONDITION                                // 1250403 (0x131463), ViInt32
#define NISCOPE_ATTR_GLITCH_WIDTH                                              IVISCOPE_ATTR_GLITCH_WIDTH                                    // 1250401 (0x131461), ViReal64
#define NISCOPE_ATTR_GLITCH_POLARITY                                           IVISCOPE_ATTR_GLITCH_POLARITY                                 // 1250402 (0x131462), ViInt32

// -- Iviscopewidthtrigger Extension --
#define NISCOPE_ATTR_WIDTH_CONDITION                                           IVISCOPE_ATTR_WIDTH_CONDITION                                 // 1250504 (0x1314c8), ViInt32
#define NISCOPE_ATTR_WIDTH_LOW_THRESHOLD                                       IVISCOPE_ATTR_WIDTH_LOW_THRESHOLD                             // 1250501 (0x1314c5), ViReal64
#define NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD                                      IVISCOPE_ATTR_WIDTH_HIGH_THRESHOLD                            // 1250502 (0x1314c6), ViReal64
#define NISCOPE_ATTR_WIDTH_POLARITY                                            IVISCOPE_ATTR_WIDTH_POLARITY                                  // 1250503 (0x1314c7), ViInt32

// -- Iviscoperunttrigger Extension --
#define NISCOPE_ATTR_RUNT_POLARITY                                             IVISCOPE_ATTR_RUNT_POLARITY                                   // 1250303 (0x1313ff), ViInt32
#define NISCOPE_ATTR_RUNT_LOW_THRESHOLD                                        IVISCOPE_ATTR_RUNT_LOW_THRESHOLD                              // 1250302 (0x1313fe), ViReal64
#define NISCOPE_ATTR_RUNT_HIGH_THRESHOLD                                       IVISCOPE_ATTR_RUNT_HIGH_THRESHOLD                             // 1250301 (0x1313fd), ViReal64

// -- Measurement Functions --
#define NISCOPE_ATTR_MEAS_HIGH_REF                                             IVISCOPE_ATTR_MEAS_HIGH_REF                                   // 1250607 (0x13152f), ViReal64
#define NISCOPE_ATTR_MEAS_LOW_REF                                              IVISCOPE_ATTR_MEAS_LOW_REF                                    // 1250608 (0x131530), ViReal64
#define NISCOPE_ATTR_MEAS_MID_REF                                              IVISCOPE_ATTR_MEAS_MID_REF                                    // 1250609 (0x131531), ViReal64

// -- Additional Instrument-Specific Attributes --
#define NISCOPE_ATTR_HORZ_NUM_RECORDS                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1L)                          // 1150001 (0x118c31), ViInt32
#define NISCOPE_ATTR_INPUT_CLOCK_SOURCE                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 2L)                          // 1150002 (0x118c32), ViString
#define NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 3L)                          // 1150003 (0x118c33), ViString
#define NISCOPE_ATTR_HORZ_ENFORCE_REALTIME                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 4L)                          // 1150004 (0x118c34), ViBoolean
#define NISCOPE_ATTR_BINARY_SAMPLE_WIDTH                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 5L)                          // 1150005 (0x118c35), ViInt32
#define NISCOPE_ATTR_TRIGGER_HYSTERESIS                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 6L)                          // 1150006 (0x118c36), ViReal64
#define NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 7L)                          // 1150007 (0x118c37), ViString
#define NISCOPE_ATTR_MASTER_ENABLE                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 8L)                          // 1150008 (0x118c38), ViBoolean
#define NISCOPE_ATTR_MIN_SAMPLE_RATE                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 9L)                          // 1150009 (0x118c39), ViReal64
#define NISCOPE_ATTR_TRIGGER_WINDOW_MODE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 12L)                         // 1150012 (0x118c3c), ViInt32
#define NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 13L)                         // 1150013 (0x118c3d), ViReal64
#define NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 14L)                         // 1150014 (0x118c3e), ViReal64
#define NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 16L)                         // 1150016 (0x118c40), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_OTHER_CHANNEL                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 18L)                         // 1150018 (0x118c42), ViString,   multi-channel
#define NISCOPE_ATTR_MEAS_HYSTERESIS_PERCENT                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 19L)                         // 1150019 (0x118c43), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_LAST_ACQ_HISTOGRAM_SIZE                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 20L)                         // 1150020 (0x118c44), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 21L)                         // 1150021 (0x118c45), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 22L)                         // 1150022 (0x118c46), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 23L)                         // 1150023 (0x118c47), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 24L)                         // 1150024 (0x118c48), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 25L)                         // 1150025 (0x118c49), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 26L)                         // 1150026 (0x118c4a), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 27L)                         // 1150027 (0x118c4b), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 28L)                         // 1150028 (0x118c4c), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_POLYNOMIAL_INTERPOLATION_ORDER                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 29L)                         // 1150029 (0x118c4d), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_INTERPOLATION_SAMPLING_FACTOR                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 30L)                         // 1150030 (0x118c4e), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_CUTOFF_FREQ                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 31L)                         // 1150031 (0x118c4f), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 32L)                         // 1150032 (0x118c50), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_RIPPLE                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 33L)                         // 1150033 (0x118c51), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 34L)                         // 1150034 (0x118c52), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_TYPE                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 35L)                         // 1150035 (0x118c53), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_ORDER                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 36L)                         // 1150036 (0x118c54), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_TAPS                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 37L)                         // 1150037 (0x118c55), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 38L)                         // 1150038 (0x118c56), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 39L)                         // 1150039 (0x118c57), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 40L)                         // 1150040 (0x118c58), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FILTER_WIDTH                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 41L)                         // 1150041 (0x118c59), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 42L)                         // 1150042 (0x118c5a), ViInt32,    multi-channel
#define NISCOPE_ATTR_MEAS_ARRAY_GAIN                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 43L)                         // 1150043 (0x118c5b), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_ARRAY_OFFSET                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 44L)                         // 1150044 (0x118c5c), ViReal64,   multi-channel
#define NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 45L)                         // 1150045 (0x118c5d), ViInt32,    multi-channel

// -- Advanced Synchronization Attributes --
#define NISCOPE_ATTR_ACQ_ARM_SOURCE                                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 53L)                         // 1150053 (0x118c65), ViString
#define NISCOPE_ATTR_IS_PROBE_COMP_ON                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 66L)                         // 1150066 (0x118c72), ViBoolean,  read-only
#define NISCOPE_ATTR_USE_SPEC_INITIAL_X                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 67L)                         // 1150067 (0x118c73), ViBoolean
#define NISCOPE_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 68L)                         // 1150068 (0x118c74), ViBoolean
#define NISCOPE_ATTR_ONBOARD_MEMORY_SIZE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 69L)                         // 1150069 (0x118c75), ViInt32,    read-only
#define NISCOPE_ATTR_RIS_NUM_AVERAGES                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 70L)                         // 1150070 (0x118c76), ViInt32
#define NISCOPE_ATTR_RIS_METHOD                                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 71L)                         // 1150071 (0x118c77), ViInt32
#define NISCOPE_ATTR_FETCH_INTERLEAVED_DATA                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 72L)                         // 1150072 (0x118c78), ViBoolean
#define NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 73L)                         // 1150073 (0x118c79), ViReal64,   read-only
#define NISCOPE_ATTR_MAX_RIS_RATE                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 74L)                         // 1150074 (0x118c7a), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_IMPEDANCE                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 75L)                         // 1150075 (0x118c7b), ViReal64
#define NISCOPE_ATTR_DEVICE_NUMBER                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 76L)                         // 1150076 (0x118c7c), ViInt32,    read-only
#define NISCOPE_ATTR_FETCH_RELATIVE_TO                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 77L)                         // 1150077 (0x118c7d), ViInt32
#define NISCOPE_ATTR_FETCH_OFFSET                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 78L)                         // 1150078 (0x118c7e), ViInt32
#define NISCOPE_ATTR_FETCH_RECORD_NUMBER                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 79L)                         // 1150079 (0x118c7f), ViInt32
#define NISCOPE_ATTR_FETCH_NUM_RECORDS                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 80L)                         // 1150080 (0x118c80), ViInt32
#define NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 81L)                         // 1150081 (0x118c81), ViInt32
#define NISCOPE_ATTR_POINTS_DONE                                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 82L)                         // 1150082 (0x118c82), ViReal64,   read-only
#define NISCOPE_ATTR_RECORDS_DONE                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 83L)                         // 1150083 (0x118c83), ViInt32,    read-only
#define NISCOPE_ATTR_BACKLOG                                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 84L)                         // 1150084 (0x118c84), ViReal64,   read-only
#define NISCOPE_ATTR_POLL_INTERVAL                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 100L)                        // 1150100 (0x118c94), ViInt32
#define NISCOPE_ATTR_PLL_LOCK_STATUS                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1303L)                       // 1151303 (0x119147), ViBoolean,  read-only

// -- New Attributes For Ni-Scope 2.5 --
#define NISCOPE_ATTR_DEVICE_TEMPERATURE                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 86L)                         // 1150086 (0x118c86), ViReal64,   read-only
#define NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 87L)                         // 1150087 (0x118c87), ViString
#define NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 88L)                         // 1150088 (0x118c88), ViReal64
#define NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 89L)                         // 1150089 (0x118c89), ViInt32
#define NISCOPE_ATTR_REF_CLK_RATE                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 90L)                         // 1150090 (0x118c8a), ViReal64
#define NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 91L)                         // 1150091 (0x118c8b), ViString
#define NISCOPE_ATTR_ENABLE_DC_RESTORE                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 93L)                         // 1150093 (0x118c8d), ViBoolean
#define NISCOPE_ATTR_ADV_TRIG_SRC                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 94L)                         // 1150094 (0x118c8e), ViString
#define NISCOPE_ATTR_ARM_REF_TRIG_SRC                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 95L)                         // 1150095 (0x118c8f), ViString
#define NISCOPE_ATTR_REF_TRIG_TDC_ENABLE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 96L)                         // 1150096 (0x118c90), ViBoolean
#define NISCOPE_ATTR_RESOLUTION                                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 102L)                        // 1150102 (0x118c96), ViInt32,    read-only

// -- New Attributes For Ni-Scope 2.6 --
#define NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 103L)                        // 1150103 (0x118c97), ViReal64

// -- New Attributes For Ni-Scope 2.7 --
#define NISCOPE_ATTR_SERIAL_NUMBER                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 104L)                        // 1150104 (0x118c98), ViString,   read-only
#define NISCOPE_ATTR_OSCILLATOR_PHASE_DAC_VALUE                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 105L)                        // 1150105 (0x118c99), ViInt32

// -- New Attributes For Ni-Scope 2.8 --
#define NISCOPE_ATTR_RIS_IN_AUTO_SETUP_ENABLE                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 106L)                        // 1150106 (0x118c9a), ViBoolean
#define NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 107L)                        // 1150107 (0x118c9b), ViInt32,    multi-channel
#define NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 109L)                        // 1150109 (0x118c9d), ViString
#define NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 110L)                        // 1150110 (0x118c9e), ViString
#define NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 111L)                        // 1150111 (0x118c9f), ViString
#define NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 112L)                        // 1150112 (0x118ca0), ViString

// -- New Attributes For Ni-Scope 2.9.1 --
#define NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 271L)                        // 1150271 (0x118d3f), ViInt32,    multi-channel

// -- New Attributes For Ni-Scope 3.0. Attributes For The Ni 5142 & 5622 Osp Functionality. --
#define NISCOPE_ATTR_DDC_ENABLED                                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 300L)                        // 1150300 (0x118d5c), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_ENABLED                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 302L)                        // 1150302 (0x118d5e), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_CENTER_FREQUENCY                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 303L)                        // 1150303 (0x118d5f), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 304L)                        // 1150304 (0x118d60), ViInt32
#define NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_I                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 305L)                        // 1150305 (0x118d61), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_Q                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 306L)                        // 1150306 (0x118d62), ViReal64,   multi-channel
#define NISCOPE_ATTR_DIGITAL_GAIN                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 307L)                        // 1150307 (0x118d63), ViReal64,   multi-channel
#define NISCOPE_ATTR_DIGITAL_OFFSET                                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 308L)                        // 1150308 (0x118d64), ViReal64,   multi-channel
#define NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 309L)                        // 1150309 (0x118d65), ViInt32
#define NISCOPE_ATTR_DDC_Q_SOURCE                                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 310L)                        // 1150310 (0x118d66), ViString,   multi-channel
#define NISCOPE_ATTR_FETCH_INTERLEAVED_IQ_DATA                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 311L)                        // 1150311 (0x118d67), ViBoolean

// -- New Attributes For Ni-Scope 3.1. --
#define NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 312L)                        // 1150312 (0x118d68), ViInt32,    multi-channel, read-only
#define NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 313L)                        // 1150313 (0x118d69), ViBoolean,  multi-channel
#define NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 314L)                        // 1150314 (0x118d6a), ViInt32
#define NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 315L)                        // 1150315 (0x118d6b), ViReal64

// -- New Attributes For Ni-Scope 3.2 --
#define NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 128L)                        // 1150128 (0x118cb0), ViBoolean,  multi-channel

// -- New Attributes For Ni-Scope 3.3 --
#define NISCOPE_ATTR_DATA_TRANSFER_BLOCK_SIZE                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 316L)                        // 1150316 (0x118d6c), ViInt32

// -- New Attributes For Ni-Scope 3.4 --
#define NISCOPE_ATTR_TRIGGER_MODIFIER                                          IVISCOPE_ATTR_TRIGGER_MODIFIER                                // 1250102 (0x131336), ViInt32
#define NISCOPE_ATTR_TRIGGER_AUTO_TRIGGERED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 278L)                        // 1150278 (0x118d46), ViBoolean,  read-only
#define NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 97L)                         // 1150097 (0x118c91), ViString
#define NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 98L)                         // 1150098 (0x118c92), ViString
#define NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 99L)                         // 1150099 (0x118c93), ViString
#define NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 101L)                        // 1150101 (0x118c95), ViString
#define NISCOPE_ATTR_5V_OUT_OUTPUT_TERMINAL                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 129L)                        // 1150129 (0x118cb1), ViString

// -- New Attributes For Ni-Scope 3.5 --
#define NISCOPE_ATTR_BANDPASS_FILTER_ENABLED                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 318L)                        // 1150318 (0x118d6e), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DITHER_ENABLED                                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 319L)                        // 1150319 (0x118d6f), ViBoolean,  multi-channel
#define NISCOPE_ATTR_FRACTIONAL_RESAMPLE_ENABLED                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 320L)                        // 1150320 (0x118d70), ViBoolean
#define NISCOPE_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 321L)                        // 1150321 (0x118d71), ViReal64
#define NISCOPE_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 322L)                        // 1150322 (0x118d72), ViInt32

// -- Ni-5900 Specific Definitions --
#define NISCOPE_ATTR_SIGNAL_COND_GAIN                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 279L)                        // 1150279 (0x118d47), ViReal64,   multi-channel, read-only
#define NISCOPE_ATTR_SIGNAL_COND_OFFSET                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 280L)                        // 1150280 (0x118d48), ViReal64,   multi-channel, read-only

// -- New Attributes For Ni-Scope 3.6, Peer-To-Peer --
#define NISCOPE_ATTR_P2P_ENABLED                                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 338L)                        // 1150338 (0x118d82), ViBoolean
#define NISCOPE_ATTR_P2P_CHANNELS_TO_STREAM                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 339L)                        // 1150339 (0x118d83), ViString
#define NISCOPE_ATTR_P2P_ENDPOINT_SIZE                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 342L)                        // 1150342 (0x118d86), ViInt32,    read-only
#define NISCOPE_ATTR_P2P_SAMPLES_AVAIL_IN_ENDPOINT                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 328L)                        // 1150328 (0x118d78), ViInt32,    read-only
#define NISCOPE_ATTR_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 341L)                        // 1150341 (0x118d85), ViInt32,    read-only
#define NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 340L)                        // 1150340 (0x118d84), ViInt64,    read-only
#define NISCOPE_ATTR_P2P_ENDPOINT_OVERFLOW                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 344L)                        // 1150344 (0x118d88), ViBoolean,  read-only
#define NISCOPE_ATTR_P2P_FIFO_ENDPOINT_COUNT                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 345L)                        // 1150345 (0x118d89), ViInt32,    read-only
#define NISCOPE_ATTR_P2P_ONBOARD_MEMORY_ENABLED                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 354L)                        // 1150354 (0x118d92), ViBoolean
#define NISCOPE_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 343L)                        // 1150343 (0x118d87), ViBoolean
#define NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 329L)                        // 1150329 (0x118d79), ViInt64,    read-only
#define NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 330L)                        // 1150330 (0x118d7a), ViInt32
#define NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 331L)                        // 1150331 (0x118d7b), ViInt64
#define NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 332L)                        // 1150332 (0x118d7c), ViInt32
#define NISCOPE_ATTR_P2P_DESTINATION_WINDOW_SIZE                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 333L)                        // 1150333 (0x118d7d), ViInt64
#define NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 334L)                        // 1150334 (0x118d7e), ViInt32
#define NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 335L)                        // 1150335 (0x118d7f), ViInt64
#define NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 336L)                        // 1150336 (0x118d80), ViInt32
#define NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_VALUE                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 337L)                        // 1150337 (0x118d81), ViInt64

// -- New Attributes For Ni-Scope 3.8 --
#define NISCOPE_ATTR_SAMP_CLK_TIMEBASE_MULT                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 367L)                        // 1150367 (0x118d9f), ViInt32

// -- New Attributes For Ni-Scope 4.0, Peer-To-Peer --
#define NISCOPE_ATTR_P2P_STREAM_RELATIVE_TO                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 373L)                        // 1150373 (0x118da5), ViInt32
#define NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED_PER_RECORD                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 380L)                        // 1150380 (0x118dac), ViInt32,    read-only

// -- New Attributes For Ni-Scope 4.2 --
#define NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 366L)                        // 1150366 (0x118d9e), ViReal64

// -- New Attributes For Ni-Scope 15.1 --
#define NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 374L)                        // 1150374 (0x118da6), ViReal64
#define NISCOPE_ATTR_FPGA_BITFILE_PATH                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 375L)                        // 1150375 (0x118da7), ViString,   read-only

// -- New Attributes For Ni-Scope 16.1 --
#define NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 376L)                        // 1150376 (0x118da8), ViBoolean,  multi-channel
#define NISCOPE_ATTR_HIGH_PASS_FILTER_FREQUENCY                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 377L)                        // 1150377 (0x118da9), ViReal64,   multi-channel

// -- New Attributes For Ni-Scope 18.6 --
#define NISCOPE_ATTR_RUNT_TIME_CONDITION                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 132L)                        // 1150132 (0x118cb4), ViInt32
#define NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 133L)                        // 1150133 (0x118cb5), ViReal64
#define NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 134L)                        // 1150134 (0x118cb6), ViReal64

// -- New Attributes For Ni-Scope 18.7 --
#define NISCOPE_ATTR_CABLE_SENSE_VOLTAGE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 137L)                        // 1150137 (0x118cb9), ViReal64
#define NISCOPE_ATTR_CABLE_SENSE_MODE                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 138L)                        // 1150138 (0x118cba), ViReal64
#define NISCOPE_ATTR_CABLE_SENSE_SIGNAL_ENABLE                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 139L)                        // 1150139 (0x118cbb), ViBoolean

// -- New Attributes For Ni-Scope 19.0 --
#define NISCOPE_ATTR_ENABLED_CHANNELS                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 140L)                        // 1150140 (0x118cbc), ViString,   read-only

// -- New Attributes For Ni-Scope 20.0 --
#define NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_TERMINAL_NAME                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 141L)                        // 1150141 (0x118cbd), ViString,   read-only
#define NISCOPE_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 142L)                        // 1150142 (0x118cbe), ViString,   read-only
#define NISCOPE_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 143L)                        // 1150143 (0x118cbf), ViString,   read-only
#define NISCOPE_ATTR_REF_TRIGGER_TERMINAL_NAME                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 144L)                        // 1150144 (0x118cc0), ViString,   read-only
#define NISCOPE_ATTR_START_TRIGGER_TERMINAL_NAME                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 145L)                        // 1150145 (0x118cc1), ViString,   read-only
#define NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 146L)                        // 1150146 (0x118cc2), ViString,   read-only
#define NISCOPE_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 147L)                        // 1150147 (0x118cc3), ViString,   read-only
#define NISCOPE_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 148L)                        // 1150148 (0x118cc4), ViString,   read-only


/****************************************************************************
 *------------------ Attribute and Parameter Value Defines -----------------*
 ****************************************************************************/
// Values used in
//     NISCOPE_ATTR_RIS_METHOD
#define NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES                                     1                                                             // 1 (0x1)
#define NISCOPE_VAL_RIS_MIN_NUM_AVERAGES                                       2                                                             // 2 (0x2)
#define NISCOPE_VAL_RIS_INCOMPLETE                                             3                                                             // 3 (0x3)
#define NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH                                      5                                                             // 5 (0x5)

// Values used in
//     niScope_SendSoftwareTriggerEdge
#define NISCOPE_VAL_SOFTWARE_TRIGGER_START                                     0                                                             // 0 (0x0)
#define NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE                             1                                                             // 1 (0x1)
#define NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE                                 2                                                             // 2 (0x2)
#define NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE                                   3                                                             // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_VERTICAL_COUPLING, niScope_ConfigureVertical
#define NISCOPE_VAL_AC                                                         IVISCOPE_VAL_AC                                               // 0 (0x0)
#define NISCOPE_VAL_DC                                                         IVISCOPE_VAL_DC                                               // 1 (0x1)
#define NISCOPE_VAL_GND                                                        IVISCOPE_VAL_GND                                              // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_MAX_INPUT_FREQUENCY
#define NISCOPE_VAL_BANDWIDTH_FULL                                             -1.0
#define NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT                                   0.0
#define NISCOPE_VAL_20MHZ_BANDWIDTH                                            20000000.0
#define NISCOPE_VAL_100MHZ_BANDWIDTH                                           100000000.0
#define NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY                                  20000000.0
#define NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY                                 100000000.0

// Values used in
//     NISCOPE_ATTR_INPUT_IMPEDANCE
#define NISCOPE_VAL_50_OHMS                                                    50.0
#define NISCOPE_VAL_75_OHMS                                                    75.0
#define NISCOPE_VAL_1_MEG_OHM                                                  1000000.0

// Values used in
//     NISCOPE_ATTR_TRIGGER_TYPE
#define NISCOPE_VAL_EDGE_TRIGGER                                               IVISCOPE_VAL_EDGE_TRIGGER                                     // 1 (0x1)
#define NISCOPE_VAL_HYSTERESIS_TRIGGER                                         (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 1L)            // 1001 (0x3e9)
#define NISCOPE_VAL_DIGITAL_TRIGGER                                            (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 2L)            // 1002 (0x3ea)
#define NISCOPE_VAL_WINDOW_TRIGGER                                             (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 3L)            // 1003 (0x3eb)
#define NISCOPE_VAL_SOFTWARE_TRIGGER                                           (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 4L)            // 1004 (0x3ec)
#define NISCOPE_VAL_TV_TRIGGER                                                 IVISCOPE_VAL_TV_TRIGGER                                       // 5 (0x5)
#define NISCOPE_VAL_GLITCH_TRIGGER                                             IVISCOPE_VAL_GLITCH_TRIGGER                                   // 4 (0x4)
#define NISCOPE_VAL_WIDTH_TRIGGER                                              IVISCOPE_VAL_WIDTH_TRIGGER                                    // 2 (0x2)
#define NISCOPE_VAL_RUNT_TRIGGER                                               IVISCOPE_VAL_RUNT_TRIGGER                                     // 3 (0x3)
#define NISCOPE_VAL_IMMEDIATE_TRIGGER                                          IVISCOPE_VAL_IMMEDIATE_TRIGGER                                // 6 (0x6)

// Values used in
//     NISCOPE_ATTR_TRIGGER_SOURCE
#define NISCOPE_VAL_IMMEDIATE                                                  "VAL_IMMEDIATE"
#define NISCOPE_VAL_EXTERNAL                                                   IVISCOPE_VAL_EXTERNAL
#define NISCOPE_VAL_SW_TRIG_FUNC                                               "VAL_SW_TRIG_FUNC"
#define NISCOPE_VAL_TTL0                                                       IVISCOPE_VAL_TTL0
#define NISCOPE_VAL_TTL1                                                       IVISCOPE_VAL_TTL1
#define NISCOPE_VAL_TTL2                                                       IVISCOPE_VAL_TTL2
#define NISCOPE_VAL_TTL3                                                       IVISCOPE_VAL_TTL3
#define NISCOPE_VAL_TTL4                                                       IVISCOPE_VAL_TTL4
#define NISCOPE_VAL_TTL5                                                       IVISCOPE_VAL_TTL5
#define NISCOPE_VAL_TTL6                                                       IVISCOPE_VAL_TTL6
#define NISCOPE_VAL_TTL7                                                       IVISCOPE_VAL_TTL7
#define NISCOPE_VAL_ECL0                                                       IVISCOPE_VAL_ECL0
#define NISCOPE_VAL_ECL1                                                       IVISCOPE_VAL_ECL1
#define NISCOPE_VAL_PXI_STAR                                                   IVISCOPE_VAL_PXI_STAR
#define NISCOPE_VAL_RTSI_0                                                     IVISCOPE_VAL_RTSI_0
#define NISCOPE_VAL_RTSI_1                                                     IVISCOPE_VAL_RTSI_1
#define NISCOPE_VAL_RTSI_2                                                     IVISCOPE_VAL_RTSI_2
#define NISCOPE_VAL_RTSI_3                                                     IVISCOPE_VAL_RTSI_3
#define NISCOPE_VAL_RTSI_4                                                     IVISCOPE_VAL_RTSI_4
#define NISCOPE_VAL_RTSI_5                                                     IVISCOPE_VAL_RTSI_5
#define NISCOPE_VAL_RTSI_6                                                     IVISCOPE_VAL_RTSI_6
#define NISCOPE_VAL_RTSI_7                                                     "VAL_RTSI_7"
#define NISCOPE_VAL_PFI_0                                                      "VAL_PFI_0"
#define NISCOPE_VAL_PFI_1                                                      "VAL_PFI_1"
#define NISCOPE_VAL_PFI_2                                                      "VAL_PFI_2"
#define NISCOPE_VAL_PFI_3                                                      "VAL_PFI_3"
#define NISCOPE_VAL_PFI_4                                                      "VAL_PFI_4"
#define NISCOPE_VAL_PFI_5                                                      "VAL_PFI_5"
#define NISCOPE_VAL_PFI_6                                                      "VAL_PFI_6"
#define NISCOPE_VAL_PFI_7                                                      "VAL_PFI_7"
#define NISCOPE_VAL_AUX_0_PFI_0                                                "VAL_AUX_0_PFI_0"
#define NISCOPE_VAL_AUX_0_PFI_1                                                "VAL_AUX_0_PFI_1"
#define NISCOPE_VAL_AUX_0_PFI_3                                                "VAL_AUX_0_PFI_3"
#define NISCOPE_VAL_AUX_0_PFI_4                                                "VAL_AUX_0_PFI_4"
#define NISCOPE_VAL_AUX_0_PFI_5                                                "VAL_AUX_0_PFI_5"
#define NISCOPE_VAL_AUX_0_PFI_6                                                "VAL_AUX_0_PFI_6"
#define NISCOPE_VAL_AUX_0_PFI_7                                                "VAL_AUX_0_PFI_7"
#define NISCOPE_VAL_AUX_0_PFI_2                                                "VAL_AUX_0_PFI_2"

// Values used in
//     NISCOPE_ATTR_FETCH_RELATIVE_TO
#define NISCOPE_VAL_READ_POINTER                                               388                                                           // 388 (0x184)
#define NISCOPE_VAL_PRETRIGGER                                                 477                                                           // 477 (0x1dd)
#define NISCOPE_VAL_NOW                                                        481                                                           // 481 (0x1e1)
#define NISCOPE_VAL_START                                                      482                                                           // 482 (0x1e2)
#define NISCOPE_VAL_TRIGGER                                                    483                                                           // 483 (0x1e3)

// Values used in
//     NISCOPE_ATTR_TRIGGER_MODIFIER
#define NISCOPE_VAL_NO_TRIGGER_MOD                                             IVISCOPE_VAL_NO_TRIGGER_MOD                                   // 1 (0x1)
#define NISCOPE_VAL_AUTO                                                       IVISCOPE_VAL_AUTO                                             // 2 (0x2)
#define NISCOPE_VAL_AUTO_LEVEL                                                 IVISCOPE_VAL_AUTO_LEVEL                                       // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_TRIGGER_COUPLING, niScope_ConfigureTriggerEdge, niScope_ConfigureTriggerGlitch,
//     niScope_ConfigureTriggerHysteresis, niScope_ConfigureTriggerRunt, niScope_ConfigureTriggerVideo,
//     niScope_ConfigureTriggerWidth, niScope_ConfigureTriggerWindow
// #define NISCOPE_VAL_AC                                                      DEFINED ABOVE (IVISCOPE_VAL_AC)                               // 0 (0x0)
// #define NISCOPE_VAL_DC                                                      DEFINED ABOVE (IVISCOPE_VAL_DC)                               // 1 (0x1)
#define NISCOPE_VAL_HF_REJECT                                                  IVISCOPE_VAL_HF_REJECT                                        // 3 (0x3)
#define NISCOPE_VAL_LF_REJECT                                                  IVISCOPE_VAL_LF_REJECT                                        // 4 (0x4)
#define NISCOPE_VAL_AC_PLUS_HF_REJECT                                          (IVISCOPE_VAL_TRIGGER_COUPLING_SPECIFIC_EXT_BASE + 1L)        // 1001 (0x3e9)

// Values used in
//     NISCOPE_ATTR_TRIGGER_SLOPE, niScope_ConfigureTriggerDigital, niScope_ConfigureTriggerEdge,
//     niScope_ConfigureTriggerHysteresis
#define NISCOPE_VAL_NEGATIVE                                                   IVISCOPE_VAL_NEGATIVE                                         // 0 (0x0)
#define NISCOPE_VAL_POSITIVE                                                   IVISCOPE_VAL_POSITIVE                                         // 1 (0x1)
#define NISCOPE_VAL_SLOPE_EITHER                                               3                                                             // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_ACQUISITION_TYPE
#define NISCOPE_VAL_NORMAL                                                     IVISCOPE_VAL_NORMAL                                           // 0 (0x0)
#define NISCOPE_VAL_FLEXRES                                                    (IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE + 1L)        // 1001 (0x3e9)
#define NISCOPE_VAL_DDC                                                        (IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE + 2L)        // 1002 (0x3ea)

// Interpolation
#define NISCOPE_VAL_NO_INTERPOLATION                                           IVISCOPE_VAL_NO_INTERPOLATION                                 // 1 (0x1)
#define NISCOPE_VAL_SINE_X                                                     IVISCOPE_VAL_SINE_X                                           // 2 (0x2)
#define NISCOPE_VAL_LINEAR                                                     IVISCOPE_VAL_LINEAR                                           // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT
#define NISCOPE_VAL_NTSC                                                       IVISCOPE_VAL_NTSC                                             // 1 (0x1)
#define NISCOPE_VAL_PAL                                                        IVISCOPE_VAL_PAL                                              // 2 (0x2)
#define NISCOPE_VAL_SECAM                                                      IVISCOPE_VAL_SECAM                                            // 3 (0x3)
#define NISCOPE_VAL_M_PAL                                                      (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 1L)        // 1001 (0x3e9)
#define NISCOPE_VAL_480I_59_94_FIELDS_PER_SECOND                               (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 10L)       // 1010 (0x3f2)
#define NISCOPE_VAL_480I_60_FIELDS_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 11L)       // 1011 (0x3f3)
#define NISCOPE_VAL_480P_59_94_FRAMES_PER_SECOND                               (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 15L)       // 1015 (0x3f7)
#define NISCOPE_VAL_480P_60_FRAMES_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 16L)       // 1016 (0x3f8)
#define NISCOPE_VAL_576I_50_FIELDS_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 20L)       // 1020 (0x3fc)
#define NISCOPE_VAL_576P_50_FRAMES_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 25L)       // 1025 (0x401)
#define NISCOPE_VAL_720P_50_FRAMES_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 31L)       // 1031 (0x407)
#define NISCOPE_VAL_720P_59_94_FRAMES_PER_SECOND                               (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 32L)       // 1032 (0x408)
#define NISCOPE_VAL_720P_60_FRAMES_PER_SECOND                                  (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 33L)       // 1033 (0x409)
#define NISCOPE_VAL_1080I_50_FIELDS_PER_SECOND                                 (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 40L)       // 1040 (0x410)
#define NISCOPE_VAL_1080I_59_94_FIELDS_PER_SECOND                              (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 41L)       // 1041 (0x411)
#define NISCOPE_VAL_1080I_60_FIELDS_PER_SECOND                                 (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 42L)       // 1042 (0x412)
#define NISCOPE_VAL_1080P_24_FRAMES_PER_SECOND                                 (IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE + 45L)       // 1045 (0x415)

// Values used in
//     NISCOPE_ATTR_TV_TRIGGER_POLARITY, niScope_ConfigureTriggerVideo
#define NISCOPE_VAL_TV_POSITIVE                                                IVISCOPE_VAL_TV_POSITIVE                                      // 1 (0x1)
#define NISCOPE_VAL_TV_NEGATIVE                                                IVISCOPE_VAL_TV_NEGATIVE                                      // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_TV_TRIGGER_EVENT, niScope_ConfigureTriggerVideo
#define NISCOPE_VAL_TV_EVENT_FIELD1                                            IVISCOPE_VAL_TV_EVENT_FIELD1                                  // 1 (0x1)
#define NISCOPE_VAL_TV_EVENT_FIELD2                                            IVISCOPE_VAL_TV_EVENT_FIELD2                                  // 2 (0x2)
#define NISCOPE_VAL_TV_EVENT_ANY_FIELD                                         IVISCOPE_VAL_TV_EVENT_ANY_FIELD                               // 3 (0x3)
#define NISCOPE_VAL_TV_EVENT_ANY_LINE                                          IVISCOPE_VAL_TV_EVENT_ANY_LINE                                // 4 (0x4)
#define NISCOPE_VAL_TV_EVENT_LINE_NUMBER                                       IVISCOPE_VAL_TV_EVENT_LINE_NUMBER                             // 5 (0x5)

// Values used in
//     NISCOPE_ATTR_GLITCH_CONDITION, niScope_ConfigureTriggerGlitch
#define NISCOPE_VAL_GLITCH_GREATER_THAN                                        IVISCOPE_VAL_GLITCH_GREATER_THAN                              // 2 (0x2)
#define NISCOPE_VAL_GLITCH_LESS_THAN                                           IVISCOPE_VAL_GLITCH_LESS_THAN                                 // 1 (0x1)

// Values used in
//     NISCOPE_ATTR_GLITCH_POLARITY, niScope_ConfigureTriggerGlitch
#define NISCOPE_VAL_GLITCH_POSITIVE                                            IVISCOPE_VAL_GLITCH_POSITIVE                                  // 1 (0x1)
#define NISCOPE_VAL_GLITCH_NEGATIVE                                            IVISCOPE_VAL_GLITCH_NEGATIVE                                  // 2 (0x2)
#define NISCOPE_VAL_GLITCH_EITHER                                              IVISCOPE_VAL_GLITCH_EITHER                                    // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_WIDTH_CONDITION, niScope_ConfigureTriggerWidth
#define NISCOPE_VAL_WIDTH_WITHIN                                               IVISCOPE_VAL_WIDTH_WITHIN                                     // 1 (0x1)
#define NISCOPE_VAL_WIDTH_OUTSIDE                                              IVISCOPE_VAL_WIDTH_OUTSIDE                                    // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_WIDTH_POLARITY, niScope_ConfigureTriggerWidth
#define NISCOPE_VAL_WIDTH_POSITIVE                                             IVISCOPE_VAL_WIDTH_POSITIVE                                   // 1 (0x1)
#define NISCOPE_VAL_WIDTH_NEGATIVE                                             IVISCOPE_VAL_WIDTH_NEGATIVE                                   // 2 (0x2)
#define NISCOPE_VAL_WIDTH_EITHER                                               IVISCOPE_VAL_WIDTH_EITHER                                     // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_RUNT_POLARITY, niScope_ConfigureTriggerRunt
#define NISCOPE_VAL_RUNT_POSITIVE                                              IVISCOPE_VAL_RUNT_POSITIVE                                    // 1 (0x1)
#define NISCOPE_VAL_RUNT_NEGATIVE                                              IVISCOPE_VAL_RUNT_NEGATIVE                                    // 2 (0x2)
#define NISCOPE_VAL_RUNT_EITHER                                                IVISCOPE_VAL_RUNT_EITHER                                      // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_RUNT_TIME_CONDITION
#define NISCOPE_VAL_RUNT_TIME_CONDITION_NONE                                   0                                                             // 0 (0x0)
#define NISCOPE_VAL_RUNT_TIME_CONDITION_WITHIN                                 1                                                             // 1 (0x1)
#define NISCOPE_VAL_RUNT_TIME_CONDITION_OUTSIDE                                2                                                             // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_CABLE_SENSE_MODE
#define NISCOPE_VAL_CABLE_SENSE_MODE_DISABLED                                  0                                                             // 0 (0x0)
#define NISCOPE_VAL_CABLE_SENSE_MODE_ON_DEMAND                                 1                                                             // 1 (0x1)

// Values used in
//     NISCOPE_ATTR_SAMPLE_MODE
#define NISCOPE_VAL_REAL_TIME                                                  IVISCOPE_VAL_REAL_TIME                                        // 0 (0x0)
#define NISCOPE_VAL_EQUIVALENT_TIME                                            IVISCOPE_VAL_EQUIVALENT_TIME                                  // 1 (0x1)

// Values used in
//     niScope_ConfigureClock, niScope_ExportSignal
#define NISCOPE_VAL_NO_SOURCE                                                  "VAL_NO_SOURCE"
#define NISCOPE_VAL_RTSI_CLOCK                                                 "VAL_RTSI_CLOCK"
// #define NISCOPE_VAL_EXTERNAL                                                DEFINED ABOVE (IVISCOPE_VAL_EXTERNAL)                        
// #define NISCOPE_VAL_PFI_0                                                   DEFINED ABOVE ("VAL_PFI_0")                                  
// #define NISCOPE_VAL_PFI_1                                                   DEFINED ABOVE ("VAL_PFI_1")                                  
// #define NISCOPE_VAL_PFI_2                                                   DEFINED ABOVE ("VAL_PFI_2")                                  
#define NISCOPE_VAL_CLK_IN                                                     "VAL_CLK_IN"
#define NISCOPE_VAL_CLK_OUT                                                    "VAL_CLK_OUT"
#define NISCOPE_VAL_INTERNAL10MHZ_OSC                                          "VAL_INTERNAL10MHZ_OSC"
#define NISCOPE_VAL_PXI_CLK                                                    "VAL_PXI_CLK"
#define NISCOPE_VAL_PXI_CLK10                                                  "VAL_PXI_CLK10"
#define NISCOPE_VAL_PXI_CLK100                                                 "VAL_PXI_CLK100"
#define NISCOPE_VAL_PXIE_DSTAR_A                                               "VAL_PXIE_DSTAR_A"
#define NISCOPE_VAL_AUX_0_CLK_IN                                               "VAL_AUX_0_CLK_IN"
#define NISCOPE_VAL_AUX_0_CLK_OUT                                              "VAL_AUX_0_CLK_OUT"
#define NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK                              "VAL_ONBOARD_CONFIGURABLE_RATE_CLK"

// Values used in
//     NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC
// #define NISCOPE_VAL_CLK_IN                                                  DEFINED ABOVE ("VAL_CLK_IN")                                 
// #define NISCOPE_VAL_NO_SOURCE                                               DEFINED ABOVE ("VAL_NO_SOURCE")                              
// #define NISCOPE_VAL_PXI_STAR                                                DEFINED ABOVE (IVISCOPE_VAL_PXI_STAR)                        
// #define NISCOPE_VAL_PXIE_DSTAR_A                                            DEFINED ABOVE ("VAL_PXIE_DSTAR_A")                           
// #define NISCOPE_VAL_AUX_0_CLK_IN                                            DEFINED ABOVE ("VAL_AUX_0_CLK_IN")                           
// #define NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK                           DEFINED ABOVE ("VAL_ONBOARD_CONFIGURABLE_RATE_CLK")          

// Values used in
//     niScope_ExportSignal
#define NISCOPE_VAL_REF_TRIGGER                                                1                                                             // 1 (0x1)
#define NISCOPE_VAL_START_TRIGGER                                              2                                                             // 2 (0x2)
#define NISCOPE_VAL_END_OF_ACQUISITION_EVENT                                   3                                                             // 3 (0x3)
#define NISCOPE_VAL_END_OF_RECORD_EVENT                                        4                                                             // 4 (0x4)
#define NISCOPE_VAL_ADVANCE_TRIGGER                                            5                                                             // 5 (0x5)
#define NISCOPE_VAL_READY_FOR_ADVANCE_EVENT                                    6                                                             // 6 (0x6)
#define NISCOPE_VAL_READY_FOR_START_EVENT                                      7                                                             // 7 (0x7)
#define NISCOPE_VAL_READY_FOR_REF_EVENT                                        10                                                            // 10 (0xa)
#define NISCOPE_VAL_5V_OUT                                                     13                                                            // 13 (0xd)
#define NISCOPE_VAL_REF_CLOCK                                                  100                                                           // 100 (0x64)
#define NISCOPE_VAL_SAMPLE_CLOCK                                               101                                                           // 101 (0x65)

// Values used in
//     NISCOPE_ATTR_TRIGGER_WINDOW_MODE, niScope_ConfigureTriggerWindow
#define NISCOPE_VAL_ENTERING_WINDOW                                            0                                                             // 0 (0x0)
#define NISCOPE_VAL_LEAVING_WINDOW                                             1                                                             // 1 (0x1)
#define NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW                                 2                                                             // 2 (0x2)

// Max Time
#define NISCOPE_VAL_MAX_TIME_INFINITE                                          0xFFFFFFFFUL                                                  // 4294967295 (0xffffffff)
#define NISCOPE_VAL_MAX_TIME_IMMEDIATE                                         0                                                             // 0 (0x0)
#define NISCOPE_VAL_MAX_TIME_NONE                                              0                                                             // 0 (0x0)

// Values used in
//     niScope_AcquisitionStatus
#define NISCOPE_VAL_ACQ_COMPLETE                                               IVISCOPE_VAL_ACQ_COMPLETE                                     // 1 (0x1)
#define NISCOPE_VAL_ACQ_IN_PROGRESS                                            IVISCOPE_VAL_ACQ_IN_PROGRESS                                  // 0 (0x0)
#define NISCOPE_VAL_ACQ_STATUS_UNKNOWN                                         IVISCOPE_VAL_ACQ_STATUS_UNKNOWN                               // -1 (-0x1)

// Values used in
//     NISCOPE_ATTR_MEAS_FILTER_TYPE
#define NISCOPE_VAL_MEAS_LOWPASS                                               0                                                             // 0 (0x0)
#define NISCOPE_VAL_MEAS_HIGHPASS                                              1                                                             // 1 (0x1)
#define NISCOPE_VAL_MEAS_BANDPASS                                              2                                                             // 2 (0x2)
#define NISCOPE_VAL_MEAS_BANDSTOP                                              3                                                             // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD
#define NISCOPE_VAL_MEAS_LOW_HIGH                                              0                                                             // 0 (0x0)
#define NISCOPE_VAL_MEAS_MIN_MAX                                               1                                                             // 1 (0x1)
#define NISCOPE_VAL_MEAS_BASE_TOP                                              2                                                             // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS
#define NISCOPE_VAL_MEAS_VOLTAGE                                               0                                                             // 0 (0x0)
#define NISCOPE_VAL_MEAS_PERCENTAGE                                            1                                                             // 1 (0x1)

// Values used in
//     niScope_FetchMeasurement, niScope_FetchMeasurementStats, niScope_ReadMeasurement
#define NISCOPE_VAL_NO_MEASUREMENT                                             4000                                                          // 4000 (0xfa0)
#define NISCOPE_VAL_RISE_TIME                                                  IVISCOPE_VAL_RISE_TIME                                        // 0 (0x0)
#define NISCOPE_VAL_FALL_TIME                                                  IVISCOPE_VAL_FALL_TIME                                        // 1 (0x1)
#define NISCOPE_VAL_FREQUENCY                                                  IVISCOPE_VAL_FREQUENCY                                        // 2 (0x2)
#define NISCOPE_VAL_PERIOD                                                     IVISCOPE_VAL_PERIOD                                           // 3 (0x3)
#define NISCOPE_VAL_VOLTAGE_RMS                                                IVISCOPE_VAL_VOLTAGE_RMS                                      // 4 (0x4)
#define NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK                                       IVISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK                             // 5 (0x5)
#define NISCOPE_VAL_VOLTAGE_MAX                                                IVISCOPE_VAL_VOLTAGE_MAX                                      // 6 (0x6)
#define NISCOPE_VAL_VOLTAGE_MIN                                                IVISCOPE_VAL_VOLTAGE_MIN                                      // 7 (0x7)
#define NISCOPE_VAL_VOLTAGE_HIGH                                               IVISCOPE_VAL_VOLTAGE_HIGH                                     // 8 (0x8)
#define NISCOPE_VAL_VOLTAGE_LOW                                                IVISCOPE_VAL_VOLTAGE_LOW                                      // 9 (0x9)
#define NISCOPE_VAL_VOLTAGE_AVERAGE                                            IVISCOPE_VAL_VOLTAGE_AVERAGE                                  // 10 (0xa)
#define NISCOPE_VAL_WIDTH_NEG                                                  IVISCOPE_VAL_WIDTH_NEG                                        // 11 (0xb)
#define NISCOPE_VAL_WIDTH_POS                                                  IVISCOPE_VAL_WIDTH_POS                                        // 12 (0xc)
#define NISCOPE_VAL_DUTY_CYCLE_NEG                                             IVISCOPE_VAL_DUTY_CYCLE_NEG                                   // 13 (0xd)
#define NISCOPE_VAL_DUTY_CYCLE_POS                                             IVISCOPE_VAL_DUTY_CYCLE_POS                                   // 14 (0xe)
#define NISCOPE_VAL_AMPLITUDE                                                  IVISCOPE_VAL_AMPLITUDE                                        // 15 (0xf)
#define NISCOPE_VAL_VOLTAGE_CYCLE_RMS                                          IVISCOPE_VAL_VOLTAGE_CYCLE_RMS                                // 16 (0x10)
#define NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE                                      IVISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE                            // 17 (0x11)
#define NISCOPE_VAL_OVERSHOOT                                                  IVISCOPE_VAL_OVERSHOOT                                        // 18 (0x12)
#define NISCOPE_VAL_PRESHOOT                                                   IVISCOPE_VAL_PRESHOOT                                         // 19 (0x13)
#define NISCOPE_VAL_LOW_REF_VOLTS                                              (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 0L)    // 1000 (0x3e8)
#define NISCOPE_VAL_MID_REF_VOLTS                                              (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1L)    // 1001 (0x3e9)
#define NISCOPE_VAL_HIGH_REF_VOLTS                                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2L)    // 1002 (0x3ea)
#define NISCOPE_VAL_AREA                                                       (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 3L)    // 1003 (0x3eb)
#define NISCOPE_VAL_CYCLE_AREA                                                 (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 4L)    // 1004 (0x3ec)
#define NISCOPE_VAL_INTEGRAL                                                   (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 5L)    // 1005 (0x3ed)
#define NISCOPE_VAL_VOLTAGE_BASE                                               (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 6L)    // 1006 (0x3ee)
#define NISCOPE_VAL_VOLTAGE_TOP                                                (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 7L)    // 1007 (0x3ef)
#define NISCOPE_VAL_FFT_FREQUENCY                                              (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 8L)    // 1008 (0x3f0)
#define NISCOPE_VAL_FFT_AMPLITUDE                                              (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 9L)    // 1009 (0x3f1)
#define NISCOPE_VAL_RISE_SLEW_RATE                                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 10L)   // 1010 (0x3f2)
#define NISCOPE_VAL_FALL_SLEW_RATE                                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 11L)   // 1011 (0x3f3)
#define NISCOPE_VAL_AC_ESTIMATE                                                (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 12L)   // 1012 (0x3f4)
#define NISCOPE_VAL_DC_ESTIMATE                                                (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 13L)   // 1013 (0x3f5)
#define NISCOPE_VAL_TIME_DELAY                                                 (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 14L)   // 1014 (0x3f6)
#define NISCOPE_VAL_AVERAGE_PERIOD                                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 15L)   // 1015 (0x3f7)
#define NISCOPE_VAL_AVERAGE_FREQUENCY                                          (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 16L)   // 1016 (0x3f8)
#define NISCOPE_VAL_VOLTAGE_BASE_TO_TOP                                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 17L)   // 1017 (0x3f9)
#define NISCOPE_VAL_PHASE_DELAY                                                (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 18L)   // 1018 (0x3fa)

// Voltage Histogram
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN                                     (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1000L) // 2000 (0x7d0)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV                                    (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1001L) // 2001 (0x7d1)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1002L) // 2002 (0x7d2)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN                                   (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1003L) // 2003 (0x7d3)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS                                     (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1004L) // 2004 (0x7d4)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX                                      (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1005L) // 2005 (0x7d5)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN                                      (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1006L) // 2006 (0x7d6)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV                          (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1007L) // 2007 (0x7d7)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1008L) // 2008 (0x7d8)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1009L) // 2009 (0x7d9)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE                                     (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1010L) // 2010 (0x7da)
#define NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS                                 (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 1011L) // 2011 (0x7db)

// Time Histogram
#define NISCOPE_VAL_TIME_HISTOGRAM_MEAN                                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2000L) // 3000 (0xbb8)
#define NISCOPE_VAL_TIME_HISTOGRAM_STDEV                                       (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2001L) // 3001 (0xbb9)
#define NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK                                (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2002L) // 3002 (0xbba)
#define NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN                                      (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2003L) // 3003 (0xbbb)
#define NISCOPE_VAL_TIME_HISTOGRAM_HITS                                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2004L) // 3004 (0xbbc)
#define NISCOPE_VAL_TIME_HISTOGRAM_MAX                                         (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2005L) // 3005 (0xbbd)
#define NISCOPE_VAL_TIME_HISTOGRAM_MIN                                         (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2006L) // 3006 (0xbbe)
#define NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV                             (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2007L) // 3007 (0xbbf)
#define NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV                           (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2008L) // 3008 (0xbc0)
#define NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV                           (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2009L) // 3009 (0xbc1)
#define NISCOPE_VAL_TIME_HISTOGRAM_MODE                                        (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2010L) // 3010 (0xbc2)
#define NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS                                    (IVISCOPE_VAL_MEASUREMENT_FUNCTION_SPECIFIC_EXT_BASE + 2011L) // 3011 (0xbc3)

// Values used in
//     niScope_ActualMeasWfmSize, niScope_AddWaveformProcessing, niScope_FetchArrayMeasurement
// #define NISCOPE_VAL_NO_MEASUREMENT                                          DEFINED ABOVE (4000)                                          // 4000 (0xfa0)
#define NISCOPE_VAL_LAST_ACQ_HISTOGRAM                                         4001                                                          // 4001 (0xfa1)
#define NISCOPE_VAL_FFT_PHASE_SPECTRUM                                         4002                                                          // 4002 (0xfa2)
#define NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS                                 4003                                                          // 4003 (0xfa3)
#define NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM                                4004                                                          // 4004 (0xfa4)
#define NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM                                   4005                                                          // 4005 (0xfa5)
#define NISCOPE_VAL_ARRAY_INTEGRAL                                             4006                                                          // 4006 (0xfa6)
#define NISCOPE_VAL_DERIVATIVE                                                 4007                                                          // 4007 (0xfa7)
#define NISCOPE_VAL_INVERSE                                                    4008                                                          // 4008 (0xfa8)
#define NISCOPE_VAL_HANNING_WINDOW                                             4009                                                          // 4009 (0xfa9)
#define NISCOPE_VAL_FLAT_TOP_WINDOW                                            4010                                                          // 4010 (0xfaa)
#define NISCOPE_VAL_POLYNOMIAL_INTERPOLATION                                   4011                                                          // 4011 (0xfab)
#define NISCOPE_VAL_MULTIPLY_CHANNELS                                          4012                                                          // 4012 (0xfac)
#define NISCOPE_VAL_ADD_CHANNELS                                               4013                                                          // 4013 (0xfad)
#define NISCOPE_VAL_SUBTRACT_CHANNELS                                          4014                                                          // 4014 (0xfae)
#define NISCOPE_VAL_DIVIDE_CHANNELS                                            4015                                                          // 4015 (0xfaf)
#define NISCOPE_VAL_MULTI_ACQ_AVERAGE                                          4016                                                          // 4016 (0xfb0)
#define NISCOPE_VAL_BUTTERWORTH_FILTER                                         4017                                                          // 4017 (0xfb1)
#define NISCOPE_VAL_CHEBYSHEV_FILTER                                           4018                                                          // 4018 (0xfb2)
#define NISCOPE_VAL_FFT_AMP_SPECTRUM_DB                                        4019                                                          // 4019 (0xfb3)
#define NISCOPE_VAL_HAMMING_WINDOW                                             4020                                                          // 4020 (0xfb4)
#define NISCOPE_VAL_WINDOWED_FIR_FILTER                                        4021                                                          // 4021 (0xfb5)
#define NISCOPE_VAL_BESSEL_FILTER                                              4022                                                          // 4022 (0xfb6)
#define NISCOPE_VAL_TRIANGLE_WINDOW                                            4023                                                          // 4023 (0xfb7)
#define NISCOPE_VAL_BLACKMAN_WINDOW                                            4024                                                          // 4024 (0xfb8)
#define NISCOPE_VAL_ARRAY_OFFSET                                               4025                                                          // 4025 (0xfb9)
#define NISCOPE_VAL_ARRAY_GAIN                                                 4026                                                          // 4026 (0xfba)

// Values used in
//     NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE
#define NISCOPE_VAL_REAL                                                       0                                                             // 0 (0x0)
#define NISCOPE_VAL_COMPLEX                                                    1                                                             // 1 (0x1)

// Values used in
//     NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION
#define NISCOPE_VAL_SINGLE_ENDED                                               0                                                             // 0 (0x0)
#define NISCOPE_VAL_UNBALANCED_DIFFERENTIAL                                    1                                                             // 1 (0x1)
#define NISCOPE_VAL_DIFFERENTIAL                                               2                                                             // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE
#define NISCOPE_VAL_48_TAP_STANDARD                                            0                                                             // 0 (0x0)
#define NISCOPE_VAL_48_TAP_HANNING                                             1                                                             // 1 (0x1)
#define NISCOPE_VAL_16_TAP_HANNING                                             2                                                             // 2 (0x2)
#define NISCOPE_VAL_8_TAP_HANNING                                              3                                                             // 3 (0x3)

// Values used in
//     NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING
#define NISCOPE_VAL_ERROR_REPORTING_ERROR                                      0                                                             // 0 (0x0)
#define NISCOPE_VAL_ERROR_REPORTING_WARNING                                    1                                                             // 1 (0x1)
#define NISCOPE_VAL_ERROR_REPORTING_DISABLED                                   2                                                             // 2 (0x2)

// Values used in
//     NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION
#define NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT                                   0                                                             // 0 (0x0)
#define NISCOPE_VAL_DDC_OUTPUT                                                 1                                                             // 1 (0x1)

// Values used in
//     NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE, NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE,
//     NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE
#define NISCOPE_VAL_ADDR_PHYSICAL                                              0                                                             // 0 (0x0)
#define NISCOPE_VAL_ADDR_VIRTUAL                                               1                                                             // 1 (0x1)

// Values used in
//     NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON
#define NISCOPE_VAL_NOTIFY_NEVER                                               0                                                             // 0 (0x0)
#define NISCOPE_VAL_NOTIFY_DONE                                                1                                                             // 1 (0x1)

// P2P Stream Relative To
#define NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER                           0                                                             // 0 (0x0)
#define NISCOPE_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER                       1                                                             // 1 (0x1)
#define NISCOPE_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER                            2                                                             // 2 (0x2)


/****************************************************************************
 *-------------------------------- Constants -------------------------------*
 ****************************************************************************/
#define NISCOPE_VAL_INPUT                                                      0                                                             // 0 (0x0)
#define NISCOPE_VAL_OUTPUT                                                     1                                                             // 1 (0x1)
#define NISCOPE_VAL_NONE                                                       0                                                             // 0 (0x0)
#define NISCOPE_VAL_TRUE                                                       VI_TRUE                                                       // 1 (0x1)
#define NISCOPE_VAL_FALSE                                                      VI_FALSE                                                      // 0 (0x0)
#define NISCOPE_VAL_SELF_CALIBRATION                                           0                                                             // 0 (0x0)
#define NISCOPE_VAL_EXTERNAL_CALIBRATION                                       1                                                             // 1 (0x1)
#define NISCOPE_VAL_RESTORE_FACTORY_CALIBRATION                                2                                                             // 2 (0x2)
#define NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION                           NISCOPE_VAL_RESTORE_FACTORY_CALIBRATION                       // 2 (0x2)
#define NISCOPE_VAL_ALL_MEASUREMENTS                                           10000                                                         // 10000 (0x2710)


/****************************************************************************
 *----------------------------- Type Definitions ---------------------------*
 ****************************************************************************/
#pragma pack(push,8)
struct niScope_wfmInfo
{
    ViReal64 absoluteInitialX;
    ViReal64 relativeInitialX;
    ViReal64 xIncrement;
    ViInt32 actualSamples;
    ViReal64 offset;
    ViReal64 gain;
    ViReal64 reserved1;
    ViReal64 reserved2;
};

struct niScope_coefficientInfo
{
    ViReal64 offset;
    ViReal64 gain;
    ViReal64 reserved1;
    ViReal64 reserved2;
};

#if !defined(_NIComplexNumber)
#define _NIComplexNumber
typedef struct NIComplexNumber_struct
{
    ViReal64 real;
    ViReal64 imaginary;
} NIComplexNumber;
#endif // !defined(_NIComplexNumber)

#if !defined(_NIComplexI16)
#define _NIComplexI16
typedef struct NIComplexI16_struct
{
    ViInt16 real;
    ViInt16 imaginary;
} NIComplexI16;
#endif // !defined(_NIComplexI16)

#pragma pack(pop)


/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/
// -- Init And Close Functions --
ViStatus _VI_FUNC niScope_init(
   ViRsrc resourceName,
   ViBoolean idQuery,
   ViBoolean resetDevice,
   ViSession* vi);

ViStatus _VI_FUNC niScope_InitWithOptions(
   ViRsrc resourceName,
   ViBoolean idQuery,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession* vi);

ViStatus _VI_FUNC niScope_close(
   ViSession vi);

// -- Autosetup Functions --
ViStatus _VI_FUNC niScope_AutoSetup(
   ViSession vi);

// -- Vertical Subsystem Configuration --
ViStatus _VI_FUNC niScope_ConfigureVertical(
   ViSession vi,
   ViConstString channelList,
   ViReal64 range,
   ViReal64 offset,
   ViInt32 coupling,
   ViReal64 probeAttenuation,
   ViBoolean enabled);

ViStatus _VI_FUNC niScope_ConfigureChanCharacteristics(
   ViSession vi,
   ViConstString channelList,
   ViReal64 inputImpedance,
   ViReal64 maxInputFrequency);

// -- Horizontal Subsystem Configuration --
ViStatus _VI_FUNC niScope_ConfigureHorizontalTiming(
   ViSession vi,
   ViReal64 minSampleRate,
   ViInt32 minNumPts,
   ViReal64 refPosition,
   ViInt32 numRecords,
   ViBoolean enforceRealtime);

// -- Synchronization Configuration --
ViStatus _VI_FUNC niScope_ConfigureClock(
   ViSession vi,
   ViConstString inputClockSource,
   ViConstString outputClockSource,
   ViConstString clockSyncPulseSource,
   ViBoolean masterEnabled);

ViStatus _VI_FUNC niScope_ExportSignal(
   ViSession vi,
   ViInt32 signal,
   ViConstString signalIdentifier,
   ViConstString outputTerminal);

ViStatus _VI_FUNC niScope_AdjustSampleClockRelativeDelay(
   ViSession vi,
   ViReal64 delay);

// -- Triggering Subsystem Configuration --
ViStatus _VI_FUNC niScope_ConfigureTriggerEdge(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViInt32 slope,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerGlitch(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViReal64 width,
   ViInt32 polarity,
   ViInt32 glitchCondition,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerHysteresis(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViReal64 hysteresis,
   ViInt32 slope,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerWindow(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 lowLevel,
   ViReal64 highLevel,
   ViInt32 windowMode,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerSoftware(
   ViSession vi,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_SendSoftwareTriggerEdge(
   ViSession vi,
   ViInt32 whichTrigger);

ViStatus _VI_FUNC niScope_ConfigureTriggerImmediate(
   ViSession vi);

ViStatus _VI_FUNC niScope_ConfigureTriggerRunt(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 lowThreshold,
   ViReal64 highThreshold,
   ViInt32 polarity,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerDigital(
   ViSession vi,
   ViConstString triggerSource,
   ViInt32 slope,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerVideo(
   ViSession vi,
   ViConstString triggerSource,
   ViBoolean enableDcRestore,
   ViInt32 signalFormat,
   ViInt32 event,
   ViInt32 lineNumber,
   ViInt32 polarity,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

ViStatus _VI_FUNC niScope_ConfigureTriggerWidth(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViReal64 lowThreshold,
   ViReal64 highThreshold,
   ViInt32 polarity,
   ViInt32 condition,
   ViInt32 triggerCoupling,
   ViReal64 holdoff,
   ViReal64 delay);

// -- Onboard Signal Processing Subsystem Configuration --
ViStatus _VI_FUNC niScope_ConfigureEqualizationFilterCoefficients(
   ViSession vi,
   ViConstString channelList,
   ViInt32 numberOfCoefficients,
   ViReal64 coefficients[]);

ViStatus _VI_FUNC niScope_GetEqualizationFilterCoefficients(
   ViSession vi,
   ViConstString channel,
   ViInt32 numberOfCoefficients,
   ViReal64 coefficients[]);

ViStatus _VI_FUNC niScope_GetFrequencyResponse(
   ViSession vi,
   ViConstString channel,
   ViInt32 bufferSize,
   ViReal64 frequencies[],
   ViReal64 amplitudes[],
   ViReal64 phases[],
   ViInt32* numberOfFrequencies);

// -- Waveform Acquisition Subsystem --
ViStatus _VI_FUNC niScope_ConfigureAcquisition(
   ViSession vi,
   ViInt32 acquisitionType);

ViStatus _VI_FUNC niScope_InitiateAcquisition(
   ViSession vi);

ViStatus _VI_FUNC niScope_Abort(
   ViSession vi);

ViStatus _VI_FUNC niScope_Commit(
   ViSession vi);

ViStatus _VI_FUNC niScope_Read(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViReal64 waveform[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_Fetch(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViReal64 waveform[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_FetchBinary8(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViInt8 waveform[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_FetchBinary16(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViInt16 waveform[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_FetchBinary32(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViInt32 waveform[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_FetchComplex(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   NIComplexNumber wfm[],
   struct niScope_wfmInfo wfmInfo[]);

ViStatus _VI_FUNC niScope_FetchComplexBinary16(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   NIComplexI16 wfm[],
   struct niScope_wfmInfo wfmInfo[]);

// -- Status --
ViStatus _VI_FUNC niScope_AcquisitionStatus(
   ViSession vi,
   ViInt32* acquisitionStatus);

// -- Actual Values --
ViStatus _VI_FUNC niScope_ActualNumWfms(
   ViSession vi,
   ViConstString channelList,
   ViInt32* numWfms);

ViStatus _VI_FUNC niScope_ActualMeasWfmSize(
   ViSession vi,
   ViInt32 arrayMeasFunction,
   ViInt32* measWaveformSize);

ViStatus _VI_FUNC niScope_ActualRecordLength(
   ViSession vi,
   ViInt32* recordLength);

ViStatus _VI_FUNC niScope_SampleRate(
   ViSession vi,
   ViReal64* sampleRate);

ViStatus _VI_FUNC niScope_SampleMode(
   ViSession vi,
   ViInt32* sampleMode);

// -- Waveform Measurement Functions --
ViStatus _VI_FUNC niScope_AddWaveformProcessing(
   ViSession vi,
   ViConstString channelList,
   ViInt32 measFunction);

ViStatus _VI_FUNC niScope_ClearWaveformProcessing(
   ViSession vi,
   ViConstString channelList);

ViStatus _VI_FUNC niScope_ClearWaveformMeasurementStats(
   ViSession vi,
   ViConstString channelList,
   ViInt32 clearableMeasurementFunction);

ViStatus _VI_FUNC niScope_ReadMeasurement(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 scalarMeasFunction,
   ViReal64 result[]);

ViStatus _VI_FUNC niScope_FetchMeasurement(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 scalarMeasFunction,
   ViReal64 result[]);

ViStatus _VI_FUNC niScope_FetchMeasurementStats(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 scalarMeasFunction,
   ViReal64 result[],
   ViReal64 mean[],
   ViReal64 stdev[],
   ViReal64 min[],
   ViReal64 max[],
   ViInt32 numInStats[]);

ViStatus _VI_FUNC niScope_FetchArrayMeasurement(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 arrayMeasFunction,
   ViInt32 measWfmSize,
   ViReal64 measWfm[],
   struct niScope_wfmInfo wfmInfo[]);

// -- Utility Functions --
ViStatus _VI_FUNC niScope_reset(
   ViSession vi);

ViStatus _VI_FUNC niScope_self_test(
   ViSession vi,
   ViInt16* selfTestResult,
   ViChar selfTestMessage[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niScope_Disable(
   ViSession vi);

ViStatus _VI_FUNC niScope_ResetDevice(
   ViSession vi);

ViStatus _VI_FUNC niScope_CalSelfCalibrate(
   ViSession vi,
   ViConstString channelList,
   ViInt32 option);

ViStatus _VI_FUNC niScope_revision_query(
   ViSession vi,
   ViChar driverRevision[IVI_MAX_MESSAGE_BUF_SIZE],
   ViChar firmwareRevision[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niScope_ProbeCompensationSignalStart(
   ViSession vi);

ViStatus _VI_FUNC niScope_ProbeCompensationSignalStop(
   ViSession vi);

ViStatus _VI_FUNC niScope_CableSenseSignalStart(
   ViSession vi);

ViStatus _VI_FUNC niScope_CableSenseSignalStop(
   ViSession vi);

ViStatus _VI_FUNC niScope_IsDeviceReady(
   ViRsrc resourceName,
   ViConstString channelList,
   ViBoolean* deviceReady);

ViStatus _VI_FUNC niScope_GetChannelName(
   ViSession vi,
   ViInt32 index,
   ViInt32 bufferSize,
   ViChar channelString[]);

ViStatus _VI_FUNC niScope_GetChannelNameFromString(
   ViSession vi,
   ViConstString index,
   ViInt32 bufferSize,
   ViChar name[]);

// -- Error Functions --
ViStatus _VI_FUNC niScope_errorHandler(
   ViSession vi,
   ViStatus errorCode,
   const ViChar errorSource[MAX_FUNCTION_NAME_SIZE],
   ViChar errorDescription[MAX_ERROR_DESCRIPTION]);

ViStatus _VI_FUNC niScope_GetError(
   ViSession vi,
   ViStatus* errorCode,
   ViInt32 bufferSize,
   ViChar description[]);

ViStatus _VI_FUNC niScope_GetErrorMessage(
   ViSession vi,
   ViStatus errorCode,
   ViInt32 bufferSize,
   ViChar errorMessage[]);

// -- Session Locking Functions --
ViStatus _VI_FUNC niScope_LockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

ViStatus _VI_FUNC niScope_UnlockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

// -- Typesafe Get, Set, And Check Attribute Functions --
ViStatus _VI_FUNC niScope_GetAttributeViInt32(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt32* value);

ViStatus _VI_FUNC niScope_SetAttributeViInt32(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt32 value);

ViStatus _VI_FUNC niScope_CheckAttributeViInt32(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt32 value);

ViStatus _VI_FUNC niScope_GetAttributeViInt64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt64* value);

ViStatus _VI_FUNC niScope_SetAttributeViInt64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt64 value);

ViStatus _VI_FUNC niScope_CheckAttributeViInt64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt64 value);

ViStatus _VI_FUNC niScope_GetAttributeViReal64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViReal64* value);

ViStatus _VI_FUNC niScope_SetAttributeViReal64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViReal64 value);

ViStatus _VI_FUNC niScope_CheckAttributeViReal64(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViReal64 value);

ViStatus _VI_FUNC niScope_GetAttributeViString(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViInt32 bufSize,
   ViChar value[]);

ViStatus _VI_FUNC niScope_SetAttributeViString(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViConstString value);

ViStatus _VI_FUNC niScope_CheckAttributeViString(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViConstString value);

ViStatus _VI_FUNC niScope_GetAttributeViSession(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViSession* value);

ViStatus _VI_FUNC niScope_SetAttributeViSession(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViSession value);

ViStatus _VI_FUNC niScope_CheckAttributeViSession(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViSession value);

ViStatus _VI_FUNC niScope_GetAttributeViBoolean(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViBoolean* value);

ViStatus _VI_FUNC niScope_SetAttributeViBoolean(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViBoolean value);

ViStatus _VI_FUNC niScope_CheckAttributeViBoolean(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId,
   ViBoolean value);

ViStatus _VI_FUNC niScope_ResetAttribute(
   ViSession vi,
   ViConstString channelList,
   ViAttr attributeId);

ViStatus _VI_FUNC niScope_ResetAllAttributes(
   ViSession vi);

// -- Import And Export Attribute Configuration Functions --
ViStatus _VI_FUNC niScope_ImportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 sizeInBytes,
   ViInt8 configuration[]);

ViStatus _VI_FUNC niScope_ExportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 sizeInBytes,
   ViInt8 configuration[]);

ViStatus _VI_FUNC niScope_ImportAttributeConfigurationFile(
   ViSession vi,
   ViConstString filePath);

ViStatus _VI_FUNC niScope_ExportAttributeConfigurationFile(
   ViSession vi,
   ViConstString filePath);

// -- Scaling And Normalization Functions --
ViStatus _VI_FUNC niScope_GetScalingCoefficients(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   struct niScope_coefficientInfo coefficientInfo[],
   ViInt32* numberOfCoefficientSets);

ViStatus _VI_FUNC niScope_GetNormalizationCoefficients(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   struct niScope_coefficientInfo coefficientInfo[],
   ViInt32* numberOfCoefficientSets);

// -- Peer-To-Peer Streaming Functions --
ViStatus _VI_FUNC niScope_GetStreamEndpointHandle(
   ViSession vi,
   ViConstString streamName,
   ViUInt32* writerHandle);



/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/
#define NISCOPE_WARN_INVALID_WFM_ELEMENT                                       IVISCOPE_WARN_INVALID_WFM_ELEMENT                             // 1073356801 (0x3ffa2001)
#define NISCOPE_WARN_HEATER_CIRCUIT_TEMPERATURE                                (IVI_SPECIFIC_WARN_BASE + 1L)                                 // 1073364993 (0x3ffa4001)
#define NISCOPE_WARN_INVALID_DATA                                              (IVI_SPECIFIC_WARN_BASE + 2L)                                 // 1073364994 (0x3ffa4002)
#define NISCOPE_WARN_CHANNEL_OVERLOAD                                          (IVI_SPECIFIC_WARN_BASE + 3L)                                 // 1073364995 (0x3ffa4003)
#define NISCOPE_WARN_AUTOSETUP_NO_SIGNAL                                       (IVI_SPECIFIC_WARN_BASE + 4L)                                 // 1073364996 (0x3ffa4004)
#define NISCOPE_WARN_PLL_UNLOCKED                                              (IVI_SPECIFIC_WARN_BASE + 5L)                                 // 1073364997 (0x3ffa4005)
#define NISCOPE_WARN_PLL_UNLOCKED_AND_ADC_OVERLOAD                             (IVI_SPECIFIC_WARN_BASE + 6L)                                 // 1073364998 (0x3ffa4006)
#define NISCOPE_WARN_TIMESTAMP_ROLLOVER                                        (IVI_SPECIFIC_WARN_BASE + 7L)                                 // 1073364999 (0x3ffa4007)
#define NISCOPE_WARN_ADC_OVERLOAD                                              (IVI_SPECIFIC_WARN_BASE + 8L)                                 // 1073365000 (0x3ffa4008)
#define NISCOPE_WARN_P2P_OVERFLOW                                              (IVI_SPECIFIC_WARN_BASE + 9L)                                 // 1073365001 (0x3ffa4009)
#define NISCOPE_ERROR_CHANNEL_NOT_ENABLED                                      IVISCOPE_ERROR_CHANNEL_NOT_ENABLED                            // 3220840449 (0xbffa2001)
#define NISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT                            IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT                  // 3220840450 (0xbffa2002)
#define NISCOPE_ERROR_MAX_TIME_EXCEEDED                                        IVISCOPE_ERROR_MAX_TIME_EXCEEDED                              // 3220840451 (0xbffa2003)
#define NISCOPE_ERROR_SOFTWARE_FAILURE                                         (IVI_SPECIFIC_ERROR_BASE + 1L)                                // 3220848641 (0xbffa4001)
#define NISCOPE_ERROR_HARDWARE_FAILURE                                         (IVI_SPECIFIC_ERROR_BASE + 2L)                                // 3220848642 (0xbffa4002)
#define NISCOPE_ERROR_INSUFFICIENT_MEMORY                                      (IVI_SPECIFIC_ERROR_BASE + 3L)                                // 3220848643 (0xbffa4003)
#define NISCOPE_ERROR_INVALID_DATA                                             (IVI_SPECIFIC_ERROR_BASE + 4L)                                // 3220848644 (0xbffa4004)
#define NISCOPE_ERROR_GAIN_CAL_FAILURE                                         (IVI_SPECIFIC_ERROR_BASE + 5L)                                // 3220848645 (0xbffa4005)
#define NISCOPE_ERROR_SINE_CAL_FAILURE                                         (IVI_SPECIFIC_ERROR_BASE + 6L)                                // 3220848646 (0xbffa4006)
#define NISCOPE_ERROR_LIN_CAL_FAILURE                                          (IVI_SPECIFIC_ERROR_BASE + 7L)                                // 3220848647 (0xbffa4007)
#define NISCOPE_ERROR_ADC_CAL_FAILURE                                          (IVI_SPECIFIC_ERROR_BASE + 8L)                                // 3220848648 (0xbffa4008)
#define NISCOPE_ERROR_ACQ_IN_PROGRESS                                          (IVI_SPECIFIC_ERROR_BASE + 9L)                                // 3220848649 (0xbffa4009)
#define NISCOPE_ERROR_DATA_NOT_AVAILABLE                                       (IVI_SPECIFIC_ERROR_BASE + 10L)                               // 3220848650 (0xbffa400a)
#define NISCOPE_ERROR_HEATER_CIRCUIT_CAL_FAILURE                               (IVI_SPECIFIC_ERROR_BASE + 11L)                               // 3220848651 (0xbffa400b)
#define NISCOPE_ERROR_FLEXRES_CONFIG_CORRUPT                                   (IVI_SPECIFIC_ERROR_BASE + 12L)                               // 3220848652 (0xbffa400c)
#define NISCOPE_ERROR_GAIN_OFFSET_CAL_FAILURE                                  (IVI_SPECIFIC_ERROR_BASE + 13L)                               // 3220848653 (0xbffa400d)
#define NISCOPE_ERROR_CREATE_THREAD                                            (IVI_SPECIFIC_ERROR_BASE + 14L)                               // 3220848654 (0xbffa400e)
#define NISCOPE_ERROR_WRONG_PASSWORD                                           (IVI_SPECIFIC_ERROR_BASE + 15L)                               // 3220848655 (0xbffa400f)
#define NISCOPE_ERROR_INVALID_GAIN                                             (IVI_SPECIFIC_ERROR_BASE + 16L)                               // 3220848656 (0xbffa4010)
#define NISCOPE_ERROR_INVALID_CAL_SESSION                                      (IVI_SPECIFIC_ERROR_BASE + 19L)                               // 3220848659 (0xbffa4013)
#define NISCOPE_ERROR_BAD_MEASUREMENT                                          (IVI_SPECIFIC_ERROR_BASE + 20L)                               // 3220848660 (0xbffa4014)
#define NISCOPE_ERROR_BUFFER_NOT_ACQUIRED                                      (IVI_SPECIFIC_ERROR_BASE + 21L)                               // 3220848661 (0xbffa4015)
#define NISCOPE_ERROR_TRIGGER_HAS_NOT_OCCURRED                                 (IVI_SPECIFIC_ERROR_BASE + 22L)                               // 3220848662 (0xbffa4016)
#define NISCOPE_ERROR_ILLEGAL_RELATIVE_TO                                      (IVI_SPECIFIC_ERROR_BASE + 23L)                               // 3220848663 (0xbffa4017)
#define NISCOPE_ERROR_DATA_OVERWRITTEN                                         (IVI_SPECIFIC_ERROR_BASE + 24L)                               // 3220848664 (0xbffa4018)
#define NISCOPE_ERROR_INVALID_TIMESTAMP_EVENT_TAG                              (IVI_SPECIFIC_ERROR_BASE + 26L)                               // 3220848666 (0xbffa401a)
#define NISCOPE_ERROR_TIMEOUT_TRANSFERRING_TIMESTAMPS                          (IVI_SPECIFIC_ERROR_BASE + 27L)                               // 3220848667 (0xbffa401b)
#define NISCOPE_ERROR_TIMEOUT_CHECKING_STATUS                                  (IVI_SPECIFIC_ERROR_BASE + 28L)                               // 3220848668 (0xbffa401c)
#define NISCOPE_ERROR_TIMEOUT_TRANSFERRING_DATA                                (IVI_SPECIFIC_ERROR_BASE + 29L)                               // 3220848669 (0xbffa401d)
#define NISCOPE_ERROR_PLL_FAILURE                                              (IVI_SPECIFIC_ERROR_BASE + 30L)                               // 3220848670 (0xbffa401e)
#define NISCOPE_ERROR_PAR_TO_SER_CONV_FAILURE                                  (IVI_SPECIFIC_ERROR_BASE + 31L)                               // 3220848671 (0xbffa401f)
#define NISCOPE_ERROR_DMA_CONFIG_ERROR                                         (IVI_SPECIFIC_ERROR_BASE + 32L)                               // 3220848672 (0xbffa4020)
#define NISCOPE_ERROR_ILLEGAL_USER_OFFSET                                      (IVI_SPECIFIC_ERROR_BASE + 33L)                               // 3220848673 (0xbffa4021)
#define NISCOPE_ERROR_NOT_A_SCOPE                                              (IVI_SPECIFIC_ERROR_BASE + 34L)                               // 3220848674 (0xbffa4022)
#define NISCOPE_ERROR_TIMEOUT_CLEARING_TIO                                     (IVI_SPECIFIC_ERROR_BASE + 35L)                               // 3220848675 (0xbffa4023)
#define NISCOPE_ERROR_RIS_DID_NOT_COMPLETE                                     (IVI_SPECIFIC_ERROR_BASE + 36L)                               // 3220848676 (0xbffa4024)
#define NISCOPE_ERROR_INVALID_RIS_METHOD                                       (IVI_SPECIFIC_ERROR_BASE + 37L)                               // 3220848677 (0xbffa4025)
#define NISCOPE_ERROR_INVALID_RIS_NUM_AVERAGES                                 (IVI_SPECIFIC_ERROR_BASE + 38L)                               // 3220848678 (0xbffa4026)
#define NISCOPE_ERROR_ILLEGAL_DATATYPE                                         (IVI_SPECIFIC_ERROR_BASE + 39L)                               // 3220848679 (0xbffa4027)
#define NISCOPE_ERROR_ATTRIBUTES_DIFFER_BY_CHANNEL                             (IVI_SPECIFIC_ERROR_BASE + 40L)                               // 3220848680 (0xbffa4028)
#define NISCOPE_ERROR_TRIGGER_DELAY_INVALID_WITH_RIS                           (IVI_SPECIFIC_ERROR_BASE + 41L)                               // 3220848681 (0xbffa4029)
#define NISCOPE_ERROR_INITIATE_NOT_CALLED                                      (IVI_SPECIFIC_ERROR_BASE + 42L)                               // 3220848682 (0xbffa402a)
#define NISCOPE_ERROR_INVALID_FUNCTION_USE                                     (IVI_SPECIFIC_ERROR_BASE + 43L)                               // 3220848683 (0xbffa402b)
#define NISCOPE_ERROR_HOLDOFF_DELAY_NONZERO                                    (IVI_SPECIFIC_ERROR_BASE + 44L)                               // 3220848684 (0xbffa402c)
#define NISCOPE_ERROR_CHANNEL_NAME_TOO_LONG                                    (IVI_SPECIFIC_ERROR_BASE + 45L)                               // 3220848685 (0xbffa402d)
#define NISCOPE_ERROR_DIGITIZER_ALREADY_IN_USE                                 (IVI_SPECIFIC_ERROR_BASE + 46L)                               // 3220848686 (0xbffa402e)
#define NISCOPE_ERROR_SIM_MODEL_NOT_SUPPORTED                                  (IVI_SPECIFIC_ERROR_BASE + 47L)                               // 3220848687 (0xbffa402f)
#define NISCOPE_ERROR_SPECIFICDLL_LOAD_FAILURE                                 (IVI_SPECIFIC_ERROR_BASE + 48L)                               // 3220848688 (0xbffa4030)
#define NISCOPE_ERROR_SPECIFICDLL_GET_ADDRESS_FAILURE                          (IVI_SPECIFIC_ERROR_BASE + 49L)                               // 3220848689 (0xbffa4031)
#define NISCOPE_ERROR_TRIGGER_TYPE_INVALID                                     (IVI_SPECIFIC_ERROR_BASE + 50L)                               // 3220848690 (0xbffa4032)
#define NISCOPE_ERROR_INVALID_FETCH_PARAMETERS                                 (IVI_SPECIFIC_ERROR_BASE + 51L)                               // 3220848691 (0xbffa4033)
#define NISCOPE_ERROR_EXT_CAL_NOT_COMPLETE                                     (IVI_SPECIFIC_ERROR_BASE + 52L)                               // 3220848692 (0xbffa4034)
#define NISCOPE_ERROR_EXT_CAL_CONSTS_INVALID                                   (IVI_SPECIFIC_ERROR_BASE + 53L)                               // 3220848693 (0xbffa4035)
#define NISCOPE_ERROR_INVALID_NUM_WAVEFORMS                                    (IVI_SPECIFIC_ERROR_BASE + 54L)                               // 3220848694 (0xbffa4036)
#define NISCOPE_ERROR_DIGITIZER_NOT_SUPPORTED_WITH_ACCESSORY                   (IVI_SPECIFIC_ERROR_BASE + 55L)                               // 3220848695 (0xbffa4037)
#define NISCOPE_ERROR_DIGITAL_TRIGGER_NOT_SUPPORTED_WITH_RIS                   (IVI_SPECIFIC_ERROR_BASE + 56L)                               // 3220848696 (0xbffa4038)
#define NISCOPE_ERROR_SELF_CAL_NOT_COMPLETE                                    (IVI_SPECIFIC_ERROR_BASE + 57L)                               // 3220848697 (0xbffa4039)
#define NISCOPE_ERROR_PATTERN_NOISE_SAMPLE_WORDS                               (IVI_SPECIFIC_ERROR_BASE + 58L)                               // 3220848698 (0xbffa403a)
#define NISCOPE_ERROR_PATTERN_NOISE_INPUT_EXPECTATION                          (IVI_SPECIFIC_ERROR_BASE + 59L)                               // 3220848699 (0xbffa403b)
#define NISCOPE_ERROR_INVALID_SESSION                                          0xBFFA1190                                                    // 3220836752 (0xbffa1190)
#define NISCOPE_ERROR_1MOHM_PATH_BANDWIDTH_LIMITED                             (IVI_SPECIFIC_ERROR_BASE + 60L)                               // 3220848700 (0xbffa403c)
#define NISCOPE_ERROR_EXT_CAL_STEP_OUT_OF_ORDER                                (IVI_SPECIFIC_ERROR_BASE + 61L)                               // 3220848701 (0xbffa403d)
#define NISCOPE_ERROR_MULTIPLES_2_ALLOWED_SAMPLE_CLK_TIMEBASE_DIV              (IVI_SPECIFIC_ERROR_BASE + 62L)                               // 3220848702 (0xbffa403e)
#define NISCOPE_ERROR_CAL_INPUT_VOLTAGE_DETECTED                               (IVI_SPECIFIC_ERROR_BASE + 63L)                               // 3220848703 (0xbffa403f)
#define NISCOPE_ERROR_EXT_CAL_ATTENUATOR_FAILED                                (IVI_SPECIFIC_ERROR_BASE + 64L)                               // 3220848704 (0xbffa4040)
#define NISCOPE_ERROR_TDC_CAL_TIME_OUT                                         (IVI_SPECIFIC_ERROR_BASE + 65L)                               // 3220848705 (0xbffa4041)
#define NISCOPE_ERROR_TDC_CAL_FAILURE                                          (IVI_SPECIFIC_ERROR_BASE + 66L)                               // 3220848706 (0xbffa4042)
#define NISCOPE_ERROR_TRIGGER_CAL_FAILURE                                      (IVI_SPECIFIC_ERROR_BASE + 67L)                               // 3220848707 (0xbffa4043)
#define NISCOPE_ERROR_OFFSET_DAC_CAL_FAILURE                                   (IVI_SPECIFIC_ERROR_BASE + 68L)                               // 3220848708 (0xbffa4044)
#define NISCOPE_ERROR_INVALID_FETCH_POSITION                                   (IVI_SPECIFIC_ERROR_BASE + 69L)                               // 3220848709 (0xbffa4045)
#define NISCOPE_ERROR_RIS_MODE_NOT_SUPPORTED_WITH_P2P                          (IVI_SPECIFIC_ERROR_BASE + 70L)                               // 3220848710 (0xbffa4046)


/*- niScopeObsolete.h included for backwards compatibility -*/
#include "niScopeObsolete.h"

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* __NISCOPE_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niScopeCal.h sha256=e1a85abfff5b9d27439efe81f9bd20b2687ecb4e18769d40416ef9f79a4191ab bytes=10123 -->
## FILE: imports/include/niScopeCal.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niScopeCal.h`
- sha256: `e1a85abfff5b9d27439efe81f9bd20b2687ecb4e18769d40416ef9f79a4191ab`
- bytes: 10123

````c
#ifndef ___niScopeCal_h___
#define ___niScopeCal_h___

#ifndef ___niScope_h___
#include "niScope.h"
#endif

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

// Values used in
//     niScope_CalEnd
#define NISCOPE_VAL_CAL_ACTION_STORE                                           0                                                             // 0 (0x0)
#define NISCOPE_VAL_CAL_ACTION_ABORT                                           1                                                             // 1 (0x1)
#define NISCOPE_VAL_CAL_ACTION_RESET                                           101                                                           // 101 (0x65)

// Options For Error Handling
#define NISCOPE_VAL_CAL_ABORT_ON_ERR                                           0                                                             // 0 (0x0)
#define NISCOPE_VAL_CAL_ABORT_ON_MAJOR_ERR                                     1                                                             // 1 (0x1)
#define NISCOPE_VAL_CAL_SKIP_BAD_SECTIONS                                      2                                                             // 2 (0x2)
#define NISCOPE_VAL_CAL_RESET_BAD_SECTIONS                                     3                                                             // 3 (0x3)

// Values used in
//     niScope_CalFetchCount, niScope_CalFetchDate
#define NISCOPE_VAL_CAL_SELF                                                   1                                                             // 1 (0x1)
#define NISCOPE_VAL_CAL_EXTERNAL                                               0                                                             // 0 (0x0)
#define NISCOPE_VAL_CAL_MANUFACTURE                                            2                                                             // 2 (0x2)

// Values used in
//     niScope_CalRouteInternalReference
#define NISCOPE_VAL_CAL_UNROUTE_SIGNAL                                         (ViUInt32)0xfffffff
#define NISCOPE_VAL_CAL_POSITIVE                                               (ViUInt32)0xffff
#define NISCOPE_VAL_CAL_NEGATIVE                                               0                                                             // 0 (0x0)

// Values used in
//     niScope_CalSetAccessorySource
#define NISCOPE_VAL_CAL_SOURCE_GROUND                                          0                                                             // 0 (0x0)
#define NISCOPE_VAL_CAL_SOURCE_POSITIVEFS                                      1                                                             // 1 (0x1)
#define NISCOPE_VAL_CAL_SOURCE_NEGATIVEFS                                      2                                                             // 2 (0x2)

// Reference Parameter For Routing And Storing And Fetching Int Ref
#define NISCOPE_VAL_CAL_10V_CH0                                                0                                                             // 0 (0x0)


#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

// -- Open / Close / Change Password --
// Gives calibration session handle
ViStatus _VI_FUNC niScope_CalStart(
   ViRsrc resourceName,             // e.g. "DAQ:1"
   ViConstString password,          // pointer to 4 bytes for password, 0 or "" by default
   ViSession* newSessionHandle);    // returns this session handle

// Either store constants in eeprom or abort.
ViStatus _VI_FUNC niScope_CalEnd(
   ViSession vi,                    // session handle from CalStart
   ViInt32 action);                 // see defined "action" constants above

// If the old password is correct, the new password is stored in eeprom
ViStatus _VI_FUNC niScope_CalChangePassword(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViConstString oldPassword,       // previous password is verfied (pointer to 4 bytes)
   ViConstString newPassword);      // new password is written to eeprom (pointer to 4 bytes)

// -- Fetch --
ViStatus _VI_FUNC niScope_CalFetchCount(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViInt32 whichOne,                // internal or external count: see defines
   ViInt32* calibrationCount);      // number of calibrations peformed

ViStatus _VI_FUNC niScope_CalFetchDate(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViInt32 whichOne,                // internal or external cal date, or manufacture date
   ViInt32* year,                   // year of last calibration from eeprom
   ViInt32* month,                  // month of last calibration from eeprom
   ViInt32* day);                   // day of last calibration from eeprom

// Not supported yet, but will be for temperature sensing devices
ViStatus _VI_FUNC niScope_CalFetchTemperature(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViInt32 whichOne,                // internal or external cal temperature
   ViReal64* temperature);          // temperature in degrees C

ViStatus _VI_FUNC niScope_CalFetchMiscInfo(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViChar miscInfo[5]);             // pointer to 5 bytes; returned from eeprom

// Return the last stored internal reference value.
// This value is not used during device operation.
ViStatus _VI_FUNC niScope_CalFetchInternalReference(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViInt32 whichReference,          // see defines
   ViReal64* internalRefValue);     // last stored internal reference measurement

// -- Store --
ViStatus _VI_FUNC niScope_CalStoreMiscInfo(
   ViSession vi,                    // session handle from CalStart
   ViConstString miscInfo);         // pointer to 4 characters to store in eeprom (operator id?)

// For verification, store the internal reference. This value is not
// used during device operation.
ViStatus _VI_FUNC niScope_CalStoreInternalReference(
   ViSession vi,                    // session handle from CalStart
   ViInt32 whichReference,          // see defines
   ViReal64 internalRefValue);      // last stored internal reference measurement

// -- Adjustment --
ViStatus _VI_FUNC niScope_CalAdjustRange(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 range,                  // see niscope calibration document
   ViReal64 stimulus);              // peak voltage of applied signal

ViStatus _VI_FUNC niScope_CalAdjustVCXO(
   ViSession vi,                    // session handle from CalStart
   ViReal64 stimulusFreq);          // frequency of applied signal

ViStatus _VI_FUNC niScope_CalAdjustDCM(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 stimulusFreq);          // frequency of applied signal

ViStatus _VI_FUNC niScope_CalAdjustOffset(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 range);                 // see niscope calibration document

ViStatus _VI_FUNC niScope_CalAdjustOffsetRange(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 range,                  // see niscope calibration document
   ViReal64 stimulus);              // peak voltage of applied signal

ViStatus _VI_FUNC niScope_CalAdjustCompensationAttenuator(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 range);                 // see niscope calibration document

ViStatus _VI_FUNC niScope_CalAdjustFrequencyResponse(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 range,                  // see niscope calibration document
   ViReal64 stimulusFreq,           // frequency of applied signal
   ViReal64 stimulusAmp);           // peak voltage of applied signal

// For the 5911 external calibration with a single DC external voltage source
ViStatus _VI_FUNC niScope_CalAdjustInternalReference(
   ViSession vi,                    // session handle from CalStart
   ViInt32 option,                  // use VI_NULL
   ViReal64 stimulus);              // voltage of applied signal

// For 5112 verification, this routes the internal reference out the
// front BNC connector for measurement.
ViStatus _VI_FUNC niScope_CalRouteInternalReference(
   ViSession vi,                    // session handle from CalStart
   ViInt32 option,                  // see defines
   ViInt32 whichReference);         // see constants

// For the 5900 external calibration
ViStatus _VI_FUNC niScope_CalAdjustAccessoryGainAndOffset(
   ViSession vi,                    // session handle from CalStart
   ViConstString channelName,       // e.g. "0" or "1"
   ViReal64 posFs,
   ViReal64 gnd,
   ViReal64 negFs);

ViStatus _VI_FUNC niScope_CalSetAccessorySource(
   ViSession vi,
   ViConstString channelName,
   ViInt32 calSource);

// -- Verification --
ViStatus _VI_FUNC niScope_CalMeasureRISDistribution(
   ViSession vi,                    // session handle from CalStart or niScope_init
   ViConstString channelName,       // e.g. "0" or "1"
   ViInt32 maxTime,                 // max time in ms for each acquisition
   ViReal64* minBinPercent,         // percent (0-1) of trigers in the least full bin
   ViInt32 distributionSize,        // number of bins for distribution
   ViInt32* distribution);          // array for distribution, NULL for "do not return it"


#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* ___niScopeCal_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niScopeObsolete.h sha256=a7def420b8e2afdf81624bc3ba3b7fc9ddc74fc28e2bf4ebf67ab2869c8fbbbd bytes=60748 -->
## FILE: imports/include/niScopeObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niScopeObsolete.h`
- sha256: `a7def420b8e2afdf81624bc3ba3b7fc9ddc74fc28e2bf4ebf67ab2869c8fbbbd`
- bytes: 60748

````c
/****************************************************************************
 *                                niScope                                   *
 *--------------------------------------------------------------------------*
 *   Copyright (c) National Instruments 2001-2022.  All Rights Reserved.    *
 *--------------------------------------------------------------------------*
 *                                                                          *
 * Title:    niScopeObsolete.h                                              *
 * Purpose:  niScope                                                        *
 *           instrument driver declarations.                                *
 *              These macros, constants, and functions are defined to keep  *
 *              backward compatibility with previous versions of niScope.   *
 *              Programs should no longer use these macros, constants, and  *
 *              functions. Instead, programs should use definitions from    *
 *              the current niScope.h header file.                          *
 *                                                                          *
 ****************************************************************************/

#ifndef __NISCOPE_HEADER_OBSOLETE
#define __NISCOPE_HEADER_OBSOLETE

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "ivi.h"
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS


/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------------- Obsolete Attribute Defines -----------------------*
 ****************************************************************************/
// Obsolete Inherent Instrument Attributes and functions.
// These attributes and functions have been deprecated and may not
// be supported in future versions of this driver.

// -- Obsolete Specific Attributes. --
#define NISCOPE_ATTR_SLAVE_TRIGGER_DELAY                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 46L)                         // 1150046 (0x118c5e), ViReal64
#define NISCOPE_ATTR_TRIGGER_TO_STAR_DELAY                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 47L)                         // 1150047 (0x118c5f), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_TO_RTSI_DELAY                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 48L)                         // 1150048 (0x118c60), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_TO_PFI_DELAY                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 49L)                         // 1150049 (0x118c61), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_FROM_STAR_DELAY                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 50L)                         // 1150050 (0x118c62), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_FROM_RTSI_DELAY                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 51L)                         // 1150051 (0x118c63), ViReal64,   read-only
#define NISCOPE_ATTR_TRIGGER_FROM_PFI_DELAY                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 52L)                         // 1150052 (0x118c64), ViReal64,   read-only
#define NISCOPE_ATTR_RECORD_ARM_SOURCE                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 65L)                         // 1150065 (0x118c71), ViString
#define NISCOPE_ATTR_5102_ADJUST_PRETRIGGER_SAMPLES                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 85L)                         // 1150085 (0x118c85), ViBoolean

// -- Attributes For The 5620 Digital Down Converter --
#define NISCOPE_ATTR_DDC_NCO_FREQUENCY                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1000L)                       // 1151000 (0x119018), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_NCO_PHASE                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1001L)                       // 1151001 (0x119019), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_ENABLE                                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1003L)                       // 1151003 (0x11901b), ViBoolean
#define NISCOPE_ATTR_DDC_CIC_DECIMATION                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1010L)                       // 1151010 (0x119022), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_CIC_SHIFT_GAIN                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1011L)                       // 1151011 (0x119023), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_ENABLED                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1020L)                       // 1151020 (0x11902c), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_FIR_DECIMATION                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1021L)                       // 1151021 (0x11902d), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_FIR_SYMMETRY                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1022L)                       // 1151022 (0x11902e), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_FIR_SYMMETRY_TYPE                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1023L)                       // 1151023 (0x11902f), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_FIR_NUM_TAPS                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1024L)                       // 1151024 (0x119030), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_DELAY                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1025L)                       // 1151025 (0x119031), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_FIR_INPUT_SOURCE                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1026L)                       // 1151026 (0x119032), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_DISCRIMINATOR_PHASE_MULTIPLIER                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1027L)                       // 1151027 (0x119033), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_PFIR_DECIMATION                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1030L)                       // 1151030 (0x119036), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_PFIR_SYMMETRY                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1031L)                       // 1151031 (0x119037), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_PFIR_SYMMETRY_TYPE                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1032L)                       // 1151032 (0x119038), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_PFIR_NUM_TAPS                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1033L)                       // 1151033 (0x119039), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_PFIR_REAL_OR_COMPLEX                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1034L)                       // 1151034 (0x11903a), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_UPPER_GAIN_LIMIT                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1040L)                       // 1151040 (0x119040), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_AGC_LOWER_GAIN_LIMIT                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1041L)                       // 1151041 (0x119041), ViReal64,   multi-channel
#define NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_0_EXPONENT                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1042L)                       // 1151042 (0x119042), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_0_MANTISSA                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1043L)                       // 1151043 (0x119043), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_1_EXPONENT                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1044L)                       // 1151044 (0x119044), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_1_MANTISSA                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1045L)                       // 1151045 (0x119045), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_THRESHOLD                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1046L)                       // 1151046 (0x119046), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_AGC_AVERAGE_CONTROL                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1047L)                       // 1151047 (0x119047), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_BYPASSED                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1050L)                       // 1151050 (0x11904a), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_1_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1051L)                       // 1151051 (0x11904b), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_2_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1052L)                       // 1151052 (0x11904c), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_3_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1053L)                       // 1151053 (0x11904d), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_4_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1054L)                       // 1151054 (0x11904e), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_HALFBAND_5_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1055L)                       // 1151055 (0x11904f), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_AOUT_PARALLEL_OUTPUT_SOURCE                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1070L)                       // 1151070 (0x11905e), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_BOUT_PARALLEL_OUTPUT_SOURCE                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1071L)                       // 1151071 (0x11905f), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_TEST_SINE_COSINE                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1072L)                       // 1151072 (0x119060), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_COORDINATE_CONVERTER_INPUT                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1073L)                       // 1151073 (0x119061), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_Q_INPUT_TO_COORD_CONVERTER_INPUT                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1074L)                       // 1151074 (0x119062), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_SYNCOUT_CLK_SELECT                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1080L)                       // 1151080 (0x119068), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_PHASE_ACCUM_LOAD                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1120L)                       // 1151120 (0x119090), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_CLEAR_PHASE_ACCUM                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1121L)                       // 1151121 (0x119091), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_ENABLE_OFFSET_FREQ                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1122L)                       // 1151122 (0x119092), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_NUM_OFFSET_FREQ_BITS                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1123L)                       // 1151123 (0x119093), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_CENTER_FREQUENCY                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1124L)                       // 1151124 (0x119094), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_TIMING_NCO_PHASE_OFFSET                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1125L)                       // 1151125 (0x119095), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_RESAMPLER_FILTER_MODE_SELECT                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1126L)                       // 1151126 (0x119096), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_RESAMPLER_BYPASS                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1127L)                       // 1151127 (0x119097), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_RESAMPLER_OUTPUT_PULSE_DELAY                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1128L)                       // 1151128 (0x119098), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_NCO_DIVIDE                                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1129L)                       // 1151129 (0x119099), ViInt32,    multi-channel
#define NISCOPE_ATTR_DDC_REFERENCE_DIVIDE                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1130L)                       // 1151130 (0x11909a), ViInt32,    multi-channel
#define NISCOPE_ATTR_ENABLE_DITHER                                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1300L)                       // 1151300 (0x119144), ViBoolean,  multi-channel
#define NISCOPE_ATTR_DDC_COMBINED_DECIMATION                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1301L)                       // 1151301 (0x119145), ViInt32,    multi-channel, read-only
#define NISCOPE_ATTR_SERIAL_DAC_CAL_VOLTAGE                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1302L)                       // 1151302 (0x119146), ViReal64
#define NISCOPE_ATTR_DELAY_BEFORE_INITIATE                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1304L)                       // 1151304 (0x119148), ViReal64
#define NISCOPE_ATTR_DDC_DIRECT_REGISTER_ADDRESS                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1305L)                       // 1151305 (0x119149), ViInt32
#define NISCOPE_ATTR_DDC_DIRECT_REGISTER_DATA                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1306L)                       // 1151306 (0x11914a), ViInt32


/****************************************************************************
 *-------------------------- Other Obsolete Values -------------------------*
 ****************************************************************************/

// -- Deprecated --
// use NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS instead
#define NISCOPE_ATTR_QUERY_INSTR_STATUS                                        NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS                          // 1050003 (0x100593)
// use NISCOPE_ATTR_SPECIFIC_DRIVER_PREFIX instead
#define NISCOPE_ATTR_SPECIFIC_PREFIX                                           NISCOPE_ATTR_SPECIFIC_DRIVER_PREFIX                           // 1050302 (0x1006be)
// use NISCOPE_ATTR_CHANNEL_COUNT instead
#define NISCOPE_ATTR_NUM_CHANNELS                                              NISCOPE_ATTR_CHANNEL_COUNT                                    // 1050203 (0x10065b)
// use NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION instead
#define NISCOPE_ATTR_DRIVER_REVISION                                           NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION                         // 1050551 (0x1007b7)
// use NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR instead
#define NISCOPE_ATTR_RESOURCE_DESCRIPTOR                                       NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR                           // 1050304 (0x1006c0)

// -- Do Not Use --
#define NISCOPE_ATTR_DRIVER_MAJOR_VERSION                                      IVISCOPE_ATTR_DRIVER_MAJOR_VERSION                            // 1050503 (0x100787)
#define NISCOPE_ATTR_DRIVER_MINOR_VERSION                                      IVISCOPE_ATTR_DRIVER_MINOR_VERSION                            // 1050504 (0x100788)
#define NISCOPE_ATTR_ENGINE_MAJOR_VERSION                                      IVISCOPE_ATTR_ENGINE_MAJOR_VERSION                            // 1050501 (0x100785)
#define NISCOPE_ATTR_ENGINE_MINOR_VERSION                                      IVISCOPE_ATTR_ENGINE_MINOR_VERSION                            // 1050502 (0x100786)
#define NISCOPE_ATTR_ENGINE_REVISION                                           IVISCOPE_ATTR_ENGINE_REVISION                                 // 1050553 (0x1007b9)
#define NISCOPE_ATTR_IO_SESSION                                                IVISCOPE_ATTR_IO_SESSION                                      // 1050322 (0x1006d2)
#define NISCOPE_ATTR_DEFER_UPDATE                                              IVI_ATTR_DEFER_UPDATE                                         // 1050051 (0x1005c3)
#define NISCOPE_ATTR_RETURN_DEFERRED_VALUES                                    IVI_ATTR_RETURN_DEFERRED_VALUES                               // 1050052 (0x1005c4)
#define NISCOPE_ATTR_PRIMARY_ERROR                                             IVISCOPE_ATTR_PRIMARY_ERROR                                   // 1050101 (0x1005f5)
#define NISCOPE_ATTR_SECONDARY_ERROR                                           IVISCOPE_ATTR_SECONDARY_ERROR                                 // 1050102 (0x1005f6)
#define NISCOPE_ATTR_ERROR_ELABORATION                                         IVISCOPE_ATTR_ERROR_ELABORATION                               // 1050103 (0x1005f7)

// -- Obsolete Specific Attributes --
// use NISCOPE_ATTR_MAX_INPUT_FREQUENCY instead
#define NISCOPE_ATTR_BANDWIDTH                                                 IVISCOPE_ATTR_MAX_INPUT_FREQUENCY                             // 1250006 (0x1312d6)
#define NISCOPE_ATTR_TRIGGER_OUTPUT_EVENT                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 10L)                         // 1150010 (0x118c3a)
#define NISCOPE_ATTR_TRIGGER_OUTPUT_SOURCE                                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 11L)                         // 1150011 (0x118c3b)
#define NISCOPE_ATTR_EXPORT_SAMP_CLK_OUTPUT_TERM                               NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL            // 1150091 (0x118c8b)

// -- Every Line Called By Configure Trigger Output Can Have A Different Event --
#define NISCOPE_ATTR_RTSI0_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 54L)                         // 1150054 (0x118c66)
#define NISCOPE_ATTR_RTSI1_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 55L)                         // 1150055 (0x118c67)
#define NISCOPE_ATTR_RTSI2_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 56L)                         // 1150056 (0x118c68)
#define NISCOPE_ATTR_RTSI3_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 57L)                         // 1150057 (0x118c69)
#define NISCOPE_ATTR_RTSI4_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 58L)                         // 1150058 (0x118c6a)
#define NISCOPE_ATTR_RTSI5_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 59L)                         // 1150059 (0x118c6b)
#define NISCOPE_ATTR_RTSI6_TRIGGER_OUTPUT_EVENT                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 60L)                         // 1150060 (0x118c6c)
#define NISCOPE_ATTR_PFI1_TRIGGER_OUTPUT_EVENT                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 61L)                         // 1150061 (0x118c6d)
#define NISCOPE_ATTR_PFI2_TRIGGER_OUTPUT_EVENT                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 62L)                         // 1150062 (0x118c6e)
#define NISCOPE_ATTR_STAR_TRIGGER_OUTPUT_EVENT                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 63L)                         // 1150063 (0x118c6f)

// -- Niscope_Attr_Trigger_Output_Event / Configuretriggeroutput Values --
#define NISCOPE_VAL_NO_EVENT                                                   0                                                             // 0 (0x0)
#define NISCOPE_VAL_STOP_TRIGGER_EVENT                                         1                                                             // 1 (0x1)
#define NISCOPE_VAL_START_TRIGGER_EVENT                                        2                                                             // 2 (0x2)

// -- Niscope_Attr_Trigger_Type Values --
#define NISCOPE_VAL_EDGE                                                       IVISCOPE_VAL_EDGE_TRIGGER                                     // 1 (0x1)
#define NISCOPE_VAL_HYSTERESIS                                                 (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 1L)            // 1001 (0x3e9)
#define NISCOPE_VAL_DIGITAL                                                    (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 2L)            // 1002 (0x3ea)
#define NISCOPE_VAL_WINDOW                                                     (IVISCOPE_VAL_TRIGGER_TYPE_SPECIFIC_EXT_BASE + 3L)            // 1003 (0x3eb)

// -- Niscope_Attr_Max_Input_Frequency Values --
#define NISCOPE_VAL_FULL_BANDWIDTH                                             0.0

// -- Niscope_Attr_Ddc_Pfir_Symmetry_Type And Niscope_Attr_Ddc_Discriminator_Fir_Symmetry_Type Values --
#define NISCOPE_VAL_EVEN                                                       0                                                             // 0 (0x0)
#define NISCOPE_VAL_ODD                                                        1                                                             // 1 (0x1)

// -- Niscope_Attr_Ddc_Pfir_Symmetry And Niscope_Attr_Ddc_Discriminator_Fir_Symmetry Values --
#define NISCOPE_VAL_SYMMETRIC                                                  0                                                             // 0 (0x0)
#define NISCOPE_VAL_ASYMMETRIC                                                 1                                                             // 1 (0x1)

// -- Niscope_Attr_Ddc_Discriminator_Fir_Input_Source Values --
#define NISCOPE_VAL_PHASE                                                      0                                                             // 0 (0x0)
#define NISCOPE_VAL_MAGNITUDE                                                  1                                                             // 1 (0x1)
#define NISCOPE_VAL_RESAMPLER                                                  2                                                             // 2 (0x2)

// -- Niscope_Attr_Ddc_Aout_Parallel_Output_Source And Niscope_Attr_Ddc_Bout_Parallel_Output_Source Values --
// Valid for AOUT only
#define NISCOPE_VAL_I_DATA                                                     0                                                             // 0 (0x0)
// Valid for both AOUT and BOUT
#define NISCOPE_VAL_MAGNITUDE_DATA                                             1                                                             // 1 (0x1)
// Valid for AOUT only
#define NISCOPE_VAL_FREQ_DATA                                                  2                                                             // 2 (0x2)
// Valid for BOUT only
#define NISCOPE_VAL_Q_DATA                                                     3                                                             // 3 (0x3)
// Valid for BOUT only
#define NISCOPE_VAL_PHASE_DATA                                                 4                                                             // 4 (0x4)

// -- Older Programs Only --
// The driver now uses an IEEE defined Nan (Not a Number) value to indicate an empty
// point in the waveform. Use the niScope_IsInvalidWfmElement function to determine
// if an element of a waveform array is invalid.
#define NISCOPE_MAX_VALID_WFM_VOLTAGE                                          1e+300
#define NISCOPE_INVALID_WFM_VOLTAGE                                            1e+301

// -- Clocking Terminal Values --
#define NISCOPE_VAL_PXI_CLOCK                                                  "VAL_PXI_CLOCK"

// -- Ni-Scope 3.7 Changed The Name Of The Advanced P2P Attribute --
#define NISCOPE_ATTR_P2P_ADVANCED_ATTRIBUTES_ENABLED                           NISCOPE_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED                 // 1150343 (0x118d87)

// -- Ni-Scope 3.9.1 - Pcie-5155 --
#define NISCOPE_ATTR_FETCH_DATA_JUSTIFICATION                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 233L)                        // 1150233 (0x118d19)

// -- Justification --
#define NISCOPE_VAL_JUSTIFY_LEFT                                               1                                                             // 1 (0x1)
#define NISCOPE_VAL_JUSTIFY_RIGHT                                              2                                                             // 2 (0x2)

// -- Level Sensitive Start Trigger.  Added For Pcie-5155 --
#define NISCOPE_ATTR_ENABLE_LEVEL_ACQ_ARM                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 410L)                        // 1150410 (0x118dca)

// -- Sync Trigger --
#define NISCOPE_ATTR_SYNC_TRIG_OUT_SOURCE                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 411L)                        // 1150411 (0x118dcb)
#define NISCOPE_ATTR_SYNC_TRIG_OUT_PULSE_WIDTH                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 412L)                        // 1150412 (0x118dcc)
#define NISCOPE_ATTR_SYNC_TRIG_OUT_PERIOD                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 413L)                        // 1150413 (0x118dcd)

// -- Sync Trigger Values --
#define NISCOPE_VAL_SYNC_TRIG_NONE                                             0                                                             // 0 (0x0)
#define NISCOPE_VAL_SYNC_TRIG_REFERENCE                                        1                                                             // 1 (0x1)
#define NISCOPE_VAL_SYNC_TRIG_TIMER                                            2                                                             // 2 (0x2)

// -- Self Calibration --
#define NISCOPE_ATTR_NO_RESET_DURING_SELF_CAL                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 415L)                        // 1150415 (0x118dcf)

// -- Osp --
#define NISCOPE_ATTR_ENABLE_PATTERN_NOISE_OSP                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 418L)                        // 1150418 (0x118dd2)
#define NISCOPE_ATTR_PATTERN_NOISE_OSP_OFFSET                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 419L)                        // 1150419 (0x118dd3)

// -- Synchronization Events --
#define NISCOPE_ATTR_ACQUISITION_ACTIVE_EVENT_OUTPUT_TERMINAL                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 381L)                        // 1150381 (0x118dad)
#define NISCOPE_ATTR_END_OF_WAVEFORM_EVENT_OUTPUT_TERMINAL                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 417L)                        // 1150417 (0x118dd1)

// -- Waveform Averaging --
#define NISCOPE_ATTR_WFM_AVG_ENABLED                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 383L)                        // 1150383 (0x118daf)
#define NISCOPE_ATTR_WFM_AVG_NUMBER_OF_WAVEFORMS                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 384L)                        // 1150384 (0x118db0)
#define NISCOPE_ATTR_OSP_TRIGGER_DELAY_TIME                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 416L)                        // 1150416 (0x118dd0)
#define NISCOPE_ATTR_ACCUM_SAMPLES_TO_DISCARD                                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 421L)                        // 1150421 (0x118dd5)

// -- Thresholding --
#define NISCOPE_ATTR_THRESHOLD_ENABLED                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 385L)                        // 1150385 (0x118db1)
#define NISCOPE_ATTR_THRESHOLD_LEVEL                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 386L)                        // 1150386 (0x118db2)
#define NISCOPE_ATTR_THRESHOLD_FLOOR                                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 387L)                        // 1150387 (0x118db3)
#define NISCOPE_ATTR_THRESHOLD_OFFSET                                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 388L)                        // 1150388 (0x118db4)
#define NISCOPE_ATTR_THRESHOLD_POLARITY                                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 389L)                        // 1150389 (0x118db5)
#define NISCOPE_ATTR_THRESHOLD_VALUE_TYPE                                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 420L)                        // 1150420 (0x118dd4)

// -- Niscope_Attr_Threshold_Polarity Values --
#define NISCOPE_VAL_THRESHOLD_SUPPRESS_BELOW                                   0                                                             // 0 (0x0)
#define NISCOPE_VAL_THRESHOLD_SUPPRESS_ABOVE                                   1                                                             // 1 (0x1)

// -- Niscope_Attr_Threshold_Value_Type Values --
#define NISCOPE_VAL_THRESHOLD_VALUE_TYPE_VOLTS                                 0                                                             // 0 (0x0)
#define NISCOPE_VAL_THRESHOLD_VALUE_TYPE_CODES                                 1                                                             // 1 (0x1)

// -- Local Peak Detection --
#define NISCOPE_ATTR_LOCAL_PEAK_DETECTION_ENABLED                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 390L)                        // 1150390 (0x118db6)
#define NISCOPE_ATTR_LOCAL_PEAK_DETECTION_ALGORITHM                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 391L)                        // 1150391 (0x118db7)
#define NISCOPE_ATTR_LOCAL_PEAK_DETECTION_FLOOR                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 392L)                        // 1150392 (0x118db8)
#define NISCOPE_ATTR_LOCAL_PEAK_DETECTION_MODE                                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 393L)                        // 1150393 (0x118db9)

// -- Niscope_Attr_Local_Peak_Detection_Algorithm Values --
#define NISCOPE_VAL_PEAKS                                                      0                                                             // 0 (0x0)
#define NISCOPE_VAL_VALLEYS                                                    1                                                             // 1 (0x1)

// -- Niscope_Attr_Local_Peak_Detection_Mode Values --
#define NISCOPE_VAL_MODE_GREATER_THAN                                          1                                                             // 1 (0x1)

// -- Array --
#define NISCOPE_ATTR_PEAK_ARRAY_DETECTION_WINDOW                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 430L)                        // 1150430 (0x118dde)
#define NISCOPE_ATTR_PEAK_ARRAY_INTERPOLATION_WINDOW                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 431L)                        // 1150431 (0x118ddf)

// -- Other Osp --
#define NISCOPE_ATTR_INVERT_DATA_ENABLED                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 414L)                        // 1150414 (0x118dce)
#define NISCOPE_ATTR_UNSIGNED_FETCH_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 422L)                        // 1150422 (0x118dd6)
#define NISCOPE_ATTR_ACQUISITION_STATE                                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 442L)                        // 1150442 (0x118dea)

// -- Niscope_Attr_Acquisition_State Value --
#define NISCOPE_VAL_ACQUISITION_STATE_UNKNOWN                                  0                                                             // 0 (0x0)
#define NISCOPE_VAL_ACQUISITION_STATE_IDLE                                     2                                                             // 2 (0x2)
#define NISCOPE_VAL_ACQUISITION_STATE_WAIT_FOR_START_TRIGGER                   3                                                             // 3 (0x3)
#define NISCOPE_VAL_ACQUISITION_STATE_MIN_PRETRIG_SAMPLING                     4                                                             // 4 (0x4)
#define NISCOPE_VAL_ACQUISITION_STATE_WAIT_FOR_TRIGGER_HOLDOFF                 5                                                             // 5 (0x5)
#define NISCOPE_VAL_ACQUISITION_STATE_WAIT_FOR_ARM_REFERENCE_TRIGGER           6                                                             // 6 (0x6)
#define NISCOPE_VAL_ACQUISITION_STATE_WAIT_FOR_REFERENCE_TRIGGER               7                                                             // 7 (0x7)
#define NISCOPE_VAL_ACQUISITION_STATE_POSTTRIG_SAMPLING                        8                                                             // 8 (0x8)
#define NISCOPE_VAL_ACQUISITION_STATE_WAIT_FOR_ADVANCE_TRIGGER                 9                                                             // 9 (0x9)

// We use native packing on Windows x64, which is on 8 byte boundaries
#if defined(_WIN64)
#define NISCOPE_STRUCT_PACK_SIZE 8
#else
#define NISCOPE_STRUCT_PACK_SIZE 1
#endif

/****************************************************************************
 *------------------------ Obsolete Type Definitions -----------------------*
 ****************************************************************************/
#pragma pack(push,NISCOPE_STRUCT_PACK_SIZE)
typedef struct tWfmInfo_struct
{
    ViInt32 actualSamples;
    ViReal64 absoluteInitialX;
    ViReal64 relativeInitialX;
    ViReal64 xIncrement;
    ViReal64 offset;
    ViReal64 gain;
    ViReal64 reserved1;
    ViReal64 reserved2;
} tWfmInfo;

#pragma pack(pop)
#pragma pack(push,8)
struct niScope_PeakArrayInfo
{
    ViInt32 recordNumber;
    ViInt32 peakCount;
    ViReal64 triggerTime;
    ViReal64 triggerDelay;
    ViReal64 xIncrement;
};

#pragma pack(pop)


/****************************************************************************
 *---- Obsolete functions and functions used for class driver compliance ---*
 ****************************************************************************/
// -- Deprecated --
ViStatus _VI_FUNC niScope_ClearError(
   ViSession vi);

ViStatus _VI_FUNC niScope_GetNextInterchangeWarning(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar interchangeWarning[]);

ViStatus _VI_FUNC niScope_ResetInterchangeCheck(
   ViSession vi);

ViStatus _VI_FUNC niScope_ClearInterchangeWarnings(
   ViSession vi);

ViStatus _VI_FUNC niScope_GetNextCoercionRecord(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar record[]);

ViStatus _VI_FUNC niScope_InvalidateAllAttributes(
   ViSession vi);

ViStatus _VI_FUNC niScope_ResetWithDefaults(
   ViSession vi);

ViStatus _VI_FUNC niScope_ConfigureAcquisitionType(
   ViSession vi,
   ViInt32 acquisitionType);

// -- Vertical --
ViStatus _VI_FUNC niScope_ConfigureChannel(
   ViSession vi,
   ViConstString channel,
   ViReal64 range,
   ViReal64 offset,
   ViInt32 coupling,
   ViReal64 probeAttenuation,
   ViBoolean enabled);

// -- Horizontal --
ViStatus _VI_FUNC niScope_ConfigureHorizontal(
   ViSession vi,
   ViReal64 timePerRecord,
   ViInt32 minNumPts,
   ViReal64 refPosition);

ViStatus _VI_FUNC niScope_ConfigureAcquisitionRecord(
   ViSession vi,
   ViReal64 timePerRecord,
   ViInt32 minNumPoints,
   ViReal64 acquisitionStartTime);

ViStatus _VI_FUNC niScope_ConfigureHorizontalRate(
   ViSession vi,
   ViReal64 minSampleRate,
   ViInt32 minNumPts,
   ViReal64 refPosition);

ViStatus _VI_FUNC niScope_ConfigureMultiHorizontal(
   ViSession vi,
   ViReal64 timePerRecord,
   ViInt32 minNumPts,
   ViReal64 refPosition,
   ViInt32 numRecords);

ViStatus _VI_FUNC niScope_ConfigureMultiHorizontalRate(
   ViSession vi,
   ViReal64 minSampleRate,
   ViInt32 minNumPts,
   ViReal64 refPosition,
   ViInt32 numRecords);

// -- Triggering --
ViStatus _VI_FUNC niScope_ConfigureTriggerSource(
   ViSession vi,
   ViConstString triggerSource,
   ViInt32 triggerType,
   ViReal64 triggerDelay,
   ViReal64 holdoff);

ViStatus _VI_FUNC niScope_ConfigureTrigger(
   ViSession vi,
   ViInt32 triggerType,
   ViReal64 holdoff);

ViStatus _VI_FUNC niScope_ConfigureTriggerCoupling(
   ViSession vi,
   ViInt32 coupling);

ViStatus _VI_FUNC niScope_ConfigureEdgeTrigger(
   ViSession vi,
   ViReal64 level,
   ViInt32 triggerCoupling,
   ViInt32 slope);

ViStatus _VI_FUNC niScope_ConfigureEdgeTriggerSource(
   ViSession vi,
   ViConstString source,
   ViReal64 level,
   ViInt32 slope);

ViStatus _VI_FUNC niScope_ConfigureHysteresisTrigger(
   ViSession vi,
   ViReal64 level,
   ViReal64 hysteresis,
   ViInt32 triggerCoupling,
   ViInt32 slope);

ViStatus _VI_FUNC niScope_ConfigureWindowTrigger(
   ViSession vi,
   ViReal64 lowLevel,
   ViReal64 highLevel,
   ViInt32 triggerCoupling,
   ViInt32 windowMode);

ViStatus _VI_FUNC niScope_ConfigureDigitalTrigger(
   ViSession vi,
   ViInt32 slope);

ViStatus _VI_FUNC niScope_SendSWTrigger(
   ViSession vi);

// -- Fetch Functions --
ViStatus _VI_FUNC niScope_ReadWaveform(
   ViSession vi,
   ViConstString channel,
   ViInt32 waveformSize,
   ViInt32 maxTime,
   ViReal64 waveform[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_FetchWaveform(
   ViSession vi,
   ViConstString channel,
   ViInt32 waveformSize,
   ViReal64 waveform[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_FetchWaveformFromOffset(
   ViSession vi,
   ViConstString channelName,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViReal64* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_FetchBinary8Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt8* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchBinary16Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt16* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchBinary32Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt32* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchMultiWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 recordNumber,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViReal64* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_FetchMultiBinary8Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 recordNumber,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt8* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchMultiBinary16Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 recordNumber,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt16* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchMultiBinary32Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 recordNumber,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViInt32* waveformArray,
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement,
   ViReal64* gainFactor,
   ViReal64* verticalOffset);

ViStatus _VI_FUNC niScope_FetchMinMaxWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformSize,
   ViReal64 minWaveform[],
   ViReal64 maxWaveform[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_ReadMinMaxWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformSize,
   ViInt32 maxTime,
   ViReal64 minWaveform[],
   ViReal64 maxWaveform[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_FetchMultiMinMaxWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 recordNumber,
   ViInt32 retrievalOffset,
   ViInt32 waveformSize,
   ViReal64 minWaveform[],
   ViReal64 maxWaveform[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_IsInvalidWfmElement(
   ViSession vi,
   ViReal64 elementValue,
   ViBoolean* isInvalid);

// -- Wavefom Measurement Functions --
ViStatus _VI_FUNC niScope_FetchWaveformMeasurementStats(
   ViSession vi,
   ViConstString channel,
   ViInt32 recordNumber,
   ViInt32 measFunction,
   ViReal64* measurement,
   ViReal64* mean,
   ViReal64* stdev,
   ViReal64* min,
   ViReal64* max,
   ViInt32* numInStats);

ViStatus _VI_FUNC niScope_FetchWaveformMeasurementArray(
   ViSession vi,
   ViConstString channel,
   ViInt32 recordNumber,
   ViInt32 measFunction,
   ViInt32 measArraySize,
   ViReal64 measArray[],
   ViInt32* actualPoints,
   ViReal64* initialX,
   ViReal64* xIncrement);

ViStatus _VI_FUNC niScope_ConfigureRefLevels(
   ViSession vi,
   ViReal64 low,
   ViReal64 mid,
   ViReal64 high);

ViStatus _VI_FUNC niScope_ReadWaveformMeasurement(
   ViSession vi,
   ViConstString channel,
   ViInt32 measFunction,
   ViInt32 maxTime,
   ViReal64* measurement);

ViStatus _VI_FUNC niScope_FetchWaveformMeasurement(
   ViSession vi,
   ViConstString channel,
   ViInt32 measFunction,
   ViReal64* measurement);

ViStatus _VI_FUNC niScope_FetchMultiWaveformMeasurement(
   ViSession vi,
   ViConstString channel,
   ViInt32 recordNumber,
   ViInt32 measFunction,
   ViReal64* measurement);

ViStatus _VI_FUNC niScope_WaitForAcquisitionToFinish(
   ViSession vi,
   ViInt32 maxTime);

ViStatus _VI_FUNC niScope_ConfigureTriggerOutput(
   ViSession vi,
   ViInt32 triggerEvent,
   ViConstString triggerOutput);

// -- Iviscopetvtrigger Extension --
ViStatus _VI_FUNC niScope_ConfigureTVTriggerSource(
   ViSession vi,
   ViConstString source,
   ViInt32 signalFormat,
   ViInt32 event,
   ViInt32 polarity);

ViStatus _VI_FUNC niScope_ConfigureTVTriggerLineNumber(
   ViSession vi,
   ViInt32 lineNumber);

// -- Iviscopeglitchtrigger Extension --
ViStatus _VI_FUNC niScope_ConfigureGlitchTriggerSource(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViReal64 glitchWidth,
   ViInt32 glitchPolarity,
   ViInt32 glitchCondition);

// -- Iviscopewidthtrigger Extension --
ViStatus _VI_FUNC niScope_ConfigureWidthTriggerSource(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 level,
   ViReal64 widthLowThreshold,
   ViReal64 widthHighTreshold,
   ViInt32 widthPolarity,
   ViInt32 widthCondition);

// -- Iviscoperunttrigger Extension --
ViStatus _VI_FUNC niScope_ConfigureRuntTriggerSource(
   ViSession vi,
   ViConstString triggerSource,
   ViReal64 runtLowThreshold,
   ViReal64 runtHighTreshold,
   ViInt32 runtPolarity);

// -- Calibrate --
ViStatus _VI_FUNC niScope_Calibrate(
   ViSession vi,
   ViConstString channel,
   ViInt32 calibrationOperation,
   ViReal64 referenceVoltage);

// -- Error Handlers --
ViStatus _VI_FUNC niScope_error_query(
   ViSession vi,
   ViInt32* errCode,
   ViChar errMessage[256]);

ViStatus _VI_FUNC niScope_GetErrorInfo(
   ViSession vi,
   ViStatus* primaryError,
   ViStatus* secondaryError,
   ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niScope_ClearErrorInfo(
   ViSession vi);

ViStatus _VI_FUNC niScope_error_message(
   ViSession vi,
   ViStatus errorCode,
   ViChar errorMessage[256]);

// -- Experimental Prototypes, Subject To Change --
// use niScope_FetchBinary instead
ViStatus _VI_FUNC niScope_DirectDMAFetchBinary(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViInt32 numSamples,
   ViInt32 bufferSize,
   void* bufferAddress,
   struct niScope_wfmInfo* wfmInfo,
   ViUInt32* offsetToFirstSample);

ViStatus _VI_FUNC niScope_ExportAttributes(
   ViSession vi);

ViStatus _VI_FUNC niScope_ImportAttributes(
   ViSession vi);

// -- Register Access Functions --
ViStatus _VI_FUNC niScope_ReadRegister(
   ViSession vi,
   ViInt32 size,
   ViInt32 offset,
   ViUInt32* value);

ViStatus _VI_FUNC niScope_WriteRegister(
   ViSession vi,
   ViInt32 size,
   ViInt32 offset,
   ViUInt32 value);

// -- Functions Reserved For Class Driver Use Only. End-Users Should Not Call These. --
ViStatus _VI_FUNC niScope_IviInit(
   ViRsrc resourceName,
   ViBoolean idQuery,
   ViBoolean reset,
   ViSession vi);

ViStatus _VI_FUNC niScope_IviClose(
   ViSession vi);

// -- Peak --
ViStatus _VI_FUNC niScope_FetchPeakArrayTime32Ampl16(
   ViSession vi,
   ViInt32 maxPeaks,
   ViReal64 timeout,
   struct niScope_PeakArrayInfo* info,
   ViUInt32* peakTimes,
   ViUInt16* peakAmplitudes);

// -- Ni-5620 Specific Functions --
ViStatus _VI_FUNC niScope_SetDDCFilterCoefficients(
   ViSession vi,
   ViConstString channel,
   ViInt32 coefficientType,
   ViInt32 numCoefficients,
   ViInt32* coefficients);

ViStatus _VI_FUNC niScope_CalSetSerialDACVoltageEeprom(
   ViSession vi,
   ViReal32 serialDACVolts);

ViStatus _VI_FUNC niScope_CalSetADCVoltageEeprom(
   ViSession vi,
   ViReal32 adcVoltageGain,
   ViReal32 adcVoltageOffset);

ViStatus _VI_FUNC niScope_CalSetFREeprom(
   ViSession vi,
   ViInt32 numCoefficients,
   ViReal32* polynomialFitCoefficients);

ViStatus _VI_FUNC niScope_CalGetSerialDACVoltageEeprom(
   ViSession vi,
   ViReal32* serialDACVolts);

ViStatus _VI_FUNC niScope_CalGetADCVoltageEeprom(
   ViSession vi,
   ViReal32* adcVoltageGain,
   ViReal32* adcVoltageOffset);

ViStatus _VI_FUNC niScope_CalGetFREeprom(
   ViSession vi,
   ViInt32 numCoefficients,
   ViReal32* polynomialFitCoefficients);



/****************************************************************************
 *--- Not Recommended error strings (these strings are subject to change) --*
 ****************************************************************************/
#define NISCOPE_WARNMSG_HEATER_CIRCUIT_TEMPERATURE     "Onboard temperature stabilization circuit requires calibration."
#define NISCOPE_WARNMSG_INVALID_DATA                   "Data acquired during the acquisition is possibly invalid. May be caused by high frequency transients or input voltage exceeding the maximum for given range."
#define NISCOPE_WARNMSG_CHANNEL_OVERLOAD               "The 50 ohm protection on one or more channels has been disabled because of excess signal power."
#define NISCOPE_WARNMSG_AUTOSETUP_NO_SIGNAL            "Auto Setup was unable to find a signal."
#define NISCOPE_WARNMSG_PLL_UNLOCKED                   "The PLL is not locked."
#define NISCOPE_WARNMSG_PLL_UNLOCKED_AND_ADC_OVERLOAD  "The PLL is not locked and the ADC has an overload."
#define NISCOPE_WARNMSG_TIMESTAMP_ROLLOVER             "The timestamp counter has rolled over."
#define NISCOPE_WARNMSG_ADC_OVERLOAD                   "One or more channels has an ADC overload."
#define NISCOPE_ERRMSG_SOFTWARE_FAILURE                "Software failure occurred during operation."
#define NISCOPE_ERRMSG_HARDWARE_FAILURE                "Hardware failure occurred during operation."
#define NISCOPE_ERRMSG_INSUFFICIENT_MEMORY             "Insufficient on-board memory available to perform the acquisition."
#define NISCOPE_ERRMSG_INVALID_DATA                    "Data acquired during the acquisition is invalid."
#define NISCOPE_ERRMSG_GAIN_CAL_FAILURE                "Unable to perform gain calibration"
#define NISCOPE_ERRMSG_SINE_CAL_FAILURE                "Unable to acquire valid sine wave for calibration"
#define NISCOPE_ERRMSG_LIN_CAL_FAILURE                 "Unable to calculate linearity coefficients"
#define NISCOPE_ERRMSG_ADC_CAL_FAILURE                 "ADC exceeds linearity specs"
#define NISCOPE_ERRMSG_ACQ_IN_PROGRESS                 "A previous acquisition is still in progress. If you are attempting to change an attribute, note you can only change fetch attributes while an acquisition is still in progress."
#define NISCOPE_ERRMSG_DATA_NOT_AVAILABLE              "Data acquired during the acquisition is not available."
#define NISCOPE_ERRMSG_HEATER_CIRCUIT_CAL_FAILURE      "Unable to calibrate onboard temperature stablization circuit."
#define NISCOPE_ERRMSG_FLEXRES_CONFIG_CORRUPT          "The FlexRes configuration files are corrupt, please reinstall niScope software or contact National Instruments."
#define NISCOPE_ERRMSG_GAIN_OFFSET_CAL_FAILURE         "Unable to perform gain/offset calibration."
#define NISCOPE_ERRMSG_CREATE_THREAD                   "Acquisition thread could not be created."
#define NISCOPE_ERRMSG_WRONG_PASSWORD                  "Password in EEPROM does not match the given password."
#define NISCOPE_ERRMSG_INVALID_GAIN                    "Invalid gain specified. Use the gain constants defined in the calibration header file."
#define NISCOPE_ERRMSG_INVALID_CAL_SESSION             "This function requires an external calibration session. Call niScope_CalStart instead of niScope_init to get the proper session type."
#define NISCOPE_ERRMSG_BAD_MEASUREMENT                 "The specified waveform measurement is not allowed with this function."
#define NISCOPE_ERRMSG_BUFFER_NOT_ACQUIRED             "Requested buffer has not been acquired yet."
#define NISCOPE_ERRMSG_TRIGGER_HAS_NOT_OCCURRED        "The trigger has not occurred for the requested buffer, so data cannot be fetched relative to the trigger."
#define NISCOPE_ERRMSG_ILLEGAL_RELATIVE_TO             "Illegal relativeTo parameter."
#define NISCOPE_ERRMSG_DATA_OVERWRITTEN                "The requested data has been overwritten in memory so it is no longer available for fetching."
#define NISCOPE_ERRMSG_INVALID_TIMESTAMP_EVENT_TAG     "Invalid timestamp event tag."
#define NISCOPE_ERRMSG_TIMEOUT_TRANSFERRING_TIMESTAMPS "Timeout transferring timestamps."
#define NISCOPE_ERRMSG_TIMEOUT_CHECKING_STATUS         "Timeout checking status."
#define NISCOPE_ERRMSG_TIMEOUT_TRANSFERRING_DATA       "Timeout transferring data."
#define NISCOPE_ERRMSG_PLL_FAILURE                     "PLL failure."
#define NISCOPE_ERRMSG_PAR_TO_SER_CONV_FAILURE         "Parallel to serial convertor failure."
#define NISCOPE_ERRMSG_DMA_CONFIG_ERROR                "DMA config error."
#define NISCOPE_ERRMSG_ILLEGAL_USER_OFFSET             "The user offset specified is not valid."
#define NISCOPE_ERRMSG_NOT_A_SCOPE                     "The specified resource name is not assigned to an NI digitizer.  Verify the resource name in Measurement & Automation Explorer (MAX).  \
To use a DAQmx device with a DAQ::N style name (e.g. DAQ::1), rename the device in MAX to N (e.g. 1)."
#define NISCOPE_ERRMSG_TIMEOUT_CLEARING_TIO            "Timeout clearing TIO."
#define NISCOPE_ERRMSG_RIS_DID_NOT_COMPLETE            "RIS did not complete so data is not available."
#define NISCOPE_ERRMSG_INVALID_RIS_METHOD              "RIS method is invalid."
#define NISCOPE_ERRMSG_INVALID_RIS_NUM_AVERAGES        "RIS num averages attribute is invalid. It must be greater than 0."
#define NISCOPE_ERRMSG_ILLEGAL_DATATYPE                "Illegal data type parameter. See niScope.h for legal defined values."
#define NISCOPE_ERRMSG_ATTRIBUTES_DIFFER_BY_CHANNEL    "Getting a channel based attribute value failed because the queried channels have different values.  Please specify a channel when querying a channel based attribute."
#define NISCOPE_ERRMSG_TRIGGER_DELAY_INVALID_WITH_RIS  "The trigger delay parameter to the configure trigger function must be zero during RIS acquisitions."
#define NISCOPE_ERRMSG_INITIATE_NOT_CALLED             "An acquisition has not been initiated."
#define NISCOPE_ERRMSG_INVALID_FUNCTION_USE            "This function may not be used for fetching multiple waveforms."
#define NISCOPE_ERRMSG_HOLDOFF_DELAY_NONZERO           "Specifying either trigger holdoff or trigger delay is allowed, but not both."
#define NISCOPE_ERRMSG_CHANNEL_NAME_TOO_LONG           "The channel name is too long."
#define NISCOPE_ERRMSG_DIGITIZER_ALREADY_IN_USE        "The digitizer is being used by another application or process."
#define NISCOPE_ERRMSG_SIM_MODEL_NOT_SUPPORTED         "Simulation does not support the selected model and board type."
#define NISCOPE_ERRMSG_SPECIFICDLL_LOAD_FAILURE        "The specific niScopeDAQ or niScopeDMF dll could not be loaded."
#define NISCOPE_ERRMSG_SPECIFICDLL_GET_ADDRESS_FAILURE "An exported function address could not be obtained from the specific niScopeDAQ or niScopeDMF dll."
#define NISCOPE_ERRMSG_TRIGGER_TYPE_INVALID            "The configure trigger type is invalid or not supported"
#define NISCOPE_ERRMSG_INVALID_FETCH_PARAMETERS        "The fetch parameters are not valid."
#define NISCOPE_ERRMSG_EXT_CAL_NOT_COMPLETE            "Attempt to store calibration constants without completing all the necessary external calibration steps.Consult the calibration procedure. \
Verify that all necessary steps are performed before closing the external calibration session."
#define NISCOPE_ERRMSG_EXT_CAL_CONSTS_INVALID          "External calibration constants are invalid.  Perform an external calibration. Contact National Instruments if you need additional information."
#define NISCOPE_ERRMSG_INVALID_NUM_WAVEFORMS           "This function may not be used for fetching multiple waveforms."

/* Not recommended */
#define NISCOPE_ERROR_CODES_AND_MSGS \
{NISCOPE_WARN_HEATER_CIRCUIT_TEMPERATURE,          NISCOPE_WARNMSG_HEATER_CIRCUIT_TEMPERATURE},    \
{NISCOPE_WARN_INVALID_DATA,                        NISCOPE_WARNMSG_INVALID_DATA},                  \
{NISCOPE_WARN_CHANNEL_OVERLOAD,                    NISCOPE_WARNMSG_CHANNEL_OVERLOAD},              \
{NISCOPE_WARN_AUTOSETUP_NO_SIGNAL,                 NISCOPE_WARNMSG_AUTOSETUP_NO_SIGNAL},           \
{NISCOPE_WARN_PLL_UNLOCKED,                        NISCOPE_WARNMSG_PLL_UNLOCKED},                  \
{NISCOPE_WARN_PLL_UNLOCKED_AND_ADC_OVERLOAD,       NISCOPE_WARNMSG_PLL_UNLOCKED_AND_ADC_OVERLOAD}, \
{NISCOPE_WARN_TIMESTAMP_ROLLOVER,                  NISCOPE_WARNMSG_TIMESTAMP_ROLLOVER},            \
{NISCOPE_WARN_ADC_OVERLOAD,                        NISCOPE_WARNMSG_ADC_OVERLOAD},                  \
{NISCOPE_ERROR_SOFTWARE_FAILURE,                   NISCOPE_ERRMSG_SOFTWARE_FAILURE},               \
{NISCOPE_ERROR_HARDWARE_FAILURE,                   NISCOPE_ERRMSG_HARDWARE_FAILURE},               \
{NISCOPE_ERROR_INSUFFICIENT_MEMORY,                NISCOPE_ERRMSG_INSUFFICIENT_MEMORY},            \
{NISCOPE_ERROR_INVALID_DATA,                       NISCOPE_ERRMSG_INVALID_DATA},                   \
{NISCOPE_ERROR_GAIN_CAL_FAILURE,                   NISCOPE_ERRMSG_GAIN_CAL_FAILURE},               \
{NISCOPE_ERROR_SINE_CAL_FAILURE,                   NISCOPE_ERRMSG_SINE_CAL_FAILURE},               \
{NISCOPE_ERROR_LIN_CAL_FAILURE,                    NISCOPE_ERRMSG_LIN_CAL_FAILURE},                \
{NISCOPE_ERROR_ADC_CAL_FAILURE,                    NISCOPE_ERRMSG_ADC_CAL_FAILURE},                \
{NISCOPE_ERROR_ACQ_IN_PROGRESS,                    NISCOPE_ERRMSG_ACQ_IN_PROGRESS},                \
{NISCOPE_ERROR_DATA_NOT_AVAILABLE,                 NISCOPE_ERRMSG_DATA_NOT_AVAILABLE},             \
{NISCOPE_ERROR_HEATER_CIRCUIT_CAL_FAILURE,         NISCOPE_ERRMSG_HEATER_CIRCUIT_CAL_FAILURE},     \
{NISCOPE_ERROR_FLEXRES_CONFIG_CORRUPT,             NISCOPE_ERRMSG_FLEXRES_CONFIG_CORRUPT},         \
{NISCOPE_ERROR_GAIN_OFFSET_CAL_FAILURE,            NISCOPE_ERRMSG_GAIN_OFFSET_CAL_FAILURE},        \
{NISCOPE_ERROR_CREATE_THREAD,                      NISCOPE_ERRMSG_CREATE_THREAD},                  \
{NISCOPE_ERROR_WRONG_PASSWORD,                     NISCOPE_ERRMSG_WRONG_PASSWORD},                 \
{NISCOPE_ERROR_INVALID_GAIN,                       NISCOPE_ERRMSG_INVALID_GAIN},                   \
{NISCOPE_ERROR_INVALID_CAL_SESSION,                NISCOPE_ERRMSG_INVALID_CAL_SESSION},            \
{NISCOPE_ERROR_BAD_MEASUREMENT,                    NISCOPE_ERRMSG_BAD_MEASUREMENT},                \
{NISCOPE_ERROR_BUFFER_NOT_ACQUIRED,                NISCOPE_ERRMSG_BUFFER_NOT_ACQUIRED},            \
{NISCOPE_ERROR_TRIGGER_HAS_NOT_OCCURRED,           NISCOPE_ERRMSG_TRIGGER_HAS_NOT_OCCURRED},       \
{NISCOPE_ERROR_ILLEGAL_RELATIVE_TO,                NISCOPE_ERRMSG_ILLEGAL_RELATIVE_TO},            \
{NISCOPE_ERROR_DATA_OVERWRITTEN,                   NISCOPE_ERRMSG_DATA_OVERWRITTEN},               \
{NISCOPE_ERROR_INVALID_TIMESTAMP_EVENT_TAG,        NISCOPE_ERRMSG_INVALID_TIMESTAMP_EVENT_TAG},    \
{NISCOPE_ERROR_TIMEOUT_TRANSFERRING_TIMESTAMPS,    NISCOPE_ERRMSG_TIMEOUT_TRANSFERRING_TIMESTAMPS},\
{NISCOPE_ERROR_TIMEOUT_CHECKING_STATUS,            NISCOPE_ERRMSG_TIMEOUT_CHECKING_STATUS},        \
{NISCOPE_ERROR_TIMEOUT_TRANSFERRING_DATA,          NISCOPE_ERRMSG_TIMEOUT_TRANSFERRING_DATA},      \
{NISCOPE_ERROR_PLL_FAILURE,                        NISCOPE_ERRMSG_PLL_FAILURE},                    \
{NISCOPE_ERROR_PAR_TO_SER_CONV_FAILURE,            NISCOPE_ERRMSG_PAR_TO_SER_CONV_FAILURE},        \
{NISCOPE_ERROR_DMA_CONFIG_ERROR,                   NISCOPE_ERRMSG_DMA_CONFIG_ERROR},               \
{NISCOPE_ERROR_ILLEGAL_USER_OFFSET,                NISCOPE_ERRMSG_ILLEGAL_USER_OFFSET},            \
{NISCOPE_ERROR_NOT_A_SCOPE,                        NISCOPE_ERRMSG_NOT_A_SCOPE},                    \
{NISCOPE_ERROR_TIMEOUT_CLEARING_TIO,               NISCOPE_ERRMSG_TIMEOUT_CLEARING_TIO},           \
{NISCOPE_ERROR_RIS_DID_NOT_COMPLETE,               NISCOPE_ERRMSG_RIS_DID_NOT_COMPLETE},           \
{NISCOPE_ERROR_INVALID_RIS_METHOD,                 NISCOPE_ERRMSG_INVALID_RIS_METHOD},             \
{NISCOPE_ERROR_INVALID_RIS_NUM_AVERAGES,           NISCOPE_ERRMSG_INVALID_RIS_NUM_AVERAGES},       \
{NISCOPE_ERROR_ILLEGAL_DATATYPE,                   NISCOPE_ERRMSG_ILLEGAL_DATATYPE},               \
{NISCOPE_ERROR_ATTRIBUTES_DIFFER_BY_CHANNEL,       NISCOPE_ERRMSG_ATTRIBUTES_DIFFER_BY_CHANNEL},   \
{NISCOPE_ERROR_TRIGGER_DELAY_INVALID_WITH_RIS,     NISCOPE_ERRMSG_TRIGGER_DELAY_INVALID_WITH_RIS}, \
{NISCOPE_ERROR_INITIATE_NOT_CALLED,                NISCOPE_ERRMSG_INITIATE_NOT_CALLED},            \
{NISCOPE_ERROR_INVALID_FUNCTION_USE,               NISCOPE_ERRMSG_INVALID_FUNCTION_USE},           \
{NISCOPE_ERROR_HOLDOFF_DELAY_NONZERO,              NISCOPE_ERRMSG_HOLDOFF_DELAY_NONZERO},          \
{NISCOPE_ERROR_CHANNEL_NAME_TOO_LONG,              NISCOPE_ERRMSG_CHANNEL_NAME_TOO_LONG},          \
{NISCOPE_ERROR_DIGITIZER_ALREADY_IN_USE,           NISCOPE_ERRMSG_DIGITIZER_ALREADY_IN_USE},       \
{NISCOPE_ERROR_SIM_MODEL_NOT_SUPPORTED,            NISCOPE_ERRMSG_SIM_MODEL_NOT_SUPPORTED},        \
{NISCOPE_ERROR_SPECIFICDLL_LOAD_FAILURE,           NISCOPE_ERRMSG_SPECIFICDLL_LOAD_FAILURE},       \
{NISCOPE_ERROR_SPECIFICDLL_GET_ADDRESS_FAILURE,    NISCOPE_ERRMSG_SPECIFICDLL_GET_ADDRESS_FAILURE},\
{NISCOPE_ERROR_TRIGGER_TYPE_INVALID,               NISCOPE_ERRMSG_TRIGGER_TYPE_INVALID},           \
{NISCOPE_ERROR_INVALID_FETCH_PARAMETERS,           NISCOPE_ERRMSG_INVALID_FETCH_PARAMETERS},       \
{NISCOPE_ERROR_INVALID_NUM_WAVEFORMS,              NISCOPE_ERRMSG_INVALID_NUM_WAVEFORMS},          \
{NISCOPE_ERROR_EXT_CAL_NOT_COMPLETE,               NISCOPE_ERRMSG_EXT_CAL_NOT_COMPLETE},           \
{NISCOPE_ERROR_EXT_CAL_CONSTS_INVALID,             NISCOPE_ERRMSG_EXT_CAL_CONSTS_INVALID}

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* __NISCOPE_HEADER_OBSOLETE */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niswitch.h sha256=f7004b8567eee8e374b74dcc9a49fbaa84d83b77041246da87b25fe1bc1938ba bytes=47529 -->
## FILE: imports/include/niswitch.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niswitch.h`
- sha256: `f7004b8567eee8e374b74dcc9a49fbaa84d83b77041246da87b25fe1bc1938ba`
- bytes: 47529

````c
/****************************************************************************
 *                       NI Switch
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 1998-2015.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niSwitch.h
 * Purpose:  NI Switch
 *           instrument driver declarations.
 *
 ****************************************************************************/

#ifndef ___niswitch_h___
#define ___niswitch_h___

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <ivi.h>
#include <IviSwtch.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "niswitchTopologies.h"

#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

#ifdef __cplusplus
 extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NISWITCH_MAJOR_VERSION                  15     /* Instrument driver major version */
#define NISWITCH_MINOR_VERSION                  9      /* Instrument driver minor version */

#define NISWITCH_CLASS_SPEC_MAJOR_VERSION       4      /* Class specification major version */
#define NISWITCH_CLASS_SPEC_MINOR_VERSION       0      /* Class specification minor version */

#define NISWITCH_SUPPORTED_INSTRUMENT_MODELS    "SCXI-1127,"\
                                                "SCXI-1128,"\
                                                "SCXI-1129,"\
                                                "SCXI-1130,"\
                                                "SCXI-1160,"\
                                                "SCXI-1161,"\
                                                "SCXI-1163R,"\
                                                "SCXI-1166,"\
                                                "SCXI-1167,"\
                                                "SCXI-1169,"\
                                                "SCXI-1175,"\
                                                "SCXI-1190,"\
                                                "SCXI-1191,"\
                                                "SCXI-1192,"\
                                                "SCXI-1193,"\
                                                "SCXI-1194,"\
                                                "SCXI-1195,"\
                                                "PXI-2501,"\
                                                "PXI-2503,"\
                                                "PXI-2510,"\
                                                "PXI-2512,"\
                                                "PXI-2514,"\
                                                "PXI-2515,"\
                                                "PXI-2520,"\
                                                "PXI-2521,"\
                                                "PXI-2522,"\
                                                "PXI-2523,"\
                                                "PXI-2527,"\
                                                "PXI-2529,"\
                                                "PXI-2530,"\
                                                "PXI-2531,"\
                                                "PXI-2532,"\
                                                "PXI-2533,"\
                                                "PXI-2534,"\
                                                "PXI-2535,"\
                                                "PXI-2536,"\
                                                "PXI-2540,"\
                                                "PXI-2541,"\
                                                "PXI-2542,"\
                                                "PXI-2543,"\
                                                "PXI-2544,"\
                                                "PXI-2545,"\
                                                "PXI-2546,"\
                                                "PXI-2547,"\
                                                "PXI-2548,"\
                                                "PXI-2549,"\
                                                "PXI-2554,"\
                                                "PXI-2555,"\
                                                "PXI-2556,"\
                                                "PXI-2557,"\
                                                "PXI-2558,"\
                                                "PXI-2559,"\
                                                "PXI-2564,"\
                                                "PXI-2565,"\
                                                "PXI-2566,"\
                                                "PXI-2567,"\
                                                "PXI-2568,"\
                                                "PXI-2569,"\
                                                "PXI-2570,"\
                                                "PXI-2571,"\
                                                "PXI-2575,"\
                                                "PXI-2576,"\
                                                "PXI-2584,"\
                                                "PXI-2585,"\
                                                "PXI-2586,"\
                                                "PXI-2590,"\
                                                "PXI-2591,"\
                                                "PXI-2593,"\
                                                "PXI-2594,"\
                                                "PXI-2595,"\
                                                "PXI-2596,"\
                                                "PXI-2597,"\
                                                "PXI-2598,"\
                                                "PXI-2599,"\
                                                "PXI-2720,"\
                                                "PXI-2722,"\
                                                "PXI-2796,"\
                                                "PXI-2797,"\
                                                "PXI-2798,"\
                                                "PXI-2799,"\
                                                "NI 2810,"\
                                                "NI 2811,"\
                                                "NI 2812,"\
                                                "NI 2813,"\
                                                "NI 2814,"\
                                                "NI 2815,"\
                                                "NI 2816,"\
                                                "NI 2817,"\
                                                "NI 2833,"\
                                                "NI 2834,"\
                                                "NI 2865,"\
                                                "PXIe-2512,"\
                                                "PXIe-2514,"\
                                                "PXIe-2515,"\
                                                "PXIe-2524,"\
                                                "PXIe-2525,"\
                                                "PXIe-2526,"\
                                                "PXIe-2527,"\
                                                "PXIe-2529,"\
                                                "PXIe-2531,"\
                                                "PXIe-2532,"\
                                                "PXIe-2540,"\
                                                "PXIe-2541,"\
                                                "PXIe-2542,"\
                                                "PXIe-2543,"\
                                                "PXIe-2544,"\
                                                "PXIe-2569,"\
                                                "PXIe-2575,"\
                                                "PXIe-2593,"\
                                                "PXIe-2725,"\
                                                "PXIe-2727,"\
                                                "PXIe-2737,"\
                                                "PXIe-2738,"\
                                                "PXIe-2739,"\
                                                "PXIe-2746,"\
                                                "PXIe-2747,"\
                                                "PXIe-2748,"\
                                                "PXIe-2790"

#define NISWITCH_DRIVER_VENDOR                  "National Instruments"
#define NISWITCH_DRIVER_DESCRIPTION             "NI-SWITCH Driver"

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/

    /*- IVI Inherent Instrument Attributes ---------------------------------*/

    /*- User Options -------------------------------------------------------*/
#define NISWITCH_ATTR_RANGE_CHECK                   IVI_ATTR_RANGE_CHECK                    /* ViBoolean */
#define NISWITCH_ATTR_QUERY_INSTRUMENT_STATUS       IVI_ATTR_QUERY_INSTR_STATUS             /* ViBoolean */
#define NISWITCH_ATTR_CACHE                         IVI_ATTR_CACHE                          /* ViBoolean */
#define NISWITCH_ATTR_SIMULATE                      IVI_ATTR_SIMULATE                       /* ViBoolean */
#define NISWITCH_ATTR_RECORD_COERCIONS              IVI_ATTR_RECORD_COERCIONS               /* ViBoolean */
#define NISWITCH_ATTR_INTERCHANGE_CHECK             IVI_ATTR_INTERCHANGE_CHECK              /* ViBoolean */

    /*- Instrument Capabilities --------------------------------------------*/
#define NISWITCH_ATTR_CHANNEL_COUNT                 IVI_ATTR_NUM_CHANNELS                   /* ViInt32,  read-only  */
#define NISWITCH_ATTR_GROUP_CAPABILITIES            IVI_ATTR_GROUP_CAPABILITIES             /* ViString, read-only */

    /*- Driver Information  ------------------------------------------------*/
#define NISWITCH_ATTR_SPECIFIC_DRIVER_PREFIX        IVI_ATTR_SPECIFIC_DRIVER_PREFIX         /* ViString, read-only  */
#define NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS   IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS    /* ViString, read-only  */
#define NISWITCH_ATTR_INSTRUMENT_MANUFACTURER       IVI_ATTR_INSTRUMENT_MANUFACTURER        /* ViString, read-only  */
#define NISWITCH_ATTR_INSTRUMENT_MODEL              IVI_ATTR_INSTRUMENT_MODEL               /* ViString, read-only  */
#define NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION  IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION   /* ViString, read-only  */
#define NISWITCH_ATTR_SPECIFIC_DRIVER_REVISION      IVI_ATTR_SPECIFIC_DRIVER_REVISION       /* ViString, read-only  */
#define NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR        IVI_ATTR_SPECIFIC_DRIVER_VENDOR         /* ViString, read-only  */
#define NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32, read-only */
#define NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32, read-only */
#define NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION   IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION    /* ViString, read-only  */
#define NISWITCH_ATTR_DRIVER_SETUP                  IVI_ATTR_DRIVER_SETUP                   /* ViString, read-only  */

    /*- Advanced Session Information ---------------------------------------*/
#define NISWITCH_ATTR_LOGICAL_NAME                  IVI_ATTR_LOGICAL_NAME                   /* ViString, read-only  */
#define NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR        IVI_ATTR_RESOURCE_DESCRIPTOR            /* ViString, read-only  */

    /*- Configuration Attributes -------------------------------------------*/
#define NISWITCH_ATTR_IS_SOURCE_CHANNEL             IVISWTCH_ATTR_IS_SOURCE_CHANNEL         /* ViBoolean, channel-based */
#define NISWITCH_ATTR_IS_CONFIGURATION_CHANNEL      IVISWTCH_ATTR_IS_CONFIGURATION_CHANNEL  /* ViBoolean, channel-based */

    /*- Status Attributes --------------------------------------------------*/
#define NISWITCH_ATTR_IS_DEBOUNCED                  IVISWTCH_ATTR_IS_DEBOUNCED              /* ViBoolean, read-only */

    /*- Device Information Attributes --------------------------------------*/
#define NISWITCH_ATTR_SETTLING_TIME                 IVISWTCH_ATTR_SETTLING_TIME             /* ViReal64, channel-based */
#define NISWITCH_ATTR_BANDWIDTH                     IVISWTCH_ATTR_BANDWIDTH                 /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_DC_VOLTAGE                IVISWTCH_ATTR_MAX_DC_VOLTAGE            /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_AC_VOLTAGE                IVISWTCH_ATTR_MAX_AC_VOLTAGE            /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT      IVISWTCH_ATTR_MAX_SWITCHING_AC_CURRENT  /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT      IVISWTCH_ATTR_MAX_SWITCHING_DC_CURRENT  /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_CARRY_AC_CURRENT          IVISWTCH_ATTR_MAX_CARRY_AC_CURRENT      /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_CARRY_DC_CURRENT          IVISWTCH_ATTR_MAX_CARRY_DC_CURRENT      /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_SWITCHING_AC_POWER        IVISWTCH_ATTR_MAX_SWITCHING_AC_POWER    /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_SWITCHING_DC_POWER        IVISWTCH_ATTR_MAX_SWITCHING_DC_POWER    /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_CARRY_AC_POWER            IVISWTCH_ATTR_MAX_CARRY_AC_POWER        /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_MAX_CARRY_DC_POWER            IVISWTCH_ATTR_MAX_CARRY_DC_POWER        /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_CHARACTERISTIC_IMPEDANCE      IVISWTCH_ATTR_CHARACTERISTIC_IMPEDANCE  /* ViReal64, channel-based, read-only */
#define NISWITCH_ATTR_WIRE_MODE                     IVISWTCH_ATTR_WIRE_MODE                 /* ViInt32,  channel-based, read-only */
#define NISWITCH_ATTR_NUM_OF_ROWS                   IVISWTCH_ATTR_NUM_OF_ROWS               /* ViInt32,  read-only */
#define NISWITCH_ATTR_NUM_OF_COLUMNS                IVISWTCH_ATTR_NUM_OF_COLUMNS            /* ViInt32,  read-only */

    /*- Scanning Attributes ------------------------------------------------*/
#define NISWITCH_ATTR_SCAN_LIST                     IVISWTCH_ATTR_SCAN_LIST                 /* ViString */
#define NISWITCH_ATTR_SCAN_MODE                     IVISWTCH_ATTR_SCAN_MODE                 /* ViInt32  */
#define NISWITCH_ATTR_TRIGGER_INPUT                 IVISWTCH_ATTR_TRIGGER_INPUT             /* ViInt32  */
#define NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT          IVISWTCH_ATTR_SCAN_ADVANCED_OUTPUT      /* ViInt32  */
#define NISWITCH_ATTR_SCAN_DELAY                    IVISWTCH_ATTR_SCAN_DELAY                /* ViReal64 */
#define NISWITCH_ATTR_CONTINUOUS_SCAN               IVISWTCH_ATTR_CONTINUOUS_SCAN           /* ViBoolean */
#define NISWITCH_ATTR_IS_SCANNING                   IVISWTCH_ATTR_IS_SCANNING               /* ViBoolean, read-only */

    /*- niSwitch specific driver attributes --------------------------------*/
#define NISWITCH_ATTR_IS_WAITING_FOR_TRIG             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 4L)    /* ViBoolean, read-only */
#define NISWITCH_ATTR_TRIGGER_MODE                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 5L)    /* ViInt32  */
#define NISWITCH_ATTR_MASTER_SLAVE_TRIGGER_BUS        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 6L)    /* ViInt32  */
#define NISWITCH_ATTR_MASTER_SLAVE_SCAN_ADVANCED_BUS  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 7L)    /* ViInt32  */
#define NISWITCH_ATTR_CABLED_MODULE_TRIGGER_BUS       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 8L)    /* ViInt32  */
#define NISWITCH_ATTR_CABLED_MODULE_SCAN_ADVANCED_BUS (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 9L)    /* ViInt32  */
#define NISWITCH_ATTR_TRIGGER_INPUT_POLARITY          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 10L)   /* ViInt32  */
#define NISWITCH_ATTR_SCAN_ADVANCED_POLARITY          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 11L)   /* ViInt32  */
#define NISWITCH_ATTR_PARSED_SCAN_LIST                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 12L)   /* ViString, read-only */
#define NISWITCH_ATTR_HANDSHAKING_INITIATION          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 13L)   /* ViInt32  */
#define NISWITCH_ATTR_NUMBER_OF_RELAYS                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 14L)   /* ViInt32  */
#define NISWITCH_ATTR_SERIAL_NUMBER                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 15L)   /* ViString, read-only */
#define NISWITCH_ATTR_DIGITAL_FILTER_ENABLE           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 16L)   /* ViBoolean */
#define NISWITCH_ATTR_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 17L)   /* ViBoolean */
#define NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 18L)   /* ViBoolean, channel-based */
#define NISWITCH_ATTR_TEMPERATURE                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 19L)   /* ViReal64  */


/****************************************************************************
 *------------------------ Attribute Value Defines -------------------------*
 ****************************************************************************/
    /* Defined values for NISWITCH_ATTR_SCAN_MODE */
#define NISWITCH_VAL_NONE                           IVISWTCH_VAL_NONE
#define NISWITCH_VAL_BREAK_BEFORE_MAKE              IVISWTCH_VAL_BREAK_BEFORE_MAKE
#define NISWITCH_VAL_BREAK_AFTER_MAKE               IVISWTCH_VAL_BREAK_AFTER_MAKE

    /* Defined values for NISWITCH_ATTR_TRIGGER_INPUT */
#define NISWITCH_VAL_REARCONNECTOR_MODULE_BASE      (IVISWTCH_VAL_TRIGGER_INPUT_SPECIFIC_EXT_BASE + 20)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE     (IVISWTCH_VAL_TRIGGER_INPUT_SPECIFIC_EXT_BASE + 40)

#define NISWITCH_VAL_IMMEDIATE                      IVISWTCH_VAL_IMMEDIATE
#define NISWITCH_VAL_EXTERNAL                       IVISWTCH_VAL_EXTERNAL
#define NISWITCH_VAL_SOFTWARE_TRIG                  IVISWTCH_VAL_SOFTWARE_TRIG
#define NISWITCH_VAL_TTL0                           IVISWTCH_VAL_TTL0
#define NISWITCH_VAL_TTL1                           IVISWTCH_VAL_TTL1
#define NISWITCH_VAL_TTL2                           IVISWTCH_VAL_TTL2
#define NISWITCH_VAL_TTL3                           IVISWTCH_VAL_TTL3
#define NISWITCH_VAL_TTL4                           IVISWTCH_VAL_TTL4
#define NISWITCH_VAL_TTL5                           IVISWTCH_VAL_TTL5
#define NISWITCH_VAL_TTL6                           IVISWTCH_VAL_TTL6
#define NISWITCH_VAL_TTL7                           IVISWTCH_VAL_TTL7
#define NISWITCH_VAL_PXI_STAR                       IVISWTCH_VAL_PXI_STAR
#define NISWITCH_VAL_REARCONNECTOR                  (IVISWTCH_VAL_TRIGGER_INPUT_SPECIFIC_EXT_BASE + 0)
#define NISWITCH_VAL_FRONTCONNECTOR                 (IVISWTCH_VAL_TRIGGER_INPUT_SPECIFIC_EXT_BASE + 1)
#define NISWITCH_VAL_REARCONNECTOR_MODULE1          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 1)
#define NISWITCH_VAL_REARCONNECTOR_MODULE2          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 2)
#define NISWITCH_VAL_REARCONNECTOR_MODULE3          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 3)
#define NISWITCH_VAL_REARCONNECTOR_MODULE4          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 4)
#define NISWITCH_VAL_REARCONNECTOR_MODULE5          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 5)
#define NISWITCH_VAL_REARCONNECTOR_MODULE6          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 6)
#define NISWITCH_VAL_REARCONNECTOR_MODULE7          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 7)
#define NISWITCH_VAL_REARCONNECTOR_MODULE8          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 8)
#define NISWITCH_VAL_REARCONNECTOR_MODULE9          (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 9)
#define NISWITCH_VAL_REARCONNECTOR_MODULE10         (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 10)
#define NISWITCH_VAL_REARCONNECTOR_MODULE11         (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 11)
#define NISWITCH_VAL_REARCONNECTOR_MODULE12         (NISWITCH_VAL_REARCONNECTOR_MODULE_BASE + 12)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE1         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 1)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE2         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 2)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE3         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 3)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE4         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 4)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE5         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 5)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE6         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 6)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE7         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 7)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE8         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 8)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE9         (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 9)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE10        (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 10)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE11        (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 11)
#define NISWITCH_VAL_FRONTCONNECTOR_MODULE12        (NISWITCH_VAL_FRONTCONNECTOR_MODULE_BASE + 12)


/* Defined values for NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT */
/* #define NISWITCH_VAL_NONE                        DEFINED ABOVE */
/* #define NISWITCH_VAL_EXTERNAL                    DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL0                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL1                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL2                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL3                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL4                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL5                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL6                        DEFINED ABOVE */
/* #define NISWITCH_VAL_TTL7                        DEFINED ABOVE */
/* #define NISWITCH_VAL_PXI_STAR                    DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR              DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE1      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE2      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE3      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE4      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE5      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE6      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE7      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE8      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE9      DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE10     DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE11     DEFINED ABOVE */
/* #define NISWITCH_VAL_FRONTCONNECTOR_MODULE12     DEFINED ABOVE */

    /* Defined values for NISWITCH_ATTR_WIRE_MODE */
#define NISWITCH_VAL_1_WIRE                         1
#define NISWITCH_VAL_2_WIRE                         2
#define NISWITCH_VAL_4_WIRE                         4

    /* Defined values for niSwitch_CanConnect path capability parameter */
#define NISWITCH_VAL_PATH_AVAILABLE                 IVISWTCH_VAL_PATH_AVAILABLE
#define NISWITCH_VAL_PATH_EXISTS                    IVISWTCH_VAL_PATH_EXISTS
#define NISWITCH_VAL_PATH_UNSUPPORTED               IVISWTCH_VAL_PATH_UNSUPPORTED
#define NISWITCH_VAL_RSRC_IN_USE                    IVISWTCH_VAL_RSRC_IN_USE
#define NISWITCH_VAL_SOURCE_CONFLICT                IVISWTCH_VAL_SOURCE_CONFLICT
#define NISWITCH_VAL_CHANNEL_NOT_AVAILABLE          IVISWTCH_VAL_CHANNEL_NOT_AVAILABLE

   /* Defined values for NISWITCH_ATTR_SCAN_ADVANCED_POLARITY and NISWITCH_TRIGGER_INPUT_POLARITY */
#define NISWITCH_VAL_RISING_EDGE                    0
#define NISWITCH_VAL_FALLING_EDGE                   1

    /* Defined values for the NISWITCH_ATTR_TRIGGER_MODE attribute */
#define NISWITCH_VAL_SINGLE                         0
#define NISWITCH_VAL_MASTER                         1
#define NISWITCH_VAL_SLAVE                          2

    /* Defined values for the Scan function */
#define NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED   0
#define NISWITCH_VAL_DMM_INITIATED                  NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED
#define NISWITCH_VAL_SWITCH_INITIATED               1

    /* Defined values for the niSwitch_GetRelayPosition's position parameter */
#define NISWITCH_VAL_OPEN                           10
#define NISWITCH_VAL_CLOSED                         11

    /* Defined values for the niSwitch_RelayControl function */
#define NISWITCH_VAL_OPEN_RELAY                     20
#define NISWITCH_VAL_CLOSE_RELAY                    21

/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

    /*- Session Management Functions ---------------------------------------*/
ViStatus _VI_FUNC  niSwitch_init(ViRsrc resourceName,
                                 ViBoolean idQuery,
                                 ViBoolean resetDevice,
                                 ViSession *newVi);
ViStatus _VI_FUNC  niSwitch_InitWithOptions(ViRsrc resourceName,
                                            ViBoolean idQuery,
                                            ViBoolean resetDevice,
                                            ViConstString optionString,
                                            ViSession *newVi);
ViStatus _VI_FUNC  niSwitch_InitWithTopology(ViRsrc resourceName,
                                             ViConstString topology,
                                             ViBoolean simulate,
                                             ViBoolean resetDevice,
                                             ViSession *newVi);

ViStatus _VI_FUNC  niSwitch_close(ViSession vi);

    /*- Locking Functions --------------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_LockSession(ViSession vi,
                                        ViBoolean *callerHasLock);
ViStatus _VI_FUNC  niSwitch_UnlockSession(ViSession vi,
                                          ViBoolean *callerHasLock);

    /*- Switch Routing Functions -------------------------------------------*/
ViStatus _VI_FUNC niSwitch_Connect(ViSession vi,
                                   ViConstString channel1,
                                   ViConstString channel2);
ViStatus _VI_FUNC niSwitch_ConnectMultiple(ViSession vi,
                                           ViConstString connectionList);
ViStatus _VI_FUNC niSwitch_Disconnect(ViSession vi,
                                      ViConstString channel1,
                                      ViConstString channel2);
ViStatus _VI_FUNC niSwitch_DisconnectMultiple(ViSession vi,
                                              ViConstString disconnectionList);
ViStatus _VI_FUNC niSwitch_DisconnectAll(ViSession vi);
ViStatus _VI_FUNC niSwitch_GetPath(ViSession vi,
                                   ViConstString channel1,
                                   ViConstString channel2,
                                   ViInt32 bufferSize,
                                   ViChar pathList[]);
ViStatus _VI_FUNC niSwitch_SetPath(ViSession vi,
                                   ViConstString pathList);
ViStatus _VI_FUNC niSwitch_CanConnect(ViSession vi,
                                      ViConstString channel1,
                                      ViConstString channel2,
                                      ViInt32 *pathCapability);
ViStatus _VI_FUNC niSwitch_IsDebounced(ViSession vi,
                                       ViBoolean* isDebounced);
ViStatus _VI_FUNC niSwitch_WaitForDebounce(ViSession vi,
                                           ViInt32 maxTime);

    /*- Scanning Functions -------------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_Scan(ViSession vi,
                                 ViConstString scanList,
                                 ViInt16 initiation);
ViStatus _VI_FUNC  niSwitch_InitiateScan(ViSession vi);
ViStatus _VI_FUNC  niSwitch_AbortScan(ViSession vi);
ViStatus _VI_FUNC  niSwitch_IsScanning(ViSession vi,
                                       ViBoolean* isScanning);
ViStatus _VI_FUNC  niSwitch_WaitForScanComplete(ViSession vi,
                                                ViInt32 maxTime);
ViStatus _VI_FUNC  niSwitch_SendSoftwareTrigger(ViSession vi);
ViStatus _VI_FUNC  niSwitch_ConfigureScanList(ViSession vi,
                                              ViConstString scanList,
                                              ViInt32 scanMode);
ViStatus _VI_FUNC  niSwitch_ConfigureScanTrigger(ViSession vi,
                                                 ViReal64 scanDelay,
                                                 ViInt32 triggerInput,
                                                 ViInt32 scanAdvancedOutput);
ViStatus _VI_FUNC  niSwitch_SetContinuousScan(ViSession vi,
                                              ViBoolean continuousScan);
ViStatus _VI_FUNC  niSwitch_RouteTriggerInput(ViSession vi,
                                              ViInt32 triggerInputConnector,
                                              ViInt32 triggerInputBusLine,
                                              ViBoolean invert);
ViStatus _VI_FUNC  niSwitch_RouteScanAdvancedOutput(ViSession vi,
                                                    ViInt32 scanAdvancedOutputConnector,
                                                    ViInt32 scanAdvancedOutputBusLine,
                                                    ViBoolean invert);


    /*- Error Functions ----------------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_error_query(ViSession vi,
                                        ViInt32 *errorCode,
                                        ViChar errorMessage[]);
ViStatus _VI_FUNC  niSwitch_GetError(ViSession vi,
                                     ViStatus *errorCode,
                                     ViInt32 bufferSize,
                                     ViChar description[]);
ViStatus _VI_FUNC  niSwitch_ClearError(ViSession vi);
ViStatus _VI_FUNC  niSwitch_error_message(ViSession vi,
                                          ViStatus errorCode,
                                          ViChar errorMessage[256]);

   /*- Channel Info Functions ---------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_GetChannelName(ViSession vi,
                                           ViInt32 index,
                                           ViInt32 bufferSize,
                                           ViChar name[]);

   /*- Relay Operation Functions -------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_GetRelayName(ViSession vi,
                                         ViInt32 index,
                                         ViInt32 bufferSize,
                                         ViChar name[]);
ViStatus _VI_FUNC  niSwitch_GetRelayCount(ViSession vi,
                                          ViConstString relayName,
                                          ViInt32* count);
ViStatus _VI_FUNC  niSwitch_GetRelayPosition(ViSession vi,
                                             ViConstString relayName,
                                             ViInt32* position);
ViStatus _VI_FUNC  niSwitch_RelayControl(ViSession vi,
                                         ViConstString relayNames,
                                         ViInt32 relayAction);

    /*- Interchangeability Checking Functions ------------------------------*/
ViStatus _VI_FUNC  niSwitch_GetNextInterchangeWarning(ViSession vi,
                                                      ViInt32 bufferSize,
                                                      ViChar warnString[]);
ViStatus _VI_FUNC  niSwitch_ResetInterchangeCheck(ViSession vi);
ViStatus _VI_FUNC  niSwitch_ClearInterchangeWarnings(ViSession vi);

    /*- Coercion Functions -------------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_GetNextCoercionRecord(ViSession vi,
                                                  ViInt32 bufferSize,
                                                  ViChar record[]);

    /*- Utility Functions --------------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_Commit(ViSession vi);
ViStatus _VI_FUNC  niSwitch_InvalidateAllAttributes(ViSession vi);
ViStatus _VI_FUNC  niSwitch_ResetWithDefaults(ViSession vi);
ViStatus _VI_FUNC  niSwitch_Disable(ViSession vi);
ViStatus _VI_FUNC  niSwitch_reset(ViSession vi);
ViStatus _VI_FUNC  niSwitch_self_test(ViSession vi,
                                      ViInt16 *selfTestResult,
                                      ViChar selfTestMessage[]);
ViStatus _VI_FUNC  niSwitch_revision_query(ViSession vi,
                                           ViChar instrumentDriverRevision[],
                                           ViChar firmwareRevision[]);

    /*- Set, Get, and Check Attribute Functions ----------------------------*/
ViStatus _VI_FUNC  niSwitch_GetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 *value);
ViStatus _VI_FUNC  niSwitch_GetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 *value);
ViStatus _VI_FUNC  niSwitch_GetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 bufferSize, ViChar value[]);
ViStatus _VI_FUNC  niSwitch_GetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attribute, ViSession *value);
ViStatus _VI_FUNC  niSwitch_GetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean *value);

ViStatus _VI_FUNC  niSwitch_SetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 value);
ViStatus _VI_FUNC  niSwitch_SetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 value);
ViStatus _VI_FUNC  niSwitch_SetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attribute, ViConstString value);
ViStatus _VI_FUNC  niSwitch_SetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value);
ViStatus _VI_FUNC  niSwitch_SetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value);

ViStatus _VI_FUNC  niSwitch_CheckAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 value);
ViStatus _VI_FUNC  niSwitch_CheckAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 value);
ViStatus _VI_FUNC  niSwitch_CheckAttributeViString(ViSession vi, ViConstString channelName, ViAttr attribute, ViConstString value);
ViStatus _VI_FUNC  niSwitch_CheckAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value);
ViStatus _VI_FUNC  niSwitch_CheckAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value);

/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/

#define NISWITCH_ERROR_SESSION_ALREADY_OPEN                          (IVI_SPECIFIC_ERROR_BASE + 1)
#define NISWITCH_ERROR_INVALID_RESOURCE_DESCRIPTOR                   (IVI_SPECIFIC_ERROR_BASE + 2)
#define NISWITCH_ERROR_SCANNING_NOT_SUPPORTED                        (IVI_SPECIFIC_ERROR_BASE + 3)
#define NISWITCH_ERROR_MUST_SPECIFY_MODULE                           (IVI_SPECIFIC_ERROR_BASE + 4)
#define NISWITCH_ERROR_MODULE_FIFO_LENGTH_EXCEEDED                   (IVI_SPECIFIC_ERROR_BASE + 5)
#define NISWITCH_ERROR_HW_COMMUNICATE_TMO                            (IVI_SPECIFIC_ERROR_BASE + 6)
#define NISWITCH_ERROR_TTL_BUS_REQUIRED                              (IVI_SPECIFIC_ERROR_BASE + 7)
#define NISWITCH_ERROR_MODULE_IS_BBM_ONLY                            (IVI_SPECIFIC_ERROR_BASE + 8)
#define NISWITCH_ERROR_1127_TTL1_CONFLICT                            (IVI_SPECIFIC_ERROR_BASE + 9)
#define NISWITCH_ERROR_INVALID_DRIVER_SETUP_STRING                   (IVI_SPECIFIC_ERROR_BASE + 11)
#define NISWITCH_ERROR_TOPOLOGY_NOT_SUPPORTED                        (IVI_SPECIFIC_ERROR_BASE + 12)
#define NISWITCH_ERROR_INVALID_TOPOLOGY                              (IVI_SPECIFIC_ERROR_BASE + 13)
#define NISWITCH_ERROR_HARDWARE_UNEXPECTEDLY_RESET                   (IVI_SPECIFIC_ERROR_BASE + 14)
#define NISWITCH_ERROR_HANDSHAKING_INITIATION_CONFLICT               (IVI_SPECIFIC_ERROR_BASE + 15)
#define NISWITCH_ERROR_LEGACY_DESCRIPTOR_DAQMX_RSC_TYPE              (IVI_SPECIFIC_ERROR_BASE + 16)
#define NISWITCH_ERROR_DAQMX_DESCRIPTOR_LEGACY_RSC_TYPE              (IVI_SPECIFIC_ERROR_BASE + 17)
#define NISWITCH_ERROR_AMBIGUOUS_MODEL_CODE                          (IVI_SPECIFIC_ERROR_BASE + 18)
#define NISWITCH_ERROR_TRIGGER_INPUT_NOT_SUPPORTED                   (IVI_SPECIFIC_ERROR_BASE + 19)
#define NISWITCH_ERROR_INVALID_TERMINALBLOCK_FOR_TOPOLOGY            (IVI_SPECIFIC_ERROR_BASE + 20)
#define NISWITCH_ERROR_CANT_INVERT_WHEN_SOURCE_EQUALS_DEST           (IVI_SPECIFIC_ERROR_BASE + 21)
#define NISWITCH_ERROR_CONFLICTING_TRIGGER_ROUTE_EXISTS              (IVI_SPECIFIC_ERROR_BASE + 22)
#define NISWITCH_ERROR_INVALID_VALUE_FOR_DEVICE                      (IVI_SPECIFIC_ERROR_BASE + 23)
#define NISWITCH_ERROR_TRIGGER_POLARITY_CONFLICT                     (IVI_SPECIFIC_ERROR_BASE + 24)
#define NISWITCH_ERROR_INTERNAL_ERROR                                (IVI_SPECIFIC_ERROR_BASE + 25)
#define NISWITCH_ERROR_RESET_NEEDED_TO_CHANGE_TOPOLOGY               (IVI_SPECIFIC_ERROR_BASE + 26)
#define NISWITCH_ERROR_RESERVATION_ERROR                             (IVI_SPECIFIC_ERROR_BASE + 27)
#define NISWITCH_ERROR_ANALOG_BUS_INVALID                            (IVI_SPECIFIC_ERROR_BASE + 28)
#define NISWITCH_ERROR_POWER_LIMIT_EXCEEDED                          (IVI_SPECIFIC_ERROR_BASE + 29)
#define NISWITCH_ERROR_DEVICE_SELF_TEST_FAILED                       (IVI_SPECIFIC_ERROR_BASE + 30)
#define NISWITCH_ERROR_CARD_DETECTED_DOES_NOT_MATCH_EXPECTED_CARD    (IVI_SPECIFIC_ERROR_BASE + 31)
#define NISWITCH_ERROR_ANALOG_BUS_STATE_INCONSISTENT                 (IVI_SPECIFIC_ERROR_BASE + 32)
#define NISWITCH_ERROR_FIVE_VOLT_DETECT_FAILED                       (IVI_SPECIFIC_ERROR_BASE + 33)
#define NISWITCH_ERROR_SLOT_POWER_LIMIT_EXCEEDED                     (IVI_SPECIFIC_ERROR_BASE + 34)
#define NISWITCH_ERROR_CANNOT_EXCEED_RELAY_DRIVE_LIMIT               (IVI_SPECIFIC_ERROR_BASE + 35)
#define NISWITCH_ERROR_INVALID_CONNECTION_LIST                       (IVI_SPECIFIC_ERROR_BASE + 36)
#define NISWITCH_ERROR_DISCONNECTION_PATH_NOT_SAME_AS_EXISTING_PATH  (IVI_SPECIFIC_ERROR_BASE + 37)
#define NISWITCH_ERROR_INVALID_RELAY_NAME                            (IVI_SPECIFIC_ERROR_BASE + 38)
#define NISWITCH_ERROR_ANALOG_BUS_SHARING_DIFFERENT_WIRE_MODES       (IVI_SPECIFIC_ERROR_BASE + 39)
#define NISWITCH_ERROR_DEVICE_NO_LONGER_SUPPORTED                    (IVI_SPECIFIC_ERROR_BASE + 40)

#define NISWITCH_WARN_PATH_REMAINS                       IVISWTCH_WARN_PATH_REMAINS
#define NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS         IVISWTCH_WARN_IMPLICIT_CONNECTION_EXISTS

#define NISWITCH_ERROR_INVALID_SWITCH_PATH               IVISWTCH_ERROR_INVALID_SWITCH_PATH
#define NISWITCH_ERROR_INVALID_SCAN_LIST                 IVISWTCH_ERROR_INVALID_SCAN_LIST
#define NISWITCH_ERROR_RSRC_IN_USE                       IVISWTCH_ERROR_RSRC_IN_USE
#define NISWITCH_ERROR_EMPTY_SCAN_LIST                   IVISWTCH_ERROR_EMPTY_SCAN_LIST
#define NISWITCH_ERROR_EMPTY_SWITCH_PATH                 IVISWTCH_ERROR_EMPTY_SWITCH_PATH
#define NISWITCH_ERROR_SCAN_IN_PROGRESS                  IVISWTCH_ERROR_SCAN_IN_PROGRESS
#define NISWITCH_ERROR_NO_SCAN_IN_PROGRESS               IVISWTCH_ERROR_NO_SCAN_IN_PROGRESS
#define NISWITCH_ERROR_NO_SUCH_PATH                      IVISWTCH_ERROR_NO_SUCH_PATH
#define NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL          IVISWTCH_ERROR_IS_CONFIGURATION_CHANNEL
#define NISWITCH_ERROR_NOT_A_CONFIGURATION_CHANNEL       IVISWTCH_ERROR_NOT_A_CONFIGURATION_CHANNEL
#define NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES        IVISWTCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES
#define NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS        IVISWTCH_ERROR_EXPLICIT_CONNECTION_EXISTS
#define NISWITCH_ERROR_LEG_MISSING_FIRST_CHANNEL         IVISWTCH_ERROR_LEG_MISSING_FIRST_CHANNEL
#define NISWITCH_ERROR_LEG_MISSING_SECOND_CHANNEL        IVISWTCH_ERROR_LEG_MISSING_SECOND_CHANNEL
#define NISWITCH_ERROR_CHANNEL_DUPLICATED_IN_LEG         IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_LEG
#define NISWITCH_ERROR_CHANNEL_DUPLICATED_IN_PATH        IVISWTCH_ERROR_CHANNEL_DUPLICATED_IN_PATH
#define NISWITCH_ERROR_PATH_NOT_FOUND                    IVISWTCH_ERROR_PATH_NOT_FOUND
#define NISWITCH_ERROR_DISCONTINUOUS_PATH                IVISWTCH_ERROR_DISCONTINUOUS_PATH
#define NISWITCH_ERROR_CANNOT_CONNECT_DIRECTLY           IVISWTCH_ERROR_CANNOT_CONNECT_DIRECTLY
#define NISWITCH_ERROR_CHANNELS_ALREADY_CONNECTED        IVISWTCH_ERROR_CHANNELS_ALREADY_CONNECTED
#define NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF          IVISWTCH_ERROR_CANNOT_CONNECT_TO_ITSELF

#ifdef IVISWTCH_ERROR_MAX_TIME_EXCEEDED
 #define NISWITCH_ERROR_MAX_TIME_EXCEEDED          IVISWTCH_ERROR_MAX_TIME_EXCEEDED
#else
 #define NISWITCH_ERROR_MAX_TIME_EXCEEDED          (IVI_CLASS_ERROR_BASE + 22L)
#endif

#define NISWITCH_ERROR_TRIGGER_NOT_SOFTWARE        IVISWTCH_ERROR_TRIGGER_NOT_SOFTWARE

    /*- Obsolete Instrument Driver Values, Attributes and functions -*/
    /*- These attributes and functions have been deprecated and may not
        be supported in future versions of this driver.
    -*/
#define niSwitch_SwitchSwitch                       niSwitch_SingleSwitchControl
#define NISWITCH_ATTR_QUERY_INSTR_STATUS            NISWITCH_ATTR_QUERY_INSTRUMENT_STATUS
    /*- Driver Information -*/
#define NISWITCH_ATTR_SPECIFIC_PREFIX               IVI_ATTR_SPECIFIC_PREFIX
#define NISWITCH_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION
#define NISWITCH_ATTR_SPECIFIC_DRIVER_MINOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION
    /*- IVI Engine Information -*/
#define NISWITCH_ATTR_ENGINE_MAJOR_VERSION          IVI_ATTR_ENGINE_MAJOR_VERSION
#define NISWITCH_ATTR_ENGINE_MINOR_VERSION          IVI_ATTR_ENGINE_MINOR_VERSION
#define NISWITCH_ATTR_ENGINE_REVISION               IVI_ATTR_ENGINE_REVISION
    /*- Error Info -*/
#define NISWITCH_ATTR_PRIMARY_ERROR                 IVI_ATTR_PRIMARY_ERROR
#define NISWITCH_ATTR_SECONDARY_ERROR               IVI_ATTR_SECONDARY_ERROR
#define NISWITCH_ATTR_ERROR_ELABORATION             IVI_ATTR_ERROR_ELABORATION
    /*- Advanced Session Information -*/
#define NISWITCH_ATTR_IO_SESSION_TYPE               IVI_ATTR_IO_SESSION_TYPE
#define NISWITCH_ATTR_IO_SESSION                    IVI_ATTR_IO_SESSION
    /*- Deprecated Attribute Identifiers for Renamed Attributes -*/
#define NISWITCH_ATTR_NUM_CHANNELS                  NISWITCH_ATTR_CHANNEL_COUNT
#define NISWITCH_ATTR_QUERY_INSTR_STATUS            NISWITCH_ATTR_QUERY_INSTRUMENT_STATUS
#define NISWITCH_ATTR_RESOURCE_DESCRIPTOR           NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR
    /* Version Info */
#define NISWITCH_ATTR_DRIVER_MAJOR_VERSION          IVI_ATTR_DRIVER_MAJOR_VERSION
#define NISWITCH_ATTR_DRIVER_MINOR_VERSION          IVI_ATTR_DRIVER_MINOR_VERSION
#define NISWITCH_ATTR_DRIVER_REVISION               IVI_ATTR_DRIVER_REVISION
    /* Serial number - ViInt32 version */
#define NISWITCH_ATTR_SERIAL_NUMBER_I32             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1L)
    /* Software Trigger */
#define NISWITCH_VAL_SW_TRIG_FUNC                   IVISWTCH_VAL_SOFTWARE_TRIG
    /* Other deprecated values */
#define NISWITCH_VAL_ECL0                           IVISWTCH_VAL_ECL0
#define NISWITCH_VAL_ECL1                           IVISWTCH_VAL_ECL1

#define NISWITCH_ERROR_SCANLIST_NOT_SPECIFIED       (IVI_SPECIFIC_ERROR_BASE + 10)

    /*- Deprecated Send Software Trigger function -*/
ViStatus _VI_FUNC  niSwitch_SendSWTrigger(ViSession vi);

    /*- Deprecated Error Information functions -*/
ViStatus _VI_FUNC  niSwitch_GetErrorInfo(ViSession vi, ViStatus *primaryError, ViStatus *secondaryError, ViChar errorElaboration[256]);
ViStatus _VI_FUNC  niSwitch_ClearErrorInfo(ViSession vi);

    /*- Deprecated Single Switch Control Functions ------------------------------------*/
ViStatus _VI_FUNC  niSwitch_SingleSwitchControl(ViSession vi, ViConstString switchName, ViInt16 switchAction);
ViStatus _VI_FUNC  niSwitch_SingleSwitchQuery(ViSession vi, ViConstString switchName, ViInt16 *switchState);

    /*- Deprecated Calibration Functions ----------------------------------------------*/
ViStatus _VI_FUNC  niSwitch_CalibrationDataWrite(ViSession vi,
                                                 ViConstString channel,
                                                 ViInt32 field,
                                                 ViReal64 calData);
ViStatus _VI_FUNC  niSwitch_CalibrationDataRead(ViSession vi,
                                                ViConstString channel,
                                                ViInt32 field,
                                                ViReal64 *calData,
                                                ViInt32 *year,
                                                ViInt32 *month,
                                                ViInt32 *day);


    /* Deprecated defined values for the niSwitch_SingleSwitchControl and */
    /* niSwitch_SingleSwitchQuery operations */
#define NISWITCH_VAL_SWITCH_OPEN                    0
#define NISWITCH_VAL_SWITCH_CLOSE                   1
#define NISWITCH_VAL_SWITCH_CLOSED                  NISWITCH_VAL_SWITCH_CLOSE

    /* Deprecated defined values for the calibration values */
#define NISWITCH_VAL_CALIBRATION_CJS_AMP            0x00000001
#define NISWITCH_VAL_CALIBRATION_CHANNEL_AMP        0x08000001

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#ifdef __cplusplus
    }
#endif

#endif // ___niswitch_h___
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niswitchTopologies.h sha256=24e41dead8ee691293ca255bae0a4304edcb2227609ff5a6354330f7325bc7a4 bytes=17770 -->
## FILE: imports/include/niswitchTopologies.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niswitchTopologies.h`
- sha256: `24e41dead8ee691293ca255bae0a4304edcb2227609ff5a6354330f7325bc7a4`
- bytes: 17770

````c

/****************************************************************************
 *                       NI-SWITCH Topologies
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 1998-2020.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niswitchTopologies.h
 * Purpose:  Define topologies for use with NI-SWITCH
 *
 ****************************************************************************/

#ifndef ___niswitch_topologies_h___
#define ___niswitch_topologies_h___

#define NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY              "Configured Topology"

#define NISWITCH_TOPOLOGY_1127_1_WIRE_64X1_MUX             "1127/1-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_1127_2_WIRE_32X1_MUX             "1127/2-Wire 32x1 Mux"
#define NISWITCH_TOPOLOGY_1127_2_WIRE_4X8_MATRIX           "1127/2-Wire 4x8 Matrix"
#define NISWITCH_TOPOLOGY_1127_4_WIRE_16X1_MUX             "1127/4-Wire 16x1 Mux"
#define NISWITCH_TOPOLOGY_1127_INDEPENDENT                 "1127/Independent"

#define NISWITCH_TOPOLOGY_1128_1_WIRE_64X1_MUX             "1128/1-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_1128_2_WIRE_32X1_MUX             "1128/2-Wire 32x1 Mux"
#define NISWITCH_TOPOLOGY_1128_2_WIRE_4X8_MATRIX           "1128/2-Wire 4x8 Matrix"
#define NISWITCH_TOPOLOGY_1128_4_WIRE_16X1_MUX             "1128/4-Wire 16x1 Mux"
#define NISWITCH_TOPOLOGY_1128_INDEPENDENT                 "1128/Independent"

#define NISWITCH_TOPOLOGY_1129_2_WIRE_16X16_MATRIX         "1129/2-Wire 16x16 Matrix"
#define NISWITCH_TOPOLOGY_1129_2_WIRE_4X64_MATRIX          "1129/2-Wire 4x64 Matrix"
#define NISWITCH_TOPOLOGY_1129_2_WIRE_8X32_MATRIX          "1129/2-Wire 8x32 Matrix"
#define NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_4X32_MATRIX     "1129/2-Wire Dual 4x32 Matrix"
#define NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_8X16_MATRIX     "1129/2-Wire Dual 8x16 Matrix"
#define NISWITCH_TOPOLOGY_1129_2_WIRE_QUAD_4X16_MATRIX     "1129/2-Wire Quad 4x16 Matrix"

#define NISWITCH_TOPOLOGY_1130_1_WIRE_256X1_MUX            "1130/1-Wire 256x1 Mux"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_4X64_MATRIX          "1130/1-Wire 4x64 Matrix"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_8X32_MATRIX          "1130/1-Wire 8x32 Matrix"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_DUAL_128X1_MUX       "1130/1-Wire Dual 128x1 Mux"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_OCTAL_32X1_MUX       "1130/1-Wire Octal 32x1 Mux"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_QUAD_64X1_MUX        "1130/1-Wire Quad 64x1 Mux"
#define NISWITCH_TOPOLOGY_1130_1_WIRE_SIXTEEN_16X1_MUX     "1130/1-Wire Sixteen 16x1 Mux"
#define NISWITCH_TOPOLOGY_1130_2_WIRE_128X1_MUX            "1130/2-Wire 128x1 Mux"
#define NISWITCH_TOPOLOGY_1130_2_WIRE_4X32_MATRIX          "1130/2-Wire 4x32 Matrix"
#define NISWITCH_TOPOLOGY_1130_2_WIRE_OCTAL_16X1_MUX       "1130/2-Wire Octal 16x1 Mux"
#define NISWITCH_TOPOLOGY_1130_2_WIRE_QUAD_32X1_MUX        "1130/2-Wire Quad 32x1 Mux"
#define NISWITCH_TOPOLOGY_1130_4_WIRE_64X1_MUX             "1130/4-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_1130_4_WIRE_QUAD_16X1_MUX        "1130/4-Wire Quad 16x1 Mux"
#define NISWITCH_TOPOLOGY_1130_INDEPENDENT                 "1130/Independent"

#define NISWITCH_TOPOLOGY_1160_16_SPDT                     "1160/16-SPDT"

#define NISWITCH_TOPOLOGY_1161_8_SPDT                      "1161/8-SPDT"

#define NISWITCH_TOPOLOGY_1163R_OCTAL_4X1_MUX              "1163R/Octal 4x1 Mux"

#define NISWITCH_TOPOLOGY_1166_16_DPDT                     "1166/16-DPDT"
#define NISWITCH_TOPOLOGY_1166_32_SPDT                     "1166/32-SPDT"

#define NISWITCH_TOPOLOGY_1167_INDEPENDENT                 "1167/Independent"

#define NISWITCH_TOPOLOGY_1169_100_SPST                    "1169/100-SPST"
#define NISWITCH_TOPOLOGY_1169_50_DPST                     "1169/50-DPST"

#define NISWITCH_TOPOLOGY_1175_1_WIRE_196X1_MUX            "1175/1-Wire 196x1 Mux"
#define NISWITCH_TOPOLOGY_1175_2_WIRE_95X1_MUX             "1175/2-Wire 95x1 Mux"
#define NISWITCH_TOPOLOGY_1175_2_WIRE_98X1_MUX             "1175/2-Wire 98x1 Mux"

#define NISWITCH_TOPOLOGY_1190_QUAD_4X1_MUX                "1190/Quad 4x1 Mux"

#define NISWITCH_TOPOLOGY_1191_QUAD_4X1_MUX                "1191/Quad 4x1 Mux"

#define NISWITCH_TOPOLOGY_1192_8_SPDT                      "1192/8-SPDT"

#define NISWITCH_TOPOLOGY_1193_16X1_TERMINATED_MUX         "1193/16x1 Terminated Mux"
#define NISWITCH_TOPOLOGY_1193_32X1_MUX                    "1193/32x1 Mux"
#define NISWITCH_TOPOLOGY_1193_DUAL_16X1_MUX               "1193/Dual 16x1 Mux"
#define NISWITCH_TOPOLOGY_1193_DUAL_8X1_TERMINATED_MUX     "1193/Dual 8x1 Terminated Mux"
#define NISWITCH_TOPOLOGY_1193_INDEPENDENT                 "1193/Independent"
#define NISWITCH_TOPOLOGY_1193_QUAD_4X1_TERMINATED_MUX     "1193/Quad 4x1 Terminated Mux"
#define NISWITCH_TOPOLOGY_1193_QUAD_8X1_MUX                "1193/Quad 8x1 Mux"

#define NISWITCH_TOPOLOGY_1194_QUAD_4X1_MUX                "1194/Quad 4x1 Mux"

#define NISWITCH_TOPOLOGY_1195_QUAD_4X1_MUX                "1195/Quad 4x1 Mux"

#define NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_AMPLIFIED_MUX   "2501/1-Wire 48x1 Amplified Mux"
#define NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX             "2501/1-Wire 48x1 Mux"
#define NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_AMPLIFIED_MUX   "2501/2-Wire 24x1 Amplified Mux"
#define NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_MUX             "2501/2-Wire 24x1 Mux"
#define NISWITCH_TOPOLOGY_2501_2_WIRE_4X6_MATRIX           "2501/2-Wire 4x6 Matrix"
#define NISWITCH_TOPOLOGY_2501_2_WIRE_DUAL_12X1_MUX        "2501/2-Wire Dual 12x1 Mux"
#define NISWITCH_TOPOLOGY_2501_2_WIRE_QUAD_6X1_MUX         "2501/2-Wire Quad 6x1 Mux"
#define NISWITCH_TOPOLOGY_2501_4_WIRE_12X1_MUX             "2501/4-Wire 12x1 Mux"

#define NISWITCH_TOPOLOGY_2503_1_WIRE_48X1_MUX             "2503/1-Wire 48x1 Mux"
#define NISWITCH_TOPOLOGY_2503_2_WIRE_24X1_MUX             "2503/2-Wire 24x1 Mux"
#define NISWITCH_TOPOLOGY_2503_2_WIRE_4X6_MATRIX           "2503/2-Wire 4x6 Matrix"
#define NISWITCH_TOPOLOGY_2503_2_WIRE_DUAL_12X1_MUX        "2503/2-Wire Dual 12x1 Mux"
#define NISWITCH_TOPOLOGY_2503_2_WIRE_QUAD_6X1_MUX         "2503/2-Wire Quad 6x1 Mux"
#define NISWITCH_TOPOLOGY_2503_4_WIRE_12X1_MUX             "2503/4-Wire 12x1 Mux"

#define NISWITCH_TOPOLOGY_2510_INDEPENDENT                 "2510/Independent"

#define NISWITCH_TOPOLOGY_2512_INDEPENDENT                 "2512/Independent"

#define NISWITCH_TOPOLOGY_2514_INDEPENDENT                 "2514/Independent"

#define NISWITCH_TOPOLOGY_2515_INDEPENDENT                 "2515/Independent"

#define NISWITCH_TOPOLOGY_2520_80_SPST                     "2520/80-SPST"

#define NISWITCH_TOPOLOGY_2521_40_DPST                     "2521/40-DPST"

#define NISWITCH_TOPOLOGY_2522_53_SPDT                     "2522/53-SPDT"

#define NISWITCH_TOPOLOGY_2523_26_DPDT                     "2523/26-DPDT"

#define NISWITCH_TOPOLOGY_2524_1_WIRE_128X1_MUX            "2524/1-Wire 128x1 Mux"
#define NISWITCH_TOPOLOGY_2524_1_WIRE_DUAL_64X1_MUX        "2524/1-Wire Dual 64x1 Mux"
#define NISWITCH_TOPOLOGY_2524_1_WIRE_OCTAL_16X1_MUX       "2524/1-Wire Octal 16x1 Mux"
#define NISWITCH_TOPOLOGY_2524_1_WIRE_QUAD_32X1_MUX        "2524/1-Wire Quad 32x1 Mux"
#define NISWITCH_TOPOLOGY_2524_1_WIRE_SIXTEEN_8X1_MUX      "2524/1-Wire Sixteen 8x1 Mux"

#define NISWITCH_TOPOLOGY_2525_2_WIRE_64X1_MUX             "2525/2-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_2525_2_WIRE_DUAL_32X1_MUX        "2525/2-Wire Dual 32x1 Mux"
#define NISWITCH_TOPOLOGY_2525_2_WIRE_OCTAL_8X1_MUX        "2525/2-Wire Octal 8x1 Mux"
#define NISWITCH_TOPOLOGY_2525_2_WIRE_QUAD_16X1_MUX        "2525/2-Wire Quad 16x1 Mux"
#define NISWITCH_TOPOLOGY_2525_2_WIRE_SIXTEEN_4X1_MUX      "2525/2-Wire Sixteen 4x1 Mux"

#define NISWITCH_TOPOLOGY_2526_1_WIRE_158X1_MUX            "2526/1-Wire 158x1 Mux"
#define NISWITCH_TOPOLOGY_2526_2_WIRE_79X1_MUX             "2526/2-Wire 79x1 Mux"

#define NISWITCH_TOPOLOGY_2527_1_WIRE_64X1_MUX             "2527/1-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_2527_1_WIRE_DUAL_32X1_MUX        "2527/1-Wire Dual 32x1 Mux"
#define NISWITCH_TOPOLOGY_2527_2_WIRE_32X1_MUX             "2527/2-Wire 32x1 Mux"
#define NISWITCH_TOPOLOGY_2527_2_WIRE_DUAL_16X1_MUX        "2527/2-Wire Dual 16x1 Mux"
#define NISWITCH_TOPOLOGY_2527_4_WIRE_16X1_MUX             "2527/4-Wire 16x1 Mux"
#define NISWITCH_TOPOLOGY_2527_INDEPENDENT                 "2527/Independent"

#define NISWITCH_TOPOLOGY_2529_2_WIRE_4X32_MATRIX          "2529/2-Wire 4x32 Matrix"
#define NISWITCH_TOPOLOGY_2529_2_WIRE_8X16_MATRIX          "2529/2-Wire 8x16 Matrix"
#define NISWITCH_TOPOLOGY_2529_2_WIRE_DUAL_4X16_MATRIX     "2529/2-Wire Dual 4x16 Matrix"

#define NISWITCH_TOPOLOGY_2530_1_WIRE_128X1_MUX            "2530/1-Wire 128x1 Mux"
#define NISWITCH_TOPOLOGY_2530_1_WIRE_4X32_MATRIX          "2530/1-Wire 4x32 Matrix"
#define NISWITCH_TOPOLOGY_2530_1_WIRE_8X16_MATRIX          "2530/1-Wire 8x16 Matrix"
#define NISWITCH_TOPOLOGY_2530_1_WIRE_DUAL_64X1_MUX        "2530/1-Wire Dual 64x1 Mux"
#define NISWITCH_TOPOLOGY_2530_1_WIRE_OCTAL_16X1_MUX       "2530/1-Wire Octal 16x1 Mux"
#define NISWITCH_TOPOLOGY_2530_1_WIRE_QUAD_32X1_MUX        "2530/1-Wire Quad 32x1 Mux"
#define NISWITCH_TOPOLOGY_2530_2_WIRE_4X16_MATRIX          "2530/2-Wire 4x16 Matrix"
#define NISWITCH_TOPOLOGY_2530_2_WIRE_64X1_MUX             "2530/2-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_2530_2_WIRE_DUAL_32X1_MUX        "2530/2-Wire Dual 32x1 Mux"
#define NISWITCH_TOPOLOGY_2530_2_WIRE_QUAD_16X1_MUX        "2530/2-Wire Quad 16x1 Mux"
#define NISWITCH_TOPOLOGY_2530_4_WIRE_32X1_MUX             "2530/4-Wire 32x1 Mux"
#define NISWITCH_TOPOLOGY_2530_4_WIRE_DUAL_16X1_MUX        "2530/4-Wire Dual 16x1 Mux"
#define NISWITCH_TOPOLOGY_2530_INDEPENDENT                 "2530/Independent"

#define NISWITCH_TOPOLOGY_2531_1_WIRE_4X128_MATRIX         "2531/1-Wire 4x128 Matrix"
#define NISWITCH_TOPOLOGY_2531_1_WIRE_8X64_MATRIX          "2531/1-Wire 8x64 Matrix"
#define NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_4X64_MATRIX     "2531/1-Wire Dual 4x64 Matrix"
#define NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_8X32_MATRIX     "2531/1-Wire Dual 8x32 Matrix"
#define NISWITCH_TOPOLOGY_2531_1_WIRE_SIXTEEN_2X16_MATRIX  "2531/1-Wire Sixteen 2x16 Matrix"

#define NISWITCH_TOPOLOGY_2532_1_WIRE_16X32_MATRIX         "2532/1-Wire 16x32 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_4X128_MATRIX         "2532/1-Wire 4x128 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_8X64_MATRIX          "2532/1-Wire 8x64 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_16X16_MATRIX    "2532/1-Wire Dual 16x16 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_4X64_MATRIX     "2532/1-Wire Dual 4x64 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_8X32_MATRIX     "2532/1-Wire Dual 8x32 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_QUAD_4X32_MATRIX     "2532/1-Wire Quad 4x32 Matrix"
#define NISWITCH_TOPOLOGY_2532_1_WIRE_SIXTEEN_2X16_MATRIX  "2532/1-Wire Sixteen 2x16 Matrix"
#define NISWITCH_TOPOLOGY_2532_2_WIRE_16X16_MATRIX         "2532/2-Wire 16x16 Matrix"
#define NISWITCH_TOPOLOGY_2532_2_WIRE_4X64_MATRIX          "2532/2-Wire 4x64 Matrix"
#define NISWITCH_TOPOLOGY_2532_2_WIRE_8X32_MATRIX          "2532/2-Wire 8x32 Matrix"
#define NISWITCH_TOPOLOGY_2532_2_WIRE_DUAL_4X32_MATRIX     "2532/2-Wire Dual 4x32 Matrix"

#define NISWITCH_TOPOLOGY_2533_1_WIRE_4X64_MATRIX          "2533/1-Wire 4x64 Matrix"

#define NISWITCH_TOPOLOGY_2534_1_WIRE_8X32_MATRIX          "2534/1-Wire 8x32 Matrix"

#define NISWITCH_TOPOLOGY_2535_1_WIRE_4X136_MATRIX         "2535/1-Wire 4x136 Matrix"

#define NISWITCH_TOPOLOGY_2536_1_WIRE_8X68_MATRIX          "2536/1-Wire 8x68 Matrix"

#define NISWITCH_TOPOLOGY_2540_1_WIRE_8X9_MATRIX           "2540/1-Wire 8x9 Matrix"

#define NISWITCH_TOPOLOGY_2541_1_WIRE_8X12_MATRIX          "2541/1-Wire 8x12 Matrix"

#define NISWITCH_TOPOLOGY_2542_QUAD_2X1_TERMINATED_MUX     "2542/Quad 2x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2543_DUAL_4X1_TERMINATED_MUX     "2543/Dual 4x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2544_8X1_TERMINATED_MUX          "2544/8x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2545_4X1_TERMINATED_MUX          "2545/4x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2546_DUAL_4X1_MUX                "2546/Dual 4x1 Mux"

#define NISWITCH_TOPOLOGY_2547_8X1_MUX                     "2547/8x1 Mux"

#define NISWITCH_TOPOLOGY_2548_4_SPDT                      "2548/4-SPDT"

#define NISWITCH_TOPOLOGY_2549_TERMINATED_2_SPDT           "2549/Terminated 2-SPDT"

#define NISWITCH_TOPOLOGY_2554_4X1_MUX                     "2554/4x1 Mux"

#define NISWITCH_TOPOLOGY_2555_4X1_TERMINATED_MUX          "2555/4x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2556_DUAL_4X1_MUX                "2556/Dual 4x1 Mux"

#define NISWITCH_TOPOLOGY_2557_8X1_MUX                     "2557/8x1 Mux"

#define NISWITCH_TOPOLOGY_2558_4_SPDT                      "2558/4-SPDT"

#define NISWITCH_TOPOLOGY_2559_TERMINATED_2_SPDT           "2559/Terminated 2-SPDT"

#define NISWITCH_TOPOLOGY_2564_16_SPST                     "2564/16-SPST"
#define NISWITCH_TOPOLOGY_2564_8_DPST                      "2564/8-DPST"

#define NISWITCH_TOPOLOGY_2565_16_SPST                     "2565/16-SPST"

#define NISWITCH_TOPOLOGY_2566_16_SPDT                     "2566/16-SPDT"
#define NISWITCH_TOPOLOGY_2566_8_DPDT                      "2566/8-DPDT"

#define NISWITCH_TOPOLOGY_2567_INDEPENDENT                 "2567/Independent"

#define NISWITCH_TOPOLOGY_2568_15_DPST                     "2568/15-DPST"
#define NISWITCH_TOPOLOGY_2568_31_SPST                     "2568/31-SPST"

#define NISWITCH_TOPOLOGY_2569_100_SPST                    "2569/100-SPST"
#define NISWITCH_TOPOLOGY_2569_50_DPST                     "2569/50-DPST"

#define NISWITCH_TOPOLOGY_2570_20_DPDT                     "2570/20-DPDT"
#define NISWITCH_TOPOLOGY_2570_40_SPDT                     "2570/40-SPDT"

#define NISWITCH_TOPOLOGY_2571_66_SPDT                     "2571/66-SPDT"

#define NISWITCH_TOPOLOGY_2575_1_WIRE_196X1_MUX            "2575/1-Wire 196x1 Mux"
#define NISWITCH_TOPOLOGY_2575_2_WIRE_95X1_MUX             "2575/2-Wire 95x1 Mux"
#define NISWITCH_TOPOLOGY_2575_2_WIRE_98X1_MUX             "2575/2-Wire 98x1 Mux"

#define NISWITCH_TOPOLOGY_2576_2_WIRE_64X1_MUX             "2576/2-Wire 64x1 Mux"
#define NISWITCH_TOPOLOGY_2576_2_WIRE_DUAL_32X1_MUX        "2576/2-Wire Dual 32x1 Mux"
#define NISWITCH_TOPOLOGY_2576_2_WIRE_OCTAL_8X1_MUX        "2576/2-Wire Octal 8x1 Mux"
#define NISWITCH_TOPOLOGY_2576_2_WIRE_QUAD_16X1_MUX        "2576/2-Wire Quad 16x1 Mux"
#define NISWITCH_TOPOLOGY_2576_2_WIRE_SIXTEEN_4X1_MUX      "2576/2-Wire Sixteen 4x1 Mux"
#define NISWITCH_TOPOLOGY_2576_INDEPENDENT                 "2576/Independent"

#define NISWITCH_TOPOLOGY_2584_1_WIRE_12X1_MUX             "2584/1-Wire 12x1 Mux"
#define NISWITCH_TOPOLOGY_2584_1_WIRE_DUAL_6X1_MUX         "2584/1-Wire Dual 6x1 Mux"
#define NISWITCH_TOPOLOGY_2584_2_WIRE_6X1_MUX              "2584/2-Wire 6x1 Mux"
#define NISWITCH_TOPOLOGY_2584_INDEPENDENT                 "2584/Independent"

#define NISWITCH_TOPOLOGY_2585_1_WIRE_10X1_MUX             "2585/1-Wire 10x1 Mux"

#define NISWITCH_TOPOLOGY_2586_10_SPST                     "2586/10-SPST"
#define NISWITCH_TOPOLOGY_2586_5_DPST                      "2586/5-DPST"

#define NISWITCH_TOPOLOGY_2590_4X1_MUX                     "2590/4x1 Mux"

#define NISWITCH_TOPOLOGY_2591_4X1_MUX                     "2591/4x1 Mux"

#define NISWITCH_TOPOLOGY_2593_16X1_MUX                    "2593/16x1 Mux"
#define NISWITCH_TOPOLOGY_2593_8X1_TERMINATED_MUX          "2593/8x1 Terminated Mux"
#define NISWITCH_TOPOLOGY_2593_DUAL_4X1_TERMINATED_MUX     "2593/Dual 4x1 Terminated Mux"
#define NISWITCH_TOPOLOGY_2593_DUAL_8X1_MUX                "2593/Dual 8x1 Mux"
#define NISWITCH_TOPOLOGY_2593_INDEPENDENT                 "2593/Independent"

#define NISWITCH_TOPOLOGY_2594_4X1_MUX                     "2594/4x1 Mux"

#define NISWITCH_TOPOLOGY_2595_4X1_MUX                     "2595/4x1 Mux"

#define NISWITCH_TOPOLOGY_2596_DUAL_6X1_MUX                "2596/Dual 6x1 Mux"

#define NISWITCH_TOPOLOGY_2597_6X1_TERMINATED_MUX          "2597/6x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2598_DUAL_TRANSFER               "2598/Dual Transfer"

#define NISWITCH_TOPOLOGY_2599_2_SPDT                      "2599/2-SPDT"

#define NISWITCH_TOPOLOGY_2720_INDEPENDENT                 "2720/Independent"

#define NISWITCH_TOPOLOGY_2722_INDEPENDENT                 "2722/Independent"

#define NISWITCH_TOPOLOGY_2725_INDEPENDENT                 "2725/Independent"

#define NISWITCH_TOPOLOGY_2727_INDEPENDENT                 "2727/Independent"

#define NISWITCH_TOPOLOGY_2737_2_WIRE_4X64_MATRIX          "2737/2-Wire 4x64 Matrix"

#define NISWITCH_TOPOLOGY_2738_2_WIRE_8X32_MATRIX          "2738/2-Wire 8x32 Matrix"

#define NISWITCH_TOPOLOGY_2739_2_WIRE_16X16_MATRIX         "2739/2-Wire 16x16 Matrix"

#define NISWITCH_TOPOLOGY_2746_QUAD_4X1_MUX                "2746/Quad 4x1 Mux"

#define NISWITCH_TOPOLOGY_2747_DUAL_8X1_MUX                "2747/Dual 8x1 Mux"

#define NISWITCH_TOPOLOGY_2748_16X1_MUX                    "2748/16x1 Mux"

#define NISWITCH_TOPOLOGY_2790_INDEPENDENT                 "2790/Independent"

#define NISWITCH_TOPOLOGY_2796_DUAL_6X1_MUX                "2796/Dual 6x1 Mux"

#define NISWITCH_TOPOLOGY_2797_6X1_TERMINATED_MUX          "2797/6x1 Terminated Mux"

#define NISWITCH_TOPOLOGY_2798_DUAL_TRANSFER               "2798/Dual Transfer"

#define NISWITCH_TOPOLOGY_2799_2_SPDT                      "2799/2-SPDT"
#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nisync.h sha256=f408514a673577ca06bb515deb2261e195e0d4131f9f0eaf45c08a36cca1e276 bytes=68999 -->
## FILE: imports/include/nisync.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nisync.h`
- sha256: `f408514a673577ca06bb515deb2261e195e0d4131f9f0eaf45c08a36cca1e276`
- bytes: 68999

````c
/****************************************************************************
 *                                NI-Sync
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2003-2018.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niSync.h
 * Purpose:  NI-Sync
 *           Instrument Driver Declarations.
 *
 ****************************************************************************/

#ifndef __NISYNC_HEADER
#define __NISYNC_HEADER

#ifndef NIVISA_PXI
#define NIVISA_PXI
#endif

#include <visa.h>

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NISYNC_MAJOR_VERSION                 21 /* Inst. driver major version */
#define NISYNC_MINOR_VERSION                 0 /* Inst. driver minor version */

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/
#define NISYNC_ATTR_BASE                     1150000 /* IVI_SPECIFIC_PUBLIC_ATTR_BASE */

/* Interface attributes */
#define NISYNC_ATTR_INTF_NUM                 (NISYNC_ATTR_BASE + 0L)    /* ViInt32 */
#define NISYNC_ATTR_SERIAL_NUM               (NISYNC_ATTR_BASE + 1L)    /* ViInt32 */

/* Calibration Attributes */
#define NISYNC_ATTR_PFI0_THRESHOLD           (NISYNC_ATTR_BASE + 100L)  /* ViReal64 */
#define NISYNC_ATTR_PFI1_THRESHOLD           (NISYNC_ATTR_BASE + 101L)  /* ViReal64 */
#define NISYNC_ATTR_PFI2_THRESHOLD           (NISYNC_ATTR_BASE + 102L)  /* ViReal64 */
#define NISYNC_ATTR_PFI3_THRESHOLD           (NISYNC_ATTR_BASE + 103L)  /* ViReal64 */
#define NISYNC_ATTR_PFI4_THRESHOLD           (NISYNC_ATTR_BASE + 104L)  /* ViReal64 */
#define NISYNC_ATTR_PFI5_THRESHOLD           (NISYNC_ATTR_BASE + 105L)  /* ViReal64 */
#define NISYNC_ATTR_OSCILLATOR_VOLTAGE       (NISYNC_ATTR_BASE + 106L)  /* ViReal64 */
#define NISYNC_ATTR_CLK10_PHASE_ADJUST       (NISYNC_ATTR_BASE + 107L)  /* ViReal64 */
#define NISYNC_ATTR_DDS_VCXO_VOLTAGE         (NISYNC_ATTR_BASE + 108L)  /* ViReal64 */
#define NISYNC_ATTR_DDS_PHASE_ADJUST         (NISYNC_ATTR_BASE + 109L)  /* ViReal64 */
#define NISYNC_ATTR_PFI0_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 110L)  /* ViBoolean */
#define NISYNC_ATTR_PFI1_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 111L)  /* ViBoolean */
#define NISYNC_ATTR_PFI2_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 112L)  /* ViBoolean */
#define NISYNC_ATTR_PFI3_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 113L)  /* ViBoolean */
#define NISYNC_ATTR_PFI4_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 114L)  /* ViBoolean */
#define NISYNC_ATTR_PFI5_1KOHM_ENABLE        (NISYNC_ATTR_BASE + 115L)  /* ViBoolean */
#define NISYNC_ATTR_PFI0_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 116L)  /* ViBoolean */
#define NISYNC_ATTR_PFI1_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 117L)  /* ViBoolean */
#define NISYNC_ATTR_PFI2_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 118L)  /* ViBoolean */
#define NISYNC_ATTR_PFI3_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 119L)  /* ViBoolean */
#define NISYNC_ATTR_PFI4_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 120L)  /* ViBoolean */
#define NISYNC_ATTR_PFI5_10KOHM_ENABLE       (NISYNC_ATTR_BASE + 121L)  /* ViBoolean */

/* Synchronization Clock Attributes */
#define NISYNC_ATTR_FRONT_SYNC_CLK_SRC       (NISYNC_ATTR_BASE + 200L)  /* ViString */
#define NISYNC_ATTR_REAR_SYNC_CLK_SRC        (NISYNC_ATTR_BASE + 201L)  /* ViString */
#define NISYNC_ATTR_SYNC_CLK_DIV1            (NISYNC_ATTR_BASE + 202L)  /* ViInt32 */
#define NISYNC_ATTR_SYNC_CLK_DIV2            (NISYNC_ATTR_BASE + 203L)  /* ViInt32 */
#define NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM (NISYNC_ATTR_BASE + 204L)  /* ViString */
#define NISYNC_ATTR_SYNC_CLK_PFI0_FREQ       (NISYNC_ATTR_BASE + 205L)  /* ViReal64 */
#define NISYNC_ATTR_SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG  (NISYNC_ATTR_BASE + 206L)     /* ViBoolean */
#define NISYNC_ATTR_SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG (NISYNC_ATTR_BASE + 207L)     /* ViBoolean */
#define NISYNC_ATTR_SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG   (NISYNC_ATTR_BASE + 208L)  /* ViBoolean */

/* Trigger State Attributes */
#define NISYNC_ATTR_TERMINAL_STATE_PXISTAR               (NISYNC_ATTR_BASE + 300L)  /* ViInt32 */
#define NISYNC_ATTR_TERMINAL_STATE_PXITRIG               (NISYNC_ATTR_BASE + 301L)  /* ViInt32 */
#define NISYNC_ATTR_TERMINAL_STATE_PFI                   (NISYNC_ATTR_BASE + 302L)  /* ViInt32 */
#define NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARC            (NISYNC_ATTR_BASE + 303L)  /* ViInt32 */
#define NISYNC_ATTR_TERMINAL_STATE_PFILVDS               (NISYNC_ATTR_BASE + 304L)  /* ViInt32 */
#define NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARCPERIPHERAL  (NISYNC_ATTR_BASE + 305L)  /* ViBoolean */
#define NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARBPERIPHERAL  (NISYNC_ATTR_BASE + 306L)  /* ViBoolean */
#define NISYNC_ATTR_TERMINAL_STATE_PXISTARPERIPHERAL     (NISYNC_ATTR_BASE + 307L)  /* ViBoolean */

/* DDS Attributes */
#define NISYNC_ATTR_DDS_FREQ                 (NISYNC_ATTR_BASE + 400L)  /* ViReal64 */
#define NISYNC_ATTR_DDS_UPDATE_SOURCE        (NISYNC_ATTR_BASE + 401L)  /* ViString */
#define NISYNC_ATTR_DDS_INITIAL_DELAY        (NISYNC_ATTR_BASE + 402L)  /* ViReal64 */

/* Clk Attributes */
#define NISYNC_ATTR_CLKIN_PLL_FREQ            (NISYNC_ATTR_BASE + 500L)  /* ViReal64 */
#define NISYNC_ATTR_CLKIN_USE_PLL             (NISYNC_ATTR_BASE + 501L)  /* ViBoolean */
#define NISYNC_ATTR_CLKIN_PLL_LOCKED          (NISYNC_ATTR_BASE + 502L)  /* ViBoolean */
#define NISYNC_ATTR_CLKOUT_GAIN_ENABLE        (NISYNC_ATTR_BASE + 503L)  /* ViBoolean */
#define NISYNC_ATTR_PXICLK10_PRESENT          (NISYNC_ATTR_BASE + 504L)  /* ViBoolean */
#define NISYNC_ATTR_CLKIN_ATTENUATION_DISABLE (NISYNC_ATTR_BASE + 505L)  /* ViBoolean */

/* User LED Attributes */
#define NISYNC_ATTR_USER_LED_STATE           (NISYNC_ATTR_BASE + 600L)  /* ViBoolean */

/* 1588 Attributes */
#define NISYNC_ATTR_1588_IP_ADDRESS                  (NISYNC_ATTR_BASE + 700L)  /* ViString */
#define NISYNC_ATTR_1588_CLOCK_STATE                 (NISYNC_ATTR_BASE + 712L)  /* ViInt32 */
#define NISYNC_ATTR_1588_CLOCK_ID                    (NISYNC_ATTR_BASE + 729L)  /* ViString */
#define NISYNC_ATTR_1588_CLOCK_CLASS                 (NISYNC_ATTR_BASE + 730L)  /* ViInt32 */
#define NISYNC_ATTR_1588_CLOCK_ACCURACY              (NISYNC_ATTR_BASE + 731L)  /* ViInt32 */
#define NISYNC_ATTR_1588_PRIORITY1                   (NISYNC_ATTR_BASE + 732L)  /* ViInt32 */
#define NISYNC_ATTR_1588_PRIORITY2                   (NISYNC_ATTR_BASE + 733L)  /* ViInt32 */
#define NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ID        (NISYNC_ATTR_BASE + 734L)  /* ViString */
#define NISYNC_ATTR_1588_GRANDMASTER_CLOCK_CLASS     (NISYNC_ATTR_BASE + 735L)  /* ViInt32 */
#define NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ACCURACY  (NISYNC_ATTR_BASE + 736L)  /* ViInt32 */
#define NISYNC_ATTR_1588_GRANDMASTER_PRIORITY1       (NISYNC_ATTR_BASE + 737L)  /* ViInt32 */
#define NISYNC_ATTR_1588_GRANDMASTER_PRIORITY2       (NISYNC_ATTR_BASE + 738L)  /* ViInt32 */
#define NISYNC_ATTR_1588_STEPS_TO_GRANDMASTER        (NISYNC_ATTR_BASE + 716L)  /* ViInt32 */
#define NISYNC_ATTR_1588_LOG_SYNC_INTERVAL           (NISYNC_ATTR_BASE + 739L)  /* ViInt32 */
#define NISYNC_ATTR_1588_MEAN_PATH_DELAY             (NISYNC_ATTR_BASE + 740L)  /* ViReal64 */
#define NISYNC_ATTR_1588_GRANDMASTER_IP_ADDRESS      (NISYNC_ATTR_BASE + 741L)  /* ViString */
#define NISYNC_ATTR_1588_BMCA_MODE                   (NISYNC_ATTR_BASE + 742L)  /* ViInt32 */
#define NISYNC_ATTR_1588_INTERFACE_NAME              (NISYNC_ATTR_BASE + 743L)  /* ViString */

#define NISYNC_ATTR_1588_TIMESTAMP_BUF_SIZE          (NISYNC_ATTR_BASE + 718L)  /* ViInt32 */
#define NISYNC_ATTR_1588_AVAIL_TIMESTAMPS            (NISYNC_ATTR_BASE + 719L)  /* ViInt32 */
#define NISYNC_ATTR_1588_CLK_RESOLUTION              (NISYNC_ATTR_BASE + 720L)  /* ViInt32 */
/* (NISYNC_ATTR_BASE + 770) */

/* Time Reference Attributes */
#define NISYNC_ATTR_TIMEREF_PRESENT               (NISYNC_ATTR_BASE + 800L)  /* ViBoolean */
#define NISYNC_ATTR_TIMEREF_CURRENT               (NISYNC_ATTR_BASE + 801L)  /* ViInt32 */
#define NISYNC_ATTR_TIMEREF_OFFSET                (NISYNC_ATTR_BASE + 802L)  /* ViReal64 */
#define NISYNC_ATTR_TIMEREF_OFFSET_NS             (NISYNC_ATTR_BASE + 808L)  /* ViReal64 */
#define NISYNC_ATTR_TIMEREF_CORRECTION            (NISYNC_ATTR_BASE + 804L)  /* ViReal64 */
#define NISYNC_ATTR_TIMEREF_UTC_OFFSET            (NISYNC_ATTR_BASE + 805L)  /* ViInt32 */
#define NISYNC_ATTR_TIMEREF_UTC_OFFSET_VALID      (NISYNC_ATTR_BASE + 806L)  /* ViBoolean */
#define NISYNC_ATTR_TIMEREF_LAST_SYNC_ID          (NISYNC_ATTR_BASE + 807L)  /* ViInt32 */
#define NISYNC_ATTR_TIMEREF_SELECTED_TYPE         (NISYNC_ATTR_BASE + 809L)  /* ViString */
#define NISYNC_ATTR_TIMEREF_TYPE                  (NISYNC_ATTR_BASE + 810L)  /* ViString */
#define NISYNC_ATTR_TIMEREF_SELECTED_NAME         (NISYNC_ATTR_BASE + 811L)  /* ViString */
#define NISYNC_ATTR_TIMEREF_ENABLED               (NISYNC_ATTR_BASE + 812L)  /* ViBoolean */
#define NISYNC_ATTR_TIMEREF_IS_SELECTED           (NISYNC_ATTR_BASE + 813L)  /* ViBoolean */

/* GPS Attributes */
#define NISYNC_ATTR_GPS_ANTENNA_CONNECTED    (NISYNC_ATTR_BASE + 900L)  /* ViBoolean */
#define NISYNC_ATTR_GPS_RECALCULATE_POSITION (NISYNC_ATTR_BASE + 901L)  /* ViBoolean */
#define NISYNC_ATTR_GPS_SATELLITES_AVAILABLE (NISYNC_ATTR_BASE + 902L)  /* ViInt32 */
#define NISYNC_ATTR_GPS_SELF_SURVEY          (NISYNC_ATTR_BASE + 903L)  /* ViInt32 */
#define NISYNC_ATTR_GPS_MOBILE_MODE          (NISYNC_ATTR_BASE + 904L)  /* ViBoolean */
#define NISYNC_ATTR_GPS_STATUS               (NISYNC_ATTR_BASE + 905L)  /* ViInt32 */

/* Deprecated Attributes - Do not use */
#define NISYNC_ATTR_TIMEREF_CLK_ADJ_OFFSET   (NISYNC_ATTR_BASE + 803L)
#define NISYNC_ATTR_GPS_UTC_OFFSET           (NISYNC_ATTR_BASE + 906L)
#define NISYNC_ATTR_IRIG_TAI_OFFSET          (NISYNC_ATTR_BASE + 1000L)

/* 8021as Attributes */
#define NISYNC_ATTR_8021AS_PORT_STATE                  (NISYNC_ATTR_BASE + 1100L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_CLOCK_ID                    (NISYNC_ATTR_BASE + 1101L)  /* ViString */
#define NISYNC_ATTR_8021AS_CLOCK_CLASS                 (NISYNC_ATTR_BASE + 1102L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_CLOCK_ACCURACY              (NISYNC_ATTR_BASE + 1103L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_PRIORITY1                   (NISYNC_ATTR_BASE + 1104L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_PRIORITY2                   (NISYNC_ATTR_BASE + 1105L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ID        (NISYNC_ATTR_BASE + 1106L)  /* ViString */
#define NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_CLASS     (NISYNC_ATTR_BASE + 1107L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ACCURACY  (NISYNC_ATTR_BASE + 1108L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY1       (NISYNC_ATTR_BASE + 1109L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY2       (NISYNC_ATTR_BASE + 1110L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_LOG_SYNC_INTERVAL           (NISYNC_ATTR_BASE + 1111L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_LOG_ANNOUNCE_INTERVAL       (NISYNC_ATTR_BASE + 1112L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_INTERFACE_NAME              (NISYNC_ATTR_BASE + 1113L)  /* ViString */
#define NISYNC_ATTR_8021AS_NEIGHBOR_PROP_DELAY_THRESH  (NISYNC_ATTR_BASE + 1114L)  /* ViInt32 */
#define NISYNC_ATTR_8021AS_AS_CAPABLE                  (NISYNC_ATTR_BASE + 1115L)  /* ViBoolean */

/* NISYNC_ATTR_BASE + 1300L to NISYNC_ATTR_BASE + 1399L is reserved for internal use */

/****************************************************************************
 *------------------------ Attribute Value Defines -------------------------*
 ****************************************************************************/

/* Trigger Terminals Selectors */
#define NISYNC_VAL_PXITRIG0               "PXI_Trig0"
#define NISYNC_VAL_PXITRIG1               "PXI_Trig1"
#define NISYNC_VAL_PXITRIG2               "PXI_Trig2"
#define NISYNC_VAL_PXITRIG3               "PXI_Trig3"
#define NISYNC_VAL_PXITRIG4               "PXI_Trig4"
#define NISYNC_VAL_PXITRIG5               "PXI_Trig5"
#define NISYNC_VAL_PXITRIG6               "PXI_Trig6"
#define NISYNC_VAL_PXITRIG7               "PXI_Trig7"
#define NISYNC_VAL_PXISTAR0               "PXI_Star0"
#define NISYNC_VAL_PXISTAR1               "PXI_Star1"
#define NISYNC_VAL_PXISTAR2               "PXI_Star2"
#define NISYNC_VAL_PXISTAR3               "PXI_Star3"
#define NISYNC_VAL_PXISTAR4               "PXI_Star4"
#define NISYNC_VAL_PXISTAR5               "PXI_Star5"
#define NISYNC_VAL_PXISTAR6               "PXI_Star6"
#define NISYNC_VAL_PXISTAR7               "PXI_Star7"
#define NISYNC_VAL_PXISTAR8               "PXI_Star8"
#define NISYNC_VAL_PXISTAR9               "PXI_Star9"
#define NISYNC_VAL_PXISTAR10              "PXI_Star10"
#define NISYNC_VAL_PXISTAR11              "PXI_Star11"
#define NISYNC_VAL_PXISTAR12              "PXI_Star12"

#define NISYNC_VAL_PXISTAR13              "PXI_Star13"
#define NISYNC_VAL_PXISTAR14              "PXI_Star14"
#define NISYNC_VAL_PXISTAR15              "PXI_Star15"
#define NISYNC_VAL_PXISTAR16              "PXI_Star16"
#define NISYNC_VAL_PXISTAR                "PXI_Star"

#define NISYNC_VAL_PXIEDSTARA0            "PXIe_DStarA0"
#define NISYNC_VAL_PXIEDSTARA1            "PXIe_DStarA1"
#define NISYNC_VAL_PXIEDSTARA2            "PXIe_DStarA2"
#define NISYNC_VAL_PXIEDSTARA3            "PXIe_DStarA3"
#define NISYNC_VAL_PXIEDSTARA4            "PXIe_DStarA4"
#define NISYNC_VAL_PXIEDSTARA5            "PXIe_DStarA5"
#define NISYNC_VAL_PXIEDSTARA6            "PXIe_DStarA6"
#define NISYNC_VAL_PXIEDSTARA7            "PXIe_DStarA7"
#define NISYNC_VAL_PXIEDSTARA8            "PXIe_DStarA8"
#define NISYNC_VAL_PXIEDSTARA9            "PXIe_DStarA9"
#define NISYNC_VAL_PXIEDSTARA10           "PXIe_DStarA10"
#define NISYNC_VAL_PXIEDSTARA11           "PXIe_DStarA11"
#define NISYNC_VAL_PXIEDSTARA12           "PXIe_DStarA12"
#define NISYNC_VAL_PXIEDSTARA13           "PXIe_DStarA13"
#define NISYNC_VAL_PXIEDSTARA14           "PXIe_DStarA14"
#define NISYNC_VAL_PXIEDSTARA15           "PXIe_DStarA15"
#define NISYNC_VAL_PXIEDSTARA16           "PXIe_DStarA16"
#define NISYNC_VAL_PXIEDSTARA             "PXIe_DStarA"

#define NISYNC_VAL_PXIEDSTARB0            "PXIe_DStarB0"
#define NISYNC_VAL_PXIEDSTARB1            "PXIe_DStarB1"
#define NISYNC_VAL_PXIEDSTARB2            "PXIe_DStarB2"
#define NISYNC_VAL_PXIEDSTARB3            "PXIe_DStarB3"
#define NISYNC_VAL_PXIEDSTARB4            "PXIe_DStarB4"
#define NISYNC_VAL_PXIEDSTARB5            "PXIe_DStarB5"
#define NISYNC_VAL_PXIEDSTARB6            "PXIe_DStarB6"
#define NISYNC_VAL_PXIEDSTARB7            "PXIe_DStarB7"
#define NISYNC_VAL_PXIEDSTARB8            "PXIe_DStarB8"
#define NISYNC_VAL_PXIEDSTARB9            "PXIe_DStarB9"
#define NISYNC_VAL_PXIEDSTARB10           "PXIe_DStarB10"
#define NISYNC_VAL_PXIEDSTARB11           "PXIe_DStarB11"
#define NISYNC_VAL_PXIEDSTARB12           "PXIe_DStarB12"
#define NISYNC_VAL_PXIEDSTARB13           "PXIe_DStarB13"
#define NISYNC_VAL_PXIEDSTARB14           "PXIe_DStarB14"
#define NISYNC_VAL_PXIEDSTARB15           "PXIe_DStarB15"
#define NISYNC_VAL_PXIEDSTARB16           "PXIe_DStarB16"
#define NISYNC_VAL_PXIEDSTARB             "PXIe_DStarB"

#define NISYNC_VAL_PXIEDSTARC0            "PXIe_DStarC0"
#define NISYNC_VAL_PXIEDSTARC1            "PXIe_DStarC1"
#define NISYNC_VAL_PXIEDSTARC2            "PXIe_DStarC2"
#define NISYNC_VAL_PXIEDSTARC3            "PXIe_DStarC3"
#define NISYNC_VAL_PXIEDSTARC4            "PXIe_DStarC4"
#define NISYNC_VAL_PXIEDSTARC5            "PXIe_DStarC5"
#define NISYNC_VAL_PXIEDSTARC6            "PXIe_DStarC6"
#define NISYNC_VAL_PXIEDSTARC7            "PXIe_DStarC7"
#define NISYNC_VAL_PXIEDSTARC8            "PXIe_DStarC8"
#define NISYNC_VAL_PXIEDSTARC9            "PXIe_DStarC9"
#define NISYNC_VAL_PXIEDSTARC10           "PXIe_DStarC10"
#define NISYNC_VAL_PXIEDSTARC11           "PXIe_DStarC11"
#define NISYNC_VAL_PXIEDSTARC12           "PXIe_DStarC12"
#define NISYNC_VAL_PXIEDSTARC13           "PXIe_DStarC13"
#define NISYNC_VAL_PXIEDSTARC14           "PXIe_DStarC14"
#define NISYNC_VAL_PXIEDSTARC15           "PXIe_DStarC15"
#define NISYNC_VAL_PXIEDSTARC16           "PXIe_DStarC16"
#define NISYNC_VAL_PXIEDSTARC             "PXIe_DStarC"

#define NISYNC_VAL_PFILVDS0               "PFI_LVDS0"
#define NISYNC_VAL_PFILVDS1               "PFI_LVDS1"
#define NISYNC_VAL_PFILVDS2               "PFI_LVDS2"

#define NISYNC_VAL_PFI0                   "PFI0"
#define NISYNC_VAL_PFI1                   "PFI1"
#define NISYNC_VAL_PFI2                   "PFI2"
#define NISYNC_VAL_PFI3                   "PFI3"
#define NISYNC_VAL_PFI4                   "PFI4"
#define NISYNC_VAL_PFI5                   "PFI5"
#define NISYNC_VAL_GND                    "Ground"
#define NISYNC_VAL_SYNC_CLK_FULLSPEED     "SyncClkFullSpeed"
#define NISYNC_VAL_SYNC_CLK_DIV1          "SyncClkDivided1"
#define NISYNC_VAL_SYNC_CLK_DIV2          "SyncClkDivided2"
/* Trigger Terminal Synchronization Clock Selectors */
#define NISYNC_VAL_SYNC_CLK_ASYNC         "SyncClkAsync"
/* #define NISYNC_VAL_SYNC_CLK_FULLSPEED  DEFINED ABOVE */
/* #define NISYNC_VAL_SYNC_CLK_DIV1       DEFINED ABOVE */
/* #define NISYNC_VAL_SYNC_CLK_DIV2       DEFINED ABOVE */

/* Software Trigger Terminal Selectors */
#define NISYNC_VAL_SWTRIG_GLOBAL          "GlobalSoftwareTrigger"

/* Clock Terminal Selectors */
#define NISYNC_VAL_CLK10                  "PXI_Clk10"
#define NISYNC_VAL_CLK10_IN               "PXI_Clk10_In"
#define NISYNC_VAL_CLKIN                  "ClkIn"
#define NISYNC_VAL_CLKOUT                 "ClkOut"
#define NISYNC_VAL_OSCILLATOR             "Oscillator"
#define NISYNC_VAL_DDS                    "DDS"
#define NISYNC_VAL_CLK100                 "PXIe_Clk100"

/* "All Connected" Terminal Selector */
#define NISYNC_VAL_ALL_CONNECTED          "AllConnected"

/* Synchronization Clock Source Selectors */
/* #define NISYNC_VAL_PFI0                DEFINED ABOVE */
/* #define NISYNC_VAL_CLK10               DEFINED ABOVE */
/* #define NISYNC_VAL_DDS                 DEFINED ABOVE */

/* Trigger Terminal Connection Mode Definitions (invert, updateEdge, etc.) */
#define NISYNC_VAL_DONT_INVERT            (0)
#define NISYNC_VAL_INVERT                 (1)
#define NISYNC_VAL_UPDATE_EDGE_RISING     (0)
#define NISYNC_VAL_UPDATE_EDGE_FALLING    (1)

/* DDS Update Signal Source Selectors */
#define NISYNC_VAL_DDS_UPDATE_IMMEDIATE   "DDS_UpdateImmediate"
/* #define NISYNC_VAL_PXITRIG0            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG1            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG2            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG3            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG4            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG5            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG6            DEFINED ABOVE */
/* #define NISYNC_VAL_PXITRIG7            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR0            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR1            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR2            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR3            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR4            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR5            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR6            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR7            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR8            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR9            DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR10           DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR11           DEFINED ABOVE */
/* #define NISYNC_VAL_PXISTAR12           DEFINED ABOVE */
/* #define NISYNC_VAL_PFI0                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI1                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI2                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI3                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI4                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI5                DEFINED ABOVE */

/* PCI-1588 Terminal Selectors */
/* #define NISYNC_VAL_PFI0                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI1                DEFINED ABOVE */
/* #define NISYNC_VAL_PFI2                DEFINED ABOVE */
#define NISYNC_VAL_RTSI0                  "RTSI0"
#define NISYNC_VAL_RTSI1                  "RTSI1"
#define NISYNC_VAL_RTSI2                  "RTSI2"
#define NISYNC_VAL_RTSI3                  "RTSI3"
#define NISYNC_VAL_RTSI4                  "RTSI4"
#define NISYNC_VAL_RTSI5                  "RTSI5"
#define NISYNC_VAL_RTSI6                  "RTSI6"
#define NISYNC_VAL_RTSI7                  "RTSI7"
#define NISYNC_VAL_BOARD_CLK              "BoardClk"

/* Initial Time Source Definitions */
#define NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK  (0)
#define NISYNC_VAL_INIT_TIME_SRC_MANUAL      (1)

/* Level Definitions (output level) */
#define NISYNC_VAL_LEVEL_LOW             (0)
#define NISYNC_VAL_LEVEL_HIGH            (1)

/* Edge Definitions (activeEdge, detectedEdge ) */
#define NISYNC_VAL_EDGE_RISING              (0)
#define NISYNC_VAL_EDGE_FALLING             (1)
#define NISYNC_VAL_EDGE_ANY                 (2)

/* 1588 Clock State Definitions */
#define NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED   (-1)
#define NISYNC_VAL_1588_CLK_STATE_INIT          (0)
#define NISYNC_VAL_1588_CLK_STATE_FAULT         (1)
#define NISYNC_VAL_1588_CLK_STATE_DISABLE       (2)
#define NISYNC_VAL_1588_CLK_STATE_LISTENING     (3)
#define NISYNC_VAL_1588_CLK_STATE_PREMASTER     (4)
#define NISYNC_VAL_1588_CLK_STATE_MASTER        (5)
#define NISYNC_VAL_1588_CLK_STATE_PASSIVE       (6)
#define NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED  (7)
#define NISYNC_VAL_1588_CLK_STATE_SLAVE         (8)
#define NISYNC_VAL_1588_CLK_STATE_STOPPED       (9)

/* Sync Interval Definitions */
#define NISYNC_VAL_SYNC_INTERVAL_125_MSEC (-3)
#define NISYNC_VAL_SYNC_INTERVAL_250_MSEC (-2)
#define NISYNC_VAL_SYNC_INTERVAL_HALF_SEC (-1)
#define NISYNC_VAL_SYNC_INTERVAL_ONE_SEC  (0)
#define NISYNC_VAL_SYNC_INTERVAL_TWO_SEC  (1)

/* 1588 Clock Accuracy Definitions */
#define NISYNC_VAL_1588_CLK_ACCURACY_UNKNOWN              (0)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_NSEC       (1)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_NSEC      (2)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_NSEC      (3)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_USEC        (4)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_NSEC     (5)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_USEC       (6)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_USEC       (7)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_USEC      (8)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_USEC      (9)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_MSEC       (10)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_2500_USEC    (11)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_MSEC      (12)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_25_MSEC      (13)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_100_MSEC     (14)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_250_MSEC     (15)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_SEC        (16)
#define NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_10_SEC       (17)
#define NISYNC_VAL_1588_CLK_ACCURACY_GREATER_THAN_10_SEC (18)

/* 8021AS Clock Accuracy Definitions */
#define NISYNC_VAL_8021AS_CLK_ACCURACY_UNKNOWN              (254)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_NSEC       (32)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_NSEC      (33)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_NSEC      (34)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_USEC        (35)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_NSEC     (36)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_USEC       (37)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_USEC       (38)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_USEC      (39)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_USEC      (40)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_MSEC        (41)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_2500_USEC     (42)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_MSEC       (43)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_25_MSEC       (44)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_100_MSEC      (45)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_250_MSEC      (46)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_1_SEC         (47)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_WITHIN_10_SEC        (48)
#define NISYNC_VAL_8021AS_CLK_ACCURACY_GREATER_THAN_10_SEC  (49)

/* IRIG Type Definitions */
#define NISYNC_VAL_IRIG_TYPE_IRIGB_DC   (0)
#define NISYNC_VAL_IRIG_TYPE_IRIGB_AM   (1)

/* GPS Status Definitions */
#define NISYNC_VAL_GPS_UNINITIALIZED            (0)
#define NISYNC_VAL_GPS_ANTENNA_ERROR            (1)
#define NISYNC_VAL_GPS_NO_USEABLE_SATELLITE     (2)
#define NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE    (3)
#define NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES   (4)
#define NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES (5)
#define NISYNC_VAL_GPS_NO_GPS_TIME              (6)
#define NISYNC_VAL_GPS_PDOP_TOO_HIGH            (7)
#define NISYNC_VAL_GPS_UNUSABLE_SATELLITE       (8)
#define NISYNC_VAL_GPS_FIX_REJECTED             (9)
#define NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE     (10)
#define NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE (11)

/* Time Reference Definitions */
#define NISYNC_VAL_TIMEREF_GPS                 (0)
#define NISYNC_VAL_TIMEREF_IRIG                (1)
#define NISYNC_VAL_TIMEREF_PPS                 (2)
#define NISYNC_VAL_TIMEREF_1588_ORDINARY_CLOCK (3)
#define NISYNC_VAL_TIMEREF_FREERUNNING         (4)
#define NISYNC_VAL_TIMEREF_8021AS              (5)

/* BMCA Mode Definitions */
#define NISYNC_VAL_BMCA_MODE_SLAVE_ONLY        (0)
#define NISYNC_VAL_BMCA_MODE_MASTER_SLAVE      (1)
/* (2) is reserved for internal use */

/* Port State Definitions */
#define NISYNC_VAL_8021AS_PORT_STATE_DISABLED  (3)
#define NISYNC_VAL_8021AS_PORT_STATE_MASTER    (6)
#define NISYNC_VAL_8021AS_PORT_STATE_PASSIVE   (7)
#define NISYNC_VAL_8021AS_PORT_STATE_SLAVE     (9)

/*- Defined values for action in niSync_CloseExtCal()  --------*/
#define NISYNC_VAL_EXT_CAL_ABORT          0L
#define NISYNC_VAL_EXT_CAL_COMMIT         1L

/*- Deprecated value definitions ---------------------------*/
#define NISYNC_VAL_GPS_UNUSEABLE_SATELLITE (8)

/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

/*- Init and Close Functions -------------------------------------------*/
ViStatus _VI_FUNC niSync_init(ViRsrc resourceName,
                              ViBoolean IDQuery,
                              ViBoolean resetDevice,
                              ViSession *vi);
ViStatus _VI_FUNC niSync_close(ViSession vi);

/*- Time Reference Functions -------------------------------------------*/
ViStatus _VI_FUNC niSync_GetTimeReferenceNames(ViSession vi,
                                               ViUInt32 bufferSize,
                                               ViChar timeReferenceNames[]);

/*- Error Functions ----------------------------------------------------*/
ViStatus _VI_FUNC niSync_error_message(ViSession vi,
                                       ViStatus errorCode,
                                       ViChar errorMessage[]);

/*- Utility Functions --------------------------------------------------*/
ViStatus _VI_FUNC niSync_reset(ViSession vi);
ViStatus _VI_FUNC niSync_PersistConfig(ViSession vi);
ViStatus _VI_FUNC niSync_self_test(ViSession vi,
                                   ViInt16* selfTestResult,
                                   ViChar selfTestMessage[]);
ViStatus _VI_FUNC niSync_revision_query(ViSession vi,
                                        ViChar instrumentDriverRevision[],
                                        ViChar firmwareRevision[]);

/*- FPGA Management Functions ------------------------------------------*/
ViStatus _VI_FUNC niSync_ConfigureFPGA(ViSession vi,
                                       ViConstString fpgaProgramPath);

/*- Trigger Terminal Connection Functions -------------------------------*/
ViStatus _VI_FUNC niSync_ConnectTrigTerminals(ViSession vi,
                                              ViConstString srcTerminal,
                                              ViConstString destTerminal,
                                              ViConstString syncClock,
                                              ViInt32 invert,
                                              ViInt32 updateEdge);
ViStatus _VI_FUNC niSync_DisconnectTrigTerminals(ViSession vi,
                                                 ViConstString srcTerminal,
                                                 ViConstString destTerminal);
ViStatus _VI_FUNC niSync_GetTrigTerminalConnectionInfo(ViSession vi,
                                                       ViConstString destTerminal,
                                                       ViChar srcTerminal[256],
                                                       ViChar syncClock[256],
                                                       ViInt32* invert,
                                                       ViInt32* updateEdge);

/*- Software Trigger Connection Functions --------------------------------*/
ViStatus _VI_FUNC niSync_ConnectSWTrigToTerminal(ViSession vi,
                                                 ViConstString srcTerminal,
                                                 ViConstString destTerminal,
                                                 ViConstString syncClock,
                                                 ViInt32 invert,
                                                 ViInt32 updateEdge,
                                                 ViReal64 delay);
ViStatus _VI_FUNC niSync_DisconnectSWTrigFromTerminal(ViSession vi,
                                                      ViConstString srcTerminal,
                                                      ViConstString destTerminal);
ViStatus _VI_FUNC niSync_GetSWTrigConnectionInfo(ViSession vi,
                                                 ViConstString destTerminal,
                                                 ViChar srcTerminal[256],
                                                 ViChar syncClk[256],
                                                 ViInt32* invert,
                                                 ViInt32* updateEdge,
                                                 ViReal64* delay);
ViStatus _VI_FUNC niSync_SendSoftwareTrigger(ViSession vi,
                                             ViConstString srcTerminal);

/*- Clk Terminal Functions -----------------------------------------------*/
ViStatus _VI_FUNC niSync_ConnectClkTerminals(ViSession vi,
                                             ViConstString srcTerminal,
                                             ViConstString destTerminal);
ViStatus _VI_FUNC niSync_DisconnectClkTerminals(ViSession vi,
                                                ViConstString srcTerminal,
                                                ViConstString destTerminal);
ViStatus _VI_FUNC niSync_GetClkTerminalConnectionInfo(ViSession vi,
                                                      ViConstString destTerminal,
                                                      ViChar srcTerminal[256]);

/*- Frequency Counting Functions ---------------------------------------*/
ViStatus _VI_FUNC niSync_MeasureFrequency(ViSession vi,
                                          ViConstString srcTerminal,
                                          ViReal64 duration,
                                          ViReal64* actualDuration,
                                          ViReal64* frequency,
                                          ViReal64* frequencyError);

ViStatus _VI_FUNC niSync_MeasureFrequencyEx(ViSession vi,
                                            ViConstString srcTerminal,
                                            ViReal64 duration,
                                            ViUInt32 decimationCount,
                                            ViReal64* actualDuration,
                                            ViReal64* frequency,
                                            ViReal64* frequencyError);
/*- 1588 Functions -----------------------------------------------------*/

/*- 1588 PTP and Time Functions ----------------------------------------*/
ViStatus _VI_FUNC niSync_Start1588(ViSession vi);
ViStatus _VI_FUNC niSync_Stop1588(ViSession vi);
ViStatus _VI_FUNC niSync_SetTime(ViSession vi,
                                 ViInt32 timeSource,
                                 ViUInt32 timeSeconds,
                                 ViUInt32 timeNanoseconds,
                                 ViUInt16 timeFractionalNanoseconds
                                 );
ViStatus _VI_FUNC niSync_GetTime(ViSession vi,
                                 ViUInt32* timeSeconds,
                                 ViUInt32* timeNanoseconds,
                                 ViUInt16* timeFractionalNanoseconds);

ViStatus _VI_FUNC niSync_ResetFrequency(ViSession vi);

/*- 1588 Future Time Events Functions ---------------------------------*/
ViStatus _VI_FUNC niSync_CreateFutureTimeEvent(ViSession vi,
                                               ViConstString terminal,
                                               ViInt32 outputLevel,
                                               ViUInt32 timeSeconds,
                                               ViUInt32 timeNanoseconds,
                                               ViUInt16 timeFractionalNanoseconds);
ViStatus _VI_FUNC niSync_ClearFutureTimeEvents(ViSession vi,
                                               ViConstString terminal);

/*- 1588 Time Stamping Triggers Functions ------------------------------*/
ViStatus _VI_FUNC niSync_EnableTimeStampTrigger(ViSession     vi,
                                                ViConstString terminal,
                                                ViInt32       activeEdge);
ViStatus _VI_FUNC niSync_EnableTimeStampTriggerWithDecimation(ViSession     vi,
                                                              ViConstString terminal,
                                                              ViInt32       activeEdge,
                                                              ViUInt32      decimationCount);
ViStatus _VI_FUNC niSync_ReadTriggerTimeStamp(ViSession vi,
                                              ViConstString terminal,
                                              ViReal64 timeout,
                                              ViUInt32* timeSeconds,
                                              ViUInt32* timeNanoseconds,
                                              ViUInt16* timeFractionalNanoseconds,
                                              ViInt32* detectedEdge);
ViStatus _VI_FUNC niSync_ReadMultipleTriggerTimeStamp(ViSession       vi,
                                                      ViConstString   terminal,
                                                      ViUInt32        timestampsToRead,
                                                      ViReal64        timeout,
                                                      ViUInt32      * timeSecondsBuffer,
                                                      ViUInt32      * timeNanosecondsBuffer,
                                                      ViUInt16      * timeFractionalNanosecondsBuffer,
                                                      ViInt32       * detectedEdgeBuffer,
                                                      ViUInt32      * timestampsRead);
ViStatus _VI_FUNC niSync_DisableTimeStampTrigger(ViSession vi,
                                                 ViConstString terminal);

/*- 1588 Clock Functions ----------------------------------*/
ViStatus _VI_FUNC niSync_CreateClock(ViSession vi,
                                     ViConstString terminal,
                                     ViUInt32 highTicks,
                                     ViUInt32 lowTicks,
                                     ViUInt32 startTimeSeconds,
                                     ViUInt32 startTimeNanoseconds,
                                     ViUInt16 startTimeFractionalNanoseconds,
                                     ViUInt32 stopTimeSeconds,
                                     ViUInt32 stopTimeNanoseconds,
                                     ViUInt16 stopTimeFractionalNanoseconds);
ViStatus _VI_FUNC niSync_ClearClock(ViSession vi,
                                      ViConstString terminal);

ViStatus _VI_FUNC niSync_Start8021AS(ViSession vi);
ViStatus _VI_FUNC niSync_Stop8021AS(ViSession vi);

/*- External Synchronization Functions ---------------------------------*/
ViStatus _VI_FUNC niSync_SetTimeReferenceFreeRunning(ViSession vi);
ViStatus _VI_FUNC niSync_SetTimeReferenceGPS(ViSession vi);
ViStatus _VI_FUNC niSync_SetTimeReferenceIRIG(ViSession vi,
                                              ViInt32 irigType,
                                              ViConstString terminalName
                                              );
ViStatus _VI_FUNC niSync_SetTimeReferencePPS(ViSession vi,
                                             ViConstString terminalName,
                                             ViBoolean useManualTime,
                                             ViUInt32 initialTimeSeconds,
                                             ViUInt32 initialTimeNanoseconds,
                                             ViUInt16 initialTimeFractionalNanoseconds
                                             );
ViStatus _VI_FUNC niSync_SetTimeReference1588OrdinaryClock(ViSession vi);
ViStatus _VI_FUNC niSync_SetTimeReference8021AS(ViSession vi);


/*- External Synchronization Timestamping Functions---------------------*/
ViStatus _VI_FUNC niSync_EnableGPSTimestamping(ViSession vi);
ViStatus _VI_FUNC niSync_EnableIRIGTimestamping(ViSession vi,
                                                ViInt32 irigType,
                                                ViConstString terminalName
                                                );

ViStatus _VI_FUNC niSync_ReadLastGPSTimestamp(ViSession vi,
                                              ViUInt32* timestampSeconds,
                                              ViUInt32* timestampNanoseconds,
                                              ViUInt16* timestampFractionalNanoseconds,
                                              ViUInt32* gpsSeconds,
                                              ViUInt32* gpsNanoseconds,
                                              ViUInt16* gpsFractionalNanoseconds
                                              );

ViStatus _VI_FUNC niSync_ReadLastIRIGTimestamp(ViSession vi,
                                               ViConstString terminal,
                                               ViUInt32* timestampSeconds,
                                               ViUInt32* timestampNanoseconds,
                                               ViUInt16* timestampFractionalNanoseconds,
                                               ViUInt32* irigbSeconds,
                                               ViUInt32* irigbNanoseconds,
                                               ViUInt16* irigbFractionalNanoseconds
                                               );

ViStatus _VI_FUNC niSync_DisableGPSTimestamping(ViSession vi);

ViStatus _VI_FUNC niSync_DisableIRIGTimestamping(ViSession vi,
                                                 ViConstString terminalName
                                                 );

ViStatus _VI_FUNC niSync_GetVelocity(ViSession vi,
                                     ViReal64* eastVelocity,
                                     ViReal64* northVelocity,
                                     ViReal64* upVelocity
                                     );

ViStatus _VI_FUNC niSync_GetLocation(ViSession vi,
                                     ViReal64* latitude,
                                     ViReal64* longitude,
                                     ViReal64* altitude
                                     );

/*- Attribute Functions ------------------------------------------------*/
ViStatus _VI_FUNC niSync_GetAttributeViInt32(ViSession vi,
                                             ViConstString activeItem,
                                             ViAttr attribute,
                                             ViInt32* value);
ViStatus _VI_FUNC niSync_GetAttributeViReal64(ViSession vi,
                                              ViConstString activeItem,
                                              ViAttr attribute,
                                              ViReal64* value);
ViStatus _VI_FUNC niSync_GetAttributeViBoolean(ViSession vi,
                                               ViConstString activeItem,
                                               ViAttr attribute,
                                               ViBoolean* value);
ViStatus _VI_FUNC niSync_GetAttributeViString(ViSession vi,
                                              ViConstString activeItem,
                                              ViAttr attribute,
                                              ViInt32 bufferSize,
                                              ViChar value[]);

ViStatus _VI_FUNC niSync_SetAttributeViInt32(ViSession vi,
                                             ViConstString activeItem,
                                             ViAttr attribute,
                                             ViInt32 value);
ViStatus _VI_FUNC niSync_SetAttributeViReal64(ViSession vi,
                                              ViConstString activeItem,
                                              ViAttr attribute,
                                              ViReal64 value);
ViStatus _VI_FUNC niSync_SetAttributeViBoolean(ViSession vi,
                                               ViConstString activeItem,
                                               ViAttr attribute,
                                               ViBoolean value);
ViStatus _VI_FUNC niSync_SetAttributeViString(ViSession vi,
                                              ViConstString activeItem,
                                              ViAttr attribute,
                                              ViConstString value);

/*- Calibration Functions ------------------------------------------*/

/*- Calibration Utility Functions ----------------------------------*/
ViStatus _VI_FUNC niSync_GetExtCalLastDateAndTime(ViSession vi,
                                                  ViInt32* year,
                                                  ViInt32* month,
                                                  ViInt32* day,
                                                  ViInt32* hour,
                                                  ViInt32* minute);

ViStatus _VI_FUNC niSync_GetExtCalLastTemp(ViSession vi,
                                           ViReal64* temp);

ViStatus _VI_FUNC niSync_GetExtCalRecommendedInterval(ViSession vi,
                                                      ViInt32* months);

ViStatus _VI_FUNC niSync_ChangeExtCalPassword(ViSession vi,
                                              ViConstString oldPassword,
                                              ViConstString newPassword);

ViStatus _VI_FUNC niSync_ReadCurrentTemperature(ViSession vi,
                                                ViReal64* temperature);

/*- Calibration Data Retrieval Functions-----------------------------*/
ViStatus _VI_FUNC niSync_CalGetOscillatorVoltage(ViSession vi,
                                                 ViReal64* voltage);

ViStatus _VI_FUNC niSync_CalGetClk10PhaseVoltage(ViSession vi,
                                                 ViReal64* voltage);

ViStatus _VI_FUNC niSync_CalGetDDSStartPulsePhaseVoltage(ViSession vi,
                                                         ViReal64* voltage);

ViStatus _VI_FUNC niSync_CalGetDDSInitialPhase(ViSession vi,
                                               ViReal64* phase);

/*- Calibration Session Management Functions (password required)-----*/
ViStatus _VI_FUNC niSync_InitExtCal(ViRsrc resourceName,
                                    ViConstString password,
                                    ViSession* extCalVi);

ViStatus _VI_FUNC niSync_CloseExtCal(ViSession extCalVi,
                                     ViInt32 action);

/*- Calibration Adjustment Functions (password required)--------------*/
ViStatus _VI_FUNC niSync_CalAdjustOscillatorVoltage(ViSession extCalVi,
                                                    ViReal64 measuredVoltage,
                                                    ViReal64* oldVoltage);

ViStatus _VI_FUNC niSync_CalAdjustClk10PhaseVoltage(ViSession extCalVi,
                                                    ViReal64 measuredVoltage,
                                                    ViReal64* oldVoltage);

ViStatus _VI_FUNC niSync_CalAdjustDDSStartPulsePhaseVoltage(ViSession extCalVi,
                                                            ViReal64 measuredVoltage,
                                                            ViReal64* oldVoltage);

ViStatus _VI_FUNC niSync_CalAdjustDDSInitialPhase(ViSession extCalVi,
                                                  ViReal64 measuredPhase,
                                                  ViReal64* oldPhase);

/*- Deprecated Functions----------------------------------------------*/
ViStatus _VI_FUNC niSync_StartPTP(ViSession vi,
                                  ViInt32 initialTimeSource,
                                  ViUInt32 initialTimeSeconds,
                                  ViUInt32 initialTimeNanoseconds,
                                  ViUInt16 initialTimeFractionalNanoseconds);

ViStatus _VI_FUNC niSync_StopPTP(ViSession vi);
ViStatus _VI_FUNC niSync_Get1588Time(ViSession vi,
                                     ViUInt32* timeSeconds,
                                     ViUInt32* timeNanoseconds,
                                     ViUInt16* timeFractionalNanoseconds);

/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/
#define NISYNC_WARN_BASE                        (ViStatus)(0x3FFA4000)
#define NISYNC_ERROR_BASE                       (ViStatus)(0xBFFA4000) /* IVI_SPECIFIC_PUBLIC_ATTR_BASE */

// NISYNC_WARN_BASE + 6x is reserved for calibration warnings.
#define NISYNC_WARN_CAL_UNCALIBRATED            (NISYNC_WARN_BASE + 60)
#define NISYNC_WARN_NETWORK_CLIENT_IN_PROGRESS  (NISYNC_WARN_BASE + 100)
#define NISYNC_WARN_UNKNOWN_STATUS              VI_WARN_UNKNOWN_STATUS

#define NISYNC_WARNMSG_CAL_UNCALIBRATED              "This device is not properly calibrated."
#define NISYNC_WARNMSG_NETWORK_CLIENT_IN_PROGRESS    "The request has been accepted by the remote device but processing has not been completed. Wait and attempt to query the property again."
#define NISYNC_WARNMSG_UNKNOWN_STATUS                "The status code passed to the operation could not be interpreted."

#define NISYNC_ERROR_INV_PARAMETER              VI_ERROR_INV_PARAMETER
#define NISYNC_ERROR_NSUP_ATTR                  VI_ERROR_NSUP_ATTR
#define NISYNC_ERROR_NSUP_ATTR_STATE            VI_ERROR_NSUP_ATTR_STATE
#define NISYNC_ERROR_ATTR_READONLY              VI_ERROR_ATTR_READONLY
#define NISYNC_ERROR_ALLOCATION_FAILED          VI_ERROR_ALLOC
#define NISYNC_ERROR_SYSTEM_ERROR               VI_ERROR_SYSTEM_ERROR
#define NISYNC_ERROR_INV_OBJECT                 VI_ERROR_INV_OBJECT
#define NISYNC_ERROR_RSRC_NFOUND                VI_ERROR_RSRC_NFOUND
#define NISYNC_ERROR_NIMPL_OPER                 VI_ERROR_NIMPL_OPER

#define NISYNC_ERROR_INVALID_DESCRIPTOR         (NISYNC_ERROR_BASE + 1)
#define NISYNC_ERROR_INVALID_MODE               (NISYNC_ERROR_BASE + 2)
#define NISYNC_ERROR_FEATURE_NOT_SUPPORTED      (NISYNC_ERROR_BASE + 3)
#define NISYNC_ERROR_VERSION_MISMATCH           (NISYNC_ERROR_BASE + 4)
#define NISYNC_ERROR_INTERNAL_SOFTWARE          (NISYNC_ERROR_BASE + 5)
#define NISYNC_ERROR_FILE_IO                    (NISYNC_ERROR_BASE + 6)
#define NISYNC_ERROR_RESET_NOT_SUPPORTED        (NISYNC_ERROR_BASE + 7)
#define NISYNC_ERROR_INVALID_TYPE               (NISYNC_ERROR_BASE + 8)
#define NISYNC_ERROR_API_SUPPORT_INCOMPATIBLE_WITH_RUNTIME (NISYNC_ERROR_BASE + 9)

#define NISYNC_ERROR_DRIVER_INITIALIZATION      (NISYNC_ERROR_BASE + 10)
#define NISYNC_ERROR_DRIVER_TIMEOUT             (NISYNC_ERROR_BASE + 11)

#define NISYNC_ERROR_READ_FAILURE               (NISYNC_ERROR_BASE + 20)
#define NISYNC_ERROR_WRITE_FAILURE              (NISYNC_ERROR_BASE + 21)
#define NISYNC_ERROR_DEVICE_NOT_FOUND           (NISYNC_ERROR_BASE + 22)
#define NISYNC_ERROR_DEVICE_NOT_READY           (NISYNC_ERROR_BASE + 23)
#define NISYNC_ERROR_INTERNAL_HARDWARE          (NISYNC_ERROR_BASE + 24)
#define NISYNC_ERROR_OVERFLOW                   (NISYNC_ERROR_BASE + 25)
#define NISYNC_ERROR_REMOTE_DEVICE              (NISYNC_ERROR_BASE + 26)

#define NISYNC_ERROR_FIRMWARE_LOAD              (NISYNC_ERROR_BASE + 30)
#define NISYNC_ERROR_DEVICE_NOT_INITIALIZED     (NISYNC_ERROR_BASE + 31)
#define NISYNC_ERROR_CLK10_NOT_PRESENT          (NISYNC_ERROR_BASE + 32)

#define NISYNC_ERROR_PLL_NOT_PRESENT            (NISYNC_ERROR_BASE + 40)
#define NISYNC_ERROR_DDS_NOT_PRESENT            (NISYNC_ERROR_BASE + 41)
#define NISYNC_ERROR_DDS_ALREADY_STARTED        (NISYNC_ERROR_BASE + 42)
#define NISYNC_ERROR_DDS_SYNC_CLK_COMBO_INVALID (NISYNC_ERROR_BASE + 43)

#define NISYNC_ERROR_DEST_TERMINAL_IN_USE                              VI_ERROR_LINE_IN_USE
#define NISYNC_ERROR_SRC_TERMINAL_INVALID                              (NISYNC_ERROR_BASE + 50)
#define NISYNC_ERROR_DEST_TERMINAL_INVALID                             (NISYNC_ERROR_BASE + 51)
#define NISYNC_ERROR_TERMINAL_NOT_CONNECTED                            (NISYNC_ERROR_BASE + 52)
#define NISYNC_ERROR_SYNC_CLK_INVALID                                  (NISYNC_ERROR_BASE + 53)
#define NISYNC_ERROR_TERMINAL_INVALID                                  (NISYNC_ERROR_BASE + 54)
#define NISYNC_ERROR_SRC_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED           (NISYNC_ERROR_BASE + 55)
#define NISYNC_ERROR_DEST_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED          (NISYNC_ERROR_BASE + 56)
#define NISYNC_ERROR_SRC_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT     (NISYNC_ERROR_BASE + 57)
#define NISYNC_ERROR_DEST_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT    (NISYNC_ERROR_BASE + 58)
#define NISYNC_ERROR_DEST_TERMINAL_PXI_CLK10_IN_NOT_IN_SYS_TIMING_SLOT (NISYNC_ERROR_BASE + 59)

#define NISYNC_ERROR_CAL_INCORRECT_PASSWORD  (NISYNC_ERROR_BASE + 60)
#define NISYNC_ERROR_CAL_PASSWORD_TOO_LARGE  (NISYNC_ERROR_BASE + 61)
#define NISYNC_ERROR_CAL_NOT_PERMITTED       (NISYNC_ERROR_BASE + 62)

#define NISYNC_ERROR_RSRC_UNAVAILABLE        (NISYNC_ERROR_BASE + 70)
#define NISYNC_ERROR_RSRC_RESERVED           (NISYNC_ERROR_BASE + 71)
#define NISYNC_ERROR_RSRC_NOT_RESERVED       (NISYNC_ERROR_BASE + 72)
#define NISYNC_ERROR_HW_BUFFER_FULL          (NISYNC_ERROR_BASE + 73)
#define NISYNC_ERROR_SW_BUFFER_FULL          (NISYNC_ERROR_BASE + 74)
#define NISYNC_ERROR_SOCKET_FAILURE          (NISYNC_ERROR_BASE + 75)
#define NISYNC_ERROR_SESSION_ABORTED         (NISYNC_ERROR_BASE + 76)
#define NISYNC_ERROR_SESSION_ABORTING        (NISYNC_ERROR_BASE + 77)
#define NISYNC_ERROR_TERMINAL_NOT_SPECIFIED  (NISYNC_ERROR_BASE + 78)

#define NISYNC_ERROR_TIME_OVERFLOW           (NISYNC_ERROR_BASE + 80)
#define NISYNC_ERROR_TIME_TOO_EARLY          (NISYNC_ERROR_BASE + 81)
#define NISYNC_ERROR_TIME_TOO_LATE           (NISYNC_ERROR_BASE + 82)
#define NISYNC_ERROR_PTP_ALREADY_STARTED     (NISYNC_ERROR_BASE + 83)
#define NISYNC_ERROR_PTP_NOT_STARTED         (NISYNC_ERROR_BASE + 84)
#define NISYNC_ERROR_INVALID_CLOCK_STATE     (NISYNC_ERROR_BASE + 85)
#define NISYNC_ERROR_IP_ADDRESS              (NISYNC_ERROR_BASE + 86)
#define NISYNC_ERROR_FUTURE_TIME_EVENT_TOO_SOON (NISYNC_ERROR_BASE + 87)
#define NISYNC_ERROR_CLOCK_PERIOD_TOO_SHORT  (NISYNC_ERROR_BASE + 88)
#define NISYNC_ERROR_DUP_FUTURE_TIME_EVENT   (NISYNC_ERROR_BASE + 89)
#define NISYNC_ERROR_SYNC_INTERVAL_MISMACH   (NISYNC_ERROR_BASE + 90)
#define NISYNC_ERROR_INVALID_INITIAL_TIME    (NISYNC_ERROR_BASE + 91)
#define NISYNC_ERROR_CLK_ADJ_TOO_LARGE       (NISYNC_ERROR_BASE + 92)
#define NISYNC_ERROR_CLOCK_PERIOD_TOO_LARGE  (NISYNC_ERROR_BASE + 93)
#define NISYNC_ERROR_NETWORK_ADAPTER_NOT_FOUND (NISYNC_ERROR_BASE + 94)

#define NISYNC_ERROR_NO_COMMON_TRIG_LINE_FOR_ROUTE (NISYNC_ERROR_BASE + 95)

#define NISYNC_ERROR_TIMESTAMP_DECIMATION_NOT_SUPPORTED   (NISYNC_ERROR_BASE + 96)
#define NISYNC_ERROR_TIMESTAMP_DECIMATION_COUNT_TOO_SMALL (NISYNC_ERROR_BASE + 97)
#define NISYNC_ERROR_TIMESTAMP_DECIMATION_COUNT_TOO_LARGE (NISYNC_ERROR_BASE + 98)

#define NISYNC_ERROR_FUTURE_TIME_EVENT_REARM_TIME_VIOLATION (NISYNC_ERROR_BASE + 99)

#define NISYNC_ERROR_TIME_SNAPPED (NISYNC_ERROR_BASE + 100)

#define NISYNC_ERROR_TR_TYPE_MISMATCH                            (NISYNC_ERROR_BASE + 101)
#define NISYNC_ERROR_TR_INSTANCE_NOT_FOUND                       (NISYNC_ERROR_BASE + 102)
#define NISYNC_ERROR_REMOTE_DEVICE_READ_FAILURE                  (NISYNC_ERROR_BASE + 103)
#define NISYNC_ERROR_REMOTE_DEVICE_COMMUNICATION_FAILURE         (NISYNC_ERROR_BASE + 104)
#define NISYNC_ERROR_LIB_LOAD_FAILURE                            (NISYNC_ERROR_BASE + 105)
#define NISYNC_ERROR_INVALID_RESOURCE_NAME_FORMAT                (NISYNC_ERROR_BASE + 106)
#define NISYNC_ERROR_TR_INSTANCE_ALREADY_EXISTS                  (NISYNC_ERROR_BASE + 107)
#define NISYNC_ERROR_REMOTE_DEVICE_RESOURCE_NOT_FOUND            (NISYNC_ERROR_BASE + 108)
#define NISYNC_ERROR_CONFLICTING_TR_INSTANCES                    (NISYNC_ERROR_BASE + 109)
#define NISYNC_ERROR_TR_ATTR_NOT_FOUND                           (NISYNC_ERROR_BASE + 110)
#define NISYNC_ERROR_COMMUNICATIONS_FAULT                        (NISYNC_ERROR_BASE + 111)


#define NISYNC_ERRMSG_INV_PARAMETER              "A parameter for this operation is invalid."
#define NISYNC_ERRMSG_NSUP_ATTR                  "The specified attribute is not supported."
#define NISYNC_ERRMSG_NSUP_ATTR_STATE            "The specified attribute state is not supported."
#define NISYNC_ERRMSG_ATTR_READONLY              "The specified attribute is read-only."
#define NISYNC_ERRMSG_ALLOCATION_FAILED          "Insufficient system resources to perform necessary memory allocation."
#define NISYNC_ERRMSG_SYSTEM_ERROR               "Unknown system error (miscellaneous error)."
#define NISYNC_ERRMSG_INV_OBJECT                 "The given session or object reference is invalid."
#define NISYNC_ERRMSG_RSRC_NFOUND                "Insufficient location information or the device or resource is not present in the system."
#define NISYNC_ERRMSG_NIMPL_OPER                 "The given operation is not implemented."
#define NISYNC_ERRMSG_INVALID_DESCRIPTOR         "The specified instrument descriptor is invalid."
#define NISYNC_ERRMSG_INVALID_MODE               "The mode for this operation is invalid."
#define NISYNC_ERRMSG_FEATURE_NOT_SUPPORTED      "This operation requires a feature that is not supported."
#define NISYNC_ERRMSG_VERSION_MISMATCH           "There is a version mismatch."
#define NISYNC_ERRMSG_INTERNAL_SOFTWARE          "An internal software error occurred."
#define NISYNC_ERRMSG_FILE_IO                    "An error occurred while reading or writing a file."
#define NISYNC_ERRMSG_RESET_NOT_SUPPORTED        "This device does not support Reset."
#define NISYNC_ERRMSG_INVALID_TYPE               "A parameter for this operation is of an invalid type."
#define NISYNC_ERRMSG_API_SUPPORT_INCOMPATIBLE_WITH_RUNTIME "The NI-Sync API Support is unable to communicate with the NI-Sync Runtime. To resolve this issue, install NI-Sync 18.0 or later."

#define NISYNC_ERRMSG_DRIVER_INITIALIZATION      "An error occurred while initializing the driver."
#define NISYNC_ERRMSG_DRIVER_TIMEOUT             "The driver timed out while performing an operation."

#define NISYNC_ERRMSG_READ_FAILURE               "A failure occurred while reading from the device."
#define NISYNC_ERRMSG_WRITE_FAILURE              "A failure occurred while writing to the device."
#define NISYNC_ERRMSG_DEVICE_NOT_FOUND           "The specified device was not found."
#define NISYNC_ERRMSG_DEVICE_NOT_READY           "The specified device is not ready."
#define NISYNC_ERRMSG_INTERNAL_HARDWARE          "An internal hardware error occurred."
#define NISYNC_ERRMSG_OVERFLOW                   "An overflow condition occurred."
#define NISYNC_ERRMSG_REMOTE_DEVICE              "The specified device is a remote device.  Remote devices are not allowed."

#define NISYNC_ERRMSG_FIRMWARE_LOAD              "The firmware failed to load."
#define NISYNC_ERRMSG_DEVICE_NOT_INITIALIZED     "The device is not initialized."
#define NISYNC_ERRMSG_CLK10_NOT_PRESENT          "PXI_Clk10 is not present."

#define NISYNC_ERRMSG_PLL_NOT_PRESENT            "This device does not support a PLL."
#define NISYNC_ERRMSG_DDS_NOT_PRESENT            "The device does not support a DDS."
#define NISYNC_ERRMSG_DDS_ALREADY_STARTED        "The specified attribute cannot be set because the DDS is already running."
#define NISYNC_ERRMSG_DDS_SYNC_CLK_COMBO_INVALID "The current DDS frequency is incompatible as a synchronization clock, either the DDS is off or running too fast."

#define NISYNC_ERRMSG_DEST_TERMINAL_IN_USE                              "The specified destination terminal is in use."
#define NISYNC_ERRMSG_SRC_TERMINAL_INVALID                              "The specified source terminal is invalid for this operation."
#define NISYNC_ERRMSG_DEST_TERMINAL_INVALID                             "The specified destination terminal is invalid for this operation."
#define NISYNC_ERRMSG_TERMINAL_NOT_CONNECTED                            "The specified terminal is not connected."
#define NISYNC_ERRMSG_SYNC_CLK_INVALID                                  "The specified synchronization clock is invalid for this operation."
#define NISYNC_ERRMSG_TERMINAL_INVALID                                  "Terminal for the device is invalid."
#define NISYNC_ERRMSG_SRC_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED           "Route failed because the PXI chassis is not identified. The existence of the source terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis."
#define NISYNC_ERRMSG_DEST_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED          "Route failed because the PXI chassis is not identified. The existence of the destination terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis."
#define NISYNC_ERRMSG_SRC_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT     "PXI_Star<n> is available as a source terminal only for devices in a system timing slot. To use PXI_Star<n>, move your device to a system timing slot."
#define NISYNC_ERRMSG_DEST_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT    "PXI_Star<n> is available as a destination terminal only for devices in a system timing slot. To use PXI_Star<n>, move your device to a system timing slot."
#define NISYNC_ERRMSG_DEST_TERMINAL_PXI_CLK10_IN_NOT_IN_SYS_TIMING_SLOT "PXI_Clk10_In is available as a destination terminal only for devices in a system timing slot. Move your device to a system timing slot."

#define NISYNC_ERRMSG_CAL_INCORRECT_PASSWORD "The supplied external calibration password is incorrect."
#define NISYNC_ERRMSG_CAL_PASSWORD_TOO_LARGE "The external calibration password contains too many characters."
#define NISYNC_ERRMSG_CAL_NOT_PERMITTED      "The specified calibration operation is not permitted on this session type."

#define NISYNC_ERRMSG_RSRC_UNAVAILABLE       "A resource necessary to complete the specified operation is not available; therefore, the operation cannot be completed."
#define NISYNC_ERRMSG_RSRC_RESERVED          "A resource necessary to complete the specified operation is already reserved by a previous operation and cannot be shared; therefore, the operation cannot be completed."
#define NISYNC_ERRMSG_RSRC_NOT_RESERVED      "A resource necessary to complete the specified operation is not reserved and should have already been; therefore, the operation cannot be completed"
#define NISYNC_ERRMSG_HW_BUFFER_FULL         "A hardware buffer necessary to complete the specified operation is unexpectedly full; therefore, the operation cannot be completed."
#define NISYNC_ERRMSG_SW_BUFFER_FULL         "A software buffer necessary to complete the specified operation is unexpectedly full; therefore, the operation cannot be completed."
#define NISYNC_ERRMSG_SOCKET_FAILURE         "A network socket necessary to complete the specified operation has generated a failure; therefore, the operation cannot be completed."
#define NISYNC_ERRMSG_SESSION_ABORTED        "The specified operation cannot be performed because a session has been aborted or a device has been removed from the system. Handle this situation as required by the application and then, if appropriate, attempt to perform the operation again."
#define NISYNC_ERRMSG_SESSION_ABORTING       "The specified operation cannot be performed because a session is in the process of being aborted or a device is in the process of being removed from the system. Wait until the abort operation is complete, and attempt to perform the operation again."
#define NISYNC_ERRMSG_TERMINAL_NOT_SPECIFIED "The specified operation cannot be performed since the Active Item was not specified."

#define NISYNC_ERRMSG_TIME_OVERFLOW          "A 1588 time value has overflowed.  The resulting value is not accurate."
#define NISYNC_ERRMSG_TIME_TOO_EARLY         "The specified time value is too early to be represented as a 1588 time value."
#define NISYNC_ERRMSG_TIME_TOO_LATE          "The specified time value is too late to be represetned as a 1588 time value."
#define NISYNC_ERRMSG_PTP_ALREADY_STARTED    "The Precision Time Protocol (PTP) has already been started on this device; therefore, it cannot be started again."
#define NISYNC_ERRMSG_PTP_NOT_STARTED        "The Precision Time Protocol (PTP) has not been started on this device; therefore, it cannot be stopped."
#define NISYNC_ERRMSG_INVALID_CLOCK_STATE    "The specified attribute cannot be set when the Precision Time Protocol (PTP) is in its current state."
#define NISYNC_ERRMSG_IP_ADDRESS             "The IP address for the specified device cannot be determined; therefore, the specified operation cannot be completed."
#define NISYNC_ERRMSG_FUTURE_TIME_EVENT_TOO_SOON "The time for the specified future time event is too soon, or may be in the past, and cannot be programmed in the device before it would occur."
#define NISYNC_ERRMSG_CLOCK_PERIOD_TOO_SHORT "A clock with the specified period is too short to be generated by the device."
#define NISYNC_ERRMSG_DUP_FUTURE_TIME_EVENT  "A future time event with the same time and same terminal as the specified future time event has already been created.  Multiple future time events on the same terminal at the same time cannot be created."
#define NISYNC_ERRMSG_SYNC_INTERVAL_MISMACH  "The specified sync interval for this 1588 clock is different than the sync interval specified for other 1588 clocks participating in the PTP.  Adjust the sync interval on this 1588 clock or the other 1588 clocks participating in the PTP to the same value."
#define NISYNC_ERRMSG_INVALID_INITIAL_TIME   "The specified initial time is invalid.  Initial times must be after 0 hours 1 January 2000 and before 0 hours 1 January 2100."
#define NISYNC_ERRMSG_CLK_ADJ_TOO_LARGE      "The specified 1588 clock adjustment offset is too large.  The clock adjustment cannot be more than +1 seconds or less than -1 seconds."
#define NISYNC_ERRMSG_CLOCK_PERIOD_TOO_LARGE "A clock with the specified period is too large to be generated by the device."
#define NISYNC_ERRMSG_NETWORK_ADAPTER_NOT_FOUND "The network interface associated with the device was not found.  Ensure that the associated NIC (network interface controller) is installed and enabled."

#define NISYNC_ERRMSG_NO_COMMON_TRIG_LINE_FOR_ROUTE "There are no shared trigger lines between the two devices which are acceptable to both devices. Consider routing the signal through the I/O connectors of the two devices, if applicable."

#define NISYNC_ERRMSG_TIMESTAMP_DECIMATION_NOT_SUPPORTED   "This device does not support timestamp decimation."
#define NISYNC_ERRMSG_TIMESTAMP_DECIMATION_COUNT_TOO_SMALL "The timestamp decimation count must be greater than 0 for this device."
#define NISYNC_ERRMSG_TIMESTAMP_DECIMATION_COUNT_TOO_LARGE "The specified timestamp decimation count is too great for this device."

#define NISYNC_ERRMSG_FUTURE_TIME_EVENT_REARM_TIME_VIOLATION "The specified future time event violates the rearm time of the future time event engine."

#define NISYNC_ERRMSG_TIME_SNAPPED "Board time was snapped back during measurement."

#define NISYNC_ERRMSG_TR_TYPE_MISMATCH "The requested property is not supported by the time reference specified on the Active Terminal."
#define NISYNC_ERRMSG_TR_INSTANCE_NOT_FOUND "The requested time reference instance was not found."
#define NISYNC_ERRMSG_REMOTE_DEVICE_READ_FAILURE "The data received from the remote device could not be interpreted. Try to perform the operation again."
#define NISYNC_ERRMSG_REMOTE_DEVICE_COMMUNICATION_FAILURE "A failure occured while communicating with the remote device. Ensure the remote device is accessible."
#define NISYNC_ERRMSG_LIB_LOAD_FAILURE "Unable to load an internal library. If the error persists contact National Instruments support."
#define NISYNC_ERRMSG_INVALID_RESOURCE_NAME_FORMAT "The resource name format is invalid."
#define NISYNC_ERRMSG_TR_INSTANCE_ALREADY_EXISTS "The specified time reference already exists."
#define NISYNC_ERRMSG_REMOTE_DEVICE_RESOURCE_NOT_FOUND "Requested resource not found on a remote device. This may be because the device was not reachable or has experienced an internal error. It may also mean you need to update software or firmware on the remote device."
#define NISYNC_ERRMSG_CONFLICTING_TR_INSTANCES "The time reference you are trying to enable conflicts with a time reference already running on the same interface. Disable the conflicting time reference and retry the operation."
#define NISYNC_ERRMSG_TR_ATTR_NOT_FOUND "The requested attribute is not currently available. This may be because the time reference is disabled, not ready, or has encountered an error."
#define NISYNC_ERRMSG_COMMUNICATIONS_FAULT "A failure occured while communicating with a required software service running on the device. Restart the device. If the error persists, contact National Instruments support."

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* __NISYNC_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nisyscfg.h sha256=d3cd0253f93fd9ccbaafcc4be28380a5b3bd6214ba203731bac71554af866cc5 bytes=63238 -->
## FILE: imports/include/nisyscfg.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nisyscfg.h`
- sha256: `d3cd0253f93fd9ccbaafcc4be28380a5b3bd6214ba203731bac71554af866cc5`
- bytes: 63238

````c
/*============================================================================*/
/*                       NI System Configuration API                          */
/*----------------------------------------------------------------------------*/
/*    Copyright (c) National Instruments 2010-2022.  All Rights Reserved.     */
/*----------------------------------------------------------------------------*/
/*                                                                            */
/* Title:   nisyscfg.h                                                        */
/* Purpose: Include file to interact with the NI System Configuration API     */
/*                                                                            */
/*============================================================================*/

#ifndef ___nisysconfig_h___
#define ___nisysconfig_h___

#include <stddef.h>
#include <stdarg.h>
#include "nisyscfg_errors.h"

#if defined(_CVI_)
   #pragma EnableLibraryRuntimeChecking
#endif

// All our public functions return a signed 32-bit status code.
#if defined(__WIN32__) || defined(__NT__) || defined(_WIN32) || defined(WIN32)
   #define NISYSCFGCONV    __stdcall
   #define NISYSCFGCDECL   NISysCfgStatus __cdecl
   typedef unsigned __int64 NISysCfgUInt64;
#else
   #define NISYSCFGCONV
   #define NISYSCFGCDECL   NISysCfgStatus
   typedef unsigned long long NISysCfgUInt64;
#endif
#define NISYSCFGCFUNC   NISysCfgStatus NISYSCFGCONV

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

// Functions that output a simple string require a user-supplied buffer of this size.
#define NISYSCFG_SIMPLE_STRING_LENGTH           1024

// Functions that auto-restart a target use a default timeout of 180 seconds (3 minutes).
// Call NISysCfgSetSystemProperty with NISysCfgSystemPropertyAutoRestartTimeout to change it.
#define NISYSCFG_REBOOT_DEFAULT_TIMEOUT_MSEC    180000

// Functions that operate on a remote target use a default timeout of 300 seconds (5 minutes).
// Call NISysCfgSetRemoteTimeout to change it.
#define NISYSCFG_REMOTE_DEFAULT_TIMEOUT_MSEC    300000

#if defined(_CVI_)
   #pragma pack(push, 4)
   #ifndef CVITime_DECLARED
      #define CVITime_DECLARED
      typedef struct CVITime { unsigned __int64 lsb; __int64 msb; } CVITime;
   #endif
   #ifndef CVIAbsoluteTime_DECLARED
      #define CVIAbsoluteTime_DECLARED
      typedef union CVIAbsoluteTime { CVITime cviTime; unsigned int u32Data[4]; } CVIAbsoluteTime;
   #endif
   typedef CVIAbsoluteTime NISysCfgTimestampUTC;
   #pragma pack(pop)
#else
   typedef struct { unsigned int u32Data[4]; } NISysCfgTimestampUTC;
#endif

////////////////////////////////////////////////////////////////////////////////
// Handles
////////////////////////////////////////////////////////////////////////////////

typedef void * NISysCfgSessionHandle;
typedef void * NISysCfgResourceHandle;
typedef void * NISysCfgFilterHandle;
typedef void * NISysCfgSoftwareSetHandle;
typedef void * NISysCfgEnumResourceHandle;
typedef void * NISysCfgEnumExpertHandle;
typedef void * NISysCfgEnumSystemHandle;
typedef void * NISysCfgEnumSoftwareFeedHandle;
typedef void * NISysCfgEnumSoftwareSetHandle;
typedef void * NISysCfgEnumDependencyHandle;
typedef void * NISysCfgEnumSoftwareComponentHandle;

////////////////////////////////////////////////////////////////////////////////
// Enumerations
////////////////////////////////////////////////////////////////////////////////

typedef enum
{
   NISysCfgIncludeCachedResultsNone          = 0,
   NISysCfgIncludeCachedResultsOnlyIfOnline  = 1,
   NISysCfgIncludeCachedResultsAll           = 3
} NISysCfgIncludeCachedResults;

// The initialization string may contain any combination of 1 or 2
// of the hostname, IP address, and/or MAC address.
typedef enum
{
   NISysCfgSystemNameFormatHostname          = 0x10,        // "hostname"
   NISysCfgSystemNameFormatHostnameIp        = 0x12,        // "hostname (1.2.3.4)"
   NISysCfgSystemNameFormatHostnameMac       = 0x13,        // "hostname (01:02:03:04:05:06)"
   NISysCfgSystemNameFormatIp                = 0x20,        // "1.2.3.4"
   NISysCfgSystemNameFormatIpHostname        = 0x21,        // "1.2.3.4 (hostname)"
   NISysCfgSystemNameFormatIpMac             = 0x23,        // "1.2.3.4 (01:02:03:04:05:06)"
   NISysCfgSystemNameFormatMac               = 0x30,        // "01:02:03:04:05:06"
   NISysCfgSystemNameFormatMacHostname       = 0x31,        // "01:02:03:04:05:06 (hostname)"
   NISysCfgSystemNameFormatMacIp             = 0x32         // "01:02:03:04:05:06 (1.2.3.4)"
} NISysCfgSystemNameFormat;

typedef enum
{
   NISysCfgFileSystemDefault                 = 0x0000,
   NISysCfgFileSystemFat                     = 0x0001,
   NISysCfgFileSystemReliance                = 0x0002,
   NISysCfgFileSystemUBIFS                   = 0x4000,
   NISysCfgFileSystemExt4                    = 0x8000
} NISysCfgFileSystemMode;

typedef enum
{
   NISysCfgResetPrimaryResetOthers           = 0,
   NISysCfgPreservePrimaryResetOthers        = 1,
   NISysCfgPreservePrimaryPreserveOthers     = 2,
   NISysCfgPreservePrimaryApplyOthers        = 3,
   NISysCfgApplyPrimaryResetOthers           = 4,
   NISysCfgApplyPrimaryPreserveOthers        = 5,
   NISysCfgApplyPrimaryApplyOthers           = 6
} NISysCfgNetworkInterfaceSettings;

typedef enum
{
   NISysCfgItemTypeStandard                  = 0,           // Standard visible component
   NISysCfgItemTypeHidden                    = 1,           // Hidden component
   NISysCfgItemTypeSystem                    = 2,           // Required system component (hidden package or base system image installed by the host)
   NISysCfgItemTypeUnknown                   = 3,           // Unknown component type
   NISysCfgItemTypeStartup                   = 4,           // Startup component
   NISysCfgItemTypeImage                     = 5,           // User-defined system image
   NISysCfgItemTypeEssential                 = 6,           // Required visible component
   NISysCfgItemTypeSystemPackage             = 7            // Base system image installed using a package from feeds on ni.com
} NISysCfgComponentType;

typedef enum
{
   NISysCfgIncludeItemsAllVisible            = 0x0000,      // All visible (standard, startup, essential)
   NISysCfgIncludeItemsAllVisibleAndHidden   = 0x0001,      // Visible and hidden
   NISysCfgIncludeItemsOnlyStandard          = 0x0002,      // Only standard
   NISysCfgIncludeItemsOnlyStartup           = 0x0003       // Only startup
} NISysCfgIncludeComponentTypes;

typedef enum
{
   NISysCfgVersionSelectionHighest           = 0,
   NISysCfgVersionSelectionExact             = 1
} NISysCfgVersionSelectionMode;

typedef enum
{
   NISysCfgImportMergeItems                  = 0,           // Source data "wins" in the case of overwrite conflicts
   NISysCfgImportDeleteConfigFirst           = 0x100000,    // Delete product data at destination prior to copying
   NISysCfgImportPreserveConflictItems       = 0x200000     // Destination data "wins" in the case of overwrite conflicts
} NISysCfgImportMode;

typedef enum
{
   NISysCfgReportXml                         = 0,
   NISysCfgReportHtml                        = 1,
   NISysCfgReportTechnicalSupportZip         = 2
} NISysCfgReportType;

typedef enum
{
   NISysCfgBusTypeBuiltIn                    = 0,
   NISysCfgBusTypePciPxi                     = 1,
   NISysCfgBusTypeUsb                        = 2,
   NISysCfgBusTypeGpib                       = 3,
   NISysCfgBusTypeVxi                        = 4,
   NISysCfgBusTypeSerial                     = 5,
   NISysCfgBusTypeTcpIp                      = 6,
   NISysCfgBusTypeCompactRio                 = 7,
   NISysCfgBusTypeScxi                       = 8,
   NISysCfgBusTypeCompactDaq                 = 9,
   NISysCfgBusTypeSwitchBlock                = 10,
   NISysCfgBusTypeScc                        = 11,
   NISysCfgBusTypeFireWire                   = 12,
   NISysCfgBusTypeAccessory                  = 13,
   NISysCfgBusTypeCan                        = 14,
   NISysCfgBusTypeSwitchBlockDevice          = 15,
   NISysCfgBusTypeSlsc                       = 16
} NISysCfgBusType;

typedef enum
{
   NISysCfgHasDriverTypeUnknown              = -1,
   NISysCfgHasDriverTypeNotInstalled         =  0,
   NISysCfgHasDriverTypeInstalled            =  1
} NISysCfgHasDriverType;

typedef enum
{
   NISysCfgIsPresentTypeInitializing         = -2,
   NISysCfgIsPresentTypeUnknown              = -1,
   NISysCfgIsPresentTypeNotPresent           =  0,
   NISysCfgIsPresentTypePresent              =  1
} NISysCfgIsPresentType;

typedef enum
{
   NISysCfgIpAddressModeStatic               = 1,
   NISysCfgIpAddressModeDhcpOrLinkLocal      = 2,
   NISysCfgIpAddressModeLinkLocalOnly        = 4,
   NISysCfgIpAddressModeDhcpOnly             = 8
} NISysCfgIpAddressMode;

typedef enum
{
   NISysCfgBoolFalse                         = 0,
   NISysCfgBoolTrue                          = 1
} NISysCfgBool;

typedef enum
{
   NISysCfgLocaleDefault                     = 0,
   NISysCfgLocaleChineseSimplified           = 2052,
   NISysCfgLocaleEnglish                     = 1033,
   NISysCfgLocaleFrench                      = 1036,
   NISysCfgLocaleGerman                      = 1031,
   NISysCfgLocaleJapanese                    = 1041,
   NISysCfgLocaleKorean                      = 1042
} NISysCfgLocale;

typedef enum
{
   NISysCfgFilterModeMatchValuesAll          = 1,
   NISysCfgFilterModeMatchValuesAny          = 2,
   NISysCfgFilterModeMatchValuesNone         = 3,
   NISysCfgFilterModeAllPropertiesExist      = 4
} NISysCfgFilterMode;

typedef enum
{
   NISysCfgServiceTypemDnsNiTcp              = 0,
   NISysCfgServiceTypemDnsNiRealtime         = 1,
   NISysCfgServiceTypemDnsNiSysapi           = 2,
   NISysCfgServiceTypemDnsNiHttp             = 3,
   NISysCfgServiceTypeLocalSystem            = 4,
   NISysCfgServiceTypeLocalNetInterface      = 5,
   NISysCfgServiceTypeLocalTimeKeeper        = 6,
   NISysCfgServiceTypeLocalTimeSource        = 7,
   NISysCfgServiceTypemDnsLxi                = 8,
   NISysCfgServiceTypeLocalFpga              = 9
} NISysCfgServiceType;

typedef enum
{
   NISysCfgAdapterTypeEthernet               = 1,
   NISysCfgAdapterTypeWlan                   = 2
} NISysCfgAdapterType;

typedef enum
{
   NISysCfgAdapterModeDisabled               = 1,
   NISysCfgAdapterModeTcpIpEthernet          = 2,
   NISysCfgAdapterModeDeterministic          = 4,
   NISysCfgAdapterModeEtherCat               = 8,
   NISysCfgAdapterModeTcpIpWlan              = 32,
   NISysCfgAdapterModeTcpIpAccessPoint       = 64
} NISysCfgAdapterMode;

typedef enum
{
   NISysCfgLinkSpeedNone                     = 0,
   NISysCfgLinkSpeedAuto                     = 1,
   NISysCfgLinkSpeed10mbHalf                 = 2,
   NISysCfgLinkSpeed10mbFull                 = 4,
   NISysCfgLinkSpeed100mbHalf                = 8,
   NISysCfgLinkSpeed100mbFull                = 16,
   NISysCfgLinkSpeedGigabitHalf              = 32,
   NISysCfgLinkSpeedGigabitFull              = 64,
   // Wireless 802.11 protocols (speeds)
   NISysCfgLinkSpeedWlan80211a               = 131072,
   NISysCfgLinkSpeedWlan80211b               = 262144,
   NISysCfgLinkSpeedWlan80211g               = 524288,
   NISysCfgLinkSpeedWlan80211n               = 1048576,
   NISysCfgLinkSpeedWlan80211n5GHz           = 2097152
} NISysCfgLinkSpeed;

typedef enum
{
   NISysCfgPacketDetectionNone               = 0,
   NISysCfgPacketDetectionLineInterrupt      = 1,
   NISysCfgPacketDetectionPolling            = 2,
   NISysCfgPacketDetectionSignaledInterrupt  = 4
} NISysCfgPacketDetection;

typedef enum
{
   NISysCfgConnectionTypeNone                = 0,
   NISysCfgConnectionTypeInfrastructure      = 1,
   NISysCfgConnectionTypeAdHoc               = 2
} NISysCfgConnectionType;

typedef enum
{
   NISysCfgSecurityTypeNone                  = 0,
   NISysCfgSecurityTypeNotSupported          = 1,
   NISysCfgSecurityTypeOpen                  = 2,
   NISysCfgSecurityTypeWep                   = 4,
   NISysCfgSecurityTypeWpaPsk                = 8,
   NISysCfgSecurityTypeWpaEap                = 16,
   NISysCfgSecurityTypeWpa2Psk               = 32,
   NISysCfgSecurityTypeWpa2Eap               = 64
} NISysCfgSecurityType;

typedef enum
{
   NISysCfgEapTypeNone                       = 0,
   NISysCfgEapTypeEapTls                     = 1,
   NISysCfgEapTypeEapTtls                    = 2,
   NISysCfgEapTypeEapFast                    = 4,
   NISysCfgEapTypeLeap                       = 8,
   NISysCfgEapTypePeap                       = 16
} NISysCfgEapType;

// Negative firmware states are in-progress; the user should continue polling.
// Non-negative firmware states are terminal; no update operation is in progress.
typedef enum
{
   NISysCfgFirmwareReadyPendingAutoRestart   = -4,
   NISysCfgFirmwareVerifyingNewImage         = -3,
   NISysCfgFirmwareWritingFlashingNewImage   = -2,
   NISysCfgFirmwareUpdateModeWaitingForImage = -1,
   NISysCfgFirmwareCorruptCannotRun          =  0,
   NISysCfgFirmwareNoneInstalled             =  1,
   NISysCfgFirmwareInstalledNormalOperation  =  2,
   NISysCfgFirmwareReadyPendingUserRestart   =  3,
   NISysCfgFirmwareReadyPendingUserAction    =  4,
   NISysCfgFirmwareUpdateAttemptFailed       =  5
} NISysCfgFirmwareStatus;

typedef enum
{
   NISysCfgValidateButDoNotDelete            = -1,
   NISysCfgDeleteIfNoDependenciesExist       =  0,
   NISysCfgDeleteItemAndAnyDependencies      =  1,
   NISysCfgDeleteItemButKeepDependencies     =  2
} NISysCfgDeleteValidationMode;

typedef enum
{
   NISysCfgAccessTypeLocalOnly               = 0,
   NISysCfgAccessTypeLocalAndRemote          = 1
} NISysCfgAccessType;

typedef enum
{
   NISysCfgLedStateOff                       = 0,
   NISysCfgLedStateSolidGreen                = 1,
   NISysCfgLedStateSolidYellow               = 2,
   NISysCfgLedStateBlinkingGreen             = 4,
   NISysCfgLedStateBlinkingYellow            = 8
} NISysCfgLedState;

typedef enum
{
   NISysCfgSwitchStateDisabled               = 0,
   NISysCfgSwitchStateEnabled                = 1
} NISysCfgSwitchState;

typedef enum
{
   NISysCfgFirmwareUpdateModeNone            = 0,
   NISysCfgFirmwareUpdateModeManual          = 1,
   NISysCfgFirmwareUpdateModeDriverManaged   = 2
} NISysCfgFirmwareUpdateMode;

typedef enum
{
   NISysCfgModuleProgramModeNone             = 0,
   NISysCfgModuleProgramModeRealtimeCpu      = 1,
   NISysCfgModuleProgramModeRealtimeScan     = 2,
   NISysCfgModuleProgramModeLabVIEWFpga      = 4
} NISysCfgModuleProgramMode;

// NOTE: For string properties, callers pass in a pointer to a buffer or array they have allocated.
typedef enum
{
   // Read-only properties
   NISysCfgResourcePropertyIsDevice                            = 16781312,    // NISysCfgBool
   NISysCfgResourcePropertyIsChassis                           = 16941056,    // NISysCfgBool
   NISysCfgResourcePropertyConnectsToBusType                   = 16785408,    // NISysCfgBusType
   NISysCfgResourcePropertyVendorId                            = 16789504,    // unsigned int
   NISysCfgResourcePropertyVendorName                          = 16793600,    // char *
   NISysCfgResourcePropertyProductId                           = 16797696,    // unsigned int
   NISysCfgResourcePropertyProductName                         = 16801792,    // char *
   NISysCfgResourcePropertySerialNumber                        = 16805888,    // char *
   NISysCfgResourcePropertyFirmwareRevision                    = 16969728,    // char *
   NISysCfgResourcePropertyIsNIProduct                         = 16809984,    // NISysCfgBool
   NISysCfgResourcePropertyIsSimulated                         = 16814080,    // NISysCfgBool
   NISysCfgResourcePropertyConnectsToLinkName                  = 16818176,    // char *
   NISysCfgResourcePropertyHasDriver                           = 16920576,    // NISysCfgHasDriverType
   NISysCfgResourcePropertyIsPresent                           = 16924672,    // NISysCfgIsPresentType
   NISysCfgResourcePropertySlotNumber                          = 16822272,    // int
   NISysCfgResourcePropertySupportsInternalCalibration         = 16842752,    // NISysCfgBool
   NISysCfgResourcePropertySupportsExternalCalibration         = 16859136,    // NISysCfgBool
   NISysCfgResourcePropertyExternalCalibrationLastTemp         = 16867328,    // double
   NISysCfgResourcePropertyCalibrationComments                 = 16961536,    // char *
   NISysCfgResourcePropertyInternalCalibrationLastLimited      = 17420288,    // NISysCfgBool
   NISysCfgResourcePropertyExternalCalibrationChecksum         = 17432576,    // char *
   NISysCfgResourcePropertyCurrentTemp                         = 16965632,    // double
   NISysCfgResourcePropertyPxiPciBusNumber                     = 16875520,    // unsigned int
   NISysCfgResourcePropertyPxiPciDeviceNumber                  = 16879616,    // unsigned int
   NISysCfgResourcePropertyPxiPciFunctionNumber                = 16883712,    // unsigned int
   NISysCfgResourcePropertyPxiPciLinkWidth                     = 16973824,    // int
   NISysCfgResourcePropertyPxiPciMaxLinkWidth                  = 16977920,    // int
   NISysCfgResourcePropertyUsbInterface                        = 16887808,    // unsigned int
   NISysCfgResourcePropertyTcpHostName                         = 16928768,    // char *
   NISysCfgResourcePropertyTcpMacAddress                       = 16986112,    // char *
   NISysCfgResourcePropertyTcpIpAddress                        = 16957440,    // char *
   NISysCfgResourcePropertyTcpDeviceClass                      = 17022976,    // char *
   NISysCfgResourcePropertyGpibPrimaryAddress                  = 16994304,    // int
   NISysCfgResourcePropertyGpibSecondaryAddress                = 16998400,    // int
   NISysCfgResourcePropertySerialPortBinding                   = 17076224,    // char *
   NISysCfgResourcePropertyProvidesBusType                     = 16932864,    // NISysCfgBusType
   NISysCfgResourcePropertyProvidesLinkName                    = 16936960,    // char *
   NISysCfgResourcePropertyNumberOfSlots                       = 16826368,    // int
   NISysCfgResourcePropertySupportsFirmwareUpdate              = 17080320,    // NISysCfgBool
   NISysCfgResourcePropertyFirmwareFilePattern                 = 17084416,    // char *
   NISysCfgResourcePropertyRecommendedCalibrationInterval      = 17207296,    // int
   NISysCfgResourcePropertySupportsCalibrationWrite            = 17215488,    // NISysCfgBool
   NISysCfgResourcePropertyHardwareRevision                    = 17256448,    // char *
   NISysCfgResourcePropertyCpuModelName                        = 17313792,    // char *
   NISysCfgResourcePropertyCpuSteppingRevision                 = 17317888,    // int
   NISysCfgResourcePropertyModelNameNumber                     = 17436672,    // unsigned int
   NISysCfgResourcePropertyModuleProgramMode                   = 17440768,    // NISysCfgModuleProgramMode
   NISysCfgResourcePropertyConnectsToNumSlots                  = 17072128,    // int
   NISysCfgResourcePropertySlotOffsetLeft                      = 17276928,    // unsigned int
   NISysCfgResourcePropertyInternalCalibrationValuesInRange    = 17489920,    // NISysCfgBool
   NISysCfgResourcePropertyNumberOfInternalCalibrationDetails  = 17510400,    // int

   // Read/Write firmware properties
   NISysCfgResourcePropertyFirmwareUpdateMode                  = 17354752,    // NISysCfgFirmwareUpdateMode

   // Read/Write calibration properties
   NISysCfgResourcePropertyExternalCalibrationLastTime         = 16863232,    // NISysCfgTimestampUTC
   NISysCfgResourcePropertyExternalCalibrationLastAdjustTime   = 17502208,    // NISysCfgTimestampUTC
   NISysCfgResourcePropertyRecommendedNextCalibrationTime      = 16871424,    // NISysCfgTimestampUTC
   NISysCfgResourcePropertyExternalCalibrationLastLimited      = 17428480,    // NISysCfgBool

   // Write-only calibration properties
   NISysCfgResourcePropertyCalibrationCurrentPassword          = 17223680,    // char *
   NISysCfgResourcePropertyCalibrationNewPassword              = 17227776,    // char *

   // Read/Write remote access properties
   NISysCfgResourcePropertySysCfgAccess                        = 219504640,   // NISysCfgAccessType

   // Read-only network adapter properties
   NISysCfgResourcePropertyAdapterType                         = 219332608,   // NISysCfgAdapterType
   NISysCfgResourcePropertyMacAddress                          = 219168768,   // char *

   // Read/Write network adapter properties
   NISysCfgResourcePropertyAdapterMode                         = 219160576,   // NISysCfgAdapterMode
   NISysCfgResourcePropertyTcpIpRequestMode                    = 219172864,   // NISysCfgIpAddressMode
   NISysCfgResourcePropertyTcpIpv4Address                      = 219181056,   // char *
   NISysCfgResourcePropertyTcpIpv4Subnet                       = 219189248,   // char *
   NISysCfgResourcePropertyTcpIpv4Gateway                      = 219193344,   // char *
   NISysCfgResourcePropertyTcpIpv4DnsServer                    = 219197440,   // char *
   NISysCfgResourcePropertyTcpPreferredLinkSpeed               = 219213824,   // NISysCfgLinkSpeed
   NISysCfgResourcePropertyTcpCurrentLinkSpeed                 = 219222016,   // NISysCfgLinkSpeed
   NISysCfgResourcePropertyTcpPacketDetection                  = 219258880,   // NISysCfgPacketDetection
   NISysCfgResourcePropertyTcpPollingInterval                  = 219262976,   // unsigned int
   NISysCfgResourcePropertyIsPrimaryAdapter                    = 219308032,   // NISysCfgBool
   NISysCfgResourcePropertyEtherCatMasterId                    = 219250688,   // unsigned int
   NISysCfgResourcePropertyEtherCatMasterRedundancy            = 219500544,   // NISysCfgBool

   // Read-only wireless network adapter properties
   NISysCfgResourcePropertyWlanBssid                           = 219398144,   // char *
   NISysCfgResourcePropertyWlanCurrentLinkQuality              = 219394048,   // unsigned int

   // Read/Write wireless network adapter properties
   NISysCfgResourcePropertyWlanCurrentSsid                     = 219377664,   // char *
   NISysCfgResourcePropertyWlanCurrentConnectionType           = 219381760,   // NISysCfgConnectionType
   NISysCfgResourcePropertyWlanCurrentSecurityType             = 219385856,   // NISysCfgSecurityType
   NISysCfgResourcePropertyWlanCurrentEapType                  = 219389952,   // NISysCfgEapType
   NISysCfgResourcePropertyWlanCountryCode                     = 219406336,   // int
   NISysCfgResourcePropertyWlanChannelNumber                   = 219410432,   // unsigned int
   NISysCfgResourcePropertyWlanClientCertificate               = 219422720,   // char *

   // Write-only wireless network adapter properties
   NISysCfgResourcePropertyWlanSecurityIdentity                = 219414528,   // char *
   NISysCfgResourcePropertyWlanSecurityKey                     = 219418624,   // char *

   // Read-only time properties
   NISysCfgResourcePropertySystemStartTime                     = 17108992,     // NISysCfgTimestampUTC

   // Read/Write time properties
   NISysCfgResourcePropertyCurrentTime                         = 219279360,    // NISysCfgTimestampUTC
   NISysCfgResourcePropertyTimeZone                            = 219471872,    // char *

   // Read/Write startup settings properties
   NISysCfgResourcePropertyUserDirectedSafeModeSwitch          = 219537408,    // NISysCfgBool
   NISysCfgResourcePropertyConsoleOutSwitch                    = 219541504,    // NISysCfgBool
   NISysCfgResourcePropertyIpResetSwitch                       = 219545600,    // NISysCfgBool

   // Read-only counts for indexed properties
   NISysCfgResourcePropertyNumberOfDiscoveredAccessPoints      = 219365376,   // unsigned int
   NISysCfgResourcePropertyNumberOfExperts                     = 16891904,    // int
   NISysCfgResourcePropertyNumberOfServices                    = 17010688,    // int
   NISysCfgResourcePropertyNumberOfAvailableFirmwareVersions   = 17088512,    // int
   NISysCfgResourcePropertyNumberOfCpuCores                    = 17506304,    // int
   NISysCfgResourcePropertyNumberOfCpuLogicalProcessors        = 17137664,    // int
   NISysCfgResourcePropertyNumberOfFans                        = 17174528,    // int
   NISysCfgResourcePropertyNumberOfPowerSensors                = 17448960,    // int
   NISysCfgResourcePropertyNumberOfTemperatureSensors          = 17186816,    // int
   NISysCfgResourcePropertyNumberOfVoltageSensors              = 17149952,    // int
   NISysCfgResourcePropertyNumberOfUserLedIndicators           = 17281024,    // int
   NISysCfgResourcePropertyNumberOfUserSwitches                = 17293312     // int
} NISysCfgResourceProperty;

#define NISysCfgResourcePropertyNumberOfCpus                   NISysCfgResourcePropertyNumberOfCpuLogicalProcessors
#define NISysCfgResourcePropertyPxiPciSlotLinkWidth            (NISysCfgResourceProperty)16982016
#define NISysCfgResourcePropertyInternalCalibrationLastTime    (NISysCfgResourceProperty)NISysCfgIndexedPropertyInternalCalibrationLastTime
#define NISysCfgResourcePropertyInternalCalibrationLastTemp    (NISysCfgResourceProperty)NISysCfgIndexedPropertyInternalCalibrationLastTemp

#if defined(WIN32) && (_MSC_VER >= 1300)
#pragma deprecated("NISysCfgResourcePropertyNumberOfCpus")
#pragma deprecated("NISysCfgResourcePropertyPxiPciSlotLinkWidth")
#pragma deprecated("NISysCfgResourcePropertyInternalCalibrationLastTime")
#pragma deprecated("NISysCfgResourcePropertyInternalCalibrationLastTemp")
#endif

typedef enum
{
   // Read-only properties
   NISysCfgIndexedPropertyServiceType                          = 17014784,    // NISysCfgServiceType
   NISysCfgIndexedPropertyAvailableFirmwareVersion             = 17092608,    // char *

   // Read-only wireless network adapter properties
   NISysCfgIndexedPropertyWlanAvailableSsid                    = 219336704,   // char *
   NISysCfgIndexedPropertyWlanAvailableBssid                   = 219443200,   // char *
   NISysCfgIndexedPropertyWlanAvailableConnectionType          = 219340800,   // NISysCfgConnectionType
   NISysCfgIndexedPropertyWlanAvailableSecurityType            = 219344896,   // NISysCfgSecurityType
   NISysCfgIndexedPropertyWlanAvailableLinkQuality             = 219353088,   // unsigned int
   NISysCfgIndexedPropertyWlanAvailableChannelNumber           = 219357184,   // unsigned int
   NISysCfgIndexedPropertyWlanAvailableLinkSpeed               = 219361280,   // NISysCfgLinkSpeed

   // Read-only properties
   NISysCfgIndexedPropertyCpuTotalLoad                         = 17141760,    // unsigned int
   NISysCfgIndexedPropertyCpuInterruptLoad                     = 17145856,    // unsigned int
   NISysCfgIndexedPropertyCpuSpeed                             = 17309696,    // unsigned int
   NISysCfgIndexedPropertyFanName                              = 17178624,    // char *
   NISysCfgIndexedPropertyFanReading                           = 17182720,    // unsigned int
   NISysCfgIndexedPropertyPowerName                            = 17453056,    // char *
   NISysCfgIndexedPropertyPowerReading                         = 17457152,    // double
   NISysCfgIndexedPropertyPowerUpperCritical                   = 17461248,    // double
   NISysCfgIndexedPropertyTemperatureName                      = 17190912,    // char *
   NISysCfgIndexedPropertyTemperatureReading                   = 16965632,    // double
   NISysCfgIndexedPropertyTemperatureLowerCritical             = 17195008,    // double
   NISysCfgIndexedPropertyTemperatureUpperCritical             = 17199104,    // double
   NISysCfgIndexedPropertyVoltageName                          = 17154048,    // char *
   NISysCfgIndexedPropertyVoltageReading                       = 17158144,    // double
   NISysCfgIndexedPropertyVoltageNominal                       = 17162240,    // double
   NISysCfgIndexedPropertyVoltageLowerCritical                 = 17166336,    // double
   NISysCfgIndexedPropertyVoltageUpperCritical                 = 17170432,    // double
   NISysCfgIndexedPropertyUserLedName                          = 17285120,    // char *
   NISysCfgIndexedPropertyUserSwitchName                       = 17297408,    // char *
   NISysCfgIndexedPropertyUserSwitchState                      = 17301504,    // NISysCfgSwitchState
   NISysCfgIndexedPropertyInternalCalibrationName              = 17514496,    // char *
   NISysCfgIndexedPropertyInternalCalibrationLastTime          = 16846848,    // NISysCfgTimestampUTC
   NISysCfgIndexedPropertyInternalCalibrationLastTemp          = 16850944,    // double

   // Read/Write properties
   NISysCfgIndexedPropertyUserLedState                         = 17289216,    // NISysCfgLedState

   // Read-only properties
   NISysCfgIndexedPropertyExpertName                           = 16900096,    // char *
   NISysCfgIndexedPropertyExpertResourceName                   = 16896000,    // char *
   NISysCfgIndexedPropertyExpertUserAlias                      = 16904192     // char *
} NISysCfgIndexedProperty;

typedef enum
{
   // Read-only properties
   NISysCfgSystemPropertyDeviceClass                           = 16941057,    // char *
   NISysCfgSystemPropertyProductId                             = 16941058,    // int
   NISysCfgSystemPropertyFileSystem                            = 16941060,    // NISysCfgFileSystemMode
   NISysCfgSystemPropertyFirmwareRevision                      = 16941061,    // char *
   NISysCfgSystemPropertyIsFactoryResetSupported               = 16941067,    // NISysCfgBool
   NISysCfgSystemPropertyIsFirmwareUpdateSupported             = 16941068,    // NISysCfgBool
   NISysCfgSystemPropertyIsLocked                              = 16941069,    // NISysCfgBool
   NISysCfgSystemPropertyIsLockingSupported                    = 16941070,    // NISysCfgBool
   NISysCfgSystemPropertyIsOnLocalSubnet                       = 16941072,    // NISysCfgBool
   NISysCfgSystemPropertyIsRestartSupported                    = 16941076,    // NISysCfgBool
   NISysCfgSystemPropertyMacAddress                            = 16941077,    // char *
   NISysCfgSystemPropertyProductName                           = 16941078,    // char *
   NISysCfgSystemPropertyOperatingSystem                       = 16941079,    // char *
   NISysCfgSystemPropertyOperatingSystemVersion                = 17100800,    // char *
   NISysCfgSystemPropertyOperatingSystemDescription            = 17104896,    // char *
   NISysCfgSystemPropertySerialNumber                          = 16941080,    // char *
   NISysCfgSystemPropertySystemState                           = 16941082,    // char *
   NISysCfgSystemPropertyMemoryPhysTotal                       = 219480064,   // double
   NISysCfgSystemPropertyMemoryPhysFree                        = 219484160,   // double
   NISysCfgSystemPropertyMemoryLargestBlock                    = 219488256,   // double
   NISysCfgSystemPropertyMemoryVirtTotal                       = 219492352,   // double
   NISysCfgSystemPropertyMemoryVirtFree                        = 219496448,   // double
   NISysCfgSystemPropertyPrimaryDiskTotal                      = 219291648,   // double
   NISysCfgSystemPropertyPrimaryDiskFree                       = 219295744,   // double
   NISysCfgSystemPropertySystemResourceHandle                  = 16941086,    // NISysCfgResourceHandle
   NISysCfgSystemPropertyImageDescription                      = 219516928,   // char *
   NISysCfgSystemPropertyImageId                               = 219521024,   // char *
   NISysCfgSystemPropertyImageTitle                            = 219525120,   // char *
   NISysCfgSystemPropertyImageVersion                          = 219529216,   // char *
   NISysCfgSystemPropertyInstalledApiVersion                   = 16941087,    // char *

   // Read/Write properties
   NISysCfgSystemPropertyIsDst                                 = 16941066,    // NISysCfgBool
   NISysCfgSystemPropertyIsRestartProtected                    = 16941073,    // NISysCfgBool
   NISysCfgSystemPropertyHaltOnError                           = 16941074,    // NISysCfgBool
   NISysCfgSystemPropertyRepositoryLocation                    = 16941084,    // char *
   NISysCfgSystemPropertySystemComment                         = 16941081,    // char *
   NISysCfgSystemPropertyAutoRestartTimeout                    = 16941085,    // unsigned int

   // Read/Write network adapter properties
   NISysCfgSystemPropertyDnsServer                             = 16941059,    // char *
   NISysCfgSystemPropertyGateway                               = 16941062,    // char *
   NISysCfgSystemPropertyHostname                              = 16941063,    // char *
   NISysCfgSystemPropertyIpAddress                             = 16941064,    // char *
   NISysCfgSystemPropertyIpAddressMode                         = 16941065,    // NISysCfgIpAddressMode
   NISysCfgSystemPropertySubnetMask                            = 16941083     // char *
} NISysCfgSystemProperty;

typedef enum
{
   // Write-only properties
   NISysCfgFilterPropertyIsDevice                              = 16781312,    // NISysCfgBool
   NISysCfgFilterPropertyIsChassis                             = 16941056,    // NISysCfgBool
   NISysCfgFilterPropertyServiceType                           = 17014784,    // NISysCfgServiceType
   NISysCfgFilterPropertyConnectsToBusType                     = 16785408,    // NISysCfgBusType
   NISysCfgFilterPropertyConnectsToLinkName                    = 16818176,    // char *
   NISysCfgFilterPropertyProvidesBusType                       = 16932864,    // NISysCfgBusType
   NISysCfgFilterPropertyVendorId                              = 16789504,    // unsigned int
   NISysCfgFilterPropertyProductId                             = 16797696,    // unsigned int
   NISysCfgFilterPropertySerialNumber                          = 16805888,    // char *
   NISysCfgFilterPropertyIsNIProduct                           = 16809984,    // NISysCfgBool
   NISysCfgFilterPropertyIsSimulated                           = 16814080,    // NISysCfgBool
   NISysCfgFilterPropertySlotNumber                            = 16822272,    // int
   NISysCfgFilterPropertyHasDriver                             = 16920576,    // NISysCfgHasDriverType
   NISysCfgFilterPropertyIsPresent                             = 16924672,    // NISysCfgIsPresentType
   NISysCfgFilterPropertySupportsCalibration                   = 16908288,    // NISysCfgBool
   NISysCfgFilterPropertySupportsFirmwareUpdate                = 17080320,    // NISysCfgBool
   NISysCfgFilterPropertyProvidesLinkName                      = 16936960,    // char *
   NISysCfgFilterPropertyExpertName                            = 16900096,    // char *
   NISysCfgFilterPropertyResourceName                          = 16896000,    // char *
   NISysCfgFilterPropertyUserAlias                             = 16904192     // char *
} NISysCfgFilterProperty;

typedef enum
{
   NISysCfgPropertyTypeBool         = 1,
   NISysCfgPropertyTypeInt          = 2,
   NISysCfgPropertyTypeUnsignedInt  = 3,
   NISysCfgPropertyTypeDouble       = 4,
   NISysCfgPropertyTypeString       = 6,
   NISysCfgPropertyTypeTimestamp    = 7,
} NISysCfgPropertyType;

// These macros are provided for backward compatibility.
#define NISysCfgBusTypeFlexAdapter                             NISysCfgBusTypeAccessory
#define NISysCfgFilterModeAll                                  NISysCfgFilterModeMatchValuesAll
#define NISysCfgFilterModeAny                                  NISysCfgFilterModeMatchValuesAny
#define NISysCfgFilterModeNone                                 NISysCfgFilterModeMatchValuesNone
#define NISysCfgPacketDetectionInterrupt                       NISysCfgPacketDetectionLineInterrupt
#define NISysCfgResourcePropertyWlanAvailableCount             NISysCfgResourcePropertyNumberOfDiscoveredAccessPoints
#define NISysCfgResetPrimaryDisableOthers                      NISysCfgResetPrimaryResetOthers
#define NISysCfgPreservePrimaryDisableOthers                   NISysCfgPreservePrimaryResetOthers
#define NISysCfgApplyPrimaryDisableOthers                      NISysCfgApplyPrimaryResetOthers

////////////////////////////////////////////////////////////////////////////////
// System Configuration core functions
////////////////////////////////////////////////////////////////////////////////

NISYSCFGCFUNC NISysCfgInitializeSession(
   const char *                           targetName,                // NULL or "" => localhost
   const char *                           username,                  // NULL or "" => no credentials
   const char *                           password,                  // NULL or "" => no credentials
   NISysCfgLocale                         language,                  // LCID or 0 to indicate default.
   NISysCfgBool                           forcePropertyRefresh,
   unsigned int                           connectTimeoutMsec,
   NISysCfgEnumExpertHandle *             expertEnumHandle,          // Can be NULL
   NISysCfgSessionHandle *                sessionHandle
   );

// This function is used to close a session or any other handle type returned by this API.
NISYSCFGCFUNC NISysCfgCloseHandle(
   void *                                 syscfgHandle
   );

NISYSCFGCFUNC NISysCfgGetSystemExperts(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           expertNames,               // NULL or "" => all experts
   NISysCfgEnumExpertHandle *             expertEnumHandle
   );

NISYSCFGCFUNC NISysCfgSetRemoteTimeout(
   NISysCfgSessionHandle                  sessionHandle,
   unsigned int                           remoteTimeoutMsec
   );

NISYSCFGCFUNC NISysCfgFindHardware(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgFilterMode                     filterMode,                // Ignored if filter handle is NULL
   NISysCfgFilterHandle                   filterHandle,              // Can be NULL
   const char *                           expertNames,               // NULL or "" => all experts
   NISysCfgEnumResourceHandle *           resourceEnumHandle
   );

NISYSCFGCFUNC NISysCfgFindSystems(
   NISysCfgSessionHandle                  sessionHandle,             // Can be NULL or a session to "localhost"
   const char *                           deviceClass,               // NULL or "" => all classes
   NISysCfgBool                           detectOnlineSystems,
   NISysCfgIncludeCachedResults           cacheMode,
   NISysCfgSystemNameFormat               findOutputMode,
   unsigned int                           timeoutMsec,
   NISysCfgBool                           onlyInstallableSystems,
   NISysCfgEnumSystemHandle *             systemEnumHandle
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgSelfTestHardware(
   NISysCfgResourceHandle                 resourceHandle,
   unsigned int                           mode,
   char **                                detailedResult
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgSelfCalibrateHardware(
   NISysCfgResourceHandle                 resourceHandle,
   char **                                detailedResult
   );

NISYSCFGCFUNC NISysCfgResetHardware(
   NISysCfgResourceHandle                 resourceHandle,
   unsigned int                           mode
   );

NISYSCFGCFUNC NISysCfgRenameResource(
   NISysCfgResourceHandle                 resourceHandle,
   const char *                           newName,
   NISysCfgBool                           overwriteConflict,
   NISysCfgBool                           updateDependencies,
   NISysCfgBool *                         nameAlreadyExisted,        // Can be NULL
   NISysCfgResourceHandle *               overwrittenResourceHandle  // Can be NULL
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgDeleteResource(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgDeleteValidationMode           mode,
   NISysCfgBool *                         dependentItemsDeleted,     // Can be NULL
   char **                                detailedResult
   );

NISYSCFGCFUNC NISysCfgGetResourceProperty(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgResourceProperty               propertyID,
   void *                                 value
   );

NISYSCFGCFUNC NISysCfgGetResourcePropertyType(
   NISysCfgResourceHandle                resourceHandle,
   NISysCfgResourceProperty              propertyID,
   NISysCfgPropertyType *                propertyType
   );

NISYSCFGCDECL NISysCfgSetResourceProperty(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgResourceProperty               propertyID,
   ...
   );

NISYSCFGCDECL NISysCfgSetResourcePropertyWithType(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgResourceProperty               propertyID,
   NISysCfgPropertyType                   propertyType,
   ...
   );

NISYSCFGCFUNC NISysCfgSetResourcePropertyV(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgResourceProperty               propertyID,
   va_list                                args
   );

NISYSCFGCFUNC NISysCfgSetResourcePropertyWithTypeV(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgResourceProperty               propertyID,
   NISysCfgPropertyType                   propertyType,
   va_list                                args
   );

NISYSCFGCFUNC NISysCfgGetResourceIndexedProperty(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgIndexedProperty                propertyID,
   unsigned int                           index,
   void *                                 value
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgSaveResourceChanges(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgBool *                         changesRequireRestart,
   char **                                detailedResult
   );

NISYSCFGCFUNC NISysCfgGetSystemProperty(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgSystemProperty                 propertyID,
   void *                                 value
   );

 NISYSCFGCFUNC NISysCfgGetSystemPropertyType(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgSystemProperty                 propertyID,
   NISysCfgPropertyType *                 propertyType
   );

NISYSCFGCDECL NISysCfgSetSystemProperty(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgSystemProperty                 propertyID,
   ...
   );

NISYSCFGCFUNC NISysCfgSetSystemPropertyV(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgSystemProperty                 propertyID,
   va_list                                args
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgSaveSystemChanges(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool *                         changesRequireRestart,
   char **                                detailedResult
   );

NISYSCFGCFUNC NISysCfgCreateFilter(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgFilterHandle *                 filterHandle
   );

NISYSCFGCDECL NISysCfgSetFilterProperty(
   NISysCfgFilterHandle                   filterHandle,
   NISysCfgFilterProperty                 propertyID,
   ...
   );

NISYSCFGCDECL NISysCfgSetFilterPropertyWithType(
   NISysCfgFilterHandle                   filterHandle,
   NISysCfgFilterProperty                 propertyID,
   NISysCfgPropertyType                   propertyType,
   ...
   );

NISYSCFGCFUNC NISysCfgSetFilterPropertyV(
   NISysCfgFilterHandle                   filterHandle,
   NISysCfgFilterProperty                 propertyID,
   va_list                                args
   );

NISYSCFGCFUNC NISysCfgSetFilterPropertyWithTypeV(
   NISysCfgFilterHandle                   filterHandle,
   NISysCfgFilterProperty                 propertyID,
   NISysCfgPropertyType                   propertyType,
   va_list                                args
   );

////////////////////////////////////////////////////////////////////////////////
// System Configuration firmware modification functions
////////////////////////////////////////////////////////////////////////////////

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgUpgradeFirmwareFromFile(
   NISysCfgResourceHandle                 resourceHandle,
   const char *                           firmwareFile,
   NISysCfgBool                           autoStopTasks,
   NISysCfgBool                           alwaysOverwrite,
   NISysCfgBool                           waitForOperationToFinish,
   NISysCfgFirmwareStatus *               firmwareStatus,
   char **                                detailedResult
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgUpgradeFirmwareVersion(
   NISysCfgResourceHandle                 resourceHandle,
   const char *                           firmwareVersion,
   NISysCfgBool                           autoStopTasks,
   NISysCfgBool                           alwaysOverwrite,
   NISysCfgBool                           waitForOperationToFinish,
   NISysCfgFirmwareStatus *               firmwareStatus,
   char **                                detailedResult
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgEraseFirmware(
   NISysCfgResourceHandle                 resourceHandle,
   NISysCfgBool                           autoStopTasks,
   NISysCfgFirmwareStatus *               firmwareStatus,
   char **                                detailedResult
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgCheckFirmwareStatus(
   NISysCfgResourceHandle                 resourceHandle,
   int *                                  percentComplete,
   NISysCfgFirmwareStatus *               firmwareStatus,
   char **                                detailedResult
   );

////////////////////////////////////////////////////////////////////////////////
// System Configuration software and installation functions
////////////////////////////////////////////////////////////////////////////////

NISYSCFGCFUNC NISysCfgFormat(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           forceSafeMode,
   NISysCfgBool                           restartAfterFormat,
   NISysCfgFileSystemMode                 fileSystem,
   NISysCfgNetworkInterfaceSettings       networkSettings,
   unsigned int                           timeoutMsec
   );

NISYSCFGCFUNC NISysCfgFormatWithBaseSystemImage(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   NISysCfgFileSystemMode                 fileSystem,
   NISysCfgNetworkInterfaceSettings       networkSettings,
   const char *                           systemImageID,
   const char *                           systemImageVersion,
   unsigned int                           timeoutMsec
   );

NISYSCFGCFUNC NISysCfgRestart(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           waitForRestartToFinish,
   NISysCfgBool                           installMode,
   NISysCfgBool                           flushDNS,
   unsigned int                           timeoutMsec,
   char                                   newIpAddress[]
   );

NISYSCFGCFUNC NISysCfgGetAvailableSoftwareComponents(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgIncludeComponentTypes          itemTypes,
   NISysCfgEnumSoftwareComponentHandle *  componentEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetAvailableSoftwareSets(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgEnumSoftwareSetHandle *        setEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetAvailableBaseSystemImages(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgEnumSoftwareComponentHandle*   systemImageEnumHandle
);

NISYSCFGCFUNC NISysCfgGetFilteredSoftwareComponents(
   const char *                           repositoryPath,
   const char *                           deviceClass,
   const char *                           operatingSystem,
   unsigned int                           productID,
   NISysCfgIncludeComponentTypes          itemTypes,
   NISysCfgEnumSoftwareComponentHandle *  componentEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetFilteredSoftwareSets(
   const char *                           repositoryPath,
   const char *                           deviceClass,
   const char *                           operatingSystem,
   unsigned int                           productID,
   NISysCfgEnumSoftwareSetHandle *        setEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetFilteredBaseSystemImages(
   const char *                           repositoryPath,
   const char *                           deviceClass,
   const char *                           operatingSystem,
   unsigned int                           productID,
   NISysCfgEnumSoftwareComponentHandle *  systemImageEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetInstalledSoftwareComponents(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgIncludeComponentTypes          itemTypes,
   NISysCfgBool                           cached,
   NISysCfgEnumSoftwareComponentHandle *  componentEnumHandle
   );

NISYSCFGCFUNC NISysCfgGetInstalledSoftwareSet(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           cached,
   NISysCfgSoftwareSetHandle *            setHandle
   );

NISYSCFGCFUNC NISysCfgGetSystemImageAsFolder(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           destinationFolder,
   const char *                           encryptionPassphrase,
   NISysCfgBool                           overwriteIfExists,
   NISysCfgBool                           installedSoftwareOnly,
   NISysCfgBool                           autoRestart
   );

NISYSCFGCFUNC NISysCfgGetSystemImageAsFolder2(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   const char *                           destinationFolder,
   const char *                           encryptionPassphrase,
   unsigned int                           numBlacklistEntries,
   const char **                          blacklistFilesDirectories, // Can be NULL if numBlacklistEntries==0
   NISysCfgBool                           overwriteIfExists,
   NISysCfgBool                           installedSoftwareOnly
   );

NISYSCFGCFUNC NISysCfgCreateSystemImageAsFolder(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           imageTitle,
   const char *                           imageID,
   const char *                           imageVersion,
   const char *                           imageDescription,
   NISysCfgBool                           autoRestart,
   const char *                           destinationFolder,
   const char *                           encryptionPassphrase,
   unsigned int                           numBlacklistEntries,
   const char **                          blacklistFilesDirectories, // Can be NULL if numBlacklistEntries==0
   NISysCfgBool                           overwriteIfExists
   );

NISYSCFGCFUNC NISysCfgSetSystemImageFromFolder(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           sourceFolder,
   const char *                           encryptionPassphrase,
   NISysCfgBool                           autoRestart,
   NISysCfgBool                           originalSystemOnly
   );

NISYSCFGCFUNC NISysCfgSetSystemImageFromFolder2(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   const char *                           sourceFolder,
   const char *                           encryptionPassphrase,
   unsigned int                           numBlacklistEntries,
   const char **                          blacklistFilesDirectories, // Can be NULL if numBlacklistEntries==0
   NISysCfgBool                           originalSystemOnly,
   NISysCfgNetworkInterfaceSettings       networkSettings
   );

NISYSCFGCFUNC NISysCfgInstallAll(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   NISysCfgBool                           deselectConflicts,
   NISysCfgEnumSoftwareComponentHandle *  installedComponentEnumHandle,
   NISysCfgEnumDependencyHandle *         brokenDependencyEnumHandle
   );

NISYSCFGCFUNC NISysCfgInstallUninstallComponents(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   NISysCfgBool                           autoSelectDependencies,
   NISysCfgEnumSoftwareComponentHandle    componentToInstallEnumHandle,
   unsigned int                           numComponentsToUninstall,
   const char **                          componentIDsToUninstall,   // Can be NULL if numComponentsToUninstall==0
   NISysCfgEnumDependencyHandle*          brokenDependencyEnumHandle
   );

NISYSCFGCFUNC NISysCfgInstallUninstallComponents2(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   NISysCfgBool                           autoSelectDependencies,
   NISysCfgBool                           autoSelectRecommends,
   NISysCfgEnumSoftwareComponentHandle    componentToInstallEnumHandle,
   unsigned int                           numComponentsToUninstall,
   const char **                          componentIDsToUninstall,   // Can be NULL if numComponentsToUninstall==0
   NISysCfgEnumDependencyHandle*          brokenDependencyEnumHandle
);

NISYSCFGCFUNC NISysCfgInstallSoftwareSet(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   const char *                           softwareSetID,
   const char *                           version,
   NISysCfgEnumSoftwareComponentHandle    addonEnumHandle,
   NISysCfgEnumDependencyHandle *         brokenDependencyEnumHandle
   );

NISYSCFGCFUNC NISysCfgInstallStartup(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart,
   NISysCfgEnumSoftwareComponentHandle    startupEnumHandle,
   NISysCfgBool                           uninstallConflicts,
   NISysCfgEnumSoftwareComponentHandle *  installedComponentEnumHandle,
   NISysCfgEnumSoftwareComponentHandle *  uninstalledComponentEnumHandle,
   NISysCfgEnumDependencyHandle *         brokenDependencyEnumHandle
   );

NISYSCFGCFUNC NISysCfgUninstallAll(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgBool                           autoRestart
   );

NISYSCFGCFUNC NISysCfgGetSoftwareFeeds(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgEnumSoftwareFeedHandle *       feedEnumHandle
   );

NISYSCFGCFUNC NISysCfgAddSoftwareFeed(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           feedName,
   const char *                           uri,
   NISysCfgBool                           enabled,
   NISysCfgBool                           trusted
   );

NISYSCFGCFUNC NISysCfgModifySoftwareFeed(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           feedName,
   const char *                           newFeedName,
   const char *                           uri,
   NISysCfgBool                           enabled,
   NISysCfgBool                           trusted
   );

NISYSCFGCFUNC NISysCfgRemoveSoftwareFeed(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           feedName
   );

////////////////////////////////////////////////////////////////////////////////
// System Configuration enumerators and utility functions
////////////////////////////////////////////////////////////////////////////////

NISYSCFGCFUNC NISysCfgChangeAdministratorPassword(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           newPassword
   );

NISYSCFGCFUNC NISysCfgExportConfiguration(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           destinationFile,
   const char *                           expertNames,               // NULL or "" => all experts
   NISysCfgBool                           overwriteIfExists
   );

// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgImportConfiguration(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           sourceFile,
   const char *                           expertNames,               // NULL or "" => all experts
   NISysCfgImportMode                     importMode,
   char **                                detailedResult
   );

NISYSCFGCFUNC NISysCfgGenerateMAXReport(
   NISysCfgSessionHandle                  sessionHandle,
   const char *                           outputFilename,
   NISysCfgReportType                     reportType,
   NISysCfgBool                           overwriteIfExists
   );

NISYSCFGCFUNC NISysCfgCreateComponentsEnum(
   NISysCfgEnumSoftwareComponentHandle *  componentEnumHandle
   );

NISYSCFGCFUNC NISysCfgAddComponentToEnum(
   NISysCfgEnumSoftwareComponentHandle    componentEnumHandle,
   const char *                           ID,
   const char *                           version,
   NISysCfgVersionSelectionMode           mode
   );

NISYSCFGCFUNC NISysCfgFreeDetailedString(
   char                                   str[]
   );

NISYSCFGCFUNC NISysCfgNextResource(
   NISysCfgSessionHandle                  sessionHandle,
   NISysCfgEnumResourceHandle             resourceEnumHandle,
   NISysCfgResourceHandle *               resourceHandle
   );

NISYSCFGCFUNC NISysCfgNextSystemInfo(
   NISysCfgEnumSystemHandle               systemEnumHandle,
   char                                   system[]
   );

NISYSCFGCFUNC NISysCfgNextExpertInfo(
   NISysCfgEnumExpertHandle               expertEnumHandle,
   char                                   expertName[],
   char                                   displayName[],
   char                                   version[]
   );

// Caller should free detailedDescription using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgNextComponentInfo(
   NISysCfgEnumSoftwareComponentHandle    componentEnumHandle,
   char                                   ID[],
   char                                   version[],
   char                                   title[],
   NISysCfgComponentType *                itemType,
   char **                                detailedDescription
   );

NISYSCFGCFUNC NISysCfgNextSoftwareSet(
   NISysCfgEnumSoftwareSetHandle          setEnumHandle,
   NISysCfgSoftwareSetHandle *            setHandle
   );

// Caller should free detailedDescription using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgGetSoftwareSetInfo(
   NISysCfgSoftwareSetHandle              setHandle,
   NISysCfgIncludeComponentTypes          itemTypes,
   NISysCfgBool                           includeAddOnDeps,
   char                                   ID[],
   char                                   version[],
   char                                   title[],
   NISysCfgComponentType *                setType,
   char **                                detailedDescription,
   NISysCfgEnumSoftwareComponentHandle *  addOnEnumHandle,
   NISysCfgEnumSoftwareComponentHandle *  itemEnumHandle
   );

// Caller should free dependerDetailedDescription and dependeeDetailedDescription using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgNextDependencyInfo(
   NISysCfgEnumDependencyHandle           dependencyEnumHandle,
   char                                   dependerID[],
   char                                   dependerVersion[],
   char                                   dependerTitle[],
   char **                                dependerDetailedDescription,
   char                                   dependeeID[],
   char                                   dependeeVersion[],
   char                                   dependeeTitle[],
   char **                                dependeeDetailedDescription
   );

NISYSCFGCFUNC NISysCfgNextSoftwareFeed(
   NISysCfgEnumSoftwareFeedHandle         feedEnumHandle,
   char                                   feedName[],
   char                                   uri[],
   NISysCfgBool *                         enabled,
   NISysCfgBool *                         trusted
   );

NISYSCFGCFUNC NISysCfgResetEnumeratorGetCount(
   void *                                 enumHandle,
   unsigned int *                         count
   );

// Helper method to get the status string for a given status code.
// Caller should free detailedResult using NISysCfgFreeDetailedString.
NISYSCFGCFUNC NISysCfgGetStatusDescription(
   NISysCfgSessionHandle                  sessionHandle,              // Can be NULL
   NISysCfgStatus                         status,
   char **                                detailedDescription
   );

NISYSCFGCFUNC NISysCfgTimestampFromValues(
   NISysCfgUInt64                         secondsSinceEpoch1970,
   double                                 fractionalSeconds,
   NISysCfgTimestampUTC *                 timestamp
   );

NISYSCFGCFUNC NISysCfgValuesFromTimestamp(
   const NISysCfgTimestampUTC *           timestamp,
   NISysCfgUInt64 *                       secondsSinceEpoch1970,
   double *                               fractionalSeconds
   );

#ifdef __cplusplus
}
#endif

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nisyscfg_errors.h sha256=d9f257ce862494a1d0e3729d5e0ca9f0275371c2ce7eacfc0b89ea164b39af83 bytes=29541 -->
## FILE: imports/include/nisyscfg_errors.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nisyscfg_errors.h`
- sha256: `d9f257ce862494a1d0e3729d5e0ca9f0275371c2ce7eacfc0b89ea164b39af83`
- bytes: 29541

````c
/*============================================================================*/
/*                       NI System Configuration API                          */
/*----------------------------------------------------------------------------*/
/*    Copyright (c) National Instruments 2010-2022.  All Rights Reserved.     */
/*----------------------------------------------------------------------------*/
/*                                                                            */
/* Title:   nisyscfg_errors.h                                                 */
/* Purpose: Error codes for NI System Configuration API                       */
/*                                                                            */
/*============================================================================*/

#if !defined(_NI_SYSTEM_CONFIG_ERRORS_H_)
  #define _NI_SYSTEM_CONFIG_ERRORS_H_

/**************************************************************************/
/* Status codes.                                                          */
/**************************************************************************/

  #define NISysCfg_Succeeded(status) ((status) >= 0) /* Check if the status indicates success */
  #define NISysCfg_Failed(status) ((status) < 0)     /* Check if the status indicates failure */

typedef enum {
  // Common success codes
  NISysCfg_OK = 0L,                             /* The operation succeeded. */
  NISysCfg_EndOfEnum = 1L,                      /* Reached end of the enumeration. Used by the NISysCfgNext* functions. */
  NISysCfg_SelfTestBasicOnly = 263024L,         /* 0x00040370: The expert performed a basic self-test because it does not implement the specified mode. */
  NISysCfg_FoundCachedOfflineSystem = 263168L,  /* 0x00040400: Initialization succeeded but the target is offline. Only cached system properties are available. */
  NISysCfg_RestartLocalhostInitiated = 263169L, /* 0x00040401: For the local system, the option to wait until the restart is complete is ignored. The function has successfully initiated a restart with the operating system. */
  NISysCfg_ChangedPropertyNotSaved = 263170L,   /* 0x00040402: The requested property value was changed in this session but the change was not successfully validated and saved. */

  // Common error codes
  NISysCfg_NotImplemented = -2147467263L,    /* 0x80004001: This operation is not implemented for this target or resource. */
  NISysCfg_NullPointer = -2147467261L,       /* 0x80004003: A required pointer parameter was NULL. */
  NISysCfg_Fail = -2147467259L,              /* 0x80004005: Miscellaneous operation failure. */
  NISysCfg_Unexpected = -2147418113L,        /* 0x8000FFFF: A critical unexpected error occurred. Please report this to NI. */
  NISysCfg_OutOfMemory = -2147024882L,       /* 0x8007000E: Out of memory. */
  NISysCfg_InvalidArg = -2147024809L,        /* 0x80070057: Some parameter is invalid. */
  NISysCfg_OperationTimedOut = -2147220448L, /* 0x80040420: The operation timed out. */
  NISysCfg_FileNotFound = -2147220322L,      /* 0x8004049E: The specified file was not found. */
  NISysCfg_InvalidMACFormat = -2147220278L,  /* 0x800404CA: Unsupported MAC address format. Supply the MAC address as a colon separated string of characters instead of Hex display. */

  // 'Hardware' and 'Resource' functions
  NISysCfg_PropMismatch = -2147220624L,                  /* 0x80040370: The property already exists with a different type or value. */
  NISysCfg_PropDoesNotExist = -2147220623L,              /* 0x80040371: The property does not exist for this resource. */
  NISysCfg_UriIllegalSyntax = -2147220622L,              /* 0x80040372: The name of the target or expert contains illegal characters or has an invalid format. Each label of the hostname must be between 1 and 63 characters long, and the entire hostname, including delimiting dots, must be 255 characters or less. */
  NISysCfg_UriTargetDoesNotExist = -2147220621L,         /* 0x80040373: Could not contact the NI System Configuration API at the specified target address. Ensure that the system is online. */
  NISysCfg_UriExpertDoesNotExist = -2147220620L,         /* 0x80040374: A specified expert is not installed. */
  NISysCfg_ItemDoesNotExist = -2147220619L,              /* 0x80040375: The specified resource name does not exist. */
  NISysCfg_InvalidMode = -2147220618L,                   /* 0x80040376: The specified mode is invalid. */
  NISysCfg_SysConfigAPINotInstalled = -2147220616L,      /* 0x80040378: The NI System Configuration API is not installed on the specified target. */
  NISysCfg_NameSyntaxIllegal = -2147220614L,             /* 0x8004037A: The suggested name contains illegal characters. */
  NISysCfg_NameCollision = -2147220613L,                 /* 0x8004037B: Another resource already has the suggested name. */
  NISysCfg_NoPropValidated = -2147220612L,               /* 0x8004037C: None of the changed properties could be validated. */
  NISysCfg_UriUnauthorized = -2147220611L,               /* 0x8004037D: The current user does not have permission for the requested operation. */
  NISysCfg_RenameResourceDependencies = -2147220610L,    /* 0x8004037E: The resource being renamed has dependencies, and the 'updateDependencies' flag was false. */
  NISysCfg_ValueInvalid = -2147220609L,                  /* 0x8004037F: A property contained a value that is not valid or is out of range. */
  NISysCfg_ValuesInconsistent = -2147220608L,            /* 0x80040380: Multiple properties contained values that are inconsistent with each other. */
  NISysCfg_Canceled = -2147220607L,                      /* 0x80040381: The operation was canceled. */
  NISysCfg_ResponseSyntax = -2147220606L,                /* 0x80040382: Could not parse the response from the NI System Configuration API at the specified target address. */
  NISysCfg_ResourceIsNotPresent = -2147220605L,          /* 0x80040383: The resource name is valid but the operation requires the resource to be present. */
  NISysCfg_ResourceIsSimulated = -2147220604L,           /* 0x80040384: The resource name is valid but the operation is not supported on simulated resources. */
  NISysCfg_NotInFirmwareUpdateState = -2147220603L,      /* 0x80040385: The resource requires being in the firmware update state to perform this operation. */
  NISysCfg_FirmwareImageDeviceMismatch = -2147220602L,   /* 0x80040386: The uploaded firmware image does not work with this resource. */
  NISysCfg_FirmwareImageCorrupt = -2147220601L,          /* 0x80040387: The uploaded firmware image is corrupt or incomplete. */
  NISysCfg_InvalidFirmwareVersion = -2147220600L,        /* 0x80040388: The specified firmware version does not exist. */
  NISysCfg_OlderFirmwareVersion = -2147220599L,          /* 0x80040389: The specified firmware version is older than what is currently installed. */
  NISysCfg_InvalidLoginCredentials = -2147220598L,       /* 0x8004038A: The username or password is incorrect. */
  NISysCfg_FirmwareUpdateAttemptFailed = -2147220597L,   /* 0x8004038B: The specified firmware was not successfully installed. See the output parameters for more information. */
  NISysCfg_EncryptionFailed = -2147220596L,              /* 0x8004038C: The data could not be encrypted. */
  NISysCfg_SomePropsNotValidated = -2147220595L,         /* 0x8004038D: The changes were not saved. Some of the modified properties were not validated because they do not apply to this item. */
  NISysCfg_InvalidCalibrationCredentials = -2147220594L, /* 0x8004038E: The calibration password is incorrect. */
  NISysCfg_CannotDeletePresentResource = -2147220593L,   /* 0x8004038F: Could not delete the specified resource because it is present. */
  NISysCfg_UriTargetTransmitError = -2147220592L,        /* 0x80040390: Failed transmitting data to or from the web server at the specified target address. */
  NISysCfg_DecryptionFailed = -2147220591L,              /* 0x80040391: The NI System Configuration API at the specified target address could not decrypt the data. */
  NISysCfg_FirmwareExpertVersionMismatch = -2147220590L, /* 0x80040392: The specified firmware requires a newer version of the expert than what is currently installed. */
  NISysCfg_AmbiguousImportAction = -2147220589L,         /* 0x80040393: There was uncertainty regarding what action to take during an import. */
  NISysCfg_RequiredItemFailedImport = -2147220588L,      /* 0x80040394: A required item could not be imported. */
  NISysCfg_ItemInUse = -2147220587L,                     /* 0x80040395: Could not perform the specified operation because the item is currently in use. */
  NISysCfg_ItemTypeNotSupported = -2147220586L,          /* 0x80040396: Could not perform the specified operation because the item type is unknown or not supported. */

  // 'Report' functions
  NISysCfg_PermissionDenied = -2147220560L,   /* 0x800403B0: Unable to write to file or folder. Permission denied. */
  NISysCfg_SystemNotFound = -2147220559L,     /* 0x800403B1: Unable to connect to the specified system. Ensure that the system is online. */
  NISysCfg_TransformFailed = -2147220558L,    /* 0x800403B2: Error running transform to generate report. */
  NISysCfg_NotInstalled = -2147220557L,       /* 0x800403B3: Unable to find MAX on the system. Please reinstall. */
  NISysCfg_LaunchFailure = -2147220556L,      /* 0x800403B4: Unexpected error launching nimax.exe. */
  NISysCfg_InternalTimeout = -2147220555L,    /* 0x800403B5: Launched nimax.exe but it did not complete in a reasonable time. */
  NISysCfg_MissingTransform = -2147220554L,   /* 0x800403B6: Unable to find an XSL transform to generate the report. */
  NISysCfg_IncorrectExtension = -2147220553L, /* 0x800403B7: Incorrect report file extension provided. */
  NISysCfg_FileReadOnly = -2147220552L,       /* 0x800403B8: Report file is read-only. Unable to generate report. */
  NISysCfg_ReportOverwrite = -2147220551L,    /* 0x800403B9: Report file already exists, but overwriting is not enabled. Specify overwrite to replace the report file. */
  NISysCfg_DirectoryError = -2147220550L,     /* 0x800403BA: Error creating directory for report files. */

  // 'Export' and 'Import' functions
  NISysCfg_CannotOpenFile = -2147220480L,              /* 0x80040400: Error opening a file. */
  NISysCfg_InsufficientPermissions = -2147220479L,     /* 0x80040401: The object cannot be accessed because of insufficient permissions. */
  NISysCfg_NCECopierFailed = -2147220478L,             /* 0x80040402: Error with the object copier. */
  NISysCfg_FileOperationFailed = -2147220477L,         /* 0x80040403: Error performing a file operation. */
  NISysCfg_NameCollisionError = -2147220476L,          /* 0x80040404: Names from one expert have collided with another expert. */
  NISysCfg_UnexpectedError = -2147220475L,             /* 0x80040405: Unexpected error has occurred. */
  NISysCfg_NCENoStreamError = -2147220474L,            /* 0x80040406: The expert requested its stream for import but one does not exist because it did not export a stream. */
  NISysCfg_NCECompressionError = -2147220473L,         /* 0x80040407: Error compressing or decompressing file. */
  NISysCfg_NCEStreamReadError = -2147220472L,          /* 0x80040408: Error reading from a stream. */
  NISysCfg_NCEStreamWriteError = -2147220471L,         /* 0x80040409: Error writing to a stream. */
  NISysCfg_NCEStreamSeekError = -2147220470L,          /* 0x8004040A: Error seeking to a position in a stream. */
  NISysCfg_NCERepoNotReady = -2147220469L,             /* 0x8004040B: Repository not ready to be exported. */
  NISysCfg_NCERepoInvalid = -2147220468L,              /* 0x8004040C: The file or stream from which to import the repository is not a valid repository. */
  NISysCfg_NCERepoIncompat = -2147220467L,             /* 0x8004040D: The repository was exported with a newer version of MAX than what is on the importing machine. */
  NISysCfg_NCENoImportStorage = -2147220466L,          /* 0x8004040E: The import storage could not be opened. */
  NISysCfg_NCENoExportStorage = -2147220465L,          /* 0x8004040F: The export storage could not be created. */
  NISysCfg_NCENoObjCopier = -2147220464L,              /* 0x80040410: The object copier could not be created. */
  NISysCfg_CopyInProgress = -2147220463L,              /* 0x80040411: A PortCfg operation is already in progress. */
  NISysCfg_FileNotRecognized = -2147220462L,           /* 0x80040412: The custom file does not belong to a given expert. */
  NISysCfg_SystemNotSupported = -2147220461L,          /* 0x80040413: A specified system is not supported by this expert. */
  NISysCfg_SystemNotReachable = -2147220460L,          /* 0x80040414: A specified system is presumably supported, but network errors prevent connection. */
  NISysCfg_ProductSoftwareNotInstalled = -2147220459L, /* 0x80040415: The product is not installed on the specified system. */
  NISysCfg_ProductSoftwareTooOld = -2147220458L,       /* 0x80040416: The product is installed on the remote system, but is too old. */
  NISysCfg_ProductSoftwareTooNew = -2147220457L,       /* 0x80040417: The product is installed on the remote system, but is too new. */
  NISysCfg_DataTooOld = -2147220456L,                  /* 0x80040418: The import data is too old. The product is not backward-compatible with this data. */
  NISysCfg_DataTooNew = -2147220455L,                  /* 0x80040419: The import data is too new. The product is not forward-compatible with this data. */
  NISysCfg_NoItemsToCopy = -2147220454L,               /* 0x8004041A: The operation failed because no source items were specified. */
  NISysCfg_OrphanItems = -2147220453L,                 /* 0x8004041B: The operation failed because some items were orphans. */
  NISysCfg_DirtyItems = -2147220452L,                  /* 0x8004041C: The operation failed because some items were in-edit and not saved. */
  NISysCfg_FileOverwrite = -2147220451L,               /* 0x8004041D: The operation failed because it would overwrite a file. */
  NISysCfg_ItemOverwrite = -2147220450L,               /* 0x8004041E: The operation failed because it would overwrite items. */
  NISysCfg_MissingDependency = -2147220449L,           /* 0x8004041F: The operation failed because of missing dependency items. */
  NISysCfg_OperationCanceled = -2147220447L,           /* 0x80040421: The operation was canceled by the client. */
  NISysCfg_WarningConflicts = -2147220446L,            /* 0x80040422: The operation failed because of warning conflicts. */
  NISysCfg_ErrorConflicts = -2147220445L,              /* 0x80040423: The operation failed because of general conflicts. */
  NISysCfg_ItemsRequireUserInput = -2147220444L,       /* 0x80040424: The operation failed because of unresolved conflicts requiring user input. */
  NISysCfg_ProductExpertNotReady = -2147220443L,       /* 0x80040425: An expert is not ready to accept the specified source or destination, but may become ready in the future. */
  NISysCfg_OrphanFiles = -2147220442L,                 /* 0x80040426: The operation failed because some files were orphans. */
  NISysCfg_IsConst = -2147220441L,                     /* 0x80040427: Caller called a non-const method on an object that is logically const. */
  NISysCfg_UnsupportedProductMode = -2147220440L,      /* 0x80040428: An expert does not support the attempted copy mode (e.g. merge to file, etc.). */

  // 'System' functions
  NISysCfg_BootFlowMigrationNotSupported = -2147220388L, /* 0x8004045C: The image you are applying is not supported by the boot flow installed on the target. Boot flow migration is not supported when running locally. */
  NISysCfg_BootFlowMigrationRequired = -2147220387L,     /* 0x8004045D: The image you are applying is not supported by the boot flow installed on the target. Make sure the target has access to ni.com or install boot flow migration support packages on the host. */
  NISysCfg_OperationRequiresAutoRestart = -2147220386L,  /* 0x8004045E: You must allow the target to reboot to perform the specified operation. */
  NISysCfg_HostSoftwareTooOld = -2147220385L,            /* 0x8004045F: The target requires newer functionality not supported by the software on your computer. Update NI System Configuration to the latest version to configure this target. See www.ni.com/r/rtconfigerror for more information. */
  NISysCfg_OpkgUpdateFeedFailure = -2147220384L,         /* 0x80040460: Running 'opkg update' failed to access at least one enabled feed. Consider disabling unnecessary feeds. */
  NISysCfg_FeedNotFound = -2147220383L,                  /* 0x80040461: The specified software feed was not found. */
  NISysCfg_FeedAlreadyExists = -2147220382L,             /* 0x80040462: Could not add the specified software feed because it already exists. */
  NISysCfg_InstallOptionNotSupported = -2147220381L,     /* 0x80040463: The target does not support one of the specified installation options. */
  NISysCfg_FirmwareTooOld = -2147220380L,                /* 0x80040464: The target does not include the functionality this operation requires. Update the firmware to the latest version. */
  NISysCfg_SoftwareTooOld = -2147220379L,                /* 0x80040465: The target does not include the functionality this operation requires. Update the software to the latest version. */
  NISysCfg_RequiresSSH = -2147220378L,                   /* 0x80040466: SSH must be enabled on the target. */
  NISysCfg_OpkgResponseSyntax = -2147220377L,            /* 0x80040467: Could not parse the response from opkg at the specified target address. */
  NISysCfg_WrongSoftwareSetType = -2147220376L,          /* 0x80040468: The specified software set is the wrong type for this operation. */
  NISysCfg_RequiresOpkg = -2147220375L,                  /* 0x80040469: The target requires using opkg to modify installed software. */
  NISysCfg_HDFormatEncryptNotSupported = -2147220374L,   /* 0x8004046A: Disk encryption is not supported by the target. */
  NISysCfg_HDFormatNoRecoveryKeyDevice = -2147220373L,   /* 0x8004046B: Could not find a device suitable for storing the encrypted disk recovery key. Format a USB drive with the appropriate filesystem label and insert it into the target. */
  NISysCfg_RestartLocalhostAmbiguous = -2147220372L,     /* 0x8004046C: To restart your system, either specify 'localhost' on the front panel for Session in, or call Initialize Session first. */
  NISysCfg_ImageInvalidCorrupt = -2147220371L,           /* 0x8004046D: The image is corrupt or the file type is invalid. */
  NISysCfg_SafeOrInstallModeRequired = -2147220370L,     /* 0x8004046E: Can only perform this action in safe or install mode, and the 'auto restart' flag was false. */
  NISysCfg_EncryptPhraseMismatch = -2147220369L,         /* 0x8004046F: The encryption passphrase when applying an image was not the same as when the image was created. */
  NISysCfg_InvalidIP = -2147220368L,                     /* 0x80040470: The IP address is invalid. */
  NISysCfg_InvalidGateway = -2147220367L,                /* 0x80040471: The gateway address is invalid. */
  NISysCfg_InvalidDNS = -2147220366L,                    /* 0x80040472: The DNS server address is invalid. */
  NISysCfg_InvalidSubnet = -2147220365L,                 /* 0x80040473: The subnet mask is invalid. */
  NISysCfg_CmdNotSupported = -2147220364L,               /* 0x80040474: Command is not supported by given protocol. */
  NISysCfg_ConfigFailed = -2147220363L,                  /* 0x80040475: Remote system replied with the failure to config command. */
  NISysCfg_Locked = -2147220362L,                        /* 0x80040476: Remote system is locked. Requires a password to configure. */
  NISysCfg_BadPassword = -2147220361L,                   /* 0x80040477: The password supplied for the operation is invalid. */
  NISysCfg_NotConfigurable = -2147220360L,               /* 0x80040478: The remote device is not configurable for some reason other than password. */
  NISysCfg_UnlockFailed = -2147220359L,                  /* 0x80040479: Failed to unlock the system. */
  NISysCfg_LockFailed = -2147220358L,                    /* 0x8004047A: Failed to lock the system. */
  NISysCfg_InstallFailed = -2147220357L,                 /* 0x8004047B: General installation failure. */
  NISysCfg_InstallationCorrupt = -2147220356L,           /* 0x8004047C: Installation component files were not found in the repository, or were corrupt. */
  NISysCfg_EmptyFile = -2147220355L,                     /* 0x8004047D: The installation file is empty. */
  NISysCfg_UnconfiguredIP = -2147220354L,                /* 0x8004047E: The system must have a valid IP address before certain operations such as installation. The IP address cannot be 0.0.0.0. */
  NISysCfg_InstallationGenericFailure = -2147220352L,    /* 0x80040480: General install error. */
  NISysCfg_DownloadAlreadyStarted = -2147220350L,        /* 0x80040482: Installation to the specified target has already started. Multiple simultaneous installations are not allowed. */
  NISysCfg_Aborted = -2147220349L,                       /* 0x80040483: Remote action aborted. */
  NISysCfg_DiskFull = -2147220338L,                      /* 0x8004048E: Hard drive on the remote system is either full or has encountered an I/O error. */
  NISysCfg_HDFormatFailed = -2147220337L,                /* 0x8004048F: Hard drive format failed. The disk on the target may be unrecoverable. */
  NISysCfg_HDFormatNotSafeMode = -2147220336L,           /* 0x80040490: System must be in safe mode before attempting a hard drive format. Restart the target into safe mode and attempt the command again. */
  NISysCfg_HDFormatRebootFailed = -2147220335L,          /* 0x80040491: System failed to restart after the hard drive was formatted. The system is in an unknown state. You may have to manually restart the target. */
  NISysCfg_ConnectionRefused = -2147220334L,             /* 0x80040492: The server refused the network connection. */
  NISysCfg_GetRemoteFilesFailed = -2147220331L,          /* 0x80040495: Failed to get one or more files while creating system image. The image is incomplete or invalid. */
  NISysCfg_PutRemoteFilesFailed = -2147220330L,          /* 0x80040496: Failed to put one or more files while applying system image. The system may be in a corrupt state. */
  NISysCfg_InvalidImage = -2147220329L,                  /* 0x80040497: The specified path does not contain a valid image. */
  NISysCfg_ImageDeviceCodeMismatch = -2147220328L,       /* 0x80040498: The image is for a different device class and is incompatible with the target. */
  NISysCfg_SystemMismatch = -2147220327L,                /* 0x80040499: The image was not originally created from the specified target. */
  NISysCfg_HDFormatWrongFS = -2147220326L,               /* 0x8004049A: The requested file system is not supported on the specified target. */
  NISysCfg_CustomInstallNotSupported = -2147220325L,     /* 0x8004049B: The specified target does not support custom software installations. */
  NISysCfg_FTPFailed = -2147220324L,                     /* 0x8004049C: A file transfer error (FTP or WebDAV) occurred. */
  NISysCfg_Timeout = -2147220323L,                       /* 0x8004049D: Operation timed out. */
  NISysCfg_DirNotFound = -2147220321L,                   /* 0x8004049F: The specified directory was not found. */
  NISysCfg_PathNotFound = -2147220320L,                  /* 0x800404A0: The specified file or directory path was not found. */
  NISysCfg_NoSoftwareAvailable = -2147220319L,           /* 0x800404A1: No software is available for installation to this target. */
  NISysCfg_OverwriteError = -2147220318L,                /* 0x800404A2: The file or directory exists and the overwrite flag was false. */
  NISysCfg_HDFormatCannotKeepCfg = -2147220317L,         /* 0x800404A3: The target was not formatted because the option to keep configuration after a format is supported only for targets on the local subnet. To format the target, repeat the operation without requesting to keep the configuration. */
  NISysCfg_FileOrPathTooLong = -2147220316L,             /* 0x800404A4: Filename or pathname is longer than what the server supports. */
  NISysCfg_DDPInternalTimeout = -2147220315L,            /* 0x800404A5: Failed when communicating with the system. This issue is usually caused by a high latency in the network. Refer to KnowledgeBase article 42GH3O00 on ni.com for possible solutions. */
  NISysCfg_IOPermissionDenied = -2147220314L,            /* 0x800404A6: The operation failed because of insufficient permissions. */
  NISysCfg_PathAlreadyExists = -2147220313L,             /* 0x800404A7: The operation failed because the path already exists. */
  NISysCfg_ExecutionFailure = -2147220312L,              /* 0x800404A8: The execution of an external command, script, or application failed. */
  NISysCfg_DownloadError = -2147220311L,                 /* 0x800404A9: Failed to download the file from the 'RT Images' repository. */
  NISysCfg_NetSendFailed = -2147220309L,                 /* 0x800404AB: Failed to send command. */
  NISysCfg_ContactHostDisconnected = -2147220308L,       /* 0x800404AC: Could not contact remote target. Ensure that the system is online. */
  NISysCfg_NetSvcDown = -2147220307L,                    /* 0x800404AD: Could not access network. */
  NISysCfg_NotConfirmed = -2147220306L,                  /* 0x800404AE: Command was not confirmed. The result of the operation is uncertain. */
  NISysCfg_HostNotResolved = -2147220305L,               /* 0x800404AF: Hostname could not be resolved by DNS. */
  NISysCfg_RebootTimeout = -2147220304L,                 /* 0x800404B0: Timeout while waiting for restart. The system is offline. */
  NISysCfg_NoConfirmationFP1600 = -2147220303L,          /* 0x800404B1: Sending new configuration operation returned a failure, but might not necessarily have failed. */
  NISysCfg_DuplicateStartup = -2147220300L,              /* 0x800404B4: Cannot install more than one startup component. */
  NISysCfg_RemoteInvalidArgument = -2147220299L,         /* 0x800404B5: Invalid argument passed. */
  NISysCfg_NotUninstallable = -2147220298L,              /* 0x800404B6: Cannot uninstall a specified software component from the target because there are dependencies. */
  NISysCfg_DuplicatesNotAllowed = -2147220297L,          /* 0x800404B7: Cannot install multiple packages of the same component. */
  NISysCfg_NotInstallable = -2147220296L,                /* 0x800404B8: Cannot install a specified software component to the target because there are dependencies. */
  NISysCfg_WrongDevice = -2147220295L,                   /* 0x800404B9: A specified software component is incompatible with this target. */
  NISysCfg_WrongOS = -2147220294L,                       /* 0x800404BA: A specified software component is incompatible with this target's operating system. */
  NISysCfg_OSVersionTooOld = -2147220293L,               /* 0x800404BB: A firmware update is required before installing. */
  NISysCfg_IOError = -2147220292L,                       /* 0x800404BC: Cannot open file or folder. */
  NISysCfg_CorruptConfig = -2147220291L,                 /* 0x800404BD: Duplicate or missing components on target installation. */
  NISysCfg_BufferOverflow = -2147220290L,                /* 0x800404BE: Buffer overflow. Size is too small. */
  NISysCfg_UnsupportedCDFVersion = -2147220289L,         /* 0x800404BF: The software installed on the target uses a CDF format not supported by the software on your computer. Update NI System Configuration or NI MAX to the latest version to configure this target. */
  NISysCfg_InvalidStack = -2147220288L,                  /* 0x800404C0: The specified software set or base system image cannot be installed to the target because it is invalid or cannot be found. */
  NISysCfg_IncompleteStack = -2147220287L,               /* 0x800404C1: The specified software set definition is incomplete and cannot be installed to the target. Some hidden dependencies were added. */
  NISysCfg_StackItemMissing = -2147220286L,              /* 0x800404C2: One or more Software Set items could not be found in the repository. */
  NISysCfg_TopLevelHiddenComponentError = -2147220285L,  /* 0x800404C3: There is a top-level hidden component installed. */
  NISysCfg_InvalidAddon = -2147220284L,                  /* 0x800404C4: A component was passed in that is not an installable add-on. It may be an unknown ID, a defined item that is not an add-on, a missing add-on, or a non-installable add-on. */
  NISysCfg_NoRTImagesFolder = -2147220283L,              /* 0x800404C5: Could not find or access 'RT Images' repository location. */
  NISysCfg_NoRTImagesRegistry = -2147220282L,            /* 0x800404C6: Could not read the 'RT Images' registry key. */
  NISysCfg_NoRTS2CDF = -2147220281L,                     /* 0x800404C7: Could not find the rts2cdf conversion utility. */
  NISysCfg_UnsupportedOS = -2147220280L,                 /* 0x800404C8: The operating system is not supported. */
  NISysCfg_ExactVersionRequired = -2147220279L,          /* 0x800404C9: Unspecified version while trying to install exact version of a component. */
  NISysCfg_InvalidStartup = -2147220277L                 /* 0x800404CB: A component was passed in that is not a startup. */
} NISysCfgStatus;

#endif  // _NI_SYSTEM_CONFIG_ERRORS_H_
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niTClk.h sha256=287644d75d43d6958c7983cb96d2ac5c74e05d72377d7dfc1912a8db9915abc3 bytes=21066 -->
## FILE: imports/include/niTClk.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niTClk.h`
- sha256: `287644d75d43d6958c7983cb96d2ac5c74e05d72377d7dfc1912a8db9915abc3`
- bytes: 21066

````c

/****************************************************************************
 *                                niTClk                                    *
 *--------------------------------------------------------------------------*
 *   Copyright (c) National Instruments 2003-2021.  All Rights Reserved.    *
 ****************************************************************************/

#ifndef ___niTClk_h___
#define ___niTClk_h___

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "IviVisaType.h"
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NITCLK_MAJOR_VERSION                                                                20      // Instrument driver major version
#define NITCLK_MINOR_VERSION                                                                7       // Instrument driver minor version
#define NITCLK_UPDATE_VERSION                                                               0       // Instrument driver update version


/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/
#define NITCLK_ATTR_SYNC_PULSE_SOURCE                                                       1       // 1 (0x1),    ViString
#define NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL                                     2       // 2 (0x2),    ViString
#define NITCLK_ATTR_START_TRIGGER_MASTER_SESSION                                            3       // 3 (0x3),    ViSession
#define NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION                                              4       // 4 (0x4),    ViSession
#define NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION                                           5       // 5 (0x5),    ViSession
#define NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION                                            6       // 6 (0x6),    ViSession
#define NITCLK_ATTR_TCLK_ACTUAL_PERIOD                                                      8       // 8 (0x8),    ViReal64,   read-only
#define NITCLK_ATTR_EXPORTED_TCLK_OUTPUT_TERMINAL                                           9       // 9 (0x9),    ViString
#define NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE                                                 10      // 10 (0xa),   ViString
#define NITCLK_ATTR_SAMPLE_CLOCK_DELAY                                                      11      // 11 (0xb),   ViReal64
#define NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE                                     13      // 13 (0xd),   ViString
#define NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION                                           16      // 16 (0x10),  ViSession
#define NITCLK_ATTR_CONDITIONAL_JUMP_TRIGGER_MASTER_SESSION                                 17      // 17 (0x11),  ViSession


/****************************************************************************
 *------------------ Attribute and Parameter Value Defines -----------------*
 ****************************************************************************/
// Values used in
//     niTClk_SynchronizeWithOptions
#define NITCLK_VAL_SYNCHRONIZE_OPTIONS_NONE                                                 0       // 0 (0x0)
#define NITCLK_VAL_SYNCHRONIZE_OPTIONS_ALLOW_TCLK_DRIFT                                     1       // 1 (0x1)

// Values used in
//     niTClk_FinishSyncPulseSenderSynchronizeWithAdjustmentType
#define NITCLK_VAL_ADJUSTMENT_TYPE_AUTO                                                     0       // 0 (0x0)
#define NITCLK_VAL_ADJUSTMENT_TYPE_TCLK_DIVISOR                                             1       // 1 (0x1)
#define NITCLK_VAL_ADJUSTMENT_TYPE_TCLK_TIMEBASE                                            2       // 2 (0x2)
#define NITCLK_VAL_ADJUSTMENT_TYPE_NONE                                                     3       // 3 (0x3)


/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/
ViStatus _VI_FUNC niTClk_ConfigureForHomogeneousTriggers(
   ViUInt32 sessionCount,
   const ViSession sessions[]);

ViStatus _VI_FUNC niTClk_Synchronize(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTclkPeriod);

ViStatus _VI_FUNC niTClk_Initiate(
   ViUInt32 sessionCount,
   const ViSession sessions[]);

ViStatus _VI_FUNC niTClk_WaitUntilDone(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 timeout);

ViStatus _VI_FUNC niTClk_GetExtendedErrorInfo(
   ViChar errorString[],
   ViUInt32 errorStringSize);

// -- Advanced Functions --
ViStatus _VI_FUNC niTClk_SynchronizeToSyncPulseSender(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime);

ViStatus _VI_FUNC niTClk_IsDone(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViBoolean* done);

ViStatus _VI_FUNC niTClk_SetupForSyncPulseSenderSynchronize(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime);

ViStatus _VI_FUNC niTClk_FinishSyncPulseSenderSynchronize(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime);

ViStatus _VI_FUNC niTClk_GetTClkMeasurementForExternalSyncPulse(
   ViSession session,
   ViReal64* measurement);

ViStatus _VI_FUNC niTClk_AdjustSyncPulseSenderTClkTimebase(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 tclkAdjustment);

ViStatus _VI_FUNC niTClk_AdjustSyncPulseSenderTClkDivisors(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 tclkAdjustment);

ViStatus _VI_FUNC niTClk_GetTClkAdjustmentForDistributedTClk(
   ViReal64 tclkPeriod,
   ViUInt32 measurementsForSenderSize,
   ViReal64 measurementsForSender[],
   ViUInt32 measurementsForReceiverSize,
   ViReal64 measurementsForReceiver[],
   ViReal64* tclkAdjustment);

ViStatus _VI_FUNC niTClk_FinishSyncPulseSenderSynchronizeWithAdjustmentType(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime,
   ViUInt32 adjustmentType);

// -- Deprecated Functions --
ViStatus _VI_FUNC niTClk_SynchronizeWithOptions(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime,
   ViUInt32 options);

ViStatus _VI_FUNC niTClk_GetTClkDriftInPPM(
   ViUInt32 sessionCount,
   const ViSession sessions[],
   ViReal64 minTime,
   ViReal64* maxTClkDriftInPPM);

// -- Set Attribute --
ViStatus _VI_FUNC niTClk_SetAttributeViString(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViConstString value);

ViStatus _VI_FUNC niTClk_SetAttributeViSession(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession value);

ViStatus _VI_FUNC niTClk_SetAttributeViReal64(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64 value);

// -- Get Attribute --
ViStatus _VI_FUNC niTClk_GetAttributeViString(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 bufSize,
   ViChar value[]);

ViStatus _VI_FUNC niTClk_GetAttributeViSession(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession* value);

ViStatus _VI_FUNC niTClk_GetAttributeViReal64(
   ViSession session,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64* value);


/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/
#define NITCLK_SUCCESS                                                                      0       // 0 (0x0)
#define NITCLK_ERROR_START_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK                                -250001 // -250001 (-0x3d091)
#define NITCLK_ERROR_REF_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK                                  -250002 // -250002 (-0x3d092)
#define NITCLK_ERROR_SCRIPT_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK                               -250003 // -250003 (-0x3d093)
#define NITCLK_ERROR_PAUSE_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK                                -250004 // -250004 (-0x3d094)
#define NITCLK_ERROR_START_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW                    -250005 // -250005 (-0x3d095)
#define NITCLK_ERROR_REF_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW                      -250006 // -250006 (-0x3d096)
#define NITCLK_ERROR_SCRIPT_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW                   -250007 // -250007 (-0x3d097)
#define NITCLK_ERROR_PAUSE_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW                    -250008 // -250008 (-0x3d098)
#define NITCLK_ERROR_CHAN_NAME_NOT_EMPTY                                                    -250009 // -250009 (-0x3d099)
#define NITCLK_ERROR_REF_CLK_RATE_ZERO                                                      -250010 // -250010 (-0x3d09a)
#define NITCLK_ERROR_REF_CLK_RATE_NEGATIVE                                                  -250011 // -250011 (-0x3d09b)
#define NITCLK_ERROR_UNEQUAL_REF_CLK_RATES                                                  -250012 // -250012 (-0x3d09c)
#define NITCLK_ERROR_MIN_TCLK_PERIOD_NOT_SUPPORTED                                          -250013 // -250013 (-0x3d09d)
#define NITCLK_ERROR_REF_CLK_SRC_NONE                                                       -250014 // -250014 (-0x3d09e)
#define NITCLK_ERROR_EXT_SAMP_CLK_RATE_NOT_ALSO_INT                                         -250015 // -250015 (-0x3d09f)
#define NITCLK_ERROR_CANNOT_FIND_COMMON_TCLK_PERIOD                                         -250016 // -250016 (-0x3d0a0)
#define NITCLK_ERROR_INCONSISTENT_SYNC_PULSE_CLK_SRC                                        -250017 // -250017 (-0x3d0a1)
#define NITCLK_ERROR_INCONSISTENT_REF_CLK_SRC                                               -250018 // -250018 (-0x3d0a2)
#define NITCLK_ERROR_NO_START_TRIGS_CONFIGURED_ONE_OR_MORE_MASTERS                          -250019 // -250019 (-0x3d0a3)
#define NITCLK_ERROR_NO_REF_TRIGS_CONFIGURED_ONE_OR_MORE_MASTERS                            -250020 // -250020 (-0x3d0a4)
#define NITCLK_ERROR_NO_PAUSE_TRIGS_CONFIGURED_ONE_OR_MORE_MASTERS                          -250021 // -250021 (-0x3d0a5)
#define NITCLK_ERROR_NO_SCRIPT_TRIGS_CONFIGURED_ONE_OR_MORE_MASTERS                         -250022 // -250022 (-0x3d0a6)
#define NITCLK_ERROR_MULTIPLE_START_TRIG_MASTERS                                            -250023 // -250023 (-0x3d0a7)
#define NITCLK_ERROR_TIMEOUT_NOT_SUPPORTED                                                  -250024 // -250024 (-0x3d0a8)
#define NITCLK_ERROR_OP_NOT_DONE_WITHIN_TIMEOUT                                             -250025 // -250025 (-0x3d0a9)
#define NITCLK_ERROR_MULTIPLE_SESSIONS_EXPORT_SYNC_PULSE                                    -250026 // -250026 (-0x3d0aa)
#define NITCLK_ERROR_SESSION_NOT_SUPPORTED                                                  -250027 // -250027 (-0x3d0ab)
#define NITCLK_ERROR_ZERO_SESSIONS                                                          -250028 // -250028 (-0x3d0ac)
#define NITCLK_ERROR_SESSIONS_ARRAY_NULL                                                    -250029 // -250029 (-0x3d0ad)
#define NITCLK_ERROR_SESSION_SPECIFIED_TWICE                                                -250030 // -250030 (-0x3d0ae)
#define NITCLK_ERROR_TWO_SESSIONS_FOR_ONE_DEVICE                                            -250031 // -250031 (-0x3d0af)
#define NITCLK_ERROR_SESSION_NOT_VALID                                                      -250032 // -250032 (-0x3d0b0)
#define NITCLK_ERROR_COMMIT_FAILED                                                          -250033 // -250033 (-0x3d0b1)
#define NITCLK_ERROR_INITIATE_FAILED                                                        -250034 // -250034 (-0x3d0b2)
#define NITCLK_ERROR_IS_DONE_FAILED                                                         -250035 // -250035 (-0x3d0b3)
#define NITCLK_ERROR_NULL_ERROR_STRING                                                      -250036 // -250036 (-0x3d0b4)
#define NITCLK_ERROR_ZERO_START_TRIG_MASTERS                                                -250037 // -250037 (-0x3d0b5)
#define NITCLK_ERROR_ATTRIBUTE_ID_NOT_SUPPORTED                                             -250038 // -250038 (-0x3d0b6)
#define NITCLK_ERROR_GET_ATTRIBUTE_FUNCTION_NOT_SUPPORTED_DUE_TO_DATA_TYPE                  -250039 // -250039 (-0x3d0b7)
#define NITCLK_ERROR_SET_ATTRIBUTE_FUNCTION_NOT_SUPPORTED_DUE_TO_DATA_TYPE                  -250040 // -250040 (-0x3d0b8)
#define NITCLK_ERROR_GET_ATTRIBUTE_NOT_SUPPORTED                                            -250041 // -250041 (-0x3d0b9)
#define NITCLK_ERROR_SET_ATTRIBUTE_NOT_SUPPORTED                                            -250042 // -250042 (-0x3d0ba)
#define NITCLK_ERROR_INSTRUMENT_DRIVER_CALL_FAILED                                          -250043 // -250043 (-0x3d0bb)
#define NITCLK_ERROR_EXT_SAMP_CLK_RATE_NOT_ABOVE_ZERO                                       -250044 // -250044 (-0x3d0bc)
#define NITCLK_ERROR_EXT_SAMP_CLK_RATES_UNEQUAL                                             -250045 // -250045 (-0x3d0bd)
#define NITCLK_ERROR_TRIG_MASTER_SESSION_NO_LONGER_VALID                                    -250046 // -250046 (-0x3d0be)
#define NITCLK_ERROR_MULTIPLE_SESSIONS_EXPORT_ONBOARD_REF_CLK                               -250047 // -250047 (-0x3d0bf)
#define NITCLK_ERROR_SAMP_CLK_DELAY_NOT_SUPPORTED                                           -250048 // -250048 (-0x3d0c0)
#define NITCLK_ERROR_ONE_START_TRIG_CONFIGURED_ONE_OR_MORE_MASTERS                          -250049 // -250049 (-0x3d0c1)
#define NITCLK_ERROR_ONE_REF_TRIG_CONFIGURED_ONE_OR_MORE_MASTERS                            -250050 // -250050 (-0x3d0c2)
#define NITCLK_ERROR_ONE_PAUSE_TRIG_CONFIGURED_ONE_OR_MORE_MASTERS                          -250051 // -250051 (-0x3d0c3)
#define NITCLK_ERROR_ONE_SCRIPT_TRIG_CONFIGURED_ONE_OR_MORE_MASTERS                         -250052 // -250052 (-0x3d0c4)
#define NITCLK_ERROR_ALL_BUT_ONE_START_TRIG_CONFIGURED_AND_NONE_TRIG_NOT_MASTER             -250053 // -250053 (-0x3d0c5)
#define NITCLK_ERROR_ALL_BUT_ONE_REF_TRIG_CONFIGURED_AND_NONE_TRIG_NOT_MASTER               -250054 // -250054 (-0x3d0c6)
#define NITCLK_ERROR_ALL_BUT_ONE_PAUSE_TRIG_CONFIGURED_AND_NONE_TRIG_NOT_MASTER             -250055 // -250055 (-0x3d0c7)
#define NITCLK_ERROR_ALL_BUT_ONE_SCRIPT_TRIG_CONFIGURED_AND_NONE_TRIG_NOT_MASTER            -250056 // -250056 (-0x3d0c8)
#define NITCLK_ERROR_NUM_SESSIONS_START_TRIG_CONFIGURED                                     -250057 // -250057 (-0x3d0c9)
#define NITCLK_ERROR_NUM_SESSIONS_REF_TRIG_CONFIGURED                                       -250058 // -250058 (-0x3d0ca)
#define NITCLK_ERROR_NUM_SESSIONS_PAUSE_TRIG_CONFIGURED                                     -250059 // -250059 (-0x3d0cb)
#define NITCLK_ERROR_NUM_SESSIONS_SCRIPT_TRIG_CONFIGURED                                    -250060 // -250060 (-0x3d0cc)
#define NITCLK_ERROR_SAMP_CLK_RATE_TOO_LOW                                                  -250061 // -250061 (-0x3d0cd)
#define NITCLK_ERROR_SAMP_CLK_DELAY_NOT_SUPPORTED_FOR_ACQ_SESSIONS                          -250062 // -250062 (-0x3d0ce)
#define NITCLK_ERROR_SAMP_CLK_DELAY_NOT_SUPPORTED_FOR_EXT_SAMP_CLK                          -250063 // -250063 (-0x3d0cf)
#define NITCLK_ERROR_SAMP_CLK_DELAY_NOT_SUPPORTED_FOR_EXT_SAMP_CLK_TIMEBASE                 -250064 // -250064 (-0x3d0d0)
#define NITCLK_ERROR_MORE_THAN_ONE_REF_TRIG_MASTER                                          -250065 // -250065 (-0x3d0d1)
#define NITCLK_ERROR_ACTIVE_CHANNELS_NOT_SUPPORTED_FOR_LABVIEW                              -250066 // -250066 (-0x3d0d2)
#define NITCLK_ERROR_ACTIVE_CHANNELS_FOR_SCRIPT_TRIGGER_MASTER_FOR_LABVIEW                  -250067 // -250067 (-0x3d0d3)
#define NITCLK_ERROR_VALUE_IS_NULL                                                          -250068 // -250068 (-0x3d0d4)
#define NITCLK_ERROR_CHANNEL_NAME_FOR_SCRIPT_TRIGGER_MASTER                                 -250069 // -250069 (-0x3d0d5)
#define NITCLK_ERROR_INCOMPATIBLE_VERSIONS_OF_NITCLK_AND_INSTRUMENT_DRIVER                  -250070 // -250070 (-0x3d0d6)
#define NITCLK_ERROR_INCOMPATIBLE_VERSIONS_OF_NITCLK_AND_2_INSTRUMENT_DRIVERS               -250071 // -250071 (-0x3d0d7)
#define NITCLK_ERROR_EXT_SAMP_CLK_AND_OR_SAMP_CLK_TIMEBASE_RATE_UNMATCHED                   -250072 // -250072 (-0x3d0d8)
#define NITCLK_ERROR_INVALID_ORDERING_OF_DEVICES_LIST                                       -250073 // -250073 (-0x3d0d9)
#define NITCLK_ERROR_SESSIONS_CANNOT_BE_SYNC_DUE_TO_CONFIGURATION                           -250074 // -250074 (-0x3d0da)
#define NITCLK_ERROR_DRIVER_VERSION_DOES_NOT_SUPPORT_ATTRIBUTE                              -250075 // -250075 (-0x3d0db)
#define NITCLK_ERROR_SESSIONS_CANNOT_CONFIGURED_DUE_TO_CONFIGURATION                        -250076 // -250076 (-0x3d0dc)
#define NITCLK_ERROR_NO_SEQUENCER_FLAGS_CONFIGURED_ONE_OR_MORE_MASTERS                      -250077 // -250077 (-0x3d0dd)
#define NITCLK_ERROR_NUM_SESSIONS_SEQUENCER_FLAGS_CONFIGURED                                -250078 // -250078 (-0x3d0de)
#define NITCLK_ERROR_SEQUENCER_FLAG_MASTER_DOES_NOT_SUPPORT_TCLK                            -250079 // -250079 (-0x3d0df)
#define NITCLK_ERROR_ALL_BUT_ONE_SEQUENCER_FLAGS_CONFIGURED_AND_NONE_TRIG_NOT_MASTER        -250080 // -250080 (-0x3d0e0)
#define NITCLK_ERROR_ONE_SEQUENCER_FLAG_CONFIGURED_ONE_OR_MORE_MASTERS                      -250081 // -250081 (-0x3d0e1)
#define NITCLK_ERROR_SEQUENCER_FLAG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW                -250082 // -250082 (-0x3d0e2)
#define NITCLK_ERROR_NUMBER_OF_MEASUREMENTS_DOES_NOT_MATCH_FOR_SENDER_AND_RECEIVER          -250083 // -250083 (-0x3d0e3)
#define NITCLK_ERROR_NUMBER_OF_MEASUREMENTS_IS_ZERO                                         -250084 // -250084 (-0x3d0e4)
#define NITCLK_ERROR_MEASUREMENT_ARRAY_NULL                                                 -250085 // -250085 (-0x3d0e5)
#define NITCLK_ERROR_INVALID_ADJUSTMENT_TYPE                                                -250086 // -250086 (-0x3d0e6)
#define NITCLK_ERROR_INVALID_SYNCHRONIZE_OPTION                                             -250087 // -250087 (-0x3d0e7)
#define NITCLK_ERROR_REMOTE_SESSIONS_HAVE_DIFFERENT_SERVERS                                 -250088 // -250088 (-0x3d0e8)
#define NITCLK_ERROR_ONLY_SOME_SESSIONS_ARE_REMOTE                                          -250089 // -250089 (-0x3d0e9)
#define NITCLK_ERROR_NO_CONDITIONAL_JUMP_TRIGS_CONFIGURED_ONE_OR_MORE_MASTERS               -250090 // -250090 (-0x3d0ea)
#define NITCLK_ERROR_ONE_CONDITIONAL_JUMP_TRIG_CONFIGURED_ONE_OR_MORE_MASTERS               -250091 // -250091 (-0x3d0eb)
#define NITCLK_ERROR_ALL_BUT_ONE_CONDITIONAL_JUMP_TRIGS_CONFIGURED_AND_NONE_TRIG_NOT_MASTER -250092 // -250092 (-0x3d0ec)
#define NITCLK_ERROR_NUM_SESSIONS_CONDITIONAL_JUMP_TRIGS_CONFIGURED                         -250093 // -250093 (-0x3d0ed)
#define NITCLK_ERROR_CONDITIONAL_JUMP_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK_FOR_LABVIEW         -250094 // -250094 (-0x3d0ee)
#define NITCLK_ERROR_CONDITIONAL_JUMP_TRIG_MASTER_DOES_NOT_SUPPORT_TCLK                     -250095 // -250095 (-0x3d0ef)
#define NITCLK_ERROR_CHANNEL_NAME_FOR_CONDITIONAL_JUMP_TRIG_MASTER                          -250096 // -250096 (-0x3d0f0)
#define NITCLK_ERROR_ACTIVE_CHANNELS_FOR_CONDITIONAL_JUMP_TRIG_MASTER_FOR_LABVIEW           -250097 // -250097 (-0x3d0f1)
#define NITCLK_WARNING_COMMIT_RETURNED_WARNING                                              250000  // 250000 (0x3d090)
#define NITCLK_WARNING_INITIATE_RETURNED_WARNING                                            250001  // 250001 (0x3d091)
#define NITCLK_WARNING_IS_DONE_RETURNED_WARNING                                             250002  // 250002 (0x3d092)
#define NITCLK_WARNING_STRING_TRUNCATED_TO_FIT_BUFFER                                       250003  // 250003 (0x3d093)
#define NITCLK_WARNING_INSTRUMENT_DRIVER_CALL_RETURNED_WARNING                              250004  // 250004 (0x3d094)


/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* ___niTClk_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niWLANGeneration.h sha256=b99b75b58938eb0670c7bb9bb2604764900eaa95a154d77c234bf6bda8766828 bytes=80836 -->
## FILE: imports/include/niWLANGeneration.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niWLANGeneration.h`
- sha256: `b99b75b58938eb0670c7bb9bb2604764900eaa95a154d77c234bf6bda8766828`
- bytes: 80836

````c
/****************************************************************************
*          National Instruments WLAN Signal Generator
*---------------------------------------------------------------------------
*   Copyright (c) National Instruments 2016.  All Rights Reserved.
*---------------------------------------------------------------------------
*
* Title:    niWLANGeneration.h
* Purpose:  National Instruments WLAN Generator
*           functions declarations.
*
****************************************************************************/


#ifndef __NIWLAN_TOOLKIT_GENERATION_HEADER_DEFINED__
#define __NIWLAN_TOOLKIT_GENERATION_HEADER_DEFINED__

#ifdef __cplusplus
extern "C"
{
#endif

	//	 NI-WLAN Typedefs
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
	typedef signed long        int32;
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

#ifndef _NI_WLAN_GENERATION_SESSION_DEFINED_
#define _NI_WLAN_GENERATION_SESSION_DEFINED_
	typedef uInt64*      niWLANGenerationSession;
#endif

#ifndef _NI_WLAN_GENERATION_ATTR_DEFINED_
#define _NI_WLAN_GENERATION_ATTR_DEFINED_
	typedef int32		niWLANG_Attr;
#endif

/****************************************************************************
*---------------------------- Attribute Defines ---------------------------*
****************************************************************************/
#define NIWLANG_COMPATIBILITY_VERSION						0x38    /*int32,readonly*/

#define NIWLANG_STANDARD									0x1F	/*int32*/
#define NIWLANG_OVERSAMPLING_RATIO							0xD3	/*int32*/
#define NIWLANG_CARRIER_FREQUENCY							0x0		/*float64*/
#define NIWLANG_PPDU_TYPE									0x5F	/*int32*/
#define NIWLANG_RU_SIZE                                     0x84    /*int32*/
#define NIWLANG_RU_OFFSET_MRU_INDEX                         0x85    /*int32*/
#define NIWLANG_RU_TYPE                                     0xDE    /*int32*/
#define NIWLANG_DISTRIBUTION_BANDWIDTH                      0xE3    /*float64*/
#define NIWLANG_RU_ALLOCATION_MODE                          0xCD	/*int32*/
#define NIWLANG_RU_ALLOCATION                               0xCE    /*1D Array of int32*/
#define NIWLANG_USER_ENABLED                                0xCF	/*int32*/
#define NIWLANG_RELATIVE_POWER                              0x88    /*float64*/
#define NIWLANG_POWER_BOOST_FACTOR                          0xA4    /*float64*/
#define NIWLANG_NON_HT_MODULATION_MODE                      0x7F    /*int32*/
#define NIWLANG_OFDM_DATA_RATE								0x20	/*int32*/
#define NIWLANG_DSSS_DATA_RATE								0x21	/*int32*/
#define NIWLANG_IDLE_INTERVAL								0x3		/*float64*/
#define NIWLANG_IDLE_INTERVAL_MODE                          0xC7    /*int32*/
#define NIWLANG_NUMBER_OF_FRAMES							0x6		/*int32*/
#define NIWLANG_FRAME_DURATION								0xD1	/*float64*/
#define NIWLANG_UNFRAMED_DATA_MODULATION_ENABLED			0xD2	/*int32*/
#define NIWLANG_DSSS_PREAMBLE_TYPE							0x4		/*int32*/
#define NIWLANG_STA_ID                                      0xA3    /*int32*/
#define NIWLANG_DUAL_CARRIER_MODULATION_ENABLED             0x9A    /*int32*/
#define NIWLANG_2XLDPC_ENABLED                              0xE4    /*int32*/
#define NIWLANG_UNEQUAL_MODULATION_ENABLED                  0xE5    /*int32*/
#define NIWLANG_UNEQUAL_MODULATION_PATTERN_INDEX            0xE6    /*int32*/
#define NIWLANG_BSS_COLOR                                   0xB8    /*int32*/
#define NIWLANG_WAVEFORM_FILE_VERSION                       0xCA    /*int32*/
#define NIWLANG_CHANNELIZATION                              0xE7    /*int32*/

/*- Payload Attributes ----------------------------------------*/
#define NIWLANG_PAYLOAD_AUTO_NUMBER_OF_MPDUS                0xB2	/*int32*/
#define NIWLANG_PAYLOAD_MAC_FRAME_TYPE                      0xBC    /*int32*/
#define NIWLANG_AUTO_PAYLOAD_DATA_LENGTH_MODE               0xB3    /*int32*/
#define NIWLANG_PAYLOAD_NUMBER_OF_MPDUS                     0x68	/*int32*/
#define NIWLANG_PAYLOAD_DATA_LENGTH							0x5		/*int32*/
#define NIWLANG_PAYLOAD_DATA_TYPE							0x7		/*int32*/
#define NIWLANG_PAYLOAD_PN_ORDER							0x8		/*int32*/
#define NIWLANG_PAYLOAD_PN_SEED								0x9		/*int32*/
#define NIWLANG_PAYLOAD_USER_DEFINED_BITS					0xA		/*1D Array of int32*/
#define NIWLANG_MAC_FRAME_FORMAT							0x78	/*int32*/
#define NIWLANG_MAC_HEADER_ENABLED							0xB		/*int32*/
#define NIWLANG_MAC_FRAME_CONTROL							0x39	/*int32*/
#define NIWLANG_MAC_DURATION_OR_ID							0x3A    /*int32*/
#define NIWLANG_MAC_ADDRESS1_ENABLED						0x3B    /*int32*/
#define NIWLANG_MAC_ADDRESS1_LENGTH							0x79	/*int32*/
#define NIWLANG_MAC_ADDRESS1								0x3C    /*int64*/
#define NIWLANG_MAC_ADDRESS2_ENABLED						0x3D    /*int32*/
#define NIWLANG_MAC_ADDRESS2_LENGTH							0x7A	/*int32*/
#define NIWLANG_MAC_ADDRESS2								0x3E    /*int64*/
#define NIWLANG_MAC_ADDRESS3_ENABLED						0x3F    /*int32*/
#define NIWLANG_MAC_ADDRESS3								0x40    /*int64*/
#define NIWLANG_MAC_SEQUENCE_CONTROL_ENABLED				0x41    /*int32*/
#define NIWLANG_MAC_SEQUENCE_CONTROL						0x42    /*int32*/
#define NIWLANG_MAC_ADDRESS4_ENABLED						0x43    /*int32*/
#define NIWLANG_MAC_ADDRESS4								0x44    /*int64*/
#define NIWLANG_MAC_QOS_CONTROL_ENABLED						0x35    /*int32*/
#define NIWLANG_MAC_QOS_CONTROL								0x47    /*int32*/
#define NIWLANG_MAC_HT_CONTROL_ENABLED						0x48    /*int32*/
#define NIWLANG_MAC_HT_CONTROL								0x49    /*int32*/
#define NIWLANG_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED		0x50    /*int32*/
#define NIWLANG_MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL		0x51    /*int32*/
#define NIWLANG_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED		0x52    /*int32*/
#define NIWLANG_MPDU_LENGTH									0x53    /*int32,readonly*/
#define NIWLANG_MAC_FCS_ENABLED                             0x64	/*int32*/
#define NIWLANG_TRIGGER_FRAME_AID12                         0xC4    /*int32*/
#define NIWLANG_TRIGGER_FRAME_CS_REQUIRED                   0xBE    /*int32*/
#define NIWLANG_TRIGGER_FRAME_AP_TX_POWER                   0xAC    /*int32*/
#define NIWLANG_TRIGGER_FRAME_TARGET_RSSI                   0xAD    /*int32*/
#define NIWLANG_TRIGGER_FRAME_MAC_PADDING_DURATION          0xBD    /*int32*/
#define NIWLANG_NUMBER_OF_DATA_SYMBOLS                      0x5E	/*int32*/
#define NIWLANG_AMPDU_ENABLED                             	0x67	/*int32*/
/*- Coding ---------------------------------------------------*/
#define NIWLANG_SUBCARRIER_MASK								0xC		/*1D Array of float64*/		
#define NIWLANG_LOCKED_CLOCK_BIT_ENABLED					0xD		/*int32*/
#define NIWLANG_HEADER_ENCODER_ENABLED						0xE		/*int32*/
#define NIWLANG_HEADER_INTERLEAVER_ENABLED					0xF		/*int32*/	
#define NIWLANG_PAYLOAD_SCRAMBLER_ENABLED					0x10	/*int32*/	
#define NIWLANG_PAYLOAD_SCRAMBLER_SEED						0x11	/*int32*/	
#define NIWLANG_PAYLOAD_ENCODER_ENABLED						0x12	/*int32*/
#define NIWLANG_FEC_CODING_TYPE								0x46	/*int32*/
#define NIWLANG_PAYLOAD_INTERLEAVER_ENABLED					0x13	/*int32*/
/*- Impairments ---------------------------------------------*/
#define NIWLANG_CARRIER_FREQUENCY_OFFSET					0x14	/*float64*/
#define NIWLANG_IQ_GAIN_IMBALANCE							0x15	/*float64*/
#define NIWLANG_I_DC_OFFSET									0x16	/*float64*/
#define NIWLANG_Q_DC_OFFSET									0x17	/*float64*/
#define NIWLANG_QUADRATURE_SKEW								0x18	/*float64*/
#define NIWLANG_TIMING_SKEW									0x4F	/*float64*/
#define NIWLANG_SAMPLE_CLOCK_OFFSET							0x19	/*float64*/
#define NIWLANG_ALL_IQ_IMPAIRMENTS_ENABLED					0x60    /*int32*/
#define NIWLANG_AWGN_ENABLED								0x61	/*int32*/
#define NIWLANG_TIME_DELAY                                  0x87	/*float64*/
#define NIWLANG_CARRIER_TO_NOISE_RATIO						0x62    /*float64*/
/*- Spectrum Control -----------------------------------------*/
#define NIWLANG_PULSE_SHAPING_FILTER_ENABLED				0x36	/*int32*/
#define NIWLANG_PULSE_SHAPING_FILTER_TYPE					0x1A	/*int32*/
#define NIWLANG_PULSE_SHAPING_FILTER_PARAMETER				0x1B	/*float64*/
#define NIWLANG_DSSS_WINDOW_LENGTH							0x1D	/*float64*/
#define NIWLANG_WINDOWING_METHOD							0x4A	/*int32*/ 
#define NIWLANG_PULSE_SHAPING_FILTER_LENGTH					0x70	/*int32*/
#define NIWLANG_OFDM_WINDOW_LENGTH							0x7D	/*int32*/

	/*------------------------------------------------------------*/
#define NIWLANG_IQ_WAVEFORM_SIZE							0x25	/*int32, readonly*/

/* 802.11n Attributes*/
#define NIWLANG_NUMBER_OF_TRANSMIT_CHANNELS					0x2F	/*int32*/
#define NIWLANG_MCS_INDEX									0x29	/*int32*/
#define NIWLANG_HE_SIG_B_MCS_INDEX                          0xA1    /*int32*/
#define NIWLANG_HE_SIG_B_DUAL_CARRIER_MODULATION_ENABLED    0xA2	/*int32*/
#define NIWLANG_CHANNEL_BANDWIDTH							0x2A	/*float64*/
#define NIWLANG_80211N_PLCP_FRAME_FORMAT					0x2B	/*int32*/
#define NIWLANG_NUMBER_OF_EXTENSION_SPATIAL_STREAMS			0x2E	/*int32*/
#define NIWLANG_NUMBER_OF_USERS								0x73	/*int32*/
#define NIWLANG_MAPPING_MATRIX_TYPE							0x37	/*int32*/
#define NIWLANG_STBC_INDEX									0x31	/*int32*/
#define NIWLANG_80211AH_PREAMBLE_TYPE						0x77	/*int32*/
#define NIWLANG_TRANSMISSION_MODE                           0x7C	/*int32*/
#define NIWLANG_PREAMBLE_PUNCTURING_ENABLED                 0xBF    /*int32*/
#define NIWLANG_PRIMARY_20MHZ_CHANNEL_INDEX                 0xC0    /*int32*/
#define NIWLANG_PREAMBLE_PUNCTURING_MASK                    0xC1    /*int32*/
/*-Hardware Settings----------------------------------------------*/
#define NIWLANG_AUTO_HEADROOM_ENABLED						0x57    /*int32*/
#define NIWLANG_HEADROOM									0x28	/*float64*/
#define NIWLANG_FULLSCALE_BACKOFF                           0xA8    /*float64*/
#define NIWLANG_AVERAGE_POWER_REFERENCE                     0xAA    /*int32*/
#define NIWLANG_MAXIMUM_HARDWARE_IQ_RATE					0x66	/*float64*/
#define NIWLANG_IQ_RATE										0x23    /*float64,readonly*/
#define NIWLANG_ACTUAL_HEADROOM								0x58    /*float64,readonly*/
#define NIWLANG_RF_BLANKING_ENABLED							0x5A    /*int32*/
#define NIWLANG_LO_SHARING_ENABLED							0x76    /*int32*/
#define NIWLANG_HYBRID_LO_SHARING_MODE				        0xDF    /*int32*/
#define NIWLANG_LO_SPLITTER_LOSS                            0XE1    /*1D Array of float64*/
#define NIWLANG_LO_SPLITTER_LOSS_FREQUENCY                  0XE2    /*1D Array of float64*/
#define NIWLANG_LO_FREQUENCY_OFFSET_MODE                    0xB0    /*int32*/
#define NIWLANG_LO_FREQUENCY_OFFSET                         0xB1    /*float64*/
#define NIWLANG_MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE     0xE0    /*int32*/
#define NIWLANG_MULTI_SEGMENT_GENERATION_MODE               0x86    /*int32*/
#define NIWLANG_SPATIAL_MAPPING_MODE                        0xB9    /*int32*/
#define NIWLANG_RF_BLANKING_MARKER_POSITIONS				0x5B    /*1D Array of int32*/
#define NIWLANG_BURST_START_LOCATIONS                       0xAE    /*1D Array of int32*/
#define NIWLANG_BURST_STOP_LOCATIONS                        0xAF    /*1D Array of int32*/
#define NIWLANG_SIGNAL_BANDWIDTH                            0xC2    /*float64,readonly*/
#define NIWLANG_RUN_TIME_SCALING                            0xC9    /*float64*/
/*-Data Rate and Frame Format-------------------------------------*/
#define NIWLANG_ACTUAL_OFDM_DATA_RATE						0x59    /*float64,readonly*/
#define NIWLANG_NOT_SOUNDING_BIT							0x56    /*int32*/

/* 802.11ac Attributes*/
#define NIWLANG_NUMBER_OF_SEGMENTS							0x4B	/*int32*/
#define NIWLANG_NUMBER_OF_SPACE_TIME_STREAMS				0x4C	/*int32*/
#define NIWLANG_SPACE_TIME_STREAM_OFFSET                    0xBB    /*int32*/
#define NIWLANG_NUMBER_OF_LTF_SYMBOLS                       0xA5    /*int32*/
#define NIWLANG_MU_MIMO_LTF_MODE_ENABLED                    0xBA    /*int32*/
#define NIWLANG_STBC_ALL_STREAMS_ENABLED					0x4D	/*int32*/
/*-Advanced-------------------------------------------------------*/
#define NIWLANG_SWAP_I_AND_Q_ENABLED						0x4E	/*int32*/
#define NIWLANG_SAMPLE_CLOCK_RATE_FACTOR					0x6B	/*float64*/
/*-Data Rate and Frame Format-------------------------------------*/
#define NIWLANG_GUARD_INTERVAL_TYPE							0x7B	/*int32*/
#define NIWLANG_LTF_SIZE                                    0x90	/*int32*/
#define NIWLANG_MIDAMBLE_PERIODICITY                        0xCC    /*int32*/
#define NIWLANG_L_SIG_LENGTH                                0xB4    /*int32*/
#define NIWLANG_PRE_FEC_PADDING_FACTOR                      0xB5    /*int32*/
#define NIWLANG_PE_DISAMBIGUITY                             0xB6    /*int32*/
#define NIWLANG_LDPC_EXTRA_SYMBOL_SEGMENT                   0xB7    /*int32*/
#define NIWLANG_NOMINAL_PACKET_PADDING                      0xC3    /*int32*/
#define NIWLANG_PACKET_EXTENSION_DURATION                   0x9F    /*float64, readonly*/
#define NIWLANG_SIG_MCS_INDEX                               0xD4    /*int32*/
#define NIWLANG_HE_SIG_B_COMPRESSION_MODE                   0xE8	/*int32*/
#define NIWLANG_INTERFERENCE_MITIGATION_PILOTS_ENABLED      0xE9	/*int32*/
#define NIWLANG_SIG_COMPRESSION_ENABLED                     0xD5    /*int32*/
#define NIWLANG_PHASE_ROTATION_COEFFICIENT_1                0xD6    /*int32*/
#define NIWLANG_PHASE_ROTATION_COEFFICIENT_2                0xD7    /*int32*/
#define NIWLANG_PHASE_ROTATION_COEFFICIENT_3                0xD8    /*int32*/
#define NIWLANG_CYCLIC_TIME_SHIFT                           0xD9    /*float64*/

/*-Obsolete--------------------------------------------------------*/
#define NIWLANG_WINDOW_LENGTH								0x1D	/*float64*/
#define NIWLANG_OFDM_LEGACY_SCALING_ENABLED					0x65	/*int32*/
#define NIWLANG_POWER_LEVEL									0x1		/*float64*/
#define NIWLANG_WAVEFORM_SCALING_FACTOR						0x24	/*float64*/
#define NIWLANG_PEAK_TO_AVERAGE_POWER_RATIO					0x1E	/*float64, readonly*/
#define NIWLANG_MAPPING_MATRIX								0x2D	/*int32, readonly*/
#define NIWLANG_GUARD_INTERVAL								0x2C	/*float64*/
#define NIWLANG_80211AH_UPLINK_INDICATION					0x7C	/*int32*/
#define NIWLANG_MAX_EXPECTED_PAPR							0x28	/*float64*/
#define NIWLANG_PAYLOAD_AUTO_DATA_LENGTH                    0xB3    /*int32*/

/****************************************************************************
*------------------------ Attribute Value Defines -------------------------*
****************************************************************************/

/*- Values for WLAN Generation Toolkit Version -*/
#define NIWLANG_VAL_COMPATIBILITY_VERSION_010000			           10000
#define NIWLANG_VAL_COMPATIBILITY_VERSION_020000			           20000
#define NIWLANG_VAL_COMPATIBILITY_VERSION_030000			           30000
#define NIWLANG_VAL_COMPATIBILITY_VERSION_040000			           40000
#define NIWLANG_VAL_COMPATIBILITY_VERSION_050000                       50000
#define NIWLANG_VAL_COMPATIBILITY_VERSION_060000                       60000  
                                                                       
/*- Values For WLAN Standards -*/                                      
#define NIWLANG_VAL_STANDARD_80211AG_OFDM					           0
#define NIWLANG_VAL_STANDARD_80211J_OFDM                               7
#define NIWLANG_VAL_STANDARD_80211P_OFDM                               8
#define NIWLANG_VAL_STANDARD_80211BG_DSSS					           1
#define NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM				           2
#define NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM				           3
#define NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM				           4
#define NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM				           5
#define NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM                         6
#define NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM                         9
#define NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM                         10
#define NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM                         11
                                                                                                                                       
/*- Values For Preamble Format attribute -*/                           
#define NIWLANG_VAL_PREAMBLE_TYPE_SHORT_PREAMBLE			           0
#define NIWLANG_VAL_PREAMBLE_TYPE_LONG_PREAMBLE				           1

/*- Values For Average Power Reference attribute -*/
#define NIWLANG_VAL_AVERAGE_POWER_REFERENCE_NON_BOOSTED_FIELDS         0
#define NIWLANG_VAL_AVERAGE_POWER_REFERENCE_POWER_BOOSTED_FIELDS       1
#define NIWLANG_VAL_AVERAGE_POWER_REFERENCE_ENTIRE_PACKET              2    

/*- Values For Payload Data Type attribute -*/
#define NIWLANG_VAL_USER_DEFINED							           0
#define NIWLANG_VAL_PN_SEQUENCE								           1
                                                                       
/*- Values For Pulse Shaping Filter attribute -*/                      
#define NIWLANG_VAL_FILTER_RECTANGULAR						           0
#define NIWLANG_VAL_FILTER_RAISED_COSINE					           1	
#define NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE				           2
#define NIWLANG_VAL_FILTER_GAUSSIAN							           3
                                                                       
/*- Values For Windowing Method -*/                                    
#define NIWLANG_VAL_WIN_METHOD_CENTERED_AT_SYMBOL_BOUNDARY	           0
#define NIWLANG_VAL_WIN_METHOD_STARTING_AT_SYMBOL_BOUNDARY	           1	
                                                                       
/*- Values For OFDM Data Rate attribute -*/                            
#define NIWLANG_VAL_OFDM_DATA_RATE_6						           0
#define NIWLANG_VAL_OFDM_DATA_RATE_9						           1
#define NIWLANG_VAL_OFDM_DATA_RATE_12						           2
#define NIWLANG_VAL_OFDM_DATA_RATE_18						           3
#define NIWLANG_VAL_OFDM_DATA_RATE_24						           4
#define NIWLANG_VAL_OFDM_DATA_RATE_36						           5
#define NIWLANG_VAL_OFDM_DATA_RATE_48						           6
#define NIWLANG_VAL_OFDM_DATA_RATE_54						           7

/*- Values For RU Size -*/                            
#define NIWLANG_VAL_RU_SIZE_26                                         26
#define NIWLANG_VAL_RU_SIZE_52                                         52
#define NIWLANG_VAL_RU_SIZE_106                                        106
#define NIWLANG_VAL_RU_SIZE_242                                        242
#define NIWLANG_VAL_RU_SIZE_484                                        484
#define NIWLANG_VAL_RU_SIZE_996                                        996
#define NIWLANG_VAL_RU_SIZE_2x996                                      1992
#define NIWLANG_VAL_RU_SIZE_4x996                                      3984
#define NIWLANG_VAL_RU_SIZE_52_PLUS_26                                 78
#define NIWLANG_VAL_RU_SIZE_106_PLUS_26                                132
#define NIWLANG_VAL_RU_SIZE_484_PLUS_242                               726
#define NIWLANG_VAL_RU_SIZE_996_PLUS_484                               1480
#define NIWLANG_VAL_RU_SIZE_996_PLUS_484_PLUS_242                      1722
#define NIWLANG_VAL_RU_SIZE_2x996_PLUS_484                             2476
#define NIWLANG_VAL_RU_SIZE_3x996                                      2988
#define NIWLANG_VAL_RU_SIZE_3x996_PLUS_484                             3472

/*- Values For DSSS Data Rate attribute -*/                            
#define NIWLANG_VAL_DSSS_DATA_RATE_1						           0
#define NIWLANG_VAL_DSSS_DATA_RATE_2						           1
#define NIWLANG_VAL_DSSS_DATA_RATE_5p5_CCK					           2
#define NIWLANG_VAL_DSSS_DATA_RATE_5p5_PBCC					           3
#define NIWLANG_VAL_DSSS_DATA_RATE_11_CCK					           4
#define NIWLANG_VAL_DSSS_DATA_RATE_11_PBCC					           5
#define NIWLANG_VAL_DSSS_DATA_RATE_22						           6
#define NIWLANG_VAL_DSSS_DATA_RATE_33						           7

/*- Data Rate and Frame Format:Transmission Mode -*/                            
#define NIWLANG_VAL_TRANSMISSION_MODE_DOWNLINK 			               0  
#define NIWLANG_VAL_TRANSMISSION_MODE_UPLINK             	           1
                                                                       
/*- Values for 80211n PLCP frame Format -*/                            
#define NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_MIXED			           0  
#define NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_GREENFIELD 	           1
                                                                       
/*- Values for Multi-segment Generation Mode -*/                       
#define NIWLANG_VAL_SINGLE_GENERATOR                                   0
#define NIWLANG_VAL_MULTIPLE_GENERATORS                                1
                                                                       
/*- Values for 80211n Mapping Matrix Type -*/                          
#define NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT                         0
#define NIWLANG_VAL_MAPPING_MATRIX_TYPE_HADAMARD                       1
#define NIWLANG_VAL_MAPPING_MATRIX_TYPE_FOURIER                        2
#define NIWLANG_VAL_MAPPING_MATRIX_TYPE_USER_DEFINED                   3
                                                                       
/* Values for TVHT Mode -*/                                            
#define NIWLANG_VAL_TVHT_MODE_1                                        0
#define NIWLANG_VAL_TVHT_MODE_2C                                       1
#define NIWLANG_VAL_TVHT_MODE_2N                                       2
#define NIWLANG_VAL_TVHT_MODE_4C                                       3
#define NIWLANG_VAL_TVHT_MODE_4N                                       4

/* Values for RU Allocation Mode -*/                                            
#define NIWLANG_VAL_RU_ALLOCATION_MODE_INDIVIDUAL                      0
#define NIWLANG_VAL_RU_ALLOCATION_MODE_GROUP                           1

                                                                       
/*- Values for binary attributes */                                    
#define NIWLANG_VAL_FALSE									           0
#define NIWLANG_VAL_TRUE									           1

/*- Values for FEC Coding Type attributes */
#define NIWLANG_VAL_FEC_CODING_TYPE_BCC						           0
#define NIWLANG_VAL_FEC_CODING_TYPE_LDPC					           1
                                                                       
/*- Values for PPDU Type */                                            
#define NIWLANG_VAL_PPDU_TYPE_SU_PPDU						           0
#define NIWLANG_VAL_PPDU_TYPE_MU_PPDU						           1
#define NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU                   2
#define NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU                       3
#define NIWLANG_VAL_PPDU_TYPE_ELR_PPDU                				   4

/*- Values for Non-HT Modulation Mode */
#define NIWLANG_VAL_NON_HT_MODULATION_MODE_OFF                         0
#define NIWLANG_VAL_NON_HT_MODULATION_MODE_ON                          1

/*- File IO Open Flags */
#define NIWLANG_VAL_FILE_OPERATION_MODE_OPEN				           0
#define NIWLANG_VAL_FILE_OPERATION_MODE_OPEN_OR_CREATE		           1
#define NIWLANG_VAL_FILE_OPERATION_MODE_CREATE_OR_REPLACE	           2
#define NIWLANG_VAL_FILE_OPERATION_MODE_CREATE				           3
                                                                       
/*- Frequency Band for Channel Number to Carrier Frequency  */
#define NIWLANG_VAL_FREQUENCY_BAND_2p4GHZ				               0
#define NIWLANG_VAL_FREQUENCY_BAND_5GHZ					               1

/* LO Source */
#define NIWLANG_VAL_LO_SOURCE_EXTERNAL                                 0
#define NIWLANG_VAL_LO_SOURCE_ONBOARD                                  2
#define NIWLANG_VAL_LO_SOURCE_SG_SA_Shared                             3
                                                                       
#define NIWLANG_VAL_MAX_ERROR_MESSAGE_SIZE					           1024
                                                                       
                                                                       
/*-MAC Frame Format---*/                                               
#define	NIWLANG_VAL_MAC_FRAME_FORMAT_LONG					           0
#define NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT					           1
                                                                       
/* 80211AH Preamble Type */                                            
#define NIWLANG_VAL_80211AH_PREAMBLE_TYPE_SHORT				           0
#define	NIWLANG_VAL_80211AH_PREAMBLE_TYPE_LONG				           1

/* Data Rate and Frame Format : Guard Interval Type */
#define NIWLANG_VAL_GUARD_INTERVAL_TYPE_ONE_BY_FOUR                    0
#define NIWLANG_VAL_GUARD_INTERVAL_TYPE_ONE_BY_EIGHT                   1
#define NIWLANG_VAL_GUARD_INTERVAL_TYPE_ONE_BY_SIXTEEN                 2

/* Data Rate and Frame Format:LTF Size */
#define NIWLANG_VAL_LTF_SIZE_AUTO                                     -1
#define NIWLANG_VAL_LTF_SIZE_4X                                        0
#define NIWLANG_VAL_LTF_SIZE_2X                                        1
#define NIWLANG_VAL_LTF_SIZE_1X                                        2

/* LO Frequency Offset Mode */
#define NIWLANG_VAL_LO_FREQUENCY_OFFSET_MODE_AUTO                      0
#define NIWLANG_VAL_LO_FREQUENCY_OFFSET_MODE_USER_DEFINED              1 
#define NIWLANG_VAL_LO_FREQUENCY_OFFSET_MODE_DISABLED                  2

/* Payload Frame Type */
#define NIWLANG_VAL_PAYLOAD_MAC_FRAME_TYPE_GENERAL_FRAME               0
#define NIWLANG_VAL_PAYLOAD_MAC_FRAME_TYPE_DATA_FRAME                  1
#define NIWLANG_VAL_PAYLOAD_MAC_FRAME_TYPE_TRIGGER_FRAME               2

/* Payload Trigger Frame Maximum Padding Duration */
#define NIWLANG_VAL_PADDING_DURATION_0US                               0
#define NIWLANG_VAL_PADDING_DURATION_8US                               1
#define NIWLANG_VAL_PADDING_DURATION_16US                              2

/* Spatial Mapping Mode */
#define NIWLANG_VAL_SPATIAL_MAPPING_MODE_COMMON                        0
#define NIWLANG_VAL_SPATIAL_MAPPING_MODE_USER_SPECIFIC                 1

/* Nominal Packet Padding */
#define NIWLANG_VAL_NOMINAL_PACKET_PADDING_AUTO                        -1
#define NIWLANG_VAL_NOMINAL_PACKET_PADDING_0US                          0
#define NIWLANG_VAL_NOMINAL_PACKET_PADDING_8US                          1
#define NIWLANG_VAL_NOMINAL_PACKET_PADDING_16US                         2
#define NIWLANG_VAL_NOMINAL_PACKET_PADDING_20US                         3

/* Idle Interval Mode */
#define NIWLANG_VAL_IDLE_INTERVAL_MODE_SPLIT                            0
#define NIWLANG_VAL_IDLE_INTERVAL_MODE_POST_BURST                       1

/* Midamble Periodicity */
#define NIWLANG_VAL_MIDAMBLE_PERIODICITY_NONE                           0
#define NIWLANG_VAL_MIDAMBLE_PERIODICITY_TEN_SYMBOLS                    1
#define NIWLANG_VAL_MIDAMBLE_PERIODICITY_TWENTY_SYMBOLS                 2

/* Auto Payload Data Length Mode */
#define NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_DISABLED				0
#define NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_L_SIG_LENGTH			1
#define NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_FRAME_DURATION		2

/* Obsolete */
#define NIWLANG_VAL_STANDARD_80211AGJP_OFDM								0

/* Data Rate and Frame Format : Guard Interval Type */
#define NIWLANG_VAL_GUARD_INTERVAL_TYPE_LONG							0
#define NIWLANG_VAL_GUARD_INTERVAL_TYPE_SHORT							1

/* Data Rate and Frame Format: HE-SIG-B Compression Mode */
#define NIWLANG_VAL_HE_SIG_B_COMPRESSION_MODE_AUTO					    0
#define NIWLANG_VAL_HE_SIG_B_COMPRESSION_MODE_MANUAL					1

/* Data Rate and Frame Format: SIG Compression Enabled */
#define NIWLANG_VAL_SIG_COMPRESSION_ENABLED_FALSE					    0
#define NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE					    1

/* Data Rate and Frame Format: Phase Rotation: Coefficient 1 */
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_1_PLUS_ONE				0
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_1_MINUS_ONE				1

/* Data Rate and Frame Format: Phase Rotation: Coefficient 2 */
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_2_PLUS_ONE				0
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_2_MINUS_ONE				1

/* Data Rate and Frame Format: Phase Rotation: Coefficient 3 */
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_3_PLUS_ONE				0
#define NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_3_MINUS_ONE				1

/* Waveform File Version */
#define NIWLANG_VAL_WAVEFORM_FILE_VERSION_1_0                     		0
#define NIWLANG_VAL_WAVEFORM_FILE_VERSION_2_0                     		1

/* Hardware Settings: Hybrid LO Sharing Mode */
#define NIWLANG_VAL_HYBRID_LO_SHARING_MODE_DISABLED                   	0
#define NIWLANG_VAL_HYBRID_LO_SHARING_MODE_MODE_0                     	1

/* Hardware Settings: Multi-chassis TClk Synchronization Mode */
#define NIWLANG_VAL_MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE_AUTO           0
#define NIWLANG_VAL_MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE_TIMING_MODULE  1

/* Data Rate and Frame Format: RU Allocation Settings */
#define NIWLANG_VAL_RU_TYPE_RRU				                            0
#define NIWLANG_VAL_RU_TYPE_DRU				                            1

/* Channelization */
#define NIWLANG_VAL_CHANNEL_320MHZ_1			                        0
#define NIWLANG_VAL_CHANNEL_320MHZ_2			                        1

/* Data Rate and Frame Format: Interference Mitigation Pilots Enabled*/
#define NIWLANG_VAL_INTERFERENCE_MITIGATION_PILOTS_ENABLED_FALSE	    0
#define NIWLANG_VAL_INTERFERENCE_MITIGATION_PILOTS_ENABLED_TRUE			1

/**************************************************************************** 
*---------------- WLAN Generator struct definititions  --------------------* 
****************************************************************************/

#if !defined(_NIComplexNumber)
#define _NIComplexNumber

#pragma pack(push, 8)
typedef struct NIComplexNumber_struct {
   float64 real;
   float64 imaginary;
} NIComplexNumber;
#pragma pack(pop)

#endif

#include "niWLANGeneration_Deprecated.h"
/****************************************************************************
*---------------- WLAN Generator Function Declarations ---------------------*
****************************************************************************/

/*- Open and Close Session Functions ---------------------------------------*/
int32 __stdcall  niWLANG_OpenSession(
	char sessionName[],
	int32 compatibilityVersion,
	niWLANGenerationSession *session,
	int32 *isNewSession);

/*- Set and Get Attribute Functions ----------------------------------------*/
int32 __stdcall niWLANG_GetToolkitCompatibilityVersion(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetStandard(
	niWLANGenerationSession session,
	char channelString[],
	int32 standard);

int32 __stdcall niWLANG_GetStandard(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetCarrierFrequency( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);
	
int32 __stdcall niWLANG_GetCarrierFrequency(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetOverSamplingRatio( 
	niWLANGenerationSession session,
	char channelString[],
	float64 overSamplingRatio);

int32 __stdcall niWLANG_GetOverSamplingRatio( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetOFDMDataRate( 
	niWLANGenerationSession session,
	char channelString[],
	int32 ofdmDataRate);

int32 __stdcall niWLANG_GetOFDMDataRate( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall  niWLANG_SetNonHTModulationMode(
    niWLANGenerationSession session,
	char channelString[],
	int32 nonHTDuplicateModulationMode);
	
int32 __stdcall  niWLANG_GetNonHTModulationMode(
    niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetPPDUType(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 ofdmDataRate);
	
int32 __stdcall niWLANG_GetPPDUType(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);
	
int32 __stdcall niWLANG_SetRUSize(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetRUSize(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	

int32 __stdcall niWLANG_SetRUOffsetMRUIndex(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetRUOffsetMRUIndex(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);		
	
int32 __stdcall niWLANG_SetRUAllocationMode(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetRUAllocationMode(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);			
	
int32 __stdcall niWLANG_SetUserEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetUserEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	
	
int32 __stdcall niWLANG_SetRUAllocation( 
	niWLANGenerationSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);

int32 __stdcall niWLANG_GetRUAllocation( 
	niWLANGenerationSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);	
	
int32 __stdcall niWLANG_SetRelativePower( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);
	
int32 __stdcall niWLANG_GetRelativePower(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	

int32 __stdcall niWLANG_SetPowerBoostFactor( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);
	
int32 __stdcall niWLANG_GetPowerBoostFactor(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niWLANG_SetDSSSDataRate( 
	niWLANGenerationSession session,
	char channelString[],
	int32 dsssDataRate);

int32 __stdcall niWLANG_GetDSSSDataRate( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetIdleInterval( 
	niWLANGenerationSession session,
	char channelString[],
	float64 idleInterval);

int32 __stdcall niWLANG_GetIdleInterval( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetIdleIntervalMode( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetIdleIntervalMode( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetNumberOfFrames( 
	niWLANGenerationSession session,
	char channelString[],
	int32 numberOfFrames);

int32 __stdcall niWLANG_GetNumberOfFrames( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetFrameDuration( 
	niWLANGenerationSession session,
	char channelString[],
	float64 frameDuration);

int32 __stdcall niWLANG_GetFrameDuration( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetUnframedDataModulationEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetUnframedDataModulationEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);

int32 __stdcall niWLANG_SetDSSSPreambleType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetDSSSPreambleType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *preambleFormat);

int32 __stdcall niWLANG_SetNumberOfMPDUs(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfMPDUs(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetAutoNumberOfMPDUs(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAutoNumberOfMPDUs(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACFrameType(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACFrameType(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
	
int32 __stdcall niWLANG_SetAutoPayloadDataLengthMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAutoPayloadDataLengthMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
	
int32 __stdcall niWLANG_SetPayloadDataLength( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadDataLength( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadDataType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadDataType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadPNOrder( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadPNOrder( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadPNSeed( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadPNSeed( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadUserDefinedBits( 
	niWLANGenerationSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize);

int32 __stdcall niWLANG_GetPayloadUserDefinedBits( 
	niWLANGenerationSession session,
	char channelString[],
	int32 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);

int32 __stdcall niWLANG_SetMACFrameFormat( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACFrameFormat( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACHeaderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACHeaderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetAMPDUEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAMPDUEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetSubcarrierMask( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize);

int32 __stdcall niWLANG_GetSubcarrierMask( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);

int32 __stdcall niWLANG_SetLockedClockBitEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetLockedClockBitEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetHeaderEncoderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetHeaderEncoderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetHeaderInterleaverEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetHeaderInterleaverEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadScramblerEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadScramblerEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadScramblerSeed( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadScramblerSeed( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadEncoderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadEncoderEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetFECCodingType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetFECCodingType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPayloadInterleaverEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPayloadInterleaverEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetCarrierFrequencyOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetCarrierFrequencyOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetIQGainImbalance( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetIQGainImbalance( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetIDCOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetIDCOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetQDCOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetQDCOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetQuadratureSkew( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetQuadratureSkew( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetTimingSkew( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetTimingSkew( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	

int32 __stdcall niWLANG_SetSampleClockOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetSampleClockOffset( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetPulseShapingFilterEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPulseShapingFilterEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPulseShapingFilterType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetPulseShapingFilterType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetPulseShapingFilterParameter( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetPulseShapingFilterParameter( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetDSSSWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetDSSSWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetOFDMWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetWindowingMethod(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetWindowingMethod(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetPulseShapingFilterLength(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);	

int32 __stdcall niWLANG_GetPulseShapingFilterLength(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	

int32 __stdcall niWLANG_GetIQWaveformSize( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetSwapIAndQEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetSwapIAndQEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	

int32 __stdcall niWLANG_SetNumberOfTransmitChannels( 
	niWLANGenerationSession session,
	char channelString[],
	int32 numberOfTransmitChannels);

int32 __stdcall niWLANG_GetNumberOfTransmitChannels( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetNumberOfSegments( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfSegments( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetNumberOfSpaceTimeStreams( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfSpaceTimeStreams( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetSpaceTimeStreamOffset( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetSpaceTimeStreamOffset( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetNumberOfHELTFSymbols( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfHELTFSymbols( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetMUMIMOLTFModeEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMUMIMOLTFModeEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
	
int32 __stdcall niWLANG_SetSTBCAllStreamsEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);	

int32 __stdcall niWLANG_GetSTBCAllStreamsEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetMCSIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 MCSIndex);

int32 __stdcall niWLANG_GetMCSIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetSTAID( 
	niWLANGenerationSession session,
	char channelString[],
	int32 STAID);

int32 __stdcall niWLANG_GetSTAID( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetHESIGBMCSIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 HESIGBMCSIndex);

int32 __stdcall niWLANG_GetHESIGBMCSIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetHESIGBDualCarrierModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 HESIGBMCSIndex);

int32 __stdcall niWLANG_GetHESIGBDualCarrierModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetDualCarrierModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 DCMEanbled);

int32 __stdcall niWLANG_GetDualCarrierModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetBSSColor( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetBSSColor( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
	
int32 __stdcall niWLANG_SetChannelBandwidth( 
	niWLANGenerationSession session,
	char channelString[],
	float64 channelBandwidth);

int32 __stdcall niWLANG_GetChannelBandwidth( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_Set80211nPLCPFrameFormat( 
	niWLANGenerationSession session,
	char channelString[],
	int32 frameFormat);

int32 __stdcall niWLANG_Get80211nPLCPFrameFormat( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_Set80211ahPreambleType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 frameFormat);

int32 __stdcall niWLANG_Get80211ahPreambleType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetTransmissionMode( 
	niWLANGenerationSession session,
	char channelString[],
	int32 transmissionMode);

int32 __stdcall niWLANG_GetTransmissionMode( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetPreamblePuncturingEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 transmissionMode);

int32 __stdcall niWLANG_GetPreamblePuncturingEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetPrimary20MHzChannelIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 transmissionMode);

int32 __stdcall niWLANG_GetPrimary20MHzChannelIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		

int32 __stdcall niWLANG_SetPreamblePuncturingMask( 
	niWLANGenerationSession session,
	char channelString[],
	int32 transmissionMode);

int32 __stdcall niWLANG_GetPreamblePuncturingMask( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);			
	
int32 __stdcall niWLANG_Set80211ahUplinkIndication( 
	niWLANGenerationSession session,
	char channelString[],
	int32 frameFormat);

int32 __stdcall niWLANG_Get80211ahUplinkIndication( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetNumberOfExtensionSpatialStreams( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfExtensionSpatialStreams( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetNumberOfUsers(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
int32 __stdcall niWLANG_GetNumberOfUsers(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	
	
int32 __stdcall niWLANG_SetMappingMatrixType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 mappingMatrixType);

int32 __stdcall niWLANG_GetMappingMatrixType( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetMultiSegmentGenerationMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niWLANG_GetMultiSegmentGenerationMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
   
int32 __stdcall niWLANG_SetSpatialMappingMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niWLANG_GetSpatialMappingMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);   
   
int32 __stdcall niWLANG_SetSTBCIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 STBCIndex);

int32 __stdcall niWLANG_GetSTBCIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMappingMatrix( 
	niWLANGenerationSession session,
	char channelString[],
	NIComplexNumber* mappingMatrix,
	int32 numMappingMatrixRows,
	int32 numMappingMatrixColumns);

int32 __stdcall niWLANG_GetMappingMatrix( 
	niWLANGenerationSession session,
	char channelString[],
	NIComplexNumber* mappingMatrix,
	int32 numMappingMatrixRows,
	int32 numMappingMatrixColumns);

int32 __stdcall  niWLANG_SetScalarAttributeF64(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	float64 attributeValue);

int32 __stdcall  niWLANG_SetScalarAttributeI32(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	int32 attributeValue);

int32 __stdcall niWLANG_SetVectorAttributeF64(
	niWLANGenerationSession session,
	char channelString[], 
	niWLANG_Attr attributeID,
	float64 data[],
	int32 dataArraySize);

int32 __stdcall niWLANG_SetVectorAttributeI32(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	int32 data[],
	int32 dataArraySize);

int32 __stdcall  niWLANG_GetScalarAttributeF64(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	float64* attributeValue);

int32 __stdcall  niWLANG_GetScalarAttributeI32(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID, 
	int32* attributeValue);

int32 __stdcall niWLANG_GetVectorAttributeF64(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	float64 data[],
	int32 dataArraySize,
	int32* actualNumDataArrayElements);

int32 __stdcall niWLANG_GetVectorAttributeI32(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,	
	int32 data[],
	int32 dataArraySize, 
	int32* actualNumDataArrayElements);	

int32 __stdcall  niWLANG_SetScalarAttributeI64(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID,
	int64 attributeValue);

int32 __stdcall  niWLANG_GetScalarAttributeI64(
	niWLANGenerationSession session,
	char channelString[],
	niWLANG_Attr attributeID, 
	int64* attributeValue);

int32 __stdcall niWLANG_SetSampleClockRateFactor(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 value);

int32 __stdcall niWLANG_GetSampleClockRateFactor(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 *value);

int32 __stdcall niWLANG_SetPhaseRotationCoefficient1(
	niWLANGenerationSession session,
	char channelString[],
	int32 phaseRotationCoefficient1);

int32 __stdcall niWLANG_GetPhaseRotationCoefficient1(
	niWLANGenerationSession session,
	char channelString[],
	int32 *phaseRotationCoefficient1);

int32 __stdcall niWLANG_SetPhaseRotationCoefficient2(
	niWLANGenerationSession session,
	char channelString[],
	int32 phaseRotationCoefficient2);

int32 __stdcall niWLANG_GetPhaseRotationCoefficient2(
	niWLANGenerationSession session,
	char channelString[],
	int32 *phaseRotationCoefficient2);

int32 __stdcall niWLANG_SetPhaseRotationCoefficient3(
	niWLANGenerationSession session,
	char channelString[],
	int32 phaseRotationCoefficient3);

int32 __stdcall niWLANG_GetPhaseRotationCoefficient3(
	niWLANGenerationSession session,
	char channelString[],
	int32 *phaseRotationCoefficient3);

int32 __stdcall niWLANG_SetCyclicTimeShift(
	niWLANGenerationSession session,
	char channelString[],
	float64 CyclicTimeShift);
	
int32 __stdcall niWLANG_GetCyclicTimeShift(
	niWLANGenerationSession session,
	char channelString[],
	float64 *CyclicTimeShift);

int32 __stdcall niWLANG_SetHybridLOSharingMode(
   niWLANGenerationSession session, 
   char channelString[], 
   int32 value);  

int32 __stdcall niWLANG_GetHybridLOSharingMode(
   niWLANGenerationSession session, 
   char channelString[], 
   int32 *value);
   
int32 __stdcall niWLANG_SetMultiChassisTClkSynchronizationMode(
   niWLANGenerationSession session, 
   char channelString[], 
   int32 value);

int32 __stdcall niWLANG_GetMultiChassisTClkSynchronizationMode(
   niWLANGenerationSession session, 
   char channelString[], 
   int32 *value);

int32 __stdcall niWLANG_SetLOSplitterLoss( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize); 

int32 __stdcall niWLANG_GetLOSplitterLoss( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);	

int32 __stdcall niWLANG_SetLOSplitterLossFrequency( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize); 

int32 __stdcall niWLANG_GetLOSplitterLossFrequency( 
	niWLANGenerationSession session,
	char channelString[],
	float64 dataArray[],
	int32 dataArraySize,
	int32 *actualNumDataArrayElements);

int32 __stdcall niWLANG_SetRUType(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);
	
int32 __stdcall niWLANG_GetRUType(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);		
	
int32 __stdcall niWLANG_SetDistributionBandwidth( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetDistributionBandwidth( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_Set2xLDPCEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_Get2xLDPCEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetUnequalModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetUnequalModulationEnabled( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetUnequalModulationPatternIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetUnequalModulationPatternIndex( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetChannelization(
   niWLANGenerationSession session,
   char channelString[],
   int32 value);

int32 __stdcall niWLANG_GetChannelization(
   niWLANGenerationSession session,
   char channelString[],
   int32 *value);

/*- Create Waveform Function -----------------------------------------------*/
int32 __stdcall  niWLANG_CreateWaveformComplexF64(
	niWLANGenerationSession session,
	int32 reset,
	float64* t0,
	float64* dt,
	NIComplexNumber waveform[],
	int32 waveformSize,
	int32* actualNumWaveformSamples,
	int32* done);

int32 __stdcall  niWLANG_CreateMIMOWaveformsComplexF64(
	niWLANGenerationSession session,
	int32 reset,
	float64 t0[],
	float64 dt[],
	NIComplexNumber *waveforms,
	int32 numberOfTxChains,
	int32 individualWaveformSize,
	int32* actualNumSamplesInEachWfm,
	int32* done);

int32 __stdcall niWLANG_SetAutoHeadroomEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 enable);

int32 __stdcall niWLANG_GetAutoHeadroomEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetHeadroom(
	niWLANGenerationSession session,
	char channelString[],
	float64 headroom);

int32 __stdcall niWLANG_GetHeadroom(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetFullscaleBackoff(
	niWLANGenerationSession session,
	char channelString[],
	float64 fullscaleBackoff);

int32 __stdcall niWLANG_GetFullscaleBackoff(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niWLANG_SetAveragePowerReference(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetAveragePowerReference(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	
	
int32 __stdcall niWLANG_SetMaximumHardwareIQRate(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 hardwareIQRate);

int32 __stdcall niWLANG_GetMaximumHardwareIQRate(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 *value);	
	
int32 __stdcall niWLANG_SetRFBlankingEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetRFBlankingEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);

int32 __stdcall niWLANG_SetLOSharingEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetLOSharingEnabled(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);

int32 __stdcall niWLANG_SetLOFrequencyOffset(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 value);

int32 __stdcall niWLANG_GetLOFrequencyOffset(
	niWLANGenerationSession session, 
	char channelString[], 
	float64 *value);
	
int32 __stdcall niWLANG_SetLOFrequencyOffsetMode(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 value);

int32 __stdcall niWLANG_GetLOFrequencyOffsetMode(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 *value);	

int32 __stdcall niWLANG_GetRFBlankingMarkerPositions(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);	

int32 __stdcall niWLANG_GetBurstStartLocations(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);	

int32 __stdcall niWLANG_GetBurstStopLocations(
	niWLANGenerationSession session, 
	char channelString[], 
	int32 dataArray[], 
	int32 dataArraySize, 
	int32 *actualNumDataArrayElements);		
	
int32 __stdcall niWLANG_GetIQRate(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_GetSignalBandwidth(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	
	
int32 __stdcall niWLANG_GetActualHeadroom(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetMACFrameControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACFrameControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACDurationOrID(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACDurationOrID(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress1Length(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress1Length(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress1Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress1Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress2Length(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress2Length(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress2Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress2Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress3Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress3Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACSequenceControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACSequenceControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACSequenceControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMacSequenceControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACCurrentSequenceControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACCurrentSequenceControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACAddress4Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACAddress4Enabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACQOSControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACQOSControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACQOSControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACQOSControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACHTControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACHTControlEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACHTControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACHTControl(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACSequenceNumberIncrementEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACSequenceNumberIncrementEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACSequenceNumberIncrementInterval(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACSequenceNumberIncrementInterval(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACFragmentNumberIncrementEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACFragmentNumberIncrementEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_GetMPDULength(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_GetMACOverheadLength(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetMACFCSEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACFCSEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetAID12(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAID12(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
	
int32 __stdcall niWLANG_SetMACPaddingDuration(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetMACPaddingDuration(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	
	
int32 __stdcall niWLANG_SetCSRequired(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetCSRequired(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetAPTXPower(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAPTXPower(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
		
int32 __stdcall niWLANG_SetTargetRSSI(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetTargetRSSI(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
		
		
int32 __stdcall niWLANG_SetNumberOfDataSymbols(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);
int32 __stdcall niWLANG_GetNumberOfDataSymbols(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
	

int32 __stdcall niWLANG_GetActualOFDMDataRate(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetNotSoundingBit(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNotSoundingBit(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetAllIQImpairmentsEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAllIQImpairmentsEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetAWGNEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAWGNEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetTimeDelay(
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetTimeDelay(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);	

int32 __stdcall niWLANG_SetCarrierToNoiseRatio(
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetCarrierToNoiseRatio(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);

int32 __stdcall niWLANG_SetMACAddress1(
	niWLANGenerationSession session,
	char channelString[],
	int64 value);

int32 __stdcall niWLANG_GetMACAddress1(
	niWLANGenerationSession session,
	char channelString[],
	int64 *value);

int32 __stdcall niWLANG_SetMACAddress2(
	niWLANGenerationSession session,
	char channelString[],
	int64 value);

int32 __stdcall niWLANG_GetMACAddress2(
	niWLANGenerationSession session,
	char channelString[],
	int64 *value);

int32 __stdcall niWLANG_SetMACAddress3(
	niWLANGenerationSession session,
	char channelString[],
	int64 value);

int32 __stdcall niWLANG_GetMACAddress3(
	niWLANGenerationSession session,
	char channelString[],
	int64 *value);

int32 __stdcall niWLANG_SetMACAddress4(
	niWLANGenerationSession session,
	char channelString[],
	int64 value);

int32 __stdcall niWLANG_GetMACAddress4(
	niWLANGenerationSession session,
	char channelString[],
	int64 *value);

	
int32 __stdcall niWLANG_SaveConfigurationToFile(
	niWLANGenerationSession session,
	char filePath[],
	int32 operation);

int32 __stdcall niWLANG_LoadConfigurationFromFile(
	niWLANGenerationSession session,
	char filePath[],
	int32 resetSession);

int32 __stdcall niWLANG_CreateAndWriteWaveformsToFile(
	niWLANGenerationSession session,
	char filePath[],
	int32 fileOperation);

int32 __stdcall niWLANG_SetOFDMGuardIntervalType(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMGuardIntervalType(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		

int32 __stdcall niWLANG_SetLTFSize(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetLTFSize(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetOFDMMidamblePeriodicity(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMMidamblePeriodicity(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_SetOFDMLSIGLength(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMLSIGLength(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetOFDMPreFECPaddingFactor(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMPreFECPaddingFactor(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetOFDMPEDisambiguity(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMPEDisambiguity(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
int32 __stdcall niWLANG_SetOFDMLDPCExtraSymbolsUsed(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMLDPCExtraSymbolsUsed(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);	

int32 __stdcall niWLANG_GetOFDMPacketExtensionDuration(
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetOFDMNominalPacketPadding(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMNominalPacketPadding(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);		
	
	
int32 __stdcall niWLANG_SetOFDMPacketExtensionThresholds(
	niWLANGenerationSession session,
	char channelString[],
	int32 PPET16[],
    int32 PPET8[],
    int32 numberOfSpaceTimeStreams[],
    int32 RUSize[],
    int32 PPET16ArraySize,
    int32 PPET8ArraySize,
    int32 numberOfSpaceTimeStreamsArraySize,
    int32 RUArraySize);
	

int32 __stdcall niWLANG_GetNumberOfUsersFromRUAllocation(
    niWLANGenerationSession session,
	char channelString[],
	int32* numberOfUsers);
	

int32 __stdcall niWLANG_CreateTriggerFrameMSDU(	
	niWLANGenerationSession session,
	char channelString[],
	int32 *generationDone,
	int32 triggerFrameMSDUBits[],
	int32 dataArraySize,
	int32 *actualDataArraySize);
	
int32 __stdcall niWLANG_ReadWaveformFromFile(
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
	
int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211abgjpn(
	float64 channelStartingFrequency, 
	float64 channelBandwidth, 
	int32 channelNumber, 
	int32 secondaryFactor, 
	float64 *carrierFrequency);

int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211ac(
	float64 channelStartingFrequency, 
	int32 channelNumber, 
	float64 *carrierFrequency);

int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211ah(
	float64 channelStartingFrequency, 
	int32 channelNumber, 
	float64 *carrierFrequency);

int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211af (
    float64	channelStartingFrequency,
	float64	channelBandwidth,
	int32 channelNumber,
    int32 TVHTMode,
	float64 *carrierFrequency);	

int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211ax(
	float64 channelStartingFrequency, 
	int32 channelNumber, 
	float64 *carrierFrequency);
	
/*- Utility Functions -----------------------------------------------------*/
int32 __stdcall niWLANG_GetErrorString(
	niWLANGenerationSession session,
	int32 errorCode,
	char errorMessage[],
	int32 errorMessageLen);

int32 __stdcall  niWLANG_ResetSession(
	niWLANGenerationSession session);

int32 __stdcall niWLANG_ReadBurstStartLocationsFromFile(
	char filePath[],
	char waveformName[],
	int32 burstStartLocations[],
	int32 dataArraySize,
	int32 *actualDataArraySize);
	
int32 __stdcall niWLANG_ReadBurstStopLocationsFromFile(
    char filePath[],
	char waveformName[],
	int32 burstStopLocations[],
	int32 dataArraySize,
	int32 *actualdataArraySize);		
	
/*--------------------------------------------------------------------------*/
int32 __stdcall  niWLANG_CloseSession(
	niWLANGenerationSession session);
	
int32 __stdcall niWLANG_DeallocateMemory(void);	


/*-Obsolete Functions --------------------------------------------------------*/
int32 __stdcall niWLANG_SetAutoDataLength(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetAutoDataLength(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);

int32 __stdcall niWLANG_GetWindowLength( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	
int32 __stdcall niWLANG_SetOFDMLegacyScalingEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMLegacyScalingEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
int32 __stdcall niWLANG_SetGuardInterval( 
	niWLANGenerationSession session,
	char channelString[],
	float64 guardInterval);

int32 __stdcall niWLANG_GetGuardInterval( 
	niWLANGenerationSession session,
	char channelString[],
	float64 *value);
	 
int32 __stdcall niWLANG_SetPowerLevel( 
	niWLANGenerationSession session,
	char channelString[],
	float64 value);
	
int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency(
	int32 frequencyBand,
	float64 channelBandwidth,
	int32 channelNumber,
	int32 secondaryFactor, 
	float64 channelStartingFactor,
	float64 *carrierFrequency);

int32 __stdcall niWLANG_SetSIGMCSIndex(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetSIGMCSIndex(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetHESIGBCompressionMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);
	
int32 __stdcall niWLANG_GetHESIGBCompressionMode(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetSIGCompressionEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetSIGCompressionEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);
	
int32 __stdcall niWLANG_SetInterferenceMitigationPilotsEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetInterferenceMitigationPilotsEnabled(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetWaveformFileVersion(
   niWLANGenerationSession session,
   char channelString[],
   int32 value);

int32 __stdcall niWLANG_GetWaveformFileVersion(
   niWLANGenerationSession session,
   char channelString[],
   int32 *value);

int32 __stdcall niWLANG_SetRunTimeScaling(
   niWLANGenerationSession session,
   char channelString[],
   float64 value);

int32 __stdcall niWLANG_GetRunTimeScaling(
   niWLANGenerationSession session,
   char channelString[],
   float64 *value);
	   
#ifdef __cplusplus
}
#endif

#endif //__NIWLAN_TOOLKIT_GENERATION_HEADER_DEFINED__
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niWLANGeneration_Deprecated.h sha256=24622322f714a41cfc65aa5b2aa105d7af8947e1b9a4cbeb2cb366bf17f69db6 bytes=12946 -->
## FILE: imports/include/niWLANGeneration_Deprecated.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niWLANGeneration_Deprecated.h`
- sha256: `24622322f714a41cfc65aa5b2aa105d7af8947e1b9a4cbeb2cb366bf17f69db6`
- bytes: 12946

````c
/****************************************************************************
*          National Instruments WLAN GENERATOR
*---------------------------------------------------------------------------
*   Copyright (c) National Instruments 2008.  All Rights Reserved.
*---------------------------------------------------------------------------
*
* Title:    niWLANGeneration_Deprecated.h
* Purpose:  National Instruments WLAN Generator deprecated
*           functions declarations.
*
****************************************************************************/


#ifndef __NIWLAN_TOOLKIT_GENERATION_DEPRECATED_HEADER_DEFINED__
#define __NIWLAN_TOOLKIT_GENERATION_DEPRECATED_HEADER_DEFINED__

typedef int32		niWLANGv1_Attr;

#ifndef TRUE
#define TRUE            (1L)
#endif
#ifndef FALSE
#define FALSE           (0L)
#endif
#ifndef NULL
#define NULL            (0L)
#endif

/****************************************************************************
*---------------------------- Attribute Defines ---------------------------*
****************************************************************************/

#define NIWLANGV1_STANDARD									0x1F	/*int32*/
#define NIWLANGV1_CARRIER_FREQUENCY							0x0		/*float64*/
#define NIWLANGV1_POWER_LEVEL								0x1		/*float64*/
#define NIWLANGV1_OVERSAMPLING_FACTOR						0x2		/*int32*/
#define NIWLANGV1_WAVEFORM_SCALING_FACTOR					0x24	/*float64*/
#define NIWLANGV1_OFDM_DATA_RATE							0x20	/*int32*/
#define NIWLANGV1_DSSS_DATA_RATE							0x21	/*int32*/
#define NIWLANGV1_IDLE_INTERVAL								0x3		/*float64*/
#define NIWLANGV1_NUMBER_OF_FRAMES							0x6		/*int32*/
#define NIWLANGV1_DSSS_PREAMBLE_TYPE						0x4		/*int32*/
/*- Payload Attributes ----------------------------------------*/
#define NIWLANGV1_PAYLOAD_DATA_LENGTH						0x5		/*int32*/
#define NIWLANGV1_PAYLOAD_DATA_TYPE							0x7		/*int32*/
#define NIWLANGV1_PAYLOAD_PN_ORDER							0x8		/*int32*/
#define NIWLANGV1_PAYLOAD_PN_SEED							0x9		/*int32*/
#define NIWLANGV1_PAYLOAD_USER_DEFINED_BITS					0xA		/*1D Array of int32*/	
#define NIWLANGV1_MAC_HEADER_ENABLED						0xB		/*int32*/
/*- Coding ---------------------------------------------------*/
#define NIWLANGV1_SUBCARRIER_MASK							0xC		/*1D Array of float64*/		
#define NIWLANGV1_LOCKED_CLOCK_BIT_ENABLED					0xD		/*int32*/
#define NIWLANGV1_HEADER_ENCODER_ENABLED					0xE		/*int32*/
#define NIWLANGV1_HEADER_INTERLEAVER_ENABLED				0xF		/*int32*/	
#define NIWLANGV1_PAYLOAD_SCRAMBLER_ENABLED					0x10	/*int32*/	
#define NIWLANGV1_PAYLOAD_SCRAMBLER_SEED					0x11	/*int32*/	
#define NIWLANGV1_PAYLOAD_ENCODER_ENABLED					0x12	/*int32*/
#define NIWLANGV1_PAYLOAD_INTERLEAVER_ENABLED				0x13	/*int32*/
/*- Impairments ---------------------------------------------*/
#define NIWLANGV1_CARRIER_FREQUENCY_OFFSET					0x14	/*float64*/
#define NIWLANGV1_IQ_GAIN_IMBALANCE							0x15	/*float64*/
#define NIWLANGV1_I_DC_OFFSET								0x16	/*float64*/
#define NIWLANGV1_Q_DC_OFFSET								0x17	/*float64*/
#define NIWLANGV1_QUADRATURE_SKEW							0x18	/*float64*/
#define NIWLANGV1_SAMPLE_CLOCK_OFFSET						0x19	/*float64*/
/*- Spectrum Control -----------------------------------------*/
#define NIWLANGV1_PULSE_SHAPING_FILTER_TYPE					0x1A	/*int32*/
#define NIWLANGV1_PULSE_SHAPING_FILTER_PARAMETER			0x1B	/*float64*/
#define NIWLANGV1_WINDOW_LENGTH								0x1D	/*float64*/
	/*------------------------------------------------------------*/
#define NIWLANGV1_PEAK_TO_AVERAGE_POWER_RATIO				0x1E	/*float64, readonly*/
#define NIWLANGV1_IQ_WAVEFORM_SIZE							0x25	/*int32, readonly*/
#define NIWLANG_HE_LTF_SIZE                                 0x90	/*int32*/
#define NIWLANG_NUMBER_OF_HE_LTF_SYMBOLS                    0xA5    /*int32*/
#define NIWLANG_RU_OFFSET                                   0x85    /*int32*/
#define NIWLANG_OVERSAMPLING_FACTOR							0x2		/*int32*/

#define NIWLANG_EHT_SIG_MCS_INDEX                           0xD4    /*int32*/
#define NIWLANG_EHT_SIG_COMPRESSION_ENABLED                 0xD5    /*int32*/

/****************************************************************************
*------------------------ Attribute Value Defines -------------------------*
****************************************************************************/

/*- Values For WLAN Standards -*/
#define NIWLANGV1_VAL_STANDARD_80211AG_OFDM					0
#define NIWLANGV1_VAL_STANDARD_80211BG_DSSS					1
#define NIWLANGV1_VAL_STANDARD_80211G_DSSS_OFDM				2

/*- Values For Preamble Format attribute -*/
#define NIWLANGV1_VAL_PREAMBLE_TYPE_SHORT_PREAMBLE			0
#define NIWLANGV1_VAL_PREAMBLE_TYPE_LONG_PREAMBLE			1

/*- Values For Payload Data Type attribute -*/
#define NIWLANGV1_VAL_USER_DEFINED							0
#define NIWLANGV1_VAL_PN_SEQUENCE							1

/*- Values For Pulse Shaping Filter attribute -*/
#define NIWLANGV1_VAL_FILTER_NONE							0
#define NIWLANGV1_VAL_FILTER_RAISED_COSINE					1
#define NIWLANGV1_VAL_FILTER_ROOT_RAISED_COSINE				2
#define NIWLANGV1_VAL_FILTER_GAUSSIAN						3

/*- Values For OFDM Data Rate attribute -*/
#define NIWLANGV1_VAL_OFDM_DATA_RATE_6						0
#define NIWLANGV1_VAL_OFDM_DATA_RATE_9						1
#define NIWLANGV1_VAL_OFDM_DATA_RATE_12						2
#define NIWLANGV1_VAL_OFDM_DATA_RATE_18						3
#define NIWLANGV1_VAL_OFDM_DATA_RATE_24						4
#define NIWLANGV1_VAL_OFDM_DATA_RATE_36						5
#define NIWLANGV1_VAL_OFDM_DATA_RATE_48						6
#define NIWLANGV1_VAL_OFDM_DATA_RATE_54						7

/*- Values For DSSS Data Rate attribute -*/
#define NIWLANGV1_VAL_DSSS_DATA_RATE_1						0
#define NIWLANGV1_VAL_DSSS_DATA_RATE_2						1
#define NIWLANGV1_VAL_DSSS_DATA_RATE_5p5_CCK				2
#define NIWLANGV1_VAL_DSSS_DATA_RATE_5p5_PBCC				3
#define NIWLANGV1_VAL_DSSS_DATA_RATE_11_CCK					4
#define NIWLANGV1_VAL_DSSS_DATA_RATE_11_PBCC				5
#define NIWLANGV1_VAL_DSSS_DATA_RATE_22						6
#define NIWLANGV1_VAL_DSSS_DATA_RATE_33						7

/* Data Rate and Frame Format:HE-LTF Size */
#define NIWLANG_VAL_HE_LTF_SIZE_AUTO                        -1
#define NIWLANG_VAL_HE_LTF_SIZE_4X                          0
#define NIWLANG_VAL_HE_LTF_SIZE_2X                          1
#define NIWLANG_VAL_HE_LTF_SIZE_1X                          2

/* Data Rate and Frame Format: EHT-SIG Compression Enabled */
#define NIWLANG_VAL_EHT_SIG_COMPRESSION_ENABLED_FALSE					0
#define NIWLANG_VAL_EHT_SIG_COMPRESSION_ENABLED_TRUE					1

#define NIWLANGV1_VAL_MAX_ERROR_MESSAGE_SIZE				1024

/****************************************************************************
*---------------- WLAN Generator Function Declarations ---------------------*
****************************************************************************/

/*- Open and Close Session Functions ---------------------------------------*/
int32 __stdcall  niWLANGv1_OpenSession(
    niWLANGenerationSession *session);

/*- Set Attribute Functions -----------------------------------------------*/

int32 __stdcall niWLANGv1_SetStandard(
    niWLANGenerationSession session,
    char* channelString,
    int32 standard);
/*--------------------------------------------------------------------------*/

int32 __stdcall niWLANGv1_SetCarrierFrequency(
    niWLANGenerationSession session,
    char* channelString,
    float64 carrierFrequency);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_SetPowerLevel(
    niWLANGenerationSession session,
    char* channelString,
    float64 powerLevel);

int32 __stdcall niWLANGv1_SetOFDMDataRate(
    niWLANGenerationSession session,
    char* channelString,
    int32 ofdmDataRate);
/*--------------------------------------------------------------------------*/

int32 __stdcall niWLANGv1_SetDSSSDataRate(
    niWLANGenerationSession session,
    char* channelString,
    int32 dsssDataRate);
/*--------------------------------------------------------------------------*/

int32 __stdcall niWLANGv1_SetDSSSPreambleType(
    niWLANGenerationSession session,
    char* channelString,
    int32 preambleFormat);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_SetIdleInterval(
    niWLANGenerationSession session,
    char* channelString,
    float64 idleInterval);

/*--------------------------------------------------------------------------*/

int32 __stdcall niWLANGv1_SetNumberOfFrames(
    niWLANGenerationSession session,
    char* channelString,
    int32 numberOfFrames);
/*--------------------------------------------------------------------------*/


/*- Set and Get Attribute Functions ----------------------------------------*/
int32 __stdcall  niWLANGv1_SetScalarAttributeF64(
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,
    float64 attributeValue);

/*--------------------------------------------------------------------------*/
int32 __stdcall  niWLANGv1_SetScalarAttributeI32 (
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,
    int32 attributeValue);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_SetVectorAttributeF64 (
    niWLANGenerationSession session,
    char* channelString, 
    niWLANGv1_Attr attributeID,
    float64* array,
    int32 arraySizeInSamples);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_SetVectorAttributeI32 (
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,
    int32* array,
    int32 arraySizeInSamples);


/*--------------------------------------------------------------------------*/
int32 __stdcall  niWLANGv1_GetScalarAttributeF64(
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,
    float64* attributeValue);

/*--------------------------------------------------------------------------*/
int32 __stdcall  niWLANGv1_GetScalarAttributeI32 (
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID, 
    int32* attributeValue);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_GetVectorAttributeF64(
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,
    float64* array,
    int32 arraySizeInSamples,
    int32* actualArraySizeInSamples);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANGv1_GetVectorAttributeI32(
    niWLANGenerationSession session,
    char* channelString,
    niWLANGv1_Attr attributeID,	
    int32* array,
    int32 arraySizeInSamples, 
    int32* actualArraySizeInSamples);	

/*- Create Waveform Function -----------------------------------------------*/
int32 __stdcall  niWLANGv1_CreateWaveformComplexF64(
    niWLANGenerationSession session,
    int32 reset,
    float64* t0,
    float64* dt,
    NIComplexNumber* waveform,
    int32 waveformSize,
    int32* actualNumWaveformSamples,
    int32* done);

/*- Get Error Function -----------------------------------------------------*/
int32 __stdcall niWLANGv1_GetErrorString(
    int32 errorCode,
    char errorMessage[],
    int32 errorMessageLen);

/*--------------------------------------------------------------------------*/
int32 __stdcall  niWLANGv1_CloseSession(
    niWLANGenerationSession session);

/*--------------------------------------------------------------------------*/
int32 __stdcall niWLANG_SetOFDMHELTFSize(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetOFDMHELTFSize(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetNumberOfHELTFSymbols(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetNumberOfHELTFSymbols(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetRUOffset(
	niWLANGenerationSession session,
	char channelString[],
	int32 ofdmDataRate);

int32 __stdcall niWLANG_GetRUOffset(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetOverSamplingFactor( 
	niWLANGenerationSession session,
	char channelString[],
	int32 overSamplingFactor);

int32 __stdcall niWLANG_GetOverSamplingFactor( 
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

int32 __stdcall niWLANG_SetEHTSIGMCSIndex(
	niWLANGenerationSession session,
	char channelString[],
	int32 value);

int32 __stdcall niWLANG_GetEHTSIGMCSIndex(
	niWLANGenerationSession session,
	char channelString[],
	int32 *value);

#endif //__NIWLAN_TOOLKIT_GENERATION_DEPRECATED_HEADER_DEFINED__
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niWLANGenerationRfsg.h sha256=4ee2003920b3c5f3319772c2d5c5d79ccc1f214016ba7aae171623e7c3d11443 bytes=6819 -->
## FILE: imports/include/niWLANGenerationRfsg.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niWLANGenerationRfsg.h`
- sha256: `4ee2003920b3c5f3319772c2d5c5d79ccc1f214016ba7aae171623e7c3d11443`
- bytes: 6819

````c
/****************************************************************************
 *          National Instruments WLAN GENERATOR
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2010.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niWLANGenerationRfsg.h
 * Purpose:  National Instruments WLAN Generator
 *           functions declarations.
 *
 ****************************************************************************/



#ifndef __NIWLAN_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__
#define __NIWLAN_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__


#include <niRFSG.h>
#include "niWLANGeneration.h"
#include "niWLANGenerationRfsg_Deprecated.h"

#ifdef __cplusplus
extern "C"
{
#endif
	
/*- Configure Functions ---------------------------------------*/
int32 __stdcall  niWLANG_RFSGConfigure(
	niWLANGenerationSession session,
	char wlanChannelString[],
	ViSession rfsgSession,
	char hwChannelString[]);
	
int32 __stdcall niWLANG_RFSGConfigureMultipleDeviceSynchronization(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
	int32 noOfChannels, 
	char masterReferenceClockSource[], 
	int32 triggerLines[], 
	int32 noOfTriggerLines);
	
int32 __stdcall niWLANG_RFSGConfigureSampleClockDelay(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
	float64 sampleClockDelay[], 
	int32 noOfChannels);	

int32 __stdcall niWLANG_RFSGForceTClkSynchronization(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
	int32 numberOfRFSGSessions, 
	int32 forceSync
);	

int32 __stdcall niWLANG_RFSGMultipleDeviceInitiate(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
	int32 numberOfRFSGSessions
);	

int32 __stdcall niWLANG_RFSGConfigureFrequencySingleLO(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
    int32 numberOfRFSGSessions,
	int32 LOSource,
	ViSession externalLOHandle,
    float64 carrierFrequency, 
	int32 rfsgLODaisyChainEnabled,
    int32 LOExportToExternalDevicesEnabled); 	
	
int32 __stdcall niWLANG_RFSGConfigureFrequencyMultipleLO(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[],
	int32 numberOfRFSGSessions,	
	int32 LOSource,
	ViSession externalLOHandles[],
	int32 numberOfexteralLOHandles,
	float64 carrierFrequency[],
	int32 dataArraySize,
	int32 rfsgLODaisyChainEnabled,
    int32 LOExportToExternalDevicesEnabled); 			
	
/*-------------------- ---------------------------------------*/
int32 __stdcall  niWLANG_RFSGConfigureWaveform(
	niWLANGenerationSession session,
	char wlanChannelString[],
	ViSession rfsgSession,
	char hwChannelString[],
	int32 resetHardware,
	int32* waveformSize);
	
/*- RFSG Database ---------------------------------------------------------*/

int32 __stdcall niWLANG_RFSGStorePAPR(
	ViSession rfsgSession, 
	char channelString[],
	char waveformName[], 
	float64 PAPR);
	
int32 __stdcall niWLANG_RFSGStoreIQRate(
	ViSession rfsgSession, 
	char channelString[],
	char waveformName[], 
	float64 IQRate);
	
int32 __stdcall niWLANG_RFSGStoreBurstStartLocations(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 burstStartLocations[],
    int32 dataArraySize);	
	
int32 __stdcall niWLANG_RFSGStoreBurstStopLocations(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 burstStopLocations[],
	int32 dataArraySize);	
	
int32 __stdcall niWLANG_RFSGRetrievePAPR(
	ViSession rfsgSession, 
	char channelString[],
	char waveformName[], 
	float64 *PAPR);
	
int32 __stdcall niWLANG_RFSGRetrieveMinimumPAPRAllWaveforms(
	ViSession rfsgSession, 
	char channelString[],
	char script[], 
	float64 *PAPR);
	
int32 __stdcall niWLANG_RFSGRetrieveIQRate(
	ViSession rfsgSession, 
	char channelString[],
	char waveformName[], 
	float64 *IQRate);
	
int32 __stdcall niWLANG_RFSGRetrieveIQRateAllWaveforms(
	ViSession rfsgSession, 
	char channelString[],
	char script[], 
	float64 *IQRate);

int32 __stdcall niWLANG_RFSGRetrieveRFBlankingMarkerPositions(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 rfBlankingMarkerPositions[], 
	int32 rfBlankingMarkerPositionsArraySize, 
	int32 *actualRFBlankingMarkerPositionsArraySize);	

int32 __stdcall niWLANG_RFSGRetrieveBurstStartLocations(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 burstStartLocations[],
	int32 dataArraySize,
	int32* actualDataArraySize);
	
int32 __stdcall niWLANG_RFSGRetrieveBurstStopLocations(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 burstStopLocations[],
	int32 dataArraySize,
	int32* actualDataArraySize);
	
int32 __stdcall niWLANG_RFSGRetrieveWaveformSize(
	ViSession rfsgSession, 
	char waveformName[], 
	int32* waveformSize);
	
int32 __stdcall niWLANG_RFSGCreateAndDownloadWaveform(
	niWLANGenerationSession session, 
	ViSession rfsgSession, 
	char hwChannelString[],
	char waveformName[]);	
	
int32 __stdcall niWLANG_RFSGCreateAndDownloadMIMOWaveforms(
	niWLANGenerationSession session, 
	ViSession rfsgSessions[], 
	char hwChannelStrings[],
	int32 numberOfTxChains, 
	char waveformName[]);
	
int32 __stdcall niWLANG_RFSGConfigureScript(
	ViSession rfsgSession, 
	char channelString[],
	char script[], 
	float64 powerLevel);
	
int32 __stdcall niWLANG_RFSGConfigurePowerLevel(
	ViSession rfsgSession, 
	char channelString[],
	char script[], 
	float64 powerLevel);
	
int32 __stdcall niWLANG_RFSGClearDatabase(
	ViSession rfsgSession, 
	char channelString[],
	char waveformName[]);
	
int32 __stdcall niWLANG_RFSGReadAndDownloadWaveformsFromFile(
	ViSession rfsgSessions[], 
	int32 numberOfChannels, 
	char waveformName[], 
	char filePath[]);	
	
int32 __stdcall niWLANG_RFSGStoreRFBlankingMarkerPositions(
	ViSession rfsgSession, 
	char waveformName[], 
	int32 rfBlankingMarkerPositions[], 
	int32 rfBlankingMarkerPositionsArraySize);

int32 __stdcall niWLANG_RFSGInsertRFBlankingMarkerPositions(
	ViSession rfsgSession, 
	char script[], 
	char scriptOut[], 
	int32 lenOfScriptOut, 
	int32 *actualLenOfScriptOut);
	
/*- Obsolete ---------------------------------------------------------*/	
int32 __stdcall niWLANG_RFSGAutoTriggerRoute(
	ViSession rfsgHandles[], 
	int32 noOfChannels, 
	char triggerLine[], 
	int32 lenOfTrigLine, 
	char reference[], 
	int32 lenOfReference, 
	int32 *isInSameBus, 
	int32 busNumber[], 
	int32 sizeOfBusNo, 
	int32 *isDefaultLineSelected);
	
int32 __stdcall niWLANG_RFSGTriggerUnroute(
	char triggerLine[], 
	char reference[], 
	int32 isInSameBus, 
	int32 busNumber[], 
	int32 sizeOfBusNo, 
	int32 isDefaultLineSelected);	
	
#ifdef __cplusplus
}
#endif

#endif //__NIWLAN_TOOLKIT_GENERATION_RFSG_HEADER_DEFINED__
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niWLANGenerationRfsg_Deprecated.h sha256=73f47fc093afe97ed4321ffe61a1afde123b1211e342c0ad8da964e4978929f3 bytes=1335 -->
## FILE: imports/include/niWLANGenerationRfsg_Deprecated.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niWLANGenerationRfsg_Deprecated.h`
- sha256: `73f47fc093afe97ed4321ffe61a1afde123b1211e342c0ad8da964e4978929f3`
- bytes: 1335

````c
/****************************************************************************
 *          National Instruments WLAN GENERATOR
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2008.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niWLANGenerationRfsg_Deprecated.h
 * Purpose:  National Instruments WLAN Generator deprecated
 *           functions declarations.
 *
 ****************************************************************************/



#ifndef __NIWLAN_TOOLKIT_GENERATION_RFSG_DEPRECATED_HEADER_DEFINED__
#define __NIWLAN_TOOLKIT_GENERATION_RFSG_DEPRECATED_HEADER_DEFINED__

#ifdef __cplusplus
extern "C"
{
#endif

	
/*- Configure Functions ---------------------------------------*/
int32 __stdcall  niWLANGv1_ConfigureRFSG(
	niWLANGenerationSession session,
	ViSession rfsgSession,
	char* channelString);

/*-------------------- ---------------------------------------*/
int32 __stdcall  niWLANGv1_ConfigureWaveform(
	niWLANGenerationSession session,
	ViSession rfsgSession,
	char* channelString,
	int32 resetHardware,
	int32* waveformSize);
	
	
#ifdef __cplusplus
}
#endif

#endif //__NIWLAN_TOOLKIT_GENERATION_RFSG_DEPRECATED_HEADER_DEFINED__
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nixnet.h sha256=71b452f7236bae8eb5b34742c2826956a047624aab37aa7904fa3d5eb6ba6391 bytes=208802 -->
## FILE: imports/include/nixnet.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nixnet.h`
- sha256: `71b452f7236bae8eb5b34742c2826956a047624aab37aa7904fa3d5eb6ba6391`
- bytes: 208802

````c
/*!
   \file nixnet.h
   \brief NI-XNET C API Implementation
*/
/*
   Copyright (c) 2008 National Instruments Corporation.
   All rights reserved.
*/

#ifndef ___nixnet_h___
#define ___nixnet_h___

#if defined(__GNUC__)
#include <stdint.h>   // C99 typedef for GCC
#endif


/***********************************************************************
                     C O M P I L E R   D E F I N E S
***********************************************************************/

   /* Needed for C++ to C (DLL) calls  */
#ifdef __cplusplus
   extern "C" {
#endif


#if defined(_WIN32)
   #define  _NXFUNC __cdecl
#else
   #define  _NXFUNC
#endif

#ifdef _CVI_
   #pragma  EnableLibraryRuntimeChecking
#endif /* _CVI_ */

/***********************************************************************
                              S T A T U S
***********************************************************************/

#define NX_STATUS_QUALIFIER                             (nxStatus_t)(0x3FF63000)
#define NX_STATUS_WARNING                               (nxStatus_t)(0x00000000)
#define NX_STATUS_ERROR                                 (nxStatus_t)(0x80000000)

#define NX_WARNING_BASE                                 (NX_STATUS_QUALIFIER | NX_STATUS_WARNING)
#define NX_ERROR_BASE                                   (NX_STATUS_QUALIFIER | NX_STATUS_ERROR)

#define nxSuccess                                       (0)

   // For a description of each error/warning (including solutions), use
   // nxStatusToString

//! An internal error occurred in the NI-XNET driver. Solution: Contact National
//! Instruments and provide the log files found in %LOCALAPPDATA%\National
//! Instruments\NI-XNET\log. Note that this location might be hidden on your
//! computer. For LabVIEW RT systems, log files are located in /ni-rt/nixnet/log
//! or /var/lib/ni-xnet/log.
#define nxErrInternalError                              (nxStatus_t)(0xBFF63001) // -1074384895

//! Board self test failed(code 2). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError1                             (nxStatus_t)(0xBFF63002) // -1074384894

//! Board self test failed(code 3). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError2                             (nxStatus_t)(0xBFF63003) // -1074384893

//! Board self test failed(code 4). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError3                             (nxStatus_t)(0xBFF63004) // -1074384892

//! Board self test failed(code 5). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError4                             (nxStatus_t)(0xBFF63005) // -1074384891

//! Board self test failed(code 6). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError5                             (nxStatus_t)(0xBFF63006) // -1074384890

//! Computer went to hibernation mode and the board lost power. Solution:
//! Prevent the computer from going to hibernation mode in the control panel.
#define nxErrPowerSuspended                             (nxStatus_t)(0xBFF63007) // -1074384889

//! A write queue overflowed. Solution: Wait until queue space becomes available
//! and retry.
#define nxErrOutputQueueOverflow                        (nxStatus_t)(0xBFF63008) // -1074384888

//! The board's firmware did not answer a command. Solution: Stop your
//! application and execute a self test. Try deactivating/reactivating the
//! driver in the Device Manager. If the problem persists, contact National
//! Instruments.
#define nxErrFirmwareNoResponse                         (nxStatus_t)(0xBFF63009) // -1074384887

//! The operation timed out. Solution: Specify a timeout long enough to complete
//! the operation, or change the operation in a way that it can get completed in
//! less time (e.g., read less data).
#define nxErrEventTimeout                               (nxStatus_t)(0xBFF6300A) // -1074384886

//! A read queue overflowed. Solution: Reduce your data rate or call Read more
//! frequently.
#define nxErrInputQueueOverflow                         (nxStatus_t)(0xBFF6300B) // -1074384885

//! The Read buffer is too small to hold a single frame. Solution: Provide a
//! buffer large enough.
#define nxErrInputQueueReadSize                         (nxStatus_t)(0xBFF6300C) // -1074384884

//! You tried to open the same frame twice. This is not permitted. Solution:
//! Open each frame only once.
#define nxErrDuplicateFrameObject                       (nxStatus_t)(0xBFF6300D) // -1074384883

//! You tried to open the same stream object twice. This is not permitted.
//! Solution: Open each stream object only once.
#define nxErrDuplicateStreamObject                      (nxStatus_t)(0xBFF6300E) // -1074384882

//! Self test is not possible since the board is in use by an application.
//! Solution: Stop all NI-XNET applications before executing a self test.
#define nxErrSelfTestNotPossible                        (nxStatus_t)(0xBFF6300F) // -1074384881

//! Allocation of memory failed. You do not have sufficient memory in the
//! LabVIEW target. Solution: Add more RAM or try to use fewer resources in your
//! applications (arrays, XNET sessions, etc).
#define nxErrMemoryFull                                 (nxStatus_t)(0xBFF63010) // -1074384880

//! The maximum number of sessions was exceeded. Solution: Use fewer sessions.
#define nxErrMaxSessions                                (nxStatus_t)(0xBFF63011) // -1074384879

//! The maximum number of frames has been exceeded. Solution: Use fewer frames
//! in your sessions.
#define nxErrMaxFrames                                  (nxStatus_t)(0xBFF63012) // -1074384878

//! The maximum number of devices has been detected. Solution: Use fewer
//! devices.
#define nxErrMaxDevices                                 (nxStatus_t)(0xBFF63013) // -1074384877

//! A driver support file is missing. Solution: Try reinstalling the driver. If
//! the error persists, contact National Instruments.
#define nxErrMissingFile                                (nxStatus_t)(0xBFF63014) // -1074384876

//! This indicates that a NULL pointer or an empty string was passed to a
//! function. The user should verify that the parameters passed in make sense
//! for the given function.
#define nxErrParameterNullOrEmpty                       (nxStatus_t)(0xBFF63015) // -1074384875

//! The maximum number of schedules has been detected. Solution: Use fewer
//! schedules.
#define nxErrMaxSchedules                               (nxStatus_t)(0xBFF63016) // -1074384874

//! Board self test failed (code 17). Solution: Try reinstalling the driver or
//! switching the slot(s) of the board(s). If the error persists, contact
//! National Instruments.
#define nxErrSelfTestError6                             (nxStatus_t)(0xBFF63017) // -1074384873

//! You cannot start an NI-XNET application while a self test is in progress.
//! Solution: Complete the self test before starting any NI-XNET applications.
#define nxErrSelfTestInProgress                         (nxStatus_t)(0xBFF63018) // -1074384872

//! The session contains a PDU with an offset that is not byte-aligned. Only
//! byte-aligned PDUs are supported for PDU sessions.
#define nxErrNonByteAlignedPDU                          (nxStatus_t)(0xBFF63019) // -1074384871

//! An invalid reference has been passed to a NI-XNET session function.
//! Solution: Only pass reference retrieved from Create Session, or from an IO
//! name of a session in LabVIEW project.
#define nxErrInvalidSessionHandle                       (nxStatus_t)(0xBFF63020) // -1074384864

//! An invalid reference has been passed to a NI-XNET system function. Solution:
//! Only pass a valid system reference.
#define nxErrInvalidSystemHandle                        (nxStatus_t)(0xBFF63021) // -1074384863

//! A device reference was expected for a NI-XNET session function. Solution:
//! Only pass a device reference.
#define nxErrDeviceHandleExpected                       (nxStatus_t)(0xBFF63022) // -1074384862

//! An interface reference was expected for a NI-XNET session function.
//! Solution: Only pass an interface reference.
#define nxErrIntfHandleExpected                         (nxStatus_t)(0xBFF63023) // -1074384861

//! You have configured a property that conflicts with the current mode of the
//! session. For example, you have created a CAN output session with a frame
//! configured with a Timing Type = Cyclic and a Transmit Time of 0.
#define nxErrPropertyModeConflicting                    (nxStatus_t)(0xBFF63024) // -1074384860

//! The XNET Create Timing Source VI is supported only on LabVIEW Real-Time
//! targets currently running the Phar Lap ETS Real-Time Operating System.
#define nxErrTimingSourceNotSupported                   (nxStatus_t)(0xBFF63025) // -1074384859

//! You tried to create more than one LabVIEW timing source for a single
//! interface. Only one timing source per interface is supported. The timing
//! source remains until the top-level VI is idle (no longer running). Solution:
//! Call the XNET Create Timing Source VI only once per interface. You can use
//! the timing source with multiple timed structures (e.g., timed loops).
#define nxErrMultipleTimingSource                       (nxStatus_t)(0xBFF63026) // -1074384858

//! You invoked two or more VIs simultaneously for the same session, and those
//! VIs do not support overlap. For example, you attempted to invoke two Read
//! VIs at the same time for the same session. Solution: Wire the error cluster
//! from one VI to another, to enforce sequential execution for the session.
#define nxErrOverlappingIO                              (nxStatus_t)(0xBFF63027) // -1074384857

//! You are trying to start an interface that is missing bus power for the
//! transceiver. Some physical layers on NI-XNET hardware are internally
//! powered, but others require external power for the port to operate. This
//! error occurs when starting an interface on hardware that requires external
//! power when no power is detected. Solution: Supply proper voltage to your
//! transceiver. Refer to the NI-XNET Hardware Overview in the NI-XNET Hardware
//! and Software Manual for more information.
#define nxErrMissingBusPower                            (nxStatus_t)(0xBFF63028) // -1074384856

//! The connection with a CompactDAQ chassis was lost, and the host software and
//! modules are out of sync.  There is no direct recovery for this problem until
//! the chassis is reset. Solutions: Call DAQmx Reset Device as the first VI or
//! function in your application, prior to creating XNET sessions. Alternately,
//! you could reset the CompactDAQ chassis in Measurement and Automation
//! Explorer (MAX).
#define nxErrCdaqConnectionLost                         (nxStatus_t)(0xBFF63029) // -1074384855

//! The transceiver value set is invalid (for this port, e.g., LS on a HS port)
//! or you are trying to perform an operation that requires a different
//! transceiver (e.g., trying to change the state of a disconnected
//! transceiver). Solution: Set a valid value.
#define nxErrInvalidTransceiver                         (nxStatus_t)(0xBFF63071) // -1074384783

//! The baud rate value set is invalid. Solution: Set a valid value.
#define nxErrInvalidBaudRate                            (nxStatus_t)(0xBFF63072) // -1074384782

//! No baud rate value has been set. Solution: Set a valid value.
#define nxErrBaudRateNotConfigured                      (nxStatus_t)(0xBFF63073) // -1074384781

//! The bit timing values set are invalid. Solution: Set valid values.
#define nxErrInvalidBitTimings                          (nxStatus_t)(0xBFF63074) // -1074384780

//! The baud rate set does not match the transceiver's allowed range. Solution:
//! Change either the baud rate or the transceiver.
#define nxErrBaudRateXcvrMismatch                       (nxStatus_t)(0xBFF63075) // -1074384779

//! The configured terminal is not known for this interface. Solution: Make sure
//! that that you pass in a valid value to Connect Terminals or Disconnect
//! Terminals.
#define nxErrUnknownTimingSource                        (nxStatus_t)(0xBFF63076) // -1074384778

//! The configured terminal is inappropriate for the hardware. For example,
//! setting a source to FrontPanel0 on XNET hardware that does not have
//! front-panel trigger inputs, or selecting PXI_Clk10 for a non-PXI device.
//! Solution: Pick an appropriate terminal for the hardware.
#define nxErrUnknownSynchronizationSource               (nxStatus_t)(0xBFF63077) // -1074384777

//! The source that you connected to the Master Timebase destination is missing.
//! When the start trigger is received, the interface verifies that a signal is
//! present on the configured source. This check has determined that this signal
//! is missing. Solution: Verify that your cables are configured correctly and
//! that your timebase source is generating an appropriate waveform.
#define nxErrMissingTimebaseSource                      (nxStatus_t)(0xBFF63078) // -1074384776

//! The source that you connected to the Master Timebase destination is not
//! generating an appropriate signal. When the start trigger is received, the
//! interface verifies that a signal of a known frequency is present on the
//! configured source. This check has determined that this source is generating
//! a signal, but that the signal is not one of the supported frequencies for
//! this hardware. Solution: Verify that your source is generating a signal at a
//! supported frequency.
#define nxErrUnknownTimebaseFrequency                   (nxStatus_t)(0xBFF63079) // -1074384775

//! You are trying to disconnect a synchronization terminal that is not
//! currently connected. Solution: Only disconnect synchronization terminals
//! that have previously been connected.
#define nxErrUnconnectedSynchronizationSource           (nxStatus_t)(0xBFF6307A) // -1074384774

//! You are trying to connect a synchronization terminal that is already in use.
//! For example, you are trying to connect a trigger line to the Master Timebase
//! when a different trigger line is already connected to the Master Timebase.
//! Solution: Only connect to synchronization terminals that are not currently
//! in use.
#define nxErrConnectedSynchronizationTerminal           (nxStatus_t)(0xBFF6307B) // -1074384773

//! You are trying to connect an XNET terminal as a source terminal,  but the
//! desired XNET terminal is not valid as a source terminal. Solution: Only
//! connect valid source terminals to the source terminal in XNET Connect
//! Terminals.
#define nxErrInvalidSynchronizationSource               (nxStatus_t)(0xBFF6307C) // -1074384772

//! You are trying to connect an XNET terminal as a destination terminal, but
//! the desired XNET terminal is not valid as a destination terminal. Solution:
//! Only connect valid destination terminals to the destination terminal in XNET
//! Connect Terminals.
#define nxErrInvalidSynchronizationDestination          (nxStatus_t)(0xBFF6307D) // -1074384771

//! You are trying to connect two XNET terminals that are incompatible.
//! Solution: Only connect a source and destination terminals that are
//! compatible with each other.
#define nxErrInvalidSynchronizationCombination          (nxStatus_t)(0xBFF6307E) // -1074384770

//! The source that you connected to the Master Timebase destination has
//! disappeared. When the start trigger is received, the interface verifies that
//! a signal is present on the configured source. This check has determined that
//! this signal was present, but while the interface was running, the signal
//! disappeared, so all timebase configuration has reverted to using the onboard
//! (unsynchronized) oscillator. Solution: Verify that your cables are
//! configured correctly and that your timebase source is generating an
//! appropriate waveform the entire time your application is running.
#define nxErrTimebaseDisappeared                        (nxStatus_t)(0xBFF6307F) // -1074384769

//! You called Read (State : FlexRay : Cycle Macrotick), and the FlexRay
//! Macrotick is not connected as the master timebase of the interface.
//! Solution: Call Connect Terminals to connect source of FlexRay Macrotick to
//! destination of Master Timebase.
#define nxErrMacrotickDisconnected                      (nxStatus_t)(0xBFF63080) // -1074384768

//! The database specified could not be opened. Solution: Check that the alias
//! and/or the file exists and that it is a valid database. Also, make sure the
//! path does not contain Unicode characters, which cannot be utilized by
//! NI-XNET.
#define nxErrCannotOpenDatabaseFile                     (nxStatus_t)(0xBFF63081) // -1074384767

//! The cluster was not found in the database. Solution: Make sure you only
//! initialize a cluster in a session that is defined in the database.
#define nxErrClusterNotFound                            (nxStatus_t)(0xBFF63082) // -1074384766

//! The frame was not found in the database. Solution: Make sure you only
//! initialize frames in a session that are defined in the database.
#define nxErrFrameNotFound                              (nxStatus_t)(0xBFF63083) // -1074384765

//! The signal was not found in the database. Solution: Make sure you only
//! initialize signals in a session that are defined in the database.
#define nxErrSignalNotFound                             (nxStatus_t)(0xBFF63084) // -1074384764

//! A necessary property for a cluster was not found in the database. Solution:
//! Make sure you only initialize a cluster in a session that is completely
//! defined in the database.
#define nxErrUnconfiguredCluster                        (nxStatus_t)(0xBFF63085) // -1074384763

//! A necessary property for a frame was not found in the database. Solution:
//! Make sure you only initialize frames in a session that are completely
//! defined in the database.
#define nxErrUnconfiguredFrame                          (nxStatus_t)(0xBFF63086) // -1074384762

//! A necessary property for a signal was not found in the database. Solution:
//! Make sure you only initialize signals in a session that are completely
//! defined in the database.
#define nxErrUnconfiguredSignal                         (nxStatus_t)(0xBFF63087) // -1074384761

//! Multiple clusters have been specified in one session, either directly
//! (Stream I/O), or through the signals or frames specified. Solution: Make
//! sure that in one session, you open only one cluster, including frames or
//! signals that belong to the same cluster.
#define nxErrMultipleClusters                           (nxStatus_t)(0xBFF63088) // -1074384760

//! You specified a database of ':subordinate:' for a session mode other than
//! mode of Frame Input Stream. Solution: Either open a Frame Input Stream
//! session, or use a real or in-memory database.
#define nxErrSubordinateNotAllowed                      (nxStatus_t)(0xBFF63089) // -1074384759

//! The interface name given does not specify a valid and existing interface.
//! Solution: Use a valid and existing interface. On Windows, these may be found
//! in MAX. On Linux distributions, interface names can be queried with either
//! the lsni or nixnetconfig command line tools. Interface names can also be
//! obtained using XNET system properties, or the LabVIEW XNET Interface IO
//! name. If you are using CompactRIO, refer to the topic "Getting Started with
//! CompactRIO" in the NI-XNET Hardware and Software Help.
#define nxErrInvalidInterface                           (nxStatus_t)(0xBFF6308A) // -1074384758

//! The operation is invalid for this interface (e.g., you tried to open a set
//! of FlexRay frames on a CAN interface, or tried to request a CAN property
//! from a FlexRay interface). Solution: Run this operation on a suitable
//! interface.
#define nxErrInvalidProtocol                            (nxStatus_t)(0xBFF6308B) // -1074384757

//! You tried to set the AutoStart property to FALSE for an Input session. This
//! is not allowed. Solution: Do not set the AutoStart property (TRUE is
//! default).
#define nxErrInputSessionMustAutoStart                  (nxStatus_t)(0xBFF6308C) // -1074384756

//! The property ID you specified is not valid (or not valid for the current
//! session mode or form factor). Check to make sure the installed XNET driver
//! supports the specified property ID.
#define nxErrInvalidPropertyId                          (nxStatus_t)(0xBFF6308D) // -1074384755

//! The contents of the property is bigger than the size specified. Use the
//! nxGetPropertySize function to determine the size of the buffer needed.
#define nxErrInvalidPropertySize                        (nxStatus_t)(0xBFF6308E) // -1074384754

//! The function you called is not defined for the session mode (e.g., you
//! called a frame I/O function on a signal I/O session).
#define nxErrIncorrectMode                              (nxStatus_t)(0xBFF6308F) // -1074384753

//! The data that you passed to XNET Write or XNET Read is too small to hold all
//! the data specified for the session. Solution: Determine the number of
//! elements (frames or signals) that you configured for the session, and pass
//! that number of elements to XNET Write or XNET Read.
#define nxErrBufferTooSmall                             (nxStatus_t)(0xBFF63090) // -1074384752

//! For Signal Output sessions, the multiplexer signals used in the session must
//! be specified explicitly in the signal list.
#define nxErrMustSpecifyMultiplexers                    (nxStatus_t)(0xBFF63091) // -1074384751

//! You used an XNET Session IO name, and that session was not found in your
//! LabVIEW project. Solution: Within LabVIEW project, right-click the target
//! (RT or My Computer), and select New > NI-XNET Session. Add the VI that uses
//! the session under the target. If you are using the session with a built
//! application (.EXE), ensure that you copy the built configuration file
//! nixnetSession.txt such that it resides in the same folder as the executable.
#define nxErrSessionNotFound                            (nxStatus_t)(0xBFF63092) // -1074384750

//! You used the same XNET session name in multiple top-level VIs, which is not
//! supported. Solution: Use each session in only one top-level VI (application)
//! at a time.
#define nxErrMultipleUseOfSession                       (nxStatus_t)(0xBFF63093) // -1074384749

//! To execute this function properly, the session's list must contain only one
//! frame. Solution: Break your session up into multiple, each of which contains
//! only one frame.
#define nxErrOnlyOneFrame                               (nxStatus_t)(0xBFF63094) // -1074384748

//! You used the same alias for different database files which is not allowed.
//! Solution: Use each alias only for a single database file.
#define nxErrDuplicateAlias                             (nxStatus_t)(0xBFF63095) // -1074384747

//! You try to deploy a database file while another deployment is in progress.
//! Solution: Wait until the other deployment has finished and try again.
#define nxErrDeploymentInProgress                       (nxStatus_t)(0xBFF63096) // -1074384746

//! A signal or frame session has been opened, but it does not contain signals
//! or frames. Solution: Specify at least one signal or frame.
#define nxErrNoFramesOrSignals                          (nxStatus_t)(0xBFF63097) // -1074384745

//! The session mode selected is not supported by the protocol of the specified
//! interface. Solution: Choose a valid session mode.
#define nxErrInvalidMode                                (nxStatus_t)(0xBFF63098) // -1074384744

//! A session was created by references, but no database references have been
//! specified. Solution: Specify at least one appropriate database reference
//! (i.e., signal or frame or cluster ref depending on the session mode).
#define nxErrNeedReference                              (nxStatus_t)(0xBFF63099) // -1074384743

//! The interface has already been opened with different cluster settings than
//! the ones specified for this session. Solution: Make sure that the cluster
//! settings agree for the interface, or use a different interface.
#define nxErrDifferentClusterOpen                       (nxStatus_t)(0xBFF6309A) // -1074384742

//! The cycle repetition of a frame in the database for the FlexRay protocol is
//! invalid. Solution: Make sure that the cycle repetition is a power of 2
//! between 1 and 64.
#define nxErrFlexRayInvalidCycleRep                     (nxStatus_t)(0xBFF6309B) // -1074384741

//! You called XNET Clear for the session, then tried to perform another
//! operation. Solution: Defer clear (session close) until you are done using
//! it. This error can also occur if you branch a wire after creating the
//! session. Solution: Do not branch a session to multiple flows in the diagram.
#define nxErrSessionCleared                             (nxStatus_t)(0xBFF6309C) // -1074384740

//! You called Create Session VI with a list of items that does not match the
//! mode. This includes using: 1) signal items for a Frame I/O mode 2) frame
//! items for a Signal I/O mode 3) cluster item for a mode other than Frame
//! Input Stream or Frame Output Stream
#define nxErrWrongModeForCreateSelection                (nxStatus_t)(0xBFF6309D) // -1074384739

//! You tried to create a new session while the interface is already running.
//! Solution: Create all sessions before starting any of them.
#define nxErrInterfaceRunning                           (nxStatus_t)(0xBFF6309E) // -1074384738

//! The length of the payload written is larger than the maximum payload size
//! allowed.
#define nxErrPayloadTooLarge                            (nxStatus_t)(0xBFF6309F) // -1074384737
#define nxErrFrameWriteTooLarge                         (nxErrPayloadTooLarge)

//! You called a Read function with a nonzero timeout, and you used a negative
//! numberToRead. Negative value for numberToRead requests all available data
//! from the Read, which is ambiguous when used with a timeout. Solutions: 1)
//! Pass timeout of 0 and numberToRead of -1, to request all available data. 2)
//! Pass timeout > 0, and numberToRead > 0, to wait for a specific number of
//! data elements.
#define nxErrTimeoutWithoutNumToRead                    (nxStatus_t)(0xBFF630A0) // -1074384736

//! Timestamps are not (yet) supported for Write Signal XY. Solution: Do not
//! provide a timestamp array for Write Signal XY.
#define nxErrTimestampsNotSupported                     (nxStatus_t)(0xBFF630A1) // -1074384735

//! The condition parameter passed to Wait is not known. Solution: Pass a valid
//! parameter.
#define nxErrUnknownCondition                           (nxStatus_t)(0xBFF630A2) // -1074384734

//! You attempted an I/O operation, but the session is not yet started (and the
//! AutoStart property is set to FALSE). Solution: Call Start before you use
//! this I/O operation.
#define nxErrSessionNotStarted                          (nxStatus_t)(0xBFF630A3) // -1074384733

//! The maximum number of Wait operations has been exceeded. Solution: If you
//! are waiting for multiple events on the interface, use fewer Wait operations
//! on this interface (even for multiple sessions). If you are waiting for
//! multiple events for a frame (e.g., transmit complete), use only one Wait at
//! a time for that frame.
#define nxErrMaxWaitsExceeded                           (nxStatus_t)(0xBFF630A4) // -1074384732

//! You used an invalid name for an XNET Device. Solution: Get valid XNET Device
//! names from the XNET System properties (only).
#define nxErrInvalidDevice                              (nxStatus_t)(0xBFF630A5) // -1074384731

//! A terminal name passed to ConnectTerminals or DisconnectTerminals is
//! unknown. Solution: Only pass valid names.
#define nxErrInvalidTerminalName                        (nxStatus_t)(0xBFF630A6) // -1074384730

//! You tried to blink the port LEDs but these are currently busy. Solution:
//! Stop all applications running on that port; do not access it from MAX or LV
//! Project.
#define nxErrPortLEDsBusy                               (nxStatus_t)(0xBFF630A7) // -1074384729

//! You tried to set a FlexRay keyslot ID that is not listed as valid in the
//! database. Solution: Only pass slot IDs of frames that have the startup or
//! sync property set in the database.
#define nxErrInvalidKeyslot                             (nxStatus_t)(0xBFF630A8) // -1074384728

//! You tried to set a queue size that is bigger than the maximum allowed.
//! Solution: Specify an in-range queue size.
#define nxErrMaxQueueSizeExceeded                       (nxStatus_t)(0xBFF630A9) // -1074384727

//! You wrote a frame whose payload length is different than the payload length
//! configured by the database. Solution: Never write a different payload length
//! for a frame that is different than the configured payload length.
#define nxErrFrameSizeMismatch                          (nxStatus_t)(0xBFF630AA) // -1074384726

//! The index to indicate an session list element is too large. Solution:
//! Specify an index in the range 0 ... NumInList-1.
#define nxErrIndexTooBig                                (nxStatus_t)(0xBFF630AB) // -1074384725

//! You have tried to create a session that is invalid for the mode of the
//! driver/firmware. For example, you are using the Replay Exclusive mode for
//! Stream Output and you have an output session open.
#define nxErrSessionModeIncompatibility                 (nxStatus_t)(0xBFF630AC) // -1074384724

//! The trigger signal for a frame is allowed only in Single Point Signal
//! sessions (Input or Output). For Output Single Point Signal sessions, only
//! one trigger signal is allowed per frame. Solution: Do not use the trigger
//! signal, or change to a single point I/O session.
#define nxErrTriggerSignalNotAllowed                    (nxStatus_t)(0xBFF630AD) // -1074384723

//! To execute this function properly, the session's list must contain only one
//! cluster. Solution: Use only one cluster in the session.
#define nxErrOnlyOneCluster                             (nxStatus_t)(0xBFF630AE) // -1074384722

//! You attempted to convert a CAN or LIN frame with a payload length greater
//! than 8. For example, you may be converting a frame that uses a higher layer
//! transport protocol, such as SAE-J1939. NI-XNET currently supports conversion
//! of CAN/LIN frames only (layer 2). Solutions: 1) Implement higher layer
//! protocols (including signal conversion) within your code. 2) Contact
//! National Instruments to request this feature in a future version.
#define nxErrConvertInvalidPayload                      (nxStatus_t)(0xBFF630AF) // -1074384721

//! Allocation of memory failed for the data returned from LabVIEW XNET Read.
//! Solutions: 1) Wire a smaller "number to read" to XNET Read (default -1 uses
//! queue size).  2) For Signal Input Waveform, use a smaller resample rate. 3)
//! Set smaller value for session's queue size property (default is large to
//! avoid loss of data).
#define nxErrMemoryFullReadData                         (nxStatus_t)(0xBFF630B0) // -1074384720

//! Allocation of memory failed in the firmware. Solutions: 1) Create less
//! firmware objects 2) Set smaller value for output session's queue size
//! property (default is large to avoid loss of data).
#define nxErrMemoryFullFirmware                         (nxStatus_t)(0xBFF630B1) // -1074384719

//! The NI-XNET driver no longer can communicate with the device. Solution: Make
//! sure the device has not been removed from the computer.
#define nxErrCommunicationLost                          (nxStatus_t)(0xBFF630B2) // -1074384718

//! A LIN schedule has an invalid priority. Solution: Use a valid priority (0 =
//! NULL schedule, 1..254 = Run once schedule, 255 = Continuous schedule).
#define nxErrInvalidPriority                            (nxStatus_t)(0xBFF630B3) // -1074384717

//! (Dis)ConnectTerminals is not allowed for XNET C Series modules. Solution: To
//! connect the module start trigger, use the Session property Interface Source
//! Terminal Start Trigger.
#define nxErrSynchronizationNotAllowed                  (nxStatus_t)(0xBFF630B4) // -1074384716

//! You requested a time (like Start or Communication Time) before the event has
//! happened. Solution: Request the time only after it occurred.
#define nxErrTimeNotReached                             (nxStatus_t)(0xBFF630B5) // -1074384715

//! An internal input queue overflowed. Solution: Attempt to pull data from the
//! hardware faster. If you are connected by an external bus (for example, USB
//! or Ethernet), you can try to use a faster connection.
#define nxErrInternalInputQueueOverflow                 (nxStatus_t)(0xBFF630B6) // -1074384714

//! A bad firmware image file can not be loaded to the hardware. Solution:
//! Uninstall and reinstall the NI-XNET software as the default firmware file
//! may be corrupt. If you are using a custom firmware file, try rebuilding it.
#define nxErrBadImageFile                               (nxStatus_t)(0xBFF630B7) // -1074384713

//! The encoding of embedded network data (CAN, FlexRay, LIN, etc.) within the
//! TDMS file is invalid. Solutions: 1) In the application that wrote (created)
//! the logfile, and the application in which you are reading it, confirm that
//! both use the same major version for frame data encoding
//! (NI_network_frame_version property of the TDMS channel). 2) Ensure that your
//! file was not corrupted.
#define nxErrInvalidLogfile                             (nxStatus_t)(0xBFF630B8) // -1074384712

//! The NI-XNET hardware no longer can communicate with the transceiver cable.
//! This may be due to the cable being removed, a power loss event, an over
//! voltage condition on the power input, or a general communication error.
//! Solution: Make sure the dongle is properly latched and, for some hardware,
//! external power is properly applied. To detect other errors, stop your
//! application and execute a self test.
#define nxErrDongleCommunicationLost                    (nxStatus_t)(0xBFF630B9) // -1074384711

//! The NI-XNET driver timed out when performing low-level communication with
//! the device. This could occur if the device was removed, communication with
//! its parent chassis failed, or a general hardware failure occurred.
#define nxErrLowLevelCommunicationTimeout               (nxStatus_t)(0xBFF630BA) // -1074384710

//! A transfer to the C Series module was aborted. This could occur if the cDAQ
//! chassis was disconnected, reset, power cycled, or another issue occurred
//! that interfered with communication. Solution: Verify that the cDAQ chassis
//! and NI-XNET module are both present, powered, and operational in Measurement
//! and Automation Explorer (MAX). A reset of the cDAQ chassis may be necessary
//! to recover from the error.
#define nxErrCdaqTransferAborted                        (nxStatus_t)(0xBFF630BB) // -1074384709

//! An invalid value has been specified for the CAN FD ISO Mode. Solution:
//! Specify a valid value.
#define nxErrInvalidCanFdIsoMode                        (nxStatus_t)(0xBFF630BC) // -1074384708

//! A property value was out of range or incorrect. Solution: Specify a correct
//! value.
#define nxErrInvalidPropertyValue                       (nxStatus_t)(0xBFF630C0) // -1074384704

//! Integration of the interface into the FlexRay cluster failed, so
//! communication did not start for the interface. Solution: Check the cluster
//! and/or interface parameters and verify that there are startup frames
//! defined.
#define nxErrFlexRayIntegrationFailed                   (nxStatus_t)(0xBFF630C1) // -1074384703

//! The data passed to XNET Write is not formatted correctly for this session
//! type. For example, frame data cannot be passed to a PDU session. Solution:
//! Use the data type that matches the session mode to which you are writing.
#define nxErrInvalidBuffer                              (nxStatus_t)(0xBFF630C2) // -1074384702

//! The PDU was not found in the database. Solution: Make sure you initialize
//! only PDUs in a session that are defined in the database.
#define nxErrPduNotFound                                (nxStatus_t)(0xBFF630D0) // -1074384688

//! A necessary property for a PDU was not found in the database. Solution: Make
//! sure you initialize only PDUs in a session that are completely defined in
//! the database.
#define nxErrUnconfiguredPdu                            (nxStatus_t)(0xBFF630D1) // -1074384687

//! You tried to open the same PDU twice. This is not permitted. Solution: Open
//! each PDU only once.
#define nxErrDuplicatePduObject                         (nxStatus_t)(0xBFF630D2) // -1074384686

//! You can access this database object only by PDU, not by frame. Solution: For
//! CAN and LIN, this is not supported by the current version of NI-XNET; for
//! FlexRay, make sure the database is set to use PDUs.
#define nxErrNeedPdu                                    (nxStatus_t)(0xBFF630D3) // -1074384685

//! The requested PDU could not be mapped to a frame. The current version of
//! NI-XNET might not support this PDU type.
#define nxErrUnmappedPdu                                (nxStatus_t)(0xBFF630D4) // -1074384684

//! The requested PDU is mapped to multiple locations. With the selected
//! hardware, the current version of NI-XNET only supports PDUs mapped to a
//! single location.
#define nxErrMultiplePduMappings                        (nxStatus_t)(0xBFF630D5) // -1074384683

//! Remote communication with the LabVIEW RT target failed. Solution: Check if
//! NI-XNET has been installed on the RT target and check if the NI-XNET RPC
//! server has been started.
#define nxErrRPCCommunication                           (nxStatus_t)(0xBFF63100) // -1074384640

//! File transfer communication with the LabVIEW Real-Time (RT) target failed.
//! Solution: Check if the RT target has been powered on, the RT target has been
//! connected to the network, and if the IP address settings are correct. If the
//! RT target is password protected, make sure you provided the correct user
//! credentials.
#define nxErrFileTransferCommunication                  (nxStatus_t)(0xBFF63101) // -1074384639

//! File transfer to the LabVIEW Real-Time (RT) target failed, because the
//! required files could not be accessed. Solution: You may have executed a VI
//! that opened the database, but did not close. If that is the case, you should
//! change the VI to call Database Close, then reboot the RT controller to
//! continue.
#define nxErrFileTransferAccess                         (nxStatus_t)(0xBFF63102) // -1074384638
#define nxErrFTPFileAccess                              (nxErrFileTransferAccess)

//! The database file you want to use is already assigned to another alias.
//! Solution: Each database file can only be assigned to a single alias. Use the
//! alias that is already assigned to the database instead.
#define nxErrDatabaseAlreadyInUse                       (nxStatus_t)(0xBFF63103) // -1074384637

//! An internal file used by NI-XNET could not be accessed. Solution: Make sure
//! that the internal NI-XNET files are not write protected and that the
//! directories for these files exist.
#define nxErrInternalFileAccess                         (nxStatus_t)(0xBFF63104) // -1074384636

//! The file cannot be deployed because another file deployment is already
//! active. Solution: Wait until the other file deployment has finished, and try
//! again.
#define nxErrFileTransferActive                         (nxStatus_t)(0xBFF63105) // -1074384635

//! The nixnet.dll or one of its components could not be loaded. Solution: Try
//! reinstalling NI-XNET. If the error persists, contact National Instruments.
#define nxErrDllLoad                                    (nxStatus_t)(0xBFF63117) // -1074384617

//! You attempted to perform an action on a session or interface that is
//! started, and the action that requires the session/interface to be stopped.
//! Solution: Stop the object before performing this action.
#define nxErrObjectStarted                              (nxStatus_t)(0xBFF6311E) // -1074384610

//! The length of the default payload does not match the payload length
//! configured in the database. Solution: Write a default payload with a length
//! that matches the Payload Length property configured in the database.
#define nxErrDefaultPayloadNumBytes                     (nxStatus_t)(0xBFF6311F) // -1074384609

//! You attempted to set a CAN arbitration ID with an invalid value. For
//! example, a CAN standard arbitration ID supports only 11 bits. If you attempt
//! to set a standard arbitration ID that uses more than 11 bits, this error is
//! returned. Solution: Use a valid arbitration ID.
#define nxErrInvalidArbitrationId                       (nxStatus_t)(0xBFF63123) // -1074384605

//! You attempted to set a LIN ID with an invalid value. For example, a LIN ID
//! supports only 6 bits. If you attempt to set an ID that uses more than 6
//! bits, this error is returned. Solution: Use a valid LIN ID.
#define nxErrInvalidLinId                               (nxStatus_t)(0xBFF63124) // -1074384604

//! Too many database files are open. NI-XNET allows up to 63 database files to
//! be opened simultaneously. Solution: Open fewer files.
#define nxErrTooManyOpenFiles                           (nxStatus_t)(0xBFF63130) // -1074384592

//! Bad reference has been passed to a database function, e.g., a session
//! reference, or frame reference to retrieve properties from a signal.
#define nxErrDatabaseBadReference                       (nxStatus_t)(0xBFF63131) // -1074384591

//! Creating a database file failed. Solution: Verify access rights to the
//! destination directory or check if overwritten file has read only permission.
#define nxErrCreateDatabaseFile                         (nxStatus_t)(0xBFF63132) // -1074384590

//! A cluster with the same name already exists in the database. Solution: Use
//! another name for this cluster.
#define nxErrDuplicateClusterName                       (nxStatus_t)(0xBFF63133) // -1074384589

//! A frame with the same name already exists in the cluster. Solution: Use
//! another name for this frame.
#define nxErrDuplicateFrameName                         (nxStatus_t)(0xBFF63134) // -1074384588

//! A signal with the same name already exists in the frame. Solution: Use
//! another name for this signal.
#define nxErrDuplicateSignalName                        (nxStatus_t)(0xBFF63135) // -1074384587

//! An ECU with the same name already exists in the cluster. Solution: Use
//! another name for this ECU.
#define nxErrDuplicateECUName                           (nxStatus_t)(0xBFF63136) // -1074384586

//! A subframe with the same name already exists in the frame. Solution: Use
//! another name for this subframe.
#define nxErrDuplicateSubframeName                      (nxStatus_t)(0xBFF63137) // -1074384585

//! The operation is improper for the protocol in use, e.g., you cannot assign
//! FlexRay channels to a CAN frame.
#define nxErrImproperProtocol                           (nxStatus_t)(0xBFF63138) // -1074384584

//! Wrong parent relationship for a child that you are creating with XNET
//! Database Create.
#define nxErrObjectRelation                             (nxStatus_t)(0xBFF63139) // -1074384583

//! The retrieved required property is not defined on the specified object.
//! Solution: Make sure that your database file has this property defined or
//! that you set it in the objects created in memory.
#define nxErrUnconfiguredRequiredProperty               (nxStatus_t)(0xBFF6313B) // -1074384581

//! The feature is not supported under LabVIEW RT, e.g.Save Database
#define nxErrNotSupportedOnRT                           (nxStatus_t)(0xBFF6313C) // -1074384580

//! The object name contains unsupported characters. The name must contain just
//! alphanumeric characters and the underscore, but cannot begin with a digit.
//! The maximum size is 128.
#define nxErrNameSyntax                                 (nxStatus_t)(0xBFF6313D) // -1074384579

//! Unsupported database format. For reading a database, the extension must be
//! .xml, .dbc, .ncd, or .ldf. For saving, the extension must be .xml or .ldf
#define nxErrFileExtension                              (nxStatus_t)(0xBFF6313E) // -1074384578

//! Database object not found (e.g., an object with given name does not exist).
#define nxErrDatabaseObjectNotFound                     (nxStatus_t)(0xBFF6313F) // -1074384577

//! Database cache file cannot be removed or replaced on the disc (e.g., file is
//! write-protected).
#define nxErrRemoveDatabaseCacheFile                    (nxStatus_t)(0xBFF63140) // -1074384576

//! You are trying to write a read-only property, e.g., the mux value on a
//! signal is a read only property (can be changed on the subframe).
#define nxErrReadOnlyProperty                           (nxStatus_t)(0xBFF63141) // -1074384575

//! You are trying to change a signal to be a mux signal, but a mux is already
//! defined in this frame
#define nxErrFrameMuxExists                             (nxStatus_t)(0xBFF63142) // -1074384574

//! You are trying to define FlexRay in-cycle-repetition slots before defining
//! the first slot. Define the first slot (frame ID) before defining
//! in-cycle-repetition slots.
#define nxErrUndefinedFirstSlot                         (nxStatus_t)(0xBFF63144) // -1074384572

//! You are trying to define FlexRay in-cycle-repetition channels before
//! defining the first channels. Define the Channel Assignment on a frame before
//! defining in-cycle-repetition channels.
#define nxErrUndefinedFirstChannels                     (nxStatus_t)(0xBFF63145) // -1074384571

//! You must define the protocol before setting this property (e.g., the frame
//! ID has a different meaning in a CAN or FlexRay cluster).
#define nxErrUndefinedProtocol                          (nxStatus_t)(0xBFF63146) // -1074384570

//! The database information on the real-time system has been created with an
//! older NI-XNET version. This version is no longer supported. To correct this
//! error, re-deploy your database to the real-time system.
#define nxErrOldDatabaseCacheFile                       (nxStatus_t)(0xBFF63147) // -1074384569

//! Frame ConfigStatus: A signal within the frame exceeds the frame boundaries
//! (Payload Length).
#define nxErrDbConfigSigOutOfFrame                      (nxStatus_t)(0xBFF63148) // -1074384568

//! Frame ConfigStatus: A signal within the frame overlaps another signal.
#define nxErrDbConfigSigOverlapped                      (nxStatus_t)(0xBFF63149) // -1074384567

//! Frame ConfigStatus: A integer signal within the frame is defined with more
//! than 52 bits. Not supported.
#define nxErrDbConfigSig52BitInteger                    (nxStatus_t)(0xBFF6314A) // -1074384566

//! Frame ConfigStatus: Frame is defined with an invalid payload size. Allowed
//! sizes vary by bus type and application protocol.
#define nxErrDbConfigFrameNumBytes                      (nxStatus_t)(0xBFF6314B) // -1074384565

//! You are trying to add transmitted FlexRay frames to an ECU, with at least
//! two of them having Startup or Sync property on. Only one Sync or Startup
//! frame is allowed to be sent by an ECU.
#define nxErrMultSyncStartup                            (nxStatus_t)(0xBFF6314C) // -1074384564

//! You are trying to add TX/RX frames to an ECU which are defined in a
//! different cluster than the ECU.
#define nxErrInvalidCluster                             (nxStatus_t)(0xBFF6314D) // -1074384563

//! Database name parameter is incorrect. Solution: Use a valid name for the
//! database, e.g., ":memory:" for in-memory database.
#define nxErrDatabaseName                               (nxStatus_t)(0xBFF6314E) // -1074384562

//! Database object is locked because it is used in a session. Solution:
//! Configure the database before using it in a session.
#define nxErrDatabaseObjectLocked                       (nxStatus_t)(0xBFF6314F) // -1074384561

//! Alias name passed to a function is not defined. Solution: Define the alias
//! before calling the function.
#define nxErrAliasNotFound                              (nxStatus_t)(0xBFF63150) // -1074384560

//! Database file cannot be saved because frames are assigned to FlexRay
//! channels not defined in the cluster. Solution: Verify that all frames in the
//! FlexRay cluster are assigned to an existing cluster channel.
#define nxErrClusterFrameChannelRelation                (nxStatus_t)(0xBFF63151) // -1074384559

//! Frame ConfigStatus: This FlexRay frame transmitted in a dynamic segment uses
//! both channels A and B. This is not allowed. Solution: Use either channel A
//! or B.
#define nxErrDynFlexRayFrameChanAandB                   (nxStatus_t)(0xBFF63152) // -1074384558

//! Database is locked because it is being modified by an another instance of
//! the same application. Solution: Close the database in the other application
//! instance.
#define nxErrDatabaseLockedInUse                        (nxStatus_t)(0xBFF63153) // -1074384557

//! A frame name is ambiguous (e.g., a frame with the same name exists in
//! another cluster). Solution: Specify the cluster name for the frame using the
//! required syntax.
#define nxErrAmbiguousFrameName                         (nxStatus_t)(0xBFF63154) // -1074384556

//! A signal name is ambiguous (e.g., a signal with the same name exists in
//! another frame). Solution: Use <frame>.<signal> syntax for the signal.
#define nxErrAmbiguousSignalName                        (nxStatus_t)(0xBFF63155) // -1074384555

//! An ECU name is ambiguous (e.g., an ECU with the same name exists in another
//! cluster). Solution: Specify the cluster name for the ECU using the required
//! syntax.
#define nxErrAmbiguousECUName                           (nxStatus_t)(0xBFF63156) // -1074384554

//! A subframe name is ambiguous (e.g., a subframe with the same name exists in
//! another cluster). Solution: Specify the cluster name for the subframe using
//! the required syntax.
#define nxErrAmbiguousSubframeName                      (nxStatus_t)(0xBFF63157) // -1074384553

//! A LIN schedule name is ambiguous (e.g., a schedule with the same name exists
//! in another cluster). Solution: Specify the cluster name for the schedule
//! using the required syntax.
#define nxErrAmbiguousScheduleName                      (nxStatus_t)(0xBFF63158) // -1074384552

//! A LIN schedule with the same name already exists in the database. Solution:
//! Use another name for this schedule.
#define nxErrDuplicateScheduleName                      (nxStatus_t)(0xBFF63159) // -1074384551

//! Multiplexers (mode-dependent signals) are not supported when the given
//! protocol is used. Solution: Contact National Instruments to see whether
//! there is a newer NI-XNET version that supports multiplexers for the given
//! protocol.
#define nxErrProtocolMuxNotSupported                    (nxStatus_t)(0xBFF6315A) // -1074384550

//! Saving a FIBEX file containing a LIN cluster is not supported in this
//! NI-XNET version. Solution: Contact National Instruments to see whether there
//! is a newer NI-XNET version that supports saving a FIBEX file that contains a
//! LIN cluster.
#define nxErrSaveLINnotSupported                        (nxStatus_t)(0xBFF6315B) // -1074384549

//! This property requires an ECU configured as LIN master to be present in this
//! cluster. Solution: Create a LIN master ECU in this cluster.
#define nxErrLINmasterNotDefined                        (nxStatus_t)(0xBFF6315C) // -1074384548

//! You have tried to create a session using a frame that is incompatible with
//! the selected session type. For example, you are using a LIN diagnostic frame
//! with a single point output session.
#define nxErrSessionTypeFrameIncompatibility            (nxStatus_t)(0xBFF6315D) // -1074384547

//! You cannot mix open of NI-XNET database objects as both manual and
//! automatic. You open manually by calling the Database Open VI. You open
//! automatically when you 1) wire the IO name directly to a property node or
//! VI, 2) branch a wire to multiple data flows on the diagram, 3) use the IO
//! name with a VI or property node after closing it with the Database Close VI.
//! Solution: Change your diagram to use the manual technique in all locations
//! (always call Open and Close VIs), or to use the automatic technique in all
//! locations (never call Open or Close VIs).
#define nxErrMixAutoManualOpen                          (nxStatus_t)(0xBFF6315E) // -1074384546

//! Due to problems in LabVIEW versions 8.5 through 8.6.1, automatic open of
//! NI-XNET database objects is not supported. You open automatically when you
//! 1) wire the IO name directly to a property node or VI, 2) branch a wire to
//! multiple data flows on the diagram, 3) use the IO name with a VI or property
//! node after closing it with the Database Close VI. Solution: Change your
//! diagram to call the Database Open VI prior to any use (VI or property node)
//! in a data flow (including a new wire branch). Change your diagram to call
//! the Database Close VI when you are finished using the database in your
//! application.
#define nxErrAutoOpenNotSupported                       (nxStatus_t)(0xBFF6315F) // -1074384545

//! A write function was called with a number of array elements (frames, PDUs,
//! or signals) different from the number of elements configured in the session
//! (such as the "list" parameter of the Create Session function). Solution:
//! Ensure the write function calls the same number of elements as configured in
//! the session.
#define nxErrWrongNumElementsWritten                    (nxStatus_t)(0xBFF63160) // -1074384544
#define nxErrWrongNumSignalsWritten                     (nxErrWrongNumElementsWritten)

//! You used XNET session from multiple LabVIEW projects (or multiple
//! executables), which NI-XNET does not support. Solution: Run XNET sessions in
//! only one LabVIEW project at a time.
#define nxErrMultipleLvProject                          (nxStatus_t)(0xBFF63161) // -1074384543

//! When an XNET session is used at runtime, all sessions in the same scope are
//! created on the interface. The same scope is defined as all sessions within
//! the same LabVIEW project which use the same cluster and interface (same
//! physical cable configuration). If you attempt to use a session in the same
//! scope after running the VI, this error occurs. The most likely cause is that
//! you added a new session, and tried to use that new session in a running VI.
//! Solution: Configure all session in LabVIEW project, then run the VI(s) that
//! use those sessions.
#define nxErrSessionConflictLvProject                   (nxStatus_t)(0xBFF63162) // -1074384542

//! You used an empty name for an XNET database object (database, cluster, ECU,
//! frame, or signal). Empty name is not supported. Solution: Refer to NI-XNET
//! help for IO names to review the required syntax for the name, and change
//! your code to use that syntax.
#define nxErrDbObjectNameEmpty                          (nxStatus_t)(0xBFF63163) // -1074384541

//! You used a name for an XNET database object (such as frame or signal) that
//! did not include a valid cluster selection. Solution: Refer to the NI-XNET
//! help for the IO name that you are using, and use the syntax specified for
//! that class, which includes the cluster selection.
#define nxErrMissingAliasInDbObjectName                 (nxStatus_t)(0xBFF63164) // -1074384540

//! Unsupported database file version. Solution: Use only database versions that
//! are supported by this version of NI-XNET. Please see the NI-XNET
//! documentation for information on which database versions are currently
//! supported.
#define nxErrDatabaseImportVersion                      (nxStatus_t)(0xBFF63165) // -1074384539
#define nxErrFibexImportVersion                         (nxErrDatabaseImportVersion)

//! You used an empty name for the XNET Session. Empty name is not supported.
//! Solution: Use a valid XNET session name from your LabVIEW project.
#define nxErrEmptySessionName                           (nxStatus_t)(0xBFF63166) // -1074384538

//! There is not enough message RAM on the FlexRay hardware to configure the
//! data partition for the object(s). Solution: Please refer to the manual for
//! limitations on the number of objects that can be created at any given time
//! based on the payload length.
#define nxErrNotEnoughMessageRAMForObject               (nxStatus_t)(0xBFF63167) // -1074384537

//! The FlexRay keyslot ID has been configured and a startup session has been
//! created. Either the keyslot ID needs to be configured OR the startup session
//! needs to be created. Both cannot exist at the same time. Solution: Choose a
//! single method to configure startup sessions in your application.
#define nxErrKeySlotIDConfig                            (nxStatus_t)(0xBFF63168) // -1074384536

//! An unsupported session was created. For example, stream output is not
//! supported on FlexRay hardware. Solution: Only use supported sessions in your
//! application.
#define nxErrUnsupportedSession                         (nxStatus_t)(0xBFF63169) // -1074384535

//! An XNET session was created after starting the Interface. Only the Stream
//! Input session in the subordinate mode can be created after the Interface has
//! started. Solution: Create sessions prior to starting the XNET Interface in
//! your application.
#define nxErrObjectCreatedAfterStart                    (nxStatus_t)(0xBFF63170) // -1074384528

//! The Single Slot property was enabled on the XNET FlexRay Interface after the
//! interface had started. Solution: Enable the Single Slot property prior to
//! starting the XNET FlexRay Interface.
#define nxErrSingleSlotEnabledAfterStart                (nxStatus_t)(0xBFF63171) // -1074384527

//! The FlexRay macrotick offset specified for XNET Create Timing Source is
//! unsupported. Example: Specifying a macrotick offset greater than
//! MacroPerCycle will result in this error. Solution: Specify a macrotick
//! offset within the supported range for the cluster.
#define nxErrUnsupportedNumMacroticks                   (nxStatus_t)(0xBFF63172) // -1074384526

//! You used invalid syntax in the name of a database object (signal, frame, or
//! ECU). For example, you may have specified a frame's name as
//! <cluster>.<frame>, which is allowed in NI-XNET for C/C++, but not NI-XNET
//! for LabVIEW. Solution: Use the string syntax specified in the help topic for
//! the XNET I/O name class you are using.
#define nxErrBadSyntaxInDatabaseObjectName              (nxStatus_t)(0xBFF63173) // -1074384525

//! A LIN schedule entry name is ambiguous, e.g., a schedule entry with the same
//! name exists in another schedule. Solution: Specify the schedule name for the
//! schedule entry using the required syntax.
#define nxErrAmbiguousScheduleEntryName                 (nxStatus_t)(0xBFF63174) // -1074384524

//! A LIN schedule entry with the same name already exists in the schedule.
//! Solution: Use another name for this schedule entry.
#define nxErrDuplicateScheduleEntryName                 (nxStatus_t)(0xBFF63175) // -1074384523

//! At least one of the frames in the session has an undefined identifier.
//! Solution: Set the frame's "Identifier (Slot)" property before creating the
//! session.
#define nxErrUndefinedFrameId                           (nxStatus_t)(0xBFF63176) // -1074384522

//! At least one of the frames in the session has an undefined payload length.
//! Solution: Set the frame's "Payload Length (in bytes)" property before
//! creating the session.
#define nxErrUndefinedFramePayloadLength                (nxStatus_t)(0xBFF63177) // -1074384521

//! At least one of the signals in the session has an undefined start bit.
//! Solution: Set the "Start Bit" property of the signal before creating the
//! session.
#define nxErrUndefinedSignalStartBit                    (nxStatus_t)(0xBFF63178) // -1074384520

//! At least one of the signals in the session has an undefined number of bits.
//! Solution: Set the "Number of Bits" property of the signal before creating
//! the session.
#define nxErrUndefinedSignalNumBits                     (nxStatus_t)(0xBFF63179) // -1074384519

//! At least one of the signals in the session has an undefined byte order.
//! Solution: Set the "Byte Order" property of the signal before creating the
//! session.
#define nxErrUndefinedSignalByteOrder                   (nxStatus_t)(0xBFF6317A) // -1074384518

//! At least one of the signals in the session has an undefined data type.
//! Solution: Set the "Data Type" property of the signal before creating the
//! session.
#define nxErrUndefinedSignalDataType                    (nxStatus_t)(0xBFF6317B) // -1074384517

//! At least one of the subframes in the session has an undefined multiplexer
//! value. Solution: Set the "Multiplexer Value" property of the subframe before
//! creating the session.
#define nxErrUndefinedSubfMuxValue                      (nxStatus_t)(0xBFF6317C) // -1074384516

//! You provided an invalid index to Write (State LIN Schedule Change).
//! Solution: Use a number from 0 to N-1, where N is the number of LIN schedules
//! returned from the cluster property LIN Schedules. If you are using LabVIEW,
//! the string for the number must be decimal (not hexadecimal).
#define nxErrInvalidLinSchedIndex                       (nxStatus_t)(0xBFF6317D) // -1074384515

//! You provided an invalid name to Write (State LIN Schedule Change). Solution:
//! Use a valid LIN schedule name returned from the cluster property LIN
//! Schedules, or the session property Interface LIN Schedules. You can use the
//! short name (schedule only) or long name (schedule plus database and
//! cluster).
#define nxErrInvalidLinSchedName                        (nxStatus_t)(0xBFF6317E) // -1074384514

//! You provided an invalid active index for the session property.
#define nxErrInvalidActiveFrameIndex                    (nxStatus_t)(0xBFF6317F) // -1074384513

//! You provided an invalid name for Frame:Active of the session property node.
//! Solution: Use a valid item name from the session's List property. You can
//! use the short name (frame or signal only) or long name (frame/signal plus
//! database and cluster).
#define nxErrInvalidActiveFrameName                     (nxStatus_t)(0xBFF63180) // -1074384512

//! The database you are using requires using PDUs, and the operation is
//! ambiguous with respect to PDUs. Example: You are trying to get the frame
//! parent of the signal, but the PDU in which the signal is contained is
//! referenced in multiple frames.
#define nxErrAmbiguousPDU                               (nxStatus_t)(0xBFF63181) // -1074384511

//! A PDU with the same name already exists in the cluster. Solution: Use
//! another name for this PDU.
#define nxErrDuplicatePDU                               (nxStatus_t)(0xBFF63182) // -1074384510

//! You are trying to assign start bits or update bits to PDUs referenced in a
//! frame, but the number of elements in this array is different than the number
//! of referenced PDUs. Solution: Use the same number of elements in the array
//! as in the PDU references array.
#define nxErrNumberOfPDUs                               (nxStatus_t)(0xBFF63183) // -1074384509

//! The configuration of this object requires using advanced PDUs, which the
//! given protocol does not support. Solution: You cannot use this object in the
//! given protocol.
#define nxErrPDUsRequired                               (nxStatus_t)(0xBFF63184) // -1074384508

//! The maximum number of PDUs has been exceeded. Solution: Use fewer PDUs in
//! your sessions.
#define nxErrMaxPDUs                                    (nxStatus_t)(0xBFF63185) // -1074384507

//! This mode value is not currently supported. Solution: Use a valid value.
#define nxErrUnsupportedMode                            (nxStatus_t)(0xBFF63186) // -1074384506

//! The firmware image on your XNET hardware is corrupted. Solution: Update the
//! firmware of this XNET hardware in MAX.
#define nxErrBadFpgaSignature                           (nxStatus_t)(0xBFF63187) // -1074384505
#define nxErrBadcSeriesFpgaSignature                    (nxErrBadFpgaSignature)

//! The firmware version of your XNET hardware is not in sync with your host
//! computer. Solution: Update the firmware of this XNET hardware in MAX.
#define nxErrBadFpgaRevision                            (nxStatus_t)(0xBFF63188) // -1074384504
#define nxErrBadcSeriesFpgaRevision                     (nxErrBadFpgaRevision)

//! The firmware version of your XNET C Series module is not in sync with the
//! NI-XNET software on your remote target. Solution: Update the NI-XNET
//! software on the remote target.
#define nxErrBadFpgaRevisionOnTarget                    (nxStatus_t)(0xBFF63189) // -1074384503

//! The terminal you are trying to use is already in use. Only one connection
//! per terminal is allowed.  Solution: Disconnect the terminal that is already
//! in use.
#define nxErrRouteInUse                                 (nxStatus_t)(0xBFF6318A) // -1074384502

//! You need to install a supported version of NI-DAQmx for your XNET C Series
//! module to work correctly with your Compact DAQ system. Solution: Check the
//! NI-XNET readme file for supported versions of the NI-DAQmx driver software.
#define nxErrDAQmxIncorrectVersion                      (nxStatus_t)(0xBFF6318B) // -1074384501

//! Unable to create the requested route. This may be caused by a routing
//! conflict or an invalid terminal name. Solution: Fix invalid terminal names,
//! such as a blank string. Since NI-XNET relies on the NI-DAQmx driver software
//! to create routes on Compact DAQ chassis, use DAQmx to resolve routing
//! conflicts.
#define nxErrAddRoute                                   (nxStatus_t)(0xBFF6318C) // -1074384500

//! You attempted to transmit a go to sleep frame (by setting the LIN Sleep mode
//! to Remote Sleep) on a LIN interface configured as slave.  In conformance
//! with the LIN protocol standard, only an interface configured as master may
//! transmit a go to sleep frame.
#define nxErrRemoteSleepOnLinSlave                      (nxStatus_t)(0xBFF6318D) // -1074384499

//! You attempted to set properties related to Sleep and Wakeup when the FlexRay
//! cluster defined in the Fibex file does not support it. Solution: Edit the
//! Fibex file used in your application to include all relevant cluster wakeup
//! attributes.
#define nxErrSleepWakeupNotSupported                    (nxStatus_t)(0xBFF6318E) // -1074384498

//! A LIN diagnostic schedule change requires the diagnostic schedule to be
//! defined in the database. Solution: Define the diagnostic schedule in the
//! database.
#define nxErrDiagnosticScheduleNotDefined               (nxStatus_t)(0xBFF6318F) // -1074384497

//! The data payload written for a diagnostic frame for transmit does not
//! conform to the LIN transport layer specification.  Solution: Ensure the data
//! payload for a diagnostic frame conforms to the transport layer
//! specification.
#define nxErrLINTransportLayer                          (nxStatus_t)(0xBFF63192) // -1074384494

//! An error occurred within the NI-XNET example code for logfile access (TDMS).
//! Solution: For LabVIEW, the subVI with the error is shown as the source, and
//! you can open that subVI to determine the cause of the problem. For other
//! programming languages, review the source code for the logfile example to
//! determine the cause of the problem.
#define nxErrLogfile                                    (nxStatus_t)(0xBFF63193) // -1074384493

//! You attempted to write a LIN schedule and use a stream output replay timing
//! mode concurrently. You can only use the stream output immediate timing mode
//! cuncurrently with the LIN scheduler.
#define nxErrStrmOutTmgLinSchedulerConflict             (nxStatus_t)(0xBFF63200) // -1074384384

//! You attempted to create a session that is incompatible with the LIN
//! interface personality (master or slave), or set the LIN interface
//! personality to one that is incompatible with a session already created for
//! it. For example, setting the LIN interface to slave after creating a stream
//! output session will report this error, because only LIN interface as master
//! supports stream output.
#define nxErrSessnTypeLinIntfPrsIncompatible            (nxStatus_t)(0xBFF63201) // -1074384383

//! You attempted to save an LDF or DBC database, but the passed reference is
//! not a database cluster. Solution: A cluster reference must be used to
//! specify the cluster you want to export.
#define nxErrSaveClusterOnly                            (nxStatus_t)(0xBFF63202) // -1074384382
//! Need to define for compatibility with older versions
#define nxErrSaveLdfClusterOnly                         (nxErrSaveClusterOnly)

//! You tried to assign the same interface name twice. This is not permitted.
//! Solution: Assign a unique name to an interface.
#define nxErrDuplicateInterfaceName                     (nxStatus_t)(0xBFF63203) // -1074384381

//! Transceiver cable hardware revision is too new. The current driver does not
//! support this transceiver cable. Solution: Upgrade the NI-XNET driver.
#define nxErrIncompatibleTransceiverRevision            (nxStatus_t)(0xBFF63204) // -1074384380
#define nxErrIncompatiableTransceiverRevision           (nxErrIncompatibleTransceiverRevision)

//! Transceiver cable image revision is too new. The current driver does not
//! support this transceiver cable. Solution: Upgrade the NI-XNET driver or
//! downgrade the image on the transceiver cable.
#define nxErrIncompatibleTransceiverImage               (nxStatus_t)(0xBFF63205) // -1074384379
#define nxErrIncompatiableTransceiverImage              (nxErrIncompatibleTransceiverImage)

//! The property does not apply to this type of hardware. For example, a dongle
//! revision property cannot be accessed on an XNET device that does not support
//! Transceiver Cables. Solution: Do not apply the property to this type of
//! hardware.
#define nxErrPropertyNotsupported                       (nxStatus_t)(0xBFF63206) // -1074384378

//! Exporting cluster into the specified database type failed. Solution: Ensure
//! the database configuration is complete. Refer to the standard documentation
//! for the related file format.
#define nxErrExport_Semantic                            (nxStatus_t)(0xBFF63207) // -1074384377

//! A J1939 input queue overflowed. Reading large J1939 frames can make  the
//! queue overflow, and the Read function delivers fewer frames then specified.
//! Solution: Call the Read function again to read the remaining frames.
#define nxErrJ1939QueueOverflow                         (nxStatus_t)(0xBFF63208) // -1074384376

//! You are trying to transmit a non-J1939 frame with more than 8 bytes. Only
//! J1939 frames can use the J1939 transport protocol.  Solution: Verify the
//! transport protocol property on the frame in  the database.
#define nxErrNonJ1939FrameSize                          (nxStatus_t)(0xBFF63209) // -1074384375

//! You are trying to transmit a J1939 frame, but no J1939 address is assigned
//! to the session. Solution: Set the address using the J1939 address property.
#define nxErrJ1939MissingAddress                        (nxStatus_t)(0xBFF6320A) // -1074384374

//! The received J1939 TP.CM_CTS message has the wrong total size.
#define nxErrJ1939AddressLost                           (nxStatus_t)(0xBFF6320B) // -1074384373

//! The next packet value of the received J1939 TP.CM_CTS message is larger than
//! the total number of packets.
#define nxErrJ1939CtsNextPckLargerTotalPckNum           (nxStatus_t)(0xBFF6320C) // -1074384372

//! The received J1939 TP.CM_CTS message has a number of packets of 0, but the
//! next packet number is not 255.
#define nxErrJ1939CtsNextPck                            (nxStatus_t)(0xBFF6320D) // -1074384371

//! The received J1939 TP.CM_CTS message has a next packet value of 0.
#define nxErrJ1939CtsNextPckNull                        (nxStatus_t)(0xBFF6320E) // -1074384370

//! The received J1939 TP.CM_CTS message does not have the same PGN as in the
//! TP.CM_RTS message.
#define nxErrJ1939CtsPgn                                (nxStatus_t)(0xBFF6320F) // -1074384369

//! Received unexpected sequence number in the J1939 TP.DT message.
#define nxErrJ1939UnexpectedSeqNum                      (nxStatus_t)(0xBFF63210) // -1074384368

//! More Packets are requested than allowed in the J1939 TP.CM_CTS message.
#define nxErrJ1939MorePckReqThanAllowed                 (nxStatus_t)(0xBFF63211) // -1074384367

//! J1939 Timeout T1 while waiting for data.
#define nxErrJ1939TimeoutT1                             (nxStatus_t)(0xBFF63212) // -1074384366

//! J1939 Timeout T2 while waiting for data.
#define nxErrJ1939TimeoutT2                             (nxStatus_t)(0xBFF63213) // -1074384365

//! J1939 Timeout T3 while waiting for TP.CM_CTS or TP.CM_EndOfMsgAck.
#define nxErrJ1939TimeoutT3                             (nxStatus_t)(0xBFF63214) // -1074384364

//! J1939 Timeout T4 while waiting for next CTS MSG.
#define nxErrJ1939TimeoutT4                             (nxStatus_t)(0xBFF63215) // -1074384363

//! Received wrong DLC in the J1939 TP.CM_RTS message. DLC must be 8.
#define nxErrJ1939RtsDlc                                (nxStatus_t)(0xBFF63216) // -1074384362

//! Received wrong DLC in the J1939 TP.CM_CTS message. DLC must be 8.
#define nxErrJ1939CtsDlc                                (nxStatus_t)(0xBFF63217) // -1074384361

//! Received wrong DLC in the J1939 TP.CM_BAM message. DLC must be 8.
#define nxErrJ1939BamDlc                                (nxStatus_t)(0xBFF63218) // -1074384360

//! Received wrong DLC in the J1939 TP.DT message. DLC must be 8.
#define nxErrJ1939DtDlc                                 (nxStatus_t)(0xBFF63219) // -1074384359

//! Received wrong DLC in the J1939 TP.CM_Abort message. DLC must be 8.
#define nxErrJ1939AbortDlc                              (nxStatus_t)(0xBFF6321A) // -1074384358

//! Received wrong DLC in the J1939 TP.CM_EndOfMsgAck message. DLC must be 8.
#define nxErrJ1939EomaDlc                               (nxStatus_t)(0xBFF6321B) // -1074384357

//! Received wrong PGN in the J1939 TP.CM_Abort message.
#define nxErrJ1939AbortPgn                              (nxStatus_t)(0xBFF6321C) // -1074384356

//! Internal error occurred for send TP.CM_CTS Hold Message.
#define nxErrJ1939CtsHoldMsg                            (nxStatus_t)(0xBFF6321D) // -1074384355

//! Invalid total message size in J1939 TP.CM_RTS message. Expect 9..1785.
#define nxErrJ1939InvalidTotalSize                      (nxStatus_t)(0xBFF6321E) // -1074384354

//! Total number of packets in received J1939 TP.CM_RTS message must be greater
//! than 1.
#define nxErrJ1939TotalPckNum                           (nxStatus_t)(0xBFF6321F) // -1074384353

//! Reserved data bytes in J1939 received message are not BFF63FF.
#define nxErrJ1939ReservedData                          (nxStatus_t)(0xBFF63220) // -1074384352

//! Not enough system resources for the J1939 Transport Protocol.
#define nxErrJ1939NotEnoughSysRes                       (nxStatus_t)(0xBFF63221) // -1074384351

//! Received J1939 TP.CM_Abort message with reason ActiveConnection: Already in
//! one or more connection managed sessions and cannot support another.
#define nxErrJ1939AbortMsgActiveConnection              (nxStatus_t)(0xBFF63222) // -1074384350

//! Received J1939 TP.CM_Abort message with reason NotEnoughSystemResources:
//! System resources were needed for another task, so this connection managed
//! session was terminated.
#define nxErrJ1939AbortMsgNotEnoughSysRes               (nxStatus_t)(0xBFF63223) // -1074384349

//! Received J1939 TP.CM_Abort message with reason Timeout: A timeout occurred,
//! and this is the connection abort to close the session.
#define nxErrJ1939AbortMsgTimeout                       (nxStatus_t)(0xBFF63224) // -1074384348

//! Received J1939 TP.CM_Abort message with reason CtsReceived: CTS messages
//! received when data transfer is in progress.
#define nxErrJ1939AbortMsgCtsRec                        (nxStatus_t)(0xBFF63225) // -1074384347

//! Received J1939 TP.CM_Abort message with reason MaxRetransmit: Maximum
//! retransmit request limit reached.
#define nxErrJ1939AbortMsgMaxRetransmit                 (nxStatus_t)(0xBFF63226) // -1074384346

//! Remote communication with the LabVIEW RT target failed because the host and
//! target versions of NI-XNET are different. Solution: On the target, install
//! the same NI-XNET version that is installed on the host.
#define nxErrRPCVersion                                 (nxStatus_t)(0xBFF63227) // -1074384345

//! The CAN frame I/O mode is higher than the CAN cluster  I/O mode. This frame
//! cannot be transmitted on the network. Solution: Change the frame or cluster
//! I/O mode.
#define nxErrFrameCanIoMode                             (nxStatus_t)(0xBFF63228) // -1074384344

//! The current driver cannot update the firmware on your hardware. Solution:
//! Ask National Instruments for compatible driver software.
#define nxErrIncompatibleFlash                          (nxStatus_t)(0xBFF63229) // -1074384343

//! You are trying to use the CAN Transmit I/O Mode (TxIoMode) property in an
//! unsupported interface mode. Solution: You can use this property in only
//! non-ISO or ISO Legacy mode.
#define nxErrTxIoMode                                   (nxStatus_t)(0xBFF6322A) // -1074384342

//! You are trying to use the XS Transceiver Cable on unsupported hardware. This
//! currently requires a PXIe-8510 board.
#define nxErrXsDongleUnsupportedBoard                   (nxStatus_t)(0xBFF6322B) // -1074384341

//! You are trying to use a database alias name that contains an invalid
//! character (for example, a comma).
#define nxErrInvalidCharInDatabaseAlias                 (nxStatus_t)(0xBFF6322C) // -1074384340

//! You are trying to use a database filepath that contains an invalid character
//! (for example, a comma).
#define nxErrInvalidCharInDatabaseFilepath              (nxStatus_t)(0xBFF6322D) // -1074384339

//! You are trying to use CAN FD with a non-HS/FD port. CAN FD is supported with
//! High Speed CAN only.
#define nxErrInvalidCanFdPortType                       (nxStatus_t)(0xBFF6322E) // -1074384338

//! An unconditional LIN schedule entry is incorrectly configured. To fix this
//! issue, reference only one frame in this entry.
#define nxErrInvUnconditionalEntry                      (nxStatus_t)(0xBFF6322F) // -1074384337

//! An event LIN schedule entry has no collision resolving schedule assigned. To
//! fix this issue, assign a schedule to the schedule entry.
#define nxErrEventEntryNoSchedule                       (nxStatus_t)(0xBFF63230) // -1074384336

//! You have connected your USB device to a port that supports only Full Speed
//! (USB 1.1). NI-XNET USB devices require at least High Speed (USB 2.0+)
//! support for correct operation.
#define nxErrUnsupportedUsbSpeed                        (nxStatus_t)(0xBFF63231) // -1074384335

//! You added two or more frames with different payload sizes to the same LIN
//! event-triggered schedule entry. Use an equal payload length for all
//! event-triggered frames in an event-triggered schedule entry.
#define nxErrEventUnequalPayloadLength                  (nxStatus_t)(0xBFF63232) // -1074384334

//! You added two or more frames with different checksum types to the same
//! event-triggered schedule entry. The LIN checksum type is determined by the
//! LIN protocol version of the ECU transmitting the frame. Solution: Use the
//! same checksum model for all event-triggered frames in an event-triggered
//! schedule entry.
#define nxErrEventUnequalCheckSumType                   (nxStatus_t)(0xBFF63233) // -1074384333

//! The versions of the NI-XNET device driver and Compact RIO driver are
//! incompatible. Solution: Install drivers listed in the Recommended Software
//! Set.
#define nxErrCrioBadDriverVersions                      (nxStatus_t)(0xBFF63234) // -1074384332

//! The module support for this slot is missing features required for the
//! NI-XNET driver to be able to communicate with the module. Solution: Load a
//! bitfile to the chassis that contains support for NI-XNET modules for the
//! occupied slots.
#define nxErrCrioMissingSlotSupport                     (nxStatus_t)(0xBFF63235) // -1074384331

//! The interface you have attempted to use with NI-XNET Compatibility Library
//! is already in use by NI-XNET.  Solution: Stop all applications running on
//! the interface, or select one not in use by NI-XNET sessions.
#define nxErrIntfAlreadyInUseByNiXnet                   (nxStatus_t)(0xBFF63236) // -1074384330

//! The interface you have attempted to use with NI-XNET is already in use by
//! NI-XNET Compatibility Library.  Solution: Stop all applications running on
//! the interface, or select one not in use by the NI-XNET Compatibility
//! Library.
#define nxErrIntfAlreadyInUseByNiXcl                    (nxStatus_t)(0xBFF63237) // -1074384329

//! Byte array signals are not allowed for this session type or function.
//! Solution: Select only numeric signals for the session.
#define nxErrByteArrayNotAllowed                        (nxStatus_t)(0xBFF63238) // -1074384328

//! Mixing of byte array signals and numeric signals is not allowed for this
//! session type. Solution: Select only numeric signals or byte array signals
//! for the session.
#define nxErrNoByteArrayMix                             (nxStatus_t)(0xBFF63239) // -1074384327

//! Only one byte array signal is allowed for this session type or function.
//! Solution: Select only one byte array signal for the session.
#define nxErrOnlyOneByteArray                           (nxStatus_t)(0xBFF6323A) // -1074384326

//! The feature you have attempted to use is not supported. Solution: Use an
//! alternate feature that is supported.
#define nxErrNotSupported                               (nxStatus_t)(0xBFF6323B) // -1074384325

//! The specified property is write-only and is therefore not readable.
//! Solution: Do not read write-only properties.
#define nxErrWriteOnlyProperty                          (nxStatus_t)(0xBFF6323C) // -1074384324

//! FPGA download is not possible because the board is in use by an application.
//! Solution: Stop all NI-XNET applications before executing FPGA download.
#define nxErrFpgaDownloadNotPossible                    (nxStatus_t)(0xBFF6323D) // -1074384323

//! The trigger timestamp cannot be read, because the trigger source is not
//! connected. Solution: Connect the TimeTrigger to a valid source before
//! reading the timestamp.
#define nxErrTimeTriggerSourceNotConnected              (nxStatus_t)(0xBFF6323E) // -1074384322

//! The trigger timestamp cannot be read, because another operation is reading
//! the timestamp. Solution: Perform only one trigger timestamp read at a time.
#define nxErrTimeTriggerReadInProgress                  (nxStatus_t)(0xBFF6323F) // -1074384321

//! The operation did not complete because it was aborted. This typically occurs
//! when the XNET session is closed while an operation is in progress. Solution:
//! Allow the operation to finish before closing the XNET session.
#define nxErrOperationAborted                           (nxStatus_t)(0xBFF63240) // -1074384320
#define nxErrWaitAborted                                (nxErrOperationAborted)

//! The future time trigger cannot be generated, because the trigger destination
//! is not connected. Solution: Connect the TimeTrigger to a valid destination
//! before generating the future time trigger.
#define nxErrFutureTimeTriggerNotConnected              (nxStatus_t)(0xBFF63241) // -1074384319

//! The log file could not be created because it already exists. Solution:
//! Specify a different file name or choose a mode that allows overwriting the
//! file.
#define nxErrLogFileAlreadyExists                       (nxStatus_t)(0xBFF63242) // -1074384318

//! Could not create or replace the log file. This can happen if there are
//! insufficient file permissions at the specified location or invalid file path
//! syntax.
#define nxErrLogFileCreate                              (nxStatus_t)(0xBFF63243) // -1074384317

//! You cannot read data using XNET Read after a session has been started with
//! logging enabled.
#define nxErrLogModeRead                                (nxStatus_t)(0xBFF63244) // -1074384316

//! A problem has been detected with the firmware on the device. Solution: Stop
//! your application and try disabling/re-enabling the driver in Device Manager.
//! If the problem persists, contact National Instruments.
#define nxErrFirmwareFault                              (nxStatus_t)(0xBFF63245) // -1074384315

//! A write queue overflowed for a session that has not been started. Solution:
//! Write less data before starting the session, or write data after the session
//! has already been started.
#define nxErrOutputQueueOverflowNotStarted              (nxStatus_t)(0xBFF63246) // -1074384314

//! The total size of the data to be transmitted is larger than the internal
//! write queue. Solution: Write less data at a time.
#define nxErrWriteTooLarge                              (nxStatus_t)(0xBFF63247) // -1074384313

//! The requested number of packets do not fit in the current queue. Solution:
//! Increase the queue size or decrease the number of packets to read.
#define nxErrReadExceedsQueue                           (nxStatus_t)(0xBFF63248) // -1074384312

//! The length of the payload written is smaller than the minimum payload size
//! allowed.
#define nxErrPayloadTooSmall                            (nxStatus_t)(0xBFF63249) // -1074384311
#define nxErrFrameWriteTooSmall                         (nxErrPayloadTooSmall)

//! The XNET endpoint on this port cannot start while the Port Mode is set to
//! Tap. The endpoint has no access to data while in this mode. Solution: Set
//! the Port Mode to Direct to have full use of the XNET endpoint.
#define nxErrEndpointCannotStartWhileInTapMode          (nxStatus_t)(0xBFF6324A) // -1074384310

//! The future time trigger cannot be generated because a previously scheduled
//! future time trigger is still pending. Solution: Wait until the previously
//! scheduled future time trigger occurs, or cancel the pre-existing trigger by
//! disconnecting the time trigger resource.
#define nxErrFutureTimeTriggerPending                   (nxStatus_t)(0xBFF6324B) // -1074384309

//! The desired time to generate the future time trigger has already elapsed.
//! Solution: Schedule the future time trigger for a point in time further into
//! the future.
#define nxErrFutureTimeTriggerAlreadyElapsed            (nxStatus_t)(0xBFF6324C) // -1074384308

//! The network time cannot be adjusted while this clock is a slave (i.e., not
//! grandmaster). Solution: Wait until the port state is no longer set to slave
//! or configure this clock as a grandmaster.
#define nxErrNetworkTimeNotAdjustableWhileSlave         (nxStatus_t)(0xBFF6324D) // -1074384307

//! Output sessions must be created using an interface's endpoint path.
//! Solution: Change the interface to use the endpoint path (e.g., use the
//! interface name that does not contain "/monitor").
#define nxErrOutputStreamMustUseEndpointPath            (nxStatus_t)(0xBFF6324E) // -1074384306

//! The time protocol cannot be used while the Port Mode is set to Tap.
//! Solution: If Tap mode is desired, disable the time protocol on both ports of
//! the Tap pair before switching to Tap mode. If usage of the time protocol is
//! desired, set the Port Mode to Direct before enabling the time protocol.
#define nxErrCannotUseTimeProtocolWhileInTapMode        (nxStatus_t)(0xBFF6324F) // -1074384305

//! You cannot write data while the XNET session is started and the link is
//! down. Solution: Ensure the link is up prior to writing data. You can use the
//! Operational Status property to query the current link state.
#define nxErrCannotWriteWhileStartedAndLinkDown         (nxStatus_t)(0xBFF63250) // -1074384304

//! Device reset is not possible since the board is in use by an application.
//! Solution: Stop all NI-XNET applications before executing a device reset.
#define nxErrDeviceResetNotPossible                     (nxStatus_t)(0xBFF63251) // -1074384303

//! You cannot start an NI-XNET application while a device reset is in progress.
//! Solution: Complete the device reset before starting any NI-XNET
//! applications.
#define nxErrDeviceResetInProgress                      (nxStatus_t)(0xBFF63252) // -1074384302

//! You wrote a frame whose frame type value is not valid. Solution: Encode the
//! frame with frame type value that is supported by NI-XNET.
#define nxErrFrameTypeInvalid                           (nxStatus_t)(0xBFF63253) // -1074384301

//! The data path you have attempted to use is already in use by another
//! session. Solution: Stop the other application using the desired data path,
//! or select a data path not in use by NI-XNET sessions.
#define nxErrDataPathAlreadyInUseBySession              (nxStatus_t)(0xBFF63254) // -1074384300

//! The timescale value is invalid. Solution: Use a valid value.
#define nxErrInvalidTimescale                           (nxStatus_t)(0xBFF63255) // -1074384299

//! A hardware error has occurred while reading the Port MAC address. Solution:
//! Reset this XNET hardware in MAX.
#define nxErrReadMacAddressFailed                       (nxStatus_t)(0xBFF63256) // -1074384298

//! You cannot write to the Time Sync Protocol property while the Port Mode is
//! set to Tap. Solution: Do not write to this property while ports are
//! configured to use Tap mode. To configure the Time Sync Protocol property,
//! set the Port Mode to Direct before writing to this property.
#define nxErrTimeProtocolPropertyReadOnlyWhileInTapMode (nxStatus_t)(0xBFF63257) // -1074384297

//! The buffer is not large enough to contain the requested path.
#define nxErrPathBufferTooSmall                         (nxStatus_t)(0xBFF63258) // -1074384296

//! A NULL pointer or an empty string was passed when requesting a path.
#define nxErrPathBufferNull                             (nxStatus_t)(0xBFF63259) // -1074384295

//! The device hardware revision is too new for the currently installed driver.
//! Solution: Upgrade the NI-XNET driver.
#define nxErrHardwareNeedsNewerDriver                   (nxStatus_t)(0xBFF6325A) // -1074384294

//! An error occurred compiling the Ethernet Frame Filter due to incorrect
//! syntax. Refer to NI-XNET documentation for information about the supported
//! syntax.
#define nxErrBadEnetFrameFilterSyntax                   (nxStatus_t)(0xBFF6325B) // -1074384293

//! This function requires that the session's list contain only one PDU.
//! Solution: Create multiple sessions, each of which contains only one PDU.
#define nxErrSessionContainsMultiplePdus                (nxStatus_t)(0xBFF6325C) // -1074384292

//! A PDU session has been opened, but it does not contain any PDUs. Solution:
//! Specify at least one PDU.
#define nxErrNoPDUs                                     (nxStatus_t)(0xBFF6325D) // -1074384291

//! You are attempting to create a session with a PDU or frame that has an
//! invalid configuration. Review the frame or PDU properties in the NI-XNET
//! Database Editor for a detailed description of the error. Refer to NI-XNET
//! help for details about PDU and frame configurations.
#define nxErrInvalidMapping                             (nxStatus_t)(0xBFF6325E) // -1074384290

//! A file input/output error occurred while writing to the log file.
#define nxErrLogFileIO                                  (nxStatus_t)(0xBFF6325F) // -1074384289

//! Sleep handshake was not successful. Solution: Ensure the connected link
//! partner is configured to respond to sleep requests.
#define nxErrSleepFail                                  (nxStatus_t)(0xBFF63260) // -1074384288

//! Sleep request did not complete within a reasonable amount of time. Solution:
//! Ensure that the link is established before sending a sleep request.
#define nxErrSleepTimeout                               (nxStatus_t)(0xBFF63261) // -1074384287

//! Local port did not wake up within a reasonable amount of time. Solution:
//! Ensure that the link is established before attempting to wake.
#define nxErrWakeTimeout                                (nxStatus_t)(0xBFF63262) // -1074384286

//! Local port configuration does not support sleep. Solution: Configure the
//! port in a way that is sleep-compatible. Refer to NI-XNET help for details.
#define nxErrSleepUnsupportedWithPortConfig             (nxStatus_t)(0xBFF63263) // -1074384285

//! NI-XNET does not support consecutive non-data frame types. Solution: Write
//! only one non-data frame type between data frames. Refer to NI-XNET help for
//! details.
#define nxErrContiguousNonDataFrames                    (nxStatus_t)(0xBFF63264) // -1074384284

//! The transmitted raw frames are not formatted correctly. For more
//! information, refer to "Raw Frame Format" in the NI-XNET help.
#define nxErrInvalidRawFrame                            (nxStatus_t)(0xBFF63265) // -1074384283

//! The environment variable `NIXNET_USE_SYSTEM_LOCALE` must be set to 0 or 1.
//! Refer to NI-XNET help for details.
#define nxErrInvalidLocaleEnvironmentVariableValue      (nxStatus_t)(0xBFF63266) // -1074384282

   // Warning Section

//! The specified CAN FD baud rate exceeds the CiA-certified baud rate for the
//! transceiver. Higher speeds are possible experimentally, but bus errors may
//! be detected or generated during communication. For more information, refer
//! to NI-XNET CAN hardware details in the NI-XNET help.
#define nxWarnFdBaudExceedsCapability                   (nxStatus_t)(0x3FF63040) // 1073098816

//! A warning occurred when importing this database. The NI-XNET Database Editor
//! may show additional information.
#define nxWarnDatabaseImport                            (nxStatus_t)(0x3FF63085) // 1073098885

//! The database file has been imported, but it was not created by the XNET
//! Editor or using the XNET API. Saving the database file with the XNET API or
//! XNET Editor may lose information from the original file.
#define nxWarnDatabaseImportFIBEXNoXNETFile             (nxStatus_t)(0x3FF63086) // 1073098886

//! A warning occurred when importing this database. This file was not created
//! by NI-XNET, so some features may not be supported. The NI-XNET Database
//! Editor may show additional information.
#define nxWarnDatabaseImportFIBEXNoXNETFilePlusWarning  (nxStatus_t)(0x3FF63087) // 1073098887

//! Close Database returns a warning instead of an error when an invalid
//! reference is passed to the function.
#define nxWarnDatabaseBadReference                      (nxStatus_t)(0x3FF63131) // 1073099057

//! You are retrieving signals from a frame that uses advanced PDU
//! configuration. The signal start bit is given relative to the PDU, and it may
//! be different than the start bit relative to the frame.
#define nxWarnAdvancedPDU                               (nxStatus_t)(0x3FF63132) // 1073099058

//! The multiplexer size exceeds 16 bits. This is not supported for Single Point
//! sessions.
#define nxWarnMuxExceeds16Bit                           (nxStatus_t)(0x3FF63133) // 1073099059

/***********************************************************************
                        P R O P E R T Y   I D S
***********************************************************************/

// Class IDs used for encoding of property IDs (nxProp*)
// Also class parameter of function nxdbCreateObject, nxdbDeleteObject, and
// nxdbFindObject
#define nxClass_Database                  (u32)0x00000000   // Database
#define nxClass_Cluster                   (u32)0x00010000   // Cluster
#define nxClass_Frame                     (u32)0x00020000   // Frame
#define nxClass_Signal                    (u32)0x00030000   // Signal
#define nxClass_Subframe                  (u32)0x00040000   // Subframe
#define nxClass_ECU                       (u32)0x00050000   // ECU
#define nxClass_LINSched                  (u32)0x00060000   // LIN Schedule
#define nxClass_LINSchedEntry             (u32)0x00070000   // LIN Schedule Entry
#define nxClass_PDU                       (u32)0x00080000   // PDU
#define nxClass_Session                   (u32)0x00100000   // Session
#define nxClass_System                    (u32)0x00110000   // System
#define nxClass_Device                    (u32)0x00120000   // Device
#define nxClass_Interface                 (u32)0x00130000   // Interface
#define nxClass_Alias                     (u32)0x00140000   // Alias
#define nxClass_IPStack                   (u32)0x00AB0000   // IP Stack
#define nxClass_TcpSocket                 (u32)0x00AC0000   // TCP Socket
#define nxClass_UdpSocket                 (u32)0x00AD0000   // UDP Socket

#define nxClass_Mask                      (u32)0x00FF0000   // mask for object class

//! Datatype IDs used in encoding of property IDs (nxProp*)
#define nxPrptype_u32                     (u32)0x00000000
#define nxPrptype_f64                     (u32)0x01000000
#define nxPrptype_bool                    (u32)0x02000000   // use u8 as datatype (semantic only)
#define nxPrptype_string                  (u32)0x03000000
#define nxPrptype_1Dstring                (u32)0x04000000   // comma-separated list
#define nxPrptype_ref                     (u32)0x05000000   // u32 reference (handle)
#define nxPrptype_1Dref                   (u32)0x06000000   // array of u32 reference
#define nxPrptype_time                    (u32)0x07000000   // nxTimestamp_t
#define nxPrptype_time100ns               (u32)0x07000000   // nxTimestamp100ns_t
#define nxPrptype_1Du32                   (u32)0x08000000   // array of u32 values
#define nxPrptype_u64                     (u32)0x09000000
#define nxPrptype_1Du8                    (u32)0x0A000000   // array of u8 values
#define nxPrptype_1Du16                   (u32)0x0B000000   // array of u16 values
#define nxPrptype_struct                  (u32)0x0C000000   // struct or array-of-struct
#define nxPrptype_time1ns                 (u32)0x0D000000   // nxTimestamp1ns_t
#define nxPrptype_i32                     (u32)0x0E000000

#define nxPrptype_Mask                    (u32)0xFF000000   // mask for nxPrptype

/* PropertyId parameter of nxGetProperty, nxGetPropertySize, nxSetProperty functions. */

// Session:Application Protocol
#define nxPropSession_ApplicationProtocol        ((u32)0x00100091) // u32 --r
// Session:Auto Start?
#define nxPropSession_AutoStart                  ((u32)0x02100001) // bool --rw
// Session:Cluster Name
#define nxPropSession_ClusterName                ((u32)0x0310000A) // string --r
// Session:Database
#define nxPropSession_DatabaseName               ((u32)0x03100002) // string --r
// Session:Ethernet:Filtering:Frame Filter
#define nxPropSession_EnetFrameFilter            ((u32)0x031000F4) // string --rw
// Session:Ethernet:Logging:Error?
#define nxPropSession_EnetLogError               ((u32)0x021000BD) // bool --r
// Session:Ethernet:Logging:Filepath
#define nxPropSession_EnetLogFile                ((u32)0x031000BA) // string --rw
// Session:Ethernet:Logging:Mode
#define nxPropSession_EnetLogMode                ((u32)0x001000B9) // u32 --rw
// Session:Ethernet:Logging:MultipleFiles:EnableMultipleFiles
#define nxPropSession_EnetLogEnableMultipleFiles ((u32)0x021000F9) // bool --rw
// Session:Ethernet:Logging:MultipleFiles:FileSizeThreshold
#define nxPropSession_EnetLogFileSizeThreshold   ((u32)0x091000FA) // u64 --rw
// Session:Ethernet:Logging:Operation
#define nxPropSession_EnetLogOperation           ((u32)0x001000BB) // u32 --rw
// Session:Ethernet:Number of Frames Received
#define nxPropSession_EnetNumFramesReceived      ((u32)0x091000EF) // u64 --r
// Session:Ethernet:Source MAC Address Auto?
#define nxPropSession_EnetSourceMacAddressAuto   ((u32)0x021000A9) // bool --rw
// Session:Interface:64bit Baud Rate
#define nxPropSession_IntfBaudRate64             ((u32)0x09100016) // u64 --rw
// Session:Interface:Adjust Local Time
#define nxPropSession_IntfAdjustLocalTime        ((u32)0x091000AB) // u64 --w
#define nxPropSession_IntfEnetAdjustLocalTime    (nxPropSession_IntfAdjustLocalTime)
// Session:Interface:Baud Rate (32-bit) Superseded by nxPropSession_IntfBaudRate64
#define nxPropSession_IntfBaudRate               ((u32)0x00100016) // u32 --rw
// Session:Interface:Bus Error Frames to Input Stream?
#define nxPropSession_IntfBusErrToInStrm         ((u32)0x02100015) // bool --rw
// Session:Interface:CAN:64bit FD Baud Rate
#define nxPropSession_IntfCanFdBaudRate64        ((u32)0x09100027) // u64 --rw
// Session:Interface:CAN:Disable Protocol Exception Handling
#define nxPropSession_IntfCanDisableProtExceptionHandling ((u32)0x021000A4) // bool --rw
// Session:Interface:CAN:Enable Edge Filter
#define nxPropSession_IntfCanEdgeFilter          ((u32)0x021000A2) // bool --rw
// Session:Interface:CAN:External Transceiver Config
#define nxPropSession_IntfCANExtTcvrConfig       ((u32)0x00100023) // u32 --w
// Session:Interface:CAN:CAN FD Baudrate (32-bit) Superseded by nxPropSession_IntfCanFdBaudRate64
#define nxPropSession_IntfCanFdBaudRate          ((u32)0x00100027) // u32 --rw
// Session:Interface:CAN:FD ISO Mode
#define nxPropSession_IntfCanFdIsoMode           ((u32)0x0010003E) // u32 --rw
// Session:Interface:CAN:I/O Mode
#define nxPropSession_IntfCanIoMode              ((u32)0x00100026) // u32 --r
// Session:Interface:CAN:Listen Only?
#define nxPropSession_IntfCANLstnOnly            ((u32)0x02100022) // bool --rw
// Session:Interface:CAN:Pending Transmit Order
#define nxPropSession_IntfCANPendTxOrder         ((u32)0x00100020) // u32 --w
// Session:Interface:CAN:Single Shot Transmit?
#define nxPropSession_IntfCANSingShot            ((u32)0x02100024) // bool --rw
// Session:Interface:CAN:Termination
#define nxPropSession_IntfCANTerm                ((u32)0x00100025) // u32 --rw
// Session:Interface:CAN:Transceiver State
#define nxPropSession_IntfCANTcvrState           ((u32)0x00100028) // u32 --rw
// Session:Interface:CAN:Transceiver Type
#define nxPropSession_IntfCANTcvrType            ((u32)0x00100029) // u32 --rw
// Session:Interface:CAN:Transmit I/O Mode
#define nxPropSession_IntfCanTxIoMode            ((u32)0x00100039) // u32 --rw
// Session:Interface:CAN:Transmit Pause
#define nxPropSession_IntfCanTransmitPause       ((u32)0x021000A3) // bool --rw
// Session:Interface:Echo Transmit?
#define nxPropSession_IntfEchoTx                 ((u32)0x02100010) // bool --rw
// Session:Interface:Ethernet:Endpoint:Receive Filter
#define nxPropSession_IntfEnetEptReceiveFilter   ((u32)0x0C1000BC) // struct --rw
// Session:Interface:Ethernet:Endpoint:Transmit Bandwidth
#define nxPropSession_IntfEnetEptTransmitBandwidth ((u32)0x091000BF) // u64 --rw
// Session:Interface:Ethernet:IPv4 Address
#define nxPropSession_IntfEnetIpV4Address        ((u32)0x031000EB) // string --r
// Session:Interface:Ethernet:Jumbo Frames
#define nxPropSession_IntfEnetJumboFrames        ((u32)0x001000F3) // u32 --r
// Session:Interface:Ethernet:Link Speed
#define nxPropSession_IntfEnetLinkSpeed          ((u32)0x001000F2) // u32 --r
// Session:Interface:Ethernet:Link Speed Configured
#define nxPropSession_IntfEnetLinkSpeedConfigured ((u32)0x001000F1) // u32 --r
// Session:Interface:Ethernet:MAC Address
#define nxPropSession_IntfEnetMacAddress         ((u32)0x031000A8) // string --r
// Session:Interface:Ethernet:OS Network Adapter Description
#define nxPropSession_IntfEnetOsNetworkAdapterDescription ((u32)0x031000ED) // string --r
// Session:Interface:Ethernet:OS Network Adapter Name
#define nxPropSession_IntfEnetOsNetworkAdapterName ((u32)0x031000EC) // string --r
// Session:Interface:Ethernet:Operational Status
#define nxPropSession_IntfEnetOperationalStatus  ((u32)0x001000AA) // u32 --r
// Session:Interface:Ethernet:Output Stream Timescale
#define nxPropSession_IntfEnetOutStrmTimescale   ((u32)0x001000F7) // u32 --rw
// Session:Interface:Ethernet:PHY Power Mode
#define nxPropSession_IntfEnetPhyPowerMode       ((u32)0x001000F9) // u32 --r
// Session:Interface:Ethernet:PHY State
#define nxPropSession_IntfEnetPhyState           ((u32)0x001000A7) // u32 --r
// Session:Interface:Ethernet:Port Mode
#define nxPropSession_IntfEnetPortMode           ((u32)0x001000A6) // u32 --r
// Session:Interface:Ethernet:Signal Quality
#define nxPropSession_IntfEnetSignalQuality      ((u32)0x0E1000F6) // i32 --r
// Session:Interface:Ethernet:Sleep Capability
#define nxPropSession_IntfEnetSleepCapability    ((u32)0x001000F8) // u32 --r
// Session:Interface:Ethernet:Statistics:MAC:Counter Names
#define nxPropSession_IntfEnetStatsCounterNames  ((u32)0x041000AC) // 1Dstring --r
// Session:Interface:Ethernet:Statistics:MAC:Counter Values
#define nxPropSession_IntfEnetStatsCounterValues ((u32)0x041000AD) // 1Dstring --r
// Session:Interface:Ethernet:Statistics:MAC:Rx Bad Frames Count
#define nxPropSession_IntfEnetStatsRxBadFrames   ((u32)0x091000B6) // u64 --r
// Session:Interface:Ethernet:Statistics:MAC:Rx Bytes Count
#define nxPropSession_IntfEnetStatsRxBytes       ((u32)0x091000AE) // u64 --r
// Session:Interface:Ethernet:Statistics:MAC:Rx Good Frames Count
#define nxPropSession_IntfEnetStatsRxGoodFrames  ((u32)0x091000AF) // u64 --r
// Session:Interface:Ethernet:Statistics:MAC:Tx Bytes Count
#define nxPropSession_IntfEnetStatsTxBytes       ((u32)0x091000B7) // u64 --r
// Session:Interface:Ethernet:Statistics:MAC:Tx Good Frames Count
#define nxPropSession_IntfEnetStatsTxGoodFrames  ((u32)0x091000B8) // u64 --r
// Session:Interface:Ethernet:Statistics:PHY:Counter Names
#define nxPropSession_IntfEnetStatsPhyCounterNames ((u32)0x041000FD) // 1Dstring --r
// Session:Interface:Ethernet:Statistics:PHY:Counter Values
#define nxPropSession_IntfEnetStatsPhyCounterValues ((u32)0x041000FE) // 1Dstring --r
// Session:Interface:Ethernet:Statistics:PHY:Low Power Sleep Count
#define nxPropSession_IntfEnetStatsPhyLowPowerSleep ((u32)0x09100101) // u64 --r
// Session:Interface:Ethernet:Statistics:PHY:Sleep Failure Count
#define nxPropSession_IntfEnetStatsPhySleepFailure ((u32)0x09100103) // u64 --r
// Session:Interface:Ethernet:Statistics:PHY:Wake Up Failure Count
#define nxPropSession_IntfEnetStatsPhyWakeupFailure ((u32)0x09100102) // u64 --r
// Session:Interface:Ethernet:Statistics:PHY:Wake Up Pulse Count
#define nxPropSession_IntfEnetStatsPhyWakeupPulse ((u32)0x091000FF) // u64 --r
// Session:Interface:Ethernet:Statistics:PHY:Wake Up Request Count
#define nxPropSession_IntfEnetStatsPhyWakeupRequest ((u32)0x09100100) // u64 --r
// Session:Interface:Ethernet:Time Sync:Adjust Network Time
#define nxPropSession_IntfEnetTimeAdjustNetworkTime ((u32)0x091000D1) // u64 --w
// Session:Interface:Ethernet:Time Sync:BMCA Enabled?
#define nxPropSession_IntfEnetTimeBMCAEnabled    ((u32)0x021000C2) // bool --rw
// Session:Interface:Ethernet:Time Sync:Clock Accuracy
#define nxPropSession_IntfEnetTimeClkAccuracy    ((u32)0x001000C6) // u32 --r
// Session:Interface:Ethernet:Time Sync:Clock Class
#define nxPropSession_IntfEnetTimeClkClass       ((u32)0x001000C5) // u32 --r
// Session:Interface:Ethernet:Time Sync:Clock ID
#define nxPropSession_IntfEnetTimeClkID          ((u32)0x031000C4) // string --r
// Session:Interface:Ethernet:Time Sync:Clock Offset Scaled Log Variance
#define nxPropSession_IntfEnetTimeClkOffsetVar   ((u32)0x001000C7) // u32 --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Clock Accuracy
#define nxPropSession_IntfEnetTimeGMClkAccuracy  ((u32)0x001000CD) // u32 --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Clock Class
#define nxPropSession_IntfEnetTimeGMClkClass     ((u32)0x001000CC) // u32 --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Clock ID
#define nxPropSession_IntfEnetTimeGMClkID        ((u32)0x031000CB) // string --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Clock Offset Scaled Log Variance
#define nxPropSession_IntfEnetTimeGMClkOffsetVar ((u32)0x001000CE) // u32 --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Priority1
#define nxPropSession_IntfEnetTimeGMPriority1    ((u32)0x001000CF) // u32 --r
// Session:Interface:Ethernet:Time Sync:Grandmaster Priority2
#define nxPropSession_IntfEnetTimeGMPriority2    ((u32)0x001000D0) // u32 --r
// Session:Interface:Ethernet:Time Sync:Offset From Master
#define nxPropSession_IntfEnetTimeOffsetFromMaster ((u32)0x091000C3) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:AS Capable?
#define nxPropSession_IntfEnetTimePortASCapable  ((u32)0x021000E1) // bool --r
// Session:Interface:Ethernet:Time Sync:Port:Announce Receipt Timeout
#define nxPropSession_IntfEnetTimePortAnnounceReceiptTimeout ((u32)0x001000E0) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Announce Transmit Enabled?
#define nxPropSession_IntfEnetTimePortAnnounceTransmitEnabled ((u32)0x021000DF) // bool --rw
// Session:Interface:Ethernet:Time Sync:Port:Log Announce Interval
#define nxPropSession_IntfEnetTimePortLogAnnounceInterval ((u32)0x001000DE) // u32 --r
// Session:Interface:Ethernet:Time Sync:Port:Log Announce Interval Configured
#define nxPropSession_IntfEnetTimePortLogAnnounceIntervalConfigured ((u32)0x001000DD) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Log Pdelay_Req Interval
#define nxPropSession_IntfEnetTimePortLogPdelayInterval ((u32)0x001000D9) // u32 --r
// Session:Interface:Ethernet:Time Sync:Port:Log Pdelay_Req Interval Configured
#define nxPropSession_IntfEnetTimePortLogPdelayIntervalConfigured ((u32)0x001000D8) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Log Sync Interval
#define nxPropSession_IntfEnetTimePortLogSyncInterval ((u32)0x001000DB) // u32 --r
// Session:Interface:Ethernet:Time Sync:Port:Log Sync Interval Configured
#define nxPropSession_IntfEnetTimePortLogSyncIntervalConfigured ((u32)0x001000DA) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Pdelay Enabled?
#define nxPropSession_IntfEnetTimePortPdelayEnabled ((u32)0x021000D7) // bool --rw
// Session:Interface:Ethernet:Time Sync:Port:Port State
#define nxPropSession_IntfEnetTimePortState      ((u32)0x001000D3) // u32 --r
// Session:Interface:Ethernet:Time Sync:Port:Port State Configured
#define nxPropSession_IntfEnetTimePortStateConfigured ((u32)0x001000D2) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Propagation Delay
#define nxPropSession_IntfEnetTimePortPropDelay  ((u32)0x011000D4) // f64 --r
// Session:Interface:Ethernet:Time Sync:Port:Propagation Delay Configured
#define nxPropSession_IntfEnetTimePortPropDelayConfigured ((u32)0x011000D5) // f64 --rw
// Session:Interface:Ethernet:Time Sync:Port:Propagation Delay Threshold
#define nxPropSession_IntfEnetTimePortPropDelayThreshold ((u32)0x011000D6) // f64 --rw
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Counter Names
#define nxPropSession_IntfEnetTimePortStatsCounterNames ((u32)0x041000E3) // 1Dstring --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Counter Values
#define nxPropSession_IntfEnetTimePortStatsCounterValues ((u32)0x041000E4) // 1Dstring --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Rx Announce Count
#define nxPropSession_IntfEnetTimePortStatsRxAnnounce ((u32)0x091000E6) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Rx Pdelay Request Count
#define nxPropSession_IntfEnetTimePortStatsRxPdelayRequest ((u32)0x091000E7) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Rx Sync Count
#define nxPropSession_IntfEnetTimePortStatsRxSync ((u32)0x091000E5) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Tx Announce Count
#define nxPropSession_IntfEnetTimePortStatsTxAnnounce ((u32)0x091000E9) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Tx Pdelay Request Count
#define nxPropSession_IntfEnetTimePortStatsTxPdelayRequest ((u32)0x091000EA) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Statistics:Tx Sync Count
#define nxPropSession_IntfEnetTimePortStatsTxSync ((u32)0x091000E8) // u64 --r
// Session:Interface:Ethernet:Time Sync:Port:Sync Receipt Timeout
#define nxPropSession_IntfEnetTimePortSyncReceiptTimeout ((u32)0x001000DC) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Port:Sync Status
#define nxPropSession_IntfEnetTimePortSyncStatus ((u32)0x001000F0) // u32 --r
// Session:Interface:Ethernet:Time Sync:Port:Synced?
#define nxPropSession_IntfEnetTimePortSynced     ((u32)0x021000E2) // bool --r
// Session:Interface:Ethernet:Time Sync:Priority1
#define nxPropSession_IntfEnetTimePriority1      ((u32)0x001000C8) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Priority2
#define nxPropSession_IntfEnetTimePriority2      ((u32)0x001000C9) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Protocol
#define nxPropSession_IntfEnetTimeProtocol       ((u32)0x001000C0) // u32 --rw
// Session:Interface:Ethernet:Time Sync:Protocol Enabled?
#define nxPropSession_IntfEnetTimeProtocolEnabled ((u32)0x021000C1) // bool --rw
// Session:Interface:Ethernet:Time Sync:Steps to Grandmaster
#define nxPropSession_IntfEnetTimeStepsToGM      ((u32)0x001000CA) // u32 --r
// Session:Interface:Ethernet:Trigger PPS Synced?
#define nxPropSession_IntfEnetTriggerPpsSynced   ((u32)0x02100104) // bool --r
// Session:Interface:FlexRay:Accepted Startup Range
#define nxPropSession_IntfFlexRayAccStartRng     ((u32)0x00100030) // u32 --rw
// Session:Interface:FlexRay:Allow Halt Due To Clock?
#define nxPropSession_IntfFlexRayAlwHltClk       ((u32)0x02100031) // bool --rw
// Session:Interface:FlexRay:Allow Passive to Active
#define nxPropSession_IntfFlexRayAlwPassAct      ((u32)0x00100032) // u32 --rw
// Session:Interface:FlexRay:Auto Asleep When Stopped?
#define nxPropSession_IntfFlexRayAutoAslpWhnStp  ((u32)0x0210003A) // bool --rw
// Session:Interface:FlexRay:Cluster Drift Damping
#define nxPropSession_IntfFlexRayClstDriftDmp    ((u32)0x00100033) // u32 --rw
// Session:Interface:FlexRay:Coldstart?
#define nxPropSession_IntfFlexRayColdstart       ((u32)0x02100034) // bool --r
// Session:Interface:FlexRay:Connected Channels
#define nxPropSession_IntfFlexRayConnectedChs    ((u32)0x0010003C) // u32 --rw
// Session:Interface:FlexRay:Decoding Correction
#define nxPropSession_IntfFlexRayDecCorr         ((u32)0x00100035) // u32 --rw
// Session:Interface:FlexRay:Delay Compensation Ch A
#define nxPropSession_IntfFlexRayDelayCompA      ((u32)0x00100036) // u32 --rw
// Session:Interface:FlexRay:Delay Compensation Ch B
#define nxPropSession_IntfFlexRayDelayCompB      ((u32)0x00100037) // u32 --rw
// Session:Interface:FlexRay:Key Slot Identifier
#define nxPropSession_IntfFlexRayKeySlotID       ((u32)0x00100038) // u32 --rw
// Session:Interface:FlexRay:Latest Tx
#define nxPropSession_IntfFlexRayLatestTx        ((u32)0x00100041) // u32 --r
// Session:Interface:FlexRay:Listen Timeout
#define nxPropSession_IntfFlexRayListTimo        ((u32)0x00100042) // u32 --rw
// Session:Interface:FlexRay:Macro Initial Offset Ch A
#define nxPropSession_IntfFlexRayMacInitOffA     ((u32)0x00100043) // u32 --rw
// Session:Interface:FlexRay:Macro Initial Offset Ch B
#define nxPropSession_IntfFlexRayMacInitOffB     ((u32)0x00100044) // u32 --rw
// Session:Interface:FlexRay:Max Drift
#define nxPropSession_IntfFlexRayMaxDrift        ((u32)0x00100047) // u32 --rw
// Session:Interface:FlexRay:Micro Initial Offset Ch A
#define nxPropSession_IntfFlexRayMicInitOffA     ((u32)0x00100045) // u32 --rw
// Session:Interface:FlexRay:Micro Initial Offset Ch B
#define nxPropSession_IntfFlexRayMicInitOffB     ((u32)0x00100046) // u32 --rw
// Session:Interface:FlexRay:Microtick
#define nxPropSession_IntfFlexRayMicrotick       ((u32)0x00100048) // u32 --r
// Session:Interface:FlexRay:Null Frames To Input Stream?
#define nxPropSession_IntfFlexRayNullToInStrm    ((u32)0x02100049) // bool --rw
// Session:Interface:FlexRay:Offset Correction
#define nxPropSession_IntfFlexRayOffCorr         ((u32)0x00100058) // u32 --r
// Session:Interface:FlexRay:Offset Correction Out
#define nxPropSession_IntfFlexRayOffCorrOut      ((u32)0x00100050) // u32 --rw
// Session:Interface:FlexRay:Rate Correction
#define nxPropSession_IntfFlexRayRateCorr        ((u32)0x00100059) // u32 --r
// Session:Interface:FlexRay:Rate Correction Out
#define nxPropSession_IntfFlexRayRateCorrOut     ((u32)0x00100052) // u32 --rw
// Session:Interface:FlexRay:Samples Per Microtick
#define nxPropSession_IntfFlexRaySampPerMicro    ((u32)0x00100053) // u32 --rw
// Session:Interface:FlexRay:Single Slot Enabled?
#define nxPropSession_IntfFlexRaySingSlotEn      ((u32)0x02100054) // bool --rw
// Session:Interface:FlexRay:Sleep
#define nxPropSession_IntfFlexRaySleep           ((u32)0x0010003B) // u32 --w
// Session:Interface:FlexRay:Statistics Enabled?
#define nxPropSession_IntfFlexRayStatisticsEn    ((u32)0x0210005A) // bool --rw
// Session:Interface:FlexRay:Symbol Frames To Input Stream?
#define nxPropSession_IntfFlexRaySymToInStrm     ((u32)0x0210003D) // bool --rw
// Session:Interface:FlexRay:Sync Frame Status
#define nxPropSession_IntfFlexRaySyncStatus      ((u32)0x0010005F) // u32 --r
// Session:Interface:FlexRay:Sync Frames Channel A Even
#define nxPropSession_IntfFlexRaySyncChAEven     ((u32)0x0810005B) // 1Du32 --r
// Session:Interface:FlexRay:Sync Frames Channel A Odd
#define nxPropSession_IntfFlexRaySyncChAOdd      ((u32)0x0810005C) // 1Du32 --r
// Session:Interface:FlexRay:Sync Frames Channel B Even
#define nxPropSession_IntfFlexRaySyncChBEven     ((u32)0x0810005D) // 1Du32 --r
// Session:Interface:FlexRay:Sync Frames Channel B Odd
#define nxPropSession_IntfFlexRaySyncChBOdd      ((u32)0x0810005E) // 1Du32 --r
// Session:Interface:FlexRay:Termination
#define nxPropSession_IntfFlexRayTerm            ((u32)0x00100057) // u32 --rw
// Session:Interface:FlexRay:Wakeup Channel
#define nxPropSession_IntfFlexRayWakeupCh        ((u32)0x00100055) // u32 --rw
// Session:Interface:FlexRay:Wakeup Pattern
#define nxPropSession_IntfFlexRayWakeupPtrn      ((u32)0x00100056) // u32 --rw
// Session:Interface:I/O Name
#define nxPropSession_IntfName                   ((u32)0x03100013) // string --r
// Session:Interface:LIN:Break Delimiter Length
#define nxPropSession_IntfLINBreakDelimiterLength ((u32)0x001000F5) // u32 --rw
// Session:Interface:LIN:Break Length
#define nxPropSession_IntfLINBreakLength         ((u32)0x00100070) // u32 --rw
// Session:Interface:LIN:Checksum to Input Stream?
#define nxPropSession_IntfLINChecksumToInStrm    ((u32)0x02100081) // bool --rw
// Session:Interface:LIN:Diagnostics P2min
#define nxPropSession_IntfLINDiagP2min           ((u32)0x01100077) // f64 --rw
// Session:Interface:LIN:Diagnostics STmin
#define nxPropSession_IntfLINDiagSTmin           ((u32)0x01100076) // f64 --rw
// Session:Interface:LIN:Master?
#define nxPropSession_IntfLINMaster              ((u32)0x02100072) // bool --rw
// Session:Interface:LIN:No Response Frames to Input Stream?
#define nxPropSession_IntfLINNoResponseToInStrm  ((u32)0x02100080) // bool --rw
// Session:Interface:LIN:Output Stream Slave Response List By NAD
#define nxPropSession_IntfLINOStrSlvRspLstByNAD  ((u32)0x08100079) // 1Du32 --rw
// Session:Interface:LIN:Schedule Names
#define nxPropSession_IntfLINSchedNames          ((u32)0x04100075) // 1Dstring --r
// Session:Interface:LIN:Sleep
#define nxPropSession_IntfLINSleep               ((u32)0x00100073) // u32 --w
// Session:Interface:LIN:Start Allowed without Bus Power?
#define nxPropSession_IntfLINAlwStartWoBusPwr    ((u32)0x02100078) // bool --rw
// Session:Interface:LIN:Termination
#define nxPropSession_IntfLINTerm                ((u32)0x00100074) // u32 --rw
// Session:Interface:Output Stream List
#define nxPropSession_IntfOutStrmList            ((u32)0x06100011) // 1Dref --rw
// Session:Interface:Output Stream List By ID
#define nxPropSession_IntfOutStrmListById        ((u32)0x08100021) // 1Du32 --rw
// Session:Interface:Output Stream Timing
#define nxPropSession_IntfOutStrmTimng           ((u32)0x00100012) // u32 --rw
// Session:Interface:Source Terminal:Start Trigger
#define nxPropSession_IntfSrcTermStartTrigger    ((u32)0x03100090) // string --rw
// Session:Interface:Start Trigger Frames to Input Stream?
#define nxPropSession_IntfStartTrigToInStrm      ((u32)0x02100014) // bool --rw
// Session:List
#define nxPropSession_List                       ((u32)0x04100003) // 1Dstring --r
// Session:Mode
#define nxPropSession_Mode                       ((u32)0x00100004) // u32 --r
// Session:Number in List
#define nxPropSession_NumInList                  ((u32)0x00100005) // u32 --r
// Session:Number of Frames
#define nxPropSession_NumFrames                  ((u32)0x0010000D) // u32 --r
// Session:Number of Values Pending
#define nxPropSession_NumPend                    ((u32)0x00100006) // u32 --r
// Session:Number of Values Unused
#define nxPropSession_NumUnused                  ((u32)0x0010000B) // u32 --r
// Session:Payload Length Maximum
#define nxPropSession_PayldLenMax                ((u32)0x00100009) // u32 --r
// Session:Protocol
#define nxPropSession_Protocol                   ((u32)0x00100008) // u32 --r
// Session:Queue Size
#define nxPropSession_QueueSize                  ((u32)0x0010000C) // u32 --rw
// Session:Resample Rate
#define nxPropSession_ResampRate                 ((u32)0x01100007) // f64 --rw
// Session:SAE J1939:ECU
#define nxPropSession_J1939ECU                   ((u32)0x05100093) // ref --w
// Session:SAE J1939:ECU Busy
#define nxPropSession_J1939ECUBusy               ((u32)0x021000A1) // bool --rw
// Session:SAE J1939:Fill Byte
#define nxPropSession_J1939FillByte              ((u32)0x0010009F) // u32 --rw
// Session:SAE J1939:Include Destination Address in PGN
#define nxPropSession_J1939IncludeDestAddrInPGN  ((u32)0x021000A5) // bool --rw
// Session:SAE J1939:Maximum Repeat CTS
#define nxPropSession_J1939MaxRepeatCTS          ((u32)0x0010009E) // u32 --rw
// Session:SAE J1939:Node Address
#define nxPropSession_J1939Address               ((u32)0x00100092) // u32 --rw
// Session:SAE J1939:Node Name
#define nxPropSession_J1939Name                  ((u32)0x09100094) // u64 --rw
// Session:SAE J1939:Number of Packets Received
#define nxPropSession_J1939NumPacketsRecv        ((u32)0x0010009C) // u32 --rw
// Session:SAE J1939:Number of Packets Response
#define nxPropSession_J1939NumPacketsResp        ((u32)0x0010009D) // u32 --rw
// Session:SAE J1939:Timing:Hold Time Th
#define nxPropSession_J1939HoldTimeTh            ((u32)0x0110009B) // f64 --rw
// Session:SAE J1939:Timing:Response Time Tr_GD
#define nxPropSession_J1939ResponseTimeTrGD      ((u32)0x0110009A) // f64 --rw
// Session:SAE J1939:Timing:Response Time Tr_SD
#define nxPropSession_J1939ResponseTimeTrSD      ((u32)0x01100099) // f64 --rw
// Session:SAE J1939:Timing:Timeout T1
#define nxPropSession_J1939TimeoutT1             ((u32)0x01100095) // f64 --rw
// Session:SAE J1939:Timing:Timeout T2
#define nxPropSession_J1939TimeoutT2             ((u32)0x01100096) // f64 --rw
// Session:SAE J1939:Timing:Timeout T3
#define nxPropSession_J1939TimeoutT3             ((u32)0x01100097) // f64 --rw
// Session:SAE J1939:Timing:Timeout T4
#define nxPropSession_J1939TimeoutT4             ((u32)0x01100098) // f64 --rw
// Session:SAE J1939:Write Queue Size
#define nxPropSession_J1939WriteQueueSize        ((u32)0x001000A0) // u32 --rw
// System:CompactDAQ Packet Time
#define nxPropSys_CDAQPktTime                    ((u32)0x0111000C) // f64 --rw
// System:Devices
#define nxPropSys_DevRefs                        ((u32)0x06110002) // 1Dref --r
// System:Interfaces
#define nxPropSys_IntfRefs                       ((u32)0x06110003) // 1Dref --r
// System:Interfaces (All)
#define nxPropSys_IntfRefsAll                    ((u32)0x0611000D) // 1Dref --r
// System:Interfaces (CAN)
#define nxPropSys_IntfRefsCAN                    ((u32)0x06110004) // 1Dref --r
// System:Interfaces (Ethernet)
#define nxPropSys_IntfRefsEthernet               ((u32)0x06110001) // 1Dref --r
// System:Interfaces (FlexRay)
#define nxPropSys_IntfRefsFlexRay                ((u32)0x06110005) // 1Dref --r
// System:Interfaces (LIN)
#define nxPropSys_IntfRefsLIN                    ((u32)0x06110007) // 1Dref --r
// System:Version:Build
#define nxPropSys_VerBuild                       ((u32)0x00110006) // u32 --r
// System:Version:Major
#define nxPropSys_VerMajor                       ((u32)0x00110008) // u32 --r
// System:Version:Minor
#define nxPropSys_VerMinor                       ((u32)0x00110009) // u32 --r
// System:Version:Phase
#define nxPropSys_VerPhase                       ((u32)0x0011000A) // u32 --r
// System:Version:Update
#define nxPropSys_VerUpdate                      ((u32)0x0011000B) // u32 --r
// Device:Form Factor
#define nxPropDev_FormFac                        ((u32)0x00120001) // u32 --r
// Device:Interfaces
#define nxPropDev_IntfRefs                       ((u32)0x06120002) // 1Dref --r
// Device:Interfaces (All)
#define nxPropDev_IntfRefsAll                    ((u32)0x06120008) // 1Dref --r
// Device:Number of Ports
#define nxPropDev_NumPorts                       ((u32)0x00120004) // u32 --r
// Device:Number of Ports (All)
#define nxPropDev_NumPortsAll                    ((u32)0x00120007) // u32 --r
// Device:Product Name
#define nxPropDev_Name                           ((u32)0x03120003) // string --r
// Device:Product Number
#define nxPropDev_ProductNum                     ((u32)0x00120008) // u32 --r
// Device:Serial Number
#define nxPropDev_SerNum                         ((u32)0x00120005) // u32 --r
// Device:Slot Number
#define nxPropDev_SlotNum                        ((u32)0x00120006) // u32 --r
// Interface:CAN:Termination Capability
#define nxPropIntf_CANTermCap                    ((u32)0x00130008) // u32 --r
// Interface:CAN:Transceiver Capability
#define nxPropIntf_CANTcvrCap                    ((u32)0x00130007) // u32 --r
// Interface:Device
#define nxPropIntf_DevRef                        ((u32)0x05130001) // ref --r
// Interface:Dongle Compatible Firmware Version
#define nxPropIntf_DongleCompatibleFirmwareVersion ((u32)0x0013000F) // u32 --r
// Interface:Dongle Compatible Revision
#define nxPropIntf_DongleCompatibleRevision      ((u32)0x0013000E) // u32 --r
// Interface:Dongle Firmware Version
#define nxPropIntf_DongleFirmwareVersion         ((u32)0x0013000D) // u32 --r
// Interface:Dongle ID
#define nxPropIntf_DongleID                      ((u32)0x0013000A) // u32 --r
// Interface:Dongle Revision
#define nxPropIntf_DongleRevision                ((u32)0x0013000C) // u32 --r
// Interface:Dongle State
#define nxPropIntf_DongleState                   ((u32)0x00130009) // u32 --r
// Interface:Name
#define nxPropIntf_Name                          ((u32)0x03130002) // string --r
// Interface:Number
#define nxPropIntf_Num                           ((u32)0x00130003) // u32 --r
// Interface:Port Number
#define nxPropIntf_PortNum                       ((u32)0x00130004) // u32 --r
// Interface:Protocol
#define nxPropIntf_Protocol                      ((u32)0x00130005) // u32 --r

/* PropertyId parameter of nxGetSubProperty, nxGetSubPropertySize, nxSetSubProperty functions. */

// Session:Frame:CAN:Start Time Offset
#define nxPropSessionSub_CANStartTimeOff         ((u32)0x01100081) // f64 --w
// Session:Frame:CAN:Transmit Time
#define nxPropSessionSub_CANTxTime               ((u32)0x01100082) // f64 --w
// Session:Frame:LIN:Transmit N Corrupted Checksums
#define nxPropSessionSub_LINTxNCorruptedChksums  ((u32)0x00100085) // u32 --w
// Session:Frame:Output Queue Update Frequency
#define nxPropSessionSub_OutputQueueUpdateFreq   ((u32)0x00100084) // u32 --w
// Session:Frame:SAE J1939:Address Filter
#define nxPropSessionSub_J1939_AddrFilter        ((u32)0x03100086) // string --w
// Session:Frame:Skip N Cyclic Frames
#define nxPropSessionSub_SkipNCyclicFrames       ((u32)0x00100083) // u32 --w

/* PropertyId parameter of nxdbGetProperty, nxdbGetPropertySize, nxdbSetProperty functions. */

// Database:Clusters
#define nxPropDatabase_ClstRefs                  ((u32)0x06000002) // 1Dref --r
// Database:Name
#define nxPropDatabase_Name                      ((u32)0x03000001) // string --r
// Database:Show Invalid From Open?
#define nxPropDatabase_ShowInvalidFromOpen       ((u32)0x02000003) // bool --rw
// Cluster:64bit Baud Rate
#define nxPropClst_BaudRate64                    ((u32)0x09010001) // u64 --rw
// Cluster:Application Protocol
#define nxPropClst_ApplicationProtocol           ((u32)0x00010073) // u32 --rw
// Cluster:Baud Rate (32-bit) Superseded by nxPropClst_BaudRate64
#define nxPropClst_BaudRate                      ((u32)0x00010001) // u32 --rw
// Cluster:CAN:64bit FD Baud Rate
#define nxPropClst_CanFdBaudRate64               ((u32)0x09010011) // u64 --rw
// Cluster:CAN:FD Baudrate (32-bit) Superseded by nxPropClst_CanFdBaudRate64
#define nxPropClst_CanFdBaudRate                 ((u32)0x00010011) // u32 --rw
// Cluster:CAN:FD ISO Mode
#define nxPropClst_CanFdIsoMode                  ((u32)0x00010074) // u32 --r
// Cluster:CAN:I/O Mode
#define nxPropClst_CanIoMode                     ((u32)0x00010010) // u32 --rw
// Cluster:Comment
#define nxPropClst_Comment                       ((u32)0x03010008) // string --rw
// Cluster:Configuration Status
#define nxPropClst_ConfigStatus                  ((u32)0x00010009) // u32 --r
// Cluster:Database
#define nxPropClst_DatabaseRef                   ((u32)0x05010002) // ref --r
// Cluster:ECUs
#define nxPropClst_ECURefs                       ((u32)0x06010003) // 1Dref --r
// Cluster:FlexRay:Action Point Offset
#define nxPropClst_FlexRayActPtOff               ((u32)0x00010020) // u32 --rw
// Cluster:FlexRay:Allow Passive to Active
#define nxPropClst_FlexRayAlwPassAct             ((u32)0x00010072) // u32 --rw
// Cluster:FlexRay:CAS Rx Low Max
#define nxPropClst_FlexRayCASRxLMax              ((u32)0x00010021) // u32 --rw
// Cluster:FlexRay:Channels
#define nxPropClst_FlexRayChannels               ((u32)0x00010022) // u32 --rw
// Cluster:FlexRay:Cluster Drift Damping
#define nxPropClst_FlexRayClstDriftDmp           ((u32)0x00010023) // u32 --rw
// Cluster:FlexRay:Cold Start Attempts
#define nxPropClst_FlexRayColdStAts              ((u32)0x00010024) // u32 --rw
// Cluster:FlexRay:Cycle
#define nxPropClst_FlexRayCycle                  ((u32)0x00010025) // u32 --rw
// Cluster:FlexRay:Dynamic Segment Start
#define nxPropClst_FlexRayDynSegStart            ((u32)0x00010026) // u32 --r
// Cluster:FlexRay:Dynamic Slot Idle Phase
#define nxPropClst_FlexRayDynSlotIdlPh           ((u32)0x00010027) // u32 --rw
// Cluster:FlexRay:Latest Guaranteed Dynamic Slot
#define nxPropClst_FlexRayLatestGuarDyn          ((u32)0x0001002B) // u32 --r
// Cluster:FlexRay:Latest Usable Dynamic Slot
#define nxPropClst_FlexRayLatestUsableDyn        ((u32)0x0001002A) // u32 --r
// Cluster:FlexRay:Listen Noise
#define nxPropClst_FlexRayLisNoise               ((u32)0x00010028) // u32 --rw
// Cluster:FlexRay:Macro Per Cycle
#define nxPropClst_FlexRayMacroPerCycle          ((u32)0x00010029) // u32 --rw
// Cluster:FlexRay:Macrotick
#define nxPropClst_FlexRayMacrotick              ((u32)0x01010030) // f64 --r
// Cluster:FlexRay:Max Without Clock Correction Fatal
#define nxPropClst_FlexRayMaxWoClkCorFat         ((u32)0x00010031) // u32 --rw
// Cluster:FlexRay:Max Without Clock Correction Passive
#define nxPropClst_FlexRayMaxWoClkCorPas         ((u32)0x00010032) // u32 --rw
// Cluster:FlexRay:Minislot
#define nxPropClst_FlexRayMinislot               ((u32)0x00010034) // u32 --rw
// Cluster:FlexRay:Minislot Action Point Offset
#define nxPropClst_FlexRayMinislotActPt          ((u32)0x00010033) // u32 --rw
// Cluster:FlexRay:NIT
#define nxPropClst_FlexRayNIT                    ((u32)0x00010036) // u32 --rw
// Cluster:FlexRay:NIT Start
#define nxPropClst_FlexRayNITStart               ((u32)0x00010037) // u32 --r
// Cluster:FlexRay:Network Management Vector Length
#define nxPropClst_FlexRayNMVecLen               ((u32)0x00010035) // u32 --rw
// Cluster:FlexRay:Number Of Minislots
#define nxPropClst_FlexRayNumMinislt             ((u32)0x00010038) // u32 --rw
// Cluster:FlexRay:Number Of Static Slots
#define nxPropClst_FlexRayNumStatSlt             ((u32)0x00010039) // u32 --rw
// Cluster:FlexRay:Offset Correction Start
#define nxPropClst_FlexRayOffCorSt               ((u32)0x00010040) // u32 --rw
// Cluster:FlexRay:Payload Length Dynamic Maximum
#define nxPropClst_FlexRayPayldLenDynMax         ((u32)0x00010041) // u32 --rw
// Cluster:FlexRay:Payload Length Maximum
#define nxPropClst_FlexRayPayldLenMax            ((u32)0x00010042) // u32 --r
// Cluster:FlexRay:Payload Length Static
#define nxPropClst_FlexRayPayldLenSt             ((u32)0x00010043) // u32 --rw
// Cluster:FlexRay:Static Slot
#define nxPropClst_FlexRayStatSlot               ((u32)0x00010045) // u32 --rw
// Cluster:FlexRay:Symbol Window
#define nxPropClst_FlexRaySymWin                 ((u32)0x00010046) // u32 --rw
// Cluster:FlexRay:Symbol Window Start
#define nxPropClst_FlexRaySymWinStart            ((u32)0x00010047) // u32 --r
// Cluster:FlexRay:Sync Node Max
#define nxPropClst_FlexRaySyncNodeMax            ((u32)0x00010048) // u32 --rw
// Cluster:FlexRay:TSS Transmitter
#define nxPropClst_FlexRayTSSTx                  ((u32)0x00010049) // u32 --rw
// Cluster:FlexRay:Use Wakeup?
#define nxPropClst_FlexRayUseWakeup              ((u32)0x02010055) // bool --rw
// Cluster:FlexRay:Wakeup Symbol Rx Idle
#define nxPropClst_FlexRayWakeSymRxIdl           ((u32)0x00010050) // u32 --rw
// Cluster:FlexRay:Wakeup Symbol Rx Low
#define nxPropClst_FlexRayWakeSymRxLow           ((u32)0x00010051) // u32 --rw
// Cluster:FlexRay:Wakeup Symbol Rx Window
#define nxPropClst_FlexRayWakeSymRxWin           ((u32)0x00010052) // u32 --rw
// Cluster:FlexRay:Wakeup Symbol Tx Idle
#define nxPropClst_FlexRayWakeSymTxIdl           ((u32)0x00010053) // u32 --rw
// Cluster:FlexRay:Wakeup Symbol Tx Low
#define nxPropClst_FlexRayWakeSymTxLow           ((u32)0x00010054) // u32 --rw
// Cluster:Frames
#define nxPropClst_FrmRefs                       ((u32)0x06010004) // 1Dref --r
// Cluster:LIN:Schedules
#define nxPropClst_LINSchedules                  ((u32)0x06010070) // 1Dref --r
// Cluster:LIN:Tick
#define nxPropClst_LINTick                       ((u32)0x01010071) // f64 --rw
// Cluster:Name (Short)
#define nxPropClst_Name                          ((u32)0x03010005) // string --rw
// Cluster:PDUs
#define nxPropClst_PDURefs                       ((u32)0x06010008) // 1Dref --r
// Cluster:PDUs Required?
#define nxPropClst_PDUsReqd                      ((u32)0x0201000A) // bool --r
// Cluster:Protocol
#define nxPropClst_Protocol                      ((u32)0x00010006) // u32 --rw
// Cluster:Signals
#define nxPropClst_SigRefs                       ((u32)0x06010007) // 1Dref --r
// Frame:Application Protocol
#define nxPropFrm_ApplicationProtocol            ((u32)0x00020064) // u32 --rw
// Frame:CAN:Extended Identifier?
#define nxPropFrm_CANExtID                       ((u32)0x02020010) // bool --rw
// Frame:CAN:I/O Mode
#define nxPropFrm_CANioMode                      ((u32)0x00020066) // u32 --rw
// Frame:CAN:Timing Type
#define nxPropFrm_CANTimingType                  ((u32)0x00020011) // u32 --rw
// Frame:CAN:Transmit Time
#define nxPropFrm_CANTxTime                      ((u32)0x01020012) // f64 --rw
// Frame:Cluster
#define nxPropFrm_ClusterRef                     ((u32)0x05020001) // ref --r
// Frame:Comment
#define nxPropFrm_Comment                        ((u32)0x03020002) // string --rw
// Frame:Configuration Status
#define nxPropFrm_ConfigStatus                   ((u32)0x00020009) // u32 --r
// Frame:Default Payload
#define nxPropFrm_DefaultPayload                 ((u32)0x0A020005) // 1Du8 --rw
// Frame:FlexRay:Base Cycle
#define nxPropFrm_FlexRayBaseCycle               ((u32)0x00020020) // u32 --rw
// Frame:FlexRay:Channel Assignment
#define nxPropFrm_FlexRayChAssign                ((u32)0x00020021) // u32 --rw
// Frame:FlexRay:Cycle Repetition
#define nxPropFrm_FlexRayCycleRep                ((u32)0x00020022) // u32 --rw
// Frame:FlexRay:In Cycle Repetitions:Channel Assignments
#define nxPropFrm_FlexRayInCycRepChAssigns       ((u32)0x08020032) // 1Du32 --rw
// Frame:FlexRay:In Cycle Repetitions:Enabled?
#define nxPropFrm_FlexRayInCycRepEnabled         ((u32)0x02020030) // bool --r
// Frame:FlexRay:In Cycle Repetitions:Identifiers
#define nxPropFrm_FlexRayInCycRepIDs             ((u32)0x08020031) // 1Du32 --rw
// Frame:FlexRay:Payload Preamble?
#define nxPropFrm_FlexRayPreamble                ((u32)0x02020023) // bool --rw
// Frame:FlexRay:Startup?
#define nxPropFrm_FlexRayStartup                 ((u32)0x02020024) // bool --rw
// Frame:FlexRay:Sync?
#define nxPropFrm_FlexRaySync                    ((u32)0x02020025) // bool --rw
// Frame:FlexRay:Timing Type
#define nxPropFrm_FlexRayTimingType              ((u32)0x00020026) // u32 --rw
// Frame:Identifier
#define nxPropFrm_ID                             ((u32)0x00020003) // u32 --rw
// Frame:LIN:Checksum
#define nxPropFrm_LINChecksum                    ((u32)0x00020050) // u32 --r
// Frame:Mux:Data Multiplexer Signal
#define nxPropFrm_MuxDataMuxSigRef               ((u32)0x05020041) // ref --r
// Frame:Mux:Is Data Multiplexed?
#define nxPropFrm_MuxIsMuxed                     ((u32)0x02020040) // bool --r
// Frame:Mux:Static Signals
#define nxPropFrm_MuxStaticSigRefs               ((u32)0x06020042) // 1Dref --r
// Frame:Mux:Subframes
#define nxPropFrm_MuxSubframeRefs                ((u32)0x06020043) // 1Dref --r
// Frame:Name (Short)
#define nxPropFrm_Name                           ((u32)0x03020004) // string --rw
// Frame:PDU Start Bits
#define nxPropFrm_PDUStartBits                   ((u32)0x08020061) // 1Du32 --rw
// Frame:PDU Update Bits
#define nxPropFrm_PDUUpdateBits                  ((u32)0x08020063) // 1Du32 --rw
// Frame:PDUs
#define nxPropFrm_PDURefs                        ((u32)0x06020060) // 1Dref --rw
// Frame:Payload Length
#define nxPropFrm_PayloadLen                     ((u32)0x00020007) // u32 --rw
// Frame:Signals
#define nxPropFrm_SigRefs                        ((u32)0x06020008) // 1Dref --r
// Frame:Variable Payload
#define nxPropFrm_VariablePayload                ((u32)0x02020065) // bool --rw
// Signal:Byte Order
#define nxPropSig_ByteOrdr                       ((u32)0x00030001) // u32 --rw
// Signal:Comment
#define nxPropSig_Comment                        ((u32)0x03030002) // string --rw
// Signal:Configuration Status
#define nxPropSig_ConfigStatus                   ((u32)0x00030009) // u32 --r
// Signal:Data Type
#define nxPropSig_DataType                       ((u32)0x00030003) // u32 --rw
// Signal:Default Value
#define nxPropSig_Default                        ((u32)0x01030004) // f64 --rw
// Signal:Frame
#define nxPropSig_FrameRef                       ((u32)0x05030005) // ref --r
// Signal:Maximum Value
#define nxPropSig_Max                            ((u32)0x01030006) // f64 --rw
// Signal:Minimum Value
#define nxPropSig_Min                            ((u32)0x01030007) // f64 --rw
// Signal:Mux:Data Multiplexer?
#define nxPropSig_MuxIsDataMux                   ((u32)0x02030030) // bool --rw
// Signal:Mux:Dynamic?
#define nxPropSig_MuxIsDynamic                   ((u32)0x02030031) // bool --r
// Signal:Mux:Multiplexer Value
#define nxPropSig_MuxValue                       ((u32)0x00030032) // u32 --r
// Signal:Mux:Subframe
#define nxPropSig_MuxSubfrmRef                   ((u32)0x05030033) // ref --r
// Signal:Name (Short)
#define nxPropSig_Name                           ((u32)0x03030008) // string --rw
// Signal:Name (Unique to Cluster)
#define nxPropSig_NameUniqueToCluster            ((u32)0x03030010) // string --r
// Signal:Number of Bits
#define nxPropSig_NumBits                        ((u32)0x00030012) // u32 --rw
// Signal:PDU
#define nxPropSig_PDURef                         ((u32)0x05030011) // ref --r
// Signal:Scaling Factor
#define nxPropSig_ScaleFac                       ((u32)0x01030013) // f64 --rw
// Signal:Scaling Offset
#define nxPropSig_ScaleOff                       ((u32)0x01030014) // f64 --rw
// Signal:Start Bit
#define nxPropSig_StartBit                       ((u32)0x00030015) // u32 --rw
// Signal:Unit
#define nxPropSig_Unit                           ((u32)0x03030016) // string --rw
// Subframe:Configuration Status
#define nxPropSubfrm_ConfigStatus                ((u32)0x00040009) // u32 --r
// Subframe:Dynamic Signals
#define nxPropSubfrm_DynSigRefs                  ((u32)0x06040001) // 1Dref --r
// Subframe:Frame
#define nxPropSubfrm_FrmRef                      ((u32)0x05040002) // ref --r
// Subframe:Multiplexer Value
#define nxPropSubfrm_MuxValue                    ((u32)0x00040003) // u32 --rw
// Subframe:Name (Short)
#define nxPropSubfrm_Name                        ((u32)0x03040004) // string --rw
// Subframe:Name (Unique to Cluster)
#define nxPropSubfrm_NameUniqueToCluster         ((u32)0x03040007) // string --r
// Subframe:PDU
#define nxPropSubfrm_PDURef                      ((u32)0x05040005) // ref --r
// ECU:Cluster
#define nxPropECU_ClstRef                        ((u32)0x05050001) // ref --r
// ECU:Comment
#define nxPropECU_Comment                        ((u32)0x03050005) // string --rw
// ECU:Configuration Status
#define nxPropECU_ConfigStatus                   ((u32)0x00050009) // u32 --r
// ECU:FlexRay:Coldstart?
#define nxPropECU_FlexRayIsColdstart             ((u32)0x02050010) // bool --r
// ECU:FlexRay:Connected Channels
#define nxPropECU_FlexRayConnectedChs            ((u32)0x00050014) // u32 --rw
// ECU:FlexRay:Startup Frame
#define nxPropECU_FlexRayStartupFrameRef         ((u32)0x05050011) // ref --r
// ECU:FlexRay:Wakeup Channels
#define nxPropECU_FlexRayWakeupChs               ((u32)0x00050013) // u32 --rw
// ECU:FlexRay:Wakeup Pattern
#define nxPropECU_FlexRayWakeupPtrn              ((u32)0x00050012) // u32 --rw
// ECU:Frames Received
#define nxPropECU_RxFrmRefs                      ((u32)0x06050003) // 1Dref --rw
// ECU:Frames Transmitted
#define nxPropECU_TxFrmRefs                      ((u32)0x06050004) // 1Dref --rw
// ECU:LIN:Configured NAD
#define nxPropECU_LINConfigNAD                   ((u32)0x00050023) // u32 --rw
// ECU:LIN:Function ID
#define nxPropECU_LINFunctionID                  ((u32)0x00050025) // u32 --rw
// ECU:LIN:Initial NAD
#define nxPropECU_LINInitialNAD                  ((u32)0x00050022) // u32 --rw
// ECU:LIN:Master?
#define nxPropECU_LINMaster                      ((u32)0x02050020) // bool --rw
// ECU:LIN:P2min
#define nxPropECU_LINP2min                       ((u32)0x01050026) // f64 --rw
// ECU:LIN:Protocol Version
#define nxPropECU_LINProtocolVer                 ((u32)0x00050021) // u32 --rw
// ECU:LIN:STmin
#define nxPropECU_LINSTmin                       ((u32)0x01050027) // f64 --rw
// ECU:LIN:Supplier ID
#define nxPropECU_LINSupplierID                  ((u32)0x00050024) // u32 --rw
// ECU:Name (Short)
#define nxPropECU_Name                           ((u32)0x03050002) // string --rw
// ECU:SAE J1939:Node Name
#define nxPropECU_J1939NodeName                  ((u32)0x09050029) // u64 --rw
// ECU:SAE J1939:Preferred Address
#define nxPropECU_J1939PreferredAddress          ((u32)0x00050028) // u32 --rw
// LIN Schedule:Cluster
#define nxPropLINSched_ClstRef                   ((u32)0x05060005) // ref --r
// LIN Schedule:Comment
#define nxPropLINSched_Comment                   ((u32)0x03060006) // string --rw
// LIN Schedule:Configuration Status
#define nxPropLINSched_ConfigStatus              ((u32)0x00060007) // u32 --r
// LIN Schedule:Entries
#define nxPropLINSched_Entries                   ((u32)0x06060001) // 1Dref --r
// LIN Schedule:Name
#define nxPropLINSched_Name                      ((u32)0x03060002) // string --rw
// LIN Schedule:Priority
#define nxPropLINSched_Priority                  ((u32)0x00060003) // u32 --rw
// LIN Schedule:Run Mode
#define nxPropLINSched_RunMode                   ((u32)0x00060004) // u32 --rw
// LIN Schedule Entry:Collision Resolving Schedule
#define nxPropLINSchedEntry_CollisionResSched    ((u32)0x05070001) // ref --rw
// LIN Schedule Entry:Delay
#define nxPropLINSchedEntry_Delay                ((u32)0x01070002) // f64 --rw
// LIN Schedule Entry:Event Identifier
#define nxPropLINSchedEntry_EventID              ((u32)0x00070003) // u32 --rw
// LIN Schedule Entry:Frames
#define nxPropLINSchedEntry_Frames               ((u32)0x06070004) // 1Dref --rw
// LIN Schedule Entry:Name
#define nxPropLINSchedEntry_Name                 ((u32)0x03070006) // string --rw
// LIN Schedule Entry:Name (Unique to Cluster)
#define nxPropLINSchedEntry_NameUniqueToCluster  ((u32)0x03070008) // string --r
// LIN Schedule Entry:Node Configuration:Free Format:Data Bytes
#define nxPropLINSchedEntry_NC_FF_DataBytes      ((u32)0x0A070009) // 1Du8 --rw
// LIN Schedule Entry:Schedule
#define nxPropLINSchedEntry_Sched                ((u32)0x05070007) // ref --r
// LIN Schedule Entry:Type
#define nxPropLINSchedEntry_Type                 ((u32)0x00070005) // u32 --rw
// PDU:Cluster
#define nxPropPDU_ClusterRef                     ((u32)0x05080004) // ref --r
// PDU:Comment
#define nxPropPDU_Comment                        ((u32)0x03080002) // string --rw
// PDU:Configuration Status
#define nxPropPDU_ConfigStatus                   ((u32)0x00080007) // u32 --r
// PDU:Default Payload
#define nxPropPDU_DefaultPayload                 ((u32)0x0A080005) // 1Du8 --rw
// PDU:Frames
#define nxPropPDU_FrmRefs                        ((u32)0x06080006) // 1Dref --r
// PDU:Mux:Data Multiplexer Signal
#define nxPropPDU_MuxDataMuxSigRef               ((u32)0x05080009) // ref --r
// PDU:Mux:Is Data Multiplexed?
#define nxPropPDU_MuxIsMuxed                     ((u32)0x02080008) // bool --r
// PDU:Mux:Static Signals
#define nxPropPDU_MuxStaticSigRefs               ((u32)0x0608000A) // 1Dref --r
// PDU:Mux:Subframes
#define nxPropPDU_MuxSubframeRefs                ((u32)0x0608000B) // 1Dref --r
// PDU:Name (Short)
#define nxPropPDU_Name                           ((u32)0x03080001) // string --rw
// PDU:Payload Length
#define nxPropPDU_PayloadLen                     ((u32)0x00080003) // u32 --rw
// PDU:Signals
#define nxPropPDU_SigRefs                        ((u32)0x06080005) // 1Dref --r


#define nxPropSession_IntfCANOutStrmListById nxPropSession_IntfOutStrmListById

/***********************************************************************
   C O N S T A N T S   F O R   F U N C T I O N   P A R A M E T E R S
***********************************************************************/

   // Parameter Mode of function nxCreateSession
#define nxMode_SignalInSinglePoint           0  // SignalInSinglePoint
#define nxMode_SignalInWaveform              1  // SignalInWaveform
#define nxMode_SignalInXY                    2  // SignalInXY
#define nxMode_SignalOutSinglePoint          3  // SignalOutSinglePoint
#define nxMode_SignalOutWaveform             4  // SignalOutWaveform
#define nxMode_SignalOutXY                   5  // SignalOutXY
#define nxMode_FrameInStream                 6  // FrameInStream
#define nxMode_FrameInQueued                 7  // FrameInQueued
#define nxMode_FrameInSinglePoint            8  // FrameInSinglePoint
#define nxMode_FrameOutStream                9  // FrameOutStream
#define nxMode_FrameOutQueued                10 // FrameOutQueued
#define nxMode_FrameOutSinglePoint           11 // FrameOutSinglePoint
#define nxMode_SignalConversionSinglePoint   12 // SignalConversionSinglePoint

   // Parameter Scope of functions nxStart, nxStop
#define nxStartStop_Normal                   0  // StartStop_Normal
#define nxStartStop_SessionOnly              1  // StartStop_SessionOnly
#define nxStartStop_InterfaceOnly            2  // StartStop_InterfaceOnly
#define nxStartStop_SessionOnlyBlocking      3  // StartStop_SessionOnlyBlocking

   // Parameter Modifier of nxBlink
#define nxBlink_Disable                      0  // Blink_Disable
#define nxBlink_Enable                       1  // Blink_Enable

   // Terminal names for nxConnectTerminals and nxDisconnectTerminals (source or destination)
#define nxTerm_PXI_Trig0                     "PXI_Trig0"             // PXI_Trig0 same as RTSI0
#define nxTerm_PXI_Trig1                     "PXI_Trig1"
#define nxTerm_PXI_Trig2                     "PXI_Trig2"
#define nxTerm_PXI_Trig3                     "PXI_Trig3"
#define nxTerm_PXI_Trig4                     "PXI_Trig4"
#define nxTerm_PXI_Trig5                     "PXI_Trig5"
#define nxTerm_PXI_Trig6                     "PXI_Trig6"
#define nxTerm_PXI_Trig7                     "PXI_Trig7"
#define nxTerm_FrontPanel0                   "FrontPanel0"
#define nxTerm_FrontPanel1                   "FrontPanel1"
#define nxTerm_PXI_Star                      "PXI_Star"
#define nxTerm_PXI_Clk10                     "PXI_Clk10"
#define nxTerm_10MHzTimebase                 "10MHzTimebase"
#define nxTerm_1MHzTimebase                  "1MHzTimebase"
#define nxTerm_MasterTimebase                "MasterTimebase"
#define nxTerm_CommTrigger                   "CommTrigger"
#define nxTerm_StartTrigger                  "StartTrigger"
#define nxTerm_FlexRayStartCycle             "FlexRayStartCycle"
#define nxTerm_FlexRayMacrotick              "FlexRayMacrotick"
#define nxTerm_LogTrigger                    "LogTrigger"
#define nxTerm_TimeTrigger                   "TimeTrigger"
#define nxTerm_NetworkTimePPS                "NetworkTimePPS"
#define nxTerm_NetworkTime1MHz               "NetworkTime1MHz"

   /* StateID for nxReadState
   These constants use an encoding similar to property ID (nxProp_ prefix).
   */
      // Current time of the interface (using nxTimestamp100ns_t)
#define nxState_TimeCurrent                  ((u32)0x00000001 | nxClass_Interface | nxPrptype_time100ns) // TimeCurrent
      // Time when communication began on the interface (protocol operational / integrated)
#define nxState_TimeCommunicating            ((u32)0x00000002 | nxClass_Interface | nxPrptype_time100ns) // TimeCommunicating
      // Start time of the interface, when the attempt to communicate began (startup protocol)
#define nxState_TimeStart                    ((u32)0x00000003 | nxClass_Interface | nxPrptype_time100ns) // TimeStart
      // Session information: Use macros with prefix nxSessionInfo_Get_ to get fields of the u32
#define nxState_SessionInfo                  ((u32)0x00000004 | nxClass_Interface | nxPrptype_u32)    // SessionInfo
      // Current time of the interface, returned with two timestamps
#define nxState_TimeCurrent2                 ((u32)0x00000005 | nxClass_Interface | nxPrptype_struct) // uses nxTimeLocalNetwork_t
      // Time when communication began on the interface, returned with two timestamps
#define nxState_TimeCommunicating2           ((u32)0x00000006 | nxClass_Interface | nxPrptype_struct) // uses nxTimeLocalNetwork_t
      // Start time of the interface, returned with two timestamps
#define nxState_TimeStart2                   ((u32)0x00000007 | nxClass_Interface | nxPrptype_struct) // uses nxTimeLocalNetwork_t
      // CAN communication: Use macros with prefix nxCANComm_Get_ to get fields of the u32
#define nxState_CANComm                      ((u32)0x00000010 | nxClass_Interface | nxPrptype_u32)    // CANComm
      // FlexRay communication: Use macros with prefix nxFlexRayComm_Get_ to get fields of the u32
#define nxState_FlexRayComm                  ((u32)0x00000020 | nxClass_Interface | nxPrptype_u32)    // FlexRayComm
      // FlexRay statistics: Use typedef nxFlexRayStats_t to read these statistics using a struct of multiple u32
#define nxState_FlexRayStats                 ((u32)0x00000021 | nxClass_Interface | nxPrptype_1Du32)  // FlexRayStats
      // LIN communication: Use macros with prefix nxLINComm_Get_ to get fields of 2 u32's
#define nxState_LINComm                      ((u32)0x00000030 | nxClass_Interface | nxPrptype_u32)    // LINComm
      // J1939 communication:
#define nxState_J1939Comm                    ((u32)0x00000040 | nxClass_Interface | nxPrptype_u32)    // J1939Comm

   /* StateID for nxWriteState
   These constants use an encoding similar to property ID (nxProp_ prefix).
   */
#define nxState_LINScheduleChange            ((u32)0x00000081 | nxClass_Interface | nxPrptype_u32)    // LINScheduleChange
#define nxState_LINDiagnosticScheduleChange  ((u32)0x00000083 | nxClass_Interface | nxPrptype_u32)    // LINDiagnosticScheduleChange
#define nxState_FlexRaySymbol                ((u32)0x00000082 | nxClass_Interface | nxPrptype_u32)    // FlexRaySymbol
#define nxState_EthernetSleep                ((u32)0x00000084 | nxClass_Interface | nxPrptype_u32)    // EthernetSleep
#define nxState_EthernetWake                 ((u32)0x00000085 | nxClass_Interface | nxPrptype_u32)    // EthernetWake

#define  nxCanFdMode_ISO         0  // ISO mode, default
#define  nxCanFdMode_NonISO      1  // Non-ISO mode (first CAN FD definition)
#define  nxCanFdMode_ISO_Legacy  2  // ISO mode, but behaviour like non-ISO

   // Macros to get fields of u32 returned by nxReadState of nxState_SessionInfo
      // Get state of frames in the session; uses constants with prefix nxSessionInfoState_
#define nxSessionInfo_Get_State(StateValue)  ((u8)( (u32)StateValue         & 0x00000003))

   // State of frames in the session, from nxState_SessionInfo (nxSessionInfo_Get_State)
#define nxSessionInfoState_Stopped           0     // all frames stopped
#define nxSessionInfoState_Started           1     // all frames started
#define nxSessionInfoState_Mix               2     // one or more frames started, and one or more frames stopped

   // Macros to get fields of u32 returned by nxReadState of nxState_CANComm
      // Get CAN communication state; uses constants with prefix nxCANCommState_
#define nxCANComm_Get_CommState(StateValue)  ((u8)( (u32)StateValue         & 0x0000000F))
      // Get CAN transceiver error (!NERR); 1 = error, 0 = no error
#define nxCANComm_Get_TcvrErr(StateValue)    ((u8)( ((u32)StateValue >> 4)  & 0x00000001))
      // Get indication of CAN controller/transceiver sleep; 1 = asleep, 0 = awake
#define nxCANComm_Get_Sleep(StateValue)      ((u8)( ((u32)StateValue >> 5)  & 0x00000001))
      // Get last bus error that incremented counters; uses constants with prefix nxCANLastErr_
#define nxCANComm_Get_LastErr(StateValue)    ((u8)( ((u32)StateValue >> 8)  & 0x0000000F))
      // Get Transmit Error Counter as defined by the CAN protocol specification
#define nxCANComm_Get_TxErrCount(StateValue) ((u8)( ((u32)StateValue >> 16) & 0x000000FF))
      // Get Receive Error Counter as defined by the CAN protocol specification
#define nxCANComm_Get_RxErrCount(StateValue) ((u8)( ((u32)StateValue >> 24) & 0x000000FF))

   // Communication state from nxState_CANComm (nxCANComm_Get_CommState)
#define nxCANCommState_ErrorActive           0
#define nxCANCommState_ErrorPassive          1
#define nxCANCommState_BusOff                2
#define nxCANCommState_Init                  3

   // Last bus error from nxState_CANComm (nxCANComm_Get_LastErr)
#define nxCANLastErr_None                    0
#define nxCANLastErr_Stuff                   1
#define nxCANLastErr_Form                    2
#define nxCANLastErr_Ack                     3
#define nxCANLastErr_Bit1                    4
#define nxCANLastErr_Bit0                    5
#define nxCANLastErr_CRC                     6

   // constants for nxPropClst_CanIoMode, nxPropSession_IntfCanIoMode, nxPropSession_IntfCanTxIoMode, nxPropAlias_CanIoMode
#define nxCANioMode_CAN                      0
#define nxCANioMode_CAN_FD                   1
#define nxCANioMode_CAN_FD_BRS               2

   // Macros to get fields of u32 returned by nxReadState of nxState_FlexRayComm
      /* Get FlexRay Protocol Operation Control (POC) state,
      which uses constants with prefix nxFlexRayPOCState_ */
#define nxFlexRayComm_Get_POCState(StateValue)        ((u8)((u32)StateValue & 0x0000000F))
      /* From FlexRay spec 9.3.1.3.4: "the number of consecutive even/odd cycle pairs
      (vClockCorrectionFailed) that have passed without clock synchronization having performed an offset or a rate
      correction due to lack of synchronization frames (as maintained by the POC process)."
      This value is used for comparison to the cluster thresholds MaxWithoutClockCorrectFatal and
      MaxWithoutClockCorrectionPassive (XNET properties nxPropClst_FlexRayMaxWoClkCorFat
      and nxPropClst_FlexRayMaxWoClkCorPas). */
#define nxFlexRayComm_Get_ClockCorrFailed(StateValue) ((u8)( ((u32)StateValue >> 4) & 0x0000000F))
      /* From FlexRay spec 9.3.1.3.1: "the number of consecutive even/odd cycle pairs (vAllowPassiveToActive)
      that have passed with valid rate and offset correction terms, but the node still in POC:normal passive
      state due to a host configured delay to POC:normal active state (as maintained by the POC process).
      This value is used for comparison to the interface threshold AllowPassiveToActive
      (XNET property nxPropSession_IntfFlexRayAlwPassAct). */
#define nxFlexRayComm_Get_PassiveToActiveCount(StateValue)  \
                                                      ((u8)( ((u32)StateValue >> 8) & 0x0000001F))
#define nxFlexRayComm_Get_ChannelASleep(StateValue)  \
                                                      ((u8)( ((u32)StateValue >> 13) & 0x00000001))
#define nxFlexRayComm_Get_ChannelBSleep(StateValue)  \
                                                      ((u8)( ((u32)StateValue >> 14) & 0x00000001))

   // POC state (Protocol Operation Control state) from nxFlexRayPOC_Get_State
#define nxFlexRayPOCState_DefaultConfig      0
#define nxFlexRayPOCState_Ready              1
#define nxFlexRayPOCState_NormalActive       2
#define nxFlexRayPOCState_NormalPassive      3
#define nxFlexRayPOCState_Halt               4
#define nxFlexRayPOCState_Monitor            5
#define nxFlexRayPOCState_Config             15

   // Macros to get fields of 1st u32 returned by nxReadState of nxState_LINComm
      // Get indication of LIN interface sleep state; 1 = asleep, 0 = awake
#define nxLINComm_Get_Sleep(StateValue)      ((u8)( ((u32)StateValue >> 1) & 0x00000001))
      // Get LIN communication state; uses constants with prefix nxLINCommState_
#define nxLINComm_Get_CommState(StateValue)  ((u8)( ((u32)StateValue >> 2) & 0x00000003))
      // Get last bus error; this code uses constants with prefix nxLINLastErrCode_
#define nxLINComm_Get_LastErrCode(StateValue) \
                                             ((u8)( ((u32)StateValue >> 4) & 0x0000000F))
      // Get received data for last bus error; this value applies only to specific codes
#define nxLINComm_Get_LastErrReceived(StateValue) \
                                             ((u8)( ((u32)StateValue >> 8) & 0x000000FF))
      // Get expected data for last bus error; this value applies only to specific codes
#define nxLINComm_Get_LastErrExpected(StateValue) \
                                             ((u8)( ((u32)StateValue >> 16) & 0x000000FF))
      // Get ID of last bus error; this value applies only to specific codes
#define nxLINComm_Get_LastErrID(StateValue) \
                                             ((u8)( ((u32)StateValue >> 24) & 0x0000003F))
      // Get indication of LIN transceiver ready (powered); 1 = powered, 0 = not powered
#define nxLINComm_Get_TcvrRdy(StateValue)    ((u8)( ((u32)StateValue >> 31) & 0x00000001))

   // Macros to get fields of 2nd u32 returned by nxReadState of nxState_LINComm
      // Get index of the currently running schedule (0xFF if Null-schedule).
#define nxLINComm_Get2_ScheduleIndex(State2Value) \
                                             ((u8)( ((u32)State2Value) & 0x000000FF))

   // Communication state from nxState_LINComm (nxLINComm_Get_CommState macro)
#define nxLINCommState_Idle                  0
#define nxLINCommState_Active                1
#define nxLINCommState_Inactive              2

   // Diagnostic schedule state for nxState_LINDiagnosticScheduleChange
#define nxLINDiagnosticSchedule_NULL         0x0000
#define nxLINDiagnosticSchedule_MasterReq    0x0001
#define nxLINDiagnosticSchedule_SlaveResp    0x0002

   // Last error code from nxState_LINComm (nxLINComm_Get_LastErrCode macro)
#define nxLINLastErrCode_None                0
#define nxLINLastErrCode_UnknownId           1
#define nxLINLastErrCode_Form                2
#define nxLINLastErrCode_Framing             3
#define nxLINLastErrCode_Readback            4
#define nxLINLastErrCode_Timeout             5
#define nxLINLastErrCode_CRC                 6

   // Condition of nxWait
#define nxCondition_TransmitComplete         0x8001  // TransmitComplete
#define nxCondition_IntfCommunicating        0x8002  // IntfCommunicating
#define nxCondition_IntfRemoteWakeup         0x8003  // IntfRemoteWakeup
#define nxCondition_EthernetSynced           0x8004  // EthernetSynced

   // Constants for use with Timeout parameter of read and write functions
#define nxTimeout_None                       (0)
#define nxTimeout_Infinite                   (-1)

   // Parameter Mode of function nxdbGetDBCAttribute and nxdbGetDBCAttributeSize
#define nxGetDBCMode_Attribute               0  // Attribute
#define nxGetDBCMode_EnumerationList         1  // Enumeration List
#define nxGetDBCMode_AttributeList           2  // List of available attributes of given type
#define nxGetDBCMode_ValueTableList          3  // Value table for a signal

   // Copy mode of function nxdbMerge
#define nxdbMerge_CopyUseSource     0  // CopyUseSource
#define nxdbMerge_CopyUseTarget     1  // CopyUseTarget
#define nxdbMerge_MergeUseSource    2  // MergeUseSource
#define nxdbMerge_MergeUseTarget    3  // MergeUseTarget

   // For nxReadState or nxReadStateTimeTrigger using nxTimeLocalNetwork_t,
   // the following bitmasks are used with the Flags field.
#define nxTimeFlags_NetworkSynced               0x00000001

   // For UseFlags field of nxEptRxFilter_Element_t, which is
   // a single element of the array that is get/set using
   // property nxPropSession_IntfEnetEptReceiveFilter.
#define nxEptRxFilter_UseFlags_VID              0x00000001
#define nxEptRxFilter_UseFlags_Priority         0x00000002
#define nxEptRxFilter_UseFlags_DestinationMAC   0x00000004

   // Timescale parameter of nxFutureTimeTrigger
#define nxTimescale_LocalTime                0
#define nxTimescale_NetworkTime              1

/***********************************************************************
   C O N S T A N T S   F O R   H A R D W A R E   P R O P E R T I E S
***********************************************************************/

// System/Device/Interface properties (hardware info)

   // Property ID nxPropSys_VerPhase
#define nxPhase_Development                  0
#define nxPhase_Alpha                        1
#define nxPhase_Beta                         2
#define nxPhase_Release                      3

   // Property ID nxPropDev_FormFac
#define nxDevForm_PXI                        0
#define nxDevForm_PCI                        1
#define nxDevForm_cSeries                    2
#define nxDevForm_PXIe                       3
#define nxDevForm_USB                        4
#define nxDevForm_PCIe                       5

   // Property ID nxPropIntf_CANTermCap
#define nxCANTermCap_No                      0
#define nxCANTermCap_Yes                     1

   // Property ID nxPropIntf_CANTcvrCap
#define nxCANTcvrCap_HS                      0
#define nxCANTcvrCap_LS                      1
#define nxCANTcvrCap_XS                      3
#define nxCANTcvrCap_XS_HS_LS                4
#define nxCANTcvrCap_Unknown                 0xFFFFFFFF

   // Property ID nxPropIntf_Protocol and nxPropClst_Protocol
#define nxProtocol_Unknown                   0xFFFFFFFE   //The value will be reported on a port with unplugged transceiver cable
#define nxProtocol_CAN                       0
#define nxProtocol_FlexRay                   1
#define nxProtocol_LIN                       2
#define nxProtocol_Ethernet                  3

   // Property ID nxPropClst_ApplicationProtocol and nxPropSession_ApplicationProtocol
#define nxAppProtocol_None                   0
#define nxAppProtocol_J1939                  1

   // State of the dongle (nxPropIntf_DongleState)
#define nxDongleState_NoDongle_NoExtPower    1
#define nxDongleState_NoDongle_ExtPower      2
#define nxDongleState_Dongle_NoExtPower      3
#define nxDongleState_Ready                  4
#define nxDongleState_Busy                   5
#define nxDongleState_CommError              13
#define nxDongleState_OverCurrent            14

   // Dongle ID (nxPropIntf_DongleID)
#define nxDongleID_LS_CAN           1
#define nxDongleID_HS_CAN           2
#define nxDongleID_SW_CAN           3
#define nxDongleID_XS_CAN           4
#define nxDongleID_LIN              6
#define nxDongleID_DongleLess       13
#define nxDongleID_Unknown          14

/***********************************************************************
   C O N S T A N T S   F O R   S E S S I O N   P R O P E R T I E S
***********************************************************************/

// Session properties (including runtime interface properties)

   // Macro to set nxPropSession_IntfBaudRate for an advanced CAN baud rate (bit timings)
   // If you pass a basic baud rate like 125000 or 500000, NI-XNET calculates bit timings for you
#define nxAdvCANBaudRate_Set(TimeQuantum, TimeSeg0, TimeSeg1, SyncJumpWidth) ( \
            (((u32)TimeQuantum) & 0x0000FFFF) | \
            (((u32)TimeSeg0 << 16) & 0x000F0000) | \
            (((u32)TimeSeg1 << 20) & 0x00700000) | \
            (((u32)SyncJumpWidth << 24) & 0x03000000) | \
            ((u32)0x80000000) )

   // Macros to get fields of nxPropSession_IntfBaudRate for an advanced CAN baud rate
#define nxAdvCANBaudRate_Get_TimeQuantum(AdvBdRt)     ((u16)( ((u32)AdvBdRt) & 0x0000FFFF))
#define nxAdvCANBaudRate_Get_TimeSeg0(AdvBdRt)        ((u8)( ((u32)AdvBdRt >> 16) & 0x0000000F))
#define nxAdvCANBaudRate_Get_TimeSeg1(AdvBdRt)        ((u8)( ((u32)AdvBdRt >> 20) & 0x00000007))
#define nxAdvCANBaudRate_Get_SyncJumpWidth(AdvBdRt)   ((u8)( ((u32)AdvBdRt >> 24) & 0x00000003))
#define nxAdvCANBaudRate_Get_NumSamples(AdvBdRt)      ((u8)( ((u32)AdvBdRt >> 26) & 0x00000001))

   // Property ID nxPropSession_IntfCANTerm
#define nxCANTerm_Off                        0
#define nxCANTerm_On                         1

    // Property ID nxPropSession_IntfCANTcvrState
#define nxCANTcvrState_Normal                0
#define nxCANTcvrState_Sleep                 1
#define nxCANTcvrState_SWWakeup              2
#define nxCANTcvrState_SWHighSpeed           3

   // Property ID nxPropSession_IntfCANTcvrType
#define nxCANTcvrType_HS                     0
#define nxCANTcvrType_LS                     1
#define nxCANTcvrType_SW                     2
#define nxCANTcvrType_Ext                    3
#define nxCANTcvrType_Disc                   4

   // Property ID nxPropSession_IntfFlexRaySampPerMicro
#define nxFlexRaySampPerMicro_1              0
#define nxFlexRaySampPerMicro_2              1
#define nxFlexRaySampPerMicro_4              2

   // Property ID nxPropSession_IntfFlexRayTerm
#define nxFlexRayTerm_Off                    0
#define nxFlexRayTerm_On                     1

   // Property ID nxPropSession_IntfLINSleep
#define nxLINSleep_RemoteSleep               0
#define nxLINSleep_RemoteWake                1
#define nxLINSleep_LocalSleep                2
#define nxLINSleep_LocalWake                 3

   // Property ID nxPropSession_IntfLINTerm
#define nxLINTerm_Off                        0
#define nxLINTerm_On                         1

   // Property ID nxPropSession_IntfOutStrmTimng
#define nxOutStrmTimng_Immediate             0
#define nxOutStrmTimng_ReplayExclusive       1
#define nxOutStrmTimng_ReplayInclusive       2

   // Property ID nxPropSession_IntfCANPendTxOrder
#define nxCANPendTxOrder_AsSubmitted         0
#define nxCANPendTxOrder_ByIdentifier        1

   // Property ID nxPropSession_IntfFlexRaySleep
#define nxFlexRaySleep_LocalSleep            0
#define nxFlexRaySleep_LocalWake             1
#define nxFlexRaySleep_RemoteWake            2

   // Property ID nxPropSession_IntfCANExtTcvrConfig
   // These bits can be combined to define the capabilities of the connected
   // external transceiver.
#define nxCANExtTcvrConfig_NormalSupported              (1 << 2)
#define nxCANExtTcvrConfig_SleepSupported               (1 << 5)
#define nxCANExtTcvrConfig_SWWakeupSupported            (1 << 8)
#define nxCANExtTcvrConfig_SWHighSpeedSupported         (1 << 11)
#define nxCANExtTcvrConfig_PowerOnSupported             (1 << 14)
#define nxCANExtTcvrConfig_NormalOutput0Set             (1 << 0)
#define nxCANExtTcvrConfig_SleepOutput0Set              (1 << 3)
#define nxCANExtTcvrConfig_SWWakeupOutput0Set           (1 << 6)
#define nxCANExtTcvrConfig_SWHighSpeedOutput0Set        (1 << 9)
#define nxCANExtTcvrConfig_PowerOnOutput0Set            (1 << 12)
#define nxCANExtTcvrConfig_NormalOutput1Set             (1 << 1)
#define nxCANExtTcvrConfig_SleepOutput1Set              (1 << 4)
#define nxCANExtTcvrConfig_SWWakeupOutput1Set           (1 << 7)
#define nxCANExtTcvrConfig_SWHighSpeedOutput1Set        (1 << 10)
#define nxCANExtTcvrConfig_PowerOnOutput1Set            (1 << 13)
#define nxCANExtTcvrConfig_nErrConnected                (1 << 31)

   // Ethernet port modes (nxPropSession_IntfEnetPortMode)
#define nxEnetPortMode_Direct                0
#define nxEnetPortMode_Tap                   1

   // Ethernet PHY states (nxPropSession_IntfEnetPhyState)
#define nxEnetPhyState_Slave                 0
#define nxEnetPhyState_Master                1
#define nxEnetPhyState_Auto                  2

   // Ethernet Link speeds (nxPropSession_IntfEnetLinkSpeedConfigured and nxPropSession_IntfEnetLinkSpeed)
   // Note: nxEnetLinkSpeed_LinkDown is valid only for nxPropSession_IntfEnetLinkSpeed
#define nxEnetLinkSpeed_LinkDown      0
#define nxEnetLinkSpeed_100Mbps       1
#define nxEnetLinkSpeed_1000Mbps      2

   // Ethernet Jumbo Frames enum values (nxPropSession_IntfEnetJumboFrames)
#define nxEnetJumboFrames_Disabled           0
#define nxEnetJumboFrames_9018Bytes          1

   // Ethernet operational status values (nxPropSession_IntfEnetOperationalStatus)
#define nxEnetOperationalStatus_Down         0
#define nxEnetOperationalStatus_Up           1

   // Ethernet logging mode values (nxPropSession_IntfEnetLogMode)
#define nxEnetLogMode_Off                    0
#define nxEnetLogMode_Log                    1

   // Ethernet logging operation values (nxPropSession_IntfEnetLogOperation)
#define nxEnetLogOperation_CreateOrReplace   0
#define nxEnetLogOperation_Create            1

   // Ethernet Time Sync Protocol (nxPropSession_IntfEnetTimeProtocol)
#define nxEnetTimeProtocol_IEEE8021as        0

   // Ethernet Time Sync Clock Accuracy (nxPropSession_IntfEnetTimeClkAccuracy)
#define nxEnetTimeClkAccuracy_Within25nsec      32
#define nxEnetTimeClkAccuracy_Within100nsec     33
#define nxEnetTimeClkAccuracy_Within250nsec     34
#define nxEnetTimeClkAccuracy_Within1usec       35
#define nxEnetTimeClkAccuracy_Within2500nsec    36
#define nxEnetTimeClkAccuracy_Within10usec      37
#define nxEnetTimeClkAccuracy_Within25usec      38
#define nxEnetTimeClkAccuracy_Within100usec     39
#define nxEnetTimeClkAccuracy_Within250usec     40
#define nxEnetTimeClkAccuracy_Within1msec       41
#define nxEnetTimeClkAccuracy_Within2500usec    42
#define nxEnetTimeClkAccuracy_Within10msec      43
#define nxEnetTimeClkAccuracy_Within25msec      44
#define nxEnetTimeClkAccuracy_Within100msec     45
#define nxEnetTimeClkAccuracy_Within250msec     46
#define nxEnetTimeClkAccuracy_Within1sec        47
#define nxEnetTimeClkAccuracy_Within10sec       48
#define nxEnetTimeClkAccuracy_GreatherThan10sec 49
#define nxEnetTimeClkAccuracy_Unknown           254


   // Ethernet Time Sync Port Sync Status (nxPropSession_IntfEnetTimePortSyncStatus)
#define nxEnetTimePortSyncStatus_Synced                   0
#define nxEnetTimePortSyncStatus_EnetLinkDown             1
#define nxEnetTimePortSyncStatus_ProtocolDisabled         2
#define nxEnetTimePortSyncStatus_MeasuringPropDelay       3
#define nxEnetTimePortSyncStatus_MasterPendingAnnounce    4
#define nxEnetTimePortSyncStatus_WaitingForMaster         5
#define nxEnetTimePortSyncStatus_SyncingToMaster          6
#define nxEnetTimePortSyncStatus_PeerNotProtoCapable      7
#define nxEnetTimePortSyncStatus_PropDelayExceedsTreshold 8
#define nxEnetTimePortSyncStatus_SyncReceiptTimeout       9
#define nxEnetTimePortSyncStatus_FrequencyOutOfRange      10
#define nxEnetTimePortSyncStatus_SyncIntervalOutOfRange   11
#define nxEnetTimePortSyncStatus_MultipleMastersDetected  12


   // Ethernet Time Sync Port State Configured (nxPropSession_IntfEnetTimePortStateConfigured)
#define nxEnetTimePortState_Disabled         3
#define nxEnetTimePortState_Master           6
#define nxEnetTimePortState_Passive          7
#define nxEnetTimePortState_Slave            9

   // Ethernet Time Sync PDelay Req Interval (nxPropSession_IntfEnetTimePortLogPdelayIntervalConfigured)
#define nxEnetTimePDelayReqInterval_125ms   -3
#define nxEnetTimePDelayReqInterval_250ms   -2
#define nxEnetTimePDelayReqInterval_500ms   -1
#define nxEnetTimePDelayReqInterval_1s       0
#define nxEnetTimePDelayReqInterval_2s       1

   // Ethernet Time Sync Sync Interval (nxPropSession_IntfEnetTimePortLogSyncIntervalConfigured)
#define nxEnetTimeSyncInterval_125ms        -3
#define nxEnetTimeSyncInterval_250ms        -2
#define nxEnetTimeSyncInterval_500ms        -1
#define nxEnetTimeSyncInterval_1s            0
#define nxEnetTimeSyncInterval_2s            1

   // Ethernet Time Sync Announce Interval (nxPropSession_IntfEnetTimePortLogAnnounceIntervalConfigured)
#define nxEnetTimeAnnounceInterval_125ms    -3
#define nxEnetTimeAnnounceInterval_250ms    -2
#define nxEnetTimeAnnounceInterval_500ms    -1
#define nxEnetTimeAnnounceInterval_1s        0
#define nxEnetTimeAnnounceInterval_2s        1

   // Ethernet Sleep Capability (nxPropSession_IntfEnetSleepCapability)
#define nxEnetSleepCapability_DisabledOrNotAvailable 0
#define nxEnetSleepCapability_Enabled  1

   // Ethernet PHY Power Mode (nxPropSession_IntfEnetPhyPowerMode)
#define nxEnetPhyPowerMode_Normal 0
#define nxEnetPhyPowerMode_Sleep 1

/***********************************************************************
   C O N S T A N T S   F O R   D A T A B A S E   P R O P E R T I E S
***********************************************************************/

// Database properties (Database/Cluster/ECU/Frame/Subframe/Signal)

   // Property ID nxPropClst_FlexRayChannels, nxPropFrm_FlexRayChAssign
   // nxPropClst_FlexRayConnectedChannels and nxPropClst_FlexRayWakeChannels
#define nxFrmFlexRayChAssign_A                  1
#define nxFrmFlexRayChAssign_B                  2
#define nxFrmFlexRayChAssign_AandB              3
#define nxFrmFlexRayChAssign_None               4

   // Property ID nxPropClst_FlexRaySampClkPer
#define nxClstFlexRaySampClkPer_p0125us         0
#define nxClstFlexRaySampClkPer_p025us          1
#define nxClstFlexRaySampClkPer_p05us           2

   // Property ID nxPropFrm_FlexRayTimingType
#define nxFrmFlexRayTiming_Cyclic               0
#define nxFrmFlexRayTiming_Event                1

   // Property ID nxPropFrm_CANTimingType
#define nxFrmCANTiming_CyclicData               0
#define nxFrmCANTiming_EventData                1
#define nxFrmCANTiming_CyclicRemote             2
#define nxFrmCANTiming_EventRemote              3
#define nxFrmCANTiming_CyclicEvent              4

   // Property ID nxPropSig_ByteOrdr
#define nxSigByteOrdr_LittleEndian              0  // Intel
#define nxSigByteOrdr_BigEndian                 1  // Motorola

   // Property ID nxPropSig_DataType
#define nxSigDataType_Signed                    0
#define nxSigDataType_Unsigned                  1
#define nxSigDataType_IEEEFloat                 2
#define nxSigDataType_ByteArray                 3

   // Property ID nxPropECU_LINProtocolVer
#define nxLINProtocolVer_1_2                    2
#define nxLINProtocolVer_1_3                    3
#define nxLINProtocolVer_2_0                    4
#define nxLINProtocolVer_2_1                    5
#define nxLINProtocolVer_2_2                    6

   // Property ID nxPropLINSched_RunMode
#define nxLINSchedRunMode_Continuous            0
#define nxLINSchedRunMode_Once                  1
#define nxLINSchedRunMode_Null                  2

   // Property ID nxPropLINSchedEntry_Type
#define nxLINSchedEntryType_Unconditional       0
#define nxLINSchedEntryType_Sporadic            1
#define nxLINSchedEntryType_EventTriggered      2
#define nxLINSchedEntryType_NodeConfigService   3

   // Property ID nxPropFrm_LINChecksum
#define nxFrmLINChecksum_Classic                0
#define nxFrmLINChecksum_Enhanced               1

/***********************************************************************
                            D A T A   T Y P E S
***********************************************************************/

   /* The ANSI C99 standard defines simple numeric types of a specific size,
   such as int32_t for a signed 32-bit integer.
   Many C/C++ compilers are not ANSI C99 by default, such as Microsoft Visual C/C++.
   Therefore, NI-XNET does not require use of ANSI C99.
   Since NI-XNET does not attempt to override ANSI C99 types (as defined in stdint.h),
   it uses legacy National Instruments numeric types such as i32. If desired, you can use
   ANSI C99 numeric types instead of the analogous NI-XNET numeric type
   (i.e. int32_t instead of i32). */

#ifndef _NIDAQ_Header_      // Traditional NI-DAQ header defines numeric types same as below.
#ifndef nNISS100_kCPP       // Same for NI SS layer.

#ifndef _NI_i8_DEFINED_
#define _NI_i8_DEFINED_
typedef signed char        i8;
#endif
#ifndef _NI_i16_DEFINED_
#define _NI_i16_DEFINED_
typedef signed short       i16;
#endif

#ifndef _NI_i32_DEFINED_
#define _NI_i32_DEFINED_
#if (defined(_MSC_VER) || defined(_CVI_) || defined(__BORLANDC__))
   typedef signed int     i32;
#elif defined(__GNUC__)
   typedef int32_t i32;
#endif
#endif

#ifndef _NI_i64_DEFINED_
#define _NI_i64_DEFINED_
#if (defined(_MSC_VER) || defined(_CVI_) || defined(__BORLANDC__))
   typedef __int64     i64;
#elif defined(__GNUC__)
   typedef long long int   i64;
#endif
#endif

#ifndef _NI_u8_DEFINED_
#define _NI_u8_DEFINED_
typedef unsigned char      u8;
#endif

#ifndef _NI_u16_DEFINED_
#define _NI_u16_DEFINED_
typedef unsigned short     u16;
#endif

#ifndef _NI_u32_DEFINED_
#define _NI_u32_DEFINED_
#if (defined(_MSC_VER) || defined(_CVI_) || defined(__BORLANDC__))
   typedef unsigned int    u32;
#elif defined(__GNUC__)
   typedef uint32_t u32;
#endif
#endif

#ifndef _NI_u64_DEFINED_
#define _NI_u64_DEFINED_
#if (defined(_MSC_VER) || defined(_CVI_) || defined(__BORLANDC__))
   typedef unsigned __int64     u64;
#elif defined(__GNUC__)
   typedef unsigned long long int   u64;
#endif
#endif

#ifndef _NI_f32_DEFINED_
#define _NI_f32_DEFINED_
typedef float              f32;
#endif

#ifndef _NI_f64_DEFINED_
#define _NI_f64_DEFINED_
typedef double             f64;
#endif

typedef void*              nxVoidPtr;
typedef u32*               nxU32Ptr;
#endif // nNISS100_kCPP
#endif // _NIDAQ_Header_

   // Session Reference (handle).
typedef u32 nxSessionRef_t;

   // Database Reference (handle).
typedef u32 nxDatabaseRef_t;

typedef i32 nxStatus_t;       // Return value

   // Absolute timestamp in 100 nanosecond increments.
   // This 64-bit type contains the number of 100 ns intervals that have
   // elapsed since 1 January 1601 00:00:00 Coordinated Universal Time (UTC).
typedef u64 nxTimestamp100ns_t;
   // In previous releases this name was used for nxTimestamp100ns_t.
typedef nxTimestamp100ns_t nxTimestamp_t;

   // Absolute timestamp in 1 nanosecond increments.
   // This 64-bit type contains the number of 1 ns intervals that have
   // elapsed since 1 January 1970 00:00:00 International Atomic Time (TAI).
typedef u64 nxTimestamp1ns_t;

typedef struct _nxFlexRayStats_t {
      u32 NumSyntaxErrorChA;
      u32 NumSyntaxErrorChB;
      u32 NumContentErrorChA;
      u32 NumContentErrorChB;
      u32 NumSlotBoundaryViolationChA;
      u32 NumSlotBoundaryViolationChB;
   } nxFlexRayStats_t;

   // nxReadState nxState_J1939Comm StateValue
typedef struct _nxJ1939CommState_t {
      u32 PGN;
      u8  SourceAddress;
      u8  DestinationAddress;
      u8  TransmitError;
      u8  ReceiveError;
      u32 Reserved1;
      u32 Reserved2;
   } nxJ1939CommState_t;

   // Use with nxReadState nxState_TimeCurrent2, nxState_TimeCommunicating2,
   //    or nxState_TimeStart2;
   // Use with nxReadStateTimeTrigger;
   // Flags field uses constants with prefix nxTimeFlags_

#if defined(_WIN32) || defined(__linux__)
#pragma pack( push, 8 )
#endif

typedef struct _nxTimeLocalNetwork_t {
      nxTimestamp1ns_t LocalTime;
      nxTimestamp1ns_t NetworkTime;
      u32 Flags;
   } nxTimeLocalNetwork_t;

#if defined(_WIN32) || defined(__linux__)
#pragma pack( pop )
#endif

   // Destination MAC address uses null-terminated string of
   // syntax AA:BB:CC:DD:EE:FF
typedef char nxMACAddress_t[18];

   // The property nxPropSession_IntfEnetEptReceiveFilter uses an
   // array of this element type.
   // UseFlags field uses constants with prefix nxEptRxFilter_UseFlags_

#if defined(_WIN32) || defined(__linux__)
#pragma pack( push, 8 )
#endif

typedef struct _nxEptRxFilter_Element_t {
      u32 UseFlags;
      u16 VID;
      u8 Priority;
      nxMACAddress_t DestinationMAC;
   } nxEptRxFilter_Element_t;

#if defined(_WIN32) || defined(__linux__)
#pragma pack( pop )
#endif

/***********************************************************************
                                F R A M E
***********************************************************************/

   // Type
#define nxFrameType_CAN_Data                 0x00
#define nxFrameType_CAN_Remote               0x01
#define nxFrameType_CAN_BusError             0x02
#define nxFrameType_CAN20_Data               0x08
#define nxFrameType_CANFD_Data               0x10
#define nxFrameType_CANFDBRS_Data            0x18
#define nxFrameType_FlexRay_Data             0x20
#define nxFrameType_FlexRay_Null             0x21
#define nxFrameType_FlexRay_Symbol           0x22
#define nxFrameType_LIN_Data                 0x40
#define nxFrameType_LIN_BusError             0x41
#define nxFrameType_LIN_NoResponse           0x42
#define nxFrameType_J1939_Data               0xC0
#define nxFrameType_Special_Delay            0xE0
#define nxFrameType_Special_LogTrigger       0xE1
#define nxFrameType_Special_StartTrigger     0xE2


   /* For Data frames, your application may not be concerned with specifics for
   CAN, FlexRay, or LIN. For example, you can use fields of the frame to determine
   the contents of Payload, and write general-purpose code to map signal
   values in/out of the Payload data bytes.
   This macro can be used with the frame's Type to determine if the frame is a
   data frame. The macro is used in boolean conditionals. */
#define nxFrameType_IsData(frametype) \
            ((u8)(frametype) & 0x7) == 0)

#define nxFrameId_CAN_IsExtended             0x20000000

   // Macros to get fields of frame Identifier for FlexRay input
#define nxFrameId_FlexRay_Get_Slot(FrameId)        (u16)( ((u32)FrameId) & 0x0000FFFF)

   /* When Type is nxFrameType_FlexRay_Data,
   the following bitmasks are used with the Flags field.
   */
#define nxFrameFlags_FlexRay_Startup         0x01     // Startup frame
#define nxFrameFlags_FlexRay_Sync            0x02     // Sync frame
#define nxFrameFlags_FlexRay_Preamble        0x04     // Preamble bit
#define nxFrameFlags_FlexRay_ChA             0x10     // Transfer on Channel A
#define nxFrameFlags_FlexRay_ChB             0x20     // Transfer on Channel B

   /* When Type is nxFrameType_LIN_Data,
   the following bitmasks are used with the Flags field.
   */
#define nxFrameFlags_LIN_EventSlot           0x01     // Unconditional frame in event-triggered slot

   /* When Type is nxFrameType_CAN_Data, nxFrameType_CAN_Remote,
   nxFrameType_FlexRay_Data, or nxFrameType_LIN_Data,
   the following bitmasks are used with the Flags field.
   */
#define nxFrameFlags_TransmitEcho            0x80

   /* When Type is nxFrameType_FlexRay_Symbol,
   the following values are used with the first Payload byte (offset 0).
   */
#define nxFlexRaySymbol_MTS                  0x00
#define nxFlexRaySymbol_Wakeup               0x01

#define  nxInternal_PadPayload(paylod) \
            ( (u16)(paylod) ? (( (u16)(paylod) + 7) & 0x07F8) : 8)

#define  nxFrameFixed_t(payld) \
            struct { \
               nxTimestamp100ns_t  Timestamp; \
               u32                 Identifier; \
               u8                  Type; \
               u8                  Flags; \
               u8                  Info; \
               u8                  PayloadLength; \
               u8                  Payload[ nxInternal_PadPayload(payld) ]; \
            }

// -----------------------------------------------------------------------------
// If you are using CVI version 2009 or earlier, you may see a compile error for
// this line. Upgrade to CVI version 2010 or later for the fix, disable the
// "Build with C99 extensions" compiler option in the "Build Options" dialog of
// CVI or edit your copy of the header file to resolve the error.
// -----------------------------------------------------------------------------
typedef nxFrameFixed_t(8) nxFrameCAN_t;
typedef nxFrameFixed_t(8) nxFrameLIN_t;
typedef nxFrameFixed_t(1) nxFrameVar_t;

#define nxFramePayldLenHigh_Mask_J1939       (7)

#define nxSizeofFrameHeader                  (16)

#define nxFrameSize(payload) \
            (  nxSizeofFrameHeader + nxInternal_PadPayload(payload) )

   /* Get Payload Length. For J1939, the lowest three bits of the Info field
   are the high bits of the PayloadLength (valid up to 1785). */
#define nxFrameGetPayloadLength(frameptr) \
            (  (u32) (frameptr)->PayloadLength | \
               ((frameptr)->Type == nxFrameType_J1939_Data ? \
                  (u32) ((frameptr)->Info & nxFramePayldLenHigh_Mask_J1939) << 8 : \
                  0) \
            )



   /* Set Payload Length. For J1939, the lowest three bits of the Info field
      are the high bits of the PayloadLength (valid up to 1785 bytes). Before using this
      macro with J1939, the frame type should be set to nxFrameType_J1939_Data */
#define nxFrameSetPayloadLength(frameptr,PayloadLen) \
   (frameptr)->PayloadLength = (u8)((PayloadLen)&0xFF); \
   if (nxFrameType_J1939_Data == (frameptr)->Type ) { \
         (frameptr)->Info = (u8)( ( (frameptr)->Info & ( ~ nxFramePayldLenHigh_Mask_J1939 ) ) | \
         (( (PayloadLen) >> 8 ) & nxFramePayldLenHigh_Mask_J1939 ));}


   /* Use this macro to iterate through variable-length frames.
   You call this macro as a function, as if it used the following prototype:
      nxFrameVar_t * nxFrameIterate(nxFrameVar_t * frameptr);
   The input parameter must be initialized to point to the header of a valid frame.
   The macro returns a pointer to the header of the next frame in the buffer.
   In other words, the macro will iterate from one variable-length frame to
   the next variable-length frame.
   */
#define nxFrameIterate(frameptr) \
            (nxFrameVar_t *) ( (u8 *)(frameptr) + nxFrameSize( nxFrameGetPayloadLength(frameptr) ) )

// ******** Ethernet uses a distinct frame format ********

   // Values for Type field.
#define nxEnetFrameType_Data                 0x00
#define nxEnetFrameType_Delay                0xE1
#define nxEnetFrameType_FutureTimeWait       0xE2

   /* When Type is nxEnetFrameType_Data,
   the following bitmasks are used with the Flags field.
   */
#define nxEnetFlags_Transmit                 0x80000000
#define nxEnetFlags_Receive                  0x40000000
#define nxEnetFlags_NetworkSynced            0x00800000
#define nxEnetFlags_Error                    0x00010000

   /* Header that can be used for iteration of Ethernet frame data.
   A 32-bit Frame Check Sequence (FCS) is located after the FrameData.
   The number of bytes of FrameData varies for each Ethernet frame.
   The Length field is the length of FrameData plus 28 (for fields in
   nxFrameEnet_t plus the FCS).
   */

#if defined(_WIN32) || defined(__linux__)
#pragma pack( push, 1 )
#endif

   /* Macro to convert frame Length parameter in the Ethernet struct from network byte order to host order for nxFrameIterateEthernetWrite
   The length is typically in Big Endian byte order
   This macro only works for 2 byte / 16 bit values */

#define BigToHostOrder16(val)      ( (((val) >> 8) & 0x00FF) | (((val) << 8) & 0xFF00) )

   /* Ethernet-specific macro to iterate frames: 

   Use this macro to iterate through variable-length Ethernet frames.
   This macro functions similarly to nxFrameIterate (see description above).
   Note : Use nxFrameIterateEthernetWrite only for Ethernet frames during a frame write session */

#define nxFrameIterateEthernetWrite(frameptr)      (nxFrameEnet_t *) ( (u8 *)(frameptr) + BigToHostOrder16((frameptr->Length)))

   /* This macro is for variable Length Ethernet frames during read sessions, frame's Length 
   parameter during read session is already in host order not requiring conversion to network byte order, 
   Therefore the need for a separate macro
   Note : Use nxFrameIterateEthernetRead only for Ethernet frames during a frame read session */

#define nxFrameIterateEthernetRead(frameptr)      (nxFrameEnet_t *) ( (u8 *)(frameptr) + (frameptr->Length))

typedef struct _nxFrameEnet_t {
      u16 Length;
      u16 Type;
      nxTimestamp1ns_t DeviceTimestamp;
      nxTimestamp1ns_t NetworkTimestamp;
      u32 Flags;
      u8 FrameData[1];
   } nxFrameEnet_t;

#if defined(_WIN32) || defined(__linux__)
#pragma pack( pop )
#endif


#ifndef _NX_FUNCTION_EXPORT

/***********************************************************************
       F U N C T I O N   P R O T O T Y P E S  :  S E S S I O N
***********************************************************************/

nxStatus_t _NXFUNC nxCreateSession (
                           const char * DatabaseName,
                           const char * ClusterName,
                           const char * List,
                           const char * Interface,
                           u32 Mode,
                           nxSessionRef_t * SessionRef);

nxStatus_t _NXFUNC nxCreateSessionByRef (
                           u32 NumberOfDatabaseRef,
                           nxDatabaseRef_t * ArrayOfDatabaseRef,
                           const char * Interface,
                           u32 Mode,
                           nxSessionRef_t * SessionRef);

nxStatus_t _NXFUNC nxGetProperty (
                           nxSessionRef_t SessionRef,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

nxStatus_t _NXFUNC nxGetPropertySize (
                           nxSessionRef_t SessionRef,
                           u32 PropertyID,
                           u32 * PropertySize);

nxStatus_t _NXFUNC nxSetProperty (
                           nxSessionRef_t SessionRef,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

nxStatus_t _NXFUNC nxGetSubProperty (
                           nxSessionRef_t SessionRef,
                           u32 ActiveIndex,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

nxStatus_t _NXFUNC nxGetSubPropertySize (
                           nxSessionRef_t SessionRef,
                           u32 ActiveIndex,
                           u32 PropertyID,
                           u32 * PropertySize);

nxStatus_t _NXFUNC nxSetSubProperty (
                           nxSessionRef_t SessionRef,
                           u32 ActiveIndex,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

nxStatus_t _NXFUNC nxReadFrame (
                           nxSessionRef_t SessionRef,
                           void * Buffer,
                           u32 SizeOfBuffer,
                           f64 Timeout,
                           u32 * NumberOfBytesReturned);

nxStatus_t _NXFUNC nxReadSignalSinglePoint (
                           nxSessionRef_t SessionRef,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           nxTimestamp100ns_t * TimestampBuffer,
                           u32 SizeOfTimestampBuffer);

nxStatus_t _NXFUNC nxReadSignalWaveform (
                           nxSessionRef_t SessionRef,
                           f64 Timeout,
                           nxTimestamp100ns_t * StartTime,
                           f64 * DeltaTime,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           u32 * NumberOfValuesReturned);

nxStatus_t _NXFUNC nxReadSignalXY (
                           nxSessionRef_t SessionRef,
                           nxTimestamp100ns_t * TimeLimit,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           nxTimestamp100ns_t * TimestampBuffer,
                           u32 SizeOfTimestampBuffer,
                           u32 * NumPairsBuffer,
                           u32 SizeOfNumPairsBuffer);

nxStatus_t _NXFUNC nxReadState (
                           nxSessionRef_t SessionRef,
                           u32 StateID,
                           u32 StateSize,
                           void * StateValue,
                           nxStatus_t * Fault);

nxStatus_t _NXFUNC nxReadStateTimeTrigger (
                           nxSessionRef_t SessionRef,
                           f64 Timeout,
                           u32 StateSize,
                           void * StateValue);

nxStatus_t _NXFUNC nxWriteFrame (
                           nxSessionRef_t SessionRef,
                           void * Buffer,
                           u32 NumberOfBytesForFrames,
                           f64 Timeout);

nxStatus_t _NXFUNC nxWriteSignalSinglePoint (
                           nxSessionRef_t SessionRef,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer);

nxStatus_t _NXFUNC nxWriteState (
                           nxSessionRef_t SessionRef,
                           u32 StateID,
                           u32 StateSize,
                           void * StateValue);

nxStatus_t _NXFUNC nxWriteSignalWaveform (
                           nxSessionRef_t SessionRef,
                           f64 Timeout,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer);

nxStatus_t _NXFUNC nxWriteSignalXY (
                           nxSessionRef_t SessionRef,
                           f64 Timeout,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           nxTimestamp100ns_t * TimestampBuffer,
                           u32 SizeOfTimestampBuffer,
                           u32 * NumPairsBuffer,
                           u32 SizeOfNumPairsBuffer);

nxStatus_t _NXFUNC nxConvertFramesToSignalsSinglePoint (
                           nxSessionRef_t SessionRef,
                           void * FrameBuffer,
                           u32 NumberOfBytesForFrames,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           nxTimestamp100ns_t * TimestampBuffer,
                           u32 SizeOfTimestampBuffer);

nxStatus_t _NXFUNC nxConvertSignalsToFramesSinglePoint (
                           nxSessionRef_t SessionRef,
                           f64 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           void * Buffer,
                           u32 SizeOfBuffer,
                           u32 * NumberOfBytesReturned);

nxStatus_t _NXFUNC nxConvertFramesToByteArraySinglePoint (
                           nxSessionRef_t SessionRef,
                           void * FrameBuffer,
                           u32 NumberOfBytesForFrames,
                           u8 * ValueBuffer,
                           u32 SizeOfValueBuffer);

nxStatus_t _NXFUNC nxConvertByteArrayToFramesSinglePoint (
                           nxSessionRef_t SessionRef,
                           u8 * ValueBuffer,
                           u32 SizeOfValueBuffer,
                           void * Buffer,
                           u32 SizeOfBuffer,
                           u32 * NumberOfBytesReturned);

nxStatus_t _NXFUNC nxConvertTimestamp100nsTo1ns (
                           nxTimestamp100ns_t From,
                           nxTimestamp1ns_t * To);

nxStatus_t _NXFUNC nxConvertTimestamp1nsTo100ns (
                           nxTimestamp1ns_t From,
                           nxTimestamp100ns_t * To);


nxStatus_t _NXFUNC nxBlink (
                           nxSessionRef_t InterfaceRef,
                           u32 Modifier);

nxStatus_t _NXFUNC nxClear (
                           nxSessionRef_t SessionRef);

nxStatus_t _NXFUNC nxConnectTerminals (
                           nxSessionRef_t SessionRef,
                           const char * source,
                           const char * destination);


nxStatus_t _NXFUNC nxDisconnectTerminals (
                           nxSessionRef_t SessionRef,
                           const char * source,
                           const char * destination);

nxStatus_t _NXFUNC nxFlush (
                           nxSessionRef_t SessionRef);

nxStatus_t _NXFUNC nxStart (
                           nxSessionRef_t SessionRef,
                           u32 Scope);

nxStatus_t _NXFUNC nxStop (
                           nxSessionRef_t SessionRef,
                           u32 Scope);

void _NXFUNC nxStatusToString (
                           nxStatus_t Status,
                           u32 SizeofString,
                           char * StatusDescription);

nxStatus_t _NXFUNC nxSystemOpen (
                           nxSessionRef_t * SystemRef);

nxStatus_t _NXFUNC nxSystemClose (
                           nxSessionRef_t SystemRef);

nxStatus_t _NXFUNC nxWait (
                           nxSessionRef_t SessionRef,
                           u32 Condition,
                           u32 ParamIn,
                           f64 Timeout,
                           u32 * ParamOut);

nxStatus_t _NXFUNC nxFutureTimeTrigger (
                           nxSessionRef_t SessionRef,
                           nxTimestamp1ns_t When,
                           u32 Timescale);


/***********************************************************************
       F U N C T I O N   P R O T O T Y P E S  :  D A T A B A S E
***********************************************************************/

nxStatus_t _NXFUNC nxdbOpenDatabase (
                           const char * DatabaseName,
                           nxDatabaseRef_t * DatabaseRef);

nxStatus_t _NXFUNC nxdbCloseDatabase (
                           nxDatabaseRef_t DatabaseRef,
                           u32 CloseAllRefs);

nxStatus_t _NXFUNC nxdbCreateObject (
                           nxDatabaseRef_t ParentObjectRef,
                           u32 ObjectClass,
                           const char * ObjectName,
                           nxDatabaseRef_t * DbObjectRef);

nxStatus_t _NXFUNC nxdbFindObject (
                           nxDatabaseRef_t ParentObjectRef,
                           u32 ObjectClass,
                           const char * ObjectName,
                           nxDatabaseRef_t * DbObjectRef);

nxStatus_t _NXFUNC nxdbDeleteObject (
                           nxDatabaseRef_t DbObjectRef);

nxStatus_t _NXFUNC nxdbSaveDatabase (
                           nxDatabaseRef_t DatabaseRef,
                           const char * DbFilepath);

nxStatus_t _NXFUNC nxdbGetProperty (
                           nxDatabaseRef_t DbObjectRef,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

nxStatus_t _NXFUNC nxdbGetPropertySize (
                           nxDatabaseRef_t DbObjectRef,
                           u32 PropertyID,
                           u32 * PropertySize);

nxStatus_t _NXFUNC nxdbSetProperty (
                           nxDatabaseRef_t DbObjectRef,
                           u32 PropertyID,
                           u32 PropertySize,
                           void * PropertyValue);

/* The NI-XNET documentation does not describe the Mode parameter.
   The Mode parameter was added near release. It specifies the type of DBC attribute
   that you want to search for. In the v1.2 release there is only one value:
      nxGetDBCMode_Attribute (0)
   Other values will be supported in subsequent releases. */
nxStatus_t _NXFUNC nxdbGetDBCAttributeSize (
                           nxDatabaseRef_t DbObjectRef,
                           u32 Mode,
                           const char* AttributeName,
                           u32 *AttributeTextSize);

/* The NI-XNET documentation does not describe the Mode parameter.
   The Mode parameter was added near release. It specifies the type of DBC attribute
   that you want to search for. In the v1.2 release there is only one value:
      nxGetDBCMode_Attribute (0)
   Other values will be supported in subsequent releases. */
nxStatus_t _NXFUNC nxdbGetDBCAttribute (
                           nxDatabaseRef_t DbObjectRef,
                           u32 Mode,
                           const char* AttributeName,
                           u32 AttributeTextSize,
                           char* AttributeText,
                           u32 * IsDefault);

nxStatus_t _NXFUNC nxdbMerge (
                           nxDatabaseRef_t TargetClusterRef,
                           nxDatabaseRef_t SourceObjRef,
                           u32 CopyMode,
                           char *Prefix,
                           u32 WaitForComplete,
                           u32 *PercentComplete);


nxStatus_t _NXFUNC nxdbAddAlias (
                           const char * DatabaseAlias,
                           const char * DatabaseFilepath,
                           u32          DefaultBaudRate);

nxStatus_t _NXFUNC nxdbAddAlias64 (
                           const char * DatabaseAlias,
                           const char * DatabaseFilepath,
                           u64          DefaultBaudRate);

nxStatus_t _NXFUNC nxdbRemoveAlias (
                           const char * DatabaseAlias);

nxStatus_t _NXFUNC nxdbDeploy (
                           const char * IPAddress,
                           const char * DatabaseAlias,
                           u32 WaitForComplete,
                           u32 * PercentComplete);

nxStatus_t _NXFUNC nxdbUndeploy (
                           const char * IPAddress,
                           const char * DatabaseAlias);

nxStatus_t _NXFUNC nxdbGetDatabaseList (
                           const char * IPAddress,
                           u32 SizeofAliasBuffer,
                           char * AliasBuffer,
                           u32 SizeofFilepathBuffer,
                           char * FilepathBuffer,
                           u32 * NumberOfDatabases);

nxStatus_t _NXFUNC nxdbGetDatabaseListSizes (
                           const char * IPAddress,
                           u32 * SizeofAliasBuffer,
                           u32 * SizeofFilepathBuffer);

#endif // _NX_FUNCTION_EXPORT

#ifdef __cplusplus
   /* See top of header file.  */
   }
#endif // __cplusplus

#endif // ___nixnet_h___
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nxsocket.h sha256=8ebfc0711e9e596b515ca820e90dcd2163588e1495bbd21fa69bdc214ced2885 bytes=22896 -->
## FILE: imports/include/nxsocket.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nxsocket.h`
- sha256: `8ebfc0711e9e596b515ca820e90dcd2163588e1495bbd21fa69bdc214ced2885`
- bytes: 22896

````c
/*============================================================================*/
/*                 National Instruments / NI-XNET BSD Socket API              */
/*----------------------------------------------------------------------------*/
/*    Copyright (c) National Instruments 2019-2020.  All Rights Reserved.     */
/*----------------------------------------------------------------------------*/
/*                                                                            */
/* Title:       nxsocket.h                                                    */
/* Purpose:     Include file for NI-XNET BSD Socket API, including TCP/IP     */
/*              stack configuration                                           */
/*                                                                            */
/*============================================================================*/

#ifndef ___nxsocket_h___
#define ___nxsocket_h___

/*--------------------------------------------------------------------------*/
/*  Includes  */
/*--------------------------------------------------------------------------*/
#include <stddef.h>

/*--------------------------------------------------------------------------*/
/* nxsocket_errors.h contains all NI-XNET IP Stack error codes defined as   */
/* preprocessor constants                                                   */
/*--------------------------------------------------------------------------*/
#include "nxsocket_errors.h"

/****************************************************************************/
/*  Base type definitions                                                   */
/****************************************************************************/
#if defined(_MSC_VER)
   #if (_MSC_VER >= 1600)
      #include <stdint.h>
   #elif !defined(_STDINT_H_) && !defined(_STDINT_H) && !defined(_STDINT)
      typedef __int8           int8_t;
      typedef unsigned __int8  uint8_t;
      typedef __int16          int16_t;
      typedef unsigned __int16 uint16_t;
      typedef __int32          int32_t;
      typedef unsigned __int32 uint32_t;
      typedef __int64          int64_t;
      typedef unsigned __int64 uint64_t;
      #ifndef _INTPTR_T_DEFINED
         #if _WIN64
            typedef __int64 intptr_t;
         #else
            typedef __int32 intptr_t;
         #endif
         #define _INTPTR_T_DEFINED
      #endif
   #endif
#elif defined(_CVI_)
   #if (_CVI_ >= 910)
      /* If we're compiling using CVI, just use their C99 types. */
      #include <stdint.h>
   #else
      #error CVI Compiler is too old
   #endif
#elif defined(__GNUC__)
   #include <stdint.h>
#else
   #error Unsupported compiler
#endif

/* Needed for C++ to C (DLL) calls  */
#ifdef __cplusplus
   extern "C" {
#endif

/* Ensure consistent packing */
#pragma pack( push, 8 )

/* Function calling convention */
#if defined(_MSC_VER)
   #ifndef NI_CDECL
      #define NI_CDECL __cdecl
   #endif
#elif defined(__GNUC__)
   #ifndef NI_CDECL
      #define NI_CDECL
   #endif
#elif defined(_CVI_)
   #ifndef NI_CDECL
      #define NI_CDECL __cdecl
   #endif
#else
   #error Unsupported compiler
#endif


/****************************************************************************/
/*  IP Stack API                                                            */
/****************************************************************************/

/*--------------------------------------------------------------------------*/
/*  IP Stack defines                                                        */
/*--------------------------------------------------------------------------*/

/* nxIPSTACK_INFO_ID is passed to the infoID parameter of nxIpStackGetInfo.
* This identifies the struct version to return.
* If/when NI-XNET adds members to a struct, nxIPSTACK_INFO_ID will be
* incremented in this header. The NI-XNET driver will support older values,
* to ensure that applications using structs from a previous version
* work safely.
*/
#define nxIPSTACK_INFO_ID           1

/* For functions that take a millisecond timeout */
#define nxTIMEOUT_INFINITE (-1)

/* Link states */
#define nxOPERATIONAL_STATUS_DOWN           0
#define nxOPERATIONAL_STATUS_UP             1

#define nxINVALID_STACKREF ((nxIpStackRef_t)(0))

/* Format supported by nxIpStackGetAllStacksInfoStr */
#define nxIPSTACK_INFO_STR_FORMAT_JSON       0
#define nxIPSTACK_INFO_STR_FORMAT_TEXT       1

/*--------------------------------------------------------------------------*/
/*  IP Stack types                                                          */
/*--------------------------------------------------------------------------*/
typedef struct nxIpStackRef_t_struct* nxIpStackRef_t;

typedef struct _nxIPAddress_t {
      struct _nxIPAddress_t* nextIPAddress;  /* next address in list */
      uint32_t family;                       /* operational address family (nxAF_INET, nxAF_INET6) */
      char* address;                         /* operational address */
      char* netmask;                         /* operational netmask */
      uint32_t prefixLength;                 /* operational prefix length */
   } nxIPAddress_t;

typedef struct _nxGatewayAddress_t {
      struct _nxGatewayAddress_t* nextGatewayAddress; /* next gateway address in list */
      uint32_t family;                                /* address family (nxAF_INET, nxAF_INET6) */
      char* address;                                  /* gateway address */
   } nxGatewayAddress_t;

typedef struct _nxVirtualInterface_t {
      struct _nxVirtualInterface_t* nextVirtualInterface; /* next virtual interface in list */
      char* xnetInterfaceName;                            /* physical XNET interface used */
      char* vlanName;                                     /* name of the virtual interface */
      char* macAddress;                                   /* operational MAC address */
      uint32_t macMTU;                                    /* maximum size packet allowed */
      uint32_t operationalStatus;                         /* operational state of the link (nxOPERATIONAL_STATUS_UP/nxOPERATIONAL_STATUS_DOWN) */
      uint32_t ifIndex;                                   /* Unique identifier for this virtual interface */
      struct _nxIPAddress_t* firstIPAddress;              /* Linked list of the IP addresses in-use on this interface (or null) */
      struct _nxGatewayAddress_t* firstGatewayAddress;    /* Linked list of the gateway addresses in-use on this interface (or null) */
   } nxVirtualInterface_t;


/*--------------------------------------------------------------------------*/
/*  IP Stack functions  */
/*--------------------------------------------------------------------------*/

int32_t NI_CDECL nxIpStackCreate(const char* stackName, const char* config,
   nxIpStackRef_t* stackRef);
int32_t NI_CDECL nxIpStackOpen(const char* stackName, nxIpStackRef_t* stackRef);
int32_t NI_CDECL nxIpStackClear(nxIpStackRef_t stackRef);
int32_t NI_CDECL nxIpStackGetInfo(nxIpStackRef_t stackRef, uint32_t infoID,
   nxVirtualInterface_t** firstVirtualInterface);
int32_t NI_CDECL nxIpStackFreeInfo(nxVirtualInterface_t* firstVirtualInterface);
int32_t NI_CDECL nxIpStackGetAllStacksInfoStr(uint32_t formatType, char** info);
void NI_CDECL nxIpStackFreeAllStacksInfoStr(char* info);
int32_t NI_CDECL nxIpStackWaitForInterface(nxIpStackRef_t stackRef, const char* localInterface, int32_t timeoutMs);

/****************************************************************************/
/*  BSD-style Socket API                                                    */
/****************************************************************************/

/*--------------------------------------------------------------------------*/
/*  Socket defines                                                          */
/*--------------------------------------------------------------------------*/

#define nxINVALID_SOCKET            ((nxSOCKET)(-1))

/* Address families */
#define nxAF_UNSPEC                 0
#define nxAF_INET                   2
#define nxAF_INET6                  10

/* Protocol families */
#define nxPF_INET                   nxAF_INET
#define nxPF_INET6                  nxAF_INET6
#define nxPF_UNSPEC                 nxAF_UNSPEC

/* IP protocols */
#define nxIPPROTO_IP                0
#define nxIPPROTO_TCP               6
#define nxIPPROTO_UDP               8
#define nxIPPROTO_IPV6              12

/* IP address constants */
#define nxIPADDR_NONE               ((uint32_t)0xffffffffUL) /* 255.255.255.255 */
#define nxIPADDR_LOOPBACK           ((uint32_t)0x7f000001UL) /* 127.0.0.1 */
#define nxIPADDR_ANY                ((uint32_t)0x00000000UL) /* 0.0.0.0 */
#define nxIPADDR_BROADCAST          ((uint32_t)0xffffffffUL) /* 255.255.255.255 */
#define nxINADDR_NONE               nxIPADDR_NONE
#define nxINADDR_LOOPBACK           nxIPADDR_LOOPBACK
#define nxINADDR_ANY                nxIPADDR_ANY
#define nxINADDR_BROADCAST          nxIPADDR_BROADCAST
#define nxIN6ADDR_ANY_INIT          {}
#define nxINET_ADDRSTRLEN           16
#define nxINET6_ADDRSTRLEN          46

/* Socket protocol types (TCP is stream, UDP is dgram) */
#define nxSOCK_STREAM               1
#define nxSOCK_DGRAM                2

/* Level for socket option to apply to socket itself */
#define nxSOL_SOCKET                13     /* options for socket level */

/* Socket options (nxSOL_SOCKET) */
#define nxSO_RXDATA                 0x101  /* num bytes for next receive */
#define nxSO_RCVBUF                 0x102  /* receive buffer size */
#define nxSO_SNDBUF                 0x103  /* send buffer size */
#define nxSO_NONBLOCK               0x104  /* indicates/controls whether socket is non-blocking */
#define nxSO_BINDTODEVICE           0x105  /* binds the socket to a virtual interface by name */
#define nxSO_ERROR                  0x106  /* returns latest error on the socket */
#define nxSO_LINGER                 0x107  /* indicates/controls the linger option of a TCP socket */
#define nxSO_REUSEADDR              0x108  /* indicates/controls the reuse address option of a socket */

/* IPv4 options (nxIPPROTO_IP) */
#define nxIP_ADD_MEMBERSHIP         3
#define nxIP_DROP_MEMBERSHIP        4
#define nxIP_MULTICAST_IF           5
#define nxIP_MULTICAST_TTL          6

/* IPv6 options (nxIPPROTO_IPV6) */
#define nxIPV6_JOIN_GROUP           12
#define nxIPV6_LEAVE_GROUP          13
#define nxIPV6_ADD_MEMBERSHIP       nxIPV6_JOIN_GROUP
#define nxIPV6_DROP_MEMBERSHIP      nxIPV6_LEAVE_GROUP
#define nxIPV6_MULTICAST_IF         14
#define nxIPV6_MULTICAST_HOPS       15
#define nxIPV6_V6ONLY               16


/* TCP options (nxIPPROTO_TCP) */
#define nxTCP_NODELAY               0x01  /* don't delay send to coalesce packets */

/* Receive flags */
#define nxMSG_PEEK                  0x01  /* peek at message without reading */

/* nxshutdown how parameter */
#define nxSHUT_RD                   0
#define nxSHUT_WR                   1
#define nxSHUT_RDWR                 2

/* nxsockaddr_storage: maximum size and alignment, padding */
#define _nxSS_MAXSIZE               128
#define _nxSS_ALIGNSIZE             (sizeof (int64_t))
#define _nxSS_PAD1SIZE              (_nxSS_ALIGNSIZE - sizeof (uint16_t))
#define _nxSS_PAD2SIZE              (_nxSS_MAXSIZE - (sizeof (uint16_t) + \
                                    _nxSS_PAD1SIZE + _nxSS_ALIGNSIZE))

/* nxgetaddrinfo flags */
#define nxAI_PASSIVE       0x0001   /* returned socket address will be used in a bind() call */
#define nxAI_CANONNAME     0x0002   /* return canonical name in first ai_canonname */
#define nxAI_NUMERICHOST   0x0004   /* if specified, given node must be a numeric address */
#define nxAI_NUMERICSERV   0x0008   /* if specified, given service must be a numeric port */
#define nxAI_V4MAPPED      0x0010   /* if no matching ipv6 address is found, return an ipv4 mapped address */
#define nxAI_ALL           0x0020   /* if set with nxAI_V4MAPPED, return all ipv4 and ipv6 addresses */
#define nxAI_ADDRCONFIG    0x0040   /* if set, return ipv4 addresses only if a local ipv4 address is configured, likewise for ipv6 */
#define nxAI_LOCALQUERY    0x0080   /* only perform a local query for the DNS name */
#define nxAI_PREFER_V4     0x0100   /* if this flag is set and the query specifies nxAF_UNSPEC then perform A query first otherwise the resolver does AAAA query first */
#define nxAI_UNICAST_REPLY 0x0200   /* only relevant for mDNS. If this flag is set then the unicast reply bit will be set in questions to request the mDNS server unicasts its response */
#define nxAI_SHARED_RRSET  0x0400   /* only relevant for mDNS. If this flag is set it indicates there may be multiple mDNS responders so the client should attempt to process more than one response */
#define nxAI_BYPASS_CACHE  0x0800   /* causes the ip stack to bypass the cache when doing a name lookup */


/* nxgetnameinfo flags */
#define nxNI_NOFQDN        0x01     /* only return the nodename portion for local hosts */
#define nxNI_NUMERICHOST   0x02     /* return the numeric form of the host's address */
#define nxNI_NAMEREQD      0x04     /* error if the host's name is not in DNS */
#define nxNI_NUMERICSERV   0x08     /* return the numeric form of the service (port #) */
#define nxNI_DGRAM         0x10     /* service is a datagram (UDP) service */

/* fd_set macros
 *
 * Select uses arrays of nxSOCKETs.  These macros manipulate such
 * arrays. nxFD_SETSIZE may be defined by the user before including
 * this file if the default is not sufficient
 */
#ifndef nxFD_SETSIZE
#define nxFD_SETSIZE       64
#endif /* nxFD_SETSIZE */

#define nxFD_SET(fd, set) do { \
   uint32_t __i; \
   for (__i = 0; __i < ((set))->fd_count; __i++) { \
      if (((set))->fd_array[__i] == (fd)) { \
         break; \
      } \
   } \
   if (__i == ((set))->fd_count) { \
      if (((set))->fd_count < nxFD_SETSIZE) { \
         ((set))->fd_array[__i] = (fd); \
         ((set))->fd_count++; \
      } \
   } \
} while(0)

#define nxFD_CLR(fd, set) do { \
   uint32_t __i; \
   for (__i = 0; __i < ((set))->fd_count; __i++) { \
      if (((set))->fd_array[__i] == fd) { \
         while (__i < ((set))->fd_count-1) { \
            ((set))->fd_array[__i] = \
               ((set))->fd_array[__i+1]; \
            __i++; \
         } \
         ((set))->fd_count--; \
         break; \
      } \
   } \
} while(0)

#define nxFD_ZERO(set) (((set))->fd_count=0)

#define nxFD_ISSET(fd, set) nxfd_isset((nxSOCKET)(fd), (set))

/*--------------------------------------------------------------------------*/
/*  Socket types                                                            */
/*--------------------------------------------------------------------------*/
typedef intptr_t nxSOCKET;
typedef int32_t  nxsocklen_t;

/*--------------------------------------------------------------------------*/
/*  Socket structs                                                          */
/*--------------------------------------------------------------------------*/

/* Structure used to store IPv4 addresses (nxAF_INET) */
struct nxin_addr {
   uint32_t addr;
};

/* Structure used to store IPv6 addresses (nxAF_INET6) */
struct nxin6_addr {
   uint8_t  addr[16];                  /* IPv6 address */
};

/* Structure used to specify transport address and port for IPv4 (nxAF_INET) */
struct nxsockaddr_in {
   uint16_t             sin_family;    /* AF_INET                     */
   uint16_t             sin_port;      /* Port number                 */
   struct nxin_addr     sin_addr;      /* IPv4 address                */
   char                 sin_zero[8];   /* Reserved                    */
};

/* Structure used to specify transport address and port for IPv6 (nxAF_INET6) */
struct nxsockaddr_in6 {
   uint16_t             sin6_family;   /* AF_INET6                    */
   uint16_t             sin6_port;     /* Port number                 */
   uint32_t             sin6_flowinfo; /* IPv6 flow information       */
   struct nxin6_addr    sin6_addr;     /* IPv6 address                */
   uint32_t             sin6_scope_id; /* Scope ID                    */
};

/* Generic structure used to specify a transport address for any protocol.
*  NOTE: The sa_data member is not typically accessed directly. Instead,
*        the pointer is cast to/from the actual structure type for the
*        address family specified by sa_family.
*/
struct nxsockaddr {
   uint16_t             sa_family;
   char                 sa_data[16];   /* Opaque, see RFC 3493 */
};

/* Storage of family-independent sockaddr (see RFC 3493) */
struct nxsockaddr_storage {
   uint16_t            ss_family;     /* address family */
   /* Following fields are implementation-specific */
   char                __ss_pad1[_nxSS_PAD1SIZE]; /* 6 byte pad, this is to make implementation-specific pad up to alignment field that follows explicit in the data structure */
   int64_t             __ss_align;                /* field to force desired structure alignment */
   /* storage alignment */
   char                __ss_pad2[_nxSS_PAD2SIZE]; /* Padding to achieve desired size */
};

/* Structure used to add/join an IPv4 multicast group (nxIP_ADD_MEMBERSHIP/nxIP_DROP_MEMBERSHIP) */
struct nxip_mreq {
   struct nxin_addr     imr_multiaddr; /* IPv4 multicast address of group */
   struct nxin_addr     imr_interface; /* local IP address of interface */
};

/* Structure used to add/join an IPv6 multicast group (nxIPV6_JOIN_GROUP/nxIPV6_LEAVE_GROUP) */
struct nxipv6_mreq {
   struct nxin6_addr    ipv6mr_multiaddr; /* IPv6 multicast address */
   int32_t              ipv6mr_interface; /* interface index, or 0 to use first available */
};

/* Specifies a time value (used by nxselect) */
struct nxtimeval {
   int64_t              tv_sec;        /* seconds */
   int32_t              tv_usec;       /* microseconds */
};

/* Specifies a set of sockets (used by nxselect)
*  This structure should not be accessed directly, but rather via the nxFD_XXX macros
*/
struct nxfd_set {
   uint32_t             fd_count;
   nxSOCKET             fd_array[nxFD_SETSIZE];
};

/* Identifies an internet address (used by nxgetaddrinfo) */
struct nxaddrinfo {
   int32_t              ai_flags;      /* Options for nxgetaddrinfo */
   int32_t              ai_family;     /* Address family */
   int32_t              ai_socktype;   /* Socket type */
   int32_t              ai_protocol;   /* Protocol type */
   nxsocklen_t          ai_addrlen;    /* Length of ai_addr in bytes */
   struct nxsockaddr*   ai_addr;       /* The address of the host */
   char*                ai_canonname;  /* The canonical name for the host */
   struct nxaddrinfo*   ai_next;       /* Pointer to the next item in the linked list (or null) */
};

/* Structure used to specify how a TCP socket is closed (used with nxSO_LINGER) */
struct nxlinger {
    int l_onoff;    /* Linger option on or off */
    int l_linger;   /* Linger timeout value in seconds */
};

/*--------------------------------------------------------------------------*/
/*  Socket functions  */
/*--------------------------------------------------------------------------*/

nxSOCKET NI_CDECL nxsocket(nxIpStackRef_t stack_ref, int32_t domain, int32_t type, int32_t protocol);
int32_t NI_CDECL nxclose(nxSOCKET socket);
int32_t NI_CDECL nxbind(nxSOCKET socket, const struct nxsockaddr *name, nxsocklen_t namelen);
nxSOCKET NI_CDECL nxaccept(nxSOCKET socket, struct nxsockaddr *addr, nxsocklen_t *addrlen);
int32_t NI_CDECL nxconnect(nxSOCKET socket, const struct nxsockaddr *name, nxsocklen_t namelen);
int32_t NI_CDECL nxlisten(nxSOCKET socket, int32_t backlog);
int32_t NI_CDECL nxsendto(nxSOCKET socket, const void *dataptr, int32_t size, int32_t flags, const struct nxsockaddr *to, nxsocklen_t tolen);
int32_t NI_CDECL nxsend(nxSOCKET socket, const void *dataptr, int32_t size, int32_t flags);
int32_t NI_CDECL nxrecvfrom(nxSOCKET socket, void *mem, int32_t len, int32_t flags, struct nxsockaddr *from, nxsocklen_t *fromlen);
int32_t NI_CDECL nxrecv(nxSOCKET socket, void *mem, int32_t len, int32_t flags);
int32_t NI_CDECL nxsetsockopt(nxSOCKET socket, int32_t level, int32_t optname, const void *optval, nxsocklen_t optlen);
int32_t NI_CDECL nxgetsockopt(nxSOCKET socket, int32_t level, int32_t optname, void *optval, nxsocklen_t *optlen);
int32_t NI_CDECL nxgetsockname(nxSOCKET socket, struct nxsockaddr *addr, nxsocklen_t *addrlen);
int32_t NI_CDECL nxgetpeername(nxSOCKET socket, struct nxsockaddr *addr, nxsocklen_t *addrlen);
int32_t NI_CDECL nxshutdown(nxSOCKET socket, int32_t how);
int32_t NI_CDECL nxselect(int32_t nfds, struct nxfd_set *readfds, struct nxfd_set *writefds, struct nxfd_set *exceptfds, struct nxtimeval *timeout);
int32_t NI_CDECL nxfd_isset(nxSOCKET socket, struct nxfd_set *set);
int32_t NI_CDECL nxgetlasterrornum(void);
char* NI_CDECL nxgetlasterrorstr(char* buf, size_t buflen);
char* NI_CDECL nxstrerr_r(int errnum, char* buf, size_t buflen);

/*--------------------------------------------------------------------------*/
/*  Inet functions (address conversion)  */
/*--------------------------------------------------------------------------*/
uint32_t NI_CDECL nxinet_addr(nxIpStackRef_t stackRef, const char *cp);
char* NI_CDECL nxinet_ntoa(nxIpStackRef_t stackRef, struct nxin_addr in);
int NI_CDECL nxinet_aton(nxIpStackRef_t stackRef, const char *cp, struct nxin_addr *addr);
const char * NI_CDECL nxinet_ntop(nxIpStackRef_t stackRef, int32_t af, const void *src, char *dst, nxsocklen_t size);
int NI_CDECL nxinet_pton(nxIpStackRef_t stackRef, int32_t af, const char *src, void *dst);

/*--------------------------------------------------------------------------*/
/*  Name/Address Lookup functions                                           */
/*--------------------------------------------------------------------------*/
int32_t NI_CDECL nxgetaddrinfo(nxIpStackRef_t stackRef, const char *node, const char *service,
                               const struct nxaddrinfo *hints, struct nxaddrinfo **res);
void NI_CDECL nxfreeaddrinfo(struct nxaddrinfo *res);
int32_t NI_CDECL nxgetnameinfo(nxIpStackRef_t stackRef, const struct nxsockaddr *addr, nxsocklen_t addrlen,
                               char *host, nxsocklen_t hostlen,
                               char *serv, nxsocklen_t servlen, int32_t flags);

/* Restore packing */
#pragma pack( pop )

#ifdef __cplusplus
}
#endif

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nxsocket_errors.h sha256=b5ccd2555a7bf7c3117859db035c0ab295631c7b14c618cb30fca5cc2384c8a8 bytes=36634 -->
## FILE: imports/include/nxsocket_errors.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nxsocket_errors.h`
- sha256: `b5ccd2555a7bf7c3117859db035c0ab295631c7b14c618cb30fca5cc2384c8a8`
- bytes: 36634

````c
/*
   \file nxsocket_errors.h
   \brief NI-XNET BSD Socket API Errors

   Copyright (c) 2020 National Instruments Corporation.
   All rights reserved.
*/

#ifndef ___nxsocket_errors_h___
#define ___nxsocket_errors_h___


#define nxIpStackErrSuccess                                         ((int32_t)0x00000000)

/******************************************************************************
 * IP Stack Error Codes
 *****************************************************************************/

// nxIpStackErrInternalError: -13000 (0xFFFFCD38)
//
//  An internal error occurred in the NI-XNET IP Stack. Contact National
//  Instruments for support.
#define nxIpStackErrInternalError                                   ((int32_t)0xFFFFCD38)

// nxIpStackErrInvalidPropertyId: -13001 (0xFFFFCD37)
//
//  The property ID you specified is not valid.
#define nxIpStackErrInvalidPropertyId                               ((int32_t)0xFFFFCD37)

// nxIpStackErrInvalidPropertySize: -13002 (0xFFFFCD36)
//
//  The content of the property are bigger than the specified size. Be
//  sure to pass in a buffer large enough for the given property.
#define nxIpStackErrInvalidPropertySize                             ((int32_t)0xFFFFCD36)

// nxIpStackErrInvalidInterface: -13003 (0xFFFFCD35)
//
//  The specified interface name or index could not be found.
#define nxIpStackErrInvalidInterface                                ((int32_t)0xFFFFCD35)

// nxIpStackErrInvalidMtuSize: -13004 (0xFFFFCD34)
//
//  The specified MTU value is too large for the current device. Lower the
//  MTU to a value less than the maximum or set it to 0 to automatically
//  configure.
#define nxIpStackErrInvalidMtuSize                                  ((int32_t)0xFFFFCD34)

// nxIpStackErrStackIsStopping: -13005 (0xFFFFCD33)
//
//  The operation cannot be performed because the IP Stack is currently
//  shutting down.
#define nxIpStackErrStackIsStopping                                 ((int32_t)0xFFFFCD33)

// nxIpStackErrIpStackMismatch: -13006 (0xFFFFCD32)
//
//  The specified operation requires that all sockets are running on the
//  same IP Stack.
#define nxIpStackErrIpStackMismatch                                 ((int32_t)0xFFFFCD32)

// nxIpStackErrInvalidParameter: -13007 (0xFFFFCD31)
//
//  A parameter of the specified operation is either missing or otherwise
//  invalid. Refer to the NI-XNET IP Stack documentation regarding this
//  operation.
#define nxIpStackErrInvalidParameter                                ((int32_t)0xFFFFCD31)

// nxIpStackErrInvalidSocket: -13008 (0xFFFFCD30)
//
//  The specified socket could not be found.
#define nxIpStackErrInvalidSocket                                   ((int32_t)0xFFFFCD30)

// nxIpStackErrInvalidIpStack: -13009 (0xFFFFCD2F)
//
//  The specified IP Stack could not be found.
#define nxIpStackErrInvalidIpStack                                  ((int32_t)0xFFFFCD2F)

// nxIpStackErrDefaultIpStackInUse: -13010 (0xFFFFCD2E)
//
//  The default IP Stack cannot be disabled while a client is using it.
//  Disconnect all clients and retry the operation.
#define nxIpStackErrDefaultIpStackInUse                             ((int32_t)0xFFFFCD2E)

// nxIpStackErrVersionMismatch: -13011 (0xFFFFCD2D)
//
//  The IP Stack API in use does not support the version of the installed
//  driver.
#define nxIpStackErrVersionMismatch                                 ((int32_t)0xFFFFCD2D)

// nxIpStackErrBufferTooLarge: -13012 (0xFFFFCD2C)
//
//  The specified buffer is too large for the current operation. Reduce
//  the size of the buffer.
#define nxIpStackErrBufferTooLarge                                  ((int32_t)0xFFFFCD2C)

// nxIpStackErrLibraryCouldNotLoad: -13019 (0xFFFFCD25)
//
//  A shared library was unable to load a dependency. Uninstall NI-XNET
//  and then reinstall.
#define nxIpStackErrLibraryCouldNotLoad                             ((int32_t)0xFFFFCD25)

// nxIpStackErrStackAlreadyExists: -13020 (0xFFFFCD24)
//
//  An IP Stack with the specified name already exists. The name provided
//  to IP Stack create must be a system-wide unique name.
#define nxIpStackErrStackAlreadyExists                              ((int32_t)0xFFFFCD24)

// nxIpStackErrZeroSizedSocketOperationUnsupported: -13021 (0xFFFFCD23)
//
//  Sending or receiving 0 bytes over a socket is not supported.
#define nxIpStackErrZeroSizedSocketOperationUnsupported             ((int32_t)0xFFFFCD23)

// nxIpStackErrBufferInvalid: -13022 (0xFFFFCD22)
//
//  The provided buffer was either invalid or too small.
#define nxIpStackErrBufferInvalid                                   ((int32_t)0xFFFFCD22)

// nxIpStackErrErrorDescriptionTruncated: -13023 (0xFFFFCD21)
//
//  The error description was truncated because the provided buffer was
//  too small.
#define nxIpStackErrErrorDescriptionTruncated                       ((int32_t)0xFFFFCD21)

// nxIpStackErrTooManyInterfaces: -13024 (0xFFFFCD20)
//
//  The IP Stack does not support the number of virtual interfaces for
//  this configuration. Reduce the number of virtual interfaces or create
//  a second IP Stack instance.
#define nxIpStackErrTooManyInterfaces                               ((int32_t)0xFFFFCD20)

// nxIpStackErrInvalidStackName: -13025 (0xFFFFCD1F)
//
//  Ensure the stack name consists of valid characters and that the length
//  is less than or equal to 105 characters. Invalid characters include
//  forward slash (/), backslash (\), period (.), and tab (\t).
#define nxIpStackErrInvalidStackName                                ((int32_t)0xFFFFCD1F)

// nxIpStackErrTooManyIpAddresses: -13026 (0xFFFFCD1E)
//
//  The IP Stack does not support the number of IP addresses for this
//  configuration. Reduce the number of IP addresses or create a second IP
//  Stack instance.
#define nxIpStackErrTooManyIpAddresses                              ((int32_t)0xFFFFCD1E)

// nxIpStackErrInterfaceNameTooLong: -13027 (0xFFFFCD1D)
//
//  The VLAN Interface name must be 15 characters or less and unique
//  across the IP Stack. In the IP Stack configuration, ensure that VLAN
//  names are a maximum of 15 characters; and if a name is not provided
//  for a parent VLAN (therefore, automatically assigned by NI-XNET), MAC
//  names are limited to 10 characters.
#define nxIpStackErrInterfaceNameTooLong                            ((int32_t)0xFFFFCD1D)

// nxIpStackErrCannotCommunicateWithStack: -13028 (0xFFFFCD1C)
//
//  A general failure occurred while communicating with the IP Stack. This
//  can occur when OS resource limits are reached or if the IP Stack
//  encountered some other unexpected failure. Recreate the IP Stack and
//  reduce the overall load on the system. If the problem persists,
//  contact National Instruments for support.
#define nxIpStackErrCannotCommunicateWithStack                      ((int32_t)0xFFFFCD1C)

// nxIpStackErrTooManyRoutes: -13029 (0xFFFFCD1B)
//
//  The IP Stack does not support the number of routes necessary for this
//  configuration. Reduce the number of gateway addresses or other
//  configured routes.
#define nxIpStackErrTooManyRoutes                                   ((int32_t)0xFFFFCD1B)

// nxIpStackErrFormatNotSupported: -13030 (0xFFFFCD1A)
//
//  The specified format is not supported for this operation. Verify the
//  available formats in the API documentation.
#define nxIpStackErrFormatNotSupported                              ((int32_t)0xFFFFCD1A)

/******************************************************************************
 * JSON Parsing Error Codes
 *****************************************************************************/

// nxIpStackErrJsonSyntaxError: -13013 (0xFFFFCD2B)
//
//  A syntax error was encountered when parsing the IP Stack
//  configuration.
#define nxIpStackErrJsonSyntaxError                                 ((int32_t)0xFFFFCD2B)

// nxIpStackErrJsonInvalid: -13014 (0xFFFFCD2A)
//
//  An unsupported unicode sequence was encountered when parsing the IP
//  Stack configuration.
#define nxIpStackErrJsonInvalid                                     ((int32_t)0xFFFFCD2A)

// nxIpStackErrJsonGenericError: -13015 (0xFFFFCD29)
//
//  An unknown error occurred while parsing the IP Stack configuration.
#define nxIpStackErrJsonGenericError                                ((int32_t)0xFFFFCD29)

// nxIpStackErrJsonIncorrectDataType: -13016 (0xFFFFCD28)
//
//  An object in the IP Stack configuration has an unexpected data type.
//  Refer to the IP Stack configuration schema for the expected type.
#define nxIpStackErrJsonIncorrectDataType                           ((int32_t)0xFFFFCD28)

// nxIpStackErrJsonObjectMissingValue: -13017 (0xFFFFCD27)
//
//  An object in the IP Stack configuration is missing a required member.
//  Refer to the IP Stack configuration schema for the expected members.
#define nxIpStackErrJsonObjectMissingValue                          ((int32_t)0xFFFFCD27)

// nxIpStackErrJsonInvalidValue: -13018 (0xFFFFCD26)
//
//  An object in the IP Stack configuration does not match the expected
//  value. Refer to the IP Stack configuration schema for the expected
//  values.
#define nxIpStackErrJsonInvalidValue                                ((int32_t)0xFFFFCD26)

/******************************************************************************
 * POSIX Error Codes
 *****************************************************************************/

// nxIpStackErrOperationNotPermitted: -13801 (0xFFFFCA17)
//                           nxEPERM:  13801 (0x000035E9)
//
//  Operation not permitted
#define nxIpStackErrOperationNotPermitted                           ((int32_t)0xFFFFCA17)
#define nxEPERM                                                     ((int32_t)0x000035E9)

// nxIpStackErrFileNotFound: -13802 (0xFFFFCA16)
//                 nxENOENT:  13802 (0x000035EA)
//
//  No such file or directory
#define nxIpStackErrFileNotFound                                    ((int32_t)0xFFFFCA16)
#define nxENOENT                                                    ((int32_t)0x000035EA)

// nxIpStackErrNoSuchProcess: -13803 (0xFFFFCA15)
//                   nxESRCH:  13803 (0x000035EB)
//
//  No such process
#define nxIpStackErrNoSuchProcess                                   ((int32_t)0xFFFFCA15)
#define nxESRCH                                                     ((int32_t)0x000035EB)

// nxIpStackErrInterruptedCall: -13804 (0xFFFFCA14)
//                     nxEINTR:  13804 (0x000035EC)
//
//  Interrupted system call
#define nxIpStackErrInterruptedCall                                 ((int32_t)0xFFFFCA14)
#define nxEINTR                                                     ((int32_t)0x000035EC)

// nxIpStackErrIOError: -13805 (0xFFFFCA13)
//               nxEIO:  13805 (0x000035ED)
//
//  I/O Error
#define nxIpStackErrIOError                                         ((int32_t)0xFFFFCA13)
#define nxEIO                                                       ((int32_t)0x000035ED)

// nxIpStackErrNoSuchDeviceOrAddress: -13806 (0xFFFFCA12)
//                           nxENXIO:  13806 (0x000035EE)
//
//  No such device or address
#define nxIpStackErrNoSuchDeviceOrAddress                           ((int32_t)0xFFFFCA12)
#define nxENXIO                                                     ((int32_t)0x000035EE)

// nxIpStackErrArgumentListTooLong: -13807 (0xFFFFCA11)
//                         nxE2BIG:  13807 (0x000035EF)
//
//  Argument list too long
#define nxIpStackErrArgumentListTooLong                             ((int32_t)0xFFFFCA11)
#define nxE2BIG                                                     ((int32_t)0x000035EF)

// nxIpStackErrExecFormatError: -13808 (0xFFFFCA10)
//                   nxENOEXEC:  13808 (0x000035F0)
//
//  Exec format error
#define nxIpStackErrExecFormatError                                 ((int32_t)0xFFFFCA10)
#define nxENOEXEC                                                   ((int32_t)0x000035F0)

// nxIpStackErrBadFile: -13809 (0xFFFFCA0F)
//             nxEBADF:  13809 (0x000035F1)
//
//  Bad file number
#define nxIpStackErrBadFile                                         ((int32_t)0xFFFFCA0F)
#define nxEBADF                                                     ((int32_t)0x000035F1)

// nxIpStackErrNoChildren: -13810 (0xFFFFCA0E)
//               nxECHILD:  13810 (0x000035F2)
//
//  No child processes
#define nxIpStackErrNoChildren                                      ((int32_t)0xFFFFCA0E)
#define nxECHILD                                                    ((int32_t)0x000035F2)

// nxIpStackErrTryAgain: -13811 (0xFFFFCA0D)
//             nxEAGAIN:  13811 (0x000035F3)
//
//  Try again
#define nxIpStackErrTryAgain                                        ((int32_t)0xFFFFCA0D)
#define nxEAGAIN                                                    ((int32_t)0x000035F3)

// nxIpStackErrMemoryFull: -13812 (0xFFFFCA0C)
//               nxENOMEM:  13812 (0x000035F4)
//
//  Out of memory
#define nxIpStackErrMemoryFull                                      ((int32_t)0xFFFFCA0C)
#define nxENOMEM                                                    ((int32_t)0x000035F4)

// nxIpStackErrPermissionDenied: -13813 (0xFFFFCA0B)
//                     nxEACCES:  13813 (0x000035F5)
//
//  Permission denied
#define nxIpStackErrPermissionDenied                                ((int32_t)0xFFFFCA0B)
#define nxEACCES                                                    ((int32_t)0x000035F5)

// nxIpStackErrBadPointer: -13814 (0xFFFFCA0A)
//               nxEFAULT:  13814 (0x000035F6)
//
//  Bad address
#define nxIpStackErrBadPointer                                      ((int32_t)0xFFFFCA0A)
#define nxEFAULT                                                    ((int32_t)0x000035F6)

// nxIpStackErrBlockDeviceRequired: -13815 (0xFFFFCA09)
//                       nxENOTBLK:  13815 (0x000035F7)
//
//  Block device required
#define nxIpStackErrBlockDeviceRequired                             ((int32_t)0xFFFFCA09)
#define nxENOTBLK                                                   ((int32_t)0x000035F7)

// nxIpStackErrResourceBusy: -13816 (0xFFFFCA08)
//                  nxEBUSY:  13816 (0x000035F8)
//
//  Device or resource busy
#define nxIpStackErrResourceBusy                                    ((int32_t)0xFFFFCA08)
#define nxEBUSY                                                     ((int32_t)0x000035F8)

// nxIpStackErrFileExists: -13817 (0xFFFFCA07)
//               nxEEXIST:  13817 (0x000035F9)
//
//  File exists
#define nxIpStackErrFileExists                                      ((int32_t)0xFFFFCA07)
#define nxEEXIST                                                    ((int32_t)0x000035F9)

// nxIpStackErrCrossDeviceLink: -13818 (0xFFFFCA06)
//                     nxEXDEV:  13818 (0x000035FA)
//
//  Cross-device link
#define nxIpStackErrCrossDeviceLink                                 ((int32_t)0xFFFFCA06)
#define nxEXDEV                                                     ((int32_t)0x000035FA)

// nxIpStackErrNoSuchDevice: -13819 (0xFFFFCA05)
//                 nxENODEV:  13819 (0x000035FB)
//
//  No such device
#define nxIpStackErrNoSuchDevice                                    ((int32_t)0xFFFFCA05)
#define nxENODEV                                                    ((int32_t)0x000035FB)

// nxIpStackErrNotADirectory: -13820 (0xFFFFCA04)
//                 nxENOTDIR:  13820 (0x000035FC)
//
//  Not a directory
#define nxIpStackErrNotADirectory                                   ((int32_t)0xFFFFCA04)
#define nxENOTDIR                                                   ((int32_t)0x000035FC)

// nxIpStackErrIsADirectory: -13821 (0xFFFFCA03)
//                 nxEISDIR:  13821 (0x000035FD)
//
//  Is a directory
#define nxIpStackErrIsADirectory                                    ((int32_t)0xFFFFCA03)
#define nxEISDIR                                                    ((int32_t)0x000035FD)

// nxIpStackErrInvalidArgument: -13822 (0xFFFFCA02)
//                    nxEINVAL:  13822 (0x000035FE)
//
//  Invalid argument
#define nxIpStackErrInvalidArgument                                 ((int32_t)0xFFFFCA02)
#define nxEINVAL                                                    ((int32_t)0x000035FE)

// nxIpStackErrFileTableOverflow: -13823 (0xFFFFCA01)
//                      nxENFILE:  13823 (0x000035FF)
//
//  File table overflow
#define nxIpStackErrFileTableOverflow                               ((int32_t)0xFFFFCA01)
#define nxENFILE                                                    ((int32_t)0x000035FF)

// nxIpStackErrTooManyOpenFiles: -13824 (0xFFFFCA00)
//                     nxEMFILE:  13824 (0x00003600)
//
//  Too many open files
#define nxIpStackErrTooManyOpenFiles                                ((int32_t)0xFFFFCA00)
#define nxEMFILE                                                    ((int32_t)0x00003600)

// nxIpStackErrNoTTY: -13825 (0xFFFFC9FF)
//          nxENOTTY:  13825 (0x00003601)
//
//  Not a typewriter
#define nxIpStackErrNoTTY                                           ((int32_t)0xFFFFC9FF)
#define nxENOTTY                                                    ((int32_t)0x00003601)

// nxIpStackErrTextFileBusy: -13826 (0xFFFFC9FE)
//                nxETXTBSY:  13826 (0x00003602)
//
//  Text file busy
#define nxIpStackErrTextFileBusy                                    ((int32_t)0xFFFFC9FE)
#define nxETXTBSY                                                   ((int32_t)0x00003602)

// nxIpStackErrFileTooLarge: -13827 (0xFFFFC9FD)
//                  nxEFBIG:  13827 (0x00003603)
//
//  File too large
#define nxIpStackErrFileTooLarge                                    ((int32_t)0xFFFFC9FD)
#define nxEFBIG                                                     ((int32_t)0x00003603)

// nxIpStackErrNoSpace: -13828 (0xFFFFC9FC)
//            nxENOSPC:  13828 (0x00003604)
//
//  No space left on device
#define nxIpStackErrNoSpace                                         ((int32_t)0xFFFFC9FC)
#define nxENOSPC                                                    ((int32_t)0x00003604)

// nxIpStackErrIllegalSeek: -13829 (0xFFFFC9FB)
//                nxESPIPE:  13829 (0x00003605)
//
//  Illegal seek
#define nxIpStackErrIllegalSeek                                     ((int32_t)0xFFFFC9FB)
#define nxESPIPE                                                    ((int32_t)0x00003605)

// nxIpStackErrTooManyLinks: -13830 (0xFFFFC9FA)
//                 nxEMLINK:  13830 (0x00003606)
//
//  Too many links
#define nxIpStackErrTooManyLinks                                    ((int32_t)0xFFFFC9FA)
#define nxEMLINK                                                    ((int32_t)0x00003606)

// nxIpStackErrBrokenPipe: -13831 (0xFFFFC9F9)
//                nxEPIPE:  13831 (0x00003607)
//
//  Broken pipe
#define nxIpStackErrBrokenPipe                                      ((int32_t)0xFFFFC9F9)
#define nxEPIPE                                                     ((int32_t)0x00003607)

// nxIpStackErrOutOfDomain: -13832 (0xFFFFC9F8)
//                  nxEDOM:  13832 (0x00003608)
//
//  Math argument out of domain of func
#define nxIpStackErrOutOfDomain                                     ((int32_t)0xFFFFC9F8)
#define nxEDOM                                                      ((int32_t)0x00003608)

// nxIpStackErrNotRepresentable: -13833 (0xFFFFC9F7)
//                     nxERANGE:  13833 (0x00003609)
//
//  Math result not representable
#define nxIpStackErrNotRepresentable                                ((int32_t)0xFFFFC9F7)
#define nxERANGE                                                    ((int32_t)0x00003609)

// nxIpStackErrNoMessage: -13834 (0xFFFFC9F6)
//              nxENOMSG:  13834 (0x0000360A)
//
//  No message of desired type
#define nxIpStackErrNoMessage                                       ((int32_t)0xFFFFC9F6)
#define nxENOMSG                                                    ((int32_t)0x0000360A)

// nxIpStackErrIdentifierRemoved: -13835 (0xFFFFC9F5)
//                       nxEIDRM:  13835 (0x0000360B)
//
//  Identifier removed
#define nxIpStackErrIdentifierRemoved                               ((int32_t)0xFFFFC9F5)
#define nxEIDRM                                                     ((int32_t)0x0000360B)

// nxIpStackErrWouldDeadlock: -13836 (0xFFFFC9F4)
//               nxEDEADLOCK:  13836 (0x0000360C)
//
//  Resource deadlock would occur
#define nxIpStackErrWouldDeadlock                                   ((int32_t)0xFFFFC9F4)
#define nxEDEADLOCK                                                 ((int32_t)0x0000360C)

// nxIpStackErrWouldBlock: -13837 (0xFFFFC9F3)
//          nxEWOULDBLOCK:  13837 (0x0000360D)
//
//  Operation would block
#define nxIpStackErrWouldBlock                                      ((int32_t)0xFFFFC9F3)
#define nxEWOULDBLOCK                                               ((int32_t)0x0000360D)

// nxIpStackErrNowInProgress: -13838 (0xFFFFC9F2)
//             nxEINPROGRESS:  13838 (0x0000360E)
//
//  Operation now in progress
#define nxIpStackErrNowInProgress                                   ((int32_t)0xFFFFC9F2)
#define nxEINPROGRESS                                               ((int32_t)0x0000360E)

// nxIpStackErrAlreadyInProgress: -13839 (0xFFFFC9F1)
//                    nxEALREADY:  13839 (0x0000360F)
//
//  Operation already in progress
#define nxIpStackErrAlreadyInProgress                               ((int32_t)0xFFFFC9F1)
#define nxEALREADY                                                  ((int32_t)0x0000360F)

// nxIpStackErrNotSock: -13840 (0xFFFFC9F0)
//          nxENOTSOCK:  13840 (0x00003610)
//
//  Socket operation on non-socket
#define nxIpStackErrNotSock                                         ((int32_t)0xFFFFC9F0)
#define nxENOTSOCK                                                  ((int32_t)0x00003610)

// nxIpStackErrDestAddrRequired: -13841 (0xFFFFC9EF)
//               nxEDESTADDRREQ:  13841 (0x00003611)
//
//  Destination address required
#define nxIpStackErrDestAddrRequired                                ((int32_t)0xFFFFC9EF)
#define nxEDESTADDRREQ                                              ((int32_t)0x00003611)

// nxIpStackErrMessageSize: -13842 (0xFFFFC9EE)
//              nxEMSGSIZE:  13842 (0x00003612)
//
//  Message too long
#define nxIpStackErrMessageSize                                     ((int32_t)0xFFFFC9EE)
#define nxEMSGSIZE                                                  ((int32_t)0x00003612)

// nxIpStackErrWrongProtocol: -13843 (0xFFFFC9ED)
//              nxEPROTOTYPE:  13843 (0x00003613)
//
//  Protocol wrong type for socket
#define nxIpStackErrWrongProtocol                                   ((int32_t)0xFFFFC9ED)
#define nxEPROTOTYPE                                                ((int32_t)0x00003613)

// nxIpStackErrProtocolNotAvail: -13844 (0xFFFFC9EC)
//                nxENOPROTOOPT:  13844 (0x00003614)
//
//  Protocol not available
#define nxIpStackErrProtocolNotAvail                                ((int32_t)0xFFFFC9EC)
#define nxENOPROTOOPT                                               ((int32_t)0x00003614)

// nxIpStackErrProtocolNotSupported: -13845 (0xFFFFC9EB)
//                nxEPROTONOSUPPORT:  13845 (0x00003615)
//
//  Protocol not supported
#define nxIpStackErrProtocolNotSupported                            ((int32_t)0xFFFFC9EB)
#define nxEPROTONOSUPPORT                                           ((int32_t)0x00003615)

// nxIpStackErrSocketTypeNotSupported: -13846 (0xFFFFC9EA)
//                  nxESOCKTNOSUPPORT:  13846 (0x00003616)
//
//  Socket type not supported
#define nxIpStackErrSocketTypeNotSupported                          ((int32_t)0xFFFFC9EA)
#define nxESOCKTNOSUPPORT                                           ((int32_t)0x00003616)

// nxIpStackErrOpNotSupportedOnTransport: -13847 (0xFFFFC9E9)
//                          nxEOPNOTSUPP:  13847 (0x00003617)
//
//  Operation not supported on transport endpoint
#define nxIpStackErrOpNotSupportedOnTransport                       ((int32_t)0xFFFFC9E9)
#define nxEOPNOTSUPP                                                ((int32_t)0x00003617)

// nxIpStackErrAddressFamilyNotSupported: -13848 (0xFFFFC9E8)
//                        nxEAFNOSUPPORT:  13848 (0x00003618)
//
//  Address family not supported by protocol
#define nxIpStackErrAddressFamilyNotSupported                       ((int32_t)0xFFFFC9E8)
#define nxEAFNOSUPPORT                                              ((int32_t)0x00003618)

// nxIpStackErrAddressInUse: -13849 (0xFFFFC9E7)
//             nxEADDRINUSE:  13849 (0x00003619)
//
//  Address already in use
#define nxIpStackErrAddressInUse                                    ((int32_t)0xFFFFC9E7)
#define nxEADDRINUSE                                                ((int32_t)0x00003619)

// nxIpStackErrAddressNotAvail: -13850 (0xFFFFC9E6)
//             nxEADDRNOTAVAIL:  13850 (0x0000361A)
//
//  Cannot assign requested address
#define nxIpStackErrAddressNotAvail                                 ((int32_t)0xFFFFC9E6)
#define nxEADDRNOTAVAIL                                             ((int32_t)0x0000361A)

// nxIpStackErrNetworkDown: -13851 (0xFFFFC9E5)
//              nxENETDOWN:  13851 (0x0000361B)
//
//  Network is down
#define nxIpStackErrNetworkDown                                     ((int32_t)0xFFFFC9E5)
#define nxENETDOWN                                                  ((int32_t)0x0000361B)

// nxIpStackErrNetworkUnreachable: -13852 (0xFFFFC9E4)
//                  nxENETUNREACH:  13852 (0x0000361C)
//
//  Network is unreachable
#define nxIpStackErrNetworkUnreachable                              ((int32_t)0xFFFFC9E4)
#define nxENETUNREACH                                               ((int32_t)0x0000361C)

// nxIpStackErrNetworkReset: -13853 (0xFFFFC9E3)
//              nxENETRESET:  13853 (0x0000361D)
//
//  Network dropped connection because of reset
#define nxIpStackErrNetworkReset                                    ((int32_t)0xFFFFC9E3)
#define nxENETRESET                                                 ((int32_t)0x0000361D)

// nxIpStackErrConnectionAborted: -13854 (0xFFFFC9E2)
//                nxECONNABORTED:  13854 (0x0000361E)
//
//  Software caused connection abort
#define nxIpStackErrConnectionAborted                               ((int32_t)0xFFFFC9E2)
#define nxECONNABORTED                                              ((int32_t)0x0000361E)

// nxIpStackErrConnectionReset: -13855 (0xFFFFC9E1)
//                nxECONNRESET:  13855 (0x0000361F)
//
//  Connection reset by peer
#define nxIpStackErrConnectionReset                                 ((int32_t)0xFFFFC9E1)
#define nxECONNRESET                                                ((int32_t)0x0000361F)

// nxIpStackErrNoBuffers: -13856 (0xFFFFC9E0)
//             nxENOBUFS:  13856 (0x00003620)
//
//  No buffer space available
#define nxIpStackErrNoBuffers                                       ((int32_t)0xFFFFC9E0)
#define nxENOBUFS                                                   ((int32_t)0x00003620)

// nxIpStackErrAlreadyConnected: -13857 (0xFFFFC9DF)
//                    nxEISCONN:  13857 (0x00003621)
//
//  Transport endpoint is already connected
#define nxIpStackErrAlreadyConnected                                ((int32_t)0xFFFFC9DF)
#define nxEISCONN                                                   ((int32_t)0x00003621)

// nxIpStackErrNotConnected: -13858 (0xFFFFC9DE)
//               nxENOTCONN:  13858 (0x00003622)
//
//  Transport endpoint is not connected
#define nxIpStackErrNotConnected                                    ((int32_t)0xFFFFC9DE)
#define nxENOTCONN                                                  ((int32_t)0x00003622)

// nxIpStackErrTransportShutdown: -13859 (0xFFFFC9DD)
//                   nxESHUTDOWN:  13859 (0x00003623)
//
//  Cannot send after transport endpoint shutdown
#define nxIpStackErrTransportShutdown                               ((int32_t)0xFFFFC9DD)
#define nxESHUTDOWN                                                 ((int32_t)0x00003623)

// nxIpStackErrTimeout: -13860 (0xFFFFC9DC)
//         nxETIMEDOUT:  13860 (0x00003624)
//
//  Operation timed out
#define nxIpStackErrTimeout                                         ((int32_t)0xFFFFC9DC)
#define nxETIMEDOUT                                                 ((int32_t)0x00003624)

// nxIpStackErrConnectionRefused: -13861 (0xFFFFC9DB)
//                nxECONNREFUSED:  13861 (0x00003625)
//
//  Connection refused
#define nxIpStackErrConnectionRefused                               ((int32_t)0xFFFFC9DB)
#define nxECONNREFUSED                                              ((int32_t)0x00003625)

// nxIpStackErrProtocolFamilyNotSupported: -13862 (0xFFFFC9DA)
//                         nxEPFNOSUPPORT:  13862 (0x00003626)
//
//  Protocol family not supported
#define nxIpStackErrProtocolFamilyNotSupported                      ((int32_t)0xFFFFC9DA)
#define nxEPFNOSUPPORT                                              ((int32_t)0x00003626)

// nxIpStackErrHostDown: -13863 (0xFFFFC9D9)
//          nxEHOSTDOWN:  13863 (0x00003627)
//
//  Host is down
#define nxIpStackErrHostDown                                        ((int32_t)0xFFFFC9D9)
#define nxEHOSTDOWN                                                 ((int32_t)0x00003627)

// nxIpStackErrHostUnreachable: -13864 (0xFFFFC9D8)
//              nxEHOSTUNREACH:  13864 (0x00003628)
//
//  No route to host
#define nxIpStackErrHostUnreachable                                 ((int32_t)0xFFFFC9D8)
#define nxEHOSTUNREACH                                              ((int32_t)0x00003628)

// nxIpStackErrNoUrgentData: -13865 (0xFFFFC9D7)
//          nxENOURGENTDATA:  13865 (0x00003629)
//
//  No high priority data are available
#define nxIpStackErrNoUrgentData                                    ((int32_t)0xFFFFC9D7)
#define nxENOURGENTDATA                                             ((int32_t)0x00003629)

// nxIpStackErrNoOOBData: -13866 (0xFFFFC9D6)
//          nxENOOOBDATA:  13866 (0x0000362A)
//
//  No out of band data available
#define nxIpStackErrNoOOBData                                       ((int32_t)0xFFFFC9D6)
#define nxENOOOBDATA                                                ((int32_t)0x0000362A)

// nxIpStackErrTooManyReferences: -13867 (0xFFFFC9D5)
//                nxETOOMANYREFS:  13867 (0x0000362B)
//
//  Too many references: cannot splice
#define nxIpStackErrTooManyReferences                               ((int32_t)0xFFFFC9D5)
#define nxETOOMANYREFS                                              ((int32_t)0x0000362B)

// nxIpStackErrProtocolDriverUnattached: -13868 (0xFFFFC9D4)
//                            nxEUNATCH:  13868 (0x0000362C)
//
//  Protocol driver not attached
#define nxIpStackErrProtocolDriverUnattached                        ((int32_t)0xFFFFC9D4)
#define nxEUNATCH                                                   ((int32_t)0x0000362C)

// nxIpStackErrLinkNumRange: -13869 (0xFFFFC9D3)
//                 nxELNRNG:  13869 (0x0000362D)
//
//  Link number out of range
#define nxIpStackErrLinkNumRange                                    ((int32_t)0xFFFFC9D3)
#define nxELNRNG                                                    ((int32_t)0x0000362D)

// nxIpStackErrTryLookupAgain: -13870 (0xFFFFC9D2)
//                nxEAI_AGAIN:  13870 (0x0000362E)
//
//  The name could not be resolved at this time. Try again later.
#define nxIpStackErrTryLookupAgain                                  ((int32_t)0xFFFFC9D2)
#define nxEAI_AGAIN                                                 ((int32_t)0x0000362E)

// nxIpStackErrBadFlags: -13871 (0xFFFFC9D1)
//       nxEAI_BADFLAGS:  13871 (0x0000362F)
//
//  The flags argument has an invalid value.
#define nxIpStackErrBadFlags                                        ((int32_t)0xFFFFC9D1)
#define nxEAI_BADFLAGS                                              ((int32_t)0x0000362F)

// nxIpStackErrNoSocketArg: -13872 (0xFFFFC9D0)
//          nxEAI_NOSOCKET:  13872 (0x00003630)
//
//  The sockaddr argument has an invalid value.
#define nxIpStackErrNoSocketArg                                     ((int32_t)0xFFFFC9D0)
#define nxEAI_NOSOCKET                                              ((int32_t)0x00003630)

// nxIpStackErrFamily: -13873 (0xFFFFC9CF)
//       nxEAI_FAMILY:  13873 (0x00003631)
//
//  The requested address family is not supported.
#define nxIpStackErrFamily                                          ((int32_t)0xFFFFC9CF)
#define nxEAI_FAMILY                                                ((int32_t)0x00003631)

// nxIpStackErrAddrinfoMemoryFull: -13874 (0xFFFFC9CE)
//                   nxEAI_MEMORY:  13874 (0x00003632)
//
//  Memory is full
#define nxIpStackErrAddrinfoMemoryFull                              ((int32_t)0xFFFFC9CE)
#define nxEAI_MEMORY                                                ((int32_t)0x00003632)

// nxIpStackErrNameNotResolved: -13875 (0xFFFFC9CD)
//                nxEAI_NONAME:  13875 (0x00003633)
//
//  getaddrinfo: The node or service is not known; or both node and
//  service are NULL; or AI_NUMERICSERV was specified in hints.ai_flags
//  and service was not a numeric port number string. getnameinfo: The
//  name does not resolve for the supplied arguments. NI_NAMEREQD is set
//  and the host's name cannot be located, or neither hostname nor service
//  name were requested.
#define nxIpStackErrNameNotResolved                                 ((int32_t)0xFFFFC9CD)
#define nxEAI_NONAME                                                ((int32_t)0x00003633)

// nxIpStackErrServiceNotAvail: -13876 (0xFFFFC9CC)
//               nxEAI_SERVICE:  13876 (0x00003634)
//
//  The requested service is not available for the requested socket type.
//  It may be available through another socket type.
#define nxIpStackErrServiceNotAvail                                 ((int32_t)0xFFFFC9CC)
#define nxEAI_SERVICE                                               ((int32_t)0x00003634)

// nxIpStackErrAddrinfoSocketTypeNotSupported: -13877 (0xFFFFC9CB)
//                             nxEAI_SOCKTYPE:  13877 (0x00003635)
//
//  The requested socket type is not supported. This could occur if
//  hints.ai_socktype and hints.ai_protocol are inconsistent.
#define nxIpStackErrAddrinfoSocketTypeNotSupported                  ((int32_t)0xFFFFC9CB)
#define nxEAI_SOCKTYPE                                              ((int32_t)0x00003635)

// nxIpStackErrAddrinfoBufferOverflow: -13878 (0xFFFFC9CA)
//                     nxEAI_OVERFLOW:  13878 (0x00003636)
//
//  The buffer pointed to by host or serv was too small.
#define nxIpStackErrAddrinfoBufferOverflow                          ((int32_t)0xFFFFC9CA)
#define nxEAI_OVERFLOW                                              ((int32_t)0x00003636)

// nxIpStackErrOperationFailed: -13879 (0xFFFFC9C9)
//                  nxEAI_FAIL:  13879 (0x00003637)
//
//  A nonrecoverable error occurred.
#define nxIpStackErrOperationFailed                                 ((int32_t)0xFFFFC9C9)
#define nxEAI_FAIL                                                  ((int32_t)0x00003637)

// nxIpStackErrSystemError: -13880 (0xFFFFC9C8)
//            nxEAI_SYSTEM:  13880 (0x00003638)
//
//  A system error occurred.
#define nxIpStackErrSystemError                                     ((int32_t)0xFFFFC9C8)
#define nxEAI_SYSTEM                                                ((int32_t)0x00003638)

// nxIpStackErrNoKnownAddrs: -13881 (0xFFFFC9C7)
//             nxEAI_NODATA:  13881 (0x00003639)
//
//  The specified network host exists, but does not have any network
//  addresses defined.
#define nxIpStackErrNoKnownAddrs                                    ((int32_t)0xFFFFC9C7)
#define nxEAI_NODATA                                                ((int32_t)0x00003639)

// nxIpStackErrDNSNotAvailable: -13882 (0xFFFFC9C6)
//        nxRSLV_NOT_AVAILABLE:  13882 (0x0000363A)
//
//  DNS resolver is disabled.
#define nxIpStackErrDNSNotAvailable                                 ((int32_t)0xFFFFC9C6)
#define nxRSLV_NOT_AVAILABLE                                        ((int32_t)0x0000363A)

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/TerminalAdaptorTypes.h sha256=56451312e96a9abc9831121efe4052940d82e3e5667ad6867bb35743925d1909 bytes=2171 -->
## FILE: imports/include/TerminalAdaptorTypes.h

- repository: `ni/grpc-device`
- source_path: `imports/include/TerminalAdaptorTypes.h`
- sha256: `56451312e96a9abc9831121efe4052940d82e3e5667ad6867bb35743925d1909`
- bytes: 2171

````c
#ifndef NIMXLC_TERMINALADAPTORTYPES_H_
#define NIMXLC_TERMINALADAPTORTYPES_H_

#include <nierr_Status.h>

/*
  This macro defines opaque handle types that have a little more type-safety
  than void pointers.  These will always be reinterpret_cast'd to the actual
  type internally.

  Although these opaque types are implemented using a pointer, NULL may be a
  valid value.
 */
#define NIMXLCAPI_DEFINE_OPAQUE_TYPE(name) \
   struct undefined_ ## name; \
   typedef struct undefined_ ## name* name

/** A handle to a Routing Adaptor session */
NIMXLCAPI_DEFINE_OPAQUE_TYPE(nimxlc_Session);

/** A handle to a container with a list of devices */
NIMXLCAPI_DEFINE_OPAQUE_TYPE(nimxlc_DeviceContainer);

/** A handle to an iterator for a nimxlc_DeviceContainer */
NIMXLCAPI_DEFINE_OPAQUE_TYPE(nimxlc_DeviceIterator);

/** A handle to a container with a list of terminals */
NIMXLCAPI_DEFINE_OPAQUE_TYPE(nimxlc_TerminalContainer);

/** A handle to an iterator for a nimxlc_TerminalContainer */
NIMXLCAPI_DEFINE_OPAQUE_TYPE(nimxlc_TerminalIterator);

#define NIMXLC_DEFINE_OPAQUE_TYPE_ACCESSOR_FNS(newFnName, fromFnName, opaqueTypeName, actualPtrType) \
   static opaqueTypeName newFnName(actualPtrType* ptr = NULL) \
   {                                                          \
      return reinterpret_cast<opaqueTypeName>(ptr);           \
   }                                                          \
   static actualPtrType* fromFnName(opaqueTypeName opaque)    \
   {                                                          \
      return reinterpret_cast<actualPtrType*>(opaque);        \
   }

#define NIMXLC_DEFINE_OPAQUE_INDEX_ACCESSOR_FNS(newFnName, fromFnName, opaqueTypeName) \
   static opaqueTypeName newFnName(size_t index = 0)     \
   {                                                     \
      return reinterpret_cast<opaqueTypeName>(index);    \
   }                                                     \
   static size_t fromFnName(opaqueTypeName opaque)       \
   {                                                     \
      return reinterpret_cast<size_t>(opaque);           \
   }

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/visa.h sha256=c708ff874dc3f94f6e809e357cf2aa56dd6403199ad88878e14fc5aa810eeb60 bytes=64034 -->
## FILE: imports/include/visa.h

- repository: `ni/grpc-device`
- source_path: `imports/include/visa.h`
- sha256: `c708ff874dc3f94f6e809e357cf2aa56dd6403199ad88878e14fc5aa810eeb60`
- bytes: 64034

````c
/*---------------------------------------------------------------------------*/
/* Distributed by the IVI Foundation                                         */
/* Contains National Instruments extensions.                                 */
/* Do not modify the contents of this file.                                  */
/*---------------------------------------------------------------------------*/
/*                                                                           */
/* Title   : VISA.H                                                          */
/* Date    : 04-01-2022                                                      */
/* Purpose : Include file for the VISA Library 7.2 specification             */
/*                                                                           */
/*---------------------------------------------------------------------------*/
/* When using NI-VISA extensions, you must link with the VISA library that   */
/* comes with NI-VISA.  Currently, the extensions provided by NI-VISA are:   */
/*                                                                           */
/* PXI (Compact PCI eXtensions for Instrumentation) and PCI support.  To use */
/* this, you must define the macro NIVISA_PXI before including this header.  */
/* You must also create an INF file with the VISA Driver Development Wizard. */
/*                                                                           */
/* A fast set of macros for viPeekXX/viPokeXX that guarantees binary         */
/* compatibility with other implementations of VISA.  To use this, you must  */
/* define the macro NIVISA_PEEKPOKE before including this header.            */
/*                                                                           */
/* Support for USB devices that do not conform to a specific class.  To use  */
/* this, you must define the macro NIVISA_USB before including this header.  */
/* You must also create an INF file with the VISA Driver Development Wizard. */
/*---------------------------------------------------------------------------*/

#ifndef __VISA_HEADER__
#define __VISA_HEADER__
#include <stdarg.h>
#if !defined(__VISATYPE_HEADER__)
#include "visatype.h"
#endif
#define VI_SPEC_VERSION     (0x00700200UL)
#if defined(__cplusplus) || defined(__cplusplus__)
   extern "C" {
#endif
#if defined(_CVI_)
#pragma EnableLibraryRuntimeChecking
#endif
/*- VISA Types --------------------------------------------------------------*/
typedef ViObject             ViEvent;
typedef ViEvent      _VI_PTR ViPEvent;
typedef ViObject             ViFindList;
typedef ViFindList   _VI_PTR ViPFindList;
#if defined(_VI_INT64_UINT64_DEFINED) && defined(_VISA_ENV_IS_64_BIT)
typedef ViUInt64             ViBusAddress;
typedef ViUInt64             ViBusSize;
typedef ViUInt64             ViAttrState;
#else
typedef ViUInt32             ViBusAddress;
typedef ViUInt32             ViBusSize;
typedef ViUInt32             ViAttrState;
#endif
#if defined(_VI_INT64_UINT64_DEFINED)
typedef ViUInt64             ViBusAddress64;
typedef ViBusAddress64 _VI_PTR ViPBusAddress64;
#endif
typedef ViUInt32             ViEventType;
typedef ViEventType  _VI_PTR ViPEventType;
typedef ViEventType  _VI_PTR ViAEventType;
typedef void         _VI_PTR ViPAttrState;
typedef ViAttr       _VI_PTR ViPAttr;
typedef ViAttr       _VI_PTR ViAAttr;
typedef ViString             ViKeyId;
typedef ViConstString        ViConstKeyId;
typedef ViPString            ViPKeyId;
typedef ViUInt32             ViJobId;
typedef ViJobId      _VI_PTR ViPJobId;
typedef ViUInt32             ViAccessMode;
typedef ViAccessMode _VI_PTR ViPAccessMode;
typedef ViBusAddress _VI_PTR ViPBusAddress;
typedef ViUInt32             ViEventFilter;
typedef va_list              ViVAList;
typedef ViStatus (_VI_FUNCH _VI_PTR ViHndlr)
   (ViSession vi, ViEventType eventType, ViEvent event, ViAddr userHandle);
/*- Resource Manager Functions and Operations -------------------------------*/
ViStatus _VI_FUNC  viOpenDefaultRM (ViPSession vi);
ViStatus _VI_FUNC  viFindRsrc      (ViSession sesn, ViConstString expr, ViPFindList vi,
                                    ViPUInt32 retCnt, ViChar _VI_FAR desc[]);
ViStatus _VI_FUNC  viFindNext      (ViFindList vi, ViChar _VI_FAR desc[]);
ViStatus _VI_FUNC  viParseRsrc     (ViSession rmSesn, ViConstRsrc rsrcName,
                                    ViPUInt16 intfType, ViPUInt16 intfNum);
ViStatus _VI_FUNC  viParseRsrcEx   (ViSession rmSesn, ViConstRsrc rsrcName, ViPUInt16 intfType,
                                    ViPUInt16 intfNum, ViChar _VI_FAR rsrcClass[],
                                    ViChar _VI_FAR expandedUnaliasedName[],
                                    ViChar _VI_FAR aliasIfExists[]);
ViStatus _VI_FUNC  viOpen          (ViSession sesn, ViConstRsrc name, ViAccessMode mode,
                                    ViUInt32 timeout, ViPSession vi);
/*- Resource Template Operations --------------------------------------------*/
ViStatus _VI_FUNC  viClose         (ViObject vi);
ViStatus _VI_FUNC  viSetAttribute  (ViObject vi, ViAttr attrName, ViAttrState attrValue);
ViStatus _VI_FUNC  viGetAttribute  (ViObject vi, ViAttr attrName, void _VI_PTR attrValue);
ViStatus _VI_FUNC  viStatusDesc    (ViObject vi, ViStatus status, ViChar _VI_FAR desc[]);
ViStatus _VI_FUNC  viTerminate     (ViObject vi, ViUInt16 degree, ViJobId jobId);
ViStatus _VI_FUNC  viLock          (ViSession vi, ViAccessMode lockType, ViUInt32 timeout,
                                    ViConstKeyId requestedKey, ViChar _VI_FAR accessKey[]);
ViStatus _VI_FUNC  viUnlock        (ViSession vi);
ViStatus _VI_FUNC  viEnableEvent   (ViSession vi, ViEventType eventType, ViUInt16 mechanism,
                                    ViEventFilter context);
ViStatus _VI_FUNC  viDisableEvent  (ViSession vi, ViEventType eventType, ViUInt16 mechanism);
ViStatus _VI_FUNC  viDiscardEvents (ViSession vi, ViEventType eventType, ViUInt16 mechanism);
ViStatus _VI_FUNC  viWaitOnEvent   (ViSession vi, ViEventType inEventType, ViUInt32 timeout,
                                    ViPEventType outEventType, ViPEvent outContext);
ViStatus _VI_FUNC  viInstallHandler(ViSession vi, ViEventType eventType, ViHndlr handler,
                                    ViAddr userHandle);
ViStatus _VI_FUNC  viUninstallHandler(ViSession vi, ViEventType eventType, ViHndlr handler,
                                      ViAddr userHandle);
/*- Basic I/O Operations ----------------------------------------------------*/
ViStatus _VI_FUNC  viRead          (ViSession vi, ViPBuf buf, ViUInt32 cnt, ViPUInt32 retCnt);
ViStatus _VI_FUNC  viReadAsync     (ViSession vi, ViPBuf buf, ViUInt32 cnt, ViPJobId  jobId);
ViStatus _VI_FUNC  viReadToFile    (ViSession vi, ViConstString filename, ViUInt32 cnt,
                                    ViPUInt32 retCnt);
ViStatus _VI_FUNC  viWrite         (ViSession vi, ViConstBuf  buf, ViUInt32 cnt, ViPUInt32 retCnt);
ViStatus _VI_FUNC  viWriteAsync    (ViSession vi, ViConstBuf  buf, ViUInt32 cnt, ViPJobId  jobId);
ViStatus _VI_FUNC  viWriteFromFile (ViSession vi, ViConstString filename, ViUInt32 cnt,
                                    ViPUInt32 retCnt);
ViStatus _VI_FUNC  viAssertTrigger (ViSession vi, ViUInt16 protocol);
ViStatus _VI_FUNC  viReadSTB       (ViSession vi, ViPUInt16 status);
ViStatus _VI_FUNC  viClear         (ViSession vi);
/*- Formatted and Buffered I/O Operations -----------------------------------*/
ViStatus _VI_FUNC  viSetBuf        (ViSession vi, ViUInt16 mask, ViUInt32 size);
ViStatus _VI_FUNC  viFlush         (ViSession vi, ViUInt16 mask);
// ViStatus _VI_FUNC  viBufWrite      (ViSession vi, ViConstBuf  buf, ViUInt32 cnt, ViPUInt32 retCnt);
ViStatus _VI_FUNC  viBufRead       (ViSession vi, ViPBuf buf, ViUInt32 cnt, ViPUInt32 retCnt);
ViStatus _VI_FUNCC viPrintf        (ViSession vi, ViConstString writeFmt, ...);
ViStatus _VI_FUNC  viVPrintf       (ViSession vi, ViConstString writeFmt, ViVAList params);
ViStatus _VI_FUNCC viSPrintf       (ViSession vi, ViPBuf buf, ViConstString writeFmt, ...);
ViStatus _VI_FUNC  viVSPrintf      (ViSession vi, ViPBuf buf, ViConstString writeFmt,
                                    ViVAList params);
ViStatus _VI_FUNCC viScanf         (ViSession vi, ViConstString readFmt, ...);
ViStatus _VI_FUNC  viVScanf        (ViSession vi, ViConstString readFmt, ViVAList params);
ViStatus _VI_FUNCC viSScanf        (ViSession vi, ViConstBuf buf, ViConstString readFmt, ...);
ViStatus _VI_FUNC  viVSScanf       (ViSession vi, ViConstBuf buf, ViConstString readFmt,
                                    ViVAList params);
ViStatus _VI_FUNCC viQueryf        (ViSession vi, ViConstString writeFmt, ViConstString readFmt, ...);
ViStatus _VI_FUNC  viVQueryf       (ViSession vi, ViConstString writeFmt, ViConstString readFmt,
                                    ViVAList params);
/*- Memory I/O Operations ---------------------------------------------------*/
ViStatus _VI_FUNC  viIn8           (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViPUInt8  val8);
ViStatus _VI_FUNC  viOut8          (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViUInt8   val8);
ViStatus _VI_FUNC  viIn16          (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViPUInt16 val16);
ViStatus _VI_FUNC  viOut16         (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViUInt16  val16);
ViStatus _VI_FUNC  viIn32          (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViPUInt32 val32);
ViStatus _VI_FUNC  viOut32         (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViUInt32  val32);
#if defined(_VI_INT64_UINT64_DEFINED)
ViStatus _VI_FUNC  viIn64          (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViPUInt64 val64);
ViStatus _VI_FUNC  viOut64         (ViSession vi, ViUInt16 space,
                                    ViBusAddress offset, ViUInt64  val64);
ViStatus _VI_FUNC  viIn8Ex         (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViPUInt8  val8);
ViStatus _VI_FUNC  viOut8Ex        (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViUInt8   val8);
ViStatus _VI_FUNC  viIn16Ex        (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViPUInt16 val16);
ViStatus _VI_FUNC  viOut16Ex       (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViUInt16  val16);
ViStatus _VI_FUNC  viIn32Ex        (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViPUInt32 val32);
ViStatus _VI_FUNC  viOut32Ex       (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViUInt32  val32);
ViStatus _VI_FUNC  viIn64Ex        (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViPUInt64 val64);
ViStatus _VI_FUNC  viOut64Ex       (ViSession vi, ViUInt16 space,
                                    ViBusAddress64 offset, ViUInt64  val64);
#endif
ViStatus _VI_FUNC  viMoveIn8       (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt8  buf8);
ViStatus _VI_FUNC  viMoveOut8      (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt8  buf8);
ViStatus _VI_FUNC  viMoveIn16      (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt16 buf16);
ViStatus _VI_FUNC  viMoveOut16     (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt16 buf16);
ViStatus _VI_FUNC  viMoveIn32      (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt32 buf32);
ViStatus _VI_FUNC  viMoveOut32     (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt32 buf32);
#if defined(_VI_INT64_UINT64_DEFINED)
ViStatus _VI_FUNC  viMoveIn64      (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt64 buf64);
ViStatus _VI_FUNC  viMoveOut64     (ViSession vi, ViUInt16 space, ViBusAddress offset,
                                    ViBusSize length, ViAUInt64 buf64);
ViStatus _VI_FUNC  viMoveIn8Ex     (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt8  buf8);
ViStatus _VI_FUNC  viMoveOut8Ex    (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt8  buf8);
ViStatus _VI_FUNC  viMoveIn16Ex    (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt16 buf16);
ViStatus _VI_FUNC  viMoveOut16Ex   (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt16 buf16);
ViStatus _VI_FUNC  viMoveIn32Ex    (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt32 buf32);
ViStatus _VI_FUNC  viMoveOut32Ex   (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt32 buf32);
ViStatus _VI_FUNC  viMoveIn64Ex    (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt64 buf64);
ViStatus _VI_FUNC  viMoveOut64Ex   (ViSession vi, ViUInt16 space, ViBusAddress64 offset,
                                    ViBusSize length, ViAUInt64 buf64);
#endif
ViStatus _VI_FUNC  viMove          (ViSession vi, ViUInt16 srcSpace, ViBusAddress srcOffset,
                                    ViUInt16 srcWidth, ViUInt16 destSpace,
                                    ViBusAddress destOffset, ViUInt16 destWidth,
                                    ViBusSize srcLength);
ViStatus _VI_FUNC  viMoveAsync     (ViSession vi, ViUInt16 srcSpace, ViBusAddress srcOffset,
                                    ViUInt16 srcWidth, ViUInt16 destSpace,
                                    ViBusAddress destOffset, ViUInt16 destWidth,
                                    ViBusSize srcLength, ViPJobId jobId);
#if defined(_VI_INT64_UINT64_DEFINED)
ViStatus _VI_FUNC  viMoveEx        (ViSession vi, ViUInt16 srcSpace, ViBusAddress64 srcOffset,
                                    ViUInt16 srcWidth, ViUInt16 destSpace,
                                    ViBusAddress64 destOffset, ViUInt16 destWidth,
                                    ViBusSize srcLength);
ViStatus _VI_FUNC  viMoveAsyncEx   (ViSession vi, ViUInt16 srcSpace, ViBusAddress64 srcOffset,
                                    ViUInt16 srcWidth, ViUInt16 destSpace,
                                    ViBusAddress64 destOffset, ViUInt16 destWidth,
                                    ViBusSize srcLength, ViPJobId jobId);
#endif
ViStatus _VI_FUNC  viMapAddress    (ViSession vi, ViUInt16 mapSpace, ViBusAddress mapOffset,
                                    ViBusSize mapSize, ViBoolean access,
                                    ViAddr suggested, ViPAddr address);
ViStatus _VI_FUNC  viUnmapAddress  (ViSession vi);
#if defined(_VI_INT64_UINT64_DEFINED)
ViStatus _VI_FUNC  viMapAddressEx  (ViSession vi, ViUInt16 mapSpace, ViBusAddress64 mapOffset,
                                    ViBusSize mapSize, ViBoolean access,
                                    ViAddr suggested, ViPAddr address);
#endif
void     _VI_FUNC  viPeek8         (ViSession vi, ViAddr address, ViPUInt8  val8);
void     _VI_FUNC  viPoke8         (ViSession vi, ViAddr address, ViUInt8   val8);
void     _VI_FUNC  viPeek16        (ViSession vi, ViAddr address, ViPUInt16 val16);
void     _VI_FUNC  viPoke16        (ViSession vi, ViAddr address, ViUInt16  val16);
void     _VI_FUNC  viPeek32        (ViSession vi, ViAddr address, ViPUInt32 val32);
void     _VI_FUNC  viPoke32        (ViSession vi, ViAddr address, ViUInt32  val32);
#if defined(_VI_INT64_UINT64_DEFINED)
void     _VI_FUNC  viPeek64        (ViSession vi, ViAddr address, ViPUInt64 val64);
void     _VI_FUNC  viPoke64        (ViSession vi, ViAddr address, ViUInt64  val64);
#endif
/*- Shared Memory Operations ------------------------------------------------*/
ViStatus _VI_FUNC  viMemAlloc      (ViSession vi, ViBusSize size, ViPBusAddress offset);
ViStatus _VI_FUNC  viMemFree       (ViSession vi, ViBusAddress offset);
#if defined(_VI_INT64_UINT64_DEFINED)
ViStatus _VI_FUNC  viMemAllocEx    (ViSession vi, ViBusSize size, ViPBusAddress64 offset);
ViStatus _VI_FUNC  viMemFreeEx     (ViSession vi, ViBusAddress64 offset);
#endif
/*- Interface Specific Operations -------------------------------------------*/
ViStatus _VI_FUNC  viGpibControlREN(ViSession vi, ViUInt16 mode);
ViStatus _VI_FUNC  viGpibControlATN(ViSession vi, ViUInt16 mode);
ViStatus _VI_FUNC  viGpibSendIFC   (ViSession vi);
ViStatus _VI_FUNC  viGpibCommand   (ViSession vi, ViConstBuf cmd, ViUInt32 cnt, ViPUInt32 retCnt);
ViStatus _VI_FUNC  viGpibPassControl(ViSession vi, ViUInt16 primAddr, ViUInt16 secAddr);
ViStatus _VI_FUNC  viVxiCommandQuery(ViSession vi, ViUInt16 mode, ViUInt32 cmd,
                                     ViPUInt32 response);
ViStatus _VI_FUNC  viAssertUtilSignal(ViSession vi, ViUInt16 line);
ViStatus _VI_FUNC  viAssertIntrSignal(ViSession vi, ViInt16 mode, ViUInt32 statusID);
ViStatus _VI_FUNC  viMapTrigger    (ViSession vi, ViInt16 trigSrc, ViInt16 trigDest,
                                    ViUInt16 mode);
ViStatus _VI_FUNC  viUnmapTrigger  (ViSession vi, ViInt16 trigSrc, ViInt16 trigDest);
ViStatus _VI_FUNC  viUsbControlOut (ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest,
                                    ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength,
                                    ViConstBuf buf);
ViStatus _VI_FUNC  viUsbControlIn  (ViSession vi, ViInt16 bmRequestType, ViInt16 bRequest,
                                    ViUInt16 wValue, ViUInt16 wIndex, ViUInt16 wLength,
                                    ViPBuf buf, ViPUInt16 retCnt);
ViStatus _VI_FUNC  viPxiReserveTriggers(ViSession vi, ViInt16 cnt, ViAInt16 trigBuses,
                                    ViAInt16 trigLines, ViPInt16 failureIndex);
/*- Attributes (platform independent size) ----------------------------------*/
#define VI_ATTR_RSRC_CLASS                    (0xBFFF0001UL)
#define VI_ATTR_RSRC_NAME                     (0xBFFF0002UL)
#define VI_ATTR_RSRC_IMPL_VERSION             (0x3FFF0003UL)
#define VI_ATTR_RSRC_LOCK_STATE               (0x3FFF0004UL)
#define VI_ATTR_MAX_QUEUE_LENGTH              (0x3FFF0005UL)
#define VI_ATTR_USER_DATA_32                  (0x3FFF0007UL)
#define VI_ATTR_FDC_CHNL                      (0x3FFF000DUL)
#define VI_ATTR_FDC_MODE                      (0x3FFF000FUL)
#define VI_ATTR_FDC_GEN_SIGNAL_EN             (0x3FFF0011UL)
#define VI_ATTR_FDC_USE_PAIR                  (0x3FFF0013UL)
#define VI_ATTR_SEND_END_EN                   (0x3FFF0016UL)
#define VI_ATTR_TERMCHAR                      (0x3FFF0018UL)
#define VI_ATTR_TMO_VALUE                     (0x3FFF001AUL)
#define VI_ATTR_GPIB_READDR_EN                (0x3FFF001BUL)
#define VI_ATTR_IO_PROT                       (0x3FFF001CUL)
#define VI_ATTR_DMA_ALLOW_EN                  (0x3FFF001EUL)
#define VI_ATTR_ASRL_BAUD                     (0x3FFF0021UL)
#define VI_ATTR_ASRL_DATA_BITS                (0x3FFF0022UL)
#define VI_ATTR_ASRL_PARITY                   (0x3FFF0023UL)
#define VI_ATTR_ASRL_STOP_BITS                (0x3FFF0024UL)
#define VI_ATTR_ASRL_FLOW_CNTRL               (0x3FFF0025UL)
#define VI_ATTR_RD_BUF_OPER_MODE              (0x3FFF002AUL)
#define VI_ATTR_RD_BUF_SIZE                   (0x3FFF002BUL)
#define VI_ATTR_WR_BUF_OPER_MODE              (0x3FFF002DUL)
#define VI_ATTR_WR_BUF_SIZE                   (0x3FFF002EUL)
#define VI_ATTR_SUPPRESS_END_EN               (0x3FFF0036UL)
#define VI_ATTR_TERMCHAR_EN                   (0x3FFF0038UL)
#define VI_ATTR_DEST_ACCESS_PRIV              (0x3FFF0039UL)
#define VI_ATTR_DEST_BYTE_ORDER               (0x3FFF003AUL)
#define VI_ATTR_SRC_ACCESS_PRIV               (0x3FFF003CUL)
#define VI_ATTR_SRC_BYTE_ORDER                (0x3FFF003DUL)
#define VI_ATTR_SRC_INCREMENT                 (0x3FFF0040UL)
#define VI_ATTR_DEST_INCREMENT                (0x3FFF0041UL)
#define VI_ATTR_WIN_ACCESS_PRIV               (0x3FFF0045UL)
#define VI_ATTR_WIN_BYTE_ORDER                (0x3FFF0047UL)
#define VI_ATTR_GPIB_ATN_STATE                (0x3FFF0057UL)
#define VI_ATTR_GPIB_ADDR_STATE               (0x3FFF005CUL)
#define VI_ATTR_GPIB_CIC_STATE                (0x3FFF005EUL)
#define VI_ATTR_GPIB_NDAC_STATE               (0x3FFF0062UL)
#define VI_ATTR_GPIB_SRQ_STATE                (0x3FFF0067UL)
#define VI_ATTR_GPIB_SYS_CNTRL_STATE          (0x3FFF0068UL)
#define VI_ATTR_GPIB_HS488_CBL_LEN            (0x3FFF0069UL)
#define VI_ATTR_CMDR_LA                       (0x3FFF006BUL)
#define VI_ATTR_VXI_DEV_CLASS                 (0x3FFF006CUL)
#define VI_ATTR_MAINFRAME_LA                  (0x3FFF0070UL)
#define VI_ATTR_MANF_NAME                     (0xBFFF0072UL)
#define VI_ATTR_MODEL_NAME                    (0xBFFF0077UL)
#define VI_ATTR_VXI_VME_INTR_STATUS           (0x3FFF008BUL)
#define VI_ATTR_VXI_TRIG_STATUS               (0x3FFF008DUL)
#define VI_ATTR_VXI_VME_SYSFAIL_STATE         (0x3FFF0094UL)
#define VI_ATTR_WIN_BASE_ADDR_32              (0x3FFF0098UL)
#define VI_ATTR_WIN_SIZE_32                   (0x3FFF009AUL)
#define VI_ATTR_ASRL_AVAIL_NUM                (0x3FFF00ACUL)
#define VI_ATTR_MEM_BASE_32                   (0x3FFF00ADUL)
#define VI_ATTR_ASRL_CTS_STATE                (0x3FFF00AEUL)
#define VI_ATTR_ASRL_DCD_STATE                (0x3FFF00AFUL)
#define VI_ATTR_ASRL_DSR_STATE                (0x3FFF00B1UL)
#define VI_ATTR_ASRL_DTR_STATE                (0x3FFF00B2UL)
#define VI_ATTR_ASRL_END_IN                   (0x3FFF00B3UL)
#define VI_ATTR_ASRL_END_OUT                  (0x3FFF00B4UL)
#define VI_ATTR_ASRL_REPLACE_CHAR             (0x3FFF00BEUL)
#define VI_ATTR_ASRL_RI_STATE                 (0x3FFF00BFUL)
#define VI_ATTR_ASRL_RTS_STATE                (0x3FFF00C0UL)
#define VI_ATTR_ASRL_XON_CHAR                 (0x3FFF00C1UL)
#define VI_ATTR_ASRL_XOFF_CHAR                (0x3FFF00C2UL)
#define VI_ATTR_WIN_ACCESS                    (0x3FFF00C3UL)
#define VI_ATTR_RM_SESSION                    (0x3FFF00C4UL)
#define VI_ATTR_VXI_LA                        (0x3FFF00D5UL)
#define VI_ATTR_MANF_ID                       (0x3FFF00D9UL)
#define VI_ATTR_MEM_SIZE_32                   (0x3FFF00DDUL)
#define VI_ATTR_MEM_SPACE                     (0x3FFF00DEUL)
#define VI_ATTR_MODEL_CODE                    (0x3FFF00DFUL)
#define VI_ATTR_SLOT                          (0x3FFF00E8UL)
#define VI_ATTR_INTF_INST_NAME                (0xBFFF00E9UL)
#define VI_ATTR_IMMEDIATE_SERV                (0x3FFF0100UL)
#define VI_ATTR_INTF_PARENT_NUM               (0x3FFF0101UL)
#define VI_ATTR_RSRC_SPEC_VERSION             (0x3FFF0170UL)
#define VI_ATTR_INTF_TYPE                     (0x3FFF0171UL)
#define VI_ATTR_GPIB_PRIMARY_ADDR             (0x3FFF0172UL)
#define VI_ATTR_GPIB_SECONDARY_ADDR           (0x3FFF0173UL)
#define VI_ATTR_RSRC_MANF_NAME                (0xBFFF0174UL)
#define VI_ATTR_RSRC_MANF_ID                  (0x3FFF0175UL)
#define VI_ATTR_INTF_NUM                      (0x3FFF0176UL)
#define VI_ATTR_TRIG_ID                       (0x3FFF0177UL)
#define VI_ATTR_GPIB_REN_STATE                (0x3FFF0181UL)
#define VI_ATTR_GPIB_UNADDR_EN                (0x3FFF0184UL)
#define VI_ATTR_DEV_STATUS_BYTE               (0x3FFF0189UL)
#define VI_ATTR_FILE_APPEND_EN                (0x3FFF0192UL)
#define VI_ATTR_VXI_TRIG_SUPPORT              (0x3FFF0194UL)
#define VI_ATTR_TCPIP_ADDR                    (0xBFFF0195UL)
#define VI_ATTR_TCPIP_HOSTNAME                (0xBFFF0196UL)
#define VI_ATTR_TCPIP_PORT                    (0x3FFF0197UL)
#define VI_ATTR_TCPIP_DEVICE_NAME             (0xBFFF0199UL)
#define VI_ATTR_TCPIP_NODELAY                 (0x3FFF019AUL)
#define VI_ATTR_TCPIP_KEEPALIVE               (0x3FFF019BUL)
#define VI_ATTR_4882_COMPLIANT                (0x3FFF019FUL)
#define VI_ATTR_USB_SERIAL_NUM                (0xBFFF01A0UL)
#define VI_ATTR_USB_INTFC_NUM                 (0x3FFF01A1UL)
#define VI_ATTR_USB_PROTOCOL                  (0x3FFF01A7UL)
#define VI_ATTR_USB_MAX_INTR_SIZE             (0x3FFF01AFUL)
#define VI_ATTR_PXI_DEV_NUM                   (0x3FFF0201UL)
#define VI_ATTR_PXI_FUNC_NUM                  (0x3FFF0202UL)
#define VI_ATTR_PXI_BUS_NUM                   (0x3FFF0205UL)
#define VI_ATTR_PXI_CHASSIS                   (0x3FFF0206UL)
#define VI_ATTR_PXI_SLOTPATH                  (0xBFFF0207UL)
#define VI_ATTR_PXI_SLOT_LBUS_LEFT            (0x3FFF0208UL)
#define VI_ATTR_PXI_SLOT_LBUS_RIGHT           (0x3FFF0209UL)
#define VI_ATTR_PXI_TRIG_BUS                  (0x3FFF020AUL)
#define VI_ATTR_PXI_STAR_TRIG_BUS             (0x3FFF020BUL)
#define VI_ATTR_PXI_STAR_TRIG_LINE            (0x3FFF020CUL)
#define VI_ATTR_PXI_SRC_TRIG_BUS              (0x3FFF020DUL)
#define VI_ATTR_PXI_DEST_TRIG_BUS             (0x3FFF020EUL)
#define VI_ATTR_PXI_MEM_TYPE_BAR0             (0x3FFF0211UL)
#define VI_ATTR_PXI_MEM_TYPE_BAR1             (0x3FFF0212UL)
#define VI_ATTR_PXI_MEM_TYPE_BAR2             (0x3FFF0213UL)
#define VI_ATTR_PXI_MEM_TYPE_BAR3             (0x3FFF0214UL)
#define VI_ATTR_PXI_MEM_TYPE_BAR4             (0x3FFF0215UL)
#define VI_ATTR_PXI_MEM_TYPE_BAR5             (0x3FFF0216UL)
#define VI_ATTR_PXI_MEM_BASE_BAR0_32          (0x3FFF0221UL)
#define VI_ATTR_PXI_MEM_BASE_BAR1_32          (0x3FFF0222UL)
#define VI_ATTR_PXI_MEM_BASE_BAR2_32          (0x3FFF0223UL)
#define VI_ATTR_PXI_MEM_BASE_BAR3_32          (0x3FFF0224UL)
#define VI_ATTR_PXI_MEM_BASE_BAR4_32          (0x3FFF0225UL)
#define VI_ATTR_PXI_MEM_BASE_BAR5_32          (0x3FFF0226UL)
#define VI_ATTR_PXI_MEM_BASE_BAR0_64          (0x3FFF0228UL)
#define VI_ATTR_PXI_MEM_BASE_BAR1_64          (0x3FFF0229UL)
#define VI_ATTR_PXI_MEM_BASE_BAR2_64          (0x3FFF022AUL)
#define VI_ATTR_PXI_MEM_BASE_BAR3_64          (0x3FFF022BUL)
#define VI_ATTR_PXI_MEM_BASE_BAR4_64          (0x3FFF022CUL)
#define VI_ATTR_PXI_MEM_BASE_BAR5_64          (0x3FFF022DUL)
#define VI_ATTR_PXI_MEM_SIZE_BAR0_32          (0x3FFF0231UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR1_32          (0x3FFF0232UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR2_32          (0x3FFF0233UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR3_32          (0x3FFF0234UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR4_32          (0x3FFF0235UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR5_32          (0x3FFF0236UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR0_64          (0x3FFF0238UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR1_64          (0x3FFF0239UL)
#define VI_ATTR_PXI_MEM_SIZE_BAR2_64          (0x3FFF023AUL)
#define VI_ATTR_PXI_MEM_SIZE_BAR3_64          (0x3FFF023BUL)
#define VI_ATTR_PXI_MEM_SIZE_BAR4_64          (0x3FFF023CUL)
#define VI_ATTR_PXI_MEM_SIZE_BAR5_64          (0x3FFF023DUL)
#define VI_ATTR_PXI_IS_EXPRESS                (0x3FFF0240UL)
#define VI_ATTR_PXI_SLOT_LWIDTH               (0x3FFF0241UL)
#define VI_ATTR_PXI_MAX_LWIDTH                (0x3FFF0242UL)
#define VI_ATTR_PXI_ACTUAL_LWIDTH             (0x3FFF0243UL)
#define VI_ATTR_PXI_DSTAR_BUS                 (0x3FFF0244UL)
#define VI_ATTR_PXI_DSTAR_SET                 (0x3FFF0245UL)
#define VI_ATTR_PXI_ALLOW_WRITE_COMBINE       (0x3FFF0246UL)
#define VI_ATTR_PXI_SLOT_WIDTH                (0x3FFF0247UL)
#define VI_ATTR_PXI_SLOT_OFFSET               (0x3FFF0248UL)
#define VI_ATTR_TCPIP_SERVER_CERT_ISSUER_NAME (0xBFFF0270UL)
#define VI_ATTR_TCPIP_SERVER_CERT_SUBJECT_NAME    (0xBFFF0271UL)
#define VI_ATTR_TCPIP_SERVER_CERT_EXPIRATION_DATE (0xBFFF0272UL)
#define VI_ATTR_TCPIP_SERVER_CERT_IS_PERPETUAL    (0x3FFF0273UL)
#define VI_ATTR_TCPIP_SASL_MECHANISM          (0xBFFF0274UL)
#define VI_ATTR_TCPIP_TLS_CIPHER_SUITE        (0xBFFF0275UL)
#define VI_ATTR_TCPIP_SERVER_CERT             (0xBFFF0276UL)
#define VI_ATTR_TCPIP_SERVER_CERT_SIZE        (0x3FFF0277UL)
#define VI_ATTR_TCPIP_HISLIP_OVERLAP_EN       (0x3FFF0300UL)
#define VI_ATTR_TCPIP_HISLIP_VERSION          (0x3FFF0301UL)
#define VI_ATTR_TCPIP_HISLIP_MAX_MESSAGE_KB   (0x3FFF0302UL)
#define VI_ATTR_TCPIP_IS_HISLIP               (0x3FFF0303UL)
#define VI_ATTR_TCPIP_HISLIP_ENCRYPTION_EN    (0x3FFF0304UL)
#define VI_ATTR_JOB_ID                        (0x3FFF4006UL)
#define VI_ATTR_EVENT_TYPE                    (0x3FFF4010UL)
#define VI_ATTR_SIGP_STATUS_ID                (0x3FFF4011UL)
#define VI_ATTR_RECV_TRIG_ID                  (0x3FFF4012UL)
#define VI_ATTR_INTR_STATUS_ID                (0x3FFF4023UL)
#define VI_ATTR_STATUS                        (0x3FFF4025UL)
#define VI_ATTR_RET_COUNT_32                  (0x3FFF4026UL)
#define VI_ATTR_BUFFER                        (0x3FFF4027UL)
#define VI_ATTR_RECV_INTR_LEVEL               (0x3FFF4041UL)
#define VI_ATTR_OPER_NAME                     (0xBFFF4042UL)
#define VI_ATTR_GPIB_RECV_CIC_STATE           (0x3FFF4193UL)
#define VI_ATTR_RECV_TCPIP_ADDR               (0xBFFF4198UL)
#define VI_ATTR_USB_RECV_INTR_SIZE            (0x3FFF41B0UL)
#define VI_ATTR_USB_RECV_INTR_DATA            (0xBFFF41B1UL)
#define VI_ATTR_PXI_RECV_INTR_SEQ             (0x3FFF4240UL)
#define VI_ATTR_PXI_RECV_INTR_DATA            (0x3FFF4241UL)
/*- Attributes (platform dependent size) ------------------------------------*/
#if defined(_VI_INT64_UINT64_DEFINED) && defined(_VISA_ENV_IS_64_BIT)
#define VI_ATTR_USER_DATA_64                  (0x3FFF000AUL)
#define VI_ATTR_RET_COUNT_64                  (0x3FFF4028UL)
#define VI_ATTR_USER_DATA                     (VI_ATTR_USER_DATA_64)
#define VI_ATTR_RET_COUNT                     (VI_ATTR_RET_COUNT_64)
#else
#define VI_ATTR_USER_DATA                     (VI_ATTR_USER_DATA_32)
#define VI_ATTR_RET_COUNT                     (VI_ATTR_RET_COUNT_32)
#endif
#if defined(_VI_INT64_UINT64_DEFINED)
#define VI_ATTR_WIN_BASE_ADDR_64              (0x3FFF009BUL)
#define VI_ATTR_WIN_SIZE_64                   (0x3FFF009CUL)
#define VI_ATTR_MEM_BASE_64                   (0x3FFF00D0UL)
#define VI_ATTR_MEM_SIZE_64                   (0x3FFF00D1UL)
#endif
#if defined(_VI_INT64_UINT64_DEFINED) && defined(_VISA_ENV_IS_64_BIT)
#define VI_ATTR_WIN_BASE_ADDR                 (VI_ATTR_WIN_BASE_ADDR_64)
#define VI_ATTR_WIN_SIZE                      (VI_ATTR_WIN_SIZE_64)
#define VI_ATTR_MEM_BASE                      (VI_ATTR_MEM_BASE_64)
#define VI_ATTR_MEM_SIZE                      (VI_ATTR_MEM_SIZE_64)
#define VI_ATTR_PXI_MEM_BASE_BAR0             (VI_ATTR_PXI_MEM_BASE_BAR0_64)
#define VI_ATTR_PXI_MEM_BASE_BAR1             (VI_ATTR_PXI_MEM_BASE_BAR1_64)
#define VI_ATTR_PXI_MEM_BASE_BAR2             (VI_ATTR_PXI_MEM_BASE_BAR2_64)
#define VI_ATTR_PXI_MEM_BASE_BAR3             (VI_ATTR_PXI_MEM_BASE_BAR3_64)
#define VI_ATTR_PXI_MEM_BASE_BAR4             (VI_ATTR_PXI_MEM_BASE_BAR4_64)
#define VI_ATTR_PXI_MEM_BASE_BAR5             (VI_ATTR_PXI_MEM_BASE_BAR5_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR0             (VI_ATTR_PXI_MEM_SIZE_BAR0_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR1             (VI_ATTR_PXI_MEM_SIZE_BAR1_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR2             (VI_ATTR_PXI_MEM_SIZE_BAR2_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR3             (VI_ATTR_PXI_MEM_SIZE_BAR3_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR4             (VI_ATTR_PXI_MEM_SIZE_BAR4_64)
#define VI_ATTR_PXI_MEM_SIZE_BAR5             (VI_ATTR_PXI_MEM_SIZE_BAR5_64)
#else
#define VI_ATTR_WIN_BASE_ADDR                 (VI_ATTR_WIN_BASE_ADDR_32)
#define VI_ATTR_WIN_SIZE                      (VI_ATTR_WIN_SIZE_32)
#define VI_ATTR_MEM_BASE                      (VI_ATTR_MEM_BASE_32)
#define VI_ATTR_MEM_SIZE                      (VI_ATTR_MEM_SIZE_32)
#define VI_ATTR_PXI_MEM_BASE_BAR0             (VI_ATTR_PXI_MEM_BASE_BAR0_32)
#define VI_ATTR_PXI_MEM_BASE_BAR1             (VI_ATTR_PXI_MEM_BASE_BAR1_32)
#define VI_ATTR_PXI_MEM_BASE_BAR2             (VI_ATTR_PXI_MEM_BASE_BAR2_32)
#define VI_ATTR_PXI_MEM_BASE_BAR3             (VI_ATTR_PXI_MEM_BASE_BAR3_32)
#define VI_ATTR_PXI_MEM_BASE_BAR4             (VI_ATTR_PXI_MEM_BASE_BAR4_32)
#define VI_ATTR_PXI_MEM_BASE_BAR5             (VI_ATTR_PXI_MEM_BASE_BAR5_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR0             (VI_ATTR_PXI_MEM_SIZE_BAR0_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR1             (VI_ATTR_PXI_MEM_SIZE_BAR1_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR2             (VI_ATTR_PXI_MEM_SIZE_BAR2_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR3             (VI_ATTR_PXI_MEM_SIZE_BAR3_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR4             (VI_ATTR_PXI_MEM_SIZE_BAR4_32)
#define VI_ATTR_PXI_MEM_SIZE_BAR5             (VI_ATTR_PXI_MEM_SIZE_BAR5_32)
#endif
/*- Event Types -------------------------------------------------------------*/
#define VI_EVENT_IO_COMPLETION                (0x3FFF2009UL)
#define VI_EVENT_TRIG                         (0xBFFF200AUL)
#define VI_EVENT_SERVICE_REQ                  (0x3FFF200BUL)
#define VI_EVENT_CLEAR                        (0x3FFF200DUL)
#define VI_EVENT_EXCEPTION                    (0xBFFF200EUL)
#define VI_EVENT_GPIB_CIC                     (0x3FFF2012UL)
#define VI_EVENT_GPIB_TALK                    (0x3FFF2013UL)
#define VI_EVENT_GPIB_LISTEN                  (0x3FFF2014UL)
#define VI_EVENT_VXI_VME_SYSFAIL              (0x3FFF201DUL)
#define VI_EVENT_VXI_VME_SYSRESET             (0x3FFF201EUL)
#define VI_EVENT_VXI_SIGP                     (0x3FFF2020UL)
#define VI_EVENT_VXI_VME_INTR                 (0xBFFF2021UL)
#define VI_EVENT_PXI_INTR                     (0x3FFF2022UL)
#define VI_EVENT_TCPIP_CONNECT                (0x3FFF2036UL)
#define VI_EVENT_USB_INTR                     (0x3FFF2037UL)
#define VI_ALL_ENABLED_EVENTS                 (0x3FFF7FFFUL)
/*- Completion and Error Codes ----------------------------------------------*/
#define VI_SUCCESS_EVENT_EN                   (0x3FFF0002L) /* 3FFF0002,  1073676290 */
#define VI_SUCCESS_EVENT_DIS                  (0x3FFF0003L) /* 3FFF0003,  1073676291 */
#define VI_SUCCESS_QUEUE_EMPTY                (0x3FFF0004L) /* 3FFF0004,  1073676292 */
#define VI_SUCCESS_TERM_CHAR                  (0x3FFF0005L) /* 3FFF0005,  1073676293 */
#define VI_SUCCESS_MAX_CNT                    (0x3FFF0006L) /* 3FFF0006,  1073676294 */
#define VI_SUCCESS_DEV_NPRESENT               (0x3FFF007DL) /* 3FFF007D,  1073676413 */
#define VI_SUCCESS_TRIG_MAPPED                (0x3FFF007EL) /* 3FFF007E,  1073676414 */
#define VI_SUCCESS_QUEUE_NEMPTY               (0x3FFF0080L) /* 3FFF0080,  1073676416 */
#define VI_SUCCESS_NCHAIN                     (0x3FFF0098L) /* 3FFF0098,  1073676440 */
#define VI_SUCCESS_NESTED_SHARED              (0x3FFF0099L) /* 3FFF0099,  1073676441 */
#define VI_SUCCESS_NESTED_EXCLUSIVE           (0x3FFF009AL) /* 3FFF009A,  1073676442 */
#define VI_SUCCESS_SYNC                       (0x3FFF009BL) /* 3FFF009B,  1073676443 */
#define VI_WARN_QUEUE_OVERFLOW                (0x3FFF000CL) /* 3FFF000C,  1073676300 */
#define VI_WARN_CONFIG_NLOADED                (0x3FFF0077L) /* 3FFF0077,  1073676407 */
#define VI_WARN_NULL_OBJECT                   (0x3FFF0082L) /* 3FFF0082,  1073676418 */
#define VI_WARN_NSUP_ATTR_STATE               (0x3FFF0084L) /* 3FFF0084,  1073676420 */
#define VI_WARN_UNKNOWN_STATUS                (0x3FFF0085L) /* 3FFF0085,  1073676421 */
#define VI_WARN_NSUP_BUF                      (0x3FFF0088L) /* 3FFF0088,  1073676424 */
#define VI_WARN_EXT_FUNC_NIMPL                (0x3FFF00A9L) /* 3FFF00A9,  1073676457 */
#define VI_WARN_SERVER_CERT_UNTRUSTED         (0x3FFF00F0L) /* 3FFF00F0,  1073676528 */
#define VI_WARN_SERVER_CERT_INV_SUBJECT       (0x3FFF00F1L) /* 3FFF00F1,  1073676529 */
#define VI_ERROR_SYSTEM_ERROR       (_VI_ERROR+0x3FFF0000L) /* BFFF0000, -1073807360 */
#define VI_ERROR_INV_OBJECT         (_VI_ERROR+0x3FFF000EL) /* BFFF000E, -1073807346 */
#define VI_ERROR_RSRC_LOCKED        (_VI_ERROR+0x3FFF000FL) /* BFFF000F, -1073807345 */
#define VI_ERROR_INV_EXPR           (_VI_ERROR+0x3FFF0010L) /* BFFF0010, -1073807344 */
#define VI_ERROR_RSRC_NFOUND        (_VI_ERROR+0x3FFF0011L) /* BFFF0011, -1073807343 */
#define VI_ERROR_INV_RSRC_NAME      (_VI_ERROR+0x3FFF0012L) /* BFFF0012, -1073807342 */
#define VI_ERROR_INV_ACC_MODE       (_VI_ERROR+0x3FFF0013L) /* BFFF0013, -1073807341 */
#define VI_ERROR_TMO                (_VI_ERROR+0x3FFF0015L) /* BFFF0015, -1073807339 */
#define VI_ERROR_CLOSING_FAILED     (_VI_ERROR+0x3FFF0016L) /* BFFF0016, -1073807338 */
#define VI_ERROR_INV_DEGREE         (_VI_ERROR+0x3FFF001BL) /* BFFF001B, -1073807333 */
#define VI_ERROR_INV_JOB_ID         (_VI_ERROR+0x3FFF001CL) /* BFFF001C, -1073807332 */
#define VI_ERROR_NSUP_ATTR          (_VI_ERROR+0x3FFF001DL) /* BFFF001D, -1073807331 */
#define VI_ERROR_NSUP_ATTR_STATE    (_VI_ERROR+0x3FFF001EL) /* BFFF001E, -1073807330 */
#define VI_ERROR_ATTR_READONLY      (_VI_ERROR+0x3FFF001FL) /* BFFF001F, -1073807329 */
#define VI_ERROR_INV_LOCK_TYPE      (_VI_ERROR+0x3FFF0020L) /* BFFF0020, -1073807328 */
#define VI_ERROR_INV_ACCESS_KEY     (_VI_ERROR+0x3FFF0021L) /* BFFF0021, -1073807327 */
#define VI_ERROR_INV_EVENT          (_VI_ERROR+0x3FFF0026L) /* BFFF0026, -1073807322 */
#define VI_ERROR_INV_MECH           (_VI_ERROR+0x3FFF0027L) /* BFFF0027, -1073807321 */
#define VI_ERROR_HNDLR_NINSTALLED   (_VI_ERROR+0x3FFF0028L) /* BFFF0028, -1073807320 */
#define VI_ERROR_INV_HNDLR_REF      (_VI_ERROR+0x3FFF0029L) /* BFFF0029, -1073807319 */
#define VI_ERROR_INV_CONTEXT        (_VI_ERROR+0x3FFF002AL) /* BFFF002A, -1073807318 */
#define VI_ERROR_QUEUE_OVERFLOW     (_VI_ERROR+0x3FFF002DL) /* BFFF002D, -1073807315 */
#define VI_ERROR_NENABLED           (_VI_ERROR+0x3FFF002FL) /* BFFF002F, -1073807313 */
#define VI_ERROR_ABORT              (_VI_ERROR+0x3FFF0030L) /* BFFF0030, -1073807312 */
#define VI_ERROR_RAW_WR_PROT_VIOL   (_VI_ERROR+0x3FFF0034L) /* BFFF0034, -1073807308 */
#define VI_ERROR_RAW_RD_PROT_VIOL   (_VI_ERROR+0x3FFF0035L) /* BFFF0035, -1073807307 */
#define VI_ERROR_OUTP_PROT_VIOL     (_VI_ERROR+0x3FFF0036L) /* BFFF0036, -1073807306 */
#define VI_ERROR_INP_PROT_VIOL      (_VI_ERROR+0x3FFF0037L) /* BFFF0037, -1073807305 */
#define VI_ERROR_BERR               (_VI_ERROR+0x3FFF0038L) /* BFFF0038, -1073807304 */
#define VI_ERROR_IN_PROGRESS        (_VI_ERROR+0x3FFF0039L) /* BFFF0039, -1073807303 */
#define VI_ERROR_INV_SETUP          (_VI_ERROR+0x3FFF003AL) /* BFFF003A, -1073807302 */
#define VI_ERROR_QUEUE_ERROR        (_VI_ERROR+0x3FFF003BL) /* BFFF003B, -1073807301 */
#define VI_ERROR_ALLOC              (_VI_ERROR+0x3FFF003CL) /* BFFF003C, -1073807300 */
#define VI_ERROR_INV_MASK           (_VI_ERROR+0x3FFF003DL) /* BFFF003D, -1073807299 */
#define VI_ERROR_IO                 (_VI_ERROR+0x3FFF003EL) /* BFFF003E, -1073807298 */
#define VI_ERROR_INV_FMT            (_VI_ERROR+0x3FFF003FL) /* BFFF003F, -1073807297 */
#define VI_ERROR_NSUP_FMT           (_VI_ERROR+0x3FFF0041L) /* BFFF0041, -1073807295 */
#define VI_ERROR_LINE_IN_USE        (_VI_ERROR+0x3FFF0042L) /* BFFF0042, -1073807294 */
#define VI_ERROR_LINE_NRESERVED     (_VI_ERROR+0x3FFF0043L) /* BFFF0043, -1073807293 */
#define VI_ERROR_NSUP_MODE          (_VI_ERROR+0x3FFF0046L) /* BFFF0046, -1073807290 */
#define VI_ERROR_SRQ_NOCCURRED      (_VI_ERROR+0x3FFF004AL) /* BFFF004A, -1073807286 */
#define VI_ERROR_INV_SPACE          (_VI_ERROR+0x3FFF004EL) /* BFFF004E, -1073807282 */
#define VI_ERROR_INV_OFFSET         (_VI_ERROR+0x3FFF0051L) /* BFFF0051, -1073807279 */
#define VI_ERROR_INV_WIDTH          (_VI_ERROR+0x3FFF0052L) /* BFFF0052, -1073807278 */
#define VI_ERROR_NSUP_OFFSET        (_VI_ERROR+0x3FFF0054L) /* BFFF0054, -1073807276 */
#define VI_ERROR_NSUP_VAR_WIDTH     (_VI_ERROR+0x3FFF0055L) /* BFFF0055, -1073807275 */
#define VI_ERROR_WINDOW_NMAPPED     (_VI_ERROR+0x3FFF0057L) /* BFFF0057, -1073807273 */
#define VI_ERROR_RESP_PENDING       (_VI_ERROR+0x3FFF0059L) /* BFFF0059, -1073807271 */
#define VI_ERROR_NLISTENERS         (_VI_ERROR+0x3FFF005FL) /* BFFF005F, -1073807265 */
#define VI_ERROR_NCIC               (_VI_ERROR+0x3FFF0060L) /* BFFF0060, -1073807264 */
#define VI_ERROR_NSYS_CNTLR         (_VI_ERROR+0x3FFF0061L) /* BFFF0061, -1073807263 */
#define VI_ERROR_NSUP_OPER          (_VI_ERROR+0x3FFF0067L) /* BFFF0067, -1073807257 */
#define VI_ERROR_INTR_PENDING       (_VI_ERROR+0x3FFF0068L) /* BFFF0068, -1073807256 */
#define VI_ERROR_ASRL_PARITY        (_VI_ERROR+0x3FFF006AL) /* BFFF006A, -1073807254 */
#define VI_ERROR_ASRL_FRAMING       (_VI_ERROR+0x3FFF006BL) /* BFFF006B, -1073807253 */
#define VI_ERROR_ASRL_OVERRUN       (_VI_ERROR+0x3FFF006CL) /* BFFF006C, -1073807252 */
#define VI_ERROR_TRIG_NMAPPED       (_VI_ERROR+0x3FFF006EL) /* BFFF006E, -1073807250 */
#define VI_ERROR_NSUP_ALIGN_OFFSET  (_VI_ERROR+0x3FFF0070L) /* BFFF0070, -1073807248 */
#define VI_ERROR_USER_BUF           (_VI_ERROR+0x3FFF0071L) /* BFFF0071, -1073807247 */
#define VI_ERROR_RSRC_BUSY          (_VI_ERROR+0x3FFF0072L) /* BFFF0072, -1073807246 */
#define VI_ERROR_NSUP_WIDTH         (_VI_ERROR+0x3FFF0076L) /* BFFF0076, -1073807242 */
#define VI_ERROR_INV_PARAMETER      (_VI_ERROR+0x3FFF0078L) /* BFFF0078, -1073807240 */
#define VI_ERROR_INV_PROT           (_VI_ERROR+0x3FFF0079L) /* BFFF0079, -1073807239 */
#define VI_ERROR_INV_SIZE           (_VI_ERROR+0x3FFF007BL) /* BFFF007B, -1073807237 */
#define VI_ERROR_WINDOW_MAPPED      (_VI_ERROR+0x3FFF0080L) /* BFFF0080, -1073807232 */
#define VI_ERROR_NIMPL_OPER         (_VI_ERROR+0x3FFF0081L) /* BFFF0081, -1073807231 */
#define VI_ERROR_INV_LENGTH         (_VI_ERROR+0x3FFF0083L) /* BFFF0083, -1073807229 */
#define VI_ERROR_INV_MODE           (_VI_ERROR+0x3FFF0091L) /* BFFF0091, -1073807215 */
#define VI_ERROR_SESN_NLOCKED       (_VI_ERROR+0x3FFF009CL) /* BFFF009C, -1073807204 */
#define VI_ERROR_MEM_NSHARED        (_VI_ERROR+0x3FFF009DL) /* BFFF009D, -1073807203 */
#define VI_ERROR_LIBRARY_NFOUND     (_VI_ERROR+0x3FFF009EL) /* BFFF009E, -1073807202 */
#define VI_ERROR_NSUP_INTR          (_VI_ERROR+0x3FFF009FL) /* BFFF009F, -1073807201 */
#define VI_ERROR_INV_LINE           (_VI_ERROR+0x3FFF00A0L) /* BFFF00A0, -1073807200 */
#define VI_ERROR_FILE_ACCESS        (_VI_ERROR+0x3FFF00A1L) /* BFFF00A1, -1073807199 */
#define VI_ERROR_FILE_IO            (_VI_ERROR+0x3FFF00A2L) /* BFFF00A2, -1073807198 */
#define VI_ERROR_NSUP_LINE          (_VI_ERROR+0x3FFF00A3L) /* BFFF00A3, -1073807197 */
#define VI_ERROR_NSUP_MECH          (_VI_ERROR+0x3FFF00A4L) /* BFFF00A4, -1073807196 */
#define VI_ERROR_INTF_NUM_NCONFIG   (_VI_ERROR+0x3FFF00A5L) /* BFFF00A5, -1073807195 */
#define VI_ERROR_CONN_LOST          (_VI_ERROR+0x3FFF00A6L) /* BFFF00A6, -1073807194 */
#define VI_ERROR_MACHINE_NAVAIL     (_VI_ERROR+0x3FFF00A7L) /* BFFF00A7, -1073807193 */
#define VI_ERROR_NPERMISSION        (_VI_ERROR+0x3FFF00A8L) /* BFFF00A8, -1073807192 */
#define VI_ERROR_SERVER_CERT        (_VI_ERROR+0x3FFF00B0L) /* BFFF00B0, -1073807184 */
#define VI_ERROR_SERVER_CERT_UNTRUSTED   (_VI_ERROR+0x3FFF00B1L) /* BFFF00B1, -1073807183 */
#define VI_ERROR_SERVER_CERT_EXPIRED     (_VI_ERROR+0x3FFF00B2L) /* BFFF00B2, -1073807182 */
#define VI_ERROR_SERVER_CERT_REVOKED     (_VI_ERROR+0x3FFF00B3L) /* BFFF00B3, -1073807181 */
#define VI_ERROR_SERVER_CERT_INV_SUBJECT (_VI_ERROR+0x3FFF00B4L) /* BFFF00B4, -1073807180 */
/*- Other VISA Definitions --------------------------------------------------*/
#define VI_VERSION_MAJOR(ver)       ((((ViVersion)ver) & 0xFFF00000UL) >> 20)
#define VI_VERSION_MINOR(ver)       ((((ViVersion)ver) & 0x000FFF00UL) >>  8)
#define VI_VERSION_SUBMINOR(ver)    ((((ViVersion)ver) & 0x000000FFUL)      )
#define VI_FIND_BUFLEN              (256)
#define VI_INTF_GPIB                (1)
#define VI_INTF_VXI                 (2)
#define VI_INTF_GPIB_VXI            (3)
#define VI_INTF_ASRL                (4)
#define VI_INTF_PXI                 (5)
#define VI_INTF_TCPIP               (6)
#define VI_INTF_USB                 (7)
#define VI_PROT_NORMAL              (1)
#define VI_PROT_FDC                 (2)
#define VI_PROT_HS488               (3)
#define VI_PROT_4882_STRS           (4)
#define VI_PROT_USBTMC_VENDOR       (5)
#define VI_FDC_NORMAL               (1)
#define VI_FDC_STREAM               (2)
#define VI_LOCAL_SPACE              (0)
#define VI_A16_SPACE                (1)
#define VI_A24_SPACE                (2)
#define VI_A32_SPACE                (3)
#define VI_A64_SPACE                (4)
#define VI_PXI_ALLOC_SPACE          (9)
#define VI_PXI_CFG_SPACE            (10)
#define VI_PXI_BAR0_SPACE           (11)
#define VI_PXI_BAR1_SPACE           (12)
#define VI_PXI_BAR2_SPACE           (13)
#define VI_PXI_BAR3_SPACE           (14)
#define VI_PXI_BAR4_SPACE           (15)
#define VI_PXI_BAR5_SPACE           (16)
#define VI_OPAQUE_SPACE             (0xFFFF)
#define VI_UNKNOWN_LA               (-1)
#define VI_UNKNOWN_SLOT             (-1)
#define VI_UNKNOWN_LEVEL            (-1)
#define VI_UNKNOWN_CHASSIS          (-1)
#define VI_QUEUE                    (1)
#define VI_HNDLR                    (2)
#define VI_SUSPEND_HNDLR            (4)
#define VI_ALL_MECH                 (0xFFFF)
#define VI_ANY_HNDLR                (0)
#define VI_TRIG_ALL                 (-2)
#define VI_TRIG_SW                  (-1)
#define VI_TRIG_TTL0                (0)
#define VI_TRIG_TTL1                (1)
#define VI_TRIG_TTL2                (2)
#define VI_TRIG_TTL3                (3)
#define VI_TRIG_TTL4                (4)
#define VI_TRIG_TTL5                (5)
#define VI_TRIG_TTL6                (6)
#define VI_TRIG_TTL7                (7)
#define VI_TRIG_ECL0                (8)
#define VI_TRIG_ECL1                (9)
#define VI_TRIG_ECL2                (10)
#define VI_TRIG_ECL3                (11)
#define VI_TRIG_ECL4                (12)
#define VI_TRIG_ECL5                (13)
#define VI_TRIG_STAR_SLOT1          (14)
#define VI_TRIG_STAR_SLOT2          (15)
#define VI_TRIG_STAR_SLOT3          (16)
#define VI_TRIG_STAR_SLOT4          (17)
#define VI_TRIG_STAR_SLOT5          (18)
#define VI_TRIG_STAR_SLOT6          (19)
#define VI_TRIG_STAR_SLOT7          (20)
#define VI_TRIG_STAR_SLOT8          (21)
#define VI_TRIG_STAR_SLOT9          (22)
#define VI_TRIG_STAR_SLOT10         (23)
#define VI_TRIG_STAR_SLOT11         (24)
#define VI_TRIG_STAR_SLOT12         (25)
#define VI_TRIG_STAR_INSTR          (26)
#define VI_TRIG_PANEL_IN            (27)
#define VI_TRIG_PANEL_OUT           (28)
#define VI_TRIG_STAR_VXI0           (29)
#define VI_TRIG_STAR_VXI1           (30)
#define VI_TRIG_STAR_VXI2           (31)
#define VI_TRIG_TTL8                (32)
#define VI_TRIG_TTL9                (33)
#define VI_TRIG_TTL10               (34)
#define VI_TRIG_TTL11               (35)
#define VI_TRIG_PROT_DEFAULT        (0)
#define VI_TRIG_PROT_ON             (1)
#define VI_TRIG_PROT_OFF            (2)
#define VI_TRIG_PROT_SYNC           (5)
#define VI_TRIG_PROT_RESERVE        (6)
#define VI_TRIG_PROT_UNRESERVE      (7)
#define VI_READ_BUF                 (1)
#define VI_WRITE_BUF                (2)
#define VI_READ_BUF_DISCARD         (4)
#define VI_WRITE_BUF_DISCARD        (8)
#define VI_IO_IN_BUF                (16)
#define VI_IO_OUT_BUF               (32)
#define VI_IO_IN_BUF_DISCARD        (64)
#define VI_IO_OUT_BUF_DISCARD       (128)
#define VI_FLUSH_ON_ACCESS          (1)
#define VI_FLUSH_WHEN_FULL          (2)
#define VI_FLUSH_DISABLE            (3)
#define VI_NMAPPED                  (1)
#define VI_USE_OPERS                (2)
#define VI_DEREF_ADDR               (3)
#define VI_DEREF_ADDR_BYTE_SWAP     (4)
#define VI_TMO_IMMEDIATE            (0L)
#define VI_TMO_INFINITE             (0xFFFFFFFFUL)
#define VI_NO_LOCK                  (0)
#define VI_EXCLUSIVE_LOCK           (1)
#define VI_SHARED_LOCK              (2)
#define VI_LOAD_CONFIG              (4)
#define VI_NO_SEC_ADDR              (0xFFFF)
#define VI_ASRL_PAR_NONE            (0)
#define VI_ASRL_PAR_ODD             (1)
#define VI_ASRL_PAR_EVEN            (2)
#define VI_ASRL_PAR_MARK            (3)
#define VI_ASRL_PAR_SPACE           (4)
#define VI_ASRL_STOP_ONE            (10)
#define VI_ASRL_STOP_ONE5           (15)
#define VI_ASRL_STOP_TWO            (20)
#define VI_ASRL_FLOW_NONE           (0)
#define VI_ASRL_FLOW_XON_XOFF       (1)
#define VI_ASRL_FLOW_RTS_CTS        (2)
#define VI_ASRL_FLOW_DTR_DSR        (4)
#define VI_ASRL_END_NONE            (0)
#define VI_ASRL_END_LAST_BIT        (1)
#define VI_ASRL_END_TERMCHAR        (2)
#define VI_ASRL_END_BREAK           (3)
#define VI_STATE_ASSERTED           (1)
#define VI_STATE_UNASSERTED         (0)
#define VI_STATE_UNKNOWN            (-1)
#define VI_BIG_ENDIAN               (0)
#define VI_LITTLE_ENDIAN            (1)
#define VI_DATA_PRIV                (0)
#define VI_DATA_NPRIV               (1)
#define VI_PROG_PRIV                (2)
#define VI_PROG_NPRIV               (3)
#define VI_BLCK_PRIV                (4)
#define VI_BLCK_NPRIV               (5)
#define VI_D64_PRIV                 (6)
#define VI_D64_NPRIV                (7)
#define VI_D64_2EVME                (8)
#define VI_D64_SST160               (9)
#define VI_D64_SST267               (10)
#define VI_D64_SST320               (11)
#define VI_WIDTH_8                  (1)
#define VI_WIDTH_16                 (2)
#define VI_WIDTH_32                 (4)
#define VI_WIDTH_64                 (8)
#define VI_GPIB_REN_DEASSERT        (0)
#define VI_GPIB_REN_ASSERT          (1)
#define VI_GPIB_REN_DEASSERT_GTL    (2)
#define VI_GPIB_REN_ASSERT_ADDRESS  (3)
#define VI_GPIB_REN_ASSERT_LLO      (4)
#define VI_GPIB_REN_ASSERT_ADDRESS_LLO (5)
#define VI_GPIB_REN_ADDRESS_GTL     (6)
#define VI_GPIB_ATN_DEASSERT        (0)
#define VI_GPIB_ATN_ASSERT          (1)
#define VI_GPIB_ATN_DEASSERT_HANDSHAKE (2)
#define VI_GPIB_ATN_ASSERT_IMMEDIATE (3)
#define VI_GPIB_HS488_DISABLED      (0)
#define VI_GPIB_HS488_NIMPL         (-1)
#define VI_GPIB_UNADDRESSED         (0)
#define VI_GPIB_TALKER              (1)
#define VI_GPIB_LISTENER            (2)
#define VI_VXI_CMD16                (0x0200)
#define VI_VXI_CMD16_RESP16         (0x0202)
#define VI_VXI_RESP16               (0x0002)
#define VI_VXI_CMD32                (0x0400)
#define VI_VXI_CMD32_RESP16         (0x0402)
#define VI_VXI_CMD32_RESP32         (0x0404)
#define VI_VXI_RESP32               (0x0004)
#define VI_ASSERT_SIGNAL            (-1)
#define VI_ASSERT_USE_ASSIGNED      (0)
#define VI_ASSERT_IRQ1              (1)
#define VI_ASSERT_IRQ2              (2)
#define VI_ASSERT_IRQ3              (3)
#define VI_ASSERT_IRQ4              (4)
#define VI_ASSERT_IRQ5              (5)
#define VI_ASSERT_IRQ6              (6)
#define VI_ASSERT_IRQ7              (7)
#define VI_UTIL_ASSERT_SYSRESET     (1)
#define VI_UTIL_ASSERT_SYSFAIL      (2)
#define VI_UTIL_DEASSERT_SYSFAIL    (3)
#define VI_VXI_CLASS_MEMORY         (0)
#define VI_VXI_CLASS_EXTENDED       (1)
#define VI_VXI_CLASS_MESSAGE        (2)
#define VI_VXI_CLASS_REGISTER       (3)
#define VI_VXI_CLASS_OTHER          (4)
#define VI_PXI_ADDR_NONE            (0)
#define VI_PXI_ADDR_MEM             (1)
#define VI_PXI_ADDR_IO              (2)
#define VI_PXI_ADDR_CFG             (3)
#define VI_TRIG_UNKNOWN             (-1)
#define VI_PXI_LBUS_UNKNOWN         (-1)
#define VI_PXI_LBUS_NONE            (0)
#define VI_PXI_LBUS_STAR_TRIG_BUS_0 (1000)
#define VI_PXI_LBUS_STAR_TRIG_BUS_1 (1001)
#define VI_PXI_LBUS_STAR_TRIG_BUS_2 (1002)
#define VI_PXI_LBUS_STAR_TRIG_BUS_3 (1003)
#define VI_PXI_LBUS_STAR_TRIG_BUS_4 (1004)
#define VI_PXI_LBUS_STAR_TRIG_BUS_5 (1005)
#define VI_PXI_LBUS_STAR_TRIG_BUS_6 (1006)
#define VI_PXI_LBUS_STAR_TRIG_BUS_7 (1007)
#define VI_PXI_LBUS_STAR_TRIG_BUS_8 (1008)
#define VI_PXI_LBUS_STAR_TRIG_BUS_9 (1009)
#define VI_PXI_STAR_TRIG_CONTROLLER (1413)
/*- Backward Compatibility Macros -----------------------------------------*/
#define viGetDefaultRM(vi)          viOpenDefaultRM(vi)
#define VI_ERROR_INV_SESSION        (VI_ERROR_INV_OBJECT)
#define VI_INFINITE                 (VI_TMO_INFINITE)
#define VI_NORMAL                   (VI_PROT_NORMAL)
#define VI_FDC                      (VI_PROT_FDC)
#define VI_HS488                    (VI_PROT_HS488)
#define VI_ASRL488                  (VI_PROT_4882_STRS)
#define VI_ASRL_IN_BUF              (VI_IO_IN_BUF)
#define VI_ASRL_OUT_BUF             (VI_IO_OUT_BUF)
#define VI_ASRL_IN_BUF_DISCARD      (VI_IO_IN_BUF_DISCARD)
#define VI_ASRL_OUT_BUF_DISCARD     (VI_IO_OUT_BUF_DISCARD)

/*- National Instruments ----------------------------------------------------*/

#if defined(_CVI_DEBUG_)
#pragma soft_reference (viGetAttribute);
#endif

#define VI_ERROR_HW_NGENUINE        (_VI_ERROR+0x3FFF00AAL) /* BFFF00AA, -1073807190 */

#define VI_INTF_RIO                 (8)
#define VI_INTF_FIREWIRE            (9)

#define VI_ATTR_SYNC_MXI_ALLOW_EN   (0x3FFF0161UL) /* ViBoolean, read/write */

/* This is for VXI SERVANT resources */

#define VI_EVENT_VXI_DEV_CMD        (0xBFFF200FUL)
#define VI_ATTR_VXI_DEV_CMD_TYPE    (0x3FFF4037UL) /* ViInt16, read-only */
#define VI_ATTR_VXI_DEV_CMD_VALUE   (0x3FFF4038UL) /* ViUInt32, read-only */

#define VI_VXI_DEV_CMD_TYPE_16      (16)
#define VI_VXI_DEV_CMD_TYPE_32      (32)

ViStatus _VI_FUNC viVxiServantResponse(ViSession vi, ViInt16 mode, ViUInt32 resp);
/* mode values include VI_VXI_RESP16, VI_VXI_RESP32, and the next 2 values */
#define VI_VXI_RESP_NONE            (0)
#define VI_VXI_RESP_PROT_ERROR      (-1)

/* This is for VXI TTL Trigger routing */

#define VI_ATTR_VXI_TRIG_LINES_EN   (0x3FFF4043UL)
#define VI_ATTR_VXI_TRIG_DIR        (0x3FFF4044UL)

/* This allows extended Serial support on Win32 and on NI ENET Serial products */

#define VI_ATTR_ASRL_DISCARD_NULL   (0x3FFF00B0UL)
#define VI_ATTR_ASRL_CONNECTED      (0x3FFF01BBUL)
#define VI_ATTR_ASRL_BREAK_STATE    (0x3FFF01BCUL)
#define VI_ATTR_ASRL_BREAK_LEN      (0x3FFF01BDUL)
#define VI_ATTR_ASRL_ALLOW_TRANSMIT (0x3FFF01BEUL)
#define VI_ATTR_ASRL_WIRE_MODE      (0x3FFF01BFUL)

#define VI_ASRL_WIRE_485_4          (0)
#define VI_ASRL_WIRE_485_2_DTR_ECHO (1)
#define VI_ASRL_WIRE_485_2_DTR_CTRL (2)
#define VI_ASRL_WIRE_485_2_AUTO     (3)
#define VI_ASRL_WIRE_232_DTE        (128)
#define VI_ASRL_WIRE_232_DCE        (129)
#define VI_ASRL_WIRE_232_AUTO       (130)

#define VI_EVENT_ASRL_BREAK         (0x3FFF2023UL)
#define VI_EVENT_ASRL_CTS           (0x3FFF2029UL)
#define VI_EVENT_ASRL_DSR           (0x3FFF202AUL)
#define VI_EVENT_ASRL_DCD           (0x3FFF202CUL)
#define VI_EVENT_ASRL_RI            (0x3FFF202EUL)
#define VI_EVENT_ASRL_CHAR          (0x3FFF2035UL)
#define VI_EVENT_ASRL_TERMCHAR      (0x3FFF2024UL)

/* This is for fast viPeek/viPoke macros */

#if defined(NIVISA_PEEKPOKE)

#if defined(NIVISA_PEEKPOKE_SUPP)
#undef NIVISA_PEEKPOKE_SUPP
#endif

#if (defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)) && !defined(_NI_mswin16_)
/* This macro is supported for all Win32 compilers, including CVI. */
#define NIVISA_PEEKPOKE_SUPP
#elif (defined(_WINDOWS) || defined(_Windows)) && !defined(_CVI_) && !defined(_NI_mswin16_)
/* This macro is supported for Borland and Microsoft compilers on Win16, but not CVI. */
#define NIVISA_PEEKPOKE_SUPP
#elif defined(_CVI_) && defined(_NI_sparc_)
/* This macro is supported for Solaris 1 and 2, from CVI only. */
#define NIVISA_PEEKPOKE_SUPP
#else
/* This macro is not supported on other platforms. */
#endif

#if defined(NIVISA_PEEKPOKE_SUPP)

extern ViBoolean NI_viImplVISA1;
ViStatus _VI_FUNC NI_viOpenDefaultRM (ViPSession vi);
#define viOpenDefaultRM(vi) NI_viOpenDefaultRM(vi)

#define viPeek8(vi,addr,val)                                                \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((ViPUInt8)(val)) = *((volatile ViUInt8 _VI_PTR)(addr)));     \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPeek8)((vi),(addr),(val));                                      \
      }                                                                     \
   }

#define viPoke8(vi,addr,val)                                                \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((volatile ViUInt8 _VI_PTR)(addr)) = ((ViUInt8)(val)));       \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPoke8)((vi),(addr),(val));                                      \
      }                                                                     \
   }

#define viPeek16(vi,addr,val)                                               \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((ViPUInt16)(val)) = *((volatile ViUInt16 _VI_PTR)(addr)));   \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPeek16)((vi),(addr),(val));                                     \
      }                                                                     \
   }

#define viPoke16(vi,addr,val)                                               \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((volatile ViUInt16 _VI_PTR)(addr)) = ((ViUInt16)(val)));     \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPoke16)((vi),(addr),(val));                                     \
      }                                                                     \
   }

#define viPeek32(vi,addr,val)                                               \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((ViPUInt32)(val)) = *((volatile ViUInt32 _VI_PTR)(addr)));   \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPeek32)((vi),(addr),(val));                                     \
      }                                                                     \
   }

#define viPoke32(vi,addr,val)                                               \
   {                                                                        \
      if ((NI_viImplVISA1) && (*((ViPUInt32)(vi))))                         \
      {                                                                     \
         do (*((volatile ViUInt32 _VI_PTR)(addr)) = ((ViUInt32)(val)));     \
         while (**((volatile ViUInt8 _VI_PTR _VI_PTR)(vi)) & 0x10);         \
      }                                                                     \
      else                                                                  \
      {                                                                     \
         (viPoke32)((vi),(addr),(val));                                     \
      }                                                                     \
   }

#endif

#endif

#if defined(NIVISA_PXI) || defined(PXISAVISA_PXI)

#if 0
/* The following 2 attributes were incorrectly implemented in earlier
   versions of NI-VISA.  You should now query VI_ATTR_MANF_ID or
   VI_ATTR_MODEL_CODE.  Those attributes contain sub-vendor information
   when it exists.  To get both the actual primary and subvendor codes
   from the device, you should call viIn16 using VI_PXI_CFG_SPACE. */
#define VI_ATTR_PXI_SUB_MANF_ID     (0x3FFF0203UL)
#define VI_ATTR_PXI_SUB_MODEL_CODE  (0x3FFF0204UL)
#endif

#define VI_ATTR_PXI_USE_PREALLOC_POOL  (0x3FFF020FUL)
#endif

#if defined(NIVISA_USB)

#define VI_ATTR_USB_BULK_OUT_PIPE   (0x3FFF01A2UL)
#define VI_ATTR_USB_BULK_IN_PIPE    (0x3FFF01A3UL)
#define VI_ATTR_USB_INTR_IN_PIPE    (0x3FFF01A4UL)
#define VI_ATTR_USB_CLASS           (0x3FFF01A5UL)
#define VI_ATTR_USB_SUBCLASS        (0x3FFF01A6UL)
#define VI_ATTR_USB_ALT_SETTING     (0x3FFF01A8UL)
#define VI_ATTR_USB_END_IN          (0x3FFF01A9UL)
#define VI_ATTR_USB_NUM_INTFCS      (0x3FFF01AAUL)
#define VI_ATTR_USB_NUM_PIPES       (0x3FFF01ABUL)
#define VI_ATTR_USB_BULK_OUT_STATUS (0x3FFF01ACUL)
#define VI_ATTR_USB_BULK_IN_STATUS  (0x3FFF01ADUL)
#define VI_ATTR_USB_INTR_IN_STATUS  (0x3FFF01AEUL)
#define VI_ATTR_USB_CTRL_PIPE       (0x3FFF01B0UL)

#define VI_USB_PIPE_STATE_UNKNOWN   (-1)
#define VI_USB_PIPE_READY           (0)
#define VI_USB_PIPE_STALLED         (1)

#define VI_USB_END_NONE             (0)
#define VI_USB_END_SHORT            (4)
#define VI_USB_END_SHORT_OR_COUNT   (5)

#endif

#define VI_ATTR_FIREWIRE_DEST_UPPER_OFFSET (0x3FFF01F0UL)
#define VI_ATTR_FIREWIRE_SRC_UPPER_OFFSET  (0x3FFF01F1UL)
#define VI_ATTR_FIREWIRE_WIN_UPPER_OFFSET  (0x3FFF01F2UL)
#define VI_ATTR_FIREWIRE_VENDOR_ID         (0x3FFF01F3UL)
#define VI_ATTR_FIREWIRE_LOWER_CHIP_ID     (0x3FFF01F4UL)
#define VI_ATTR_FIREWIRE_UPPER_CHIP_ID     (0x3FFF01F5UL)

#define VI_FIREWIRE_DFLT_SPACE           (5)

#if defined(__cplusplus) || defined(__cplusplus__)
   }
#endif
#endif
/*- The End -----------------------------------------------------------------*/
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/visatype.h sha256=f5bec3f6201ddc78b51de95a9e38db01ca982defa79f926a963dc2d9f7289ef9 bytes=7064 -->
## FILE: imports/include/visatype.h

- repository: `ni/grpc-device`
- source_path: `imports/include/visatype.h`
- sha256: `f5bec3f6201ddc78b51de95a9e38db01ca982defa79f926a963dc2d9f7289ef9`
- bytes: 7064

````c
/*---------------------------------------------------------------------------*/
/* Distributed by IVI Foundation Inc.                                        */
/*                                                                           */
/* Do not modify the contents of this file.                                  */
/*---------------------------------------------------------------------------*/
/*                                                                           */
/* Title   : VISATYPE.H                                                      */
/* Date    : 06-08-2017                                                      */
/* Purpose : Fundamental VISA data types and macro definitions               */
/*                                                                           */
/*---------------------------------------------------------------------------*/

/* IviVisaType.h defines the include guard of this file for backward
 * compatibility reasons. Please ensure that changes in this file are reflected
 * in IviVisaType.h when necessary.
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

#endif

/*- The End -----------------------------------------------------------------*/
````
