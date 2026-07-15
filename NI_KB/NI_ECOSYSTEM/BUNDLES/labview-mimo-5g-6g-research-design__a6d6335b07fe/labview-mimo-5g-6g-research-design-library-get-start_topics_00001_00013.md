# NI DOCUMENT BUNDLE: labview-mimo-5g-6g-research-design-library-get-start

<!--NI_BUNDLE_CHUNK bundle=labview-mimo-5g-6g-research-design-library-get-start start=1 end=13 -->
<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=assign-ip.html language=enus -->
## TOPIC 00001: Assigning IP Addresses to Control PC and Ettus USRP X410

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `assign-ip.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/assign-ip.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Before assigning IP addresses, you must connect the control PC and the Ettus USRP X410 with a USB cable and image the PXI controller. The PXI controller is automatically assigned an IP address after imaging. Complete any of the following steps on both the gNodeB and UE sides to assign IP addresses t

Assigning IP Addresses to Control PC and Ettus USRP X410

Ettus USRP X410

Ettus USRP X410

- Statically assign IP addresses to the control PC and the Ettus USRP X410. 
 The IP addresses of the control PC and the Ettus USRP X410
 should be in the same domain as the IP address of the PXI controller.
- If you find the IP address of the control PC is not in the same domain as the
 IP address of the PXI controller, change the IP address of the control PC to the
 same domain as the PXI controller.
- If you find the IP address of the Ettus USRP X410 is not in
 the same domain as the IP address of the PXI controller, login to PuTTY using
 the root user account with no password and change the IP address of the Ettus USRP X410 by running the following command:
 ifconfig eth0 <ip address> netmask <255.255.255.0>
 up.

Related tasks:

- Setting Up a System
- Imaging PXI Controllers

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=changes.html language=enus -->
## TOPIC 00002: New Features and Changes

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/changes.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of the LabVIEW MIMO 5G/6G Research Design Library. LabVIEW MIMO 5G/6G Research Design Library 2.0 New Features and Changes Supports configuring the physical-layer parameters in config_user.json for 5G NR wavef

New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of the LabVIEW MIMO 5G/6G
 Research Design Library.

#### LabVIEW MIMO 5G/6G
 Research Design Library 2.0
 New Features and Changes

- Supports configuring the physical-layer parameters in
 config_user.json for 5G NR waveforms on both the gNodeB and UE
 sides.
- Adds the 5G NR miniRAN gNB L1C and 5G NR miniRAN UE L1C
 (NSA & SA) VIs for system configuration.
- Supports customizing functions with the 5G NR miniRAN gNB
 X410(FPGA) and 5G NR miniRAN UE X410(FPGA) VIs.
- Requires LabVIEW 2020 Digital Filter Design Toolkit (32-bit).

Related tasks:

- Configuring the System
- Installing the Software

Related reference:

- Customizing Functions

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=component.html language=enus -->
## TOPIC 00003: LabVIEW MIMO 5G/6G Research Design Library System Components

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `component.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/component.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW MIMO 5G/6G Research Design Library system is a configurable hardware and software system designed for generating and analyzing 5G NR signals in PDSCHs. Hardware Components Required Hardware Components from NI Part Number Description Quantity 786991-01 PXIe-1092, 9-slot 3U PXI Express cha

LabVIEW MIMO 5G/6G
 Research Design Library
 System Components

The LabVIEW MIMO 5G/6G
 Research Design Library system is a configurable hardware and
 software system designed for generating and analyzing 5G NR signals in PDSCHs.

#### Hardware
 Components

| Part Number | Description | Quantity |
| --- | --- | --- |
| 786991-01 | PXIe-1092, 9-slot 3U PXI Express chassis with Timing and Synchronization option | 2 |
| 787806-01 | PXIe-8881 Xeon 18-core controller | 2 |
| 787272-01 | Ettus USRP X410 (4 TX and 4 RX, 400 MHz bandwidth, 1 MHz to 7.2 GHz SDR, GPSDO) | 2 |
| 785157-01 | PXIe-8394, x8, Gen 3 MXI-Express Daisy-Chain Interface | 2 |
| 784306-01 | CDA-2990 8-channel clock distribution accessory with GPSDO | 1 |
| 785550-01 | MXI-Express cable, Gen 3 x8, copper, 1 m | 2 |
| Depending on locations | Power cord, 125 V, 15 A | 4 |
| 783469-01 | Cable assembly, SMA to SMA, 1 m | 10 |

| Component | Quantity |
| --- | --- |
| Monitor | 2 |
| Keyboard | 2 |
| Mouse | 2 |
| ETH cable | 8 |
| VAT-30+ Attenuator | 4 |
| Network switch | 1 |
| Desktop PC or laptop | 2 |

| Part Number | Description | Quantity |
| --- | --- | --- |
| 786774-01 | 1 TB NVMe Solid State Drive Upgrade, M.2, 80 mm | 2 |
| 785971-01 | PXIe-1095, 18-slot 3U PXI Express chassis with Timing and Synchronization option | 2 |

#### Software Components

- LabVIEW MIMO 5G/6G
 Research Design Library
- Windows 10 64-bit Operating System (for the Control PC)
- LabVIEW Real-Time (NI Linux Real-Time) Operating System (for the PXI
 Controller)
- LabVIEW 2020 (32-bit)
- LabVIEW 2020 FPGA Module
- LabVIEW 2020 Real-Time Module
- NI-USRP 21.0
- LabVIEW 2020 Digital Filter Design Toolkit (32-bit)

#### Additional Required
 Components

Prepare components required for setting up Ettus USRP X410 as described in the *Ettus USRP X410
 Getting Started Guide*.

Related information:

- Ettus USRP X410 Getting Started Guide

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=config-system.html language=enus -->
## TOPIC 00004: Configuring the System

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `config-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/config-system.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps on both the gNodeB and UE sides to configure the LabVIEW MIMO 5G/6G Research Design Library system: Login to PuTTY with the following information. IP address of the PXI controller Username: admin Password: admin Run the following command on the gNodeB and UE PXI controll

Configuring the System

LabVIEW MIMO 5G/6G
 Research Design Library

1. Login to PuTTY with the following information. 
 IP address of the PXI controller
 Username: admin
 Password: admin
2. Run the following command on the gNodeB and UE PXI controllers to configure
 "Configuration_File_videostream.ini": vim
 /home/admin/Configuration_File_videostream.ini.
3. On OpenSSH SSH client of both the gNodeB and UE
 "Configuration_File_videostream.ini", add the following IP
 addresses and port numbers. 
 RT Physical IP address:Port: Add the IP address and port number
 of the gNodeB or UE PXI controller.
 gNB Virtual IP address:Port: Add the same IP address and port
 number in the following figure.
 UE Virtual IP address:Port: Add the same IP address and port
 number in the following figure.
 UE VLC IP address:Port: Add the IP address and port number of
 the UE control PC.
 
[IMAGE alt='IP Addresses and Port Numbers' src='GUID-682DF147-30F4-417F-8B33-25890BB9C4C9-a5.svg']
4. Optional: 
 Configure the physical-layer parameters.
  1. Run the following command to open gNodeB or UE
 config_user.json with a File Transfer Protocol application,
 such as WinSCP, or a text editor, such as Vim. 
 gNodeB: cd
 /home/admin/L2_Stubs/L2Stub_v1.8/ni_ue/gNBL2Stub/config_user.json
 UE: cd
 /home/admin/L2_Stubs/L2Stub_v1.8/ni_ue/ueL2Stub/config_user.json
  2. Follow the comments in config_user.json to modify the
 physical-layer parameters.
  3. Save config_user.json.
5. Run the following commands in sequence on both the gNodeB and UE sides to access the
 gNBL2Stub and ueL2Stub directories on the PXI controllers. 
 
 The following figure shows an example of running the previous commands in sequence.
 
[IMAGE alt='Example Commands' src='GUID-ABE9BF8B-C458-4D0C-BE42-FA57A551DBE5-a5.png']
  1. Either of the following commands. 
 gNodeB: cd
 /home/admin/L2_Stubs/L2Stub_v1.8/ni_ue/gNBL2Stub/
 UE: cd /home/admin/L2_Stubs/L2Stub_v1.8/ni_ue/ueL2Stub/
  2. Run the following command only when you configure the system for the first time:
 chmod +x L2StubIperf.
  3. ./L2StubIperf
6. Run the gNodeB or UE LabVIEW Real-Time VI in the following directories. 
 gNodeB VI: C:\Program Files (x86)\National Instruments\LabVIEW
 2020\examples \LabVIEW MIMO 5G-6G Research Design Library\gNB\5G NR miniRAN gNB
 L1C
 UE VI: C:\Program Files (x86)\National Instruments\LabVIEW 2020\examples
 \LabVIEW MIMO 5G-6G Research Design Library\UE\5G NR miniRAN UE L1C (NSA &
 SA)
7. Once System State on the front panel of the LabVIEW Real-Time VI
 returns Starting Slot Procedure, open the gNodeB or UE GUI in the
 following directories. 
 gNodeB GUI: LabVIEW MIMO 5G-6G Research Design Library \GUI\gNB Monitoring
 GUI
 UE GUI: LabVIEW MIMO 5G-6G Research Design Library \GUI\UE Monitoring
 GUI
8. On the General tab of the GUI, enter the IP address of the PXI
 controller in the IPv4 box.
9. Click Connect to connect to the PXI controller.
10. Ensure the System tab appears on the GUI after the connection is
 established. 
 The following figures show example System tabs on the gNodeB and
 UE GUIs.
 Figure 5.Example System Tab on the gNodeB GUI
 
 
[IMAGE alt='Example System Tab on the gNodeB GUI' src='GUID-46FBE774-561F-45F1-B18B-E4449FC876F0-a5.png']
 Figure 6.Example System Tab on the UE GUI
 
 
[IMAGE alt='Example System Tab on the UE GUI' src='GUID-34065589-47BF-4B4B-8FE8-7FAEDE21F1A5-a5.png']

Related reference:

- LabVIEW MIMO 5G/6G Research Design Library 2.0 New Features and Changes

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=customize-function.html language=enus -->
## TOPIC 00005: Customizing Functions

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `customize-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/customize-function.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `reference`
- source_description: Introduced in LabVIEW MIMO 5G/6G Research Design Library 2.0 You can customize functions by modifying the FPGA code in the 5G NR miniRAN gNB X410(FPGA) and 5G NR miniRAN UE X410(FPGA) VIs. When loading the VIs, open the .dll file in the directory that LabVIEW indicates. Contact your NI sales represe

Customizing Functions

Introduced in LabVIEW MIMO 5G/6G
 Research Design Library 2.0

You can customize functions by modifying the FPGA code in the 5G NR miniRAN gNB
 X410(FPGA) and 5G NR miniRAN UE X410(FPGA) VIs.
 When loading the VIs, open the .dll file in the directory that
 LabVIEW indicates.

Contact your NI sales representative, TSE, or AE for more information and
 support.

Related reference:

- LabVIEW MIMO 5G/6G Research Design Library 2.0 New Features and Changes

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=image-pxi-controller.html language=enus -->
## TOPIC 00006: Imaging PXI Controllers

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `image-pxi-controller.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/image-pxi-controller.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps on both the gNodeB and UE sides to image the PXI controllers:The Ettus USRP X410 has an image or filesystem installed. Create a Clonezilla Live USB flash drive with either Rufus USB Creator or YUMI – Multiboot USB Creator. Visit links in Related information for details.

Imaging PXI Controllers

Note

Ettus USRP X410

1. Create a Clonezilla Live USB flash drive with either Rufus USB Creator or YUMI –
 Multiboot USB Creator. 
 Visit links in Related information for details.
2. Copy and extract the Real-Time image to an external USB hard drive.
3. Turn off the PXI controller.
4. Insert the Clonezilla Live USB flash drive and the external USB hard drive into the PXI
 controller.
5. Turn on the PXI controller.
6. Select F10 to open the boot menu.
7. Select the Clonezilla Live UEFI USB flash drive as the boot device. 
 The Clonezilla Live boots from your USB flash drive.
8. Restore the Real-Time image. 
 Refer to *Restore disk image* on the Clonezilla site for
 instructions.
9. Turn off the PXI controller.
10. Remove the Clonezilla Live USB flash drive and the external USB hard drive from the PXI
 controller.
11. Turn on the PXI controller again. 
 NI Linux Real-Time operating system starts normally.
12. Run the following command to set the hostname of the PXI controller: nirtcfg
 –-set section=systemsettings,token=host_name,value=<HOSTNAME>.
13. Run the following command to double-check the hostname: nirtcfg --get
 section=systemsettings,token=host_name.
14. Add the PXI chassis to Remote Systems in NI Measurement &
 Automation Explorer (MAX). 
 Refer to *Creating a Remote System* in *Measurement and Automation
 Explorer* for instructions.

Related information:

- Clonezilla Live on USB flash drive or USB hard drive
- Rufus USB Creator
- YUMI - Multiboot USB Creator
- Restore disk image
- Creating a Remote System

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=install-sw.html language=enus -->
## TOPIC 00007: Installing the Software

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `install-sw.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/install-sw.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps on both the gNodeB and UE sides: Install LabVIEW and Drivers on the control PC. In NI Package Manager, search for LabVIEW and Drivers. Select 2020 and 32-bit for Version and Bitness, respectively. Click INSTALL. Select the following modules: LabVIEW LabVIEW Real-Time Mod

Installing the Software

Complete the following steps on both the
 gNodeB and UE sides:

1. Install LabVIEW and Drivers on the control PC.
  1. In NI Package Manager, search for LabVIEW and Drivers.
  2. Select 2020 and 32-bit
 for Version and Bitness,
 respectively.
  3. Click INSTALL.
  4. Select the following modules: 
 LabVIEW
 LabVIEW Real-Time Module
 LabVIEW FPGA Module
 LabVIEW Digital Filter Design Toolkit
  5. Follow the instructions in the installation prompts.
2. Install the NI-USRP 21.0 on the control PC.
3. Update the FPGA bitfile for Ettus USRP X410. 
 Refer to *NI-USRP* in *Ettus USRP X410
 Getting Started Guide* for more information.
4. Contact your NI sales representative, Technical Support Engineer (TSE), or
 Applications Engineer (AE) to obtain the Real-Time image and the LabVIEW MIMO 5G/6G
 Research Design Library package.
5. Install the package by running Install.exe in the package
 folder.
6. After the installation completes, unzip the XilinxsIp
 folder in the C:\Program Files (x86)\National Instruments\LabVIEW
 2020\examples\LabVIEW MIMO 5G-6G Research Design Library\Common
 directory.

Related reference:

- LabVIEW MIMO 5G/6G Research Design Library 2.0 New Features and Changes

Related information:

- Ettus USRP X410 Getting Started Guide

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=monitor-system-gui.html language=enus -->
## TOPIC 00008: Monitoring System with GUIs

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `monitor-system-gui.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/monitor-system-gui.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Monitor the gNodeB or UE system with graphical user interfaces (GUIs) on the control PC. Open a UE or gNodeB GUI based on the system you want to monitor. A UE GUI monitors a single UE system that connects to a single gNodeB. A gNodeB GUI monitors a single gNodeB system that connects to a single UE.

Monitoring System with GUIs

Monitor the gNodeB or UE system with graphical user interfaces (GUIs) on the control
 PC.

1. Open a UE or gNodeB GUI based on the system you want to monitor. 
 A UE GUI monitors a single UE system that connects to a single
 gNodeB.
 A gNodeB GUI monitors a single gNodeB system that connects to a single
 UE.
2. On the General tab, verify a connection to the PXI
 controller has been successfully established. 
 Refer to *Configuring the System* for instructions for connecting
 to the PXI controller.
3. On the General tab, check Error
 Messages from the respective stacks.
4. On the System tab, configure parameters under
 DL Waveform Selector as the following table
 shows. 
 Parameter
 ValueCC
 Only one CC is supported.
 Antenna port
 A value from 0 through 3
 Slot
 A value from 0 through 19
 Symbol
 A value from 0 through 13
 Channel
 PDSCH
5. On the System tab, observe graphs to monitor the
 connections between the gNodeB and its associated UEs and the state of PXI
 system stacks when the system is running.

Related tasks:

- Configuring the System

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=overview.html language=enus -->
## TOPIC 00009: LabVIEW MIMO 5G/6G Research Design Library Overview

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/overview.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW MIMO 5G/6G Research Design Library helps you generate and analyze 5G NR signals in Physical Downlink Shared Channels (PDSCHs) with the Ettus USRP X410. Key Features The features that set the LabVIEW MIMO 5G/6G Research Design Library apart include the following. Support for 30 kHz subcar

LabVIEW MIMO 5G/6G
 Research Design Library
 Overview

The LabVIEW MIMO 5G/6G
 Research Design Library helps you generate and analyze 5G NR
 signals in Physical Downlink Shared Channels (PDSCHs) with the Ettus USRP X410.

Related information:

- License Setup and Activation

#### Key Features

The features that set the LabVIEW MIMO 5G/6G
 Research Design Library apart include the
 following.

- Support for 30 kHz subcarrier spacing with up to 100 MHz bandwidth in the Frequency
 Range 1 (FR1) band
- Configurable physical-layer parameters for 5G NR waveforms
- 4x4 MIMO operation
- Video streaming
- System configuration with the gNodeB and UE LabVIEW Real-Time VIs
- Function customization with the gNodeB and UE X410 (FPGA) VIs

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=run-video-stream.html language=enus -->
## TOPIC 00010: Running Video Streaming

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `run-video-stream.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/run-video-stream.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Before running video streaming, you must configure the LabVIEW MIMO 5G/6G Research Design Library system and install the VLC media player. Complete the following steps to run video streaming: On the gNodeB side, open a VLC media player window and complete the following steps. Select Media Stream . A

Running Video Streaming

LabVIEW MIMO 5G/6G
 Research Design Library

Complete the following steps to run video
 streaming:

1. On the gNodeB side, open a VLC media player window and complete
 the following steps.
  1. Select Media»Stream. 
 An Open Media dialog appears.
  2. On File Selection, click Add to add a
 video file for streaming.
  3. Click Stream to open a Stream Output
 dialog.
  4. On Source, click Next.
  5. On Destinations, select the Display
 locally checkbox, select UDP (legacy) from the
 list, and then click Add.
  6. Enter RT Physical IP address:Port you previously added to the
 gNodeB "Configuration_File_videostream.ini" into
 Address and Port, respectively.
  7. On Transcoding options, make sure the Activate
 Transcoding checkbox is selected, select the video format you are
 transmitting from the list, and then click Next.
  8. On Miscellaneous Options, select the Stream all
 elementary streams checkbox and then click
 Stream.
2. On the UE side, open a VLC media player window and complete the
 following steps.
  1. Select Media»Open Network Stream. 
 A Open Media dialog appears.
  2. On Network, enter udp://@:UE
 control PC port number you previously added for UE VLC IP
 address:Port.
  3. Click Play.

Related tasks:

- Configuring the System

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=set-up-system.html language=enus -->
## TOPIC 00011: Setting Up a System

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `set-up-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/set-up-system.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to set up a LabVIEW MIMO 5G/6G Research Design Library system: Install the PXI controller and modules into the PXI chassis on both the gNodeB and UE sides. Refer to the documentation of PXI instruments for installation instructions. Visit the NI Product Documentation Cen

Setting Up a System

LabVIEW MIMO 5G/6G
 Research Design Library

1. Install the PXI controller and modules into the PXI chassis on both the gNodeB
 and UE sides. 
 Refer to the documentation of PXI instruments for installation instructions.
 Visit the NI Product Documentation Center for the latest documentation.
2. Connect hardware components on the front side as the following figure
 shows. 
 Figure 1.Hardware Connections on the Front Side
 
 
[IMAGE alt='Hardware Connections on the Front Side' src='GUID-48351B4D-28F3-4CE3-9F00-8F7B381F98DF-a5.png']
3. On both the gNodeB and UE sides, connect hardware components on the rear side
 as the following figure shows. 
 Figure 2.Hardware Connections on the Rear Side
 
 
[IMAGE alt='Hardware Connections on the Rear Side' src='GUID-788F8BAC-A9C0-41ED-8D7B-3AAF53E068D1-a5.png']
4. On the OctoClock, set the PRIMARY REF switch to INTERNAL.

Related information:

- NI Product Documentation Center

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=troubleshoot.html language=enus -->
## TOPIC 00012: Troubleshooting

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `troubleshoot.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/troubleshoot.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `reference`
- source_description: Troubleshoot common issues you may encounter when using the LabVIEW MIMO 5G/6G Research Design Library. What Should I Do If Slot Processing Takes Longer Than Expected After I Ran the L2StubIperf Command?Make sure you access the gNBL2Stub or ueL2Stub directory on the PXI controller, and then run the

Troubleshooting

Troubleshoot common issues you may encounter when using the LabVIEW MIMO 5G/6G
 Research Design Library.

#### What Should
 I Do If Slot Processing Takes Longer Than Expected After I Ran the
 L2StubIperf Command?

1. /etc/init.d/nilvrt stop
2. /etc/init.d/nilvrt start
3. ./L2StubIperf

If the issue persists, reboot the software or hardware.

#### What Should I Do If
 PDSCH CRC Is Flickering on the UE GUI or DL
 Channel Bandwidth, EVM, and DL
 Modulation order Are Flickering on Both the gNodeB and UE
 GUIs?

This issue occurs because fixedSchedule is set
 to True in config_user.json. Change the
 parameter value to False.

#### What Should I Do If a Memory Full
 Error Occurs When I Am Trying to Connect to the gNodeB GUI?

This issue
 occurs because DL subcarrierSpacing is set to
 15 in config_user.json. Change the
 parameter value to 30.

<!--NI_TOPIC bundle=labview-mimo-5g-6g-research-design-library-get-start path=verify-system.html language=enus -->
## TOPIC 00013: Verifying System Setup

- bundle_id: `labview-mimo-5g-6g-research-design-library-get-start`
- source_path: `verify-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-mimo-5g-6g-research-design-library-get-start/raw/resource/enus/verify-system.html
- document_id: `labview-mimo-5g-6g-research-design-library-get-start`
- page_type: `leaf`
- content_type: `task`
- source_description: Before verifying system setup, you must turn on the following system components in sequence. OctoClock Ettus USRP X410 PXI chassis Complete the following steps on both the gNodeB and UE sides to verify system setup. Open NI MAX on the control PC. In NI MAX, verify the name of the Ettus USRP X410 in

Verifying System Setup

1. OctoClock
2. Ettus USRP X410
3. PXI chassis

Complete the following steps on both the
 gNodeB and UE sides to verify system setup.

1. Open NI MAX on the control PC.
2. In NI MAX, verify the name of the Ettus USRP X410 in the gNodeB and UE systems is "X410". If
 not, change the name to "X410".
3. Verify NI MAX detects all PXI modules in the PXI chassis and check the
 information of each module, such as slot number and alias. 
 The following figure shows example devices that NI MAX detects.
 Figure 3.Example Devices in NI MAX
 
 
[IMAGE alt='Example Devices in NI MAX' src='GUID-53722925-2A3C-42A6-8D4F-00BB52FC3F9B-a5.png']
4. Click the PXI controller to open System Settings.
5. Check the system settings. 
 The firmware version for PXIe-8881 must be 23.0.0f0 or later. The following
 figure shows example system settings.
 Figure 4.Example System Settings
 
 
[IMAGE alt='Example System Settings' src='GUID-726893F9-F700-4884-BD54-14AA2F94A6C1-a5.png']
