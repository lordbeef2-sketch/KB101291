# NI DOCUMENT BUNDLE: ni_rfsa-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni_rfsa-csharp-api-ref start=501 end=504 -->
<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-reserved2.html language=enus -->
## TOPIC 00501: Reserved2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-reserved2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-reserved2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reserved 2 for waveform information. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double Reserved2 { get; }RemarksReturns a Double representing reserved 2 for waveform information.

### Reserved2

Gets the reserved 2 for waveform information.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double Reserved2 { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing reserved 2 for waveform information.

Parent topic:

RfsaWaveformInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-xincrement.html language=enus -->
## TOPIC 00502: XIncrement

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-xincrement.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo-xincrement.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double XIncrement { get; }RemarksReturns a Double representing the time interval between data points in th

### XIncrement

Gets the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double XIncrement { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the time interval between data points in the acquired signal.

Parent topic:

RfsaWaveformInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo.html language=enus -->
## TOPIC 00503: RfsaWaveformInfo Data Structure

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsawaveforminfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods and properties associated with waveform information. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic struct RfsaWaveformInfoRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionAbsoluteInitialXGets th

### RfsaWaveformInfo Data Structure

Provides methods and properties associated with waveform information.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public struct RfsaWaveformInfo

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| AbsoluteInitialX | Gets the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. |
| ActualSamples | Gets the number of samples in the waveform. |
| Gain | Gets the gain to scale data. |
| Offset | Gets the offset to scale data. |
| RelativeInitialX | Gets a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference trigger location. |
| Reserved1 | Gets the reserved 1 for waveform information. |
| Reserved2 | Gets the reserved 2 for waveform information. |
| XIncrement | Gets the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(RfsaWaveformInfo) | Determines whether the current instance of RfsaWaveformInfo and the RfsaWaveformInfo object that you specify are equal. |
| Equals(object) | Determines if the current instance of RfsaWaveformInfo and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaWaveformInfo. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(RfsaWaveformInfo, RfsaWaveformInfo) | Checks whether the two instances of RfsaWaveformInfo are unequal. |
| operator==(RfsaWaveformInfo, RfsaWaveformInfo) | Checks whether the two instances of RfsaWaveformInfo are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa.html language=enus -->
## TOPIC 00504: NationalInstruments.ModularInstruments.NIRfsa

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionNIRfsaDefines a root class that is used to identify and control the instrument session. RfsaAcquisitionProvides the objects of specific acquisition classes. RfsaAdvanceTriggerRepresents the properties used to configure the Advance trigger for NI-RFSA. RfsaAdvanceTriggerSynchron

### NationalInstruments.ModularInstruments.NIRfsa

#### Classes

| Name | Description |
| --- | --- |
| NIRfsa | Defines a root class that is used to identify and control the instrument session. |
| RfsaAcquisition | Provides the objects of specific acquisition classes. |
| RfsaAdvanceTrigger | Represents the properties used to configure the Advance trigger for NI-RFSA. |
| RfsaAdvanceTriggerSynchronization | Represents the properties used to synchronize the Advance Trigger. |
| RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies which external trigger line distributes the RfsaAdvanceTriggerSynchronization signal. When synchronizing the RfsaAdvanceTrigger, configure all devices to use the same Advance Trigger distribution line. |
| RfsaAdvancedAcquisition | Represents the properties to access the advanced features related to acquisition. |
| RfsaAdvancedConfigurationList | Represents the advanced methods and properties used to work with configuration list and its related steps. |
| RfsaAdvancedIQAcquisitionConfiguration | Represents the advanced properties used to configure the RF vector analyzer for an IQ acquisition. |
| RfsaAdvancedReferenceTrigger | Provides properties to configure the Advanced Reference trigger. |
| RfsaAdvancedSignalPath | Provides advanced properties related to signal path. |
| RfsaAdvancedTrigger | Represents the advanced properties related to triggers. |
| RfsaAdvancedVertical | Represents the advanced properties related to vertical. |
| RfsaArmReferenceTrigger | Represents the methods and properties used to configure the Arm Reference trigger for NI-RFSA. |
| RfsaBasicConfigurationList | Represents the methods and properties to work with configuration list and its related steps. |
| RfsaCalibration | Provides objects of specific types to calibrate NI-RFSA. |
| RfsaChannelBasedDeembedding | Represents the channel-based properties and methods used to configure Deembedding. |
| RfsaChannelBasedDeviceCharacteristics | Represents the channel-based methods and properties related to device information. |
| RfsaChannelBasedLO | Represents the properties used to configure channel based LO. |
| RfsaConfiguration | Provides objects of specific types used to configure the NI-RFSA. |
| RfsaConfigurationListStepTrigger | Represents the properties used to configure the Configuration List Step trigger. |
| RfsaDeembedding | Represents the properties and methods used to configure Deembedding. |
| RfsaDeviceCharacteristics | Represents the methods and properties related to device information. |
| RfsaDeviceSpecific | Represents RFSA Device Specific properties. |
| RfsaDigitalEdgeAdvanceTrigger | Represents the properties used to configure the digital edge for Advance trigger. |
| RfsaDigitalEdgeAdvanceTriggerSource | Represents the source terminal for RfsaDigitalEdgeAdvanceTrigger. |
| RfsaDigitalEdgeArmReferenceTrigger | Represents the properties used to configure digital edge for RfsaArmReferenceTrigger. |
| RfsaDigitalEdgeArmReferenceTriggerSource | Represents the source terminal for RfsaDigitalEdgeArmReferenceTrigger. |
| RfsaDigitalEdgeConfigurationListStepTrigger | Represents the methods and properties used to configure digital edge for the Configuration List Step trigger. |
| RfsaDigitalEdgeConfigurationListStepTriggerSource | Represents the source terminal for RfsaDigitalEdgeConfigurationListStepTrigger. |
| RfsaDigitalEdgeReferenceTrigger | Represents the methods and properties used to configure digital edge for the Reference trigger. |
| RfsaDigitalEdgeReferenceTriggerSource | Represents the source terminal for RfsaDigitalEdgeReferenceTrigger. |
| RfsaDigitalEdgeStartTrigger | Represents the properties used to configure RfsaDigitalEdgeStartTrigger. |
| RfsaDigitalEdgeStartTriggerSource | Represents the source terminal for RfsaDigitalEdgeStartTrigger. |
| RfsaDigitizerSampleClock | Represents the properties used to configure Digitizer Sample Clock. |
| RfsaDigitizerSampleClockSynchronizationDistributionLine | Specifies which external trigger line distributes the RfsaDigitizerSampleClockSynchronizationDistributionLine signal. When synchronizing the RfsaDigitizerSampleClock, configure all devices to use the same Digitizer Sample Clock distribution line. |
| RfsaDigitizerSampleClockTimebaseSource | Represents the source of the Sample clock timebase, which is the timebase used to control waveform sampling. |
| RfsaDoneEvent | Represents the properties used to configure Done event. |
| RfsaDoneEventExportedOutputTerminal | Represents the destination terminal for RfsaDoneEvent. |
| RfsaDriverIdentity | Provides the methods and properties that provide information about the instrument and the NI-RFSA driver. |
| RfsaDriverLock | Provides synchronization locks obtained on the driver session. |
| RfsaDriverOperation | Provides properties that affect the operation of the instrument driver. |
| RfsaDriverUtility | Represents the methods that provide a basic set of utility operations. |
| RfsaEndOfRecordEvent | Represents the properties used to configure the underlying hardware End of Record event. |
| RfsaEndOfRecordEventExportedOutputTerminal | Represents the destination terminal for RfsaEndOfRecordEvent. |
| RfsaEvents | Provides underlying hardware events of specific types. |
| RfsaExportAdvanceTrigger | Represents the properties used to export Advance triggers. |
| RfsaExportAdvanceTriggerExportedOutputTerminal | Represents the destination terminal for RfsaExportAdvanceTrigger. |
| RfsaExportDigitizerSampleClock | Represents properties used to export Reference clock. |
| RfsaExportDigitizerSampleClockExportedOutputTerminal | Represents the destination terminal for RfsaDigitizerSampleClock. |
| RfsaExportReferenceClock | Represents properties used to export Reference clock. |
| RfsaExportReferenceClockExportedOutputTerminal | Represents a destination terminal to which a Reference clock is exported. |
| RfsaExportReferenceTrigger | Represents the properties used to export Reference trigger. |
| RfsaExportReferenceTriggerExportedOutputTerminal | Represents the destination terminal for RfsaExportReferenceTrigger. |
| RfsaExportStartTrigger | Represents the properties used to export Start trigger. |
| RfsaExportStartTriggerExportedOutputTerminal | Represents the destination terminal for RfsaExportStartTrigger. |
| RfsaExternalCalibration | Provides the properties used to perform external calibration. |
| RfsaIQAcquisition | Represents the properties and methods used to configure and acquire I/Q signals. |
| RfsaIQAcquisitionConfiguration | Represents the properties used to configure the RF vector analyzer for an IQ acquisition. |
| RfsaIQAnalogEdge | Represents the properties to configure the I/Q analog edge specific to 5644R and 5645R. |
| RfsaIQAnalogEdgeSource | Specifies the the channel from which the device monitors the trigger. |
| RfsaIQInPortChannel | Represents the channel-based properties to configure I/Q In port terminals specific to 5644R and 5645R. |
| RfsaIQInPortChannelCollection | Represents the properties to configure the I/Q port specific for the 5644R and 5645R devices. |
| RfsaIQPowerEdge | Represents the properties and method used to configure the I/Q power edge. |
| RfsaIQPowerEdgeReferenceTriggerSource | Represents the source terminal for RfsaIQPowerEdge. |
| RfsaLOSource | Represents the source for LOSource. |
| RfsaLocalOscillator | Represents the properties used to configure LO. |
| RfsaNI5663AdvancedVertical | Defines the advanced vertical methods and properties that are applicable to NI 5663 specifically. |
| RfsaNI5663SignalPath | Defines the properties related to NI 5663-specific signal path features. |
| RfsaNI5665AdvancedVertical | Defines the advance vertical methods and properties applicable to NI 5665 specifically. |
| RfsaNI5665SignalPath | Defines the properties related to NI 5665-specific signal path features. |
| RfsaNI5693AdvancedVertical | Defines the advanced vertical methods and properties that are applicable to NI 5693 specifically. |
| RfsaNI5693SelfCalibration | Defines properties used to self calibrate the NI5693. |
| RfsaNI5694AdvancedVertical | Defines the advanced vertical methods and properties that are applicable to NI 5694 specifically. |
| RfsaNI5694SignalPath | Defines the properties related to NI 5694-specific signal path features. |
| RfsaOutputTerminal | Specifies the terminal where the signal is exported. You can also choose not to export any signal. |
| RfsaPxiChassisClk10Source | Represents the properties used to configure the signal to drive the 10 MHz Reference clock on the PXI backplane. |
| RfsaReadyForAdvanceEvent | Represents the properties related to Ready for Advance event of the hardware. |
| RfsaReadyForAdvanceEventExportedOutputTerminal | Represents the destination terminal for RfsaReadyForAdvanceEvent. |
| RfsaReadyForReferenceEvent | Represents the properties related to Ready for Reference event of the hardware. |
| RfsaReadyForReferenceEventExportedOutputTerminal | Represents the destination terminal for RfsaReadyForReferenceEvent. |
| RfsaReadyForStartEvent | Represents the properties related to Ready for Start event of the hardware. |
| RfsaReadyForStartEventExportedOutputTerminal | Represents the destination terminal of the RfsaReadyForStartEvent. |
| RfsaReferenceClock | Represents the methods and properties used to configure the Reference clock. |
| RfsaReferenceClockSource | Represents the source of RfsaReferenceClock. |
| RfsaReferenceTrigger | Represents the properties used to configure the Reference trigger for NI-RFSA. |
| RfsaReferenceTriggerSynchronization | Represents the properties to synchronize the Reference Trigger. |
| RfsaReferenceTriggerSynchronizationDistributionLine | Specifies the external trigger line that distributes the RfsaReferenceTriggerSynchronization signal. When synchronizing the RfsaReferenceTrigger, configure all devices to use the same Reference Trigger distribution line. |
| RfsaSelfCalibration | Defines methods and properties used to perform self calibration and query data related to self calibration. |
| RfsaSignalIdentifier | Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions. |
| RfsaSignalPath | Represents the signal path properties. |
| RfsaSpectrumAcquisition | Represents the methods used to configure and acquire data in the spectrum mode. |
| RfsaSpectrumAcquisitionConfiguration | Represents the properties used to configure the hardware when acquiring in I/Q mode. |
| RfsaStartTrigger | Represents the properties used to configure the Start trigger for NI-RFSA. |
| RfsaStartTriggerSynchronization | Represents various Synchronization Triggers specific to the 5644R and 5645R devices. |
| RfsaStartTriggerSynchronizationDistributionLine | Specifies the external trigger line that distributes the RfsaStartTriggerSynchronization signal. When synchronizing the RfsaStartTrigger, configure all devices to use the same Start Trigger distribution line. |
| RfsaSubObject | Represents members that are common to all sub-object NI-Rfsa classes. |
| RfsaTimerStartSource | Represents the source for TimerStartSource. |
| RfsaTriggers | Provides triggers of specific types. |
| RfsaUserSource | Represents the channel-based properties used to configure User Source. |
| RfsaUserSourceCollection | Represents a collection of User Sources. |
| RfsaVertical | Represents the properties related to vertical. |
| RfsaWarning | Provides warning codes for the warnings raised by the underlying driver. |
| RfsaWarningEventArgs | Represents the properties under the Warning Event Args raised incase of a driver warning. |

#### Interfaces

None

#### Structures

| Name | Description |
| --- | --- |
| RfsaCoefficientInfo | Represents the coefficient info struct of the underlying driver. |
| RfsaErrorQueryResult | Represents the the result of an error query. |
| RfsaRevisionQueryResult | Represents the result of the revision query operation. |
| RfsaSelfTestResult | Represents the result of the NationalInstruments.ModularInstruments.NIRfsa.RfsaDriverUtility.SelfTest method. |
| RfsaSpectrumInfo | Provides methods and properties associated with power spectrum information. |
| RfsaWaveformInfo | Provides methods and properties associated with waveform information. |

#### Enumerations

| Name | Description |
| --- | --- |
| MechanicalAttenuatorEnabled | Specifies whether the mechanical attenuator is enabled or disabled. |
| RfsaAcquisitionStatus | Defines constants for the different of acquisition status supported by NI-RFSA. |
| RfsaAcquisitionType | Specifies whether the session acquires I/Q data or computes a power spectrum over the specified frequency range. |
| RfsaAdvanceTriggerType | Specifies whether you want the Advance trigger to be a digital edge or software trigger. |
| RfsaAllowOutOfSpecificationUserSettingsEnabled | Specifies where to enable or disable warnings and errors when you set frequency and power values beyond the limits of the NI-RFSA device specifications. |
| RfsaArmReferenceTriggerType | Specifies whether you want the Arm Reference trigger to be digital edge or software trigger. |
| RfsaChannelCoupling | Specifies whether the RF input channel is AC-coupled or DC-coupled on a downconverter. |
| RfsaConfigurationListProperties | Specifies the configuration list properties that the user can change between configuration list steps. |
| RfsaContiguousMultiRecordEnabled | Specifies whether to enable contiguous multirecord acquisition. |
| RfsaDeembeddingType | Specifies the type of de-embedding to apply to measurements on the specified port. |
| RfsaDeviceResponseType | Specifies the requested response type, based on current NI-RFSA settings. |
| RfsaDigitizerDitherEnabled | Specifies whether dithering is enabled on the digitizer. |
| RfsaDownconverterFrequencyOffsetMode | Specifies whether NI-RFSA automatically selects the downconverter frequency offset. |
| RfsaDownconverterLoopBandwidth | Specifies the bandwidth that the downconverter module uses. |
| RfsaDownconverterPreselectorEnabled | Specifies options which indicate whether the tunable preselector is enabled on the downconverter. |
| RfsaFetchRelativeTo | Specifies the reference location within the acquired record from which to begin fetching. |
| RfsaFftWindowType | Specifies the time-domain window type. |
| RfsaFrequencySettlingUnits | Specifies the delay duration units and interpretation for LO settling. |
| RfsaIFConditioningDownconversionEnabled | Specifies whether to enable IF conditioning down conversion. |
| RfsaIFFilter | Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA. |
| RfsaIQAnalogEdgeReferenceTriggerSlope | Specifies whether the device asserts the trigger when the voltage level is rising or falling. |
| RfsaIQInPortTerminalConfiguration | Specifies the terminal configuration of the I/Q port. |
| RfsaIQPowerEdgeReferenceTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
| RfsaInputIsolationEnabled | Specifies whether input isolation is enabled. |
| RfsaInputPort | Specifies the connector(s) to use to acquire the signal. |
| RfsaLO2ExportEnabled | Specifies whether to enable the LO2 OUT terminal on the installed devices. |
| RfsaLOInjectionSide | Specifies the LO injection side. |
| RfsaLOOutExportConfigureFromRfsg | Specifies whether to allow NI-RFSG to control the NI-RFSA local oscillator export. |
| RfsaLOPllFractionalModeEnabled | Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). |
| RfsaLOYigMainCoilDrive | Adjusts the dynamics of the current driving the YIG main coil. |
| RfsaLinearInterpolationFormat | Specifies the format of parameters to interpolate. |
| RfsaLoadConfigurationsFromFileResetOptions | Specifies the configurations to skip while loading from a file. |
| RfsaLowFrequencyBypassEnabled | Specifies whether to use the low-frequency bypass path for the incoming RF signal. |
| RfsaNI5693RFConditioningCalibrationToneMode | Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled. |
| RfsaNI5693RFPreselectorCalibrationToneMode | Specifies the location in a signal path where an RF preselector calibration tone is injected or whether the tone is disabled. |
| RfsaNISelfCalibrationToneMode | Specifies the location in a path where a calibration tone is injected or whether the tone is disabled. |
| RfsaNoiseSourcePowerEnabled | Specifies whether to enable the noise source power. |
| RfsaNotchFilterEnabled | Specifies whether the notch filter is enabled on the RF conditioning module. |
| RfsaOspDelayEnabled | Specifies whether the digitizer onboard signal processing (OSP) block delays the Reference triggers and the data samples moving through the OSP block, or if the Reference triggers bypass the OSP block and are processed immediately. |
| RfsaOverflowErrorReporting | Configures error reporting for ADC and onboard signal processing overflows. |
| RfsaPowerSpectrumUnits | Specifies the units of the power spectrum. |
| RfsaPreselectorEnabled | Specifies the different options of enabling or disabling the preselector. |
| RfsaRFOutLOExportEnabled | Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840. |
| RfsaRFPreamplifierEnabled | Specifies whether to enable the RF preamplifier on the downconverter. |
| RfsaRFPreselectorFilter | Specifies the RF preselector filter to use. |
| RfsaReferenceTriggerSynchronizationDelayEnabled | Specifies whether Reference Trigger is delayed with the data. |
| RfsaReferenceTriggerType | Specifies whether you want the Reference trigger to be a digital edge, I/Q power edge, or software trigger. |
| RfsaResetStepsToOmit | Specifies a list of steps to skip during the reset process. |
| RfsaResolutionBandwidthType | Specifies how the ResolutionBandwidth property is expressed. |
| RfsaSParameterOrientation | Specifies the orientation of the data in the S2P file relative to the port on the DUT port. |
| RfsaSelfCalibrationDownconverterToneMode | Specifies the location in a path where a calibration tone is injected or whether the tone is disabled. |
| RfsaSelfCalibrationSteps | Specifies the various steps involved in self calibration of NI-RFSA. |
| RfsaSignalConditioningEnabled | Specifies whether signal conditioning is enabled on the NI 5694. |
| RfsaSignalType | Specifies the type of signal to route. |
| RfsaSmoothSpectrumEnabled | Specifies whether an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition. |
| RfsaSpectrumAveragingMode | Specifies the averaging mode for the spectrum acquisition. |
| RfsaStartTriggerType | Specifies constants for different types of Start trigger. |
| RfsaStepGainEnabled | Specifies whether to enable the step gain amplifier. |
| RfsaTriggerEdge | Specifies the transitions of the signal from one discrete level to another. |
| RfsaUserSourcePulseWidthUnits | Specifies the pulse width units for the User Source. |

#### Delegates

None
