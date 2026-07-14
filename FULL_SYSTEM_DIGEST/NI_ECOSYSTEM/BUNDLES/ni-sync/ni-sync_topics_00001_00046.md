# NI DOCUMENT BUNDLE: ni-sync

<!--NI_BUNDLE_CHUNK bundle=ni-sync start=1 end=46 -->
<!--NI_TOPIC bundle=ni-sync path=clock-terminal-connections.html language=enus -->
## TOPIC 00001: Clock Terminal Connections

- bundle_id: `ni-sync`
- source_path: `clock-terminal-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/clock-terminal-connections.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following table to determine which clock source terminals are compatible with which clock destination terminals. You can connect clock terminals with niSync Connect Clock Terminals. Only devices in the system timing slot can use PXI_Clk10_In as a clock destination terminal. Only devices i

### Clock Terminal Connections

Note

- Only devices in the system timing slot can use
 PXI_Clk10_In as a clock destination
 terminal.
- Only devices in the system timing slot can use
 PXI_Clk10 or
 PXIe_DStarA<n> terminals as a clock source
 terminal.
- Only devices in a peripheral slot can use the
 PXIe_DStarC<n> terminals as a clock source
 terminal.
- Refer to your hardware manual to determine if a clock source or destination
 terminal is available on your device.

| Clock Source | Clock Destination |
| --- | --- |
| PXI_Clk10 | ClkOut BoardClk |
| ClkIn | PXI_Clk10_In ClkOut PFI_LVDS<n> PXIe_DStarA<n> |
| Oscillator | PXI_Clk10_In ClkOut BoardClk |
| DDS Clock | ClkOut PFI_LVDS<n> PXIe_DStarA<n> |
| PFI_LVDS<n> | ClkOut PFI_LVDS<n> PXIe_DStarA<n> |
| PXIe_DStarC<n> | ClkOut PFI_LVDS<n> PXIe_DStarA<n> |
| PXIe_DStarA | ClkOut PFI_LVDS<n> |

Parent topic:

Clocks in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=clocks-in-ni-sync.html language=enus -->
## TOPIC 00002: Clocks in NI-Sync

- bundle_id: `ni-sync`
- source_path: `clocks-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/clocks-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`

### Clocks in NI-Sync

- [Routing Clock Signals Between Devices](routing-clock-signals-between-devices.html)
- [Clock Terminal Connections](clock-terminal-connections.html)
- [Defining NI-Sync Clock Terminals](defining-ni-sync-clock-terminals.html)
- [Phase Locking to an External Clock Using a PLL Circuit](phase-locking-to-an-external-clock-using-a-pl.html)
- [Using Synchronization Clocks in NI-Sync](using-synchronization-clocks-in-ni-sync.html)

<!--NI_TOPIC bundle=ni-sync path=comparing-signal-based-and-time-based-synchro.html language=enus -->
## TOPIC 00003: Comparing Signal-Based and Time-Based Synchronization

- bundle_id: `ni-sync`
- source_path: `comparing-signal-based-and-time-based-synchro.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/comparing-signal-based-and-time-based-synchro.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synchronizing multiple devices requires accurate timing for event synchronization and data correlation. NI-Sync achieves timing accuracy between devices using two synchronization methods: signal-based and time-based. In a signal-based application, clocks and trigger signals are shared directly betwe

### Comparing Signal-Based and Time-Based Synchronization

Synchronizing multiple devices requires accurate timing for event synchronization and
 data correlation. NI-Sync achieves timing accuracy between devices using two
 synchronization methods: signal-based and time-based. In a signal-based application,
 clocks and trigger signals are shared directly between nodes that require
 synchronization. In a time-based application, nodes independently synchronize their
 individual clocks based on a common time source, usually an external timing reference
 like GPS.

Note

| Signal-Based | Time-Based |
| --- | --- |
| Nodes are less than 100 meters apart. System has no access to an external time reference. Nodes are physically connected using cables or switches. System is in a closed environment without network access. System requires higher precision synchronization. System requires synchronization of a small number of nodes. | Nodes are more than 100 meters apart. System has access to an external time reference, such as an IRIG generator or a GPS antenna. Nodes are connected through a network (including through Ethernet). System requires synchronization of a large number of nodes. Nodes frequently change location. |

Parent topic:

Synchronization Methods

<!--NI_TOPIC bundle=ni-sync path=connecting-and-synchronizing-triggers.html language=enus -->
## TOPIC 00004: Connecting and Synchronizing Triggers

- bundle_id: `ni-sync`
- source_path: `connecting-and-synchronizing-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/connecting-and-synchronizing-triggers.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use niSync Connect Trigger Terminals to link hardware trigger lines together. You can also use niSync Connect Software Trigger to connect the global software trigger to a destination trigger terminal. Complete the following steps to connect trigger terminals: Place niSync Initialize. Place n

### Connecting and Synchronizing Triggers

You can use niSync Connect Trigger Terminals to link hardware trigger lines together. You
 can also use niSync Connect Software Trigger to connect the global software trigger to a
 destination trigger terminal. Complete the following steps to connect trigger terminals:

1. Place niSync Initialize.
2. Place niSync Connect Trigger Terminals or niSync Connect Software Trigger.
3. Wire a constant or control to source and
 destination and select the source of the trigger and the
 destination to connect it to. Note The only acceptable source value
 for niSync Connect Software Triggers is Global Software
 Trigger.
4. (Optional) Set additional parameters for the new trigger route:
  - Select a value for synchronization clock . Use this
 value to send the trigger signal from the source terminal to the destination
 terminal asynchronously or on an update edge of the specified clock. Refer
 to Firing Triggers with a Synchronization Clock for more detailed
 information about synchronizing triggers.
  - Select a value for update edge . Use this value to
 determine whether to align the trigger signal with the rising or falling
 edge of the synchronization clock.
  - Select a value for invert . Use this value to
 determine whether to invert the source terminal signal when it reaches the
 destination terminal. You can use this terminal for differential analysis or
 to eliminate noise in your signal.
  - If you are using niSync Connect Software Triggers, select a value for
 delay . Use this value to delay firing the global
 software trigger by the selected value when you invoke niSync Send Software
 Trigger.
5. (Optional) If you are using niSync Connect Software Triggers, place niSync Send
 Software Trigger on the block diagram where you would like to fire the software
 trigger.
6. Place niSync Disconnect Trigger Terminals or niSync Disconnect Software Trigger on
 the block diagram and wire the appropriate terminals.
7. Place niSync Close on the block diagram to close the NI-Sync I/O session.

Parent topic:

Triggers in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=converting-ni-sync-error-codes-to-a-user-read.html language=enus -->
## TOPIC 00005: Converting NI-Sync Error Codes to a User-Readable String

- bundle_id: `ni-sync`
- source_path: `converting-ni-sync-error-codes-to-a-user-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/converting-ni-sync-error-codes-to-a-user-read.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to explain an NI-Sync error code with a user-readable string: Place niSync Error Message. Wire the session handle of an NI-Sync session to instrument handle. Open the Functions palette and select Programming>>Cluster, Class, & Variant>>Unbundle by Name to place the Unbun

### Converting NI-Sync Error Codes to a User-Readable String

Complete the following steps to explain an NI-Sync error code with a user-readable
 string:

1. Place niSync Error Message.
2. Wire the session handle of an NI-Sync session to instrument
 handle .
3. Open the Functions palette and select
 Programming>>Cluster, Class, & Variant>>Unbundle by
 Name to place the Unbundle by Name function on the block
 diagram.
4. Wire the error cluster of an NI-Sync VI to input cluster of
 the Unbundle by Name function.
5. Left-click the Unbundle by Name function and select
 code .
6. Wire the output of the Unbundle by Name function to error
 code of niSync Error Message.
7. Wire an indicator to error message of niSync Error Message to
 display an explanation of the error code.

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=ni-sync path=creating-and-reading-timestamps.html language=enus -->
## TOPIC 00006: Creating and Reading Timestamps

- bundle_id: `ni-sync`
- source_path: `creating-and-reading-timestamps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/creating-and-reading-timestamps.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-Sync timestamp VIs to record the board time when an event—like a clock edge, trigger, or future time event—occurs. You can use timestamps to measure clock drift and skew between devices, record changes in a signal, or mark the beginning and end of data acquisition. Timestamping is availab

### Creating and Reading Timestamps

Note

- Timestamping is available only on time-based timing and synchronization
 modules.
- You can only timestamp terminals with I/O, such as trigger signals, future
 time events, synchronization clock signals, and clocks generated with DDS or
 niSync Create Clock.

Complete the following steps to timestamp a user-generated clock using the NI-Sync
 timestamp VIs and niSync Create Clock:

1. Place niSync Initialize.
2. Place niSync Create Clock and configure it:
  1. Select the Ticks instance.
  2. Wire a control or constant to terminal and select the
 terminal you would like to create the clock on.
  3. Specify the number of high ticks and low ticks each clock cycle will have
 using high ticks and low
 ticks .
  4. (Optional) Specify a start and stop time for the clock using
 start time and stop
 time .
3. Place niSync Enable Time Stamp Trigger and configure it:
  1. Connect terminal to the same terminal you generated
 the clock on.
  2. (Optional) Wire a control or constant to decimation
 count to adjust the number of timestamps that occur between
 recorded timestamps.
  3. (Optional) Wire a control or constant to active edge 
 to create timestamps on a specific clock edge.
4. Place niSync Read Trigger Time Stamp and configure it:
  1. Select the Read Single Timestamp instance to read the
 first timestamp written, or select the Read Multiple
 Timestamps instance to read a specified number of
 timestamps.
  2. Wire terminal to the same terminal you generated the
 clock on.
  3. Wire an indicator to time stamp out . This returns an
 array of timestamps if you selected the Read Multiple Timestamps instance,
 or a single timestamp if you selected the Read Single Timestamp
 instance.
  4. (Optional) Wire an indicator to detected edge to
 return the clock edge the timestamp was recorded on.
  5. (Optional) Wire a control or constant to timeout to
 specify how long, in seconds, the VI should try to read a timestamp before
 stopping.
  6. (Optional) If you selected the Read Multiple Timestamps instance, wire a
 control or constant to number of timestamps to
 specify how many timestamps the VI should read.
5. Place niSync Disable Time Stamp Trigger and wire terminal to
 the same terminal you generated the clock on.
6. Place niSync Clear Clock and wire terminal to the terminal
 you generated the clock on.
7. Place niSync Close to end the NI-Sync session and free all resources for another
 program.

After you complete the preceding steps, you have an application that records a timestamp
 whenever there is a rising edge to the clock you generate with niSync Create Clock. You
 can substitute niSync Create Clock with any clock signal, future time event, or trigger
 signal that you can propagate on a PFI or PXI_Trig line to timestamp those signals.

Parent topic:

Time References in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=defining-ni-sync-clock-terminals.html language=enus -->
## TOPIC 00007: Defining NI-Sync Clock Terminals

- bundle_id: `ni-sync`
- source_path: `defining-ni-sync-clock-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/defining-ni-sync-clock-terminals.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using niSync Connect Clock Terminals, you can route clocks between chassis, discipline the PXI backplane clock to the oscillator of a system timing module, or route an external time reference throughout a chassis or to multiple chassis. The VI uses clock terminals to route clock signals between devi

### Defining NI-Sync Clock Terminals

Note

#### Clock Source Terminals

| Clock Source | Description |
| --- | --- |
| ClkIn | The ClkIn input connector on the front panel of your device. Using ClkIn, you can connect a 10 MHz reference clock directly to the PXI_Clk10_In pin. You also can phase lock a clock connected to ClkIn using a PLL circuit, or you can use a clock connected to ClkIn as the synchronization clock for the front and rear zones of your chassis. |
| PXI_Clk10 | The 10 MHz backplane clock of the PXI or PXIe chassis. |
| Oscillator | The oscillator of the device specified in the instrument handle terminal. |
| DDS Clock | The DDS signal generated by the device specified in the instrument handle terminal. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of your device. PFI LVDS lines consist of paired PFI lines. You can use PFI_LVDS to route clock and trigger signals between multiple PXIe chassis at high speeds. You can achieve faster speeds when using an LVDS line compared to a single-ended PFI line. Signals on PFI LVDS lines use the standard PFI synchronization clock. |
| PXIe_DStarC<n> | The differential star trigger line of your PXIe chassis. Use DStarC lines to route clock and/or trigger signals from a peripheral slot to a system timing slot. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis' documentation for more information on the mapping of differential star trigger lines. |
| PXIe_DStarA | The differential star trigger line of your PXIe chassis. Use DStarA lines to route clock signals from a system timing slot to a peripheral slot. Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis' documentation for more information on the mapping of differential star trigger lines. |

#### Clock Destination Terminals

| Clock Destination | Description |
| --- | --- |
| PXI_Clk10_In | The connector pin that you use to provide the backplane with a reference 10 MHz signal from the system timing slot. When you connect a signal to this pin, PXI_Clk10 and PXIe_Clk100 are phase aligned to this reference. |
| ClkOut | The ClkOut connector on the front panel of your device. Use this terminal to export clocks to an external device or to another chassis. You can export only clock signals through the ClkOut connector. |
| BoardClk | The timekeeper used to schedule future time events and timestamping on PXI-6682, PXI-6682H, PXI-6683, and PXI-6683H modules. BoardClk accepts a 10 MHz reference clock and multiplies it by 10 to create a 100 MHz clock for use as a timekeeper. The only two valid sources for BoardClk are the on-board oscillator and PXI_Clk10. You can specify the source of BoardClk using the niSync Connect Clock Terminals VI. Note BoardClk is a valid terminal only on PXI-668x devices. |
| PFI_LVDS<n> | The PFI_LVDS output connector on the front panel of your device. |
| PXIe_DStarA<n> | The differential star trigger line of your PXIe chassis. Use DStarA lines to route clock signals from the system timing slot to a peripheral slot of your chassis. |

Parent topic:

Clocks in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=defining-ni-sync-trigger-terminals.html language=enus -->
## TOPIC 00008: Defining NI-Sync Trigger Terminals

- bundle_id: `ni-sync`
- source_path: `defining-ni-sync-trigger-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/defining-ni-sync-trigger-terminals.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using niSync Connect Trigger Terminals, you can route triggers between modules, synchronize triggers to different synchronization clocks, and export clock signals along some trigger lines. The VI uses trigger terminals to pass trigger signals from place to place. Use the following table to determine

### Defining NI-Sync Trigger Terminals

Note

| Trigger Terminal | Description |
| --- | --- |
| PXI_Trig<n> | The basic trigger lines of your PXI or PXIe chassis. PXI triggers go to and from all slots in the chassis—though the signals do not reach all slots at the same time—and all modules receive the same PXI triggers, so PXI_Trig0 is the same for Slot 3 as it is for Slot 4, and so on. |
| PXI_Star<n> | The star trigger lines of your PXI or PXIe chassis. Each trigger line is a dedicated connection between the system timing slot and one other slot. Star triggers are all of equal length, so signals routed via star triggers should reach their destinations at the same time if they were sent at the same time.Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to your hardware documentation to determine the orientation of PXI_Star lines in your chassis. |
| PFI<n> | The PFI connectors on the front panel of your module. You can use PFI connectors to route triggers between multiple chassis or devices. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of your device. PFI LVDS lines consist of paired PFI lines and can be used to route timing and triggering signals between multiple PXIe chassis at high speeds. You can achieve faster speeds when using an LVDS line compared to a single-ended PFI line. Signals on PFI LVDS lines use the standard PFI synchronization clock. |
| Ground Source Only | The Ground source continuously outputs a logic low signal, unless you invert it with the niSync Connect Trigger Terminals VI. |
| Synchronization Clock (Full Speed) Source Only | The full speed synchronization clock signal of the destination terminal zone. Use this source to send a full-speed clock signal along a trigger line (for example, to route a PXI_Clk10 clock signal to a PFI line). Caution Routing a clock signal through a PXI_Trig line is not recommended, due to poor clock signal integrity caused by the topology of the PXI_Trig lines. Use PXI_Star, PXIe_DStar, or PFI lines instead. |
| Synchronization Clock (Divided 1) Source Only | The first divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 1 parameter of the niSync Property Node and uses the result as the trigger source. Use this source to send a divided clock signal along a trigger line (for example, to route a divided DDS signal to a PXI_Star line). |
| Synchronization Clock (Divided 2) Source Only | The second divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 2 parameter of the niSync Property Node and uses the result as the trigger source. Use this source to send a divided clock signal along a trigger line (for example, to route a divided PXI_Clk10 signal to a PXI_Star line). |
| ClkIn Source Only | The ClkIn connector on the front panel of your device. Use this terminal source to route triggers from an external device. |
| PXIe_DStarB<n> | The differential star trigger lines of your PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of your chassis. Note Each PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarC | The differential star trigger lines of your PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of your chassis. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis documentation to determine the orientation of differential star trigger lines. |

Parent topic:

Triggers in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=displaying-the-state-of-a-trigger-line-as-an.html language=enus -->
## TOPIC 00009: Displaying the State of a Trigger Line as an Array

- bundle_id: `ni-sync`
- source_path: `displaying-the-state-of-a-trigger-line-as-an.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/displaying-the-state-of-a-trigger-line-as-an.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can asses the state of a trigger line by using the niSync Property Node to display the state of a trigger line. Complete the following steps to display the state of a trigger line: Place the niSync Property Node on the block diagram. Click on the niSync Property Node, select Trigger State Proper

### Displaying the State of a Trigger Line as an Array

You can asses the state of a trigger line by using the niSync Property Node to display
 the state of a trigger line. Complete the following steps to display the state of a
 trigger line:

1. Place the niSync Property Node on the block diagram.
2. Click on the niSync Property Node, select Trigger State
 Properties , and select the trigger line you would like to evaluate
 from the context menu. You can select the following trigger lines:
  - PXI_Star
  - PXI_Trig
  - PFI
  - PFI_LVDS
  - PXIe_DStarC
3. Place the Number to Boolean Array function on the block diagram by selecting
 Boolean»Num to Array from the Functions Palette and wire
 it to the first parameter of the niSync Property Node.
4. Wire an indicator to the output of the Number to Boolean Array function. A Boolean
 array appears on the front panel.
5. Resize the array on the front panel so that the number of rows matches the number of
 lines in the chassis. For example, if you are trying to display the state of
 PXI_Star lines in a chassis with eight PXI_Star lines, the array should have eight
 Boolean indicators.

Tip

Array»Reverse 1D Array

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=ni-sync path=enabling-and-configuring-a-phase-locked-loop.html language=enus -->
## TOPIC 00010: Enabling and Configuring a Phase-Locked Loop

- bundle_id: `ni-sync`
- source_path: `enabling-and-configuring-a-phase-locked-loop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/enabling-and-configuring-a-phase-locked-loop.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to use an NI-Sync device's PLL circuit to phase lock the oscillator of the system timing module to an external clock: Connect an external clock to the ClkIn connector on the front panel of the module in the system timing slot of the chassis. Place niSync Initialize and s

### Enabling and Configuring a Phase-Locked Loop

Complete the following steps to use an NI-Sync device's PLL circuit to phase lock the
 oscillator of the system timing module to an external clock:

1. Connect an external clock to the ClkIn connector on the front panel of the module in
 the system timing slot of the chassis.
2. Place niSync Initialize and select the module in the chassis' system timing slot for
 resource name .
3. Place an niSync Property Node.
4. Select Clk Properties»Use PLL? for the first parameter of the
 niSync Property Node and set its value to TRUE.
5. Add another parameter to the niSync Property Node and select Clk
 Properties»PLL Frequency for the second parameter.
6. Right click the PLL Frequency parameter and select
 Change to Write .
7. Wire a control or constant to the PLL Frequency parameter and
 enter the frequency of the external clock connected to ClkIn. Refer to the device's
 hardware manual for the reference frequency range supported by the device's PLL
 circuit.

After completing the preceding steps, the oscillator of the NI-Sync device is configured
 to enable a phase-locked loop. However, you must create a route from ClkIn to
 PXI_CLK10_In before you can successfully phase-lock the oscillator to an external
 clock.

Refer to Routing and Locking to the PLL Reference Clock to complete the phase-locked
 loop.

Parent topic:

Phase Locking to an External Clock Using a PLL Circuit

Related concepts:

- Routing and Locking to the PLL Reference Clock

<!--NI_TOPIC bundle=ni-sync path=extended-support-changes.html language=enus -->
## TOPIC 00011: Updates and Changes for NI-Sync Extended Support Versions

- bundle_id: `ni-sync`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/extended-support-changes.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-Sync versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible changes,

### Updates and Changes for NI-Sync Extended Support Versions

Browse updates and changes made in NI-Sync versions
 on extended support.

Note

Release Notes

#### NI-Sync 2022
 Q4

##### New Features

- Added new properties for IEEE-1588 protocol.
- Added support for LabVIEW 2022.

#### NI-Sync
 21.8

##### New
 Feature

- Added support for PXI-6683H on DEB and RPM Linux desktop distributions.

#### NI-Sync
 21.3

##### New
 Features

- Improved support for PXI-6683H on NI Linux RT.
- Added support for synchronous routing on the PXI-6683H.
- Added support for reading timestamps when using IRIG-B.
- Improved support for GPS Time Synchronization on NI Linux RT.
- Added support for MAX test panels for PXI-6683H on NI Linux RT.
- Added support for PXIe-6674T on DEB Linux desktop distributions.
- Improved support for PXIe-6674T on RPM Linux desktop distributions.

#### NI-Sync
 21.1

##### New
 Features

- Added support for LabVIEW 2021.
- Improved support for the PXIe-6674T on Linux Real-Time.
- Added support for GPS Mobile Mode for the PXI-6683 and PXI-6683H on Linux
 Real-Time.
- Added support for Pulse Per Second (PPS) Time Synchronization for the PXI-6683 and
 PXI-6683H on Linux Real-Time.
- Improved support for System Configuration and NI-Sync properties on Linux RT.
- Added support for MAX test panels for the PXIe-6674T on Linux RT.
- Partial support for MAX test panels for the PXI-6683 and PXI-6683H on Linux RT.

<!--NI_TOPIC bundle=ni-sync path=firing-triggers-with-a-synchronization-clock.html language=enus -->
## TOPIC 00012: Firing Triggers with a Synchronization Clock

- bundle_id: `ni-sync`
- source_path: `firing-triggers-with-a-synchronization-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/firing-triggers-with-a-synchronization-clock.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Setting and Dividing a Synchronization Clock After you have set a synchronization clock for the front and/or rear zones of your chassis, you can use the synchronization clock to control when triggers fire. Using the synchronization clock terminal of niSync Connect Trigger Terminals, y

### Firing Triggers with a Synchronization Clock

Prerequisites: Setting and Dividing a Synchronization Clock

After you have set a synchronization clock for the front and/or rear zones of your
 chassis, you can use the synchronization clock to control when triggers fire. Using the
 synchronization clock terminal of niSync Connect Trigger
 Terminals, you can set a trigger to fire on an update edge of the full-speed or a
 divided synchronization clock.

You can also fire a trigger asynchronously using this terminal, though a trigger
 synchronized to a time reference is generally more accurate than an asynchronous
 trigger. Using a synchronization clock to coordinate trigger firing is ideal for
 situations where you are trying to synchronize different signals coming through the
 front and back zones of your chassis.

Complete the following steps to synchronize a trigger with a divided or full-speed clock:

1. Place niSync Connect Trigger Terminals.
2. Wire instrument handle with the session handle from the
 niSync Property Node you used in Setting and Dividing a Synchronization Clock.
3. Set Divided Clock 1 as the value for
 synchronization clock . This divides the frequency of the
 synchronization clock by the value you set in the Clock Divisor 1 parameter of the
 niSync Property Node and uses the result as the synchronization clock frequency for
 this trigger. Note You can also set the synchronization clock
 terminal to the following values:Divided Clock 2—Fires the trigger on an update
 edge of the second divided clock you created with the Clock Divisor 2
 parameter of the niSync Property Node.
 Full Speed Clock—Fires the trigger on an update
 edge of the full-speed synchronization clock.
 Asynchronous—Fires the trigger independently of
 the synchronization clock.
4. Select the source and destination 
 terminals for this trigger.

After completing the preceding steps, the trigger fires on an update edge of the
 full-speed or divided synchronization clock.

Parent topic:

Using Synchronization Clocks in NI-Sync

Related concepts:

- Setting and Dividing a Synchronization Clock

<!--NI_TOPIC bundle=ni-sync path=glossary.html language=enus -->
## TOPIC 00013: Glossary

- bundle_id: `ni-sync`
- source_path: `glossary.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/glossary.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefixes Symbol Prefix Value n nano 10 ^-9 µ micro 10 ^-6 m milli 10 ^-3 M mega 10 ^6 G giga 10 ^9 Numbers/Symbols 1588 epoch A period of absolute time defined by the IEEE 1588 specification. The current 1588 epoch is assigned the number 0 and started at 0 hours 1 January 1970. The length of a 1588

### Glossary

#### Prefixes

| Symbol | Prefix | Value |
| --- | --- | --- |
| n | nano | 10 -9 |
| µ | micro | 10 -6 |
| m | milli | 10 -3 |
| M | mega | 10 6 |
| G | giga | 10 9 |

#### Numbers/Symbols

| 1588 epoch | A period of absolute time defined by the IEEE 1588 specification. The current 1588 epoch is assigned the number 0 and started at 0 hours 1 January 1970. The length of a 1588 epoch is 2³² seconds. |
| --- | --- |
| 1588 grandmaster clock | The 1588 clock to which all other 1588 devices in a specific PTP subdomain are synchronized |
| 1588 master clock | The 1588 clock to which other 1588 devices are synchronized if they are directly connected to it (that is, they are not connected via a boundary clock) |
| 1588 time | The time format specified by IEEE 1588. IEEE 1588 represents time as a 32-bit unsigned integer for the number of seconds and a 32-bit unsigned integer for the number of nanoseconds since the 1588 epoch. From 1 January 1972 onward, 1588 time typically follows TAI time, but can follow UTC time. |
| A |  |
| accumulator | A part where numbers are totaled or stored |
| asynchronous | A property of an event that occurs at an arbitrary time, without synchronization to a reference clock |
| B |  |
| backplane | An assembly, typically a printed circuit board (PCB), with 96-pin connectors and signal paths that bus the connector pins. PXI systems have two connectors, called the J1 and J2 connectors. |
| BMC | Best Master Clock—an algorithm that determines which clock in a 1588 network should be used as the grandmaster clock. |
| bus | The group of conductors that interconnect individual circuitry in a computer. Typically, a bus is the expansion vehicle to which I/O or other devices are connected. An example of a PC bus is the PCI bus. |
| C |  |
| C | Celsius |
| ClkIn | ClkIn is a signal connected to the SMB input pin of the same name. ClkIn can serve as PXI_Clk10_IN or be used as a phase lock reference for the OCXO. |
| ClkOut | ClkOut is the signal on the SMB output pin of the same name. The OCXO clock, DDS clock, or PXI_Clk10 may be routed to ClkOut. |
| clock | A hardware component that controls timing for reading from or writing to groups |
| D |  |
| DAC | Digital-to-analog converter—an electronic device that converts a digital number into a corresponding analog voltage or current |
| DAQ | Data acquisition—(1) collecting and measuring electrical signals from sensors, transducers, and test probes or fixtures and inputting them to a computer for processing; (2) collecting and measuring the same kinds of electrical signals with A/D and/or DIO devices plugged into a computer, and possibly generating control signals with D/A and/or DIO devices in the same computer. |
| DC | Direct current |
| DDS | Direct Digital Synthesis—A method of creating a clock with a programmable frequency |
| duty cycle (n.), duty-cycle (adj.) | The ratio of the duration (time) that a signal is on to the total period of the signal |
| E |  |
| EEPROM | Electrically erasable programmable read-only memory—ROM that can be erased with an electrical signal and reprogrammed |
| F |  |
| frequency | The basic unit of rate, measured in events or oscillations per second using a frequency counter or spectrum analyzer. Frequency is the reciprocal of the period of a signal. |
| front panel | The physical front panel of an instrument or other hardware |
| G |  |
| GPS | Global Positioning System—a system of satellites that broadcast accurate times. GPS receivers acquire these times, which you can use to establish geographic position. You can also use the time received as an accurate clock source. |
| H |  |
| Hz | Hertz—the number of scans read or updates written per second |
| I |  |
| IEEE 1588 | The IEEE specification that describes a synchronization protocol for clocks of multiple devices connected via a network |
| in. | Inch or inches |
| IP | Internet Protocol—a packet-based protocol used to communicate between multiple computer systems on a network. The IP is a low-level protocol on top of which other, more reliable, protocols are often defined. |
| J |  |
| jitter | The rapid variation of a clock or sampling frequency from an ideal constant frequency |
| L |  |
| LED | Light-Emitting Diode—a semiconductor light source |
| M |  |
| master | The requesting or controlling device in a master/slave configuration |
| Measurement & Automation Explorer (MAX) | A controlled centralized configuration environment that allows you to configure all of your NI DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices |
| N |  |
| NTP | Network Time Protocol—a protocol that synchronizes the clocks of computers connected via an IP network. You may use NTP to synchronize computer clocks over a very wide geographical area. |
| O |  |
| OCXO | Oven-controlled crystal oscillator |
| oscillator | A device that generates a fixed frequency signal. An oscillator most often generates signals by using oscillating crystals, but may also use tuned networks, lasers, or atomic clock sources. The most important specifications on oscillators are frequency accuracy, frequency stability, and phase noise. |
| output impedance | The measured resistance and capacitance between the output terminals of a circuit |
| P |  |
| PCI | Peripheral Component Interconnect—a high-performance expansion bus architecture originally developed by Intel to replace ISA and EISA. It is achieving widespread acceptance as a standard for PCs and work-stations; it offers a theoretical maximum transfer rate of 132 Mbytes/s. |
| PFI | Programmable Function Interface |
| PLL | Phase-locked loop |
| precision | The measure of the stability of an instrument and its capability to give the same measurement over and over again for the same input signal |
| propagation delay | The amount of time required for a signal to pass through a circuit |
| PTP | Precision Time Protocol—the IEEE 1588-defined network protocol used to synchronize the clocks of multiple devices connected via a network |
| PXI | A rugged, open system for modular instrumentation based on CompactPCI, with special mechanical, electrical, and software features. The PXIbus standard was originally developed by NI in 1997, and is now managed by the PXIbus Systems Alliance. |
| PXI Star | A special set of trigger lines in the PXI backplane for high-accuracy device synchronization with minimal latencies on each PXI slot |
| R |  |
| RMS | root mean square—The square root of the average value of the square of the instantaneous signal amplitude; a measure of signal amplitude. The RMS voltage of a signal is computed by squaring the instantaneous voltage, integrating over the desired time, and taking the square root. |
| S |  |
| s | Seconds |
| skew | The actual time difference between two events that would ideally occur simultaneously. Inter-channel skew is an example of the time differences introduced by different characteristics of multiple channels. Skew can occur between channels on one module, or between channels on separate modules (intermodule skew). |
| slave | A computer or peripheral device controlled by another computer |
| slot | The place in the computer or chassis in which a card or module can be installed |
| Slot 2 | The second slot in a PXI system, which can house a master timing unit |
| SMB | Sub Miniature Type B—a small coaxial signal connector that features a snap coupling for fast connection |
| synchronization clock | A clock that controls the frequency at which triggers fire in the front and rear zones of a PXI chassis. |
| synchronous | A property of an event that is synchronized to a reference clock |
| T |  |
| TAI | International Atomic Time. Unlike UTC, TAI does not account for leap seconds. Therefore, TAI is the time system employed by network standards for which leap seconds may be problematic. |
| tri-state | A state in which an output driver assumes high impedance and does not drive a voltage |
| TRIG | Trigger signal |
| trigger | A digital signal that starts or times a hardware event (for example, starting a data acquisition operation) |
| U |  |
| UTC | Coordinated Universal Time—the time system that accounts for leap seconds and is employed by many network standards, including NTP |
| V |  |
| V | Volts |
| VI | Virtual instrument |
| Z |  |
| zone | The location of trigger lines in a PXI chassis. There are two zones: front zone—Contains the front panel connectors of the PXI chassis, including PFI and PFI_LVDS lines. rear zone—Contains the backplane trigger lines of the PXI chassis, including PXI_Trig and PXI_Star. |

<!--NI_TOPIC bundle=ni-sync path=gps-time-synchronization-protocol.html language=enus -->
## TOPIC 00014: GPS Time Synchronization Protocol

- bundle_id: `ni-sync`
- source_path: `gps-time-synchronization-protocol.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/gps-time-synchronization-protocol.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: GPS is a system of 24 satellites funded and controlled by the US Department of Defense. The global positioning satellites (GPS) continually transmit their coordinates in space along with a time message on a 1.5 GHz carrier frequency. A time-based timing and synchronization module that has a GPS rece

### GPS Time Synchronization Protocol

GPS is a system of 24 satellites funded and controlled by the US Department of Defense.
 The global positioning satellites (GPS) continually transmit their coordinates in space
 along with a time message on a 1.5 GHz carrier frequency. A time-based timing and
 synchronization module that has a GPS receiver can use this global timebase to precisely
 correlate, trigger, and timestamp measurement data. Each global positioning satellite
 contains multiple atomic clocks, which are controlled and referenced by the Master Clock
 (MC) at the United States Naval Observatory (USNO), called UTC(USNO).

#### Synchronizing to GPS Time

NI time-based synchronization modules can use GPS technology as a time reference. If
 you set GPS as the time reference for a module, the module uses the time updates
 received by the onboard GPS receiver every second, derives from it the current TAI
 time, and sets this time as the current board time.

When you initially connect a GPS antenna to a time-based synchronization module or
 set GPS as the time reference, the onboard GPS receiver searches for visible
 satellites. After detecting at least four satellites, the GPS receiver performs a
 self survey, which is the process of performing measurements of the visible
 satellites once per second and averaging those measurements to determine the
 receiver's current position as accurately as possible. During a self survey, you can
 use GPS as a time reference, but it is less accurate than after the self survey is
 finished. Once the GPS unit completes the self survey, you can precisely apply the
 time data received from GPS satellites.

If you configure the time-based synchronization module for mobile mode, a self survey
 does not apply. If the antenna is moving and mobile mode is not enabled, you may get
 unexpected and invalid timing results. However, using mobile mode degrades the
 accuracy of the onboard GPS receiver, so you should not use it unless the antenna is
 moving.

#### Factors Affecting GPS Synchronization Accuracy

You can obtain the best GPS timing results by having an ideally located, long-term,
 stable GPS antenna installation. Ideally, you should mount the GPS antenna in a
 location where it has an unobstructed, clear view of the entire sky. In this
 orientation, the GPS receiver can detect additional satellites and perform
 additional averaging while discarding the worst signals and alleviating the effects
 of multipath, which is when the GPS antenna receives a signal reflected off an
 object or surface instead of a signal directly from the satellite(s).

Completing a self survey will also improve accuracy by performing long-term averaging
 of location. It is best to ensure the antenna is in a fixed location throughout the
 self survey process and throughout use, because any small movement of the antenna
 reduces accuracy. For this reason, you should also attempt to minimize the movement
 of a GPS antenna caused by wind or vibration.

Antenna cable latency also adds constant error. For maximum accuracy, you can
 calculate the latency of the GPS antenna cable in use and apply a correction. You
 can use the Time Reference Correction parameter of the niSync Property Node to
 remove the source of this error. For example, if the antenna cable in use has a
 published latency of 5 ns/m, and the antenna installation uses 30 m of cable, the
 total delay that the antenna installation causes is 150 ns, so you can set the Time
 Reference Correction property to 150 to correct this. While not necessary in all
 cases, you can improve the accuracy of GPS by accounting for all sources of delay in
 your GPS installation, including cabling, lightning arrestors, and amplifiers.

You can also use the niSync Property Node to query the number of visible satellites
 using the Satellites Available parameter and determine if any fatal GPS errors are
 present using the Status parameter. A minimum of four satellites should be visible
 for stable GPS operations, and GPS clock accuracy and stability increase as the
 number of visible satellites increase.

Parent topic:

Time Synchronization Protocols in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=hardware-compatibility-with-ni-sync-features.html language=enus -->
## TOPIC 00015: Hardware Compatibility with NI-Sync Features

- bundle_id: `ni-sync`
- source_path: `hardware-compatibility-with-ni-sync-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/hardware-compatibility-with-ni-sync-features.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer the following tables to determine which signal-based and time-based modules are compatible with which NI-Sync features: Signal-Based Modules Signal-Based Module Supported Hardware Features NI PXI-6651 PFI Lines ClkIn PXI_Trig, PXI_Star Lines NI PXI-6652 PXI_Clk10 PLL Circuit DDS Clock Generati

### Hardware Compatibility with NI-Sync Features

Refer the following tables to determine which signal-based and time-based modules are
 compatible with which NI-Sync features:

#### Signal-Based Modules

| Signal-Based Module | Supported Hardware Features |
| --- | --- |
| NI PXI-6651 | PFI Lines ClkIn PXI_Trig, PXI_Star Lines |
| NI PXI-6652 | PXI_Clk10 PLL Circuit DDS Clock Generation PFI Lines ClkIn / ClkOut On-board TCXO PXI_Trig, PXI_Star Lines |
| NI PXI-6653 | PXI_Clk10 PLL Circuit DDS Clock Generation PFI Lines ClkIn / ClkOut On-board OCXO PXI_Trig, PXI_Star Lines |
| NI PXIe-6672 | PXI_Clk10 PLL Circuit DDS Clock Generation PFI Lines ClkIn / ClkOut On-board TCXO PXI_Trig, PXI_Star Lines |
| NI PXIe-6674T | PXI_Clk10 PLL Circuit DDS Clock Generation PFI and PFI LVDS Lines ClkIn / ClkOut On-board OCXO PXI_Trig, PXI_Star, and PXIe_DStar Lines |

#### Time-Based Modules

| Time-Based Module | Supported Hardware Features |
| --- | --- |
| PCI-1588 | IEEE 1588-2008 PFI Lines On-board TCXO |
| PXI-6682 | GPS, IEEE 1588-2008, PPS, and IRIG-B PFI Lines ClkIn / ClkOut On-board TCXO PXI_Trig, PXI_Star Lines |
| PXI-6682H | GPS, IEEE 1588-2008, PPS, and IRIG-B PFI Lines ClkOut On-board TCXO PXI_Trig Lines |
| PXI-6683 | GPS, IEEE 1588-2008, PPS, and IRIG-B PFI Lines ClkIn / ClkOut On-board TCXO PXI_Trig, PXI_Star Lines |
| PXI-6683H | GPS, IEEE 1588-2008, PPS, and IRIG-B PFI Lines ClkOut On-board TCXO PXI_Trig Lines |

<!--NI_TOPIC bundle=ni-sync path=ieee-1588-2008-time-synchronization-protocol.html language=enus -->
## TOPIC 00016: IEEE 1588-2008 Time Synchronization Protocol

- bundle_id: `ni-sync`
- source_path: `ieee-1588-2008-time-synchronization-protocol.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/ieee-1588-2008-time-synchronization-protocol.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the IEEE 1588-2008 precision time protocol (PTP), you can synchronize several clocks connected via a multicast capable network, such as Ethernet. The protocol requires little network bandwidth overhead, processing power, and administrative setup. Depending on the hardware you use, IEEE 1588-20

### IEEE 1588-2008 Time Synchronization Protocol

Using the IEEE 1588-2008 precision time protocol (PTP), you can synchronize several
 clocks connected via a multicast capable network, such as Ethernet. The protocol
 requires little network bandwidth overhead, processing power, and administrative setup.
 Depending on the hardware you use, IEEE 1588-2008 can provide submicrosecond
 synchronization over long distances with standard cabling. Refer to the device's
 hardware manual for typical performance results with NI-Sync.

Tip

ni.com/info

Refer to the following table to compare synchronization accuracy using the PXI backplane,
 multichassis synchronization using cabling from a PXI system timing slot, a hardware
 implementation of the IEEE 1588-2008 protocol over Ethernet, and network time protocol
 (NTP):

|  | PXI Backplane | PXI System Timing Slot | IEEE 1588 | NTP on IP |
| --- | --- | --- | --- | --- |
| Event Resolution | ~0.01 ns | ~50 ns | ~50 ns* | <1x107 ns |
| Event Jitter | ~0.002 ns | ~0.5 ns | ~100 ns* | ~3x106 ns |
| Distance | ~0.5 m | <200 m | <400 m† | Worldwide |
| Sample Rates | 100s of MHz | 100s of MHz | <100 KHz | <10 Hz |
| Asynchronous Trigger | Supported | Supported | Not Supported | Not Supported |
| Cabling Type | n/a | Coaxial | CAT 5 Ethernet | Ethernet, etc. |
| Topology | User-defined | User-defined | Auto-resolve, master/slave | Peer-to-peer |
| Source: Special Focus: Understanding the IEEE 1588 Precision Time Protocol *Best case, topology- and traffic-dependent. †Can extend further using boundary clocks and transparent switches. |  |  |  |  |

#### Understanding Bidirectional Multicast Communication

IEEE 1588-2008 mainly uses bidirectional multicast communication to synchronize slave
 clocks to the 1588 grandmaster. The grandmaster clock periodically issues a sync
 packet, which is timestamped when it leaves the grandmaster clock. Optionally, the
 grandmaster may issue a follow up packet that contains the timestamp for the sync
 packet. Using a follow up packet, the grandmaster can accurately timestamp the sync
 packet on networks where you cannot know the departure time of a packet
 beforehand.

A slave clock receives the grandmaster's sync packet and timestamps the packet's
 arrival time using its own clock. The difference in the sync packet's departure
 timestamp and its arrival timestamp is the combination of the slave clock's offset
 from the grandmaster and the propagation delay of the network. When the slave
 adjusts its clock by the offset it measures when it receives the sync packet, it
 reduces the offset between the master and slave to the network propagation delay
 only.

The slave clock then compensates for the network propagation delay using a delay
 request packet. The delay request packet is timestamped when it departs from the
 slave, timestamped again when the master clock receives it, and then sent back to
 the slave clock with the new arrival timestamp. The difference between the arrival
 and the departure timestamps is the network propagation delay. Slave clocks can
 accurately measure the offset between their local clock and the master's clock using
 these synchronization packets, allowing them to adjust their clocks to match the
 time of the master. The IEEE 1588-2008 specification does not include any standard
 implementation for adjusting a clock, it merely provides a standard protocol for
 exchanging the synchronization messages, allowing devices from different
 manufacturers and with different implementations to work together.

Actual performance on an IEEE 1588 network is highly application-specific. For
 example, the protocol does not specify the clock frequency in the master and slaves,
 so lower-frequency clocks have poorer time resolution, resulting in less-accurate
 timestamps in the PTP synchronization messages. 1588's performance is also dependent
 on clock stability: clocks based on TCXOs and OCXOs have a higher stability than
 clocks using uncontrolled crystal oscillators. Clocks with lower stabilities drift
 apart faster, resulting in more frequent phase or frequency corrections and larger
 skews. Network topology also impacts IEEE 1588 performance.

#### Synchronizing Devices with IEEE 1588-2008

IEEE 1588-2008 uses two steps to synchronize devices: (1) the Best Master Clock
 algorithm (BMCA) determines which device serves as the master clock, and (2) the
 NI-Sync driver measures and corrects time skew caused by clock offsets and network
 delays.

The BMCA defines a standard set of clock characteristics—such as the origin of a
 clock's time source and the stability of the clock's frequency—and then assigns a
 value to each clock in order to determine the highest ranking, most accurate clock
 on the network, which then becomes the grandmaster clock. All the slave clocks in
 the network synchronize to the grandmaster clock. The BMCA continues to assess the
 quality of each clock, so if the grandmaster clock leaves the network or is no
 longer the most accurate clock, the algorithm automatically selects a new
 grandmaster. The BMCA also takes into account user-defined priority values, which
 you can set using the Priority 1 and Priority 2 properties.

You can use IEEE 1588 boundary clocks and transparent switches to measure and correct
 time skew across large networks. A boundary clock is a network switch with an
 accurate IEEE 1588 clock. A switch acting as a boundary clock runs the PTP protocol
 and is synchronized to an attached master clock. The boundary clock then acts as a
 master clock to all attached slaves. Boundary clocks do not pass Sync, Follow_Up,
 Delay_Req, or Delay_Resp messages. Within a subnet, a port of a boundary clock acts
 just like an ordinary clock with respect to synchronization and the BMC algorithm.
 Boundary clocks define a parent-child hierarchy of master-slave clocks: the boundary
 clock internally selects a port that sees the best clock as the single slave port,
 which then becomes a slave in the selected subnet. All other ports of the boundary
 clock internally synchronize to this slave port. Using a boundary clock, all
 internal latencies and jitter in the switch can be compensated for and do not affect
 synchronization accuracy.

Transparent switches solve the same problem as boundary clocks, but in a slightly
 different manner. A transparent switch is so called because it does not operate as a
 PTP node in an IEEE 1588-2008 system. Instead, it modifies the timing contents of
 PTP packets to account for the delay caused by the switch. Typically, a transparent
 switch calculates how much time a sync packet spends inside the switch, and then
 modifies the timestamp of the associated follow up packet to account for this delay.
 The use of transparent switches allows PTP nodes to operate as if they were all part
 of one LAN segment connected by hubs.

Parent topic:

Time Synchronization Protocols in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=ieee-802-1as-time-synchronization-protocol.html language=enus -->
## TOPIC 00017: IEEE 802.1AS Time Synchronization Protocol

- bundle_id: `ni-sync`
- source_path: `ieee-802-1as-time-synchronization-protocol.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/ieee-802-1as-time-synchronization-protocol.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 802.1AS time synchronization protocol is supported only on Linux RT targets. The IEEE 802.1AS generalized precision time protocol (gPTP) is a standard based on IEEE 1588 that is better optimized for time-sensitive applications. Like 1588, 802.1AS controls synchronization across a series of nod

### IEEE 802.1AS Time Synchronization Protocol

Note

The IEEE 802.1AS generalized precision time protocol (gPTP) is a standard based on IEEE
 1588 that is better optimized for time-sensitive applications. Like 1588, 802.1AS
 controls synchronization across a series of nodes connected by Ethernet cables,
 switches, and bridges by automatically designating a grandmaster clock using the Best
 Master Clock algorithm (BMCA). The grandmaster clock then serves as the source of time
 to slave devices (devices not elected as the 1588 grandmaster) across the network.

Each distributed device runs the BMCA to determine the highest ranking, most accurate
 device clock on the network, which automatically becomes the grandmaster. If the
 grandmaster clock leaves the network or is no longer the most accurate clock on the
 network, the BMCA selects a new grandmaster. The BMCA defines a standard set of clock
 characteristics—such as the origin of a clock's time source and the stability of the
 clock's frequency—and then assigns a value to each clock in order to determine the
 grandmaster. The BMCA also takes into account user-defined priority values, which you
 can set using the 802.1AS Priority1 and 802.1AS Priority2 properties.

One of the main differences between 802.1AS and 1588 is that 802.1AS requires
 802.1AS-capable network switches and network interfaces providing hardware-assisted
 timestamping in order to operate. You can determine whether or not a device is capable
 of running 802.1AS using the AS Capable property.

Parent topic:

Time Synchronization Protocols in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=irig-b-time-synchronization-protocol.html language=enus -->
## TOPIC 00018: IRIG-B Time Synchronization Protocol

- bundle_id: `ni-sync`
- source_path: `irig-b-time-synchronization-protocol.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/irig-b-time-synchronization-protocol.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: IRIG-B is one of six serial protocols for distributing time codes currently defined by the Inter Range Instrumentation Group (IRIG). The six IRIG protocols mainly differ in the frame size or the amount of time before new information is sent. IRIG-B is the most common IRIG standard and the one NI-Syn

### IRIG-B Time Synchronization Protocol

IRIG-B is one of six serial protocols for distributing time codes currently defined by
 the Inter Range Instrumentation Group (IRIG). The six IRIG protocols mainly differ in
 the frame size or the amount of time before new information is sent.

IRIG-B is the most common IRIG standard and the one NI-Sync devices use. IRIG-B is an
 encoded TLL signal that carries the absolute time. It is similar to a pulse per second
 (PPS) signal, but instead of outputting a single uniform pulse every second, IRIG-B
 sends coded bits that make up a one-second-long data frame, and it repeats or
 re-synchronizes every second. IRIG-B specifies that a 100-bit time frame is transmitted
 once per second, with each bit being represented as a 10 ms period.

The 0 bit represents 2 ms of a high logic state, the 1 bit represents a 5 ms high, and
 the P bit represents an 8 ms high. The P bit also separates seconds from minutes,
 minutes from hours, and so on, within the one-second frame. Data in the time frame
 includes Binary Coded Decimal (BCD) time of year, year, and straight binary seconds
 (SBS). The data can be DC biased (DC) or amplitude modulated (AM) with a 1 kHz sine
 wave.

The reception of the first bit of an IRIG-B data frame generates a timestamp for the
 event. You cannot read or use the timestamp as a time reference until the entire IRIG-B
 frame has been received and decoded. After the frame is successfully decoded, the frame
 drives the time reference engine if you have set IRIG-B as the external time reference.
 Both the timestamp generated by receiving the first frame bit and the time/date encoded
 in the IRIG-B frame can be read using the Read Last IRIG or GPS Time Stamp VI.

Parent topic:

Time Synchronization Protocols in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=locking-to-an-external-time-reference.html language=enus -->
## TOPIC 00019: Locking to an External Time Reference

- bundle_id: `ni-sync`
- source_path: `locking-to-an-external-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/locking-to-an-external-time-reference.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Selecting a Time Reference Complete the following steps to wait until the module is locked to the selected time reference before continuing the program: Place a While Loop. Place an niSync Property Node inside the While Loop. Select Timing»Is Time Reference Present as the first parame

### Locking to an External Time Reference

Prerequisites: Selecting a Time Reference

Complete the following steps to wait until the module is locked to the selected time
 reference before continuing the program:

1. Place a While Loop .
2. Place an niSync Property Node inside the While Loop.
3. Select Timing»Is Time Reference Present as the first
 parameter of the niSync Property Node. This property returns TRUE if your selected
 time reference is detected.
4. Add another parameter to the niSync Property Node and select
 Timing»Offset from Time Reference (ns) . This property
 returns the offset between your timing module and the selected time reference. Note You can also select
 Offset from Time Reference (s) to measure the offset in seconds instead of
 nanoseconds.
5. Determine whether or not the offset from the selected time reference is within an
 acceptable range for synchronization:
  1. Place the Less? function on the block diagram.
  2. Connect the Offset from Time Reference parameter to
 x of the Less? function.
  3. Wire a constant to y of the Less? function and set
 the value as needed to achieve the appropriate level of synchronization for
 your application. Note If you are using GPS as
 the selected time reference, you can achieve higher synchronization
 accuracy if you wait until the self-survey is complete before
 continuing. You can monitor the status of the self-survey using the
 Percent Complete of Self Survey property.
6. Place the And function on the block diagram.
7. Wire x < y? of the Less? function to the first input of
 the And function and the value from the Is Time Reference
 Present parameter to the second input.
8. Wire the output of the And function to the conditional terminal. The conditional
 terminal automatically stops the While Loop when the selected time reference is
 present and when the offset is less than the value you set for
 y of the Less? function.

You created a program that waits until your module is synchronized with the selected time
 reference before continuing.

Parent topic:

Time References in NI-Sync

Related concepts:

- Selecting a Time Reference

<!--NI_TOPIC bundle=ni-sync path=manually-correcting-a-time-reference.html language=enus -->
## TOPIC 00020: Manually Correcting a Time Reference

- bundle_id: `ni-sync`
- source_path: `manually-correcting-a-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/manually-correcting-a-time-reference.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Selecting a Time Reference Complete the following steps to manually adjust a selected time reference: Place an niSync Property Node. Wire the instrument handle of the NI-Sync session to reference. Select Timing»Time Reference Correction as the first parameter of the niSync Property No

### Manually Correcting a Time Reference

Prerequisites: Selecting a Time Reference

Complete the following steps to manually adjust a selected time reference:

1. Place an niSync Property Node.
2. Wire the instrument handle of the NI-Sync session to
 reference .
3. Select Timing»Time Reference Correction as the first
 parameter of the niSync Property Node.
4. Right-click Time Reference Correction and select
 Change To Write .
5. Wire a control or constant to Time Reference Correction .
6. Set the offset, in seconds, to apply to the selected time reference.

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=ni-sync path=new-features-and-changes.html language=enus -->
## TOPIC 00021: NI-Sync New Features and Changes

- bundle_id: `ni-sync`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-Sync. Discover what is new in the latest releases of NI-Sync.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### NI-Sync
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-Sync.

NI-Sync

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-Sync
 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-Sync 2025 Q1.

##### New
 Features

This version of NI-Sync provides
 support for the following feature:

- Added support for LabVIEW 2025 Q1.

<!--NI_TOPIC bundle=ni-sync path=phase-locking-to-an-external-clock-using-a-pl.html language=enus -->
## TOPIC 00022: Phase Locking to an External Clock Using a PLL Circuit

- bundle_id: `ni-sync`
- source_path: `phase-locking-to-an-external-clock-using-a-pl.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/phase-locking-to-an-external-clock-using-a-pl.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the phase-locked loop (PLL) circuit on an NI-Sync device to synchronize your system timing module's oscillator to an external reference clock. Once the oscillator is synchronized, you can route it to the backplane using the PXI_Clk10_In connector, which can then phase lock the PXI_Clk10 and PXIe

### Phase Locking to an External Clock Using a PLL Circuit

[IMAGE alt='image' src='GUID-228393CA-6216-427F-AF32-775DC22D9CD3-a5.gif']

Use the phase-locked loop (PLL) circuit on an NI-Sync device to synchronize your system
 timing module's oscillator to an external reference clock. Once the oscillator is
 synchronized, you can route it to the backplane using the PXI_Clk10_In connector, which
 can then phase lock the PXI_Clk10 and PXIe_Clk100 signals to the oscillator. Using a PLL
 circuit, you can perform the following actions:

- Align the frequency of your system timing module's oscillator with an external
 clock.
- Lock PXI_Clk10 and PXIe_Clk100 to the same external reference clock.
- Phase-lock PXI_Clk10 to a higher frequency clock.
- Lock multiple boards to a shared reference signal that is not interrupted even if
 the external reference clock is disconnected.

Parent topic:

Clocks in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=pulse-per-second-pps-time-synchronization-pro.html language=enus -->
## TOPIC 00023: Pulse Per Second (PPS) Time Synchronization Protocol

- bundle_id: `ni-sync`
- source_path: `pulse-per-second-pps-time-synchronization-pro.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/pulse-per-second-pps-time-synchronization-pro.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pulse per second (PPS) is the simplest form of synchronization. PPS is a signal that outputs a high logic level once a second. It does not contain information about the specific time of day or year. The pulse width is generally 100 ms. You can input a PPS signal on a PFI, PXI_Trig, or PXI_Star line.

### Pulse Per Second (PPS) Time Synchronization Protocol

Pulse per second (PPS) is the simplest form of synchronization. PPS is a signal that
 outputs a high logic level once a second. It does not contain information about the
 specific time of day or year. The pulse width is generally 100 ms. You can input a PPS
 signal on a PFI, PXI_Trig, or PXI_Star line.

Selecting PPS as the time reference for an NI-Sync device configures the device to
 interpret a rising edge on the configured input as representing a second's boundary.
 Since the PPS signal cannot indicate an absolute time, you can configure the device to
 use either a manual start time or its current board time, and use the PPS signal only to
 correct frequency.

If you configure the device to use a manual start time, the device will use the first
 pulse received on the PPS input terminal as the configured start time. The device
 interprets every subsequent pulse as occurring one second after the previous pulse.
 Using this configuration, you can synchronize multiple systems equipped with NI-Sync
 timing devices if absolute time is not a concern. You can use PPS as the time reference
 for all the systems you want to synchronize and then configure them with the same manual
 start time. You can then connect the PPS signal to the systems and start the PPS output.
 Since the systems are connected to the same signal with the same start time, they are
 closely synchronized.

If you configure the device to use current time instead of the manual start time, the
 device interprets the first pulse received as the time equal to the device's current
 time. The device applies no correction when the first pulse is received, so it
 interprets every subsequent pulse as occurring one second after the previous pulse. You
 can use this configuration to distribute frequency corrections to multiple systems
 without concern for actual time values.

For best results when using PPS as a selected time reference, ensure that the device
 supplying the PPS signal provides a stable, consistent 1 Hz signal. You can achieve
 optimal results when an OCXO, TCXO, or better oscillator drives the source signal. You
 can introduce error into the system if the reference signal contains significant jitter
 or the reference frequency strays from 1 Hz.

Parent topic:

Time Synchronization Protocols in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=routing-a-synchronization-clock-along-a-trigg.html language=enus -->
## TOPIC 00024: Routing a Synchronization Clock Along a Trigger Line

- bundle_id: `ni-sync`
- source_path: `routing-a-synchronization-clock-along-a-trigg.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/routing-a-synchronization-clock-along-a-trigg.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Setting and Dividing a Synchronization Clock You can route full-speed or divided synchronization clocks through trigger lines using niSync Connect Trigger Terminals. Using this technique, you can export a DDS clock using a PFI line and send full-speed or divided clocks along routes th

### Routing a Synchronization Clock Along a Trigger Line

Prerequisites: Setting and Dividing a Synchronization Clock

Caution

Complete the following steps to route a synchronization clock along a trigger line:

1. Place niSync Connect Trigger Terminals.
2. Wire a constant or control to source and
 destination .
3. Select Synchronization Clock (Divided 2) for
 source . This divides the synchronization clock by the
 value you set in the Clock Divisor 2 parameter of the niSync Property Node and uses
 the result as the source for this trigger. You can also select
 Synchronization Clock (Divided 1) or
 Synchronization Clock (Full Speed) .
4. Select a destination for niSync Connect Trigger Terminals:
  - Select a PXI_Star line to route the specified clock through the backplane
 trigger lines of your chassis.
  - Select a front panel terminal (PFI, PFI_LVDS) to route the specified clock
 through the front zone of your chassis to another PXI chassis, a physically
 connected module in the same chassis, or an external device.
  - Select PXIe_DStarB to route the specified clock from a system timing module
 to a peripheral slot.
  - Select PXIe_DStarC to route the specified clock from a peripheral slot to a
 system timing module.
5. Place niSync Disconnect Trigger Terminals to free the trigger lines for other
 applications.
6. Place niSync Close to end the NI-Sync session.

After completing the preceding steps, the synchronization clock you set using the niSync
 Property Node is routed to a different location in your chassis using a trigger line.

Parent topic:

Using Synchronization Clocks in NI-Sync

Related concepts:

- Setting and Dividing a Synchronization Clock

<!--NI_TOPIC bundle=ni-sync path=routing-and-locking-to-the-pll-reference-cloc.html language=enus -->
## TOPIC 00025: Routing and Locking to the PLL Reference Clock

- bundle_id: `ni-sync`
- source_path: `routing-and-locking-to-the-pll-reference-cloc.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/routing-and-locking-to-the-pll-reference-cloc.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Enabling and Configuring a Phase-Locked Loop After you phase lock the oscillator of the system timing module to an external clock connected to ClkIn, complete the following steps to route the external reference clock from ClkIn to the PXI_Clk10_In connector and wait until the system i

### Routing and Locking to the PLL Reference Clock

Prerequisites: Enabling and Configuring a Phase-Locked Loop

After you phase lock the oscillator of the system timing module to an external clock
 connected to ClkIn, complete the following steps to route the external reference clock
 from ClkIn to the PXI_Clk10_In connector and wait until the system is phase-locked:

1. Place niSync Connect Clock Terminals.
2. Select ClkIn as the source and select
 PXI_Clk10_In as the
 destination .
3. Place a While Loop. Adding a While Loop ensures that the system is phase locked
 before moving on.
4. Place an niSync Property Node inside the While Loop.
5. Select Clk Properties»PLL Locked? as the first parameter of
 the niSync Property Node.
6. Wire PLL Locked? to the conditional terminal of the While
 Loop to stop the loop once the system is phase locked.
  - (Optional) Wire an indicator to the PLL Locked? 
 parameter to display PLL lock status on the front panel.
7. (Optional) Add a Wait function inside the While Loop to delay iterations of the
 loop. This eases the load on your processor.
8. Place niSync Disconnect Clock Terminals outside the While Loop and wire
 source and destination to close
 the clock route between ClkIn and PXI_Clk10_In.
9. Place niSync Close to terminate the NI-Sync session.

This program disconnects the clock at ClkIn right after the PLL circuit is locked. To
 maintain the phase lock throughout a program, place your code outside the While Loop and
 before niSync Disconnect Clock Terminals. You can now use the phase-locked backplane
 clock to synchronize modules within the chassis or export it for multi-chassis
 synchronization.

Parent topic:

Phase Locking to an External Clock Using a PLL Circuit

Related concepts:

- Enabling and Configuring a Phase-Locked Loop

<!--NI_TOPIC bundle=ni-sync path=routing-clock-signals-between-devices.html language=enus -->
## TOPIC 00026: Routing Clock Signals Between Devices

- bundle_id: `ni-sync`
- source_path: `routing-clock-signals-between-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/routing-clock-signals-between-devices.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-Sync clock terminal VIs to route clock signals between modules and chassis. You can use this functionality to synchronize multiple chassis using a single 10 MHz backplane clock, distribute a generated clock to different devices and modules, replace the 10 MHz backplane clock with a more p

### Routing Clock Signals Between Devices

Use the NI-Sync clock terminal VIs to route clock signals between modules and chassis.
 You can use this functionality to synchronize multiple chassis using a single 10 MHz
 backplane clock, distribute a generated clock to different devices and modules, replace
 the 10 MHz backplane clock with a more precise TCXO or OCXO from a timing and
 synchronization module, or synchronize devices and modules to an external clock
 connected to the ClkIn front panel connector.

Complete the following steps to connect clock terminals using NI-Sync:

1. Place niSync Initialize.
2. Place niSync Connect Clock Terminals.
3. Wire a control or constant to source and
 destination and select the source and destination
 terminals for the new clock route. Refer to Clock Terminal Connections for a list of
 compatible clock routes.
4. Place niSync Disconnect Clock Terminals and wire the clock source to
 source and the clock destination to
 destination .
5. Place niSync Close to close the NI-Sync I/O session.

Note

Refer to the Route Clock example for a demonstration of connecting and routing clock
 terminals. Access the Route Clock example by opening the NI Example Finder and selecting
 Hardware Input and Output»Timing and Synchronization»Signal-Based»Route
 Clock.vi.

[IMAGE alt='image' src='GUID-12F77DE4-1929-429A-B1CC-9DE3F4E6D1FF-a5.gif'] Open
 example [IMAGE alt='image' src='GUID-31770893-B6C8-4D87-AA04-0683C43E5657-a5.gif'] Find
 related examples

Parent topic:

Clocks in NI-Sync

Related concepts:

- Clock Terminal Connections

<!--NI_TOPIC bundle=ni-sync path=routing-trigger-signals-between-devices.html language=enus -->
## TOPIC 00027: Routing Trigger Signals Between Devices

- bundle_id: `ni-sync`
- source_path: `routing-trigger-signals-between-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/routing-trigger-signals-between-devices.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-Sync trigger VIs to connect trigger lines in a single or multiple PXI chassis. Triggers are an essential component of a signal-based synchronization application. You can accomplish the following tasks using trigger terminals: Share a trigger signal to start data acquisition on multiple de

### Routing Trigger Signals Between Devices

[IMAGE alt='image' src='GUID-0C008219-AC7E-4C83-8F6B-246ED75E28AE-a5.gif']

Use the NI-Sync trigger VIs to connect trigger lines in a single or multiple PXI chassis.
 Triggers are an essential component of a signal-based synchronization application. You
 can accomplish the following tasks using trigger terminals:

- Share a trigger signal to start data acquisition on multiple devices at the same
 time.
- Share a sync pulse to align common clocks on multiple chassis.
- Synchronize the system timing module and any connected peripherals with DStar
 terminals.
- Route digital signal pulses between multiple chassis or between modules in a single
 chassis.
- Distribute divided or full-speed clock signals between modules.

In addition to using the hardware trigger lines, you can also set up a software trigger
 in NI-Sync. A software trigger fires when you invoke niSync Send Software Trigger,
 allowing you to fire the trigger at a specific time in the program or let the user fire
 the trigger with a front panel button or switch.

Parent topic:

Triggers in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=selecting-a-time-reference.html language=enus -->
## TOPIC 00028: Selecting a Time Reference

- bundle_id: `ni-sync`
- source_path: `selecting-a-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/selecting-a-time-reference.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: The selected time reference is used by NI-Sync to drive time on a device; in other words, NI-Sync matches the device's time to that of the device's selected time reference. Each device can have a maximum of one selected time reference. Complete the following steps to set a selected time reference: S

### Selecting a Time Reference

The selected time reference is used by NI-Sync to drive time on a device; in other words,
 NI-Sync matches the device's time to that of the device's selected time reference. Each
 device can have a maximum of one selected time reference. Complete the following steps
 to set a selected time reference:

#### Selecting a Time Reference for a PXI
 Module

1. Place niSync Initialize.
2. Select a PXI timing and synchronization module as the resource
 name for niSync Initialize.
3. Place niSync Set Time Reference.
4. Select an instance of niSync Set Time Reference. You can select GPS, IRIG, PPS,
 or 1588 Ordinary Clock using niSync Set Time Reference. You can also put the
 device in Free Running mode.

The time reference you chose with niSync Set Time Reference becomes the selected time
 reference for the device specified in resource name.

Tip

Hardware Input
 and Output»Timing and Synchronization»Time-based»Set Time
 Reference.vi

Note

#### Selecting a Time Reference for a
 Linux RT Target

Unlike selecting a time reference for a PXI module, you cannot manually select a time
 reference on a Linux RT target. Instead, the most accurate time reference is
 automatically determined and selected for the user. However, you can manually enable
 or disable time references on a Linux RT target, allowing you to determine which
 time references are eligible to be selected. Only an enabled time reference can be
 the selected time reference.

Complete the following steps to enable and/or disable time references on a Linux RT
 target:

1. Place niSync Initialize.
2. Select a Linux RT device as the resource name for niSync
 Initialize.
3. Place niSync Get Time References to retrieve a list of time references installed
 on the device.
4. Place an niSync Property Node and select Active Item as the first property.
5. Specify the time reference to enable or disable by wiring it from the output of
 niSync Get Time References to Active Item.
6. Expand the niSync Property Node and select Time Reference Enabled
 (niSync » Timing » Time
 Reference » Time Reference Enabled) as the second
 property.
7. Right-click the Time Reference Enabled property and select Change to
 Write .
8. Enable or disable the time reference:
  - To enable the time reference, select TRUE.
  - To disable the time reference, select FALSE.

The time reference connected to Active Item is either enabled or disabled. An
 enabled time reference is eligible to be chosen as the selected time reference.

Parent topic:

Time References in NI-Sync

Related concepts:

- Time References in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=setting-and-dividing-a-synchronization-clock.html language=enus -->
## TOPIC 00029: Setting and Dividing a Synchronization Clock

- bundle_id: `ni-sync`
- source_path: `setting-and-dividing-a-synchronization-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/setting-and-dividing-a-synchronization-clock.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to set and divide the synchronization clock of the front and rear zones of a PXI or PXIe chassis: Place niSync Initialize. Place niSync Property Node and select Synchronization Clock Properties»Synchronization Clock Source (PFI, PFI_LVDS) as the first parameter. Right-cl

### Setting and Dividing a Synchronization Clock

Complete the following steps to set and divide the synchronization clock of the front and
 rear zones of a PXI or PXIe chassis:

1. Place niSync Initialize.
2. Place niSync Property Node and select Synchronization Clock
 Properties»Synchronization Clock Source (PFI, PFI_LVDS) as the first
 parameter.
3. Right-click the Synchronization Clock Source (PFI, PFI_LVDS) 
 parameter and select Change To Write .
4. Wire a control or constant to the Synchronization Clock Source (PFI,
 PFI_LVDS) parameter. The value you select here becomes the
 synchronization clock for the front zone of your PXI chassis, which comprises the
 front panel inputs and outputs of each module. The default is PXI_Clk10.
5. Add another parameter to the niSync Property Node and select
 Synchronization Clock Properties»Synchronization Clock Source
 (PXI_Trig, PXI_Star, PXIe_DStarB) .
6. Wire a control or constant to the Synchronization Clock Source (PXI_Trig,
 PXI_Star, PXIe_DStarB) parameter. The value you select here becomes
 the synchronization clock for the back zone of your PXI chassis, which includes all
 the chassis' backplane trigger lines. The default is PXI_Clk10.
7. Add another parameter to the niSync Property Node and select
 Synchronization Clock Properties»Clock Divisor 1 as the
 third parameter. Note Clock Divisor parameters apply to whatever
 synchronization clock source is placed in the same niSync Property Node. This
 example sets a clock divisor for both the front and rear zone synchronization
 clocks, but if the niSync Property Node only contained Synchronization Clock
 Source (PFI, PFI_LVDS), the Clock Divisor parameters would only divide the
 synchronization clock for the front zone.
8. (Optional) Add a fourth parameter to the niSync Property Node and select
 Synchronization Clock Properties»Clock Divisor 2 to use a
 second value to divide the synchronization clock.
9. Wire a control or a constant to the Clock Divisor 1 and/or
 Clock Divisor 2 parameters and set the number(s) you
 would like to divide the clock by. Note Values for the
 Clock Divisor 1 and Clock Divisor
 2 parameters must be a power of 2, up to 512.

When you complete the preceding steps, you have successfully set the synchronization
 clock source for both the front and rear zones of the chassis. You have also created two
 divided synchronization clocks using the values you set for the Clock Divisor 1 and
 Clock Divisor 2 parameters.

Parent topic:

Using Synchronization Clocks in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=synchronization-methods.html language=enus -->
## TOPIC 00030: Synchronization Methods

- bundle_id: `ni-sync`
- source_path: `synchronization-methods.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/synchronization-methods.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`

### Synchronization Methods

- [Comparing Signal-Based and Time-Based Synchronization](comparing-signal-based-and-time-based-synchro.html)
- [Using Signal-Based Synchronization in NI-Sync](using-signal-based-synchronization-in-ni-sync.html)
- [Using Time-Based Synchronization in NI-Sync](using-time-based-synchronization-in-ni-sync.html)

<!--NI_TOPIC bundle=ni-sync path=target-support-for-timing-properties-and-vis.html language=enus -->
## TOPIC 00031: Target Support for Timing Properties and VIs

- bundle_id: `ni-sync`
- source_path: `target-support-for-timing-properties-and-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/target-support-for-timing-properties-and-vis.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many timing properties and VIs are supported only on certain targets. Refer to the tables below to determine whether or not a given property or VI is supported on your chosen target. Target Support for Timing Properties Property 6683(H)Windows 6683(H)Linux RT and DT cRIO, Vision Industrial Controlle

### Target Support for Timing Properties and VIs

Many timing properties and VIs are supported only on certain targets. Refer to the tables
 below to determine whether or not a given property or VI is supported on your chosen target.

#### Target Support for Timing Properties

| Property | 6683(H)Windows | 6683(H)Linux RT and DT | cRIO, Vision Industrial Controller Linux RT | Ethernet cDAQ Linux RT |
| --- | --- | --- | --- | --- |
| Timing Properties |  |  |  |  |
| Selected Time Reference Type | Yes | Yes | Yes | Yes |
| Selected Time Reference Name | Yes | Yes | Yes | Yes |
| Is Time Reference Present | Yes | Yes | No | No |
| Offset from Time Reference (ns) | Yes | Yes | Yes | Yes |
| Offset from Time Reference (s) | Yes | Yes | Yes | Yes |
| Time Reference Correction | Yes | Yes | No | No |
| UTC Offset | Yes | No | No | No |
| UTC Offset Valid | Yes | No | No | No |
| Clock Resolution | Yes | Yes | No | No |
| Last Synchronization ID | Yes | Yes | Yes | No |
| Timing:Time Reference |  |  |  |  |
| Time Reference Type | No | Yes | Yes | Yes |
| Time Reference Enabled | No | Yes | Yes | Yes |
| Is Time Reference Selected | No | Yes | Yes | Yes |
| Timing:Time Reference:1588 |  |  |  |  |
| BMCA Mode | No | Yes | Yes | No |
| Clock Accuracy | Yes | Yes | Yes | Yes |
| Clock Class | Yes | Yes | Yes | Yes |
| Clock ID | Yes | Yes | Yes | Yes |
| Clock State | Yes | Yes | Yes | No |
| Frequency Traceable | Yes* | Yes* | Yes* | No |
| Grandmaster Clock Accuracy | Yes | Yes | Yes | Yes |
| Grandmaster Clock Class | Yes | Yes | Yes | Yes |
| Grandmaster Clock ID | Yes | Yes | Yes | Yes |
| Grandmaster IP Address | No | Yes | Yes | No |
| Grandmaster Priority1 | Yes | Yes | Yes | Yes |
| Grandmaster Priority2 | Yes | Yes | Yes | Yes |
| Interface Name | No | Yes | Yes | No |
| IP Address | Yes | Yes | No | No |
| Leap59 | Yes* | Yes* | Yes* | No |
| Leap61 | Yes* | Yes* | Yes* | No |
| Log Sync Interval | Yes | Yes | Yes | No |
| Mean Path Delay | Yes | Yes | Yes | No |
| Offset Scaled Log Variance | Yes* | Yes* | Yes* | No |
| Priority1 | Yes | Yes | Yes | Yes |
| Priority2 | Yes | Yes | Yes | Yes |
| Steps to Grandmaster | Yes | Yes | Yes | No |
| Time Source | Yes* | Yes* | Yes* | No |
| Time Traceable | Yes* | Yes* | Yes* | No |
| Timing:Time Reference:802.1AS |  |  |  |  |
| Port State | No | Yes | Yes | No |
| Clock ID | No | Yes | Yes | Yes |
| Clock Class | No | Yes | Yes | Yes |
| Clock Accuracy | No | Yes | Yes | Yes |
| Priority1 | No | Yes | Yes | Yes |
| Priority2 | No | Yes | Yes | Yes |
| Grandmaster Clock ID | No | Yes | Yes | Yes |
| Grandmaster Clock Class | No | Yes | Yes | Yes |
| Grandmaster Clock Accuracy | No | Yes | Yes | Yes |
| Grandmaster Priority1 | No | Yes | Yes | Yes |
| Grandmaster Priority2 | No | Yes | Yes | Yes |
| Log Sync Interval | No | Yes | Yes | No |
| Log Announce Interval | No | Yes | Yes | No |
| Interface Name | No | Yes | Yes | No |
| Neighbor Propagation Delay Threshold (ns) | No | Yes | Yes | No |
| AS Capable | No | Yes | Yes | No |
| Timing:Time Reference:GPS |  |  |  |  |
| Is Antenna Connected | Yes | Yes | No | No |
| Mobile Mode | Yes | Yes | No | No |
| Percent Complete of Self Survey | Yes | Yes | No | No |
| Recalculate Position on Reboot | Yes | Yes | No | No |
| Satellites Available | Yes | Yes | No | No |
| Status | Yes | Yes | No | No |
| Timing:Time Stamps |  |  |  |  |
| Available Time Stamps | Yes | Yes | No | No |
| Time Stamp Buffer Size | Yes | Yes | No | No |
| * Support was added in NI-Sync 2022 Q4. |  |  |  |  |

#### Target Support for Timing VIs

| LabVIEW VI | 6683(H)Windows | 6683(H)Linux RT and DT | cRIO, Ethernet cDAQ*, Industrial Controller†Linux RT |
| --- | --- | --- | --- |
| Clear Clock | Yes | Yes | No |
| Clear Future Time Events | Yes | Yes | No |
| Create Clock | Yes | Yes | No |
| Create Future Time Event | Yes | Yes | No |
| Disable Time Stamp Trigger | Yes | Yes | No |
| Enable Time Stamp Trigger | Yes | Yes | No |
| Get Time | Yes | Yes | Yes |
| Disable GPS or IRIG Timestamping | Yes | Yes | No |
| Enable GPS or IRIG Timestamping | Yes | Yes | No |
| Get Location | Yes | Yes | No |
| Get Velocity | Yes | Yes | No |
| Read Last GPS or IRIG Timestamp | Yes | Yes | No |
| Get Time References | Yes | Yes | Yes |
| Reset Frequency | Yes | Yes | No |
| Set Time | Yes | Yes | No |
| Set Time Reference | Yes | Yes | No |
| Start Time Reference | Yes | Yes | No |
| Stop Time Reference | Yes | Yes | No |
| * Linux RT support for cRIO and Industrial Controller modules was first added in NI-Sync 18.0. † Linux RT support for cDAQ was first added in NI-Sync 18.1. |  |  |  |

<!--NI_TOPIC bundle=ni-sync path=testing-the-stability-of-an-external-irig-sou.html language=enus -->
## TOPIC 00032: Testing the Stability of an External IRIG Source

- bundle_id: `ni-sync`
- source_path: `testing-the-stability-of-an-external-irig-sou.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/testing-the-stability-of-an-external-irig-sou.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prerequisites: Selecting a Time Reference You can test the stability of an external IRIG source relative to a selected time reference using NI-Sync. Complete the following steps to build a basic program to judge if the stability of an IRIG source is appropriate for your application: Set the selected

### Testing the Stability of an External IRIG Source

Prerequisites: Selecting a Time Reference

You can test the stability of an external IRIG source relative to a selected time
 reference using NI-Sync. Complete the following steps to build a basic program to judge
 if the stability of an IRIG source is appropriate for your application:

1. Set the selected time reference of a time-based timing and synchronization module to
 the time reference you want to measure IRIG stability against.
2. Place niSync Enable GPS or IRIG Timestamping.
3. Select the IRIG instance and set the IRIG
 type you would like to measure, either IRIGB
 AM or IRIGB DC .
4. Wire the hardware terminal containing the external IRIG source to
 terminal of niSync Enable GPS or IRIG Timestamping.
5. Place a While Loop.
6. Place niSync Read Last GPS or IRIG Timestamp in the While Loop, select the
 IRIG instance, and wire the following terminals:
  1. Wire the NI-Sync instrument handle to instrument
 handle .
  2. Wire the terminal containing the external IRIG source to
 terminal .
  3. Wire indicators to IRIG Time and
 timestamp .
7. Place niSync Disable GPS or IRIG Timestamping outside of the While Loop, select the
 IRIG instance, and wire the relevant terminals.
8. Place niSync Close to end the NI-Sync session.

On every iteration of the While Loop, the program returns the IRIG-B timestamp and a
 timestamp of the board time when the module received the IRIG-B message. The difference
 between these two timestamps is the offset. You can use the offset to help determine if
 the IRIG-B source is stable enough for your application. Using a While Loop returns
 multiple timestamps, which allows you to perform a more detailed analysis of the offset.

Parent topic:

IRIG-B Time Synchronization Protocol

Related concepts:

- Selecting a Time Reference

<!--NI_TOPIC bundle=ni-sync path=time-references-and-protocols.html language=enus -->
## TOPIC 00033: Time References and Protocols

- bundle_id: `ni-sync`
- source_path: `time-references-and-protocols.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/time-references-and-protocols.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Selecting a Time Reference Locking to an External Time Reference Creating and Reading Timestamps IEEE 1588-2008 IEEE 802.1AS GPS PPS IRIG-B Testing the Stability of an External IRIG Source

### Time References and Protocols

- [Time References in NI-Sync](time-references-in-ni-sync.html)
- [Time Synchronization Protocols in NI-Sync](time-synchronization-protocols-in-ni-sync.html)

<!--NI_TOPIC bundle=ni-sync path=time-references-in-ni-sync.html language=enus -->
## TOPIC 00034: Time References in NI-Sync

- bundle_id: `ni-sync`
- source_path: `time-references-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/time-references-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Sync time-based family of devices introduces the concept of a time reference as a means to synchronize time on a device. A time reference represents a potential source of time that NI-Sync can refer to when adjusting a device's time. A time reference typically incorporates a time synchronizat

### Time References in NI-Sync

The NI-Sync time-based family of devices introduces the concept of a time
 reference as a means to synchronize time on a device. A time reference
 represents a potential source of time that NI-Sync can refer to when adjusting a
 device's time. A time reference typically incorporates a time synchronization protocol,
 a set of standards that controls how timing information is sent and received from a
 separate device that provides the reference time, like an external clock.

The time reference is responsible for translating this timing information into
 adjustments that NI-Sync periodically applies to the device's time. NI-Sync allows a
 system to have multiple time references available and enabled at once, but only one time
 reference, the selected time reference, is used in adjusting the
 device's time. Once the device has an established notion of time from the selected time
 reference, it can be used by the system or applications to generate synchronous
 triggers, create backplane clocks aligned with other devices, timestamp events that
 correlate with other device times, and more.

Device time continues to advance even when NI-Sync is not actively receiving adjustments
 from the selected time reference. This behavior allows for a continuous source of time
 to the system and applications. However, if a selected time reference is not available
 and NI-Sync is not able to periodically adjust the device time as a result, the device's
 onboard clock will drift and may eventually differ significantly from the desired
 reference time. You can use the NI-Sync API to monitor the status of the available and
 selected time references to determine if their device time is adequate for the intended
 application.

#### Time Reference States

The state of a time reference determines its role in synchronizing NI-Sync
 devices:

- Selected —The time reference is currently driving time on
 the device; in other words, the time reference is currently providing the
 reference time that NI-Sync periodically adjusts the device time to match. A
 device can have a maximum of one selected time reference at a time. A time
 reference must be enabled in order to be selected. 
 Note It is possible for a device to have no selected time
 reference, in which case the device's clock is free running. Some properties
 will return an empty string if there is no selected time reference.
- Enabled —The time reference is running (monitoring time,
 running a time synchronization protocol, etc.), but it is not necessarily
 driving time on the device. A time reference must be enabled in order to be
 selected.
- Disabled —The time reference is installed on the device,
 but it is not currently running. A time reference cannot be disabled and
 selected at the same time.

Parent topic:

Time References and Protocols

Related concepts:

- Time Synchronization Protocols in NI-Sync
- Selecting a Time Reference

<!--NI_TOPIC bundle=ni-sync path=time-synchronization-protocols-in-ni-sync.html language=enus -->
## TOPIC 00035: Time Synchronization Protocols in NI-Sync

- bundle_id: `ni-sync`
- source_path: `time-synchronization-protocols-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/time-synchronization-protocols-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: A time synchronization protocol is a specific set of standards that enables clocks distributed amongst different systems to maintain the same notion of time to within a certain degree of precision. PXI modules support four different time synchronization protocols: IEEE 1588-2008, GPS, PPS, and IRIG-

### Time Synchronization Protocols in NI-Sync

A time synchronization protocol is a specific set of standards that enables clocks
 distributed amongst different systems to maintain the same notion of time to within a
 certain degree of precision. PXI modules support four different time synchronization
 protocols: IEEE 1588-2008, GPS, PPS, and IRIG-B. Linux RT targets support the IEEE
 802.1AS time synchronization protocol in addition to the four previously-mentioned
 protocols.

Each time synchronization protocol follows different standards to encode and transmit
 time data. Though multiple time synchronization protocols can be running at the same
 time, only one time synchronization protocol can govern the device's various clocks.
 NI-Sync timing and synchronization modules support the following time synchronization
 protocols:

- IEEE 1588-2008—This time synchronization protocol synchronizes a group of device
 clocks distributed across a network, typically connected via Ethernet, to a single
 grandmaster device clock within the network. The grandmaster is automatically chosen
 with the Best Master Clock algorithm (BMCA). Each distributed device runs the BMCA
 to determine the highest ranking, most accurate device clock on the network. All the
 slave devices (devices not elected as the 1588 grandmaster) in the network
 synchronize to the grandmaster clock. If the grandmaster clock leaves the network or
 is no longer the most accurate clock on the network, the BMCA selects a new
 grandmaster.Unlike 802.1AS, 1588 can operate with or without hardware-assisted
 timestamping features. With hardware-assist, 1588 is typically accurate to within 1
 microsecond, and without (known as "software only" mode), it is accurate to within 1
 millisecond.
- IEEE 802.1AS—This time synchronization protocol is a simplified standard based on
 IEEE 1588 that is better optimized for time-sensitive applications. Like 1588,
 802.1AS uses the BMCA to determine a grandmaster clock, which then distributes
 timing information to the other devices in order to maintain synchronization. One of
 the main differences between 802.1AS and 1588 is that 802.1AS requires
 802.1AS-capable network switches and network interfaces providing hardware-assisted
 timestamping in order to operate. 802.1AS is typically accurate to sub-microsecond
 precision. Note The 802.1AS time synchronization protocol can be
 used only with Linux RT targets.
- Global Positioning Satellite (GPS)—This time synchronization protocol uses a network
 of satellites to create a radio frequency-encoded signal that provides time,
 position, and velocity information. GPS delivers a synchronization precision between
 the tens and hundreds of nanoseconds, depending on the number of satellites that are
 visible from your position (at least four satellites must be visible for GPS to
 function) and the accuracy of the antenna. GPS is the only NI-Sync compatible time
 synchronization protocol that returns velocity and position information.
- IRIG-B—This time synchronization protocol transmits encoded time data. Each data
 frame is one second long, and presents the time information in seconds, minutes, and
 days. LabVIEW and NI-Sync can decode IRIG packets into a readable timestamp format
 that you can then use to synchronize your devices. IRIG-B has a synchronization
 precision of tens of nanoseconds, making it one of the more precise protocols
 available for NI-Sync. To use IRIG-B as an NI-Sync time synchronization protocol,
 you must have an external IRIG signal generator connected to your module, typically
 through the PFI0 front panel connector of a time-based synchronization module.
- PPS—This time synchronization protocol is the simplest form of time-based
 synchronization. Pulse Per Second (PPS) outputs a signal at a high logic level once
 every second, with the leading edge aligned to the clock's seconds boundary. PPS
 doesn't contain any information about date, year, or position. You must specify a
 terminal to receive the PPS signal when you use the PPS protocol.

When a PXI-6683 device resets, its internal device time is set to the host time of the
 system it is in. Once it has an active time reference, the internal device time will
 become whatever the active time reference's time is. GPS, 1588, and 802.1as time
 reference sources are typically referenced to International Atomic Time (TAI). Free
 running, IRIG-B, and PPS sources are not necessarily referenced to any particular
 timescale.

The NI-Sync driver uses the International Atomic Time (TAI) standard to format timestamps
 regardless of what the active time reference's source is. TAI time is not adjusted for
 leap seconds. You can convert a LabVIEW timestamp to the TAI and 1588 format using
 niSync Convert Time Stamp to 1588 Time, or a 1588 timestamp to the LabVIEW format using
 niSync Convert 1588 Time to Time Stamp.

Parent topic:

Time References and Protocols

Related concepts:

- IEEE 1588-2008 Time Synchronization Protocol
- IEEE 802.1AS Time Synchronization Protocol
- GPS Time Synchronization Protocol
- IRIG-B Time Synchronization Protocol
- Pulse Per Second (PPS) Time Synchronization Protocol

<!--NI_TOPIC bundle=ni-sync path=trigger-terminal-connections.html language=enus -->
## TOPIC 00036: Trigger Terminal Connections

- bundle_id: `ni-sync`
- source_path: `trigger-terminal-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/trigger-terminal-connections.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following table to determine which trigger source terminals are compatible with which trigger destination terminals. You can connect trigger terminals with niSync Connect Trigger Terminals. Only devices in a system timing slot can use PXI_Star<n> terminals as a trigger source. Only devices i

### Trigger Terminal Connections

Note

- Only devices in a system timing slot can use
 PXI_Star<n> terminals as a trigger
 source.
- Only devices in a system timing slot can use
 PXIe_DStarB<n> terminals as a trigger
 source.
- Only devices in a peripheral slot can use
 PXIe_DStarC<n> terminals as a trigger
 source.

| Trigger Source | Trigger Destination |
| --- | --- |
| PXI_Trig<n> | PXI_Trig<n> (except for source PXI_Trig) PXI_Star<n> PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |
| PXI_Star<n> | PXI_Trig<n> PXI_Star<n> (except for source PXI_Star) PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |
| PXI_Star | Cannot be used as a trigger source terminal. |
| PFI<n> | PXI_Trig<n> PXI_Star<n> PFI<n> (except for source PFI terminal) PFI_LVDS<n> (except for source PFI terminal) PXIe_DStarB<n> PXIe_DStarC |
| PFI_LVDS<n> | PXI_Trig<n> PXI_Star<n> PFI<n> (except for source PFI_LVDS terminal) PFI_LVDS<n> (except for source PFI_LVDS terminal) PXIe_DStarB<n> PXIe_DStarC |
| Ground | PXI_Trig<n> PXI_Star<n> PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |
| Synchronization Clock Full Speed Divided 1 Divided 2 | PXI_Trig<n> PXI_Star<n> PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |
| ClkIn | PFI_LVDS<n> |
| PXIe_DStarC<n> | PXI_Trig<n> PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |
| PXIe_DStarB | PXI_Trig0 PXI_Star<n> PFI<n> PXIe_DStarB<n> PXIe_DStarC |

Parent topic:

Triggers in NI-Sync

<!--NI_TOPIC bundle=ni-sync path=triggers-in-ni-sync.html language=enus -->
## TOPIC 00037: Triggers in NI-Sync

- bundle_id: `ni-sync`
- source_path: `triggers-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/triggers-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`

### Triggers in NI-Sync

- [Routing Trigger Signals Between Devices](routing-trigger-signals-between-devices.html)
- [Connecting and Synchronizing Triggers](connecting-and-synchronizing-triggers.html)
- [Defining NI-Sync Trigger Terminals](defining-ni-sync-trigger-terminals.html)
- [Trigger Terminal Connections](trigger-terminal-connections.html)

<!--NI_TOPIC bundle=ni-sync path=troubleshooting-clock-terminals.html language=enus -->
## TOPIC 00038: Troubleshooting Clock Terminals

- bundle_id: `ni-sync`
- source_path: `troubleshooting-clock-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/troubleshooting-clock-terminals.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following techniques to troubleshoot errors you might encounter while routing clock signals and connecting clock terminals: Ensure that the source and/or destination terminals you selected are compatible with one another. Refer to Clock Terminal Connections for a list of compatible clock rou

### Troubleshooting Clock Terminals

Use the following techniques to troubleshoot errors you might encounter while routing
 clock signals and connecting clock terminals:

- Ensure that the source and/or destination terminals you selected are compatible with
 one another. Refer to Clock Terminal Connections for a list of compatible clock
 routes.
- Ensure that the source and/or destination terminals you selected physically exist on
 your hardware. Refer to your hardware documentation for specific information on its
 terminals and connections.
- Ensure that the source and/or destination terminals you selected are not already in
 use by another application. You can do this in Measurement & Automation Explorer
 (MAX) by selecting your device, opening the Test Panels 
 window, selecting the Measure tab, and clicking
 Update Line State . Occupied lines are green, unoccupied
 lines are gray. Note 
 The Measure tab is not available on every timing
 and synchronization module.
 Whenever you use niSync Connect Clock Terminals, you must disconnect the
 terminal route using niSync Disconnect Clock Terminals before you can
 use the terminals for another clock route.
- If you receive an error code, connect niSync Error Message to return a readable
 explanation of the error code.
- Ensure that the clock terminal you are connecting is valid for the module you are
 using. For example, only time-based timing and synchronization devices can use the
 BoardClk terminal.

Parent topic:

Troubleshooting

Related concepts:

- Clock Terminal Connections

<!--NI_TOPIC bundle=ni-sync path=troubleshooting-gps.html language=enus -->
## TOPIC 00039: Troubleshooting GPS

- bundle_id: `ni-sync`
- source_path: `troubleshooting-gps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/troubleshooting-gps.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following techniques to troubleshoot errors you might encounter while using GPS as an external time reference: Ensure that the module has a GPS receiver and a properly connected GPS antenna. Ensure that the GPS self survey is completed using the Percent Complete of Self Survey property. GPS

### Troubleshooting GPS

Use the following techniques to troubleshoot errors you might encounter while using GPS
 as an external time reference:

- Ensure that the module has a GPS receiver and a properly connected GPS antenna.
- Ensure that the GPS self survey is completed using the Percent Complete of Self
 Survey property. GPS is most accurate after the self survey.
- Ensure that the GPS receiver is not in mobile mode if your
 antenna is in a fixed position. Devices in mobile mode are not as accurate as
 stationary devices. You can return the status of mobile mode or activate mobile mode
 using the Mobile Mode property.
- Ensure that your GPS receiver is in mobile mode if you are trying
 to retrieve velocity and location information. Velocity and position information are
 only available while your device is in mobile mode.
- Ensure that there are at least four satellites visible from your GPS antenna. The
 more satellites that are visible, the more accurate GPS is. GPS does not function if
 less than four satellites are visible. You can confirm the number of visible
 satellites using the Satellites Available property.
- Ensure that you are within the maximum cable length for accurate GPS performance.
 Maximum cable length depends on the GPS antenna gain and the cable's loss per unit
 of distance. NI recommends a GPS signal strength of between -135 dBm and -120 dBm at
 the device's SMB input. Targeting a signal strength of -125 dBm at the SMB input,
 you can compute the maximum cable length as: Max_cable_loss = -130 dBm +
 antenna_gain - (-125 dBm) 
 Max_cable_length = Max_cable_loss /
 (loss_per_unit_of_distance) If you are not within the maximum
 cable length, the self-survey may not complete due to poor signal integrity.

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=ni-sync path=troubleshooting-time-references.html language=enus -->
## TOPIC 00040: Troubleshooting Time References

- bundle_id: `ni-sync`
- source_path: `troubleshooting-time-references.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/troubleshooting-time-references.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following techniques to troubleshoot errors you might encounter while selecting and locking to a time reference: Ensure the time reference you would like to select is enabled using the Is Time Ref Enabled property. Ensure that you selected the time reference you want to use for your device u

### Troubleshooting Time References

Use the following techniques to troubleshoot errors you might encounter while selecting
 and locking to a time reference:

- Ensure the time reference you would like to select is enabled using the Is Time Ref
 Enabled property.
- Ensure that you selected the time reference you want to use for your device using
 the Selected Time Reference Name and/or Selected Time Reference Type
 properties.
- Correct for the offset from the time reference using the Time Reference Correction
 property. You can return the offset using the Offset from Time Reference (s) or
 Offset from Time Reference (ns) property.
- Verify that the time reference you would like to select is compatible with the
 target. The 802.1AS time synchronization protocol is supported only on Linux RT
 targets.

Parent topic:

Troubleshooting

Related concepts:

- Manually Correcting a Time Reference

<!--NI_TOPIC bundle=ni-sync path=troubleshooting-trigger-terminals.html language=enus -->
## TOPIC 00041: Troubleshooting Trigger Terminals

- bundle_id: `ni-sync`
- source_path: `troubleshooting-trigger-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/troubleshooting-trigger-terminals.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following techniques to troubleshoot errors you might encounter while routing trigger signals and connecting trigger terminals: Ensure that the source and/or destination terminals you selected are compatible with one another. Refer to Trigger Terminal Connections for a list of compatible ter

### Troubleshooting Trigger Terminals

Use the following techniques to troubleshoot errors you might encounter while routing
 trigger signals and connecting trigger terminals:

- Ensure that the source and/or destination terminals you selected are compatible with
 one another. Refer to Trigger Terminal Connections for a list of compatible
 terminals. Tip You can
 also check for possible trigger routes in Measurement & Automation Explorer
 (MAX) by selecting your device and clicking the Device
 Routes tab.
- Ensure that the source and/or destination terminals you selected physically exist on
 your hardware. Refer to your hardware documentation for specific information on its
 terminals and connections.
- Ensure that the source and/or destination terminals you selected are not already in
 use by another application. You can do this in MAX by selecting your device, opening
 the Test Panels window, selecting the
 Measure tab, and clicking Update Line
 State . Occupied lines are green, unoccupied lines are gray. Note 
 The Measure tab is not available on every timing
 and synchronization module.
 Whenever you use niSync Connect Trigger Terminals, you must disconnect
 the terminal route using niSync Disconnect Trigger Terminals before you
 can use the terminals for another trigger route.
- Ensure that you set a value in the synchronization clock 
 terminal of niSync Connect Trigger Terminals if you are using the optional
 parameters update edge and invert . You
 must connect the source and the destination terminals synchronously for these
 parameters to work.
- If you are using PXIe_DStar triggers, ensure that you are using the right trigger
 line for the module you are trying to connect to. Refer to your chassis
 documentation to see a map of your chassis' differential star triggers.
- Ensure that your chosen trigger line is receiving a signal. You can determine the
 status of a line in two ways:
  - niSync Measure Frequency VI—Use this VI to return the frequency of a clock
 or trigger signal on a specific line. This VI does not work for time-based
 modules like the 6683(H).
  - niSync Property Node—Use the Trigger State Properties 
 to confirm that future time events are activating and to confirm that
 triggers and clocks created with niSync Create Clock are firing on a
 specific trigger line. Refer to Displaying the State of a Trigger Line as an
 Array for more information.

Parent topic:

Troubleshooting

Related concepts:

- Trigger Terminal Connections
- Displaying the State of a Trigger Line as an Array

<!--NI_TOPIC bundle=ni-sync path=troubleshooting.html language=enus -->
## TOPIC 00042: Troubleshooting

- bundle_id: `ni-sync`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/troubleshooting.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`

### Troubleshooting

- [Converting NI-Sync Error Codes to a User-Readable String](converting-ni-sync-error-codes-to-a-user-read.html)
- [Displaying the State of a Trigger Line as an Array](displaying-the-state-of-a-trigger-line-as-an.html)
- [Manually Correcting a Time Reference](manually-correcting-a-time-reference.html)
- [Troubleshooting Clock Terminals](troubleshooting-clock-terminals.html)
- [Troubleshooting Time References](troubleshooting-time-references.html)
- [Troubleshooting GPS](troubleshooting-gps.html)
- [Troubleshooting Trigger Terminals](troubleshooting-trigger-terminals.html)

<!--NI_TOPIC bundle=ni-sync path=user-manual-welcome.html language=enus -->
## TOPIC 00043: NI-Sync User Manual

- bundle_id: `ni-sync`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Sync User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-Sync
 User Manual

The NI-Sync User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-Sync
- NI-Sync Release Notes
- Interactive Activation Guide
- NI-Sync LabVIEW API Reference
- NI-Sync C API Reference
- NI Learning Center

<!--NI_TOPIC bundle=ni-sync path=using-signal-based-synchronization-in-ni-sync.html language=enus -->
## TOPIC 00044: Using Signal-Based Synchronization in NI-Sync

- bundle_id: `ni-sync`
- source_path: `using-signal-based-synchronization-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/using-signal-based-synchronization-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal-based synchronization is characterized by physically sharing a combination of clocks and triggers to synchronize data acquisition and instrument control. Using a signal-based synchronization method, you can route clock and trigger signals throughout the system with niSync Connect Clock Termin

### Using Signal-Based Synchronization in NI-Sync

Signal-based synchronization is characterized by physically sharing a combination of
 clocks and triggers to synchronize data acquisition and instrument control. Using a
 signal-based synchronization method, you can route clock and trigger signals throughout
 the system with niSync Connect Clock Terminals and niSync Connect Trigger Terminals.
 Once you connect clock and trigger terminals, the signals are used to synchronize
 devices and modules using the terminal routes you established.

Using the signal-based synchronization method, you can perform the following actions:

- Generate a clock that runs at user-defined frequency.
- Use triggers to synchronize data acquisition.
- Divide a clock to create new frequencies that are still synchronized with the main
 clock.
- Route clock and trigger terminals between devices using niSync Connect Clock
 Terminals and niSync Connect Trigger Terminals.
- Lock the backplane clock to an external device's clock using the PLL circuit.
- Discipline the backplane clock to a module's oscillator.
- Measure the frequency on a specific terminal using niSync Measure Frequency.

The clock signal(s) used to synchronize devices in the signal-based synchronization
 method can originate from an external clock connected to ClkIn, a DDS signal created
 with a signal-based timing and synchronization module, the backplane clock of a PXI or
 PXIe chassis, or the oscillator of the NI-Sync device.

#### Signal-Based Synchronization Phases

The signal-based synchronization method can be broken down into the following
 phases:

- Initialize —Create an NI-Sync session to establish
 communication with an NI signal-based timing and synchronization device. The
 niSync Initialize VI creates a unique session handle that identifies the device
 to subsequent NI-Sync nodes. You can also use niSync Initialize to reset the
 device to a known state and verify that the NI-Sync instrument driver is valid
 for the device.
- Configure Hardware —Set up your device for
 synchronization, typically using the niSync Property Node. You can choose the
 type of signal to generate or synchronize with, the frequency of the signal (if
 you are using DDS), and the synchronization clock the front and rear zones of
 your chassis should use.
- Connect Terminals —Connect clock and trigger terminals
 between modules and chassis. Use this step to route triggers to different parts
 of the chassis and synchronize modules to the same clock signal. During the
 Connect Terminals phase, you can connect source and destination terminals, set a
 synchronization clock for triggers, and discipline the backplane clock to a
 clock signal. You can use the niSync Connect Clock Terminals, niSync Connect
 Trigger Terminals, and niSync Connect Software Trigger VIs in the Connect
 Terminals phase.
- Configure and Perform Measurement —Begin data acquisition
 using the parameters you set in the Configure Hardware phase and the terminal
 routes you created in the Connect Terminals phases. Taking a measurement is an
 application-specific operation that usually involves the use of a separate API,
 such as NI-DAQmx. You can also return synchronization information using the
 niSync Property Node or send a software trigger using niSync Send Software
 Trigger in this phase.
- Disconnect Terminals —Disconnect the terminal routes you
 set up in the Connect Terminals phase. Once you disconnect terminals, they are
 free for use in other applications. You can use the niSync Disconnect Clock
 Terminals, niSync Disconnect Trigger Terminals, and niSync Disconnect Software
 Trigger VIs in this phase.
- Close —Close the NI-Sync session and end communication
 between the driver and your device using niSync Close. This phase is necessary
 for deallocating memory and freeing other operating system resources. You must
 close every NI-Sync session you initialize, even if an error occurs when you
 execute the program.

#### Signal-Based Advanced and Utility Functions

Functions and VIs that do not fall into the above signal-based synchronization phases
 are considered Advanced or Utility functions. You can access the Advanced palette by
 selecting NI-Sync»Advanced from the Functions palette, and
 the Utility palette by selecting NI-Sync»Utility.

Parent topic:

Synchronization Methods

<!--NI_TOPIC bundle=ni-sync path=using-synchronization-clocks-in-ni-sync.html language=enus -->
## TOPIC 00045: Using Synchronization Clocks in NI-Sync

- bundle_id: `ni-sync`
- source_path: `using-synchronization-clocks-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/using-synchronization-clocks-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use synchronization clocks to synchronize separate signals coming from the front and back zones of your PXI chassis. Using the niSync Property Node, you can set the synchronization clock for each zone. The synchronization clock can be the backplane clock, a generated DDS clock, a module's os

### Using Synchronization Clocks in NI-Sync

[IMAGE alt='image' src='GUID-3DBAAB52-5EAE-4E28-8E16-0C652CA5F5C6-a5.gif']

You can use synchronization clocks to synchronize separate signals coming from the front
 and back zones of your PXI chassis. Using the niSync Property Node, you can set the
 synchronization clock for each zone. The synchronization clock can be the backplane
 clock, a generated DDS clock, a module's oscillator, or a clock originating from the
 PFI0 or ClkIn front panel connector of your module. You can also use the niSync Property
 Node to divide down a synchronization clock into a lower frequency.

Dividing a synchronization clock is a good choice for applications where you want one set
 of triggers to fire more or less frequently than another while still having both sets of
 triggers synchronized to the same reference clock. You can use a full-speed or divided
 synchronization clock to perform the following actions:

- Synchronize the firing of triggers.
- Export a clock through a PXI_Star or PXIe_DStar line within a single chassis.
- Export a clock through a PFI or PFI_LVDS line to synchronize multiple chassis,
 modules, and/or devices with the clock.
- Use multiple sample clocks that run in different increments but have the same
 concept of time.
- Synchronize front panel inputs to a different frequency than the PXI backplane and
 vice versa.

Refer to the following topics to use synchronization clocks in a program:

- Setting and Dividing a Synchronization Clock
- Routing a Synchronization Clock Along a Trigger Line
- Firing Triggers with a Synchronization Clock

Parent topic:

Clocks in NI-Sync

Related concepts:

- Setting and Dividing a Synchronization Clock
- Routing a Synchronization Clock Along a Trigger Line
- Firing Triggers with a Synchronization Clock

<!--NI_TOPIC bundle=ni-sync path=using-time-based-synchronization-in-ni-sync.html language=enus -->
## TOPIC 00046: Using Time-Based Synchronization in NI-Sync

- bundle_id: `ni-sync`
- source_path: `using-time-based-synchronization-in-ni-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync/raw/resource/enus/using-time-based-synchronization-in-ni-sync.html
- document_id: `ni-sync`
- page_type: `leaf`
- content_type: `concept`
- source_description: Time-based synchronization—also known as a distributed clock synchronization—is characterized by the use of an external timing source such as GPS, 1588, or an external IRIG generator. The system timing module uses the external time reference to determine the present time and create a clock that is l

### Using Time-Based Synchronization in NI-Sync

Time-based synchronization—also known as a distributed clock synchronization—is
 characterized by the use of an external timing source such as GPS, 1588, or an external
 IRIG generator. The system timing module uses the external time reference to determine
 the present time and create a clock that is locked to the external source. The
 individual clocks of each module and device in the system are synchronized to the same
 external source, ensuring synchronization between nodes no matter how far apart they
 are. Devices act on timing signals originating from a local clock that is synchronized
 to the other clocks in the system, so instead of sharing timing signals directly, the
 devices periodically adjust their local timing sources to match the selected external
 time reference.

Using the time-based synchronization method, you can perform the following actions:

- Create future time events that execute at a specific board time to control clock and
 trigger signals.
- Write and read timestamps to measure clock skew, record the start time of data
 acquisition, and troubleshoot timing issues.
- Create timed loops that run at a specific time of the day.
- Discipline the backplane clock to an external time reference.
- Return the current date and time, or the date and time when a measurement was
 taken.
- Generate a sample clock that starts and stops at a specific board time.

Synchronizing distributed clocks requires constant adjustment. A clock is essentially a
 two-part device that consists of a frequency source and an accumulator. In theory, if
 you set two clocks identically and their frequency sources run at the exact same rate,
 they are synchronized indefinitely. In practice, however, clocks are set with limited
 precision, frequency sources run at slightly different rates, and the rate of a
 frequency source changes over time and temperature. Most time-based NI timing and
 synchronization devices use an oven-controlled crystal oscillator (OCXO) or a
 temperature-controlled crystal oscillator (TCXO) as a frequency source, but even these
 highly accurate frequency sources vary due to initial manufacturing tolerance,
 temperature and pressure changes, and aging.

Because of these instabilities, distributed clocks must be synchronized continually to
 match each other in frequency and phase. While a time-based system is generally not as
 accurate as a signal-based system, you can use the time-based synchronization method to
 synchronize complex systems with many different nodes spread out over a large area—even
 nodes that are moving— with no loss of accuracy. If you are using the GPS timing
 protocol, you can even measure the location, speed, and altitude of a node using
 time-based synchronization.

You can configure PXI modules to use four different external time references: IEEE
 1588-2008, GPS, IRIG-B, and PPS. Linux RT targets can also use IEEE 802.1AS as a time
 reference.

#### Time-Based Synchronization Phases

The time-based synchronization method can be broken down into the following
 phases:

- Initialize —Create an NI-Sync session to establish
 communication with a time-based module. niSync Initialize creates a unique
 session handle that identifies the device to subsequent NI-Sync nodes. You can
 also use niSync Initialize to reset the device to a known state and verify that
 the NI-Sync instrument driver is valid for the device.
- Configure Hardware —Set up your device for
 synchronization, typically by selecting an external time reference using niSync
 Set Time Reference. If you select IEEE 1588-2008 as the external time reference,
 you can also start participation in 1588 in this phase. You can use the niSync
 Property Node, niSync Set Time Reference, and niSync Start 1588 in the Configure
 Hardware phase.
- Get Time —Use niSync Get Time to return the current board
 time of your device, which is synchronized with the external time reference you
 select in the Configure Hardware phase. You can pass this board time on to
 subsequent nodes to schedule future time events, start clocks at a specific
 time, or create timed loops in the later phases.

In the following phases, you configure future time events, enable timestamps, and
 generate clocks. These phases are independent of each other; you can use all, none,
 or a combination of the phases with time-based synchronization.

- Create Future Time Event —Use niSync Create Future Time
 Event to schedule a future time event at a later point in the application. A
 future time event changes the signal at a specific terminal when the board time
 reaches a specified point. You can create multiple future time events that
 change the signal levels on different terminals, change the signal multiple
 times at the same terminal to create waveforms, or use the future time event as
 a trigger to start data acquisition. The terminal you create a future time event
 on cannot be used for other purposes until you clear the future time event.
- Enable Timestamp Trigger —Use niSync Enable Time Stamp
 Trigger to record a timestamp every time the signal at a specified terminal
 changes. This is useful for tracking future time events, recording the timing of
 data acquisition, and comparing clocks between devices to check for jitter and
 offset.
- Create Clock —Use niSync Create Clock to create a custom
 clock that is synchronized with the external timing reference. You can set the
 clock to run for a specific number of ticks per cycle, a set length of time, or
 at a certain frequency. You can use the board time you returned in the Get Time
 phase to determine when the created clock should start and stop.

In the following phases, you read timestamps you created and close the connections
 you established earlier in the application to free the resources for other uses.

- Read Trigger Timestamp —Use niSync Read Trigger Time Stamp
 to read the timestamps you recorded in the Enable Timestamp Trigger phase. You
 can read a single timestamp or multiple timestamps in this phase. You can only
 read timestamps if you enabled the timestamp trigger with niSync Enable Time
 Stamp Trigger.
- Clear Future Time Events/Disable Timestamp Trigger/Clear
 Clock —Disconnect the future time events, timestamp triggers, and
 clocks you created earlier in the program. Every time you create a future time
 event, enable a timestamp trigger, or create a clock, you must free the terminal
 at the end of the program using the appropriate VI. Use niSync Clear Future Time
 Events to remove future time events, niSync Disable Time Stamp Trigger to stop
 recording timestamps, and niSync Clear Clock to remove a generated clock from a
 terminal. If you selected IEEE 1588-2008 as the external time reference, you can
 also stop 1588 participation in this phase.
- Close —Close the NI-Sync session and end communication
 between the driver and your device using niSync Close. This phase is necessary
 for deallocating memory and freeing other operating system resources. You must
 close every NI-Sync session you initialize, even if an error occurs when you
 execute the program.

#### Time-Based Advanced and Utility Functions

Functions and VIs that do not fall into the above time-based synchronization phases
 are considered Advanced or Utility functions. You can access the Advanced palette by
 selecting NI-Sync»Advanced from the Functions palette, and
 the Utility palette by selecting NI-Sync»Utility. Functions
 dealing with IEEE 1588-2008 and GPS also have their own palettes. Access the 1588
 palette by selecting NI-Sync»Timing»1588 and the GPS palette
 by selecting NI-Sync»Timing»GPS.

Parent topic:

Synchronization Methods

Related concepts:

- IEEE 1588-2008 Time Synchronization Protocol
- GPS Time Synchronization Protocol
- IRIG-B Time Synchronization Protocol
- Pulse Per Second (PPS) Time Synchronization Protocol
- IEEE 802.1AS Time Synchronization Protocol
