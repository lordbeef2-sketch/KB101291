# NI DOCUMENT BUNDLE: ni-dmm-net-api-overview

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-net-api-overview start=1 end=6 -->
<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=fetch-read-dmm-dotnet.html language=enus -->
## TOPIC 00001: Using Memory-Optimized and Async Methods to Fetch and Read

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `fetch-read-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/fetch-read-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Fetch and Read methods are in the DmmMeasurement and DmmWaveformAcquisition classes. A session must be open and configured correctly for reading. In case of fetch, the session must be open, configured correctly, and initiated before the actual fetch. Reading is equivalent to initiating the acqui

Using Memory-Optimized and Async Methods to Fetch and Read

The Fetch and Read methods are in the DmmMeasurement and DmmWaveformAcquisition classes. A session must be open and configured correctly for reading. In case of fetch, the session must be open, configured correctly, and initiated before the actual fetch. Reading is equivalent to initiating the acquisition and fetching the results. Calling Read() combines Initiate() and Fetch() into one call. Read() is suitable for simple acquisitions. Initiate() and Fetch() are better suited for complex applications.

The Read and Fetch methods can be categorized into:

- Normal methods
- Memory-optimized methods
- Async methods
- Async memory-optimized methods

Normal overloads have the option of specifying the number of points to fetch and maximum time allowed for the operation to complete. Each of the overloads has a corresponding memory-optimized overload and async overload.

#### Memory-Optimized Methods

Memory-optimized methods perform the fetch operation on pre-allocated memory.

If you fetch or read large amounts of data, and your application processes data between each call, and the acquired data is not necessary after processing, you can use the memory-optimized method overloads of the reader classes to improve the performance of your application.

Memory-optimized methods take an object that stores the acquired data. These overloads do not allocate memory if the buffer object passed is large enough to hold the amount of data being fetched or read, which prevents the overhead of .NET memory allocation and garbage collection. As a result, performance will improve for applications that fetch or read large amount of data.

```text
          VB.NET

Dim reading As Double() = New Double(999) {}
Dim dmmSession As New NIDmm("DMM-4072", False, False)
dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, 0.0001)
dmmSession.Trigger.MultiPoint.SampleCount = 2000
dmmSession.Measurement.Initiate()

Dim actualNumberOfPoints As Integer 

'Passing the reading for the first time.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, actualNumberOfPoints, reading)

'Process the reading using the 'reading' variable, then fetch next few samples into the 
'same variable, which reuses rather than reallocates memory. 
'Ensure that the data in the 'reading' variable is no longer needed.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, actualNumberOfPoints, reading)
```

```text
          C#

double[] reading = new double[1000];
NIDmm dmmSession = new NIDmm("DMM-4072", false, false);
dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, .0001);
dmmSession.Trigger.MultiPoint.SampleCount = 2000;
dmmSession.Measurement.Initiate();

int actualNumberOfPoints;
//Passing the reading for the first time.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, out actualNumberOfPoints, ref reading);

//Process the reading using the 'reading' variable, then fetch next few samples into the 
//same variable, which reuses rather than reallocates memory. 
//Ensure that the data in the 'reading' variable is no longer needed.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, out actualNumberOfPoints, ref reading);
```

#### Async Methods

For every non-asynchronous fetch and read method, there is a method which does the same operation asynchronously. We follow the event-based asynchronous pattern. These asynchronous methods perform the fetch or read operation in a separate worker thread and return the data through OperationCompleted events. Each of these asynchronous methods has a corresponding OperationCompleted event. After an async method completes execution, its corresponding event occurs. You must handle this event to get the result of the asynchronous operation. The event handler to this event should take two parameters, one of type Object and another of type DmmMeasurementEventArgs<T>.

The following code shows how to read a sample number of points asynchronously.

```text
          VB.NET

Dim dmmSession As NIDmm
Dim result As Double()
Public Sub FetchAsync()
    dmmSession = New NIDmm("DMM-4072", False, False)
    AddHandler dmmSession.Measurement.ReadMultiPointCompleted, AddressOf Measurement_ReadMultipointCompleted
    dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, 0.0001)
    dmmSession.Trigger.MultiPoint.SampleCount = 10
    dmmSession.Measurement.ReadMultiPointAsync(10, Nothing)
End Sub 

Sub Measurement_ReadMultipointCompleted(ByVal sender As Object, ByVal e As DmmMeasurementEventArgs(Of Double()))
    If e.[Error] IsNot Nothing Then
        result = e.Reading
    End If
    dmmSession.Close()
End Sub
```

```text
          C#

NIDmm dmmSession;
double[] result;
public void Fetch()
{
    dmmSession = new NIDmm("DMM-4072", false, false);
    dmmSession.Measurement.ReadMultiPointCompleted += new EventHandler<DmmMeasurementEventArgs<double[]>>(Measurement_ReadMultiPointCompleted);
    dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, .0001);
    dmmSession.Trigger.MultiPoint.SampleCount = 10;
    dmmSession.Measurement.ReadMultiPointAsync(10, null);
}
void Measurement_ReadMultiPointCompleted(object sender, DmmMeasurementEventArgs<double[]> e)
{
    if (e.Error == null)
    {
        result = e.Reading;
    }
    dmmSession.Close();
}
```

#### Async Memory-Optimized Methods

There are asynchronous versions of memory-optimized methods. You use these asynchronous methods similarly to the way you use non-memory-optimized asynchronous methods. The only difference between memory-optimized asynchronous methods and non-memory-optimized asynchronous methods is that the asynchronous memory-optimized read or fetch methods take an additional buffer object that stores the data.

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=interchangeability-ivi-dmm-dotnet.html language=enus -->
## TOPIC 00002: Using the NI-DMM .NET Class Library in IVI.NET Applications

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `interchangeability-ivi-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/interchangeability-ivi-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: The .NET API for NI-DMM is IVI.NET class-compliant. You can use the NI-DMM .NET API to run IVI.NET-compliant applications using DMM hardware when you have the NI-DMM driver and the .NET API for NI-DMM installed. For more information, refer to the NI Digital Multimeters Help. Integrated help for IVI

Using the NI-DMM .NET Class Library in IVI.NET Applications

NI Digital Multimeters Help

Note

The .NET API for NI-DMM has two parts: the IVI.NET class-compliant API and the specific driver API. The following code snippet demonstrates how you can use an NI-DMM .NET specific driver API from a session obtained from an IVI.NET class-compliant API.

Note

OperationMode

IviDmmMode

OperationMode

WaveformMode

Note

IIviDmm

NIDmm

1. Create an IVI.NET class-compliant session object and acquire data, then create and use a specific driver NIDmm object to access device-specific functionality. 
 VB.NET

'Create an IVI DMM session. 
Dim iviDmmSession As IIviDmm = Ivi.Driver.IviDriver.Create(Of IIviDmm)("DMM-4072", True, True)
Dim currentRange As Double = 0.2 
Dim currentResolutionDigits As Double = 6.5
iviDmmSession.Configure(Ivi.Dmm.MeasurementFunction.DCCurrent, currentRange, currentResolutionDigits)

'Take a reading. 
Dim reading As Double = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2))

'Get an NIDmm session from the IVI DMM session and get a reading using the NIDmm session. 
Dim sampleDmmSession As NIDmm = TryCast(iviDmmSession.GetService(GetType(NIDmm)), NIDmm)
If sampleDmmSession IsNot Nothing Then 
 Dim waveformVoltageRange As Double = 10 
 Dim waveformPointsToRead As Integer = 100 
 Dim rate As Double = 100
 sampleDmmSession.ConfigureWaveformAcquisition(DmmMeasurementFunction.WaveformVoltage, waveformVoltageRange, rate, waveformPointsToRead)
 Dim readingArray As AnalogWaveform(Of Double) = sampleDmmSession.WaveformAcquisition.ReadWaveform(waveformPointsToRead, NationalInstruments.PrecisionTimeSpan.FromMilliseconds(10000))
Else 
 Dim voltageRange As Double = 10, voltageResolution As Double = 0.0001 
 Dim numberOfSamples As Integer = 100
 iviDmmSession.Configure(MeasurementFunction.DCVolts, voltageRange, voltageResolution)
 iviDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples
 iviDmmSession.Trigger.Source = "Immediate" 
 Dim readingArray As Double() = iviDmmSession.Measurement.ReadMultiPoint(Ivi.Driver.PrecisionTimeSpan.FromMilliseconds(20000))
End If
iviDmmSession.Close()
 C# 

// Create an IVI DMM session.
IIviDmm iviDmmSession = Ivi.Driver.IviDriver.Create<IIviDmm>("DMM-4072", true, true);
double currentRange = 0.2;
double currentResolutionDigits = 6.5;
iviDmmSession.Configure(Ivi.Dmm.MeasurementFunction.DCCurrent, currentRange, currentResolutionDigits);

//Take a reading. 
double reading = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2));

//Get an NIDmm session from the IVI DMM session and get a reading using the NIDmm session.
NIDmm sampleDmmSession = iviDmmSession.GetService(typeof(NIDmm)) as NIDmm;
if (sampleDmmSession != null)
{
 double waveformVoltageRange = 10;
 int waveformPointsToRead = 100;
 double rate = 100;
 sampleDmmSession.ConfigureWaveformAcquisition(DmmMeasurementFunction.WaveformVoltage, waveformVoltageRange, rate, waveformPointsToRead);
 AnalogWaveform<double> readingArray = sampleDmmSession.WaveformAcquisition.ReadWaveform(waveformPointsToRead, NationalInstruments.PrecisionTimeSpan.FromMilliseconds(10000));
}
else
{
 double voltageRange = 10, voltageResolution = 0.0001;
 int numberOfSamples = 100;
 iviDmmSession.Configure(MeasurementFunction.DCVolts, voltageRange, voltageResolution);
 iviDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples;
 iviDmmSession.Trigger.Source = "Immediate";
 double[] readingArray = iviDmmSession.Measurement.ReadMultiPoint(Ivi.Driver.PrecisionTimeSpan.FromMilliseconds(20000));
}
iviDmmSession.Close();
2. Switch from an NI-DMM .NET-specific driver session to an IVI.NET DMM session in the application. 
 org.dita.html5/xsl/topic.xsl 455Note Before obtaining an IIviDmm reference from an existing NIDmm that is configured for waveform acquisition, set the OperationMode to IviDmmMode.
 VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5 
' Use the NIDmm session as an IVI DMM session.
sampleDmmSession.OperationMode = DmmOperationMode.IviDmmMode
Dim serviceProvider As IServiceProvider = TryCast(sampleDmmSession, IServiceProvider)
Dim iviDmmSession As IIviDmm = TryCast(serviceProvider.GetService(GetType(IIviDmm)), IIviDmm)
If iviDmmSession IsNot Nothing Then
 iviDmmSession.Configure(MeasurementFunction.DCVolts, range, resolution)
 Dim reading As Double = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2))
End If
sampleDmmSession.Close()
 C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
// Use the NIDmm session as an IVI DMM session.
sampleDmmSession.OperationMode = DmmOperationMode.IviDmmMode;
IServiceProvider serviceProvider = sampleDmmSession as IServiceProvider;
IIviDmm iviDmmSession = serviceProvider.GetService(typeof(IIviDmm)) as IIviDmm;
if (iviDmmSession != null)
{
 iviDmmSession.Configure(MeasurementFunction.DCVolts, range, resolution);
 double reading = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2));
}
sampleDmmSession.Close();

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=mapping-c-api-dmm-dotnet.html language=enus -->
## TOPIC 00003: Mapping the NI-DMM .NET API to the NI-DMM C API

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `mapping-c-api-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/mapping-c-api-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-DMM .NET API members to the corresponding NI-DMM C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIDmm namespace. IVI .NET API Member .NET API Member C API Member DmmCalibration Class UserDefinedInfoMaximumSize niDMM_

Mapping the NI-DMM .NET API to the NI-DMM C API

The following table maps the NI-DMM .NET API members to the corresponding NI-DMM C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIDmm namespace.

| IVI .NET API Member | .NET API Member | C API Member |
| --- | --- | --- |
|  | DmmCalibration Class |  |
|  | UserDefinedInfoMaximumSize | niDMM_GetCalUserDefinedInfoMaxSize |
|  | ExternalCalibrationRecommendedInterval | niDMM_GetExtCalRecommendedInterval |
|  | GetCalibrationCount | niDMM_GetCalCount |
|  | GetCalibrationDateAndTime | niDMM_GetCalDateAndTime |
|  | GetDeviceTemperature | niDMM_GetDevTemp |
|  | GetLastCalibrationTemperature | niDMM_GetLastCalTemp |
|  | SelfCalibrate | niDMM_SelfCal |
|  | RestoreLastExternalCalibrationConstants | niDMM_RestoreLastExtCalConstants |
|  | SetCalibrationPassword | niDMM_SetCalPassword |
|  | IsSelfCalibrationSupported | niDMM_GetSelfCalSupported |
|  | UserDefinedInfo | niDMM_GetCalUserDefinedInfo / niDMM_SetCalUserDefinedInfo |
|  | NIDmm Class |  |
| Ivi.Driver.IIviDriver.Close | Close | niDMM_close |
| Ivi.Dmm.IIviDmm.Configure | Configure | niDMM_ConfigureMeasurementAbsolute |
|  | ConfigureMeasurementDigits | niDMM_ConfigureMeasurementDigits |
|  | ConfigureWaveformAcquisition | niDMM_ConfigureWaveformAcquisition |
| Ivi.Dmm.IIviDmm.AutoRange | AutoRange | NIDMM_ATTR_RANGE |
|  | MeasurementPeriod | niDMM_GetMeasurementPeriod |
|  | InputResistance | NIDMM_ATTR_INPUT_RESISTANCE |
|  | CurrentSource | NIDMM_ATTR_CURRENT_SOURCE |
| Ivi.Dmm.IIviDmm.Resolution | Resolution | NIDMM_ATTR_RESOLUTION_ABSOLUTE |
|  | DigitsResolution | NIDMM_ATTR_RESOLUTION_DIGITS |
| Ivi.Dmm.IIviDmm.Range | Range | NIDMM_ATTR_RANGE |
| Ivi.Dmm.IIviDmm.MeasurementFunction | MeasurementFunction | NIDMM_ATTR_FUNCTION |
|  | OperationMode | NIDMM_ATTR_OPERATION_MODE |
|  | DmmAC Class |  |
| Ivi.Dmm.IIviDmmAC.ConfigureBandwidth | ConfigureBandwidth | niDMM_ConfigureACBandwidth |
| Ivi.Dmm.IIviDmmAC.FrequencyMin | FrequencyMin | NIDMM_ATTR_AC_MIN_FREQ |
| Ivi.Dmm.IIviDmmAC.FrequencyMax | FrequencyMax | NIDMM_ATTR_AC_MAX_FREQ |
|  | DmmMeasurement Class |  |
| Ivi.Dmm.IIviDmmMeasurement.Abort | Abort | niDMM_Abort |
| Ivi.Dmm.IIviDmmMeasurement.Fetch | Fetch | niDMM_Fetch |
| Ivi.Dmm.IIviDmmMeasurement.FetchMultiPoint | FetchMultiPoint | niDMM_FetchMultiPoint |
|  | MemoryOptimizedFetchMultiPoint | niDMM_FetchMultiPoint |
|  | FetchMultiPointAsync | niDMM_FetchMultiPoint |
|  | MemoryOptimizedFetchMultiPointAsync | niDMM_FetchMultiPoint |
| Ivi.Dmm.IIviDmmMeasurement.Initiate | Initiate | niDMM_Initiate |
|  | IsOverRange | niDMM_IsOverRange |
| Ivi.Dmm.IIviDmmMeasurement.ReadMultiPoint | ReadMultiPoint | niDMM_ReadMultiPoint |
|  | MemoryOptimizedReadMultiPoint | niDMM_ReadMultiPoint |
|  | ReadMultiPointAsync | niDMM_ReadMultiPoint |
|  | MemoryOptimizedReadMultiPointAsync | niDMM_ReadMultiPoint |
| Ivi.Dmm.IIviDmmMeasurement.SendSoftwareTrigger | SendSoftwareTrigger | niDMM_SendSoftwareTrigger |
|  | IsUnderRange | niDMM_IsUnderRange |
|  | Control | niDMM_Control |
|  | ReadAsync | niDMM_Read |
| Ivi.Dmm.IIviDmmMeasurement.Read | Read | niDMM_Read |
|  | ReadStatus | niDMM_ReadStatus |
|  | DmmTrigger Class |  |
| Ivi.Dmm.IIviDmmTrigger.DelayAuto | DelayAuto | NIDMM_ATTR_TRIGGER_DELAY |
| Ivi.Dmm.IIviDmmTrigger.MeasurementCompleteDestination | MeasurementCompleteDestination | NIDMM_ATTR_MEAS_COMPLETE_DEST |
|  | MeasurementCompleteDestinationSlope | NIDMM_ATTR_MEAS_DEST_SLOPE |
| Ivi.Dmm.IIviDmmTrigger.Configure | Configure | niDMM_ConfigureTrigger |
| Ivi.Dmm.IIviDmmTrigger.Source | Source | NIDMM_ATTR_TRIGGER_SOURCE |
| Ivi.Dmm.IIviDmmTrigger.Slope | Slope | NIDMM_ATTR_TRIGGER_SLOPE |
| Ivi.Dmm.IIviDmmTrigger.Delay | Delay | NIDMM_ATTR_TRIGGER_DELAY |
|  | DmmDriverIdentity Class |  |
| Ivi.Driver.IIviDriverIdentity.GetSupportedInstrumentModels | GetSupportedInstrumentModels | NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS |
| Ivi.Driver.IIviDriverIdentity.GetGroupCapabilities | GetGroupCapabilities | NIDMM_ATTR_GROUP_CAPABILITIES |
| Ivi.Driver.IIviComponentIdentity.Vendor | Vendor | NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR |
| Ivi.Driver.IIviComponentIdentity.Revision | Revision | NIDMM_ATTR_SPECIFIC_DRIVER_REVISION |
| Ivi.Driver.IIviComponentIdentity.Description | Description | NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| Ivi.Driver.IIviDriverIdentity.Identifier | Identifier | NIDMM_ATTR_INSTR_SERIAL_NUMBER |
| Ivi.Driver.IIviDriverIdentity.InstrumentModel | InstrumentModel | NIDMM_ATTR_INSTRUMENT_MODEL |
| Ivi.Driver.IIviDriverIdentity.InstrumentManufacturer | InstrumentManufacturer | NIDMM_ATTR_INSTRUMENT_MANUFACTURER |
| Ivi.Driver.IIviDriverIdentity.InstrumentFirmwareRevision | InstrumentFirmwareRevision | NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION |
|  | SpecificDriverPrefix | NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX |
|  | SpecificDriverMinorVersion | NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION |
|  | SpecificDriverMajorVersion | NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION |
|  | DmmDriverUtility Class |  |
| Ivi.Driver.IIviDriverUtility.SelfTest | SelfTest | niDMM_self_test |
| Ivi.Driver.IIviDriverUtility.ErrorQuery | ErrorQuery | niDMM_error_query |
|  | RevisionQuery | NIDMM_ATTR_SPECIFIC_DRIVER_REVISION |
| Ivi.Driver.IIviDriverUtility.Disable | Disable | niDMM_Disable |
| Ivi.Driver.IIviDriverUtility.ResetWithDefaults | ResetWithDefaults | niDMM_ResetWithDefaults |
| Ivi.Driver.IIviDriverUtility.Lock | Lock |  |
| Ivi.Driver.IIviDriverUtility.Reset | Reset | niDMM_reset |
|  | ExportAttributeConfigurationBuffer | niDMM_ExportAttributeConfigurationBuffer |
|  | ExportAttributeConfigurationFile | niDMM_ExportAttributeConfigurationFile |
|  | ImportAttributeConfigurationBuffer | niDMM_ImportAttributeConfigurationBuffer |
|  | ImportAttributeConfigurationFile | niDMM_ImportAttributeConfigurationFile |
|  | DmmDriverOperation Class |  |
| Ivi.Driver.IIviDriverOperation.ResetInterchangeCheck | ResetInterchangeCheck | niDMM_ResetInterchangeCheck |
| Ivi.Driver.IIviDriverOperation.InvalidateAllAttributes | InvalidateAllAttributes | niDMM_Control |
| Ivi.Driver.IIviDriverOperation.IOResourceDescriptor | IOResourceDescriptor | NIDMM_ATTR_RESOURCE_DESCRIPTOR |
| Ivi.Driver.IIviDriverOperation.LogicalName | LogicalName | NIDMM_ATTR_LOGICAL_NAME |
| Ivi.Driver.IIviDriverOperation.Simulate | Simulate | NIDMM_ATTR_SIMULATE |
|  | RecordValueCoercions | NIDMM_ATTR_RECORD_COERCIONS |
| Ivi.Driver.IIviDriverOperation.RangeCheck | RangeCheck | NIDMM_ATTR_RANGE_CHECK |
| Ivi.Driver.IIviDriverOperation.QueryInstrumentStatus | QueryInstrumentStatus | NIDMM_ATTR_QUERY_INSTR_STATUS |
|  | InterchangeCheck | NIDMM_ATTR_INTERCHANGE_CHECK |
| Ivi.Driver.IIviDriverOperation.DriverSetup | DriverSetup | NIDMM_ATTR_DRIVER_SETUP |
| Ivi.Driver.IIviDriverOperation.Cache | Cache | NIDMM_ATTR_CACHE |
|  | DmmWaveformAcquisition Class |  |
|  | ReadWaveform | niDMM_ReadWaveform |
|  | MemoryOptimizedReadWaveform | niDMM_ReadWaveform |
|  | ReadWaveformAsync | niDMM_ReadWaveform |
|  | MemoryOptimizedReadWaveformAsync | niDMM_ReadWaveform |
|  | FetchWaveform | niDMM_FetchWaveform |
|  | MemoryOptimizedFetchWaveform | niDMM_FetchWaveform |
|  | FetchWaveformAsync | niDMM_FetchWaveform |
|  | MemoryOptimizedFetchWaveformAsync | niDMM_FetchWaveform |
|  | Rate | NIDMM_ATTR_WAVEFORM_RATE |
|  | NumberOfPoints | NIDMM_ATTR_WAVEFORM_POINTS |
|  | Coupling | NIDMM_ATTR_WAVEFORM_COUPLING |
|  | DmmMultiPoint Class |  |
| Ivi.Dmm.IIviDmmMultiPoint.Configure | Configure | niDMM_ConfigureMultiPoint |
| Ivi.Dmm.IIviDmmMultiPoint.TriggerCount | TriggerCount | NIDMM_ATTR_TRIGGER_COUNT |
|  | SampleTriggerSlope | NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE |
| Ivi.Dmm.IIviDmmMultiPoint.SampleTrigger | SampleTrigger | NIDMM_ATTR_SAMPLE_TRIGGER |
| Ivi.Dmm.IIviDmmMultiPoint.SampleInterval | SampleInterval | NIDMM_ATTR_SAMPLE_INTERVAL |
|  | SampleDelayMode | NIDMM_ATTR_SAMPLE_DELAY_MODE |
| Ivi.Dmm.IIviDmmMultiPoint.SampleCount | SampleCount | NIDMM_ATTR_SAMPLE_COUNT |
|  | Latency | NIDMM_ATTR_LATENCY |
|  | BufferSize | NIDMM_ATTR_BUFFER_SIZE |
|  | DmmAdvancedCapacitanceAndInductance Class |  |
|  | NumberOfLCMeasurementsToAverage | NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE |
|  | DCBias | NIDMM_ATTR_DC_BIAS |
|  | LCCalculationModel | NIDMM_ATTR_LC_CALCULATION_MODEL |
|  | DmmFrequency Class |  |
| Ivi.Dmm.IIviDmmFrequency.VoltageAutoRange | VoltageAutoRange | NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE |
| Ivi.Dmm.IIviDmmFrequency.VoltageRange | VoltageRange | NIDMM_ATTR_FREQ_VOLTAGE_RANGE |
|  | DmmTemperature Class |  |
|  | ConfigureThermistorCustom | niDMM_ConfigureThermistorCustom |
|  | ThermistorType | niDMM_ConfigureThermistorType |
| Ivi.Dmm.IIviDmmTemperature.TransducerType | TransducerType | niDMM_ConfigureTransducerType |
|  | ThermistorA | NIDMM_ATTR_TEMP_THERMISTOR_A |
|  | ThermistorB | NIDMM_ATTR_TEMP_THERMISTOR_B |
|  | ThermistorC | NIDMM_ATTR_TEMP_THERMISTOR_C |
|  | DmmThermocouple Class |  |
| Ivi.Dmm.IIviDmmThermocouple.ReferenceJunctionType | ReferenceJunctionType | NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE |
| Ivi.Dmm.IIviDmmThermocouple.FixedReferenceJunction | FixedReferenceJunction | NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC |
| Ivi.Dmm.IIviDmmThermocouple.Type | Type | NIDMM_ATTR_TEMP_TC_TYPE |
| Ivi.Dmm.IIviDmmThermocouple.Configure | Configure | niDMM_ConfigureThermocouple |
|  | DmmRtd Class |  |
|  | A | NIDMM_ATTR_TEMP_RTD_A |
|  | B | NIDMM_ATTR_TEMP_RTD_B |
|  | C | NIDMM_ATTR_TEMP_RTD_C |
| Ivi.Dmm.IIviDmmRtd.Resistance | Resistance | NIDMM_ATTR_TEMP_RTD_RES |
| Ivi.Dmm.IIviDmmRtd.Type | Type | NIDMM_ATTR_TEMP_RTD_TYPE |
|  | ConfigureCustom | niDMM_ConfigureRTDCustom |

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=mapping-enums-dmm-dotnet.html language=enus -->
## TOPIC 00004: Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `mapping-enums-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/mapping-enums-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-DMM .NET API enums and enum values to the corresponding NI-DMM C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIDmm namespace. .NET API Enums and Enum Values C API Attributes and Values DmmMeasurementFunction NIDMM_ATTR

Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values

The following table maps the NI-DMM .NET API enums and enum values to the corresponding NI-DMM C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIDmm namespace.

| .NET API Enums and Enum Values | C API Attributes and Values |
| --- | --- |
| DmmMeasurementFunction | NIDMM_ATTR_FUNCTION |
| DCVolts | NIDMM_VAL_DC_VOLTS |
| ACVolts | NIDMM_VAL_AC_VOLTS |
| DCCurrent | NIDMM_VAL_DC_CURRENT |
| ACCurrent | NIDMM_VAL_AC_CURRENT |
| TwoWireResistance | NIDMM_VAL_2_WIRE_RES |
| FourWireResistance | NIDMM_VAL_4_WIRE_RES |
| Frequency | NIDMM_VAL_FREQ |
| Period | NIDMM_VAL_PERIOD |
| ACVoltsDCCoupled | NIDMM_VAL_AC_VOLTS_DC_COUPLED |
| Diode | NIDMM_VAL_DIODE |
| Capacitance | NIDMM_VAL_CAPACITANCE |
| Inductance | NIDMM_VAL_INDUCTANCE |
| WaveformVoltage | NIDMM_VAL_WAVEFORM_VOLTAGE |
| WaveformCurrent | NIDMM_VAL_WAVEFORM_CURRENT |
| DmmAdcCalibration | NIDMM_ATTR_ADC_CALIBRATION |
| Auto | NIDMM_VAL_ADC_CALIBRATION_AUTO |
| Off | NIDMM_VAL_ADC_CALIBRATION_OFF |
| On | NIDMM_VAL_ADC_CALIBRATION_ON |
| DmmAuto | NIDMM_ATTR_AUTO_ZERO |
| Auto | NIDMM_VAL_AUTO_ZERO_AUTO |
| Off | NIDMM_VAL_AUTO_ZERO_OFF |
| On | NIDMM_VAL_AUTO_ZERO_ON |
| Once | NIDMM_VAL_AUTO_ZERO_ONCE |
| DmmDCNoiseRejection | NIDMM_ATTR_DC_NOISE_REJECTION |
| Auto | NIDMM_VAL_DCNR_AUTO |
| Normal | NIDMM_VAL_DCNR_NORMAL |
| SecondOrder | NIDMM_VAL_DCNR_SECOND_ORDER |
| HighOrder | NIDMM_VAL_DCNR_HIGH_ORDER |
| DmmOffsetCompensatedOhm | NIDMM_ATTR_OFFSET_COMP_OHMS |
| Off | NIDMM_VAL_OFFSET_COMP_OHMS_OFF |
| On | NIDMM_VAL_OFFSET_COMP_OHMS_ON |
| DmmCableCompensationType | NIDMM_ATTR_CABLE_COMP_TYPE |
| None | NIDMM_VAL_CABLE_COMP_NONE |
| Open | NIDMM_VAL_CABLE_COMP_OPEN |
| Short | NIDMM_VAL_CABLE_COMP_SHORT |
| OpenAndShort | NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT |
| DmmLCCalculationModel | NIDMM_ATTR_LC_CALCULATION_MODEL |
| Auto | NIDMM_VAL_CALC_MODEL_AUTO |
| Series | NIDMM_VAL_CALC_MODEL_SERIES |
| Parallel | NIDMM_VAL_CALC_MODEL_PARALLEL |
| DmmDcBias | NIDMM_ATTR_DC_BIAS |
| Off | NIDMM_VAL_DC_BIAS_OFF |
| On | NIDMM_VAL_DC_BIAS_ON |
| DmmSlope | NIDMM_ATTR_MEAS_DEST_SLOPE |
| Positive | NIDMM_VAL_POSITIVE |
| Negative | NIDMM_VAL_NEGATIVE |
| DmmApertureTimeUnits | NIDMM_ATTR_APERTURE_TIME_UNITS |
| Seconds | NIDMM_VAL_SECONDS |
| PowerLineCycles | NIDMM_VAL_POWER_LINE_CYCLES |
| DmmOperationMode | NIDMM_ATTR_OPERATION_MODE |
| IvidmmMode | NIDMM_VAL_IVIDMM_MODE |
| WaveformMode | NIDMM_VAL_WAVEFORM_MODE |
| DmmWaveformCoupling | NIDMM_ATTR_WAVEFORM_COUPLING |
| AC | NIDMM_VAL_WAVEFORM_COUPLING_AC |
| DC | NIDMM_VAL_WAVEFORM_COUPLING_DC |
| DmmTransducerType | niDMM_ConfigureTransducerType |
| TwoWireRtd | NIDMM_VAL_2_WIRE_RTD |
| FourWireRtd | NIDMM_VAL_4_WIRE_RTD |
| Thermistor | NIDMM_VAL_THERMISTOR |
| Thermocouple | NIDMM_VAL_THERMOCOUPLE |
| DmmThermocoupleType | NIDMM_ATTR_TEMP_TC_TYPE |
| B | NIDMM_VAL_TEMP_TC_B |
| E | NIDMM_VAL_TEMP_TC_E |
| J | NIDMM_VAL_TEMP_TC_J |
| K | NIDMM_VAL_TEMP_TC_K |
| N | NIDMM_VAL_TEMP_TC_N |
| R | NIDMM_VAL_TEMP_TC_R |
| S | NIDMM_VAL_TEMP_TC_S |
| T | NIDMM_VAL_TEMP_TC_T |
| DmmThermistorType | NIDMM_ATTR_TEMP_THERMISTOR_TYPE |
| Custom | NIDMM_VAL_TEMP_THERMISTOR_CUSTOM |
| Thermistor44004 | NIDMM_VAL_TEMP_THERMISTOR_44004 |
| Thermistor44006 | NIDMM_VAL_TEMP_THERMISTOR_44006 |
| Thermistor44007 | NIDMM_VAL_TEMP_THERMISTOR_44007 |
| DmmRtdType | NIDMM_ATTR_TEMP_RTD_TYPE |
| Custom | NIDMM_VAL_TEMP_RTD_CUSTOM |
| PT3851 | NIDMM_VAL_TEMP_RTD_PT3851 |
| PT3750 | NIDMM_VAL_TEMP_RTD_PT3750 |
| PT3916 | NIDMM_VAL_TEMP_RTD_PT3916 |
| PT3920 | NIDMM_VAL_TEMP_RTD_PT3920 |
| PT3911 | NIDMM_VAL_TEMP_RTD_PT3911 |
| PT3928 | NIDMM_VAL_TEMP_RTD_PT3928 |
| DmmReferenceJunctionType | NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE |
| Fixed | NIDMM_VAL_TEMP_REF_JUNC_FIXED |
| DmmDelayMode | NIDMM_ATTR_SAMPLE_DELAY_MODE |
| IntervalSampleTrigger | NIDMM_ATTR_SAMPLE_INTERVAL |
| AnySampleTrigger | NIDMM_ATTR_SAMPLE_ANY |
| DmmControlAction | niDMM_Control |
| Commit | NIDMM_VAL_CONTROL_COMMIT |
| DmmCalibrationType | niDMM_GetCalCount |
| SelfCalibration | NIDMM_VAL_INTERNAL_AREA |
| External | NIDMM_VAL_EXTERNAL_AREA |
| DmmMeasurementCompleteDestination | NIDMM_ATTR_MEAS_COMPLETE_DEST |
| None | NIDMM_VAL_NONE |
| External | NIDMM_VAL_EXTERNAL |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| LbrTrig0 | NIDMM_VAL_LBR_TRIG_0 |
| DmmSampleTrigger | NIDMM_ATTR_SAMPLE_TRIGGER |
| Immediate | NIDMM_VAL_IMMEDIATE |
| External | NIDMM_VAL_EXTERNAL |
| SoftwareTrigger | NIDMM_VAL_SOFTWARE_TRIG |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| PxiStar | NIDMM_VAL_PXI_STAR |
| LbrTrig1 | NIDMM_VAL_LBR_TRIG_1 |
| AuxTrig1 | NIDMM_VAL_AUX_TRIG_1 |
| Interval | NIDMM_VAL_INTERVAL |
| DmmTriggerSource | NIDMM_ATTR_TRIGGER_SOURCE |
| Immediate | NIDMM_VAL_IMMEDIATE |
| External | NIDMM_VAL_EXTERNAL |
| SoftwareTrigger | NIDMM_VAL_SOFTWARE_TRIG |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| PxiStar | NIDMM_VAL_PXI_STAR |
| LbrTrig1 | NIDMM_VAL_LBR_TRIG_1 |
| AuxTrig1 | NIDMM_VAL_AUX_TRIG_1 |

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=overview-dmm-dotnet.html language=enus -->
## TOPIC 00005: NI-DMM .NET Class Library Help

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `overview-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/overview-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: October 2017, 375591C-01 You can use the NI-DMM .NET Class Library to initialize, configure, and read from your NI-DMM instrument. For additional information on developing applications using NI drivers and the .NET Framework, refer to ni.com/mstudio or visit ni.com/info and enter the Info Code NIdot

NI-DMM .NET Class Library Help

You can use the NI-DMM .NET Class Library to initialize, configure, and read from your NI-DMM instrument.

For additional information on developing applications using NI drivers and the .NET Framework, refer to 
 [ni.com/mstudio](http://www.ni.com/mstudio/) or visit 
 [ni.com/info](http://www.ni.com/info/) and enter the Info Code 
 NIdotNET.

You can find example applications by selecting 
 National Instruments»NI-DMM»NI-DMM Examples in the Start menu.

Note

© 2016-2017 National Instruments. All rights reserved.

Related concepts:

- Using Memory-Optimized and Async Methods to Fetch and Read
- NI-DMM .NET Programming Flow

Related tasks:

- Using the NI-DMM .NET Class Library in IVI.NET Applications

Related reference:

- Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values
- Mapping the NI-DMM .NET API to the NI-DMM C API

<!--NI_TOPIC bundle=ni-dmm-net-api-overview path=program-flow-dmm-dotnet.html language=enus -->
## TOPIC 00006: NI-DMM .NET Programming Flow

- bundle_id: `ni-dmm-net-api-overview`
- source_path: `program-flow-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-net-api-overview/raw/resource/enus/program-flow-dmm-dotnet.html
- document_id: `ni-dmm-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NIDmm .NET class library to initialize, configure, and read from your NI-DMM device. NI-DMM .NET, an Interchangeable Virtual Instrument (IVI)-compliant instrument driver, features a set of methods and properties that exercise the functionality of the NI-DMM hardware. For more informa

NI-DMM .NET Programming Flow

You can use the NIDmm .NET class library to initialize, configure, and read from your NI-DMM device. NI-DMM .NET, an Interchangeable Virtual Instrument (IVI)-compliant instrument driver, features a set of methods and properties that exercise the functionality of the NI-DMM hardware.

Tip

Programming with NI-DMM

NI Digital Multimeters Help

[IMAGE alt='NI-DMM Programming Workflow Diagram' src='GUID-93266187-2881-4B64-8BD2-136881EB93AE-a5.png']

#### Initializing a New NIDmm Session Object

For any application you write, you need to create a new NIDmm session object to establish communication with your NI-DMM device. In addition to establishing a session with the NI-DMM device in .NET, creating a new session object also sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver.

#### Configuring the Hardware

You can configure NI-DMM .NET to acquire single point measurements, multipoint measurements, and waveform acquisitions. If you are configuring NI-DMM .NET directly by setting properties, you need to also set OperationMode. If you are configuring NI-DMM .NET using a configuration method, then you can determine the configuration method depending on the type of acquisition you use in your application. For example, DmmTrigger contains methods and properties for configuring triggers, and DmmAdvanced contains methods and properties for advanced configurations such as PowerlineFrequency and OperationMode. Set this property to WaveformMode for waveform acquisition and to IviDmmMode to work in IVI applications.

#### Acquiring Data

After you have configured your NI-DMM device, you can acquire data by calling Read or Initiate and Fetch. For multipoint acquisitions, you can use ReadMultiPoint or Initiate and FetchMultiPoint, and for waveform acquisitions you can use ReadWaveform orInitiate and FetchWaveform.

#### Closing the Session

When your acquisition is complete, close the instrument I/O session with Close or Dispose. Close destroys the session and all of its attributes and deallocates any memory resources used by the NIDmm. Dispose calls Close, then disposes the .NET object.

Note

NIDmm

IntPtr

Close

Dispose

#### Configuring the NIDmm for Reading

The code snippet below creates and configures an NIDmm object to read DC voltage with a specific range and resolution and then closes the session.

```text
        VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution)
Dim reading As Double = sampleDmmSession.Measurement.Read()
sampleDmmSession.Close()
```

```text
        C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution);
double reading = sampleDmmSession.Measurement.Read();
sampleDmmSession.Close();
```

#### Configuring NI-DMM .NET for Multipoint Operations

The code snippet below demonstrates how to:

1. Create and configure an NIDmm object to read DC voltage with a specific range and resolution;
2. Acquire a multipoint measurement of 10 samples;
3. Use ReadStatus to determine the number of samples acquired;
4. Call FetchMultiPoint when a sufficient number of samples is acquired; and
5. Call Close to end the session and deallocate any memory resources used by this NIDmm .

```text
        VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5 
Dim numberOfSamples As Integer = 10 
Dim acquisitionBacklog As Integer = 0
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution)
sampleDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples
sampleDmmSession.Trigger.Source = DmmTriggerSource.Immediate
sampleDmmSession.Measurement.Initiate()
While acquisitionBacklog < numberOfSamples 
    sampleDmmSession.Measurement.ReadStatus(acquisitionBacklog)
End While 
Dim readingArray As Double() = sampleDmmSession.Measurement.FetchMultiPoint(PrecisionTimeSpan.FromMilliseconds(2000), acquisitionBacklog)
sampleDmmSession.Close()
```

```text
        C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
int numberOfSamples = 10;
int acquisitionBacklog=0;
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution);
sampleDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples;
sampleDmmSession.Trigger.Source = DmmTriggerSource.Immediate;
sampleDmmSession.Measurement.Initiate();
while (acquisitionBacklog < numberOfSamples) 
    sampleDmmSession.Measurement.ReadStatus(out acquisitionBacklog);
double[] readingArray = sampleDmmSession.Measurement.FetchMultiPoint(PrecisionTimeSpan.FromMilliseconds(2000), acquisitionBacklog);
sampleDmmSession.Close();
```

Parent topic:

NI-DMM .NET Class Library Help
