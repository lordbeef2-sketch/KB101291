# NI DOCUMENT BUNDLE: ni-daqmx

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx start=1 end=175 -->
<!--NI_TOPIC bundle=ni-daqmx path=2wireres.html language=enus -->
## TOPIC 00001: 2-Wire Resistance

- bundle_id: `ni-daqmx`
- source_path: `2wireres.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/2wireres.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resistance measurements in the range above 100 Ω are generally made using the 2-wire method shown in the following figure. The excitation current flows through the leads and the unknown resistance, R[meas]. Your device measures the voltage across the resistance through the same set of leads and comp

### 2-Wire Resistance

Resistance measurements in the range above 100 Ω are generally made using the 2-wire method shown in the following figure. The excitation current flows through the leads and the unknown resistance, R<sub>meas</sub>. Your device measures the voltage across the resistance through the same set of leads and computes the resistance accordingly.

Errors in the 2-wire measurements are introduced by the lead resistance, R<sub>Lead</sub>, when measuring lower resistances. Because there is a voltage drop across the lead resistance equal to I × R<sub>Lead</sub>, the voltage measured by your device is not exactly the same as the voltage across the resistance, R<sub>meas</sub>. Because typical lead resistances lie in the range of 0.01–1 Ω, accurate 2-wire resistance measurements are very difficult to obtain if R<sub>meas</sub> is below 100 Ω.

[IMAGE alt='image' src='GUID-52BC8BB5-8EBD-420A-9D35-74C38853E525-a5.svg']

Parent topic:

Common Sensors

<!--NI_TOPIC bundle=ni-daqmx path=3wireres.html language=enus -->
## TOPIC 00002: 3-Wire Resistance

- bundle_id: `ni-daqmx`
- source_path: `3wireres.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/3wireres.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the 3-wire resistance method, as shown in the following figure, to measure resistance on resistors that have three lead wires. The 3-wire method uses three test leads, one pair for the excitation current (EX+, EX-), and a third wire (Sense-) to compensate for the lead wire resistances. The third

### 3-Wire Resistance

Use the 3-wire resistance method, as shown in the following figure, to measure resistance on resistors that have three lead wires.

[IMAGE alt='image' src='GUID-7730891A-2CFE-4FD0-95C4-EF2E282E161F-a5.svg']

The 3-wire method uses three test leads, one pair for the excitation current (EX+, EX-), and a third wire (Sense-) to compensate for the lead wire resistances. The third wire measures the voltage developed over the lead resistance in the EX- leg of the excitation current path. By subtracting its value from the overall differential signal, the device can compensate for parasitic lead resistances in the EX+ leg. However, this would only compensate for lead resistance in the EX+ leg and not in the EX- leg. To compensate for lead resistance both in the EX- leg and in the EX+ leg, the device approximates the EX+ leg by assuming the voltage is the same as in the EX- leg. Thus the voltage between Sense- and EX- is multiplied by two before being subtracted from the overall differential signal. This method works well when lead resistances in the EX+ leg match resistances in the EX- leg.

Some legacy devices do not provide compensation. In that case, you need to specify the lead-wire resistance so that it can be subtracted in software.

Parent topic:

Common Sensors

<!--NI_TOPIC bundle=ni-daqmx path=430x-simultaneous-tasks.html language=enus -->
## TOPIC 00003: NI 4302, 4303, 4304, 4305 Simultaneous Tasks

- bundle_id: `ni-daqmx`
- source_path: `430x-simultaneous-tasks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/430x-simultaneous-tasks.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4302, 4303, 4304, and 4305 can run up to four analog input tasks simultaneously, each using independent timing and triggering configurations. Each task uses at least one of the four timing engines on the device. Each timing engine can control up to eight channels. If a task has more than eight c

### NI 4302, 4303, 4304, 4305 Simultaneous Tasks

The 4302, 4303, 4304, and 4305 can run up to four analog input tasks simultaneously, each using independent timing and triggering configurations. Each task uses at least one of the four timing engines on the device.

Each timing engine can control up to eight channels. If a task has more than eight channels, NI-DAQmx automatically uses multiple timing engines for the task, synchronizing and sharing settings across all timing engines. For example, if a task has 10 channels, NI-DAQmx uses two timing engines for the task, which leaves two timing engines for other tasks. If the task has 32 channels, all four timing engines are used for one task.

Each bank of 8 ADCs (ai0:7, ai8:15, ai16:23, ai23:31) must all be in the same sample mode (buffered or hardware timed single point). For example, if ai0 is used in a task configured for hardware timed single point, any task using ai1:7 must also use the hardware timed single point sample mode.

Each channel's gain can be independently configured regardless of what task it's in or what sample mode it's used with.

Parent topic:

Simultaneous Tasks

Related concepts:

- NI 4302, 4303, 4304, 4305 Timing Engines

<!--NI_TOPIC bundle=ni-daqmx path=430x-timing-engines.html language=enus -->
## TOPIC 00004: NI 4302, 4303, 4304, 4305 Timing Engines

- bundle_id: `ni-daqmx`
- source_path: `430x-timing-engines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/430x-timing-engines.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 4302, 4303, 4304, and 4305 have four timing engines. Each of these timing engines can have its own configuration settings for timing, triggering, and the sample mode (either buffered or hardware timed single point). Each timing engine can use any AI channel and can control up to eight channels.

### NI 4302, 4303, 4304, 4305 Timing Engines

The 4302, 4303, 4304, and 4305 have four timing engines. Each of these timing engines can have its own configuration settings for timing, triggering, and the sample mode (either buffered or hardware timed single point).

Each timing engine can use any AI channel and can control up to eight channels. Each channel can only be used once across all timing engines.

By default, NI-DAQmx automatically selects an available timing engine when reserving the task. Use the DAQmx Timing attribute/property SampTimingEngine to specify the timing engine to use or to determine which timing engine NI-DAQmx automatically selected.

Note

The SampTimingEngine attribute/property is an integer value corresponding to one of the four analog input timing engines available on the device:

| SampTimingEngine Value | Timing Engine Used |
| --- | --- |
| 0 | te0 |
| 1 | te1 |
| 2 | te2 |
| 3 | te3 |

If a task has more than eight channels, NI-DAQmx automatically uses multiple timing engines, synchronizing and sharing settings across all timing engines. All timing engines in a single task must share the same settings.

For example, if a task has 10 channels, NI-DAQmx uses two timing engines, which leaves two timing engines for other tasks. If the task has 32 channels, all four timing engines are used.

Each channel's digital filter settings can be configured independently if the channel is used in a task in buffered sample mode. For tasks using HWTSP sample mode, all channels in the task must have the same digital filter configuration.

Parent topic:

Multiple Timing Engines

Related concepts:

- Digital AI Filtering

<!--NI_TOPIC bundle=ni-daqmx path=653xphyschan.html language=enus -->
## TOPIC 00005: NI 6533/6534 Device Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `653xphyschan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/653xphyschan.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital Input and Output All NI 6533/6534 devices have 32 individually configurable lines of digital input and output that are grouped into four 8-bit ports. Port NI-DAQmx Physical Channel Name (Lines) NI-DAQmx Physical Channel Name (Ports)This physical channel name refers to all eight lines in a po

### NI 6533/6534 Device Physical Channels

Parent topic:

Physical Channels

#### Digital Input and Output

All NI 6533/6534 devices have 32 individually configurable lines of digital input and output that are grouped into four 8-bit ports.

| Port | NI-DAQmx Physical Channel Name (Lines) | NI-DAQmx Physical Channel Name (Ports)[1]1 This physical channel name refers to all eight lines in a port at once. |
| --- | --- | --- |
| Port 0 | Dev1/port0/line0 — Dev1/port0/line7 | Dev1/port0 |
| Port 1 | Dev1/port1/line0 — Dev1/port1/line7 | Dev1/port1 |
| Port 2 | Dev1/port2/line0 — Dev1/port2/line7 | Dev1/port2 |
| Port 3 | Dev1/port3/line0 — Dev1/port3/line7 | Dev1/port3 |

For Ports 0 through 3, you can configure a port width of eight, 16, or 32 bits. To configure a 32-bit port, use the physical channel name Dev1/port0_32. To configure a 16-bit port, use channel names that refer to all the lines in multiple consecutive ports: 
 Dev1/portP_N, where 
 P is the port number of the lowest numbered port, and 
 N is the total number of lines. For instance, combining Port 2 and 3 into a 16-bit port, you would specify 
 Dev1/port2_16 as the physical channel.

NI 6533/6534 devices also have eight fixed-direction lines, grouped into two ports, that use PFI lines. Port 4 is used for input operations; Port 5 is for output.

Port 4 and port 5 can be used as static digital I/O lines or PFI lines. When any of these PFI lines is used as a digital I/O signal, it uses the physical channel name shown in the following table.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI0 | Dev1/port4/line0 |
| PFI1 | Dev1/port4/line1 |
| PFI2 | Dev1/port4/line2 |
| PFI3 | Dev1/port4/line3 |
| PFI4 | Dev1/port5/line2 |
| PFI5 | Dev1/port5/line3 |
| PFI6 | Dev1/port5/line0 |
| PFI7 | Dev1/port5/line1 |

[<sup>1</sup>](#note_ref-d15677e102) This physical channel name refers to all eight lines in a port at once.

<!--NI_TOPIC bundle=ni-daqmx path=adtrig.html language=enus -->
## TOPIC 00006: Advance Trigger

- bundle_id: `ni-daqmx`
- source_path: `adtrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/adtrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: An Advance Trigger causes a switch device to execute the next entry in its instruction (scan) list. You can configure this trigger to occur on a digital edge or when the Send Software Trigger function/VI runs.

### Advance Trigger

An Advance Trigger causes a switch device to execute the next entry in its instruction (scan) list. You can configure this trigger to occur on a digital edge or when the Send Software Trigger function/VI runs.

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-daqmx path=aiconnectiso.html language=enus -->
## TOPIC 00007: Connecting Analog Voltage Input Signals for Isolated Devices

- bundle_id: `ni-daqmx`
- source_path: `aiconnectiso.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/aiconnectiso.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Input Signal Source Type Floating Signal Sources (Not Connected to Building Ground) Ground-Referenced Signal Sources Examples: Ungrounded thermocouples Signal conditioning with isolated outputs Battery devices Example: Plug-in instruments with non-isolated outputs Differential (DIFF) Referenced Sing

### Connecting Analog Voltage Input Signals for Isolated Devices

| Input | Signal Source Type |  |
| --- | --- | --- |
| Floating Signal Sources (Not Connected to Building Ground) | Ground-Referenced Signal Sources |  |
| Examples: Ungrounded thermocouples Signal conditioning with isolated outputs Battery devices | Example: Plug-in instruments with non-isolated outputs |  |
| Differential (DIFF) |  |  |
| Referenced Single-Ended (RSE) |  |  |

Parent topic:

NI-DAQmx Device Considerations

Related concepts:

- Terminal Configurations (Analog Input Ground Reference Settings) for Isolated Devices

<!--NI_TOPIC bundle=ni-daqmx path=aitermname.html language=enus -->
## TOPIC 00008: Analog Input Accessory Terminal Names

- bundle_id: `ni-daqmx`
- source_path: `aitermname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/aitermname.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the revised names for analog input terminal names. Original Terminal Names Revised Terminal Names Explanation AIGND, ACHGND AIGND The reference point for referenced single-ended measurements and the bias current return point for differential measurements ACH# AI# AI0, AI1,

### Analog Input Accessory Terminal Names

The following table lists the revised names for analog input terminal names.

| Original Terminal Names | Revised Terminal Names | Explanation |
| --- | --- | --- |
| AIGND, ACHGND | AIGND | The reference point for referenced single-ended measurements and the bias current return point for differential measurements |
| ACH# | AI# | AI0, AI1, and so on; the analog input channels |
| AISENSE | AISENSE | The reference point for NRSE measurements using channels 0-15 |
| AISENSE2 | AISENSE2 | The reference point for NRSE measurements using channels 16-79 |
| AISENSE3 | AISENSE3 | The reference point for NRSE measurements using channels 80-143 |
| AISENSE4 | AISENSE4 | The reference point for NRSE measurements using channels 144-207 |
| SCANCLK | AI HOLD COMP | The terminal where the AI Hold Complete Event signal appears |
| TRIG1 | AI START TRIG | Placed as a hint next to the PFI terminal where the AI Start Trigger can be emitted |
| TRIG2 | AI REF TRIG | Placed as a hint next to the PFI terminal where the AI Reference Trigger can be emitted |
| CONVERT* | AI CONV CLK | Placed as a hint next to the PFI terminal where the AI Convert Clock can be emitted |
| STARTSCAN | AI SAMP CLK | Placed as a hint next to the PFI terminal where the AI Sample Clock can be emitted |

Parent topic:

Terminal Names

Related concepts:

- Change Detection Considerations for NI 6527 Devices

<!--NI_TOPIC bundle=ni-daqmx path=algwindowtrig.html language=enus -->
## TOPIC 00009: Analog Window Triggering

- bundle_id: `ni-daqmx`
- source_path: `algwindowtrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/algwindowtrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A window trigger occurs when an analog signal either passes into (enters) or passes out of (leaves) a window defined by two voltage levels. Specify the levels by setting the window top value and the window bottom value. The following image demonstrates a trigger that acquires data when the signal en

### Analog Window Triggering

A window trigger occurs when an analog signal either passes into (enters) or passes out of (leaves) a window defined by two voltage levels. Specify the levels by setting the window top value and the window bottom value. The following image demonstrates a trigger that acquires data when the signal enters the window.

[IMAGE alt='image' src='GUID-B6AC9687-2846-4937-BD00-41E17D1C32F6-a5.svg']

The following image demonstrates a trigger that acquires data when the signal leaves the window.

[IMAGE alt='image' src='GUID-6E25E6DB-BAF5-427D-967C-29A4779B545A-a5.svg']

Parent topic:

Trigger Types

Related concepts:

- Analog Triggering Considerations for TestScale Modules and C Series, E Series, M Series, and S Series Devices
- Analog Triggering Considerations for SC Express Devices

<!--NI_TOPIC bundle=ni-daqmx path=amplification.html language=enus -->
## TOPIC 00010: Amplification

- bundle_id: `ni-daqmx`
- source_path: `amplification.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/amplification.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Amplification is a type of signal conditioning that improves accuracy in the resulting digitized signal by increasing signal amplitude relative to noise. For the highest possible accuracy, amplify the signal so the maximum voltage swing equals the maximum input range of the ADC, or digitizer. Your s

### Amplification

Amplification is a type of signal conditioning that improves accuracy in the resulting digitized signal by increasing signal amplitude relative to noise.

For the highest possible accuracy, amplify the signal so the maximum voltage swing equals the maximum input range of the ADC, or digitizer. Your system should amplify low-level signals at the measurement device located nearest the signal source, as shown in the following figure.

[IMAGE alt='image' src='GUID-3865E721-F72F-46FF-8CF2-512BB75F12F4-a5.svg']

Tip

If you amplify the signal at the measurement device, the signal is measured and digitized with noise that may have entered the lead wires. However, if you amplify the signal close to the signal source with an SCXI module, noise has less impact on the measured signal.

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx path=analeveltrig.html language=enus -->
## TOPIC 00011: Analog Level Triggering

- bundle_id: `ni-daqmx`
- source_path: `analeveltrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analeveltrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: An analog level trigger is similar to an analog edge trigger. With both trigger types, you specify the edge—rising or falling—and the trigger level. With an analog edge trigger, you are interested in the point at which the trigger condition is met. With an analog level trigger, on the other hand, yo

### Analog Level Triggering

An analog level trigger is similar to an analog edge trigger. With both trigger types, you specify the edge—rising or falling—and the trigger level. With an analog edge trigger, you are interested in the point at which the trigger condition is met. With an analog level trigger, on the other hand, you are interested in the 
 *duration* that the signal remains above or below the trigger level. An analog level trigger is typically used with a Pause Trigger. The Pause Trigger asserts or deasserts when the trigger condition is met. In the following illustration, a trigger asserts when the signal crosses above the trigger level and deasserts when it drops below it. The deassertion of the trigger could correspond to a Pause Trigger.

[IMAGE alt='image' src='GUID-DF2CE9B5-462D-4A9F-BB30-4D6F9E49E64A-a5.svg']

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-daqmx path=analog-multi-edge-triggering.html language=enus -->
## TOPIC 00012: Analog Multi Edge Triggering

- bundle_id: `ni-daqmx`
- source_path: `analog-multi-edge-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analog-multi-edge-triggering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: An analog multi edge trigger functions similar to an analog edge trigger. The analog multi edge trigger differs in that you can configure multiple channel sources acquiring in the same task to each have their own analog trigger condition. When any of the multiple channel sources satisfy their respec

### Analog Multi Edge Triggering

An analog multi edge trigger functions similar to an analog edge trigger. The analog multi edge trigger differs in that you can configure multiple channel sources acquiring in the same task to each have their own analog trigger condition. When any of the multiple channel sources satisfy their respective condition, a trigger is generated and the device will perform the specified action associated with the trigger.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-daqmx path=analog-output-programming-flowcharts.html language=enus -->
## TOPIC 00013: Analog Output Programming Flowcharts

- bundle_id: `ni-daqmx`
- source_path: `analog-output-programming-flowcharts.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analog-output-programming-flowcharts.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains general programming flowcharts that you can use when creating an application. You also can find programming flowcharts for typical applications—such as generating voltage and generating current—in the Common Applications section of this help file.In the programming flowcharts,

### Analog Output Programming Flowcharts

This section contains general programming flowcharts that you can use when creating an application. You also can find programming flowcharts for typical applications—such as generating voltage and generating current—in the Common Applications section of this help file.

In the programming flowcharts, many applications also include explicit control functions to start, stop, and clear the task. In LabVIEW, clearing occurs automatically. For other ADEs, you must include these functions in your application.

Functions and VIs provide the core functionality of the NI-DAQmx API. For instance, NI-DAQmx includes functions for timing, triggering, reading, and writing samples. However, for advanced functionality, Visual C++, Visual C#, Visual Basic .NET, and LabVIEW require properties. ANSI C and LabWindows/CVI employ the Get and Set Attribute functions. For more information, refer to the programming reference help for your ADE.

- [Single Sample Analog Output Programming Flowchart](single-sample-analog-output-programming-flowc.html)
- [Finite Analog Output Programming Flowchart](finite-analog-output-programming-flowchart.html)
- [Continuous Analog Output Programming Flowchart](continuous-analog-output-programming-flowchart.html)

Parent topic:

Generic Programming Flowcharts

Related concepts:

- Generating Voltage
- Measuring and Generating Current

<!--NI_TOPIC bundle=ni-daqmx path=analogconnconsid.html language=enus -->
## TOPIC 00014: Analog Connection Considerations

- bundle_id: `ni-daqmx`
- source_path: `analogconnconsid.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analogconnconsid.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: To measure analog signals, you need to know the signal source—grounded or floating. You also must consider the measurement system—differential, referenced single-ended, or nonreferenced single-ended.

### Analog Connection Considerations

To measure analog signals, you need to know the signal source—grounded or floating. You also must consider the measurement system—differential, referenced single-ended, or nonreferenced single-ended.

Parent topic:

Signal Types

Related concepts:

- Grounded Signal Sources
- Floating Signal Sources
- Differential Measurement System
- Referenced and Nonreferenced Single-Ended Measurement Systems

<!--NI_TOPIC bundle=ni-daqmx path=analogtrig.html language=enus -->
## TOPIC 00015: Analog Triggering

- bundle_id: `ni-daqmx`
- source_path: `analogtrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analogtrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about analog triggering for C Series, NI ELVIS II Family, DSA, E Series, M Series, S Series, and SC Express devices.

### Analog Triggering

This section contains information about analog triggering for C Series, NI ELVIS II Family, DSA, E Series, M Series, S Series, and SC Express devices.

- [Valid Analog Trigger Sources for DSA Devices](analogtrigdsa.html)
- [Analog Triggering Considerations for TestScale Modules and C Series, E Series, M Series, and S Series Devices](anltrigeseries.html#GUID-CCE9A924-46DE-4773-ABA7-25572B273E34)
- [Triggering Considerations for NI ELVIS II Family Devices](elvistriggering.html)
- [Analog Triggering Considerations for SC Express Devices](scexpressanlgtrigg.html)

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=analogtrigdsa.html language=enus -->
## TOPIC 00016: Valid Analog Trigger Sources for DSA Devices

- bundle_id: `ni-daqmx`
- source_path: `analogtrigdsa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analogtrigdsa.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog trigger source must be a channel included in your physical channel list. PFI 0 is not a valid analog trigger source. PFI 0 is reserved for digital triggers.

### Valid Analog Trigger Sources for DSA Devices

The analog trigger source must be a channel included in your physical channel list. PFI 0 is not a valid analog trigger source. PFI 0 is reserved for digital triggers.

Parent topic:

Analog Triggering

<!--NI_TOPIC bundle=ni-daqmx path=analogtriggering.html language=enus -->
## TOPIC 00017: Analog Edge Triggering

- bundle_id: `ni-daqmx`
- source_path: `analogtriggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/analogtriggering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: For analog edge triggering, you configure the measurement device to look for a certain signal level and slope (either rising or falling). After the device identifies the trigger condition, the device performs the specified action associated with the trigger, such as starting the measurement or marki

### Analog Edge Triggering

For analog edge triggering, you configure the measurement device to look for a certain signal level and slope (either rising or falling). After the device identifies the trigger condition, the device performs the specified action associated with the trigger, such as starting the measurement or marking which sample was acquired when the trigger occurred. You connect analog trigger signals to any analog input channel or terminal capable of accepting analog signals. Refer to the device-specific analog triggering considerations for your device for additional information.

In the following figure, the trigger is set to capture data for a rising edge signal when the signal reaches 3.2.

[IMAGE alt='image' src='GUID-7089A4AE-6509-44C7-88E2-4107C85A2812-a5.svg']

Hysteresis adds a window above or below the trigger level and often is used to reduce false triggering due to noise or jitter in the signal. When using hysteresis with a rising slope, the trigger asserts when the signal starts below level (or threshold level) minus hysteresis and then crosses above level. The trigger deasserts when the signal crosses below level minus hysteresis.

For example, if you add a hysteresis of 1 to the previous example, which used a level of 3.2, the signal must start at or drop below 2.2 for triggering to occur. The trigger then asserts as the signal rises above 3.2 and deasserts when it falls below 2.2.

[IMAGE alt='image' src='GUID-1119E349-ECE0-4E44-AAD6-0F2F25BAE19D-a5.svg']

When using hysteresis with a falling slope, the trigger asserts when the signal starts or rises above level (or threshold level) plus hysteresis and then crosses below level. The trigger deasserts when the signal crosses above level plus hysteresis. If you instead trigger on a falling edge at 3.2 with a hysteresis of 1, the signal must start at or rise above 4.2 and then fall below 3.2 for triggering to occur. The trigger will then assert as the signal falls below 3.2 and deassert when it rises above 4.2.

[IMAGE alt='image' src='GUID-2BC989E6-6611-4990-8283-C79FDDA73E8D-a5.svg']

Parent topic:

Trigger Types

Related concepts:

- Analog Triggering

<!--NI_TOPIC bundle=ni-daqmx path=anltrigeseries.html language=enus -->
## TOPIC 00018: Analog Triggering Considerations for TestScale Modules and C Series, E Series, M Series, and S Series Devices

- bundle_id: `ni-daqmx`
- source_path: `anltrigeseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/anltrigeseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all E Series, M Series, S Series, and C Series devices support analog triggering. Refer to the specifications for your device to determine if your device supports analog triggering. Certain C Series, E Series, M Series, S Series devices and TestScale modules contain a single analog trigger circu

### Analog Triggering Considerations for
 TestScale Modules and C Series, E Series, M Series, and S Series Devices

Note

Certain C Series, E Series, M Series, S Series devices and TestScale modules contain a single
 analog trigger circuit that you can configure for analog triggering. The analog trigger
 circuitry is a shared resource for the device, and any of the subsystems can use it. This
 trigger circuitry supports level and slope triggering with hysteresis as well as analog window
 triggering. After it is configured, the output of this circuitry appears as the Analog
 Comparison Event, which can be the source for various triggers and clocks within the analog
 input, analog output, and counter subsystems.

Parent topic:

Analog Triggering

#### Sharing an Analog Trigger for C Series, E Series, M Series, and S Series Devices

Even though the analog trigger is a shared resource, only one analog input or analog output task at a time can configure and reserve it. If you want to share the analog trigger among multiple tasks, configure and reserve it in one task, and use the trigger in subsequent tasks by referring to the source of your trigger, clock, or signal of interest as the Analog Comparison Event. For tasks that support multiple types of analog triggers within the same task, all triggers must share the same configuration settings, or you receive an error. For instance, if you want to use an analog trigger for both your Start and Reference Trigger within an analog input task, the configuration settings for the start and Reference Trigger must be identical.

#### E Series and S Series Valid Sources for the Analog Trigger

- PFI 0 
 Typically, when configuring an analog trigger, you connect your analog signal to the PFI 0 terminal. Because PFI 0 is the trigger source for both analog and digital signals, NI-DAQmx automatically tristates this terminal when a task exporting a signal on the terminal is not in the committed or running state. This behavior when exporting a signal on PFI 0 differs from typical task-based routing with other PFI lines. It prevents accidental connections of an analog signal directly to digital circuitry, which could permanently damage the device. Also, notice that when connecting an analog signal to PFI 0, the terminal configuration is referenced single-ended. Even when PFI 0 is not the source of your analog trigger, you cannot use PFI 0 for other digital signal routes because the analog trigger takes over the PFI 0 terminal internal to the device when it is enabled. If you try to use the analog trigger and PFI 0 for digital signals at the same time, you receive a routing error. 
 Note On PXI-6132/6133 and PXIe-6124 devices, you cannot use PFI 0 as the source of an analog trigger. On PXI-6132/6133, the analog triggering circuitry still reserves PFI 0 for internal routing.
- Analog Input Channel 
 In addition to PFI 0, analog input tasks can trigger off of one of the analog input channels being sampled. Because E Series devices use a scanning architecture, many restrictions are placed on how you can use an analog trigger when the source is one of the channels you are sampling. When you use an analog Start Trigger, the trigger channel must be the first channel in the channel list. When you use an Analog Reference or Pause Trigger, and the analog channel is the source of the trigger, there can be only one channel in the channel list. If you have more than one channel for Pause or Reference Triggers, you must use PFI 0. Since S Series devices do not use a scanning architecture, none of these restrictions apply. Therefore, for an S Series device, you can use any analog input channel as the source of the trigger regardless of how many channels are being sampled or the order of the trigger channel in the sequence.
- Scaling with PFI 0 and Analog Input Channels 
 Scaling, including custom scales, is not applied if PFI 0 is the trigger source. For instance, you would specify the DAQmx Trigger Analog Edge Level attribute/property in volts. However, if you use an analog input channel as the trigger source, you could use scaled units.

#### M Series Valid Sources for the Analog Trigger

- APFI 0 and APFI 1 
 When configuring an analog trigger, connect your analog signal to either the APFI 0 or APFI 1 terminal and specify APFI 0 or APFI 1 as your trigger source.
- Analog Input Channel 
 In addition to APFI 0 and APFI 1, analog input tasks can trigger off of one of the analog input channels being sampled. Because M Series devices use a scanning architecture, many restrictions are placed on how you can use an analog trigger when the source is one of the channels you are sampling. When you use an Analog Start Trigger, the trigger channel must be the first channel in the channel list. When you use an Analog Reference or Pause Trigger, and the analog channel is the source of the trigger, there can be only one channel in the channel list. If you have more than one channel for Pause or Reference Triggers, you must use APFI 0 or APFI 1.
- Scaling with APFI 0, APFI 1, and Analog Input Channels 
 Scaling, including custom scales, is not applied if APFI 0 or APFI 1 is the trigger source. For instance, you would specify the DAQmx Trigger Analog Edge Level attribute/property in volts. However, if you use an analog input channel as the trigger source, you could use scaled units.

#### Device Calibration and Accuracy of the Analog Trigger for E Series, M Series, C Series, or S Series Devices

The trigger DACs in the analog trigger circuitry on an E Series, M Series, C Series, or S Series device typically contain four less bits of accuracy than the ADC of the device. No hardware calibration is provided for the analog trigger circuitry. In addition, the propagation delay from when a valid trigger condition is met to when the analog trigger circuitry emits the Analog Comparison Event may have an impact on your measurements if the trigger signal has a high slew rate. If you find these conditions have a noticeable impact on your measurements, you can perform software calibration on the analog trigger circuitry by configuring your task as normal and applying a known signal for your analog trigger. Comparing the observed results against the expected results, you can calculate the necessary offsets to apply in software to fine tune the desired triggering behavior.

#### C Series and TestScale Module Valid Sources
 for the Analog Trigger

The NI 9204, NI 9205, and TS-15100 have no APFI 0 or APFI 1 terminal. Analog input tasks
 using the NI 9204, NI 9205, or
 TS-15100 can trigger off one of the analog input channels
 being sampled. When you use an Analog Start Trigger, the trigger channel must be the first
 channel from the NI 9204, NI 9205, or TS-15100 in the channel list, but channels from other C
 Series devices can come first. When you use an Analog Reference or Pause Trigger, you can use
 only one channel from the NI 9204, NI 9205, or TS-15100 in the channel list, but you can use
 channels from other C Series devices. You can combine Analog Start, Reference, and Pause
 Triggers with different configuration settings by using multiple NI 9204 or NI 9205 devices.
 All analog triggers on the same device must share the same configuration settings.

The NI 9775 can only use an analog trigger that is an active channel. See 
 *NI 9775 Considerations* for further restrictions on analog trigger usage. When you use a trigger with the NI 9775 in Analog Multi Edge, all of the trigger channels must come from the same device. When using multiple NI 9775 modules, those modules can be in the same task as long as the trigger source comes from one of the NI 9775 modules.

Related concepts:

- NI 9775 Considerations

<!--NI_TOPIC bundle=ni-daqmx path=aophyschan.html language=enus -->
## TOPIC 00019: AO Series Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `aophyschan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/aophyschan.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dev1 in physical channel names is the default device name for AO Series devices. You can change these names in MAX. Analog Output An AO Series device has between four and 64 analog output physical channels named Dev1/ao0 to Dev1/ao63. For more detailed information on the device physical AO character

### AO Series Physical Channels

Dev1 in physical channel names is the default device name for AO Series devices. You can change these names in MAX.

Parent topic:

Physical Channels

Related reference:

- AO Series, E Series, and S Series Signal Connections for Counters

#### Analog Output

An AO Series device has between four and 64 analog output physical channels named 
 Dev1/ao0 to 
 Dev1/ao63.

For more detailed information on the device physical AO characteristics, refer to your device user manual and specifications.

#### Digital Input and Output

All AO Series devices have eight lines of digital input and output named 
 Dev1/port0/line0 through 
 Dev1/port0/line7. These lines belong to a single port, and the physical channel 
 Dev1/port0 refers to all eight lines at once.

#### Counter Input and Output

All AO Series devices have two counter/timers referred to by the physical channel names 
 Dev1/ctr0 and 
 Dev1/ctr1. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device. There are three primary terminals associated with each counter. These are the terminals used as the SOURCE, GATE and OUT functions. NI-DAQmx has default values for these terminals. For counter input tasks, if you know whether your signal provides the SOURCE or GATE function and wire your signal to the default, you do not have to set the Input Terminal attribute/property.

| Counter | SOURCE Default | GATE Default | OUT Default |
| --- | --- | --- | --- |
| Dev1/ctr0 | PFI 8 | PFI 9 | CTR 0 OUT |
| Dev/ctr1 | PFI 3 | PFI 4 | CTR 1 OUT |

<!--NI_TOPIC bundle=ni-daqmx path=aoseriescal.html language=enus -->
## TOPIC 00020: AO Series Calibration

- bundle_id: `ni-daqmx`
- source_path: `aoseriescal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/aoseriescal.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your device uses software calibration to fine-tune the analog output circuitry. The software must be programmed (or loaded) with certain numbers called calibration constants. Those constants are stored in nonvolatile memory (EEPROM) on your device or are maintained by NI-DAQmx. To achieve specificat

### AO Series Calibration

Your device uses software calibration to fine-tune the analog output circuitry. The software must be programmed (or loaded) with certain numbers called calibration constants. Those constants are stored in nonvolatile memory (EEPROM) on your device or are maintained by NI-DAQmx. To achieve specification accuracy, you should self-calibrate your device just before a measurement session but after your computer and the device have been powered on and warmed up for at least 15 minutes. You should allow this same warm-up time before performing any calibration of your system. Frequent calibration produces the most stable and repeatable measurement performance. The device is not harmed in any way if you recalibrate it often.

Static AO devices, such as the NI 6703 and NI 6704, do not self-calibrate or automatically calibrate. You must use a manual procedure to calibrate static AO devices. Refer to the calibration procedure for your device.

Note

- Calibrating your AO device takes some time. Do not be alarmed if the Self-Calibrate or Adjust AO Series Calibration function/VI takes several seconds to execute.
- For best results, stop any ongoing tasks and disconnect any unnecessary external connections before running calibration.

NI-DAQmx automatically loads calibration constants into the software whenever you call functions/VIs that depend on them.

Parent topic:

Device Calibration Considerations

Related concepts:

- Device Calibration Signal Connections for AO Series Devices

Related information:

- Calibration Procedures

<!--NI_TOPIC bundle=ni-daqmx path=aotermname.html language=enus -->
## TOPIC 00021: Analog Output Accessory Terminal Names

- bundle_id: `ni-daqmx`
- source_path: `aotermname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/aotermname.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the revised names for analog output terminal names. Original Terminal Names Revised Terminal Names Explanation DAC0OUT AO0 An analog output channel DAC1OUT AO1 An analog output channel EXTREF AO EXT REF AO external reference AOGND AO GND The analog output ground UPDATE* AO

### Analog Output Accessory Terminal Names

The following table lists the revised names for analog output terminal names.

| Original Terminal Names | Revised Terminal Names | Explanation |
| --- | --- | --- |
| DAC0OUT | AO0 | An analog output channel |
| DAC1OUT | AO1 | An analog output channel |
| EXTREF | AO EXT REF | AO external reference |
| AOGND | AO GND | The analog output ground |
| UPDATE* | AO SAMP CLK | Placed as a hint next to the PFI terminal where the AO Sample Clock can be emitted |
| WFTRIG | AO START TRIG | Placed as a hint next to the PFI terminal where the AO Start Trigger can be emitted |

Parent topic:

Terminal Names

<!--NI_TOPIC bundle=ni-daqmx path=armtrig.html language=enus -->
## TOPIC 00022: Arm Start Trigger

- bundle_id: `ni-daqmx`
- source_path: `armtrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/armtrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you configure an Arm Start Trigger, a counter task does not respond to any Start Triggers until after the Arm Start Trigger occurs. You can configure this trigger to occur on a digital edge or at a specified time (for devices that support time triggering). The Arm Start Trigger is separate from

### Arm Start Trigger

When you configure an Arm Start Trigger, a counter task does not respond to any Start
 Triggers until after the Arm Start Trigger occurs. You can configure this trigger to
 occur on a digital edge or at a specified time (for devices that support time
 triggering). The Arm Start Trigger is separate from a Start Trigger and is typically
 used in advanced counter/timer applications. You might use an Arm Start Trigger to
 synchronize multiple tasks, such as counting edges and pulse generation. The Start
 Trigger then would be used to start the acquisition or generation.

Note

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-daqmx path=bridgeconfig.html language=enus -->
## TOPIC 00023: Strain Gage Bridge Configurations

- bundle_id: `ni-daqmx`
- source_path: `bridgeconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/bridgeconfig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect strain gages in a variation on a generic Wheatstone bridge configuration. These configurations vary based on the placement of strain gages within the bridge; their location and orientation on the material you want to measure; and whether the gages are active sensing gages or dummy gages, use

### Strain Gage Bridge Configurations

Connect strain gages in a variation on a generic Wheatstone bridge configuration. These configurations vary based on the placement of strain gages within the bridge; their location and orientation on the material you want to measure; and whether the gages are active sensing gages or dummy gages, used for temperature compensation.

Parent topic:

Strain Gages

Related concepts:

- Bridge Configurations
- Quarter-Bridge Type I
- Quarter-Bridge Type II
- Half-Bridge Type I
- Half-Bridge Type II
- Full-Bridge Type I
- Full-Bridge Type II
- Full-Bridge Type III

<!--NI_TOPIC bundle=ni-daqmx path=bridgeexcitation.html language=enus -->
## TOPIC 00024: Bridge Excitation

- bundle_id: `ni-daqmx`
- source_path: `bridgeexcitation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/bridgeexcitation.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Bridge-based sensors require a constant voltage to power the bridge. Bridge signal conditioners typically include a voltage source. While there is no standard voltage level that is recognized industry wide, excitation voltage levels of around 3 V and 10 V are common. Excitation sources can suffer fr

### Bridge Excitation

Bridge-based sensors require a constant voltage to power the bridge. Bridge signal conditioners typically include a voltage source. While there is no standard voltage level that is recognized industry wide, excitation voltage levels of around 3 V and 10 V are common.

Excitation sources can suffer from stability and accuracy issues. To compensate, ratiometric devices constantly measure the actual excitation voltage and use it, rather than an intended excitation value, when scaling data.

Parent topic:

Signal Conditioning Requirements for Bridge-Based Sensors

Related concepts:

- Bridge Sensor Scaling

#### Remote Sensing

If the bridge circuit is located away from the signal conditioner and excitation source, a possible source of error is voltage drops caused by resistance in the wires that connect the excitation voltage to the bridge. Therefore, some signal conditioners include a feature called remote sensing to compensate for this error. There are two common methods of remote sensing.

With feedback remote sensing, you connect extra sense wires to the point where the excitation voltage wires connect to the bridge circuit. The extra sense wires serve to regulate the excitation supply, to compensate for lead losses, and to deliver the needed voltage at the bridge.

An alternative remote sensing scheme uses a separate measurement channel to measure directly the excitation voltage delivered across the bridge. Because the measurement channel leads carry very little current, the lead resistance has negligible effect on the measurement. You then can use the measured excitation voltage in the voltage-to-strain conversion to compensate for lead losses.

<!--NI_TOPIC bundle=ni-daqmx path=bridgeforcepressuretorque.html language=enus -->
## TOPIC 00025: Bridge-Based Force, Pressure, and Torque Sensors

- bundle_id: `ni-daqmx`
- source_path: `bridgeforcepressuretorque.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/bridgeforcepressuretorque.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sensors for measuring force, pressure, and torque, such as a load cell, are often based on a Wheatstone bridge. These sensors typically use a full-bridge configuration with a 350 Ω nominal bridge resistance. Sensor manufacturers often provide a table or polynomial equation to describe how electrical

### Bridge-Based Force, Pressure, and Torque Sensors

Sensors for measuring force, pressure, and torque, such as a load cell, are often based on a Wheatstone bridge. These sensors typically use a full-bridge configuration with a 350 Ω nominal bridge resistance.

Sensor manufacturers often provide a table or polynomial equation to describe how electrical values scale to the physical phenomena the sensor measures. NI-DAQmx provides several scaling types for scaling data according to the specifications provided by the sensor manufacturer.

Parent topic:

Bridge-Based Sensors

Related concepts:

- Bridge-Based Sensors
- Bridge Configurations
- Bridge Scaling Types

<!--NI_TOPIC bundle=ni-daqmx path=bridgemeastypes.html language=enus -->
## TOPIC 00026: Bridge Measurement Types

- bundle_id: `ni-daqmx`
- source_path: `bridgemeastypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/bridgemeastypes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DAQmx provides several measurement types for taking measurements from a bridge-based sensor. Strain gage Use the strain gage measurement type for performing strain measurements. Force, pressure, and torque Use these measurement types for performing bridge-based force, pressure, or torque measurem

### Bridge Measurement Types

NI-DAQmx provides several measurement types for taking measurements from a bridge-based sensor.

Strain gage

Force, pressure, and torque

NI-DAQmx provides additional measurement types from which you read data in electrical units. Use a custom scale or write scaling code to convert the electrical units to physical units.

Bridge (V/V)

Custom voltage with excitation

Voltage

Current

Parent topic:

Bridge-Based Sensors

Related concepts:

- Bridge Measurement Type Support

<!--NI_TOPIC bundle=ni-daqmx path=calsigeseries.html language=enus -->
## TOPIC 00027: Device Calibration Signal Connections for E Series Devices

- bundle_id: `ni-daqmx`
- source_path: `calsigeseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/calsigeseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you self-calibrate your E Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels and you do not want changes on these channels, you

### Device Calibration Signal Connections for E Series Devices

When you self-calibrate your E Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels and you do not want changes on these channels, you should disconnect the circuitry before beginning the self-calibration.

When externally calibrating your E Series device, connect the signals as described below for the type of E Series device you are calibrating. Set the reference voltage between +6.000 V and +9.999 V. Typically, you use a calibrator or other stable voltage source for the reference voltage. Do not use a power supply as its signals are not very stable.

- 12-Bit E Series Devices 
 Follow these steps for 12-bit E Series devices:
  1. Connect the positive output of your reference voltage source to physical channel ai8.
  2. Connect the negative output of your reference voltage source to the AI SENSE terminal.
  3. Connect physical channel ao0 to physical channel ai0.
  4. If your reference voltage source and your computer are floating with respect to each other, connect the AI SENSE terminal to the AI GND terminal as well as to the negative output of your reference voltage source.

- 16-Bit E Series Devices
 Follow these steps for 16-bit E Series devices:
  1. Connect the positive output of your reference voltage source to physical channel ai0.
  2. Connect the negative output of your reference voltage source to physical channel ai8.
  3. If your reference voltage source and your computer are floating with respect to each other, connect the negative output of your reference voltage source to the AI GND terminal as well as to physical channel ai8.

Parent topic:

Signal Connections

<!--NI_TOPIC bundle=ni-daqmx path=calsigsseries.html language=enus -->
## TOPIC 00028: Device Calibration Signal Connections for S Series Devices

- bundle_id: `ni-daqmx`
- source_path: `calsigsseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/calsigsseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you self-calibrate your S Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels that is sensitive to these changes, you should disc

### Device Calibration Signal Connections for S Series Devices

When you self-calibrate your S Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels that is sensitive to these changes, you should disconnect the circuitry before beginning self-calibration.

When externally calibrating your S Series device, connect the signals as described below. Set the reference voltage to the following:

- NI PCI/PXI 6143: between 3.0 V and 4.998 V
- NI PCI/PXI 6115: between 4.995 V and 5.005 V
- NI PCI/PXI 6120: between 4.995 V and 5.005 V
- All other S Series Devices: between 6.0 V and 9.998 V

Typically, you should use a calibrator or other stable voltage source for calibration. Do not use a power supply as its signals are not very stable.

For external calibration, make the following signal connections:

1. Connect the positive output of your reference voltage source to ACH0+.
2. Connect the negative output of your reference voltage source to ACH0-.

Parent topic:

Signal Connections

<!--NI_TOPIC bundle=ni-daqmx path=cdaqcountsigconn.html language=enus -->
## TOPIC 00029: C Series and TestScale Module Signal Connections for Counters

- bundle_id: `ni-daqmx`
- source_path: `cdaqcountsigconn.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/cdaqcountsigconn.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following tables lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties. For information about counters on CompactRIO Single-Boa

### C Series and TestScale Module Signal Connections for Counters

The following tables lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties.

For information about counters on CompactRIO Single-Board controllers, refer to the Counter input and Output section in 
 *CompactRIO Single-Board Controller Physical Channels*.

#### NI 9401, NI 9421, NI 9422, NI 9423, NI 9436, NI 9437 (8-Channel), and TS-15050 DIO P0

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 |
| --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 0 Count Direction: PFI 2 | Edges: PFI 4 Count Direction: PFI 6 | Edges: PFI 3 Count Direction: PFI 0 | Edges: PFI 7 Count Direction: PFI 4 |
| Pulse Width Measurement | PFI 1 | PFI 5 | PFI 2 | PFI 6 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 1 | PFI 5 | PFI 2 | PFI 6 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 0 | PFI 4 | PFI 3 | PFI 7 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 0 | PFI 4 | PFI 3 | PFI 7 |
| Semiperiod Measurement | PFI 1 | PFI 5 | PFI 2 | PFI 6 |
| Two-Edge Separation Measurement | Start: PFI 2 Stop: PFI 1 | Start: PFI 6 Stop: PFI 5 | Start: PFI 0 Stop: PFI 2 | Start: PFI 4 Stop: PFI 6 |
| Position Measurement | A: PFI 0 B: PFI 2 Z: PFI 1 | A: PFI 4 B: PFI 6 Z: PFI 5 | A: PFI 3 B: PFI 0 Z: PFI 2 | A: PFI 7 B: PFI 4 Z: PFI 6 |

#### NI 9402 and NI 9435 (4-Channel)

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 |
| --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 0 Count Direction: PFI 2 | Edges: PFI 3 Count Direction: PFI 1 | Edges: PFI 1 Count Direction: PFI 0 | Edges: PFI 2 Count Direction: PFI 3 |
| Pulse Width Measurement | PFI 1 | PFI 2 | PFI 3 | PFI 0 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 1 | PFI 2 | PFI 3 | PFI 0 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 0 | PFI 3 | PFI 1 | PFI 2 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 0 | PFI 3 | PFI 1 | PFI 2 |
| Semiperiod Measurement | PFI 1 | PFI 2 | PFI 3 | PFI 0 |
| Two-Edge Separation Measurement | Start: PFI 2 Stop: PFI 1 | Start: PFI 1 Stop: PFI 2 | Start: PFI 0 Stop: PFI 3 | Start: PFI 3 Stop: PFI 0 |
| Position Measurement | A: PFI 0 B: PFI 2 Z: PFI 1 | A: PFI 3 B: PFI 1 Z: PFI 2 | A: PFI 1 B: PFI 0 Z: PFI 3 | A: PFI 2 B: PFI 3 Z: PFI 0 |

#### NI 9411 (6-Channel)

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 |
| --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 0 Count Direction: PFI 2 | Edges: PFI 3 Count Direction: PFI 5 | Edges: PFI 2 Count Direction: PFI 1 | Edges: PFI 5 Count Direction: PFI 4 |
| Pulse Width Measurement | PFI 1 | PFI 4 | PFI 0 | PFI 3 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 1 | PFI 4 | PFI 0 | PFI 3 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 0 | PFI 3 | PFI 2 | PFI 5 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 0 | PFI 3 | PFI 2 | PFI 5 |
| Semiperiod Measurement | PFI 1 | PFI 4 | PFI 0 | PFI 3 |
| Two-Edge Separation Measurement | Start: PFI 2 Stop: PFI 1 | Start: PFI 5 Stop: PFI 4 | Start: PFI 1 Stop: PFI 0 | Start: PFI 4 Stop: PFI 3 |
| Position Measurement | A: PFI 0 B: PFI 2 Z: PFI 1 | A: PFI 3 B: PFI 5 Z: PFI 4 | A: PFI 2 B: PFI 1 Z: PFI 0 | A: PFI 5 B: PFI 4 Z: PFI 3 |

The following tables list the output terminals for counter output. You can use a different PFI line for any of the output terminals.

#### NI 9401, NI 9472, NI 9474, NI 9475, NI 9485 (8-Channel), and TS-15050 DIO P0

| Ctr0 | Ctr1 | Ctr2 | Ctr3 | FreqOut |
| --- | --- | --- | --- | --- |
| PFI 3 | PFI 7 | PFI 1 | PFI 5 | PFI 2 |

#### NI 9481, NI 9482, and NI 9402 (4-Channel)

| Ctr0 | Ctr1 | Ctr2 | Ctr3 | FreqOut |
| --- | --- | --- | --- | --- |
| PFI 0 | PFI 3 | PFI 1 | PFI 2 | PFI 1 |

#### NI 9361 (8-Counters)

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 | Ctr4 | Ctr5 | Ctr6 | Ctr7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 0 Count Direction: PFI 7 Reset: PFI4 | Edges: PFI 1 Count Direction: PFI 6 Reset: PFI5 | Edges: PFI 2 Count Direction: PFI 5 Reset: PFI6 | Edges: PFI 3 Count Direction: PFI 4 Reset: PFI7 | Edges: PFI 4 Count Direction: PFI 3 Reset: PFI0 | Edges: PFI 5 Count Direction: PFI 2 Reset: PFI1 | Edges: PFI 6 Count Direction: PFI 1 Reset: PFI2 | Edges: PFI 7 Count Direction: PFI 0 Reset: PFI3 |
| Duty Cycle Measurement | PFI 0 | PFI 1 | PFI 2 | PFI 3 | PFI 4 | PFI 5 | PFI 6 | PFI 7 |
| Pulse Width Measurement | PFI 0 | PFI 1 | PFI 2 | PFI 3 | PFI 4 | PFI 5 | PFI 6 | PFI 7 |
| Period/Frequency Measurement (Dynamic Averaging) | PFI 0 | PFI 1 | PFI 2 | PFI 3 | PFI 4 | PFI 5 | PFI 6 | PFI 7 |
| Position Measurement | A: PFI 0 B: PFI 4 Z: PFI 7 | A: PFI 1 B: PFI 5 Z: PFI 6 | A: PFI 2 B: PFI 6 Z: PFI 5 | A: PFI 3 B: PFI 7 Z: PFI 4 | A: PFI 4 B: PFI 0 Z: PFI 3 | A: PFI 5 B: PFI 1 Z: PFI 2 | A: PFI 6 B: PFI 2 Z: PFI 1 | A: PFI 7 B: PFI 3 Z: PFI 0 |
| Velocity | A: PFI 0 B: PFI 4 | A: PFI 1 B: PFI 5 | A: PFI 2 B: PFI 6 | A: PFI 3 B: PFI 7 | A: PFI 4 B: PFI 0 | A: PFI 5 B: PFI 1 | A: PFI 6 B: PFI 2 | A: PFI 7 B: PFI 3 |

Parent topic:

Connecting Counter Signals

Related concepts:

- CompactRIO Single-Board Controller Physical Channels

<!--NI_TOPIC bundle=ni-daqmx path=cdaqiicountroutedia.html language=enus -->
## TOPIC 00030: Counter Internal Routing Diagrams for C Series Devices with NI cDAQ-91xx Chassis and TestScale Modules with TestScale Chassis

- bundle_id: `ni-daqmx`
- source_path: `cdaqiicountroutedia.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/cdaqiicountroutedia.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the internal routing for C Series devices used with a NI cDAQ-91xxcDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9171, 9174, 9178, 9179, 9181, 9184, 9185, 9188, 9188XT, 9189, and 9191 or TestScale modules connected to a TestScale chassisTS-15000 and TS-15010. The figure shows di

### Counter Internal Routing Diagrams for C
 Series Devices with NI cDAQ-91*xx* Chassis and TestScale Modules with TestScale
 Chassis

The following figure shows the internal routing for C Series devices used with a NI cDAQ-91xx<sup>[[1]](#note-d11842e38)</sup>[<sup>1</sup>](#fnsrc_1-d11842e38) cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9171, 9174,
 9178, 9179, 9181, 9184, 9185, 9188, 9188XT, 9189, and 9191 or TestScale modules connected to a TestScale chassis<sup>[[2]](#note-d11842e42)</sup>[<sup>2</sup>](#fnsrc_2-d11842e42) TS-15000 and TS-15010. 
 The figure shows direct routes available. Indirect routes are available as well, but use extra internal resources. The black circles represent terminals.

[IMAGE alt='image' src='GUID-5B70FC04-D5DB-4CF1-B328-6E7EEA1EDFF4-a5.svg']

Parent topic:

Counter Internal Routing Diagrams

[<sup>1</sup>](#note_ref-d11842e38) cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9171, 9174,
 9178, 9179, 9181, 9184, 9185, 9188, 9188XT, 9189, and 9191

[<sup>2</sup>](#note_ref-d11842e42) TS-15000 and TS-15010

<!--NI_TOPIC bundle=ni-daqmx path=cdaqmultidevice.html language=enus -->
## TOPIC 00031: C Series Multidevice Tasks

- bundle_id: `ni-daqmx`
- source_path: `cdaqmultidevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/cdaqmultidevice.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you include channels from multiple C Series modules in a task, NI-DAQmx automatically synchronizes the modules. A task can include channels from multiple C Series modules, given the following conditions: All channels in the task must be of the same I/O type. Multiple counter I/O channels are on

### C Series Multidevice Tasks

When you include channels from multiple C Series modules in a task, NI-DAQmx automatically synchronizes the modules. A task can include channels from multiple C Series modules, given the following conditions:

- All channels in the task must be of the same I/O type. Multiple counter I/O channels are only allowed for 
 Devices That Support Multi-Counter Tasks .
- If the task includes channels from a mixture of C Series Delta-Sigma devices, you must account for filter delay differences between the devices. This delay is also known as the input delay. Refer to your device specifications for the value.
- The modules must all be in the same NI CompactDAQ chassis or meet the conditions for multichassis device tasks.

Note

- AI tasks containing only 16-bit or lower resolution AI modules use half the USB bandwidth of tasks with 24-bit AI modules.
- The format of raw data returned by a C Series AI task varies depending on if any 24-bit AI modules are in the task and might not correspond to the order of the channels in the task. Scaled or unscaled data is preferable to raw data with the NI CompactDAQ chassis.
- The acquisition mode of the NI 9775 will vary depending on the other modules in the task. If the task uses only NI 9775 modules, all the modules can operate in Record Mode. If the task uses an NI 9775 module and other types of modules, the NI 9775 operates in Continuous Mode.

Parent topic:

Multidevice Tasks

Related concepts:

- C Series Device Groupings
- Filter Delay (DSA, C Series, and NI 433x)
- Devices That Support Multi-Counter Tasks

#### C Series Multichassis Device Tasks

A task can include channels from multiple C Series modules in separate CompactDAQ chassis<sup>[[1]](#note-d26831e174)</sup>[<sup>1</sup>](#fnsrc_1-d26831e174) cDAQ-9171, 9174, 9178, 9179, 9181, 9184, 9185,
 9188, 9188XT, 9189, and 9191., CompactDAQ controllers<sup>[[2]](#note-d26831e179)</sup>[<sup>2</sup>](#fnsrc_2-d26831e179) cDAQ-9132, 9133, 9134, 9135, 9136, and 9137., CompactRIO controllers<sup>[[3]](#note-d26831e184)</sup>[<sup>3</sup>](#fnsrc_3-d26831e184) cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048,
 9049, 9053, 9054, 9055, 9056, 9057, and 9058. and CompactRIO Single-Board controllers<sup>[[4]](#note-d26831e189)</sup>[<sup>4</sup>](#fnsrc_4-d26831e189) sbRIO-9603, 9608, 9609, 9628, 9629, and 9638., given the following conditions:

- Network-synchronized devices 
 [[5]](#note-d26831e199) [<sup>5</sup>](#fnsrc_5-d26831e199) Network-synchronized devices include the
 cDAQ-9185, 9189; FD-11601, FD-11603, FD-11605, FD-11613, FD-11614,
 FD-11634, FD-11637; cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047,
 9048, 9049, 9053, 9054, 9055, 9056, 9057, 9058; and sbRIO-9603,
 9608, 9609, 9628, 9629, and 9638. must be part of the same time-synchronized network. Refer to the device specifications for supported synchronization protocols and topologies.
- Chassis that are not network-synchronized must be connected through a NI 9469.
- If a task has a network-synchronized chassis and connections through the NI 9469 to chassis that are not synchronized, the first channel in the task must be in the network-synchronized chassis along with the NI 9469 connection to other chassis that are not synchronized.
- When using signal-based synchronization using the NI 9469, the first channel in the channel list must be on a module in the master chassis. The master chassis is determined by the physical configuration of the chassis connections, and it should be able to output signals to the slave chassis.
- If an Analog Input task contains Delta-Sigma modules, a channel on a Delta-Sigma module in the master chassis needs to be first on the channel list.
- If an Analog Input task contains a device with a reference clock, a channel from a reference-clocked device needs to be first on the channel list.
- No more than one CompactRIO controller may participate in a multichassis device task.

##### Exceptions

- The NI 9361 does not support multichassis device tasks.
- The NI 9260 must drive the idle output to zero. If you don't, you will receive an error.
- The NI 9775 does not support multichassis device tasks.

Related concepts:

- Time-Based Features for Network-Synchronized Devices

[<sup>1</sup>](#note_ref-d26831e174) cDAQ-9171, 9174, 9178, 9179, 9181, 9184, 9185,
 9188, 9188XT, 9189, and 9191.

[<sup>2</sup>](#note_ref-d26831e179) cDAQ-9132, 9133, 9134, 9135, 9136, and 9137.

[<sup>3</sup>](#note_ref-d26831e184) cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048,
 9049, 9053, 9054, 9055, 9056, 9057, and 9058.

[<sup>4</sup>](#note_ref-d26831e189) sbRIO-9603, 9608, 9609, 9628, 9629, and 9638.

[<sup>5</sup>](#note_ref-d26831e199) Network-synchronized devices include the
 cDAQ-9185, 9189; FD-11601, FD-11603, FD-11605, FD-11613, FD-11614,
 FD-11634, FD-11637; cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047,
 9048, 9049, 9053, 9054, 9055, 9056, 9057, 9058; and sbRIO-9603,
 9608, 9609, 9628, 9629, and 9638.

<!--NI_TOPIC bundle=ni-daqmx path=cdaqphychannels.html language=enus -->
## TOPIC 00032: C Series and TestScale Module Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `cdaqphychannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/cdaqphychannels.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In physical channel names: cDAQ1Mod1 is the default device name for a C Series device plugged into a USB or Standalone CompactDAQ chassis, where cDAQ1 is the default chassis device name, and Mod1 refers to the slot number TS1Mod1 is the default device name for a TestScale module plugged into a Stand

### C Series and TestScale Module Physical
 Channels

In physical channel names:

- cDAQ1Mod1 is the default device name for a C Series device plugged into a
 USB or Standalone CompactDAQ chassis, where cDAQ1 is the default chassis device name, and
 Mod1 refers to the slot number
- TS1Mod1 is the default device name for a TestScale module plugged into a
 Standalone TestScale chassis, where TS1 is the default chassis device name, and Mod1 refers
 to the slot number

For C Series devices plugged into a network CompactDAQ chassis, such as the NI cDAQ-9188,
 the default chassis device name is the host name of the chassis. You can change these names in
 MAX. For C Series devices plugged into a supported CompactRIO<sup>[[1]](#note-d17938e52)</sup>[<sup>1</sup>](#fnsrc_1-d17938e52) cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048,
 9049, 9053, 9054, 9055, 9056, 9057, and 9058. or CompactRIO Single-Board<sup>[[2]](#note-d17938e57)</sup>[<sup>2</sup>](#fnsrc_2-d17938e57) sbRIO-9603, 9608, 9609, 9628, 9629, and 9638. controller, Mod1 is the default device name.

Parent topic:

Physical Channels

Related concepts:

- Digital I/O Considerations for C Series and TestScale Devices
- CompactRIO Single-Board Controller Physical Channels
- Digital I/O Considerations for C Series Devices

Related reference:

- C Series and TestScale Module Signal Connections for Counters
- C Series Signal Connections for Counters

#### Analog Input

The following table lists the number and naming of analog input physical channels for C
 Series devices and TestScale modules.

| Device | Number of Channels | Naming |
| --- | --- | --- |
| NI 9218, NI 9250, NI 9251 | 2 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai1 |
| NI 9225, NI 9230, NI 9232, NI 9246, NI 9247 | 3 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai2 |
| NI 9210, NI 9211, NI 9215, NI 9217, NI 9219, NI 9222, NI 9223, NI 9227, NI 9229, NI 9234, NI 9237, NI 9238, NI 9239, NI 9775 | 4 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai3 |
| NI 9242, NI 9244 | 4 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai2, cDAQ1Mod1/neutral |
| NI 9201, NI 9203, NI 9212, NI 9216, NI 9221, NI 9226, NI 9224, NI 9228, NI 9231, NI 9235, NI 9236, NI 9252, NI 9253 | 8 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai7 |
| NI 9202, NI 9204, NI 9207, NI 9208, NI 9209, NI 9213, NI 9214, NI 9220, NI 9320 | 16 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai15 |
| NI 9205, NI 9206 | 32 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai31 |
| TS-15100 | 32 | TS1Mod1/ai0 to TS1Mod1/ai31 |

On the NI 9204, you can configure channels 0-7 as the positive channel of a differential
 pair. On the NI 9205 and NI
 9206, you can configure channels 0-7 and 16-23 as the positive channel of a differential
 pair. If N is this channel, channel N + 8 is the
 negative input of the pair. For instance,
 you
 can
 configure channel 1 in differential
 mode.
 In this configuration, channel 1 serves as the positive input. Channel 9 serves as
 the negative input. Use only the physical channel name of the positive
 channel (not both) when creating a differential channel.

You can use channels from multiple analog input C Series devices in the same NI-DAQmx
 task.

- Up to three analog input tasks can run at a given
 time per chassis in a
 cDAQ-91 xx 
 or TestScale [[3]](#note-d17938e358) [<sup>3</sup>](#fnsrc_3-d17938e358) TS-15000 and TS-15010 chassis.
- Up to eight analog input tasks can run a given
 time in a CompactRIO controller or a CompactRIO Single-Board controller.
- A
 C Series Delta-Sigma device
 supports
 up to two analog input tasks at a given
 time. This limit
 applies per chassis in a
 cDAQ-91 xx 
 or TestScale [[4]](#note-d17938e386) [<sup>4</sup>](#fnsrc_4-d17938e386) TS-15000 and TS-15010 chassis.
- Up to eight analog input tasks with a C Series
 Delta-Sigma device can run at a given time in a CompactRIO controller or a CompactRIO
 Single-Board controller.

Related concepts:

- C Series Device Groupings

##### Strain and Wheatstone Bridge Measurements

The NI 9235, NI 9236, and NI 9237 support only the AI Strain Gage, AI Force Bridge, AI Pressure Bridge, AI Torque Bridge, AI Bridge (V/V), and AI Custom Voltage With Excitation channel types.

When using the NI 9218, NI 9219, NI 9235, NI 9236, or NI 9237 with an AI Custom Voltage With Excitation channel, you must set the AI.Excit.UseForScaling attribute/property to true. This attribute/property causes the channel to return ratiometric data: Vin/Vex. The NI 9219, NI 9235, NI 9236, and NI 9237 modules perform this division in hardware.

For the NI 9219, NI-DAQmx requires the AI.Excit.Val attribute/property to be set to 2.5 V for AI Strain Gage and AI Custom Voltage With Excitation channel types and to 500 µA for resistance and RTD measurements. The actual excitation voltage or current output by the NI 9219 varies with the sensor resistance or the load being measured.

For the NI 9218, NI-DAQmx requires the AI.Excit.Val attribute/property to be set to 3.3 V or 2 V for AI Strain Gage and AI Custom Voltage With Excitation (bridge mode), to 12 V for AI Custom Voltage With Excitation (no bridge mode) for powered sensors, and to 2 mA for IEPE.

NI 9218, NI 9219, NI 9235, NI 9236, and NI 9237 devices return a voltage ratio rather than a voltage. Therefore, use the AI.Bridge.InitialRatio attribute/property to specify the initial voltage ratio, or set the AI.Bridge.InitialVoltage attribute/property to the ratio Vin/Vex returned by the device, multiplied by Vex.

The NI 9219 does not have quarter bridge completion circuitry, which affects AI Strain Gage Quarter Bridge I channels and AI Custom Voltage With Excitation Quarter Bridge channels (but not AI Strain Gage Quarter Bridge II channels). With these channels, the NI 9219 performs a 2-wire resistance measurement on the active gage element, then NI-DAQmx uses software scaling to convert the resistance measurement into a bridge ratio. For these channels, the polynomial coefficients specified by the AI.DevScalingCoeff attribute/property convert unscaled data into Ohms, not into V/V. Likewise, the AI.Rng.High/AI.Rng.Low attributes/properties should be specified in units of Ohms, not V/V.

When the NI 9219 is in quarter bridge mode, you need to use the AI.Bridge.NomResistance attribute/property to control whether the channel uses the 120 Ω range or the 350 Ω range.

The NI 9218 has an internal full bridge. However, it can support quarter-bridge and half-bridge measurements with the proper accessories.

##### NI 9218 Powered Sensor Measurements

The NI 9218 supports powered sensor measurements. For voltage powered sensor measurements, you can use either the DAQmx Create Channel function/VI (the AI Custom Voltage with Excitation measurement type) with the Bridge Configuration set to No Bridge, or you can use the DAQmx Create Channel function/VI (voltage measurement type) with the AI.Excit.Val attribute/property. For current powered sensor measurements, you have to use the DAQmx Create Channel function/VI (current measurement type) with the AI.Excit.Val attribute/property.

#### Analog Output

The following table lists the number and naming of analog output physical channels for C
 Series devices.

| Device | Number of Channels | Naming |
| --- | --- | --- |
| NI 9260 | 2 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao1 |
| NI 9263, NI 9265 | 4 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao3 |
| TS-15110 | 4 | TS1Mod1/ao0 to TS1Mod1/ao3 |
| NI 9262 | 6 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao5 |
| NI 9266 | 8 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao7 |
| NI 9264 | 16 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao15 |

You can use channels from multiple analog output C Series devices in the same analog output
 task. With certain cDAQ-91xx<sup>[[5]](#note-d17938e658)</sup>[<sup>5</sup>](#fnsrc_5-d17938e658) cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189 or TestScale<sup>[[6]](#note-d17938e662)</sup>[<sup>6</sup>](#fnsrc_6-d17938e662) TS-15000 and TS-15010 chassis, if
 the task is hardware-timed and uses only onboard memory, there is a limit of 16 channels per
 task, but if the task is software-timed or does not use only onboard memory, the number of
 channels is limited only by the number of devices. Only one hardware-timed analog output task
 per CompactDAQ chassis can run at a given time. With a CompactRIO controller or CompactRIO
 single-board controller, up to eight hardware-timed analog output tasks can run at a given
 time.

When using the NI 9262, NI 9263, NI 9264, NI 9265, NI 9266, or TS-15110 you can run only one type of timing at a time. You can have one software-timed task per channel or one hardware-timed task running on a device at one time, but you cannot have a combination of timing on that device. For instance, you can run up to four software-timed tasks on the NI 9265 concurrently, but running one hardware-timed task with one software-timed task generates an error.

When using the NI 9260, if you start a task that uses a different channel than the one you
 are currently using, the channel no longer in use reverts to the calibrated 0 V value.

#### Digital Input and Output

The following table lists the number, type, and naming of digital input/output lines for C Series devices.

| Device | Lines | Type | Naming |
| --- | --- | --- | --- |
| NI 9344 | 4 | digital input | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line3 |
| 4 | digital output | cDAQ1Mod1/port1/line0 to cDAQ1Mod1/port1/line3 |  |
| NI 9402, NI 9435, NI 9481, 9482 | 4 | digital input and/or output | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line3 |
| NI 9411 | 6 | digital input | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line5 |
| NI 9401, NI 9421, NI 9422, NI 9423, NI 9472, NI 9474, NI 9475, NI 9485 | 8 | digital input and/or output | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line7 |
| TS-15050 DIO P0 | 8 | digital input and/or output | TS1Mod1/port0/line0 to TS1Mod1/port0/line7 |
| NI 9436, NI 9437 | 8 | digital input | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line7 |
| NI 9375 | 16 | digital input | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line15 |
| 16 | digital output | cDAQ1Mod1/port1/line0 to cDAQ1Mod1/port1/line15 |  |
| NI 9478 | 16 | digital output | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line15 |
| NI 9403, NI 9425, NI 9426, NI 9476, NI 9477 | 32 | digital input and/or output | cDAQ1Mod1/port0/line0 to cDAQ1Mod1/port0/line31 |
| TS-15120, TS-15130 | 32 | digital input and/or output | TS1Mod1/port0/line0 to TS1Mod1/port0/line31 |

Note

Digital I/O Considerations for C Series

#### Chassis Counter Input and Output

The CompactDAQ chassis, CompactDAQ controllers, CompactRIO controllers, and CompactRIO single-board controllers have four counters. You can use counters/timers with a C Series device in any slot. CompactRIO single-board controllers feature onboard I/O connectors in addition to C Series device access through the RMC connector. See 
 *CompactRIO Single-Board Controller Physical Channels* for more information and counter terminal default configuration of CompactRIO single-board controller onboard I/O connectors.

These chassis also have a 4-bit frequency output generator, referred to as cDAQ1Modx/freqout, where 
 x is the slot in which the module is located.

Each counter has four primary terminals associated with it. These are the terminals used as the SOURCE, GATE, AUX, and OUT functions. NI-DAQmx has default values for these terminals. For counter input tasks, if you know whether your signal provides the SOURCE, AUX, or GATE function and wire your signal to the default, you do not have to set the Input Terminal attribute/property.

Counter/timers are only supported on parallel digital I/O modules. Refer to 
 *Digital I/O Considerations for C Series* for more information.

The following table shows the counter terminal defaults for 8-channel DIO/DI/DO C Series devices.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | ctr0 src/ctr2 aux |
| PFI 1 | ctr0 gate/ctr2 out |
| PFI 2 | ctr0 aux/ctr2 gate/freqout |
| PFI 3 | ctr0 out/ctr2 src |
| PFI 4 | ctr1 src/ctr3 aux |
| PFI 5 | ctr1 gate/ctr3 out |
| PFI 6 | ctr1 aux/ctr3 gate |
| PFI 7 | ctr1 out/ctr3 src |

The following table shows the counter terminal defaults for 6-channel DIO/DI/DO C Series devices.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | ctr0 src/ctr2 gate |
| PFI 1 | ctr0 gate/ctr2 aux/ctr2 out/freqout |
| PFI 2 | ctr0 aux/ctr0 out/ctr2 src |
| PFI 3 | ctr1 src/ctr3 gate |
| PFI 4 | ctr1 gate/ctr3 aux/ctr3 out |
| PFI 5 | ctr1 aux/ctr1 out/ctr3 src |

The following table shows the counter terminal defaults for 4-channel DIO/DI/DO C Series devices.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | ctr0 src/ctr0 out/ctr2 aux/ctr3 gate |
| PFI 1 | ctr0 gate/ctr1 aux/ctr2 src/ctr2 out/freqout |
| PFI 2 | ctr0 aux/ctr1 gate/ctr3 src/ctr3 out |
| PFI 3 | ctr1 src/ctr1 out/ctr2 gate/ctr3 aux |

#### Module Counter Input and Output

The following table lists the number, type, and naming of counter input lines for C Series counter modules.

| Device | Counter | Type | Names |
| --- | --- | --- | --- |
| NI 9361 | 8 | Counter input | cDAQ1Mod1/ctr0 to cDAQ1Mod1/ctr7 |

There are 8 PFI lines, from PFI0 to PFI7. Each counter can use any of the input PFI lines to perform measurements. Two counters can use the same PFI line as inputs for their measurements, as long as the input configurations are the same for both counters.

The following table shows the terminal defaults for edge counting measurements for C Series counter modules.

| Counter | Input terminal | Reset | Direction |
| --- | --- | --- | --- |
| ctr0 | PFI0 | PFI4 | PFI7 |
| ctr1 | PFI1 | PFI5 | PFI6 |
| ctr2 | PFI2 | PFI6 | PFI5 |
| ctr3 | PFI3 | PFI7 | PFI4 |
| ctr4 | PFI4 | PFI0 | PFI3 |
| ctr5 | PFI5 | PFI1 | PFI2 |
| ctr6 | PFI6 | PFI2 | PFI1 |
| ctr7 | PFI7 | PFI3 | PFI0 |

The following table shows the terminal defaults for position measurements for C Series counter modules.

| Counter | A | B | Z |
| --- | --- | --- | --- |
| ctr0 | PFI0 | PFI4 | PFI7 |
| ctr1 | PFI1 | PFI5 | PFI6 |
| ctr2 | PFI2 | PFI6 | PFI5 |
| ctr3 | PFI3 | PFI7 | PFI4 |
| ctr4 | PFI4 | PFI0 | PFI3 |
| ctr5 | PFI5 | PFI1 | PFI2 |
| ctr6 | PFI6 | PFI2 | PFI1 |
| ctr7 | PFI7 | PFI3 | PFI0 |

The following table shows the terminal defaults for velocity measurements for C Series counter modules that support velocity measurements.

| Counter | A | B |
| --- | --- | --- |
| ctr0 | PFI0 | PFI4 |
| ctr1 | PFI1 | PFI5 |
| ctr2 | PFI2 | PFI6 |
| ctr3 | PFI3 | PFI7 |
| ctr4 | PFI4 | PFI0 |
| ctr5 | PFI5 | PFI1 |
| ctr6 | PFI6 | PFI2 |
| ctr7 | PFI7 | PFI3 |

The following table shows the terminal defaults for frequency, period, duty cycle, and pulse width measurements for C Series counter modules.

| Counter | Input Terminal |
| --- | --- |
| ctr0 | PFI0 |
| ctr1 | PFI1 |
| ctr2 | PFI2 |
| ctr3 | PFI3 |
| ctr4 | PFI4 |
| ctr5 | PFI5 |
| ctr6 | PFI6 |
| ctr7 | PFI7 |

Connections for PFI lines should be based on the terminal configuration property. PFI + and PFI- should be connected in differential mode, and PFI + and COM should be connected for RSE. The default terminal configuration for all counter input terminals is RSE.

[<sup>1</sup>](#note_ref-d17938e52) cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048,
 9049, 9053, 9054, 9055, 9056, 9057, and 9058.

[<sup>2</sup>](#note_ref-d17938e57) sbRIO-9603, 9608, 9609, 9628, 9629, and 9638.

[<sup>3</sup>](#note_ref-d17938e358) TS-15000 and TS-15010

[<sup>4</sup>](#note_ref-d17938e386) TS-15000 and TS-15010

[<sup>5</sup>](#note_ref-d17938e658) cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189

[<sup>6</sup>](#note_ref-d17938e662) TS-15000 and TS-15010

<!--NI_TOPIC bundle=ni-daqmx path=common-applications.html language=enus -->
## TOPIC 00033: Common Applications

- bundle_id: `ni-daqmx`
- source_path: `common-applications.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/common-applications.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`

### Common Applications

- [Measuring Acceleration](measuring-acceleration.html)
- [Measuring Analog Frequency](measuring-analog-frequency.html)
- [Measuring Angular Displacement](measuring-angular-displacement.html)
- [Control](control.html)
- [Edge Counting](edge-counting.html)
- [Measuring Calculated Power](measuring-calculated-power.html) Many measurement devices can measure voltage and current, but not all measurement devices can measure calculated power.
- [Measuring Charge](measuring-charge.html)
- [Measuring and Generating Current](measuring-and-generating-current.html) Many measurement devices can measure and generate current. To measure or generate current with a DAQ device, you need a resistor.
- [Measuring and Generating Digital Values](measuring-and-generating-digital-values.html)
- [Measuring Duty Cycle](measuring-duty-cycle.html)
- [Measuring Force](measuring-force.html)
- [Measuring Digital Frequency](measuring-digital-frequency.html)
- [Generic Programming Flowcharts](generic-programming-flowcharts.html)
- [Measuring GPS Timestamp](measuring-gps-timestamp.html)
- [Measuring Linear Displacement](measuring-linear-displacement.html)
- [Measuring Period, Semi-Period, Pulse Width, and Two-Edge Separation](measuring-period-semi-period-pulse-width-and-.html)
- [Measuring Pressure](measuring-pressure.html)
- [Measuring Proximity](measuring-proximity.html)
- [Generating Pulses](generating-pulses.html)
- [Measuring Resistance](measuring-resistance.html)
- [Measuring Sound Pressure](measuring-sound-pressure.html)
- [Measuring Strain](measuring-strain.html)
- [Measuring Torque](measuring-torque.html)
- [Measuring Temperature](measuring-temperature.html)
- [Measuring Velocity](measuring-velocity.html)
- [Generating Voltage](generating-voltage.html)
- [Measuring Voltage](measuring-voltage.html) Measurement devices commonly measure voltage, including direct current (DC) and alternating current (AC). DC voltage is ideal for slowly changing phenomena, while AC voltage is used in power systems.

<!--NI_TOPIC bundle=ni-daqmx path=commonmodeoverrangedetection.html language=enus -->
## TOPIC 00034: Common-Mode Over-Range Detection

- bundle_id: `ni-daqmx`
- source_path: `commonmodeoverrangedetection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/commonmodeoverrangedetection.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: All input channels share a common ground, COM, that is isolated from other modules in the system. The device's common-mode range is the maximum voltage between any channel and COM. The NI 9213, NI 9214, and PXIe 4353 measures the common-mode voltage level of each channel, and its over-range status c

### Common-Mode Over-Range Detection

All input channels share a common ground, COM, that is isolated from other modules in the system. The device's common-mode range is the maximum voltage between any channel and COM. The NI 9213, NI 9214, and PXIe 4353 measures the common-mode voltage level of each channel, and its over-range status can be monitored in NI-DAQmx.

To determine if a common-mode over-range detection has occurred, use the Common Mode Range Error Channels Existand Common Mode Range Error Channels properties within the DAQmx Read property node. Common Mode Range Error Channels Exist returns a Boolean of true if one or more channels exceed the common-mode input range since the last time the property was queried, and Common Mode Range Error Channels returns the names of the virtual channels that exceed the common-mode input range.

If a common-mode voltage out of range is detected, the accuracy of the data on any channel in the task may be impacted. If a thermocouple is connected to the device, but is not in the task, make sure the channel does not exceed the common-mode voltage range. A floating thermocouple, or a channel that is left unconnected, will not exceed the common-mode voltage range. Refer to the devices Specifications document for more information about the common-mode voltage range.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=configadctiming.html language=enus -->
## TOPIC 00035: Configurable ADC Timing

- bundle_id: `ni-daqmx`
- source_path: `configadctiming.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/configadctiming.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: On some devices, you can configure high-speed, high-resolution, or low-noise measurements using the AI.ADCTimingMode attribute/property. The following devices support configurable ADC Timing. FD-11613 and FD-11614 NI 9207, NI 9208, NI 9212, NI 9213, NI 9217, and NI 9219 NI 4353 and NI 4357

### Configurable ADC Timing

On some devices, you can configure high-speed, high-resolution, or low-noise measurements using the AI.ADCTimingMode attribute/property. The following devices support configurable ADC Timing.

- FD-11613 and FD-11614
- NI 9207, NI 9208, NI 9212, NI 9213, NI 9217, and NI 9219
- NI 4353 and NI 4357

Parent topic:

NI-DAQmx Device Considerations

Related concepts:

- Configurable Timing for SC Express Devices
- Timing Considerations for C Series Devices

<!--NI_TOPIC bundle=ni-daqmx path=confighndshklines.html language=enus -->
## TOPIC 00036: Handshaking Line Configuration

- bundle_id: `ni-daqmx`
- source_path: `confighndshklines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/confighndshklines.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI 6533/6534 devices have two timing engines, each of which use a set of default lines for handshaking and burst handshaking. You can specify a different timing engine to use the handshaking lines associates with that timing engine.

### Handshaking Line Configuration

NI 6533/6534 devices have two timing engines, each of which use a set of default lines for handshaking and burst handshaking. You can specify a different timing engine to use the handshaking lines associates with that timing engine.

Parent topic:

Digital I/O

Related concepts:

- NI 6533, 6534 Timing Engines
- Handshake Timing Defaults
- Burst Handshaking Timing Defaults for NI 653x Devices

<!--NI_TOPIC bundle=ni-daqmx path=configtimemeas.html language=enus -->
## TOPIC 00037: Configuring a Time-Based Measurement in NI-DAQmx

- bundle_id: `ni-daqmx`
- source_path: `configtimemeas.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/configtimemeas.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure a measurement, you specify the expected range of the input signal. Based on this range, NI-DAQmx automatically picks the internal timebase that provides the highest resolution for your measurement and uses it as the counter timebase. You also can explicitly specify the source of the cou

### Configuring a Time-Based Measurement in NI-DAQmx

To configure a measurement, you specify the expected range of the input signal. Based on this range, NI-DAQmx automatically picks the internal timebase that provides the highest resolution for your measurement and uses it as the counter timebase. You also can explicitly specify the source of the counter timebase by setting the Counter Timebase Source attribute/property and the rate of the timebase by setting the Counter Timebase Rate attribute/property. For more information on where to connect input signals, refer to Connecting Counter Signals.

For non-buffered time-based measurements, calling the Read function/VI initiates the measurement and returns the next valid sample. Calling the Read function/VI repeatedly does not return consecutive measurements of the input signal.

To perform buffered time-based measurements, you must use Implicit or Sample Clock timing, configured using the DAQmx Timing function/VI.

Parent topic:

Counters

Related concepts:

- Connecting Counter Signals

#### Implicit Timing

After the acquisition begins, NI-DAQmx measures each consecutive sample of the input signal and stores the measurement in the input buffer. Due to this consecutive measurement, the rate of the input signal implicitly determines the rate of the acquisition.

#### Sample Clock Timing

Some devices support Sample Clock timing for buffered time-based measurements. After the acquisition begins, your device measures each consecutive sample of the input signal, but does not store it to the input buffer until an active edge of the Sample Clock occurs. Using this timing type, the Sample Clock rate determines the acquisition rate rather than the input signal. When using Sample Clock timing, all measurements returned are a valid, complete cycle of your input signal. Using this method, you can measure signals that are much faster than your sample rate, which minimizes the amount of data transferred from your device to NI-DAQmx.

Related concepts:

- Sample Clock Timing Support for Time-Based Measurements

##### Averaging

For frequency and period measurements using Sample Clock timing, some devices can return an averaged measurement of all periods since the previous Sample Clock pulse, instead of measuring only the period immediately preceding the current Sample Clock pulse. Use the EnableAveraging DAQmx Channel property/attribute, associated with each of those measurement types, to enable averaging.

Related concepts:

- Averaging Support

#### Invalid Initial Samples

Depending on the phase of the input signal in relation to the start of the measurement, the first sample of a buffered measurement is often invalid. For instance, if you are performing a buffered period measurement, and you start the measurement when the input signal is halfway through its current cycle, the measured period for the first sample is half its expected value. Subsequent samples indicate the correct values because they are guaranteed to be taken after a full period of the input signal. For this reason, the first sample of buffered period, pulse width, and semi-period measurements often indicates a smaller value than the actual value. For buffered frequency measurements, the first sample often indicates a higher frequency than the actual frequency. Some devices detect these incomplete samples and discard them.

Related concepts:

- Incomplete Sample Detection

#### Pulse Measurement

Some devices support measuring individual pulses, returning each sample as a tuple of frequency/duty cycle, high/low time, or high/low ticks.

Related concepts:

- Pulse Measurement Support

<!--NI_TOPIC bundle=ni-daqmx path=configtimescexp.html language=enus -->
## TOPIC 00038: Configurable Timing for SC Express Devices

- bundle_id: `ni-daqmx`
- source_path: `configtimescexp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/configtimescexp.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: On the NI 4353 and NI 4357, you can configure high-speed or high-resolution measurements using the AI.ADCTimingMode attribute/property. You can also configure a custom value. To configure a custom value, do the following: Set the AI.ADCTimingMode attribute/property to Custom. Specify a custom value

### Configurable Timing for SC Express Devices

On the NI 4353 and NI 4357, you can configure high-speed or high-resolution measurements using the AI.ADCTimingMode attribute/property. You can also configure a custom value. To configure a custom value, do the following:

1. Set the AI.ADCTimingMode attribute/property to Custom.
2. Specify a custom value with the AI.ADCCustomTimingMode attribute/property. A smaller value is the lowest noise option while a larger value is the highest speed option. Refer to your device documentation for additional information on custom values.

Parent topic:

Configurable ADC Timing

<!--NI_TOPIC bundle=ni-daqmx path=connectai.html language=enus -->
## TOPIC 00039: Connecting Analog Input Signals

- bundle_id: `ni-daqmx`
- source_path: `connectai.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/connectai.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal connections vary depending on your device, connector block, and signal conditioning module. The DAQ Assistant contains connection diagrams that show terminal connections for all common analog input measurements, such as measuring strain, temperature, current, voltage, and so on. Refer to View

### Connecting Analog Input Signals

Signal connections vary depending on your device, connector block, and signal conditioning module. The DAQ Assistant contains connection diagrams that show terminal connections for all common analog input measurements, such as measuring strain, temperature, current, voltage, and so on. Refer to 
 *Viewing Connection Diagrams* in the 
 *DAQ Assistant Help* for additional information.

For terminals specific to your device, refer to your device documentation.

Parent topic:

Analog Connection Considerations

<!--NI_TOPIC bundle=ni-daqmx path=connectaisigs.html language=enus -->
## TOPIC 00040: Measurement System Types and Signal Sources

- bundle_id: `ni-daqmx`
- source_path: `connectaisigs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/connectaisigs.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The type of input signal source (grounded or floating) and the configuration of the measurement system (differential, single-ended, pseudodifferential) determine how you connect signals to measurement devices. The following table provides an application-independent summary of analog input connection

### Measurement System Types and Signal Sources

The type of input signal source (grounded or floating) and the configuration of the measurement system (differential, single-ended, pseudodifferential) determine how you connect signals to measurement devices.

The following table provides an application-independent summary of analog input connections.

| Input | Signal Source Type |  |
| --- | --- | --- |
| Floating Signal Source (Not Connected to Building Ground) | Grounded Signal Source |  |
| Examples: Ungrounded thermocouples, signal conditioning with isolated outputs, battery devices | Example: Instruments with nonisolated outputs |  |
| Differential (DIFF) |  |  |
| Ground Referenced Single-Ended (RSE) Note: AI GND is shared as a reference for all RSE channels |  |  |
| Nonreferenced Single-Ended (NRSE) Note: AI SENSE is shared as a reference for all NRSE channels |  |  |
| Pseudodifferential |  |  |
| R ext is the external bias resistor that you add. |  |  |

Parent topic:

Connecting Analog Input Signals

Related concepts:

- Grounded Signal Sources
- Floating Signal Sources
- Differential Measurement System
- Referenced and Nonreferenced Single-Ended Measurement Systems
- Pseudodifferential Measurement System

<!--NI_TOPIC bundle=ni-daqmx path=connectaosigs.html language=enus -->
## TOPIC 00041: Connecting Analog Output Signals

- bundle_id: `ni-daqmx`
- source_path: `connectaosigs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/connectaosigs.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal connections vary depending on your device, connector block, and signal conditioning module. The following figure shows how to make analog output connections for a typical NI device. For terminals specific to your device, refer to your device documentation.

### Connecting Analog Output Signals

Signal connections vary depending on your device, connector block, and signal conditioning module. The following figure shows how to make analog output connections for a typical NI device.

[IMAGE alt='image' src='GUID-AD1395F5-39C4-4D4F-9E2E-7DA964F21026-a5.svg']

For terminals specific to your device, refer to your device documentation.

Parent topic:

Analog Connection Considerations

<!--NI_TOPIC bundle=ni-daqmx path=connectdiosigs.html language=enus -->
## TOPIC 00042: Connecting Digital I/O Signals

- bundle_id: `ni-daqmx`
- source_path: `connectdiosigs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/connectdiosigs.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The number of digital lines varies from device to device. The following figure shows signal connections for three typical DIO applications. The figure shows PO <0..3> configured for digital input and PO <4..7> configured for digital output. Digital input applications include receiving TTL signals an

### Connecting Digital I/O Signals

The number of digital lines varies from device to device. The following figure shows signal connections for three typical DIO applications.

[IMAGE alt='image' src='GUID-5566C866-13C1-476B-B033-69C89F53FAF5-a5.svg']

The figure shows PO <0..3> configured for digital input and PO <4..7> configured for digital output. Digital input applications include receiving TTL signals and sensing external device states such as the state of a switch. Digital output applications include sending TTL signals and driving external devices such as the LED shown in the figure.

Parent topic:

Digital Signals

<!--NI_TOPIC bundle=ni-daqmx path=contcacqgen.html language=enus -->
## TOPIC 00043: Continuous Acquisition and Generation with Finite Buffer Size

- bundle_id: `ni-daqmx`
- source_path: `contcacqgen.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/contcacqgen.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx API uses circular buffers as shown in the following figure. For input operations, portions of data are read from the buffer while the buffer is filled. Likewise for output operations, portions of the buffer can be written to while the buffer is emptied. Using a circular buffer, you can

### Continuous Acquisition and Generation with Finite Buffer Size

The NI-DAQmx API uses circular buffers as shown in the following figure. For input operations, portions of data are read from the buffer while the buffer is filled. Likewise for output operations, portions of the buffer can be written to while the buffer is emptied. Using a circular buffer, you can set up your device to continuously acquire data in the background while NI-DAQmx retrieves the acquired data.

[IMAGE alt='image' src='GUID-5D48F54E-796A-42B3-AD20-287F369A9379-a5.svg']

When a continuous operation reaches the end of the buffer, it returns to the beginning and fills up (or in the case of output operations, reads from) the same buffer again. Your input application must retrieve data in blocks, from one location in the buffer, while the data enters the circular buffer at a different location, so newer data does not overwrite unread data.

While a circular buffer works well in many applications, two possible problems can occur with this type of acquisition: Your application might try to retrieve data from the buffer faster than data is placed into it, or your application might not retrieve data from the buffer before NI-DAQmx overwrites the data into the buffer. When your application tries to read data from the buffer that has not yet been collected, NI-DAQmx waits for the data to be acquired and then returns the data. If your application does not read the data from the circular buffer fast enough, you receive an error, stating that some data has been overwritten and lost. If losing data in this way is not important to you, change the setting of the OverWrite Mode attribute/property.

Parent topic:

Buffering

<!--NI_TOPIC bundle=ni-daqmx path=continuous-analog-input-programming-flowchart.html language=enus -->
## TOPIC 00044: Continuous Analog Input Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `continuous-analog-input-programming-flowchart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/continuous-analog-input-programming-flowchart.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to view, process, or log a subset of the samples as they are being acquired, you need to continually acquire samples. For these types of applications, set the sample mode to continuous. The following flowchart depicts the main steps required in an NI-DAQmx application for measuring volta

### Continuous Analog Input Programming Flowchart

If you want to view, process, or log a subset of the samples as they are being acquired, you need to continually acquire samples. For these types of applications, set the sample mode to continuous. The following flowchart depicts the main steps required in an NI-DAQmx application for measuring voltage. Instead, you can configure a task for continuous analog input using the DAQ Assistant.

[IMAGE alt='image' src='GUID-578247F4-4327-439E-983C-FE183E11971E-a5.gif']

Parent topic:

Analog Input Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=continuous-analog-output-programming-flowchart.html language=enus -->
## TOPIC 00045: Continuous Analog Output Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `continuous-analog-output-programming-flowchart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/continuous-analog-output-programming-flowchart.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps required in an NI-DAQmx application to continuously generate voltage samples. If you prefer, you can configure this task using the DAQ Assistant.

### Continuous Analog Output Programming Flowchart

The following flowchart depicts the main steps required in an NI-DAQmx application to continuously generate voltage samples. If you prefer, you can configure this task using the DAQ Assistant.

[IMAGE alt='image' src='GUID-6F5F5C82-0386-440F-8B40-6A25409D8279-a5.gif']

Parent topic:

Analog Output Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=continuous-counter-input-programming-flowchar.html language=enus -->
## TOPIC 00046: Continuous Counter Input Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `continuous-counter-input-programming-flowchar.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/continuous-counter-input-programming-flowchar.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps you must complete for continuous counting in an NI-DAQmx application. If you prefer, you can configure this task using the DAQ Assistant.^1Time-based measurements include period, semi-period, pulse width, two-edge separation, and digital frequency.^2Edg

### Continuous Counter Input Programming Flowchart

The following flowchart depicts the main steps you must complete for continuous counting in an NI-DAQmx application. If you prefer, you can configure this task using the DAQ Assistant.

[IMAGE alt='image' src='GUID-7E34AE54-0172-41DB-88F2-A2C2D24B9545-a5.gif']

<sup>1</sup>Time-based measurements include period, semi-period, pulse width, two-edge separation, and digital frequency.

<sup>2</sup>Edge counting-based measurements include edge counting, encoder-based position measurements, and GPS timestamp measurements.

Parent topic:

Counter Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=continuous-digital-input-programming-flowchar.html language=enus -->
## TOPIC 00047: Continuous Digital Input Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `continuous-digital-input-programming-flowchar.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/continuous-digital-input-programming-flowchar.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to view, process, or log a subset of the samples as they are being acquired, you need to continually acquire samples. For these types of applications, set the sample mode to continuous. The following flowchart depicts the main steps required in an NI-DAQmx application for acquiring digit

### Continuous Digital Input Programming Flowchart

If you want to view, process, or log a subset of the samples as they are being acquired, you need to continually acquire samples. For these types of applications, set the sample mode to continuous. The following flowchart depicts the main steps required in an NI-DAQmx application for acquiring digital signals. You can configure a task for continuously acquiring digital values using the DAQ Assistant.

[IMAGE alt='image' src='GUID-24CC76DB-F9AA-4510-8AD2-4CBABDF3C72A-a5.gif']

Note

Parent topic:

Digital Input Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=controlappcase3.html language=enus -->
## TOPIC 00048: Hardware-Timed Input, Software-Timed Output

- bundle_id: `ni-daqmx`
- source_path: `controlappcase3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/controlappcase3.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Requirement An analog input task must be hardware-timed. The output task does not need hardware synchronization with the sample clock edge. Solution Use the DAQmx real-time Report Missed Samples attribute/property, which returns an error if new samples are available before the read operation finishe

### Hardware-Timed Input, Software-Timed Output

Requirement

Solution

Report Missed Samples

Advantages

- Input samples are hardware-timed.
- Read, process, and write operations can overflow into the next sample period, as long as enough time remains for the subsequent read operation to complete on the next set of input samples. An application that acquires data from multiple channels on multiplexed devices (such as E Series and M Series) has to wait for the device to convert input samples before the read operation can return. By allowing process and write operations to overflow into the next sample period, the application takes advantage of otherwise idle time. This enables the application to achieve higher control-loop rates.

Restrictions

Output updates suffer from software jitter because they are not hardware-timed.

Parent topic:

NI-DAQmx Single-Point Real-Time Applications

#### Sample Application—Hardware-Timed Input, Software-Timed Output

An example of this kind of application is an analog control loop that reads samples from a specific number of multiplexed analog input channels, processes the data using a control algorithm (such as PID), and writes the new control values to the analog output channels using a software-timed task.

Timing Diagram

[IMAGE alt='image' src='GUID-358D8BA7-0704-410C-A2F3-74B9733B9589-a5.svg']

#### LabVIEW Example—Hardware-Timed Input, Software-Timed Output

Note

- Set the Report Missed Samples property for the analog input operation to True.
- The analog input operation returns an error if new samples are available before the read operation finishes converting samples from the previous iteration.

Sample Block Diagram

[IMAGE alt='image' src='GUID-31E08C53-03F9-43A6-AAD9-C832BA1EBFE7-a5.gif']

Note

- If, when an Analog Input Read overflow error occurs, you prefer to receive a warning rather than an error, set the Convert Late Errors to Warnings property to True.
- Do not use the Wait For Next Sample Clock VI and the Report Missed Samples property within the same LabVIEW loop.
- Only hardware-timed single-point analog input tasks support the Report Missed Samples property.
- Because the analog output task is software timed, the value is written out as soon as the write call is initiated. It does not wait for a hardware clock to output the data.

<!--NI_TOPIC bundle=ni-daqmx path=controlappcase4.html language=enus -->
## TOPIC 00049: Hardware-Timed Counter Tasks

- bundle_id: `ni-daqmx`
- source_path: `controlappcase4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/controlappcase4.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Requirement Use hardware-timed counter input operations to drive a control loop. Solution Use the Wait For Next Sample Clock function/VI to synchronize the counter operations with the counter's sample clock. Advantages Counter tasks allow for flexible timing and event detection operations that can d

### Hardware-Timed Counter Tasks

Requirement

Solution

Advantages

- Counter tasks allow for flexible timing and event detection operations that can drive the software processing of the control loop. In other words, the control loop can have a dynamic clock rate.
- NI-DAQmx returns an error if the Wait For Next Sample Clock function/VI does not start before the next sample clock edge arrives.

Restrictions

Read, process, and write operations are confined to the time available between the moment the device starts acquiring data and the moment the next sample clock edge arrives.

Parent topic:

NI-DAQmx Single-Point Real-Time Applications

Related concepts:

- LabVIEW Example—Hardware-Timed Counter Tasks

#### Sample Application—Hardware-Timed Counter Tasks

An example of this kind of application is a control loop that uses a counter input task, such as count edges, while controlling digital lines based on some predefined control logic. This sample application performs communication through the use of real-time FIFOs. In LabWindows/CVI, you can use a thread-safe queue instead of real-time FIFOs.

Timing Diagram

[IMAGE alt='image' src='GUID-272ADDD9-5161-42E6-9895-2553F9077FD2-a5.svg']

#### Sample Application 2—Hardware-Timed Counter Tasks

Another example application is a control loop that monitors discrete inputs and uses the values to update a counter output task, using pulse frequency mode to generate pulse-width modulation control signals. This example application performs communication through the use of real-time FIFOs. In LabWindows/CVI, you can use a thread-safe queue instead of real-time FIFOs.

Timing Diagram

[IMAGE alt='image' src='GUID-F354F4FA-6E4F-4009-B39B-11EB6C045237-a5.svg']

#### LabVIEW Example—Hardware-Timed Counter Tasks

Note

- Wire the Wait For Next Sample Clock VI to the counter input task.
- If the Wait For Next Sample Clock VI does execute before the arrival of the next sample clock edge, it returns an error.

Sample Block Diagram

[IMAGE alt='image' src='GUID-33E59DF6-D26B-4B9E-9379-CA0BE37D8E70-a5.gif']

Example 2

- Wire the Wait For Next Sample Clock VI to the counter output task.
- If the Wait For Next Sample Clock VI does not execute before the arrival of the next sample clock edge, it returns an error.

Sample Block Diagram

[IMAGE alt='image' src='GUID-922E33CB-E526-4B21-A483-638FB65B3214-a5.gif']

Note

- Use only one Wait For Next Sample Clock VI within a LabVIEW loop. If you have multiple hardware-timed I/O tasks within the same LabVIEW loop, you can connect the Wait For Next Sample Clock VI to any one hardware-timed single-point task within that loop.
- If, when a cycle overflow occurs, you want to receive a warning rather than an error, set the 
 DAQmx Real-Time»Convert Late Errors to Warnings property to True.
- Hardware-timed counter operations have no conversion period similar to that of multiplexed analog input. Therefore, the real-time FIFO can be placed anywhere within the LabVIEW loop.
- NI-DAQmx provides a mechanism to recover after missing a sample clock edge when performing counter writes. If this write recovery mechanism is not successful, NI-DAQmx returns an error, and subsequent operations on that task are no longer hardware timed.
- The 
 DAQmx Real-Time»Write Recovery Mode property allows you to choose between Wait For Interrupt or Polling mode for the recovery mechanism. Wait For Interrupt, which is the default, allows lower priority processes to execute while NI-DAQmx attempts to recover. Polling mode, on the other hand, allows for higher sampling rates.

<!--NI_TOPIC bundle=ni-daqmx path=controlappcase5.html language=enus -->
## TOPIC 00050: Software-Timed I/O

- bundle_id: `ni-daqmx`
- source_path: `controlappcase5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/controlappcase5.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Requirement The I/O tasks do not support hardware-timed operations. Solution Apply software timing to your time-critical loop by using the Timed Loop in LabVIEW or asynchronous timers in LabWindows/CVI. Configure your NI-DAQmx tasks to use on-demand timing. Advantages You can perform I/O control loo

### Software-Timed I/O

Requirement

Solution

Advantages

- You can perform I/O control loops with operations that are not hardware-timed.
- Read, process, and write operations are confined to the software timing period that you define with the Timed Loop or asynchronous timers.

Restrictions

I/O samples suffer from software jitter.

Parent topic:

NI-DAQmx Single-Point Real-Time Applications

#### Sample Application—Software-Timed I/O

An example of this kind of application is a digital I/O control loop. The application monitors the state of several discrete inputs and toggles the corresponding output based on the control algorithm. Hardware timing is not available for single-point digital I/O tasks in NI-DAQmx.

Timing Diagram

[IMAGE alt='image' src='GUID-417F8AB0-8D3F-45E0-8991-A63C28AFDA3D-a5.svg']

#### LabVIEW Example—Software-Timed I/O

Note

- A Timed Loop running off the system's time sources (millisecond or microsecond resolution) accomplishes the task. Configure the Timed Loop to run at the desired rate.
- Configure all tasks to be software-timed (on demand).
- The Timed Loop provides feedback to the application as to whether the previous iteration completed in time. It does this through the "Finished Late [i-1]" node.

Sample Block Diagram

[IMAGE alt='image' src='GUID-3F93C932-2700-4F96-9B05-FE7B690C2275-a5.gif']

Note

- The Timed Loop allows the application to adjust its period from within the loop, allowing the implementation of dynamic timing algorithms for control.
- Lower-priority processes can execute while the Timed Loop waits until its next iteration.
- Other software timing methods include the use of the Wait and Wait Until next multiple VIs (with microsecond or milliseconds resolution). These methods provide no feedback when the application falls behind.

<!--NI_TOPIC bundle=ni-daqmx path=controlappcase6.html language=enus -->
## TOPIC 00051: Hardware-Timed Simultaneously Updated I/O Using the Timed Loop (LabVIEW Only)

- bundle_id: `ni-daqmx`
- source_path: `controlappcase6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/controlappcase6.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Requirement I/O needs to be hardware-timed. All output values need to simultaneously update at the arrival of the sample clock edge. The application uses the Timed Loop. Solution Use the DAQmx Create Timing Source function/VI to create a timing source that drives a Timed Loop that contains the I/O o

### Hardware-Timed Simultaneously Updated I/O Using the Timed Loop (LabVIEW Only)

Requirement

Solution

Advantages

- Using a timing source allows you to specify an I/O signal (for example, the sample clock signal) to trigger the execution of Timed Loop iterations.
- Timing sources such as the Control Loop From Task provide strict lateness checking and allow other threads to execute while several analog channels are being multiplexed and sampled.
- The Timed Loop provides feedback as to whether the iterations complete in time.
- Multi-rate applications, using distinct I/O hardware subsystems, are possible by extending this approach to multiple Timed Loops.

Restrictions

- Minor increase in overhead when compared to a regular LabVIEW While Loop
- Requires additional code to handle warm-up iterations

Parent topic:

NI-DAQmx Single-Point Real-Time Applications

#### Sample Application—Hardware-Timed Simultaneously Updated I/O Using the Timed Loop (LabVIEW Only)

An example of this kind of application is an analog control loop that reads samples from a specific number of analog input channels, processes the data using a control algorithm (such as PID), and writes the new control values to the analog output channels.

You can create such an application with the Control Loop From Task timing source. The Control Loop From Task timing source uses the sample clock signal from the analog input task, which allows strict lateness-checking of all tasks associated with that sample clock.

The Control Loop From Task timing source also allows you to specify a delay between the time the sample clock event is handled and the time the Timed Loop starts executing. This delay, or sleep time, keeps the DAQmx Read function/VI inside the Timed Loop from using 100% of the CPU time available while waiting for the analog input samples to be multiplexed and digitized.

Timing Diagram

[IMAGE alt='image' src='GUID-90F4EF3E-CE54-4BA6-82BE-D29266B5B09B-a5.svg']

#### LabVIEW Example—Hardware-Timed Simultaneously Updated I/O Using the Timed Loop

- Create a Control Loop From Task timing source for the Timed Loop. This signal serves as the timebase that drives the execution of the Timed Loop.
- The Timed Loop provides feedback to the application as to whether the previous iteration completed in time. It does this through the "Finished Late [i-1]" node.
- Allow a few warm-up iterations to account for the effects of processor-caching and other events that may occur during the first iterations of the loop.

Sample Block Diagram

[IMAGE alt='image' src='GUID-E6C6D056-AE86-40A2-8592-456AAA578491-a5.gif']

Note

- The DAQmx Read VI is implicitly configured to polling mode when using the Control Loop From Task timing source. Polling mode avoids the additional scheduling overhead associated with interrupts inside the Timed Loop.
- You can increase the Analog Input Conversion Rate manually through DAQmx Timing properties. This reduces the total amount of time spent converting the requested number of samples. It is important to consider the minimum settling time specifications for the complete data acquisition system to avoid signal degradation and interference.
- Do not use the Wait For Next Sample Clock VI for any of these tasks.
- Lower-priority processes, including other Timed Loops with lower priorities, can execute while the Timed Loop waits until its next iteration.
- To optimize multi-channel control applications in which lower-priority threads might require additional processing time, provide a non-zero value for the sleep time (us) parameter of the DAQmx Create Timing Source VI. This non-zero value allows other threads to use the time spent converting analog input samples to perform other tasks such as communication or logging to disk.
- The maximum amount of sleep time you can set without impacting the overall rate of the application depends on several factors, including the number of analog channels being acquired, the sample conversion rate, and the system's specifications.

The following diagram shows, for multiple channel configurations, the effect of the amount of sleep over the maximum achievable rate and the amount of work lower-priority threads can execute at such rates.

[IMAGE alt='image' src='GUID-D0C1A02A-FC78-4A7B-8B89-35D7DF172D33-a5.png']

*See benchmark configuration below.

The graph shows that, when acquiring 8 channels using a specific hardware and software configuration, the maximum achievable rate decreases as soon as the amount of sleep time increases from 0 to 5 µs. This is not, however, the case for the 12- and 16-channel configurations, for which increasing the amount of sleep up to 10 and 15 µs respectively has no visible effect on the maximum achievable I/O rates. In the 12- and 16-channel case, the additional sleep interval allows other threads to execute more work (refer to definition below) without affecting the overall I/O rate of the application.

Benchmark Configuration

- Hardware Configuration:
  - NI PXI-8196 RT Controller
  - NI PXI-6070 E Series MIO device
  - NI PXI-6723 Analog Output device
- Software Configuration:
  - LabVIEW Real-Time 8.0
  - NI-DAQmx 8.0
  - Ethernet driver set to polling mode
- Benchmark details:
  - A work unit is defined as the number of times a normal-priority loop can increment an unsigned 64-bit number while the I/O Timed Loop, depicted in the sample block diagram above, runs in parallel with it.
  - The analog input conversion is not explicitly configured. This means that the DAQmx driver auto-calculates it based on the number of channels and desired sample clock rate.

<!--NI_TOPIC bundle=ni-daqmx path=counterfrequencycoercion.html language=enus -->
## TOPIC 00052: Counter Frequency Coercion

- bundle_id: `ni-daqmx`
- source_path: `counterfrequencycoercion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/counterfrequencycoercion.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency of the counter output must be evenly divisible into the frequency of its timebase. The resulting period is further divided by the duty cycle, which defines how long the signal stays high and how long it stays low for each period. If the requested frequency and duty cycle combination ca

### Counter Frequency Coercion

The frequency of the counter output must be evenly divisible into the frequency of its timebase. The resulting period is further divided by the duty cycle, which defines how long the signal stays high and how long it stays low for each period. If the requested frequency and duty cycle combination can't be produced exactly, then DAQmx will coerce the signal to the closest frequency and duty cycle that is possible. If you want to define exactly how long the signal stays high and low, use ticks instead.

Parent topic:

Counters

Related concepts:

- Clock Frequency Coercion

<!--NI_TOPIC bundle=ni-daqmx path=countersig.html language=enus -->
## TOPIC 00053: Counters

- bundle_id: `ni-daqmx`
- source_path: `countersig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/countersig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Counters measure and generate digital signals. Counters are used commonly to count edges and for time measurements, such as measuring digital frequency or the period of a signal. The signal connections required for counters vary depending on the device and your application.

### Counters

Counters measure and generate digital signals. Counters are used commonly to count edges and for time measurements, such as measuring digital frequency or the period of a signal. The signal connections required for counters vary depending on the device and your application.

Parent topic:

Digital Signals

Related concepts:

- Connecting Counter Signals

<!--NI_TOPIC bundle=ni-daqmx path=countsigconn6010.html language=enus -->
## TOPIC 00054: 37-Pin DSUB Signal Connections for Counters

- bundle_id: `ni-daqmx`
- source_path: `countsigconn6010.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/countsigconn6010.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default input terminals for various counter measurements for devices that use the 37-Pin DSUB connector such as the NI 6010, NI 6154, and NI 623x. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQm

### 37-Pin DSUB Signal Connections for Counters

The following table lists the default input terminals for various counter measurements for devices that use the 37-Pin DSUB connector such as the NI 6010, NI 6154, and NI 623x. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties.

| Measurement | Ctr0 | Ctr1 |
| --- | --- | --- |
| Count Edges | Edges: PFI 0 Count Direction: PFI 2 | Edges: PFI 3 Count Direction: PFI 5 |
| Pulse Width Measurement | PFI 1 | PFI 4 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 1 | PFI 4 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 0 | PFI 3 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 0 | PFI 3 |
| Semiperiod Measurement | PFI 1 | PFI 4 |
| Two-Edge Separation Measurement | Start: PFI 2 Stop: PFI 1 | Start: PFI 5 Stop: PFI 4 |

The following table lists the output terminals for counter output. You can use a different PFI line for any of the output terminals.

| Ctr0 | Ctr1 |
| --- | --- |
| PFI 6 | PFI 7 |

Parent topic:

Connecting Counter Signals

<!--NI_TOPIC bundle=ni-daqmx path=countterms.html language=enus -->
## TOPIC 00055: Counter Accessory Terminal Names

- bundle_id: `ni-daqmx`
- source_path: `countterms.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/countterms.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the revised names for counter terminal names. Original Terminal Names Revised Terminal Names Explanation GPCTR1_SOURCE CTR1SOURCE Placed as a hint next to the PFI terminal where the Ctr1Source signal can be emitted GPCTR1_GATE CTR1GATE Placed as a hint next to the PFI termi

### Counter Accessory Terminal Names

The following table lists the revised names for counter terminal names.

| Original Terminal Names | Revised Terminal Names | Explanation |
| --- | --- | --- |
| GPCTR1_SOURCE | CTR1SOURCE | Placed as a hint next to the PFI terminal where the Ctr1Source signal can be emitted |
| GPCTR1_GATE | CTR1GATE | Placed as a hint next to the PFI terminal where the Ctr1Gate signal can be emitted |
| GPCTR1_OUT | CTR1OUT | The name of the terminal where the Ctr1Out signal appears |
| GPCTR0_SOURCE | CTR0SOURCE | Placed as a hint next to the PFI terminal where the Ctr0Source signal can be emitted |
| GPCTR0_GATE | CTR0GATE | Placed as a hint next to the PFI terminal where the Ctr0Gate signal can be emitted |
| GPCTR0_OUT | CTR0OUT | The name of the terminal where the Ctr0Out signal appears |
| FREQ_OUT | FREQ OUT | The name of the terminal where the output of the 4-bit clock divider signal appears |

Parent topic:

Terminal Names

<!--NI_TOPIC bundle=ni-daqmx path=createchansapi.html language=enus -->
## TOPIC 00056: Creating Virtual Channels with the API

- bundle_id: `ni-daqmx`
- source_path: `createchansapi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/createchansapi.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `task`
- source_description: The following example illustrates the difference between physical and virtual channels and demonstrates how to create virtual channels with the API. Problem Create an NI-DAQmx virtual channel to measure temperature in the range 50° C to 200° C using a J-type thermocouple wired to channel 0 on an M S

### Creating Virtual Channels with the API

The following example illustrates the difference between physical and virtual channels and demonstrates how to create virtual channels with the API.

Problem

Create an NI-DAQmx virtual channel to measure temperature in the range 50° C to 200° C using a J-type thermocouple wired to channel 0 on an M Series device configured as Device 1. Use LabVIEW or LabWindows™/CVI™ to write your application.

Solution

1. Call the AI Temp TC instance of the DAQmx Create Virtual Channel VI in LabVIEW (DAQmxCreateAIThrmcplChan function in LabWindows/CVI).
2. Use 
 Dev1/ai0 as the physical channel on the device to which the thermocouple signal is connected.
3. Specify 
 myThermocoupleChannel as the name to assign to your virtual channel.
4. Select the appropriate values for the thermocouple type and range inputs. NI-DAQmx applies these attributes to the virtual channel.

You have now created a virtual channel.

Parent topic:

Channels: Physical, Virtual, Local Virtual, and Global Virtual

Related concepts:

- Choosing Whether to Use the API or the DAQ Assistant
- Physical Channels
- Internal Channels

<!--NI_TOPIC bundle=ni-daqmx path=createtaskapi.html language=enus -->
## TOPIC 00057: Creating Tasks with the API

- bundle_id: `ni-daqmx`
- source_path: `createtaskapi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/createtaskapi.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `task`
- source_description: The following example illustrates how to create a task with the API: Problem Create an NI-DAQmx task to measure temperature in the range 50°C to 200°C using a J-type thermocouple that is wired to channel 0 on an M Series device configured as Device 1. Sample the temperature 10 times per second, and

### Creating Tasks with the API

The following example illustrates how to create a task with the API:

Problem

Create an NI-DAQmx task to measure temperature in the range 50°C to 200°C using a J-type thermocouple that is wired to channel 0 on an M Series device configured as Device 1. Sample the temperature 10 times per second, and acquire 10,000 samples. Use LabVIEW or LabWindows/CVI to write your application.

Solution

1. Call the AI Temp TC instance of the DAQmx Create Virtual Channel VI in LabVIEW (DAQmxCreateAIThrmcplChan function in LabWindows/CVI).
2. Specify 
 Dev1/ai0 as the physical channel for the device connected to the thermocouple signal.
3. Specify 
 myThermocoupleChannel as the name to assign to your virtual channel.
4. Select the appropriate values for the thermocouple type and range inputs. NI-DAQmx applies these attributes to the virtual channel.
5. Call the Sample Clock instance of DAQmx Timing VI in LabVIEW (or DAQmxCfgSampClkTiming function in LabWindows/CVI), specifying a rate of 10 Hz and a sample mode of finite.
6. Call the DAQmx Start Task VI (DAQmxStartTask in LabWindows/CVI).
7. Call the Analog 1D DBL 1Chan NSamp instance of DAQmx Read VI (DAQmxReadAnalogF64 in LabWindows/CVI), specifying number of samples per channel as 10,000.
8. Call the DAQmx Stop Task VI (DAQmxStopTask function in LabWindows/CVI) after the desired number of samples have been acquired.
9. Call the DAQmx Clear Task VI (DAQmxClearTask function in LabWindows/CVI).

Note

Parent topic:

Tasks in NI-DAQmx

Related concepts:

- Creating Channels and Tasks with the DAQ Assistant
- Choosing Whether to Use the API or the DAQ Assistant

<!--NI_TOPIC bundle=ni-daqmx path=creating-an-application-with-labwindowscvi.html language=enus -->
## TOPIC 00058: Creating an Application with LabWindows/CVI

- bundle_id: `ni-daqmx`
- source_path: `creating-an-application-with-labwindowscvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/creating-an-application-with-labwindowscvi.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you program your NI-DAQmx-supported device in LabWindows/CVI, you can interactively create global or local virtual channels and tasks by launching the DAQ Assistant from MAX or from within LabWindows/CVI. You can generate the configuration code based on your task or channel in LabWindows/CVI. Ref

### Creating an Application with LabWindows/CVI

If you program your NI-DAQmx-supported device in LabWindows/CVI, you can interactively create global or local virtual channels and tasks by launching the DAQ Assistant from MAX or from within LabWindows/CVI. You can generate the configuration code based on your task or channel in LabWindows/CVI. Refer to the DAQ Assistant Help for additional information about generating code. You also can create local virtual channels and tasks, and write your own applications using the NI-DAQmx API.

For help with NI-DAQmx functions, refer to NI-DAQmx C Function Reference Help. For general help with programming in LabWindows/CVI, refer to LabWindows/CVI Help, accessible through Start»All Programs»National Instruments»LabWindows CVI»LabWindows CVI Help.

For help with using the DAQ Assistant with LabWindows/CVI, refer to Using the DAQ Assistant in NI LabWindows/CVI.

Parent topic:

NI-DAQmx Overview

Related information:

- Using the DAQ Assistant in NI LabWindows™/CVI™

<!--NI_TOPIC bundle=ni-daqmx path=crio_considerations.html language=enus -->
## TOPIC 00059: CompactRIO Considerations

- bundle_id: `ni-daqmx`
- source_path: `crio_considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/crio_considerations.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information on using the following CompactRIO and CompactRIO single-board controllers with NI-DAQmx: cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048, 9049, 9053, 9054, 9055, 9056, 9057, and 9058 controllers. sbRIO-9603, 9608, 9609, 9628, 9629, and 9638 controllers. Slot Pro

### CompactRIO Considerations

This section contains information on using the following CompactRIO and CompactRIO single-board controllers with NI-DAQmx:

- cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047,
 9048, 9049, 9053, 9054, 9055, 9056, 9057, and 9058 controllers.
- sbRIO-9603, 9608, 9609, 9628, 9629, and 9638
 controllers.

Parent topic:

NI-DAQmx Device Considerations

Related concepts:

- CompactRIO Timing Engines
- CompactDAQ, CompactRIO, and TestScale Simultaneous Tasks
- Time-Based Features for Network-Synchronized Devices

#### Slot Program Mode

In MAX, when you add a C Series module to a CompactRIO controller there are three program modes to choose from.

- Real-Time (NI-DAQmx)
- Real-Time Scan
- LabVIEW FPGA

In order for DAQmx to communicate with the module, the module must be in 
 Real-Time (NI-DAQmx) mode.

Note

Related information:

- Software Support for CompactRIO and CompactDAQ

#### Hardware Timed Single Point Sample Mode

The CompactRIO controllers support hardware timed single point (HWTSP) sample mode with a few caveats.

- The NI 9260 does not support HWTSP.
- The NI 9361 does not support HWTSP.
- C Series Scanned Devices do not default to the lowest latency mode. They default to a slower convert rate to allow more time for settling. This behavior limits the maximum HWTSP acquisition rate of the module to allow more time for settling. If you prefer, you can configure the module for a faster acquisition rate with less time for settling. For additional information, see 
 Sampling Rate Considerations .

Related concepts:

- AI Sampling Rate Considerations
- C Series Scanned Devices
- Sampling Rate Considerations

#### Model Names

CompactRIO may use slightly different C Series model names and product IDs compared to CompactDAQ. For CompactRIO, see 
 *C Series Module IDs* on ni.com.

Related information:

- C Series Module IDs

#### Timing Considerations

CompactRIO controllers handle sampling rate and the default value for the hardware-timed mode differently than CompactDAQ chassis.

In a CompactRIO or Single-Board RIO controller with C Series Slow Sample devices, such as the NI 9211, if the sampling rate of a hardware-timed acquisition exceeds the maximum sampling rate of the module, DAQmx generates warning or errors. When a Slow Sample device is in the same task as a non-Slow Sample device, exceeding the maximum sampling rate of the Slow Sample device results in the most recently acquired sample being read multiple times. In this scenario, the first sample of a hardware-timed acquisition with C Series Slow Sample devices is sampled when the task is committed.

##### Default Settings for the AI.ADCTimingMode Attribute/Property

For all modules in the CompactRIO and Single-Board RIO controllers, the default value in hardware-timed mode is automatically determined based on Sample Clock Rate.

Related concepts:

- AI Sampling Rate Considerations
- Configurable Timing for C Series Devices
- CompactRIO Timing Engines
- CompactDAQ, CompactRIO, and TestScale Simultaneous Tasks
- C Series Device Groupings
- Sampling Rate Considerations
- CompactDAQ and CompactRIO Simultaneous Tasks

#### Shared Trigger Bus

On the CompactRIO and CompactRIO Single-Board controllers, NI-DAQmx provides a simple trigger
 bus between LabVIEW FPGA and NI-DAQmx with the following characteristics:

| CompactRIO[1]1 cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048, 9049, 9053, 9054, 9055, 9056, 9057, and 9058 | CompactRIO Single-Board[2]2 sbRIO-9603, 9608, 9609, 9628, 9629, and 9638 |
| --- | --- |
| Four fixed direction LabVIEW FPGA to NI-DAQmx Lines: cRIO_Trig0, cRIO_Trig1, cRIO_Trig2, and cRIO_Trig3 are terminals that are driven from LabVIEW FPGA to NI-DAQmx. LabVIEW FPGA: output boolean chassis I/O NI-DAQmx: common-visibility source terminals Can be used with Immediate Routing and Task-Based RoutingDoes not prescribe to Lazy Line Transitions rules Four Fixed Direction NI-DAQmx to LabVIEW FPGA Lines: cRIO_Trig4, cRIO_Trig5, cRIO_Trig6, and cRIO_Trig7 are terminals that are driven from NI-DAQmx to LabVIEW FPGA. LabVIEW FPGA: input boolean chassis I/O Minimum pulse width requirements: 12.5 ns for most destination terminals 150 ns for SyncPulse terminals NI-DAQmx: common-visibility destination terminals Can be used with Immediate Routing and Task-Based RoutingDoes not prescribe to Lazy Line Transitions rules | Two fixed direction LabVIEW FPGA to NI-DAQmx Lines: cRIO_Trig0 and cRIO_Trig1 are terminals that are driven from LabVIEW FPGA to NI-DAQmx. LabVIEW FPGA: output boolean chassis I/O NI-DAQmx: common-visibility source terminals Can be used with Immediate Routing and Task-Based RoutingDoes not prescribe to Lazy Line Transitions rules Two Fixed Direction NI-DAQmx to LabVIEW FPGA Lines: cRIO_Trig2 and cRIO_Trig3 are terminals that are driven from NI-DAQmx to LabVIEW FPGA. LabVIEW FPGA: input boolean chassis I/O Minimum pulse width requirements: 12.5 ns for most destination terminals 150 ns for SyncPulse terminals NI-DAQmx: common-visibility destination terminals Can be used with Immediate Routing and Task-Based RoutingDoes not prescribe to Lazy Line Transitions rules |

Note

- Change detection event exported from a buffered
 change detection DI task
- Sample clock exported from a hardware-timed
 digital input or output task running faster than 3.5 MHz
- Counter output event exported from a counter task that configures its output behavior
 to pulse

Related concepts:

- Immediate Routing
- Task-Based Routing
- Lazy Line Transitions

[<sup>1</sup>](#note_ref-d9754e345) cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047, 9048,
 9049, 9053, 9054, 9055, 9056, 9057, and 9058

[<sup>2</sup>](#note_ref-d9754e351) sbRIO-9603, 9608, 9609, 9628, 9629, and 9638

<!--NI_TOPIC bundle=ni-daqmx path=daqversusapi.html language=enus -->
## TOPIC 00060: Choosing Whether to Use the API or the DAQ Assistant

- bundle_id: `ni-daqmx`
- source_path: `daqversusapi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/daqversusapi.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When creating a new application, you can choose to use DAQ Assistant or the API. Advantages of Using the DAQ Assistant: The DAQ Assistant requires no programming. You can configure channels, timing, triggering, and scales interactively. The DAQ Assistant can decrease development time. You can create

### Choosing Whether to Use the API or the DAQ Assistant

When creating a new application, you can choose to use DAQ Assistant or the API.

Advantages of Using the DAQ Assistant:

- The DAQ Assistant requires no programming. You can configure channels, timing, triggering, and scales interactively.
- The DAQ Assistant can decrease development time. You can create a complete application in a matter of minutes.
- If you create your application using the DAQ Assistant and later need functionality that it doesn't expose, you can easily generate the equivalent API code from your DAQ Assistant task if you use an NI ADE such as LabVIEW, LabWindows/CVI, or Measurement Studio.

Advantages of Using the API:

- The API contains advanced features not exposed by the DAQ Assistant.
- The API provides additional flexibility, allowing you to customize your application to suit your needs.
- The API gives you tighter control over the performance of your application.

Parent topic:

Channels and Tasks in NI-DAQmx

<!--NI_TOPIC bundle=ni-daqmx path=datalogging.html language=enus -->
## TOPIC 00061: TDMS Logging

- bundle_id: `ni-daqmx`
- source_path: `datalogging.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/datalogging.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Technical Data Management Streaming (TDMS) is a binary file format that allows for high-speed data logging. When you enable TDMS data logging, NI-DAQmx can stream data directly from the device buffer to the hard disk. NI-DAQmx improves performance and reduces the disk footprint by writing raw data t

### TDMS Logging

Technical Data Management Streaming (TDMS) is a binary file format that allows for high-speed data logging. When you enable TDMS data logging, NI-DAQmx can stream data directly from the device buffer to the hard disk. NI-DAQmx improves performance and reduces the disk footprint by writing raw data to the TDMS file, including the scaling information separately for use when reading back the TDMS file. You can also read data while logging to disk.

For optimal performance, follow these tips:

- Use a PCI Express or PXI Express device with a RAID array.
- Log data only. For very high-speed acquisitions, logging and reading data can slow performance.
- If logging and reading data, ensure the number of samples per channel to read is evenly divisible by the sector size of the hard disk.
- If manually configuring the buffer size, choose a multiple of eight times the sector size of the hard disk. For instance, if your sector size is 512 bytes, your buffer size might be 4,096 samples.

NI provides a number of mechanisms for reading TDMS files, including software support in
 LabVIEW, LabWindows/CVI, ANSI C, DIAdem, and Measurement Studio. In addition, NI provides a
 Microsoft Excel plug in. Refer to [ni.com/tdms](http://digital.ni.com/express.nsf/bycode/ex57sh)
 for additional information. For information about high-speed data streaming, refer to
 ni.com/streaming.

Parent topic:

Reading and Writing Data

Related information:

- The NI TDMS File Format
- Streaming Architecture of the Industry’s Highest Performance PXI Express Platform

<!--NI_TOPIC bundle=ni-daqmx path=dataorganization.html language=enus -->
## TOPIC 00062: Data Organization

- bundle_id: `ni-daqmx`
- source_path: `dataorganization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/dataorganization.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The number of channels and the number of samples being read generally affect data organization. For example, if 100 samples are read for eight analog channels using 64-bit floating-point format, a two-dimensional array is used with one index selecting the channel and the second index selecting the s

### Data Organization

The number of channels and the number of samples being read generally affect data organization. For example, if 100 samples are read for eight analog channels using 64-bit floating-point format, a two-dimensional array is used with one index selecting the channel and the second index selecting the sample. On the other hand, a simple floating-point scalar value is sufficient to read one sample for one analog channel using the 64-bit floating-point format. In general, the data organization for a particular read or write call is the simplest reasonable format that can handle the number of channels and samples requested.

There are often multiple legal data organizations to choose from. The main tradeoff to consider for data organization is difficulty in manipulation of the data. You can use data organizations that can handle multiple channels and multiple samples, but they are generally the most complicated to manipulate.

Performance is similar for equivalent operations used to read or write data with different data organizations.

Waveform Data Organization

1D Waveform Array Data Organization

Scalar Data Organization

Scalar data is generally not a good match for high-speed multiple sample applications.

Scalar data also is not a good choice if multiple channels are acquired or generated simultaneously. Using a multiple channel organization is easier and in the case of output operations is actually a requirement.

Array Data Organization

Raw Data Organization

Parent topic:

Selecting Read and Write Data Format and Organization

Related concepts:

- Raw Data

<!--NI_TOPIC bundle=ni-daqmx path=deployment.html language=enus -->
## TOPIC 00063: Deployment

- bundle_id: `ni-daqmx`
- source_path: `deployment.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/deployment.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deployment refers to developing an application so that it can be distributed, or deployed, on a different computer than the one on which the application was developed. To deploy an application, you need the saved application and any configuration information the application and system requires. When

### Deployment

*Deployment* refers to developing an application so that it can be
 distributed, or deployed, on a different computer than the one on which the application
 was developed. To deploy an application, you need the saved application and any
 configuration information the application and system requires.

NI-DAQmx

- Tasks
- Channels
- Scales
- Device setups

You can use the NI MAX Export Wizard to save and transfer this configuration data. The
 wizard allows you to export settings to a file that can be imported on another
 system.

Note

For detailed instructions on exporting and importing configuration data in NI MAX, see
 the official Knowledge Base article, *Export/Import the System Configuration in NI
 MAX*.

Parent topic:

Distributed Applications

Related information:

- Export/Import the System Configuration in NI MAX

#### Developing Applications for Deployment

You can deploy NI-DAQmx applications in several ways:

- You can use the MAX Export Wizard to deploy an entire setup to another computer, including tasks, channels, scales, and devices.
- You can use the MAX Export Wizard to deploy an entire setup, except the device configurations, to another computer. You might choose to do this if the target computer already has tasks that rely on existing device configurations. In this case, you might have to make modifications after deployment so that your tasks and channels refer to the device configurations on the target computer.
- You can use the MAX Export Wizard initially to deploy a fixed set of device, scale, and global virtual channel configurations among a group of users. Each member of the group can create tasks that rely on the shared configurations, then create applications that use these tasks, and finally share the applications within the group. In some cases, the tasks deploy with the applications automatically. In other cases, you must deploy the tasks separately from the applications. Refer to the Deploying Tasks and Channels section for more information.

#### Deploying Tasks and Channels

Your tasks and channels deploy automatically with your application under the following circumstances:

- You use LabVIEW Express VIs for your DAQ applications, and the tasks use local channels only.
- You save your tasks within a LabWindows/CVI or Measurement Studio project, and the tasks use local channels only.
- You create your tasks and channels programmatically using the NI-DAQmx API.

You must deploy your tasks and channels using the MAX Export Wizard if you create your tasks and channels in the following ways:

- You create your tasks and channels directly in MAX.
- You create your tasks and channels in LabVIEW from the Task Name and Channel Name controls and do not generate configuration code.
- You create your tasks in LabWindows/CVI and neither generate configuration code nor copy the tasks to your project.
- You create a SignalExpress project that includes a global virtual channel.
- You use LabVIEW Express VIs for your DAQ applications with tasks that use global virtual channels, but do not use code generation. 
 Note If your project uses global virtual channels that were added, not copied, generating a LabVIEW diagram from SignalExpress still requires deployment of channels using the MAX Export Wizard.

<!--NI_TOPIC bundle=ni-daqmx path=dev-groups.html language=enus -->
## TOPIC 00064: Device Groups in NI-DAQmx

- bundle_id: `ni-daqmx`
- source_path: `dev-groups.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/dev-groups.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following list to see how devices are grouped in NI-DAQmx. FieldDAQ FD-11601 FD-11603 FD-11605 FD-11613 FD-11614 FD-11634 FD-11637 CompactRIO Single-Board Controllers sbRIO-9603 sbRIO-9608 sbRIO-9609 sbRIO-9628 sbRIO-9629 sbRIO-9638 CompactRIO Controllers cRIO-9040 cRIO-9041 cRIO-9042 c

### Device Groups in NI-DAQmx

Refer to the following list to see how devices are grouped in NI-DAQmx.

#### FieldDAQ

- FD-11601
- FD-11603
- FD-11605
- FD-11613
- FD-11614
- FD-11634
- FD-11637

#### CompactRIO Single-Board
 Controllers

- sbRIO-9603
- sbRIO-9608
- sbRIO-9609
- sbRIO-9628
- sbRIO-9629
- sbRIO-9638

#### CompactRIO Controllers

- cRIO-9040
- cRIO-9041
- cRIO-9042
- cRIO-9043
- cRIO-9045
- cRIO-9046
- cRIO-9047
- cRIO-9048
- cRIO-9049
- cRIO-9053
- cRIO-9054
- cRIO-9055
- cRIO-9056
- cRIO-9057
- cRIO-9058

#### X Series DAQ (Multifunction
 I/O)

- NI 6320
- NI 6321
- NI 6323
- NI 6341
- NI 6343
- NI 6345
- NI 6346
- NI 6347
- NI 6349
- NI 6351
- NI 6353
- NI 6355
- NI 6356
- NI 6357
- NI 6358
- NI 6361
- NI 6363
- NI 6365
- NI 6366
- NI 6368
- NI 6374
- NI 6375
- NI 6376
- NI 6378
- NI 6381
- NI 6383
- NI 6386
- NI 6396

#### M Series DAQ (Multifunction
 I/O)

- NI 6210/11/12/15/16/18
- NI 6220
- NI 6221
- NI 6224
- NI 6225
- NI 6229
- NI 6230/32/33/36/38/39
- NI 6250
- NI 6251
- NI 6254
- NI 6255
- NI 6259
- NI 6280
- NI 6281
- NI 6284
- NI 6289

#### S Series DAQ

- NI 6110
- NI 6111
- NI 6115
- NI 6120
- NI 6122
- NI 6123
- NI 6124
- NI 6132
- NI 6133
- NI 6143
- NI 6154

#### SC Express

- NI 4300
- NI 4302
- NI 4303
- NI 4304
- NI 4305
- NI 4309
- NI 4310
- NI 4322
- NI 4330
- NI 4331
- NI 4339
- NI 4340
- NI 4353
- NI 4357

#### C Series, Network DAQ, and USB
 DAQ

- NI 9201
- NI 9202
- NI 9203
- NI 9204
- NI 9205
- NI 9206
- NI 9207
- NI 9208
- NI 9209
- NI 9210
- NI 9211
- NI 9212
- NI 9213
- NI 9214
- NI 9215
- NI 9216
- NI 9217
- NI 9218
- NI 9219
- NI 9220
- NI 9221
- NI 9222
- NI 9223
- NI 9224
- NI 9225
- NI 9226
- NI 9227
- NI 9228
- NI 9229
- NI 9230
- NI 9231
- NI 9232
- NI 9234
- NI 9235
- NI 9236
- NI 9237
- NI 9237(DSUB)
- NI 9238
- NI 9239
- NI 9242
- NI 9244
- NI 9246
- NI 9247
- NI 9250
- NI 9251
- NI 9252
- NI 9253
- NI 9260
- NI 9262
- NI 9263
- NI 9264
- NI 9265
- NI 9266
- NI 9269
- NI 9320
- NI 9326
- NI 9344
- NI 9361
- NI 9375
- NI 9401
- NI 9402
- NI 9403
- NI 9411
- NI 9421
- NI 9422
- NI 9423
- NI 9425
- NI 9426
- NI 9435
- NI 9436
- NI 9437
- NI 9469
- NI 9472
- NI 9474
- NI 9475
- NI 9476
- NI 9477
- NI 9478
- NI 9481
- NI 9482
- NI 9485
- NI 9775

#### CompactDAQ Chassis

- NI cDAQ-9171
- NI cDAQ-9174
- NI cDAQ-9178
- NI cDAQ-9179
- NI cDAQ-9181
- NI cDAQ-9184
- NI cDAQ-9185
- NI cDAQ-9188
- NI cDAQ-9189
- NI cDAQ-9188XT
- NI cDAQ-9191

#### CompactDAQ Controllers

- NI cDAQ-9132
- NI cDAQ-9133
- NI cDAQ-9134
- NI cDAQ-9135
- NI cDAQ-9136
- NI cDAQ-9137

#### AO Series

- NI 6703
- NI 6704
- NI 6711
- NI 6713
- NI 6722
- NI 6723
- NI 6731
- NI 6733
- NI 6738
- NI 6739

#### Digital I/O

- NI 6501
- NI 6503
- NI 6508
- NI 6509
- NI 6510
- NI 6511
- NI 6512
- NI 6513
- NI 6514
- NI 6515
- NI 6516
- NI 6517
- NI 6518
- NI 6519
- NI 6520
- NI 6521
- NI 6525
- NI 6527
- NI 6528
- NI 6529
- NI 6533
- NI 6534
- NI 6535
- NI 6535B
- NI 6536
- NI 6536B
- NI 6537
- NI 6537B
- NI DIO-32HS
- NI DIO-96

#### TIO Series

- NI 6601
- NI 6602
- NI 6608
- NI 6612
- NI 6614
- NI 6624

#### Dynamic Signal Acquisition
 (DSA)

- NI 4431
- NI 4432
- NI 4461
- NI 4462
- NI 4463
- NI 4464
- NI 4466
- NI 4472/B
- NI 4474
- NI 4480
- NI 4481
- NI 4492
- NI 4495
- NI 4496
- NI 4497
- NI 4498
- NI 4499
- NI 4610

#### Academic Devices

- NI ELVIS II
- NI ELVIS II+
- NI myDAQ

#### Low-Cost USB

- NI 6000
- NI 6001
- NI 6002
- NI 6003
- NI 6008
- NI 6009
- NI TC01

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=devcalibrate.html language=enus -->
## TOPIC 00065: Device Calibration

- bundle_id: `ni-daqmx`
- source_path: `devcalibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/devcalibrate.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: What Is Device Calibration? Device calibration consists of verifying the measurement accuracy of a device and adjusting for any measurement error. Verification consists of measuring the performance of the device and comparing these measurements to the published specifications. During calibration, yo

### Device Calibration

Parent topic:

Calibration

#### What Is Device Calibration?

*Device calibration* consists of verifying the measurement accuracy of a device and adjusting for any measurement error. Verification consists of measuring the performance of the device and comparing these measurements to the published specifications. During calibration, you supply and read voltage levels or other signals using external standards, then you adjust the device calibration constants. The new calibration constants are stored in the EEPROM. These calibration constants are loaded from memory as needed to adjust for the error in the measurements taken by the device. There are two kinds of calibration, external and self. For more information on calibrating your device with NI-DAQmx, refer to Device Calibration Considerations. For detailed external calibration procedures, refer to ni.com/calibration.

Related concepts:

- Device Calibration Considerations

Related information:

- Calibration Services

#### External Calibration

External calibration, which is typically performed by a metrology lab, requires using a high-precision voltage source to verify and adjust calibration constants. This procedure replaces all calibration constants in the EEPROM and is equivalent to a factory calibration. Because the external calibration procedure changes all EEPROM constants, it invalidates the original calibration certificate. If an external calibration is done with a NIST-certified voltage source, a new NIST traceability certificate can be issued.

#### Self-Calibration (Internal Calibration)

Self-calibration adjusts the calibration constants with respect to an onboard reference stored on the device. The new calibration constants are defined with respect to the calibration constants created during an external calibration to ensure that the measurements are traceable to these external standards. The new calibration constants do not affect the constants created during an external calibration because they are stored in a different area of the device memory. You can perform a self-calibration at any time to adjust the device for use in environments other than those in which the device was externally calibrated. You use the DAQmx Self Calibrate (or DAQmxSelfCal) function/VI to perform a self-calibration.

Note

<!--NI_TOPIC bundle=ni-daqmx path=devconsid.html language=enus -->
## TOPIC 00066: NI-DAQmx Device Considerations

- bundle_id: `ni-daqmx`
- source_path: `devconsid.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/devconsid.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file contains information specific to analog output (AO) Series devices, B Series devices, C Series devices, digital I/O (DIO) devices, DSA devices, E Series devices, FieldDAQ Devices, M Series devices, S Series devices, SCC devices, SC Express, SCXI devices, switches, timing I/O (TIO) dev

### NI-DAQmx Device Considerations

This help file contains information specific to analog output (AO) Series devices, B Series
 devices, C Series devices, digital I/O (DIO) devices, DSA devices, E Series devices,
 FieldDAQ Devices, M Series devices, S Series devices, SCC devices, SC Express, SCXI
 devices, switches, timing I/O (TIO) devices, USB DAQ devices, X Series, and NI mioDAQ devices that might help you as you create
 applications with NI-DAQmx.

<!--NI_TOPIC bundle=ni-daqmx path=device-routing.html language=enus -->
## TOPIC 00067: Device Routing in MAX

- bundle_id: `ni-daqmx`
- source_path: `device-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/device-routing.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: To find the device routing table for your device, launch MAX and select Devices and Interfaces. Click a device to open a tabbed window in the middle pane. Click the Device Routes tab at the bottom of the pane to display the device routing table. MAX does not display the device routing table for SCXI

### Device Routing in MAX

To find the device routing table for your device, launch MAX and select
 Devices and Interfaces. Click a device to open a tabbed
 window in the middle pane. Click the Device Routes tab at the bottom of the pane to
 display the device routing
 table.

Note

Each cell in the table is an index with the valid source terminal and destination terminal for
 the device. Destination terminal names are identical to the terminal names found in the
 Terminal Name I/O LabVIEW control.

Note

DAQmxConnectTerms

DAQmxDisconnectTerms

If a route is possible between a source and destination terminal, the intersecting cell is
 colored green or yellow. A green cell indicates the route can be made without consuming
 any important resource of your device. A yellow cell indicates that although the route
 is possible, something important must be consumed to create the route. Placing the
 cursor over a yellow square reveals the resource used in the subsystem
 used indicator. Usually, the sacrificed resource is a counter.

When you display the device routing table for a cDAQ chassis or a C Series device, the table
 contains all of the terminals for the chassis and all devices installed in the
 chassis.

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-daqmx path=devicecalibrationsignalconnections6614.html language=enus -->
## TOPIC 00068: Device Calibration Signal Connections for NI 6614

- bundle_id: `ni-daqmx`
- source_path: `devicecalibrationsignalconnections6614.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/devicecalibrationsignalconnections6614.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: For signal connections needed to externally calibrate your NI 6614, refer to the calibration procedure for the NI 6614.

### Device Calibration Signal Connections for NI 6614

For signal connections needed to externally calibrate your NI 6614, refer to the calibration procedure for the NI 6614.

Parent topic:

Signal Connections

<!--NI_TOPIC bundle=ni-daqmx path=devrange.html language=enus -->
## TOPIC 00069: Device Range

- bundle_id: `ni-daqmx`
- source_path: `devrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/devrange.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Device range refers to the minimum and maximum analog signal levels that the ADC can digitize. Many measurement devices can select from several ranges by changing from unipolar mode to bipolar mode or by selecting from multiple gains, allowing the ADC to take full advantage of its resolution to digi

### Device Range

Device range refers to the minimum and maximum analog signal levels that the ADC can digitize. Many measurement devices can select from several ranges by changing from unipolar mode to bipolar mode or by selecting from multiple gains, allowing the ADC to take full advantage of its resolution to digitize the signal.

Parent topic:

Sampling Considerations

Related concepts:

- Input Limits (Maximum and Minimum Values)
- Gain for DSA Devices

#### Unipolar and Bipolar Modes

Unipolar mode means that a device only supports a range of 0 V to +X V. Bipolar mode means that a device supports a range of -X V to +X V. Some devices support only one mode or the other, while other devices can change from unipolar mode to bipolar mode.

Devices that can change from unipolar to bipolar mode are able to select the mode that best fits the signal to measure. The first chart of the following figure illustrates unipolar mode for a 3-bit ADC. The ADC has eight digital divisions in the range from 0 to 10 V. In bipolar mode, the range is -10.00 to 10.00 V, as shown in the second chart. The same ADC now separates a 20 V range into eight divisions. The smallest detectable difference in voltage increases from 1.25 to 2.50 V, and you now have a much less accurate representation of the signal. The device selects the best mode available based on the input limits you specify when you create a virtual channel.

[IMAGE alt='image' src='GUID-ABAEE7CB-48B6-4452-A709-4C18C0F8B549-a5.svg']

#### Gain Adjustment

If a device has multiple gains, it multiplies an input signal by one of the gains to make the signal take up more of the full device range. This essentially gives the device multiple ranges it can select from. For example, a device with an overall range of -10 V to 10 V and possible gains of 1, 2, and 4 can select between ranges of -10 V to 10 V, -5 V to 5 V, and -2.5 V to 2.5 V. The device selects the best gain available according to the input limits you specify when you create a virtual channel.

Note

<!--NI_TOPIC bundle=ni-daqmx path=devresetrouting.html language=enus -->
## TOPIC 00070: Device Resetting and Interactions with Routing

- bundle_id: `ni-daqmx`
- source_path: `devresetrouting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/devresetrouting.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you reset a device in NI-DAQmx, every immediate route and task associated with the device is invalidated. When the task is invalidated, all the routes are invalidated, too. If a task-based route is invalidated using a device reset, its parent task also is invalidated. For instance, device A is

### Device Resetting and Interactions with Routing

When you reset a device in NI-DAQmx, every immediate route and task associated with the device is invalidated. When the task is invalidated, all the routes are invalidated, too. If a task-based route is invalidated using a device reset, its parent task also is invalidated.

For instance, device A is running a task that performs an analog input operation. This same analog input operation receives its Start Trigger from device B. This task spans across device A and B due to the multi-device routing. If device B gets reset, all routes on device B are destroyed. The invalidation of the task-based route on device B causes its parent task on device A to be invalidated, too. You must consider these possible consequences when issuing a device reset. If the route between device A and B is an immediate route, there is not a relationship between the immediate route and the task. This could result in the task not being invalidated. You need to decide if you need to preserve the task.

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-daqmx path=diffmeassys.html language=enus -->
## TOPIC 00071: Differential Measurement System

- bundle_id: `ni-daqmx`
- source_path: `diffmeassys.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/diffmeassys.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A differential measurement system has neither of its inputs tied to a fixed reference, such as earth or building ground. A differential measurement system is similar to a floating signal source in that the measurement is made with respect to a floating ground that is different from the measurement s

### Differential Measurement System

A differential measurement system has neither of its inputs tied to a fixed reference, such as earth or building ground. A differential measurement system is similar to a floating signal source in that the measurement is made with respect to a floating ground that is different from the measurement system ground. Hand-held, battery-powered instruments and DAQ devices with instrumentation amplifiers are examples of differential measurement systems.

The following figure shows an implementation of an 8-channel differential measurement system used in a typical NI device. Analog multiplexers are used in the signal path to increase the number of measurement channels when there is only a single instrumentation amplifier. For this device, the pin labeled AIGND, the analog input ground, is the measurement system ground.

[IMAGE alt='image' src='GUID-EE269C18-FB98-4C57-ACD6-98788FC138B6-a5.svg']

Your signal source—floating or grounded—helps determine if you should use a differential measurement system.

Parent topic:

Measurement System Types and Signal Sources

Related concepts:

- Floating Signal Sources
- Grounded Signal Sources

<!--NI_TOPIC bundle=ni-daqmx path=digfiltdio.html language=enus -->
## TOPIC 00072: Digital Filtering Considerations for DIO Devices

- bundle_id: `ni-daqmx`
- source_path: `digfiltdio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/digfiltdio.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital filtering is enabled by default on all isolated DIO devices that support digital filtering. The default minimum pulse width is 0.1 ms or 100 µs. Refer to the following table for a list of devices and their digital filtering settings. Digital Filtering Setting Devices Digital Filtering Enable

### Digital Filtering Considerations for DIO Devices

Digital filtering is enabled by default on all isolated DIO devices that support digital filtering. The default minimum pulse width is 0.1 ms or 100 µs. Refer to the following table for a list of devices and their digital filtering settings.

| Digital Filtering Setting | Devices |
| --- | --- |
| Digital Filtering Enabled by Default | PCI-6510 PCI-6511 PCI-6514 PCI-6515 PCI-6518 PCI-6519 PCI-6527 PCI-6528 PXI-6511 PXI-6514 PXI-6515 PXI-6527 PXI-6528 PXI-6529 USB-6525 |
| Digital Filtering Disabled by Default | PCI-6509 PCIe-6509 PXI-6509 PXIe-6509 |
| Digital Filtering Not Supported | PCI-6503 PCI-6512 PCI-6513 PCI-6516 PCI-6517 PCI-DIO-96 PXI-6508 PXI-6512 PXI-6513 USB-6501 |

Parent topic:

Digital Filtering

<!--NI_TOPIC bundle=ni-daqmx path=digfiltering.html language=enus -->
## TOPIC 00073: Digital Filtering

- bundle_id: `ni-daqmx`
- source_path: `digfiltering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/digfiltering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital filtering rejects state transitions that do not stay at a state for a specified amount of time. For example, for an edge counting measurement with digital filtering, the device does not count an edge if the pulse width is not at least the specified time. For digital input tasks, the device d

### Digital Filtering

Digital filtering rejects state transitions that do not stay at a state for a specified amount of time. For example, for an edge counting measurement with digital filtering, the device does not count an edge if the pulse width is not at least the specified time. For digital input tasks, the device does not recognize that a signal changed from one state to another unless the signal remains at that state for the specified amount of time.

This section contains information about digital filtering for C Series, DIO, M Series, SC Express, TIO, and X Series devices.

- [Digital Filtering Considerations for C Series Devices or or TestScale Modules](digfiltcseries.html#GUID-CA2C7D19-DC22-4281-A275-9E46D19E68A1)
- [Digital Filtering Considerations for DIO Devices](digfiltdio.html)
- [Digital Filtering Considerations for TIO-Based Devices](digfilttio.html)
- [Digital Filtering Considerations for X Series, NI 661x, and NI mioDAQ Devices](digfiltxseries.html)
- [Digital Filtering Considerations for SC Express Devices](scexpressdigfilt.html)
- [FieldDAQ Filtering](fieldaq-filtering.html)
- [NI 9202, NI 9252, and NI 9253 Filtering](ni-9202-filtering.html)

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=digfilttio.html language=enus -->
## TOPIC 00074: Digital Filtering Considerations for TIO-Based Devices

- bundle_id: `ni-daqmx`
- source_path: `digfilttio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/digfilttio.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: For digital filtering with NI 661x devices, refer to Digital Filtering Considerations for X Series and NI 661x Devices. There are two methods for filtering and synchronizing digital signals. One method is to synchronize the input signal to the maximum onboard timebase on the device. To do this, set

### Digital Filtering Considerations for TIO-Based Devices

Note

x

Digital Filtering Considerations for X Series and NI 661x Devices.

There are two methods for filtering and synchronizing digital signals. One method is to synchronize the input signal to the maximum onboard timebase on the device. To do this, set Digital Synchronization Enable to true.

The other method is to pass the input of any PFI line through a digital debouncing filter. Each PFI line can independently select from four fixed values (5 µs, 1 µs, 500 ns, 100 ns) and one custom filter value. The custom filter value must be the same for each PFI line. That is, if you choose a filter value of 2 µs for a PFI line, other PFI lines on the device at the same time can only choose from the four fixed values and the 2 µs value selected as the custom filter value. For each counter input property, there are four attributes/properties associated with digital debounce filtering: Digital Filter Enable, Digital Filter Minimum Pulse Width, Digital Filter Timebase Source, and Digital Filter Timebase Rate.

When you set the Digital Filter Enable to true, you must also configure the Digital Filter Minimum Pulse Width attribute/property. This value represents the minimum value that is guaranteed to pass into the TIO. The minimum pulse width guaranteed to be blocked is one-half of the Digital Filter Minimum Pulse Width attribute/property. When you select a custom filter value with the Minimum Pulse Width attribute/property, NI-DAQmx uses an internal 32-bit utility counter to generate the desired filter value. If you would like to generate the filter clock using your own external signal, you can use the Digital Filter Timebase Source and Digital Filter Timebase Rate attributes/properties. You must configure both to use an external signal as the source for the digital filter.

You cannot set both Digital Filter Enable and Digital Synchronization Enable to true at the same time. You can use only one of these digital filtering methods at a time.

The following table lists the counter input terminals that can be digitally filtered.

| Type | Attribute/Property |
| --- | --- |
| Channel | Frequency Input Terminal |
| Period Input Terminal |  |
| Count Edges Input Terminal |  |
| Count Edges Count Direction |  |
| Position A Input Terminal |  |
| Position B Input Terminal |  |
| Position Z Input Terminal |  |
| Pulse Width Input Terminal |  |
| Two-Edge First Input Terminal |  |
| Two-Edge Second Input Terminal |  |
| Semi-Period Input Terminal |  |
| Counter Input Timebase Source |  |
| Counter Output Timebase Source |  |
| Timing | Sample Clock Source |
| Triggering | Start Trigger Source |
| Pause Trigger Source |  |
| Arm Start Trigger Source |  |

Parent topic:

Digital Filtering

<!--NI_TOPIC bundle=ni-daqmx path=edge-counting-programming-flowchart.html language=enus -->
## TOPIC 00075: Edge Counting Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `edge-counting-programming-flowchart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/edge-counting-programming-flowchart.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps you must complete for counting edges in an NI-DAQmx application. If you prefer, you can configure a task for counting edges using the DAQ Assistant.Edge counting is an example of a counter measurement. Refer to Counter Programming Flowcharts for additio

### Edge Counting Programming Flowchart

The following flowchart depicts the main steps you must complete for counting edges in an NI-DAQmx application. If you prefer, you can configure a task for counting edges using the DAQ Assistant.

[IMAGE alt='image' src='GUID-95354FB9-3354-44CC-A775-E3B7CE42E31B-a5.gif']

Edge counting is an example of a counter measurement. Refer to Counter Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Edge Counting

Related concepts:

- Counter Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=elvisinternalchannels.html language=enus -->
## TOPIC 00076: Internal Channels for NI ELVIS II Family

- bundle_id: `ni-daqmx`
- source_path: `elvisinternalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/elvisinternalchannels.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Internal Channel Name Description _aignd_vs_aignd A differential terminal with the positive and negative terminals both connected to the ground reference for analog input. _ao0_vs_aognd A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal con

### Internal Channels for NI ELVIS II Family

| Internal Channel Name | Description |
| --- | --- |
| _aignd_vs_aignd | A differential terminal with the positive and negative terminals both connected to the ground reference for analog input. |
| _ao0_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal connected to the ground reference for analog output. |
| _ao1_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao1 and the negative terminal connected to the ground reference for analog output. |
| _calref_vs_aignd | A differential terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the ground reference for analog input. |
| _aignd_vs_aisense | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE. |
| _aignd_vs_aisense2 | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE2. |
| _calSrcHi_vs_aignd | A differential terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. |
| _calref_vs_calSrcHi | A differential terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the calibration PWM. |
| _calSrcHi_vs_calSrcHi | A differential terminal with the positive and negative terminals connected to the calibration PWM. |
| _aignd_vs_calSrcHi | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to the calibration PWM. |
| _calSrcMid_vs_aignd | A differential terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. _calSrcMid is the divided down version of _calSrcHi. |
| _calSrcLo_vs_aignd | A differential terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. _calSrcLo is the divided down version of _calSrcHi. |
| _ai0_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ai0 and the negative terminal connected to the calibration PWM. |
| _ai8_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ai8 and the negative terminal connected to the calibration PWM. |
| _boardTempSensor_vs_aignd | A differential terminal with the positive terminal connected to the onboard temperature sensor and the negative terminal connected to the ground reference for analog input.. |
| _ai16:31 | A differential or RSE terminal used to access internally connected AI terminals. |
| _vpsPosCurrent | A differential terminal connected to the shunt resistor on the variable power supply. |
| _vpsNegCurrent | A differential terminal connected to the shunt resistor on the variable power supply. |
| _vpsPos_vs_gnd | A differential terminal connected to a voltage divider on the variable power supply. |
| _vpsNeg_vs_gnd | A differential terminal connected to a voltage divider on the variable power supply. |
| _dutNeg | Reads the voltage equivalent of Current into the DUT- pin. |
| _base | Reads the voltage at the base pin (base voltage for 3-wire analyzer). |
| _dutPos | Reads the voltage at the DUT+ pin. |
| _fgenImpedance | Internally routes the function generator to the impedance analyzer circuit. |
| _ao0Impedance | Internally routes AO 0 to the impedance analyzer for Three-Wire Current-Voltage Analyzer measurements. |

Parent topic:

Internal Channels

<!--NI_TOPIC bundle=ni-daqmx path=elvisphyschanns.html language=enus -->
## TOPIC 00077: NI ELVIS II Family Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `elvisphyschanns.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/elvisphyschanns.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In physical channel names, Dev1 is the default device name for the NI ELVIS II Family device. You can change these names in MAX. Analog Input NI ELVIS II Family devices have 16 analog input channels, ranging from Dev1/ai0 to Dev1/ai15. You can configure the first eight channels as the positive chann

### NI ELVIS II Family Physical Channels

In physical channel names, 
 Dev1 is the default device name for the NI ELVIS II Family device. You can change these names in MAX.

Parent topic:

Physical Channels

Related reference:

- NI ELVIS II Family Signal Connections for Counters

#### Analog Input

NI ELVIS II Family devices have 16 analog input channels, ranging from 
 Dev1/ai0 to 
 Dev1/ai15. You can configure the first eight channels as the positive channel of a differential pair. If 
 N is this channel, channel 
 N + 8 is the negative input of the pair. For instance, if you configure channel 1 in differential mode, the positive input is channel 1, and channel 9 is the negative input.

Use only the physical channel name of the positive channel (not both) when creating a differential channel.

NI ELVIS II Family devices have two oscilloscope physical channels, 
 Dev1/scopeCh0 and 
 Dev1/scopeCh1, available from the NI ELVIS II Family benchtop workstation. The NI ELVIS II Family benchtop workstation also has a DMM physical channel, 
 Dev1/dmm. On the NI ELVIS II Family devices, the DMM and oscilloscope physical channels cannot be used in the same task with other channels. However, scopeCh0 and scopeCh1 can be used together.

#### Analog Output

NI ELVIS II Family devices have two analog outputs with analog output physical channels named 
 Dev1/ao0 and 
 Dev1/ao1. NI ELVIS II Family devices also have two function generator channels, 
 Dev1/fgen and 
 Dev1/fgenBNC, and two variable power supply channels, 
 Dev1/vpsPos (the positive variable power supply) and 
 Dev1/vpsNeg (the negative variable power supply). The function generator channels, 
 Dev1/fgen and 
 Dev1/fgenBNC, use the FGEN Create Channel function/VI. These function generator terminals also share the same resource.

#### Digital Input and Output

NI ELVIS II Family devices have 24 lines of digital input and output named 
 Dev1/port0/line0 through 
 Dev1/port0/line23. These lines belong to a single port, and the physical channel 
 Dev1/port0 refers to all 24 lines at once. Port 0 can perform static digital operations.

NI ELVIS II Family devices have two more ports, port 1 and port 2. Port 1 has eight digital I/O lines, 
 Dev1/port1/line0 through 
 Dev1/port1/line7. Port 2 has seven digital I/O lines, 
 Dev1/port2/line0 through 
 Dev1/port2/line6. Port 1 and port 2 can be used as static digital I/O lines or PFI lines, PFI 0..14. When any of PFI lines 0..14 is used as a digital I/O signal, it uses the physical channel name shown in the following table.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | Dev1/port1/line0 |
| PFI 1 | Dev1/port1/line1 |
| PFI 2 | Dev1/port1/line2 |
| PFI 3 | Dev1/port1/line3 |
| PFI 4 | Dev1/port1/line4 |
| PFI 5 | Dev1/port1/line5 |
| PFI 6 | Dev1/port1/line6 |
| PFI 7 | Dev1/port1/line7 |
| PFI 8 | Dev1/port2/line0 |
| PFI 9 | Dev1/port2/line1 |
| PFI 10 | Dev1/port2/line2 |
| PFI 11 | Dev1/port2/line3 |
| PFI 12 | Dev1/port2/line4 |
| PFI 13 | Dev1/port2/line5 |
| PFI 14 | Dev1/port2/line6 |

Physical channel Dev1/port1 refers to all eight lines, 
 Dev1/port1/line0:7, at once. Physical channel Dev1/port2 refers to all seven lines, 
 Dev1/port2/line0:6, at once.

#### Counter Input and Output

NI ELVIS II Family devices have two counter/timers referred to by the physical channel names 
 Dev1/ctr0 and 
 Dev1/ctr1. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device. There are four primary terminals associated with each counter. These are the terminals used as the SOURCE, GATE, AUX, and OUT functions. NI-DAQmx has default values for these terminals. For counter input tasks, if you know whether your signal provides the SOURCE, AUX, or GATE function and wire your signal to the default, you do not have to set the Input Terminal attribute/property.

| Counter | SOURCE Default | GATE Default | AUX Default | OUT Default |
| --- | --- | --- | --- | --- |
| Dev1/ctr0 | PFI 8 | PFI 9 | PFI 10 | PFI 12 |
| Dev1/ctr1 | PFI 3 | PFI 4 | PFI 11 | PFI 13 |

Note

dev1/fgenBNC

<!--NI_TOPIC bundle=ni-daqmx path=encoders.html language=enus -->
## TOPIC 00078: Encoders

- bundle_id: `ni-daqmx`
- source_path: `encoders.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/encoders.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are two common types of encoders used for measuring position: two-pulse encoders and quadrature encoders.

### Encoders

There are two common types of encoders used for measuring position: two-pulse encoders and quadrature encoders.

Parent topic:

Common Sensors

Related concepts:

- Two-Pulse Encoders
- Quadrature Encoders

<!--NI_TOPIC bundle=ni-daqmx path=enhancedaliasrej.html language=enus -->
## TOPIC 00079: Enhanced Alias Rejection

- bundle_id: `ni-daqmx`
- source_path: `enhancedaliasrej.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/enhancedaliasrej.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: To avoid aliasing at low sample rates, some DSA devices support enhanced alias rejection. With enhanced alias rejection enabled, the device clocks the ADCs at a multiple of the user-specified sample rate. This results in an improvement in low-frequency alias rejection. With enhanced alias rejection

### Enhanced Alias Rejection

To avoid aliasing at low sample rates, some DSA devices support enhanced alias rejection. With enhanced alias rejection enabled, the device clocks the ADCs at a multiple of the user-specified sample rate. This results in an improvement in low-frequency alias rejection. With enhanced alias rejection enabled, you do not need to scale the desired sample rate, and you do not need to programmatically decimate data the device returns.

Enhanced alias rejection is controlled with the AI.EnhancedAliasRejectionEnable attribute/property. Enhanced alias rejection is enabled by default on NI 4461/4462 devices and disabled by default on NI 447x and NI 449x devices.

Note

x

Dynamic Signal Acquisition Help

Parent topic:

Alias Rejection (DSA, C Series, and NI 433x)

Related concepts:

- Alias Rejection at Low Sample Rates (DSA, C Series, and NI 4330/1)

#### Synchronization Issues

When synchronizing multiple devices, set the AI.EnhancedAliasRejectionEnable attribute/property to the same value on all devices. If any of the synchronized devices do not support enhanced alias rejection, set AI.EnhancedAliasRejectionEnable to FALSE on all devices. When synchronizing devices from different categories, NI 4461/4462 with NI 447x for example, set AI.EnhancedAliasRejectionEnable to FALSE on all devices.

<!--NI_TOPIC bundle=ni-daqmx path=eseriesphyschans.html language=enus -->
## TOPIC 00080: E Series Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `eseriesphyschans.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/eseriesphyschans.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dev1 in physical channel names is the default device name for E Series devices. You can change these names in MAX. Analog Input A 16-channel E Series device has physical channels ranging from Dev1/ai0 to Dev1/ai15. You can configure only channels 0 through 7 in differential mode. When you configure

### E Series Physical Channels

Dev1 in physical channel names is the default device name for E Series devices. You can change these names in MAX.

Parent topic:

Physical Channels

Related reference:

- AO Series, E Series, and S Series Signal Connections for Counters

#### Analog Input

A 16-channel E Series device has physical channels ranging from 
 Dev1/ai0 to 
 Dev1/ai15. You can configure only channels 0 through 7 in differential mode. When you configure a channel in differential mode, the channel is the positive input and channel plus eight is the negative input. For instance, if you configure channel 1 in differential mode, the positive input is channel 1, and channel 9 is the negative input.

A 64-channel E Series device has physical channels ranging from 
 Dev1/ai0 to 
 Dev1/ai63. You can configure channels in banks of every other eight beginning with 0 through 7 as the positive channel of a differential pair (0-7, 16-23, 32-39, and 48-55). If 
 N is this channel, channel 
 N + 8 is the negative input of the pair.

Use only the physical channel name of the positive channel when creating a differential channel (not both).

#### Analog Output

An E Series device that supports analog output has two analog output physical channels named 
 Dev1/ao0 and 
 Dev1/ao1.

#### Digital Input and Output

All E Series devices except the NI 6025E have eight lines of digital input and output named 
 Dev1/port0/line0 through 
 Dev1/port0/line7. These lines belong to a single port, and the physical channel Dev1/port0 refers to all eight lines at once.

The NI 6025E has 32 lines of digital input and output with eight lines belonging to one of four ports. The names are of the form 
 Dev1/portP/line0 through 
 Dev1/portP/line7, where 
 P ranges from 0 through 3. There are also four physical channel names that refer to all eight lines in a port at once of the form 
 Dev1/portP, where 
 P ranges from 0 through 3. There are two more physical channel names that refer to all the lines in multiple consecutive ports. They are both of the form 
 Dev1/portP_N, where 
 P is the port number of the lowest numbered port, and 
 N is the total number of lines. All 32 lines at once can be configured as a single virtual channel with the physical channel name 
 Dev1/port0_32. You can configure the two ports that can be handshaked as a single virtual channel by using the physical channel name 
 Dev1/port1_16.

#### Counter Input and Output

All E Series devices have two counter/timers referred to by the physical channel names 
 Dev1/ctr0 and 
 Dev1/ctr1. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device. There are three primary terminals associated with each counter. These are the terminals used as the SOURCE, GATE and OUT functions. NI-DAQmx has default values for these terminals. For counter input tasks, if you know whether your signal provides the SOURCE or GATE function and wire your signal to the default, you do not have to set the Input Terminal attribute/property.

| Counter | SOURCE Default | GATE Default | OUT Default |
| --- | --- | --- | --- |
| Dev1/ctr0 | PFI 8 | PFI 9 | CTR 0 OUT |
| Dev/ctr1 | PFI 3 | PFI 4 | CTR 1 OUT |

<!--NI_TOPIC bundle=ni-daqmx path=eseriessigcounters.html language=enus -->
## TOPIC 00081: AO Series, E Series, and S Series Signal Connections for Counters

- bundle_id: `ni-daqmx`
- source_path: `eseriessigcounters.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/eseriessigcounters.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals, with the exception of the count direction terminal for edge counting. To change the PFI input for a measurement, use the NI-DAQmx channel attribute

### AO Series, E Series, and S Series Signal Connections for Counters

The following table lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals, with the exception of the count direction terminal for edge counting. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties.

| Measurement | Ctr0 | Ctr1 |
| --- | --- | --- |
| Count Edges | Edges: PFI 8 Count Direction[1]1 The count direction terminal must be tristated to use an external signal. Reset the device to ensure the terminal is tristated: port0/line6 | Edges: PFI 3 Count Direction[1]: port0/line7 |
| Pulse Width Measurement | PFI 9 | PFI 4 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 9 | PFI 4 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 8 | PFI 3 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 8 | PFI 3 |
| Semiperiod Measurement | PFI 9 | PFI 4 |

The following table lists the default output terminals for counter output. You must use the default output terminal, with the exception that for Ctr0, you can select a RTSI line.

| Ctr0 | Ctr1 |
| --- | --- |
| CTR 0 OUT | CTR 1 OUT |

Parent topic:

Connecting Counter Signals

<sup>1</sup> The count direction terminal must be tristated to use an external signal. Reset the device to ensure the terminal is tristated

<!--NI_TOPIC bundle=ni-daqmx path=event-response.html language=enus -->
## TOPIC 00082: Event Response

- bundle_id: `ni-daqmx`
- source_path: `event-response.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/event-response.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a control application, an event is the same as an occurrence. This occurrence leads to an action, or a response. An example is monitoring the temperature of an engine. When the temperature rises too high, the engine slows down. The event, in this case, would be the temperature rising above a pred

### Event Response

In a control application, an event is the same as an occurrence. This occurrence leads to an action, or a response. An example is monitoring the temperature of an engine. When the temperature rises too high, the engine slows down. The event, in this case, would be the temperature rising above a predetermined level, and the response would be the engine slowing down. Another example comes from manufacturing. In a manufacturing line, a system senses when a part is in front of a station (the event) and takes a reading or manipulates the part (the response). If the system does not sense and respond to the presence of that part in a set amount of time, the manufacturing line creates defective parts.

When creating an event response application, make sure you consider the amount of time needed to respond to the event. For example, if the device controls the temperature of your home, the time to react to events (changes in temperature) is less critical than if the device controls a nuclear reactor. If the application is not time critical, the application does not need to be deterministic, meaning that you do not need the LabVIEW Real-Time Module or a real-time controller.

The relative priority of the task is important as well. Because LabVIEW is multi-threaded, you can separate the application into tasks, each with its own priority. By setting priorities, time-critical tasks can take precedence over non-time-critical tasks. The time-critical task must periodically yield processor resources to the lower-priority tasks so they can execute. By properly separating the time-critical task from lower priority tasks, you can reduce application jitter. Refer to the LabVIEW Real-Time Module Concepts book in the LabVIEW Help for more information about assigning priorities to tasks.

Parent topic:

Control

Related concepts:

- Finding Examples

<!--NI_TOPIC bundle=ni-daqmx path=events.html language=enus -->
## TOPIC 00083: Events

- bundle_id: `ni-daqmx`
- source_path: `events.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/events.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Triggers and clocks are input signals. Exportable triggers and clocks, such as the sample clock, also can be output signals. Output signals that do not have a trigger or clock counterpart are called events. Events are emitted to signify a device state change, the arrival of a certain kind of sample,

### Events

Triggers and clocks are input signals. Exportable triggers and clocks, such as the sample clock, also can be output signals. Output signals that do not have a trigger or clock counterpart are called events. Events are emitted to signify a device state change, the arrival of a certain kind of sample, the production of a certain amount of samples, or the passage of time.

NI-DAQmx includes the following events:

Advance Complete Event

AI Hold Complete Event

Change Detection Event

Counter Output Event

Handshake Event

Ready For Start Event

Ready For Transfer Event

Sample Complete Event

Watchdog Timer Expired Event

Note

Note

Parent topic:

Timing and Triggering

Related concepts:

- Handshake Trigger
- Start Trigger

Related reference:

- Burst Handshake Timing for Digital I/O

<!--NI_TOPIC bundle=ni-daqmx path=excitationfaultdetection.html language=enus -->
## TOPIC 00084: Excitation Fault Detection

- bundle_id: `ni-daqmx`
- source_path: `excitationfaultdetection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/excitationfaultdetection.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Two NI-DAQmx Read attributes/properties allow you to check for excitation faults. The first is ExcitFaultChansExist. This attribute/property returns a Boolean of true if one or more channels experience an excitation fault condition. The second is ExcitFaultChans. This attribute/property returns an a

### Excitation Fault Detection

Two NI-DAQmx Read attributes/properties allow you to check for excitation faults. The first is ExcitFaultChansExist. This attribute/property returns a Boolean of true if one or more channels experience an excitation fault condition. The second is ExcitFaultChans. This attribute/property returns an array of strings indicating which channels (if any) experienced an excitation fault condition. You must query the ExcitFaultChansExist attribute/property before querying the ExcitFaultChans attribute/property.

ExcitFaultChansExist reads the excitation fault condition from the device and stores it in NI-DAQmx. Subsequent reads of ExcitFaultChans will read the excitation fault channel information stored in NI-DAQmx from the previous ExcitFaultChansExist query.

NI-DAQmx returns all data regardless of whether an excitation fault happens. If your application needs excitation fault checking, you should read the excitation fault attributes/properties after each call to read. Your program should discard questionable data or return a flag when NI-DAQmx reports an excitation fault.

The NI 9218 can detect if there is an overcurrent fault between EX+ and EX- pins of either channel for either the strain mode case or the powered sensor measurement case. When the NI 9218 is configured for powered sensor measurement, which requires a +12 V excitation, it can also detect the absence of the required 9-30 V external power supply connected to the Vsup terminal. Both of these types of faults are reported as excitation faults.

The PXIe-4340 can detect if there is an overcurrent fault between the EX+ and EX- pins of any channel. This fault occurs when a voltage source is connected to the EX+ and EX- pins of any channel, or the load impedance is too low (excessive current). Ensure that only the primary winding of an LVDT/RVDT sensor is connected to the EX+ and EX- pins of any channel on this module.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=expirationtrigger.html language=enus -->
## TOPIC 00085: Expiration Trigger

- bundle_id: `ni-daqmx`
- source_path: `expirationtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/expirationtrigger.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: An Expiration Trigger expires a watchdog task. You can use this trigger instead of the watchdog timer to signal an expiration. You can configure this trigger to occur on a digital edge.

### Expiration Trigger

An Expiration Trigger expires a watchdog task. You can use this trigger instead of the watchdog timer to signal an expiration. You can configure this trigger to occur on a digital edge.

Parent topic:

Triggering

Related concepts:

- Watchdog Timers

<!--NI_TOPIC bundle=ni-daqmx path=explicitimplicitstates.html language=enus -->
## TOPIC 00086: Explicit Versus Implicit State Transitions

- bundle_id: `ni-daqmx`
- source_path: `explicitimplicitstates.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/explicitimplicitstates.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In some scenarios, the user performs explicit state transitions. Other times, the user should rely on the task to perform implicit state transitions. Which method you use depends on your application. The following list identifies instances that require explicit state transitions: Verify Some applica

### Explicit Versus Implicit State Transitions

In some scenarios, the user performs explicit state transitions. Other times, the user should
 rely on the task to perform implicit state transitions. Which method you use depends on
 your application. The following list identifies instances that require explicit state
 transitions:

Verify

Reserve

- Your application contains many different tasks that use the same set of
 resources.
- One of these tasks performs a repeated operation.
- You want to ensure that no other tasks acquire the resources used by
 this task after the repeated operation begins.

Commit

Using
 the Start Task Function/VI

Start

- Reserves the resources used by the task.
- Programs some of the settings for these resources.
- Begins to perform the specified operation.

Parent topic:

Task State Model

Related concepts:

- Using the Start Task function/VI

<!--NI_TOPIC bundle=ni-daqmx path=extended-support-changes.html language=enus -->
## TOPIC 00087: Updates and Changes for NI-DAQmx Extended Support Versions

- bundle_id: `ni-daqmx`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/extended-support-changes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-DAQmx versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible changes

### Updates and Changes for NI-DAQmx Extended Support Versions

Browse updates and changes made in NI-DAQmx versions
 on extended support.

Note

Release Notes

#### NI-DAQmx
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx
 2024 Q4.

##### New
 Hardware Support

NI-DAQmx

NI mioDAQ

- USB-6421 (OEM)
- USB-6423 (OEM)
- USB-6451 (OEM)
- USB-6453 (OEM)

This version of NI-DAQmx also provides support
 for the following hardware:

- NI-9204
- cDAQ-9183
- cDAQ-9187

#### NI-DAQmx 2024 Q3.1 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx 2024
 Q3.1.

##### New
 Features

- USB-6421
- USB-6423
- USB-6451
- USB-6453

#### NI-DAQmx 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx 2024
 Q3.

##### Behavior Changes

- Support for VB6 has been removed.

#### NI-DAQmx 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx 2024
 Q2.

##### Behavior
 Changes

NI-DAQmx support for VB6 is expected to be removed in NI-DAQmx 2024 Q3.
 NI-DAQmx 2024 Q2 will be the last release to support VB6.

#### NI-DAQmx 2022 Q4 Changes

Learn about new features, behavior changes, and other updates in DAQmx 2022
 Q4.

##### New Features

- TS-15050 DIO P0
- TS-15100
- TS-15110
- TS-15120
- TS-15130
- TS-15200

<!--NI_TOPIC bundle=ni-daqmx path=extrefsource.html language=enus -->
## TOPIC 00088: External Reference Sources for Generating Voltage

- bundle_id: `ni-daqmx`
- source_path: `extrefsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/extrefsource.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Devices that support an external voltage reference enable you to maximize the resolution of your device. If the voltages you want to generate do not exceed a certain level and you can supply an external reference voltage at that level, you achieve your device's maximum resolution. The external refer

### External Reference Sources for Generating Voltage

Devices that support an external voltage reference enable you to maximize the resolution
 of your device. If the voltages you want to generate do not exceed a certain level and
 you can supply an external reference voltage at that level, you achieve your device's
 maximum resolution. The external reference voltage settings are available as a Channel
 property in the Analog Output»General Properties»DAC»Reference
 Voltage.

You also can use external reference voltages to apply a gain to a DC voltage or to a
 time-varying waveform. For example, set your external reference voltage level to 1.0,
 and write a sine wave buffer with values from -1.0 to +1.0 V. When you apply an actual
 reference voltage of 2.0 V, your signal jumps to ±2 V in amplitude. Increasing the
 reference voltage level to 3.0 again jumps the signal to ±3 V. Applying a reference
 voltage level of 0.0 V immediately flat-lines your time-varying voltage signal at 0.0 V.

The terminal you use for external reference sources varies depending on your device.

#### AO Reference and Offset Support for PXIe-6381/6383
 (X Series)

For PXIe‑6381 and PXIe‑6383, analog output channels support
 both Reference and Offset selection (similar to M‑Series AO behavior). Use the
 NI‑DAQmx AO Reference and AO Offset properties to configure these options. Refer to
 the device specifications for supported ranges.

Parent topic:

NI-DAQmx Key Concepts

Related concepts:

- External Reference Sources

<!--NI_TOPIC bundle=ni-daqmx path=fd-11637-signal-conditioning.html language=enus -->
## TOPIC 00089: FD-11637 Signal Conditioning

- bundle_id: `ni-daqmx`
- source_path: `fd-11637-signal-conditioning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/fd-11637-signal-conditioning.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about excitation, quarter-bridge completion, and shunt calibration for the FD-11637. Excitation The FD-11637 supports internal excitation at 3 V, 5 V, and 10 V. 10 V excitation is only supported in Full-Bridge and Half-Bridge modes. Quarter-Bridge Completion The FD-11637 supports internal quar

### FD-11637 Signal Conditioning

Learn about excitation, quarter-bridge completion, and shunt calibration for the FD-11637.

#### Excitation

The FD-11637 supports internal excitation at 3 V, 5 V, and 10 V. 10 V excitation is only supported in Full-Bridge and Half-Bridge modes.

#### Quarter-Bridge Completion

The FD-11637 supports internal quarter-bridge completion with resistances of 120 Ω and 350 Ω.

#### Shunt Calibration

The FD-11637 has a built-in resistor for shunt calibration. Shunt calibration also only works in Quarter-Bridge mode.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=fieldaq-filtering.html language=enus -->
## TOPIC 00090: FieldDAQ Filtering

- bundle_id: `ni-daqmx`
- source_path: `fieldaq-filtering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/fieldaq-filtering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FD-11601, FD-11603, FD-11605, FD-11634, and FD-11637 can use filtering to provide an accurate representation of in-band signals while rejecting out-of-band signals. The filters discriminate between signals based on the frequency range, or bandwidth, of the signal. Use the AI.Filter.Enable DAQmx

### FieldDAQ Filtering

The FD-11601, FD-11603, FD-11605, FD-11634, and FD-11637 can use filtering to provide an accurate representation of in-band signals while rejecting out-of-band signals. The filters discriminate between signals based on the frequency range, or bandwidth, of the signal. Use the AI.Filter.Enable DAQmx Channel property to enable or disable a filter. You can then specify the center or cutoff frequency (AI.Filter.Freq), the filter order (AI.Filter.Order), and choose a Brickwall, Butterworth, or Comb filter response (AI.Filter.Response). The filter selection applies to all channels on a bank.

Refer to your device user guide for additional information on filtering.

Parent topic:

Digital Filtering

<!--NI_TOPIC bundle=ni-daqmx path=fielddaqcalibration.html language=enus -->
## TOPIC 00091: FieldDAQ Calibration

- bundle_id: `ni-daqmx`
- source_path: `fielddaqcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/fielddaqcalibration.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: FieldDAQ devices use software calibration to adjust the software scaling of signals read from and produced by your device. Using a precise reference signal, your device measures and calculates scaling constants for analog input. The scaling constants are stored in nonvolatile memory (EEPROM) on your

### FieldDAQ Calibration

FieldDAQ devices use software calibration to adjust the software scaling of signals read from and produced by your device. Using a precise reference signal, your device measures and calculates scaling constants for analog input. The scaling constants are stored in nonvolatile memory (EEPROM) on your device. Frequent calibration produces the most stable and repeatable measurement performance. The device is not harmed in any way if you recalibrate it often.

Note

- Calibrating your device takes some time. Do not be alarmed if the Adjust FieldDAQ Calibration function/VI takes several seconds to execute.
- For best results, stop any ongoing tasks and disconnect any unnecessary external connections before running calibration.

FieldDAQ devices do not self-calibrate or automatically calibrate. You must use a manual procedure to calibrate these devices.

FieldDAQ devices include the FD-11601, FD-11603,
 FD-11605, FD-11613, FD-11614, FD-11634, and FD-11637.

Parent topic:

Device Calibration Considerations

Related information:

- Calibration Procedures

<!--NI_TOPIC bundle=ni-daqmx path=handdefault.html language=enus -->
## TOPIC 00092: Handshake Timing Defaults

- bundle_id: `ni-daqmx`
- source_path: `handdefault.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/handdefault.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the default terminals used for handshake timing for NI 653x devices. The NI 6533 and NI 6534 have two timing engines, Timing Engine 1 and Timing Engine 0. Each timing engine is associated with PFI lines. The timing engine you use is determined by the digital lines you use.

### Handshake Timing Defaults

The following table lists the default terminals used for handshake timing for NI 653x devices.

Note

| Device | Handshake Trigger Source Terminal Default | Handshake Event Output Terminal Default |
| --- | --- | --- |
| PCI-6533 (DIO-32HS), PXI-6533, PCI-6534, PXI-6534 | PFI 2 (Timing Engine 0), PFI 3 (Timing Engine 1) | PFI 6 (Timing Engine 0), PFI 7 (Timing Engine 1) |
| PCIe-6535, PXIe-6535, PCIe-6536, PXIe-6536, PCIe-6537, PXIe-6537 | PFI 0 | PFI 1 |

The recommended sample clock terminal for burst handshake timing is PFI 4 (Timing Engine 0) or PFI 5 (Timing Engine 1).

Parent topic:

Digital I/O

<!--NI_TOPIC bundle=ni-daqmx path=handshake8255.html language=enus -->
## TOPIC 00093: Handshaking Signals for 8255-Based Devices

- bundle_id: `ni-daqmx`
- source_path: `handshake8255.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/handshake8255.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: 8255-based devices that perform handshaking support four handshaking signals: Strobe Input (STB) Input Buffer Full (IBF) Output Buffer Full (OBF) Acknowledge Input (ACK) Use the STB and IBF signals for digital input operations and the OBF and ACK signals for digital output operations. When the STB l

### Handshaking Signals for 8255-Based Devices

8255-based devices that perform handshaking support four handshaking signals:

- Strobe Input (STB)
- Input Buffer Full (IBF)
- Output Buffer Full (OBF)
- Acknowledge Input (ACK)

Use the STB and IBF signals for digital input operations and the OBF and ACK signals for digital output operations. When the STB line is low, the samples are sent to the measurement device. After the samples have been sent, IBF is high, which tells the peripheral device that the data has been read. For digital output, OBF is low while the software sends the samples to a peripheral device. After the peripheral device receives the samples, it sends a low pulse back on the ACK line. Refer to your device documentation to determine which digital ports you can configure for handshaking signals.

Parent topic:

Handshaking

#### Digital Data on Multiple Ports

For 8255-based devices, the ports in the task affect which handshaking lines are used. Always use the handshaking lines associated with the highest order port in the task. For instance, if you want to group ports 1 and 2 into a single task, use the handshaking lines associated with port 2.

Connect all the STB lines together if you are grouping ports for digital input, as shown in the following figure. Connect only the IBF line of the highest order port in the task to the other device. No connection is needed for the IBF signals for the other ports.

[IMAGE alt='image' src='GUID-48B26813-F075-48DD-9D87-DB6C3A021AB6-a5.svg']

If you group ports for digital output on an 8255-based device, connect only the handshaking signals of the last port in the port list, as shown in the following figure.

[IMAGE alt='image' src='GUID-FB08F081-8660-4448-A7FD-8DC8FAE1C677-a5.svg']

When performing handshaking, some lines are automatically reserved for control purposes and are unavailable for use. The control lines used depend on the ports you are using and whether you are handshaking with input or output channels. The remaining lines in the port not used for control are still available for use. If you are transferring data across any line in a port in a handshaking task, the entire port is reserved for handshaking data and the remaining lines in the port are unavailable for use.

<!--NI_TOPIC bundle=ni-daqmx path=hardwareids.html language=enus -->
## TOPIC 00094: Supported Device ID Numbers

- bundle_id: `ni-daqmx`
- source_path: `hardwareids.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/hardwareids.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Find the ID for your supported device. For information about which versions of NI-DAQmx support your device, go to ni.com/info and enter rdsoftwareversion. 7 Supported device ID numbers Device ID Device name 0x0160 PCI-DIO-96 0x075C DAQCard-DIO-24 0x075F DAQCard-6715 0x1150 PCI-DIO-32HS 0x1290 PCI-6

### Supported Device ID Numbers

Find the ID for your supported device.

For information about which versions of NI-DAQmx support your device, go to
 ni.com/info and enter rdsoftwareversion.

| Device ID | Device name |
| --- | --- |
| 0x0160 | PCI-DIO-96 |
| 0x075C | DAQCard-DIO-24 |
| 0x075F | DAQCard-6715 |
| 0x1150 | PCI-DIO-32HS |
| 0x1290 | PCI-6704 |
| 0x12B0 | PCI-6534 |
| 0x1310 | PCI-6602 |
| 0x1320 | PXI-6533 |
| 0x1360 | PXI-6602 |
| 0x13C0 | PXI-6508 |
| 0x1490 | PXI-6534 |
| 0x14E0 | PCI-6110 |
| 0x14F0 | PCI-6111 |
| 0x1710 | PXI-6509 |
| 0x17D0 | PCI-6503 |
| 0x1870 | PCI-6713 |
| 0x1880 | PCI-6711 |
| 0x1920 | PXI-6704 |
| 0x1AD0 | PCI-6133 |
| 0x1AE0 | PXI-6133 |
| 0x1E30 | PCI-6624 |
| 0x1E40 | PXI-6624 |
| 0x2410 | PCI-6733 |
| 0x2420 | PXI-6733 |
| 0x2430 | PCI-6731 |
| 0x24F0 | PXI-4472 |
| 0x2510 | PCI-4472 |
| 0x2520 | PCI-4474 |
| 0x27A0 | PCI-6123 |
| 0x27B0 | PXI-6123 |
| 0x2B10 | PXI-6527 |
| 0x2B20 | PCI-6527 |
| 0x2B80 | PXI-6713 |
| 0x2B90 | PXI-6711 |
| 0x2C60 | PCI-6601 |
| 0x2C90 | PCI-6703 |
| 0x2CC0 | PXI-6608 |
| 0x2EC0 | PXI-6115 |
| 0x2ED0 | PCI-6115 |
| 0x2EE0 | PXI-6120 |
| 0x2EF0 | PCI-6120 |
| 0x7023 | PXI-2593 |
| 0x703F | PXI-2566 |
| 0x7040 | PXI-2567 |
| 0x704C | PXI-2530 |
| 0x7067 | PXI-2529 |
| 0x7073 | PCI-6723 |
| 0x707E | PXI-4462 |
| 0x7085 | PCI-6509 |
| 0x7086 | PXI-6528 |
| 0x7087 | PCI-6515 |
| 0x7088 | PCI-6514 |
| 0x708C | PXI-2568 |
| 0x708D | PXI-2569 |
| 0x709F | USB-9421 |
| 0x70A1 | USB-9472 |
| 0x70A2 | USB-9481 |
| 0x70A4 | USB-9201 |
| 0x70A5 | USB-9221 |
| 0x70A7 | USB-9263 |
| 0x70A8 | USB-9233 |
| 0x70A9 | PCI-6528 |
| 0x70AA | PCI-6229 |
| 0x70AB | PCI-6259 |
| 0x70AC | PCI-6289 |
| 0x70AD | PXI-6251 |
| 0x70AE | PXI-6220 |
| 0x70AF | PCI-6221 |
| 0x70B0 | PCI-6220 |
| 0x70B1 | PXI-6229 |
| 0x70B2 | PXI-6259 |
| 0x70B3 | PXI-6289 |
| 0x70B4 | PCI-6250 |
| 0x70B5 | PXI-6221 |
| 0x70B6 | PCI-6280 |
| 0x70B7 | PCI-6254 |
| 0x70B8 | PCI-6251 |
| 0x70B9 | PXI-6250 |
| 0x70BA | PXI-6254 |
| 0x70BB | PXI-6280 |
| 0x70BC | PCI-6284 |
| 0x70BD | PCI-6281 |
| 0x70BE | PXI-6284 |
| 0x70BF | PXI-6281 |
| 0x70C0 | PCI-6143 |
| 0x70C3 | PCI-6511 |
| 0x70C8 | PCI-6513 |
| 0x70C9 | PXI-6515 |
| 0x70CC | PCI-6512 |
| 0x70CD | PXI-6514 |
| 0x70D0 | PXI-2570 |
| 0x70D1 | PXI-6513 |
| 0x70D2 | PXI-6512 |
| 0x70D3 | PXI-6511 |
| 0x70D4 | PCI-6722 |
| 0x70E1 | PXI-2532 |
| 0x70F2 | PCI-6224 |
| 0x70F3 | PXI-6224 |
| 0x70FF | PXI-6723 |
| 0x7100 | PXI-6722 |
| 0x710D | PXI-6143 |
| 0x7124 | PCI-6510 |
| 0x7125 | PCI-6516 |
| 0x7126 | PCI-6517 |
| 0x7127 | PCI-6518 |
| 0x7128 | PCI-6519 |
| 0x712C | USB-9265 |
| 0x712E | USB-9421 (DSUB) |
| 0x7132 | USB-9472 (DSUB) |
| 0x7137 | PXI-2575 |
| 0x713C | PXI-2585 |
| 0x713D | PXI-2586 |
| 0x7146 | PCI-6132 |
| 0x7147 | PXI-6132 |
| 0x7148 | PCI-6122 |
| 0x7149 | PXI-6122 |
| 0x7150 | PXI-2564 |
| 0x715F | NI 9221 |
| 0x7160 | NI 9421 |
| 0x7161 | NI 9421 (DSUB) |
| 0x7162 | NI 9472 |
| 0x7163 | NI 9472 (DSUB) |
| 0x7164 | NI 9481 |
| 0x7165 | NI 9401 |
| 0x716B | PCI-6230 |
| 0x716C | PCI-6225 |
| 0x716D | PXI-6225 |
| 0x716F | PCI-4461 |
| 0x7170 | PCI-4462 |
| 0x7171 | PCI-6010 |
| 0x7177 | PXI-6230 |
| 0x717A | USB-6008 |
| 0x717B | USB-6009 |
| 0x717D | PCIe-6251 |
| 0x717F | PCIe-6259 |
| 0x718A | USB-6501 |
| 0x718B | PCI-6521 |
| 0x718C | PXI-6521 |
| 0x7191 | PCI-6154 |
| 0x71A1 | USB-9201 (DSUB) |
| 0x71A2 | USB-9221 (DSUB) |
| 0x71A5 | PXI-2594 |
| 0x71A7 | PXI-2595 |
| 0x71A9 | PXI-2596 |
| 0x71AA | PXI-2597 |
| 0x71AB | PXI-2598 |
| 0x71AC | PXI-2599 |
| 0x71B0 | NI 9211 |
| 0x71B1 | NI 9215 |
| 0x71B2 | NI 9215 (BNC) |
| 0x71B3 | NI 9205 (DSUB) |
| 0x71B4 | NI 9263 |
| 0x71BB | PXI-2584 |
| 0x71BC | PCI-6221 (37-pin) |
| 0x71C2 | USB-9239 |
| 0x71C3 | USB-9237 |
| 0x71C5 | PCI-6520 |
| 0x71C6 | PXI-2576 |
| 0x71D9 | USB-9211A |
| 0x71DA | USB-9215A |
| 0x71DB | USB-9215A (BNC) |
| 0x71DF | USB-6525 |
| 0x71E0 | PCI-6255 |
| 0x71E1 | PXI-6255 |
| 0x7209 | PCI-6233 |
| 0x720A | PXI-6233 |
| 0x720B | PCI-6238 |
| 0x720C | PXI-6238 |
| 0x7252 | USB-6251 |
| 0x7253 | USB-6259 |
| 0x7263 | NI 9234 |
| 0x7264 | NI 9206 |
| 0x7265 | NI 9205 |
| 0x726F | USB-6210 |
| 0x7270 | USB-6211 |
| 0x7271 | USB-6215 |
| 0x7272 | USB-6218 |
| 0x7279 | PCI-6232 |
| 0x727A | PXI-6232 |
| 0x727B | PCI-6239 |
| 0x727C | PXI-6239 |
| 0x7281 | PCI-6236 |
| 0x7282 | PXI-6236 |
| 0x7283 | PXI-2554 |
| 0x7285 | NI 9237 |
| 0x72A0 | USB-6251 (Mass Termination) |
| 0x72A1 | USB-6259 (Mass Termination) |
| 0x72B5 | USB-9234 |
| 0x72B9 | NI 9411 |
| 0x72BA | NI 9422 |
| 0x72BB | NI 9423 |
| 0x72BC | NI 9435 |
| 0x72BD | NI 9474 |
| 0x72BE | NI 9485 |
| 0x72BF | NI 9403 |
| 0x72C0 | NI 9425 |
| 0x72C1 | NI 9476 |
| 0x72C2 | NI 9477 |
| 0x72C3 | NI 9264 |
| 0x72C4 | NI 9265 |
| 0x72C5 | NI 9201 |
| 0x72C6 | NI 9201 (DSUB) |
| 0x72C7 | NI 9221 (DSUB) |
| 0x72C8 | NI 9203 |
| 0x72C9 | NI 9217 |
| 0x72CA | NI 9219 |
| 0x72CB | NI 9239 |
| 0x72CC | SensorDAQ |
| 0x72D0 | PXI-2545 |
| 0x72D1 | PXI-2546 |
| 0x72D2 | PXI-2547 |
| 0x72D3 | PXI-2548 |
| 0x72D4 | PXI-2549 |
| 0x72D5 | PXI-2555 |
| 0x72D6 | PXI-2556 |
| 0x72D7 | PXI-2557 |
| 0x72D8 | PXI-2558 |
| 0x72D9 | PXI-2559 |
| 0x72DC | USB-6221 |
| 0x72DE | USB-6229 |
| 0x72E8 | PXIe-6251 |
| 0x72E9 | PXIe-6259 |
| 0x72EF | PXI-4498 |
| 0x72F0 | PXI-4496 |
| 0x72F3 | USB-6005 VSA |
| 0x72F6 | USB-9264 |
| 0x72FA | NI 9229 |
| 0x72FD | USB-9229 |
| 0x72FF | USB-6509 |
| 0x730C | USB-9219 |
| 0x731C | PXI-2535 |
| 0x731D | PXI-2536 |
| 0x7322 | PXIe-6124 |
| 0x7326C4C4 | PCIe-6509 |
| 0x7327 | PXI-6529 |
| 0x732D | USB-6255 |
| 0x732E | USB-6255 (Mass Termination) |
| 0x732F | USB-6225 |
| 0x7330 | USB-6225 (Mass Termination) |
| 0x7335 | PXI-2533 |
| 0x7336 | PXI-2534 |
| 0x7337 | NI 9402 |
| 0x7338 | NI 9375 |
| 0x7339 | USB-6212 |
| 0x733B | USB-6216 |
| 0x733F | USB-6281 |
| 0x7340 | USB-6281 (Mass Termination) |
| 0x7342 | PXI-4461 |
| 0x7343 | USB-6289 |
| 0x7344 | USB-6289 (Mass Termination) |
| 0x7345 | USB-6221 (BNC) |
| 0x7346 | USB-6229 (BNC) |
| 0x7347 | USB-6251 (BNC) |
| 0x7348 | USB-6259 (BNC) |
| 0x7359 | PXI-4495 |
| 0x7367 | USB-9239 (BNC) |
| 0x7368 | USB-9229 (BNC) |
| 0x7369 | USB-9263 (BNC) |
| 0x737A | NI 9229 (BNC) |
| 0x737B | NI 9239 (BNC) |
| 0x737C | NI 9263 (BNC) |
| 0x7381 | NI 9235 |
| 0x7382 | NI 9236 |
| 0x7388 | NI 9225 |
| 0x7389 | USB-6212 (Mass Termination) |
| 0x738A | USB-6216 (Mass Termination) |
| 0x73A1 | PXIe-4498 |
| 0x73A2 | PXIe-4496 |
| 0x73A6 | ELVIS II |
| 0x73C5 | PXIe-2527 |
| 0x73C6 | PXIe-2529 |
| 0x73C9 | PXIe-2532 |
| 0x73CA | PXIe-2569 |
| 0x73CB | PXIe-2575 |
| 0x73CC | PXIe-2593 |
| 0x73D1 | USB-4432 |
| 0x73E2 | NI 9213 |
| 0x73E3 | NI 9426 |
| 0x73E4 | NI 9475 |
| 0x73E5 | NI 9478 |
| 0x73E6 | NI 9237 (DSUB) |
| 0x73E7 | ELVIS II+ |
| 0x73F4 | PXI-2515 |
| 0x73FC | USB-6212 (BNC) |
| 0x73FD | USB-6216 (BNC) |
| 0x73FE | USB-6218 (BNC) |
| 0x7420 | NI 9227 |
| 0x7425C4C4 | PCIe-6320 |
| 0x7426C4C4 | PXIe-6321 |
| 0x7427C4C4 | PCIe-6321 |
| 0x7428C4C4 | PXIe-6323 |
| 0x7429C4C4 | PCIe-6323 |
| 0x742AC4C4 | PXIe-6341 |
| 0x742BC4C4 | PCIe-6341 |
| 0x742CC4C4 | PXIe-6343 |
| 0x742DC4C4 | PCIe-6343 |
| 0x742EC4C4 | PXIe-6351 |
| 0x742FC4C4 | PCIe-6351 |
| 0x7430C4C4 | PXIe-6353 |
| 0x7431C4C4 | PCIe-6353 |
| 0x7432C4C4 | PXIe-6361 |
| 0x7433C4C4 | PCIe-6361 |
| 0x7434C4C4 | PXIe-6363 |
| 0x7435C4C4 | PCIe-6363 |
| 0x7436C4C4 | PXIe-6356 |
| 0x7437C4C4 | PXIe-6358 |
| 0x7438C4C4 | PXIe-6366 |
| 0x7439C4C4 | PXIe-6368 |
| 0x7448 | PXI-2510 |
| 0x7449 | USB-9213 |
| 0x744F | USB-4431 |
| 0x7454 | PXI-2512 |
| 0x7455 | PXI-2514 |
| 0x7456 | PXIe-2512 |
| 0x7457 | PXIe-2514 |
| 0x745C | USB-9264 (DSUB) |
| 0x7492C4C4 | PXIe-4300 |
| 0x7493 | cDAQ-9188 |
| 0x7494 | NI 9264 (DSUB) |
| 0x74A4 | cDAQ-9178 |
| 0x74A5 | cDAQ-9174 |
| 0x74A8C4C4 | PXIe-4330 |
| 0x74A9C4C4 | PXIe-4331 |
| 0x74AE | PXIe-2515 |
| 0x74B2C4C4 | PXIe-4353 |
| 0x74B4 | PXI-2531 |
| 0x74B5 | PXIe-2531 |
| 0x74B7 | USB-TC01 |
| 0x74DF | NI 9207 (DSUB) |
| 0x74E0 | NI 9208 (DSUB) |
| 0x74E6 | NI 9269 |
| 0x74F7 | USB-6343 |
| 0x74F8 | USB-6341 |
| 0x74FA | USB-6351 |
| 0x74FB | USB-6353 |
| 0x74FD | USB-6361 |
| 0x74FE | USB-6363 |
| 0x7510 | NI 2810 |
| 0x7511 | NI 2811 |
| 0x7512 | NI 2815 |
| 0x7513 | NI 2816 |
| 0x7528 | PXIe-4497 |
| 0x7529 | PXIe-4499 |
| 0x752A | PXIe-4492 |
| 0x752B | NI 9214 |
| 0x7530 | NI 9222 |
| 0x7531 | NI 9223 |
| 0x7559 | NI 9232 |
| 0x755B | myDAQ |
| 0x755F | cDAQ-9181 |
| 0x7560 | cDAQ-9191 |
| 0x7561 | USB-6356 (32 MS) |
| 0x7563 | USB-6356 (64 MS) |
| 0x7567 | USB-6366 (32 MS) |
| 0x7569 | USB-6366 (64 MS) |
| 0x7578 | NI 9375 (DSUB) |
| 0x757B | NI 2812 |
| 0x757E | NI 2813 |
| 0x7581 | NI 2814 |
| 0x7584 | NI 2817 |
| 0x7587 | NI 2833 |
| 0x758A | NI 2834 |
| 0x7598 | PXI-2571 |
| 0x759D | USB-6361 (Mass Termination) |
| 0x759E | USB-6363 (Mass Termination) |
| 0x75A1 | USB-6366 (64 MS) (Mass Termination) |
| 0x75BA | PXI-2543 |
| 0x75BB | PXIe-2543 |
| 0x75CFC4C4 | PXIe-4357 |
| 0x75DA | USB-6341 (BNC) |
| 0x75DB | USB-6343 (BNC) |
| 0x75DC | USB-6361 (BNC) |
| 0x75DD | USB-6363 (BNC) |
| 0x75DE | USB-6356 (32 MS) (BNC) |
| 0x75DF | USB-6366 (64 MS) (BNC) |
| 0x75EB | NI 9469 |
| 0x75F0 | cDAQ-9171 |
| 0x7606 | NI 9220 |
| 0x7614 | cDAQ-9138 |
| 0x7616 | NI 9220 (DSUB) |
| 0x7617 | cDAQ-9184 |
| 0x761F | PXI-2540 |
| 0x7620 | PXIe-2540 |
| 0x7621 | PXI-2541 |
| 0x7622 | PXIe-2541 |
| 0x7625 | USB-6346 |
| 0x7628 | cDAQ-9139 |
| 0x7638 | PXI-2720 |
| 0x7639 | PXI-2722 |
| 0x763A | PXIe-2725 |
| 0x763B | PXIe-2727 |
| 0x763DC4C4 | PXIe-6349 |
| 0x764B | PXIe-2790 |
| 0x764C | PXI-2520 |
| 0x764D | PXI-2521 |
| 0x764E | PXI-2522 |
| 0x764F | PXI-2523 |
| 0x7654 | PXI-2796 |
| 0x7655 | PXI-2797 |
| 0x7656 | PXI-2798 |
| 0x7657 | PXI-2799 |
| 0x765D | PXI-2542 |
| 0x765E | PXIe-2542 |
| 0x765F | PXI-2544 |
| 0x7660 | PXIe-2544 |
| 0x76ABC4C4 | PXIe-4322 |
| 0x76AF | USB-6000 |
| 0x76BF | USB-6001 |
| 0x76C4 | USB-6002 |
| 0x76C6 | USB-6003 |
| 0x76C8C4C4 | PXIe-6614 |
| 0x76C9C4C4 | PXIe-6612 |
| 0x76DCC4C4 | PXIe-4610 |
| 0x76E3 | USB-9482 |
| 0x76E7 | cDAQ-9188XT |
| 0x76F5 | NI 9482 |
| 0x770B | NI 2865 |
| 0x770F | NI 9244 |
| 0x7711C4C4 | PXIe-4464 |
| 0x7712C4C4 | PXIe-4463 |
| 0x7716C4C4 | PCIe-6612 |
| 0x771EC4C4 | PXIe-4339 |
| 0x7739 | cDAQ-9132 |
| 0x773A | cDAQ-9134 |
| 0x773C | NI 9222 (BNC) |
| 0x773D | NI 9223 (BNC) |
| 0x7749 | NI 9242 |
| 0x7751 | NI 9238 |
| 0x7779 | NI 9218 (DSUB) |
| 0x777A | NI 9218 |
| 0x777F | NI 9361 |
| 0x778D | NI 9437 |
| 0x77A5C4C4 | PXIe-6345 |
| 0x77A6C4C4 | PXIe-6355 |
| 0x77A7C4C4 | PXIe-6365 |
| 0x77A8C4C4 | PXIe-6375 |
| 0x77AB | NI 9212 |
| 0x77BE | cDAQ-9133 |
| 0x77BF | cDAQ-9135 |
| 0x77CAC4C4 | PXIe-6738 |
| 0x77CBC4C4 | PXIe-6739 |
| 0x77CE | NI 9230 |
| 0x77CF | NI 9260 (BNC) |
| 0x77D0 | NI 9260 (Mini XLR) |
| 0x77D8 | NI 9216 |
| 0x77D9 | NI 9226 |
| 0x77E6 | NI 9344 |
| 0x77E7 | NI 9247 |
| 0x77EB | NI 9251 (Mini XLR) |
| 0x77EC | NI 9250 (BNC) |
| 0x77F1 | NI 9209 (DSUB) |
| 0x77F4 | cDAQ-9179 |
| 0x77F6 | NI 9246 |
| 0x77F9 | NI 9216 (DSUB) |
| 0x77FA | NI 9226 (DSUB) |
| 0x7802C4C4 | PXIe-4302 |
| 0x7803C4C4 | PXIe-4303 |
| 0x7805C4C4 | PXIe-4305 |
| 0x780F | NI 9224 |
| 0x7810 | NI 9228 |
| 0x7829C4C4 | PXIe-4340 |
| 0x7834 | cDAQ-9136 |
| 0x7836 | cDAQ-9137 |
| 0x7844C4C4 | PXIe-4480 |
| 0x7845C4C4 | PXIe-4481 |
| 0x7868 | NI 9232 (BNC) |
| 0x7869 | NI 9230 (BNC) |
| 0x786D | NI 9436 |
| 0x7870 | Simulated DAQ Device |
| 0x7882C4C4 | PXIe-6376 |
| 0x7883C4C4 | PXIe-6378 |
| 0x788B | NI 9202 (DSUB) |
| 0x788D | NI 9202 |
| 0x788EC4C4 | PXIe-4304 |
| 0x78A0 | NI 9775 |
| 0x78ACC4C4 | PXIe-4309 |
| 0x78B2 | NI 9210 (miniTC) |
| 0x78B5 | NI 9266 |
| 0x78B9 | cDAQ-9189 |
| 0x78C7 | cDAQ-9185 |
| 0x78DFC4C4 | PXIe-4310 |
| 0x7903 | cRIO-9040 |
| 0x7905 | cRIO-9045 |
| 0x7907 | cRIO-9043 |
| 0x7909 | cRIO-9048 |
| 0x790D | cRIO-9048 (TPM) |
| 0x790F | cRIO-9042 |
| 0x7911 | cRIO-9047 |
| 0x7913 | cRIO-9049 |
| 0x7918 | NI 9207 |
| 0x7919 | NI 9208 |
| 0x791A | NI 9209 |
| 0x7923 | NI 9425 (Spring) |
| 0x7924 | NI 9476 (Spring) |
| 0x7931 | NI 9231 |
| 0x7941 | FD-11613 |
| 0x7943 | FD-11637 |
| 0x7945 | FD-11603 |
| 0x7988C4C4 | PCIe-6738 |
| 0x7998 | NI 9262 |
| 0x7999C4C4 | PCIe-6376 |
| 0x799AC4C4 | PCIe-6374 |
| 0x799EC4C4 | PXIe-6386 |
| 0x799FC4C4 | PXIe-6396 |
| 0x79A7C4C4 | PCIe-6346 |
| 0x79C5 | NI 9253 |
| 0x79C9 | NI 9252 |
| 0x79CB | NI 9252 (DSUB) |
| 0x79CF | cRIO-9046 |
| 0x79D1 | cRIO-9041 |
| 0x79E1 | cRIO-9053 |
| 0x79E2 | cRIO-9054 |
| 0x79E3 | cRIO-9056 |
| 0x79E4 | cRIO-9057 |
| 0x79F7 | USB-6349 |
| 0x79FD | NI 9266 (DSUB) |
| 0x79FF | FD-11614 |
| 0x7A07 | FD-11601 |
| 0x7A08 | USB-6346 (BNC) |
| 0x7A1C | FD-11634 |
| 0x7A27 | NI 9210 |
| 0x7A29 | cRIO-9058 |
| 0x7A2C | cRIO-9055 |
| 0x7A32 | FD-11605 |
| 0x7A3C | sbRIO-9603 |
| 0x7A3D | sbRIO-9608 |
| 0x7A3E | sbRIO-9628 |
| 0x7A3F | sbRIO-9638 |
| 0x7A42 | sbRIO-9609 |
| 0x7A44 | sbRIO-9629 |
| 0x7A47 | NI AI 0-15 |
| 0x7A48 | NI AO 0-3 |
| 0x7A49 | NI DIO 0-3 |
| 0x7A4A | NI DIO 4-11 |
| 0x7A50 | NI DIO 12-19 |
| 0x7A51 | NI DIO 20-27 |
| 0x7A5F | NI 9326 |
| 0x7A77C4C4 | PXIe-6509 |
| 0x7AD5 | TS-15100 |
| 0x7AD6 | TS-15110 |
| 0x7AD7 | TS-15120 |
| 0x7AD8 | TS-15130 |
| 0x7ADA | TS-15010 |
| 0x7ADC | TS-15000 |
| 0x7ADE | TS-15050 DIO P0 |
| 0x7ADf | TS-15200 |
| 0x7B39 | NI 9204 (DSUB) |
| 0x7B3A | NI 9204 |
| 0x7B3E | USB-6421 |
| 0x7B40 | USB-6423 |
| 0x7B42 | USB-6451 |
| 0x7B44 | USB-6453 |
| 0x7B46 | NI 9222 (Snap In) |
| 0x7B48 | NI 9223 (Snap In) |
| 0x7B4A | NI 9225 (Snap In) |
| 0x7B4C | NI 9227 (Snap In) |
| 0x7B4E | NI 9230 (Snap In) |
| 0x7B50 | NI 9232 (Snap In) |
| 0x7B52 | NI 9238 (Snap In) |
| 0x7B54 | NI 9269 (Snap In) |
| 0x7B56 | NI 9229 (Snap In) |
| 0x7B58 | NI 9239 (Snap In) |
| 0x7B64C4C4 | PCIe-6340 |
| 0x7B65C4C4 | PCIe-6342 |
| 0x7B68C4C4 | PCIe-6350 |
| 0x7B69C4C4 | PCIe-6352 |
| 0x7B6CC4C4 | PXIe-6357 |
| 0x9020 | PXI-2501 |
| 0x9030 | PXI-2503 |
| 0x9040 | PXI-2527 |
| 0x9050 | PXI-2565 |
| 0x9060 | PXI-2590 |
| 0x9070 | PXI-2591 |
| 0x7B5E | NI 9320 |
| 0x7B5F | NI 9320 (DSUB) |
| 0x7B66C4C4 | PCIe-6345 |
| 0x7B67C4C4 | PCIe-6347 |
| 0x7B6AC4C4 | PCIe-6355 |
| 0x7B6BC4C4 | PCIe-6357 |
| 0X7B6DC4C4 | PXIe-6381 |
| 0X7B6EC4C4 | PXIe-6383 |

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=hardwredatacompression.html language=enus -->
## TOPIC 00095: Hardware Data Compression (DSA and NI 433x)

- bundle_id: `ni-daqmx`
- source_path: `hardwredatacompression.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/hardwredatacompression.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the raw data compression type is set to lossless packing and all channels in a task support hardware compression, hardware data compression is enabled by default. However, if any channels do not support hardware data compression, software data compression is selected by default.

### Hardware Data Compression (DSA and NI 433*x*)

If the raw data compression type is set to lossless packing and all channels in a task support hardware compression, hardware data compression is enabled by default. However, if any channels do not support hardware data compression, software data compression is selected by default.

Parent topic:

DSA

<!--NI_TOPIC bundle=ni-daqmx path=hardwresoftwretiming.html language=enus -->
## TOPIC 00096: Timing, Hardware Versus Software

- bundle_id: `ni-daqmx`
- source_path: `hardwresoftwretiming.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/hardwresoftwretiming.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use software timing or hardware timing to control when a signal is generated. With hardware timing, a digital signal, such as a clock on your device, controls the rate of generation. With software timing, the rate at which the samples are generated is determined by the software and operating

### Timing, Hardware Versus Software

You can use software timing or hardware timing to control when a signal is generated. With hardware timing, a digital signal, such as a clock on your device, controls the rate of generation. With software timing, the rate at which the samples are generated is determined by the software and operating system instead of by the measurement device. A hardware clock can run much faster than a software loop. A hardware clock is also more accurate than a software loop.

In NI-DAQmx, select hardware timing with the Sample Clock Timing function/VI or by setting the Sample Timing Type attribute/property to Sample Clock. If you do neither of these things, or you set the Sample Timing Type attribute/property to On Demand, you are selecting software timing.

Note

Parent topic:

Timing and Triggering

<!--NI_TOPIC bundle=ni-daqmx path=labview.html language=enus -->
## TOPIC 00097: LabVIEW

- bundle_id: `ni-daqmx`
- source_path: `labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/labview.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you program your NI-DAQmx-supported device in LabVIEW, you can interactively create virtual channels—both global and local—and tasks by launching the DAQ Assistant from MAX or from within LabVIEW. You also can create local virtual channels and tasks, and write your own applications using the NI-D

### LabVIEW

If you program your NI-DAQmx-supported device in LabVIEW, you can interactively create virtual channels—both global and local—and tasks by launching the DAQ Assistant from MAX or from within LabVIEW. You also can create local virtual channels and tasks, and write your own applications using the NI-DAQmx API.

To learn about which NI-DAQmx VIs are most commonly used when creating a NI-DAQmx data acquisition application, see Learn 10 Functions in NI-DAQmx and Handle 80% of your Data Acquisition Applications.

For help with NI-DAQmx VIs, refer to DAQmx - Data Acquisition VIs and Functions.

For general help with programming in LabVIEW, refer to LabVIEW Help.

For help with using the DAQ Assistant with LabVIEW, refer to Using the DAQ Assistant to Automatically Generate LabVIEW Code.

Parent topic:

NI-DAQmx Overview

<!--NI_TOPIC bundle=ni-daqmx path=measuring-digital-frequency-and-period-progra_2.html language=enus -->
## TOPIC 00098: Measuring Digital Frequency and Period Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `measuring-digital-frequency-and-period-progra_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/measuring-digital-frequency-and-period-progra_2.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps required in an NI-DAQmx application to measure digital frequency or period. Alternatively, you can configure a task for measuring digital frequency using the DAQ Assistant.Digital frequency and period are examples of counter measurements. Refer to Count

### Measuring Digital Frequency and Period Programming Flowchart

The following flowchart depicts the main steps required in an NI-DAQmx application to measure digital frequency or period. Alternatively, you can configure a task for measuring digital frequency using the DAQ Assistant.

[IMAGE alt='image' src='GUID-17C03DC5-CACA-42ED-B7FA-CECF5CD3E704-a5.gif']

Digital frequency and period are examples of counter measurements. Refer to Counter Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Measuring Period, Semi-Period, Pulse Width, and Two-Edge Separation

<!--NI_TOPIC bundle=ni-daqmx path=measuring-position-with-an-rvdt-or-lvdt-progr_2.html language=enus -->
## TOPIC 00099: Measuring Position with an RVDT or LVDT Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `measuring-position-with-an-rvdt-or-lvdt-progr_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/measuring-position-with-an-rvdt-or-lvdt-progr_2.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps required in an NI-DAQmx application to measure position with an RVDT or LVDT. Alternatively, you can configure a task for measuring position using the DAQ Assistant. To increase performance, especially when multiple samples are read, include the Start

### Measuring Position with an RVDT or LVDT Programming Flowchart

The following flowchart depicts the main steps required in an NI-DAQmx application to measure position with an RVDT or LVDT. Alternatively, you can configure a task for measuring position using the DAQ Assistant.

[IMAGE alt='image' src='GUID-79EF44E8-5B2A-4DB1-B69E-914970BC12CA-a5.gif']

Tip

Measuring position is an example of an analog input measurement. Refer to Analog Input Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Measuring Linear Displacement

<!--NI_TOPIC bundle=ni-daqmx path=measuring-position-with-encoders-programming-_2.html language=enus -->
## TOPIC 00100: Measuring Position with Encoders Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `measuring-position-with-encoders-programming-_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/measuring-position-with-encoders-programming-_2.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps you must complete for measuring position with an encoder in an NI-DAQmx application. If you prefer, you can configure a task using the DAQ Assistant.Measuring position with an encoder is an example of a counter measurement. Refer to Counter Programming

### Measuring Position with Encoders Programming Flowchart

The following flowchart depicts the main steps you must complete for measuring position with an encoder in an NI-DAQmx application. If you prefer, you can configure a task using the DAQ Assistant.

[IMAGE alt='image' src='GUID-2BD2DAEC-C044-4DBB-8831-61B36778649F-a5.gif']

Measuring position with an encoder is an example of a counter measurement. Refer to Counter Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Measuring Linear Displacement

<!--NI_TOPIC bundle=ni-daqmx path=measuring-pulses-programming-flowchart_2.html language=enus -->
## TOPIC 00101: Measuring Pulses Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `measuring-pulses-programming-flowchart_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/measuring-pulses-programming-flowchart_2.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps required in an NI-DAQmx application to measure the frequency/duty cycle, high/low ticks, or high/low time of digital pulses. Alternatively, you can configure a task for measuring digital pulses using the DAQ Assistant.Digital frequency and period are ex

### Measuring Pulses Programming Flowchart

The following flowchart depicts the main steps required in an NI-DAQmx application to measure the frequency/duty cycle, high/low ticks, or high/low time of digital pulses. Alternatively, you can configure a task for measuring digital pulses using the DAQ Assistant.

[IMAGE alt='image' src='GUID-1943DD6D-3001-479E-99EE-76021CE17C19-a5.gif']

Digital frequency and period are examples of counter measurements. Refer to Counter Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Measuring Digital Frequency

<!--NI_TOPIC bundle=ni-daqmx path=measuring-pulses-programming-flowchart_3.html language=enus -->
## TOPIC 00102: Measuring Pulses Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `measuring-pulses-programming-flowchart_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/measuring-pulses-programming-flowchart_3.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps required in an NI-DAQmx application to measure the frequency/duty cycle, high/low ticks, or high/low time of digital pulses. Alternatively, you can configure a task for measuring digital pulses using the DAQ Assistant.Digital frequency and period are ex

### Measuring Pulses Programming Flowchart

The following flowchart depicts the main steps required in an NI-DAQmx application to measure the frequency/duty cycle, high/low ticks, or high/low time of digital pulses. Alternatively, you can configure a task for measuring digital pulses using the DAQ Assistant.

[IMAGE alt='image' src='GUID-1943DD6D-3001-479E-99EE-76021CE17C19-a5.gif']

Digital frequency and period are examples of counter measurements. Refer to Counter Programming Flowcharts for additional flowcharts that can help you create an application.

Parent topic:

Measuring Period, Semi-Period, Pulse Width, and Two-Edge Separation

<!--NI_TOPIC bundle=ni-daqmx path=new-features-and-changes.html language=enus -->
## TOPIC 00103: NI-DAQmx New Features and Changes

- bundle_id: `ni-daqmx`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-DAQmx. Discover what is new in the latest releases of NI-DAQmx.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might includ

### NI-DAQmx
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-DAQmx.

NI-DAQmx

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-DAQmx
 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx 2026 Q2.

##### New
 Features

This version of the NI-DAQmx provides
 support for the following features:

- New features for the PXIe‑4311
  - Virtual Power Channel — Support for virtual power channels
 that calculate power measurements with physical voltage and current channels.
  - Analog AI Filtering — Support for enabling a lowpass
 anti-aliasing filter through the following DAQmx property: Analog
 Input::Filter::Analog Filter::Lowpass::Enable . The filter has a fixed
 cutoff frequency of 100 kHz , disabled by default, and
 applies to all channels when enabled.
  - Averaging SMIO Timing Mode — Adds an Averaging (SMIO) timing
 mode that averages multiple ADC samples to reduce noise and improve effective
 resolution. The averaging behavior depends on the sample rate. You can also configure
 the rate through the Averaging Window Size property in hardware-timed single-point
 mode.

##### New
 Hardware Support

This version of NI-DAQmx adds
 support for the following hardware:

- PXIe-4311 (SC Express)

#### NI-DAQmx
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx
 2025 Q4.

##### New
 Hardware Support

This version of
 NI-DAQmx provides support for the following hardware:

- NI-9320 (C Series)
- PXIe-6381 (X Series)
- PXIe-6383 (X Series)
- PCIe-6345 (X Series)
- PCIe-6347 (X Series)
- PCIe-6355 (X Series)
- PCIe-6357 (X Series)

#### NI-DAQmx
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx
 2025 Q3.

##### New
 Hardware Support

This version of NI-DAQmx
 provides support for the following hardware:

- PCIe-6340
- PCIe-6342
- PCIe-6350
- PCIe-6352
- PXIe-6321
- PXIe-6323
- PXIe-6343
- PXIe-6351
- PXIe-6353
- PXIe-6357

#### NI-DAQmx
 2025 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx
 2025 Q2.

##### New
 Hardware Support

This version of NI-DAQmx
 provides support for the following hardware:

- NI-9225 (Snap In)
- NI-9229 (Snap In)
- NI-9239 (Snap In)
- NI-9170
- NI-9173
- NI-9177

#### NI-DAQmx
 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-DAQmx
 2025 Q1.

##### New
 Hardware Support

This version of NI-DAQmx
 provides support for the following hardware:

- NI-9222 (Snap In)
- NI-9223 (Snap In)
- NI-9227 (Snap In)
- NI-9230 (Snap In)
- NI-9232 (Snap In)
- NI-9238 (Snap In)
- NI-9269 (Snap In)

<!--NI_TOPIC bundle=ni-daqmx path=strainrosette.html language=enus -->
## TOPIC 00104: Strain Rosette

- bundle_id: `ni-daqmx`
- source_path: `strainrosette.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/strainrosette.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A strain gage can measure strain in only one direction—the axis along which the strain gage is mounted. To effectively measure the three independent components of plane strain (extensional strain along X and Y axis, as well as shear strain), three independent strain measurements are needed. Strain g

### Strain Rosette

A strain gage can measure strain in only one direction—the axis along which the strain gage is mounted. To effectively measure the three independent components of plane strain (extensional strain along X and Y axis, as well as shear strain), three independent strain measurements are needed. Strain gage rosettes are used to perform such measurements.

A strain gage rosette is an arrangement of two or three closely positioned strain gages, separately oriented to measure the strains along different directions of the underlying surface of the object being measured.

Strain-gage manufacturers offer three basic types of strain gage rosettes.

Tee Rosette

Rectangular Rosette

Delta Rosette

Parent topic:

Bridge-Based Sensors

Related concepts:

- Strain Gages

<!--NI_TOPIC bundle=ni-daqmx path=subsystem.html language=enus -->
## TOPIC 00105: Subsystem

- bundle_id: `ni-daqmx`
- source_path: `subsystem.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/subsystem.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A subsystem is the circuitry (ADCs, DACs, clocks, triggers, timing signals, timing engines, and so on) that a device uses to acquire or generate samples. On DAQ devices, there are separate subsystems for analog input, analog output, each counter, and digital I/O. A subsystem is not synonymous with I

### Subsystem

A 
 *subsystem* is the circuitry (ADCs, DACs, clocks, triggers, timing signals, timing engines, and so on) that a device uses to acquire or generate samples. On DAQ devices, there are separate subsystems for analog input, analog output, each counter, and digital I/O. A subsystem is not synonymous with I/O type, however. For instance, each counter's input and output circuitry make up one subsystem. The trigger bus can also function as a subsystem.

Parent topic:

Timing and Triggering

<!--NI_TOPIC bundle=ni-daqmx path=supconnect.html language=enus -->
## TOPIC 00106: SC Express Smart Accessory Connections

- bundle_id: `ni-daqmx`
- source_path: `supconnect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/supconnect.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following connections are supported on these SC Express accessories: Accessory Supported Connections Description CAL-4353 _tc_calibration Connects all TC channels to the calibration input. This connection is used to verify and adjust TC gain accuracy. _cjc_calibration Connects one CJC channel to

### SC Express Smart Accessory Connections

The following connections are supported on these SC Express accessories:

| Accessory | Supported Connections | Description |
| --- | --- | --- |
| CAL-4353 | _tc_calibration | Connects all TC channels to the calibration input. This connection is used to verify and adjust TC gain accuracy. |
| _cjc_calibration | Connects one CJC channel to the calibration input. This connection is used to verify and adjust CJC gain and offset accuracy. |  |
| _short_tc_terminals | Connects all TC channels together. |  |
| RM-4339 | _remote_sense_floating | Disconnects remote sensing for calibration. |
| _cal_channel | Connects all channels to an external calibration source. |  |
| RM-4302 | _cal_channel | Connects all channels to an external calibration source. |
| RM-4304 | _cal_channel | Connects all channels to an external calibration source. |

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=supported-devs-tsc.html language=enus -->
## TOPIC 00107: Supported Devices for Trigger Skew Correction

- bundle_id: `ni-daqmx`
- source_path: `supported-devs-tsc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/supported-devs-tsc.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following devices support locking synchronized triggers to a clock to compensate for skew. SC Express devices X Series devices

### Supported Devices for Trigger Skew Correction

The following devices support locking synchronized triggers to a clock to compensate for skew.

- SC Express devices
- X Series devices

Parent topic:

Synchronization

Related concepts:

- Trigger Skew Correction

<!--NI_TOPIC bundle=ni-daqmx path=switches.html language=enus -->
## TOPIC 00108: Switches

- bundle_id: `ni-daqmx`
- source_path: `switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/switches.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information specific to switch devices about API support and switching capacity, including switching voltage, switching current, and switching power.

### Switches

This section contains information specific to switch devices about API support and switching capacity, including switching voltage, switching current, and switching power.

- [API Support for Switch Modules](switchdapisupport.html#GUID-DD7ADD5E-23CD-4C72-8C4E-6B6A57748B6C)
- [Switching Capacity](switchcapacity.html)

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=switchpower.html language=enus -->
## TOPIC 00109: Switching Power

- bundle_id: `ni-daqmx`
- source_path: `switchpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/switchpower.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching power is the limit on the combined open-contact voltage and closed-contact current of a signal in the switch. Switching Power = Switching Voltage * Switching Current Switching high-power signals causes high-energy arcing at the electromechanical contacts during actuation, reducing the usef

### Switching Power

*Switching power* is the limit on the combined open-contact voltage and closed-contact current of a signal in the switch.

Switching Power = Switching Voltage * Switching Current

Switching high-power signals causes high-energy arcing at the electromechanical contacts during actuation, reducing the useful life of the switch.

Parent topic:

Switching Capacity

<!--NI_TOPIC bundle=ni-daqmx path=switchvoltage.html language=enus -->
## TOPIC 00110: Switching Voltage

- bundle_id: `ni-daqmx`
- source_path: `switchvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/switchvoltage.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching voltage refers to the maximum signal voltage that the switch module can safely maintain. Switching voltage is defined from channel-to-ground and from channel-to-channel. Channel-to-ground is the voltage potential between the signal line and the grounded chassis. Channel-to-channel is the v

### Switching Voltage

*Switching voltage* refers to the maximum signal voltage that the switch module can safely maintain. Switching voltage is defined from channel-to-ground and from channel-to-channel. Channel-to-ground is the voltage potential between the signal line and the grounded chassis. Channel-to-channel is the voltage potential between any pair of signal lines within the module. This voltage includes voltages across open relay contacts, as well as voltages between adjacent connection terminals.

Note

rms

NI Switches Getting Started Guide

Parent topic:

Switching Capacity

<!--NI_TOPIC bundle=ni-daqmx path=synccounters.html language=enus -->
## TOPIC 00111: Counter Synchronization

- bundle_id: `ni-daqmx`
- source_path: `synccounters.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/synccounters.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: You cannot synchronize counter input applications using implicit timing in the same sense as analog input or output applications. These types of counter input applications cannot be programmed to make their measurements at the same time because the signals being measured themselves determine when th

### Counter Synchronization

You cannot synchronize counter input applications using implicit timing in the same sense as analog input or output applications. These types of counter input applications cannot be programmed to make their measurements at the same time because the signals being measured themselves determine when the measurements are made, and there is no reason to set up multiple devices to measure the same signal. You also cannot use Start Triggers for these applications.

You can, however, ensure that all counters are using the same timebase for their input measurements by sharing the CI Counter Timebase signal. Program all devices to use the same signal (usually the 20MHzTimebase from one of the devices) as their CI Counter Timebase. More generally, one device can be queried for its CI Counter Timebase source and that terminal can be set as the source of the CI Counter Timebase for the other devices.

To synchronize Sample Clock-timed buffered counter input applications, use Sample Clock synchronization. The Sample Clock must be externally supplied to one of your devices. The other synchronized devices are programmed to use as their Sample Clock the CtrnGate signal, where n is the number of the counter.

To synchronize pulse generation counter output applications, share the CO Counter Timebase and Start Trigger signal. Program all devices to use the same signal (usually the 20MHzTimebase from one of the devices) as their CO Counter Timebase. More generally, one device can be queried for its CO Counter Timebase source and that terminal can be set as the source of the CO Counter Timebase for the other devices. Program all devices to use the same signal as their Digital Edge Start Trigger. This is typically the CtrnGate signal from one of the devices, where n is the number of the counter.

Parent topic:

Synchronization

Related concepts:

- Sample Clock Synchronization

<!--NI_TOPIC bundle=ni-daqmx path=synchrontypes.html language=enus -->
## TOPIC 00112: Types of Synchronization, Lockstep and Handshaked

- bundle_id: `ni-daqmx`
- source_path: `synchrontypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/synchrontypes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Lockstep synchronization involves two or more similar devices sharing the same timing and triggering and essentially acting as a single device. Sharing a sample clock between analog input and analog output operations on a single device is also considered lockstep synchronization. The goal of lockste

### Types of Synchronization, Lockstep and Handshaked

Lockstep synchronization involves two or more similar devices sharing the same timing and triggering and essentially acting as a single device. Sharing a sample clock between analog input and analog output operations on a single device is also considered lockstep synchronization. The goal of lockstep synchronization is to eliminate skew as much as possible. In lockstep synchronization, clocks and triggers are typically shared.

Handshaked synchronization (or stimulus/response) is two or more devices acting in sequence. In handshaked synchronization, triggers and events are typically shared. A simplified DAC test is an example of this type of synchronization. A digital device sends a digital pattern to the DAC and a signal causing the DAC to create a voltage in response to this pattern. At the same time or soon after, the digital device sends a signal to a DMM causing the DMM to measure the voltage output by the DAC. When the DMM has finished the measurement, it sends a signal back to the digital device causing the digital device to send the next pattern to the DAC.

In lockstep synchronization, the operations involved all use a clock or trigger for the same purpose. In handshaked synchronization, the roles of the trigger or event are typically reversed between the operations (for example a Sample Complete Event from a DMM is used as a Sample Clock by the digital device that receives it).

Parent topic:

Synchronization

Related concepts:

- Skew

<!--NI_TOPIC bundle=ni-daqmx path=synclocklostdetection.html language=enus -->
## TOPIC 00113: Sync Lock Lost Detection

- bundle_id: `ni-daqmx`
- source_path: `synclocklostdetection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/synclocklostdetection.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Network-synchronized devices that are part of a time network are synchronized to a grand master. When the network conditions cause a chassis to lose synchronization, any task running on that chassis will error. This can be configured in a task through the DAQmx Channel Property SyncUnlockBehavior, w

### Sync Lock Lost Detection

Network-synchronized devices that are part of a time network are synchronized to a grand master. When the network conditions cause a chassis to lose synchronization, any task running on that chassis will error.

This can be configured in a task through the DAQmx Channel Property SyncUnlockBehavior, which defaults to StopTaskAndError, and can be disabled by setting the value to IgnoreLostSyncLock. If IgnoreLostSyncLock is configured, the task will keep running regardless of synchronization status. To query the state on a given task, the DAQmx Read or Write Property Sync.UnlockedChansExist returns whether the target is currently locked to the grand master. Sync.UnlockedChans returns the channels from the devices in an unlocked target.

- cDAQ-9185, and
 9189.
- FD-11601, FD-11603,
 FD-11605, FD-11613, FD-11614, FD-11634, and FD-11637.
- cRIO-9040, 9041,
 9042, 9043, 9045, 9046, 9047, 9048, 9049, 9053, 9054, 9055,
 9056, 9057, and 9058.
- sbRIO-9603, 9608,
 9609, 9628, 9629, and 9638.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=thermocouples.html language=enus -->
## TOPIC 00114: Thermocouples

- bundle_id: `ni-daqmx`
- source_path: `thermocouples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/thermocouples.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thermocouples are the most commonly used temperature sensors. A thermocouple forms when two dissimilar metals touch. The contact point produces a small open-circuit voltage that corresponds to temperature. This thermoelectric voltage is known as Seebeck voltage and is nonlinear with respect to tempe

### Thermocouples

Thermocouples are the most commonly used temperature sensors.

[IMAGE alt='image' src='GUID-2B1354B0-FFB1-4B41-99F8-31E536E53486-a5.svg']

A thermocouple forms when two dissimilar metals touch. The contact point produces a small
 open-circuit voltage that corresponds to temperature. This thermoelectric voltage is
 known as Seebeck voltage and is nonlinear with respect to temperature. Thermocouples
 require signal conditioning.

Thermocouple types differ in composition and accurate range:

| Thermocouple Type | Positive Conductor | Negative Conductor | Temperature Range (°C) for Polynomial Coefficients or for Table Conversion | Temperature Range (°C) for Inverse Polynomial Coefficients |
| --- | --- | --- | --- | --- |
| J | Iron | Constantan | -210 to 1200 | -210 to 1200 |
| K | Chromel | Alumel | -270 to 1372 | -200 to 1372 |
| N | Nicrosil | Nisil | -270 to 1300 | -200 to 1300 |
| R | Platinum-13% Rhodium | Platinum | -50 to 1768 | -50 to 1768 |
| S | Platinum-10% Rhodium | Platinum | -50 to 1768 | -50 to 1768 |
| T | Copper | Constantan | -270 to 400 | -200 to 400 |
| B | Platinum | Rhodium | 0 to 1820 | 250 to 1820 |
| E | Chromel | Constantan | -270 to 1000 | -200 to 1000 |

Use the temperature ranges for polynomial coefficients when converting temperature to
 voltage. For most thermocouples, the equation used for converting temperature to voltage
 is the following:

V

R

=

∑

i

=

0

n

c

i

(

t

90

)

i

- V R is the voltage ratio.
- t 90 is the temperature in degrees Celsius.
- c i is the coefficient.

Use the temperature ranges for inverse polynomial coefficients when converting voltage to
 temperature. For most thermocouples, the equation for converting voltage to temperature
 is the following:

t

90

=

∑

i

=

0

n

D

i

(

E

)

i

- t 90 is the temperature in degrees Celsius.
- E is the voltage in millivolts.
- D i is the coefficient.

Note

Parent topic:

Overview of Temperature Sensor Types

Related concepts:

- Signal Conditioning Requirements for Thermocouples

Related information:

- nist.gov

<!--NI_TOPIC bundle=ni-daqmx path=timctrlloops.html language=enus -->
## TOPIC 00115: Timing Control Loops

- bundle_id: `ni-daqmx`
- source_path: `timctrlloops.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timctrlloops.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can time control loops using software timing or hardware timing. You can also use the Timed Loop structure. For software timing, the software and operating system determines the rate at which the loop executes. Software timing is not deterministic. Controlling a while loop and using the Wait Unt

### Timing Control Loops

You can time control loops using software timing or hardware timing. You can also use the Timed Loop structure.

For software timing, the software and operating system determines the rate at which the loop executes. Software timing is not deterministic. Controlling a while loop and using the Wait Until Next ms Multiple VI to handle timing is an example of a software-timed loop. Hardware timing uses the DAQ device internal clock or an external clock to control when a read executes within a loop. The example block diagram shown in 
 *Control Loops* in the Common Applications section uses hardware timing.

The Timed Loop structure is hardware timed. It is ideal for multirate applications. By default, the Timed Loop uses the 1 kHz clock of the Windows operating system as its timing source. Refer to your 
 *LabVIEW Help* for more information about the Timed Loop structure.

Parent topic:

Control in NI-DAQmx

Related concepts:

- Real Time

<!--NI_TOPIC bundle=ni-daqmx path=time-based-features.html language=enus -->
## TOPIC 00116: Time-Based Features for Network-Synchronized Devices

- bundle_id: `ni-daqmx`
- source_path: `time-based-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/time-based-features.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Network-synchronized devices feature automatic network-based synchronization when connected together across a compatible network. When these devices are synchronized across a compatible network all device timebases, time triggers, and timestamps will automatically be synchronized. Network-synchroniz

### Time-Based Features for Network-Synchronized Devices

Network-synchronized devices feature automatic network-based synchronization when connected together across a compatible network. When these devices are synchronized across a compatible network all device timebases, time triggers, and timestamps will automatically be synchronized.

- cDAQ-9185, and
 9189.
- FD-11601, FD-11603,
 FD-11605, FD-11613, FD-11614, FD-11634, and FD-11637.
- cRIO-9040, 9041,
 9042, 9043, 9045, 9046, 9047, 9048, 9049, 9053, 9054, 9055,
 9056, 9057, and 9058.
- sbRIO-9603, 9608,
 9609, 9628, 9629, and 9638.

The cDAQ-9185/9189 are tethered chassis that can be daisy-chained to each other or connected to external networks that support 802.1AS synchronization. To learn about this feature, refer to the 
 *cDAQ-9185/9189 User Manual* and the related concepts in this help.

The FD-116xx are devices that can be daisy-chained to each other and connected to external networks that support 802.1AS synchronization. To learn about this feature, refer to your 
 *FieldDAQ User Guide* and the related concepts in this help.

Parent topic:

NI-DAQmx Device Considerations

Related concepts:

- Time Triggering
- C Series Multichassis Device Tasks
- Sync Lock Lost Detection
- Timestamps

<!--NI_TOPIC bundle=ni-daqmx path=time-triggering.html language=enus -->
## TOPIC 00117: Time Triggering

- bundle_id: `ni-daqmx`
- source_path: `time-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/time-triggering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: For devices that support it, a time trigger starts an acquisition or measurement at a specific time. If the specified time has already elapsed, you will get an error message indicating the time has already elapsed. The timestamp timescale can be configured using the Timestamp.Timescale attribute/pro

### Time Triggering

For devices that support it, a time trigger starts an acquisition or measurement at a
 specific time. If the specified time has already elapsed, you will get an error message
 indicating the time has already elapsed.

The timestamp timescale can be configured using the Timestamp.Timescale attribute/property. Time triggers and timestamps can be specified in I/O Device Time or Host Time, depending on the needs of your application.

- I/O Device Time 
 Shared by all network-synchronized devices on your 802.1AS subnet. I/O Device Time is
 most useful for synchronizing events across multiple chassis or correlating timestamps
 from multiple chassis, because even though it may be in an obscure time scale (for
 example, related to a point in the distant past, such as the Linux 1970 epoch), it removes
 other sources of skew related to Windows system time or other systems that are not
 network-synchronized to the same 802.1AS subnet. In that way, the I/O Device Time provides
 the best precision and relative accuracy but may reduce usability if it is not correlated
 to a recognizable global time. I/O Device Time also has the advantage of being
 monotonically increasing, so time triggers and timestamps spread across multiple devices
 or tasks accurately maintain their offsets from each other.
- Host Time 
 The timescale your PC or NI Linux Real-Time controller uses. In cases where the NI Linux Real-Time controller is the Grand Master of your 802.1AS subnet, Host Time and I/O Device Time are the same. However, Host Time is typically synchronized to a local Real Time Clock or a Network Time Protocol server, and it is usually traceable to global time. Using Host Time is more intuitive because triggers and timestamps on the chassis are specified in times that are easily correlated to your local system time. However, this usability comes at the cost of reduced relative accuracy between time triggers and timestamps that are spread across multiple devices or tasks, because using the calculated offset between the two timescales is not as accurate as using I/O Device Time directly. To help account for this loss of accuracy in a specific and common use-case, NI-DAQmx guarantees that two events that are scheduled for the same Host Time are guaranteed to start at the same I/O Device Time, preserving precise synchronization between chassis. 
 Whether a device supports time triggers or not can be queried using TimeTrigSupported attribute/property. 
 Network-synchronized devices include the
 cDAQ-9185, 9189; FD-11601, FD-11603, FD-11605, FD-11613, FD-11614,
 FD-11634, FD-11637; cRIO-9040, 9041, 9042, 9043, 9045, 9046, 9047,
 9048, 9049, 9053, 9054, 9055, 9056, 9057, 9058; and sbRIO-9603,
 9608, 9609, 9628, 9629, and 9638.

Parent topic:

Trigger Types

Related concepts:

- Time-Based Features for Network-Synchronized Devices

<!--NI_TOPIC bundle=ni-daqmx path=timestamps.html language=enus -->
## TOPIC 00118: Timestamps

- bundle_id: `ni-daqmx`
- source_path: `timestamps.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timestamps.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Network-synchronized devices support four timestamp resources that allow for timestamping the first sample clock, start trigger, arm start trigger (counters only) or reference trigger. The timestamp resources will be used to provide an accurate t0 for waveform reads with timed acquisitions that will

### Timestamps

Network-synchronized devices support four timestamp resources that allow for timestamping the first sample clock, start trigger, arm start trigger (counters only) or reference trigger.

The timestamp resources will be used to provide an accurate t0 for waveform reads with timed acquisitions that will correspond to the first sample clock for Analog Input and Digital Input tasks. Therefore, the first sample timestamp is enabled by default for these types of tasks.

The timestamp timescale can be configured using the Timestamp.Timescale attribute/property. Time triggers and timestamps can be specified in I/O Device Time or Host Time, depending on the needs of your application.

- I/O Device Time 
 Shared by all network-synchronized devices on your 802.1AS subnet. I/O Device Time is most useful for synchronizing events across multiple chassis or correlating timestamps from multiple chassis, because even though it may be in an obscure time scale (for example, related to a point in the distant past, such as the Linux 1970 epoch), it removes other sources of skew related to Windows system time or other systems that are not network-synchronized to the same 802.1AS subnet. In that way, it provides best time trigger and timestamp accuracy but may reduce usability if it is not correlated to a recognizable global time. I/O Device Time also has the advantage of being monotonically increasing, so time triggers and timestamps spread across multiple devices or tasks accurately maintain their offsets from each other.
- Host Time 
 The timescale your PC or NI Linux Real-Time controller uses. In cases where the NI Linux Real-Time controller is the Grand Master of your 802.1AS subnet, Host Time and I/O Device Time are the same. However, Host Time is typically synchronized to a local Real Time Clock or a Network Time Protocol server, and it is usually traceable to global time. Using Host Time is more intuitive because triggers and timestamps on the chassis are specified in times that are easily correlated to your local system time. However, this usability comes at the cost of reduced relative accuracy between time triggers and timestamps that are spread across multiple devices or tasks, because using the calculated offset between the two timescales is not as accurate as using I/O Device Time directly. To help account for this loss of accuracy in a specific and common use-case, NI-DAQmx guarantees that two events that are scheduled for the same Host Time are guaranteed to start at the same I/O Device Time, preserving precise synchronization between chassis.

The number of available timestamp resources can be queried using the NumTimestampEngines attribute/property.

- cDAQ-9185, and
 9189.
- FD-11601, FD-11603,
 FD-11605, FD-11613, FD-11614, FD-11634, and FD-11637.
- cRIO-9040, 9041,
 9042, 9043, 9045, 9046, 9047, 9048, 9049, 9053, 9054, 9055,
 9056, 9057, and 9058.
- sbRIO-9603, 9608,
 9609, 9628, 9629, and 9638.

Parent topic:

Timing

Related concepts:

- First Sample Timestamp
- Using Wait for Valid Timestamp VI
- Sync Lock Lost Detection
- Triggering
- Time-Based Features for Network-Synchronized Devices

<!--NI_TOPIC bundle=ni-daqmx path=timetrig.html language=enus -->
## TOPIC 00119: Timing and Triggering

- bundle_id: `ni-daqmx`
- source_path: `timetrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timetrig.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Timing and triggering are important in NI-DAQmx. The clocks section explains clocks and handshaking. The triggering section goes over the triggers—such as a Start Trigger and a Reference Trigger—and common trigger types—such as an analog edge trigger or a digital edge trigger.

### Timing and Triggering

Timing and triggering are important in NI-DAQmx. The clocks section explains clocks and handshaking. The triggering section goes over the triggers—such as a Start Trigger and a Reference Trigger—and common trigger types—such as an analog edge trigger or a digital edge trigger.

Parent topic:

NI-DAQmx Key Concepts

Related concepts:

- Clocks
- Triggering

<!--NI_TOPIC bundle=ni-daqmx path=timetrigsimdev.html language=enus -->
## TOPIC 00120: Timing and Triggering with NI-DAQmx Simulated Devices

- bundle_id: `ni-daqmx`
- source_path: `timetrigsimdev.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timetrigsimdev.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: With NI-DAQmx simulated devices, the following timing and triggering considerations exist: NI-DAQmx simulated devices simulate timing for continuous analog input, digital input, and all output tasks. Timing is not simulated for counter tasks. NI-DAQmx simulated devices do not cause a timed loop to e

### Timing and Triggering with NI-DAQmx Simulated Devices

With NI-DAQmx simulated devices, the following timing and triggering considerations exist:

- NI-DAQmx simulated devices simulate timing for continuous analog input, digital input, and all output tasks. Timing is not simulated for counter tasks.
- NI-DAQmx simulated devices do not cause a timed loop to execute.
- NI-DAQmx simulated devices support software events. However, events that rely on the hardware, such as a sample clock event, are not supported.
- Triggers always occur immediately.
- Watchdog timers do not expire.

Parent topic:

NI-DAQmx Simulated Devices

<!--NI_TOPIC bundle=ni-daqmx path=timing-fielddaq.html language=enus -->
## TOPIC 00121: Timing Considerations for FieldDAQ

- bundle_id: `ni-daqmx`
- source_path: `timing-fielddaq.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timing-fielddaq.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sampling Rate Considerations For the FD-11613 and FD-11614, if the sampling rate of a hardware-timed acquisition exceeds the maximum sampling rate of the module, the most recently acquired sample may be read multiple times and no warning or error is generated. Exceeding the maximum sampling rate of

### Timing Considerations for FieldDAQ

Parent topic:

Timing

#### Sampling Rate Considerations

For the FD-11613 and FD-11614, if the sampling rate of a hardware-timed acquisition exceeds the maximum sampling rate of the module, the most recently acquired sample may be read multiple times and no warning or error is generated. Exceeding the maximum sampling rate of other devices in the same task generates warnings or errors. The first sample of a hardware-timed acquisition with these devices is sampled when the task is committed. Software-timed acquisitions with these devices always wait for a new sample to be acquired.

The FD-11601, FD-11603, FD-11605, FD-11634, and FD-11637 have a user-selectable sample clock timebase. You can set the sample clock timebase with the SampClk.Timebase.Src attribute/property. The FD-11601, FD-11603, FD-11605, FD-11634, and FD-11637 also have both a maximum and a minimum sampling rate. Refer to your device documentation to determine the sampling rate range and the user-selectable timebase for your FieldDAQ device.

If you do not specify a sample clock timebase source or rate, NI-DAQmx auto-selects the sample clock timebase with the closest sampling rate greater than or equal to your requested sampling rate. If you do specify the sample clock timebase source or rate, NI-DAQmx respects the setting and only chooses a sampling rate supported with that sample clock timebase.

#### On-Demand Timing

The FD-11601, FD-11603, FD-11605, FD-11634, and FD-11637 do not support the on-demand timing type.

#### Configurable Timing for FD-11613 and FD-11614

The FD-11613 and FD-11614 support the following timing modes:

| High Resolution | Optimizes accuracy and noise and rejects power line frequencies. |
| --- | --- |
| Best 50 Hz Rejection | Optimizes 50 Hz noise rejection. |
| Best 60 Hz Rejection | Optimizes 60 Hz noise rejection. |
| High Speed | Optimizes sample rate and signal bandwidth. |
| Automatic | Uses the most appropriate supported timing mode based on the Sample Clock Rate. |

Use the AI.ADCTimingMode attribute/property to configure timing on the FD-11613 and FD-11614. This attribute/property is set by default to Automatic, which causes the module to sample with the highest resolution timing mode that is faster than the rate you specified.

<!--NI_TOPIC bundle=ni-daqmx path=timing.html language=enus -->
## TOPIC 00122: Timing

- bundle_id: `ni-daqmx`
- source_path: `timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timing.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about timing for AO Series, C Series, DSA, E Series, FieldDAQ, M Series USB, NI ELVIS II Family, S Series, and SC Express devices.

### Timing

This section contains information about timing for AO Series, C Series, DSA, E Series, FieldDAQ, M Series USB, NI ELVIS II Family, S Series, and SC Express devices.

- [Timing Considerations for AO Series Devices](timingconsidaoseries.html)
- [Timing Considerations for C Series Devices](cdaqtimingconsiderations.html#GUID-F736BBD7-85E8-46B3-AC09-C607256B9875)
- [Timing Considerations for DSA Devices](timingconsiddsaseries.html)
- [Timing Considerations for E Series Devices](timingconsideseries.html)
- [Timing Considerations for FieldDAQ](timing-fielddaq.html#GUID-344EC3F9-21CC-4B6A-BD16-E85D1BAAA5A0)
- [Hardware-Timed Non-Buffered Sample Mode](hwtimednonbuffsamp.html)
- [Timing Considerations with NI ELVIS II Family and M Series USB Devices](timingmusb.html)
- [Non-Buffered Change Detection](nonbuffchangedet.html)
- [Timing Considerations for S Series](timingconsidsseries.html#GUID-F28F0CBF-FF31-45A4-BC86-2A092B2FAE80)
- [Timing Considerations for SC Express Devices](scexpresstimingconsid.html#GUID-0C83CF89-9B33-4146-9330-2FDC70166E63)
- [Timing Considerations with Standalone NI CompactDAQ Systems](timingconsiderationsstandalonecompactdaqsystem.html)
- [Sample Rate Considerations](smplrateconsid.html)
- [Sample Clock-Timed Pulse Train Generation](smpclkcountertime.html)
- [Device-Specific Sampling Methods](simvsmultisamp.html)
- [Timing Considerations for X Series and NI mioDAQ Devices](timingconsidxseries.html)
- [Timestamps](timestamps.html) Network-synchronized devices support four timestamp resources that allow for timestamping the first sample clock, start trigger, arm start trigger (counters only) or reference trigger.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=timingconsidaoseries.html language=enus -->
## TOPIC 00123: Timing Considerations for AO Series Devices

- bundle_id: `ni-daqmx`
- source_path: `timingconsidaoseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsidaoseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using an external ao/SampleClock for finite generations, you need to provide one more sample clock pulse than the number of samples in the generation. The Wait Until Done function/VI uses the extra sample clock to indicate the task is complete. For example, if you want to generate 1000 samples

### Timing Considerations for AO Series Devices

When using an external ao/SampleClock for finite generations, you need to provide one more sample clock pulse than the number of samples in the generation. The Wait Until Done function/VI uses the extra sample clock to indicate the task is complete. For example, if you want to generate 1000 samples using an external sample clock, the first 1000 samples clocks you provide generates all of the samples, but you need to provide 1001 sample clock pulses for the Wait Until Done function/VI to indicate the task is done. If you are trying to synchronize an analog output generation with another acquisition or generation by sharing a common clock, use the ao/SampleClock as the master clock, or key off of the generation or acquisition providing the master clock to determine when the generation is complete.

Static AO devices, such as the NI 6703 and NI 6704, do not have hardware timing and have multiplexed output. Refer to your device documentation for specifics concerning your device.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx path=timingconsiddsaseries.html language=enus -->
## TOPIC 00124: Timing Considerations for DSA Devices

- bundle_id: `ni-daqmx`
- source_path: `timingconsiddsaseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsiddsaseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Supported Sampling Rates Unlike some other DAQmx devices, DSA devices have both a maximum and a minimum sampling rate. Refer to the specifications for your device to determine the sampling rate range. Other DSA Timing Considerations DSA devices do not support the on-demand timing type. All DSA acqui

### Timing Considerations for DSA Devices

- Supported Sampling Rates 
 Unlike some other DAQmx devices, DSA devices have both a maximum and a minimum sampling rate. Refer to the specifications for your device to determine the sampling rate range.
- Other DSA Timing Considerations 
 DSA devices do not support the on-demand timing type. All DSA acquisitions and generations require hardware timing from a steady clock. The NI 4464, 4480, and 4481 are an exception. The NI 4464, 4480, and 4481 support on-demand timing type. DSA devices do not support external clocking from arbitrary external signal sources such as encoders and tachometers. The PFI lines on DSA devices cannot accept external clocks. You can program a DSA device to use an external clock only when it is a slave in multi-device synchronized system. Refer to Synchronizing DSA Devices for more details.

Parent topic:

Timing

Related concepts:

- Synchronizing DSA Devices

<!--NI_TOPIC bundle=ni-daqmx path=timingconsiderationsstandalonecompactdaqsystem.html language=enus -->
## TOPIC 00125: Timing Considerations with Standalone NI CompactDAQ Systems

- bundle_id: `ni-daqmx`
- source_path: `timingconsiderationsstandalonecompactdaqsystem.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsiderationsstandalonecompactdaqsystem.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: While Standalone NI CompactDAQ systems, such as the NI cDAQ-9132, 9133, 9134, 9135, 9136, and 9137 can be programmed with and run the LabVIEW Real-Time Module, the hardware and software architecture is optimized for data logging applications rather than for real-time control applications. This means

### Timing Considerations with Standalone NI CompactDAQ Systems

While Standalone NI CompactDAQ systems, such as the NI cDAQ-9132, 9133, 9134, 9135, 9136, and 9137 can be programmed with and run the LabVIEW Real-Time Module, the hardware and software architecture is optimized for data logging applications rather than for real-time control applications. This means that Standalone NI CompactDAQ systems are ideal for streaming many channels to or from disk for extended periods of time, but should not be used for applications that require hard determinism. The Standalone NI CompactDAQ hardware and software architectures are not designed for deterministic operation.

Note

- Standalone NI CompactDAQ systems do not support hardware-timed single-point sample mode or hardware-timed non-buffered sample mode.
- Standalone NI CompactDAQ systems do not support DAQ events as timing sources for time loops.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx path=timingconsideseries.html language=enus -->
## TOPIC 00126: Timing Considerations for E Series Devices

- bundle_id: `ni-daqmx`
- source_path: `timingconsideseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsideseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Special timing considerations when using E Series devices: ai/ConvertClock When using the ai/ConvertClock as the source of a route, one extra convert pulse is generated than you might expect. For example, if you perform a finite acquisition of 100 samples with four channels, you see 401 convert puls

### Timing Considerations for E Series Devices

Special timing considerations when using E Series devices:

- ai/ConvertClock 
 When using the ai/ConvertClock as the source of a route, one extra convert pulse is generated than you might expect. For example, if you perform a finite acquisition of 100 samples with four channels, you see 401 convert pulses instead of 400. This extra convert pulse is necessary to set up the configuration memory in hardware and occurs as the task transitions to the committed state.
- ao/SampleClock 
 When using an external ao/SampleClock for finite generations, you need to provide one extra sample clock pulse than the number of samples in the generation for the Wait Until Done function/VI to indicate the task is complete. For example, if you want to generate 1000 samples using an external sample clock, you need to provide 1001 sample clock pulses or the Wait Until Done function/VI never indicates the task is done. All of the samples are generated, but the analog output timing engine needs one additional clock pulse to indicate the generation is complete. If you are trying to synchronize an analog output generation with another acquisition or generation by sharing a common clock, use the ao/SampleClock as the master clock or key off of the generation or acquisition providing the master clock to determine when the generation is complete.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx path=timingconsidsseries.html language=enus -->
## TOPIC 00127: Timing Considerations for S Series

- bundle_id: `ni-daqmx`
- source_path: `timingconsidsseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsidsseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog Input with Pipelined ADCs Not all S Series devices have pipelined ADCs. Refer to the specifications for your device to determine if your device contains pipelined ADCs. Many S Series devices have pipelined ADCs with an intrinsic pipeline depth. This pipelining allows the device to sample at h

### Timing Considerations for S Series

Parent topic:

Timing

#### Analog Input with Pipelined ADCs

Note

Many S Series devices have pipelined ADCs with an intrinsic pipeline depth. This pipelining allows the device to sample at higher rates, but it also has other consequences on the timing requirements for the device. S Series devices, except for the NI 6143, do not support AI hardware-timed single-point sample mode. Since the data needs to travel through the pipeline before it can be read, the data being read is always pipeline-depth points old. For instance, if the pipeline depth for a device is three, the first sample is acquired on clock tick 1, but it is not available for reading until clock tick 4. Following this logic, you must supply pipeline-depth extra clock pulses for a finite acquisition to flush the pipeline. Continuing with the previous example, if the pipeline depth is three and you want to acquire 1000 samples, you need to generate 1003 sample clock pulses. If you are using the onboard sample clock, NI-DAQmx automatically generates the appropriate number of sample clock pulses. However, when using an external sample clock or when synchronizing devices, you need to ensure you supply the appropriate number of sample clock pulses.

There is also a finite amount of time a sample can be held in the pipeline before it starts to degrade and lose measurement accuracy. This time limit imposes a minimum sampling rate that must be met to achieve the measurement accuracy specified for the device. Although you can sample slower than this minimum recommend sampling rate, the accuracy specifications for the device are not guaranteed. Refer to the specifications for your device to determine the recommended minimum sampling rate.

This degradation of samples in the pipeline also affects on-demand single-point acquisitions and acquisitions that use a Pause Trigger. For on-demand single-point acquisitions, NI-DAQmx generates multiple sample clocks at the maximum sample rate of the device for each sample that is read. For S Series devices with a pipelined ADC, the number of sample clocks generated is equal to the pipeline depth plus one. For S Series devices that do not have a pipelined ADC, two sample clock pulses are generated for each point. This means that if you export the sample clock while doing an on-demand single-point acquisition, you get more sample clock pulses than data points. NI-DAQmx then throws away all points except the data point that corresponds to the first sample clock pulse. This ensures the data returned is always valid data. For acquisitions that use a Pause Trigger, the trigger could invalidate the samples in the pipeline if the trigger is asserted longer than the pipeline depth divided by the minimum sampling rate. For instance, if the device has a pipeline depth of three and a minimum sampling rate of 1000 samples per second, data should not sit in the pipeline for more than 3 ms. This gives up to a maximum of 3 ms for the Pause Trigger to remain asserted and three sample clocks to be detected before the data in the pipeline deteriorates past specifications. In the case of a Pause Trigger, NI-DAQmx does not detect or throw out any invalid samples. You must detect this situation and deal with any invalid samples as appropriate.

#### Analog Output

When using an external ao/SampleClock for finite generations, you need to provide one more sample clock pulse than the number of samples in the generation for the Wait Until Done function/VI to indicate the task is complete. For example, if you want to generate 1000 samples using an external sample clock, you need to provide 1001 sample clock pulses, or the Wait Until Done function/VI never indicates the task is done. All of the samples are generated, but the analog output timing engine needs one additional clock pulse to indicate the generation is complete. If you are trying to synchronize an analog output generation with another acquisition or generation by sharing a common clock, use the ao/SampleClock as the master clock, or key off of the generation or acquisition providing the master clock to determine when the generation is complete.

Note

<!--NI_TOPIC bundle=ni-daqmx path=timingconsidxseries.html language=enus -->
## TOPIC 00128: Timing Considerations for X Series and NI mioDAQ Devices

- bundle_id: `ni-daqmx`
- source_path: `timingconsidxseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingconsidxseries.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: X Series USB and NI mioDAQ devices do not support hardware-timed single-point sample mode or Wait for Next Sample Clock.

### Timing Considerations for X Series and NI mioDAQ
 Devices

X Series USB and NI mioDAQ devices
 do not support hardware-timed single-point sample mode or Wait for Next Sample Clock.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx path=timingenginehsdio.html language=enus -->
## TOPIC 00129: NI 6533, 6534 Timing Engines

- bundle_id: `ni-daqmx`
- source_path: `timingenginehsdio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingenginehsdio.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI 6533 and 6534 devices provide two timing engines for digital I/O. Multiple timing engines allow those devices to run up to two tasks simultaneously, each using independent timing and triggering configurations. Also, each timing engine uses different lines for handshaking and burst handshaking. By

### NI 6533, 6534 Timing Engines

NI 6533 and 6534 devices provide two timing engines for digital I/O. Multiple timing engines allow those devices to run up to two tasks simultaneously, each using independent timing and triggering configurations. Also, each timing engine uses different lines for handshaking and burst handshaking.

By default, NI-DAQmx assigns a timing engine based on the ports used in the task. Refer to device documentation to determine which ports use which timing engine. Use the DAQmx Timing property/attribute SampTimingEngine to specify the timing engine to use or to determine which timing engine NI-DAQmx automatically selected.

The SampTimingEngine property/attribute is an integer value corresponding to one of the two timing engines available on the device:

| SampTimingEngine Value | Timing Engine Used |
| --- | --- |
| 0 | dig0 |
| 1 | dig1 |

On NI 6533 and 6534 devices, the Sample Clock and Sample Clock Timebase, as well as the Start and Reference triggers, exist on each timing engine. Therefore, the names of the output terminals for those signals include the associated timing engine.

Parent topic:

Multiple Timing Engines

Related concepts:

- Timing Engines
- Handshake Timing Defaults
- Burst Handshaking Timing Defaults for NI 653x Devices
- Syntax for Terminal Names
- Terminals

<!--NI_TOPIC bundle=ni-daqmx path=timingenginemio.html language=enus -->
## TOPIC 00130: cDAQ-91xx and TestScale Chassis Timing Engines

- bundle_id: `ni-daqmx`
- source_path: `timingenginemio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingenginemio.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The cDAQ-91xxcDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174, 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and 9189 or TestScaleTS-15000 and TS-15010 chassis provide three timing engines for analog input. Multiple timing engines allow those chassis to run up to three analog input task

### cDAQ-91*xx* and TestScale Chassis Timing Engines

The cDAQ-91xx<sup>1</sup> cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189
 or TestScale<sup>2</sup> TS-15000 and TS-15010 chassis provide
 three timing engines for analog input. Multiple timing engines allow those chassis to run up
 to three analog input tasks simultaneously, each using independent timing and triggering
 configurations.

By default, NI-DAQmx automatically selects an available timing engine when reserving the task. Use the DAQmx Timing attribute/property SampTimingEngine to specify the timing engine to use or to determine which timing engine NI-DAQmx automatically selected.

Note

The SampTimingEngine attribute/property is an integer value corresponding to one of the three analog input timing engines available on the chassis:

| SampTimingEngine Value | Timing Engine Used |
| --- | --- |
| 0 | te0 |
| 1 | te1 |
| 2 | ai |

xx

[3]

3

cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189

[4]

4

TS-15000 and TS-15010

Terminal

Note

#### Counter Input Modules

The NI 9361 can also use te0 and te1.

Parent topic:

Multiple Timing Engines

Related concepts:

- Timing Engines
- Reserved State
- Syntax for Terminal Names
- Terminals

<sup>1</sup> cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189

<sup>2</sup> TS-15000 and TS-15010

[<sup>3</sup>](#note_ref-d7065e124) cDAQ-9132, 9133, 9134, 9135, 9136, 9137, 9173, 9174,
 9177, 9178, 9179, 9183, 9184, 9185, 9187, 9188, 9188XT, and
 9189

[<sup>4</sup>](#note_ref-d7065e128) TS-15000 and TS-15010

<!--NI_TOPIC bundle=ni-daqmx path=timingengines.html language=enus -->
## TOPIC 00131: Timing Engines

- bundle_id: `ni-daqmx`
- source_path: `timingengines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingengines.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A timing engine is the circuitry a device uses to control an acquisition or generation. Controlling an acquisition or generation includes: Utilizing timing signals to control when the device acquires or generates each sample. Determining when to start and stop the acquisition or generation, using tr

### Timing Engines

A timing engine is the circuitry a device uses to control an acquisition or generation. Controlling an acquisition or generation includes:

- Utilizing timing signals to control when the device acquires or generates each sample.
- Determining when to start and stop the acquisition or generation, using triggers and other control signals.
- Producing clocks, triggers, and other control signals.
- Routing those signals to other devices or other parts of the same device.

Timing engines for different devices and subsystems provide different functionality. The timing engine for an analog input or output subsystem uses a timebase to produce a Sample Clock. The capabilities of a digital I/O timing engine depend on the device. Some can use change detection and/or handshaking for sample timing, while others can also produce a Sample Clock. Some timing engines cannot produce a Sample Clock, but can perform Sample Clock timing if the clock comes from an external source, such as from another subsystem or from a source external to the device. For example, counters produce no inherent timing signals, but can utilize a Sample Clock from an external source. Some devices can perform Sample Clock timing for digital I/O, but require an external clock.

All timing engines can respond to and route control signals, such as triggers. Not all triggers are supported by all devices and measurement types.

Most devices have a single timing engine per subsystem. When a task reserves resources from a timing engine, another task cannot reserve those same resources. However, another task can use signals routed by that timing engine. For example, a counter task can use the Sample Clock from an analog input task. One task can use the Start Trigger from another task to synchronize when the tasks start. Reserving one part of a timing engine reserves the entire timing engine. For example, if an analog input task uses the Sample Clock from an analog output task, the analog input task must reserve the analog input timing engine to utilize that external Sample Clock. As a result, another task can not use the Sample Clock from the analog input timing engine.

Note

Some devices have multiple timing engines available for some subsystems. Multiple timing engines allow a device to run multiple tasks simultaneously on the same subsystem or to use different terminals for handshaking.

Parent topic:

Timing and Triggering

Related concepts:

- Multiple Timing Engines
- Simultaneous Tasks
- Handshaking Line Configuration

Related reference:

- Sample Clock Timing for Digital I/O

<!--NI_TOPIC bundle=ni-daqmx path=timingmusb.html language=enus -->
## TOPIC 00132: Timing Considerations with NI ELVIS II Family and M Series USB Devices

- bundle_id: `ni-daqmx`
- source_path: `timingmusb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingmusb.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI ELVIS II and M Series USB devices do not support hardware-timed single-point sample mode or Wait for Next Sample Clock. The oscilloscope channels on NI ELVIS II+, scopeCh0 and scopeCh1, support only finite samples mode, not hardware-timed single-point mode or continuous samples mode. The NI ELVIS

### Timing Considerations with NI ELVIS II Family and M Series USB Devices

NI ELVIS II and M Series USB devices do not support hardware-timed single-point sample mode or Wait for Next Sample Clock. The oscilloscope channels on NI ELVIS II+, scopeCh0 and scopeCh1, support only finite samples mode, not hardware-timed single-point mode or continuous samples mode. The NI ELVIS II+ oscilloscope channels also only support the sample clock sample timing type.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx path=timingresponse.html language=enus -->
## TOPIC 00133: Timing Response Modes

- bundle_id: `ni-daqmx`
- source_path: `timingresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/timingresponse.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital I/O and DAQ devices typically use the single-cycle timing response mode, meaning the device responds to an external signal by the next active sample clock edge. Devices that support the pipelined timing response mode, such as the PCIe-6536 and PCIe-6537, can respond to an external signal a f

### Timing Response Modes

Digital I/O and DAQ devices typically use the single-cycle timing response mode, meaning the device responds to an external signal by the next active sample clock edge.

Devices that support the pipelined timing response mode, such as the PCIe-6536 and PCIe-6537, can respond to an external signal a few sample clock edges later. This mode uses a source-synchronous clock scheme, which simultaneously returns the clock and data to the acquiring device. With a source-synchronous data transfer, you can acquire and generate data at much higher rates than with single-cycle timing response mode.

With the pipelined timing response mode, you can configure external sample clocks, but the sample clock must be free-running and started before the task commits. If you export the sample clock, the export occurs during a task commit. As with other events, when the task uncommits, the signal remains exported.

Parent topic:

Timing, Hardware Versus Software

<!--NI_TOPIC bundle=ni-daqmx path=tiophyschans.html language=enus -->
## TOPIC 00134: TIO Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `tiophyschans.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/tiophyschans.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Counter Input and Output TIO devices have up to eight counter/timers referred to by the physical channel names Dev1/ctr0 to Dev1/ctr7. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device. There are four pri

### TIO Physical Channels

Parent topic:

Physical Channels

#### Counter Input and Output

TIO devices have up to eight counter/timers referred to by the physical channel names 
 Dev1/ctr0 to 
 Dev1/ctr7. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device.

There are four primary terminals associated with each TIO counter. These are the terminals used as the SOURCE, GATE, AUX, and OUT functions. NI-DAQmx has default values for these terminals. For counter input tasks, if you know whether your signals provide the SOURCE, GATE, or AUX functions and wire your signal to the default input, you do not have to set the Input Terminal attribute/property.

| Counter | SOURCE Default | GATE Default | AUX Default | OUT Default |
| --- | --- | --- | --- | --- |
| Dev1/ctr0 | PFI 39 | PFI 38 | PFI 37 | PFI 36 |
| Dev1/ctr1 | PFI 35 | PFI 34 | PFI 33 | PFI 32 |
| Dev1/ctr2 | PFI 31 | PFI 30 | PFI 29 | PFI 28 |
| Dev1/ctr3 | PFI 27 | PFI 26 | PFI 25 | PFI 24 |
| Dev1/ctr4 | PFI 23 | PFI 22 | PFI 21 | PFI 20 |
| Dev1/ctr5 | PFI 19 | PFI 18 | PFI 17 | PFI 16 |
| Dev1/ctr6 | PFI 15 | PFI 14 | PFI 13 | PFI 12 |
| Dev1/ctr7 | PFI 11 | PFI 10 | PFI 9 | PFI 8 |

Note

#### Digital Input and Output

NI 661x devices have two ports, port 0 and port 1. Port 0 has 32 lines of digital input and output named 
 Dev1/port0/line0 through 
 Dev1/port0/line31. Port 1 has 8 lines of digital input and output named 
 Dev1/port1/line0 through 
 Dev1/port1/line7. The physical channel Dev1/port0 refers to all 32 lines at once, and the physical channel Dev1/port1 refers to all 8 lines at once. Port 0 can perform hardware-timed and static digital operations, while port 1 can perform only static digital operations.

Port 0 and port 1 can be used as static PFI lines, PFI 0..39. When any of PFI lines 0..39 is used as a digital I/O signal, it uses the physical channel name shown in the following table.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | Dev1/port0/line0 |
| PFI 1 | Dev1/port0/line1 |
| PFI 2 | Dev1/port0/line2 |
| PFI 3 | Dev1/port0/line3 |
| PFI 4 | Dev1/port0/line4 |
| PFI 5 | Dev1/port0/line5 |
| PFI 6 | Dev1/port0/line6 |
| PFI 7 | Dev1/port0/line7 |
| PFI 8 | Dev1/port0/line8 |
| PFI 9 | Dev1/port0/line9 |
| PFI 10 | Dev1/port0/line10 |
| PFI 11 | Dev1/port0/line11 |
| PFI 12 | Dev1/port0/line12 |
| PFI 13 | Dev1/port0/line13 |
| PFI 14 | Dev1/port0/line14 |
| PFI 15 | Dev1/port0/line15 |
| PFI 16 | Dev1/port0/line16 |
| PFI 17 | Dev1/port0/line17 |
| PFI 18 | Dev1/port0/line18 |
| PFI 19 | Dev1/port0/line19 |
| PFI 20 | Dev1/port0/line20 |
| PFI 21 | Dev1/port0/line21 |
| PFI 22 | Dev1/port0/line22 |
| PFI 23 | Dev1/port0/line23 |
| PFI 24 | Dev1/port0/line24 |
| PFI 25 | Dev1/port0/line25 |
| PFI 26 | Dev1/port0/line26 |
| PFI 27 | Dev1/port0/line27 |
| PFI 28 | Dev1/port0/line28 |
| PFI 29 | Dev1/port0/line29 |
| PFI 30 | Dev1/port0/line30 |
| PFI 31 | Dev1/port0/line31 |
| PFI 32 | Dev1/port1/line1 |
| PFI 33 | Dev1/port1/line2 |
| PFI 34 | Dev1/port1/line3 |
| PFI 35 | Dev1/port1/line4 |
| PFI 36 | Dev1/port1/line5 |
| PFI 37 | Dev1/port1/line6 |
| PFI 38 | Dev1/port1/line7 |
| PFI 39 | Dev1/port1/line8 |

<!--NI_TOPIC bundle=ni-daqmx path=tiosigconcounters.html language=enus -->
## TOPIC 00135: TIO Signal Connections for Counters

- bundle_id: `ni-daqmx`
- source_path: `tiosigconcounters.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/tiosigconcounters.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel properties/attributes. You cannot change the default PFI lines for quadrature e

### TIO Signal Connections for Counters

The following table lists the default input terminals for various counter measurements. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel properties/attributes.

Note

x

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 | Ctr4 | Ctr5 | Ctr6 | Ctr7 | gpsTimestampCtr0 (NI 6608 Only) | gpsTimestampCtr1 (NI 6608 Only) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 39 Count Direction: PFI 37 | Edges: PFI 35 Count Direction: PFI 33 | Edges: PFI 31 Count Direction: PFI 29 | Edges: PFI 27 Count Direction: PFI 25 | Edges: PFI 23 Count Direction: PFI 21 | Edges: PFI 19 Count Direction: PFI 17 | Edges: PFI 15 Count Direction: PFI 13 | Edges: PFI 11 Count Direction: PFI 9 | N/A | N/A |
| Pulse Width Measurement | PFI 38 | PFI 34 | PFI 30 | PFI 26 | PFI 22 | PFI 18 | PFI 14 | PFI 10 | N/A | N/A |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 38 | PFI 34 | PFI 30 | PFI 26 | PFI 22 | PFI 18 | PFI 14 | PFI 10 | N/A | N/A |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 39 | PFI 35 | PFI 31 | PFI 27 | PFI 23 | PFI 19 | PFI 15 | PFI 11 | N/A | N/A |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 39 | PFI 35 | PFI 31 | PFI 27 | PFI 23 | PFI 19 | PFI 15 | PFI 11 | N/A | N/A |
| Semiperiod Measurement | PFI 38 | PFI 34 | PFI 30 | PFI 26 | PFI 22 | PFI 18 | PFI 14 | PFI 10 | N/A | N/A |
| Two-Edge Separation Measurement | Start: PFI 37 Stop: PFI 38 | Start: PFI 33 Stop: PFI 34 | Start: PFI 29 Stop: PFI 30 | Start: PFI 25 Stop: PFI 26 | Start: PFI 21 Stop: PFI 22 | Start: PFI 17 Stop: PFI 18 | Start: PFI 13 Stop: PFI 14 | Start: PFI 9 Stop: PFI 10 | N/A | N/A |
| Position Measurement | A: PFI 39 B: PFI 37 Z: PFI 38 | A: PFI 35 B: PFI 33 Z: PFI 34 | A: PFI 31 B: PFI 29 Z: PFI 30 | A: PFI 27 B: PFI 25 Z: PFI 26 | A: PFI 23 B: PFI 21 Z: PFI 22 | A: PFI 19 B: PFI 17 Z: PFI 18 | A: PFI 15 B: PFI 13 Z: PFI 14 | A: PFI 11 B: PFI 9 Z: PFI 10 | N/A | N/A |
| GPS Timestamp Measurement | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | PFI 7 Synch. Source: PFI 7 | PFI 7 Synch. Source: PFI 7 |

Note

The following table lists the output terminals for counter output. You can use a different PFI line for any of the output terminals.

| Ctr0 | Ctr1 | Ctr2 | Ctr3 | Ctr4 | Ctr5 | Ctr6 | Ctr7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PFI 36 | PFI 32 | PFI 28 | PFI 24 | PFI 20 | PFI 16 | PFI 12 | PFI 8 |

Note

Parent topic:

Connecting Counter Signals

#### NI 6624 Issues

The eight PFI lines listed as the defaults for counter output are dedicated for output, and they are the only terminals you can use for counter output. For example, you can use PFI 8 (the default for Ctr7) as the output terminal for any counter, but you cannot use it as an input terminal.

When using counter output, if the Idle State attribute/property is low, the optocouplers on the NI 6624 will still be driving your output load. Set the Idle State attribute/property to high to prevent driving the output after your task completes.

<!--NI_TOPIC bundle=ni-daqmx path=tips-on-measuring-ac-current.html language=enus -->
## TOPIC 00136: Tips on Measuring AC Current

- bundle_id: `ni-daqmx`
- source_path: `tips-on-measuring-ac-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/tips-on-measuring-ac-current.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: To measure AC current, insert a precisely calibrated, low-value resistor into the signal path and measure the voltage drop across the resistor. You must then perform high-pass filtering on the resulting signal to remove the DC component. You can perform this filtering using an analog filter or digit

### Tips on Measuring AC Current

To measure AC current, insert a precisely calibrated, low-value resistor into the signal path and measure the voltage drop across the resistor. You must then perform high-pass filtering on the resulting signal to remove the DC component. You can perform this filtering using an analog filter or digital signal processing techniques, such as the filtering tools in the analysis library of LabVIEW.

Parent topic:

Measuring and Generating Current

<!--NI_TOPIC bundle=ni-daqmx path=transexcit.html language=enus -->
## TOPIC 00137: Transducer Excitation

- bundle_id: `ni-daqmx`
- source_path: `transexcit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/transexcit.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal conditioning systems can generate excitation for some transducers. Strain gages and RTDs require external voltage and current, respectively, to excite their circuitry into measuring physical phenomena. This type of excitation is similar to the power a radio needs to receive and decode audio s

### Transducer Excitation

Signal conditioning systems can generate excitation for some transducers. Strain gages and RTDs require external voltage and current, respectively, to excite their circuitry into measuring physical phenomena. This type of excitation is similar to the power a radio needs to receive and decode audio signals. Several measurement devices provide the necessary excitation for transducers. Consult your device documentation to see if your device can generate excitation.

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx path=transstate.html language=enus -->
## TOPIC 00138: Transitioning the State Backwards

- bundle_id: `ni-daqmx`
- source_path: `transstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/transstate.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a task is implicitly transitioned backwards, it returns to the state of the task prior to the last operation that resulted in a forward state transition. For example, if the task was in the Verified state and you called the Start Task function/VI to start the task, the task is reserved, committ

### Transitioning the State Backwards

When a task is implicitly transitioned backwards, it returns to the state of the task prior to the last operation that resulted in a forward state transition. For example, if the task was in the Verified state and you called the Start Task function/VI to start the task, the task is reserved, committed, and started, transitioning to the Reserved state and to the Committed state before transitioning to the Running state. When you invoke the Stop Task function/VI, the task is not just stopped and transitioned from the Running state to the Committed state. If this were the case, the result is unexpected because the task still has its resources reserved despite the fact that you never explicitly reserved them. Instead, the task is stopped, uncommitted, and unreserved, returning to the Verified state, its state immediately before you performed the last operation that resulted in the state transition, calling the Start Task function/VI.

As another example, suppose the task is in the Reserved state, and you call the Read function/VI to perform a finite measurement. This results in the task implicitly transitioning from the Reserved state to the Committed state and then to the Running state before performing the read operation. When the read operation completes, the task does not remain in the running state. If this were the case, the result is unexpected behavior, because you need to stop the task and unreserve its resources despite the fact you never explicitly reserved the resources or started the task. Instead, after the finite read operation completes, the task is implicitly transitioned from the Running state to the Committed state to the Reserved state. This results in the task returning to the state before you performed the read operation.

Keep in mind that setting the value of a channel, timing, or triggering attribute/property does not implicitly transition the task back to the Unverified state. Instead, the task remains in its current state and is implicitly verified when the next state transition occurs. For example, if the task is in the Reserved state and you set the value of timing attribute/property, the task remains in the Reserved state. The next time the task, either implicitly or explicitly, is committed, the task is verified. Because the task is implicitly verified when the next state transition occurs, NI-DAQmx can return an error specifying that the value of attribute/property is invalid.

Parent topic:

Implicit Task State Transitions

<!--NI_TOPIC bundle=ni-daqmx path=triggerbuslines.html language=enus -->
## TOPIC 00139: Dynamically Selecting Trigger Bus Lines

- bundle_id: `ni-daqmx`
- source_path: `triggerbuslines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/triggerbuslines.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Management of trigger lines is another feature of NI-DAQmx routing. If you hard-code two measurement tasks to the same trigger line for different signals, at least one of the measurement tasks causes a resource conflict. Multi-device routing allows you to dynamically select trigger lines at run time

### Dynamically Selecting Trigger Bus Lines

Management of trigger lines is another feature of NI-DAQmx routing. If you hard-code two measurement tasks to the same trigger line for different signals, at least one of the measurement tasks causes a resource conflict. Multi-device routing allows you to dynamically select trigger lines at run time. This means that NI-DAQmx selects any available trigger line. You can still select a specific trigger bus line by splitting your multi-device route into two single-device routes. However, the two static routes lose the ability to dynamically choose an available trigger at run time.

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-daqmx path=triggered-acquisition-programming-flowchart.html language=enus -->
## TOPIC 00140: Triggered Acquisition Programming Flowchart

- bundle_id: `ni-daqmx`
- source_path: `triggered-acquisition-programming-flowchart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/triggered-acquisition-programming-flowchart.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following flowchart depicts the main steps you follow for adding triggering to an acquisition. If you prefer, you can configure triggering with the DAQ Assistant.

### Triggered Acquisition Programming Flowchart

The following flowchart depicts the main steps you follow for adding triggering to an acquisition. If you prefer, you can configure triggering with the DAQ Assistant.

[IMAGE alt='image' src='GUID-39B6354E-0285-4578-86A2-C811DF34A54C-a5.gif']

Parent topic:

Generic Programming Flowcharts

<!--NI_TOPIC bundle=ni-daqmx path=triggering.html language=enus -->
## TOPIC 00141: Triggering

- bundle_id: `ni-daqmx`
- source_path: `triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/triggering.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a device controlled by NI-DAQmx does something, it performs an action. Two very common actions are producing a sample and starting a waveform acquisition. Every NI-DAQmx action needs a stimulus or cause. When the stimulus occurs, the action is performed. Causes for actions are called triggers.

### Triggering

When a device controlled by NI-DAQmx does something, it performs an action. Two very common actions are producing a sample and starting a waveform acquisition. Every NI-DAQmx action needs a stimulus or cause. When the stimulus occurs, the action is performed. Causes for actions are called triggers. Triggers are named after the actions they cause:

- Advance Trigger
- Expiration Trigger
- Handshake Trigger
- Pause Trigger
- Reference Trigger
- Start Trigger
- Arm Start Trigger

In addition to specifying the action you want a trigger to cause, you must select the type of trigger to use, which determines how the trigger is produced.

- [Advance Trigger](adtrig.html)
- [Arm Start Trigger](armtrig.html)
- [Expiration Trigger](expirationtrigger.html)
- [Handshake Trigger](handtrig.html)
- [Pause Trigger](pausetrigger.html)
- [Reference Trigger](referencetrigger.html)
- [Start Trigger](starttrig.html)
- [Trigger Types](triggertypes.html)

Parent topic:

Timing and Triggering

<!--NI_TOPIC bundle=ni-daqmx path=triggertypes.html language=enus -->
## TOPIC 00142: Trigger Types

- bundle_id: `ni-daqmx`
- source_path: `triggertypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/triggertypes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to specifying the action you want a trigger to cause, you must select the type of trigger to use, which determines how the trigger is produced. If you need to trigger off an analog signal, use an analog edge trigger or an analog window trigger. If the trigger signal is digital, choose a

### Trigger Types

In addition to specifying the action you want a trigger to cause, you must select the type of trigger to use, which determines how the trigger is produced. If you need to trigger off an analog signal, use an analog edge trigger or an analog window trigger. If the trigger signal is digital, choose a digital edge trigger with the source typically being one of the PFI pins.

- [Analog Edge Triggering](analogtriggering.html)
- [Analog Level Triggering](analeveltrig.html)
- [Analog Multi Edge Triggering](analog-multi-edge-triggering.html)
- [Analog Window Triggering](algwindowtrig.html)
- [Digital Edge Triggering](digtrigger.html)
- [Digital Level Triggers](digleveltrig.html)
- [Digital Pattern Triggering](digpattern.html)
- [Software Triggers](softwaretrig.html)
- [Time Triggering](time-triggering.html)

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-daqmx path=tristating.html language=enus -->
## TOPIC 00143: Line Tristating Issues

- bundle_id: `ni-daqmx`
- source_path: `tristating.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/tristating.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: During device initialization, all terminals on the I/O connector and trigger buses are tristated. Tristated means the terminal is floating or at high impedance. For the terminal to be driven from the device, the tristate buffer associated with the terminal must be enabled. For instance, assume that

### Line Tristating Issues

During device initialization, all terminals on the I/O connector and trigger buses are tristated. Tristated means the terminal is floating or at high impedance. For the terminal to be driven from the device, the tristate buffer associated with the terminal must be enabled.

For instance, assume that you have a device with a single bidirectional terminal on the I/O connector. The terminal on the I/O connector is called the trigger terminal for reference purposes. Also, the trigger terminal of the device is bidirectional because it can accept an external trigger signal or export the internal trigger signal. The exported internal trigger signal could be different from the external trigger signal.

| Scenario | Usage and Consequences |
| --- | --- |
| The trigger terminal is being driven by an external trigger signal only. | This is a common case for triggering an operation from an external source. As a result of this operation, you must disable the tristate buffer associated with the trigger terminal so that the internal trigger signal does not drive the trigger terminal, too. |
| The trigger terminal is being driven by the internal device trigger only. | In this case, an internally generated trigger is starting the device. This signal could be useful for other devices, too. To export this trigger signal, you must enable the tristate buffer associated with the trigger terminal, so the device can drive the pin with the trigger signal. It is important that there is no external signal hooked up to the trigger terminal. If it is inconvenient to unhook the external signal, you must make sure the external signal is at least tristated. |
| The trigger terminal is being driven by both the internal device trigger AND an external trigger signal. | Driving the trigger terminal both internally and externally is called double driving. If the internal and external sources drive the signal in opposite directions, it signals problems. Usually the driving hardware is damaged, but more extreme consequences can occur as well. Remember to be very careful to avoid double driving any terminals on your I/O connectors. |

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-daqmx path=troubleshooting.html language=enus -->
## TOPIC 00144: Troubleshooting

- bundle_id: `ni-daqmx`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/troubleshooting.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Installation and Configuration Refer to the DAQ Getting Started Guide for general installation and configuration instructions. Use the following resources if you have problems installing your DAQ hardware and/or software: Refer to NI DAQ Setup and Support on ni.com for information on getting started

### Troubleshooting

#### Installation and Configuration

Refer to the DAQ Getting Started Guide for general installation and configuration instructions.

Use the following resources if you have problems installing your DAQ hardware and/or software:

- Refer to NI DAQ Setup and Support on ni.com for information on getting started with NI DAQ, support, drivers and code, and other resources.
- Refer to ni.com/kb for documents on troubleshooting common
installation and programming problems and for answering frequently
asked questions about NI products.
- If you think you have damaged your device and need to return your NI hardware for repair or
 calibration, refer to sending a NI board in for repair or calibration.

For LabWindows/CVI users, if the Data Acquisition function panel is disabled, you may need to uninstall NI-DAQmx and reinstall it, making sure that you add support for LabWindows/CVI. If you have installed LabWindows/CVI support and Data Acquisition is still dimmed, select Library»Customize. In the Customize Library Menu dialog box, check Data Acquisition, and restart LabWindows/CVI. You might also need to verify that the dataacq.lib is in the bin directory.

#### Programming

To help you get started programming, you can use the shipping examples for your ADE.

You can also visit NI's extensive library of technical support resources at ni.com/support.

You can interactively configure global virtual channels and tasks with the DAQ Assistant. For NI application software such as LabVIEW, you can use the DAQ Assistant to generate code.

You can use NI I/O Trace to analyze the functions you have called in the API with NI application software. With NI I/O Trace, you can watch the order of execution of the application and locate errors as they happen.

Note

Finally, the NI-DAQmx Help contains programming flowcharts for common applications such as measuring temperature, current, strain, position, and acceleration.

#### External Connections

In addition to the information on making signal connections in this help file, the Connection Diagram tab in the DAQ Assistant within MAX shows you how to connect signals.

#### Calibration

- For information on externally calibrating your device, including step-by-step calibration procedures, refer to ni.com/calibration.
- For an overview of calibration, including the difference between self-calibration and external calibration, refer to Device Calibration.
- For device-specific information required for calibration with NI-DAQmx, refer to Device-Specific Calibration.
- For information on channel calibration, refer to What Is Channel Calibration?

#### CPU Usage

NI-DAQmx tasks use 100% of the CPU if no other processes are running. However, as soon as another process requires the CPU, the NI-DAQmx task yields to that process.

Parent topic:

Getting Started with NI-DAQmx

Related concepts:

- Finding Examples

<!--NI_TOPIC bundle=ni-daqmx path=tspower.html language=enus -->
## TOPIC 00145: Power Supply and Power Channel Considerations

- bundle_id: `ni-daqmx`
- source_path: `tspower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/tspower.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to Hardware Input and Output DAQmx Power in the LabVIEW Example Finder for examples that implement many of the following considerations. Default Values The following property values take effect when the task is committed or started. Property Name Default Value Pwr.IdleOutputBehavior Maintain E

### Power Supply and Power Channel
 Considerations

Refer to Hardware Input and Output»DAQmx»Power in the LabVIEW Example Finder for examples that implement many of the following
 considerations.

#### Default Values

The following property values take effect when the task is committed or started.

| Property Name | Default Value |
| --- | --- |
| Pwr.IdleOutputBehavior | Maintain Existing Value |
| Pwr.RemoteSense | Local Sense |
| Pwr.OutputEnable | True |
| Pwr.CurrentSetpoint | 0.03A |
| Pwr.VoltageSetpoint | 0 V |

#### Configuring Voltage and Current
 Setpoints

Use the DAQmx Create Channel VI/function to set the current and voltage setpoints. Two
 properties reflect the current and voltage setpoints for a power channel, and are settable
 at runtime via the DAQmx Channel property node:

Pwr.Current.Setpoint

Pwr.Voltage.Setpoint

#### Configuring and Reading Power Output States and Behavior

Use the DAQmx Create Channel VI/function with the Pwr.OutputEnable
 property to enable or disable power channel output. At runtime, set this property via the
 DAQmx Channel property node.

Use the DAQmx Channel property node with the Pwr.IdleOutputBehavior
 property to enable or disable power channel output when the task is uncommitted.

Use the DAQmx Channel property node to read the Pwr.OutputState property
 and determine the channel state.

Note

#### Detecting Auxiliary Power Errors

Use the DAQmx Read property node to read auxiliary power supply errors. Two properties
 reflect the error state for auxiliary power.

Note

AuxPowerErrorChansExist

AuxPowerErrorChans

#### Detecting Remote Sense Errors

Use the DAQmx Read property node to read remote sense errors. Two properties reflect the
 error state for Remote Sense.

Note

RemoteSenseErrorChansExist

RemoteSenseErrorChans

#### Detecting Over-Temperature
 Errors

Use the DAQmx Read property node to read over-temperature errors. Two properties reflect an
 [over-temperature
 condition](overtemp.html).

Note

OvertemperatureChansExist

OvertemperatureChans

#### Detecting Reverse Voltage Errors

Use the DAQmx Read property node to read reverse voltage errors. Two properties reflect the
 reverse voltage error state of channel

Note

ReverseVoltageErrorChansExist

ReverseVoltageErrorChans

#### Configuring Remote Sense

Use the DAQmx Channel property to set the Pwr.RemoteSense property.

- DAQmx Read will return local voltage if Pwr.RemoteSense is
 configured to Local .
- DAQmx Read will return remote voltage if Pwr.RemoteSense if
 configured to Remote .

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=twocountermeasmeth.html language=enus -->
## TOPIC 00146: Two Counter Measurement Method

- bundle_id: `ni-daqmx`
- source_path: `twocountermeasmeth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/twocountermeasmeth.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: For period and frequency measurements, you also can use a second counter. For most applications, the low frequency with one counter method is sufficient and desirable because it uses fewer resources. However, if you have a high-frequency or widely varying signal, you can use one of the two counter m

### Two Counter Measurement Method

For period and frequency measurements, you also can use a second counter. For most applications, the low frequency with one counter method is sufficient and desirable because it uses fewer resources. However, if you have a high-frequency or widely varying signal, you can use one of the two counter measurement methods—the high-frequency measurement method or the large-range measurement method. Depending on the rate of your input signal and measurement method used, your measurement is subject to different amounts of quantization error. In two counter applications, you only need to call the Create Channel function/VI once, specifying only the counter channel to which you want to connect your input signal. NI-DAQmx automatically takes care of making the internal routes necessary to perform the measurement across paired counters.

Parent topic:

Counters

Related concepts:

- High Frequency Two-Counter Measurement Method
- Large-Range Two-Counter Measurement Method
- Quantization Error
- Paired Counters

<!--NI_TOPIC bundle=ni-daqmx path=twopulse.html language=enus -->
## TOPIC 00147: Two-Pulse Encoders

- bundle_id: `ni-daqmx`
- source_path: `twopulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/twopulse.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: A two pulse encoder is a position measurement sensor that has two channels, A and B. When the encoder is moved, either signal A or signal B on the encoder pulses. A pulse on signal A represents a movement in one direction, and a pulse on signal B represents movement in the opposite direction. When s

### Two-Pulse Encoders

A two pulse encoder is a position measurement sensor that has two channels, A and B. When the encoder is moved, either signal A or signal B on the encoder pulses. A pulse on signal A represents a movement in one direction, and a pulse on signal B represents movement in the opposite direction. When signal A pulses, the counter increments. When signal B pulses, the counter decrements.

[IMAGE alt='image' src='GUID-AC61A9A7-88B6-4A8B-980B-9AF4CB943864-a5.svg']

Many encoders also use z indexing for precise determination of a reference position.

Parent topic:

Encoders

Related concepts:

- Z Indexing

<!--NI_TOPIC bundle=ni-daqmx path=unscaleddata.html language=enus -->
## TOPIC 00148: Unscaled Data

- bundle_id: `ni-daqmx`
- source_path: `unscaleddata.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/unscaleddata.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Unscaled data is in the native format of the device, read directly from the device or buffer without scaling. The native format of a device can be an 8-, 16-, or 32-bit integer, signed or unsigned. If your device supports software calibration, NI-DAQmx does not calibrate unscaled samples. Refer to c

### Unscaled Data

Unscaled data is in the native format of the device, read directly from the device or buffer without scaling. The native format of a device can be an 8-, 16-, or 32-bit integer, signed or unsigned.

Note

Parent topic:

Selecting Read and Write Data Format and Organization

Related concepts:

- Device Calibration Considerations

<!--NI_TOPIC bundle=ni-daqmx path=unverified.html language=enus -->
## TOPIC 00149: Unverified State

- bundle_id: `ni-daqmx`
- source_path: `unverified.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/unverified.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a task is created or loaded, either explicitly or implicitly, it is in the Unverified state. In this state, you configure the timing, triggering, and channel attributes/properties of the task.

### Unverified State

When a task is created or loaded, either explicitly or implicitly, it is in the Unverified state. In this state, you configure the timing, triggering, and channel attributes/properties of the task.

Parent topic:

Task State Model

<!--NI_TOPIC bundle=ni-daqmx path=usbinterchans.html language=enus -->
## TOPIC 00150: Internal Channels for USB DAQ Devices

- bundle_id: `ni-daqmx`
- source_path: `usbinterchans.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/usbinterchans.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the internal channel for the USB-9211 device. Internal Channel Name Description _cjtemp A differential terminal with the positive terminal connected to the onboard temperature sensor and the negative terminal connected to the ground reference for analog input. This channel

### Internal Channels for USB DAQ Devices

The following table lists the internal channel for the USB-9211 device.

| Internal Channel Name | Description |
| --- | --- |
| _cjtemp | A differential terminal with the positive terminal connected to the onboard temperature sensor and the negative terminal connected to the ground reference for analog input. This channel is used for cold-junction compensation. |

The following table lists the internal channels for the USB-9219 device.

| Internal Channel Name | Description |
| --- | --- |
| _cjtemp0 | A differential terminal with the positive terminal connected to the onboard temperature sensor and the negative terminal connected to the ground reference for analog input. This channel is used for cold-junction compensation for analog input channel 0. |
| _cjtemp1 | This channel is used for cold-junction compensation for analog input channel 1. |
| _cjtemp2 | This channel is used for cold-junction compensation for analog input channel 2. |
| _cjtemp3 | This channel is used for cold-junction compensation for analog input channel 3. |

Parent topic:

Internal Channels

<!--NI_TOPIC bundle=ni-daqmx path=usbphyschanns.html language=enus -->
## TOPIC 00151: USB DAQ Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `usbphyschanns.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/usbphyschanns.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dev1 in physical channel names is the default device name for USB Series DAQ devices. You can change these names in MAX. Analog Input The following table lists the number and naming of analog input physical channels for USB DAQ devices. Device Number of Channels Naming NI USB-9211A, NI USB-9215A, NI

### USB DAQ Physical Channels

Dev1 in physical channel names is the default device name for USB Series DAQ devices. You can change these names in MAX.

Parent topic:

Physical Channels

#### Analog Input

The following table lists the number and naming of analog input physical channels for USB DAQ devices.

| Device | Number of Channels | Naming |
| --- | --- | --- |
| NI USB-9211A, NI USB-9215A, NI USB-9219, NI USB-9229, NI USB-9234, NI USB-9237, NI USB-9239 | 4 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai3 |
| NI USB-9201, NI USB-9221 | 8 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai7 |
| NI USB-9213 | 16 | cDAQ1Mod1/ai0 to cDAQ1Mod1/ai15 |

##### Strain and Wheatstone Bridge Measurements

The NI 9235, NI 9236, and NI 9237 support only the AI Strain Gage, AI Force Bridge, AI Pressure Bridge, AI Torque Bridge, AI Bridge (V/V), and AI Custom Voltage With Excitation channel types.

When using the NI USB-9219 or I USB-9237 with an AI Custom Voltage With Excitation channel, you must set the AI.Excit.UseForScaling attribute/property to true. This attribute/property causes the channel to return ratiometric data: Vin/Vex. The NI USB-9219 and NI USB-9237 modules perform this division in hardware.

For the NI USB-9219, NI-DAQmx requires the AI.Excit.Val attribute/property to be set to 2.5 V for AI Strain Gage and AI Custom Voltage With Excitation channel types and to 500 µA for resistance and RTD measurements. The actual excitation voltage or current output by the NI USB-9219 varies with the sensor resistance or the load being measured.

NI USB-9219 and NI USB-9237 devices return a voltage ratio rather than a voltage. Therefore, use the AI.Bridge.InitialRatio attribute/property to specify the initial voltage ratio, or set the AI.Bridge.InitialVoltage attribute/property to the ratio Vin/Vex returned by the device, multiplied by Vex.

The NI USB-9219 does not have quarter bridge completion circuitry, which affects AI Strain Gage Quarter Bridge I channels and AI Custom Voltage With Excitation Quarter Bridge channels (but not AI Strain Gage Quarter Bridge II channels). With these channels, the NI USB-9219 performs a 2-wire resistance measurement on the active gage element, then NI-DAQmx uses software scaling to convert the resistance measurement into a bridge ratio. For these channels, the polynomial coefficients specified by the AI.DevScalingCoeff attribute/property convert unscaled data into Ohms, not into V/V. Likewise, the AI.Rng.High/AI.Rng.Low attributes/properties should be specified in units of Ohms, not V/V.

When the NI USB-9219 is in quarter bridge mode, you need to use the AI.Bridge.NomResistance attribute/property to control whether the channel uses the 120 Ω range or the 350 Ω range.

#### Analog Output

The following table lists the number and naming of analog output physical channels for USB DAQ devices.

| Device | Number of Channels | Naming |
| --- | --- | --- |
| NI USB-9263, NI USB-9265 | 4 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao3 |
| NI USB-9264 | 16 | cDAQ1Mod1/ao0 to cDAQ1Mod1/ao15 |

When using the NI USB-9263, NI-USB 9264, or NI USB-9265, you can run only one type of timing at a time. You can have one software-timed task per channel or one hardware-timed task running on a device at one time, but you cannot have a combination of timing on that device. For instance, you can run up to four software-timed tasks on an the NI USB-9263 concurrently, but running one hardware-timed task with one software-timed task generates an error. Additionally, the NI USB-9263, NI-USB 9264, and NI USB-9265 can run only one hardware-timed analog output task per device at a given time.

<!--NI_TOPIC bundle=ni-daqmx path=user-manual-welcome.html language=enus -->
## TOPIC 00152: NI-DAQmx User Manual

- bundle_id: `ni-daqmx`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-DAQmx
 User Manual

The NI-DAQmx User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-DAQmx
- NI-DAQmx Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center
- NI-DAQmx VI and Function Reference
- NI-DAQ™mx C Reference

<!--NI_TOPIC bundle=ni-daqmx path=usingchopping.html language=enus -->
## TOPIC 00153: Using Chopping to Remove Offset Voltages

- bundle_id: `ni-daqmx`
- source_path: `usingchopping.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/usingchopping.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Chopping is a feature that can be used to remove offset voltages and other low frequency errors. The signal is measured twice, once normally and once with the inputs inverted. These measurements are then averaged by the device to create each sample. The NI 4309 supports chopping but disables it by d

### Using Chopping to Remove Offset Voltages

Chopping is a feature that can be used to remove offset voltages and other low frequency errors. The signal is measured twice, once normally and once with the inputs inverted. These measurements are then averaged by the device to create each sample.

The NI 4309 supports chopping but disables it by default. Chopping can be enabled with the AI.Chop.Enable attribute/property, or when configuring a voltage input task in the DAQ Assistant by selecting the 
 Enable Chopping option. Refer to the NI 4309 User Manual for wiring instructions.

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=usingtherm4339withpxie4339.html language=enus -->
## TOPIC 00154: Using the RM-4339 with the PXIe-4339

- bundle_id: `ni-daqmx`
- source_path: `usingtherm4339withpxie4339.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/usingtherm4339withpxie4339.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: This section contains information on using the NI RM-4339 with the PXIe-4339. Refer to SC Express Smart Accessory Connections for specific terminal connections. Excitation The RM-4339 has a connection for an external excitation source. Each channel can also use it's own channel-specific internal exc

### Using the RM-4339 with the PXIe-4339

This section contains information on using the NI RM-4339 with the PXIe-4339. Refer to 
 *SC Express Smart Accessory Connections* for specific terminal connections.

#### Excitation

The RM-4339 has a connection for an external excitation source. Each channel can also use it's own channel-specific internal excitation. Use the AI.Excit.Src attribute/property to set the excitation connection.

#### Quarter-Bridge Completion

The RM-4339 includes three internal resistors you can use for quarter-bridge completion. These resistors are 120 Ω, 350 Ω, and 1 kΩ. Use the AI.Bridge.NomResistance attribute/property to set quarter-bridge completion.

#### Shunt Calibration

The RM-4339 includes two independent shunt calibration resistors, named A and B. You can select which resistor to use using the AI.Bridge.ShuntCal.Select attribute/property.

You can use an internal or external resistor for shunt resistor A. Use the AI.Bridge.ShuntCal.ShuntCalASrc attribute/property to set this. Select Built-In to use the internal 100 kΩ resistor, or User Provided to use an external resistor.

Shunt resistor B is an internal resistor that you can use only with quarter-bridge completion. You can use a 50 kΩ or 100 kΩ resistor by setting the AI.Bridge.ShuntCal.ShuntCalBResistance attribute/property.

Note

The DAQmx Perform Shunt Calibration function/VI and the Strain Gage Calibration Wizard in MAX do not support AI.Bridge.ShuntCal.ShuntCalASrc or AI.Bridge.ShuntCal.ShuntCalBResistance.

Parent topic:

NI-DAQmx Device Considerations

Related concepts:

- SC Express Smart Accessory Connections

<!--NI_TOPIC bundle=ni-daqmx path=usingwaitfortimestampvi.html language=enus -->
## TOPIC 00155: Using Wait for Valid Timestamp VI

- bundle_id: `ni-daqmx`
- source_path: `usingwaitfortimestampvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/usingwaitfortimestampvi.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Wait for Valid Timestamp VI waits until the selected timestamp is available and a value is returned. Possible timestamps are Start Trigger, Reference Trigger, Arm Start Trigger and First Sample.

### Using Wait for Valid Timestamp VI

The Wait for Valid Timestamp VI waits until the selected timestamp is available and a value is returned. Possible timestamps are Start Trigger, Reference Trigger, Arm Start Trigger and First Sample.

Parent topic:

Timestamps

<!--NI_TOPIC bundle=ni-daqmx path=velocitytransducer.html language=enus -->
## TOPIC 00156: Velocity Transducers

- bundle_id: `ni-daqmx`
- source_path: `velocitytransducer.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/velocitytransducer.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Velocity transducers are used to measure dynamic velocity such as that produced by a running machine or a vibrating structure. Older velocity probes use a moving coil in a permanent magnetic field to generate a signal that is proportional to the velocity of the vibration. More modern implementations

### Velocity Transducers

Velocity transducers are used to measure dynamic velocity such as that produced by a running machine or a vibrating structure.

Older velocity probes use a moving coil in a permanent magnetic field to generate a signal that is proportional to the velocity of the vibration.

More modern implementations operate using the same principles as IEPE accelerometers. Additionally, an integrating circuit is used to convert acceleration to velocity. Use the same best practices for storage and handling, calibration, mounting, and signal conditioning of IEPE velocity sensors as you would for IEPE accelerometers.

Note

Sensor manufacturers make IEPE velocity transducers with varying sensitivity and other characteristics. Use a sensor appropriate for your application.

Parent topic:

Integrated Electronics Piezoelectric (IEPE) and Charge

<!--NI_TOPIC bundle=ni-daqmx path=verified.html language=enus -->
## TOPIC 00157: Verified State

- bundle_id: `ni-daqmx`
- source_path: `verified.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/verified.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DAQmx checks the timing, triggering, and channel attributes/properties for correctness when the task transitions from the Unverified to the Verified state. You can explicitly perform this transition by calling the Control Task function/VI with Action set to Verify. While NI-DAQmx detects and veri

### Verified State

NI-DAQmx checks the timing, triggering, and channel attributes/properties for correctness when the task transitions from the Unverified to the Verified state. You can explicitly perform this transition by calling the Control Task function/VI with Action set to Verify. While NI-DAQmx detects and verifies some invalid values for attributes/properties immediately when you set the attribute/property, NI-DAQmx cannot verify other values immediately because they depend on other attributes/properties and the devices being used. NI-DAQmx checks the value of these attributes/properties during the verify transition and reports any invalid values at that time. If NI-DAQmx finds no invalid values, the task is successfully verified and transitions to the Verified state. Otherwise, it remains in the Unverified state.

In certain cases, NI-DAQmx will coerce the values of attributes/properties when successfully verifying a task rather than generating an error. This is done when the value set on the attribute/property cannot be met exactly as specified and coercing it to a legal value has little functional impact on the task.

Parent topic:

Task State Model

Related concepts:

- Coercion

<!--NI_TOPIC bundle=ni-daqmx path=virtchantypes.html language=enus -->
## TOPIC 00158: Types of Virtual Channels

- bundle_id: `ni-daqmx`
- source_path: `virtchantypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/virtchantypes.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a number of different types of virtual channels, depending on the signal type—analog, digital, or counter—and direction (input or output). These channels can be either global virtual channels or local virtual channels. For information on specific functions/VIs, refer to the NI referen

### Types of Virtual Channels

You can create a number of different types of virtual channels, depending on the signal type—analog, digital, or counter—and direction (input or output). These channels can be either global virtual channels or local virtual channels. For information on specific functions/VIs, refer to the NI reference help for your ADE.

Analog Input Channels

Analog Output Channels

Counter Input/Output Channels

Digital Input/Output Channels

A port-based channel represents a fixed collection of lines on the device. Reading or writing to a port affects all the lines on the port. The number of lines in the port (commonly referred to as port width) is hardware dependent and typically varies from 8 lines (MIO device) to 32 lines (SCXI digital modules).

Power Channels

Parent topic:

Channels: Physical, Virtual, Local Virtual, and Global Virtual

Related concepts:

- Channels: Physical, Virtual, Local Virtual, and Global Virtual
- Digital Lines, Ports, and Port Width
- Tasks in NI-DAQmx
- Counter Parts in NI-DAQmx

<!--NI_TOPIC bundle=ni-daqmx path=virtualchancal.html language=enus -->
## TOPIC 00159: Virtual Channel Calibration Support

- bundle_id: `ni-daqmx`
- source_path: `virtualchancal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/virtualchancal.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following devices do not support NI-DAQmx virtual channel calibration: NI DAQPad-6015 NI DAQPad-6016 NI PCI-6010 NI PCI-6013 NI PCI-6014 NI USB-6000 NI USB-6001 NI USB-6002 NI USB-6003 NI USB-6008 NI USB-6009 SensorDAQ

### Virtual Channel Calibration Support

The following devices do not support NI-DAQmx virtual channel calibration:

- NI DAQPad-6015
- NI DAQPad-6016
- NI PCI-6010
- NI PCI-6013
- NI PCI-6014
- NI USB-6000
- NI USB-6001
- NI USB-6002
- NI USB-6003
- NI USB-6008
- NI USB-6009
- SensorDAQ

Parent topic:

Device Calibration Considerations

<!--NI_TOPIC bundle=ni-daqmx path=voltagemeasurements4339.html language=enus -->
## TOPIC 00160: Taking Custom Voltage Measurements with the PXIe-4339

- bundle_id: `ni-daqmx`
- source_path: `voltagemeasurements4339.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/voltagemeasurements4339.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-4339 supports taking regular (non-ratiometric) voltage measurements using an AI Voltage task. In addition, as of NI-DAQmx 14.5, the PXIe-4339 can perform custom voltage measurements while providing voltage excitation, for example, when using DC powered sensors that return a non-ratiometric

### Taking Custom Voltage Measurements with the PXIe-4339

The PXIe-4339 supports taking regular (non-ratiometric) voltage measurements using an AI Voltage task. In addition, as of NI-DAQmx 14.5, the PXIe-4339 can perform custom voltage measurements while providing voltage excitation, for example, when using DC powered sensors that return a non-ratiometric voltage. To enable this type of measurement, configure the DAQmx Create Virtual Channel VI to AI Custom Voltage with Excitation mode.

Setting the use excitation for scaling input to False will prevent the PXIe-4339's ADCs from scaling the measured voltage ratiometrically to the excitation voltage.

Setting the use excitation for scaling input to True, will enable the PXIe-4339 to use the excitation value that the user sets with the DAQmx driver for scaling the ratiometric input. The device will not use the voltage present on the remote sense lines for scaling as it does when providing internal excitation. Thus, while the driver will support using external excitation for ratiometric measurements, this is not a recommended configuration.

The table below covers each possible combination of AI channel type, voltage excitation source input value, and use excitation for scaling input value. The cases highlighted will throw DAQmx errors, and the reasons for the errors are described in the Use Case and Notes column of the table.

[IMAGE alt='image' src='GUID-A4C265E9-8356-4223-9981-120AEC09F51C-a5.svg']

Note

Parent topic:

NI-DAQmx Device Considerations

Related reference:

- Using the RM-4339 with the PXIe-4339

<!--NI_TOPIC bundle=ni-daqmx path=vsaphyschan.html language=enus -->
## TOPIC 00161: SensorDAQ Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `vsaphyschan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/vsaphyschan.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: SensorDAQ has analog input, analog output, digital I/O, and counter channels. It also has three analog sensor channels (labeled Ch. 1, Ch. 2, and Ch. 3 on the device) and one digital sensor channel (labeled DIG on the device) for use with Vernier sensors. Please contact Vernier for additional inform

### SensorDAQ Physical Channels

SensorDAQ has analog input, analog output, digital I/O, and counter channels. It also has three analog sensor channels (labeled Ch. 1, Ch. 2, and Ch. 3 on the device) and one digital sensor channel (labeled DIG on the device) for use with Vernier sensors. Please contact Vernier for additional information on the analog and digital sensor channels.

Parent topic:

Physical Channels

#### Analog Input

SensorDAQ has two AI physical channels, 
 Dev1/ai0 and 
 Dev1/ai1. When you configure a channel in differential mode, 
 Dev1/ai0 is the positive input and 
 Dev1/ai1 is the negative input.

#### Analog Output

SensorDAQ has two AO physical channels, 
 Dev1/ao0 and 
 Dev1/ao1.

#### Digital Input/Output

SensorDAQ has four digital I/O physical channels.

#### Counter Input and Output

There is one counter channel referred to by the physical channel name 
 Dev1/ctr0. pfi0 is the terminal used for this physical channel.

<!--NI_TOPIC bundle=ni-daqmx path=waituntildone.html language=enus -->
## TOPIC 00162: Using Wait Until Done

- bundle_id: `ni-daqmx`
- source_path: `waituntildone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/waituntildone.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: You might need to call the Wait Until Done function/VI to ensure that the specified operation is complete before you stop the task. The most common example is a finite generation. If you start a task that performs a finite generation and then immediately stop the task, the generation probably has no

### Using Wait Until Done

You might need to call the Wait Until Done function/VI to ensure that the specified operation is complete before you stop the task.

The most common example is a finite generation. If you start a task that performs a finite generation and then immediately stop the task, the generation probably has not completed when you stop the task. As a result, the generation does not complete as expected. To ensure that the finite generation completes as expected, call the Wait Until Done function/VI before stopping the task. After the Wait Until Done function/VI executes, the finite generation has been completed, and you can stop the task.

In general, use the Wait Until Task Done function/VI with finite measurements and generations.

Parent topic:

Tasks in NI-DAQmx

Related concepts:

- When Is A Task Done?

<!--NI_TOPIC bundle=ni-daqmx path=watchdogtimers.html language=enus -->
## TOPIC 00163: Watchdog Timers

- bundle_id: `ni-daqmx`
- source_path: `watchdogtimers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/watchdogtimers.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Watchdog timers are a hardware feature that you can use to detect a failure in the software controlling the device. Software failures could include a system crash or a loop rate that is slower than you intend. To use a watchdog timer, you must use a watchdog timer task. When you create a watchdog ti

### Watchdog Timers

Watchdog timers are a hardware feature that you can use to detect a failure in the software controlling the device. Software failures could include a system crash or a loop rate that is slower than you intend. To use a watchdog timer, you must use a watchdog timer task. When you create a watchdog timer task, you specify the timeout value for the watchdog timer and a set of expiration states for output physical channels on the device. The channels go to those expiration states if the watchdog timer expires. In addition, you cannot perform any actions with the task until you reset it.

Your application must continuously reset the watchdog timer to prevent it from expiring. For example, if you have a digital I/O application, and you expect a loop in the application to acquire and analyze data 10 times per second, you should set the watchdog timer to expire in 100 ms and reset the timer inside the digital I/O loop. If the loop does not execute once every 100 ms, the watchdog timer expires and the device goes into the expired state. You must then clear the expiration or reset the device.

Also, you can use the Expiration Trigger to cause the watchdog timer to expire. Set the timeout of the watchdog timer task to -1 to disable expiration due to timeout if you want the Expiration Trigger to be the only mechanism to cause expiration.

Note

Note

Parent topic:

Digital I/O

<!--NI_TOPIC bundle=ni-daqmx path=waveformlimits.html language=enus -->
## TOPIC 00164: Waveform Timing Limitations

- bundle_id: `ni-daqmx`
- source_path: `waveformlimits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/waveformlimits.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The limitation on t0 is that NI-DAQmx calculates the starting time for the task when data is read the first time. At this time, NI-DAQmx calculates the starting time for the task by reading the current system time and subtracting the number of samples acquired × dt from the system. Therefore, if you

### Waveform Timing Limitations

The limitation on t0 is that NI-DAQmx calculates the starting time for the task when data is read the first time. At this time, NI-DAQmx calculates the starting time for the task by reading the current system time and subtracting the number of samples acquired × dt from the system. Therefore, if you call read after the acquisition is complete, the calculated start time for the task is not accurate. This inaccuracy is reflected in the t0 returned with the waveform data.

The limitation on dt is that for certain timing types, NI-DAQmx cannot calculate the value of dt. When you use sample clock timing, NI-DAQmx calculates dt based on the rate of the clock. Because NI-DAQmx does not know the rate when handshake, implicit, on demand, or change detection timing is specified, NI-DAQmx returns dt as 0. Waveforms with a dt of 0 often do not work with the waveform analysis functions. However, you can always update the value of dt in your application if you know the expected rate of the timing source. Your ADE has an interface to update the value of dt.

Note

Parent topic:

Selecting Read and Write Data Format and Organization

<!--NI_TOPIC bundle=ni-daqmx path=whentaskdone.html language=enus -->
## TOPIC 00165: When Is A Task Done?

- bundle_id: `ni-daqmx`
- source_path: `whentaskdone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/whentaskdone.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the measurement or generation is finite, the task is done when you acquire or generate the final sample or when you call the Stop Task function/VI. If the measurement or generation is continuous (including on-demand timing), or if retriggering is enabled, the task is not done until you call the S

### When Is A Task Done?

If the measurement or generation is finite, the task is done when you acquire or generate the final sample or when you call the Stop Task function/VI. If the measurement or generation is continuous (including on-demand timing), or if retriggering is enabled, the task is not done until you call the Stop Task function/VI. In addition, the task is done if a fatal error is generated while performing the measurement or generation, or you abort the measurement or generation. Check for errors and warnings to verify the task completed successfully.

Parent topic:

Tasks in NI-DAQmx

<!--NI_TOPIC bundle=ni-daqmx path=windowing.html language=enus -->
## TOPIC 00166: Windowing

- bundle_id: `ni-daqmx`
- source_path: `windowing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/windowing.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use windowing, or smoothing windows, to minimize spectral leakage associated with truncated waveforms. Spectral Leakage Spectral leakage is a phenomenon whereby the measured spectral energy appears to leak from one frequency into other frequencies. It occurs when a sampled waveform does not contain

### Windowing

Use windowing, or smoothing windows, to minimize spectral leakage associated with truncated waveforms.

Parent topic:

Signal Analysis

#### Spectral Leakage

Spectral leakage is a phenomenon whereby the measured spectral energy appears to leak from one frequency into other frequencies. It occurs when a sampled waveform does not contain an integral number of cycles over the time period during which it was sampled. The technique used to reduce spectral leakage is to multiply the time-domain waveform by a window function.

Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) are mathematical techniques that resolve a given signal into the sum of sines and cosines. It is the basis for spectrum analysis. Using the DFT/FFT when you sample a noninteger number of cycles, such as 7.5 cycles, returns a spectrum in which it appears as if the energy at one frequency leaks into all the other frequencies because the FFT assumes that the data is a single period of a periodically repeating waveform. The artificial discontinuities appear as very high frequencies that were not present in the original signal. Because these frequencies are higher than the Nyquist frequency, they appear aliased between 0 and fs/2.

The type of window to use depends on the type of signal you acquire and on the application. Choosing the correct window requires some knowledge of the signal that you are analyzing. The following table lists common types of windows, the appropriate signal types, and example applications.

| Window | Signal Type and Description | Applications |
| --- | --- | --- |
| Rectangular (no window) | Transient signals that are shorter than the length of the window; truncates a window to within a finite time interval | Order tracking, system analysis (frequency response measurements) with pseudorandom excitation, separation of two tones with frequencies very close to each other but with almost equal amplitudes |
| Triangle | Window that is the shape of a triangle | General-purpose applications |
| Hanning | Transient signals that are longer than the length of the window | Often used in speech signal processing |
| Hamming | Transient signals that are longer than the length of the window; a modified version of the Hanning window that is discontinuous at the edges | Often used in speech signal processing |
| Blackman | Transient signals; similar to Hanning and Hamming windows but adds one additional cosine term to reduce ripple | General-purpose applications |
| Flat Top | Has the best amplitude accuracy of all the windows but limits frequency selectivity | Accurate, single-tone amplitude measurements with no nearby frequency components |

Note

<!--NI_TOPIC bundle=ni-daqmx path=writestatus.html language=enus -->
## TOPIC 00167: Write Status Attributes/Properties and Buffers

- bundle_id: `ni-daqmx`
- source_path: `writestatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/writestatus.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: The three Write Status attributes/properties are useful for observing the progress of your generation. The Current Write Position is the place in the buffer where the next write begins if the Relative To attribute/property is Current Write Position and the Offset is 0. In any case, the Current Write

### Write Status Attributes/Properties and Buffers

The three Write Status attributes/properties are useful for observing the progress of your generation.

- The Current Write Position is the place in the buffer where the next write begins if the Relative To attribute/property is Current Write Position and the Offset is 0. In any case, the Current Write Position is always where the last write left it.
- Total Samples per Channel Generated is the total number of samples per channel generated by your device since the task started.
- Space Available in Buffer is computed by first calculating the Current Write Position based on the settings of the Relative To and Offset attributes/properties and then subtracting this number from the sum of Total Samples per Channel Generated and the buffer size. If regeneration is allowed, the Space Available in Buffer value is capped at the buffer size and grows from 0 to the buffer size repeatedly.

Parent topic:

Buffering

<!--NI_TOPIC bundle=ni-daqmx path=writingteds.html language=enus -->
## TOPIC 00168: Writing Data to TEDS Sensors

- bundle_id: `ni-daqmx`
- source_path: `writingteds.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/writingteds.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Write TEDS Data function/VI to write data to a TEDS sensor. The TEDS data must be in a virtual TEDS file or in a bitstream constructed according to the IEEE 1451.4 specification. National Instruments provides a LabVIEW library for viewing and editing TEDS bitstreams and virtual TEDS files. Y

### Writing Data to TEDS Sensors

Use the Write TEDS Data function/VI to write data to a TEDS sensor. The TEDS data must be in a virtual TEDS file or in a bitstream constructed according to the IEEE 1451.4 specification.

National Instruments provides a LabVIEW library for viewing and editing TEDS bitstreams and
 virtual TEDS files. You can download the TEDS Library for LabVIEW at [How Do I
 Install the TEDS Library into LabVIEW?](https://www.ni.com/r/download-teds-library-lv).

Parent topic:

Transducer Electronic Data Sheets (TEDS)

Related concepts:

- Transducer Electronic Data Sheets (TEDS)

#### Basic TEDS Data

Some TEDS sensors include a PROM, to which you can write data one time. When you write TEDS data, you can choose to write basic TEDS data to the PROM or to the EEPROM. Basic TEDS data includes the manufacturer ID, model number, serial number, version number, and version letter. If you write basic TEDS data to the PROM, the Write TEDS Data function/VI returns an error if you later attempt to write basic TEDS data to the EEPROM.

<!--NI_TOPIC bundle=ni-daqmx path=xcalconn.html language=enus -->
## TOPIC 00169: Device Calibration Signal Connections for X Series Devices

- bundle_id: `ni-daqmx`
- source_path: `xcalconn.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xcalconn.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you self-calibrate your X Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels and you do not want changes on these channels, you

### Device Calibration Signal Connections for X Series Devices

When you self-calibrate your X Series device, no signal connections are necessary. However, values generated on the analog output channels change during the calibration process. If you have external circuitry connected to the analog output channels and you do not want changes on these channels, you should disconnect the circuitry before beginning the self-calibration.

When externally calibrating (or adjusting) your X Series device, connect the signals as described below for the type of device you are calibrating. Set the reference voltage between +6.0 V and +8.5 V for X Series devices. You should use a calibrator or other stable voltage source for the reference voltage. Do not use a power supply as its signals are not very stable.

Follow these steps:

1. Disconnect any external connections or circuitry to your device.
2. Connect the positive output of your reference voltage source to physical channel ai0.
3. Connect the negative output of your reference voltage source to physical channel ai8.
4. If your reference voltage source and your computer are floating with respect to each other, connect the negative output of your reference voltage source to the AI GND terminal as well as to physical channel ai8.

Parent topic:

Signal Connections

<!--NI_TOPIC bundle=ni-daqmx path=xseriescountsigconn.html language=enus -->
## TOPIC 00170: X Series Signal Connections for Counters

- bundle_id: `ni-daqmx`
- source_path: `xseriescountsigconn.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xseriescountsigconn.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default input terminals for various counter measurements on X Series devices. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties. Measurement Ctr0 Ctr1 Ctr2 Ctr3 Coun

### X Series Signal Connections for Counters

The following table lists the default input terminals for various counter measurements on X Series devices. You can use a different PFI line for any of the input terminals. To change the PFI input for a measurement, use the NI-DAQmx channel attributes/properties.

| Measurement | Ctr0 | Ctr1 | Ctr2 | Ctr3 |
| --- | --- | --- | --- | --- |
| Count Edges | Edges: PFI 8 Count Direction: PFI 10 | Edges: PFI 3 Count Direction: PFI 11 | Edges: PFI 0 Count Direction: PFI 2 | Edges: PFI 5 Count Direction: PFI 7 |
| Pulse Width Measurement | PFI 9 | PFI 4 | PFI 1 | PFI 6 |
| Period/Frequency Measurement (Low Frequency with One Counter) | PFI 9 | PFI 4 | PFI 1 | PFI 6 |
| Period/Frequency Measurement (High Frequency with Two Counters) | PFI 8 | PFI 3 | PFI 0 | PFI 5 |
| Period/Frequency Measurement (Large Range with Two Counters) | PFI 8 | PFI 3 | PFI 0 | PFI 5 |
| Pulse Measurement | PFI 9 | PFI 4 | PFI 1 | PFI 6 |
| Semiperiod Measurement | PFI 9 | PFI 4 | PFI 1 | PFI 6 |
| Two-Edge Separation Measurement | Start: PFI 10 Stop: PFI 9 | Start: PFI 11 Stop: PFI 4 | Start: PFI 2 Stop: PFI 1 | Start: PFI 7 Stop: PFI 6 |
| Position Measurement | A: PFI 8 B: PFI 10 Z: PFI 9 | A: PFI 3 B: PFI 11 Z: PFI 4 | A: PFI 0 B: PFI 2 Z: PFI 1 | A: PFI 5 B: PFI 7 Z: PFI 6 |

The following table lists the output terminals for counter output. You can use a different PFI line for any of the output terminals.

| Ctr0 | Ctr1 | Ctr2 | Ctr3 |
| --- | --- | --- | --- |
| PFI 12 | PFI 13 | PFI 14 | PFI 15 |

Parent topic:

Connecting Counter Signals

<!--NI_TOPIC bundle=ni-daqmx path=xseriesinterchan.html language=enus -->
## TOPIC 00171: Internal Channels for X Series Multiplexed Sampling Devices

- bundle_id: `ni-daqmx`
- source_path: `xseriesinterchan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xseriesinterchan.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: On an X Series device, you can either acquire a signal present on the I/O connector, or you can acquire a signal that is being generated from the internal calibration multiplexer. The channels available on this multiplexer are typically used for calibration purposes, but you can also sample them as

### Internal Channels for X Series Multiplexed Sampling Devices

On an X Series device, you can either acquire a signal present on the I/O connector, or you can acquire a signal that is being generated from the internal calibration multiplexer. The channels available on this multiplexer are typically used for calibration purposes, but you can also sample them as you would a physical signal present on the I/O connector. To read from one of these internal channels on a X Series multiplexed sampling device, you must use the internal channel as the device's physical channel (for example, Dev1/_aignd_vs_aignd) when creating the virtual channel.

The following table describes all internal channels for X Series multiplexed sampling devices.

| Internal Channel Name | Description |
| --- | --- |
| _aignd_vs_aignd | A single-ended terminal with the positive and negative terminals both connected to the ground reference for analog input. |
| _ao0_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal connected to the ground reference for analog output. |
| _ao1_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao1 and the negative terminal connected to the ground reference for analog output. |
| _ao2_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao2 and the negative terminal connected to the ground reference for analog output. |
| _ao3_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao3 and the negative terminal connected to the ground reference for analog output. |
| _calref_vs_aignd | A single-ended terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the ground reference for analog input. |
| _aignd_vs_aisense | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE. |
| _aignd_vs_aisense2 | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE2. |
| _aignd_vs_aisense3 | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE3. |
| _aignd_vs_aisense4 | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to physical channel AI SENSE4. |
| _calSrcHi_vs_aignd | A single-ended terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. |
| _calref_vs_calSrcHi | A differential terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the calibration PWM. |
| _calSrcHi_vs_calSrcHi | A differential terminal with the positive and negative terminals connected to the calibration PWM. |
| _aignd_vs_calSrcHi | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to the calibration PWM. |
| _calSrcMid_vs_aignd | A single-ended terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. _calSrcMid is the divided down version of _calSrcHi. |
| _calSrcLo_vs_aignd | A single-ended terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. _calSrcLo is the divided down version of _calSrcHi. |
| _ai0_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ai0 and the negative terminal connected to the calibration PWM. |
| _ai8_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ai8 and the negative terminal connected to the calibration PWM. |
| _boardTempSensor_vs_aignd | A single-ended terminal with the positive terminal connected to the onboard temperature sensor and the negative terminal connected to the ground reference for analog input. |

Parent topic:

Internal Channels

Related concepts:

- X Series Device Groupings

<!--NI_TOPIC bundle=ni-daqmx path=xseriesnames.html language=enus -->
## TOPIC 00172: X Series Device Groupings

- bundle_id: `ni-daqmx`
- source_path: `xseriesnames.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xseriesnames.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: X Series Multiplexed Sampling Devices: NI 6320 NI 6321 NI 6323 NI 6340 NI 6341 NI 6342 NI 6343 NI 6345 NI 6347 NI 6350 NI 6351 NI 6352 NI 6353 NI 6355 NI 6357 NI 6361 NI 6363 NI 6365 NI 6375 NI 6381 NI 6383 X Series Simultaneous Sampling Devices: NI 6346 NI 6349 NI 6356 NI 6358 NI 6366 NI 6368 NI 63

### X Series Device Groupings

X Series Multiplexed Sampling Devices:

- NI 6320
- NI 6321
- NI 6323
- NI 6340
- NI 6341
- NI 6342
- NI 6343
- NI 6345
- NI 6347
- NI 6350
- NI 6351
- NI 6352
- NI 6353
- NI 6355
- NI 6357
- NI 6361
- NI 6363
- NI 6365
- NI 6375
- NI 6381
- NI 6383

X Series Simultaneous Sampling Devices:

- NI 6346
- NI 6349
- NI 6356
- NI 6358
- NI 6366
- NI 6368
- NI 6374
- NI 6376
- NI 6378
- NI 6386
- NI 6396

Parent topic:

NI-DAQmx Device Considerations

<!--NI_TOPIC bundle=ni-daqmx path=xseriesphychannels.html language=enus -->
## TOPIC 00173: X Series Physical Channels

- bundle_id: `ni-daqmx`
- source_path: `xseriesphychannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xseriesphychannels.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: In physical channel names, Dev1 is the default device name for X Series devices. You can change these names in MAX. Analog Input Depending on your X Series device, you can have from eight to 208 analog input channels. An 8-channel X Series device has physical channels ranging from Dev1/ai0 to Dev1/a

### X Series Physical Channels

In physical channel names, 
 Dev1 is the default device name for X Series devices. You can change these names in MAX.

Parent topic:

Physical Channels

Related reference:

- X Series Signal Connections for Counters

#### Analog Input

Depending on your X Series device, you can have from eight to 208 analog input channels. An 8-channel X Series device has physical channels ranging from 
 Dev1/ai0 to 
 Dev1/ai7, a 208-channel device from 
 Dev1/ai0 to 
 Dev1/ai207.

Use only the physical channel name of the positive channel (not both) when creating a differential channel.

#### Analog Output

An X Series device that supports two analog outputs has analog output physical channels named 
 Dev1/ao0and 
 Dev1/ao1.

An X Series device that supports four analog outputs has analog output physical channels named 
 Dev1/ao0, 
 Dev1/ao1, 
 Dev1/ao2, and 
 Dev1/ao3.

#### Digital Input and Output

All X Series devices have eight or 32 lines of digital input and output named 
 Dev1/port0/line0 through 
 Dev1/port0/line7 or 
 Dev1/port0/line0 through 
 Dev1/port0/line31. These lines belong to a single port, and the physical channel Dev1/port0 refers to all eight or 32 lines at once. Port 0 can perform both hardware-timed and static digital operations.

X Series devices have two more ports, port 1 and port 2. Port 1 has eight digital I/O lines, 
 Dev1/port1/line0 through 
 Dev1/port1/line7. Port 2 has eight digital I/O lines, 
 Dev1/port2/line0 through 
 Dev1/port2/line7. Port 1 and port 2 can be used as static digital I/O lines or PFI lines, PFI 0..15. When any of PFI lines 0..15 is used as a digital I/O signal, it uses the physical channel name shown in the following table.

| PFI Signal | Physical Channel Name |
| --- | --- |
| PFI 0 | Dev1/port1/line0 |
| PFI 1 | Dev1/port1/line1 |
| PFI 2 | Dev1/port1/line2 |
| PFI 3 | Dev1/port1/line3 |
| PFI 4 | Dev1/port1/line4 |
| PFI 5 | Dev1/port1/line5 |
| PFI 6 | Dev1/port1/line6 |
| PFI 7 | Dev1/port1/line7 |
| PFI 8 | Dev1/port2/line0 |
| PFI 9 | Dev1/port2/line1 |
| PFI 10 | Dev1/port2/line2 |
| PFI 11 | Dev1/port2/line3 |
| PFI 12 | Dev1/port2/line4 |
| PFI 13 | Dev1/port2/line5 |
| PFI 14 | Dev1/port2/line6 |
| PFI 15 | Dev1/port2/line7 |

Physical channel 
 Dev1/port1 refers to all eight lines, 
 Dev1/port1/line0:7, at once. Physical channel 
 Dev1/port2 refers to all eight lines, 
 Dev1/port2/line0:7, at once.

#### Counter Input and Output

All X Series devices have four counter/timers referred to by the physical channel names 
 Dev1/ctr0, 
 Dev1/ctr1, 
 Dev1/ctr2, and 
 Dev1/ctr3. Unlike the other I/O types, these physical channel names do not refer to terminals on the I/O connector but instead to circuits within the device. There are five primary signals associated with each counter: SOURCE, GATE, AUX, OUT, and sample clock. NI-DAQmx has default terminals for these signals, except for the sample clock. For counter input tasks, if you know whether your signal provides the SOURCE, AUX, or GATE function and wire your signal to the default, you do not have to set the Input Terminal attribute/property.

| Counter | SOURCE Default | GATE Default | AUX Default | OUT Default |
| --- | --- | --- | --- | --- |
| Dev1/ctr0 | PFI 8 | PFI 9 | PFI 10 | PFI 12 |
| Dev1/ctr1 | PFI 3 | PFI 4 | PFI 11 | PFI 13 |
| Dev1/ctr2 | PFI 0 | PFI 1 | PFI 2 | PFI 14 |
| Dev1/ctr3 | PFI 5 | PFI 6 | PFI 7 | PFI 15 |

<!--NI_TOPIC bundle=ni-daqmx path=xseriessimulinterchan.html language=enus -->
## TOPIC 00174: Internal Channels for X Series Simultaneous Sampling Devices

- bundle_id: `ni-daqmx`
- source_path: `xseriessimulinterchan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/xseriessimulinterchan.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: On an X Series device, you can either acquire a signal present on the I/O connector, or you can acquire a signal that is being generated from the internal calibration multiplexer. The channels available on this multiplexer are typically used for calibration purposes, but you can also sample them as

### Internal Channels for X Series Simultaneous Sampling Devices

On an X Series device, you can either acquire a signal present on the I/O connector, or you can acquire a signal that is being generated from the internal calibration multiplexer. The channels available on this multiplexer are typically used for calibration purposes, but you can also sample them as you would a physical signal present on the I/O connector. To read from one of these internal channels on a X Series simultaneous sampling device, you must use one of the device's AI physical channels (for example, Dev1/ai0) when creating the virtual channel. The physical channel specifies the ADC for the internal channel. You can then set the appropriate string value on the Input Source channel attribute/property.

Note

Input Source

| Internal Channel Name | Description |
| --- | --- |
| _external_channel | The differential terminal on the I/O connector that is typically used for acquiring data. |
| _ai0_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal connected to the calibration PWM. |
| _ai1_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ao1 and the negative terminal connected to the calibration PWM |
| _ai0_vs_aignd | A differential terminal with the positive terminal connected to physical channel ai0 and the negative terminal connected to the ground reference for analog input |
| _ai8_vs_aignd | A differential terminal with the positive terminal connected to the negative terminal of ai0 and the negative terminal connected to the ground reference for analog input. |
| _ai8_vs_calSrcHi | A differential terminal with the positive terminal connected to the negative terminal of ai0 and the negative terminal connected to the calibration PWM. |
| _aignd_vs_aignd | A single-ended terminal with the positive and negative terminals both connected to the ground reference for analog input. |
| _aignd_vs_calSrcHi | A differential terminal with the positive terminal connected to the ground reference for analog input and the negative terminal connected to the calibration PWM. |
| _ao0_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal connected to the ground reference for analog output. |
| _ao0_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ao0 and the negative terminal connected to the calibration PWM. |
| _ao1_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao1 and the negative terminal connected to the ground reference for analog output. |
| _ao1_vs_calSrcHi | A differential terminal with the positive terminal connected to physical channel ao1 and the negative terminal connected to the calibration PWM. |
| _ao2_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao2 and the negative terminal connected to the ground reference for analog output. |
| _ao3_vs_aognd | A differential terminal with the positive terminal connected to physical channel ao3 and the negative terminal connected to the ground reference for analog output. |
| _calref_vs_aignd | A single-ended terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the ground reference for analog input. |
| _calSrcHi_vs_aignd | A single-ended terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. |
| _calSrcHi_vs_calSrcHi | A differential terminal with the positive and negative terminals connected to the calibration PWM. |
| _calref_vs_calSrcHi | A differential terminal with the positive terminal connected to the internal calibration reference voltage and the negative terminal connected to the calibration PWM. |
| _calSrcMid_vs_aignd | A single-ended terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to the ground reference for analog input. _calSrcMid is the divided down version of _calSrcHi. |
| _calSrcMid_vs_calSrcHi | A differential terminal with the positive and negative terminals connected to the calibration PWM. _calSrcMid is the divided down version of _ calSrcHi . |
| _calSrcHi_vs_ai0 | A differential terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to physical channel ai0. |
| _calSrcHi_vs_ai8 | A differential terminal with the positive terminal connected to the calibration PWM and the negative terminal connected to physical channel ai8. |

Parent topic:

Internal Channels

Related concepts:

- X Series Device Groupings

<!--NI_TOPIC bundle=ni-daqmx path=zindexing.html language=enus -->
## TOPIC 00175: Z Indexing

- bundle_id: `ni-daqmx`
- source_path: `zindexing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx/raw/resource/enus/zindexing.html
- document_id: `ni-daqmx`
- page_type: `leaf`
- content_type: `concept`
- source_description: Encoders typically use a third signal for Z indexing, which produces a pulse at fixed positions that you can use for precise determination of a reference position. For instance, if the Z index is 45° for an angular encoder, the encoder sends a pulse on the Z input terminal every time the encoder is

### Z Indexing

Encoders typically use a third signal for Z indexing, which produces a pulse at fixed positions that you can use for precise determination of a reference position. For instance, if the Z index is 45° for an angular encoder, the encoder sends a pulse on the Z input terminal every time the encoder is turned to the 45° mark.

The behavior of signal Z differs with designs. You must refer to the documentation for an encoder to obtain the timing of signal Z in relation to the A and B signals. In NI-DAQmx, you can configure Z indexing with the 
 Z Index Phase attribute/property.

Parent topic:

Encoders
