# NI DOCUMENT BUNDLE: oscilloscope-probe-compensator-getting-started

<!--NI_BUNDLE_CHUNK bundle=oscilloscope-probe-compensator-getting-started start=1 end=4 -->
<!--NI_TOPIC bundle=oscilloscope-probe-compensator-getting-started path=compatibility.html language=enus -->
## TOPIC 00001: Compatibility

- bundle_id: `oscilloscope-probe-compensator-getting-started`
- source_path: `compatibility.html`
- source_url: https://docs-be.ni.com/bundle/oscilloscope-probe-compensator-getting-started/raw/resource/enus/compatibility.html
- document_id: `oscilloscope-probe-compensator-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The oscilloscope probe compensator is compatible with the following oscilloscopes and PFI lines. Module Connector PXIe/PXI/PCI-5105 Requires a probe capable of compensating high capacitance inputs and a BNC (f)-to-SMB (f) cable with sufficiently low capacitance, such as the 0.08 mSMB-100 (part numbe

Compatibility

The oscilloscope probe compensator is compatible with the following oscilloscopes and PFI lines.

| Module | Connector |
| --- | --- |
| PXIe/PXI/PCI-5105 [1] | PFI 1 |
| PXI/PCI-5152 | PFI 1 |
| PXIe-5160 | PFI 1 |
| PXIe-5162 | PFI 1 |
| PXIe-5163 | SMB PFI 0 [2] |
| PXIe-5164 | SMB PFI 0 [2] |

Parent topic:

Introduction

[<sup>1</sup>](#note_ref-1) Requires a probe capable of compensating high capacitance inputs and a BNC (f)-to-SMB (f) cable with sufficiently low capacitance, such as the 0.08 mSMB-100 (part number 781449-01).

<sup>2</sup> Though the PFI 0 line is also available via the AUX 0 MHDMR connector, the probe compensation signal is available only from SMB PFI 0.

<!--NI_TOPIC bundle=oscilloscope-probe-compensator-getting-started path=compensating-passive-probes.html language=enus -->
## TOPIC 00002: Compensating Passive Probes

- bundle_id: `oscilloscope-probe-compensator-getting-started`
- source_path: `compensating-passive-probes.html`
- source_url: https://docs-be.ni.com/bundle/oscilloscope-probe-compensator-getting-started/raw/resource/enus/compensating-passive-probes.html
- document_id: `oscilloscope-probe-compensator-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Compensating passive probes increases the accuracy of your measurements by matching the capacitance of your probe to the capacitance of a particular oscilloscope input channel. Before beginning this procedure, complete the following: Set up your oscilloscope in a compatible chassis; Install a versio

Compensating Passive Probes

Compensating passive probes increases the accuracy of your measurements by matching the
 capacitance of your probe to the capacitance of a particular oscilloscope input
 channel.

Before beginning this procedure, complete the following:

- Set up your oscilloscope in a compatible chassis;
- Install a version of NI-SCOPE compatible with your oscilloscope on your system; and
- Configure a panel and layout in InstrumentStudio to include your oscilloscope. 
 org.dita.html5/xsl/topic.xsl 455 Note For more information on using InstrumentStudio, refer to the 
 *Instrument Studio Manual* at [ni.com/manuals](http://www.ni.com/manuals).

NI oscilloscopes can output a 1 kHz square wave that you can use
 to compensate passive probes. This procedure assumes your passive probe uses a BNC
 connector and has a 10× attenuation option.

Complete the following steps to compensate a passive probe:

1. Connect the probe to an input channel of your oscilloscope.
  - PXIe-5105 , PXI-5105 , PCI-5105 only:
    1. Connect the BNC end of the probe to the BNC end of the SMB (f) -to- BNC (f) cable.
    2. Connect the SMB end of the cable to an input channel of your
 oscilloscope.
  - All other applicable oscilloscopes: Connect the BNC end of the probe to
 an input channel of your oscilloscope.
2. If your probe has switchable attenuation, ensure the physical switch on the
 probe is set to 10× attenuation.
3. Depending on your probe compensation technique, connect the probe tip to the
 oscilloscope: 
 Instrument
 Compensation
 Technique
 DescriptionPXIe/PXI/PCI-5105
 PXI/PCI-5152
 PXIe-5160
 PXIe-5162
 PXIe-5163
 PXIe-5164
 Oscilloscope Probe
 Compensator
 Connect the SMB end of the
 Oscilloscope Probe Compensator to the PFI connector
 of the oscilloscope that generates the probe
 compensation signal.
 Connect the ground clip of the
 probe to the ground terminal.
 Contact the tip of the probe to
 the square wave terminal.
 Direct connection to oscilloscope
 PFI
 SMB PFI
 Attach the BNC adapter to the
 tip of the probe.
 Connect the ground clip of the
 probe to a ground.
 Connect the probe to the BNC end
 of the SMB (f)-to-BNC (f) cable.
 Connect the SMB end of the cable
 to the PFI connector of the oscilloscope that
 generates the probe compensation signal.
 PXIe/PXI/PCI-5114
 PXIe/PXI/PCI-5122
 PXI/PCI-5124
 PXI/PCI-5142
 DIN PFI
 Attach the BNC adapter to the
 tip of the probe.
 Connect the ground clip of the
 probe to a ground.
 Connect the probe to the BNC end
 of the 9-pin
 DIN–to-BNC cable.
 Connect the DIN end of the cable
 to the DIN connector on the oscilloscope.
 USB-5132
 USB-5133
 BNC PFI
 Attach the BNC adapter to the
 tip of the probe.
 Connect the ground clip of the
 probe to a ground.
 Connect the probe to the PFI
 connector.
 PXIe-5110
 PXIe-5111
 PXIe-5113
 Connection to probe
 compensation terminals
 Connect the ground clip of the
 probe to the ground terminal on the front of the
 oscilloscope.
 Contact the tip of the probe to
 the 5 V square wave
 terminal on the front of the oscilloscope.
4. Enable the probe compensation signal:
  - PXIe-5110 , PXIe-5111 , PXIe-5113 only: No action required, the probe compensation signal
 is enabled by default.
  - All other applicable oscilloscopes: based on
 your programming environment, do either of the following:
    - InstrumentStudio: In the instrument header menu
 ( ) in the upper-right
 corner of the panel, select Probe Compensation»Enabled .
    - NI-SCOPE : Call
 the Probe Compensation Signal Start 
 function.
5. In InstrumentStudio, configure the settings of the input channel to which you
 connected the probe.
  1. Set the channel to On to display the
 signal.
  2. Set the Input impedance of the channel to
 1 MΩ.
  3. (PXIe-5110, PXIe-5111, PXIe-5113 only) Set
 the Vertical Offset to 2.5 V.
  4. Set the Probe attenuation setting to
 10 X.
6. Adjust the vertical range on the input channel until the signal starts to clip
 and then increase the vertical range by one step so that it no longer
 clips. 
 This process ensures you are using the maximum dynamic range of the ADC.
7. Examine the digitized signal and adjust the tunable capacitor on the
 probe. 
 The probe is correctly compensated when the waveform appears as square
 as possible: 
[IMAGE alt='1378' src='GUID-47AE0512-8BC1-4866-8FE9-D65A49A3689D-a5.svg']

A compensated probe conveys signals to the
 input channel accurately, without artificially attenuating or amplifying frequency
 components of the signal.

Tip

- Compensate probes for each channel of the
 oscilloscope;
- Use a compensated probe only with the channel you
 used to compensate it; and
- Compensate your probes frequently.

Parent topic:

Introduction

<!--NI_TOPIC bundle=oscilloscope-probe-compensator-getting-started path=introduction.html language=enus -->
## TOPIC 00003: Introduction

- bundle_id: `oscilloscope-probe-compensator-getting-started`
- source_path: `introduction.html`
- source_url: https://docs-be.ni.com/bundle/oscilloscope-probe-compensator-getting-started/raw/resource/enus/introduction.html
- document_id: `oscilloscope-probe-compensator-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: This guide describes how to use the oscilloscope probe compensator. The oscilloscope probe compensator allows you to compensate passive probes on compatible NI oscilloscopes using traditional compensation terminals.

Introduction

This guide describes how to use the oscilloscope probe compensator.

The oscilloscope probe compensator allows you to compensate passive probes on compatible NI oscilloscopes using traditional compensation terminals.

© 2018–2021 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=oscilloscope-probe-compensator-getting-started path=physical.html language=enus -->
## TOPIC 00004: Physical

- bundle_id: `oscilloscope-probe-compensator-getting-started`
- source_path: `physical.html`
- source_url: https://docs-be.ni.com/bundle/oscilloscope-probe-compensator-getting-started/raw/resource/enus/physical.html
- document_id: `oscilloscope-probe-compensator-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connectors SMB (f) Terminals: compensation signal, ground Dimensions 8.53 cm × 2.03 cm × 0.76 cm (3.94 in. × 0.80 in. × 0.30 in.) Weight 24 g (0.85 oz)

Physical

| Connectors | SMB (f) Terminals: compensation signal, ground |
| --- | --- |
| Dimensions | 8.53 cm × 2.03 cm × 0.76 cm(3.94 in. × 0.80 in. × 0.30 in.) |
| Weight | 24 g (0.85 oz) |

Parent topic:

Introduction
