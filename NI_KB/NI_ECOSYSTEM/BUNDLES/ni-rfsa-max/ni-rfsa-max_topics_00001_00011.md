# NI DOCUMENT BUNDLE: ni-rfsa-max

<!--NI_BUNDLE_CHUNK bundle=ni-rfsa-max start=1 end=11 -->
<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_associating.html language=enus -->
## TOPIC 00001: Associating NI-RFSA Modules

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_associating.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_associating.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Associating NI-RFSA Modules

To control multiple hardware modules as a single RF device, you must first associate the modules. MAX treats the hardware modules as separate devices. If you are using a hardware system (PXI-5661, PXIe-5663/5663E/5665/5667/5668/5668 with PXIe-5698, or PXIe-5830/5831/5831 with PXIe-5653/5832/5841 with PXIe-5655), you must associate the devices for transparent operation of all hardware modules as a single device using NI-RFSA.

Complete the following steps to associate modules in MAX:

1. In the configuration tree, select the module associated with your hardware system, as identified in the following table.
2. In the Associated Devices section for the selected module, select the appropriate module from each system component drop-down list. 
 
 Refer to the following table for a complete list of device associations.

| Hardware System | Associations |
| --- | --- |
| PXI-5661 | Select the PXI-5600 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXI-5142 from the Digitizer list. |
| PXIe-5663/5663E | Select the PXI-5601 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5622 from the Digitizer list and the PXI/PXIe-5652 from the LO list. |
| PXIe-5665 | Select the PXIe-5603/5605 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5622 from the Digitizer list and the PXIe-5653 from the LO list. |
| PXIe-5667 | Select the PXIe-5603/5605 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5622 from the Digitizer list, the PXIe-5653 from the LO list, the PXIe-5693 from the RF Conditioner list, and the PXIe-5694 from the IF Conditioner List. |
| PXIe-5668 | Select the PXIe-5606 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5624 from the Digitizer list and the PXIe-5653 from the LO list. |
| PXIe-5668 with PXIe-5698 | Select the PXIe-5606 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5624 from the Digitizer list, the PXIe-5653 from the LO list and the PXIe-5698 from the RF Conditioner list. |
| PXIe-5830 | Select the PXIe-3621 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5831 | Select the PXIe-3622 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5831 with PXIe-5653 | Select the PXIe-3622 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave LO) list. The mmRH-5582 mmWave Radio Head automatically appears as connected in MAX when you expand the PXIe-3622 configuration tree item. |
| PXIe-5832 | Select the PXIe-3623 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5832 with PXIe-5653 | Select the PXIe-3623 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave LO) list. The mmRH-5582 mmWave Radio Head automatically appears as connected in MAX when you expand the PXIe-3623 configuration tree item. |
| PXIe-5841 with PXIe-5655 | Select the PXIe-5841 Vector Signal Transceiver in the configuration tree. In the Associated Devices section, select the PXIe-5655 from the RF In LO and RF Out LO lists. You must select the same PXIe-5655 from both lists. |

|  | Note Select Not Specified if you do not want to associate a specific module. Select External if you want to use an external module, such as a third-party LO or digitizer. |
| --- | --- |

|  | Note Associations between modules are lost when you move modules to different slots in the chassis. |
| --- | --- |

1. Click Save in the MAX toolbar.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_creating.html language=enus -->
## TOPIC 00002: Creating Dynamic and Static Signal Routes for an NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_creating.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_creating.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Creating Dynamic and Static Signal Routes for an NI-RFSA Device

To establish a dynamic route across segments, you must specify a fully qualified [terminal name](/csh?topicname=nirfsa/terminal-name-syntax.html) for the source
and destination signal.

1. In the configuration tree, double-click Device and Interfaces to see a list of installed devices. Installed devices appear under the name of their associated chassis.

|  | Note If you are using your NI-RFSA device with the LabVIEW Real-Time Module, expand Remote Systems. Find your target IP address or name, expand it, and then expand Devices and Interfaces. |
| --- | --- |

1. Select your chassis in the configuration tree. The attributes of your chassis are displayed on the right of the MAX window.
2. Click the Trigger tab below the attributes view. A table in the Triggers view shows the PXI
trigger bus segments of your chassis.
3. Configure the static route that you want to make.
4. Save the changes.

To establish a dynamic route across segments, you must specify a fully qualified terminal name for the source and destination signal.

|  | Note You may not be able to establish a dynamic route across segments if your application already contains too many static routes between PXI trigger buses of your chassis or if your hardware route segmentation does not support dynamic signal routing. Refer to your chassis documentation to determine the number of allowed static routes between the PXI trigger buses of your chassis and whether your chassis supports dynamic signal routing. |
| --- | --- |

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_locating.html language=enus -->
## TOPIC 00003: Locating an NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_locating.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_locating.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Locating an NI-RFSA Device

To locate your NI-RFSA device in MAX, complete the following steps:

1. In the configuration tree, double-click Device and Interfaces to see a list of installed devices. Installed devices appear under the name of their associated chassis.

|  | Note If you are using your NI-RFSA device with the LabVIEW Real-Time Module, expand Remote Systems. Find your target IP address or name, expand it, and then expand Devices and Interfaces. |
| --- | --- |

1. Expand your chassis tree item. MAX lists all devices installed in the chassis. Your default device names may vary.
2. Record the device identifier MAX assigns to the hardware. Use this identifier when programming your NI-RFSA device. For hardware systems, record the device identifier for the downconverter module.

|  | Tip Instead of using the default naming convention, you may find it convenient to rename your devices in MAX. |
| --- | --- |

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_removing.html language=enus -->
## TOPIC 00004: Removing a Simulated NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_removing.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_removing.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Removing a Simulated NI-RFSA Device

To remove a simulated NI-RFSA device in MAX, complete the following steps:

1. Right-click the device name in the configuration tree.
2. Select Delete .

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_renaming.html language=enus -->
## TOPIC 00005: Renaming an NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_renaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_renaming.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Renaming an NI-RFSA Device

MAX allows you to rename each of your NI-RFSA devices. 
 The MAX name is used in NI-RFSA to operate the hardware resources. 
 You are not required to change the device names from the default, but doing so can make programming easier. 
 To rename your NI-RFSA device in MAX, complete the following steps:

1. Select the device name in the configuration tree.
2. Within the Settings section, enter a new name for your NI-RFSA device in the Name textbox.
3. Click Save in the MAX toolbar.
4. Verify that the new names for all of your devices are displayed before associating your devices.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_self_test.html language=enus -->
## TOPIC 00006: Running a Self-Test on an NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_self_test.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_self_test.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Running a Self-Test on an NI-RFSA Device

The MAX self-test performs a basic verification of hardware resources. To run a self-test on your NI-RFSA device in MAX, complete the following steps:

|  | Note You can only perform a self-test on the individual associated modules within a hardware system. |
| --- | --- |

1. Select the device name in the configuration tree.
2. Click Self-Test in the MAX toolbar.
 [IMAGE alt='Note' src='note.gif']
 **Note** For the PXIe-3621/3622/3623, you can perform a basic or intermediate self-test. Use a basic self-test to verify communication with the device. Use an intermediate self-test to verify analog cable connections and locate failures on the device and associated devices.
3. A message appears indicating the self-test result. Close the dialog box to continue.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_simulating.html language=enus -->
## TOPIC 00007: Simulating an NI-RFSA Device

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_simulating.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_simulating.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Simulating an NI-RFSA Device

Simulate an NI-RFSA device using NI-RFSA or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated NI-RFSA device to evaluate an NI product for which you do not have hardware.

|  | Note PXI-5600 RF signal downconverters cannot be simulated by MAX or NI-RFSA. PXIe-5624 IF digitizers cannot be simulated by MAX, and can be simulated by NI-RFSA only as components of PXIe-5668 vector signal analyzers. Simulation is supported for all other devices. |
| --- | --- |

#### MAX

Complete the following steps to create and configure a simulated NI-RFSA device in MAX.

1. Launch MAX.
2. Select Devices and Interfaces in the MAX configuration tree, and click Create New in the MAX toolbar. The Create New dialog box opens.
3. Select Simulated NI-DAQmx Device or Modular Instrument , and click Finish . The Create Simulated NI-DAQmx Device dialog box opens.
4. Expand RF Devices , and select the NI-RFSA device to simulate.

|  | Note There is no option to simulate a vector signal analyzer. If you want to simulate a vector signal analyzer, you must simulate the individual devices that comprise the vector signal analyzer. |
| --- | --- |

1. Click OK . The NI-RFSA device appears in the MAX configuration tree with a yellow icon to indicate that it is a simulated device.

#### NI-RFSA

Complete the following steps to create and configure a simulated NI-RFSA device using NI-RFSA.

1. Call Initialize With Options .
2. Set the option string parameter. The option string parameter is composed of the Simulate and Driver Setup keywords, as illustrated in the following example:
 Simulate=1,DriverSetup=Model:*<model number>*;LOBoardType:*<type>*

##### Example

When simulating a PXIe-5668, you can use either of the following **option string** parameters:

Simulate=1, DriverSetup=Model:5668R

Simulate=1, DriverSetup=Model:5606; Digitizer:5624R; LO:5653

To set multiple properties, separate their assignments with a comma.

##### Related Topics

[Driver Setup Options](/csh?topicname=nirfsa/driver-setup-options.html)—Refer to this topic for more information about using the Driver Setup string.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_synchronizing.html language=enus -->
## TOPIC 00008: Synchronizing NI-RFSA Devices

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_synchronizing.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_synchronizing.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Synchronizing NI-RFSA Devices

If you plan to share triggers or clocks to synchronize devices, your chassis and controller must be properly detected and identified in MAX.

#### PXI Express devices controlled using MXI-Express:

1. In the MAX configuration tree under Devices and Interfaces, 
 right-click PXI System .
2. Select Identify As , and select External PC . Your chassis is automatically identified.

#### PXI Express controllers:

A PXI Express controller installed in a PXI Express chassis is automatically identified in MAX.

For more information on synchronizing NI-RFSA devices, refer to the *NI-TClk Synchronization Help*.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_top.html language=enus -->
## TOPIC 00009: MAX Help for NI-RFSA Devices

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_top.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_top.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### MAX Help for NI-RFSA Devices

April 2021, 373874J-01

Refer to the following topics to learn how to complete the most common NI-RFSA tasks in Measurement & Automation Explorer (MAX).

[[IMAGE alt='image' src='arrow_close.gif']Adding and Removing Devices](javascript:expand('test1_section','test1_arrow'))

[Locating an NI-RFSA Device](mi_rf_locating.html)

[Removing an NI-RFSA Device](mi_rf_removing.html)

[Simulating an NI-RFSA Device](mi_rf_simulating.html)

[[IMAGE alt='image' src='arrow_close.gif']Configuring an NI-RFSA Device](javascript:expand('test2_section','test2_arrow'))

[Associating NI-RFSA Modules](mi_rf_associating.html)

[Renaming an NI-RFSA Device](mi_rf_renaming.html)

[Running a Self-Test on an NI-RFSA Device](mi_rf_self_test.html)

[Using the NI-RFSA Soft Front Panel](mi_rf_using_sfp.html)

[[IMAGE alt='image' src='arrow_close.gif']Programming an NI-RFSA Device](javascript:expand('test3_section','test3_arrow'))

[Creating Dynamic and Static Signal Routes for an NI-RFSA Device](mi_rf_creating.html)

[Synchronizing NI-RFSA Devices](mi_rf_synchronizing.html)

[[IMAGE alt='image' src='arrow_close.gif']Troubleshooting](javascript:expand('test4_section','test4_arrow'))

[A Device Does Not Appear in MAX](troubleshooting-device_not_in_max.html)

You can launch MAX by navigating to **Start**»**All Programs**»**National Instruments**»**NI MAX** or by clicking the NI MAX desktop icon.

© 2012–2021 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/mi_rf_using_sfp.html language=enus -->
## TOPIC 00010: Using the NI-RFSA Soft Front Panel

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/mi_rf_using_sfp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/mi_rf_using_sfp.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### Using the NI-RFSA Soft Front Panel

To verify your device configuration, use the NI-RFSA Soft Front Panel (SFP) to analyze a simple signal using your hardware.

1. Select the device name in the MAX configuration tree.
2. Click Soft Front Panel in the MAX toolbar. The NI-RFSA SFP launches.
3. In the NI-RFSA SFP, specify a center frequency, span, reference level, and resolution bandwidth for signal analysis.
4. Close the SFP when you have finished signal analysis.

<!--NI_TOPIC bundle=ni-rfsa-max path=maxrfsa/troubleshooting-device_not_in_max.html language=enus -->
## TOPIC 00011: A Device Does Not Appear in MAX

- bundle_id: `ni-rfsa-max`
- source_path: `maxrfsa/troubleshooting-device_not_in_max.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-max/raw/resource/enus/maxrfsa/troubleshooting-device_not_in_max.html
- document_id: `ni-rfsa-max`
- page_type: `leaf`
- content_type: ``

### A Device Does Not Appear in MAX

If your NI-RFSA device does not appear in MAX, complete the following steps:

1. In the MAX configuration tree, expand the Chassis tree.
2. Press <F5> to refresh the list of installed devices.
3. If the NI-RFSA device is still not listed, power off the system, ensure that the NI-RFSA device is correctly installed, and restart the system.
4. Navigate to the Device Manager.
  - (Windows 10/8.1) Right-click the Start button, and select Device Manager .
  - (Windows 7) Select Start » Control Panel » Device Manager .
5. If you are using a PXI controller, verify that a National Instruments entry appears in the system device list. 
 Reinstall the driver software and the hardware devices if error conditions are present in the list. 
 If you are using a MXI-3 controller, right-click PCI-to-PCI Bridge and select Configure from the shortcut menu to verify that the bridge is enabled.
6. If the NI-RFSA device still fails to appear in MAX, contact NI technical support or visit ni.com/support.
