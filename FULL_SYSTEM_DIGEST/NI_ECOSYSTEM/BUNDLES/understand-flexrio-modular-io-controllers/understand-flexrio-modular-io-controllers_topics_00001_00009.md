# NI DOCUMENT BUNDLE: understand-flexrio-modular-io-controllers

<!--NI_BUNDLE_CHUNK bundle=understand-flexrio-modular-io-controllers start=1 end=9 -->
<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=base-clk.html language=enus -->
## TOPIC 00001: Base Clock Resources for FlexRIO Modular I/O Controllers

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `base-clk.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/base-clk.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: A base clock is a digital signal existing in hardware that you can use as a clock for an FPGA application. Your FlexRIO with Modular I/O Controller provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock, the 100 MHz clock, and the 200 MHz clock are

Base Clock Resources for FlexRIO Modular I/O
 Controllers

A base clock is a digital signal existing in hardware that you
 can use as a clock for an FPGA application.

Your FlexRIO with Modular I/O Controller provides several base clock resources
 that can be used to run a LabVIEW FPGA VI. The 40 MHz
 onboard clock, the 100 MHz clock, and the 200 MHz clock are generated within the device FPGA
 using a PLL.

The following base clock resources are available for FlexRIO with Modular I/O
 Controllers.

40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. You can use this clock as a top-level clock to run your LabVIEW FPGA VI. The top-level clock on an FPGA target determines the execution time of the individual functions and VIs on the FPGA VI block diagram. If you change the frequency of the top-level clock, you also change the execution speed of functions on the block diagram and the execution rate of the FPGA VI.

100 MHz Clock

You can use the 100 MHz Clock as a source for running your LabVIEW FPGA VI. The 100 MHz Clock is generated from a PLL in the module.

200 MHz Clock

You can use the 200 MHz Clock as a source for running your LabVIEW FPGA VI. The 200 MHz Clock is generated from a PLL in the module.

10 MHz Reference Clock

The device derives its 10 MHz Reference Clock
 from an internal oscillator. For information about how to configure the 10 MHz Reference Clock, refer to the user manual.

DRAM Clock

The DRAM Clock is a 166 MHz clock that drives the DRAM interface.

MGT Reference Clock

The MGT Reference Clock is a user-selectable clock that drives the
 multi-gigabit transceiver (MGT) interface. Selectable values are 156.25 MHz and 312.5 MHz.

Note

#### NI-7931 Base Clock Routing

The following figure shows the clock routing for the NI-7931 base clocks.

[IMAGE alt='1378' src='GUID-638855B2-FED9-404D-9AD4-2B95FA26CBFC-a5.svg']

#### NI-7932 and NI-7935 Base Clock
 Routing

The following figure shows the clock routing for the NI-7931 base clocks.

[IMAGE alt='1378' src='GUID-7B0BEF28-F64A-4724-99DA-F4B6065C7D29-a5.svg']

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=fpga-io.html language=enus -->
## TOPIC 00002: Adding FPGA I/O to your LabVIEW Project

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `fpga-io.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/fpga-io.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: To add FPGA I/O to your LabVIEW Project, right-click the FPGA target and select NewFPGA I/O.

Adding FPGA I/O to your LabVIEW
 Project

To add FPGA I/O to your LabVIEW Project, right-click the FPGA target and select New»FPGA I/O.

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=front-panel-io.html language=enus -->
## TOPIC 00003: Front Panel I/O

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `front-panel-io.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/front-panel-io.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Front Panel I/O signals to configure the front panel connectors.Front Panel I/O ItemsFront Panel I/O ItemDescriptionaTrigReadDataReturns the value of the TRIG front panel connector. aTrigWriteData Drives the TRIG front panel connector when aTrigWriteEnable is set to True.aTrigWriteEnable Dri

Front Panel I/O

| Front Panel I/O Item | Description |
| --- | --- |
| aTrigReadData | Returns the value of the TRIG front panel connector. |
| aTrigWriteData | Drives the TRIG front panel connector when aTrigWriteEnable is set to True. |
| aTrigWriteEnable | Drives the aTrigWriteData signal out of the TRIG front panel connector. |
| ReferenceClk10 | Controls the 10 MHz Reference Clock. Refer to the device user manual for the clocking diagram. |
| UserLed1 | Controls the LED indicator on the front panel. Refer to the device user manual for detailed information about the LED indicator. |

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=leds.html language=enus -->
## TOPIC 00004: Explanation of LED Indicators on FlexRIO Modular I/O Controllers

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `leds.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/leds.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following figure shows the LEDs in more detail. LEDs LED Indicator Status LED State Indication POWER Lit Controller is powered. Off Controller is not powered. STATUS 2 flashes every few seconds There is no software installed, which is the out-of-box state, or the controller has detected an error

Explanation of LED Indicators on FlexRIO
 Modular I/O Controllers

The following figure shows the LEDs in more detail.

Figure 1.

[IMAGE alt='1378' src='GUID-A499339F-9BEE-44D8-B4C1-496922EE2C1E-a5.svg']

| LED | State | Indication |
| --- | --- | --- |
| POWER | Lit | Controller is powered. |
| Off | Controller is not powered. |  |
| STATUS | 2 flashes every few seconds | There is no software installed, which is the out-of-box state, or the controller has detected an error in its software. An error can occur when an attempt to upgrade the software is interrupted. Refer to the MAX Help for information about reinstalling software on the controller. |
| 3 flashes every few seconds | The controller is in safe mode. Refer to the MAX Help for information about safe mode. |  |
| 4 flashes every few seconds | The software has crashed twice without rebooting or cycling power between crashes. This usually occurs when the controller runs out of memory. Review your RT VI and check the memory usage. Modify the VI as necessary to solve the memory usage issue. |  |
| Continuously flashing | The controller has not booted into NI Linux Real-Time. The controller has either booted into an unsupported operating system, was interrupted during the boot process, or detected an unrecoverable software error.Or, this indicates a hardware error. An internal power supply has failed. Check front-panel I/O and adapter modules connections for shorts. Remove any shorts and power cycle the controller. If the problem persists, contact NI. |  |
| Lit, solid | The controller is booting up. |  |
| Off | Normal operation. |  |
| FPGA USER LED | — | The FPGA USER LED is a green LED that is controlled directly from the LabVIEW FPGA diagram. To control this LED, use an FPGA I/O node on your FPGA diagram. Refer to the LabVIEW Help for information about programming this LED. |
| RT USER LED | — | The RT USER LED is a green LED that is controlled directly from your LabVIEW Real-Time application. You can define the RT USED LED to meet the needs of your application. To define this LED, use the Real-Time LED VIs in LabVIEW. For more information about the Real-Time LED VIs, refer to the LabVIEW Help. |

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=pinout.1.html language=enus -->
## TOPIC 00005: NI-7932 Front Panel Connector Descriptions

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `pinout.1.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/pinout.1.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following figure shows the front panel connectors, buttons, and LEDs. TRIG REF IN µSD card USB device port USB host 1 Gigabit Ethernet LED indicators Reset DC power source FlexRIO adapter module connector SFP+ connectors Front Panel Connectors Connector Function SFP+ connectors Allow access to t

NI-7932 Front Panel Connector
 Descriptions

The following figure shows the front
 panel connectors, buttons, and LEDs.

[IMAGE alt='1378' src='GUID-99C2E169-D230-4514-95CA-A5467CE8169A-a5.svg']

1. TRIG
2. REF IN
3. µSD card
4. USB device port
5. USB host
6. 1 Gigabit Ethernet
7. LED indicators
8. Reset
9. DC power source
10. FlexRIO adapter module connector
11. SFP+ connectors

| Connector | Function |
| --- | --- |
| SFP+ connectors | Allow access to the multi-gigabit transceivers (MGTs). |
| TRIG | Trigger input and output channel. |
| REF IN | Reference clock input. |
| µSD card | SD card slot that can read from and write to DC cards. Use an NI-approved SD card to improve the performance and memory integrity of the controller. |
| USB device port | Intended for use in device configuration, application deployment, debug, and maintenance. |
| USB host | Supports common USB mass-storage devices such as USB Flash drives. |
| 1 Gigabit Ethernet | Ethernet port. |
| Reset | Pressing the RESET button resets the processor in the same manner as cycling power.You can also use the RESET button to troubleshoot network connectivity. Refer to the MAX Help for FlexRIO for more information about troubleshooting network issues. |
| DC power source | Refer to the NI-7932 Getting Started Guide for information about wiring power to the device. |
| FlexRIO adapter module connector | Refer to the NI-7932 Getting Started Guide for information about the NI-7932 adapter module connector pinout. |

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=pinout.2.html language=enus -->
## TOPIC 00006: NI-7932 Front Panel

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `pinout.2.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/pinout.2.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following figure shows the front panel connectors, buttons, and LEDs. TRIG REF IN µSD card USB device port USB host 1 Gigabit Ethernet LED indicators Reset DC power source FlexRIO adapter module connector SFP+ connectors Front Panel Connectors Connector Function SFP+ connectors Allow access to t

NI-7932 Front Panel

The following figure shows the front
 panel connectors, buttons, and LEDs.

[IMAGE alt='1378' src='GUID-99C2E169-D230-4514-95CA-A5467CE8169A-a5.svg']

1. TRIG
2. REF IN
3. µSD card
4. USB device port
5. USB host
6. 1 Gigabit Ethernet
7. LED indicators
8. Reset
9. DC power source
10. FlexRIO adapter module connector
11. SFP+ connectors

| Connector | Function |
| --- | --- |
| SFP+ connectors | Allow access to the multi-gigabit transceivers (MGTs). |
| TRIG | Trigger input and output channel. |
| REF IN | Reference clock input. |
| µSD card | SD card slot that can read from and write to DC cards. Use an NI-approved SD card to improve the performance and memory integrity of the controller. |
| USB device port | Intended for use in device configuration, application deployment, debug, and maintenance. |
| USB host | Supports common USB mass-storage devices such as USB Flash drives. |
| 1 Gigabit Ethernet | Ethernet port. |
| Reset | Pressing the RESET button resets the processor in the same manner as cycling power.You can also use the RESET button to troubleshoot network connectivity. Refer to the MAX Help for FlexRIO for more information about troubleshooting network issues. |
| DC power source | Refer to the NI-7932 Getting Started Guide for information about wiring power to the device. |
| FlexRIO adapter module connector | Refer to the NI-7932 Getting Started Guide for information about the NI-7932 adapter module connector pinout. |

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=pinout.html language=enus -->
## TOPIC 00007: NI-7935 Front Panel Connector Descriptions

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/pinout.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following figure shows the NI-7935 front panel connectors, buttons, and LEDs. NI-7935 TRIG REF CLK Storage (µSD card) USB device port USB host 1 Gigabit Ethernet LED indicators Reset DC power source FlexRIO adapter module connector Port 0/Port 1 (SFP+ connectors) Front Panel Connectors Connector

NI-7935 Front Panel Connector
 Descriptions

The following figure shows the NI-7935 front panel connectors, buttons, and LEDs.

Figure 2.

[IMAGE alt='1378' src='GUID-99C2E169-D230-4514-95CA-A5467CE8169A-a5.svg']

1. TRIG
2. REF CLK
3. Storage (µSD card)
4. USB device port
5. USB host
6. 1 Gigabit Ethernet
7. LED indicators
8. Reset
9. DC power source
10. FlexRIO adapter module connector
11. Port 0/Port 1 (SFP+ connectors)

| Connector | Function |
| --- | --- |
| SFP+ connectors | Allow access to the multi-gigabit transceivers (MGTs). |
| TRIG | Trigger input and output channel. |
| REF IN | Reference clock input. |
| µSD card | SD card slot that can read from and write to DC cards. Use an NI-approved SD card to improve the performance and memory integrity of the controller. |
| USB device port | Intended for use in device configuration, application deployment, debug, and maintenance. |
| USB host | Supports common USB mass-storage devices such as USB Flash drives. |
| 1 Gigabit Ethernet | Ethernet port. |
| Reset | Pressing the RESET button resets the processor in the same manner as cycling power.You can also use the RESET button to troubleshoot network connectivity. Refer to the MAX Help for FlexRIO for more information about troubleshooting network issues. |
| DC power source | Refer to the NI-7931 Getting Started Guide for information about wiring power to the NI-7931. |
| FlexRIO adapter module connector | Refer to the NI-7931 Getting Started Guide for information about the NI-7931 adapter module connector pinout. |

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=reference-clock-source.html language=enus -->
## TOPIC 00008: Using the External Reference Clock Input

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `reference-clock-source.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/reference-clock-source.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Reference Clock Source item provides the option to use the physical front panel external reference clock input on your device as the reference clock. Right-click this item and select Properties to enable or disable the front panel external reference clock in your application.

Using the External Reference Clock Input

The Reference Clock Source item provides the option to use the physical front panel
 external reference clock input on your device as the reference clock. Right-click
 this item and select Properties to enable or disable the
 front panel external reference clock in your application.

<!--NI_TOPIC bundle=understand-flexrio-modular-io-controllers path=status-items.html language=enus -->
## TOPIC 00009: Board IO FPGA I/O Items and Status Items

- bundle_id: `understand-flexrio-modular-io-controllers`
- source_path: `status-items.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-modular-io-controllers/raw/resource/enus/status-items.html
- document_id: `understand-flexrio-modular-io-controllers`
- page_type: `leaf`
- content_type: `reference`
- source_description: FPGA I/O Node You can use an FPGA I/O Node, configured for reading and writing, with your FlexRIO Modular I/O Controller. The FPGA I/O Node is located on the FPGA I/O Functions palette and performs specific FPGA I/O operations on your FPGA target. The IO Module Status terminals are synchronous to th

Board IO FPGA I/O Items and Status
 Items

Figure 3.

[IMAGE alt='1378' src='GUID-E902C285-6C4F-4BA7-8985-0EDD7D3C2224-a5.gif']

You can use an FPGA I/O Node, configured for reading and writing, with your FlexRIO
 Modular I/O Controller. The FPGA I/O Node is located on the FPGA I/O
 Functions palette and performs specific FPGA I/O operations on your
 FPGA target.

The IO Module Status terminals are synchronous to the 40 MHz clock, and they should
 be accessed through that clock domain.

You can select the following FPGA I/O items for the device.

| FPGA I/O Item | Description |
| --- | --- |
| Clock100 PLL Unlocked | Indicates if the PLL that generates the 40 MHz, 100 MHz, and 200 MHz base clocks has unlocked after the FPGA bitfile downloads. After the FPGA bitfile downloads, the PLL locks to the 100 MHz clock generated by the PLL on the baseboard. If the PLL becomes unlocked, then the FPGA attempts to relock the PLL to the 100 MHz oscillator. Refer to the device user manual for more information about the device clocking architecture.Note NI recommends that you reload the FPGA bitfile if the Clock100 PLL Unlocked status is TRUE. Xilinx does not guarantee proper PLL operation in these cases, and undesired behavior may occur. |

| FPGA I/O Item | Description |
| --- | --- |
| EEPROM Power Enabled | TRUE = Indicates that the adapter module EEPROM power rail is enabled. FALSE = Indicates that the adapter module EEPROM power rail is not enabled. |
| Expected IO Module ID | Reports the unique 32-bit IO Module ID that the currently downloaded FPGA VI is configured to use. The inserted IO Module ID must match the expected IO Module ID so the adapter module can function properly. The Expected IO Module ID is configured by choosing the appropriate adapter module in the IO Module General Properties dialog box and then recompiling and redownloading the FPGA VI. |
| Inserted IO Module ID | Reports the unique 32-bit IO module ID of the currently inserted adapter module. The Inserted IO Module ID must match the expected IO Module ID for the adapter module to function properly. |
| IO Module IO Enabled | TRUE = Indicates that the adapter module connector FPGA I/O pins are enabled. FALSE = Indicates that the adapter module connector FPGA I/O pins are not enabled. Note These pins are enabled only when an adapter module is connected, properly powered, and when the FPGA has determined that the connected adapter module is compatible with the FPGA VI currently downloaded to the FPGA. |
| IO Module Power Enabled | TRUE = Indicates that the adapter module power is fully enabled. FALSE = Indicates that the adapter module power is not enabled. Note Adapter module power is enabled only when an adapter module is connected and the FPGA has determined that the connected adapter module is compatible with the program currently downloaded to the FPGA. |
| IO Module Power Good | Reports the state of the power good signal on the adapter module connector interface. TRUE = Indicates that the connected adapter module power rails have had the proper amount of time to initialize and are operational and stable. FALSE = Indicates that the connected adapter module power rails are not ready. |
| IO Module Present | TRUE = Indicates that an adapter module is physically connected to the FPGA module. FALSE = Indicates that an adapter module is not connected to the FPGA module. |

#### Invoke Method Functions

[IMAGE alt='1378' src='GUID-589D0C45-4D20-4B58-AF4B-485251E71C70-a5.gif']

You can also use an Invoke Method function to invoke an action
 from the host VI to the FPGA VI your FlexRIO Modular I/O Controller. The host VI is
 available from the LabVIEW FPGA host interface. The Invoke Method function is
 located on the FPGA Interface VIs and Functions
 palette.

In addition to the standard methods supported by the LabVIEW FPGA
 Module, FlexRIO targets also support the following custom FPGA Invoke
 methods.

| Interface Methods | Description |
| --- | --- |
| Control IO Module Power | Enables or disables power to the connected adapter module. You must physically insert an adapter module into the FPGA module to run this method. Enabled TRUE = Enables power to the adapter module. FALSE = Disables power to the adapter module. |
| IO Module Status | Queries status information about the FlexRIO adapter module interface. You do not need to physically insert an adapter module in the FlexRIO system to run this method. IO Module Present? TRUE = Indicates that an adapter module is physically inserted in the FlexRIO system. FALSE = Indicates that no adapter module is inserted. Power Enabled? TRUE = Indicates that power to the adapter module is enabled. FALSE = Indicates that power to the adapter module is disabled. I/O Enabled? TRUE = Indicates that FPGA GPIO pin buffers on the adapter module interface are enabled. FALSE = Indicates that FPGA GPIO pin buffers are disabled. IO Module Mismatch? TRUE = Indicates that the currently downloaded FPGA VI is expecting to use a different adapter module than that which is currently inserted. In this case, power and I/O to the adapter module is disabled. To use the currently inserted adapter module with your FPGA program, configure your LabVIEW project to use the currently inserted adapter module, recompile your VI, and redownload it to the FPGA. FALSE = Indicates that the currently downloaded FPGA VI is compatible with the current adapter module. |
| Redetect IO Module | Redetects the adapter module that is currently connected to the FlexRIO FPGA module. You must physically insert an adapter module in the FlexRIO FPGA module to run this method. Note This method is only necessary when creating a custom adapter module. |
