# NI DOCUMENT BUNDLE: understand-high-speed-serial-instrument-features

<!--NI_BUNDLE_CHUNK bundle=understand-high-speed-serial-instrument-features start=1 end=9 -->
<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=access-labview-examples-high-speed-serial.html language=enus -->
## TOPIC 00001: Accessing LabVIEW Example Projects for High-Speed Serial Instruments

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `access-labview-examples-high-speed-serial.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/access-labview-examples-high-speed-serial.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `task`
- source_description: The LabVIEW Instrument Design Libraries for High Speed Serial Instruments driver includes example projects to get you started designing for NI High-Speed Serial Instruments. Complete the following steps to access the example projects: Open LabVIEW and select Create Project. In the Create Project dia

Accessing LabVIEW Example Projects for
 High-Speed Serial Instruments

The LabVIEW Instrument Design
 Libraries for High Speed Serial Instruments driver includes example projects to get you
 started designing for NI High-Speed Serial Instruments. Complete the following steps to
 access the example projects:

1. Open LabVIEW and select Create Project.
2. In the Create Project dialog box, select
 High-Speed Serial and select an example project for
 your device.
3. Click Next.
4. Configure the Project Name, Project
 Root, and File Name Prefix (Optional)
 fields.
5. Click Finish.

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=base-clock-resources-high-speed-serial.html language=enus -->
## TOPIC 00002: Base Clock Resources for High-Speed Serial Instruments

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `base-clock-resources-high-speed-serial.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/base-clock-resources-high-speed-serial.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: A base clock is a digital signal existing in hardware that you can use as a clock for an FPGA application. Use the FPGA Base Clock Properties dialog box to configure your base clock. Your High-Speed Serial Instrument provides several base clock resources that you can use to run a LabVIEW FPGA VI. Th

Base Clock Resources for High-Speed Serial
 Instruments

A base clock is a digital signal existing
 in hardware that you can use as a clock for an FPGA application.

Use the FPGA Base Clock
 Properties dialog box to configure your base clock.

| Base Clock | Description |
| --- | --- |
| 40 MHz Onboard Clock | The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. You can use this clock as a top-level clock for running your LabVIEW FPGA VI. The top-level clock on an FPGA target determines the execution time of the individual functions and VIs on the FPGA VI block diagram. If you change the frequency of the top-level clock, you also change the execution speed of functions on the block diagram and the execution rate of the FPGA VI. |
| PXI_CLK10 | You can use PXI_CLK10 as a source for running your LabVIEW FPGA VI. |
| 200 MHz Clock | You can use the 200 MHz Clock as a source for running your LabVIEW FPGA VI. The PLL in the PXIe-6592R generates the 200 MHz Clock. |
| PXIe_DStarA | Configure this clock to the frequency of your choice for running your LabVIEW FPGA VI. You can drive the PXIe_DStarA using a timing and synchronization device. |
| PXIe_Clk100 | PXIe_Clk100 is a 100 MHz clock that you can use as a source for running your LabVIEW FPGA VI. The PLL in the PXIe-6592R generates the PXIe_Clk100. |
| Reserved Clock | Reserved for future use. Do not use. |

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=configuring-trigger-pulses-high-speed.html language=enus -->
## TOPIC 00003: Configuring Trigger Pulses for High-Speed Serial Instruments

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `configuring-trigger-pulses-high-speed.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/configuring-trigger-pulses-high-speed.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: To ensure compatibility with PXI Express devices, configure trigger pulses on high-speed serial modules to last for at least two clock cycles of the clock on the receiving device. For example, if the clock on the receiving device is 80 MHz, which is a clock period of 12.5 ns, the trigger line must b

Configuring Trigger Pulses for High-Speed
 Serial Instruments

Note

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=disable-sync-registers.html language=enus -->
## TOPIC 00004: Disabling Synchronization Registers for Proper DRAM Function

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `disable-sync-registers.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/disable-sync-registers.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `task`
- source_description: Because synchronization registers cause a delay in sending and receiving data or commands to and from the DRAM interface, for proper DRAM function, you must disable all synchronization registers for all DRAM interface signals and all input signals.All NI PXI version 1.1 and later CLIP items and all

Disabling Synchronization Registers for Proper
 DRAM Function

Note

1. Right-click a DRAM interface signal and select
 Properties from the shortcut menu to open the
 FPGA I/O Properties dialog box.
2. Select Advanced Code Generation in the Category list to
 open the Advanced Code Generation page.
3. Select 0 in the Number of Synchronizing Registers for
 Output Data box to disable all synchronization registers for that signal. Always
 disable synchronization registers for synchronous interfaces when proper
 operation depends on no latency.

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=fpga-io-method-nodes-use-pxie-659x.html language=enus -->
## TOPIC 00005: FPGA I/O Method Node for Use with PXIe-659x

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `fpga-io-method-nodes-use-pxie-659x.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/fpga-io-method-nodes-use-pxie-659x.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA I/O Method Node to invoke a method on an I/O item or hardware under an FPGA target. The I/O Method Node is located on the FPGA I/O Functions palette. You can use the following methods with the PXIe-6591 or PXIe-6592. Method Description Set Output Data Writes data to the digital line or

FPGA I/O Method Node for Use with
 PXIe-659*x*

[IMAGE alt='1378' src='GUID-5B769599-4901-40B2-86AE-8273351DA30C-a5.gif']

Use the FPGA I/O Method Node to invoke a method on an I/O item or hardware under an FPGA
 target. The I/O Method Node is located on the FPGA I/O
 Functions palette. You can use the following methods with the
 PXIe-6591 or PXIe-6592.

| Method | Description |
| --- | --- |
| Set Output Data | Writes data to the digital line or port without enabling the line or port. You can use the Set Output Data method to optimize performance when performing successive writes to a DIO resource. The data type of the Data input depends on the I/O item. For example, if the I/O item is a digital line, Data requires a Boolean data type. |
| Set Output Enable | Determines whether the digital input and output resource reads external input or writes output. Wiring TRUE to Set Output Enable for a digital line allows the resource to write data. Wiring FALSE to Set Output Enable allows the resource to read external data. The data type of the Enable input depends on the I/O item. For example, if the I/O item is a digital line, Enable requires a Boolean data type, and if the I/O item is an 8-bit digital port, Enable requires a U8 data type. The binary values of the U8 input correspond to the individual lines of the digital port. Zeros correspond to FALSE inputs and ones correspond to TRUE inputs. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input on this method specifies the number of FPGA clock cycles that the Wait on Any Edge method waits for the next falling or rising edge. 0 = Causes the method to timeout immediately.Negative value = Causes the method to wait indefinitely. Positive value = Causes the method to wait for that number of clock cycles before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input on this method specifies the number of FPGA clock cycles that the Wait on Falling Edge method waits for the next falling edge. 0 = Causes the method to timeout immediately.Negative value = Causes the method to wait indefinitely.Positive value = Causes the method to wait for that number of clock cycles before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input on this method specifies the number of FPGA clock cycles that the Wait on High Level method waits for the next logic high level. 0 = Causes the method to timeout immediately. Negative value = Causes the method to wait indefinitely. Positive value = Causes the method to wait for that number of clock cycles before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input on this method specifies the number of FPGA clock cycles that the Wait on Low Level method waits for the next logic low level. 0 = Causes the method to timeout immediately. Negative value = Causes the method to wait indefinitely. Positive value = Causes the method to wait for that number of clock cycles before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input on this method specifies the number of FPGA clock cycles that the Wait on Rising Edge method waits for the next rising edge. 0 = Causes the method to timeout immediately. Negative value = Causes the method to wait indefinitely. Positive value = Causes the method to wait for that number of clock cycles before timing out. |

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=pxie-659x-led-status-indicators.html language=enus -->
## TOPIC 00006: PXIe-659x LED Status Indicators

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `pxie-659x-led-status-indicators.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/pxie-659x-led-status-indicators.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: ACCESS LED Color Indication Off Instrument not yet functional Amber Instrument being accessed by software Green Instrument ready to be programmed ACTIVE LED Color Indication Off Instrument is not waiting for a trigger, bursting a pattern, or experiencing an error. Amber Instrument awaiting Start tri

PXIe-659*x* LED Status
 Indicators

| Color | Indication |
| --- | --- |
| Off | Instrument not yet functional |
| Amber | Instrument being accessed by software |
| Green | Instrument ready to be programmed |

| Color | Indication |
| --- | --- |
| Off | Instrument is not waiting for a trigger, bursting a pattern, or experiencing an error. |
| Amber | Instrument awaiting Start trigger |
| Green | Instrument is active |
| Red | Instrument error |

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=pxie-7902-component-level-ip.html language=enus -->
## TOPIC 00007: PXIe-7902 Component-Level IP

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `pxie-7902-component-level-ip.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/pxie-7902-component-level-ip.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following signals to interface with the PXIe-7902 CLIP in LabVIEW. Signal Direction Clock Domain Description aResetSI In Async An asynchronous reset signal from the LabVIEW FPGA environment. This signal is not required. If you create an input signal to your CLIP wizard, that signal is driven

PXIe-7902 Component-Level IP

Use the following signals to interface
 with the PXIe-7902 CLIP in LabVIEW.

| Signal | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| aResetSI | In | Async | An asynchronous reset signal from the LabVIEW FPGA environment. This signal is not required. If you create an input signal to your CLIP wizard, that signal is driven as an asynchronous reset signal. Reset all CLIP state machines and logic whenever this signal is logic high. This signal is driven high when you call the LabVIEW FPGA Reset invoke method. Call Run on the FPGA VI to deassert this signal. Do not use CLIP inputs from the LabVIEW FPGA VI in the CLIP until aResetSI is deasserted. |
| UserClk | Out | — | Parallel clock shared by the core and the user application. |
| Clock40 | In | — | A 40 MHz clock that runs continuously regardless of connectivity. |
| cPort<0..5>_PMA_Init | In | Clock40 | Reinitializes the transceiver that the corresponding Aurora core is connected to. |
| uPort<0..5>_s_axi_tx_tdata_0 | In | UserClk | 64-bit wide Boolean array that provides data to lane 0 of the corresponding port. |
| uPort<0..5>_s_axi_tx_tdata_1 | In | UserClk | 64-bit wide Boolean array that provides data to lane 1 of the corresponding port. |
| uPort<0..5>_s_axi_tx_tdata_2 | In | UserClk | 64-bit wide Boolean array that provides data to lane 2 of the corresponding port. |
| uPort<0..5>_s_axi_tx_tdata_3 | In | UserClk | 64-bit wide Boolean array that provides data to lane 3 of the corresponding port. |
| uPort<0..5>_s_axi_tx_tdata_tvalid | In | UserClk | Indicates whether the data provided to the AXI interface is valid. |
| uPort<0..5>_s_axi_tx_tdata_tready | Out | UserClk | Specifies whether the AXI interface is ready for addition data in the next clock cycle. |
| uPort<0..5>_m_axi_rx_tdata_0 | Out | UserClk | 64-bit wide Boolean array from the AXI interface on the corresponding port. |
| uPort<0..5>_m_axi_rx_tdata_1 | Out | UserClk | 64-bit wide Boolean array from the AXI interface on the corresponding port. |
| uPort<0..5>_m_axi_rx_tdata_2 | Out | UserClk | 64-bit wide Boolean array from the AXI interface on the corresponding port. |
| uPort<0..5>_m_axi_rx_tdata_3 | Out | UserClk | 64-bit wide Boolean array from the AXI interface on the corresponding port. |
| uPort<0..5>_m_axi_rx_tdata_tvalid | Out | UserClk | Indicates that data received from RX data lines is valid for that clock cycle. |
| uPort<0..5>_HardError | Out | UserClk | Indicates that a buffer overflow or underflow internal to the Aurora core has occurred. The core automatically resets and re-initializes when a hard error occurs. Refer to the Xilinx Aurora 64B/66B Vivado Design Guide (PG 074) for more information about soft errors. |
| uPort<0..5>_SoftError | Out | UserClk | Indicates that too many soft errors have occurred. Refer to the Xilinx Aurora 64B/66B Vivado Design Guide (PG 074) for more information about soft errors. |
| uPort<0..5>_LaneUp | Out | UserClk | Indicates that the corresponding lanes in the ports are functional. |
| uPort<0..5>_ChannelUp | Out | UserClk | Indicates that a link has been established on the corresponding port. |
| uPort<0..5>_sys_reset_out | Out | UserClk | System reset output to be used by the example design level logic. |
| cPort<0..5>_link_reset_out | Out | Clock40 | Driven High if the hot-plug count expires. |
| s_aclk | In | Clock40 | AXI clock provided by LabVIEW. |
| s_axi_awaddr | In | Clock40 | AXI4-Lite Write address for DRP. |
| s_axi_awvalid | In | Clock40 | Indicates that the write address is valid. |
| s_axi_awready | Out | Clock40 | Indicates that the write address is ready. |
| s_axi_wdata | In | Clock40 | Write data for DRP. |
| s_axi_wvalid | In | Clock40 | Indicates that the write data is valid. |
| s_axi_wready | Out | Clock40 | Indicates that the write data is ready. |
| s_axi_wstrb | In | Clock40 | Write data strobe. |
| s_axi_bvalid | Out | Clock40 | Indicates that the write response is valid. |
| s_axi_bready | In | Clock40 | Indicates that the write data is ready. |
| s_axi_bresp | Out | Clock40 | Write response. |
| s_axi_araddr | In | Clock40 | AXI4-Lite Read address for DRP. |
| s_axi_arvalid | In | Clock40 | Indicates that the read address is valid. |
| s_axi_arready | Out | Clock40 | Indicates that the read address is ready. |
| s_axi_rdata | Out | Clock40 | Read data. |
| s_axi_rvalid | Out | Clock40 | Indicates that the read data is valid. |
| s_axi_rready | In | Clock40 | Indicates that the read data is ready. |
| s_axi_rresp | Out | Clock40 | Read response. |
| MgtRefClks_Locked | Out | — | Indicates the state of the FPGA multi-gigabit transceivers (MGTs). |
| MgtRefClks_Valid | Out | — | Indicates whether the selected clock input to the clocking logic is valid. |
| sFrontEndConfig_Complete | Out | — | Asserts high and stays high when the power-on self-configuration (POSC) state machine is finished with configuration. After the aResetSI signal transitions from high to low, indicating that the CLIP logic should come out of a reset, a POSC reconfiguration occurs unconditionally. The required clocking signals are not valid until after this signal asserts high. |

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=pxipxi-express-fpga-io-items-high-speed.html language=enus -->
## TOPIC 00008: PXI/PXI Express FPGA I/O Items for High-Speed Serial Instruments

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `pxipxi-express-fpga-io-items-high-speed.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/pxipxi-express-fpga-io-items-high-speed.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use an FPGA I/O Node, configured for reading and writing, with your High-Speed Serial Instrument. The FPGA I/O Node is located on the FPGA I/O Functions palette and performs specific FPGA I/O operations on your FPGA target. Refer to the tables below to determine which PXI/PXI Express FPGA I/

PXI/PXI Express FPGA I/O Items for
 High-Speed Serial Instruments

[IMAGE alt='1378' src='GUID-0DDF3D0F-C0A5-401D-93CF-0DDDDDEEBCC5-a5.gif']

You can use an FPGA I/O Node, configured for reading and writing, with your
 High-Speed Serial Instrument. The FPGA I/O Node is located on the FPGA
 I/O Functions palette and performs specific FPGA I/O operations on
 your FPGA target.

Refer to the tables below to determine which PXI/PXI Express FPGA I/O items you can
 select for your High-Speed Serial Instrument.

| FPGA I/O Item | Description |
| --- | --- |
| PXI_Trigx | Controls PXI trigger channel x, where x is a PXI trigger number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable methods to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module for proper device functionality. |
| PXI_CLK10 | Controls the 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI_Star | Controls the PXI star trigger line. Use an FPGA I/O Node configured for reading to access this channel. |

| Terminal | Description |
| --- | --- |
| PXIe_DStarB | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXIe_DStarC | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXIe_Sync100 | Controls the reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |

#### Board I/O Items

| Board I/O Item | Description |
| --- | --- |
| Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the high-speed serial module PCB, external to the FPGA. In this format, the device temperature is given by the following equation:Device Temperature = (Returned Device Temperature Decimal Value)/4 For example, a Returned Device Temperature Decimal Value of 120 indicates a Device Temperature of 30 °C. |

| Board I/O Item | Description |
| --- | --- |
| Device Temperature | Returns the current temperature of the device, in increments of 0.01 °C. The temperature is measured from an on-die temperature on the FPGA. This signal is an I16 data type that you must access in the 40 MHz onboard clock domain. |
| PLL Unlocked | A TRUE value indicates that either the DRAM controller PLL is failing to lock, or the PLL is not locking to the PXIeClk100. PXIeClk100 generates the core 200 MHz, 100 MHz, and 40 MHz clocks. This signal is sticky, meaning that a single unlock occurrence keeps the signal asserted. |
| 12V Power | Indicates power, in cW, consumed by the 12V power rail. The 12V power rail supplies power to the FPGA core and the MGTs. This signal is a U16 data type that you must access in the 40 MHz onboard clock domain. |
| 3.3V Power | Indicates power, in cW, consumed by the 3.3V power rail. The 3.3V power rail supplies power to the DRAM and various device components. This signal is a U16 data type that you must access in the 40 MHz onboard clock domain. |
| Optical Power | Indicates power, in cW, consumed by the optical power supply. The optical power supply provides power to the mini-SAS HD front panel connectors when optical power is enabled. This signal is a U16 data type that you must access in the 40 MHz onboard clock domain. |

<!--NI_TOPIC bundle=understand-high-speed-serial-instrument-features path=reserving-releasing-trigger-lines-high.html language=enus -->
## TOPIC 00009: Reserving and Releasing Trigger Lines for High-Speed Serial Modules

- bundle_id: `understand-high-speed-serial-instrument-features`
- source_path: `reserving-releasing-trigger-lines-high.html`
- source_url: https://docs-be.ni.com/bundle/understand-high-speed-serial-instrument-features/raw/resource/enus/reserving-releasing-trigger-lines-high.html
- document_id: `understand-high-speed-serial-instrument-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: It's important that you reserve the trigger lines used by your high-speed serial module. Without the trigger lines reserved, two PXIe devices could try to drive the same trigger line in different applications, which could cause an application to fail, and, in some cases, cause damage to third-party

Reserving and Releasing Trigger Lines for
 High-Speed Serial Modules

It's important that you reserve the trigger lines used by your high-speed serial module. Without
 the trigger lines reserved, two PXIe devices could try to drive the same
 trigger line in different applications, which could cause an application to
 fail, and, in some cases, cause damage to third-party PXIe devices.

You can use Measurement & Automation Explorer (MAX) or the host VI to reserve
 trigger lines.

If you download and
 run the FPGA VI interactively, configure the PXI triggers in MAX. MAX maintains the
 trigger reservation for the device even after you cycle power to the PXI chassis.

If you download and run the FPGA VI programmatically, reserve the trigger lines in the host VI.
 Use the Invoke Method function to reserve the trigger and to release the
 trigger reservation. LabVIEW releases the trigger reservation for the device
 automatically when you close the FPGA VI reference. You must run the host VI
 again to reserve the trigger.

#### Reserving and Releasing Trigger Lines
 Step-by-Step

Note

Unreserve PXI Trigger

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA
 VI Reference function to the FPGA VI Reference In input
 of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference
 function to the error in input of the Invoke Method
 function.
5. Click the Invoke Method function and select Reserve PXI
 Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant. An enum constant is created to help you select the trigger. 
 org.dita.html5/xsl/topic.xsl 455Note To reserve or release
 multiple trigger lines, repeat steps 2 through 6 for each trigger line you
 want to reserve or release, wiring the FPGA VI Reference
 Out output of the existing Invoke Method function to the
 FPGA VI Reference In input of the Invoke Method
 node that follows it.
