# NI DOCUMENT BUNDLE: labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started

<!--NI_BUNDLE_CHUNK bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started start=1 end=8 -->
<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=config-run-ref-design.html language=enus -->
## TOPIC 00001: Configuring and Running the Reference Design

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `config-run-ref-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/config-run-ref-design.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Launch NI Measurement & Automation Explorer (MAX) and ensure MAX detects all the devices in your reference design.For more information about detecting devices in MAX or troubleshooting, refer to the Ettus USRP X410 Getting Started Guide. 5G Signal Generating and Processing Run LabVIEW Reference Arch

Configuring and Running the Reference
 Design

For
 more information about detecting devices in MAX or troubleshooting, refer to the
 *Ettus USRP X410 Getting Started Guide*.

Related information:

- Ettus USRP X410 Getting Started Guide

#### 5G Signal Generating and Processing

1. Run LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 as Administrator.
2. Open the LabVIEW project
 Wireless_Prototype_Software_for_USRP_X410.lvproj. 
 Figure 2.LabVIEW Project View
 
 
[IMAGE alt='LabVIEW Project View' src='GUID-B224336F-501F-43EC-9F55-D1ED1C02E3D8-a5.png']
3. Choose the VI to configure according to your use case: 
 VIUse CaseX410_5GNR_Loopback_WithRFmx.vi
 Performs 5G NR transmission and analysis.X410_5GNR_Loopback_WithoutRFmx.vi
 Performs signal transmission and recording. 
 You must install RFmx NR in your reference design if you use
 X410_5GNR_Loopback_WithRFmx.vi.
4. Configure Setting with the NR waveform you want to
 playback.
  1. In MAX, configure X410 with Device name.
  2. Select Default under Select
 Bitfile to load the default bitfile
 X410ReferenceFpga_4ch_4spc.lvbitx.
 Alternatively, select Customize and click the
 [IMAGE alt='1378' src='GUID-C17743A5-71C5-45D2-8B64-760224905212-a5.png'] button to load a
 customized bitfile.
  3. Configure values or use the default values for the RF parameters of X410 as shown
 in the following figure. Pay attention to the Tx:Gain and Rx:Gain
 according to your hardware connection. 
 Figure 3.Setting
 
 
[IMAGE alt='Setting' src='GUID-BD17C85B-934A-49EC-88E9-362FA0509E87-a5.png']
5. Configure the following tabs. 
 org.dita.html5/xsl/topic.xsl 455Note You can enable only one
 function with one run, 5G Analysis or Rx Record.
 5G Analysis Configuration: Analyzes NR waveform.
 All the NR parameters must exactly match the parameters of NR waveform
 you are transmitting.Figure 4.5G Analysis Configuration
 
 
[IMAGE alt='5G Analysis Configuration' src='GUID-657178DB-465B-4040-896C-588B72F70893-a5.png']
 Rx Record Configuration: Records with Rx. Click the
 file path browse button and specify a
 location to save the record files, such as RAID. Enable
 Disable Buffering to speed up data transfers
 in certain situations. Specify the record size, in four bytes per
 sample, in Samples to Acquire. Specify
 Max TDMS Asynchronous Writes to complete the
 configuration. The saved data has real (I) and imaginary (Q) components.
 I and Q are interleaved (I, Q, I, Q, ...) in the saved files.Figure 5.Rx Record Configuration
 
 
[IMAGE alt='Rx Record Configuration' src='GUID-B745ED0F-8F5C-4669-8A17-AB541CFBFD0D-a5.png']
6. Click Run. The initialization process takes a few
 minutes. Do not switch tabs until the Initialization parameters have non-zero
 values in the Idle&Debug tab. 
 Figure 6.Initialization Parameters During
 Initialization
 
 
[IMAGE alt='Initialization Parameters During Initialization' src='GUID-C6A2CB21-430A-4819-A578-23BB68A35127-a5.png']
 org.dita.html5/xsl/topic.xsl 455Tip To optimize
 performance, disable the Enable Spectrum View button
 when navigating away from the Idle&Debug
 tab.
 Figure 7.Rx - Spectrum
 
 
[IMAGE alt='Rx - Spectrum' src='GUID-2DAB6B3C-E4F8-4BA3-A2E3-8403BDE5014C-a5.png']
  1. Switch to the ModAcc measure tab to view the EVM
 of NR Rx waveform.
  2. If you previously set the Rx Record Configuration, start and monitor
 the record process in the Record Rx Data tab.
7. Click Stop.

#### Extending to mmWave

LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410

- TMYTEK-NI UD Box 5G - Dual Channel x1
- TMYTEK-NI BBox One 5G x1
- TMYTEK-NI BBox Lite 5G x1

For more information about TMYTEK-NI mmWave devices, visit *Research 6G
 Technologies with Wideband RF Record and Playback Systems* or contact your
 local NI sales representative.

1. Switch to mmWave Settings.
2. Specify parameters in the BBoxOne or
 BBoxLite section according to the mmWave BBox devices
 you have. In this case, X410 is working as an IF device and the IF
 output/input should be connected to UD Box.
3. Click Control by LAN.
4. Click Enable mmWave? in the UD
 section to enable your mmWave devices.
5. Wait for 10 seconds until Active in the
 BBoxOne or BBoxLite section is
 on (green).

Related information:

- Research 6G Technologies with Wideband RF Record and Playback
 Systems

#### Fast Beam Steering

1. Open X410_5GNR_Loopback_WithRFmx.vi or
 X410_5GNR_Loopback_WithoutRFmx.vi. 
 org.dita.html5/xsl/topic.xsl 455Note You must install RFmx NR in your reference design if you use
 X410_5GNR_Loopback_WithRFmx.vi.
2. In the Setting section, select
 FastBeamSteering under Select Bitfile to
 load X410ReferenceFpga_4ch_4spc_FBS.lvbitx. Alternatively, select
 Customize and click the [IMAGE alt='1378' src='GUID-C17743A5-71C5-45D2-8B64-760224905212-a5.png'] button to load a customized fast beam
 steering bitfile.
3. Switch to the mmWave Settings tab.
4. Specify parameters in the BBoxOne or
 BBoxLite section according to the mmWave BBox devices you
 have.
5. Click Control by SPI.
6. Click Enable mmWave? in the UD section to
 enable your mmWave devices.
7. Wait for 10 seconds until Active in the
 BBoxOne or BBoxLite section is on
 (green).
8. Under Control by SPI, select a row in Beam Pattern
 Table. 
 Each row specifies a default beam pattern.
9. Optional: 
 Click Edit selected pattern and modify beam forming parameters
 to adjust the default beam pattern based on your test needs.
10. Select a port from the SPI Port list according to your hardware
 connection.
11. Click Commit. 
 The Ettus USRP X410 generates an SPI command based on the
 beam pattern you configured and sends the SPI command to the mmWave BBox devices. The
 mmWave BBox devices perform fast beam steering after receiving the SPI
 command.
12. Switch to the Spectrum TRX tab to check the impact of fast beam
 steering on spectrums.

Related reference:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 2.0 New Features and Changes

#### Multi-Channel Rx Recording (Single
 Device)

1. Run LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 as Administrator.
2. Open the LabVIEW project
 Wireless_Prototype_Software_for_USRP_X410.lvproj. 
 Figure 8.LabVIEW Project View - X410_Record.vi
 
 
[IMAGE alt='LabVIEW Project View - X410_Record.vi' src='GUID-2B94CD94-4867-43A0-BB19-4081B9E013B1-a5.png']
3. Open X410_Record.vi for multi-channel streaming with a
 single X410
 device. 
 Figure 9.Rx Recording - Multi-Channels
 
 
[IMAGE alt='Rx Recording - Multi-Channels' src='GUID-384E4883-28B9-42DB-90F3-06804FF6CE37-a5.png']
4. Complete the following configuration:
  1. Specify Device Name according to the X410 name
 in MAX.
  2. Specify Enabled Channel (0, 1, 2, 3) to capture
 signal. You can only enable one, two, or four channels. When specifying
 more than one channel, enter channel names in numerical order. For
 example, to enable four channels, enter channel names as 0,
 1, 2, 3.
  3. Specify IQ rate. IQ rate can be up to 491.52 MSps with one or two channels
 enabled, and up to 245.76 MSps with four
 channels enabled.
  4. Under Bitfile Path, keep the default bitfile
 RxRecording.lvbitx or load a customized Rx
 recording bitfile.
  5. Specify Rx Gain according to the received
 signal, RF frequency, and Active Antenna as
 RX1.
  6. Specify file information, including file path, file size, and block
 size per write. You can use the default values or specify values based
 on your test needs. This recording VI saves data as Samples of U32
 (combining I data I16 and Q data I16 into U32, with high-order byte is Q
 and low-order byte is I). For example, if you use PXIe-8267, the maximum
 samples to acquire is close to 1 T
 samples.
5. Click Run to start recording.
6. Monitor the CustomizedData.status. If overflow shows up,
 you can adjust your setting parameters.
7. X410_Record.vi stops when recording finishes.

Related reference:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 1.1 New Features and Changes

#### Multi-Channel Tx Playback (Single
 Device)

1. Run LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 as Administrator.
2. Open the LabVIEW project
 Wireless_Prototype_Software_for_USRP_X410.lvproj. 
 Figure 10.LabVIEW Project View -
 X410_Playback.vi
 
 
[IMAGE alt='LabVIEW Project View - X410_Playback.vi' src='GUID-73BFFF86-32A5-4A4A-BE02-C2D050933314-a5.png']
3. Open X410_Playback.vi for multi-channel streaming with a
 single X410
 device. 
 Figure 11.Tx Playback - Multi-Channels
 
 
[IMAGE alt='Tx Playback - Multi-Channels' src='GUID-DC957A94-FE95-435D-BF88-8DC47E6E271A-a5.png']
4. Complete the following configuration:
  1. Specify Device Name according to the X410 name
 in MAX.
  2. Specify Enabled Channel (0, 1, 2, 3) to transmit
 signal. You can only enable one, two, or four channels. When specifying
 more than one channel, enter channel names in numerical order. For
 example, to enable four channels, enter channel names as 0,
 1, 2, 3.
  3. Specify IQ rate. IQ rate can be up to 491.52 MSps with one or two channels
 enabled, and up to 245.76 MSps with four
 channels enabled.
  4. Under Bitfile Path, keep the default bitfile
 TxPlayback.lvbitx or load a customized Tx
 playback bitfile.
  5. Specify Tx Gain according to the received
 signal, RF frequency, and Active Antenna as
 Tx/RX0.
  6. Specify file information, including playback file path, write block
 size, and Max TDMS Asynchronous Read. You can use the default values or
 specify values based on your test needs. This playback VI transmits data
 as Samples of U32 (combining I data I16 and Q data I16 into U32, where
 high-order byte is Q and low-order byte is I). For example, if you use
 PXIe-8267, the maximum samples to transmit is close to 1 T samples.
5. Click Run to start transmitting.
6. Monitor the CustomizedDataTx.status. If overflow shows
 up, you can adjust your setting parameters.
7. X410_Playback.vi stops when transmitting finishes.

Related reference:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 1.1 New Features and Changes

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=connect-hardware.html language=enus -->
## TOPIC 00002: Connecting the Hardware

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `connect-hardware.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/connect-hardware.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Connecting Hardware for Record & PlaybackIf you want to use record & playback, connect hardware components by following the NI-USRP section in the Ettus USRP X410 Getting Started Guide.If your part number contains PXIe-8267, set up PXIe-8267 by following the PXIe-8267 Getting Started Guide. Connecti

Connecting the Hardware

#### Connecting Hardware for
 Record & Playback

If you want to use record &
 playback, connect hardware
 components by following the *NI-USRP* section in the *Ettus USRP
 X410 Getting Started Guide*.

Note

PXIe-8267 Getting Started
 Guide

#### Connecting Hardware for Fast
 Beam Steering

The following figure shows an example of hardware
 connections for fast beam steering. You can adjust hardware connections based on
 your test needs.

You must keep the IP addresses of all the hardware components
 in the same domain.

Figure 1.

[IMAGE alt='Hardware Connections for Fast Beam Steering' src='GUID-F61BD66F-AF45-4507-9996-A4E580F6D5AD-a5.svg']

Related information:

- Ettus USRP X410 Getting Started Guide
- PXIe-8267 Getting Started Guide

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=customizing-reference-fpga.html language=enus -->
## TOPIC 00003: Customizing the Reference FPGA

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `customizing-reference-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/customizing-reference-fpga.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: To modify the reference FPGA project, you must install the NI Streaming Controller IP from VI Package Manager (VIPM). The NI Streaming Controller IP contains VIs that the reference FPGA project requires.The reference FPGA project source code is in the C:\Program Files\National Instruments\LabVIEW 20

Customizing the Reference FPGA

NI Streaming Controller IP

VI Package Manager (VIPM)

NI Streaming Controller IP

The reference FPGA project source code is in the C:\Program
 Files\National Instruments\LabVIEW 2022\examples\Wireless Prototype Software for
 USRP X410\Reference FPGA Project directory. The source code contains
 the following projects:

- referenceFPGA (USRP-X410 4ch-4spc)
 CustomizedFIFORx.lvproj —Rx Recording project for building the Rx
 recording bitfile.
- referenceFPGA (USRP-X410 4ch-4spc)
 CustomizedFIFOTx.lvproj —Tx Playback project for building the Tx
 playback bitfile.
- referenceFPGA (USRP-X410 4ch-4spc)
 FastBeamSteering.lvproj —Fast beam steering project for building the
 fast beam steering bitfile.

You can modify these bitfiles to fit your application needs. The customized
 bitfiles are saved to the C:\Program Files\National Instruments\LabVIEW
 2022\examples\Wireless Prototype Software for USRP X410\Reference FPGA
 Project\FPGA Bitfiles directory by default. You can specify another
 directory to save your bitfiles.

Related reference:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 1.1 New Features and Changes
- LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 2.0 New Features and Changes

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=install-software.html language=enus -->
## TOPIC 00004: Installing the Software

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `install-software.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/install-software.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Before installing the LabVIEW Reference Architecture Software for Prototyping Wireless Systems with Ettus USRP X410, you must complete the steps described in the Installing the Software sections of the Ettus USRP X410 Getting Started Guide and ensure your LabVIEW reference design meets the following

Installing the Software

LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410

Installing the Software

Ettus USRP X410 Getting
 Started Guide

- Windows 10 (64-bit)
- LabVIEW 2022 Q3 (64-bit)
- LabVIEW 2022 Q3 FPGA Module
- (Optional) RFmx NR 2022 Q3 org.dita.html5/xsl/topic.xsl 455 Note Install NI-RFSA when
 installing RFmx NR.
- NI-USRP 2022 Q4

1. Download the LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 from ni.com.
2. Install the software.
3. Activate the software with NI License Manager.
4. Find the source code in the C:\Program Files\National
 Instruments\LabVIEW 2022\examples\Wireless Prototype Software for USRP
 X410 directory.

Related information:

- Ettus USRP X410 Getting Started Guide

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=new-feature-change.html language=enus -->
## TOPIC 00005: New Features and Changes

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `new-feature-change.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/new-feature-change.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of the LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410. LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 2.0 New Features and Changes Support up to 64 preconfigured

New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of the LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410.

#### LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410 2.0 New Features and Changes

- Support up to 64 preconfigured beams for fast beam steering in Tx mode and Rx mode,
 respectively.
- Support single beam steering in 2 μs.
- Build custom reference FPGA bitfiles for fast beam steering using the FPGA project included
 with the LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 .
- Change the offering name from Wireless Prototype System for USRP X410 to
 LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410.

Related tasks:

- Fast Beam Steering
- Customizing the Reference FPGA

#### LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410 1.1 New Features and Changes

- Support up to 245.76 MSps with four channels for
 multi-channel Rx recording.
- Support multi-channel Tx playback.
- Build custom reference FPGA bitfiles for Rx recording and Tx playback using the FPGA
 project included with the LabVIEW Reference Architecture Software for
 Prototyping Wireless Systems with Ettus USRP X410 .

Related tasks:

- Multi-Channel Rx Recording (Single Device)
- Multi-Channel Tx Playback (Single Device)
- Customizing the Reference FPGA

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=overview.html language=enus -->
## TOPIC 00006: Overview

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/overview.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: This document explains how to install, configure, and verify the record & playback and fast beam steering features of LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410, and describes common tasks you may perform. This document applies to all design variants, such as the PCIe or

Overview

This document explains how to install, configure, and verify the record &
 playback and fast beam steering
 features of LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410, and describes common tasks you may
 perform. This document applies to all design variants, such as the PCIe or PXIe
 option.

Use the record &
 playback feature to generate and
 process 5G signals and perform continuous streaming with the Ettus USRP X410.

Use the fast beam steering feature to control beams in real time. The Ettus USRP X410 generates an SPI command based
 on user-defined beam patterns and sends the SPI command to the mmWave BBox devices. The
 mmWave BBox devices perform fast beam steering after receiving the SPI command.

Notice

record &
 playback

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=receiving-shipment.html language=enus -->
## TOPIC 00007: Receiving the Shipment

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `receiving-shipment.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/receiving-shipment.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Read the documentation, such as specifications and getting started guides, of the components included in your LabVIEW reference design. Visit the NI Product Documentation Center for the latest documentation. LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 arrives with all the

Receiving the Shipment

Read the documentation, such as
 specifications and getting started guides, of the components
 included in your LabVIEW reference design. Visit the NI Product
 Documentation Center for the latest documentation.

LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410

Related information:

- NI Product Documentation Center

#### Verifying Shipment Contents

Verify the following items are included in the shipment based on your reference design part
 number.

| Reference Design Part Number | Component | Quantity |
| --- | --- | --- |
| 868001-04, USRP X410 LabVIEW Bundle for 6G Research Standard | Cable assy, SMA to SMA, coax, RG-402, 50 Ω, 1 m | 2 |
| PXIe-8394, x8, Gen 3 MXI-Express Daisy-Chain Interface | 1 |  |
| PXIe-8267 high-speed NVMe data storage module, 4 TB | 1 |  |
| MXI-Express cable, Gen 3 x8, copper, 3 m | 1 |  |
| PXIe-1092, 9-slot 3U PXI Express chassis with Timing and Synchronization option | 1 |  |
| Ettus USRP X410 (4 TX and 4 RX, 400 MHz bandwidth, 1 MHz to 7.2 GHz SDR, GPSDO) | 1 |  |
| PXIe-8881 Xeon 18-core controller, Windows 10 64-bit (Multiple Languages) | 1 |  |
| Packaging BOM, 37.4" × 25.98" × 18.7" box, PADPAK58 QTY 21 | 1 |  |
| 868001-03, USRP X410 LabVIEW Bundle for 6G Research Standard - Chinese Language Controller | Cable assy, SMA to SMA, coax, RG-402, 50 Ω, 1 m | 2 |
| PXIe-8394, x8, Gen 3 MXI-Express Daisy-Chain Interface | 1 |  |
| PXIe-8267 high-speed NVMe data storage module, 4 TB | 1 |  |
| MXI-Express cable, Gen 3 x8, copper, 3 m | 1 |  |
| PXIe-1092, 9-slot 3U PXI Express chassis with Timing and Synchronization option | 1 |  |
| Ettus USRP X410 (4 TX and 4 RX, 400 MHz bandwidth, 1 MHz to 7.2 GHz SDR, GPSDO) | 1 |  |
| PXIe-8881 Xeon 18-core controller, Windows 10 64-bit (Simplified Chinese) | 1 |  |
| Packaging BOM, 37.4" × 25.98" × 18.7" box, PADPAK58 QTY 21 | 1 |  |
| 868002-03, USRP X410 LabVIEW Bundle for 6G Research PCIe Base | Cable assy, SMA to SMA, coax, RG-402, 50 Ω, 1 m | 2 |
| Ettus USRP X410 (4 TX and 4 RX, 400 MHz bandwidth, 1 MHz to 7.2 GHz SDR, GPSDO) | 1 |  |
| PCIe Gen3 Interface Kit for Ettus USRP X4xx (Desktop) | 1 |  |
| Packaging BOM, Container 56.6 × 47.7 × 35.5 cm W/ PADPAK58-20 | 1 |  |
| 868003-03, USRP X410 LabVIEW Bundle for 6G Research PXIe Base | Cable assy, SMA to SMA, coax, RG-402, 50 Ω, 1 m | 2 |
| PXIe-8394, x8, Gen 3 MXI-Express Daisy-Chain Interface | 1 |  |
| MXI-Express cable, Gen 3 x8, copper, 3 m | 1 |  |
| Ettus USRP X410 (4 TX and 4 RX, 400 MHz bandwidth, 1 MHz to 7.2 GHz SDR, GPSDO) | 1 |  |
| Packaging BOM, Container 51.1 × 37.5 × 31.1 cm W/ PADPAK58-06 | 1 |  |
| 868064-26, USRP RF Extension, TMYTEK-NI BBox One 5G 28GHz Beamformer Box 16 Channels | TMYTEK-NI BBox One 5G 28GHz Beamformer Box 16 Channels | 1 |
| 868064-24, USRP RF Extension, TMYTEK-NI BBox Lite 5G 28GHz Beamformer Box 4 Channels | TMYTEK-NI BBox Lite 5G 28GHz Beamformer Box 4 Channels | 1 |
| 868064-22, USRP RF Extension, TMYTEK-NI UD Box 5G Series - Dual Channels | TMYTEK-NI UD Box 5G Series - Dual Channels | 1 |
| 868064-21, USRP RF Extension, TMYTEK-NI UD Box 5G Series - Single Channel | TMYTEK-NI UD Box 5G Series - Single Channel | 1 |

#### Required Components

Prepare additional items for device setup following the *Ettus USRP X410 Getting Started
 Guide*.

Related information:

- Ettus USRP X410 Getting Started Guide

<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started path=troubleshooting.html language=enus -->
## TOPIC 00008: Troubleshooting

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started/raw/resource/enus/troubleshooting.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Troubleshoot common issues with the solutions provided in the following table. For unexpected behavior not covered in the table, restart the system. Common Issues and Solutions in LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410 Issue Solution I receive an Error -68002. Run Lab

Troubleshooting

Troubleshoot common issues with the solutions provided in the following table. For unexpected
 behavior not covered in the table, restart the system.

| Issue | Solution |
| --- | --- |
| I receive an Error -68002. | Run LabVIEW as Administrator. |
| An overflow occurs while streaming. | Adjust streaming-related parameters like file destination, block size per write, Max TDMS Asynchronous Writes, and increase Host Buffer Blocks. |
| I cannot find the USRP X410 in NI MAX. | Try the following solutions: Turn off the Windows Firewall. Ensure you power on the USRP X410 before powering on the PXIe-8881. Ensure you use the Ettus USRP X410 with NI-USRP 2022 Q4. Check cabling. |

Contact your designated support channel if restarting the system or trying the above
 troubleshooting solutions does not resolve your issues.
