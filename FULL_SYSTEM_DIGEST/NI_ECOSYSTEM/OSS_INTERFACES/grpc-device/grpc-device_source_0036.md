# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/NIDAQmxInternalWaveform.h sha256=e4601674a5f421cd7e7dc61e22e8e41f95b7295a85c9ec062a5c8d1275c697f2 bytes=5097 -->
## FILE: imports/include/NIDAQmxInternalWaveform.h

- repository: `ni/grpc-device`
- source_path: `imports/include/NIDAQmxInternalWaveform.h`
- sha256: `e4601674a5f421cd7e7dc61e22e8e41f95b7295a85c9ec062a5c8d1275c697f2`
- bytes: 5097

````c
#ifndef ___nicai_NIDAQmxInternal_h___
#define ___nicai_NIDAQmxInternal_h___
#include "NIDAQmx.h"
#ifdef __cplusplus
extern "C"
{
#endif
/******************************************************/
/***                 Read Data                      ***/
/******************************************************/
#define DAQmx_Val_WfmAttrType_Bool32 1
#define DAQmx_Val_WfmAttrType_Float64 2
#define DAQmx_Val_WfmAttrType_Int32 3
#define DAQmx_Val_WfmAttrType_String 4
    // To retrieve waveform attributes, provide this optional callback:
    // - attributeName is "NI_ChannelName", "NI_UnitDescription", etc.
    // - attributeType uses the WfmAttrType enum.
    // - Boolean and numeric values are in native byte order.
    // - String values are in the encoding used by the DLL (MBCS for nicaiu.dll, UTF-8 for nicai_utf8.dll).
    // - callbackData is used to pass an object instance into the callback.
    // - The callback returns an error code.
    typedef int32(CVICALLBACK *DAQmxSetWfmAttrCallbackPtr)(uInt32 channelIndex, const char attributeName[], int32 attributeType, const void *value, uInt32 valueSizeInBytes, void *callbackData);
    // int64 t0 and dt use the same format as .NET System.DateTime and System.TimeSpan: 100 ns ticks
    // with an epoch of Jan 1, 0001. The t0 and dt arrays are optional and may be NULL.
    int32 __CFUNC DAQmxInternalReadAnalogWaveformPerChan(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, int64 t0Array[], int64 dtArray[], uInt32 timingArraySize, DAQmxSetWfmAttrCallbackPtr setWfmAttrCallback, void *setWfmAttrCallbackData, float64 *readArrayPtrs[], uInt32 readArrayCount, uInt32 arraySizeInSampsPerChan, int32 *sampsPerChanRead, bool32 *reserved);
    // DAQmxInternalReadDigitalWaveform reverses the order of lines within ports. For example,
    // DAQmxReadDigitalLines expands Dev1/port0 into Dev1/port0/line0:31 (little-endian), but
    // DAQmxInternalReadDigitalWaveform expands Dev1/port0 into Dev1/port0/line31:0 (big-endian). This
    // matches the data layout of the digital waveform datatype in LabVIEW and .NET.
    //
    // Depending on fillMode, readArray is assumed to be in the format (numChans x numSampsPerChan x
    // maxDataWidth) or (numSampsPerChan x numChans x maxDataWidth), where numChans = ReadNumChans and
    // maxDataWidth = ReadDigitalLinesBytesPerChan.
    //
    // If bytesPerChanArray is specified, this function uses it to return DINumLines[i], to enable
    // resizing waveform buffers efficiently. This function does not validate expected data widths.
    int32 __CFUNC DAQmxInternalReadDigitalWaveform(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, int64 t0Array[], int64 dtArray[], uInt32 timingArraySize, DAQmxSetWfmAttrCallbackPtr setWfmAttrCallback, void *setWfmAttrCallbackData, uInt8 readArray[], uInt32 arraySizeInBytes, int32 *sampsPerChanRead, int32 *numBytesPerSamp, uInt32 bytesPerChanArray[], uInt32 bytesPerChanArraySize, bool32 *reserved);
    /******************************************************/
    /***                 Write Data                     ***/
    /******************************************************/
    int32 __CFUNC DAQmxInternalWriteAnalogWaveformPerChan(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, const float64 *const writeArrayPtrs[], uInt32 writeArrayCount, int32 *sampsPerChanWritten, bool32 *reserved);
    // DAQmxInternalWriteDigitalWaveform reverses the order of lines within ports. See comments about
    // DAQmxInternalReadDigitalWaveform, above.
    //
    // Depending on dataLayout, writeArray is assumed to be in the format (numChans x numSampsPerChan x
    // maxDataWidth) or (numSampsPerChan x numChans x maxDataWidth), where numChans = WriteNumChans and
    // maxDataWidth = WriteDigitalLinesPerChan.
    //
    // If bytesPerChanArray is specified, this function validates expected number of channels and
    // expected data width per channel: bytesPerArraySize == WriteNumChans and bytesPerChanArray[i] ==
    // DONumLines[i]. Each channel's data must still be padded to maxDataWidth. If not specified, the
    // data is assumed to be in the correct format and no validation is performed.
    int32 __CFUNC DAQmxInternalWriteDigitalWaveform(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, const uInt8 writeArray[], const uInt32 bytesPerChanArray[], uInt32 bytesPerChanArraySize, int32 *sampsPerChanWritten, bool32 *reserved);
    
/******************************************************************************
 *** NI-DAQmx Internal Attributes *********************************************
 ******************************************************************************/
#define DAQmx_DefaultNumberOfSamplesToRead                               0x31E8 // xx Indicates the default number of samples to read per channel. This value is the same for all channels in the task.

#ifdef __cplusplus
}
#endif
#endif // ___nicai_NIDAQmxInternal_h___
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nidcpower.h sha256=06627e6ddbbf88576661082a407e52df85772fd37e079a0cc504cdfbd0ea1480 bytes=89089 -->
## FILE: imports/include/nidcpower.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nidcpower.h`
- sha256: `06627e6ddbbf88576661082a407e52df85772fd37e079a0cc504cdfbd0ea1480`
- bytes: 89089

````c
/****************************************************************************
 *              National Instruments DC Power Supplies and SMUs
 *--------------------------------------------------------------------------*
 *      Copyright (c) National Instruments 2022.  All Rights Reserved.      *
 *--------------------------------------------------------------------------*
 *
 * Title:    nidcpower.h
 * Purpose:  National Instruments DC Power Supplies and SMUs Instrument
 *           Driver declarations
 *
 ****************************************************************************/

#ifndef __NIDCPOWER_HEADER
#define __NIDCPOWER_HEADER

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <ivi.h>
#include <IviDCPwr.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

/******************************************************************************/
/*                   Instrument Driver Revision Information                   */
/******************************************************************************/
#define NIDCPOWER_MAJOR_VERSION               23     /* Instrument driver major version   */
#define NIDCPOWER_MINOR_VERSION                0     /* Instrument driver minor version   */
#define NIDCPOWER_UPDATE_VERSION               0     /* Instrument driver update version  */

#define NIDCPOWER_CLASS_SPEC_MAJOR_VERSION     3     /* Class specification major version */
#define NIDCPOWER_CLASS_SPEC_MINOR_VERSION     0     /* Class specification minor version */


/******************************************************************************/
/*                             Attribute Defines                              */
/******************************************************************************/
#define NIDCPOWER_ATTR_BASE                       IVI_SPECIFIC_PUBLIC_ATTR_BASE
#define NIDCPOWER_ATTR_PRIVATE_BASE               IVI_SPECIFIC_PRIVATE_ATTR_BASE
#define NIDCPOWER_ERROR_BASE                      IVI_SPECIFIC_ERROR_BASE
#define NIDCPOWER_WARN_BASE                       IVI_SPECIFIC_WARN_BASE

/*- User Options -*/
#define NIDCPOWER_ATTR_RANGE_CHECK                                          IVI_ATTR_RANGE_CHECK                              /* ViBoolean device */
#define NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS                              IVI_ATTR_QUERY_INSTRUMENT_STATUS                  /* ViBoolean device */
#define NIDCPOWER_ATTR_CACHE                                                IVI_ATTR_CACHE                                    /* ViBoolean device */
#define NIDCPOWER_ATTR_SIMULATE                                             IVI_ATTR_SIMULATE                                 /* ViBoolean device */
#define NIDCPOWER_ATTR_RECORD_COERCIONS                                     IVI_ATTR_RECORD_COERCIONS                         /* ViBoolean device */
#define NIDCPOWER_ATTR_INTERCHANGE_CHECK                                    IVI_ATTR_INTERCHANGE_CHECK                        /* ViBoolean device */

/*- Instrument Capabilities -*/
#define NIDCPOWER_ATTR_CHANNEL_COUNT                                        IVI_ATTR_CHANNEL_COUNT                            /* ViInt32   device  read-only */

/*- Driver Information -*/
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX                               IVI_ATTR_SPECIFIC_DRIVER_PREFIX                   /* ViString  device  read-only */
#define NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS                          IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS              /* ViString  device  read-only */
#define NIDCPOWER_ATTR_GROUP_CAPABILITIES                                   IVI_ATTR_GROUP_CAPABILITIES                       /* ViString  device  read-only */
#define NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER                              IVI_ATTR_INSTRUMENT_MANUFACTURER                  /* ViString  device  read-only */
#define NIDCPOWER_ATTR_INSTRUMENT_MODEL                                     IVI_ATTR_INSTRUMENT_MODEL                         /* ViString  device  read-only */
#define NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION                         IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION             /* ViString  device  read-only */
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION                             IVI_ATTR_SPECIFIC_DRIVER_REVISION                 /* ViString  device  read-only */
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR                               IVI_ATTR_SPECIFIC_DRIVER_VENDOR                   /* ViString  device  read-only */
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION                          IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION              /* ViString  device  read-only */
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION             IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32   device  read-only */
#define NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION             IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32   device  read-only */
#define NIDCPOWER_ATTR_SERIAL_NUMBER                                        NIDCPOWER_ATTR_BASE + 152L                        /* ViString  device  read-only */

/*- Advanced Session Information -*/
#define NIDCPOWER_ATTR_LOGICAL_NAME                                         IVI_ATTR_LOGICAL_NAME                             /* ViString  device  read-only */
#define NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR                               IVI_ATTR_IO_RESOURCE_DESCRIPTOR                   /* ViString  device  read-only */
#define NIDCPOWER_ATTR_DRIVER_SETUP                                         IVI_ATTR_DRIVER_SETUP                             /* ViString  device  read-only */

/*- Source Configuration -*/
#define NIDCPOWER_ATTR_SOURCE_MODE                                          NIDCPOWER_ATTR_BASE + 54L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_OUTPUT_FUNCTION                                      NIDCPOWER_ATTR_BASE + 8L                          /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_ENABLED                                       IVIDCPWR_ATTR_OUTPUT_ENABLED                      /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CONNECTED                                     NIDCPOWER_ATTR_BASE + 60L                         /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_RESISTANCE                                    NIDCPOWER_ATTR_BASE + 61L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_TRANSIENT_RESPONSE                                   NIDCPOWER_ATTR_BASE + 62L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH                               NIDCPOWER_ATTR_BASE + 67L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY                       NIDCPOWER_ATTR_BASE + 68L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO                              NIDCPOWER_ATTR_BASE + 69L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH                               NIDCPOWER_ATTR_BASE + 70L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY                       NIDCPOWER_ATTR_BASE + 71L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO                              NIDCPOWER_ATTR_BASE + 72L                         /* ViReal64  multi-channel */

/*- DC Voltage Output Function Configuration -*/
#define NIDCPOWER_ATTR_VOLTAGE_LEVEL                                        IVIDCPWR_ATTR_VOLTAGE_LEVEL                       /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT                                        IVIDCPWR_ATTR_CURRENT_LIMIT                       /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE                                  NIDCPOWER_ATTR_BASE + 5L                          /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE                                  NIDCPOWER_ATTR_BASE + 4L                          /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT_BEHAVIOR                               IVIDCPWR_ATTR_CURRENT_LIMIT_BEHAVIOR              /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE                              NIDCPOWER_ATTR_BASE + 15L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE                              NIDCPOWER_ATTR_BASE + 16L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH                                   NIDCPOWER_ATTR_BASE + 187L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LIMIT_LOW                                    NIDCPOWER_ATTR_BASE + 188L                        /* ViReal64  multi-channel */

/*- DC Current Output Function Configuration -*/
#define NIDCPOWER_ATTR_CURRENT_LEVEL                                        NIDCPOWER_ATTR_BASE + 9L                          /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LIMIT                                        NIDCPOWER_ATTR_BASE + 10L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE                                  NIDCPOWER_ATTR_BASE + 11L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE                                  NIDCPOWER_ATTR_BASE + 12L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE                              NIDCPOWER_ATTR_BASE + 17L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE                              NIDCPOWER_ATTR_BASE + 18L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH                                   NIDCPOWER_ATTR_BASE + 185L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW                                    NIDCPOWER_ATTR_BASE + 186L                        /* ViReal64  multi-channel */

/*- Pulse Voltage Output Function Configuration -*/
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL                                  NIDCPOWER_ATTR_BASE + 80L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT                                  NIDCPOWER_ATTR_BASE + 81L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL                             NIDCPOWER_ATTR_BASE + 82L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT                             NIDCPOWER_ATTR_BASE + 83L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE                            NIDCPOWER_ATTR_BASE + 84L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE                            NIDCPOWER_ATTR_BASE + 85L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH                             NIDCPOWER_ATTR_BASE + 193L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW                              NIDCPOWER_ATTR_BASE + 194L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH                        NIDCPOWER_ATTR_BASE + 195L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW                         NIDCPOWER_ATTR_BASE + 196L                        /* ViReal64  multi-channel */

/*- Pulse Current Output Function Configuration -*/
#define NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL                                  NIDCPOWER_ATTR_BASE + 86L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT                                  NIDCPOWER_ATTR_BASE + 87L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL                             NIDCPOWER_ATTR_BASE + 88L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT                             NIDCPOWER_ATTR_BASE + 89L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE                            NIDCPOWER_ATTR_BASE + 90L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE                            NIDCPOWER_ATTR_BASE + 91L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH                             NIDCPOWER_ATTR_BASE + 189L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW                              NIDCPOWER_ATTR_BASE + 190L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH                        NIDCPOWER_ATTR_BASE + 191L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW                         NIDCPOWER_ATTR_BASE + 192L                        /* ViReal64  multi-channel */

/*- Advanced Source Configuration -*/
#define NIDCPOWER_ATTR_SOURCE_DELAY                                         NIDCPOWER_ATTR_BASE + 51L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OVERRANGING_ENABLED                                  NIDCPOWER_ATTR_BASE + 7L                          /* ViBoolean device */
#define NIDCPOWER_ATTR_OUTPUT_CAPACITANCE                                   NIDCPOWER_ATTR_BASE + 14L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT                                  NIDCPOWER_ATTR_BASE + 25L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE                        NIDCPOWER_ATTR_BASE + 78L                         /* ViBoolean device */
#define NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY                            NIDCPOWER_ATTR_BASE + 184L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME                             NIDCPOWER_ATTR_BASE + 198L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED                     NIDCPOWER_ATTR_BASE + 199L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION                              NIDCPOWER_ATTR_BASE + 205L                        /* ViReal64  multi-channel  read-only */
#define NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION                           NIDCPOWER_ATTR_BASE + 206L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_POWER_ALLOCATION_MODE                                NIDCPOWER_ATTR_BASE + 207L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_MERGED_CHANNELS                                      NIDCPOWER_ATTR_BASE + 249L                        /* ViString  multi-channel */

/*- Advanced Pulsing Source Configuration -*/
#define NIDCPOWER_ATTR_PULSE_BIAS_DELAY                                     NIDCPOWER_ATTR_BASE + 92L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_ON_TIME                                        NIDCPOWER_ATTR_BASE + 93L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_PULSE_OFF_TIME                                       NIDCPOWER_ATTR_BASE + 94L                         /* ViReal64  multi-channel */

/*- Over Voltage Protection Configuration -*/
#define NIDCPOWER_ATTR_OVP_ENABLED                                          IVIDCPWR_ATTR_OVP_ENABLED                         /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_OVP_LIMIT                                            IVIDCPWR_ATTR_OVP_LIMIT                           /* ViReal64  multi-channel */

/*- Measurement Configuration -*/
#define NIDCPOWER_ATTR_SENSE                                                NIDCPOWER_ATTR_BASE + 13L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTO_ZERO                                            NIDCPOWER_ATTR_BASE + 55L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_APERTURE_TIME                                        NIDCPOWER_ATTR_BASE + 58L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_APERTURE_TIME_UNITS                                  NIDCPOWER_ATTR_BASE + 59L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_POWER_LINE_FREQUENCY                                 NIDCPOWER_ATTR_BASE + 20L                         /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE                                   NIDCPOWER_ATTR_BASE + 3L                          /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_FETCH_BACKLOG                                        NIDCPOWER_ATTR_BASE + 56L                         /* ViInt32   device  read-only */
#define NIDCPOWER_ATTR_AUTORANGE                                            NIDCPOWER_ATTR_BASE + 244L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE                              NIDCPOWER_ATTR_BASE + 314L                        /* ViInt32   multi-channel */

/*- Advanced Measurement Configuration -*/
#define NIDCPOWER_ATTR_MEASURE_WHEN                                         NIDCPOWER_ATTR_BASE + 57L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT                     NIDCPOWER_ATTR_BASE + 6L                          /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH                                NIDCPOWER_ATTR_BASE + 63L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE                      NIDCPOWER_ATTR_BASE + 64L                         /* ViBoolean device */
#define NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME                            NIDCPOWER_ATTR_BASE + 65L                         /* ViReal64  device  read-only */
#define NIDCPOWER_ATTR_DC_NOISE_REJECTION                                   NIDCPOWER_ATTR_BASE + 66L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE                         NIDCPOWER_ATTR_BASE + 73L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE                                  NIDCPOWER_ATTR_BASE + 77L                         /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR                                   NIDCPOWER_ATTR_BASE + 245L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE                         NIDCPOWER_ATTR_BASE + 246L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME                      NIDCPOWER_ATTR_BASE + 247L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS                NIDCPOWER_ATTR_BASE + 248L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE                      NIDCPOWER_ATTR_BASE + 255L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE                      NIDCPOWER_ATTR_BASE + 256L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE                             NIDCPOWER_ATTR_BASE + 257L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE           NIDCPOWER_ATTR_BASE + 322L                        /* ViReal64  multi-channel */

/*- Start Trigger Configuration -*/
#define NIDCPOWER_ATTR_START_TRIGGER_TYPE                                   NIDCPOWER_ATTR_BASE + 21L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE                      NIDCPOWER_ATTR_BASE + 22L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL            NIDCPOWER_ATTR_BASE + 23L                         /* ViString  device */
#define NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL               NIDCPOWER_ATTR_BASE + 24L                         /* ViString  device */

/*- Source Trigger Configuration -*/
#define NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE                                  NIDCPOWER_ATTR_BASE + 30L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE                     NIDCPOWER_ATTR_BASE + 31L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL           NIDCPOWER_ATTR_BASE + 32L                         /* ViString  device */
#define NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL              NIDCPOWER_ATTR_BASE + 33L                         /* ViString  device */

/*- Measure Trigger Configuration -*/
#define NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE                                 NIDCPOWER_ATTR_BASE + 34L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE                    NIDCPOWER_ATTR_BASE + 35L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL          NIDCPOWER_ATTR_BASE + 36L                         /* ViString  device */
#define NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL             NIDCPOWER_ATTR_BASE + 37L                         /* ViString  device */

/*- Sequence Advance Trigger Configuration -*/
#define NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE                        NIDCPOWER_ATTR_BASE + 26L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE           NIDCPOWER_ATTR_BASE + 27L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL NIDCPOWER_ATTR_BASE + 28L                         /* ViString  device */
#define NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL    NIDCPOWER_ATTR_BASE + 29L                         /* ViString  device */

/*- Source Iteration Complete Event Configuration -*/
#define NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL                NIDCPOWER_ATTR_BASE + 43L                         /* ViString  device */
#define NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY                 NIDCPOWER_ATTR_BASE + 41L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH                    NIDCPOWER_ATTR_BASE + 42L                         /* ViReal64  device */

/*- Measure Complete Event Configuration -*/
#define NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL               NIDCPOWER_ATTR_BASE + 47L                         /* ViString  device */
#define NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY                         NIDCPOWER_ATTR_BASE + 46L                         /* ViReal64  device */
#define NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY                NIDCPOWER_ATTR_BASE + 44L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH                   NIDCPOWER_ATTR_BASE + 45L                         /* ViReal64  device */

/*- Sequence Iteration Complete Event Configuration -*/
#define NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL    NIDCPOWER_ATTR_BASE + 40L                         /* ViString  device */
#define NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY     NIDCPOWER_ATTR_BASE + 38L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH        NIDCPOWER_ATTR_BASE + 39L                         /* ViReal64  device */

/*- Sequence Engine Done Event Configuration -*/
#define NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL           NIDCPOWER_ATTR_BASE + 50L                         /* ViString  device */
#define NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY            NIDCPOWER_ATTR_BASE + 48L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH               NIDCPOWER_ATTR_BASE + 49L                         /* ViReal64  device */

/*- Advanced Sequencing -*/
#define NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE                             NIDCPOWER_ATTR_BASE + 74L                         /* ViString  multi-channel */
#define NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP                        NIDCPOWER_ATTR_BASE + 75L                         /* ViInt64   multi-channel */

/*- Pulse Trigger -*/
#define NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE                                   NIDCPOWER_ATTR_BASE + 95L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE                      NIDCPOWER_ATTR_BASE + 96L                         /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL            NIDCPOWER_ATTR_BASE + 97L                         /* ViString  device */
#define NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL               NIDCPOWER_ATTR_BASE + 98L                         /* ViString  device */

/*- Pulse Complete Event Configuration -*/
#define NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL                 NIDCPOWER_ATTR_BASE + 99L                         /* ViString  device */
#define NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY                  NIDCPOWER_ATTR_BASE + 100L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH                     NIDCPOWER_ATTR_BASE + 101L                        /* ViReal64  device */

/*- Ready For Pulse Trigger Event Configuration -*/
#define NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL        NIDCPOWER_ATTR_BASE + 102L                        /* ViString  device */
#define NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY         NIDCPOWER_ATTR_BASE + 103L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH            NIDCPOWER_ATTR_BASE + 104L                        /* ViReal64  device */

/*- Shutdown Trigger Configuration -*/
#define NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE                                NIDCPOWER_ATTR_BASE + 275L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE                   NIDCPOWER_ATTR_BASE + 276L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL         NIDCPOWER_ATTR_BASE + 277L                        /* ViString  device */

/*- Interlock State -*/
#define NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN                                 NIDCPOWER_ATTR_BASE + 105L                        /* ViBoolean device  read-only */

/*- Advanced Instrument Configuration -*/
#define NIDCPOWER_ATTR_POWER_SOURCE                                         NIDCPOWER_ATTR_BASE + 0L                          /* ViInt32   device */
#define NIDCPOWER_ATTR_POWER_SOURCE_IN_USE                                  NIDCPOWER_ATTR_BASE + 1L                          /* ViInt32   device  read-only */
#define NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE                     NIDCPOWER_ATTR_BASE + 2L                          /* ViBoolean device  read-only */
#define NIDCPOWER_ATTR_ISOLATION_STATE                                      NIDCPOWER_ATTR_BASE + 302L                        /* ViInt32   multi-channel */

/*- LCR-Related Configuration -*/
#define NIDCPOWER_ATTR_INSTRUMENT_MODE                                      NIDCPOWER_ATTR_BASE + 208L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION                                NIDCPOWER_ATTR_BASE + 209L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_FREQUENCY                                        NIDCPOWER_ATTR_BASE + 210L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE                                NIDCPOWER_ATTR_BASE + 211L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE                                NIDCPOWER_ATTR_BASE + 212L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE                                   NIDCPOWER_ATTR_BASE + 213L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL                            NIDCPOWER_ATTR_BASE + 214L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL                            NIDCPOWER_ATTR_BASE + 215L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE                             NIDCPOWER_ATTR_BASE + 216L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE                                  NIDCPOWER_ATTR_BASE + 217L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME                                 NIDCPOWER_ATTR_BASE + 218L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED                        NIDCPOWER_ATTR_BASE + 220L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED                       NIDCPOWER_ATTR_BASE + 221L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED                        NIDCPOWER_ATTR_BASE + 222L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE         NIDCPOWER_ATTR_BASE + 223L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME                          NIDCPOWER_ATTR_BASE + 258L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE                                 NIDCPOWER_ATTR_BASE + 261L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE                                 NIDCPOWER_ATTR_BASE + 262L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE                                 NIDCPOWER_ATTR_BASE + 263L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_SHORT_REACTANCE                                  NIDCPOWER_ATTR_BASE + 264L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE                                    NIDCPOWER_ATTR_BASE + 265L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE                            NIDCPOWER_ATTR_BASE + 266L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_CURRENT_RANGE                                    NIDCPOWER_ATTR_BASE + 267L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE                            NIDCPOWER_ATTR_BASE + 274L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE                         NIDCPOWER_ATTR_BASE + 268L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE                          NIDCPOWER_ATTR_BASE + 269L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE                           NIDCPOWER_ATTR_BASE + 270L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE                            NIDCPOWER_ATTR_BASE + 271L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_CABLE_LENGTH                                         NIDCPOWER_ATTR_BASE + 278L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL                          NIDCPOWER_ATTR_BASE + 290L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL                  NIDCPOWER_ATTR_BASE + 291L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED          NIDCPOWER_ATTR_BASE + 299L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE                                NIDCPOWER_ATTR_BASE + 315L                        /* ViInt32   multi-channel */
#define NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE                                  NIDCPOWER_ATTR_BASE + 318L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE                                  NIDCPOWER_ATTR_BASE + 319L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE                                 NIDCPOWER_ATTR_BASE + 320L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE                           NIDCPOWER_ATTR_BASE + 321L                        /* ViInt32   multi-channel */

/*- Output Cutoff Configuration -*/
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED                                NIDCPOWER_ATTR_BASE + 235L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH              NIDCPOWER_ATTR_BASE + 236L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH             NIDCPOWER_ATTR_BASE + 237L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW               NIDCPOWER_ATTR_BASE + 238L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW               NIDCPOWER_ATTR_BASE + 239L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED              NIDCPOWER_ATTR_BASE + 240L                        /* ViBoolean multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW               NIDCPOWER_ATTR_BASE + 292L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW              NIDCPOWER_ATTR_BASE + 293L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH              NIDCPOWER_ATTR_BASE + 294L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH              NIDCPOWER_ATTR_BASE + 295L                        /* ViReal64  multi-channel */
#define NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY                                  NIDCPOWER_ATTR_BASE + 300L                        /* ViReal64  multi-channel */

/*- Auxiliary IO Configuration -*/
#define NIDCPOWER_ATTR_AUXILIARY_IO_ACTIVE_TERMINAL                         NIDCPOWER_ATTR_BASE + 331L                        /* ViString  device */
#define NIDCPOWER_ATTR_AUXILIARY_IO_BEHAVIOR                                NIDCPOWER_ATTR_BASE + 332L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_DIRECTION                          NIDCPOWER_ATTR_BASE + 333L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_POLARITY                           NIDCPOWER_ATTR_BASE + 334L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_DRIVE_MODE                         NIDCPOWER_ATTR_BASE + 335L                        /* ViInt32   device */
#define NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_PULSE_DURATION                     NIDCPOWER_ATTR_BASE + 336L                        /* ViReal64  device */

/******************************************************************************/
/*                          Attribute Value Defines                           */
/******************************************************************************/
#define NIDCPOWER_VAL_BASE                                (1000L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_CURRENT_LIMIT_BEHAVIOR -*/
#define NIDCPOWER_VAL_CURRENT_REGULATE                                                   IVIDCPWR_VAL_CURRENT_REGULATE
#define NIDCPOWER_VAL_CURRENT_TRIP                                                       IVIDCPWR_VAL_CURRENT_TRIP

/*- Defined values for RangeType parameter of function -*/
/*-   ConfigureOutputRange -*/
#define NIDCPOWER_VAL_RANGE_CURRENT                                                      IVIDCPWR_VAL_RANGE_CURRENT
#define NIDCPOWER_VAL_RANGE_VOLTAGE                                                      IVIDCPWR_VAL_RANGE_VOLTAGE

/*- Defined values for OutputState parameter of function -*/
/*-   QueryOutputState -*/
#define NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE                                            IVIDCPWR_VAL_OUTPUT_CONSTANT_VOLTAGE
#define NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT                                            IVIDCPWR_VAL_OUTPUT_CONSTANT_CURRENT
#define NIDCPOWER_VAL_OUTPUT_OVER_VOLTAGE                                                IVIDCPWR_VAL_OUTPUT_OVER_VOLTAGE
#define NIDCPOWER_VAL_OUTPUT_OVER_CURRENT                                                IVIDCPWR_VAL_OUTPUT_OVER_CURRENT
#define NIDCPOWER_VAL_OUTPUT_UNREGULATED                                                 IVIDCPWR_VAL_OUTPUT_UNREGULATED

/*- Defined values for MeasurementType parameter of function -*/
/*-   Measure -*/
#define NIDCPOWER_VAL_MEASURE_CURRENT                                                    IVIDCPWR_VAL_MEASURE_CURRENT
#define NIDCPOWER_VAL_MEASURE_VOLTAGE                                                    IVIDCPWR_VAL_MEASURE_VOLTAGE

/*- Defined values for Action parameter of function -*/
/*-   CloseExtCal -*/
#define NIDCPOWER_VAL_CANCEL                                                             (NIDCPOWER_VAL_BASE + 1L)
#define NIDCPOWER_VAL_COMMIT                                                             (NIDCPOWER_VAL_BASE + 2L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_POWER_SOURCE -*/
/*-   NIDCPOWER_ATTR_POWER_SOURCE_IN_USE -*/
#define NIDCPOWER_VAL_INTERNAL                                                           (NIDCPOWER_VAL_BASE + 3L)
#define NIDCPOWER_VAL_AUXILIARY                                                          (NIDCPOWER_VAL_BASE + 4L)
#define NIDCPOWER_VAL_AUTOMATIC                                                          (NIDCPOWER_VAL_BASE + 5L)

/*- Defined values for OutputFunction parameter of function -*/
/*-   ConfigureOutputFunction -*/
/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_OUTPUT_FUNCTION -*/
#define NIDCPOWER_VAL_DC_VOLTAGE                                                         (NIDCPOWER_VAL_BASE + 6L)
#define NIDCPOWER_VAL_DC_CURRENT                                                         (NIDCPOWER_VAL_BASE + 7L)
#define NIDCPOWER_VAL_PULSE_VOLTAGE                                                      (NIDCPOWER_VAL_BASE + 49L)
#define NIDCPOWER_VAL_PULSE_CURRENT                                                      (NIDCPOWER_VAL_BASE + 50L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_SENSE -*/
#define NIDCPOWER_VAL_LOCAL                                                              (NIDCPOWER_VAL_BASE + 8L)
#define NIDCPOWER_VAL_REMOTE                                                             (NIDCPOWER_VAL_BASE + 9L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_OUTPUT_CAPACITANCE -*/
#define NIDCPOWER_VAL_LOW                                                                (NIDCPOWER_VAL_BASE + 10L)
#define NIDCPOWER_VAL_HIGH                                                               (NIDCPOWER_VAL_BASE + 11L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_START_TRIGGER_TYPE -*/
/*-   NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE -*/
/*-   NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE -*/
/*-   NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE -*/
/*-   NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE -*/
/*-   NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE -*/
#define NIDCPOWER_VAL_NONE                                                               (NIDCPOWER_VAL_BASE + 12L)
#define NIDCPOWER_VAL_DIGITAL_EDGE                                                       (NIDCPOWER_VAL_BASE + 14L)
#define NIDCPOWER_VAL_SOFTWARE_EDGE                                                      (NIDCPOWER_VAL_BASE + 15L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE -*/
/*-   NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE -*/
#define NIDCPOWER_VAL_RISING                                                             (NIDCPOWER_VAL_BASE + 16L)
#define NIDCPOWER_VAL_FALLING                                                            (NIDCPOWER_VAL_BASE + 17L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY -*/
/*-   NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY -*/
/*-   NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY -*/
/*-   NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY -*/
/*-   NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY -*/
/*-   NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY -*/
#define NIDCPOWER_VAL_ACTIVE_HIGH                                                        (NIDCPOWER_VAL_BASE + 18L)
#define NIDCPOWER_VAL_ACTIVE_LOW                                                         (NIDCPOWER_VAL_BASE + 19L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_SOURCE_MODE -*/
#define NIDCPOWER_VAL_SINGLE_POINT                                                       (NIDCPOWER_VAL_BASE + 20L)
#define NIDCPOWER_VAL_SEQUENCE                                                           (NIDCPOWER_VAL_BASE + 21L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE -*/
/*-   NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE -*/
/*-   NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE -*/
/*-   NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE -*/
/*-   NIDCPOWER_ATTR_AUTO_ZERO -*/
/*-   NIDCPOWER_ATTR_AUTORANGE -*/
/*-   NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL -*/
/*-   NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL -*/
#define NIDCPOWER_VAL_OFF                                                                (0L)
#define NIDCPOWER_VAL_ONCE                                                               (NIDCPOWER_VAL_BASE + 24L)
#define NIDCPOWER_VAL_ON                                                                 (1L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_MEASURE_WHEN -*/
#define NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE                                (NIDCPOWER_VAL_BASE + 25L)
#define NIDCPOWER_VAL_ON_DEMAND                                                          (NIDCPOWER_VAL_BASE + 26L)
#define NIDCPOWER_VAL_ON_MEASURE_TRIGGER                                                 (NIDCPOWER_VAL_BASE + 27L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_POWER_LINE_FREQUENCY -*/
#define NIDCPOWER_VAL_50_HERTZ                                                           (50.0)
#define NIDCPOWER_VAL_60_HERTZ                                                           (60.0)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_APERTURE_TIME_UNITS -*/
/*-   NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS -*/
#define NIDCPOWER_VAL_SECONDS                                                            (NIDCPOWER_VAL_BASE + 28L)
#define NIDCPOWER_VAL_POWER_LINE_CYCLES                                                  (NIDCPOWER_VAL_BASE + 29L)

/*- Defined values for Signal parameter of function -*/
/*-   ExportSignal -*/
#define NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT                                              (NIDCPOWER_VAL_BASE + 30L)
#define NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT                                             (NIDCPOWER_VAL_BASE + 31L)
#define NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT                                  (NIDCPOWER_VAL_BASE + 32L)
#define NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT                                         (NIDCPOWER_VAL_BASE + 33L)
#define NIDCPOWER_VAL_PULSE_COMPLETE_EVENT                                               (NIDCPOWER_VAL_BASE + 51L)
#define NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT                                      (NIDCPOWER_VAL_BASE + 52L)
#define NIDCPOWER_VAL_START_TRIGGER                                                      (NIDCPOWER_VAL_BASE + 34L)
#define NIDCPOWER_VAL_SOURCE_TRIGGER                                                     (NIDCPOWER_VAL_BASE + 35L)
#define NIDCPOWER_VAL_MEASURE_TRIGGER                                                    (NIDCPOWER_VAL_BASE + 36L)
#define NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER                                           (NIDCPOWER_VAL_BASE + 37L)
#define NIDCPOWER_VAL_PULSE_TRIGGER                                                      (NIDCPOWER_VAL_BASE + 53L)
#define NIDCPOWER_VAL_SHUTDOWN_TRIGGER                                                   (NIDCPOWER_VAL_BASE + 118L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_TRANSIENT_RESPONSE -*/
#define NIDCPOWER_VAL_NORMAL                                                             (NIDCPOWER_VAL_BASE + 38L)
#define NIDCPOWER_VAL_FAST                                                               (NIDCPOWER_VAL_BASE + 39L)
#define NIDCPOWER_VAL_SLOW                                                               (NIDCPOWER_VAL_BASE + 41L)
#define NIDCPOWER_VAL_CUSTOM                                                             (NIDCPOWER_VAL_BASE + 42L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_DC_NOISE_REJECTION -*/
#define NIDCPOWER_VAL_DC_NOISE_REJECTION_NORMAL                                          (NIDCPOWER_VAL_BASE + 44L)
#define NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER                                    (NIDCPOWER_VAL_BASE + 43L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE -*/
#define NIDCPOWER_VAL_KEEP_IN_MEMORY                                                     (NIDCPOWER_VAL_BASE + 45L)
#define NIDCPOWER_VAL_WRITE_TO_EEPROM                                                    (NIDCPOWER_VAL_BASE + 46L)

/*- Defined values for InternalReference parameter of function -*/
/*-   ConnectInternalReference, CalAdjustInternalReference -*/
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_5V                                              (NIDCPOWER_VAL_BASE + 54L)
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM                                         (NIDCPOWER_VAL_BASE + 55L)
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_GROUND                                          (NIDCPOWER_VAL_BASE + 56L)
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_NONE                                            (NIDCPOWER_VAL_BASE + 57L)
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_7V                                              (NIDCPOWER_VAL_BASE + 119L)
#define NIDCPOWER_VAL_INTERNAL_REFERENCE_1KOHM                                           (NIDCPOWER_VAL_BASE + 120L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY -*/
#define NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC                                (0L)
#define NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_ASYMMETRIC                               (1L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_POWER_ALLOCATION_MODE -*/
#define NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED                                     (NIDCPOWER_VAL_BASE + 58L)
#define NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC                                    (NIDCPOWER_VAL_BASE + 59L)
#define NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL                                       (NIDCPOWER_VAL_BASE + 60L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_INSTRUMENT_MODE -*/
#define NIDCPOWER_VAL_SMU_PS                                                             (NIDCPOWER_VAL_BASE + 61L)
#define NIDCPOWER_VAL_LCR                                                                (NIDCPOWER_VAL_BASE + 62L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION -*/
#define NIDCPOWER_VAL_AC_VOLTAGE                                                         (NIDCPOWER_VAL_BASE + 63L)
#define NIDCPOWER_VAL_AC_CURRENT                                                         (NIDCPOWER_VAL_BASE + 64L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE -*/
#define NIDCPOWER_VAL_DC_BIAS_OFF                                                        (NIDCPOWER_VAL_BASE + 65L)
#define NIDCPOWER_VAL_DC_BIAS_VOLTAGE                                                    (NIDCPOWER_VAL_BASE + 66L)
#define NIDCPOWER_VAL_DC_BIAS_CURRENT                                                    (NIDCPOWER_VAL_BASE + 67L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE -*/
#define NIDCPOWER_VAL_AUTO_RANGE_OFF                                                     (NIDCPOWER_VAL_BASE + 68L)
#define NIDCPOWER_VAL_AUTO_RANGE_ON                                                      (NIDCPOWER_VAL_BASE + 70L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME -*/
#define NIDCPOWER_VAL_MEASUREMENT_TIME_SHORT                                             (NIDCPOWER_VAL_BASE + 71L)
#define NIDCPOWER_VAL_MEASUREMENT_TIME_MEDIUM                                            (NIDCPOWER_VAL_BASE + 72L)
#define NIDCPOWER_VAL_MEASUREMENT_TIME_LONG                                              (NIDCPOWER_VAL_BASE + 73L)
#define NIDCPOWER_VAL_MEASUREMENT_TIME_CUSTOM                                            (NIDCPOWER_VAL_BASE + 117L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE -*/
#define NIDCPOWER_VAL_ONBOARD_STORAGE                                                    (NIDCPOWER_VAL_BASE + 74L)
#define NIDCPOWER_VAL_AS_DEFINED                                                         (NIDCPOWER_VAL_BASE + 75L)
#define NIDCPOWER_VAL_AS_CONFIGURED                                                      (NIDCPOWER_VAL_BASE + 146L)

/*- Defined values for LCRReferenceValueType values -*/
#define NIDCPOWER_VAL_LCR_LOAD_COMPENSATION_SPOT_REFERENCE_VALUE_TYPE_IMPEDANCE          (NIDCPOWER_VAL_BASE + 76L)
#define NIDCPOWER_VAL_LCR_LOAD_COMPENSATION_SPOT_REFERENCE_VALUE_TYPE_IDEAL_CAPACITANCE  (NIDCPOWER_VAL_BASE + 77L)
#define NIDCPOWER_VAL_LCR_LOAD_COMPENSATION_SPOT_REFERENCE_VALUE_TYPE_IDEAL_INDUCTANCE   (NIDCPOWER_VAL_BASE + 78L)
#define NIDCPOWER_VAL_LCR_LOAD_COMPENSATION_SPOT_REFERENCE_VALUE_TYPE_IDEAL_RESISTANCE   (NIDCPOWER_VAL_BASE + 79L)

/*- Defined values for OutputCutoffReason values -*/
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL                                           (-1L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH                           (1L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW                            (2L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH                          (4L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW                           (8L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH                           (16L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW                            (32L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH                           (64L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW                            (128L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_SATURATED                             (256L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_SATURATED                             (512L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_HIGH                          (1024L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_LOW                           (2048L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_HIGH                    (4096L)
#define NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_LOW                     (8192L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR -*/
#define NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN                                        (NIDCPOWER_VAL_BASE + 107L)
#define NIDCPOWER_VAL_RANGE_UP                                                           (NIDCPOWER_VAL_BASE + 108L)
#define NIDCPOWER_VAL_RANGE_UP_AND_DOWN                                                  (NIDCPOWER_VAL_BASE + 109L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE -*/
#define NIDCPOWER_VAL_APERTURE_TIME_AUTO                                                 (NIDCPOWER_VAL_BASE + 110L)
#define NIDCPOWER_VAL_APERTURE_TIME_CUSTOM                                               (NIDCPOWER_VAL_BASE + 111L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE -*/
#define NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL                                              (NIDCPOWER_VAL_BASE + 112L)
#define NIDCPOWER_VAL_THRESHOLD_MODE_FAST_STEP                                           (NIDCPOWER_VAL_BASE + 113L)
#define NIDCPOWER_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS                                     (NIDCPOWER_VAL_BASE + 114L)
#define NIDCPOWER_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS                                   (NIDCPOWER_VAL_BASE + 115L)
#define NIDCPOWER_VAL_THRESHOLD_MODE_HOLD                                                (NIDCPOWER_VAL_BASE + 116L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_CABLE_LENGTH -*/
#define NIDCPOWER_VAL_ZERO_M                                                             (NIDCPOWER_VAL_BASE + 121L)
#define NIDCPOWER_VAL_NI_STANDARD_1M                                                     (NIDCPOWER_VAL_BASE + 122L)
#define NIDCPOWER_VAL_NI_STANDARD_2M                                                     (NIDCPOWER_VAL_BASE + 123L)
#define NIDCPOWER_VAL_NI_STANDARD_4M                                                     (NIDCPOWER_VAL_BASE + 124L)
#define NIDCPOWER_VAL_CUSTOM_ONBOARD_STORAGE                                             (NIDCPOWER_VAL_BASE + 125L)
#define NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED                                               (NIDCPOWER_VAL_BASE + 126L)
#define NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_1M                                            (NIDCPOWER_VAL_BASE + 139L)
#define NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_2M                                            (NIDCPOWER_VAL_BASE + 140L)
#define NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_4M                                            (NIDCPOWER_VAL_BASE + 141L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_ISOLATION_STATE -*/
#define NIDCPOWER_VAL_ISOLATED                                                           (NIDCPOWER_VAL_BASE + 128L)
#define NIDCPOWER_VAL_NON_ISOLATED                                                       (NIDCPOWER_VAL_BASE + 129L)

/*- Defined values for LCRCompensationType values -*/
#define NIDCPOWER_VAL_OPEN_COMPENSATION                                                  (NIDCPOWER_VAL_BASE + 130L)
#define NIDCPOWER_VAL_SHORT_COMPENSATION                                                 (NIDCPOWER_VAL_BASE + 131L)
#define NIDCPOWER_VAL_LOAD_COMPENSATION                                                  (NIDCPOWER_VAL_BASE + 132L)
#define NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION                                     (NIDCPOWER_VAL_BASE + 133L)
#define NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION                                    (NIDCPOWER_VAL_BASE + 134L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE -*/
#define NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_OFF                                        (NIDCPOWER_VAL_BASE + 135L)
#define NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_SHORT                                      (NIDCPOWER_VAL_BASE + 136L)
#define NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_NORMAL                                     (NIDCPOWER_VAL_BASE + 137L)
#define NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_LONG                                       (NIDCPOWER_VAL_BASE + 138L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE -*/
#define NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC                                    (NIDCPOWER_VAL_BASE + 144L)
#define NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_MANUAL                                       (NIDCPOWER_VAL_BASE + 145L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE -*/
#define NIDCPOWER_VAL_LCR_IMPEDANCE_RANGE                                                (NIDCPOWER_VAL_BASE + 142L)
#define NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION                                             (NIDCPOWER_VAL_BASE + 143L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUXILIARY_IO_BEHAVIOR -*/
#define NIDCPOWER_VAL_AUXILIARY_IO_OFF                                                   (NIDCPOWER_VAL_BASE + 147L)
#define NIDCPOWER_VAL_AUXILIARY_IO_SIGNAL_ROUTING                                        (NIDCPOWER_VAL_BASE + 148L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO                                                  (NIDCPOWER_VAL_BASE + 149L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_DIRECTION -*/
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_INPUT                                            (NIDCPOWER_VAL_BASE + 150L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_OUTPUT                                           (NIDCPOWER_VAL_BASE + 151L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_POLARITY -*/
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_ACTIVE_HIGH                                      (NIDCPOWER_VAL_BASE + 152L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_ACTIVE_LOW                                       (NIDCPOWER_VAL_BASE + 153L)

/*- Defined values for attributes -*/
/*-   NIDCPOWER_ATTR_AUXILIARY_IO_GPIO_DRIVE_MODE -*/
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_PUSH_PULL                                        (NIDCPOWER_VAL_BASE + 154L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_OPEN_DRAIN                                       (NIDCPOWER_VAL_BASE + 155L)

/*- Defined values for AuxiliaryIoGpioState values -*/
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_INACTIVE                                         (NIDCPOWER_VAL_BASE + 156L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_ACTIVE                                           (NIDCPOWER_VAL_BASE + 157L)
#define NIDCPOWER_VAL_AUXILIARY_IO_GPIO_PULSE                                            (NIDCPOWER_VAL_BASE + 158L)

/******************************************************************************/
/*                    Instrument Driver Type Declarations                     */
/******************************************************************************/

#if !defined(_NIComplexNumber)
#define _NIComplexNumber
   typedef struct NIComplexNumber_struct
   {
      ViReal64 real;
      ViReal64 imaginary;
   } NIComplexNumber;
#endif

#if !defined(_NILCRMeasurement)
#define _NILCRMeasurement
#pragma pack(push,8)
   typedef struct NILCRMeasurement_struct
   {
      // DcBias values
      ViReal64 Vdc;
      ViReal64 Idc;

      // Stimulus frequency
      ViReal64 stimulusFrequency;

      // Raw measurements
      NIComplexNumber ACVoltage;
      NIComplexNumber ACCurrent;

      // Z values
      NIComplexNumber Z;
      ViReal64 ZMagnitude;
      ViReal64 ZPhase; // degrees

      // Y values
      NIComplexNumber Y;
      ViReal64 YMagnitude;
      ViReal64 YPhase; // degrees

      // Series model values
      ViReal64 Ls;
      ViReal64 Cs;
      ViReal64 Rs;

      // Parallel model values
      ViReal64 Lp;
      ViReal64 Cp;
      ViReal64 Rp;

      // Dissipation factor & Q factor
      ViReal64 D;
      ViReal64 Q;

      // Measurement metadata
      ViUInt16 measurementMode;
      ViBoolean dcInCompliance;
      ViBoolean acInCompliance;
      ViBoolean unbalanced;

      // Reserved for future use
      ViReal64 reserved1;
      ViReal64 reserved2;
      ViReal64 reserved3;
      ViReal64 reserved4;
      ViReal64 reserved5;
      ViReal64 reserved6;
      ViReal64 reserved7;
   } NILCRMeasurement;
#pragma pack(pop)
#endif

#if !defined(_NILCRLoadCompensationSpot)
#define _NILCRLoadCompensationSpot
#if defined(_WIN64)
#pragma pack(push,8)
#elif defined(__linux__) || defined(__APPLE__)
#pragma pack(push,4)
#else
#pragma pack(push,1)
#endif
   typedef struct NILCRLoadCompensationSpot_struct
   {
      ViReal64 frequency;
      ViInt32 referenceValueType;
      ViReal64 referenceValueA;
      ViReal64 referenceValueB;
   } NILCRLoadCompensationSpot;
#pragma pack(pop)
#endif

/******************************************************************************/
/*                  Instrument Driver Function Declarations                   */
/******************************************************************************/

   /*- Initialize and Close Functions -*/
   ViStatus _VI_FUNC niDCPower_InitializeWithChannels(
      ViRsrc resourceName,
      ViConstString channels,
      ViBoolean reset,
      ViConstString optionString,
      ViSession *vi);

   ViStatus _VI_FUNC niDCPower_InitializeWithIndependentChannels(
      ViRsrc resourceName,
      ViBoolean reset,
      ViConstString optionString,
      ViSession *vi);

   ViStatus _VI_FUNC niDCPower_close(
      ViSession vi);

   /*- Source -*/
   ViStatus _VI_FUNC niDCPower_ConfigureSourceMode(
      ViSession vi,
      ViInt32 sourceMode);

   ViStatus _VI_FUNC niDCPower_ConfigureSourceModeWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViInt32 sourceMode);

   ViStatus _VI_FUNC niDCPower_ConfigureOutputFunction(
      ViSession vi,
      ViConstString channelName,
      ViInt32 outputFunction);

   ViStatus _VI_FUNC niDCPower_ConfigureOutputEnabled(
      ViSession vi,
      ViConstString channelName,
      ViBoolean enabled);

   ViStatus _VI_FUNC niDCPower_SetSequence(
      ViSession vi,
      ViConstString channelName,
      const ViReal64 values[],
      const ViReal64 sourceDelays[],
      ViUInt32 size);

   /*- DC Voltage -*/
   ViStatus _VI_FUNC niDCPower_ConfigureVoltageLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigureCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViInt32 behavior,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigureVoltageLevelRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   ViStatus _VI_FUNC niDCPower_ConfigureCurrentLimitRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   ViStatus _VI_FUNC niDCPower_ConfigureOutputResistance(
      ViSession vi,
      ViConstString channelName,
      ViReal64 resistance);

   /*- DC Current -*/
   ViStatus _VI_FUNC niDCPower_ConfigureCurrentLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigureCurrentLevelRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   ViStatus _VI_FUNC niDCPower_ConfigureVoltageLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigureVoltageLimitRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   /*- Pulse Voltage -*/
   ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasVoltageLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevelRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLimitRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   /*- Pulse Current -*/
   ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasCurrentLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 level);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasVoltageLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 limit);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLevelRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLimitRange(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range);

   /*- Advanced Sequencing */
   ViStatus _VI_FUNC niDCPower_CreateAdvancedSequence(
      ViSession vi,
      ViConstString sequenceName,
      ViInt32 attributeIDCount,
      const ViInt32 attributeIDs[],
      ViBoolean setAsActiveSequence);

   ViStatus _VI_FUNC niDCPower_CreateAdvancedSequenceWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString sequenceName,
      ViInt32 attributeIDCount,
      const ViInt32 attributeIDs[],
      ViBoolean setAsActiveSequence);

   ViStatus _VI_FUNC niDCPower_CreateAdvancedSequenceStep(
      ViSession vi,
      ViBoolean setAsActiveStep);

   ViStatus _VI_FUNC niDCPower_CreateAdvancedSequenceStepWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViBoolean setAsActiveStep);

   ViStatus _VI_FUNC niDCPower_CreateAdvancedSequenceCommitStepWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViBoolean setAsActiveStep);

   ViStatus _VI_FUNC niDCPower_DeleteAdvancedSequence(
      ViSession vi,
      ViConstString sequenceName);

   ViStatus _VI_FUNC niDCPower_DeleteAdvancedSequenceWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString sequenceName);

   /*- Measure */
   ViStatus _VI_FUNC niDCPower_ConfigureApertureTime(
      ViSession vi,
      ViConstString channelName,
      ViReal64 apertureTime,
      ViInt32 units);

   ViStatus _VI_FUNC niDCPower_ConfigureAutoZero(
      ViSession vi,
      ViConstString channelName,
      ViInt32 autoZero);

   ViStatus _VI_FUNC niDCPower_ConfigurePowerLineFrequency(
      ViSession vi,
      ViReal64 powerLineFrequency);

   ViStatus _VI_FUNC niDCPower_ConfigureSense(
      ViSession vi,
      ViConstString channelName,
      ViInt32 sense);

   ViStatus _VI_FUNC niDCPower_Measure(
      ViSession vi,
      ViConstString channelName,
      ViInt32 measurementType,
      ViReal64* measurement);

   ViStatus _VI_FUNC niDCPower_MeasureMultiple(
      ViSession vi,
      ViConstString channelName,
      ViReal64 voltageMeasurements[],
      ViReal64 currentMeasurements[]);

   ViStatus _VI_FUNC niDCPower_FetchMultiple(
      ViSession vi,
      ViConstString channelName,
      ViReal64 timeout,
      ViInt32 count,
      ViReal64 voltageMeasurements[],
      ViReal64 currentMeasurements[],
      ViBoolean inCompliance[],
      ViInt32* actualCount);

   ViStatus _VI_FUNC niDCPower_MeasureMultipleLCR(
      ViSession vi,
      ViConstString channelName,
      NILCRMeasurement measurements[]);

   ViStatus _VI_FUNC niDCPower_FetchMultipleLCR(
      ViSession vi,
      ViConstString channelName,
      ViReal64 timeout,
      ViInt32 count,
      NILCRMeasurement measurements[],
      ViInt32* actualCount);

   ViStatus _VI_FUNC niDCPower_QueryInCompliance(
      ViSession vi,
      ViConstString channelName,
      ViBoolean *inCompliance);

   ViStatus _VI_FUNC niDCPower_QueryOutputState(
      ViSession vi,
      ViConstString channelName,
      ViInt32 outputState,
      ViBoolean* inState);

   ViStatus _VI_FUNC niDCPower_QueryLatchedOutputCutoffState(
      ViSession vi,
      ViConstString channelName,
      ViInt32 outputCutoffReason,
      ViBoolean* outputCutoffState);

   ViStatus _VI_FUNC niDCPower_ClearLatchedOutputCutoffState(
      ViSession vi,
      ViConstString channelName,
      ViInt32 outputCutoffReason);

   /*- Control -*/
   ViStatus _VI_FUNC niDCPower_Commit(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_CommitWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_Initiate(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_InitiateWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_Abort(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_AbortWithChannels(
      ViSession vi,
      ViConstString channelName);

   /*- Query -*/
   ViStatus _VI_FUNC niDCPower_QueryMaxCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 voltageLevel,
      ViReal64* maxCurrentLimit);

   ViStatus _VI_FUNC niDCPower_QueryMaxVoltageLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 currentLimit,
      ViReal64* maxVoltageLevel);

   ViStatus _VI_FUNC niDCPower_QueryMinCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 voltageLevel,
      ViReal64* minCurrentLimit);

   /*- Calibration Functions -*/
   ViStatus _VI_FUNC niDCPower_InitExtCal(
      ViRsrc resourceName,
      ViConstString password,
      ViSession *vi);

   ViStatus _VI_FUNC niDCPower_CloseExtCal(
      ViSession vi,
      ViInt32 action);

   ViStatus _VI_FUNC niDCPower_CalAdjustVoltageLevel(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range,
      ViUInt32 numberOfMeasurements,
      const ViReal64 requestedOutputs[],
      const ViReal64 measuredOutputs[]);

   ViStatus _VI_FUNC niDCPower_CalAdjustVoltageMeasurement(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range,
      ViUInt32 numberOfMeasurements,
      const ViReal64 reportedOutputs[],
      const ViReal64 measuredOutputs[]);

   ViStatus _VI_FUNC niDCPower_CalAdjustCurrentLimit(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range,
      ViUInt32 numberOfMeasurements,
      const ViReal64 requestedOutputs[],
      const ViReal64 measuredOutputs[]);

   ViStatus _VI_FUNC niDCPower_CalAdjustCurrentMeasurement(
      ViSession vi,
      ViConstString channelName,
      ViReal64 range,
      ViUInt32 numberOfMeasurements,
      const ViReal64 reportedOutputs[],
      const ViReal64 measuredOutputs[]);

   ViStatus _VI_FUNC niDCPower_CalAdjustOutputResistance(
      ViSession vi,
      ViConstString channelName,
      ViUInt32 numberOfValues,
      const ViReal64 requestedOutputs[],
      const ViReal64 measuredOutputs[]);

   ViStatus _VI_FUNC niDCPower_CalAdjustResidualVoltageOffset(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_CalAdjustResidualCurrentOffset(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConnectInternalReference(
      ViSession vi,
      ViInt32 internalReference);

   ViStatus _VI_FUNC niDCPower_CalAdjustInternalReference(
      ViSession vi,
      ViInt32 internalReference,
      ViReal64 internalReferenceValue);

   ViStatus _VI_FUNC niDCPower_CalBeginACFlatness(
      ViSession vi,
      ViConstString channelName,
      ViUInt32* totalNumberOfSteps);

   ViStatus _VI_FUNC niDCPower_CalConfigACFlatness(
      ViSession vi,
      ViConstString channelName,
      ViReal64* generatedFrequency,
      ViReal64* generatedVoltageRMS);

   ViStatus _VI_FUNC niDCPower_CalAdjustACFlatness(
      ViSession vi,
      ViConstString channelName,
      ViReal64 generatedFrequency,
      ViReal64 generatedVoltageRMS,
      ViReal64 measuredVoltageRMS,
      ViUInt32* numberOfStepsRemaining);

   ViStatus _VI_FUNC niDCPower_CalEndACFlatness(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_CalAdjustACImpedanceReference(
      ViSession vi,
      ViConstString channelName,
      ViReal64 actualResistance,
      ViInt32 cableLength);

   ViStatus _VI_FUNC niDCPower_CalSelfCalibrate(
      ViSession vi,
      ViConstString channelName);

   /*- Calibration Utility Functions -*/
   ViStatus _VI_FUNC niDCPower_ChangeExtCalPassword(
      ViSession vi,
      ViConstString oldPassword,
      ViConstString newPassword);

   ViStatus _VI_FUNC niDCPower_GetExtCalRecommendedInterval(
      ViSession vi,
      ViInt32* months);

   ViStatus _VI_FUNC niDCPower_GetExtCalLastDateAndTime(
      ViSession vi,
      ViInt32* year,
      ViInt32* month,
      ViInt32* day,
      ViInt32* hour,
      ViInt32* minute);

   ViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfoMaxSize(
      ViSession vi,
      ViInt32* infoSize);

   ViStatus _VI_FUNC niDCPower_SetCalUserDefinedInfo(
      ViSession vi,
      ViConstString info);

   ViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfo(
      ViSession vi,
      ViString info);

   ViStatus _VI_FUNC niDCPower_ReadCurrentTemperature(
      ViSession vi,
      ViReal64* temperature);

   ViStatus _VI_FUNC niDCPower_GetExtCalLastTemp(
      ViSession vi,
      ViReal64* temperature);

   ViStatus _VI_FUNC niDCPower_GetSelfCalLastDateAndTime(
      ViSession vi,
      ViInt32* year,
      ViInt32* month,
      ViInt32* day,
      ViInt32* hour,
      ViInt32* minute);

   ViStatus _VI_FUNC niDCPower_GetSelfCalLastTemp(
      ViSession vi,
      ViReal64* temperature);

   ViStatus _VI_FUNC niDCPower_GetLCRCompensationLastDateAndTime(
      ViSession vi,
      ViConstString channelName,
      ViInt32 compensationType,
      ViInt32* year,
      ViInt32* month,
      ViInt32* day,
      ViInt32* hour,
      ViInt32* minute);

   /*- Triggers and Events Functions -*/
   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTrigger(
      ViSession vi,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeStartTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_DisableStartTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_DisableStartTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(
      ViSession vi,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_DisableSequenceAdvanceTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_DisableSequenceAdvanceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeSourceTrigger(
      ViSession vi,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeSourceTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_DisableSourceTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_DisableSourceTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeMeasureTrigger(
      ViSession vi,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeMeasureTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgePulseTrigger(
      ViSession vi,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgePulseTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_DisablePulseTrigger(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_DisablePulseTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeShutdownTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViConstString inputTerminal,
      ViInt32 edge);

   ViStatus _VI_FUNC niDCPower_ConfigureSoftwareEdgeShutdownTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_DisableShutdownTriggerWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ExportSignal(
      ViSession vi,
      ViInt32 signal,
      ViConstString signalIdentifier,
      ViConstString outputTerminal);

   ViStatus _VI_FUNC niDCPower_ExportSignalWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViInt32 signal,
      ViConstString signalIdentifier,
      ViConstString outputTerminal);

   ViStatus _VI_FUNC niDCPower_SendSoftwareEdgeTrigger(
      ViSession vi,
      ViInt32 trigger);

   ViStatus _VI_FUNC niDCPower_SendSoftwareEdgeTriggerWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViInt32 trigger);

   ViStatus _VI_FUNC niDCPower_WaitForEvent(
      ViSession vi,
      ViInt32 eventId,
      ViReal64 timeout);

   ViStatus _VI_FUNC niDCPower_WaitForEventWithChannels(
      ViSession vi,
      ViConstString channelName,
      ViInt32 eventId,
      ViReal64 timeout);

   /*- Utility Functions -*/
   ViStatus _VI_FUNC niDCPower_Disable(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_reset(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ResetWithChannels(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_ResetDevice(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_self_test(
      ViSession vi,
      ViInt16 *testResult,
      ViChar testMessage[]);

   /*- Other IVI Utility Functions -*/
   ViStatus _VI_FUNC niDCPower_revision_query(
      ViSession vi,
      ViChar instrumentDriverRevision[],
      ViChar firmwareRevision[]);

   ViStatus _VI_FUNC niDCPower_ResetWithDefaults(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_GetChannelName(
      ViSession vi,
      ViInt32 index,
      ViInt32 bufferSize,
      ViChar name[]);

   ViStatus _VI_FUNC niDCPower_GetChannelNameFromString(
      ViSession vi,
      ViConstString index,
      ViInt32 bufferSize,
      ViChar name[]);

   ViStatus _VI_FUNC niDCPower_GetNextCoercionRecord(
      ViSession vi,
      ViInt32 bufferSize,
      ViChar record[]);

   ViStatus _VI_FUNC niDCPower_ClearInterchangeWarnings(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ResetInterchangeCheck(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_GetNextInterchangeWarning(
      ViSession vi,
      ViInt32 bufferSize,
      ViChar warnString[]);

   ViStatus _VI_FUNC niDCPower_InvalidateAllAttributes(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_ConfigureOVP(
      ViSession vi,
      ViConstString channelName,
      ViBoolean enabled,
      ViReal64 limit);

      /*- Error Info Utility Functions -*/
   ViStatus _VI_FUNC niDCPower_GetError(
      ViSession vi, ViStatus *errorCode,
      ViInt32 bufferSize,
      ViChar description[]);

   ViStatus _VI_FUNC niDCPower_ClearError(
      ViSession vi);

   ViStatus _VI_FUNC niDCPower_error_message(
      ViSession vi,
      ViStatus errorCode,
      ViChar errorMessage[256]);

   ViStatus _VI_FUNC niDCPower_error_query(
      ViSession vi,
      ViInt32 *errorCode,
      ViChar errorMessage[]);

      /*- Locking Utility Functions -*/
   ViStatus _VI_FUNC niDCPower_LockSession(
      ViSession vi,
      ViBoolean *callerHasLock);

   ViStatus _VI_FUNC niDCPower_UnlockSession(
      ViSession vi,
      ViBoolean *callerHasLock);

   /*- Set and Get Attribute Functions -*/
   ViStatus _VI_FUNC niDCPower_SetAttributeViInt32(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViInt32 value);

   ViStatus _VI_FUNC niDCPower_SetAttributeViInt64(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViInt64 value);

   ViStatus _VI_FUNC niDCPower_SetAttributeViReal64(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViReal64 value);

   ViStatus _VI_FUNC niDCPower_SetAttributeViString(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViConstString value);

   ViStatus _VI_FUNC niDCPower_SetAttributeViSession(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViSession value);

   ViStatus _VI_FUNC niDCPower_SetAttributeViBoolean(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViBoolean value);

   ViStatus _VI_FUNC niDCPower_GetAttributeViInt32(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViInt32 *value);

   ViStatus _VI_FUNC niDCPower_GetAttributeViInt64(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViInt64 *value);

   ViStatus _VI_FUNC niDCPower_GetAttributeViReal64(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViReal64 *value);

   ViStatus _VI_FUNC niDCPower_GetAttributeViString(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViInt32 bufSize,
      ViChar value[]);

   ViStatus _VI_FUNC niDCPower_GetAttributeViSession(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViSession *value);

   ViStatus _VI_FUNC niDCPower_GetAttributeViBoolean(
      ViSession vi,
      ViConstString channelName,
      ViAttr attribute,
      ViBoolean *value);

   /*- Import and Export Attribute Configuration Functions -*/
   ViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationFile(
      ViSession vi,
      ViConstString filePath);

   ViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationFile(
      ViSession vi,
      ViConstString filePath);

   ViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationBuffer(
      ViSession vi,
      ViInt32 size,
      ViAddr configuration);

   ViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationBuffer(
      ViSession vi,
      ViInt32 size,
      ViAddr configuration);

   /*- LCR Compensation functions -*/
   ViStatus _VI_FUNC niDCPower_PerformLCROpenCompensation(
      ViSession vi,
      ViConstString channelName,
      ViInt32 numFrequencies,
      const ViReal64 additionalFrequencies[]);

   ViStatus _VI_FUNC niDCPower_PerformLCRShortCompensation(
      ViSession vi,
      ViConstString channelName,
      ViInt32 numFrequencies,
      const ViReal64 additionalFrequencies[]);

   ViStatus _VI_FUNC niDCPower_PerformLCRLoadCompensation(
      ViSession vi,
      ViConstString channelName,
      ViInt32 numCompensationSpots,
      const NILCRLoadCompensationSpot compensationSpots[]);

   ViStatus _VI_FUNC niDCPower_ConfigureLCRCompensation(
      ViSession vi,
      ViConstString channelName,
      ViInt32 compensationDataSize,
      ViAddr compensationData);

   /*- LCR Custom Cable Compensation functions -*/
   ViStatus _VI_FUNC niDCPower_PerformLCROpenCustomCableCompensation(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_PerformLCRShortCustomCableCompensation(
      ViSession vi,
      ViConstString channelName);

   ViStatus _VI_FUNC niDCPower_GetLCRCustomCableCompensationData(
      ViSession vi,
      ViConstString channelName,
      ViInt32 customCableCompensationDataSize,
      ViAddr customCableCompensationData);

   ViStatus _VI_FUNC niDCPower_GetLCRCompensationData(
      ViSession vi,
      ViConstString channelName,
      ViInt32 compensationDataSize,
      ViAddr compensationData);

   ViStatus _VI_FUNC niDCPower_ConfigureLCRCustomCableCompensation(
      ViSession vi,
      ViConstString channelName,
      ViInt32 customCableCompensationDataSize,
      ViAddr customCableCompensationData);

#include "nidcpowerObsolete.h"

/******************************************************************************/
/*                              End Include File                              */
/******************************************************************************/
#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nidcpowerObsolete.h sha256=0bd8117caa456708370851953fcfa4071cc52a8766ce0d5d0c2f6dc0b56120ea bytes=1920 -->
## FILE: imports/include/nidcpowerObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nidcpowerObsolete.h`
- sha256: `0bd8117caa456708370851953fcfa4071cc52a8766ce0d5d0c2f6dc0b56120ea`
- bytes: 1920

````c
/****************************************************************************
 *              National Instruments DC Power Supplies and SMUs
 *--------------------------------------------------------------------------*
 *      Copyright (c) National Instruments 2016.  All Rights Reserved.      *
 *--------------------------------------------------------------------------*
 *
 * Title:    nidcpowerObsolete.h
 * Purpose:  National Instruments DC Power Supplies and SMUs Instrument
 *           Driver declarations that are now obsolete.
 *           They are defined here to maintain backward compatibility with
 *           previous versions of the driver. New applications should not use
 *           any of the definitions in this file. Instead, they must
 *           use definitions from the nidcpower.h header file.
 ****************************************************************************/

#ifndef __NIDCPOWER_OBSOLETE_HEADER
#define __NIDCPOWER_OBSOLETE_HEADER

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <ivi.h>
#include <IviDCPwr.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/*- Obsoleted Functions -*/
ViStatus _VI_FUNC  niDCPower_init(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViSession *vi);

ViStatus _VI_FUNC  niDCPower_InitWithOptions(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession *vi);

ViStatus _VI_FUNC  niDCPower_ConfigureOutputRange(
   ViSession vi,
   ViConstString channelName,
   ViInt32 rangeType,
   ViReal64 range);

/*- Unsupported Functions -*/
ViStatus _VI_FUNC  niDCPower_ResetOutputProtection(
   ViSession vi,
   ViConstString channelName);

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* __NIDCPOWER_OBSOLETE_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niDigital.h sha256=76c5b35b21b1ba040fef889d0d314b109f9f09e8c96500fb9c9ea09fd230cb3a bytes=44165 -->
## FILE: imports/include/niDigital.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niDigital.h`
- sha256: `76c5b35b21b1ba040fef889d0d314b109f9f09e8c96500fb9c9ea09fd230cb3a`
- bytes: 44165

````c
/****************************************************************************
 *          National Instruments Digital Pattern Driver                     *
 *--------------------------------------------------------------------------*
 *   Copyright (c) National Instruments 2017.  All Rights Reserved.         *
 *--------------------------------------------------------------------------*
 *                                                                          *
 * Title:    niDigital.h                                                    *
 * Purpose:  National Instruments Digital Pattern Driver declarations.      *
 *                                                                          *
 ****************************************************************************/

#ifndef ___niDigital_niDigital_h___
#define ___niDigital_niDigital_h___

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <ivi.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#ifdef _CVI_
   #pragma EnableLibraryRuntimeChecking
#endif


#if defined(__cplusplus) || defined(__cplusplus__)
   extern "C" {
#endif


/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NIDIGITAL_MAJOR_VERSION             20    /* Instrument driver major version   */
#define NIDIGITAL_MINOR_VERSION             6    /* Instrument driver minor version   */

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/

/*- IVI Inherent Attributes ------------------------------------------------*/
#define NIDIGITAL_ATTR_CACHE                                         /* ViBoolean   */  IVI_ATTR_CACHE
#define NIDIGITAL_ATTR_RANGE_CHECK                                   /* ViBoolean   */  IVI_ATTR_RANGE_CHECK
#define NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS                       /* ViBoolean   */  IVI_ATTR_QUERY_INSTRUMENT_STATUS
#define NIDIGITAL_ATTR_RECORD_COERCIONS                              /* ViBoolean   */  IVI_ATTR_RECORD_COERCIONS
#define NIDIGITAL_ATTR_SIMULATE                                      /* ViBoolean   */  IVI_ATTR_SIMULATE
#define NIDIGITAL_ATTR_INTERCHANGE_CHECK                             /* ViBoolean   */  IVI_ATTR_INTERCHANGE_CHECK
#define NIDIGITAL_ATTR_LOGICAL_NAME                                  /* ViString    */  IVI_ATTR_LOGICAL_NAME
#define NIDIGITAL_ATTR_GROUP_CAPABILITIES                            /* ViString    */  IVI_ATTR_GROUP_CAPABILITIES
#define NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS                   /* ViString    */  IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS

/*- Specific Driver Information, Read-only ---------------------------------*/
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_DESCRIPTION                   /* ViString    */  IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX                        /* ViString    */  IVI_ATTR_SPECIFIC_DRIVER_PREFIX
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_VENDOR                        /* ViString    */  IVI_ATTR_SPECIFIC_DRIVER_VENDOR
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_REVISION                      /* ViString    */  IVI_ATTR_SPECIFIC_DRIVER_REVISION
#define NIDIGITAL_ATTR_CHANNEL_COUNT                                 /* ViInt32     */  IVI_ATTR_CHANNEL_COUNT
#define NIDIGITAL_ATTR_INSTRUMENT_MANUFACTURER                       /* ViString    */  IVI_ATTR_INSTRUMENT_MANUFACTURER
#define NIDIGITAL_ATTR_INSTRUMENT_MODEL                              /* ViString    */  IVI_ATTR_INSTRUMENT_MODEL
#define NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION                  /* ViString    */  IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION      /* ViInt32     */  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION
#define NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION      /* ViInt32     */  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION
#define NIDIGITAL_ATTR_IO_RESOURCE_DESCRIPTOR                        /* ViString    */  IVI_ATTR_RESOURCE_DESCRIPTOR

/*- Driver Setup Information -----------------------------------------------*/
#define NIDIGITAL_ATTR_DRIVER_SETUP                                  /* ViString    */  IVI_ATTR_DRIVER_SETUP

/*- Device Attributes ------------------------------------------------------*/
#define NIDIGITAL_ATTR_SERIAL_NUMBER                                 /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  1L)

/*- Pin Control ------------------------------------------------------------*/
#define NIDIGITAL_ATTR_SELECTED_FUNCTION                             /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  4L)

/*- Level Configuration ----------------------------------------------------*/
#define NIDIGITAL_ATTR_VIL                                           /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  7L)
#define NIDIGITAL_ATTR_VIH                                           /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  8L)
#define NIDIGITAL_ATTR_VOL                                           /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  9L)
#define NIDIGITAL_ATTR_VOH                                           /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 10L)
#define NIDIGITAL_ATTR_VTERM                                         /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 11L)
#define NIDIGITAL_ATTR_TERMINATION_MODE                              /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE +  6L)
#define NIDIGITAL_ATTR_ACTIVE_LOAD_IOL                               /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 12L)
#define NIDIGITAL_ATTR_ACTIVE_LOAD_IOH                               /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 13L)
#define NIDIGITAL_ATTR_ACTIVE_LOAD_VCOM                              /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 14L)

/*- Trigger Configuration --------------------------------------------------*/
#define NIDIGITAL_ATTR_START_TRIGGER_TYPE                            /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 29L)
#define NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE             /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 30L)
#define NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE               /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 31L)
#define NIDIGITAL_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL        /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 32L)

#define NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TYPE                 /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 33L)
#define NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE  /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 34L)
#define NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE    /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 35L)
#define NIDIGITAL_ATTR_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 36L)
#define NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME        /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 40L)

/*- PPMU -------------------------------------------------------------------*/
#define NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION                          /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 15L)

#define NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL                            /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 16L)
#define NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT                            /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 54L)
#define NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE                      /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 17L)
#define NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_SUPPORTED                  /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 55L)
#define NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR                   /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 64L)

#define NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL                            /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 19L)
#define NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL_RANGE                      /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 20L)
#define NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW                        /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 21L)
#define NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH                       /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 22L)

#define NIDIGITAL_ATTR_PPMU_APERTURE_TIME                            /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 37L)
#define NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS                      /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 38L)

#define NIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE             /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 76L)

/*- Patterns ---------------------------------------------------------------*/
#define NIDIGITAL_ATTR_START_LABEL                                   /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 23L)
#define NIDIGITAL_ATTR_MASK_COMPARE                                  /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 60L)

/*- Pattern Opcode Event ---------------------------------------------------*/
#define NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 41L)

/*- Timing Offset ----------------------------------------------------------*/
#define NIDIGITAL_ATTR_TDR_OFFSET                                    /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 51L)
#define NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED                 /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 71L)
#define NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY                         /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 72L)

/*- Keep Alive -------------------------------------------------------------*/
#define NIDIGITAL_ATTR_HALT_ON_KEEP_ALIVE_OPCODE                     /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 62L)
#define NIDIGITAL_ATTR_IS_KEEP_ALIVE_ACTIVE                          /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 63L)

/*- Frequency Measurement --------------------------------------------------*/
#define NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_TIME            /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 69L)
#define NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE            /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 84L)
#define NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED          /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 85L)

/*- Clock Generator --------------------------------------------------------*/
#define NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY                     /* ViReal64    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 73L)
#define NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING                    /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 74L)

/*- History RAM ------------------------------------------------------------*/
#define NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE                      /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 43L)
#define NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER /* ViInt64     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 44L)
#define NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET  /* ViInt64  */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 52L)
#define NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET   /* ViInt64  */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 45L)
#define NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL       /* ViString    */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 46L)
#define NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE                 /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 47L)
#define NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES                /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 48L)
#define NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE   /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 77L)
#define NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE       /* ViBoolean   */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 78L)
#define NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE              /* ViInt64     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 79L)

/*- Synchronization --------------------------------------------------------*/
#define NIDIGITAL_ATTR_START_TRIGGER_TERMINAL_NAME                  /* ViString     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 39L)
#define NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAME                 /* ViString     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 59L)
#define NIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAME           /* ViString     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 42L)

/*- TDR Endpoint Termination------------------------------------------------*/
#define NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION                      /* ViInt32     */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 81L)

/*- Digital States ---------------------------------------------------------*/
#define NIDIGITAL_VAL_0                         0
#define NIDIGITAL_VAL_1                         1
#define NIDIGITAL_VAL_L                         3
#define NIDIGITAL_VAL_H                         4
#define NIDIGITAL_VAL_X                         5
#define NIDIGITAL_VAL_M                         6
#define NIDIGITAL_VAL_V                         7
#define NIDIGITAL_VAL_D                         8
#define NIDIGITAL_VAL_E                         9
#define NIDIGITAL_VAL_NOT_A_PIN_STATE           254
#define NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED    255

/*- Values for NIDIGITAL_ATTR_SELECTED_FUNCTION ----------------------------*/
#define NIDIGITAL_VAL_DIGITAL                   1100
#define NIDIGITAL_VAL_PPMU                      1101
#define NIDIGITAL_VAL_OFF                       1102
#define NIDIGITAL_VAL_DISCONNECT                1103

/*- Values for NIDIGITAL_ATTR_TERMINATION_MODE -----------------------------*/
#define NIDIGITAL_VAL_ACTIVE_LOAD               1200
#define NIDIGITAL_VAL_VTERM                     1201
#define NIDIGITAL_VAL_HIGH_Z                    1202

/*- Values for NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION -------------------------*/
#define NIDIGITAL_VAL_DC_VOLTAGE                1300
#define NIDIGITAL_VAL_DC_CURRENT                1301

/*- Values for drive edge set format ---------------------------------------*/
#define NIDIGITAL_VAL_NR                        1500
#define NIDIGITAL_VAL_RL                        1501
#define NIDIGITAL_VAL_RH                        1502
#define NIDIGITAL_VAL_SBC                       1503

/*- Values for Trigger Type ------------------------------------------------*/
#define NIDIGITAL_VAL_NONE                      1700
#define NIDIGITAL_VAL_DIGITAL_EDGE              1701
#define NIDIGITAL_VAL_SOFTWARE                  1702

/*- Values for Digital Edge Attributes -------------------------------------*/
#define NIDIGITAL_VAL_RISING_EDGE               1800
#define NIDIGITAL_VAL_FALLING_EDGE              1801

/*- Values for Signals -----------------------------------------------------*/
#define NIDIGITAL_VAL_START_TRIGGER             2000
#define NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER  2001
#define NIDIGITAL_VAL_PATTERN_OPCODE_EVENT      2002
#define NIDIGITAL_VAL_REF_CLOCK                 2003

/*- Values for NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE --*/
#define NIDIGITAL_VAL_ACQUIRE_ALL_SAMPLES       -1

/*- Values for Terminals ---------------------------------------------------*/
#define NIDIGITAL_VAL_DO_NOT_EXPORT_STR         ""
#define NIDIGITAL_VAL_PXI_TRIG0_STR             "PXI_Trig0"
#define NIDIGITAL_VAL_PXI_TRIG1_STR             "PXI_Trig1"
#define NIDIGITAL_VAL_PXI_TRIG2_STR             "PXI_Trig2"
#define NIDIGITAL_VAL_PXI_TRIG3_STR             "PXI_Trig3"
#define NIDIGITAL_VAL_PXI_TRIG4_STR             "PXI_Trig4"
#define NIDIGITAL_VAL_PXI_TRIG5_STR             "PXI_Trig5"
#define NIDIGITAL_VAL_PXI_TRIG6_STR             "PXI_Trig6"
#define NIDIGITAL_VAL_PXI_TRIG7_STR             "PXI_Trig7"

/*- Values for Pattern Opcode Event ----------------------------------------*/
#define NIDIGITAL_VAL_PATTERN_OPCODE_EVENT0     "patternOpcodeEvent0"
#define NIDIGITAL_VAL_PATTERN_OPCODE_EVENT1     "patternOpcodeEvent1"
#define NIDIGITAL_VAL_PATTERN_OPCODE_EVENT2     "patternOpcodeEvent2"
#define NIDIGITAL_VAL_PATTERN_OPCODE_EVENT3     "patternOpcodeEvent3"

/*- Values for Sequencer Flags ---------------------------------------------*/
#define NIDIGITAL_VAL_SEQUENCER_FLAG0           "seqflag0"
#define NIDIGITAL_VAL_SEQUENCER_FLAG1           "seqflag1"
#define NIDIGITAL_VAL_SEQUENCER_FLAG2           "seqflag2"
#define NIDIGITAL_VAL_SEQUENCER_FLAG3           "seqflag3"

/*- Values for Sequencer Registers -----------------------------------------*/
#define NIDIGITAL_VAL_SEQUENCER_REGISTER0       "reg0"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER1       "reg1"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER2       "reg2"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER3       "reg3"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER4       "reg4"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER5       "reg5"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER6       "reg6"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER7       "reg7"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER8       "reg8"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER9       "reg9"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER10      "reg10"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER11      "reg11"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER12      "reg12"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER13      "reg13"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER14      "reg14"
#define NIDIGITAL_VAL_SEQUENCER_REGISTER15      "reg15"

/*- Values for Conditional Jump Triggers -----------------------------------*/
#define NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0   "conditionalJumpTrigger0"
#define NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1   "conditionalJumpTrigger1"
#define NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2   "conditionalJumpTrigger2"
#define NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3   "conditionalJumpTrigger3"

/*- Values for NIDIGITAL_ATTR_APERTURE_TIME_UNITS --------------------------*/
#define NIDIGITAL_VAL_SECONDS                   2100

/*- Values for niDigital PPMU Measure function -----------------------------*/
#define NIDIGITAL_VAL_MEASURE_CURRENT           2400
#define NIDIGITAL_VAL_MEASURE_VOLTAGE           2401

/*- Source and Capture Memory bit order ------------------------------------*/
#define NIDIGITAL_VAL_MSB_FIRST                 2500
#define NIDIGITAL_VAL_LSB_FIRST                 2501

/* Source Memory Data Mapping ----------------------------------------------*/
#define NIDIGITAL_VAL_BROADCAST                 2600
#define NIDIGITAL_VAL_SITE_UNIQUE               2601

/*- Values for PPMU Current Limit Behavior ---------------------------------*/
#define NIDIGITAL_VAL_CURRENT_REGULATE          3100

/*- Values for Site Result Type --------------------------------------------*/
#define NIDIGITAL_VAL_PASS_FAIL                 3300
#define NIDIGITAL_VAL_CAPTURE_WAVEFORM          3301

/*- Values for HRAM Trigger Type -------------------------------------------*/
#define NIDIGITAL_VAL_FIRST_FAILURE             2200
#define NIDIGITAL_VAL_CYCLE_NUMBER              2201
#define NIDIGITAL_VAL_PATTERN_LABEL             2202

/*- Values for HRAM Cycles to Acquire --------------------------------------*/
#define NIDIGITAL_VAL_FAILED_CYCLES             2303
#define NIDIGITAL_VAL_ALL_CYCLES                2304

/*- Values for Time Set Edge -----------------------------------------------*/
#define NIDIGITAL_VAL_DRIVE_ON                  2800
#define NIDIGITAL_VAL_DRIVE_DATA                2801
#define NIDIGITAL_VAL_DRIVE_RETURN              2802
#define NIDIGITAL_VAL_DRIVE_OFF                 2803
#define NIDIGITAL_VAL_COMPARE_STROBE            2804
#define NIDIGITAL_VAL_DRIVE_DATA2               2805
#define NIDIGITAL_VAL_DRIVE_RETURN2             2806
#define NIDIGITAL_VAL_COMPARE_STROBE2           2807

/*- Values for NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION -----------------------------*/
#define NIDIGITAL_VAL_TDR_TO_OPEN               3600
#define NIDIGITAL_VAL_TDR_TO_SHORT_TO_GROUND    3601

/*- Values for NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE -------------------*/
#define NIDIGITAL_VAL_BANKED               3700
#define NIDIGITAL_VAL_PARALLEL             3701


/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

/*- Init and Close ---------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_init(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViSession* newVi);

ViStatus _VI_FUNC niDigital_InitWithOptions(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession* newVi);

ViStatus _VI_FUNC niDigital_close(
   ViSession vi);

/*- Session Locking --------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_LockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

ViStatus _VI_FUNC niDigital_UnlockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

/*- Utility ----------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_reset(
   ViSession vi);

ViStatus _VI_FUNC niDigital_ResetDevice(
   ViSession vi);

ViStatus _VI_FUNC niDigital_self_test(
   ViSession vi,
   ViInt16* testResult,
   ViChar testMessage[]);

/*- Error Handling ---------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_GetError(
   ViSession vi,
   ViStatus* errorCode,
   ViInt32 errorDescriptionBufferSize,
   ViChar errorDescription[]);

ViStatus _VI_FUNC niDigital_ClearError(
   ViSession vi);

ViStatus _VI_FUNC  niDigital_error_message(
   ViSession vi,
   ViStatus errorCode,
   ViChar errorMessage[IVI_MAX_MESSAGE_BUF_SIZE]);

/*- Calibration ------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_SelfCalibrate(
   ViSession vi);

/*- Attributes -------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_GetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViInt32* value);

ViStatus _VI_FUNC niDigital_GetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViInt64* value);

ViStatus _VI_FUNC niDigital_GetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViReal64* value);

ViStatus _VI_FUNC niDigital_GetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViInt32 bufferSize,
   ViChar value[]);

ViStatus _VI_FUNC niDigital_GetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViSession* value);

ViStatus _VI_FUNC niDigital_GetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViBoolean* value);

ViStatus _VI_FUNC niDigital_SetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViInt32 value);

ViStatus _VI_FUNC niDigital_SetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViInt64 value);

ViStatus _VI_FUNC niDigital_SetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViReal64 value);

ViStatus _VI_FUNC niDigital_SetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViConstString value);

ViStatus _VI_FUNC niDigital_SetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViSession value);

ViStatus _VI_FUNC niDigital_SetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attribute,
   ViBoolean value);

ViStatus _VI_FUNC niDigital_ResetAttribute(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId);

/*- Pin Map ----------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_LoadPinMap(
   ViSession vi,
   ViConstString pinMapFilePath);

ViStatus _VI_FUNC niDigital_EnableSites(
   ViSession vi,
   ViConstString siteList);

ViStatus _VI_FUNC niDigital_DisableSites(
   ViSession vi,
   ViConstString siteList);

ViStatus _VI_FUNC niDigital_IsSiteEnabled(
   ViSession vi,
   ViConstString site,
   ViBoolean* enable);

/*- Low Level -*/
ViStatus _VI_FUNC niDigital_CreatePinMap(
   ViSession vi,
   ViConstString dutPinList,
   ViConstString systemPinList);

ViStatus _VI_FUNC niDigital_CreatePinGroup(
   ViSession vi,
   ViConstString pinGroupName,
   ViConstString pinList);

ViStatus _VI_FUNC niDigital_CreateChannelMap(
   ViSession vi,
   ViInt32 numSites);

ViStatus _VI_FUNC niDigital_MapPinToChannel(
   ViSession vi,
   ViConstString pin,
   ViInt32 site,
   ViConstString channel);

ViStatus _VI_FUNC niDigital_EndChannelMap(
   ViSession vi);

ViStatus _VI_FUNC niDigital_GetPinName(
   ViSession vi,
   ViInt32 pinIndex,
   ViInt32 nameBufferSize,
   ViChar name[]);

ViStatus _VI_FUNC niDigital_GetChannelName(
   ViSession vi,
   ViInt32 index, /* 1-based */
   ViInt32 nameBufferSize,
   ViChar name[]);

ViStatus _VI_FUNC niDigital_GetChannelNameFromString(
   ViSession vi,
   ViConstString index, /* 0-based */
   ViInt32 nameBufferSize,
   ViChar name[]);

/*- Pin Control ------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_SelectFunction(
   ViSession vi,
   ViConstString channelList,
   ViInt32 function);

/*- Static I/O -------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_ReadStatic(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   ViUInt8 data[],
   ViInt32* actualNumRead);

ViStatus _VI_FUNC niDigital_WriteStatic(
   ViSession vi,
   ViConstString channelList,
   ViUInt8 state);

/*- Clock Generator --------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_ClockGenerator_GenerateClock(
   ViSession vi,
   ViConstString channelList,
   ViReal64 frequency,
   ViBoolean selectDigitalFunction);

ViStatus _VI_FUNC niDigital_ClockGenerator_Initiate(
   ViSession vi,
   ViConstString channelList);

ViStatus _VI_FUNC niDigital_ClockGenerator_Abort(
   ViSession vi,
   ViConstString channelList);

/*- Levels and Timing ------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_LoadSpecifications(
   ViSession vi,
   ViConstString specificationsFilePath);

ViStatus _VI_FUNC niDigital_UnloadSpecifications(
   ViSession vi,
   ViConstString specificationsFilePath);

ViStatus _VI_FUNC niDigital_LoadLevels(
   ViSession vi,
   ViConstString levelsFilePath);

ViStatus _VI_FUNC niDigital_LoadTiming(
   ViSession vi,
   ViConstString timingFilePath);

ViStatus _VI_FUNC niDigital_ApplyLevelsAndTiming(
   ViSession vi,
   ViConstString siteList,
   ViConstString levelsSheet,
   ViConstString timingSheet,
   ViConstString initialStateHighPins,
   ViConstString initialStateLowPins,
   ViConstString initialStateTristatePins);

ViStatus _VI_FUNC niDigital_ConfigureVoltageLevels(
   ViSession vi,
   ViConstString channelList,
   ViReal64 vil,
   ViReal64 vih,
   ViReal64 vol,
   ViReal64 voh,
   ViReal64 vterm);

ViStatus _VI_FUNC niDigital_ConfigureActiveLoadLevels(
   ViSession vi,
   ViConstString channelList,
   ViReal64 iol,
   ViReal64 ioh,
   ViReal64 vcom);

ViStatus _VI_FUNC niDigital_ConfigureTerminationMode(
   ViSession vi,
   ViConstString channelList,
   ViInt32 mode);

ViStatus _VI_FUNC niDigital_CreateTimeSet(
   ViSession vi,
   ViConstString name);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetPeriod(
   ViSession vi,
   ViConstString timeSet,
   ViReal64 period);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetDriveEdges(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViInt32 format,
   ViReal64 driveOnEdge,
   ViReal64 driveDataEdge,
   ViReal64 driveReturnEdge,
   ViReal64 driveOffEdge);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetCompareEdgesStrobe(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViReal64 strobeEdge);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetDriveFormat(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViInt32 driveFormat);

ViStatus _VI_FUNC niDigital_DeleteAllTimeSets(
   ViSession vi);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetEdgeMultiplier(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViInt32 edgeMultiplier);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetDriveEdges2x(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViInt32 format,
   ViReal64 driveOnEdge,
   ViReal64 driveDataEdge,
   ViReal64 driveReturnEdge,
   ViReal64 driveOffEdge,
   ViReal64 driveData2Edge,
   ViReal64 driveReturn2Edge);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetCompareEdgesStrobe2x(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViReal64 strobeEdge,
   ViReal64 strobe2Edge);

ViStatus _VI_FUNC niDigital_ConfigureTimeSetEdge(
   ViSession vi,
   ViConstString pinList,
   ViConstString timeSet,
   ViInt32 edge,
   ViReal64 time);

ViStatus _VI_FUNC niDigital_GetTimeSetPeriod(
   ViSession vi,
   ViConstString timeSet,
   ViReal64* period);

ViStatus _VI_FUNC niDigital_GetTimeSetEdge(
   ViSession vi,
   ViConstString pin,
   ViConstString timeSet,
   ViInt32 edge,
   ViReal64* time);

ViStatus _VI_FUNC niDigital_GetTimeSetEdgeMultiplier(
   ViSession vi,
   ViConstString pin,
   ViConstString timeSet,
   ViInt32* edgeMultiplier);

ViStatus _VI_FUNC niDigital_GetTimeSetDriveFormat(
   ViSession vi,
   ViConstString pin,
   ViConstString timeSet,
   ViInt32* format);

ViStatus _VI_FUNC niDigital_GetTimeSetName(
   ViSession vi,
   ViInt32 timeSetIndex,
   ViInt32 nameBufferSize,
   ViChar name[]);

/*- TDR --------------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_TDR(
   ViSession vi,
   ViConstString channelList,
   ViBoolean applyOffsets,
   ViInt32 offsetsBufferSize,
   ViReal64 offsets[],
   ViInt32* actualNumOffsets);

ViStatus _VI_FUNC niDigital_ApplyTDROffsets(
   ViSession vi,
   ViConstString channelList,
   ViInt32 numOffsets,
   ViReal64 offsets[]);

/*- PPMU Configuration -----------------------------------------------------*/
ViStatus _VI_FUNC niDigital_PPMU_ConfigureOutputFunction(
   ViSession vi,
   ViConstString channelList,
   ViInt32 outputFunction);

ViStatus _VI_FUNC niDigital_PPMU_ConfigureApertureTime(
   ViSession vi,
   ViConstString channelName,
   ViReal64 apertureTime,
   ViInt32 units);

/*- DC Voltage -*/
ViStatus _VI_FUNC niDigital_PPMU_ConfigureVoltageLevel(
   ViSession vi,
   ViConstString channelList,
   ViReal64 voltageLevel);

ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimit(
   ViSession vi,
   ViConstString channelList,
   ViInt32 behavior,
   ViReal64 limit);

ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimitRange(
   ViSession vi,
   ViConstString channelList,
   ViReal64 range);

/*- DC Current -*/
ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLevel(
   ViSession vi,
   ViConstString channelList,
   ViReal64 currentLevel);

ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLevelRange(
   ViSession vi,
   ViConstString channelList,
   ViReal64 range);

ViStatus _VI_FUNC niDigital_PPMU_ConfigureVoltageLimits(
   ViSession vi,
   ViConstString channelList,
   ViReal64 lowerVoltageLimit,
   ViReal64 upperVoltageLimit);

/*- PPMU Action-------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_PPMU_Source(
   ViSession vi,
   ViConstString channelList);

ViStatus _VI_FUNC niDigital_PPMU_Measure(
   ViSession vi,
   ViConstString channelList,
   ViInt32 measurementType,
   ViInt32 bufferSize,
   ViReal64 measurements[],
   ViInt32* actualNumRead);

/*- Pattern Configuration --------------------------------------------------*/
ViStatus _VI_FUNC niDigital_LoadPattern(
   ViSession vi,
   ViConstString filePath);

ViStatus _VI_FUNC niDigital_UnloadAllPatterns(
   ViSession vi,
   ViBoolean unloadKeepAlivePattern);

ViStatus _VI_FUNC niDigital_ConfigureStartLabel(
   ViSession vi,
   ViConstString label);

ViStatus _VI_FUNC niDigital_ConfigurePatternBurstSites(
   ViSession vi,
   ViConstString siteList);

ViStatus _VI_FUNC niDigital_GetPatternPinIndexes(
   ViSession vi,
   ViConstString startLabel,
   ViInt32 pinIndexesBufferSize,
   ViInt32 pinIndexes[],
   ViInt32* actualNumPins);

ViStatus _VI_FUNC niDigital_GetPatternPinList(
   ViSession vi,
   ViConstString startLabel,
   ViInt32 pinListBufferSize,
   ViChar pinList[]);

ViStatus _VI_FUNC niDigital_GetPatternName(
   ViSession vi,
   ViInt32 patternIndex,
   ViInt32 nameBufferSize,
   ViChar name[]);

/*- Pattern Action ---------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_BurstPattern(
   ViSession vi,
   ViConstString siteList,
   ViConstString startLabel,
   ViBoolean selectDigitalFunction,
   ViBoolean waitUntilDone,
   ViReal64 timeout);

ViStatus _VI_FUNC niDigital_BurstPatternSynchronized(
   ViUInt32 sessionCount,
   ViSession sessions[],
   ViConstString siteList,
   ViConstString startLabel,
   ViBoolean selectDigitalFunction,
   ViBoolean waitUntilDone,
   ViReal64 timeout);

/*- Low Level -*/
ViStatus _VI_FUNC niDigital_Commit(
   ViSession vi);

ViStatus _VI_FUNC niDigital_Initiate(
   ViSession vi);

ViStatus _VI_FUNC niDigital_IsDone(
   ViSession vi,
   ViBoolean* done);

ViStatus _VI_FUNC niDigital_WaitUntilDone(
   ViSession vi,
   ViReal64 timeout);

ViStatus _VI_FUNC niDigital_Abort(
   ViSession vi);

ViStatus _VI_FUNC niDigital_AbortKeepAlive(
   ViSession vi);

/*- History RAM ------------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_ConfigurePatternLabelHistoryRAMTrigger(
   ViSession vi,
   ViConstString label,
   ViInt64 vectorOffset,
   ViInt64 cycleOffset,
   ViInt32 pretriggerSamples);

ViStatus _VI_FUNC niDigital_ConfigureCycleNumberHistoryRAMTrigger(
   ViSession vi,
   ViInt64 cycleNumber,
   ViInt32 pretriggerSamples);

ViStatus _VI_FUNC niDigital_ConfigureFirstFailureHistoryRAMTrigger(
   ViSession vi,
   ViInt32 pretriggerSamples);

ViStatus _VI_FUNC niDigital_ConfigureHistoryRAMCyclesToAcquire(
   ViSession vi,
   ViInt32 cyclesToAcquire);

ViStatus _VI_FUNC niDigital_GetHistoryRAMSampleCount(
   ViSession vi,
   ViConstString site,
   ViInt64* sampleCount);

ViStatus _VI_FUNC niDigital_FetchHistoryRAMCycleInformation(
   ViSession vi,
   ViConstString site,
   ViInt64 sampleIndex,
   ViInt32* patternIndex,
   ViInt32* timeSetIndex,
   ViInt64* vectorNumber,
   ViInt64* cycleNumber,
   ViInt32* numDutCycles);

ViStatus _VI_FUNC niDigital_FetchHistoryRAMCyclePinData(
   ViSession vi,
   ViConstString site,
   ViConstString pinList,
   ViInt64 sampleIndex,
   ViInt32 dutCycleIndex,
   ViInt32 pinDataBufferSize,
   ViUInt8 expectedPinStates[],
   ViUInt8 actualPinStates[],
   ViBoolean perPinPassFail[],
   ViInt32* actualNumPinData);

ViStatus _VI_FUNC niDigital_FetchHistoryRAMScanCycleNumber(
   ViSession vi,
   ViConstString site,
   ViInt64 sampleIndex,
   ViInt64* scanCycleNumber);

/*- Source Memory ----------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_CreateSourceWaveformParallel(
   ViSession vi,
   ViConstString pinList,
   ViConstString waveformName,
   ViInt32 dataMapping);

ViStatus _VI_FUNC niDigital_CreateSourceWaveformSerial(
   ViSession vi,
   ViConstString pinList,
   ViConstString waveformName,
   ViInt32 dataMapping,
   ViUInt32 sampleWidth,
   ViInt32 bitOrder);

ViStatus _VI_FUNC niDigital_CreateSourceWaveformFromFileTDMS(
   ViSession vi,
   ViConstString waveformName,
   ViConstString waveformFilePath,
   ViBoolean writeWaveformData);

ViStatus _VI_FUNC niDigital_WriteSourceWaveformBroadcastU32(
   ViSession vi,
   ViConstString waveformName,
   ViInt32 waveformSize,
   ViUInt32 waveformData[]);

ViStatus _VI_FUNC niDigital_WriteSourceWaveformSiteUniqueU32(
   ViSession vi,
   ViConstString siteList,
   ViConstString waveformName,
   ViInt32 numWaveforms,
   ViInt32 samplesPerWaveform,
   ViUInt32 waveformData[]);

ViStatus _VI_FUNC niDigital_WriteSourceWaveformDataFromFileTDMS(
   ViSession vi,
   ViConstString waveformName,
   ViConstString waveformFilePath);

/*- Capture Memory ---------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_CreateCaptureWaveformParallel(
   ViSession vi,
   ViConstString pinList,
   ViConstString waveformName);

ViStatus _VI_FUNC niDigital_CreateCaptureWaveformSerial(
   ViSession vi,
   ViConstString pinList,
   ViConstString waveformName,
   ViUInt32 sampleWidth,
   ViInt32 bitOrder);

ViStatus _VI_FUNC niDigital_CreateCaptureWaveformFromFileDigicapture(
   ViSession vi,
   ViConstString waveformName,
   ViConstString waveformFilePath);

ViStatus _VI_FUNC niDigital_FetchCaptureWaveformU32(
   ViSession vi,
   ViConstString siteList,
   ViConstString waveformName,
   ViInt32 samplesToRead,
   ViReal64 timeout,
   ViInt32 dataBufferSize,
   ViUInt32 data[],
   ViInt32* actualNumWaveforms,
   ViInt32* actualSamplesPerWaveform);

/*- Triggers and Events ----------------------------------------------------*/
ViStatus _VI_FUNC niDigital_ExportSignal(
   ViSession      vi,
   ViInt32        signal,
   ViConstString  signalIdentifier,
   ViConstString  outputTerminal);

ViStatus _VI_FUNC niDigital_ConfigureDigitalEdgeStartTrigger(
   ViSession vi,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niDigital_ConfigureSoftwareEdgeStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niDigital_DisableStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niDigital_SendSoftwareEdgeTrigger(
   ViSession vi,
   ViInt32 trigger,
   ViConstString triggerIdentifier);

/*- Conditional Jump Trigger -----------------------------------------------*/
ViStatus _VI_FUNC niDigital_ConfigureDigitalEdgeConditionalJumpTrigger(
   ViSession vi,
   ViConstString triggerIdentifier,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger(
   ViSession vi,
   ViConstString triggerIdentifier);

ViStatus _VI_FUNC niDigital_DisableConditionalJumpTrigger(
   ViSession vi,
   ViConstString triggerIdentifier);

/*- Sequencer Flag ---------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_WriteSequencerFlag(
   ViSession vi,
   ViConstString flag,
   ViBoolean value);

ViStatus _VI_FUNC niDigital_WriteSequencerFlagSynchronized(
   ViUInt32 sessionCount,
   ViSession sessions[],
   ViConstString flag,
   ViBoolean value);

ViStatus _VI_FUNC niDigital_ReadSequencerFlag(
   ViSession vi,
   ViConstString flag,
   ViBoolean* value);

/*- Sequencer Register -----------------------------------------------------*/
ViStatus _VI_FUNC niDigital_WriteSequencerRegister(
   ViSession vi,
   ViConstString reg,
   ViInt32 value);

ViStatus _VI_FUNC niDigital_ReadSequencerRegister(
   ViSession vi,
   ViConstString reg,
   ViInt32* value);

/*- Match Fail Combination -------------------------------------------------*/
ViStatus _VI_FUNC niDigital_EnableMatchFailCombination(
   ViUInt32 sessionCount,
   ViSession sessions[],
   ViSession syncSession);

/*- Pattern Results --------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_GetSitePassFail(
   ViSession vi,
   ViConstString siteList,
   ViInt32 passFailBufferSize,
   ViBoolean passFail[],
   ViInt32* actualNumSites);

ViStatus _VI_FUNC niDigital_GetFailCount(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   ViInt64 failureCount[],
   ViInt32* actualNumRead);

/*- Sort Results -----------------------------------------------------------*/
ViStatus _VI_FUNC niDigital_GetPinResultsPinInformation(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   ViInt32 pinIndexes[],
   ViInt32 siteNumbers[],
   ViInt32 channelIndexes[], /* 1-based index */
   ViInt32* actualNumValues);

ViStatus _VI_FUNC niDigital_GetSiteResultsSiteNumbers(
   ViSession vi,
   ViConstString siteList,
   ViInt32 siteResultType,
   ViInt32 siteNumbersBufferSize,
   ViInt32 siteNumbers[],
   ViInt32* actualNumSiteNumbers);

ViStatus _VI_FUNC niDigital_SortPinResultsBySiteViReal64(
   ViInt32 sessionCount,
   ViSession sessions[],
   ViConstString channelList,
   ViInt32 numResults,
   ViReal64 results[],
   ViInt32 pinIndexes[],
   ViInt32 siteNumbers[]);

ViStatus _VI_FUNC niDigital_SortPinResultsBySiteViInt64(
   ViInt32 sessionCount,
   ViSession sessions[],
   ViConstString channelList,
   ViInt32 numResults,
   ViInt64 results[],
   ViInt32 pinIndexes[],
   ViInt32 siteNumbers[]);

ViStatus _VI_FUNC niDigital_SortPinResultsBySiteViUInt8(
   ViInt32 sessionCount,
   ViSession sessions[],
   ViConstString channelList,
   ViInt32 numResults,
   ViUInt8 results[],
   ViInt32 pinIndexes[],
   ViInt32 siteNumbers[]);

ViStatus _VI_FUNC niDigital_SortSiteResultsViBoolean(
   ViInt32 sessionCount,
   ViSession sessions[],
   ViConstString siteList,
   ViInt32 siteResultType,
   ViInt32 numResults,
   ViBoolean results[],
   ViInt32 siteNumbers[],
   ViInt32* actualNumResults);

ViStatus _VI_FUNC niDigital_SortSiteResultsViUInt32Waveform(
   ViInt32 sessionCount,
   ViSession sessions[],
   ViConstString siteList,
   ViInt32 siteResultType,
   ViInt32 numWaveforms,
   ViInt32 numSamplesPerWaveform,
   ViUInt32 waveforms[],
   ViInt32 siteNumbers[],
   ViInt32* actualNumWaveforms);

/*- Frequency Measurement --------------------------------------------------*/
ViStatus _VI_FUNC niDigital_FrequencyCounter_ConfigureMeasurementTime(
   ViSession vi,
   ViConstString channelList,
   ViReal64 measurementTime);

ViStatus _VI_FUNC niDigital_FrequencyCounter_ConfigureMeasurementMode(
   ViSession vi,
   ViInt32 mode);

ViStatus _VI_FUNC niDigital_FrequencyCounter_MeasureFrequency(
   ViSession vi,
   ViConstString channelList,
   ViInt32 frequenciesBufferSize,
   ViReal64 frequencies[],
   ViInt32* actualNumFrequencies);

/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/

/* IVI_SPECIFIC_ERROR_BASE == 0xbffa4000 */
#define NIDIGITAL_ERROR_BASE IVI_SPECIFIC_ERROR_BASE

/* IVI_SPECIFIC_WARN_BASE == 0x3ffa4000 */
#define NIDIGITAL_WARN_BASE IVI_SPECIFIC_WARN_BASE

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#endif /* ___niDigital_niDigital_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nidmm.h sha256=00e8bec07bed71104f9cdb9ae897d5abffab4770cd043fb139fcbd472e2e0f23 bytes=44931 -->
## FILE: imports/include/nidmm.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nidmm.h`
- sha256: `00e8bec07bed71104f9cdb9ae897d5abffab4770cd043fb139fcbd472e2e0f23`
- bytes: 44931

````c
/*****************************************************************************
 *                            N I - D M M
 *----------------------------------------------------------------------------
 *    Copyright (c) National Instruments 2020.  All Rights Reserved.
 *----------------------------------------------------------------------------
 *
 * Title:       nidmm.h
 * Purpose:     NiDmm Class value, attribute Id, and function declarations.
 *
 * National Instruments, Austin Texas
 * PH. (800)433-3488
 * Website  http://www.ni.com
 *
 *****************************************************************************/

#ifndef __NIDMM__HEADER
   #define __NIDMM__HEADER

   #if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
   #endif

   /******************************************************************************/
   /*                               Include Files                                */
   /******************************************************************************/

   #define IVI_DO_NOT_INCLUDE_VISA_HEADERS
   #include "IviDmm.h"
   #include "ivi.h"
   #undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

   #ifdef _CVI_
      #pragma EnableLibraryRuntimeChecking
   #endif


   /******************************************************************************/
   /*                         Version/Revision Constants                         */
   /******************************************************************************/

   #define NIDMM_MAJOR_VERSION                 20
   #define NIDMM_MINOR_VERSION                 1

   #define NIDMM_CLASS_SPEC_MAJOR_VERSION      4
   #define NIDMM_CLASS_SPEC_MINOR_VERSION      1

   #define NIDMM_ATTR_BASE                     IVI_SPECIFIC_PUBLIC_ATTR_BASE
   #define NIDMM_ATTR_PRIVATE_BASE             IVI_SPECIFIC_PRIVATE_ATTR_BASE
   #define NIDMM_ERROR_BASE                    IVI_SPECIFIC_ERROR_BASE
   #define NIDMM_WARN_BASE                     IVI_SPECIFIC_WARN_BASE

   // additional status base
   #define NIDMM_ERROR_EXT_STATUS_BASE         (NIDMM_ERROR_BASE + 0x0F00)
   #define NIDMM_ERROR_EXTCAL_ERROR_BASE       (NIDMM_ERROR_BASE + 0x0200)

   // additional warning base
   #define NIDMM_WARN_EXT_STATUS_BASE          (NIDMM_WARN_BASE + 0x0F00)
   #define NIDMM_WARN_EXTCAL_WARN_BASE         (NIDMM_WARN_BASE + 0x0200)

   #define NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE    IVIDMM_VAL_FUNC_SPECIFIC_EXT_BASE
   #define NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE   IVIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE

   /******************************************************************************/
   /*                     Instrument Specific Warning Codes                      */
   /******************************************************************************/

   #define NIDMM_WARN_NOT_SUPPORTED            (NIDMM_WARN_BASE  +  0L) // 0x3FFA4000  1073364992
   #define NIDMM_WARN_SIMULATING               (NIDMM_WARN_BASE  +  1L) // 0x3FFA4001  1073364993
   #define NIDMM_WARN_RANGE_INVALIDATED        (NIDMM_WARN_BASE  +  2L) // 0x3FFA4002  1073364994

   // additional warnings
   #define NIDMM_WARN_UNDERRANGE               (NIDMM_WARN_EXT_STATUS_BASE + 0x80) // 0x3FFA4F80 1073368960
   #define NIDMM_WARN_OVERRANGE                IVIDMM_WARN_OVER_RANGE

   #define NIDMM_WARN_EXTCAL_SELF_CAL_NEEDED          (NIDMM_WARN_EXTCAL_WARN_BASE + 0L)
   #define NIDMM_WARN_EXTCAL_BUFFER_TRUNCATED         (NIDMM_WARN_EXTCAL_WARN_BASE + 1L)

   /******************************************************************************/
   /*                                 Attributes                                 */
   /******************************************************************************/
   /*- User Options -*/
   #define NIDMM_ATTR_RANGE_CHECK                              IVI_ATTR_RANGE_CHECK                              /* ViBoolean */
   #define NIDMM_ATTR_QUERY_INSTRUMENT_STATUS                  IVI_ATTR_QUERY_INSTRUMENT_STATUS                  /* ViBoolean */
   #define NIDMM_ATTR_CACHE                                    IVI_ATTR_CACHE                                    /* ViBoolean */
   #define NIDMM_ATTR_SIMULATE                                 IVI_ATTR_SIMULATE                                 /* ViBoolean */
   #define NIDMM_ATTR_RECORD_COERCIONS                         IVI_ATTR_RECORD_COERCIONS                         /* ViBoolean */
   #define NIDMM_ATTR_INTERCHANGE_CHECK                        IVI_ATTR_INTERCHANGE_CHECK                        /* ViBoolean */

   /*- Class Driver Identification -*/
   #define NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32   (read only) */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32   (read only) */

   /*- Driver Identification -*/
   #define NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION              IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION              /* ViString  (read only) */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX                   IVI_ATTR_SPECIFIC_DRIVER_PREFIX                   /* ViString  (read only) */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR                   IVI_ATTR_SPECIFIC_DRIVER_VENDOR                   /* ViString  (read only) */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_REVISION                 IVI_ATTR_SPECIFIC_DRIVER_REVISION                 /* ViString  (read only) */
   #define NIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION    IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION    /* ViInt32   (read only) */
   #define NIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION    IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION    /* ViInt32   (read only) */

   /*- Driver Capabilities -*/
   #define NIDMM_ATTR_CHANNEL_COUNT                            IVI_ATTR_CHANNEL_COUNT                            /* ViInt32   (read only) */
   #define NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS              IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS              /* ViString  (read only) */
   #define NIDMM_ATTR_GROUP_CAPABILITIES                       IVI_ATTR_GROUP_CAPABILITIES                       /* ViString  (read only) */

   /*- Instrument Identification -*/
   #define NIDMM_ATTR_INSTRUMENT_MANUFACTURER                  IVI_ATTR_INSTRUMENT_MANUFACTURER                  /* ViString  (read only) */
   #define NIDMM_ATTR_INSTRUMENT_MODEL                         IVI_ATTR_INSTRUMENT_MODEL                         /* ViString  (read only) */
   #define NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION             IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION             /* ViString  (read only) */

   /*- Advanced Session I/O -*/
   #define NIDMM_ATTR_LOGICAL_NAME                             IVI_ATTR_LOGICAL_NAME                             /* ViString  (read only) */
   #define NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR                   IVI_ATTR_IO_RESOURCE_DESCRIPTOR                   /* ViString  (read only) */
   #define NIDMM_ATTR_DRIVER_SETUP                             IVI_ATTR_DRIVER_SETUP                             /* ViString  (read only) */
   #define NIDMM_ATTR_IO_SESSION                               IVI_ATTR_IO_SESSION                               /* ViSession (read only) */

   /*- IviDmmBase Capability Group -*/
   #define NIDMM_ATTR_FUNCTION                                 IVIDMM_ATTR_FUNCTION                              /* ViInt32   */
   #define NIDMM_ATTR_RANGE                                    IVIDMM_ATTR_RANGE                                 /* ViReal64  */
   #define NIDMM_ATTR_RESOLUTION_ABSOLUTE                      IVIDMM_ATTR_RESOLUTION_ABSOLUTE                   /* ViReal64  */
   #define NIDMM_ATTR_RESOLUTION_DIGITS                        (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)                 /* ViReal64  */
   #define NIDMM_ATTR_TRIGGER_DELAY                            IVIDMM_ATTR_TRIGGER_DELAY                         /* ViReal64  */
   #define NIDMM_ATTR_TRIGGER_SOURCE                           IVIDMM_ATTR_TRIGGER_SOURCE                        /* ViInt32   */

   /*- IviDmmAcMeasurement Extension Group -*/
   #define NIDMM_ATTR_AC_MAX_FREQ                              IVIDMM_ATTR_AC_MAX_FREQ                           /* ViReal64  */
   #define NIDMM_ATTR_AC_MIN_FREQ                              IVIDMM_ATTR_AC_MIN_FREQ                           /* ViReal64  */

   /*- IviDmmFrequencyMeasurement Extension Group -*/
   #define NIDMM_ATTR_FREQ_VOLTAGE_RANGE                       IVIDMM_ATTR_FREQ_VOLTAGE_RANGE                    /* ViReal64  */

   /*- IviDmmMultiPoint Extension Group -*/
   #define NIDMM_ATTR_MEAS_COMPLETE_DEST                       IVIDMM_ATTR_MEAS_COMPLETE_DEST                    /* ViInt32   */
   #define NIDMM_ATTR_SAMPLE_COUNT                             IVIDMM_ATTR_SAMPLE_COUNT                          /* ViInt32   */
   #define NIDMM_ATTR_SAMPLE_INTERVAL                          IVIDMM_ATTR_SAMPLE_INTERVAL                       /* ViReal64  */
   #define NIDMM_ATTR_SAMPLE_TRIGGER                           IVIDMM_ATTR_SAMPLE_TRIGGER                        /* ViInt32   */
   #define NIDMM_ATTR_TRIGGER_COUNT                            IVIDMM_ATTR_TRIGGER_COUNT                         /* ViInt32   */

   /*- IviDmmDeviceInfo Extension Group -*/
   #define NIDMM_ATTR_APERTURE_TIME                            IVIDMM_ATTR_APERTURE_TIME                         /* ViReal64  */
   #define NIDMM_ATTR_APERTURE_TIME_UNITS                      IVIDMM_ATTR_APERTURE_TIME_UNITS                   /* ViInt32   */

   /*- IviDmmAutoRangeValue Extension Group -*/
   #define NIDMM_ATTR_AUTO_RANGE_VALUE                         IVIDMM_ATTR_AUTO_RANGE_VALUE                      /* ViReal64  (read only) */

   /*- IviDmmAutoZero Extension Group -*/
   #define NIDMM_ATTR_AUTO_ZERO                                IVIDMM_ATTR_AUTO_ZERO                             /* ViInt32   */

   /*- IviDmmPowerLineFrequency Extension Group -*/
   #define NIDMM_ATTR_POWERLINE_FREQ                           IVIDMM_ATTR_POWERLINE_FREQ                        /* ViReal64  */

   /*- Advanced Triggering -*/
   #define NIDMM_ATTR_TRIGGER_SLOPE                            IVIDMM_ATTR_TRIGGER_SLOPE                         /* ViInt32   */
   #define NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE                     (NIDMM_ATTR_BASE + 10L)                           /* ViInt32   */
   #define NIDMM_ATTR_MEAS_DEST_SLOPE                          (NIDMM_ATTR_BASE + 2L)                            /* ViInt32   */

   /*- Advanced measurement configuration attributes -*/
   #define NIDMM_ATTR_ADC_CALIBRATION                          (NIDMM_ATTR_BASE + 22L)                           /* ViInt32   */
   #define NIDMM_ATTR_OFFSET_COMP_OHMS                         (NIDMM_ATTR_BASE + 23L)                           /* ViInt32   */
   #define NIDMM_ATTR_NUMBER_OF_AVERAGES                       (NIDMM_ATTR_BASE + 32L)                           /* ViInt32   */
   #define NIDMM_ATTR_CURRENT_SOURCE                           (NIDMM_ATTR_BASE + 25L)                           /* ViReal64  */
   #define NIDMM_ATTR_DC_NOISE_REJECTION                       (NIDMM_ATTR_BASE + 26L)                           /* ViInt32   */
   #define NIDMM_ATTR_SETTLE_TIME                              (NIDMM_ATTR_BASE + 28L)                           /* ViReal64  */
   #define NIDMM_ATTR_INPUT_RESISTANCE                         (NIDMM_ATTR_BASE + 29L)                           /* ViReal64  */
   #define NIDMM_ATTR_LATENCY                                  (NIDMM_ATTR_BASE + 34L)                           /* ViInt32   */
   #define NIDMM_ATTR_BUFFER_SIZE                              (NIDMM_ATTR_BASE + 37L)                           /* ViInt32   */
   #define NIDMM_ATTR_SHUNT_VALUE                              (NIDMM_ATTR_BASE + 3L)                            /* ViReal64  */

   /*- Behavior model attribute -*/
   #define NIDMM_ATTR_OPERATION_MODE                           (NIDMM_ATTR_BASE + 14L)                           /* ViInt32   */

   /*- Waveform acquisition attributes -*/
   #define NIDMM_ATTR_WAVEFORM_RATE                            (NIDMM_ATTR_BASE + 18L)                           /* ViReal64  */
   #define NIDMM_ATTR_WAVEFORM_POINTS                          (NIDMM_ATTR_BASE + 19L)                           /* ViInt32   */

   /*- Waveform acquisition signal coupling attribute -*/
   #define NIDMM_ATTR_WAVEFORM_COUPLING                        (NIDMM_ATTR_BASE + 27L)                           /* ViInt32   */

   /*- Frequency voltage auto range value attribute -*/
   #define NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE            (NIDMM_ATTR_BASE + 44L)                           /* ViReal64  */

   /*- Capacitance and Inductance Measurement Attributes -*/
   #define NIDMM_ATTR_CABLE_COMP_TYPE                          (NIDMM_ATTR_BASE + 45L)                           /* ViInt32   */
   #define NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE               (NIDMM_ATTR_BASE + 46L)                           /* ViReal64  */
   #define NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE              (NIDMM_ATTR_BASE + 47L)                           /* ViReal64  */
   #define NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE              (NIDMM_ATTR_BASE + 48L)                           /* ViReal64  */
   #define NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE              (NIDMM_ATTR_BASE + 49L)                           /* ViReal64  */
   #define NIDMM_ATTR_LC_CALCULATION_MODEL                     (NIDMM_ATTR_BASE + 52L)                           /* ViInt32   */
   #define NIDMM_ATTR_DC_BIAS                                  (NIDMM_ATTR_BASE + 53L)                           /* ViInt32   */
   #define NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE                (NIDMM_ATTR_BASE + 55L)                           /* ViInt32   */

   /*- Attribute for serial number of the instrument -*/
   #define NIDMM_ATTR_SERIAL_NUMBER                            (NIDMM_ATTR_BASE + 54L)                           /* ViString  (read only) */

   /*- Attribute for product number of the instrument -*/
   #define NIDMM_ATTR_CONFIG_PRODUCT_NUMBER                    (NIDMM_ATTR_BASE + 61L)                           /* ViInt32   (read only) */

   /*- Attributes for Temperature Functions -*/
   #define NIDMM_ATTR_TEMP_TRANSDUCER_TYPE                     IVIDMM_ATTR_TEMP_TRANSDUCER_TYPE                  /* ViInt32   */
   #define NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE                    IVIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE                 /* ViInt32   */
   #define NIDMM_ATTR_TEMP_TC_TYPE                             IVIDMM_ATTR_TEMP_TC_TYPE                          /* ViInt32   */
   #define NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC                   IVIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC                /* ViReal64  */
   #define NIDMM_ATTR_TEMP_RTD_TYPE                            (NIDMM_ATTR_BASE + 120L)                          /* ViInt32   */
   #define NIDMM_ATTR_TEMP_RTD_RES                             IVIDMM_ATTR_TEMP_RTD_RES                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_RTD_A                               (NIDMM_ATTR_BASE + 121L)                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_RTD_B                               (NIDMM_ATTR_BASE + 122L)                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_RTD_C                               (NIDMM_ATTR_BASE + 123L)                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_THERMISTOR_TYPE                     (NIDMM_ATTR_BASE + 124L)                          /* ViInt32   */
   #define NIDMM_ATTR_TEMP_THERMISTOR_A                        (NIDMM_ATTR_BASE + 125L)                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_THERMISTOR_B                        (NIDMM_ATTR_BASE + 126L)                          /* ViReal64  */
   #define NIDMM_ATTR_TEMP_THERMISTOR_C                        (NIDMM_ATTR_BASE + 127L)                          /* ViReal64  */

   /******************************************************************************/
   /*                              Attribute Values                              */
   /******************************************************************************/

   /*- Defined values for describing floating point number types -*/
   #define NIDMM_VAL_TYPE_NORMAL          IVI_VAL_TYPE_NORMAL
   #define NIDMM_VAL_TYPE_NAN             IVI_VAL_TYPE_NAN
   #define NIDMM_VAL_TYPE_PINF            IVI_VAL_TYPE_PINF
   #define NIDMM_VAL_TYPE_NINF            IVI_VAL_TYPE_NINF

   /*- Defined values for NIDMM_ATTR_FUNCTION -*/
   #define NIDMM_VAL_DC_VOLTS             IVIDMM_VAL_DC_VOLTS
   #define NIDMM_VAL_AC_VOLTS             IVIDMM_VAL_AC_VOLTS
   #define NIDMM_VAL_DC_CURRENT           IVIDMM_VAL_DC_CURRENT
   #define NIDMM_VAL_AC_CURRENT           IVIDMM_VAL_AC_CURRENT
   #define NIDMM_VAL_2_WIRE_RES           IVIDMM_VAL_2_WIRE_RES
   #define NIDMM_VAL_4_WIRE_RES           IVIDMM_VAL_4_WIRE_RES
   #define NIDMM_VAL_FREQ                 IVIDMM_VAL_FREQ
   #define NIDMM_VAL_PERIOD               IVIDMM_VAL_PERIOD
   #define NIDMM_VAL_TEMPERATURE          IVIDMM_VAL_TEMPERATURE
   #define NIDMM_VAL_AC_VOLTS_DC_COUPLED  (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 1L)
   #define NIDMM_VAL_DIODE                (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 2L)
   #define NIDMM_VAL_WAVEFORM_VOLTAGE     (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 3L)
   #define NIDMM_VAL_WAVEFORM_CURRENT     (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 4L)
   #define NIDMM_VAL_CAPACITANCE          (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 5L)
   #define NIDMM_VAL_INDUCTANCE           (NIDMM_VAL_FUNC_SPECIFIC_EXT_BASE + 6L)

   /*- Defined values for NIDMM_ATTR_RANGE -*/
   #define NIDMM_VAL_AUTO_RANGE_ON        IVIDMM_VAL_AUTO_RANGE_ON
   #define NIDMM_VAL_AUTO_RANGE_OFF       IVIDMM_VAL_AUTO_RANGE_OFF
   #define NIDMM_VAL_AUTO_RANGE_ONCE      IVIDMM_VAL_AUTO_RANGE_ONCE

   /*- Defined values for NIDMM_ATTR_FREQ_VOLTAGE_RANGE -*/
   /* #define NIDMM_VAL_AUTO_RANGE_ON     DEFINED ABOVE */
   /* #define NIDMM_VAL_AUTO_RANGE_OFF    DEFINED ABOVE */

   /*- Defined values for NIDMM_ATTR_TRIGGER_DELAY -*/
   #define NIDMM_VAL_AUTO_DELAY           -1.0

   #define NIDMM_VAL_AUTO_DELAY_ON        IVIDMM_VAL_AUTO_DELAY_ON
   #define NIDMM_VAL_AUTO_DELAY_OFF       IVIDMM_VAL_AUTO_DELAY_OFF

   /*- Defined value for NIDMM_ATTR_SAMPLE_INTERVAL -*/
   /* #define NIDMM_VAL_AUTO_DELAY        DEFINED ABOVE */

   /*- Defined values for NIDMM_ATTR_TRIGGER_SOURCE -*/
   #define NIDMM_VAL_IMMEDIATE            IVIDMM_VAL_IMMEDIATE
   #define NIDMM_VAL_EXTERNAL             IVIDMM_VAL_EXTERNAL
   #define NIDMM_VAL_SOFTWARE_TRIG        IVIDMM_VAL_SOFTWARE_TRIG
   #define NIDMM_VAL_PXI_TRIG0            IVIDMM_VAL_TTL0
   #define NIDMM_VAL_PXI_TRIG1            IVIDMM_VAL_TTL1
   #define NIDMM_VAL_PXI_TRIG2            IVIDMM_VAL_TTL2
   #define NIDMM_VAL_PXI_TRIG3            IVIDMM_VAL_TTL3
   #define NIDMM_VAL_PXI_TRIG4            IVIDMM_VAL_TTL4
   #define NIDMM_VAL_PXI_TRIG5            IVIDMM_VAL_TTL5
   #define NIDMM_VAL_PXI_TRIG6            IVIDMM_VAL_TTL6
   #define NIDMM_VAL_PXI_TRIG7            IVIDMM_VAL_TTL7
   #define NIDMM_VAL_PXI_STAR             IVIDMM_VAL_PXI_STAR
   #define NIDMM_VAL_LBR_TRIG1            (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 4L)
   #define NIDMM_VAL_AUX_TRIG1            (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 1L)

   /*- Defined values for NIDMM_ATTR_MEAS_COMPLETE_DEST -*/
   #define NIDMM_VAL_NONE                 IVIDMM_VAL_NONE

   /* #define NIDMM_VAL_EXTERNAL          DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG0         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG1         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG2         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG3         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG4         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG5         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG6         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG7         DEFINED ABOVE */
   #define NIDMM_VAL_LBR_TRIG0            (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 3L)

   /*- Defined values for NIDMM_ATTR_SAMPLE_TRIGGER -*/
   /* #define NIDMM_VAL_IMMEDIATE         DEFINED ABOVE */
   /* #define NIDMM_VAL_EXTERNAL          DEFINED ABOVE */
   /* #define NIDMM_VAL_SOFTWARE_TRIG     DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG0         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG1         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG2         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG3         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG4         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG5         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG6         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_TRIG7         DEFINED ABOVE */
   /* #define NIDMM_VAL_PXI_STAR          DEFINED ABOVE */
   /* #define NIDMM_VAL_LBR_TRIG1         DEFINED ABOVE */
   /* #define NIDMM_VAL_AUX_TRIG1         DEFINED ABOVE */
   #define NIDMM_VAL_INTERVAL             IVIDMM_VAL_INTERVAL

   /*- Defined values for NIDMM_ATTR_TRIGGER_SLOPE,
       NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE, and
       NIDMM_ATTR_MEAS_DEST_SLOPE, -*/
   #define NIDMM_VAL_POSITIVE             IVIDMM_VAL_POSITIVE
   #define NIDMM_VAL_NEGATIVE             IVIDMM_VAL_NEGATIVE

   /*- Defined value for NIDMM_ATTR_TRIGGER_COUNT -*/
   #define NIDMM_VAL_TRIG_COUNT_INFINITE      0

   /*- Definde value for NIDMM_ATTR_SAMPLE_COUNT -*/
   #define NIDMM_VAL_SAMPLE_COUNT_INFINITE    0

   /*- Defined values for NIDMM_ATTR_POWERLINE_FREQ -*/
   #define NIDMM_VAL_50_HERTZ             (50.0)
   #define NIDMM_VAL_60_HERTZ             (60.0)

   /*- Defined values for NIDMM_ATTR_APERTURE_TIME_UNITS -*/
   #define NIDMM_VAL_SECONDS              IVIDMM_VAL_SECONDS
   #define NIDMM_VAL_POWER_LINE_CYCLES    IVIDMM_VAL_POWER_LINE_CYCLES

   /*- Defined values for NIDMM_ATTR_APERTURE_TIME -*/
   #define NIDMM_VAL_APERTURE_TIME_AUTO    -1.0
   #define NIDMM_VAL_1_PLC                  1.0
   #define NIDMM_VAL_5_PLC                  5.0
   #define NIDMM_VAL_6_PLC                  6.0
   #define NIDMM_VAL_10_PLC                10.0
   #define NIDMM_VAL_12_PLC                12.0
   #define NIDMM_VAL_100_PLC              100.0
   #define NIDMM_VAL_120_PLC              120.0

   /*- Defined value for NIDMM_ATTR_SETTLE_TIME -*/
   #define NIDMM_VAL_SETTLE_TIME_AUTO      -1.0

   /*- Defined values for NIDMM_ATTR_AUTO_ZERO -*/
   #define NIDMM_VAL_AUTO_ZERO_AUTO       -1
   #define NIDMM_VAL_AUTO_ZERO_OFF        IVIDMM_VAL_AUTO_ZERO_OFF
   #define NIDMM_VAL_AUTO_ZERO_ON         IVIDMM_VAL_AUTO_ZERO_ON
   #define NIDMM_VAL_AUTO_ZERO_ONCE       IVIDMM_VAL_AUTO_ZERO_ONCE

   /*- Defined values for NIDMM_ATTR_ADC_CALIBRATION -*/
   #define NIDMM_VAL_ADC_CALIBRATION_AUTO    -1
   #define NIDMM_VAL_ADC_CALIBRATION_OFF      0
   #define NIDMM_VAL_ADC_CALIBRATION_ON       1

   /*- Defined values for NIDMM_ATTR_OFFSET_COMP_OHMS -*/
   #define NIDMM_VAL_OFFSET_COMP_OHMS_OFF     0
   #define NIDMM_VAL_OFFSET_COMP_OHMS_ON      1

   /*- Defined values for NIDMM_ATTR_CURRENT_SOURCE -*/
   #define NIDMM_VAL_1_MICROAMP         0.000001
   #define NIDMM_VAL_10_MICROAMP        0.00001
   #define NIDMM_VAL_100_MICROAMP       0.0001
   #define NIDMM_VAL_1_MILLIAMP         0.001

   /*- Defined values for NIDMM_ATTR_DC_NOISE_REJECTION -*/
   #define NIDMM_VAL_DCNR_AUTO         -1
   #define NIDMM_VAL_DCNR_NORMAL        0
   #define NIDMM_VAL_DCNR_SECOND_ORDER  1
   #define NIDMM_VAL_DCNR_HIGH_ORDER    2

   /*- Defined values for NIDMM_ATTR_INPUT_RESISTANCE -*/
   #define NIDMM_VAL_1_MEGAOHM                    1000000.0
   #define NIDMM_VAL_10_MEGAOHM                  10000000.0
   #define NIDMM_VAL_GREATER_THAN_10_GIGAOHM  10000000000.0
   #define NIDMM_VAL_RESISTANCE_NA                      0.0

   /*- Defined value for NIDMM_ATTR_LATENCY -*/
   #define NIDMM_VAL_LATENCY_AUTO      -1

   /*- Defined value for NIDMM_ATTR_BUFFER_SIZE -*/
   #define NIDMM_VAL_BUFFER_SIZE_AUTO  -1

   /*- Defined values for calibration functions -*/
   #define NIDMM_VAL_INTERNAL_AREA      0
   #define NIDMM_VAL_EXTERNAL_AREA      1

   /*- Defined values for time limit -*/
   #define NIDMM_VAL_TIME_LIMIT_AUTO         -1

   /*- Defined values for NIDMM_ATTR_OPERATION_MODE -*/
   #define NIDMM_VAL_IVIDMM_MODE             0
   #define NIDMM_VAL_WAVEFORM_MODE           1

   /*- Defined Values for NIDMM_ATTR_WAVEFORM_COUPLING -*/
   #define NIDMM_VAL_WAVEFORM_COUPLING_AC    0
   #define NIDMM_VAL_WAVEFORM_COUPLING_DC    1

   /*- Defined values for NIDMM_ATTR_CALCULATION_MODEL -*/
   #define NIDMM_VAL_CALC_MODEL_AUTO         -1
   #define NIDMM_VAL_CALC_MODEL_SERIES       0
   #define NIDMM_VAL_CALC_MODEL_PARALLEL     1

   /*- Defined values for NIDMM_ATTR_DC_BIAS -*/
   #define NIDMM_VAL_DC_BIAS_OFF          0
   #define NIDMM_VAL_DC_BIAS_ON           1

   /*- Defined values for the typeOfCompensation parameter of "niDMM_LC_Measurement_Compensation" -*/
   #define NIDMM_VAL_CABLE_COMP_NONE               0
   #define NIDMM_VAL_CABLE_COMP_OPEN               1
   #define NIDMM_VAL_CABLE_COMP_SHORT              2
   #define NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT     3

   /*- Defined values for the action parameter of "niDMM_control" -*/
   #define NIDMM_VAL_CONTROL_COMMIT                0   // Commit

   /*- Defined values for NIDMM_ATTR_TEMP_TRANSDUCER_TYPE -*/
   #define NIDMM_VAL_THERMOCOUPLE            IVIDMM_VAL_THERMOCOUPLE
   #define NIDMM_VAL_THERMISTOR              IVIDMM_VAL_THERMISTOR
   #define NIDMM_VAL_2_WIRE_RTD              IVIDMM_VAL_2_WIRE_RTD
   #define NIDMM_VAL_4_WIRE_RTD              IVIDMM_VAL_4_WIRE_RTD

   /*- Defined values for NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE -*/
   #define NIDMM_VAL_TEMP_REF_JUNC_FIXED     IVIDMM_VAL_TEMP_REF_JUNC_FIXED

   /*- Defined values for NIDMM_ATTR_TEMP_TC_TYPE -*/
   #define NIDMM_VAL_TEMP_TC_B               IVIDMM_VAL_TEMP_TC_B
   #define NIDMM_VAL_TEMP_TC_E               IVIDMM_VAL_TEMP_TC_E
   #define NIDMM_VAL_TEMP_TC_J               IVIDMM_VAL_TEMP_TC_J
   #define NIDMM_VAL_TEMP_TC_K               IVIDMM_VAL_TEMP_TC_K
   #define NIDMM_VAL_TEMP_TC_N               IVIDMM_VAL_TEMP_TC_N
   #define NIDMM_VAL_TEMP_TC_R               IVIDMM_VAL_TEMP_TC_R
   #define NIDMM_VAL_TEMP_TC_S               IVIDMM_VAL_TEMP_TC_S
   #define NIDMM_VAL_TEMP_TC_T               IVIDMM_VAL_TEMP_TC_T

   /*- Defined values for NIDMM_ATTR_TEMP_RTD_TYPE -*/
   #define NIDMM_VAL_TEMP_RTD_CUSTOM         0
   #define NIDMM_VAL_TEMP_RTD_PT3750         1
   #define NIDMM_VAL_TEMP_RTD_PT3851         2
   #define NIDMM_VAL_TEMP_RTD_PT3911         3
   #define NIDMM_VAL_TEMP_RTD_PT3916         4
   #define NIDMM_VAL_TEMP_RTD_PT3920         5
   #define NIDMM_VAL_TEMP_RTD_PT3928         6

   /*- Defined values for NIDMM_ATTR_TEMP_THERMISTOR_TYPE -*/
   #define NIDMM_VAL_TEMP_THERMISTOR_CUSTOM  0
   #define NIDMM_VAL_TEMP_THERMISTOR_44004   1
   #define NIDMM_VAL_TEMP_THERMISTOR_44006   2
   #define NIDMM_VAL_TEMP_THERMISTOR_44007   3

   /******************************************************************************/
   /*                       External Calibration Constants                       */
   /******************************************************************************/

   #define NIDMM_EXTCAL_MISCCAL_VREF                  0L
   #define NIDMM_EXTCAL_MISCCAL_RREF                  1L
   #define NIDMM_EXTCAL_MISCCAL_ZINT                  2L
   #define NIDMM_EXTCAL_MISCCAL_2WIRELEAKAGE          3L
   #define NIDMM_EXTCAL_MISCCAL_4WIRELEAKAGE          4L
   #define NIDMM_EXTCAL_MISCCAL_SECTION               5L
   #define NIDMM_EXTCAL_MISCCAL_VREF_DC_VOLTAGE       6L
   #define NIDMM_EXTCAL_MISCCAL_VREF_DC_CURRENT       7L
   #define NIDMM_EXTCAL_MISCCAL_VREF_AC_VOLTAGE       8L
   #define NIDMM_EXTCAL_MISCCAL_VREF_AC_CURRENT       9L
   #define NIDMM_EXTCAL_MISCCAL_VREF_RESISTANCE       10L
   #define NIDMM_EXTCAL_MISCCAL_VOLTAGE_AC_FILTER     11L

   #define NIDMM_EXTCAL_ACTION_ABORT                  0L
   #define NIDMM_EXTCAL_ACTION_SAVE                   1L

   #define NIDMM_EXTCAL_LC_OPEN                       0L
   #define NIDMM_EXTCAL_LC_SHORT                      1L
   #define NIDMM_EXTCAL_LC_25OHM                      2L
   #define NIDMM_EXTCAL_LC_1KOHM                      3L
   #define NIDMM_EXTCAL_LC_5KOHM                      4L
   #define NIDMM_EXTCAL_LC_100KOHM                    5L
   #define NIDMM_EXTCAL_LC_125OHM                     6L

   #define NIDMM_4022_CONFIG_GUARD                    0L
   #define NIDMM_4022_CONFIG_CURRENT_100_NANOAMP      2L
   #define NIDMM_4022_CONFIG_CURRENT_10_MICROAMP      3L
   #define NIDMM_4022_CONFIG_CURRENT_1_MILLIAMP       7L
   #define NIDMM_4022_CONFIG_DISCONNECT_AGND          8L

   /******************************************************************************/
   /*               NI-DMM Specific Driver Functions Declarations                */
   /******************************************************************************/

   /*- Init and Close Functions -*/
   ViStatus _VI_FUNC niDMM_init(
      ViRsrc      resourceName,
      ViBoolean   IDQuery,
      ViBoolean   reset,
      ViSession   *newVi);

   ViStatus _VI_FUNC niDMM_InitWithOptions(
      ViRsrc      resourceName,
      ViBoolean   IDQuery,
      ViBoolean   resetDevice,
      ViString    optionsString,
      ViSession   *newVi);

   ViStatus _VI_FUNC niDMM_close(
      ViSession   vi);

   /*- Error Functions -*/
   ViStatus _VI_FUNC niDMM_GetError(
      ViSession   vi,
      ViStatus    *errorCode,
      ViInt32     bufferSize,
      ViChar      description[]);

   ViStatus _VI_FUNC niDMM_GetErrorMessage(
      ViSession   vi,
      ViStatus    errorCode,
      ViInt32     bufferSize,
      ViChar      errMessage[]);

   ViStatus _VI_FUNC niDMM_ClearError(
      ViSession   vi);

   /*- Utility Functions -*/
   ViStatus _VI_FUNC niDMM_reset(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_self_test(
      ViSession   vi,
      ViInt16     *selfTestResult,
      ViChar      selfTestMessage[]);

   ViStatus _VI_FUNC niDMM_SelfCal(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_revision_query(
      ViSession   vi,
      ViChar      driverRev[],
      ViChar      instrRev[]);

   ViStatus _VI_FUNC niDMM_InvalidateAllAttributes(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_ResetWithDefaults(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_Disable(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_GetMeasurementPeriod(
      ViSession   vi,
      ViReal64    *period);

   /*- IviDmmBase Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureTrigger(
      ViSession   vi,
      ViInt32     trigSource,
      ViReal64    triggerDelay);

   ViStatus _VI_FUNC niDMM_Read(
      ViSession   vi,
      ViInt32     maxTime,
      ViReal64    *reading);

   ViStatus _VI_FUNC niDMM_Fetch(
      ViSession   vi,
      ViInt32     maxTime,
      ViReal64    *reading);

   ViStatus _VI_FUNC niDMM_Abort(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_Initiate(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_IsOverRange(
      ViSession   vi,
      ViReal64    measurementValue,
      ViBoolean   *isOverRange);

   ViStatus _VI_FUNC niDMM_IsUnderRange(
      ViSession   vi,
      ViReal64    measurementValue,
      ViBoolean   *isUnderRange);

   /*- IviDmmAcMeasurement Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureACBandwidth(
      ViSession   vi,
      ViReal64    minFreq,
      ViReal64    maxFreq);

   /*- IviDmmFrequencyMeasurement Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureFrequencyVoltageRange(
      ViSession   vi,
      ViReal64    frequencyVoltageRange);

   /*- IviDmmMultiPoint Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureMeasCompleteDest(
      ViSession   vi,
      ViInt32     destination);

   ViStatus _VI_FUNC niDMM_ConfigureMultiPoint(
      ViSession   vi,
      ViInt32     triggerCount,
      ViInt32     sampleCount,
      ViInt32     sampleTrigger,
      ViReal64    sampleInterval);

   ViStatus _VI_FUNC niDMM_ReadMultiPoint(
      ViSession   vi,
      ViInt32     maxTime,
      ViInt32     arraySize,
      ViReal64    readingArray[],
      ViInt32     *actualPts);

   ViStatus _VI_FUNC niDMM_FetchMultiPoint(
      ViSession   vi,
      ViInt32     maxTime,
      ViInt32     arraySize,
      ViReal64    readingArray[],
      ViInt32     *actualPts);

   /*- IviDmmTriggerSlope Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureTriggerSlope(
      ViSession   vi,
      ViInt32     polarity);

   /*- IviDmmSoftwareTrigger Functions -*/
   ViStatus _VI_FUNC niDMM_SendSoftwareTrigger(
      ViSession   vi);

   /*- IviDmmDeviceInfo Functions -*/
   ViStatus _VI_FUNC niDMM_GetApertureTimeInfo (
      ViSession   vi,
      ViReal64    *apertureTime,
      ViInt32     *apertureTimeUnits);

   /*- IviDmmAutoRangeValue Functions -*/
   ViStatus _VI_FUNC niDMM_GetAutoRangeValue(
      ViSession   vi,
      ViReal64    *autoRangeValue);

   /*- IviDmmAutoZero Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureAutoZeroMode(
      ViSession   vi,
      ViInt32     autoZeroMode);

   /*- IviDmmPowerLineFrequency Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigurePowerLineFrequency(
      ViSession   vi,
      ViReal64    frequency);

   /*- Extended Instrument Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureMeasurementDigits(
      ViSession   vi,
      ViInt32     measFunction,
      ViReal64    range,
      ViReal64    resolutionDigits);

   ViStatus _VI_FUNC niDMM_ConfigureMeasurementAbsolute(
      ViSession   vi,
      ViInt32     measFunction,
      ViReal64    range,
      ViReal64    resolutionAbsolute);

   ViStatus _VI_FUNC niDMM_ConfigureMeasCompleteSlope(
      ViSession   vi,
      ViInt32     polarity);

   ViStatus _VI_FUNC niDMM_ConfigureSampleTriggerSlope(
      ViSession   vi,
      ViInt32     polarity);

   ViStatus _VI_FUNC niDMM_ReadStatus(
      ViSession   vi,
      ViInt32     *acqBacklog,
      ViInt16     *acqDone);

   ViStatus _VI_FUNC niDMM_Control(
      ViSession   vi,
      ViInt32     action);

   /*- Functions for Advanced Measurement Configuration attributes -*/
   ViStatus _VI_FUNC niDMM_ConfigureADCCalibration(
      ViSession   vi,
      ViInt32     adcGainComp);

   ViStatus _VI_FUNC niDMM_ConfigureOffsetCompOhms(
      ViSession   vi,
      ViInt32     offsetCompOhms);

   ViStatus _VI_FUNC niDMM_ConfigureCurrentSource(
      ViSession   vi,
      ViReal64    diodeCurrentSrc);

   /*- Capacitance and Inductance Measurement Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureCableCompType(
      ViSession vi,
      ViInt32 typeOfCompensation);

   ViStatus _VI_FUNC niDMM_PerformOpenCableComp(
      ViSession vi,
      ViReal64  *conductance,
      ViReal64  *susceptance);

   ViStatus _VI_FUNC niDMM_PerformShortCableComp(
      ViSession vi,
      ViReal64  *resistance,
      ViReal64  *reactance);

   ViStatus _VI_FUNC niDMM_ConfigureOpenCableCompValues(
      ViSession vi,
      ViReal64  conductance,
      ViReal64  susceptance);

   ViStatus _VI_FUNC niDMM_ConfigureShortCableCompValues(
      ViSession vi,
      ViReal64  resistance,
      ViReal64  reactance);

   /*- Locking Functions --*/
   ViStatus _VI_FUNC niDMM_LockSession(
      ViSession   vi,
      ViBoolean   *callerHasLock);

   ViStatus _VI_FUNC niDMM_UnlockSession(
      ViSession   vi,
      ViBoolean   *callerHasLock);

   /*- Waveform Acquisition Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureWaveformAcquisition(
      ViSession   vi,
      ViInt32     function,
      ViReal64    range,
      ViReal64    rate,
      ViInt32     waveformPoints);

   ViStatus _VI_FUNC niDMM_ConfigureWaveformCoupling(
      ViSession   vi,
      ViInt32     coupling);

   ViStatus _VI_FUNC niDMM_FetchWaveform(
      ViSession   vi,
      ViInt32     maxTime,
      ViInt32     arraySize,
      ViReal64    waveformArray[],
      ViInt32     *actualPoints);

   ViStatus _VI_FUNC niDMM_ReadWaveform(
      ViSession   vi,
      ViInt32     maxTime,
      ViInt32     arraySize,
      ViReal64    waveformArray[],
      ViInt32     *actualPoints);

   /*- Set, Get, and Check Attribute Functions -*/
   ViStatus _VI_FUNC niDMM_GetAttributeViInt32(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViInt32       *value);

   ViStatus _VI_FUNC niDMM_SetAttributeViInt32(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViInt32       value);

   ViStatus _VI_FUNC niDMM_CheckAttributeViInt32(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViInt32       value);

   ViStatus _VI_FUNC niDMM_GetAttributeViReal64(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViReal64      *value);

   ViStatus _VI_FUNC niDMM_SetAttributeViReal64(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViReal64      value);

   ViStatus _VI_FUNC niDMM_CheckAttributeViReal64(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViReal64      value);

   ViStatus _VI_FUNC niDMM_GetAttributeViString(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViInt32       bufSize,
      ViChar        value[]);

   ViStatus _VI_FUNC niDMM_SetAttributeViString(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViChar        value[]);

   ViStatus _VI_FUNC niDMM_CheckAttributeViString(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViChar        value[]);

   ViStatus _VI_FUNC niDMM_GetAttributeViSession(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViSession     *value);

   ViStatus _VI_FUNC niDMM_SetAttributeViSession(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViSession     value);

   ViStatus _VI_FUNC niDMM_CheckAttributeViSession(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViSession     value);

   ViStatus _VI_FUNC niDMM_GetAttributeViBoolean(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViBoolean     *value);

   ViStatus _VI_FUNC niDMM_SetAttributeViBoolean(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViBoolean     value);

   ViStatus _VI_FUNC niDMM_CheckAttributeViBoolean(
      ViSession     vi,
      ViConstString channelName,
      ViAttr        attributeId,
      ViBoolean     value);

   /*- Import and Export Session Configuration Functions -*/
   ViStatus _VI_FUNC niDMM_ImportAttributeConfigurationFile(
      ViSession vi,
      ViConstString filePath);

   ViStatus _VI_FUNC niDMM_ExportAttributeConfigurationFile(
      ViSession vi,
      ViConstString filePath);

   ViStatus _VI_FUNC niDMM_ImportAttributeConfigurationBuffer(
      ViSession vi,
      ViInt32 size,
      const ViAddr configuration);

   ViStatus _VI_FUNC niDMM_ExportAttributeConfigurationBuffer(
      ViSession vi,
      ViInt32 size,
      ViAddr configuration);

   /*- Interchangeability Checking Functions -*/
   ViStatus _VI_FUNC niDMM_GetNextCoercionRecord(
      ViSession   vi,
      ViInt32     bufferSize,
      ViChar      record[]);

   ViStatus _VI_FUNC niDMM_GetNextInterchangeWarning(
      ViSession   vi,
      ViInt32     bufferSize,
      ViChar      warnString[]);

   ViStatus _VI_FUNC niDMM_ResetInterchangeCheck(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_ClearInterchangeWarnings(
      ViSession   vi);

   /*- 4022 Functions -*/
   ViStatus _VI_FUNC niDMM_4022Control(
      ViRsrc      resourceName,
      ViInt32     configuration);

   /*- Channel Info Functions -*/
   ViStatus _VI_FUNC niDMM_GetChannelName(
      ViSession   vi,
      ViInt32     index,
      ViInt32     bufferSize,
      ViChar      name[]);

   /*- External Cal Init and Close Functions -*/
   ViStatus _VI_FUNC niDMM_InitExtCal(
      ViRsrc      resourceName,
      ViChar      password[],
      ViSession   *newVi);

   ViStatus _VI_FUNC niDMM_CloseExtCal(
      ViSession   vi,
      ViInt32     action);

   /*- Adjust Functions -*/
   ViStatus _VI_FUNC niDMM_CalAdjustLinearization(
      ViSession   vi,
      ViInt32     mode,
      ViReal64    range,
      ViReal64    inputR,
      ViReal64    expectedValue);

   ViStatus _VI_FUNC niDMM_CalAdjustGain(
      ViSession   vi,
      ViInt32     mode,
      ViReal64    range,
      ViReal64    inputR,
      ViReal64    expectedValue);

   ViStatus _VI_FUNC niDMM_CalAdjustOffset(
      ViSession   vi,
      ViInt32     mode,
      ViReal64    range,
      ViReal64    inputR);

   ViStatus _VI_FUNC niDMM_CalAdjustMisc(
      ViSession   vi,
      ViInt32     type);

   ViStatus _VI_FUNC niDMM_CalAdjustLC(
      ViSession   vi,
      ViInt32     type);

   ViStatus _VI_FUNC niDMM_CalAdjustACFilter(
      ViSession   vi,
      ViInt32     mode,
      ViReal64    range,
      ViReal64    frequency,
      ViReal64    expectedValue);

   /*- Utility Functions -*/
   ViStatus _VI_FUNC niDMM_RestoreLastExtCalConstants(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_SetCalPassword(
      ViSession   vi,
      ViChar      oldPassword[],
      ViChar      newPassword[]);

   ViStatus _VI_FUNC niDMM_GetExtCalRecommendedInterval(
      ViSession   vi,
      ViInt32    *months);

   ViStatus _VI_FUNC niDMM_SetCalUserDefinedInfo(
      ViSession   vi,
      ViChar      info[]);

   ViStatus _VI_FUNC niDMM_GetCalUserDefinedInfoMaxSize(
      ViSession   vi,
      ViInt32    *infoSize);

   ViStatus _VI_FUNC niDMM_GetCalUserDefinedInfo(
      ViSession   vi,
      ViInt32     bufferSize,
      ViChar      info[]);

   ViStatus _VI_FUNC niDMM_GetSelfCalSupported(
      ViSession   vi,
      ViBoolean  *selfCalSupported);

   ViStatus _VI_FUNC niDMM_GetCalDateAndTime(
      ViSession   vi,
      ViInt32     calType,
      ViInt32     *month,
      ViInt32     *day,
      ViInt32     *year,
      ViInt32     *hour,
      ViInt32     *minute);

   ViStatus _VI_FUNC niDMM_GetCalCount(
      ViSession   vi,
      ViInt32     calType,
      ViInt32     *count);

   ViStatus _VI_FUNC niDMM_GetLastCalTemp(
      ViSession   vi,
      ViInt32     calType,
      ViReal64    *temperature);

   ViStatus _VI_FUNC niDMM_GetDevTemp(
      ViSession   vi,
      ViString    reserved,
      ViReal64    *temperature);

   /*- Temperature Measurement Functions -*/
   ViStatus _VI_FUNC niDMM_ConfigureTransducerType(
      ViSession vi,
      ViInt32 transducerType);

   ViStatus _VI_FUNC niDMM_ConfigureThermocouple(
      ViSession vi,
      ViInt32 thermocoupleType,
      ViInt32 refJunctionType);

   ViStatus _VI_FUNC niDMM_ConfigureFixedRefJunction(
      ViSession vi,
      ViReal64 fixedRefJunction);

   ViStatus _VI_FUNC niDMM_ConfigureRTDType(
      ViSession vi,
      ViInt32 rtdType,
      ViReal64 resistance);

   ViStatus _VI_FUNC niDMM_ConfigureRTDCustom(
      ViSession vi,
      ViReal64 a,
      ViReal64 b,
      ViReal64 c);

   ViStatus _VI_FUNC niDMM_ConfigureThermistorType(
      ViSession vi,
      ViInt32 thermistorType);

   ViStatus _VI_FUNC niDMM_ConfigureThermistorCustom(
      ViSession vi,
      ViReal64 a,
      ViReal64 b,
      ViReal64 c);

   /*- IviDmmObsolete.h included for backwards compatibility -*/
   #include "nidmmObsolete.h"

   /******************************************************************************/
   /*                              END INCLUDE FILE                              */
   /******************************************************************************/

   #if defined(__cplusplus) || defined(__cplusplus__)
}
   #endif

#endif // __NIDMM__HEADER
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nidmmObsolete.h sha256=4fdf88a918af1a4258823ed094eba9fb179ae95c61ee245ac454bec1c916a3ff bytes=21335 -->
## FILE: imports/include/nidmmObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nidmmObsolete.h`
- sha256: `4fdf88a918af1a4258823ed094eba9fb179ae95c61ee245ac454bec1c916a3ff`
- bytes: 21335

````c
/*****************************************************************************
 *                            N I - D M M
 *----------------------------------------------------------------------------
 *    Copyright (c) National Instruments 2012.  All Rights Reserved.
 *----------------------------------------------------------------------------
 *
 * Title:       nidmmObsolete.h
 * Purpose:     Declarations of constants and functions that are now obsolete
 *              in the NI-DMM driver.
 *              They are defined here to maintain backward compatibility with
 *              previous versions of driver. New applications should not use
 *              any of the definitions in this file. Instead, they must
 *              use definitions from the nidmm.h header file.
 *****************************************************************************/

#ifndef __NIDMM__HEADER_OBSOLETE
   #define __NIDMM__HEADER_OBSOLETE

   #if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
   #endif

   /******************************************************************************/
   /*                               Include Files                                */
   /******************************************************************************/

   #define IVI_DO_NOT_INCLUDE_VISA_HEADERS
   #include "IviDmm.h"
   #include "ivi.h"
   #undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

   /*********************************************************************************
   * This section lists all attributes and values that became obsolete. Do not use  *
   * these attributes and values in your drivers and applications.                  *
   *********************************************************************************/

   #if (defined(_EXPORTING) && defined(_IVI_mswin32_))
      #define NIDMM_DECLSPEC    __declspec(dllexport)
   #else
      #define NIDMM_DECLSPEC
   #endif

   /*  Use NIDMM_ATTR_CHANNEL_COUNT instead */
   #define NIDMM_ATTR_NUM_CHANNELS             IVI_ATTR_NUM_CHANNELS              /* ViInt32, read only*/
   /*  Use NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX instead */
   #define NIDMM_ATTR_SPECIFIC_PREFIX          IVI_ATTR_SPECIFIC_PREFIX           /* ViString, read only*/
   /*  Use NIDMM_ATTR_SPECIFIC_DRIVER_REVISION instead */
   #define NIDMM_ATTR_DRIVER_REVISION          IVI_ATTR_DRIVER_REVISION           /* ViString, read only*/
   /*  Use NIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION instead */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION   IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION /* ViInt32, read only  */
   /*  Use NIDMM_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION instead */
   #define NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION   IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION /* ViInt32, read only  */
   /*  Use NIDMM_ATTR_QUERY_INSTRUMENT_STATUS instead */
   #define NIDMM_ATTR_QUERY_INSTR_STATUS       IVI_ATTR_QUERY_INSTR_STATUS        /* ViBoolean */
   /*  Use NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION instead */
   #define NIDMM_ATTR_DRIVER_MAJOR_VERSION     IVI_ATTR_DRIVER_MAJOR_VERSION      /* ViInt32, read only  */
   /*  Use NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION instead */
   #define NIDMM_ATTR_DRIVER_MINOR_VERSION     IVI_ATTR_DRIVER_MINOR_VERSION      /* ViInt32, read only  */
   #define NIDMM_ATTR_PRIMARY_ERROR            IVI_ATTR_PRIMARY_ERROR             /* ViInt32   */
   #define NIDMM_ATTR_SECONDARY_ERROR          IVI_ATTR_SECONDARY_ERROR           /* ViInt32   */
   #define NIDMM_ATTR_ERROR_ELABORATION        IVI_ATTR_ERROR_ELABORATION         /* ViString  */
   #define NIDMM_ATTR_ENGINE_MAJOR_VERSION     IVI_ATTR_ENGINE_MAJOR_VERSION      /* ViInt32, read only  */
   #define NIDMM_ATTR_ENGINE_MINOR_VERSION     IVI_ATTR_ENGINE_MINOR_VERSION      /* ViInt32, read only  */
   #define NIDMM_ATTR_ENGINE_REVISION          IVI_ATTR_ENGINE_REVISION           /* ViString, read-only */
   #define NIDMM_ATTR_VISA_RM_SESSION          IVI_ATTR_VISA_RM_SESSION           /* ViSession, read only */
   #define NIDMM_ATTR_DEFER_UPDATE             IVI_ATTR_DEFER_UPDATE              /* ViBoolean */
   #define NIDMM_ATTR_RETURN_DEFERRED_VALUES   IVI_ATTR_RETURN_DEFERRED_VALUES    /* ViBoolean */
   /*  Use NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR instead */
   #define NIDMM_ATTR_RESOURCE_DESCRIPTOR      IVI_ATTR_RESOURCE_DESCRIPTOR       /* ViString, read only */
   /*  Use NIDMM_ATTR_RESOLUTION_ABSOLUTE */
   #define NIDMM_ATTR_RESOLUTION               NIDMM_ATTR_RESOLUTION_DIGITS       /* ViReal64  */
   /*  Use NIDMM_ATTR_TRIGGER */
   #define NIDMM_ATTR_START_TRIGGER            (NIDMM_ATTR_BASE + 8L)             /* ViInt32   */
   #define NIDMM_ATTR_START_TRIG_SLOPE         (NIDMM_ATTR_BASE + 9L)             /* ViInt32   */
   #define NIDMM_ATTR_SAMPLE_TRIGGER_DELAY     (NIDMM_ATTR_BASE + 11L)            /* ViReal64  */
   #define NIDMM_ATTR_OLD_TRIGGER_MODEL        (NIDMM_ATTR_BASE + 12L)            /* ViBoolean */
   #define NIDMM_ATTR_CHAN_NAMES               (NIDMM_ATTR_BASE + 4L)             /* ViString, read only */
   #define NIDMM_ATTR_ID_QUERY_RESPONSE        (NIDMM_ATTR_BASE + 1L)             /* ViString, read only */
   #define NIDMM_ATTR_AI_NUM_CHANNELS          (NIDMM_ATTR_BASE + 5L)             /* ViInt32, read only  */
   #define NIDMM_ATTR_FILTER_NOTCH             (NIDMM_ATTR_BASE + 6L)             /* ViInt32, read only  */
   #define NIDMM_ATTR_CONVER_PER_SAMPLE        (NIDMM_ATTR_BASE + 7L)             /* ViInt32, read only  */
   #define NIDMM_ATTR_AI_BUFFER_SIZE           (NIDMM_ATTR_BASE + 13L)            /* ViInt32   */
   #define NIDMM_ATTR_SAMPLE_DELAY_MODE        (NIDMM_ATTR_BASE + 31L)            /* ViInt32  */
   #define NIDMM_VAL_3_5_DIGITS                (3.5)
   #define NIDMM_VAL_4_5_DIGITS                (4.5)
   #define NIDMM_VAL_5_5_DIGITS                (5.5)
   #define NIDMM_VAL_6_5_DIGITS                (6.5)
   #define NIDMM_VAL_7_5_DIGITS                (7.5)
   /*  Use NIDMM_VAL_SOFTWARE_TRIG instead */
   #define NIDMM_VAL_SW_TRIG_FUNC              IVIDMM_VAL_SW_TRIG_FUNC
   /*  Use NIDMM_VAL_POSITIVE instead */
   #define NIDMM_VAL_POS                       IVIDMM_VAL_POSITIVE
   /*  Use NIDMM_VAL_NEGATIVE instead */
   #define NIDMM_VAL_NEG                       IVIDMM_VAL_NEGATIVE
   /*  Use NIDMM_VAL_MILLIAMP instead */
   #define NIDMM_VAL_1_MILIAMP         0.001
   #define NIDMM_WARN_FREQ_UNDERRANGE          (NIDMM_WARN_EXT_STATUS_BASE + 0x80) // 0x3FFA4F80 1073368960
   /*  Use NIDMM_VAL_PXI_TRIG<0-7> instead */
   #define NIDMM_VAL_TTL0                      IVIDMM_VAL_TTL0
   #define NIDMM_VAL_TTL1                      IVIDMM_VAL_TTL1
   #define NIDMM_VAL_TTL2                      IVIDMM_VAL_TTL2
   #define NIDMM_VAL_TTL3                      IVIDMM_VAL_TTL3
   #define NIDMM_VAL_TTL4                      IVIDMM_VAL_TTL4
   #define NIDMM_VAL_TTL5                      IVIDMM_VAL_TTL5
   #define NIDMM_VAL_TTL6                      IVIDMM_VAL_TTL6
   #define NIDMM_VAL_TTL7                      IVIDMM_VAL_TTL7
   /*  Use NIDMM_VAL_LBR_TRIG<0-1> instead */
   #define NIDMM_VAL_LBR_TRIG_0           (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 3L)
   #define NIDMM_VAL_LBR_TRIG_1           (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 4L)
   /*  Use NIDMM_VAL_AUX_TRIG1 instead */
   #define NIDMM_VAL_AUX_TRIG_1           (NIDMM_VAL_TRIGGER_SOURCE_SPECIFIC_EXT_BASE + 1L)
   /*  Internal constants used in the NI 407x external calibration procedure */
   #define NIDMM_EXTCAL_MISCCAL_MAX_TYPES      6L
   #define NIDMM_EXTCAL_LC_MAX_STAGES          6L


   /*********************************************************************************
   * This section lists all driver functions that became obsolete. Do not use       *
   * these functions in your drivers and applications.                              *
   *********************************************************************************/
   ViStatus _VI_FUNC niDMM_error_message(
      ViSession   vi,
      ViStatus    errorCode,
      ViChar      errMessage[]);

   ViStatus _VI_FUNC niDMM_GetErrorInfo(
      ViSession   vi,
      ViStatus    *primaryError,
      ViStatus    *secondaryError,
      ViChar      errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

   ViStatus _VI_FUNC niDMM_ClearErrorInfo(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_error_query(
      ViSession   vi,
      ViStatus    *errorCode,
      ViChar      errMessage[]);

   ViStatus _VI_FUNC niDMM_Configure(
      ViSession   vi,
      ViInt32     measFunction,
      ViReal64    range,
      ViReal64    resolution,
      ViReal64    minFrequency,
      ViReal64    maxFrequency);

   ViStatus _VI_FUNC niDMM_ConfigureMeasurement(
      ViSession   vi,
      ViInt32     measFunction,
      ViReal64    range,
      ViReal64    resolution);

   ViStatus _VI_FUNC niDMM_ConfigureSampleDelayMode(
      ViSession   vi,
      ViInt32     sampleDelayMode);

   ViStatus _VI_FUNC niDMM_Measure(
      ViSession   vi,
      ViInt32     measFunction,
      ViInt32     maxTime,
      ViReal64    *reading);

   ViStatus _VI_FUNC niDMM_MeasureMultiPoint(
      ViSession   vi,
      ViInt32     function,
      ViInt32     maxTime,
      ViInt32     arraySize,
      ViReal64    readingArray[],
      ViInt32     *actualPts);

   ViStatus _VI_FUNC niDMM_ConfigureMeasurementComplete(
      ViSession   vi,
      ViInt32     destination,
      ViInt32     slope);

   ViStatus _VI_FUNC niDMM_SendSWTrigger(
      ViSession   vi);

   ViStatus _VI_FUNC niDMM_SetPowerlineFrequency(
      ViSession   vi,
      ViReal64    frequency);

   ViStatus _VI_FUNC niDMM_ConfigureStartTrigger(
      ViSession   vi,
      ViInt32     source,
      ViInt32     slope);

   ViStatus _VI_FUNC niDMM_SetAutoZero(
      ViSession   vi,
      ViInt32     enable);

   ViStatus _VI_FUNC niDMM_GetDigitsOfPrecision(
      ViSession   vi,
      ViReal64    *digits);

   ViStatus _VI_FUNC niDMM_ConvertDigitsToAbsolute(
      ViInt32   productID,
      ViInt32   function,
      ViReal64  range,
      ViReal64  resolution,
      ViPReal64 absoluteUnits);

   ViStatus _VI_FUNC niDMM_ConvertAbsoluteToDigits(
      ViInt32   productID,
      ViInt32   function,
      ViReal64  range,
      ViReal64  resolution,
      ViPReal64 digits);

   ViStatus _VI_FUNC niDMM_FormatMeasDigitsResolution(
      ViInt32  productID,
      ViInt32  function,
      ViReal64 range,
      ViReal64 resolution,
      ViReal64 reading,
      ViChar   modeString[],
      ViChar   rangeString[],
      ViChar   dataString[]);

   ViStatus _VI_FUNC niDMM_FormatMeasAbsoluteResolution(
      ViInt32  productID,
      ViInt32  function,
      ViReal64 range,
      ViReal64 resolution,
      ViReal64 reading,
      ViChar   modeString[],
      ViChar   rangeString[],
      ViChar   dataString[]);

   ViStatus _VI_FUNC niDMM_FormatMeas(
      ViInt32     function,
      ViReal64    range,
      ViReal64    resolution,
      ViReal64    reading,
      ViChar      modeString[],
      ViChar      rangeString[],
      ViChar      dataString[]);

   ViStatus _VI_FUNC niDMM_FormatMeasAbsolute(
      ViInt32     function,
      ViReal64    range,
      ViReal64    resolution,
      ViReal64    reading,
      ViChar      modeString[],
      ViChar      rangeString[],
      ViChar      dataString[]);

   ViStatus _VI_FUNC niDMM_CalculateAccuracy(
      ViSession   vi,
      ViReal64    frequency,
      ViReal64    *multiplier,
      ViReal64    *offset);

   ViStatus _VI_FUNC niDMM_GetViReal64Type(
      ViSession   vi,
      ViReal64    value,
      ViInt32*    type);

   /*********************************************************************************
   * This section lists constants for some of the error codes returned by NI-DMM.   *
   * Do not use these constants in your drivers and applications as they may vary   *
   * by driver release or device model.                                             *
   *********************************************************************************/

   #define NIDMM_ERROR_MAX_TIME_EXCEEDED              IVIDMM_ERROR_MAX_TIME_EXCEEDED        // 0xBFFA2003 (-1074126845)
   #define NIDMM_ERROR_UNKNOWN_DEVICE                 (NIDMM_ERROR_BASE + 0L)               // 0xBFFA4000 (-1074118656)
   #define NIDMM_ERROR_INVALID_DESCRIPTOR             (NIDMM_ERROR_BASE + 1L)               // 0xBFFA4001 (-1074118655)
   #define NIDMM_ERROR_INVALID_DRIVER_SETUP           (NIDMM_ERROR_BASE + 2L)               // 0xBFFA4002 (-1074118654)
   #define NIDMM_ERROR_ATTRIBUTE_INVALIDATED          (NIDMM_ERROR_BASE + 3L)               // 0xBFFA4003 (-1074118653)
   #define NIDMM_ERROR_INVALID_TRIG                   (NIDMM_ERROR_BASE + 4L)               // 0xBFFA4004 (-1074118652)
   #define NIDMM_ERROR_TRANSFER_IN_PROGRESS           (NIDMM_ERROR_BASE + 5L)               // 0xBFFA4005 (-1074118651)
   #define NIDMM_ERROR_INTERNAL                       (NIDMM_ERROR_BASE + 6L)               // 0xBFFA4006 (-1074118650)
   #define NIDMM_ERROR_NUM_SESSIONS_EXCEEDED          (NIDMM_ERROR_BASE + 7L)               // 0xBFFA4007 (-1074118649)
   #define NIDMM_ERROR_REV_QUERY_FAILURE              (NIDMM_ERROR_BASE + 8L)               // 0xBFFA4008 (-1074118648)
   #define NIDMM_ERROR_AC_TEST_FAILURE                (NIDMM_ERROR_BASE + 9L)               // 0xBFFA4009 (-1074118647)
   #define NIDMM_ERROR_DC_TEST_FAILURE                (NIDMM_ERROR_BASE + 10L)              // 0xBFFA400A (-1074118646)
   #define NIDMM_ERROR_RESISTANCE_TEST_FAILURE        (NIDMM_ERROR_BASE + 11L)              // 0xBFFA400B (-1074118645)
   #define NIDMM_ERROR_INVALID_SCAN_CONFIG            (NIDMM_ERROR_BASE + 12L)              // 0xBFFA400C (-1074118644)
   #define NIDMM_ERROR_INVALID_AUTO_RANGE             (NIDMM_ERROR_BASE + 13L)              // 0xBFFA400D (-1074118643)
   #define NIDMM_ERROR_INVALID_RESOLUTION             (NIDMM_ERROR_BASE + 14L)              // 0xBFFA400E (-1074118642)
   #define NIDMM_ERROR_DATA_NOT_AVAILABLE             (NIDMM_ERROR_BASE + 15L)              // 0xBFFA400F (-1074118641)
   #define NIDMM_ERROR_SELF_CAL_OVERRANGE             (NIDMM_ERROR_BASE + 16L)              // 0xBFFA4010 (-1074118640)
   #define NIDMM_ERROR_DEVICE_IN_USE_BY_PROC          (NIDMM_ERROR_BASE + 17L)              // 0xBFFA4011 (-1074118639)
   #define NIDMM_ERROR_EXT_TRIG_LINE_IN_USE           (NIDMM_ERROR_BASE + 18L)              // 0xBFFA4012 (-1074118638)
   #define NIDMM_ERROR_CALIBRATION                    (NIDMM_ERROR_BASE + 19L)              // 0xBFFA4013 (-1074118637)
   #define NIDMM_ERROR_DRIVER_INITIALIZATION          (NIDMM_ERROR_BASE + 20L)              // 0xBFFA4014 (-1074118636)
   #define NIDMM_ERROR_BUFFER_OVERWRITE               (NIDMM_ERROR_BASE + 21L)              // 0xBFFA4015 (-1074118635)
   #define NIDMM_ERROR_INVALID_MODE                   (NIDMM_ERROR_BASE + 22L)              // 0xBFFA4016 (-1074118634)

   #define NIDMM_ERROR_SELF_TEST_FAILURE              (NIDMM_ERROR_BASE + 23L)              // 0xBFFA4017 (-1074118633)
   #define NIDMM_ERROR_WAVEFORM_CONFIG                (NIDMM_ERROR_BASE + 24L)              // 0xBFFA4018 (-1074118632)
   #define NIDMM_ERROR_WAVEFORM_ACQ_TIME              (NIDMM_ERROR_BASE + 25L)              // 0xBFFA4019 (-1074118631)
   #define NIDMM_ERROR_INVALID_MEAS_COMP_DEST         (NIDMM_ERROR_BASE + 26L)              // 0xBFFA401A (-1074118630)
   #define NIDMM_ERROR_CABLE_COMP_NOT_ALLOWED         (NIDMM_ERROR_BASE + 27L)              // 0xBFFA401B (-1074118629)
   #define NIDMM_ERROR_INVALID_CABLE_COMP_VALUE       (NIDMM_ERROR_BASE + 28L)              // 0xBFFA401C (-1074118628)
   #define NIDMM_ERROR_CABLE_COMP_FAILED              (NIDMM_ERROR_BASE + 29L)              // 0xBFFA401D (-1074118627)
   #define NIDMM_ERROR_INVALID_CABLE_COMP_SETUP       (NIDMM_ERROR_BASE + 30L)              // 0xBFFA401E (-1074118626)
   #define NIDMM_ERROR_SERIAL_PORT_ERROR              (NIDMM_ERROR_BASE + 31L)              // 0xBFFA401F (-1074118625)
   #define NIDMM_ERROR_AVERAGING_NOT_ALLOWED          (NIDMM_ERROR_BASE + 32L)              // 0xBFFA4020 (-1074118624)
   #define NIDMM_ERROR_COMMIT_WHILE_RUNNING           (NIDMM_ERROR_BASE + 33L)              // 0xBFFA4021 (-1074118623)
   #define NIDMM_ERROR_INVALID_BUFFER_SIZE            (NIDMM_ERROR_BASE + 34L)              // 0xBFFA4022 (-1074118622)
   #define NIDMM_ERROR_INVALID_APERTURE_AVG_TIME      (NIDMM_ERROR_BASE + 35L)              // 0xBFFA4023 (-1074118621)
   #define NIDMM_ERROR_TEMPERATURE_RESOLUTION         (NIDMM_ERROR_BASE + 36L)              // 0xBFFA4024 (-1074118620)

   #define NIDMM_ERROR_FIRMWARE_LOAD                  (NIDMM_ERROR_BASE + 800L)             // 0xBFFA4320 (-1074117856)
   #define NIDMM_ERROR_DRIVER_TIMEOUT                 (NIDMM_ERROR_BASE + 801L)             // 0xBFFA4321 (-1074117855)
   #define NIDMM_ERROR_ACQ_IN_PROGRESS                (NIDMM_ERROR_BASE + 802L)             // 0xBFFA4322 (-1074117854)
   #define NIDMM_ERROR_VERSION_MISMATCH               (NIDMM_ERROR_BASE + 803L)             // 0xBFFA4323 (-1074117853)
   #define NIDMM_ERROR_EEPROM_NOT_RESERVED            (NIDMM_ERROR_BASE + 804L)             // 0xBFFA4324 (-1074117852)
   #define NIDMM_ERROR_SET_SA_SOURCE_TO_AUXIO         (NIDMM_ERROR_BASE + 805L)             // 0xBFFA4325 (-1074117851)
   #define NIDMM_ERROR_SCANLIST_SIZE_EXCEEDED         (NIDMM_ERROR_BASE + 806L)             // 0xBFFA4326 (-1074117850)
   #define NIDMM_ERROR_FEATURE_NOT_SUPPORTED          (NIDMM_ERROR_BASE + 807L)             // 0xBFFA4327 (-1074117849)
   #define NIDMM_ERROR_BAD_READ                       (NIDMM_ERROR_BASE + 808L)             // 0xBFFA4328 (-1074117848)
   #define NIDMM_ERROR_AZ_REQUIRED                    (NIDMM_ERROR_BASE + 809L)             // 0xBFFA4329 (-1074117847)
   #define NIDMM_ERROR_MAX_SETTLE_TIME_EXCEEDED       (NIDMM_ERROR_BASE + 810L)             // 0xBFFA432A (-1074117846)
   #define NIDMM_ERROR_AZ_REQUIRED_FOR_75             (NIDMM_ERROR_BASE + 812L)             // 0xBFFA432C (-1074117844)

   #define NIDMM_ERROR_INTERNAL_HARDWARE              (NIDMM_ERROR_BASE + 900L)             // 0xBFFA4384 (-1074117756)
   #define NIDMM_ERROR_EEPROM_WRITE                   (NIDMM_ERROR_BASE + 901L)             // 0xBFFA4385 (-1074117755)
   #define NIDMM_ERROR_SERIAL_PORT_RESET_FAIL         (NIDMM_ERROR_BASE + 902L)             // 0xBFFA4386 (-1074117754)
   #define NIDMM_ERROR_DEVICE_NOT_READY               (NIDMM_ERROR_BASE + 903L)             // 0xBFFA4387 (-1074117753)
   #define NIDMM_ERROR_HARDWARE_FIFO_OVERFLOW         (NIDMM_ERROR_BASE + 904L)             // 0xBFFA4388 (-1074117752)
   #define NIDMM_ERROR_HARDWARE_STATUS_INVALID        (NIDMM_ERROR_BASE + 905L)             // 0xBFFA4389 (-1074117751)

   #define NIDMM_ERROR_EXTCAL_INVALID_PASSWORD        (NIDMM_ERROR_EXTCAL_ERROR_BASE + 0L)  // 0xBFFA4200 (-1074118144)
   #define NIDMM_ERROR_EXTCAL_INCOMPLETE_CAL          (NIDMM_ERROR_EXTCAL_ERROR_BASE + 1L)  // 0xBFFA4201 (-1074118143)
   #define NIDMM_ERROR_EXTCAL_CAL_SESSION_NOT_VALID   (NIDMM_ERROR_EXTCAL_ERROR_BASE + 2L)  // 0xBFFA4202 (-1074118142)
   #define NIDMM_ERROR_EXTCAL_SIMULATION_NOT_ALLOWED  (NIDMM_ERROR_EXTCAL_ERROR_BASE + 3L)  // 0xBFFA4203 (-1074118141)
   #define NIDMM_ERROR_EXTCAL_RESOURCE_NOT_AVAILABLE  (NIDMM_ERROR_EXTCAL_ERROR_BASE + 4L)  // 0xBFFA4204 (-1074118140)
   #define NIDMM_ERROR_EXTCAL_SESSION_ALREADY_OPEN    (NIDMM_ERROR_EXTCAL_ERROR_BASE + 6L)  // 0xBFFA4206 (-1074118138)
   #define NIDMM_ERROR_EXTCAL_IMPROPER_CLOSE          (NIDMM_ERROR_EXTCAL_ERROR_BASE + 7L)  // 0xBFFA4207 (-1074118137)
   #define NIDMM_ERROR_EXTCAL_IMPROPER_INIT           (NIDMM_ERROR_EXTCAL_ERROR_BASE + 8L)  // 0xBFFA4208 (-1074118136)
   #define NIDMM_ERROR_EXTCAL_BAD_LEAKAGE_RESISTANCE  (NIDMM_ERROR_EXTCAL_ERROR_BASE + 9L)  // 0xBFFA4209 (-1074118135)
   #define NIDMM_ERROR_EXTCAL_DEPENDENCY_CHECK_FAILED (NIDMM_ERROR_EXTCAL_ERROR_BASE + 10L) // 0xBFFA420A (-1074118134)
   #define NIDMM_ERROR_EXTCAL_BAD_GAIN                (NIDMM_ERROR_EXTCAL_ERROR_BASE + 11L) // 0xBFFA420B (-1074118133)
   #define NIDMM_ERROR_EXTCAL_BAD_FILTER              (NIDMM_ERROR_EXTCAL_ERROR_BASE + 12L) // 0xBFFA420C (-1074118132)
   #define NIDMM_ERROR_EXTCAL_BAD_LC_COEFF            (NIDMM_ERROR_EXTCAL_ERROR_BASE + 13L) // 0xBFFA420D (-1074118131)
   #define NIDMM_ERROR_EXTCAL_BAD_LINEARIZATION       (NIDMM_ERROR_EXTCAL_ERROR_BASE + 14L) // 0xBFFA420E (-1074118130)
   #define NIDMM_ERROR_EXTCAL_BAD_OFFSET              (NIDMM_ERROR_EXTCAL_ERROR_BASE + 15L) // 0xBFFA420F (-1074118129)
   #define NIDMM_ERROR_EXTCAL_LEAKAGE_DEPRECATED      (NIDMM_ERROR_EXTCAL_ERROR_BASE + 16L) // 0xBFFA4210 (-1074118128)



   /****************************************************************************
    *---------------------------- End Include File ----------------------------*
    ****************************************************************************/

   #if defined(__cplusplus) || defined(__cplusplus__)
}
   #endif

#endif // __NIDMM__HEADER_OBSOLETE
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nierr_Status.cpp sha256=22ddb21bc718fea587357769e122af767fbf82cdad7420963a5699ba416acb83 bytes=2769 -->
## FILE: imports/include/nierr_Status.cpp

- repository: `ni/grpc-device`
- source_path: `imports/include/nierr_Status.cpp`
- sha256: `22ddb21bc718fea587357769e122af767fbf82cdad7420963a5699ba416acb83`
- bytes: 2769

````cpp
/*!
   \file nierr_Status.c
   \brief Status C functions, the low level manipulator for Status.

   This file is a pared-down version of nierr_Status.c in the nierr component,
   with required elements defined in ni-build and additional dependencies removed.
   This file also includes functions defined in jsonz/cgenerate.c
*/
/*
   Copyright (c) 2012-2022 National Instruments Corporation.
   All rights reserved.
*/

/* includes... */
#include "nierr_Status.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define STATUS_MIN_DESC_SIZE 512

#define STATUS_JSON_MAX_CAPACITY ((uint32_t)(INT32_MAX))  /* quite arbitrary, but big enough. */

char *initJsonBuffer(char* buf, size_t size, const char* initial_json)
{
   const char JSONZ_TERM_CHAR = 'J';
   size_t len;

   if (!initial_json)
   {
      len = strlen(buf);
      if (size <= len+1) 
      {
         return NULL; /* not enough space in buffer */
      }
   }
   else
   {
      len = strlen(initial_json);
      if (size <= len+1)
      {
         return NULL; /* not enough space in buffer */
      }

      strncpy(buf, initial_json, len+1);
   }

   memset(buf+len+1 /*+1 from the null char*/, 0, size-len-1-1 /* the last -1 from termination char*/);
   buf[size-1] = JSONZ_TERM_CHAR;
   return buf+len-1;
}

uint32_t calcDescSizeToAllocate_(uint32_t size)
{
   if (size <= STATUS_MIN_DESC_SIZE) return STATUS_MIN_DESC_SIZE;
   /* else, round up to the next highest power of 2 - http://graphics.stanford.edu/~seander/bithacks.html#RoundUpPowerOf2
    * This is done for performance and minimize memory fragmentation
    */
   --size;
   size |= (size >> 1);
   size |= (size >> 2);
   size |= (size >> 4);
   size |= (size >> 8);
   size |= (size >> 16);
   ++size;
   return size;
}

bool kNICCall nierr_defaultReallocJson(nierr_Status *s, uint32_t size)
{
   char *json;

   if (size == 0)
   {
      if (s->json)
      {
         free(s->json);
         s->capacity = 0;
         s->json = NULL;
      }
      return true;
   }

   if (size <= s->capacity) return true; // we're never shrinking json
   if (size > STATUS_JSON_MAX_CAPACITY) return false; // avoid overflow

   /* alright, we're growing the json here */
   size = calcDescSizeToAllocate_(size);
   json = (char*)malloc(size);
   if (!json) return false;

   initJsonBuffer(json, size, (s->json)? s->json : NIERR_JSON_EMPTY);
   free(s->json);

   s->capacity = size;
   s->json = json;
   return true;
}

void nierr_Status_initialize(struct nierr_Status * status)
{
   status->code = 0;
   status->capacity = 0;
   status->reallocJson = &nierr_defaultReallocJson;
   status->json = nullptr;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/nierr_Status.h sha256=7188a0e1bb3d317709d43b35ce180735d33dcc166b6aed981869ac9f366ca3fc bytes=7511 -->
## FILE: imports/include/nierr_Status.h

- repository: `ni/grpc-device`
- source_path: `imports/include/nierr_Status.h`
- sha256: `7188a0e1bb3d317709d43b35ce180735d33dcc166b6aed981869ac9f366ca3fc`
- bytes: 7511

````c
/*!
   \file
   \brief Status C definition and helper functions.

   This file is a pared-down version of the one in the nierr component,
   with required elements defined in ni-build and additional dependencies removed.
*/
/*
   Copyright (c) 2012-2022 National Instruments Corporation.
   All rights reserved.
*/

#ifndef NIERR_NIERR_STATUS_H_
#define NIERR_NIERR_STATUS_H_

#include <stdint.h>

extern "C" {
#define kNICCall

#if kNICompilerMSVC
   #define  kNIInlineC     __inline       /*!< Defined to specify that
                                          the following C function should be inlined. */
   #define  kNIForceInline __forceinline  /*!< Defined to force inline. */
#else
   #define  kNIInlineC     static inline
   #define  kNIForceInline __attribute__((always_inline))
#endif

#define JSONZ_TERMINATOR_SIZE 2 /* '\0' + JSONZ_TERM_CHAR */

struct nierr_Status;

/*! This function type is responsible to allocate/free json buffer and put the
 * buffer size into the capacity field for a given nierr_Status.
 * \return true if successful, else false. If size is 0, success is guaranteed.
 * \param[in] s status
 * \param[in] size if size>0, then it indicates minimum size to allocate. It may allocate more than size.
 *       If size is 0, then json buffer will be freed and capacity set to 0
 * \post if size is not 0, json field will be fully initialized jsonz buffer.
 * \post if size is 0, json field will be freed, and capacity reset to 0
 * \post if failed, nothing will be changed
 */
typedef bool (kNICCall nierr_ReallocJson)(struct nierr_Status * s, uint32_t size);

/*! nierr_Status structure for C code that can be used for status chaining
 * across DLL boundary.
 * For coding implementation, please use nierr::Status instead, because its
 * interface to stuff information into json is easier.
 * \sa nierr::Status
 */
typedef struct nierr_Status
{
   int32_t code;        /*!< status code */
   uint32_t capacity;   /*!< capacity of the json buffer in bytes total */
   nierr_ReallocJson *reallocJson; /*!< function pointer to realloc json
                                     buffer. Please refer to nierr_ReallocJson
                                     function type for more details.
                                     \sa nierr_ReallocJson */
   char* json;          /*!< pointer to description buffer in jsonz
                          format. Please allocate and initialize this buffer
                          using nierr_Status_jsonReserve() or
                          nierr_Status_jsonSet(). It's automatically freed by
                          nierr_Status_reset().
                          \warning Do not write to this buffer directly without
                          using jsonz library.
                          */
} nierr_Status;

void nierr_Status_initialize(struct nierr_Status * status);

/*! the function to be used for nierr_Status::reallocJson field.
 *  This function is responsible to allocate/free json buffer and put the
 * buffer size into the capacity field for a given nierr_Status.
 * \return true if successful, else false. If size is 0, success is guaranteed.
 * \param[in] s status
 * \param[in] size if size>0, then it indicates minimum size to allocate. It may allocate more than size.
 *       If size is 0, then json buffer will be freed and capacity set to 0
 * \post if size is not 0, json field will be fully initialized jsonz buffer.
 * \post if size is 0, json field will be freed, and capacity reset to 0
 * \post if failed, nothing will be changed
 */
bool kNICCall nierr_defaultReallocJson(struct nierr_Status * s, uint32_t size);

/*! free the json string
 * \param[in,out] s status
 */
kNIInlineC void nierr_Status_jsonFree(struct nierr_Status *s)
   { s->reallocJson(s,0); }

/*! whether nierr_Status code is fatal
 * \param s status
 * \return true if fatal (code<0), false otherwise
 */
kNIInlineC bool nierr_Status_isFatal(const struct nierr_Status *s)
   { return (bool) /* thx msvc71 */ (s->code < 0); }

/*! whether nierr_Status code is not fatal
 * \param s status
 * \return true if not fatal (code>=0), false otherwise
 */
kNIInlineC bool nierr_Status_isNotFatal(const struct nierr_Status *s)
   { return !nierr_Status_isFatal(s); }

/*! whether nierr_Status code is warning
 * \param s status
 * \return true if warning (code>0), false otherwise
 */
kNIInlineC bool nierr_Status_isWarning(const struct nierr_Status *s)
   { return (bool) /* thx msvc71 */ (s->code > 0); }

/*! whether nierr_Status code is not warning
 * \param s status
 * \return true if not warning (code<=0), false otherwise
 */
kNIInlineC bool nierr_Status_isNotWarning(const struct nierr_Status *s)
   { return !nierr_Status_isWarning(s); }

/*! whether nierr_Status code is success (0)
 * \param s status
 * \return true if success (code==0), false otherwise
 */
kNIInlineC bool nierr_Status_isSuccess(const struct nierr_Status *s)
   { return (bool) /* thx msvc71 */ (s->code == 0); }

/* JSON Descriptor Support =============================================== */

/*! Empty nierr::Status json string. Defined as "{}" */
#define NIERR_JSON_EMPTY "{}"

/*! Status json key for file name where error originated. The value needs to
 * be a string */
#define NIERR_JSON_KEY_FILE "file"

/*! Status json key for line number where error originated. The value needs
 * to be an integer */
#define NIERR_JSON_KEY_LINE "line"

/*! Status json key for component name where error originated, usually taken
 * from kComponentName define from mxBS. The value needs to be a string */
#define NIERR_JSON_KEY_COMPONENT "component"

/*! Status json key for error constant. The value shall be a string */
#define NIERR_JSON_KEY_ERROR_CONSTANT "error_constant"

/*! Status json key for translator module responsible to translate the json
 * information into human readable string. The value needs to be a string. */
#define NIERR_JSON_KEY_TRANSLATOR "translator"

/*! Status json key for info for translator module */
#define NIERR_JSON_KEY_TRANSLATOR_INFO "translator_info"

/*! Status json key to capture std::exception::what(), if we happen to
 * translate std::exception to nierr::Exception. The value is a string */
#define NIERR_JSON_KEY_STD_EXCEPTION_WHAT "std_exception_what"

/*! Status json key for nested error object */
#define NIERR_JSON_KEY_NESTED_ERROR "nested_error"
/*! Status json key for nested error code */
#define NIERR_JSON_KEY_NESTED_ERROR_CODE "code"

/*! Status json key for internal error object */
#define NIERR_JSON_KEY_INTERNAL_ERROR "internal_error"
/*! Status json key for internal error code */
#define NIERR_JSON_KEY_INTERNAL_ERROR_CODE "code"
/*! Status json key for internal error string */
#define NIERR_JSON_KEY_INTERNAL_ERROR_STRING "string"
/*! Status json key for internal error API */
#define NIERR_JSON_KEY_INTERNAL_ERROR_API "api"

/*! Status json value for internal error API for win32 */
#define NIERR_JSON_VALUE_INTERNAL_ERROR_API_WIN32 "win32"
/*! Status json value for internal error API for HRESULT */
#define NIERR_JSON_VALUE_INTERNAL_ERROR_API_HRESULT "hresult"
/*! Status json value for internal error API for mach */
#define NIERR_JSON_VALUE_INTERNAL_ERROR_API_MACH "mach"
/*! Status json value for internal error API for errno */
#define NIERR_JSON_VALUE_INTERNAL_ERROR_API_ERRNO "errno"

}

#endif // NIERR_NIERR_STATUS_H_
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niFake.h sha256=ea76ac4f9e98585ad099368d31e2356e6a1db87269792e32e3c89e30c853ba8c bytes=20221 -->
## FILE: imports/include/niFake.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niFake.h`
- sha256: `ea76ac4f9e98585ad099368d31e2356e6a1db87269792e32e3c89e30c853ba8c`
- bytes: 20221

````c
/*
    **** THIS FILE IS GENERATED. ANY CHANGES WILL BE OVERWRITTEN! ****
    Command-line: e:/perforce/build/exports/ni/hapi/hapigen/official/export/23.0/23.0.0d26/tools/win32/i386/hapigen_render.exe --processed-metadata-path e:/dev/_r/18/src/hapigen/niFakeHeaders/objects/niFakeHeaders/win64U/x64/other/release/cheader_expanded_metadata.hapigen_processed --template-path e:/perforce/build/exports/ni/hapi/hapigen_cheader_plugin/official/export/23.0/23.0.0d26/templates/ivi_based_public_header.h.mako --output-path ./objects/codegen/niFakeHeaders/niFake.h --template-search-path e:/perforce/build/exports/ni/hapi/hapigen/official/export/23.0/23.0.0d26/templates --template-search-path e:/perforce/build/exports/ni/hapi/hapigen_cheader_plugin/official/export/23.0/23.0.0d26/templates
*/

#ifndef __NIFAKE_HEADER
#define __NIFAKE_HEADER

/******************************************************************************/
/*                               Include Files                                */
/******************************************************************************/

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <IviVisaType.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#ifdef _CVI_
#pragma EnableLibraryRuntimeChecking
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NIFAKE_MAJOR_VERSION                                   23                              // Instrument driver major version
#define NIFAKE_MINOR_VERSION                                   0                               // Instrument driver minor version
#define NIFAKE_UPDATE_VERSION                                  0                               // Instrument driver update version


#define NIFAKE_ATTR_BASE                                       1000000                         // 1000000 (0xf4240)
#define NIFAKE_ATTR_PRIVATE_BASE                               (NIFAKE_ATTR_BASE + 100L)       // 1000100 (0xf42a4)
#define NIFAKE_MAX_MESSAGE_BUF_SIZE                            256                             // 256 (0x100)
#define NIFAKE_FLAG0                                           (1L << 0)                       // 1 (0x1)
#define NIFAKE_FLAG1                                           (1L << 1)                       // 2 (0x2)
#define NIFAKE_FLAG2                                           (1L << 2)                       // 4 (0x4)
#define NIFAKE_FLAG3                                           (1L << 3)                       // 8 (0x8)
#define NIFAKE_FLAG4                                           (1L << 4)                       // 16 (0x10)
#define NIFAKE_FLAG5                                           (1L << 5)                       // 32 (0x20)
#define NIFAKE_FLAG6                                           (1L << 6)                       // 64 (0x40)
#define NIFAKE_FLAG7                                           (1L << 7)                       // 128 (0x80)
#define NIFAKE_FLAG8                                           (1L << 8)                       // 256 (0x100)
#define NIFAKE_FLAG_FLAG3                                      (1L << NIFAKE_FLAG3)            // 256 (0x100)
#define NIFAKE_FLAG_COMBO0                                     (NIFAKE_FLAG0 | NIFAKE_FLAG1)   // 3 (0x3)
#define NIFAKE_FLAG_COMBO1                                     (NIFAKE_FLAG1 | NIFAKE_FLAG4)   // 18 (0x12)
#define NIFAKE_FLOAT_DEFINE                                    42.0
#define NIFAKE_INT_DEFINE                                      42                              // 42 (0x2a)

// Values
// Alt Color
// Test comment
#define NIFAKE_VAL_RED                                         1                               // 1 (0x1)
#define NIFAKE_VAL_BLUE                                        (NIFAKE_VAL_RED + 1L)           // 2 (0x2)
#define NIFAKE_VAL_YELLOW                                      5                               // 5 (0x5)
#define NIFAKE_VAL_BLACK                                       42                              // 42 (0x2a)

// Beautiful Color
#define NIFAKE_VAL_PINK                                        44                              // 44 (0x2c)
#define NIFAKE_VAL_AQUA                                        43                              // 43 (0x2b)
#define NIFAKE_VAL_GREEN                                       45                              // 45 (0x2d)
// #define NIFAKE_VAL_BLACK                                    DEFINED ABOVE (42)              // 42 (0x2a)

// Test comment
// Values used in
//     NIFAKE_ATTR_READ_WRITE_COLOR
// #define NIFAKE_VAL_RED                                      DEFINED ABOVE (1)               // 1 (0x1)
// #define NIFAKE_VAL_BLUE                                     DEFINED ABOVE ((NIFAKE_VAL_RED + 1L)) // 2 (0x2)
// #define NIFAKE_VAL_YELLOW                                   DEFINED ABOVE (5)               // 5 (0x5)
// #define NIFAKE_VAL_BLACK                                    DEFINED ABOVE (42)              // 42 (0x2a)

// Test comment
// Values used in
//     NIFAKE_ATTR_READ_WRITE_ENUM_WITH_CONVERTER
// #define NIFAKE_VAL_RED                                      DEFINED ABOVE (1)               // 1 (0x1)
// #define NIFAKE_VAL_BLUE                                     DEFINED ABOVE ((NIFAKE_VAL_RED + 1L)) // 2 (0x2)
// #define NIFAKE_VAL_YELLOW                                   DEFINED ABOVE (5)               // 5 (0x5)
// #define NIFAKE_VAL_BLACK                                    DEFINED ABOVE (42)              // 42 (0x2a)

// Values used in
//     NIFAKE_ATTR_FLOAT_ENUM, niFake_ParametersAreMultipleTypes, niFake_ReturnMultipleTypes
#define NIFAKE_VAL_THREE_POINT_FIVE                            3.5
#define NIFAKE_VAL_FOUR_POINT_FIVE                             4.5
#define NIFAKE_VAL_FIVE_POINT_FIVE                             5.5
#define NIFAKE_VAL_SIX_POINT_FIVE                              6.5
#define NIFAKE_VAL_SEVEN_POINT_FIVE                            7.5

// Values used in
//     niFake_StringValuedEnumInputFunctionWithDefaults
#define NIFAKE_VAL_ANDROID                                     "Android"
#define NIFAKE_VAL_IOS                                         "iOS"
#define NIFAKE_VAL_NONE                                        "None"

// Values used in
//     niFake_EnumArrayOutputFunction, niFake_EnumInputFunctionWithDefaults, niFake_GetEnumValue,
//     niFake_ParametersAreMultipleTypes, niFake_ReturnMultipleTypes
#define NIFAKE_VAL_LEONARDO                                    0                               // 0 (0x0)
#define NIFAKE_VAL_DONATELLO                                   1                               // 1 (0x1)
#define NIFAKE_VAL_RAPHAEL                                     2                               // 2 (0x2)
#define NIFAKE_VAL_MICHELANGELO                                3                               // 3 (0x3)

// Attributes
#define NIFAKE_ATTR_READ_WRITE_BOOL                            (NIFAKE_ATTR_BASE + 0L)         // 1000000 (0xf4240), ViBoolean
#define NIFAKE_ATTR_READ_WRITE_DOUBLE                          (NIFAKE_ATTR_BASE + 1L)         // 1000001 (0xf4241), ViReal64
#define NIFAKE_ATTR_READ_WRITE_STRING                          (NIFAKE_ATTR_BASE + 2L)         // 1000002 (0xf4242), ViString
#define NIFAKE_ATTR_READ_WRITE_COLOR                           (NIFAKE_ATTR_BASE + 3L)         // 1000003 (0xf4243), ViInt32
#define NIFAKE_ATTR_READ_WRITE_INTEGER                         (NIFAKE_ATTR_BASE + 4L)         // 1000004 (0xf4244), ViInt32
// Test comment
#define NIFAKE_ATTR_FLOAT_ENUM                                 (NIFAKE_ATTR_BASE + 5L)         // 1000005 (0xf4245), ViReal64
#define NIFAKE_ATTR_READ_WRITE_INT64                           (NIFAKE_ATTR_BASE + 6L)         // 1000006 (0xf4246), ViInt64
#define NIFAKE_ATTR_READ_WRITE_DOUBLE_WITH_CONVERTER           (NIFAKE_ATTR_BASE + 7L)         // 1000007 (0xf4247), ViReal64
#define NIFAKE_ATTR_READ_WRITE_INTEGER_WITH_CONVERTER          (NIFAKE_ATTR_BASE + 8L)         // 1000008 (0xf4248), ViInt32
#define NIFAKE_ATTR_READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY (NIFAKE_ATTR_BASE + 9L)         // 1000009 (0xf4249), ViReal64,   multi-channel
#define NIFAKE_ATTR_READ_WRITE_STRING_REPEATED_CAPABILITY      (NIFAKE_ATTR_BASE + 10L)        // 1000010 (0xf424a), ViString
#define NIFAKE_ATTR_READ_WRITE_ENUM_WITH_CONVERTER             (NIFAKE_ATTR_BASE + 11L)        // 1000011 (0xf424b), ViInt32

#pragma pack(push,8)
// Test comment
#if !defined(_NIStruct)
#define _NIStruct
struct CustomStruct
{
    ViInt32 structInt;
    ViReal64 structDouble;
};
#endif // !defined(_NIStruct)

// Test comment
#if !defined(_NIStructTypedef)
#define _NIStructTypedef
typedef struct CustomStructTypedef_struct
{
    ViInt32 structInt;
    ViReal64 structDouble;
} CustomStructTypedef;
#endif // !defined(_NIStructTypedef)

// Test comment
#if !defined(_NIStructNestedTypedef)
#define _NIStructNestedTypedef
typedef struct CustomStructNestedTypedef_struct
{
    struct CustomStruct structCustomStruct;
    CustomStructTypedef structCustomStructTypedef;
} CustomStructNestedTypedef;
#endif // !defined(_NIStructNestedTypedef)

#pragma pack(pop)

// Functions
ViStatus _VI_FUNC niFake_Abort(
   ViSession vi);

ViStatus _VI_FUNC niFake_BoolArrayOutputFunction(
   ViSession vi,
   ViInt32 numberOfElements,
   ViBoolean anArray[]);

ViStatus _VI_FUNC niFake_ClearError(
   ViSession vi);

ViStatus _VI_FUNC niFake_close(
   ViSession vi);

ViStatus _VI_FUNC niFake_EnumArrayOutputFunction(
   ViSession vi,
   ViInt32 numberOfElements,
   ViInt16 anArray[]);

ViStatus _VI_FUNC niFake_EnumInputFunctionWithDefaults(
   ViSession vi,
   ViInt16 aTurtle);

ViStatus _VI_FUNC niFake_StringValuedEnumInputFunctionWithDefaults(
   ViSession vi,
   ViConstString aMobileOSName);

ViStatus _VI_FUNC niFake_error_message(
   ViSession vi,
   ViStatus errorCode,
   ViChar errorMessage[NIFAKE_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niFake_FetchWaveform(
   ViSession vi,
   ViInt32 numberOfSamples,
   ViReal64 waveformData[],
   ViInt32* actualNumberOfSamples);

ViStatus _VI_FUNC niFake_GetABoolean(
   ViSession vi,
   ViBoolean* aBoolean);

ViStatus _VI_FUNC niFake_GetANumber(
   ViSession vi,
   ViInt16* aNumber);

ViStatus _VI_FUNC niFake_GetAStringOfFixedMaximumSize(
   ViSession vi,
   ViChar aString[NIFAKE_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niFake_GetAStringUsingPythonCode(
   ViSession vi,
   ViInt16 aNumber,
   ViChar aString[]);

// Test comment
ViStatus _VI_FUNC niFake_GetAnIviDanceString(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar aString[]);

ViStatus _VI_FUNC niFake_GetArrayForPythonCodeDouble(
   ViSession vi,
   ViInt32 numberOfElements[],
   ViReal64 arrayOut[]);

ViStatus _VI_FUNC niFake_GetArraySizeForPythonCode(
   ViSession vi,
   ViInt32* sizeOut);

ViStatus _VI_FUNC niFake_GetArrayUsingIviDance(
   ViSession vi,
   ViInt32 arraySize,
   ViReal64 arrayOut[]);

ViStatus _VI_FUNC niFake_GetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViBoolean* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt64* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 bufferSize,
   ViChar attributeValue[]);

ViStatus _VI_FUNC niFake_GetCalDateAndTime(
   ViSession vi,
   ViInt32 calType,
   ViInt32* month,
   ViInt32* day,
   ViInt32* year,
   ViInt32* hour,
   ViInt32* minute);

ViStatus _VI_FUNC niFake_GetCalInterval(
   ViSession vi,
   ViInt32* months);

ViStatus _VI_FUNC niFake_GetEnumValue(
   ViSession vi,
   ViInt32* aQuantity,
   ViInt16* aTurtle);

ViStatus _VI_FUNC niFake_GetError(
   ViSession vi,
   ViStatus* errorCode,
   ViInt32 bufferSize,
   ViChar description[]);

ViStatus _VI_FUNC niFake_GetErrorMessage(
   ViSession vi,
   ViStatus errorCode,
   ViInt32 bufferSize,
   ViChar errorMessage[]);

ViStatus _VI_FUNC niFake_InitWithOptions(
   ViString resourceName,
   ViBoolean idQuery,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession* vi);

ViStatus _VI_FUNC niFake_Initiate(
   ViSession vi);

ViStatus _VI_FUNC niFake_LockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

ViStatus _VI_FUNC niFake_UnlockSession(
   ViSession vi,
   ViBoolean* callerHasLock);

ViStatus _VI_FUNC niFake_MultipleArrayTypes(
   ViSession vi,
   ViInt32 outputArraySize,
   ViReal64 outputArray[],
   ViReal64 outputArrayOfFixedLength[3],
   ViInt32 inputArraySizes,
   ViReal64 inputArrayOfFloats[],
   ViInt16 inputArrayOfIntegers[]);

ViStatus _VI_FUNC niFake_MultipleArraysSameSize(
   ViSession vi,
   ViReal64 values1[],
   ViReal64 values2[],
   ViReal64 values3[],
   ViReal64 values4[],
   ViInt32 size);

ViStatus _VI_FUNC niFake_OneInputFunction(
   ViSession vi,
   ViInt32 aNumber);

ViStatus _VI_FUNC niFake_ParametersAreMultipleTypes(
   ViSession vi,
   ViBoolean aBoolean,
   ViInt32 anInt32,
   ViInt64 anInt64,
   ViInt16 anIntEnum,
   ViReal64 aFloat,
   ViReal64 aFloatEnum,
   ViInt32 stringSize,
   ViConstString aString[]);

ViStatus _VI_FUNC niFake_PoorlyNamedSimpleFunction(
   ViSession vi);

ViStatus _VI_FUNC niFake_Read(
   ViSession vi,
   ViReal64 maximumTime,
   ViReal64* reading);

ViStatus _VI_FUNC niFake_ReadFromChannel(
   ViSession vi,
   ViConstString channelName,
   ViInt32 maximumTime,
   ViReal64* reading);

ViStatus _VI_FUNC niFake_ReturnANumberAndAString(
   ViSession vi,
   ViInt16* aNumber,
   ViChar aString[NIFAKE_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niFake_ReturnMultipleTypes(
   ViSession vi,
   ViBoolean* aBoolean,
   ViInt32* anInt32,
   ViInt64* anInt64,
   ViInt16* anIntEnum,
   ViReal64* aFloat,
   ViReal64* aFloatEnum,
   ViInt32 arraySize,
   ViReal64 anArray[],
   ViInt32 stringSize,
   ViChar aString[]);

ViStatus _VI_FUNC niFake_self_test(
   ViSession vi,
   ViInt16* selfTestResult,
   ViChar selfTestMessage[NIFAKE_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niFake_SetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViBoolean attributeValue);

ViStatus _VI_FUNC niFake_SetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 attributeValue);

ViStatus _VI_FUNC niFake_SetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt64 attributeValue);

ViStatus _VI_FUNC niFake_SetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64 attributeValue);

ViStatus _VI_FUNC niFake_SetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession attributeValue);

ViStatus _VI_FUNC niFake_SetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViConstString attributeValue);

ViStatus _VI_FUNC niFake_TwoInputFunction(
   ViSession vi,
   ViReal64 aNumber,
   ViString aString);

ViStatus _VI_FUNC niFake_Use64BitNumber(
   ViSession vi,
   ViInt64 input,
   ViInt64* output);

ViStatus _VI_FUNC niFake_WriteWaveform(
   ViSession vi,
   ViInt32 numberOfSamples,
   ViReal64 waveform[]);

ViStatus _VI_FUNC niFake_SetCustomType(
   ViSession vi,
   struct CustomStruct* cs);

ViStatus _VI_FUNC niFake_SetCustomTypeArray(
   ViSession vi,
   ViInt32 numberOfElements,
   struct CustomStruct cs[]);

ViStatus _VI_FUNC niFake_GetCustomType(
   ViSession vi,
   struct CustomStruct* cs);

ViStatus _VI_FUNC niFake_GetCustomTypeArray(
   ViSession vi,
   ViInt32 numberOfElements,
   struct CustomStruct cs[]);

ViStatus _VI_FUNC niFake_GetArrayForPythonCodeCustomType(
   ViSession vi,
   ViInt32 numberOfElements[],
   struct CustomStruct arrayOut[]);

ViStatus _VI_FUNC niFake_ResetAttribute(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViInt32* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViReal64* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViInt32 bufferSize,
   ViChar attributeValue[]);

ViStatus _VI_FUNC niFake_OneOutputFunction(
   ViSession vi,
   ViInt16* aNumber);

ViStatus _VI_FUNC niFake_GetAnIviDanceWithATwistString(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar aString[],
   ViInt32* actualSize);

ViStatus _VI_FUNC niFake_InitializeWithChannels(
   ViRsrc resourceName,
   ViConstString channels,
   ViBoolean reset,
   ViConstString optionString,
   ViSession* newVi);

ViStatus _VI_FUNC niFake_GetChannelName(
   ViSession vi,
   ViInt32 index,
   ViInt32 nameSize,
   ViChar name[]);

ViStatus _VI_FUNC niFake_GetChannelNames(
   ViSession vi,
   ViConstString indices,
   ViInt32 nameSize,
   ViChar names[]);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViInt64* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViSession* attributeValue);

ViStatus _VI_FUNC niFake_GetAttributeWithOptionsViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 retrievalMode,
   ViBoolean* attributeValue);

ViStatus _VI_FUNC niFake_AttributeWasSetByUser(
   ViSession vi,
   ViConstString repCapName,
   ViAttr attributeId,
   ViBoolean* wasSetByUser);

ViStatus _VI_FUNC niFake_DisableParentSessionAutoClose(
   ViSession vi);

ViStatus _VI_FUNC niFake_DoubleAllTheNums(
   ViSession vi,
   ViInt32 numberCount,
   ViReal64 numbers[]);

ViStatus _VI_FUNC niFake_GetCustomTypeTypedef(
   ViSession vi,
   CustomStructTypedef* cst,
   CustomStructNestedTypedef* csnt);

ViStatus _VI_FUNC niFake_AcceptListOfDurationsInSeconds(
   ViSession vi,
   ViInt32 count,
   ViReal64 delays[]);

ViStatus _VI_FUNC niFake_ReturnDurationInSeconds(
   ViSession vi,
   ViReal64* timedelta);

ViStatus _VI_FUNC niFake_ReturnListOfDurationsInSeconds(
   ViSession vi,
   ViInt32 numberOfElements,
   ViReal64 timedeltas[]);

ViStatus _VI_FUNC niFake_FunctionWithRepeatedCapabilityType(
   ViSession vi,
   ViConstString siteList);

// Test comment
ViStatus _VI_FUNC niDifferentPrefix_GetAnIviDanceWithCFunctionPrefixString(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar aString[]);

ViStatus _VI_FUNC niFake_ImportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 sizeInBytes,
   ViInt8 configuration[]);

ViStatus _VI_FUNC niFake_ExportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 sizeInBytes,
   ViInt8 configuration[]);


// Errors and Warnings

#include "niFakeObsolete.h"

#endif /* __NIFAKE_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niFakeNonIvi.h sha256=b2e1e3051879de008b13db7c73206f5157b53975015b3f6f9de1193ab7f0804d bytes=575 -->
## FILE: imports/include/niFakeNonIvi.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niFakeNonIvi.h`
- sha256: `b2e1e3051879de008b13db7c73206f5157b53975015b3f6f9de1193ab7f0804d`
- bytes: 575

````c
#ifndef NIFAKE_NON_IVI_H
#define NIFAKE_NON_IVI_H
#include <cstdint>
// For CVIAbsoluteTime
#include "NIDAQmx.h"

const int32 kDriverSuccess = 0;
const int32 kDriverFailure = 1;

using FakeCrossDriverHandle = int32;
using FakeHandle = uint64_t;
using SecondarySessionHandle = int32;
using myInt16 = int16_t;
using myUInt16 = uint16_t;
using myInt8 = int8_t;
using myUInt8 = uint8_t;

struct StructWithCoercion_struct {
  myInt16 first;
  myUInt16 second;
  myInt8 third;
};

using CallbackPtr = int32(myInt16, void*);

#endif /* NIFAKE_NON_IVI_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niFakeObsolete.h sha256=6ac7a798b26a2e3e0a8bfe5649f0988daaeb6df6b12a76cb6fbf3ad3e2b9b4e5 bytes=103 -->
## FILE: imports/include/niFakeObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niFakeObsolete.h`
- sha256: `6ac7a798b26a2e3e0a8bfe5649f0988daaeb6df6b12a76cb6fbf3ad3e2b9b4e5`
- bytes: 103

````c
// This file is only for test
#ifndef __NIFAKEOBSOLETE_HEADER
#define __NIFAKEOBSOLETE_HEADER
#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niFgen.h sha256=815f379e272c836541ba98863b61972d0e00ae00599f94fed66bde11b9055f91 bytes=76901 -->
## FILE: imports/include/niFgen.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niFgen.h`
- sha256: `815f379e272c836541ba98863b61972d0e00ae00599f94fed66bde11b9055f91`
- bytes: 76901

````c
/****************************************************************************
 *    NI-FGEN Instrument Driver for National Instruments Signal Generators
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 1998-2017.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niFgen.h
 * Purpose:  NI-FGEN Instrument Driver for National Instruments Signal Generators
 *           declarations.
 *
 ****************************************************************************/

#ifndef __NIFGEN_HEADER
#define __NIFGEN_HEADER

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include "IviFgen.h"
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NIFGEN_MAJOR_VERSION       17    /* Instrument driver major version */
#define NIFGEN_MINOR_VERSION       800   /* Instrument driver minor version */

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/

/*--------------- Output Attributes ----------------------------------------*/

#define NIFGEN_ATTR_OUTPUT_MODE                              IVIFGEN_ATTR_OUTPUT_MODE              /* ViInt32   */
#define NIFGEN_ATTR_OUTPUT_ENABLED                           IVIFGEN_ATTR_OUTPUT_ENABLED           /* ViBoolean, multi-channel */
#define NIFGEN_ATTR_DIGITAL_GAIN                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 254L) /* ViReal64  */
#define NIFGEN_ATTR_ANALOG_PATH                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 222L) /* ViInt32   */
#define NIFGEN_ATTR_LOAD_IMPEDANCE                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 220L) /* ViReal64  */
#define NIFGEN_ATTR_OUTPUT_IMPEDANCE                         IVIFGEN_ATTR_OUTPUT_IMPEDANCE         /* ViReal64,  multi-channel, ohms */
#define NIFGEN_ATTR_TERMINAL_CONFIGURATION                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 365L) /* ViInt32   */
#define NIFGEN_ATTR_COMMON_MODE_OFFSET                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 366L) /* ViReal64  */
#define NIFGEN_ATTR_CHANNEL_DELAY                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 369L) /* ViReal64  */
#define NIFGEN_ATTR_ABSOLUTE_DELAY                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 413L) /* ViReal64 */

/*- Filter -----------------------------------------------------------------*/
#define NIFGEN_ATTR_ANALOG_FILTER_ENABLED                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 103L) /* ViBoolean */
#define NIFGEN_ATTR_DIGITAL_FILTER_ENABLED                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 102L) /* ViBoolean */
#define NIFGEN_ATTR_DIGITAL_FILTER_INTERPOLATION_FACTOR     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 218L) /* ViReal64  */
#define NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 323L) /* ViBoolean */

/*- Data Mask --------------------------------------------------------------*/
#define NIFGEN_ATTR_ANALOG_DATA_MASK                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 234L) /* ViInt32 */
#define NIFGEN_ATTR_ANALOG_STATIC_VALUE                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 235L) /* ViInt32 */
#define NIFGEN_ATTR_DIGITAL_DATA_MASK                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 236L) /* ViInt32 */
#define NIFGEN_ATTR_DIGITAL_STATIC_VALUE                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 237L) /* ViInt32 */

/*- Advanced Output Attributes ---------------------------------------------*/
#define NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 101L) /* ViBoolean */
#define NIFGEN_ATTR_AUX_POWER_ENABLED                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 411L) /* ViBoolean */
#define NIFGEN_ATTR_IDLE_BEHAVIOR                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 377L) /* ViInt32 */
#define NIFGEN_ATTR_IDLE_VALUE                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 378L) /* ViInt32 */
#define NIFGEN_ATTR_WAIT_BEHAVIOR                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 379L) /* ViInt32 */
#define NIFGEN_ATTR_WAIT_VALUE                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 380L) /* ViInt32 */


/*----------------------------- Arbitrary Waveform -------------------------*/

#define NIFGEN_ATTR_ARB_GAIN                                 IVIFGEN_ATTR_ARB_GAIN                 /* ViReal64, multi-channel        */
#define NIFGEN_ATTR_ARB_OFFSET                               IVIFGEN_ATTR_ARB_OFFSET               /* ViReal64, multi-channel, volts */
#define NIFGEN_ATTR_WAVEFORM_QUANTUM                         IVIFGEN_ATTR_WAVEFORM_QUANTUM         /* ViInt32,  read-only, samples   */
#define NIFGEN_ATTR_MAX_NUM_WAVEFORMS                        IVIFGEN_ATTR_MAX_NUM_WAVEFORMS        /* ViInt32,  read-only            */
#define NIFGEN_ATTR_MIN_WAVEFORM_SIZE                        IVIFGEN_ATTR_MIN_WAVEFORM_SIZE        /* ViInt32,  read-only, samples   */
#define NIFGEN_ATTR_MAX_WAVEFORM_SIZE                        IVIFGEN_ATTR_MAX_WAVEFORM_SIZE        /* ViInt32,  read-only, samples   */

/*- Arbitrary Waveform Generation ------------------------------------------*/
#define NIFGEN_ATTR_ARB_WAVEFORM_HANDLE                      IVIFGEN_ATTR_ARB_WAVEFORM_HANDLE  /* ViInt32,  multi-channel        */
#define NIFGEN_ATTR_ARB_MARKER_POSITION                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 327L) /* ViInt32,  readwrite, samples   */
#define NIFGEN_ATTR_ARB_REPEAT_COUNT                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 328L) /* ViInt32,  readwrite            */

/*- Arbitrary Sequence Generation ------------------------------------------*/
#define NIFGEN_ATTR_ARB_SEQUENCE_HANDLE                      IVIFGEN_ATTR_ARB_SEQUENCE_HANDLE /* ViInt32,  multi-channel        */
#define NIFGEN_ATTR_MAX_NUM_SEQUENCES                        IVIFGEN_ATTR_MAX_NUM_SEQUENCES   /* ViInt32,  read-only            */
#define NIFGEN_ATTR_MIN_SEQUENCE_LENGTH                      IVIFGEN_ATTR_MIN_SEQUENCE_LENGTH /* ViInt32,  read-only            */
#define NIFGEN_ATTR_MAX_SEQUENCE_LENGTH                      IVIFGEN_ATTR_MAX_SEQUENCE_LENGTH /* ViInt32,  read-only            */
#define NIFGEN_ATTR_MAX_LOOP_COUNT                           IVIFGEN_ATTR_MAX_LOOP_COUNT      /* ViInt32,  read-only            */

/*- Script Generation ------------------------------------------------------*/
#define NIFGEN_ATTR_SCRIPT_TO_GENERATE                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 270L)  /* ViString */

/*- Data Transfer ----------------------------------------------------------*/
#define NIFGEN_ATTR_FILE_TRANSFER_BLOCK_SIZE                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 240L)  /* ViInt32, samples */
#define NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 241L)  /* ViInt32, samples */
#define NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 373L)  /* ViReal64 */
/*- Direct DMA -------------------------------------------------------------*/
#define NIFGEN_ATTR_DIRECT_DMA_ENABLED                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 244L)  /* ViBoolean */
#define NIFGEN_ATTR_DIRECT_DMA_WINDOW_SIZE                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 245L)  /* ViInt32, bytes */
#define NIFGEN_ATTR_DIRECT_DMA_WINDOW_ADDRESS               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 274L)  /* ViInt32 */
/*- Streaming --------------------------------------------------------------*/
#define NIFGEN_ATTR_STREAMING_WAVEFORM_NAME                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 326L)  /* ViString */
#define NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 324L)  /* ViInt32  */
#define NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 325L)  /* ViInt32  */
#define NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 409L)  /* ViReal64 */
/*- Advanced Data Transfer -------------------------------------------------*/
#define NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 374L)  /* ViInt32  */
#define NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 375L)  /* ViInt32  */
#define NIFGEN_ATTR_PCI_DMA_OPTIMIZATIONS_ENABLED           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 362L)  /* ViBoolean */

/*- Onboard Signal Processing-------------------------------------------*/
#define NIFGEN_ATTR_OSP_ENABLED                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 246L) /* ViBoolean */
#define NIFGEN_ATTR_OSP_IQ_RATE                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 248L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 247L) /* ViInt32   */
#define NIFGEN_ATTR_OSP_MODE                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 370L) /* ViInt32   */
#define NIFGEN_ATTR_OSP_FREQUENCY_SHIFT                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 371L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_CARRIER_ENABLED                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 249L) /* ViBoolean */
#define NIFGEN_ATTR_OSP_CARRIER_FREQUENCY                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 250L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_CARRIER_PHASE_I                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 251L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_CARRIER_PHASE_Q                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 252L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 389L) /* ViBoolean  */
#define NIFGEN_ATTR_OSP_FIR_FILTER_TYPE                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 253L) /* ViInt32   */
#define NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 255L) /* ViBoolean */
#define NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 256L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 257L) /* ViBoolean */
#define NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 258L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 259L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 260L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 261L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 262L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_CIC_FILTER_GAIN                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 263L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 264L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 265L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 266L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 267L) /* ViReal64  */
#define NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 268L) /* ViInt32   */
#define NIFGEN_ATTR_OSP_OVERFLOW_STATUS                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 269L) /* ViInt32   */

/*- Peer-to-Peer (P2P)-------------------------------------------*/
#define NIFGEN_ATTR_P2P_ENABLED                                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 391L) /* ViBoolean  */
#define NIFGEN_ATTR_P2P_DESTINATION_CHANNELS                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 392L) /* ViString */
#define NIFGEN_ATTR_P2P_ENDPOINT_SIZE                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 393L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 394L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 395L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_ENDPOINT_COUNT                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 396L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 400L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 408L) /* ViInt32 */


/*- Peer-to-Peer (P2P) ADVANCED -------------------------------------------*/
#define NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 397L) /* ViBoolean */

/*- Peer-to-Peer (P2P) ADVANCED CONFIGURATION-------------------------------------------*/
#define NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 398L) /* ViInt64 */
#define NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 399L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 401L) /* ViInt64 */
#define NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 402L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_SIZE                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 403L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 410L) /* ViInt32 */

/*- Peer-to-Peer (P2P) ADVANCED STATUS NOTIFICATION-------------------------------------------*/
#define NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 405L) /* ViInt64 */
#define NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS_TYPE         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 406L) /* ViInt32 */
#define NIFGEN_ATTR_P2P_DONE_NOTIFICATION_VALUE                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 407L) /* ViInt32 */


/*---------------------------- Standard Function --------------------------*/

#define NIFGEN_ATTR_FUNC_WAVEFORM                            IVIFGEN_ATTR_FUNC_WAVEFORM            /* ViInt32,  multi-channel        */
#define NIFGEN_ATTR_FUNC_AMPLITUDE                           IVIFGEN_ATTR_FUNC_AMPLITUDE           /* ViReal64, multi-channel, volts */
#define NIFGEN_ATTR_FUNC_DC_OFFSET                           IVIFGEN_ATTR_FUNC_DC_OFFSET           /* ViReal64, multi-channel, volts */
#define NIFGEN_ATTR_FUNC_START_PHASE                         IVIFGEN_ATTR_FUNC_START_PHASE         /* ViReal64, multi-channel, deg   */
#define NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH                     IVIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH     /* ViReal64, multi-channel, pct   */
#define NIFGEN_ATTR_SYNC_DUTY_CYCLE_HIGH                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 105L) /* ViReal64 */
#define NIFGEN_ATTR_SYNC_OUT_OUTPUT_TERMINAL                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 330L) /* ViString */

/*- Standard Waveform Generation -------------------------------------------*/
#define NIFGEN_ATTR_FUNC_FREQUENCY                           IVIFGEN_ATTR_FUNC_FREQUENCY           /* ViReal64, multi-channel, hertz */
#define NIFGEN_ATTR_FUNC_BUFFER_SIZE                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 238L) /* ViInt32,  read-only, samples   */
#define NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 239L) /* ViInt32,  multi-channel        */

/*- Frequency List Generation ------------------------------------------*/
#define NIFGEN_ATTR_FREQ_LIST_HANDLE                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 208L) /* ViInt32,  multi-channel */
#define NIFGEN_ATTR_MAX_NUM_FREQ_LISTS                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 209L) /* ViInt32,  read-only     */
#define NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 210L) /* ViInt32,  read-only     */
#define NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH                    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 211L) /* ViInt32,  read-only     */
#define NIFGEN_ATTR_MIN_FREQ_LIST_DURATION                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 212L) /* ViReal64, read-only     */
#define NIFGEN_ATTR_MAX_FREQ_LIST_DURATION                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 213L) /* ViReal64, read-only     */
#define NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 214L) /* ViReal64, read-only     */


/*-------------------------------- Clocks ----------------------------------*/

/*- Reference Clock --------------------------------------------------------*/
#define NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 113L) /* ViString */
#define NIFGEN_ATTR_REF_CLOCK_FREQUENCY                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 107L) /* ViReal64 */
#define NIFGEN_ATTR_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 321L) /* ViString */
#define NIFGEN_ATTR_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 322L) /* ViString */

/*- Sample Clock -----------------------------------------------------------*/
#define NIFGEN_ATTR_ARB_SAMPLE_RATE                                 IVIFGEN_ATTR_ARB_SAMPLE_RATE          /* ViReal64, samples-per-second */
#define NIFGEN_ATTR_CLOCK_MODE                                       (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 110L) /* ViInt32 */
#define NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 112L) /* ViString */
#define NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 320L) /* ViString */
#define NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 219L) /* ViInt32  */

/*- Sample Clock Timebase --------------------------------------------------*/
#define NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 367L) /* ViString */
#define NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 368L) /* ViReal64 */
#define NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 329L) /* ViString */
#define NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 230L) /* ViInt32  */

/*- Advanced Clock Attributes ----------------------------------------------*/
#define NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 376L)   /* ViReal64 */
#define NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 231L)   /* ViReal64 */
#define NIFGEN_ATTR_OSCILLATOR_PHASE_DAC_VALUE                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 232L) /* ViInt32  */
#define NIFGEN_ATTR_EXTERNAL_CLOCK_DELAY_BINARY_VALUE          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 233L) /* ViInt32  */


/*--------------------------  Events  --------------------------------------*/

/*- Marker Event -------------------------------------------------------*/
#define NIFGEN_ATTR_MARKER_EVENT_OUTPUT_TERMINAL               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 312L)   /* ViString  */
#define NIFGEN_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 342L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_PULSE_POLARITY                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 313L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 340L)   /* ViReal64  */
#define NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 341L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 343L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_DELAY                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 354L)   /* ViReal64  */
#define NIFGEN_ATTR_MARKER_EVENT_DELAY_UNITS                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 355L)   /* ViInt32   */
#define NIFGEN_ATTR_ALL_MARKER_EVENTS_LIVE_STATUS              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 344L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_LIVE_STATUS                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 345L)   /* ViBoolean */
#define NIFGEN_ATTR_ALL_MARKER_EVENTS_LATCHED_STATUS           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 349L)   /* ViInt32   */
#define NIFGEN_ATTR_MARKER_EVENT_LATCHED_STATUS                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 350L)   /* ViBoolean */

/*- Data Marker Event --------------------------------------------------*/
#define NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 337L)   /* ViInt32  */
#define NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 338L)   /* ViInt32  */
#define NIFGEN_ATTR_DATA_MARKER_EVENT_OUTPUT_TERMINAL          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 339L)   /* ViString */

/*- Ready For Start Event ----------------------------------------------*/
#define NIFGEN_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 310L)   /* ViString  */
#define NIFGEN_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 311L)   /* ViInt32   */
#define NIFGEN_ATTR_READY_FOR_START_EVENT_LIVE_STATUS          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 348L)   /* ViBoolean */

/*- Started Event ------------------------------------------------------*/
#define NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 314L) /* ViString */
#define NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 331L) /* ViInt32  */
#define NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 316L) /* ViInt32  */
#define NIFGEN_ATTR_STARTED_EVENT_PULSE_POLARITY               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 318L) /* ViInt32  */
#define NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH_UNITS            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 333L) /* ViInt32  */
#define NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 335L) /* ViReal64 */
#define NIFGEN_ATTR_STARTED_EVENT_DELAY                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 356L) /* ViReal64 */
#define NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 357L) /* ViInt32  */
#define NIFGEN_ATTR_STARTED_EVENT_LATCHED_STATUS               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 352L) /* ViBoolean */

/*- Done Event ---------------------------------------------------------*/
#define NIFGEN_ATTR_DONE_EVENT_OUTPUT_TERMINAL                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 315L) /* ViString */
#define NIFGEN_ATTR_DONE_EVENT_OUTPUT_BEHAVIOR                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 332L) /* ViInt32  */
#define NIFGEN_ATTR_DONE_EVENT_LEVEL_ACTIVE_LEVEL              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 317L) /* ViInt32  */
#define NIFGEN_ATTR_DONE_EVENT_PULSE_POLARITY                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 319L) /* ViInt32  */
#define NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH_UNITS               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 334L) /* ViInt32  */
#define NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 336L) /* ViReal64 */
#define NIFGEN_ATTR_DONE_EVENT_DELAY                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 358L) /* ViReal64 */
#define NIFGEN_ATTR_DONE_EVENT_DELAY_UNITS                     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 359L) /* ViInt32  */
#define NIFGEN_ATTR_DONE_EVENT_LATCHED_STATUS                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 351L) /* ViBoolean */


/*----------------------- Triggers -------------------------------------*/

#define NIFGEN_ATTR_TRIGGER_MODE                               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 108L) /* ViInt32 */
#define NIFGEN_ATTR_BURST_COUNT                                 IVIFGEN_ATTR_BURST_COUNT              /* ViInt32, multi-channel */

/*- Start Trigger ------------------------------------------------------*/
#define NIFGEN_ATTR_START_TRIGGER_TYPE                         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 280L) /* ViInt32  */
#define NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 281L) /* ViString */
#define NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 282L) /* ViInt32  */
#define NIFGEN_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 283L) /* ViString */

/*- Script Trigger -----------------------------------------------------*/
#define NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 290L) /* ViInt32  */
#define NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE         (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 291L) /* ViString */
#define NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 292L) /* ViInt32  */
#define NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 293L) /* ViString */
#define NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 294L) /* ViInt32  */
#define NIFGEN_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 295L) /* ViString */

/*------------------ Instrument Specific Attributes --------------------*/

#define NIFGEN_ATTR_BUS_TYPE                                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 215L) /* ViInt32,  read-only */
#define NIFGEN_ATTR_MEMORY_SIZE                                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 242L) /* ViInt32,  read-only, bytes */
#define NIFGEN_ATTR_SERIAL_NUMBER                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 243L) /* ViString, read-only */
#define NIFGEN_ATTR_MARKER_EVENTS_COUNT                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 271L) /* ViInt32,  Read-only */
#define NIFGEN_ATTR_DATA_MARKER_EVENTS_COUNT                   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 273L) /* ViInt32,  Read-only */
#define NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT                      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 272L) /* ViInt32,  Read-only */
#define NIFGEN_ATTR_VIDEO_WAVEFORM_TYPE                        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 216L) /* ViInt32             */
#define NIFGEN_ATTR_FPGA_BITFILE_PATH                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 412L) /* ViString, read-only */

/*- 5401/5411/5431 Attributes -------------------------------------------*/
#define NIFGEN_ATTR_FILTER_CORRECTION_FREQUENCY                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 104L) /* ViReal64                */
#define NIFGEN_ATTR_TRIGGER_SOURCE                              IVIFGEN_ATTR_TRIGGER_SOURCE           /* ViInt32, multi-channel */
#define NIFGEN_ATTR_SYNCHRONIZATION                            (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 111L) /* ViInt32,  multi-channel */
#define NIFGEN_ATTR_ID_QUERY_RESPONSE                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1L)   /* ViString, read-only     */

/*-------------------- Calibration --------------------------------------*/
#define NIFGEN_ATTR_GAIN_DAC_VALUE                             (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 223L) /* ViInt32  */
#define NIFGEN_ATTR_OFFSET_DAC_VALUE                           (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 224L) /* ViInt32  */
#define NIFGEN_ATTR_OSCILLATOR_FREQ_DAC_VALUE                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 225L) /* ViInt32  */
#define NIFGEN_ATTR_CAL_ADC_INPUT                              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 227L) /* ViInt32  */
#define NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION                  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 228L) /* ViReal64 */
#define NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 229L) /* ViReal64 */

/*-------------- IVI Inherent Attributes -----------------------------------*/
/*- User Options */
#define NIFGEN_ATTR_CACHE                                     IVI_ATTR_CACHE                   /* ViBoolean */
#define NIFGEN_ATTR_RANGE_CHECK                               IVI_ATTR_RANGE_CHECK             /* ViBoolean */
#define NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS                   IVI_ATTR_QUERY_INSTRUMENT_STATUS /* ViBoolean */
#define NIFGEN_ATTR_RECORD_COERCIONS                          IVI_ATTR_RECORD_COERCIONS        /* ViBoolean */
#define NIFGEN_ATTR_SIMULATE                                  IVI_ATTR_SIMULATE                /* ViBoolean */
#define NIFGEN_ATTR_INTERCHANGE_CHECK                         IVI_ATTR_INTERCHANGE_CHECK       /* ViBoolean */
/*- Driver Information, Read-only ------------------------------------------*/
#define NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION               IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION              /* ViString */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_PREFIX                    IVI_ATTR_SPECIFIC_DRIVER_PREFIX                   /* ViString */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR                    IVI_ATTR_SPECIFIC_DRIVER_VENDOR                   /* ViString */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION                  IVI_ATTR_SPECIFIC_DRIVER_REVISION                 /* ViString */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32  */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32  */
/*- Driver Capabilities, Read-only -----------------------------------------*/
#define NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS              IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS /* ViString */
#define NIFGEN_ATTR_GROUP_CAPABILITIES                       IVI_ATTR_GROUP_CAPABILITIES          /* ViString */
#define NIFGEN_ATTR_CHANNEL_COUNT                            IVI_ATTR_CHANNEL_COUNT               /* ViInt32,  Read-only  */
/*- Instrument Information, Read-only --------------------------------------*/
#define NIFGEN_ATTR_INSTRUMENT_MANUFACTURER                  IVI_ATTR_INSTRUMENT_MANUFACTURER      /* ViString */
#define NIFGEN_ATTR_INSTRUMENT_MODEL                         IVI_ATTR_INSTRUMENT_MODEL             /* ViString */
#define NIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION             IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION /* ViString */
#define NIFGEN_ATTR_MODULE_REVISION                          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 390L)/* ViString */
/*- Advanced Session Information, read-only --------------------------------*/
#define NIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR                   IVI_ATTR_IO_RESOURCE_DESCRIPTOR /* ViString */
#define NIFGEN_ATTR_LOGICAL_NAME                             IVI_ATTR_LOGICAL_NAME           /* ViString */
#define NIFGEN_ATTR_DRIVER_SETUP                             IVI_ATTR_DRIVER_SETUP           /* ViString */


/****************************************************************************
 *------------------------ Attribute Value Defines -------------------------*
 ****************************************************************************/

#define NIFGEN_VAL_TRIG_SRC_RANGE               (200L)
#define NIFGEN_VAL_CLK_SRC_BASE                 (IVIFGEN_VAL_CLK_SRC_SPECIFIC_EXT_BASE + NIFGEN_VAL_TRIG_SRC_RANGE)

/*- Defined value for NIFGEN_ATTR_OPERATION_MODE -----------------------*/
#define NIFGEN_VAL_OPERATE_CONTINUOUS           IVIFGEN_VAL_OPERATE_CONTINUOUS

/*- Defined values for attribute NIFGEN_ATTR_OUTPUT_MODE ---------------*/
#define NIFGEN_VAL_OUTPUT_FUNC                  IVIFGEN_VAL_OUTPUT_FUNC
#define NIFGEN_VAL_OUTPUT_ARB                   IVIFGEN_VAL_OUTPUT_ARB
#define NIFGEN_VAL_OUTPUT_SEQ                   IVIFGEN_VAL_OUTPUT_SEQ
#define NIFGEN_VAL_OUTPUT_FREQ_LIST             (101L)
#define NIFGEN_VAL_OUTPUT_SCRIPT                (102L)

/*- Defined values for attribute NIFGEN_ATTR_OUTPUT_IMPEDANCE ----------*/
#define NIFGEN_VAL_50_OHMS                      50.0
#define NIFGEN_VAL_75_OHMS                      75.0

/*- Defined values for attribute NIFGEN_ATTR_LOAD_IMPEDANCE ----------*/
#define NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE       -1.0

/*- Defined values for attribute NIFGEN_ATTR_FUNC_WAVEFORM -------------*/
#define NIFGEN_VAL_WFM_SINE                     IVIFGEN_VAL_WFM_SINE
#define NIFGEN_VAL_WFM_SQUARE                   IVIFGEN_VAL_WFM_SQUARE
#define NIFGEN_VAL_WFM_TRIANGLE                 IVIFGEN_VAL_WFM_TRIANGLE
#define NIFGEN_VAL_WFM_RAMP_UP                  IVIFGEN_VAL_WFM_RAMP_UP
#define NIFGEN_VAL_WFM_RAMP_DOWN                IVIFGEN_VAL_WFM_RAMP_DOWN
#define NIFGEN_VAL_WFM_DC                       IVIFGEN_VAL_WFM_DC
#define NIFGEN_VAL_WFM_NOISE                    (101L)
#define NIFGEN_VAL_WFM_USER                     (102L)

/*- Defined values for attribute NIFGEN_ATTR_ARB_WAVEFORM_HANDLE ---------*/
#define NIFGEN_VAL_FIRST_WAVEFORM_HANDLE        (10000L)
#define NIFGEN_VAL_LAST_WAVEFORM_HANDLE         (NIFGEN_VAL_FIRST_WAVEFORM_HANDLE + 999L)
#define NIFGEN_VAL_NO_WAVEFORM                  (-1L)

/*- Defined values for attribute NIFGEN_ATTR_ARB_SEQUENCE_HANDLE --------*/
#define NIFGEN_VAL_FIRST_SEQUENCE_HANDLE        (100000L)
#define NIFGEN_VAL_LAST_SEQUENCE_HANDLE         (NIFGEN_VAL_FIRST_SEQUENCE_HANDLE + 9999L)
#define NIFGEN_VAL_NO_SEQUENCE                  (-1L)

/*- Defined values for attribute NIFGEN_ATTR_FREQ_LIST_HANDLE --------*/
#define NIFGEN_VAL_FIRST_FREQ_LIST_HANDLE       (200000L)
#define NIFGEN_VAL_LAST_FREQ_LIST_HANDLE        (NIFGEN_VAL_FIRST_FREQ_LIST_HANDLE + 9999L)
#define NIFGEN_VAL_NO_FREQ_LIST                 (-1L)

/*- Defined values for Arbitrary Waveform Handles ----------------------*/
#define NIFGEN_VAL_ALL_WAVEFORMS                IVIFGEN_VAL_ALL_WAVEFORMS
#define NIFGEN_VAL_ALL_SEQUENCES                IVIFGEN_VAL_ALL_SEQUENCES
#define NIFGEN_VAL_ALL_FLISTS                   (-1L)

/*- Defined values for atttribute NIFGEN_ATTR_BURST_COUNT ---------------*/
#define NIFGEN_VAL_GENERATE_CONTINUOUS          (-1L)

/*- Defined values for attribute NIFGEN_ATTR_TERMINAL_CONFIGURATION -----*/
#define NIFGEN_VAL_SINGLE_ENDED                 (300L)
#define NIFGEN_VAL_DIFFERENTIAL                 (301L)

/*- Defined values for Signal Values ---------------------------------*/
#define NIFGEN_VAL_MARKER_EVENT                                (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 1L)  /* ViInt32 */
#define NIFGEN_VAL_SYNC_OUT                                    (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 2L)  /* ViInt32 */
#define NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK                     (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 19L) /* ViInt32 */
#define NIFGEN_VAL_START_TRIGGER                               (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 4L)  /* ViInt32 */
#define NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE                       (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 6L)
#define NIFGEN_VAL_SYNCHRONIZATION                             (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 7L)  /* ViInt32 */
#define NIFGEN_VAL_SAMPLE_CLOCK                                (101L)
#define NIFGEN_VAL_REFERENCE_CLOCK                             (102L)
#define NIFGEN_VAL_SCRIPT_TRIGGER                              (103L)
#define NIFGEN_VAL_READY_FOR_START_EVENT                       (105L)
#define NIFGEN_VAL_STARTED_EVENT                               (106L)
#define NIFGEN_VAL_DONE_EVENT                                  (107L)
#define NIFGEN_VAL_DATA_MARKER_EVENT                           (108L)

/*- Additional defined values for 5404 signal routing ----------------*/
#define NIFGEN_VAL_NONE                         (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 0L)
#define NIFGEN_VAL_MARKER                       (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 1L)
#define NIFGEN_VAL_OUT_START_TRIGGER            (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 4L)
#define NIFGEN_VAL_BOARD_CLOCK                  (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 6L)
#define NIFGEN_VAL_REF_OUT                      (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 8L)
#define NIFGEN_VAL_CLOCK_OUT                    (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 9L)
#define NIFGEN_VAL_RTSI_7                       (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 10L)
#define NIFGEN_VAL_PFI_0                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 11L)

/*- Defined values for Digital Edge ----------------------------------*/
#define NIFGEN_VAL_RISING_EDGE                                 (101L)
#define NIFGEN_VAL_FALLING_EDGE                                (102L)

/*- Defined values for Toggle ----------------------------------------*/
#define NIFGEN_VAL_HIGH                                        (101L)
#define NIFGEN_VAL_LOW                                         (102L)

/*- Defined values for Event polarity --------------------------------*/
#define NIFGEN_VAL_ACTIVE_HIGH                                 (101L)
#define NIFGEN_VAL_ACTIVE_LOW                                  (102L)

/*- Defined values for Output Behavior -------------------------------*/
#define NIFGEN_VAL_PULSE                                       (101L)
#define NIFGEN_VAL_LEVEL                                       (102L)
#define NIFGEN_VAL_TOGGLE                                      (103L)

/*- Defined values for Pulse Width & Delay ---------------------------*/
#define NIFGEN_VAL_SAMPLE_CLOCK_PERIODS                        (101L)
#define NIFGEN_VAL_SECONDS                                     (102L)

/*- Defined values for Triggers types --------------------------------*/
#define NIFGEN_VAL_TRIG_NONE                                   (101L)                                   /* ViInt32 */
#define NIFGEN_VAL_DIGITAL_EDGE                                (102L)                                   /* ViInt32 */
#define NIFGEN_VAL_DIGITAL_LEVEL                               (103L)                                   /* ViInt32 */
#define NIFGEN_VAL_SOFTWARE_EDGE                               (104L)                                   /* ViInt32 */
#define NIFGEN_VAL_SOFTWARE_LEVEL                              (105L)                                   /* ViInt32 */
#define NIFGEN_VAL_P2P_ENDPOINT_FULLNESS                       (106L)                                   /* ViInt32 */

/*- Defined values for attribute NIFGEN_ATTR_TRIGGER_MODE ------------*/
#define NIFGEN_VAL_SINGLE                       1L
#define NIFGEN_VAL_CONTINUOUS                   2L
#define NIFGEN_VAL_STEPPED                      3L
#define NIFGEN_VAL_BURST                        4L

/*- Defined values for attribute NIFGEN_ATTR_ARB_SAMPLE_RATE ---------*/
#define NIFGEN_VAL_EXTERNAL_SAMPLE_RATE         -1.0

/*- Defined values for attribute NIFGEN_ATTR_CLOCK_MODE --------------*/
#define NIFGEN_VAL_HIGH_RESOLUTION               0L
#define NIFGEN_VAL_DIVIDE_DOWN                   1L
#define NIFGEN_VAL_AUTOMATIC                     2L

/*- Defined values for attribute NIFGEN_ATTR_IDLE_BEHAVIOR and NIFGEN_ATTR_WAIT_BEHAVIOR ---*/
#define NIFGEN_VAL_HOLD_LAST_VALUE               400L
#define NIFGEN_VAL_JUMP_TO_VALUE                 401L

/*- Defined values for Arbitrary Sequence Creation -------------------*/
#define NIFGEN_VAL_INFINITE_LOOP                 0L
#define NIFGEN_VAL_WHOLE_BUFFER                  0L
#define NIFGEN_VAL_NO_MARKER                    -1L
#define NIFGEN_VAL_MARKER_QUANTUM                8L

/*- Defined Values for Bus Type --------------------------------------*/
#define NIFGEN_VAL_BUS_INVALID                   0L
#define NIFGEN_VAL_BUS_AT                        1L
#define NIFGEN_VAL_BUS_PCI                       2L
#define NIFGEN_VAL_BUS_PXI                       3L
#define NIFGEN_VAL_BUS_VXI                       4L
#define NIFGEN_VAL_BUS_PCMCIA                    5L
#define NIFGEN_VAL_BUS_PXIE                      6L

/*- Defined Values for Video Waveform Type ---------------------------*/
#define NIFGEN_VAL_PAL_B                         0L
#define NIFGEN_VAL_PAL_D                         1L
#define NIFGEN_VAL_PAL_G                         2L
#define NIFGEN_VAL_PAL_H                         3L
#define NIFGEN_VAL_PAL_I                         4L
#define NIFGEN_VAL_PAL_M                         5L
#define NIFGEN_VAL_PAL_N                         6L
#define NIFGEN_VAL_NTSC_M                        7L

/*- Defined Values for Next Waveform Write Position ------------------*/
#define NIFGEN_VAL_WAVEFORM_POSITION_START       0L
#define NIFGEN_VAL_WAVEFORM_POSITION_CURRENT     1L

/*- Defined values for attribute NIFGEN_ATTR_ANALOG_PATH -------------*/
#define NIFGEN_VAL_MAIN_ANALOG_PATH              0L
#define NIFGEN_VAL_DIRECT_ANALOG_PATH            1L
#define NIFGEN_VAL_FIXED_LOW_GAIN_ANALOG_PATH    2L
#define NIFGEN_VAL_FIXED_HIGH_GAIN_ANALOG_PATH   3L

/*- Defined values for attribute NIFGEN_ATTR_CAL_ADC_INPUT -----------*/
#define NIFGEN_VAL_ANALOG_OUTPUT                 0L
#define NIFGEN_VAL_INTERNAL_VOLTAGE_REFERENCE    1L
#define NIFGEN_VAL_GROUND                        2L
#define NIFGEN_VAL_ANALOG_OUTPUT_DIFFERENTIAL    3L
#define NIFGEN_VAL_ANALOG_OUTPUT_PLUS            4L
#define NIFGEN_VAL_ANALOG_OUTPUT_MINUS           5L

/*- Defined values for action in niFgen_CloseExtCal()  ---------------*/
#define NIFGEN_VAL_EXT_CAL_ABORT                 0L
#define NIFGEN_VAL_EXT_CAL_COMMIT                1L

/*- Defined values for state in niFgen_GetHardwareState ()  ----------*/
#define NIFGEN_VAL_IDLE                          0L
#define NIFGEN_VAL_WAITING_FOR_START_TRIGGER     100L
#define NIFGEN_VAL_RUNNING                       200L
#define NIFGEN_VAL_DONE                          600L
#define NIFGEN_VAL_HARDWARE_ERROR                1000L

/*- Defined values for byte order in From File functions -------------*/
#define NIFGEN_VAL_LITTLE_ENDIAN                 0L
#define NIFGEN_VAL_BIG_ENDIAN                    1L

/*- Defined values for configuration in niFgen_CalAdjustMainPathPreAmpOffset ()
    and niFgen_CalAdjustMainPathPreAmpGain ()  -*/
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB         0L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB         1L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB         2L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB         3L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB        4L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB          5L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB          6L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB          7L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB          8L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB         9L

/*- Defined values for configuration in niFgen_CalAdjustMainPathPostAmpGainAndOffset ()  -*/
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_0DB           0L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_12DB          1L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_24DB          2L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_36DB          3L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_0DB          4L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_12DB         5L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_24DB         6L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_36DB         7L

/*- Defined values for configuration in niFgen_CalAdjustMainPathOutputImpedance ()  -*/
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_0DB_50OHMS    0L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_0DB_75OHMS    1L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_12DB_50OHMS   2L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_12DB_75OHMS   3L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_24DB_50OHMS   4L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_24DB_75OHMS   5L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_36DB_50OHMS   6L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_36DB_75OHMS   7L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_0DB_50OHMS   8L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_0DB_75OHMS   9L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_12DB_50OHMS  10L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_12DB_75OHMS  11L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_24DB_50OHMS  12L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_24DB_75OHMS  13L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_36DB_50OHMS  14L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_36DB_75OHMS  15L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_DIFFERENTIAL           16L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_RSE                    17L

/*- Defined values for configuration in niFgen_CalAdjustDirectPathOutputImpedance ()  -*/
#define NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_50OHMS               0L
#define NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_75OHMS               1L
#define NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_DIFFERENTIAL         2L


/*- Defined values for configuration in niFgen_CalAdjustFlatness and niFgen_CalAdjustCalADC ()  -*/
#define NIFGEN_VAL_CAL_CONFIG_GLOBAL                          -1L
#define NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_0DB        0L
#define NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_3DB        1L
#define NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_6DB        2L
#define NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_9DB        3L
#define NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_12DB       4L
#define NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_0DB       5L
#define NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_3DB       6L
#define NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_6DB       7L
#define NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_9DB       8L
#define NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_12DB      9L
#define NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH                     10L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH                       11L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_0DB                   12L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_9DB                   13L
#define NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_33DB                  14L

/*- Defined values for NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE -*/
#define NIFGEN_VAL_OSP_REAL                                    0L
#define NIFGEN_VAL_OSP_COMPLEX                                 1L

/*- Defined values for NIFGEN_ATTR_OSP_MODE -*/
#define NIFGEN_VAL_OSP_IF                                      0L
#define NIFGEN_VAL_OSP_BASEBAND                                1L

/*- Defined values for NIFGEN_ATTR_OSP_FIR_FILTER_TYPE -*/
#define NIFGEN_VAL_OSP_FLAT                                    0L
#define NIFGEN_VAL_OSP_RAISED_COSINE                           1L
#define NIFGEN_VAL_OSP_ROOT_RAISED_COSINE                      2L
#define NIFGEN_VAL_OSP_GAUSSIAN                                3L
#define NIFGEN_VAL_OSP_CUSTOM                                  4L

/*- Defined bit mask values for NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING -*/
#define NIFGEN_VAL_ERROR_REPORTING_ERROR                       0L
#define NIFGEN_VAL_ERROR_REPORTING_DISABLED                    2L

/*- Defined bit mask values for NIFGEN_ATTR_OSP_OVERFLOW_STATUS -*/
#define NIFGEN_VAL_OSP_OVERFLOW_NONE                           0L
#define NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I              1L
#define NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q              2L
#define NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I            4L
#define NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q            8L
#define NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_I                   16L
#define NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_I                  16L
#define NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_Q                   32L
#define NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_Q                  32L
#define NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_I                   64L
#define NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_Q                   128L
#define NIFGEN_VAL_OSP_OVERFLOW_COMPLEX_DATA                   256L
#define NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_I                  512L
#define NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_Q                  1024L
#define NIFGEN_VAL_OSP_OVERFLOW_EQUALIZER                      2048L

/*- Defined values for P2P Address Type Attributes -*/
#define NIFGEN_VAL_ADDR_PHYSICAL                               0L
#define NIFGEN_VAL_ADDR_VIRTUAL                                1L



/****************************************************************************
 *---------------- Instrument Driver struct definititions  -----------------*
 ****************************************************************************/

/*- Use with:
      niFgen_CreateWaveformComplexF64
      niFgen_WriteWaveformComplexF64
      niFgen_WriteNamedWaveformComplexF64
*/
#if !defined(_NIComplexNumber)
typedef struct NIComplexNumber_struct {
   ViReal64 real;
   ViReal64 imaginary;
} NIComplexNumber;
#define _NIComplexNumber
#endif

/*- Use with:
      niFgen_WriteComplexBinary16Waveform
      niFgen_WriteNamedWaveformComplexI16
*/
#if !defined(_NIComplexI16)
typedef struct NIComplexI16_struct {
   ViInt16 real;
   ViInt16 imaginary;
} NIComplexI16;
#define _NIComplexI16
#endif


/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

/*- Init and Close Functions -------------------------------------------*/

ViStatus _VI_FUNC  niFgen_init(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViSession *vi);

ViStatus _VI_FUNC  niFgen_InitWithOptions(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession *newVi);

ViStatus _VI_FUNC niFgen_InitializeWithChannels(
   ViRsrc resourceName,
   ViConstString channelName,
   ViBoolean resetDevice,
   ViConstString optionString,
   ViSession *newVi);

ViStatus _VI_FUNC  niFgen_close(
   ViSession vi);

/*- Required VXIplug&play Functions -------------------------------------*/

ViStatus _VI_FUNC niFgen_reset(
   ViSession vi);

ViStatus _VI_FUNC niFgen_self_test(
   ViSession vi,
   ViInt16 *testResult,/*Output*/
   ViChar testMessage[]);

ViStatus _VI_FUNC niFgen_error_query(
   ViSession vi,
   ViInt32 *errorCode,
   ViChar selfTestMessage[]);

ViStatus _VI_FUNC niFgen_error_message(
   ViSession vi,
   ViStatus statusCode,
   ViChar message[]);

ViStatus _VI_FUNC niFgen_revision_query(
   ViSession vi,
   ViChar driverRev[],
   ViChar instrRev[]);

/*- Error Functions --------------------------------------------------------*/
ViStatus _VI_FUNC niFgen_GetError(
   ViSession vi,
   ViStatus *errorCode,
   ViInt32 errorDescriptionBufferSize,
   ViChar errorDescription[]);

ViStatus _VI_FUNC niFgen_ClearError(
   ViSession vi);

ViStatus _VI_FUNC niFgen_ErrorHandler(
   ViSession vi,
   ViStatus statusCode,
   ViChar errorMessage[256]);

/*- Required IVI Functions ---------------------------------------------*/
ViStatus _VI_FUNC niFgen_LockSession(
   ViSession vi,
   ViBoolean *callerHasLock);

ViStatus _VI_FUNC niFgen_UnlockSession(
   ViSession vi,
   ViBoolean *callerHasLock);

/*- Channel Info Functions ---------------------------------------------*/
ViStatus _VI_FUNC niFgen_GetChannelName(
   ViSession vi,
   ViInt32 index,
   ViInt32 bufferSize,
   ViChar name[]);

/*- Interchangeability Checking Functions ------------------------------*/
ViStatus _VI_FUNC niFgen_GetNextInterchangeWarning(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar warnString[]);

ViStatus _VI_FUNC niFgen_ResetInterchangeCheck(
   ViSession vi);

ViStatus _VI_FUNC niFgen_ClearInterchangeWarnings(
   ViSession vi);

ViStatus _VI_FUNC niFgen_GetNextCoercionRecord(
   ViSession vi,
   ViInt32 bufferSize,
   ViChar record[]);

/*- Utility Functions --------------------------------------------------*/
ViStatus _VI_FUNC niFgen_InvalidateAllAttributes(
   ViSession vi);

ViStatus _VI_FUNC niFgen_ResetWithDefaults(
   ViSession vi);

ViStatus _VI_FUNC niFgen_Disable(
   ViSession vi);

ViStatus _VI_FUNC niFgen_Commit(
   ViSession vi);

ViStatus _VI_FUNC niFgen_GetHardwareState(
   ViSession vi,
   ViInt32* state);

ViStatus _VI_FUNC niFgen_WaitUntilDone(
   ViSession vi,
   ViInt32  maxTime);

ViStatus _VI_FUNC niFgen_IsDone(
   ViSession vi,
   ViBoolean* done);

ViStatus _VI_FUNC niFgen_ResetDevice(
   ViSession vi);

/*- Basic Instrument Operation -----------------------------------------*/
ViStatus _VI_FUNC niFgen_ConfigureOperationMode(
   ViSession vi,
   ViConstString channelName,
   ViInt32 mode);

ViStatus _VI_FUNC niFgen_ConfigureOutputMode(
   ViSession vi,
   ViInt32 outputMode);

ViStatus _VI_FUNC niFgen_ConfigureReferenceClock(
   ViSession vi,
   ViConstString referenceClockSource,
   ViReal64 referenceClockFrequency);

ViStatus _VI_FUNC niFgen_ConfigureOutputImpedance(
   ViSession vi,
   ViConstString channelName,
   ViReal64 outputImpedance);

ViStatus _VI_FUNC niFgen_ConfigureOutputEnabled(
   ViSession vi,
   ViConstString channelName,
   ViBoolean enabled);

ViStatus _VI_FUNC niFgen_ConfigureChannels(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_InitiateGeneration(
   ViSession vi);

ViStatus _VI_FUNC niFgen_AbortGeneration(
   ViSession vi);

/*- Standard Function Output -------------------------------------------*/
ViStatus _VI_FUNC niFgen_ConfigureStandardWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveform,
   ViReal64 amplitude,
   ViReal64 dcOffset,
   ViReal64 frequency,
   ViReal64 startPhase);

ViStatus _VI_FUNC niFgen_DefineUserStandardWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   ViReal64 data[]);

ViStatus _VI_FUNC niFgen_ClearUserStandardWaveform(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_ConfigureFrequency(
   ViSession vi,
   ViConstString channelName,
   ViReal64 Frequency);

ViStatus _VI_FUNC niFgen_ConfigureAmplitude(
   ViSession vi,
   ViConstString channelName,
   ViReal64 Amplitude);

/*- Arbitrary Waveform Output ------------------------------------------*/
ViStatus _VI_FUNC niFgen_QueryArbWfmCapabilities(
   ViSession vi,
   ViInt32 *maxNumWfms,
   ViInt32 *wfmQuantum,
   ViInt32 *minNumberOfSamples,
   ViInt32 *maxNumberOfSamples);

ViStatus _VI_FUNC  niFgen_CreateWaveformF64(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   ViReal64 wfmData[],
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_CreateWaveformI16(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   ViInt16 wfmData[],
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_CreateWaveformComplexF64(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   NIComplexNumber wfmData[],
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_CreateWaveformFromFileI16(
   ViSession vi,
   ViConstString channelName,
   ViConstString fileName,
   ViInt32 byteOrder,
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_CreateWaveformFromFileF64(
   ViSession vi,
   ViConstString channelName,
   ViConstString fileName,
   ViInt32 byteOrder,
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_CreateWaveformFromFileHWS(
   ViSession vi,
   ViConstString channelName,
   ViConstString fileName,
   ViBoolean useRateFromWaveform,
   ViBoolean useGainAndOffsetFromWaveform,
   ViInt32 *wfmHandle);

ViStatus _VI_FUNC  niFgen_ConfigureSampleRate(
   ViSession vi,
   ViReal64 sampleRate);

ViStatus _VI_FUNC  niFgen_ConfigureArbWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 wfmHandle,
   ViReal64 arbGain,
   ViReal64 arbOffset);

ViStatus _VI_FUNC  niFgen_ClearArbWaveform (
   ViSession vi,
   ViInt32 wfmHandle);

ViStatus _VI_FUNC niFgen_AllocateNamedWaveform(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 numberOfSamples);

ViStatus _VI_FUNC niFgen_SetNamedWaveformNextWritePosition(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 relativeTo,
   ViInt32 offset);

ViStatus _VI_FUNC niFgen_WriteNamedWaveformF64(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 numberOfSamples,
   ViReal64 wfmData[]);

ViStatus _VI_FUNC niFgen_WriteNamedWaveformI16(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 numberOfSamples,
   ViInt16 wfmData[]);

ViStatus _VI_FUNC niFgen_WriteNamedWaveformComplexF64(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 numberOfSamples,
   NIComplexNumber wfmData[]);

ViStatus _VI_FUNC niFgen_WriteNamedWaveformComplexI16(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName,
   ViInt32 numberOfSamples,
   NIComplexI16 wfmData[]);

ViStatus _VI_FUNC niFgen_DeleteNamedWaveform(
   ViSession vi,
   ViConstString channelName,
   ViConstString wfmName);

/*- Arbitrary Sequence Output ------------------------------------------*/
ViStatus _VI_FUNC niFgen_QueryArbSeqCapabilities(
   ViSession vi,
   ViInt32 *maxNumSeqs,
   ViInt32 *minSeqLength,
   ViInt32 *maxSeqLength,
   ViInt32 *maxLoopCount);

ViStatus _VI_FUNC niFgen_CreateArbSequence(
   ViSession vi,
   ViInt32 seqLength,
   ViInt32 wfmHandle[],
   ViInt32 wfmLoopCount[],
   ViInt32 *seqHandle);

ViStatus _VI_FUNC  niFgen_CreateAdvancedArbSequence(
   ViSession vi,
   ViInt32 seqLength,
   ViInt32 wfmHandles[],
   ViInt32 loopCounts[],
   ViInt32 sampleCounts[],
   ViInt32 markers[],
   ViInt32 coercedMarkers[],
   ViInt32 *seqHandle);

ViStatus _VI_FUNC niFgen_ConfigureArbSequence(
   ViSession vi,
   ViConstString channelName,
   ViInt32 seqHandle,
   ViReal64 arbGain,
   ViReal64 arbOffset);

ViStatus _VI_FUNC niFgen_ClearArbSequence(
   ViSession vi,
   ViInt32 seqHandle);

ViStatus _VI_FUNC niFgen_ClearArbMemory(
   ViSession vi);

/*- Frequency List Output ----------------------------------------------*/
ViStatus _VI_FUNC niFgen_QueryFreqListCapabilities(
   ViSession vi,
   ViInt32 *maximumNumberOfFreqLists,
   ViInt32 *minimumFrequencyListLength,
   ViInt32 *maximumFrequencyListLength,
   ViReal64 *minimumFrequencyListDuration,
   ViReal64 *maximumFrequencyListDuration,
   ViReal64 *frequencyListDurationQuantum);

ViStatus _VI_FUNC niFgen_CreateFreqList(
   ViSession vi,
   ViInt32 waveform,
   ViInt32 frequencyListLength,
   ViReal64 frequencyArray[],
   ViReal64 durationArray[],
   ViInt32 *frequencyListHandle);

ViStatus _VI_FUNC niFgen_ConfigureFreqList(
   ViSession vi,
   ViConstString channelName,
   ViInt32 frequencyListHandle,
   ViReal64 amplitude,
   ViReal64 dcOffset,
   ViReal64 startPhase);

ViStatus _VI_FUNC niFgen_ClearFreqList(
   ViSession vi,
   ViInt32 frequencyListHandle);

/*- Script Output ----------------------------------------------------*/
ViStatus _VI_FUNC niFgen_WriteScript(
   ViSession vi,
   ViConstString channelName,
   ViConstString script);

ViStatus _VI_FUNC niFgen_DeleteScript(
   ViSession vi,
   ViConstString channelName,
   ViConstString scriptName);

/*- Routing ------------------------------------------------------------*/
ViStatus _VI_FUNC niFgen_ExportSignal(
   ViSession vi,
   ViInt32 signal,
   ViConstString signalIdentifier,
   ViConstString outputTerminal);

/*- 5404 Routing -------------------------------------------------------*/
ViStatus _VI_FUNC  niFgen_RouteSignalOut(
   ViSession vi,
   ViConstString channelName,
   ViInt32 from,
   ViInt32 to);

/*- Triggering ---------------------------------------------------------*/
ViStatus _VI_FUNC niFgen_SendSoftwareEdgeTrigger(
   ViSession vi,
   ViInt32 triggerName,
   ViConstString triggerIdentifier);


/* Start Trigger */

ViStatus _VI_FUNC niFgen_ConfigureDigitalEdgeStartTrigger(
   ViSession vi,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niFgen_ConfigureSoftwareEdgeStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niFgen_DisableStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niFgen_ConfigureP2PEndpointFullnessStartTrigger(
   ViSession vi,
   ViInt32 p2pEndpointFullnessLevel);


/* Script Trigger */

ViStatus _VI_FUNC niFgen_ConfigureDigitalEdgeScriptTrigger(
   ViSession vi,
   ViConstString triggerID,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niFgen_ConfigureDigitalLevelScriptTrigger(
   ViSession vi,
   ViConstString triggerID,
   ViConstString source,
   ViInt32 level);

ViStatus _VI_FUNC niFgen_ConfigureSoftwareEdgeScriptTrigger(
   ViSession vi,
   ViConstString triggerID);

ViStatus _VI_FUNC niFgen_DisableScriptTrigger(
   ViSession vi,
   ViConstString triggerID);

/*- Sampling Control -----------------------------------------------------*/
ViStatus _VI_FUNC niFgen_ConfigureClockMode(
   ViSession vi,
   ViInt32 clockMode);

ViStatus _VI_FUNC niFgen_AdjustSampleClockRelativeDelay(
   ViSession vi,
   ViReal64 time);

/*- Incremental Write -----------------------------------------------------*/
ViStatus _VI_FUNC niFgen_AllocateWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   ViInt32* waveformHandle);

ViStatus _VI_FUNC niFgen_SetWaveformNextWritePosition(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformHandle,
   ViInt32 relativeTo,
   ViInt32 offset);

ViStatus _VI_FUNC niFgen_WriteWaveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformHandle,
   ViInt32 numberOfSamples,
   ViReal64 wfmData[]);

ViStatus _VI_FUNC niFgen_WriteBinary16Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformHandle,
   ViInt32 numberOfSamples,
   ViInt16 wfmData[]);

ViStatus _VI_FUNC  niFgen_WriteWaveformComplexF64(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfSamples,
   NIComplexNumber wfmData[],
   ViInt32 wfmHandle);

ViStatus _VI_FUNC  niFgen_WriteComplexBinary16Waveform(
   ViSession vi,
   ViConstString channelName,
   ViInt32 waveformHandle,
   ViInt32 numberOfSamples,
   NIComplexI16 wfmData[]);

/*- Calibration --------------------------------------------*/
ViStatus _VI_FUNC niFgen_InitExtCal(
   ViRsrc resourceName,
   ViConstString password,
   ViSession* vi);

ViStatus _VI_FUNC niFgen_InitializeOscillatorFrequencyCalibration(
   ViSession vi);

ViStatus _VI_FUNC niFgen_InitializeAnalogOutputCalibration(
   ViSession vi);

ViStatus _VI_FUNC niFgen_InitializeCalADCCalibration(
   ViSession vi);

ViStatus _VI_FUNC niFgen_InitializeFlatnessCalibration(
   ViSession vi);

ViStatus _VI_FUNC niFgen_CloseExtCal(
   ViSession vi,
   ViInt32 action);

ViStatus _VI_FUNC niFgen_SelfCal(
   ViSession vi);

ViStatus _VI_FUNC niFgen_RestoreLastExtCalConstants(
   ViSession vi);

ViStatus _VI_FUNC niFgen_GetSelfCalSupported(
   ViSession vi,
   ViBoolean* selfCalSupported);

ViStatus _VI_FUNC niFgen_GetSelfCalLastDateAndTime(
   ViSession vi,
   ViInt32* year,
   ViInt32* month,
   ViInt32* day,
   ViInt32* hour,
   ViInt32* minute);

ViStatus _VI_FUNC niFgen_GetExtCalLastDateAndTime(
   ViSession vi,
   ViInt32* year,
   ViInt32* month,
   ViInt32* day,
   ViInt32* hour,
   ViInt32* minute);

ViStatus _VI_FUNC niFgen_GetSelfCalLastTemp(
   ViSession vi,
   ViReal64* temp);

ViStatus _VI_FUNC niFgen_GetExtCalLastTemp(
   ViSession vi,
   ViReal64* temp);

ViStatus _VI_FUNC niFgen_GetExtCalRecommendedInterval(
   ViSession vi,
   ViInt32* months);

ViStatus _VI_FUNC niFgen_ChangeExtCalPassword(
   ViSession vi,
   ViConstString oldPassword,
   ViConstString newPassword);

ViStatus _VI_FUNC niFgen_SetCalUserDefinedInfo(
   ViSession vi,
   ViConstString info);

ViStatus _VI_FUNC niFgen_GetCalUserDefinedInfo(
   ViSession vi,
   ViString info);

ViStatus _VI_FUNC niFgen_GetCalUserDefinedInfoMaxSize(
   ViSession vi,
   ViInt32* infoSize);

ViStatus _VI_FUNC niFgen_ReadCurrentTemperature(
   ViSession vi,
   ViReal64* temperature);

ViStatus _VI_FUNC niFgen_ReadCalADC(
   ViSession vi,
   ViInt32 numberOfReadsToAverage,
   ViBoolean returnCalibratedValue,
   ViReal64* calADCValue);

ViStatus _VI_FUNC niFgen_WriteBinary16AnalogStaticValue(
   ViSession vi,
   ViConstString channelName,
   ViInt16 value);


/*- Calibration Adjust Functions-------------------------------------*/

ViStatus _VI_FUNC niFgen_CalAdjustMainPathPreAmpOffset(
   ViSession vi,
   ViConstString channelName,
   ViInt32  configuration,
   ViInt32* gainDACValues,
   ViInt32* offsetDACValues,
   ViReal64* measuredOutputs);

ViStatus _VI_FUNC niFgen_CalAdjustMainPathPreAmpGain(
   ViSession vi,
   ViConstString channelName,
   ViInt32  configuration,
   ViInt32* mainDACValues,
   ViInt32* gainDACValues,
   ViInt32* offsetDACValues,
   ViReal64* measuredOutputs);

ViStatus _VI_FUNC niFgen_CalAdjustMainPathPostAmpGainAndOffset(
   ViSession vi,
   ViConstString channelName,
   ViInt32  configuration,
   ViInt32* mainDACValues,
   ViInt32* gainDACValues,
   ViInt32* offsetDACValues,
   ViReal64* measuredOutputs);

ViStatus _VI_FUNC niFgen_CalAdjustDirectPathGain(
   ViSession vi,
   ViConstString channelName,
   ViInt32* mainDACValues,
   ViInt32* gainDACValues,
   ViReal64* measuredOutputs);

ViStatus _VI_FUNC niFgen_CalAdjustMainPathOutputImpedance(
   ViSession vi,
   ViConstString channelName,
   ViInt32 configuration,
   ViReal64 loadImpedance,
   ViReal64 measuredSourceVoltage,
   ViReal64 measuredVoltageAcrossLoad);

ViStatus _VI_FUNC niFgen_CalAdjustDirectPathOutputImpedance(
   ViSession vi,
   ViConstString channelName,
   ViInt32 configuration,
   ViReal64 loadImpedance,
   ViReal64 measuredSourceVoltage,
   ViReal64 measuredVoltageAcrossLoad);

ViStatus _VI_FUNC niFgen_CalAdjustOscillatorFrequency(
   ViSession vi,
   ViReal64 desiredFrequencyInHz,
   ViReal64 measuredFrequencyInHz);

ViStatus _VI_FUNC niFgen_CalAdjustADC(
   ViSession vi,
   ViConstString channelName,
   ViInt32 configuration,
   ViReal64* voltagesMeasuredExternally,
   ViReal64* voltagesMeasuredWithCalADC);

ViStatus _VI_FUNC niFgen_CalAdjustFlatness(
   ViSession vi,
   ViConstString channelName,
   ViInt32 configuration,
   ViReal64 requestedAmplitude,
   ViReal64* frequencies,
   ViReal64* measuredAmplitudes,
   ViInt32 numberOfMeasurements);


/*- Onboard Signal Processing Functions --------------------------------*/
ViStatus _VI_FUNC niFgen_ConfigureCustomFIRFilterCoefficients(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfCoefficients,
   ViReal64* coefficients);

ViStatus _VI_FUNC niFgen_GetFIRFilterCoefficients(
   ViSession vi,
   ViConstString channelName,
   ViInt32 arraySize,
   ViReal64* coefficients,
   ViInt32* numberOfCoefficientsRead);


/*- Peer-to-Peer (P2P) Functions --------------------------------*/
ViStatus _VI_FUNC niFgen_GetStreamEndpointHandle(
   ViSession vi,
   ViConstString streamEndpoint,
   ViUInt32* readerHandle);

ViStatus _VI_FUNC niFgen_ManualEnableP2PStream(
   ViSession vi,
   ViConstString streamEndpoint);

ViStatus _VI_FUNC niFgen_WriteP2PEndpointI16(
   ViSession vi,
   ViConstString fifoEndpointName,
   ViInt32 numberOfSamples,
   ViInt16 endpointData[]);


/*- Miscellaneous Functions --------------------------------------------*/
ViStatus _VI_FUNC  niFgen_ConfigureSynchronization(
   ViSession vi,
   ViConstString channelName,
   ViInt32 Synchronization);

ViStatus _VI_FUNC niFgen_EnableDigitalPatterning(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_DisableDigitalPatterning(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_EnableDigitalFilter(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_DisableDigitalFilter(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_EnableAnalogFilter(
   ViSession vi,
   ViConstString channelName,
   ViReal64 filterCorrectionFreq);

ViStatus _VI_FUNC niFgen_DisableAnalogFilter(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_ConfigureSampleClockSource(
   ViSession vi,
   ViConstString sampleClockSource);

ViStatus _VI_FUNC niFgen_ConfigureTriggerMode(
   ViSession vi,
   ViConstString channelName,
   ViInt32 mode);

/*- Import and Export Attribute Configuration Functions -----------------*/
ViStatus _VI_FUNC niFgen_ImportAttributeConfigurationFile(
   ViSession vi,
   ViConstString filePath);

ViStatus _VI_FUNC niFgen_ExportAttributeConfigurationFile(
   ViSession vi,
   ViConstString filePath);

ViStatus _VI_FUNC niFgen_ImportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 size,
   ViAddr configuration);

ViStatus _VI_FUNC niFgen_ExportAttributeConfigurationBuffer(
   ViSession vi,
   ViInt32 size,
   ViAddr configuration);

/*- Attributes ---------------------------------------------------------*/
#ifdef _VI_INT64_UINT64_DEFINED
ViStatus _VI_FUNC niFgen_SetAttributeViInt64    (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 value) ;
ViStatus _VI_FUNC niFgen_CheckAttributeViInt64  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 value) ;
ViStatus _VI_FUNC niFgen_GetAttributeViInt64    (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 *value) ;
#endif

ViStatus _VI_FUNC niFgen_SetAttributeViInt32    (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 value) ;
ViStatus _VI_FUNC niFgen_SetAttributeViReal64   (ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 value) ;
ViStatus _VI_FUNC niFgen_SetAttributeViString   (ViSession vi, ViConstString channelName, ViAttr attributeId, ViConstString value) ;
ViStatus _VI_FUNC niFgen_SetAttributeViBoolean  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean value) ;
ViStatus _VI_FUNC niFgen_SetAttributeViSession  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession value) ;

ViStatus _VI_FUNC niFgen_CheckAttributeViInt32  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 value) ;
ViStatus _VI_FUNC niFgen_CheckAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 value) ;
ViStatus _VI_FUNC niFgen_CheckAttributeViString (ViSession vi, ViConstString channelName, ViAttr attributeId, ViConstString value) ;
ViStatus _VI_FUNC niFgen_CheckAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean value) ;
ViStatus _VI_FUNC niFgen_CheckAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession value) ;

ViStatus _VI_FUNC niFgen_GetAttributeViInt32    (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 *value) ;
ViStatus _VI_FUNC niFgen_GetAttributeViReal64   (ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 *value) ;
ViStatus _VI_FUNC niFgen_GetAttributeViString   (ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 bufSize, ViChar value[]) ;
ViStatus _VI_FUNC niFgen_GetAttributeViBoolean  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean *value) ;
ViStatus _VI_FUNC niFgen_GetAttributeViSession  (ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession *value) ;

ViStatus _VI_FUNC niFgen_ResetAttribute         (ViSession vi, ViConstString channelName, ViAttr attributeId);

/****************************************************************************
 *------------------------------- Error Codes ------------------------------*
 ****************************************************************************/
#define NIFGEN_ERROR_TRIGGER_NOT_SOFTWARE      IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE
#define NIFGEN_ERROR_NOT_CONFIGURABLE          0xBFFA2001
#define NIFGEN_ERROR_NOT_GENERATING            0xBFFA2002
#define NIFGEN_ERROR_INVALID_MODE              0xBFFA2003
#define NIFGEN_ERROR_NO_WFMS_AVAILABLE         IVIFGEN_ERROR_NO_WFMS_AVAILABLE
#define NIFGEN_ERROR_INVALID_WFM_LENGTH        0xBFFA2005
#define NIFGEN_ERROR_INVALID_WFM_ELEMENT       0xBFFA2006
#define NIFGEN_ERROR_INVALID_WAVEFORM          0xBFFA2007
#define NIFGEN_ERROR_WFM_IN_USE                IVIFGEN_ERROR_WFM_IN_USE
#define NIFGEN_ERROR_NO_SEQS_AVAILABLE         IVIFGEN_ERROR_NO_SEQS_AVAILABLE
#define NIFGEN_ERROR_INVALID_SEQ_LENGTH        0xBFFA200A
#define NIFGEN_ERROR_INVALID_LOOP_COUNT        0xBFFA200B
#define NIFGEN_ERROR_INVALID_SEQUENCE          0xBFFA200C
#define NIFGEN_ERROR_SEQ_IN_USE                IVIFGEN_ERROR_SEQ_IN_USE
#define NIFGEN_ERROR_INVALID_SESSION           0xBFFA1190

#define NIFGEN_ERROR_DAQ_PARAMETER_CHANGE      (IVI_SPECIFIC_ERROR_BASE + 1L)
#define NIFGEN_ERROR_DAQ_GROUP_CONTROL         (IVI_SPECIFIC_ERROR_BASE + 2L)
#define NIFGEN_ERROR_DAQ_SELECT_SIGNAL         (IVI_SPECIFIC_ERROR_BASE + 3L)
#define NIFGEN_ERROR_DAQ_GROUP_SETUP           (IVI_SPECIFIC_ERROR_BASE + 4L)
#define NIFGEN_ERROR_DAQ_CONFIGURE             (IVI_SPECIFIC_ERROR_BASE + 5L)
#define NIFGEN_ERROR_DAQ_INIT_BOARD            (IVI_SPECIFIC_ERROR_BASE + 6L)
#define NIFGEN_ERROR_DAQ_WFM_LOAD              (IVI_SPECIFIC_ERROR_BASE + 7L)
#define NIFGEN_ERROR_DAQ_GET_ATTRIBUTE         (IVI_SPECIFIC_ERROR_BASE + 8L)
#define NIFGEN_ERROR_INVALID_FREQ_LIST         (IVI_SPECIFIC_ERROR_BASE + 9L)
#define NIFGEN_ERROR_NO_FREQ_LISTS_AVAILABLE   (IVI_SPECIFIC_ERROR_BASE + 10L)
#define NIFGEN_ERROR_INVALID_FREQ_LIST_LENGTH  (IVI_SPECIFIC_ERROR_BASE + 11L)
#define NIFGEN_ERROR_DAQ_CLOCK_RATE            (IVI_SPECIFIC_ERROR_BASE + 12L)
#define NIFGEN_ERROR_INVALID_SAMPLE_COUNT      (IVI_SPECIFIC_ERROR_BASE + 13L)
#define NIFGEN_ERROR_INVALID_MARKER            (IVI_SPECIFIC_ERROR_BASE + 14L)
#define NIFGEN_ERROR_INVALID_FREQUENCY         (IVI_SPECIFIC_ERROR_BASE + 15L)
#define NIFGEN_ERROR_INVALID_DURATION          (IVI_SPECIFIC_ERROR_BASE + 16L)
#define NIFGEN_ERROR_DAQ_SET_CLOCK             (IVI_SPECIFIC_ERROR_BASE + 17L)
#define NIFGEN_ERROR_DAQ_DEVICE_INFO           (IVI_SPECIFIC_ERROR_BASE + 18L)
#define NIFGEN_ERROR_MAX_TIME_EXCEEDED         (IVI_SPECIFIC_ERROR_BASE + 19L)
#define NIFGEN_ERROR_NO_WFMS_EXIST             (IVI_SPECIFIC_ERROR_BASE + 20L)
#define NIFGEN_ERROR_NO_SEQS_EXIST             (IVI_SPECIFIC_ERROR_BASE + 21L)
#define NIFGEN_ERROR_NO_WFM_SPECIFIED          (IVI_SPECIFIC_ERROR_BASE + 22L)
#define NIFGEN_ERROR_NO_SEQ_SPECIFIED          (IVI_SPECIFIC_ERROR_BASE + 23L)
#define NIFGEN_ERROR_INVALID_DURING_SIMULATION (IVI_SPECIFIC_ERROR_BASE + 24L)
#define NIFGEN_ERROR_CAL_ADC_OVER_RANGE        (IVI_SPECIFIC_ERROR_BASE + 25L)
#define NIFGEN_ERROR_CAL_ADC_UNDER_RANGE       (IVI_SPECIFIC_ERROR_BASE + 26L)
#define NIFGEN_ERROR_HWS_ERROR                 (IVI_SPECIFIC_ERROR_BASE + 27L)
#define NIFGEN_ERROR_INSTRUMENT_ALREADY_IN_USE (IVI_SPECIFIC_ERROR_BASE + 28L)
#define NIFGEN_ERROR_SAMPLE_RATE_INVALID_FOR_INTERPOLATION (IVI_SPECIFIC_ERROR_BASE + 29L)
#define NIFGEN_ERROR_CODE_LAST                 (IVI_SPECIFIC_ERROR_BASE + 100L)

/* Warning codes */
#define NIFGEN_WARN_CODE_BASE                  (IVI_SPECIFIC_WARN_BASE + 0L)

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

#include "niFgenObsolete.h"

#endif /* __NIFGEN_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niFgenObsolete.h sha256=48ff6a12c16ad03892e5ebd022a9696eaf8f9138fcce5f200bf3b4e7ca7f3194 bytes=10440 -->
## FILE: imports/include/niFgenObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niFgenObsolete.h`
- sha256: `48ff6a12c16ad03892e5ebd022a9696eaf8f9138fcce5f200bf3b4e7ca7f3194`
- bytes: 10440

````c
/****************************************************************************
 *    NI-FGEN Instrument Driver for National Instruments Signal Generators
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 1998-2017.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niFgenObsolete.h
 * Purpose:  NI-FGEN Instrument Driver for National Instruments Signal Generators
 *           Obsolete functions and attributes declarations.
 *
 ****************************************************************************/

#ifndef __NIFGENOBSOLETE_HEADER
#define __NIFGENOBSOLETE_HEADER

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

#define IVI_DO_NOT_INCLUDE_VISA_HEADERS
#include <ivi.h>
#undef IVI_DO_NOT_INCLUDE_VISA_HEADERS

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/*  Compatibility with older versions ------*/

/*-  Deprecated Attributes and Values --------*/
//
// Obsoleted prior to NI-FGEN 2.4
//
#define NIFGEN_ATTR_SPECIFIC_PREFIX                         IVI_ATTR_SPECIFIC_DRIVER_PREFIX              /* ViString, Read-only */
#define NIFGEN_ATTR_DRIVER_MAJOR_VERSION                    IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION       /* ViInt32, Read-only */
#define NIFGEN_ATTR_DRIVER_MINOR_VERSION                    IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION       /* ViInt32, Read-only */
#define NIFGEN_ATTR_DRIVER_REVISION                         IVI_ATTR_SPECIFIC_DRIVER_REVISION            /* ViString, Read-only */
#define NIFGEN_ATTR_ENGINE_MAJOR_VERSION                    IVI_ATTR_ENGINE_MAJOR_VERSION                /* ViInt32, Read-only */
#define NIFGEN_ATTR_ENGINE_MINOR_VERSION                    IVI_ATTR_ENGINE_MINOR_VERSION                /* ViInt32, Read-only */
#define NIFGEN_ATTR_ENGINE_REVISION                         IVI_ATTR_ENGINE_REVISION                     /* ViString, Read-only */
#define NIFGEN_ATTR_VISA_RM_SESSION                         IVI_ATTR_VISA_RM_SESSION                     /* ViSession, Read-only */
#define NIFGEN_ATTR_IO_SESSION                              IVI_ATTR_IO_SESSION                          /* ViSession, Read-only */
#define NIFGEN_ATTR_DEFER_UPDATE                            IVI_ATTR_DEFER_UPDATE                        /* ViBoolean */
#define NIFGEN_ATTR_RETURN_DEFERRED_VALUES                  IVI_ATTR_RETURN_DEFERRED_VALUES              /* ViBoolean */
#define NIFGEN_ATTR_PRIMARY_ERROR                           IVI_ATTR_PRIMARY_ERROR                       /* ViInt32   */
#define NIFGEN_ATTR_SECONDARY_ERROR                         IVI_ATTR_SECONDARY_ERROR                     /* ViInt32   */
#define NIFGEN_ATTR_ERROR_ELABORATION                       IVI_ATTR_ERROR_ELABORATION                   /* ViString  */
#define NIFGEN_ATTR_CYCLE_COUNT                             IVIFGEN_ATTR_BURST_COUNT                     /* ViInt32, multi-channel */
#define NIFGEN_VAL_TTL7                                     IVIFGEN_VAL_TTL7
#define NIFGEN_VAL_RTSI_CLOCK                               IVIFGEN_VAL_REF_CLOCK_RTSI_CLOCK
#define NIFGEN_ATTR_NUM_CHANNELS                            IVI_ATTR_NUM_CHANNELS                        /* ViInt32,  Read-only */
#define NIFGEN_ATTR_QUERY_INSTR_STATUS                      IVI_ATTR_QUERY_INSTR_STATUS                  /* ViBoolean */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION           IVI_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION       /* ViInt32  */
#define NIFGEN_ATTR_SPECIFIC_DRIVER_MINOR_VERSION           IVI_ATTR_SPECIFIC_DRIVER_MINOR_VERSION       /* ViInt32  */
#define NIFGEN_VAL_SW_TRIG_FUNC                             IVIFGEN_VAL_SOFTWARE_TRIG
#define NIFGEN_ATTR_OSP_DATA_RATE                           NIFGEN_ATTR_OSP_IQ_RATE                      /* ViReal64 */

//
// Obsoleted in NI-FGEN 2.4
//
/*- Defined values for attribute NIFGEN_ATTR_TRIGGER_SOURCE ------------*/
#define NIFGEN_VAL_IMMEDIATE                    0L
#define NIFGEN_VAL_EXTERNAL                     IVIFGEN_VAL_EXTERNAL
#define NIFGEN_VAL_SOFTWARE_TRIG                IVIFGEN_VAL_SOFTWARE_TRIG
#define NIFGEN_VAL_PXI_STAR                     IVIFGEN_VAL_PXI_STAR
#define NIFGEN_VAL_RTSI_0                       IVIFGEN_VAL_RTSI_0
#define NIFGEN_VAL_RTSI_1                       IVIFGEN_VAL_RTSI_1
#define NIFGEN_VAL_RTSI_2                       IVIFGEN_VAL_RTSI_2
#define NIFGEN_VAL_RTSI_3                       IVIFGEN_VAL_RTSI_3
#define NIFGEN_VAL_RTSI_4                       IVIFGEN_VAL_RTSI_4
#define NIFGEN_VAL_RTSI_5                       IVIFGEN_VAL_RTSI_5
#define NIFGEN_VAL_RTSI_6                       IVIFGEN_VAL_RTSI_6
#define NIFGEN_VAL_TTL0                         IVIFGEN_VAL_TTL0
#define NIFGEN_VAL_TTL1                         IVIFGEN_VAL_TTL1
#define NIFGEN_VAL_TTL2                         IVIFGEN_VAL_TTL2
#define NIFGEN_VAL_TTL3                         IVIFGEN_VAL_TTL3
#define NIFGEN_VAL_TTL4                         IVIFGEN_VAL_TTL4
#define NIFGEN_VAL_TTL5                         IVIFGEN_VAL_TTL5
#define NIFGEN_VAL_TTL6                         IVIFGEN_VAL_TTL6

/*- Defined values for attribute NIFGEN_ATTR_UPDATE_CLOCK_SOURCE ------------*/
#define NIFGEN_VAL_INTERNAL                     (0L)
/*NIFGEN_VAL_EXTERNAL*/

/*- Defined values for signal routing ----------------------------------*/
#define NIFGEN_VAL_PLL_REF_SOURCE               (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 3L)
#define NIFGEN_VAL_PFI_1                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 12L)
#define NIFGEN_VAL_PFI_2                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 13L)
#define NIFGEN_VAL_PFI_3                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 14L)
#define NIFGEN_VAL_PFI_4                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 15L)
#define NIFGEN_VAL_PFI_5                        (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 16L)
#define NIFGEN_VAL_UPDATE_CLOCK                 (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 17L)
#define NIFGEN_VAL_OTHER_TERMINAL               (IVIFGEN_VAL_TRIG_SRC_SPECIFIC_EXT_BASE + 18L)

/*- Defined values for attribute NIFGEN_ATTR_REF_CLOCK_SOURCE ----------*/
#define NIFGEN_VAL_REF_CLOCK_INTERNAL           IVIFGEN_VAL_REF_CLOCK_INTERNAL
#define NIFGEN_VAL_REF_CLOCK_EXTERNAL           IVIFGEN_VAL_REF_CLOCK_EXTERNAL
#define NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK         IVIFGEN_VAL_REF_CLOCK_RTSI_CLOCK
#define NIFGEN_VAL_REF_CLOCK_TTL7               IVIFGEN_VAL_TTL7
#define NIFGEN_VAL_REF_IN                       (NIFGEN_VAL_CLK_SRC_BASE + 0L)
#define NIFGEN_VAL_PXI_CLK10                    (NIFGEN_VAL_CLK_SRC_BASE + 1L)
#define NIFGEN_VAL_CLK_IN                       (NIFGEN_VAL_CLK_SRC_BASE + 2L)
#define NIFGEN_VAL_DDC_CLK_IN                   (NIFGEN_VAL_CLK_SRC_BASE + 3L)

/*- Attributes ---------------------*/
#define NIFGEN_ATTR_UPDATE_CLOCK_SOURCE    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 106L) /* ViInt32 */
#define NIFGEN_ATTR_REF_CLOCK_SOURCE        IVIFGEN_ATTR_REF_CLOCK_SOURCE         /* ViInt32 */

//
// Obsoleted in NI-FGEN 2.6.1
//
#define NIFGEN_ATTR_OPERATION_MODE           IVIFGEN_ATTR_OPERATION_MODE            /* ViInt32 */
#define NIFGEN_ATTR_ACTUAL_ARB_SAMPLE_RATE  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 109L) /* ViReal64, read-only */
#define NIFGEN_ATTR_DAQMX_TASK              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 221L) /* ViInt32 */

/*-  Deprecated Types --------------*/

//
// Obsoleted in NI-FGEN 2.4
//
#ifndef NIFGEN_NICOMPLEXNUMBER_TYPE_UNDEFINED
   typedef NIComplexNumber niFgen_ComplexF64;
#endif



/*-  Deprecated Functions ----------*/

//
// Obsoleted in NI-FGEN 2.0
//
ViStatus _VI_FUNC niFgen_IviInit(
   ViChar instrName[],
   ViBoolean IDQuery,
   ViBoolean resetDevice,
   ViSession vi);

ViStatus _VI_FUNC niFgen_IviClose(
   ViSession vi);

ViStatus _VI_FUNC niFgen_GetErrorInfo(
   ViSession vi,
   ViStatus *primaryError,
   ViStatus *secondaryError,
   ViChar errorElaboration[IVI_MAX_MESSAGE_BUF_SIZE]);

ViStatus _VI_FUNC niFgen_ClearErrorInfo(
   ViSession vi);

ViStatus _VI_FUNC niFgen_EnableOutput(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC niFgen_DisableOutput(
   ViSession vi,
   ViConstString channelName);

ViStatus _VI_FUNC  niFgen_ConfigureTrigger(
   ViSession vi,
   ViConstString channelName,
   ViInt32 trigSource,
   ViInt32 cycleCount);

ViStatus _VI_FUNC  niFgen_SendSWTrigger(
   ViSession vi);


//
// Obsoleted in NI-FGEN 2.2
//

// use niFgen_CreateWaveformF64 instead
ViStatus _VI_FUNC  niFgen_CreateArbWaveform(
   ViSession vi,
   ViInt32 wfmSize,
   ViReal64 wfmData[],
   ViInt32 *wfmHandle);

// use niFgen_CreateWaveformI16 instead
ViStatus _VI_FUNC  niFgen_CreateBinary16ArbWaveform(
   ViSession vi,
   ViInt32 wfmSize,
   ViInt16 wfmData[],
   ViInt32 *wfmHandle);

//
// Obsoleted in NI-FGEN 2.3
//

// use niFgen_SetAttributeViReal64 with attribute NIFGEN_ATTR_ARB_GAIN instead
ViStatus _VI_FUNC  niFgen_ConfigureGain(
   ViSession vi,
   ViConstString channelName,
   ViReal64 Gain);

//
// Obsoleted in NI-FGEN 2.4
//

// use niFgen_ConfigureReferenceClock instead
ViStatus _VI_FUNC niFgen_ConfigureRefClockSource(
   ViSession vi,
   ViInt32 referenceClockSource);

// use niFgen_ConfigureReferenceClock instead
ViStatus _VI_FUNC niFgen_ConfigureRefClockFrequency(
   ViSession vi,
   ViReal64 frequency);

// use niFgen_ConfigureSampleClockSource instead
ViStatus _VI_FUNC niFgen_ConfigureUpdateClockSource(
   ViSession vi,
   ViInt32 source);

// use niFgen_SendSoftwareEdgeTrigger instead
ViStatus _VI_FUNC niFgen_SendSoftwareTrigger(
   ViSession vi);

// use the configure trigger specific to the trigger instead
ViStatus _VI_FUNC  niFgen_ConfigureTriggerSource(
   ViSession vi,
   ViConstString channelName,
   ViInt32 trigSource);

//
// Obsoleted in NI-FGEN 2.7
//

ViStatus _VI_FUNC niFgen_CalAdjustCalADC(
   ViSession vi,
   ViReal64* voltagesMeasuredExternally,
   ViReal64* voltagesMeasuredWithCalADC);

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* __NIFGENOBSOLETE_HEADER */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/NiFpga.h sha256=7dc4f86076e53bb0774e4cf8ffabee78d692ccf4a3e0be0900e88436289b253b bytes=174061 -->
## FILE: imports/include/NiFpga.h

- repository: `ni/grpc-device`
- source_path: `imports/include/NiFpga.h`
- sha256: `7dc4f86076e53bb0774e4cf8ffabee78d692ccf4a3e0be0900e88436289b253b`
- bytes: 174061

````c
/*
 * FPGA Interface C API 24.3 header file.
 *
 * Copyright (c) 2024,
 * National Instruments Corporation.
 * All rights reserved.
 */


#ifndef __NiFpga_h__
#define __NiFpga_h__

/*
 * Determine platform details.
 */
#if defined(_M_IX86) \
 || defined(_M_X64) \
 || defined(_M_AMD64) \
 || defined(i386) \
 || defined(__i386) \
 || defined(__i386__) \
 || defined(__i486__) \
 || defined(__i586__) \
 || defined(__i686__) \
 || defined(__amd64__) \
 || defined(__amd64) \
 || defined(__x86_64__) \
 || defined(__x86_64) \
 || defined(__IA32__) \
 || defined(_X86_) \
 || defined(__THW_INTEL__) \
 || defined(__I86__) \
 || defined(__INTEL__) \
 || defined(__X86__) \
 || defined(__386__) \
 || defined(__I86__) \
 || defined(M_I386) \
 || defined(M_I86) \
 || defined(_M_I386) \
 || defined(_M_I86)
   #if defined(_WIN32) \
    || defined(_WIN64) \
    || defined(__WIN32__) \
    || defined(__TOS_WIN__) \
    || defined(__WINDOWS__) \
    || defined(_WINDOWS) \
    || defined(__WINDOWS_386__) \
    || defined(__CYGWIN__)
      /* Either Windows or Phar Lap ETS. */
      #define NiFpga_Windows 1
   #elif defined(__linux__) \
      || defined(__linux) \
      || defined(linux) \
      || defined(__gnu_linux__)
      #define NiFpga_Linux 1
   #elif defined(__APPLE__) && defined(__MACH__)
      #define NiFpga_MacOsX 1
   #else
      #error Unsupported OS.
   #endif
#elif defined(__powerpc) \
   || defined(__powerpc__) \
   || defined(__POWERPC__) \
   || defined(__ppc__) \
   || defined(__PPC) \
   || defined(_M_PPC) \
   || defined(_ARCH_PPC) \
   || defined(__PPC__) \
   || defined(__ppc)
   #if defined(__vxworks)
      #define NiFpga_VxWorks 1
      #error VxWorks is no longer supported by the FPGA Interface C API
   #else
      #error Unsupported OS.
   #endif
#elif defined(__arm__) \
   || defined(__thumb__) \
   || defined(__TARGET_ARCH_ARM) \
   || defined(__TARGET_ARCH_THUMB) \
   || defined(_ARM) \
   || defined(_M_ARM) \
   || defined(_M_ARMT)
#if defined(__linux__) \
 || defined(__linux) \
 || defined(linux) \
 || defined(__gnu_linux__)
   #define NiFpga_Linux 1
#else
      #error Unsupported OS.
   #endif
#else
   #error Unsupported architecture.
#endif

/*
 * Determine compiler.
 */
#if defined(_MSC_VER)
   #define NiFpga_Msvc 1
#elif defined(__GNUC__)
   #define NiFpga_Gcc 1
#elif defined(_CVI_) && !defined(_TPC_)
   #define NiFpga_Cvi 1
   /* Enables CVI Library Protection Errors. */
   #pragma EnableLibraryRuntimeChecking
#else
   /* Unknown compiler. */
#endif

/*
 * Determine compliance with different C/C++ language standards.
 */
#if defined(__cplusplus)
   #define NiFpga_Cpp 1
   #if __cplusplus >= 199707L
      #define NiFpga_Cpp98 1
      #if __cplusplus >= 201103L
         #define NiFpga_Cpp11 1
      #endif
   #endif
#endif
#if defined(__STDC__)
   #define NiFpga_C89 1
   #if defined(__STDC_VERSION__)
      #define NiFpga_C90 1
      #if __STDC_VERSION__ >= 199409L
         #define NiFpga_C94 1
         #if __STDC_VERSION__ >= 199901L
            #define NiFpga_C99 1
            #if __STDC_VERSION__ >= 201112L
               #define NiFpga_C11 1
            #endif
         #endif
      #endif
   #endif
#endif

/*
 * Determine ability to inline functions.
 */
#if NiFpga_Cpp || NiFpga_C99
   /* The inline keyword exists in C++ and C99. */
   #define NiFpga_Inline inline
#elif NiFpga_Msvc
   /* Visual C++ (at least since 6.0) also supports an alternate keyword. */
   #define NiFpga_Inline __inline
#elif NiFpga_Gcc
   /* GCC (at least since 2.95.2) also supports an alternate keyword. */
   #define NiFpga_Inline __inline__
#elif !defined(NiFpga_Inline)
   /*
    * Disable inlining if inline support is unknown. To manually enable
    * inlining, #define the following macro before #including NiFpga.h:
    *
    *    #define NiFpga_Inline inline
    */
   #define NiFpga_Inline
#endif

/*
 * Define exact-width integer types, if they have not already been defined.
 */
#if NiFpga_ExactWidthIntegerTypesDefined \
 || defined(_STDINT) \
 || defined(_STDINT_H) \
 || defined(_STDINT_H_) \
 || defined(_INTTYPES_H) \
 || defined(_INTTYPES_H_) \
 || defined(_SYS_STDINT_H) \
 || defined(_SYS_STDINT_H_) \
 || defined(_SYS_INTTYPES_H) \
 || defined(_SYS_INTTYPES_H_) \
 || defined(_STDINT_H_INCLUDED) \
 || defined(_MSC_STDINT_H_) \
 || defined(_PSTDINT_H_INCLUDED)
   /* Assume that exact-width integer types have already been defined. */
#elif NiFpga_C99 \
   || NiFpga_Gcc /* GCC (at least since 3.0) has a stdint.h. */ \
   || defined(HAVE_STDINT_H)
   /* Assume that stdint.h can be included. */
   #include <stdint.h>
#elif NiFpga_Msvc \
   || NiFpga_Cvi
   /* Manually define exact-width integer types. */
   typedef   signed    char  int8_t;
   typedef unsigned    char uint8_t;
   typedef            short  int16_t;
   typedef unsigned   short uint16_t;
   typedef              int  int32_t;
   typedef unsigned     int uint32_t;
   typedef          __int64  int64_t;
   typedef unsigned __int64 uint64_t;
#else
   /*
    * Exact-width integer types must be defined by the user, and the following
    * macro must be #defined, before #including NiFpga.h:
    *
    *    #define NiFpga_ExactWidthIntegerTypesDefined 1
    */
   #error Exact-width integer types must be defined by the user. See comment.
#endif

/* Included for definition of size_t. */
#include <stddef.h>
/* Included for definition of FLT_MAX and DBL_MAX */
#include <float.h>
/* Included for definition of ldexp and ldexpf */
#include <math.h>

#if NiFpga_Cpp
extern "C"
{
#endif

/**
 * A boolean value; either NiFpga_False or NiFpga_True.
 */
typedef uint8_t NiFpga_Bool;

/**
 * Represents a false condition.
 */
static const NiFpga_Bool NiFpga_False = 0;

/**
 * Represents a true condition.
 */
static const NiFpga_Bool NiFpga_True = 1;

/** \addtogroup Status
 *  @{
 */

/**
 * Represents the resulting status of a function call through its return value.
 * 0 is success, negative values are errors, and positive values are warnings.
 */
typedef int32_t NiFpga_Status;

/**
 * No errors or warnings.
 */
static const NiFpga_Status NiFpga_Status_Success = 0;

/**
 * The timeout expired before the FIFO operation could complete.
 */
static const NiFpga_Status NiFpga_Status_FifoTimeout = -50400;

/**
 * No transfer is in progress because the transfer was aborted by the client.
 * The operation could not be completed as specified.
 */
static const NiFpga_Status NiFpga_Status_TransferAborted = -50405;

/**
 * A memory allocation failed. Try again after rebooting.
 */
static const NiFpga_Status NiFpga_Status_MemoryFull = -52000;

/**
 * An unexpected software error occurred.
 */
static const NiFpga_Status NiFpga_Status_SoftwareFault = -52003;

/**
 * A parameter to a function was not valid. This could be a NULL pointer, a bad
 * value, etc.
 */
static const NiFpga_Status NiFpga_Status_InvalidParameter = -52005;

/**
 * A required resource was not found. The NiFpga.* library, the RIO resource, or
 * some other resource may be missing.
 */
static const NiFpga_Status NiFpga_Status_ResourceNotFound = -52006;

/**
 * A required resource was not properly initialized. This could occur if
 * NiFpga_Initialize was not called or a required NiFpga_IrqContext was not
 * reserved.
 */
static const NiFpga_Status NiFpga_Status_ResourceNotInitialized = -52010;

/**
 * The FPGA is already running.
 */
static const NiFpga_Status NiFpga_Status_FpgaAlreadyRunning = -61003;

/**
 * An error occurred downloading the VI to the FPGA device. Verify that
 * the target is connected and powered and that the resource of the target
 * is properly configured.
 */
static const NiFpga_Status NiFpga_Status_DownloadError = -61018;

/**
 * The bitfile was not compiled for the specified resource's device type.
 */
static const NiFpga_Status NiFpga_Status_DeviceTypeMismatch = -61024;

/**
 * An error was detected in the communication between the host computer and the
 * FPGA target.
 */
static const NiFpga_Status NiFpga_Status_CommunicationTimeout = -61046;

/**
 * The timeout expired before any of the IRQs were asserted.
 */
static const NiFpga_Status NiFpga_Status_IrqTimeout = -61060;

/**
 * The specified bitfile is invalid or corrupt.
 */
static const NiFpga_Status NiFpga_Status_CorruptBitfile = -61070;

/**
 * The requested FIFO depth is invalid. It is either 0 or an amount not
 * supported by the hardware.
 */
static const NiFpga_Status NiFpga_Status_BadDepth = -61072;

/**
 * The number of FIFO elements is invalid. Either the number is greater than the
 * depth of the host memory DMA FIFO, or more elements were requested for
 * release than had been acquired.
 */
static const NiFpga_Status NiFpga_Status_BadReadWriteCount = -61073;

/**
 * A hardware clocking error occurred. A derived clock lost lock with its base
 * clock during the execution of the LabVIEW FPGA VI. If any base clocks with
 * derived clocks are referencing an external source, make sure that the
 * external source is connected and within the supported frequency, jitter,
 * accuracy, duty cycle, and voltage specifications. Also verify that the
 * characteristics of the base clock match the configuration specified in the
 * FPGA Base Clock Properties. If all base clocks with derived clocks are
 * generated from free-running, on-board sources, please contact National
 * Instruments technical support at ni.com/support.
 */
static const NiFpga_Status NiFpga_Status_ClockLostLock = -61083;

/**
 * The operation could not be performed because the FPGA is busy. Stop all
 * activities on the FPGA before requesting this operation. If the target is in
 * Scan Interface programming mode, put it in FPGA Interface programming mode.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusy = -61141;

/**
 * The operation could not be performed because the FPGA is busy operating in
 * FPGA Interface C API mode. Stop all activities on the FPGA before requesting
 * this operation.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyFpgaInterfaceCApi = -61200;

/**
 * The chassis is in Scan Interface programming mode. In order to run FPGA VIs,
 * you must go to the chassis properties page, select FPGA programming mode, and
 * deploy settings.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyScanInterface = -61201;

/**
 * The operation could not be performed because the FPGA is busy operating in
 * FPGA Interface mode. Stop all activities on the FPGA before requesting this
 * operation.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyFpgaInterface = -61202;

/**
 * The operation could not be performed because the FPGA is busy operating in
 * Interactive mode. Stop all activities on the FPGA before requesting this
 * operation.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyInteractive = -61203;

/**
 * The operation could not be performed because the FPGA is busy operating in
 * Emulation mode. Stop all activities on the FPGA before requesting this
 * operation.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyEmulation = -61204;

/**
 * LabVIEW FPGA does not support the Reset method for bitfiles that allow
 * removal of implicit enable signals in single-cycle Timed Loops.
 */
static const NiFpga_Status NiFpga_Status_ResetCalledWithImplicitEnableRemoval = -61211;

/**
 * LabVIEW FPGA does not support the Abort method for bitfiles that allow
 * removal of implicit enable signals in single-cycle Timed Loops.
 */
static const NiFpga_Status NiFpga_Status_AbortCalledWithImplicitEnableRemoval = -61212;

/**
 * LabVIEW FPGA does not support Close and Reset if Last Reference for bitfiles
 * that allow removal of implicit enable signals in single-cycle Timed Loops.
 * Pass the NiFpga_CloseAttribute_NoResetIfLastSession attribute to NiFpga_Close
 * instead of 0.
 */
static const NiFpga_Status NiFpga_Status_CloseAndResetCalledWithImplicitEnableRemoval = -61213;

/**
 * For bitfiles that allow removal of implicit enable signals in single-cycle
 * Timed Loops, LabVIEW FPGA does not support this method prior to running the
 * bitfile.1. NiFpga_IsError
2. NiFpga_IsNotError
3. NiFpga_MergeStatus
4. NiFpga_CalculateFxpDeltaFloat
5. NiFpga_ConvertFromFxpToFloat
6. NiFpga_CalculateFxpDeltaDouble
7. NiFpga_ConvertFromFxpToDouble
8. NiFpga_ConvertFromFloatToFxp
9. NiFpga_ConvertFromDoubleToFxp1. NiFpga_IsError
2. NiFpga_IsNotError
3. NiFpga_MergeStatus
4. NiFpga_CalculateFxpDeltaFloat
5. NiFpga_ConvertFromFxpToFloat
6. NiFpga_CalculateFxpDeltaDouble
7. NiFpga_ConvertFromFxpToDouble
8. NiFpga_ConvertFromFloatToFxp
9. NiFpga_ConvertFromDoubleToFxp
 */
static const NiFpga_Status NiFpga_Status_ImplicitEnableRemovalButNotYetRun = -61214;

/**
 * Bitfiles that allow removal of implicit enable signals in single-cycle Timed
 * Loops can run only once. Download the bitfile again before re-running the VI.
 */
static const NiFpga_Status NiFpga_Status_RunAfterStoppedCalledWithImplicitEnableRemoval = -61215;

/**
 * A gated clock has violated the handshaking protocol. If you are using
 * external gated clocks, ensure that they follow the required clock gating
 * protocol. If you are generating your clocks internally, please contact
 * National Instruments Technical Support.
 */
static const NiFpga_Status NiFpga_Status_GatedClockHandshakingViolation = -61216;

/**
 * The number of elements requested must be less than or equal to the number of
 * unacquired elements left in the host memory DMA FIFO. There are currently
 * fewer unacquired elements left in the FIFO than are being requested. Release
 * some acquired elements before acquiring more elements.
 */
static const NiFpga_Status NiFpga_Status_ElementsNotPermissibleToBeAcquired = -61219;

/**
 * The operation could not be performed because the FPGA is in configuration or
 * discovery mode. Wait for configuration or discovery to complete and retry
 * your operation.
 */
static const NiFpga_Status NiFpga_Status_FpgaBusyConfiguration = -61252;

/**
 * LabVIEW FPGA does not support Close and Reset if Last Reference for bitfiles
 * that do not support Reset. Pass the
 * NiFpga_CloseAttribute_NoResetIfLastSession attribute to NiFpga_Close instead
 * of 0.
 */
static const NiFpga_Status NiFpga_Status_CloseAndResetCalledWithResetNotSupported = -61253;

/**
 * An unexpected internal error occurred.
 */
static const NiFpga_Status NiFpga_Status_InternalError = -61499;

/**
 * DMA from host to FPGA target is not supported for this remote system. Use
 * another method for I/O or change the controller associated with the FPGA
 * target.
 */
static const NiFpga_Status NiFpga_Status_DmaOutputNotSupported = -63001;

/**
 * The specified DMA FIFO depth is greater than the maximum size supported by
 * this system.
 */
static const NiFpga_Status NiFpga_Status_DmaFifoDepthNotSupported = -63002;

/**
 * The NI-RIO driver was unable to allocate memory for a FIFO. This can happen
 * when the combined depth of all DMA FIFOs exceeds the maximum depth for the
 * controller, or when the controller runs out of system memory. You may be able
 * to reconfigure the controller with a greater maximum FIFO depth. For more
 * information, refer to the NI KnowledgeBase article 65OF2ERQ.
 */
static const NiFpga_Status NiFpga_Status_TotalDmaFifoDepthExceeded = -63003;

/**
 * Operation failed due to device reconfiguration. Multiple sessions to FPGA
 * devices are not supported. Close the other session and retry this operation.
 */
static const NiFpga_Status NiFpga_Status_DeviceReconfigured = -63030;

/**
 * The operation could not be completed because another session is accessing the
 * device. Close all other sessions and retry.
 */
static const NiFpga_Status NiFpga_Status_DeviceInvariant = -63031;

/**
 * Access to the remote system was denied. If you are trying to connect to an RT
 * target, use MAX to check the Remote Device Access settings under
 * Software>>[Recommended software set, such as "NI CompactRIO version -
 * date"]>>NI-RIO>>NI-RIO Settings on the remote system. If you are trying to
 * connect to a desktop Linux target, check the settings in
 * /etc/natinst/nirio/nirio.ini on the Linux target.
 */
static const NiFpga_Status NiFpga_Status_AccessDenied = -63033;

/**
 * The attempt to open a RIO session failed because the driver was not yet
 * initialized.
 */
static const NiFpga_Status NiFpga_Status_DriverNotInitialized = -63035;

/**
 * The operation could not be completed because the device being accessed was
 * unavailable, either because it was disconnected from the network or because
 * power was removed (e.g., the system went into a low-power state). Close any
 * RIO FPGA sessions; check network, USB, and power connections; power-cycle the
 * device if necessary; and open a new RIO session.
 */
static const NiFpga_Status NiFpga_Status_ResourceRemoved = -63036;

/**
 * The NI-RIO software on the host is not compatible with the software on the
 * target. Upgrade the NI-RIO software on the host in order to connect to this
 * target.
 */
static const NiFpga_Status NiFpga_Status_HostVersionMismatch = -63038;

/**
 * A connection could not be established to the specified remote device. Ensure
 * that the device is on and accessible over the network, that the device is not
 * in safe mode, that NI-RIO software is installed, and that the RIO server is
 * running and properly configured.  Refer to Software>>NI-RIO>>NI-RIO Settings
 * under the system in MAX.
 */
static const NiFpga_Status NiFpga_Status_RpcConnectionError = -63040;

/**
 * The connection to the remote device has been lost due to an error on the
 * remote device. Retry the operation. If the remote device continues to report
 * this error, check its power supply and look for diagnostic messages on the
 * console.
 */
static const NiFpga_Status NiFpga_Status_RpcServerError = -63041;

/**
 * A fault on the network caused the operation to fail.
 */
static const NiFpga_Status NiFpga_Status_NetworkFault = -63042;

/**
 * The session is invalid. The target may have been reset or rebooted, or the
 * network connection may have timed out because of processor overuse. Check the
 * network connection, reduce the demand on the processor, and decrease the
 * timeout of the operation that failed. If the problem persists, visit
 * ni.com/info and enter the Info Code expd6p.
 */
static const NiFpga_Status NiFpga_Status_RpcSessionError = -63043;

/**
 * The RIO server could not be found on the specified remote device. Ensure that
 * NI-RIO software is installed and that the RIO server is running and properly
 * configured.  Refer to Software>>NI-RIO>>NI-RIO Settings under the system in
 * MAX.
 */
static const NiFpga_Status NiFpga_Status_RpcServerMissing = -63044;

/**
 * The requested feature is not supported when using a remote RIO session.
 * Opening a remote RIO session occurs when the resource string is specified as
 * rio://hostname/device_name.  A local session can be opened by specifying just
 * the device_name.
 */
static const NiFpga_Status NiFpga_Status_FeatureNotSupportedOverRpc = -63045;

/**
 * The specified trigger line is already reserved. Consult the MAX Trigger
 * settings or the trigger reservations for each device within the system.
 */
static const NiFpga_Status NiFpga_Status_TriggerReserved = -63050;

/**
 * The specified trigger line is not reserved in the current session.
 */
static const NiFpga_Status NiFpga_Status_TriggerNotReserved = -63051;

/**
 * Trigger lines are not supported or enabled. For PXI, identify the controller
 * and chassis using MAX.
 */
static const NiFpga_Status NiFpga_Status_TriggerNotSupported = -63052;

/**
 * The specified event type is invalid.
 */
static const NiFpga_Status NiFpga_Status_EventInvalid = -63070;

/**
 * The specified RIO event has already been enabled for this session.
 */
static const NiFpga_Status NiFpga_Status_EventEnabled = -63071;

/**
 * The specified RIO event has not been enabled for this session. Attempting a
 * Wait on IRQ after an Abort causes this error.
 */
static const NiFpga_Status NiFpga_Status_EventNotEnabled = -63072;

/**
 * The specified event did not occur within the specified time period, in
 * milliseconds. Extend the time period, or ignore if the result was expected.
 */
static const NiFpga_Status NiFpga_Status_EventTimedOut = -63073;

/**
 * The allocated buffer is too small.
 */
static const NiFpga_Status NiFpga_Status_BufferInvalidSize = -63080;

/**
 * The caller did not allocate a memory buffer.
 */
static const NiFpga_Status NiFpga_Status_BufferNotAllocated = -63081;

/**
 * The operation could not complete because another session is accessing the
 * FIFO. Close the other session and retry.
 */
static const NiFpga_Status NiFpga_Status_FifoReserved = -63082;

/**
 * A Configure FIFO, Stop FIFO, Read FIFO, or Write FIFO function was called
 * while the host had acquired elements of the FIFO. Release all acquired
 * elements before configuring, stopping, reading, or writing.
 */
static const NiFpga_Status NiFpga_Status_FifoElementsCurrentlyAcquired = -63083;

/**
 * A function was called using a misaligned address. The address must be a
 * multiple of the size of the datatype.
 */
static const NiFpga_Status NiFpga_Status_MisalignedAccess = -63084;

/**
 * The FPGA Read/Write Control Function is accessing a control or indicator with
 * data that exceeds the maximum size supported on the current target. Refer to
 * the hardware documentation for the limitations on data types for this target.
 */
static const NiFpga_Status NiFpga_Status_ControlOrIndicatorTooLarge = -63085;

/**
 * The FIFO function called cannot be used while the FIFO is running. To use
 * this function, ensure the FIFO is stopped.
 */
static const NiFpga_Status NiFpga_Status_OperationNotSupportedWhileStarted = -63086;

/**
 * The function called does not match the datatype of the specified property.
 * Ensure you are calling the correct function for the property.
 */
static const NiFpga_Status NiFpga_Status_TypesDoNotMatch = -63087;

/**
 * Cannot acquire more regions from the selected FIFO. Release some regions and
 * try again.
 */
static const NiFpga_Status NiFpga_Status_OutOfFifoRegions = -63088;

/**
 * A valid .lvbitx bitfile is required. If you are using a vaild .lvbitx
 * bitfile, the bitfile may not be compatible with the software you are using.
 * Determine which version of LabVIEW was used to make the bitfile, update your
 * software to that version or later, and try again.
 */
static const NiFpga_Status NiFpga_Status_BitfileReadError = -63101;

/**
 * Invalid output directory.
 */
static const NiFpga_Status NiFpga_Status_InvalidOutputDirectory = -63102;

/**
 * Invalid prefix override. Prefixes must include only alphanumerics and
 * underscores.
 */
static const NiFpga_Status NiFpga_Status_InvalidPrefixOverride = -63103;

/**
 * Could not convert "%s" to a valid C/C++ identifier.
 */
static const NiFpga_Status NiFpga_Status_NoSuitableIdentifier = -63104;

/**
 * The C/C++ identifier "%s" is already in use and could not be created.
 */
static const NiFpga_Status NiFpga_Status_IdentifierConflict = -63105;

/**
 * The specified bitfile is not the bitfile used to generate the C API. Specify
 * the original bitfile or regenerate the C API for this bitfile.
 */
static const NiFpga_Status NiFpga_Status_SignatureMismatch = -63106;

/**
 * The bitfile you are trying to use is incompatible with the version of NI-RIO
 * installed on the target and/or host. Update the version of NI-RIO on the
 * target and/or host to the same version (or later) used to compile the
 * bitfile. Alternatively, recompile the bitfile with the same version of NI-RIO
 * that is currently installed on the target and/or host.
 */
static const NiFpga_Status NiFpga_Status_IncompatibleBitfile = -63107;

/**
 * An unspecified hardware failure has occurred. The operation could not be
 * completed.
 */
static const NiFpga_Status NiFpga_Status_HardwareFault = -63150;

/**
 * You must download the bitfile to the flash memory on the FPGA device before
 * you can set when the bitfile is autoloaded. Download the bitfile to the flash
 * memory then try again.
 */
static const NiFpga_Status NiFpga_Status_NoBitfilePresentOnFlash = -63160;

/**
 * The device has shut down to protect against excessive power consumption.
 * Check airflow and cooling and reboot the system. To avoid this error, monitor
 * the power consumption, power shutdown threshold, and margin of the device. If
 * necessary, reduce FPGA power consumption.
 */
static const NiFpga_Status NiFpga_Status_PowerShutdown = -63170;

/**
 * The device has shut down to protect against excessive FPGA temperature. Check
 * airflow and cooling and reboot the system. To avoid this error, monitor the
 * FPGA temperature, temperature shutdown threshold, and margin of the FPGA. If
 * necessary, reduce FPGA temperature.
 */
static const NiFpga_Status NiFpga_Status_ThermalShutdown = -63171;

/**
 * The alias name is invalid. A valid alias name must meet the following
 * conditions:  1) Cannot be or contain a reserved word. 2) Can use only
 * alphanumeric characters, hyphens, and underscores. 3) Cannot conflict with
 * the default alias of another device. A default alias is the name that the NI-
 * RIO Device Driver assigns to a device based on its attributes if you have not
 * assigned a custom alias to the device using MAX or the System Configuration
 * API. For example, 'PXI1Slot3' is the default alias for the device at Slot 3
 * of PXI Chassis 1, and it cannot be used as an alias name for any other
 * device. Refer to the LabVIEW Help for NI-RIO for more information about
 * aliases.
 */
static const NiFpga_Status NiFpga_Status_InvalidAliasName = -63180;

/**
 * The supplied alias was not found.
 */
static const NiFpga_Status NiFpga_Status_AliasNotFound = -63181;

/**
 * An invalid device access setting was specified. RIO device access patterns
 * may contain only alphanumerics, '-', '_', '.', and '*'.
 */
static const NiFpga_Status NiFpga_Status_InvalidDeviceAccess = -63182;

/**
 * An invalid port was specified. The RIO server port must be between 0 and
 * 65535, where 0 indicates a dynamically assigned port. Port 3580 is reserved
 * and cannot be used.
 */
static const NiFpga_Status NiFpga_Status_InvalidPort = -63183;

/**
 * The selected bitfile requires a driver that could not be loaded or that was
 * invalid. Use MAX to install all necessary software to your target. Note that
 * if your project includes modules under the chassis item, user-defined
 * variables, or references to the Scan Clock Chassis I/O item, you must install
 * NI-RIO IO Scan software to the target.
 */
static const NiFpga_Status NiFpga_Status_ChildDeviceNotInserted = -63184;

/**
 * This remote system does not support connections to other remote systems.
 */
static const NiFpga_Status NiFpga_Status_RemoteTarget = -63187;

/**
 * The operation is no longer supported.
 */
static const NiFpga_Status NiFpga_Status_DeprecatedFunction = -63188;

/**
 * The supplied search pattern is invalid.
 */
static const NiFpga_Status NiFpga_Status_InvalidPattern = -63189;

/**
 * The specified device was not found. Use MAX or System Designer to find the
 * proper resource name for the intended device.
 */
static const NiFpga_Status NiFpga_Status_InvalidResourceName = -63192;

/**
 * The requested feature is not supported.
 */
static const NiFpga_Status NiFpga_Status_FeatureNotSupported = -63193;

/**
 * The NI-RIO software on the target system is not compatible with this
 * software. Upgrade the NI-RIO software on the target system.
 */
static const NiFpga_Status NiFpga_Status_VersionMismatch = -63194;

/**
 * The handle for device communication is invalid or has been closed. Restart
 * the application.
 */
static const NiFpga_Status NiFpga_Status_InvalidSession = -63195;

/**
 * An invalid attribute has been specified.
 */
static const NiFpga_Status NiFpga_Status_InvalidAttribute = -63196;

/**
 * An invalid attribute value has been specified.
 */
static const NiFpga_Status NiFpga_Status_InvalidAttributeValue = -63197;

/**
 * The system has run out of resources. Close a session and retry the operation.
 */
static const NiFpga_Status NiFpga_Status_OutOfHandles = -63198;

/**
 * The session could not be opened because another session with a different
 * bitfile is already open on the device. Close the current session before
 * opening another.
 */
static const NiFpga_Status NiFpga_Status_CannotDownloadDifferentBitfile = -63199;


/**
 * Tests whether a status is an error.
 *
 * @param status status to check for an error
 * @return whether the status was an error
 */
static NiFpga_Inline NiFpga_Bool NiFpga_IsError(const NiFpga_Status status)
{
   return status < NiFpga_Status_Success ? NiFpga_True : NiFpga_False;
}

/**
 * Tests whether a status is not an error. Success and warnings are not errors.
 *
 * @param status status to check for an error
 * @return whether the status was a success or warning
 */
static NiFpga_Inline NiFpga_Bool NiFpga_IsNotError(const NiFpga_Status status)
{
   return status >= NiFpga_Status_Success ? NiFpga_True : NiFpga_False;
}

/**
 * Conditionally sets the status to a new value. The previous status is
 * preserved unless the new status is more of an error, which means that
 * warnings and errors overwrite successes, and errors overwrite warnings. New
 * errors do not overwrite older errors, and new warnings do not overwrite
 * older warnings.
 *
 * @param status status to conditionally set
 * @param newStatus new status value that may be set
 * @return the resulting status
 */
static NiFpga_Inline NiFpga_Status NiFpga_MergeStatus(
                                               NiFpga_Status* const status,
                                               const NiFpga_Status  newStatus)
{
   if (!status)
      return NiFpga_Status_InvalidParameter;
   if (NiFpga_IsNotError(*status)
   &&  (*status == NiFpga_Status_Success || NiFpga_IsError(newStatus)))
      *status = newStatus;
   return *status;
}

/**
 * This macro evaluates the expression only if the status is not an error. The
 * expression must evaluate to an NiFpga_Status, such as a call to any NiFpga_*
 * function, because the status will be set to the returned status if the
 * expression is evaluated.
 *
 * You can use this macro to mimic status chaining in LabVIEW, where the status
 * does not have to be explicitly checked after each call. Such code may look
 * like the following example.
 *
 *        NiFpga_Status status = NiFpga_Status_Success;
 *        NiFpga_IfIsNotError(status, NiFpga_WriteU32(...));
 *        NiFpga_IfIsNotError(status, NiFpga_WriteU32(...));
 *        NiFpga_IfIsNotError(status, NiFpga_WriteU32(...));
 *
 * @param status status to check for an error
 * @param expression expression to call if the incoming status is not an error
 */
#define NiFpga_IfIsNotError(status, expression) \
   if (NiFpga_IsNotError(status)) \
      NiFpga_MergeStatus(&status, (expression)); \

/**
 * @}
 */

/** \addtogroup FXP
 *  @{
 */

/**
 * This struct contains information needed to interpret an FXP Type.
 *   - `isSigned` tells if the type is signed.
 *   - `wordLength` tells us the number of bits used in the type.
 *   - `integerWordLength` is the number of bits to shift the binary point to
 *     reach the most significant bit.
 *
 * More information can be found at the following links:
 * - http://zone.ni.com/reference/en-XX/help/371361J-01/lvconcepts/numeric_data/
 * - http://www.ni.com/newsletter/50303/en/
 * - http://digital.ni.com/public.nsf/allkb/346CC529EC1092B3862574FA0053B9B2
 */
typedef struct NiFpga_FxpTypeInfo
{
   NiFpga_Bool isSigned;
   uint8_t wordLength;
   int16_t integerWordLength;
} NiFpga_FxpTypeInfo;

/**
 * @}
 */

/** \addtogroup FXP
 *  @{
 */

/**
 * Calculates the FXP delta as a float.  The delta is the smallest increment
 * that the FXP number can represent.
 *
 * @warning This function can lose precision.
 *
 * @param typeInfo the information about the FXP type
 * @return delta the delta for the specified FXP type
 */
static NiFpga_Inline float NiFpga_CalculateFxpDeltaFloat(
                                          const NiFpga_FxpTypeInfo typeInfo)
{
   const int32_t exponent = typeInfo.integerWordLength - typeInfo.wordLength;
#if NiFpga_C99 && !NiFpga_Cvi
   return ldexpf(FLT_EPSILON, exponent + FLT_MANT_DIG - 1);
#else
   return (float)ldexp((double)FLT_EPSILON, exponent + FLT_MANT_DIG - 1);
#endif
}

/*
 * Private helper macro for converting from Fxp to float or double.
 * This is not intended for external use and may be changed or modified in
 * future versions.
 */
#define NiFpga_Private_FxpToFloatingPoint(typeInfo, delta, data) \
   const uint64_t wordLengthMask = typeInfo.wordLength != 64 \
      ? (1ULL << typeInfo.wordLength) - 1 : 0xFFFFFFFFFFFFFFFFULL; \
   data &= wordLengthMask; \
   if (typeInfo.isSigned) \
   { \
      const uint64_t signedMask = 1ULL << (typeInfo.wordLength - 1); \
      if (data & signedMask) \
      { \
         int64_t signedData = data ^ wordLengthMask; \
         signedData = (signedData + 1) * -1; \
         return delta * signedData; \
      } \
   } \
   return delta * data;

/**
 * @}
 */

/** \addtogroup FXP
 *  @{
 */

/**
 * Converts from a raw FXP value from the FPGA to a float.
 *
 * @warning This function can lose precision.
 * @warning This function truncates when losing precision rather than rounding.
 *
 * @param typeInfo information about the FXP data provided
 * @param data the raw FXP data from the FPGA
 * @return a float representation of the data
 */
static NiFpga_Inline float NiFpga_ConvertFromFxpToFloat(
                                          const NiFpga_FxpTypeInfo typeInfo,
                                          uint64_t data)
{
   const float delta = NiFpga_CalculateFxpDeltaFloat(typeInfo);
   NiFpga_Private_FxpToFloatingPoint(typeInfo, delta, data)
}

/**
 * @}
 */

/**
 * Calculates the FXP delta as a double.  The delta is the smallest increment
 * that the FXP number can represent.
 *
 * @warning This function can lose precision.
 *
 * @param typeInfo the information about the FXP type
 * @return delta the delta for the specified FXP type
 */
static NiFpga_Inline double NiFpga_CalculateFxpDeltaDouble(
                                          const NiFpga_FxpTypeInfo typeInfo)
{
   const int32_t exponent = typeInfo.integerWordLength - typeInfo.wordLength;
   return ldexp(DBL_EPSILON, exponent + DBL_MANT_DIG - 1);
}

/** \addtogroup FXP
 *  @{
 */

/**
 * Converts from a raw FXP value from the FPGA to a double.
 *
 * @warning This function can lose precision.
 * @warning This function truncates when losing precision rather than rounding.
 *
 * @param typeInfo information about the FXP data provided
 * @param data the raw FXP data from the FPGA
 * @return a double representation of the data
 */
static NiFpga_Inline double NiFpga_ConvertFromFxpToDouble(
                                          const NiFpga_FxpTypeInfo typeInfo,
                                          uint64_t data)
{
   const double delta = NiFpga_CalculateFxpDeltaDouble(typeInfo);
   NiFpga_Private_FxpToFloatingPoint(typeInfo, delta, data)
}

/**
 * @}
 */

/*
 * Private helper macro for converting from float or double to Fxp.
 * This is not intended for external use and may be changed or modified in
 * future versions.
 */
#define NiFpga_Private_FloatingPointToFxp(typeInfo, delta, data) \
   const uint64_t wordLengthMask = typeInfo.wordLength != 64 \
      ? (1ULL << typeInfo.wordLength) - 1 : 0xFFFFFFFFFFFFFFFFULL; \
   if (data < 0) \
   { \
      if (typeInfo.isSigned) \
      { \
         int64_t fxpRepresentation = (int64_t)(data / delta); \
         fxpRepresentation ^= wordLengthMask; \
         fxpRepresentation += 1; \
         fxpRepresentation *= -1; \
         if ((int64_t)(fxpRepresentation & wordLengthMask) == fxpRepresentation) \
         { \
            return fxpRepresentation; \
         } \
         else /* minimum */ \
         { \
            return (-1LL * (1LL << (typeInfo.wordLength - 1))) \
               & wordLengthMask; \
         } \
      } \
      else \
      { \
         return 0; \
      } \
   } \
   else \
   { \
      const uint64_t fxpRepresentation = (uint64_t)(data / delta); \
      if ((fxpRepresentation & wordLengthMask) == fxpRepresentation) \
      { \
         return fxpRepresentation; \
      } \
      else /* maxmimum */ \
      { \
         const uint64_t magnitude = typeInfo.wordLength \
                                    - (typeInfo.isSigned ? 1 : 0); \
         return (1ULL << magnitude) - 1; \
      } \
   }

/** \addtogroup FXP
 *  @{
 */

/**
 * Converts a float into a FXP representation of the specified type.
 *
 * @warning This function can lose precision.
 * @warning This function truncates when losing precision rather than rounding.
 *
 * @param typeInfo information about the FXP data provided
 * @param data the value to be converted to FXP
 * @return a value containing the FXP representation of data
 */
static NiFpga_Inline uint64_t NiFpga_ConvertFromFloatToFxp(
                                          const NiFpga_FxpTypeInfo typeInfo,
                                          float data)
{
   const float delta = NiFpga_CalculateFxpDeltaFloat(typeInfo);
   NiFpga_Private_FloatingPointToFxp(typeInfo, delta, data)
}

/**
 * Converts a double into a FXP representation of the specified type.
 *
 * @warning This function can lose precision.
 * @warning This function truncates when losing precision rather than rounding.
 *
 * @param typeInfo information about the FXP data provided
 * @param data the value to be converted to FXP
 * @return a value containing the FXP representation of data
 */
static NiFpga_Inline uint64_t NiFpga_ConvertFromDoubleToFxp(
                                          const NiFpga_FxpTypeInfo typeInfo,
                                          double data)
{
   const double delta = NiFpga_CalculateFxpDeltaDouble(typeInfo);
   NiFpga_Private_FloatingPointToFxp(typeInfo, delta, data)
}

/**
 * @}
 */

/** \addtogroup Required
 *  @{
 */

/**
 * You must call this function before all other function calls. This function
 * loads the NiFpga library so that all the other functions will work. If this
 * function succeeds, you must call NiFpga_Finalize after all other function
 * calls.
 *
 * @warning This function is not thread safe.
 *
 * @return result of the call
 */
NiFpga_Status NiFpga_Initialize(void);

/**
 * You must call this function after all other function calls if
 * NiFpga_Initialize succeeds. This function unloads the NiFpga library.
 *
 * @warning This function is not thread safe.
 *
 * @return result of the call
 */
NiFpga_Status NiFpga_Finalize(void);

/**
 * @}
 */

/** \addtogroup Session
 *  @{
 */

/**
 * A handle to an FPGA session.
 */
typedef uint32_t NiFpga_Session;

/**
 * Attributes that NiFpga_Open accepts.
 */
typedef enum
{
   /**
    * By default the FPGA VI will start running when Open is called.
    * This attribute will ensure the bitfile is loaded to the FPGA, but does not
    * run the VI.  If the VI is already running on the FPGA, its state will not
    * be changed.
    */
   NiFpga_OpenAttribute_NoRun = 1,
   /**
    * On windows the bitfile path is assumed to be encoded as the current
    * codepage. This attribute will specify that the bitfile path is encoded as
    * UTF-8. This parameter has no effect on Linux systems.
    */
   NiFpga_OpenAttribute_BitfilePathIsUTF8 = 2,
   /**
    * Causes the  bitfile argument passed in to be interpreted as the contents
    * of the lvbitx file rather than a path to an lvbitx file.
    */
   NiFpga_OpenAttribute_BitfileContentsNotPath = 1u << 30,
   /**
    * Skips the check of the signature argument, which otherwise would ensure
    * that users would not accidentally rebuild their bitfile (thereby getting
    * new offsets, etc.) without also regenerating their C API and rebuilding
    * their application with the new constants. This is useful if one is not
    * using the FPGA Interface C API Generator to obtain resource information,
    * such as by calling NiFpga_FindRegister or NiFpga_FindFifo.
    * If using this attribute, pass `NULL` to `signature` instead.
    */
   NiFpga_OpenAttribute_IgnoreSignatureArgument = 1u << 31
} NiFpga_OpenAttribute;

/**
 * Opens a session to the FPGA. This call ensures that the contents of the
 * bitfile are programmed to the FPGA. The FPGA runs unless the
 * NiFpga_OpenAttribute_NoRun attribute is used.
 *
 * Because different operating systems have different default current working
 * directories for applications, you must pass an absolute path for the bitfile
 * parameter. If you pass only the filename instead of an absolute path, the
 * operating system may not be able to locate the bitfile. For example, the
 * default current working directory is C:/ni-rt/system/ for Phar Lap ETS.s.
 * Because the generated *_Bitfile constant is a "#define" to a
 * string literal, you can use C/C++ string-literal concatenation to form an
 * absolute path. For example, if the bitfile is in the root directory of a
 * Phar Lap ETS system, pass the following for the bitfile parameter.
 *
 *    \"C:\\\\\\\\\" NiFpga_MyApplication_Bitfile
 *
 * @param bitfile path to the bitfile
 * @param signature signature of the bitfile
 * @param resource RIO resource string to open ("RIO0" or "rio://mysystem/RIO")
 * @param attribute bitwise OR of any NiFpga_OpenAttributes, or 0
 * @param session outputs the session handle, which must be closed when no
 *                longer needed
 * @return result of the call
 */
NiFpga_Status NiFpga_Open(const char*     bitfile,
                          const char*     signature,
                          const char*     resource,
                          uint32_t        attribute,
                          NiFpga_Session* session);

/**
 * Attributes that NiFpga_Close accepts.
 */
typedef enum
{
   NiFpga_CloseAttribute_NoResetIfLastSession = 1
} NiFpga_CloseAttribute;

/**
 * Closes the session to the FPGA. The FPGA resets unless either another session
 * is still open or you use the NiFpga_CloseAttribute_NoResetIfLastSession
 * attribute.
 *
 * @param session handle to a currently open session
 * @param attribute bitwise OR of any NiFpga_CloseAttributes, or 0
 * @return result of the call
 */
NiFpga_Status NiFpga_Close(NiFpga_Session session,
                           uint32_t       attribute);

/**
 * Returns the signature of the bitfile currently loaded on the FPGA. If the
 * signature size specified is too small, signature size will be filled with
 * the size required and NiFpga_Status_InvalidParameter will be returned.

 * @param session handle to a currently open session
 * @param signature the uint32_t array to fill with the signature value
 * @param signatureSize the number of elements in signature
 * @return result of the call
 */
NiFpga_Status NiFpga_GetBitfileSignature(NiFpga_Session session,
                                         uint32_t* signature,
                                         size_t*   signatureSize);

/**
 * Returns the offset of a control or indicator.  This offset can be used as the
 * control or indicator parameter to a Read/Write or Read/WriteArray call.
 * This intent of this function is to make sharing code that accesses the same
 * interface implemented in different bitfiles easy.
 *
 * @warning Its possible to create a FPGA VI with multiple controls and
 * indicators that have the same name. Attempting to find a control or indicator
 * that shares a name is undefined behavior.
 *
 * @warning You must ensure you use the correct Read/Write call with the correct
 * type for the register you have looked up.
 *
 * @param session handle to a currently open session
 * @param registerName the name of the register to find
 * @param registerOffset outputs the offset of the register
 * @return result of the call
 */
NiFpga_Status NiFpga_FindRegister(NiFpga_Session session,
                                  const char* registerName,
                                  uint32_t* registerOffset);

/**
 * Returns the fifoNumber of a FIFO.  This fifoNumber can be used as the
 * fifo parameter to a Read/WriteFifo or AcquireFifoRead/WriteElements call.
 *
 * @param session handle to a currently open session
 * @param fifoName the name of the FIFO to find
 * @param fifoNumber outputs the number of the FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_FindFifo(NiFpga_Session session,
                              const char* fifoName,
                              uint32_t* fifoNumber);

/**
 * @}
 */

/** \addtogroup Method
 *  @{
 */

/**
 * Attributes that NiFpga_Run accepts.
 */
typedef enum
{
   NiFpga_RunAttribute_WaitUntilDone = 1
} NiFpga_RunAttribute;

/**
 * Runs the FPGA VI on the target. If you use NiFpga_RunAttribute_WaitUntilDone,
 * NiFpga_Run blocks the thread until the FPGA finishes running.
 *
 * @param session handle to a currently open session
 * @param attribute bitwise OR of any NiFpga_RunAttributes, or 0
 * @return result of the call
 */
NiFpga_Status NiFpga_Run(NiFpga_Session session,
                         uint32_t       attribute);

/**
 * Aborts the FPGA VI.
 *
 * @param session handle to a currently open session
 * @return result of the call
 */
NiFpga_Status NiFpga_Abort(NiFpga_Session session);

/**
 * Resets the FPGA VI.
 *
 * @param session handle to a currently open session
 * @return result of the call
 */
NiFpga_Status NiFpga_Reset(NiFpga_Session session);

/**
 * Re-downloads the FPGA bitstream to the target.
 *
 * @param session handle to a currently open session
 * @return result of the call
 */
NiFpga_Status NiFpga_Download(NiFpga_Session session);

/**
 * Possible FPGA VI States that GetFpgaViState will output.
 */
typedef enum
{
   /**
    * The FPGA VI has either been downloaded and not run, or the VI was aborted
    * or reset.
    */
   NiFpga_FpgaViState_NotRunning = 0,
   /**
    * An error has occurred.
    */
   NiFpga_FpgaViState_Invalid = 1,
   /**
    * The FPGA VI is currently executing.
    */
   NiFpga_FpgaViState_Running = 2,
   /**
    * The FPGA VI stopped normally.  This indicates it was not aborted or reset,
    * but instead reached the end of any loops it was executing and ended.
    */
   NiFpga_FpgaViState_NaturallyStopped = 3
} NiFpga_FpgaViState;

/**
 * Get the current state of the FPGA VI on the target.
 *
 * @param session handle to a currently open session
 * @param state the current state specified as NiFpga_FpgaViState
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFpgaViState(NiFpga_Session session,
                                    uint32_t*      state);

/**
 * @}
 */

/** \addtogroup Read
 *  @{
 */

/**
 * Reads a boolean value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadBool(NiFpga_Session session,
                              uint32_t       indicator,
                              NiFpga_Bool*   value);

/**
 * Reads a signed 8-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadI8(NiFpga_Session session,
                            uint32_t       indicator,
                            int8_t*        value);

/**
 * Reads an unsigned 8-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadU8(NiFpga_Session session,
                            uint32_t       indicator,
                            uint8_t*       value);

/**
 * Reads a signed 16-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadI16(NiFpga_Session session,
                             uint32_t       indicator,
                             int16_t*       value);

/**
 * Reads an unsigned 16-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadU16(NiFpga_Session session,
                             uint32_t       indicator,
                             uint16_t*      value);

/**
 * Reads a signed 32-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadI32(NiFpga_Session session,
                             uint32_t       indicator,
                             int32_t*       value);

/**
 * Reads an unsigned 32-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadU32(NiFpga_Session session,
                             uint32_t       indicator,
                             uint32_t*      value);

/**
 * Reads a signed 64-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadI64(NiFpga_Session session,
                             uint32_t       indicator,
                             int64_t*       value);

/**
 * Reads an unsigned 64-bit integer value from a given indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadU64(NiFpga_Session session,
                             uint32_t       indicator,
                             uint64_t*      value);

/**
 * Reads a single-precision floating-point value from a given indicator or
 * control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadSgl(NiFpga_Session session,
                             uint32_t       indicator,
                             float*         value);

/**
 * Reads a double-precision floating-point value from a given indicator or
 * control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadDbl(NiFpga_Session session,
                             uint32_t       indicator,
                             double*        value);

/**
 * Reads a FXP value with a wordlength greater than 32-bits from a given
 * indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param typeInfo typeInfo from the generated FXP type
 * @param value outputs the value that was read
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFxp64(NiFpga_Session     session,
                               uint32_t           indicator,
                               NiFpga_FxpTypeInfo typeInfo,
                               uint64_t*          value);

/**
 * @}
 */

/** \addtogroup Write
 *  @{
 */

/**
 * Writes a boolean value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteBool(NiFpga_Session session,
                               uint32_t       control,
                               NiFpga_Bool    value);

/**
 * Writes a signed 8-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteI8(NiFpga_Session session,
                             uint32_t       control,
                             int8_t         value);

/**
 * Writes an unsigned 8-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteU8(NiFpga_Session session,
                             uint32_t       control,
                             uint8_t        value);

/**
 * Writes a signed 16-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteI16(NiFpga_Session session,
                              uint32_t       control,
                              int16_t        value);

/**
 * Writes an unsigned 16-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteU16(NiFpga_Session session,
                              uint32_t       control,
                              uint16_t       value);

/**
 * Writes a signed 32-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteI32(NiFpga_Session session,
                              uint32_t       control,
                              int32_t        value);

/**
 * Writes an unsigned 32-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteU32(NiFpga_Session session,
                              uint32_t       control,
                              uint32_t       value);

/**
 * Writes a signed 64-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteI64(NiFpga_Session session,
                              uint32_t       control,
                              int64_t        value);

/**
 * Writes an unsigned 64-bit integer value to a given control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteU64(NiFpga_Session session,
                              uint32_t       control,
                              uint64_t       value);

/**
 * Writes a single-precision floating-point value to a given control or
 * indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteSgl(NiFpga_Session session,
                              uint32_t       control,
                              float          value);

/**
 * Writes a double-precision floating-point value to a given control or
 * indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteDbl(NiFpga_Session session,
                              uint32_t       control,
                              double         value);

/**
 * Writes a FXP value with a wordlength greater than 32-bits to a given
 * indicator or control.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param typeInfo typeInfo from the generated FXP type
 * @param value value to write
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFxp64(NiFpga_Session     session,
                                uint32_t           control,
                                NiFpga_FxpTypeInfo typeInfo,
                                uint64_t           value);

/**
 * @}
 */

/** \addtogroup ReadArray
 *  @{
 */

/**
 * Reads an entire array of boolean values from a given array indicator or
 * control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayBool(NiFpga_Session session,
                                   uint32_t       indicator,
                                   NiFpga_Bool*   array,
                                   size_t         size);

/**
 * Reads an entire array of signed 8-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayI8(NiFpga_Session session,
                                 uint32_t       indicator,
                                 int8_t*        array,
                                 size_t         size);

/**
 * Reads an entire array of unsigned 8-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayU8(NiFpga_Session session,
                                 uint32_t       indicator,
                                 uint8_t*       array,
                                 size_t         size);

/**
 * Reads an entire array of signed 16-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayI16(NiFpga_Session session,
                                  uint32_t       indicator,
                                  int16_t*       array,
                                  size_t         size);

/**
 * Reads an entire array of unsigned 16-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayU16(NiFpga_Session session,
                                  uint32_t       indicator,
                                  uint16_t*      array,
                                  size_t         size);

/**
 * Reads an entire array of signed 32-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayI32(NiFpga_Session session,
                                  uint32_t       indicator,
                                  int32_t*       array,
                                  size_t         size);

/**
 * Reads an entire array of unsigned 32-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayU32(NiFpga_Session session,
                                  uint32_t       indicator,
                                  uint32_t*      array,
                                  size_t         size);

/**
 * Reads an entire array of signed 64-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayI64(NiFpga_Session session,
                                  uint32_t       indicator,
                                  int64_t*       array,
                                  size_t         size);

/**
 * Reads an entire array of unsigned 64-bit integer values from a given array
 * indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayU64(NiFpga_Session session,
                                  uint32_t       indicator,
                                  uint64_t*      array,
                                  size_t         size);

/**
 * Reads an entire array of single-precision floating-point values from a
 * given array indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArraySgl(NiFpga_Session session,
                                  uint32_t       indicator,
                                  float*         array,
                                  size_t         size);

/**
 * Reads an entire array of double-precision floating-point values from a
 * given array indicator or control.
 *
 * @warning The size passed must be the exact number of elements in the
 *          indicator or control.
 *
 * @param session handle to a currently open session
 * @param indicator indicator or control from which to read
 * @param array outputs the entire array that was read
 * @param size exact number of elements in the indicator or control
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadArrayDbl(NiFpga_Session session,
                                  uint32_t       indicator,
                                  double*        array,
                                  size_t         size);

/**
 * @}
 */

/** \addtogroup WriteArray
 *  @{
 */

/**
 * Writes an entire array of boolean values to a given array control or
 * indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayBool(NiFpga_Session     session,
                                    uint32_t           control,
                                    const NiFpga_Bool* array,
                                    size_t             size);

/**
 * Writes an entire array of signed 8-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayI8(NiFpga_Session session,
                                  uint32_t       control,
                                  const int8_t*  array,
                                  size_t         size);

/**
 * Writes an entire array of unsigned 8-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayU8(NiFpga_Session session,
                                  uint32_t       control,
                                  const uint8_t* array,
                                  size_t         size);

/**
 * Writes an entire array of signed 16-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayI16(NiFpga_Session session,
                                   uint32_t       control,
                                   const int16_t* array,
                                   size_t         size);

/**
 * Writes an entire array of unsigned 16-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayU16(NiFpga_Session  session,
                                   uint32_t        control,
                                   const uint16_t* array,
                                   size_t          size);

/**
 * Writes an entire array of signed 32-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayI32(NiFpga_Session session,
                                   uint32_t       control,
                                   const int32_t* array,
                                   size_t         size);

/**
 * Writes an entire array of unsigned 32-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayU32(NiFpga_Session  session,
                                   uint32_t        control,
                                   const uint32_t* array,
                                   size_t          size);

/**
 * Writes an entire array of signed 64-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayI64(NiFpga_Session session,
                                   uint32_t       control,
                                   const int64_t* array,
                                   size_t         size);

/**
 * Writes an entire array of unsigned 64-bit integer values to a given array
 * control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayU64(NiFpga_Session  session,
                                   uint32_t        control,
                                   const uint64_t* array,
                                   size_t          size);

/**
 * Writes an entire array of single-precision floating-point values to a given
 * array control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArraySgl(NiFpga_Session session,
                                   uint32_t       control,
                                   const float*   array,
                                   size_t         size);

/**
 * Writes an entire array of double-precision floating-point values to a given
 * array control or indicator.
 *
 * @warning The size passed must be the exact number of elements in the
 *          control or indicator.
 *
 * @param session handle to a currently open session
 * @param control control or indicator to which to write
 * @param array entire array to write
 * @param size exact number of elements in the control or indicator
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteArrayDbl(NiFpga_Session session,
                                   uint32_t       control,
                                   const double*  array,
                                   size_t         size);

/**
 * @}
 */

/**
 * Represents an infinite timeout.
 */
static const uint32_t NiFpga_InfiniteTimeout = 0xFFFFFFFF;

/** \addtogroup Interrupt
 *  @{
 */

/**
 * Enumeration of all 32 possible IRQs. Multiple IRQs can be bitwise ORed
 * together like this:
 *
 *    NiFpga_Irq_3 | NiFpga_Irq_23
 */
typedef enum
{
   NiFpga_Irq_0  = 1 << 0,
   NiFpga_Irq_1  = 1 << 1,
   NiFpga_Irq_2  = 1 << 2,
   NiFpga_Irq_3  = 1 << 3,
   NiFpga_Irq_4  = 1 << 4,
   NiFpga_Irq_5  = 1 << 5,
   NiFpga_Irq_6  = 1 << 6,
   NiFpga_Irq_7  = 1 << 7,
   NiFpga_Irq_8  = 1 << 8,
   NiFpga_Irq_9  = 1 << 9,
   NiFpga_Irq_10 = 1 << 10,
   NiFpga_Irq_11 = 1 << 11,
   NiFpga_Irq_12 = 1 << 12,
   NiFpga_Irq_13 = 1 << 13,
   NiFpga_Irq_14 = 1 << 14,
   NiFpga_Irq_15 = 1 << 15,
   NiFpga_Irq_16 = 1 << 16,
   NiFpga_Irq_17 = 1 << 17,
   NiFpga_Irq_18 = 1 << 18,
   NiFpga_Irq_19 = 1 << 19,
   NiFpga_Irq_20 = 1 << 20,
   NiFpga_Irq_21 = 1 << 21,
   NiFpga_Irq_22 = 1 << 22,
   NiFpga_Irq_23 = 1 << 23,
   NiFpga_Irq_24 = 1 << 24,
   NiFpga_Irq_25 = 1 << 25,
   NiFpga_Irq_26 = 1 << 26,
   NiFpga_Irq_27 = 1 << 27,
   NiFpga_Irq_28 = 1 << 28,
   NiFpga_Irq_29 = 1 << 29,
   NiFpga_Irq_30 = 1 << 30,
   NiFpga_Irq_31 = 1U << 31
} NiFpga_Irq;

/**
 * See NiFpga_ReserveIrqContext for more information.
 */
typedef void* NiFpga_IrqContext;

/**
 * IRQ contexts are single-threaded; only one thread can wait with a
 * particular context at any given time. To minimize jitter when first
 * waiting on IRQs, reserve as many contexts as the application
 * requires.
 *
 * If a context is successfully reserved (the returned status is not an error),
 * it must be unreserved later. Otherwise a memory leak will occur.
 *
 * @param session handle to a currently open session
 * @param context outputs the IRQ context
 * @return result of the call
 */
NiFpga_Status NiFpga_ReserveIrqContext(NiFpga_Session     session,
                                       NiFpga_IrqContext* context);

/**
 * Unreserves an IRQ context obtained from NiFpga_ReserveIrqContext.
 *
 * @param session handle to a currently open session
 * @param context IRQ context to unreserve
 * @return result of the call
 */
NiFpga_Status NiFpga_UnreserveIrqContext(NiFpga_Session    session,
                                         NiFpga_IrqContext context);

/**
 * This is a blocking function that stops the calling thread until the
 * FPGA asserts any IRQ in the irqs parameter, or until the function
 * call times out. Before calling this function, use
 * NiFpga_ReserveIrqContext to reserve an IRQ context. No other
 * threads can use the same context when this function is called.
 *
 * You can use the irqsAsserted parameter to determine which IRQs were asserted
 * for each function call.
 *
 * @param session handle to a currently open session
 * @param context IRQ context with which to wait
 * @param irqs bitwise OR of NiFpga_Irqs
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param irqsAsserted if non-NULL, outputs bitwise OR of IRQs that were
 *                     asserted
 * @param timedOut if non-NULL, outputs whether the timeout expired
 * @return result of the call
 */
NiFpga_Status NiFpga_WaitOnIrqs(NiFpga_Session    session,
                                NiFpga_IrqContext context,
                                uint32_t          irqs,
                                uint32_t          timeout,
                                uint32_t*         irqsAsserted,
                                NiFpga_Bool*      timedOut);

/**
 * Acknowledges an IRQ or set of IRQs.
 *
 * @param session handle to a currently open session
 * @param irqs bitwise OR of NiFpga_Irqs
 * @return result of the call
 */
NiFpga_Status NiFpga_AcknowledgeIrqs(NiFpga_Session session,
                                     uint32_t       irqs);

/**
 * @}
 */

/** \addtogroup FifoMethod
 *  @{
 */

/**
 * Specifies the depth of the host memory part of the DMA FIFO. This method is
 * optional. In order to see the actual depth configured, use
 * NiFpga_ConfigureFifo2.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to configure
 * @param depth requested number of elements in the host memory part of the
 *              DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ConfigureFifo(NiFpga_Session session,
                                   uint32_t       fifo,
                                   size_t         depth);

/**
 * Specifies the depth of the host memory part of the DMA FIFO. This method is
 * optional.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to configure
 * @param requestedDepth requested number of elements in the host memory part
 *                       of the DMA FIFO
 * @param actualDepth if non-NULL, outputs the actual number of elements in the
 *                    host memory part of the DMA FIFO, which may be more than
 *                    the requested number
 * @return result of the call
 */
NiFpga_Status NiFpga_ConfigureFifo2(NiFpga_Session session,
                                    uint32_t       fifo,
                                    size_t         requestedDepth,
                                    size_t*        actualDepth);

/**
 * @}
 */

/** \addtogroup AdvancedFifoConfig
 *  @{
 */

/**
 * FIFO Properties are only supported by certain RIO devices and is not
 * supported on Pharlap.
 */
#if NiFpga_Linux || NiFpga_Windows || NiFpga_MacOsX
typedef enum
{
   /**
    * BytesPerElement
    *
    * Type: U32
    *
    * Specifies the number of bytes in a single element of the FIFO. Other
    * FIFO Buffer related properties are specified in number of elements, so
    * this property can be used to convert that number to a number of bytes.
    *
    * This property is only Getable and cannot be Set.
    */
   NiFpga_FifoProperty_BytesPerElement = 1,
   /**
    * HostBufferAllocationGranularity
    *
    * Type: U32
    *
    * Specifies the smallest discreet allocation unit that the HostBufferSize
    * will be coerced too. By default, this value will be set to the most
    * optimized setting for your hardware and system. This usually ends up
    * being the system's page size. The only valid values for this property
    * are powers of 2.
    */
   NiFpga_FifoProperty_HostBufferAllocationGranularity = 2,
   /**
    * HostBufferSize
    *
    * Type: U64
    *
    * The number of elements in the host memory part of the DMA FIFO. This size
    * will be coerced to be a multiple of the HostBufferAllocationGranularity.
    */
   NiFpga_FifoProperty_HostBufferSize = 3,
   /**
    * HostBufferMirrorSize
    *
    * Type: U64
    *
    * Specifies the number of elements mirrored at the end of the host memory
    * part of the DMA FIFO. By mirrored, we mean that the memory is mapped in
    * such a way that these elements point to the same physical memory as the
    * elements at the beginning of the host memory part of the DMA FIFO.
    *
    * Setting up memory like this improves use with the AcquireFifoElements API.
    * When using AcquireFifoElements, you can hit the end of the buffer and
    * recieve less elements than you attempted to acquire. This requires a
    * second AcquireFifoElements call to get the remaining elements.
    * Mirroring Elements avoids that second call.
    *
    * Example:
    * ========
    * **Behavior without Mirrored Elements**:
    *
    * This is a Target to Host FIFO of 10 elements:
    *
    *        0-1-2-3-4-5-6-7-8-9
    *        ^
    *        Current FIFO pointer here.
    *
    * 1. Acquire, use and Release 7 elements.
    *
    *        0-1-2-3-4-5-6-7-8-9
    *                      ^
    *                      Current FIFO pointer here.
    *
    * 2. The device writes to those 7 elements, filling up the FIFO.
    * 3. Attempt to acquire 7 elements, get back 3 because we can only give a
    *    pointer to 3 elements.
    *
    * **Behavior with Mirrored Elements**:
    *
    * If instead we had mirrored 4 elements, it would act like this.
    *
    *        0-1-2-3-4-5-6-7-8-9{0-1-2-3}
    *        ^                   ^mirrored elements
    *        Current FIFO pointer here.
    *
    * 1. Acquire, use and Release 7 elements.
    *
    *        0-1-2-3-4-5-6-7-8-9{0-1-2-3}
    *                      ^     ^mirrored elements
    *                      Current FIFO pointer here.
    *
    * 2. The device writes to those 7 elements, filling up the FIFO.
    * 3. Acquire, use and Release 7 elements. No problems are encountered
    *    because the driver gives back a pointer to the 7 elements requested.
    */
   NiFpga_FifoProperty_HostBufferMirrorSize = 4,
   /**
    * HostBufferType
    *
    * Type: I32
    *
    * Specifies the type of memory used in the host memory part of the DMA FIFO.
    * See NiFpga_HostBufferType for the valid values of this property.
    */
   NiFpga_FifoProperty_HostBufferType = 5,
   /**
    * HostBuffer
    *
    * Type: Ptr
    *
    * Specifies a pointer to the start of the host memory part of the DMA FIFO.
    * Can only be set if the HostBufferType is set to
    * NiFpga_HostBufferType_AllocatedByUser.
    *
    * Note, if the buffer is user supplied, the buffer will be pagelocked
    * by the driver. When the user has finished with the buffer, the user must
    * do one of the following before deallocating the buffer:
    * 1. Call NiFpga_Close on the NiFpga_Session
    * 2. Set the buffer type to NiFpga_HostBufferType_AllocatedByRIO and call
    *    NiFpga_CommitFifoConfiguration.
    * 3. Set the NiFpga_FifoProperty_HostBuffer to a different buffer.
    * 4. End the process.
    */
   NiFpga_FifoProperty_HostBuffer= 6,
   /**
    * FlowControl
    *
    * Type: I32
    *
    * Specifies the flow control behavior of the DMA FIFO.
    * See NiFpga_FifoFlowControl for specifics on the behaviors.
    * Note, changing the behavior of a FIFO can make it work in a non-"first in
    * first out" manner.
    */
   NiFpga_FifoProperty_FlowControl = 7,
   /**
    * ElementsCurrentlyAcquired
    *
    * Type: U64
    *
    * Specifies the number of elements that are currently acquired by the user
    * using the NiFpga_AcquireFifoReadElements* functions that have not yet
    * been released.
    *
    * This property is only Getable and cannot be Set.
    */
   NiFpga_FifoProperty_ElementsCurrentlyAcquired = 8,
   /**
    * PreferredNumaNode
    * Type: I32
    * The NUMA node the FIFO should be allocated on.
    */
   NiFpga_FifoProperty_PreferredNumaNode = 9,
   /**
    * NumberOfZeroCopyRegions
    * Type: U32
    * The number of zero copy regions that can be acquired at once.
    */
   NiFpga_FifoProperty_NumberOfZeroCopyRegions = 10
} NiFpga_FifoProperty;

typedef enum
{
   /**
    * Specifies that the DMA Buffer will be allocated by the NI-RIO driver
    * according to the options specified in the other FIFO properties.
    */
   NiFpga_HostBufferType_AllocatedByRIO = 1,
   /**
    * Specifies that the user has allocated the FIFO to the options specified
    * in the other FIFO properties. After setting this property, the user
    * should set NiFpga_FifoProperty_HostBuffer to their specified buffer.
    */
   NiFpga_HostBufferType_AllocatedByUser = 2
} NiFpga_HostBufferType;

typedef enum
{
   /**
    * When this option is specified, the FPGA will fully control data transfer
    * without any action from the host. FIFOs will no longer act in a first
    * in first out manner. It is up to the user to synchronize with the FPGA
    * and ensure coherent data.
    *
    * For Target To Host FIFOs, data will being transferring on StartFifo.
    * For Host To Target FIFOs, data will begin transferring when the entire
    * host part of the DMA FIFO has been written once. This is intended to
    * prevent the FPGA from reading garbage data from an uninitialized buffer
    * on the host.
    */
   NiFpga_FifoFlowControl_Disabled = 1,
   /**
    * This is the default options for FIFOs. When this option is specified,
    * FIFOs act with First In First Out behavior and no data is ever lost.
    * Data will stop transferring if the host memory part of the FIFO becomes
    * full rather than overwriting it.
    */
   NiFpga_FifoFlowControl_Enabled = 2
} NiFpga_FifoFlowControl;
#else
typedef enum
{
   NiFpga_FifoProperty_NotSupported
} NiFpga_FifoProperty;
#endif /* NiFpga_Linux || NiFpga_Windows || NiFpga_MacOsX */

/**
 * Sets the specified U32 FIFO property to the requested value. The specified
 * value may be coerced to a different value if nessessary. The FIFO must be
 * stopped before using this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to set
 * @param value the desired value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_SetFifoPropertyU32(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        uint32_t            value);

/**
 * Sets the specified I32 FIFO property to the requested value. The specified
 * value may be coerced to a different value if nessessary. The FIFO must be
 * stopped before using this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to set
 * @param value the desired value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_SetFifoPropertyI32(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        int32_t             value);

/**
 * Sets the specified U64 FIFO property to the requested value. The specified
 * value may be coerced to a different value if nessessary. The FIFO must be
 * stopped before using this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to set
 * @param value the desired value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_SetFifoPropertyU64(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        uint64_t            value);

/**
 * Sets the specified I64 FIFO property to the requested value. The specified
 * value may be coerced to a different value if nessessary. The FIFO must be
 * stopped before using this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to set
 * @param value the desired value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_SetFifoPropertyI64(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        int64_t             value);

/**
 * Sets the specified pointer FIFO property to the requested value. The
 * specified value may be coerced to a different value if nessessary. The FIFO
 * must be stopped before using this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to set
 * @param value the desired value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_SetFifoPropertyPtr(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        void*               value);

/**
 * Gets the value of the specified U32 FIFO property. The value returned may be
 * coerced from the value set. The value returned will be used by the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to get
 * @param value the actual value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFifoPropertyU32(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        uint32_t*           value);

/**
 * Gets the value of the specified I32 FIFO property. The value returned may be
 * coerced from the value set. The value returned will be used by the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to get
 * @param value the actual value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFifoPropertyI32(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        int32_t*            value);

/**
 * Gets the value of the specified U64 FIFO property. The value returned may be
 * coerced from the value set. The value returned will be used by the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to get
 * @param value the actual value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFifoPropertyU64(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        uint64_t*           value);

/**
 * Gets the value of the specified I64 FIFO property. The value returned may be
 * coerced from the value set. The value returned will be used by the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to get
 * @param value the actual value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFifoPropertyI64(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        int64_t*            value);

/**
 * Gets the value of the specified pointer FIFO property. The value returned may
 * be coerced from the value set. The value returned will be used by the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to use
 * @param property NiFpga_FifoProperty to get
 * @param value the actual value of the property
 * @return result of the call
 */
NiFpga_Status NiFpga_GetFifoPropertyPtr(NiFpga_Session      session,
                                        uint32_t            fifo,
                                        NiFpga_FifoProperty property,
                                        void**              value);

/**
 * Commits the configuration of the FIFO. Resolves the host memory part of the
 * DMA FIFO and commits FIFO properties to the driver. The FIFO must be stopped
 * to call this function.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to commit configuration
 * @return result of the call
 */
NiFpga_Status NiFpga_CommitFifoConfiguration(NiFpga_Session session,
                                             uint32_t       fifo);
/**
 * @}
 */

/** \addtogroup FifoMethod
 *  @{
 */

/**
 * Starts a FIFO. This method is optional.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to start
 * @return result of the call
 */
NiFpga_Status NiFpga_StartFifo(NiFpga_Session session,
                               uint32_t       fifo);

/**
 * Stops a FIFO. This method is optional.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to stop
 * @return result of the call
 */
NiFpga_Status NiFpga_StopFifo(NiFpga_Session session,
                              uint32_t       fifo);

/**
 * Unreserves a FIFO. This method is optional. FIFOs are only usable in the
 * process that first uses them.  This function releases a FIFO from the using
 * session and process so a session in a different process can use the FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO to unreserve
 * @return result of the call
 */
NiFpga_Status NiFpga_UnreserveFifo(NiFpga_Session session,
                                   uint32_t       fifo);

/**
 * @}
 */

/** \addtogroup ReadFifo
 *  @{
 */

/**
 * Reads from a target-to-host FIFO of booleans.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoBool(NiFpga_Session session,
                                  uint32_t       fifo,
                                  NiFpga_Bool*   data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of signed 8-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoI8(NiFpga_Session session,
                                uint32_t       fifo,
                                int8_t*        data,
                                size_t         numberOfElements,
                                uint32_t       timeout,
                                size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of unsigned 8-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoU8(NiFpga_Session session,
                                uint32_t       fifo,
                                uint8_t*       data,
                                size_t         numberOfElements,
                                uint32_t       timeout,
                                size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of signed 16-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoI16(NiFpga_Session session,
                                 uint32_t       fifo,
                                 int16_t*       data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of unsigned 16-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoU16(NiFpga_Session session,
                                 uint32_t       fifo,
                                 uint16_t*      data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of signed 32-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoI32(NiFpga_Session session,
                                 uint32_t       fifo,
                                 int32_t*       data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of unsigned 32-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoU32(NiFpga_Session session,
                                 uint32_t       fifo,
                                 uint32_t*      data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of signed 64-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoI64(NiFpga_Session session,
                                 uint32_t       fifo,
                                 int64_t*       data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of unsigned 64-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoU64(NiFpga_Session session,
                                 uint32_t       fifo,
                                 uint64_t*      data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of single-precision floating-point values.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoSgl(NiFpga_Session session,
                                 uint32_t       fifo,
                                 float*         data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of double-precision floating-point values.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoDbl(NiFpga_Session session,
                                 uint32_t       fifo,
                                 double*        data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        elementsRemaining);

/**
 * Reads from a target-to-host FIFO of composite types such as clusters.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param data outputs the data that was read
 * @param bytesPerElement the size in bytes of each element
 * @param numberOfElements number of elements to read
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_ReadFifoComposite(NiFpga_Session session,
                                       uint32_t       fifo,
                                       void*          data,
                                       uint32_t       bytesPerElement,
                                       size_t         numberOfElements,
                                       uint32_t       timeout,
                                       size_t*        elementsRemaining);

/**
 * @}
 */

/** \addtogroup WriteFifo
 *  @{
 */

/**
 * Writes to a host-to-target FIFO of booleans.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoBool(NiFpga_Session     session,
                                   uint32_t           fifo,
                                   const NiFpga_Bool* data,
                                   size_t             numberOfElements,
                                   uint32_t           timeout,
                                   size_t*            emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of signed 8-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoI8(NiFpga_Session session,
                                 uint32_t       fifo,
                                 const int8_t*  data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of unsigned 8-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoU8(NiFpga_Session session,
                                 uint32_t       fifo,
                                 const uint8_t* data,
                                 size_t         numberOfElements,
                                 uint32_t       timeout,
                                 size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of signed 16-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoI16(NiFpga_Session session,
                                  uint32_t       fifo,
                                  const int16_t* data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of unsigned 16-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoU16(NiFpga_Session  session,
                                  uint32_t        fifo,
                                  const uint16_t* data,
                                  size_t          numberOfElements,
                                  uint32_t        timeout,
                                  size_t*         emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of signed 32-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoI32(NiFpga_Session session,
                                  uint32_t       fifo,
                                  const int32_t* data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of unsigned 32-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoU32(NiFpga_Session  session,
                                  uint32_t        fifo,
                                  const uint32_t* data,
                                  size_t          numberOfElements,
                                  uint32_t        timeout,
                                  size_t*         emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of signed 64-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoI64(NiFpga_Session session,
                                  uint32_t       fifo,
                                  const int64_t* data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of unsigned 64-bit integers.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoU64(NiFpga_Session  session,
                                  uint32_t        fifo,
                                  const uint64_t* data,
                                  size_t          numberOfElements,
                                  uint32_t        timeout,
                                  size_t*         emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of single-precision floating-point values.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoSgl(NiFpga_Session session,
                                  uint32_t       fifo,
                                  const float*   data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of double-precision floating-point values.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoDbl(NiFpga_Session session,
                                  uint32_t       fifo,
                                  const double*  data,
                                  size_t         numberOfElements,
                                  uint32_t       timeout,
                                  size_t*        emptyElementsRemaining);

/**
 * Writes to a host-to-target FIFO of composite types such as clusters.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param data data to write
 * @param bytesPerElement the size in bytes of each element
 * @param numberOfElements number of elements to write
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param emptyElementsRemaining if non-NULL, outputs the number of empty
 *                               elements remaining in the host memory part of
 *                               the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_WriteFifoComposite(NiFpga_Session session,
                                        uint32_t       fifo,
                                        const void*    data,
                                        uint32_t       bytesPerElement,
                                        size_t         numberOfElements,
                                        uint32_t       timeout,
                                        size_t*        emptyElementsRemaining);

/**
 * @}
 */

/** \addtogroup AcquireFifoRead
 *  @{
 */

/**
 * Acquires elements for reading from a target-to-host FIFO of booleans.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsBool(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             NiFpga_Bool**  elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of signed 8-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsI8(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             int8_t**       elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of unsigned 8-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsU8(
                                            NiFpga_Session  session,
                                            uint32_t        fifo,
                                            uint8_t**       elements,
                                            size_t          elementsRequested,
                                            uint32_t        timeout,
                                            size_t*         elementsAcquired,
                                            size_t*         elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of signed 16-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsI16(
                                            NiFpga_Session  session,
                                            uint32_t        fifo,
                                            int16_t**       elements,
                                            size_t          elementsRequested,
                                            uint32_t        timeout,
                                            size_t*         elementsAcquired,
                                            size_t*         elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of unsigned 16-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsU16(
                                           NiFpga_Session   session,
                                           uint32_t         fifo,
                                           uint16_t**       elements,
                                           size_t           elementsRequested,
                                           uint32_t         timeout,
                                           size_t*          elementsAcquired,
                                           size_t*          elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of signed 32-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsI32(
                                            NiFpga_Session  session,
                                            uint32_t        fifo,
                                            int32_t**       elements,
                                            size_t          elementsRequested,
                                            uint32_t        timeout,
                                            size_t*         elementsAcquired,
                                            size_t*         elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of unsigned 32-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsU32(
                                           NiFpga_Session   session,
                                           uint32_t         fifo,
                                           uint32_t**       elements,
                                           size_t           elementsRequested,
                                           uint32_t         timeout,
                                           size_t*          elementsAcquired,
                                           size_t*          elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of signed 64-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsI64(
                                            NiFpga_Session  session,
                                            uint32_t        fifo,
                                            int64_t**       elements,
                                            size_t          elementsRequested,
                                            uint32_t        timeout,
                                            size_t*         elementsAcquired,
                                            size_t*         elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of unsigned 64-bit
 * integers.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsU64(
                                           NiFpga_Session   session,
                                           uint32_t         fifo,
                                           uint64_t**       elements,
                                           size_t           elementsRequested,
                                           uint32_t         timeout,
                                           size_t*          elementsAcquired,
                                           size_t*          elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of single-precision
 * floating-point values.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsSgl(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             float**        elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for reading from a target-to-host FIFO of double-precision
 * floating-point values.
 *
 * Acquiring, reading, and releasing FIFO elements prevents the need to copy
 * the contents of elements from the host memory buffer to a separate
 * user-allocated buffer before reading. The FPGA target cannot write to
 * elements acquired by the host. Therefore, the host must release elements
 * after reading them. The number of elements acquired may differ from the
 * number of elements requested if, for example, the number of elements
 * requested reaches the end of the host memory buffer. Always release all
 * acquired elements before closing the session. Do not attempt to access FIFO
 * elements after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadElementsDbl(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             double**       elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires a zero copy region for reading from a target-to-host FIFO
 *
 * Acquiring, reading, and releasing zero copy FIFO regions prevents the need to copy
 * the contents of elements from the host memory buffer to a separate user-allocated 
 * buffer. This can be useful when accessing large sections.The FPGA target cannot write to
 * elements acquired by the host. Therefore the host must release regions after reading them.
 * The number of elements may differ from the number of elements requested if, for example,
 * the number of elements requested reaches the end of the host memory buffer. Always release all
 * acquired regions before closing the session. Do not attempt to access FIFO
 * regions after the regions are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo target-to-host FIFO from which to read
 * @param region points to an opaque type the user will need to release the region
 * @param elements outputs a pointer to the elements acquired
 * @param isSigned whether the data is signed or not
 * @param elementSizeBytes Size in bytes of the data type to read
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoReadRegion(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             void**         region,
                                             void**         elements,
                                             NiFpga_Bool    isSigned,
                                             uint32_t       elementSizeBytes,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * @}
 */

/** \addtogroup AcquireFifoWrite
 *  @{
 */

/**
 * Acquires elements for writing to a host-to-target FIFO of booleans.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsBool(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             NiFpga_Bool**  elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of signed 8-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsI8(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             int8_t**       elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of unsigned 8-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsU8(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             uint8_t**      elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of signed 16-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsI16(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             int16_t**      elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of unsigned 16-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsU16(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             uint16_t**     elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of signed 32-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsI32(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             int32_t**      elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of unsigned 32-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsU32(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             uint32_t**     elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of signed 64-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsI64(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             int64_t**      elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of unsigned 64-bit
 * integers.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsU64(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             uint64_t**     elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of single-precision
 * floating-point values.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsSgl(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             float**        elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires elements for writing to a host-to-target FIFO of single-precision
 * floating-point values.
 *
 * Acquiring, writing, and releasing FIFO elements prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release elements after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param elements outputs a pointer to the elements acquired
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteElementsDbl(
                                             NiFpga_Session session,
                                             uint32_t       fifo,
                                             double**       elements,
                                             size_t         elementsRequested,
                                             uint32_t       timeout,
                                             size_t*        elementsAcquired,
                                             size_t*        elementsRemaining);

/**
 * Acquires a zero copy region for writing to a host-to-target FIFO.
 *
 * Acquiring, writing, and releasing FIFO zero copy FIFO regions prevents the need to write
 * first into a separate user-allocated buffer and then copy the contents of
 * elements to the host memory buffer. The FPGA target cannot read elements
 * acquired by the host. Therefore, the host must release regions after
 * writing to them. The number of elements acquired may differ from the number
 * of elements requested if, for example, the number of elements requested
 * reaches the end of the host memory buffer. Always release all acquired
 * regions before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo host-to-target FIFO to which to write
 * @param region points to an opaque type the user will need to release the region
 * @param elements outputs a pointer to the elements acquired
 * @param isSigned whether the data is signed or not
 * @param elementSizeBytes Size in bytes of the data type to write
 * @param elementsRequested requested number of elements
 * @param timeout timeout in milliseconds, or NiFpga_InfiniteTimeout
 * @param elementsAcquired actual number of elements acquired, which may be
 *                         less than the requested number
 * @param elementsRemaining if non-NULL, outputs the number of elements
 *                          remaining in the host memory part of the DMA FIFO
 * @return result of the call
 */
NiFpga_Status NiFpga_AcquireFifoWriteRegion(
                                       NiFpga_Session session,
                                       uint32_t       fifo,
                                       void**         region,
                                       void**         elements,
                                       NiFpga_Bool    isSigned,
                                       uint32_t       elementSizeBytes,
                                       size_t         elementsRequested,
                                       uint32_t       timeout,
                                       size_t*        elementsAcquired,
                                       size_t*        elementsRemaining);

/**
 * @}
 */

/** \addtogroup FifoMethod
 *  @{
 */

/**
 * Releases previously acquired FIFO elements.
 *
 * The FPGA target cannot read elements acquired by the host. Therefore, the
 * host must release elements after acquiring them. Always release all acquired
 * elements before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO from which to release elements
 * @param elements number of elements to release
 * @return result of the call
 */
NiFpga_Status NiFpga_ReleaseFifoElements(NiFpga_Session session,
                                         uint32_t       fifo,
                                         size_t         elements);

/**
 * Releases a previously acquired FIFO region.
 *
 * The FPGA target cannot read elements in a region acquired by the host. Therefore, the
 * host must release regions after acquiring them. Always release all acquired
 * regions before closing the session. Do not attempt to access FIFO elements
 * after the elements are released or the session is closed.
 *
 * @param session handle to a currently open session
 * @param fifo FIFO from which to release elements
 * @param region Points to the region to release
 * @return result of the call
 */
NiFpga_Status NiFpga_ReleaseFifoRegion(NiFpga_Session session,
                                       uint32_t       fifo,
                                       void*          region);

/**
 * Gets an endpoint reference to a peer-to-peer FIFO.
 *
 * @param session handle to a currently open session
 * @param fifo peer-to-peer FIFO
 * @param endpoint Outputs the endpoint reference.
 *                 The actual type is a nip2p_tEndpointHandle usable by
 *                 the NI Peer-to-Peer Streaming C/C++ API.
 * @return result of the call
 */
NiFpga_Status NiFpga_GetPeerToPeerFifoEndpoint(NiFpga_Session session,
                                               uint32_t       fifo,
                                               uint32_t*      endpoint);

/**
 * Maps the write window of a peer-to-peer reader FIFO.
 *
 * The P2P reader expects linear accesses to the memory. This means that the
 * libc memcpy is probably not safe and will cause out-of-order data writes.
 *
 * This memory may not be read from. Doing so could cause a bus hang on some
 * targets. This includes reads issued by a debugger. Proceed with caution.
 *
 * This FIFO must be unmapped before a new FPGA image can be downloaded.
 *
 * @param session handle to a currently open session
 * @param fifo peer-to-peer Sink FIFO
 * @param size Outputs the size of the mapped region.
 * @param virtualAddress Outputs the base address of the mapped region.
 * @return result of the call
 */
NiFpga_Status NiFpga_MapP2PSinkFifo(const NiFpga_Session session,
                                    const uint32_t       fifo,
                                    size_t*              size,
                                    void**               virtualAddress);

/**
 * Unmaps the write window of a peer-to-peer reader FIFO.
 *
 * @param session handle used to map the FIFO
 * @param fifo peer-to-peer Sink FIFO
 */
NiFpga_Status NiFpga_UnmapP2PSinkFifo(const NiFpga_Session session,
                                      const uint32_t       fifo);

/**
 * Open a Host Memory Buffer
 *
 * If the target supports creating a Host Memory Buffer, open the memory region
 * mapped into the calling process.
 *
 * Call NiFpga_CloseHostMemoryBuffer to unmap and close the HMB.
 *
 * @param session handle to a currently open session
 * @param memoryName Name given to the memory in the FPGA target
 * @param memorySize Outputs the size of the mapped region.
 * @param virtualAddress Outputs the base address of the mapped region.
 * @return result of the call
 */
NiFpga_Status NiFpga_OpenHostMemoryBuffer(const NiFpga_Session session,
                                          const char*          memoryName,
                                          size_t*              memorySize,
                                          void**               virtualAddress);

/**
 * Unmaps and closes the Host Memory Buffer
 *
 * @param session handle used to open the HMB
 * @param memoryName Name given to the memory in the FPGA target
 */
NiFpga_Status NiFpga_CloseHostMemoryBuffer(const NiFpga_Session session,
                                           const char*          memoryName);

/**
 * Open a Low Latency Buffer
 *
 * If the target supports creating a Low Latency Buffer, open the two memory
 * regions mapped into the calling process.
 *
 * Each mapped memory space is unidirectional allowing posted writes in each
 * direction for low-latency memory accesses between host and FPGA.
 *
 * Call NiFpga_CloseLowLatencyBuffer to unmap and close the LLB.
 *
 * @param session handle to a currently open session
 * @param memoryName Name given to the memory in the FPGA target
 * @param memorySizeToHost Outputs the size of the mapped region the FPGA writes to the Host.
 * @param virtualAddressToHost Outputs the base address of the mapped region the FPGA writes to the Host.
 * @param memorySizeToFpga Outputs the size of the mapped region the Host writes to the FPGA.
 * @param virtualAddressToFpga Outputs the base address of the mapped region the Host writes to the FPGA.
 * @return result of the call
 */
NiFpga_Status NiFpga_OpenLowLatencyBuffer(const NiFpga_Session session,
                                          const char*          memoryName,
                                          size_t*              memorySizeToHost,
                                          void**               virtualAddressToHost,
                                          size_t*              memorySizeToFpga,
                                          void**               virtualAddressToFpga);

/**
 * Unmaps and closes the Low Latency Buffer
 *
 * @param session handle used to open the LLB
 * @param memoryName Name given to the memory in the FPGA target
 */
NiFpga_Status NiFpga_CloseLowLatencyBuffer(const NiFpga_Session session,
                                           const char*          memoryName);

/**
 * @}
 */

#if NiFpga_Cpp
}
#endif

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxBT.h sha256=b2f626e18e8164868193eb0558be2273b6ffbcb179c867cba68ce37722137779 bytes=105504 -->
## FILE: imports/include/niRFmxBT.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxBT.h`
- sha256: `b2f626e18e8164868193eb0558be2273b6ffbcb179c867cba68ce37722137779`
- bytes: 105504

````c

/****************************************************************************************************
*          National Instruments RFmx BT
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2024.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxBT.h
*
* Purpose:  National Instruments RFmx BT,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_BT_H__
#define __NI_RFMX_BT_H__

#include "niRFmxInstr.h"

#define RFMXBT_ATTR_SELECTED_PORTS                                                                 0x00b00ffd
#define RFMXBT_ATTR_CENTER_FREQUENCY                                                               0x00b00001
#define RFMXBT_ATTR_REFERENCE_LEVEL                                                                0x00b00002
#define RFMXBT_ATTR_EXTERNAL_ATTENUATION                                                           0x00b00003
#define RFMXBT_ATTR_REFERENCE_LEVEL_HEADROOM                                                       0x00b00ffc
#define RFMXBT_ATTR_TRIGGER_TYPE                                                                   0x00b00004
#define RFMXBT_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                                    0x00b00005
#define RFMXBT_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                                      0x00b00006
#define RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                                   0x00b00007
#define RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                                    0x00b00008
#define RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                                               0x00b00fff
#define RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                                    0x00b00009
#define RFMXBT_ATTR_TRIGGER_DELAY                                                                  0x00b0000a
#define RFMXBT_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                                0x00b0000b
#define RFMXBT_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                                            0x00b0000c
#define RFMXBT_ATTR_PACKET_TYPE                                                                    0x00b0000d
#define RFMXBT_ATTR_DATA_RATE                                                                      0x00b0000e
#define RFMXBT_ATTR_BANDWIDTH_BIT_PERIOD_PRODUCT                                                   0x00b00034
#define RFMXBT_ATTR_BD_ADDRESS_LAP                                                                 0x00b0000f
#define RFMXBT_ATTR_ACCESS_ADDRESS                                                                 0x00b00011
#define RFMXBT_ATTR_PAYLOAD_BIT_PATTERN                                                            0x00b00012
#define RFMXBT_ATTR_PAYLOAD_LENGTH_MODE                                                            0x00b00013
#define RFMXBT_ATTR_PAYLOAD_LENGTH                                                                 0x00b00014
#define RFMXBT_ATTR_DIRECTION_FINDING_MODE                                                         0x00b0002c
#define RFMXBT_ATTR_CTE_LENGTH                                                                     0x00b0002d
#define RFMXBT_ATTR_CTE_SLOT_DURATION                                                              0x00b0002e
#define RFMXBT_ATTR_CTE_NUMBER_OF_TRANSMIT_SLOTS                                                   0x00b0002f
#define RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT                                                 0x00b00030
#define RFMXBT_ATTR_CHANNEL_SOUNDING_SYNC_SEQUENCE                                                 0x00b00031
#define RFMXBT_ATTR_CHANNEL_SOUNDING_PHASE_MEASUREMENT_PERIOD                                      0x00b00032
#define RFMXBT_ATTR_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT                                           0x00b00033
#define RFMXBT_ATTR_CHANNEL_SOUNDING_NUMBER_OF_ANTENNA_PATH                                        0x00b00036
#define RFMXBT_ATTR_CHANNEL_SOUNDING_ANTENNA_SWITCH_TIME                                           0x00b00035
#define RFMXBT_ATTR_AUTO_PREAMBLE_DETECTION_ENABLED                                                0x00b00042
#define RFMXBT_ATTR_ZADOFF_CHU_INDEX                                                               0x00b00039
#define RFMXBT_ATTR_HIGH_DATA_THROUGHPUT_PACKET_FORMAT                                             0x00b00038
#define RFMXBT_ATTR_VHDT_MODE_ENABLED                                                              0x00b00040
#define RFMXBT_ATTR_NUMBER_OF_BLOCK_REPETITION_SEQUENCES                                           0x00b00041
#define RFMXBT_ATTR_FREQUENCY_BAND                                                                 0x00b00045
#define RFMXBT_ATTR_CHANNEL_NUMBER                                                                 0x00b00017
#define RFMXBT_ATTR_DETECTED_PACKET_TYPE                                                           0x00b00019
#define RFMXBT_ATTR_DETECTED_DATA_RATE                                                             0x00b0002a
#define RFMXBT_ATTR_DETECTED_PAYLOAD_LENGTH                                                        0x00b0002b
#define RFMXBT_ATTR_DETECTED_PACKET_FORMAT                                                         0x00b00043
#define RFMXBT_ATTR_MODACC_MEASUREMENT_ENABLED                                                     0x00b04000
#define RFMXBT_ATTR_MODACC_BURST_SYNCHRONIZATION_TYPE                                              0x00b0402b
#define RFMXBT_ATTR_MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED                                     0x00b04003
#define RFMXBT_ATTR_MODACC_IQ_MISMATCH_CORRECTION_ENABLED                                          0x00b0403d
#define RFMXBT_ATTR_MODACC_FREQUENCY_TRACKING_ENABLED                                              0x00b04040
#define RFMXBT_ATTR_MODACC_AVERAGING_ENABLED                                                       0x00b04004
#define RFMXBT_ATTR_MODACC_AVERAGING_COUNT                                                         0x00b04005
#define RFMXBT_ATTR_MODACC_ALL_TRACES_ENABLED                                                      0x00b04006
#define RFMXBT_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS                                              0x00b04007
#define RFMXBT_ATTR_MODACC_RESULTS_DF1AVG_MEAN                                                     0x00b04009
#define RFMXBT_ATTR_MODACC_RESULTS_DF1AVG_MAXIMUM                                                  0x00b0400a
#define RFMXBT_ATTR_MODACC_RESULTS_DF1AVG_MINIMUM                                                  0x00b0400b
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_DF1MAX_MAXIMUM                                             0x00b0400c
#define RFMXBT_ATTR_MODACC_RESULTS_MINIMUM_DF1MAX_MINIMUM                                          0x00b0400d
#define RFMXBT_ATTR_MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF1MAX_THRESHOLD                    0x00b0402c
#define RFMXBT_ATTR_MODACC_RESULTS_DF2AVG_MEAN                                                     0x00b0400e
#define RFMXBT_ATTR_MODACC_RESULTS_DF2AVG_MAXIMUM                                                  0x00b0400f
#define RFMXBT_ATTR_MODACC_RESULTS_DF2AVG_MINIMUM                                                  0x00b04010
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_DF2MAX_MAXIMUM                                             0x00b04011
#define RFMXBT_ATTR_MODACC_RESULTS_MINIMUM_DF2MAX_MINIMUM                                          0x00b04012
#define RFMXBT_ATTR_MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF2MAX_THRESHOLD                    0x00b04013
#define RFMXBT_ATTR_MODACC_RESULTS_DF3AVG_MEAN                                                     0x00b04034
#define RFMXBT_ATTR_MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF4AVG_THRESHOLD                    0x00b04035
#define RFMXBT_ATTR_MODACC_RESULTS_BR_INITIAL_FREQUENCY_ERROR_MAXIMUM                              0x00b04014
#define RFMXBT_ATTR_MODACC_RESULTS_BR_PEAK_FREQUENCY_DRIFT_MAXIMUM                                 0x00b04015
#define RFMXBT_ATTR_MODACC_RESULTS_BR_PEAK_FREQUENCY_DRIFT_RATE_MAXIMUM                            0x00b04016
#define RFMXBT_ATTR_MODACC_RESULTS_EDR_HEADER_FREQUENCY_ERROR_WI_MAXIMUM                           0x00b04017
#define RFMXBT_ATTR_MODACC_RESULTS_EDR_PEAK_FREQUENCY_ERROR_WI_PLUS_W0_MAXIMUM                     0x00b04018
#define RFMXBT_ATTR_MODACC_RESULTS_EDR_PEAK_FREQUENCY_ERROR_W0_MAXIMUM                             0x00b04019
#define RFMXBT_ATTR_MODACC_RESULTS_LE_INITIAL_FREQUENCY_ERROR_MAXIMUM                              0x00b04031
#define RFMXBT_ATTR_MODACC_RESULTS_LE_PEAK_FREQUENCY_ERROR_MAXIMUM                                 0x00b0401a
#define RFMXBT_ATTR_MODACC_RESULTS_LE_INITIAL_FREQUENCY_DRIFT_MAXIMUM                              0x00b0401b
#define RFMXBT_ATTR_MODACC_RESULTS_LE_PEAK_FREQUENCY_DRIFT_MAXIMUM                                 0x00b0401c
#define RFMXBT_ATTR_MODACC_RESULTS_LE_PEAK_FREQUENCY_DRIFT_RATE_MAXIMUM                            0x00b0401d
#define RFMXBT_ATTR_MODACC_RESULTS_PREAMBLE_FREQUENCY_ERROR_W0_MAXIMUM                             0x00b0403a
#define RFMXBT_ATTR_MODACC_RESULTS_PAYLOAD_FREQUENCY_ERROR_W1_MAXIMUM                              0x00b0403b
#define RFMXBT_ATTR_MODACC_RESULTS_FREQUENCY_ERROR_W0_PLUS_W1_MAXIMUM                              0x00b0403c
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_RMS_DEVM_MAXIMUM                                           0x00b0401e
#define RFMXBT_ATTR_MODACC_RESULTS_RMS_DEVM_MEAN                                                   0x00b0401f
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_DEVM_MAXIMUM                                               0x00b04020
#define RFMXBT_ATTR_MODACC_RESULTS_99_PERCENT_DEVM                                                 0x00b04021
#define RFMXBT_ATTR_MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_BELOW_99_PERCENT_DEVM_LIMIT               0x00b04022
#define RFMXBT_ATTR_MODACC_RESULTS_AVERAGE_RMS_MAGNITUDE_ERROR_MEAN                                0x00b0402d
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_RMS_MAGNITUDE_ERROR_MAXIMUM                                0x00b0402e
#define RFMXBT_ATTR_MODACC_RESULTS_AVERAGE_RMS_PHASE_ERROR_MEAN                                    0x00b0402f
#define RFMXBT_ATTR_MODACC_RESULTS_PEAK_RMS_PHASE_ERROR_MAXIMUM                                    0x00b04030
#define RFMXBT_ATTR_MODACC_RESULTS_PREAMBLE_RMS_EVM_MEAN                                           0x00b04036
#define RFMXBT_ATTR_MODACC_RESULTS_CONTROL_HEADER_RMS_EVM_MEAN                                     0x00b04037
#define RFMXBT_ATTR_MODACC_RESULTS_PAYLOAD_RMS_EVM_MEAN                                            0x00b04038
#define RFMXBT_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN                                           0x00b04023
#define RFMXBT_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN                                          0x00b0403e
#define RFMXBT_ATTR_MODACC_RESULTS_QUADRATURE_ERROR_MEAN                                           0x00b0403f
#define RFMXBT_ATTR_MODACC_RESULTS_CLOCK_DRIFT_MEAN                                                0x00b04032
#define RFMXBT_ATTR_MODACC_RESULTS_PREAMBLE_START_TIME_MEAN                                        0x00b04033
#define RFMXBT_ATTR_MODACC_RESULTS_FRACTIONAL_TIME_OFFSET_MEAN                                     0x00b04039
#define RFMXBT_ATTR_ACP_MEASUREMENT_ENABLED                                                        0x00b05000
#define RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE                                                        0x00b05002
#define RFMXBT_ATTR_ACP_NUMBER_OF_OFFSETS                                                          0x00b05003
#define RFMXBT_ATTR_ACP_OFFSET_FREQUENCY                                                           0x00b05004
#define RFMXBT_ATTR_ACP_REFERENCE_CHANNEL_BANDWIDTH_MODE                                           0x00b05016
#define RFMXBT_ATTR_ACP_REFERENCE_CHANNEL_BANDWIDTH                                                0x00b05015
#define RFMXBT_ATTR_ACP_BURST_SYNCHRONIZATION_TYPE                                                 0x00b05012
#define RFMXBT_ATTR_ACP_AVERAGING_ENABLED                                                          0x00b05005
#define RFMXBT_ATTR_ACP_AVERAGING_COUNT                                                            0x00b05006
#define RFMXBT_ATTR_ACP_ALL_TRACES_ENABLED                                                         0x00b05007
#define RFMXBT_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                                                 0x00b05008
#define RFMXBT_ATTR_ACP_RESULTS_MEASUREMENT_STATUS                                                 0x00b0500a
#define RFMXBT_ATTR_ACP_RESULTS_REFERENCE_CHANNEL_POWER                                            0x00b0500b
#define RFMXBT_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                                        0x00b0500c
#define RFMXBT_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                                        0x00b0500d
#define RFMXBT_ATTR_ACP_RESULTS_LOWER_OFFSET_MARGIN                                                0x00b0500e
#define RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                                        0x00b0500f
#define RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                                        0x00b05010
#define RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_MARGIN                                                0x00b05011
#define RFMXBT_ATTR_20DB_BANDWIDTH_MEASUREMENT_ENABLED                                             0x00b02000
#define RFMXBT_ATTR_20DB_BANDWIDTH_AVERAGING_ENABLED                                               0x00b02002
#define RFMXBT_ATTR_20DB_BANDWIDTH_AVERAGING_COUNT                                                 0x00b02003
#define RFMXBT_ATTR_20DB_BANDWIDTH_ALL_TRACES_ENABLED                                              0x00b02004
#define RFMXBT_ATTR_20DB_BANDWIDTH_NUMBER_OF_ANALYSIS_THREADS                                      0x00b02005
#define RFMXBT_ATTR_20DB_BANDWIDTH_RESULTS_PEAK_POWER                                              0x00b02007
#define RFMXBT_ATTR_20DB_BANDWIDTH_RESULTS_BANDWIDTH                                               0x00b02008
#define RFMXBT_ATTR_20DB_BANDWIDTH_RESULTS_HIGH_FREQUENCY                                          0x00b02009
#define RFMXBT_ATTR_20DB_BANDWIDTH_RESULTS_LOW_FREQUENCY                                           0x00b0200a
#define RFMXBT_ATTR_FREQUENCY_RANGE_MEASUREMENT_ENABLED                                            0x00b03000
#define RFMXBT_ATTR_FREQUENCY_RANGE_SPAN                                                           0x00b03002
#define RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_ENABLED                                              0x00b03003
#define RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_COUNT                                                0x00b03004
#define RFMXBT_ATTR_FREQUENCY_RANGE_ALL_TRACES_ENABLED                                             0x00b03005
#define RFMXBT_ATTR_FREQUENCY_RANGE_NUMBER_OF_ANALYSIS_THREADS                                     0x00b03006
#define RFMXBT_ATTR_FREQUENCY_RANGE_RESULTS_HIGH_FREQUENCY                                         0x00b03008
#define RFMXBT_ATTR_FREQUENCY_RANGE_RESULTS_LOW_FREQUENCY                                          0x00b03009
#define RFMXBT_ATTR_MODSPECTRUM_MEASUREMENT_ENABLED                                                0x00b0f000
#define RFMXBT_ATTR_MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE                                         0x00b0f002
#define RFMXBT_ATTR_MODSPECTRUM_AVERAGING_ENABLED                                                  0x00b0f003
#define RFMXBT_ATTR_MODSPECTRUM_AVERAGING_COUNT                                                    0x00b0f004
#define RFMXBT_ATTR_MODSPECTRUM_ALL_TRACES_ENABLED                                                 0x00b0f005
#define RFMXBT_ATTR_MODSPECTRUM_NUMBER_OF_ANALYSIS_THREADS                                         0x00b0f006
#define RFMXBT_ATTR_MODSPECTRUM_RESULTS_BANDWIDTH                                                  0x00b0f008
#define RFMXBT_ATTR_MODSPECTRUM_RESULTS_HIGH_FREQUENCY                                             0x00b0f009
#define RFMXBT_ATTR_MODSPECTRUM_RESULTS_LOW_FREQUENCY                                              0x00b0f00a
#define RFMXBT_ATTR_TXP_MEASUREMENT_ENABLED                                                        0x00b01000
#define RFMXBT_ATTR_TXP_BURST_SYNCHRONIZATION_TYPE                                                 0x00b01010
#define RFMXBT_ATTR_TXP_AVERAGING_ENABLED                                                          0x00b01002
#define RFMXBT_ATTR_TXP_AVERAGING_COUNT                                                            0x00b01003
#define RFMXBT_ATTR_TXP_ALL_TRACES_ENABLED                                                         0x00b01004
#define RFMXBT_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS                                                 0x00b01005
#define RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN                                                 0x00b01007
#define RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MAXIMUM                                              0x00b01008
#define RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MINIMUM                                              0x00b01009
#define RFMXBT_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM                                                 0x00b0100a
#define RFMXBT_ATTR_TXP_RESULTS_PEAK_TO_AVERAGE_POWER_RATIO_MAXIMUM                                0x00b0100b
#define RFMXBT_ATTR_TXP_RESULTS_EDR_GFSK_AVERAGE_POWER_MEAN                                        0x00b0100c
#define RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_AVERAGE_POWER_MEAN                                        0x00b0100d
#define RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_GFSK_AVERAGE_POWER_RATIO_MEAN                             0x00b01013
#define RFMXBT_ATTR_TXP_RESULTS_LE_CTE_REFERENCE_PERIOD_AVERAGE_POWER_MEAN                         0x00b01014
#define RFMXBT_ATTR_TXP_RESULTS_LE_CTE_REFERENCE_PERIOD_PEAK_ABSOLUTE_POWER_DEVIATION_MAXIMUM      0x00b01015
#define RFMXBT_ATTR_TXP_RESULTS_LE_CTE_TRANSMIT_SLOT_AVERAGE_POWER_MEAN                            0x00b01016
#define RFMXBT_ATTR_TXP_RESULTS_LE_CTE_TRANSMIT_SLOT_PEAK_ABSOLUTE_POWER_DEVIATION_MAXIMUM         0x00b01017
#define RFMXBT_ATTR_TXP_RESULTS_LE_CS_PHASE_MEASUREMENT_PERIOD_AVERAGE_POWER_MEAN                  0x00b01018
#define RFMXBT_ATTR_POWERRAMP_MEASUREMENT_ENABLED                                                  0x00b0e000
#define RFMXBT_ATTR_POWERRAMP_BURST_SYNCHRONIZATION_TYPE                                           0x00b0e002
#define RFMXBT_ATTR_POWERRAMP_AVERAGING_ENABLED                                                    0x00b0e005
#define RFMXBT_ATTR_POWERRAMP_AVERAGING_COUNT                                                      0x00b0e006
#define RFMXBT_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS                                           0x00b0e007
#define RFMXBT_ATTR_POWERRAMP_RESULTS_RISE_TIME_MEAN                                               0x00b0e009
#define RFMXBT_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN                                               0x00b0e00a
#define RFMXBT_ATTR_POWERRAMP_RESULTS_40DB_RISE_TIME_MEAN                                          0x00b00044
#define RFMXBT_ATTR_POWERRAMP_RESULTS_40DB_FALL_TIME_MEAN                                          0x00b0e00b
#define RFMXBT_ATTR_LIMITED_CONFIGURATION_CHANGE                                                   0x00b0d000
#define RFMXBT_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                                             0x00b0d001
#define RFMXBT_ATTR_RESULT_FETCH_TIMEOUT                                                           0x00b0c000

// Values for RFMXBT_ATTR_TRIGGER_TYPE
#define RFMXBT_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXBT_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXBT_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXBT_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXBT_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXBT_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXBT_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXBT_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXBT_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXBT_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXBT_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXBT_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXBT_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXBT_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXBT_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXBT_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXBT_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXBT_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXBT_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXBT_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXBT_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXBT_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXBT_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXBT_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXBT_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXBT_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXBT_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXBT_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXBT_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXBT_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXBT_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXBT_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXBT_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXBT_ATTR_PACKET_TYPE
#define RFMXBT_VAL_PACKET_TYPE_UNKNOWN                                                            -1
#define RFMXBT_VAL_PACKET_TYPE_DH1                                                                0
#define RFMXBT_VAL_PACKET_TYPE_DH3                                                                1
#define RFMXBT_VAL_PACKET_TYPE_DH5                                                                2
#define RFMXBT_VAL_PACKET_TYPE_DM1                                                                3
#define RFMXBT_VAL_PACKET_TYPE_DM3                                                                4
#define RFMXBT_VAL_PACKET_TYPE_DM5                                                                5
#define RFMXBT_VAL_PACKET_TYPE_2_DH1                                                              6
#define RFMXBT_VAL_PACKET_TYPE_2_DH3                                                              7
#define RFMXBT_VAL_PACKET_TYPE_2_DH5                                                              8
#define RFMXBT_VAL_PACKET_TYPE_3_DH1                                                              9
#define RFMXBT_VAL_PACKET_TYPE_3_DH3                                                              10
#define RFMXBT_VAL_PACKET_TYPE_3_DH5                                                              11
#define RFMXBT_VAL_PACKET_TYPE_2_EV3                                                              12
#define RFMXBT_VAL_PACKET_TYPE_2_EV5                                                              13
#define RFMXBT_VAL_PACKET_TYPE_3_EV3                                                              14
#define RFMXBT_VAL_PACKET_TYPE_3_EV5                                                              15
#define RFMXBT_VAL_PACKET_TYPE_LE                                                                 16
#define RFMXBT_VAL_PACKET_TYPE_LE_CS                                                              17
#define RFMXBT_VAL_PACKET_TYPE_LE_HDT                                                             18

// Values for RFMXBT_ATTR_PAYLOAD_BIT_PATTERN
#define RFMXBT_VAL_PAYLOAD_BIT_PATTERN_STANDARD_DEFINED                                           0
#define RFMXBT_VAL_PAYLOAD_BIT_PATTERN_11110000                                                   1
#define RFMXBT_VAL_PAYLOAD_BIT_PATTERN_10101010                                                   2

// Values for RFMXBT_ATTR_PAYLOAD_LENGTH_MODE
#define RFMXBT_VAL_PAYLOAD_LENGTH_MODE_MANUAL                                                     0
#define RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO                                                       1

// Values for RFMXBT_ATTR_DIRECTION_FINDING_MODE
#define RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED                                                0
#define RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL                                        1
#define RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE                                      2

// Values for RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT
#define RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC                                            0
#define RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE                                         1
#define RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_AFTER_SYNC                              2
#define RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_BEFORE_SYNC                             3

// Values for RFMXBT_ATTR_CHANNEL_SOUNDING_SYNC_SEQUENCE
#define RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_NONE                                            0
#define RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_32_BIT                        1
#define RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_96_BIT                        2
#define RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_PAYLOAD_PATTERN                                 3

// Values for RFMXBT_ATTR_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT
#define RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_DISABLED                                  0
#define RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_ENABLED                                   1

// Values for RFMXBT_ATTR_AUTO_PREAMBLE_DETECTION_ENABLED
#define RFMXBT_VAL_AUTO_PREAMBLE_DETECTION_ENABLED_FALSE                                          0
#define RFMXBT_VAL_AUTO_PREAMBLE_DETECTION_ENABLED_TRUE                                           1

// Values for RFMXBT_ATTR_HIGH_DATA_THROUGHPUT_PACKET_FORMAT
#define RFMXBT_VAL_HIGH_DATA_THROUGHPUT_PACKET_FORMAT_SHORT_FORMAT                                0
#define RFMXBT_VAL_HIGH_DATA_THROUGHPUT_PACKET_FORMAT_FORMAT0                                     1
#define RFMXBT_VAL_HIGH_DATA_THROUGHPUT_PACKET_FORMAT_FORMAT1                                     2

// Values for RFMXBT_ATTR_VHDT_MODE_ENABLED
#define RFMXBT_VAL_VHDT_MODE_ENABLED_FALSE                                                        0
#define RFMXBT_VAL_VHDT_MODE_ENABLED_TRUE                                                         1

// Values for RFMXBT_ATTR_FREQUENCY_BAND
#define RFMXBT_VAL_FREQUENCY_BAND_2_4_GHZ                                                         0
#define RFMXBT_VAL_FREQUENCY_BAND_5_GHZ_1                                                         1
#define RFMXBT_VAL_FREQUENCY_BAND_5_GHZ_3                                                         2
#define RFMXBT_VAL_FREQUENCY_BAND_5_GHZ_4                                                         3
#define RFMXBT_VAL_FREQUENCY_BAND_5_GHZ_3_4                                                       4

// Values for RFMXBT_ATTR_MODACC_BURST_SYNCHRONIZATION_TYPE
#define RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_NONE                                         0
#define RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_PREAMBLE                                     1
#define RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD                                    2

// Values for RFMXBT_ATTR_MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED
#define RFMXBT_VAL_MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_FALSE                               0
#define RFMXBT_VAL_MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE                                1

// Values for RFMXBT_ATTR_MODACC_IQ_MISMATCH_CORRECTION_ENABLED
#define RFMXBT_VAL_MODACC_IQ_MISMATCH_CORRECTION_ENABLED_FALSE                                    0
#define RFMXBT_VAL_MODACC_IQ_MISMATCH_CORRECTION_ENABLED_TRUE                                     1

// Values for RFMXBT_ATTR_MODACC_FREQUENCY_TRACKING_ENABLED
#define RFMXBT_VAL_MODACC_FREQUENCY_TRACKING_ENABLED_FALSE                                        0
#define RFMXBT_VAL_MODACC_FREQUENCY_TRACKING_ENABLED_TRUE                                         1

// Values for RFMXBT_ATTR_MODACC_AVERAGING_ENABLED
#define RFMXBT_VAL_MODACC_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE
#define RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC                                              0
#define RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND                                                 1

// Values for RFMXBT_ATTR_ACP_REFERENCE_CHANNEL_BANDWIDTH_MODE
#define RFMXBT_VAL_ACP_REFERENCE_CHANNEL_BANDWIDTH_MODE_AUTO                                      0
#define RFMXBT_VAL_ACP_REFERENCE_CHANNEL_BANDWIDTH_MODE_MANUAL                                    1

// Values for RFMXBT_ATTR_ACP_BURST_SYNCHRONIZATION_TYPE
#define RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_NONE                                            0
#define RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE                                        1
#define RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD                                       2

// Values for RFMXBT_ATTR_ACP_AVERAGING_ENABLED
#define RFMXBT_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXBT_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXBT_ATTR_ACP_RESULTS_MEASUREMENT_STATUS
#define RFMXBT_VAL_ACP_RESULTS_MEASUREMENT_STATUS_NOT_APPLICABLE                                  -1
#define RFMXBT_VAL_ACP_RESULTS_MEASUREMENT_STATUS_FAIL                                            0
#define RFMXBT_VAL_ACP_RESULTS_MEASUREMENT_STATUS_PASS                                            1

// Values for RFMXBT_ATTR_20DB_BANDWIDTH_AVERAGING_ENABLED
#define RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_FALSE                                         0
#define RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_TRUE                                          1

// Values for RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_ENABLED
#define RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE                                        0
#define RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE                                         1

// Values for RFMXBT_ATTR_MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE
#define RFMXBT_VAL_MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE_NONE                                    0
#define RFMXBT_VAL_MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE_PREAMBLE                                1
#define RFMXBT_VAL_MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD                               2

// Values for RFMXBT_ATTR_MODSPECTRUM_AVERAGING_ENABLED
#define RFMXBT_VAL_MODSPECTRUM_AVERAGING_ENABLED_FALSE                                            0
#define RFMXBT_VAL_MODSPECTRUM_AVERAGING_ENABLED_TRUE                                             1

// Values for RFMXBT_ATTR_TXP_BURST_SYNCHRONIZATION_TYPE
#define RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_NONE                                            0
#define RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE                                        1
#define RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD                                       2

// Values for RFMXBT_ATTR_TXP_AVERAGING_ENABLED
#define RFMXBT_VAL_TXP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXBT_ATTR_POWERRAMP_BURST_SYNCHRONIZATION_TYPE
#define RFMXBT_VAL_POWERRAMP_BURST_SYNCHRONIZATION_TYPE_NONE                                      0
#define RFMXBT_VAL_POWERRAMP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE                                  1
#define RFMXBT_VAL_POWERRAMP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD                                 2

// Values for RFMXBT_ATTR_POWERRAMP_AVERAGING_ENABLED
#define RFMXBT_VAL_POWERRAMP_AVERAGING_ENABLED_FALSE                                              0
#define RFMXBT_VAL_POWERRAMP_AVERAGING_ENABLED_TRUE                                               1

// Values for RFMXBT_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXBT_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for Standard
#define RFMXBT_VAL_STANDARD_BR                                                                    0
#define RFMXBT_VAL_STANDARD_EDR                                                                   0
#define RFMXBT_VAL_STANDARD_LE                                                                    1
#define RFMXBT_VAL_STANDARD_LE_CS                                                                 2

// Values for Boolean
#define RFMXBT_VAL_FALSE                                                                          0
#define RFMXBT_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXBT_VAL_TXP                                                                            1<<0
#define RFMXBT_VAL_MODACC                                                                         1<<1
#define RFMXBT_VAL_20DB_BANDWIDTH                                                                 1<<2
#define RFMXBT_VAL_FREQUENCY_RANGE                                                                1<<3
#define RFMXBT_VAL_ACP                                                                            1<<4
#define RFMXBT_VAL_POWERRAMP                                                                      1<<5
#define RFMXBT_VAL_MODSPECTRUM                                                                    1<<6

// Values for FrequencyReferenceSource
#define RFMXBT_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXBT_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXBT_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXBT_VAL_CLK_IN_STR                                                                     "ClkIn"

/* ---------------- RFmxBT APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxBT_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxBT_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxBT_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxBT_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxBT_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxBT_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxBT_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxBT_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxBT_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxBT_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxBT_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxBT_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxBT_BuildSlotString(
   char selectorString[],
   int32 slotNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxBT_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxBT_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxBT_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxBT_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxBT_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxBT_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxBT_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxBT_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxBT_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxBT_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxBT_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxBT_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxBT_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxBT_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxBT_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxBT_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxBT_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxBT_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxBT_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxBT_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxBT_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxBT_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxBT_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxBT_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxBT_AutoDetectSignal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxBT_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxBT_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxBT_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxBT_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_CfgFrequencyChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 standard,
   int32 channelNumber
);

int32 __stdcall RFmxBT_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxBT_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxBT_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxBT_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxBT_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxBT_TXPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_TXPCfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxBT_ModAccCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_ModAccCfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxBT_20dBBandwidthCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_FrequencyRangeCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_FrequencyRangeCfgSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 span
);

int32 __stdcall RFmxBT_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_ACPCfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxBT_ACPCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxBT_ACPCfgOffsetChannelMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetChannelMode
);

int32 __stdcall RFmxBT_PowerRampCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_PowerRampCfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxBT_ModSpectrumCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxBT_ModSpectrumCfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxBT_CfgChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelNumber
);

int32 __stdcall RFmxBT_CfgDataRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 dataRate
);

int32 __stdcall RFmxBT_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxBT_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxBT_CfgLEDirectionFinding(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 directionFindingMode,
   float64 CTELength,
   float64 CTESlotDuration
);

int32 __stdcall RFmxBT_CfgPacketType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 packetType
);

int32 __stdcall RFmxBT_CfgPayloadBitPattern(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 payloadBitPattern
);

int32 __stdcall RFmxBT_CfgPayloadLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 payloadLengthMode,
   int32 payloadLength
);

int32 __stdcall RFmxBT_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxBT_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxBT_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxBT_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 triggerMinQuietTimeMode,
   float64 triggerMinQuietTimeDuration,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxBT_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxBT_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxBT_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxBT_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxBT_TXPFetchLECTETransmitSlotPowersArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 transmitSlotAveragePowerMean[],
   float64 transmitSlotPeakAbsolutePowerDeviationMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_TXPFetchPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 power[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_TXPFetchEDRPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* EDRGFSKAveragePowerMean,
   float64* EDRDPSKAveragePowerMean,
   float64* EDR_DPSK_GFSKAveragePowerRatioMean
);

int32 __stdcall RFmxBT_TXPFetchLECTEReferencePeriodPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* referencePeriodAveragePowerMean,
   float64* referencePeriodPeakAbsolutePowerDeviationMaximum
);

int32 __stdcall RFmxBT_TXPFetchLECTETransmitSlotPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* transmitSlotAveragePowerMean,
   float64* transmitSlotPeakAbsolutePowerDeviationMaximum
);

int32 __stdcall RFmxBT_TXPFetchPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averagePowerMean,
   float64* averagePowerMaximum,
   float64* averagePowerMinimum,
   float64* peakToAveragePowerRatioMaximum
);

int32 __stdcall RFmxBT_ModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchCSDetrendedPhaseTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 CSDetrendedPhase[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchCSToneTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 CSToneAmplitude[],
   float32 CSTonePhase[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDemodulatedBitTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 demodulatedBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 DEVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 EVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDf1maxTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 df1max[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDf2maxTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 df2max[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDf4avgTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 df4avg[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorTraceBR(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 frequencyError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorTraceLE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 frequencyError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorWiPlusW0TraceEDR(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 time[],
   float32 frequencyErrorWiPlusW0[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 frequency[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchRMSDEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 RMSDEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ModAccFetchDEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakRMSDEVMMaximum,
   float64* peakDEVMMaximum,
   float64* ninetyninePercentDEVM
);

int32 __stdcall RFmxBT_ModAccFetchDEVMMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averageRMSMagnitudeErrorMean,
   float64* peakRMSMagnitudeErrorMaximum
);

int32 __stdcall RFmxBT_ModAccFetchDEVMPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averageRMSPhaseErrorMean,
   float64* peakRMSPhaseErrorMaximum
);

int32 __stdcall RFmxBT_ModAccFetchDf1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* df1avgMaximum,
   float64* df1avgMinimum
);

int32 __stdcall RFmxBT_ModAccFetchDf2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* df2avgMinimum,
   float64* percentageOfSymbolsAboveDf2maxThreshold
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorBR(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* initialFrequencyErrorMaximum,
   float64* peakFrequencyDriftMaximum,
   float64* peakFrequencyDriftRateMaximum
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorEDR(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* headerFrequencyErrorWiMaximum,
   float64* peakFrequencyErrorWiPlusW0Maximum,
   float64* peakFrequencyErrorW0Maximum
);

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorLE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakFrequencyErrorMaximum,
   float64* initialFrequencyDriftMaximum,
   float64* peakFrequencyDriftMaximum,
   float64* peakFrequencyDriftRateMaximum
);

int32 __stdcall RFmxBT_20dBBandwidthFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_20dBBandwidthFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakPower,
   float64* bandwidth,
   float64* highFrequency,
   float64* lowFrequency
);

int32 __stdcall RFmxBT_FrequencyRangeFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_FrequencyRangeFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* highFrequency,
   float64* lowFrequency
);

int32 __stdcall RFmxBT_ACPFetchAbsolutePowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 absolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ACPFetchMaskTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 limitWithExceptionMask[],
   float32 limitWithoutExceptionMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ACPFetchOffsetMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerMargin[],
   float64 upperMargin[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_ACPFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxBT_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerMargin,
   float64* upperMargin
);

int32 __stdcall RFmxBT_ACPFetchReferenceChannelPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* referenceChannelPower
);

int32 __stdcall RFmxBT_ModSpectrumFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxBT_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxBT_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxBT_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxBT_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxBT_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxBT_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxBT_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetPacketType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetPacketType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetDataRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetDataRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetBandwidthBitPeriodProduct(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetBandwidthBitPeriodProduct(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetBDAddressLAP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetBDAddressLAP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetAccessAddress(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetAccessAddress(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetPayloadBitPattern(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetPayloadBitPattern(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetPayloadLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetPayloadLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetPayloadLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetPayloadLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetDirectionFindingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetDirectionFindingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetCTELength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetCTELength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetCTESlotDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetCTESlotDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetCTENumberOfTransmitSlots(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingPacketFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingPacketFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingSyncSequence(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingSyncSequence(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingPhaseMeasurementPeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingPhaseMeasurementPeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingToneExtensionSlot(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingToneExtensionSlot(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingNumberOfAntennaPath(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingNumberOfAntennaPath(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetChannelSoundingAntennaSwitchTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetChannelSoundingAntennaSwitchTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetAutoPreambleDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetAutoPreambleDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetZadoffChuIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetZadoffChuIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetHighDataThroughputPacketFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetHighDataThroughputPacketFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetVHDTModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetVHDTModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetNumberOfBlockRepetitionSequences(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetNumberOfBlockRepetitionSequences(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetFrequencyBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetFrequencyBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetDetectedPacketType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_GetDetectedDataRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_GetDetectedPayloadLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_GetDetectedPacketFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetIQOriginOffsetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetIQOriginOffsetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetIQMismatchCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetIQMismatchCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetFrequencyTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetFrequencyTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf1avgMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf1avgMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf1avgMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakDf1maxMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsMinimumDf1maxMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPercentageOfSymbolsAboveDf1maxThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf2avgMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf2avgMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf2avgMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakDf2maxMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsMinimumDf2maxMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPercentageOfSymbolsAboveDf2maxThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsDf3avgMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPercentageOfSymbolsAboveDf4avgThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsBRInitialFrequencyErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsBRPeakFrequencyDriftMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsBRPeakFrequencyDriftRateMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsEDRHeaderFrequencyErrorWiMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsEDRPeakFrequencyErrorWiPlusW0Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsEDRPeakFrequencyErrorW0Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsLEInitialFrequencyErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsLEPeakFrequencyErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsLEInitialFrequencyDriftMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsLEPeakFrequencyDriftMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsLEPeakFrequencyDriftRateMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPreambleFrequencyErrorW0Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPayloadFrequencyErrorW1Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsFrequencyErrorW0PlusW1Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakRMSDEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsRMSDEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakDEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResults99PercentDEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPercentageOfSymbolsBelow99PercentDEVMLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsAverageRMSMagnitudeErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakRMSMagnitudeErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsAverageRMSPhaseErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPeakRMSPhaseErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPreambleRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsControlHeaderRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPayloadRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsIQGainImbalanceMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsQuadratureErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsClockDriftMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsPreambleStartTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModAccGetResultsFractionalTimeOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetOffsetChannelMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetOffsetChannelMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetReferenceChannelBandwidthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetReferenceChannelBandwidthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetReferenceChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPSetReferenceChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_ACPGetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsReferenceChannelPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ACPGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetResultsPeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetResultsBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetResultsHighFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_20dBBandwidthGetResultsLowFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetResultsHighFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_FrequencyRangeGetResultsLowFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetResultsBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetResultsHighFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_ModSpectrumGetResultsLowFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_TXPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsAveragePowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsAveragePowerMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsPeakToAveragePowerRatioMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsEDRGFSKAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsEDRDPSKAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsEDR_DPSK_GFSKAveragePowerRatioMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsLECTEReferencePeriodAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsLECTEReferencePeriodPeakAbsolutePowerDeviationMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsLECTETransmitSlotAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsLECTETransmitSlotPeakAbsolutePowerDeviationMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_TXPGetResultsLECSPhaseMeasurementPeriodAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_PowerRampGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_PowerRampSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_PowerRampGetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_PowerRampSetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_PowerRampGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_PowerRampSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_PowerRampGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_PowerRampSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_PowerRampGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxBT_PowerRampSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxBT_PowerRampGetResultsRiseTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_PowerRampGetResultsFallTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_PowerRampGetResults40dBRiseTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxBT_PowerRampGetResults40dBFallTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

// Values for RFMXBT_ATTR_DIRECTION_FINDING_MODE
#define RFMXBT_VAL_DIRECTION_FINDING_MODE_ENABLED                                                 1

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxBT_CfgDirectionFinding(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 directionFindingMode,
   float64 CTELength
);

int32 __stdcall RFmxBT_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxBT_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxCDMA2k.h sha256=6006936e43e3d9b624751e21eec0292cfbb15718f707833511568c48c87ad53a bytes=138939 -->
## FILE: imports/include/niRFmxCDMA2k.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxCDMA2k.h`
- sha256: `6006936e43e3d9b624751e21eec0292cfbb15718f707833511568c48c87ad53a`
- bytes: 138939

````c

/****************************************************************************************************
*          National Instruments RFmx CDMA2k
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2023.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxCDMA2k.h
*
* Purpose:  National Instruments RFmx CDMA2k,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_CDMA2K_H__
#define __NI_RFMX_CDMA2K_H__

#include "niRFmxInstr.h"

#define RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_ENABLED                              0x00611000
#define RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE                             0x00611005
#define RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET                               0x00611006
#define RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH                               0x00611007
#define RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED                                0x00611009
#define RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED                        0x00611008
#define RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                0x006110a1
#define RFMXCDMA2K_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED              0x006110a2
#define RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED                           0x006110a3
#define RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED                     0x00611010
#define RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED                               0x00611015
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_EVM                                  0x00611020
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM                                 0x00611021
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR                      0x00611022
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR                          0x00611023
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_RHO                                      0x00611028
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET                         0x00611024
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE                        0x00611025
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR                      0x00611026
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_FREQUENCY_ERROR                          0x00611027
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR                          0x00611033
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE                                 0x00611029
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_WALSH_CODE_NUMBER               0x0061102b
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH                          0x00611038
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE                          0x0061102c
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH        0x0061102d
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER        0x0061102f
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH                   0x00611039
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_SLOT_TIMING_ERROR                        0x00611030
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS              0x00611034
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH               0x00611035
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER               0x00611036
#define RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH                          0x00611037
#define RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED                                 0x00601000
#define RFMXCDMA2K_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH                       0x00601005
#define RFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETS                                   0x00601008
#define RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCY                                    0x0060100a
#define RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH                        0x0060100e
#define RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH                           0x0060101b
#define RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTH                                0x0060101c
#define RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE                                     0x0060101d
#define RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_AUTO                                     0x0060101e
#define RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL                                 0x0060101f
#define RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD                                  0x00601012
#define RFMXCDMA2K_ATTR_ACP_NOISE_COMPENSATION_ENABLED                          0x00601020
#define RFMXCDMA2K_ATTR_ACP_AVERAGING_ENABLED                                   0x00601016
#define RFMXCDMA2K_ATTR_ACP_AVERAGING_COUNT                                     0x00601015
#define RFMXCDMA2K_ATTR_ACP_AVERAGING_TYPE                                      0x00601018
#define RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP_MODE                                    0x00601039
#define RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP                                         0x0060103a
#define RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO                         0x00601034
#define RFMXCDMA2K_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET                         0x00601035
#define RFMXCDMA2K_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET                          0x00601036
#define RFMXCDMA2K_ATTR_ACP_ALL_TRACES_ENABLED                                  0x00601021
#define RFMXCDMA2K_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                          0x00601014
#define RFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER                      0x00601026
#define RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                 0x0060102c
#define RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                 0x0060102d
#define RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                 0x00601032
#define RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                 0x00601033
#define RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE                                 0x00601038
#define RFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLED                                 0x00603000
#define RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTH                               0x00603002
#define RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH                           0x0060300c
#define RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH                                0x0060300d
#define RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE                                     0x0060300e
#define RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO                                     0x00603011
#define RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVAL                                 0x00603012
#define RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED                                   0x00603007
#define RFMXCDMA2K_ATTR_CHP_AVERAGING_COUNT                                     0x00603006
#define RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE                                      0x00603009
#define RFMXCDMA2K_ATTR_CHP_ALL_TRACES_ENABLED                                  0x00603014
#define RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS                          0x00603003
#define RFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER                      0x00603015
#define RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLED                                 0x00606000
#define RFMXCDMA2K_ATTR_OBW_SPAN                                                0x00606004
#define RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH                           0x0060600c
#define RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH                                0x0060600d
#define RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE                                     0x0060600e
#define RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO                                     0x0060600f
#define RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL                                 0x00606010
#define RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED                                   0x00606007
#define RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT                                     0x00606006
#define RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE                                      0x00606009
#define RFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLED                                  0x00606012
#define RFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS                          0x00606003
#define RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH                          0x00606013
#define RFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWER                              0x00606014
#define RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY                             0x00606015
#define RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY                              0x00606016
#define RFMXCDMA2K_ATTR_SEM_MEASUREMENT_ENABLED                                 0x00608000
#define RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH                       0x00608005
#define RFMXCDMA2K_ATTR_SEM_NUMBER_OF_OFFSETS                                   0x0060800b
#define RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY                              0x00608014
#define RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY                               0x00608015
#define RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH                         0x00608017
#define RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_TYPE                              0x00608018
#define RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL                           0x0060800c
#define RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO                                     0x00608025
#define RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL                                 0x00608026
#define RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED                                   0x0060801f
#define RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT                                     0x0060801e
#define RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE                                      0x00608021
#define RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED                                  0x00608027
#define RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                          0x0060801d
#define RFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUS                          0x00608029
#define RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER           0x0060802d
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS             0x0060803d
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER      0x00608034
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER      0x00608035
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER            0x00608036
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER            0x00608037
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                 0x00608038
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                         0x00608039
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER          0x0060803a
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER          0x0060803b
#define RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY               0x0060803c
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS             0x0060804a
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER      0x00608041
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER      0x00608042
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER            0x00608043
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER            0x00608044
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                 0x00608045
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                         0x00608046
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER          0x00608047
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER          0x00608048
#define RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY               0x00608049
#define RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED                                0x00612000
#define RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH                                 0x00612002
#define RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED                                  0x00612003
#define RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT                                    0x00612004
#define RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED                                  0x00612005
#define RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED                          0x00612006
#define RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                  0x00612007
#define RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED                0x00612008
#define RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED                             0x00612009
#define RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED                                 0x0061200a
#define RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS                         0x0061200b
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_RMS_EVM                               0x0061200d
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM                            0x0061200e
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM                              0x0061200f
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM                           0x00612010
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR                       0x00612011
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR                    0x00612012
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR                           0x00612013
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR                        0x00612014
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR                       0x00612015
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR                    0x00612016
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET                      0x00612017
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET                   0x00612018
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE                     0x00612019
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE                  0x0061201a
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR                   0x0061201b
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR                0x0061201c
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR                       0x0061201d
#define RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR                    0x0061201e
#define RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE                            0x0060d003
#define RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT                                    0x0060c000
#define RFMXCDMA2K_ATTR_CENTER_FREQUENCY                                        0x00600001
#define RFMXCDMA2K_ATTR_REFERENCE_LEVEL                                         0x00600002
#define RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION                                    0x00600003
#define RFMXCDMA2K_ATTR_TRIGGER_TYPE                                            0x00600004
#define RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                             0x00600005
#define RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                               0x00600006
#define RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                            0x00600007
#define RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                             0x00600008
#define RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                        0x00600fff
#define RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                             0x00600009
#define RFMXCDMA2K_ATTR_TRIGGER_DELAY                                           0x0060000a
#define RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                         0x0060000b
#define RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                     0x0060000c
#define RFMXCDMA2K_ATTR_LINK_DIRECTION                                          0x0060000d
#define RFMXCDMA2K_ATTR_BAND_CLASS                                              0x00600010
#define RFMXCDMA2K_ATTR_RADIO_CONFIGURATION                                     0x00600011
#define RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE                              0x00600012
#define RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELS                                      0x00600016
#define RFMXCDMA2K_ATTR_WALSH_CODE_LENGTH                                       0x00600017
#define RFMXCDMA2K_ATTR_WALSH_CODE_NUMBER                                       0x00600018
#define RFMXCDMA2K_ATTR_BRANCH                                                  0x00600019
#define RFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASK                         0x0060001e
#define RFMXCDMA2K_ATTR_DOWNLINK_SPREADING_PN_OFFSET                            0x00600020
#define RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                      0x0060d000
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_ENABLED                                 0x00613000
#define RFMXCDMA2K_ATTR_CDA_SYNCHRONIZATION_MODE                                0x00613002
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_OFFSET                                  0x00613003
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_LENGTH                                  0x00613004
#define RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR                               0x00613005
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_LENGTH               0x00613006
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_NUMBER               0x00613007
#define RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH                          0x00613008
#define RFMXCDMA2K_ATTR_CDA_POWER_UNIT                                          0x00613009
#define RFMXCDMA2K_ATTR_CDA_SPECTRUM_INVERTED                                   0x0061300a
#define RFMXCDMA2K_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED                           0x0061300b
#define RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                   0x0061300c
#define RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED                 0x0061300d
#define RFMXCDMA2K_ATTR_CDA_RECEIVE_FILTER_ENABLED                              0x0061300e
#define RFMXCDMA2K_ATTR_CDA_ALL_TRACES_ENABLED                                  0x0061300f
#define RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM                              0x00613012
#define RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM                             0x00613013
#define RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR                  0x00613014
#define RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR                      0x00613015
#define RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER                           0x00613016
#define RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER                                 0x00613017
#define RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER                          0x00613018
#define RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER                           0x00613019
#define RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER                           0x0061301a
#define RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER                         0x0061301b
#define RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER                         0x0061301c
#define RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER                         0x0061301d
#define RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER                       0x0061301e
#define RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER                         0x0061301f
#define RFMXCDMA2K_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER                       0x00613020
#define RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER                            0x00613021
#define RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET                            0x00613022
#define RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE                           0x00613023
#define RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR                         0x00613024
#define RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERROR                             0x00613025
#define RFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERROR                             0x00613026
#define RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED                           0x00614000
#define RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE                          0x00614002
#define RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET                            0x00614003
#define RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH                            0x00614004
#define RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED                             0x00614005
#define RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED                        0x00614006
#define RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_ENABLED                           0x00615000
#define RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE                          0x00615002
#define RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_OFFSET                            0x00615003
#define RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_LENGTH                            0x00615004
#define RFMXCDMA2K_ATTR_SLOTPHASE_SPECTRUM_INVERTED                             0x00615005
#define RFMXCDMA2K_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED                        0x00615006
#define RFMXCDMA2K_ATTR_SLOTPHASE_TRANSIENT_DURATION                            0x00615007
#define RFMXCDMA2K_ATTR_SLOTPHASE_ALL_TRACES_ENABLED                            0x00615008
#define RFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY           0x0061500b
#define RFMXCDMA2K_ATTR_SELECTED_PORTS                                          0x00600ffd
#define RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM                                0x00600ffc

// Values for RFMXCDMA2K_ATTR_TRIGGER_TYPE
#define RFMXCDMA2K_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXCDMA2K_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXCDMA2K_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXCDMA2K_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXCDMA2K_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXCDMA2K_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXCDMA2K_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXCDMA2K_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXCDMA2K_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXCDMA2K_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXCDMA2K_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXCDMA2K_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXCDMA2K_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXCDMA2K_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXCDMA2K_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXCDMA2K_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXCDMA2K_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXCDMA2K_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXCDMA2K_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXCDMA2K_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXCDMA2K_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXCDMA2K_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXCDMA2K_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXCDMA2K_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXCDMA2K_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXCDMA2K_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXCDMA2K_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXCDMA2K_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXCDMA2K_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXCDMA2K_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXCDMA2K_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXCDMA2K_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXCDMA2K_ATTR_LINK_DIRECTION
#define RFMXCDMA2K_VAL_LINK_DIRECTION_DOWNLINK                                                        0
#define RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for RFMXCDMA2K_ATTR_RADIO_CONFIGURATION
#define RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC1                                                        0
#define RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC2                                                        1
#define RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3                                                        2
#define RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC4                                                        3
#define RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC5                                                        4

// Values for RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE
#define RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT                                         0
#define RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                                        1

// Values for RFMXCDMA2K_ATTR_BRANCH
#define RFMXCDMA2K_VAL_BRANCH_I                                                                       0
#define RFMXCDMA2K_VAL_BRANCH_Q                                                                       1
#define RFMXCDMA2K_VAL_BRANCH_I_AND_Q                                                                 2

// Values for RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE
#define RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME                                              0
#define RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT                                               1
#define RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY                                          2

// Values for RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED
#define RFMXCDMA2K_VAL_MODACC_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXCDMA2K_VAL_MODACC_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                         0
#define RFMXCDMA2K_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                          1

// Values for RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                 0
#define RFMXCDMA2K_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                  1

// Values for RFMXCDMA2K_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                               0
#define RFMXCDMA2K_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                1

// Values for RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED
#define RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE                                            0
#define RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE                                             1

// Values for RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED
#define RFMXCDMA2K_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE                                      0
#define RFMXCDMA2K_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE                                       1

// Values for RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH
#define RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I                                                       0
#define RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_Q                                                       1
#define RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q                                                 2

// Values for RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH
#define RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I                                                0
#define RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q                                                1
#define RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q                                          2

// Values for RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH
#define RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I                                                       0
#define RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q                                                       1
#define RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q                                                 2

// Values for RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXCDMA2K_VAL_ACP_RBW_AUTO_FALSE                                                             0
#define RFMXCDMA2K_VAL_ACP_RBW_AUTO_TRUE                                                              1

// Values for RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE
#define RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_AUTO
#define RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD
#define RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1
#define RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT                                          2

// Values for RFMXCDMA2K_ATTR_ACP_NOISE_COMPENSATION_ENABLED
#define RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXCDMA2K_ATTR_ACP_AVERAGING_ENABLED
#define RFMXCDMA2K_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXCDMA2K_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXCDMA2K_ATTR_ACP_AVERAGING_TYPE
#define RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_RMS                                                         0
#define RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_LOG                                                         1
#define RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP_MODE
#define RFMXCDMA2K_VAL_ACP_FFT_OVERLAP_MODE_DISABLED                                                  0
#define RFMXCDMA2K_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC                                                 1

// Values for RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO
#define RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE                                          0
#define RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE                                           1

// Values for RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE                                                             0
#define RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE                                                              1

// Values for RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE
#define RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO
#define RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED
#define RFMXCDMA2K_VAL_CHP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXCDMA2K_VAL_CHP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE
#define RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_RMS                                                         0
#define RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_LOG                                                         1
#define RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXCDMA2K_VAL_OBW_RBW_AUTO_FALSE                                                             0
#define RFMXCDMA2K_VAL_OBW_RBW_AUTO_TRUE                                                              1

// Values for RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE
#define RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO
#define RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED
#define RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE
#define RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_RMS                                                         0
#define RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_LOG                                                         1
#define RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_TYPE
#define RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED                                           0
#define RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN                                            1
#define RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT                                                2
#define RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4                                       3
#define RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5                                       4

// Values for RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED
#define RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE
#define RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUS
#define RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED
#define RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE                                                   0
#define RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE                                                    1

// Values for RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED
#define RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_FALSE                                                   0
#define RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_TRUE                                                    1

// Values for RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                           0
#define RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                            1

// Values for RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                   0
#define RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                    1

// Values for RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                                 0
#define RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                  1

// Values for RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED
#define RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_FALSE                                              0
#define RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_TRUE                                               1

// Values for RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for Boolean
#define RFMXCDMA2K_VAL_FALSE                                                                          0
#define RFMXCDMA2K_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXCDMA2K_VAL_MODACC                                                                         1 << 0
#define RFMXCDMA2K_VAL_ACP                                                                            1 << 1
#define RFMXCDMA2K_VAL_CHP                                                                            1 << 2
#define RFMXCDMA2K_VAL_OBW                                                                            1 << 3
#define RFMXCDMA2K_VAL_SEM                                                                            1 << 4
#define RFMXCDMA2K_VAL_QEVM                                                                           1 << 5
#define RFMXCDMA2K_VAL_CDA                                                                            1 << 6
#define RFMXCDMA2K_VAL_SLOTPHASE                                                                      1 << 7
#define RFMXCDMA2K_VAL_SLOTPOWER                                                                      1 << 8

// Values for FrequencyReferenceSource
#define RFMXCDMA2K_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXCDMA2K_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXCDMA2K_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXCDMA2K_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for RFMXCDMA2K_ATTR_LINK_DIRECTION
#define RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for MechanicalAttenuationAuto
#define RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

// Values for RFAttenuationAuto
#define RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for RFMXCDMA2K_ATTR_CDA_SYNCHRONIZATION_MODE
#define RFMXCDMA2K_VAL_CDA_SYNCHRONIZATION_MODE_FRAME                                                 0
#define RFMXCDMA2K_VAL_CDA_SYNCHRONIZATION_MODE_SLOT                                                  1
#define RFMXCDMA2K_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY                                             2

// Values for RFMXCDMA2K_ATTR_CDA_POWER_UNIT
#define RFMXCDMA2K_VAL_CDA_POWER_UNIT_DB                                                              0
#define RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM                                                             1

// Values for RFMXCDMA2K_ATTR_CDA_SPECTRUM_INVERTED
#define RFMXCDMA2K_VAL_CDA_SPECTRUM_INVERTED_FALSE                                                    0
#define RFMXCDMA2K_VAL_CDA_SPECTRUM_INVERTED_TRUE                                                     1

// Values for RFMXCDMA2K_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                            0
#define RFMXCDMA2K_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                             1

// Values for RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                    0
#define RFMXCDMA2K_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                     1

// Values for RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH
#define RFMXCDMA2K_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_I                                               0
#define RFMXCDMA2K_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_Q                                               1

// Values for RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                                  0
#define RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                   1

// Values for RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE
#define RFMXCDMA2K_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXCDMA2K_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED
#define RFMXCDMA2K_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXCDMA2K_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED
#define RFMXCDMA2K_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_FALSE                                         0
#define RFMXCDMA2K_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE                                          1

// Values for RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE
#define RFMXCDMA2K_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXCDMA2K_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXCDMA2K_ATTR_SLOTPHASE_SPECTRUM_INVERTED
#define RFMXCDMA2K_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXCDMA2K_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXCDMA2K_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED
#define RFMXCDMA2K_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_FALSE                                         0
#define RFMXCDMA2K_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE                                          1

// Values for RFMXCDMA2K_ATTR_CDA_RECEIVE_FILTER_ENABLED
#define RFMXCDMA2K_VAL_CDA_RECEIVE_FILTER_ENABLED_FALSE                                               0
#define RFMXCDMA2K_VAL_CDA_RECEIVE_FILTER_ENABLED_TRUE                                                1

/* ---------------- RFmxCDMA2k APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxCDMA2k_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxCDMA2k_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxCDMA2k_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxCDMA2k_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxCDMA2k_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxCDMA2k_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxCDMA2k_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxCDMA2k_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxCDMA2k_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxCDMA2k_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxCDMA2k_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxCDMA2k_BuildChannelString(
   char selectorString[],
   int32 channelNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxCDMA2k_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxCDMA2k_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxCDMA2k_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxCDMA2k_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* done
);

int32 __stdcall RFmxCDMA2k_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxCDMA2k_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxCDMA2k_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxCDMA2k_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxCDMA2k_AnalyzeSpectrum1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxCDMA2k_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxCDMA2k_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxCDMA2k_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxCDMA2k_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxCDMA2k_CfgFrequencyChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection,
   int32 bandClass,
   int32 channelNumber
);

int32 __stdcall RFmxCDMA2k_CfgBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 bandClass
);

int32 __stdcall RFmxCDMA2k_CfgChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelConfigurationMode
);

int32 __stdcall RFmxCDMA2k_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxCDMA2k_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxCDMA2k_CfgNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfChannels
);

int32 __stdcall RFmxCDMA2k_CfgRadioConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 radioConfiguration
);

int32 __stdcall RFmxCDMA2k_CfgUplinkSpreading(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 uplinkSpreadingLongCodeMask
);

int32 __stdcall RFmxCDMA2k_CfgUserDefinedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 walshCodeLength,
   int32 walshCodeNumber,
   int32 branch
);

int32 __stdcall RFmxCDMA2k_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxCDMA2k_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxCDMA2k_CfgUserDefinedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 walshCodeLength[],
   int32 walshCodeNumber[],
   int32 branch[],
   int32 numberOfElements
);

int32 __stdcall RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxCDMA2k_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxCDMA2k_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxCDMA2k_QEVMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxCDMA2k_QEVMCfgMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementLength
);

int32 __stdcall RFmxCDMA2k_CHPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxCDMA2k_CHPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxCDMA2k_CHPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxCDMA2k_OBWCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxCDMA2k_OBWCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxCDMA2k_OBWCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxCDMA2k_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxCDMA2k_ACPCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxCDMA2k_ACPCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxCDMA2k_ACPCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxCDMA2k_ACPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxCDMA2k_ACPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxCDMA2k_CDACfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxCDMA2k_CDACfgMeasurementChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 walshCodeLength,
   int32 walshCodeNumber,
   int32 branch
);

int32 __stdcall RFmxCDMA2k_CDACfgPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerUnit
);

int32 __stdcall RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxCDMA2k_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxCDMA2k_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxCDMA2k_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxCDMA2k_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxCDMA2k_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 minimumQuietTimeMode,
   float64 minimumQuietTime,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxCDMA2k_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxCDMA2k_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxCDMA2k_QEVMFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_QEVMFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_QEVMFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSEVM,
   float64* maximumPeakEVM,
   float64* meanFrequencyError,
   float64* meanMagnitudeError,
   float64* meanPhaseError,
   float64* meanChipRateError
);

int32 __stdcall RFmxCDMA2k_QEVMFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanIQOriginOffset,
   float64* meanIQGainImbalance,
   float64* meanIQQuadratureError,
   float64* maximumIQOriginOffset,
   float64* maximumIQGainImbalance,
   float64* maximumIQQuadratureError
);

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SEMFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   float32 relativeMask[],
   float32 absoluteMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* carrierAbsoluteIntegratedPower
);

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxCDMA2k_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 detectedWalshCodeLength[],
   int32 detectedWalshCodeNumber[],
   int32 detectedBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* detectedWalshCodeLength,
   int32* detectedWalshCodeNumber,
   int32* detectedBranch
);

int32 __stdcall RFmxCDMA2k_ModAccFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSEVM,
   float64* peakEVM,
   float64* rho,
   float64* frequencyError,
   float64* chipRateError,
   float64* RMSMagnitudeError,
   float64* RMSPhaseError
);

int32 __stdcall RFmxCDMA2k_ModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffset,
   float64* IQGainImbalance,
   float64* IQQuadratureError
);

int32 __stdcall RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfDetectedChannels
);

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakActiveCDE,
   int32* peakActiveCDEWalshCodeLength,
   int32* peakActiveCDEWalshCodeNumber,
   int32* peakActiveCDEBranch
);

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakCDE,
   int32* peakCDEWalshCodeNumber,
   int32* peakCDEBranch
);

int32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ACPFetchRelativePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 relativePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ACPFetchAbsolutePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 absolutePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower
);

int32 __stdcall RFmxCDMA2k_ACPFetchCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* carrierAbsolutePower
);

int32 __stdcall RFmxCDMA2k_CHPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CHPFetchCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* carrierAbsolutePower
);

int32 __stdcall RFmxCDMA2k_OBWFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_OBWFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* occupiedBandwidth,
   float64* absolutePower,
   float64* startFrequency,
   float64* stopFrequency
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolMagnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 ICodeDomainPowers[],
   float32 QCodeDomainPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle symbolConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolConstellationI[],
   float32 symbolConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_CDAFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffset,
   float64* IQGainImbalance,
   float64* IQQuadratureError
);

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSSymbolEVM,
   float64* peakSymbolEVM,
   float64* RMSSymbolMagnitudeError,
   float64* RMSSymbolPhaseError,
   float64* meanSymbolPower,
   float64* frequencyError,
   float64* chipRateError
);

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalPower,
   float64* totalActivePower,
   float64* meanActivePower,
   float64* peakActivePower,
   float64* meanInactivePower,
   float64* peakInactivePower
);

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IMeanActivePower,
   float64* QMeanActivePower,
   float64* IPeakInactivePower,
   float64* QPeakInactivePower
);

int32 __stdcall RFmxCDMA2k_SlotPowerFetchPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotPower[],
   float64 slotPowerDelta[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotPhaseDiscontinuity[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseErrorLinearFit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumPhaseDiscontinuity
);

int32 __stdcall RFmxCDMA2k_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsRMSMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsRMSPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsRho(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakCDEWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakActiveCDEWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakActiveCDEWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsPeakActiveCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsSlotTimingError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsDetectedWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsDetectedWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ModAccGetResultsDetectedBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAdvancedIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAdvancedIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAdvancedNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAdvancedNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAdvancedFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAdvancedFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPGetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_ACPSetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CHPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CHPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetResultsOccupiedBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetResultsAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetResultsStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_OBWGetResultsStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMeanChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_QEVMGetResultsMaximumChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetRadioConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetRadioConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetUplinkSpreadingLongCodeMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetUplinkSpreadingLongCodeMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetDownlinkSpreadingPNOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetDownlinkSpreadingPNOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxCDMA2k_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetBaseSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetBaseSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementChannelWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementChannelWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementChannelWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementChannelWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetMeasurementChannelBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetMeasurementChannelBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDASetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsRMSSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsPeakSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsRMSSymbolMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsRMSSymbolPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsMeanSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsTotalPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsTotalActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsPeakActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsMeanInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsIMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsIPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsQMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsQPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsMeanPilotPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_CDAGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPowerSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetTransientDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetTransientDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxCDMA2k_SlotPhaseGetResultsMaximumPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxCDMA2k_CalculateFrequencyFromChannelNumber(
   int32 linkDirection,
   int32 bandClass,
   int32 channelNumber,
   float64* centerFrequency
);

int32 __stdcall RFmxCDMA2k_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxCDMA2k_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxCDMA2k_AnalyzeSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxDemod.h sha256=50c4a74ffab44134889e659bc3299906be14a6e85548b8479e419a6fbc2e32f5 bytes=96562 -->
## FILE: imports/include/niRFmxDemod.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxDemod.h`
- sha256: `50c4a74ffab44134889e659bc3299906be14a6e85548b8479e419a6fbc2e32f5`
- bytes: 96562

````c

/****************************************************************************************************
*          National Instruments RFmx Demod
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2021.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxDemod.h
*
* Purpose:  National Instruments RFmx Demod,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_DEMOD_H__
#define __NI_RFMX_DEMOD_H__

#include "niRFmxInstr.h"

#define RFMXDEMOD_ATTR_SELECTED_PORTS                                                     0x00202ffd
#define RFMXDEMOD_ATTR_CENTER_FREQUENCY                                                   0x00202001
#define RFMXDEMOD_ATTR_REFERENCE_LEVEL                                                    0x00202003
#define RFMXDEMOD_ATTR_EXTERNAL_ATTENUATION                                               0x00202002
#define RFMXDEMOD_ATTR_REFERENCE_LEVEL_HEADROOM                                           0x00202ffc
#define RFMXDEMOD_ATTR_TRIGGER_TYPE                                                       0x00202004
#define RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                        0x00202005
#define RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                          0x00202006
#define RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                       0x00202007
#define RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                        0x00202008
#define RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                                   0x00202fff
#define RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                        0x00202009
#define RFMXDEMOD_ATTR_TRIGGER_DELAY                                                      0x0020200a
#define RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                    0x0020200b
#define RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                                0x0020200c
#define RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLED                                         0x00200039
#define RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED                                   0x00200040
#define RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE                                             0x0020000e
#define RFMXDEMOD_ATTR_ADEMOD_AM_CARRIER_SUPPRESSED                                       0x00200002
#define RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE                                             0x00200010
#define RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_BANDWIDTH                                        0x00200011
#define RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA                                            0x00200012
#define RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVAL                                        0x0020000d
#define RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED                        0x0020000a
#define RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_PHASE_ENABLED                            0x0020000b
#define RFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASIS                                               0x0020000c
#define RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE                                           0x00200003
#define RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_LOWER_CUTOFF_FREQUENCY                         0x00200004
#define RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY                         0x00200005
#define RFMXDEMOD_ATTR_ADEMOD_AVERAGING_ENABLED                                           0x00200006
#define RFMXDEMOD_ATTR_ADEMOD_AVERAGING_COUNT                                             0x00200007
#define RFMXDEMOD_ATTR_ADEMOD_AVERAGING_TYPE                                              0x00200009
#define RFMXDEMOD_ATTR_ADEMOD_ALL_TRACES_ENABLED                                          0x00200013
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_CARRIER_FREQUENCY_ERROR                        0x00200014
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_CARRIER_POWER                                  0x00200015
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCY                           0x00200016
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_SINAD                                       0x00200017
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISE                              0x00200018
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD                                         0x00200019
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_SNR                                         0x0020001a
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION         0x0020001b
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK          0x0020001c
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK              0x0020001d
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK              0x0020001e
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_RMS                        0x0020001f
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION      0x00200020
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_HALF_PEAK_TO_PEAK       0x00200021
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK           0x00200022
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK           0x00200023
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS                     0x00200024
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATION                0x00200025
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK                 0x00200026
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_POSITIVE_PEAK                     0x00200027
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAK                     0x00200028
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_RMS                               0x00200029
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_STANDARD_DEVIATION             0x0020002a
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_HALF_PEAK_TO_PEAK              0x0020002b
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_POSITIVE_PEAK                  0x0020002c
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_NEGATIVE_PEAK                  0x0020002d
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_RMS                            0x0020002e
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATION                0x0020002f
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK                 0x00200030
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAK                     0x00200031
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAK                     0x00200032
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMS                               0x00200033
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_STANDARD_DEVIATION             0x00200034
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_HALF_PEAK_TO_PEAK              0x00200035
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_POSITIVE_PEAK                  0x00200036
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_NEGATIVE_PEAK                  0x00200037
#define RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMS                            0x00200038
#define RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_ENABLED                                         0x00201000
#define RFMXDEMOD_ATTR_DDEMOD_MODULATION_TYPE                                             0x0020100b
#define RFMXDEMOD_ATTR_DDEMOD_M                                                           0x00201009
#define RFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTED                                           0x00201012
#define RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT                                                  0x0020100e
#define RFMXDEMOD_ATTR_DDEMOD_DIFFERENTIAL_ENABLED                                        0x00201005
#define RFMXDEMOD_ATTR_DDEMOD_SYMBOL_RATE                                                 0x00201013
#define RFMXDEMOD_ATTR_DDEMOD_NUMBER_OF_SYMBOLS                                           0x0020100d
#define RFMXDEMOD_ATTR_DDEMOD_SAMPLES_PER_SYMBOL                                          0x00201011
#define RFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCE                                 0x00201039
#define RFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATION                                               0x00201008
#define RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED                          0x00201038
#define RFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIO                                         0x00201049
#define RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIO                                         0x0020104a
#define RFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPE                                             0x00201040
#define RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE                                   0x0020100f
#define RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER                              0x00201010
#define RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE                                     0x0020100a
#define RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_MODE                                              0x00201006
#define RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_FILTER_LENGTH                                     0x00201036
#define RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_TRAINING_COUNT                                    0x00201037
#define RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_CONVERGENCE_FACTOR                                0x00201007
#define RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_ENABLED                                     0x00201014
#define RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_BITS                                        0x0020101f
#define RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_MEASUREMENT_OFFSET                          0x00201034
#define RFMXDEMOD_ATTR_DDEMOD_AVERAGING_ENABLED                                           0x00201002
#define RFMXDEMOD_ATTR_DDEMOD_AVERAGING_COUNT                                             0x00201003
#define RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE                                            0x00201041
#define RFMXDEMOD_ATTR_DDEMOD_BURST_START_EXCLUSION_SYMBOLS                               0x00201042
#define RFMXDEMOD_ATTR_DDEMOD_BURST_END_EXCLUSION_SYMBOLS                                 0x00201043
#define RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED                                   0x00201044
#define RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE                                         0x00201045
#define RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO                                          0x00201047
#define RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH                                               0x00201048
#define RFMXDEMOD_ATTR_DDEMOD_ALL_TRACES_ENABLED                                          0x00201015
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_FREQUENCY_OFFSET                       0x00201021
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_FREQUENCY_DRIFT                        0x00201022
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERROR                            0x00201023
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMS                                        0x00201024
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMS                                     0x00201025
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAK                                       0x00201026
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAK                                    0x00201027
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO                     0x00201028
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_RMS                                 0x0020103a
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_PEAK                                0x0020103b
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS                              0x0020103c
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_PEAK                             0x0020103d
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_MAGNITUDE_ERROR_MEAN                                0x00201029
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_MAGNITUDE_ERROR_MAXIMUM                             0x0020102a
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN                                    0x0020102b
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM                                 0x0020102c
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION                                  0x0020102d
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR                              0x0020102e
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR                          0x0020102f
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET                0x00201032
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_GAIN_IMBALANCE               0x00201030
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW                 0x00201031
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR                                     0x0020103e
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP                                0x0020103f
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND                                          0x00201035
#define RFMXDEMOD_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                                 0x0020200d
#define RFMXDEMOD_ATTR_LIMITED_CONFIGURATION_CHANGE                                       0x0020200e
#define RFMXDEMOD_ATTR_RESULT_FETCH_TIMEOUT                                               0x00203000

// Values for RFMXDEMOD_ATTR_TRIGGER_TYPE
#define RFMXDEMOD_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXDEMOD_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXDEMOD_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXDEMOD_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXDEMOD_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXDEMOD_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXDEMOD_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXDEMOD_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXDEMOD_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXDEMOD_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXDEMOD_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXDEMOD_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXDEMOD_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXDEMOD_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXDEMOD_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXDEMOD_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXDEMOD_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXDEMOD_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXDEMOD_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXDEMOD_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXDEMOD_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXDEMOD_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXDEMOD_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXDEMOD_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXDEMOD_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXDEMOD_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXDEMOD_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXDEMOD_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXDEMOD_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXDEMOD_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_MEASUREMENT_ENABLED_FALSE                                         0
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_MEASUREMENT_ENABLED_TRUE                                          1

// Values for RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE
#define RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_AM                                                      0
#define RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_FM                                                      1
#define RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_PM                                                      2

// Values for RFMXDEMOD_ATTR_ADEMOD_AM_CARRIER_SUPPRESSED
#define RFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_FALSE                                             0
#define RFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_TRUE                                              1

// Values for RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_NONE                                                    0
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_GAUSSIAN                                                1
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_FLAT                                                    2
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_SYNCH_TUNED_4                                           3
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_SYNCH_TUNED_5                                           4
#define RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_RRC                                                     5

// Values for RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED
#define RFMXDEMOD_VAL_ADEMOD_CARRIER_FREQUENCY_CORRECTION_ENABLED_FALSE                              0
#define RFMXDEMOD_VAL_ADEMOD_CARRIER_FREQUENCY_CORRECTION_ENABLED_TRUE                               1

// Values for RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_PHASE_ENABLED
#define RFMXDEMOD_VAL_ADEMOD_CARRIER_PHASE_CORRECTION_ENABLED_FALSE                                  0
#define RFMXDEMOD_VAL_ADEMOD_CARRIER_PHASE_CORRECTION_ENABLED_TRUE                                   1

// Values for RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_NONE                                                  0
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_CUSTOM                                                1
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_A_WEIGHT                                              2
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_B_WEIGHT                                              3
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_C_WEIGHT                                              4
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_CCITT                                                 5
#define RFMXDEMOD_VAL_ADEMOD_AUDIO_FILTER_TYPE_ITU_R_468_4                                           6

// Values for RFMXDEMOD_ATTR_ADEMOD_AVERAGING_ENABLED
#define RFMXDEMOD_VAL_ADEMOD_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXDEMOD_VAL_ADEMOD_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXDEMOD_ATTR_ADEMOD_AVERAGING_TYPE
#define RFMXDEMOD_VAL_ADEMOD_AVERAGING_TYPE_LINEAR                                                   0
#define RFMXDEMOD_VAL_ADEMOD_AVERAGING_TYPE_MAXIMUM                                                  1
#define RFMXDEMOD_VAL_ADEMOD_AVERAGING_TYPE_MINIMUM                                                  2

// Values for RFMXDEMOD_ATTR_DDEMOD_MODULATION_TYPE
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_ASK                                                     0
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_FSK                                                     1
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_PSK                                                     2
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_QAM                                                     3
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_MSK                                                     4
#define RFMXDEMOD_VAL_DDEMOD_MODULATION_TYPE_APSK                                                    5

// Values for RFMXDEMOD_ATTR_DDEMOD_M
#define RFMXDEMOD_VAL_DDEMOD_M_2                                                                     2
#define RFMXDEMOD_VAL_DDEMOD_M_4                                                                     4
#define RFMXDEMOD_VAL_DDEMOD_M_8                                                                     8
#define RFMXDEMOD_VAL_DDEMOD_M_16                                                                    16
#define RFMXDEMOD_VAL_DDEMOD_M_32                                                                    32
#define RFMXDEMOD_VAL_DDEMOD_M_64                                                                    64
#define RFMXDEMOD_VAL_DDEMOD_M_128                                                                   128
#define RFMXDEMOD_VAL_DDEMOD_M_256                                                                   256
#define RFMXDEMOD_VAL_DDEMOD_M_512                                                                   512
#define RFMXDEMOD_VAL_DDEMOD_M_1024                                                                  1024
#define RFMXDEMOD_VAL_DDEMOD_M_2048                                                                  2048
#define RFMXDEMOD_VAL_DDEMOD_M_4096                                                                  4096

// Values for RFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTED
#define RFMXDEMOD_VAL_DDEMOD_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXDEMOD_VAL_DDEMOD_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_NORMAL                                                       0
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_OFFSET_QPSK                                                  1
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_PI_BY_4_QPSK                                                 2
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_PI_BY_8_8PSK                                                 3
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_3PI_BY_8_8PSK                                                4
#define RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_SHAPED_OFFSET_QPSK                                           5

// Values for RFMXDEMOD_ATTR_DDEMOD_DIFFERENTIAL_ENABLED
#define RFMXDEMOD_VAL_DDEMOD_DIFFERENTIAL_ENABLED_FALSE                                              0
#define RFMXDEMOD_VAL_DDEMOD_DIFFERENTIAL_ENABLED_TRUE                                               1

// Values for RFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCE
#define RFMXDEMOD_VAL_DDEMOD_EVM_NORMALIZATION_REFERENCE_PEAK                                        0
#define RFMXDEMOD_VAL_DDEMOD_EVM_NORMALIZATION_REFERENCE_RMS                                         1

// Values for RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED
#define RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_FALSE                                0
#define RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_TRUE                                 1

// Values for RFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPE
#define RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_AUTO                                                    0
#define RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_CUSTOM                                                  1

// Values for RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_RECTANGULAR                                   0
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE                                 1
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_ROOT_RAISED_COSINE                            2
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_GAUSSIAN                                      3
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_CUSTOM                                        4
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_HALF_SINE                                     5
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_LINEARIZED_GMSK_EDGE                          6
#define RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_SOQPSK_TG                                     7

// Values for RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE
#define RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_AUTO                                            0
#define RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_CUSTOM                                          1

// Values for RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_MODE
#define RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_OFF                                                      0
#define RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_TRAIN                                                    1
#define RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_HOLD                                                     2

// Values for RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_ENABLED
#define RFMXDEMOD_VAL_DDEMOD_SYNCHRONIZATION_ENABLED_FALSE                                           0
#define RFMXDEMOD_VAL_DDEMOD_SYNCHRONIZATION_ENABLED_TRUE                                            1

// Values for RFMXDEMOD_ATTR_DDEMOD_AVERAGING_ENABLED
#define RFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE
#define RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED                                                0
#define RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS                                             1

// Values for RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXDEMOD_VAL_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                         0
#define RFMXDEMOD_VAL_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                          1

// Values for RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE
#define RFMXDEMOD_VAL_DDEMOD_CFO_ESTIMATION_MODE_NARROW                                              0
#define RFMXDEMOD_VAL_DDEMOD_CFO_ESTIMATION_MODE_WIDE                                                1

// Values for RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO
#define RFMXDEMOD_VAL_DDEMOD_SEARCH_LENGTH_AUTO_FALSE                                                0
#define RFMXDEMOD_VAL_DDEMOD_SEARCH_LENGTH_AUTO_TRUE                                                 1

// Values for RFMXDEMOD_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for FrequencyReferenceSource
#define RFMXDEMOD_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXDEMOD_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXDEMOD_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXDEMOD_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for Boolean
#define RFMXDEMOD_VAL_FALSE                                                                          0
#define RFMXDEMOD_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXDEMOD_VAL_ADEMOD                                                                         1<<0
#define RFMXDEMOD_VAL_DDEMOD                                                                         1<<1

// Values for RFAttenuationAuto
#define RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for MechanicalAttenuationAuto
#define RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

/* ---------------- RFmxDemod APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxDemod_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxDemod_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxDemod_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxDemod_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxDemod_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxDemod_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxDemod_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxDemod_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxDemod_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxDemod_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxDemod_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxDemod_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxDemod_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxDemod_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxDemod_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxDemod_DDemodCfgSymbolMap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 symbolMapType,
   NIComplexSingle symbolMap[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgSymbolMapSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 symbolMapType,
   float32 symbolMapI[],
   float32 symbolMapQ[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgEqualizerInitialCoefficients(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   NIComplexSingle equalizerInitialCoefficients[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgEqualizerInitialCoefficientsSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 equalizerInitialCoefficientsI[],
   float32 equalizerInitialCoefficientsQ[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodSetSymbolMap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodSetSymbolMapSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 attrValI[],
   float32 attrValQ[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxDemod_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 bandwidth,
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxDemod_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxDemod_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxDemod_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxDemod_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxDemod_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxDemod_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxDemod_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxDemod_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxDemod_ADemodCfgModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modulationType
);

int32 __stdcall RFmxDemod_ADemodCfgMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval
);

int32 __stdcall RFmxDemod_ADemodCfgAMCarrierSuppressed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 AMCarrierSuppressedEnabled
);

int32 __stdcall RFmxDemod_ADemodCfgAudioFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 audioFilterType,
   float64 audioFilterLowerCutoffFrequency,
   float64 audioFilterUpperCutoffFrequency
);

int32 __stdcall RFmxDemod_ADemodCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxDemod_ADemodCfgCarrierCorrection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 carrierFrequencyCorrectionEnabled,
   int32 carrierPhaseCorrectionEnabled
);

int32 __stdcall RFmxDemod_ADemodCfgFMDeEmphasis(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 deEmphasis
);

int32 __stdcall RFmxDemod_ADemodCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 RBW,
   int32 RBWFilterType,
   float64 RBWRRCAlpha
);

int32 __stdcall RFmxDemod_DDemodCfgModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modulationType,
   int32 M,
   int32 differentialEnabled
);

int32 __stdcall RFmxDemod_DDemodCfgM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 M
);

int32 __stdcall RFmxDemod_DDemodCfgNumberOfSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfSymbols
);

int32 __stdcall RFmxDemod_DDemodCfgSamplesPerSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 samplesPerSymbol
);

int32 __stdcall RFmxDemod_DDemodCfgSymbolRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 symbolRate
);

int32 __stdcall RFmxDemod_DDemodCfgPSKFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 PSKFormat
);

int32 __stdcall RFmxDemod_DDemodCfgFSKDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 FSKDeviation,
   int32 FSKRefCompEnabled
);

int32 __stdcall RFmxDemod_DDemodCfgSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 spectrumInverted
);

int32 __stdcall RFmxDemod_DDemodCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 pulseShapingFilterCustomCoefficients[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 measurementFilterCustomCoefficients[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgSynchronization(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationEnabled,
   int8 syncBits[],
   int32 measurementOffset,
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgEVMNormalizationReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 EVMNormRef
);

int32 __stdcall RFmxDemod_DDemodCfgSignalStructure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 signalStructure
);

int32 __stdcall RFmxDemod_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxDemod_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxDemod_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxDemod_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxDemod_DDemodCfgEqualizer(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 equalizerMode,
   int32 equalizerFilterLength,
   float64 x0,
   float64 dx,
   NIComplexSingle equalizerInitialCoefficients[],
   int32 equalizerTrainingCount,
   float64 equalizerConvergenceFactor,
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgEqualizerSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 equalizerMode,
   int32 equalizerFilterLength,
   float64 x0,
   float64 dx,
   float32 equalizerInitialCoefficientsI[],
   float32 equalizerInitialCoefficientsQ[],
   int32 equalizerTrainingCount,
   float64 equalizerConvergenceFactor,
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgMeasurementFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementFilterType,
   float64 x0,
   float64 dx,
   float32 measurementFilterCustomCoefficients[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodCfgPulseShapingFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 pulseShapingFilterType,
   float64 pulseShapingFilterParameter,
   float64 x0,
   float64 dx,
   float32 pulseShapingFilterCustomCoefficients[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxDemod_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxDemod_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxDemod_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   float64 IQPowerEdgeLevel,
   int32 IQPowerEdgeSlope,
   float64 triggerDelay,
   int32 triggerMinQuietTimeMode,
   float64 triggerMinQuietTimeDuration,
   int32 enableTrigger
);

int32 __stdcall RFmxDemod_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxDemod_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxDemod_SetAttributeNIComplexSingle(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal
);

int32 __stdcall RFmxDemod_GetAttributeNIComplexSingle(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle *attrVal
);

int32 __stdcall RFmxDemod_SetAttributeNIComplexDouble(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal
);

int32 __stdcall RFmxDemod_GetAttributeNIComplexDouble(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble *attrVal
);

int32 __stdcall RFmxDemod_ADemodFetchDemodSignalTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 demodulatedSignal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_ADemodFetchDemodSpectrumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 demodulatedSpectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_ADemodFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanCarrierFrequencyError,
   float64* meanCarrierPower
);

int32 __stdcall RFmxDemod_ADemodFetchMeanModulationFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanModulationFrequency
);

int32 __stdcall RFmxDemod_ADemodFetchAMMaximumModulationDepth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumModulationDepth,
   float64* maximumHalfPeakToPeak,
   float64* maximumRMS,
   float64* maximumPositivePeak,
   float64* maximumNegativePeak
);

int32 __stdcall RFmxDemod_ADemodFetchAMMeanModulationDepth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanModulationDepth,
   float64* meanHalfPeakToPeak,
   float64* meanRMS,
   float64* meanPositivePeak,
   float64* meanNegativePeak
);

int32 __stdcall RFmxDemod_ADemodReadAM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanModulationDepth,
   float64* meanCarrierPower
);

int32 __stdcall RFmxDemod_ADemodFetchFMMaximumDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumDeviation,
   float64* maximumHalfPeakToPeak,
   float64* maximumRMS,
   float64* maximumPositivePeak,
   float64* maximumNegativePeak
);

int32 __stdcall RFmxDemod_ADemodFetchFMMeanDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanDeviation,
   float64* meanHalfPeakToPeak,
   float64* meanRMS,
   float64* meanPositivePeak,
   float64* meanNegativePeak
);

int32 __stdcall RFmxDemod_ADemodReadFM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanDeviation,
   float64* meanCarrierFrequencyError
);

int32 __stdcall RFmxDemod_ADemodFetchPMMaximumDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumDeviation,
   float64* maximumHalfPeakToPeak,
   float64* maximumRMS,
   float64* maximumPositivePeak,
   float64* maximumNegativePeak
);

int32 __stdcall RFmxDemod_ADemodFetchPMMeanDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanDeviation,
   float64* meanHalfPeakToPeak,
   float64* meanRMS,
   float64* meanPositivePeak,
   float64* meanNegativePeak
);

int32 __stdcall RFmxDemod_ADemodReadPM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanDeviation,
   float64* meanCarrierFrequencyError
);

int32 __stdcall RFmxDemod_ADemodFetchDistortions(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averageSINAD,
   float64* averageSNR,
   float64* averageTHD,
   float64* averageTHDWithNoise
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficients(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* x0,
   float64* dx,
   NIComplexSingle equalizerInitialCoefficients[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* x0,
   float64* dx,
   float32 equalizerInitialCoefficientsI[],
   float32 equalizerInitialCoefficientsQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodGetSymbolMap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexSingle symbolMap[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodGetSymbolMapSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 symbolMapI[],
   float32 symbolMapQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchOffsetEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 offsetEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchReferenceWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   NIComplexSingle referenceWaveform[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchReferenceWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficients(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   NIComplexSingle equalizerCoefficients[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficientsSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 equalizerCoefficientsI[],
   float32 equalizerCoefficientsQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchFSKDeviationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 FSKError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   NIComplexSingle measurementWaveform[],
   int32 arraySize,
   int32* actualArraySize,
   int32* samplesPerSymbol,
   float64* symbolRate
);

int32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 measurementWaveformI[],
   float32 measurementWaveformQ[],
   int32 arraySize,
   int32* actualArraySize,
   int32* samplesPerSymbol,
   float64* symbolRate
);

int32 __stdcall RFmxDemod_DDemodFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellationTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationTraceI[],
   float32 constellationTraceQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle offsetConstellationTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 offsetConstellationTraceI[],
   float32 offsetConstellationTraceQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchDemodulatedBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 demodulatedBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxDemod_DDemodFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSEVM,
   float64* maximumRMSEVM,
   float64* meanModulationErrorRatio,
   float64* maximumPeakEVM,
   float64* meanPeakEVM
);

int32 __stdcall RFmxDemod_DDemodFetchOffsetEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSOffsetEVM,
   float64* maximumRMSOffsetEVM,
   float64* maximumPeakOffsetEVM,
   float64* meanPeakOffsetEVM
);

int32 __stdcall RFmxDemod_DDemodFetchMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanMagnitudeError,
   float64* maximumMagnitudeError
);

int32 __stdcall RFmxDemod_DDemodFetchPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanPhaseError,
   float64* maximumPhaseError
);

int32 __stdcall RFmxDemod_DDemodFetchFSKResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanFSKDeviation,
   float64* meanRMSFSKError,
   float64* maximumPeakFSKError
);

int32 __stdcall RFmxDemod_DDemodFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanIQGainImbalance,
   float64* meanQuadratureSkew,
   float64* meanIQOriginOffset
);

int32 __stdcall RFmxDemod_DDemodFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanFrequencyOffset,
   float64* meanFrequencyDrift,
   float64* meanPhaseError
);

int32 __stdcall RFmxDemod_DDemodFetchMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32* meanIQOriginOffset
);

int32 __stdcall RFmxDemod_DDemodFetchMeanQuadratureSkew(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32* meanQuadratureSkew
);

int32 __stdcall RFmxDemod_DDemodFetchMeanRhoFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRhoFactor
);

int32 __stdcall RFmxDemod_DDemodFetchSyncFound(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* syncFound
);

int32 __stdcall RFmxDemod_DDemodFetchMeanAmplitudeDroop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanAmplitudeDroop
);

int32 __stdcall RFmxDemod_DDemodRead(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanFrequencyOffset,
   float64* meanRMSEVM,
   float64* maximumPeakEVM,
   float64* meanModulationErrorRatio
);

int32 __stdcall RFmxDemod_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxDemod_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxDemod_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxDemod_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxDemod_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxDemod_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxDemod_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAudioMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAudioMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAMCarrierSuppressed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAMCarrierSuppressed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetRBWFilterAlpha(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetRBWFilterAlpha(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetCarrierCorrectionFrequencyEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetCarrierCorrectionFrequencyEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetCarrierCorrectionPhaseEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetCarrierCorrectionPhaseEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetFMDeEmphasis(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetFMDeEmphasis(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAudioFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAudioFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAudioFilterLowerCutoffFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAudioFilterLowerCutoffFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAudioFilterUpperCutoffFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAudioFilterUpperCutoffFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_ADemodSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsMeanCarrierFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsMeanCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsMeanModulationFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAverageSINAD(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAverageTHDWithNoise(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAverageTHD(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAverageSNR(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMeanStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMeanHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMeanPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMeanNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMeanRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMaximumStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMaximumHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMaximumPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMaximumNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsAMModulationDepthMaximumRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMeanStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMeanHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMeanPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMeanNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMeanRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMaximumStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMaximumHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMaximumPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMaximumNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsFMDeviationMaximumRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMeanStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMeanHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMeanPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMeanNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMeanRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMaximumStandardDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMaximumHalfPeaktoPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMaximumPositivePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMaximumNegativePeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_ADemodGetResultsPMDeviationMaximumRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetPSKFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetPSKFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetDifferentialEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetDifferentialEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSymbolRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSymbolRate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetNumberOfSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetNumberOfSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSamplesPerSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSamplesPerSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetEVMNormalizationReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetEVMNormalizationReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetFSKDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetFSKDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetFSKReferenceCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetFSKReferenceCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetAPSKR2ToR1Ratio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetAPSKR2ToR1Ratio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetAPSKR3ToR1Ratio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetAPSKR3ToR1Ratio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSymbolMapType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSymbolMapType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetPulseShapingFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetPulseShapingFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetPulseShapingFilterParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetPulseShapingFilterParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetMeasurementFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetMeasurementFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetEqualizerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerFilterLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetEqualizerFilterLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerTrainingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetEqualizerTrainingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetEqualizerConvergenceFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetEqualizerConvergenceFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSynchronizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSynchronizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSynchronizationBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int8 attrVal[],
   int32 arraySize,
   int32 *actualArraySize
);

int32 __stdcall RFmxDemod_DDemodSetSynchronizationBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxDemod_DDemodGetSynchronizationMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSynchronizationMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSignalStructure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSignalStructure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetBurstStartExclusionSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetBurstStartExclusionSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetBurstEndExclusionSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetBurstEndExclusionSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetCFOEstimationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetCFOEstimationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSearchLengthAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSearchLengthAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetSearchLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetSearchLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxDemod_DDemodSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsCarrierMeanFrequencyOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsCarrierMeanFrequencyDrift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsCarrierMeanPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsEVMMeanRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsEVMMaximumRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsEVMMeanPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsEVMMaximumPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsEVMMeanModulationErrorRatio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsOffsetEVMMeanRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsOffsetEVMMeanPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsOffsetEVMMaximumRMS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsOffsetEVMMaximumPeak(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsMagnitudeErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsMagnitudeErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsPhaseErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsPhaseErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsFSKMeanDeviation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsFSKMeanRMSFSKError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsFSKMaximumPeakFSKError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsIQImpairmentsMeanQuadratureSkew(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsMeanRhoFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsMeanAmplitudeDroop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsSyncFound(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_FREQUENCY_ERROR                        0x00201021
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_DEVIATION_ERROR                        0x0020102e
#define RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_PEAK_DEVIATION_ERROR                       0x0020102f

// Values for RFMXDEMOD_ATTR_DDEMOD_SAMPLES_PER_SYMBOL
#define RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_AUTO                                                 -1
#define RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_4                                                    4
#define RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_8                                                    8
#define RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_16                                                   16

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxDemod_DDemodGetResultsCarrierMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsFSKMeanRMSDeviationError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxDemod_DDemodGetResultsFSKMeanPeakDeviationError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif


#endif
````
