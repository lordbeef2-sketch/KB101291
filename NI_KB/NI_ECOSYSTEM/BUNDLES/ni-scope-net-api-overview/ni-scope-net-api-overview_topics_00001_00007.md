# NI DOCUMENT BUNDLE: ni-scope-net-api-overview

<!--NI_BUNDLE_CHUNK bundle=ni-scope-net-api-overview start=1 end=7 -->
<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopebasicusage.html language=enus -->
## TOPIC 00001: Basic Usage

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopebasicusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopebasicusage.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the NI-SCOPE .NET class library to interactively program NI high-speed oscilloscopes and digitizers. The NI-SCOPE .NET API is an Interchangeable Virtual Instrument (IVI)-compliant instrument driver that features a set of methods and properties that exercise the functionality of the NI-SC

Basic Usage

You can use the NI-SCOPE .NET class library to interactively program NI high-speed oscilloscopes and digitizers. The NI-SCOPE .NET API is an Interchangeable Virtual Instrument (IVI)-compliant instrument driver that features a set of methods and properties that exercise the functionality of the NI-SCOPE hardware.

1. Initialization—Use a constructor to create a new instance of the NIScope class. You must create an instance of this class before you can call into the underlying NI-SCOPE driver. 
 VB.NET

Using scopeSession As New NIScope("resourceName", false, false)
 ' Initialize a session to NI-SCOPE instruments.
 ' Your code goes here. 
End Using
 C#

using (NIScope scopeSession = new NIScope("resourceName", false, false))
{
 // Initialize a session to NI-SCOPE instruments.
 // Your code goes here.
}
2. Configuration—Use the NIScope object to access various sub-objects and to configure the NI-SCOPE driver directly or indirectly. You can use a sub-object of the ScopeChannelCollection class to configure channel-specific properties. 
 VB.NET

Dim scopeSession As New NIScope(ResourceName, False, False)
scopeSession.Channels(ChannelName).Configure(VerticalRange, VerticalOffset, ScopeVerticalCoupling.DC, 1.0, True)
scopeSession.Timing.ConfigureTiming(sampleRateMin, recordLengthMin, refPosition, 1, True)
Dim recordLength As Long = scopeSession.Acquisition.RecordLength
scopeSession.Measurement.Initiate()
Dim byteWaveforms As AnalogWaveformCollection(Of Byte) = scopeSession.Channels(ChannelName).Measurement.FetchByte(timeout, recordLength, byteWaveforms, waveformInfo)
 C#

NIScope scopeSession = new NIScope(ResourceName, false, false);
scopeSession.Channels[ChannelName].Configure(VerticalRange, VerticalOffset, ScopeVerticalCoupling.DC, 1.0, true);
scopeSession.Timing.ConfigureTiming(sampleRateMin, recordLengthMin, refPosition, 1,true);
long recordLength = scopeSession.Acquisition.RecordLength;
scopeSession.Measurement.Initiate();
AnalogWaveformCollection<byte> byteWaveforms = scopeSession.Channels[ChannelName].Measurement.FetchByte(timeout, recordLength, byteWaveforms, out waveformInfo);
3. Initiate—NI-SCOPE devices start acquiring waveforms, causing the NIScope session to enter the running state. 
 VB.NET

scopeSession.Measurement.Initiate()
 C#

scopeSession.Measurement.Initiate();
4. Running State—In the Running state, you can take measurements, fetch buffered measurements, query the output state, or query device states. 
 VB.NET

Dim recordLength As Long = scopeSession.Acquisition.RecordLength
Dim sampleRate As Double = scopeSession.Acquisition.SampleRate
Dim byteWaveforms As AnalogWaveformCollection(Of Byte) = scopeSession.Channels(ChannelName).Measurement.FetchByte(timeout, recordLength, byteWaveforms, waveformInfo)
 C#

long recordLength = scopeSession.Acquisition.RecordLength;
double sampleRate = scopeSession.Acquisition.SampleRate;
AnalogWaveformCollection<byte> byteWaveforms
= scopeSession.Channels[ChannelName].Measurement.FetchByte(timeout, recordLength, byteWaveforms, out waveformInfo);
5. Close—Closes the session to the device(s) and frees un-managed resources that are held by the session. You can close the session with Close or Dispose. 
 VB.NET

scopeSession.Close()
or
scopeSession.Dispose()
or 
Using scopeSession As New NIScope("resourceName", false, false)
 ' Your code goes here. 
End Using
 C#

scopeSession.Close();
or
scopeSession.Dispose();
or
using (NIScope scopeSession = new NIScope("resourceName", false, false))
{
 // Your code goes here.
}

Refer to the 
 *Programming Flow* topic in the 
 *NI High-Speed Digitizers Help* for information about the specific NI-SCOPE software states.

Parent topic:

NI-SCOPE .NET Class Library Help

Related information:

- NIScope Class
- NI-SCOPE Programming Flow

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopecustomvalues.html language=enus -->
## TOPIC 00002: How Do I Pass a Predefined Value to an NI-SCOPE Property?

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopecustomvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopecustomvalues.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are certain properties, such as trigger sources and trigger and event output terminals, that work with a set of predefined string values, but might also accept custom values. For example, the Source property specifies a ScopeDigitalEdgeStartTriggerSource object. You can configure Source using

How Do I Pass a Predefined Value to an NI-SCOPE Property?

Source

ScopeDigitalEdgeStartTriggerSource

Source

```text
VB.NET

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = ScopeDigitalEdgeStartTriggerSource.Pfi0
```

```text
C#

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = ScopeDigitalEdgeStartTriggerSource.Pfi0;
```

FromString

```text
VB.NET

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = ScopeDigitalEdgeStartTriggerSource.FromString("CustomSource")
```

```text
C#

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = ScopeDigitalEdgeStartTriggerSource.FromString("CustomSource");
```

FromString

```text
VB.NET

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = "CustomSource"
```

```text
C#

scopeSession.Trigger.StartTrigger.DigitalEdge.Source = "CustomSource";
```

#### How Do I Get the Underlying String from Source or Output Terminal Value?

ToString

```text
VB.NET

Dim triggerSource As String = ScopeDigitalEdgeStartTriggerSource.Pfi0.ToString()
```

```text
C#

string triggerSource = ScopeDigitalEdgeStartTriggerSource.Pfi0.ToString();
```

You can use the underlying string value to assign a source or output terminal to some other source or output terminal.

Parent topic:

NI-SCOPE .NET Class Library Help

Related information:

- ScopeDigitalEdgeStartTrigger.Source Property

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopeenummapping.html language=enus -->
## TOPIC 00003: Mapping the NI-SCOPE .NET API Enums and Enum Values to the NI-SCOPE C API Attributes/Functions and Values

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopeenummapping.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopeenummapping.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-SCOPE .NET API enums and enum values to the corresponding NI-SCOPE C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIScope namespace. .NET API Enums and Enum Values C API Attributes/Functions and Values ScopeAcquisitionS

Mapping the NI-SCOPE .NET API Enums and Enum Values to the NI-SCOPE C API Attributes/Functions and Values

The following table maps the NI-SCOPE .NET API enums and enum values to the corresponding NI-SCOPE C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIScope namespace.

| .NET API Enums and Enum Values | C API Attributes/Functions and Values |
| --- | --- |
| ScopeAcquisitionStatus | niScope_AcquisitionStatus |
| Complete | NISCOPE_VAL_ACQ_COMPLETE |
| InProgress | NISCOPE_VAL_ACQ_IN_PROGRESS |
| Unknown | NISCOPE_VAL_ACQ_STATUS_UNKNOWN |
| ScopeAcquisitionType | NISCOPE_ATTR_ACQUISITION_TYPE |
| Ddc | NISCOPE_VAL_DDC |
| FlexibleResolution | NISCOPE_VAL_FLEXRES |
| Normal | NISCOPE_VAL_NORMAL |
| ScopeArrayMeasurementType | niScope_FetchArrayMeasurement |
| NoMeasurement | NISCOPE_VAL_NO_MEASUREMENT |
| LastAcquisitionHistogram | NISCOPE_VAL_LAST_ACQ_HISTOGRAM |
| FftPhaseSpectrum | NISCOPE_VAL_FFT_PHASE_SPECTRUM |
| FftAmplitudeSpectrumVoltsRms | NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS |
| MultipleAcquisitionVoltageHistogram | NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM |
| MultipleAcquisitionTimeHistogram | NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM |
| ArrayIntegral | NISCOPE_VAL_ARRAY_INTEGRAL |
| Derivative | NISCOPE_VAL_DERIVATIVE |
| Inverse | NISCOPE_VAL_INVERSE |
| HanningWindow | NISCOPE_VAL_HANNING_WINDOW |
| FlatTopWindow | NISCOPE_VAL_FLAT_TOP_WINDOW |
| PolynomialInterpolation | NISCOPE_VAL_POLYNOMIAL_INTERPOLATION |
| MultiplyChannels | NISCOPE_VAL_MULTIPLY_CHANNELS |
| AddChannels | NISCOPE_VAL_ADD_CHANNELS |
| SubtractChannels | NISCOPE_VAL_SUBTRACT_CHANNELS |
| DivideChannels | NISCOPE_VAL_DIVIDE_CHANNELS |
| MultipleAcquisitionAverage | NISCOPE_VAL_MULTI_ACQ_AVERAGE |
| ButterworthFilter | NISCOPE_VAL_BUTTERWORTH_FILTER |
| ChebyshevFilter | NISCOPE_VAL_CHEBYSHEV_FILTER |
| FftAmplitudeSpectrumDB | NISCOPE_VAL_FFT_AMP_SPECTRUM_DB |
| HammingWindow | NISCOPE_VAL_HAMMING_WINDOW |
| WindowedFirFilter | NISCOPE_VAL_WINDOWED_FIR_FILTER |
| BesselFilter | NISCOPE_VAL_BESSEL_FILTER |
| TriangleWindow | NISCOPE_VAL_TRIANGLE_WINDOW |
| BlackmanWindow | NISCOPE_VAL_BLACKMAN_WINDOW |
| ArrayOffset | NISCOPE_VAL_ARRAY_OFFSET |
| ArrayGain | NISCOPE_VAL_ARRAY_GAIN |
| ScopeCableSenseMode | NISCOPE_ATTR_CABLE_SENSE_MODE |
| Disabled | NISCOPE_VAL_CABLE_SENSE_DISABLED |
| OnDemand | NISCOPE_VAL_CABLE_SENSE_ON_DEMAND |
| ScopeChannelTerminalConfiguration | NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION |
| Differential | NISCOPE_VAL_DIFFERENTIAL |
| SingleEnded | NISCOPE_VAL_SINGLE_ENDED |
| UnbalancedDifferential | NISCOPE_VAL_UNBALANCED_DIFFERENTIAL |
| ScopeDdcDataProcessingMode | NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE |
| Real | NISCOPE_VAL_REAL |
| Complex | NISCOPE_VAL_COMPLEX |
| ScopeFetchRelativeTo | NISCOPE_ATTR_FETCH_RELATIVE_TO |
| Now | NISCOPE_VAL_NOW |
| Pretrigger | NISCOPE_VAL_PRETRIGGER |
| ReadPointer | NISCOPE_VAL_READ_POINTER |
| Start | NISCOPE_VAL_START |
| Trigger | NISCOPE_VAL_TRIGGER |
| ScopeFlexFirAntiAliasFilterType | NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE |
| Tap16Hanning | NISCOPE_VAL_16_TAP_HANNING |
| Tap48Hanning | NISCOPE_VAL_48_TAP_HANNING |
| Tap48Standard | NISCOPE_VAL_48_TAP_STANDARD |
| Tap8Hanning | NISCOPE_VAL_8_TAP_HANNING |
| ScopeMeasurementFilterType | NISCOPE_ATTR_MEAS_FILTER_TYPE |
| LowPass | NISCOPE_VAL_MEAS_LOWPASS |
| HighPass | NISCOPE_VAL_MEAS_HIGHPASS |
| BandPass | NISCOPE_VAL_MEAS_BANDPASS |
| BandStop | NISCOPE_VAL_MEAS_BANDSTOP |
| ScopeMeasurementFirFilterWindow | NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW |
| None | NISCOPE_VAL_NONE |
| HanningWindow | NISCOPE_VAL_HANNING_WINDOW |
| FlatTopWindow | NISCOPE_VAL_FLAT_TOP_WINDOW |
| HammingWindow | NISCOPE_VAL_HAMMING_WINDOW |
| TriangleWindow | NISCOPE_VAL_TRIANGLE_WINDOW |
| BlackmanWindow | NISCOPE_VAL_BLACKMAN_WINDOW |
| ScopeMeasurementPercentageMethod | NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD |
| LowHigh | NISCOPE_VAL_MEAS_LOW_HIGH |
| MinMax | NISCOPE_VAL_MEAS_MIN_MAX |
| BaseTop | NISCOPE_VAL_MEAS_BASE_TOP |
| ScopeMeasurementReferenceLevelUnits | NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS |
| Voltage | NISCOPE_VAL_MEAS_VOLTAGE |
| Percentage | NISCOPE_VAL_MEAS_PERCENTAGE |
| ScopeOverflowErrorReportingMode | NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING |
| Error | NISCOPE_VAL_ERROR_REPORTING_ERROR |
| Warning | NISCOPE_VAL_ERROR_REPORTING_WARNING |
| Disabled | NISCOPE_VAL_ERROR_REPORTING_DISABLED |
| ScopeReferenceTriggerDetectorLocation | NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION |
| AnalogDetectionCircuit | NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT |
| DdcOutput | NISCOPE_VAL_DDC_OUTPUT |
| ScopeRisMethod | NISCOPE_ATTR_RIS_METHOD |
| ExactNumberOfAverages | NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES |
| MinimumNumberOfAverages | NISCOPE_VAL_RIS_MIN_NUM_AVERAGES |
| Incomplete | NISCOPE_VAL_RIS_INCOMPLETE |
| LimitedBinWidth | NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH |
| ScopeSampleMode | NISCOPE_ATTR_SAMPLE_MODE |
| EquivalentTime | NISCOPE_VAL_EQUIVALENT_TIME |
| Realtime | NISCOPE_VAL_REAL_TIME |
| ScopeScalarMeasurementType | niScope_FetchMeasurement |
| RiseTime | NISCOPE_VAL_RISE_TIME |
| FallTime | NISCOPE_VAL_FALL_TIME |
| Frequency | NISCOPE_VAL_FREQUENCY |
| Period | NISCOPE_VAL_PERIOD |
| VoltageRMS | NISCOPE_VAL_VOLTAGE_RMS |
| VoltagePeakToPeak | NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK |
| VoltageMax | NISCOPE_VAL_VOLTAGE_MAX |
| VoltageMin | NISCOPE_VAL_VOLTAGE_MIN |
| VoltageHigh | NISCOPE_VAL_VOLTAGE_HIGH |
| VoltageLow | NISCOPE_VAL_VOLTAGE_LOW |
| VoltageAverage | NISCOPE_VAL_VOLTAGE_AVERAGE |
| WidthNegative | NISCOPE_VAL_WIDTH_NEG |
| WidthPositive | NISCOPE_VAL_WIDTH_POS |
| DutyCycleNegative | NISCOPE_VAL_DUTY_CYCLE_NEG |
| DutyCyclePositive | NISCOPE_VAL_DUTY_CYCLE_POS |
| VoltageAmplitude | NISCOPE_VAL_AMPLITUDE |
| VoltageCycleRms | NISCOPE_VAL_VOLTAGE_CYCLE_RMS |
| VoltageCycleAverage | NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE |
| Overshoot | NISCOPE_VAL_OVERSHOOT |
| Preshoot | NISCOPE_VAL_PRESHOOT |
| LowReferenceVolts | NISCOPE_VAL_LOW_REF_VOLTS |
| MidReferenceVolts | NISCOPE_VAL_MID_REF_VOLTS |
| HighReferenceVolts | NISCOPE_VAL_HIGH_REF_VOLTS |
| Area | NISCOPE_VAL_AREA |
| CycleArea | NISCOPE_VAL_CYCLE_AREA |
| Integral | NISCOPE_VAL_INTEGRAL |
| VoltageBase | NISCOPE_VAL_VOLTAGE_BASE |
| VoltageTop | NISCOPE_VAL_VOLTAGE_TOP |
| FftFrequency | NISCOPE_VAL_FFT_FREQUENCY |
| FftAmplitude | NISCOPE_VAL_FFT_AMPLITUDE |
| RiseSlewRate | NISCOPE_VAL_RISE_SLEW_RATE |
| FallSlewRate | NISCOPE_VAL_FALL_SLEW_RATE |
| ACEstimate | NISCOPE_VAL_AC_ESTIMATE |
| DCEstimate | NISCOPE_VAL_DC_ESTIMATE |
| TimeDelay | NISCOPE_VAL_TIME_DELAY |
| AveragePeriod | NISCOPE_VAL_AVERAGE_PERIOD |
| AverageFrequency | NISCOPE_VAL_AVERAGE_FREQUENCY |
| VoltageBaseToTop | NISCOPE_VAL_VOLTAGE_BASE_TO_TOP |
| PhaseDelay | NISCOPE_VAL_PHASE_DELAY |
| TimeHistogramMean | NISCOPE_VAL_TIME_HISTOGRAM_MEAN |
| TimeHistogramStandardDeviation | NISCOPE_VAL_TIME_HISTOGRAM_STDEV |
| TimeHistogramPeakToPeak | NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK |
| TimeHistogramMedian | NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN |
| TimeHistogramHits | NISCOPE_VAL_TIME_HISTOGRAM_HITS |
| TimeHistogramMax | NISCOPE_VAL_TIME_HISTOGRAM_MAX |
| TimeHistogramMin | NISCOPE_VAL_TIME_HISTOGRAM_MIN |
| TimeHistogramMeanPlusStandardDeviation | NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV |
| TimeHistogramMeanPlus2StandardDeviation | NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV |
| TimeHistogramMeanPlus3StandardDeviation | NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV |
| TimeHistogramMode | NISCOPE_VAL_TIME_HISTOGRAM_MODE |
| TimeHistogramNewHits | NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS |
| VoltageHistogramMean | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN |
| VoltageHistogramStandardDeviation | NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV |
| VoltageHistogramPeakToPeak | NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK |
| VoltageHistogramMedian | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN |
| VoltageHistogramHits | NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS |
| VoltageHistogramMax | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX |
| VoltageHistogramMin | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN |
| VoltageHistogramMeanPlusStandardDeviation | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV |
| VoltageHistogramMeanPlus2StandardDeviation | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV |
| VoltageHistogramMeanPlus3StandardDeviation | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV |
| VoltageHistogramMode | NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE |
| VoltageHistogramNewHits | NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS |
| ScopeSelfCalibrationOption | niScope_CalSelfCalibrate |
| NormalSelfCalibration | NISCOPE_VAL_SELF_CALIBRATION |
| RestorePreviousExternalCalibration | NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION |
| ScopeTriggerCoupling | NISCOPE_ATTR_TRIGGER_COUPLING |
| AC | NISCOPE_VAL_AC |
| DC | NISCOPE_VAL_DC |
| HighFrequencyReject | NISCOPE_VAL_HF_REJECT |
| LowFrequencyReject | NISCOPE_VAL_LF_REJECT |
| ACPlusHighFrequencyReject | NISCOPE_VAL_AC_PLUS_HF_REJECT |
| ScopeTriggerSlope | NISCOPE_ATTR_TRIGGER_SLOPE |
| Positive | NISCOPE_VAL_POSITIVE |
| Negative | NISCOPE_VAL_NEGATIVE |
| ScopeTriggerModifier | NISCOPE_ATTR_TRIGGER_MODIFIER |
| None | NISCOPE_VAL_NO_TRIGGER_MOD |
| Auto | NISCOPE_VAL_AUTO |
| ScopeTriggerType | NISCOPE_ATTR_TRIGGER_TYPE |
| Edge | NISCOPE_VAL_EDGE_TRIGGER |
| Hysterisis | NISCOPE_VAL_HYSTERESIS_TRIGGER |
| DigitalEdge | NISCOPE_VAL_DIGITAL_TRIGGER |
| Window | NISCOPE_WINDOW_TRIGGER |
| Software | NISCOPE_VAL_SOFTWARE_TRIGGER |
| TV | NISCOPE_VAL_TV_TRIGGER |
| Immediate | NISCOPE_VAL_IMMEDIATE_TRIGGER |
| ScopeTVTriggerEvent | NISCOPE_ATTR_TV_TRIGGER_EVENT |
| Field1 | NISCOPE_VAL_TV_EVENT_FIELD1 |
| Field2 | NISCOPE_VAL_TV_EVENT_FIELD2 |
| AnyField | NISCOPE_VAL_TV_EVENT_ANY_FIELD |
| AnyLine | NISCOPE_VAL_TV_EVENT_ANY_LINE |
| LineNumber | NISCOPE_VAL_TV_EVENT_LINE_NUMBER |
| ScopeTVTriggerPolarity | NISCOPE_ATTR_TV_TRIGGER_POLARITY |
| Positive | NISCOPE_VAL_TV_POSITIVE |
| Negative | NISCOPE_VAL_TV_NEGATIVE |
| ScopeTVTriggerSignalFormat | NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT |
| Ntsc | NISCOPE_VAL_NTSC |
| Pal | NISCOPE_VAL_Pal |
| Secam | NISCOPE_VAL_Secam |
| MPal | NISCOPE_VAL_M_PAL |
| I480Lines5994FieldsPerSecond | NISCOPE_VAL_480I_59_94_FIELDS_PER_SECOND |
| I480Lines60FieldsPerSecond | NISCOPE_VAL_480I_60_FIELDS_PER_SECOND |
| P480Lines5994FieldsPerSecond | NISCOPE_VAL_480P_59_94_FIELDS_PER_SECOND |
| P480Lines60FieldsPerSecond | NISCOPE_VAL_480P_60_FIELDS_PER_SECOND |
| I576Lines50FieldsPerSecond | NISCOPE_VAL_576I_50_FIELDS_PER_SECOND |
| P576Lines50FieldsPerSecond | NISCOPE_VAL_576P_50_FIELDS_PER_SECOND |
| P720Lines50FramesPerSecond | NISCOPE_VAL_720P_50_FRAMES_PER_SECOND |
| P720Lines5994FramesPerSecond | NISCOPE_VAL_720P_59_94_FRAMES_PER_SECOND |
| P720Lines60FramesPerSecond | NISCOPE_VAL_720P_60_FRAMES_PER_SECOND |
| I1080Lines50FieldsPerSecond | NISCOPE_VAL_1080I_50_FIELDS_PER_SECOND |
| I1080Lines5994FieldsPerSecond | NISCOPE_VAL_1080I_59_94_FIELDS_PER_SECOND |
| I1080Lines60FieldsPerSecond | NISCOPE_VAL_1080I_60_FIELDS_PER_SECOND |
| P1080Lines24FramesPerSecond | NISCOPE_VAL_1080P_24_FRAMES_PER_SECOND |
| ScopeVerticalCoupling | NISCOPE_ATTR_VERTICAL_COUPLING |
| AC | NISCOPE_VAL_AC |
| DC | NISCOPE_VAL_DC |
| Ground | NISCOPE_VAL_GND |
| ScopeWindowTriggerMode | NISCOPE_ATTR_TRIGGER_WINDOW_MODE |
| Entering | NISCOPE_VAL_ENTERING_WINDOW |
| Leaving | NISCOPE_VAL_LEAVING_WINDOW |

Parent topic:

NI-SCOPE .NET Class Library Help

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopeerrors.html language=enus -->
## TOPIC 00004: How Do I Manage Errors and Warnings in the NI-SCOPE .NET Class Library?

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopeerrors.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopeerrors.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The underlying NI-SCOPE driver reports any errors or warnings as error codes. Negative return values indicate errors, whereas positive values indicate warnings. In case of warnings, a warning event is raised that you can subscribe to. Errors The NI-SCOPE .NET API converts the negative error codes in

How Do I Manage Errors and Warnings in the NI-SCOPE .NET Class Library?

The underlying NI-SCOPE driver reports any errors or warnings as error codes. Negative return values indicate errors, whereas positive values indicate warnings. In case of warnings, a warning event is raised that you can subscribe to.

#### Errors

The NI-SCOPE .NET API converts the negative error codes into exceptions and throws these exceptions. All exceptions that the API throws are either .NET-defined or IVI-defined; none of them are custom exceptions. The exception message for driver errors has the driver error code appended at the end.

#### Warnings

Warning

- Driver Warning VB.NET

AddHandler scopeSession.DriverOperation.Warning, New EventHandler(Of ScopeWarningEventArgs)(AddressOf DriverOperation_Warning)
Private Sub DriverOperation_Warning(ByVal sender As Object, ByVal e As ScopeWarningEventArgs)
 'Code to handle Warnings. 
End Sub C#

scopeSession.DriverOperation.Warning += new EventHandler<ScopeWarningEventArgs>(DriverOperation_Warning);
void DriverOperation_Warning(object sender, ScopeWarningEventArgs e)
{
 //Code to handle Warnings.
} org.dita.html5/xsl/topic.xsl 455 Note National Instruments recommends subscribing to the warning event immediately after creating the NIScope object, to avoid missing any warnings that might occur.
- InterchangeCheck Warning — InterchangeCheck warnings are communicated as events. To receive warnings, you must subscribe to the InterchangeCheckWarning event as follows: 
 VB.NET

AddHandler scopeSession.DriverOperation.InterchangeCheckWarning, AddressOf DriverOperation_InterchangeCheckWarning
Private Sub DriverOperation_InterchangeCheckWarning(ByVal sender As Object, ByVal e As ScopeInterchangeCheckWarningEventArgs)
 'Code to handle InterchangeCheckWarnings. 
End Sub C#

scopeSession.DriverOperation.InterchangeCheckWarning += new EventHandler<ScopeInterchangeCheckWarningEventArgs>(DriverOperation_InterchangeCheckWarning);
void DriverOperation_InterchangeCheckWarning(object sender, ScopeInterchangeCheckWarningEventArgs e)
{
 //Code to handle InterchangeCheckWarnings.
}
- Coercion Warning — CoercionWarnings are communicated as events. To receive warnings, your must subscribe to the Coercion event as follows: 
 VB.NET

AddHandler scopeSession.DriverOperation.Coercion, AddressOf DriverOperation_CoercionWarning
Private Sub DriverOperation_CoercionWarning(ByVal sender As Object, ByVal e As ScopeCoercionEventArgs)
 'Code to handle CoercionWarnings. 
End Sub C#

scopeSession.DriverOperation.Coercion += new EventHandler<ScopeCoercionEventArgs>(DriverOperation_CoercionWarning);
void DriverOperation_CoercionWarning(object sender, ScopeCoercionEventArgs e)
{
 //Code to handle CoercionWarnings.
}

Each warning EventArgs class contains a read-only property Textto get the description of that event. For example:

- Ivi.Driver.CoercionEventArgs 
 VB.NET

Private Sub DriverOperation_CoercionWarning(ByVal sender As Object, ByVal e As Ivi.Driver.CoercionEventArgs)
 Dim description As string = e.Text
End Sub 
 C#

void DriverOperation_CoercionWarning(object sender, Ivi.Driver.CoercionEventArgs e)
{
 string description = e.Text;
}
- Ivi.Driver.InterchangeCheckWarningEventArgs 
 VB.NET

Private Sub DriverOperation_InterchangeCheckWarning(ByVal sender As Object, ByVal e As Ivi.Driver.InterchangeCheckWarningEventArgs)
 Dim description As string = e.Text 
End Sub 
 C#

void DriverOperation_InterchangeCheckWarning(object sender, Ivi.Driver.InterchangeCheckWarningEventArgs e)
{
 string description = e.Text;
}

Parent topic:

NI-SCOPE .NET Class Library Help

Related information:

- ScopeDriverOperation.Warning Event
- ScopeDriverOperation.Coercion Event

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopefetchread.html language=enus -->
## TOPIC 00005: Using Fetch and Read Methods

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopefetchread.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopefetchread.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Fetch and Read methods are present in the ScopeChannelMeasurement class. A session must be opened, configured, and initiated before you can use Fetch and Read methods. Read methods internally invoke the Initiate method. The Fetch and Read methods can be categorized into synchronous and asynchron

Using Fetch and Read Methods

The Fetch and Read methods are present in the ScopeChannelMeasurement class. A session must be opened, configured, and initiated before you can use Fetch and Read methods. Read methods internally invoke the Initiate method.

The Fetch and Read methods can be categorized into synchronous and asynchronous methods.

#### Using Async Methods

Some input/output (I/O) operations in NI-SCOPE can take a long time relative to other client program operations. In such cases, the NI-SCOPE .NET class library provides asynchronous programming support to execute the I/O operation on a different thread. This permits the client program to perform other operations without waiting for the I/O operation to complete.

The asynchronous I/O API in NI-SCOPE class library uses the Asynchronous Programming Model (APM) to implement the asynchronous I/O. In the APM, an asynchronous operation is implemented as two methods: Begin <Operation> and End <Operation> , where <Operation> is the name of an I/O method that operates synchronously.

After calling the Begin <Operation> method, a client program can continue executing instructions on the calling thread while the specific driver performs an <Operation> on a different thread. For each call to the Begin <Operation> method, the client program calls the End <Operation> method to get the results of the operation.

```text
VB.NET

Private scopeSession As NIScope
    Private Sub StartAcquisition()
      Dim callBack As New AsyncCallback(AddressOf ProcessRead)
      scopeSession = New NIScope("scope1", True, True)
      scopeSession.Measurement.AutoSetup()
      ' Start the asynchronous Read operation. 
      Dim timeout As New PrecisionTimeSpan(10.0)
      Dim asyncResult As IAsyncResult = scopeSession.Channels("0").Measurement.BeginRead(timeout, -1, Nothing, callBack, Nothing)
      ' … 
    End Sub 

    Private Sub ProcessRead(asyncResult As IAsyncResult)
      Dim waveforms As AnalogWaveformCollection(Of Double)
      Try 
        ' Get the results.
        waveforms = scopeSession.Channels("0").Measurement.EndRead(asyncResult)
      Catch ex As Exception
        ' Handle the exception from the asynchronous Read operation. 
      End Try 
      ' ... 
      ' Process waveforms. 
      ' ... 
    End Sub
```

```text
C#

NIScope scopeSession;
    void StartAcquisition()
    {
      AsyncCallback callBack = new AsyncCallback(ProcessRead);
      scopeSession = new NIScope("scope1", true, true);
      scopeSession.Measurement.AutoSetup();
      // Start the asynchronous Read operation.
      PrecisionTimeSpan timeout = new PrecisionTimeSpan(10.0);
      IAsyncResult asyncResult = scopeSession.Channels["0"].Measurement.BeginRead(timeout, -1, null, callBack, null);
      // …
     }

    void ProcessRead(IAsyncResult asyncResult)
    {
      AnalogWaveformCollection<double> waveforms;
      try
      {
        // Get the results.
        waveforms = scopeSession.Channels["0"].Measurement.EndRead(asyncResult);
      }
      catch (Exception ex)
      {
        // Handle the exception from the asynchronous Read operation.
      }
      // ... 
      // Process waveforms. 
      // ...
    }
```

#### Using Memory Optimization

Fetch

Read

```text
VB.NET

Using scopeSession As New NIScope("scope1", True, True)
    ' ... 
    ' Configure scope channel "0" properties. 
    ' ... 

    ' First read operation. 
    ' Here the waveform parameter is null, so the FetchDouble method 
    ' internally allocates memory for the return waveform object. 
    Dim waveform As AnalogWaveformCollection(Of Double) = scopeSession.Channels("0").Measurement.FetchDouble(New PrecisionTimeSpan(10), 1000, Nothing)

    ' Second read operation. Notice the waveform is passed as a parameter to the FetchDouble method. 
    ' This time the FetchDouble method reuses memory of waveform object for the returned waveform if possible.
    waveform = scopeSession.Channels("0").Measurement.FetchDouble(New PrecisionTimeSpan(10), 1000, waveform)
End Using
```

```text
C#

using (NIScope scopeSession = new NIScope("scope1", true, true))
{
    // ... 
    // Configure scope channel "0" properties. 
    // ... 

    // First read operation. 
    // Here the waveform parameter is null, so the FetchDouble method 
    // internally allocates memory for the return waveform object.
    AnalogWaveformCollection<double> waveform = scopeSession.Channels["0"].Measurement.FetchDouble(new PrecisionTimeSpan(10), 1000, null);

    // Second read operation. Notice the waveform is passed as a parameter to the FetchDouble method. 
    // This time the FetchDouble method reuses memory of waveform object for the returned waveform if possible.
    waveform = scopeSession.Channels["0"].Measurement.FetchDouble(new PrecisionTimeSpan(10), 1000, waveform);
}
```

Parent topic:

NI-SCOPE .NET Class Library Help

Related information:

- ScopeChannelMeasurement Class
- Asynchronous Programming Model (APM)

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopeintro.html language=enus -->
## TOPIC 00006: NI-SCOPE .NET Class Library Help

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopeintro.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopeintro.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI-SCOPE .NET Class Library to interactively program NI high-speed oscilloscopes and digitizers. For additional information, refer to the NI High-Speed Digitizers Help. Select StartAll ProgramsNational InstrumentsNI-SCOPENI-SCOPE Documentation to access the NI High-Speed Digitizers H

NI-SCOPE .NET Class Library Help

You can use the NI-SCOPE .NET Class Library to interactively program NI high-speed oscilloscopes and digitizers. For additional information, refer to the 
 *NI High-Speed Digitizers Help*. Select 
 Start»All Programs»National Instruments»NI-SCOPE»NI-SCOPE Documentation to access the 
 *NI High-Speed Digitizers Help* and 
 *NI-SCOPE Readme*.

For additional information on developing applications using NI drivers and the .NET Framework, refer to 
 [ni.com/mstudio](http://www.ni.com/mstudio/) or visit 
 [ni.com/info](http://www.ni.com/info/) and enter the Info Code 
 NIdotNET.

You can find example applications by selecting 
 National Instruments»NI-SCOPE»NI-SCOPE Examples in the Start menu.

© 2018–2019 National Instruments. All rights reserved.

Related information:

- NIScope Namespace
- NI High-Speed Digitizers Help

<!--NI_TOPIC bundle=ni-scope-net-api-overview path=netscopemapping.html language=enus -->
## TOPIC 00007: Mapping the NI-SCOPE .NET API to the NI-SCOPE C API

- bundle_id: `ni-scope-net-api-overview`
- source_path: `netscopemapping.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-net-api-overview/raw/resource/enus/netscopemapping.html
- document_id: `ni-scope-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-SCOPE .NET API members to the corresponding NI-SCOPE C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIScope namespace. IVI .NET API Member .NET API Member C API Member .NET Hierarchy NIScope Class IIviDriver.Close Cl

Mapping the NI-SCOPE .NET API to the NI-SCOPE C API

The following table maps the NI-SCOPE .NET API members to the corresponding NI-SCOPE C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIScope namespace.

| IVI .NET API Member | .NET API Member | C API Member | .NET Hierarchy |
| --- | --- | --- | --- |
|  | NIScope Class |  |  |
| IIviDriver.Close | Close | niScope_close | ScopeSession.Close |
|  | ExportSignal | niScope_ExportSignal | ScopeSession.ExportSignal |
|  | IsDeviceReady | niScope_IsDeviceReady | NIScope.IsDeviceReady |
|  | ProbeCompensationSignalStart | niScope_ProbeCompensationSignalStart | ScopeSession.ProbeCompensationSignalStart |
|  | ProbeCompensationSignalStop | niScope_ProbeCompensationSignalStop | ScopeSession.ProbeCompensationSignalStop |
|  | ScopeAcquisition Class |  |  |
|  | Backlog | NISCOPE_ATTR_BACKLOG | ScopeSession.Acquisition.Backlog |
|  | BinarySampleWidth | NISCOPE_ATTR_BINARY_SAMPLE_WIDTH | ScopeSession.Acquisition.BinarySampleWidth |
|  | DataTransferBandwidthMax | NISCOPE_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH | ScopeSession.Acquisition.DataTransferBandwidthMax |
|  | DataTransferBlockSize | NISCOPE_ATTR_DATA_TRANSFER_BLOCK_SIZE | ScopeSession.Acquisition.DataTransferBlockSize |
|  | DataTransferPacketSizePreferred | NISCOPE_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE | ScopeSession.Acquisition.DataTransferPacketSizePreferred |
|  | DdcDataProcessingMode | NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE | ScopeSession.Acquisition.DdcDataProcessingMode |
|  | NumberOfPointsMin | NISCOPE_ATTR_HORZ_MIN_NUM_PTS | ScopeSession.Acquisition.NumberOfPointsMin |
|  | NumberOfMeasurementSamplesToFetch | NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES | ScopeSession.Acquisition.NumberOfMeasurementSamplesToFetch |
|  | OverflowErrorReportingMode | NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING | ScopeSession.Acquisition.OverflowErrorReportingMode |
|  | RecordLength | NISCOPE_ATTR_HORZ_RECORD_LENGTH | ScopeSession.Acquisition.RecordLength |
|  | RecordNumberToFetch | NISCOPE_ATTR_FETCH_RECORD_NUMBER | ScopeSession.Acquisition.RecordNumberToFetch |
|  | Resolution | NISCOPE_ATTR_RESOLUTION | ScopeSession.Acquisition.Resolution |
|  | SampleMode | NISCOPE_ATTR_SAMPLE_MODE | ScopeSession.Acquisition.SampleMode |
|  | SampleRate | NISCOPE_ATTR_HORZ_SAMPLE_RATE | ScopeSession.Acquisition.SampleRate |
|  | SampleRateMin | NISCOPE_ATTR_MIN_SAMPLE_RATE | ScopeSession.Acquisition.SampleRateMin |
|  | StartTime | NISCOPE_ATTR_ACQUISITION_START_TIME | ScopeSession.Acquisition.StartTime |
|  | TimePerRecord | NISCOPE_ATTR_HORZ_TIME_PER_RECORD | ScopeSession.Acquisition.TimePerRecord |
|  | Type | NISCOPE_ATTR_ACQUISITION_TYPE | ScopeSession.Acquisition.Type |
|  | ScopeAdvanceTrigger Class |  |  |
|  | SendSoftwareEdgeTrigger | niScope_SendSoftwareTriggerEdge | ScopeSession.Trigger.AdvanceTrigger.SendSoftwareEdgeTrigger |
|  | ScopeAdvanceTriggerExportedOutputTerminal Class | NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeAdvanceTriggerSource Class | NISCOPE_ATTR_ADV_TRIG_SRC |  |
|  | Immediate | NISCOPE_VAL_IMMEDIATE |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | SoftwareTriggerFunction | NISCOPE_VAL_SW_TRIG_FUNC |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | ScopeArmReferenceTrigger Class |  |  |
|  | SendSoftwareEdgeTrigger | niScope_SendSoftwareTriggerEdge | ScopeSession.Trigger.ArmReferenceTrigger.SendSoftwareEdgeTrigger |
|  | ScopeArmReferenceTriggerSource Class | NISCOPE_ATTR_ARM_REF_TRIG_SRC |  |
|  | Immediate | NISCOPE_VAL_IMMEDIATE |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | SoftwareTriggerFunction | NISCOPE_VAL_SW_TRIG_FUNC |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeCalibrationUtility Class |  |  |
|  | DeviceTemperature | NISCOPE_ATTR_DEVICE_TEMPERATURE | ScopeSession.Calibration.Utility.DeviceTemperature |
|  | ScopeChannel Class |  |  |
|  | BandPassFilterEnabled | NISCOPE_ATTR_BANDPASS_FILTER_ENABLED | ScopeSession.Channels[].BandpassFilterEnabled |
|  | CableSenseMode | NISCOPE_ATTR_CABLE_SENSE_MODE |  |
|  | CableSenseVoltage | NISCOPE_ATTR_CABLE_SENSE_VOLTAGE |  |
|  | Coupling | NISCOPE_ATTR_VERTICAL_COUPLING | ScopeSession.Channels[].Coupling |
|  | DigitalGain | NISCOPE_ATTR_DIGITAL_GAIN | ScopeSession.Channels[].DigitalGain |
|  | DigitalOffset | NISCOPE_ATTR_DIGITAL_OFFSET | ScopeSession.Channels[].DigitalOffset |
|  | DitherEnabled | NISCOPE_ATTR_DITHER_ENABLED | ScopeSession.Channels[].DitherEnabled |
|  | Enabled | NISCOPE_ATTR_CHANNEL_ENABLED | ScopeSession.Channels[].Enabled |
|  | EnableInterleavingOffsetCorrection | NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED | ScopeSession.Channels[].EnableInterleavingOffsetCorrection |
|  | EnableTimeInterleavedSampling | NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING | ScopeSession.Channels[].EnableTimeInterleavedSampling |
|  | FlexFirAntiAliasFilterType | NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE | ScopeSession.Channels[].FlexFirAntiAliasFilterType |
|  | HighPassFilterFrequency | NISCOPE_ATTR_HIGH_PASS_FILTER_FREQUENCY | ScopeSession.Channels[].HighPassFilterFrequency |
|  | InputFrequencyMax | NISCOPE_ATTR_MAX_INPUT_FREQUENCY | ScopeSession.Channels[].InputFrequencyMax |
|  | InputImpedance | NISCOPE_ATTR_INPUT_IMPEDANCE | ScopeSession.Channels[].InputImpedance |
|  | Offset | NISCOPE_ATTR_VERTICAL_OFFSET | ScopeSession.Channels[].Offset |
|  | ProbeAttenuation | NISCOPE_ATTR_PROBE_ATTENUATION | ScopeSession.Channels[].ProbeAttenuation |
|  | Range | NISCOPE_ATTR_VERTICAL_RANGE | ScopeSession.Channels[].Range |
|  | TerminalConfiguration | NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION | ScopeSession.Channels[].TerminalConfiguration |
|  | Configure | niScope_ConfigureVertical | ScopeSession.Channels[].Configure |
|  | ConfigureCharacteristics | niScope_ConfigureChanCharacteristics | ScopeSession.Channels[].ConfigureCharacteristics |
|  | GetFrequencyResponse | niScope_GetFrequencyResponse | ScopeSession.Channels[].GetFrequencyResponse |
|  | GetNormalizationCoefficients | niScope_GetNormalizationCoefficients | ScopeSession.Channels[].GetNormalizationCoefficients |
|  | GetScalingCoefficients | niScope_GetScalingCoefficients | ScopeSession.Channels[].GetScalingCoefficients |
|  | ScopeChannelDdc Class |  |  |
|  | CenterFrequency | NISCOPE_ATTR_DDC_CENTER_FREQUENCY | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.CenterFrequency |
|  | Enabled | NISCOPE_ATTR_DDC_ENABLED | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.Enabled |
|  | FrequencyTranslationEnabled | NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_ENABLED | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.FrequencyTranslationEnabled |
|  | FrequencyTranslationPhaseI | NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_I | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.FrequencyTranslationPhaseI |
|  | FrequencyTranslationPhaseQ | NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_Q | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.FrequencyTranslationPhaseQ |
|  | QSource | NISCOPE_ATTR_DDC_Q_SOURCE | ScopeSession.Channels[].OnboardSignalProcessing.Ddc.QSource |
|  | ScopeChannelMeasurement Class |  |  |
|  | ArrayGain | NISCOPE_ATTR_MEAS_ARRAY_GAIN | ScopeSession.Channels[].Measurement.ArrayGain |
|  | ArrayOffset | NISCOPE_ATTR_MEAS_ARRAY_OFFSET | ScopeSession.Channels[].Measurement.ArrayOffset |
|  | HysteresisPercent | NISCOPE_ATTR_MEAS_HYSTERESIS_PERCENT | ScopeSession.Channels[].Measurement.HysteresisPercent |
|  | InterpolationSamplingFactor | NISCOPE_ATTR_MEAS_INTERPOLATION_SAMPLING_FACTOR | ScopeSession.Channels[].Measurement.InterpolationSamplingFactor |
|  | LastHistogramSize | NISCOPE_ATTR_MEAS_LAST_ACQ_HISTOGRAM_SIZE | ScopeSession.Channels[].Measurement.LastHistogramSize |
|  | OtherChannel | NISCOPE_ATTR_MEAS_OTHER_CHANNEL | ScopeSession.Channels[].Measurement.OtherChannel |
|  | PolynomialInterpolationOrder | NISCOPE_ATTR_MEAS_POLYNOMIAL_INTERPOLATION_ORDER | ScopeSession.Channels[].Measurement.PolynomialInterpolationOrder |
|  | AddWaveformProcessing | niScope_AddWaveformProcessing | ScopeSession.Channels[].Measurement.AddWaveformProcessing |
|  | BeginFetchArrayMeasurement | niScope_FetchArrayMeasurement | ScopeSession.Channels[].Measurement.BeginFetchArrayMeasurement |
|  | BeginFetchByte | niScope_FetchBinary8 | ScopeSession.Channels[].Measurement.BeginFetchByte |
|  | BeginFetchComplexDouble | niScope_FetchComplex | ScopeSession.Channels[].Measurement.BeginFetchComplexDouble |
|  | BeginFetchComplexInt16 | niScope_FetchComplexBinary16 | ScopeSession.Channels[].Measurement.BeginFetchComplexInt16 |
|  | BeginFetchDouble | niScope_Fetch | ScopeSession.Channels[].Measurement.BeginFetchDouble |
|  | BeginFetchInt16 | niScope_FetchBinary16 | ScopeSession.Channels[].Measurement.BeginFetchInt16 |
|  | BeginFetchInt32 | niScope_FetchBinary32 | ScopeSession.Channels[].Measurement.BeginFetchInt32 |
|  | BeginFetchScalarMeasurement | niScope_FetchMeasurement | ScopeSession.Channels[].Measurement.BeginFetchScalarMeasurement |
|  | BeginFetchScalarMeasurementStatistics | niScope_FetchMeasurementStats | ScopeSession.Channels[].Measurement.BeginFetchScalarMeasurementStatistics |
|  | BeginRead | niScope_Read | ScopeSession.Channels[].Measurement.BeginRead |
|  | BeginReadScalarMeasurement | niScope_ReadMeasurement | ScopeSession.Channels[].Measurement.BeginReadScalarMeasurement |
|  | ClearWaveformMeasurements | niScope_ClearWaveformMeasurementStats | ScopeSession.Channels[].Measurement.ClearWaveformMeasurements |
|  | ClearWaveformProcessing | niScope_ClearWaveformProcessing | ScopeSession.Channels[].Measurement.ClearWaveformProcessing |
|  | EndFetchArrayMeasurement | niScope_FetchArrayMeasurement | ScopeSession.Channels[].Measurement.EndFetchArrayMeasurement |
|  | EndFetchByte | niScope_FetchBinary8 | ScopeSession.Channels[].Measurement.EndFetchByte |
|  | EndFetchComplexDouble | niScope_FetchComplex | ScopeSession.Channels[].Measurement.EndFetchComplexDouble |
|  | EndFetchComplexInt16 | niScope_FetchComplexBinary16 | ScopeSession.Channels[].Measurement.EndFetchComplexInt16 |
|  | EndFetchDouble | niScope_Fetch | ScopeSession.Channels[].Measurement.EndFetchDouble |
|  | EndFetchInt16 | niScope_FetchBinary16 | ScopeSession.Channels[].Measurement.EndFetchInt16 |
|  | EndFetchInt32 | niScope_FetchBinary32 | ScopeSession.Channels[].Measurement.EndFetchInt32 |
|  | EndFetchScalarMeasurement | niScope_FetchMeasurement | ScopeSession.Channels[].Measurement.EndFetchScalarMeasurement |
|  | EndFetchScalarMeasurementStatistics | niScope_FetchMeasurementStats | ScopeSession.Channels[].Measurement.EndFetchScalarMeasurementStatistics |
|  | EndRead | niScope_Read | ScopeSession.Channels[].Measurement.EndRead |
|  | EndReadScalarMeasurement | niScope_ReadMeasurement | ScopeSession.Channels[].Measurement.EndReadScalarMeasurement |
|  | FetchArrayMeasurement | niScope_FetchArrayMeasurement | ScopeSession.Channels[].Measurement.FetchArrayMeasurement |
|  | FetchByte | niScope_FetchBinary8 | ScopeSession.Channels[].Measurement.FetchByte |
|  | FetchInt16 | niScope_FetchBinary16 | ScopeSession.Channels[].Measurement.FetchInt16 |
|  | FetchInt32 | niScope_FetchBinary32 | ScopeSession.Channels[].Measurement.FetchInt32 |
|  | FetchComplexDouble | niScope_FetchComplex | ScopeSession.Channels[].Measurement.FetchComplexDouble |
|  | FetchComplexInt16 | niScope_FetchComplexBinary16 | ScopeSession.Channels[].Measurement.FetchComplexInt16 |
|  | FetchDouble | niScope_Fetch | ScopeSession.Channels[].Measurement.FetchDouble |
|  | FetchScalarMeasurement | niScope_FetchMeasurement | ScopeSession.Channels[].Measurement.FetchScalarMeasurement |
|  | FetchScalarMeasurementStatistics | niScope_FetchMeasurementStats | ScopeSession.Channels[].Measurement.FetchScalarMeasurementStatistics |
|  | Read | niScope_Read | ScopeSession.Channels[].Measurement.Read |
|  | ReadScalarMeasurement | niScope_ReadMeasurement | ScopeSession.Channels[].Measurement.ReadScalarMeasurement |
|  | ScopeChannelMeasurementFilter Class |  |  |
|  | CenterFrequency | NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ | ScopeSession.Channels[].Measurement.Filter.CenterFrequency |
|  | CutoffFrequency | NISCOPE_ATTR_MEAS_FILTER_CUTOFF_FREQ | ScopeSession.Channels[].Measurement.Filter.CutoffFrequency |
|  | FirFilterWindow | NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW | ScopeSession.Channels[].Measurement.Filter.FirFilterWindow |
|  | Order | NISCOPE_ATTR_MEAS_FILTER_ORDER | ScopeSession.Channels[].Measurement.Filter.Order |
|  | Ripple | NISCOPE_ATTR_MEAS_FILTER_RIPPLE | ScopeSession.Channels[].Measurement.Filter.Ripple |
|  | Taps | NISCOPE_ATTR_MEAS_FILTER_TAPS | ScopeSession.Channels[].Measurement.Filter.Taps |
|  | TransientPercent | NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT | ScopeSession.Channels[].Measurement.Filter.TransientPercent |
|  | Type | NISCOPE_ATTR_MEAS_FILTER_TYPE | ScopeSession.Channels[].Measurement.Filter.Type |
|  | Width | NISCOPE_ATTR_MEAS_FILTER_WIDTH | ScopeSession.Channels[].Measurement.Filter.Width |
|  | ScopeChannelMeasurementReferenceLevel Class |  |  |
|  | High | NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL | ScopeSession.Channels[].Measurement.ReferenceLevel.High |
|  | Low | NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL | ScopeSession.Channels[].Measurement.ReferenceLevel.Low |
|  | Mid | NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL | ScopeSession.Channels[].Measurement.ReferenceLevel.Mid |
|  | PercentageMethod | NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD | ScopeSession.Channels[].Measurement.ReferenceLevel.PercentageMethod |
|  | Units | NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS | ScopeSession.Channels[].Measurement.ReferenceLevel.Units |
|  | ScopeChannelMeasurementTimeHistogram Class |  |  |
|  | HighTime | NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME | ScopeSession.Channels[].Measurement.TimeHistogram.HighTime |
|  | HighVolts | NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS | ScopeSession.Channels[].Measurement.TimeHistogram.HighVolts |
|  | LowTime | NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME | ScopeSession.Channels[].Measurement.TimeHistogram.LowTime |
|  | LowVolts | NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS | ScopeSession.Channels[].Measurement.TimeHistogram.LowVolts |
|  | Size | NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE | ScopeSession.Channels[].Measurement.TimeHistogram.Size |
|  | ScopeChannelMeasurementVoltageHistogram Class |  |  |
|  | HighVolts | NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS | ScopeSession.Channels[].Measurement.VoltageHistogram.HighVolts |
|  | LowVolts | NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS | ScopeSession.Channels[].Measurement.VoltageHistogram.LowVolts |
|  | Size | NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE | ScopeSession.Channels[].Measurement.VoltageHistogram.Size |
|  | ScopeClockSynchronizationPulseSource Class | NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE |  |
|  | NoSource | NISCOPE_VAL_NO_SOURCE |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeDigitalEdgeAdvanceTrigger Class |  |  |
|  | Source | NISCOPE_ATTR_ADV_TRIG_SRC | ScopeSession.Trigger.AdvanceTrigger.DigitalEdge.Source |
|  | ScopeDigitalEdgeArmReferenceTrigger Class |  |  |
|  | Source | NISCOPE_ATTR_ARM_REF_TRIG_SRC | ScopeSession.Trigger.ArmReferenceTrigger.DigitalEdge.Source |
|  | ScopeDigitalEdgeStartTrigger Class |  |  |
|  | Source | NISCOPE_ATTR_ACQ_ARM_SOURCE | ScopeSession.Trigger.StartTrigger.DigitalEdge.Source |
|  | ScopeDigitalEdgeStartTriggerSource Class | NISCOPE_ATTR_ACQ_ARM_SOURCE |  |
|  | Immediate | NISCOPE_VAL_IMMEDIATE |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | SoftwareTriggerFunction | NISCOPE_VAL_SW_TRIG_FUNC |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeDriverOperation Class |  |  |
| IIviDriverOperation.Cache | Cache | NISCOPE_ATTR_CACHE | ScopeSession.DriverOperation.Cache |
| IIviDriverOperation.Coercion | Coercion |  | ScopeSession.DriverOperation.Coercion |
| IIviDriverOperation.DriverSetup | DriverSetup | NISCOPE_ATTR_DRIVER_SETUP | ScopeSession.DriverOperation.DriverSetup |
|  | InterchangeCheck | NISCOPE_ATTR_INTERCHANGE_CHECK | ScopeSession.DriverOperation.InterchangeCheck |
| IIviDriverOperation.IOResourceDescriptor | IOResourceDescriptor | NISCOPE_ATTR_RESOURCE_DESCRIPTOR | ScopeSession.DriverOperation.IOResourceDescriptor |
| IIviDriverOperation.LogicalName | LogicalName | NISCOPE_ATTR_LOGICAL_NAME | ScopeSession.DriverOperation.LogicalName |
| IIviDriverOperation.QueryInstrumentStatus | QueryInstrumentStatus | NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS | ScopeSession.DriverOperation.QueryInstrumentStatus |
| IIviDriverOperation.RangeCheck | RangeCheck | NISCOPE_ATTR_RANGE_CHECK | ScopeSession.DriverOperation.RangeCheck |
| IIviDriverOperation.Simulate | Simulate | NISCOPE_ATTR_SIMULATE | ScopeSession.DriverOperation.Simulate |
| IIviDriverOperation.InvalidateAllAttributes | InvalidateAllAttributes | niScope_InvalidateAllAttributes | ScopeSession.DriverOperation.InvalidateAllAttributes |
| IIviDriverOperation.ResetInterchangeCheck | ResetInterchangeCheck | niScope_ResetInterchangeCheck | ScopeSession.DriverOperation.ResetInterchangeCheck |
| IIviDriverOperation.InterchangeCheckWarning | InterchangeCheckWarning |  | ScopeSession.DriverOperation.InterchangeCheck |
| IIviDriverOperation.Warning | Warning |  | ScopeSession.DriverOperation.Warning |
|  | ScopeDriverUtility Class |  |  |
| IIviDriverUtility.Disable | Disable | niScope_Disable | ScopeSession.Utility.Disable |
|  | ExportAttributeConfigurationBuffer | niScope_ExportAttributeConfigurationBuffer |  |
|  | ExportAttributeConfigurationFile | niScope_ExportAttributeConfigurationFile |  |
|  | FpgaBitFilePath | NISCOPE_ATTR_FPGA_BITFILE_PATH | ScopeSession.Utility.FpgaBitFilePath |
|  | ImportAttributeConfigurationBuffer | niScope_ImportAttributeConfigurationBuffer |  |
|  | ImportAttributeConfigurationFile | niScope_ImportAttributeConfigurationFile |  |
|  | QueryDriverRevision | niScope_revision_query | ScopeSession.Utility.QueryDriverRevision |
| IIviDriverUtility.Reset | Reset | niScope_reset | ScopeSession.Utility.Reset |
|  | ResetDevice | niScope_ResetDevice | ScopeSession.Utility.ResetDevice |
| IIviDriverUtility.ResetWithDefaults | ResetWithDefaults | niScope_ResetWithDefaults | ScopeSession.Utility.ResetWithDefaults |
| IIviDriverUtility.SelfTest | SelfTest | niScope_self_test | ScopeSession.Utility.SelfTest |
| IIviDriverUtility.ErrorQuery |  |  |  |
|  | ScopeEdgeTrigger Class |  |  |
|  | Slope | NISCOPE_ATTR_TRIGGER_SLOPE | ScopeSession.Trigger.EdgeTrigger.Slope |
|  | Configure | niScope_ConfigureTriggerEdge | ScopeSession.Trigger.EdgeTrigger.Configure |
|  | ScopeChannelEqualizationFilter Class |  |  |
|  | Enabled | NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED | ScopeSession.Channels[].OnboardSignalProcessing.EqualizationFilter.Enabled |
|  | GetCoefficients | niScope_GetEqualizationFilterCoefficients | ScopeSession.Channels[].OnboardSignalProcessing.EqualizationFilter.GetCoefficients |
|  | NumberOfCoefficients | NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS | ScopeSession.Channels[].OnboardSignalProcessing.EqualizationFilter.NumberOfCoefficients |
|  | ConfigureCoefficients | niScope_ConfigureEqualizationFilterCoefficients | ScopeSession.Channels[].OnboardSignalProcessing.EqualizationFilter.ConfigureCoefficients |
|  | ScopeDriverIdentity Class |  |  |
| IIviComponentIdentity.Description | Description | NISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION | ScopeSession.Identity.Description |
| IIviDriverIdentity.Identifier | Identifier |  | ScopeSession.Identity.Description |
| IIviDriverIdentity.InstrumentFirmwareRevision | InstrumentFirmwareRevision | NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION | ScopeSession.Identity.InstrumentFirmwareRevision |
| IIviDriverIdentity.IIviDriverIdentity.InstrumentManufacturer | InstrumentManufacturer | NISCOPE_ATTR_INSTRUMENT_MANUFACTURER | ScopeSession.Identity.InstrumentManufacturer |
| IIviDriverIdentity.InstrumentModel | InstrumentModel | NISCOPE_ATTR_INSTRUMENT_MODEL | ScopeSession.Identity.InstrumentModel |
| IIviComponentIdentity.Revision | Revision | NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION | ScopeSession.Identity.Revision |
| IIviComponentIdentity.SerialNumber | SerialNumber | NISCOPE_ATTR_SERIAL_NUMBER | ScopeSession.Identity.SerialNumber |
| IIviDriverIdentity.SpecificationMajorVersion | SpecificationMajorVersion | NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | ScopeSession.Identity.SpecificationMajorVersion |
| IIviDriverIdentity.SpecificationMinorVersion | SpecificationMinorVersion | NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | ScopeSession.Identity.SpecificationMinorVersion |
| IIviComponentIdentity.Vendor | Vendor | NISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR | ScopeSession.Identity.Vendor |
| IIviDriverIdentity.GetGroupCapabilities | GetGroupCapabilities | NISCOPE_ATTR_GROUP_CAPABILITIES | ScopeSession.Identity.GetGroupCapabilities |
| IIviDriverIdentity.GetSupportedInstrumentModels | GetSupportedInstrumentModels | NISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS | ScopeSession.Identity.GetSupportedInstrumentModels |
|  | ScopeExportedSignals Class |  |  |
|  | AdvanceTriggerOutputTerminal | NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.AdvanceTriggerOutputTerminal |
|  | EndOfAcquisitionEventOutputTerminal | NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.EndOfAcquisitionEventOutputTerminal |
|  | EndOfRecordEventOutputTerminal | NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.EndOfRecordEventOutputTerminal |
|  | FiveVoltOutputTerminal | NISCOPE_ATTR_5V_OUT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.FiveVoltOutputTerminal |
|  | ReadyForAdvanceEventOutputTerminal | NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.ReadyForAdvanceEventOutputTerminal |
|  | ReadyForReferenceEventOutputTerminal | NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.ReadyForReferenceEventOutputTerminal |
|  | ReadyForStartEventOutputTerminal | NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.ReadyForStartEventOutputTerminal |
|  | ReferenceClockOutputTerminal | NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE | ScopeSession.ExportedSignals.SampleClockOutputTerminal |
|  | ReferenceTriggerOutputTerminal | NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.ReferenceTriggerOutputTerminal |
|  | SampleClockOutputTerminal | NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.SampleClockOutputTerminal |
|  | StartTriggerOutputTerminal | NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | ScopeSession.ExportedSignals.StartTriggerOutputTerminal |
|  | ScopeEndOfAcquisitionEventOutputTerminal Class | NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeEndOfRecordEventOutputTerminal Class | NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeExternalCalibration Class |  |  |
|  | ExternalCalibrationDate | niScope_CalFetchDate | ScopeSession.Calibration.External.ExternalCalibrationDate |
|  | ExternalCalibrationTemperature | niScope_CalFetchTemperature | ScopeSession.Calibration.External.ExternalCalibrationTemperature |
|  | ScopeFiveVoltsOutOutputTerminal Class | NISCOPE_ATTR_5V_OUT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeFractionalResample Class |  |  |
|  | Enabled | NISCOPE_ATTR_FRACTIONAL_RESAMPLE_ENABLED | ScopeSession.Timing.FractionalResample.Enabled |
|  | ScopeInputClockSource Class | NISCOPE_ATTR_INPUT_CLOCK_SOURCE |  |
|  | Aux0ClkIn | NISCOPE_VAL_AUX_0_CLK_IN |  |
|  | NoSource | NISCOPE_VAL_NO_SOURCE |  |
|  | RtsiClock | NISCOPE_VAL_RTSI_CLOCK |  |
|  | PxiClock | NISCOPE_VAL_PXI_CLOCK |  |
|  | External | NISCOPE_VAL_PXI_EXTERNAL |  |
|  | ClkIn | NISCOPE_VAL_CLK_IN |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeMeasurement Class |  |  |
|  | FetchInterleavedData | NISCOPE_ATTR_FETCH_INTERLEAVED_DATA | ScopeSession.Measurement.FetchInterleavedData |
|  | FetchInterleavedIQData | NISCOPE_ATTR_FETCH_INTERLEAVED_IQ_DATA | ScopeSession.Measurement.FetchInterleavedIQData |
|  | FetchOffset | NISCOPE_ATTR_FETCH_OFFSET | ScopeSession.Measurement.FetchOffset |
|  | FetchRelativeTo | NISCOPE_ATTR_FETCH_RELATIVE_TO | ScopeSession.Measurement.FetchRelativeTo |
|  | PointsDone | NISCOPE_ATTR_POINTS_DONE | ScopeSession.Measurement.PointsDone |
|  | RecordsDone | NISCOPE_ATTR_RECORDS_DONE | ScopeSession.Measurement.RecordsDone |
|  | RisInAutoSetupAllowed | NISCOPE_ATTR_RIS_IN_AUTO_SETUP_ENABLE | ScopeSession.Measurement.RisInAutoSetupAllowed |
|  | Abort | niScope_Abort | ScopeSession.Measurement.Abort |
|  | AutoSetup | niScope_AutoSetup | ScopeSession.Measurement.AutoSetup |
|  | Commit | niScope_Commit | ScopeSession.Measurement.Commit |
|  | Initiate | niScope_InitiateAcquisition | ScopeSession.Measurement.Initiate |
|  | Status | niScope_AcquisitionStatus | ScopeSession.Measurement.Status |
|  | ScopeOutputClockSource Class | NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE |  |
|  | Aux0ClkOut | NISCOPE_VAL_AUX_0_CLK_OUT |  |
|  | NoSource | NISCOPE_VAL_NO_SOURCE |  |
|  | RtsiClock | NISCOPE_VAL_RTSI_CLOCK |  |
|  | ClkOut | NISCOPE_VAL_CLK_OUT |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeReadyForAdvanceEventOutputTerminal Class | NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeReadyForReferenceEventOutputTerminal Class | NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeReadyForStartEventOutputTerminal Class | NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeReferenceLevel Class |  |  |
|  | High | NISCOPE_ATTR_MEAS_HIGH_REF | TBD |
|  | Low | NISCOPE_ATTR_MEAS_LOW_REF | TBD |
|  | Mid | NISCOPE_ATTR_MEAS_MID_REF | TBD |
|  | ScopeReferenceTrigger Class |  |  |
|  | Delay | NISCOPE_ATTR_TRIGGER_DELAY_TIME | ScopeSession.Trigger.ReferenceTrigger.Delay |
|  | DetectorLocation | NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION | ScopeSession.Trigger.ReferenceTrigger.DetectorLocation |
|  | Hysteresis | NISCOPE_ATTR_TRIGGER_HYSTERESIS | ScopeSession.Trigger.ReferenceTrigger.Hysteresis |
|  | QuietTimeMin | NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME | ScopeSession.Trigger.ReferenceTrigger.QuietTimeMin |
|  | ReferencePosition | NISCOPE_ATTR_HORZ_RECORD_REF_POSITION | ScopeSession.Trigger.ReferenceTrigger.ReferencePosition |
|  | SendSoftwareEdgeTrigger | niScope_SendSoftwareTriggerEdge | ScopeSession.Trigger.ReferenceTrigger.SendSoftwareEdgeTrigger |
|  | ScopeReferenceTriggerExportedOutputTerminal Class | NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeSampleClockExportedOutputTerminal Class | NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL |  |
|  | NoSource | NISCOPE_VAL_NO_SOURCE |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | ClkOut | NISCOPE_VAL_CLK_OUT |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeSampleClockTimebaseSource Class | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC |  |
|  | ClkIn | NISCOPE_VAL_CLK_IN |  |
|  | NoSource | NISCOPE_VAL_NO_SOURCE |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | PxieDStarA | NISCOPE_VAL_PXIE_DSTAR_A |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeSelfCalibration Class |  |  |
|  | SelfCalibrate | niScope_CalSelfCalibrate | ScopeSession.Calibration.Self.SelfCalibration |
|  | SelfCalibrationDate | niScope_CalFetchDate | ScopeSession.Calibration.Self.SelfCalibrationDate |
|  | SelfCalibrationTemperature | niScope_CalFetchTemperature | ScopeSession.Calibration.Self.SelfCalibrationTemperature |
|  | ScopeStartTrigger Class |  |  |
|  | SendSoftwareEdgeTrigger | niScope_SendSoftwareTriggerEdge | ScopeSession.Trigger.StartTrigger.SendSoftwareEdgeTrigger |
|  | ScopeStartTriggerExportedOutputTerminal Class | NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | ScopeTiming Class |  |  |
|  | AbsoluteSampleClockOffset | NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET | ScopeSession.Timing.AbsoluteSampleClockOffset |
|  | ClockSynchronizationPulseSource | NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE | ScopeSession.Timing.ClockSynchronizationPulseSource |
|  | EnforceRealtime | NISCOPE_ATTR_HORZ_ENFORCE_REALTIME | ScopeSession.Timing.EnforceRealtime |
|  | MoreRecordsThanMemoryAllowed | NISCOPE_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY | ScopeSession.Timing.MoreRecordsThanMemoryAllowed |
|  | NumberOfRecordsToAcquire | NISCOPE_ATTR_HORZ_NUM_RECORDS | ScopeSession.Timing.NumberOfRecordsToAcquire |
|  | OnboardMemorySize | NISCOPE_ATTR_ONBOARD_MEMORY_SIZE | ScopeSession.Timing.OnboardMemorySize |
|  | OscillatorPhaseDac | NISCOPE_ATTR_OSCILLATOR_PHASE_DAC_VALUE | ScopeSession.Timing.OscillatorPhaseDac |
|  | PllLockStatus | NISCOPE_ATTR_PLL_LOCK_STATUS | ScopeSession.Timing.PllLockStatus |
|  | PollInterval | NISCOPE_ATTR_POLL_INTERVAL | ScopeSession.Timing.PollInterval |
|  | RealtimeSampleRateMax | NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE | ScopeSession.Timing.RealtimeSampleRateMax |
|  | ReferenceClockRate | NISCOPE_ATTR_REF_CLK_RATE | ScopeSession.Timing.ReferenceClockRate |
|  | ReferenceClockSource | NISCOPE_ATTR_INPUT_CLOCK_SOURCE | ScopeSession.Timing.ReferenceClockSource |
|  | RisAverages | NISCOPE_ATTR_RIS_NUM_AVERAGES | ScopeSession.Timing.RisAverages |
|  | RisMethod | NISCOPE_ATTR_RIS_METHOD | ScopeSession.Timing.RisMethod |
|  | RisRateMax | NISCOPE_ATTR_MAX_RIS_RATE | ScopeSession.Timing.RisRateMax |
|  | SampleClockTimebaseDivisor | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV | ScopeSession.Timing.SampleClockTimebaseDiv |
|  | SampleClockTimebaseRate | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE | ScopeSession.Timing.SampleClockTimebaseRate |
|  | SampleClockTimebaseSource | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC | ScopeSession.Timing.SampleClockTimebaseSource |
|  | SampleClockTimebaseMultiplier | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_MULT | ScopeSession.Timing.SampleClockTimebaseMultiplier |
|  | AdjustSampleClockRelativeDelay | niScope_AdjustSampleClockRelativeDelay | ScopeSession.Timing.AdjustSampleClockRelativeDelay |
|  | ConfigureClock | niScope_ConfigureClock | ScopeSession.Timing.ConfigureClock |
|  | ConfigureTiming | niScope_ConfigureHorizontalTiming | ScopeSession.Timing.ConfigureTiming |
|  | ScopeTrigger Class |  |  |
|  | Coupling | NISCOPE_ATTR_TRIGGER_COUPLING | ScopeSession.Trigger.Coupling |
|  | EndOfRecordToAdvanceTriggerHoldoff | NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF | ScopeSession.Trigger.EndOfRecordToAdvanceTriggerHoldoff |
|  | ExternalTriggerSourceImpedance | NISCOPE_ATTR_TRIGGER_IMPEDANCE | ScopeSession.Trigger.ExternalTriggerSourceImpedance |
|  | Holdoff | NISCOPE_ATTR_TRIGGER_HOLDOFF | ScopeSession.Trigger.Holdoff |
|  | IsAutoTriggered | NISCOPE_ATTR_TRIGGER_AUTO_TRIGGERED | ScopeSession.Trigger.IsAutoTriggered |
|  | Level | NISCOPE_ATTR_TRIGGER_LEVEL | ScopeSession.Trigger.Level |
|  | Modifier | NISCOPE_ATTR_TRIGGER_MODIFIER | ScopeSession.Trigger.Modifier |
|  | Source | NISCOPE_ATTR_TRIGGER_SOURCE | ScopeSession.Trigger.Source |
|  | StartToReferenceTriggerHoldoff | NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF | ScopeSession.Trigger.StartToReferenceTriggerHoldoff |
|  | TdcEnable | NISCOPE_ATTR_REF_TRIG_TDC_ENABLE | ScopeSession.Trigger.TdcEnable |
|  | Type | NISCOPE_ATTR_TRIGGER_TYPE | ScopeSession.Trigger.Type |
|  | Configure | niScope_ConfigureTrigger | ScopeSession.Trigger.Configure |
|  | ConfigureTriggerDigital | niScope_ConfigureTriggerDigital | ScopeSession.Trigger.ConfigureTriggerDigital |
|  | ConfigureTriggerHysteresis | niScope_ConfigureTriggerHysteresis | ScopeSession.Trigger.ConfigureTriggerHysteresis |
|  | ConfigureTriggerImmediate | niScope_ConfigureTriggerImmediate | ScopeSession.Trigger.ConfigureTriggerImmediate |
|  | ConfigureTriggerSoftware | niScope_ConfigureTriggerSoftware | ScopeSession.Trigger.ConfigureTriggerSoftware |
|  | ConfigureTriggerWindow | niScope_ConfigureTriggerWindow | ScopeSession.Trigger.ConfigureTriggerWindow |
|  | ScopeTriggerSource Class | NISCOPE_ATTR_TRIGGER_SOURCE |  |
|  | Aux0Pfi0 | NISCOPE_VAL_AUX_0_PFI_0 |  |
|  | Aux0Pfi1 | NISCOPE_VAL_AUX_0_PFI_1 |  |
|  | Aux0Pfi2 | NISCOPE_VAL_AUX_0_PFI_2 |  |
|  | Aux0Pfi3 | NISCOPE_VAL_AUX_0_PFI_3 |  |
|  | Aux0Pfi4 | NISCOPE_VAL_AUX_0_PFI_4 |  |
|  | Aux0Pfi5 | NISCOPE_VAL_AUX_0_PFI_5 |  |
|  | Aux0Pfi6 | NISCOPE_VAL_AUX_0_PFI_6 |  |
|  | Aux0Pfi7 | NISCOPE_VAL_AUX_0_PFI_7 |  |
|  | Immediate | NISCOPE_VAL_IMMEDIATE |  |
|  | External | NISCOPE_VAL_EXTERNAL |  |
|  | SoftwareTriggerFunction | NISCOPE_VAL_SW_TRIG_FUNC |  |
|  | PxiStar | NISCOPE_VAL_PXI_STAR |  |
|  | Rtsi0 | NISCOPE_VAL_RTSI_0 |  |
|  | Rtsi1 | NISCOPE_VAL_RTSI_1 |  |
|  | Rtsi2 | NISCOPE_VAL_RTSI_2 |  |
|  | Rtsi3 | NISCOPE_VAL_RTSI_3 |  |
|  | Rtsi4 | NISCOPE_VAL_RTSI_4 |  |
|  | Rtsi5 | NISCOPE_VAL_RTSI_5 |  |
|  | Rtsi6 | NISCOPE_VAL_RTSI_6 |  |
|  | Rtsi7 | NISCOPE_VAL_RTSI_7 |  |
|  | Pfi0 | NISCOPE_VAL_PFI_0 |  |
|  | Pfi1 | NISCOPE_VAL_PFI_1 |  |
|  | Pfi2 | NISCOPE_VAL_PFI_2 |  |
|  | Channel0 | 0 |  |
|  | Channel1 | 1 |  |
|  | Channel2 | 2 |  |
|  | Channel3 | 3 |  |
|  | Channel4 | 4 |  |
|  | Channel5 | 5 |  |
|  | Channel6 | 6 |  |
|  | Channel7 | 7 |  |
|  | ScopeTVTrigger Class |  |  |
|  | DCRestoreEnabled | NISCOPE_ATTR_ENABLE_DC_RESTORE | ScopeSession.Trigger.TV.DCRestoreEnabled |
|  | LineNumber | NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER | ScopeSession.Trigger.TV.LineNumber |
|  | Polarity | NISCOPE_ATTR_TV_TRIGGER_POLARITY | ScopeSession.Trigger.TV.Polarity |
|  | SignalFormat | NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT | ScopeSession.Trigger.TV.Polarity |
|  | TriggerEvent | NISCOPE_ATTR_TV_TRIGGER_EVENT | ScopeSession.Trigger.TV.Polarity |
|  | Configure | niScope_ConfigureTriggerVideo | ScopeSession.Trigger.TV.Configure |
|  | ScopeWindowReferenceTrigger Class |  |  |
|  | HighLevel | NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL | ScopeSession.Trigger.ReferenceTrigger.Window.HighLevel |
|  | LowLevel | NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL | ScopeSession.Trigger.ReferenceTrigger.Window.LowLevel |
|  | Mode | NISCOPE_ATTR_TRIGGER_WINDOW_MODE | ScopeSession.Trigger.ReferenceTrigger.Window.Mode |

Parent topic:

NI-SCOPE .NET Class Library Help
