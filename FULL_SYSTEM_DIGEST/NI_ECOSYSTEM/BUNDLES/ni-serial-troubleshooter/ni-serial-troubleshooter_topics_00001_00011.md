# NI DOCUMENT BUNDLE: ni-serial-troubleshooter

<!--NI_BUNDLE_CHUNK bundle=ni-serial-troubleshooter start=1 end=11 -->
<!--NI_TOPIC bundle=ni-serial-troubleshooter path=address-resource-conflict.html language=enus -->
## TOPIC 00001: Address Resource Conflict

- bundle_id: `ni-serial-troubleshooter`
- source_path: `address-resource-conflict.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/address-resource-conflict.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: This error occurs if the address resources assigned to a serial interface conflict with the address resources being used by other devices in the system.Typically, resource conflicts occur when your system contains hardware that is configured to use the same resources as your serial interface. Resour

### Address Resource Conflict

This error occurs if the address resources assigned to a serial interface conflict with the
 address resources being used by other devices in the system.

Typically, resource conflicts occur when your system contains hardware that is configured to use
 the same resources as your serial interface. Resource conflicts are detected by
 NI-Serial when the driver is loaded. If there is a resource conflict, the driver fails
 to load and records an error in the *Event Viewer* describing why it failed
 to load.

*Determine the resource* that caused the conflict and select new resources that are
 not in conflict.

Use the *Windows System Information tool* to get a list of the resource usage that is
 known to the operating system. This utility displays a list of I/O addresses and
 interrupt levels that are currently in use.

Once you know what resources are in conflict, run the Windows Device Manager utility to configure
 the new conflict-free resources.

Related concepts:

- Event Viewer
- Determining Resource Conflicts
- Windows System Information Tool

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=determining-resource-conflicts.html language=enus -->
## TOPIC 00002: Determining Resource Conflicts

- bundle_id: `ni-serial-troubleshooter`
- source_path: `determining-resource-conflicts.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/determining-resource-conflicts.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Windows Device Manager to determine which resources have a conflict. Launch Device Manager. Select the device that has the resource conflict and click the Properties button. A yellow exclamation point (!) indicates the device with the resource conflict. Select the Resources tab and click the

### Determining Resource Conflicts

Use the Windows Device Manager to determine which resources have a conflict.

1. Launch Device Manager.
2. Select the device that has the resource conflict and click the Properties button. A yellow exclamation point ( ! ) indicates the device with the resource conflict.
3. Select the Resources tab and click the Set Configuration Manually button.
4. View the conflicting resource information to determine which resource conflicts with which device.
5. Click OK when you are finished.
6. In the System Settings Change dialog, click Yes to restart the computer or No if you want to restart the computer later.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=event-viewer.html language=enus -->
## TOPIC 00003: Event Viewer

- bundle_id: `ni-serial-troubleshooter`
- source_path: `event-viewer.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/event-viewer.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Event Viewer is used to maintain a system log. If the NI-Serial driver fails to start properly, it records entries in the system log that explain why it failed to start.Follow these steps to use the Event Viewer: Open Event Viewer. From the left window pane, select the appropriate log: For Windo

### Event Viewer

The Event Viewer is used to maintain a system log. If the NI-Serial driver fails to start
 properly, it records entries in the system log that explain why it failed to start.

Follow these steps to use the Event Viewer:

1. Open Event Viewer.
2. From the left window pane, select the appropriate log:
  - For Windows XP, select System .
  - For all other versions of Windows, expand the Windows Logs folder and select System .
3. Using the View menu and the column headings, show all logs and sort so that the newest logs are shown first.
4. Begin examining the event details from the top of the list. To view event details, double-click on the event.
5. The events of interest are those with the word niser in the Source column. You are looking for serial-related events that mention a resource conflict. You can ignore all other serial-related events.
6. Note the very first resource conflict encountered. You need to know the type of resource conflict, for example, I/O address or IRQ. You also need to know which board the conflict is for.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=interrupt-resource-conflict.html language=enus -->
## TOPIC 00004: Interrupt Resource Conflict

- bundle_id: `ni-serial-troubleshooter`
- source_path: `interrupt-resource-conflict.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/interrupt-resource-conflict.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: This error occurs if the interrupt resource assigned to a serial interface conflicts with the interrupt resource being used by another device in the system.Typically, resource conflicts occur when your system contains hardware that is configured to use the same resources as your serial interface. Re

### Interrupt Resource Conflict

This error occurs if the interrupt resource assigned to a serial interface conflicts with the
 interrupt resource being used by another device in the system.

Typically, resource conflicts occur when your system contains hardware that is configured to use
 the same resources as your serial interface. Resource conflicts are detected by
 NI-Serial when the driver is loaded. If there is a resource conflict, the driver fails
 to load and records an error in the *Event Viewer* describing why it failed
 to load.

*Determine the resource* that caused the conflict and select new resources that are
 not in conflict.

Use the *Windows System Information tool* to get a list of the resource usage that is
 known to the operating system. This utility displays a list of I/O addresses and
 interrupt levels that are currently in use.

Once you know what resources are in conflict, run the Windows Device Manager utility to configure
 the new conflict-free resources.

Related concepts:

- Event Viewer
- Determining Resource Conflicts
- Windows System Information Tool

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=one-or-more-missing-serial-interfaces.html language=enus -->
## TOPIC 00005: One or More Missing Serial Interfaces

- bundle_id: `ni-serial-troubleshooter`
- source_path: `one-or-more-missing-serial-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/one-or-more-missing-serial-interfaces.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Serial did not recognize every serial interface. There are several reasons why you might encounter this problem: The serial interface is not properly installedRefer to the Serial Hardware and Software Help to verify that your serial interface is correctly installed. Rerun the NI-Serial Troublesho

### One or More Missing Serial Interfaces

NI-Serial did not recognize every serial interface. There are several reasons why you might
 encounter this problem:

#### The serial interface is not properly
 installed

Refer to the Serial Hardware and Software
 Help to verify that your serial interface is correctly installed.
 Rerun the NI-Serial Troubleshooter.

#### You ran the Troubleshooter before the Add New
 Hardware Wizard completed the task of adding the Plug-and-Play interface to your
 system.

Follow the steps in the Add New Hardware Wizard to finish adding
 the hardware to your system before you run the Troubleshooter. If you canceled the
 Add New Hardware Wizard before it completed, reboot your system and make sure the
 Add New Hardware Wizard completes before continuing with the
 Troubleshooter.

#### Serial USB interface not detected

The USB
 host controller must be working properly to use the serial interface. Refer to the
 Device Manager to verify that the host controller is functioning properly. If you
 select View devices by type, you can review the USB Host
 Controller properties to ensure it is correctly enabled and
 functioning.

#### Serial interface has been removed from the
 system

You have removed the serial interface from the system. Click on the
 link below to launch the Device Manager. Right-click on your computer's name in the
 list and select Scan for hardware changes. You may also
 reboot your computer to allow the operating system to detect and install your serial
 interface.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=overview.html language=enus -->
## TOPIC 00006: NI-Serial Troubleshooter Overview

- bundle_id: `ni-serial-troubleshooter`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/overview.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Serial Troubleshooter is used to verify installation and troubleshoot issues. The NI-Serial Troubleshooter supports ports only on your local Windows system. It does not test your LabVIEW Real-Time serial ports.

### NI-Serial Troubleshooter
 Overview

NI-Serial Troubleshooter is used to verify installation and troubleshoot issues. The
 NI-Serial Troubleshooter supports ports only on your local Windows system. It does not
 test your LabVIEW Real-Time serial ports.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=unable-to-open-port.html language=enus -->
## TOPIC 00007: Unable to Open Port

- bundle_id: `ni-serial-troubleshooter`
- source_path: `unable-to-open-port.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/unable-to-open-port.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Serial was unable to open this port. Possible causes for this problem are listed below: The port is already openYou must close all open ports to run this test successfully. Close all serial applications and click Retest to rerun the NI-Serial Troubleshooter. The port is disabled in the Device Man

### Unable to Open Port

NI-Serial was unable to open this port. Possible causes for this problem are listed below:

#### The port is already open

You must close
 all open ports to run this test successfully. Close all serial applications and
 click Retest to rerun the NI-Serial
 Troubleshooter.

#### The port is disabled in the Device
 Manager

All NI Serial ports must be enabled to run this test successfully.
 Refer to the Device Manager to verify that all ports are enabled.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=unknown-hardware-error.html language=enus -->
## TOPIC 00008: Unknown Hardware Error

- bundle_id: `ni-serial-troubleshooter`
- source_path: `unknown-hardware-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/unknown-hardware-error.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: An unknown serial hardware error has been encountered. The basic problem is that your hardware is not being correctly recognized by the system. Several of the possible causes for this problem are listed below: The NI-Serial driver for your serial interface failed to load correctly due to a resource

### Unknown Hardware Error

An unknown serial hardware error has been encountered. The basic problem is that your hardware is
 not being correctly recognized by the system. Several of the possible causes for this
 problem are listed below: The NI-Serial driver for your serial interface failed to load
 correctly due to a resource conflict.

Typically, resource conflicts occur when your system contains hardware that is configured to use
 the same resources as your serial interface. Resource conflicts are detected by
 NI-Serial when the driver is loaded. If there is a resource conflict, the driver fails
 to load and records an error in the *Event Viewer* describing why it failed
 to load.

*Determine the resource* that caused the conflict and select new resources that are
 not in conflict.

Use the *Windows System Information tool* to get a list of the resource usage that is
 known to the operating system. This utility displays a list of I/O addresses and
 interrupt levels that are currently in use.

Once you know what resources are in conflict, run the Windows Device Manager utility to configure
 the new conflict-free resources. Your serial interface is incorrectly installed or
 configured.

Verify that your serial interface is correctly installed and configured. For information about the installation and configuration of your serial hardware, refer to the Serial Hardware and Software Help.
Your serial interface appears to be installed correctly and working properly, but the NI-Serial Troubleshooter still reports this error.

Try restarting your computer and rerunning the NI-Serial Troubleshooter. If problems persist, contact NI for more help.

Related concepts:

- Event Viewer
- Determining Resource Conflicts
- Windows System Information Tool

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=unknown-ni-serial-software-error.html language=enus -->
## TOPIC 00009: Unknown NI-Serial Software Error

- bundle_id: `ni-serial-troubleshooter`
- source_path: `unknown-ni-serial-software-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/unknown-ni-serial-software-error.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: An unknown NI-Serial software problem has occurred. Please try the following to resolve the problem before calling NI: Restart your system. Run the NI-Serial Troubleshooter again. If you still have the problem, try the following: Use the NI-Serial installer to repair your version of the NI-Serial so

### Unknown NI-Serial Software Error

An unknown NI-Serial software problem has occurred. Please try the following to resolve the
 problem before calling NI:

1. Restart your system.
2. Run the NI-Serial Troubleshooter again.

If you still have the problem, try the following:

1. Use the NI-Serial installer to repair your version of the NI-Serial software for Windows.
2. Restart your system.
3. Run the NI-Serial Troubleshooter again.

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=user-manual-welcome.html language=enus -->
## TOPIC 00010: NI-Serial Troubleshooter User Manual

- bundle_id: `ni-serial-troubleshooter`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Serial Troubleshooter User Manual provides detailed descriptions of the product functionality and the step-by-step processes for use. Looking For Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-Serial Troubleshooter
 User Manual

The NI-Serial Troubleshooter User Manual provides detailed
 descriptions of the product functionality and the step-by-step processes for use.

#### Looking For Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ni-serial-troubleshooter path=windows-system-information-tool.html language=enus -->
## TOPIC 00011: Windows System Information Tool

- bundle_id: `ni-serial-troubleshooter`
- source_path: `windows-system-information-tool.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial-troubleshooter/raw/resource/enus/windows-system-information-tool.html
- document_id: `ni-serial-troubleshooter`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Windows System Information tool collects and displays your system configuration information. Use this tool to determine which resources in the system are currently in use. The information provided by this utility is a useful guide for selecting conflict-free resources.Follow these steps to use i

### Windows System Information Tool

The Windows System Information tool collects and displays your system configuration information.
 Use this tool to determine which resources in the system are currently in use. The
 information provided by this utility is a useful guide for selecting conflict-free
 resources.

Follow these steps to use it:

1. Access the System Information tool.
2. Expand Hardware Resources by clicking the + from the left window pane.
3. Use the IRQs and I/O folders to view in-use resources.
4. When you are finished, click the x in the top right corner to exit the
 System Information utility.

Use System Information to find free resources. For example, if you are experiencing an interrupt
 resource conflict, view the IRQ resources that are being used and determine which are
 available. Note an available IRQ resource and then use the Windows Device Manager
 utility to configure NI-Serial to use that available IRQ resource for the serial
 interface.
