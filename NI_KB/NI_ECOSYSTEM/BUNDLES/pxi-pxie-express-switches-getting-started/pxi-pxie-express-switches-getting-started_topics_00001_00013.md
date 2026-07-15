# NI DOCUMENT BUNDLE: pxi-pxie-express-switches-getting-started

<!--NI_BUNDLE_CHUNK bundle=pxi-pxie-express-switches-getting-started start=1 end=13 -->
<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=connect-signals-switch-terminal-block.html language=enus -->
## TOPIC 00001: Connecting Signals to Switch Terminal Blocks

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `connect-signals-switch-terminal-block.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/connect-signals-switch-terminal-block.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the documentation for your terminal block to install the terminal block and connect signals to the NI PXI/PXI Express Switch.

Connecting Signals to Switch Terminal Blocks

Refer to the documentation for your terminal block to install the terminal block and connect signals to the NI PXI/PXI Express Switch.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=emc.html language=enus -->
## TOPIC 00002: EMC Guidelines

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `emc.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/emc.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: This product was tested and complies with the regulatory requirements and limits for electromagnetic compatibility (EMC) stated in the product specifications. These requirements and limits provide reasonable protection against harmful interference when the product is operated in the intended operati

EMC Guidelines

This product was tested and complies with the regulatory requirements and limits for electromagnetic compatibility (EMC) stated in the product specifications. These requirements and limits provide reasonable protection against harmful interference when the product is operated in the intended operational electromagnetic environment.

This product is intended for use in industrial locations.
 However, harmful interference may occur in some installations, when the product is
 connected to a peripheral device or test object, or if the product is used in
 residential areas. To minimize interference with radio and television reception and
 prevent unacceptable performance degradation, install and use this product in strict
 accordance with the instructions in the product documentation.

Furthermore, any changes or modifications to the product not expressly approved by NI could void your authority to operate it under your local regulatory rules.

#### EMC Notices

Notice

Notice

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=examples.html language=enus -->
## TOPIC 00003: NI-SWITCH Examples

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/examples.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Examples demonstrate the functionality of the device and serve as programming models and building blocks for your own applications. The NI Example Finder is a utility available for some ADEs that organizes examples into categories and allows you to easily browse and search installed examples. You ca

NI-SWITCH Examples

Examples demonstrate the functionality of the device and serve as programming models
 and building blocks for your own applications. The NI Example Finder is a utility available for
 some ADEs that organizes examples into categories and allows you to easily browse and search
 installed examples. You can see descriptions and compatible hardware models for each example or
 see all the examples compatible with one particular hardware model.

| ADE | How to Locate Examples |
| --- | --- |
| LabVIEW or LabWindows/CVI | Locate examples with the NI Example Finder. Within LabVIEW or LabWindows/CVI, select Help » Find Examples and navigate to Hardware Input and Output » Modular Instruments. |
| ANSI C or Microsoft Visual C/C++ | Locate examples in the <NIDocDir>\\CVI\\Samples\\niswitch directory, where <NIDocDir> is one of the following directories: Windows 8/7/Vista—Users\\Public\\Public Documents\\National InstrumentsWindows XP—Documents and Settings\\All Users\\Documents\\National Instruments |

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=install-hardware-pxi.html language=enus -->
## TOPIC 00004: Installing the Hardware

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `install-hardware-pxi.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/install-hardware-pxi.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must install the software before installing the hardware. Before you install the hardware, refer to the guidelines in the Maintain Forced-Air Cooling Note to Users at ni.com/manuals to ensure that the device can cool itself effectively. To prevent damage to the NI PXI/PXI Express Switch caused b

Installing the Hardware

You must install the software before installing the hardware.

Before you install the hardware, refer to the guidelines in the 
 *Maintain Forced-Air Cooling Note to Users* at 
 [ni.com/manuals](http://www.ni.com/manuals) to ensure that the device can cool itself effectively.

Notice

NI PXI/PXI Express Switch

Caution

#### Installing an NI PXI/PXI Express Switch

Note

Figure 2.

[IMAGE alt='1378' src='GUID-6CC4E53C-409A-4151-82E9-3D5F6C310AC3-a5.svg']

1. NI PXI/PXI Express or NI PXI/SCXI Combination Chassis
2. Controller
3. NI PXI/PXI Express Switch
4. Screws
5. Certain products: Ejector Handle

1. Ensure the AC power source is connected to the chassis before installing the switches. 
 The AC power cord grounds the chassis and protects it from electrical damage while you install the switches.
2. Power off the chassis.
3. If the NI PXI/PXI Express chassis has multiple fan speed settings, ensure that the fans are set to high.
4. Position the chassis so that inlet and outlet vents are not obstructed. 
 For more information about optimal chassis positioning, refer to chassis documentation.
5. Remove the black vinyl caps from all the captive screws on the switch front panel.
6. Identify a supported slot in the NI PXI/PXI Express chassis. 
 Refer to the following table to determine what slots support your switch if you are using a NI PXI Express chassis. Refer to the chassis documentation for details. 
 Table 1.Slot Identification Symbols in an NI PXI/PXI Express Chassis[IMAGE alt='1378' src='GUID-C52C176B-C2E2-4A1D-A0E4-D1AF940FCF1E-a5.svg']NI PXI Peripheral Slot[IMAGE alt='1378' src='GUID-F567489C-4CE9-4CED-94CC-D4D30EC1729E-a5.svg']NI PXI Express Peripheral Slot[IMAGE alt='1378' src='GUID-84A1F363-611E-4341-8D85-7B25494DFD23-a5.svg']NI PXI Express Hybrid Peripheral Slot[IMAGE alt='1378' src='GUID-A75B1CC1-B38C-4661-A003-BE1DF1F16EA6-a5.svg']NI PXI Express System Timing Slot
7. Remove the filler panel of an unused PXI/PXI Express slot.
8. Touch any metal part of the chassis to discharge static electricity.
9. Ensure that the injector/ejector handle of the device is in the unlatched (down) position and swings freely.
10. Holding the device by the injector/ejector handle, slide it into the empty slot, ensuring that the card engages with the card guides in the chassis.
11. When you begin to feel resistance, pull up on the injector/ejector handle to latch the device.
12. Secure the module front panel to the chassis using the front-panel mounting screws. 
 org.dita.html5/xsl/topic.xsl 455Note Tightening the top and bottom mounting screws increases mechanical stability and also electrically connects the front panel to the chassis, which can improve the signal quality and electromagnetic performance.
13. Cover all empty slots using either filler panels (standard or EMC) or slot
 blockers with filler panels, depending on your application. 
 org.dita.html5/xsl/topic.xsl 455Note For more information about installing slot
 blockers and filler panels, go to [ni.com/r/pxiblocker](http://www.ni.com/r/pxiblocker).
14. Power on the chassis.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=install-software.html language=enus -->
## TOPIC 00005: Installing the Software

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `install-software.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/install-software.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: You must be an Administrator to install NI software on your computer. Install an ADE, such as LabVIEW or LabWindows™/CVI™. Download the driver software installer from ni.com/downloads. Package Manager downloads with the driver software to handle the installation. Refer to the Package Manager Manual

Installing the Software

You must be an Administrator to install NI software on your computer.

1. Install an ADE, such as LabVIEW or LabWindows™/CVI™.
2. Download the driver software installer from [ni.com/downloads](https://www.ni.com/en-us/support/downloads.html). 
 Package Manager downloads with the driver software to handle the
 installation. Refer to the [Package Manager Manual](http://ni.com/r/nipmmanual) for more
 information about installing, removing, and upgrading NI software using Package Manager.
3. Follow the instructions in the installation prompts. 
 org.dita.html5/xsl/topic.xsl 455Note Windows users may see access and security messages during installation. Accept the prompts to complete the installation.
4. When the installer completes, select 
 Restart in the dialog box that prompts you to restart, shut down, or restart later.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=ni-pxi-pxie-gsg-purpose.html language=enus -->
## TOPIC 00006: Getting Started with Express Switches

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `ni-pxi-pxie-gsg-purpose.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/ni-pxi-pxie-gsg-purpose.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: This document explains how to install, configure, and test NI PXI/PXI Express Switches. The switch ships with the NI-SWITCH instrument driver, which you can use to program the device. Before you begin, install and configure your chassis and controller.

Getting Started with Express Switches

This document explains how to install, configure, and test NI PXI/PXI Express Switches. The switch ships with the NI-SWITCH instrument driver, which you can use to program the device.

Note

Before you begin, install and configure your chassis and controller.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=preparing-the-environment.html language=enus -->
## TOPIC 00007: Preparing the Environment

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `preparing-the-environment.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/preparing-the-environment.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ensure that the environment in which you are using the NI PXI/PXI Express Switch meets the following specifications. PXI Express Modules Operating Environment Ambient temperature range 0 °C to 40 °C Relative humidity range 10% to 90%, noncondensing Maximum altitude 2,000 m (800 mbar) (at 25 °C ambie

Preparing the Environment

Ensure that the environment in which you are using the NI PXI/PXI Express Switch meets the following specifications.

#### PXI Express Modules

| Operating Environment Ambient temperature range 0 °C to 40 °C Relative humidity range 10% to 90%, noncondensing |  |
| --- | --- |
| Operating Environment |  |
| Ambient temperature range | 0 °C to 40 °C |
| Relative humidity range | 10% to 90%, noncondensing |
| Maximum altitude | 2,000 m (800 mbar) (at 25 °C ambient temperature) |
| Pollution Degree | 2 |

Indoor use only.

#### PXI Modules

| Operating Environment Ambient temperature range 0 °C to 55 °C Relative humidity range 10% to 90%, noncondensing |  |
| --- | --- |
| Operating Environment |  |
| Ambient temperature range | 0 °C to 55 °C |
| Relative humidity range | 10% to 90%, noncondensing |

| Maximum altitude | 2,000 m (at 25 °C ambient temperature) |
| --- | --- |
| Pollution degree | 2 |
| Indoor use only |  |

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=program-device-switch.html language=enus -->
## TOPIC 00008: Programming the NI PXI/PXI Express Switch

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `program-device-switch.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/program-device-switch.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can acquire data interactively using the NI-SWITCH Soft Front Panel (SFP), or you can control the device programmatically using the NI-SWITCH instrument driver. You can then use NI-SWITCH to program the device in the application development environment (ADE) of your choice. NI PXI/PXI Express Sw

Programming the NI PXI/PXI Express Switch

You can acquire data interactively using the NI-SWITCH Soft Front Panel (SFP), or you can control the device programmatically using the NI-SWITCH instrument driver. You can then use NI-SWITCH to program the device in the application development environment (ADE) of your choice.

| Application Programming Interface (API) | Location | Description |
| --- | --- | --- |
| NI-SWITCH SFP | Available from the Start menu or NI Launcher in Windows 8. | Provides a graphical interface for controlling and viewing the state of your NI PXI/PXI Express Switch. |
| NI-SWITCH Instrument Driver | LabVIEW—Available on the LabVIEW Functions palette at Measurement I/O » NI-SWITCH. | Features a set of operations and attributes that exercise all the functionality of the NI PXI/PXI Express Switch, including configuration, control, and other device-specific functions. |
| C or LabWindows/CVI—Available at Program Files\\IVI Foundation\\IVI\\Drivers\\niSWITCH. |  |  |
| Installed examples for Visual C/C++ are in the NI-SWITCH Readme. | Refer to the Creating an Application with Microsoft Visual C/C++ topic in the NI Switches Help for information about developing an NI-SWITCH application. |  |

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=troubleshooting.html language=enus -->
## TOPIC 00009: Troubleshooting

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/troubleshooting.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: If an issue persists after you complete a troubleshooting procedure, search our KnowledgeBase for additional information our technical support engineers create as they answer common user questions and resolve unexpected issues. What Should I Do if the NI PXI/PXI Express Switch Does Not Appear in MAX

Troubleshooting

If an issue persists after you complete a troubleshooting procedure, search our KnowledgeBase for additional information our technical support engineers create as they answer common user questions and resolve unexpected issues.

#### What Should I Do if the NI PXI/PXI Express Switch Does Not Appear in MAX?

1. In the MAX configuration tree, expand Devices and Interfaces .
2. Expand the Chassis tree to see the list of installed hardware,
 and press <F5> to refresh the list.
3. If the module is still not listed, power off the system, ensure that all hardware is
 correctly installed, and restart the system.
4. Navigate to the Device Manager by right-clicking the Start button, and selecting
 Device Manager .
5. Verify the NI PXI/PXI Express Switch appears in the Device Manager.
  1. Under an NI entry, confirm that a NI PXI/PXI Express Switch entry
 appears. org.dita.html5/xsl/topic.xsl 455 Note If you are using a PC with a device for PXI remote control system,
 under System Devices, also confirm that no error conditions
 appear for the PCI-to-PCI Bridge.
  2. If error conditions appear, reinstall NI-SWITCH .

#### What Should I Do if the NI PXI/PXI Express Switch Fails the Self-Test?

1. Reset the NI PXI/PXI Express Switch through Hardware Configuration
 Utility or MAX and then perform the self-test again.
2. Restart the system, and then perform the self-test again.
3. Power off the chassis.
4. Reinstall the failed module in a different slot.
5. Power on the chassis.
6. Perform the self-test again. 
 org.dita.html5/xsl/topic.xsl 455Note If the module fails the self-test
 again, contact NI or visit [ni.com/support](http://www.ni.com/support) for further troubleshooting information.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=unpacking.html language=enus -->
## TOPIC 00010: Unpacking the Kit

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `unpacking.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/unpacking.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: To prevent electrostatic discharge (ESD) from damaging the device, ground yourself using a grounding strap or by holding a grounded object, such as your computer chassis. Touch the antistatic package to a metal part of the computer chassis. Remove the device from the package and inspect the device f

Unpacking the Kit

Notice

1. Touch the antistatic package to a metal part of the computer chassis.
2. Remove the device from the package and inspect the device for loose components or any other sign of damage. 
 org.dita.html5/xsl/topic.xsl 455Notice Never touch the exposed pins of connectors.
 org.dita.html5/xsl/topic.xsl 455Note Do not install a device if it appears damaged in any way.
3. Unpack any other items and documentation from the kit.

Note

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=verify-kit-contents-pxi.html language=enus -->
## TOPIC 00011: Verifying the Kit Contents

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `verify-kit-contents-pxi.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/verify-kit-contents-pxi.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The items shown in the following figure are necessary to set up and use your device. Kit Contents NI PXI/PXI Express Switch NI-SWITCH Driver Software DVD NI PXI/PXI Express Switches Getting Started Guide Safety, Environmental, and Regulatory Information In addition to the items contained in the kit,

Verifying the Kit Contents

The items shown in the following figure are necessary to set up and use your device.

Figure 1.

[IMAGE alt='1378' src='GUID-C78FC79A-289E-41E1-A3DD-53EB5F9D878C-a5.svg']

1. NI PXI/PXI Express Switch
2. NI-SWITCH Driver Software DVD
3. NI PXI/PXI Express Switches Getting Started Guide
4. Safety, Environmental, and Regulatory Information

In addition to the items contained in the kit, you need the following items to install or operate your device.

#### NI PXI/PXI Express Switch Required Items

- NI PXI chassis, NI PXI Express chassis, or NI PXI/SCXI combination chassis
- 1/8 in. flathead screwdriver or #1 Phillips screwdriver

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=verify-max.html language=enus -->
## TOPIC 00012: Verifying the Installation in MAX

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `verify-max.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/verify-max.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use Measurement & Automation Explorer (MAX) to configure your NI hardware. MAX informs other programs about which NI hardware products are in the system and how they are configured. MAX is automatically installed with NI-SWITCH. MAX is not available on Linux. Launch MAX. In the configuration

Verifying the Installation in MAX

You can use Measurement & Automation Explorer (MAX) to configure your NI
 hardware. MAX informs other programs about which NI hardware products are in the system and
 how they are configured. MAX is automatically installed with NI-SWITCH.

Note

1. Launch MAX.
2. In the configuration tree, expand Devices and
 Interfaces to see the list of installed NI hardware. 
 Installed modules appear under the name of their associated
 chassis.
3. Expand your Chassis tree item. 
 MAX lists all modules installed in the chassis. Your default names may vary. org.dita.html5/xsl/topic.xsl 455Note If you do not see your module listed,
 press <F5> to refresh the list of installed modules. If the module is still not
 listed, power off the system, ensure the module is correctly installed, and restart.
4. Record the name MAX assigns to the hardware. Use this identifier when
 programming the NI PXI/PXI Express Switch.
5. Self-test the hardware by selecting the item in the configuration tree
 and clicking Self-Test in the MAX toolbar. 
 MAX self-test performs a basic verification of hardware resources.

<!--NI_TOPIC bundle=pxi-pxie-express-switches-getting-started path=verify-system-requirements-switch.html language=enus -->
## TOPIC 00013: Verifying the System Requirements

- bundle_id: `pxi-pxie-express-switches-getting-started`
- source_path: `verify-system-requirements-switch.html`
- source_url: https://docs-be.ni.com/bundle/pxi-pxie-express-switches-getting-started/raw/resource/enus/verify-system-requirements-switch.html
- document_id: `pxi-pxie-express-switches-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use the NI-SWITCH driver, your system must meet certain requirements. For more information about minimum system requirements, recommended system, and supported application development environments (ADEs), refer to the readme, which is available on the software media or online at ni.com/updates.

Verifying the System Requirements

To use the NI-SWITCH driver, your system must meet certain requirements. For more information about minimum system requirements, recommended system, and supported application development environments (ADEs), refer to the readme, which is available on the software media or online at 
 [ni.com/updates](http://www.ni.com/updates).
