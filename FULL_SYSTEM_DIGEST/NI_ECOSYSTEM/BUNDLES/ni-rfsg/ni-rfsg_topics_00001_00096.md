# NI DOCUMENT BUNDLE: ni-rfsg

<!--NI_BUNDLE_CHUNK bundle=ni-rfsg start=1 end=96 -->
<!--NI_TOPIC bundle=ni-rfsg path=a-device-does-not-appear-in-max.html language=enus -->
## TOPIC 00001: A Device Does Not Appear in MAX

- bundle_id: `ni-rfsg`
- source_path: `a-device-does-not-appear-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/a-device-does-not-appear-in-max.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: If your NI-RFSG device does not appear in MAX, complete the following steps: In the configuration tree, expand the Chassis tree. Press F5 to refresh the list of installed devices. If the NI-RFSG device is still not listed, power off the system, ensure that the NI-RFSG device is correctly installed,

### A Device Does Not Appear in MAX

NI-RFSG

1. In the configuration tree, expand the Chassis
 tree.
2. Press F5 to refresh the list of installed devices.
3. If the NI-RFSG device is still not listed, power
 off the system, ensure that the NI-RFSG device is
 correctly installed, and restart the system.
4. Navigate to the Device Manager.
  - Windows 10/8.1: Right-click the Start button,
 and select Device Manager .
  - Windows 7: Select Start»Control Panel»Device Manager .
5. Proceed based on your controller type. 
 Controller TypeDescriptionPXI controller
 Verify that a National Instruments entry
 appears in the system device list. Reinstall NI-RFSG and the device if error conditions appear in the
 list.MXI-3 controller
 Right-click PCI-to-PCI Bridge and select
 Properties from the shortcut menu to verify
 that the bridge is enabled.
6. If the NI-RFSG device still fails to appear in
 MAX, contact NI technical support or visit ni.com/support.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=assigning-properties-or-attributes-to-a-wavef.html language=enus -->
## TOPIC 00002: Assigning Properties to a Waveform in NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `assigning-properties-or-attributes-to-a-wavef.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/assigning-properties-or-attributes-to-a-wavef.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG can store the I/Q Rate, Peak Power Adjustment, and Arb Carrier Frequency for a waveform. When switching between waveforms, the associated waveform properties also change. You can assign waveform properties in Arb Waveform Generation mode or Script Generation mode. Use Configure Generation Mo

### Assigning Properties to a Waveform in
 NI-RFSG

NI-RFSG can store the I/Q Rate,
 Peak Power Adjustment, and Arb Carrier Frequency
 for a waveform. When switching between waveforms, the associated waveform properties also
 change. You can assign waveform properties in *Arb Waveform Generation mode* or
 *Script Generation mode*. Use Configure Generation Mode
 to select between the two modes.

Use one of the following methods to determine the coerced values of
 properties associated with a waveform:

- Use the Active Channel property or the
 channelName parameter of the
 niRFSG_GetAttributeViReal64 function to specify the waveform or
 script from which to return the coerced value.
- If you do not use the Active Channel property
 or the channelName parameter of the
 niRFSG_GetAttributeViReal64 function, NI-RFSG returns the coerced value set by the Selected
 Waveform property or the Selected Script 
 property.

Note

#### Arb Waveform Generation
 Mode

Use the Active Channel property or the channelName
 parameter of the niRFSG_GetAttributeViReal64 function to name a
 waveform and associate the IQ Rate, Peak Power
 Adjustment, and Arb Carrier Frequency properties
 with the named waveform. You must allocate or write the waveform before associating
 properties with the waveform. When you select the waveform through Select
 Arb Waveform, the associated properties are used when the you initiate
 the device.

When you clear a waveform, the properties associated with the waveform are also cleared.

#### Script Generation Mode

Use the Active Channel property or the channelName
 parameter of the niRFSG_GetAttributeViReal64 function to specify
 the waveform name to assign the IQ Rate, Peak Power
 Adjustment, and Arb Carrier Frequency properties to
 the waveforms called in your script. NI-RFSG then
 parses the script to determine which waveforms to generate and which waveform
 properties to inherit. If a script inherits a property, NI-RFSG uses the inherited value when generating the script.

Property inheritance typically requires all values for a particular property o be the same for
 all waveforms in the script. However, property inheritance doesn't always behave
 typically. Typical inheritance cases are as follows:

- If a property isn't set for a waveform, the waveform uses the value of the
 non-waveform specific property to compare to the other values found in the
 script. For example, given a global I/Q rate of 5 MS/s , a script generates three waveforms ( A ,
 B , and C ). Waveforms B and
 C have specified I/Q rates of 10 MS/s . Waveform A doesn't specify the I/Q rate, so NI-RFSG compares the two I/Q rates, 10 MS/s and 5 MS/s . An error occurs because the rates aren't the same.
- If using the Peak Power Adjustment property to create an
 offset of different power levels between waveforms in a script, the
 Peak Power Adjustment Inheritance Behavior property
 determines the inheritance behavior for Peak Power
 Adjustment .
- If you set the Peak Power Adjustment or IQ
 Rate to INF for a waveform, NI-RFSG uses the
 value specified by the other waveforms in the script.

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsg path=associating-ni-rfsg-modules.html language=enus -->
## TOPIC 00003: Associating NI-RFSG Modules

- bundle_id: `ni-rfsg`
- source_path: `associating-ni-rfsg-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/associating-ni-rfsg-modules.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To control multiple hardware modules as a single RF device, you must first associate the modules in MAX. MAX treats the hardware modules as separate devices. If you are using a hardware system (PXIe-5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, or PXIe-5830/5831/5831 with PXIe-5653/5832/

### Associating NI-RFSG Modules

To control multiple hardware modules as a single RF device,
 you must first associate the modules in MAX.

MAX treats the hardware modules as separate devices. If you are using a
 hardware system (PXIe-5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, or PXIe-5830/5831/5831 with PXIe-5653/5832/5841 with PXIe-5655), you must associate the devices for transparent operation of all hardware
 modules as a single device using NI-RFSG.

Complete the following steps to associate modules in MAX:

1. In the configuration tree, select the module associated with your hardware system, as
 identified in the following table.
2. In the Associated Devices section for the selected module,
 select the appropriate module from each system component drop-down list. Refer to the
 following table for a complete list of device associations. 
 Hardware System
 AssociationsPXIe-5654 with PXIe-5696
 Select the PXIe-5654 RF Analog Signal
 Generator in the configuration tree. In the Associated
 Devices section, select the PXIe-5696 from the AE list.
 PXI-5670
 Select the PXI-5610 RF Signal Upconverter in
 the configuration tree. In the Associated Devices
 section, select the PXI-5421 from the
 AWG list.
 PXI-5671
 Select the PXI-5610 RF Signal Upconverter in
 the configuration tree. In the Associated Devices
 section, select the PXI-5441 from the
 AWG list.
 PXIe-5672
 Select the PXI-5610 RF Signal Upconverter in
 the configuration tree. In the Associated Devices
 section, select the PXIe-5442 from the AWG list.
 PXIe-5673/5673E
 Select the PXIe-5611 I/Q Modulator in the
 configuration tree. In the Associated Devices section,
 select the PXIe-5450/5451 from the
 AWG list and the PXI/PXIe-5650/5651/5652 from the LO list.
 PXIe-5830
 Select the PXIe-3621 Vector Signal Up/Down
 Converter in the configuration tree. In the Associated
 Devices section, select the PXIe-5820 from the Baseband list.
 PXIe-5831
 Select the PXIe-3622 Vector Signal Up/Down
 Converter in the configuration tree. In the Associated
 Devices section, select the PXIe-5820 from the Baseband list.
 PXIe-5831 with PXIe-5653
 Select the PXIe-3622 Vector Signal Up/Down
 Converter in the configuration tree. In the Associated
 Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave
 LO) list.The mmRH-5582 mmWave Radio
 Head automatically appears as connected in MAX when you expand the PXIe-3622 configuration tree item.
 PXIe-5832
 Select the PXIe-3623 Vector Signal Up/Down
 Converter in the configuration tree. In the Associated
 Devices section, select the PXIe-5820 from the Baseband list.
 PXIe-5832 with PXIe-5653
 Select the PXIe-3623 Vector Signal Up/Down
 Converter in the configuration tree. In the Associated
 Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave
 LO) list.The mmRH-5582 mmWave Radio
 Head automatically appears as connected in MAX when you expand the PXIe-3622 configuration tree item.
 PXIe-5841 with PXIe-5655
 Select the PXIe-5841 Vector Signal
 Transceiver in the configuration tree. In the Associated
 Devices section, select the PXIe-5655 from the RF In LO and RF Out
 LO lists. You must select the same PXIe-5655 from both lists.
 Note Select Not Specified if you do not want
 to associate a specific module. Select External if you want to
 use an external module, such as a third-party LO.
 Note Associations between modules may be lost when you move modules
 to different slots in the chassis.
3. Click Save in the MAX toolbar.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

Related tasks:

- Renaming an NI-RFSG Device

<!--NI_TOPIC bundle=ni-rfsg path=break.html language=enus -->
## TOPIC 00004: break

- bundle_id: `ni-rfsg`
- source_path: `break.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/break.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Provide the ability for instruction execution to jump forward to the next instruction immediately following the break block as soon as the trigger is received. The following restrictions apply when using the break statement: Instructions that require a reaction to a trigger are not allowed, includin

### break

Provide the ability for instruction execution to jump
 forward to the next instruction immediately following the break block as
 soon as the trigger is received.

The following restrictions apply when using the break statement:

- Instructions that require a reaction to a trigger are not allowed, including
 repeat until trigger , if-else , and wait until
 trigger instructions.
- Nested break instructions are not allowed.
- clear instruction is not allowed.
- The break block must be preceded by a generate or
 wait N instruction.
- stream instruction is not allowed.

Usage:

Go to the next instruction following the break block as soon as Script
 trigger *N* is received:

```text
generate
Break on scriptTriggerN
  instructions
End break
instructions
```

or

```text
wait N
Break on scriptTriggerN
  instructions
End break
instructions
```

#### break Example

In the following scripts, ScriptTrigger0 is used as a Stop trigger. Script
 execution breaks out of the repeat forever loop as soon as the trigger is
 received, instead of waiting until the last waveform in the loop (testWfm1)
 is generated. Script B generates wfm 1,000 times, but stops generation as
 soon as the Script trigger is detected. A marker is placed at the start of the
 wfm and exported to a counter device to determine the number of times the
 wfm was generated before the condition was met.

```text
Script A
generate wfm
  Break on ScriptTrigger0
    Repeat forever
      Generate testWfm0
      Wait 12
      Generate testWfm1
    End repeat
  End Break
End script
```

```text
Script B
generate wfm
  Break on ScriptTrigger0
    Repeat 10000
      Generate hugeTestWfm marker0(1)
    End repeat
  End Break
  Generate idleStateWfm
End script
```

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=carrier-wave.html language=enus -->
## TOPIC 00005: Carrier Wave

- bundle_id: `ni-rfsg`
- source_path: `carrier-wave.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/carrier-wave.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier wave is a sinusoidal wave that is modulated by a message signal prior to transmission. The message signal modifies the carrier wave amplitude, frequency, or phase. The modulation process may vary these characteristics individually or in combination. The modified carrier signal, also refe

### Carrier Wave

The *carrier wave* is a sinusoidal wave that is
 modulated by a message signal prior to transmission.

The message signal modifies the carrier wave amplitude, frequency, or
 phase. The modulation process may vary these characteristics individually or in
 combination. The modified carrier signal, also referred to as the *modulated
 wave*, is transmitted to a receiver. The process of demodulation removes the
 carrier signal from the received modulated wave to extract the original message signal
 data. In advanced communication systems, the carrier may be a moving signal, also known
 as a spread spectrum signal. When the characteristics of the carrier signal are
 deterministic and known by the receiver, virtually any type of carrier signal can be
 used. The nominal frequency of the carrier wave is the *carrier frequency*.
 In frequency modulation, the carrier frequency is the center frequency.

Parent topic:

NI-RFSG RF Fundamentals

Related concepts:

- Message Signal
- Modulation

<!--NI_TOPIC bundle=ni-rfsg path=clear.html language=enus -->
## TOPIC 00006: clear

- bundle_id: `ni-rfsg`
- source_path: `clear.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/clear.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Clear a received Script trigger. The clear instruction is commonly used immediately before a wait or repeat until instruction to ensure that any Script triggers received before the wait or repeat until instructions are ignored. Usage: clear scripttrigger0 clear Examples Generate myWfmA, clear any Sc

### clear

Clear a received Script trigger.

The clear instruction is commonly used immediately before a
 wait or repeat until instruction to ensure that any Script
 triggers received before the wait or repeat until
 instructions are ignored.

Usage:

```text
clear scripttrigger0
```

#### clear Examples

- Generate myWfmA , clear any Script triggers, wait for receipt of a
 Script trigger, then generate
 myWfmB : generate myWfmA
clear scripttrigger0
wait until scripttrigger0
generate myWfmB Without
 the clear instruction, any Script triggers received during generation
 of myWfmA would cause myWfmB to be generated after the
 smallest possible delay.
- Continuously step between three waveforms, waiting for a Script trigger between
 each: repeat forever
 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmA

 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmB

 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmC
end repeat

Note

clear

wait

```text
generate myWfmA
wait until scripttrigger0
wait until scripttrigger0
generate myWfmB
```

The
 device waits for two Script triggers to occur before generating myWfmB.
 The same situation is true when a Script trigger is "consumed" by a repeat
 until instruction or an if/else/end if instruction.

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=clocking-modes.html language=enus -->
## TOPIC 00007: NI-RFSG Clocking Modes

- bundle_id: `ni-rfsg`
- source_path: `clocking-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/clocking-modes.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI RF signal generators have three modes of clocking to consider to achieve desired I/Q rates. Divide-down clocking Divides an RF signal generator timebase to derive a unique frequency.The divide-down clocking mechanism is preferred when possible because it offers the lowest jitter of the Sample Clo

### NI-RFSG
 Clocking Modes

NI RF signal generators have three modes of clocking to
 consider to achieve desired I/Q rates.

Divide-down clocking

The divide-down clocking mechanism is preferred when
 possible because it offers the lowest jitter of the Sample Clock. However,
 I/Q rates are coerced to the rates the hardware can achieve. Read the value
 of the I/Q rate back after setting it to see what the actual I/Q rate is
 when using divide-down clocking.

High-resolution clocking

The divide-down clocking
 mechanism is preferred when possible because it offers the lowest jitter of
 the Sample Clock. However, I/Q rates are coerced to the rates the hardware
 can achieve. Read the value of the I/Q rate back after setting it to see
 what the actual I/Q rate is when using divide-down clocking.

External clocking

<!--NI_TOPIC bundle=ni-rfsg path=common-scripting-use-cases.html language=enus -->
## TOPIC 00008: Common Scripting Use Cases

- bundle_id: `ni-rfsg`
- source_path: `common-scripting-use-cases.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/common-scripting-use-cases.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to Scripting Instructions for examples of using primary scripting instructions, including generate, repeat/end repeat, wait, and clear.Single Waveform (one-shot/finite generation)script singleWfmExample generate wfm01 end scriptThis script generates wfm01 and then stops. When generation stops,

### Common Scripting Use Cases

Refer to *Scripting Instructions* for examples of using
 primary scripting instructions, including generate, repeat/end
 repeat, wait, and clear.

#### Single Waveform (one-shot/finite
 generation)

```text
script singleWfmExample
    generate wfm01
end script
```

This
 script generates wfm01 and then stops. When generation stops, the
 last sample of wfm01 is held at the output.

#### Generating Waveforms with
 Markers

```text
script wfm01MarkersExample
    generate wfm01 marker0 (0, 20)
end script
```

This
 script generates the entire wfm01 waveform and generates a Marker
 Event at samples 0 (the start of the waveform) and 20.

#### Sequence of Multiple
 Waveforms

```text
script upWfm01DownExample
    generate countUp
    generate wfm01
    generate countDown
end script
```

#### Conditional Branching —
 If/Else

```text
script branchingExample
    repeat forever
        generate wfm01
        if scripttrigger0 then
            generate wfm02
        else
            generate wfm03
        end if
    end repeat
end script
```

The
 following diagram illustrates the preceding script behavior:

[IMAGE alt='image' src='GUID-AFA224E3-38B8-4B5B-9D46-0BAA8DAC575A-a5.gif']

Note

NI-RFSG

Scripting Instructions

#### Generating Waveform
 Subsets

```text
script wfm01SubsetExample
    generate wfm01 subset (20, 60)
end script
```

This
 script generates 60 samples from wfm01, starting at sample
 20.

Note

#### Finite Repetition (*N*
 Times)

```text
script up3Wfm01DownExample
    generate countUp
    repeat 3
        generate wfm01
    end repeat
    generate countDown
end script
```

#### Conditional Repetition — Repeat until
 Trigger

```text
script upWfm01UntilTrigDownExample
    generate countUp
    repeat until scripttrigger0
        generate wfm01
    end repeat
    generate countDown
end script
```

#### Continuous Generation — Repeat
 Forever

```text
script upThenUpAndDownForeverExample
    generate countUp
    repeat forever
        generate countUpAndDown
    end repeat
end script
```

#### Waiting for
 Triggers

```text
script upWaitWfm01DownExample
    generate countUp
    wait until scripttrigger0
    generate wfm01
    generate countDown
end script
```

The following diagrams illustrate the preceding script
 behavior:

[IMAGE alt='image' src='GUID-09D01403-6026-4578-9E8C-757D7EE9704A-a5.gif']

or

```text
script upWaitWfm01DownExample
    generate countUp
    clear scripttrigger0
    wait until scripttrigger0
    generate wfm01
    generate countDown
end script
```

[IMAGE alt='image' src='GUID-F22DEB53-213D-4E6D-B81D-EAC365EAE04A-a5.gif']

These two scripts are similar, but a Script trigger received
 during generation of countUp causes the first script to move to
 wfm01 after the smallest possible delay. By adding a
 clear instruction, you can ignore any triggers received before
 the wait instruction.

#### Finite
 Wait

```text
script upWait32DownExample
    generate countUp
    wait 32
    generate countDown
end script
```

#### Stepping Through Multiple
 Waveforms

```text
script stepThroughUpAllZerosDownExample
    repeat forever
        generate countUp
        clear scripttrigger0
        wait until scripttrigger0

        generate allZeros
        clear scripttrigger0
        wait until scripttrigger0

        generate countDown
        clear scripttrigger0
        wait until scripttrigger0

    end repeat
end script
```

#### Bursting through Multiple
 Waveforms

```text
script burstThroughUpDownThenZerosOnesExample
    repeat forever
        repeat until scripttrigger0
            generate countUp
            generate countDown
        end repeat

        repeat until scripttrigger0
            generate allZeros
            generate allOnes
        end repeat
    end repeat
end script
```

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=creating-an-application-with-microsoft-visual-c-six.html language=enus -->
## TOPIC 00009: Creating an Application with Microsoft Visual C++ 6.0

- bundle_id: `ni-rfsg`
- source_path: `creating-an-application-with-microsoft-visual-c-six.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/creating-an-application-with-microsoft-visual-c-six.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To develop an NI-RFSG application with Microsoft Visual C++ 6.0, follow these general steps: Open an existing or new Visual C/C++ project to manage your application code. Create source code files of type .c (C) or .cpp (C++). Add the source code files to the project. Add the following code in the so

### Creating an Application with Microsoft Visual C++ 6.0

NI-RFSG

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or
 .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: 
 #include "niRFSG.h"
5. Add the NI-RFSG include and library files to the
 project. 
 Note In the following steps,
 IVIROOTDIR32 and
 VXIPNPPATH are aliases to specific National
 Instruments file folder locations. Refer to the *NI-RFSG Readme* for more information about installed file
 locations.
  1. Select Project»Settings»C/C++»Preprocessor»Additional include
 directories, and add the paths to the following files, separated by a
 semicolon: 
 IVIROOTDIR32\Include\niRFSG.h
 VXIPNPPATH\WinNT\Visa\include\visa.h
  2. Select Object/Library Modules»Link»General»Object/Library Modules and add niRFSG.lib.
  3. Select Project»Link»Input»Additional library path and add the following path: 
 32-bit systems:
 IVIROOTDIR32\Lib\msc\niRFSG.lib
 64-bit systems:
 IVIROOTDIR32\Lib x64\msc\niRFSG.lib
6. Build your application using the appropriate programming flow steps.

Parent topic:

Creating an Application with Microsoft Visual C and C++

Related concepts:

- NI-RFSG Instrument Driver Programming Flow

<!--NI_TOPIC bundle=ni-rfsg path=creating-an-application-with-microsoft-visual-c.html language=enus -->
## TOPIC 00010: Creating an Application with Microsoft Visual C and C++

- bundle_id: `ni-rfsg`
- source_path: `creating-an-application-with-microsoft-visual-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/creating-an-application-with-microsoft-visual-c.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: You can create applications using Microsoft Visual C and C++ in one of the following ADEs: Microsoft Visual C++ 6.0 Microsoft Visual Studio 2010

### Creating an Application with Microsoft Visual C and C++

- Microsoft Visual C++ 6.0
- Microsoft Visual Studio 2010

- [Creating an Application with Microsoft Visual C++ 6.0](creating-an-application-with-microsoft-visual-c-six.html)
- [Creating an Application with Microsoft Visual Studio 2010](creating-an-application-with-microsoft-visual-studio.html)

Parent topic:

Creating an Application with NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=creating-an-application-with-microsoft-visual-studio.html language=enus -->
## TOPIC 00011: Creating an Application with Microsoft Visual Studio 2010

- bundle_id: `ni-rfsg`
- source_path: `creating-an-application-with-microsoft-visual-studio.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/creating-an-application-with-microsoft-visual-studio.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To develop an NI-RFSG application with Microsoft Visual Studio 2010, follow these general steps: Open an existing or new Visual C/C++ project to manage your application code. Create source code files of type .c (C) or .cpp (C++). Add the source code files to the project. Add the following code in th

### Creating an Application with Microsoft Visual Studio 2010

NI-RFSG

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or
 .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: 
 #include "niRFSG.h"
5. Add the NI-RFSG include and library files to the
 project. 
 Note In the following steps,
 IVIROOTDIR32 and VXIPNPPATH are aliases to
 specific National Instruments file folder locations. Refer to the NI-RFSG
 *Readme* for more information about installed file locations.
  1. Select Project»Properties»Configuration Properties»C/C++»General»Additional Include Directories and add the paths to the following files, separated by a
 semicolon: 
 IVIROOTDIR32\Include\niRFSG.h
 VXIPNPPATH\WinNT\Visa\include\visa.h
  2. Select Linker»Input»Additional Dependencies and add niRFSG.lib.
  3. Select Linker»General»Additional Dependencies, and add the following path: 
 32-bit systems:
 IVIROOTDIR32\Lib\msc\niRFSG.lib
 64-bit systems: IVIROOTDIR32\Lib
 x64\msc\niRFSG.lib
6. Build your application using the appropriate programming flow steps.

Parent topic:

Creating an Application with Microsoft Visual C and C++

Related concepts:

- NI-RFSG Instrument Driver Programming Flow

<!--NI_TOPIC bundle=ni-rfsg path=creating-an-application-with-ni-rfsg.html language=enus -->
## TOPIC 00012: Creating an Application with NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `creating-an-application-with-ni-rfsg.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/creating-an-application-with-ni-rfsg.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create your application, you need the NI-RFSG instrument driver to control your device. NI-RFSG controls the configuration and operation of NI-RFSG devices using the following application development environments (ADEs): LabVIEW LabWindows/CVI Microsoft Visual C/C++ The NI-RFSG instrument driver

### Creating an Application with NI-RFSG

To create your application, you need the NI-RFSG
 instrument driver to control your device.

NI-RFSG

NI-RFSG

- LabVIEW
- LabWindows/CVI
- Microsoft Visual C/C++

NI-RFSG

Each section includes basic information about how to create an application for each
 ADE.

Parent topic:

Getting Started

Related concepts:

- NI-RFSG Examples

<!--NI_TOPIC bundle=ni-rfsg path=creating-static-signal-routes-for-an-ni-rfsg-.html language=enus -->
## TOPIC 00013: Creating Static Signal Routes for an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `creating-static-signal-routes-for-an-ni-rfsg-.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/creating-static-signal-routes-for-an-ni-rfsg-.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To determine the possible static routes between the PXI trigger buses of your chassis, complete the following steps: Select your chassis in the configuration tree. The settings of your chassis are displayed on the right of the MAX window. Click the Trigger tab below the settings view. A table in the

### Creating Static Signal Routes for an NI-RFSG Device

To determine the possible static routes between the PXI
 trigger buses of your chassis, complete the following steps:

1. Select your chassis in the configuration tree. 
 The settings of your chassis are displayed on the right of the MAX
 window.
2. Click the Trigger tab below the settings view. 
 A table in the Triggers view shows the PXI
 trigger bus segments of your chassis.
3. Configure the static route that you want to make.
4. Save the changes.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=detecting-and-identifying-ni-rfsg-devices.html language=enus -->
## TOPIC 00014: Detecting and Identifying NI-RFSG Devices

- bundle_id: `ni-rfsg`
- source_path: `detecting-and-identifying-ni-rfsg-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/detecting-and-identifying-ni-rfsg-devices.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To share triggers or clocks to synchronize devices, you must properly detect and identify your chassis and controller in MAX. MAX automatically detects and identifies all PXI Express chassis and controllers, including devices controlled using MXI-Express. MAX does not automatically detects and ident

### Detecting and Identifying NI-RFSG Devices

To share triggers or clocks to synchronize devices, you must
 properly detect and identify your chassis and controller in MAX.

MAX automatically detects and identifies all PXI Express chassis and
 controllers, including devices controlled using MXI-Express.

MAX does not automatically detects and identifies all PXI chassis and
 controllers. Complete the following steps to manually detect and identify your PXI
 chassis.

1. In the configuration tree, double-click Devices and Interfaces
 to see a list of detected chassis.
2. Detect or identify your chassis in the list. 
 OptionDescriptionChassis Detection
 If your chassis does not appear under Devices and
 Interfaces, complete the following procedure.Select Devices and Interfaces and
 click Create New in the MAX toolbar.
 Select the PXI Chassis option under
 Devices and Interfaces and enter the requested
 information regarding your PXI equipment.Chassis Identification
 If your chassis appears as Chassis (Unidentified) in the
 list, complete the following procedure:Select your chassis tree item and click
 Identify from the MAX toolbar.
 Select the appropriate model name of your chassis.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=driver-setup-options.html language=enus -->
## TOPIC 00015: NI-RFSG Driver Setup Options

- bundle_id: `ni-rfsg`
- source_path: `driver-setup-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/driver-setup-options.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Driver Setup string allows you to configure hardware devices, simulate devices, and specify FPGA extensions for NI-RFSG instruments. Use the format "Tag:Value" to define your setup, and separate multiple devices with a semicolon. The following table lists common uses and corresponding examples o

### NI-RFSG Driver
 Setup Options

The Driver Setup string allows you to configure hardware devices, simulate devices,
 and specify FPGA extensions for NI-RFSG instruments. Use the format
 "Tag:Value" to define your
 setup, and separate multiple devices with a semicolon.

The following table lists common uses and corresponding examples of the Driver Setup
 string.

| Use | Example Driver Setup String | Supported Devices |
| --- | --- | --- |
| Specify an amplitude extender (AE) | DriverSetup=AE:Dev1 | PXIe-5654/5654 with PXIe-5696 |
| Specify an AWG | DriverSetup=AWG:Dev1 | PXI-5610, PXIe-5611, PXI-5670/5671, PXIe-5672/5673/5673E |
| Specify an external AWG | DriverSetup=AWG:<external> |  |
| Specify an LO | DriverSetup=LO:Dev1 | PXIe-5611, PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842 |
| Specify an external LO | DriverSetup=LO:<external> | PXIe-5611, PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842 |
| Specify an NI-RFSG instrument driver FPGA extensions bitfile | DriverSetup=Bitfile:filename.lvbitx | PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841/5842/5860 |
| Simulate a device | DriverSetup=Model:model number; BoardType:type | Refer to the Simulating an NI RF Signal Generator topic for more information about supported devices. |

#### Configuring the Driver Setup String

1. Use the Driver Setup keyword in the option string 
 parameter of the Initialize with Options function to complete
 the following tasks: Note Specifying an AE, AWG, or LO module in the Driver Setup string
 overrides any different existing association configured in MAX.
  - Specify your hardware device or external (non-NI) device
  - Simulate hardware that is not present
  - Specify an NI-RFSG instrument driver FPGA extensions bitfile
2. Use the following format when configuring the Driver Setup
 string: Tag:Value
3. When specifying or simulating multiple devices, separate the devices with a semicolon, as shown
 in the following
 string: DriverSetup=AWG:pxi1slot4; LO:pxi1slot7

Parent topic:

Programming Considerations

Related concepts:

- NI-RFSG Instrument Driver FPGA Extensions

Related tasks:

- Simulating a Device Using NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=enob.html language=enus -->
## TOPIC 00016: ENOB

- bundle_id: `ni-rfsg`
- source_path: `enob.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/enob.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Effective number of bits (ENOB) is another way of specifying signal-to-noise and distortion ratio (SINAD). ENOB is calculated using the following formula: ENOB = SINAD − 1.76 6.02 Assumes the full scale of the DAC is utilized. The ENOB value is the value of an ideal DAC that is equivalent to the DAC

### ENOB

Effective number of bits (ENOB) is another way of
 specifying signal-to-noise and distortion ratio (SINAD).

ENOB is calculated using the following formula:

ENOB

=

SINAD

−

1.76

6.02

Note

The ENOB value is the value of an ideal DAC that is equivalent to the DAC of the
 device.

Parent topic:

Understanding RF Specifications

Related concepts:

- SINAD

<!--NI_TOPIC bundle=ni-rfsg path=evm.html language=enus -->
## TOPIC 00017: EVM

- bundle_id: `ni-rfsg`
- source_path: `evm.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/evm.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Error vector magnitude (EVM) is a measurement of demodulator performance in the presence of impairments. The soft symbol decisions obtained after decimating the recovered waveform at the demodulator output are compared against the ideal symbol locations. The root mean square (RMS) error vector magni

### EVM

Error vector magnitude (EVM) is a
 measurement of demodulator performance in the presence of impairments.

The soft symbol decisions obtained after decimating the recovered waveform
 at the demodulator output are compared against the ideal symbol locations. The root mean
 square (RMS) error vector magnitude and phase error are then used in determining the EVM
 measurement over a window of *N* demodulated symbols.

As shown in the figure below, the symbol decision output by the
 demodulator is given by

w

̲

v

̲

error vector

e

̲

=

w

̲

−

v

̲

e

̲

[IMAGE alt='image' src='GUID-6FE9E744-DF11-482F-BD6D-30DB55F05A46-a5.gif']

where

- v
 ̲ is the ideal symbol vector
- w
 ̲ is the measured symbol vector
- w
 ̲
 −
 v
 ̲ is the magnitude vector
- ϴ is the phase error
- e
 ̲
 =
 w
 ̲
 −
 v
 ̲ is the error vector
- e
 ̲
 ÷
 v
 ̲ is the EVM

This quantifies, but does not necessarily reveal the nature of, the
 impairment. To remove the dependence on system gain distribution, EVM is normalized by |

v

̲

N

EVM

=

1

N

∑

j

=

1

N

[

(

I

j

−

I

j

˜

)

2

+

(

Q

j

−

Q

˜

j

)

2

]

|

v

̲

max

⁡

|

where

- I j is the I component of the j -th symbol
 received
- Q j is the Q component of the j -th symbol
 received
- I
 j
 ˜ is the ideal I component of the j -th symbol received
- Q
 ˜
 j is the ideal Q component of the j -th symbol received

EVM is related to the modulation error ratio (MER) and *ρ*.
 There is a one-to-one relationship between EVM and MER. Although EVM measures the vector
 difference between the measured and ideal signals, *ρ* measures the correlation
 between the two signals.

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=generate.html language=enus -->
## TOPIC 00018: generate

- bundle_id: `ni-rfsg`
- source_path: `generate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/generate.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the generate instruction to describe which waveform to generate. Usage: Generate a waveform written to the device with the Write Named Waveform VI/function for your driver:generate waveform name Generate a subset of the named waveform:generate <waveform name> subset (<start position>, <length>)S

### generate

Use the generate instruction to describe
 which waveform to generate.

Usage:

- Generate a waveform written to the device with the Write Named Waveform 
 VI/function for your driver: generate waveform
 name
- Generate a subset of the named waveform:generate <waveform name> subset (<start
 position>, <length>)Specify start position and length in
 samples. generate waveform name subset (start
 position, length Specify start
 position and length in samples.
- Generate the waveform and generate a Marker event when a position(s) within the waveform
 is generated: generate waveform name marker0 (position
 1, position 2, ... , position
 n Specify each position in samples. Use the Export
 Signal VI/function for your driver to specify the destination terminal of the
 marker. Marker position is zero-based. For example, 0 refers to the first
 point in the waveform, 999 refers to the 1,000th point in the waveform,
 and so on.
- Generate a subset of the named waveform and generate a Marker event when a position(s)
 within the waveform is generated: generate waveform name
 subset(start position), length) marker0
 (list of positions) Specify
 positions and length in samples. When a subset and markers are specified in the same
 generate instruction, the marker positions are relative to the
 subset.

#### Generating waveforms

Assume myWfm in each example has 1,024 samples.

- Generate myWfm generate myWfm
- Generate 10 samples of myWfm starting at sample
 40 generate myWfm subset (40, 10)
- Generate myWfm and generate a marker at the start of the waveform
 (sample 0) generate myWfm marker0 (0)
- Generate myWfm and generate a marker at positions 10 and
 80 generate myWfm marker0 (10, 80)
- Generate 10 samples of myWfm starting at sample 40, and generate a
 marker at position 6 of the
 subset generate myWfm subset (40, 10) marker0 (6)

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=generating-a-cw-tone-in-the-ni-rfsg-sfp.html language=enus -->
## TOPIC 00019: Generating a CW Tone in the NI-RFSG SFP

- bundle_id: `ni-rfsg`
- source_path: `generating-a-cw-tone-in-the-ni-rfsg-sfp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/generating-a-cw-tone-in-the-ni-rfsg-sfp.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To use the NI-RFSG SFP with your device, you must first configure the device in Measurement & Automation Explorer (MAX). Refer to the getting started guide for your device for information about configuring and associating your device(s) in MAX. Open the NI-RFSG SFP by selecting Start National Instru

### Generating a CW Tone in the NI-RFSG SFP

Note

NI-RFSG

1. Open the NI-RFSG SFP by selecting Start»National Instruments»NI-RFSG»NI-RFSG Soft Front Panel.
2. Depending on the number of devices you have configured: 
 
 Tip You can run multiple instances of the NI-RFSG SFP if you have multiple devices installed in your
 chassis. Select File»New Window to open
 another instance of the SFP. Each new instance of the SFP opens in a separate
 application window.
  - If you have more than one device configured in MAX, select
 a device in the Select Device dialog box and click
 OK .
  - If you have only one device configured, the SFP
 automatically opens a session for that device.
  - If you do not have devices configured for use with the
 SFP, a message displays to indicate no RF devices are available.
3. Click the RF On/Off button to generate the RF signal at the RF
 output terminal of your device.
4. Adjust the frequency. 
 
 Note Some parameter values are coerced to a value supported by the
 current device. Actual (coerced) values display in the Device Configuration
 Area, while the data entry field and softkey continue to display the
 desired value.
  1. Click the Freq button to display the
 Frequency softkey menu.
  2. Use the keypad, knob, keyboard, or mouse to specify a frequency.
5. Adjust the power level. 
 
 Note The NI-RFSG SFP interprets the
 power level as average power.
  1. Click the Level button to display the
 Level softkey menu.
  2. Use the keypad, knob, keyboard, or mouse to specify a power level.
6. Monitor your device to view the generated signal.

Parent topic:

NI-RFSG Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsg path=generating-a-signal-using-the-ni-rfsg-soft-fr.html language=enus -->
## TOPIC 00020: Generating a Signal Using the NI-RFSG Soft Front Panel

- bundle_id: `ni-rfsg`
- source_path: `generating-a-signal-using-the-ni-rfsg-soft-fr.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/generating-a-signal-using-the-ni-rfsg-soft-fr.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To verify your device configuration, use the NI-RFSG Soft Front Panel (SFP) in MAX to generate a simple signal. The NI-RFSG SFP allows you to interactively control your NI-RFSG device and tests all the hardware modules as a single instrument. Select the device name in the configuration tree. Click S

### Generating a Signal Using the NI-RFSG Soft Front Panel

To verify your device configuration, use the NI-RFSG Soft Front Panel (SFP) in MAX to generate a simple signal.
 The NI-RFSG SFP allows you to interactively control your NI-RFSG device and tests all the hardware modules as a single
 instrument.

1. Select the device name in the configuration tree.
2. Click Soft Front Panel in the MAX toolbar. 
 The NI-RFSG SFP launches.
3. In the NI-RFSG SFP, specify a frequency and a power
 level for signal generation. 
 Notice Clicking RF On/Off
 generates a signal from the output terminals on the device. Disconnect any equipment
 that can be damaged by the test signal prior to clicking the RF
 On/Off button on the NI-RFSG SFP.
4. Click RF On/Off to begin signal generation. 
 During signal generation the ACTIVE LED on the
 NI-RFSG device illuminates.
5. Click RF On/Off to stop the signal generation.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=getting-started.html language=enus -->
## TOPIC 00021: Getting Started

- bundle_id: `ni-rfsg`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/getting-started.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your NI-RFSG device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks: Install the software and hardware Interconnect multiple modules Configure and associate the hardware in MAX Progra

### Getting Started

To get started using your NI-RFSG device and driver software,
 refer to the getting started guide for your device. The getting started guide explains how to
 complete the following tasks:

- Install the software and hardware
- Interconnect multiple modules
- Configure and associate the hardware in MAX
- Program the hardware
- Generate a signal
- Troubleshoot

The getting started guide for your device is printed in your hardware kit, installed with the
 driver software, and available at ni.com/manuals.

Tip

- [Creating an Application with NI-RFSG](creating-an-application-with-ni-rfsg.html) To create your application, you need the NI-RFSG instrument driver to control your device.

<!--NI_TOPIC bundle=ni-rfsg path=harmonic-distortion.html language=enus -->
## TOPIC 00022: Harmonic Distortion

- bundle_id: `ni-rfsg`
- source_path: `harmonic-distortion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/harmonic-distortion.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Harmonic distortion measures the amount of power that is contained in the harmonics of a fundamental signal. Harmonic distortion is inherent to devices and systems that possess nonlinear characteristics—the more nonlinear the device, the greater its harmonic distortion. Harmonic distortion can be ex

### Harmonic Distortion

Harmonic distortion measures the amount of power that is
 contained in the harmonics of a fundamental signal. Harmonic distortion is inherent to devices
 and systems that possess nonlinear characteristics—the more nonlinear the device, the greater
 its harmonic distortion.

Harmonic distortion can be expressed as a power ratio or as a percentage
 ratio. Use the following formula to express it as a power ratio:

P

HD

=

P

fund

−

P

harm

(

dbc

)

where

- P HD is the power of the harmonic distortion in dBc
- P fund is the fundamental signal power in dB or dBm
- P harm is the power of the harmonic or interest in dB or dBm

Convert power to voltage and use the following equation to express
 harmonic distortion as a percentage ratio:

Percentage

⁢

of

⁢

Distortion

⁢

=

V

harm

V

fund

×

100

%

Parent topic:

Understanding RF Specifications

Related concepts:

- Total Harmonic Distortion

<!--NI_TOPIC bundle=ni-rfsg path=ifelseend-if.html language=enus -->
## TOPIC 00023: if/else/end if

- bundle_id: `ni-rfsg`
- source_path: `ifelseend-if.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ifelseend-if.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the if/else/end if instruction to determine what sections of a script to execute, based on whether a particular Script trigger was received. Usage:Execute a set of instructions if the device receives a Script trigger, execute another set of instructions otherwise:if scriptTrigger0 instructions e

### if/else/end if

Use the if/else/end if instruction to
 determine what sections of a script to execute, based on whether a particular Script trigger
 was received.

Usage:

- Execute a set of instructions if the device receives a Script trigger, execute another set of
 instructions
 otherwise: if scriptTrigger0
 instructions
else
 instructions
end if
- Execute a set of instructions if the device receives a Script
 trigger: if scriptTrigger0
 instructions
end if
- Execute a set of instructions if the device has not received a Script trigger: if
 scriptTrigger0 else <instructions> end
 if if scriptTrigger0
else
 instructions
end if

Note

if/else/end if

generate

N

if/else/end if

if/else/end if

repeat until

N

#### if/else/end if Examples

- Generate myWfmB five times if a Script trigger is received, otherwise
 generate
 myWfmC : generate myWfmA
if scripttrigger0
 repeat 5
 generate myWfmB
 end repeat
else
 generate myWfmC
end if
- Generate myWfmA if two Script triggers were
 received: wait 8
if scripttrigger0
 wait 8
 if scripttrigger1
 generate myWfmA
 end if
end if
- Generate myWfmA if Script trigger 0 was received, or generate
 myWfmB if Script trigger 1 was received, otherwise generate
 myWfmC : wait 8
if scripttrigger0
 generate myWfmA
else
 wait 8
 if scripttrigger1
 generate myWfmB
 else
 generate myWfmC
 end if
end if
- If an error is flagged in the form of a Script trigger while generating a waveform, do
 not generate all subsequent
 waveforms: generate myWfmA
if scripttrigger0
else
 generate myWfmB
 if scripttrigger0
 else
 generate myWfmC
 end if
end if

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=imd3.html language=enus -->
## TOPIC 00024: IMD3

- bundle_id: `ni-rfsg`
- source_path: `imd3.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/imd3.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Two-tone third-order intermodulation distortion (IMD3) is the measure of the third-order distortion products produced by a nonlinear device when two tones closely spaced in frequency are fed into its input. This distortion product is usually so close to the carrier that it is almost impossible to fi

### IMD3

Two-tone third-order intermodulation distortion (IMD3) is
 the measure of the third-order distortion products produced by a nonlinear device when two
 tones closely spaced in frequency are fed into its input. This distortion product is usually
 so close to the carrier that it is almost impossible to filter out and can cause
 interference in multichannel communications equipment.

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=impedance-matching.html language=enus -->
## TOPIC 00025: NI-RFSG Impedance Matching

- bundle_id: `ni-rfsg`
- source_path: `impedance-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/impedance-matching.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: When broadband signals are transmitted on lines of any significant length, impedance discontinuities or mismatches degrade the amplitude and phase accuracy, as well as the temporal fidelity, of waveforms generated with a signal generator. To minimize signal reflections, the source and load impedance

### NI-RFSG
 Impedance Matching

When broadband signals are transmitted on lines of any
 significant length, impedance discontinuities or mismatches degrade the amplitude and phase
 accuracy, as well as the temporal fidelity, of waveforms generated with a signal generator.
 To minimize signal reflections, the source and load impedances should equal the
 characteristic impedance of the transmission line.

One of the most common mismatch errors encountered in such
 measurements is shown in the following figure:

Figure 6.

[IMAGE alt='image' src='GUID-81CC325E-05A5-49C8-A2BF-6828F5B64A79-a5.svg']

In this example, selectable source impedances are provided at the
 signal generator outputs to accommodate the most popular coaxial cable characteristic
 impedances: 50 Ω and 75 Ω.

Consider an example where a 50 Ω
 coaxial cable connects 75 Ω source and load impedances.
 The following figure shows the discontinuities that occur in this situation and how they
 compare to a matched cable:

Figure 7.

[IMAGE alt='image' src='GUID-A00BD202-3A85-4826-ABA6-675B2B39721B-a5.svg']

The pulse encounters impedance mismatches at each end of the cable,
 and the pulse is partially reflected. The reflected pulse traverses the cable back and
 forth numerous times, diminishing at each end by the reflection coefficient, Γ:

Γ

=

v

r

v

i

=

z

t

−

z

0

z

t

+

z

0

where

- v r = reflected voltage
- v i = incident voltage
- z t = terminating impedance
- z 0 = characteristic impedance

The resulting voltage waveform is distorted by the asymptotic decay of
 the reflected pulse as shown, exaggerated for visual effect. Impedance discontinuities
 of smaller magnitude and/or duration have correspondingly smaller effects. Also
 displayed is the waveform that results when a cable of matched impedance (75 Ω) is used.

#### Mismatch
 Uncertainty

Impedance matching is also important for preserving the
 absolute delivered power from a device. The accuracy with which power can be
 delivered is limited by mismatch error. The mismatch error in a z<sub>0</sub> system
 can be shown to be bounded by:

(

1

−

|

Γ

L

|

2

)

(

1

+

|

Γ

L

|

⋅

|

Γ

G

|

)

2

≤

mismatch error

≤

(

1

−

|

Γ

L

|

2

)

(

1

−

|

Γ

L

|

⋅

|

Γ

G

|

)

2

where

- Γ L = load reflection coefficient
- Γ G = generator reflection coefficient

The denominator term represents mismatch uncertainty, which is a fundamental
 limit to the power transfer accuracy that can be achieved across a mismatched
 junction.

#### Resistive Matching

You can use a resistor in series (shunt) to match the total source
 impedance (admittance) that an RF signal generator sees to the characteristic
 impedance (admittance) of a cable. This method works for RF signal generates with
 low or high source impedance.

RF signal generators that are not capable of
 driving the cable impedance directly can be coupled through a matching L-pad. In
 this case, the RF signal generator sees an approximately 500 Ω load, while the source impedance presented to the cable is 50 Ω.

Refer to the following figure:

Figure 8.

[IMAGE alt='image' src='GUID-99092191-5F71-49FA-A449-E8E3222F2E55-a5.svg']

To minimize parasitic effects, use high-frequency components and layout
 techniques throughout.

<!--NI_TOPIC bundle=ni-rfsg path=importing-data-to-the-ni-rfsg-sfp-for-generat.html language=enus -->
## TOPIC 00026: Importing Data to the NI-RFSG SFP for Generation

- bundle_id: `ni-rfsg`
- source_path: `importing-data-to-the-ni-rfsg-sfp-for-generat.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/importing-data-to-the-ni-rfsg-sfp-for-generat.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To use the NI-RFSG SFP with your device, you must first configure the device in Measurement & Automation Explorer (MAX). Refer to the getting started guide for your device for information about configuring and associating your device(s) in MAX. Open the NI-RFSG SFP by selecting Start National Instru

### Importing Data to the NI-RFSG SFP for Generation

NI-RFSG

1. Open the NI-RFSG SFP by selecting Start»National Instruments»NI-RFSG»NI-RFSG Soft Front Panel.
2. Depending on the devices you have configured: 
 
 Tip Click the
 Preset button to return the SFP to the default
 settings if you previously generated a CW tone or changed any
 settings.
  - If you have more than one device configured in MAX, select a device in
 the Select Device dialog box and click
 OK .
  - If you have only one device configured, the SFP automatically opens a
 session for that device.
  - If you do not have devices that are configured for use with the SFP, a
 message displays to indicate no RF devices are available.
3. Select the arbitrary waveform mode.
  1. Click the Mode button to display the
 Mode softkey menu.
  2. Click the Arb softkey to select arbitrary
 waveform mode and display the Arb softkey
 menu.
4. Load a waveform file.
  1. In the Arb softkey menu, click the
 Load IQ File softkey.
  2. Click Load Text File to open the
 Import Text File dialog box.
  3. Navigate to the <Users>\Public\Documents\National
 Instruments\NI-RFSG Soft Front Panel\examples\Waveforms
 folder.
  4. Select the TwoTone_IQ100MHz_2D.txt text file and
 click OK.
  5. In the Import parameters dialog box, specify the
 file and the data information.
  6. Click OK to import the data.
  7. Click Return to return to the
 Arb softkey menu.
5. Click the RF On/Off button to transmit the RF signal to
 your device.
6. Optional: 
 Preview the signal on the SFP. 
 
 Tip Adjust the
 bottom display area splitter bar to change the size of the graph.
  1. Click the Preview Data softkey to display a
 preview of the signal on the SFP.
  2. Click the CCDF softkey to display a CCDF graph
 of the loaded waveform.

Parent topic:

NI-RFSG Soft Front Panel

Related concepts:

- Supported Data File Formats in the NI-RFSG SFP

Related tasks:

- Modeling I/Q Impairments in the NI-RFSG SFP

<!--NI_TOPIC bundle=ni-rfsg path=improving-streaming-performance.html language=enus -->
## TOPIC 00027: Improving NI-RFSG Streaming Performance

- bundle_id: `ni-rfsg`
- source_path: `improving-streaming-performance.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/improving-streaming-performance.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Note after DITA conversion of NI-RFSG driver help, which sourced this topic. This topic is written as if it is generic to all RFSG instruments, but if you look at which devices the properties are supported by, it's clear this topic is relevant only to 567x instruments. Don't use in a generic sense.

### Improving NI-RFSG Streaming Performance

To improve your maximum sustainable transfer rate for streaming,
 consider the following recommendations:

- Adjust the Data Transfer Block Size property or
 the NIRFSG_ATTR_DATA_TRANSFER_BLOCK_SIZE attribute. The default
 data transfer block size for NI-RFSG is 8 MS (or 16 MB ). If
 you were to write a 32 MB waveform to the RF signal
 generator, the complete transfer would occur using four separate DMA transfers. If
 you modify the data transfer block size to 16 MS ( 32 MB ), for example, the data transfer is more
 efficient and is instead accomplished in a single transfer.
- Configure advanced streaming properties by calling the
 Maximum In-Flight Reads or Preferred Packet
 Size property or the
 NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS or
 NIRFSG_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE 
 attributes.
- Optimize the bus bandwidth usage for multi-device streaming
 applications by calling the Maximum Bandwidth property or the
 NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH attribute.
- When streaming from hard drives, consider the hard drive speed
 for maximum sustainable rates. Laptop hard drives typically have a data transfer
 rate of 25 MB/s to 30 MB/s . Desktop hard drives often can meet 55 MB/s to 70 MB/s . Transfer rates from hard drives can vary for a number of reasons, including
 where the data is physically stored on the hard drive and how much data is
 stored. Storing your waveform files on a fairly empty, defragmented hard drive
 may help increase performance.
- Consider using a redundant array of independent disks (RAID)
 configuration to utilize striping to increase data transfer rates from disk.
- When using 18-slot PXI chassis, install the RF signal generator
 used for streaming in the first segment (Slots 2 to 6) of the PXI chassis.

Parent topic:

NI-RFSG Streaming

<!--NI_TOPIC bundle=ni-rfsg path=iq-modulation.html language=enus -->
## TOPIC 00028: I/Q Modulation

- bundle_id: `ni-rfsg`
- source_path: `iq-modulation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/iq-modulation.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: I/Q is a common way to represent message signals in modern communication systems. As described in the Modulation topic, there are two fundamental ways (degrees of freedom) to produce a modulated wave from a carrier wave. You can either perturb its amplitude or its phase. I/Q signaling allows you to

### I/Q Modulation

I/Q is a common way to represent message signals in modern
 communication systems.

As described in the Modulation topic, there are two
 fundamental ways (degrees of freedom) to produce a modulated wave from a carrier wave.
 You can either perturb its amplitude or its phase. I/Q signaling allows you to
 simultaneously change both amplitude and phase. Using both degrees of freedom when
 modulating a carrier allows greater spectral efficiency with regard to bits per hertz of
 channel bandwidth (for a given bits per second transmission rate) than if using only one
 degree of freedom.

To simultaneously perturb both the amplitude and phase of a carrier,
 two canonical forms of frequency-translating transmitters simultaneously use the two
 degrees of freedom in modulation. These canonical forms are described in the following
 sections.

#### Canonical Polar Modulation

[IMAGE alt='image' src='GUID-9D08C194-D364-4FC6-86D6-373A82A5C331-a5.gif']

In polar modulation, the message signal is split into two components: R(t) controls the carrier wave amplitude changes, and φ(t) drives the carrier wave phase changes.

#### Canonical Rectangular Modulation

[IMAGE alt='image' src='GUID-4CB395EC-29DF-4CE2-89EB-763EE2A4164C-a5.gif']

In rectangular modulation, the message signal is also split into two components: I(t) controls the in-phase carrier wave changes, and Q(t) controls the quadrature-phase carrier wave changes.

#### The Mathematical
 Relationship

The modulated outputs of the two canonical forms are
 mathematically and physically equivalent. To show their equality, you can compare
 and translate between the polar and rectangular representations.

Begin with
 the equation

R

(

t

)

cos

(

ω

c

(

t

)

+

φ

(

t

)

)

Plug in the following trigonometric identity

cos

(

α

+

β

)

=

cos

(

α

)

cos

(

β

)

−

sin

(

α

)

sin

(

β

)

to yield the following equation:

R

(

t

)

[

cos

ω

c

(

t

)

cos

φ

(

t

)

−

sin

ω

c

(

t

)

sin

φ

(

t

)

]

When you simplify this equation, you have the following relationship:

I

(

t

)

cos

(

ω

c

(

t

)

)

−

Q

(

t

)

sin

(

ω

c

(

t

)

)

where

- I
 (
 t
 )
 =
 R
 (
 t
 )
 cos
 (
 φ
 (
 t
 )
 )
- Q
 (
 t
 )
 =
 R
 (
 t
 )
 sin
 (
 φ
 (
 t
 )
 )
- ω
 c
 =
 2
 π
 f
 c
- f
 c is the carrier frequency in hertz

The rectangular form of modulation, often called I/Q
 Modulation, has become popular for certain technical reasons.

In
 the rectangular modulation figure, the real baseband signals of
 I(t) and
 Q(t) are created (in some way) to contain
 all the information of message input m(t).
 (The polar R(t) and
 φ(t) also contain the information of
 m(t).) Because the carriers
 cos(ω<sub>c</sub>(t)) and
 sin(ω<sub>c</sub>(t)) are orthogonal functions, we use the
 terminology of quadrature modulation, where the signal applied to
 the cosine mixer is called the in-phase component (I), and the
 signal applied to the sine mixer is called the quadrature-phase
 component (Q). The I and Q
 designations are useful because the I(t)
 baseband signal is applied to the cosine mixer, and the
 Q(t) baseband signal is applied to the
 sine mixer.

The analytical relationship between the polar form
 (R(t) and
 φ(t)) of the baseband signal and Cartesian
 form (I(t) and
 Q(t)) of the baseband signal is shown in
 the following figure.

[IMAGE alt='image' src='GUID-730FB158-6B3D-4713-8AA9-053E867A30E9-a5.gif']

The diagram is a "snapshot in time" of the complex (analytical)
 baseband envelope g(t). Because the diagram is
 for an arbitrary instant in time, the independent time variable t
 is dropped. The amplitude of Q is projected onto the imaginary
 (j) axis and the amplitude of I is
 projected onto the real axis.

Note

Digital and Analog Communication Systems

I/Q modulation produces a single-sideband suppressed carrier
 waveform to modulate baseband signals. A lower sideband suppressed carrier can be
 configured with the following equations:

R

F

1

=

sin

(

w

c

t

)

⋅

A

sin

(

w

b

t

)

=

(

A

2

cos

(

(

w

c

−

w

b

)

t

)

)

−

(

A

2

cos

(

(

w

c

+

w

b

)

t

)

)

R

F

2

=

cos

(

w

b

t

)

⋅

A

cos

(

w

b

t

)

=

(

A

2

cos

(

(

w

c

−

w

b

)

t

)

)

+

(

A

2

cos

(

(

w

c

+

w

b

)

t

)

)

where

- w
 c represents the carrier frequency
- w
 b represents the baseband frequency
- t represents time

Parent topic:

Modulation

<!--NI_TOPIC bundle=ni-rfsg path=locating-an-ni-rfsg-device.html language=enus -->
## TOPIC 00029: Locating an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `locating-an-ni-rfsg-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/locating-an-ni-rfsg-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: Locate your NI-RFSG device in MAX in Devices and Interfaces. To locate your NI-RFSG device in MAX, complete the following steps: In the configuration tree, double-click Devices and Interfaces to see a list of installed devices. If you are using your NI-RFSG device with the LabVIEW Real-Time Module,

### Locating an NI-RFSG Device

Locate your NI-RFSG device in MAX in Devices and
 Interfaces.

To locate your NI-RFSG device in MAX,
 complete the following steps:

1. In the configuration tree, double-click Devices and Interfaces
 to see a list of installed devices. 
 Note If you are using your NI-RFSG
 device with the LabVIEW Real-Time Module, expand Remote Systems.
 Find your target IP address or name, expand it, and then expand Devices and
 Interfaces 
 Installed devices appear under the name of their associated
 chassis.
2. Expand your chassis tree item. MAX lists all devices installed in the chassis. Your
 default device names may vary.
3. Record the device identifier MAX assigns to the hardware. Use this identifier when
 programming your NI-RFSG device. 
 Tip Instead of using the default naming convention, you
 can also choose to rename your devices in MAX.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

Related tasks:

- Renaming an NI-RFSG Device

<!--NI_TOPIC bundle=ni-rfsg path=manage-errors-warnings-net.html language=enus -->
## TOPIC 00030: Errors and Warnings in the .NET Class Library

- bundle_id: `ni-rfsg`
- source_path: `manage-errors-warnings-net.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/manage-errors-warnings-net.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The .NET Class Library manages errors and warnings by converting error codes into exceptions and warning codes into events. Subscribe to the Warning event to handle warnings effectively, ensuring you capture all potential warnings. The driver reports errors or warnings through the method return valu

### Errors and Warnings in the .NET Class Library

The .NET Class Library manages errors and
 warnings by converting error codes into exceptions and warning codes into events. Subscribe
 to the Warning event to handle warnings effectively, ensuring you capture all potential
 warnings.

The driver reports errors or warnings through the
 method return values. Negative return values indicate errors and positive values
 indicate warnings.

The .NET class library converts the error codes into
 exceptions. All exceptions are either .NET defined or IVI defined; none of them are
 custom exceptions. The exception message for driver errors includes the driver error
 code at the end.

#### Subscribe to Warning Events

The .NET class library converts the warning
 codes into events. To receive warnings, you must subscribe to the Warning event as
 follows:

```text
VB.NET

AddHandler session.DriverOperation.Warning, AddressOf Me.DriverOperation_Warning

Private Sub DriverOperation_Warning(ByVal sender As Object, ByVal e As RfsgWarningEventArgs)
    'User code goes here 
End Sub
```

```text
Visual C#

session.DriverOperation.Warning += new EventHandler<RfsgWarningEventArgs>(DriverOperation_Warning);

void DriverOperation_Warning(object sender, RfsgWarningEventArgs e)
{
    //User code goes here
}
```

Note

NIRfsg

The RfsgWarningEventArgs class contains a read-only property to
 get the RfsgWarning object out. For ease-of-use, it also gives
 direct access to the warning’s Code and
 Message.

RfsgWarning is an immutable class and hence its
 Equals method and the == operator are
 overloaded to compare values and not references.

The driver dynamically generates the warning message for a particular warning code,
 so it's possible for a warning with same code to have different messages. The
 default behavior of the Equals method checks the value equality
 of both the Code and the Message. However,
 there is an overload of the Equals method that lets you ignore
 the Message when comparing two warnings.

Parent topic:

Using the .NET Class Library

<!--NI_TOPIC bundle=ni-rfsg path=markers.html language=enus -->
## TOPIC 00031: NI-RFSG Marker Event Details

- bundle_id: `ni-rfsg`
- source_path: `markers.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/markers.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: A marker is an event that an NI RF signal generator produces in relation to a waveform that is generated. The marker event is delayed slightly relative to the leading edge of the waveform that it marks. By default, the marker event is a pulse of fixed width. The following figure shows a waveform gen

### NI-RFSG Marker
 Event Details

A *marker* is an event that an NI RF signal
 generator produces in relation to a waveform that is generated. The marker event is delayed
 slightly relative to the leading edge of the waveform that it marks.

By default, the marker event is a pulse of fixed width. The following
 figure shows a waveform generated on the output of a waveform generator. The waveform
 contains a pulse that represents a waveform sample *n* that is one Sample
 Clock in width. The second pulse, the marker event, represents the pulse that generates
 when the corresponding waveform sample *n* is output at the output
 connector.

Figure 5.

[IMAGE alt='image' src='GUID-B1CB55F0-19D6-46EB-BEB3-405C49F00CBC-a5.svg']

m1

n

NI-RFSG

Events Delay

Relative Delay

m2

NI-RFSG

Width Units

Width Value

You can use NI-RFSG to configure the
 characteristics of the pulse generated as the Marker event.

In addition, you can use scripts to create markers to develop complex
 behaviors around generated waveforms.

For example, you can configure the Marker event as a toggled digital pulse signal that
 changes state between a low level and high level. While the basic pulse option for
 Marker events generates event pulses of fixed width, using the toggle option allows you
 to use scripts to change the duration of the Marker event pulse. You can control the
 initial state of the toggled pulse with
 MarkerEvent.Toggle.InitialState.

Parent topic:

NI-RFSG Event Types

<!--NI_TOPIC bundle=ni-rfsg path=max-help-for-ni-rfsg-devices.html language=enus -->
## TOPIC 00032: Using Measurement & Automation Explorer for NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `max-help-for-ni-rfsg-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/max-help-for-ni-rfsg-devices.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to complete the most common NI-RFSG tasks in Measurement & Automation Explorer (MAX). You can launch MAX by navigating to Start All Programs National Instruments NI MAX or by selecting the NI MAX desktop icon.

### Using Measurement & Automation Explorer
 for NI-RFSG

Learn how to complete the most common NI-RFSG tasks in
 Measurement & Automation Explorer (MAX).

You can launch MAX by navigating to Start»All Programs»National Instruments»NI MAX or by selecting the NI MAX desktop icon.

- [Locating an NI-RFSG Device](locating-an-ni-rfsg-device.html) Locate your NI-RFSG device in MAX in Devices and Interfaces .
- [Removing an NI-RFSG Device](removing-ni-rfsg-instrument.html)
- [Simulating an NI-RFSG Device](simulating-an-ni-rfsg-device.html) Simulate an NI-RFSG device using MAX to develop, modify, and/or test an application without hardware.
- [Associating NI-RFSG Modules](associating-ni-rfsg-modules.html) To control multiple hardware modules as a single RF device, you must first associate the modules in MAX.
- [Generating a Signal Using the NI-RFSG Soft Front Panel](generating-a-signal-using-the-ni-rfsg-soft-fr.html) To verify your device configuration, use the NI-RFSG Soft Front Panel (SFP) in MAX to generate a simple signal. The NI-RFSG SFP allows you to interactively control your NI-RFSG device and tests all the hardware modules as a single instrument.
- [Renaming an NI-RFSG Device](renaming-an-ni-rfsg-device.html) MAX allows you to rename each of your NI-RFSG devices. NI-RFSG uses the MAX name to operate the hardware resources.
- [Resetting an NI-RFSG Device](resetting-an-ni-rfsg-device.html)
- [Running a Self-Test on an NI-RFSG Device](running-a-self-test-on-an-ni-rfsg-device.html) The MAX self-test performs a basic verification of hardware resources.
- [Creating Static Signal Routes for an NI-RFSG Device](creating-static-signal-routes-for-an-ni-rfsg-.html)
- [Detecting and Identifying NI-RFSG Devices](detecting-and-identifying-ni-rfsg-devices.html) To share triggers or clocks to synchronize devices, you must properly detect and identify your chassis and controller in MAX.
- [A Device Does Not Appear in MAX](a-device-does-not-appear-in-max.html)

<!--NI_TOPIC bundle=ni-rfsg path=mer.html language=enus -->
## TOPIC 00033: MER

- bundle_id: `ni-rfsg`
- source_path: `mer.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/mer.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The modulation error ratio (MER) is a measure of the signal-to-noise ratio (SNR) in a digitally modulated signal. Like SNR, MER is usually expressed in dB. MER over N number of symbols is defined as the following equation: MER = ∑ j = 1 ( I ˜ j 2 + Q ˜ j 2 ) ∑ j = 1 N [ ( I j − I ˜ j ) 2 + ( Q j − Q

### MER

The modulation error ratio (MER) is a
 measure of the signal-to-noise ratio (SNR) in a digitally modulated signal. Like SNR, MER is
 usually expressed in dB.

MER over *N* number of symbols is defined as the following
 equation:

MER

=

∑

j

=

1

(

I

˜

j

2

+

Q

˜

j

2

)

∑

j

=

1

N

[

(

I

j

−

I

˜

j

)

2

+

(

Q

j

−

Q

˜

j

)

2

]

where

- I
 j is the I component of the j -th symbol received
- Q
 j is the Q component of the j -th symbol received
- I
 ˜
 j is the ideal I component of the j -th symbol received
- Q
 ˜
 j is the ideal Q component of the j -th symbol received

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=message-signal.html language=enus -->
## TOPIC 00034: Message Signal

- bundle_id: `ni-rfsg`
- source_path: `message-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/message-signal.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The message signal contains the data for transmission. The message signal is used to modulate the carrier wave to create the modulated wave for transmission. The message signal data is recovered from the modulated wave by a process of demodulation. The message signal is often referred to as the base

### Message Signal

The *message signal* contains the data for
 transmission.

The message signal is used to modulate the carrier wave to create the
 modulated wave for transmission. The message signal data is recovered from the modulated
 wave by a process of demodulation.

The message signal is often referred to as the *baseband
 signal*.

Parent topic:

NI-RFSG RF Fundamentals

Related concepts:

- Carrier Wave
- Modulation

<!--NI_TOPIC bundle=ni-rfsg path=modeling-iq-impairments-in-the-ni-rfsg-sfp.html language=enus -->
## TOPIC 00035: Modeling I/Q Impairments in the NI-RFSG SFP

- bundle_id: `ni-rfsg`
- source_path: `modeling-iq-impairments-in-the-ni-rfsg-sfp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/modeling-iq-impairments-in-the-ni-rfsg-sfp.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the NI-RFSG SFP to model I/Q impairments on imported signals. You can model I/Q impairments on only the NI 5673/5673E vector signal generator. Import signals for which you want to model I/Q impairments. Enable I/Q impairments. In the Arb softkey menu, click the IQ Impairments softkey to

### Modeling I/Q Impairments in the NI-RFSG SFP

You can use the NI-RFSG SFP
 to model I/Q impairments on imported signals. You can model I/Q impairments on only the NI 5673/5673E vector signal generator.

1. Import signals for which you want to model I/Q impairments.
2. Enable I/Q impairments.
  1. In the Arb softkey menu, click the IQ
 Impairments softkey to display the IQ
 Impairments softkey menu.
  2. Click the Impairments softkey to enable I/Q
 impairments.
3. Specify I/Q impairments. 
 
 Note The up, down, left, and right specifications for the
 effects of I/Q impairments on the data assume that the data is displayed on
 an I/Q graph where I is the x-axis and Q is the y-axis.
  - I Offset: Specifies the I-signal DC offset, in
 percent (%). The arbitrary waveform generator (AWG) offset is the specified
 percentage of the AWG peak power level. Actual AWG signal offset is equal to
 the I/Q modulator offset correction plus the value specified in this
 parameter. A negative offset shifts the locus of the symbol coordinates left
 of center in the I/Q plane. A positive offset shifts the locus of the
 coordinates right of center in the I/Q plane. Valid offset range is -100% to
 100%.
  - Q Offset: Specifies the Q-signal DC offset, in
 percent (%). The AWG offset is the specified percentage of the AWG peak
 power level. Actual AWG signal offset is equal to the I/Q modulator offset
 correction plus the value specified in this parameter. A negative offset
 shifts the locus of the symbol coordinates lower in the I/Q plane. A
 positive offset shifts the locus of the coordinates higher in the I/Q plane.
 Valid offset range is -100% to 100%.
  - Gain Imbalance: Specifies the gain imbalance of
 the I/Q modulator (I versus Q), in dB. I/Q gain imbalance is the difference
 in scaling between the I and Q components. A positive value indicates that
 the I component is impaired. A negative value indicates that the Q component
 is impaired. Valid gain imbalance range is -6 dB to 6 dB .
  - IQ Skew: Specifies the adjustment of the phase
 angle between the I and Q vectors, in degrees (°). If the skew is zero, the
 phase angle is 90°. A negative skew twists the constellation to the left. A
 positive skew twists the constellation to the right. Valid skew range is
 -30° to 30°.
4. Preview the signal on the SFP.
  1. Click the Preview Data softkey on the
 Arb softkey menu to display a preview of the
 signal on the SFP.
  2. Click the I vs Q softkey to plot the I and Q
 signals.

Parent topic:

NI-RFSG Soft Front Panel

Related tasks:

- Importing Data to the NI-RFSG SFP for Generation

<!--NI_TOPIC bundle=ni-rfsg path=modulation.html language=enus -->
## TOPIC 00036: Modulation

- bundle_id: `ni-rfsg`
- source_path: `modulation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/modulation.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modulation is a process that alters the characteristics of a carrier wave according to information in the message signal to generate and transmit a modulated wave. There are several different types of modulation. The unmodulated carrier is represented by the following equation: v ( t ) = A c cos ( 2

### Modulation

Modulation is a process that alters the
 characteristics of a carrier wave according to information in the message signal to generate
 and transmit a modulated wave. There are several different types of modulation.

The unmodulated carrier is represented by
 the following equation:

v

(

t

)

=

A

c

cos

(

2

π

f

t

+

φ

)

The amplitude-modulated carrier signal is represented by the following
 equation:

v

(

t

)

=

(

m

(

t

)

+

A

c

)

cos

(

2

π

f

t

+

φ

)

The frequency-modulated carrier signal is represented by the following
 equation:

v

(

t

)

=

A

c

(

(

m

(

t

)

+

2

π

f

)

t

+

φ

)

This yields the following equation:

A

c

cos

(

2

π

f

t

+

φ

+

∫

m

(

t

)

ⅆ

t

)

The phase-modulated carrier signal is represented by the following
 equation:

v

(

t

)

=

A

c

cos

(

2

π

f

t

+

φ

+

m

(

t

)

)

where

- m(t) is the time-varying modulation
- A c is the amplitude of the carrier wave
- f is the frequency of the carrier wave

Parent topic:

NI-RFSG RF Fundamentals

Related concepts:

- Message Signal
- Carrier Wave

<!--NI_TOPIC bundle=ni-rfsg path=net-values-for-properties.html language=enus -->
## TOPIC 00037: Using Predefined or Custom Values for Source and Output Terminal Properties

- bundle_id: `ni-rfsg`
- source_path: `net-values-for-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/net-values-for-properties.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use predefined values or custom values for source properties or output terminal properties in the .NET API. How Do I Pass a Predefined Value to an Property? There are certain properties, such as trigger sources, clock sources, and output terminals, that work with a set of predefined str

### Using Predefined or Custom Values for Source
 and Output Terminal Properties

Learn how to use predefined values or custom values for source properties or output
 terminal properties in the .NET API.

#### How Do I Pass a Predefined Value to an 
 Property?

There are certain properties, such as trigger sources, clock sources, and output
 terminals, that work with a set of predefined string values, but might also accept
 custom values. For this you can use the utility classes that are part of .NET API. For example, the
 Source property in
 RfsgDigitalEdgeStartTrigger specifies an
 RfsgDigitalEdgeStartTriggerSource object. You can configure
 Source using one of the predefined values, such as:

```text
VB.NET

session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.Pfi0
```

```text
Visual C#

session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.Pfi0;
```

Similarly, you can configure the ExportedOutputTerminal property
 using one of the predefined values, such as:

```text
VB.NET

session.DeviceEvents.DoneEvent.ExportedOutputTerminal = RfsgDoneEventExportedOutputTerminal.Pfi0
```

```text
Visual C#

session.DeviceEvents.DoneEvent.ExportedOutputTerminal = RfsgDoneEventExportedOutputTerminal.Pfi0;
```

You can also create a custom value with the static FromString
 method.

```text
VB.NET

session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.FromString("CustomSource")
```

```text
Visual C#
session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.FromString("CustomSource");
```

You can also directly set the source as a string instead of using the FromString
 method.

```text
VB.NET

session.Triggers.StartTrigger.DigitalEdge.Source = "CustomSource"
```

```text
Visual C#

session.Triggers.StartTrigger.DigitalEdge.Source = "CustomSource";
```

#### How Do I Get the Underlying String from Source or Output Terminal Value?

You can use the implicit conversion operator for conversion from and to string.
 Alternatively, you can also use theToString method. The
 following code shows how to retrieve the source name:

```text
VB.NET

Dim triggerSource As String = RfsgDigitalEdgeStartTriggerSource.Pfi0
```

```text
Visual C#

string triggerSource = RfsgDigitalEdgeStartTriggerSource.Pfi0;
```

You can use the underlying source value if you want to assign a trigger source to the
 same source as an output terminal.

```text
VB.NET

session.Triggers.StartTrigger.DigitalEdge.Source = (string)session.DeviceEvents.DoneEvent.ExportedOutputTerminal
```

```text
Visual C#

session.Triggers.StartTrigger.DigitalEdge.Source = CType(session.DeviceEvents.DoneEvent.ExportedOutputTerminal, String);
```

Parent topic:

Using the .NET Class Library

<!--NI_TOPIC bundle=ni-rfsg path=new-features-and-changes.html language=enus -->
## TOPIC 00038: NI-RFSG New Features and Changes

- bundle_id: `ni-rfsg`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-RFSG. Discover what is new in the latest releases of NI-RFSG.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### NI-RFSG
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-RFSG.

NI-RFSG

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-RFSG 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2026 Q2.

This version of NI-RFSG provides support for the
 following features:

- Support for NI RMM-5544
- Support for 1-channel variant of PXIe-5860
- Support for remote sessions to the NI gRPC Device Server in the Python API

#### NI-RFSG
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2026 Q1.

This version of NI-RFSG provides support for the
 following features:

- Support for List Mode for PXIe-5860 VST with PXIe-5633 VNA.
- Support for deleting a script by script name.
- Save Configuration now supports saving downloaded scripts.

#### NI-RFSG
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2025 Q4.

This version of NI-RFSG provides support for the
 following features:

- Support for PXIe-5842 VST with 54 GHz Frequency Extension (RMM-5586).
- Support for Python API.
- Support for querying script content by script name.
- Improved trigger/event to data alignment for PXIe-5860.

#### NI-RFSG
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2025 Q3.

This version of NI-RFSG provides support for the
 following features:

- Support for SystemLink Asset Utilization.
- Support for PXIe-5842 VST with 54 GHz Frequency Extension (RMM-5585).
- Support for PXIe-5563 RF Port Switch.

#### NI-RFSG
 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2025 Q1.

This version of NI-RFSG provides support for the
 following features:

- Support for 4 GHz Bandwidth variant of PXIe-5842 VST.

#### NI-RFSG
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-RFSG 2024 Q4.

##### Behavior changes

- Uninstalling the RFSG software also removes any previous versions of RFSG .NET runtimes that were leaked in .NET Global Assembly
 Cache directory.

#### NI-RFSA 2024 Q3 New Features and
 Changes

- Support for PXIe-5860 VST
- Support for querying downloaded waveform and script names in PXIe-5830/31/40/41/42
 VST devices
- Support for checking if a waveform or script exists with a given name in
 PXIe-5830/31/40/41/42 VST devices
- Save Configuration now supports saving information about de-embedding S-parameter
 tables loaded from S2P files

#### NI-RFSG 2024 Q2 New Features and
 Changes

- Support for querying Max Settable Power with current configuration

#### NI-RFSG 2024 Q1 New Features and
 Changes

- Support for an enhanced functionality which now allows the utilization of
 DIO or PFIN as triggers and events for
 PXIe-5841 and PXIe-5842

#### NI-RFSG 2023 Q4 New Features and Changes

- Support for PXIe-5842 VST with PXIe-5633 VNA

#### NI-RFSG 2023 Q1 Patch 1 New Features and
 Changes

- Support for PXIe-5842 VST with 54 GHz Frequency Extension

<!--NI_TOPIC bundle=ni-rfsg path=ni-frsa-rd-fundamentals.html language=enus -->
## TOPIC 00039: NI-RFSG RF Fundamentals

- bundle_id: `ni-rfsg`
- source_path: `ni-frsa-rd-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-frsa-rd-fundamentals.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Radio Frequency (RF) communication enables the transmission and reception of information over the air.

### NI-RFSG RF
 Fundamentals

Radio Frequency (RF) communication enables the transmission and reception of information
 over the air.

- [Carrier Wave](carrier-wave.html) The carrier wave is a sinusoidal wave that is modulated by a message signal prior to transmission.
- [Message Signal](message-signal.html) The message signal contains the data for transmission.
- [Modulation](modulation.html) Modulation is a process that alters the characteristics of a carrier wave according to information in the message signal to generate and transmit a modulated wave. There are several different types of modulation.

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-digital-level-trigger.html language=enus -->
## TOPIC 00040: Digital Level

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-digital-level-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-digital-level-trigger.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: A channel performs an operation when a signal goes below a defined low level or above a defined high level. Triggers configured to act in this way are known as level triggers. Only Script triggers may be configured to trigger based on a digital level.

### Digital Level

A channel performs an operation when a signal goes below a
 defined low level or above a defined high level.

Triggers configured to act in this way are known as *level
 triggers*.

Only Script triggers may be configured to trigger based on a digital
 level.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-examples.html language=enus -->
## TOPIC 00041: NI-RFSG Examples

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-examples.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG includes several example applications that demonstrate the functionality of your device and can serve as interactive tools, programming models, and building blocks for your own applications. The NI Example Finder is a utility that organizes examples into categories and allows you to browse a

### NI-RFSG
 Examples

NI-RFSG includes several
 example applications that demonstrate the functionality of your device and can serve as
 interactive tools, programming models, and building blocks for your own
 applications.

The NI Example Finder is a utility that organizes examples into
 categories and allows you to browse and search installed examples. For example, search
 for RFSG to locate all NI RF signal generator examples. You can
 see descriptions and compatible hardware models for each example or see all the examples
 compatible with one particular hardware model.

To locate examples using the NI Example Finder within LabVIEW or
 LabWindows/CVI, select Help»Find Examples and navigate to Hardware Input and Output»Modular Instruments»NI-RFSG.

| Software Application | Installed Example Locations |
| --- | --- |
| LabVIEW | LabVIEW\\examples\\instr\\niRFSG, where LabVIEW is the LabVIEW directory for the specific LabVIEW version you installed on your system. |
| LabWindows/CVI | Program Files\\IVI Foundation\\IVI\\Drivers\\niRFSG\\Examples\\CVI |

| NI-RFSG Example | Description |
| --- | --- |
| RFSG Arbitrary Waveform Generation | This example demonstrates how to generate one of three arbitrary waveforms, including a double side band, lower side band, or upper side band waveform. |
| RFSG Arbitrary Waveform Streaming | This example demonstrates how to read chirp signal data in chunks from a file and then use streaming capabilities to generate chirp signal data. |
| RFSG Write Waveform From File | This example demonstrates how to read chirp signal data in chunks from a file and then generate data using the arbitrary waveform capabilities of NI-RFSG. |
| RFSG Getting Started Single Tone Generation | This example demonstrates how to generate a sine wave at a specified frequency and power. |
| RFSG 5673 Synchronization (TClk, Shared LO) | This example demonstrates how to synchronize multiple PXIe-5673 devices that share a local oscillator (LO) using NI-TClk. |

Related concepts:

- Creating an Application with NI-RFSG
- Streaming Waveform Data in NI-RFSG

Related tasks:

- Using NI-RFSG in LabVIEW
- Using NI-RFSG in LabWindows/CVI

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-instrument-driver-fpga-extensions.html language=enus -->
## TOPIC 00042: NI-RFSG Instrument Driver FPGA Extensions

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-instrument-driver-fpga-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-instrument-driver-fpga-extensions.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG instrument driver FPGA extensions for VSTs enable you to use precompiled FPGA bitfiles to customize the behavior of the VST FPGA. At the same time, the FPGA extensions maintain the functionality of the NI-RFSG instrument drivers. Before you begin using NI-RFSG instrument driver FPGA extensio

### NI-RFSG
 Instrument Driver FPGA Extensions

NI-RFSG instrument driver FPGA extensions for VSTs enable
 you to use precompiled FPGA bitfiles to customize the behavior of the VST FPGA. At the same
 time, the FPGA extensions maintain the functionality of the NI-RFSG instrument
 drivers.

NI-RFSG

NI-RFSG

NI-RFSG

NI-RFSG

1. Visit ni.com/info and enter the Info Code
 ex6h8h .
2. Select your hardware, and browse the download page for the NI-RFSG FPGA extensions precompiled FPGA
 bitfile.

Note

NI-RFSG

NI-RFSG

- A precompiled bitfile that features application-specific IP
- A host-based example that uses NI-RFSA , NI-RFSG , or both
- IP dependencies, such as source code

When you install NI-RFSG,
 model-specific folders for your VST device are created in the following
 location:

- Windows 10/8.1/7: 
 Users\Public\Documents\National Instruments\FPGA Extensions
 Bitfiles

Note

FPGABitfile

#### Loading an FPGA Bitfile

To
 use NI-RFSG instrument driver FPGA extensions, you
 must specify the precompiled bitfile you want to use when you initialize the
 instrument driver session. If you want to access additional FPGA functionality
 provided by the precompiled bitfile, you must also obtain an FPGA reference. The
 FPGA reference is used with the LabVIEW FPGA host interface.

Note

NI-RFSG

NI-RFSA

Complete the following steps to open an instrument driver
 session that uses a precompiled bitfile:

1. Call the niRFSG Initialize with Options VI.
2. Wire the DriverSetup string to the options
 string input.
3. Include the Bitfile tag in the DriverSetup 
 string, and set the value of the Bitfile tag to the name of the
 bitfile you want to load, as shown in the following example
 string: DriverSetup=Bitfile:filename.lvbitx where
 filename.lvbitx is the file
 name of the bitfile you want to load.

#### Obtaining an FPGA
 Reference

Complete the following steps to obtain an FPGA reference to use
 with the LabVIEW FPGA host interface:

1. Call the niRFSG FPGA Bitfile Path property. The FPGA
 Bitfile Path property returns the absolute path to the bitfile as a
 string.
2. Wire the output of the FPGA Bitfile Path property to the
 String input of the String to Path 
 function.
3. Wire the Path output of the String to
 Path function to the Bitfile Path input of
 the Open Dynamic Bitfile Reference function.

Visit ni.com/info and enter the Info Code exkt9h to
 learn more about instrument driver FPGA extensions.

Parent topic:

Programming Considerations

Related concepts:

- NI-RFSG Driver Setup Options

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-instrument-driver-programming-flow.html language=enus -->
## TOPIC 00043: NI-RFSG Instrument Driver Programming Flow

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-instrument-driver-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-instrument-driver-programming-flow.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG VIs are located on the LabVIEW Functions palette at Measurement I/O NI-RFSG . The top-level NI-RFSG Functions palette is shown, and the core VIs are highlighted in the following figure: Every application using NI-RFSG must call the five VIs highlighted on the preceding palette image. These V

### NI-RFSG
 Instrument Driver Programming Flow

NI-RFSG VIs are located on the LabVIEW Functions palette at Measurement I/O»NI-RFSG. The top-level NI-RFSG Functions palette is
 shown, and the core VIs are highlighted in the following figure:

[IMAGE alt='image' src='GUID-CAF92AC7-A921-43E2-9D54-083448996761-a5.gif']

Every application using NI-RFSG must call the five VIs highlighted on the preceding palette
 image. These VIs are arranged from left to right in the order they must be called:

1. niRFSG
 Initialize —Opens a session to the NI-RFSG device and initializes both the AWG and the upconverter hardware.
2. niRFSG
 Configure RF —Configures the frequency and power level of the RF output
 signal.
3. niRFSG
 Initiate —Initiates signal generation.
4. niRFSG
 Check Generation Status —Monitors signal generation status and checks
 for any errors which may occur during signal generation.
5. niRFSG
 Close —Closes the NI-RFSG session and
 deallocates memory resources used by NI-RFSG . You must call
 this VI once for every session opened with niRFSG Initialize .

Parent topic:

Programming Considerations

Related tasks:

- Creating an Application with Microsoft Visual C++ 6.0
- Creating an Application with Microsoft Visual Studio 2010

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-ni-rfsa-digital-edge.html language=enus -->
## TOPIC 00044: Digital Edge

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-ni-rfsa-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-ni-rfsa-digital-edge.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital edge trigger acts on the rising or falling edge of a digital signal. A digital signal has two discrete levels: a high level and a low level. When the signal transitions from high to low or from low to high, a digital edge is created. There are two types of edges: Rising Occurs when the sig

### Digital Edge

A *digital edge trigger* acts on the rising or falling edge of a digital
 signal.

digital
 edge

Rising

Falling

Triggers acting on a rising or a falling edge of a digital signal are *edge
 triggers*. Digital triggering is possible on the RTSI lines, PFI lines, and
 the PXI Star Trigger line.

As the figure shows, an edge trigger can be configured to occur either
 at the place labeled Falling Edge of Signal or Rising Edge of Signal.

Figure 4.

[IMAGE alt='image' src='GUID-1C1BDC5B-E1AC-469F-A80B-60BDD009BD13-a5.svg']

You can configure each named trigger to operate based on a digital
 edge.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-none.html language=enus -->
## TOPIC 00045: None

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-none.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal generation starts immediately upon execution of the NI-RFSG Initiate function; no Start or Script trigger is necessary to begin generation. This configuration is the default behavior for instruments programmed with NI-RFSG.

### None

Signal generation starts immediately upon execution of the
 NI-RFSG
 Initiate function; no Start or Script trigger is necessary to begin
 generation.

This configuration is the default behavior for instruments programmed
 with NI-RFSG.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-programming-state-model.html language=enus -->
## TOPIC 00046: NI-RFSG Programming State Model

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-programming-state-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-programming-state-model.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSG programming model has three main states: Configuration (idle), Committed, and Generation (running). 9 NI-RFSG Programming State Model for the PXI-5670/5671 and PXIe-5672 The diagram depicts the programming state model for the PXI-5670/5671 and PXIe-5672 Vector Signal Generator and NI-RFS

### NI-RFSG
 Programming State Model

The NI-RFSG programming model
 has three main states: *Configuration* (idle), *Committed*, and
 *Generation* (running).

Figure 9.

PXI-5670/5671

[IMAGE alt='The diagram depicts the programming state model for the PXI-5670/5671 and PXIe-5672 Vector Signal Generator and NI-RFSG software.' src='GUID-88B9A051-F27A-463D-AC7C-C4AC3BC2B19A-a5.svg']

Figure 10.

PXIe-5673/5673E

[IMAGE alt='The diagram depicts the programming state model for the PXIe-5673/5673E Vector Signal Generator and NI-RFSG software.' src='GUID-6A1180ED-23AE-41E4-BF46-D5E1E190586A-a5.svg']

Configuration

NI-RFSG

Note

NI-RFSG

Committed

NI-RFSG Commit

- Verifies all property or attribute settings
- Validates the specified configuration
- Writes all settings to the hardware modules
- Writes the waveform to the AWG module onboard memory
- Transitions to the Committed state

If you change any properties or attributes while in the Committed
 state, the session implicitly transitions back to the Configuration
 state. The hardware configuration reflects the previously committed
 properties or attributes.

Note

PXIe-5673/5673E

Generation

Note

PXI-5670/5671

PXIe-5672

PXI/PXIe-5650/5651/5652

PXIe-5673/5673E

Note

NI-RFSG
 Close

NI-RFSG Close

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-script-trigger.html language=enus -->
## TOPIC 00047: NI-RFSG Script Trigger Details

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-script-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-script-trigger.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Script trigger is a general-purpose trigger with a role determined entirely by the context of the dynamic generation script. A script allows you to create sophisticated dynamic generation operations. For example, the script can configure the instrument to generate waveform A, then wait for a Scrip

### NI-RFSG Script
 Trigger Details

A Script trigger is a general-purpose trigger with a role
 determined entirely by the context of the dynamic generation script.

A script allows you to create sophisticated dynamic generation operations. For example, the
 script can configure the instrument to generate waveform A, then wait for a Script trigger,
 then generate waveform B. You can configure up to four Script triggers for use in your
 application.

Figure 3.

NI-RFSG

[IMAGE alt='image' src='GUID-9ED86C90-8124-4C26-B8CF-52C677D7E114-a5.svg']

Note

Configure the Script trigger using the Script Trigger Type property. The
 Configure Trigger function also provides access to this property.

Tip

Script Trigger Type

Digital Edge

Parent topic:

NI-RFSG Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-sfp-environment.html language=enus -->
## TOPIC 00048: NI-RFSG SFP Environment

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-sfp-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-sfp-environment.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Similar to stand-alone RF signal generators, the NI-RFSG SFP controls your RF device, which generates data. However, because the SFP operates on the PC, it provides additional processing, storage, and display capabilities. You can open multiple instances of the SFP to interact with more than one dev

### NI-RFSG SFP
 Environment

Similar to stand-alone RF signal generators, the NI-RFSG
 SFP controls your RF device, which generates data. However, because the SFP operates on
 the PC, it provides additional processing, storage, and display capabilities. You can
 open multiple instances of the SFP to interact with more than one device. Each instance
 of the SFP opens as a separate application window and interacts with one device.

You can access the NI-RFSG SFP at Start»National Instruments»NI-RFSG»NI-RFSG Soft Front Panel. The SFP launches at the minimum application window size. To resize the
 application window, click the Maximize button in the upper right
 corner of the window or click and drag a corner of the window.

The following figure illustrates the elements of the NI-RFSG SFP environment.

[IMAGE alt='image' src='GUID-4337FA46-18F5-41FF-AFD2-32F222F6B614-a5.gif']

1. Menu —Use the NI-RFSG SFP
 menus to perform the following actions:
  - Use the File menu options to open new instances
 of the NI-RFSG SFP, set up and print the
 Display Window, save and load configuration files, and exit the
 SFP.
  - Use the Device menu to open and close a device
 session.
  - Use the Help menu to access information about the
 SFP, help for the SFP, and device-specific help.
2. Display Window —The upper pane of the Display Window shows
 information about the RF device in session. The upper pane includes a data entry
 field that appears when you click instrument control buttons for which you can
 specify instrument settings. Note Some parameter values are coerced to a value
 supported by the current device. Actual (coerced) values display in the
 Device Configuration Area, while the data entry
 field and softkey continue to display the desired value.
3. Device Configuration Area —The middle pane of the
 Display Window shows the configuration settings of
 the current device session and parameters of the current generation. In Arb
 mode, the lower pane can display a graphical preview of the data.
4. Instrument Control Buttons —Use the instrument control
 buttons to select softkey menus where you can configure signals and specify
 device, system, and display options. You can also use instrument control buttons
 to save and recall configurations for signal generation and to print the current
 Display Window . Use the instrument control buttons as
 you would the buttons on stand-alone RF signal generators.
5. Softkey Menu —Use the softkey menu to configure a
 generation and specify device, system, and display settings. The softkey menu is
 dynamic and changes according to the selected instrument control button.The
 >> symbol on a softkey indicates additional
 options are available by clicking that softkey. Click the
 Return softkey to return to the previous softkey
 menu. Use the < and > 
 softkeys below the Return softkey to view additional
 softkeys related to the current softkey menu.
6. Keypad and Knob —Use the keypad and knob to enter values
 for device settings as you would on stand-alone RF signal generators. You can
 also use your computer keyboard to enter values for device settings, and you can
 use the mouse scroll wheel to move the knob.
7. Status Bar —The status bar displays status, warning, and
 error information about the current device session. Click the
 Clear button to clear warnings from the status bar.
 The SFP automatically clears resolved errors from the status bar.

Parent topic:

NI-RFSG Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-soft-front-panel-help.html language=enus -->
## TOPIC 00049: NI-RFSG Soft Front Panel

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-soft-front-panel-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-soft-front-panel-help.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-RFSG Soft Front Panel (SFP) to interactively control your NI RF signal generator. The NI-RFSG SFP uses the NI-RFSG driver software for LabVIEW to perform standard, built-in RF signal generator operations. This documentation includes information about the SFP environment and details about

### NI-RFSG Soft Front Panel

Use the NI-RFSG Soft Front Panel (SFP) to interactively control your NI RF signal
 generator.

The NI-RFSG SFP uses the NI-RFSG driver software for LabVIEW to perform standard, built-in RF signal
 generator operations. This documentation includes information about the SFP environment
 and details about how to generate a CW tone, import data, and model I/Q impairments. For
 information about developing applications outside the SFP using the NI-RFSG driver software, refer to the programming
 reference.

Tip

To learn more about using the NI-RFSG SFP, by launch the SFP
 and select Help»Show Context Help or press Ctrl+H. In the
 context help window, move the cursor over an item to display additional help.

- [NI-RFSG SFP Environment](ni-rfsg-sfp-environment.html)
- [Generating a CW Tone in the NI-RFSG SFP](generating-a-cw-tone-in-the-ni-rfsg-sfp.html)
- [Importing Data to the NI-RFSG SFP for Generation](importing-data-to-the-ni-rfsg-sfp-for-generat.html)
- [Modeling I/Q Impairments in the NI-RFSG SFP](modeling-iq-impairments-in-the-ni-rfsg-sfp.html) You can use the NI-RFSG SFP to model I/Q impairments on imported signals. You can model I/Q impairments on only the NI 5673/5673E vector signal generator.
- [Supported Data File Formats in the NI-RFSG SFP](supported-data-file-formats-sfp.html) You can use the NI-RFSG SFP to import data from a file for generation. The SFP supports text and TDMS waveform file formats.
- [Saving a Configuration](saving-a-configuration.html) The NI-RFSG Soft Front Panel allows you to save all the current settings, and to later recall them to restore the Soft Front Panel to a predefined state. The NI-RFSG SFP uses the TDMS file type for this purpose.

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-software.html language=enus -->
## TOPIC 00050: Software Edge

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-software.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: After initiation, a software trigger is generated internally by a programmatic call using NI-RFSG and can occur at any time, based upon the conditions specified in the program. You can configure Start and Script triggers in NI-RFSG to operate based on a software edge. Use NI-RFSG Send Software Edge

### Software Edge

After initiation, a software trigger is generated
 internally by a programmatic call using NI-RFSG and can occur
 at any time, based upon the conditions specified in the program.

You can configure Start and Script triggers in NI-RFSG to operate based on a software edge.

Use NI-RFSG
 Send Software Edge Trigger and set the trigger
 type input to the type of trigger you want to send.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-start-trigger.html language=enus -->
## TOPIC 00051: NI-RFSG Start Trigger Details

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-start-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-start-trigger.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: For waveform generators and VSTs, a Start trigger initiates signal generation. When the instrument receives a Start trigger, the RF output signal begins to generate as shown in the following figure. The instrument ignores a Start trigger received after signal generation has started. 1 NI-RFSG Start

### NI-RFSG Start
 Trigger Details

For waveform generators and VSTs, a Start trigger initiates signal
 generation.

When the instrument receives a Start trigger, the RF output signal begins to generate as
 shown in the following figure. The instrument ignores a Start trigger received after
 signal generation has started.

Figure 1.

NI-RFSG

[IMAGE alt='image' src='GUID-258B5DF8-CED9-4446-9268-C59A78C27972-a5.svg']

Note

Configure the Start trigger using the Start Trigger
 Type property. The Configure Trigger function also
 provides access to this property.

Tip

Start Trigger Type

Digital Edge

The possible sources for a Start trigger are as follows.

Figure 2.

NI-RFSG

[IMAGE alt='image' src='GUID-AF485F1E-290A-443D-8199-C6D708CC6414-a5.svg']

Parent topic:

NI-RFSG Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-supported-events.html language=enus -->
## TOPIC 00052: NI-RFSG Event Types

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-supported-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-supported-events.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG includes specific events you can use in tandem with triggers to coordinate actions across instruments. Marker Occurs at the time that a specific location or sample n in the waveform generates on the output connector. If the waveform loops multiple times in a segment, the marker generates eac

### NI-RFSG Event
 Types

NI-RFSG includes specific
 events you can use in tandem with triggers to coordinate actions across
 instruments.

Marker

n

Started

Done

Configuration Settled

settled

Frequency Settling

Frequency Settling
 Units

<!--NI_TOPIC bundle=ni-rfsg path=ni-rfsg-triggers.html language=enus -->
## TOPIC 00053: NI-RFSG Named Trigger Types

- bundle_id: `ni-rfsg`
- source_path: `ni-rfsg-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/ni-rfsg-triggers.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Named trigger types in NI-RFSG define the action you want an instrument or instrument channel to take upon detecting a specific signal condition. Trigger stimuli include digital edges, software functions, and analog levels. The trigger can be derived from attributes of the signal to be acquired, suc

### NI-RFSG Named
 Trigger Types

Named trigger types in NI-RFSG define the action you want an instrument or instrument channel to take
 upon detecting a specific signal condition.

Trigger stimuli include digital edges, software functions, and analog
 levels. The trigger can be derived from attributes of the signal to be acquired, such as
 the level and slope of the signal.

The following named trigger types are available in NI-RFSG:

Start

Supported signal conditions:
 None, Digital Edge, Software

Script

Supported signal conditions: None, Digital Edge, Digital
 Level, Software

Configuration List Step

Supported signal conditions: None, Digital Edge

<!--NI_TOPIC bundle=ni-rfsg path=noise-figure.html language=enus -->
## TOPIC 00054: Noise Figure

- bundle_id: `ni-rfsg`
- source_path: `noise-figure.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/noise-figure.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: All devices have inherent noise. When noise is quantified, all noise power that a UUT inherits is assumed to come from its input. The noise figure (NF) of a UUT is the ratio, in decibels (dB), of its noise power to the noise power that a matched resistive load would deliver at room temperature. If y

### Noise Figure

All devices have inherent noise. When noise is quantified,
 all noise power that a UUT inherits is assumed to come from its input. The noise
 figure (NF) of a UUT is the ratio, in decibels (dB), of its noise power to the noise
 power that a matched resistive load would deliver at room temperature. If you
 terminate a UUT input with a matched resistive load (typically 50 Ω) and measure the noise power density at its
 output (*N*<sub>o</sub>), the noise figure (*NF*) is given by
 the following equation:

NF

=

10

log

⁡

(

N

o

/

G

k

T

)

where

- G is the power gain (in linear units) of the UUT
- k is Boltzmann’s constant (1.38 ×10 -23 J/K)
- T is the room temperature (≈ 290° K)

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=noise-floor.html language=enus -->
## TOPIC 00055: Noise Floor

- bundle_id: `ni-rfsg`
- source_path: `noise-floor.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/noise-floor.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise floor is the noise level below which signals cannot be detected under the same measurement conditions. Noise floor is the measure of the noise density (dBm/Hz), or the noise power, in a signal of 1 Hz bandwidth. Noise can be classified into several types, including the following: Shot noise Th

### Noise Floor

Noise floor is the noise level below
 which signals cannot be detected under the same measurement conditions.

Noise floor is the measure of the noise density (dBm/Hz), or the noise
 power, in a signal of 1 Hz bandwidth. Noise can be
 classified into several types, including the following:

- Shot noise
- Thermal noise
- Flicker noise
- Burst noise
- Quantization noise
- Avalanche noise

For example, in an audio system, the broadband noise level may be 5 µV. This means that broadband signal levels cannot be
 detected below this level. If the noise is broadband random noise rather than consisting
 of sinusoidal components, it behaves differently. In that case, you can use a narrow
 band filter to investigate it further.

Noise floor is normally specified as one or more of the following
 characteristics:

- Broadband noise (referenced to full scale deflection)
- Spurious free dynamic range
- Noise power density (used to specify broadband random
 noise)

Parent topic:

Understanding RF Specifications

Related information:

- Dynamic Range

<!--NI_TOPIC bundle=ni-rfsg path=open-loop-and-closed-loop-use-cases.html language=enus -->
## TOPIC 00056: Open-Loop and Closed-Loop Use Cases

- bundle_id: `ni-rfsg`
- source_path: `open-loop-and-closed-loop-use-cases.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/open-loop-and-closed-loop-use-cases.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specifing the source for the configuration trigger allows you to use RF list mode with open-loop and closed-loop use cases. Open-Loop Use Case The RF device advances through the RF configuration list based on a user-defined time-specification for each step. In one configuration option, you can speci

### Open-Loop and Closed-Loop Use Cases

Specifing the source for the configuration trigger allows you to use RF list mode
 with open-loop and closed-loop use cases.

Open-Loop Use Case

Closed-Loop Use Case

- The RF device is able to receive triggers to advance through the
 frequency list.
- The RF device is able to produce events as it moves to each step in the
 RF configuration list.

Parent topic:

RF List Mode

Related concepts:

- Signal Routing in NI-RFSG

Related tasks:

- Using RF List Mode

<!--NI_TOPIC bundle=ni-rfsg path=output-attenuation.html language=enus -->
## TOPIC 00057: Output Attenuation

- bundle_id: `ni-rfsg`
- source_path: `output-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/output-attenuation.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Output attenuation is a method of controlling the output voltage level of the signal being generated. RF signal generators typically generate signals with a digital–to–analog converter (DAC) that has an output voltage range of –5.0 V to +5.0 V with a number of bits of resolution.This signal is appli

### Output Attenuation

Output attenuation is a method of controlling the output
 voltage level of the signal being generated.

RF signal generators typically generate signals with a digital–to–analog converter (DAC)
 that has an output voltage range of –5.0 V to +5.0 V with a number of bits of resolution.This signal is
 applied to an attenuator that controls the output voltage of the RF signal source.

By attenuating the DAC output signal, you keep the dynamic range of the DAC; that is, you
 do not lose any bits from the digital representation of the signal because the
 attenuation is done after the DAC and not before it.

For example, if a DAC with a range of –5.0 V to +5.0 V and aresolution of 12 bits with each bit
 corresponding to 2.44 mV [ ( +5.0 – (–5.0) ) /
 2<sup>12</sup> ] does not use output attenuation, and the desired signal is 2.0 V<sub>pk-pk</sub> (–1.0 V to +1.0 V), waveform values can be
 generated with the DAC that only use one fifth of the DAC range. The resolution of each
 digital bit is still 2.44 mV.

However, if the same DAC uses the output attenuation, the full range of the DAC generates
 the signal, creating the signal at the full 10.0 V<sub>pk-pk</sub>. The value of each digital bit is still the
 original 2.44 mV. The signal is applied to an attenuator,
 which reduces the voltage level by a factor of 5 V<sub>pk-pk</sub> to 2.0 V<sub>pk-pk</sub>. The attenuator also reduces the value of each bit,
 which results in an effective bit value of 0.488 mV at
 the analog output connector. The attenuator allows the use of the full range of the DAC,
 and reduces the effective value of each bit corresponding to the degree of
 attenuation.

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=output-impedance.html language=enus -->
## TOPIC 00058: Output Impedance

- bundle_id: `ni-rfsg`
- source_path: `output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/output-impedance.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: RF signal generators have an output impedance of 50 Ω. If the load impedance matches the output impedance, the voltage at the signal output connector is at the needed level. In the preceding figure, the required output voltage is ±5 V. The relationship between the output voltage and the load can be

### Output Impedance

RF signal generators have an output impedance of 50 Ω.

If the load impedance matches the output impedance, the voltage at the signal output
 connector is at the needed level.

[IMAGE alt='image' src='GUID-5E795CE0-40BB-4F7F-BFA9-2D7EF58A46BE-a5.gif']

In the preceding figure, the required output voltage is ±5 V. The relationship between the output voltage and the load can be
 calculated as follows:

V

o

u

t

=

[

R

L

(

R

L

+

R

O

)

]

×

[

V

S

]

where

- V out = the voltage level delivered to
 R L
- R L = the load impedance in ohms
- R O = the output impedance on the NI RF signal
 generator
- V S = the voltage level generated by the source previous to
 R O

By default, *R*<sub>O</sub> = 50 Ω.

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=overview.html language=enus -->
## TOPIC 00059: NI-RFSG Overview

- bundle_id: `ni-rfsg`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/overview.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG is a driver software you use to control and configure NI PXI RF analog signal generators, NI PXI vector signal generators, and the RF outputs on NI PXI vector signal transceivers (VST). NI-RFSG provides the standard IVI-based functionality needed for most RF signal generator applications. Us

### NI-RFSG
 Overview

NI-RFSG is a driver software you use to control and
 configure NI PXI RF analog signal generators, NI PXI vector signal generators, and the RF
 outputs on NI PXI vector signal transceivers (VST). NI-RFSG
 provides the standard IVI-based functionality needed for most RF signal generator
 applications. Use NI-RFSG to perform waveform programming
 and generation. Perform basic modulation tasks using the NI-RFSG API.

<!--NI_TOPIC bundle=ni-rfsg path=phase-noise.html language=enus -->
## TOPIC 00060: Phase Noise

- bundle_id: `ni-rfsg`
- source_path: `phase-noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/phase-noise.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Phase noise refers to noise in a carrier signal due to phase and frequency modulation in the signal. Phase noise is normally very close to the carrier and is measured in decibels relative to the carrier frequency (dBc). Phase noise is expressed as a function of power spectral density and frequency.

### Phase Noise

Phase noise refers to noise in a
 carrier signal due to phase and frequency modulation in the signal.

Phase noise is normally very close to the carrier and is measured in decibels relative to
 the carrier frequency (dBc).

Phase noise is expressed as a function of power spectral density and frequency. In a 1 Hz bandwidth, phase noise is given by the following
 formula:

ℒ

(

f

)

=

10

log

⁡

[

0.5

(

S

⁢

φ

(

f

)

)

]

φ

where

- S
 ⁢
 
 φ
 (
 f
 ) is the spectral density of phase fluctuations

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=programming.html language=enus -->
## TOPIC 00061: Programming Considerations

- bundle_id: `ni-rfsg`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/programming.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-RFSG API and its supported ADEs to program NI RF signal generators.

### Programming Considerations

Use the NI-RFSG API and its supported ADEs to program NI RF signal
 generators.

- [NI-RFSG Instrument Driver Programming Flow](ni-rfsg-instrument-driver-programming-flow.html)
- [NI-RFSG Programming State Model](ni-rfsg-programming-state-model.html) The NI-RFSG programming model has three main states: Configuration (idle), Committed , and Generation (running).
- [NI-RFSG Driver Setup Options](driver-setup-options.html) The Driver Setup string allows you to configure hardware devices, simulate devices, and specify FPGA extensions for NI-RFSG instruments. Use the format " *Tag*:*Value* " to define your setup, and separate multiple devices with a semicolon.
- [Simulating a Device Using NI-RFSG](simulating-a-device.html) Simulate your device using NI-RFSG to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Simulating a device also allows you to evaluate an NI product even if you don't have the hardware.
- [Set Properties Before Reading Them](setting-properties-and-attributes-before-read.html) You can modify properties when you set them or when you call a configuration function that sets them.
- [Assigning Properties to a Waveform in NI-RFSG](assigning-properties-or-attributes-to-a-wavef.html) NI-RFSG can store the I/Q Rate, Peak Power Adjustment, and Arb Carrier Frequency for a waveform. When switching between waveforms, the associated waveform properties also change. You can assign waveform properties in Arb Waveform Generation mode or Script Generation mode . Use Configure Generation Mode to select between the two modes.
- [NI-RFSG Instrument Driver FPGA Extensions](ni-rfsg-instrument-driver-fpga-extensions.html) NI-RFSG instrument driver FPGA extensions for VSTs enable you to use precompiled FPGA bitfiles to customize the behavior of the VST FPGA. At the same time, the FPGA extensions maintain the functionality of the NI-RFSG instrument drivers.
- [RF List Mode](rf-list-mode.html) RF list mode is an operating mode in which the device deterministically sequences through a predetermined set of RF configurations.
- [Scripting Instructions](scripting-instructions.html)
- [Using the .NET Class Library](using-net-class-library.html) You can use the .NET class library to initialize, configure, initiate, generate, and close a session on your device. The .NET API is an IVI-compliant instrument driver that features a set of methods and properties that exercise the functionality of the hardware.

<!--NI_TOPIC bundle=ni-rfsg path=removing-ni-rfsg-instrument.html language=enus -->
## TOPIC 00062: Removing an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `removing-ni-rfsg-instrument.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/removing-ni-rfsg-instrument.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To remove your NI-RFSG device in MAX, complete the following steps: Right-click the device name in the configuration tree. Select Delete. You can only delete simulated devices or physical devices that are no longer present in the system.

### Removing an NI-RFSG Device

To remove your NI-RFSG device in MAX, complete the following
 steps:

1. Right-click the device name in the configuration tree.
2. Select Delete. 
 Note You can only delete simulated devices or physical
 devices that are no longer present in the system.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=renaming-an-ni-rfsg-device.html language=enus -->
## TOPIC 00063: Renaming an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `renaming-an-ni-rfsg-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/renaming-an-ni-rfsg-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: MAX allows you to rename each of your NI-RFSG devices. NI-RFSG uses the MAX name to operate the hardware resources. You are not required to change the device names from the default, but doing so can make programming easier. To rename your NI-RFSG device in MAX, complete the following steps: Select t

### Renaming an NI-RFSG Device

MAX allows you to rename each of your NI-RFSG devices. NI-RFSG uses
 the MAX name to operate the hardware resources.

NI-RFSG

1. Select the device name in the configuration tree.
2. Within the Settings section, enter a new name for your
 NI-RFSG device in the Name textbox.
3. Click Save in the MAX toolbar.
4. Verify that MAX displays the new names for all of your devices.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

Related tasks:

- Locating an NI-RFSG Device
- Associating NI-RFSG Modules

<!--NI_TOPIC bundle=ni-rfsg path=repeatend-repeat.html language=enus -->
## TOPIC 00064: repeat/end repeat

- bundle_id: `ni-rfsg`
- source_path: `repeatend-repeat.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/repeatend-repeat.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the repeat/end repeat instruction to describe how to "loop" sections of a script until a particular condition is met. Usage:Execute a set of instructions n times:repeat n instructions end RepeatExecute a set of instructions until the device receives a Script trigger:Repeat until scriptTrigger0 i

### repeat/end
 repeat

Use the repeat/end repeat instruction to
 describe how to "loop" sections of a script until a particular condition is met.

Usage:

- Execute a set of instructions n 
 times: repeat n
 instructions
end Repeat
- Execute a set of instructions until the device receives a Script
 trigger: Repeat until scriptTrigger0
 instructions
end Repeat When
 the device receives the Script trigger, all instructions remaining in the repeat
 until loop are completed before advancing, so receipt of the Script trigger
 does not break out of the repeat loop immediately.
- Execute a set of instructions until the generation operation is aborted (using the
 Abort VI/function for your
 driver) repeat forever
 instructions
end repeat
- Nest repeat N or repeat until instructions inside a
 repeat forever 
 instruction: repeat forever
 instructions
 repeat N
 instructions
 end repeat
 instructions
end repeat repeat forever
 instructions
 repeat until scripttrigger0
 instructions
 end repeat
 instructions
end repeat Note You
 can nest repeat N and repeat until
 instructions, one level deep, inside a repeat forever instruction. The
 if/else/end if instruction is allowed inside a repeat
 forever instruction, but if/else/end if is not allowed
 inside of repeat N and repeat until
 instructions. Other nesting (for example, repeat N
 inside another repeat N) is not allowed.

#### repeat/end repeat Examples

- Generate myWfmA followed by myWfmB five
 times: repeat 5
 generate myWfmA
 generate myWfmB
end repeat
- Generate the sequence myWfmA , myWfmB ,
 myWfmC until a Script trigger is
 received: Repeat until scripttrigger0
 generate myWfmA
 generate myWfmB
 generate myWfmC
end repeat
- Generate myWfmA forever (until the operation is
 aborted): repeat forever
 generate myWfmA
end repeat
- Generate continuously the sequence initialWfm once;
 myWfmA , myWfmB , myWfmC 1000 times;
 myWfmD 
 once: repeat forever
 generate initialWfm
 repeat 1000
 generate myWfmA
 generate myWfmB
 generate myWfmC
 end repeat
 generate myWfmD end repeat
- Switch between two waveforms upon receipt of a Script trigger (until the operation is
 aborted): repeat forever
 repeat until scripttrigger0
 generate myWfmA
 end repeat
 repeat until scripttrigger0
 generate myWfmB
 end repeat
end repeat

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=resetting-an-ni-rfsg-device.html language=enus -->
## TOPIC 00065: Resetting an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `resetting-an-ni-rfsg-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/resetting-an-ni-rfsg-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To reset your NI-RFSG device in MAX, complete the following steps: Select the device name in the configuration tree. Click Reset in the MAX toolbar. A message appears indicating the result of the device reset.

### Resetting an NI-RFSG Device

NI-RFSG

1. Select the device name in the configuration tree.
2. Click Reset in the MAX toolbar. 
 A message appears indicating the result of the device reset.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=rf-list-mode.html language=enus -->
## TOPIC 00066: RF List Mode

- bundle_id: `ni-rfsg`
- source_path: `rf-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/rf-list-mode.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: RF list mode is an operating mode in which the device deterministically sequences through a predetermined set of RF configurations. A given set of RF configurations, as specified by an RF configuration list, is enacted by the RF modules themselves, without any interaction with the host system and NI

### RF List Mode

RF list mode is an operating mode in which the device
 deterministically sequences through a predetermined set of RF configurations.

A given set of RF configurations, as specified by an RF configuration
 list, is enacted by the RF modules themselves, without any interaction with the host
 system and NI-RFSG. Because NI-RFSG is not involved in executing the RF configuration list changes, the
 changes from one step in the list to the next are deterministic.

- PXIe-5644/5645/5646
- PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5830/5831/5832/5840/5841

Note

- [Using RF List Mode](using-rf-list-mode.html) An RF configuration list consists of configuration list steps. Each step specifies the state of the instrument by specifying values for properties or attributes.
- [Open-Loop and Closed-Loop Use Cases](open-loop-and-closed-loop-use-cases.html) Specifing the source for the configuration trigger allows you to use RF list mode with open-loop and closed-loop use cases.

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsg path=running-a-self-test-on-an-ni-rfsg-device.html language=enus -->
## TOPIC 00067: Running a Self-Test on an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `running-a-self-test-on-an-ni-rfsg-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/running-a-self-test-on-an-ni-rfsg-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: The MAX self-test performs a basic verification of hardware resources. You can only perform a self-test on the individual associated modules within the hardware system. To run a self-test on your NI-RFSG device in MAX, complete the following steps: Select the device name in the configuration tree. C

### Running a Self-Test on an NI-RFSG Device

The MAX self-test performs a basic verification of hardware
 resources.

Note

To run a self-test on your NI-RFSG device in MAX, complete the following
 steps:

1. Select the device name in the configuration tree.
2. Click Self-Test in the MAX toolbar. 
 Note For the PXIe-3621/3622/3623,
 you can perform a basic or intermediate self-test. Use a basic self-test to verify
 communication with the device. Use an intermediate self-test to verify analog cable
 connections and locate failures on the device and associated devices. 
 A message appears indicating the self-test result.
3. Close the dialog box to continue.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=sample-rate.html language=enus -->
## TOPIC 00068: Sample Rate

- bundle_id: `ni-rfsg`
- source_path: `sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/sample-rate.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which digital data is transferred from the memory to the digital-to-analog converter (DAC). According to Shannon’s Sampling theorem, a digital waveform must be updated at least twice as fast as the bandwidth of the signal to be accurately generated. Ideally, a sample rate

### Sample Rate

Sample rate is the rate at which
 digital data is transferred from the memory to the digital-to-analog converter
 (DAC).

According to Shannon’s Sampling theorem, a digital waveform must be
 updated at least twice as fast as the bandwidth of the signal to be accurately
 generated. Ideally, a sample rate many times greater than the frequency of the signal
 produces accurate waveforms. A higher sample rate also captures more waveform details.
 The following figure illustrates a 1 MHz sine wave
 generated by a sampled 2 MS/s DAC and a 20 MS/s DAC. The faster DAC generates 20 points per cycle
 of the expected signal compared with 2 points per cycle with the slower DAC. In this
 example, the higher sample rate more accurately defines the waveform shape.

[IMAGE alt='image' src='GUID-D202B4FE-7A61-4654-8DF8-99C200DD4DC0-a5.svg']

Related concepts:

- Nyquist and Shannon's Sampling Theorems

<!--NI_TOPIC bundle=ni-rfsg path=sampling-nyquist-shannon.html language=enus -->
## TOPIC 00069: Nyquist and Shannon's Sampling Theorems

- bundle_id: `ni-rfsg`
- source_path: `sampling-nyquist-shannon.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/sampling-nyquist-shannon.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem concerns digital sampling of a continuous time analog waveform, while Shannon’s Sampling theorem concerns the creation of a continuous time analog waveform from digital, discrete samples. Nyquist Theorem The Nyquist theorem states that an analog signal must be sampled at least tw

### Nyquist and Shannon's Sampling Theorems

The Nyquist theorem concerns digital sampling of a
 continuous time analog waveform, while Shannon’s Sampling theorem concerns the creation of a
 continuous time analog waveform from digital, discrete samples.

Nyquist Theorem

alias

passband

alias

5 MHz

6 MS/s

[IMAGE alt='image' src='GUID-C313ADA4-C41D-4825-8793-4979637F1136-a5.svg']

The 5 MHz
 frequency aliases back in the passband, falsely appearing as a 1 MHz sine wave.

Shannon’s Sampling Theorem

5 MHz

6 MS/s

5 MHz

[IMAGE alt='image' src='GUID-C313ADA4-C41D-4825-8793-4979637F1136-a5.svg']

In this case, the
 high–frequency sine wave is the desired signal, but was severely undersampled by only
 being generated by a 6 MS/s DAC; the actual resulting
 waveform is a 1 MHz signal.

In
 systems where you want to generate accurate signals using sampled data, the sampling
 rate must be set high enough to prevent aliasing.

Parent topic:

Sample Rate

Related concepts:

- Sample Rate

<!--NI_TOPIC bundle=ni-rfsg path=saving-a-configuration.html language=enus -->
## TOPIC 00070: Saving a Configuration

- bundle_id: `ni-rfsg`
- source_path: `saving-a-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/saving-a-configuration.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: The NI-RFSG Soft Front Panel allows you to save all the current settings, and to later recall them to restore the Soft Front Panel to a predefined state. The NI-RFSG SFP uses the TDMS file type for this purpose. Although the configuration is stored in binary format, you can open and read TDMS files

### Saving a Configuration

The NI-RFSG Soft Front Panel
 allows you to save all the current settings, and to later recall them to restore the Soft Front
 Panel to a predefined state. The NI-RFSG SFP uses the TDMS file
 type for this purpose.

[IMAGE alt='image' src='GUID-F8598C82-FCF9-4737-9867-0363C7029624-a5.png']

When you view a configuration file in the NI LabVIEW TDMS Viewer,
 parameter values are stored in the StateDB group, and any waveform data
 loaded in Arb mode is stored in the Waveforms group. To view the waveform
 data, click the Values (table) tab or the Analog Values
 (graph) tab.

Click the Save button to save measurement and
 acquisition configurations in the TDMS file format.Click the Save to
 File softkey to save to a TDMS file, or click one of the Quick
 Save softkeys to allow for one click save/recall. Click the
 Recall button to recall a previously saved configuration.

To save your current Soft Front Panel settings, complete the following
 steps:

1. Click the Save button or select File»Save Configuration.
2. If you clicked on the Save button, click the Save to
 File softkey, otherwise, skip to step 3.
3. Specify a path and file name in the dialog box.
4. Click OK.

To apply a Soft Front Panel configuration that was previously saved,
 complete the following steps:

1. Click the Recall button or select File»Recall Configuration .
2. If you clicked the Recall button, click the
 Recall from File softkey, otherwise, skip to step 3.
3. In the file dialog box, navigate to the configuration that you want
 to recall.
4. Click OK .

Parent topic:

NI-RFSG Soft Front Panel

Related concepts:

- Supported Data File Formats in the NI-RFSG SFP

<!--NI_TOPIC bundle=ni-rfsg path=scriptend-script.html language=enus -->
## TOPIC 00071: script/end script

- bundle_id: `ni-rfsg`
- source_path: `scriptend-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/scriptend-script.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the script/end script statement to define a set of instructions to be contained within a single script and to associate a name with that script. Script names must be unique, and they cannot have the same name as a waveform name. Usage: script script name instructions end script Create a simple s

### script/end script

Use the script/end script statement to define a set of instructions to
 be contained within a single script and to associate a name with that script.

Script names must be unique, and they cannot have the same name as a waveform name.

Usage:

```text
script script name
  instructions
end script
```

#### Create a simple script named myScript to generate
 myWfm

```text
script myScript
  generate myWfm
end script
```

#### Create multiple scripts named myScript1 &
 myScript2

```text
script myScript1
  generate myWfmA
end script

script myScript2
  generate myWfmB
end script
```

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=scripting-instructions.html language=enus -->
## TOPIC 00072: Scripting Instructions

- bundle_id: `ni-rfsg`
- source_path: `scripting-instructions.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/scripting-instructions.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scripts consist of five primary instructions: generate, repeat/end repeat, wait, if/else/end if, and clear. Additionally, all instructions in a script are surrounded by the keywords script script name/end script. Multiple scripts can exist on the device at one time—you can choose which script to exe

### Scripting Instructions

Scripts consist of five primary instructions: generate,
 repeat/end repeat, wait, if/else/end
 if, and clear. Additionally, all instructions in a script
 are surrounded by the keywords script script name/end
 script. Multiple scripts can exist on the device at one time—you can choose
 which script to execute by referencing the script name.

For examples of scripting applications, refer to *Common Scripting Use
 Cases*.

Note

wait

PXI-5670/5671

PXIe-5672

PXI-5610

PXI-5671

8.33 MS/s

Note

stream n

PXIe-5673E

Note

- if else is not supported.
- break instruction is not supported.
- stream instruction is not supported.
- The maximum compiled script size is 6,100 instructions. Each script language
 instruction requires roughly one compiled instruction, plus one instruction for
 each marker.
- Nested repeats are only allowed if the outer repeat is a
 repeat forever instruction, and there are no other
 instructions preceding it or past the end of the repeat block.
 You can only use a single nesting level.
- Markers are allowed in generate and finite
 wait instructions. They are not allowed in conditional
 wait instructions.

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsg path=scripts.html language=enus -->
## TOPIC 00073: NI-RFSG Scripts

- bundle_id: `ni-rfsg`
- source_path: `scripts.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/scripts.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can link and loop multiple waveforms together in a generation operation using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. The script can specify the order in which the waveforms are generated, the number of ti

### NI-RFSG
 Scripts

You can link and loop multiple waveforms together in a
 generation operation using a script. A *script* is a series of
 instructions that indicates how waveforms saved in the onboard memory should be sent to the
 DUT.

The script can specify the order in which the waveforms are generated,
 the number of times they are generated, and the triggers and markers associated with the
 generation.

Note

NI-RFSG

#### Basic Scripting Example

You can create a script to manage waveform generation based on
 multiple waveforms and triggers. For example, you could download waveforms A, B, C,
 and D into instrument memory and script it to do the following:

1. Wait for a trigger to initiate generation
2. Upon receiving this trigger, generate waveform A three times
 with a marker at position 16 each time
3. Generate waveforms B, C, and D twice (BCDBCD)

The following is the script of this example:

```text
script myFirstScript
    wait until scriptTrigger0
    repeat 3
        generate waveformA marker0(16)
    end repeat
    repeat 2
        generate waveformB
        generate waveformC
        generate waveformD
    end repeat
end script
```

<!--NI_TOPIC bundle=ni-rfsg path=setting-properties-and-attributes-before-read.html language=enus -->
## TOPIC 00074: Set Properties Before Reading Them

- bundle_id: `ni-rfsg`
- source_path: `setting-properties-and-attributes-before-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/setting-properties-and-attributes-before-read.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify properties when you set them or when you call a configuration function that sets them. It's important to set the properties or call any configuration functions before reading back any property values for the following reasons: The driver coerces read values depending on the current co

### Set Properties Before Reading Them

You can modify properties when you set them or when you call a configuration function
 that sets them.

It's important to set the properties or call any configuration
 functions before reading back any property values for the following reasons:

- The driver coerces read values depending on the current
 configuration of the session. If you read a property value and then set other
 properties, the value read may no longer be valid.
- The driver verifies that the configuration of the device is
 valid when reading the property. It's possible to get an error when reading a
 property if the configuration isn't valid at that point, even when a setting later
 could make it valid.
- Reading properties causes the driver to verify the current
 configuration. If you change some settings later, you need to validate those
 settings again.

Note

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsg path=signal-routing-concepts.html language=enus -->
## TOPIC 00075: Signal Routing in NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `signal-routing-concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/signal-routing-concepts.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI VSTs are capable of sending and receiving signals through the front panel connectors and the PXI trigger bus. Signals are routed between a source and destination via a path through the PXI trigger bus; there are two broad categories of routes. The front panel connectors provide connectivity for i

### Signal Routing in NI-RFSG

NI VSTs are capable of sending and receiving signals
 through the front panel connectors and the PXI trigger bus. Signals are routed between a
 source and destination via a path through the PXI trigger bus; there are two broad
 categories of routes.

The front panel connectors provide connectivity for input and output
 signals as well as for the control lines that send and receive clocks, triggers, and
 events. You can use the PXI trigger bus to send and receive events, triggers, and Sample
 and Reference Clocks.

Signals can be routed to and from the supported front panel connectors
 of your instrument. All signal routing operations can be characterized by a
 source and a destination. The possible signal
 routes for your instrument depend on the instrument, the PXI chassis, and the occupied
 PXI chassis slot.

When a signal is exported to a PXI trigger bus line from an
 instrument, only instruments in the same PXI chassis segment recognize the signal from
 that PXI trigger bus line. To route the signal to instruments in a different PXI chassis
 segment, you must establish a *dynamic route* or *static
 route*.

Dynamic route

NI recommends using dynamic reservations
 and routing whenever possible.

Static route

Triggers

Refer to your chassis documentation to determine the PXI trigger bus segments of your
 chassis.

Related concepts:

- Open-Loop and Closed-Loop Use Cases

<!--NI_TOPIC bundle=ni-rfsg path=simulating-a-device.html language=enus -->
## TOPIC 00076: Simulating a Device Using NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `simulating-a-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/simulating-a-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: Simulate your device using NI-RFSG to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Simulating a device also allows you to evaluate an NI product even if you don't have the hardware. Complete the

### Simulating a Device Using NI-RFSG

Simulate your device using NI-RFSG to develop, modify,
 and/or test an application without hardware. Using a simulated device to test an application
 eliminates the risk of hardware damage. Simulating a device also allows you to evaluate an NI
 product even if you don't have the hardware.

Complete the following steps to create and configure a
 simulated NI-RFSG device using the NI-RFSG instrument driver.

1. Call Initialize With Options.
2. Set the option string parameter. 
 The option string parameter is composed of the
 Simulate and the DriverSetup keywords, as illustrated
 in the following example: 
 Simulate=1,DriverSetup=Model:model number;
 BoardType:type 
 Note You must enable simulation (Simulate=1) to
 simulate any device.
 The following table shows the valid values for model number and
 type:
 Table 4.Valid Values for Model Number and TypeOption
 Valid Valuesmodel number
 5610, 5611, 5644R, 5645R, 5646R, 5650, 5650E, 5651, 5651E, 5652, 5652E,
 5653, 5654, 5670, 5671, 5672, 5673, 5673E, 5820, 5830, 5831, 5840, 5841, 5842,
 5860
 type
 PXI, PXIe
 Note For PXI/PXIe-5650/5651/5652
 devices only, you can use the BoardType:PXI and the
 BoardType:PXIe values to indicate whether a module is PXI or PXI
 Express, respectively.

#### Simulating a PXIe-5673E

When simulating the PXIe-5673E, you can
 use any of the following option string parameters:

- Simulate=1,DriverSetup=Model:5673E
- Simulate=1,DriverSetup=Model:5611; AWG:5450; LO:5652E
- Simulate=1,DriverSetup=Model:5611; AWG:5450; LO:5652;
 loBoardType:PXIe

To simulate a PXIe-5673E with an external
 LO, use the following option string:

Simulate=1,DriverSetup=Model:5611; AWG:5450;
 LO:<external>

#### Simulating a PXIe-5650

When simulating the PXIe-5650, use either
 of the following option string parameters:

- Simulate=1,DriverSetup=Model:5650E
- Simulate=1,DriverSetup=Model:5650; BoardType:PXIe

#### Simulating a PXIe-5842

When simulating the PXIe-5842, use the
 following option string parameter:

Simulate=1,DriverSetup=Model:5842; LO:5655

#### Simulating a PXIe-5860

When simulating the PXIe-5860, use the following
 option string parameter:

Simulate=1,DriverSetup=Model:5860;Channel:0

Parent topic:

Programming Considerations

Related concepts:

- NI-RFSG Driver Setup Options

Related tasks:

- Simulating an NI-RFSG Device

<!--NI_TOPIC bundle=ni-rfsg path=simulating-an-ni-rfsg-device.html language=enus -->
## TOPIC 00077: Simulating an NI-RFSG Device

- bundle_id: `ni-rfsg`
- source_path: `simulating-an-ni-rfsg-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/simulating-an-ni-rfsg-device.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: Simulate an NI-RFSG device using MAX to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated device to evaluate an NI product for which you do not have hardware.Simu

### Simulating an NI-RFSG Device

Simulate an NI-RFSG device
 using MAX to develop, modify, and/or test an application without hardware.

Note

PXIe-5611

PXI/PXIe-5650/5651/5652

PXIe-5653

To create and configure a simulated NI-RFSG device in MAX, complete the following steps:

1. Select Devices and Interfaces in the configuration tree, and
 click Create New in the MAX toolbar. 
 The Create New dialog box opens.
2. Select Simulated NI-DAQmx Device or Modular Instrument, and
 click Finish. 
 The Create Simulated NI-DAQmx Device dialog box
 opens.
3. Expand RF Devices, and select the NI-RFSG device to simulate.
4. Click OK. 
 The NI-RFSG device appears in the MAX
 configuration tree with a yellow icon to indicate it is a simulated device.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSG

Related tasks:

- Simulating a Device Using NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=sinad.html language=enus -->
## TOPIC 00078: SINAD

- bundle_id: `ni-rfsg`
- source_path: `sinad.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/sinad.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal-to-noise-and-distortion ratio (SINAD) is the ratio of the RMS signal amplitude to the RMS sum of all other spectral components, including the harmonics but excluding DC. SINAD is usually expressed in dB.

### SINAD

Signal-to-noise-and-distortion ratio (SINAD) is the ratio
 of the RMS signal amplitude to the RMS sum of all other spectral components, including the
 harmonics but excluding DC. SINAD is usually expressed in dB.

Parent topic:

Understanding RF Specifications

Related concepts:

- ENOB

<!--NI_TOPIC bundle=ni-rfsg path=stream-n.html language=enus -->
## TOPIC 00079: stream n

- bundle_id: `ni-rfsg`
- source_path: `stream-n.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/stream-n.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Usage: Stream n samples: stream nstream n Stream the data and generate a Marker event when a position(s) within the data is generated:stream n marker0 (position 1, position 2, ... , position n)Specify each position in samples. Use the Export Signal VI/function for your driver to specify the destinat

### stream
 *n*

Usage:

- Stream n samples: stream
 n stream n
- Stream the data and generate a Marker event when a position(s) within the data is
 generated: stream n marker0 (position 1, position 2, ... , position n) Specify
 each position in samples. Use the Export Signal VI/function for your
 driver to specify the destination terminal of the marker. Marker position is zero-based.
 For example, 0 refers to the first point in the data, 63
 refers to the 64th point in the data, and so on.

The following restrictions apply when using the stream n
 statement:

- The script may not contain conditional statements, including if-else ,
 repeat until , and break statements.
- Markers must be on 128 byte boundaries.

#### stream n Examples

- Stream 1,280
 samples: Script myScript
 stream 1280
end script
- Stream
 forever: Script myScript
repeat forever
 stream 1280
end repeat
end script

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=streaming-waveform-data.html language=enus -->
## TOPIC 00080: Streaming Waveform Data in NI-RFSG

- bundle_id: `ni-rfsg`
- source_path: `streaming-waveform-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/streaming-waveform-data.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of an instrument. The following instructions are a guide for configuring your application for streaming. For a programmatic example, refer to RFSG Arbitrary Waveform Streaming.vi for LabVIEW or ArbitraryWaveform

### Streaming Waveform Data in NI-RFSG

*Streaming* is a way to generate waveforms that
 are too large to fit in the onboard memory of an instrument.

The following instructions are a guide for configuring your application
 for streaming. For a programmatic example, refer to RFSG Arbitrary Waveform
 Streaming.vi for LabVIEW or ArbitraryWaveformStreaming.prj
 for LabWindows/CVI, available using the NI Example Finder.

As an example, we have a 1.6 GB waveform we
 want to generate and an NI arbitrary waveform generator with 256 MB of onboard memory. This 1.6 GB waveform may be
 in the host memory, on disk, or data that your application generates dynamically during
 generation.

1. Identify the streaming waveform —Set the
 Streaming Waveform Name property. Setting this property ensures that none
 of your streaming data is overwritten before it is generated. NI-RFSG monitors your progress to ensure that you write fresh data fast enough to
 keep up with the generation. If your application fails to keep up or attempts to write fresh
 data over data that has not been generated, NI-RFSG returns
 an error.
2. Specify the amount of onboard memory to be used for
 streaming —Call NI-RFSG 
 Allocate Arb Waveform to specify the amount of onboard memory to reserve
 for streaming. The allocated memory, known as the streaming waveform ,
 serves as a buffer for the streaming process. The size of the waveform you wish to stream
 must be evenly divisible by the amount of onboard memory allocated for streaming to prevent
 the streaming waveform from being overwritten before it has generated.
3. Fill the streaming waveform with initial
 data —Call NI-RFSG 
 Write Arb Waveform to write the first part of the waveform data to the
 streaming waveform in onboard memory. Tip When
 transferring large blocks of waveform data, break the data into smaller blocks and call
 the NI-RFSG
 Write Arb Waveform multiple times. The data is appended sequentially. A
 computer can allocate smaller blocks of a large waveform faster than allocating a single
 large contiguous block in memory. Depending on the amount of RAM on the computer,
 transferring ten 16 MB blocks may be faster than
 transferring one 160 MB block.
4. Begin generating the waveform —Call NI-RFSG 
 Initiate to begin the waveform generation. As the waveform generates,
 space in the streaming waveform becomes free.
5. (Optional) Monitor available memory as the waveform
 generates —Use the Space Available in Streaming Waveform 
 property to determine how much of the streaming waveform is free for writing new data. As
 the waveform generates, space becomes available to write more waveform data.
6. Write a block of waveform data —Call NI-RFSG 
 Write Arb Waveform to write a new block of waveform data to the streaming
 waveform in onboard memory. If the size
 of the new block of waveform data is larger than the space available, NI-RFSG waits until
 sufficient space becomes available or the streaming write time expires. Use the
 Streaming Write Timeout property to change the streaming write
 time.
7. Repeat steps 5 and 6 until all waveform data is written.

Parent topic:

NI-RFSG Streaming

Related concepts:

- NI-RFSG Examples

<!--NI_TOPIC bundle=ni-rfsg path=streaming.html language=enus -->
## TOPIC 00081: NI-RFSG Streaming

- bundle_id: `ni-rfsg`
- source_path: `streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/streaming.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of an RF signal generator. Streaming can be used in Arbitrary Waveform or Script generation modes. You can stream waveforms only when the power level is defined as a peak power, not an average power. To stream w

### NI-RFSG
 Streaming

*Streaming* is a way to generate waveforms that
 are too large to fit in the onboard memory of an RF signal generator.

Streaming can be used in Arbitrary Waveform or Script generation
 modes. You can stream waveforms only when the power level is defined as a peak power,
 not an average power.

To stream waveform data, allocate and identify all or a portion of the
 RF signal generator onboard memory to act as an onboard waveform for streaming. Before
 initiating waveform generation, fill that onboard memory with the first part of your
 waveform. As the waveform is generated, continuously write the remaining waveform data
 until generation is complete. The RF signal generator uses the instrument to stream the
 waveform.

- [Streaming Waveform Data in NI-RFSG](streaming-waveform-data.html) Streaming is a way to generate waveforms that are too large to fit in the onboard memory of an instrument.
- [Improving NI-RFSG Streaming Performance](improving-streaming-performance.html)

<!--NI_TOPIC bundle=ni-rfsg path=supported-data-file-formats-sfp.html language=enus -->
## TOPIC 00082: Supported Data File Formats in the NI-RFSG SFP

- bundle_id: `ni-rfsg`
- source_path: `supported-data-file-formats-sfp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/supported-data-file-formats-sfp.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI-RFSG SFP to import data from a file for generation. The SFP supports text and TDMS waveform file formats. Use NI RF Toolkit Soft Front Panels to generate TDMS files that are supported by the NI-RFSG SFP.Text FilesFormat data in text files in the following ways: As two columns of I

### Supported Data File Formats in the NI-RFSG SFP

You can use the NI-RFSG SFP
 to import data from a file for generation. The SFP supports text and TDMS waveform file
 formats.

Use NI RF Toolkit Soft Front Panels to generate TDMS files that are
 supported by the NI-RFSG SFP.

#### Text Files

- As two columns of I/Q data separated by a delimiter
- As a single row of interleaved I/Q data with elements separated by a
 delimiter

The Import parameters dialog box for text files
 includes the following options:

- File Information
  - Column Delimiter —Specifies the type of delimiter
 the file uses—tab, comma, or semicolon.
  - Decimal Point —Specifies the type of character the
 file uses for a decimal point—system-defined, period, or comma.
  - Offset (bytes) —Specifies the number of bytes
 (characters) to ignore at the beginning of the file to account for a
 header.
- Data
  - Array Type —Specifies whether the data is
 formatted as 2D , which corresponds to two columns
 of I/Q data, or 1D Interleaved , which corresponds
 to a single row of interleaved I/Q data.
  - IQ Rate (S/s) —Specifies the I/Q rate of the data.
 The default value is 100 MS/s .
- Swap I & Q —Enables noninverse phase rotation of the
 I/Q signal by swapping the I and Q values in the data.

#### TDMS Files

When you import
 a TDMS file, the SFP populates the waveform name, headroom, and I/Q rate values from
 the corresponding properties in the TDMS file.

Note

Parent topic:

NI-RFSG Soft Front Panel

Related tasks:

- Importing Data to the NI-RFSG SFP for Generation
- Saving a Configuration

<!--NI_TOPIC bundle=ni-rfsg path=syntax-for-terminal-names.html language=enus -->
## TOPIC 00083: Syntax for Terminal Names

- bundle_id: `ni-rfsg`
- source_path: `syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/syntax-for-terminal-names.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multipledevices, terminal names begin with a forward slash, followed by thename of the device as configured in MAX, such as Dev1. A forward sl

### Syntax for Terminal Names

The syntax for terminal names is a unique identifier that
 refers to a physical terminal in your system.

To guarantee the uniqueness of a terminal name across multipledevices,
 terminal names begin with a forward slash, followed by thename of the device as
 configured in MAX, such as Dev1. A forward slash and the nameof the
 terminal follow the device identifier, such as PFI1. For example, the
 fullyqualified terminal name for PFI1 on Dev1 is
 /Dev1/PFI1.

Parent topic:

Signal Routing in NI-RFSG

<!--NI_TOPIC bundle=ni-rfsg path=system-requirements.html language=enus -->
## TOPIC 00084: System Requirements

- bundle_id: `ni-rfsg`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/system-requirements.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSG has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM* A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs *Depending on the amount of data acquired and/or processed, a larger amount of memory may be required. G

### System Requirements

NI-RFSG has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM*
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

*Depending on the amount of data acquired and/or processed, a larger amount of memory may
 be required.

Note

Guest accounts are not supported under any OS.

<!--NI_TOPIC bundle=ni-rfsg path=toi.html language=enus -->
## TOPIC 00085: TOI

- bundle_id: `ni-rfsg`
- source_path: `toi.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/toi.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Third-order intercept (TOI) point is a measurement of the degree of linearity of a system. TOI point is a calculated number derived from a two-tone intermodulation test. Typically, two tones of the same power level and of different frequencies are applied to the input of a device. When the signal is

### TOI

Third-order intercept (TOI) point is a measurement of the
 degree of linearity of a system. TOI point is a calculated number derived from a two-tone
 intermodulation test.

Typically, two tones of the same power
 level and of different frequencies are applied to the input of a device. When the
 signal is generated, the two desired tones appear with distortion products. These
 distortion products are a result of nonlinearities within the device. The following
 equation represents the input signals:

x

(

t

)

=

A

1

cos

(

ω

1

t

)

+

A

2

cos

(

ω

2

t

)

A nonlinear device has an output response that is expressed by the following
 equation:

y

(

t

)

=

a

1

x

(

t

)

+

a

2

x

2

(

t

)

+

a

3

x

3

(

t

)

+

...

where

- a x coefficients represent the gain and the degree of
 nonlinearity within the device
- x 2 terms represent the second-order distortion
 terms
- x 3 represents the third-order distortion terms
- a
 1
 x
 (
 t
 ) represents the desired output

Plugging *x(t)* into *yt* results in distortion factors
 shown in the following table:

| Frequency | Distortion Order | Typical Output Power Level |
| --- | --- | --- |
| 0 (DC offset) | Second | 0.5 α 2 ( A 1 2 + A 2 2 ) |
| 2ω1 | Second | 0.5 α 2 A 1 2 |
| 2ω2 | Second | 0.5 α 2 A 2 2 |
| ω2 - ω1 | Second | 0.5 α 2 A 1 A 2 |
| ω2 + ω1 | Second | 0.5 α 2 A 1 A 2 |
| 3ω1 | Third | 0.25 α 3 A 1 3 |
| 3ω2 | Third | 0.25 α 3 A 2 3 |
| ω1 | Third | 0.75 α 3 A 1 3 + 1.5 A 1 A 2 2 |
| ω2 | Third | 0.75 α 3 A 2 3 + 1.5 A 2 A 1 2 |
| 2ω2 - ω1, 2ω2 + ω1 | Third | 0.75 α 3 A 1 A 2 2 |
| 2ω1 - ω2, 2ω1 + ω2 | Third | 0.75 α 3 A 2 A 1 2 |

The terms of most interest are

2

ω

2

−

ω

1

2

ω

1

−

ω

2

[IMAGE alt='image' src='GUID-40A4967C-7D2A-409B-B865-3279192964AC-a5.gif']

The output second-order intercept point (OIP<sub>2</sub>)
 and the output third-order intercept point (OIP<sub>3</sub>) occur where the
 second-order line and third-order line, respectively, intersect the desired output
 signal. If *A*<sub>1</sub> is set equal to
 *A*<sub>2</sub>, and each value is
 increased by 1 dB, then the third-order distortion
 products increases 3 dB for every 1 dB increase in output power. The second-order
 distortion products increases 2 dB for every 1 dB increase in output power. Therefore, based on a
 two-tone intermodulation test, the output IP<sub>3</sub> can be calculated using the following
 formula:

OIP<sub>3</sub> = P<sub>out</sub> (dBm) +
 .5IMD<sub>3rd</sub>(dBc)

OIP<sub>2</sub> = P<sub>out</sub> (dBm) +
 IMD<sub>2nd</sub>(dBc)

The TOI is dependent upon power levels. The
 following table summarizes typical RF signal generator performance.

| Frequency (MHz) | -20 dBm/tone | -6 dBm/tone | 5 dBm/tone |
| --- | --- | --- | --- |
| 100 | 86 dBc | 78 dBc | 54 dBc |
| 1000 | 86 dBc | 86 dBc | 54 dBc |
| 2000 | 86 dBc | 86 dBc | 50 dBc |
| 2700 | 86 dBc | 82 dBc | 46 dBc |

As the power output level increases, the TOI point increases, except for
 power levels above -3 dBm/tone. Beyond -3 dBm/tone, there is a step reduction in the TOI
 point, as shown in the preceding table. The second-order intercept point behaves in
 a similar manner. This step change above -3 dBm/tone
 is caused by the architecture and attenuator locations of the PXI-5610 RF Signal Upconverter module.

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=total-harmonic-distortion-thd.html language=enus -->
## TOPIC 00086: Total Harmonic Distortion

- bundle_id: `ni-rfsg`
- source_path: `total-harmonic-distortion-thd.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/total-harmonic-distortion-thd.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Total harmonic distortion (THD) is a representation of the effect that multiple harmonic spurs throughout a spectrum band have on the fundamental tone. You can calculate THD by summing the power in each of the harmonics and dividing by the total power of the fundamental. As a general principle, a si

### Total Harmonic Distortion

Total harmonic distortion (THD) is a
 representation of the effect that multiple harmonic spurs throughout a spectrum band have on
 the fundamental tone.

You can calculate THD by summing the power in each of the harmonics and dividing by the
 total power of the fundamental. As a general principle, a signal becomes visibly
 distorted when the THD approaches -30 dB.

The equation for THD is:

THD

=

V

h

2

2

+

V

h

3

2

+

V

h

4

2

+

...

+

V

h

N

2

V

fund

×

100

%

As this equation suggests, the THD specification evaluates the power in harmonic spurs
 from the second through the *n*<sup>th</sup> harmonic. In practice, typical
 signal generators feature THD specifications for harmonics two through six. The
 following figure shows an example plot of a generated signal. The figure also
 illustrates the concept of THD specification in signal generators.

[IMAGE alt='image' src='GUID-885E680B-7FC8-49EE-B811-1B1E4432789D-a5.gif']

The above figure shows an example plot of a 20 kHz
 sinusoid that is generated with an arbitrary waveform generator. Notice the power levels
 of the harmonic spurs, indicated with circles. This generator features -77 dBc or better of THD for the second through sixth
 harmonics.

THD generally deteriorates as the generated signal increases in frequency. When working
 with a signal generator, be sure to consider the THD throughout the bandwidth of the
 generator.

Parent topic:

Understanding RF Specifications

Related concepts:

- Harmonic Distortion

<!--NI_TOPIC bundle=ni-rfsg path=trigger-types.html language=enus -->
## TOPIC 00087: Trigger Types

- bundle_id: `ni-rfsg`
- source_path: `trigger-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/trigger-types.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger your RF signal generator using various trigger types. Individual triggers may not support all trigger types listed here.

### Trigger Types

Trigger your RF signal generator using various trigger types.

Note

- [None](ni-rfsg-none.html) Signal generation starts immediately upon execution of the NI-RFSG Initiate function; no Start or Script trigger is necessary to begin generation.
- [Digital Edge](ni-rfsg-ni-rfsa-digital-edge.html) A digital edge trigger acts on the rising or falling edge of a digital signal.
- [Digital Level](ni-rfsg-digital-level-trigger.html) A channel performs an operation when a signal goes below a defined low level or above a defined high level.
- [Software Edge](ni-rfsg-software.html) After initiation, a software trigger is generated internally by a programmatic call using NI-RFSG and can occur at any time, based upon the conditions specified in the program.

Parent topic:

NI-RFSG Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsg path=understanding-rf-specifications.html language=enus -->
## TOPIC 00088: Understanding RF Specifications

- bundle_id: `ni-rfsg`
- source_path: `understanding-rf-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/understanding-rf-specifications.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use key parameters to define the performance and quality of RF signal generation.

### Understanding RF Specifications

Use key parameters to define the performance and quality of RF signal
 generation.

- [Output Attenuation](output-attenuation.html) Output attenuation is a method of controlling the output voltage level of the signal being generated.
- [Output Impedance](output-impedance.html)
- [ENOB](enob.html) Effective number of bits (ENOB) is another way of specifying signal-to-noise and distortion ratio (SINAD).
- [EVM](evm.html) Error vector magnitude (EVM) is a measurement of demodulator performance in the presence of impairments.
- [Harmonic Distortion](harmonic-distortion.html) Harmonic distortion measures the amount of power that is contained in the harmonics of a fundamental signal. Harmonic distortion is inherent to devices and systems that possess nonlinear characteristics—the more nonlinear the device, the greater its harmonic distortion.
- [MER](mer.html) The modulation error ratio (MER) is a measure of the signal-to-noise ratio (SNR) in a digitally modulated signal. Like SNR, MER is usually expressed in dB.
- [Noise Figure](noise-figure.html)
- [Noise Floor](noise-floor.html) Noise floor is the noise level below which signals cannot be detected under the same measurement conditions.
- [Phase Noise](phase-noise.html) Phase noise refers to noise in a carrier signal due to phase and frequency modulation in the signal.
- [TOI](toi.html) Third-order intercept (TOI) point is a measurement of the degree of linearity of a system. TOI point is a calculated number derived from a two-tone intermodulation test.
- [SINAD](sinad.html) Signal-to-noise-and-distortion ratio (SINAD) is the ratio of the RMS signal amplitude to the RMS sum of all other spectral components, including the harmonics but excluding DC. SINAD is usually expressed in dB.
- [Total Harmonic Distortion](total-harmonic-distortion-thd.html) Total harmonic distortion (THD) is a representation of the effect that multiple harmonic spurs throughout a spectrum band have on the fundamental tone.
- [IMD3](imd3.html) Two-tone third-order intermodulation distortion (IMD3) is the measure of the third-order distortion products produced by a nonlinear device when two tones closely spaced in frequency are fed into its input. This distortion product is usually so close to the carrier that it is almost impossible to filter out and can cause interference in multichannel communications equipment.
- [VSWR](vswr.html) Voltage standing wave ratio (VSWR) is the ratio of reflected-to-transmitted waves.

<!--NI_TOPIC bundle=ni-rfsg path=user-manual-welcome.html language=enus -->
## TOPIC 00089: NI-RFSG User Manual

- bundle_id: `ni-rfsg`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSG User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-RFSG
 User Manual

The NI-RFSG User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-RFSG
- NI-RFSG Release Notes
- Interactive Activation Guide
- RFSG C API Reference Manual
- NI-RFSG C# .NET API Reference Manual
- NI-RFSG LabVIEW Reference
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-rfsg path=using-net-class-library.html language=enus -->
## TOPIC 00090: Using the .NET Class Library

- bundle_id: `ni-rfsg`
- source_path: `using-net-class-library.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/using-net-class-library.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the .NET class library to initialize, configure, initiate, generate, and close a session on your device. The .NET API is an IVI-compliant instrument driver that features a set of methods and properties that exercise the functionality of the hardware. 1. Initialization Use a constructor t

### Using the .NET Class Library

You can use the .NET class library to initialize,
 configure, initiate, generate, and close a session on your device. The 
 .NET API is an IVI-compliant instrument driver that features a set of methods and properties
 that exercise the functionality of the 
 hardware.

#### 1. Initialization

Use a constructor to create a new instance of the NIRfsg class.

Important

```text
VB.NET

Dim session As New NIRfsg(resourceName, True, False) ' Initialize
```

```text
Visual C#

NIRfsg session = new NIRfsg(resourceName, true, false); // Initialize
```

#### 2. Configuration

Use the NIRfsg object to configure the waveform properties

```text
VB.NET

Dim session As New NIRfsg(resourceName, True, False) ' Initialize
session.RF.Configure(10000000.0, -10)
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave
session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10000000.0)
```

```text
Visual C#

NIRfsg session = new NIRfsg(resourceName, true, false); // Initialize
session.RF.Configure(10E6, -10);
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave;
session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10E6);
```

#### 3. Initiate

The device starts generating the configured
 waveform signal as soon as you initiate the signal generation, unless the driver is waiting for a trigger.

```text
VB.NET 

session.Initiate()
```

```text
Visual C#

session.Initiate();
```

#### 4. Check Generation Status

Check whether the device is generating the signal or has stopped generating the
 signal. You use this step to check for any errors that might occur during signal
 generation or to check whether the device has completed the signal generation.

```text
VB.NET

session.CheckGenerationStatus()
```

```text
Visual C#

session.CheckGenerationStatus();
```

#### 5. Close

Close the session to the device and free unmanaged resources that are held by the
 session. You can close the session with Close or
 Dispose.

```text
VB.NET

session.Close()
                or
session.Dispose()
                or 
Using session As New NIRfsg(resourceName, True, True)
    'User code goes here. 
End Using
```

```text
Visual C#

session.Close();
                or
session.Dispose();
                or
using (NIRfsg session = new NIRfsg(resourceName, true, true))
{
    // User code goes here.
}
```

#### Example: Generating a
 Waveform

The following code snippet generates a basic waveform.

```text
VB.NET

Using session As New NIRfsg(resourceName, True, True) 
    session.RF.Configure(10000000.0, -10)
    session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave
    session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10000000.0)
    session.Initiate()
End Using
```

```text
Visual C#

using (NIRfsg session = new NIRfsg(resourceName, true, true))
{
    session.RF.Configure(10E6, -10);
    session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave;
    session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10E6);
    session.Initiate();
}
```

Parent topic:

Programming Considerations

Related information:

- NI-RFSG C# .NET API Reference Manual

<!--NI_TOPIC bundle=ni-rfsg path=using-ni-rfsg-in-labview.html language=enus -->
## TOPIC 00091: Using NI-RFSG in LabVIEW

- bundle_id: `ni-rfsg`
- source_path: `using-ni-rfsg-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/using-ni-rfsg-in-labview.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To develop an NI-RFSG application in LabVIEW, follow these general steps: Open an existing or new LabVIEW VI. From the Function palette, locate the NI-RFSG VIs at Measurement I/O NI-RFSG . Select the VIs that you want to use and drop them on the block diagram to build your application.

### Using NI-RFSG
 in LabVIEW

To develop an NI-RFSG application in LabVIEW, follow these general steps:

1. Open an existing or new LabVIEW VI.
2. From the Function palette, locate the NI-RFSG VIs at Measurement I/O»NI-RFSG.
3. Select the VIs that you want to use and drop them on the block diagram to build
 your application.

Parent topic:

Creating an Application with NI-RFSG

Related concepts:

- NI-RFSG Examples

<!--NI_TOPIC bundle=ni-rfsg path=using-ni-rfsg-in-labwindowscvi.html language=enus -->
## TOPIC 00092: Using NI-RFSG in LabWindows/CVI

- bundle_id: `ni-rfsg`
- source_path: `using-ni-rfsg-in-labwindowscvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/using-ni-rfsg-in-labwindowscvi.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: To develop an NI-RFSG application in LabWindows/CVI, follow these general steps: Open an existing or new project file. Load the NI-RFSG function panel from the location specified in the NI-RFSG Readme. Use the function panel to navigate the function hierarchy. Generate function calls with the proper

### Using NI-RFSG
 in LabWindows/CVI

NI-RFSG

1. Open an existing or new project file.
2. Load the NI-RFSG function panel from the
 location specified in the NI-RFSG Readme.
3. Use the function panel to navigate the function hierarchy. Generate function
 calls with the proper syntax and variable values.

Parent topic:

Creating an Application with NI-RFSG

Related concepts:

- NI-RFSG Examples

<!--NI_TOPIC bundle=ni-rfsg path=using-rf-list-mode.html language=enus -->
## TOPIC 00093: Using RF List Mode

- bundle_id: `ni-rfsg`
- source_path: `using-rf-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/using-rf-list-mode.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: An RF configuration list consists of configuration list steps. Each step specifies the state of the instrument by specifying values for properties or attributes. Only select and add to the list the properties or attributes you want to set from step-to-step. To use RF list mode, complete the followin

### Using RF List Mode

An RF configuration list consists of configuration list
 steps. Each step specifies the state of the instrument by specifying values for properties
 or attributes.

Only select and add to the list the properties or attributes you
 want to set from step-to-step.

To use RF list mode, complete the following steps:

1. Create the RF configuration list by calling the niRFSG Create
 Configuration List VI or the
 niRFSG_CreateConfigurationList function. When you call
 this VI or function, pass the array of properties or attribute IDs that you
 intend to change between configuration list steps. When the set as
 active list or setAsActiveList parameter is
 set to TRUE (which is the default), the newly created list is set as the active
 configuration list.
2. If in the previous step you did not specify the active configuration list, do
 so now using the Active Configuration List property or the
 NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute. The active
 configuration list also specifies whether NI-RFSG
 operates using the RF list mode.
3. Typically, next you immediately populate the steps that make up that list.
 (Initially, the list has no steps.) To create the configuration steps, call the
 niRFSG Create Configuration List Step VI or the
 niRFSG_CreateConfigurationListStep function. When
 set as active step or
 setAsActiveStep is set to TRUE (which is the default),
 the newly created step becomes the active configuration list step.
4. If in the previous step you did not specify the active configuration list step,
 do so now using the Active Configuration List Step property or
 the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute.
 Initially, this configuration list step contains the driver default values for
 each configuration list property that you specified in the the niRFSG
 Create Configuration List VI or the
 niRFSG_CreateConfigurationList function. Now, while this
 step is active, use the property node or one of the set attribute functions to
 change the default values of those properties and attributes. 
 Note Configuration list steps are zero-based and numbered
 in the order in which you created them for the active list.
5. To start RF list mode operation, call the niRFSG Initiate VI
 or the niRFSG_Initiate function. If you set the active list
 to "" (empty string), the NI-RFSG device operates without using RF list mode. 
 After initiate, the device starts executing the list starting with step 0 as
 indicated by any of the following:The Active Configuration List property
 The NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST
 attribute
6. Specify how the RF configuration list advances from one step to the next by
 configuring the source for the configuration list trigger with the
 Configuration List Step Digital Edge Source property or the
 NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE
 attribute. 
 Generally, the configuration trigger can come from the following:An internal timer
 A waveform Marker Event in a script
 An external signal from the PXI trigger lines
 An external signal from front panel connectorsNote For the PXIe-5830/5831/5841 with PXIe-5655,
 RF list mode requires at least two available PXI backplane triggers for NI-RFSG synchronization or at least four
 available PXI backplane triggers for simultaneous NI-RFSA and NI-RFSG
 synchronization.

Parent topic:

RF List Mode

Related concepts:

- Open-Loop and Closed-Loop Use Cases

<!--NI_TOPIC bundle=ni-rfsg path=vswr.html language=enus -->
## TOPIC 00094: VSWR

- bundle_id: `ni-rfsg`
- source_path: `vswr.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/vswr.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Voltage standing wave ratio (VSWR) is the ratio of reflected-to-transmitted waves. Any impedance mismatches along a transmission line causes partial reflection of the propagating signals. The impedance difference determines the magnitude of the reflection. The length of a mismatched section determin

### VSWR

Voltage standing wave ratio (VSWR) is the ratio of
 reflected-to-transmitted waves.

Any impedance mismatches along a transmission line causes partial reflection of the
 propagating signals. The impedance difference determines the magnitude of the
 reflection. The length of a mismatched section determines the lowest signal frequencies
 that reflect from the section. VSWR is a measure of that signal reflection.With an
 incident sine wave into the switch module, some of the signal reflects down the line.
 This reflected wave interferes with the incident wave. VSWR is the ratio of maximum to
 minimum amplitude in the resulting interference wave, as shown in the following
 formula:

VSWR

=

1

+

[

p

]

1

−

[

p

]

- p is the reflection coefficient

Reflections can also be represented as a logarithmic ratio of the reflected signal to the
 input signal. This ratio is called return loss:

| RL (dB) = | 10 log (Pin / PREFLECTED) 20 log (Vin / VREFLECTED) –20 log (VREFLECTED / VIN) –20 log \|p\| |
| --- | --- |

Parent topic:

Understanding RF Specifications

<!--NI_TOPIC bundle=ni-rfsg path=wait.html language=enus -->
## TOPIC 00095: wait

- bundle_id: `ni-rfsg`
- source_path: `wait.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/wait.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pause execution of a script. You can pause the script until a particular Script trigger is received or until a specified number of samples are generated. Usage: Pause the execution until a particular Script trigger is received:wait until scripttrigger0If the Script trigger is received before the wai

### wait

Pause execution of a script. You can pause the script
 until a particular Script trigger is received or until a specified number of samples are
 generated.

Usage:

- Pause the execution until a particular Script trigger is
 received: wait until scripttrigger0 Note If the Script trigger is received before the
 wait instruction, then the script moves to the next
 instruction with the smallest possible delay. If you want to ignore Script
 triggers received before a wait statement, use the
 clear instruction.
- Pause the execution for a finite amount of
 time: wait number of samples
- Pause the execution for a finite amount of time and generates markers while
 waiting: wait 256 marker1(0, 128) marker0(64)

#### wait Examples

- Generate myWfmA , wait for receipt of a Script trigger, then
 generate
 myWfmB : generate myWfmA
wait until scripttrigger0
generate myWfmB
- Generate the sequence myWfmA , myWfmB five
 times; wait for receipt of a Script trigger; generate myWfmC ,
 myWfmD 10 times; wait for receipt of a Script
 trigger: repeat forever
 repeat 5
 generate myWfmA
 generate myWfmB
 end repeat
 wait until scripttrigger0
 repeat 10
 generate myWfmC
 generate myWfmD
 end repeat
 wait until scripttrigger0
end repeat
- Generate the sequence myWfmA , wait 100 samples, then generate
 myWfmB : wait 100
generate myWfmB
- Wait 256 samples, generating Marker 1 at samples 0 and 128, and generating
 Marker 0 at sample 64. Then generate Marker 0 and wait for receipt of a Script
 trigger: script waitWithMarkers
 wait 256 marker1(0, 128) marker0(64)
 wait until scripttrigger marker0(0)
end script

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-rfsg path=writing-waveforms-net.html language=enus -->
## TOPIC 00096: Writing Waveforms in the .NET Class Libraries

- bundle_id: `ni-rfsg`
- source_path: `writing-waveforms-net.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg/raw/resource/enus/writing-waveforms-net.html
- document_id: `ni-rfsg`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use one of the WriteWaveform methods to write waveform data to the onboard memory of an NI-RFSG device. To write a waveform to the onboard memory, you use the Arb property. Complete the following steps to write the waveform. Set the generation mode. You can set the device in either Arbitrary

### Writing Waveforms in the .NET Class Libraries

You can use one of the WriteWaveform methods to write waveform data to
 the onboard memory of an NI-RFSG device.

To write a waveform to the onboard memory, you use the Arb
 property. Complete the following steps to write the waveform.

1. Set the generation mode. You can set the device in either ArbitraryWaveform
 mode or Script mode. 
 VB.NET

Dim session As New NIRfsg(resourceName, True, False)
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ArbitraryWaveform
 Visual C#

NIRfsg session = new NIRfsg(resourceName, true, false);
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ArbitraryWaveform;
2. Allocate the waveform. 
 Note NI recommends allocating the onboard memory before
 writing the data into it.
 VB.NET

session.Arb.AllocateWaveform("waveformName", 1000)
 Visual C#

session.Arb.AllocateWaveform("waveformName", 1000);
3. Write the waveform into the onboard memory. 
 You can write one or more waveforms into the onboard memory; however, you can
 play only one waveform in the ArbitraryWaveform mode. Select this waveform
 using the SelectedWaveform property.
 You can use Script mode to generate multiple arbitrary waveforms based on the
 selected script.
 VB.NET

Dim dataArray As ComplexInt16() = New ComplexInt16(100) {}
For i as Short = 0 To dataArray.Length -1
 dataArray(i).Real = 1
 dataArray(i).Imaginary = 0 
Next
session.Arb.WriteWaveform(Of ComplexInt16)("waveformName", dataArray)
 Visual C#

ComplexInt16[] dataArray = new ComplexInt16[100];
for (short i = 0; i < dataArray.Length; i++)
{
 dataArray[i].Real = 1;
 dataArray[i].Imaginary = 0;
}
session.Arb.WriteWaveform<ComplexInt16>("waveformName", dataArray);

Parent topic:

Using the .NET Class Library

Related information:

- NI-RFSG C# .NET API Reference Manual
