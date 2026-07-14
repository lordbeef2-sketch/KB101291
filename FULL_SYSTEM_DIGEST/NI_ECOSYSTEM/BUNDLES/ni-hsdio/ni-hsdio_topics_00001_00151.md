# NI DOCUMENT BUNDLE: ni-hsdio

<!--NI_BUNDLE_CHUNK bundle=ni-hsdio start=1 end=151 -->
<!--NI_TOPIC bundle=ni-hsdio path=ac-and-dc-current.html language=enus -->
## TOPIC 00001: AC and DC Current

- bundle_id: `ni-hsdio`
- source_path: `ac-and-dc-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ac-and-dc-current.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC current is current sourced or sunk during the transition between low level and high level states. This current drives a capacitive load or an inductive load. A capacitive load is, for example, a cable. An inductive load, is, for example, a device interconnect. DC current is the current that is so

### AC and DC Current

AC current is current sourced or sunk during the transition between low
 level and high level states. This current drives a
 capacitive load or an inductive load. A capacitive load is, for example, a cable. An
 inductive load, is, for example, a device interconnect.

DC current is the current that is sourced or sunk when the generation terminals are at a
 static voltage. The current drives a resistive load. The following illustration of a
 digital waveform shows when AC or DC current is sourced or sunk.

[IMAGE alt='image' src='GUID-03D8136C-F3A1-4EC6-BC2B-8ADECF5C6B1C-a5.gif']

Use the following formulas to calculate AC current:

I

=

C

·

d

v

d

t

where I is current in amps,

C is load capacitance in farads,

dV/dt is the rate of change of the voltage level in volts/s

or

I

=

1

L

∫

v

t

d

t

where I is the current in amps,

L is the inductive loading in henrys,

V<sub>(t)</sub> is the voltage in volts as a function of time.

Use the following formula to calculate DC current:

I

=

V

R

where I is current in amps,

V is voltage level in volts,

R is resistance in ohms.

<!--NI_TOPIC bundle=ni-hsdio path=ac-waveform-characteristics.html language=enus -->
## TOPIC 00002: AC Waveform Characteristics

- bundle_id: `ni-hsdio`
- source_path: `ac-waveform-characteristics.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ac-waveform-characteristics.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following terms describe some of the common AC waveform characteristics. Rise time and fall time Rise time (t[rise]) is the time that it takes a signal to rise from 20% to 80% of the voltage between the voltage low level and the voltage high level. Fall time (t[fall])is the time that it takes a

### AC Waveform Characteristics

The following terms describe some of the common AC waveform characteristics.

Rise time and fall time

rise

voltage low

voltage high

fall

voltage low

voltage high

The following figure illustrates rise and fall time:

[IMAGE alt='image' src='GUID-F1DDDD18-CB9C-4AA8-B585-3F1AD37023F6-a5.gif']

Preshoot and overshoot

Note

[IMAGE alt='image' src='GUID-297DF38E-2B4C-4FA3-BBDE-C8D717618CBD-a5.gif']

Settling time

S

The following figure illustrates settling time on a digital signal:

[IMAGE alt='image' src='GUID-D4E097B8-0028-43B3-9061-6B79B3EFD137-a5.gif']

Duty cycle

logic high

The following figure shows the difference between two waveforms with
 different duty cycles. Notice that the 30% duty-cycle waveform is at
 logic high level for less time than the 50% duty cycle
 waveform.

[IMAGE alt='image' src='GUID-67E2C576-179C-4556-AADD-E88851451AFA-a5.gif']

<!--NI_TOPIC bundle=ni-hsdio path=acquiring-dynamic-data.html language=enus -->
## TOPIC 00003: Acquiring Dynamic Data

- bundle_id: `ni-hsdio`
- source_path: `acquiring-dynamic-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquiring-dynamic-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you have configured the acquisition, you can acquire data using the read VIs or functions or using the initiate and fetch VIs or functions. The following figure shows the flow of acquiring dynamic data:

### Acquiring Dynamic Data

After you have configured the acquisition, you can acquire data using the read VIs or functions
 or using the initiate and fetch VIs or
 functions.

The following figure shows the flow of acquiring dynamic
 data:

[IMAGE alt='image' src='GUID-1C23A137-8F78-4F7B-A46D-DEEE6F4FDBE0-a5.gif']

Parent topic:

Programming Flow

Related concepts:

- Read
- Initiate and Fetch

<!--NI_TOPIC bundle=ni-hsdio path=acquiring-or-generating-static-data.html language=enus -->
## TOPIC 00004: Acquiring or Generating Static Data

- bundle_id: `ni-hsdio`
- source_path: `acquiring-or-generating-static-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquiring-or-generating-static-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you configure the acquisition or generation, you can acquire or generate the static data using the static read/write VIs and functions. The following figure shows the flow of acquiring and generating static data:

### Acquiring or Generating Static Data

After you configure the acquisition or generation, you can acquire or generate the static data
 using the static read/write VIs and functions.

The following figure shows the flow of acquiring and generating
 static data:

[IMAGE alt='image' src='GUID-336EE8C3-79A3-455A-B456-1FBC86E7697B-a5.gif']

Parent topic:

Programming Flow

Related concepts:

- Reading and Writing Static Data

<!--NI_TOPIC bundle=ni-hsdio path=acquisition-configuration-functions.html language=enus -->
## TOPIC 00005: Acquisition Configuration Functions

- bundle_id: `ni-hsdio`
- source_path: `acquisition-configuration-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquisition-configuration-functions.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW VIs C Functions niHSDIO Configure Sample Clock niHSDIO_ConfigureSampleClock niHSDIO Configure Acquisition Size niHSDIO_ConfigureAcquisitionSize niHSDIO Configure Data Interpretation niHSDIO_ConfigureDataInterpretation niHSDIO Configure Voltage(Polymorphic VI) niHSDIO_ConfigureDataVoltageLogi

### Acquisition Configuration Functions

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Configure Sample Clock | niHSDIO_ConfigureSampleClock |
| niHSDIO Configure Acquisition Size | niHSDIO_ConfigureAcquisitionSize |
| niHSDIO Configure Data Interpretation | niHSDIO_ConfigureDataInterpretation |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureDataVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureDataVoltageCustomLevels |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureTriggerVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureTriggerVoltageCustomLevels |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureEventVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureEventVoltageCustomLevels |
| niHSDIO Configure Data Position | niHSDIO_ConfigureDataPosition |
| niHSDIO Configure Data Position Delay | niHSDIO_ConfigureDataPositionDelay |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalEdgeStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchStartTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureSoftwareStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisableStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalEdgeRefTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchRefTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchRefTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureSoftwareRefTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisableRefTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalEdgeAdvanceTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchAdvanceTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchAdvanceTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureSoftwareAdvanceTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisableAdvanceTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalLevelPauseTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchPauseTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchPauseTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisablePauseTrigger |
| niHSDIO Export Signal | niHSDIO_ExportSignal |
| niHSDIO Configure Ref Clock | niHSDIO_ConfigureRefClock |

Note

Using Attributes with NI-HSDIO

Advanced Attributes

Parent topic:

Configure the Hardware

Related concepts:

- Using Attributes with NI-HSDIO
- Advanced Attributes

<!--NI_TOPIC bundle=ni-hsdio path=acquisition-considerations-for-ddr.html language=enus -->
## TOPIC 00006: Acquisition Considerations for DDR

- bundle_id: `ni-hsdio`
- source_path: `acquisition-considerations-for-ddr.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquisition-considerations-for-ddr.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Edge Triggers In DDR acquisitions, while data channels are sampled on both clock edges, triggers are only stored once per Sample clock period. For example, refer to the following figure: Consider if PFI Trigger A was a digital edge start trigger, and the device were configured for rising edge data p

### Acquisition Considerations for DDR

#### Edge
 Triggers

In DDR acquisitions, while data channels are
 sampled on both clock edges, triggers are only stored once per
 Sample clock period. For example, refer to the following
 figure:

[IMAGE alt='image' src='GUID-C902E849-ED96-406C-BC93-D53CBF05D463-a5.gif']

Consider if PFI Trigger A was a digital edge start trigger, and the
 device were configured for rising edge data position. Whether PFI
 Trigger A arrives before the rising edge of the clock or before the
 falling clock edge, the trigger has the same effect, the first
 sample acquired is that of the rising clock edge.

#### Pattern Match Trigger

In DDR acquisitions, while data
 channels are sampled on both clock edges, triggers are only stored
 once per sample clock period. In the following figure, the device is
 configured for a pattern match start trigger and rising edge data
 position:

[IMAGE alt='image' src='GUID-F0EB2FD4-28AF-4E65-8955-E868E888DF4E-a5.gif']

Whether the data in sample A or B matches the pattern configured
 for the pattern match trigger, sample A is the first acquired
 sample.

#### Special Considerations for Using the Pause Trigger

If a
 pause trigger is asserted on either edge of the sample clock, the
 acquisition is paused for the samples that occur on both edges of
 the clock.

#### Data
 Width

Data width is a function of your data rate
 multiplier. Since data width refers to how large your sample is in
 bytes, using DDR mode effectively halves your allowable data width.
 For example, on a device with 16 channels, you can generate or
 acquire data on all 16 channels. For the same device with its data
 rate multiplier configured for DDR, you can generate on only eight
 channels and acquire on the other eight.

#### Memory Usage

Memory usage is effectively doubled for each
 channel since the data width and channel count are
 halved.

Parent topic:

Double Data Rate (DDR)

Related concepts:

- Data Width
- Configuring a Data Rate Multiplier
- Onboard Memory

<!--NI_TOPIC bundle=ni-hsdio path=acquisition-onboard-memory.html language=enus -->
## TOPIC 00007: Acquisition Onboard Memory

- bundle_id: `ni-hsdio`
- source_path: `acquisition-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquisition-onboard-memory.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When an acquisition operation is initiated, the device begins waiting for the Start trigger. Once the start trigger is received, the device starts acquiring data and storing the samples into device memory. The first sample acquired marks the beginning of the acquired record, as shown in the followin

### Acquisition Onboard Memory

When an acquisition operation is initiated, the device begins waiting for the Start trigger. Once
 the start trigger is received, the device starts acquiring data and storing the samples
 into device memory. The first sample acquired marks the beginning of the acquired
 record, as shown in the following figure:

[IMAGE alt='image' src='GUID-483F8878-680A-420F-B1F1-CCD2CC20A13A-a5.gif']

If no start trigger has been configured, acquisition begins immediately after the operation is
 initiated.

After the device recognizes the start trigger and acquires the configured number of pretrigger
 samples, the device can now recognize a reference trigger. While waiting for the
 reference trigger, the device is still sampling data into the device memory. If the
 record overflows, the newest samples overwrite the oldest samples in the record. After
 the reference trigger is received, the device acquires enough posttrigger samples and
 finishes the acquisition, as shown in the following figure:

[IMAGE alt='image' src='GUID-5492D243-818D-4292-8B3F-1DC4199C55F5-a5.gif']

If no reference trigger has been configured, a single record of data is acquired.

#### Fetching Acquired Data

Data acquired between the start trigger and the
 first pretrigger sample can also be fetched. The following figure shows the four
 common fetch positions:

[IMAGE alt='image' src='GUID-0FD26E0A-4F58-4E75-8678-20BD72148494-a5.gif']

In cases where no reference trigger is configured, the first pretrigger sample
 and reference trigger are equivalent to first sample.

#### Multirecord Acquisitions

In the case of multirecord acquisitions, the
 advance trigger initiates the acquisition or fetch operation for the second and all
 subsequent records. For multirecord acquisitions, the start trigger shown in the
 previous figures would be replaced by an advance trigger for all records after the
 initial acquisition.

Parent topic:

Onboard Memory

<!--NI_TOPIC bundle=ni-hsdio path=acquisition.html language=enus -->
## TOPIC 00008: Acquisition

- bundle_id: `ni-hsdio`
- source_path: `acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/acquisition.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains the concepts and terminology related to acquisition.

### Acquisition

This section explains the concepts and terminology related to acquisition.

Parent topic:

Digital Terminology

<!--NI_TOPIC bundle=ni-hsdio path=active-drive.html language=enus -->
## TOPIC 00009: Active Drive

- bundle_id: `ni-hsdio`
- source_path: `active-drive.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/active-drive.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When configured for active drive generation, a channel generates the Generation Voltage High level for logic 1, and the channel generates the Generation Voltage Low level for logic 0. You can configure all digital waveform generator/analyzers for active drive generation and some for open collector g

### Active Drive

When configured for active drive generation, a channel generates the **Generation
 Voltage High**level for logic 1, and
 the channel generates the **Generation Voltage
 Low** level for logic 0.

You can configure all digital waveform generator/analyzers for active drive generation and some
 for open collector generation.

Parent topic:

Drive Type

Related concepts:

- Open Collector

<!--NI_TOPIC bundle=ni-hsdio path=advanced-attributes.html language=enus -->
## TOPIC 00010: Advanced Attributes

- bundle_id: `ni-hsdio`
- source_path: `advanced-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/advanced-attributes.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: These advanced attributes, called properties in LabVIEW, are not available through a configuration VI or function. Set these attributes directly using the niHSDIO Property Node or the niHSDIO Set Attribute functions. Refer to Using Attributes with NI-HSDIO for more information about programming attr

### Advanced Attributes

These advanced attributes, called properties in LabVIEW, are not available through a
 configuration VI or function. Set these attributes directly using the niHSDIO
 Property Node or the niHSDIO Set Attribute functions. Refer to *Using
 Attributes with NI-HSDIO* for more information about programming
 attributes.

| LabVIEW Property | C Attribute |
| --- | --- |
| Sample Clock Impedance | NIHSDIO_ATTR_SAMPLE_CLOCK_IMPEDANCE |
| Ref Clock Impedance | NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE |
| Digital Edge Start Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_IMPEDANCE |
| Digital Edge Start Trigger Position | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_POSITION |
| Digital Edge Start Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Reference Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_IMPEDANCE |
| Digital Edge Reference Trigger Position | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_POSITION |
| Digital Edge Reference Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Advance Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_IMPEDANCE |
| Digital Edge Advance Trigger Position | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_POSITION |
| Digital Edge Advance Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION |
| Ready For Advance Event Terminal Configuration | NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_CONFIGURATION |
| Ready For Start Event Terminal Configuration | NIHSDIO_ATTR_READY_FOR_START_EVENT_TERMINAL_CONFIGURATION |
| Digital Level Pause Trigger Impedance | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_IMPEDANCE |
| Digital Level Pause Trigger Position | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_POSITION |
| Digital Level Pause Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_TERMINAL_CONFIGURATION |
| Exported Sample Clock Mode | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_MODE |
| Exported Sample Clock Delay | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_DELAY |
| Fetch Relative To | NIHSDIO_ATTR_FETCH_RELATIVE_TO |
| Fetch Offset | NIHSDIO_ATTR_FETCH_OFFSET |
| Fetch Backlog | NIHSDIO_ATTR_FETCH_BACKLOG |
| Samples Per Record Is Finite | NIHSDIO_ATTR_SAMPLES_PER_RECORD_IS_FINITE |
| Supported Data States | NIHSDIO_ATTR_SUPPORTED_DATA_STATES |

| LabVIEW Property | C Attribute |
| --- | --- |
| Sample Clock Impedance | NIHSDIO_ATTR_SAMPLE_CLOCK_IMPEDANCE |
| Ref Clock Impedance | NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE |
| Data Active Event Position | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_POSITION |
| Marker Event Pulse Polarity | NIHSDIO_ATTR_MARKER_EVENT_PULSE_POLARITY |
| Marker Event Position | NIHSDIO_ATTR_MARKER_EVENT_POSITION |
| Exported Sample Clock Mode | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_MODE |
| Exported Sample Clock Delay | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_DELAY |
| Exported Sample Clock Offset | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_OFFSET |
| Digital Edge Start Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_IMPEDANCE |
| Digital Edge Start Trigger Position | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_POSITION |
| Digital Edge Start Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Reference Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_IMPEDANCE |
| Digital Edge Reference Trigger Position | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_POSITION |
| Digital Edge Reference Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Script Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_IMPEDANCE |
| Digital Edge Script Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Level Script Trigger Impedance | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_IMPEDANCE |
| Digital Level Script Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Stop Trigger Source | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_SOURCE |
| Digital Edge Stop Trigger Edge | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_EDGE |
| Digital Edge Stop Trigger Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Stop Trigger Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_IMPEDANCE |
| Export Stop Trigger Output Terminal | NIHSDIO_ATTR_EXPORT_STOP_TRIGGER_OUTPUT_TERMINAL |
| Export Stop Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORT_STOP_TRIGGER_TERMINAL_CONFIGURATION |
| Supported Data States | NIHSDIO_ATTR_SUPPORTED_DATA_STATES |

| LabVIEWProperty | C Attribute |
| --- | --- |
| Advanced:Hardware Compare:Filter Repeated Sample Errors | NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS |
| Advanced:Hardware Compare:Samples Compared | NIHSDIO_ATTR_HWC_SAMPLES_COMPARED |
| Advanced:Hardware Compare:Number Of Sample Errors | NIHSDIO_ATTR_HWC_NUM_SAMPLE_ERRORS |
| Advanced:Hardware Compare:Sample Error Backlog | NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BACKLOG |
| Advanced:Hardware Compare:Samples Error Buffer Overflowed | NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BUFFER_OVERFLOWED |

Parent topic:

Configure the Hardware

Related concepts:

- Using Attributes with NI-HSDIO

<!--NI_TOPIC bundle=ni-hsdio path=channel-to-channel-skew.html language=enus -->
## TOPIC 00011: Channel-to-Channel Skew

- bundle_id: `ni-hsdio`
- source_path: `channel-to-channel-skew.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/channel-to-channel-skew.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For dynamic generation, channel-to-channel skew is defined as the time difference between corresponding edges on the data channels. For example, if two data channels are each programmed to transition from low to high level on a particular sample, the time difference between the rising edges on the t

### Channel-to-Channel Skew

For dynamic generation, channel-to-channel skew is defined as the time difference between
 corresponding edges on the data channels. For example, if two data channels are each
 programmed to transition from low to high level on a particular sample, the time
 difference between the rising edges on the two channels would be the channel-to-channel
 skew between the two channels.

For dynamic acquisition, channel-to-channel skew is defined as the difference between the
 sampling times for each data channel. When each sample is acquired, the point in time at
 which each data channel is sampled with respect to every other data channel is not
 identical. The difference is within some small window of time. This time window is
 referred to as the channel-to-channel skew.

Refer to *Specifications* of your device for more information about the
 channel-to-channel skew.

The following figure shows the channel-to-channel skew of a group of signals:

[IMAGE alt='image' src='GUID-3034C2D9-9B47-44E0-960B-DCFD7D84B956-a5.gif']

Specified channel-to-channel skew generally refers to the skew across all data channels
 on a device.

Parent topic:

Digital Terminology

Related concepts:

- Dynamic Acquisition

<!--NI_TOPIC bundle=ni-hsdio path=characteristic-impedance.html language=enus -->
## TOPIC 00012: Characteristic Impedance

- bundle_id: `ni-hsdio`
- source_path: `characteristic-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/characteristic-impedance.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The characteristic impedance of a transmission line influences the transient response of a signal that passing through it. The physical properties of the transmission line materials determine its characteristic impedance. For example, the dielectric of the insulators and the cross-sectional geometry

### Characteristic Impedance

The characteristic impedance of a transmission line influences the transient response of a signal
 that passing through it. The physical properties of the transmission line materials
 determine its characteristic impedance. For example, the dielectric of the insulators
 and the cross-sectional geometry of a cable determine its capacitance. Likewise, the
 inductance of the cable is a function of the length and the properties of the
 dielectric. The characteristic impedance is a function of both this inductance and
 capacitance. Manufacturers of cables provide the specification for the characteristic
 impedance of that cable, along with how it behaves over environmental extremes.

Caution

Parent topic:

Termination

Related concepts:

- Transmission Lines
- Signal Reflections

<!--NI_TOPIC bundle=ni-hsdio path=chassis-considerations.html language=enus -->
## TOPIC 00013: Chassis Considerations

- bundle_id: `ni-hsdio`
- source_path: `chassis-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/chassis-considerations.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: PXI modules are designed to operate in a PXI or Compact PCI chassis at specified environmental conditions. Device performance and reliability might be limited at temperatures above the specified operating range. For best performance, take the following precautions: Ensure that the ambient temperatur

### Chassis Considerations

PXI modules are designed to operate in a PXI or Compact PCI chassis at specified environmental
 conditions. Device performance and reliability might be limited at temperatures above the
 specified operating range. For best performance, take the following precautions:

- Ensure that the ambient temperature is within the temperature listed in the specifications document for your module, and that the temperature is stable (±5 °C).
- Follow standard metrology practices.
- Use a PXI chassis with a well designed cooling system.

Operating the module outside the specified operating temperatures might have the following
 consequences:

- Increase bias currents in the electronic components
- Increase noise
- Accelerate drifts
- Decrease product life

Beyond the maximum specified operating temperatures, the circuits perform differently than
 during the factory calibration, resulting in additional measurement errors which might not
 be accounted for by the Tempco specifications.

To minimize the temperature rise above ambient, position the chassis away from heat sources and
 clean the PXI or Compact PCI chassis air filter at regular intervals. Clean air filters are
 essential to ensuring that the devices operate at peak performance.

Operating under high humidity or dusty conditions can cause leakages between circuit components
 to increase and result in additional measurement errors.

#### Chassis
 Cooling Guidelines

Follow these guidelines to optimize cooling and ensure best
 performance and reliability:

- Always run chassis with fans set on high. In newer chassis the settings are
 HIGH and AUTO . On some older chassis the fan
 settings might be HI and LO .
- Cover all empty slots in the chassis with a blank EMC slot filler panel.
- Remove and clean the inlet filters often to prevent buildup of dust and other
 foreign material that might restrict airflow.
- Locate the chassis such that the fan inlets and outlet vents are not obstructed.
 Keep other objects and equipment a minimum of 3 inches sway from the fan inlets.

For more information regarding cooling considerations, refer to the
 *Specifications* document of your chassis.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-hsdio path=clock-position-settings.html language=enus -->
## TOPIC 00014: Clock Position Settings

- bundle_id: `ni-hsdio`
- source_path: `clock-position-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/clock-position-settings.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following clock position settings are available for the position of the exported sample clock: Inverted The exported Sample clock is an inverted copy of the sample clock. Noninverted The exported Sample clock is an exact copy of the sample clock. Delayed The exported Sample clock is a delayed ve

### Clock Position Settings

The following clock position settings are available for the position of the exported sample
 clock:

Inverted

Noninverted

Delayed

NI 656x devices have special considerations for exporting the sample clock at frequencies
 between 25 and 50 MHz.

Parent topic:

Data and Clock Position

Related concepts:

- Sample Clock
- Data Position Delay Resolution

<!--NI_TOPIC bundle=ni-hsdio path=clocks.html language=enus -->
## TOPIC 00015: Clocks

- bundle_id: `ni-hsdio`
- source_path: `clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/clocks.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the following device clocks for your digital waveform generator/analyzer.

### Clocks

You can configure the following device clocks for your digital waveform generator/analyzer.

Parent topic:

Timing and Triggering

Related concepts:

- Sample Clock
- Reference Clock
- STROBE

<!--NI_TOPIC bundle=ni-hsdio path=closing-your-session.html language=enus -->
## TOPIC 00016: Closing Your Session

- bundle_id: `ni-hsdio`
- source_path: `closing-your-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/closing-your-session.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For any application you write, you must close the specified session to close communication with the device and free resources that it has reserved. If the session is running, it is first aborted.You can close your session by using the VI or function shown in the following table. LabVIEW VI C Functio

### Closing Your Session

For any application you write, you must close the specified session to close communication with
 the device and free resources that it has reserved. If the session is running, it is
 first aborted.

You can close your session by using the VI or function shown in the following table.

| LabVIEW VI | C Function |
| --- | --- |
| niHSDIO Close | niHSDIO_close |

Note

niHSDIO_Abort

niHSDIO_reset

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-hsdio path=comparing-data-in-response-only-mode.html language=enus -->
## TOPIC 00017: Comparing Data in Response-Only Mode

- bundle_id: `ni-hsdio`
- source_path: `comparing-data-in-response-only-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/comparing-data-in-response-only-mode.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In response-only mode, the NI 655x device does not drive any data. Tt only acquires data and compares the acquired data against an expected waveform. A generation session is exclusively used to download expected data. The following figure shows the flow of comparing data in response-only mode:

### Comparing Data in Response-Only Mode

- In response-only mode, the NI 655x device does not drive any data. Tt
 only acquires data and compares the acquired data against an expected waveform. A
 generation session is exclusively used to download expected data.

The following figure shows the flow of comparing data in response-only mode:

[IMAGE alt='image' src='GUID-C2702793-35CF-401B-85E0-899E790A6574-a5.gif']

Parent topic:

Acquiring Dynamic Data

<!--NI_TOPIC bundle=ni-hsdio path=comparing-response-data-in-hardware.html language=enus -->
## TOPIC 00018: Comparing Response Data in Hardware

- bundle_id: `ni-hsdio`
- source_path: `comparing-response-data-in-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/comparing-response-data-in-hardware.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the onboard FPGA to compare the acquired response data to the expected data has the following benefits: Increases speed. Reduces the post-processing data analysis of stimulus-response applications. To develop a program to compare the response data in hardware, complete the following steps: The

### Comparing Response Data in Hardware

- Increases speed.
- Reduces the post-processing data analysis of stimulus-response
 applications.

To develop a program to compare the response data in hardware, complete the following steps:

1. The original test data is entered by a user or read from a file. The test data may contain both
 stimulus and response data. Note Use the Waveform Data Type (WDT)
 instance of the niHSDIO Write Named Waveform VI to write expected data to the
 device. The device drives any values of 0, 1,
 or Z in the waveform, while values of H, L, or X are treated as
 expected data values.
2. Stimulus data is extracted from the test data. 1s and 0s in the test data specify stimulus data;
 all other characters indicate that no data is generated, so the voltage drivers are
 disabled.
3. Use the Supported Data States property or the
 NIHSDIO_ATTR_SUPPORTED_DATA_STATES attribute to enable the
 hardware comparison block on the device during the configuration stage of both the
 generation and acquisition sessions. When hardware comparison is enabled, a
 six-state digital waveform controls acquisition, generation, and comparison,
 removing the need for parsing or software analysis.
4. Configure a start trigger for your device. Valid start trigger source and destination terminals
 include PFI <0..3>. Note RTSI and PXI trigger lines are
 not recommended for triggering hardware comparison operations because RTSI and
 PXI trigger lines are not synchronous to the data.
5. The stimulus data is generated onto the channel by the digital tester, and the response data is
 acquired. The generation and acquisition operations occur in parallel, so
 eliminating the round-trip delay can be important.
6. Once the generation and acquisition are complete, the application program performs the
 comparison on a per bit basis in software. The final pass/fail decision is only
 effected by the response data that was acquired when an H or
 L was present in the original test data.
7. For applications requiring more complex fault analysis, a fetch function can acquire the faulty
 data and any samples surrounding that error. For every sample that is in error, you
 can retrieve the following information:
  - Sample number of the fault
  - Channel(s) at fault
  - Total number of repeated errors (useful if the Filter Repeated Sample Errors
 property or the
 NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS 
 attribute are enabled)

Use the Sample Error Backlog property or the
 NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BACKLOG attribute to query how many
 errors can be returned using the niHSDIO HWC Fetch Sample Errors (U32) VI or the
 niHSDIO_HWC_FetchSampleErrors function. Use the Number Of Sample
 Errors property or NIHSDIO_ATTR_HWC_NUM_SAMPLE_ERRORS attribute, along
 with the Samples Compared property or the
 NIHSDIO_ATTR_HWC_SAMPLES_COMPARED attribute, to calculate the
 sample error rate. By capturing this information, you can perform more detailed fault
 analysis.

Note

wait

For a complete hardware compare example, refer to the Hardware Compare - Fetch Error
 Records example included with NI-HSDIO.

Parent topic:

Comparing Response Data with Expected Data

Related concepts:

- Digital Logic States
- Eliminating Round Trip Delay
- Scripts

<!--NI_TOPIC bundle=ni-hsdio path=comparing-response-data-in-software.html language=enus -->
## TOPIC 00019: Comparing Response Data in Software

- bundle_id: `ni-hsdio`
- source_path: `comparing-response-data-in-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/comparing-response-data-in-software.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: During a software comparison application, the tester: Generates the stimulus data, Captures the actual response data, Performs analysis of the response data after it is stored in the host PC memory, Analyzes the response data after storage. The following steps describe software comparison in more de

### Comparing Response Data in Software

- Generates the stimulus data,
- Captures the actual response data,
- Performs analysis of the response data after it is stored in the host PC
 memory,
- Analyzes the response data after storage.

The following steps describe software comparison in more detail:

1. You enter original test data or read the data from a file. The test data might contain both
 stimulus and response data.
2. The tester extracts stimulus data from the test data. 1s and 0s in the test data specify
 stimulus data; all other characters indicate that no data is generated, so the
 voltage drivers are disabled.
3. The digital tester generates stimulus data onto the channel and acquires the response data. The
 generation and acquisition operations occur in parallel. During this step, reducing
 the round-trip delay might be important.
4. Once the generation and acquisition are complete, the application program performs the
 comparison on a per bit basis in software. The final pass/fail decision is only
 affected by the response data acquired when an H or L digital logic state was
 present in the original test data.

To perform software comparison, you must transfer all data to the host computer for
 post-processing, which makes this method suitable for slower-speed applications.
 Transferring all the data to the host computer might exceed computer bandwidth
 limitations if more data is to be acquired than can fit on the tester’s onboard memory.
 For this situation and other cases that require faster comparison rates, real-time
 hardware comparison may be used.

Parent topic:

Comparing Response Data with Expected Data

Related concepts:

- Eliminating Round Trip Delay
- Digital Logic States
- Comparing Response Data in Hardware

<!--NI_TOPIC bundle=ni-hsdio path=comparing-response-data-with-expected-data.html language=enus -->
## TOPIC 00020: Comparing Response Data with Expected Data

- bundle_id: `ni-hsdio`
- source_path: `comparing-response-data-with-expected-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/comparing-response-data-with-expected-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate stimulus data and acquire the response data for analysis by synchronizing the generation and acquisition sessions.To perform software comparison, you must transfer all data to the host computer for post-processing, which makes this method suitable for slower-speed applications. Tran

### Comparing Response Data with Expected Data

You can generate stimulus data and acquire the response data for analysis by synchronizing the
 generation and acquisition sessions.

Note

Response-only mode

Stimulus-response mode

NI 6547/6548/655x

The following figure shows the flow of the stimulus-response mode:

[IMAGE alt='image' src='GUID-5FE4288F-C09C-4ABB-99D9-5ACC6C8B09BF-a5.gif']

Parent topic:

Programming Flow

Related concepts:

- Comparing Response Data in Hardware
- Comparing Data in Response-Only Mode
- Digital Logic States

<!--NI_TOPIC bundle=ni-hsdio path=configure-the-hardware.html language=enus -->
## TOPIC 00021: Configure the Hardware

- bundle_id: `ni-hsdio`
- source_path: `configure-the-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configure-the-hardware.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Configuration VIs and functions to set up the triggers, voltage levels, and other settings and features needed for your data operation.

### Configure the Hardware

Use Configuration VIs and functions to set up the triggers, voltage levels, and other settings
 and features needed for your data operation.

Parent topic:

Programming Flow

Related concepts:

- Acquisition Configuration Functions
- Generation Configuration Functions

<!--NI_TOPIC bundle=ni-hsdio path=configuring-a-data-rate-multiplier.html language=enus -->
## TOPIC 00022: Configuring a Data Rate Multiplier

- bundle_id: `ni-hsdio`
- source_path: `configuring-a-data-rate-multiplier.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-a-data-rate-multiplier.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the data rate multiplier for acquisition or generation operations using the following property or attribute. LabVIEW Property C Attribute Data Rate Multiplier NIHSDIO_ATTR_DATA_RATE_MULTIPLIER

### Configuring a Data Rate Multiplier

You can configure the data rate multiplier for acquisition or generation operations using the
 following property or attribute.

| LabVIEW Property | C Attribute |
| --- | --- |
| Data Rate Multiplier | NIHSDIO_ATTR_DATA_RATE_MULTIPLIER |

Parent topic:

Features

Related concepts:

- Data Rate Multiplier

<!--NI_TOPIC bundle=ni-hsdio path=configuring-and-exporting-events.html language=enus -->
## TOPIC 00023: Configuring and Exporting Events

- bundle_id: `ni-hsdio`
- source_path: `configuring-and-exporting-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-and-exporting-events.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure how events are exported with NI-HSDIO using the following VIs or functions. LabVIEW VI C Functions niHSDIO Export Signal niHSDIO_ExportSignal Events are exported until you explicitly stop exporting the event or reset the device. You must configure the event output terminal to not e

### Configuring and Exporting Events

You can configure how events are exported with NI-HSDIO using the following VIs or functions.

| LabVIEW VI | C Functions |
| --- | --- |
| niHSDIO Export Signal | niHSDIO_ExportSignal |

Note

In
 LabVIEW, to stop exporting the event, configure the event output terminal as None
 using the appropriate property and call the niHSDIO Commit VI. In C or
 LabWindows/CVI, configure the event output terminal as NIHSDIO_VAL_DO_NOT_EXPORT_STR using the appropriate attribute and call
 the niHSDIO_CommitDynamic or niHSDIO_CommitStatic
 functions.

To reset the device, call the niHSDIO Reset or niHSDIO Reset Device
 VI or call the niHSDIO_reset or
 niHSDIO_ResetDevice functions.

You can also use additional properties and attributes to configure certain aspects of your
 events.

Parent topic:

Features

Related concepts:

- Events

<!--NI_TOPIC bundle=ni-hsdio path=configuring-data-interpretation.html language=enus -->
## TOPIC 00024: Configuring Data Interpretation

- bundle_id: `ni-hsdio`
- source_path: `configuring-data-interpretation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-data-interpretation.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the data interpretation for use during static or dynamic acquisition operations using the following VI or function. LabVIEW VI C Function niHSDIO Configure Data Interpretation niHSDIO_ConfigureDataInterpretation

### Configuring Data Interpretation

You can configure the data interpretation for use during static or dynamic acquisition operations
 using the following VI or function.

| LabVIEW VI | C Function |
| --- | --- |
| niHSDIO Configure Data Interpretation | niHSDIO_ConfigureDataInterpretation |

Parent topic:

Features

<!--NI_TOPIC bundle=ni-hsdio path=configuring-data-position.html language=enus -->
## TOPIC 00025: Configuring Data Position

- bundle_id: `ni-hsdio`
- source_path: `configuring-data-position.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-data-position.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the data position for acquisition or generation operations using the following VIs or functions. LabVIEW VI C Function niHSDIO Configure Data Position niHSDIO_ConfigureDataPosition niHSDIO Configure Data Position Delay niHSDIO_ConfigureDataPositionDelay

### Configuring Data Position

You can configure the data position for acquisition or generation operations using the following
 VIs or functions.

| LabVIEW VI | C Function |
| --- | --- |
| niHSDIO Configure Data Position | niHSDIO_ConfigureDataPosition |
| niHSDIO Configure Data Position Delay | niHSDIO_ConfigureDataPositionDelay |

Parent topic:

Features

Related concepts:

- Data and Clock Position

<!--NI_TOPIC bundle=ni-hsdio path=configuring-data-width.html language=enus -->
## TOPIC 00026: Configuring Data Width

- bundle_id: `ni-hsdio`
- source_path: `configuring-data-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-data-width.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the data width for acquisition operations using the following property or attribute. LabVIEW Property C Attribute Advanced:Data Width NIHSDIO_ATTR_DATA_WIDTH Valid values for data width vary by device. Device Supported Data Widths NI 6541/6542 1, 2, 4 NI 6544/6545/6547/6548 2, 4 NI

### Configuring Data Width

You can configure the *data width* for acquisition operations using the following
 property or attribute.

| LabVIEW Property | C Attribute |
| --- | --- |
| Advanced:Data Width | NIHSDIO_ATTR_DATA_WIDTH |

Valid values for data width vary by *device*.

| Device | Supported Data Widths |
| --- | --- |
| NI 6541/6542 | 1, 2, 4 |
| NI 6544/6545/6547/6548 | 2, 4 |
| NI 655x | 1, 2, 4 |
| NI 656x | 1, 2 |

Parent topic:

Features

Related concepts:

- Data Width

<!--NI_TOPIC bundle=ni-hsdio path=configuring-generation-acquisition-frequencie.html language=enus -->
## TOPIC 00027: Configuring Generation/Acquisition Frequencies

- bundle_id: `ni-hsdio`
- source_path: `configuring-generation-acquisition-frequencie.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-generation-acquisition-frequencie.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the generation or acquisition frequencies of your device using the following VI or function. LabVIEW VI C Function niHSDIO Configure Sample Clock niHSDIO_ConfigureSampleClock Additionally, you can export a clock using the niHSDIO Export Signal VI or the niHSDIO_ExportSignal functio

### Configuring Generation/Acquisition Frequencies

You can configure the generation or acquisition frequencies of your device using the following VI
 or function.

| LabVIEW VI | C Function |
| --- | --- |
| niHSDIO Configure Sample Clock | niHSDIO_ConfigureSampleClock |

Additionally, you can export a clock using the niHSDIO Export Signal VI or the
 niHSDIO_ExportSignal function.

Parent topic:

Features

Related concepts:

- Clocks

<!--NI_TOPIC bundle=ni-hsdio path=configuring-initial-and-idle-states.html language=enus -->
## TOPIC 00028: Configuring Initial and Idle States

- bundle_id: `ni-hsdio`
- source_path: `configuring-initial-and-idle-states.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-initial-and-idle-states.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure Initial and Idle States for use during a dynamic generation operation using the following VIs or functions. LabVIEW VIs C Functions Initial StateInitial State Use one of the following instances of the niHSDIO Configure Initial State polymorphic VI: niHSDIO Configure Initial State (

### Configuring Initial and Idle States

You can configure Initial and Idle States for use during a dynamic generation operation using the
 following VIs or functions.

| LabVIEW VIs | C Functions |
| --- | --- |
| Initial State | Initial State |
| Use one of the following instances of the niHSDIO Configure Initial State polymorphic VI: niHSDIO Configure Initial State (String) niHSDIO Configure Initial State (U32) | niHSDIO_ConfigureInitialState or niHSDIO_ConfigureInitialStateU32 |

| LabVIEW VIs | C Functions |
| --- | --- |
| Idle State | Idle State |
| Use one of the following instances of the niHSDIO Configure Idle State polymorphic VI: niHSDIO Configure Idle State (String) niHSDIO Configure Idle State (U32) | niHSDIO_ConfigureIdleState or niHSDIO_ConfigureIdleStateU32 |

Parent topic:

Features

Related concepts:

- Initial and Idle States
- Dynamic Generation

<!--NI_TOPIC bundle=ni-hsdio path=configuring-input-impedance.html language=enus -->
## TOPIC 00029: Configuring Input Impedance

- bundle_id: `ni-hsdio`
- source_path: `configuring-input-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-input-impedance.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure input impedance on particular channels by setting the following property or attribute. LabVIEW Property C Attribute Input Impedance NIHSDIO_ATTR_INPUT_IMPEDANCE Configurable input impedance is not supported on NI 654x/656x devices, except for signals present on the Clk In connector

### Configuring Input Impedance

You can configure input impedance on particular channels by setting the following property or
 attribute.

| LabVIEW Property | C Attribute |
| --- | --- |
| Input Impedance | NIHSDIO_ATTR_INPUT_IMPEDANCE |

Note

Parent topic:

Features

Related concepts:

- Using Attributes with NI-HSDIO

<!--NI_TOPIC bundle=ni-hsdio path=configuring-pfi-terminal-configuration.html language=enus -->
## TOPIC 00030: Configuring PFI Terminal Configuration

- bundle_id: `ni-hsdio`
- source_path: `configuring-pfi-terminal-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-pfi-terminal-configuration.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure PFI 3 on the NI 656x to be single-ended or LVDS terminals using the properties and attributes shown in the following table. In LabVIEW, you must specify the exported signal as the active channel when you use the property. LabVIEW Property C Attribute Start Trigger Digital Edge Term

### Configuring PFI Terminal Configuration

You can configure PFI 3 on the NI 656x to be single-ended or LVDS terminals using the properties
 and attributes shown in the following table. In LabVIEW, you must specify the exported
 signal as the active channel when you use the property.

| LabVIEW Property | C Attribute |
| --- | --- |
| Start Trigger Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION |
| Script Trigger Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Script Trigger Digital Level Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Reference Trigger Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Pause Trigger Digital Level Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_TERMINAL_CONFIGURATION |
| Marker Event Terminal Configuration | NIHSDIO_ATTR_MARKER_EVENT_TERMINAL_CONFIGURATION |
| Ready for Start Event Terminal Configuration | NIHSDIO_ATTR_READY_FOR_START_EVENT_TERMINAL_CONFIGURATION |
| Ready for Advance Event Terminal Configuration | NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_CONFIGURATION |
| Data Active Event Terminal Configuration | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION |
| End of Record Event Terminal Configuration | NIHSDIO_ATTR_END_OF_RECORD_EVENT_TERMINAL_CONFIGURATION |
| Exported Start Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORTED_START_TRIGGER_TERMINAL_CONFIGURATION |
| Exported Advance Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORTED_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION |
| Exported Reference Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORTED_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Exported Script Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORTED_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Exported Pause Trigger Terminal Configuration | NIHSDIO_ATTR_EXPORTED_PAUSE_TRIGGER_TERMINAL_CONFIGURATION |

Note

Refer to *Using Attributes with NI-HSDIO* for more information about setting
 attribute-based configuration options.

Parent topic:

Features

Related concepts:

- Single-Ended Voltage Levels
- Differential Logic Families
- Using Attributes with NI-HSDIO

<!--NI_TOPIC bundle=ni-hsdio path=configuring-triggers.html language=enus -->
## TOPIC 00031: Configuring Triggers

- bundle_id: `ni-hsdio`
- source_path: `configuring-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-triggers.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure triggers with NI-HSDIO using the following VIs or functions. LabVIEW VIs C Functions Use one of the following instances of the niHSDIO Configure Trigger polymorphic VI: Digital Edge Start Trigger Pattern Match Start Trigger Software Start Trigger Disable Start Trigger Digital Edge

### Configuring Triggers

You can configure triggers with NI-HSDIO using the following VIs or functions.

| LabVIEW VIs | C Functions |
| --- | --- |
| Use one of the following instances of the niHSDIO Configure Trigger polymorphic VI: Digital Edge Start Trigger Pattern Match Start Trigger Software Start Trigger Disable Start Trigger Digital Edge Ref Trigger Pattern Match Ref Trigger Software Ref Trigger Disable Ref Trigger Digital Edge Advance Trigger Pattern Match Advance Trigger Software Advance Trigger Disable Advance Trigger Digital Edge Script Trigger Digital Level Script Trigger Software Script Trigger Disable Script Trigger Digital Level Pause Trigger Pattern Match Pause Trigger Disable Pause Trigger Digital Edge Stop Trigger Software Stop Trigger Disable Stop Trigger | niHSDIO_ConfigureDigitalEdgeStartTrigger niHSDIO_ConfigurePatternMatchStartTrigger niHSDIO_ConfigurePatternMatchStartTriggerU32 niHSDIO_ConfigureSoftwareStartTrigger niHSDIO_DisableStartTrigger niHSDIO_ConfigureDigitalEdgeRefTrigger niHSDIO_ConfigurePatternMatchRefTrigger niHSDIO_ConfigurePatternMatchRefTriggerU32 niHSDIO_ConfigureSoftwareRefTrigger niHSDIO_DisableRefTrigger niHSDIO_ConfigureDigitalEdgeAdvanceTrigger niHSDIO_ConfigurePatternMatchAdvanceTrigger niHSDIO_ConfigurePatternMatchAdvanceTriggerU32 niHSDIO_ConfigureSoftwareAdvanceTrigger niHSDIO_DisableAdvanceTrigger niHSDIO_ConfigureDigitalEdgeScriptTrigger niHSDIO_ConfigureDigitalLevelScriptTrigger niHSDIO_ConfigureSoftwareScriptTrigger niHSDIO_DisableScriptTrigger niHSDIO_ConfigureDigitalLevelPauseTrigger niHSDIO_ConfigurePatternMatchPauseTrigger niHSDIO_ConfigurePatternMatchPauseTriggerU32 niHSDIO_DisablePauseTrigger niHSDIO_ConfigureDigitalEdgeStopTrigger niHSDIO_ConfigureSoftwareStopTrigger niHSDIO_DisableStopTrigger |
| niHSDIO Send Software Edge Trigger | niHSDIO_SendSoftwareEdgeTrigger |

Parent topic:

Features

Related concepts:

- Triggers

<!--NI_TOPIC bundle=ni-hsdio path=configuring-voltage-levels.html language=enus -->
## TOPIC 00032: Configuring Voltage Levels

- bundle_id: `ni-hsdio`
- source_path: `configuring-voltage-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/configuring-voltage-levels.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI 654x/655x devices support configuring voltage levels for use with a predefined logic family during a acquisition or generation session. If you are using an NI 6547/6548/655x device, you can also configure custom voltage levels. Refer to Single-Ended Voltage Levels for information about restrictio

### Configuring Voltage Levels

NI 654x/655x devices support configuring voltage levels for use with a predefined logic family
 during a acquisition or generation session. If you are using an NI 6547/6548/655x
 device, you can also configure custom voltage levels. Refer to *Single-Ended
 Voltage Levels* for information about restrictions when configuring custom
 voltage levels.

You can configure these voltage levels using the following VIs or functions.

| LabVIEW VIs | C Functions |
| --- | --- |
| Use one of the following instances of the niHSDIO Configure Voltage polymorphic VI: niHSDIO Configure Data Voltage Logic Family niHSDIO Configure Data Voltage Custom Levels niHSDIO Configure Event Voltage Logic Family niHSDIO Configure Event Voltage Custom Levels niHSDIO Configure Trigger Voltage Logic Family niHSDIO Configure Trigger Voltage Custom Levels | niHSDIO_ConfigureDataVoltageLogicFamily, niHSDIO_ConfigureDataVoltageCustomLevels, niHSDIO_ConfigureEventVoltageLogicFamily, niHSDIO_ConfigureEventVoltageCustomLevels, niHSDIO_ConfigureTriggerVoltageLogicFamily, or niHSDIO_ConfigureTriggerVoltageCustomLevels |

Parent topic:

Features

Related concepts:

- Voltage Levels
- Logic Families
- Single-Ended Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=considerations-for-using-the-labview-real-tim.html language=enus -->
## TOPIC 00033: Considerations for using the LabVIEW Real-Time Module

- bundle_id: `ni-hsdio`
- source_path: `considerations-for-using-the-labview-real-tim.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/considerations-for-using-the-labview-real-tim.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an NI-HSDIO application in the LabVIEW Real-Time Module, follow the same steps used for developing any application in LabVIEW, using the NI-HSDIO LabVIEW VIs.Applications running NI-HSDIO in the LabVIEW Real-Time Module on a real-time target may be compromised and/or slow at 64 MB. Hardwa

### Considerations for using the LabVIEW Real-Time Module

Note

#### Hardware Support

NI-HSDIO supports operating all NI digital waveform generator/analyzers on RT
 targets.

#### Unsupported Features

When using digital waveform generator/analyzers with the LabVIEW Real-Time Module,
 the following features are not supported:

- External calibration
- Express VIs

#### Related Documentation

- For configuration instructions for remote systems, refer to the Remote Systems Help in
 Measurement & Automation Explorer (MAX) by selecting Help»Help
 Topics»Remote Systems in MAX.
- For more information on the LabVIEW Real-Time Module, refer to the LabVIEW Real-Time Module
 Help at ni.com/manuals.

Parent topic:

Using NI-HSDIO in LabVIEW

<!--NI_TOPIC bundle=ni-hsdio path=crosstalk.html language=enus -->
## TOPIC 00034: Crosstalk

- bundle_id: `ni-hsdio`
- source_path: `crosstalk.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/crosstalk.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crosstalk is the ratio of the level of the intereference on the affected channel and the actual level of the interfering signal. Crosstalk is measured in dB. Crosstalk consists of any unwanted signal on one channel that is caused by a signal on another channel.

### Crosstalk

Crosstalk is the ratio of the level of the intereference on the affected channel and
 the actual level of the interfering signal. Crosstalk is measured in dB. Crosstalk
 consists of any unwanted signal on one channel that is caused by a signal on
 another channel.

<!--NI_TOPIC bundle=ni-hsdio path=data-and-clock-position.html language=enus -->
## TOPIC 00035: Data and Clock Position

- bundle_id: `ni-hsdio`
- source_path: `data-and-clock-position.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-and-clock-position.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your digital waveform generator and analyzer allows you to configure the subperiod time at which each waveform sample is generated or acquired. This subperiod time selection is referred to as the data position. You can also configure the position of the exported Sample clock (clock position). Config

### Data and Clock Position

Your digital waveform generator and analyzer allows you to configure the subperiod time
 at which each waveform sample is generated or acquired. This subperiod time selection is
 referred to as the data position. You can also configure the position of the exported
 Sample clock (clock position).

Configuring data and clock positions enables the use of your digital waveform generator
 and analyzer in various applications:

- Measuring setup and hold times
- Measuring propagation delays
- Maximizing timing margins in high-speed data transfers

Data deskew allows you to specify the timing delay after the Sample clock rising edge
 when the device generates or acquires a new data sample. Data deskew is applied at all
 times, regardless of the value of the data or clock position. It is expressed as an
 absolute time (in seconds). Refer to the data deskew topic for your device for
 information about valid values.

Parent topic:

Digital Terminology

Related concepts:

- Data Position Settings
- Clock Position Settings

<!--NI_TOPIC bundle=ni-hsdio path=data-deskew.html language=enus -->
## TOPIC 00036: Data Deskew

- bundle_id: `ni-hsdio`
- source_path: `data-deskew.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-deskew.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data deskew specifies the delay after the sample clock rising edge when the device generates or acquires a new data sample. Data deskew is applied at all times, regardless of the data position, and is expressed as an absolute time (in seconds). When you delay the data position from the sample clock

### Data Deskew

Data deskew specifies the delay after the sample clock rising edge when the device
 generates or acquires a new data sample. Data deskew is applied at all times, regardless
 of the data position, and is expressed as an absolute time (in seconds). When you delay
 the data position from the sample clock rising edge and apply deskew, the total timing
 delay applied to the channel is the aggregate total of the data delay and data deskew
 values.

Parent topic:

Data and Clock Position

<!--NI_TOPIC bundle=ni-hsdio path=data-position-delay-resolution.html language=enus -->
## TOPIC 00037: Data Position Delay Resolution

- bundle_id: `ni-hsdio`
- source_path: `data-position-delay-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-position-delay-resolution.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital waveform generators and analyzers include three independent internal delay mechanisms: Dynamic generation delay Dynamic acquisition delay Exported sample clock delay Each mechanism can delay data and clock positions by up to one full sample clock period. For valid frequencies and ranges for

### Data Position Delay Resolution

Digital waveform generators and analyzers include three independent internal delay
 mechanisms:

- Dynamic generation delay
- Dynamic acquisition delay
- Exported sample clock delay

Each mechanism can delay data and clock positions by up to one full sample clock period.
 For valid frequencies and ranges for delays check the device specifications document.

For NI 6547/6548 devices, channels are arranged into three different banks for multibank data
 delay.

Note

The following table lists the resolution of the delay mechanisms for the frequencies that the
 digital waveform generator/analyzer internal sample clock can produce. For externally
 supplied frequencies above 25 MHz that are not listed in this table, the delay
 resolution is 1/256 of the sample clock period.

| Operating Frequency* | Resolution/Step Size† |
| --- | --- |
| 200 MHz | 20 ps‡ |
| 100 MHz | 39 ps‡ |
| 66.7 MHz | 59 ps‡ |
| 50 MHz | 78 ps |
| 40 MHz | 98 ps |
| 33.3 MHz | 117 ps |
| 28.6 MHz | 137 ps |
| 25 MHz | 156 ps |

<sup>*</sup>Not all operating frequencies may be applicable on your device.

<sup>†</sup>These values are not supported for NI 6544/6545/6547/6548 devices.

<sup>‡</sup>For NI 656x devices, refer to the device specifications document for more
 information about the supported step sizes.

Parent topic:

Data and Clock Position

Related concepts:

- Dynamic Generation
- Dynamic Acquisition
- Sample Clock

<!--NI_TOPIC bundle=ni-hsdio path=data-position-settings.html language=enus -->
## TOPIC 00038: Data Position Settings

- bundle_id: `ni-hsdio`
- source_path: `data-position-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-position-settings.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following data position settings are available for acquisition and generation channels: Sample clock rising edge Data is generated/acquired on the rising edge of the clock driving the operation. Sample clock falling edge Data is generated/acquired on the falling edge of the clock driving the ope

### Data Position Settings

The following data position settings are available for acquisition and generation channels:

Sample clock rising edge

Sample clock falling edge

Delay from Sample clock rising edge

Note

Parent topic:

Data and Clock Position

Related concepts:

- Data Position Delay Resolution
- Configuring Data Position

<!--NI_TOPIC bundle=ni-hsdio path=data-position-with-ddr.html language=enus -->
## TOPIC 00039: Data Position with DDR

- bundle_id: `ni-hsdio`
- source_path: `data-position-with-ddr.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-position-with-ddr.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure acquisition and generation sessions to control when the first data sample is acquired or generated. The sample can occur on: The rising edge of the sample clock The falling edge of the sample clock A delayed version of the rising edge, when the data rate multiplier is set for DDR (

### Data Position with DDR

You can configure acquisition and generation sessions to control when the
 first data sample is acquired or generated.

The sample can occur on:

- The rising edge of the sample clock
- The falling edge of the sample clock
- A delayed version of the rising edge, when the data rate
 multiplier is set for DDR (Double Data Rate)
 operation

The second sample is acquired or generated on each subsequent sample clock edge. Notice that the
 delay is still a fraction of the entire sample clock period.
 These data positions are shown in the following figure:

[IMAGE alt='image' src='GUID-1A1D0A80-ECB2-4ED7-97DC-E8DE813C6CAA-a5.gif']

Parent topic:

Double Data Rate (DDR)

Related concepts:

- Acquisition Considerations for DDR
- Generation Considerations for DDR

<!--NI_TOPIC bundle=ni-hsdio path=data-rate-multiplier.html language=enus -->
## TOPIC 00040: Data Rate Multiplier

- bundle_id: `ni-hsdio`
- source_path: `data-rate-multiplier.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-rate-multiplier.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital waveform generators and analyzers can be configured to acquire and/or generate data once per sample clock period (single data rate, or SDR mode) or twice per sample clock period (double data rate, or DDR mode). DDR is currently available only on the NI 6547/6548 and NI 656x devices.You can c

### Data Rate Multiplier

Digital waveform generators and analyzers can be configured to acquire and/or generate
 data once per sample clock period (single data rate, or SDR mode) or twice per sample
 clock period (double data rate, or DDR mode).

Note

You can configure the data rate
 multiplier for your acquisition and generation sessions by configuring the data rate
 multiplier property/attribute in NI-HSDIO.

Parent topic:

Digital Terminology

Related concepts:

- Configuring a Data Rate Multiplier

<!--NI_TOPIC bundle=ni-hsdio path=data-width.html language=enus -->
## TOPIC 00041: Data Width

- bundle_id: `ni-hsdio`
- source_path: `data-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/data-width.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data width is the size, in bytes, of a raw sample from the operation. Raw sample refers to the native format and organization of the device, which can be an 1-, 2-, or 4-byte integer. You can increase memory depth during dynamic acquisition by reducing the number of active channels. To do this, spec

### Data Width

Data width is the size, in bytes, of a raw sample from the operation. Raw sample refers
 to the native format and organization of the device, which can be an 1-, 2-, or 4-byte
 integer.

You can increase memory depth during dynamic acquisition by reducing the number of active
 channels.

To do this, specify a data width smaller than the total number of available bits for your
 device. For example, if you acquire data on eight of the 16 channels of an PXI 656x and
 you specify a data width of one byte, you can store twice as many samples than if you
 had specified the data width as being the entire two bytes.

Data width is read-only during generation sessions.

Parent topic:

Digital Terminology

Related concepts:

- Dynamic Acquisition

<!--NI_TOPIC bundle=ni-hsdio path=differential-logic-families.html language=enus -->
## TOPIC 00042: Differential Logic Families

- bundle_id: `ni-hsdio`
- source_path: `differential-logic-families.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/differential-logic-families.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Differential logic families use differential voltage levels to measure the voltage difference between a pair of wires. These logic families interpret the difference as a binary 1 or binary 0. Low-Voltage Differential Signaling (LVDS)LVDS is a low-noise, low-power, low-amplitude differential method f

### Differential Logic Families

Differential logic families use differential voltage levels to measure the voltage difference
 between a pair of wires. These logic families interpret the difference as a binary
 **1** or binary **0**.

#### Low-Voltage Differential Signaling
 (LVDS)

LVDS is a low-noise, low-power, low-amplitude differential method for
 high-speed digital data transfer.

The following figure shows a diagram of a
 typical LVDS circuit:

[IMAGE alt='image' src='GUID-B574EB74-3A28-4409-AB0D-4EAE7B942B48-a5.gif']

A current source at the driver provides approximately 3.5 mA of current. The
 direction of the current depends on whether the driver drives a logic high level or low
 level. When the current reaches the receiver, a 100 Ω terminating resistor connects the
 two ends of the differential transmission line to provide a return path for the current.
 A voltage of approximately 350 mV (3.5 mA x 100 Ω) is established across the two input
 terminals of the receiver. The differential voltage at the receiver is either positive
 or negative, depending on the direction of the current. The receiver recognizes a
 positive differential voltage signal as a logic high level (binary
 **1**) and a negative differential voltage as a logic low
 level (binary **0**).

The electrical characteristics of
 an LVDS signal offers many performance improvements compared to single-ended standards.
 For example, since the received voltage is a differential between two signals, the
 voltage swing between the logic high level and low level state can be smaller, allowing
 for faster rise and fall times and thus faster toggle and data rates. Also, as with
 LVPECL circuits, the differential receiver is less susceptible to common-mode noise than
 single-ended transmission methods.

The LVDS standard defines the electrical
 aspects of this type of data transmission. The standard defines driver and receiver
 electrical characteristics only. The standard does not create protocol, interconnect, or
 connector definitions because these aspects are application-specific.

Note

#### Low-Voltage Positive Emitter-Coupled Logic (LVPECL)

Emitter-coupled logic
 (ECL) circuits use a design with transistors that steer current through gates to compute
 logical functions. Because the transistors are always in the active region, they can
 change state very rapidly, so ECL circuits might operate at very high speeds.

LVPECL circuits are a type of ECL circuit that require a pair of signal lines for each
 channel. The differential transmission scheme is less susceptible to common-mode noise
 than single-ended transmission methods. LVPECL circuits are designed for use with supply
 voltages of 3 V or 3.3 V.

Parent topic:

Logic Families

Related concepts:

- Differential Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=differential-voltage-levels.html language=enus -->
## TOPIC 00043: Differential Voltage Levels

- bundle_id: `ni-hsdio`
- source_path: `differential-voltage-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/differential-voltage-levels.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Unlike single-ended signals, differential signals are transmitted in parity. That is, instead of a single conductor referenced to ground, two conductors, referenced to each other, transmit data. The digital driver still drives two voltages, as in the single-ended case. The receiver, however, interpr

### Differential Voltage Levels

Unlike single-ended signals, differential signals are transmitted in parity. That is, instead of
 a single conductor referenced to ground, two conductors, referenced to each other,
 transmit data. The digital driver still drives two voltages, as in the single-ended
 case. The receiver, however, interprets the signals based on the voltage difference
 between the pair of signals — not on a reference to ground. For the differential digital
 signal to be interpreted as a binary **0**, the signal must be
 less than its complementary signal by more than a particular value, shown as
 V<sub>TH</sub> in the following figure. V<sub>TH</sub> varies and is specified by
 the particular logic *family*.

The conductors are referenced and transmitted together. Therefore, you can achieve higher noise
 immunity in your signals by using differential signals. A benefit to this transmission
 scheme is that you can allow much smaller signal swings. Therefore, you can transmit
 data farther, faster, and at a fraction of the power.

Since differential signals reference a positive signal to a complementary signal, across a
 specified differential impedance, voltage levels are typically specified from a
 differential, rather than an absolute, perspective (depending on the standard).

For example, the absolute voltage levels of an LVDS transmission pair across a 100 Ω
 differential terminating impedance may have a V<sub>OH</sub> of 1.4 V on the positive
 conductor and a V<sub>OL</sub> of 1.1 V on the complementary conductor. The differential
 voltage would then be called out as the difference between the two—300 mV, shown as
 V<sub>OD</sub> in the following figure. There is, however, a common-mode component
 of the signal, shown as V<sub>OS</sub> in the illustration below, that is also called
 out by most differential specifications and is referenced to common.

For differential digital waveform generator/analyzers, the voltage levels are defined as
 follows:

OD

OS

TH

RANGE

When connecting a differential digital waveform generator/analyzer to a DUT, ensure that the
 interface voltage levels are compatible. The relationship between the differential
 device voltage levels and the DUT voltage levels are shown in the following figure:

[IMAGE alt='image' src='GUID-3292A02B-4A57-41FB-B423-3544EE50C2D0-a5.gif']

The total NIM is computed by the following formula:

N

I

M

=

m

i

n

G

e

n

e

r

a

t

i

o

n

V

O

D

-

D

U

T

V

T

H

,

D

U

T

V

O

D

-

A

c

q

u

i

s

i

t

i

o

n

V

T

H

The SHB12X-B12X shielded cable for differential high-speed digital signals provides excellent
 protection against external noise sources.

Parent topic:

Voltage Levels

Related concepts:

- Differential Logic Families

<!--NI_TOPIC bundle=ni-hsdio path=digital-logic-states.html language=enus -->
## TOPIC 00044: Digital Logic States

- bundle_id: `ni-hsdio`
- source_path: `digital-logic-states.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-logic-states.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can choose from a number of different digital I/O instruments with a range of features for communication and test applications. The primary function of digital instruments is to drive a digital pattern of binary 1s and 0s. Digital instruments might also support waveforms that might include certa

### Digital Logic States

You can choose from a number of different digital I/O instruments with a range of features for
 communication and test applications.

The primary function of digital instruments is to drive a digital pattern
 of binary 1s and 0s. Digital instruments might also support
 waveforms that might include certain parts of the logic states
 from the following table:

|  | Logic State | Drive Data | Expected Response |
| --- | --- | --- | --- |
| Drive States | 0 | Logic Low | Don’t Care |
| Drive States | 1 | Logic High | Don’t Care |
| Drive States | Z | Disable | Don’t Care |
| Compare States | L | Disable | Logic Low |
| Compare States | H | Disable | Logic High |
| Compare States | X | Disable | Don’t Care |

The six logic states control the voltage driver and, if supported, the compare engine of the
 digital tester on a per clock cycle basis. The drive states
 specify what stimulus data the tester drives on a particular
 channel or when to disable the voltage driver. This state is
 referred to as the tristate or high-impedance state. Compare
 states indicate the expected response from the DUT. These six
 logic states make it possible to perform bidirectional
 communication and real-time hardware comparison of acquired
 response data.

Only the NI 6547/6548/655x digital waveform generators and analyzers support all six logic states
 shown in the preceding table, allowing the devices to perform bidirectional stimulus/response
 test options with hardware comparison. Other digital waveform generators and analyzers can
 perform simultaneous generation and acquisition using 1's and 0's, but they do not support
 bidirectional operation.

Parent topic:

Digital Logic

Related concepts:

- Comparing Response Data with Expected Data

<!--NI_TOPIC bundle=ni-hsdio path=digital-logic.html language=enus -->
## TOPIC 00045: Digital Logic

- bundle_id: `ni-hsdio`
- source_path: `digital-logic.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-logic.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about digital logic families and states.

### Digital Logic

This section contains information about digital logic families and states.

<!--NI_TOPIC bundle=ni-hsdio path=digital-terminology.html language=enus -->
## TOPIC 00046: Digital Terminology

- bundle_id: `ni-hsdio`
- source_path: `digital-terminology.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-terminology.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains the key terms used in this document.

### Digital Terminology

This section explains the key terms used in this document.

<!--NI_TOPIC bundle=ni-hsdio path=digital-waveform-data-representation-in-c.html language=enus -->
## TOPIC 00047: Digital Waveform Data Representation in C

- bundle_id: `ni-hsdio`
- source_path: `digital-waveform-data-representation-in-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-waveform-data-representation-in-c.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: As in LabVIEW, the NI-HSDIO C functions represent digital waveform data in two formats. Data can be represented as a one-dimensional array of binary data or in an expanded Waveform Data Type (WDT) format.Each integer value in the array corresponds to the state of one channel during one sample of the

### Digital Waveform Data Representation in C

As in LabVIEW, the NI-HSDIO C functions represent digital waveform data in two formats. Data can
 be represented as a one-dimensional array of binary data or in an expanded Waveform Data
 Type (WDT) format.

Each integer value in the array corresponds to the state of one channel during one sample of the
 waveform. The following example shows writing a waveform in the waveform data type
 format:

```text
ViUInt8 data[NUM_BITS * NUM_SAMPLES] = {
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 1,
0, 0, 0, 0, 0, 0, 1, 0,
0, 0, 0, 0, 0, 0, 1, 1,
...
1, 1, 1, 0, 0, 1, 1, 1,
};
error = niHSDIO_WriteNamedWaveformWDT( vi, waveformName, NUM_SAMPLES, NIHSDIO_VAL_GROUP_BY_SAMPLE, data;
```

If your device supports per cycle tristate or hardware compare, use the waveform data type format
 to use this feature. The digital state values for 0, 1, Z, L, H, and X. are defined in the
 niHSDIO.h header file under Digital Channel States, as follows:

```text
#define NI_DIO_0 0
#define NI_DIO_1 1
#define NI_DIO_Z 2
#define NI_DIO_L 3
#define NI_DIO_H 4
#define NI_DIO_X 5
```

Parent topic:

Digital Waveform Data Representation

Related concepts:

- Digital Waveform Data Representation in LabVIEW
- Per Cycle Tristate
- Hardware Comparison

<!--NI_TOPIC bundle=ni-hsdio path=digital-waveform-data-representation-in-labvi.html language=enus -->
## TOPIC 00048: Digital Waveform Data Representation in LabVIEW

- bundle_id: `ni-hsdio`
- source_path: `digital-waveform-data-representation-in-labvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-waveform-data-representation-in-labvi.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-HSDIO supports two data types to represent digital waveform data. The first data type is as a one-dimensional array of integer data. The following figures show the LabVIEW control for this data type and an example of a VI wired to the data type: The following figures show the control for the LabV

### Digital Waveform Data Representation in LabVIEW

NI-HSDIO supports two data types to represent digital waveform data. The first data type is as a
 one-dimensional array of integer data. The following figures show the LabVIEW control
 for this data type and an example of a VI wired to the data type:

[IMAGE alt='image' src='GUID-21E5BCB3-5A82-41C0-AD3A-BCDEE69E6BD3-a5.gif']

[IMAGE alt='image' src='GUID-38FE6F2A-E8DE-4B9E-9030-91E47EBCA4A9-a5.gif']

The following figures show the control for the LabVIEW digital Waveform Data Type (WDT) and an
 example of a VI wired to the data type:

[IMAGE alt='image' src='GUID-AC685979-3DB7-4146-B87C-E1ED23C1E9DA-a5.gif']

[IMAGE alt='image' src='GUID-059B9310-A017-4119-AD00-F3357CCA2131-a5.gif']

VIs in NI-HSDIO that write or read/fetch digital waveform data can accept either data type.

The digital WDT includes digital values and attribute information, such as time stamps. Raw data,
 such as the U32 array data, consist only of the digital values.

If you intend to graph data using the LabVIEW digital waveform graph, it is recommended that you
 use the WDT, as it can be directly wired, as shown in the following figure.

[IMAGE alt='image' src='GUID-64E9B9F2-2B5F-4624-B40E-6DD4D645315C-a5.gif']

[IMAGE alt='image' src='GUID-643AECAC-2202-41A9-8478-1F61B2C88267-a5.gif']

#### Creating Waveforms with per Cycle Tristate
 Capabilities

NI-HSDIO provides the niHSDIO Convert Binary to DWDT VI to
 convert digital waveforms containing Z values from a U32 array of binary data values
 and a U32 array of masks of which channels to tristate.

Parent topic:

Digital Waveform Data Representation

<!--NI_TOPIC bundle=ni-hsdio path=digital-waveform-data-representation.html language=enus -->
## TOPIC 00049: Digital Waveform Data Representation

- bundle_id: `ni-hsdio`
- source_path: `digital-waveform-data-representation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/digital-waveform-data-representation.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-HSDIO supports two data types to represent digital waveform data. The first data type is as a one-dimensional array of integer data. The other data type is the digital waveform data type (WDT). VIs and functions in NI-HSDIO that write or read/fetch digital waveform data can accept either data typ

### Digital Waveform Data Representation

NI-HSDIO supports two data types to represent digital waveform data. The first data type is as a
 one-dimensional array of integer data. The other data type is the digital waveform data type
 (WDT). VIs and functions in NI-HSDIO that write or read/fetch digital waveform data can accept
 either data type.

- Z
- X
- H
- L

One difference between U32 array data and WDT data is memory usage. Each sample of U32 data
 occupies four bytes of PC memory, independent of the number of channels being
 used. Each sample of a digital WDT data occupies one byte for each channel used,
 but unused channels do not occupy memory. Thus, a 1,000-sample waveform of
 16 channels represented in a raw U32 array would occupy (4 Bytes/sample) x (1,000
 samples) = 4,000 Bytes.

The same 1,000 sample waveform represented in a WDT would occupy approximately (1 byte/channel) x
 (16 channels/sample) x (1,000 samples) = 16,000 Bytes.

Parent topic:

Getting Started with NI-HSDIO

Related concepts:

- Digital Waveform Data Representation in LabVIEW
- Digital Waveform Data Representation in C

<!--NI_TOPIC bundle=ni-hsdio path=direct-dma.html language=enus -->
## TOPIC 00050: Direct DMA

- bundle_id: `ni-hsdio`
- source_path: `direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/direct-dma.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA is used to transfer waveform data to and from device onboard memory at rates higher than the typical 5 to 30 MB/sec range in a standard PC-based architecture. To achieve these high rates, direct DMA establishes a direct connection between device onboard memory and a specialized waveform d

### Direct DMA

Direct DMA is used to transfer waveform data to and from device onboard memory at rates higher
 than the typical 5 to 30 MB/sec range in a standard PC-based architecture. To achieve
 these high rates, direct DMA establishes a direct connection between device onboard
 memory and a specialized waveform data source. Direct DMA is commonly used to stream
 waveform data from disk at data rates of higher than 100 MB/sec. The StreamStor™
 products of Conduant are an example of direct DMA-compatible data sources.

#### Configuring Your Application for Direct DMA

Direct DMA is available for
 both acquisition and generation. For acquisition operations, use the direct DMA
 instance of the niHSDIO Fetch Waveform VI; no additional
 attribute configurations are needed. For generation operations, complete the
 following steps to configure your application for direct DMA.

1. Enable the device for direct DMA writes by setting the direct DMA
 Enable property or the
 NIHSDIO_ATTR_DIRECT_DMA_ENABLED attribute to TRUE. Once
 enabled, NI-HSDIO monitors and reports any issues with the direct DMA
 transfer.
2. Identify the waveform data source and set the direct DMA Window
 Address property or the
 NIHSDIO_ATTR_DIRECT_DMA_WINDOW_ADDRESS attribute to the
 address provided by your direct DMA-compatible data source.
3. Set the direct DMA Window Size property or the
 NIHSDIO_ATTR_DIRECT_DMA_WINDOW_SIZE attribute to the size
 of the memory window provided by your direct DMA compatible data source.
4. In LabVIEW, use the Direct DMA instance of the niHSDIO Write Named
 Waveform VI . In C/CVI , use the instance of the
 write named waveform function that corresponds to the data width of your device
 to write blocks of data to the device. For each block of data written to the
 device, you pass the direct DMA window address to the data parameter. This frees
 up host memory, because the arrays of samples do not reside in host memory.
 NI-HSDIO detects when the address is within the direct DMA window and handles
 the transfer appropriately.

Parent topic:

Generating Waveforms Using Streaming

Related concepts:

- Generating Waveforms Using Streaming
- Writing Waveforms to Your Device

<!--NI_TOPIC bundle=ni-hsdio path=double-data-rate-ddr.html language=enus -->
## TOPIC 00051: Double Data Rate (DDR)

- bundle_id: `ni-hsdio`
- source_path: `double-data-rate-ddr.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/double-data-rate-ddr.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the data rate multiplier is configured for DDR operation, the digital waveform generator and analyzer generates or acquires data twice per Sample clock period. The digital waveform generator and analyzer trades channel count for data rate by generating or acquiring on half the number of channel

### Double Data Rate (DDR)

When the data rate multiplier is configured for DDR operation, the digital waveform generator and
 analyzer generates or acquires data twice per Sample clock period. The digital waveform
 generator and analyzer trades channel count for data rate by generating or acquiring on
 half the number of channels but at twice the rate. The phase relationship of the data to
 the sample clock is determined by the data position. While you can configure the data
 rate multiplier for acquisition and generation separately, you cannot have both SDR
 channels and DDR channels in the same direction.

The following figure shows an example of DDR generation configured for rising edge data
 position:

[IMAGE alt='image' src='GUID-74C8343A-A6CD-4331-BB5F-32D84B81ED77-a5.gif']

Note

The NI 6547/6548 allows the user to determine whether acquisition or generation will use
 the upper or lower sixteen channels. The NI 6547/6548 also allows both acquisition and
 generation on the same set of channels at the same time.

Configuring the data rate multiplier for DDR operation impacts memory usage, data width,
 and other aspects of your application. Refer to the device documentation to determine if
 DDR mode meets your application needs.

Parent topic:

Data Rate Multiplier

Related concepts:

- Configuring a Data Rate Multiplier
- Data Position with DDR
- Onboard Memory
- Data Width

<!--NI_TOPIC bundle=ni-hsdio path=drive-type.html language=enus -->
## TOPIC 00052: Drive Type

- bundle_id: `ni-hsdio`
- source_path: `drive-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/drive-type.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Drive type describes the behavior of the generation channels. Single-ended high-speed digital waveform generators and analyzers support two drive types: active drive and open collector. The generation drive type can be configured individually for each channel and is available for dynamic and static

### Drive Type

Drive type describes the behavior of the generation channels. Single-ended high-speed digital
 waveform generators and analyzers support two drive types: active drive and open
 collector. The generation drive type can be configured individually for each channel and
 is available for dynamic and static operations.

For active drive channels, data is fed to the output driver. For open-collector channels, the
 data provided to the output driver is always zero, and the data is fed to the tristate
 control terminal of the output driver.

You can configure all digital waveform generators and analyzers for active drive generation and
 some for open collector generation. When configured for active drive generation, a
 channel generates the **Generation Voltage High** level for
 logic 1. When configured for open-collector generation, a channel goes to the
 high-impedance state for logic 1. In both cases, a channel generates the
 **Generation Voltage Low** level for logic 0.

Parent topic:

Generation

Related concepts:

- Active Drive
- Open Collector

<!--NI_TOPIC bundle=ni-hsdio path=dynamic-acquisition.html language=enus -->
## TOPIC 00053: Dynamic Acquisition

- bundle_id: `ni-hsdio`
- source_path: `dynamic-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/dynamic-acquisition.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dynamic acquisition is a clocked event in which digital data is transferred from the DUT into onboard memory. The logic state of each acquisition is determined by the configured data interpretation method. The acquisition voltage levels are defined by your dynamic acquisition operation. At every clo

### Dynamic Acquisition

Dynamic acquisition is a clocked event in which digital data is transferred from the DUT into
 onboard memory. The logic state of each acquisition is determined by the configured data
 interpretation method. The acquisition voltage levels are defined by your dynamic
 acquisition operation.

At every clock edge, the pattern acquisition engine stores the current state of each DIO channel
 configured for dynamic acquisition into onboard memory as a sample. Samples are stored
 in the order they are received to onboard memory as a record. You can configure the
 number of samples for each record.

Parent topic:

Acquisition

Related concepts:

- Onboard Memory
- Configuring Data Interpretation
- Voltage Levels
- Records

<!--NI_TOPIC bundle=ni-hsdio path=dynamic-generation.html language=enus -->
## TOPIC 00054: Dynamic Generation

- bundle_id: `ni-hsdio`
- source_path: `dynamic-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/dynamic-generation.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dynamic generation is a clocked operation where binary data is sent from the device to the DUT across multiple digital channels. The data is generated based on complex scripts, and it can react to triggers, generate markers, and be shifted in time with respect to the generating clock.

### Dynamic Generation

Dynamic generation is a clocked operation where binary data is sent from the device to the DUT
 across multiple digital channels. The data is generated based on complex scripts, and it
 can react to triggers, generate markers, and be shifted in time with respect to the
 generating clock.

Parent topic:

Generation

Related concepts:

- Scripts

<!--NI_TOPIC bundle=ni-hsdio path=edge-trigger.html language=enus -->
## TOPIC 00055: Edge Trigger

- bundle_id: `ni-hsdio`
- source_path: `edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/edge-trigger.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital signal has the following discrete levels: high level low level When the signal transitions from high to low or from low to high, a digital edge is created. A digital signal has the following types of edges: Rising Occurs when the signal transitions from low level to high level. Falling Occ

### Edge Trigger

A digital signal has the following discrete levels:

- high level
- low level

When the signal transitions from high to low or from low to high, a
 digital edge is created. A digital signal has the following
 types of edges:

Rising

Falling

Triggers configured to act on a rising or falling edge of a digital
 signal are called edge triggers.

In the following figure, an edge trigger could be configured to occur either at the place
 labeled Falling Edge of Signal or at Rising Edge of Signal.

[IMAGE alt='image' src='GUID-0D960D37-FDB6-4DF1-B0BF-CFA84A02375E-a5.gif']

Parent topic:

Types of Triggers

<!--NI_TOPIC bundle=ni-hsdio path=eliminating-round-trip-delay.html language=enus -->
## TOPIC 00056: Eliminating Round Trip Delay

- bundle_id: `ni-hsdio`
- source_path: `eliminating-round-trip-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/eliminating-round-trip-delay.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you perform a stimulus-response application, the time required for data to move from the digital tester, through the cable and DUT, and back to the tester is known as round trip delay (RTD).One way to account for round-trip delay is by exporting a signal with an edge that is synchronous to the

### Eliminating Round Trip Delay

When you perform a stimulus-response application, the time required for data to move from the
 digital tester, through the cable and DUT, and back to the tester is known as round trip delay
 (RTD).

One way to account for round-trip delay is by exporting a signal with an edge that is synchronous
 to the start of the stimulus data. This signal must be routed through equal lengths of cable
 to the acquisition start trigger so that the signal has the same round trip delay as the data.
 Use the Data Active event to export the signal, because it is synchronous to the start of the
 stimulus data.

The following figure illustrates the signal routing involved in elimination round trip delay.

[IMAGE alt='image' src='GUID-1C4E1B1C-6FB3-41FD-A4D8-0429F5C2879C-a5.gif']

For example, you can export the Data Active event on PFI 1 and route it to PFI 2, which you can
 configure as the acquisition Start trigger source. Then you can export the generation Sample
 clock to DDC CLK OUT and configure the acquisition Sample clock source as STROBE. Match your
 cable lengths so that the signals are routed with the same round trip delay as the data. This
 method ensures that clocks, control signals, and data signals all arrive at the device at the
 same time.

Another method to account for round-trip delay is to internally route a delayed version of your
 Data Active event to your acquisition Start trigger. To use this method, you must first know
 your total round-trip delay. After you know this delay, set the Data Active Internal Route
 Delay property or the NIHSDIO_ATTR_DATA_ACTIVE_INTERNAL_ROUTE_DELAY attribute
 to that number of clock cycles. Then set the Data Position Delay property or the
 NIHSDIO_ATTR_DATA_POSITION_DELAY attribute to the desired fractional
 delay.

Parent topic:

Features

Related concepts:

- Events Summary

<!--NI_TOPIC bundle=ni-hsdio path=events-summary.html language=enus -->
## TOPIC 00057: Events Summary

- bundle_id: `ni-hsdio`
- source_path: `events-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/events-summary.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes the event types supported by digital waveform generators and analyzers. The Used In column indicates which types of operations can use an event type. Event Name Used In Description Data Active Event Generation The data active event indicates when the pattern generation

### Events Summary

The following table describes the event types supported by digital waveform generators and
 analyzers. The Used In column indicates which types of operations can use an
 event type.

| Event Name | Used In | Description |
| --- | --- | --- |
| Data Active Event | Generation | The data active event indicates when the pattern generation engine is generating data. If the pattern generation engine is waiting for a trigger or is paused, the data active event is deasserted. When the pattern generation engine is generating data, the data active event is asserted, synchronous with the data. |
| Marker Event | Generation | The marker event is a general-purpose event that is configured within a generation script. The marker event can be asserted synchronous to any even numbered sample within a waveform within a script. For example, the marker event can be asserted when sample 432 of waveform A is generated. You can create multiple marker events for use in your application. Note When using DDR mode, marker positions will have a quantization twice that of SDR mode. Refer to your device specifications for more information about marker quantization. |
| Ready for Start Event | Acquisition, Generation | For both acquisition and generation, the ready for start event indicates that the digital waveform generator and analyzer is configured and ready to receive a start trigger. |
| Ready for Advance Event | Acquisition | An event that indicates when the device enters its wait for advance trigger state, which indicates that the acquisition of the previous record is complete. |
| End of Record Event | Acquisition | An event that indicates when the device enters its record complete state, which indicates that the current record has been acquired. |
| Sample Error Event | Hardware Comparison | An event that indicates when the device detects a sample where the actual response and the expected response do not match. |

Parent topic:

Events

Related concepts:

- Dynamic Generation
- Double Data Rate (DDR)
- Dynamic Acquisition
- Hardware Comparison

<!--NI_TOPIC bundle=ni-hsdio path=events.html language=enus -->
## TOPIC 00058: Events

- bundle_id: `ni-hsdio`
- source_path: `events.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/events.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: An event is a signal generated by the device at a device state. Typically, events are configured to indicate when a specific hardware condition is met. After the condition is met, the event is exported. Events are exported until you explicitly stop the event or reset the device. You must configure t

### Events

An event is a signal generated by the device at a device state. Typically, events are
 configured to indicate when a specific hardware condition is met. After the
 condition is met, the event is exported.

Events are exported until you explicitly stop the event or reset the device. You
 must configure the event output terminal to not export the event within the
 same session in which it was routed. After the session is closed, the signal
 is exported until the device is reset. In LabVIEW, to stop exporting the
 event, configure the event output terminal as None using the appropriate
 property and call the niHSDIO Commit VI. In C or LabWindows/CVI, configure
 the event output terminal as NIHSDIO_VAL_DO_NOT_EXPORT_STR using the
 appropriate attribute and call the niHSDIO_CommitDynamic or
 niHSDIO_CommitStatic functions.

To reset the device, call the niHSDIO Reset or niHSDIO Reset Device VI or call the
 niHSDIO_reset or niHSDIO_ResetDevicefunctions.

Refer to *Triggers Summary* and *Events Summary* for descriptions
 of the triggers and events you can use with your device.

Parent topic:

Timing and Triggering

Related concepts:

- Configuring and Exporting Events
- Triggers Summary
- Events Summary

<!--NI_TOPIC bundle=ni-hsdio path=features.html language=enus -->
## TOPIC 00059: Features

- bundle_id: `ni-hsdio`
- source_path: `features.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/features.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections explain how to configure certain features of the digital waveform generator/analyzer with NI-HSDIO.

### Features

The following sections explain how to configure certain features of the digital waveform
 generator/analyzer with NI-HSDIO.

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-hsdio path=file-i-o-and-digital-waveform-data.html language=enus -->
## TOPIC 00060: File I/O and Digital Waveform Data

- bundle_id: `ni-hsdio`
- source_path: `file-i-o-and-digital-waveform-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/file-i-o-and-digital-waveform-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Remove fluff (first sentence: "Use the .hws file format to store digital waveform data on a disk. To retrieve that data, use file I/O in your program. The Hierarchical Waveform Storage (NI-HWS) provides a set of functions for easily and efficiently storing and retrieving digital waveform data files.

### File I/O and Digital Waveform Data

Remove fluff (first sentence: "Use the .hws file format to store digital waveform data on a disk.
 To retrieve that data, use file I/O in your program. The Hierarchical Waveform Storage
 (NI-HWS) provides a set of functions for easily and efficiently storing and retrieving digital
 waveform data files. NI-HWS works with binary data (U8, U16, and U32) and Waveform Data Type
 (WDT) data, as shown in the LabVIEW code snippets in the following figure:

[IMAGE alt='image' src='GUID-BF6D5C25-6569-418B-A098-46CB6FDE5795-a5.gif']

NI-HWS can convert some waveform data from the data type in which it was stored to a different
 data type when the data is read or retrieved. The table below shows the supported type
 conversions.

Note

| Stored Type | Retrieved Type: DigitalWDT | Retrieved Type: Digital1D U8 | Retrieved Type: Digital2D U8 | Retrieved Type: Digital1D U16 | Retrieved Type: Digital2D U16 | Retrieved Type: Digital1D U32 | Retrieved Type: Digital2D U32 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DigitalWDT | Yes | — | — | — | — | — | — |
| Digital1D U8 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Digital2D U8 | Yes | — | Yes | — | Yes | — | Yes |
| Digital1D U16 | Yes | Yes* | Yes* | Yes | Yes | Yes | Yes |
| Digital2D U16 | Yes | — | Yes* | — | Yes | — | Yes |
| Digital1D U32 | Yes | Yes* | Yes* | Yes* | Yes* | Yes | Yes |
| Digital2D U32 | Yes | — | Yes* | — | Yes* | — | Yes |

<sup>*</sup>For digital waveforms, smaller data types can read larger data types with the
 following restrictions: the data must be mapped and all mapped bits must be within the smaller
 data types range.

When digital data is retrieved as WDT, the Dynamic Channel List attribute is used to determine
 the number of channels of data that the digital WDT contains. When data is initially stored as
 WDT, this attribute is automatically set.

The Digital Waveform Editor (DWE) uses digital .hws files as its native file
 format for easy transfer of data between the DWE and your programming environment. The
 following figure illustrates the relationship between your programming environment, the DWE,
 and .hws files.

[IMAGE alt='image' src='GUID-4B0ED147-C34E-4589-8A44-85D8B338F865-a5.gif']

Parent topic:

Digital Waveform Data Representation

Related concepts:

- Digital Waveform Data Representation

<!--NI_TOPIC bundle=ni-hsdio path=generating-data-in-single-waveform-mode.html language=enus -->
## TOPIC 00061: Generating Data in Single-Waveform Mode

- bundle_id: `ni-hsdio`
- source_path: `generating-data-in-single-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generating-data-in-single-waveform-mode.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate data in one of two generation modes: Waveform Scripted Use the niHSDIO Configure Generation Mode VI or the niHSDIO_ConfigureGenerationMode function to switch between the two modes. The default mode is waveform.In waveform mode, call initiate to generate the waveform you specified by

### Generating Data in Single-Waveform Mode

- Waveform
- Scripted

niHSDIO_ConfigureGenerationMode

niHSDIO_ConfigureWaveformToGenerate

niHSDIO_ConfigureWaveformToGenerate

Tip

niHSDIO_ConfigureGenerationRepeat

Parent topic:

Generating Dynamic Data

Related concepts:

- Generating Multiple Waveforms with Linking & Looping
- Initiate and Fetch

<!--NI_TOPIC bundle=ni-hsdio path=generating-dynamic-data.html language=enus -->
## TOPIC 00062: Generating Dynamic Data

- bundle_id: `ni-hsdio`
- source_path: `generating-dynamic-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generating-dynamic-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you configure the generation and write your waveform(s) to the device, you can generate the data by calling an initiate VI or function. You can generate data one waveform at a time, or you can use scripts to generate complex sequences of waveforms. The following figure shows the flow of genera

### Generating Dynamic Data

After you configure the generation and write your waveform(s) to the device, you can generate the
 data by calling an initiate VI or function. You can generate
 data one waveform at a time, or you can use scripts to generate
 complex sequences of waveforms.

The following figure shows the flow of generating dynamic data:

[IMAGE alt='image' src='GUID-D62B1243-19C3-4D6B-8C89-0153F5E96297-a5.gif']

Parent topic:

Programming Flow

Related concepts:

- Initiate and Fetch
- Scripts

<!--NI_TOPIC bundle=ni-hsdio path=generating-multiple-waveforms-linking-looping.html language=enus -->
## TOPIC 00063: Generating Multiple Waveforms with Linking & Looping

- bundle_id: `ni-hsdio`
- source_path: `generating-multiple-waveforms-linking-looping.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generating-multiple-waveforms-linking-looping.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The scripted generation mode allows you to link and loop multiple waveforms in complex combinations. Use the niHSDIO Configure Generation Mode VI or the niHSDIO_ConfigureGenerationMode function to switch to scripted mode.Write all waveforms that are referenced in the script using a Write Named Wavef

### Generating Multiple Waveforms with Linking
 & Looping

The scripted generation mode allows you to link and loop multiple waveforms in complex
 combinations.

Use the niHSDIO Configure Generation Mode VI or the
 niHSDIO_ConfigureGenerationMode function to switch to scripted
 mode.

Write all waveforms that are referenced in the script using a Write Named Waveform call, and
 associate the proper names to them.

niHSDIO_WriteScript

niHSDIO_ConfigureScriptToGenerate

Note

Parent topic:

Generating Dynamic Data

Related concepts:

- Writing Waveforms to Your Device
- Initiate and Fetch
- Scripts

<!--NI_TOPIC bundle=ni-hsdio path=generating-waveforms-using-streaming.html language=enus -->
## TOPIC 00064: Generating Waveforms Using Streaming

- bundle_id: `ni-hsdio`
- source_path: `generating-waveforms-using-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generating-waveforms-using-streaming.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a method of generating waveforms that are too large to fit in the onboard memory of the device. Streaming can be used in dynamic generation sessions.To stream waveform data, you allocate and identify all or a portion of the device onboard memory to act as an onboard waveform for streami

### Generating Waveforms Using Streaming

Streaming is a method of generating waveforms that are too large to fit in the onboard memory of
 the device. Streaming can be used in dynamic generation sessions.

To stream waveform data, you allocate and identify all or a portion of the device onboard memory
 to act as an onboard waveform for streaming. Before initiating generation, you fill that
 onboard memory with the first part of your waveform. As the waveform is generated, space
 in the onboard memory becomes free and you fill that space with new waveform data. You
 repeat the process of filling the freed onboard memory in blocks of new waveform data
 until the waveform is complete.

The following instructions are a guide for configuring your application for streaming.

As an example, we have a 1.6 GB waveform we want to generate and a device with 256 MB of onboard
 memory. This 1.6 GB waveform might be in the host memory, on disk, or data that your
 application generates on-the-fly during generation.

[IMAGE alt='image' src='GUID-B24121FB-1288-4949-B3DD-36554461646D-a5.gif']

1. Specify the amount of onboard memory used for streaming. Use the niHSDIO Allocate
 Named Waveform VI or the function to specify the amount of onboard
 memory to reserve for streaming. This memory serves as a buffer for the
 streaming process. The niHSDIOAllocate Waveform VI function
 returns a waveform handle. 
 [IMAGE alt='image' src='GUID-A810E99A-C758-4197-8288-BC1801CCFA33-a5.gif']
2. Identify the streaming waveform. Set the Streaming Waveform Name property
 or the NIHSDIO_ATTR_STREAMING_WAVEFORM_NAME attribute to the
 waveform handle returned in Step 1. Setting this property ensures that no
 streaming data is overwritten before it is generated. NI-HSDIO monitors your
 progress to ensure that you write fresh data fast enough to keep up with the
 generation. If your application cannot write data fast enough, or attempts to
 write fresh data on top of data that has not been generated, NI-HSDIO returns an
 error. 
 [IMAGE alt='image' src='GUID-26AE589C-53C0-4287-83FA-0E37CD80B4E9-a5.gif']
3. Fill the streaming waveform with initial data. Call the niHSDIO Write Named Waveform
 VI or the one of the Write Named Waveform
 functions to write the first part of the waveform data to the streaming waveform
 in onboard memory. 
 Tip When transferring
 large waveform data blocks, divide the data into smaller segments. Use the
 niHSDIO Write Named Waveform VI or one of the Write
 Named Waveform functions multiple times. Each call appends data
 sequentially. Computers typically allocate smaller blocks faster than a single
 large contiguous block. For example, transferring ten 16 MB blocks may be faster
 than transferring one 160 MB block, depending on the available RAM. 
 [IMAGE alt='image' src='GUID-96084C98-63FD-416E-AD04-4FE6215095E3-a5.gif']
4. Begin generating the waveform. Call the niHSDIOInit Generation Session VIor the niHSDIO_InitGenerationSession function to
 begin the waveform generation. As the waveform generates, space in the streaming
 waveform becomes free. 
 [IMAGE alt='image' src='GUID-20562DE5-CDDA-453F-89EC-1DAAF72EE4E2-a5.gif']
5. As the waveform generates, monitor available memory. Use the Space Available in
 Streaming Waveform property or the
 NIHSDIO_ATTR_SPACE_AVAILABLE_IN_STREAMING_WAVEFORM
 attribute to determine how much of the onboard waveform is free for writing new
 data. As the waveform generates, space becomes available to write more waveform
 data. Once a certain amount of the onboard memory becomes available, you can
 write more of the waveform to the streaming waveform in onboard memory. In
 general, writing in larger blocks, such as 16 MB, results in more efficient
 streaming and faster streaming rates. 
 [IMAGE alt='image' src='GUID-6ABCE51A-5EBA-4BD8-8AA1-8FB25ED6632B-a5.gif']
6. Write a block of waveform data. Call the niHSDIO Write Named Waveform VI or
 the one of the Write Named Waveform functions to write a new
 block of waveform data to the streaming waveform in onboard memory. 
 [IMAGE alt='image' src='GUID-8176B297-823F-462C-8A71-ACF63381E9A7-a5.gif']
7. Repeat the process of monitoring the available memory and writing waveform data in blocks as free
 space becomes available. 
 [IMAGE alt='image' src='GUID-EE92BE44-DB1C-4DA7-A617-C15E01AF6074-a5.gif']

Tip

Continuous
 Generation - Stream From Memory VI. This VI

Dynamic Generation.llb

#### Improving Streaming Performance

To improve your maximum sustainable
 transfer rate for streaming, do the following:

- Adjust the Data Transfer Block Size property or the
 NIHSDIO_ATTR_DATA_TRANSFER_BLOCK_SIZE attribute to be
 closer to the waveform size. This change makes the data transfer more efficient
 and is accomplished in a single transfer instead of four transfers.
- When streaming from hard drives, consider the hard drive speed for maximum
 sustainable rates. Laptop hard drives typically have a data transfer rate of
 5 to 10 MB/s. Desktop hard drives typically meet or exceed 20 MB/s.
- Transfer rates from hard drives vary for different reasons. For example, where
 the data is physically stored on the hard drive and how much data is stored can
 affect transfer rates. Storing your waveform files on a dedicated and
 defragmented hard drive might increase performance.
- Consider using your hard drives in a RAID configuration. This allows for
 striping, which increases data transfer rates from the disk.
- When using an 18-slot PXI chassis, install the device that is used for streaming
 in slots 2 to 6 of the chassis.
- Utilize Direct DMA.

Parent topic:

Dynamic Generation

Related concepts:

- Writing Waveforms to Your Device
- Direct DMA

<!--NI_TOPIC bundle=ni-hsdio path=generation-configuration-functions.html language=enus -->
## TOPIC 00065: Generation Configuration Functions

- bundle_id: `ni-hsdio`
- source_path: `generation-configuration-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generation-configuration-functions.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW VIs C Functions niHSDIO Configure Sample Clock niHSDIO_ConfigureSampleClock niHSDIO Configure Generation Mode niHSDIO_ConfigureGenerationMode niHSDIO Configure Generation Repeat niHSDIO_ConfigureGenerationRepeat niHSDIO Configure Waveform to Generate niHSDIO_ConfigureWaveformToGenerate niHSD

### Generation Configuration Functions

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Configure Sample Clock | niHSDIO_ConfigureSampleClock |
| niHSDIO Configure Generation Mode | niHSDIO_ConfigureGenerationMode |
| niHSDIO Configure Generation Repeat | niHSDIO_ConfigureGenerationRepeat |
| niHSDIO Configure Waveform to Generate | niHSDIO_ConfigureWaveformToGenerate |
| niHSDIO Configure Script to Generate | niHSDIO_ConfigureScriptToGenerate |
| niHSDIO Configure Initial State(Polymorphic VI) | niHSDIO_ConfigureInitialState |
| niHSDIO Configure Initial State(Polymorphic VI) | niHSDIO_ConfigureInitialStateU32 |
| niHSDIO Configure Idle State(Polymorphic VI) | niHSDIO_ConfigureIdleState |
| niHSDIO Configure Idle State(Polymorphic VI) | niHSDIO_ConfigureIdleStateU32 |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureDataVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureDataVoltageCustomLevels |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureTriggerVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureTriggerVoltageCustomLevels |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureEventVoltageLogicFamily |
| niHSDIO Configure Voltage(Polymorphic VI) | niHSDIO_ConfigureEventVoltageCustomLevels |
| niHSDIO Configure Data Position | niHSDIO_ConfigureDataPosition |
| niHSDIO Configure Data Position Delay | niHSDIO_ConfigureDataPositionDelay |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalEdgeStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchStartTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureSoftwareStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisableStartTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalEdgeScriptTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalLevelScriptTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureSoftwareScriptTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisableScriptTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigureDigitalLevelPauseTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchPauseTrigger |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_ConfigurePatternMatchPauseTriggerU32 |
| niHSDIO Configure Trigger(Polymorphic VI) | niHSDIO_DisablePauseTrigger |
| niHSDIO Export Signal | niHSDIO_ExportSignal |
| niHSDIO Configure Ref Clock | niHSDIO_ConfigureRefClock |

Note

Using Attributes with NI-HSDIO

Advanced
 Attributes

Parent topic:

Configure the Hardware

Related concepts:

- Using Attributes with NI-HSDIO
- Advanced Attributes

<!--NI_TOPIC bundle=ni-hsdio path=generation-considerations-for-ddr.html language=enus -->
## TOPIC 00066: Generation Considerations for DDR

- bundle_id: `ni-hsdio`
- source_path: `generation-considerations-for-ddr.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generation-considerations-for-ddr.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: DDR generation has some additional considerations for your application. The following diagram shows how digital data is stored in generation onboard memory and how that impacts the trigger, event, and waveform quantum and the generated data: Data Width Data width is a function of your data rate mult

### Generation Considerations for DDR

DDR generation has some additional considerations for your application. The following diagram
 shows how digital data is stored in generation onboard memory and how that impacts the
 trigger, event, and waveform quantum and the generated data:

[IMAGE alt='image' src='GUID-0AEBEFC3-8728-4A82-9351-9BA686A04D96-a5.gif']

#### Data
 Width

Data width is a function of your data rate multiplier. Since data
 width refers to how large your sample is in bytes, using DDR mode effectively halves
 your allowable data width. For example, on a device with 16 channels, you can
 generate or acquire data on all 16 channels. For the same device in DDR mode, you
 can generate on only eight channels and acquire on the other eight.

#### Memory Usage

Memory usage is effectively doubled for each channel since
 the data width and channel count are halved.

#### Marker Positions

Marker positions have a quantization twice that of SDR
 mode. Refer to the *Specifications* for more information about
 quantization.

#### Waveform Sizes

The size of the waveforms you save to the onboard memory
 have a quantization twice that of SDR mode. Refer to the *Specifications*
 for more information about quantization.

#### Initial/Idle States

If a channel's Idle state is configured for "hold
 last value" (X), the last value held is the last DDR data sample.

Parent topic:

Double Data Rate (DDR)

Related concepts:

- Generation Onboard Memory
- Data Width
- Onboard Memory
- Events Summary
- Waveforms
- Initial and Idle States

<!--NI_TOPIC bundle=ni-hsdio path=generation-onboard-memory.html language=enus -->
## TOPIC 00067: Generation Onboard Memory

- bundle_id: `ni-hsdio`
- source_path: `generation-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generation-onboard-memory.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveforms and scripts are stored together in device memory. They are stored in contiguous blocks, appearing in memory in the order they were written to the device. You can delete individual waveforms from the device, freeing up the space they occupy for other waveforms to be written.Deleting wavefor

### Generation Onboard Memory

Waveforms and scripts are stored together in device memory. They are stored in contiguous blocks,
 appearing in memory in the order they were written to the device. You can delete
 individual waveforms from the device, freeing up the space they occupy for other
 waveforms to be written.

Deleting waveforms that are not at the end of the utilized space causes memory fragmentation. The
 following figure demonstrates how memory fragmentation can occur. First, assume four
 waveforms are currently in memory as shown in the following figure (sizes, in MS, are
 shown for clarity):

[IMAGE alt='image' src='GUID-63F60BA9-86C3-40D3-BB2F-4C33AC4F46DA-a5.gif']

In the previous figure, there is enough memory to write an additional 22 MS waveform to the
 device.

If Waveform C is deleted, that memory is freed, as shown in the following figure:

[IMAGE alt='image' src='GUID-2CC0D846-67DD-4735-9496-CAB8B9438871-a5.gif']

However, because waveforms are always stored contiguously in memory, the largest waveform that
 could be stored in memory is still 22 MS.

Waveform C last would have been advantageous because then deleting Waveform C would create a
 single block of free space, as shown in the following figure:

[IMAGE alt='image' src='GUID-2CFA4440-C10E-4CF3-9313-C9AEFDDF97F3-a5.gif']

[IMAGE alt='image' src='GUID-781233A2-0609-42EA-ADF5-801500E85B17-a5.gif']

In this situation, you can now write a 37 MS waveform to your device.

When you create a script for your dynamic generation operation, the scipt takes space in the
 memory. This is shown in the following figure:

[IMAGE alt='image' src='GUID-0DB0ABA7-9E2B-4328-BB46-2CE63A248999-a5.gif']

Note

Parent topic:

Onboard Memory

Related concepts:

- Initiate and Fetch

<!--NI_TOPIC bundle=ni-hsdio path=generation.html language=enus -->
## TOPIC 00068: Generation

- bundle_id: `ni-hsdio`
- source_path: `generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/generation.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains the concepts and terminology related to generation.

### Generation

This section explains the concepts and terminology related to generation.

Parent topic:

Digital Terminology

<!--NI_TOPIC bundle=ni-hsdio path=getting-started-with-ni-hsdio.html language=enus -->
## TOPIC 00069: Getting Started with NI-HSDIO

- bundle_id: `ni-hsdio`
- source_path: `getting-started-with-ni-hsdio.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/getting-started-with-ni-hsdio.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes how to begin using NI-HSDIO with your application development environment (ADE), lists any files to include in your application, and mentions special considerations to make with each ADE.To successfully build your application, install NI-HSDIO. You also must install one of the

### Getting Started with NI-HSDIO

This section describes how to begin using NI-HSDIO with your application development environment
 (ADE), lists any files to include in your application, and
 mentions special considerations to make with each ADE.

To successfully build your application, install NI-HSDIO. You also must install one of the
 following ADEs:

- LabVIEW
- LabWindows/CVI
- Microsoft Visual C++

Parent topic:

Programming

Related concepts:

- Using NI-HSDIO in LabVIEW
- Using NI-HSDIO in LabWindows/CVI
- Using NI-HSDIO in Visual C and C++

<!--NI_TOPIC bundle=ni-hsdio path=hardware-comparison-functions.html language=enus -->
## TOPIC 00070: Hardware Comparison Functions

- bundle_id: `ni-hsdio`
- source_path: `hardware-comparison-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/hardware-comparison-functions.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For hardware comparison, in addition to using the same VIs and functions as you normally would to configure your acquisition and generation sessions, you can also use the following VI and function to fetch the fault data. LabVIEW VI C Function niHSDIO HWC Fetch Sample Errors (U32) niHSDIO_HWC_FetchS

### Hardware Comparison Functions

For hardware comparison, in addition to using the same VIs and functions as you normally would to
 configure your *acquisition* and *generation* sessions, you can
 also use the following VI and function to fetch the fault data.

| LabVIEW VI | C Function |
| --- | --- |
| niHSDIO HWC Fetch Sample Errors (U32) | niHSDIO_HWC_FetchSampleErrors |

Note

Using Attributes with NI-HSDIO

Advanced
 Attributes

Parent topic:

Comparing Response Data with Expected Data

Related concepts:

- Acquisition Configuration Functions
- Generation Configuration Functions
- Using Attributes with NI-HSDIO
- Advanced Attributes

<!--NI_TOPIC bundle=ni-hsdio path=hardware-comparison.html language=enus -->
## TOPIC 00071: Hardware Comparison

- bundle_id: `ni-hsdio`
- source_path: `hardware-comparison.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/hardware-comparison.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hardware comparison allows a device to verify if a DUT generates the correct response data. This verification is in real-time and uses the full bandwidth of the device.Real-time hardware comparison is supported with only the NI 6547/6548/655x devices. Other digital waveform generators and analyzers

### Hardware Comparison

Note

There are two primary methods for comparing acquired response data with expected data.

The first method, the device captures the actual response data into PC memory and uses
 software to post-process the results. The software uses only the two basic logic states,
 0 and 1, to configure the tester’s stimulus data.

The second method, you can preload the device with both stimulus and expected response
 data and make real-time comparisons as data is acquired.

Whenever a waveform contains a comparison logic state (H or L), the acquired response
 data is compared to the expected response. You can choose whether this real-time
 hardware comparison operation drives and compares data (0, 1, Z, H, L, and X) or whether
 it only acquires and compares (H, L, and X).

Data comparison logic in the onboard FPGA connects the generation and acquisition circuitry. The
 data decoder receives data from onboard memory and enables/disables the driver based on
 the logic state of each sample. The decoder transfers the expected response to the
 acquisition engine. A FIFO allows the alignment of the actual response with the expected
 response.

If an error is detected during the comparison, then information on the fault is stored
 separately from the acquired data. The application software can retrieve both types of
 information for further analysis.

The device stores the following information for each fault detected:

- Sample number of the fault
- Channel(s) at fault
- Total number of repeated errors (useful if the Filter Repeated Sample Errors property or the
 NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS attribute is
 enabled)

Parent topic:

Digital Terminology

Related concepts:

- Digital Logic States
- Comparing Response Data with Expected Data

<!--NI_TOPIC bundle=ni-hsdio path=hysteresis.html language=enus -->
## TOPIC 00072: Hysteresis

- bundle_id: `ni-hsdio`
- source_path: `hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/hysteresis.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hysteresis refers to the difference in voltage levels between the detection of a transition from a logic low level to a logic high level and the transition from a logic high level to a logic low level. The following figure illustrates hysteresis for high and low logic levels: All digital logic devic

### Hysteresis

Hysteresis refers to the difference in voltage levels between the detection of a
 transition from a logic low level to a logic high level and the transition from a
 logic high level to a logic low level. The
 following figure illustrates hysteresis for high and low logic levels:

[IMAGE alt='image' src='GUID-1A19B2E1-D883-419A-9AF1-4612637EB50D-a5.gif']

All digital logic devices have some level of hysteresis on their digital inputs. The
 hysteresis magnitude for a particular device can be determined by the following
 formula:

Hysteresis ≈ V<sub>IH</sub> - V<sub>IL</sub>

On a rising edge of the digital signal on the input, the device detects a transition
 from a logic low to a logic high at
 *V<sub>IH</sub>*. Conversely, the device detects a transition from a
 logic high to a logic low when the voltage at the
 input of the device crosses *V<sub>IL</sub>*.

Hysteresis is a useful property for digital devices because it provides some amount of
 natural immunity to high-frequency noise in your digital system. This noise is generally
 caused by reflections from the high edge rates of logic level transitions.
 High-frequency noise might cause false transition detections by the digital device.
 These false detections occur when only a single voltage threshold determines a change in
 the logic state. The following figure illustrates this occurrence:

[IMAGE alt='image' src='GUID-89907A6A-0E44-4411-95DA-0A2ED09FD031-a5.gif']

After applying hysteresis the first sample is acquired as a logic low
 level. The second sample is also a logic lowlevel because the signal
 does not cross the logic high level threshold. The third and fourth
 samples are logic high level, and the fifth is logic
 low level.

For devices with fixed voltage thresholds, the NIM and hysteresis of your system are
 determined by your choice of system components. Some devices allow you to control both
 your system NIM and hysteresis. Both system NIM and hysteresis give your system levels
 of noise immunity.

For a specific logic family, increasing hysteresis reduces the NIM and decreasing
 hysteresis increases it.

To set voltage thresholds appropriately, carefully examine the signal quality in your
 system:

- If your system requires greater noise immunity for valid logic levels, aim for a
 higher NIM.
- If your system needs more noise immunity during logic level transitions, prioritize
 greater hysteresis.

<!--NI_TOPIC bundle=ni-hsdio path=initial-and-idle-states.html language=enus -->
## TOPIC 00073: Initial and Idle States

- bundle_id: `ni-hsdio`
- source_path: `initial-and-idle-states.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/initial-and-idle-states.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The initial state configures the state of the data generation channels after a session is configured but before the device starts generating the waveform. The initial state is often useful while the device is waiting for a Start trigger.The initial state is not the same as the channel power-up state

### Initial and Idle States

Note

Device Specifications

The idle state configures the state of the data generation channels after the waveform
 generation has begun and the generation has paused or stopped.

You can choose between initial state and idle state for each channel. You can select the
 following values on all digital waveform generator/analyzers for data generation
 channels:

- 1 —Drive the channel to a high level.
- 0 —Drive the channel to a low level.
- X —Hold last value/Leave the channel at its current state.
- Z —(PXI 654x/655x only) Put the channel in a high-impedance state.

Note

X

Parent topic:

Dynamic Generation

Related concepts:

- Double Data Rate (DDR)
- Configuring Initial and Idle States
- Generation Considerations for DDR

<!--NI_TOPIC bundle=ni-hsdio path=initialize-your-session.html language=enus -->
## TOPIC 00074: Initialize Your Session

- bundle_id: `ni-hsdio`
- source_path: `initialize-your-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/initialize-your-session.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For any application you write, open a session to establish communication with the instrument by using one of the following two VIs or functions: LabVIEW VIs C Functions niHSDIO Init Acquisition Session niHSDIO_InitAcquisitionSession niHSDIO Init Generation Session niHSDIO_InitGenerationSession niHSD

### Initialize Your Session

For any application you write, open a session to establish communication with the instrument by
 using one of the following two VIs or functions:

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Init Acquisition Session | niHSDIO_InitAcquisitionSession |
| niHSDIO Init Generation Session | niHSDIO_InitGenerationSession |
| niHSDIO Init Ext Cal | niHSDIO_InitExtCal |

Tip

niHSDIO_Initiate

In addition to establishing a session with the device, these VIs and functions also send
 initialization commands to set the device to the state necessary for the instrument driver.
 These two functions can perform a number of additional tasks, such as verifying that the
 instrument driver is valid for the device and resetting the device to a known state.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-hsdio path=initiate-and-fetch.html language=enus -->
## TOPIC 00075: Initiate and Fetch

- bundle_id: `ni-hsdio`
- source_path: `initiate-and-fetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/initiate-and-fetch.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Initiate and Fetch VIs and functions to perform other operations while the device acquires data. Initiate begins the acquisition operation and returns control to your program. Fetch transfers the acquired data from acquisition onboard memory to your application. The Initiate and Fetch VIs/fu

### Initiate and Fetch

Use the Initiate and Fetch VIs and functions to perform other operations while the device
 acquires data. Initiate begins the acquisition operation and returns control to your
 program. Fetch transfers the acquired data from acquisition onboard memory to your
 application.

The Initiate and Fetch VIs/functions are shown in the following table:

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Initiate | niHSDIO_Initiate |
| Use one of the following instances of the niHSDIO Fetch Waveform polymorphic VI: niHSDIO Fetch Waveform (U32) niHSDIO Fetch Waveform (U16) niHSDIO Fetch Waveform (U8) niHSDIO Fetch Waveform (WDT) niHSDIO Fetch Multi Record (2D U32) niHSDIO Fetch Multi Record (2D U16) niHSDIO Fetch Multi Record (2D U8) niHSDIO Fetch Multi Record (1D WDT) | niHSDIO_FetchWaveformU32 niHSDIO_FetchWaveformU16 niHSDIO_FetchWaveformU8 niHSDIO_FetchMultiRecordU32 niHSDIO_FetchMultiRecordU16 niHSDIO_FetchMultiRecordU8 |

Note

timeout

niHSDIO_Abort

Tip

NIHSDIO_ATTR_FETCH_BACKLOG

Note

Parent topic:

Acquiring Dynamic Data

Related concepts:

- Acquisition Onboard Memory
- Read

<!--NI_TOPIC bundle=ni-hsdio path=integration-and-system-considerations.html language=enus -->
## TOPIC 00076: Integration and System Considerations

- bundle_id: `ni-hsdio`
- source_path: `integration-and-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/integration-and-system-considerations.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains system considerations and hardware integration.

### Integration and System Considerations

This section explains system considerations and hardware integration.

<!--NI_TOPIC bundle=ni-hsdio path=level-trigger.html language=enus -->
## TOPIC 00077: Level Trigger

- bundle_id: `ni-hsdio`
- source_path: `level-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/level-trigger.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure certain triggers to act when a signal goes below the defined low level or above the defined high level. Triggers configured to act in this way are known as level triggers. Not all triggers can be configured to be level triggers. Refer to Triggers Summary for information about which

### Level Trigger

You can configure certain triggers to act when a signal goes below the defined low level or above
 the defined high level. Triggers configured to act in this way are known as level
 triggers. Not all triggers can be configured to be level triggers. Refer to
 *Triggers Summary* for information about which triggers you can configure
 for level triggering.

Parent topic:

Types of Triggers

Related concepts:

- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio path=logic-families.html language=enus -->
## TOPIC 00078: Logic Families

- bundle_id: `ni-hsdio`
- source_path: `logic-families.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/logic-families.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Logic families are groups of logic circuits with standardized voltage levels that constitute a valid logic state. All circuits within a logic family are compatible with other circuits within that family, because they share the same characteristics. Logic families are defined by the following charact

### Logic Families

Logic families are groups of logic circuits with standardized voltage levels that
 constitute a valid logic state. All circuits within a logic family are compatible with
 other circuits within that family, because they share the same characteristics.

Logic families are defined by the following characteristics:

- Single-ended voltage levels, such as the following logic families:
  - 1.2 V
  - 1.5 V
  - 1.8 V
  - 2.5 V
  - 3.3 V
  - 5.0 V
- Differential voltage levels, such as the following:
  - Low-voltage emitter-coupled logic (LVPECL)
  - Low-voltage differential signaling (LVDS)

Refer to *Configuring Voltage Levels* for more information about using
 NI-HSDIO to select logic families and configure your voltage levels.

Note

Parent topic:

Digital Logic

Related concepts:

- Voltage Levels
- Single-Ended Voltage Levels
- Differential Voltage Levels
- Configuring Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=making-multirecord-acquisitions.html language=enus -->
## TOPIC 00079: Making Multirecord Acquisitions

- bundle_id: `ni-hsdio`
- source_path: `making-multirecord-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/making-multirecord-acquisitions.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-HSDIO supports multirecord acquisitions, which allow you to capture multiple, triggered waveforms without software intervention. NI-HSDIO stores each record in separate memory locations on the device.The main benefit of multirecord acquisitions is that you can quickly acquire numerous triggered w

### Making Multirecord Acquisitions

NI-HSDIO supports multirecord acquisitions, which allow you to capture multiple, triggered
 waveforms without software intervention. NI-HSDIO stores each record in separate memory
 locations on the device.

The main benefit of multirecord acquisitions is that you can quickly acquire numerous triggered
 waveforms. Multirecord acquisitions allow hardware rearming of the device before the
 data is fetched. Therefore, the rearm time, or the time when the device is not ready for
 a trigger, is extremely small, often from 1 to 100 µs, depending on the record length
 and the device. This short rearm time allows you to capture data whether the triggers
 occur microseconds or many days apart.

#### Fetching Multirecord Acquisitions

You use the same fetch VIs and
 functions for retrieving multirecord acquisitions as you do for single-record
 acquisitions. However, you must also specify the starting record and the number of
 records to fetch.

Fetching multiple records with a single fetch VI or function
 requires understanding the order of the returned waveforms. If you are using a
 C-based language, the waveforms are packed into a one-dimensional array. For LabVIEW
 users, the waveforms are returned as a two-dimensional array (where rows represent
 records and columns represent samples). You can use the Index Array VI to extract
 the waveform of interest.

You can also fetch each record individually using
 the following procedure:

1. Set the number of records to fetch to 1.
2. Use a loop to set the starting record as the zero-based index of the record you
 want to fetch.
3. Call one of the fetch VIs or functions.

Parent topic:

Acquiring Dynamic Data

Related concepts:

- Records
- Initiate and Fetch

<!--NI_TOPIC bundle=ni-hsdio path=mxi-3-optimization-application.html language=enus -->
## TOPIC 00080: MXI-3 Optimization Application

- bundle_id: `ni-hsdio`
- source_path: `mxi-3-optimization-application.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/mxi-3-optimization-application.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using the MXI-3 interface to control the PXI chassis, the MXI-3 Optimization Application must be run prior to using the signal generator. By default, this application runs automatically when Windows starts. If you experience an initialization, timeout, or performance issue with your modul

### MXI-3 Optimization Application

If you are using the MXI-3 interface to control the PXI chassis, the MXI-3 Optimization
 Application must be run prior to using the signal generator. By default, this
 application runs automatically when Windows starts.

If you experience an initialization, timeout, or performance issue with your module, or
 if you're unsure whether the application ran:

- Select Start » All Programs » National Instruments MXI-3 » MXI-3
 Optimization to run the application

If the issue persists:

- Refer to the MXI-3 documentation located at Start » All Programs »
 National Instruments MXI-3
- Or visit Technical Support at ni.com/support

#### MXI-4 and MXI-Express Optimization

Optimization for MXI-4 and MXI Express are performed automatically by the hardware.

Parent topic:

PXI/PXI Express

<!--NI_TOPIC bundle=ni-hsdio path=ni-654x-acquisition-termination.html language=enus -->
## TOPIC 00081: NI 654x Acquisition Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-654x-acquisition-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-654x-acquisition-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: High-Impedance Load Acquisition ConfigurationFor acquisition operations, the NI 654x can only be used in a high-impedance load configuration because the input impedance of the NI 654x is set to 10 kΩ. The high-impedance load configuration is easy to drive since it does not present a significant DC l

### NI 654x Acquisition Termination

#### High-Impedance Load Acquisition Configuration

For
 acquisition operations, the NI 654x can only be used in a
 high-impedance load configuration because the input impedance of the
 NI 654x is set to 10 kΩ. The high-impedance load configuration is
 easy to drive since it does not present a significant DC load to the
 source and preserves the signal amplitude. To achieve the highest
 level of AC signal quality, you must follow the recommendations in
 this section.

The same transmission line considerations
 discussed for the generation case are applicable to acquired
 signals. The input impedance of 10 kΩ implies a reflection
 coefficient Γ<sub>t</sub> of 0.99, or nearly full
 reflection.

With all high-impedance load transmission lines,
 it is essential that you take care to match the source impedance of
 the transmission line to the characteristic impedance of the
 transmission line. The source matching in this configuration is
 particularly important, since there are significant reflections from
 the high-impedance load, in this caseinput of NI 654x.

You
 must ensure that your transmission line has a characteristic
 impedance of as close to 50 Ω as possible.

Z<sub>s</sub>
 (external source output impedance) should match Z<sub>0</sub> = 50 Ω
 (the cable impedance) for 10 kΩ input configuration.

To
 achieve this Z<sub>s</sub> = 50 Ω, determine the output impedance of
 your digital driver. Add a series resistor as close as possible to
 the driver pin.

Ensure that the output impedance of your
 buffer plus the value of the series resistor equal 50 Ω.

If
 you require 50 Ω termination for your acquisition application,
 consider using one of the NI 655x products.

Parent topic:

Terminating Your NI 654x

Related concepts:

- NI 654x Generation Termination
- Characteristic Impedance

<!--NI_TOPIC bundle=ni-hsdio path=ni-654x-generation-termination.html language=enus -->
## TOPIC 00082: NI 654x Generation Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-654x-generation-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-654x-generation-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generation Termination: High-Impedance Load ConfigurationA common NI 654x configuration is to connect the output terminals of your device directly to your device under test (DUT). Most digital logic inputs have an input impedance of at least 1–10 KΩ. Connecting the NI 654x output terminals directly

### NI 654x Generation Termination

#### Generation Termination: High-Impedance Load Configuration

A common
 NI 654x configuration is to connect the output terminals of your device directly to
 your device under test (DUT). Most digital logic inputs have an input impedance of
 at least 1–10 KΩ. Connecting the NI 654x output terminals directly to the input of
 your DUT creates a source-terminated configuration, because the generation channels
 of the NI 654x have a 50 Ω source impedance.

While this source termination
 configuration does not provide the absolute highest level of signal quality, there
 are many advantages:

1. You can achieve good signal levels are possible if you ensure that you have the
 cleanest possible 50 Ω characteristic impedance transmission line.
2. The source-terminated configuration allows you to directly wire to your DUT
 without the need for additional termination resistors.
3. At DC there is effectively a voltage divider between the 50 Ω Z s 
 resistance and the high-impedance Z t of your DUT, having an
 source-terminated system preserves the largest possible voltage swings at the
 DUT according to the following formula:

V<sub>DUT</sub> = V<sub>source</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> +
 Z<sub>t</sub>))

For a DUT with an input impedance of 1 kΩ, programming a
 generation *voltage level* of 3.3 V at the NI 654x source produces a
 3.3 V × (1000/1050) = 3.14 V swing at the DUT.

A source-terminated
 configuration results in reflections in the transmission line. These reflections are
 absorbed at the source and not re-reflected back to the load, preserving the signal
 integrity. The source impedance does not perfectly match the transmission line
 impedance. A small fraction of the reflected wave is re-reflected back toward the
 load. This second reflection creates small signal aberrations and a low level of
 inter-symbol interference.

For example, a 5% mismatch at the source results in
 a 2.5% re-reflection back at the load:

Γ<sub>s</sub> = (1.05 - 1)/(1.05 + 1) ≈
 2.5%

#### Generation Termination: Terminated Load Configuration

The
 source-terminated load configuration is easy to use with a terminated source, such
 as the NI 654x, and is recommended for all applications except the most demanding in
 regard to timing precision or signal integrity. For applications demanding the
 highest levels of signal quality and timing precision, it is recommended to follow
 the recommendations of the terminated load configuration.

For applications
 requiring the highest levels of signal integrity and timing accuracy, it is
 recommended that you control the termination impedance at the end of the
 transmission line. To control the termination impedance, add a parallel termination
 resistor to ground as close as possible to the digital input pin of the device under
 test (DUT). In this configuration, the transmission line is terminated at both ends,
 which produces the highest possible signal integrity.

The source impedance,
 Z<sub>S</sub>, and the characteristic impedance of the transmission line,
 Z<sub>0</sub>, should be kept as close as possible to 50 Ω as this gives you the
 best possible signal quality.

Depending on your device, having all the lines
 terminated into 50 Ω might violate the maximum current specifications. Refer to the
 *Specifications* document of your device for more information about
 the maximum current to determine how many lines you can simultaneously terminate
 into 50 Ω.

While a *Z<sub>t</sub>* of 50 Ω is ideal, you can also
 use values as high as 300 Ω without significantly affecting signal quality. Using
 this higher resistance value allows you to increase the voltage swing across the DUT
 and decrease the drive current requirements on your NI 654x.

At DC there is
 effectively a voltage divider between the 50 Ω Z<sub>S</sub> resistance and the
 termination resistance, having a terminated load reduces the largest possible
 voltage swings at the DUT according to the following
 formula:

V<sub>DUT</sub> = V<sub>source</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> + Z<sub>t</sub>))

For
 a 50 Ω termination, programming a generation voltage level of 3.3 V at the NI 654x
 source produces a 3.3 V x (50/100), or 1.65 V swing at the DUT. This reduced voltage
 swing at the DUT should be considered when you create your system.

Depending
 on voltage swing requirements, you have several generation termination options. The
 following table lists some of the options for the different voltage swings:

Tip

| Required Voltage Swing at DUT | Termination Options |
| --- | --- |
| 3.3 V | Generation voltage family = 3.3 V Logic, no termination resistance |
| 2.5 V | Generation voltage family = 2.5 V Logic, no termination resistance Generation voltage family = 3.3 V Logic, Zt = 156 Ω (Imax = 16 mA) |
| 1.8 V | Generation voltage family = 1.8 V Logic, no termination resistance Generation voltage family = 3.3 V Logic, Zt = 60 Ω (Imax = 30 mA) Generation voltage family = 2.5 V Logic, Zt = 129 Ω (Imax = 14 mA) |

Parent topic:

Terminating Your NI 654x

Related concepts:

- Characteristic Impedance
- Voltage Levels
- Transmission Lines

<!--NI_TOPIC bundle=ni-hsdio path=ni-654x-termination-summary.html language=enus -->
## TOPIC 00083: NI 654x Termination Summary

- bundle_id: `ni-hsdio`
- source_path: `ni-654x-termination-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-654x-termination-summary.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following illustration provides a high-level summary of the termination considerations for your NI 654x:Generation Termination Source Transmission Line Termination (Load) Z[s] = 50 Ω Z[o] = 50 Ω Z[t] = Open (Tristate) or Unterminated Works for all except the most demanding applications. Z[s] = 5

### NI 654x Termination Summary

The following illustration provides a high-level summary of the termination considerations for
 your NI 654x:

#### *Generation
 Termination*

[IMAGE alt='image' src='GUID-C86F69C1-30B1-41A5-BDBC-9BA3E98FDDFE-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zs = 50 Ω | Zo = 50 Ω | Zt = Open (Tristate) or Unterminated Works for all except the most demanding applications. |
| Zs = 50 Ω | Zo = 50 Ω | Zt = 50Ω–300 Ω Recommended for better signal integrity. |

#### *Acquisition Termination*

[IMAGE alt='image' src='GUID-20878CB1-3C2A-4A03-AB8D-A5B894B34C2D-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zt = 10 kΩ | 50 Ω | Zs = 50 Ω This is the recommended configuration for most applications. |
| Zt = 10 kΩ | 50 Ω | Zs < 50 Ω This configuration is not recommended because of the mismatch on both ends. The recommended setup is to increase Zs to 50 Ω by adding series resistance at the source. |
| Zt = 10 kΩ | 50 Ω | Zs > 50 Ω This configuration is not recommended because of the mismatch on both ends.Note You must reduce the operating frequency significantly to allow the signal reflections to settle down. You must reduce the frequency proportional to cable length and impedance mismatch. |

Parent topic:

Terminating Your NI 654x

Related concepts:

- NI 654x Generation Termination
- NI 654x Acquisition Termination

<!--NI_TOPIC bundle=ni-hsdio path=ni-6551-6552-acquisition-termination.html language=enus -->
## TOPIC 00084: NI 6551/6552 Acquisition Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-6551-6552-acquisition-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6551-6552-acquisition-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Unterminated Acquisition ConfigurationFor acquisition operations, an unterminated configuration essentially implies that you set the input impedance of the device to 10 kΩ using NI-HSDIO. The unterminated configuration is easy to drive since it does not present a significant DC load to the source an

### NI 6551/6552 Acquisition Termination

#### Unterminated Acquisition Configuration

For acquisition
 operations, an unterminated configuration essentially implies that
 you set the input impedance of the device to 10 kΩ using NI-HSDIO.
 The unterminated configuration is easy to drive since it does not
 present a significant DC load to the source and preserves the signal
 amplitude. As a result, this is the recommended configuration for
 most applications. When you use this mode. To achieve the highest
 level of AC signal quality, you must follow the recommendations in
 this section.

The same transmission line considerations
 discussed for the generation case are applicable to acquired
 signals. Programming an input impedance of 10 kΩ implies a
 reflection coefficient Γ<sub>t</sub> of 0.99, or nearly full
 reflection and is effectively an unterminated input.

With all
 unterminated transmission lines, you must ensure that match the
 source impedance of the transmission line to the characteristic
 impedance of the transmission line. The source matching in this
 configuration is important, since there are significant reflections
 from the unterminated load (input of NI 6551/6552 in the
 case).

You must ensure that your transmission line has a
 characteristic impedance of as close to 50 Ω as
 possible.

Z<sub>s</sub> (external source output
 impedance) should match Z<sub>0</sub> = 50 Ω (the cable impedance)
 for 10 kΩ input configuration.

To achieve this Z<sub>s</sub>
 = 50 Ω, you must determine the output impedance of your digital
 driver. Add a series resistor as close as possible to the driver
 pin.

Ensure that the output impedance of your buffer plus the
 value of the series resistor equal 50 Ω.

A 10 kΩ input
 configuration is not recommended for use with drivers that are not
 matched to the cable impedance at 50 Ω.

#### Terminated Acquisition Configuration

Input termination of
 50 Ω is recommended for best signal integrity since there are no
 reflections back to the signal source, provided that the signal
 source can drive this load.

The 50 Ω input configuration
 reduces the signal swing seen by the NI 6551/6552 input comparators
 by half, assuming the signal source is 50 Ω. You must consider this
 amplitude reduction when configuring the input thresholds.

For
 example, a 50 Ω source with a 0 to 5 V step generation (into
 high-impedance) is seen as a 0 to 2.5 step source at the
 NI 6551/6552 acquisition comparators when you configure the
 NI 6551/6552 for 50 Ω input impedance.

Parent topic:

Terminating Your NI 6551/6552

Related concepts:

- NI 6551/6552 Generation Termination
- Characteristic Impedance

<!--NI_TOPIC bundle=ni-hsdio path=ni-6551-6552-generation-termination.html language=enus -->
## TOPIC 00085: NI 6551/6552 Generation Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-6551-6552-generation-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6551-6552-generation-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generation Termination: Unterminated Load ConfigurationA common NI 6551/6552 configuration is to connect the output terminals of your device directly to your device under test (DUT). Most digital logic inputs have an input impedance of 1–10 KΩ. Since your NI 6551/6552 is designed to be used in a 50

### NI 6551/6552 Generation Termination

#### Generation Termination: Unterminated Load Configuration

A common
 NI 6551/6552 configuration is to connect the output terminals of your device
 directly to your device under test (DUT). Most digital logic inputs have an input
 impedance of 1–10 KΩ. Since your NI 6551/6552 is designed to be used in a 50 Ω
 environment, connecting the device output terminals directly to the input of your
 DUT effectively creates an unterminated load configuration.

While an
 unterminated configuration does not offer the highest possible signal quality, it
 has many advantages:

1. You can achieve good signal levels if you ensure a clean 50 Ω characteristic
 impedance transmission line.
2. The unterminated configuration allows direct wiring to the DUT without the need
 for additional termination resistors.
3. At DC there is effectively a voltage divider between the 50 Ω Z s 
 resistance and the high-impedance Z t of your DUT. In an unterminated
 load preserves the largest possible voltage swings at the DUT according to the
 following formula:

V<sub>t</sub> = V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> +
 Z<sub>t</sub>))

For a DUT with an input impedance of 1 kΩ, programming a
 generation voltage level of 3.3 V at the NI 655x source produces a 3.3 V ×
 (1000/1050) = 3.14 V swing.

The unterminated load generates reflections in the
 transmission line. The load reflections are absorbed at the source and not
 re-reflected back to the load, preserving the signal integrity. The source impedance
 does not perfectly match the transmission line impedance. A small fraction of the
 reflected wave is re-reflected back toward the load. This second reflection creates
 small signal aberrations and a low level of inter-symbol interference.

For
 example, a 5% mismatch at the source results in a 2.5% re-reflection back at the
 load:

Γ<sub>s</sub> = (1.05 - 1)/(1.05 + 1) ≈ 2.5%

#### Generation Termination: Terminated Load Configuration

The unterminated
 load configuration is easy to use with a terminated source, such as the
 NI 6551/6552, and is recommended for all applications except the most demanding in
 regard to timing precision or signal integrity. For applications requiring the
 highest levels of signal quality and timing precision, it is important to follow the
 recommendations of the terminated load configuration.

For applications
 requiring the highest levels of signal integrity and timing accuracy, it is
 recommended that you control the termination impedance at the end of the
 transmission line. To control the termination impedance, add a parallel termination
 resistor to ground as close as possible to the digital input pin of the device under
 test (DUT). In this configuration, the transmission line is terminated at both ends
 of the transmission line, which produces the highest possible signal
 integrity.

The source impedance, Z<sub>S</sub>, and the characteristic
 impedance of the transmission line, Z<sub>0</sub>, must be kept as close as possible
 to 50 Ω as this gives you the best possible signal quality.

Depending on your
 device, having all the lines terminated into 50 Ω might violate the maximum current
 specifications for your device. To determine how many lines you can simultaneously
 terminate into 50 Ω, refer to the *Specifications* document for your
 device. It provides information about the maximum allowable current for your
 specific model.

While a Z<sub>t</sub> of 50 Ω is ideal, you can also use
 values as high as 150 Ω without significantly affecting signal quality. Using this
 higher resistance value allows you to increase the voltage swing across the DUT and
 decrease the drive current requirements on your NI 6551/6552.

At DC there is
 effectively a voltage divider between the 50 Ω Z<sub>S</sub> resistance and the
 termination resistance, having a terminated load reduces the largest possible
 voltage swings at the DUT according to the following formula:

V<sub>t</sub> =
 V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> + Z<sub>t</sub>))

For a 50 Ω
 termination, programming a generation voltage level of 3.3 V at the NI 6551/6552
 source produces a 3.3 V x (50/100) = 1.65 V swing. This reduced voltage swing at the
 DUT must be considered when you create your system.

Parent topic:

Terminating Your NI 6551/6552

Related concepts:

- Characteristic Impedance
- Voltage Levels
- Transmission Lines

<!--NI_TOPIC bundle=ni-hsdio path=ni-6551-6552-termination-summary.html language=enus -->
## TOPIC 00086: NI 6551/6552 Termination Summary

- bundle_id: `ni-hsdio`
- source_path: `ni-6551-6552-termination-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6551-6552-termination-summary.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following illustration provides a high-level summary of the termination considerations for your NI 6551/6552.Generation Termination Source Transmission Line Termination (Load) Z[s] = 50 Ω Z[o] = 50 Ω Z[t] = Open (Tristate) or Unterminated Works for all except the most demanding applications. Z[s

### NI 6551/6552 Termination Summary

The following illustration provides a high-level summary of the termination
 considerations for your NI 6551/6552.

#### *Generation
 Termination*

[IMAGE alt='image' src='GUID-C86F69C1-30B1-41A5-BDBC-9BA3E98FDDFE-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zs = 50 Ω | Zo = 50 Ω | Zt = Open (Tristate) or Unterminated Works for all except the most demanding applications. |
| Zs = 50 Ω | Zo = 50 Ω | Zt = 50Ω–150 Ω Recommended for better signal integrity. |

#### *Acquisition Termination*

[IMAGE alt='image' src='GUID-20878CB1-3C2A-4A03-AB8D-A5B894B34C2D-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zt = 10 kΩ | 50 Ω | Zs = 50 Ω This is the recommended configuration for most applications. |
| Zt = 10 kΩ | 50 Ω | Zs < 50 Ω This configuration is not recommended because of the mismatch on both ends. The recommended setup is to increase Zs to 50 Ω by adding series resistance at the source. |
| Zt = 10 kΩ | 50 Ω | Zs > 50 ΩThis configuration is not recommended because of the mismatch on both ends.Note You must reduce the operating frequency significantly to allow the signal reflections to settle down. You must reduce the frequency proportional to cable length and impedance mismatch. |
| Zt = 50 Ω | 50 Ω | Zs = 50 Ω This configuration is recommended for best signal integrity. Vi = Vo/2 Source must be able to drive 50 Ω. |
| Zt = 50 Ω | 50 Ω | Zs < 50 Ω Source-side mismatch degrades signal integrity, but this configuration is still usable in many applications. Vi = 50/(50 + Zs) × Vo |
| Zt = 50 Ω | 50 Ω | Zs > 50 Ω Source-side mismatch degrades signal integrity, but this configuration is still usable in many applications. Vi = 50/(50 + Zs) × Vo |

Parent topic:

Terminating Your NI 6551/6552

Related concepts:

- NI 6551/6552 Generation Termination
- NI 6551/6552 Acquisition Termination

<!--NI_TOPIC bundle=ni-hsdio path=ni-6555-6556-acquisition-termination.html language=enus -->
## TOPIC 00087: NI 6555/6556 Acquisition Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-6555-6556-acquisition-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6555-6556-acquisition-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: High-Impedance Acquisition ConfigurationFor acquisition operations, a high-impedance input implies minimal amounts of leakage. Refer to the Specifications document for your device to determine the leakage levels. The unterminated configuration is easy to drive since it does not present a significant

### NI 6555/6556 Acquisition Termination

#### High-Impedance Acquisition Configuration

For acquisition operations, a
 high-impedance input implies minimal amounts of leakage. Refer to the
 *Specifications* document for your device to determine the leakage
 levels. The unterminated configuration is easy to drive since it does not present a
 significant DC load to the source and preserves the signal amplitude. As a result,
 this is the recommended configuration for most applications. To achieve the highest
 level of AC signal quality, you must follow the recommendations in this
 section.

The same transmission line considerations discussed for the
 generation case are applicable to acquired signals. With all unterminated
 transmission lines, it is essential that you match the source impedance of the
 transmission line to the characteristic impedance of the transmission line. The
 source matching in this configuration is particularly important, since there are
 significant reflections from the unterminated load (input of NI 6555/6556 in the
 case).

You must ensure that your transmission line has a characteristic
 impedance of as close to 50 Ω as possible.

Z<sub>s</sub> (external source
 output impedance) should match Z<sub>0</sub> = 50 Ω (the cable impedance) for a high
 impedance input configuration.

To achieve this Z<sub>s</sub> = 50 Ω, you must
 determine the output impedance of your digital driver. Add a series resistor as
 close as possible to the driver pin such that the output impedance of your buffer
 plus the value of the series resistor equal 50 Ω.

A high impedance input
 configuration is not recommended for use with drivers that are not matched to the
 cable impedance at 50 Ω.

#### Terminated Acquisition Configuration

Input termination of 50 Ω, with
 *V<sub>TT</sub>*, is recommended for the best signal integrity
 since there are no reflections back to the signal source, provided that the signal
 source can drive this load.

You must set the Tristate Mode or Termination Mode
 property to Drive termination voltage or the
 NIHSDIO_ATTR_DATA_TRISTATE_MODE or
 NIHSDIO_ATTR_DATA_TERMINATION_MODE attribute to
 NIHSDIO_VAL_DRIVE_TERMINATION_VOLTAGE in this
 configuration.

The 50 Ω input configuration reduces the signal swing seen by
 the NI 6555/6556 input comparators by half, assuming the signal source is 50 Ω. You
 must consider this amplitude reduction when configuring the input thresholds. For
 example, a 50 Ω source with a 0 V to 5 V step generation (into high-impedance) is
 seen as a 0 to 2.5 step source at the NI 6555/6556 acquisition comparators when you
 configure the NI 6555/6556 for 50 Ω input impedance.

For more information
 about tristate and termination voltage, refer to the *Tristate
 Functionality* topic.

Parent topic:

Terminating Your NI 6555/6556

Related concepts:

- NI 6555/6556 Generation Termination
- Characteristic Impedance

Related information:

- Voltage Ranges and Settings 72
- Tristate Functionality

<!--NI_TOPIC bundle=ni-hsdio path=ni-6555-6556-generation-termination.html language=enus -->
## TOPIC 00088: NI 6555/6556 Generation Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-6555-6556-generation-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6555-6556-generation-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generation Termination: High-Impedance Load ConfigurationA common NI 6555/6556 configuration is to connect the output terminals of your device directly to your device under test (DUT). Most digital logic inputs have an input impedance of greater than 10 kΩ. Since your NI 6555/6556 is designed to be

### NI 6555/6556 Generation Termination

#### Generation Termination: High-Impedance Load Configuration

A common
 NI 6555/6556 configuration is to connect the output terminals of your device
 directly to your device under test (DUT). Most digital logic inputs have an input
 impedance of greater than 10 kΩ. Since your NI 6555/6556 is designed to be used in a
 50 Ω environment, connecting the device output terminals directly to the input of
 your DUT effectively creates an unterminated load configuration.

While this
 unterminated configuration does not provide the absolute highest level of signal
 quality, it has many advantages:

1. You can achieve good signal levels are possible if you ensure that you have the
 cleanest possible 50 Ω characteristic impedance transmission line.
2. The unterminated configuration allows you to directly wire to your DUT without
 the need for additional termination resistors.
3. At DC there is effectively a voltage divider between the 50 Ω Z s 
 resistance and the high-impedance Z t of your DUT, having an
 unterminated load preserves the largest possible voltage swings at the DUT
 according to the following formula:

V<sub>t</sub> = V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> +
 Z<sub>t</sub>))

Therefore, for a DUT with an input impedance of 1 kΩ,
 programming a *generation voltage level* of 3.3 V at the NI 655x source
 produces a 3.3 V × (1000/1050) = 3.14 V swing.

The unterminated load generates
 reflections in the transmission line. The load reflections are absorbed at the
 source and not re-reflected back to the load preserving the signal integrity. The
 source impedance does not perfectly match the transmission line impedance. A small
 fraction of the reflected wave is re-reflected back toward the load. This second
 reflection creates small signal aberrations and a low level of inter-symbol
 interference.

For example, a 5% mismatch at the source results in a 2.5%
 re-reflection back at the load:

Γ<sub>s</sub> = (1.05 - 1)/(1.05 + 1) ≈ 2.5%

#### Generation Termination: Terminated Load Configuration

The
 source-terminated load configuration is easy to use with a terminated source, such
 as the NI 6555/6556, and is recommended for all applications except the most
 demanding in regard to timing precision or signal integrity. For applications
 demanding the highest levels of signal quality and timing precision, it is
 recommended to follow the recommendations of the terminated load
 configuration.

For applications that require the highest levels of signal
 integrity and timing accuracy, it is recommended that you control the termination
 impedance at the end of the transmission line. To control the termination impedance,
 add a parallel termination resistor to ground as close as possible to the digital
 input pin of the device under test (DUT). In this configuration, the transmission
 line is terminated at both ends of the transmission line, which produces the highest
 possible signal integrity.

The source impedance, Z<sub>S</sub>, and the
 characteristic impedance of the transmission line, Z<sub>0</sub>, must be kept as
 close as possible to 50 Ω as this gives you the best possible signal
 quality.

Dpending on your device, having all the lines terminated into 50 Ω
 might violate the maximum current specifications for your device. Refer to the
 *Specifications* document for your device for more information about
 the maximum current.

While a Z<sub>t</sub> of 50 Ω is ideal, you can also use
 values as high as 150 Ω without significantly affecting signal quality. Using this
 higher resistance value allows you to increase the voltage swing across the DUT and
 decrease the drive current requirements on your NI 6555/6556.

At DC there is
 effectively a voltage divider between the 50 Ω Z<sub>S</sub> resistance and the
 termination resistance, having a terminated load reduces the largest possible
 voltage swings at the DUT according to the following formula:

V<sub>t</sub> =
 V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> + Z<sub>t</sub>))

For a 50 Ω
 termination, programming a generation voltage level of 3.3 V at the NI 6555/6556
 source produces a 3.3 V x (50/100) = 1.65 V swing. This reduced voltage swing at the
 DUT must be considered when you create your system.

Parent topic:

Terminating Your NI 6555/6556

Related concepts:

- Characteristic Impedance
- Voltage Levels
- Transmission Lines

<!--NI_TOPIC bundle=ni-hsdio path=ni-6555-6556-termination-summary.html language=enus -->
## TOPIC 00089: NI 6555/6556 Termination Summary

- bundle_id: `ni-hsdio`
- source_path: `ni-6555-6556-termination-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6555-6556-termination-summary.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following illustration provides a high-level summary of the termination considerations for your NI 6555/6556:Generation Termination Source Transmission Line Termination (Load) Z[s] = 50 Ω Z[o] = 50 Ω Z[t] = Open (Tristate) or Unterminated Works for all except the most demanding applications. Z[s

### NI 6555/6556 Termination Summary

The following illustration provides a high-level summary of the termination considerations for
 your NI 6555/6556:

#### *Generation
 Termination*

[IMAGE alt='image' src='GUID-C86F69C1-30B1-41A5-BDBC-9BA3E98FDDFE-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zs = 50 Ω | Zo = 50 Ω | Zt = Open (Tristate) or Unterminated Works for all except the most demanding applications. |
| Zs = 50 Ω | Zo = 50 Ω | Zt = 50Ω–150 Ω Recommended for better signal integrity. |

#### *Acquisition Termination*

[IMAGE alt='image' src='GUID-20878CB1-3C2A-4A03-AB8D-A5B894B34C2D-a5.gif']

| Source | Transmission Line | Termination (Load) |
| --- | --- | --- |
| Zt = high impedance | 50 Ω | Zs = 50 Ω This is the recommended configuration for most applications. |
| Zt = high impedance | 50 Ω | Zs < 50 Ω This configuration is not recommended because of the mismatch on both ends. The recommended setup is to increase Zs to 50 Ω by adding series resistance at the source. |
| Zt = high impedance | 50 Ω | Zs > 50 Ω This configuration is not recommended because of the mismatch on both ends.Note You must reduce the operating frequency significantly to allow the signal reflections to settle down. You must reduce the frequency proportional to cable length and impedance mismatch. |
| Zt = 50 Ω | 50 Ω | Zs = 50 Ω This configuration is recommended for best signal integrity. Vi = Vo/2 Source must be able to drive 50 Ω. |
| Zt = 50 Ω | 50 Ω | Zs < 50 Ω Source-side mismatch degrades signal integrity, but this configuration is still usable in many applications. Vi = 50/(50 + Zs) × Vo |
| Zt = 50 Ω | 50 Ω | Zs > 50 Ω Source-side mismatch degrades signal integrity, but this configuration is still usable in many applications. Vi = 50/(50 + Zs) × Vo |

Parent topic:

Terminating Your NI 6555/6556

Related concepts:

- NI 6551/6552 Generation Termination
- NI 6551/6552 Acquisition Termination

<!--NI_TOPIC bundle=ni-hsdio path=ni-6555-6556-termination-with-remote-sense.html language=enus -->
## TOPIC 00090: NI 6555/6556 Termination With Remote Sense

- bundle_id: `ni-hsdio`
- source_path: `ni-6555-6556-termination-with-remote-sense.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-6555-6556-termination-with-remote-sense.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Feedback PathsThe PPMU is the only component on the NI 6555/6556 that can use the remote sense feedback path. Feedback paths are required to regulate voltage and current levels in force operations. On the NI 6555/6556, there are multiple feedback paths. Current feedback uses a local feedback path an

### NI 6555/6556 Termination With Remote Sense

#### Feedback Paths

The PPMU is the only component on the NI 6555/6556 that can
 use the remote sense feedback path. Feedback paths are required to regulate voltage
 and current levels in force operations. On the NI 6555/6556, there are multiple
 feedback paths. Current feedback uses a local feedback path and requires that you
 enable the PPMU. Voltage feedback can use a local feedback path or one of two remote
 feedback paths. The NI 6555/6556 can measure a voltage on any pin at any time,
 regardless of whether or not you have enabled the PPMU.

#### Remote Sense Feedback Through the Front Panel

Remote sense feedback
 through the NI 6555/6556 REMOTE SENSE front panel connector. This method provides
 maximum accuracy for high current applications and requires additional cabling and
 design considerations to connect the NI 6555/6556 to the DUT. Low current and low
 aperture time applications have greater accuracy when using the local feedback path
 due to improved noise performance.

#### Moderate Impedance

For applications that use a channel for both high-speed digital signaling and remote
 sense PMU operations, it is recommended that you use moderate impedance
 (R<sub>Sense</sub>) to connect the remote sense path to the load point. Such a
 design minimizes reflections which could increase the noise and decrease the
 accuracy on the feedback path. The exact value of the moderate impedance appropriate
 for your system depends on the variables in your application.

Example Values of Moderate Impedance:

- Values near DC values require no additional impedance to prevent reflections
 because there is no additional voltage drop when run in parallel with the 100 kΩ
 internal resistor.
- For high-speed applications, use a nominal resistance of 1 kΩ which yields an
 equivalent 1 kΩ resistance when run in parallel with the 100 kΩ internal
 resistor.

#### Voltage Drop

The feedback path through the remote sense front panel connector is parallel to the
 100 kΩ onboard resistor, which compensates for the cable resistance error to the
 DUT. The exact value of the voltage drop depends on the resistance used in your
 high-speed digital application.

[IMAGE alt='image' src='GUID-E13501AE-3E03-4DEF-B556-E9B9DB54B39F-a5.gif']

The following equation represents the voltage drop when measured through the
 remote sense front panel connector:

V<sub>Error</sub> = I<sub>Max</sub> ×
 R<sub>Cable</sub> × [R<sub>Interconnect</sub> / (R<sub>Interconnect</sub> +
 100 kΩ)] Where R<sub>Cable</sub> is the cable impedance and R<sub>Interconnect</sub>
 is the moderate impedance placed between the REMOTE SENSE front panel connector and
 the DUT.

#### Improved Performance

The voltage drop is typically not significant relative to the overall accuracy of the
 system, which makes the feedback path through the remote sense front panel connector
 useful for high-current applications. For example, if you regulate 32 mA using the
 feedback path through the remote sense front panel connector with a cable resistance
 of 2 Ω, the voltage drop between the 100 kΩ internal resistor and the 1 kΩ resistor
 is 64 mV. This yields a voltage drop of 0.63 mV, as shown in the following
 equation:

64 mV × [1 kΩ / (1 kΩ + 100 kΩ)] = 0.63 mV

If this voltage
 drop is still too large, you can replace the 1 kΩ resistor with a switch.

Parent topic:

Terminating Your NI 6555/6556

<!--NI_TOPIC bundle=ni-hsdio path=ni-656x-acquisition-termination.html language=enus -->
## TOPIC 00091: NI 656x Acquisition Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-656x-acquisition-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-656x-acquisition-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: DIO, STROBE, LVDS PFI ChannelsThe NI 656x devices employ a single differential 100 Ω terminating resistor located at the differential receiver. This 100 Ω resistor guarantees signal quality in a 100 Ω differential environment and induces the correct voltage levels required by the LVDS standard.This

### NI 656x Acquisition Termination

#### DIO, STROBE, LVDS PFI Channels

The NI
 656x devices employ a single differential 100 Ω terminating resistor located at the
 differential receiver. This 100 Ω resistor guarantees signal quality in a 100 Ω
 differential environment and induces the correct voltage levels required by the LVDS
 standard.

This impedance is always present and is not software
 selectable.

#### Single-Ended PFI Channels

For single-ended trigger
 operations, the NI 656x can only be used in a high-impedance load
 configuration because the input impedance of the NI 656x is set to
 10 kΩ, when in single-ended mode. The high-impedance load
 configuration is easy to drive since it does not present a
 significant DC load to the source and preserves the signal
 amplitude. To achieve the highest level of AC signal quality, you
 must follow the recommendations in this section..

The same
 transmission line considerations discussed for the generation case
 are applicable to acquired signals. The input impedance of 10 kΩ
 implies a reflection coefficient Γ<sub>t</sub> of 0.99, or nearly
 full reflection.

With all high-impedance load transmission
 lines, you must take care to match the source impedance of the
 transmission line to the characteristic impedance of the
 transmission line. The source matching in this configuration is
 important, since there are significant reflections from the
 high-impedance load (input of NI 656x in this case).

You must
 ensure that your transmission line has a characteristic impedance of
 as close to 50 Ω as possible.

Z<sub>s</sub> (external source
 output impedance) must match Z<sub>0</sub> = 50 Ω (the cable
 impedance) for 10 kΩ input configuration.

To achieve this
 Z<sub>s</sub> = 50 Ω, you must determine the output
 impedance of your digital driver. Add a series resistor as close as
 possible to the driver pin such that the output impedance of your
 buffer plus the value of the series resistor equal 50 Ω.

If
 you require 50 Ω termination for your acquisition application,
 consider using one of the NI 655x products.

Parent topic:

Terminating Your NI 656x

Related concepts:

- NI 656x Generation Termination
- Characteristic Impedance

<!--NI_TOPIC bundle=ni-hsdio path=ni-656x-generation-termination.html language=enus -->
## TOPIC 00092: NI 656x Generation Termination

- bundle_id: `ni-hsdio`
- source_path: `ni-656x-generation-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/ni-656x-generation-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generation Termination: Terminated Load ConfigurationDIO, DDC CLK OUT, and LVDS PFI Channels The NI 656x requires a differential termination at the destination of 100 Ω to properly drive the LVDS logic levels and to maintain signal integrity.LVDS is a current-driven technology. That is, a logic stat

### NI 656x Generation Termination

#### Generation Termination: Terminated Load
 Configuration

#### DIO, DDC CLK OUT, and LVDS PFI
 Channels

The NI 656x requires a differential termination at the destination
 of 100 Ω to properly drive the LVDS logic levels and to maintain signal
 integrity.

LVDS is a current-driven technology. That is, a logic state is
 derived from the differential voltage generated by forcing a current through a known
 impedance. Forcing current one direction signifies a logic high level, and forcing
 current the alternate direction signifies a logic low level. As such, it requires
 that the current path be completed, through a 100 Ω resistor, at the destination.
 The differential voltage then seen at the receiver is a function of this resistor.
 LVDS levels are generated using a 100 Ω resistor at the receiver.

For
 applications requiring the highest levels of signal integrity and timing accuracy,
 strongly recommended to carefully control the termination impedance at the end of
 the transmission line. In a differential environment, there is an effective virtual
 ground at the midpoint of there terminating resistor. In a 50 Ω single-ended
 environment, the transmission line is effectively matched with the 100 Ω
 differential impedance caused by this virtual ground effect.

#### Unloaded Single-Ended PFI
 Channels

A common configuration for your NI 656x is to configure the terminals for
 single-ended mode and connect them directly to your device under test (DUT). Most
 digital logic inputs have an input impedance of 1–10 KΩ. Therefore, connecting the
 NI 656x output terminals directly to the input of your DUT effectively creates a
 source-terminated configuration because the PFI channels of the NI 656x have a 50 Ω
 source impedance when in single-ended mode.

While this source configuration
 does not provide the absolute highest level of signal quality, there are many
 advantages to a source-terminated configuration. First, very good signal levels are
 possible if you ensure that you have the cleanest possible 50 Ω characteristic
 impedance transmission line. Second, this source-terminated configuration allows you
 to directly wire to your DUT without the need for additional termination resistors.
 Lastly, given that at DC there is effectively a voltage divider between the 50 Ω
 Z<sub>s</sub> resistance and the high-impedance Z<sub>t</sub> of your DUT,
 having a source-terminated load preserves the largest possible voltage swings at the
 DUT according to the following formula:

V<sub>t</sub> =
 V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> + Z<sub>t</sub>))

Therefore,
 for a DUT with an input impedance of 1 kΩ, programming a generation voltage level of
 3.3 V at the NI 655x source produces a 3.3 V × (1000/1050) = 3.14 V swing.

The source-terminated load generates reflections in the transmission line. These
 reflections are absorbed at the source and not re-reflected back to the load, thus
 preserving the signal integrity. The source impedance does not perfectly match the
 transmission line impedance. A small fraction of the reflected wave is re-reflected
 back toward the load. This second reflection creates small signal aberrations and a
 low level of inter-symbol interference.

For example, a 5% mismatch at the
 source results in a 2.5% re-reflection back at the load:

Γ<sub>s</sub> = (1.05
 - 1)/(1.05 + 1) ≈ 2.5%

#### Loaded Single-Ended PFI
 Channels

The source-terminated load configuration is easy to use with a terminated source,
 such as the NI 656x, and is recommended for all applications except the most
 demanding in regard to timing precision or signal integrity. For applications
 demanding the highest levels of signal quality and timing precision, it is
 recommended that you seriously consider following the recommendations of the
 terminated load configuration.

For applications requiring the highest levels
 of signal integrity and timing accuracy, it is recommended that you control the
 termination impedance at the end of the transmission line. To control the
 termination impedance, add a parallel termination resistor to ground as close as
 possible to the digital input pin of the device under test (DUT). In this
 configuration, the transmission line is terminated at both ends of the transmission
 line, which produces the highest possible signal integrity.

The source
 impedance, Z<sub>S</sub>, and the characteristic impedance of the transmission line,
 Z<sub>0</sub>, must be kept as close as possible to 50 Ω as this gives you the
 best possible signal quality.

Depending on your device, having all the lines
 terminated into 50 Ω may violate the maximum current specifications. Refer to the
 *Specifications* document for more information about the maximum
 current for your device to determine how many lines you can simultaneously terminate
 into 50 Ω.

While a Z<sub>t</sub> of 50 Ω is ideal, you can also use values as
 high as 300 Ω without significantly affecting signal quality. Using this higher
 resistance value allows you to increase the voltage swing across the DUT and
 decrease the drive current requirements on your NI 656x.

At DC there is
 effectively a voltage divider between the 50 Ω Z<sub>S</sub> resistance and the
 termination resistance, having a terminated load reduces the largest possible
 voltage swings at the DUT according to the following formula:

V<sub>t</sub> =
 V<sub>s</sub>×(Z<sub>t</sub>/(Z<sub>s</sub> + Z<sub>t</sub>))

For a 50 Ω
 termination, programming a generation voltage level of 3.3 V at the NI 656x PFI
 source produces a 3.3 V x (50/100) = 1.65 V swing at the DUT. This reduced voltage
 swing at the DUT must be considered when you create your system.

Parent topic:

Terminating Your NI 656x

Related concepts:

- Differential Logic Families
- Transmission Lines
- Characteristic Impedance
- Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=onboard-memory.html language=enus -->
## TOPIC 00093: Onboard Memory

- bundle_id: `ni-hsdio`
- source_path: `onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/onboard-memory.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital waveform generators and analyzers use multiple megabytes of onboard memory to acquire and generate data. Onboard memory allows much higher data rates than would be allowed by streaming data from system memory across the PCI bus. Acquisition memory and generation memory are separate. For exam

### Onboard Memory

Digital waveform generators and analyzers use multiple megabytes of onboard memory to
 acquire and generate data. Onboard memory allows much higher data rates than would be
 allowed by streaming data from system memory across the PCI bus. Acquisition memory and
 generation memory are separate. For example, a 64 MS device has two 64 MS memory blocks,
 one for acquisition and one for generation.

Note

The NI 654x/655x/656x can be purchased with different memory options. For more
 information on these options, see *ni.com/shop*.

Parent topic:

Digital Terminology

Related concepts:

- Generation Onboard Memory
- Acquisition Onboard Memory

<!--NI_TOPIC bundle=ni-hsdio path=open-collector.html language=enus -->
## TOPIC 00094: Open Collector

- bundle_id: `ni-hsdio`
- source_path: `open-collector.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/open-collector.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When configured for open-collector generation, generating logic 1 puts the channel into a high-impedance state. For open collector operations, external pull-up resistors are typically used to force a voltage for the logic high state.Differential digital waveform generator/analyzers, such as the NI 6

### Open Collector

Note

Drive type is a channel-based attribute. Channels configured for open-collector output never
 drive the **Generation Voltage High** level. Logic 1s found in
 initial and idle states force the line to high-impedance for static and dynamic
 generations.

The main applications for open collector generation channels are bidirectional, multidrop busses.
 Open-collector outputs prevent different drivers from attempting to double-drive the
 line. By using a pull-up resistor, the bus is high if all connected devices are high,
 and the bus is low if any device drives a 0. This setup is generally called wired-AND
 for positive-true logic and wired-OR for negative-true logic. Some examples of busses
 implemented with open-collector outputs include I<sup>2</sup>C and SMBus.

When interfacing with a wired logic bus, you must consider the voltages that are generated on the
 bus. These voltages depend on four factors: value of the pull-up resistor, value to
 which the line is "pulled up", configured voltage for low state, and configured input
 impedance.

The following diagram shows how these factors interact:

[IMAGE alt='image' src='GUID-011FF341-C26D-406B-8BFF-AD9849555ED3-a5.gif']

Typical applications have a **Generation Voltage Low** level of 0.0 V,
 and R<sub>in</sub> as high impedance; R<sub>pull</sub> must be carefully chosen to get
 the desired voltage values in the bus. Refer to your device specifications for the
 R<sub>in</sub> for your device. Typical values for a pull-up resistor in
 I<sup>2</sup>C range between 2.4 kΩ and 3.9 kΩ.

NI 655x devices have per cycle, per pin tristate functionality, which allows the generation of
 0s, 1s, and tristate in the same channel. Open collector is limited to 0 and tristate;
 however, these two features can operate simultaneously. Using per cycle tristate in a
 channel configured for open-collector generation causes the line to be tristated by Z
 and 1 digital logic states found in the waveform.

Parent topic:

Drive Type

Related concepts:

- Static Generation
- Initial and Idle States
- Per Cycle Tristate
- Digital Logic States

<!--NI_TOPIC bundle=ni-hsdio path=overview.html language=enus -->
## TOPIC 00095: NI-HSDIO Overview

- bundle_id: `ni-hsdio`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/overview.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-HSDIO provide support for customers using PXI Digital Waveform Instruments or Digital Waveform Devices. NI-HSDIO is an instrument driver that communicates with digital waveform hardware, which perform high-speed DIO (HSDIO) functions. This driver software includes: Flexible API based on IVI guide

### NI-HSDIO
 Overview

NI-HSDIO provide support for customers using PXI Digital Waveform Instruments or
 Digital Waveform Devices.

NI-HSDIO is an instrument driver that communicates with digital waveform hardware, which
 perform high-speed DIO (HSDIO) functions.

This driver software includes:

- Flexible API based on IVI guidelines
- Complete documentation of the supported hardware
- Configuration and testing utilities

<!--NI_TOPIC bundle=ni-hsdio path=pattern-match-trigger.html language=enus -->
## TOPIC 00096: Pattern-Match Trigger

- bundle_id: `ni-hsdio`
- source_path: `pattern-match-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pattern-match-trigger.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A pattern-match trigger behaves like a combination lock. When the correct combination is read, the lock opens. Likewise, in the case of triggers, when the desired acquisition pattern is read, the pattern-match trigger is asserted. The level state of a digital signal can be represented by a binary pa

### Pattern-Match Trigger

A pattern-match trigger behaves like a combination lock. When the correct combination is read,
 the lock opens. Likewise, in the case of triggers, when the desired acquisition pattern
 is read, the pattern-match trigger is asserted.

The level state of a digital signal can be represented by a binary pattern, where a
 1 corresponds to the high level (H) and a
 0 corresponds to a low level (L).

For example, consider the logic levels on channels 0 through 3: H, L, L, H. This pattern
 can be represented in binary by replacing each H with 1 and each L with 0. The resulting
 binary representation is: 1001.

A pattern-match trigger enables the device to monitor input terminals for a specific bit
 pattern. For example, the pattern could be 10101110. When the device detects this
 pattern, it asserts the pattern-match trigger.

R

r

F

f

E

e

Note

Parent topic:

Types of Triggers

<!--NI_TOPIC bundle=ni-hsdio path=pci-chassis-cooling.html language=enus -->
## TOPIC 00097: PCI Chassis Cooling

- bundle_id: `ni-hsdio`
- source_path: `pci-chassis-cooling.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pci-chassis-cooling.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all PCI chassis provide the same cooling. When you select a PCI chassis, consider if the chassis provides adequate air flow. Air flow is especially important for high-power and sensitive devices, such as PCI signal generators.PCI digital waveform generators and analyzers are high-precision instr

### PCI Chassis Cooling

Not all PCI chassis provide the same cooling. When you select a PCI chassis, consider if the
 chassis provides adequate air flow. Air flow is especially
 important for high-power and sensitive devices, such as PCI
 signal generators.

PCI digital waveform generators and analyzers are high-precision instruments and may be sensitive
 to interference from other electronic devices. To optimize the
 accuracy and performance of the device. To optimize the accuracy
 and performance of such devices, place the device one slot away
 from devices with power supplies and other noisy circuitry. The
 device might also be sensitive to heat generated by high-power
 products in neighboring slots. When possible, consider placing
 the device away from high-power devices to optimize cooling.

Parent topic:

PCI

<!--NI_TOPIC bundle=ni-hsdio path=pci.html language=enus -->
## TOPIC 00098: PCI

- bundle_id: `ni-hsdio`
- source_path: `pci.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pci.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Peripheral Component Interconnect (PCI) is a high-performance expansion bus architecture originally developed by Intel to replace ISA and EISA. It achieved widespread acceptance as a standard for PCs and workstations and offers a theoretical maximum transfer rate of 132 MB/s.

### PCI

Peripheral Component Interconnect (PCI) is a high-performance expansion bus architecture
 originally developed by Intel to replace ISA and EISA. It
 achieved widespread acceptance as a standard for PCs and
 workstations and offers a theoretical maximum transfer rate of
 132 MB/s.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-hsdio path=per-cycle-tristate.html language=enus -->
## TOPIC 00099: Per Cycle Tristate

- bundle_id: `ni-hsdio`
- source_path: `per-cycle-tristate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/per-cycle-tristate.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital waveform generators and analyzers allow you to drive a logic 0 or a 1 during every active period of the sample clock. Some devices have the additional capability of driving a logic 0, logic 1 or tristating the channel during every active clock cycle. This capability is referred to as per cyc

### Per Cycle Tristate

Digital waveform generators and analyzers allow you to drive a logic 0 or a 1 during
 every active period of the sample clock. Some devices have the additional capability of
 driving a logic 0, logic 1 or tristating the channel during every active clock cycle.
 This capability is referred to as per cycle tristate. This functionality allows you to
 create waveforms composed of 0, 1, and Z values on any channel and on any sample. For
 each sample in the waveform, you can select which channel to tristate by inserting Z
 values in the waveform at that location. When using per cycle tristate, some devices
 support less channels than when in binary mode.

[IMAGE alt='image' src='GUID-8D5A4518-E842-401B-9D38-751CC38499BE-a5.gif']

Note

When switching a channel from driving to receiving data at high-speeds, allow enough time
 for all the samples to propogate through the system. This ensures that signal
 reflections resulting from tristating the channel do not affect the signal
 transmission.

Before writing waveforms using per cycle tristate, you must first configure the device to
 support extended data states. To do this, set the supported data states property to
 O, 1, Z (tristate) or the
 NIHSDIO_ATTR_SUPPORTED_DATA_STATES attribute to
 NIHSDIO_VAL_STATES_0_1_Z.

Parent topic:

Dynamic Generation

<!--NI_TOPIC bundle=ni-hsdio path=programming-flow.html language=enus -->
## TOPIC 00100: Programming Flow

- bundle_id: `ni-hsdio`
- source_path: `programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/programming-flow.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The diagrams in the following sections show the basic programming flow of applications using NI-HSDIO for the following tasks: Waveform generation Waveform acquisition Simultaneous generation Acquisition Static generation The functions and VIs are categorized under these main topics to assist you in

### Programming Flow

The diagrams in the following sections show the basic programming flow of applications using
 NI-HSDIO for the following tasks:

- Waveform generation
- Waveform acquisition
- Simultaneous generation
- Acquisition
- Static generation

The functions and VIs are categorized under these main topics to assist you in understanding
 where you should call a function or VI in your applications.
 Functions and VIs that do not fall into the programming flow are
 considered utility functions that perform various tasks, such as
 resetting the device.

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-hsdio path=programming.html language=enus -->
## TOPIC 00101: Programming

- bundle_id: `ni-hsdio`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/programming.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides information about programming your waveform generator/analyzer with NI-HSDIO.

### Programming

This section provides information about programming your waveform generator/analyzer with
 NI-HSDIO.

<!--NI_TOPIC bundle=ni-hsdio path=pxi-clk10.html language=enus -->
## TOPIC 00102: PXI_CLK10

- bundle_id: `ni-hsdio`
- source_path: `pxi-clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-clk10.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI chassis supplies the PXI 10 MHz system Reference clock signal (PXI_CLK10) independently to each peripheral slot. An independent buffer drives the clock signal to each peripheral slot. The buffer has a source impedance matched to the backplane and a skew ranging from less than 1 ns to better

### PXI_CLK10

The PXI chassis supplies the PXI 10 MHz system Reference clock signal (PXI_CLK10) independently
 to each peripheral slot. An independent buffer drives the clock signal to each peripheral
 slot. The buffer has a source impedance matched to the backplane and a skew ranging from less
 than 1 ns to better than 250 ps between slots. You can use this common reference clock signal
 to synchronize multiple devices in a measurement or control system.

You can drive PXI_CLK10 from an external source through the PXI_CLK10_IN pin on the P2
 connector of the PXI Star trigger slot, which is slot 2. Sourcing an external clock on this
 pin automatically disables the 10 MHz source on the backplane. You can synchronize multiple
 chassis that have connectors on the back panel for 10 MHz reference in and 10 MHz reference
 out. For more information about PXI_CLK10, refer to the *Specifications* document
 for your PXI chassis.

Parent topic:

PXI/PXI Express

<!--NI_TOPIC bundle=ni-hsdio path=pxi-express-bandwidth-considerations.html language=enus -->
## TOPIC 00103: PXI Express Bandwidth Considerations

- bundle_id: `ni-hsdio`
- source_path: `pxi-express-bandwidth-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-express-bandwidth-considerations.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: PXI Express (PCIe) digital waveform generators and analyzers use PCIe as the interface to the computer. The logical connection between the device and the computer is called a PCIe link. When the device fetches a waveform or downloads a waveform, it can saturate its link. This saturation occurs becau

### PXI Express Bandwidth Considerations

PXI Express (PCIe) digital waveform generators and analyzers use PCIe as the interface to the
 computer. The logical connection between the device and the
 computer is called a PCIe link. When the device fetches a
 waveform or downloads a waveform, it can saturate its link. This
 saturation occurs because the device is copying data to or from
 its onboard memory to the CPU memory as fast as it can. This
 transfer can exceed the bandwidth of the PCIe link.

The theoretical bandwidth of the onboard memory of the device is 3.2 GB/s. However, the
 theoretical bandwidth of the PCIe link is about about 850 MB/s.
 Transferring data from the onboard memory can saturate the PCIe
 link. The maximum waveform fetching data rate is 820 MB/s, and
 the maximum waveform downloading data rates is 600 MB/s. For
 example, with an PXI 8130 controller in a 1065Q chassis and a
 device in slot 9, this device would share bandwidth with devices
 in slots 10 through 14.

Bandwidth sharing is a problem if other devices in your application require guaranteed bandwidth
 to the PCI Express bus. For example, if two PXIe devices perform
 concurrent data transfers, an underflow or overflow error could
 occur because the concurrent transfers saturate the PCIe
 bus.

You can limit the PXIe digital waveform generators and analyzer so that it doesn't saturate the
 PCIe bus.

The following table lists the properties and attributes that allow you to modify how the hardware
 uses the PXIe bus:

| LabVIEW Property | C/C++ Attribute |
| --- | --- |
| Advanced:Data Transfer:Maximum Bandwidth | NIHSDIO_ATTR_MAXIMUM_BANDWIDTH |
| Advanced:Data Transfer:Preferred Packet Size | NIHSDIO_ATTR_PREFERRED_PACKET_SIZE |
| Advanced:Data Transfer:Maximum In-Flight Read Requests | NIHSDIO_ATTR_MAXIMUM_IN_FLIGHT_READ_REQUESTS |

Parent topic:

Generating Waveforms Using Streaming

<!--NI_TOPIC bundle=ni-hsdio path=pxi-express-modules.html language=enus -->
## TOPIC 00104: PXI Express Modules

- bundle_id: `ni-hsdio`
- source_path: `pxi-express-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-express-modules.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI Express Specification integrates PCI Express signaling into the PXI standard, which increases backplane bandwidth and enhancing PXI timing and synchronization features while maintaining backward compatibility with PXI. The following figure shows a typical PXI Express chassis installation: Di

### PXI Express Modules

The PXI Express Specification integrates PCI Express signaling into the PXI standard, which
 increases backplane bandwidth and enhancing PXI timing and synchronization features
 while maintaining backward compatibility with PXI.

The following figure shows a typical PXI Express chassis installation:

[IMAGE alt='image' src='GUID-F00FA59A-E2FA-4D04-85B6-9F72D07793C4-a5.gif']

#### Digital Waveform Generators and Analyzers Available as PXI Express
 Modules

The following digital waveform generators and analyzers are
 available in the PXI Express form factor:

- NI 6544/6545
- NI 6547/6548
- NI 6555/6556

#### Chassis Guidelines

PXI Express signal generators can be installed in the
 following PXI Express chassis slots:

- PXI hybrid slots —Accepts either PXI modules that are
 hybrid slot-compatible or PXI Express modules
- PXI Express slots —Accepts PXI Express modules

Note

Specifications

#### Using PXI Express Products with CompactPCI Express Products

The
 CompactPCI/PXI Express backplane integrates PCI Express while still preserving
 compatibility with current PXI modules. PXI Express hybrid slots are capable of
 delivering signals for both PCI and PCI Express. The hybrid slot allows you to
 install a PXI module that uses PCI signaling or a PXI Express module that uses PCI
 Express signaling.

Parent topic:

PXI/PXI Express

<!--NI_TOPIC bundle=ni-hsdio path=pxi-modules.html language=enus -->
## TOPIC 00105: PXI Modules

- bundle_id: `ni-hsdio`
- source_path: `pxi-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-modules.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: PCI eXtensions for Instrumentation (PXI) modular instrumentation delivers a PC based, standardized, high performance measurement and automation system. PXI combines the high speed PCI bus with integrated timing and triggering designed specifically for measurement and automation applications to deliv

### PXI Modules

PCI eXtensions for Instrumentation (PXI) modular instrumentation delivers a PC based,
 standardized, high performance measurement and automation system. PXI combines the high
 speed PCI bus with integrated timing and triggering designed specifically for
 measurement and automation applications to deliver significant performance improvements
 over older architectures. The following figure shows a typical PXI chassis
 installation:

[IMAGE alt='image' src='GUID-E0F99E65-D88A-4FE7-A760-4F525B1DFC01-a5.gif']

#### Digital Waveform Generator/Analyzers Available as PXI Modules

The
 following digital waveform generators and analyzers are available in the PXI form
 factor:

- NI 6541/6542
- NI 6551/6552
- NI 6561/6562

#### Chassis Guidelines

PXI signal generators can be installed in the
 following chassis and slots:

- PXI chassis —PXI signal generators can be installed in any
 peripheral slot of a PXI chassis.
- PXI Express chassis —PXI signal generators can be
 installed in the following PXI Express chassis slots:
  - PXI 1 slots —Accepts PXI modules
  - PXI hybrid slots —Accepts either PXI modules that
 are hybrid slot compatible or PXI Express modules

Note

Specifications

#### Using PXI-Compatible Products with Standard CompactPCI Products

The
 ability to use PXI compatible products with standard CompactPCI products is an
 important feature of revision 2.1 of the PXI specification. If you use a PXI
 compatible plugin device in a standard CompactPCI chassis, you cannot use PXI
 specific functions, but you can still use the basic plug-in device
 functions.

For example, the PXI trigger bus on signal generators is available
 in a PXI chassis but not in a CompactPCI chassis. The CompactPCI specification
 permits vendors to develop sub buses that co-exist with the basic PCI interface on
 the CompactPCI bus. Compatible operation is not guaranteed between CompactPCI
 devices with different sub buses nor between CompactPCI devices with sub buses and
 PXI.

The standard implementation for CompactPCI does not include these
 sub-buses. Signal generators work in any standard CompactPCI chassis. PXI specific
 features, such as the PXI trigger bus and PXI_CLK10 reference are implemented on the
 J2 connector of the CompactPCI bus.

Parent topic:

PXI/PXI Express

Related concepts:

- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-hsdio path=pxi-pxi-express-chassis-cooling.html language=enus -->
## TOPIC 00106: PXI/PXI Express Chassis Cooling

- bundle_id: `ni-hsdio`
- source_path: `pxi-pxi-express-chassis-cooling.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-pxi-express-chassis-cooling.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you select a PXI or PXI Express chassis, consider if the chassis provides adequate air flow. Air flow is especially important for high-power and sensitive devices, such as signal generators.PXI and PXI Express digital waveform generators and analyzers are high precision instruments and might be

### PXI/PXI Express Chassis Cooling

When you select a PXI or PXI Express chassis, consider if the chassis
 provides adequate air flow. Air flow is especially important for
 high-power and sensitive devices, such as signal generators.

PXI and PXI Express digital waveform generators and analyzers are high precision instruments and
 might be sensitive to interference from other electronic
 devices. optimize the accuracy and performance of such devices,
 place the device one slot away from devices with power supplies
 and other noisy circuitry. The device might also be sensitive to
 heat generated by high power products in neighboring slots. When
 possible, consider placing the device away from high power
 devices to optimize cooling.

Parent topic:

PXI/PXI Express

<!--NI_TOPIC bundle=ni-hsdio path=pxi-pxi-express.html language=enus -->
## TOPIC 00107: PXI/PXI Express

- bundle_id: `ni-hsdio`
- source_path: `pxi-pxi-express.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-pxi-express.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about integrating digital waveform generator/analyzers into a PXI based measurement system. The PXI architecture has built-in timing and triggering features that can synchronize multiple devices using the PXI trigger bus lines on the PXI backplane. Multiple devices

### PXI/PXI Express

This section contains information about integrating digital waveform generator/analyzers into a
 PXI based measurement system.

The PXI architecture has built-in timing and triggering features that can synchronize multiple
 devices using the PXI trigger bus lines on the PXI backplane. Multiple devices in a modular
 instrumentation system can share a common reference clock and synchronize to triggers that are
 distributed over controlled signal paths that ensure matched propagation.

PC plugins with RTSI also provide an internal bus that can be accessed by multiple devices.
 Internal routing of these timing signals in PXI (and PC plugins with RTSI) eliminate complicated
 external wiring and must calculate propagation delays. Standardized timing protocols eliminate
 incompatibilities, giving you the best performance when synchronizing any kind of analog,
 digital, or timing measurements.

Parent topic:

Integration and System Considerations

Related concepts:

- Reference Clock
- Triggers
- RTSI

<!--NI_TOPIC bundle=ni-hsdio path=pxi-star-trigger-line.html language=enus -->
## TOPIC 00108: PXI Star Trigger Line

- bundle_id: `ni-hsdio`
- source_path: `pxi-star-trigger-line.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-star-trigger-line.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI star trigger is a feature implemented on PXI chassis. PXI chassis have a PXI trigger bus that is linked to all slots in the chassis. In addition, PXI chassis have a PXI star trigger that is linked to the system timing slot (slot 2 on PXI chassis). The PXI star trigger is a high performance t

### PXI Star Trigger Line

The PXI star trigger is a feature implemented on PXI chassis. PXI chassis have a PXI trigger bus
 that is linked to all slots in the chassis. In addition, PXI chassis have a PXI star
 trigger that is linked to the system timing slot (slot 2 on PXI chassis).

The PXI star trigger is a high performance trigger signal that you can use to synchronize
 all the devices in a chassis. You can also do this using the normal PXI trigger bus, but
 the PXI star trigger offers increased performance. Specifically, a propagation delay of
 no more than 5 ns and a skew of no more than 1 ns.

[IMAGE alt='image' src='GUID-308547AC-E227-4920-AEFC-FB53AD15DC04-a5.gif']

The PXI star trigger lines allow a PXI star controller in slot 2 to route signals to or from
 other peripheral slots with very low skew and at higher bandwidth than other PXI trigger
 lines.

- You must have a PXI star controller in slot 2 of the chassis.
- You must have one or more peripheral devices in the other slots.

PXI digital waveform generators and analyzers can receive a signal from PXI_STAR if they
 are placed in a peripheral slot 3 or higher.

Note

Parent topic:

PXI/PXI Express

Related concepts:

- PXI Modules

<!--NI_TOPIC bundle=ni-hsdio path=pxi-trigger-lines.html language=enus -->
## TOPIC 00109: PXI Trigger Lines

- bundle_id: `ni-hsdio`
- source_path: `pxi-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxi-trigger-lines.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The eight PXI bus trigger lines offer the following benefits: Synchronize the opration of several different PXI peripheral devices Have one device control the timed sequences of operations of other devices on in the system Triggers can be passed from one device to another. This allows for precisely

### PXI Trigger Lines

The eight PXI bus trigger lines offer the following benefits:

- Synchronize the opration of several different PXI peripheral devices
- Have one device control the timed sequences of operations of other devices on in the
 system

Triggers can be passed from one device to another. This allows for
 precisely timed responses to monitored or controlled asynchronous external events. The number
 of triggers that a particular application requires varies with the complexity and number of
 events involved.

[IMAGE alt='image' src='GUID-FCD7BB54-D174-4534-8D11-0A01C0DBA8EF-a5.gif']

The PXI specification is implemented with the RTSI bus through the PXI trigger lines. PXI
 specification requires eight lines,PXI_TRIG<0..7>, on the P2/J2
 connector of the PXI chassis for the trigger lines. The RTSI features of signal generators is
 implemented on this sub-bus. RTSI<0..6> are implemented on
 PXI_TRIG<0..6>, and the RTSI clock is routed on
 PXI_TRIG7.

Parent topic:

PXI/PXI Express

Related concepts:

- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-hsdio path=pxie-clk100.html language=enus -->
## TOPIC 00110: PXIe_CLK100

- bundle_id: `ni-hsdio`
- source_path: `pxie-clk100.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/pxie-clk100.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI Express chassis supplies the PXI 100 MHz differential system reference clock signal (PXIe_CLK100) independently to each peripheral slot. You can use this common reference clock signal to synchronize multiple devices in a measurement or control system. The PXIe_Clk100 is phase aligned with th

### PXIe_CLK100

The PXI Express chassis supplies the PXI 100 MHz differential system reference clock signal
 (PXIe_CLK100) independently to each peripheral slot. You can use this common reference
 clock signal to synchronize multiple devices in a measurement or control system.

The PXIe_Clk100 is phase aligned with the PXI_Clk10 which provides for a very accurate
 synchronization of devices. You can synchronize multiple chassis that have connectors on
 the back panel for 10 MHz reference in and 10 MHz reference out or with a system timing
 module. For more information about PXIe_CLK100, refer to the *Specifications*
 document for your PXI Express chassis.

Parent topic:

PXI/PXI Express

<!--NI_TOPIC bundle=ni-hsdio path=read.html language=enus -->
## TOPIC 00111: Read

- bundle_id: `ni-hsdio`
- source_path: `read.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/read.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Read VIs and functions are easy ways to acquire data from the device. These functions initiate an acquisition, fetch the acquired data, and return control to your program after all the requested data has been acquired. If you have not configured a Start trigger, the device immediately begins acq

### Read

The Read VIs and functions are easy ways to acquire data from the device. These functions
 initiate an acquisition, fetch the acquired data, and return control to your program
 after all the requested data has been acquired. If you have not configured a Start
 trigger, the device immediately begins acquiring the data.

The Read VIs and functions are shown in the following table:

| LabVIEW VIs | C Functions |
| --- | --- |
| Use one of the following instances of the niHSDIO Read Waveform polymorphic VI: niHSDIO Read Waveform (U32) niHSDIO Read Waveform (U16) niHSDIO Read Waveform (U8) niHSDIO Read Waveform (WDT) niHSDIO Read Multi Record (2D U32) niHSDIO Read Multi Record (2D U16) niHSDIO Read Multi Record (2D U8) niHSDIO Read Multi Record (1D WDT) | niHSDIO_ReadWaveformU16 niHSDIO_ReadWaveformU8 niHSDIO_ReadMultiRecordU32 niHSDIO_ReadMultiRecordU16 niHSDIO_ReadMultiRecordU8 |

Note

Parent topic:

Acquiring Dynamic Data

Related concepts:

- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio path=reading-and-writing-static-data.html language=enus -->
## TOPIC 00112: Reading and Writing Static Data

- bundle_id: `ni-hsdio`
- source_path: `reading-and-writing-static-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/reading-and-writing-static-data.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Static acquisition and static generation are software-timed operations that can be performed on any number of channels. Static operations can be performed using the VIs and functions shown in the following table: LabVIEW VIs C Functions niHSDIO Assign Static Channels niHSDIO_AssignStaticChannels niH

### Reading and Writing Static Data

Static acquisition and static generation are software-timed operations that can be performed on
 any number of channels. Static operations can be performed using the VIs and functions shown
 in the following table:

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Assign Static Channels | niHSDIO_AssignStaticChannels |
| niHSDIO Read Static (U32) | niHSDIO_ReadStaticU32 |
| niHSDIO Write Static (U32) | niHSDIO_WriteStaticU32 |

Parent topic:

Acquiring or Generating Static Data

Related concepts:

- Static Acquisition
- Static Generation

<!--NI_TOPIC bundle=ni-hsdio path=records.html language=enus -->
## TOPIC 00113: Records

- bundle_id: `ni-hsdio`
- source_path: `records.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/records.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A record is a group of samples. Acquired data is stored into device onboard memory as a record. When configuring an acquisition session, you can determine how many samples are stored in a record.You can also acquire multiple unique records in a series. This process is known as multirecord acquisitio

### Records

A record is a group of samples. Acquired data is stored into device onboard memory as a record.
 When configuring an acquisition session, you can determine how
 many samples are stored in a record.

You can also acquire multiple unique records in a series. This process is known as multirecord
 acquisition. The Advance trigger initiates the acquisition of
 the additional records in a multirecord acquisition. The end of
 record event indicates when a record acquisition is
 complete.

Parent topic:

Dynamic Acquisition

Related concepts:

- Onboard Memory
- Acquisition Configuration Functions
- Triggers Summary
- Events Summary

<!--NI_TOPIC bundle=ni-hsdio path=reference-clock.html language=enus -->
## TOPIC 00114: Reference Clock

- bundle_id: `ni-hsdio`
- source_path: `reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/reference-clock.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard frequency generator on the digital waveform generators and analyzer uses a Phase-Locked Loop (PLL) circuit to lock the high-frequency internal timebase of the device to a known reference frequency. The most common clock to which the device is locked is the reference clock signal on the P

### Reference Clock

Note

You can use the reference clock only when onboard clock is selected as the sample clock source
 for a dynamic generation or acquisition session.

Parent topic:

Clocks

Related concepts:

- Sample Clock

<!--NI_TOPIC bundle=ni-hsdio path=rtsi.html language=enus -->
## TOPIC 00115: RTSI

- bundle_id: `ni-hsdio`
- source_path: `rtsi.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/rtsi.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Real-Time System Integration Bus (RTSI) is a timing bus developed by NI. PCI devices can use the RTSI bus to share and exchange timing and control signals between multiple devices. The RTSI bus consists of the RTSI bus interface connector and an RTSI ribbon cable. The RTSI bus interface connecto

### RTSI

The Real-Time System Integration Bus (RTSI) is a timing bus developed by NI. PCI devices can use
 the RTSI bus to share and exchange timing and control signals between multiple devices.
 The RTSI bus consists of the RTSI bus interface connector and an RTSI ribbon cable. The
 RTSI bus interface connector is located at the back of the device.

Tip

Parent topic:

PCI

<!--NI_TOPIC bundle=ni-hsdio path=sample-clock.html language=enus -->
## TOPIC 00116: Sample Clock

- bundle_id: `ni-hsdio`
- source_path: `sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/sample-clock.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sample clock is the primary timebase for the digital waveform generator and analyzer. This clock controls the rate at which samples are acquired or generated. Each period of the sample clock is capable of initiating the acquisition or generation of one sample per channel. Using NI-HSDIO, you can

### Sample Clock

The sample clock is the primary timebase for the digital waveform generator and analyzer. This
 clock controls the rate at which samples are acquired or
 generated. Each period of the sample clock is capable of
 initiating the acquisition or generation of one sample per
 channel.

Using NI-HSDIO, you can program the sample clock to come from either the onborad clock source
 signal or an external frequency generator. Because of the pipelined architecture of the
 digital waveform generator and analyzer, the clock source for the Sample clock must be
 continuous, free-running, and of a constant frequency for the duration of each
 generation and acquisition operation.

Parent topic:

Clocks

Related concepts:

- Getting Started with NI-HSDIO

<!--NI_TOPIC bundle=ni-hsdio path=scripts.html language=enus -->
## TOPIC 00117: Scripts

- bundle_id: `ni-hsdio`
- source_path: `scripts.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/scripts.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can link and loop multiple waveforms together in a generation operation using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. The script can specify the order in which the waveforms are generated, the number of ti

### Scripts

You can link and loop multiple waveforms together in a generation operation using a script. A
 script is a series of instructions that indicates how waveforms saved in the onboard
 memory should be sent to the DUT. The script can specify the order in which the
 waveforms are generated, the number of times they are generated, and the triggers and
 markers associated with the generation.

You can create a script to manage dynamic generation based on multiple waveforms and triggers.
 For example, you download waveforms A, B, C, and D into device memory. You can then
 write a script that waits for a trigger to start generation. Then, when this trigger is
 received, generate waveform A three times with a marker at position 16 for each
 generation. Then, generate waveforms B, C, and D twice (BCDBCD).

A simple script example is shown below:

script myFirstScript

wait until scriptTrigger0

repeat 3

generate waveformA marker0(16)

end repeat

repeat 2

generate waveformB

generate waveformC

generate waveformD

end repeat

end script

When executed, this script generates three waveforms (countUp,
 allOnes, and countDown) consecutively.

Parent topic:

Dynamic Generation

Related concepts:

- Onboard Memory
- Dynamic Generation
- Generating Multiple Waveforms with Linking & Looping

<!--NI_TOPIC bundle=ni-hsdio path=select-channels.html language=enus -->
## TOPIC 00118: Select Channels

- bundle_id: `ni-hsdio`
- source_path: `select-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/select-channels.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your digital device contains multiple channels. Use the following VIs and functions to specify which channels you want to use in your data operations. LabVIEW VIs C Functions niHSDIO Assign Dynamic Channels niHSDIO_AssignDynamicChannels niHSDIO Assign Static Channels niHSDIO_AssignStaticChannels You

### Select Channels

Your digital device contains multiple channels. Use the following VIs and functions to specify
 which channels you want to use in your data operations.

| LabVIEW VIs | C Functions |
| --- | --- |
| niHSDIO Assign Dynamic Channels | niHSDIO_AssignDynamicChannels |
| niHSDIO Assign Static Channels | niHSDIO_AssignStaticChannels |

You can configure a channel for more than one simultaneous data operation. A channel can be
 simultaneously configured for the following operations:

- Dynamic generation and any (static and/or dynamic) acquisition
- Static generation and any (static and/or dynamic) acquisition
- Both static and dynamic acquisition

Note

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-hsdio path=signal-reflections.html language=enus -->
## TOPIC 00119: Signal Reflections

- bundle_id: `ni-hsdio`
- source_path: `signal-reflections.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/signal-reflections.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital rising or falling edge is a step function that can be modeled as a high-frequency wavefront. As the wavefront travels along the transmission line, it acts as a purely AC signal, encountering the characteristic impedance (Z[0]) of the transmission line. When the wavefront reaches the end of

### Signal Reflections

A digital rising or falling edge is a step function that can be modeled as a high-frequency
 wavefront. As the wavefront travels along the transmission line, it acts as a purely AC
 signal, encountering the characteristic impedance (Z<sub>0</sub>) of the transmission
 line. When the wavefront reaches the end of the path, if Z<sub>0</sub> and the
 termination (Z<sub>t</sub>) do not match, portions of the wave are reflected. As the
 wave reflects back along the transmission line, it eventually reaches the original
 source impedance (Z<sub>s</sub>). If the transmission line characteristic impedance
 (Z<sub>0</sub>) and Z<sub>s</sub> do not match, then portions of the wave are
 re-reflected. The superposition of these reflected waves can cause significant signal
 degradation.

Reflection caused by an impedance mismatch at the end of a transmission line is quantified by
 the reflection coefficient. Reflection coefficient Γ is given by the following
 formula:

Γ = V<sub>r</sub>/V<sub>i</sub> = (Z<sub>t</sub> - Z<sub>0</sub>)/(Z<sub>t</sub> +
 Z<sub>0</sub>)

where:

V<sub>r</sub> is the reflected voltage,

V<sub>i</sub> is the incident voltage,

Z<sub>t</sub> is the terminating impedance,

Z<sub>0</sub> is the characteristic impedance of the transmission line.

For example, by applying this formula, you can calculate that when a 3.3 V wave, traveling down a
 50 Ω characteristic medium hits a 1 kΩ load impedance.

The reflection coefficient Γ<sub>t</sub>, is equal to
 (1 kΩ - 50 Ω)/(1 kΩ + 50 Ω), or .90, and V<sub>r</sub> equals 0.9 x 3.3 V = 2.97 V.

Thus, the reflected wave V<sub>r</sub> is almost the same magnitude as the incident wave. At the
 load, this condition only has the effect of giving an erroneous voltage assuming that
 the circuit was originally calibrated with a 50 Ω load. While nearly the entire signal
 is reflected back, this reflection is eliminated at the source because the source and
 the transmission line are matched.

Termination

Note

Parent topic:

Termination

Related concepts:

- Transmission Lines
- Characteristic Impedance
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=single-data-rate-sdr.html language=enus -->
## TOPIC 00120: Single Data Rate (SDR)

- bundle_id: `ni-hsdio`
- source_path: `single-data-rate-sdr.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/single-data-rate-sdr.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the data rate multiplier is configured for SDR operation, the digital waveform generator and analyzer generates or acquires data once per sample clock period. The relationship of the data to the Sample clock is determined by the data position.The following figure shows an example of SDR generat

### Single Data Rate (SDR)

When the data rate multiplier is configured for SDR operation, the digital waveform generator
 and analyzer generates or acquires data once per sample clock period. The relationship
 of the data to the Sample clock is determined by the data position.

The following figure shows an example of SDR generation configured for rising edge data
 position:

[IMAGE alt='image' src='GUID-1CC38990-C3E1-4EE4-9A28-57C33872DA29-a5.gif']

Parent topic:

Data Rate Multiplier

Related concepts:

- Data Rate Multiplier
- Data Position Settings

<!--NI_TOPIC bundle=ni-hsdio path=single-ended-logic-families.html language=enus -->
## TOPIC 00121: Single-Ended Logic Families

- bundle_id: `ni-hsdio`
- source_path: `single-ended-logic-families.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/single-ended-logic-families.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Single-ended logic families use standardized single-ended voltage levels. These voltage levels interpret voltage swings between the voltage that is driven by the device and the ground. The logic then returns a binary 1 or a binary 0. The following table shows examples of the voltage levels that are

### Single-Ended Logic Families

Single-ended logic families use standardized single-ended voltage levels. These voltage levels
 interpret voltage swings between the voltage that is driven by the device and the
 ground. The logic then returns a binary **1** or a binary
 **0**.

The following table shows examples of the voltage levels that are typical for
 single-ended logic families:

| Logic Family | Voltage Range |
| --- | --- |
| CMOS | 0 to 5 V |
| TTL | 0 to 5 V |
| LVTTL | 0 to 3.3 V |
| LVCMOS | 0 to 3.3 V |

The single-ended logic families for digital waveform generator and analyzers are named after the
 voltage that the device interprets as a binary **1** when
 configured for active drive generation.

These logic families include the following values:

- 1.2V
- 1.5V
- 1.8V
- 2.5V
- 3.3V
- 5.0V

Parent topic:

Logic Families

Related concepts:

- Single-Ended Voltage Levels
- Drive Type

<!--NI_TOPIC bundle=ni-hsdio path=single-ended-voltage-levels.html language=enus -->
## TOPIC 00122: Single-Ended Voltage Levels

- bundle_id: `ni-hsdio`
- source_path: `single-ended-voltage-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/single-ended-voltage-levels.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For single-ended devices, voltage levels are usually specified in terms of the voltage placed on the output terminal when driving a high level signal or when driving a low level signal, and by the voltage required on the input terminal for the signal to be recognized as a high or low level signal. F

### Single-Ended Voltage Levels

For single-ended devices, voltage levels are usually specified in terms of the voltage
 placed on the output terminal when driving a high level signal or when driving a low
 level signal, and by the voltage required on the input terminal for the signal to be
 recognized as a high or low level signal.

For the digital waveform generators and analyzers, the single-ended voltage levels are
 defined as follows:

- Generation Voltage High —When configured for active drive
 generation, this is the voltage produced at the channel electronics when the pattern
 generation engine generates a binary one. When configured for open
 collector generation, Generation Voltage High Level is equivalent to
 setting the data channel to a high-impedance state.
- Generation Voltage Low —The voltage produced at the channel
 electronics when the pattern generation engine generates a binary zero.
- Acquisition Voltage High —The pattern acquisition engine
 senses a binary 1 at or above this voltage level.
- Acquisition Voltage Low —The pattern acquisition engine senses
 a binary 0 at or above this voltage level.

Note

When connecting an digital waveform generator and analyzer to a Device Under Test (DUT),
 you must ensure that the interface voltage levels are compatible. The relationship
 between the single-ended voltage levels and the DUT voltage levels are shown in the
 following figure:

[IMAGE alt='image' src='GUID-BEA8CEA2-EFA0-4795-BDEB-380F82D2C49D-a5.gif']

To accurately communicate with a DUT, you must configure the module such that the
 following conditions are met:

- Generation Voltage High Level ³ DUT V<sub>IH</sub>
- Generation Voltage Low Level £ DUT V<sub>IL</sub>
- Acquisition Voltage High Level £ DUT V<sub>OH</sub>
- Acquisition Voltage Low Level ³ DUT V<sub>OL</sub>
- Acquisition Voltage High Level > Acquisition Voltage Low Level

The extra margin between the voltage level that is driven by the source and the voltage
 level that is required at the destination is called the Noise Immunity Margin (NIM). The
 NIM indicates the amount of noise tolerable on the connecting cable with a data bit
 being received in correctly. The total NIM is computed by the following formula:

N

I

M

=

m

i

n

G

e

n

e

r

a

t

i

o

n

V

o

l

t

a

g

e

H

i

g

h

-

D

U

T

V

I

H

,

G

e

n

e

r

a

t

i

o

n

V

o

l

t

a

g

e

L

o

w

-

D

U

T

V

I

L

,

D

U

T

V

O

H

-

A

q

u

i

s

i

t

i

o

n

V

o

l

t

a

g

e

H

i

g

h

,

D

U

T

V

O

L

-

A

q

u

i

s

i

t

i

o

n

V

o

l

t

a

g

e

L

o

w

The NI SHC68-C68-D4 shielded cable for single-ended high-speed digital signals provides
 excellent protection against external noise sources. If your system operates in a
 particularly noisy environment, some data bits might be incorrect. In such an
 environment, increase the NIM if possible.

Parent topic:

Voltage Levels

Related concepts:

- Open Collector
- Configuring Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=software-trigger.html language=enus -->
## TOPIC 00123: Software Trigger

- bundle_id: `ni-hsdio`
- source_path: `software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/software-trigger.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A software trigger is generated internally by a programmatic call for example, a LabVIEW VI or a C function. The trigger can occur at any time, depending on the conditions defined in the program.

### Software Trigger

A software trigger is generated internally by a programmatic call for example, a LabVIEW VI or a
 C function. The trigger can occur at any time, depending on the
 conditions defined in the program.

Parent topic:

Types of Triggers

<!--NI_TOPIC bundle=ni-hsdio path=static-acquisition.html language=enus -->
## TOPIC 00124: Static Acquisition

- bundle_id: `ni-hsdio`
- source_path: `static-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/static-acquisition.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Static acquisition samples the configured channels once, capturing their current state. Static acquisition, like static generation, is controlled by software and does not use hardware timing. Each data point requires a separate function call. Therefore, static acquisition is typically used for: Sing

### Static Acquisition

Static acquisition samples the configured channels once, capturing their current state. Static
 acquisition, like static generation, is controlled by software
 and does not use hardware timing.

Each data point requires a separate function call. Therefore, static
 acquisition is typically used for:

- Single-point measurements
- Low-speed applications

Static acquisition is useful for:

- System and cable debugging
- DC-level semiconductor testing
- Other diagnostic or low-speed applications

Static acquisition is also called immediate, unstrobed, or nonlatched
 acquisition.

Parent topic:

Acquisition

Related concepts:

- Static Generation

<!--NI_TOPIC bundle=ni-hsdio path=static-generation.html language=enus -->
## TOPIC 00125: Static Generation

- bundle_id: `ni-hsdio`
- source_path: `static-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/static-generation.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Static generation places a single pattern on the configured channels. Static generation, like static acquisition, is controlled by software and does not use hardware timing.Because a function call is required for each data point generated, static generation is generally used only for single-point or

### Static Generation

Static generation places a single pattern on the configured channels. Static generation, like
 static acquisition, is controlled by software and does not use hardware timing.

Because a function call is required for each data point generated, static generation is generally
 used only for single-point or low-speed applications. Static generation can be helpful
 in system and cable debugging, DC-level semiconductor testing, and many other
 applications.

Static generation is also called immediate, unstrobed, or nonlatched generation.

Parent topic:

Generation

Related concepts:

- Static Acquisition

<!--NI_TOPIC bundle=ni-hsdio path=strobe.html language=enus -->
## TOPIC 00126: STROBE

- bundle_id: `ni-hsdio`
- source_path: `strobe.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/strobe.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The STROBE channel on the DDC connector is a dedicated channel for the STROBE signal. STROBE can be used only for acquisition sessions. The data channels are sampled on the rising or falling edge of the STROBE signal, based on user selection, when STROBE is used as the sample clock. Using STROBE as

### STROBE

The STROBE channel on the DDC connector is a dedicated channel for the STROBE signal. STROBE can
 be used only for acquisition sessions.

The data channels are sampled on the rising or falling edge of the STROBE
 signal, based on user selection, when STROBE is used as the
 sample clock. Using STROBE as the sample clock ensures that the
 clock and data travel together through the same cable and system
 delays, keeping them time-aligned.

Digital waveform generators and analyzers have one onboard clock. The
 generation and acquisition sessions on the same device typically
 use the same sample clock rate. Selecting STROBE as the
 acquisition clock allows generation and acquisition to use
 separate timebases.

Parent topic:

Clocks

Related concepts:

- Sample Clock

Related information:

- Front Panel and Connector Pinout
- Clock Sources Summary 31
- Clock Sources Summary 30
- Clock Sources Summary
- Clock Sources Summary 32
- Clock Sources Summary 33

<!--NI_TOPIC bundle=ni-hsdio path=synchronizing-multiple-devices.html language=enus -->
## TOPIC 00127: Synchronizing Multiple Devices

- bundle_id: `ni-hsdio`
- source_path: `synchronizing-multiple-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/synchronizing-multiple-devices.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: For the digital waveform generators and analyzers, devices are synchronized through the following methods: Sample Clock Phase Alignment PXI Devices For PXI digital waveform generators and analyzers that use an internal clock source, the internal clock source can be phase aligned to the PXI_CLK10 sig

### Synchronizing Multiple Devices

For the digital waveform generators and analyzers, devices are synchronized through the following
 methods:

#### Sample Clock Phase Alignment

- PXI Devices

For PXI digital waveform generators and analyzers that use an internal clock
 source, the internal clock source can be phase aligned to the PXI_CLK10 signal on
 the backplane by selecting PXI_CLK10 as the Reference clock source. NI-TClk ensures
 that the Sample clock dividers on each PXI device are in phase for Sample clock
 alignment.

For PXI digital waveform generators and analyzers using an
 external clock source (CLK IN, STROBE, or PXI_STAR), ensure that the sample clocks
 are aligned when presented to the devices. If you are using PXI_STAR as the external
 clock source, the matched length traces on the PXI backplane assist in keeping the
 distributed sample clocks aligned. You can use a device like the PXI-5404 or
 PXI-6653 to distribute clocks on PXI_STAR.

- PXIe Devices

For PXIe digital waveform generator/analyzers using an internal clock source,
 the internal clock source can be phase aligned to the PXIe_CLK100 signal on the
 backplane by selecting PXIe_CLK100 as the Reference clock source. NI-TClk ensures
 that the Sample clock dividers on each PXIe device are in phase for sample clock
 alignment.

For PXIe digital waveform generators and analyzers using an
 external clock source (CLK IN or STROBE), ensure that the sample clocks are aligned
 when presented to the devices.

- PCI Devices

For PCI digital waveform generators and analyzers using an internal clock
 source, the internal clock source can be phase aligned to a 10 MHz reference signal
 on the RTSI 7 line of the RTSI connector. Configure the PCI device at one end of the
 RTSI cable to drive the onboard reference clock onto RTSI 7. Then configure all of
 the PCI devices to receive their reference clock from RTSI 7. NI-TClk ensures that
 the sample clock dividers on each device are in phase for sample clock
 alignment.

For PCI digital waveform generators and analyzers using an external
 clock source (CLK IN or STROBE), ensure that the sample clocks are aligned when
 presented to the devices.

#### Trigger Routing

The NI-TClk software uses the PXI trigger bus and RTSI
 bus lines to deterministically pass triggers between multiple digital waveform
 generator/analyzers. Refer to the multidevice NI-TClk examples for more information.
 Deterministic trigger routing ensures that all digital waveform generators and
 analyzers in the system start on the same sample.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-hsdio path=terminating-your-module.html language=enus -->
## TOPIC 00128: Terminating Your Module

- bundle_id: `ni-hsdio`
- source_path: `terminating-your-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/terminating-your-module.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this section to learn about terminated and unterminated configurations for acquisition and generation operations with the following device families: NI 654x NI 655x NI 656x Refer to Termination for more information about the theory and recommendations for system termination.

### Terminating Your Module

Expand this section to learn about terminated and unterminated configurations for acquisition and
 generation operations with the following device families:

- NI 654x
- NI 655x
- NI 656x

Refer to *Termination* for more information about the theory and recommendations for
 system termination.

Parent topic:

Integration and System Considerations

Related concepts:

- Terminating Your NI 654x
- Terminating Your NI 6551/6552
- Terminating Your NI 656x
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=terminating-your-ni-654x.html language=enus -->
## TOPIC 00129: Terminating Your NI 654x

- bundle_id: `ni-hsdio`
- source_path: `terminating-your-ni-654x.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/terminating-your-ni-654x.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this section to learn about the termination configurations for acquisition and generation with the NI 654x.Refer to Termination for more information about the theory and recommendations for system termination.

### Terminating Your NI 654x

Expand this section to learn about the termination configurations for acquisition and generation
 with the NI 654x.

Refer to *Termination* for more information about the theory and recommendations for
 system termination.

Parent topic:

Terminating Your Module

Related concepts:

- NI 654x Acquisition Termination
- NI 654x Generation Termination
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=terminating-your-ni-6551-6552.html language=enus -->
## TOPIC 00130: Terminating Your NI 6551/6552

- bundle_id: `ni-hsdio`
- source_path: `terminating-your-ni-6551-6552.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/terminating-your-ni-6551-6552.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this section to learn about the termination configurations for acquisition and generation with the NI 6551/6552.Refer to Termination for more information about the theory and recommendations for system termination.

### Terminating Your NI 6551/6552

Expand this section to learn about the termination configurations for acquisition and generation
 with the NI 6551/6552.

Refer to *Termination* for more information about the theory and recommendations for
 system termination.

Parent topic:

Terminating Your Module

Related concepts:

- NI 6551/6552 Acquisition Termination
- NI 6551/6552 Generation Termination
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=terminating-your-ni-6555-6556.html language=enus -->
## TOPIC 00131: Terminating Your NI 6555/6556

- bundle_id: `ni-hsdio`
- source_path: `terminating-your-ni-6555-6556.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/terminating-your-ni-6555-6556.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this section to learn about the termination configurations for acquisition and generation on the NI 6555/6556.Refer to Termination for more information about the theory and recommendations for system termination.

### Terminating Your NI 6555/6556

Expand this section to learn about the termination configurations for *acquisition*
 and *generation* on the NI 6555/6556.

Refer to *Termination* for more information about the theory and recommendations for
 system termination.

Parent topic:

Terminating Your Module

Related concepts:

- NI 6555/6556 Acquisition Termination
- NI 6555/6556 Generation Termination
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=terminating-your-ni-656x.html language=enus -->
## TOPIC 00132: Terminating Your NI 656x

- bundle_id: `ni-hsdio`
- source_path: `terminating-your-ni-656x.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/terminating-your-ni-656x.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this section to learn about the termination configurations for acquisition and generation with the NI 656x.Refer to Termination for more information about the theory and recommendations for system termination.

### Terminating Your NI 656x

Expand this section to learn about the termination configurations for *acquisition*
 and *generation* with the NI 656x.

Refer to *Termination* for more information about the theory and recommendations for
 system termination.

Parent topic:

Terminating Your Module

Related concepts:

- NI 656x Acquisition Termination
- NI 656x Generation Termination
- Termination

<!--NI_TOPIC bundle=ni-hsdio path=termination.html language=enus -->
## TOPIC 00133: Termination

- bundle_id: `ni-hsdio`
- source_path: `termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In high-speed digital systems, simple passive circuit elements might significantly affect signal quality. These elements include, for example, wires, cables, and chip PCB interconnections. High-speed digital edges contain frequency components that are several times the effective toggle rate of that

### Termination

In high-speed digital systems, simple passive circuit elements might significantly affect
 signal quality. These elements include, for example, wires, cables, and chip PCB
 interconnections. High-speed digital edges contain frequency components that are several
 times the effective toggle rate of that signal. For example, a digital edge with a rise
 time of 1.5 ns contains significant energy in frequencies up to 333 MHz, regardless of
 toggle rate.

When designing systems using digital waveform generators and analyzers, you must have a
 basic understanding of both transmission lines and termination so that you can maximize
 signal quality and minimize the effects of signal reflections.

The signals in the following figures show identical digital waveforms generated by an
 PXI-6552. The first figure shows a properly terminated waveform. In this case, the test
 system is designed by considering the effects of transmission lines and termination. The
 second figure shows a waveform from an unterminated system. In this case, the test
 system is designed without considering the effects of transmission lines and
 termination.

[IMAGE alt='image' src='GUID-D8C9BB2A-A6F3-47E0-99AC-562BDCAB184F-a5.gif']

When designing your test system, you must control the following key areas:

- Z s —The impedance at the source of the transmission line
- Z 0 —The characteristic AC impedance of the transmission line
- Z t —The impedance at the destination of the transmission line

If you do not control these elements, the signal becomes distorted. This results in the
 following issues:

- Signals that exceed specified high-level and low-level thresholds (overshoot and
 undershoot)
- Signals that have false edges (ringing)
- Signals that have reduced operating margins (degraded eye diagram caused by
 inter-symbol interference)
- Potential physical damage or overheating of driver/receiver components in extreme
 cases

Refer to *Terminating Your Module* for information about series and parallel
 resistor termination that is commonly applicable to your digital waveform
 generator/analyzer.

Related concepts:

- Transmission Lines
- Characteristic Impedance
- AC Waveform Characteristics
- Terminating Your Module

<!--NI_TOPIC bundle=ni-hsdio path=thermal-shutdown.html language=enus -->
## TOPIC 00134: Thermal Shutdown

- bundle_id: `ni-hsdio`
- source_path: `thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/thermal-shutdown.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-HSDIO 1.1 and later support thermal shutdown capabilities with digital waveform generators ans analyzers. These capabilities let your device detect high temperatures and shut down to prevent damage or poor performance. The following factors might influence device temperature: Air circulation path

### Thermal Shutdown

NI-HSDIO 1.1 and later support thermal shutdown capabilities with digital waveform generators ans
 analyzers. These capabilities let your device detect high temperatures and shut down to
 prevent damage or poor performance.

The following factors might influence device temperature:

- Air circulation paths
- Fan settings
- Space allowances

For more information on the temperature requirements, see the *Specifications*
 document of your device.

If you device powers down, the following error messages are shown:

- NI-HSDIO —NI-HSDIO returns an error when you use any of the functions
 that program the hardware or check hardware status, for example, the static
 acquisition and generation functions, commit functions, and self calibration
 function. Note This
 particular error code is not returned by niHSDIO_self_test (or
 the niHSDIO Self Test VI) because it can only return a 0 for pass or a nonzero
 value for fail.
- MAX —Measurement & Automation Explorer will return an error message if you run a 
self-test on your device after it exceeds the thermal shutdown temperature. The thermal 
shutdown error continues to be reported until the device is successfully reset.

To re-enable your device after thermal shutdown, complete the following steps:

1. Power down the computer or chassis that contains the module.
2. Ensure that you follow the guidelines in the Installing the Hardware section of the
 User Manual for your device at ni.com/docs .
3. Reset the device in one of the following ways: The thermal shutdown error is present until the device is reset.
  - calling niHSDIO_ResetDevice (or using the niHSDIO Reset
 Device VI)
  - performing a device reset in MAX

Parent topic:

Integration and System Considerations

Related information:

- Digital Waveform Generator/Analyzer
 Getting Started Guide

<!--NI_TOPIC bundle=ni-hsdio path=timing-and-triggering.html language=enus -->
## TOPIC 00135: Timing and Triggering

- bundle_id: `ni-hsdio`
- source_path: `timing-and-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/timing-and-triggering.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains the concepts and terminology related to timing and triggering.

### Timing and Triggering

This section explains the concepts and terminology related to timing and triggering.

Parent topic:

Digital Terminology

<!--NI_TOPIC bundle=ni-hsdio path=transmission-lines.html language=enus -->
## TOPIC 00136: Transmission Lines

- bundle_id: `ni-hsdio`
- source_path: `transmission-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/transmission-lines.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: At low frequencies (slow edge rates), small wires between devices do not affect system performance. You can assume the voltage is the same at every point along the wire at any moment. This is called "lumped" circuit model. As frequency increases, wire dimensions become comparable to signal wavelengt

### Transmission Lines

At low frequencies (slow edge rates), small wires between devices do not affect system
 performance. You can assume the voltage is the same at every point along the wire at any
 moment. This is called "lumped" circuit model.

As frequency increases, wire dimensions become comparable to signal wavelengths. In this
 case, even small inductance and capacitance create significant electrical impedance.

Generally, a significant proporation of the wavelength means that the propagation delay in a wire
 or interconnect is greater than one-sixth of the rise time of the digital signal. In
 this case, the "lumped" circuit analysis is incorrect and you must analyze the
 interconnect as a transmission line.

For calculation purposes, you must understand the concept of electrical length (l). Electrical
 length is defined as the distance that a signal can travel in an electrical medium
 during the time that it takes for one *rise or fall time*, whichever is
 longer.

Using the concept of electrical length, the general rule for what constitues a
 significant proportion of the wavelength can be redefined. The system must be analyzed
 as a transmission line if the physical length of a wire or electrical interconnect is
 greater than one-sixth of the electrical length of a signal that propagates on that
 wire.

Velocity is defined as the rate at which an electrical wave propagates in the transmission
 medium. Using this value you can calculate electrical length in one of the following
 ways:

- l(in) = Velocity(in/ns) • t rise
- l(in) = t rise (ns)/t pd (ns/in)

where,

t<sub>rise</sub> is the rise/fall time of the digital edge,

t<sub>pd</sub> is the propagation delay of the edge in the transmission line.

For example, the NI SHC68-C68-D2 shielded cable has a t<sub>pd</sub> of 165 ps/inch.

On an *NI 6551/6552* device, t<sub>rise</sub> for a high-speed digital signal
 can be as low as 1.5 ns.

Therefore, the electrical length is 9 in. (t<sub>rise</sub>/t<sub>pd</sub> =
  1.5/.165 = 9 in.), and any trace lengths longer than 1.5 in. (9 in./6) should be
 treated as a transmission line. This cable is significantly longer than 1.5 in., so this
 cable is considered to be a transmission line and designed the cable to have 50 Ω
 characteristic impedance.

Note

A voltage source (V<sub>s</sub>) generates a digital edge with an impedance of Z<sub>s</sub>
 looking "into" the transmission line. The transmission line itself has some low
 *characteristic AC impedance* (Z<sub>0</sub>) to ground, typically 50 Ω
 for most test systems. The end of the transmission line is most commonly terminated
 through an impedance (Z<sub>t</sub>) to ground at the destination.

The following figure shows a simple diagram of a basic single-ended transmission
 line:

[IMAGE alt='image' src='GUID-C86F69C1-30B1-41A5-BDBC-9BA3E98FDDFE-a5.gif']

Practically, termination at only one end of the transmission line is often adequate and is more
 commonly used. However, for high-precision applications, termination at both the source
 and the load end of the transmission line yields the best results.

Parent topic:

Termination

Related concepts:

- AC Waveform Characteristics
- Characteristic Impedance

<!--NI_TOPIC bundle=ni-hsdio path=triggers-summary.html language=enus -->
## TOPIC 00137: Triggers Summary

- bundle_id: `ni-hsdio`
- source_path: `triggers-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/triggers-summary.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes the triggers supported by digital waveform generator/analyzers. The Used In column indicates which types of operations can use a trigger type. The Supported Types column denotes which trigger types are valid for a given trigger. Using DDR mode has certain implications f

### Triggers Summary

The following table describes the triggers supported by digital waveform
 generator/analyzers. The Used In column indicates which types of operations can use a
 trigger type. The Supported Types column denotes which trigger types are valid for a
 given trigger.

Note

| Trigger Name | Used In | Supported Types | Description |
| --- | --- | --- | --- |
| Start | Acquisition, Generation | Digital Edge, Pattern Match, Software | The Start trigger transitions a device into a state where the device can respond to Sample clocks. For an acquisition session, this trigger transitions the device from a nonsampling state into a sampling state—the device starts sampling and storing data. For a generation session, this trigger transitions the device from an Idle state to a sample generation state—the device starts generating samples. |
| Reference | Acquisition | Digital Edge, Pattern Match, Software | The Reference trigger transitions a device from the Wait for Reference Trigger sampling state into the Post Reference trigger sampling state. In the Post Reference Trigger sampling state, a counter begins counting Sample clock cycles. When the configured number of samples is acquired, the device transitions into a Done state. In other words, the arrival of this trigger establishes the reference point that separates pretrigger and posttrigger samples. |
| Advance | Acquisition | Digital Edge, Pattern match, Software | The Advance trigger initiates the acquisition of the additional records in a multirecord acquisition. |
| Pause | Acquisition, Generation | Digital Level, Pattern Match | The Pause trigger indicates to the device that it should pause the acquisition or generation. Therefore, the Pause trigger is only effective when received during an active acquisition or generation session. For generation operations, the Data Active event indicates when the operation is paused. |
| Script | Generation | Digital Edge, Digital Level, Software | The Script trigger is a general-purpose trigger with a role that is entirely determined by the context of the dynamic generation script. A script allows you to create sophisticated dynamic generation operations. For example, the script could configure the device to generate waveform A, then wait for the Script trigger, then generate waveform B. You can create multiple Script triggers for use in your application. |
| Stop | Generation | Digital Edge, Software | The Stop Trigger stops active generation regardless of the the current state of the generation. The stop trigger is a request to stop, not an immediate synchronized trigger; therefore, it will take some clock cycles for the device to actually stop. The Stop Trigger is only valid for generation sessions and only available on the PXIe-6544/6545/6547/6548/6555/6556. |

Note

Parent topic:

Triggers

Related concepts:

- Double Data Rate (DDR)
- Acquisition Considerations for DDR
- Dynamic Acquisition
- Dynamic Generation
- Edge Trigger
- Pattern-Match Trigger
- Software Trigger
- Initial and Idle States
- Level Trigger
- Events Summary

<!--NI_TOPIC bundle=ni-hsdio path=triggers.html language=enus -->
## TOPIC 00138: Triggers

- bundle_id: `ni-hsdio`
- source_path: `triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/triggers.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Triggers are signals that cause the device to perform some action such as the starting, stopping, or pausing of an acquisition or generation operation. Triggers can be internal or external. External digital triggers come in various types. They can be re-exported and used with events to synchronize h

### Triggers

Triggers are signals that cause the device to perform some action such as the starting,
 stopping, or pausing of an acquisition or generation operation.

Triggers can be internal or external. External digital triggers come in various types.
 They can be re-exported and used with events to synchronize hardware operations with
 external circuits or other devices.

Parent topic:

Timing and Triggering

Related concepts:

- Types of Triggers
- Events
- Triggers Summary
- Events Summary

<!--NI_TOPIC bundle=ni-hsdio path=types-of-termination.html language=enus -->
## TOPIC 00139: Types of Termination

- bundle_id: `ni-hsdio`
- source_path: `types-of-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/types-of-termination.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The forms of line termination include the following: parallel series differential Parallel termination matches the characteristic impedance of the medium at the end of the line, squelching the wavefront at the destination (Z[t] = Z[0]). Differential termination is a variation of parallel termination

### Types of Termination

- parallel
- series
- differential

Parallel termination matches the characteristic impedance of the medium at the end of the line,
 squelching the wavefront at the destination (Z<sub>t</sub> = Z<sub>0</sub>).

Differential termination is a variation of parallel termination used for differential
 transmission lines. Many electrical standards, such as emitter-coupled logic (ECL) and
 *LVDS*, require that traces are routed differentially. As such, parallel
 termination is used between the two modes of the differential trace.

Series termination places series impedance equal to the characteristic impedance at the source of
 the transmission line. This termination prevents the source from re-reflecting any
 reflections from an unterminated transmission line. It also prevents reflections from
 the transmission line to the source at the entry (Z<sub>S</sub> = Z<sub>0</sub>).

Practically, termination at only one end of the transmission line is often adequate and is more
 commonly used.

Parent topic:

Termination

Related concepts:

- Characteristic Impedance
- Differential Logic Families

<!--NI_TOPIC bundle=ni-hsdio path=types-of-triggers.html language=enus -->
## TOPIC 00140: Types of Triggers

- bundle_id: `ni-hsdio`
- source_path: `types-of-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/types-of-triggers.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the triggers supported by your digital waveform generator/analyzer as one of the following trigger types: Edge Level Pattern Match Software Individual triggers may not support all the trigger types listed here. Refer to Triggers Summary for more information.

### Types of Triggers

You can configure the triggers supported by your digital waveform generator/analyzer as one of
 the following trigger types:

- Edge
- Level
- Pattern Match
- Software

Note

Triggers
 Summary

Parent topic:

Triggers

Related concepts:

- Edge Trigger
- Level Trigger
- Pattern-Match Trigger
- Software Trigger
- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio path=user-manual-welcome.html language=enus -->
## TOPIC 00141: NI-HSDIO User Manual

- bundle_id: `ni-hsdio`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-HSDIO User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-HSDIO
 User Manual

The NI-HSDIO User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ni-hsdio path=using-attributes-with-ni-hsdio.html language=enus -->
## TOPIC 00142: Using Attributes with NI-HSDIO

- bundle_id: `ni-hsdio`
- source_path: `using-attributes-with-ni-hsdio.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-attributes-with-ni-hsdio.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Attributes, which are typically called properties in LabVIEW, serve as a base for parameters.NI-HSDIO contains high-level functions that set most of the instrument attributes. Some attributes are not accessible through the high-level functions. For example, input impedance is not set with any of the

### Using Attributes with NI-HSDIO

Attributes, which are typically called properties in LabVIEW, serve as a base for parameters.

NI-HSDIO contains high-level functions that set most of the instrument attributes. Some
 attributes are not accessible through the high-level functions. For example, input
 impedance is not set with any of the NI-HSDIO configuration functions. The values for
 these attributes must be set using the attribute.

Some NI-HSDIO properties are channel based. When a property is channel based, you must specify an
 active channel before setting, getting, or checking properties.

#### Accessing Attributes

In LabVIEW, you can find attributes in the NI-HSDIO
 property node. To access them, complete the following steps:

1. Open a VI.
2. Make sure that you are viewing the block diagram. Navigate to the NI-HSDIO
 palette at All Functions»NI Measurements»NI-HSDIO»Static and Dynamic
 Acquisition or All
 Functions»NI Measurements»NI-HSDIO»Static and Dynamic
 Generation .
3. Drag the property node icon to the block diagram.
4. Left-click the property node, and select the attribute you want to use.
5. Resize the property node to add additional attributes.

In C, attributes are accessed with the niHSDIO Set and Get Attribute functions.
 These functions correspond to a particular data type. For example, to set the input
 impedance, which has a data type or ViReal64, use
 niHSDIO_SetAttributeViReal64.

Refer to the *Function
 Reference* section for a complete listing of available attributes and
 properties.

#### Setting Properties and Attributes Before Reading Them

Properties and
 attributes are modified when you set them or when you call a configuration VI or
 function that sets them, respectively. It is important to set the properties or
 attributes or call any configuration VIs or functions before reading back any
 property or attribute values for the following reasons:

- Values read are forced depending on the current configuration of the session. If
 you read a property or attribute value and then set other properties or
 attributes, the value read might no longer be valid.
- The driver verifies that the configuration of the device is valid at the time
 the property or attribute is read. It is possible to get an error when reading a
 property or attribute if the configuration is not valid at that point, even when
 a setting later might make it valid.
- Reading properties or attributes causes the driver to verify the current
 configuration. If you change some of the settings later, those settings must be
 validated again.

Note

Parent topic:

Programming Flow

Related concepts:

- Configuring Input Impedance

<!--NI_TOPIC bundle=ni-hsdio path=using-ni-hsdio-in-labview.html language=enus -->
## TOPIC 00143: Using NI-HSDIO in LabVIEW

- bundle_id: `ni-hsdio`
- source_path: `using-ni-hsdio-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-ni-hsdio-in-labview.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the LabVIEW ADE to manage your code development and that you are familiar with the ADE.To develop an NI-HSDIO application in LabVIEW, follow these general steps: Open an existing or new LabVIEW VI. From the Function Palette, locate the NI-HSDIO VIs at NI Measure

### Using NI-HSDIO in LabVIEW

This topic assumes that you are using the LabVIEW ADE to manage your code development and that
 you are familiar with the ADE.

To develop an NI-HSDIO application in LabVIEW, follow these general steps:

1. Open an existing or new LabVIEW VI.
2. From the Function Palette, locate the NI-HSDIO VIs at NI Measurements»NI-HSDIO .
3. Select the VIs that you want to use and drop them on the block diagram to build your application.

#### Example Programs for LabVIEW

If you are using LabVIEW 7.1 or later, you
 can use the Example Finder to search or browse examples. NI-HSDIO examples are
 classified by keyword, so you can search for a particular device or measurement
 function.

To browse the NI-HSDIO examples available in LabVIEW, launch
 LabVIEW, click Open»Examples, and navigate to
 Hardware Input and Output»Modular Instruments»NI-HSDIO.
 You can also access the examples using the Start menu, by selecting
 Start»All Programs»National
 Instruments»NI-HSDIO»Examples.

Parent topic:

Getting Started with NI-HSDIO

<!--NI_TOPIC bundle=ni-hsdio path=using-ni-hsdio-in-labwindows-cvi.html language=enus -->
## TOPIC 00144: Using NI-HSDIO in LabWindows/CVI

- bundle_id: `ni-hsdio`
- source_path: `using-ni-hsdio-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-ni-hsdio-in-labwindows-cvi.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the LabWindows™/CVI™ ADE to manage your code development and that you are familiar with the ADE.To develop an NI-HSDIO application in LabWindows/CVI, follow these general steps: Open an existing or new project file. Load the NI-HSDIO function panel from the loca

### Using NI-HSDIO in LabWindows/CVI

This topic assumes that you are using the LabWindows™/CVI™ ADE to manage your code development
 and that you are familiar with the ADE.

To develop an NI-HSDIO application in LabWindows/CVI, follow these general steps:

1. Open an existing or new project file.
2. Load the NI-HSDIO function panel from the location specified in the NI-HSDIO Instrument Driver Readme .
3. Use the function panel to navigate the function hierarchy and generate function calls with the proper syntax and variable values.

#### Example Programs for LabWindows/CVI

If you
 are using LabWindows/CVI 7.1 or later, you can use the Example Finder to search or
 browse examples. NI-HSDIO examples are classified by keyword, so you can search for
 a particular device or measurement function.

To browse the NI-HSDIO examples
 available in LabWindows/CVI, launch LabWindows/CVI, select Help»NI
 Example Finder, and navigate to Hardware Input and
 Output»Modular Instruments»NI-HSDIO. You can also acess the examples
 using the Start menu, by selecting Start»All Programs»National
 Instruments»NI-HSDIO»Examples.

Parent topic:

Getting Started with NI-HSDIO

Related information:

- NI-HSDIO 18.0 Readme

<!--NI_TOPIC bundle=ni-hsdio path=using-ni-hsdio-in-visual-c-and-c.html language=enus -->
## TOPIC 00145: Using NI-HSDIO in Visual C and C++

- bundle_id: `ni-hsdio`
- source_path: `using-ni-hsdio-in-visual-c-and-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-ni-hsdio-in-visual-c-and-c.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code development.To develop an NI-HSDIO application with Microsoft Visual C++ 6.0, follow these general steps: Open an existing or new Visual C/C++ project to manage your application code. Create source code files

### Using NI-HSDIO in Visual C and C++

This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code
 development.

To develop an NI-HSDIO application with Microsoft Visual C++ 6.0, follow these general steps:

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include "nihsdio.h"
5. Add the NI-HSDIO include and library files to the project. <IVIROOTDIR32> 
 is an alias to a specific National Instruments file folder location. Refer to the
 NI-HSDIO Readme for more information about installed file locations. Tip You can modify an NI-HSDIO C
 example to create an application, and all required include and library files are added to
 the project for you.
  1. Select Project»Settings»C/C++»Preprocessor»Additional include
 directories , and add the paths, separated by a semicolon, to the
 nihsdio.h and visa.h files. The
 nihsdio.h and visa.h files are located in the
 <IVIROOTDIR32>\Include and
 <VXIPNPPATH>\WinNT\Visa\include directories, respectively.
  2. Select Project»Link»General»Object/Library Modules , and add
 nihsdio.lib .
  3. Select Project»Link»Input»Additional library path , and add the
 path to the nihsdio.lib file. The nihsdio.lib file is
 located in the <IVIROOTDIR32>\Lib\msc or the
 <IVIROOTDIR32>\Lib x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Creating an Application with Microsoft Visual Studio
 2010

To develop an NI-HSDIO application with Microsoft Visual Studio 2010, follow
 these general steps:

1. Open an existing or new Visual C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp 
 (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include "nihsdio.h"
5. Add the NI-HSDIO include and library files to the project.
 <IVIROOTDIR32> is an alias to a specific National Instruments
 file folder location. Refer to the NI-HSDIO Readme for more information about
 installed file locations.
  1. Select Project»Properties»Configuration
 Properties»C/C++»General»Additional Include Directories , add the paths,
 separated by a semicolon, to the nihsdio.h and
 visa.h files. The nihsdio.h and
 visa.h files are located in the
 <IVIROOTDIR32>\Include and
 <VXIPNPPATH>\WinNT\Visa\include directories, respectively.
  2. Select Linker»Input»Additional Dependencies , and add
 nihsdio.lib .
  3. Select Linker»General»Additional Dependencies , and add the
 path to the nihsdio.lib file. The nihsdio.lib file
 is located in the <IVIROOTDIR32>\Lib\msc or the
 <IVIROOTDIR32>\Lib x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Microsoft Visual C and Visual C++ Examples

The
 C examples were built and tested using Microsoft Visual C++ 6.0 with Service Pack 5.0. These
 examples are console-based with no graphical interface.

To build the examples in Microsoft
 Visual C++ 6.0 using the Microsoft NMAKE utility, complete the following steps:

1. Go to the directory for the particular example you want to use.
2. Run the VCVARS32.BAT batch file (located in the \bin 
 directory of the MSVC compiler) to set up the environment variables for command line usage if
 they are not already set. You might need to increase the initial environment size of the DOS
 box to accommodate the added environment variables.
3. To build an example, run nmake examplename.mak . The executable is built to
 the debug subdirectory by default.

To build the examples in Microsoft Visual C++ 6.0 using the Microsoft Developer Studio
 workspace, complete the following steps:

1. Go to the directory for the example you want to use.
2. Open the project workspace file ( .dsw ) that launches Developer Studio. You
 can find the installed location of this file in the NI-HSDIO Readme .
3. Build the example.

Parent topic:

Getting Started with NI-HSDIO

Related concepts:

- Programming Flow

<!--NI_TOPIC bundle=ni-hsdio path=using-the-ni-digital-waveform-editor.html language=enus -->
## TOPIC 00146: Using the Digital Waveform Editor

- bundle_id: `ni-hsdio`
- source_path: `using-the-ni-digital-waveform-editor.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-the-ni-digital-waveform-editor.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Digital Waveform Editor (DWE) provides a simple way to create source data for your digital waveform generation application. Refer to ni.com/catalog for more information about how you can purchase this software.

### Using the Digital Waveform Editor

The Digital Waveform Editor (DWE) provides a simple way to create source data for your digital
 waveform generation application. Refer to
 *ni.com/catalog* for more information
 about how you can purchase this software.

[IMAGE alt='image' src='GUID-A6D74535-49D7-4446-8A51-D91E8646DF70-a5.gif']

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-hsdio path=using-the-standard-functionality-for-error-in.html language=enus -->
## TOPIC 00147: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-hsdio`
- source_path: `using-the-standard-functionality-for-error-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-the-standard-functionality-for-error-in.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

error in

error in

Note

error in

error in

|  | Error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | Status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | Code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | Source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

Parent topic:

Using NI-HSDIO in LabVIEW

<!--NI_TOPIC bundle=ni-hsdio path=using-the-standard-functionality-for-error-ou.html language=enus -->
## TOPIC 00148: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-hsdio`
- source_path: `using-the-standard-functionality-for-error-ou.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/using-the-standard-functionality-for-error-ou.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs and functions contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs and functions contain an error out
 parameter you can use to manage errors. These parameters typically provide the same,
 standard functionality. When a node exhibits different parameter functionality, the
 exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | Error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

Error out contains the following cluster elements:

|  | Status is TRUE (X) if an error occurred before or during the running of this node; status is FALSE (checkmark) to indicate a warning or that no error occurred before or during the running of this node. |
| --- | --- |
|  | Code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | Source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

Parent topic:

Using NI-HSDIO in LabVIEW

<!--NI_TOPIC bundle=ni-hsdio path=voltage-levels.html language=enus -->
## TOPIC 00149: Voltage Levels

- bundle_id: `ni-hsdio`
- source_path: `voltage-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/voltage-levels.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital devices have voltage levels specified for normal operation of their acquisition and generation operations. Voltage levels define how a device determines a valid logic state (logic high level or logic low level). Voltage levels are defined differently for single-ended and differential devices

### Voltage Levels

Digital devices have voltage levels specified for normal operation of their acquisition and
 generation operations. Voltage levels define how a device determines a valid logic state
 (logic high level or logic low level).

Voltage levels are defined differently for *single-ended* and
 *differential* devices.

Related concepts:

- Single-Ended Voltage Levels
- Differential Voltage Levels

<!--NI_TOPIC bundle=ni-hsdio path=waveforms.html language=enus -->
## TOPIC 00150: Waveforms

- bundle_id: `ni-hsdio`
- source_path: `waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/waveforms.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: User-generated data patterns are stored to the device onboard memory as waveforms. These waveforms are arrays of every sample that the device generates in the order they are generated.Generated waveforms are assigned a name when they are stored in onboard memory. This name allows you to store or del

### Waveforms

User-generated data patterns are stored to the device onboard memory as waveforms. These
 waveforms are arrays of every sample that the device generates
 in the order they are generated.

Generated waveforms are assigned a name when they are stored in onboard memory. This name allows
 you to store or delete multiple waveforms from the device memory and refer to them
 easily for simple generation or for complex scripts. When the generation session is
 closed, the waveforms are removed from onboard memory.

Parent topic:

Dynamic Generation

Related concepts:

- Onboard Memory

<!--NI_TOPIC bundle=ni-hsdio path=writing-waveforms-to-your-device.html language=enus -->
## TOPIC 00151: Writing Waveforms to Your Device

- bundle_id: `ni-hsdio`
- source_path: `writing-waveforms-to-your-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio/raw/resource/enus/writing-waveforms-to-your-device.html
- document_id: `ni-hsdio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you can generate any data, you must write your waveform(s) to the device onboard memory. Use the Write Named Waveform VIs and functions to write waveform data from your PC memory to your onboard device memory. The Write Named Waveform VIs and functions are shown in the following table: LabVIE

### Writing Waveforms to Your Device

Before you can generate any data, you must write your waveform(s) to the device onboard memory.
 Use the Write Named Waveform VIs and functions to write waveform data from your PC
 memory to your onboard device memory.

The Write Named Waveform VIs and functions are shown in the following table:

| LabVIEW VIs | C Functions |
| --- | --- |
| Use one of the following instances of the niHSDIO Write Named Waveform polymorphic VI: niHSDIO Write Named Waveform (U32) niHSDIO Write Named Waveform (U16) niHSDIO Write Named Waveform (U8) niHSDIO Write Named Waveform (WDT) niHSDIO Write Named Waveform From File (HWS) | niHSDIO_WriteNamedWaveformU32 niHSDIO_WriteNamedWaveformU16 niHSDIO_WriteNamedWaveformU8 niHSDIO_WriteNamedWaveformWDT niHSDIO_WriteNamedWaveformFromFileHWS |

niHSDIO Configure Waveform To Generate

niHSDIO_ConfigureWaveformToGenerate

Initiate

generate

Note

Programming»Reference»Script Instructions

generate

niHSDIO_AllocateNamedWaveform

Note

niHSDIO_WriteNamedWaveformFromFileHWS

Refer to the following code snippets for an example of writing a 1 MS waveform to onboard memory
 in LabVIEW and in C.

[IMAGE alt='image' src='GUID-3563D510-76A9-4B7F-AF04-91032D640CCB-a5.gif']

```text
#define BLOCK_SIZE         8192 
ViUInt32 data[BLOCK_SIZE];
.
.
.
niHWS_OpenFile("mydata.hws", niHWS_Val_ReadOnly, &fileHandle);
niHWS_GetWfmReference (fileHandle, VI_NULL, VI_NULL, &wfmRef);
/* reserve onboard memory, name the waveform "myWfm" */
niHWS_GetWfmI32Attribute (wfmRef, niHWS_Attr_WaveformSize, &wfmSize);
niHSDIO_AllocateNamedWaveform (instrHdl, "myWfm", wfmSize);
/* write waveform 1 block at a time */
numSamplesWritten = 0;
while (numSamplesWritten <= wfmSize)
{
 /* Read BLOCK_SIZE samples from .hws file, put in data */
 niHWS_ReadDigitalU32(wfmRef, BLOCK_SIZE, data, &actualSamplesRead);
 niHSDIO_WriteNamedWaveformU32 (instrHdl, "myWfm", actualSamplesRead, data);
 numSamplesRead = numSamplesRead + actualSamplesRead;
}
.
.
.
```

Note

If you try to write past the end of a
 waveform, NI-HSDIO returns an error.

The digital waveform generator/analyzers support writing waveforms according to the following
 standards:

| NI 654x/655x devices | Require waveform blocks be multiples of 32 samples when writing to preallocated waveforms. The overall waveform size does not have this restriction, but it must be even. |
| --- | --- |
| NI 656x devices | Require blocks be multiples of 64 samples when writing to preallocated waveforms. The overall waveform size does not have this restriction, but it must be a multiple of four (or a multiple of eight if in DDR mode). |

The last call to Write Named Waveform VI should write enough data to fill the waveform.

Parent topic:

Generating Dynamic Data

Related concepts:

- Generation Onboard Memory
- Initiate and Fetch
