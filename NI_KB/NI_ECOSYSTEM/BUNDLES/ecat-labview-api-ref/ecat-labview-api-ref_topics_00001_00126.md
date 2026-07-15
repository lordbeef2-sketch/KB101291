# NI DOCUMENT BUNDLE: ecat-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ecat-labview-api-ref start=1 end=126 -->
<!--NI_TOPIC bundle=ecat-labview-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-EtherCAT LabVIEW API Reference

- bundle_id: `ecat-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/api-reference.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-EtherCAT LabVIEW API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ecatadvdcproppage.html language=enus -->
## TOPIC 00002: EtherCAT:Adv:Distributed Clock Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ecatadvdcproppage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ecatadvdcproppage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the EtherCAT Distributed Clock configuration parameters. The distributed clock can enable all the slave devices to have the same time. The first slave device with the distributed clock enabled is the clock master. The clock of the clock master synchronizes the clocks in other slave d

### EtherCAT:Adv:Distributed Clock Property Page

This page shows the EtherCAT Distributed Clock configuration parameters. The distributed clock can enable all the slave devices to have the same time. The first slave device with the distributed clock enabled is the clock master. The clock of the clock master synchronizes the clocks in other slave devices and master.

This page includes the following component:

- Additional correction for synchronized IO (microseconds) —specifies an additional correction to ensure that all slave devices receive their process data.

The following figure describes the distributed clock-related properties.

[IMAGE alt='image' src='images/distributedclock.gif']

Parent topic:

EtherCAT Master Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-lvprojectitem.html language=enus -->
## TOPIC 00003: LabVIEW Project Items

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-lvprojectitem.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-lvprojectitem.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Project Explorer window includes the following items: Project root—Contains all other items in the Project Explorer window. Real-Time target—A supported real-time controller can contain the following EtherCAT items: EtherCAT master—One real-time controller usually has one master using th

### LabVIEW Project Items

The LabVIEW Project Explorer window includes the following items:

- Project root —Contains all other items in the Project Explorer window.
- Real-Time target —A supported real-time controller can contain the following EtherCAT items:
  - EtherCAT master —One real-time controller usually has one master using the special Ethernet adapter for the EtherCAT network.
  - EtherCAT slave device —An EtherCAT slave device from NI or a third-party vendor.
  - EtherCAT module —A flexible EtherCAT slave device can have several modules.
  - I/O Variable —The physical channels of the slave device and module are mapped to the I/O variables. A slave device or module can have several I/O variables.
  - FPGA Target —You need an FPGA target to program the FPGA of the NI 9145. Drag and drop the modules between the NI 9145 item and the FPGA target item to switch between Scan Mode and FPGA Mode.
  - User-Defined Variable —User-defined variables transfer custom FPGA-processed data between an FPGA VI and an RT VI.

Note

NI-Industrial Communications for EtherCAT Readme

[IMAGE alt='image' src='images/getstarted_addmasterresult.gif']

Note

Project root

- A real-Time controller
- An EtherCAT master device
- EtherCAT slave devices
- An EtherCAT module

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-masterpropertydialog.html language=enus -->
## TOPIC 00004: EtherCAT Master Properties Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-masterpropertydialog.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-masterpropertydialog.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit an EtherCAT master property, right-click the EtherCAT master item and select Properties to display the EtherCAT Master Properties dialog box. The EtherCAT Master Properties dialog box includes the following pages. General EtherCAT:Basic EtherCAT:Advanced:Distributed Clock

### EtherCAT Master Properties Dialog Box

To edit an EtherCAT master property, right-click the [EtherCAT master item](environment-lvprojectitem.html) and select Properties to display the EtherCAT Master Properties dialog box.

The EtherCAT Master Properties dialog box includes the following pages.

- General
- EtherCAT:Basic
- EtherCAT:Advanced:Distributed Clock

- [General Property Page Master](generalpropertypagemaster.html)
- [EtherCAT:Basic Property Page Master](ethercatbasicpropertypagemaster.html)
- [EtherCAT:Adv:Distributed Clock Property Page](ecatadvdcproppage.html)

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-menu.html language=enus -->
## TOPIC 00005: LabVIEW Project Item Menus

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-menu.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-menu.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you right-click an EtherCAT project item, you can see the following item context menus: Project root item menu: New»Targets and Devices—Displays the Add Targets and Devices dialog box to add a real-time target. Real-time target item menu: New»Targets and Devices—Displays the Add Targets and Dev

### LabVIEW Project Item Menus

When you right-click an EtherCAT project item, you can see the following item context menus:

- Project root item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add a real-time target.

- Real-time target item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add an EtherCAT master.

- EtherCAT master item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add an EtherCAT slave device.
  - Utilities»Import Device Profiles — Imports one or more device profile XML files.
  - Deploy —Deploys the item configuration to the target controller.
  - Undeploy —Removes the item configuration from the target controller.
  - Online Master State —Displays the Online Master State dialog box.
  - Remove from Project —Removes the item from the project.
  - Rename —Renames the item.
  - Help —Displays this help file.
  - Properties —Displays the EtherCAT Master Properties dialog box.

- EtherCAT slave device item menu:
  - New»Targets and Devices —Displays the Add Targets and Devices dialog box to add an EtherCAT slave device or module attached to the slave device item.
  - New»FPGA Target —Creates an FPGA target item under the NI 9145 item if the FPGA target does not exist. Refer to the NI-Industrial Communications for EtherCAT Readme for requirements on using the FPGA features of the NI 9145.
  - New»User-Defined Variable —Displays the Shared Variable Properties dialog box to add a user-defined variable to the NI 9145 item. Add an FPGA target before adding a user-defined variable.
  - Online Device State —Displays the Online Device State dialog box.
  - Remove from Project —Removes the item from the project.
  - Rename —Renames the item.
  - Help —Displays this help file.
  - Properties —Displays the EtherCAT Slave Device Properties dialog box.

- EtherCAT module item menu:
  - Remove from Project —Removes the item from the project.
  - Rename —Renames the item.
  - Help —Displays the module help file.
  - Properties —Displays the C Series Module Properties dialog box.

- I/O variable item menu:
  - Properties —Displays the I/O Variable Properties dialog box.

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-onlinemasterpanel.html language=enus -->
## TOPIC 00006: Online Master State Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-onlinemasterpanel.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-onlinemasterpanel.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the EtherCAT master item and select Online Master State from the shortcut menu to display this dialog box. If the Online Master State menu item is disabled, check the following items: Ensure the target controller is connected. Ensure the target item in the project has the correct IP addr

### Online Master State Dialog Box

Right-click the 
 [EtherCAT master item](environment-lvprojectitem.html) and select 
 Online Master State from the shortcut menu to display this dialog box.

If the 
 Online Master State menu item is disabled, check the following items:

- Ensure the target controller is connected.
- Ensure the target item in the project has the correct IP address.
- Ensure the EtherCAT master item has the correct adapter. You can change the physical adapter on the 
 General page of the 
 EtherCAT Master Properties dialog box.

As with the 
 OK button, the 
 Cancel button does not revert your changes in this dialog box.

This dialog box includes the following component:

- Slave device state list —Displays the slave device state. The table includes the following columns:
  - Address —Displays the slave device position address.
  - Slave Device Name —Displays the slave device name.
  - State —Displays the slave device state.
  - Error —Indicates whether an error has occurred in the slave device.

You can also 
 [leverage](/csh?context=niecat_indcomecat_relationshipbetweenethercatandscanengine) the NI Scan Engine, 
 [change](/csh?context=niecat_indcomecat_ethercatslavetransition) to the slave device state, or 
 [change](/csh?context=niecat_indcomecat_scanenginemodetransition) the NI Scan Engine mode.

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-onlineslavepanel-parameter.html language=enus -->
## TOPIC 00007: EtherCAT:Parameters Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-onlineslavepanel-parameter.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-onlineslavepanel-parameter.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the slave device parameter information. All parameters are updated from the online slave device. The parameters are read only. The Object Dictionary table includes the following columns: Index—The parameter index. SubIndex—The parameter subindex. Name—The parameter name. Data Type—Th

### EtherCAT:Parameters Page

This page shows the slave device parameter information. All parameters are updated from the online slave device. The parameters are read only.

The 
 Object Dictionary table includes the following columns:

- Index —The parameter index.
- SubIndex —The parameter subindex.
- Name —The parameter name.
- Data Type —The parameter data type.
- Value —The parameter value in the slave device.

Parent topic:

Online Device State Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-onlineslavepanel-state.html language=enus -->
## TOPIC 00008: EtherCAT:Online:State Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-onlineslavepanel-state.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-onlineslavepanel-state.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the EtherCAT slave device online state. This page includes the following components: Device State—Displays the state of the slave device. The current slave device state LED is on (light green). You can change the slave device state by clicking the corresponding button. Device Error—D

### EtherCAT:Online:State Page

This page shows the EtherCAT slave device online state. This page includes the following components:

- Device State —Displays the state of the slave device. The current slave device state LED is on (light green). You can change the slave device state by clicking the corresponding button.
- Device Error —Displays the slave device error information.
  - Error LED —If the slave device has no error in the last configuration, the LED is off (dark red). Otherwise, the LED is on (light red). Click the 
 Explain Error button to see the error happening in the last slave device configuration.
  - Clear Error —Clears the error.
- Download Firmware —Downloads the firmware to the slave device.

If the slave device is disconnected, all state LEDs are off in dark green.

You can also 
 [leverage](/csh?context=niecat_indcomecat_relationshipbetweenethercatandscanengine) the NI Scan Engine, 
 [change](/csh?context=niecat_indcomecat_ethercatslavetransition) to the slave device state, or 
 [change](/csh?context=niecat_indcomecat_scanenginemodetransition) the NI Scan Engine mode.

Parent topic:

Online Device State Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-onlineslavepanel.html language=enus -->
## TOPIC 00009: Online Device State Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-onlineslavepanel.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-onlineslavepanel.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the EtherCAT slave device item and select Online Device State to display the Online Device State dialog box. If the Online Device State menu is disabled, check the following items: Be sure the target controller and slave device are connected. Be sure the target item in the project is a

### Online Device State Dialog Box

EtherCAT slave device item

Online Device State

Online Device State

Note

Online Device State

- Be sure the target controller and slave device are connected.
- Be sure the target item in the project is assigned the correct IP address.
- Be sure the EtherCAT master item is assigned the correct adapter. You can change the physical adapter on the General page of the EtherCAT Master Properties dialog box.
- Be sure you have deployed the master settings by right-clicking the master item and selecting the Deploy menu.

Note

OK

Cancel

The dialog box includes the following pages:

- EtherCAT:Online:State
- EtherCAT:Parameters

- [EtherCAT:Online:State Page](environment-onlineslavepanel-state.html)
- [EtherCAT:Parameters Page](environment-onlineslavepanel-parameter.html)

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-riomodulepropertydialog.html language=enus -->
## TOPIC 00010: C Series Module Properties Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-riomodulepropertydialog.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-riomodulepropertydialog.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit an EtherCAT module property, right-click the EtherCAT module item and select Properties to display the C Series Module Properties dialog box. Click Help on the dialog box for more information. Unlike the module on the local cRIO controller, the C Series Module Properties dialog box does no

### C Series Module Properties Dialog Box

To edit an EtherCAT module property, right-click the [EtherCAT module item](environment-lvprojectitem.html) and select Properties to display the C Series Module Properties dialog box.

Help

Note

C Series Module Properties

Specialty Digital Configuration

Note

C Series Module Properties

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-slavedevicepropertydialog.html language=enus -->
## TOPIC 00011: EtherCAT Slave Device Properties Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-slavedevicepropertydialog.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-slavedevicepropertydialog.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit an EtherCAT slave device property, right-click the EtherCAT slave device item and select Properties to display the EtherCAT Slave Device Properties dialog box. The EtherCAT Slave Device Properties dialog box includes the following pages: General EtherCAT:Basic EtherCAT:Advanced:Mailbox Ether

### EtherCAT Slave Device Properties Dialog Box

To edit an EtherCAT slave device property, right-click the [EtherCAT slave device item](environment-lvprojectitem.html) and select Properties to display the EtherCAT Slave Device Properties dialog box.

The EtherCAT Slave Device Properties dialog box includes the following pages:

- General
- EtherCAT:Basic
- EtherCAT:Advanced:Mailbox
- EtherCAT:Advanced:Watch Dog
- EtherCAT:Advanced:Distributed Clock
- EtherCAT:Advanced:Initial Commands

- [General Property Page](generalpropertypageslave.html)
- [EtherCAT:Basic Property Page](ethercatbasicpropertypage.html)
- [EtherCAT:Advanced:Mailbox Property Page](ethercatadvancedmailboxpropertypage.html)
- [EtherCAT:Advanced:Watchdog Property Page](ethercatadvancedwatchdogpropertypage.html)
- [EtherCAT:Advanced:Distributed Clock Property Page](ethercatadvanceddistributedclockpropertypage.html)
- [EtherCAT:Advanced:Initial Commands Property Page](ethercatadvancedinitcmdpropertypage.html)

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-summary.html language=enus -->
## TOPIC 00012: NI-Industrial Communications for EtherCAT Environment

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-summary.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-summary.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can see the following EtherCAT items in the LabVIEW Project Explorer window. LabVIEW Project Items and Menus EtherCAT Master Properties Dialog Box EtherCAT Slave Device Properties Dialog Box C Series Module Properties Dialog Box I/O Variable Properties Dialog Box Online Master State Dialog Box O

### NI-Industrial Communications for EtherCAT Environment

You can see the following EtherCAT items in the LabVIEW Project Explorer window.

- LabVIEW Project Items and Menus
- EtherCAT Master Properties Dialog Box
- EtherCAT Slave Device Properties Dialog Box
- C Series Module Properties Dialog Box
- I/O Variable Properties Dialog Box
- Online Master State Dialog Box
- Online Device State Dialog Box

- [LabVIEW Project Items](environment-lvprojectitem.html)
- [LabVIEW Project Item Menus](environment-menu.html)
- [EtherCAT Master Properties Dialog Box](environment-masterpropertydialog.html)
- [EtherCAT Slave Device Properties Dialog Box](environment-slavedevicepropertydialog.html)
- [Third-Party EtherCAT Module Properties Dialog Box](third-party-ethercat-module-prop-dialog.html)
- [C Series Module Properties Dialog Box](environment-riomodulepropertydialog.html)
- [I/O Variable Properties Dialog Box](environment-variablepropertydialog.html)
- [Online Master State Dialog Box](environment-onlinemasterpanel.html)
- [Online Device State Dialog Box](environment-onlineslavepanel.html)
- [Import Device Profile Dialog Box](importdeviceprofile.html)

<!--NI_TOPIC bundle=ecat-labview-api-ref path=environment-variablepropertydialog.html language=enus -->
## TOPIC 00013: I/O Variable Properties Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `environment-variablepropertydialog.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/environment-variablepropertydialog.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit an I/O variable property, right-click the I/O variable and select Properties to display the Shared Variable Properties dialog box. Click Help on the dialog box for more information.

### I/O Variable Properties Dialog Box

To edit an I/O variable property, right-click the [I/O variable](environment-lvprojectitem.html) and select Properties to display the Shared Variable Properties dialog box.

Click Help on the dialog box for more information.

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatadvanceddistributedclockpropertypage.html language=enus -->
## TOPIC 00014: EtherCAT:Advanced:Distributed Clock Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatadvanceddistributedclockpropertypage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatadvanceddistributedclockpropertypage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the slave device EtherCAT-specific distributed clock properties. The distributed clock can enable all the slave devices to have the same time. The first slave device with the distributed clock enabled is the clock master. The clock of the clock master synchronizes the clocks in the o

### EtherCAT:Advanced:Distributed Clock Property Page

This page shows the slave device EtherCAT-specific distributed clock properties. The distributed clock can enable all the slave devices to have the same time. The first slave device with the distributed clock enabled is the clock master. The clock of the clock master synchronizes the clocks in the other slave devices and master.

This page includes the following components:

- Enable distributed clock —Specifies whether to enable the distributed clock.
- Synchronization Signal (SYNC0) Interval —Specifies the interval of SYNC0. The distributed clock synchronization signal is SYNC0. A device usually processes the data at SYNC0.
  - Cycle Time (scan periods) —Specifies the SYNC0 cycle time.
  - Shift Time (microseconds) —Specifies the SYNC0 shift time within a synchronization interval.
- Auxiliary Synchronization Signal (SYNC1) Interval —Specifies the SYNC1 interval. The auxiliary synchronization signal is SYNC1. A slave device can process the additional data at SYNC1.
  - Enable SYNC1 —Specifies whether to enable SYNC1.
  - Cycle Time (SYNC0 cycles) —Specifies the SYNC1 cycle time.
- Synchronize Input and Output —Specifies settings to synchronize the input and output with the distributed clock. The NI EtherCAT slave devices implement the simultaneous sampling with these settings enabled.
  - Synchronize Input Mode —Specifies the mode to synchronize the input with the distributed clock.
    - Unsynchronized —No synchronization.
    - Synchronized to EtherCAT frame —Synchronize the input to the EtherCAT frame.
    - Synchronized to distributed clock —Synchronize the input to the distributed clock.
  - Input Correction (microseconds) —Specifies the correction time to synchronize the input.
  - Synchronize Output Mode —Specifies the mode to synchronize the output with the distributed clock.
    - Unsynchronized —No synchronization.
    - Synchronized to EtherCAT frame —Synchronize the output to the EtherCAT frame.
    - Synchronized to distributed clock —Synchronize the output to the distributed clock.
  - Output Correction (microseconds) —Specifies the correction time to synchronize the output.

For the four-adapter slave device, you must uncheck 
 Enable. Otherwise, the device cannot work properly.

The SYNC0 cycle time is a multiple of the scan period. You can 
 [change the scan period](/csh?context=niecat_indcomecat_changescanperiod) by configuring the scan engine.

If you specify improper values for 
 Input Correction and 
 Output Correction, the slave device enters the error mode. The NI slave device returns the error 
 Timing monitors have detected a synchronization or timing error.

The following figure describes the distributed clock-related properties.

[IMAGE alt='image' src='images/distributedclock.gif']

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatadvancedinitcmdpropertypage.html language=enus -->
## TOPIC 00015: EtherCAT:Advanced:Initial Commands Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatadvancedinitcmdpropertypage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatadvancedinitcmdpropertypage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the slave device initial commands. These commands are the additional commands to apply to the slave device during the mode transition. Only a few devices support the initial commands. The Initial command configuration table includes the following columns. Double-click the table row t

### EtherCAT:Advanced:Initial Commands Property Page

This page shows the slave device initial commands. These commands are the additional commands to apply to the slave device during the mode transition. Only a few devices support the initial commands.

The 
 Initial command configuration table includes the following columns. Double-click the table row to edit the related data value.

- Transition —The related object value is applied only when the transition happens.
- Object Index —The object index.
- Object Subindex —The object subindex.
- Data —The value to apply to the object.
- Comments —The device profile command comments.

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatadvancedmailboxpropertypage.html language=enus -->
## TOPIC 00016: EtherCAT:Advanced:Mailbox Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatadvancedmailboxpropertypage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatadvancedmailboxpropertypage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the slave device EtherCAT-specific mailbox properties. This page contains the following component: Mailbox Poll Period—The scan period to poll the device for the non-cyclic or asynchronous data such as the emergency message. You can change the scan period by configuring the scan engi

### EtherCAT:Advanced:Mailbox Property Page

This page shows the slave device EtherCAT-specific mailbox properties.

This page contains the following component:

- Mailbox Poll Period —The scan period to poll the device for the non-cyclic or asynchronous data such as the emergency message. You can 
 change the scan period by configuring the scan engine.

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatadvancedwatchdogpropertypage.html language=enus -->
## TOPIC 00017: EtherCAT:Advanced:Watchdog Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatadvancedwatchdogpropertypage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatadvancedwatchdogpropertypage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the slave device EtherCAT-specific watchdog properties. The watchdog can trigger slave device error handling. For example, entering the Safe-Operational state when a certain condition happens. This page includes the following component: Enable Sync Manager Watchdog—Specifies whether

### EtherCAT:Advanced:Watchdog Property Page

This page shows the slave device EtherCAT-specific watchdog properties. The watchdog can trigger slave device error handling. For example, entering the Safe-Operational state when a certain condition happens.

This page includes the following component:

- Enable Sync Manager Watchdog —Specifies whether to enable the sync manager watchdog for the slave device to monitor the related sync manager. The sync manager controls access to the application memory. A write access to the application memory area configured in the sync manager resets the watchdog.
- Timeout —Specifies the timeout value of the EtherCAT watchdog. The default is ten times of your scan period . If you do not use the scan period to set the watchdog timeout value, you can set the value to a multiple of 100 microseconds according to your needs.

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatbasicpropertypage.html language=enus -->
## TOPIC 00018: EtherCAT:Basic Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatbasicpropertypage.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatbasicpropertypage.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page displays the slave device EtherCAT-specific properties. This page includes the following components: Identification —Specifies the conditions to identify a slave device. The software uses the identification conditions to identify a slave device to make the deployment or upload. Position ad

### EtherCAT:Basic Property Page

This page displays the slave device EtherCAT-specific properties.

This page includes the following components:

- Identification 
 —Specifies the conditions to identify a slave device. The software uses the identification conditions to identify a slave device to make the deployment or upload.
  - Position address 
 —Identifies a slave device by the position address. This address is the numeric position of the slave device sequentially within the EtherCAT network starting from address 0. You must change the position address when you change the slave device position in the network.
- Parameters 
 —Indicates basic information of a slave device, including the following items:
  - E2PROM size (bytes) 
 —Indicates the E2PROM size.
  - FMMU number 
 —Indicates the fieldbus memory management unit number.
  - Sync manager number 
 —Indicates the synchronization manager number.
  - Mailbox protocol support 
 —Indicates the supported mailbox protocol features:
    - CANopen over EtherCAT (CoE)
    - Ethernet over EtherCAT (EoE)
    - File over EtherCAT (FoE)

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=ethercatbasicpropertypagemaster.html language=enus -->
## TOPIC 00019: EtherCAT:Basic Property Page Master

- bundle_id: `ecat-labview-api-ref`
- source_path: `ethercatbasicpropertypagemaster.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/ethercatbasicpropertypagemaster.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page shows the EtherCAT master basic properties. This page contains the following components: Percentage of each scan period to transfer cyclic data—Percentage of the scan cycle for transferring cyclic data, such as PDO. The remaining bandwidth is for transferring non-cyclic data, such as SDO.

### EtherCAT:Basic Property Page Master

This page shows the EtherCAT master basic properties.

This page contains the following components:

- Percentage of each scan period to transfer cyclic data —Percentage of the scan cycle for transferring cyclic data, such as PDO. The remaining bandwidth is for transferring non-cyclic data, such as SDO. The default value is 40 percent.
- Enable Logical Read Write (LRW) whenever possible —With the Logical Read Write service, the EtherCAT master can read and write process data of multiple slave devices in one telegram. You can enable the EtherCAT Logic Read Write to save bandwidth. When this checkbox contains a checkmark, the EtherCAT master automatically enables the service whenever possible.

Parent topic:

EtherCAT Master Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=generalpropertypagemaster.html language=enus -->
## TOPIC 00020: General Property Page Master

- bundle_id: `ecat-labview-api-ref`
- source_path: `generalpropertypagemaster.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/generalpropertypagemaster.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page includes general information about the EtherCAT master, including vendor information, adapter information, and the EtherCAT master name. This page includes the following components: Name—Specifies the EtherCAT master name. This name must be unique for each controller if the controller has

### General Property Page Master

This page includes general information about the EtherCAT master, including vendor information, adapter information, and the EtherCAT master name.

This page includes the following components:

- Name —Specifies the EtherCAT master name. This name must be unique for each controller if the controller has multiple EtherCAT masters.
- Physical adapter —Specifies the binding Ethernet adapter. You can select Offline Adapter to disconnect the connection from the EtherCAT network. Configure the Ethernet Adapter if the adapter list includes only Offline Adapter .
- Vendor —Indicates the EtherCAT master vendor. The vendor always is National Instruments.
- Type —Indicates the EtherCAT master physical type. The type always is Communication Adapter.
- Product —Indicates the EtherCAT master product category. The category always is EtherCAT Interface.
- Protocol —Indicates the protocol the EtherCAT master uses. The protocol always is EtherCAT.
- Comments —Describes the EtherCAT master.

Parent topic:

EtherCAT Master Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=generalpropertypageslave.html language=enus -->
## TOPIC 00021: General Property Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `generalpropertypageslave.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/generalpropertypageslave.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page displays the EtherCAT slave device general properties, including vendor and device information. This page includes the following components: Name—Specifies the slave device name. This name must be unique among the slave devices under an EtherCAT master. Vendor—Indicates the slave device ve

### General Property Page

This page displays the EtherCAT slave device general properties, including vendor and device information.

This page includes the following components:

- Name —Specifies the slave device name. This name must be unique among the slave devices under an EtherCAT master.
- Vendor —Indicates the slave device vendor name.
- Product code —Indicates the slave device product code.
- Type —Indicates the slave device type name.
- Description —Indicates the slave device description in the device description file.
- Revision number —Indicates the slave device revision number.
- Serial number —Indicates the slave device serial number.

Parent topic:

EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=importdeviceprofile.html language=enus -->
## TOPIC 00022: Import Device Profile Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `importdeviceprofile.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/importdeviceprofile.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In LabVIEW, right-click the EtherCAT master item and select Utilities»Import Device Profiles from the shortcut menu to display this dialog box. You must import a device profile XML file before configuring the slave device for NI-Industrial Communications for EtherCAT. This dialog box includes the fo

### Import Device Profile Dialog Box

In LabVIEW, right-click the [EtherCAT master](/csh?context=niecat_indcomecat_getstarted-addmaster) item and select Utilities»Import Device Profiles from the shortcut menu to display this dialog box.

You must import a device profile XML file before configuring the slave device for NI-Industrial Communications for EtherCAT.

This dialog box includes the following components:

- Select a device profile or file path —Specifies the device profile to import.
- Import to the host computer —Specifies whether to import the device profile to the host computer.
- Import to the real-time target —Specifies whether to import the device profile to the real-time target.
- Found device profiles —Displays the device filename and import result of the device profile.
  - Device Filename —Displays the device filename that you want to import.
  - Result —Displays the import result. The following table lists the profile type and description of each result.
 Result Profile Type DescriptionSucceeded Slave or Module Device Imported the profile successfully.Cancelled Slave or Module Device Cancelled because you do not login before accessing the remote target. Make sure that you login when the [Target Login](importdeviceprofile.html) dialog box appears.No supported protocol installed Slave or Module Device The real-time target does not have regular protocols to transfer files. Use NI Measurement & Automation Explorer (MAX) to install the WebDAV or FTP protocol to the real-time target.Failed to import the device profile Slave or Module Device Failed due to one of the following reasons: the device profile structure is changed; the profile format is not supported; the profiles are corrupted.Module profile is not referenced by any slave profiles Module Device Cannot import a module device profile that no slave device profile references. Make sure that you select a folder that contains the module device profile and the related slave device profile.Failed to transfer device profiles to the real-time target Slave or Module Device Failed because the connection between the host and the real-time target is broken or because the permission of the profiles on the real-time target does not allow the operation.
- Import —Imports device profiles. If the target is password-protected, a Target Login dialog box appears after you click the Import button. Enter the user name and the password that you specified in NI Measurement & Automation Explorer (MAX) to login before accessing the target.
- Close —Closes the dialog box.
- Help —Launches the help.

Note

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=rem-11180-io-variables.html language=enus -->
## TOPIC 00023: REM-11180 I/O Variables

- bundle_id: `ecat-labview-api-ref`
- source_path: `rem-11180-io-variables.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/rem-11180-io-variables.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: After adding the REM-11180 item to a LabVIEW project, you can see the REM-11180 I/O variables under the REM-11180 item. I/O Variable Attribute Description Localbus Add_Error InfoRead OnlyReturns the position of the Remote I/O module that is in error condition.Localbus bus StateRead OnlyReturns the c

### REM-11180 I/O Variables

After adding the REM-11180 item to a LabVIEW project, you can see the REM-11180 I/O variables under the REM-11180 item.

| I/O Variable | Attribute | Description |
| --- | --- | --- |
| Localbus Add_Error Info | Read Only | Returns the position of the Remote I/O module that is in error condition. |
| Localbus bus State | Read Only | Returns the current state of the local bus. |
| Localbus Error_Code | Read Only | Returns the error codes of Remote I/O modules. |
| New Diagnosis Message | Read Only | Returns the new message available from the diagnosis history. |

Refer to the Reading Error Codes from REM-11180 IOVs section of the NI REM-11180 User Manual for detailed information.

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc.html language=enus -->
## TOPIC 00024: Variable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### Variable

- [IndComECAT Master](../../resource/objmgr/indcomecat-rc/indcomecat-master.html)
- [IndComECAT Slave](../../resource/objmgr/indcomecat-rc/indcomecat-slave.html)

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master-m.html language=enus -->
## TOPIC 00025: IndComECAT Master Methods

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master-m.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master-m.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Master Methods

- [GetSlaveStates](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-slave-state.html) Gets an array that contains the states of all deployed and refreshed slave devices that connect to the master device.
- [GetDeviceCount](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-device-count.html) Gets the total number of slave devices that connect to the master device.
- [RawData:InputInfo](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-info.html) Gets the start position and the size of the target raw data in the input raw data array.
- [RawData:OutputInfo](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-info.html) Gets the start position and the size of the target raw data in the output raw data array.
- [RawData:TotalInputSize](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-size.html) Gets the total size of the input raw data array.
- [RawData:TotalOutputSize](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-size.html) Gets the total size of the output raw data array.
- [RawData:Read](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-raw-data.html) Reads data from the input raw data array.
- [RawData:Write](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-write-raw-data.html) Writes data to the output raw data array.
- [RawData:ReadAll](../../../resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-all-raw.html) Reads data from the input and output raw data array and returns the timestamp when the master device receives the input and output data.

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master-p.html language=enus -->
## TOPIC 00026: IndComECAT Master Properties

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master-p.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master-p.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Master Properties

- [Cable Redundancy:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-enable.html) Whether cable redundancy is enabled.
- [Cable Redundancy:Redundant Master ID](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-redundant-master-id.html) The ID of the redundant adapter.
- [Cyclic Data Bandwidth](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cyclic-data-bandwidth.html) The percentage of each scan period to transfer cyclic data (PDO & time sync).
- [Enable Device Monitor](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-device-monitor.html) Whether to enable the device monitor on the master device.
- [Enable LRW](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-lrw.html) Enable logic read write whenever possible.
- [MAC Address](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-mac-address.html) The MAC address of the NIC.
- [Master ID](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-masterid.html) The ID of this master adapter, configured in MAX.
- [Name](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-name.html) The name of the master item.
- [User Sync Shift](../../../resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-user-sync-shift.html) Additional Correction for Synchronized IO in nanoseconds.

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master.html language=enus -->
## TOPIC 00027: IndComECAT Master

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Master

Parent topic:

Variable

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-device-count.html language=enus -->
## TOPIC 00028: GetDeviceCount

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-device-count.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-device-count.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total number of slave devices that connect to the master device. Parameters Name Data type Required Description Device Count iu16.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Master_GetDeviceCount

### GetDeviceCount

Gets the total number of slave devices that connect to the master device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Device Count |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetDeviceCount |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-info.html language=enus -->
## TOPIC 00029: RawData:InputInfo

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-info.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-info.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start position and the size of the target raw data in the input raw data array. Parameters Name Data type Required Description URL cstr.png Yes Offset In Bit iu32.png No Size In Bit iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Maste

### RawData:InputInfo

Gets the start position and the size of the target raw data in the input raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| URL |  | Yes |  |
| Offset In Bit |  | No |  |
| Size In Bit |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetInputRawDataInfo |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-size.html language=enus -->
## TOPIC 00030: RawData:TotalInputSize

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-size.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-input-size.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total size of the input raw data array. Parameters Name Data type Required Description Size iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Master_GetInputRawDataSize

### RawData:TotalInputSize

Gets the total size of the input raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Size |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetInputRawDataSize |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-info.html language=enus -->
## TOPIC 00031: RawData:OutputInfo

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-info.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-info.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start position and the size of the target raw data in the output raw data array. Parameters Name Data type Required Description URL cstr.png Yes Offset In Bit iu32.png No Size In Bit iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Mast

### RawData:OutputInfo

Gets the start position and the size of the target raw data in the output raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| URL |  | Yes |  |
| Offset In Bit |  | No |  |
| Size In Bit |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetOutputRawDataInfo |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-size.html language=enus -->
## TOPIC 00032: RawData:TotalOutputSize

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-size.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-output-size.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total size of the output raw data array. Parameters Name Data type Required Description Size iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Master_GetOutputRawDataSize

### RawData:TotalOutputSize

Gets the total size of the output raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Size |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetOutputRawDataSize |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-slave-state.html language=enus -->
## TOPIC 00033: GetSlaveStates

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-slave-state.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-get-slave-state.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the states of all deployed and refreshed slave devices that connect to the master device. Parameters Name Data type Required Description Slave States c1du32.png Yes Slave States i1du32.png No Remarks The following table lists the characteristics of this method. Short Name

### GetSlaveStates

Gets an array that contains the states of all deployed and refreshed slave devices that connect to the master device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Slave States |  | Yes |  |
| Slave States |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_GetSlaveStates |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-all-raw.html language=enus -->
## TOPIC 00034: RawData:ReadAll

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-all-raw.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-all-raw.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from the input and output raw data array and returns the timestamp when the master device receives the input and output data. Parameters Name Data type Required Description Data In All c1du8.png Yes Data In All i1du8.png No Remarks The following table lists the characteristics of this met

### RawData:ReadAll

Reads data from the input and output raw data array and returns the timestamp when the master device receives the input and output data.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Data In All |  | Yes |  |
| Data In All |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_ReadAllRawData |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-raw-data.html language=enus -->
## TOPIC 00035: RawData:Read

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-raw-data.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-read-raw-data.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from the input raw data array. Parameters Name Data type Required Description Data In c1du8.png Yes Data In i1du8.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Master_ReadRawData

### RawData:Read

Reads data from the input raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Data In |  | Yes |  |
| Data In |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_ReadRawData |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/ecat-write-raw-data.html language=enus -->
## TOPIC 00036: RawData:Write

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/ecat-write-raw-data.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/ecat-write-raw-data.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the output raw data array. Parameters Name Data type Required Description Data Out c1du8.png Yes Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Master_WriteRawData

### RawData:Write

Writes data to the output raw data array.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Data Out |  | Yes |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Master_WriteRawData |
| --- | --- |

Parent topic:

IndComECAT Master Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-enable.html language=enus -->
## TOPIC 00037: Cable Redundancy:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether cable redundancy is enabled. Remarks The following table lists the characteristics of this property. Short Name Cable Redundancy.Enable Data type cbool.png Permissions Read Only

### Cable Redundancy:Enable

Whether cable redundancy is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cable Redundancy.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-redundant-master-id.html language=enus -->
## TOPIC 00038: Cable Redundancy:Redundant Master ID

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-redundant-master-id.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cable-redundancy-redundant-master-id.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ID of the redundant adapter. Remarks The following table lists the characteristics of this property. Short Name Cable Redundancy.Redundant Master ID Data type cu32.png Permissions Read Only

### Cable Redundancy:Redundant Master ID

The ID of the redundant adapter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cable Redundancy.Redundant Master ID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cyclic-data-bandwidth.html language=enus -->
## TOPIC 00039: Cyclic Data Bandwidth

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cyclic-data-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-cyclic-data-bandwidth.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The percentage of each scan period to transfer cyclic data (PDO & time sync). Remarks The following table lists the characteristics of this property. Short Name Cyclic Data Bandwidth Data type cu32.png Permissions Read/Write

### Cyclic Data Bandwidth

The percentage of each scan period to transfer cyclic data (PDO & time sync).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cyclic Data Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-device-monitor.html language=enus -->
## TOPIC 00040: Enable Device Monitor

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-device-monitor.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-device-monitor.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether to enable the device monitor on the master device. Remarks The following table lists the characteristics of this property. Short Name Enable Device Monitor Data type cbool.png Permissions Read/Write

### Enable Device Monitor

Whether to enable the device monitor on the master device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable Device Monitor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-lrw.html language=enus -->
## TOPIC 00041: Enable LRW

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-lrw.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-enable-lrw.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enable logic read write whenever possible. Remarks The following table lists the characteristics of this property. Short Name Enable LRW Data type cbool.png Permissions Read/Write

### Enable LRW

Enable logic read write whenever possible.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable LRW |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-mac-address.html language=enus -->
## TOPIC 00042: MAC Address

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-mac-address.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-mac-address.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The MAC address of the NIC. Remarks The following table lists the characteristics of this property. Short Name MAC Address Data type cstr.png Permissions Read Only

### MAC Address

The MAC address of the NIC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Address |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-masterid.html language=enus -->
## TOPIC 00043: Master ID

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-masterid.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-masterid.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ID of this master adapter, configured in MAX. Remarks The following table lists the characteristics of this property. Short Name Master ID Data type cu32.png Permissions Read Only

### Master ID

The ID of this master adapter, configured in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Master ID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-name.html language=enus -->
## TOPIC 00044: Name

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-name.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-name.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The name of the master item. Remarks The following table lists the characteristics of this property. Short Name Name Data type cstr.png Permissions Read Only

### Name

The name of the master item.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-user-sync-shift.html language=enus -->
## TOPIC 00045: User Sync Shift

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-user-sync-shift.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-master/masterproperties-user-sync-shift.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Additional Correction for Synchronized IO in nanoseconds. Remarks The following table lists the characteristics of this property. Short Name User Sync Shift Data type ci32.png Permissions Read/Write

### User Sync Shift

Additional Correction for Synchronized IO in nanoseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | User Sync Shift |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Master Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave-m.html language=enus -->
## TOPIC 00046: IndComECAT Slave Methods

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave-m.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave-m.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Slave Methods

- [GetState](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getstate.html) Gets the state of the slave device.
- [SetState](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/setstate.html) Sets the state of the slave device.
- [QueryLastError](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/querylasterror.html) Gets the last error of the slave device.
- [ClearLastError](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/clearlasterror.html) Clears the last error of the slave device.
- [WriteSDO](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/writesdo.html) Writes SDO to the slave device.
- [WriteSDOCompleteAccess](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/writesdocompleteaccess.html) Writes SDO in complete access.
- [CheckWriteSDODone](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/checkwritesdodone.html) Checks whether a non-blocking write SDO has been completed.
- [ReadSDO](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/readsdo.html) Reads SDO from the slave device.
- [ReadSDOCompleteAccess](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/readsdocompleteaccess.html) Reads SDO in complete access.
- [CheckReadSDODone](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/checkreadsdodone.html) Checks whether a non-blocking Read SDO has been completed.
- [GetODList](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getodlist.html) Gets an object dictionary list.
- [GetObjDesc](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getobjdesc.html) Gets an object description.
- [GetEntryDesc](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getentrydesc.html) Gets an Entry Description.
- [ReadEmergencyData](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/reademergencydata.html) Reads emergency data from a queue.
- [CancelSDO](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/cancelsdo.html) Cancels any SDO operation.
- [WriteFoEStart](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/writefoestart.html) Starts an FoE write operation.
- [WriteFoEData](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/writefoedata.html) Executes an FoE write operation.
- [CancelFoE](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/cancelfoe.html) Cancels any FoE operation.
- [GetFoERequestError](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getfoerequesterror.html) Get the detailed FoE error info.
- [GetPortLinkStatus](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/getportlinkstatus.html) Get the port link status of the slave device.

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave-p.html language=enus -->
## TOPIC 00047: IndComECAT Slave Properties

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave-p.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave-p.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Slave Properties

- [CoE support](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-coe-support.html) Whether the slave device supports CoE.
- [DC:Sync0:CycleByScan](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-cyclebyscan.html) The Sync0 cycle time in the number of scans.
- [DC:Sync0:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-enable.html) Whether to enable DC and Sync0.
- [DC:Sync0:Shift](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-shift.html) The Sync0 shift in nanoseconds.
- [DC:Sync1:CycleBySync0Cycle](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync1-cyclebysync0cycle.html) The Sync1 cycle time in the number of sync0 cycles.
- [DC:Sync1:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable.html) Whether to enable Sync1.
- [Description](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-desc.html) The description of the slave device in the slave device profile.
- [EEPROM size](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eeprom-size.html) The EEPROM size of the slave device, in bytes.
- [Enable Raw Data Mode](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable-raw-data-mode.html) Whether to enable Raw Data mode on this device.
- [EoE support](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eoe-support.html) Whether the slave device supports EoE.
- [FMMU num](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-fmmu-num.html) How many FMMUs are supported in the slave device.
- [FoE support](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-foe-support.html) Whether the slave device supports FoE.
- [Mailbox:PollRateByScan](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-mailbox-pollratebyscan.html) The Mailbox polling cycle in the number of scans.
- [Name](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-name.html) The name of the slave device.
- [Position Address](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-position-address.html) The position address of the slave device.
- [Product Code](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-product-code.html) The Product Code of the slave device.
- [Revision Number](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-revision-number.html) The Revision Number of the slave device.
- [SM num](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-sm-num.html) How many Sync Managers are supported in the slave device.
- [Serial Number](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-serial-number.html) The Serial Number of the slave device.
- [SyncIO:Input:Correction](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-correction.html) The correction for the input sync in nanoseconds.
- [SyncIO:Input:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-enable.html) Whether input sync manager parameter object 1C33 is enabled.
- [SyncIO:Input:Mode](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-mode.html) The mode of the input sync.
- [SyncIO:Output:Correction](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-correction.html) The correction for the output sync in nanoseconds.
- [SyncIO:Output:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-enable.html) Whether output sync manager parameter object 1C32 is enabled.
- [SyncIO:Output:Mode](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-mode.html) The mode of the output sync.
- [Vendor ID](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-vendor-id.html) The Vendor ID of the slave device.
- [Watchdog:SMWatchdog:Enable](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-enable.html) Whether to enable Sync Manager watchdog.
- [Watchdog:SMWatchdog:TimeByScan](../../../resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-timebyscan.html) The Sync manager timeout in the number of scans.

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave.html language=enus -->
## TOPIC 00048: IndComECAT Slave

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### IndComECAT Slave

Parent topic:

Variable

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/cancelfoe.html language=enus -->
## TOPIC 00049: CancelFoE

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/cancelfoe.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/cancelfoe.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cancels any FoE operation. Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_WriteFoE_Cancel

### CancelFoE

Cancels any FoE operation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_WriteFoE_Cancel |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/cancelsdo.html language=enus -->
## TOPIC 00050: CancelSDO

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/cancelsdo.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/cancelsdo.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cancels any SDO operation. Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_CoECancel

### CancelSDO

Cancels any SDO operation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_CoECancel |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/checkreadsdodone.html language=enus -->
## TOPIC 00051: CheckReadSDODone

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/checkreadsdodone.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/checkreadsdodone.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether a non-blocking Read SDO has been completed. Parameters Name Data type Required Description Done ibool.png No Data i1du8.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_CheckReadSDO

### CheckReadSDODone

Checks whether a non-blocking Read SDO has been completed.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Done |  | No |  |
| Data |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_CheckReadSDO |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/checkwritesdodone.html language=enus -->
## TOPIC 00052: CheckWriteSDODone

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/checkwritesdodone.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/checkwritesdodone.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether a non-blocking write SDO has been completed. Parameters Name Data type Required Description Done ibool.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_CheckWriteSDO

### CheckWriteSDODone

Checks whether a non-blocking write SDO has been completed.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Done |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_CheckWriteSDO |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/clearlasterror.html language=enus -->
## TOPIC 00053: ClearLastError

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/clearlasterror.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/clearlasterror.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the last error of the slave device. Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_ClearLastError

### ClearLastError

Clears the last error of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_ClearLastError |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getentrydesc.html language=enus -->
## TOPIC 00054: GetEntryDesc

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getentrydesc.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getentrydesc.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an Entry Description. Parameters Name Data type Required Description OD Addr cu16.png Yes Index cu16.png Yes Subindex cu8.png Yes Value Mask cu8.png Yes Data Type iu16.png No Bit Length iu16.png No Obj Access iu16.png No Unit Type iu16.png No Default Value i1du8.png No Min Value i1du8.png No Ma

### GetEntryDesc

Gets an Entry Description.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Subindex |  | Yes |  |
| Value Mask |  | Yes |  |
| Data Type |  | No |  |
| Bit Length |  | No |  |
| Obj Access |  | No |  |
| Unit Type |  | No |  |
| Default Value |  | No |  |
| Min Value |  | No |  |
| Max Value |  | No |  |
| Description |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetEntryDesc |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getfoerequesterror.html language=enus -->
## TOPIC 00055: GetFoERequestError

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getfoerequesterror.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getfoerequesterror.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the detailed FoE error info. Parameters Name Data type Required Description Error Code iu32.png No Error Msg istr.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_GetFoERequestError

### GetFoERequestError

Get the detailed FoE error info.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Error Code |  | No |  |
| Error Msg |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetFoERequestError |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getobjdesc.html language=enus -->
## TOPIC 00056: GetObjDesc

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getobjdesc.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getobjdesc.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an object description. Parameters Name Data type Required Description OD Addr cu16.png Yes Index cu16.png Yes Name istr.png No Obj Type iu8.png No Data Type iu16.png No Max Subindex iu8.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Nam

### GetObjDesc

Gets an object description.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Name |  | No |  |
| Obj Type |  | No |  |
| Data Type |  | No |  |
| Max Subindex |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetObjDesc |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getodlist.html language=enus -->
## TOPIC 00057: GetODList

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getodlist.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getodlist.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an object dictionary list. Parameters Name Data type Required Description OD Addr cu16.png Yes List Type cu32.png Yes Indices i1du16.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_GetODList

### GetODList

Gets an object dictionary list.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| OD Addr |  | Yes |  |
| List Type |  | Yes |  |
| Indices |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetODList |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getportlinkstatus.html language=enus -->
## TOPIC 00058: GetPortLinkStatus

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getportlinkstatus.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getportlinkstatus.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the port link status of the slave device. Parameters Name Data type Required Description Status i1dbool.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_GetPortLinkStatus

### GetPortLinkStatus

Get the port link status of the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Status |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetPortLinkStatus |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/getstate.html language=enus -->
## TOPIC 00059: GetState

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/getstate.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/getstate.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the state of the slave device. Parameters Name Data type Required Description Slave State iu32.png No App Spec Code iu8.png No Status Code iu16.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_GetState

### GetState

Gets the state of the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Slave State |  | No |  |
| App Spec Code |  | No |  |
| Status Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_GetState |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/querylasterror.html language=enus -->
## TOPIC 00060: QueryLastError

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/querylasterror.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/querylasterror.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the last error of the slave device. Parameters Name Data type Required Description Last Error ii32.png No Error Ext iu32.png No Error Ext Para i1du32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_QueryLastError

### QueryLastError

Gets the last error of the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Last Error |  | No |  |
| Error Ext |  | No |  |
| Error Ext Para |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_QueryLastError |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/reademergencydata.html language=enus -->
## TOPIC 00061: ReadEmergencyData

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/reademergencydata.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/reademergencydata.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads emergency data from a queue. Parameters Name Data type Required Description Has Data ibool.png No Error Code iu16.png No Error Register iu8.png No Emergency Data i1du8.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_ReadEmergency

### ReadEmergencyData

Reads emergency data from a queue.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Has Data |  | No |  |
| Error Code |  | No |  |
| Error Register |  | No |  |
| Emergency Data |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_ReadEmergency |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/readsdo.html language=enus -->
## TOPIC 00062: ReadSDO

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/readsdo.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/readsdo.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads SDO from the slave device. Parameters Name Data type Required Description Blocking cbool.png Yes OD Addr cu16.png Yes Index cu16.png Yes Subindex cu8.png Yes Data i1du8.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Sla

### ReadSDO

Reads SDO from the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Blocking |  | Yes |  |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Subindex |  | Yes |  |
| Data |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_ReadSDO |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/readsdocompleteaccess.html language=enus -->
## TOPIC 00063: ReadSDOCompleteAccess

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/readsdocompleteaccess.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/readsdocompleteaccess.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads SDO in complete access. Parameters Name Data type Required Description Blocking cbool.png Yes OD Addr cu16.png Yes Index cu16.png Yes Data i1du8.png No Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_ReadSDOCompleteAccess

### ReadSDOCompleteAccess

Reads SDO in complete access.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Blocking |  | Yes |  |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Data |  | No |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_ReadSDOCompleteAccess |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/setstate.html language=enus -->
## TOPIC 00064: SetState

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/setstate.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/setstate.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the state of the slave device. Parameters Name Data type Required Description Slave State cu32.png Yes Ack Error cbool.png Yes Timeout cu32.png Yes App Spec Code iu8.png No Status Code iu16.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_

### SetState

Sets the state of the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Slave State |  | Yes |  |
| Ack Error |  | Yes |  |
| Timeout |  | Yes |  |
| App Spec Code |  | No |  |
| Status Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_SetState |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-coe-support.html language=enus -->
## TOPIC 00065: CoE support

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-coe-support.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-coe-support.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the slave device supports CoE. Remarks The following table lists the characteristics of this property. Short Name CoE support Data type cbool.png Permissions Read Only

### CoE support

Whether the slave device supports CoE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CoE support |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-cyclebyscan.html language=enus -->
## TOPIC 00066: DC:Sync0:CycleByScan

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-cyclebyscan.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-cyclebyscan.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Sync0 cycle time in the number of scans. Remarks The following table lists the characteristics of this property. Short Name DC.Sync0.CycleByScan Data type cu32.png Permissions Read/Write

### DC:Sync0:CycleByScan

The Sync0 cycle time in the number of scans.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC.Sync0.CycleByScan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-enable.html language=enus -->
## TOPIC 00067: DC:Sync0:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync0-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether to enable DC and Sync0. Remarks The following table lists the characteristics of this property. Short Name DC.Sync0.Enable Data type cbool.png Permissions Read/Write

### DC:Sync0:Enable

Whether to enable DC and Sync0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC.Sync0.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync1-cyclebysync0cycle.html language=enus -->
## TOPIC 00068: DC:Sync1:CycleBySync0Cycle

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync1-cyclebysync0cycle.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-dc-sync1-cyclebysync0cycle.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Sync1 cycle time in the number of sync0 cycles. Remarks The following table lists the characteristics of this property. Short Name DC.Sync1.CycleBySync0Cycle Data type cu32.png Permissions Read/Write

### DC:Sync1:CycleBySync0Cycle

The Sync1 cycle time in the number of sync0 cycles.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC.Sync1.CycleBySync0Cycle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-desc.html language=enus -->
## TOPIC 00069: Description

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-desc.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-desc.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The description of the slave device in the slave device profile. Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only

### Description

The description of the slave device in the slave device profile.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Description |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eeprom-size.html language=enus -->
## TOPIC 00070: EEPROM size

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eeprom-size.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eeprom-size.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The EEPROM size of the slave device, in bytes. Remarks The following table lists the characteristics of this property. Short Name EEPROM size Data type cu32.png Permissions Read Only

### EEPROM size

The EEPROM size of the slave device, in bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EEPROM size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable-raw-data-mode.html language=enus -->
## TOPIC 00071: Enable Raw Data Mode

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable-raw-data-mode.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable-raw-data-mode.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether to enable Raw Data mode on this device. Remarks The following table lists the characteristics of this property. Short Name Enable Raw Data Mode Data type cbool.png Permissions Read/Write

### Enable Raw Data Mode

Whether to enable Raw Data mode on this device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable Raw Data Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable.html language=enus -->
## TOPIC 00072: DC:Sync1:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether to enable Sync1. Remarks The following table lists the characteristics of this property. Short Name DC.Sync1.Enable Data type cbool.png Permissions Read/Write

### DC:Sync1:Enable

Whether to enable Sync1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC.Sync1.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eoe-support.html language=enus -->
## TOPIC 00073: EoE support

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eoe-support.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-eoe-support.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the slave device supports EoE. Remarks The following table lists the characteristics of this property. Short Name EoE support Data type cbool.png Permissions Read Only

### EoE support

Whether the slave device supports EoE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EoE support |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-fmmu-num.html language=enus -->
## TOPIC 00074: FMMU num

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-fmmu-num.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-fmmu-num.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: How many FMMUs are supported in the slave device. Remarks The following table lists the characteristics of this property. Short Name FMMU num Data type cu32.png Permissions Read Only

### FMMU num

How many FMMUs are supported in the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FMMU num |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-foe-support.html language=enus -->
## TOPIC 00075: FoE support

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-foe-support.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-foe-support.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the slave device supports FoE. Remarks The following table lists the characteristics of this property. Short Name FoE support Data type cbool.png Permissions Read Only

### FoE support

Whether the slave device supports FoE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FoE support |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-mailbox-pollratebyscan.html language=enus -->
## TOPIC 00076: Mailbox:PollRateByScan

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-mailbox-pollratebyscan.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-mailbox-pollratebyscan.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Mailbox polling cycle in the number of scans. Remarks The following table lists the characteristics of this property. Short Name Mailbox.PollRateByScan Data type cu32.png Permissions Read/Write

### Mailbox:PollRateByScan

The Mailbox polling cycle in the number of scans.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mailbox.PollRateByScan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-name.html language=enus -->
## TOPIC 00077: Name

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-name.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-name.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The name of the slave device. Remarks The following table lists the characteristics of this property. Short Name Name Data type cstr.png Permissions Read Only

### Name

The name of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-position-address.html language=enus -->
## TOPIC 00078: Position Address

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-position-address.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-position-address.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The position address of the slave device. Remarks The following table lists the characteristics of this property. Short Name Position Address Data type cu16.png Permissions Read Only

### Position Address

The position address of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Position Address |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-product-code.html language=enus -->
## TOPIC 00079: Product Code

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-product-code.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-product-code.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Product Code of the slave device. Remarks The following table lists the characteristics of this property. Short Name Product Code Data type cu32.png Permissions Read Only

### Product Code

The Product Code of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Product Code |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-revision-number.html language=enus -->
## TOPIC 00080: Revision Number

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-revision-number.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-revision-number.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Revision Number of the slave device. Remarks The following table lists the characteristics of this property. Short Name Revision Number Data type cu32.png Permissions Read Only

### Revision Number

The Revision Number of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Revision Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-serial-number.html language=enus -->
## TOPIC 00081: Serial Number

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-serial-number.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-serial-number.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Serial Number of the slave device. Remarks The following table lists the characteristics of this property. Short Name Serial Number Data type cu32.png Permissions Read Only

### Serial Number

The Serial Number of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-shift.html language=enus -->
## TOPIC 00082: DC:Sync0:Shift

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-shift.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-shift.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Sync0 shift in nanoseconds. Remarks The following table lists the characteristics of this property. Short Name DC.Sync0.Shift Data type cu32.png Permissions Read/Write

### DC:Sync0:Shift

The Sync0 shift in nanoseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC.Sync0.Shift |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-sm-num.html language=enus -->
## TOPIC 00083: SM num

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-sm-num.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-sm-num.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: How many Sync Managers are supported in the slave device. Remarks The following table lists the characteristics of this property. Short Name SM num Data type cu32.png Permissions Read Only

### SM num

How many Sync Managers are supported in the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SM num |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-correction.html language=enus -->
## TOPIC 00084: SyncIO:Input:Correction

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-correction.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-correction.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The correction for the input sync in nanoseconds. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Input.Correction Data type ci32.png Permissions Read/Write

### SyncIO:Input:Correction

The correction for the input sync in nanoseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Input.Correction |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-enable.html language=enus -->
## TOPIC 00085: SyncIO:Input:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether input sync manager parameter object 1C33 is enabled. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Input.Enable Data type cbool.png Permissions Read/Write

### SyncIO:Input:Enable

Whether input sync manager parameter object 1C33 is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Input.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-mode.html language=enus -->
## TOPIC 00086: SyncIO:Input:Mode

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-mode.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-input-mode.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The mode of the input sync. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Input.Mode Data type cu32.png Permissions Read/Write Unsynchronized 0 Synchronized to EtherCAT frame 1 Synchronized to distributed clock 2

### SyncIO:Input:Mode

The mode of the input sync.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Input.Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Unsynchronized | 0 |  |
| --- | --- | --- |
| Synchronized to EtherCAT frame | 1 |  |
| Synchronized to distributed clock | 2 |  |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-correction.html language=enus -->
## TOPIC 00087: SyncIO:Output:Correction

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-correction.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-correction.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The correction for the output sync in nanoseconds. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Output.Correction Data type ci32.png Permissions Read/Write

### SyncIO:Output:Correction

The correction for the output sync in nanoseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Output.Correction |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-enable.html language=enus -->
## TOPIC 00088: SyncIO:Output:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether output sync manager parameter object 1C32 is enabled. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Output.Enable Data type cbool.png Permissions Read/Write

### SyncIO:Output:Enable

Whether output sync manager parameter object 1C32 is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Output.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-mode.html language=enus -->
## TOPIC 00089: SyncIO:Output:Mode

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-mode.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-syncio-output-mode.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The mode of the output sync. Remarks The following table lists the characteristics of this property. Short Name SyncIO.Output.Mode Data type cu32.png Permissions Read/Write Unsynchronized 0 Synchronized to EtherCAT frame 1 Synchronized to distributed clock 2

### SyncIO:Output:Mode

The mode of the output sync.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncIO.Output.Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Unsynchronized | 0 |  |
| --- | --- | --- |
| Synchronized to EtherCAT frame | 1 |  |
| Synchronized to distributed clock | 2 |  |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-vendor-id.html language=enus -->
## TOPIC 00090: Vendor ID

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-vendor-id.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-vendor-id.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Vendor ID of the slave device. Remarks The following table lists the characteristics of this property. Short Name Vendor ID Data type cu32.png Permissions Read Only

### Vendor ID

The Vendor ID of the slave device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vendor ID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-enable.html language=enus -->
## TOPIC 00091: Watchdog:SMWatchdog:Enable

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-enable.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-enable.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether to enable Sync Manager watchdog. Remarks The following table lists the characteristics of this property. Short Name Watchdog.SMWatchdog.Enable Data type cbool.png Permissions Read/Write

### Watchdog:SMWatchdog:Enable

Whether to enable Sync Manager watchdog.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Watchdog.SMWatchdog.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-timebyscan.html language=enus -->
## TOPIC 00092: Watchdog:SMWatchdog:TimeByScan

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-timebyscan.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/slaveproperties-watchdog-smwatchdog-timebyscan.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Sync manager timeout in the number of scans. Remarks The following table lists the characteristics of this property. Short Name Watchdog.SMWatchdog.TimeByScan Data type cu32.png Permissions Read/Write

### Watchdog:SMWatchdog:TimeByScan

The Sync manager timeout in the number of scans.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Watchdog.SMWatchdog.TimeByScan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

IndComECAT Slave Properties

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/writefoedata.html language=enus -->
## TOPIC 00093: WriteFoEData

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/writefoedata.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/writefoedata.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes an FoE write operation. Parameters Name Data type Required Description Data c1du8.png Yes Last Block cbool.png Yes Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_WriteFoE_WriteData

### WriteFoEData

Executes an FoE write operation.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Data |  | Yes |  |
| Last Block |  | Yes |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_WriteFoE_WriteData |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/writefoestart.html language=enus -->
## TOPIC 00094: WriteFoEStart

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/writefoestart.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/writefoestart.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts an FoE write operation. Parameters Name Data type Required Description File Name cstr.png Yes Password cu32.png Yes Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_WriteFoE_Start

### WriteFoEStart

Starts an FoE write operation.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| File Name |  | Yes |  |
| Password |  | Yes |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_WriteFoE_Start |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/writesdo.html language=enus -->
## TOPIC 00095: WriteSDO

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/writesdo.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/writesdo.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes SDO to the slave device. Parameters Name Data type Required Description Blocking cbool.png Yes OD Addr cu16.png Yes Index cu16.png Yes Subindex cu8.png Yes Data c1du8.png Yes Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Sla

### WriteSDO

Writes SDO to the slave device.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Blocking |  | Yes |  |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Subindex |  | Yes |  |
| Data |  | Yes |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_WriteSDO |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=resource/objmgr/indcomecat-rc/indcomecat-slave/writesdocompleteaccess.html language=enus -->
## TOPIC 00096: WriteSDOCompleteAccess

- bundle_id: `ecat-labview-api-ref`
- source_path: `resource/objmgr/indcomecat-rc/indcomecat-slave/writesdocompleteaccess.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/resource/objmgr/indcomecat-rc/indcomecat-slave/writesdocompleteaccess.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes SDO in complete access. Parameters Name Data type Required Description Blocking cbool.png Yes OD Addr cu16.png Yes Index cu16.png Yes Data c1du8.png Yes Abort Code iu32.png No Remarks The following table lists the characteristics of this method. Short Name neLVRefNum_Slave_WriteSDOCompleteAcc

### WriteSDOCompleteAccess

Writes SDO in complete access.

#### Parameters

| Name | Data type | Required | Description |
| --- | --- | --- | --- |
| Blocking |  | Yes |  |
| OD Addr |  | Yes |  |
| Index |  | Yes |  |
| Data |  | Yes |  |
| Abort Code |  | No |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this method.

| Short Name | neLVRefNum_Slave_WriteSDOCompleteAccess |
| --- | --- |

Parent topic:

IndComECAT Slave Methods

<!--NI_TOPIC bundle=ecat-labview-api-ref path=targets/ni/rt/menus/categories/industrial-communications/ethercat/dir-mnu.html language=enus -->
## TOPIC 00097: EtherCAT

- bundle_id: `ecat-labview-api-ref`
- source_path: `targets/ni/rt/menus/categories/industrial-communications/ethercat/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/industrial-communications/ethercat/dir-mnu.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the EtherCAT VIs to interact with EtherCAT devices. icon

### EtherCAT

Use the EtherCAT VIs to interact with EtherCAT devices.

[IMAGE alt='icon' src='dir-mnu.png']

<!--NI_TOPIC bundle=ecat-labview-api-ref path=targets/ni/rt/menus/categories/industrial-communications/ethercat/remote-io/remote-io-mnu.html language=enus -->
## TOPIC 00098: Remote I/O

- bundle_id: `ecat-labview-api-ref`
- source_path: `targets/ni/rt/menus/categories/industrial-communications/ethercat/remote-io/remote-io-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/industrial-communications/ethercat/remote-io/remote-io-mnu.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Remote I/O VIs to interact with Remote I/O components. icon

### Remote I/O

Use the Remote I/O VIs to interact with Remote I/O components.

[IMAGE alt='icon' src='remote-io-mnu.png']

- [REM-11180 I/O Variables](../../../../../../../../rem-11180-io-variables.html)
- [Open Slave VI](../../../../../../../../vi-lib/indcomecat/remote-io/open-slave-vi.html) Opens a reference to the Remote I/O slave.
- [Close Slave VI](../../../../../../../../vi-lib/indcomecat/remote-io/close-slave-vi.html) Closes a reference to the Remote I/O slave.
- [Configure Module VI](../../../../../../../../vi-lib/indcomecat/remote-io/configure-module-vi.html) Configures a Remote I/O module.
- [Read Module Config VI](../../../../../../../../vi-lib/indcomecat/remote-io/read-module-config-vi.html) Reads parameters of a Remote I/O module.
- [Scale VI](../../../../../../../../vi-lib/indcomecat/remote-io/scale-vi.html) Manages conversion between raw data and scaled data.
- [Diagnose VI](../../../../../../../../vi-lib/indcomecat/remote-io/diagnose-vi.html) Returns error information and bus state from the Remote I/O slave.

<!--NI_TOPIC bundle=ecat-labview-api-ref path=third-party-ethercat-general-properties.html language=enus -->
## TOPIC 00099: General Properties Page

- bundle_id: `ecat-labview-api-ref`
- source_path: `third-party-ethercat-general-properties.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/third-party-ethercat-general-properties.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page displays the third-party EtherCAT module general properties, including module type and slot information. This page includes the following components: Name—Specifies the third-party module name. This name must be unique among the modules under a slave. Module type—Indicates the third-party

### General Properties Page

This page displays the third-party EtherCAT module general properties, including module type and slot information.

This page includes the following components:

- Name —Specifies the third-party module name. This name must be unique among the modules under a slave.
- Module type —Indicates the third-party module slot information.
- Slot —Specifies the third-party module slot information.

Parent topic:

Third-Party EtherCAT Module Properties Dialog Box

<!--NI_TOPIC bundle=ecat-labview-api-ref path=third-party-ethercat-module-prop-dialog.html language=enus -->
## TOPIC 00100: Third-Party EtherCAT Module Properties Dialog Box

- bundle_id: `ecat-labview-api-ref`
- source_path: `third-party-ethercat-module-prop-dialog.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/third-party-ethercat-module-prop-dialog.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To edit a third-party EtherCAT module property, right-click the third-party EtherCAT module item and select Properties to display the Third-Party EtherCAT Module Properties dialog box. The Third-Party EtherCAT Module Properties dialog box includes the following page: General

### Third-Party EtherCAT Module Properties Dialog Box

To edit a third-party EtherCAT module property, right-click the third-party [EtherCAT module item](environment-lvprojectitem.html) and select Properties to display the Third-Party EtherCAT Module Properties dialog box.

The Third-Party EtherCAT Module Properties dialog box includes the following page:

- General

- [General Properties Page](third-party-ethercat-general-properties.html)

Parent topic:

NI-Industrial Communications for EtherCAT Environment

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/close-slave-vi.html language=enus -->
## TOPIC 00101: Close Slave VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/close-slave-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/close-slave-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a reference to the Remote I/O slave. icon Inputs/Outputs cgenclassrntag.png slave reference slave reference specifies the reference to the Remote I/O slave. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard

### Close Slave VI

Closes a reference to the Remote I/O slave.

[IMAGE alt='icon' src='close-slave-vi.png']

#### Inputs/Outputs

| slave reference — slave reference specifies the reference to the Remote I/O slave. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/configure-module-vi.html language=enus -->
## TOPIC 00102: Configure Module VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/configure-module-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/configure-module-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon

### Configure Module VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-module-vi.png']

- [_Configure REM-11100 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11100-vi.html) Configures a Remote I/O module.
- [_Configure REM-11102 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11102-vi.html) Configures a Remote I/O module.
- [_Configure REM-11115 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11115-vi.html) Configures a Remote I/O module.
- [_Configure REM-11120 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11120-vi.html) Configures a Remote I/O module.
- [_Configure REM-11152 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11152-vi.html) Configures a Remote I/O module.
- [_Configure REM-11154 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11154-vi.html) Configures a Remote I/O module.
- [_Configure REM-11175 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11175-vi.html) Configures a Remote I/O module.
- [_Configure REM-11178 VI](../../../vi-lib/indcomecat/remote-io/internal/configure-rem-11178-vi.html) Configures a Remote I/O module.

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/diagnose-vi.html language=enus -->
## TOPIC 00103: Diagnose VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/diagnose-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/diagnose-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns error information and bus state from the Remote I/O slave. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs.

### Diagnose VI

Returns error information and bus state from the Remote I/O slave.

[IMAGE alt='icon' src='diagnose-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. bus state — bus state returns the current state of the local bus. error code — error code returns error codes of Remote I/O modules. Refer to the NI REM-11180 User Manual for detailed information about error codes of Remote I/O modules. additional error info — additional error info returns the position of the Remote I/O module that is in error condition. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11100-vi.html language=enus -->
## TOPIC 00104: _Configure REM-11100 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11100-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11100-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. c1dnclst.png para

### _Configure REM-11100 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11100-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters for channels — parameters for channels specifies parameters for channels of the Remote I/O module. channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. mean-value — mean-value specifies the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range specifies the voltage range that the channel measures. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. mean-value — mean-value specifies the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range specifies the voltage range that the channel measures. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11102-vi.html language=enus -->
## TOPIC 00105: _Configure REM-11102 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11102-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11102-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. c1dnclst.png para

### _Configure REM-11102 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11102-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters for channels — parameters for channels specifies parameters for channels of the Remote I/O module. channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. mean-value — mean-value specifies the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range specifies the current range that the channel measures. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. mean-value — mean-value specifies the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range specifies the current range that the channel measures. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11115-vi.html language=enus -->
## TOPIC 00106: _Configure REM-11115 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11115-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11115-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. c1dnclst.png para

### _Configure REM-11115 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11115-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters for channels — parameters for channels specifies parameters for channels of the Remote I/O module. channel number — channel number specifies the number of the channel to configure. output range — output range specifies the output voltage or current range of the channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number specifies the number of the channel to configure. output range — output range specifies the output voltage or current range of the channel. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11120-vi.html language=enus -->
## TOPIC 00107: _Configure REM-11120 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11120-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11120-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. ccclst.png parame

### _Configure REM-11120 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11120-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters — parameters specifies the mounting position and channel information of the Remote I/O module. mounting position — mounting position specifies the mounting position of the Remote I/O module. parameters for channels — parameters for channels specifies parameters for channels of the Remote I/O module. channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. cold junction type — cold junction type specifies the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution specifies the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type specifies the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| mounting position — mounting position specifies the mounting position of the Remote I/O module. parameters for channels — parameters for channels specifies parameters for channels of the Remote I/O module. channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. cold junction type — cold junction type specifies the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution specifies the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type specifies the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. |
| channel number — channel number specifies the number of the channel to configure. input filter time — input filter time specifies the sampling frequency of the channel. cold junction type — cold junction type specifies the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution specifies the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type specifies the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11152-vi.html language=enus -->
## TOPIC 00108: _Configure REM-11152 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11152-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11152-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cu8.png input fil

### _Configure REM-11152 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11152-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. input filter time — input filter time specifies the sampling period of the Remote I/O module. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11154-vi.html language=enus -->
## TOPIC 00109: _Configure REM-11154 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11154-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11154-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cu8.png input fil

### _Configure REM-11154 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11154-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. input filter time — input filter time specifies the sampling period of the Remote I/O module. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11175-vi.html language=enus -->
## TOPIC 00110: _Configure REM-11175 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11175-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11175-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cnclst.png parame

### _Configure REM-11175 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11175-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters — parameters specifies the parameter information of the Remote I/O module. substitute value on error — substitute value on error specifies the output value behavior in case of a communication failure or bus reset. actuator detection — report "actuator supply not present" message? specifies whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| substitute value on error — substitute value on error specifies the output value behavior in case of a communication failure or bus reset. actuator detection — report "actuator supply not present" message? specifies whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/configure-rem-11178-vi.html language=enus -->
## TOPIC 00111: _Configure REM-11178 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/configure-rem-11178-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/configure-rem-11178-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cnclst.png parame

### _Configure REM-11178 VI

Configures a Remote I/O module.

[IMAGE alt='icon' src='configure-rem-11178-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. parameters — parameters specifies the parameter information of the Remote I/O module. substitute value on error — substitute value on error specifies the output value behavior in case of a communication failure or bus reset. actuator detection — report "actuator supply not present" message? specifies whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. SDO abort code — SDO abort code returns the SDO abort code from the Remote I/O slave if an SDO write is aborted. negative confirmation — error code — additional error code — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| substitute value on error — substitute value on error specifies the output value behavior in case of a communication failure or bus reset. actuator detection — report "actuator supply not present" message? specifies whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. |
| error code — additional error code — |

Parent topic:

Configure Module VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11100-vi.html language=enus -->
## TOPIC 00112: _Read Config REM-11100 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11100-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11100-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11100 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11100-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters for channels — parameters for channels returns parameters for channels of the Remote I/O module. channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. mean-value — mean-value returns the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range returns the voltage range that the channel measures. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. mean-value — mean-value returns the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range returns the voltage range that the channel measures. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11102-vi.html language=enus -->
## TOPIC 00113: _Read Config REM-11102 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11102-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11102-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11102 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11102-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters for channels — parameters for channels returns parameters for channels of the Remote I/O module. channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. mean-value — mean-value returns the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range returns the current range that the channel measures. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. mean-value — mean-value returns the number of samples that the channel uses to calculate the mean sample value. measuring range — measuring range returns the current range that the channel measures. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11115-vi.html language=enus -->
## TOPIC 00114: _Read Config REM-11115 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11115-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11115-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11115 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11115-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters for channels — parameters for channels returns parameters for channels of the Remote I/O module. channel number — channel number returns the number of the channel in the Remote I/O module. output range — output range returns the output voltage or current range of the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel number — channel number returns the number of the channel in the Remote I/O module. output range — output range returns the output voltage or current range of the channel. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11120-vi.html language=enus -->
## TOPIC 00115: _Read Config REM-11120 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11120-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11120-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11120 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11120-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters — parameters returns the mounting position and channel information of the Remote I/O module. mounting position — mounting position returns the mounting position of the Remote I/O module. parameters for channels — parameters for channels returns parameters for channels of the Remote I/O module. channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. cold junction type — cold junction type returns the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution returns the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type returns the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| mounting position — mounting position returns the mounting position of the Remote I/O module. parameters for channels — parameters for channels returns parameters for channels of the Remote I/O module. channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. cold junction type — cold junction type returns the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution returns the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type returns the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. |
| channel number — channel number returns the number of the channel in the Remote I/O module. input filter time — input filter time returns the sampling frequency of the channel. cold junction type — cold junction type returns the type of cold junction that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about cold junctions. resolution — resolution returns the smallest change of temperature or voltage that the Remote I/O module can detect. sensor type — sensor type returns the type of sensor that connects to the Remote I/O module. Refer to the NI REM-11120 Datasheet for detailed information about sensors. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11152-vi.html language=enus -->
## TOPIC 00116: _Read Config REM-11152 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11152-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11152-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11152 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11152-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. input filter time — input filter time returns the sampling period of the Remote I/O module. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11154-vi.html language=enus -->
## TOPIC 00117: _Read Config REM-11154 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11154-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11154-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11154 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11154-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. input filter time — input filter time returns the sampling period of the Remote I/O module. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11175-vi.html language=enus -->
## TOPIC 00118: _Read Config REM-11175 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11175-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11175-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11175 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11175-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters — parameters returns the parameter information of the Remote I/O module. substitute value on error — substitute value on error returns the output value behavior in case of a communication failure or bus reset. report "actuator supply not present" message? — report "actuator supply not present" message? returns whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| substitute value on error — substitute value on error returns the output value behavior in case of a communication failure or bus reset. report "actuator supply not present" message? — report "actuator supply not present" message? returns whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/read-config-rem-11178-vi.html language=enus -->
## TOPIC 00119: _Read Config REM-11178 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/read-config-rem-11178-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/read-config-rem-11178-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon Inputs/Outputs cgenclassrntag.png slave reference in slave reference in specifies the reference to the Remote I/O slave. cu8.png module slot index module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. cerrcode

### _Read Config REM-11178 VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-config-rem-11178-vi.png']

#### Inputs/Outputs

| slave reference in — slave reference in specifies the reference to the Remote I/O slave. module slot index — module slot index specifies the slot index of the Remote I/O module. The slot index starts from 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference out — slave reference out returns the reference to the Remote I/O slave. parameters — parameters returns the parameter information of the Remote I/O module. substitute value on error — substitute value on error returns the output value behavior in case of a communication failure or bus reset. report "actuator supply not present" message? — report "actuator supply not present" message? returns whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| substitute value on error — substitute value on error returns the output value behavior in case of a communication failure or bus reset. report "actuator supply not present" message? — report "actuator supply not present" message? returns whether the Remote I/O module reports the "actuator supply not present" error message to the real-time controller. |

Parent topic:

Read Module Config VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/scale-rem-11100-vi.html language=enus -->
## TOPIC 00120: _Scale REM-11100 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/scale-rem-11100-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/scale-rem-11100-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages conversion between raw data and scaled data. icon Inputs/Outputs cu16.png raw data raw data specifies the process data input value. cu8.png measuring range measuring range specifies the voltage range that the VI uses to calculate scaled data from raw data. cerrcodeclst.png error in (no error

### _Scale REM-11100 VI

Manages conversion between raw data and scaled data.

[IMAGE alt='icon' src='scale-rem-11100-vi.png']

#### Inputs/Outputs

| raw data — raw data specifies the process data input value. measuring range — measuring range specifies the voltage range that the VI uses to calculate scaled data from raw data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. scaled data — scaled data returns the measured value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scale VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/scale-rem-11102-vi.html language=enus -->
## TOPIC 00121: _Scale REM-11102 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/scale-rem-11102-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/scale-rem-11102-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages conversion between raw data and scaled data. icon Inputs/Outputs cu16.png raw data raw data specifies the process data input value. cu8.png measuring range measuring range specifies the current range that the VI uses to calculate raw data from scaled data. cerrcodeclst.png error in (no error

### _Scale REM-11102 VI

Manages conversion between raw data and scaled data.

[IMAGE alt='icon' src='scale-rem-11102-vi.png']

#### Inputs/Outputs

| raw data — raw data specifies the process data input value. measuring range — measuring range specifies the current range that the VI uses to calculate raw data from scaled data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. scaled data — scaled data returns the measured value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scale VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/scale-rem-11115-vi.html language=enus -->
## TOPIC 00122: _Scale REM-11115 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/scale-rem-11115-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/scale-rem-11115-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages conversion between raw data and scaled data. icon Inputs/Outputs cdbl.png scaled data scaled data specifies the measured value. cu8.png output range output range specifies the output voltage or current range that the VI uses to calculate raw data from scaled data. cerrcodeclst.png error in (

### _Scale REM-11115 VI

Manages conversion between raw data and scaled data.

[IMAGE alt='icon' src='scale-rem-11115-vi.png']

#### Inputs/Outputs

| scaled data — scaled data specifies the measured value. output range — output range specifies the output voltage or current range that the VI uses to calculate raw data from scaled data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. raw data — raw data returns the process data input value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scale VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/internal/scale-rem-11120-vi.html language=enus -->
## TOPIC 00123: _Scale REM-11120 VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/internal/scale-rem-11120-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/internal/scale-rem-11120-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages conversion between raw data and scaled data. icon Inputs/Outputs cu16.png raw data raw data specifies the process data input value. cu8.png resolution resolution specifies the smallest change of temperature or voltage that the Remote I/O module can detect. cbool.png voltage measurement mode?

### _Scale REM-11120 VI

Manages conversion between raw data and scaled data.

[IMAGE alt='icon' src='scale-rem-11120-vi.png']

#### Inputs/Outputs

| raw data — raw data specifies the process data input value. resolution — resolution specifies the smallest change of temperature or voltage that the Remote I/O module can detect. voltage measurement mode? — voltage measurement mode? specifies whether the VI calculates scaled value in voltage measurement mode. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. scaled data — scaled data returns the measured value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scale VI

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/open-slave-vi.html language=enus -->
## TOPIC 00124: Open Slave VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/open-slave-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/open-slave-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the Remote I/O slave. icon Inputs/Outputs cu32.png master id slave position address specifies the position address of the Remote I/O slave. The position address starts from 0. cu16.png slave station address cerrcodeclst.png error in (no error) error in describes error conditions

### Open Slave VI

Opens a reference to the Remote I/O slave.

[IMAGE alt='icon' src='open-slave-vi.png']

#### Inputs/Outputs

| master id — slave position address specifies the position address of the Remote I/O slave. The position address starts from 0. slave station address — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. slave reference — slave reference returns the reference to the Remote I/O slave. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/read-module-config-vi.html language=enus -->
## TOPIC 00125: Read Module Config VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/read-module-config-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/read-module-config-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads parameters of a Remote I/O module. icon

### Read Module Config VI

Reads parameters of a Remote I/O module.

[IMAGE alt='icon' src='read-module-config-vi.png']

- [_Read Config REM-11100 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11100-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11102 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11102-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11115 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11115-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11120 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11120-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11152 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11152-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11154 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11154-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11175 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11175-vi.html) Reads parameters of a Remote I/O module.
- [_Read Config REM-11178 VI](../../../vi-lib/indcomecat/remote-io/internal/read-config-rem-11178-vi.html) Reads parameters of a Remote I/O module.

Parent topic:

Remote I/O

<!--NI_TOPIC bundle=ecat-labview-api-ref path=vi-lib/indcomecat/remote-io/scale-vi.html language=enus -->
## TOPIC 00126: Scale VI

- bundle_id: `ecat-labview-api-ref`
- source_path: `vi-lib/indcomecat/remote-io/scale-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecat-labview-api-ref/raw/resource/enus/vi-lib/indcomecat/remote-io/scale-vi.html
- document_id: `ecat-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages conversion between raw data and scaled data. icon

### Scale VI

Manages conversion between raw data and scaled data.

[IMAGE alt='icon' src='scale-vi.png']

- [_Scale REM-11100 VI](../../../vi-lib/indcomecat/remote-io/internal/scale-rem-11100-vi.html) Manages conversion between raw data and scaled data.
- [_Scale REM-11102 VI](../../../vi-lib/indcomecat/remote-io/internal/scale-rem-11102-vi.html) Manages conversion between raw data and scaled data.
- [_Scale REM-11115 VI](../../../vi-lib/indcomecat/remote-io/internal/scale-rem-11115-vi.html) Manages conversion between raw data and scaled data.
- [_Scale REM-11120 VI](../../../vi-lib/indcomecat/remote-io/internal/scale-rem-11120-vi.html) Manages conversion between raw data and scaled data.

Parent topic:

Remote I/O
