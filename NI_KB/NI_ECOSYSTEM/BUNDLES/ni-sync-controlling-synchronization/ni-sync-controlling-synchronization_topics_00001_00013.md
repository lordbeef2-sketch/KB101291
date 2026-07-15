# NI DOCUMENT BUNDLE: ni-sync-controlling-synchronization

<!--NI_BUNDLE_CHUNK bundle=ni-sync-controlling-synchronization start=1 end=13 -->
<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=connect-reference-clock-pxi-clk10.html language=enus -->
## TOPIC 00001: Connecting an External Reference Clock to a PXI Backplane Clock

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `connect-reference-clock-pxi-clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/connect-reference-clock-pxi-clk10.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the following procedure to connect an external reference clock to the backplane clock of a PXI chassis. You can do this to synchronize a backplane clock to an external reference clock. Alternately, you can discipline the 10 MHz backplane clock with an OCXO on a timing and synchronization module

Connecting an External Reference Clock to a PXI Backplane Clock

Use the following procedure to connect an external reference clock to the backplane clock of a PXI chassis. You can do this to synchronize a backplane clock to an external reference clock. Alternately, you can discipline the 10 MHz backplane clock with an OCXO on a timing and synchronization module installed in the PXI chassis.

- NI-Sync 17.0 or above.
- An external reference clock.

1. Connect the external 10 MHz reference source to the CLKIN connector on the device in the system timing slot of the PXI chassis.

Program the Route from ClkIn to PXI_Clk10_IN

1. Call [Initialize (niSync)](/csh?topicname=initialize-nisync.html)to set up a handle for the device.
2. This step is only necessary if you are using a PXI-6674T in the system timing slot. Set the Use PLL? property to 
 False. 
 
 The PXI-6674T will not use a phase-locked loop to sync with PXI_Clk10_In.
  1. Place [niSync Properties](/csh?topicname=nisync-properties.html) on the diagram.
  2. Select 
 Clock from the drop-down menu and select Use PLL? as the first property.
  3. Right-click Use PLL? and select 
 Change to Write.
  4. Connect a Boolean constant to Use PLL? and set it to 
 False.
3. Place [Connect Clock Terminals](/csh?topicname=connect-clock-terminals.html). Set the source terminal to 
 ClkIn and the destination terminal to 
 PXI_Clk10_In. 
 The external reference clock connected to ClkIn is now routed to the PXI backplane clock.
4. Place [Close](/csh?topicname=close.html) on the diagram to close the niSync session.

Parent topic:

Using an External Time Reference in NI-Sync

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=connecting-and-synchronizing-triggers.html language=enus -->
## TOPIC 00002: Routing and Synchronizing Triggers with niSync Connect Trigger Terminals

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `connecting-and-synchronizing-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/connecting-and-synchronizing-triggers.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: How to connect trigger terminals and synchronize triggers using NI-Sync. You can use Connect Trigger Terminals to link hardware trigger lines together. You can also use Connect Software Trigger to connect the global software trigger to a destination trigger terminal. Place Initialize on the diagram.

Routing and Synchronizing Triggers with niSync Connect Trigger Terminals

How to connect trigger terminals and synchronize triggers using NI-Sync.

Connect Trigger Terminals

Connect Software Trigger

1. Place Initialize on the diagram.
2. Place Connect Trigger Terminals or Connect Software Trigger on the block diagram.
3. Wire a constant or control to source terminal and destination terminal and select the source of the trigger and the destination to connect it to.
4. (Optional) Set additional parameters for the new trigger route:
  1. Select a value for synchronization clock. Use this value to send the trigger signal from the source terminal to the destination terminal asynchronously or on an update edge of the specified clock.
  2. Select a value for update edge. Use this value to determine whether to align the trigger signal with the rising or falling edge of the synchronization clock.
  3. Select a value for invert. Use this value to determine whether to invert the source terminal signal when it reaches the destination terminal. You can use this terminal for differential analysis or to eliminate noise in your signal.
  4. If you are using Connect Software Trigger, select a value for delay. Use this value to delay firing the global software trigger by the selected value when you invoke Send Software Trigger.
5. (Optional) If you are using Connect Software Triggers, place Send Software Trigger in the place on the diagram where you would like to fire the software trigger.
6. Place Disconnect Trigger Terminals or Disconnect Software Trigger on the block diagram and wire the appropriate terminals.
7. Place Close on the diagram to close the NI-Sync I/O session.

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=creating-and-reading-timestamps.html language=enus -->
## TOPIC 00003: Creating and Reading Timestamps

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `creating-and-reading-timestamps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/creating-and-reading-timestamps.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Timestamps a user-generated clock using the NI-Sync timestamp functions and the Create Clock function. Use NI-Sync timestamp functions to record the board time when an event—like a clock edge, trigger, or future time event—occurs. You can use timestamps to measure clock drift and skew between device

Creating and Reading Timestamps

Timestamps a user-generated clock using the NI-Sync timestamp functions and the Create Clock function.

Note

- Timestamping is available only on time-based timing and synchronization modules.
- You can only timestamp terminals with I/O, such as trigger signals, future time events, synchronization clock signals, and clocks generated with DDS or Create Clock .

1. Place Initialize on the diagram.
2. Place Create Clock on the diagram and configure it.
  1. Select the 
 Ticks mode.
  2. Wire a control or constant to terminal and select the terminal you would like to create the clock on.
  3. Specify the number of high ticks and low ticks each clock cycle will have using high ticks and low ticks.
  4. (Optional) Specify a start and stop time for the clock using start time and stop time.
3. Place Enable Time Stamp Trigger on the diagram and configure it.
  1. Connect terminal to the same terminal you generated the clock on.
  2. (Optional) Wire a control or constant to decimation count to adjust the number of timestamps that occur between recorded timestamps.
  3. (Optional) Wire a control or constant to active edge to create timestamps on a specific clock edge.
4. Place Read Trigger Time Stamp on the block diagram and configure it.
  1. Select the 
 Single Timestamp mode to read the first timestamp written, or select the 
 Multiple Timestamps instance to read a specified number of timestamps.
  1. Wire terminal to the same terminal you generated the clock on.
  2. Wire an indicator to time stamp out. This returns an array of timestamps if you selected the Read Multiple Timestamps mode, or a single timestamp if you selected the Read Single Timestamp mode.
  3. (Optional) Wire an indicator to detected edge to return the clock edge the timestamp was recorded on.
  4. (Optional) Wire a control or constant to timeout to specify how long, in seconds, the function should try to read a timestamp before stopping.
  5. (Optional) If you selected the Read Multiple Timestamps instance, wire a control or constant to number of timestamps to specify how many timestamps the function should read.
5. Place Disable Time Stamp Trigger on the diagram and wire terminal to the same terminal you generated the clock on.
6. Place Clear Clock on the diagram and wire terminal to the terminal you generated the clock on.
7. Place Close on the diagram to end the NI-Sync session and free all resources for another program.

You have an application that records a timestamp whenever there is a rising edge to the clock you generate with Create Clock. You can substitute Create Clock with any clock signal, future time event, or trigger signal that you can propagate on a PFI or PXI_Trig line to timestamp those signals.

Parent topic:

Using an External Time Reference in NI-Sync

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=enabling-configuring-phase-locked-loop.html language=enus -->
## TOPIC 00004: Enabling and Configuring a Phase-Locked Loop

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `enabling-configuring-phase-locked-loop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/enabling-configuring-phase-locked-loop.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use an NI-Sync device's PLL circuit to phase lock the oscillator of the system timing module to an external clock. Connect an external clock to the ClkIn connector on the front panel of the module in the system timing slot of the chassis. Place Initialize on the diagr

Enabling and Configuring a Phase-Locked Loop

Complete the following steps to use an NI-Sync device's PLL circuit to phase lock the oscillator of the system timing module to an external clock.

1. Connect an external clock to the ClkIn connector on the front panel of the module in the system timing slot of the chassis.
2. Place Initialize on the diagram. Select the module in the chassis' system timing slot for resource name.
3. Place niSync Properties on the diagram.
4. Select 
 Clk Properties»Use PLL? for the first parameter of niSync Properties and set its value to 
 True.
5. Add another parameter to the niSync Properties and select 
 Clk Properties»PLL Frequency for the second parameter.
6. Right click the PLL Frequency parameter and select 
 Change to Write.
7. Wire a control or constant to the PLL Frequency parameter and enter the frequency of the external clock connected to ClkIn. Refer to the device's hardware manual for the reference frequency range supported by the device's PLL circuit. 
 The oscillator of the NI-Sync device is configured to phase-lock to the external clock connected at ClkIn. The oscillator locks to the frequency you specified in the PLL Frequency parameter.

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=fire-trigger-sync-clock.html language=enus -->
## TOPIC 00005: Firing Triggers with a Synchronization Clock

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `fire-trigger-sync-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/fire-trigger-sync-clock.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Describes how you can synchronously fire trigger using a synchronization clock. Setting and Dividing a Synchronization Clock After you have set a synchronization clock for the front and/or rear zones of your chassis, you can use the synchronization clock to control when triggers fire. You can set a

Firing Triggers with a Synchronization Clock

Describes how you can synchronously fire trigger using a synchronization clock.

Setting and Dividing a Synchronization Clock

After you have set a synchronization clock for the front and/or rear zones of your chassis, you can use the synchronization clock to control when triggers fire.

You can set a trigger to fire on an update edge of the full-speed or a divided synchronization clock. You can also fire a trigger asynchronously using this terminal, though a trigger synchronized to a time reference is generally more accurate than an asynchronous trigger. Using a synchronization clock to coordinate trigger firing is ideal for situations where you are trying to synchronize different signals coming through the front and rear zones of the chassis.

1. Place Connect Trigger Terminals on the diagram.
2. Wire instrument handle with the session handle from the niSync Properties function you used in Setting and Dividing a Synchronization Clock.
3. Set 
 Divided Clock 1 as the value for synchronization clock. This divides the frequency of the synchronization clock by the value you set in the Clock Divisor 1 property and uses the result as the synchronization clock frequency for this trigger. 
 org.dita.html5/xsl/topic.xsl 455Note You can also set the synchronization clock terminal to the following values: 
 Divided Clock 2—Fires the trigger on an update edge of the second divided clock you created with the Clock Divisor 2 property.Full Speed Clock—Fires the trigger on an update edge of the full-speed synchronization clock.Asynchronous—Fires the trigger independently of the synchronization clock.
4. Select the source terminal and destination terminal for this trigger. 
 The trigger is now set to fire on an update edge of the full-speed or divided synchronization clock.

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=locking-to-an-external-time-reference.html language=enus -->
## TOPIC 00006: Locking to an External Time Reference

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `locking-to-an-external-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/locking-to-an-external-time-reference.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Describes how to wait until the module is locked to an external time reference before continuing the program. Setting an External Time Reference Place a While Loop on the diagram. Place an niSync Properties on the diagram inside the While Loop. Select TimingTime ReferenceIs Time Reference Present as

Locking to an External Time Reference

Describes how to wait until the module is locked to an external time reference before continuing the program.

Setting an External Time Reference

1. Place a While Loop on the diagram.
2. Place an niSync Properties on the diagram inside the While Loop.
3. Select 
 Timing»Time Reference»Is Time Reference Present as the first parameter of niSync Properties. This property returns 
 True if the chosen time reference is detected.
4. Add another parameter to niSync Properties and select 
 Timing»Time Reference»Offset from Time Reference. This property returns the offset between the timing module and the external time reference.
5. Determine whether or not the offset from the time reference is within an acceptable range for synchronization:
  1. Place Less? function on the diagram.
  2. Connect the Offset from Time Reference property to x of the Less? function.
  3. Wire a constant to y of the Less? function and set the value as needed to achieve the appropriate level of synchronization for your application. If you are setting GPS as the external time reference, you can achieve higher synchronization accuracy if you wait until the self-survey is complete before continuing. You can monitor the status of the self-survey using niSync Properties.
6. Place the And function on the diagram.
7. Wire x < y? of the Less? function to the first input of the And function and the value from Is Time Reference Present? to the second input.
8. Wire the output of the And function to the conditional terminal. The conditional terminal automatically stops the While Loop when a time reference is present and when the offset is less than the value you set for y of the Less? function.

You created a program that sets the external time reference for the timing and synchronization module, and then waits until the module is synchronized with the time reference before continuing.

Parent topic:

Using an External Time Reference in NI-Sync

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=route-sync-clock-along-trigger-line.html language=enus -->
## TOPIC 00007: Routing a Synchronization Clock Along a Trigger Line

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `route-sync-clock-along-trigger-line.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/route-sync-clock-along-trigger-line.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: You can route full-speed or divided synchronization clocks through trigger lines using NI-Sync. With this technique, you can export a DDS clock using a PFI line and send full-speed or divided clocks along routes that are not accessible when you use clock terminals alone. Setting and Dividing a Synch

Routing a Synchronization Clock Along a Trigger Line

You can route full-speed or divided synchronization clocks through trigger lines using NI-Sync. With this technique, you can export a DDS clock using a PFI line and send full-speed or divided clocks along routes that are not accessible when you use clock terminals alone.

Setting and Dividing a Synchronization Clock

1. Place Connect Trigger Terminals on the diagram.
2. Wire a constant or control to source terminal and destination terminal.
3. Select 
 Synchronization Clock (Divided 2) for source terminal. This divides the synchronization clock by the value you set in the Clock Divisor 2 property of niSync Properties and uses the result as the source for this trigger. You can also select 
 Synchronization Clock (Divided 1) or 
 Synchronization Clock (Full Speed).
4. Select a destination terminal for Connect Trigger Terminals: 
 org.dita.html5/xsl/topic.xsl 455Caution Routing a clock signal through a PXI_Trig line is not recommended. due to poor clock signal integrity caused by the topology of the PXI_Trig lines. Use PXI_Star, PXIe_DStar, or PFI lines instead.
  - Select a PXI_Star line to route the specified clock through the backplane trigger lines of the chassis.
  - Select a front panel terminal (PFI, PFI_LVDS) to route the specified clock through the front zone of the chassis to another PXI chassis, a physically connected module in the same chassis, or an external device.
  - Select PXIe_DStarB to route the specified clock from a system timing module to a peripheral slot.
  - Select PXIe_DStarC to route the specified clock from a peripheral slot to a system timing module.
5. Place Disconnect Trigger Terminals on the diagram to free the trigger lines for other applications.
6. Place Close on the diagram to end the NI-Sync session. 
 The synchronization clock you set using niSync Properties is routed to a different location in the chassis using a trigger line.

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=routing-clock-signals.html language=enus -->
## TOPIC 00008: Routing Clock Signals Using niSync Connect Clock Terminals

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `routing-clock-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/routing-clock-signals.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Connects clock terminals using NI-Sync. Use this functionality to synchronize multiple chassis using a single 10 MHz backplane clock, distribute a generated clock to different devices and modules, replace the 10 MHz backplane clock with a more precise TCXO or OCXO from a timing and synchronization m

Routing Clock Signals Using niSync Connect Clock Terminals

Connects clock terminals using NI-Sync.

Use this functionality to synchronize multiple chassis using a single 10 MHz backplane clock, distribute a generated clock to different devices and modules, replace the 10 MHz backplane clock with a more precise TCXO or OCXO from a timing and synchronization module, or synchronize devices and modules to an external clock connected to the ClkIn front panel connector.

1. Place Initialize on the diagram.
2. Place Connect Clock Terminals on the block diagram.
3. Wire a control or constant to source terminal and destination terminal and select the source and destination terminals for the new clock route.
4. Place Disconnect Clock Terminals on the diagram and wire the clock source to source terminal and the clock destination to destination terminal.
5. Place Close on the diagram to close the NI-Sync I/O session.

Connect Clock Terminals

Disconnect Clock Terminals

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=routing-locking-pll-reference-clock.html language=enus -->
## TOPIC 00009: Routing and Locking to the PLL Reference Clock

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `routing-locking-pll-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/routing-locking-pll-reference-clock.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Routes the external reference clock from ClkIn to the PXI_Clk10_In connector and waits until the system is phase-locked. Enabling and Configuring a Phase-Locked Loop Place Connect Clock Terminals on the diagram. Select ClkIn as the source terminal and select PXI_Clk10_In as the destination terminal.

Routing and Locking to the PLL Reference Clock

Routes the external reference clock from ClkIn to the PXI_Clk10_In connector and waits until the system is phase-locked.

Enabling and Configuring a Phase-Locked Loop

1. Place Connect Clock Terminals on the diagram.
2. Select 
 ClkIn as the source terminal and select 
 PXI_Clk10_In as the destination terminal.
3. Place a While Loop on the diagram. 
 Adding a While Loop ensures that the system is phase-locked before moving on.
4. Place niSync Properties inside the While Loop.
5. Select 
 Clk Properties»PLL Locked? as the first parameter of niSync Properties.
6. Wire PLL Locked? to the conditional terminal of the While Loop to stop the loop once the system is phase-locked.
  1. (Optional) Wire an indicator to the PLL Locked? parameter to display PLL lock status on the front panel.
7. (Optional) Add a Wait function inside the While Loop to delay iterations of the loop. 
 Using the Wait function eases the load on the processor.
8. Place Disconnect Clock Terminals on the block diagram outside the While Loop and wire source terminal and destination terminal to close the clock route between ClkIn and PXI_Clk10_In.
9. Place Close on the diagram to terminate the NI-Sync session.

This program disconnects the clock at ClkIn right after the PLL circuit is locked. To maintain the phase lock throughout a program, place your code outside the While Loop and before Disconnect Clock Terminals. You can now use the phase-locked backplane clock to synchronize modules within the chassis or export it for multi-chassis synchronization.

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=set-divide-synchronization-clock.html language=enus -->
## TOPIC 00010: Setting and Dividing a Synchronization Clock

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `set-divide-synchronization-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/set-divide-synchronization-clock.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: The following steps will set and divide the synchronization clock of the front and rear zones of a PXI or PXIe chassis: Place Initialize on the diagram. Place niSync Properties on the diagram and select Synchronization Clock PropertiesSynchronization Clock Source (PFI, PFI_LVDS) as the first propert

Setting and Dividing a Synchronization Clock

The following steps will set and divide the synchronization clock of the front and rear zones of a PXI or PXIe chassis:

1. Place Initialize on the diagram.
2. Place niSync Properties on the diagram and select 
 Synchronization Clock Properties»Synchronization Clock Source (PFI, PFI_LVDS) as the first property.
3. Right-click the 
 Synchronization Clock Source (PFI, PFI_LVDS) property and select 
 Change to Write.
4. Wire a control or constant to the Synchronization Clock Source (PFI, PFI_LVDS) property. The value you select here becomes the synchronization clock for the front zone of the PXI chassis, which comprises the front panel inputs and outputs of each module. The default is PXI_CLK10.
5. Add another parameter to niSync Properties and select 
 Synchronization Clock Properties»Synchronization Clock Source (PXI_Trig, PXI_Star, PXIe_DStarB).
6. Wire a control or constant to the Synchronization Clock Source (PXI_Trig, PXI_Star, PXIe_DStarB) property. The value you select here becomes the synchronization clock for the back zone of the PXI chassis, which includes all the chassis' backplane trigger lines. The default is PXI_CLK10.
7. Add another parameter to niSync Properties and select 
 Synchronization Clock Properties»Clock Divisor 1 as the third property. 
 org.dita.html5/xsl/topic.xsl 455Note Clock Divisor properties apply to whatever synchronization clock source is placed in the same niSync Properties function. This example sets a clock divisor for both the front and rear zone synchronization clocks, but if niSync Properties only contained Synchronization Clock Source (PFI, PFI_LVDS), the Clock Divisor properties would only divide the synchronization clock for the front zone.
8. (Optional) Add a fourth parameter to niSync Properties and select 
 Synchronization Clock Properties»Clock Divisor 2 to use a second value to divide the synchronization clock.
9. Wire a control or a constant to the Clock Divisor 1 and/or Clock Divisor 2 parameters and set the number(s) you would like to divide the clock by. 
 org.dita.html5/xsl/topic.xsl 455Note Values for the Clock Divisor 1 and Clock Divisor 2 properties must be a power of 2, up to 512. 
 You have successfully set the synchronization clock source for both the front and rear zones of the chassis. You have also created two divided synchronization clocks using the values you set for the Clock Divisor 1 and Clock Divisor 2 properties.

Enter the tasks the user should do after finishing this task (optional).

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=setting-an-external-time-reference.html language=enus -->
## TOPIC 00011: Setting an External Time Reference

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `setting-an-external-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/setting-an-external-time-reference.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Sets an external time reference for a time-based synchronization module. Place Initialize on the diagram. Wire a control or constant to resource name and select a time-based timing and synchronization module. Place Set Time Reference on the diagram. Select a mode of Set Time Reference. You can set t

Setting an External Time Reference

Sets an external time reference for a time-based synchronization module.

1. Place Initialize on the diagram.
2. Wire a control or constant to resource name and select a time-based timing and synchronization module.
3. Place Set Time Reference on the diagram.
4. Select a mode of Set Time Reference. You can set the external time reference to GPS, 1588 Ordinary Clock, IRIG, or PPS. You can also put the device in Free Running mode.

Parent topic:

Using an External Time Reference in NI-Sync

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=testing-stability-external-irig-source.html language=enus -->
## TOPIC 00012: Testing the Stability of an External IRIG Source

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `testing-stability-external-irig-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/testing-stability-external-irig-source.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `task`
- source_description: Tests the stability of an external IRIG source relative to an external time reference like GPS or IEEE 1588-2008 using NI-Sync. Setting an External Time Reference Set the external time reference of a time-based timing and synchronization module to the source you want to measure IRIG stability agains

Testing the Stability of an External IRIG Source

Tests the stability of an external IRIG source relative to an external time reference like GPS or IEEE 1588-2008 using NI-Sync.

Setting an External Time Reference

1. Set the external time reference of a time-based timing and synchronization module to the source you want to measure IRIG stability against.
2. Place Enable GPS or IRIG Timestamping on the diagram.
3. Select the 
 IRIG mode and set the IRIG Type you would like to measure, either 
 IRIGB AM or 
 IRIGB DC.
4. Wire the hardware terminal containing the external IRIG source to terminal of Enable GPS or IRIG Timestamping.
5. Place a While Loop on the block diagram.
6. Place Read Last GPS or IRIG Timestamp in the While Loop, select the 
 IRIG mode, and wire the following terminals:
  1. Wire the NI-Sync instrument handle to instrument handle.
  2. Wire the terminal containing the external IRIG source to terminal.
  3. Wire indicators to IRIG Time and timestamp.
7. Place Disable GPS or IRIG Timestamping outside of the While Loop, select the 
 IRIG mode, and wire the relevant terminals.
8. Place Close on the diagram to end the NI-Sync session.

On every iteration of the While Loop, the program returns the IRIG-B timestamp and a timestamp of the board time when the module received the IRIG-B message. The difference between these two timestamps is the offset. You can use the offset to help determine if the IRIG-B source is stable enough for your application. Using a While Loop returns multiple timestamps, which allows you to perform a more detailed analysis of the offset.

Parent topic:

Using an External Time Reference in NI-Sync

<!--NI_TOPIC bundle=ni-sync-controlling-synchronization path=using-external-time-reference.html language=enus -->
## TOPIC 00013: Using an External Time Reference in NI-Sync

- bundle_id: `ni-sync-controlling-synchronization`
- source_path: `using-external-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-controlling-synchronization/raw/resource/enus/using-external-time-reference.html
- document_id: `ni-sync-controlling-synchronization`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using NI-Sync and a time-based synchronization module, you can discipline clocks and triggers to an external time reference such as GPS, IRIG-B, or IEEE 1588-2008. Before you can synchronize your devices, you must choose an external time reference for your device to synchronize with. Once you have s

Using an External Time Reference in NI-Sync

Using NI-Sync and a time-based synchronization module, you can discipline clocks and triggers to an external time reference such as GPS, IRIG-B, or IEEE 1588-2008. Before you can synchronize your devices, you must choose an external time reference for your device to synchronize with. Once you have selected a time reference for your device you can perform the following actions:

- Discipline the backplane clock to GPS, 1588, IRIG, or PPS.
- Slave other modules and devices to the external time reference.
- Return the current time or use the current time to fire future time events and triggers.
- Create clocks or future time events tied to a specific time.
- Return the status of the time reference, including offset, clock resolution, and master/slave status.
- Create and read timestamps from almost any terminal in your network of chassis.

Note

- You only can set the external time reference to IRIG-B if you have an external device capable of generating an IRIG signal physically connected to the PXI chassis.
- You must have a time-based timing and synchronization module such as the PXI-6683 in the system timing slot, or a PXI-6683H in a hybrid slot connected to the 10 MHz Ref In of the chassis SMB to BNC cable, in order to discipline the backplane clock to an external time reference using NI-Sync drivers alone.
