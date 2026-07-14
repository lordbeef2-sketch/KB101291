# NI DOCUMENT BUNDLE: ni-dmm

<!--NI_BUNDLE_CHUNK bundle=ni-dmm start=251 end=473 -->
<!--NI_TOPIC bundle=ni-dmm path=high-voltages.html language=enus -->
## TOPIC 00251: High Voltages

- bundle_id: `ni-dmm`
- source_path: `high-voltages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/high-voltages.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: All cables, connectors, and fixtures used in your system must have specifications to handle with an adequate safety margin 1000 V signals for the NI 4071 and 300 V signals for the NI 4065 and NI 4070/4072.When switching high-voltage signals, the parasitic capacitance of the cable connecting the NI

### High Voltages

Caution

When switching high-voltage signals, the parasitic capacitance of the cable connecting the NI 4065 and NI 4070/4071/4072 with the switches, as well as the input capacitance of the instrument, needs to be charged to the source voltage. Depending on the voltage present at the DMM input during the measurement on the previous channel, a significant current can flow from the high–voltage source to charge this capacitance.

This current transient does not cause any degradation effect on the NI 4065 and NI 4070/4071/4072, but this action, referred to as hot switching, can reduce the life of the switches. Refer to Handling High DC Voltages for more information about the degradation effect, and refer to the switch documentation for information about extending switch life.

When switching high-voltage signals into a low-voltage range of any DMM (such as applying 300 V on the 10 V range), the input impedance is lower than it is when the proper range is selected. Repetitive operations such as these may shorten switch life. To maximize switch life, always select a measurement range that can handle the maximum voltage expected.

Remember that you might need to increase the settling time of your measurement. Consider the following illustration showing a DMM connected to a 100 V DC source, a thermocouple, and device under test (DUT) through a multiplexing switch.

[IMAGE alt='image' src='GUID-744A3D66-39D1-4E6A-A35D-4F95F2CC39B7-a5.svg']

For example, assume you are switching from the 100 V range to the 100 mV range and want to obtain the best sensitivity using the thermocouple. When the switch module advances from the 100 V channel to a thermocouple channel, the input signal conditioning of the DMM (along with the cabling, switching module, and so on) must discharge any stray capacitance from 100 V to 100 µV. If you need a sensitivity of 1 µV from the low–voltage channel, the system must settle from 100 V to 1 µV (10 parts per billion, or eight decades).

When you require resolutions better than 10 ppm, dielectric absorption is a major factor.

Depending upon the source resistance (R), system capacitance (C), and dielectric qualities of the system components, you must allow more settling time in this example. In practice, you may need to allow settling times of 10 ms or more in situations where you are switching high voltages (>30 V).

Parent topic:

Switching Voltages

Related concepts:

- Handling High DC Voltages
- Dielectric Absorption

<!--NI_TOPIC bundle=ni-dmm path=initialize.html language=enus -->
## TOPIC 00252: Initialize

- bundle_id: `ni-dmm`
- source_path: `initialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/initialize.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: For any application you write, you need to open a session to establish communication with the DMM by using niDMM Initialize or niDMM Initialize with Options. Do not confuse niDMM Initialize with niDMM Initiate. niDMM Initiate is used to start an asynchronous acquisition.In addition to establishing

### Initialize

For any application you write, you need to open a session to establish communication with the DMM by using niDMM Initialize or niDMM Initialize with Options.

Tip

In addition to establishing a session with the DMM, niDMM Initialize also sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. niDMM Initialize can also perform a number of additional tasks such as verifying that the instrument driver is valid for the instrument and resetting the DMM to a known state. niDMM Initialize returns a ViSession handle that you use to identify the instrument in all subsequent NI-DMM calls.

niDMM Initialize and niDMM Initialize With Options create a new session. Repeated calls to niDMM Initialize for the same resource returns the existing session. You can use the same session in multiple program threads.

niDMM Initialize With Options performs all the functionality of niDMM Initialize and optionally sets the initial state of the DMM. With niDMM Initialize With Options, you can configure range checking, caching, coercion recording, simulation, and status reporting.

Parent topic:

Programming Flow

Related concepts:

- Simulating NI Digital Multimeters

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=input-coupling.html language=enus -->
## TOPIC 00253: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-coupling_2.html language=enus -->
## TOPIC 00254: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-coupling_3.html language=enus -->
## TOPIC 00255: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-coupling_4.html language=enus -->
## TOPIC 00256: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-coupling_5.html language=enus -->
## TOPIC 00257: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-coupling_6.html language=enus -->
## TOPIC 00258: Input Coupling

- bundle_id: `ni-dmm`
- source_path: `input-coupling_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-coupling_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC s

### Input Coupling

The input channels can be configured for DC coupling or AC coupling. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal. Use AC coupling to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power supply. Refer to the specifications for input limits that must be observed regardless of coupling.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=input-resistance.html language=enus -->
## TOPIC 00259: Input Resistance

- bundle_id: `ni-dmm`
- source_path: `input-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/input-resistance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resistance is a measure of the opposition to the flow of current. The input resistance of the DMM can affect the accuracy of voltage measurements, particularly when the resistance of the source voltage is comparable to the input resistance of the DMM. For example, assume a DMM with a 10 MΩ input res

### Input Resistance

Resistance is a measure of the opposition to the flow of current. The input resistance of the DMM can affect the accuracy of voltage measurements, particularly when the resistance of the source voltage is comparable to the input resistance of the DMM.

For example, assume a DMM with a 10 MΩ input resistance measures a 9 V source voltage with a series resistance of 50 Ω while in a 10 V DC range, as represented in the following figure.

[IMAGE alt='image' src='GUID-B3392445-05DB-469C-B4F6-C8DD327995D7-a5.svg']

Using the following formula, you can determine the approximate value returned by the DMM:

V<sub>M</sub> = V<sub>S</sub> *[(R<sub>in</sub>)/(R<sub>S</sub> + R<sub>in</sub>)]

where V<sub>M</sub> is the voltage measured by the DMM, V<sub>S</sub> is source voltage, R<sub>in</sub> is the input resistance of the DMM, and R<sub>S</sub> is external source resistance.

V<sub>M</sub> = (9 V * 10 M Ω)/(50 Ω + 10 M Ω)

V<sub>M</sub> = 8.99996 V

Another example is to assume a DMM with a 10 MΩ input resistance measures a 9 V source voltage with a series resistance of 1 M Ω while in a 10 V DC range, as represented in the following figure.

[IMAGE alt='image' src='GUID-39236626-BE3E-4340-BDF7-DC03B868E4AB-a5.svg']

Using the same formula, you can determine the approximate value returned by the DMM.

V<sub>M</sub> = (9 V * 10 M Ω)/(1 M Ω + 10 M Ω)

V<sub>M</sub> = 8.18182 V

When measuring the source voltage with a low source resistance, the DMM returns a value that was accurate to within ±0.0005%, or 5 ppm, and the same source voltage with a high resistance returns a value that was accurate to within ±10%, or 100,000 ppm.

NI 4065 and NI 4070/4071/4072 users can select the input resistance for DC voltage measurements.

Refer to the *Shunt Resistors* section and *Burden Voltage*
 section for more information on shunt resistance in current mode.

Parent topic:

Measurement Considerations

Related concepts:

- DC Voltage
- Burden Voltage

<!--NI_TOPIC bundle=ni-dmm path=instrumentstudio.html language=enus -->
## TOPIC 00260: InstrumentStudio

- bundle_id: `ni-dmm`
- source_path: `instrumentstudio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/instrumentstudio.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduced in NI-DMM 18.1 When you install NI‑DMM, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device types, incl

### InstrumentStudio

Introduced in NI-DMM 18.1

When you install NI‑DMM, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device types, including DMMs, in a single program.

Note

InstrumentStudio is automatically installed when you install the NI‑DMM driver. You can access InstrumentStudio in one of the following ways:

- From the Windows start menu, select National Instruments»InstrumentStudio [year] . This launches InstrumentStudio and runs a soft front panel populated with devices detected on your system.
- From Measurement & Automation Explorer (MAX), select a device and then click Test Panels... . This launches InstrumentStudio and runs a soft front panel for the device you selected.

For more information on using InstrumentStudio, refer to the InstrumentStudio Manual.

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=integration-and-system-considerations.html language=enus -->
## TOPIC 00261: Integration and System Considerations

- bundle_id: `ni-dmm`
- source_path: `integration-and-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/integration-and-system-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section includes information related to integrating your DMM with other devices and environments.

### Integration and System Considerations

This section includes information related to integrating your DMM with other devices and environments.

<!--NI_TOPIC bundle=ni-dmm path=labview-trigger-routing.html language=enus -->
## TOPIC 00262: LabVIEW Trigger Routing

- bundle_id: `ni-dmm`
- source_path: `labview-trigger-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/labview-trigger-routing.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following tables show which values are supported by NI DMMs. 17 Measurement Complete Destination Destination Description Device NI PXIe-408x NI PXI-407x NI PCI-4070 NI PXI-4065 NI PCI/PCIe/USB-4065 NONE (default) No destination specified √ √ √ √ √ EXTERNAL Pin 6 on the AUX Connector — √ √ √ √ TT

### LabVIEW Trigger Routing

The following tables show which values are supported by NI DMMs.

| Destination | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| NONE (default) | No destination specified | √ | √ | √ | √ | √ |
| EXTERNAL | Pin 6 on the AUX Connector | — | √ | √ | √ | √ |
| TTL0 | PXI Trigger Line 0 | √ | √ | — | √ | — |
| TTL1 | PXI Trigger Line 1 | √ | √ | — | √ | — |
| TTL2 | PXI Trigger Line 2 | √ | √ | — | √ | — |
| TTL3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| TTL4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| TTL5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| TTL6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| PXI_TTL7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| LBR TRIG 0 | Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis | — | √2 | — | — | — |

| Source | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| IMMEDIATE (default) | No trigger specified | √ | √ | √ | √ | √ |
| EXTERNAL | Pin 9 on the AUX Connector | — | √ | √ | √ | √ |
| SOFTWARE | Configures the DMM to wait until niDMM Send Software Trigger is called | √ | √ | √ | √ | √ |
| TTL0 | PXI Trigger Line 0 | √ | √ | √1 | √ | — |
| TTL1 | PXI Trigger Line 1 | √ | √ | √1 | √ | — |
| TTL2 | PXI Trigger Line 2 | √ | √ | √1 | √ | — |
| TTL3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| TTL4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| TTL5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| TTL6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| TTL7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| PXI STAR | PXI STAR Trigger Line | — | √ | — | √ | — |
| LBR TRIG 1 | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis | — | √2 | — | — | — |
| AUX TRIG 1 | Pin 3 on the AUX Connector | — | √ | — | √ | √ |

| Source | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| IMMEDIATE (default) | No trigger specified | √ | √ | √ | √ | √ |
| EXTERNAL | Pin 9 on the AUX Connector | — | √ | √ | √ | √ |
| SOFTWARE TRIG | Configures the DMM to wait until niDMM Send Software Trigger is called | √ | √ | √ | √ | √ |
| INTERVAL | Interval Trigger |  | √ | √ | √ | √ |
| TTL0 | PXI Trigger Line 0 | √ | √ | √1 | √ | — |
| TTL1 | PXI Trigger Line 1 | √ | √ | √1 | √ | — |
| TTL2 | PXI Trigger Line 2 | √ | √ | √1 | √ | — |
| TTL3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| TTL4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| TTL5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| TTL6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| TTL7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| PXI STAR | PXI STAR Trigger Line | — | √ | — | √ | — |
| LBR TRIG 1 | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis | — | √2 | — | — | — |
| AUX TRIG 1 | Pin 3 on the AUX Connector | — | √ | — | √ | √ |

<sup>1</sup>Lines TTL0, TLL1, and TTL2 refer to the device interconnect on the NI
 PCI-4070.

<sup>2</sup>Refer to the chassis section for more information regarding limitations
 of using this feature.

Parent topic:

Triggering

Related concepts:

- Chassis

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=labwindowscvi-trigger-routing.html language=enus -->
## TOPIC 00263: LabWindows/CVI Trigger Routing

- bundle_id: `ni-dmm`
- source_path: `labwindowscvi-trigger-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/labwindowscvi-trigger-routing.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following tables show which values are supported by NI DMMs. 14 NIDMM_ATTR_MEAS_COMPLETE_DESTINATION Destination Description Device NI PXIe-408x NI PXI-407x NI PCI-4070 NI PXI-4065 NI PCI/PCIe/USB-4065 NIDMM_VAL_NONE (default) No destination specified √ √ √ √ √ NIDMM_VAL_EXTERNAL Pin 6 on the AU

### LabWindows/CVI Trigger Routing

The following tables show which values are supported by NI DMMs.

| Destination | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| NIDMM_VAL_NONE (default) | No destination specified | √ | √ | √ | √ | √ |
| NIDMM_VAL_EXTERNAL | Pin 6 on the AUX Connector | — | √ | √ | √ | √ |
| NIDMM_VAL_PXI_TRIG0 | PXI Trigger Line 0 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG1 | PXI Trigger Line 1 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG2 | PXI Trigger Line 2 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| NIDMM_VAL_LBR_TRIG0 | Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis | — | √2 | — | — | — |

| Source | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| NIDMM_VAL_IMMEDIATE (default) | No trigger specified | √ | √ | √ | √ | √ |
| NIDMM_VAL_EXTERNAL | Pin 9 on the AUX Connector | — | √ | √ | √ | √ |
| NIDMM_VAL_SOFTWARE_TRIG | Configures the DMM to wait until niDMM_SendSoftwareTrigger is called | √ | √ | √ | √ | √ |
| NIDMM_VAL_PXI_TRIG0 | PXI Trigger Line 0 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG1 | PXI Trigger Line 1 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG2 | PXI Trigger Line 2 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_STAR | PXI STAR Trigger Line | — | √ | — | √ | — |
| NIDMM_VAL_LBR_TRIG1 | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis | — | √2 | — | — | — |
| NIDMM_VAL_AUX_TRIG1 | Pin 3 on the AUX Connector | — | √ | — | √ | √ |

| Source | Description | Device |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NI PXIe-408x | NI PXI-407x | NI PCI-4070 | NI PXI-4065 | NI PCI/PCIe/USB-4065 |  |  |
| NIDMM_VAL_IMMEDIATE (default) | No trigger specified | √ | √ | √ | √ | √ |
| NIDMM_VAL_EXTERNAL | Pin 9 on the AUX Connector | — | √ | √ | √ | √ |
| NIDMM_VAL_SOFTWARE | Configures the DMM to wait until niDMM_SendSoftwareTrigger is called | √ | √ | √ | √ | √ |
| NIDMM_VAL_INTERVAL | Interval Trigger | — | √ | √ | √ | √ |
| NIDMM_VAL_PXI_TRIG0 | PXI Trigger Line 0 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG1 | PXI Trigger Line 1 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG2 | PXI Trigger Line 2 | √ | √ | √1 | √ | — |
| NIDMM_VAL_PXI_TRIG3 | PXI Trigger Line 3 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG4 | PXI Trigger Line 4 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG5 | PXI Trigger Line 5 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG6 | PXI Trigger Line 6 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_TRIG7 | PXI Trigger Line 7 | √ | √ | — | √ | — |
| NIDMM_VAL_PXI_STAR | PXI STAR Trigger Line | — | √ | — | √ | — |
| NIDMM_VAL_LBR_TRIG1 | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis | — | √2 | — | — | — |
| NIDMM_VAL_AUX_TRIG1 | Pin 3 on the AUX Connector | — | √ | — | √ | √ |

<sup>1</sup>Lines PXI_TRIG0, PXI_TRIG1, and PXI_TRIG2 refer to the device
 interconnect on the NI PCI-4070.

<sup>2</sup>Refer to the chassis section for more information regarding limitations
 of using this feature.

Parent topic:

Triggering

Related concepts:

- Chassis

Related information:

- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=load-switching.html language=enus -->
## TOPIC 00264: Load Switching

- bundle_id: `ni-dmm`
- source_path: `load-switching.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/load-switching.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic addresses analog signal-path related challenges associated with connecting a DUT, a switch, and a high-performance DMM. Topics include the following:

### Load Switching

This topic addresses analog signal-path related challenges associated with connecting a DUT, a switch, and a high-performance DMM. Topics include the following:

- [Switching Voltages](switching-voltages.html)
- [Switching Current](switching-current.html)
- [Switching Capacitance and Inductance](switching-capacitance-and-inductance.html)

Parent topic:

Using Switches

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations.html language=enus -->
## TOPIC 00265: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

Related concepts:

- Performing Offset Nulling
- Burden Voltage
- Switching Current
- DC Noise Rejection

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations_2.html language=enus -->
## TOPIC 00266: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations_3.html language=enus -->
## TOPIC 00267: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations_4.html language=enus -->
## TOPIC 00268: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations_5.html language=enus -->
## TOPIC 00269: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=low-current-measurement-considerations_6.html language=enus -->
## TOPIC 00270: Low-Current Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `low-current-measurement-considerations_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-current-measurement-considerations_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DMM to measure low current levels.The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.Low-level measurements are susceptible to sources of err

### Low-Current Measurement Considerations

You can use the DMM to measure low current levels.

The NI 4081 and NI 4071 offers more current measurement ranges than the NI 4080/4082 and NI 4070/4072. In the 1 µA range of the NI 4081 and NI 4071, you can resolve currents down to picoamperes.

Low-level measurements are susceptible to sources of error and noise that are often negligible for higher level measurements. In the low-level signals world, no material is an ideal insulator. Some materials are better insulators than others. Selection of proper cables and interconnects becomes very important.

When making low-level current measurements, noise and error sources are more likely to affect measurements in the order of 10µA or less. Take into account the recommendations listed in the table below to ensure measurement integrity.

| Error or Noise Source | Cause | Level of Induced Error | Recommendations |
| --- | --- | --- | --- |
| Input bias current | Input bias current doubles with every 10 °C increase. Input bias current results in an offset error that is temperature dependent on the 1 µA–10 µA ranges. | Typically 10 pA at 23 °C ambient, but it is factory calibrated to zero at that temperature. | Maintain an operating ambient temperature of less than 28 °C and enable Auto Zero to remove the internal DMM offset errors from the measurement. If you need to operate above 28 °C, perform offset nulling before taking your measurements. |
| Leakage currents due to poor insulation | When measuring low-level currents, leakage currents in insulators become relevant. Current flows between a high-impedance point and the nearby voltage sources. | Depends upon the resistivity of the insulator material. Some examples include the following: Glass Epoxy: >1012 Ω Nylon: >1012 Ω Polyethylene: >1015 Ω Virgin Teflon: >1016 Ω | Be sure that the test fixture for the DUT is constructed of a material appropriate for the desired test and that the test fixture is clean. |
| Noise currents due to triboelectrics1 | Currents are generated by moving the cables because a transfer of charge occurs between the insulator and the conductor when they rub against each other. | Hundreds of pA in a polyethylene cable (for example, RG-58) | Use cables designed for low noise. If you are not using polyethylene cables, be especially mindful to do the following: Secure the cables to non-vibrating surfaces. Do not move or flex the cables during measurements. |
| Noise currents due to piezoelectrics2 | Currents can be generated when the insulator is subjected to mechanical stress. | Hundreds of pA for polyethylene | Remove mechanical stress from cables and insulators. Make connecting structures rigid, especially when using Teflon insulated cable. |
| Error currents due to contamination and humidity | Insulation resistance gets reduced with increasing humidity and contamination. These two combined could also generate small electrochemically-induced currents. | On the order of pA to µA | Select insulators with low water absorption, such as Teflon. Keep humidity at moderate levels. It is recommended to maintain a relative humidity less than 55% especially when the level of cleanliness in the environment is questionable. Keep insulators and DUT connections clean. |
| Noise currents due to electromagnetic interference and electric fields | Surrounding equipment (motors, power cables, vibrating equipment) can induce noise currents. Moving people and charged objects near measurement setup can induce electrostatic coupling. | On the order of nA and tens of uA depending on proximity, device shielding, and magnitude of relative movement | Use shielded or twisted pair cables. Shield the device under test. Move power cables and other electrical equipment away from the measurement circuit. Avoid vibration and movement around the circuit while the measurement is being taken. Use shielded cabling, such as the Belden 83317E cable. Refer to the Belden CDT Incorporated Web site at www.belden.com for more information about these cables. |
| Burden voltage | For the maximum burden voltage per range, refer to the DMM specifications documents. | Depends on the circuit being measured | Calculate if the error caused by burden voltage is relevant when measuring the current in the circuit of interest. Refer to Burden Voltage for an example. |
| Leakage currents due to external switching | External switches used for routing low level currents could be a source of leakage currents. | Depends on the switch, temperature and humidity of the environment. | Consult your switch documentation on how to reduce leakage errors. Refer to Switching Current for other recommendations for systems with switches. Maintain temperature and humidity conditions under 28 °C and 55% relative humidity unless the switch specifies leakage performance above this level. |
| 1The Triboelectric Effect can be compared to the phenomenon of static electricity caused by rubbing certain insulators together. Teflon and silver in combination, for example, can create a very high level of triboelectric-induced current noise.2The Piezoelectric Effect, although well-exploited in sensors which convert changes in pressure from sound waves or physical vibration into small voltage signals, is highly undesirable in cables and interconnects. |  |  |  |

In addition to following these recommendations to reduce noise and errors, use software filtering and noise reduction techniques such as increasing the measurement aperture, choosing the most appropriate type of DC Noise Rejection, or averaging several measurements by setting the Number of Averages property.

Refer to Switching Current for more recommendations for systems with switches.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=low-voltages.html language=enus -->
## TOPIC 00271: Low Voltages

- bundle_id: `ni-dmm`
- source_path: `low-voltages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/low-voltages.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When setting up systems using relay switching, keep in mind that low–voltage performance is largely limited by the switches selected and the input terminals used on the switch.Good low–thermal relay switching cards are available from NI.Common, uncompensated reed relays can reach tens of µV of rathe

### Low Voltages

When setting up systems using relay switching, keep in mind that low–voltage performance is largely limited by the switches selected and the input terminals used on the switch.

Good low–thermal relay switching cards are available from NI.

Common, uncompensated reed relays can reach tens of µV of rather unstable offset, but high–performance reeds can reach below 1 µV.

Many armature–style latching reed relays can give very low drift (one such device is used in the NI 4065 and NI 4070/4071/4072 signal path). It is sometimes possible to compensate for this drift by using similar relays in both HI and LO connections or by placing adjacent poles of a 2–pole relay back–to–back.

Lastly, a common metrology technique involves making a measurement, reversing the leads, taking another measurement, and subtracting and averaging the two readings.

Parent topic:

Switching Voltages

<!--NI_TOPIC bundle=ni-dmm path=measurement-considerations.html language=enus -->
## TOPIC 00272: Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When taking measurements with a DMM, consider the following:

### Measurement Considerations

When taking measurements with a DMM, consider the following:

- [Normal and Common-Mode Signals](normal-and-common-mode-signals.html)
- [Normal-Mode Rejection Ratio (NMRR)](normal-mode-rejection-ratio-nmrr.html)
- [Common-Mode Rejection Ratio (CMRR)](common-mode-rejection-ratio-cmrr.html)
- [Effective Common-Mode Rejection Ratio (ECMRR)](effective-common-mode-rejection-ratio-ecmrr.html)
- [Input Resistance](input-resistance.html)
- [Burden Voltage](burden-voltage.html)
- [Thermal Voltages](thermal-voltages.html)
- [Settling Time](settling-time.html)
- [Resistor Self-Heating](resistor-self-heating.html)
- [Dielectric Absorption](dielectric-absorption.html)
- [Residual Impedance](residual-impedance.html)
- [Stray Admittance](stray-admittance.html)

<!--NI_TOPIC bundle=ni-dmm path=measurement-quality.html language=enus -->
## TOPIC 00273: Measurement Quality

- bundle_id: `ni-dmm`
- source_path: `measurement-quality.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measurement-quality.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: To achieve the highest measurement quality, you must understand the relationships between accuracy, sensitivity, resolution, noise, and precision.

### Measurement Quality

To achieve the highest measurement quality, you must understand the relationships between accuracy, sensitivity, resolution, noise, and precision.

Related concepts:

- Accuracy
- Sensitivity
- Resolution
- Noise
- Precision

<!--NI_TOPIC bundle=ni-dmm path=measuring-current.html language=enus -->
## TOPIC 00274: Measuring Current

- bundle_id: `ni-dmm`
- source_path: `measuring-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes how to measure current on NI DMMs. Measuring Current Within the Normal Range To configure current measurements within the normal range on the DMM, use one of the following two methods: Method 1 Select the current measurement function. Take a reading from the DMM immediately. M

### Measuring Current

This section describes how to measure current on NI DMMs.

#### Measuring Current Within the Normal Range

To configure current measurements within the normal range on the DMM, use one of the following two methods:

#### Method 1

1. Select the current measurement function.
2. Take a reading from the DMM immediately.

#### Method 2

1. Configure the DMM for a software trigger.
2. Initiate the DMM for a current measurement to cause the input relay to switch.
3. Send a software trigger to the DMM to take a measurement.

#### Using Current Shunt
 Modules

When taking current measurements outside of the specified range on
 the DMM, you must use a current shunt module. NI offers the NI CSM-10A and the
 NI CSM-200mA current shunt modules. The NI CSM-10A has a 0.01 Ω sense resistor, and
 the NI CSM-200mA has a 1.0 Ω sense resistor.

Note

Each current shunt
 module (CSM) operates by passing the input current through a precise resistor. The
 following figure shows the internal circuitry of the CSM:

[IMAGE alt='image' src='GUID-B32B2736-1581-4BC5-B757-6B560C647B3D-a5.svg']

1. Voltage Across Resistor (V
 OUT )
2. Precision Resistor
3. Fuse
4. Current Source (I
 IN )

To configure current measurements using the NI CSM-200mA or the NI CSM-10A,
 complete the following steps:

1. Measure the voltage drop across the resistor of the CSM.
2. Use this value to calculate the current using Ohm's Law, as
 follows:
 I
 <sub>IN</sub> =
 (
 V
 <sub>OUT</sub>)/
 R 
 where 
 I
 is the input current 
 V is the voltage across the
 precision resistor 
 R is the resistance of the
 precision resistor 
 For example, assume that you are using the
 CSM-200mA, which has a 1 Ω precision resistor, and the measured voltage is
 50 mV. Apply these values to Ohm's Law to determine the current, as
 follows: 
 50 mA = 50 mV / 1 Ω

Note

Parent topic:

Features

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range.html language=enus -->
## TOPIC 00275: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

Related concepts:

- Configuring Measurement Timing
- DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_2.html language=enus -->
## TOPIC 00276: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_3.html language=enus -->
## TOPIC 00277: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_4.html language=enus -->
## TOPIC 00278: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_5.html language=enus -->
## TOPIC 00279: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_6.html language=enus -->
## TOPIC 00280: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=measuring-on-the-100-m-range_7.html language=enus -->
## TOPIC 00281: Measuring on the 100 MΩ Range

- bundle_id: `ni-dmm`
- source_path: `measuring-on-the-100-m-range_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/measuring-on-the-100-m-range_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enable

### Measuring on the 100 MΩ Range

The 100 MΩ range allows for measurements up to 1.05 GΩ (NI 4080/4082, NI 4070/4072, and NI 4065) or 5 GΩ (NI 4081 and NI 4071), because of the methodology of the measurement and the high–impedance design of the device. This range allows 2-wire operation only. Offset Compensated Ohms cannot be enabled.

It is difficult to get a meaningful measurement with resistances above 10 MΩ without good shielding—including shielding of the resistor under test. Enclose the resistor under test in a metallic box, and connect this enclosure to the LO terminal. In the laboratory, even a small box covered with a single, continuous sheet of aluminum foil helps significantly with this kind of measurement.

#### Noise

The following diagram shows an equivalent circuit for all measurements above the 10 MΩ range.

[IMAGE alt='image' src='GUID-31F0E1F9-21D7-4964-B4D7-0869F3F78C32-a5.svg']

The voltage across the resistor is measured by the DMM and the resistor is calculated from:

R<sub>x</sub> = V /(I<sub>s</sub>—(V/10 MΩ)

where

R<sub>x</sub> = the resistor under test (up to 1.05 GΩ on the NI 4065 and NI 4070/4072, or up to 5 GΩ on the NI 4071)

V = the voltage measured by the DMM with Rx applied

I<sub>s</sub> = the source current (nominally 0.95 uA)

In the 100 MΩ range, any environmental noise or interference is amplified as the resistance being measured is increased. The requirement for good shielding increases as the resistor value increases.

Measurements above 10 MΩ should be made with as long an aperture time as possible, and 100 ms is the minimum recommended value. High-order DC noise rejection is recommended.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=multiple-point-acquisitions.html language=enus -->
## TOPIC 00282: Multiple Point Acquisitions

- bundle_id: `ni-dmm`
- source_path: `multiple-point-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/multiple-point-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multiple point acquisitions are useful when you need to acquire multiple measurements with the same configuration. In multiple point acquisitions, the DMM recognizes two different triggers: the trigger and the sample trigger. The number of times a trigger is received is specified as a count. The Tri

### Multiple Point Acquisitions

Multiple point acquisitions are useful when you need to acquire multiple measurements with the same configuration. In multiple point acquisitions, the DMM recognizes two different triggers: the trigger and the sample trigger. The number of times a trigger is received is specified as a count. The Trigger Count and Sample Count parameters specify the count for each type of trigger. The total number of samples acquired is equal to the product of Trigger Count and Sample Count.

To configure multiple point acquisitions, first configure the Function, Range, and Resolution with niDMM Config Measurement, and then configure the Sample Count to acquire with niDMM Configure Multi Point.

Configure the trigger source with niDMM Configure Trigger and the trigger source polarity with niDMM Configure Trigger Slope. Use niDMM Configure Multi Point to configure the sample trigger source, trigger count, and sample count. Use niDMM Configure Sample Trigger Slope to configure the sample trigger polarity.

As explained in Single Point Acquisitions, different sources are available for the trigger source. In a similar manner, the sample trigger also has different source options. Refer to niDMM Configure Trigger and niDMM Configure Multi Point for the possible trigger sources.

The multiple point acquisition initiates when niDMM Initiate or niDMM Read Multi Point is called. The figure below demonstrates the sequence of multiple point acquisitions.

Note

[IMAGE alt='image' src='GUID-7766D74E-090C-47E2-A853-C7D5DE531C9A-a5.svg']

After the acquisition is initiated, the DMM enters the Wait-For-Trigger state. When the trigger is received on the specified trigger source, the DMM waits for the specified trigger delay and then takes the first measurement. If Sample Count is greater than 1, the DMM enters the Wait-for-Sample-Trigger state. When the sample trigger is received on the appropriate sample trigger source, the DMM takes the next measurement. The DMM remains in the Sample Trigger loop until the measurement count is equal to the sample count. The DMM then compares the number of triggers received to the requested Trigger Count. If the number of triggers received is less than the Trigger Count, the DMM returns to the Wait-For-Trigger state and repeats the measurement process as described above. When the DMM has received the requested number of triggers for the sample trigger and the trigger, it returns to the Idle State.

Based upon the needs of your application, choose appropriate sources and counts for each trigger, as follows:

- If you require a multiple point acquisition with each measurement triggered by the same signal, you can set the Trigger Count equal to one and set the Sample Count to the total number of measurements. Specify the same source of the trigger for both the Trigger Source parameter of niDMM Configure Trigger and the Sample Trigger parameter of niDMM Configure Multi Point. For a demonstration, refer to the example Acq Multiple Samples-Ext Trig-Ext Sample Trig.
- If you need to initiate an acquisition with a single digital trigger and then acquire multiple measurements without triggering, set the source of the trigger in the Trigger Source parameter of niDMM Configure Trigger to the appropriate digital line, set the Trigger Count to 1, set the Sample Trigger to Immediate, and set the Sample Count to the desired number of measurements. For a demonstration, refer to the example Acq Multiple Samples-Ext Trig.
- If you want to insert a delay between measurement cycles in the sample loop, set the Sample Trigger to Interval and specify the delay in seconds for the Sample Interval parameter. For a demonstration, refer to the example Acq Multiple Samples-Interval Sample Trig. This functionality is not available for the NI 4080/4081/4082.
- If you want to control the acquisition using Software timing, configure the Trigger Source and/or Sample Trigger to Software. Use niDMM Send Software Trigger to send a trigger to the DMM. For a demonstration, refer to the example Cont Acq Multiple Samples-SW Sample Trig.

Refer to Scanning Switch Modules for more information about possible trigger sources.

After taking the measurement, the DMM can generate a Measurement Complete signal. The DMM then returns to the Idle State.

Parent topic:

Triggering

Related concepts:

- Single Point Acquisitions
- Acquiring Data
- Examples
- Scanning Switch Modules
- Generating a Measurement Complete Event

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=multiple-waveform-acquisitions.html language=enus -->
## TOPIC 00283: Multiple Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `multiple-waveform-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/multiple-waveform-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Acquire multiple waveforms by calling niDMM Initiate and niDMM Fetch Waveform or niDMM Read Waveform for every waveform you wish to capture. This feature is supported on the NI 4080/4081/4082 and the NI 4070/4071/4072.

### Multiple Waveform Acquisitions

Acquire multiple waveforms by calling niDMM Initiate and niDMM Fetch Waveform or niDMM Read Waveform for every waveform you wish to capture.

Note

Parent topic:

Acquiring Waveforms

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=new-features-and-changes.html language=enus -->
## TOPIC 00284: NI-DMM New Features and Changes

- bundle_id: `ni-dmm`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-DMM. Discover what is new in the latest releases of NI-DMM.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include no

### NI-DMM
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-DMM.

NI-DMM

Note

Release Notes

Related information:

- Software and Driver Downloads

<!--NI_TOPIC bundle=ni-dmm path=ni-4072.html language=enus -->
## TOPIC 00285: NI 4072

- bundle_id: `ni-dmm`
- source_path: `ni-4072.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni-4072.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4072 is a 6½ digit DMM for the PXI bus. The NI 4072 can take capacitance and inductance measurements and can acquire waveforms at 1.8 MS/s. For more information about the NI 4072 specifications, refer to Related Documentation for the NI 4072 specifications document.ImpedanceThe NI 4072 uses a

### NI 4072

The NI 4072 is a 6½ digit DMM for the PXI bus. The NI 4072 can take capacitance and inductance measurements and can acquire waveforms at 1.8 MS/s. For more information about the NI 4072 specifications, refer to Related Documentation for the NI 4072 specifications document.

#### Impedance

The NI 4072 uses a 2-wire, AC-current technique to measure capacitance and inductance. A current source (I<sub>src</sub>) is supplied to the device under test (DUT), and the NI 4072 determines the measured voltage (V<sub>m</sub>), as shown in the following figure.

[IMAGE alt='image' src='GUID-ED3A7AED-DEA3-482A-81D1-8780216530C6-a5.svg']

With a known current and voltage, the NI 4072 determines the capacitance or inductance of the DUT if the residual serial impedance (Z<sub>s</sub>) and the stray parallel impedance (Y<sub>p</sub>) are small or negligible compared to the DUT. If (Z<sub>s</sub>) and (Y<sub>p</sub>) introduce a significant error into the measurement, the NI 4072 can measure the error and reduce it using compensation techniques. For more information, refer to the OPEN/SHORT Compensation section.

For the measurement ranges for the capacitance and inductance modes on the NI 4072, refer to Related Documentation for the NI 4072 specifications document.

#### Interconnects and
 Cables

The front of the NI 4072 module has five connectors—four banana
 plug connectors and one 9-pin mini–circular DIN connector. The four banana plug
 connectors are high-voltage, safety-agency approved signal connectors. The 9-pin DIN
 connector labeled AUX I/O is a digital signal connector, which carries triggers and
 SCXI communication signals. For an illustration of the front panel connectors and
 wiring instructions, refer to Front Panel Connections
 topic for the NI 4072.

The input connectors on the NI 4072 are gold-plated,
 low-thermal copper for best low-voltage performance. The insulator material is a
 Lexan compound, optimized for low leakage over the full environmental operating
 range.

For use with the NI 4072, NI recommends selecting a cable with
 characteristics similar to the Belden 83317E, which is available at www.belden.com.
 Tape-wrapped polytetrafluoroethylene (PTFE) insulation guarantees low leakage.
 Copper conductors with silver plating perform very well for low-voltage measurements
 because of their low thermal characteristics. Use a cable with at least 90%
 shielding effectiveness.

| Type of Insulator | AWG | Conductor Material | Resistance per Foot | Capacitance per Foot |
| --- | --- | --- | --- | --- |
| TFE | 26 | Silver-plated copper, stranded | 39 mΩ | 35.5 pF |

#### Operation

The NI 4072 can
 operate as a DMM and can acquire waveforms up to
 1.8 MS/s. The following table lists the functions and ranges supported by the NI
 4072 while in DMM mode.

The following table lists the functions and ranges
 supported for waveform acquisitions:

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 300 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 300 V |
| DC Current1 | 20 mA, 200 mA, 1 A |
| AC Current1 | 10 mA, 100 mA, 1 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.5 V at 1 mA |
| Frequency/Period2 | 1 Hz - 500 kHz / 2 µs - 1 s |
| Capacitance | 300 pF, 1 nF, 10 nF, 100 nF, 1 µF, 10 µF, 100 µF, 1,000 µF, 10,000 µF |
| Inductance | 10 µH, 100 µH, 1 mH, 10 mH, 100 mH, 1 H, 5 H |
| 1To measure current outside of the normal range on the NI 4072, you must use a current shunt module (CSM). Refer to Measuring Current for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the available NI 4072 input resistance selections.
 NI calibrates the NI 4072 for full accuracy with all input resistances
 shown.

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 300 V | AC or DC |
| Current Waveform1 | 20 mA, 200 mA, 1 A | DC |
| 1To measure current outside of the normal range on the NI 4072, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. |  |  |

Note

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4072 is equipped with a F 1.25 A 250 V Fast–Acting fuse designed to help protect the DMM and your test system. For instructions on replacing the fuse, refer to Related Documentation for the NI Digital Multimeters Getting Started Guide.

#### Calibrating the NI
 4072

Calibration maximizes the accuracy of a DMM. To ensure accuracy, you
 must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to the NI 4070/4072 6½ Digit FlexDMM Calibration
 Procedure at the NI Calibration Solutions Web site for information on
 externally calibrating the NI PXI/PCI-4070/4072. For information on calibrating the
 NI 4072 using Calibration Executive, refer to the NI Calibration Solutions Web site.
 All NI measurement devices receive NIST-traceable calibration before
 shipping.

Related concepts:

- Capacitance/Inductance
- OPEN/SHORT Compensation
- Front Panel Connections
- Acquiring Waveforms
- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=ni-dmm-examples.html language=enus -->
## TOPIC 00286: NI-DMM Examples

- bundle_id: `ni-dmm`
- source_path: `ni-dmm-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni-dmm-examples.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DMM includes several example applications that demonstrate the functionality of your device and can serve as interactive tools, programming models, and building blocks for your own applications.NI Example FinderThe NI Example Finder is a utility that organizes examples into categories and allows

### NI-DMM Examples

NI-DMM includes several example applications that demonstrate the functionality of your
 device and can serve as interactive tools, programming models, and building blocks for
 your own applications.

#### NI Example Finder

The NI
 Example Finder is a utility that organizes examples into categories and allows you
 to browse and search installed examples. For example, search for
 "DMM" to locate all NI digital multimeter examples. You can see
 descriptions and compatible hardware models for each example or see all the examples
 compatible with one particular hardware model.

To locate examples using the NI
 Example Finder within LabVIEW or LabWindows/CVI, select
 Help»Find Examples and navigate to
 Hardware Input and Output»Modular
 Instruments»NI-DMM.

| Software Application | Installed Example Locations |
| --- | --- |
| LabVIEW | LabVIEW\\examples\\instr\\niDMM, where LabVIEW is the LabVIEW directory for the specific LabVIEW version you installed on your system. |
| LabWindows/CVI | Program Files\\IVI Foundation\\IVI\\Drivers\\niDMM\\Examples\\CVI |
| ANSI C or Microsoft Visual C/C++ | NIDocDir\\NI-DMM\\examples, where NIDocDir is one of the following directories: Windows 8/7/Vista—Users\\Public\\Documents\\National Instruments Windows XP—Documents and Settings\\All Users\\Shared Documents\\National Instruments |

| NI-RFSG Example | Description |  |
| --- | --- | --- |
|  | NI-DMM Measure DC Voltage | This example demonstrates how to acquire a single DC Voltage measurement. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range. |
|  | NI-DMM Measure AC Voltage | This example demonstrates how to acquire a single AC Voltage measurement. The measured value displays in the Measurement indicator. A Boolean control indicates if the measured value is out of range. |
|  | Cont Acq&Graph Multiple Samples | This example performs a continuous acquisition. The niDMM Initiatve VI starts the acquisition, and the niDMM Fetch Multi Point VI returns the requested samples. The data displays in a waveform chart. |
|  | Read & Graph Waveform | This example acquires a waveform using the niDMM Read Waveform VI. The data is displayed in a waveform graph. |

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-dmm path=ni-dmm.html language=enus -->
## TOPIC 00287: NI-DMM Overview

- bundle_id: `ni-dmm`
- source_path: `ni-dmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni-dmm.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DMM provides support for customers using NI digital multimeters. Below is the product definition. In the angle brackets, we've included suggestions for how to construct these sentences. For more guidance on using the suggestions, refer to "How to Write a Product Definition" (Word doc on Doc Strat

### NI-DMM
 Overview

NI-DMM provides support for customers using NI digital
 multimeters.

NI-DMM is an NI instrument driver that communicates with all NI
 programmable digital multimeters (DMMs). NI-DMM is an
 interchangeable virtual instrument (IVI)–compliant instrument driver, and it features a
 set of operations and properties that exercise the functionality of the DMM and includes
 an interactive soft front panel and examples.

NI-DMM supports the following devices:

| DMM | Details |
| --- | --- |
| PXIe‑4082 | 6½ digits; functionality includes inductance and capacitance modes |
| PXIe‑4081 | 7½ digits, 1000 V, 3 A with 10 pA sensitivity |
| PXIe‑4080 | 6½ digits |
| PXI‑4072 | 6½ digits; functionality includes inductance and capacitance modes |
| PXI‑4071 | 7½ digits, 1000 V, 3 A with 10 pA sensitivity |
| PXI/PCI‑4070 | 6½ digits |
| PXI/PCI/PCIe/USB‑4065 | 6½ digits |

<!--NI_TOPIC bundle=ni-dmm path=ni-usb-4065-front-panel-connections.html language=enus -->
## TOPIC 00288: USB-4065 Front Panel Connections

- bundle_id: `ni-dmm`
- source_path: `ni-usb-4065-front-panel-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni-usb-4065-front-panel-connections.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: DC Voltage AC Voltage DC Current AC Current 2-Wire Resistance 4-Wire Resistance Voltage Drop Across a Diode Triggering The following table shows the pins used for input and output triggers, which are used during synchronous scanning or handshaking: Pin Assignment 2 Ground 3 AUX Trigger In 6 Measurem

### USB-4065 Front Panel Connections

[IMAGE alt='image' src='GUID-6FB4C6C2-053A-4214-AB1C-6680B1514CF0-a5.svg']

Parent topic:

NI 4065

#### DC Voltage

[IMAGE alt='image' src='GUID-2C6D2690-467E-4974-B570-A3C6BF96FD2F-a5.svg']

#### AC Voltage

[IMAGE alt='image' src='GUID-D98BFC62-771E-4E98-8210-53300807F52E-a5.svg']

#### DC Current

[IMAGE alt='image' src='GUID-17D0C289-9ED4-4E09-83CA-0D23B22984B3-a5.svg']

#### AC Current

[IMAGE alt='image' src='GUID-5FD06762-906F-440A-8461-28638137ADC2-a5.svg']

#### 2-Wire Resistance

[IMAGE alt='image' src='GUID-24E66C6B-AD6A-4D1C-B201-1944E569CE76-a5.svg']

#### 4-Wire Resistance

[IMAGE alt='image' src='GUID-E028F006-E154-4F47-B3BB-CC35FDF0496B-a5.svg']

#### Voltage Drop Across a Diode

[IMAGE alt='image' src='GUID-D72D9C28-90BE-42E4-A6A2-D6E8C2FE5CD2-a5.svg']

#### Triggering

[IMAGE alt='image' src='GUID-4DDF1F08-6FAC-4C80-B847-D716C8133641-a5.svg']

The following table shows the pins used for input and output triggers, which are used
 during synchronous scanning or handshaking:

| Pin | Assignment |
| --- | --- |
| 2 | Ground |
| 3 | AUX Trigger In |
| 6 | Measurement Complete |
| 9 | External Trigger In (Trigger/Sample Trigger) |

Note

##### Cable Accessories

| AUX Trigger Cable | This cable allows the NI 4065 to trigger NI switches, third-party switches, and any other external device during synchronous scanning or handshaking scanning. Note The AUX Trigger Cable only provides access to AUX I/O Connector Pins 2, 6, and 9, where Pin 2 is Ground and is present in both ends of the cable. |
| --- | --- |
| SH9MD-AUX Cable | This cable allows the NI PXI/PCI/PCIe 4065 to control SCXI switches, send measurement complete, and receive external trigger. This cable allows the NI USB 4065 to send measurement complete and receive external trigger. This functionality allows the NI 4065 to work under both synchronous scanning and handshaking scanning. Refer to Scanning Switch Modules for more information. |

For installation instructions for NI switch modules, refer to the
 NI Switches Help at either of the following locations:

- Start»Programs»National
 Instruments»NI-SWITCH»Documentation»NI Switches Help (if you
 have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not 
 installed NI-SWITCH)

#### Temperature (Thermocouple)

[IMAGE alt='image' src='GUID-8D35A6CB-8958-42EF-B7CB-F16FDE40E2BF-a5.svg']

#### Temperature (2-wire RTD)

[IMAGE alt='image' src='GUID-AA624398-AEB5-4DA9-8137-D6CED38D4BF5-a5.svg']

#### Temperature (4-wire RTD)

[IMAGE alt='image' src='GUID-063EEAD4-EF60-4144-9411-D2971BEB5988-a5.svg']

#### Temperature (Thermistor)

[IMAGE alt='image' src='GUID-AA624398-AEB5-4DA9-8137-D6CED38D4BF5-a5.svg']

<!--NI_TOPIC bundle=ni-dmm path=ni4065-dmm-measurement-cycle.html language=enus -->
## TOPIC 00289: NI 4065 DMM Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `ni4065-dmm-measurement-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni4065-dmm-measurement-cycle.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065 measurement cycle is made up of three measurement phases: switch time, settling time, and aperture time. Refer to the figure below for relative timing of these phases. The aperture time is the length of time the signal of interest is being measured. Generally the settle and aperture time

### NI 4065 DMM Measurement Cycle

The NI 4065 measurement cycle is made up of three measurement phases: switch time, settling time, and aperture time. Refer to the figure below for relative timing of these phases. The aperture time is the length of time the signal of interest is being measured. Generally the settle and aperture times are selected by the device driver based on the specified resolution. Settling time and aperture can be set using the niDMM Property Node. Refer to Configuring Measurement Timing for more information.

[IMAGE alt='image' src='GUID-A81EFFBE-BB88-4C8E-82F1-5521C18CECDF-a5.svg']

The internal switch time is required to configure the analog circuitry of the NI 4065 for the next measurement. This time is not user programmable.

During resistance measurements, the signal is measured with an applied current source. The AC measurement cycle contains the same phases, but the minimum signal measurement time is based on the minimum frequency required of the measurement. For example, for a minimum frequency of 50 Hz with a 5½ digit resolution, an aperture time of 10x the period of the 50 Hz signal is required, or in this example, 200 ms.

When Auto Range is selected, the Auto Range measurement phase occurs before the signal measurement phases. After the correct range is identified, signal measurements use the selected range.

Note

Parent topic:

DMM Measurements

Related concepts:

- Configuring Measurement Timing

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=ni4065.html language=enus -->
## TOPIC 00290: NI 4065

- bundle_id: `ni-dmm`
- source_path: `ni4065.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni4065.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065 is a 6½ digit DMM for the PXI, PCI, PCI Express, and USB buses. For more detailed information about the NI 4065 specifications, refer to Related Documentation for the NI 4065 Specifications document.Front Panel ConnectionsThe PXI, PCI, and PCI Express front panels have four shrouded bana

### NI 4065

The NI 4065 is a 6½ digit DMM for the PXI, PCI, PCI Express, and USB buses. For more
 detailed information about the NI 4065 specifications, refer to Related Documentation
 for the NI 4065 Specifications document.

#### Front Panel Connections

The
 PXI, PCI, and PCI Express front panels have four shrouded banana plug connectors and
 one 9-pin mini–circular DIN connector. The NI USB-4065 has five shrouded banana plug
 connectors on the front panel and one 9-pin mini–circular DIN connector on the back
 panel. The banana plug connectors are high-voltage, safety signal connectors. The
 9-pin DIN connector labeled AUX I/O is a digital signal connector, which carries
 triggers and SCXI communication
 signals. For an illustration of the front panel connectors and wiring instructions,
 refer to NI 4065 Front Panel Connections.

Note

ni.com/support

#### Operation

The following
 table lists the functions and ranges supported by the NI 4065:

| Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 300 V |
| AC Voltage | 200 mV, 2 V, 20 V, 300 V |
| DC Current1 | 10 mA, 100 mA, 1 A, 3 A |
| AC Current1 | 10 mA, 100 mA, 500 mA, 3A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ |
| Diode | 10 V at 100 µA, 3.5 V at 1 mA |
| 1To measure current outside of the normal range on the NI 4065, you must use a current shunt module (CSM). Refer to Measuring Current for more information. |  |

The following table lists the available NI 4065 input resistance selections.
 NI calibrates the NI 4065 for full accuracy with all input resistances
 shown.

| DCV | ACV |  |  |
| --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 200 mV | 10 MΩ |
| 1 V | 10 MΩ (default) or 10 GΩ | 2 V | 10 MΩ |
| 10 V | 10 MΩ (default) or 10 GΩ | 20 V | 10 MΩ |
| 100 V | 10 MΩ (default) | 300 V | 10 MΩ |
| 300 V | 10 MΩ (default) |  |  |

#### Additional Features

- Auto Zero
- Configuring Auto Range
- Configuring Measurement Timing
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4065 is equipped with a Fast–Acting fuse designed to help protect your module and test
 system. For instructions on replacing the fuse, refer to *Fuse
 Replacement*.

#### Calibrating the
 NI 4065

Calibration maximizes the accuracy of a DMM. To ensure accuracy,
 you must perform calibration. NI recommends you calibrate annually.

Refer to
 the NI 4065 6½ Digit DMM Calibration Procedure at the
 NI Calibration Solutions Web site for information on externally calibrating the NI
 PXI/PCI/PCIe-4065. For information on calibrating the NI 4065 using Calibration
 Executive, refer to the NI Calibration Solutions Web site.

Related concepts:

- Triggering
- SCXI Communication
- PXI/PCI/PCIe-4065 Front Panel Connections
- Auto Zero
- Configuring Auto Range
- Configuring Measurement Timing
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules
- Fuse Replacement

<!--NI_TOPIC bundle=ni-dmm path=ni4070.html language=enus -->
## TOPIC 00291: NI 4070

- bundle_id: `ni-dmm`
- source_path: `ni4070.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni4070.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4070 is a 6½ digit DMM for the PXI and PCI buses. The NI 4070 can acquire waveforms at 1.8 MS/s. For more information about the NI 4070 specifications, refer to Related Documentation for the NI 4070 specifications document.Interconnects and CablesThe front of the NI 4070 module has five conne

### NI 4070

The NI 4070 is a 6½ digit DMM for the PXI and PCI buses. The NI 4070 can acquire
 waveforms at 1.8 MS/s. For more information about the NI 4070 specifications, refer to
 Related Documentation for the NI 4070 specifications document.

#### Interconnects and
 Cables

The front of the NI 4070 module has five connectors—four banana
 plug connectors and one 9-pin mini–circular DIN connector. The four banana plug
 connectors are high-voltage, safety-agency approved signal connectors. The 9-pin DIN
 connector labeled AUX I/O is a digital signal connector, which carries triggers and
 SCXI communication signals. For an illustration of the front panel connectors and
 wiring instructions, refer to NI 4070 Front Panel
 Connections.

The input connectors on the NI 4070 are gold-plated,
 low-thermal copper for best low-voltage performance. The insulator material is a
 Lexan compound, optimized for low leakage over the full environmental operating
 range.

For use with the NI 4070, NI recommends selecting a cable with
 characteristics similar to the Belden 83317E; refer to the Belden CDT Incorporated
 Web site at www.belden.com for information about this cable.

Tape-wrapped
 polytetrafluoroethylene (PTFE) insulation guarantees low leakage. Copper conductors
 with silver plating perform very well for low-voltage measurements because of their
 low thermal characteristics. Use a cable with at least 90% shielding
 effectiveness.

| Type of Insulator | AWG | Conductor Material | Resistance per Foot | Capacitance per Foot |
| --- | --- | --- | --- | --- |
| TFE | 26 | Silver-plated copper, stranded | 39 mΩ | 35.5 pF |

#### Operation

The NI 4070 can
 operate as a DMM and can acquire waveforms up to
 1.8 MS/s. The following table lists the functions and ranges supported by the
 NI 4070 while in DMM mode:

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 300 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 300 V |
| DC Current1 | 20 mA, 200 mA, 1 A |
| AC Current1 | 10 mA, 100 mA, 1 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.5 V at 1 mA |
| Frequency/Period2 | 1 Hz - 500 kHz / 2 µs - 1 s |
| 1To measure current outside of the normal range on the NI 4070, you must use a current shunt module (CSM). Refer to Measuring Current for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the functions and ranges supported for waveform
 acquisitions:

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 300 V | AC or DC |
| Current Waveform1 | 20 mA, 200 mA, 1 A | DC |
| 1To measure current outside of the normal range on the NI 4070, you must use a current shunt module (CSM). Refer to Measuring Current for more information. |  |  |

The following table lists the available NI 4070 input resistance selections.
 NI calibrates the NI 4070 for full accuracy with all input resistances
 shown.

| DCV | ACV | Waveform Acquisitions |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 50 mV | 1 MΩ | 100 mV | 10 GΩ or 1 MΩ (default) |
| 1 V | 10 MΩ (default) or 10 GΩ | 500 mV | 1 MΩ | 1 V | 10 GΩ or 1 MΩ (default) |
| 10 V | 10 MΩ (default) or 10 GΩ | 5 V | 1 MΩ | 10 V | 10 GΩ or 1 MΩ (default) |
| 100 V | 10 MΩ (default) | 50 V | 1 MΩ | 100 V | 1 MΩ (default) |
| 300 V | 10 MΩ (default) | 300 V | 1 MΩ | 300 V | 1 MΩ (default) |

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4070 is equipped with a Fast–Acting fuse designed to help protect the DMM and your test
 system. For instructions on replacing the fuse, refer to *Fuse
 Replacement*.

#### Calibrating the
 NI 4070

Calibration maximizes the accuracy of a DMM. To ensure accuracy,
 you must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to self-calibration or ADC calibration to
 internally calibrate the NI 4070. Refer to the NI 4070/4072 6½ Digit
 FlexDMM Calibration Procedure at the NI Calibration Solutions Web site
 for information on externally calibrating the NI PXI/PCI-4070/4072. For information
 on calibrating the NI 4070 using Calibration Executive, refer to the NI Calibration
 Solutions Web site. All NI measurement devices receive NIST-traceable calibration
 before shipping.

Related concepts:

- Front Panel Connections
- Acquiring Waveforms
- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules
- Fuse Replacement

<!--NI_TOPIC bundle=ni-dmm path=ni4071.html language=enus -->
## TOPIC 00292: NI 4071

- bundle_id: `ni-dmm`
- source_path: `ni4071.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni4071.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4071 DMM for the PXI bus has a 7½ digit capability for the resistance and DCV modes and a 6½ digit capability for all other modes. The NI 4071 has a 1000 V capability and can acquire waveforms at 1.8 MS/s. For more information about the NI 4071 specifications, refer to Related Documentation f

### NI 4071

The NI 4071 DMM for the PXI bus has a 7½ digit capability for the resistance and DCV
 modes and a 6½ digit capability for all other modes. The NI 4071 has a 1000 V capability
 and can acquire waveforms at 1.8 MS/s. For more information about the NI 4071
 specifications, refer to Related Documentation for the NI 4071 specifications
 document.

#### Interconnects and
 Cables

The front of the NI 4071 module has five connectors—four banana
 jacks and one 9-pin mini–circular DIN connector. The four banana jack connectors are
 high-voltage, safety-agency approved signal connectors. The 9-pin DIN connector
 labeled AUX I/O is a digital signal connector, which carries triggers and SCXI
 communication signals. For an illustration of the front panel connectors and wiring
 instructions, refer to Front Panel Connections
 topic for the NI 4071.

The input connectors on the NI 4071 are gold-plated,
 low-thermal copper for best low-voltage performance. The insulator material is a
 Lexan compound, optimized for low leakage over the full environmental operating
 range.

For use with the NI 4071, NI recommends selecting a cable with
 characteristics similar to the Belden 83317E; refer to the Belden CDT Incorporated
 Web site at www.belden.com for information about this cable.

Tape-wrapped
 polytetrafluoroethylene (PTFE) insulation guarantees low leakage. Copper conductors
 with silver plating perform very well for low-voltage measurements because of their
 low thermal characteristics. Use a cable with at least 90% shielding
 effectiveness.

| Type of Insulator | AWG | Conductor Material | Resistance per Foot | Capacitance per Foot |
| --- | --- | --- | --- | --- |
| TFE | 26 | Silver-plated copper, stranded | 39 mΩ | 35.5 pF |

#### Operation

The NI 4071 can
 operate as a DMM and can acquire waveforms up to
 1.8 MS/s. The following table lists the functions and ranges supported by the
 NI 4071 while in DMM mode:

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 1000 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 700 V |
| DC Current1 | 1 µA, 10 µA, 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A |
| AC Current1 | 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ, 5 GΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.0 V at 1 mA |
| Frequency/Period2 | 1 Hz - 500 kHz / 2 µs - 1 s |
| 1To measure current outside of the normal range on the NI 4071, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the functions and ranges supported for waveform
 acquisitions:

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 1000 V | AC or DC |
| Current Waveform1 | 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A | DC |
| 1To measure current outside of the normal range on the NI 4071, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. |  |  |

The following table lists the available NI 4071 input resistance selections.
 NI calibrates the NI 4071 for full accuracy with all input resistances
 shown.

| DCV | ACV | Waveform Acquisitions |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 50 mV | 10 MΩ | 100 mV | 10 GΩ or 10 MΩ (default) |
| 1 V | 10 MΩ (default) or 10 GΩ | 500 mV | 10 MΩ | 1 V | 10 GΩ or 10 MΩ (default) |
| 10 V | 10 MΩ (default) or 10 GΩ | 5 V | 10 MΩ | 10 V | 10 GΩ or 10 MΩ (default) |
| 100 V | 10 MΩ (default) | 50 V | 10 MΩ | 100 V | 10 MΩ (default) |
| 1000 V | 10 MΩ (default) | 700 V | 10 MΩ | 1000 V | 10 MΩ (default) |

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4071 is equipped with a F 3.15 A 250 V Fast–Acting fuse designed to help protect the DMM and your test system. For instructions on replacing the fuse, refer to Related Documentation for the NI Digital Multimeters Getting Started Guide.

#### Calibrating the
 NI 4071

Calibration maximizes the accuracy of a DMM. To ensure accuracy,
 you must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to the self-calibration or
 ADC
 calibration sections to internally calibrate the NI 4071. Refer to the
 NI 4071 7½–Digit FlexDMM Calibration Procedure at the
 NI Calibration Solutions Web site for information on externally calibrating the
 NI PXI-4071. For information on calibrating the NI 4071 using Calibration Executive,
 refer to the NI Calibration Solutions Web site. All NI measurement devices receive
 NIST-traceable calibration before shipping.

Related concepts:

- Front Panel Connections
- Acquiring Waveforms
- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=ni4081.html language=enus -->
## TOPIC 00293: NI 4081

- bundle_id: `ni-dmm`
- source_path: `ni4081.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/ni4081.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4081 DMM for the PXI Express bus has a 7½ digit capability for the resistance and DCV modes and a 6½ digit capability for all other modes. The NI 4081 has a 1000 V capability. For more information about the NI 4081 specifications, refer to Related Documentation for the NI 4081 specifications

### NI 4081

The NI 4081 DMM for the PXI Express bus has a 7½ digit capability for the resistance and
 DCV modes and a 6½ digit capability for all other modes. The NI 4081 has a 1000 V
 capability. For more information about the NI 4081 specifications, refer to Related
 Documentation for the NI 4081 specifications document.

#### Interconnects and Cables

The front of the NI 4081 module has four high-voltage, safety-agency approved banana plug connectors. For an illustration of the front panel connectors and wiring instructions, refer to the Front Panel Connections topic for the NI 4081.

For use with the NI 4081, NI recommends selecting a cable with characteristics similar to the Belden 83317E; refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Tape-wrapped polytetrafluoroethylene (PTFE) insulation guarantees low leakage. Copper conductors with silver plating perform very well for low-voltage measurements because of their low thermal characteristics. Use a cable with at least 90% shielding effectiveness.

#### Operation

The NI 4081 can
 operate as a DMM and can acquire waveforms up to 1.8 MS/s. Refer to the NI
 PXIe-4081 Specifications document for the functions and ranges
 supported by the NI 4081.

The following table lists the functions and ranges
 supported by the NI 4081 while in DMM mode:

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 1000 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 700 V |
| DC Current1 | 1 µA, 10 µA, 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A |
| AC Current1 | 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ, 5 GΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.0 V at 1 mA |
| Frequency/Period2 | 15 Hz - 500 kHz / 2 µs - 67 ms |
| 1To measure current outside of the normal range on the NI 4081, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the functions and ranges supported for waveform
 acquisitions:

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 1000 V | AC or DC |
| Current Waveform1 | 100 µA, 1 mA, 10 mA, 100 mA, 1 A, 3 A | DC |
| 1To measure current outside of the normal range on the NI 4081, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. |  |  |

The following table lists the available NI 4081 input resistance selections.
 NI calibrates the NI 4081 for full accuracy with all input resistances
 shown.

| DCV | ACV | Voltage Waveform |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 50 mV | 10 MΩ | 100 mV | 10 GΩ or 10 MΩ (default) |
| 1 V | 10 MΩ (default) or 10 GΩ | 500 mV | 10 MΩ | 1 V | 10 GΩ or 10 MΩ (default) |
| 10 V | 10 MΩ (default) or 10 GΩ | 5 V | 10 MΩ | 10 V | 10 GΩ or 10 MΩ (default) |
| 100 V | 10 MΩ (default) | 50 V | 10 MΩ | 100 V | 10 MΩ (default) |
| 1000 V | 10 MΩ (default) | 700 V | 10 MΩ | 1000 V | 10 MΩ (default) |

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4081 is equipped with a 3.5 A 1000 V time-delay user-replaceable fuse designed to help protect the DMM and your test system. For information on replacing the fuse, refer to the Fuse Replacement topic for the NI 4081.

#### Calibrating the
 NI 4081

Calibration maximizes the accuracy of a DMM. To ensure accuracy,
 you must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to the self-calibration or ADC calibration sections to internally
 calibrate the NI 4081. Refer to the NI 4081 7½-Digit DMM Calibration
 Procedure at the NI Calibration Solutions Web site for information on
 externally calibrating the NI PXI-4081. For information on calibrating the NI 4081
 using Calibration Executive, refer to the NI Calibration Solutions Web site. All
 NI measurement devices receive NIST-traceable calibration before
 shipping.

Related concepts:

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules
- Fuse Replacement

<!--NI_TOPIC bundle=ni-dmm path=nipxie-4080.html language=enus -->
## TOPIC 00294: NI PXIe-4080

- bundle_id: `ni-dmm`
- source_path: `nipxie-4080.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nipxie-4080.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-4080 (NI 4080) is a 6½ digit DMM for the PXI Express bus. For more information about the NI 4080 specifications, refer to the NI 4080 Specifications document.Interconnects and CablesThe front of the NI PXIe-4080 module has four high-voltage, safety-agency approved banana plug connectors.

### NI PXIe-4080

The NI PXIe-4080 (NI 4080) is a 6½ digit DMM for the PXI Express bus. For more
 information about the NI 4080 specifications, refer to the NI 4080
 Specifications document.

#### Interconnects and Cables

The front of the NI PXIe-4080 module has four high-voltage, safety-agency approved banana plug connectors. For an illustration of the front panel connectors and wiring instructions, refer to the NI 4080 Front Panel Connections topic.

For use with the NI 4080, NI recommends selecting a cable with characteristics similar to the Belden 83317E. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Tape-wrapped polytetrafluoroethylene (PTFE) insulation guarantees low leakage. Copper conductors with silver plating perform very well for low-voltage measurements because of their low thermal characteristics. Use a cable with at least 90% shielding effectiveness.

#### Operation

The NI 4080 can
 operate as a DMM and can acquire waveforms up to 1.8 MS/s. Refer to the NI
 PXIe-4080 Specifications document for a full list of functions and
 ranges supported by the NI 4080.

The following table lists the functions and
 ranges supported by the NI 4080 while in DMM mode:

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 300 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 300 V |
| DC Current1 | 20 mA, 200 mA, 1 A |
| AC Current1 | 10 mA, 100 mA, 1 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.5 V at 1 mA |
| Frequency/Period2 | 15 Hz - 500 kHz / 2 µs - 67 ms |
| 1To measure current outside of the normal range on the NI 4080, you must use a current shunt module (CSM). Refer to Measuring Current for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the functions and ranges supported for waveform
 acquisitions:

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 300 V | AC or DC |
| Current Waveform1 | 20 mA, 200 mA, 1 A | DC |
| 1To measure current outside of the normal range on the NI 4080, you must use a current shunt module (CSM). Refer to Measuring Current for more information |  |  |

The following table lists the available NI 4080 input resistance selections.
 NI calibrates the NI 4080 for full accuracy with all input resistances
 shown.

| DCV | ACV | Voltage Waveform |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 50 mV | 1 MΩ | 100 mV | 10 GΩ or 1 MΩ (default) |
| 1 V | 10 MΩ (default) or 10 GΩ | 500 mV | 1 MΩ | 1 V | 10 GΩ or 1 MΩ (default) |
| 10 V | 10 MΩ (default) or 10 GΩ | 5 V | 1 MΩ | 10 V | 10 GΩ or 1 MΩ (default) |
| 100 V | 10 MΩ (default) | 50 V | 1 MΩ | 100 V | 1 MΩ (default) |
| 300 V | 10 MΩ (default) | 300 V | 1 MΩ | 300 V | 1 MΩ (default) |

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4080 is equipped with a 1 A 400 V Time-Lag fuse designed to help protect the DMM and your test system.

#### Calibrating the
 NI 4080

Calibration maximizes the accuracy of a DMM. To ensure accuracy,
 you must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to the self-calibration or ADC calibration topics to internally
 calibrate the NI 4080. Refer to the NI 4080 6½-Digit DMM Calibration
 Procedure at the NI Calibration Solutions Web site for information on
 externally calibrating the NI PXIe-4080. For information on calibrating the NI 4080
 using Calibration Executive, refer to the NI Calibration Solutions Web site. All
 NI measurement devices receive NIST-traceable calibration before
 shipping.

Related concepts:

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=nipxie-4082.html language=enus -->
## TOPIC 00295: NI PXIe-4082

- bundle_id: `ni-dmm`
- source_path: `nipxie-4082.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nipxie-4082.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-4082 (NI 4082) is a 6½ digit DMM for the PXI bus. The NI 4082 can take capacitance and inductance measurements and can acquire waveforms at 1.8 MS/s. For more information about the NI 4082 specifications, refer to the NI PXIe-4082 Specifications document.ImpedanceThe NI 4082 uses a 2-wir

### NI PXIe-4082

The NI PXIe-4082 (NI 4082) is a 6½ digit DMM for the PXI bus. The NI 4082 can take
 capacitance and inductance measurements and can acquire waveforms at 1.8 MS/s. For more
 information about the NI 4082 specifications, refer to the NI PXIe-4082
 Specifications document.

#### Impedance

The NI 4082 uses a 2-wire, AC-current technique to measure capacitance and inductance. A current source (I<sub>src</sub>) is supplied to the device under test (DUT), and the NI 4082 determines the measured voltage (V<sub>m</sub>), as shown in the following figure.

[IMAGE alt='image' src='GUID-ED3A7AED-DEA3-482A-81D1-8780216530C6-a5.svg']

With a known current and voltage, the NI 4082 determines the capacitance or inductance of the DUT if the residual serial impedance (Z<sub>s</sub>) and the stray parallel impedance (Y<sub>p</sub>) are small or negligible compared to the DUT. If (Z<sub>s</sub>) and (Y<sub>p</sub>) introduce a significant error into the measurement, the NI 4082 can measure the error and reduce it using compensation techniques. For more information, refer to the OPEN/SHORT Compensation section.

For the measurement ranges for the capacitance and inductance modes on the NI 4082, refer to Related Documentation for the NI 4082 specifications document.

#### Interconnects and
 Cables

The front of the NI 4082 module has four high-voltage,
 safety-agency approved banana plug connectors. For an illustration of the front
 panel connectors and wiring instructions, refer to Front Panel Connections topic for
 the NI 4082.

For use with the NI 4082, NI recommends selecting a cable with
 characteristics similar to the Belden 83317E, which is available at www.belden.com.
 Tape-wrapped polytetrafluoroethylene (PTFE) insulation guarantees low leakage.
 Copper conductors with silver plating perform very well for low-voltage measurements
 because of their low thermal characteristics. Use a cable with at least 90%
 shielding effectiveness.

| Type of Insulator | AWG | Conductor Material | Resistance per Foot | Capacitance per Foot |
| --- | --- | --- | --- | --- |
| TFE | 26 | Silver-plated copper, stranded | 39 mΩ | 35.5 pF |

#### Operation

The NI 4082 can
 operate as a DMM and can acquire waveforms up to 1.8 MS/s. Refer to the NI
 PXIe-4082 Specifications document for a full list of functions and
 ranges supported by the NI 4082.

The following table lists the functions and
 ranges supported by the NI 4082 while in DMM mode.

| DMM Function | Ranges |
| --- | --- |
| DC Voltage | 100 mV, 1 V, 10 V, 100 V, 300 V |
| AC Voltage | 50 mV, 500 mV, 5 V, 50 V, 300 V |
| DC Current1 | 20 mA, 200 mA, 1 A |
| AC Current1 | 10 mA, 100 mA, 1 A |
| 2-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ, 100 MΩ |
| 4-Wire Resistance | 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ, 10 MΩ |
| Diode | 10 V at 1 µA / 10µA / 100µA; 4.5 V at 1 mA |
| Frequency/Period2 | 15 Hz - 500 kHz / 2 µs - 67 ms |
| Capacitance | 300 pF, 1 nF, 10 nF, 100 nF, 1 µF, 10 µF, 100 µF, 1,000 µF, 10,000 µF |
| Inductance | 10 µH, 100 µH, 1 mH, 10 mH, 100 mH, 1 H, 5 H |
| 1To measure current outside of the normal range on the NI 4082, you must use a current shunt module (CSM). Refer to Measuring Current for more information. 2Frequency/Period voltage ranges are the same as AC voltage ranges. |  |

The following table lists the functions and ranges supported for waveform
 acquisitions:

| Waveform Function | Ranges | Coupling |
| --- | --- | --- |
| Voltage Waveform | 100 mV, 1 V, 10 V, 100 V, 300 V | AC or DC |
| Current Waveform1 | 20 mA, 200 mA, 1 A | DC |
| 1To measure current outside of the normal range on the NI 4082, you must use a current shunt module (CSM). Refer to the Measuring Current section for more information. |  |  |

The following table lists the available NI 4082 input resistance selections.
 NI calibrates the NI 4082 for full accuracy with all input resistances
 shown.

| DCV | ACV | Voltage Waveform |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Range | Input Resistance | Range | Input Resistance | Range | Input Resistance |
| 100 mV | 10 MΩ (default) or 10 GΩ | 50 mV | 1 MΩ | 100 mV | 10 GΩ or 1 MΩ (default) |
| 1 V | 10 MΩ (default) or 10 GΩ | 500 mV | 1 MΩ | 1 V | 10 GΩ or 1 MΩ (default) |
| 10 V | 10 MΩ (default) or 10 GΩ | 5 V | 1 MΩ | 10 V | 10 GΩ or 1 MΩ (default) |
| 100 V | 10 MΩ (default) | 50 V | 1 MΩ | 100 V | 1 MΩ (default) |
| 300 V | 10 MΩ (default) | 300 V | 1 MΩ | 300 V | 1 MΩ (default) |

#### Additional Features

- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating Measurement Complete
- Scanning Switch Modules

#### Replacing the Fuse

The NI 4082 is equipped with a 1 A 400 V time-lag fuse designed to help protect the DMM and your test system. For instructions on replacing the fuse, refer to the Fuse Replacement topic for the NI 4082.

#### Calibrating the NI
 4082

Calibration maximizes the accuracy of a DMM. To ensure accuracy, you
 must perform calibration. NI recommends that you externally calibrate every two
 years. Refer to the NI 4082 6½-Digit DMM Calibration Procedure at
 the NI Calibration Solutions Web site for information on externally calibrating the
 NI PXIe-4082. For information on calibrating the NI 4082 using Calibration
 Executive, refer to the NI Calibration Solutions Web site. All NI measurement
 devices receive NIST-traceable calibration before shipping.

Related concepts:

- OPEN/SHORT Compensation
- Self-Calibration
- Auto Zero
- Configuring Auto Range
- Offset Compensated Ohms
- ADC Calibration
- Input Resistance
- Configuring Measurement Timing
- Aperture Time
- DC Noise Rejection
- Waveform Acquisitions
- Single Point Acquisitions
- Generating a Measurement Complete Event
- Scanning Switch Modules
- Measuring Current

<!--NI_TOPIC bundle=ni-dmm path=noise.html language=enus -->
## TOPIC 00296: Noise

- bundle_id: `ni-dmm`
- source_path: `noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/noise.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise in a measurement can originate from the instrument taking the measurement or from an interfering signal passing through the instrument and causing measurement instability. When considering noise, you need to know the measurement bandwidth because it sets the bounds for how you can manage the n

### Noise

Noise in a measurement can originate from the instrument taking the measurement or from an interfering signal passing through the instrument and causing measurement instability. When considering noise, you need to know the measurement bandwidth because it sets the bounds for how you can manage the noise. You can decrease the measurement bandwidth by increasing the aperture of the measurement or by averaging the measurement.

Noise in the system is a common challenge in designing measurement systems. Noise sources in the environment can be electrostatically or inductively coupled in from the powerline; therefore, most DMMs specify noise rejection at line frequencies of 50 Hz or 60 Hz. The rejection at 400 Hz is, at a minimum, as good as the rejection at 50 Hz because the aperture time for 50 Hz also eliminates 400 Hz components. For more information about how to configure the NI 4065 and NI 4070/4071/4072 for optimum normal-mode rejection ratio (NMRR), refer to DC Noise Rejection.

#### Johnson Noise of Resistors

A commonly overlooked source of noise in precision instrumentation is the source noise resistance, as shown in the following figure.

[IMAGE alt='image' src='GUID-8533C4B6-5B32-48FE-B85B-0050C3533615-a5.svg']

Even a simple fixed-value resistor is noisy. The inherent noise generated by a non-ideal resistor is represented by a noise voltage source (e<sub>nr</sub>) in series with the ideal, noise-free resistance. This noise results from random motion of thermally generated electrons in the material. This signal is usually called Johnson noise. The Johnson's equation normalized to 1 kΩ results in the following equation:

V<sub>n</sub> = 4[√(R/1 kΩ)][(nV/√(Hz))]

e<sub>nr</sub> = √(4kTRf)

This noise, which is present in every resistor at common laboratory temperatures, is a function of temperature, the value of the resistance, and the bandwidth of the measurement. The noise is defined as:

e<sub>nr</sub> = 1.28*10<sup>–10</sup>*√(Rf) rms

You can convert this equation to:

e<sub>nr</sub> = 8.45 * 10<sup>–10</sup> * √(Rf) p–p

where

R =resistance being measured

f = noise bandwidth of the measurement

This equation assumes you are using ideal resistor elements that exhibit white noise. The white noise is assumed to be a Gaussian distribution. Some resistors, such as certain carbon film resistors, can generate noise from other mechanisms when current is passed through them. Metal foil and wire wound resistors approach this theoretical limit.

As a point of reference to simplify the calculation, a 1 kΩ resistor has [IMAGE alt='image' src='GUID-B1991B64-E670-4C13-A262-D317C98FA46E-a5.gif'] rms noise density (1 Hz bandwidth). You can scale this value to get to any noise level given any resistor or frequency by multiplying it by [IMAGE alt='image' src='GUID-ADD1D35B-49C3-4B9D-BF6F-43EDF353E277-a5.gif']. For example, a 100 kΩ resistor in a 100 Hz bandwidth has a noise of:

e<sub>nr</sub> = 4 nV√(Hz) * √(100 * (100 kΩ / 1 kΩ))

e<sub>nr</sub> = 400 nVrms

If the DMM is digitizing at 1 kS/s, the measurement bandwidth is 1 kHz and the effective noise is:

e<sub>nr</sub> = 4 nV√(Hz) * √(1,000 * (100 kΩ / 1 kΩ))

e<sub>nr</sub> = 4 nV x 316

e<sub>nr</sub> = 1.26 µVrms or 8.3 µV<sub>p-p</sub>

Thus, the source resistance limits the noise floor of the measurement over a 1 kHz bandwidth to 8.3 µVp-p.

Parent topic:

Measurement Quality

Related concepts:

- Configuring Measurement Timing
- Normal-Mode Rejection Ratio (NMRR)
- DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=normal-and-common-mode-signals.html language=enus -->
## TOPIC 00297: Normal and Common-Mode Signals

- bundle_id: `ni-dmm`
- source_path: `normal-and-common-mode-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/normal-and-common-mode-signals.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A normal-mode signal is a signal applied differentially to the DMM front panel connectors for the purpose of measuring that signal, as shown in the following figure.A common-mode signal is the component of an input, "common" to the differential input, as shown in the following figure.

### Normal and Common-Mode Signals

A normal-mode signal is a signal applied differentially to the DMM front panel connectors for the purpose of measuring that signal, as shown in the following figure.

[IMAGE alt='image' src='GUID-E37A33F4-E727-4EAE-8A08-06980A9B5570-a5.svg']

A common-mode signal is the component of an input, "common" to the differential input, as shown in the following figure.

[IMAGE alt='image' src='GUID-A179AADD-FE90-4BE1-9860-21F0288F4187-a5.svg']

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=normal-mode-rejection-ratio-nmrr.html language=enus -->
## TOPIC 00298: Normal-Mode Rejection Ratio (NMRR)

- bundle_id: `ni-dmm`
- source_path: `normal-mode-rejection-ratio-nmrr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/normal-mode-rejection-ratio-nmrr.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Normal-mode rejection ratio (NMRR) describes the ability of the DMM to reject an AC normal-mode signal, usually at powerline frequencies. NMRR is given by the following formula:NMRR = 20*log(V[in]/V[error])where V[error] is the value returned by the DMM for an applied AC normal-mode voltage V[in].NM

### Normal-Mode Rejection Ratio (NMRR)

Normal-mode rejection ratio (NMRR) describes the ability of the DMM to reject an AC normal-mode signal, usually at powerline frequencies. NMRR is given by the following formula:

NMRR = 20*log(V<sub>in</sub>/V<sub>error</sub>)

where V<sub>error</sub> is the value returned by the DMM for an applied AC normal-mode voltage V<sub>in</sub>.

NMRR is useful for measurement systems that can eliminate signals at a given frequency or over a range of frequencies. NMRR, which is often used to indicate the capability of the instrument to reject powerline noise of 50 or 60 Hz, is valid only at the specified frequency and is useful when making DC measurements.

Parent topic:

Measurement Considerations

Related concepts:

- Normal and Common-Mode Signals

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem.html language=enus -->
## TOPIC 00299: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

Related concepts:

- Analog Bandwidth

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem_2.html language=enus -->
## TOPIC 00300: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem_3.html language=enus -->
## TOPIC 00301: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem_4.html language=enus -->
## TOPIC 00302: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem_5.html language=enus -->
## TOPIC 00303: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=nyquist-theorem_6.html language=enus -->
## TOPIC 00304: Nyquist Theorem

- bundle_id: `ni-dmm`
- source_path: `nyquist-theorem_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/nyquist-theorem_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the bandwidth of the signal; otherwise, aliased products in the band of interest can distort the signal, causing loss of information. An alias is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows an 800 kHz sine wave digitized by a 1 MS/s ADC. The dotted line indicates the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-E7B00B64-91F5-47E4-89A2-F1875215EECA-a5.svg']

The 800 kHz frequency aliases back in the passband, falsely appearing as a 200 kHz sine wave. To prevent aliasing in the passband, a lowpass filter limits the frequency content of the input signal above the Nyquist rate. The analog bandwidth of the DMM is 300 kHz and you can avoid aliased signals in that passband by sampling at the full rate of 1.8 MS/s.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms.html language=enus -->
## TOPIC 00305: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

Related concepts:

- Resistance
- Configuring Offset Compensated Ohms

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms_2.html language=enus -->
## TOPIC 00306: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms_3.html language=enus -->
## TOPIC 00307: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms_4.html language=enus -->
## TOPIC 00308: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms_5.html language=enus -->
## TOPIC 00309: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=offset-compensated-ohms_6.html language=enus -->
## TOPIC 00310: Offset Compensated Ohms

- bundle_id: `ni-dmm`
- source_path: `offset-compensated-ohms_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-compensated-ohms_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the curren

### Offset Compensated Ohms

Offset Compensated Ohms eliminates thermal EMFs or offset voltages in a resistance test system. Offset Compensated Ohms applies to both 2-wire and 4-wire resistance. The measurement involves two cycles as shown in the following figures. The following figure represents the first cycle with the current source ON:

[IMAGE alt='image' src='GUID-3028DD7C-A514-44BF-9444-A0B3F1FFD7BE-a5.svg']

The following figure represents the second cycle with the current source OFF:

[IMAGE alt='image' src='GUID-A2442CC2-4630-411A-A16E-C5BFE414BF57-a5.svg']

The net result is the difference between the two measurements. Because the offset voltage is present in both cycles, it is subtracted out and does not affect the resistance calculation.

V<sub>OCO</sub> = V<sub>M1</sub>—V<sub>M2</sub> = (I<sub>S</sub>R<sub>X</sub> + V<sub>THERMAL</sub>)—V<sub>THERMAL</sub>= I<sub>S</sub>R<sub>X</sub>

therefore:

R<sub>X</sub> = V<sub>OCO</sub>/I<sub>S</sub>

#### When to Use Offset Compensated
 Ohms

4-wire measurements are accurate if you use copper interconnects and
 low-thermal relays in your measurement system. However, there are situations when
 offset voltages present introduce significant errors:

1. Switching systems using uncompensated reed relays can have offset voltages
 >10 µV due to the Kovar lead material used at the device glass seal.
2. In-circuit resistance measurements, for example, power supply conductors being
 measured for resistance, while the circuit is live.
3. Measuring the on-resistance of batteries, dynamic resistance of forward biased
 diodes, and so on.

In the case of scenario 1, often a test system is built with switching optimized
 for other things besides resistance measurements. For example, reed relays are
 common in RF test systems due to their predictable impedance characteristics and
 high reliability. In such a system you may want to also measure resistances. It
 might not be economical to add switching hardware for a few channels of resistance,
 and the RF relays may already be present.

In the case of scenario 2, an
 example would be measuring the resistance of a power supply bus cable. The
 resistance might be 10 mΩ. If 100 mA is flowing through this resistance, the voltage
 drop is:

V = 100 mA x 10 mΩ = 1 mV

The DMM without
 offset compensation on the 100 Ω range interprets this as 1.05 Ω (recall from the
 table of Source Current and Maximum Test Voltages that 105 Ω corresponds to
 nominally 100 mV). With the DMM and Offset Compensation, the 1 mV offset is
 rejected, and the correct value of resistance is returned.

In the case of
 scenario 3, remember that this test only works if the diode is already forward
 biased. The DMM does not supply a DC bias to the diode in Offset Compensated Ohms.
 The DMM does provide the small signal displacement current, but the diode still
 needs to be biased. The following figure shows this diode example:

[IMAGE alt='image' src='GUID-B05BEB2A-5FE3-4534-963D-C4A512D9228B-a5.svg']

To get
 the dynamic resistance of the diode (or transistor) the selection of the appropriate
 measurement range is key. NI recommends selecting a range with a corresponding
 current source value 10% of the bias current level or less.

NI does not
 recommend using the DMM to directly measure the series resistance of cells greater
 than 1 V. The DMM does not have enough voltage dynamic range to do this on the lower
 resistance ranges. Of course, you can use the DMM in conjunction with an external
 current source or load to do this.

As a general rule for measuring resistances
 in the presence of large DC offsets, do not violate the following formula, or the
 results may be erroneous:

V<sub>os</sub>+ I<sub>s</sub>R<sub>x</sub> ≤
 V<sub>t</sub>

where

V<sub>os</sub> is the offset voltage (what you
 are trying to compensate out)

I<sub>s</sub> is the source current (dependent
 on range, refer to the table above)

R<sub>x</sub> is the resistance being
 measured (or its upper bound)

V<sub>t</sub> is the maximum test voltage (from
 table above)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=offset-errors.html language=enus -->
## TOPIC 00311: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=offset-errors_2.html language=enus -->
## TOPIC 00312: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=offset-errors_3.html language=enus -->
## TOPIC 00313: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=offset-errors_4.html language=enus -->
## TOPIC 00314: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=offset-errors_5.html language=enus -->
## TOPIC 00315: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=offset-errors_6.html language=enus -->
## TOPIC 00316: Offset Errors

- bundle_id: `ni-dmm`
- source_path: `offset-errors_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/offset-errors_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise present on the input signal path of a DMM results in offset on the AC[rms] function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs. As an example, assume a 0.5 mV offset error on the 5 V range exists. If an in

### Offset Errors

Noise present on the input signal path of a DMM results in offset on the AC<sub>rms</sub> function. It is not advisable to reduce this error by doing a subtraction operation because the value displayed is the rms sum of the inputs.

As an example, assume a 0.5 mV offset error on the 5 V range exists. If an input of 50 mV<sub>rms</sub> is applied, the reading is:

Reading = √(S<sup>2</sup> + N<sup>2</sup>)

Reading = √[(50 mV)<sup>2</sup> + (0.5 mV)<sup>2</sup>]

Reading = 50.0025 mV<sub>rms</sub>

What appeared to be a huge offset error now accounts for only a 0.005% error in the measurement because of the rms conversion.

50 mV—0.5 mV = 49.5 mV

This result represents a 1% error.

Parent topic:

AC Voltage

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements.html language=enus -->
## TOPIC 00317: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

Related concepts:

- Measuring on the 100 MΩ Range

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_2.html language=enus -->
## TOPIC 00318: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_3.html language=enus -->
## TOPIC 00319: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_4.html language=enus -->
## TOPIC 00320: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_5.html language=enus -->
## TOPIC 00321: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_6.html language=enus -->
## TOPIC 00322: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-for-high-resistance-measurements_7.html language=enus -->
## TOPIC 00323: Optimizing for High-Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-for-high-resistance-measurements_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-for-high-resistance-measurements_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section f

### Optimizing for High-Resistance Measurements

The techniques required to accurately measure high resistances are somewhat different than those required for low resistances. Electrostatic noise pickup becomes a major concern. To prevent problems with noise pickup, shielding must be considered. Refer to the Measuring on the 100 MΩ Range section for more information.

#### Shielding

Proper shielding is critical when measuring resistances >100 kΩ. High-resistance measurements are extremely sensitive to environmental noise such as powerline pickup, changes in electrostatic fields caused by people moving nearby, and even RF pickup. For these reasons, NI strong recommends using shielded cables when measuring high resistances. For 2-wire measurements, the shield should be tied to the LO terminal. For 4-wire measurements, there are two pairs of shielded cables. The first pair should be tied to HI and LO (shield to LO), and the second pair to HI SENSE and LO SENSE (shield to LO SENSE). Refer to the figure below:

[IMAGE alt='image' src='GUID-6032FDB1-7648-4B65-BA67-3514195A18DE-a5.svg']

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=optimizing-low-voltage-measurements.html language=enus -->
## TOPIC 00324: Optimizing Low-Voltage Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-low-voltage-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-low-voltage-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then

### Optimizing Low-Voltage Measurements

As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then you have two junctions of dissimilar metals. This basic concept can be extended to just about any other setup.

If the two jacks are at different temperatures, then a voltage is generated. The amplitude of the voltage depends on the other metal that is being used. If the other metal is copper, then the Seebeck coefficient for copper to copper is very low-well under 100 nV/°C, as long as the connections are clean and tight.

A temperature difference between the two jacks greater than 1–2 °C would be rare, but a temperature difference does exist. The interior of the PXI chassis is warmer than the outside air creating heat flow that ultimately results in a temperature difference.

For copper-to-copper connections, the generated voltage is relatively small. If you used brass instead of copper where a 1–2 °C temperature difference exists, there could be a 6 µV difference in the measurement value detectable by the DMM.

One rule for low-voltage measurements is to always use metals with Seebeck coefficients close to that of copper. Copper, gold, and silver are all good candidates. Typical Seebeck coefficients for common conductors are listed in the table in Thermal Voltage.

If the connections do not change temperatures, then the thermal voltage is stable and can be corrected; it is temperature changes between these junctions that create problems (such as offset drift, instability, and very low frequency noise). The key to preventing changes in temperature is to prevent circulating air currents that can disturb the thermal equilibrium of the junctions. This leads to another rule for low-voltage measurements-keep junctions and connections at a stable temperature and away from circulating air currents caused by movement, fans, and so on. You can prevent these temperature differences by creating a "thermal baffle," such as wrapping the junctions with common foam padding (even Styrofoam sheet can work) and keeping them away from sources of heat such as equipment heat sinks and sunlight.

Even common lead-tin solder connections can create thermal offsets of (1–3 µV/°C). While not insignificant, they can be managed using the techniques described above. For increased performance, cold weld connections by tightly twisting clean copper-to-copper connections together and then using either crimped or twist-on plastic connectors.

When copper oxidizes, the Seebeck coefficient can easily increase by several hundred µV/°C. This
 leads to another rule for low-voltage measurements-keep the connections clean. One
 option is to simply use a pencil eraser to clean the bare wire until the wire is
 shiny, then clean off any rubber fragments with a paper towel. Another way to clean
 connections is to use Scotch-Brite pads to clean the wire. After cleaning the
 connections, do not handle the connections with your fingers. Skin oil contains a
 very effective corrosive that accelerates oxidation of many metals.

Refer to Switching Voltages for recommendations on reading low voltage signals through switches.

Parent topic:

DC Voltage

Related concepts:

- Thermal Voltages
- Switching Voltages

<!--NI_TOPIC bundle=ni-dmm path=optimizing-low-voltage-measurements_2.html language=enus -->
## TOPIC 00325: Optimizing Low-Voltage Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-low-voltage-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-low-voltage-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then

### Optimizing Low-Voltage Measurements

As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then you have two junctions of dissimilar metals. This basic concept can be extended to just about any other setup.

If the two jacks are at different temperatures, then a voltage is generated. The amplitude of the voltage depends on the other metal that is being used. If the other metal is copper, then the Seebeck coefficient for copper to copper is very low-well under 100 nV/°C, as long as the connections are clean and tight.

A temperature difference between the two jacks greater than 1–2 °C would be rare, but a temperature difference does exist. The interior of the PXI chassis is warmer than the outside air creating heat flow that ultimately results in a temperature difference.

For copper-to-copper connections, the generated voltage is relatively small. If you used brass instead of copper where a 1–2 °C temperature difference exists, there could be a 6 µV difference in the measurement value detectable by the DMM.

One rule for low-voltage measurements is to always use metals with Seebeck coefficients close to that of copper. Copper, gold, and silver are all good candidates. Typical Seebeck coefficients for common conductors are listed in the table in Thermal Voltage.

If the connections do not change temperatures, then the thermal voltage is stable and can be corrected; it is temperature changes between these junctions that create problems (such as offset drift, instability, and very low frequency noise). The key to preventing changes in temperature is to prevent circulating air currents that can disturb the thermal equilibrium of the junctions. This leads to another rule for low-voltage measurements-keep junctions and connections at a stable temperature and away from circulating air currents caused by movement, fans, and so on. You can prevent these temperature differences by creating a "thermal baffle," such as wrapping the junctions with common foam padding (even Styrofoam sheet can work) and keeping them away from sources of heat such as equipment heat sinks and sunlight.

Even common lead-tin solder connections can create thermal offsets of (1–3 µV/°C). While not insignificant, they can be managed using the techniques described above. For increased performance, cold weld connections by tightly twisting clean copper-to-copper connections together and then using either crimped or twist-on plastic connectors.

When copper oxidizes, the Seebeck coefficient can easily increase by several hundred µV/°C. This
 leads to another rule for low-voltage measurements-keep the connections clean. One
 option is to simply use a pencil eraser to clean the bare wire until the wire is
 shiny, then clean off any rubber fragments with a paper towel. Another way to clean
 connections is to use Scotch-Brite pads to clean the wire. After cleaning the
 connections, do not handle the connections with your fingers. Skin oil contains a
 very effective corrosive that accelerates oxidation of many metals.

Refer to Switching Voltages for recommendations on reading low voltage signals through switches.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=optimizing-low-voltage-measurements_3.html language=enus -->
## TOPIC 00326: Optimizing Low-Voltage Measurements

- bundle_id: `ni-dmm`
- source_path: `optimizing-low-voltage-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/optimizing-low-voltage-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then

### Optimizing Low-Voltage Measurements

As discussed in Thermal Voltages, pairs of dissimilar metal junctions—rather than a single junction—potentially can create problems. The NI 4070/4071/4072 uses proprietary gold-plated copper input leads (HI and LO). If you just connect these two jacks directly with some wire that is not copper, then you have two junctions of dissimilar metals. This basic concept can be extended to just about any other setup.

If the two jacks are at different temperatures, then a voltage is generated. The amplitude of the voltage depends on the other metal that is being used. If the other metal is copper, then the Seebeck coefficient for copper to copper is very low-well under 100 nV/°C, as long as the connections are clean and tight.

A temperature difference between the two jacks greater than 1–2 °C would be rare, but a temperature difference does exist. The interior of the PXI chassis is warmer than the outside air creating heat flow that ultimately results in a temperature difference.

For copper-to-copper connections, the generated voltage is relatively small. If you used brass instead of copper where a 1–2 °C temperature difference exists, there could be a 6 µV difference in the measurement value detectable by the DMM.

One rule for low-voltage measurements is to always use metals with Seebeck coefficients close to that of copper. Copper, gold, and silver are all good candidates. Typical Seebeck coefficients for common conductors are listed in the table in Thermal Voltage.

If the connections do not change temperatures, then the thermal voltage is stable and can be corrected; it is temperature changes between these junctions that create problems (such as offset drift, instability, and very low frequency noise). The key to preventing changes in temperature is to prevent circulating air currents that can disturb the thermal equilibrium of the junctions. This leads to another rule for low-voltage measurements-keep junctions and connections at a stable temperature and away from circulating air currents caused by movement, fans, and so on. You can prevent these temperature differences by creating a "thermal baffle," such as wrapping the junctions with common foam padding (even Styrofoam sheet can work) and keeping them away from sources of heat such as equipment heat sinks and sunlight.

Even common lead-tin solder connections can create thermal offsets of (1–3 µV/°C). While not insignificant, they can be managed using the techniques described above. For increased performance, cold weld connections by tightly twisting clean copper-to-copper connections together and then using either crimped or twist-on plastic connectors.

When copper oxidizes, the Seebeck coefficient can easily increase by several hundred µV/°C. This
 leads to another rule for low-voltage measurements-keep the connections clean. One
 option is to simply use a pencil eraser to clean the bare wire until the wire is
 shiny, then clean off any rubber fragments with a paper towel. Another way to clean
 connections is to use Scotch-Brite pads to clean the wire. After cleaning the
 connections, do not handle the connections with your fingers. Skin oil contains a
 very effective corrosive that accelerates oxidation of many metals.

Refer to Switching Voltages for recommendations on reading low voltage signals through switches.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=overrange.html language=enus -->
## TOPIC 00327: Overrange

- bundle_id: `ni-dmm`
- source_path: `overrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overrange.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the overrange conditions for the PXI/PCI/PCIe/USB‑4065. Function Overrange^1 DC Functions:Voltage, Current, Resistance, and Diode All ranges, except 300 V and 3 A: Occurs above 105% of the range. Above 105%, NI-DMM returns NaN^2 (except for the 100 MΩ range on the NI 4065) and

### Overrange

This section describes the overrange conditions for the PXI/PCI/PCIe/USB‑4065.

| Function | Overrange1 |
| --- | --- |
| DC Functions:Voltage, Current, Resistance, and Diode | All ranges, except 300 V and 3 A: Occurs above 105% of the range. Above 105%, NI-DMM returns NaN2 (except for the 100 MΩ range on the NI 4065) and the IVI overrange warning. For the 100 MΩ range on the NI 4065, measurements between the 105 MΩ and 1.05 GΩ ranges have a typical accuracy of 5%, although NI-DMM returns the IVI overrange warning. For measurements above 1.05 GΩ, NI‑DMM returns NaN2 and the IVI overrange warning instead of the reading. 300 V and 3 A ranges: Occurs above 100% of the range. Above 100%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. |
| AC Functions:Voltage and Current | All ranges, except 300 V and 3 A: Occurs above 105% of the range. Above 105%, NI-DMM returns NaN2 and the IVI overrange warning. 300 V and 3 A ranges: Occurs above 100% of the range. Above 100%, NI-DMM returns readings (not NaN2) and the IVI overrange warning, even though the readings are not guaranteed within specifications. |
| 1Refer to the NI IVI Driver Help at ni.com/manuals for the IVI overrange warning code. 2 NaN is a digital display value for a floating-point representation of "Not a Number," as defined by the IEEE standard for binary floating point arithmetic. NaN is typically the result of an undefined operation, such as log(-1). |  |

Parent topic:

NI 4065 DMM Measurement Cycle

<!--NI_TOPIC bundle=ni-dmm path=overranging.html language=enus -->
## TOPIC 00328: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=overranging_2.html language=enus -->
## TOPIC 00329: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=overranging_3.html language=enus -->
## TOPIC 00330: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=overranging_4.html language=enus -->
## TOPIC 00331: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=overranging_5.html language=enus -->
## TOPIC 00332: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=overranging_6.html language=enus -->
## TOPIC 00333: Overranging

- bundle_id: `ni-dmm`
- source_path: `overranging_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/overranging_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For

### Overranging

The DMM sigma-delta modulator has a characteristic overload recovery behavior that you must be aware of when selecting the range of measurement for waveform acquisition. Select the input range carefully, so that the acquired signals, including instantaneous peaks, are within range at all times. For instance, when the device is configured for the 10 V input range, the signal must remain within +/- 10.5 VDC (21 V<sub>P–P</sub>). Signals applied to the device that are outside of the input range cause the sigma-delta modulator within the ADC to enter into an overrange condition. In this condition, the software returns the value of NaN (Not a Number) for all the measurements during the time that the signal is outside the range. During recovery from an overrange condition, the device may return several invalid data points once the signal recovers to within the range limits. To prevent the ADC from being saturated, it is imperative that the signal being measured is always within the input range limits. When the input signal is outside the limits, the niDMM Read Waveform and niDMM Fetch Waveform functions return an overrange warning. If your application encounters this warning, you should consider your data to be corrupted, and you should acquire the data again with the appropriate input range selections.

We recommend starting with the highest available range first before settling on the range of measurement. By doing this, it is possible to get a "preview" of the measured waveform while avoiding transient overloads caused by slew rate limitations. This is also a good way to determine the signal peaks before zooming in with a more sensitive range.

The frequency response is similar across all ranges, so there is no loss of signal integrity by using this approach. If the signal is small, some resolution is lost. However, once you identify this small signal and loss of resolution, you can carefully select a more sensitive range.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling.html language=enus -->
## TOPIC 00334: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Capacitance/Inductance

Related concepts:

- Offset Compensated Ohms
- OPEN/SHORT Compensation
- Thermal Voltages

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_10.html language=enus -->
## TOPIC 00335: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_10.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_10.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_11.html language=enus -->
## TOPIC 00336: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_11.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_11.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_12.html language=enus -->
## TOPIC 00337: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_12.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_12.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Capacitance/Inductance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_13.html language=enus -->
## TOPIC 00338: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_13.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_13.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_14.html language=enus -->
## TOPIC 00339: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_14.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_14.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_15.html language=enus -->
## TOPIC 00340: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_15.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_15.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_16.html language=enus -->
## TOPIC 00341: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_16.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_16.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_17.html language=enus -->
## TOPIC 00342: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_17.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_17.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_18.html language=enus -->
## TOPIC 00343: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_18.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_18.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_19.html language=enus -->
## TOPIC 00344: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_19.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_19.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_2.html language=enus -->
## TOPIC 00345: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_20.html language=enus -->
## TOPIC 00346: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_20.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_20.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_21.html language=enus -->
## TOPIC 00347: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_21.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_21.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_22.html language=enus -->
## TOPIC 00348: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_22.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_22.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_3.html language=enus -->
## TOPIC 00349: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_4.html language=enus -->
## TOPIC 00350: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_5.html language=enus -->
## TOPIC 00351: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_6.html language=enus -->
## TOPIC 00352: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_7.html language=enus -->
## TOPIC 00353: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_8.html language=enus -->
## TOPIC 00354: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_8.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=performing-offset-nulling_9.html language=enus -->
## TOPIC 00355: Performing Offset Nulling

- bundle_id: `ni-dmm`
- source_path: `performing-offset-nulling_9.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-offset-nulling_9.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.To perform offset nulling, complete the following

### Performing Offset Nulling

Offset nulling consists of measuring the corresponding zero reading in a measurement path and subtracting this value from subsequent samples.

The way you connect the leads to obtain the zero reading depends upon the type of measurement you are taking.

To perform offset nulling, complete the following steps:

1. Disconnect the DUT from the leads that are connected to the DMM.
2. If you are measuring DC voltage, inductance, or resistance, short the input leads to obtain the corresponding zero reading. If you are measuring DC current or capacitance, leave the leads unconnected (open circuit) to obtain the corresponding zero reading. In a switching system, you can make the open-circuit or short-circuit measurement with channels dedicated as short or as an open. NI recommends using cables and switches with low thermal voltages and low-path resistance to minimize the offset introduced by the measurement path. Refer to the Thermal Voltages section for more information.
3. Record the value of the measurement.
4. Connect the leads to the DUT, and subtract the value measured in step 3 from all subsequent measurements.

The subtraction operation can be performed programmatically with the ADE or using offset nulling in InstrumentStudio.

For capacitance and inductance measurements, NI recommends using OPEN/SHORT compensation rather than offset nulling to remove offset errors. OPEN/SHORT compensation performs a fixture/cable characterization at the test frequency to compensate for offset and gain errors, while offset nulling only performs an arithmetic subtraction of the offset present in the fixture/cable.

For resistance measurements in the ranges ≤10 kΩ, you can enable offset compensated ohms, which removes offsets in the measurement path much better than offset nulling alone.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=performing-self-calibration.html language=enus -->
## TOPIC 00356: Performing Self-Calibration

- bundle_id: `ni-dmm`
- source_path: `performing-self-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/performing-self-calibration.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Run the self-calibration routine:LabVIEW—Use niDMM Self Cal.CVI, C++, or Visual Basic—Use niDMM_SelfCal. This feature is supported on the NI 4080/4081/4082 and the NI 4070/4072/4072.

### Performing Self-Calibration

Run the self-calibration routine:

LabVIEW—Use niDMM Self Cal.CVI, C++, or Visual Basic—Use niDMM_SelfCal.

Note

Parent topic:

Features

Related concepts:

- Self-Calibration

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=precision.html language=enus -->
## TOPIC 00357: Precision

- bundle_id: `ni-dmm`
- source_path: `precision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/precision.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Precision is a measure of the stability of the DMM and the repeatability of its measurement results for the same input signal. Resolution is a measure of the precision. Precision is given by:Precision = 1 – |X[n] – Av(X[n])|/|Av(X[n])|where X[n] = the value of the nth measurementAv(X[n]) = the avera

### Precision

Precision is a measure of the stability of the DMM and the repeatability of its measurement results for the same input signal. Resolution is a measure of the precision. Precision is given by:

Precision = 1 – |X<sub>n</sub> – Av(X<sub>n</sub>)|/|Av(X<sub>n</sub>)|

where

X<sub>n</sub> = the value of the nth measurement

Av(X<sub>n</sub>) = the average value of the set of n measurements

For example, if you are monitoring a constant voltage of 1 V, and your measured value changes by 20 µV between measurements, then your measurement precision is:

Precision (1 – 20 µV/1 V) x 100 = 99.998%

Precision is most valuable when you are using the DMM to calibrate a device or perform relative measurements.

Parent topic:

Measurement Quality

<!--NI_TOPIC bundle=ni-dmm path=programming-flow.html language=enus -->
## TOPIC 00358: Programming Flow

- bundle_id: `ni-dmm`
- source_path: `programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/programming-flow.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the basic programming flow of applications using NI-DMM. NI-DMM functions and VIs are organized under the Initialize, Configure Hardware, Read or Fetch Data, and Close categories to assist you in understanding where you should call a function or VI in your applications. F

### Programming Flow

The following diagram shows the basic
 programming flow of applications using NI-DMM. NI-DMM functions and VIs are
 organized under the Initialize, Configure Hardware, Read or Fetch Data, and Close
 categories to assist you in understanding where you should call a function or VI in
 your applications. Functions and VIs that do not fall into the programming flow are
 considered Utility functions that perform various tasks such as resetting the DMM,
 returning the revision number of the NI-DMM driver and instrument firmware, and
 other functions.

[IMAGE alt='image' src='GUID-FCCC2BD6-8AE2-4E19-A174-8A141B473929-a5.svg']

Tip

Parent topic:

Programming with NI-DMM

Related concepts:

- Using Attributes and Properties with NI-DMM

<!--NI_TOPIC bundle=ni-dmm path=programming-with-ni-dmm.html language=enus -->
## TOPIC 00359: Programming with NI-DMM

- bundle_id: `ni-dmm`
- source_path: `programming-with-ni-dmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/programming-with-ni-dmm.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can control your NI digital multimeter using the NI-DMM instrument driver.NI-DMMNI-DMM, an Interchangeable Virtual Instrument (IVI)–compliant instrument driver, is included with your kit and communicates with all NI digital multimeters. NI-DMM features a set of operations and properties that exe

### Programming with NI-DMM

You can control your NI digital multimeter using the NI-DMM instrument driver.

#### NI-DMM

NI-DMM, an Interchangeable Virtual Instrument (IVI)–compliant instrument driver, is included with your kit and communicates with all NI digital multimeters. NI-DMM features a set of operations and properties that exercise the functionality of the DMM hardware, including configuration, measuring, and scanning. In addition, NI-DMM comes with InstrumentStudio, a software-based front panel application that allows you to perform interactive measurements. NI-DMM eliminates the need to understand complex register programming and interrupt handling in the Microsoft operating systems, and frees you to focus on creating a test system.

#### Making Signal
 Connections

To acquire data, you need to connect the signals you want to
 measure to the DMM. For more information, refer to the front panel connections for
 your device linked under *Related concepts*.

#### Examples

Refer to
 *Creating an Application with NI-DMM* to begin controlling your DMM
 with NI-DMM. Refer to *Examples* for examples in NI LabVIEW,
 LabWindows/CVI, Visual C++, and Visual Basic.

Related concepts:

- InstrumentStudio
- PXI/PCI/PCIe-4065 Front Panel Connections
- Front Panel Connections
- Front Panel Connections
- Front Panel Connections
- Creating an Application with NI-DMM
- Examples

<!--NI_TOPIC bundle=ni-dmm path=pxi-express-compatibility.html language=enus -->
## TOPIC 00360: PXI Express Compatibility

- bundle_id: `ni-dmm`
- source_path: `pxi-express-compatibility.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/pxi-express-compatibility.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI Systems Alliance (pxisa.org) recently defined a modification for PXI modules. Modified PXI modules provide future compatibility for systems incorporating PCI Express signaling in PXI. Previous versions of these modules had two large PXI connectors. In the modified PXI Express compatible DMM,

### PXI Express Compatibility

The PXI Systems Alliance (pxisa.org) recently defined a modification for PXI modules. Modified PXI modules provide future compatibility for systems incorporating PCI Express signaling in PXI. Previous versions of these modules had two large PXI connectors. In the modified PXI Express compatible DMM, the top connector has been replaced with a smaller connector. You may notice a series of regularly spaced holes in the printed circuit board that are not used by the smaller connector.

[IMAGE alt='image' src='GUID-C37C3340-3A8A-49F4-A5A5-3DB15435F090-a5.svg']

1. PXI DMM
2. PXI Express Compatible DMM

Modified PXI modules are supported by new hybrid PXI chassis slots that can accept either future PXI Express modules or existing modified PXI modules. To provide future compatibility, modified modules do not include the pins used to implement 64-bit PCI and local bus. NI PXI modules do not implement 64-bit PCI. The following functionality is preserved in the smaller top connector:

- All PXI chassis accept modified PXI modules.
- Product specifications are the same.
- No software changes (application or driver software) are required.
- Modified PXI modules are compatible with existing PXI timing and PXI triggering capabilities.
- The speed and capability of all PXI communication is unchanged.

PXI Express compatible DMMs do not support SCXI control and triggering via the backplane of a PXI/SCXI combination chassis.

PXI Express compatible DMMs are capable of SCXI control and triggering in an NI PXI-1010/1050 chassis using external cabling with an NI SCXI-1357/1358/1359 communication backplane. PXI Express compatible DMMs are not capable of controlling SCXI in an NI PXI-1011/1052 chassis. You can still accomplish SCXI triggering when using the NI PXI-1011/1052 chassis by cabling from the DMM to the SCXI module front panel.

For more information on SCXI control and triggering using a PXI/SCXI combination chassis, reference KnowledgeBase entry 3V07KP2W. Refer to ni.com/support to access the KnowledgeBase.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-dmm path=relay-forms.html language=enus -->
## TOPIC 00361: Relay Forms

- bundle_id: `ni-dmm`
- source_path: `relay-forms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/relay-forms.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Relays are classified by their number of poles and number of throws. The pole of a relay is the terminal common to every path. Each position that the pole can connect to is called a throw. A relay can be made of n poles and m throws. For example, a single-pole single-throw relay (SPST) has one pole

### Relay Forms

Relays are classified by their number of poles and number of throws. The pole of a relay is the terminal common to every path. Each position that the pole can connect to is called a throw. A relay can be made of n poles and m throws. For example, a single-pole single-throw relay (SPST) has one pole and one throw, as illustrated in the following figure.

[IMAGE alt='image' src='GUID-0BFB4E41-860D-4F4D-9235-7A404B0521C3-a5.svg']

A single-pole double-throw (SPDT) relay has one pole and two throws, as illustrated in the following figure.

[IMAGE alt='image' src='GUID-98CE80D8-7781-4337-9251-1A206FB3A056-a5.svg']

A double-pole double-throw (DPDT) relay has two poles, each with two simultaneously controlled throws, as illustrated in the following figure.

[IMAGE alt='image' src='GUID-4DDFB1AF-3C6C-4CF1-B797-8EABDD6D077A-a5.svg']

Relays are then classified into forms. Relay forms are categorized by the number of poles and throws as well as the default position of the relay. Three common relay forms are: A, B, and C.

#### Form A

Form A relays are SPST with a default state of normally open.

[IMAGE alt='image' src='GUID-0BFB4E41-860D-4F4D-9235-7A404B0521C3-a5.svg']

#### Form B

Form B relays are SPST with a default state of normally closed.

[IMAGE alt='image' src='GUID-EEB8B63D-D602-468A-8D48-E8701BC15122-a5.svg']

#### Form C

Form C relays are SPDT and break the connection with one throw before making contact with the other (break-before-make).

[IMAGE alt='image' src='GUID-98CE80D8-7781-4337-9251-1A206FB3A056-a5.svg']

Parent topic:

Switch Fundamentals

<!--NI_TOPIC bundle=ni-dmm path=requirements.html language=enus -->
## TOPIC 00362: NI-DMM Requirements

- bundle_id: `ni-dmm`
- source_path: `requirements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/requirements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `reference`
- source_description: Your system must meet the following minimum requirements to run and use NI-DMM. Minimum System Requirements Processor—2.53 GHz Intel Core 2 Duo processor or equivalent RAM—1 GB, 800 MHz DDR2 RAM A screen resolution of 1,024 x 768 Recommended System Processor—2.3 GHz quad-core Intel Core i7 or equiva

### NI-DMM
 Requirements

Your system must meet the following minimum requirements to run and use NI-DMM.

#### Minimum System
 Requirements

- Processor— 2.53 GHz Intel Core 2 Duo processor or equivalent
- RAM— 1 GB , 800 MHz DDR2 RAM
- A screen resolution of 1,024 x 768

#### Recommended System

- Processor— 2.3 GHz quad-core Intel Core i7 or
 equivalent
- RAM— 4 GB , dual-channel 1600 MHz DDR3 RAM

Refer to the *LabVIEW Readme* for additional system requirements and
 supported operating systems for LabVIEW.

#### Supported Operating Systems

- Windows 11
- Windows 10
- Windows Server 2022
- Windows Server 2019
- Windows Server 2016
- NI Linux® Real-Time

Note

NI-DMM no longer supports any 32-bit
 Windows operating system.

<!--NI_TOPIC bundle=ni-dmm path=residual-impedance.html language=enus -->
## TOPIC 00363: Residual Impedance

- bundle_id: `ni-dmm`
- source_path: `residual-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/residual-impedance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: For the NI 4072 only, Impedance is a measure of opposition to the flow of alternating currents. Residual impedances, which are found in series between the DMM and the DUT, result from the connectivity required between the DMM and the DUT. The residual impedance on the test application introduces an

### Residual Impedance

For the NI 4072 only,
 Impedance is a measure of opposition to the flow of
 alternating currents. Residual impedances, which are found in
 series between the DMM and the DUT, result from the connectivity required between
 the DMM and the DUT. The residual impedance on the test application introduces an
 error by dividing the voltage across the DUT. This error can affect the accuracy for
 inductance and capacitance measurements, particularly when the residual impedance is
 comparable to the impedance of the DUT. The following figure illustrates residual
 impedance in a typical measurement.

[IMAGE alt='image' src='GUID-463604A8-DE17-429D-8F5D-7F317D1AF1D2-a5.svg']

where

Z<sub>P</sub> = residual impedance, Z<sub>X</sub> = impedance
 of the DUT, V<sub>M</sub> = total input voltage measured by the DMM, V<sub>P</sub> =
 voltage drop across total residual impedance, V<sub>X</sub> = voltage across
 DUT

V<sub>M</sub> = V<sub>P</sub> + V<sub>X</sub>Z<sub>M</sub> =
 V<sub>M</sub> / I = V<sub>P</sub> /
 I + V<sub>X</sub> / I =
 Z<sub>P</sub> + Z<sub>X</sub>

Note

For example, in an application with a
 10 µH inductor in series with a 1 µH cable, the meter reads a 10% error, or 11 µH
 (10 µH + 1 µH).

To reduce residual impedances on test fixtures and cables,
 take the following steps:

- Keep the cables as short as possible.
- Avoid any variations due to mechanical vibrations, handling, and temperature
 changes.
- Use the compensation techniques available on the NI 4072. Refer to OPEN/SHORT
 Compensation for more information.

In addition to residual impedance, stray admittances can also be found in test
 setups. Refer to Stray Admittance for more information.

Parent topic:

Measurement Considerations

Related concepts:

- OPEN/SHORT Compensation
- Stray Admittance

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds.html language=enus -->
## TOPIC 00364: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

Related concepts:

- Resistor Self-Heating

Related information:

- Temperature

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_2.html language=enus -->
## TOPIC 00365: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_3.html language=enus -->
## TOPIC 00366: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_4.html language=enus -->
## TOPIC 00367: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_5.html language=enus -->
## TOPIC 00368: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_6.html language=enus -->
## TOPIC 00369: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance-temperature-detector-rtds_7.html language=enus -->
## TOPIC 00370: Resistance Temperature Detector (RTDs)

- bundle_id: `ni-dmm`
- source_path: `resistance-temperature-detector-rtds_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance-temperature-detector-rtds_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular

### Resistance Temperature Detector (RTDs)

An RTD, or Resistance Temperature Detector, is a temperature sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C.

Numerous types of RTDs exist, and they are typically defined by their material, their nominal resistance, and their temperature coefficient of resistance (TCR). The TCR, or α, of an RTD is the average temperature coefficient of resistance of the RTD from 0 to 100 °C and is the most common method of specifying the behavior of an RTD. The TCR for platinum RTDs is determined by the Callendar-Van Dusen equation.

The Callendar-Van Dusen equation is as follows:

Temperatures below 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup> + C × T<sup>3</sup> × (T – 100 °C)]

Temperatures above 0 °C:

R<sub>T</sub> = R<sub>0</sub>[1 + A × T + B × T<sup>2</sup>]

T = temperature in degrees Celsius

R<sub>T</sub> = RTD resistance at temperature T

R<sub>0</sub> = RTD nominal resistance at 0 °C

A, B, and C = coefficients listed in the following table.

The following table lists common platinum RTD types and standards supported in NI-DMM. Notice that there are some shared standards. The TCR and the Callendar-Van Dusen coefficients are more important than the standards. NI-DMM also supports user-specified A, B, and C coefficients through the custom RTD type if none of the presets below match the transducer.

| Standards | Material | TCR (α) | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- |
| IEC-751DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω | A = 3.9083 × 10-3 B = –5.775×10-7 C = –4.183×10-12 | Most common RTDs |
| Low-cost vendor compliant RTD1 | Platinum | .003750 | 1000 Ω | A = 3.81 × 10-3 B = –6.02×10-7 C = –6.0×10-12 | Low-cost RTD |
| JISC 1604 | Platinum | .003916 | 100 Ω | A = 3.9739 × 10-3 B = –5.870×10-7 C = –4.4 ×10-12 | Used primarily in Japan |
| US Industrial Standard D-100 American | Platinum | .003920 | 100 Ω | A = 3.9787 × 10-3 B = –5.8686×10-7 C = –4.167 ×10-12 | Low-cost RTD |
| US Industrial Standard American | Platinum | .003911 | 100 Ω | A = 3.9692 × 10-3 B = –5.8495×10-7 C = –4.233 ×10-12 | Low-cost RTD |
| ITS-90 | Platinum | .003928 | 100 Ω | A = 3.9888 × 10-3 B = –5.915×10-7 C = –3.85 ×10-12 | The definition of temperature |
| 1No standard. Check the TCR. |  |  |  |  |  |

Note

Temperature

#### Cabling

2-Wire RTD
 measurements are wired using the HI and LO connectors of the DMM:

[IMAGE alt='image' src='GUID-8AA44FB7-4BED-4744-ABD8-AED4A8FAA75D-a5.svg']

To use a
 3-Wire RTD configuration in a 4-wire RTD, jumper the negative end of the current
 excitation connection to the negative end of the voltage measurement connection.
 This configuration decreases the effect of lead resistance on the measurement,
 however, R<sub>lead3</sub> will still contribute some error, depending on its
 resistance:

[IMAGE alt='image' src='GUID-4F89C6F3-CEAD-49D9-A443-C6CBCEE7865F-a5.svg']

4-Wire RTD measurements are wired using the HI, LO,
 HI<sub>SENSE</sub>, and LO<sub>SENSE</sub> connectors of the DMM. This
 configuration minimizes the effects of lead resistance:

[IMAGE alt='image' src='GUID-6A49E006-0B10-48EE-ADCC-FD612B305297-a5.svg']

#### Underlying DMM Measurement

To measure temperature with an RTD, the DMM performs a 2-Wire or 4-Wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Callendar-Van Dusen equation and R<sub>0</sub>, A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 100 Ω RTD is 1 kΩ and the recommended range for a 1 kΩ RTD is 10 kΩ.

#### Self-Heating

There
 is an I<sup>2</sup>R power dissipated by the
 RTD that causes self-heating. Self-heating will actually change the resistance of
 the RTD, causing error in the measurement. RTDs are prone to self-heating because
 they require current excitation. The effects of self-heating can be minimized by
 supplying lower excitation current.

Typically, a dissipation
 constant is provided in RTD specifications. This number relates the
 power required to raise the RTD temperature by one degree of temperature. Thus, a
 25-mW/°C dissipation constant shows that if
 I<sup>2</sup>R power losses in the RTD
 equal 25 mW, then the RTD will be heated by 1 °C. The dissipation constant is
 usually specified under two conditions free air and a well-stirred oil bath. This is
 because of the difference in capacity of the medium to carry heat away from the
 device. The self-heating temperature rise can be found from the power dissipated by
 the RTD and the dissipation constant from

[IMAGE alt='image' src='GUID-CBBB1C75-55BC-4F2E-B280-F359C4E93CA7-a5.gif']

where

ΔT = temperature rise because of self-heating in
 °C

P = power dissipated in the RTD from the circuit in
 W

P<sub>D</sub> = dissipation constant
 of the RTD in W/°C

Refer to Resistor Self-Heating for more
 information.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance.html language=enus -->
## TOPIC 00371: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

Related concepts:

- 2-Wire Resistance Measurements
- 4-Wire Resistance Measurements
- Measuring on the 100 MΩ Range

<!--NI_TOPIC bundle=ni-dmm path=resistance_2.html language=enus -->
## TOPIC 00372: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance_3.html language=enus -->
## TOPIC 00373: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance_4.html language=enus -->
## TOPIC 00374: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance_5.html language=enus -->
## TOPIC 00375: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance_6.html language=enus -->
## TOPIC 00376: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistance_7.html language=enus -->
## TOPIC 00377: Resistance

- bundle_id: `ni-dmm`
- source_path: `resistance_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistance_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.With a known current and voltage, the DMM can determine resistance using Ohm's Law, as fo

### Resistance

The DMM can make resistance measurements using a constant-current technique. A current is supplied to the resistance under test, and the DMM measures the resulting voltage as represented in the following figure.

[IMAGE alt='image' src='GUID-85FA5C5C-1967-4697-A555-F0882B17C30B-a5.svg']

With a known current and voltage, the DMM can determine resistance using Ohm's Law, as follows:

V<sub>M</sub> = I<sub>s</sub>R<sub>T</sub>

where R<sub>T</sub> is the sum of all resistances

R<sub>T</sub> = R<sub>x</sub> + R<sub>LEAD</sub> + R<sub>LEAD</sub>

Therefore, the value of R<sub>x</sub> = V<sub>M</sub>/I<sub>s</sub> if R<sub>LEAD</sub> is small or negligible compared to R<sub>x</sub>.

The NI 4080/4081/4082 and NI 4070/4071/4072 generate a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) | Offset Compensated Ohms Available? |
| --- | --- | --- | --- |
| 100 Ω | 1 mA | 100 mV | Yes |
| 1 kΩ | 1 mA | 1 V | Yes |
| 10 kΩ | 100 µA | 1 V | Yes |
| 100 kΩ | 10 µA | 1 V | No |
| 1 MΩ | 10 µA | 10 V | No |
| 10 MΩ | 1 µA | 10 V | No |
| 100 MΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 5 GΩ | 1 µA \|\| 10 MΩ2 | 10 V | No |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |  |

Every time you run self-calibration, the current source recalibrates to an ultra-high stability 10 kΩ reference resistor. While the absolute tolerance of the current is ±5%, the recalibration process identifies the value to a sub-ppm precision level. The calculated value of resistance is corrected to the precision of the ultra-stable reference resistor, assuring accurate measurements.

The NI 4065 generates a highly-stable current source, I<sub>s</sub>. The table below lists the value of this current by range:

| Range | Test Current1 | Maximum Test Voltage (Vt) |
| --- | --- | --- |
| 100 Ω | 1 mA | 100 mV |
| 1 kΩ | 1 mA | 1 V |
| 10 kΩ | 100 µA | 1 V |
| 100 kΩ | 10 µA | 1 V |
| 1 MΩ | 5 µA | 5 V |
| 10 MΩ | 500 nA | 5 V |
| 100 MΩ | 500 nA \|\| 10 MΩ2 | 5 V |
| 1-10% to 0% tolerance 2Refer to Measuring on the 100 MΩ Range. |  |  |

The DMM has two modes of resistance measurement: 2-wire and 4-wire. Each mode applies the same
 precision current to the circuit, but the difference between 2-wire and 4-wire
 resistance measurements is how the voltage measurement is made.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=resistor-self-heating.html language=enus -->
## TOPIC 00378: Resistor Self-Heating

- bundle_id: `ni-dmm`
- source_path: `resistor-self-heating.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resistor-self-heating.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: As dissipation of power in a resistor increases, the temperature of the resistor increases and causes a change in the resistance value. You can calculate how much error is introduced in your measurement by resistor self-heating from the derating curve of Rated Power(%) vs. Ambient Temperature common

### Resistor Self-Heating

As dissipation of power in a resistor increases, the temperature of the resistor increases and causes a change in the resistance value. You can calculate how much error is introduced in your measurement by resistor self-heating from the derating curve of Rated Power(%) vs. Ambient Temperature commonly given in resistor specifications.

The specifications of resistors include a derating curve, similar to the one shown below. Notice that this curve does not show the temperature change of the resistor due to self-heating. The curve shows the percentage of the rated power that you can apply to a resistor vs. the ambient temperature. So at 70 °C of ambient temperature, you can apply up to 100% of the rated power, but at 100 °C you can only apply up to 65% of the rated power. Refer to the following graph.

[IMAGE alt='image' src='GUID-21EB6408-F78A-4297-BCD8-A7FF90768A95-a5.svg']

At any temperature, the resistor will have a temperature change due to self-heating (which we will refer to as ΔT<sub>SH</sub> from here on), so the actual temperature of the resistor is the ambient temperature plus an unknown ΔT<sub>SH</sub>. Even though this graph is not directly showing the value of ΔT<sub>SH</sub>, it can be calculated from the graph.

Notice that at 70 °C and applying 100% of the rated power, the temperature of the resistor will be equal to 70 °C plus ΔT<sub>SH</sub>. At 150 °C, you cannot apply any power to the resistor, so the temperature of the resistor is equal to the ambient temperature. You can thus infer that when applying 100% of the rated power at 70 °C the total temperature of the resistor is 150 °C. Therefore, above 70 °C, the value of ΔT<sub>SH</sub> increases in such a way that when you add to it the ambient temperature it surpasses 150 °C. Therefore, you need to limit the power you apply to the resistor to keep the total temperature of the part under 150 °C. Hence, the value of ΔT<sub>SH</sub> is a function of the power applied to the part.

The thermal resistance ([IMAGE alt='image' src='GUID-5A709C15-1007-4DAC-9E76-D0C536B8209E-a5.gif']) is therefore equal to the absolute value of the slope between the 70 °C and the 150 °C points in the derating curve shown above.

[IMAGE alt='image' src='GUID-5A709C15-1007-4DAC-9E76-D0C536B8209E-a5.gif'] = (150 °C—70 °C)/ΔP = (150 °C—70 °C)/P<sub>max</sub>) °C/W

If the resistor has a Rated Power at 70 °C equal to 0.25 W, then the value for [IMAGE alt='image' src='GUID-5A709C15-1007-4DAC-9E76-D0C536B8209E-a5.gif'] would be equal to:

[IMAGE alt='image' src='GUID-5A709C15-1007-4DAC-9E76-D0C536B8209E-a5.gif'] = (150 °C—70 °C)/ΔP = (150 °C—70 °C)/250 mW = 80 °C/(250*10<sup>–3</sup> W) = 320 °C/W = 0.32 °C/mW

If you want to decrease the thermal resistance, you would need to look for a resistor with higher rated power, or find a way to "heat sink" the resistor to the environment. This however can become complicated and expensive unless the resistor is specifically designed for heat sinking.

You can now calculate the change in temperature due to power dissipation using the thermal resistance ([IMAGE alt='image' src='GUID-5A709C15-1007-4DAC-9E76-D0C536B8209E-a5.gif']) and the power on the resistor (product of voltage and current). Then you can use the temperature coefficient of the resistor (usually given in ppm/ °C) to calculate the change in the resistance value.

Resistor self-heating is more relevant when measuring currents above 100 mA. Resistor self-heating does not present a problem on the NI 4065 and NI 4070/4071/4072, because the internal shunt values are selected for optimum performance. You may observe a settling tail of a few ppm of reading due to self-heating when measuring currents over 100 mA; if this is an issue, increase the settling time of your measurement.

Parent topic:

Measurement Considerations

Related concepts:

- Settling Time

<!--NI_TOPIC bundle=ni-dmm path=resolution.html language=enus -->
## TOPIC 00379: Resolution

- bundle_id: `ni-dmm`
- source_path: `resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/resolution.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: For a noise-free DMM, resolution is the smallest change in an input signal that produces, on average, a change in the output signal. Resolution can be expressed in terms of bits, digits, or absolute units, which are related to each other.BitsResolution is often expressed in bits, which specifically

### Resolution

For a noise-free DMM, resolution is the smallest change in an input signal
 that produces, on average, a change in the output signal. Resolution can be
 expressed in terms of bits, digits, or absolute units, which are related to each
 other.

#### Bits

Resolution is often expressed in bits, which specifically refers to the performance of the analog-to-digital converter (ADC). Theoretically, a 12-bit ADC can convert an analog input signal into 2<sup>12</sup> (4,096) distinct values. 4,096 is the number of least significant bits (LSB). LSB can be translated into digits of resolution:

Digits of resolution = log<sub>10</sub> (Number of LSB)

Using the previous equation, a DMM with a 12-bit ADC has a resolution of:

Log<sub>10</sub> (4,096) = 3.61 digits

Note

#### DMM Absolute Units and Digits of Resolution

For traditional DMMs, 5½ digits refers to the number of digits displayed on the readout of a DMM. A traditional 5½–digit DMM has five full digits that only display values from 0 to 9 and one half digit that only displays 0 or 1. This DMM can show positive or negative values from 0 to 199,999.

For more sophisticated digital instruments, and particularly virtual instruments, digits of resolution does not directly apply to the digits displayed by the readout.

#### Absolute Units

Counts for a DMM is analogous to LSBs for an ADC. A count represents a value that a signal can be digitized to and is equivalent to a step in a quantizer. The weight of a count, or the step size, is the absolute unit of resolution.

Absolute unit of resolution = total span/counts

#### Digits

Digits can be defined as:

Digits of resolution = log<sub>10</sub> (total span/absolute unit of resolution)

For example, a noise–free DMM set to the 10 V range (20 V total span) with 200,000 available counts has an absolute unit of resolution of:

Absolute unit of resolution = 20.0 V/200,000 = 100 µV

The readout of this noise–free DMM would display six digits. A change of the last digit would indicate a change of 100 µV of the input signal.

An 18-bit ADC provides the minimum number of LSB. You can now calculate the digits of resolution:

(2<sup>17</sup> = 131,072, 2<sup>18</sup> = 262,144)

Digits of resolution = log<sub>10</sub> (20.0 V/100 x 10<sup>-6</sup>V)

Digits of resolution = 5.3

This noise–free DMM can be called a 5½ digit DMM.

The quantization process introduces into any converted signal an irremovable error, called the quantization noise. For input signals through a uniform quantizer (without overload distortion), the rms value of the quantization noise in a noise–free DMM can be expressed as:

rms of quantization noise = absolute units of resolution/√12

In reality, a noise-free DMM does not exist and you need to account for the noise level when calculating absolute units of resolution. You can define the effective absolute units of resolution of a noisy DMM as the step size of a noise–free DMM with a quantization noise equal to the total noise of the noisy DMM.

Effective absolute units of resolution = √12 * rms noise

You can define the Effective Number of Digits (ENOD) of this noisy DMM as:

ENOD = log<sub>10</sub>(total span/Effective absolute units of resolution)

#### Example 1

If a DMM set on the 10 V
 range (20 V total span) shows readings with an rms
 noise level of 70 µV, its effective absolute units
 of resolution and the ENOD
 is:

Absolute units of
 resolution = √12 * 70 µV = 242.49
 µV

ENOD = log<sub>10</sub> (20.0
 V/242.49*10<sup>-6</sup>V) = 4.92
 digits

This DMM can be called a 5 digit DMM.

The minimum number of counts needed for
 this DMM would be 20 V/242.49*10<sup>-6</sup> V =
 82,478. The minimum number of bits needed would be
 17 (2<sup>16</sup> = 65,536, 2<sup>17</sup> =
 131,072).

#### Example 2

If the same DMM demonstrates an rms noise level of 20 µV:

Absolute units of resolution = √12 * 20 µV = 69.28 µV

ENOD = log<sub>10</sub> (20 V/69.28*10<sup>-6</sup>V) = 5.46 digits

This DMM can be considered a "5½" digit DMM.

The minimum number of counts needed for this DMM would be 20 V/69.28*10<sup>-6</sup> V = 288,675. The minimum number of bits needed would be 19 (2<sup>18</sup> = 262,144, 2<sup>19</sup> = 524,288).

The following table relates bits, counts, and ENOD to conventional digits of resolution for DMMs. As evidenced by the table, bits, counts, and ENOD are deterministically related. A direct mathematical relationship between ENOD and digits does not exist because digits are used only as an approximation.

[IMAGE alt='image' src='GUID-07C348D2-A8EF-4CEF-9850-CB16AE54829C-a5.svg']

Parent topic:

Measurement Quality

Related concepts:

- Noise

<!--NI_TOPIC bundle=ni-dmm path=sample-rate.html language=enus -->
## TOPIC 00380: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

Related concepts:

- Nyquist Theorem

<!--NI_TOPIC bundle=ni-dmm path=sample-rate_2.html language=enus -->
## TOPIC 00381: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=sample-rate_3.html language=enus -->
## TOPIC 00382: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=sample-rate_4.html language=enus -->
## TOPIC 00383: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=sample-rate_5.html language=enus -->
## TOPIC 00384: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=sample-rate_6.html language=enus -->
## TOPIC 00385: Sample Rate

- bundle_id: `ni-dmm`
- source_path: `sample-rate_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sample-rate_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.The available sample rates (r) correspond to the following equation:r = (1.8 MS/s)/ywhere y = 1, 2, 3,...1.8 x 10^5.The fig

### Sample Rate

Sample rate is the rate at which a signal is sampled by an ADC. A higher sample rate captures more waveform details while a sample rate that is too low can distort the waveform.

The available sample rates (r) correspond to the following equation:

r = (1.8 MS/s)/y

where y = 1, 2, 3,...1.8 x 10<sup>5</sup>.

The figure below illustrates a 100 kHz sine wave sampled at 500 kS/s:

[IMAGE alt='image' src='GUID-CEC98C90-3528-4BA8-B160-7D3976FCD43B-a5.svg']

The figure below shows the same sine wave sampled at 1.8 MS/s:

[IMAGE alt='image' src='GUID-5964D382-538A-4978-836D-E3ADCBB416C4-a5.gif']

The faster rate digitizes 18 points per cycle of the input signal compared with 5 points per cycle with the slower ADC. In this example, the higher sample rate more accurately captures the waveform shape as well as frequency. This process is called over-sampling and can greatly improve the quality of the waveform measurement. The DMM allows for 6 times over-sampling when acquiring a voltage waveform at the limit of its analog bandwidth of 300 kHz.

When performing a waveform acquisition, select a sampling rate that observes the Nyquist Theorem. Excessive over-sampling has tradeoffs. First, excessive over-sampling may give you more data than you need, unnecessarily consume processor resources, and slow the display. Second, additional noise becomes apparent, because the noise performance of the DMM improves as your sampling rate decreases.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=scanning-switch-modules.html language=enus -->
## TOPIC 00386: Scanning Switch Modules

- bundle_id: `ni-dmm`
- source_path: `scanning-switch-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/scanning-switch-modules.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can exchange signals with NI and third-party switches during multipoint scanning operations. Two methods of scanning are available and are normally used: synchronous and handshaking.Scanning is a method of sequentially connecting channels and is often used when connecting instrument(s) and d

### Scanning Switch Modules

#### Scanning
 Options

The DMM can exchange signals with NI and
 third-party switches during multipoint scanning operations. Two methods of scanning
 are available and are normally used: synchronous and handshaking.

Scanning is a method of sequentially connecting
 channels and is often used when connecting instrument(s) and device(s) under test
 (DUT), in a specific order.

Refer to Using Switches for the
 theory of operation, scanning methods, and measurement considerations. Refer to
 Triggering, Single Point
 Acquisitions, and Multiple Point
 Acquisitions for programming flow information.

To determine if your
 switch supports scanning, and for switch configuration information and initial
 programming tips, refer to the Scanning NI Switches with NI Digital
 Multimeters section of the NI Switches Help
 (Programming with NI-SWITCH»Features»Scanning»Scanning NI Switches
 with NI Digital Multimeters) at either of the following
 locations:

| Condition | Path |
| --- | --- |
| If you have installed NI-SWITCH | Start»All Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help |
| If you do not have NI-SWITCH installed | ni.com/docs |

The following tables show synchronization options for NI DMMs and
 switches.

Note

SCXI Communication

| NI PXIe-4080/4081/4082 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Installation | Switch Type for Synchronization with DMM | Possible Destination of Measurement Complete | Possible Inputs for External Trigger In | Comments |
| Any PXI slot of a PXI/PXI Express chassis, and not controlling an SCXI chassis | PXI or PXI Express switch | PXI Trigger Lines <0..7> | PXI Trigger Lines <0..7>1 | — |
| 1Refer to SCXI Communication and Triggering for the NI PXI-4070/4071/4072 for cable accessories for the AUX I/O Connector. |  |  |  |  |
| NI PXI-4070/4071/4072 |  |  |  |  |
| Installation | Switch Type for Synchronization with DMM | Possible Destination of Measurement Complete1 | Possible Inputs for External Trigger In1 | Comments |
| Any PXI slot of a PXI/PXIe chassis, and not controlling an SCXI chassis | PXI/PXIe switch | PXI Trigger Lines <0..7> AUX I/O Connector Pin 64 | PXI Trigger Lines <0..7>2 AUX I/O Connector Pin 94 | — |
| SCXI switch (installed in an SCXI chassis that is controlled by another device) | AUX I/O Connector Pin 64 | AUX I/O Connector Pin 94 AUX I/O Connector Pin 34 | — |  |
| Any PXI slot of a PXI/PXIe chassis, and controlling an SCXI chassis using the AUX I/O Connector | PXI/PXIe switch | PXI Trigger Lines <0..7> | PXI Trigger Lines <0..7>2 | — |
| SCXI switch (installed in an SCXI chassis that is controlled by the NI PXI-4070/4071/4072) | AUX I/O Connector Pin 63 | AUX I/O Connector Pin 33 | — |  |
| Right-most slot of a PXI/SCXI combination chassis, and controlling the SCXI portion through the PXI backplane lines5 | PXI switch | PXI Trigger Lines <0..7> AUX I/O Connector Pin 64 | PXI Trigger Lines <0..7>2 AUX I/O Connector Pin 94 AUX I/O Connector Pin 34 | — |
| SCXI switch (installed in an SCXI chassis that is controlled by the NI PXI-4070/4071/4072) | Local Bus Right Line 0 AUX I/O Connector Pin 64 | Local Bus Right Line 1 AUX I/O Connector Pin 34 | Local Bus Right Trigger Lines 0 and 1 connect the signal to SCXI Trigger Lines 0 and 1, respectively. |  |
| 1Refer to SCXI Communication and Triggering for the NI PXI-4070/4071/4072 for cable accessories for the AUX I/O Connector. 2You can receive the Sample Trigger and the Trigger from the PXI Star Line. Refer to the documentation for the switch you are using to determine whether the switch can route a trigger to the PXI Star Line. 3The AUX I/O Connector of the NI PXI-4070/4071/4072 can be used to control an SCXI chassis, send the Measurement Complete signal, and receive an external trigger. 4You can use a cable accessory for the AUX I/O Connector to connect the trigger signal directly to the front terminal block of the switch. Refer to Triggering for more information. 5Not all PXI-407x devices are capable of controlling the SCXI portion through the backplane. Refer to PXI Express Compatibility for more information. |  |  |  |  |
| NI PXI-4065 |  |  |  |  |
| Installation | Switch Type for Synchronization with DMM | Possible Destination of Measurement Complete1 | Possible Inputs for External Trigger In1 | Comments |
| Any PXI slot of a PXI/PXIe chassis, and not controlling an SCXI chassis | PXI/PXIe switch | PXI Trigger Lines <0..7> AUX I/O Connector Pin 64 | PXI Trigger Lines <0..7>2 AUX I/O Connector Pin 94 | — |
| SCXI switch (installed in an SCXI chassis that is controlled by another device) | AUX I/O Connector Pin 64 | AUX I/O Connector Pin 94 AUX I/O Connector Pin 34 | — |  |
| Any PXI slot of a PXI/PXIe chassis, and controlling an SCXI chassis using the AUX I/O Connector | PXI/PXIe switch | PXI Trigger Lines <0..7> | PXI Trigger Lines <0..7>2 | — |
| SCXI switch (installed in an SCXI chassis that is controlled by the NI PXI-4065) | AUX I/O Connector Pin 63 | AUX I/O Connector Pin 33 | — |  |
| 1Refer to SCXI Communication and Triggering for the NI PXI-4065 for cable accessories for the AUX I/O Connector. 2You can receive the Sample Trigger and the Trigger from the PXI Star Line. Refer to the documentation for the switch you are using to determine whether the switch can route a trigger to the PXI Star Line. 3The AUX I/O Connector of the NI PXI-4065 can be used to control an SCXI chassis, send the Measurement Complete signal, and receive an external trigger. 4You can use a cable accessory for the AUX I/O Connector to connect the trigger signal directly to the front terminal block of the switch. Refer to Triggering for more information. |  |  |  |  |
| NI PCI-4070 and NI PCI/PCIe-4065 |  |  |  |  |
| Installation | Switch/Device Type for Synchronization with DMM | Possible Destination of Measurement Complete1 | Possible Inputs for External Trigger In1 | Comments |
| Not controlling an SCXI chassis | Other devices | AUX I/O Connector Pin 63 | AUX I/O Connector Pin 93 AUX I/O Connector Pin 33 | — |
| Controlling an SCXI chassis | SCXI switch | AUX I/O Connector Pin 62 | AUX I/O Connector Pin 32 | — |
| 1Refer to SCXI Communication and Triggering for the NI PCI-4070 for cable accessories for the AUX I/O Connector. Refer to SCXI Communication and Triggering for the NI PCI/PCIe-4065 for cable accessories for the AUX I/O Connector. 2The AUX I/O Connector of the NI PCI-4070 and NI PCI/PCIe-4065 can be used to control an SCXI chassis and to send and receive triggers. 3You can use a cable accessory for the AUX I/O Connector to connect the trigger signal directly to the front terminal block of the switch. Refer to Triggering for the NI PCI-4070 or Triggering for the NI PCI/PCIe-4065 for more information. |  |  |  |  |
| NI USB-4065 |  |  |  |  |
| Installation | Switch/Device Type for Synchronization with DMM | Possible Destination of Measurement Complete1 | Possible Inputs for External Trigger In1 | Comments |
| Not controlling an SCXI chassis | Other devices | AUX I/O Connector Pin 62 | AUX I/O Connector Pin 92 AUX I/O Connector Pin 32 | — |
| 1Refer to SCXI Communication and Triggering for the NI USB-4065 for cable accessories for the AUX I/O Connector. 2You can use a cable accessory for the AUX I/O Connector to connect the trigger signal directly to the front terminal block of the switch. Refer to Triggering for more information. |  |  |  |  |

Parent topic:

Triggering

Related concepts:

- Synchronous Scanning
- Handshaking Scanning
- Using Switches
- Triggering
- Single Point Acquisitions
- Multiple Point Acquisitions
- PXI Express Compatibility
- SCXI Communication
- SCXI Communication
- SCXI Communication

<!--NI_TOPIC bundle=ni-dmm path=scanning.html language=enus -->
## TOPIC 00387: Scanning

- bundle_id: `ni-dmm`
- source_path: `scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/scanning.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4065, NI 4070/4071/4072, and PXIe-4080/4081/4082 can exchange signals with NI switches during multipoint scanning operations. Two methods of scanning are available: synchronous and handshaking.Refer to Triggering for programming flow information.Refer to Scanning Switch Modules for informatio

### Scanning

The NI 4065, NI 4070/4071/4072, and PXIe-4080/4081/4082 can exchange signals with NI switches during multipoint scanning operations. Two methods of scanning are available: synchronous and handshaking.

Refer to Triggering for programming flow information.

Refer to Scanning Switch Modules for information on trigger signals.

For switch configuration information and initial programming tips, refer to the Scanning NI Switches with NI Digital Multimeters section of the NI Switches Help (Programming with NI-SWITCH»Features»Scanning»Scanning NI Switches with NI Digital Multimeters) at either of the following locations:

- Start»Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not installed NI-SWITCH)

#### Scan List

A scan list is a string composed of channel names and characteristics that define connections, disconnections, triggering, and timing of the scan in the switch.

Parent topic:

Using Switches

Related concepts:

- Synchronous Scanning
- Handshaking Scanning
- Triggering
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements.html language=enus -->
## TOPIC 00388: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

Related concepts:

- AC Voltage
- Configuring Measurement Timing
- DC Noise Rejection
- Noise

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements_2.html language=enus -->
## TOPIC 00389: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements_3.html language=enus -->
## TOPIC 00390: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements_4.html language=enus -->
## TOPIC 00391: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements_5.html language=enus -->
## TOPIC 00392: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=selecting-aperture-time-for-dc-measurements_6.html language=enus -->
## TOPIC 00393: Selecting Aperture Time for DC Measurements

- bundle_id: `ni-dmm`
- source_path: `selecting-aperture-time-for-dc-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-aperture-time-for-dc-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution me

### Selecting Aperture Time for DC Measurements

The aperture time shapes the noise rejection of the measurement. Shorter aperture time yields a wider measurement bandwidth at the expense of resolution. Sensitivity to source noise increases with shorter apertures. Conversely, larger aperture times quiet noisy sources and yield higher resolution measurements. Refer to the DC Noise Rejection section for more information.

Selecting aperture times equal to multiples of power line frequency helps to reject these frequencies, when DC Noise Rejection is set to Normal. An aperture set to 1 powerline cycles (1 PLC equals 16.67 ms for 60 Hz powerline or 20 ms for 50 Hz) is the minimum that provides this line rejection.

Apertures of >100 ms can be used for measuring very high resistance values, when sensitivity to powerline frequency noise pickup is inevitable. Coupling the aperture time with DC Noise Rejection set to High Order provides extremely high noise rejection (>100 dB). Long apertures of >100 ms do not significantly improve resolution but can provide better rejection to externally generated noise.

You can average multiple measurements by setting the Number of Averages property to a value greater than one. Averaging with Auto Zero enabled circumvents the effects of low–frequency, self-generated noise and yields the highest resolution performance level. Having more averages also reduces external noise, but the tradeoff is speed.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dmm path=selecting-dc-noise-rejection.html language=enus -->
## TOPIC 00394: Selecting DC Noise Rejection

- bundle_id: `ni-dmm`
- source_path: `selecting-dc-noise-rejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/selecting-dc-noise-rejection.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the DC noise rejection setting by choosing one of the following:LabVIEW—Set the DC Noise Rejection property.CVI, C++, or Visual Basic—Set the NIDMM_ATTR_DC_NOISE_REJECTION attribute.By default, DC Noise Rejection is set to Auto (-1). Considerations If you configure the NI 408x and NI 407x wit

### Selecting DC Noise Rejection

Select the DC noise rejection setting by choosing one of the following:

LabVIEW—Set the DC Noise Rejection property.CVI, C++, or Visual Basic—Set the NIDMM_ATTR_DC_NOISE_REJECTION attribute.

By default, DC Noise Rejection is set to Auto (-1).

#### Considerations

- If you configure the NI 408 x and NI 407 x 
 with an absolute resolution that corresponds to 6½ digits (NI 4080/4082 and
 NI 4070/4072) or 7½ digits (NI 4081 and NI 4071), the driver uses high-order DC noise rejection.
- If you configure the NI 4065 with an absolute resolution that corresponds to 6½
 digits, the driver uses second-order DC
 noise rejection.
- For lower resolution DC measurements, the driver uses second-order DC noise
 rejection for the NI 408 x and NI 407 x and
 normal DC noise rejection for the NI 4065.
- If you configure the device for a waveform acquisition, the driver uses normal
 DC noise rejection by default. For NI 407x, if you set the aperture time, the
 driver uses normal DC noise rejection by default.
- For AC measurements with the NI 4065, the driver uses second-order DC noise
 rejection.

Refer to the DMM Measurement Defaults
 section for your device for more information.

| Values | Description |
| --- | --- |
| AUTO (-1) | NI-DMM chooses the DC noise rejection setting based on the configured function and resolution. |
| Normal (0) | NI-DMM weighs all samples equally. |
| Second-Order (1) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement. |
| High-Order (2) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement. Note The NI 4065 does not support High-Order. |

Parent topic:

Features

Related concepts:

- DC Noise Rejection
- DMM Measurement Defaults

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=sensitivity.html language=enus -->
## TOPIC 00395: Sensitivity

- bundle_id: `ni-dmm`
- source_path: `sensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/sensitivity.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sensitivity is the smallest unit of a given parameter that can be meaningfully detected with the instrument when used under specified conditions.For example, assume the sensitivity of a DMM in the volts function is 100 nV. With this sensitivity, the DMM can be used to detect a 100 nV change in the i

### Sensitivity

Sensitivity is the smallest unit of a given parameter that can be meaningfully detected with the instrument when used under specified conditions.

For example, assume the sensitivity of a DMM in the volts function is 100 nV. With this sensitivity, the DMM can be used to detect a 100 nV change in the input voltage.

Parent topic:

Measurement Quality

<!--NI_TOPIC bundle=ni-dmm path=setting-attributes-before-reading-attributes.html language=enus -->
## TOPIC 00396: Setting Attributes Before Reading Attributes

- bundle_id: `ni-dmm`
- source_path: `setting-attributes-before-reading-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/setting-attributes-before-reading-attributes.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Attributes—which are also called properties in LabVIEW—are modified when you set them or when you call a configuration VI or function that sets them. It is important to set the attributes or call any configuration VIs or functions before reading back any attribute values for the following reasons:Va

### Setting Attributes Before Reading Attributes

Attributes—which are also called properties in LabVIEW—are modified when you set them or when you call a configuration VI or function that sets them. It is important to set the attributes or call any configuration VIs or functions before reading back any attribute values for the following reasons:

- Values read are coerced depending on the current configuration of the session. If you read an attribute value and then set other attributes, the value read may no longer be valid.
- The driver verifies that the configuration of the device is valid at the time the attribute is
 read. It is possible to get an error when reading an attribute if the
 configuration is not valid at that point, even when a setting later could make
 it valid.
- Reading attributes causes the driver to verify the current configuration. If you change some of the settings later, those settings need to be validated again.

Note

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-dmm path=settling-time-and-switches.html language=enus -->
## TOPIC 00397: Settling Time and Switches

- bundle_id: `ni-dmm`
- source_path: `settling-time-and-switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/settling-time-and-switches.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using switches in an application, you need to consider switching and measurement timing issues. Switches take time to actuate and settle, so changing channels requires care to avoid compromising the measurement with a DMM.Electromechanical switches use coil-induced magnetic fields to move an ar

### Settling Time and Switches

When using switches in an application, you need to consider switching and measurement timing issues. Switches take time to actuate and settle, so changing channels requires care to avoid compromising the measurement with a DMM.

Electromechanical switches use coil-induced magnetic fields to move an armature and connect two contacts, completing the circuit. The time it requires is called relay actuation time. The actuation time required to close a contact usually takes longer than the time it takes to break the connection.

FET switches use transistor devices to modulate path resistance. The actuation time is based on charging the gate of these transistors and semiconductor device physics, and it is much faster than actuating the armature of an electromechanical switch.

Solid–state relays (SSR) also use transistors to create the circuit. To provide high-voltage switching capability, the gate is driven by an optical isolator. The optical isolator takes longer to charge and actuate the switch than the non-isolated gate of a FET switch, but it is faster than an electromechanical switch.

In addition to actuation time, switches require a settling time. After an electromechanical switch actuates, the armature vibrates, or bounces, on the channel contact. Measurements cannot be made until this effect has subsided. Settling time can also be affected by the length and type of external cabling. The DMM should wait for the switch to actuate and for the system to settle before taking a measurement. The total settling time is dependent on the required accuracy. For information on settling time, refer to Settling Time.

If you are using NI switches, you can exchange triggering signals between the switches and the
 DMM (handshaking), or the DMM can signal the switch to actuate (synchronous
 scanning). Refer to Scanning Switch Modules
 for information about how NI DMMs and switch modules can exchange trigger
 signals.

Parent topic:

Switch Fundamentals

Related concepts:

- Settling Time
- Handshaking Scanning
- Synchronous Scanning
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=settling-time.html language=enus -->
## TOPIC 00398: Settling Time

- bundle_id: `ni-dmm`
- source_path: `settling-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/settling-time.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Settling time is the time required for a measurement system to stabilize to a specified accuracy limit. The DMM settling time is dictated by the measurement range, cable properties, source impedance, and change in input level. Use short cables with low dielectric absorption and minimal capacitance—N

### Settling Time

Settling time is the time required for a measurement system to stabilize to a specified accuracy limit. The DMM settling time is dictated by the measurement range, cable properties, source impedance, and change in input level. Use short cables with low dielectric absorption and minimal capacitance—NI recommends Teflon cable. Ideally, your source should have a low output impedance (for example, <10 kΩ). Settling time becomes especially important in scanning systems. The scanner or multiplexer requires an additional settling time before the measurement can be taken. NI-DMM allows for a programmable delay between channels so that both the DMM and the multiplexer can settle. Settling times are dependent on the input signal and your selected resolution.

Parent topic:

Measurement Considerations

Related concepts:

- Settling Time and Switches

<!--NI_TOPIC bundle=ni-dmm path=simulating-ni-digital-multimeters.html language=enus -->
## TOPIC 00399: Simulating NI Digital Multimeters

- bundle_id: `ni-dmm`
- source_path: `simulating-ni-digital-multimeters.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/simulating-ni-digital-multimeters.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Simulating your device is useful if you are developing your applications and the hardware you are using is unavailable.To simulate a device, complete the following steps:LabVIEW Use niDMM Initialize With Options. Add "Simulate=1,DriverSetup=Model:[40xx]; BoardType:[PCMCIA, PCI, PCIe, PXI, PXIe, USB]

### Simulating NI Digital Multimeters

Simulating your device is useful if you are developing your applications and the hardware you are using is unavailable.

To simulate a device, complete the following steps:

- LabVIEW
  1. Use niDMM Initialize With Options.
  2. Add "Simulate=1,DriverSetup=Model:[40xx]; BoardType:[PCMCIA, PCI, PCIe, PXI, PXIe, USB]" to the Option String of the VI.
- CVI/C++/Visual Basic
  1. Use niDMM_InitWithOptions .
  2. Add "Simulate=1,DriverSetup=Model:[40xx]; BoardType:[PCMCIA, PCI, PCIe, PXI, PXIe, USB]" to the Option String of the function.

For example, to simulate the NI PCI-4065, the option string would be:

"Simulate=1, DriverSetup=Model:4065; BoardType:PCI"

| Model | Board Type |
| --- | --- |
| 4065 | PXI, PCI, PCIe, USB |
| 4070 | PXI, PCI |
| 4071 | PXI |
| 4072 | PXI |
| 4080 | PXIe |
| 4081 | PXIe |
| 4082 | PXIe |

If the Instrument Descriptor parameter and the Driver Setup property are not specified, an NI PXI-4070 is simulated by default. If the Driver Setup string is not provided, and the Instrument Descriptor parameter specifies a valid device, the device of the Instrument Descriptor property is simulated. If the Driver Setup string is specified, the Instrument Descriptor property is ignored.

Parent topic:

Features

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=single-point-acquisitions.html language=enus -->
## TOPIC 00400: Single Point Acquisitions

- bundle_id: `ni-dmm`
- source_path: `single-point-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/single-point-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A single point acquisition allows you to acquire a single measurement within a configuration. To configure a single point acquisition, use niDMM Config Measurement, which configures the DMM for a single point acquisition by default. The niDMM Config Measurement function allows you to configure the f

### Single Point Acquisitions

A single point acquisition allows you to
 acquire a single measurement within a configuration. To configure a single point
 acquisition, use niDMM Config Measurement, which configures the DMM for a single
 point acquisition by default. The niDMM Config Measurement function allows you to
 configure the function, range, and resolution. Refer to Configuring the Hardware
 for more information.

Initiate a single point acquisition by calling either
 niDMM Initiate or niDMM Read. The DMM enters the Wait-for-Trigger state after niDMM
 Initiate is called. After taking the measurement, the DMM can generate a Measurement
 Complete signal. The DMM then returns to the Idle state. The figure below
 demonstrates the sequence of a single point acquisition.

[IMAGE alt='image' src='GUID-7A2FC788-AD61-4879-8ECB-E0821A06BD15-a5.svg']

During a single
 point acquisition, you can configure the DMM to wait for a trigger before taking a
 measurement. You can also specify a delay between when the DMM receives the trigger
 and when it acquires the measurement. Use niDMM Configure Trigger to set the
 Trigger Source and Trigger
 Delay.

By default, the Trigger Delay is
 Auto Delay (-1), which means the DMM waits an appropriate settling time before
 taking the measurement. The following table contains additional information about
 the Trigger Delay setting for the DMMs:

| Device | Description |
| --- | --- |
| NI 4065 NI 4070/4071/4072 NI 4080/4081/4082 | The DMM uses the value specified in Trigger Delay as additional settling time as demonstrated in the Acq One Sample-Ext Trig example. |

Note

Parent topic:

Triggering

Related concepts:

- Configuring the Hardware
- Generating a Measurement Complete Event
- Acquiring Data
- Examples
- Scanning Switch Modules
- LabWindows/CVI Trigger Routing
- LabVIEW Trigger Routing

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=single-waveform-acquisitions.html language=enus -->
## TOPIC 00401: Single Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `single-waveform-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/single-waveform-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a single waveform acquisition by calling niDMM Configure Waveform Acquisition.Initiate a waveform acquisition by calling either niDMM Initiate or niDMM Read Waveform. Configure Trigger Source to force the DMM to wait for a trigger before measuring the first waveform point. Configure Trigge

### Single Waveform Acquisitions

Configure a single waveform acquisition by calling niDMM Configure Waveform Acquisition.

Initiate a waveform acquisition by calling either niDMM Initiate or niDMM Read Waveform. Configure Trigger Source to force the DMM to wait for a trigger before measuring the first waveform point. Configure Trigger Delay to specify the timing between when the DMM receives the trigger and when it acts upon the trigger. Use niDMM Configure Trigger to set the Trigger Source and Trigger Delay. The Trigger Delay setting is Auto Delay (-1), which means the DMM waits an appropriate settling time before acquiring the waveform.

The default trigger source is Immediate. Refer to the trigger routing sections for information about possible trigger sources and information on which values are supported by each device.

The figure below demonstrates the sequence for single waveform acquisitions.

[IMAGE alt='image' src='GUID-470DC039-AD66-4BCC-82BE-02FE738D8ACB-a5.svg']

Note

The latency of the DMM is negative by default. Latency can be reduced to zero or made positive by setting the Trigger Delay property appropriately. The latency can be specified only within the tolerance indicated by the jitter specification for the input trigger. Refer to the specifications document for your device for more information.

After acquiring the entire waveform, the DMM can generate a Measurement Complete signal. The DMM then returns to the Idle State.

Parent topic:

Acquiring Waveforms

Related concepts:

- Generating a Measurement Complete Event
- LabVIEW Trigger Routing
- LabWindows/CVI Trigger Routing
- Scanning Switch Modules

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=stray-admittance.html language=enus -->
## TOPIC 00402: Stray Admittance

- bundle_id: `ni-dmm`
- source_path: `stray-admittance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/stray-admittance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: For the NI 4072 only, Admittance is the reciprocal of the residual impedance. Stray admittances, which are found in series between the DMM and the DUT, result from the connectivity required between the DMM and the DUT. The stray admittance on the test setup introduces an error on the voltage reading

### Stray Admittance

For the NI 4072 only,
 Admittance is the reciprocal of the residual impedance.
 Stray admittances, which are found in series between the
 DMM and the DUT, result from the connectivity required between the DMM and the DUT.
 The stray admittance on the test setup introduces an error on the voltage reading by
 dividing the excitation current. This error can affect the accuracy of inductance
 and capacitance measurements, particularly when it is comparable to the admittance
 of the DUT. The following figure illustrates stray admittance in a typical
 measurement:

[IMAGE alt='image' src='GUID-B7A71EBF-6272-4CFE-BAD7-388DD289F2A2-a5.svg']

where

V<sub>M</sub> = total input voltage measured by the
 DMM, Y<sub>P</sub> = stray admittance, Y<sub>X</sub> = admittance of the DUT, I = test current, I<sub>P</sub> = current going
 through the stray admittance, I<sub>X</sub> = current going through the DUT

I = I<sub>P</sub> + I<sub>X</sub> V<sub>M</sub> =
 I / (Y<sub>P</sub> + Y<sub>X</sub>) Y<sub>M</sub> =
 I / V<sub>M</sub> = Y<sub>P</sub> +
 Y<sub>X</sub>

Note

For example, in
 an application with a 10 nF capacitor in parallel with 1 nF of stray capacitance,
 the meter reads a 10% error, or 11 nF (10 nF + 1 nF).

To reduce stray
 admittances on test fixture and cables, take the following steps:

- Keep the cables as short as possible.
- Avoid any variations due to mechanical vibrations, handling, and temperature
 changes.
- Use the compensation techniques available on the NI 4072. Refer to OPEN/SHORT
 Compensation for more information.

In addition to stray admittance, residual impedance can also be found in test
 setups. Refer to Residual Impedance for more information.

Parent topic:

Measurement Considerations

Related concepts:

- OPEN/SHORT Compensation
- Residual Impedance

<!--NI_TOPIC bundle=ni-dmm path=switch-fundamentals.html language=enus -->
## TOPIC 00403: Switch Fundamentals

- bundle_id: `ni-dmm`
- source_path: `switch-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/switch-fundamentals.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following topics for fundamental information about switches:

### Switch Fundamentals

Refer to the following topics for fundamental information about switches:

- [Relay Forms](relay-forms.html)
- [Topologies](topologies.html)
- [Settling Time and Switches](settling-time-and-switches.html)

Parent topic:

Using Switches

<!--NI_TOPIC bundle=ni-dmm path=switching-capacitance-and-inductance.html language=enus -->
## TOPIC 00404: Switching Capacitance and Inductance

- bundle_id: `ni-dmm`
- source_path: `switching-capacitance-and-inductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/switching-capacitance-and-inductance.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 4072 can be integrated as part of an ATE system that includes switches, cables, and other custom test fixtures. The quality of the measurement is directly related to the quality of the system setup.For information about the various NI switch modules that are available, refer to the NI Switche

### Switching Capacitance and Inductance

The NI 4072 can be integrated as part of an ATE system that includes switches, cables, and other custom test fixtures. The quality of the measurement is directly related to the quality of the system setup.

For information about the various NI switch modules that are available, refer to the NI
 Switches Help at either of the following locations:

- Start»Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- ni.com/manuals (if you have not installed NI-SWITCH)

#### Measurement
 Considerations

Inductors and capacitors store energy. Inductors store
 currents that can damage other devices connected to them when disconnected.
 Capacitors store energy as voltage that can be harmful to some equipment or to the
 capacitors themselves.

For applications that require scanning through
 different types of measurements, NI recommends taking notice when switching channels
 that use built-in current excitation. The measurement modes in the NI 4072 that use
 current excitation are as follow:

| Type of Excitation Signal | Function Mode |
| --- | --- |
| DC Current | ResistanceRefer to the Resistance section for more information on the test current. |
| DiodeRefer to the Diode section for more information on the test current. |  |
| AC Current | CapacitanceRefer to the Capacitance and Inductance Measurement Considerations section for more information on the test signal for capacitance measurements. |
| InductanceRefer to the Capacitance and Inductance Measurement Considerations section for more information on the test signal for inductance measurements. |  |

After a measurement is completed, the front-end configuration remains
 unchanged until the next type of measurement is initiated or the DMM is reset.
 Therefore, after taking a resistance, diode, capacitance, or inductance measurement,
 the current excitation remains on until niDMM Initiate (after configuring the
 device) or niDMM Reset is called. The existing excitation current could lead to an
 unsafe condition for the setup, the device under test, or the operator.

To
 avoid such situations, review the channel assignments and configuration of your
 system, taking into account the following considerations:

- After taking a resistance measurement, turn off the DC current before switching
 to a channel for a capacitance or inductance measurement. If the resistance or
 diode DC current excitation is applied to a capacitor, the voltage can increase
 to 12 V. If this same current is switched into an inductor, you could see a
 short voltage spike of up to 12 V. You should turn off the DC current by
 resetting the device or initiating the DMM for the capacitance or inductance
 measurement before switching to the channel.
- When you use the appropriate range for capacitance measurements, the voltage
 across the capacitor does not exceed 1 V. If you have a capacitor with a value
 lower than 5% of the range, you observe an underrange condition
 and can apply a test voltage exceeding the 1 V limit (maximum of 12 V). If the
 capacitor is not built to tolerate this voltage level, you could reduce its
 life, shift its value, or damage it permanently (less likely). When performing
 in-circuit testing, you could inadvertently bias other components in the
 circuit, such as transistors or diodes.
- After you take an inductance measurement or a resistance measurement on an
 inductive load, the excitation current remains on. If the channel is opened
 immediately after you take the measurement, a voltage develops across the open
 circuit, because the inductor is still charged with current. This charge could
 produce a voltage across the open circuit that could shorten the life of the
 relays in the switch. To prevent damage to the setup, multiplexer, test fixture,
 or device under test, NI recommends performing one of the following actions
 before switching to the successive measurement:
  - If the next measurement uses a function mode that requires a current
 excitation signal, turn off the current source by resetting the device
 immediately after taking the inductance measurement before breaking the
 channel.
  - If the next measurement does not use a function mode
 that requires a current excitation signal (such as DC voltage), you can
 either reset the device or configure and initiate the next measurement
 before breaking the channel.

#### Recommendations for System
 Integration

To integrate the NI 4072 into an ATE system, take the
 following steps to maximize your success:

- Keep cables as short as possible. Longer leads are more likely to introduce
 noise or errors into the system.
- Use twisted pairs or coaxial cable to reduce noise pickup.
- Use strain relief ties to maintain a consistent mechanical configuration.
- Minimize contact resistance everywhere a connection is present. Contacts should
 be firm and must be kept clean and free from oxides.
- Verify that the contact electrodes can be opened or shorted so that it is
 possible to perform OPEN/SHORT
 compensation. Note Components such as cables,
 switches, and fixtures can contribute noise to the measurement. Setting open
 or short conditions at the contact electrodes can minimize the noise effects
 of system components connected between the DMM and the DUT. To set a short
 condition, establish direct contact at the end of the cable, or connect a
 short (<2 cm) AWG 18 gauge or thicker wire between the two
 conductors.NI-DMM 2.3 or later allows you to save and load different
 compensation values per channel. To provide maximum flexibility in the
 test system, you can manipulate, store, and load these values for high
 channel-count systems.
- Minimize the variation of impedance between channels. If two channels have very
 similar impedance (for example, same cable type and length, and same type of
 switch path), one channel can perform the OPEN measurement and the other channel
 can perform the SHORT measurement. This multi-channel compensation is not as
 accurate as per-channel compensation, but multi-channel compensation can reduce
 test time and simplify the OPEN/SHORT
 compensation procedure for the other measurements. The impedance
 levels between all channels are more likely to be similar if all channels share
 the majority of the measurement path, as shown below:

Note

For recommendations about how to set up your scan list and configure
 your system, refer to Load Switching.

Parent topic:

Load Switching

Related concepts:

- Overrange/Underrange
- OPEN/SHORT Compensation
- Resistance
- Diode
- Measurement Considerations
- Frequency Effects of Real-World Components
- Temperature Effects
- Cabling
- Noise Pickup
- Using Switches
- Load Switching

Related information:

- NI-DMM LabVIEW Reference

<!--NI_TOPIC bundle=ni-dmm path=switching-current.html language=enus -->
## TOPIC 00405: Switching Current

- bundle_id: `ni-dmm`
- source_path: `switching-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/switching-current.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The current measurement path within the NI 4065 and NI 4070/4071/4072 utilizes an electromechanical relay that provides very low resistance to assure a low burden voltage. While this relay has an exceptionally long life, you can take special precautions to ensure reliable operation.Whenever possible

### Switching Current

The current measurement path within the NI 4065 and NI 4070/4071/4072 utilizes an electromechanical relay that provides very low resistance to assure a low burden voltage. While this relay has an exceptionally long life, you can take special precautions to ensure reliable operation.

Whenever possible, switch the NI 4065 and NI 4070/4071/4072 into the current measurement function before applying the current. Switching inductive current sources generally creates flyback voltages that stress the relay and, if done on a frequent basis, can shorten the reliability of the relay. Also, avoid interrupting the current by switching out of the current measurement function or resetting the DMM when currents are flowing through the circuit.

While the internal shunts are ideal for many applications, in applications where more than one current needs to be measured using the same DMM and the conditions require that the current cannot be interrupted across the load, you can use a break-before-make switch in multiplexer topology and place external shunts across the channels. Connect the shunts in series with the circuit under test and then measure the voltage drop across the shunts.

If the conditions allow interrupting the current flow through the circuit under test, it is still recommended to use external shunts. It is not common to find switches that can switch currents higher than 1 A, and switching currents can diminish the life of the switch.

The benefits of using the break-before-make switch in multiplexer topology with external shunts across the channels are as follows:

- Allows uninterrupted switching of current sources because the multiplexer switches voltages developed across the shunts instead of routing currents; ensuring that the current loop is not interrupted is generally helpful to avoid disturbing the current sources
- Extends the switch life, especially if the switch consists of electromechanical relays

The tradeoffs involved may be as follows:

- Reduces accuracy, although using the DMM to measure the resistance of shunts periodically (in 4-wire) can address this issue
- Introduces a leakage current from the switch that could significantly affect low-level current measurements; refer to your switch documentation for methods to reduce leakage currents
- Introduces errors due to resistor self-heating in high-level current measurements if the shunt resistor characteristics are not good enough

You should choose a shunt resistor whose characteristics and value help you reduce noise and errors, as follows:

- Consider the tradeoff between creating a large enough voltage across the shunt for resolution, while at the same time keeping the shunt voltage small enough to prevent high heat dissipation or burden voltage errors during the measurement.
- Look for a shunt resistor with low temperature coefficient (preferably not more than 10 ppm/°C) and absolute tolerance matched to your application requirement.

Recall that voltage offsets introduced by the switch could affect your measurement, because they add an additional burden voltage to the one specified by the ammeter itself. For the burden voltage per range, refer to Related Documentation for the specifications documents for the DMMs.

In cases where you must use the built-in current measurement capability of the NI 4065 and NI 4070/4071/4072, use a make-before-break setup for the switches for ensuring uninterrupted current loops. You may also choose to use specially designed current routing switches for this application.

Refer to DC and AC Current for the NI 4070/4072 or the NI 4065 and NI 4071 for general information about current measurements with the NI 4065 and NI 4070/4071/4072 and for recommendations when taking low and high level current measurements.

Parent topic:

Load Switching

Related concepts:

- Resistor Self-Heating
- Burden Voltage
- DC and AC Current
- DC and AC Current

<!--NI_TOPIC bundle=ni-dmm path=switching-voltages.html language=enus -->
## TOPIC 00406: Switching Voltages

- bundle_id: `ni-dmm`
- source_path: `switching-voltages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/switching-voltages.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When switching high-voltage signals, the parasitic capacitance of the cable connecting the NI 4065 and NI 4070/4071/4072 with the switches, as well as the input capacitance of the instrument, need to be charged to the source voltage. Depending on the voltage present at the DMM input during the measu

### Switching Voltages

When switching high-voltage signals, the parasitic capacitance of the cable connecting the NI 4065 and NI 4070/4071/4072 with the switches, as well as the input capacitance of the instrument, need to be charged to the source voltage. Depending on the voltage present at the DMM input during the measurement on the previous channel, a significant current can flow from the high–voltage source to charge this capacitance. This action is referred to as hot switching, which can reduce the life of the switches. Refer to your switch documentation for information about extending switch life.

When switching high-voltage signals into a low-voltage range of any DMM (such as applying 300 V on the 10 V range), the input impedance will be lower than it is when the proper range is selected. Repetitive operations like this may shorten switch life. To maximize switch life, always select a measurement range that can handle the maximum voltage expected.

Switching signals with large common-mode components (LO switched from +250 V to -250 V) may, over extended periods of time (tens of Hz for several weeks) begin to degrade the relay performance. The switching life of the relays can be extended in many cases by inserting some small common-mode resistance in series with the LO terminals. Even several hundred ohms (200 to 500 Ω) helps significantly. Refer to the following figure, where V<sub>CM1</sub> or V<sub>CM2</sub> >50 V:

[IMAGE alt='image' src='GUID-999E5F40-D0B0-4DB2-AF26-DD2C6EF3D86C-a5.svg']

In these situations, break-before-make switching is essential to obtaining any kind of reliable relay life. Should S<sub>1</sub> and S<sub>2</sub> be turned on together, even momentarily, V<sub>CM1</sub> + V<sub>SIG1</sub>, is shorted to V<sub>CM2</sub> + V<sub>SIG2</sub>, which could cause high currents to permanently damage the contacts of S<sub>1</sub> or S<sub>2</sub>.

Parent topic:

Load Switching

<!--NI_TOPIC bundle=ni-dmm path=synchronizing-waveform-measurements.html language=enus -->
## TOPIC 00407: Synchronizing Waveform Measurements

- bundle_id: `ni-dmm`
- source_path: `synchronizing-waveform-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/synchronizing-waveform-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synchronizing multiple devices is useful in various scenarios. For example, when taking power measurements, you can synchronize multiple devices to get an accurate measurement. One device can acquire current, while the other can acquire voltage. You can determine the power measurement from the curre

### Synchronizing Waveform Measurements

Synchronizing multiple devices is useful in various scenarios. For example, when taking power measurements, you can synchronize multiple devices to get an accurate measurement. One device can acquire current, while the other can acquire voltage. You can determine the power measurement from the current and voltage measurements taken.

When synchronizing multiple devices, ensure that the measurement settling times and triggering are configured similarly. Each device must also receive all the triggers from the same source.

To ensure that the two devices start the waveform acquisitions at the same time, configure the same external hardware trigger for each device. While NI-DMM typically chooses the optimal settling time based on function and range parameters, when synchronizing multiple devices, you must set the settling time for each device to the same value. Otherwise, the measurements will be off by the difference in settling times. Making the settling time the same for each device allows the signals connected to the devices to settle before taking a measurement.

For example, to capture a voltage waveform in a 300 V range and a current waveform in a 1 A range, set the settling time for both measurements to 2 ms. The default settling times for voltage and current waveforms are different. The 2 ms settling time is required by the 300 V range and is greater than 100 µs required by 1 A range. Increasing the settling time for the 1 A range helps get an accurate measurement because the 1 A range is slower to settle than the 300 V range.

Note

Parent topic:

Acquiring Waveforms

Related concepts:

- Waveform Acquisition Defaults

<!--NI_TOPIC bundle=ni-dmm path=synchronous-scanning.html language=enus -->
## TOPIC 00408: Synchronous Scanning

- bundle_id: `ni-dmm`
- source_path: `synchronous-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/synchronous-scanning.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: With synchronous scanning, the DMM takes a measurement and generates a digital pulse—measurement complete. When the switch receives the digital pulse, it advances to the next entry in its scan list. The DMM takes the next measurement after a time interval. You must program the DMM interval time by c

### Synchronous Scanning

With synchronous scanning, the DMM takes a measurement and generates a digital pulse—measurement complete. When the switch receives the digital pulse, it advances to the next entry in its scan list. The DMM takes the next measurement after a time interval. You must program the DMM interval time by configuring an Interval Sample Trigger. Set the Interval parameter to the time needed for the switch to activate and settle. Initiate the switch before initiating the DMM for its first measurement.

The following figure shows a DMM performing synchronous scanning with a switch module:

[IMAGE alt='image' src='GUID-5FDCE081-A848-4801-A406-A9CF2BC8FA7C-a5.svg']

#### Synchronous Scanning Timing Diagram

The following figure shows the timing signals associated with the synchronous scanning shown above:

[IMAGE alt='image' src='GUID-2B97E9AC-0588-4523-8302-53D92A9FC146-a5.svg']

where

M = measurement

WFT = wait for trigger

S&S = switch and settle

#### Hardware Connections to an External Multiplexer in Synchronous Mode

The following figure shows how to configure the hardware when performing synchronous scanning between a DMM and an external multiplexer:

[IMAGE alt='image' src='GUID-C0D7C4DB-0878-4DE8-924D-E0D434EB5412-a5.svg']

Refer to Triggering for more information:

- For programming flow, refer to Single Point Acquisitions, Multi Point Acquisitions, and Continuous Acquisitions.
- For information on available trigger sources and destinations when using NI DMMs and switch
 modules, refer to Scanning Switch
 Modules.

For switch configuration information and initial programming tips, refer to the Scanning NI Switches with NI Digital Multimeters section of the NI Switches Help (Programming with NI-SWITCH»Features»Scanning»Scanning NI Switches with NI Digital Multimeters) at either of the following locations:

- Start»All Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not installed NI-SWITCH)

Parent topic:

Scanning

Related concepts:

- Scanning
- Triggering
- Single Point Acquisitions
- Multiple Point Acquisitions
- Continuous Acquisitions
- Scanning Switch Modules

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements.html language=enus -->
## TOPIC 00409: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

Related concepts:

- Dielectric Absorption
- DMM Measurement Cycle
- Settling Time

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_2.html language=enus -->
## TOPIC 00410: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_3.html language=enus -->
## TOPIC 00411: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_4.html language=enus -->
## TOPIC 00412: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_5.html language=enus -->
## TOPIC 00413: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_6.html language=enus -->
## TOPIC 00414: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=system-considerations-for-resistance-measurements_7.html language=enus -->
## TOPIC 00415: System Considerations for Resistance Measurements

- bundle_id: `ni-dmm`
- source_path: `system-considerations-for-resistance-measurements_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/system-considerations-for-resistance-measurements_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple g

### System Considerations for Resistance Measurements

When measuring resistance in a system, it is important to consider the effects of cable resistance. It is also important to notice that interactions between scanning multiple resistances and system cabling can present time-dependent problems. These problems can be avoided by following these simple guidelines.

- As you scan from channel to channel, the current source must drive the voltage across the resistor to a quiescent level before a meaningful measurement can be made. If there is substantial system capacitance, this capacitance must also be charged by the current source. Starting the measurement before the capacitance is fully charged results in an erroneous measurement.
- Resistance measurements up to 10 kΩ seldom encounter settling time problems, as long as the system capacitance is <500 pF and you allow a settling time of 2 ms or more.
- Settling time might need to be longer if significant dielectric absorption effects are present in the cables and switching system. Resistance values above 100 kΩ are most sensitive to cable capacitance and other dielectric effects. If dielectric absorption is suspect, find the optimum setting experimentally by increasing the settling time until the readings no longer change.

The following figure illustrates the factors affecting settling time for a resistance measurement:

[IMAGE alt='image' src='GUID-C30B8263-616A-46C9-B4EB-6BFEBDC01A24-a5.svg']

Settling Time = kC<sub>C</sub>R<sub>X</sub>

where

k = the value related to accuracy required

C<sub>C</sub> = the capacitance of the cable and switching network

R<sub>X</sub> = the resistance being measured

Note

Refer to the DMM Measurement Cycle section for more information on settling time. Remember that the Offset Compensated Ohms function toggles the current source on and off. Excessive system capacitance due to cables, in circuit elements, and so on may affect this measurement as it affects it in a scanning system. The Belden 83317E cable has a capacitance of 35.5 pF/ft and extremely low dielectric absorption. Refer to the Belden CDT Incorporated Web site at www.belden.com for information about this cable.

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-dmm path=temperature-effects.html language=enus -->
## TOPIC 00416: Temperature Effects

- bundle_id: `ni-dmm`
- source_path: `temperature-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-effects.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Temperature can have a large impact on the DUT impedance. Usually, capacitors have large temperature coefficients (5% to 80% variation over the entire temperature range, depending upon the capacitor used) except for ceramic COG capacitors, which can exhibit only a 0.003%/°C variation. Inductors, esp

### Temperature Effects

Temperature can have a large impact on the DUT impedance. Usually, capacitors have large temperature coefficients (5% to 80% variation over the entire temperature range, depending upon the capacitor used) except for ceramic COG capacitors, which can exhibit only a 0.003%/°C variation. Inductors, especially those with non-air cores, may vary largely with temperature. Ambient and DUT temperature drifts (due to handling, for instance) may introduce error into the measurement. Control ambient temperature changes to reduce errors.

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements.html language=enus -->
## TOPIC 00417: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

Related concepts:

- Thermocouples
- Thermistors
- Resistance Temperature Detector (RTDs)

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_2.html language=enus -->
## TOPIC 00418: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_3.html language=enus -->
## TOPIC 00419: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_4.html language=enus -->
## TOPIC 00420: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_5.html language=enus -->
## TOPIC 00421: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_6.html language=enus -->
## TOPIC 00422: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=temperature-measurements_7.html language=enus -->
## TOPIC 00423: Temperature Measurements

- bundle_id: `ni-dmm`
- source_path: `temperature-measurements_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/temperature-measurements_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).The following table illustrates some of the capabilities and limitations of these sensors. Use th

### Temperature Measurements

The DMM can measure temperature using common temperature transducers. The three most commonly used transducers for temperature are thermocouples, thermistors, and resistance temperature detectors (RTDs).

The following table illustrates some of the capabilities and limitations of these sensors. Use this table as a reference for choosing the right sensor for your temperature measurement application.

| Sensor | Advantages | Disadvantages |
| --- | --- | --- |
| Thermocouples | wide range, fast response,inexpensive | require reference temperature,nonlinear |
| Thermistors | repeatable, fine resolution, low current, fast response | narrow range, nonlinear |
| RTDs | rugged, accurate | slow response, lead resistance, nonlinear, self-heating |

The following table lists NI-DMM supported sensor combinations:

| Thermocouple Support | Thermistor Support | RTD Support |
| --- | --- | --- |
| 2-wire ITS-90 polynomial scaling Presets for types B, E, J, K, N, R, S, and T | 2-wire Steinhart-Hart scaling Presets for common Omega 44000 Series thermistors (44004, 44006, 44007) Custom coefficients | 4-wire and 2-wire Callendar-Van Dusen scaling Presets for common sensor standards (alpha=0.00385, alpha=0.00391, etc.) Custom coefficients |

#### Measurement Range, Resolution, and
 Options

NI-DMMs perform a measurement
 appropriate to the temperature transducer type (DC
 voltage for thermocouples, resistance for
 thermistors or RTDs), and convert this reading
 into degrees Celsius. See thermocouples,
 thermistors, and RTDs for specific cabling
 details.

When configuring a temperature
 transducer measurement, the user must specify the
 range and resolution of the underlying voltage or
 resistance measurement while configuring the DMM.
 The following range settings are recommended for
 optimal accuracy, speed, and range of the
 supported transducers. Users may wish to select a
 different range for measurements at extreme
 temperatures or when using custom transducer
 types.

| Transducer | Recommended Range |
| --- | --- |
| Thermocouple | 100 mV |
| 1kΩ to 10kΩ Thermistor | 100 kΩ |
| 100 Ω RTD | 1 kΩ |
| 1k Ω RTD | 10 kΩ |

Other measurement options, such as Auto
 Zero, Offset Compensated Ohms, Settling Time, and
 Aperture Time still apply to the underlying
 voltage or resistance measurement where
 applicable.

Parent topic:

DMM Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermal-voltages.html language=enus -->
## TOPIC 00424: Thermal Voltages

- bundle_id: `ni-dmm`
- source_path: `thermal-voltages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermal-voltages.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermal voltages, also known as thermal EMFs, are voltages created by the junction of dissimilar metals when a temperature difference exists between these junctions. The generated voltage increases with temperature.The specific metal-to-metal junctions result in specific temperature coefficients (V/

### Thermal Voltages

Thermal voltages, also known as thermal EMFs, are voltages created by the junction of dissimilar metals when a temperature difference exists between these junctions. The generated voltage increases with temperature.The specific metal-to-metal junctions result in specific temperature coefficients (V/°C) called Seebeck coefficients, which are shown in the following table.

| Junction | Seebeck Coefficient(µV/°C) |
| --- | --- |
| Copper–Copper | <0.3 |
| Copper–Gold | 0.5 |
| Copper–Silver | 0.5 |
| Copper–Brass | 3 |
| Copper–Nickel | 10 |
| Copper–Lead-Tin Solder | 1–3 |
| Copper–Aluminum | 5 |
| Copper–Kovar | 40 |
| Copper–Copper Oxide | 1000 |

You can determine thermal voltages using the following formula:

V<sub>T</sub> = K(T<sub>2</sub>—T<sub>1</sub>)

where

T<sub>1</sub> and T<sub>2</sub> are temperatures measured at the junctions of dissimilar metals

K is the Seebeck coefficient of Copper—N (from table above), and N is a dissimilar metal

[IMAGE alt='image' src='GUID-FE495A1D-42E7-42D1-B13E-48AE8AC9B854-a5.svg']

To reduce the effects of thermal voltages, use clean copper–to–copper connectors with gold-plating.

Note

Thermal EMF and Offset Voltage

NI Switches Help

- Start»Programs»National Instruments»NI-SWITCH»Documentation»NI Switches Help (if you have installed NI-SWITCH)
- NI Product Manuals Library Web site (if you have not installed NI-SWITCH)

Parent topic:

Measurement Considerations

<!--NI_TOPIC bundle=ni-dmm path=thermistors.html language=enus -->
## TOPIC 00425: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_2.html language=enus -->
## TOPIC 00426: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_3.html language=enus -->
## TOPIC 00427: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_4.html language=enus -->
## TOPIC 00428: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_5.html language=enus -->
## TOPIC 00429: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_6.html language=enus -->
## TOPIC 00430: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermistors_7.html language=enus -->
## TOPIC 00431: Thermistors

- bundle_id: `ni-dmm`
- source_path: `thermistors_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermistors_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass. Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors h

### Thermistors

A thermistor is a piece of semiconductor made from metal oxides, pressed into a small bead, disk, wafer, or other shape, heated at high temperatures, and coated with epoxy or glass.

Like RTDs, Thermistors have a resistance that varies nonlinear with respect to temperature. Unlike RTDs, thermistors have a higher resistance (anywhere from 2,000 to 10,000 Ω) and a much higher sensitivity (~200 Ω/°C). However, thermistors are generally used only up to the 300 °C temperature range.

NI-DMM scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation:

1/
 T = 
 A + 
 B(
 ln(
 R)) + 
 C(
 ln(
 R))
 <sup>3</sup>

where 
 T is the temperature in Kelvins, 
 R is the measured resistance, and 
 A, 
 B, and 
 C are constants provided by the thermistor manufacturer.

Because thermistors have high resistance, lead-wire resistance does not affect the accuracy of the measurements. Unlike RTDs, 2-wire measurements are adequate.

The DMM supports the following sensors from Omega's 44000-Series. NI-DMM also supports user-specified A, B, and C coefficients through the custom thermistor type if none of the presets below match the transducer.

| Sensor | Nominal Resistance (25 °C) | Steinhart-Hart Coefficients |
| --- | --- | --- |
| Omega 44004 | 2.25k | A =1.468e-3B =2.383e-4C = 1.007e-7 |
| Omega 44006 | 10k | A = 1.032e-3B = 2.387e-4C = 1.580e-7 |
| Omega 44007 | 5k | A = 1.285e-3B = 2.362e-4C = 9.285e-8 |

#### Cabling

Thermistor measurements are wired using the HI and LO connectors on the DMM:

[IMAGE alt='image' src='GUID-4031EFD7-7E8E-49A4-8151-F46B20850818-a5.svg']

#### Underlying DMM Measurement

To measure temperature with a thermistor, the DMM performs a 2-wire resistance measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting resistance is then converted to degrees Celsius by software using the Steinhart-Hart equation and A, B, and C coefficients.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for a 1 to 10kΩ thermistor is 100 kΩ.

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples.html language=enus -->
## TOPIC 00432: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_2.html language=enus -->
## TOPIC 00433: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_3.html language=enus -->
## TOPIC 00434: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_4.html language=enus -->
## TOPIC 00435: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_5.html language=enus -->
## TOPIC 00436: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_6.html language=enus -->
## TOPIC 00437: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=thermocouples_7.html language=enus -->
## TOPIC 00438: Thermocouples

- bundle_id: `ni-dmm`
- source_path: `thermocouples_7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/thermocouples_7.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.This voltage is converted to temperatu

### Thermocouples

Thermocouples consist of a pair of dissimilar metals that meet at a contact point, which produces a small, open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to temperature.

This voltage is converted to temperature using tables of coefficients and the following polynomial scaling function:

[IMAGE alt='image' src='GUID-996869FA-734D-4930-8925-D9D31F317732-a5.gif']

where t<sub>90</sub> is the temperature in degrees Celsius, E is the voltage in millivolts, and D<sub>i</sub> is the coefficient.

The DMM supports temperature measurements with J, K, N, T, E, R, S, and B type thermocouples. The driver software contains all necessary coefficient tables to perform the ITS-90 polynomial scaling.

Thermocouple types differ in composition and accurate range as illustrated in the following table:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) | Extended Temperature Range (°C) |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | –150 to 1200 | –210 to –150 |
| K | Chromel | Alumel | –100 to 1200 | –200 to –100 |
| N | Nicrosil | Nisil | –100 to 1300 | –200 to –100 |
| T | Copper | Constantan | –100 to 400 | –200 to –100 |
| E | Chromel | Constantan | –150 to 1000 | –200 to –150 |
| R | Platinum-13% Rhodium | Platinum | 300 to 1760 | –50 to 300 |
| S | Platinum-10% Rhodium | Platinum | 400 to 1760 | –50 to 400 |
| B | Platinum | Rhodium | 1100 to 1820 | 400 to 1100 |

#### Reference Junction

Thermocouple measurements require a user-specified fixed reference junction temperature. This is also referred to as the "cold-junction compensation" or "CJC" temperature. If the user does not specify a reference junction temperature, a default of 25 °C is assumed.

NI-DMM provides the Measure Temperature (Thermocouple) example, which you can find by using the shortcut at Start»All Programs»National Instruments»NI-DMM»Examples.

In many applications, the reference junction temperature is measured by a separate temperature sensor (typically an RTD or thermistor) to improve thermocouple measurement accuracy.

#### Cabling

Thermocouples are cabled using the HI and LO connectors of the DMM. The polarity of the thermocouple leads is critical for correct thermocouple measurements.

[IMAGE alt='image' src='GUID-3A3AE021-5753-4ADE-943D-85DE11048D57-a5.svg']

You must use a thermocouple adapter to connect a thermocouple to your DMM.

Thermocouples require some form of temperature reference to compensate for unwanted parasitic thermocouples. This process is called cold-junction compensation.

[IMAGE alt='image' src='GUID-E908ED6C-149D-46CB-ADC7-2E42AD570952-a5.svg']

#### Underlying DMM Measurement

To measure temperature with any thermocouple, the DMM internally performs a DC Voltage measurement with the range, resolution, timing, and other measurement options that have been specified by the user. The resulting voltage is then converted to degrees Celsius by software using ITS-90 polynomial scaling.

When configuring a temperature transducer measurement, the user must specify the range and resolution of the underlying voltage or resistance measurement while configuring the DMM. The recommended range for thermocouples is 100 mV

Note

Parent topic:

Temperature Measurements

<!--NI_TOPIC bundle=ni-dmm path=topologies.html language=enus -->
## TOPIC 00439: Topologies

- bundle_id: `ni-dmm`
- source_path: `topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/topologies.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: A switch topology is an organizational representation of the channels and relays in a switch module. The topology establishes the default states for all relays in a module and defines the channel names. Some switches can use multiple topologies or variations of each topology type. Some terminal bloc

### Topologies

A switch topology is an organizational representation of the channels and relays in a switch module. The topology establishes the default states for all relays in a module and defines the channel names. Some switches can use multiple topologies or variations of each topology type. Some terminal blocks or accessories may force the switch to use a given topology or set of topologies.

NI switches use three categories of topologies:

#### General-Purpose Topologies

General-purpose topologies consist of multiple isolated relays. Each channel of a general-purpose switch module can connect one input to one output. They are typically used to power ON or OFF devices such as motors, fans, and lights or to switch high-voltage or high-current signals.

[IMAGE alt='image' src='GUID-74C50B37-4956-4AD7-A8B1-8F71BEF6D4D6-a5.svg']

#### Multiplexer

A multiplexer, or a MUX, is a topology in which you can connect one input to multiple outputs or one output to multiple inputs. This topology is often used for scanning when you need to automatically connect a sequence of channels to a common line.

| 4x1 Multiplexer Composed of Form A Relays | 4x1 Multiplexer Composed of Form C Relays |
| --- | --- |
|  |  |

#### Matrix

A matrix is one of the most flexible switching configurations. Unlike a multiplexer, a matrix can connect multiple inputs to multiple outputs organized as columns and rows. You can connect any column to any number of rows and any row to any number of columns. At each intersection of a row and column, there is a switch. When the switch is closed, the row is connected to the column.

Matrix size is often described as M rows by N columns (M x N). The figure below depicts a 1-wire, 2 x 4 matrix, where c<sub>n</sub> is any device under test (DUT) and r<sub>n</sub> is any of the instruments, including the DMM.

[IMAGE alt='image' src='GUID-5C1A459F-A285-4675-BD33-AAFBF4B3AAE0-a5.svg']

Parent topic:

Switch Fundamentals

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations.html language=enus -->
## TOPIC 00440: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations_2.html language=enus -->
## TOPIC 00441: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations_3.html language=enus -->
## TOPIC 00442: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations_4.html language=enus -->
## TOPIC 00443: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations_5.html language=enus -->
## TOPIC 00444: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=transient-measurement-considerations_6.html language=enus -->
## TOPIC 00445: Transient Measurement Considerations

- bundle_id: `ni-dmm`
- source_path: `transient-measurement-considerations_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/transient-measurement-considerations_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NoneCablingWhen using the DMM to acquire waveforms, choose your connecting cable carefully. Any unshielded cable or test leads can pick up common electromagnetic and electrostatic interference which corrupts waveform measurements and introduces spurs in the frequency domain. Shielded coaxial cables

### Transient Measurement Considerations

None

#### Cabling

When using the DMM
 to acquire waveforms, choose your connecting cable carefully. Any unshielded cable
 or test leads can pick up common electromagnetic and electrostatic interference
 which corrupts waveform measurements and introduces spurs in the frequency domain.
 Shielded coaxial cables are often used for waveform measurement. You can use a
 female-BNC-to-dual-banana-plug adapter, such as Pomona part number 1269, to easily
 connect the DMM inputs to signal sources using coaxial shielded cable. NI recommends
 the Belden 83317E shielded cable. Refer to the Belden Inc. website at www.belden.com
 for information about this cable. The Belden 83317E shielded cable works well for
 DMM measurements within the 300 kHz bandwidth of the DMM and in situations where BNC
 connectivity is not required.

There are two alternative ways to connect the
 shield. If high frequency (> 1 kHz) common-mode AC signals are present, better
 results can be obtained if the shield is connected to the DMM LO terminal. If no
 common-mode AC signal is present or if the common-mode AC signal is low (< 100
 mV), then connecting the shield to PXI chassis ground is preferable. The following
 figures show the DMM connected to a device under test (DUT) with the Belden 83317E
 cable.

As shown in the figure below, the best HI signal shielding results with
 a common-mode AC signal > 1 kHz. The shield potential must remain within 42
 V<sub>AC/DC</sub> of LO:

[IMAGE alt='image' src='GUID-3C49AB03-E1A8-407F-BA09-BB39BB5D79FA-a5.svg']

As
 shown in the figure below, good shielding results if common-mode AC signals are less
 than 100 mV, and the shielding is safest if a large DC common-mode voltage is
 present.

[IMAGE alt='image' src='GUID-D01FF767-2F57-464D-94C3-594B5719026B-a5.svg']

Caution

#### Slew Rate Limitations

The
 DMM can measure almost any signal within its 300 kHz bandwidth. However, some
 signals may have enough high-frequency energy to introduce significant distortion.
 In general, the rate of change of the input signal voltage, also known as its slew
 rate, should stay below the following limits to avoid excessive
 distortion:

| Input Range | Maximum Slew Rate |
| --- | --- |
| 300 V (NI 4080/4082 and NI 4070/4072 only),1000 V (NI 4081 and NI 4071 only) | 2000 V/µs |
| 100 V | 200 V/µs |
| 10 V | 20 V/µs |
| 1 V | 2 V/µs |
| 100 mV | 0.2 V/µs |

If you suspect your slew rate may be too high, you can switch to a higher
 range to see if the waveform shape changes significantly.

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=triggering.html language=enus -->
## TOPIC 00446: Triggering

- bundle_id: `ni-dmm`
- source_path: `triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/triggering.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Triggering is a feature that allows you to take a measurement with a deterministic response. In other words, you can begin taking a measurement in response to an external event. For example, if you are scanning with a switch, you may want to trigger the DMM to take a measurement after the switch has

### Triggering

Triggering is a feature that allows you to take a measurement with a deterministic response. In
 other words, you can begin taking a measurement in response to an external event.
 For example, if you are scanning with a switch, you may want to trigger the DMM to
 take a measurement after the switch has been activated and settled. To understand
 triggering, you must understand the DMM behavior during an acquisition.

Refer to the Triggering sections for your device for pin assignments and cable accessory information.

This section includes:

- [Single Point Acquisitions](single-point-acquisitions.html)
- [Multiple Point Acquisitions](multiple-point-acquisitions.html)
- [Continuous Acquisitions](continuous-acquisitions.html)
- [Generating a Measurement Complete Event](generating-a-measurement-complete-event.html)
- [Scanning Switch Modules](scanning-switch-modules.html)
- [LabWindows/CVI Trigger Routing](labwindowscvi-trigger-routing.html)
- [LabVIEW Trigger Routing](labview-trigger-routing.html)

Parent topic:

Features

<!--NI_TOPIC bundle=ni-dmm path=usb-system-considerations.html language=enus -->
## TOPIC 00447: USB System Considerations

- bundle_id: `ni-dmm`
- source_path: `usb-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/usb-system-considerations.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI USB-4065 conforms to USB 2.0 specifications and is 1.1 compliant. The NI USB-4065 is a high powered USB device that supports both Hi-Speed and full-speed USB protocol. For more information about power requirements, refer to Related Documentation for the NI 4065 Specifications document.

### USB System Considerations

The NI USB-4065 conforms to USB 2.0 specifications and is 1.1 compliant. The NI USB-4065 is a high powered USB device that supports both Hi-Speed and full-speed USB protocol. For more information about power requirements, refer to Related Documentation for the NI 4065 Specifications document.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-dmm path=user-manual-welcome.html language=enus -->
## TOPIC 00448: NI-DMM User Manual

- bundle_id: `ni-dmm`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DMM User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-DMM
 User Manual

The NI-DMM User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-DMM
- NI-DMM Release Notes
- Interactive Activation Guide
- NI-DMM Discussion Forums
- NI-DMM LabVIEW VI Reference
- NI-DMM C Function Reference Help
- NI-DMM .NET API Overview
- NI-DMM C Function Reference Help
- NI-ModInst Help

<!--NI_TOPIC bundle=ni-dmm path=using-attributes-and-properties-with-ni-dmm.html language=enus -->
## TOPIC 00449: Using Attributes and Properties with NI-DMM

- bundle_id: `ni-dmm`
- source_path: `using-attributes-and-properties-with-ni-dmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-attributes-and-properties-with-ni-dmm.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DMM contains high-level functions and VIs that set most of the instrument attributes. Use the high-level driver functions and VIs as much as possible, because they handle order dependencies and multithread locking for you. Some attributes and properties are not accessible through the high-level f

### Using Attributes and Properties with NI-DMM

NI-DMM contains high-level functions and VIs that set most of the instrument attributes. Use the high-level driver functions and VIs as much as possible, because they handle order dependencies and multithread locking for you.

Some attributes and properties are not accessible through the high-level functions or VIs. For example, Input Resistance is not set with any of the NI-DMM configuration functions or VIs. The values for these attributes and properties must be set using the attribute or property.

#### Accessing Attributes and Properties

In LabVIEW, properties are accessed through the NI-DMM property node. To access them, complete the following steps:

1. Open a VI.
2. Make sure that you are viewing the block diagram. Navigate to the NI-DMM palette at Instrument I/O»Instrument Drivers»NI-DMM , and drag the property node icon to the diagram.
3. Select the correct property node class by wiring an instrument handle in into the property node reference, or by right-clicking on the property node and choosing Select Class»IVI»niDMM .
4. Left-click the property node, and select the property you want to use.
5. To add additional properties, resize the property node.

In C and Visual Basic, attributes are accessed with the Get Attribute and Set Attribute functions. These functions correspond to a particular data type. To set the NIDMM_ATTR_INPUT_RESISTANCE attribute, use the niDMM_SetAttributeViReal64 function.

The defined properties values are not always equivalent to the values used in LabVIEW enumeration controls. In NI-DMM VIs, the first value for LabVIEW enumerations always begins at zero. For example, If you use niDMM Config Measurement to set the VI to DC volts, this value is zero. This value is translated before being passed to the driver. If you use the property node to configure the VI, DC volts is set with IVIDMM VAL DC VOLTS = 1.

To translate between LabVIEW enumerated values and IVI constants, use the conversion VIs in LabVIEW located in the NI-DMM.llb.

Refer to the LabVIEW VI Reference or Function Reference for a complete listing of available attributes.

Parent topic:

Programming Flow

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=using-ni-dmm-in-labview.html language=enus -->
## TOPIC 00450: Using NI-DMM in LabVIEW

- bundle_id: `ni-dmm`
- source_path: `using-ni-dmm-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-ni-dmm-in-labview.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the NI LabVIEW ADE to manage your code development and that you are familiar with the ADE. To develop an NI-DMM application in LabVIEW, follow these general steps:Open an existing or new LabVIEW VI.From the Function Palette (the default location), locate the NI-

### Using NI-DMM in LabVIEW

This topic assumes that you are using the NI LabVIEW ADE to manage your code development and
 that you are familiar with the ADE.

To develop an NI-DMM application in LabVIEW, follow these general steps:

1. Open an existing or new LabVIEW VI.
2. From the Function Palette (the default location), locate the NI-DMM VIs at All Functions»NI Measurements»NI-DMM .
3. Select the VIs that you want to use and drop them on the block diagram to build your application.

#### Example Programs

LabVIEW users can use the LabVIEW Example Finder to search or browse examples. NI-DMM examples are classified by keyword, so you can search for a particular device or measurement function.

To browse the NI-DMM examples available in LabVIEW, launch LabVIEW, click Find Examples, and navigate to Hardware Input and Output»Modular Instruments»NI-DMM (Digital Multimeters).

You can find the installed locations of example programs in the NI-DMM Readme File. For additional information regarding NI-DMM examples, refer to Examples.

Parent topic:

Creating an Application with NI-DMM

Related concepts:

- Examples

<!--NI_TOPIC bundle=ni-dmm path=using-ni-dmm-in-labwindowscvi.html language=enus -->
## TOPIC 00451: Using NI-DMM in LabWindows/CVI

- bundle_id: `ni-dmm`
- source_path: `using-ni-dmm-in-labwindowscvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-ni-dmm-in-labwindowscvi.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the LabWindows™/CVI™ ADE to manage your code development and that you are familiar with the ADE. To develop an NI-DMM application in LabWindows/CVI, follow these general steps:Open an existing or new project file.Load the NI-DMM function panel. You can find the

### Using NI-DMM in LabWindows/CVI

This topic assumes that you are using the LabWindows™/CVI™ ADE to manage your code development and that you are familiar with the ADE.

To develop an NI-DMM application in LabWindows/CVI, follow these general steps:

1. Open an existing or new project file.
2. Load the NI-DMM function panel. You can find the installed location of the NI-DMM function panel in the NI-DMM Readme.
3. Use the function panel to navigate the function hierarchy and generate function calls with the proper syntax and variable values.

#### Example Programs

LabWindows/CVI users can use the NI Example Finder to search or browse examples. NI-DMM examples are classified by keyword, so you can search for a particular device or measurement function.To browse the NI-DMM examples available in LabWindows/CVI, launch LabWindows/CVI, select Help»Find Examples, and navigate to Hardware Input and Output»Modular Instruments»NI-DMM (Digital Multimeters).

You can find the installed locations of example programs in the NI-DMM Readme. For additional information regarding NI-DMM examples, refer to Examples.

Parent topic:

Creating an Application with NI-DMM

<!--NI_TOPIC bundle=ni-dmm path=using-ni-dmm-in-visual-basic.html language=enus -->
## TOPIC 00452: Using NI-DMM in Visual Basic

- bundle_id: `ni-dmm`
- source_path: `using-ni-dmm-in-visual-basic.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-ni-dmm-in-visual-basic.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code development and that you are familiar with the ADE. To develop an NI-DMM application in Visual Basic, follow these general steps:Open an existing or new Visual Basic project.Create files necessary for your appli

### Using NI-DMM in Visual Basic

This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code development and that you are familiar with the ADE.

To develop an NI-DMM application in Visual Basic, follow these general steps:

1. Open an existing or new Visual Basic project.
2. Create files necessary for your application: .frm (form definition and event handling code), .bas (Visual Basic generic code module), or .cls (Visual Basic class module) and add them to the project.
3. Add a reference to the NI DMM Library (NIDMM), which is part of the NI-DMM DLL. In Visual Basic
 6.0, select the Project»References menu option and NI DMM
 Library (NIDMM). If you do not see the NIDMM listed there, click
 Browse and locate nidmm_32.dll . You
 can find the installed location of the NI-DMM DLL in the NI-DMM Readme.
4. Use the Object Browser <F2> to find function prototypes and constants.
5. Add NI-DMM function calls to your application.
6. Run your application by clicking Run .

#### Example Programs

You can find the installed locations of example programs in the NI-DMM Readme File. For additional information regarding NI-DMM examples, refer to the Examples section.

To load an example project with Visual Basic 6.0 or later, select File»Open Project, then select the .vbp file of your choice.

#### String Passing

In Visual Basic, variables of data type String do not need special modifications to be passed to NI-DMM functions. Visual Basic automatically appends a null character to the end of a string before passing it (by reference, because strings cannot be passed by value in Visual Basic) to a procedure or function.

#### Parameter Passing

By default, Visual Basic passes parameters by reference. Prepend the ByVal keyword if you need to pass by value.

Parent topic:

Creating an Application with NI-DMM

<!--NI_TOPIC bundle=ni-dmm path=using-ni-dmm-in-visual-cc.html language=enus -->
## TOPIC 00453: Using NI-DMM in Visual C/C++

- bundle_id: `ni-dmm`
- source_path: `using-ni-dmm-in-visual-cc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-ni-dmm-in-visual-cc.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code development and that you are familiar with the following ADEs:Microsoft Visual C++ 6.0 Microsoft Visual Studio 2010Creating an Application with Microsoft Visual C++ 6.0To develop an NI-DMM application with Mi

### Using NI-DMM in Visual C/C++

This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code development and that you are familiar with the following ADEs:

- Microsoft Visual C++ 6.0
- Microsoft Visual Studio 2010

#### Creating an Application with Microsoft Visual C++ 6.0

To develop an NI-DMM application with Microsoft Visual C++ 6.0, follow these general steps:

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include "nidmm.h"
5. Add the NI-DMM include and library files to the project. <IVIROOTDIR32> is an alias to a
 specific NI file folder location. Refer to the
 NI-DMM Readme for more information about installed
 file locations.
  1. Select
 Project»Settings»C/C++»Preprocessor»Additional
 include directories , and add the path
 to the nidmm.h file. The
 nidmm.h file is located in the
 <IVIROOTDIR32>\Include 
 directory.
  2. Select
 Project»Link»General»Object/Library
 Modules , and add
 nidmm.lib .
  3. Select
 Project»Link»Input»Additional library
 path , and add the path to the
 nidmm.lib file. The
 nidmm.lib file is located in the
 <IVIROOTDIR32>\Lib\msc or
 the <IVIROOTDIR32>\Lib
 x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Creating an Application with Microsoft Visual Studio 2010

To develop an NI-DMM application with Microsoft Visual Studio 2010, follow these general steps:

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include "nidmm.h"
5. Add the NI-DMM include and library files to the project. <IVIROOTDIR32> is an alias to a
 specific NI file folder location. Refer to the
 NI-DMM Readme for more information about installed
 file locations.
  1. Select
 Project»Properties»Configuration
 Properties»C/C++»General»Additional Include
 Directories , add the path to the
 nidmm.h file. The
 nidmm.h file is located in the
 <IVIROOTDIR32>\Include 
 directory.
  2. Select Linker»Input»Additional
 Dependencies , and add
 nidmm.lib .
  3. Select Linker»General»Additional
 Dependencies , and add the path to the
 nidmm.lib file. The
 nidmm.lib file is located in the
 <IVIROOTDIR32>\Lib\msc or
 the <IVIROOTDIR32>\Lib
 x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Example Programs

You can find the installed locations of example programs in the NI-DMM Readme File. For additional information regarding NI-DMM examples, refer to the Examples section.

#### String Passing

To pass strings, pass a pointer to the first element of the character array. Be sure that the string is null-terminated.

#### Parameter Passing

By default, C passes parameters by value. Remember to pass pointers to variables when you need to pass by address.

Parent topic:

Creating an Application with NI-DMM

<!--NI_TOPIC bundle=ni-dmm path=using-switches.html language=enus -->
## TOPIC 00454: Using Switches

- bundle_id: `ni-dmm`
- source_path: `using-switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/using-switches.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to Triggering for more information.In applications where you are connecting many test points to the DMM, it may be appropriate to incorporate a switch. Switches are used to route signals between test points and instruments.Switch selection should be based on the signal types you are routing an

### Using Switches

Refer to Triggering for more information.

In applications where you are connecting many test points to the DMM, it may be appropriate to incorporate a switch. Switches are used to route signals between test points and instruments.

Switch selection should be based on the signal types you are routing and the topology required.

For current and resistance measurements, the switch should have very low path resistance (for example, under 1–2 Ω path resistance). Refer to Offset Compensated Ohms for optimizing resistance measurements in the presence of relay thermal offsets. For capacitance and inductance measurements, it is necessary to have 1–2 Ω path resistance as well. Electromechanical switches are a good match for these applications.

For high–speed scanning through different channels, solid–state relays (SSRs) or FET switches work well. They have high path resistances, so they work best for high-impedance voltage measurements. FET switches operate at logic levels and are usually very fast (25 to 100 kHz), at the expense of low maximum voltage limits (<10 V). SSRs provide internal isolation that allow them to switch much higher voltages (300 V), but they are not as fast as their FET counterparts (1 to 2 kHz).

For low-voltage measurements, keep in mind that the relay section determines the ultimate measurement error due to contact thermal voltages. Refer to Optimizing Low-Voltage Measurements for more information.

| Function | Electromechanical | SSR | FET |
| --- | --- | --- | --- |
| Voltage | Up to 300 V | Up to 300 V | Up to 10 V |
| Current | Up to 10 A | Up to 300 mA | <10 mA |
| Resistance | Recommended | For 4-wire measurements, check the maximum lead resistance allowed by the DMM1 | For 4-wire measurements, check the maximum lead resistance allowed by the DMM1 |
| Capacitance and Inductance | Recommended | Not recommended | Not recommended |
| Scanning Speed | Up to 100 channels/second | Up to 2,000 channels/second | Up to 100,000 channels/second |
| Lifetime | 107 operations | No theoretical limit | No theoretical limit |
| 1Not recommended for 2-wire measurements below 10 kΩ. Switch resistance must be nulled prior to resistance measurement. Refer to Offset Nulling. |  |  |  |

Parent topic:

Integration and System Considerations

Related concepts:

- Triggering
- Offset Compensated Ohms
- Optimizing Low-Voltage Measurements
- Performing Offset Nulling

<!--NI_TOPIC bundle=ni-dmm path=voltages-with-large-common-mode-components.html language=enus -->
## TOPIC 00455: Voltages with Large Common-Mode Components

- bundle_id: `ni-dmm`
- source_path: `voltages-with-large-common-mode-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/voltages-with-large-common-mode-components.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching signals with large common-mode components (LO switched from +250 V to -250 V) may, over extended periods of time (tens of Hz for several weeks), begin to degrade the relay performance. The switching life of the relays can be extended in many cases by inserting some small common-mode resist

### Voltages with Large Common-Mode Components

Switching signals with large common-mode components (LO switched from +250 V to -250 V) may, over extended periods of time (tens of Hz for several weeks), begin to degrade the relay performance. The switching life of the relays can be extended in many cases by inserting some small common-mode resistance in series with the LO terminals. Even several hundred ohms (200 to 500 Ω) helps significantly.

Refer to the following figure, where V<sub>CM1</sub> or V<sub>CM2</sub> are >50 V:

[IMAGE alt='image' src='GUID-999E5F40-D0B0-4DB2-AF26-DD2C6EF3D86C-a5.svg']

In these situations, break-before-make switching is essential to obtaining any kind of reliable relay life. If S1 and S2 are turned on together, even momentarily, VCM1 + VSIG1, is shorted to VCM2 + VSIG2, which could cause high currents to permanently damage the contacts of S1 or S2.The transient signal generated when switching signals with large common mode voltages closely resemble the effect of applying signals that exceed the V-Hz limit. This could affect the internal transfer of data in the device and would generate an error prompting you to reset the board and reconfigure your measurement. Refer to Handling High DC Voltages for more information.

Tip

NIDMM_ERROR_SERIAL_PORT_ERROR

- niDMM Read ( niDMM_Read )
- niDMM Read Multipoint ( niDMM_ReadMultipoint )
- niDMM Fetch ( niDMM_Fetch )
- niDMM Fetch Multipoint ( niDMM_FetchMultipoint )

Your application can handle this error by calling the following VIs or functions:

1. niDMM Reset ( niDMM_reset )
2. Any configuration VI or function to reconfigure the instrument to the required settings
3. niDMM Initiate ( niDMM_Initiate ), niDMM Read ( niDMM_Read ), or niDMM Read Multipoint ( niDMM_ReadMultipoint ) to restart the measurement

Parent topic:

Switching Voltages

Related concepts:

- Handling High DC Voltages

Related information:

- NI-DMM LabVIEW Reference
- NI-DMM C Function Reference Help

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults.html language=enus -->
## TOPIC 00456: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

Related concepts:

- Features
- Configuring Auto Zero
- Configuring ADC Calibration
- Selecting DC Noise Rejection

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults_2.html language=enus -->
## TOPIC 00457: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults_3.html language=enus -->
## TOPIC 00458: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults_4.html language=enus -->
## TOPIC 00459: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults_5.html language=enus -->
## TOPIC 00460: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-defaults_6.html language=enus -->
## TOPIC 00461: Waveform Acquisition Defaults

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-defaults_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-defaults_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default waveform acquisition settings for the device. For more information on a particular attribute, including how to configure a non-default setting, refer to Features. Waveform Function Auto Zero ADC Calibration DC Noise Rejection Voltage OFF N/A Normal Current OFF N

### Waveform Acquisition Defaults

The following table lists the default waveform acquisition settings for the device. For
 more information on a particular attribute, including how to configure a non-default
 setting, refer to Features.

| Waveform Function | Auto Zero | ADC Calibration | DC Noise Rejection |
| --- | --- | --- | --- |
| Voltage | OFF | N/A | Normal |
| Current | OFF | N/A | Normal |

| Function (Range) | Settling Time |
| --- | --- |
| Voltage (≤10 V) | 1 ms |
| Voltage (≥100 V, NI 4080/4081/4082 and NI 4070/4072 only) | 2 ms |
| Voltage (≥100 V) (NI 4071 only) | 5 ms |
| Current | 100 µs |

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle.html language=enus -->
## TOPIC 00462: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

Related concepts:

- Configuring Measurement Timing
- Auto Zero

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle_2.html language=enus -->
## TOPIC 00463: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle_3.html language=enus -->
## TOPIC 00464: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle_4.html language=enus -->
## TOPIC 00465: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle_5.html language=enus -->
## TOPIC 00466: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisition-measurement-cycle_6.html language=enus -->
## TOPIC 00467: Waveform Acquisition Measurement Cycle

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisition-measurement-cycle_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisition-measurement-cycle_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device

### Waveform Acquisition Measurement Cycle

The DMM waveform measurement cycle is made up of several phases: switching time, Auto Zero, settling time, and waveform acquisition phase.The length of the waveform measurement phase is determined by the selected sample rate and number of points. Generally the settling time is selected by the device driver based on the specified function and range. This value can also be independently controlled. Refer to Configuring Measurement Timing for more information.

An internal switch time is required to configure the analog circuitry of the DMM for the next measurement. Default settling times also precedes Auto Zero. These settling times are not user programmable and are optimized in the design.

When Auto Zero is set to ON or ONCE, a zero measurement is taken before the waveform acquisition begins. This offset is subtracted from all samples in the subsequent acquisition.

Note

Parent topic:

Waveform Acquisitions

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions.html language=enus -->
## TOPIC 00468: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

- [Waveform Acquisition Defaults](waveform-acquisition-defaults.html)
- [Waveform Acquisition Measurement Cycle](waveform-acquisition-measurement-cycle.html)
- [Analog Bandwidth](analog-bandwidth.html)
- [Nyquist Theorem](nyquist-theorem.html)
- [Overranging](overranging.html)
- [Input Coupling](input-coupling.html)
- [Sample Rate](sample-rate.html)
- [Transient Measurement Considerations](transient-measurement-considerations.html)
- [Current Waveforms](current-waveforms.html)

Parent topic:

NI PXIe-4082

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions_2.html language=enus -->
## TOPIC 00469: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions_2.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

Parent topic:

NI 4081

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions_3.html language=enus -->
## TOPIC 00470: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions_3.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

Parent topic:

NI PXIe-4080

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions_4.html language=enus -->
## TOPIC 00471: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions_4.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

Parent topic:

NI 4072

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions_5.html language=enus -->
## TOPIC 00472: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions_5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions_5.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

Parent topic:

NI 4071

<!--NI_TOPIC bundle=ni-dmm path=waveform-acquisitions_6.html language=enus -->
## TOPIC 00473: Waveform Acquisitions

- bundle_id: `ni-dmm`
- source_path: `waveform-acquisitions_6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm/raw/resource/enus/waveform-acquisitions_6.html
- document_id: `ni-dmm`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

### Waveform Acquisitions

In addition to its other capabilities, the DMM can acquire waveforms. The following sections provide information on optimizing waveform acquisitions.

Parent topic:

NI 4070
