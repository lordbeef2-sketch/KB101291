# NI DOCUMENT BUNDLE: ni-switch

<!--NI_BUNDLE_CHUNK bundle=ni-switch start=1 end=250 -->
<!--NI_TOPIC bundle=ni-switch path=about-the-ni-switch-health-center.html language=enus -->
## TOPIC 00001: About the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `about-the-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/about-the-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Switch Health Center simplifies relay maintenance and reliability in high-channel-count NI switching systems. The NI Switch Health Center executes a hardware-integrated relay continuity test that verifies that every relay on the card is functional, executes an integrated relay resistance test

### About the NI Switch Health Center

The NI Switch Health Center simplifies relay maintenance and reliability in
 high-channel-count NI switching systems. The NI Switch Health Center executes a
 hardware-integrated relay continuity test that verifies that every relay on the card is
 functional, executes an integrated relay resistance test that measures the resistance
 changes across relays, and provides access to the relay count tracking data stored on
 the cards. When you launch the NI Switch Health Center, the test starts automatically.
 Click the Start button to run the test again. Click the
 Abort button to stop a test in progress. Click the
 Report button to generate an HTML report that documents the
 results of the relay test and relay counts for each relay in your switching system.

#### NI Switch Health Center Tests

The NI Switch Health Center can report the following:

- Relay functionality using the integrated relay continuity test
- Relay contact resistance changes (ΔΩ) using the integrated relay resistance
 test
- Relay cycle counts using relay count tracking

Note

#### PCB Thumbnails

The NI Switch Health Center displays a thumbnail for the relay card in the main
 window beneath the card's PCB diagram, as shown in the figure below. You can use the
 drop-down arrow beneath the PCB diagram to select the PCB diagram you want to
 display.

[IMAGE alt='image' src='GUID-F7A70109-8BA9-4F44-B996-016F3BBA5555-a5.gif']

#### NI SwitchBlock

For NI SwitchBlock, the NI Switch Health Center displays thumbnails representing the
 card occupying the numbered slot. You can click on a thumbnail to view a specific
 card diagram. Thumbnails for slots without cards are grayed out completely, as shown
 in slot 6 in the figure below.

For cards occupying more than one slot, such as the NI 2833 and NI 2834, only the
 thumbnail of the left-most slot is enabled and the others are disabled. Slots 1 and
 2 in the figure below represent a multislot card. When you click on the thumbnail of
 an enabled multislot card, the diagram for the left-most PCB is displayed by
 default.

[IMAGE alt='image' src='GUID-FC303927-90EA-4DE5-AF4A-12DE96375BA4-a5.gif']

#### Test Results

Results from the relay test are graphically displayed on a PCB diagram and in a
 sortable table, making it easy to locate relays for replacement. If you click on any
 relay in the PCB diagram, its corresponding relay will be highlighted in the table.
 Conversely, if you click on any relay in the table, its corresponding relay in the
 PCB diagram will be highlighted.

Note

Double-pole relays are referred to by relay contact name. For example, a 2-Wire DPST
 relay is referred to as "kr0c0_w0" and "kr0c0_w1," with "_w0" referring to one relay
 contact and "_w1" referring to the other relay contact. When you select a relay on
 the PCB diagram, the first relay contact is highlighted in the results table. If you
 select either relay contact in the results table, the corresponding relay will be
 highlighted in the PCB diagram.

Note

If any relays fail the relay test, a banner will appear indicating that one or more
 relays have failed the test. The banner will also provide recommendations for the
 relay(s) that failed the test.

#### Report Generation

At the end of each relay test, you can generate an HTML report documenting the
 condition and resistance change of all the relays on each card along with their
 relay counts. Once the test has completed, click the Report
 icon to generate a report. The report can not be generated until the test for at
 least one card has completed. The report includes links to the online model pages
 for each device tested.

Note

Parent topic:

NI Switch Health Center Help

Related concepts:

- Accessing the NI Switch Health Center
- Switch Relay Maintenance with the NI Switch Health Center
- Testing Relays with the NI Switch Health Center
- Generating Reports with the NI Switch Health Center

<!--NI_TOPIC bundle=ni-switch path=accessing-the-ni-switch-health-center.html language=enus -->
## TOPIC 00002: Accessing the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `accessing-the-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/accessing-the-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can access the NI Switch Health Center from within Measurement & Automation Explorer (MAX) or from the Start menu. From MAX Right-click on a resource and select NI Switch Health Center, or Select a resource and click NI Switch Health Center in the task bar. From the Start Menu Select Start Progr

### Accessing the NI Switch Health Center

You can access the NI Switch Health Center from within Measurement & Automation
 Explorer (MAX) or from the Start menu.

#### From MAX

- Right-click on a resource and select NI Switch Health
 Center , or

- Select a resource and click NI Switch Health Center in
 the task bar.

#### From the Start Menu

Select Start»Programs»National Instruments»NI-SWITCH»NI Switch Health Center.

Parent topic:

NI Switch Health Center Help

Related concepts:

- Testing Relays with the NI Switch Health Center
- About the NI Switch Health Center

<!--NI_TOPIC bundle=ni-switch path=adding-additional-settling-time.html language=enus -->
## TOPIC 00003: Adding Additional Settling Time

- bundle_id: `ni-switch`
- source_path: `adding-additional-settling-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/adding-additional-settling-time.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some applications, such as high temperature or vibration measurements, may require additional settling time to acquire accurate measurements. Setting the Settling Time You can change the default settling time of a switch by using the niSwitch Property Node or the niSwitch_SetAttributeViReal64 functi

### Adding Additional Settling Time

Some applications, such as high temperature or vibration measurements, may require
 additional settling time to acquire accurate measurements.

#### Setting the Settling Time

You can change the default settling time of a switch by using the niSwitch Property
 Node
 or the
 niSwitch_SetAttributeViReal64
 function and NISWITCH_ATTR_SETTLING_TIME attribute.

#### In LabVIEW:

1. Add the niSwitch Property
 Node
 to the block diagram.
2. Click the property node and select Module
 Characteristics» Settling
 Time.
3. Right-click the Settling Time property and select
 Change to Write .
4. Right-click the Settling Time property and create a
 constant.
5. Set the constant to the amount of time (in seconds) to wait for settling.

#### In C:

1. Create a new ViSession named switchSession using the
 niswitchinit function.
2. Create a ViReal64 variable named settlingTime and set the
 value to the desired new settling time in seconds.
3. Call the function
 niSwitchCheckErr(niSwitch_SetAttributeViReal64(switchSession,
 VI_NULL, NISWITCH_ATTR_SETTLING_TIME, settlingTime));

Note

#### Checking the Settling Time

You can check the default settling time of a switch by using the niSwitch Property
 Node
 or the
 niSwitch_CheckAttributeViReal64
 function and NISWITCH_ATTR_SETTLING_TIME attribute.

#### In LabVIEW:

1. Add the niSwitch Property
 Node
 to the block diagram.
2. Click the property node and select Module
 Characteristics» Settling
 Time.
3. Right-click the Settling Time property and create an
 indicator.

#### In C:

1. Create a new ViSession named switchSession using the
 niswitchinit function.
2. Create a ViReal64 variable named settlingTime . Its value
 in seconds will be returned in the next step.
3. Call the function
 niSwitchCheckErr(niSwitch_GetAttributeViReal64(switchSession,
 VI_NULL, NISWITCH_ATTR_SETTLING_TIME, &settlingTime));

Parent topic:

Features

Related concepts:

- Settling Time

<!--NI_TOPIC bundle=ni-switch path=arcing.html language=enus -->
## TOPIC 00004: Arcing

- bundle_id: `ni-switch`
- source_path: `arcing.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/arcing.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every switching system has some amount of inductance. When a relay opens a circuit with inductance, an arc occurs across the relay contacts, sometimes causing significant damage. The small mass of the reed relay switch makes the reed more susceptible to damage during arcing. When bouncing, the first

### Arcing

Every switching system has some amount of inductance. When a relay opens a circuit with
 inductance, an arc occurs across the relay contacts, sometimes causing significant
 damage. The small mass of the reed relay switch makes the reed more susceptible to
 damage during arcing.

When bouncing, the first momentary closure initiates current flow through the relay. As
 the contacts open, an arc forms that can melt part of the contact surface. If the
 contacts are still molten when they finally stabilize in the closed position and
 solidify before reopening, a micro-weld can form, permanently closing the relay. The
 spring force of the reeds may not be sufficient to break this weld when the current
 stops flowing through the coil. Such contact welding constitutes end-of-life for the
 relay. The following sequence of figures illustrates a relay bouncing, arcing, and
 welding closed.

#### Relay Closed. Current Flows.

[IMAGE alt='image' src='GUID-E63C4F07-E6A4-4B62-9A68-70C1B7834EB9-a5.gif']

#### Relay Bounces. Arc Melts Contacts.

[IMAGE alt='image' src='GUID-AF52EAC2-52EB-4AD6-A7C0-BFE56877CECC-a5.gif']

#### Relay Closes. Contacts Still Molten.

[IMAGE alt='image' src='GUID-52E4B245-E6E0-403D-B208-A25F01F2254A-a5.gif']

#### Contacts Welded Closed; Spring Force Unable to Break Weld.

[IMAGE alt='image' src='GUID-4D6D9666-9BE1-4A96-B3BE-DA4708D1F93F-a5.gif']

Welding contacts is also possible if you send a large current through relays that are
 already closed. The non-zero contact resistance can heat up and cause the same
 welding phenomenon described above. The following sequence of figures show large
 current welding a relay closed.

#### Relay Closed

[IMAGE alt='image' src='GUID-8B0A4042-C000-48C8-A340-5A475257441C-a5.gif']

#### Large Current Melts Contacts

[IMAGE alt='image' src='GUID-5C910B6E-CBB8-47DF-92A6-BC71989F5F9C-a5.gif']

#### Contacts Welded Closed; Spring Force Unable to Break Weld.

[IMAGE alt='image' src='GUID-27519283-C428-4D44-89CE-A5770B2638F7-a5.gif']

Parent topic:

Reed Relay Protection

Related concepts:

- Reed Relays
- Relay Life

<!--NI_TOPIC bundle=ni-switch path=armature-relays.html language=enus -->
## TOPIC 00005: Armature Relays

- bundle_id: `ni-switch`
- source_path: `armature-relays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/armature-relays.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Armature relays are a type of electromechanical relay made of coils, an armature mechanism, and contacts. When the coil is energized, the induced magnetic field moves the armature. This movement opens or closes the contacts. If your switch module uses armature relays, consider the factors that affec

### Armature Relays

Armature relays are a type of electromechanical relay made of coils, an armature
 mechanism, and contacts. When the coil is energized, the induced magnetic field moves
 the armature. This movement opens or closes the contacts. If your switch module uses
 armature relays, consider the factors that affect relay life. The following figure
 represents an armature relay.

[IMAGE alt='image' src='GUID-B8D21B55-1DE0-42DF-93E6-AF4680C1DB93-a5.gif']

There are two types of armature relays, latching and nonlatching.

#### Nonlatching

A nonlatching relay has an initial position of normally closed (NC). This position is
 maintained by the force of a spring or permanent magnet while no current flows. The
 normally open (NO) contact is maintained by the force of a magnetic field while
 current flows through the coil. When the current stops, the relay reverts to its
 initial NC position.

Nonlatching armature relays are useful in control applications when the switch must
 return to a known state if power is lost. The following figure shows examples of
 nonlatching relays.

[IMAGE alt='image' src='GUID-F2AEE1A5-3DC5-4408-9844-B26E8ABAB623-a5.gif']

#### Latching

A latching relay can have one or two coils. Latching relays have no default position
 and remain in their last position when the drive current stops flowing. While the
 relays themselves may be latching, their reset position in a module is based on the
 control circuitry and software (NI-SWITCH resets all relays on all modules during
 initialize and reset). Latching relays are useful in applications where power
 consumption and dissipation must be limited because, once actuated, the relays
 require no current flow to maintain their position.

In one–coil latching, the direction of current flow determines the position of the
 relay. In two–coil latching, the coil in which the current flows determines the
 position of the armature. The following figure shows a one-coil latching relay.

[IMAGE alt='image' src='GUID-01A4CECD-1A77-4E83-B6E6-C17176D8D448-a5.gif']

The following figure shows a two-coil latching relay.

[IMAGE alt='image' src='GUID-3D0D8072-00C7-4B3D-A5EC-1E897F927779-a5.gif']

#### Related Topics

Electromechanical Relays

Parent topic:

Electromechanical Relays

Related concepts:

- Electromechanical Relays
- Relay Life

<!--NI_TOPIC bundle=ni-switch path=available-5-v-and-12-v-sources.html language=enus -->
## TOPIC 00006: Available 5 V and 12 V Sources

- bundle_id: `ni-switch`
- source_path: `available-5-v-and-12-v-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/available-5-v-and-12-v-sources.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2567 has a 5 V and a 12 V source available to drive relays. The 5 V source, available on pin 58, can provide up to 1.25 A of current. The 12 V source, available on pin 19, can provide 0.50 A of current.

### Available 5 V and 12 V Sources

The NI PXI-2567 has a 5 V and a 12 V source available to drive relays. The 5 V source,
 available on pin 58, can provide up to 1.25 A of current. The 12 V source, available on
 pin 19, can provide 0.50 A of current.

Parent topic:

NI PXI-2567

<!--NI_TOPIC bundle=ni-switch path=bandwidth-and-insertion-loss.html language=enus -->
## TOPIC 00007: Bandwidth and Insertion Loss

- bundle_id: `ni-switch`
- source_path: `bandwidth-and-insertion-loss.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/bandwidth-and-insertion-loss.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal bandwidth is the useful range of signal frequencies for a switch. NI switch modules are specified for frequencies as low as DC, so bandwidth is specified as the maximum recommended signal frequency. In many cases, bandwidth is the highest signal frequency that the switch can maintain <3 dB of

### Bandwidth and Insertion Loss

Signal bandwidth is the useful range of signal frequencies for a switch. NI switch
 modules are specified for frequencies as low as DC, so bandwidth is specified as the
 maximum recommended signal frequency. In many cases, bandwidth is the highest signal
 frequency that the switch can maintain <3 dB of insertion loss. Some RF modules
 specify bandwidths based on reflections (VSWR) instead of insertion loss.

#### Insertion Loss

As a high-frequency signal traverses through a switch module, it is attenuated by
 series resistance, dielectric absorption, and by reflections from impedance
 mismatches. This attenuation is called insertion loss. The amount of signal
 remaining at the output of the switch module is represented as a ratio to the input
 signal in decibels (dB):

Transmitted signal (dB) = 10 log(P<sub>out</sub>/P<sub>in</sub>)

where P<sub>out</sub> is the output power level, and P<sub>in</sub> is the input
 power level.

This ratio can also be expressed in terms of signal voltage:

Transmitted signal (dB) = 20 log(V<sub>out</sub>/V<sub>in</sub>)

Because the switch attenuates the signal, output magnitude is less than input
 magnitude, and the transmitted signal ratio is always <0 dB.

By convention, insertion loss is the ratio of input signal to the
 output signal, in decibels (dB):

Insertion loss (dB) = 10 log(P<sub>in</sub>/P<sub>out</sub>) = -10
 log(P<sub>out</sub>/P<sub>in</sub>)

Insertion loss (dB) = 20 log(V<sub>in</sub>/V<sub>out</sub>) = -20
 log(V<sub>out</sub>/V<sub>in</sub>)

Output magnitude is less than input magnitude, so insertion loss is >0 dB.

The contributing factors of series resistance, dielectric loss, and mismatch
 reflections are frequency dependent and generally result in insertion loss rising
 with signal frequency.

The following figures illustrate single-ended and differential measurements,
 respectively.

|  |
| --- |

|  |
| --- |

#### Bandwidth and Square Waves

If a signal is purely sinusoidal, the bandwidth/insertion loss rating of a switch
 module can be directly applied. For signals that have multiple frequency components,
 like a square wave, the rating may be difficult to apply.

A square wave can be represented using a natural harmonic series, where only the odd
 harmonics are used. The frequency components that make up an ideal square wave are
 infinite.

Square wave (t) = (4/[IMAGE alt='image' src='GUID-A1A22FB3-ADBD-449B-9EA9-3B4A16779ED8-a5.gif'])[sin [IMAGE alt='image' src='GUID-1A2B14EF-E99F-46CF-A863-18A978F9C276-a5.gif']t + (1/3)sin 3[IMAGE alt='image' src='GUID-1A2B14EF-E99F-46CF-A863-18A978F9C276-a5.gif']t
 + (1/5)sin 5[IMAGE alt='image' src='GUID-1A2B14EF-E99F-46CF-A863-18A978F9C276-a5.gif']t + …]

where [IMAGE alt='image' src='GUID-1A2B14EF-E99F-46CF-A863-18A978F9C276-a5.gif'] is frequency in radians per second

A square wave may have a fundamental frequency below the rated bandwidth. However,
 harmonics above the rating may be attenuated by increasing insertion loss.

For example, consider a 2 V peak-to-peak square wave. The square wave can be
 approximated by the summation of multiple harmonic sine waves. Three harmonics are
 shown in the following figure: the fundamental frequency (or first harmonic), the
 fifth, and the 13<sup>th</sup> harmonic.

|  |
| --- |

If the frequency content of a square wave is known, the required
 switch bandwidth can be determined based on the highest harmonic to be passed with
 minimal distortion.

If the frequency content is unknown, the –3 dB point can be
 approximated using the rise time of the harmonic to be preserved. The rise time is
 related to the –3 dB point bandwidth by the following approximation:

3 dB bandwidth (Hz) ≈ 0.35/τ<sub>r</sub>

where τ is the rise time from 10% to 90% of the signal
 amplitude.

The following figure shows this approximation applied to the fifth harmonic of the
 square wave from the previous example:

|  |
| --- |

where τ = 0.0515 s

3 dB bandwidth = 6.79 Hz

To preserve the rise time of the signal, a switch with an insertion loss of 3 dB at
 6.79 Hz minimum should be chosen.

For a square wave, once the fifth or seventh harmonic is reached, the change in the
 rise time is minimal. In the previous example, a switch with an insertion loss of 3
 dB at 7 Hz will be sufficient to pass as a 1 Hz square wave.

Tip

Parent topic:

RF Switching Considerations

Related concepts:

- Voltage Standing Wave Ratio (VSWR)
- Rise Time

<!--NI_TOPIC bundle=ni-switch path=board-layout-and-topology.html language=enus -->
## TOPIC 00008: Board Layout and Topology

- bundle_id: `ni-switch`
- source_path: `board-layout-and-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/board-layout-and-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The open contact capacitance of a single reed relay is often very low (< 1 pF), and cannot store enough energy to damage the relay when switching at the rated voltage. The amount of capacitance across an open relay is directly related to the topology of the switch, the layout of the PCBs, and the lo

### Board Layout and Topology

The open contact capacitance of a single reed relay is often very low (< 1 pF), and
 cannot store enough energy to damage the relay when switching at the rated voltage. The
 amount of capacitance across an open relay is directly related to the topology of the
 switch, the layout of the PCBs, and the loads connected to the switch module.

Topologies with long traces and many connected relays, such as matrices, have higher
 capacitances than simpler topologies.

#### Matrix Topology

[IMAGE alt='image' src='GUID-8FD0A080-E1CD-49BE-B3EE-F7C045EFE498-a5.gif']

#### Multiplexer Topology

[IMAGE alt='image' src='GUID-35AF809E-571E-44EB-8EE5-B92BC099DB51-a5.gif']

#### Equivalent Circuit

[IMAGE alt='image' src='GUID-B2BF859C-1466-4A2F-B879-AE0848A8ED69-a5.gif']

Most instrumentation switches have arrays of relays on a circuit board and a
 connector on one side. All of the traces must route to the connector. Dense,
 parallel routes on a PCB increase capacitance between the traces.

#### Dense Signal Routing Increases Parasitic Capacitance

[IMAGE alt='image' src='GUID-0437DE48-7BBE-4442-8988-135020680D51-a5.gif']

Connecting large capacitive loads directly to the switch terminals or connecting
 multiple terminals together can substantially increase the load capacitance.

#### Capacitive Load Connected to a Multiplexer Channel

[IMAGE alt='image' src='GUID-6A6AE595-9AD9-44BA-9D02-4BE30228D11C-a5.gif']

#### Multiplexer with 2 Inputs Tied Together

[IMAGE alt='image' src='GUID-CDB85E13-3C8B-437B-8339-C4C7633ED240-a5.gif']

#### Equivalent Circuit of 2 Multiplexer Channels Tied Together

[IMAGE alt='image' src='GUID-77F9B69D-7D68-46B3-84FE-FDDC7D8B807E-a5.gif']

Parent topic:

Reed Relay Protection

Related concepts:

- Reed Relays

<!--NI_TOPIC bundle=ni-switch path=bounce.html language=enus -->
## TOPIC 00009: Bounce

- bundle_id: `ni-switch`
- source_path: `bounce.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/bounce.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Armature and reed relay contacts bounce. When closing, the contacts touch momentarily, making and breaking continuity until finally remaining in the closed position. The following figures demonstrate relay bounce. Test System to Measure Relay Bounce Voltage During Relay Bounce

### Bounce

Armature and reed relay contacts bounce. When closing, the contacts touch momentarily,
 making and breaking continuity until finally remaining in the closed position. The
 following figures demonstrate relay bounce.

#### Test System to Measure Relay Bounce

[IMAGE alt='image' src='GUID-52D811B9-4D35-4E11-B19D-755AC51F7636-a5.gif']

#### Voltage During Relay Bounce

|  |
| --- |

Parent topic:

Reed Relay Protection

Related concepts:

- Armature Relays
- Reed Relays

<!--NI_TOPIC bundle=ni-switch path=characteristic-impedance.html language=enus -->
## TOPIC 00010: Characteristic Impedance

- bundle_id: `ni-switch`
- source_path: `characteristic-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/characteristic-impedance.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Characteristic impedance is a transmission line parameter that determines how propagating signals are transmitted or reflected in the line. The following equation and figures represent the components of characteristic impedance. Z 0 = R + j ω L G + j ω C where Z[0] is the characteristic impedance L

### Characteristic Impedance

Characteristic impedance is a transmission line parameter that determines how propagating
 signals are transmitted or reflected in the line. The following equation and figures
 represent the components of characteristic impedance.

Z

0

=

R

+

j

ω

L

G

+

j

ω

C

where

Z<sub>0</sub> is the characteristic impedance

L is the inductance per length

C is the capacitance per length

R is the resistance per length

G is the dielectric conductance per length

[IMAGE alt='image' src='GUID-1A2B14EF-E99F-46CF-A863-18A978F9C276-a5.gif'] is the frequency (radians/s)

If a transmission line is in the system, its characteristic impedance must also match the
 source and the load for maximum power transfer.

In an ideal, lossless transmission line, there is no series resistance or dielectric
 loss, as shown by the following formula:

R

=

0

,

G

=

0

⇒

Z

0

=

L

C

f

r

e

q

u

e

n

c

y

i

n

d

e

p

e

n

d

e

n

t

The following figure shows an electrical system diagram

where

Z<sub>s</sub> is the source impedance

Z<sub>0</sub> is the characteristic impedance of the transmission line

Z<sub>L</sub> is the load impedance

[IMAGE alt='image' src='GUID-998DA93E-7E2A-4CEA-8910-39AB72688395-a5.gif']

The following figure is an electrical representation of a transmission line showing the
 components that affect characteristic impedance.

[IMAGE alt='image' src='GUID-919C0A70-388B-4B7A-B1C6-40C774806875-a5.gif']

Maximum power is transferred from the source to the load when both have the same
 impedance. This is displayed in the following graph which shows the voltage, current,
 and power transferred at various load impedances. The graph assumes no transmission line
 losses and a source impedance of 50 Ohms.

[IMAGE alt='image' src='GUID-038337F2-2C67-46FD-BBCA-2453E61F10F1-a5.gif']

Parent topic:

RF Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=close.html language=enus -->
## TOPIC 00011: Close

- bundle_id: `ni-switch`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/close.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your program finishes, terminate the session with the niSwitch Close VI or the niSwitch_close function. The niSwitch Close VI or the niSwitch_close function is essential for freeing resources, including deallocating memory, destroying threads, and freeing operating system resources. Every sessi

### Close

When your program finishes, terminate the session with the niSwitch
 Close VI or the
 niSwitch_close
 function.

The niSwitch Close VI or the niSwitch_close function is essential for
 freeing resources, including deallocating memory, destroying threads, and freeing
 operating system resources. Every session that you initialize must be closed, even if an
 error occurs during your program. Although NI does not recommend it, when debugging an
 application, you can abort execution before reaching the niSwitch Close VI or the
 niSwitch_close function.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-switch path=cold-junction-temperature-sensor-channel.html language=enus -->
## TOPIC 00012: Cold-Junction Temperature Sensor Channel

- bundle_id: `ni-switch`
- source_path: `cold-junction-temperature-sensor-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/cold-junction-temperature-sensor-channel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2501/2503 has a dedicated temperature sensor channel useful for cold-junction compensation when switching thermocouples. The NI TB-2605 and TBX-68S terminal blocks both have onboard temperature sensors that connect to the dedicated cold-junction sensor channel. You can access the cold-jun

### Cold-Junction Temperature Sensor Channel

The NI PXI-2501/2503 has a dedicated temperature sensor channel useful for cold-junction
 compensation when switching thermocouples. The NI TB-2605 and TBX-68S terminal blocks
 both have onboard temperature sensors that connect to the dedicated cold-junction sensor
 channel. You can access the cold-junction sensor channel by connecting to channel
 cjtemp in the 2-wire 24×1 multiplexer, 2-wire dual 12×1
 multiplexer, and 2-wire quad 6×1 multiplexer topologies.

Parent topic:

NI PXI-2501/2503

Related concepts:

- NI PXI-2501/2503 2-Wire 24×1 Multiplexer Topology
- NI PXI-2501/2503 2-Wire Dual 12×1 Multiplexer Topology
- NI PXI-2501/2503 2-Wire Quad 6×1 Multiplexer Topology

<!--NI_TOPIC bundle=ni-switch path=configuring-a-pxi-pxi-express-switch.html language=enus -->
## TOPIC 00013: Configuring a PXI/PXI Express Switch

- bundle_id: `ni-switch`
- source_path: `configuring-a-pxi-pxi-express-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/configuring-a-pxi-pxi-express-switch.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure an NI PXI/PXI Express switch module, complete the following steps in MAX: Expand Devices and Interfaces. If you are using a remote RT target, expand Remote Systems, find and expand your target, and expand Devices and Interfaces. Right-click the switch device you want to configure. Selec

### Configuring a PXI/PXI Express Switch

To configure an NI PXI/PXI Express switch module, complete the following steps in MAX:

1. Expand Devices and Interfaces . If you are using a remote RT
 target, expand Remote Systems, find and expand your target, and expand
 Devices and Interfaces .
2. Right-click the switch device you want to configure. Select
 Configure .
3. The Terminal Block/Topology tab is selected by default.
 Select the terminal block connected to the switch module from the
 Terminal Block/Accessory listbox.
4. Select the Channels tab.
5. If necessary, designate source channels for the topology selected in the
 Terminal Block/Topology tab. You can set different source
 channels for each topology.
6. If necessary, designate reserved channels for routing. You can reserve different
 channels for routing in each topology.
7. Click OK to accept the changes.

Note

Parent topic:

Configuring Hardware in MAX

Related concepts:

- Setting Source and Configuration Channels

<!--NI_TOPIC bundle=ni-switch path=configuring-hardware-in-max.html language=enus -->
## TOPIC 00014: Configuring Hardware in MAX

- bundle_id: `ni-switch`
- source_path: `configuring-hardware-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/configuring-hardware-in-max.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Measurement & Automation Explorer (MAX) to configure your National Instruments hardware. MAX informs other programs about which devices reside in the system and how they are configured. MAX is installed by default with NI-SWITCH. Launch MAX by navigating to Start»All Programs»National Instrument

### Configuring Hardware in MAX

Use Measurement & Automation Explorer (MAX) to configure your National Instruments
 hardware. MAX informs other programs about which devices reside in the system and how
 they are configured. MAX is installed by default with NI-SWITCH.

1. Launch MAX by navigating to Start»All Programs»National
 Instruments»Measurement & Automation or by clicking the
 Measurement & Automation desktop icon.
2. In the Configuration pane, double-click Devices and
 Interfaces to see the list of installed devices. Installed devices
 appear under the name of their associated chassis.
3. Expand your Chassis tree item. MAX lists all devices
 installed in the chassis. Your default device names may vary.
4. Record the device identifier MAX assigns to the hardware. Use this identifier when
 programming your NI switch.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-switch path=configuring-the-ni-switchblock-in-max.html language=enus -->
## TOPIC 00015: Configuring the NI SwitchBlock in MAX

- bundle_id: `ni-switch`
- source_path: `configuring-the-ni-switchblock-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/configuring-the-ni-switchblock-in-max.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the NI SwitchBlock under Devices and Interfaces in MAX. If you are using an embedded PXI controller, power on the chassis. If you are using a MXI controller, you should power on the chassis before you power on the computer. Launch MAX (Start»All Programs»National Instruments»Measurement &

### Configuring the NI SwitchBlock in MAX

Configure the NI SwitchBlock under Devices and Interfaces in MAX.

1. If you are using an embedded PXI controller, power on the chassis. If you are using
 a MXI controller, you should power on the chassis before you power on the
 computer.
2. Launch MAX ( Start » All
 Programs » National
 Instruments » Measurement &
 Automation ).
3. Expand Devices and Interfaces . If you are using a remote
 real-time (RT) target, expand Remote Systems , find and expand
 the target, and then expand Devices and Interfaces .
4. Verify that the NI SwitchBlock carrier appears under the appropriate chassis. The
 slot number MAX assigns to the NI SwitchBlock carrier is the second PXI slot from
 the left of the carrier. If your chassis does not show up under Devices
 and Interfaces , refer to the chassis documentation to identify the
 chassis. Note If the
 carrier does not appear, press <F5> to refresh the view in MAX. If the
 carrier still does not appear, reinstall the hardware. Refer to NI Technical
 Support at ni.com/support for troubleshooting information if
 the carrier is still not recognized. For more information about using MAX, refer
 to the available help files within MAX.
5. Right-click the carrier and select Configure to launch the
 NI SwitchBlock Configuration Panel as shown in the following figure. [IMAGE alt='image' src='GUID-6971BFEC-329F-44B5-9548-7693CD653C1D-a5.gif']
6. By default, all NI SwitchBlock cards in the carrier appear as single-card devices,
 as shown in the following figure. [IMAGE alt='image' src='GUID-C6690264-614F-4BBF-B8A2-E999A4143215-a5.gif'] To combine or uncombine
 the cards in your carriers, use one or more of the following methods to designate
 which cards compose each device: 
 Note If a device name has not been previously specified in the MAX
 configuration tree, MAX will auto-generate a device name such as
 SwitchBlock1Dev1, where SwitchBlock1 indicates the name of the carrier in which
 the cards that compose the device are installed. 
 Refer to the NI Switches Help for guidelines for creating
 multicard devices. 
 The following figure illustrates the resulting configuration if you select
 Combine All when configuring an NI SwitchBlock
 composed of four different models of cards. 
 [IMAGE alt='image' src='GUID-F2412B18-37C9-417B-9327-A56107C8D950-a5.gif']
  - Select Combine All to combine all NI SwitchBlock
 cards of the same model in the carrier into multicard devices.
  - Select Uncombine All to split all NI SwitchBlock
 cards in the carrier into single-card devices.
  - After cards have been combined, right-click a card and select
 Move To»New Device to create a new device.
  - Drag and drop a card into the desired device to create a multicard device.
  - Select Move To»Device Name to
 create a multicard device, where Device Name 
 indicates the name of the device into which you would like to move the card.
7. When you have completed assigning cards to devices, select OK 
 to update the configuration tree in MAX, or select Cancel to
 revert to the existing configuration. The updated configuration also appears in the
 right pane in MAX.
8. To test the configuration, right-click each of the devices in the carrier under
 Devices and Interfaces in the MAX configuration tree, and
 select Self-Test . After the test, a message indicates either
 successful verification of the configuration or that an error occurred. If an error
 occurs, refer to ni.com/support for troubleshooting
 information.

Parent topic:

NI SwitchBlock Configuration Panel Help

<!--NI_TOPIC bundle=ni-switch path=connection-and-disconnection-list-syntax.html language=enus -->
## TOPIC 00016: Connection and Disconnection List Syntax

- bundle_id: `ni-switch`
- source_path: `connection-and-disconnection-list-syntax.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/connection-and-disconnection-list-syntax.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use connection lists and disconnection lists with niSwitch Connect Channels (Multiple) and niSwitch Disconnect Channels (Multiple) to create strings of one or more switching operation. For lists with multiple operations, commas separate each operation. NI-SWITCH validates the connection and

### Connection and Disconnection List Syntax

You can use connection lists and disconnection lists with niSwitch Connect Channels
 (Multiple)
 and niSwitch Disconnect Channels
 (Multiple)
 to create strings of one or more switching operation. For lists with multiple
 operations, commas separate each operation. NI-SWITCH validates the connection and
 disconnection lists, and aborts execution of the list if errors are returned.

configuration channel

Note

Switching operations can connect and disconnect channels in one of two ways. Refer to the
 following table to determine the switching operation.

| Switching Operations | Syntax | Description |
| --- | --- | --- |
| Specify Endpoints | channel1 -> channel2 | NI-SWITCH searches for an available path between endpoints to connect or disconnect. The two specified channels must be on the same device, and an available path must exist between them. |
| Specify Explicit Path | [channel1 -> channel2 -> channel3] | You define the endpoints and any intermediate channels of the path.* |

Note

*

Tip

#### Connection and Disconnection List Examples

#### Example 1

If you want to create a connection or disconnection list with switching operations
 that specify endpoints and explicit paths, separate the switching operations with
 commas.

Syntax: Operation1, Operation2, Operation3

Example: c0 -> r0, [c1 -> r2 -> c5], r0 -> c4

#### Example 2

If a path exists between channel0, com0, and AB0, you can connect channel0 to AB0 by
 setting the channel type of com0 as a configuration channel.

Syntax: channel1 -> channel2

Example: channel0 -> AB0

#### Example 3

If you want to connect column 1 and column 5 of a matrix, and use row 2 to complete
 the connection, you must set the channel type of row 2 to a configuration channel
 before the connection is made.

Syntax: [channel1 -> channel2 -> channel3]

Example: [c1 -> r2 -> c5]

#### Related Information:

- Scan Lists

- Setting Source and Configuration Channels

Parent topic:

Features

Related concepts:

- Scan Lists
- Setting Source and Configuration Channels

<!--NI_TOPIC bundle=ni-switch path=considerations-for-using-the-labview-real-tim.html language=enus -->
## TOPIC 00017: Considerations for using the LabVIEW Real-Time Module

- bundle_id: `ni-switch`
- source_path: `considerations-for-using-the-labview-real-tim.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/considerations-for-using-the-labview-real-tim.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an NI-SWITCH application in the LabVIEW Real-Time Module, follow the same steps used for developing any application in the LabVIEW Real-Time Module, with the addition of using the NI-SWITCH LabVIEW VIs. Applications running NI-SWITCH in the LabVIEW Real-Time Module on an RT target may b

### Considerations for using the LabVIEW Real-Time Module

Note

#### Hardware Support

NI-SWITCH supports all National Instruments switch modules on RT targets.

#### Unsupported Features

When using NI switch modules with the LabVIEW Real-Time Module, the Switch Soft Front
 Panel is not supported.

#### Related Documentation

- For configuration instructions for remote systems, refer to the MAX
 Remote Systems Help in Measurement & Automation Explorer (MAX)
 by selecting Help»Help Topics»Remote Systems .
- For more information about the LabVIEW Real-Time Module, refer to the
 LabVIEW Real-Time Module Help at
 ni.com/manuals.
- For additional troubleshooting and support information, refer to the LabVIEW
 Real-Time Support main page at
 ni.com/support/labview/real-time.

Parent topic:

Using NI-SWITCH in LabVIEW

<!--NI_TOPIC bundle=ni-switch path=contact-resistance.html language=enus -->
## TOPIC 00018: Contact Resistance

- bundle_id: `ni-switch`
- source_path: `contact-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/contact-resistance.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Contact resistance refers to the DC resistance through one set of closed contacts in a relay.

### Contact Resistance

Contact resistance refers to the DC resistance through one set of closed contacts in a
 relay.

Parent topic:

General Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=creating-an-application-with-ni-switch.html language=enus -->
## TOPIC 00019: Creating an application with NI-SWITCH

- bundle_id: `ni-switch`
- source_path: `creating-an-application-with-ni-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/creating-an-application-with-ni-switch.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book explains how to begin using NI-SWITCH with your application development environment (ADE), lists files to include in your application, and includes special considerations for each ADE. Install NI-SWITCH before you build an application. To build an application, use one of the following AD

### Creating an application with NI-SWITCH

Note

before

To build an application, use one of the following ADEs:

- LabVIEW
- LabWindows/CVI
- Visual C++
- Visual Basic

Parent topic:

Getting Started

Related concepts:

- Using NI-SWITCH in LabVIEW
- Using NI-SWITCH in LabWindows/CVI
- Using NI-SWITCH in Visual C/C++
- Using NI-SWITCH in Visual Basic

<!--NI_TOPIC bundle=ni-switch path=crosstalk.html language=enus -->
## TOPIC 00020: Crosstalk

- bundle_id: `ni-switch`
- source_path: `crosstalk.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/crosstalk.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crosstalk is the amount of signal from one active channel that appears on another active channel. Crosstalk is specified in dB of transmission, according to one of the following equations: Crosstalk (dB) = 10 log (P[out] / P[source]) Crosstalk (dB) = 20 log (V[out] / V[source]) The following figures

### Crosstalk

Crosstalk is the amount of signal from one active channel that appears
 on another active channel. Crosstalk is specified in dB of transmission, according to
 one of the following equations:

Crosstalk (dB) = 10 log (P<sub>out</sub> / P<sub>source</sub>)

Crosstalk (dB) = 20 log (V<sub>out</sub> / V<sub>source</sub>)

The following figures illustrate crosstalk. All channels are assumed to be appropriately
 terminated.

#### Crosstalk on a General Purpose Module

[IMAGE alt='image' src='GUID-4D99FA53-78A4-4AA4-8297-6FD741DD9E11-a5.gif']

#### Crosstalk on a Matrix Module

[IMAGE alt='image' src='GUID-D16FBD85-E40A-4E55-9F5F-550A594FE9A9-a5.gif']

Parent topic:

RF Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=cycle-process.html language=enus -->
## TOPIC 00021: Cycle Process

- bundle_id: `ni-switch`
- source_path: `cycle-process.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/cycle-process.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram represents the process an electromechanical SPDT general-purpose relay performs during a cycle. The following diagram represents the process an electromechanical SPST general-purpose relay performs during a cycle. For certain situations you may need to increase the default sett

### Cycle Process

The following diagram represents the process an electromechanical SPDT general-purpose
 relay performs during a cycle.

[IMAGE alt='image' src='GUID-27F4F8CE-97DA-4883-A8F3-9088D7DA5317-a5.gif']

The following diagram represents the process an electromechanical SPST general-purpose
 relay performs during a cycle.

[IMAGE alt='image' src='GUID-649A1370-BD41-48AA-BA75-1CF10E223469-a5.gif']

For certain situations you may need to increase the default settling time. Refer to
 Adding Additional Settling Time for more information on increasing the default settling
 time.

Parent topic:

Relay Operation

Related concepts:

- Adding Additional Settling Time

<!--NI_TOPIC bundle=ni-switch path=dimensionally-flexible-sparse-matrix.html language=enus -->
## TOPIC 00022: Dimensionally Flexible Sparse Matrix

- bundle_id: `ni-switch`
- source_path: `dimensionally-flexible-sparse-matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/dimensionally-flexible-sparse-matrix.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2593 architecture allows signals to be routed between any channel pair or common pair while maintaining >500 MHz bandwidth and minimizing RF stubs and reflections. The architecture provides more flexibility than traditional sparse matrices because the shape of the matrix is user-defi

### Dimensionally Flexible Sparse Matrix

The NI PXI/PXIe-2593 architecture allows signals to be routed between any channel pair or
 common pair while maintaining >500 MHz bandwidth and minimizing RF stubs and
 reflections. The architecture provides more flexibility than traditional sparse matrices
 because the shape of the matrix is user-defined, and there is no restriction on
 row-to-row or column-to-column connections. For additional information about
 dimensionally flexible sparse matrices, refer to the document, Advanced Signal
 Routing with the NI PXI/PXIe-2593 and NI SCXI-1193 RF Switches at
 ni.com/info
 using the info code ex2qd9.

#### Routing Configuration

[IMAGE alt='image' src='GUID-F502B120-B94E-412B-8B14-19CF8191BB94-a5.gif']

#### Equivalent Representation

[IMAGE alt='image' src='GUID-09D650C3-F490-4CAC-B10E-1E780687C985-a5.gif']

Parent topic:

NI PXI/PXIe-2593

<!--NI_TOPIC bundle=ni-switch path=disabling-digital-filtering.html language=enus -->
## TOPIC 00023: Disabling Digital Filtering

- bundle_id: `ni-switch`
- source_path: `disabling-digital-filtering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/disabling-digital-filtering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital filtering, enabled by default, prevents the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0–7. Some devices used with a switch may only be able to send triggers that are less than 150 ns. For the switch module to recognize these pulse widths, dig

### Disabling Digital Filtering

Digital filtering, enabled by default, prevents the switch module from being triggered by
 pulses that are less than 150 ns on PXI trigger lines 0–7. Some devices used with a
 switch may only be able to send triggers that are less than 150 ns. For the switch
 module to recognize these pulse widths, digital filtering must be disabled.

niSwitch_SetAttributeViBoolean

Caution

1. Add the niSwitch Property
 Node
 to the block diagram.
2. Click the property node and select Module Characteristics»Digital Filter
 Enable .
3. Right-click the Digital Filter Enable property and select
 Change to Write .
4. Right-click the Digital Filter Enable property and create a
 constant.
5. Set the constant to False .

Parent topic:

Features

<!--NI_TOPIC bundle=ni-switch path=electromechanical-relays.html language=enus -->
## TOPIC 00024: Electromechanical Relays

- bundle_id: `ni-switch`
- source_path: `electromechanical-relays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/electromechanical-relays.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI uses the following types of electromechanical relays: Armature Relays Transfer Switches Reed Relays

### Electromechanical Relays

NI uses the following types of electromechanical relays:

- Armature Relays
  - Transfer Switches
- Reed Relays

Parent topic:

Relay Types

Related concepts:

- Armature Relays
- Transfer Switches
- Reed Relays

<!--NI_TOPIC bundle=ni-switch path=environment.html language=enus -->
## TOPIC 00025: Environment

- bundle_id: `ni-switch`
- source_path: `environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/environment.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI switch modules use components whose performance can be adversely affected by operation outside the specified limits. For more information, refer to the Environment section in the specifications document of the device at Related Documentation. For best performance, observe the following recommenda

### Environment

NI switch modules use components whose performance can be adversely affected by operation
 outside the specified limits. For more information, refer to the
 Environment section in the specifications document of the device
 at Related Documentation.

For best performance, observe the following recommendations:

- Operate NI PXI/PXI Express switch modules in a PXI-compliant PXI/PXI Express chassis
 at an ambient temperature between 0 ºC and 55 ºC and at a relative humidity up to
 90%.
- Use a chassis that has a well-designed cooling system. All NI PXI/PXI Express
 chassis meet this requirement. Note To ensure that an NI PXI/PXI
 Express switch device operates at peak performance within the PXI/PXI Express
 chassis, refer to PXI/PXI Express Chassis Recommendations.
- Keep the NI switch device clean and free from contaminants.

Operating in high humidity or dusty conditions may cause increased leakage between
 circuit components and can result in additional errors.

Parent topic:

Integration and System Considerations

Related concepts:

- PXI/PXI Express Chassis Recommendations

<!--NI_TOPIC bundle=ni-switch path=error-and-status-codes.html language=enus -->
## TOPIC 00026: Error and Status Codes

- bundle_id: `ni-switch`
- source_path: `error-and-status-codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/error-and-status-codes.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH Codes Error Code Hexadecimal Code Error and Status Code Description 1073356801 0x3FFA2001 NISWITCH_WARN_PATH_REMAINS Some connections remain after disconnecting. 1073356802 0x3FFA2002 NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS The channels are implicitly connected. -1074130943 0xBFFA1001 NIS

### Error and Status Codes

#### NI-SWITCH Codes

| Error Code | Hexadecimal Code | Error and Status Code | Description |
| --- | --- | --- | --- |
| 1073356801 | 0x3FFA2001 | NISWITCH_WARN_PATH_REMAINS | Some connections remain after disconnecting. |
| 1073356802 | 0x3FFA2002 | NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS | The channels are implicitly connected. |
| -1074130943 | 0xBFFA1001 | NISWITCH_ERROR_TRIGGER_NOT_SOFTWARE | The trigger source is not a software trigger. |
| -1074126847 | 0xBFFA2001 | NISWITCH_ERROR_INVALID_SWITCH_PATH | Invalid path string. |
| -1074126846 | 0xBFFA2002 | NISWITCH_ERROR_INVALID_SCAN_LIST | Invalid Scan List string. |
| -1074126845 | 0xBFFA2003 | NISWITCH_ERROR_RSRC_IN_USE | One of the channels is a configuration channel that is in use or is a common multiplexer channel that is in use. |
| -1074126844 | 0xBFFA2004 | NISWITCH_ERROR_EMPTY_SCAN_LIST | The scan list string is empty. |
| -1074126843 | 0xBFFA2005 | NISWITCH_ERROR_EMPTY_SWITCH_PATH | The path string is empty. |
| -1074126842 | 0xBFFA2006 | NISWITCH_ERROR_SCAN_IN_PROGRESS | The switch module is currently in scanning mode, and the operation cannot be performed at this time. |
| -1074126841 | 0xBFFA2007 | NISWITCH_ERROR_NO_SCAN_IN_PROGRESS | The switch module is not currently in scanning mode, and the operation cannot be performed at this time. |
| -1074126840 | 0xBFFA2008 | NISWITCH_ERROR_NO_SUCH_PATH | No explicit path exists between the two channels. |
| -1074126839 | 0xBFFA2009 | NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL | You cannot make an explicit connection to a configuration channel. |
| -1074126838 | 0xBFFA200A | NISWITCH_ERROR_NOT_A_CONFIGURATION_CHANNEL | One of the non-terminal channels in the path is not a configuration channel. |
| -1074126837 | 0xBFFA200B | NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES | You cannot make a connection between two different sources. |
| -1074126836 | 0xBFFA200C | NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS | An explicit connection between the channels already exists. |
| -1074126835 | 0xBFFA200D | NISWITCH_ERROR_LEG_MISSING_FIRST_CHANNEL | A leg in the path does not begin with a channel name. |
| -1074126834 | 0xBFFA200E | NISWITCH_ERROR_LEG_MISSING_SECOND_CHANNEL | A leg in the path is missing the second channel. |
| -1074126833 | 0xBFFA200F | NISWITCH_ERROR_CHANNEL_DUPLICATED_IN_LEG | The first and second channels in the leg are the same. |
| -1074126832 | 0xBFFA2010 | NISWITCH_ERROR_CHANNEL_DUPLICATED_IN_PATH | A channel name is duplicated in the path string. |
| -1074126831 | 0xBFFA2011 | NISWITCH_ERROR_PATH_NOT_FOUND | No path was found between the two channels. |
| -1074126830 | 0xBFFA2012 | NISWITCH_ERROR_DISCONTINUOUS_PATH | The first channel of a leg in the path is not the same as the second channel in the previous leg. |
| -1074126829 | 0xBFFA2013 | NISWITCH_ERROR_CANNOT_CONNECT_DIRECTLY | The path contains a leg with two channels that cannot be directly connected. |
| -1074126828 | 0xBFFA2014 | NISWITCH_ERROR_CHANNELS_ALREADY_CONNECTED | A leg in the path contains two channels that are already directly connected. |
| -1074126827 | 0xBFFA2015 | NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF | A channel cannot be connected to itself. |
| -1074126826 | 0xBFFA2016 | NISWITCH_ERROR_MAX_TIME_EXCEEDED | Maximum time exceeded before the operation completed. |
| -1074118655 | 0xBFFA4001 | NISWITCH_ERROR_SESSION_ALREADY_OPEN | Another process has already opened a session to this switch module. |
| -1074118654 | 0xBFFA4002 | NISWITCH_ERROR_INVALID_RESOURCE_DESCRIPTOR | Invalid resource name. |
| -1074118653 | 0xBFFA4003 | NISWITCH_ERROR_SCANNING_NOT_SUPPORTED | You have set an attribute or called a function that is only used for scanning, and this switch module does not support scanning (or this module does not support scanning in the current topology). |
| -1074118652 | 0xBFFA4004 | NISWITCH_ERROR_MUST_SPECIFY_MODULE | You have indicated that a non-cabled module should get its trigger from the rear connector, and the niSwitch software could not automatically detect which cabled module to route the trigger from. Be more specific (ie, specify Rear Connector of Module X). |
| -1074118651 | 0xBFFA4005 | NISWITCH_ERROR_MODULE_FIFO_LENGTH_EXCEEDED | The scan list commands exceeds the size of memory on the switch module. |
| -1074118650 | 0xBFFA4006 | NISWITCH_ERROR_HW_COMMUNICATE_TMO | Error communicating with hardware. Internal timeout occurred waiting for hardware response. |
| -1074118649 | 0xBFFA4007 | NISWITCH_ERROR_TTL_BUS_REQUIRED | Expecting trigger or scan advanced bus to be one of the TTL lines (TTL 0-TTL 7). |
| -1074118648 | 0xBFFA4008 | NISWITCH_ERROR_MODULE_IS_BBM_ONLY | This module requires scan mode to be Break Before Make. |
| -1074118647 | 0xBFFA4009 | NISWITCH_ERROR_1127_TTL1_CONFLICT | TTL 1 conflict detected. SCXI 1127 modules constantly use the TTL 1 line. Use a different line, or power down the chassis and remove all 1127 modules from it. |
| -1074118645 | 0xBFFA400B | NISWITCH_ERROR_INVALID_DRIVER_SETUP_STRING | The driver setup string is invalid. |
| -1074118644 | 0xBFFA400C | NISWITCH_ERROR_TOPOLOGY_NOT_SUPPORTED | No legacy device supports the specified topology. Use a different topology, or configure the device under DAQmx and use the DAQmx resource descriptor. |
| -1074118643 | 0xBFFA400D | NISWITCH_ERROR_INVALID_TOPOLOGY | The specified topology string is invalid. |
| -1074118642 | 0xBFFA400E | NISWITCH_ERROR_HARDWARE_UNEXPECTEDLY_RESET | The device was unexpectedly power cycled. Close and re-open the session. |
| -1074118641 | 0xBFFA400F | NISWITCH_ERROR_HANDSHAKING_INITIATION_CONFLICT | The values for Handshaking Initiation and Trigger Input are incompatible. An Immediate Trigger Input is not compatible with Measurement Device Initiated (or DMM Initiated) Handshaking Initiation. |
| -1074118639 | 0xBFFA4011 | NISWITCH_ERROR_DAQMX_DESCRIPTOR_LEGACY_RSC_TYPE | A DAQmx resource descriptor was specified, but the driver setup string specifies a Legacy resource type. |
| -1074118638 | 0xBFFA4012 | NISWITCH_ERROR_AMBIGUOUS_MODEL_CODE | Model code specified in the driver setup string is ambiguous. Multiple switches match the specified model code. |
| -1074118637 | 0xBFFA4013 | NISWITCH_ERROR_TRIGGER_INPUT_NOT_SUPPORTED | The trigger input specified is not supported by the device. |
| -1074118636 | 0xBFFA4014 | NISWITCH_ERROR_INVALID_TERMINALBLOCK_FOR_TOPOLOGY | The configured terminal block is invalid for current topology. |
| -1074118635 | 0xBFFA4015 | NISWITCH_ERROR_CANT_INVERT_WHEN_SOURCE_EQUALS_DEST | Signal cannot be inverted when the signal source equals the destination. |
| -1074118634 | 0xBFFA4016 | NISWITCH_ERROR_CONFLICTING_TRIGGER_ROUTE_EXISTS | Requested trigger route cannot be made because a conflicting trigger route already exists. |
| -1074118633 | 0xBFFA4017 | NISWITCH_ERROR_INVALID_VALUE_FOR_DEVICE | This device does not support the specified value for this attribute or operation. |
| -1074118632 | 0xBFFA4018 | NISWITCH_ERROR_TRIGGER_POLARITY_CONFLICT | Trigger input polarity and scan advanced output polarity must be the same on this particular switch device. |
| -1074118629 | 0xBFFA401B | NISWITCH_ERROR_RESERVATION_ERROR | Reservation error. |
| -1074118628 | 0xBFFA401C | NISWITCH_ERROR_ANALOG_BUS_INVALID | Analog bus invalid |
| -1074118627 | 0xBFFA401D | NISWITCH_ERROR_POWER_LIMIT_EXCEEDED | Power limit exceeded for the switch carrier. |
| -1074118626 | 0xBFFA401E | NISWITCH_ERROR_DEVICE_SELF_TEST_FAILED | Device self-test failed. |
| -1074118625 | 0xBFFA401F | NISWITCH_ERROR_CARD_DETECTED_DOES_NOT_MATCH_EXPECTED_CARD | One or more cards for your NI SwitchBlock device have been inserted and or removed while your system was powered on. This can lead to unexpected behavior. Restart your system. |
| -1074118624 | 0xBFFA4020 | NISWITCH_ERROR_ANALOG_BUS_STATE_INCONSISTENT | An expansion bridge has been inserted or removed while your system is powered on. This can lead to unexpected behavior. Restart your system. |
| -1074118623 | 0xBFFA4021 | NISWITCH_ERROR_FIVE_VOLT_DETECT_FAILED | The 5 V fuse on your NI SwitchBlock carrier is blown. Refer to your documentation for help with replacing the fuse. |
| -1074118622 | 0xBFFA4022 | NISWITCH_ERROR_SLOT_POWER_LIMIT_EXCEEDED | Power limit exceeded for a specific slot in the switch carrier. |
| -1074118621 | 0xBFFA4023 | NISWITCH_ERROR_CANNOT_EXCEED_RELAY_DRIVE_LIMIT | The number of relays attempted to be driven on this device has exceeded the relay drive limit for this device. |
| -1074118620 | 0xBFFA4024 | NISWITCH_ERROR_INVALID_CONNECTION_LIST | Invalid NI-SWITCH connection list. |
| -1074118619 | 0xBFFA4025 | NISWITCH_ERROR_DISCONNECTION_PATH_NOT_SAME_AS_EXISTING_PATH | Disconnection path is not the same as the existing path. |
| -1074118618 | 0xBFFA4026 | NISWITCH_ERROR_INVALID_RELAY_NAME | Specified relay name is invalid for this device. |
| -1074118617 | 0xBFFA4027 | NISWITCH_ERROR_ANALOG_BUS_SHARING_DIFFERENT_WIRE_MODES | Unable to connect channels composed of different wire modes through the analog bus. Disconnect any devices of different wire modes from the analog bus before routing this device through the analog bus. |

Parent topic:

Programming with NI-SWITCH

<!--NI_TOPIC bundle=ni-switch path=error-cases-in-the-ni-switch-health-center.html language=enus -->
## TOPIC 00027: Error Cases in the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `error-cases-in-the-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/error-cases-in-the-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Switch Health Center will stop running and return errors in the following cases. Error message: The test cannot run because the Integrated Relay Test terminals are shorted. This is usually caused by specific combinations of failed relays on a resource. Refer to the NI Switch Health Center Hel

### Error Cases in the NI Switch Health Center

The NI Switch Health Center will stop running and return errors in the following cases.

Error message: The test cannot run because the Integrated Relay Test terminals are
 shorted. This is usually caused by specific combinations of failed relays on a
 resource. Refer to the NI Switch Health Center Help for more information about
 locating the resource that is causing this error.

The NI Switch Health
 Center will not be able to perform the Integrated Relay Test when there are specific
 combinations of relay failures on resource. Complete the following steps to identify
 which resource is causing this error:

1. Shut down the NI PXI system.
2. Remove any resource.
3. Power on the NI PXI system and run the NI Switch Health Center.
4. Repeat steps 1 through 3 until the NI Switch Health Center runs without
 errors.

If the removal of a specific resource allows the NI Switch Health Center to run
 successfully, contact National Instruments to have the resource repaired. If errors
 continue after trying this procedure, contact National Instruments for
 assistance.

Parent topic:

NI Switch Health Center Help

<!--NI_TOPIC bundle=ni-switch path=example-system.html language=enus -->
## TOPIC 00028: Example System

- bundle_id: `ni-switch`
- source_path: `example-system.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/example-system.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates a test system with a capacitance of 200 pF added to simulate cable capacitance. Also, the external load has been identified as the input to a high-impedance DMM. Even the input to the DMM presents a substantial capacitive load. The addition of the cable to connect th

### Example System

The following figure illustrates a test system with a capacitance of 200 pF added to
 simulate cable capacitance. Also, the external load has been identified as the input to
 a high-impedance DMM. Even the input to the DMM presents a substantial capacitive load.
 The addition of the cable to connect the switch to the load increases this load further.
 The total load capacitance is 300 pF.

#### Test System with Protection

[IMAGE alt='image' src='GUID-0C58AC36-105B-4C10-93EE-72F4F104E2A9-a5.gif']

The following table shows lifetime test results for a circuit with no protection and
 for a circuit with 200 [IMAGE alt='image' src='GUID-E9F79B63-C2DD-471D-9D3F-66622AE8BFB9-a5.gif'] of protection
 resistance.

| Rp () | Lifetime (cycles) |
| --- | --- |
| 0 | 160,000 |
| 200 | 1,500,000 |

This example shows nearly a 10-to-1 increase in lifetime when a protective series
 impedance is used to isolate the switch from the capacitive load.

Parent topic:

Reed Relay Protection

<!--NI_TOPIC bundle=ni-switch path=expanding-multiple-ni-switchblock-carriers.html language=enus -->
## TOPIC 00029: Expanding Multiple NI SwitchBlock Carriers

- bundle_id: `ni-switch`
- source_path: `expanding-multiple-ni-switchblock-carriers.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/expanding-multiple-ni-switchblock-carriers.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can connect the analog buses of multiple adjacent NI SwitchBlock carriers with the NI 2806 expansion bridge for the NI SwitchBlock. If you connect multiple carriers with the expansion bridge, you cannot connect to the analog bus on any of the connected carriers until the drivers for all connec

### Expanding Multiple NI SwitchBlock Carriers

Note

niSwitch_RelayControl

The following figure shows where to insert the NI 2806 expansion bridge.

[IMAGE alt='image' src='GUID-F6F5BFEC-5645-49BE-953E-71EFC6C29FAA-a5.gif']

| 1 | NI PXI/PXI Express Chassis |
| --- | --- |
| 2 | NI PXI-2800 Carriers |
| 3 | NI 2806 Expansion Bridge |

NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE

Note

NI Switch Executive
 Help

Parent topic:

Setting Up and Configuring the NI SwitchBlock

<!--NI_TOPIC bundle=ni-switch path=expanding-the-ni-pxi-2530-2530b-matrix-using.html language=enus -->
## TOPIC 00030: Expanding the NI PXI-2530/2530B Matrix Using the NI TB-2632/2632B

- bundle_id: `ni-switch`
- source_path: `expanding-the-ni-pxi-2530-2530b-matrix-using.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/expanding-the-ni-pxi-2530-2530b-matrix-using.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2632/2632B and bare wire to expand the NI PXI-2530/2530B. Getting Started To expand the NI PXI-2530/2530B, you need the following items: Bare wire Two or more NI TB-2632/2632B terminal blocks Two or more NI PXI-2530/2530B switch modules NI TB-2632/2632B Terminal Reference Refer to the

### Expanding the NI PXI-2530/2530B Matrix Using the NI TB-2632/2632B

Use the NI TB-2632/2632B and bare wire to expand the NI PXI-2530/2530B.

#### Getting Started

To expand the NI PXI-2530/2530B, you need the following items:

- Bare wire
- Two or more NI TB-2632/2632B terminal blocks
- Two or more NI PXI-2530/2530B switch modules

#### NI TB-2632/2632B Terminal
 Reference

Refer to the following figure and complete the procedures in either the Expanding the
 NI PXI-2530/2530B Columns or Expanding the NI PXI-2530/2530B Rows section to expand
 the NI PXI-2530/2530B.

[IMAGE alt='image' src='GUID-747C8225-FF41-401B-9133-AC6D5F1C629D-a5.gif']

#### Expanding the NI PXI-2530/2530B Columns

Complete the following steps to expand the columns of an NI PXI-2530/2530B using an
 NI TB-2632/2632B terminal block.

1. Connect one end of the bare wire to a row screw terminal on one
 NI TB-2632/2632B.
2. Connect the other end of the bare wire to the corresponding row screw terminal
 on another NI TB-2632/2632B.
3. (Optional) To expand the columns on the NI PXI-2530/2530B further, attach
 another bare wire to the row screw terminal you accessed in the previous step.
 Connect the other end of the bare wire to the corresponding row screw terminal
 on another NI TB-2632/2632B.
4. Repeat the previous steps for all rows.

#### Expanding the NI PXI-2530/2530B Rows

Complete the following steps to expand the rows of an NI PXI-2530/2530B using an
 NI TB-2632/2632B terminal block.

1. Connect one end of the bare wire to a column screw terminal on one
 NI TB-2632/2632B.
2. Connect the other end of the bare wire to the corresponding column screw
 terminal on another NI TB-2632/2632B.
3. (Optional) To expand the rows on the NI PXI-2530/2530B further, attach another
 bare wire to the column screw terminal you accessed in the previous step.
 Connect the other end of the bare wire to the corresponding column screw
 terminal on another NI TB-2632/2632B.
4. Repeat the previous steps for all columns.

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=expanding-the-ni-pxi-pxie-2529-matrix-using-t.html language=enus -->
## TOPIC 00031: Expanding the NI PXI/PXIe-2529 Matrix Using the NI TB-2636

- bundle_id: `ni-switch`
- source_path: `expanding-the-ni-pxi-pxie-2529-matrix-using-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/expanding-the-ni-pxi-pxie-2529-matrix-using-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2636 and bare wire to expand the NI PXI/PXIe-2529 (NI 2529). Getting Started To expand the NI 2529, you need the following items: Bare wire Two or more NI TB-2636 terminal blocks Two or more NI 2529 switch modules NI TB-2636 Terminal Reference Refer to the following figure and complete

### Expanding the NI PXI/PXIe-2529 Matrix Using the NI TB-2636

Use the NI TB-2636 and bare wire to expand the NI PXI/PXIe-2529 (NI 2529).

#### Getting Started

To expand the NI 2529, you need the following items:

- Bare wire
- Two or more NI TB-2636 terminal blocks
- Two or more NI 2529 switch modules

#### NI TB-2636 Terminal
 Reference

Refer to the following figure and complete the procedures in either the Expanding the
 NI 2529 Columns or Expanding the NI 2529 Rows section to expand the NI 2529.

[IMAGE alt='image' src='GUID-22BB3AA5-4421-47D1-A2B0-F5B75B503861-a5.gif']

#### Expanding the NI 2529 Columns

Complete the following steps to expand the columns of an NI 2529 using an NI TB-2636
 terminal block.

1. Connect one end of the bare wire to a row screw terminal on one NI TB-2636.
2. Connect the other end of the bare wire to the corresponding row screw terminal
 on another NI TB-2636.
3. (Optional) To expand the columns on the NI 2529 further, attach another bare
 wire to the row screw terminal you accessed in the previous step. Connect the
 other end of the bare wire to the corresponding row screw terminal on another
 NI TB-2636.
4. Repeat the previous steps for all rows.

#### Expanding the NI 2529 Rows

Complete the following steps to expand the rows of an NI 2529 using an NI TB-2636
 terminal block.

1. Connect one end of the bare wire to a column screw terminal on one
 NI TB-2636.
2. Connect the other end of the bare wire to the corresponding column screw
 terminal on another NI TB-2636.
3. (Optional) To expand the rows on the NI 2529 further, attach another bare wire
 to the column screw terminal you accessed in the previous step. Connect the
 other end of the bare wire to the corresponding column screw terminal on another
 NI TB-2636.
4. Repeat the previous steps for all columns.

Parent topic:

NI PXI/PXIe-2529

<!--NI_TOPIC bundle=ni-switch path=extended-support-changes.html language=enus -->
## TOPIC 00032: Updates and Changes for NI-SWITCH Extended Support Versions

- bundle_id: `ni-switch`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/extended-support-changes.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-SWITCH versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible change

### Updates and Changes for NI-SWITCH Extended Support Versions

Browse updates and changes made in NI-SWITCH versions
 on extended support.

Note

Release Notes

#### NI-SWITCH 2023
 Q1 Changes

- Added support for LabVIEW 2023 and later.

<!--NI_TOPIC bundle=ni-switch path=fault-insertion-units.html language=enus -->
## TOPIC 00033: Fault Insertion Units

- bundle_id: `ni-switch`
- source_path: `fault-insertion-units.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/fault-insertion-units.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Fault insertion units (FIUs) are designed to insert fault conditions between automated test equipment, such as hardware-in-the-loop (HIL) simulation systems, and devices under test (DUTs). The following figure represents how a FIU would be used in a complete test system. To insert fault conditions,

### Fault Insertion Units

Fault insertion units (FIUs) are designed to insert fault conditions between automated
 test equipment, such as hardware-in-the-loop (HIL) simulation systems, and devices under
 test (DUTs). The following figure represents how a FIU would be used in a complete test
 system.

[IMAGE alt='image' src='GUID-42DA3E83-0308-4259-9A8B-A1428C804EF7-a5.gif']

To insert fault conditions, internal relays are configured to create short-circuit
 connections and open circuits.

Automated test applications commonly use the following fault conditions:

- open circuits
- short to ground or short to power
- pin-to-pin short

FIUs with switchable fault bus inputs can be used to create additional fault conditions,
 such as a pin-to-pin short through a load.

#### No-Fault Operation

In an FIUs no-fault setting, test equipment is directly connected to DUT signal
 lines through the FIU module. The following figure shows a no-fault operation.

[IMAGE alt='image' src='GUID-3D5AB5FB-E338-46FA-BFAD-20CF1339E05C-a5.gif']

#### Open Circuit Faults

In an open circuit or interrupt fault, the signal line between the test application
 and DUT is left open to determine how the DUT behaves after a signal interruption.
 The following figure shows an open circuit or interrupt fault.

[IMAGE alt='image' src='GUID-CBBAE2D7-1E74-4453-BE01-3037CE0B92CB-a5.gif']

#### Short to Ground or Short to Power

To simulate shorts to ground or power, the signal line is connected from an external
 fault line or fault bus to the DUT. The fault buses can be configured to simulate
 power supply lines or system ground. The following figures represent a short to
 ground and short to power.

[IMAGE alt='image' src='GUID-5BB17B9E-9B84-4526-8940-2D93E1EDE1D9-a5.gif']

#### Pin-to-Pin Short

In a pin-to-pin short, the DUT signal line is connected to one or more additional DUT
 signal lines. The following figure shows a pin-to-pin short.

[IMAGE alt='image' src='GUID-F726084D-7A69-486A-940B-89677FD56BFC-a5.gif']

#### Example Pin-to-Pin Short Through a Load Using the NI PXI-2510

The NI PXI-2510 has two fault buses. Each fault bus has four switchable inputs to
 select among multiple fault conditions such as battery voltage (Vbatt), ground
 (GND), and other fault voltage potentials. The non-switchable input to each fault
 bus is intended for monitoring the fault bus with a DMM. The switchable fault bus
 inputs allow for another fault condition: a pin-to-pin short through a load.

The following example shows a pin-to-pin short through a load using the NI
 PXI-2510:

[IMAGE alt='image' src='GUID-B15B3511-6E3B-4684-B66A-0C59EF514EB2-a5.gif']

Parent topic:

Topologies

<!--NI_TOPIC bundle=ni-switch path=features.html language=enus -->
## TOPIC 00034: Features

- bundle_id: `ni-switch`
- source_path: `features.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/features.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This content explains how to program switches for the following features:

### Features

This content explains how to program switches for the following features:

- [Scanning](scanning.html)
- [Adding Additional Settling Time](adding-additional-settling-time.html)
- [Connection and Disconnection List Syntax](connection-and-disconnection-list-syntax.html)
- [Disabling Digital Filtering](disabling-digital-filtering.html)
- [Immediate Operations](immediate-operations.html)
- [Setting Source and Configuration Channels](setting-source-and-configuration-channels.html)
- [Simulating a Switch](simulating-a-switch.html)

<!--NI_TOPIC bundle=ni-switch path=fet-switches.html language=enus -->
## TOPIC 00035: FET Switches

- bundle_id: `ni-switch`
- source_path: `fet-switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/fet-switches.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Field-effect transistor (FET) switches are made of several CMOS transistors. A voltage is applied to the control circuitry, which connects the source (S) and drain (D) of a transistor network (load circuit) as shown in the following figure. There is no additional isolation between the control circui

### FET Switches

Field-effect transistor (FET) switches are made of several CMOS transistors. A voltage is
 applied to the control circuitry, which connects the source (S) and drain (D) of a
 transistor network (load circuit) as shown in the following figure.

[IMAGE alt='image' src='GUID-61D4F910-C702-45CA-8EAF-401530DFF40D-a5.gif']

There is no additional isolation between the control circuitry and the signal path, as
 shown in the following figure. This lack of isolation restricts operation to low
 voltage, but it allows very fast switching speeds.

[IMAGE alt='image' src='GUID-4898F38A-5396-4B0D-9317-EFFAC8BCCFB6-a5.gif']

Parent topic:

Relay Types

<!--NI_TOPIC bundle=ni-switch path=fundamentals.html language=enus -->
## TOPIC 00036: Fundamentals

- bundle_id: `ni-switch`
- source_path: `fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/fundamentals.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains information about the terminology and concepts related to switches and switching applications. Relay Forms Relay Types Topologies N-Wire Switching Modes General Switching Considerations NI SwitchBlock Switching Considerations RF Switching Considerations Scanning

### Fundamentals

This book contains information about the terminology and concepts related to switches and
 switching applications.

- Relay Forms
- Relay Types
- Topologies
- N -Wire Switching Modes
- General Switching Considerations
- NI SwitchBlock Switching Considerations
- RF Switching Considerations
- Scanning

Related concepts:

- Relay Forms
- Relay Types
- Topologies
- N-Wire Switching Modes
- General Switching Considerations
- RF Switching Considerations
- Scanning Fundamentals

<!--NI_TOPIC bundle=ni-switch path=general-purpose-topologies.html language=enus -->
## TOPIC 00037: General-Purpose Topologies

- bundle_id: `ni-switch`
- source_path: `general-purpose-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/general-purpose-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: General-purpose topologies consist of multiple isolated relays. Each channel of a general-purpose switch module can connect one input to one output. They are typically used to power on or power off devices such as motors, fans, and lights or to switch high-voltage or high-current signals. The follow

### General-Purpose Topologies

General-purpose topologies consist of multiple isolated relays. Each channel of a
 general-purpose switch module can connect one input to one output. They are typically
 used to power on or power off devices such as motors, fans, and lights or to switch
 high-voltage or high-current signals.

The following figure shows an example general-purpose topology.

[IMAGE alt='image' src='GUID-849802DC-ACB3-4904-B98C-8376DF57B436-a5.gif']

Parent topic:

Topologies

<!--NI_TOPIC bundle=ni-switch path=general-switching-considerations.html language=enus -->
## TOPIC 00038: General Switching Considerations

- bundle_id: `ni-switch`
- source_path: `general-switching-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/general-switching-considerations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following concepts when developing a switching application.

### General Switching Considerations

Consider the following concepts when developing a switching application.

- [Contact Resistance](contact-resistance.html)
- [Relay Life](relay-life.html)
- [Path Resistance](path-resistance.html)
- [Thermal EMF and Offset Voltage](thermal-emf-and-offset-voltage.html)
- [Relay Operation](relay-operation.html)
- [Switching Inductive Loads](switching-inductive-loads.html)
- [Switching Capacitive Loads](switching-capacitive-loads.html)
- [Switching Capacity](switching-capacity.html)
- [Reed Relay Protection](reed-relay-protection.html)

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=ni-switch path=generating-reports-ni-switch-health-center.html language=enus -->
## TOPIC 00039: Generating Reports with the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `generating-reports-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/generating-reports-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: After completing a relay test for at least one resource, you can generate an HTML report documenting the condition of all the relays. The report includes links to the online model pages for reference. The report also includes PCB diagrams for each card, to identify the physical location of relays th

### Generating Reports with the NI Switch Health Center

After completing a relay test for at least one resource, you can generate an HTML report
 documenting the condition of all the relays. The report includes links to the online
 model pages for reference. The report also includes PCB diagrams for each card, to
 identify the physical location of relays that need replacement.

Complete the following steps to generate a report after each relay test:

1. Click the Report button.
2. In the Save Report dialog box, specify a file name and location for the report
 directory.
3. Click Save . The NI Switch Health Center creates an HTML
 report and supporting files in the directory location you specified.

Parent topic:

NI Switch Health Center Help

<!--NI_TOPIC bundle=ni-switch path=getting-started.html language=enus -->
## TOPIC 00040: Getting Started

- bundle_id: `ni-switch`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/getting-started.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your NI switch device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks: Install the software and hardware Configure the hardware in MAX Connect signals to Switch Terminal Blocks Progra

### Getting Started

To get started using your NI switch device and driver software, refer to the getting
 started guide for your device. The getting started guide explains how to complete the
 following tasks:

- Install the software and hardware
- Configure the hardware in MAX
- Connect signals to Switch Terminal Blocks
- Program the hardware
- Troubleshoot

Tip

Related concepts:

- Creating an application with NI-SWITCH
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=glossary.html language=enus -->
## TOPIC 00041: Glossary

- bundle_id: `ni-switch`
- source_path: `glossary.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/glossary.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefixes Symbol Prefix Value p pico 10 ^-12 n nano 10 ^-9 µ micro 10 ^-6 m milli 10 ^-3 k kilo 10 ^3 M mega 10 ^6 G giga 10 ^9 T tera 10 ^12 Numbers/Symbols nV nanovolts 10^-9 volts µV microvolts 10^-6 volts µΩ microohms 10^-6 ohms mΩ milliohms 10^-3 ohms MΩ megaohms 10^6 ohms pA picoamps 10^-12 amp

### Glossary

#### Prefixes

| Symbol | Prefix | Value |
| --- | --- | --- |
| p | pico | 10 -12 |
| n | nano | 10 -9 |
| µ | micro | 10 -6 |
| m | milli | 10 -3 |
| k | kilo | 10 3 |
| M | mega | 10 6 |
| G | giga | 10 9 |
| T | tera | 10 12 |

#### Numbers/Symbols

| nV | nanovolts | 10-9 volts |
| --- | --- | --- |
| µV | microvolts | 10-6 volts |
| µΩ | microohms | 10-6 ohms |
| mΩ | milliohms | 10-3 ohms |
| MΩ | megaohms | 106 ohms |
| pA | picoamps | 10-12 amperes |
| nA | nanoamps | 10-9 amperes |
| µA | microamps | 10-6 amperes |
| mA | milliamps | 10-3 amperes |

| A |  |
| --- | --- |
| A | amps |
| AC | alternating current |
| AC current | The measurement of the electrical current (in amperes) of AC signals. The measurement is typically made using rms averaging. |
| AC Voltage | A voltage that changes as a function of time. |
| ADE | application development environment—A software environment incorporating the development, debug, and analysis tools for software development. LabVIEW, Measurement Studio, and Visual Studio are examples. |
| American Wire Gauge | AWG—A U.S. standard set of non-ferrous wire conductor sizes. Gauge means the diameter. Non-ferrous includes copper and also aluminum and other materials, but is most frequently applied to copper household electrical wiring and telephone wiring. Typical household wiring is AWG number 12 or 14. Telephone wire is usually 22, 24, or 26. The higher the gauge number, the smaller the diameter and the thinner the wire. Since thicker wire carries more current because it has less electrical resistance over a given length, thicker wire is better for longer distances. For this reason, where extended distance is critical, a company installing a network might prefer telephone wire with the lower-gauge, thicker wire of AWG 24 to AWG 26. AWG is sometimes known as Brown and Sharpe (B&S) Wire Gauge. |
| analog | A signal whose amplitude can have a continuous range of values. |
| analog bus | See NI SwitchBlock analog bus. |
| analog bus sharing | The simultaneous connection of multiple NI SwitchBlock devices to the same analog bus line, enabled using the Analog Bus Sharing Enable property or NISWITCH_ANALOG_BUS_SHARING_ENABLE attribute. |
| API, application programming interface | A standardized set of subroutines or functions along with the parameters that a program can call. A set of functions exported by a library. |
| B |  |
| backplane | Circuit board that installed modules or cards connect to at the back of a chassis or carrier. |
| bandwidth | The range of frequencies present in a signal, or the range of frequencies to which a measuring device can respond. |
| Break-Before-Make | A type of switching contact that is completely disengaged from one terminal before it connects with another terminal. |
| bus, buses | The group of electrical conductors that interconnect individual circuitry in a computer. Typically, a bus is the expansion vehicle to which I/O or other devices are connected. Examples of PC buses are the PCI, AT(ISA), and EISA bus. |
| C |  |
| capacitance | The ability to hold an electrical charge. |
| card | See NI SwitchBlock card. |
| carrier | See NI SwitchBlock carrier. |
| channel | Pathway from a CPU or, on a network, between computers. A channel can also be an input connection to a data acquisition system or to an instrument, such as an oscilloscope or logic analyzer. Pin or wire lead to which you apply or from which you read an analog or digital signal. Analog signals can be single-ended or differential. For digital signals, channels group to form ports. Ports usually consist of either four or eight digital channels. |
| characteristic impedance | A transmission line parameter that determines how propagating signals are transmitted or reflected in the line. |
| CMOS | Complementary-Metal-Oxide Semiconductor |
| cold junction, cold-junction, cold-junction compensation | A method of compensating for inaccuracies in thermocouple circuits. An artificial reference level that compensates for ambient temperature variations in thermocouple measurement circuits. IC temperature sensors are linear and their output is expressed as mV/°C. A 10 mV/°C sensor, for example, outputs 250 mV at 25 °C. Thermistor outputs, however, are nonlinear. Therefore, thermistor output is specified as the voltage range over a defined temperature range (x volts at 50 °C to y volts at 0 °C). |
| cold switching | The process of closing the relay contacts before applying voltage and current, as well as removing voltage and current before opening the contacts. |
| COM | The common terminal of a multiplexer. |
| contact bounce | The intermittent and usually undesired opening of mechanical relay contacts during closure, or closing of contacts during opening. The contact bounce period depends upon the type of relay and varies from .5 ms for small reed relays to 10-20 ms for larger relays. |
| contact life | The maximum number of expected switch or relay closures with a given voltage/current load before failure. |
| contact material | The material of which the contacts of a relay are made. |
| contact potential | A voltage produced between contact terminals due to the temperature gradient across the relay contacts. |
| contact rating | The maximum voltage, current, and power capacities of relay contacts under specified environmental conditions. |
| contact resistance | The electrical resistance across closed contacts. |
| contactor | An electric switch for controlling a motor or other electric device. |
| Controller | An intelligent device (usually involving a CPU) that is capable of controlling other devices. |
| crosspoint switch | An integrated circuit term; a switch that connects the signal on an input bus to one or more output buses. Also referred to as a switch matrix. |
| current | The rate of flow of electric charge measured in amperes. |
| current drive | The ability to supply a given output current. Refer to current sinking. |
| current drive capability | The amount of current a digital or analog output channel is capable of sourcing or sinking while still operating within voltage range specifications. |
| current excitation | The current a DMM can generate to perform a variety of measurements including resistance measurements. |
| current loop | A communications method that transmits data as current flow over relatively long distances and through environments with relatively high noise. |
| current sinking | The ability of a signal generator or output of a DAQ device to dissipate current for analog or digital output signals. Refer to current drive. |
| current sourcing | The ability of a DAQ device or instrument device to supply current for external devices, such as sensors or conditioning units. ICP is one technique for supplying DC current to transducers with built-in amplifiers. |
| D |  |
| DAQ | Data acquisition—The process of collecting and measuring electrical signals from sensors, transducers, and test probes or fixtures and inputting them to a computer for processing. Data acquisition—The process of collecting and measuring the same kinds of electrical signals with A/D and/or DIO devices plugged into a computer, and possibly generating control signals with D/A and/or DIO devices in the same computer. |
| dB | decibel |
| DC | direct current—Although the term speaks of current, many different types of DC measurements are made, including DC voltage, DC current, and DC power. |
| DC coupled | Allowing the transmission of both AC and DC signals. |
| DC current | The electric current of a DC signal. |
| DC gain error | The gain error on the DC component of a signal. This specification is not applicable when the device has AC input coupling. |
| DC offset | The DC voltage or current present on a signal. A typical technique in many instruments is to put the instrument in DC offset calibration mode, where the external signal is removed. Then, the internally generated DC offset signal is measured, and in some cases, stored, and compensated for. |
| DC parametric measurement | The use of Ohm's Law, which states that the current through a conductor is directly proportional to the voltage and inversely proportional to the resistance, to measure one DC characteristic by forcing another. For instance, you can force a current in order to measure terminal voltage, or vice versa. |
| DC voltage | The direct current (non-changing) component of a voltage. In practice, the DC voltage should not change over the period of observation, that is, the measurement time. |
| dielectric constant | The ratio of a capacitance using a given dielectric to the capacitance using a vacuum as a dielectric. |
| differential thermal EMF | the voltage difference between two junctions |
| DIO | digital input/output |
| DMM | digital multimeter—A digital instrument capable of measuring several different fundamental electrical characteristics, most often voltage, resistance, and current. |
| DPDT | double-pole double-throw |
| drive current | the current that flows through the coil of an electromechanical relay to move the armature |
| dry circuit switching | Switching below specified levels of voltage and current to minimize any physical and electrical changes in the contact junction. |
| dry reed relay | A glass enclosed, hermetically sealed, magnetically actuated contact. Typical atmosphere inside the glass enclosure is nitrogen. |
| DUT | device under test |
| E |  |
| E Series | A standard architecture for instrumentation-class, multichannel data acquisition devices. |
| electrical life | The number of switch cycles, under load, before the contact resistance of a relay rises above 1 Ω. |
| electromechanical relay | A type of relay composed of a coil, an armature mechanism, and contacts. |
| EMF | electromotive force—The electrical force present without a load on the circuit. |
| endpoint programming | Programming technique that uses two inputs which are the physical channels that connect together. NI Switch Executive will automatically use of any channels that have been reserved for routing to create this connection. For example, specifying to connect column 0 (c0) to column 1(c1) would be used in endpoint programming. In order for the connection to be made, at least one row (r0), must be configured as reserved for routing. This programming technique is simple regardless of how many modules are added to the system, assuming channels are reserved for routing appropriately. |
| expansion bridge | Accessory for the NI SwitchBlock that connects the analog buses of adjacent carriers so that the carriers share a single analog bus. |
| explicit path programming | Programming technique that requires every individual path to be explicitly closed. NI Switch Executive will not automatically route through devices or channels that have been reserved for routing. For example, to connect column 0 (c0) to column 1 (c1), two separate connection paths must be defined: one to connect column 0 to a row, and the second to connect the row to column 1. Explicit path programming becomes more complicated as additional modules are required in the route. |
| F |  |
| fault | In a component or circuit, a defect such as a short-circuit to ground or an unintended open circuit. Also, a failure condition caused by such a defect. |
| fault insertion unit | A device designed to insert fault conditions. |
| FET switch | Field-Effect Transistor—A type of relay composed of several CMOS transistors. A voltage applied to the control circuitry connects the source and drain of a transistor network. |
| form | A classification of relays categorized by the number of poles, throws, and default position of the relay. |
| FIU | fault insertion unit |
| frequency | The basic unit of rate, measured in events or oscillations per second using a frequency counter or spectrum analyzer. Frequency is the reciprocal of the period of a signal. |
| front panel | The interactive user interface of a VI. Modeled after the front panel of physical instruments, it is composed of switches, slides, meters, graphs, charts, gauges, LEDs, and other controls and indicators. The physical front panel of an instrument or other hardware |
| Functions palette | The LabVIEW palette containing block diagram structures, constants, communication features, and VIs. |
| fundamental | The component of a periodic wave whose frequency, f0, is the greatest common divisor of the harmonic frequencies, and the inverse of the wave period T. |
| G |  |
| general-purpose topology | A topology composed of multiple isolated relays used to connect one input to one output. |
| GND | ground |
| ground | A pin. An electrically neutral wire that has the same potential as the surrounding earth. Normally, a noncurrent-carrying circuit intended for safety. A common reference point for an electrical system. |
| H |  |
| handshaking | A type of scanning similar to synchronous scanning except that the switch sends a digital pulse back to the other device after each scan list entry has been executed. |
| harmonic | Pertaining to whole-number multiples of the fundamental frequency of a sound or signal. |
| HIL | hardware-in-the-loop |
| hot switching | The process of closing the relay contacts after applying voltage and current, as well as applying voltage and current before opening the contacts. |
| HVAB | high-voltage analog bus |
| I |  |
| I/O | input/output—Transfer of data to/from a computer system involving communications channels, operator interface devices, and/or data acquisition and control interfaces. |
| impedance | The electrical characteristic of a circuit expressed in ohms and/or capacitance/inductance. resistance |
| inductance | The characteristic of a coil that generates a voltage due to changes in the current. An inductor creates a voltage that is the derivate of the current, while a capacitor creates a voltage that is the integral of the current. |
| inrush current | The peak instantaneous current drawn by a circuit or device when first turned on. |
| insertion loss | The attenuation of signals due to the impedance when passing the signals through a switching module or system. Specified as a decibel value (dB) over a frequency range. |
| integrated relay test | Integrated feature for NI SwitchBlock that verifies the proper operation of each individual relay. |
| isolation voltage | The voltage that an isolated circuit can normally withstand, usually specified from input to input and/or from any input to the amplifier output, or to the computer bus. |
| L |  |
| LabVIEW | Laboratory Virtual Instrument Engineering Workbench—A program development application based on the programming language G and used commonly for test and measurement purposes. |
| latching | The ability to keep a relay contact in its current state if power is removed. |
| latching relay | A type of electromechanical relay without a default position that remains in its last position when the drive current stops flowing. |
| LED | light-emitting diode |
| load impedance | Resistance, capacitance, and (often) inductance presented by a load to an output amplifier. The recommended load impedance is the minimum resistance and maximum capacitance that the circuitry connected to the analog output should have. |
| load regulation | The ability of a power supply to keep its output voltage or current at a constant value with a changing output load. |
| LVDS | low voltage differential signaling. A low-noise, low-power, low-amplitude method for high-speed digital data transfer. |
| M |  |
| make-before-break | Breaking and completing two paths simultaneously. |
| matrix | A topology in which you can connect multiple inputs to multiple outputs organized as columns and rows. |
| MAX | Measurement & Automation Explorer—A controlled, centralized configuration environment that allows you to configure all of your NI devices. |
| Measurement Category | The following is a description of measurement categories: Measurement Category I is for measurements performed on circuits not directly connected to MAINS 1 . This category includes signals such as voltages on a printed wire board (PWB) on the secondary of an isolation transformer. Measurement Category II is for measurements performed on circuits directly connected to the low-voltage installation. This category refers to local-level distribution such as that provided by a standard wall outlet. Measurement Category III is for measurements performed in the building installation. This category is a distribution level referring to hardwired equipment that does not rely on standard building insulation. Measurement Category IV is for measurements performed at the source of the low-voltage (<1,000 V) installation. |
| mechanical life | The number of switch cycles before the contact resistance of a relay rises above 1 Ω. |
| minimum switch load | In hot switching, the minimum power required to sufficiently close and maintain connection between electromechanical relay contacts. |
| MOSFET | Metal-Oxide-Semiconductor Field-Effect Transistor |
| multicard device | NI SwitchBlock device composed of two or more cards. |
| multiplex | To assign more than one signal to a channel. |
| multiplexer | A topology in which you can connect one input to multiple outputs or one output to multiple inputs. |
| mux | synonym for multiplexer |
| N |  |
| NC | normally closed |
| NI SwitchBlock | High-density expandable switch carrier and interconnectable cards that enable greater switching capacity per slot than standalone PXI switch modules. The NI SwitchBlock operates within a PXI chassis or, when connected to a PXI peripheral slot or a PXI Express hybrid peripheral slot, within a PXI Express chassis. |
| NI SwitchBlock analog bus | A shared set of traces on the carrier backplane used to internally route connections between cards in the carrier. This bus is shared across multiple carriers when the carriers are connected using the NI 2806 expansion bridge. |
| NI SwitchBlock analog bus line | A single trace of the analog bus on an NI SwitchBlock carrier. See NI SwitchBlock analog bus. |
| NI SwitchBlock card | High-density relay card that can be combined with other NI SwitchBlock cards in software to operate as a single device. |
| NI SwitchBlock carrier | Subchassis that operates within a PXI/PXI Express chassis and holds interconnectable NI SwitchBlock cards. |
| NI SwitchBlock device | One or more cards configured in software to function as a single device. |
| NO | normally open |
| nonlatching relay | A type of electromechanical relay with an initial position of normally closed maintained by the force of a spring or permanent magnet while no drive current flows. |
| O |  |
| overcurrent | A current above the optimum, operational, or rated current. |
| overtemperature | A temperature above that at which a component, circuit, device, or system is rated. |
| P |  |
| path | The route a signal follows through the switch from input terminal to output terminal. |
| path resistance | The resistance of a complete signal path from source to destination. This includes resistance of wiring, switching, and input and output connectors. |
| PCB | printed circuit board |
| power consumption limit | Maximum amount of power that a module or carrier can draw from a chassis, or that a card can draw from a carrier, without damaging the NI switch products. |
| power dissipation limit | Maximum amount of power that can be lost as heat from signals or from power consumed from the backplane without damaging the NI switch products. |
| power limits | Maximum amount of power, including power consumption and power dissipation, that can route through a module, carrier or carrier slot without damaging the NI switch products. |
| PXI | PCI eXtensions for Instrumentation—A modular, computer-based instrumentation platform. |
| PXI Express | PCI Express eXtensions for Instrumentation—The PXI implementation of PCI Express, a scalable full-simplex serial bus standard that operates at 2.5 Gbps and offers both asynchronous and isochronous data transfers. |
| PXI Express-compatible module | A modified PXI module that is compatible with existing PXI chassis slots and PXI hybrid chassis slots. PXI Express-compatible modules preserve hardware and software compatibility, with the exception of local bus features. |
| R |  |
| R-C time constant | Time required to charge a capacitor to 63.2 percent of its maximum voltage. |
| reed relay | A type of relay composed of two overlapping ferromagnetic blades hermetically sealed within a gas capsule that is filled with an inert gas. |
| relay | An electrically activated mechanical device that opens and closes electrical contacts. |
| resource | Term that can refer to any of the following: NI SwitchBlock carrier, NI SwitchBlock card, PXI/PXI Express card. |
| resistance | The resistance to the flow of electric current. One ohm (Ω) is the resistance through which one volt of electric force causes one ampere to flow. |
| RF | radio frequency—Refers to frequencies below the infrared range. |
| RF multiplexer | A switch capable of selecting one of many RF channels. |
| rise time | The time for a signal to transition from 10% to 90% of the maximum signal amplitude. |
| S |  |
| safety interlock | Safety feature that prevents the front connector of an installed NI SwitchBlock card from exposing high-voltage signals when disconnected from accessories. |
| scan | The process of cycling through a predefined scan list to when and how to make or break connections. |
| scan list | A string composed of channel names and characters that define connections, disconnections, triggering, and timing of the scan. |
| scan rate | The number of relay cycles that can be performed in a given time frame. Applicable when using a scan list. The scan rate specifies the frequency of the following actions (initial state - ch0 is connected to com0): Obtain trigger input, disconnect ch0 from com0, and wait for debounce. Connect ch0 to com0, wait for debounce, send scan advanced signal, and wait for trigger input. |
| Seebeck coefficients | Temperature coefficients of specific metal-to-metal junctions. |
| Seebeck voltage | A property of dissimilar materials to develop a voltage offset across their junction, proportional to the temperature gradient across said junction, resulting in a current if there is a complete electrical path between the materials. For switching, the Seebeck effect can become an issue when performing low level signal measurements. |
| sense | The channel of a DMM used to measure the voltage drop across a resistance in a 4-wire measurement. |
| settling time | The time required for a signal to reach a steady state after sending an actuation command to the relay. |
| shared analog bus line | An analog bus line that multiple NI SwitchBlock devices connect to simultaneously. See analog bus sharing. |
| short | Short-circuit. A low-resistance connection which is established between two points in a circuit, bypassing any paths with higher resistance. For example, such a connection between the conductors of a transmission line. An intentional short (such as a short-circuit fault condition) rarely causes damage, but an accidental or otherwise unintentional short between transmission lines or power rails at different voltage potentials can often cause damage due to excessive current flow. |
| single-card device | NI SwitchBlock device composed of one card. |
| software trigger scanning | A type of scanning where the scan list advances at every call of niSwitch Send Software Trigger. |
| solid-state relay | A type of relay incorporating an LED to control the gate of a photo-sensitive MOSFET. |
| SPDT | single-pole double-throw |
| SPST | single-pole single-throw |
| SSR | solid-state relay |
| stub | Portion of trace attached to a signal path that degrades the signal. |
| switch | A device for routing signals between two points. |
| switching capacity | The maximum current and voltage that a relay is specified to handle. |
| switching current | The maximum rated current that can flow through the switch as it makes or breaks a contact. |
| switching time (speed) | The time necessary for a switch to actuate and settle to a known state. |
| switching voltage | The maximum signal voltage that the switch module can safely maintain. |
| synchronous scanning | A type of scanning where the scan list advances after the switch receives a digital pulse from another device. |
| T |  |
| terminal | Named location where a signal is either produced (generated) or consumed (acquired). |
| terminal block | A group of several terminals, intended for interconnection of circuits, mounted on a solid insulating block. |
| thermal EMF | The voltage created by the junction of dissimilar metals that increases and decreases with the rise and fall of the ambient temperature. |
| topology | Organizational representation of the channels and relays in a switch module. |
| transistor | A device used to amplify a signal or open and close a circuit. |
| V |  |
| VA | volt-ampere—A measurement of power. The volt-ampere rating is sometimes used if the rated equipment has significant phase shift between the current and voltage. Hence, the volt-ampere rating gives a power rating that ignores this phase shift. |
| Vbatt | battery voltage |
| VI | virtual instrument |
| voltage | the electromotive force |
| voltage standing wave ratio | The measure of signal reflection in a propagating signal. |
| VSWR | voltage standing wave ratio |

<!--NI_TOPIC bundle=ni-switch path=handshaking.html language=enus -->
## TOPIC 00042: Handshaking

- bundle_id: `ni-switch`
- source_path: `handshaking.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/handshaking.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Handshaking allows the DMM and switch to take measurements without controller interaction. The controller periodically acquires data from the DMM at a user-specified interval. Handshaking frees the controller for other tasks and takes measurements faster than immediate operations mode. The handshaki

### Handshaking

Handshaking allows the DMM and switch to take measurements without controller
 interaction. The controller periodically acquires data from the DMM at a user-specified
 interval. Handshaking frees the controller for other tasks and takes measurements faster
 than immediate operations mode. The handshaking trigger is sent from both DMM to switch
 and switch to DMM. This differs from synchronous mode, in which only one trigger is sent
 from the DMM to switch. Scanning is faster in handshaking mode; therefore, handshaking
 is recommended over synchronous mode when using NI products.

Multiple Point
 Acquisitions

NI Digital Multimeters Help

ni.com/manuals

Note

[IMAGE alt='image' src='GUID-82BAEB58-74F9-4FB8-BCD9-4E0DE662672B-a5.gif']

The following figure shows a handshaking timing diagram.

[IMAGE alt='image' src='GUID-6B668436-C0CE-4DB7-AE09-0DA8C06411A9-a5.gif']

where

M = measurement

WFT = wait for trigger

S&S = switch and settle

Parent topic:

Scanning Fundamentals

Related concepts:

- Immediate Operations
- Synchronous Scanning

<!--NI_TOPIC bundle=ni-switch path=immediate-operations.html language=enus -->
## TOPIC 00043: Immediate Operations

- bundle_id: `ni-switch`
- source_path: `immediate-operations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/immediate-operations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following VIs perform immediate operations: niSwitch Connect Channels (Single) niSwitch Connect Channels (Multiple) niSwitch Disconnect Channels (Single) niSwitch Disconnect Channels (Multiple) niSwitch Disconnect All Channels niSwitch Relay Control The following functions perform immediate oper

### Immediate Operations

The following VIs perform immediate operations:

- niSwitch Connect Channels
 (Single)
- niSwitch Connect Channels
 (Multiple)
- niSwitch Disconnect Channels
 (Single)
- niSwitch Disconnect Channels
 (Multiple)
- niSwitch Disconnect All
 Channels
- niSwitch Relay
 Control

The following functions perform immediate operations:

- niSwitch_Connect
- niSwitch_ConnectMultiple
- niSwitch_Disconnect
- niSwitch_DisconnectMultiple
- niSwitch_DisconnectAll
- niSwitch_RelayControl

When you use the immediate functions, NI-SWITCH determines if the path is valid and
 actuates the appropriate relays to make connecting and disconnecting channels easy for
 you.

niSwitch_InitWithTopology

niSwitch_CanConnect

Note

#### Connecting Channels

To connect channels, complete the following steps:

1. Run the niSwitch Connect Channels
 (Single)
 VI or the
 niSwitch_Connect 
 function.
2. Set Channel 1 to one endpoint of the path you want to
 create.
3. Set Channel 2 to the other endpoint of the path you want
 to create.

#### Connecting Multiple Channels

To connect multiple channels, complete the following steps:

1. Run the niSwitch Connect Channels
 (Multiple)
 VI or the
 niSwitch_ConnectMultiple 
 function.
2. Set the connection list to the paths you want to create.
 Use Connection and Disconnection List Syntax for valid connection list syntax
 and examples.
3. Separate multiple operations with commas.

#### Disconnecting Channels

To disconnect channels, complete the following steps:

1. Run the niSwitch Disconnect Channels
 (Single)
 VI or the
 niSwitch_Disconnect 
 function.
2. Set Channel 1 to one endpoint of the path you want to
 break.
3. Set Channel 2 to the other endpoint of the path you want
 to break.

#### Disconnecting Multiple Channels

To disconnect multiple channels, complete the following steps:

1. Run the niSwitch Disconnect Channels
 (Multiple)
 VI or the
 niSwitch_DisconnectMultiple 
 function.
2. Set the disconnection list to the paths you want to
 break. Use Connection and Disconnection List Syntax for valid disconnection list
 syntax and examples.
3. Separate multiple operations with commas.

#### Disconnecting All Channels

To disconnect all channels, run the niSwitch Disconnect All
 Channels
 VI or the
 niSwitch_DisconnectAll
 function.

#### Individual Relay Control

Caution

To control individual relays, complete the following steps:

1. Run the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl 
 function.
2. Set Relay Name to the name of the relay you want to
 control. Refer to the hardware diagram of the switch for valid relay names.
3. Set Relay Action to Open or
 Close .
4. Run the niSwitch
 Close
 VI or the
 niSwitch_close 
 function to end the session.

Parent topic:

Features

Related concepts:

- Setting Source and Configuration Channels
- Connection and Disconnection List Syntax
- Topologies

<!--NI_TOPIC bundle=ni-switch path=initialization.html language=enus -->
## TOPIC 00044: Initialization

- bundle_id: `ni-switch`
- source_path: `initialization.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/initialization.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: A call to initialize sets the switch to a known state and allows you to simulate the switch and reset the device. Initializing with the niSwitch Initialize With Topology VI or the niSwitch_InitWithTopology function also allows you to define the topology. For any application you write, call the niSwi

### Initialization

A call to initialize sets the switch to a known state and allows you to simulate the
 switch and reset the device. Initializing with the niSwitch Initialize With
 Topology
 VI or the
 niSwitch_InitWithTopology
 function also allows you to define the topology.

For any application you write, call the niSwitch Initialize With
 Topology
 VI or the
 niSwitch_InitWithTopology
 function to establish communication with the switch.

Use the niSwitch Initialize With Topology VI or the
 niSwitch_InitWithTopology function to establish a session with the
 switch and send initialization commands that set the instrument to the state necessary
 for NI-SWITCH operation. The niSwitch Initialize With Topology VI or the
 niSwitch_InitWithTopology function also verifies that NI-SWITCH
 supports the switch, resets the switch to a known state, returns a ViSession handle used
 to identify the instrument in all subsequent NI-SWITCH calls, and allows you to set the
 topology of the switch, including simulation.

The niSwitch Initialize With Topology VI and the
 niSwitch_InitWithTopology function override the topology for the
 switch module you set in Measurement & Automation Explorer (MAX). Refer to the
 NI Switches Getting Started Guide for information on configuring
 your switch module in MAX.

#### Resource Names

To establish a session with the correct switch module, you must pass a resource name
 to the niSwitch Initialize With Topology VI or the
 niSwitch_InitWithTopology function. The syntax of the resource
 name depends on where in MAX you configured your switch module—under
 Devices and Interfaces or PXI
 System.

#### MAX Configuration Under Devices and Interfaces

If you configured the switch module under Devices and
 Interfaces in MAX, the resource name is the string in quotes. For
 example, the resource name of the NI PXI-2576 in the following figure would be
 Dev4. Pass this string to the niSwitch Initialize With Topology
 VI or the niSwitch_InitWithTopology function. You can rename the
 resource name for switch modules configured under Devices and
 Interfaces simply by clicking on the device in MAX and entering a
 new name.

|  |
| --- |

#### Alternative Initialization Methods

You can also open a session to the switch module by calling the niSwitch
 Initialize
 VI or the
 niSwitch_init
 function, or by calling the niSwitch Initialize With
 Options
 VI or the
 niSwitch_InitWithOptions
 function. The niSwitch Initialize VI or the niSwitch_init function
 performs all the functionality of the niSwitch Initialize With Topology VI or the
 niSwitch_InitWithTopology function except that it does
 not set the topology of the switch. Instead, the driver uses
 the topology you set in MAX for the switch module. The niSwitch Initialize VI or the
 niSwitch_init function is available for those interested in
 maintaining IVI-compliance. For more information about IVI, refer to
 ivifoundation.org.

In addition to performing all the functionality of the niSwitch Initialize VI or the
 niSwitch_init function, the niSwitch Initialize With Options VI
 or the niSwitch_InitWithOptions function optionally sets the
 initial state of the switch. With the niSwitch Initialize With Options VI or the
 niSwitch_InitWithOptions function, you can configure the
 topology, range checking, caching, coercion recording, simulation, and status
 reporting. Refer to the option string
 (optionString) parameter of niSwitch Initialize With Options VI
 or the niSwitch_InitWithOptions function.

Once you have initialized the switch, you must configure it.

Parent topic:

Programming Flow

Related concepts:

- Simulating a Switch
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=initializing-with-topology-for-ni-switchblock.html language=enus -->
## TOPIC 00045: Initializing with Topology for NI SwitchBlock Devices

- bundle_id: `ni-switch`
- source_path: `initializing-with-topology-for-ni-switchblock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/initializing-with-topology-for-ni-switchblock.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the topology of the NI SwitchBlock device you created in MAX and one of the VIs or functions described in the following sections to initialize your NI SwitchBlock device with topology. Initializing with Topology in LabVIEW Initializing with Topology in C Initializing with Topology in LabVIEW Ref

### Initializing with Topology for NI SwitchBlock Devices

Use the topology of the NI SwitchBlock device you created in MAX and one of the VIs or
 functions described in the following sections to initialize your NI SwitchBlock device
 with topology.

- Initializing with Topology in LabVIEW
- Initializing with Topology in C

#### Initializing with Topology in LabVIEW

Refer to the following sections for information about initializing an NI SwitchBlock
 device with topology using the niSwitch Initialize With
 Topology VI
 or the niSwitch Initialize With
 Options
 VI.

Note

#### Initializing with the niSwitch Initialize With Topology VI

You can specify the topology of your device using the niSwitch Initialize With
 Topology VI
 by wiring either a constant or a string to the topology name
 parameter. If you wire a constant to the topology name
 parameter, select Configured Topology from the drop-down menu
 for the constant. Configured Topology specifies the last
 topology that was configured for the device in MAX.

[IMAGE alt='image' src='GUID-D12FE7AB-7BB6-42AB-A610-9E3DC904A6F6-a5.gif']

If you would like to explicitly state the device topology in your programming, you
 can wire a string to the topology name parameter instead of
 creating a constant. The following figure shows the topology string wired to the
 niSwitch Initialize With Topology VI for a combination of three NI 2810 cards.

[IMAGE alt='image' src='GUID-44BA7095-24E3-48EB-8CEC-0F9EC785B4D4-a5.gif']

Use the following format to type the topology string for the device you configured in
 MAX.

MODEL(N)/1-Wire
 RxC Matrix

where   MODEL represents the model number, not including the
 letter for the card type, of the NI SwitchBlock cards combined in the device.

N represents the quantity of NI SwitchBlock cards combined in the
 device. The topology string for a single-card device does not contain
 (N).

R represents the number of rows in the topology.

C represents the number of columns in the topology.

You can also find the topology string for your device in MAX. When you select your
 device in the MAX configuration tree, you can find the topology string for your
 device in the Topology column of the item view in MAX.

#### Initializing with the niSwitch Initialize With Options VI

You can specify the topology of your device using the niSwitch Initialize With
 Options
 VI by setting the topology config token, located in the Driver Setup string for the
 option string parameter. You can set the value of the
 topology config token to Configured Topology to specify the last
 topology that was configured for the device in MAX.

[IMAGE alt='image' src='GUID-3B9670ED-C9CA-4DF0-9757-247A9340A356-a5.gif']

If you would like to explicitly state the device topology in your programming, you
 can set the value of the topology config token using the topology string for the
 device in the format described in the Initializing with the niSwitch Initialize With
 Topology VI section of this topic. The following figure shows the topology string
 used with the niSwitch Initialize With Options VI for a combination of three NI 2810
 cards.

[IMAGE alt='image' src='GUID-6051B71C-5716-4DD7-9357-62EA0BFBB356-a5.gif']

#### Initializing with Topology in C

Refer to the following sections for information about initializing an NI SwitchBlock
 device with topology using the
 niSwitch_InitWithTopology
 function and the
 niSwitch_InitWithOptions
 function.

Note

#### Initializing with the niSwitch_InitWithTopology Function

You can specify the topology of your device using the
 niSwitch_InitWithTopology
 function by setting the topology parameter. If you set the
 topology parameter using the #define
 topology name, the only valid value is
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY.

If you would like to explicitly state the device topology in your programming, you
 can set the topology parameter using the topology string for
 the device in the format described in the Initializing with the niSwitch Initialize
 With Topology VI section of this topic.

Note

#### Initializing with the niSwitch_InitWithOptions Function

You can specify the topology of your device using the
 niSwitch_InitWithOptions
 function by setting the topology config token, located in the Driver Setup string
 for the optionString parameter. You can set the value of the
 topology config token to Configured Topology to specify the last
 topology that was configured for the device in MAX.

If you would like to explicitly state the device topology in your programming, you
 can set the value of the topology config token using the topology string for the
 device in the format described in the Initializing with the niSwitch Initialize With
 Topology VI section of this topic.

Note

Parent topic:

NI SwitchBlock Programming Considerations

<!--NI_TOPIC bundle=ni-switch path=inrush-current.html language=enus -->
## TOPIC 00046: Inrush Current

- bundle_id: `ni-switch`
- source_path: `inrush-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/inrush-current.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: As current flows through the relay, power is dissipated in the contacts as represented in the following equation: P=I^2R[contact]+I^2R[arc] where P = power absorbed by relay contacts I = inrush current through the module R[arc] = resistance of the arc that exists between the relay contacts during bo

### Inrush Current

As current flows through the relay, power is dissipated in the contacts as represented in
 the following equation:

P=I<sup>2</sup>R<sub>contact</sub>+I<sup>2</sup>R<sub>arc</sub>

where

P = power absorbed by relay contacts

I = inrush current through the module

R<sub>arc</sub> = resistance of the arc that exists between the relay contacts during
 bounce

R
 <sub>contact</sub> = resistance across the relay contacts

R<sub>arc</sub> dissipates as heat, raising the temperature of the contacts. Inrush
 currents momentarily expose the contacts to very high power levels. The energy
 associated with the inrush current may be sufficient to melt the contact surfaces after
 bouncing and weld the relay contacts closed. Inrush currents usually decrease rapidly to
 the steady state levels. Contact bounce, however, can subject the relay to multiple
 inrushes per activation, causing further damage.

The following figure shows a relay within a switch module connected to a voltage source
 and a load. C<sub>int1</sub>, C<sub>int2</sub> and R<sub>contact</sub> always produce an
 inrush current proportional to the input voltage. The duration of the inrush current
 increases (as does contact heating) with the addition of external capacitance at the
 load. Inrush current flows while load capacitance C<sub>int2</sub> and C<sub>ext</sub>are being charged.

|  |
| --- |

where [IMAGE alt='image' src='GUID-6670F132-4B61-40F5-B402-A35C44F79735-a5.gif'] = time constant

In this figure, C<sub>int 2</sub> + C<sub>external</sub> = C and
 [IMAGE alt='image' src='GUID-6670F132-4B61-40F5-B402-A35C44F79735-a5.gif'] = R<sub>contact</sub>C >
 R<sub>contact</sub>C<sub>int 2</sub>

When the voltage across C<sub>int 1</sub> is not the same as (C<sub>int 2</sub> +
 C<sub>external</sub>), closing the relay causes momentary
 inrush current equal to the voltage difference across the relay, divided by the
 resistance of the relay and associated wiring.

#### Capacitive Load Switching ([IMAGE alt='image' src='GUID-6670F132-4B61-40F5-B402-A35C44F79735-a5.gif']
 =R<sub>contact</sub>C)

|  |
| --- |

To prevent damage to these modules, place a resistor in series with your load as
 detailed in Switching Capacitive Loads .

#### Related Topics

Switching Capacitive Loads

Parent topic:

Reed Relay Protection

Related concepts:

- Bounce
- Switching Capacitive Loads

<!--NI_TOPIC bundle=ni-switch path=installing-the-ni-switchblock.html language=enus -->
## TOPIC 00047: Installing the NI SwitchBlock

- bundle_id: `ni-switch`
- source_path: `installing-the-ni-switchblock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/installing-the-ni-switchblock.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the NI Switches Getting Started Guide for information about installing an NI SwitchBlock carrier or card. Refer to the expansion bridge documentation for information about installing the NI 2806 expansion bridge for the NI SwitchBlock.

### Installing the NI SwitchBlock

Refer to the NI Switches Getting Started Guide for information about
 installing an NI SwitchBlock carrier or card. Refer to the expansion bridge
 documentation for information about installing the NI 2806 expansion bridge for the
 NI SwitchBlock.

Parent topic:

Setting Up and Configuring the NI SwitchBlock

<!--NI_TOPIC bundle=ni-switch path=integration-and-system-considerations.html language=enus -->
## TOPIC 00048: Integration and System Considerations

- bundle_id: `ni-switch`
- source_path: `integration-and-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/integration-and-system-considerations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains information related to integrating NI switch modules with other devices and environments.

### Integration and System Considerations

This book contains information related to integrating NI switch modules with other
 devices and environments.

- [Environment](environment.html)
- [PXI/PXI Express Chassis Recommendations](pxi-pxi-express-chassis-recommendations.html)
- [PXI Express Compatibility](pxi-express-compatibility.html)
- [Protecting NI Switch Products when Switching Inductive Loads](protecting-ni-switch-products-when-switching.html)

<!--NI_TOPIC bundle=ni-switch path=isolation.html language=enus -->
## TOPIC 00049: Isolation

- bundle_id: `ni-switch`
- source_path: `isolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/isolation.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Isolation is the ability to keep a signal on an unused channel from appearing on an active, terminated channel. Isolation is specified in dB of rejection, according to one of the following equations: Isolation (dB) = 10 log (P[source] / P[out]) Isolation (dB) = 20 log (V[source] / V[out]) The follow

### Isolation

Isolation is the ability to keep a signal on an unused channel from
 appearing on an active, terminated channel. Isolation is specified in dB of rejection,
 according to one of the following equations:

Isolation (dB) = 10 log (P<sub>source</sub> / P<sub>out</sub>)

Isolation (dB) = 20 log (V<sub>source</sub> / V<sub>out</sub>)

The following figures illustrate isolation.

#### Open Relay Isolation on a Multiplexer Module

[IMAGE alt='image' src='GUID-E566C54B-3A64-48BD-AC88-9B94EE24AFCE-a5.gif']

#### Open Relay Isolation on a General Purpose Module

[IMAGE alt='image' src='GUID-A5DDAF5E-4D17-40EE-B93A-59F7FB21E729-a5.gif']

#### Channel to Channel Isolation

[IMAGE alt='image' src='GUID-7D0CB7D8-C993-41F2-B55E-8C652AF4CBE5-a5.gif']

Parent topic:

RF Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=matrix-expansion.html language=enus -->
## TOPIC 00050: Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To expand the matrix of a PXI-2501/2503, directly connect wire from one terminal block to the other using the NI TB-2606 terminal block. Each PXI-2501/2503 can operate as a 4×6 matrix. To form a 4×12 matrix, use two PXI-2501/2503 modules and connect all the rows from both TB-2606 terminal blocks. To

### Matrix Expansion

To expand the matrix of a PXI-2501/2503, directly connect wire from one terminal block to
 the other using the NI TB-2606 terminal block. Each PXI-2501/2503 can operate as a 4×6
 matrix. To form a 4×12 matrix, use two PXI-2501/2503 modules and connect all the rows
 from both TB-2606 terminal blocks.

Note

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=matrix.html language=enus -->
## TOPIC 00051: Matrix

- bundle_id: `ni-switch`
- source_path: `matrix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/matrix.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: A matrix is one of the most flexible switching configurations. Unlike a multiplexer, a matrix can connect multiple inputs to multiple outputs organized as columns and rows. You can connect any column to any number of rows and any row to any number of columns. At each intersection of a row and column

### Matrix

A matrix is one of the most flexible switching configurations. Unlike a multiplexer, a
 matrix can connect multiple inputs to multiple outputs organized as columns and rows.
 You can connect any column to any number of rows and any row to any number of columns.
 At each intersection of a row and column, there is a switch. When the switch is closed,
 the row is connected to the column.

Matrix size is often described as M rows by N columns (M × N). The following figure
 illustrates a 1-wire, 2×4 matrix.

[IMAGE alt='image' src='GUID-F303D84F-8907-473F-A399-B7BC123EB997-a5.gif']

#### Related Topics

Multiplexer

Parent topic:

Topologies

Related concepts:

- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=multiple-module-scan-lists.html language=enus -->
## TOPIC 00052: Multiple Module Scan Lists

- bundle_id: `ni-switch`
- source_path: `multiple-module-scan-lists.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiple-module-scan-lists.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following process for populating the scan lists of the switches in the scanning operation using NI-SWITCH. The following example scans four consecutive channels of three switches. Refer to Scan Lists for basic scan list syntax. Scan List for Switch #1 In the scan list of switch #1, enter the

### Multiple Module Scan Lists

Use the following process for populating the scan lists of the switches in the scanning
 operation using NI-SWITCH. The following example scans four consecutive channels of
 three switches. Refer to Scan Lists for basic scan list syntax.

#### Scan List for Switch #1

In the scan list of switch #1, enter the channels that you want to scan followed by
 the number of semicolons ";" equal to the sum of the channels in the other scan
 lists plus one. For the purpose of this example, the total number of semicolons
 after the channel entry is nine. The scan list looks like this:
 ch0:3->com0;;;;;;;;;

The following figure illustrates the scan list for switch #1.

[IMAGE alt='image' src='GUID-1ADC9470-2EA6-4D5A-A35F-C846A01B24B9-a5.gif']

1. Channels of switch #1 to be scanned followed by one semicolon. This entry is the
 same as for scanning a single module.
2. Number of semicolons equal to the number of channels of switch #2 instructs
 switch #1 not to react to the triggers dedicated to switch #2. These semicolons
 are dummy entries corresponding to the channels of switch #2.
3. Number of semicolons equal to the number of channels of switch #3 instructs
 switch #1 not to react to the triggers dedicated to switch #3. These semicolons
 are dummy entries corresponding to the channels of switch #3.

#### Scan List for Switch #2

In the scan list for switch #2, enter the number of semicolons equal to the channels
 in the first scan list, then the channels that you want to scan in switch #2 and the
 number of semicolons equal to the sum of channels in the remaining scan lists plus
 one. For the purpose of this example, the number of semicolons before the channel
 entry is four, the number of semicolons after the channel entry is five. The scan
 list looks like this: ;;;;ch0:3->com0;;;;;

The following figure illustrates the scan list for switch #2.

[IMAGE alt='image' src='GUID-54540682-DACE-4933-8474-B68815A7CE0E-a5.gif']

1. Number of semicolons equal to the number of channels of switch #1 instructs
 switch #2 not to react to the triggers dedicated to switch #1. These semicolons
 are dummy entries corresponding to the channels of switch #1.
2. Channels of switch #2 to be scanned followed by one semicolon. This entry is the
 same as for scanning a single module.
3. Number of semicolons equal to the number of channels switch #3 instructs switch
 #2 not to react to the triggers dedicated to switch #3. These semicolons are
 dummy entries corresponding to the channels of switch #3.

#### Scan List for Switch #3

In the scan list for switch #3, enter the number of semicolons equal to sum of the
 channels in all the previous scan lists, then the channels that you want to scan
 followed by one semicolon. For the purpose of this example, the number of semicolons
 before the channel entry is 8. The scan list looks like this:
 ;;;;;;;;ch0:3->com0;

The following figure illustrates the scan list for switch #3.

[IMAGE alt='image' src='GUID-D9F53299-C25C-4F95-8632-2C866CE3DB7F-a5.gif']

1. Number of semicolons equal to the number of channels of switch #1 instructs
 switch #3 not to react to the triggers dedicated to switch #1. These semicolons
 are dummy entries corresponding to the channels of switch #1.
2. Number of semicolons equal to the number of channels of switch #2 instructs
 switch #3 not to react to the triggers dedicated to switch #2. These semicolons
 are dummy entries corresponding to the channels of switch #2.
3. Channels of switch #3 to be scanned followed by one semicolon. This entry is the
 same as for scanning a single module.

Parent topic:

Multiple Module Scanning

Related concepts:

- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=multiple-module-scanning-handshaking.html language=enus -->
## TOPIC 00053: Multiple Module Scanning - Handshaking

- bundle_id: `ni-switch`
- source_path: `multiple-module-scanning-handshaking.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiple-module-scanning-handshaking.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the trigger topic of the switch module in Devices for possible Trigger Input locations. Setup 3—Using Internal PXI Trigger Lines Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch Setup 3—Using Internal PXI Trigger Lines To handshake with multiple PXI/PXI Express s

### Multiple Module Scanning - Handshaking

Refer to the trigger topic of the switch module in Devices for possible
 Trigger Input locations.

- Setup 3—Using Internal PXI Trigger Lines
- Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch

#### Setup 3—Using Internal PXI Trigger Lines

To handshake with multiple PXI/PXI Express switches, you can use internal PXI trigger
 lines. In this setup, a trigger cable is not needed between the DMM and the PXI/PXI
 Express switches.

[IMAGE alt='image' src='GUID-26537D51-DC17-4DB3-9738-5F64A7A956C7-a5.gif']

1. Open niSwitch Multi Switch Hand Int .
2. Create scan lists according to the process described in Multiple Module Scan
 Lists.
3. Set Trigger Input to the same PXI trigger line for all
 switches. This input line should coincide with the destination of the DMM MC
 signal.
4. Set Scan Advanced Output to the same PXI trigger line for
 all switches. This output must coincide with the trigger source of the DMM.

[IMAGE alt='image' src='GUID-CC54732D-48FD-42DC-9DEF-95BBA92BF4E2-a5.gif']

#### Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Some PXI/PXI Express switches can receive/send triggers from/to the front panel or
 terminal block. This setup uses the AUX trigger cable to trigger the switches.

[IMAGE alt='image' src='GUID-467DD385-CDC0-4E1B-AE5F-F05E271ECB2E-a5.gif']

1. Connect the MC signal from the DMM to the external trigger input terminal on the
 front panel or in the terminal block of one PXI/PXI Express switch.
2. Connect the Ext Trig In signal of the DMM to the Scanner Advanced terminal on
 the front panel or in the terminal block of the same PXI/PXI Express
 switch.
3. Open niSwitch Multi Switch Hand Ext .
4. Create scan lists according to the process described in Multiple Module Scan
 Lists.
5. Add niSwitch Route Trigger Input and niSwitch Route
 Scan Advanced Output before niSwitch Commit of the
 switch where the AUX trigger cable from the DMM is connected.
6. Set Trigger Input Connector to Front
 Connector .
7. Set Scan Advanced Output Connector to Front
 Connector .
8. Set Trigger Input Bus Line to a PXI trigger line.
9. Set Trigger Input of all the switches to the same PXI
 trigger line of Trigger Input Bus Line .
10. Set Scan Advanced Output Bus Line to a different PXI
 trigger line.
11. Set Scan Advanced Output of all the switches to the same
 PXI trigger line of Scan Advanced Output Bus Line .
12. Set Measurement Complete Destination to
 External in the DMM configuration.
13. Set Trigger Source to External in the
 DMM configuration.

[IMAGE alt='image' src='GUID-CFEE3CE1-B1AF-4F57-9A6E-5E70299B1182-a5.gif']

Parent topic:

Multiple Module Scanning

Related concepts:

- Multiple Module Scanning
- Multiple Module Scan Lists

<!--NI_TOPIC bundle=ni-switch path=multiple-module-scanning-synchronous.html language=enus -->
## TOPIC 00054: Multiple Module Scanning - Synchronous

- bundle_id: `ni-switch`
- source_path: `multiple-module-scanning-synchronous.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiple-module-scanning-synchronous.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the trigger topic of the switch module in Devices for possible Trigger Input locations. Setup 1—Using Internal PXI Trigger Lines Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch Setup 1—Using Internal PXI Trigger Lines All PXI/PXI Express switches can receive an

### Multiple Module Scanning - Synchronous

Refer to the trigger topic of the switch module in Devices for possible
 Trigger Input locations.

- Setup 1—Using Internal PXI Trigger Lines
- Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch

#### Setup 1—Using Internal PXI Trigger Lines

All PXI/PXI Express switches can receive an input trigger from PXI trigger lines of
 a PXI/PXI Express chassis. In this setup, no cable is used between the DMM and the
 PXI/PXI Express switches for triggering. The DMM sends its MC signal to the PXI/PXI
 Express switches through a PXI trigger line.

[IMAGE alt='image' src='GUID-4C32E6AF-9C62-4E79-868D-1E94C50AF9B0-a5.gif']

1. Open niSwitch Multi Switch Synch Int .
2. Create scan lists according to the process described in Multiple Module Scan
 Lists.
3. Set Trigger Input to the same PXI trigger line for all
 switches. This input line should coincide with the destination of the DMM MC
 signal.

[IMAGE alt='image' src='GUID-FEF10481-CD73-4BFE-B3BC-BFD64B1A7577-a5.gif']

#### Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Some PXI/PXI Express switches can receive an input trigger from the front panel or
 terminal block. This setup uses the AUX trigger cable to trigger the switches.

[IMAGE alt='image' src='GUID-E0C72E7B-1EE2-49BE-9118-8D614B9079F4-a5.gif']

1. Connect the MC signal from the DMM to the external trigger input terminal on the
 front panel or in the terminal block of one PXI/PXI Express switch.
2. Open niSwitch Multi Switch Sync Ext .
3. Create scan lists according to the process described in Multiple Module Scan
 Lists.
4. Add niSwitch Route Trigger Input to the configuration of the
 switch where the AUX trigger cable from the DMM is connected.
5. Set Trigger Input Connector to Front
 Connector .
6. Set Trigger Input Bus Line to
 TTLn .
7. Set Trigger Input to the same
 TTLn for all switches.
8. Set Measurement Complete Destination to
 External in the DMM configuration.

[IMAGE alt='image' src='GUID-C33239EE-59CF-4C51-9BD8-85B595D30A48-a5.gif']

Parent topic:

Multiple Module Scanning

Related concepts:

- Multiple Module Scanning
- Multiple Module Scan Lists

<!--NI_TOPIC bundle=ni-switch path=multiple-module-scanning.html language=enus -->
## TOPIC 00055: Multiple Module Scanning

- bundle_id: `ni-switch`
- source_path: `multiple-module-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiple-module-scanning.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH supports multiple module scanning for PXI/PXI Express switches in NI-DAQmx and NI-SWITCH. Some devices may not support scanning. Refer to your device book for more information about supported features. NI-DAQmx NI recommends NI-DAQmx for multiple module switch scanning. You can access th

### Multiple Module Scanning

Note

#### NI-DAQmx

NI recommends NI-DAQmx for multiple module switch scanning. You can access the
 NI-DAQmx multiple module switch scanning programming examples at
 <LabVIEW>\examples\DAQmx\Switches. For more information
 about developing a multiple module switch scanning application using NI-DAQmx, refer
 to the document, Multi-module Scanning with National Instruments
 Switches at ni.com/info using the info code
 ex797g.

#### NI-SWITCH

To scan multiple switches using NI-SWITCH, you can write a scan list or use the
 programming examples. When scanning multiple switch modules, you must duplicate the
 NI-SWITCH programming example for each switch you want to scan.

#### Determining the Scanning Setup

The scanning setup is dependent on your hardware and triggering scheme. Based on your
 hardware and triggering scheme, choose one of the following scanning setups:

Tip

niSwitch Multi Switch Synch Int

niSwitch Multi Switch Sync Ext

niSwitch Multi 27_28
 Sync

niSwitch Multi Switch Hand Int

niSwitch Multi Switch Hand Ext

ni.com/support

Example Code

#### PXI/PXI Express Scanning—Synchronous

- Setup 1—Using Internal PXI Trigger Lines
- Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

#### PXI/PXI Express Scanning—Handshaking

- Setup 3—Using Internal PXI Trigger Lines
- Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Parent topic:

Scanning NI Switches with NI Digital Multimeters

Related concepts:

- Multiple Module Scan Lists
- NI-SWITCH Programming Examples
- Multiple Module Scanning - Synchronous
- Multiple Module Scanning - Handshaking

<!--NI_TOPIC bundle=ni-switch path=multiplexer-expansion.html language=enus -->
## TOPIC 00056: Multiplexer Expansion

- bundle_id: `ni-switch`
- source_path: `multiplexer-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiplexer-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you need to multiplex through more channels than the number present on your NI PXI-2501/2503, you can expand the size of the multiplexer. The NI TB-2605 terminal block has two analog bus connectors that allow analog bus sharing between two other NI PXI-2501/2503s. Each NI TB-2605 comes with a plu

### Multiplexer Expansion

If you need to multiplex through more channels than the number present on your NI
 PXI-2501/2503, you can expand the size of the multiplexer. The NI TB-2605 terminal block
 has two analog bus connectors that allow analog bus sharing between two other NI
 PXI-2501/2503s. Each NI TB-2605 comes with a plug to share this analog bus between
 modules.

Refer to the NI PXI-2501/2503 hardware diagrams to see the analog bus relay that connects
 the multiplexer COM lines to an analog bus. This analog bus relay must be closed for
 multiplexer expansion. When this analog bus is shared between NI PXI-2501/2503 modules,
 a single larger multiplexer is formed. For example, connecting two NI PXI-2501/2503
 modules using their analog bus in 2-wire 24×1 multiplexer topology, creates a 2-wire
 48×1 multiplexer.

You can also use the LV6-BAN4 cable to connect a DMM directly to the analog bus that acts
 as the COM of the expanded multiplexer.

#### Related Topics

NI PXI-2501 Hardware Diagram

NI PXI-2503 Hardware Diagram

Parent topic:

NI PXI-2501/2503

Related concepts:

- NI PXI-2501 Hardware Diagram
- NI PXI-2503 Hardware Diagram

<!--NI_TOPIC bundle=ni-switch path=multiplexer.html language=enus -->
## TOPIC 00057: Multiplexer

- bundle_id: `ni-switch`
- source_path: `multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: A multiplexer, or a mux, is a topology in which you can connect one input to multiple outputs or one output to multiple inputs. This topology is often used for scanning when you need to automatically connect a sequence of channels to a common line. The following figure shows a multiplexer composed o

### Multiplexer

A multiplexer, or a mux, is a topology in which you can connect one input to multiple
 outputs or one output to multiple inputs. This topology is often used for scanning when
 you need to automatically connect a sequence of channels to a common line.

The following figure shows a multiplexer composed of form A relays.

[IMAGE alt='image' src='GUID-1AA72330-5ED9-4CA9-9D81-7998AEA5902E-a5.gif']

The following figure shows a multiplexer composed of form C relays.

[IMAGE alt='image' src='GUID-1F8D8411-E99B-4C8E-8B95-80C1FC8AD907-a5.gif']

#### Related Topics

Operation Modes

Parent topic:

Topologies

Related concepts:

- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=n-wire-switching-modes.html language=enus -->
## TOPIC 00058: N-Wire Switching Modes

- bundle_id: `ni-switch`
- source_path: `n-wire-switching-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/n-wire-switching-modes.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI switch modules are capable of switching one, two and/or four wires. 1-Wire In 1-wire mode, you connect the HI leads to the relays and the LO leads to a common connection. All signals are referenced to this common connection. All NI multiplexers can operate in 1-wire mode. The following figure sho

### N-Wire Switching Modes

NI switch modules are capable of switching one, two and/or four wires.

#### 1-Wire

In 1-wire mode, you connect the HI leads to the relays and the LO leads to a common
 connection. All signals are referenced to this common connection. All NI
 multiplexers can operate in 1-wire mode. The following figure shows an example of
 1-wire mode.

[IMAGE alt='image' src='GUID-775C52CB-114A-43AD-A06A-12B0E88C4623-a5.gif']

#### 2-Wire

In 2-wire mode, you connect both positive and negative leads to the terminals of a
 channel. The following figure shows an example of 2-wire mode.

[IMAGE alt='image' src='GUID-2EC6DFD5-3CFC-438E-80B5-C2BC13BEFCC6-a5.gif']

#### 4-Wire

4-wire mode is usually used for 4-wire resistance measurements. One channel (two
 leads) is used for the current excitation and another channel (two leads) is used
 for measuring the voltage drop (sense) across the resistor. The following figure
 shows an example of 4-wire mode.

[IMAGE alt='image' src='GUID-A1B52840-AA56-4BD2-8991-93D5F75DDF4A-a5.gif']

Parent topic:

Fundamentals

Related concepts:

- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=new-features-and-changes.html language=enus -->
## TOPIC 00059: NI-SWITCH New Features and Changes

- bundle_id: `ni-switch`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-SWITCH. Discover what is new in the latest releases of NI-SWITCH.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might incl

### NI-SWITCH
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-SWITCH.

NI-SWITCH

Note

Release Notes

Related information:

- Software and Driver Downloads

<!--NI_TOPIC bundle=ni-switch path=ni-2810-1-wire-4-43-matrix-topology.html language=enus -->
## TOPIC 00060: NI 2810 1-Wire 4×43 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2810-1-wire-4-43-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2810-1-wire-4-43-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2810A/B (NI 2810) in the 1-wire 4×43 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2 is

### NI 2810 1-Wire 4×43 Matrix Topology

The following figure represents the NI 2810A/B (NI 2810) in the 1-wire 4×43 matrix
 topology.

[IMAGE alt='image' src='GUID-E385B618-CA3D-4006-BF52-1A521749DEB6-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI 2810.

[IMAGE alt='image' src='GUID-34793636-4437-44BA-B4B2-79DA68BC0AA2-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2810

<!--NI_TOPIC bundle=ni-switch path=ni-2810-hardware-diagram.html language=enus -->
## TOPIC 00061: NI 2810 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2810-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2810-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2810A/B (NI 2810). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2810 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2810 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-E385B618-CA3D-4006-BF52-1A521749DEB6-a5.gif']

The following table lists relay names for one NI 2810 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0 |
| kCARD1AB1 |
| kCARD1AB2 |
| kCARD1AB3 |
| kCARD1R0C0...kCARD1R0C42 |
| kCARD1R1C0...kCARD1R1C42 |
| kCARD1R2C0...kCARD1R2C42 |
| kCARD1R3C0...kCARD1R3C42 |

Parent topic:

NI 2810

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2810-multicard-topologies.html language=enus -->
## TOPIC 00062: NI 2810 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2810-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2810-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2810 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2810 Multicard Topologies

Note

must

| Number ofNI 2810 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 4×43 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 4×86 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 4×129 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 4×172 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 4×215 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 4×258 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2810

Related concepts:

- NI 2810 1-Wire 4×43 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2810-relay-replacement.html language=enus -->
## TOPIC 00063: NI 2810 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2810-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2810-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2810A/B (NI 2810) uses reed relays. The NI 2810 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2810 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Meder | MS05-BV50980 |
| Safety (Reference Designators K17 and K58) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2810 Relay Map 
 [IMAGE alt='image' src='GUID-4EB9B856-D990-4E83-A509-A81BC5DEC3FE-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K16
 kcard1r0c40
 K170
 kcard1r1c41
 K179
 kcard1r2c42
 K175kcard1ab1
 K25
 kcard1r0c41
 K180
 kcard1r1c42
 K176
 kcard1r3c0
 K1kcard1ab2
 K57
 kcard1r0c42
 K177
 kcard1r2c0
 K2
 kcard1r3c1
 K5kcard1ab3
 K66
 kcard1r1c0
 K3
 kcard1r2c1
 K6
 kcard1r3c2
 K9kcard1r0c0
 K4
 kcard1r1c1
 K7
 kcard1r2c2
 K10
 kcard1r3c3
 K13kcard1r0c1
 K8
 kcard1r1c2
 K11
 kcard1r2c3
 K14
 kcard1r3c4
 K18kcard1r0c2
 K12
 kcard1r1c3
 K15
 kcard1r2c4
 K19
 kcard1r3c5
 K22kcard1r0c3
 K24
 kcard1r1c4
 K20
 kcard1r2c5
 K23
 kcard1r3c6
 K26kcard1r0c4
 K21
 kcard1r1c5
 K32
 kcard1r2c6
 K27
 kcard1r3c7
 K30kcard1r0c5
 K33
 kcard1r1c6
 K28
 kcard1r2c7
 K31
 kcard1r3c8
 K34kcard1r0c6
 K29
 kcard1r1c7
 K40
 kcard1r2c8
 K35
 kcard1r3c9
 K38kcard1r0c7
 K41
 kcard1r1c8
 K36
 kcard1r2c9
 K39
 kcard1r3c10
 K42kcard1r0c8
 K37
 kcard1r1c9
 K48
 kcard1r2c10
 K43
 kcard1r3c11
 K46kcard1r0c9
 K49
 kcard1r1c10
 K44
 kcard1r2c11
 K47
 kcard1r3c12
 K50kcard1r0c10
 K45
 kcard1r1c11
 K55
 kcard1r2c12
 K51
 kcard1r3c13
 K54kcard1r0c11
 K56
 kcard1r1c12
 K52
 kcard1r2c13
 K63
 kcard1r3c14
 K59kcard1r0c12
 K53
 kcard1r1c13
 K64
 kcard1r2c14
 K60
 kcard1r3c15
 K67kcard1r0c13
 K65
 kcard1r1c14
 K61
 kcard1r2c15
 K68
 kcard1r3c16
 K71kcard1r0c14
 K62
 kcard1r1c15
 K69
 kcard1r2c16
 K72
 kcard1r3c17
 K75kcard1r0c15
 K70
 kcard1r1c16
 K73
 kcard1r2c17
 K76
 kcard1r3c18
 K79kcard1r0c16
 K82
 kcard1r1c17
 K77
 kcard1r2c18
 K80
 kcard1r3c19
 K84kcard1r0c17
 K78
 kcard1r1c18
 K81
 kcard1r2c19
 K85
 kcard1r3c20
 K88kcard1r0c18
 K74
 kcard1r1c19
 K86
 kcard1r2c20
 K89
 kcard1r3c21
 K92kcard1r0c19
 K87
 kcard1r1c20
 K90
 kcard1r2c21
 K93
 kcard1r3c22
 K96kcard1r0c20
 K91
 kcard1r1c21
 K94
 kcard1r2c22
 K97
 kcard1r3c23
 K100kcard1r0c21
 K95
 kcard1r1c22
 K98
 kcard1r2c23
 K101
 kcard1r3c24
 K104kcard1r0c22
 K99
 kcard1r1c23
 K102
 kcard1r2c24
 K105
 kcard1r3c25
 K108kcard1r0c23
 K103
 kcard1r1c24
 K106
 kcard1r2c25
 K109
 kcard1r3c26
 K112kcard1r0c24
 K107
 kcard1r1c25
 K110
 kcard1r2c26
 K113
 kcard1r3c27
 K117kcard1r0c25
 K111
 kcard1r1c26
 K114
 kcard1r2c27
 K118
 kcard1r3c28
 K121kcard1r0c26
 K115
 kcard1r1c27
 K119
 kcard1r2c28
 K122
 kcard1r3c29
 K125kcard1r0c27
 K120
 kcard1r1c28
 K123
 kcard1r2c29
 K126
 kcard1r3c30
 K129kcard1r0c28
 K124
 kcard1r1c29
 K127
 kcard1r2c30
 K130
 kcard1r3c31
 K132kcard1r0c29
 K128
 kcard1r1c30
 K131
 kcard1r2c31
 K133
 kcard1r3c32
 K136kcard1r0c30
 K138
 kcard1r1c31
 K134
 kcard1r2c32
 K137
 kcard1r3c33
 K139kcard1r0c31
 K135
 kcard1r1c32
 K144
 kcard1r2c33
 K140
 kcard1r3c34
 K143kcard1r0c32
 K145
 kcard1r1c33
 K141
 kcard1r2c34
 K150
 kcard1r3c35
 K146kcard1r0c33
 K142
 kcard1r1c34
 K151
 kcard1r2c35
 K147
 kcard1r3c36
 K153kcard1r0c34
 K152
 kcard1r1c35
 K148
 kcard1r2c36
 K154
 kcard1r3c37
 K157kcard1r0c35
 K149
 kcard1r1c36
 K155
 kcard1r2c37
 K158
 kcard1r3c38
 K160kcard1r0c36
 K156
 kcard1r1c37
 K159
 kcard1r2c38
 K161
 kcard1r3c39
 K164kcard1r0c37
 K166
 kcard1r1c38
 K162
 kcard1r2c39
 K165
 kcard1r3c40
 K167kcard1r0c38
 K163
 kcard1r1c39
 K172
 kcard1r2c40
 K168
 kcard1r3c41
 K171kcard1r0c39
 K173
 kcard1r1c40
 K169
 kcard1r2c41
 K178
 kcard1r3c42
 K174

#### Replace the Relay

The NI 2810 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2810

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2810.html language=enus -->
## TOPIC 00064: NI 2810

- bundle_id: `ni-switch`
- source_path: `ni-2810.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2810.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2810A/B (NI 2810) is a high-density matrix switch card for the NI SwitchBlock. The NI 2810 is designed for combination with other NI 2810 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2810

The NI 2810A/B (NI 2810) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2810 is designed for combination with other NI 2810 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2810 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×43 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2810 1-Wire 4×43 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2811-1-wire-8-21-matrix-topology.html language=enus -->
## TOPIC 00065: NI 2811 1-Wire 8×21 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2811-1-wire-8-21-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2811-1-wire-8-21-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2811A/B (NI 2811) in the 1-wire 8×21 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r1 and c1, results in the signal connected to CARD1R1 being routed to C1. Pinou

### NI 2811 1-Wire 8×21 Matrix Topology

The following figure represents the NI 2811A/B (NI 2811) in the 1-wire 8×21 matrix
 topology.

[IMAGE alt='image' src='GUID-A519C979-1494-4AC8-B548-1F7245ADFD40-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r1 and c1, results
 in the signal connected to CARD1R1 being routed to C1.

#### Pinout

The following figure identifies the pins for the NI 2811.

[IMAGE alt='image' src='GUID-6BD6023E-8377-4ED2-9918-0AA9696D5CB2-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2811

<!--NI_TOPIC bundle=ni-switch path=ni-2811-hardware-diagram.html language=enus -->
## TOPIC 00066: NI 2811 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2811-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2811-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2811A/B (NI 2811). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2811 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2811 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-A519C979-1494-4AC8-B548-1F7245ADFD40-a5.gif']

The following table lists relay names for one NI 2811 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0 |
| kCARD1AB1 |
| kCARD1AB2 |
| kCARD1AB3 |
| kCARD1AB4 |
| kCARD1AB5 |
| kCARD1AB6 |
| kCARD1AB7 |
| kCARD1R0C0...kCARD1R0C20 |
| kCARD1R1C0...kCARD1R1C20 |
| kCARD1R2C0...kCARD1R2C20 |
| kCARD1R3C0...kCARD1R3C20 |
| kCARD1R4C0...kCARD1R4C20 |
| kCARD1R5C0...kCARD1R5C20 |
| kCARD1R6C0...kCARD1R6C20 |
| kCARD1R7C0...kCARD1R7C20 |

Parent topic:

NI 2811

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2811-multicard-topologies.html language=enus -->
## TOPIC 00067: NI 2811 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2811-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2811-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2811 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2811 Multicard Topologies

Note

must

| Number ofNI 2811 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 8×21 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 8×42 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 8×63 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 8×84 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 8×105 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 8×126 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2811

Related concepts:

- NI 2811 1-Wire 8×21 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2811-relay-replacement.html language=enus -->
## TOPIC 00068: NI 2811 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2811-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2811-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2811A/B (NI 2811) uses reed relays. The NI 2811 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2811 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Meder | MS05-BV50980 |
| Safety (Reference Designators K17, K58, K83, and K116) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2811 Relay Map 
 [IMAGE alt='image' src='GUID-AC44FEEC-2726-4F90-91E1-54CA8A774B3F-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K16
 kcard1r1c15
 K31
 kcard1r3c17
 K97
 kcard1r5c19
 K98kcard1ab1
 K25
 kcard1r1c16
 K39
 kcard1r3c18
 K56
 kcard1r5c20
 K99kcard1ab2
 K49
 kcard1r1c17
 K47
 kcard1r3c19
 K65
 kcard1r6c0
 K146kcard1ab3
 57
 kcard1r1c18
 K24
 kcard1r3c20
 K66
 kcard1r6c1
 K153kcard1ab4
 K82
 kcard1r1c19
 K32
 kcard1r4c0
 K100
 kcard1r6c2
 K160kcard1ab5
 K91
 kcard1r1c20
 K33
 kcard1r4c1
 K108
 kcard1r6c3
 K147kcard1ab6
 K115
 kcard1r2c0
 K50
 kcard1r4c2
 K117
 kcard1r6c4
 K154kcard1ab7
 K124
 kcard1r2c1
 K59
 kcard1r4c3
 K101
 kcard1r6c5
 K161kcard1r0c0
 K1
 kcard1r2c2
 K67
 kcard1r4c4
 K109
 kcard1r6c6
 K148kcard1r0c1
 K9
 kcard1r2c3
 K51
 kcard1r4c5
 K118
 kcard1r6c7
 K155kcard1r0c2
 K18
 kcard1r2c4
 K60
 kcard1r4c6
 K102
 kcard1r6c8
 K162kcard1r0c3
 K2
 kcard1r2c5
 K68
 kcard1r4c7
 K110
 kcard1r6c9
 K149kcard1r0c4
 K10
 kcard1r2c6
 K52
 kcard1r4c8
 K119
 kcard1r6c10
 K156kcard1r0c5
 K19
 kcard1r2c7
 K61
 kcard1r4c9
 K103
 kcard1r6c11
 K157kcard1r0c6
 K3
 kcard1r2c8
 K69
 kcard1r4c10
 K111
 kcard1r6c12
 K150kcard1r0c7
 K11
 kcard1r2c9
 K53
 kcard1r4c11
 K120
 kcard1r6c13
 K151kcard1r0c8
 K20
 kcard1r2c10
 K62
 kcard1r4c12
 K104
 kcard1r6c14
 K158kcard1r0c9
 K4
 kcard1r2c11
 K70
 kcard1r4c13
 K112
 kcard1r6c15
 K145kcard1r0c10
 K12
 kcard1r2c12
 K54
 kcard1r4c14
 K121
 kcard1r6c16
 K152kcard1r0c11
 K21
 kcard1r2c13
 K63
 kcard1r4c15
 K105
 kcard1r6c17
 K159kcard1r0c12
 K5
 kcard1r2c14
 K71
 kcard1r4c16
 K113
 kcard1r6c18
 K106kcard1r0c13
 K13
 kcard1r2c15
 K55
 kcard1r4c17
 K122
 kcard1r6c19
 K114kcard1r0c14
 K22
 kcard1r2c16
 K64
 kcard1r4c18
 K73
 kcard1r6c20
 K107kcard1r0c15
 K6
 kcard1r2c17
 K72
 kcard1r4c19
 K81
 kcard1r7c0
 K167kcard1r0c16
 K14
 kcard1r2c18
 K40
 kcard1r4c20
 K74
 kcard1r7c1
 K174kcard1r0c17
 K23
 kcard1r2c19
 K48
 kcard1r5c0
 K125
 kcard1r7c2
 K175kcard1r0c18
 K7
 kcard1r2c20
 K41
 kcard1r5c1
 K132
 kcard1r7c3
 K168kcard1r0c19
 K15
 kcard1r3c0
 K75
 kcard1r5c2
 K139
 kcard1r7c4
 K169kcard1r0c20
 K8
 kcard1r3c1
 K84
 kcard1r5c3
 K126
 kcard1r7c5
 K176kcard1r1c0
 K26
 kcard1r3c2
 K92
 kcard1r5c4
 K133
 kcard1r7c6
 K163kcard1r1c1
 K34
 kcard1r3c3
 K76
 kcard1r5c5
 K140
 kcard1r7c7
 K170kcard1r1c2
 K42
 kcard1r3c4
 K85
 kcard1r5c6
 K127
 kcard1r7c8
 K177kcard1r1c3
 K27
 kcard1r3c5
 K93
 kcard1r5c7
 K134
 kcard1r7c9
 K164kcard1r1c4
 K35
 kcard1r3c6
 K77
 kcard1r5c8
 K141
 kcard1r7c10
 K171kcard1r1c5
 K43
 kcard1r3c7
 K86
 kcard1r5c9
 K128
 kcard1r7c11
 K178kcard1r1c6
 K28
 kcard1r3c8
 K94
 kcard1r5c10
 K135
 kcard1r7c12
 K165kcard1r1c7
 K36
 kcard1r3c9
 K78
 kcard1r5c11
 K142
 kcard1r7c13
 K172kcard1r1c8
 K44
 kcard1r3c10
 K87
 kcard1r5c12
 K129
 kcard1r7c14
 K179kcard1r1c9
 K29
 kcard1r3c11
 K95
 kcard1r5c13
 K136
 kcard1r7c15
 K166kcard1r1c10
 K37
 kcard1r3c12
 K79
 kcard1r5c14
 K143
 kcard1r7c16
 K173kcard1r1c11
 K45
 kcard1r3c13
 K88
 kcard1r5c15
 K130
 kcard1r7c17
 K180kcard1r1c12
 K30
 kcard1r3c14
 K96
 kcard1r5c16
 K137
 kcard1r7c18
 K123kcard1r1c13
 K38
 kcard1r3c15
 K80
 kcard1r5c17
 K144
 kcard1r7c19
 K131kcard1r1c14
 K46
 kcard1r3c16
 K89
 kcard1r5c18
 K90
 kcard1r7c20
 K138

#### Replace the Relay

The NI 2811 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2811

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2811.html language=enus -->
## TOPIC 00069: NI 2811

- bundle_id: `ni-switch`
- source_path: `ni-2811.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2811.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2811A/B (NI 2811) is a high-density matrix switch card for the NI SwitchBlock. The NI 2811 is designed for combination with other NI 2811 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2811

The NI 2811A/B (NI 2811) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2811 is designed for combination with other NI 2811 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2811 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8×21 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2811 1-Wire 8×21 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2812-1-wire-16-9-matrix-topology.html language=enus -->
## TOPIC 00070: NI 2812 1-Wire 16×9 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2812-1-wire-16-9-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2812-1-wire-16-9-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2812A/B (NI 2812) in the 1-wire 16×9 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2 is

### NI 2812 1-Wire 16×9 Matrix Topology

The following figure represents the NI 2812A/B (NI 2812) in the 1-wire 16×9 matrix
 topology.

[IMAGE alt='image' src='GUID-97DC080B-DBA4-4D5E-9471-9744022AF145-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI 2812.

[IMAGE alt='image' src='GUID-E99B0036-DCBE-4DCC-8EE4-FB54E4F2A93D-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2812

<!--NI_TOPIC bundle=ni-switch path=ni-2812-hardware-diagram.html language=enus -->
## TOPIC 00071: NI 2812 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2812-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2812-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2812A/B (NI 2812). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2812 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2812 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-97DC080B-DBA4-4D5E-9471-9744022AF145-a5.gif']

The following table lists relay names for one NI 2812 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0...kCARD1AB15 |
| kCARD1R0C0...kCARD1R0C8 |
| kCARD1R1C0...kCARD1R1C8 |
| kCARD1R2C0...kCARD1R2C8 |
| kCARD1R3C0...kCARD1R3C8 |
| kCARD1R4C0...kCARD1R4C8 |
| kCARD1R5C0...kCARD1R5C8 |
| kCARD1R6C0...kCARD1R6C8 |
| kCARD1R7C0...kCARD1R7C8 |
| kCARD1R8C0...kCARD1R8C8 |
| kCARD1R9C0...kCARD1R9C8 |
| kCARD1R10C0...kCARD1R10C8 |
| kCARD1R11C0...kCARD1R11C8 |
| kCARD1R12C0...kCARD1R12C8 |
| kCARD1R13C0...kCARD1R13C8 |
| kCARD1R14C0...kCARD1R14C8 |
| kCARD1R15C0...kCARD1R15C8 |

Parent topic:

NI 2812

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2812-multicard-topologies.html language=enus -->
## TOPIC 00072: NI 2812 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2812-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2812-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2812 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2812 Multicard Topologies

Note

must

| Number ofNI 2812 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 16×9 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 16×18 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 16×27 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 16×36 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 16×45 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 16×54 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2812

Related concepts:

- NI 2812 1-Wire 16×9 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2812-relay-replacement.html language=enus -->
## TOPIC 00073: NI 2812 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2812-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2812-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2812A/B (NI 2812) uses reed relays. The NI 2812 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2812 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Meder | MS05-BV50980 |
| Safety (Reference Designators K181–K188) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2812 Relay Map 
 [IMAGE alt='image' src='GUID-8F433DE8-FF54-46B2-AF53-3C6508F7B740-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K174
 kcard1r2c6
 K34
 kcard1r7c1
 K93
 kcard1r11c5
 K144kcard1ab1
 K175
 kcard1r2c7
 K35
 kcard1r7c2
 K94
 kcard1r11c6
 K137kcard1ab2
 K176
 kcard1r2c8
 K36
 kcard1r7c3
 K95
 kcard1r11c7
 K136kcard1ab3
 K177
 kcard1r3c0
 K42
 kcard1r7c4
 K96
 kcard1r11c8
 K135kcard1ab4
 K178
 kcard1r3c1
 K43
 kcard1r7c5
 K97
 kcard1r12c0
 K146kcard1ab5
 K179
 kcard1r3c2
 K44
 kcard1r7c6
 K89
 kcard1r12c1
 K147kcard1ab6
 K180
 kcard1r3c3
 K45
 kcard1r7c7
 K88
 kcard1r12c2
 K148kcard1ab7
 K173
 kcard1r3c4
 K46
 kcard1r7c8
 K87
 kcard1r12c3
 K149kcard1ab8
 K7
 kcard1r3c5
 K47
 kcard1r8c0
 K100
 kcard1r12c4
 K150kcard1ab9
 K15
 kcard1r3c6
 K39
 kcard1r8c1
 K101
 kcard1r12c5
 K151kcard1ab10
 K24
 kcard1r3c7
 K38
 kcard1r8c2
 K102
 kcard1r12c6
 K81kcard1ab11
 K32
 kcard1r3c8
 K37
 kcard1r8c3
 K103
 kcard1r12c7
 K90kcard1ab12
 K40
 kcard1r4c0
 K50
 kcard1r8c4
 K104
 kcard1r12c8
 K98kcard1ab13
 K48
 kcard1r4c1
 K51
 kcard1r8c5
 K105
 kcard1r13c0
 K153kcard1ab14
 K56
 kcard1r4c2
 K52
 kcard1r8c6
 K108
 kcard1r13c1
 K154kcard1ab15
 K65
 kcard1r4c3
 K53
 kcard1r8c7
 K109
 kcard1r13c2
 K155kcard1r0c0
 K1
 kcard1r4c4
 K54
 kcard1r8c8
 K110
 kcard1r13c3
 K156kcard1r0c1
 K2
 kcard1r4c5
 K55
 kcard1r9c0
 K117
 kcard1r13c4
 K157kcard1r0c2
 K3
 kcard1r4c6
 K59
 kcard1r9c1
 K118
 kcard1r13c5
 K58kcard1r0c3
 K4
 kcard1r4c7
 K60
 kcard1r9c2
 K119
 kcard1r13c6
 K106kcard1r0c4
 K5
 kcard1r4c8
 K61
 kcard1r9c3
 K120
 kcard1r13c7
 K114kcard1r0c5
 K6
 kcard1r5c0
 K67
 kcard1r9c4
 K121
 kcard1r13c8
 K123kcard1r0c6
 K9
 kcard1r5c1
 K68
 kcard1r9c5
 K122
 kcard1r14c0
 K160kcard1r0c7
 K10
 kcard1r5c2
 K69
 kcard1r9c6
 K113
 kcard1r14c1
 K161kcard1r0c8
 K11
 kcard1r5c3
 K70
 kcard1r9c7
 K112
 kcard1r14c2
 K162kcard1r1c0
 K18
 kcard1r5c4
 K71
 kcard1r9c8
 K111
 kcard1r14c3
 K163kcard1r1c1
 K19
 kcard1r5c5
 K72
 kcard1r10c0
 K125
 kcard1r14c4
 K164kcard1r1c2
 K20
 kcard1r5c6
 K64
 kcard1r10c1
 K126
 kcard1r14c5
 K165kcard1r1c3
 K21
 kcard1r5c7
 K63
 kcard1r10c2
 K127
 kcard1r14c6
 K131kcard1r1c4
 K22
 kcard1r5c8
 K62
 kcard1r10c3
 K128
 kcard1r14c7
 K138kcard1r1c5
 K23
 kcard1r6c0
 K75
 kcard1r10c4
 K129
 kcard1r14c8
 K145kcard1r1c6
 K14
 kcard1r6c1
 K76
 kcard1r10c5
 K130
 kcard1r15c0
 K167kcard1r1c7
 K13
 kcard1r6c2
 K77
 kcard1r10c6
 K132
 kcard1r15c1
 K168kcard1r1c8
 K12
 kcard1r6c3
 K78
 kcard1r10c7
 K133
 kcard1r15c2
 K169kcard1r2c0
 K26
 kcard1r6c4
 K79
 kcard1r10c8
 K134
 kcard1r15c3
 K170kcard1r2c1
 K27
 kcard1r6c5
 K80
 kcard1r11c0
 K139
 kcard1r15c4
 K171kcard1r2c2
 K28
 kcard1r6c6
 K84
 kcard1r11c1
 K140
 kcard1r15c5
 K172kcard1r2c3
 K29
 kcard1r6c7
 K85
 kcard1r11c2
 K141
 kcard1r15c6
 K152kcard1r2c4
 K30
 kcard1r6c8
 K86
 kcard1r11c3
 K142
 kcard1r15c7
 K159kcard1r2c5
 K31
 kcard1r7c0
 K92
 kcard1r11c4
 K143
 kcard1r15c8
 K166

#### Replace the Relay

The NI 2812 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2812

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2812.html language=enus -->
## TOPIC 00074: NI 2812

- bundle_id: `ni-switch`
- source_path: `ni-2812.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2812.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2812A/B (NI 2812) is a high-density matrix switch card for the NI SwitchBlock. The NI 2812 is designed for combination with other NI 2812 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2812

The NI 2812A/B (NI 2812) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2812 is designed for combination with other NI 2812 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2812 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 16×9 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2812 1-Wire 16×9 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2813-2-wire-4-21-matrix-topology.html language=enus -->
## TOPIC 00075: NI 2813 2-Wire 4×21 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2813-2-wire-4-21-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2813-2-wire-4-21-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2813A/B (NI 2813) in the 2-Wire 4×21 Matrix Topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2W0 i

### NI 2813 2-Wire 4×21 Matrix Topology

The following figure represents the NI 2813A/B (NI 2813) in the 2-Wire 4×21 Matrix
 Topology.

[IMAGE alt='image' src='GUID-B52591F6-5E23-4888-B418-BFD211CC7473-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2W0 is routed to C1W0

signal connected to CARD1R2W1 is routed to C1W1

#### Pinout

The following figure identifies the pins for the NI 2813.

[IMAGE alt='image' src='GUID-36FA0EE3-36D1-480F-9C3B-F6D310EFD88E-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2813

<!--NI_TOPIC bundle=ni-switch path=ni-2813-hardware-diagram.html language=enus -->
## TOPIC 00076: NI 2813 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2813-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2813-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2813A/B (NI 2813). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2813 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2813 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-B52591F6-5E23-4888-B418-BFD211CC7473-a5.gif']

Note

| Relays |
| --- |
| kCARD1AB0W0...kCARD1AB3W0 |
| kCARD1AB0W1...kCARD1AB3W1 |
| kCARD1R0C0W0...kCARD1R0C20W0 |
| kCARD1R0C0W1...kCARD1R0C20W1 |
| kCARD1R1C0W0...kCARD1R1C20W0 |
| kCARD1R1C0W1...kCARD1R1C20W1 |
| kCARD1R2C0W0...kCARD1R2C20W0 |
| kCARD1R2C0W1...kCARD1R2C20W1 |
| kCARD1R3C0W0...kCARD1R3C20W0 |
| kCARD1R3C0W1...kCARD1R3C20W1 |

Parent topic:

NI 2813

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2813-multicard-topologies.html language=enus -->
## TOPIC 00077: NI 2813 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2813-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2813-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2813 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2813 Multicard Topologies

Note

must

| Number ofNI 2813 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 2-Wire 4×21 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 2-Wire 4×42 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 2-Wire 4×63 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 2-Wire 4×84 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 2-Wire 4×105 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 2-Wire 4×126 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2813

Related concepts:

- NI 2813 2-Wire 4×21 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2813-relay-replacement.html language=enus -->
## TOPIC 00078: NI 2813 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2813-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2813-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2813A/B (NI 2813) uses reed relays. The NI 2813 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2813 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Meder | MS05-BV50980 |
| Safety (Reference Designators K17, K58, K83, and K116) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2813 Relay Map 
 [IMAGE alt='image' src='GUID-E34B66A5-FDE0-4E63-B892-63AB6A296F4D-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0w0
 K8
 kcard1r0c18w0
 K38
 kcard1r1c19w0
 K89
 kcard1r2c20w0
 K138kcard1ab0w1
 K16
 kcard1r0c18w1
 K46
 kcard1r1c19w1
 K97
 kcard1r2c20w1
 K145kcard1ab1w0
 K25
 kcard1r0c19w0
 K39
 kcard1r1c20w0
 K90
 kcard1r3c0w0
 K146kcard1ab1w1
 K33
 kcard1r0c19w1
 K47
 kcard1r1c20w1
 K98
 kcard1r3c0w1
 K153kcard1ab2w0
 K41
 kcard1r0c20w0
 K40
 kcard1r2c0w0
 K100
 kcard1r3c1w0
 K147kcard1ab2w1
 K49
 kcard1r0c20w1
 K48
 kcard1r2c0w1
 K108
 kcard1r3c1w1
 K154kcard1ab3w0
 K57
 kcard1r1c0w0
 K50
 kcard1r2c1w0
 K101
 kcard1r3c2w0
 K148kcard1ab3w1
 K66
 kcard1r1c0w1
 K59
 kcard1r2c1w1
 K109
 kcard1r3c2w1
 K155kcard1r0c0w0
 K1
 kcard1r1c1w0
 K51
 kcard1r2c2w0
 K102
 kcard1r3c3w0
 K149kcard1r0c0w1
 K9
 kcard1r1c1w1
 K60
 kcard1r2c2w1
 K110
 kcard1r3c3w1
 K156kcard1r0c1w0
 K2
 kcard1r1c2w0
 K51
 kcard1r2c3w0
 K103
 kcard1r3c4w0
 K150kcard1r0c1w1
 K10
 kcard1r1c2w1
 K60
 kcard1r2c3w1
 K111
 kcard1r3c4w1
 K157kcard1r0c2w0
 K3
 kcard1r1c3w0
 K53
 kcard1r2c4w0
 K104
 kcard1r3c5w0
 K151kcard1r0c2w1
 K11
 kcard1r1c3w1
 K62
 kcard1r2c4w1
 K112
 kcard1r3c5w1
 K158kcard1r0c3w0
 K4
 kcard1r1c4w0
 K54
 kcard1r2c5w0
 K105
 kcard1r3c6w0
 K152kcard1r0c3w1
 K12
 kcard1r1c4w1
 K63
 kcard1r2c5w1
 K113
 kcard1r3c6w1
 K159kcard1r0c4w0
 K5
 kcard1r1c5w0
 K55
 kcard1r2c6w0
 K106
 kcard1r3c7w0
 K160kcard1r0c4w1
 K13
 kcard1r1c5w1
 K64
 kcard1r2c6w1
 K114
 kcard1r3c7w1
 K167kcard1r0c5w0
 K6
 kcard1r1c6w0
 K56
 kcard1r2c7w0
 K117
 kcard1r3c8w0
 K161kcard1r0c5w1
 K14
 kcard1r1c6w1
 K65
 kcard1r2c7w1
 K125
 kcard1r3c8w1
 K168kcard1r0c6w0
 K7
 kcard1r1c7w0
 K67
 kcard1r2c8w0
 K118
 kcard1r3c9w0
 K162kcard1r0c6w1
 K15
 kcard1r1c7w1
 K75
 kcard1r2c8w1
 K126
 kcard1r3c9w1
 K169kcard1r0c7w0
 K18
 kcard1r1c8w0
 K68
 kcard1r2c9w0
 K119
 kcard1r3c10w0
 K163kcard1r0c7w1
 K26
 kcard1r1c8w1
 K76
 kcard1r2c9w1
 K127
 kcard1r3c10w1
 K170kcard1r0c8w0
 K19
 kcard1r1c9w0
 K69
 kcard1r2c10w0
 K120
 kcard1r3c11w0
 K164kcard1r0c8w1
 K27
 kcard1r1c9w1
 K77
 kcard1r2c10w1
 K128
 kcard1r3c11w1
 K171kcard1r0c9w0
 K20
 kcard1r1c10w0
 K70
 kcard1r2c11w0
 K121
 kcard1r3c12w0
 K165kcard1r0c9w1
 K28
 kcard1r1c10w1
 K78
 kcard1r2c11w1
 K129
 kcard1r3c12w1
 K172kcard1r0c10w0
 K21
 kcard1r1c11w0
 K71
 kcard1r2c12w0
 K122
 kcard1r3c13w0
 K166kcard1r0c10w1
 K29
 kcard1r1c11w1
 K79
 kcard1r2c12w1
 K130
 kcard1r3c13w1
 K173kcard1r0c11w0
 K22
 kcard1r1c12w0
 K72
 kcard1r2c13w0
 K123
 kcard1r3c14w0
 K174kcard1r0c11w1
 K30
 kcard1r1c12w1
 K80
 kcard1r2c13w1
 K131
 kcard1r3c14w1
 K175kcard1r0c12w0
 K23
 kcard1r1c13w0
 K73
 kcard1r2c14w0
 K132
 kcard1r3c15w0
 K176kcard1r0c12w1
 K31
 kcard1r1c13w1
 K81
 kcard1r2c14w1
 K139
 kcard1r3c15w1
 K177kcard1r0c13w0
 K24
 kcard1r1c14w0
 K84
 kcard1r2c15w0
 K133
 kcard1r3c16w0
 K178kcard1r0c13w1
 K32
 kcard1r1c14w1
 K92
 kcard1r2c15w1
 K140
 kcard1r3c16w1
 K179kcard1r0c14w0
 K34
 kcard1r1c15w0
 K85
 kcard1r2c16w0
 K134
 kcard1r3c17w0
 K180kcard1r0c14w1
 K42
 kcard1r1c15w1
 K93
 kcard1r2c16w1
 K141
 kcard1r3c17w1
 K124kcard1r0c15w0
 K35
 kcard1r1c16w0
 K86
 kcard1r2c17w0
 K135
 kcard1r3c18w0
 K107kcard1r0c15w1
 K43
 kcard1r1c16w1
 K94
 kcard1r2c17w1
 K142
 kcard1r3c18w1
 K115kcard1r0c16w0
 K36
 kcard1r1c17w0
 K87
 kcard1r2c18w0
 K136
 kcard1r3c19w0
 K91kcard1r0c16w1
 K44
 kcard1r1c17w1
 K95
 kcard1r2c18w1
 K143
 kcard1r3c19w1
 K99kcard1r0c17w0
 K37
 kcard1r1c18w0
 K88
 kcard1r2c19w0
 K137
 kcard1r3c20w0
 K74kcard1r0c17w1
 K45
 kcard1r1c18w1
 K96
 kcard1r2c19w1
 K144
 kcard1r3c20w1
 K82

#### Replace the Relay

The NI 2813 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2813

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2813.html language=enus -->
## TOPIC 00079: NI 2813

- bundle_id: `ni-switch`
- source_path: `ni-2813.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2813.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2813A/B (NI 2813) is a high-density matrix switch card for the NI SwitchBlock. The NI 2813 is designed for combination with other NI 2813 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2813

The NI 2813A/B (NI 2813) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2813 is designed for combination with other NI 2813 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2813 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 4×21 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2813 2-Wire 4×21 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2814-2-wire-8-9-matrix-topology.html language=enus -->
## TOPIC 00080: NI 2814 2-Wire 8×9 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2814-2-wire-8-9-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2814-2-wire-8-9-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2814A/B (NI 2814) in the 2-Wire 8×9 Matrix Topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2W0 is

### NI 2814 2-Wire 8×9 Matrix Topology

The following figure represents the NI 2814A/B (NI 2814) in the 2-Wire 8×9 Matrix
 Topology.

[IMAGE alt='image' src='GUID-CF98BCDC-AD0B-4338-8BC7-F0A68ACFB8FF-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2W0 is routed to C1W0

signal connected to CARD1R2W1 is routed to C1W1

#### Pinout

The following figure identifies the pins for the NI 2814.

[IMAGE alt='image' src='GUID-A58708D0-D70B-4305-B5F2-BEE527D1091A-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2814

<!--NI_TOPIC bundle=ni-switch path=ni-2814-hardware-diagram.html language=enus -->
## TOPIC 00081: NI 2814 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2814-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2814-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2814A/B (NI 2814). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2814 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2814 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-CF98BCDC-AD0B-4338-8BC7-F0A68ACFB8FF-a5.gif']

Note

| Relays |
| --- |
| kCARD1AB0W0...kCARD1AB7W0 |
| kCARD1AB0W1...kCARD1AB7W1 |
| kCARD1R0C0W0...kCARD1R0C8W0 |
| kCARD1R0C0W1...kCARD1R0C8W1 |
| kCARD1R1C0W0...kCARD1R1C8W0 |
| kCARD1R1C0W1...kCARD1R1C8W1 |
| kCARD1R2C0W0...kCARD1R2C8W0 |
| kCARD1R2C0W1...kCARD1R2C8W1 |
| kCARD1R3C0W0...kCARD1R3C8W0 |
| kCARD1R3C0W1...kCARD1R3C8W1 |
| kCARD1R4C0W0...kCARD1R4C8W0 |
| kCARD1R4C0W1...kCARD1R4C8W1 |
| kCARD1R5C0W0...kCARD1R5C8W0 |
| kCARD1R5C0W1...kCARD1R5C8W1 |
| kCARD1R6C0W0...kCARD1R6C8W0 |
| kCARD1R6C0W1...kCARD1R6C8W1 |
| kCARD1R7C0W0...kCARD1R7C8W0 |
| kCARD1R7C0W1...kCARD1R7C8W1 |

Parent topic:

NI 2814

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2814-multicard-topologies.html language=enus -->
## TOPIC 00082: NI 2814 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2814-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2814-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2814 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2814 Multicard Topologies

Note

must

| Number ofNI 2814 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 2-Wire 8×9 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 2-Wire 8×18 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 2-Wire 8×27 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 2-Wire 8×36 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 2-Wire 8×45 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 2-Wire 8×54 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2814

Related concepts:

- NI 2814 2-Wire 8×9 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2814-relay-replacement.html language=enus -->
## TOPIC 00083: NI 2814 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2814-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2814-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2814A/B (NI 2814) uses reed relays. The NI 2814 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2814 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Meder | MS05-BV50980 |
| Safety (Reference Designators K15, K16, K45, K46, K74, K75, K104, and K105) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2814 Relay Map 
 [IMAGE alt='image' src='GUID-DD68EB02-19AA-4EF9-82CB-5FA58F516574-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0w0
 K7
 kcard1r1c3w0
 K34
 kcard1r3c5w0
 K81
 kcard1r5c7w0
 K110kcard1ab0w1
 K14
 kcard1r1c3w1
 K41
 kcard1r3c5w1
 K88
 kcard1r5c7w1
 K117kcard1ab1w0
 K23
 kcard1r1c4w0
 K35
 kcard1r3c6w0
 K66
 kcard1r5c8w0
 K109kcard1ab1w1
 K30
 kcard1r1c4w1
 K42
 kcard1r3c6w1
 K72
 kcard1r5c8w1
 K116kcard1ab2w0
 K37
 kcard1r1c5w0
 K36
 kcard1r3c7w0
 K65
 kcard1r6c0w0
 K134kcard1ab2w1
 K44
 kcard1r1c5w1
 K43
 kcard1r3c7w1
 K71
 kcard1r6c0w1
 K141kcard1ab3w0
 K53
 kcard1r1c6w0
 K22
 kcard1r3c8w0
 K64
 kcard1r6c1w0
 K135kcard1ab3w1
 K60
 kcard1r1c6w1
 K29
 kcard1r3c8w1
 K70
 kcard1r6c1w1
 K142kcard1ab4w0
 K73
 kcard1r1c7w0
 K21
 kcard1r4c0w0
 K90
 kcard1r6c2w0
 K136kcard1ab4w1
 K82
 kcard1r1c7w1
 K28
 kcard1r4c0w1
 K97
 kcard1r6c2w1
 K143kcard1ab5w0
 K89
 kcard1r1c8w0
 K20
 kcard1r4c1w0
 K91
 kcard1r6c3w0
 K137kcard1ab5w1
 K96
 kcard1r1c8w1
 K27
 kcard1r4c1w1
 K98
 kcard1r6c3w1
 K144kcard1ab6w0
 K103
 kcard1r2c0w0
 K47
 kcard1r4c2w0
 K92
 kcard1r6c4w0
 K138kcard1ab6w1
 K112
 kcard1r2c0w1
 K54
 kcard1r4c2w1
 K99
 kcard1r6c4w1
 K145kcard1ab7w0
 K119
 kcard1r2c1w0
 K48
 kcard1r4c3w0
 K93
 kcard1r6c5w0
 K139kcard1ab7w1
 K126
 kcard1r2c1w1
 K55
 kcard1r4c3w1
 K100
 kcard1r6c5w1
 K146kcard1r0c0w0
 K1
 kcard1r2c2w0
 K49
 kcard1r4c4w0
 K94
 kcard1r6c6w0
 K148kcard1r0c0w1
 K8
 kcard1r2c2w1
 K56
 kcard1r4c4w1
 K101
 kcard1r6c6w1
 K155kcard1r0c1w0
 K2
 kcard1r2c3w0
 K50
 kcard1r4c5w0
 K95
 kcard1r6c7w0
 K149kcard1r0c1w1
 K9
 kcard1r2c3w1
 K57
 kcard1r4c5w1
 K102
 kcard1r6c7w1
 K156kcard1r0c2w0
 K3
 kcard1r2c4w0
 K51
 kcard1r4c6w0
 K106
 kcard1r6c8w0
 K150kcard1r0c2w1
 K10
 kcard1r2c4w1
 K58
 kcard1r4c6w1
 K113
 kcard1r6c8w1
 K157kcard1r0c3w0
 K4
 kcard1r2c5w0
 K52
 kcard1r4c7w0
 K107
 kcard1r7c0w0
 K162kcard1r0c3w1
 K11
 kcard1r2c5w1
 K59
 kcard1r4c7w1
 K114
 kcard1r7c0w1
 K163kcard1r0c4w0
 K5
 kcard1r2c6w0
 K61
 kcard1r4c8w0
 K108
 kcard1r7c1w0
 K164kcard1r0c4w1
 K12
 kcard1r2c6w1
 K67
 kcard1r4c8w1
 K115
 kcard1r7c1w1
 K165kcard1r0c5w0
 K6
 kcard1r2c7w0
 K62
 kcard1r5c0w0
 K120
 kcard1r7c2w0
 K166kcard1r0c5w1
 K13
 kcard1r2c7w1
 K68
 kcard1r5c0w1
 K127
 kcard1r7c2w1
 K167kcard1r0c6w0
 K17
 kcard1r2c8w0
 K63
 kcard1r5c1w0
 K121
 kcard1r7c3w0
 K161kcard1r0c6w1
 K24
 kcard1r2c8w1
 K69
 kcard1r5c1w1
 K128
 kcard1r7c3w1
 K168kcard1r0c7w0
 K18
 kcard1r3c0w0
 K76
 kcard1r5c2w0
 K122
 kcard1r7c4w0
 K147kcard1r0c7w1
 K25
 kcard1r3c0w1
 K83
 kcard1r5c2w1
 K129
 kcard1r7c4w1
 K154kcard1r0c8w0
 K19
 kcard1r3c1w0
 K77
 kcard1r5c3w0
 K123
 kcard1r7c5w0
 K133kcard1r0c8w1
 K26
 kcard1r3c1w1
 K84
 kcard1r5c3w1
 K130
 kcard1r7c5w1
 K140kcard1r1c0w0
 K31
 kcard1r3c2w0
 K78
 kcard1r5c4w0
 K124
 kcard1r7c6w0
 K153kcard1r1c0w1
 K38
 kcard1r3c2w1
 K85
 kcard1r5c4w1
 K131
 kcard1r7c6w1
 K160kcard1r1c1w0
 K32
 kcard1r3c3w0
 K79
 kcard1r5c5w0
 K125
 kcard1r7c7w0
 K152kcard1r1c1w1
 K39
 kcard1r3c3w1
 K86
 kcard1r5c5w1
 K132
 kcard1r7c7w1
 K159kcard1r1c2w0
 K33
 kcard1r3c4w0
 K80
 kcard1r5c6w0
 K111
 kcard1r7c8w0
 K151kcard1r1c2w1
 K40
 kcard1r3c4w1
 K87
 kcard1r5c6w1
 K118
 kcard1r7c8w1
 K158

#### Replace the Relay

The NI 2814 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2814

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2814.html language=enus -->
## TOPIC 00084: NI 2814

- bundle_id: `ni-switch`
- source_path: `ni-2814.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2814.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2814A/B (NI 2814) is a high-density matrix switch card for the NI SwitchBlock. The NI 2814 is designed for combination with other NI 2814 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2814

The NI 2814A/B (NI 2814) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2814 is designed for combination with other NI 2814 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2814 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 8×9 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2814 2-Wire 8×9 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2815-1-wire-4-86-matrix-topology.html language=enus -->
## TOPIC 00085: NI 2815 1-Wire 4×86 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2815-1-wire-4-86-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2815-1-wire-4-86-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2815A/B (NI 2815) in the 1-wire 4×86 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2 is

### NI 2815 1-Wire 4×86 Matrix Topology

The following figure represents the NI 2815A/B (NI 2815) in the 1-wire 4×86 matrix
 topology.

[IMAGE alt='image' src='GUID-EE7DBCF1-F8AF-42FD-B598-F2F13CCE78F8-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI 2815.

[IMAGE alt='image' src='GUID-392660B5-8322-466B-A436-614B9414F8D6-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2815

<!--NI_TOPIC bundle=ni-switch path=ni-2815-hardware-diagram.html language=enus -->
## TOPIC 00086: NI 2815 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2815-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2815-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2815A/B (NI 2815). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2815 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2815 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-EE7DBCF1-F8AF-42FD-B598-F2F13CCE78F8-a5.gif']

The following table lists relay names for one NI 2815 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0 |
| kCARD1AB1 |
| kCARD1AB2 |
| kCARD1AB3 |
| kCARD1R0C0...kCARD1R0C85 |
| kCARD1R1C0...kCARD1R1C85 |
| kCARD1R2C0...kCARD1R2C85 |
| kCARD1R3C0...kCARD1R3C85 |

Parent topic:

NI 2815

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2815-multicard-topologies.html language=enus -->
## TOPIC 00087: NI 2815 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2815-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2815-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2815 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2815 Multicard Topologies

Note

must

| Number ofNI 2815 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 4×86 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 4×172 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 4×258 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 4×344 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 4×430 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 4×516 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2815

Related concepts:

- NI 2815 1-Wire 4×86 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2815-relay-replacement.html language=enus -->
## TOPIC 00088: NI 2815 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2815-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2815-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2815A/B (NI 2815) uses reed relays. The NI 2815 uses a custom lead length to meet safety standards. Trim the leads per rework instructions or use one of the custom relays from the relay kit. If spare relays are included with the module at locations K351 to K358, you can also use those. Refer

### NI 2815 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Coto | 9117-0001 |
| Safety (Reference Designators K18 and K53) | Tyco Electronics | 5-1462039-8 |
| Matrix | Standex-Meder | UMS05-BV51338 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays, Coto 9117) | 781451-10 |
| National Instruments (10 safety relays, Tyco Electronics) | 781089-10 |
| National Instruments (10 matrix relays, Standex-Meder UMS) | 786915-01 |

Note

Note

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Disassemble the Card

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to your card from electrostatic
 discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. Figure 1.NI 2815 Relay Map
 
 [IMAGE alt='NI-2815 Relay Map' src='GUID-42885B02-F6F5-46EF-B721-1FB1D1F0D7BF-a5.gif'] Note The
 insulator cover attaches to the two rightmost columns of matrix relays,
 outlined in bold on the relay map, and must be removed to replace these
 relays. You can replace these relays and the insulator cover by sending the
 card to National Instruments for a rework return material authorization
 (RMA) or by following the instructions in the relay replacement procedure. Note The
 relay names in the following table correspond to a single-card device. Refer
 to the NI SwitchBlock Device Reference for information about relay naming
 for multicard devices. RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K35
 kcard1r0c83
 K343
 kcard1r1c84
 K336
 kcard1r2c85
 K349
 kcard1ab1
 K17
 kcard1r0c84
 K335
 kcard1r1c85
 K348
 kcard1r3c0
 K4
 kcard1ab2
 K70
 kcard1r0c85
 K347
 kcard1r2c0
 K3
 kcard1r3c1
 K22
 kcard1ab3
 K52
 kcard1r1c0
 K2
 kcard1r2c1
 K21
 kcard1r3c2
 K8
 kcard1r0c0
 K1
 kcard1r1c1
 K20
 kcard1r2c2
 K7
 kcard1r3c3
 K26
 kcard1r0c1
 K19
 kcard1r1c2
 K6
 kcard1r2c3
 K25
 kcard1r3c4
 K12
 kcard1r0c2
 K5
 kcard1r1c3
 K24
 kcard1r2c4
 K11
 kcard1r3c5
 K30
 kcard1r0c3
 K23
 kcard1r1c4
 K10
 kcard1r2c5
 K29
 kcard1r3c6
 K16
 kcard1r0c4
 K9
 kcard1r1c5
 K28
 kcard1r2c6
 K15
 kcard1r3c7
 K34
 kcard1r0c5
 K27
 kcard1r1c6
 K14
 kcard1r2c7
 K33
 kcard1r3c8
 K39
 kcard1r0c6
 K13
 kcard1r1c7
 K32
 kcard1r2c8
 K38
 kcard1r3c9
 K57
 kcard1r0c7
 K31
 kcard1r1c8
 K37
 kcard1r2c9
 K56
 kcard1r3c10
 K43
 kcard1r0c8
 K36
 kcard1r1c9
 K55
 kcard1r2c10
 K42
 kcard1r3c11
 K61
 kcard1r0c9
 K54
 kcard1r1c10
 K41
 kcard1r2c11
 K60
 kcard1r3c12
 K47
 kcard1r0c10
 K40
 kcard1r1c11
 K59
 kcard1r2c12
 K46
 kcard1r3c13
 K65
 kcard1r0c11
 K58
 kcard1r1c12
 K45
 kcard1r2c13
 K64
 kcard1r3c14
 K51
 kcard1r0c12
 K44
 kcard1r1c13
 K63
 kcard1r2c14
 K50
 kcard1r3c15
 K69
 kcard1r0c13
 K62
 kcard1r1c14
 K49
 kcard1r2c15
 K68
 kcard1r3c16
 K74
 kcard1r0c14
 K48
 kcard1r1c15
 K67
 kcard1r2c16
 K73
 kcard1r3c17
 K90
 kcard1r0c15
 K66
 kcard1r1c16
 K72
 kcard1r2c17
 K89
 kcard1r3c18
 K78
 kcard1r0c16
 K71
 kcard1r1c17
 K88
 kcard1r2c18
 K77
 kcard1r3c19
 K94
 kcard1r0c17
 K87
 kcard1r1c18
 K76
 kcard1r2c19
 K93
 kcard1r3c20
 K82
 kcard1r0c18
 K75
 kcard1r1c19
 K92
 kcard1r2c20
 K81
 kcard1r3c21
 K98
 kcard1r0c19
 K91
 kcard1r1c20
 K80
 kcard1r2c21
 K97
 kcard1r3c22
 K86
 kcard1r0c20
 K79
 kcard1r1c21
 K96
 kcard1r2c22
 K85
 kcard1r3c23
 K102
 kcard1r0c21
 K95
 kcard1r1c22
 K84
 kcard1r2c23
 K101
 kcard1r3c24
 K106
 kcard1r0c22
 K83
 kcard1r1c23
 K100
 kcard1r2c24
 K105
 kcard1r3c25
 K122
 kcard1r0c23
 K99
 kcard1r1c24
 K104
 kcard1r2c25
 K121
 kcard1r3c26
 K110
 kcard1r0c24
 K103
 kcard1r1c25
 K120
 kcard1r2c26
 K109
 kcard1r3c27
 K126
 kcard1r0c25
 K119
 kcard1r1c26
 K108
 kcard1r2c27
 K125
 kcard1r3c28
 K114
 kcard1r0c26
 K107
 kcard1r1c27
 K124
 kcard1r2c28
 K113
 kcard1r3c29
 K130
 kcard1r0c27
 K123
 kcard1r1c28
 K112
 kcard1r2c29
 K129
 kcard1r3c30
 K118
 kcard1r0c28
 K111
 kcard1r1c29
 K128
 kcard1r2c30
 K117
 kcard1r3c31
 K134
 kcard1r0c29
 K127
 kcard1r1c30
 K116
 kcard1r2c31
 K133
 kcard1r3c32
 K138
 kcard1r0c30
 K115
 kcard1r1c31
 K132
 kcard1r2c32
 K137
 kcard1r3c33
 K154
 kcard1r0c31
 K131
 kcard1r1c32
 K136
 kcard1r2c33
 K153
 kcard1r3c34
 K142
 kcard1r0c32
 K135
 kcard1r1c33
 K152
 kcard1r2c34
 K141
 kcard1r3c35
 K158
 kcard1r0c33
 K151
 kcard1r1c34
 K140
 kcard1r2c35
 K157
 kcard1r3c36
 K146
 kcard1r0c34
 K139
 kcard1r1c35
 K156
 kcard1r2c36
 K145
 kcard1r3c37
 K162
 kcard1r0c35
 K155
 kcard1r1c36
 K144
 kcard1r2c37
 K161
 kcard1r3c38
 K150
 kcard1r0c36
 K143
 kcard1r1c37
 K160
 kcard1r2c38
 K149
 kcard1r3c39
 K166
 kcard1r0c37
 K159
 kcard1r1c38
 K148
 kcard1r2c39
 K165
 kcard1r3c40
 K170
 kcard1r0c38
 K147
 kcard1r1c39
 K164
 kcard1r2c40
 K169
 kcard1r3c41
 K186
 kcard1r0c39
 K163
 kcard1r1c40
 K168
 kcard1r2c41
 K185
 kcard1r3c42
 K174
 kcard1r0c40
 K167
 kcard1r1c41
 K184
 kcard1r2c42
 K173
 kcard1r3c43
 K190
 kcard1r0c41
 K183
 kcard1r1c42
 K172
 kcard1r2c43
 K189
 kcard1r3c44
 K178
 kcard1r0c42
 K171
 kcard1r1c43
 K188
 kcard1r2c44
 K177
 kcard1r3c45
 K194
 kcard1r0c43
 K187
 kcard1r1c44
 K176
 kcard1r2c45
 K193
 kcard1r3c46
 K182
 kcard1r0c44
 K175
 kcard1r1c45
 K192
 kcard1r2c46
 K181
 kcard1r3c47
 K198
 kcard1r0c45
 K191
 kcard1r1c46
 K180
 kcard1r2c47
 K197
 kcard1r3c48
 K202
 kcard1r0c46
 K179
 kcard1r1c47
 K196
 kcard1r2c48
 K201
 kcard1r3c49
 K218
 kcard1r0c47
 K195
 kcard1r1c48
 K200
 kcard1r2c49
 K217
 kcard1r3c50
 K206
 kcard1r0c48
 K199
 kcard1r1c49
 K216
 kcard1r2c50
 K205
 kcard1r3c51
 K222
 kcard1r0c49
 K215
 kcard1r1c50
 K204
 kcard1r2c51
 K221
 kcard1r3c52
 K210
 kcard1r0c50
 K203
 kcard1r1c51
 K220
 kcard1r2c52
 K209
 kcard1r3c53
 K226
 kcard1r0c51
 K219
 kcard1r1c52
 K208
 kcard1r2c53
 K225
 kcard1r3c54
 K214
 kcard1r0c52
 K207
 kcard1r1c53
 K224
 kcard1r2c54
 K213
 kcard1r3c55
 K230
 kcard1r0c53
 K223
 kcard1r1c54
 K212
 kcard1r2c55
 K229
 kcard1r3c56
 K234
 kcard1r0c54
 K211
 kcard1r1c55
 K228
 kcard1r2c56
 K233
 kcard1r3c57
 K250
 kcard1r0c55
 K227
 kcard1r1c56
 K232
 kcard1r2c57
 K249
 kcard1r3c58
 K238
 kcard1r0c56
 K231
 kcard1r1c57
 K248
 kcard1r2c58
 K237
 kcard1r3c59
 K254
 kcard1r0c57
 K247
 kcard1r1c58
 K236
 kcard1r2c59
 K253
 kcard1r3c60
 K242
 kcard1r0c58
 K235
 kcard1r1c59
 K252
 kcard1r2c60
 K241
 kcard1r3c61
 K258
 kcard1r0c59
 K251
 kcard1r1c60
 K240
 kcard1r2c61
 K257
 kcard1r3c62
 K246
 kcard1r0c60
 K239
 kcard1r1c61
 K256
 kcard1r2c62
 K245
 kcard1r3c63
 K262
 kcard1r0c61
 K255
 kcard1r1c62
 K244
 kcard1r2c63
 K261
 kcard1r3c64
 K266
 kcard1r0c62
 K243
 kcard1r1c63
 K260
 kcard1r2c64
 K265
 kcard1r3c65
 K282
 kcard1r0c63
 K259
 kcard1r1c64
 K264
 kcard1r2c65
 K281
 kcard1r3c66
 K270
 kcard1r0c64
 K263
 kcard1r1c65
 K280
 kcard1r2c66
 K269
 kcard1r3c67
 K286
 kcard1r0c65
 K279
 kcard1r1c66
 K268
 kcard1r2c67
 K285
 kcard1r3c68
 K274
 kcard1r0c66
 K267
 kcard1r1c67
 K284
 kcard1r2c68
 K273
 kcard1r3c69
 K290
 kcard1r0c67
 K283
 kcard1r1c68
 K272
 kcard1r2c69
 K289
 kcard1r3c70
 K278
 kcard1r0c68
 K271
 kcard1r1c69
 K288
 kcard1r2c70
 K277
 kcard1r3c71
 K294
 kcard1r0c69
 K287
 kcard1r1c70
 K276
 kcard1r2c71
 K293
 kcard1r3c72
 K298
 kcard1r0c70
 K275
 kcard1r1c71
 K292
 kcard1r2c72
 K297
 kcard1r3c73
 K314
 kcard1r0c71
 K291
 kcard1r1c72
 K296
 kcard1r2c73
 K313
 kcard1r3c74
 K302
 kcard1r0c72
 K295
 kcard1r1c73
 K312
 kcard1r2c74
 K301
 kcard1r3c75
 K318
 kcard1r0c73
 K311
 kcard1r1c74
 K300
 kcard1r2c75
 K317
 kcard1r3c76
 K306
 kcard1r0c74
 K299
 kcard1r1c75
 K316
 kcard1r2c76
 K305
 kcard1r3c77
 K322
 kcard1r0c75
 K315
 kcard1r1c76
 K304
 kcard1r2c77
 K321
 kcard1r3c78
 K310
 kcard1r0c76
 K303
 kcard1r1c77
 K320
 kcard1r2c78
 K309
 kcard1r3c79
 K326
 kcard1r0c77
 K319
 kcard1r1c78
 K308
 kcard1r2c79
 K325
 kcard1r3c80
 K330
 kcard1r0c78
 K307
 kcard1r1c79
 K324
 kcard1r2c80
 K329
 kcard1r3c81
 K342
 kcard1r0c79
 K323
 kcard1r1c80
 K328
 kcard1r2c81
 K341
 kcard1r3c82
 K334
 kcard1r0c80
 K327
 kcard1r1c81
 K340
 kcard1r2c82
 K333
 kcard1r3c83
 K346
 kcard1r0c81
 K339
 kcard1r1c82
 K332
 kcard1r2c83
 K345
 kcard1r3c84
 K338
 kcard1r0c82
 K331
 kcard1r1c83
 K344
 kcard1r2c84
 K337
 kcard1r3c85
 K350
3. Remove the screws that hold one side of the insulator cover to the card. 1
 NI 2815
 2
 Insulator Cover
 3
 Screws
4. Lift the insulator cover to access the relays. To replace a relay in one of the
 two rightmost columns of matrix relays, carefully peel the adhesive strip of the
 insulator cover off of these two columns of relays. 1
 NI 2815
 2
 Insulator Cover

#### Replace the Relay

The NI 2815 uses lead-free assemblies.

Note

Caution

Caution

Make
 sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced
 relay leads to no more than 0.5 mm (0.02 inch) from the PCB.

#### Reassemble the Card

Refer to one of the following procedures to reassemble your card after replacing any
 relays.

#### Reassembly If Insulator Cover Was Not Removed

If you only replaced relays outside of the two rightmost columns of matrix relays,
 and therefore did not remove the adhesive strip of the insulator cover, complete the
 Disassemble the Card steps in reverse order to reassemble your card.

#### Reassembly If Insulator Cover Was
 Removed

If you removed the insulator cover, including the adhesive strip, to replace a relay
 in one of the two rightmost columns of matrix relays, complete the following steps
 to reassemble your card.

1. Use screws to attach one side of the replacement insulator cover to the card.
 1
 NI 2815
 2
 Insulator Cover
 3
 Screws
2. Lift the unattached side of the replacement insulator cover and remove the liner
 from the adhesive strip. 1
 Adhesive Strip
 2
 Insulator Cover
 3
 NI 2815
3. Firmly press the adhesive strip on top of the two rightmost columns of matrix
 relays.

Tip

Switch Soft Front Panel Help

Parent topic:

NI 2815

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2815.html language=enus -->
## TOPIC 00089: NI 2815

- bundle_id: `ni-switch`
- source_path: `ni-2815.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2815.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2815A/B (NI 2815) is a high-density matrix switch card for the NI SwitchBlock. The NI 2815 is designed for combination with other NI 2815 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2815

The NI 2815A/B (NI 2815) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2815 is designed for combination with other NI 2815 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2815 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×86 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2815 1-Wire 4×86 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2816-1-wire-8-46-matrix-topology.html language=enus -->
## TOPIC 00090: NI 2816 1-Wire 8×46 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2816-1-wire-8-46-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2816-1-wire-8-46-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2816A/B (NI 2816) in the 1-wire 8×46 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r1 and c1, results in the following connection: signal connected to CARD1R1 is

### NI 2816 1-Wire 8×46 Matrix Topology

The following figure represents the NI 2816A/B (NI 2816) in the 1-wire 8×46 matrix
 topology.

[IMAGE alt='image' src='GUID-E4670DA6-638D-436D-9D5E-D7599FC682D5-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r1 and c1, results
 in the following connection:

signal connected to CARD1R1 is routed to C1

#### Pinout

The following figure identifies the pins for the NI 2816.

[IMAGE alt='image' src='GUID-E6C6EF83-D97C-4098-9F6B-F10B98B54764-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2816

<!--NI_TOPIC bundle=ni-switch path=ni-2816-hardware-diagram.html language=enus -->
## TOPIC 00091: NI 2816 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2816-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2816-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2816A/B (NI 2816). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2816 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2816 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-E4670DA6-638D-436D-9D5E-D7599FC682D5-a5.gif']

The following table lists relay names for one NI 2816 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0 |
| kCARD1AB1 |
| kCARD1AB2 |
| kCARD1AB3 |
| kCARD1AB4 |
| kCARD1AB5 |
| kCARD1AB6 |
| kCARD1AB7 |
| kCARD1R0C0...kCARD1R0C45 |
| kCARD1R1C0...kCARD1R1C45 |
| kCARD1R2C0...kCARD1R2C45 |
| kCARD1R3C0...kCARD1R3C45 |
| kCARD1R4C0...kCARD1R4C45 |
| kCARD1R5C0...kCARD1R5C45 |
| kCARD1R6C0...kCARD1R6C45 |
| kCARD1R7C0...kCARD1R7C45 |

Parent topic:

NI 2816

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2816-multicard-topologies.html language=enus -->
## TOPIC 00092: NI 2816 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2816-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2816-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2816 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2816 Multicard Topologies

Note

must

| Number ofNI 2816 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 8×46 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 8×92 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 8×138 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 8×184 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 8×230 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 8×276 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2816

Related concepts:

- NI 2816 1-Wire 8×46 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2816-relay-replacement.html language=enus -->
## TOPIC 00093: NI 2816 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2816-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2816-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2816A/B (NI 2816) uses reed relays. The NI 2816 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2816 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Coto | 9117-0001 |
| Safety (Reference Designators K18, K53, K168, and K283) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781451-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Disassemble the Card

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2816 Relay Map 
 [IMAGE alt='image' src='GUID-4D316103-4B87-4AE3-B70B-0ADCF6A61553-a5.gif'] 
 Note The insulator cover attaches to the two rightmost columns
 of matrix relays, outlined in bold on the relay map, and must be removed to
 replace these relays. You can replace these relays and the insulator cover
 by sending the card to National Instruments for a rework return material
 authorization (RMA) or by following the instructions in the relay
 replacement procedure. 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K35
 kcard1r1c40
 K333
 kcard1r3c42
 K351
 kcard1r5c44
 K375kcard1ab1
 K17
 kcard1r1c41
 K334
 kcard1r3c43
 K352
 kcard1r5c45
 K376kcard1ab2
 K70
 kcard1r1c42
 K349
 kcard1r3c44
 K367
 kcard1r6c0
 K13kcard1ab3
 K52
 kcard1r1c43
 K350
 kcard1r3c45
 K368
 kcard1r6c1
 K14kcard1ab4
 K185
 kcard1r1c44
 K365
 kcard1r4c0
 K9
 kcard1r6c2
 K31kcard1ab5
 K167
 kcard1r1c45
 K366
 kcard1r4c1
 K10
 kcard1r6c3
 K32kcard1ab6
 K300
 kcard1r2c0
 K7
 kcard1r4c2
 K27
 kcard1r6c4
 K48kcard1ab7
 K282
 kcard1r2c1
 K8
 kcard1r4c3
 K28
 kcard1r6c5
 K49kcard1r0c0
 K5
 kcard1r2c2
 K25
 kcard1r4c4
 K44
 kcard1r6c6
 K66kcard1r0c1
 K6
 kcard1r2c3
 K26
 kcard1r4c5
 K45
 kcard1r6c7
 K67kcard1r0c2
 K23
 kcard1r2c4
 K42
 kcard1r4c6
 K62
 kcard1r6c8
 K83kcard1r0c3
 K24
 kcard1r2c5
 K43
 kcard1r4c7
 K63
 kcard1r6c9
 K84kcard1r0c4
 K40
 kcard1r2c6
 K60
 kcard1r4c8
 K79
 kcard1r6c10
 K99kcard1r0c5
 K41
 kcard1r2c7
 K61
 kcard1r4c9
 K80
 kcard1r6c11
 K100kcard1r0c6
 K58
 kcard1r2c8
 K77
 kcard1r4c10
 K95
 kcard1r6c12
 K115kcard1r0c7
 K59
 kcard1r2c9
 K78
 kcard1r4c11
 K96
 kcard1r6c13
 K116kcard1r0c8
 K75
 kcard1r2c10
 K93
 kcard1r4c12
 K111
 kcard1r6c14
 K131kcard1r0c9
 K76
 kcard1r2c11
 K94
 kcard1r4c13
 K112
 kcard1r6c15
 K132kcard1r0c10
 K91
 kcard1r2c12
 K109
 kcard1r4c14
 K127
 kcard1r6c16
 K147kcard1r0c11
 K92
 kcard1r2c13
 K110
 kcard1r4c15
 K128
 kcard1r6c17
 K148kcard1r0c12
 K107
 kcard1r2c14
 K125
 kcard1r4c16
 K143
 kcard1r6c18
 K163kcard1r0c13
 K108
 kcard1r2c15
 K126
 kcard1r4c17
 K144
 kcard1r6c19
 K164kcard1r0c14
 K123
 kcard1r2c16
 K141
 kcard1r4c18
 K159
 kcard1r6c20
 K181kcard1r0c15
 K124
 kcard1r2c17
 K142
 kcard1r4c19
 K160
 kcard1r6c21
 K182kcard1r0c16
 K139
 kcard1r2c18
 K157
 kcard1r4c20
 K177
 kcard1r6c22
 K198kcard1r0c17
 K140
 kcard1r2c19
 K158
 kcard1r4c21
 K178
 kcard1r6c23
 K199kcard1r0c18
 K155
 kcard1r2c20
 K175
 kcard1r4c22
 K194
 kcard1r6c24
 K214kcard1r0c19
 K156
 kcard1r2c21
 K176
 kcard1r4c23
 K195
 kcard1r6c25
 K215kcard1r0c20
 K173
 kcard1r2c22
 K192
 kcard1r4c24
 K210
 kcard1r6c26
 K230kcard1r0c21
 K174
 kcard1r2c23
 K193
 kcard1r4c25
 K211
 kcard1r6c27
 K231kcard1r0c22
 K190
 kcard1r2c24
 K208
 kcard1r4c26
 K226
 kcard1r6c28
 K246kcard1r0c23
 K191
 kcard1r2c25
 K209
 kcard1r4c27
 K227
 kcard1r6c29
 K247kcard1r0c24
 K206
 kcard1r2c26
 K224
 kcard1r4c28
 K242
 kcard1r6c30
 K262kcard1r0c25
 K207
 kcard1r2c27
 K225
 kcard1r4c29
 K243
 kcard1r6c31
 K263kcard1r0c26
 K222
 kcard1r2c28
 K240
 kcard1r4c30
 K258
 kcard1r6c32
 K278kcard1r0c27
 K223
 kcard1r2c29
 K241
 kcard1r4c31
 K259
 kcard1r6c33
 K279kcard1r0c28
 K238
 kcard1r2c30
 K256
 kcard1r4c32
 K274
 kcard1r6c34
 K296kcard1r0c29
 K239
 kcard1r2c31
 K257
 kcard1r4c33
 K275
 kcard1r6c35
 K297kcard1r0c30
 K254
 kcard1r2c32
 K272
 kcard1r4c34
 K292
 kcard1r6c36
 K313kcard1r0c31
 K255
 kcard1r2c33
 K273
 kcard1r4c35
 K293
 kcard1r6c37
 K314kcard1r0c32
 K270
 kcard1r2c34
 K290
 kcard1r4c36
 K309
 kcard1r6c38
 K329kcard1r0c33
 K271
 kcard1r2c35
 K291
 kcard1r4c37
 K310
 kcard1r6c39
 K330kcard1r0c34
 K288
 kcard1r2c36
 K307
 kcard1r4c38
 K325
 kcard1r6c40
 K345kcard1r0c35
 K289
 kcard1r2c37
 K308
 kcard1r4c39
 K326
 kcard1r6c41
 K346kcard1r0c36
 K305
 kcard1r2c38
 K323
 kcard1r4c40
 K341
 kcard1r6c42
 K361kcard1r0c37
 K306
 kcard1r2c39
 K324
 kcard1r4c41
 K342
 kcard1r6c43
 K362kcard1r0c38
 K321
 kcard1r2c40
 K339
 kcard1r4c42
 K357
 kcard1r6c44
 K377kcard1r0c39
 K322
 kcard1r2c41
 K340
 kcard1r4c43
 K358
 kcard1r6c45
 K378kcard1r0c40
 K337
 kcard1r2c42
 K355
 kcard1r4c44
 K373
 kcard1r7c0
 K16kcard1r0c41
 K338
 kcard1r2c43
 K356
 kcard1r4c45
 K374
 kcard1r7c1
 K15kcard1r0c42
 K353
 kcard1r2c44
 K371
 kcard1r5c0
 K11
 kcard1r7c2
 K34kcard1r0c43
 K354
 kcard1r2c45
 K372
 kcard1r5c1
 K12
 kcard1r7c3
 K33kcard1r0c44
 K369
 kcard1r3c0
 K3
 kcard1r5c2
 K29
 kcard1r7c4
 K51kcard1r0c45
 K370
 kcard1r3c1
 K4
 kcard1r5c3
 K30
 kcard1r7c5
 K50kcard1r1c0
 K1
 kcard1r3c2
 K21
 kcard1r5c4
 K46
 kcard1r7c6
 K69kcard1r1c1
 K2
 kcard1r3c3
 K22
 kcard1r5c5
 K47
 kcard1r7c7
 K68kcard1r1c2
 K19
 kcard1r3c4
 K38
 kcard1r5c6
 K64
 kcard1r7c8
 K86kcard1r1c3
 K20
 kcard1r3c5
 K39
 kcard1r5c7
 K65
 kcard1r7c19
 K85kcard1r1c4
 K36
 kcard1r3c6
 K56
 kcard1r5c8
 K81
 kcard1r7c10
 K102kcard1r1c5
 K37
 kcard1r3c7
 K57
 kcard1r5c9
 K82
 kcard1r7c11
 K101kcard1r1c6
 K54
 kcard1r3c8
 K73
 kcard1r5c10
 K97
 kcard1r7c12
 K118kcard1r1c7
 K55
 kcard1r3c9
 K74
 kcard1r5c11
 K98
 kcard1r7c13
 K117kcard1r1c8
 K71
 kcard1r3c10
 K89
 kcard1r5c12
 K113
 kcard1r7c14
 K134kcard1r1c9
 K72
 kcard1r3c11
 K90
 kcard1r5c13
 K114
 kcard1r7c15
 K133kcard1r1c10
 K87
 kcard1r3c12
 K105
 kcard1r5c14
 K129
 kcard1r7c16
 K150kcard1r1c11
 K88
 kcard1r3c13
 K106
 kcard1r5c15
 K130
 kcard1r7c17
 K149kcard1r1c12
 K103
 kcard1r3c14
 K121
 kcard1r5c16
 K145
 kcard1r7c18
 K165kcard1r1c13
 K104
 kcard1r3c15
 K122
 kcard1r5c17
 K146
 kcard1r7c19
 K166kcard1r1c14
 K119
 kcard1r3c16
 K137
 kcard1r5c18
 K161
 kcard1r7c20
 K183kcard1r1c15
 K120
 kcard1r3c17
 K138
 kcard1r5c19
 K162
 kcard1r7c21
 K184kcard1r1c16
 K135
 kcard1r3c18
 K153
 kcard1r5c20
 K179
 kcard1r7c22
 K200kcard1r1c17
 K136
 kcard1r3c19
 K154
 kcard1r5c21
 K180
 kcard1r7c23
 K201kcard1r1c18
 K151
 kcard1r3c20
 K171
 kcard1r5c22
 K196
 kcard1r7c24
 K216kcard1r1c19
 K152
 kcard1r3c21
 K172
 kcard1r5c23
 K197
 kcard1r7c25
 K217kcard1r1c20
 K169
 kcard1r3c22
 K188
 kcard1r5c24
 K212
 kcard1r7c26
 K232kcard1r1c21
 K170
 kcard1r3c23
 K189
 kcard1r5c25
 K213
 kcard1r7c27
 K233kcard1r1c22
 K186
 kcard1r3c24
 K204
 kcard1r5c26
 K228
 kcard1r7c28
 K249kcard1r1c23
 K187
 kcard1r3c25
 K205
 kcard1r5c27
 K229
 kcard1r7c29
 K248kcard1r1c24
 K202
 kcard1r3c26
 K220
 kcard1r5c28
 K244
 kcard1r7c30
 K264kcard1r1c25
 K203
 kcard1r3c27
 K221
 kcard1r5c29
 K245
 kcard1r7c31
 K265kcard1r1c26
 K218
 kcard1r3c28
 K236
 kcard1r5c30
 K260
 kcard1r7c32
 K281kcard1r1c27
 K219
 kcard1r3c29
 K237
 kcard1r5c31
 K261
 kcard1r7c33
 K280kcard1r1c28
 K234
 kcard1r3c30
 K252
 kcard1r5c32
 K276
 kcard1r7c34
 K299kcard1r1c29
 K235
 kcard1r3c31
 K253
 kcard1r5c33
 K277
 kcard1r7c35
 K298kcard1r1c30
 K250
 kcard1r3c32
 K268
 kcard1r5c34
 K294
 kcard1r7c36
 K315kcard1r1c31
 K251
 kcard1r3c33
 K269
 kcard1r5c35
 K295
 kcard1r7c37
 K316kcard1r1c32
 K266
 kcard1r3c34
 K286
 kcard1r5c36
 K311
 kcard1r7c38
 K331kcard1r1c33
 K267
 kcard1r3c35
 K287
 kcard1r5c37
 K312
 kcard1r7c39
 K332kcard1r1c34
 K284
 kcard1r3c36
 K303
 kcard1r5c38
 K327
 kcard1r7c40
 K347kcard1r1c35
 K285
 kcard1r3c37
 K304
 kcard1r5c39
 K328
 kcard1r7c41
 K348kcard1r1c36
 K301
 kcard1r3c38
 K319
 kcard1r5c40
 K343
 kcard1r7c42
 K363kcard1r1c37
 K302
 kcard1r3c39
 K320
 kcard1r5c41
 K344
 kcard1r7c43
 K364kcard1r1c38
 K317
 kcard1r3c40
 K335
 kcard1r5c42
 K359
 kcard1r7c44
 K379kcard1r1c39
 K318
 kcard1r3c41
 K336
 kcard1r5c43
 K360
 kcard1r7c45
 K380
3. Remove the screws that hold one side of the insulator cover to the card. 
 1
 NI 28162
 Insulator Cover3
 Screws
4. Lift the insulator cover to access the relays. To replace a relay in one of the
 two rightmost columns of matrix relays, carefully peel the adhesive strip of the
 insulator cover off of these two columns of relays. 1
 NI 28162
 Insulator Cover

#### Replace the Relay

The NI 2816 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

#### Reassemble the Card

Refer to one of the following procedures to reassemble your card after replacing any
 relays.

#### Reassembly If Insulator Cover Was Not Removed

If you only replaced relays outside of the two rightmost columns of matrix relays,
 and therefore did not remove the adhesive strip of the insulator cover, complete the
 Disassemble the Card steps in reverse order to reassemble your card.

#### Reassembly If Insulator Cover Was Removed

If you removed the insulator cover, including the adhesive strip, to replace a relay
 in one of the two rightmost columns of matrix relays, complete the following steps
 to reassemble your card.

1. Use screws to attach one side of the replacement insulator cover to the card.
 1
 NI 28162
 Insulator Cover3
 Screws
2. Lift the unattached side of the replacement insulator cover and remove the liner
 from the adhesive strip. 1
 Adhesive Strip2
 Insulator Cover3
 NI 2816
3. Firmly press the adhesive strip on top of the two rightmost columns of matrix
 relays.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2816

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2816.html language=enus -->
## TOPIC 00094: NI 2816

- bundle_id: `ni-switch`
- source_path: `ni-2816.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2816.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2816A/B (NI 2816) is a high-density matrix switch card for the NI SwitchBlock. The NI 2816 is designed for combination with other NI 2816 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2816

The NI 2816A/B (NI 2816) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2816 is designed for combination with other NI 2816 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2816 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8×46 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2816 1-Wire 8×46 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2817-1-wire-16-22-matrix-topology.html language=enus -->
## TOPIC 00095: NI 2817 1-Wire 16×22 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2817-1-wire-16-22-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2817-1-wire-16-22-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2817A/B (NI 2817) in the 1-wire 16×22 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2 is

### NI 2817 1-Wire 16×22 Matrix Topology

The following figure represents the NI 2817A/B (NI 2817) in the 1-wire 16×22 matrix
 topology.

[IMAGE alt='image' src='GUID-EECB4132-23B9-45CD-BC4F-D9E937E61D92-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI 2817.

[IMAGE alt='image' src='GUID-1504491D-9E32-4F92-9585-58F2F759166D-a5.gif']

Note

TYPE A SIGNAL

(A)

TYPE B
 SIGNAL

(B)

(A)

(B)

Parent topic:

NI 2817

<!--NI_TOPIC bundle=ni-switch path=ni-2817-hardware-diagram.html language=enus -->
## TOPIC 00096: NI 2817 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2817-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2817-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2817A/B (NI 2817). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2817 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2817 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-EECB4132-23B9-45CD-BC4F-D9E937E61D92-a5.gif']

The following table lists relay names for one NI 2817 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0...kCARD1AB15 |
| kCARD1R0C0...kCARD1R0C21 |
| kCARD1R1C0...kCARD1R1C21 |
| kCARD1R2C0...kCARD1R2C21 |
| kCARD1R3C0...kCARD1R3C21 |
| kCARD1R4C0...kCARD1R4C21 |
| kCARD1R5C0...kCARD1R5C21 |
| kCARD1R6C0...kCARD1R6C21 |
| kCARD1R7C0...kCARD1R7C21 |
| kCARD1R8C0...kCARD1R8C21 |
| kCARD1R9C0...kCARD1R9C21 |
| kCARD1R10C0...kCARD1R10C21 |
| kCARD1R11C0...kCARD1R11C21 |
| kCARD1R12C0...kCARD1R12C21 |
| kCARD1R13C0...kCARD1R13C21 |
| kCARD1R14C0...kCARD1R14C21 |
| kCARD1R15C0...kCARD1R15C21 |

Parent topic:

NI 2817

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2817-multicard-topologies.html language=enus -->
## TOPIC 00097: NI 2817 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2817-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2817-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2817 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2817 Multicard Topologies

Note

must

| Number ofNI 2817 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 16×22 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 16×44 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 16×66 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 16×88 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 16×110 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 16×132 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2817

Related concepts:

- NI 2817 1-Wire 16×22 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2817-relay-replacement.html language=enus -->
## TOPIC 00098: NI 2817 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2817-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2817-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2817A/B (NI 2817) uses reed relays. The NI 2817 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacture

### NI 2817 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Coto | 9117-0001 |
| Safety (Reference Designators K18, K53, K168, K283, K381, K382, K383 and K384) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781451-10 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on your
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI 2817 Relay Map 
 [IMAGE alt='image' src='GUID-BAF4BF1C-0F31-4BF2-8DB9-BEBE48DFA3B4-a5.gif'] 
 Note The relay names in the following table correspond to a
 single-card device. Refer to the NI SwitchBlock Device Reference for
 information about relay naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K15
 kcard1r3c10
 K97
 kcard1r7c14
 K182
 kcard1r11c18
 K275kcard1ab1
 K33
 kcard1r3c11
 K98
 kcard1r7c15
 K181
 kcard1r11c19
 K274kcard1ab2
 K50
 kcard1r3c12
 K99
 kcard1r7c16
 K180
 kcard1r11c20
 K273kcard1ab3
 K68
 kcard1r3c13
 K100
 kcard1r7c17
 K179
 kcard1r11c21
 K134kcard1ab4
 K85
 kcard1r3c14
 K84
 kcard1r7c18
 K178
 kcard1r12c0
 K301kcard1ab5
 K101
 kcard1r3c15
 K83
 kcard1r7c19
 K177
 kcard1r12c1
 K302kcard1ab6
 K117
 kcard1r3c16
 K82
 kcard1r7c20
 K176
 kcard1r12c2
 K303kcard1ab7
 K133
 kcard1r3c17
 K81
 kcard1r7c21
 K69
 kcard1r12c3
 K304kcard1ab8
 K149
 kcard1r3c18
 K80
 kcard1r8c0
 K202
 kcard1r12c4
 K305kcard1ab9
 K165
 kcard1r3c19
 K79
 kcard1r8c1
 K203
 kcard1r12c5
 K306kcard1ab10
 K183
 kcard1r3c20
 K78
 kcard1r8c2
 K204
 kcard1r12c6
 K307kcard1ab11
 K200
 kcard1r3c21
 K35
 kcard1r8c3
 K205
 kcard1r12c7
 K308kcard1ab12
 K216
 kcard1r4c0
 K103
 kcard1r8c4
 K206
 kcard1r12c8
 K309kcard1ab13
 K232
 kcard1r4c1
 K104
 kcard1r8c5
 K207
 kcard1r12c9
 K310kcard1ab14
 K248
 kcard1r4c2
 K105
 kcard1r8c6
 K208
 kcard1r12c10
 K311kcard1ab15
 K264
 kcard1r4c3
 K90
 kcard1r8c7
 K209
 kcard1r12c11
 K312kcard1r0c0
 K1
 kcard1r4c4
 K91
 kcard1r8c8
 K210
 kcard1r12c12
 K313kcard1r0c1
 K2
 kcard1r4c5
 K108
 kcard1r8c9
 K211
 kcard1r12c13
 K314kcard1r0c2
 K3
 kcard1r4c6
 K109
 kcard1r8c10
 K212
 kcard1r12c14
 K317kcard1r0c3
 K4
 kcard1r4c7
 K110
 kcard1r8c11
 K213
 kcard1r12c15
 K318kcard1r0c4
 K5
 kcard1r4c8
 K111
 kcard1r8c12
 K214
 kcard1r12c16
 K319kcard1r0c5
 K6
 kcard1r4c9
 K112
 kcard1r8c13
 K215
 kcard1r12c17
 K320kcard1r0c6
 K7
 kcard1r4c10
 K113
 kcard1r8c14
 K218
 kcard1r12c18
 K321kcard1r0c7
 K8
 kcard1r4c11
 K114
 kcard1r8c15
 K219
 kcard1r12c19
 K322kcard1r0c8
 K9
 kcard1r4c12
 K115
 kcard1r8c16
 K220
 kcard1r12c20
 K323kcard1r0c9
 K10
 kcard1r4c13
 K116
 kcard1r8c17
 K221
 kcard1r12c21
 K150kcard1r0c10
 K11
 kcard1r4c14
 K119
 kcard1r8c18
 K222
 kcard1r13c0
 K333kcard1r0c11
 K12
 kcard1r4c15
 K120
 kcard1r8c19
 K223
 kcard1r13c1
 K334kcard1r0c12
 K13
 kcard1r4c16
 K121
 kcard1r8c20
 K224
 kcard1r13c2
 K335kcard1r0c13
 K14
 kcard1r4c17
 K122
 kcard1r8c21
 K70
 kcard1r13c3
 K336kcard1r0c14
 K19
 kcard1r4c18
 K123
 kcard1r9c0
 K234
 kcard1r13c4
 K337kcard1r0c15
 K20
 kcard1r4c19
 K124
 kcard1r9c1
 K235
 kcard1r13c5
 K338kcard1r0c16
 K21
 kcard1r4c20
 K125
 kcard1r9c2
 K236
 kcard1r13c6
 K339kcard1r0c17
 K22
 kcard1r4c21
 K51
 kcard1r9c3
 K237
 kcard1r13c7
 K340kcard1r0c18
 K23
 kcard1r5c0
 K135
 kcard1r9c4
 K238
 kcard1r13c8
 K341kcard1r0c19
 K24
 kcard1r5c1
 K136
 kcard1r9c5
 K239
 kcard1r13c9
 K342kcard1r0c20
 K25
 kcard1r5c2
 K137
 kcard1r9c6
 K240
 kcard1r13c10
 K343kcard1r0c21
 K16
 kcard1r5c3
 K138
 kcard1r9c7
 K241
 kcard1r13c11
 K344kcard1r1c0
 K36
 kcard1r5c4
 K139
 kcard1r9c8
 K242
 kcard1r13c12
 K345kcard1r1c1
 K37
 kcard1r5c5
 K140
 kcard1r9c9
 K243
 kcard1r13c13
 K346kcard1r1c2
 K38
 kcard1r5c6
 K141
 kcard1r9c10
 K244
 kcard1r13c14
 K330kcard1r1c3
 K39
 kcard1r5c7
 K142
 kcard1r9c11
 K245
 kcard1r13c15
 K329kcard1r1c4
 K40
 kcard1r5c8
 K143
 kcard1r9c12
 K246
 kcard1r13c16
 K328kcard1r1c5
 K41
 kcard1r5c9
 K144
 kcard1r9c13
 K247
 kcard1r13c17
 K327kcard1r1c6
 K42
 kcard1r5c10
 K145
 kcard1r9c14
 K231
 kcard1r13c18
 K326kcard1r1c7
 K43
 kcard1r5c11
 K146
 kcard1r9c15
 K230
 kcard1r13c19
 K325kcard1r1c8
 K44
 kcard1r5c12
 K147
 kcard1r9c16
 K229
 kcard1r13c20
 K324kcard1r1c9
 K45
 kcard1r5c13
 K148
 kcard1r9c17
 K228
 kcard1r13c21
 K166kcard1r1c10
 K46
 kcard1r5c14
 K132
 kcard1r9c18
 K227
 kcard1r14c0
 K349kcard1r1c11
 K47
 kcard1r5c15
 K131
 kcard1r9c19
 K226
 kcard1r14c1
 K350kcard1r1c12
 K48
 kcard1r5c16
 K130
 kcard1r9c20
 K225
 kcard1r14c2
 K351kcard1r1c13
 K49
 kcard1r5c17
 K129
 kcard1r9c21
 K86
 kcard1r14c3
 K352kcard1r1c14
 K32
 kcard1r5c18
 K128
 kcard1r10c0
 K250
 kcard1r14c4
 K353kcard1r1c15
 K31
 kcard1r5c19
 K127
 kcard1r10c1
 K251
 kcard1r14c5
 K354kcard1r1c16
 K30
 kcard1r5c20
 K126
 kcard1r10c2
 K252
 kcard1r14c6
 K355kcard1r1c17
 K29
 kcard1r5c21
 K52
 kcard1r10c3
 K253
 kcard1r14c7
 K356kcard1r1c18
 K28
 kcard1r6c0
 K151
 kcard1r10c4
 K254
 kcard1r14c8
 K357kcard1r1c19
 K27
 kcard1r6c1
 K152
 kcard1r10c5
 K255
 kcard1r14c9
 K358kcard1r1c20
 K26
 kcard1r6c2
 K153
 kcard1r10c6
 K256
 kcard1r14c10
 K359kcard1r1c21
 K17
 kcard1r6c3
 K154
 kcard1r10c7
 K257
 kcard1r14c11
 K360kcard1r2c0
 K54
 kcard1r6c4
 K155
 kcard1r10c8
 K258
 kcard1r14c12
 K361kcard1r2c1
 K55
 kcard1r6c5
 K156
 kcard1r10c9
 K259
 kcard1r14c13
 K362kcard1r2c2
 K56
 kcard1r6c6
 K157
 kcard1r10c10
 K260
 kcard1r14c14
 K280kcard1r2c3
 K39
 kcard1r6c7
 K158
 kcard1r10c11
 K261
 kcard1r14c15
 K298kcard1r2c4
 K58
 kcard1r6c8
 K159
 kcard1r10c12
 K262
 kcard1r14c16
 K315kcard1r2c5
 K59
 kcard1r6c9
 K160
 kcard1r10c13
 K263
 kcard1r14c17
 K331kcard1r2c6
 K60
 kcard1r6c10
 K161
 kcard1r10c14
 K266
 kcard1r14c18
 K347kcard1r2c7
 K61
 kcard1r6c11
 K162
 kcard1r10c15
 K267
 kcard1r14c19
 K363kcard1r2c8
 K62
 kcard1r6c12
 K163
 kcard1r10c16
 K268
 kcard1r14c20
 K379kcard1r2c9
 K63
 kcard1r6c13
 K164
 kcard1r10c17
 K269
 kcard1r14c21
 K167kcard1r2c10
 K64
 kcard1r6c14
 K169
 kcard1r10c18
 K270
 kcard1r15c0
 K365kcard1r2c11
 K65
 kcard1r6c15
 K170
 kcard1r10c19
 K271
 kcard1r15c1
 K366kcard1r2c12
 K66
 kcard1r6c16
 K171
 kcard1r10c20
 K272
 kcard1r15c2
 K367kcard1r2c13
 K67
 kcard1r6c17
 K172
 kcard1r10c21
 K102
 kcard1r15c3
 K368kcard1r2c14
 K71
 kcard1r6c18
 K173
 kcard1r11c0
 K284
 kcard1r15c4
 K369kcard1r2c15
 K31
 kcard1r6c19
 K174
 kcard1r11c1
 K285
 kcard1r15c5
 K370kcard1r2c16
 K73
 kcard1r6c20
 K175
 kcard1r11c2
 K286
 kcard1r15c6
 K371kcard1r2c17
 K74
 kcard1r6c21
 K184
 kcard1r11c3
 K287
 kcard1r15c7
 K372kcard1r2c18
 K76
 kcard1r7c0
 K186
 kcard1r11c4
 K288
 kcard1r15c8
 K373kcard1r2c19
 K76
 kcard1r7c1
 K187
 kcard1r11c5
 K289
 kcard1r15c9
 K374kcard1r2c20
 K77
 kcard1r7c2
 K188
 kcard1r11c6
 K290
 kcard1r15c10
 K375kcard1r2c21
 K34
 kcard1r7c3
 K189
 kcard1r11c7
 K291
 kcard1r15c11
 K376kcard1r3c0
 K87
 kcard1r7c4
 K190
 kcard1r11c8
 K292
 kcard1r15c12
 K377kcard1r3c1
 K88
 kcard1r7c5
 K191
 kcard1r11c9
 K293
 kcard1r15c13
 K378kcard1r3c2
 K89
 kcard1r7c6
 K192
 kcard1r11c10
 K294
 kcard1r15c14
 K281kcard1r3c3
 K90
 kcard1r7c7
 K193
 kcard1r11c11
 K295
 kcard1r15c15
 K299kcard1r3c4
 K91
 kcard1r7c8
 K194
 kcard1r11c12
 K296
 kcard1r15c16
 K316kcard1r3c5
 K92
 kcard1r7c9
 K195
 kcard1r11c13
 K297
 kcard1r15c17
 K332kcard1r3c6
 K93
 kcard1r7c10
 K196
 kcard1r11c14
 K279
 kcard1r15c18
 K348kcard1r3c7
 K94
 kcard1r7c11
 K197
 kcard1r11c15
 K278
 kcard1r15c19
 K364kcard1r3c8
 K95
 kcard1r7c12
 K198
 kcard1r11c16
 K277
 kcard1r15c20
 K380kcard1r3c9
 K96
 kcard1r7c13
 K199
 kcard1r11c17
 K276
 kcard1r15c21
 K185

#### Replace the Relay

The NI 2817 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2817

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2817.html language=enus -->
## TOPIC 00099: NI 2817

- bundle_id: `ni-switch`
- source_path: `ni-2817.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2817.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2817A/B (NI 2817) is a high-density matrix switch card for the NI SwitchBlock. The NI 2817 is designed for combination with other NI 2817 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2817

The NI 2817A/B (NI 2817) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2817 is designed for combination with other NI 2817 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2817 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 16×22 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2817 1-Wire 16×22 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2833-2-wire-4-71-matrix-topology.html language=enus -->
## TOPIC 00100: NI 2833 2-Wire 4×71 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2833-2-wire-4-71-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2833-2-wire-4-71-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2833A/B (NI 2833) in the 2-wire 4×71 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2W0 i

### NI 2833 2-Wire 4×71 Matrix Topology

The following figure represents the NI 2833A/B (NI 2833) in the 2-wire 4×71 matrix
 topology.

[IMAGE alt='image' src='GUID-5CD9B13F-1397-4E3E-9A54-48074EAD718C-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2W0 is routed to C1W0

signal connected to CARD1R2W1 is routed to C1W1

#### Pinout

The following figure identifies the pins for the NI 2833.

[IMAGE alt='image' src='GUID-75616A67-4B05-4ED8-8389-4D21B4AC0EAC-a5.gif']

Note

TYPE A SIGNAL

TYPE B SIGNAL

Parent topic:

NI 2833

<!--NI_TOPIC bundle=ni-switch path=ni-2833-hardware-diagram.html language=enus -->
## TOPIC 00101: NI 2833 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2833-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2833-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2833A/B (NI 2833). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2833 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2833 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-5CD9B13F-1397-4E3E-9A54-48074EAD718C-a5.gif']

The following table lists relay names for one NI 2833 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0...kCARD1AB3 |
| kCARD1R0C0...kCARD1R0C70 |
| kCARD1R1C0...kCARD1R1C70 |
| kCARD1R2C0...kCARD1R2C70 |
| kCARD1R3C0...kCARD1R3C70 |

Parent topic:

NI 2833

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2833-multicard-topologies.html language=enus -->
## TOPIC 00102: NI 2833 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2833-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2833-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2833 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2833 Multicard Topologies

Note

must

| Number ofNI 2833 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 2-Wire 4×71 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 2-Wire 4×142 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 2-Wire 4×213 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2833

Related concepts:

- NI 2833 2-Wire 4×71 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2833-relay-replacement.html language=enus -->
## TOPIC 00103: NI 2833 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2833-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2833-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2833A/B (NI 2833) uses electromechanical relays. The NI 2833 uses a custom lead length to meet safety standards. Trim leads according to rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. R

### NI 2833 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Tyco Electronics | 7-1462039-8 |
| Safety (Reference Designators K10, K20, K30, and K40) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781678-01 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on an
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to the PXI
 chassis. Note Properly grounding yourself prevents damage to the
 card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. NI 2833 PCB1 Relay Map 
 [IMAGE alt='image' src='GUID-23B58F5B-DEC7-4EC9-8CC4-644657C44338-a5.gif'] 
 NI 2833 PCB2 Relay Map 
 [IMAGE alt='image' src='GUID-02DA6DFD-113D-4FF8-B1E3-760D37877F07-a5.gif'] 
 The relay names in the following table correspond to a single-card device.
 Refer to the NI SwitchBlock Device Reference for information about relay
 naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K9
 kcard1r0c68
 K343
 kcard1r1c69
 K314
 kcard1r2c70
 K304kcard1ab1
 K29
 kcard1r0c69
 K334
 kcard1r1c70
 K324
 kcard1r3c0
 K264kcard1ab2
 K49
 kcard1r0c70
 K344
 kcard1r2c0
 K243
 kcard1r3c1
 K253kcard1ab3
 K50
 kcard1r1c0
 K232
 kcard1r2c1
 K254
 kcard1r3c2
 K263kcard1r0c0
 K210
 kcard1r1c1
 K220
 kcard1r2c2
 K242
 kcard1r3c3
 K262kcard1r0c1
 K221
 kcard1r1c2
 K231
 kcard1r2c3
 K241
 kcard1r3c4
 K251kcard1r0c2
 K209
 kcard1r1c3
 K230
 kcard1r2c4
 K252
 kcard1r3c5
 K261kcard1r0c3
 K208
 kcard1r1c4
 K218
 kcard1r2c5
 K240
 kcard1r3c6
 K260kcard1r0c4
 K219
 kcard1r1c5
 K229
 kcard1r2c6
 K239
 kcard1r3c7
 K51kcard1r0c5
 K207
 kcard1r1c6
 K228
 kcard1r2c7
 K31
 kcard1r3c8
 K61kcard1r0c6
 K206
 kcard1r1c7
 K11
 kcard1r2c8
 K41
 kcard1r3c9
 K249kcard1r0c7
 K1
 kcard1r1c8
 K21
 kcard1r2c9
 K250
 kcard1r3c10
 K42kcard1r0c8
 K2
 kcard1r1c9
 K227
 kcard1r2c10
 K22
 kcard1r3c11
 K52kcard1r0c9
 K217
 kcard1r1c10
 K3
 kcard1r2c11
 K32
 kcard1r3c12
 K43kcard1r0c10
 K4
 kcard1r1c11
 K12
 kcard1r2c12
 K23
 kcard1r3c13
 K53kcard1r0c11
 K13
 kcard1r1c12
 K24
 kcard1r2c13
 K33
 kcard1r3c14
 K44kcard1r0c12
 K5
 kcard1r1c13
 K34
 kcard1r2c14
 K45
 kcard1r3c15
 K54kcard1r0c13
 K14
 kcard1r1c14
 K25
 kcard1r2c15
 K55
 kcard1r3c16
 K46kcard1r0c14
 K6
 kcard1r1c15
 K35
 kcard1r2c16
 K26
 kcard1r3c17
 K36kcard1r0c15
 K15
 kcard1r1c16
 K27
 kcard1r2c17
 K16
 kcard1r3c18
 K47kcard1r0c16
 K7
 kcard1r1c17
 K37
 kcard1r2c18
 K48
 kcard1r3c19
 K57kcard1r0c17
 K17
 kcard1r1c18
 K28
 kcard1r2c19
 K58
 kcard1r3c20
 K60kcard1r0c18
 K8
 kcard1r1c19
 K38
 kcard1r2c20
 K59
 kcard1r3c21
 K71kcard1r0c19
 K18
 kcard1r1c20
 K39
 kcard1r2c21
 K82
 kcard1r3c22
 K70kcard1r0c20
 K19
 kcard1r1c21
 K136
 kcard1r2c22
 K92
 kcard1r3c23
 K81kcard1r0c21
 K137
 kcard1r1c22
 K114
 kcard1r2c23
 K103
 kcard1r3c24
 K69kcard1r0c22
 K148
 kcard1r1c23
 K125
 kcard1r2c24
 K91
 kcard1r3c25
 K80kcard1r0c23
 K147
 kcard1r1c24
 K113
 kcard1r2c25
 K102
 kcard1r3c26
 K68kcard1r0c24
 K135
 kcard1r1c25
 K124
 kcard1r2c26
 K90
 kcard1r3c27
 K79kcard1r0c25
 K146
 kcard1r1c26
 K112
 kcard1r2c27
 K101
 kcard1r3c28
 K67kcard1r0c26
 K134
 kcard1r1c27
 K123
 kcard1r2c28
 K89
 kcard1r3c29
 K78kcard1r0c27
 K145
 kcard1r1c28
 K111
 kcard1r2c29
 K100
 kcard1r3c30
 K56kcard1r0c28
 K133
 kcard1r1c29
 K122
 kcard1r2c30
 K77
 kcard1r3c31
 K66kcard1r0c29
 K144
 kcard1r1c30
 K99
 kcard1r2c31
 K88
 kcard1r3c32
 K65kcard1r0c30
 K121
 kcard1r1c31
 K110
 kcard1r2c32
 K87
 kcard1r3c33
 K76kcard1r0c31
 K132
 kcard1r1c32
 K109
 kcard1r2c33
 K98
 kcard1r3c34
 K64kcard1r0c32
 K131
 kcard1r1c33
 K120
 kcard1r2c34
 K86
 kcard1r3c35
 K75kcard1r0c33
 K143
 kcard1r1c34
 K108
 kcard1r2c35
 K97
 kcard1r3c36
 K63kcard1r0c34
 K130
 kcard1r1c35
 K119
 kcard1r2c36
 K85
 kcard1r3c37
 K74kcard1r0c35
 K142
 kcard1r1c36
 K107
 kcard1r2c37
 K96
 kcard1r3c38
 K62kcard1r0c36
 K129
 kcard1r1c37
 K118
 kcard1r2c38
 K84
 kcard1r3c39
 K73kcard1r0c37
 K141
 kcard1r1c38
 K106
 kcard1r2c39
 K95
 kcard1r3c40
 K72kcard1r0c38
 K128
 kcard1r1c39
 K117
 kcard1r2c40
 K105
 kcard1r3c41
 K83kcard1r0c39
 K140
 kcard1r1c40
 K116
 kcard1r2c41
 K104
 kcard1r3c42
 K94kcard1r0c40
 K139
 kcard1r1c41
 K127
 kcard1r2c42
 K93
 kcard1r3c43
 K248kcard1r0c41
 K126
 kcard1r1c42
 K115
 kcard1r2c43
 K238
 kcard1r3c44
 K258kcard1r0c42
 K138
 kcard1r1c43
 K215
 kcard1r2c44
 K237
 kcard1r3c45
 K257kcard1r0c43
 K216
 kcard1r1c44
 K226
 kcard1r2c45
 K236
 kcard1r3c46
 K246kcard1r0c44
 K205
 kcard1r1c45
 K225
 kcard1r2c46
 K247
 kcard1r3c47
 K256kcard1r0c45
 K204
 kcard1r1c46
 K213
 kcard1r2c47
 K235
 kcard1r3c48
 K255kcard1r0c46
 K214
 kcard1r1c47
 K224
 kcard1r2c48
 K234
 kcard1r3c49
 K265kcard1r0c47
 K203
 kcard1r1c48
 K223
 kcard1r2c49
 K245
 kcard1r3c50
 K244kcard1r0c48
 K202
 kcard1r1c49
 K211
 kcard1r2c50
 K233
 kcard1r3c51
 K275kcard1r0c49
 K212
 kcard1r1c50
 K222
 kcard1r2c51
 K295
 kcard1r3c52
 K285kcard1r0c50
 K201
 kcard1r1c51
 K315
 kcard1r2c52
 K305
 kcard1r3c53
 K266kcard1r0c51
 K335
 kcard1r1c52
 K325
 kcard1r2c53
 K286
 kcard1r3c54
 K276kcard1r0c52
 K336
 kcard1r1c53
 K306
 kcard1r2c54
 K296
 kcard1r3c55
 K267kcard1r0c53
 K326
 kcard1r1c54
 K316
 kcard1r2c55
 K287
 kcard1r3c56
 K277kcard1r0c54
 K337
 kcard1r1c55
 K307
 kcard1r2c56
 K297
 kcard1r3c57
 K268kcard1r0c55
 K327
 kcard1r1c56
 K317
 kcard1r2c57
 K288
 kcard1r3c58
 K278kcard1r0c56
 K338
 kcard1r1c57
 K308
 kcard1r2c58
 K298
 kcard1r3c59
 K259kcard1r0c57
 K328
 kcard1r1c58
 K318
 kcard1r2c59
 K279
 kcard1r3c60
 K269kcard1r0c58
 K339
 kcard1r1c59
 K299
 kcard1r2c60
 K289
 kcard1r3c61
 K270kcard1r0c59
 K319
 kcard1r1c60
 K309
 kcard1r2c61
 K290
 kcard1r3c62
 K280kcard1r0c60
 K329
 kcard1r1c61
 K310
 kcard1r2c62
 K300
 kcard1r3c63
 K271kcard1r0c61
 K330
 kcard1r1c62
 K320
 kcard1r2c63
 K291
 kcard1r3c64
 K281kcard1r0c62
 K340
 kcard1r1c63
 K311
 kcard1r2c64
 K301
 kcard1r3c65
 K272kcard1r0c63
 K331
 kcard1r1c64
 K321
 kcard1r2c65
 K292
 kcard1r3c66
 K282kcard1r0c64
 K341
 kcard1r1c65
 K312
 kcard1r2c66
 K302
 kcard1r3c67
 K273kcard1r0c65
 K332
 kcard1r1c66
 K322
 kcard1r2c67
 K293
 kcard1r3c68
 K283kcard1r0c66
 K342
 kcard1r1c67
 K313
 kcard1r2c68
 K303
 kcard1r3c69
 K274kcard1r0c67
 K333
 kcard1r1c68
 K323
 kcard1r2c69
 K294
 kcard1r3c70
 K284

#### Disassemble the Card

Complete the following steps to disassemble the NI 2833.

1. Remove the six screws from the top of PCB1.
2. Gently separate PCB1 and PCB2. 
 1
 PCB12
 PCB23
 Screws

#### Replace the Relay

The NI 2833 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

#### Reassemble the Card

Complete the Disassemble the Card steps in reverse order to reassemble your switch
 module.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2833

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2833.html language=enus -->
## TOPIC 00104: NI 2833

- bundle_id: `ni-switch`
- source_path: `ni-2833.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2833.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2833A/B (NI 2833) is a high-density matrix switch card for the NI SwitchBlock. The NI 2833 is designed for combination with other NI 2833 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2833

The NI 2833A/B (NI 2833) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2833 is designed for combination with other NI 2833 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2833 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 4×71 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2833 2-Wire 4×71 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2834-2-wire-8-34-matrix-topology.html language=enus -->
## TOPIC 00105: NI 2834 2-Wire 8×34 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2834-2-wire-8-34-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2834-2-wire-8-34-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2834A/B (NI 2834) in the 2-Wire 8×34 Matrix Topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to CARD1R2W0 i

### NI 2834 2-Wire 8×34 Matrix Topology

The following figure represents the NI 2834A/B (NI 2834) in the 2-Wire 8×34 Matrix
 Topology.

[IMAGE alt='image' src='GUID-0DD70CE5-8DF4-45C6-9F1D-759C503914A7-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to CARD1R2W0 is routed to C1W0

signal connected to CARD1R2W1 is routed to C1W1

#### Pinout

The following figure identifies the pins for the NI 2834.

[IMAGE alt='image' src='GUID-7146AEC7-7844-4295-B0E2-46D15D2C9FFD-a5.gif']

Note

TYPE A SIGNAL

TYPE B SIGNAL

Parent topic:

NI 2834

<!--NI_TOPIC bundle=ni-switch path=ni-2834-hardware-diagram.html language=enus -->
## TOPIC 00106: NI 2834 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2834-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2834-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2834A/B (NI 2834). Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2834 card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards

### NI 2834 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-0DD70CE5-8DF4-45C6-9F1D-759C503914A7-a5.gif']

The following table lists relay names for one NI 2834 card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0...kCARD1AB7 |
| kCARD1R0C0...kCARD1R0C33 |
| kCARD1R1C0...kCARD1R1C33 |
| kCARD1R2C0...kCARD1R2C33 |
| kCARD1R3C0...kCARD1R3C33 |
| kCARD1R4C0...kCARD1R0C33 |
| kCARD1R5C0...kCARD1R1C33 |
| kCARD1R6C0...kCARD1R2C33 |
| kCARD1R7C0...kCARD1R3C33 |

Parent topic:

NI 2834

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2834-multicard-topologies.html language=enus -->
## TOPIC 00107: NI 2834 Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2834-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2834-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2834 NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABLE

### NI 2834 Multicard Topologies

Note

must

| Number ofNI 2834 Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 2-Wire 8×34 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 2-Wire 8×68 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 2-Wire 8×102 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2834

Related concepts:

- NI 2834 2-Wire 8×34 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2834-relay-replacement.html language=enus -->
## TOPIC 00108: NI 2834 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-2834-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2834-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2834A/B (NI 2834) uses electromechanical relays. The NI 2834 uses a custom lead length to meet safety standards. Trim leads according to rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. R

### NI 2834 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| Matrix | Tyco Electronics | 7-1462039-8 |
| Safety (Reference Designators K10, K20, K30, K40, K50, K60, K70, and K80) | Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781678-01 |
| National Instruments (10 safety relays) | 781089-10 |

Complete the following sets of steps to locate and replace a failed relay on an
 NI SwitchBlock card.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to the PXI
 chassis. Note Properly grounding yourself prevents damage to the
 card from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. NI 2834 PCB1 Relay Map 
 [IMAGE alt='image' src='GUID-A98B30FB-59C1-4C02-B42F-671BAFB2822E-a5.gif'] 
 NI 2834 PCB2 Relay Map 
 [IMAGE alt='image' src='GUID-EC24CD60-FF7D-4BA8-8EC5-175AEA08F8EF-a5.gif'] 
 The relay names in the following table correspond to a single-card device.
 Refer to the NI SwitchBlock Device Reference for information about relay
 naming for multicard devices. 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkcard1ab0
 K19
 kcard1r1c28
 K225
 kcard1r3c30
 K256
 kcard1r5c32
 K285kcard1ab1
 K29
 kcard1r1c29
 K214
 kcard1r3c31
 K266
 kcard1r5c33
 K295kcard1ab2
 K49
 kcard1r1c30
 K224
 kcard1r3c32
 K245
 kcard1r6c0
 K313kcard1ab3
 K69
 kcard1r1c31
 K223
 kcard1r3c33
 K255
 kcard1r6c1
 K324kcard1ab4
 K90
 kcard1r1c32
 K212
 kcard1r4c0
 K283
 kcard1r6c2
 K323kcard1ab5
 K112
 kcard1r1c33
 K222
 kcard1r4c1
 K294
 kcard1r6c3
 K312kcard1ab6
 K123
 kcard1r2c0
 K264
 kcard1r4c2
 K293
 kcard1r6c4
 K322kcard1ab7
 K134
 kcard1r2c1
 K254
 kcard1r4c3
 K282
 kcard1r6c5
 K124kcard1r0c0
 K221
 kcard1r2c2
 K253
 kcard1r4c4
 K272
 kcard1r6c6
 K114kcard1r0c1
 K210
 kcard1r2c3
 K263
 kcard1r4c5
 K102
 kcard1r6c7
 K126kcard1r0c2
 K209
 kcard1r2c4
 K241
 kcard1r4c6
 K81
 kcard1r6c8
 K115kcard1r0c3
 K220
 kcard1r2c5
 K51
 kcard1r4c7
 K92
 kcard1r6c9
 K331kcard1r0c4
 K208
 kcard1r2c6
 K41
 kcard1r4c8
 K82
 kcard1r6c10
 K321kcard1r0c5
 K1
 kcard1r2c7
 K31
 kcard1r4c9
 K281
 kcard1r6c11
 K105kcard1r0c6
 K2
 kcard1r2c8
 K52
 kcard1r4c10
 K291
 kcard1r6c12
 K116kcard1r0c7
 K3
 kcard1r2c9
 K240
 kcard1r4c11
 K63
 kcard1r6c13
 K106kcard1r0c8
 K12
 kcard1r2c10
 K251
 kcard1r4c12
 K73
 kcard1r6c14
 K117kcard1r0c9
 K219
 kcard1r2c11
 K43
 kcard1r4c13
 K74
 kcard1r6c15
 K118kcard1r0c10
 K207
 kcard1r2c12
 K33
 kcard1r4c14
 K84
 kcard1r6c16
 K320kcard1r0c11
 K4
 kcard1r2c13
 K44
 kcard1r4c15
 K75
 kcard1r6c17
 K107kcard1r0c12
 K13
 kcard1r2c14
 K55
 kcard1r4c16
 K290
 kcard1r6c18
 K119kcard1r0c13
 K5
 kcard1r2c15
 K45
 kcard1r4c17
 K76
 kcard1r6c19
 K131kcard1r0c14
 K14
 kcard1r2c16
 K250
 kcard1r4c18
 K86
 kcard1r6c20
 K309kcard1r0c15
 K6
 kcard1r2c17
 K36
 kcard1r4c19
 K87
 kcard1r6c21
 K141kcard1r0c16
 K206
 kcard1r2c18
 K46
 kcard1r4c20
 K279
 kcard1r6c22
 K100kcard1r0c17
 K15
 kcard1r2c19
 K47
 kcard1r4c21
 K98
 kcard1r6c23
 K122kcard1r0c18
 K16
 kcard1r2c20
 K260
 kcard1r4c22
 K99
 kcard1r6c24
 K319kcard1r0c19
 K7
 kcard1r2c21
 K57
 kcard1r4c23
 K88
 kcard1r6c25
 K101kcard1r0c20
 K217
 kcard1r2c22
 K48
 kcard1r4c24
 K269
 kcard1r6c26
 K308kcard1r0c21
 K17
 kcard1r2c23
 K58
 kcard1r4c25
 K89
 kcard1r6c27
 K318kcard1r0c22
 K8
 kcard1r2c24
 K249
 kcard1r4c26
 K288
 kcard1r6c28
 K307kcard1r0c23
 K18
 kcard1r2c25
 K59
 kcard1r4c27
 K278
 kcard1r6c29
 K317kcard1r0c24
 K216
 kcard1r2c26
 K237
 kcard1r4c28
 K267
 kcard1r6c30
 K316kcard1r0c25
 K9
 kcard1r2c27
 K248
 kcard1r4c29
 K277
 kcard1r6c31
 K326kcard1r0c26
 K205
 kcard1r2c28
 K236
 kcard1r4c30
 K276
 kcard1r6c32
 K305kcard1r0c27
 K215
 kcard1r2c29
 K246
 kcard1r4c31
 K286
 kcard1r6c33
 K315kcard1r0c28
 K204
 kcard1r2c30
 K235
 kcard1r4c32
 K265
 kcard1r7c0
 K344kcard1r0c29
 K213
 kcard1r2c31
 K234
 kcard1r4c33
 K275
 kcard1r7c1
 K334kcard1r0c30
 K203
 kcard1r2c32
 K244
 kcard1r5c0
 K314
 kcard1r7c2
 K333kcard1r0c31
 K202
 kcard1r2c33
 K233
 kcard1r5c1
 K304
 kcard1r7c3
 K343kcard1r0c32
 K211
 kcard1r3c0
 K284
 kcard1r5c2
 K303
 kcard1r7c4
 K342kcard1r0c33
 K201
 kcard1r3c1
 K274
 kcard1r5c3
 K302
 kcard1r7c5
 K135kcard1r1c0
 K243
 kcard1r3c2
 K273
 kcard1r5c4
 K292
 kcard1r7c6
 K136kcard1r1c1
 K232
 kcard1r3c3
 K262
 kcard1r5c5
 K113
 kcard1r7c7
 K125kcard1r1c2
 K231
 kcard1r3c4
 K252
 kcard1r5c6
 K103
 kcard1r7c8
 K137kcard1r1c3
 K242
 kcard1r3c5
 K91
 kcard1r5c7
 K93
 kcard1r7c9
 K332kcard1r1c4
 K230
 kcard1r3c6
 K61
 kcard1r5c8
 K104
 kcard1r7c10
 K341kcard1r1c5
 K11
 kcard1r3c7
 K71
 kcard1r5c9
 K301
 kcard1r7c11
 K127kcard1r1c6
 K21
 kcard1r3c8
 K72
 kcard1r5c10
 K311
 kcard1r7c12
 K138kcard1r1c7
 K32
 kcard1r3c9
 K261
 kcard1r5c11
 K83
 kcard1r7c13
 K128kcard1r1c8
 K22
 kcard1r3c10
 K271
 kcard1r5c12
 K94
 kcard1r7c14
 K139kcard1r1c9
 K218
 kcard1r3c11
 K62
 kcard1r5c13
 K95
 kcard1r7c15
 K129kcard1r1c10
 K229
 kcard1r3c12
 K53
 kcard1r5c14
 K85
 kcard1r7c16
 K330kcard1r1c11
 K42
 kcard1r3c13
 K64
 kcard1r5c15
 K96
 kcard1r7c17
 K140kcard1r1c12
 K23
 kcard1r3c14
 K54
 kcard1r5c16
 K300
 kcard1r7c18
 K130kcard1r1c13
 K24
 kcard1r3c15
 K65
 kcard1r5c17
 K108
 kcard1r7c19
 K132kcard1r1c14
 K34
 kcard1r3c16
 K270
 kcard1r5c18
 K97
 kcard1r7c20
 K340kcard1r1c15
 K25
 kcard1r3c17
 K56
 kcard1r5c19
 K109
 kcard1r7c21
 K142kcard1r1c16
 K228
 kcard1r3c18
 K66
 kcard1r5c20
 K310
 kcard1r7c22
 K133kcard1r1c17
 K35
 kcard1r3c19
 K67
 kcard1r5c21
 K120
 kcard1r7c23
 K143kcard1r1c18
 K26
 kcard1r3c20
 K280
 kcard1r5c22
 K110
 kcard1r7c24
 K329kcard1r1c19
 K27
 kcard1r3c21
 K77
 kcard1r5c23
 K121
 kcard1r7c25
 K144kcard1r1c20
 K239
 kcard1r3c22
 K68
 kcard1r5c24
 K299
 kcard1r7c26
 K328kcard1r1c21
 K37
 kcard1r3c23
 K78
 kcard1r5c25
 K111
 kcard1r7c27
 K339kcard1r1c22
 K28
 kcard1r3c24
 K259
 kcard1r5c26
 K289
 kcard1r7c28
 K327kcard1r1c23
 K38
 kcard1r3c25
 K79
 kcard1r5c27
 K298
 kcard1r7c29
 K338kcard1r1c24
 K227
 kcard1r3c26
 K258
 kcard1r5c28
 K287
 kcard1r7c30
 K337kcard1r1c25
 K39
 kcard1r3c27
 K268
 kcard1r5c29
 K297
 kcard1r7c31
 K325kcard1r1c26
 K238
 kcard1r3c28
 K257
 kcard1r5c30
 K296
 kcard1r7c32
 K336kcard1r1c27
 K226
 kcard1r3c29
 K247
 kcard1r5c31
 K306
 kcard1r7c33
 K335

#### Disassemble the Card

Complete the following steps to disassemble the NI 2834.

1. Remove the six screws from the top of PCB1.
2. Gently separate PCB1 and PCB2. 1
 PCB12
 PCB23
 Screws

#### Replace the Relay

The NI 2834 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 0.5 mm (0.02 inch) from the PCB.

#### Reassemble the Card

Complete the Disassemble the Card steps in reverse order to reassemble your switch
 module.

Tip

Switch Soft Front
 Panel Help

Parent topic:

NI 2834

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2834.html language=enus -->
## TOPIC 00109: NI 2834

- bundle_id: `ni-switch`
- source_path: `ni-2834.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2834.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2834A/B (NI 2834) is a high-density matrix switch card for the NI SwitchBlock. The NI 2834 is designed for combination with other NI 2834 cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding

### NI 2834

The NI 2834A/B (NI 2834) is a high-density matrix switch card for the NI SwitchBlock. The
 NI 2834 is designed for combination with other NI 2834 cards to create a customized
 NI SwitchBlock multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2834 and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 8×34 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI 2834 2-Wire 8×34 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-2865a-1-wire-4-84-matrix-topology.html language=enus -->
## TOPIC 00110: NI 2865A 1-Wire 4×84 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-2865a-1-wire-4-84-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2865a-1-wire-4-84-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI 2865A in the 1-wire 4×84 matrix topology. Making a Connection The immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters card1r2 and c1, results in the following connection: signal connected to card1r2 is routed to c1

### NI 2865A 1-Wire 4×84 Matrix Topology

The following figure represents the NI 2865A in the 1-wire 4×84 matrix topology.

[IMAGE alt='image' src='GUID-6BFE524E-5D64-4403-9046-B008838ED067-a5.gif']

#### Making a Connection

The immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters card1r2 and c1, results
 in the following connection:

signal connected to card1r2 is routed to c1

#### Pinout

The following figure identifies the pins for the NI 2865A.

[IMAGE alt='image' src='GUID-E9D3F85F-0F9A-46FE-8E90-FB8030D6DA49-a5.gif']

Parent topic:

NI 2865A

<!--NI_TOPIC bundle=ni-switch path=ni-2865a-hardware-diagram.html language=enus -->
## TOPIC 00111: NI 2865A Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-2865a-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2865a-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI 2865A. Hardware relay names are for the topology of a single-card device. The following table lists relay names for one NI 2865A card. Refer to the NI SwitchBlock Device Reference for channel and relay naming when multiple cards are combin

### NI 2865A Hardware Diagram

Note

[IMAGE alt='image' src='GUID-6BFE524E-5D64-4403-9046-B008838ED067-a5.gif']

The following table lists relay names for one NI 2865A card. Refer to the NI SwitchBlock
 Device Reference for channel and relay naming when multiple cards are combined.

| Relays |
| --- |
| kCARD1AB0 |
| kCARD1AB1 |
| kCARD1AB2 |
| kCARD1AB3 |
| kCARD1BP0 |
| kCARD1BP1 |
| kCARD1BP2 |
| kCARD1BP3 |
| kCARD1R0C0...kCARD1R0C83 |
| kCARD1R1C0...kCARD1R1C83 |
| kCARD1R2C0...kCARD1R2C83 |
| kCARD1R3C0...kCARD1R3C83 |

Parent topic:

NI 2865A

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2865a-multicard-topologies.html language=enus -->
## TOPIC 00112: NI 2865A Multicard Topologies

- bundle_id: `ni-switch`
- source_path: `ni-2865a-multicard-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2865a-multicard-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists possible topologies for an NI 2865A NI SwitchBlock device. Refer to Initializing with Topology for NI SwitchBlock Devices for information about using the Configured Topology and NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names. You must connect pin 96 (INTERLOCK ENABL

### NI 2865A Multicard Topologies

Note

must

| Number ofNI 2865A Cards | Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- | --- |
| 1 | 1-Wire 4×84 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 2 | 1-Wire 4×168 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 3 | 1-Wire 4×252 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 4 | 1-Wire 4×336 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 5 | 1-Wire 4×420 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |
| 6 | 1-Wire 4×504 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

Refer to the NI SwitchBlock Device Reference for information about creating multicard
 devices.

Parent topic:

NI 2865A

Related concepts:

- NI 2865A 1-Wire 4×84 Matrix Topology
- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-2865a.html language=enus -->
## TOPIC 00113: NI 2865A

- bundle_id: `ni-switch`
- source_path: `ni-2865a.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-2865a.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 2865A is a high-density matrix switch card for the NI SwitchBlock. The NI 2865A is designed for combination with other NI 2865A cards to create a customized NI SwitchBlock multicard device. For certain applications, you may need to increase the default settling time. Refer to Adding Additiona

### NI 2865A

The NI 2865A is a high-density matrix switch card for the NI SwitchBlock. The NI 2865A is
 designed for combination with other NI 2865A cards to create a customized NI SwitchBlock
 multicard device.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2865A and possible
 operation modes. Refer to Initializing with Topology for NI SwitchBlock Devices for
 information about using the Configured Topology and
 NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY software names.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×84 Matrix | Configured Topology(NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY) |  | — |

#### Related Topics

Matrix

NI SwitchBlock Switching Considerations

Settling Time

Operation Modes

Integration and System Considerations<

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Settling Time
- Adding Additional Settling Time
- Reed Relay Protection
- Protecting NI Switch Products when Switching Inductive Loads
- NI 2865A 1-Wire 4×84 Matrix Topology
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-1-wire-48-1-amplified-multiplexer.html language=enus -->
## TOPIC 00114: NI PXI-2501 1-Wire 48×1 Amplified Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-1-wire-48-1-amplified-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-1-wire-48-1-amplified-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501 as a 1-wire 48×1 amplified multiplexer, connect your signals using the NI TB-2605 terminal block. The following figure is a representation of the NI PXI-2501 in this mode. The NI PXI-2501 in this topology operates the same way as the 1-wire 48×1 multiplexer topology except

### NI PXI-2501 1-Wire 48×1 Amplified Multiplexer Topology

When using the NI PXI-2501 as a 1-wire 48×1 amplified multiplexer, connect your signals
 using the NI TB-2605 terminal block. The following figure is a representation of the
 NI PXI-2501 in this mode.

|  |
| --- |

The NI PXI-2501 in this topology operates the same way as the 1-wire 48×1 multiplexer
 topology except that an amplifier, indicated in the figure above, can be used.

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- NI PXI-2501 Amplifier
- Multiplexer
- NI PXI-2501/2503 1-Wire 48×1 Multiplexer Topology

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2-wire-24-1-amplified-multiplexer.html language=enus -->
## TOPIC 00115: NI PXI-2501 2-Wire 24×1 Amplified Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2-wire-24-1-amplified-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2-wire-24-1-amplified-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501 as a 2-wire 24×1 amplified multiplexer, connect your signals using the NI TB-2605 terminal block. In this topology, you can connect to a cold-junction sensor channel for cold-junction compensation. The following figure is a representation of the NI PXI-2501 in this mode. T

### NI PXI-2501 2-Wire 24×1 Amplified Multiplexer Topology

When using the NI PXI-2501 as a 2-wire 24×1 amplified multiplexer, connect your signals
 using the NI TB-2605 terminal block. In this topology, you can connect to a
 cold-junction sensor channel for cold-junction compensation. The following figure is a
 representation of the NI PXI-2501 in this mode.

|  |
| --- |

The NI PXI-2501 in this topology operates the same way as the 2-wire 24×1 multiplexer
 topology except that an amplifier, indicated in the figure above, can be used.

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- NI PXI-2501 Amplifier
- Multiplexer
- Cold-Junction Temperature Sensor Channel
- NI PXI-2501/2503 2-Wire 24×1 Multiplexer Topology

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-1-wire-48-1-multiplexer-topo.html language=enus -->
## TOPIC 00116: NI PXI-2501/2503 1-Wire 48×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-1-wire-48-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-1-wire-48-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 1-wire 48×1 multiplexer, connect your signals using the NI TB-2605 terminal block. The following figure is a representation of the NI PXI-2501/2503 in this mode. Making a Connection In 1-wire mode, all channels can connect to COM0+. COM0– is always connected to 1

### NI PXI-2501/2503 1-Wire 48×1 Multiplexer Topology

When using the NI PXI-2501/2503 as a 1-wire 48×1 multiplexer, connect your signals using
 the NI TB-2605 terminal block. The following figure is a representation of the
 NI PXI-2501/2503 in this mode.

|  |
| --- |

#### Making a Connection

In 1-wire mode, all channels can connect to COM0+. COM0– is always connected to
 1_WIRE_LO_REF and can optionally be used to route the second wire of a different
 signal (for example, the LO terminal of a DMM) through the switch.

During scanning, an example scan list entry is ch2->com0;. This
 entry routes the signal connected to ch2 to COM0+.

During immediate operations when calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with ch2 and com0, the signal connected
 to ch2 is routed to COM0+. To route the signals to AB0, use the niSwitch Connect
 Channels VI or the niSwitch_Connect function with
 com0 and ab0.

#### Pinout

The following figure and tables identify the pins for the NI PXI-2501/2503 in the
 1-wire 48×1 multiplexer topology.

[IMAGE alt='image' src='GUID-8BB2DD41-5134-4F6D-913E-15CB2D715CEC-a5.gif']

Caution

#### Pinout

| Software Name | PXI-2501/2503 Connector Pin Number | NI TB-2605 Terminal Name |
| --- | --- | --- |
| ch0 | 67 | CH0 |
| ch1 | 66 | CH1 |
| ch2 | 65 | CH2 |
| ch3 | 64 | CH3 |
| ch4 | 63 | CH4 |
| ch5 | 62 | CH5 |
| ch6 | 59 | CH6 |
| ch7 | 58 | CH7 |
| ch8 | 57 | CH8 |
| ch9 | 55 | CH9 |
| ch10 | 54 | CH10 |
| ch11 | 53 | CH11 |
| ch12 | 50 | CH12 |
| ch13 | 49 | CH13 |
| ch14 | 48 | CH14 |
| ch15 | 47 | CH15 |
| ch16 | 46 | CH16 |
| ch17 | 45 | CH17 |
| ch18 | 40 | CH18 |
| ch19 | 39 | CH19 |
| ch20 | 38 | CH20 |
| ch21 | 37 | CH21 |
| ch22 | 36 | CH22 |
| ch23 | 35 | CH23 |
| ch24 | 33 | CH24 |
| ch25 | 32 | CH25 |
| ch26 | 31 | CH26 |
| ch27 | 30 | CH27 |
| ch28 | 29 | CH28 |
| ch29 | 28 | CH29 |
| ch30 | 25 | CH30 |
| ch31 | 24 | CH31 |
| ch32 | 23 | CH32 |
| ch33 | 21 | CH33 |
| ch34 | 20 | CH34 |
| ch35 | 19 | CH35 |
| ch36 | 16 | CH36 |
| ch37 | 15 | CH37 |
| ch38 | 14 | CH38 |
| ch39 | 13 | CH39 |
| ch40 | 12 | CH40 |
| ch41 | 11 | CH41 |
| ch42 | 6 | CH42 |
| ch43 | 5 | CH43 |
| ch44 | 4 | CH44 |
| ch45 | 3 | CH45 |
| ch46 | 2 | CH46 |
| ch47 | 1 | CH47 |
| 1wire | 22 | 1wireREF |
| com0 | 61 | COM0+ |
| com0 | 27 | COM0– |
| ab0 | 52 | AB0+ |
| ab0 | 18 | AB0– |
| No Connect1 | 60 | COM1+ |
| No Connect1 | 26 | COM1– |
| No Connect1 | 44 | COM2+ |
| No Connect1 | 10 | COM2– |
| No Connect1 | 43 | COM3+ |
| No Connect1 | 9 | COM3– |
| No Connect1 | 51 | AB1+ |
| No Connect1 | 17 | AB1– |
| 1 Not used in this topology |  |  |

#### Additional Pin References

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-2-wire-24-1-multiplexer-topo.html language=enus -->
## TOPIC 00117: NI PXI-2501/2503 2-Wire 24×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-2-wire-24-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-2-wire-24-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 2-wire 24×1 multiplexer, connect your signals using the NI TB-2605 terminal block. In this topology, you can connect to a Cold-Junction Sensor Channel for cold-junction compensation. The following figure is a representation of the NI PXI-2501/2503 in this mode. M

### NI PXI-2501/2503 2-Wire 24×1 Multiplexer Topology

When using the NI PXI-2501/2503 as a 2-wire 24×1 multiplexer, connect your signals using
 the NI TB-2605 terminal block. In this topology, you can connect to a Cold-Junction
 Sensor Channel for cold-junction compensation. The following figure is a representation
 of the NI PXI-2501/2503 in this mode.

|  |
| --- |

#### Making a Connection

The NI PXI-2501/2503 in this topology contains 24 2-wire input channels connected to
 a common 2-wire channel. In software, these input channels are referred to as
 ch<0..23> and the common channel is referred to as com0. All positive leads
 (CH0+ through CH23+) can connect to COM0+, and all negative leads (CH0– through
 CH23–) can connect to COM0–.

For example, to connect a 2-wire signal to ch5, wire the HI side to CH5+ and the LO
 side to CH5–. For com0, connect to COM0+ and COM0– for the HI and LO of the signal,
 respectively.

You can also route cjtemp to com0, which routes com0 to a temperature sensor on the
 NI TB-2605 terminal block. Refer to Cold-Junction Sensor Channel for more
 information.

During scanning, an example scan list entry is CH2->com0;. This
 entry routes the signal connected to CH2+ to COM0+ and the signal connected to CH2–
 to COM0–.

During immediate operations when calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with ch2 and com0, the signal connected
 to CH2+ is routed to COM0+ and the signal connected to CH2– is routed to COM0–. To
 route the signals to AB0, use the niSwitch Connect Channels VI or the
 niSwitch_Connect function with com0 and
 ab0.

#### Pinout

The following figure and tables identify the pins for the NI PXI-2501/2503 in the
 2-wire 24×1 multiplexer topology.

[IMAGE alt='image' src='GUID-98E0DCD8-23C1-4AF8-9BC0-496BE4CA2909-a5.gif']

Caution

| Software Name | Polarity | NI PXI-2501/2503 Connector Pin Number | NI TB-2605 Terminal Name |
| --- | --- | --- | --- |
| ch0 | + | 67 | CH0+ |
| ch0 | – | 33 | CH0– |
| ch1 | + | 66 | CH1+ |
| ch1 | – | 32 | CH1– |
| ch2 | + | 65 | CH2+ |
| ch2 | – | 31 | CH2– |
| ch3 | + | 64 | CH3+ |
| ch3 | – | 30 | CH3– |
| ch4 | + | 63 | CH4+ |
| ch4 | – | 29 | CH4– |
| ch5 | + | 62 | CH5+ |
| ch5 | – | 28 | CH5– |
| ch6 | + | 59 | CH6+ |
| ch6 | – | 25 | CH6– |
| ch7 | + | 58 | CH7+ |
| ch7 | – | 24 | CH7– |
| ch8 | + | 57 | CH8+ |
| ch8 | – | 23 | CH8– |
| ch9 | + | 55 | CH9+ |
| ch9 | – | 21 | CH9– |
| ch10 | + | 54 | CH10+ |
| ch10 | – | 20 | CH10– |
| ch11 | + | 53 | CH11+ |
| ch11 | – | 19 | CH11– |
| ch12 | + | 50 | CH12+ |
| ch12 | – | 16 | CH12– |
| ch13 | + | 49 | CH13+ |
| ch13 | – | 15 | CH13– |
| ch13 | + | 49 | CH13+ |
| ch14 | + | 48 | CH14+ |
| ch14 | – | 14 | CH14– |
| ch15 | + | 47 | CH15+ |
| ch15 | – | 13 | CH15– |
| ch16 | + | 46 | CH16+ |
| ch16 | – | 12 | CH16– |
| ch17 | + | 45 | CH17+ |
| ch17 | – | 11 | CH17– |
| ch18 | + | 40 | CH18+ |
| ch18 | – | 6 | CH18– |
| ch19 | + | 39 | CH19+ |
| ch19 | – | 5 | CH19– |
| ch20 | + | 38 | CH20+ |
| ch20 | – | 4 | CH20– |
| ch21 | + | 37 | CH21+ |
| ch21 | – | 3 | CH21– |
| ch22 | + | 36 | CH22+ |
| ch22 | – | 2 | CH22– |
| ch23 | + | 35 | CH23+ |
| ch23 | – | 1 | CH23– |
| com0 | + | 61 | COM0+ |
| com0 | – | 27 | COM0– |
| ab0 | + | 52 | AB0+ |
| ab0 | – | 18 | AB0– |
| No Connect1 | + | 60 | COM1+ |
| No Connect1 | – | 26 | COM1– |
| No Connect1 | + | 44 | COM2+ |
| No Connect1 | – | 10 | COM2– |
| No Connect1 | + | 43 | COM3+ |
| No Connect1 | – | 9 | COM3– |
| No Connect1 | + | 51 | AB1+ |
| No Connect1 | – | 17 | AB1– |
| 1 Not used in this topology |  |  |  |

#### Additional Pin References

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |
| 22 | 1wireREF |

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- Cold-Junction Temperature Sensor Channel

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-2-wire-4-6-matrix-topology.html language=enus -->
## TOPIC 00118: NI PXI-2501/2503 2-Wire 4×6 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-2-wire-4-6-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-2-wire-4-6-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 2-wire 4×6 matrix, connect your signals using the NI TB-2606 terminal block. The following figure is a representation of the NI PXI-2501/2503 in this mode. Making a Connection In this topology, connect your positive and negative leads to Cx± or Rx± inside the NI

### NI PXI-2501/2503 2-Wire 4×6 Matrix Topology

When using the NI PXI-2501/2503 as a 2-wire 4×6 matrix, connect your signals using the NI
 TB-2606 terminal block. The following figure is a representation of the NI PXI-2501/2503
 in this mode.

|  |
| --- |

#### Making a Connection

In this topology, connect your positive and negative leads to Cx±
 or Rx± inside the NI TB-2606 terminal block.

During scanning, an example scan list entry is r2->c1;. This
 entry routes the signal connected to R2+ to C1+ and connects R2– to C1–.

During immediate operations when calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with r2 and c1, the signal connected to
 R2+ is routed to C1+ and the signal connected to R2– is routed to C1–. To route the
 signals to AB0, use the niSwitch Connect Channels VI or the
 niSwitch_Connect function with com0 and
 ab0.

#### Pinout

The following figure and tables identify the pins for the NI PXI-2501/2503 in the
 2-wire 4×6 matrix topology.

[IMAGE alt='image' src='GUID-82597A1F-B9D5-40F3-9E18-41711E41C271-a5.gif']

| Software Name | Polarity | NI PXI-2501/2503 Connector Pin Number | NI TB-2606 Terminal Name |
| --- | --- | --- | --- |
| c0 | + | 67, 59, 50, 40 | C0+ |
| c0 | – | 33, 25, 16, 6 | C0- |
| c1 | + | 66, 58, 49, 39 | C1+ |
| c1 | – | 32, 24, 15, 5 | C1- |
| c2 | + | 65, 57, 48, 38 | C2+ |
| c2 | – | 31, 23, 14, 4 | C2- |
| c3 | + | 64, 55, 47, 37 | C3+ |
| c3 | – | 30, 21, 13, 3 | C3- |
| c4 | + | 63, 54, 46, 36 | C4+ |
| c4 | – | 29, 20, 12, 2 | C4- |
| c5 | + | 62, 53, 45, 35 | C5+ |
| c5 | – | 28, 19, 11, 1 | C5- |
| r0 | + | 61 | R0+ |
| r0 | – | 27 | R0- |
| r1 | + | 60 | R1+ |
| r1 | – | 26 | R1- |
| r2 | + | 44 | R2+ |
| r2 | – | 10 | R2- |
| r3 | + | 43 | R3+ |
| r3 | – | 9 | R3- |
| ab0 | + | 52 | AB0+ |
| ab0 | – | 18 | AB0- |
| ab1 | + | 51 | AB1+ |
| ab1 | – | 17 | AB1- |

#### Additional Pin References

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |
| 22 | 1wireREF |

Caution

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Matrix
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-2-wire-dual-12-1-multiplexer.html language=enus -->
## TOPIC 00119: NI PXI-2501/2503 2-Wire Dual 12×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-2-wire-dual-12-1-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-2-wire-dual-12-1-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 2-wire dual 12×1 multiplexer, connect your signals using the NI TB-2605 terminal block. In this topology, you can connect to a Cold-Junction Sensor Channel for cold-junction compensation. The following figure is a representation of the NI PXI-2501/2503 in this mo

### NI PXI-2501/2503 2-Wire Dual 12×1 Multiplexer Topology

When using the NI PXI-2501/2503 as a 2-wire dual 12×1 multiplexer, connect your signals
 using the NI TB-2605 terminal block. In this topology, you can connect to a
 Cold-Junction Sensor Channel for cold-junction compensation. The following figure is a
 representation of the NI PXI-2501/2503 in this mode.

|  |
| --- |

#### Making a Connection

The NI PXI-2501/2503 in this topology contains two banks of 12 2-wire input channels
 connected to a common 2-wire channel. These input channels are referred to as
 ch<0..23> and the two common channels are referred to as com0 and com2. You
 can only connect to the common channel that is in the same bank. The banks are
 organized as follows:

| Input Channels | Common Channel |
| --- | --- |
| ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, cjtemp | com0 |
| ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23 | com2 |

For example, you can connect ch5 to com0; however, you cannot connect ch5 to com2 in
 this topology. When connecting signals for ch5, you would connect them to CH5+ and
 CH5– for HI and LO of the signal, respectively. For com0, connect to COM0+ and COM0–
 for HI and LO of the signal, respectively.

Notice that in the first bank you can connect cjtemp to com0. This connects com0 to a
 temperature sensor on the NI TB-2605 terminal block. Refer to Cold-Junction Sensor
 Channel for more information.

During scanning, an example scan list entry is ch2->com0;. This
 entry routes the signal connected to CH2+ to COM0+ and the signal from CH2– to
 COM0–.

During immediate operations when calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with ch2+ and com0, the signal connected
 to CH2+ is routed to COM0+ and the signal connected to CH2– is routed to COM0–. To
 route the signals to AB0, use the niSwitch Connect Channels VI or the
 niSwitch_Connect function with com0 and
 ab0.

#### Pinout

The following figure and tables identify the pins for the NI PXI-2501/2503 in the
 2-wire dual 12×1 multiplexer topology.

[IMAGE alt='image' src='GUID-71414D21-50EC-4399-B508-23C5C5104E0D-a5.gif']

Caution

| Software Name | Polarity | NI PXI-2501/2503 Connector Pin Number | NI TB-2605 Terminal Name |
| --- | --- | --- | --- |
| ch0 | + | 67 | CH0+ |
| ch0 | – | 33 | CH0– |
| ch1 | + | 66 | CH1+ |
| ch1 | – | 32 | CH1– |
| ch2 | + | 65 | CH2+ |
| ch2 | – | 31 | CH2– |
| ch3 | + | 64 | CH3+ |
| ch3 | – | 30 | CH3– |
| ch4 | + | 63 | CH4+ |
| ch4 | – | 29 | CH4– |
| ch5 | + | 62 | CH5+ |
| ch5 | – | 28 | CH5– |
| ch6 | + | 59 | CH6+ |
| ch6 | – | 25 | CH6– |
| ch7 | + | 58 | CH7+ |
| ch7 | – | 24 | CH7– |
| ch8 | + | 57 | CH8+ |
| ch8 | – | 23 | CH8– |
| ch9 | + | 55 | CH9+ |
| ch9 | – | 21 | CH9– |
| ch10 | + | 54 | CH10+ |
| ch10 | – | 20 | CH10– |
| ch11 | + | 53 | CH11+ |
| ch11 | – | 19 | CH11– |
| ch12 | + | 50 | CH12+ |
| ch12 | – | 16 | CH12– |
| ch13 | + | 49 | CH13+ |
| ch13 | – | 15 | CH13– |
| ch14 | + | 48 | CH14+ |
| ch14 | – | 14 | CH14– |
| ch15 | + | 47 | CH15+ |
| ch15 | – | 13 | CH15– |
| ch16 | + | 46 | CH16+ |
| ch16 | – | 12 | CH16– |
| ch17 | + | 45 | CH17+ |
| ch17 | – | 11 | CH17– |
| ch18 | + | 40 | CH18+ |
| ch18 | – | 6 | CH18– |
| ch19 | + | 39 | CH19+ |
| ch19 | – | 5 | CH19– |
| ch20 | + | 38 | CH20+ |
| ch20 | – | 4 | CH20– |
| ch21 | + | 37 | CH21+ |
| ch21 | – | 3 | CH21– |
| ch22 | + | 36 | CH22+ |
| ch22 | – | 2 | CH22– |
| ch23 | + | 35 | CH23+ |
| ch23 | – | 1 | CH23– |
| com0 | + | 61 | COM0+ |
| com0 | – | 27 | COM0– |
| com2 | + | 44 | COM2+ |
| com2 | – | 10 | COM2– |
| ab0 | + | 52 | AB0+ |
| ab0 | – | 18 | AB0– |
| ab1 | + | 51 | AB1+ |
| ab1 | – | 17 | AB1– |
| No Connect1 | + | 60 | COM1+ |
| No Connect1 | – | 26 | COM1– |
| No Connect1 | + | 43 | COM3+ |
| No Connect1 | – | 9 | COM3– |
| 1Not used in this topology |  |  |  |

#### Additional Pin References

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |
| 22 | 1wireREF |

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- Cold-Junction Temperature Sensor Channel

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-2-wire-quad-6-1-multiplexer.html language=enus -->
## TOPIC 00120: NI PXI-2501/2503 2-Wire Quad 6×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-2-wire-quad-6-1-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-2-wire-quad-6-1-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 2-wire quad 6×1 multiplexer, connect your signals using the NI TB-2605 terminal block. In this topology, you can connect to a Cold-Junction Temperature Sensor Channel for cold-junction compensation. The following figure is a representation of the NI PXI-2501/2503

### NI PXI-2501/2503 2-Wire Quad 6×1 Multiplexer Topology

When using the NI PXI-2501/2503 as a 2-wire quad 6×1 multiplexer, connect your signals
 using the NI TB-2605 terminal block. In this topology, you can connect to a
 Cold-Junction Temperature Sensor Channel for cold-junction compensation. The following
 figure is a representation of the NI PXI-2501/2503 in this mode.

|  |
| --- |

#### Making a Connection

The NI PXI-2501/2503 in this topology contains four banks of six 2-wire input
 channels connected to a common 2-wire channel. These input channels are referred to
 as ch<0..23>, and the four common channels are referred to as com<0..3>.
 You can only connect to the common channel that is in the same bank. The banks are
 organized as shown in the following table.

| Input Channels | Common Channel |
| --- | --- |
| ch0, ch1, ch2, ch3, ch4, ch5, cjtemp | com0 |
| ch6, ch7, ch8, ch9, ch10, ch11 | com1 |
| ch12, ch13, ch14, ch15, ch16, ch17 | com2 |
| ch18, ch19, ch20, ch21, ch22, ch23 | com3 |

For example, you can connect ch5 to com0; however, you cannot connect ch5 to com1 in
 this topology. When connecting signals for ch5, you would connect them to CH5+ and
 CH5– for HI and LO of the signal, respectively. For com0, connect to COM0+ and COM0–
 for HI and LO of the signal, respectively.

Notice that in the first bank you can connect cjtemp to com0. This
 connects com0 to a temperature sensor on the NI TB-2605 terminal block. Refer to
 Cold-Junction Temperature Sensor Channel for more information.

During scanning, an example scan list entry is ch2->com0;. This
 entry routes the signal connected to CH2+ to COM0+ and the signal connected to CH2–
 is routed to COM0–.

During immediate operations when calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with ch2 and com0, the signal connected
 to CH2+ is routed to COM0+. To route the signals to ABO, use the niSwitch Connect
 Channels VI or the niSwitch_Connect function with
 com0 and ab0 and the signal connected to CH2–
 is routed to COM0–.

#### Pinout

The following figure and tables identify the pins for the NI PXI-2501/2503 in the
 2-wire quad 6×1 multiplexer topology.

[IMAGE alt='image' src='GUID-49729058-E60E-4F0E-BA95-5D18A8EBE4E3-a5.gif']

Caution

| Software Name | Polarity | NI PXI-2501/2503 Connector Pin Number | NI TB-2605 Terminal Name |
| --- | --- | --- | --- |
| ch0 | + | 67 | CH0+ |
| ch0 | – | 33 | CH0– |
| ch1 | + | 66 | CH1+ |
| ch1 | – | 32 | CH1– |
| ch2 | + | 65 | CH2+ |
| ch2 | – | 31 | CH2– |
| ch3 | + | 64 | CH3+ |
| ch3 | – | 30 | CH3– |
| ch4 | + | 63 | CH4+ |
| ch4 | – | 29 | CH4– |
| ch5 | + | 62 | CH5+ |
| ch5 | – | 28 | CH5– |
| ch6 | + | 59 | CH6+ |
| ch6 | – | 25 | CH6– |
| ch7 | + | 58 | CH7+ |
| ch7 | – | 24 | CH7– |
| ch8 | + | 57 | CH8+ |
| ch8 | – | 23 | CH8– |
| ch9 | + | 55 | CH9+ |
| ch9 | – | 21 | CH9– |
| ch10 | + | 54 | CH10+ |
| ch10 | – | 20 | CH10– |
| ch11 | + | 53 | CH11+ |
| ch11 | – | 19 | CH11– |
| ch12 | + | 50 | CH12+ |
| ch12 | – | 16 | CH12– |
| ch13 | + | 49 | CH13+ |
| ch13 | – | 15 | CH13– |
| ch14 | + | 48 | CH14+ |
| ch14 | – | 14 | CH14– |
| ch15 | + | 47 | CH15+ |
| ch15 | – | 13 | CH15– |
| ch16 | + | 46 | CH16+ |
| ch16 | – | 12 | CH16– |
| ch17 | + | 45 | CH17+ |
| ch17 | – | 11 | CH17– |
| ch18 | + | 40 | CH18+ |
| ch18 | – | 6 | CH18– |
| ch19 | + | 39 | CH19+ |
| ch19 | – | 5 | CH19– |
| ch20 | + | 38 | CH20+ |
| ch20 | – | 4 | CH20– |
| ch21 | + | 37 | CH21+ |
| ch21 | – | 3 | CH21– |
| ch22 | + | 36 | CH22+ |
| ch22 | – | 2 | CH22– |
| ch23 | + | 35 | CH23+ |
| ch23 | – | 1 | CH23– |
| com0 | + | 61 | COM0+ |
| com0 | – | 27 | COM0– |
| com1 | + | 60 | COM1+ |
| com1 | – | 26 | COM1– |
| com2 | + | 44 | COM2+ |
| com2 | – | 10 | COM2– |
| com3 | + | 43 | COM2+ |
| com3 | – | 9 | COM2– |
| ab0 | + | 52 | AB0+ |
| ab0 | – | 18 | AB0– |
| ab1 | + | 51 | AB1+ |
| ab1 | – | 17 | AB1– |

#### Additional Pin References

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |
| 22 | 1wireREF |

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- Cold-Junction Temperature Sensor Channel

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-4-wire-12-1-multiplexer-topo.html language=enus -->
## TOPIC 00121: NI PXI-2501/2503 4-Wire 12×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-4-wire-12-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-4-wire-12-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2501/2503 as a 4-wire 12×1 multiplexer, connect your signals using the NI TB-2605 terminal block. The following figure is a representation of the NI PXI-2501/2503 in this mode. 4-wire mode is usually used in 4-wire resistance measurements. One pair of wires supplies the excitat

### NI PXI-2501/2503 4-Wire 12×1 Multiplexer Topology

When using the NI PXI-2501/2503 as a 4-wire 12×1 multiplexer, connect your signals using
 the NI TB-2605 terminal block. The following figure is a representation of the
 NI PXI-2501/2503 in this mode.

|  |
| --- |

4-wire mode is usually used in 4-wire resistance measurements. One pair of wires supplies
 the excitation current while the other pair makes the voltage measurement. In 4-wire
 mode, connect your excitation or source leads to CHxA+ and
 CHxA-, and connect your measurement or sensing leads to
 CHxB+ and CHxB-, as shown in the following
 figure:

|  |
| --- |

Note

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

- signal connected to CH2A+ is routed to COM0A+
- signal connected to CH2A– is routed to COM0A–
- signal connected to CH2B+ is routed to COM0B+
- signal connected to CH2B– is routed to COM0B–

#### Pinout

The following figure identifies the pins for the NI PXI-2501/2503 in the 4-wire 12×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-22CE8D20-A125-4CD8-9591-DA8C5745381B-a5.gif']

Caution

| Software Name | Polarity | NI PXI-2501/2503 Connector Pin Number | NI TB-2605 Terminal Name |
| --- | --- | --- | --- |
| ch0 | + | 67 | CH0A+ |
| ch0 | - | 33 | CH0A- |
| ch0 | + | 50 | CH0B+ |
| ch0 | - | 16 | CH0B- |
| ch1 | + | 66 | CH1A+ |
| ch1 | - | 32 | CH1A- |
| ch1 | + | 49 | CH1B+ |
| ch1 | - | 15 | CH1B- |
| ch2 | + | 65 | CH2A+ |
| ch2 | - | 31 | CH2A- |
| ch2 | + | 48 | CH2B+ |
| ch2 | - | 14 | CH2B- |
| ch3 | + | 64 | CH3A+ |
| ch3 | - | 30 | CH3A- |
| ch3 | + | 47 | CH3B+ |
| ch3 | - | 13 | CH3B- |
| ch4 | + | 63 | CH4A+ |
| ch4 | - | 29 | CH4A- |
| ch4 | + | 46 | CH4B+ |
| ch4 | - | 12 | CH4B- |
| ch5 | + | 62 | CH5A+ |
| ch5 | - | 28 | CH5A- |
| ch5 | + | 45 | CH5B+ |
| ch5 | - | 11 | CH5B- |
| ch6 | + | 59 | CH6A+ |
| ch6 | - | 25 | CH6A- |
| ch6 | + | 40 | CH6B+ |
| ch6 | - | 6 | CH6B- |
| ch7 | + | 58 | CH7A+ |
| ch7 | - | 24 | CH7A- |
| ch7 | + | 39 | CH7B+ |
| ch7 | - | 5 | CH7B- |
| ch8 | + | 57 | CH8A+ |
| ch8 | - | 23 | CH8A- |
| ch8 | + | 38 | CH8B+ |
| ch8 | - | 4 | CH8B- |
| ch9 | + | 55 | CH9A+ |
| ch9 | - | 21 | CH9A- |
| ch9 | + | 37 | CH9B+ |
| ch9 | - | 3 | CH9B- |
| ch10 | + | 54 | CH10A+ |
| ch10 | - | 20 | CH10A- |
| ch10 | + | 36 | CH10B+ |
| ch10 | - | 2 | CH10B- |
| ch11 | + | 53 | CH11A+ |
| ch11 | - | 19 | CH11A- |
| ch11 | + | 35 | CH11B+ |
| ch11 | - | 1 | CH11B- |
| com0 | + | 61 | COM0A+ |
| com0 | - | 27 | COM0A- |
| com0 | + | 44 | COM0B+ |
| com0 | - | 10 | COM0B- |
| No Connect1 | + | 60 | COM1A+ |
| No Connect1 | - | 26 | COM1A- |
| No Connect1 | + | 43 | COM1B+ |
| No Connect1 | - | 9 | COM1B- |
| ab0 | + | 52 | AB0A+ |
| ab0 | - | 18 | AB0A- |
| ab0 | + | 51 | AB0B+ |
| ab0 | - | 17 | AB0B- |
| 1Not used in this topology |  |  |  |

| NI PXI-2501/2503 Connector Pin Number | Signal name |
| --- | --- |
| 7, 56 | GND |
| 41 | TRIG IN |
| 42 | SCANADV |
| 8 | RESERVED |
| 68 | CJS+ |
| 34 | CJS- |
| 22 | 1wireREF |

Parent topic:

NI PXI-2501/2503

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-current-loop-receivers.html language=enus -->
## TOPIC 00122: NI PXI-2501/2503 Current-Loop Receivers

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-current-loop-receivers.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-current-loop-receivers.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2501/2503 modules have sockets for transforming individual channels to current-to-voltage converters. NI offers a process-current pack of four 249 Ω, 0.1%, 5 ppm, 0.25 W resistors. The reference designator format for the current-loop resistors is such that for input channel x, the resisto

### NI PXI-2501/2503 Current-Loop Receivers

x

x

Caution

Before installing your module in the NI PXI chassis, you must install the resistors by
 performing the following steps:

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis. Properly
 grounding yourself prevents damage to your PXI module from electrostatic discharge.
2. Bend and trim the resistor lead as shown in the following figure. Be sure that the resistor
 does not extend more than 0.5 in. (1.3 cm) above the surface of the circuit board. [IMAGE alt='image' src='GUID-CD4A8321-77EE-462D-A492-581D2F05F10F-a5.gif']
3. Insert the resistor into the appropriate socket, labeled RCL x .

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503-triggering.html language=enus -->
## TOPIC 00123: NI PXI-2501/2503 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2501/2503. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trig

### NI PXI-2501/2503 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2501/2503.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG IN on TB-2605 terminal block |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2501/2503.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | SCANADV on TB-2605 terminal block |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-2503.html language=enus -->
## TOPIC 00124: NI PXI-2501/2503

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-2503.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-2503.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2501/2503 are multiplexer/matrix switch modules for the PXI platform. The NI PXI-2501 is composed of FET switches, and the NI PXI-2503 uses armature relays. NI PXI-2501 Operation Modes The following table lists the supported topology of the NI PXI-2501 and possible operation modes. Topolo

### NI PXI-2501/2503

The NI PXI-2501/2503 are multiplexer/matrix switch modules for the PXI platform. The
 NI PXI-2501 is composed of FET switches, and the NI PXI-2503 uses armature relays.

#### NI PXI-2501 Operation Modes

The following table lists the supported topology of the NI PXI-2501 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 48×1 Multiplexer | 2501/1-Wire 48x1 Mux(NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX) |  |  |
| 1-Wire 48×1 Amplified Multiplexer | 2501/1-Wire 48x1 Amplified Mux(NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_AMPLIFIED_MUX) |  |  |
| 2-Wire 24×1 Multiplexer | 2501/2-Wire 24x1 Mux(NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_MUX) |  |  |
| 2-Wire 24×1 Amplified Multiplexer | 2501/2-Wire 24x1 Amplified Mux(NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_AMPLIFIED_MUX) |  |  |
| 2-Wire Dual 12×1 Multiplexer | 2501/2-Wire Dual 12x1 Mux(NISWITCH_TOPOLOGY_2501_2_WIRE_DUAL_12X1_MUX) |  |  |
| 2-Wire Quad 6×1 Multiplexer | 2501/2-Wire Quad 6x1 Mux(NISWITCH_TOPOLOGY_2501_2_WIRE_QUAD_6X1_MUX) |  |  |
| 2-Wire 4×6 Matrix | 2501/2-Wire 4x6 Matrix(NISWITCH_TOPOLOGY_2501_2_WIRE_4X6_MATRIX) |  |  |
| 4-Wire 12×1 Multiplexer | 2501/4-Wire 12x1 Mux(NISWITCH_TOPOLOGY_2501_4_WIRE_12X1_MUX) |  |  |

#### NI PXI-2503 Operation Modes

The following table lists the supported topologies of the NI PXI-2503 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 48×1 Multiplexer | 2503/1-Wire 48x1 Mux(NISWITCH_TOPOLOGY_2503_1_WIRE_48X1_MUX) |  |  |
| 2-Wire 24×1 Multiplexer | 2503/2-Wire 24x1 Mux(NISWITCH_TOPOLOGY_2503_2_WIRE_24X1_MUX) |  |  |
| 2-Wire Dual 12×1 Multiplexer | 2503/2-Wire Dual 12x1 Mux(NISWITCH_TOPOLOGY_2503_2_WIRE_DUAL_12X1_MUX) |  |  |
| 2-Wire Quad 6×1 Multiplexer | 2503/2-Wire Quad 6x1 Mux(NISWITCH_TOPOLOGY_2503_2_WIRE_QUAD_6X1_MUX) |  |  |
| 2-Wire 4×6 Matrix | 2503/2-Wire 4x6 Matrix(NISWITCH_TOPOLOGY_2503_2_WIRE_4X6_MATRIX) |  |  |
| 4-Wire 12×1 Multiplexer | 2503/4-Wire 12x1 Mux(NISWITCH_TOPOLOGY_2503_4_WIRE_12X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- NI PXI-2501/2503 1-Wire 48×1 Multiplexer Topology
- NI PXI-2501 1-Wire 48×1 Amplified Multiplexer Topology
- NI PXI-2501/2503 2-Wire 24×1 Multiplexer Topology
- NI PXI-2501 2-Wire 24×1 Amplified Multiplexer Topology
- NI PXI-2501/2503 2-Wire Dual 12×1 Multiplexer Topology
- NI PXI-2501/2503 2-Wire Quad 6×1 Multiplexer Topology
- NI PXI-2501/2503 2-Wire 4×6 Matrix Topology
- NI PXI-2501/2503 4-Wire 12×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-amplifier.html language=enus -->
## TOPIC 00125: NI PXI-2501 Amplifier

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-amplifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-amplifier.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2501 has an amplifier with a gain of 1. This amplifier can be switched in-line before the COM0 signal and the AB0 signal. The amplifier helps decrease the settling time of the FET switch. The high-impedance amplifier isolates the FET from the resistance, capacitance, and inductance in the

### NI PXI-2501 Amplifier

The NI PXI-2501 has an amplifier with a gain of 1. This amplifier can be switched in-line
 before the COM0 signal and the AB0 signal. The amplifier helps decrease the settling
 time of the FET switch. The high-impedance amplifier isolates the FET from the
 resistance, capacitance, and inductance in the external wiring. This isolation decreases
 the resistance/capacitance time constant seen by the FET, which improves settling time.
 When the amplifier is used, the switch module becomes directional, where
 CHx is for signal inputs and COM0 or AB0 are for signal outputs.

The amplifier has an offset that can be calibrated for more accurate measurements. The
 calibration data can be stored into and retrieved from the EEPROM on the module.

The NI PXI-2501 also has an amplifier in the CJS0+ to COM0+ signal path. This amplifier
 in the cold-junction sensor signal path is used to improve settling time performance. It
 prevents the impedance of the cold-junction sensor from increasing the settling time
 when switching the CJS channel. As a result, when scanning thermocouples, the settling
 time for the cold-junction sensor channel should be about the same as for the channels
 with the thermocouples.

Parent topic:

NI PXI-2501/2503

Related concepts:

- FET Switches

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2501-hardware-diagram.html language=enus -->
## TOPIC 00126: NI PXI-2501 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2501-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2501-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2501. Relay names are the same for every topology.

### NI PXI-2501 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-15DF2F6D-BC93-4272-B2B8-1B10D4748CB2-a5.gif']

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2503-hardware-diagram.html language=enus -->
## TOPIC 00127: NI PXI-2503 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2503-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2503-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2503. Relay names are the same for every topology.

### NI PXI-2503 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-3398B085-4555-4A8B-84C9-D778B17D8D92-a5.gif']

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2510-hardware-diagram.html language=enus -->
## TOPIC 00128: NI PXI-2510 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2510-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2510-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2510. The following table lists relay names for the NI PXI-2510. Relays k0...k67 k0a...k67a k0b...k67b ka0busA...ka3busA kb0busB...kb3busB

### NI PXI-2510 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2510.

[IMAGE alt='image' src='GUID-00546B29-B475-48F6-BFD9-DA61C9C76B56-a5.gif']

The following table lists relay names for the NI PXI-2510.

| Relays |
| --- |
| k0...k67 |
| k0a...k67a |
| k0b...k67b |
| ka0busA...ka3busA |
| kb0busB...kb3busB |

Parent topic:

NI PXI-2510

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2510-independent-topology.html language=enus -->
## TOPIC 00129: NI PXI-2510 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2510-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2510-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2510 in the independent topology. Making a Connection Both the scanning command, dut1->busA;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters dut1 and busA, result in the following connection: signa

### NI PXI-2510 Independent Topology

The following figure represents the NI PXI-2510 in the independent topology.

[IMAGE alt='image' src='GUID-00546B29-B475-48F6-BFD9-DA61C9C76B56-a5.gif']

#### Making a Connection

Both the scanning command, dut1->busA;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters dut1 and busA, result in
 the following connection:

signal connected to DUT1 is routed to busA

Note

N

N

N

N

N

N

N

N

N

N

None

NISWITCH_ATTR_SCAN_MODE

NISWITCH_VAL_NONE

#### Pinout

The following figure identifies the pins for the NI PXI-2510.

[IMAGE alt='image' src='GUID-E412C720-80FF-4728-B981-DA012E52046E-a5.gif']

Parent topic:

NI PXI-2510

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2510-relay-replacement.html language=enus -->
## TOPIC 00130: NI PXI-2510 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2510-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2510-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2510 uses electromechanical armature relays. The NI PXI-2510 uses a custom lead length to meet safety standards. Trim leads to no more than 1 mm (0.04 inch) from the PCB. You also can use the spare relay included with the module at location K49. Refer to the following tables for informa

### NI PXI-2510 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. Base Board 
 [IMAGE alt='image' src='GUID-417BFA4F-0ACD-4104-BBDC-05D8A06022C8-a5.gif'] 
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNamek0
 K12
 k7a
 K14
 k14b
 K40
 k22
 K67k0a
 K11
 k7b
 K15
 k15
 K37
 k22a
 K65k0b
 K10
 k8
 K35
 k15a
 K39
 k22b
 K66k1
 K7
 k8a
 K34
 k15b
 K38
 k23
 K64k1a
 K8
 k8b
 K36
 k16
 K59
 k23a
 K62k1b
 K9
 k9
 K33
 k16a
 K60
 k23b
 K63k2
 K6
 k9a
 K32
 k16b
 K61
 k24
 K79k2a
 K5
 k9b
 K31
 k17
 K56
 k24a
 K77k2b
 K4
 k10
 K28
 k17a
 K58
 k24b
 K78k3
 K2
 k10a
 K29
 k17b
 K57
 k25
 K76k3a
 K3
 k10b
 K30
 k18
 K53
 k25a
 K74k3b
 K1
 k11
 K25
 k18a
 K55
 k25b
 K75k4
 K23
 k11a
 K26
 k18b
 K54
 ka0busA
 K84k4a
 K22
 k11b
 K27
 k19
 K50
 ka1busA
 K83k4b
 K24
 k12
 K48
 k19a
 K52
 ka2busA
 K82k5
 K21
 k12a
 K47
 k19b
 K51
 ka3busA
 K81k5a
 K19
 k12b
 K46
 k20
 K73
 kb0busB
 K80k5b
 K20
 k13
 K45
 k20a
 K72
 kb1busB
 K87k6
 K16
 k13a
 K44
 k20b
 K71
 kb2busB
 K86k6a
 K17
 k13b
 K43
 k21
 K70
 kb3busB
 K85k6b
 K18
 k14
 K42
 k21a
 K68
 Spare
 K49k7
 K13
 k14a
 K41
 k21b
 K69 
 Mezzanine Board 
 [IMAGE alt='image' src='GUID-5C72AE7C-A401-4D00-A7EE-E7EC2342C8C3-a5.gif'] 
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNamek26
 K57
 k36b
 K85
 k47a
 K11
 k58
 K93k26a
 K56
 k37
 K21
 k47b
 K10
 k58a
 K92k26b
 K55
 k37a
 K20
 k48
 K66
 k58b
 K91k27
 K72
 k37b
 K19
 k48a
 K65
 k59
 K90k27a
 K71
 k38
 K30
 k48b
 K64
 k59a
 K89k27b
 K70
 k38a
 K29
 k49
 K63
 k59b
 K88k28
 K3
 k38b
 K28
 k49a
 K62
 k60
 K78k28a
 K2
 k39
 K33
 k49b
 K61
 k60a
 K77k28b
 K1
 k39a
 K32
 k50
 K69
 k60b
 K76k29
 K6
 k39b
 K31
 k50a
 K68
 k61
 K114k29a
 K5
 k40
 K42
 k50b
 K67
 k61a
 K113k29b
 K4
 k40a
 K41
 k51
 K84
 k61b
 K112k30
 K45
 k40b
 K40
 k51a
 K83
 k62
 K111k30a
 K44
 k41
 K39
 k51b
 K82
 k62a
 K110k30b
 K43
 k41a
 K38
 k52
 K102
 k62b
 K109k31
 K60
 k41b
 K37
 k52a
 K101
 k63
 K75k31a
 K59
 k42
 K9
 k52b
 K100
 k63a
 K74k31b
 K58
 k42a
 K8
 k53
 K81
 k63b
 K73k32
 K18
 k42b
 K7
 k53a
 K80
 k64
 K126k32a
 K17
 k43
 K15
 k53b
 K79
 k64a
 K125k32b
 K16
 k43a
 K14
 k54
 K105
 k64b
 K124k33
 K24
 k43b
 K13
 k54a
 K104
 k65
 K117k33a
 K23
 k44
 K36
 k54b
 K103
 k65a
 K116k33b
 K22
 k44a
 K35
 k55
 K123
 k65b
 K115k34
 K27
 k44b
 K34
 k55a
 K122
 k66
 K120k34a
 K26
 k45
 K54
 k55b
 K121
 k66a
 K119k34b
 K25
 k45a
 K53
 k56
 K99
 k66b
 K118k35
 K48
 k45b
 K52
 k56a
 K98
 k67
 K108k35a
 K47
 k46
 K51
 k56b
 K97
 k67a
 K107k35b
 K46
 k46a
 K50
 k57
 K96
 k67b
 K106k36
 K87
 k46b
 K49
 k57a
 K95k36a
 K86
 k47
 K12
 k57b
 K94
3. Remove the four screws that secure the mezzanine board to the base board. Do
 not remove the hex standoffs or the base board. 
 1
 Screws2
 Mezzanine board3
 Hex standoff4
 Base board
4. Separate the mezzanine board from the base board.

#### Replace the Relay

The NI PXI-2510 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 1 mm (0.04 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2510

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2510-triggering.html language=enus -->
## TOPIC 00131: NI PXI-2510 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2510-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2510-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2520 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2520. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2510 Triggering

The NI PXI-2520 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2520.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2520.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2510

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2510.html language=enus -->
## TOPIC 00132: NI PXI-2510

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2510.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2510.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2510 is an FIU switch module for the PXI platform. The NI PXI-2510 is composed of armature relays. Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Without additional protection, these transients c

### NI PXI-2510

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2510 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2510/Independent(NISWITCH_TOPOLOGY_2510_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Fault Insertion Units
- Armature Relays
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2510 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2520-80-spst-topology.html language=enus -->
## TOPIC 00133: NI PXI-2520 80-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2520-80-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2520-80-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2520 in the 80-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2520 80-SPST Topology

The following figure represents the NI PXI-2520 in the 80-SPST topology.

[IMAGE alt='image' src='GUID-76FE1997-FFD2-49EE-9C3A-A13AD21AAD88-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi,
 "ch2", "com2"). To open the relay of channel 2, call
 niSwitch_Disconnect(vi, "ch2", "com2").

When scanning the NI PXI-2520, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2520 in the 80-SPST
 topology.

[IMAGE alt='image' src='GUID-328A8684-5232-4747-A6FF-8D16B3925392-a5.gif']

Parent topic:

NI PXI-2520

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2520-hardware-diagram.html language=enus -->
## TOPIC 00134: NI PXI-2520 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2520-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2520-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2520. The following table lists relay names for the NI PXI-2520. Relays k0...k79

### NI PXI-2520 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2520.

[IMAGE alt='image' src='GUID-76FE1997-FFD2-49EE-9C3A-A13AD21AAD88-a5.gif']

The following table lists relay names for the NI PXI-2520.

| Relays |
| --- |
| k0...k79 |

Parent topic:

NI PXI-2520

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2520-relay-replacement.html language=enus -->
## TOPIC 00135: NI PXI-2520 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2520-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2520-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2520 uses electromechanical armature relays. The NI PXI-2520 uses a custom lead length to meet safety standards. Trim leads to no more than 1 mm (0.04 inch) from the PCB. You also can use the spare relay included with the module at location K80. Refer to the following tables for informa

### NI PXI-2520 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco Electronics | 1462041-5 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 782460-10 |

Complete the following steps to disassemble your module and replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the front of the
 module. The following table maps the relay names to the channel names.
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNamech0
 K0
 ch20
 K20
 ch40
 K40
 ch60
 K60ch1
 K1
 ch21
 K21
 ch41
 K41
 ch61
 K61ch2
 K2
 ch22
 K22
 ch42
 K42
 ch62
 K62ch3
 K3
 ch23
 K23
 ch43
 K43
 ch63
 K63ch4
 K4
 ch24
 K24
 ch44
 K44
 ch64
 K64ch5
 K5
 ch25
 K25
 ch45
 K45
 ch65
 K65ch6
 K6
 ch26
 K26
 ch46
 K46
 ch66
 K66ch7
 K7
 ch27
 K27
 ch47
 K47
 ch67
 K67ch8
 K8
 ch28
 K28
 ch48
 K48
 ch68
 K68ch9
 K9
 ch29
 K29
 ch49
 K49
 ch69
 K69ch10
 K10
 ch30
 K30
 ch50
 K50
 ch70
 K70ch11
 K11
 ch31
 K31
 ch51
 K51
 ch71
 K71ch12
 K12
 ch32
 K32
 ch52
 K52
 ch72
 K72ch13
 K13
 ch33
 K33
 ch53
 K53
 ch73
 K73ch14
 K14
 ch34
 K34
 ch54
 K54
 ch74
 K74ch15
 K15
 ch35
 K35
 ch55
 K55
 ch75
 K75ch16
 K16
 ch36
 K36
 ch56
 K56
 ch76
 K76ch17
 K17
 ch37
 K37
 ch57
 K57
 ch77
 K77ch18
 K18
 ch38
 K38
 ch58
 K58
 ch78
 K78ch19
 K19
 ch39
 K39
 ch59
 K59
 ch79
 K79
3. Replace the relay. The NI PXI-2520 uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this. This can prevent the same unit from being
 reworked later on a lead-free solder station, which could contaminate the
 station. 
 Make sure you have the following: 
 
 Replace the relay as you would any other through-hole part. Trim the replaced
 relay leads to no more than 1 mm (0.04 inch) from the PCB.
  - Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free
 solder rework
  - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
  - Solder wick
  - Fine pick
  - Isopropyl alcohol
  - Cotton swabs

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2520

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2520-triggering.html language=enus -->
## TOPIC 00136: NI PXI-2520 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2520-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2520-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2520 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2520. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2520 Triggering

The NI PXI-2520 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2520.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2520.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2520

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2520.html language=enus -->
## TOPIC 00137: NI PXI-2520

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2520.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2520.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2520 is an 80-channel general-purpose relay module for the PXI platform. The NI PXI-2520 is composed of 80 armature non-latching SPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Swit

### NI PXI-2520

The NI PXI-2520 is an 80-channel general-purpose relay module for the PXI platform. The
 NI PXI-2520 is composed of 80 armature non-latching SPST relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2520 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 80-SPST | 2520/80-SPST(NISWITCH_TOPOLOGY_2520_80_SPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2520 80-SPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2521-40-dpst-topology.html language=enus -->
## TOPIC 00138: NI PXI-2521 40-DPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2521-40-dpst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2521-40-dpst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2521 in the 40-DPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2521 40-DPST Topology

The following figure represents the NI PXI-2521 in the 40-DPST topology.

[IMAGE alt='image' src='GUID-7D5A473C-9032-415A-A0F3-680BE18D1244-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi,
 "ch2", "com2"). To open the relay of channel 2, call
 niSwitch_Disconnect(vi, "ch2", "com2").

When scanning the NI PXI-2521, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2521 in the 40-DPST
 topology.

[IMAGE alt='image' src='GUID-55D6ADF2-506C-4961-AA92-AB420F600523-a5.gif']

Parent topic:

NI PXI-2521

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2521-hardware-diagram.html language=enus -->
## TOPIC 00139: NI PXI-2521 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2521-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2521-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2521. The following table lists relay names for the NI PXI-2521. Relays k0...k39

### NI PXI-2521 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2521.

[IMAGE alt='image' src='GUID-7D5A473C-9032-415A-A0F3-680BE18D1244-a5.gif']

The following table lists relay names for the NI PXI-2521.

| Relays |
| --- |
| k0...k39 |

Parent topic:

NI PXI-2521

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2521-relay-replacement.html language=enus -->
## TOPIC 00140: NI PXI-2521 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2521-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2521-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2521 uses electromechanical armature relays. The NI PXI-2521 uses a custom lead length to meet safety standards. Trim leads to no more than 1 mm (0.04 inch) from the PCB. You also can use the spare relay included with the module at location K40. Refer to the following tables for informa

### NI PXI-2521 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco Electronics | 1462043-6 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 782461-10 |

Complete the following steps to disassemble your module and replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the front of the
 module. The following table maps the relay names to the channel names.
 ChannelName
 RelayName
 ChannelName
 RelayNamech0
 K0
 ch20
 K20ch1
 K1
 ch21
 K21ch2
 K2
 ch22
 K22ch3
 K3
 ch23
 K23ch4
 K4
 ch24
 K24ch5
 K5
 ch25
 K25ch6
 K6
 ch26
 K26ch7
 K7
 ch27
 K27ch8
 K8
 ch28
 K28ch9
 K9
 ch29
 K29ch10
 K10
 ch30
 K30ch11
 K11
 ch31
 K31ch12
 K12
 ch32
 K32ch13
 K13
 ch33
 K33ch14
 K14
 ch34
 K34ch15
 K15
 ch35
 K35ch16
 K16
 ch36
 K36ch17
 K17
 ch37
 K37ch18
 K18
 ch38
 K38ch19
 K19
 ch39
 K39
3. Replace the relay. The NI PXI-2521 uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this. This can prevent the same unit from being
 reworked later on a lead-free solder station, which could contaminate the
 station. 
 Make sure you have the following: 
 
 Replace the relay as you would any other through-hole part. Trim the replaced
 relay leads to no more than 1 mm (0.04 inch) from the PCB.
  - Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free
 solder rework
  - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
  - Solder wick
  - Fine pick
  - Isopropyl alcohol
  - Cotton swabs

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2521

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2521-triggering.html language=enus -->
## TOPIC 00141: NI PXI-2521 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2521-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2521-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2521 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2521. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2521 Triggering

The NI PXI-2521 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2521.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2521.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2521

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2521.html language=enus -->
## TOPIC 00142: NI PXI-2521

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2521.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2521.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2521 is a 40-channel general-purpose relay module for the PXI platform. The NI PXI-2521 is composed of 40 armature non-latching DPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switc

### NI PXI-2521

The NI PXI-2521 is a 40-channel general-purpose relay module for the PXI platform. The NI
 PXI-2521 is composed of 40 armature non-latching DPST relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2521 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 40-DPST | 2521/40-DPST(NISWITCH_TOPOLOGY_2521_40_DPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2521 40-DPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2522-53-spdt-topology.html language=enus -->
## TOPIC 00143: NI PXI-2522 53-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2522-53-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2522-53-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2522 in the 53-SPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM o

### NI PXI-2522 53-SPDT Topology

The following figure represents the NI PXI-2522 in the 53-SPDT topology.

[IMAGE alt='image' src='GUID-84C0DE47-7802-4B70-9340-B7D995A0D0B0-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal
 from the COM of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

To connect the NC terminal to the COM terminal of that channel, disconnect the NO terminal
 from the COM of that channel.

For example, to connect NC2 to COM2, use the following code:

niSwitch_Disconnect(vi, "no2", "com2")

niSwitch_Connect(vi, "nc2", "com2")

When scanning the NI PXI-2522, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2522 in the 53-SPDT topology.

[IMAGE alt='image' src='GUID-658F2942-9699-42C7-B068-301E0FD542E7-a5.gif']

Parent topic:

NI PXI-2522

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2522-hardware-diagram.html language=enus -->
## TOPIC 00144: NI PXI-2522 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2522-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2522-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2522. The following table lists relay names for the NI PXI-2522. Relays k0...k52

### NI PXI-2522 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2522.

[IMAGE alt='image' src='GUID-84C0DE47-7802-4B70-9340-B7D995A0D0B0-a5.gif']

The following table lists relay names for the NI PXI-2522.

| Relays |
| --- |
| k0...k52 |

Parent topic:

NI PXI-2522

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2522-relay-replacement.html language=enus -->
## TOPIC 00145: NI PXI-2522 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2522-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2522-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2522 uses electromechanical armature relays. The NI PXI-2522 uses a custom lead length to meet safety standards. Trim leads to no more than 1 mm (0.04 inch) from the PCB. You also can use the spare relay included with the module at location K53. Refer to the following tables for informa

### NI PXI-2522 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following steps to disassemble your module and replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the front of the
 module. The following table maps the relay names to the channel names.
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNamech0
 K0
 ch20
 K20
 ch40
 K40ch1
 K1
 ch21
 K21
 ch41
 K41ch2
 K2
 ch22
 K22
 ch42
 K42ch3
 K3
 ch23
 K23
 ch43
 K43ch4
 K4
 ch24
 K24
 ch44
 K44ch5
 K5
 ch25
 K25
 ch45
 K45ch6
 K6
 ch26
 K26
 ch46
 K46ch7
 K7
 ch27
 K27
 ch47
 K47ch8
 K8
 ch28
 K28
 ch48
 K48ch9
 K9
 ch29
 K29
 ch49
 K49ch10
 K10
 ch30
 K30
 ch50
 K50ch11
 K11
 ch31
 K31
 ch51
 K51ch12
 K12
 ch32
 K32
 ch52
 K52ch13
 K13
 ch33
 K33
 -
 -ch14
 K14
 ch34
 K34
 -
 -ch15
 K15
 ch35
 K35
 -
 -ch16
 K16
 ch36
 K36
 -
 -ch17
 K17
 ch37
 K37
 -
 -ch18
 K18
 ch38
 K38
 -
 -ch19
 K19
 ch39
 K39
 -
 -
3. Replace the relay. The NI PXI-2522 uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this. This can prevent the same unit from being
 reworked later on a lead-free solder station, which could contaminate the
 station. 
 Make sure you have the following: 
 
 Replace the relay as you would any other through-hole part. Trim the replaced
 relay leads to no more than 1 mm (0.04 inch) from the PCB.
  - Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free
 solder rework
  - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
  - Solder wick
  - Fine pick
  - Isopropyl alcohol
  - Cotton swabs

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2522

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2522-triggering.html language=enus -->
## TOPIC 00146: NI PXI-2522 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2522-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2522-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2522 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2522. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2522 Triggering

The NI PXI-2522 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2522.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2522.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2522

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2522.html language=enus -->
## TOPIC 00147: NI PXI-2522

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2522.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2522.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2522 is a 53-channel general-purpose relay module for the PXI platform. The NI PXI-2522 is composed of 53 armature non-latching SPDT relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switc

### NI PXI-2522

The NI PXI-2522 is a 53-channel general-purpose relay module for the PXI platform. The NI
 PXI-2522 is composed of 53 armature non-latching SPDT relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2522 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 53-SPDT | 2522/53-SPDT(NISWITCH_TOPOLOGY_2522_53_SPDT) |  |  |

#### Related Information:

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2522 53-SPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2523-26-dpdt-topology.html language=enus -->
## TOPIC 00148: NI PXI-2523 26-DPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2523-26-dpdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2523-26-dpdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2523 in the 26-DPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM o

### NI PXI-2523 26-DPDT Topology

The following figure represents the NI PXI-2523 in the 26-DPDT topology.

[IMAGE alt='image' src='GUID-0E8F7EEF-1E9F-4DFD-AFDF-1DE15A3A5953-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC
 terminal from the COM of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

To connect the NC terminal to the COM terminal of that channel, disconnect the NO
 terminal from the COM of that channel.

For example, to connect NC2 to COM2, use the following code:

niSwitch_Disconnect(vi, "no2", "com2")

niSwitch_Connect(vi, "nc2", "com2")

When scanning the NI PXI-2523, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2523 in the 26-DPDT
 topology.

[IMAGE alt='image' src='GUID-F212D6FA-E72F-48A2-9F4C-D7C1A9E0AA8C-a5.gif']

Parent topic:

NI PXI-2523

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2523-hardware-diagram.html language=enus -->
## TOPIC 00149: NI PXI-2523 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2523-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2523-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2523. The following table lists relay names for the NI PXI-2523. Relays k0...k25

### NI PXI-2523 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2523.

[IMAGE alt='image' src='GUID-0E8F7EEF-1E9F-4DFD-AFDF-1DE15A3A5953-a5.gif']

The following table lists relay names for the NI PXI-2523.

| Relays |
| --- |
| k0...k25 |

Parent topic:

NI PXI-2523

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2523-relay-replacement.html language=enus -->
## TOPIC 00150: NI PXI-2523 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2523-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2523-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2523 uses electromechanical armature relays. The NI PXI-2523 uses a custom lead length to meet safety standards. Trim leads to no more than 1 mm (0.04 inch) from the PCB. You also can use the spare relay included with the module at location K26. Refer to the following tables for informa

### NI PXI-2523 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following steps to disassemble your module and replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the front of the
 module. The following table maps the relay names to the channel names.
 ChannelName
 RelayName
 ChannelName
 RelayNamech0
 K0
 ch20
 K20ch1
 K1
 ch21
 K21ch2
 K2
 ch22
 K22ch3
 K3
 ch23
 K23ch4
 K4
 ch24
 K24ch5
 K5
 ch25
 K25ch6
 K6
 -
 -ch7
 K7
 -
 -ch8
 K8
 -
 -ch9
 K9
 -
 -ch10
 K10
 -
 -ch11
 K11
 -
 -ch12
 K12
 -
 -ch13
 K13
 -
 -ch14
 K14
 -
 -ch15
 K15
 -
 -ch16
 K16
 -
 -ch17
 K17
 -
 -ch18
 K18
 -
 -ch19
 K19
 -
 -
3. Replace the relay. The NI PXI-2523 uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this. This can prevent the same unit from being
 reworked later on a lead-free solder station, which could contaminate the
 station. 
 Make sure you have the following: 
 
 Replace the relay as you would any other through-hole part. Trim the replaced
 relay leads to no more than 1 mm (0.04 inch) from the PCB.
  - Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free
 solder rework
  - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
  - Solder wick
  - Fine pick
  - Isopropyl alcohol
  - Cotton swabs

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2523

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2523-triggering.html language=enus -->
## TOPIC 00151: NI PXI-2523 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2523-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2523-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2523 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2523. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2523 Triggering

The NI PXI-2523 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2523.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2523.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2523

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2523.html language=enus -->
## TOPIC 00152: NI PXI-2523

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2523.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2523.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2523 is an 26-channel general-purpose relay module for the PXI platform. The NI PXI-2523 is composed of 26 armature non-latching DPDT relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Swit

### NI PXI-2523

The NI PXI-2523 is an 26-channel general-purpose relay module for the PXI platform. The
 NI PXI-2523 is composed of 26 armature non-latching DPDT relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2523 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 26-DPDT | 2523/26-DPDT(NISWITCH_TOPOLOGY_2523_26_DPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2523 26-DPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-1-wire-4x32-matrix-topology.html language=enus -->
## TOPIC 00153: NI PXI-2530 1-Wire 4x32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-1-wire-4x32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-1-wire-4x32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 1-wire 4x32 matrix topology. Software Name NI PXI-2530Connector Pin Number NI TB-2631Terminal Name r0 141 ROW 0 r1 114 ROW 2 r2 9 ROW 4 r3 70 ROW 6 c0 1, 62, 106, 133 COLUMN 0 c1 45, 19, 151, 89 COLUMN 1 c2 2, 63, 107, 134 C

### NI PXI-2530 1-Wire 4x32 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530 in the 1-wire 4x32
 matrix topology.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Software Name | NI PXI-2530Connector Pin Number | NI TB-2631Terminal Name |
| --- | --- | --- |
| r0 | 141 | ROW 0 |
| r1 | 114 | ROW 2 |
| r2 | 9 | ROW 4 |
| r3 | 70 | ROW 6 |
| c0 | 1, 62, 106, 133 | COLUMN 0 |
| c1 | 45, 19, 151, 89 | COLUMN 1 |
| c2 | 2, 63, 107, 134 | COLUMN 2 |
| c3 | 46, 20, 152, 90 | COLUMN 3 |
| c4 | 3, 64, 108, 135 | COLUMN 4 |
| c5 | 47, 21, 153, 91 | COLUMN 5 |
| c6 | 4, 65, 109, 136 | COLUMN 6 |
| c7 | 48, 22, 154, 92 | COLUMN 7 |
| c8 | 5, 66, 110, 137 | COLUMN 8 |
| c9 | 49, 23, 155, 93 | COLUMN 9 |
| c10 | 6, 67, 111, 138 | COLUMN 10 |
| c11 | 50, 24, 156, 94 | COLUMN 11 |
| c12 | 7, 68, 112, 139 | COLUMN 12 |
| c13 | 51, 25, 157, 95 | COLUMN 13 |
| c14 | 8, 69, 113, 140 | COLUMN 14 |
| c15 | 52, 26, 158, 96 | COLUMN 15 |
| c16 | 10, 71, 115, 142 | COLUMN 16 |
| c17 | 54, 28, 160, 98 | COLUMN 17 |
| c18 | 11, 72, 116, 143 | COLUMN 18 |
| c19 | 55, 29, 161, 99 | COLUMN 19 |
| c20 | 12, 73, 117, 144 | COLUMN 20 |
| c21 | 56, 30, 162, 100 | COLUMN 21 |
| c22 | 13, 74, 118, 145 | COLUMN 22 |
| c23 | 57, 31, 163, 101 | COLUMN 23 |
| c24 | 14, 75, 119, 146 | COLUMN 24 |
| c25 | 58, 32, 164, 102 | COLUMN 25 |
| c26 | 15, 76, 120, 147 | COLUMN 26 |
| c27 | 59, 33, 165, 103 | COLUMN 27 |
| c28 | 16, 77, 121, 148 | COLUMN 28 |
| c29 | 60, 34, 166, 104 | COLUMN 29 |
| c30 | 17, 78, 122, 149 | COLUMN 30 |
| c31 | 61, 35, 167, 105 | COLUMN 31 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-1-wire-8x16-matrix-topology.html language=enus -->
## TOPIC 00154: NI PXI-2530 1-Wire 8x16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-1-wire-8x16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-1-wire-8x16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 1-wire 8x16 matrix topology. Software Name NI PXI-2530Connector Pin Number NI TB-2632Terminal Name r0 141 ROW 0 r1 97 ROW 1 r2 114 ROW 2 r3 159 ROW 3 r4 9 ROW 4 r5 53 ROW 5 r6 70 ROW 6 r7 27 ROW 7 c0 1, 62, 106, 133, 10, 71,

### NI PXI-2530 1-Wire 8x16 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530 in the 1-wire 8x16
 matrix topology.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Software Name | NI PXI-2530Connector Pin Number | NI TB-2632Terminal Name |
| --- | --- | --- |
| r0 | 141 | ROW 0 |
| r1 | 97 | ROW 1 |
| r2 | 114 | ROW 2 |
| r3 | 159 | ROW 3 |
| r4 | 9 | ROW 4 |
| r5 | 53 | ROW 5 |
| r6 | 70 | ROW 6 |
| r7 | 27 | ROW 7 |
| c0 | 1, 62, 106, 133, 10, 71, 115, 142 | COLUMN 0 |
| c1 | 45, 19, 151, 89, 54, 28, 160, 98 | COLUMN 1 |
| c2 | 2, 63, 107, 134, 11, 72, 116, 143 | COLUMN 2 |
| c3 | 46, 20, 152, 90, 55, 29, 161, 99 | COLUMN 3 |
| c4 | 3, 64, 108, 135, 12, 73, 117, 144 | COLUMN 4 |
| c5 | 47, 21, 153, 91, 56, 30, 162, 100 | COLUMN 5 |
| c6 | 4, 65, 109, 136, 13, 74, 118, 145 | COLUMN 6 |
| c7 | 48, 22, 154, 92, 57, 31, 163, 101 | COLUMN 7 |
| c8 | 5, 66, 110, 137, 14, 75, 119, 146 | COLUMN 8 |
| c9 | 49, 23, 155, 93, 58, 32, 164, 102 | COLUMN 9 |
| c10 | 6, 67, 111, 138, 15, 76, 120, 147 | COLUMN 10 |
| c11 | 50, 24, 156, 94, 59, 33, 165, 103 | COLUMN 11 |
| c12 | 7, 68, 112, 139, 16, 77, 121, 148 | COLUMN 12 |
| c13 | 51, 25, 157, 95, 60, 34, 166, 104 | COLUMN 13 |
| c14 | 8, 69, 113, 140, 17, 78, 122, 149 | COLUMN 14 |
| c15 | 52, 26, 158, 96, 61, 35, 167, 105 | COLUMN 15 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-1-wire-multiplexer-and-independen.html language=enus -->
## TOPIC 00155: NI PXI-2530 1-Wire Multiplexer and Independent Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-1-wire-multiplexer-and-independen.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-1-wire-multiplexer-and-independen.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 1-wire multiplexer and independent topologies. Single128x1 Dual64x1 Quad32x1 Octal16x1 Independent NI PXI-2530Connector Pin Number NI TB-2630Terminal Name com0 com0 com0 com0 com0 141 Bank 0, Pin 18 ── ── ── com1 com1 97 Ban

### NI PXI-2530 1-Wire Multiplexer and Independent Topologies

The following figure and table identify the pins for the NI PXI-2530 in the 1-wire
 multiplexer and independent topologies.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Single128x1 | Dual64x1 | Quad32x1 | Octal16x1 | Independent | NI PXI-2530Connector Pin Number | NI TB-2630Terminal Name |
| --- | --- | --- | --- | --- | --- | --- |
| com0 | com0 | com0 | com0 | com0 | 141 | Bank 0, Pin 18 |
| ── | ── | ── | com1 | com1 | 97 | Bank 1, Pin 18 |
| ── | ── | com2 | com2 | com2 | 114 | Bank 2, Pin 18 |
| ── | ── | ── | com3 | com3 | 159 | Bank 3, Pin 18 |
| ── | com4 | com4 | com4 | com4 | 9 | Bank 4, Pin 18 |
| ── | ── | ── | com5 | com5 | 53 | Bank 5, Pin 18 |
| ── | ── | com6 | com6 | com6 | 70 | Bank 6, Pin 18 |
| ── | ── | ── | com7 | com7 | 27 | Bank 7, Pin 18 |
| ── | ── | ── | ── | 1wref0 | 150 | Bank 0-1, Pin 17 |
| ── | ── | ── | ── | 1wref1 | 123 | Bank 2-3, Pin 17 |
| ── | ── | ── | ── | 1wref2 | 18 | Bank 4-5, Pin 17 |
| ── | ── | ── | ── | 1wref3 | 79 | Bank 6-7 Pin 17 |
| ch0 |  |  |  |  | 133 | Bank 0, Pin 1 |
| ch1 |  |  |  |  | 89 | Bank 0, Pin 2 |
| ch2 |  |  |  |  | 134 | Bank 0, Pin 3 |
| ch3 |  |  |  |  | 90 | Bank 0, Pin 4 |
| ch4 |  |  |  |  | 135 | Bank 0, Pin 5 |
| ch5 |  |  |  |  | 91 | Bank 0, Pin 6 |
| ch6 |  |  |  |  | 136 | Bank 0, Pin 7 |
| ch7 |  |  |  |  | 92 | Bank 0, Pin 8 |
| ch8 |  |  |  |  | 137 | Bank 0, Pin 9 |
| ch9 |  |  |  |  | 93 | Bank 0, Pin 10 |
| ch10 |  |  |  |  | 138 | Bank 0, Pin 11 |
| ch11 |  |  |  |  | 94 | Bank 0, Pin 12 |
| ch12 |  |  |  |  | 139 | Bank 0, Pin 13 |
| ch13 |  |  |  |  | 95 | Bank 0, Pin 14 |
| ch14 |  |  |  |  | 140 | Bank 0, Pin 15 |
| ch15 |  |  |  |  | 96 | Bank 0, Pin 16 |
| ch16 |  |  |  |  | 142 | Bank 1, Pin 1 |
| ch17 |  |  |  |  | 98 | Bank 1, Pin 2 |
| ch18 |  |  |  |  | 143 | Bank 1, Pin 3 |
| ch19 |  |  |  |  | 99 | Bank 1, Pin 4 |
| ch20 |  |  |  |  | 144 | Bank 1, Pin 5 |
| ch21 |  |  |  |  | 100 | Bank 1, Pin 6 |
| ch22 |  |  |  |  | 145 | Bank 1, Pin 7 |
| ch23 |  |  |  |  | 101 | Bank 1, Pin 8 |
| ch24 |  |  |  |  | 146 | Bank 1, Pin 9 |
| ch25 |  |  |  |  | 102 | Bank 1, Pin 10 |
| ch26 |  |  |  |  | 147 | Bank 1, Pin 11 |
| ch27 |  |  |  |  | 103 | Bank 1, Pin 12 |
| ch28 |  |  |  |  | 148 | Bank 1, Pin 13 |
| ch29 |  |  |  |  | 104 | Bank 1, Pin 14 |
| ch30 |  |  |  |  | 149 | Bank 1, Pin 15 |
| ch31 |  |  |  |  | 105 | Bank 1, Pin 16 |
| ch32 |  |  |  |  | 106 | Bank 2, Pin 1 |
| ch33 |  |  |  |  | 151 | Bank 2, Pin 2 |
| ch34 |  |  |  |  | 107 | Bank 2, Pin 3 |
| ch35 |  |  |  |  | 152 | Bank 2, Pin 4 |
| ch36 |  |  |  |  | 108 | Bank 2, Pin 5 |
| ch37 |  |  |  |  | 153 | Bank 2, Pin 6 |
| ch38 |  |  |  |  | 109 | Bank 2, Pin 7 |
| ch39 |  |  |  |  | 154 | Bank 2, Pin 8 |
| ch40 |  |  |  |  | 110 | Bank 2, Pin 9 |
| ch41 |  |  |  |  | 155 | Bank 2, Pin 10 |
| ch42 |  |  |  |  | 111 | Bank 2, Pin 11 |
| ch43 |  |  |  |  | 156 | Bank 2, Pin 12 |
| ch44 |  |  |  |  | 112 | Bank 2, Pin 13 |
| ch45 |  |  |  |  | 157 | Bank 2, Pin 14 |
| ch46 |  |  |  |  | 113 | Bank 2, Pin 15 |
| ch47 |  |  |  |  | 158 | Bank 2, Pin 16 |
| ch48 |  |  |  |  | 115 | Bank 3, Pin 1 |
| ch49 |  |  |  |  | 160 | Bank 3, Pin 2 |
| ch50 |  |  |  |  | 116 | Bank 3, Pin 3 |
| ch51 |  |  |  |  | 161 | Bank 3, Pin 4 |
| ch52 |  |  |  |  | 117 | Bank 3, Pin 5 |
| ch53 |  |  |  |  | 162 | Bank 3, Pin 6 |
| ch54 |  |  |  |  | 118 | Bank 3, Pin 7 |
| ch55 |  |  |  |  | 163 | Bank 3, Pin 8 |
| ch56 |  |  |  |  | 119 | Bank 3, Pin 9 |
| ch57 |  |  |  |  | 164 | Bank 3, Pin 10 |
| ch58 |  |  |  |  | 120 | Bank 3, Pin 11 |
| ch59 |  |  |  |  | 165 | Bank 3, Pin 12 |
| ch60 |  |  |  |  | 121 | Bank 3, Pin 13 |
| ch61 |  |  |  |  | 166 | Bank 3, Pin 14 |
| ch62 |  |  |  |  | 122 | Bank 3, Pin 15 |
| ch63 |  |  |  |  | 167 | Bank 3, Pin 16 |
| ch64 |  |  |  |  | 1 | Bank 4, Pin 1 |
| ch65 |  |  |  |  | 45 | Bank 4, Pin 2 |
| ch66 |  |  |  |  | 2 | Bank 4, Pin 3 |
| ch67 |  |  |  |  | 46 | Bank 4, Pin 4 |
| ch68 |  |  |  |  | 3 | Bank 4, Pin 5 |
| ch69 |  |  |  |  | 47 | Bank 4, Pin 6 |
| ch70 |  |  |  |  | 4 | Bank 4, Pin 7 |
| ch71 |  |  |  |  | 48 | Bank 4, Pin 8 |
| ch72 |  |  |  |  | 5 | Bank 4, Pin 9 |
| ch73 |  |  |  |  | 49 | Bank 4, Pin 10 |
| ch74 |  |  |  |  | 6 | Bank 4, Pin 11 |
| ch75 |  |  |  |  | 50 | Bank 4, Pin 12 |
| ch76 |  |  |  |  | 7 | Bank 4, Pin 13 |
| ch77 |  |  |  |  | 51 | Bank 4, Pin 14 |
| ch78 |  |  |  |  | 8 | Bank 4, Pin 15 |
| ch79 |  |  |  |  | 52 | Bank 4, Pin 16 |
| ch80 |  |  |  |  | 10 | Bank 5, Pin 1 |
| ch81 |  |  |  |  | 54 | Bank 5, Pin 2 |
| ch82 |  |  |  |  | 11 | Bank 5, Pin 3 |
| ch83 |  |  |  |  | 55 | Bank 5, Pin 4 |
| ch84 |  |  |  |  | 12 | Bank 5, Pin 5 |
| ch85 |  |  |  |  | 56 | Bank 5, Pin 6 |
| ch86 |  |  |  |  | 13 | Bank 5, Pin 7 |
| ch87 |  |  |  |  | 57 | Bank 5, Pin 8 |
| ch88 |  |  |  |  | 14 | Bank 5, Pin 9 |
| ch89 |  |  |  |  | 58 | Bank 5, Pin 10 |
| ch90 |  |  |  |  | 15 | Bank 5, Pin 11 |
| ch91 |  |  |  |  | 59 | Bank 5, Pin 12 |
| ch92 |  |  |  |  | 16 | Bank 5, Pin 13 |
| ch93 |  |  |  |  | 60 | Bank 5, Pin 14 |
| ch94 |  |  |  |  | 17 | Bank 5, Pin 15 |
| ch95 |  |  |  |  | 61 | Bank 5, Pin 16 |
| ch96 |  |  |  |  | 62 | Bank 6, Pin 1 |
| ch97 |  |  |  |  | 19 | Bank 6, Pin 2 |
| ch98 |  |  |  |  | 63 | Bank 6, Pin 3 |
| ch99 |  |  |  |  | 20 | Bank 6, Pin 4 |
| ch100 |  |  |  |  | 64 | Bank 6, Pin 5 |
| ch101 |  |  |  |  | 21 | Bank 6, Pin 6 |
| ch102 |  |  |  |  | 65 | Bank 6, Pin 7 |
| ch103 |  |  |  |  | 22 | Bank 6, Pin 8 |
| ch104 |  |  |  |  | 66 | Bank 6, Pin 9 |
| ch105 |  |  |  |  | 23 | Bank 6, Pin 10 |
| ch106 |  |  |  |  | 67 | Bank 6, Pin 11 |
| ch107 |  |  |  |  | 24 | Bank 6, Pin 12 |
| ch108 |  |  |  |  | 68 | Bank 6, Pin 13 |
| ch109 |  |  |  |  | 25 | Bank 6, Pin 14 |
| ch110 |  |  |  |  | 69 | Bank 6, Pin 15 |
| ch111 |  |  |  |  | 26 | Bank 6, Pin 16 |
| ch112 |  |  |  |  | 71 | Bank 7, Pin 1 |
| ch113 |  |  |  |  | 28 | Bank 7, Pin 2 |
| ch114 |  |  |  |  | 72 | Bank 7, Pin 3 |
| ch115 |  |  |  |  | 29 | Bank 7, Pin 4 |
| ch116 |  |  |  |  | 73 | Bank 7, Pin 5 |
| ch117 |  |  |  |  | 30 | Bank 7, Pin 6 |
| ch118 |  |  |  |  | 74 | Bank 7, Pin 7 |
| ch119 |  |  |  |  | 31 | Bank 7, Pin 8 |
| ch120 |  |  |  |  | 75 | Bank 7, Pin 9 |
| ch121 |  |  |  |  | 32 | Bank 7, Pin 10 |
| ch122 |  |  |  |  | 76 | Bank 7, Pin 11 |
| ch123 |  |  |  |  | 33 | Bank 7, Pin 12 |
| ch124 |  |  |  |  | 77 | Bank 7, Pin 13 |
| ch125 |  |  |  |  | 34 | Bank 7, Pin 14 |
| ch126 |  |  |  |  | 78 | Bank 7, Pin 15 |
| ch127 |  |  |  |  | 35 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2-wire-4x16-matrix-topology.html language=enus -->
## TOPIC 00156: NI PXI-2530 2-Wire 4x16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2-wire-4x16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2-wire-4x16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 2-wire 4x16 matrix topology. Software Name Polarity NI PXI-2530Connector Pin Number NI TB-2631Terminal Name r0 + 141 ROW 0 r0 – 97 ROW 1 r1 + 114 ROW 2 r1 – 159 ROW 3 r2 + 9 ROW 4 r2 – 53 ROW 5 r3 + 70 ROW 6 r3 – 27 ROW 7 c0

### NI PXI-2530 2-Wire 4x16 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530 in the 2-wire 4x16
 matrix topology.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Software Name | Polarity | NI PXI-2530Connector Pin Number | NI TB-2631Terminal Name |
| --- | --- | --- | --- |
| r0 | + | 141 | ROW 0 |
| r0 | – | 97 | ROW 1 |
| r1 | + | 114 | ROW 2 |
| r1 | – | 159 | ROW 3 |
| r2 | + | 9 | ROW 4 |
| r2 | – | 53 | ROW 5 |
| r3 | + | 70 | ROW 6 |
| r3 | – | 27 | ROW 7 |
| c0 | + | 1, 62, 106, 133 | COLUMN 0 |
| c0 | – | 45, 19, 151, 89 | COLUMN 16 |
| c1 | + | 2, 63, 107, 134 | COLUMN 1 |
| c1 | – | 46, 20, 152, 90 | COLUMN 17 |
| c2 | + | 3, 64, 108, 135 | COLUMN 2 |
| c2 | – | 47, 21, 153, 91 | COLUMN 18 |
| c3 | + | 4, 65, 109, 136 | COLUMN 3 |
| c3 | – | 48, 22,154, 92 | COLUMN 19 |
| c4 | + | 5, 66, 110, 137 | COLUMN 4 |
| c4 | – | 49, 23, 155, 93 | COLUMN 20 |
| c5 | + | 6, 67, 111, 138 | COLUMN 5 |
| c5 | – | 50, 24, 156, 94 | COLUMN 21 |
| c6 | + | 7, 68, 112, 139 | COLUMN 6 |
| c6 | – | 51, 25, 157, 95 | COLUMN 22 |
| c7 | + | 8, 69, 113, 140 | COLUMN 7 |
| c7 | – | 52, 26, 158, 96 | COLUMN 23 |
| c8 | + | 10, 71, 115, 142 | COLUMN 8 |
| c8 | – | 54, 28, 160, 98 | COLUMN 24 |
| c9 | + | 11, 72, 116, 143 | COLUMN 9 |
| c9 | – | 55, 29, 161, 99 | COLUMN 25 |
| c10 | + | 12, 73, 117, 144 | COLUMN 10 |
| c10 | – | 56, 30, 162, 100 | COLUMN 26 |
| c11 | + | 13, 74, 118, 145 | COLUMN 11 |
| c11 | – | 57, 31, 163, 101 | COLUMN 27 |
| c12 | + | 14, 75, 119, 146 | COLUMN 12 |
| c12 | – | 58, 32, 164, 102 | COLUMN 28 |
| c13 | + | 15, 76, 120, 147 | COLUMN 13 |
| c13 | – | 59, 33, 165, 103 | COLUMN 29 |
| c14 | + | 16, 77, 121, 148 | COLUMN 14 |
| c14 | – | 60, 34, 166, 104 | COLUMN 30 |
| c15 | + | 17, 78, 122, 149 | COLUMN 15 |
| c15 | – | 61, 35, 167, 105 | COLUMN 31 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2-wire-4x16-matrix-topology_2.html language=enus -->
## TOPIC 00157: NI PXI-2530 2-Wire 4x16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2-wire-4x16-matrix-topology_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2-wire-4x16-matrix-topology_2.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 2-wire 4x16 matrix topology. Software Name Polarity NI PXI-2530Connector Pin Number NI TB-2631Terminal Name r0 + 141 ROW 0 r0 – 97 ROW 1 r1 + 114 ROW 2 r1 – 159 ROW 3 r2 + 9 ROW 4 r2 – 53 ROW 5 r3 + 70 ROW 6 r3 – 27 ROW 7 c0

### NI PXI-2530 2-Wire 4x16 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530 in the 2-wire 4x16
 matrix topology.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Software Name | Polarity | NI PXI-2530Connector Pin Number | NI TB-2631Terminal Name |
| --- | --- | --- | --- |
| r0 | + | 141 | ROW 0 |
| r0 | – | 97 | ROW 1 |
| r1 | + | 114 | ROW 2 |
| r1 | – | 159 | ROW 3 |
| r2 | + | 9 | ROW 4 |
| r2 | – | 53 | ROW 5 |
| r3 | + | 70 | ROW 6 |
| r3 | – | 27 | ROW 7 |
| c0 | + | 1, 62, 106, 133 | COLUMN 0 |
| c0 | – | 45, 19, 151, 89 | COLUMN 16 |
| c1 | + | 2, 63, 107, 134 | COLUMN 1 |
| c1 | – | 46, 20, 152, 90 | COLUMN 17 |
| c2 | + | 3, 64, 108, 135 | COLUMN 2 |
| c2 | – | 47, 21, 153, 91 | COLUMN 18 |
| c3 | + | 4, 65, 109, 136 | COLUMN 3 |
| c3 | – | 48, 22,154, 92 | COLUMN 19 |
| c4 | + | 5, 66, 110, 137 | COLUMN 4 |
| c4 | – | 49, 23, 155, 93 | COLUMN 20 |
| c5 | + | 6, 67, 111, 138 | COLUMN 5 |
| c5 | – | 50, 24, 156, 94 | COLUMN 21 |
| c6 | + | 7, 68, 112, 139 | COLUMN 6 |
| c6 | – | 51, 25, 157, 95 | COLUMN 22 |
| c7 | + | 8, 69, 113, 140 | COLUMN 7 |
| c7 | – | 52, 26, 158, 96 | COLUMN 23 |
| c8 | + | 10, 71, 115, 142 | COLUMN 8 |
| c8 | – | 54, 28, 160, 98 | COLUMN 24 |
| c9 | + | 11, 72, 116, 143 | COLUMN 9 |
| c9 | – | 55, 29, 161, 99 | COLUMN 25 |
| c10 | + | 12, 73, 117, 144 | COLUMN 10 |
| c10 | – | 56, 30, 162, 100 | COLUMN 26 |
| c11 | + | 13, 74, 118, 145 | COLUMN 11 |
| c11 | – | 57, 31, 163, 101 | COLUMN 27 |
| c12 | + | 14, 75, 119, 146 | COLUMN 12 |
| c12 | – | 58, 32, 164, 102 | COLUMN 28 |
| c13 | + | 15, 76, 120, 147 | COLUMN 13 |
| c13 | – | 59, 33, 165, 103 | COLUMN 29 |
| c14 | + | 16, 77, 121, 148 | COLUMN 14 |
| c14 | – | 60, 34, 166, 104 | COLUMN 30 |
| c15 | + | 17, 78, 122, 149 | COLUMN 15 |
| c15 | – | 61, 35, 167, 105 | COLUMN 31 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2-wire-multiplexer-topologies.html language=enus -->
## TOPIC 00158: NI PXI-2530 2-Wire Multiplexer Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2-wire-multiplexer-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2-wire-multiplexer-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 2-wire multiplexer topologies. Polarity Single 64x1 Dual 32x1 Quad 16x1 NI PXI-2530 Connector Pin Number NI TB-2630 Terminal Name + com0 com0 com0 141 Bank 0, Pin 18 – com0 com0 com0 97 Bank 1, Pin 18 + ── ── com1 114 Bank 2

### NI PXI-2530 2-Wire Multiplexer Topologies

The following figure and table identify the pins for the NI PXI-2530 in the 2-wire
 multiplexer topologies.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Polarity | Single 64x1 | Dual 32x1 | Quad 16x1 | NI PXI-2530 Connector Pin Number | NI TB-2630 Terminal Name |
| --- | --- | --- | --- | --- | --- |
| + | com0 | com0 | com0 | 141 | Bank 0, Pin 18 |
| – | com0 | com0 | com0 | 97 | Bank 1, Pin 18 |
| + | ── | ── | com1 | 114 | Bank 2, Pin 18 |
| – | ── | ── | com1 | 159 | Bank 3, Pin 18 |
| + | ── | com1 | com2 | 9 | Bank 4, Pin 18 |
| – | ── | com1 | com2 | 53 | Bank 5, Pin 18 |
| + | ── | ── | com3 | 70 | Bank 6, Pin 18 |
| – | ── | ── | com3 | 27 | Bank 7, Pin 18 |
| + | ── | ── | ── | 150 | Bank 0-1, Pin 17 |
| – | ── | ── | ── | 123 | Bank 2-3, Pin 17 |
| + | ── | ── | ── | 18 | Bank 4-5, Pin 17 |
| – | ── | ── | ── | 79 | Bank 6-7 Pin 17 |
| + | ch0 | ch0 | ch0 | 133 | Bank 0, Pin 1 |
| – | ch0 | ch0 | ch0 | 142 | Bank 1, Pin 1 |
| + | ch1 | ch1 | ch1 | 135 | Bank 0, Pin 2 |
| – | ch1 | ch1 | ch1 | 144 | Bank 1, Pin 2 |
| + | ch2 | ch2 | ch2 | 137 | Bank 0, Pin 3 |
| – | ch2 | ch2 | ch2 | 146 | Bank 1, Pin 3 |
| + | ch3 | ch3 | ch3 | 139 | Bank 0, Pin 4 |
| – | ch3 | ch3 | ch3 | 148 | Bank 1, Pin 4 |
| + | ch4 | ch4 | ch4 | 141 | Bank 0, Pin 5 |
| – | ch4 | ch4 | ch4 | 150 | Bank 1, Pin 5 |
| + | ch5 | ch5 | ch5 | 143 | Bank 0, Pin 6 |
| – | ch5 | ch5 | ch5 | 152 | Bank 1, Pin 6 |
| + | ch6 | ch6 | ch6 | 145 | Bank 0, Pin 7 |
| – | ch6 | ch6 | ch6 | 154 | Bank 1, Pin 7 |
| + | ch7 | ch7 | ch7 | 147 | Bank 0, Pin 8 |
| – | ch7 | ch7 | ch7 | 156 | Bank 1, Pin 8 |
| + | ch8 | ch8 | ch8 | 149 | Bank 0, Pin 9 |
| – | ch8 | ch8 | ch8 | 158 | Bank 1, Pin 9 |
| + | ch9 | ch9 | ch9 | 151 | Bank 0, Pin 10 |
| – | ch9 | ch9 | ch9 | 160 | Bank 1, Pin 10 |
| + | ch10 | ch10 | ch10 | 153 | Bank 0, Pin 11 |
| – | ch10 | ch10 | ch10 | 162 | Bank 1, Pin 11 |
| + | ch11 | ch11 | ch11 | 155 | Bank 0, Pin 12 |
| – | ch11 | ch11 | ch11 | 164 | Bank 1, Pin 12 |
| + | ch12 | ch12 | ch12 | 157 | Bank 0, Pin 13 |
| – | ch12 | ch12 | ch12 | 166 | Bank 1, Pin 13 |
| + | ch13 | ch13 | ch13 | 159 | Bank 0, Pin 14 |
| – | ch13 | ch13 | ch13 | 168 | Bank 1, Pin 14 |
| + | ch14 | ch14 | ch14 | 161 | Bank 0, Pin 15 |
| – | ch14 | ch14 | ch14 | 170 | Bank 1, Pin 15 |
| + | ch15 | ch15 | ch15 | 163 | Bank 0, Pin 16 |
| – | ch15 | ch15 | ch15 | 172 | Bank 1, Pin 16 |
| + | ch16 | ch16 | ch16 | 106 | Bank 2, Pin 1 |
| – | ch16 | ch16 | ch16 | 115 | Bank 3, Pin 1 |
| + | ch17 | ch17 | ch17 | 108 | Bank 2, Pin 2 |
| – | ch17 | ch17 | ch17 | 117 | Bank 3, Pin 2 |
| + | ch18 | ch18 | ch18 | 110 | Bank 2, Pin 3 |
| – | ch18 | ch18 | ch18 | 119 | Bank 3, Pin 3 |
| + | ch19 | ch19 | ch19 | 112 | Bank 2, Pin 4 |
| – | ch19 | ch19 | ch19 | 121 | Bank 3, Pin 4 |
| + | ch20 | ch20 | ch20 | 114 | Bank 2, Pin 5 |
| – | ch20 | ch20 | ch20 | 123 | Bank 3, Pin 5 |
| + | ch21 | ch21 | ch21 | 116 | Bank 2, Pin 6 |
| – | ch21 | ch21 | ch21 | 125 | Bank 3, Pin 6 |
| + | ch22 | ch22 | ch22 | 118 | Bank 2, Pin 7 |
| – | ch22 | ch22 | ch22 | 127 | Bank 3, Pin 7 |
| + | ch23 | ch23 | ch23 | 120 | Bank 2, Pin 8 |
| – | ch23 | ch23 | ch23 | 129 | Bank 3, Pin 8 |
| + | ch24 | ch24 | ch24 | 122 | Bank 2, Pin 9 |
| – | ch24 | ch24 | ch24 | 131 | Bank 3, Pin 9 |
| + | ch25 | ch25 | ch25 | 124 | Bank 2, Pin 10 |
| – | ch25 | ch25 | ch25 | 133 | Bank 3, Pin 10 |
| + | ch26 | ch26 | ch26 | 126 | Bank 2, Pin 11 |
| – | ch26 | ch26 | ch26 | 135 | Bank 3, Pin 11 |
| + | ch27 | ch27 | ch27 | 128 | Bank 2, Pin 12 |
| – | ch27 | ch27 | ch27 | 137 | Bank 3, Pin 12 |
| + | ch28 | ch28 | ch28 | 130 | Bank 2, Pin 13 |
| – | ch28 | ch28 | ch28 | 139 | Bank 3, Pin 13 |
| + | ch29 | ch29 | ch29 | 132 | Bank 2, Pin 14 |
| – | ch29 | ch29 | ch29 | 141 | Bank 3, Pin 14 |
| + | ch30 | ch30 | ch30 | 134 | Bank 2, Pin 15 |
| – | ch30 | ch30 | ch30 | 143 | Bank 3, Pin 15 |
| + | ch31 | ch31 | ch31 | 136 | Bank 2, Pin 16 |
| – | ch31 | ch31 | ch31 | 145 | Bank 3, Pin 16 |
| + | ch32 | ch32 | ch32 | 1 | Bank 4, Pin 1 |
| – | ch32 | ch32 | ch32 | 10 | Bank 5, Pin 1 |
| + | ch33 | ch33 | ch33 | 3 | Bank 4, Pin 2 |
| – | ch33 | ch33 | ch33 | 12 | Bank 5, Pin 2 |
| + | ch34 | ch34 | ch34 | 5 | Bank 4, Pin 3 |
| – | ch34 | ch34 | ch34 | 14 | Bank 5, Pin 3 |
| + | ch35 | ch35 | ch35 | 7 | Bank 4, Pin 4 |
| – | ch35 | ch35 | ch35 | 16 | Bank 5, Pin 4 |
| + | ch36 | ch36 | ch36 | 9 | Bank 4, Pin 5 |
| – | ch36 | ch36 | ch36 | 18 | Bank 5, Pin 5 |
| + | ch37 | ch37 | ch37 | 11 | Bank 4, Pin 6 |
| – | ch37 | ch37 | ch37 | 20 | Bank 5, Pin 6 |
| + | ch38 | ch38 | ch38 | 13 | Bank 4, Pin 7 |
| – | ch38 | ch38 | ch38 | 22 | Bank 5, Pin 7 |
| + | ch39 | ch39 | ch39 | 15 | Bank 4, Pin 8 |
| – | ch39 | ch39 | ch39 | 24 | Bank 5, Pin 8 |
| + | ch40 | ch40 | ch40 | 17 | Bank 4, Pin 9 |
| – | ch40 | ch40 | ch40 | 26 | Bank 5, Pin 9 |
| + | ch41 | ch41 | ch41 | 19 | Bank 4, Pin 10 |
| – | ch41 | ch41 | ch41 | 28 | Bank 5, Pin 10 |
| + | ch42 | ch42 | ch42 | 21 | Bank 4, Pin 11 |
| – | ch42 | ch42 | ch42 | 30 | Bank 5, Pin 11 |
| + | ch43 | ch43 | ch43 | 23 | Bank 4, Pin 12 |
| – | ch43 | ch43 | ch43 | 32 | Bank 5, Pin 12 |
| + | ch44 | ch44 | ch44 | 25 | Bank 4, Pin 13 |
| – | ch44 | ch44 | ch44 | 34 | Bank 5, Pin 13 |
| + | ch45 | ch45 | ch45 | 27 | Bank 4, Pin 14 |
| – | ch45 | ch45 | ch45 | 36 | Bank 5, Pin 14 |
| + | ch46 | ch46 | ch46 | 29 | Bank 4, Pin 15 |
| – | ch46 | ch46 | ch46 | 38 | Bank 5, Pin 15 |
| + | ch47 | ch47 | ch47 | 31 | Bank 4, Pin 16 |
| – | ch47 | ch47 | ch47 | 40 | Bank 5, Pin 16 |
| + | ch48 | ch48 | ch48 | 62 | Bank 6, Pin 1 |
| – | ch48 | ch48 | ch48 | 71 | Bank 7, Pin 1 |
| + | ch49 | ch49 | ch49 | 64 | Bank 6, Pin 2 |
| – | ch49 | ch49 | ch49 | 73 | Bank 7, Pin 2 |
| + | ch50 | ch50 | ch50 | 66 | Bank 6, Pin 3 |
| – | ch50 | ch50 | ch50 | 75 | Bank 7, Pin 3 |
| + | ch51 | ch51 | ch51 | 68 | Bank 6, Pin 4 |
| – | ch51 | ch51 | ch51 | 77 | Bank 7, Pin 4 |
| + | ch52 | ch52 | ch52 | 70 | Bank 6, Pin 5 |
| – | ch52 | ch52 | ch52 | 79 | Bank 7, Pin 5 |
| + | ch53 | ch53 | ch53 | 72 | Bank 6, Pin 6 |
| – | ch53 | ch53 | ch53 | 81 | Bank 7, Pin 6 |
| + | ch54 | ch54 | ch54 | 74 | Bank 6, Pin 7 |
| – | ch54 | ch54 | ch54 | 83 | Bank 7, Pin 7 |
| + | ch55 | ch55 | ch55 | 76 | Bank 6, Pin 8 |
| – | ch55 | ch55 | ch55 | 85 | Bank 7, Pin 8 |
| + | ch56 | ch56 | ch56 | 78 | Bank 6, Pin 9 |
| – | ch56 | ch56 | ch56 | 87 | Bank 7, Pin 9 |
| + | ch57 | ch57 | ch57 | 80 | Bank 6, Pin 10 |
| – | ch57 | ch57 | ch57 | 89 | Bank 7, Pin 10 |
| + | ch58 | ch58 | ch58 | 82 | Bank 6, Pin 11 |
| – | ch58 | ch58 | ch58 | 91 | Bank 7, Pin 11 |
| + | ch59 | ch59 | ch59 | 84 | Bank 6, Pin 12 |
| – | ch59 | ch59 | ch59 | 93 | Bank 7, Pin 12 |
| + | ch60 | ch60 | ch60 | 86 | Bank 6, Pin 13 |
| – | ch60 | ch60 | ch60 | 95 | Bank 7, Pin 13 |
| + | ch61 | ch61 | ch61 | 88 | Bank 6, Pin 14 |
| – | ch61 | ch61 | ch61 | 97 | Bank 7, Pin 14 |
| + | ch62 | ch62 | ch62 | 90 | Bank 6, Pin 15 |
| – | ch62 | ch62 | ch62 | 99 | Bank 7, Pin 15 |
| + | ch63 | ch63 | ch63 | 92 | Bank 6, Pin 16 |
| – | ch63 | ch63 | ch63 | 101 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-128-1-multiplexer-to.html language=enus -->
## TOPIC 00159: NI PXI-2530/2530B 1-Wire 128×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-128-1-multiplexer-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-128-1-multiplexer-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire 128×1 multiplexer. In this topology, all channel terminals (CH0 through CH127) route to COM0. A reference, 1WREF0, always remains connected to COM1. The pair, COM0 and COM1, is provided for convenient connectivity to a 2-

### NI PXI-2530/2530B 1-Wire 128×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire 128×1
 multiplexer. In this topology, all channel terminals (CH0 through CH127) route to COM0.
 A reference, 1WREF0, always remains connected to COM1. The pair, COM0 and COM1, is
 provided for convenient connectivity to a 2-wire device, such as a DMM.

When using the 1-wire 128x1 topology, COM1 connects only to 1WREF0 and can optionally be
 used to route the second wire of a differential signal through the switch. This is
 useful to keep the path lengths and routing conditions similar on the differential pair,
 but is not necessary.

The following figure represents the NI PXI-2530/2530B in the 1-wire 128×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-BFDCDA01-8731-41A0-A197-1A8072E581CE-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connection:

signal connected to CH2 is routed to COM0

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-4-32-matrix-topology.html language=enus -->
## TOPIC 00160: NI PXI-2530/2530B 1-Wire 4×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-4-32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-4-32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2631/2631B terminal block with the NI PXI-2530/2530B as a 1-wire 4×32 matrix. The following figure represents the NI PXI-2530/2530B in the 1-wire 4×32 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or t

### NI PXI-2530/2530B 1-Wire 4×32 Matrix Topology

Use the NI TB-2631/2631B terminal block with the NI PXI-2530/2530B as a 1-wire 4×32
 matrix.

The following figure represents the NI PXI-2530/2530B in the 1-wire 4×32 matrix topology.

[IMAGE alt='image' src='GUID-B7E7E415-2AE9-4981-AA8B-BAE6CB513D72-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2631 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2631B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-8-16-matrix-topology.html language=enus -->
## TOPIC 00161: NI PXI-2530/2530B 1-Wire 8×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-8-16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-8-16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2632/2632B terminal block with the NI PXI-2530/2530B as a 1-wire 8×16 matrix. The following figure represents the NI PXI-2530/2530B in the 1-wire 8×16 matrix topology. Making a Connection Both the scanning command, r1->c1;, and the immediate operation, niSwitch Connect Channels VI or t

### NI PXI-2530/2530B 1-Wire 8×16 Matrix Topology

Use the NI TB-2632/2632B terminal block with the NI PXI-2530/2530B as a 1-wire 8×16
 matrix.

The following figure represents the NI PXI-2530/2530B in the 1-wire 8×16 matrix topology.

[IMAGE alt='image' src='GUID-DC0949D7-85DF-413E-9426-0333A500F829-a5.gif']

#### Making a Connection

Both the scanning command, r1->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r1 and c1, result in the
 following connection:

signal connected to R1 is routed to C1

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2632 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2632B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-dual-64-1-multiplexe.html language=enus -->
## TOPIC 00162: NI PXI-2530/2530B 1-Wire Dual 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-dual-64-1-multiplexe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-dual-64-1-multiplexe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire dual 64×1 multiplexer. In this topology, channel terminals CH0 through CH63 route to COM0. A reference, 1WREF0, always remains connected to COM1. Channel terminals CH64 through CH127 route to COM4. A reference, 1WREF2, al

### NI PXI-2530/2530B 1-Wire Dual 64×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire dual 64×1
 multiplexer. In this topology, channel terminals CH0 through CH63 route to COM0. A
 reference, 1WREF0, always remains connected to COM1.

Channel terminals CH64 through CH127 route to COM4. A reference, 1WREF2, always remains
 connected to COM5.

The following figure represents the NI PXI-2530/2530B in the 1-wire dual 64×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-BD2066C7-788C-43DB-A91D-58897E9DF6A6-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connection:

signal connected to CH2 is routed to COM0

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-octal-16-1-multiplex.html language=enus -->
## TOPIC 00163: NI PXI-2530/2530B 1-Wire Octal 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-octal-16-1-multiplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-octal-16-1-multiplex.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire octal 16×1 multiplexer. In this topology, channel terminals CH0 through CH15 route to COM0. All other banks follow a similar routing scheme. The following figure represents the NI PXI-2530/2530B in the 1-wire octal 16×1 m

### NI PXI-2530/2530B 1-Wire Octal 16×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire octal 16×1
 multiplexer. In this topology, channel terminals CH0 through CH15 route to COM0. All
 other banks follow a similar routing scheme.

The following figure represents the NI PXI-2530/2530B in the 1-wire octal 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-7038838D-CF42-4EA9-BE82-E2A34B785551-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connection:

signal connected to CH2 is routed to COM0

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-1-wire-quad-32-1-multiplexe.html language=enus -->
## TOPIC 00164: NI PXI-2530/2530B 1-Wire Quad 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-1-wire-quad-32-1-multiplexe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-1-wire-quad-32-1-multiplexe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire quad 32×1 multiplexer. In this topology, channel terminals CH0 through CH31 route to COM0, CH32 through CH63 route to COM2, CH64 through CH95 route to COM4, and CH96 through CH127 route to COM6. A reference, 1WREF0, alway

### NI PXI-2530/2530B 1-Wire Quad 32×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 1-wire quad 32×1
 multiplexer. In this topology, channel terminals CH0 through CH31 route to COM0, CH32
 through CH63 route to COM2, CH64 through CH95 route to COM4, and CH96 through CH127
 route to COM6. A reference, 1WREF0, always remains connected to COM1.

The following figure represents the NI PXI-2530/2530B in the 1-wire quad 32×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-8EF2782F-0B6C-4B2E-8283-48A1539745B5-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connection:

signal connected to CH2 is routed to COM0

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-2-wire-4-16-matrix-topology.html language=enus -->
## TOPIC 00165: NI PXI-2530/2530B 2-Wire 4×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-2-wire-4-16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-2-wire-4-16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2631/2631B terminal block with the NI PXI-2530/2530B as a 2-wire 4×16 matrix. The following figure represents the NI PXI-2530/2530B in the 2-wire 4×16 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or t

### NI PXI-2530/2530B 2-Wire 4×16 Matrix Topology

Use the NI TB-2631/2631B terminal block with the NI PXI-2530/2530B as a 2-wire 4×16
 matrix.

The following figure represents the NI PXI-2530/2530B in the 2-wire 4×16 matrix topology.

[IMAGE alt='image' src='GUID-F9FBA2D0-9A6A-4F58-9E50-3A325A5E109B-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connections:

signal connected to R2+ is routed to C1+

signal connected to R2– is routed to C1–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2631 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2631B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-2-wire-64-1-multiplexer-top.html language=enus -->
## TOPIC 00166: NI PXI-2530/2530B 2-Wire 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-2-wire-64-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-2-wire-64-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire 64×1 multiplexer. In this topology, all positive leads (CH0+ through CH63+) route to COM0+, and all negative leads (CH0– through CH63–) route to COM0–. The pair COM0+ and COM0– is addressed collectively as com0 in softwar

### NI PXI-2530/2530B 2-Wire 64×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire 64×1
 multiplexer. In this topology, all positive leads (CH0+ through CH63+) route to COM0+,
 and all negative leads (CH0– through CH63–) route to COM0–. The pair COM0+ and COM0– is
 addressed collectively as com0 in software.

The following figure represents the NI PXI-2530/2530B in the 2-wire 64×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-2ABA6550-0147-4AA1-A400-9AAC60A83D7B-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to CH2+ is routed to COM0+

signal connected to CH2– is routed to COM0–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-2-wire-dual-32-1-multiplexe.html language=enus -->
## TOPIC 00167: NI PXI-2530/2530B 2-Wire Dual 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-2-wire-dual-32-1-multiplexe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-2-wire-dual-32-1-multiplexe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire dual 32×1 multiplexer. In this topology, the positive leads of the first bank (CH0+ through CH31+) route to COM0+, and the negative leads of the first bank (CH0– through CH31–) route to COM0–. The pair COM0+ and COM0– is

### NI PXI-2530/2530B 2-Wire Dual 32×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire dual 32×1
 multiplexer. In this topology, the positive leads of the first bank (CH0+ through CH31+)
 route to COM0+, and the negative leads of the first bank (CH0– through CH31–) route to
 COM0–. The pair COM0+ and COM0– is addressed collectively as com0 in software. The other
 bank follows a similar routing scheme.

The following figure represents the NI PXI-2530/2530B in the 2-wire dual 32×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-EAB32E8F-C7B2-48AD-98C7-0AE7524B8D55-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to CH2+ is routed to COM0+

signal connected to CH2– is routed to COM0–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-2-wire-quad-16-1-multiplexe.html language=enus -->
## TOPIC 00168: NI PXI-2530/2530B 2-Wire Quad 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-2-wire-quad-16-1-multiplexe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-2-wire-quad-16-1-multiplexe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire quad 16×1 multiplexer. In this topology, the positive leads of the first bank (CH0+ through CH15+) route to COM0+, and the negative leads of the first bank (CH0– through CH15–) route to COM0–. The pair COM0+ and COM0– is

### NI PXI-2530/2530B 2-Wire Quad 16×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 2-wire quad 16×1
 multiplexer. In this topology, the positive leads of the first bank (CH0+ through CH15+)
 route to COM0+, and the negative leads of the first bank (CH0– through CH15–) route to
 COM0–. The pair COM0+ and COM0– is addressed collectively as com0 in software. All other
 banks follow a similar routing scheme.

The following figure represents the NI PXI-2530/2530B in the 2-wire quad 16×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-54B7703C-7546-4EFF-AA77-1733FC63647E-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to CH2+ is routed to COM0+

signal connected to CH2– is routed to COM0–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-4-wire-32-1-multiplexer-top.html language=enus -->
## TOPIC 00169: NI PXI-2530/2530B 4-Wire 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-4-wire-32-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-4-wire-32-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 4-wire 32×1 multiplexer. In this topology, all positive "A" leads (CH0A+ through CH31A+) route to COM0A+. All negative "A" leads (CH0A– through CH31A–) route to COM0A–. All positive "B" leads (CH0B+ through CH31B+) route to COM0

### NI PXI-2530/2530B 4-Wire 32×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 4-wire 32×1
 multiplexer. In this topology, all positive "A" leads (CH0A+ through CH31A+) route to
 COM0A+. All negative "A" leads (CH0A– through CH31A–) route to COM0A–. All positive "B"
 leads (CH0B+ through CH31B+) route to COM0B+. All negative "B" leads (CH0B– through
 CH31B–) route to COM0B–. COM0A+, COM0A–, COM0B+, and COM0B– are addressed collectively
 as com0 in software.

The following figure represents the NI PXI-2530/2530B in the 4-wire 32×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-8B13BDAD-EBA3-48B6-B32B-5C0D92B542DA-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to CH2A+ is routed to COM0A+

signal connected to CH2A– is routed to COM0A–

signal connected to CH2B+ is routed to COM0B+

signal connected to CH2B– is routed to COM0B–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-4-wire-dual-16-1-multiplexe.html language=enus -->
## TOPIC 00170: NI PXI-2530/2530B 4-Wire Dual 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-4-wire-dual-16-1-multiplexe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-4-wire-dual-16-1-multiplexe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 4-wire dual 16×1 multiplexer. In this topology, the positive "A" leads of the first bank (CH0A+ through CH15A+) route to COM0A+. The negative "A" leads of the first bank (CH0A– through CH15B–) route to COM0A–. The positive "B" l

### NI PXI-2530/2530B 4-Wire Dual 16×1 Multiplexer Topology

Use the NI TB-2630/2630B terminal block with the NI PXI-2530/2530B as a 4-wire dual 16×1
 multiplexer. In this topology, the positive "A" leads of the first bank (CH0A+ through
 CH15A+) route to COM0A+. The negative "A" leads of the first bank (CH0A– through CH15B–)
 route to COM0A–. The positive "B" leads of the first bank (CH0B+ through CH15B+) route
 to COM0B+. The negative "B" leads of the first bank (CH0B– through CH15B–) route to
 COM0B-. COM0A+, COM0A–, COM0B+, and COM0B– are addressed collectively as com0 in
 software. The other bank follows a similar routing scheme.

The following figure represents the NI PXI-2530/2530B in the 4-wire dual 16×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-C5AF489C-550D-42E2-BAE6-79847D355FF8-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to CH2A+ is routed to COM0A+

signal connected to CH2A– is routed to COM0A–

signal connected to CH2B+ is routed to COM0B+

signal connected to CH2B– is routed to COM0B–

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- N-Wire Switching Modes
- Multiplexer
- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-hardware-diagram.html language=enus -->
## TOPIC 00171: NI PXI-2530/2530B Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2530/2530B.

### NI PXI-2530/2530B Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2530/2530B.

[IMAGE alt='image' src='GUID-EE0B91B4-0943-4722-A89C-0E959714E77A-a5.gif']

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-independent-topology.html language=enus -->
## TOPIC 00172: NI PXI-2530/2530B Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2530/2530B in the independent topology, connect your signals using the NI TB-2630/2630B terminal block. Select this topology to utilize the full routing capabilities of the NI PXI-2530/2530B. When using the independent topology, always select NONE in MAX for the terminal bloc

### NI PXI-2530/2530B Independent Topology

Note

NONE

[IMAGE alt='image' src='GUID-3175ACA1-A7E0-4947-BEBB-38FC08776495-a5.gif']

#### Making a Connection

With the independent topology, you can let NI-SWITCH determine the path between two
 specified channels by setting the intermediate channels as reserved for routing and
 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function, or you can control individual relays using the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function.

#### Signal Connections

Refer to the NI PXI-2530 Signal Connections section for the NI PXI-2530 front
 connector pinout and NI TB-2630 terminal mapping. Refer to the NI PXI-2530B Signal
 Connections section for the NI PXI-2530B front connector pinout and NI TB-2630B
 terminal mapping.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- NI PXI-2530 Signal Connections
- NI PXI-2530B Signal Connections

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-matrix-expansion.html language=enus -->
## TOPIC 00173: NI PXI-2530/2530B Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the NI PXI-2530/2530B matrix using either the NI TB-2631/2631B or NI TB-2632/2632B terminal block. The terminal block you are using determines the matrix expansion procedure you will follow. The following table lists the terminal blocks and matrix topologies available for the NI PXI-2

### NI PXI-2530/2530B Matrix Expansion

You can expand the NI PXI-2530/2530B matrix using either the NI TB-2631/2631B or
 NI TB-2632/2632B terminal block. The terminal block you are using determines the matrix
 expansion procedure you will follow. The following table lists the terminal blocks and
 matrix topologies available for the NI PXI-2530/2530B.

| Terminal Block | Topology(Row x Column) |
| --- | --- |
| NI TB-2631/2631B | 1-wire 4×32, 2-wire 4×16 |
| NI TB-2632/2632B | 1-wire 8×16 |

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b-triggering.html language=enus -->
## TOPIC 00174: NI PXI-2530/2530B Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2530/2530B can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2530/2530B. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL

### NI PXI-2530/2530B Triggering

The NI PXI-2530/2530B can recognize trigger pulse widths less than 150 ns by disabling
 digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2530/2530B.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG IN on NI terminal block |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2530/2530B.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG OUT on NI terminal block |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2530/2530B

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-2530b.html language=enus -->
## TOPIC 00175: NI PXI-2530/2530B

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-2530b.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-2530b.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2530 and NI PXI-2530B are high-density multiplexer/matrix switch modules for the PXI platform. The NI PXI-2530/2530B uses reed relays. A number of factors can affect the life expectancy of reed relays. Refer to Reed Relay Protection for information about protecting reed relays. Refer to t

### NI PXI-2530/2530B

The NI PXI-2530 and NI PXI-2530B are high-density multiplexer/matrix switch modules for
 the PXI platform. The NI PXI-2530/2530B uses reed relays.

A number of factors can affect the life expectancy of reed relays. Refer to Reed Relay
 Protection for information about protecting reed relays.

Note

#### Operation Modes

The following table lists the supported topologies of the NI PXI-2530/2530B and
 possible operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 128×1 Multiplexer | 2530/1-Wire 128x1 Mux(NISWITCH_TOPOLOGY_2530_1_WIRE_128X1_MUX) |  |  |
| 1-Wire Dual 64×1 Multiplexer | 2530/1-Wire Dual 64x1 Mux(NISWITCH_TOPOLOGY_2530_1_WIRE_DUAL_64X1_MUX) |  |  |
| 1-Wire Quad 32×1 Multiplexer | 2530/1-Wire Quad 32x1 Mux(NISWITCH_TOPOLOGY_2530_1_WIRE_QUAD_32X1_MUX) |  |  |
| 1-Wire Octal 16×1 Multiplexer | 2530/1-Wire Octal 16x1 Mux(NISWITCH_TOPOLOGY_2530_1_WIRE_OCTAL_16X1_MUX) |  |  |
| 2-Wire 64×1 Multiplexer | 2530/2-Wire 64x1 Mux(NISWITCH_TOPOLOGY_2530_2_WIRE_64X1_MUX) |  |  |
| 2-Wire Dual 32×1 Multiplexer | 2530/2-Wire Dual 32x1 Mux(NISWITCH_TOPOLOGY_2530_2_WIRE_DUAL_32X1_MUX) |  |  |
| 2-Wire Quad 16×1 Multiplexer | 2530/2-Wire Quad 16x1 Mux(NISWITCH_TOPOLOGY_2530_2_WIRE_QUAD_16X1_MUX) |  |  |
| 4-Wire 32×1 Multiplexer | 2530/4-Wire 32x1 Mux(NISWITCH_TOPOLOGY_2530_4_WIRE_32X1_MUX) |  |  |
| 4-Wire Dual 16×1 Multiplexer | 2530/4-Wire Dual 16x1 Mux(NISWITCH_TOPOLOGY_2530_4_WIRE_DUAL_16X1_MUX) |  |  |
| 1-Wire 4×32 Matrix | 2530/1-Wire 4x32 Matrix(NISWITCH_TOPOLOGY_2530_1_WIRE_4X32_MATRIX) |  |  |
| 1-Wire 8×16 Matrix | 2530/1-Wire 8x16 Matrix(NISWITCH_TOPOLOGY_2530_1_WIRE_8X16_MATRIX) |  |  |
| 2-Wire 4×16 Matrix | 2530/2-Wire 4x16 Matrix(NISWITCH_TOPOLOGY_2530_2_WIRE_4X16_MATRIX) |  |  |
| Independent | 2530/Independent(NISWITCH_TOPOLOGY_2530_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- NI PXI-2530/2530B 1-Wire 128×1 Multiplexer Topology
- NI PXI-2530/2530B 1-Wire Dual 64×1 Multiplexer Topology
- NI PXI-2530/2530B 1-Wire Quad 32×1 Multiplexer Topology
- NI PXI-2530/2530B 1-Wire Octal 16×1 Multiplexer Topology
- NI PXI-2530/2530B 2-Wire 64×1 Multiplexer Topology
- NI PXI-2530/2530B 2-Wire Dual 32×1 Multiplexer Topology
- NI PXI-2530/2530B 2-Wire Quad 16×1 Multiplexer Topology
- NI PXI-2530/2530B 4-Wire 32×1 Multiplexer Topology
- NI PXI-2530/2530B 4-Wire Dual 16×1 Multiplexer Topology
- NI PXI-2530/2530B 1-Wire 4×32 Matrix Topology
- NI PXI-2530/2530B 1-Wire 8×16 Matrix Topology
- NI PXI-2530/2530B 2-Wire 4×16 Matrix Topology
- NI PXI-2530/2530B Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-4-wire-multiplexer-topologies.html language=enus -->
## TOPIC 00176: NI PXI-2530 4-Wire Multiplexer Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-4-wire-multiplexer-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-4-wire-multiplexer-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530 in the 4-wire multiplexer topologies. Polarity Single 32x1 Dual 16x1 NI PXI-2530 Connector Pin Number NI TB-2630 Terminal Name A+ com0 com0 141 Bank 0, Pin 18 A- com0 com0 97 Bank 1, Pin 18 B+ com0 com0 9 Bank 4, Pin 18 B- com0 com

### NI PXI-2530 4-Wire Multiplexer Topologies

The following figure and table identify the pins for the NI PXI-2530 in the 4-wire
 multiplexer topologies.

[IMAGE alt='image' src='GUID-A28BF4ED-8078-4A0D-8C8B-86BC539A8201-a5.gif']

| Polarity | Single 32x1 | Dual 16x1 | NI PXI-2530 Connector Pin Number | NI TB-2630 Terminal Name |
| --- | --- | --- | --- | --- |
| A+ | com0 | com0 | 141 | Bank 0, Pin 18 |
| A- | com0 | com0 | 97 | Bank 1, Pin 18 |
| B+ | com0 | com0 | 9 | Bank 4, Pin 18 |
| B- | com0 | com0 | 53 | Bank 5, Pin 18 |
| A+ | ── | com1 | 114 | Bank 2, Pin 18 |
| A- | ── | com1 | 159 | Bank 3, Pin 18 |
| B+ | ── | com1 | 70 | Bank 6, Pin 18 |
| B- | ── | com1 | 27 | Bank 7, Pin 18 |
| ── | ── | ── | 150 | Bank 0-1, Pin 17 |
| ── | ── | ── | 123 | Bank 2-3, Pin 17 |
| ── | ── | ── | 18 | Bank 4-5, Pin 17 |
| ── | ── | ── | 79 | Bank 6-7 Pin 17 |
| A+ | ch0 | ch0 | 133 | Bank 0, Pin 1 |
| A- | ch0 | ch0 | 142 | Bank 1, Pin 1 |
| B+ | ch0 | ch0 | 1 | Bank 4, Pin 1 |
| B- | ch0 | ch0 | 10 | Bank 5, Pin 1 |
| A+ | ch1 | ch1 | 135 | Bank 0, Pin 2 |
| A- | ch1 | ch1 | 144 | Bank 1, Pin 2 |
| B+ | ch1 | ch1 | 3 | Bank 4, Pin 2 |
| B- | ch1 | ch1 | 12 | Bank 5, Pin 2 |
| A+ | ch2 | ch2 | 137 | Bank 0, Pin 3 |
| A- | ch2 | ch2 | 146 | Bank 1, Pin 3 |
| B+ | ch2 | ch2 | 5 | Bank 4, Pin 3 |
| B- | ch2 | ch2 | 14 | Bank 5, Pin 3 |
| A+ | ch3 | ch3 | 139 | Bank 0, Pin 4 |
| A- | ch3 | ch3 | 148 | Bank 1, Pin 4 |
| B+ | ch3 | ch3 | 7 | Bank 4, Pin 4 |
| B- | ch3 | ch3 | 16 | Bank 5, Pin 4 |
| A+ | ch4 | ch4 | 141 | Bank 0, Pin 5 |
| A- | ch4 | ch4 | 150 | Bank 1, Pin 5 |
| B+ | ch4 | ch4 | 9 | Bank 4, Pin 5 |
| B- | ch4 | ch4 | 18 | Bank 5, Pin 5 |
| A+ | ch5 | ch5 | 143 | Bank 0, Pin 6 |
| A- | ch5 | ch5 | 152 | Bank 1, Pin 6 |
| B+ | ch5 | ch5 | 11 | Bank 4, Pin 6 |
| B- | ch5 | ch5 | 20 | Bank 5, Pin 6 |
| A+ | ch6 | ch6 | 145 | Bank 0, Pin 7 |
| A- | ch6 | ch6 | 154 | Bank 1, Pin 7 |
| B+ | ch6 | ch6 | 13 | Bank 4, Pin 7 |
| B- | ch6 | ch6 | 22 | Bank 5, Pin 7 |
| A+ | ch7 | ch7 | 147 | Bank 0, Pin 8 |
| A- | ch7 | ch7 | 156 | Bank 1, Pin 8 |
| B+ | ch7 | ch7 | 15 | Bank 4, Pin 8 |
| B- | ch7 | ch7 | 24 | Bank 5, Pin 8 |
| A+ | ch8 | ch8 | 149 | Bank 0, Pin 9 |
| A- | ch8 | ch8 | 158 | Bank 1, Pin 9 |
| B+ | ch8 | ch8 | 17 | Bank 4, Pin 9 |
| B- | ch8 | ch8 | 26 | Bank 5, Pin 9 |
| A+ | ch9 | ch9 | 151 | Bank 0, Pin 10 |
| A- | ch9 | ch9 | 160 | Bank 1, Pin 10 |
| B+ | ch9 | ch9 | 19 | Bank 4, Pin 10 |
| B- | ch9 | ch9 | 28 | Bank 5, Pin 10 |
| A+ | ch10 | ch10 | 153 | Bank 0, Pin 11 |
| A- | ch10 | ch10 | 162 | Bank 1, Pin 11 |
| B+ | ch10 | ch10 | 21 | Bank 4, Pin 11 |
| B- | ch10 | ch10 | 30 | Bank 5, Pin 11 |
| A+ | ch11 | ch11 | 155 | Bank 0, Pin 12 |
| A- | ch11 | ch11 | 164 | Bank 1, Pin 12 |
| B+ | ch11 | ch11 | 23 | Bank 4, Pin 12 |
| B- | ch11 | ch11 | 32 | Bank 5, Pin 12 |
| A+ | ch12 | ch12 | 157 | Bank 0, Pin 13 |
| A- | ch12 | ch12 | 166 | Bank 1, Pin 13 |
| B+ | ch12 | ch12 | 25 | Bank 4, Pin 13 |
| B- | ch12 | ch12 | 34 | Bank 5, Pin 13 |
| A+ | ch13 | ch13 | 159 | Bank 0, Pin 14 |
| A- | ch13 | ch13 | 168 | Bank 1, Pin 14 |
| B+ | ch13 | ch13 | 27 | Bank 4, Pin 14 |
| B- | ch13 | ch13 | 36 | Bank 5, Pin 14 |
| A+ | ch14 | ch14 | 161 | Bank 0, Pin 15 |
| A- | ch14 | ch14 | 170 | Bank 1, Pin 15 |
| B+ | ch14 | ch14 | 29 | Bank 4, Pin 15 |
| B- | ch14 | ch14 | 38 | Bank 5, Pin 15 |
| A+ | ch15 | ch15 | 163 | Bank 0, Pin 16 |
| A- | ch15 | ch15 | 172 | Bank 1, Pin 16 |
| B+ | ch15 | ch15 | 31 | Bank 4, Pin 16 |
| B- | ch15 | ch15 | 40 | Bank 5, Pin 16 |
| A+ | ch16 | ch16 | 165 | Bank 2, Pin 1 |
| A- | ch16 | ch16 | 174 | Bank 3, Pin 1 |
| B+ | ch16 | ch16 | 33 | Bank 6, Pin 1 |
| B- | ch16 | ch16 | 42 | Bank 7, Pin 1 |
| A+ | ch17 | ch17 | 167 | Bank 2, Pin 2 |
| A- | ch17 | ch17 | 176 | Bank 3, Pin 2 |
| B+ | ch17 | ch17 | 35 | Bank 6, Pin 2 |
| B- | ch17 | ch17 | 44 | Bank 7, Pin 2 |
| A+ | ch18 | ch18 | 169 | Bank 2, Pin 3 |
| A- | ch18 | ch18 | 178 | Bank 3, Pin 3 |
| B+ | ch18 | ch18 | 37 | Bank 6, Pin 3 |
| B- | ch18 | ch18 | 46 | Bank 7, Pin 3 |
| A+ | ch19 | ch19 | 171 | Bank 2, Pin 4 |
| A- | ch19 | ch19 | 180 | Bank 3, Pin 4 |
| B+ | ch19 | ch19 | 39 | Bank 6, Pin 4 |
| B- | ch19 | ch19 | 48 | Bank 7, Pin 4 |
| A+ | ch20 | ch20 | 173 | Bank 2, Pin 5 |
| A- | ch20 | ch20 | 182 | Bank 3, Pin 5 |
| B+ | ch20 | ch20 | 41 | Bank 6, Pin 5 |
| B- | ch20 | ch20 | 50 | Bank 7, Pin 5 |
| A+ | ch21 | ch21 | 175 | Bank 2, Pin 6 |
| A- | ch21 | ch21 | 184 | Bank 3, Pin 6 |
| B+ | ch21 | ch21 | 43 | Bank 6, Pin 6 |
| B- | ch21 | ch21 | 52 | Bank 7, Pin 6 |
| A+ | ch22 | ch22 | 177 | Bank 2, Pin 7 |
| A- | ch22 | ch22 | 186 | Bank 3, Pin 7 |
| B+ | ch22 | ch22 | 45 | Bank 6, Pin 7 |
| B- | ch22 | ch22 | 54 | Bank 7, Pin 7 |
| A+ | ch23 | ch23 | 179 | Bank 2, Pin 8 |
| A- | ch23 | ch23 | 188 | Bank 3, Pin 8 |
| B+ | ch23 | ch23 | 47 | Bank 6, Pin 8 |
| B- | ch23 | ch23 | 56 | Bank 7, Pin 8 |
| A+ | ch24 | ch24 | 181 | Bank 2, Pin 9 |
| A- | ch24 | ch24 | 190 | Bank 3, Pin 9 |
| B+ | ch24 | ch24 | 49 | Bank 6, Pin 9 |
| B- | ch24 | ch24 | 58 | Bank 7, Pin 9 |
| A+ | ch25 | ch25 | 183 | Bank 2, Pin 10 |
| A- | ch25 | ch25 | 192 | Bank 3, Pin 10 |
| B+ | ch25 | ch25 | 51 | Bank 6, Pin 10 |
| B- | ch25 | ch25 | 60 | Bank 7, Pin 10 |
| A+ | ch26 | ch26 | 185 | Bank 2, Pin 11 |
| A- | ch26 | ch26 | 194 | Bank 3, Pin 11 |
| B+ | ch26 | ch26 | 53 | Bank 6, Pin 11 |
| B- | ch26 | ch26 | 62 | Bank 7, Pin 11 |
| A+ | ch27 | ch27 | 187 | Bank 2, Pin 12 |
| A- | ch27 | ch27 | 196 | Bank 3, Pin 12 |
| B+ | ch27 | ch27 | 55 | Bank 6, Pin 12 |
| B- | ch27 | ch27 | 64 | Bank 7, Pin 12 |
| A+ | ch28 | ch28 | 189 | Bank 2, Pin 13 |
| A- | ch28 | ch28 | 198 | Bank 3, Pin 13 |
| B+ | ch28 | ch28 | 57 | Bank 6, Pin 13 |
| B- | ch28 | ch28 | 66 | Bank 7, Pin 13 |
| A+ | ch29 | ch29 | 191 | Bank 2, Pin 14 |
| A- | ch29 | ch29 | 200 | Bank 3, Pin 14 |
| B+ | ch29 | ch29 | 59 | Bank 6, Pin 14 |
| B- | ch29 | ch29 | 68 | Bank 7, Pin 14 |
| A+ | ch30 | ch30 | 193 | Bank 2, Pin 15 |
| A- | ch30 | ch30 | 202 | Bank 3, Pin 15 |
| B+ | ch30 | ch30 | 61 | Bank 6, Pin 15 |
| B- | ch30 | ch30 | 70 | Bank 7, Pin 15 |
| A+ | ch31 | ch31 | 195 | Bank 2, Pin 16 |
| A- | ch31 | ch31 | 204 | Bank 3, Pin 16 |
| B+ | ch31 | ch31 | 63 | Bank 6, Pin 16 |
| B- | ch31 | ch31 | 72 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530 Connector Pin Number | Signal Name |
| --- | --- |
| 36, 80, 37, 81, 38, 82, 39, 83, 40, 84, 41, 85, 168, 124, 169, 125, 170, 126, 171, 127, 172, 128, 173, 129 | NO CONNECT |
| 42, 86, 174, 130 | GND |
| 43 | TRIGIN |
| 87 | TRIGOUT |
| 44, 88, 175, 131, 176, 132 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-relay-replacement.html language=enus -->
## TOPIC 00177: NI PXI-2530 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2530 uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Meder MS05-1A87-75DHR Coto 9097-0006 Relay Kit Part Number National Instruments (10 matrix relays) 781450-10 Complete the following steps to disassemble your swit

### NI PXI-2530 Relay Replacement

The NI PXI-2530 uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Meder | MS05-1A87-75DHR |
| Coto | 9097-0006 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 matrix relays) | 781450-10 |

Note

#### Disassemble the Switch Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your switch module from electrostatic discharge.
2. Remove the four screws that secure the top and bottom daughterboards to the
 switch assembly.
3. Remove the insulator and the plastic spacers that separate the daughterboards. 
 1
 Screws2
 Insulator3
 Plastic Spacers
4. To access the daughterboards, disconnect the PCB interconnect cable by lifting
 the PCB cable latch on the J1 connector. 1
 PCB Interconnect Cable2
 PCB Cable Latch3
 J1 Connector
5. Carefully disconnect connectors J7 and J1 on the bottom daughterboard from
 connectors J8 and J1, respectively, on the top daughterboard. 1
 J7 Connector2
 J1 Connector3
 Bottom Daughterboard4
 J8 Connector5
 J1 Connector6
 Top Daughterboard
6. Refer to the following figures to locate the relay you want to replace.
 Table 6.Top Daughterboard[IMAGE alt='image' src='GUID-8B6C207D-EB5F-455A-B2D3-5E89054A0F25-a5.gif'] 
 Table 7.Bottom Daughterboard[IMAGE alt='image' src='GUID-C8C3AE26-F811-49E5-A0E5-A1E6634C9FA4-a5.gif']
7. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part.

#### Reassemble the Switch Module

Complete the Disassemble the Switch Module steps in reverse order to reassemble your
 switch module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530-signal-connections.html language=enus -->
## TOPIC 00178: NI PXI-2530 Signal Connections

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530-signal-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530-signal-connections.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains the pinout and signal connection information for the following types of topologies of the NI PXI-2530: 1-Wire Multiplexer Topologies 2-Wire Multiplexer Topologies 4-Wire Multiplexer Topologies 1-Wire 4x32 Matrix Topology 1-Wire 8x16 Matrix Topology 2-Wire 4x16 Matrix Topology Inde

### NI PXI-2530 Signal Connections

This book contains the pinout and signal connection information for the following types
 of topologies of the NI PXI-2530:

- 1-Wire Multiplexer Topologies
- 2-Wire Multiplexer Topologies
- 4-Wire Multiplexer Topologies
- 1-Wire 4x32 Matrix Topology
- 1-Wire 8x16 Matrix Topology
- 2-Wire 4x16 Matrix Topology
- Independent Topology

Parent topic:

NI PXI-2530/2530B

Related concepts:

- NI PXI-2530 1-Wire Multiplexer and Independent Topologies
- NI PXI-2530 2-Wire Multiplexer Topologies
- NI PXI-2530 4-Wire Multiplexer Topologies
- NI PXI-2530 1-Wire 4x32 Matrix Topology
- NI PXI-2530 1-Wire 8x16 Matrix Topology
- NI PXI-2530 2-Wire 4x16 Matrix Topology

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-1-wire-4x32-matrix-topology.html language=enus -->
## TOPIC 00179: NI PXI-2530B 1-Wire 4x32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-1-wire-4x32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-1-wire-4x32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 1-wire 4x32 matrix topology. Software Name NI PXI-2530B Connector Pin Number NI TB-2631B Terminal Name r0 51 ROW 0 r1 5 ROW 2 r2 110 ROW 4 r3 156 ROW 6 c0 120, 94, 67, 41 COLUMN 0 c1 121, 149, 15, 40 COLUMN 1 c2 119, 91, 12

### NI PXI-2530B 1-Wire 4x32 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530B in the 1-wire 4x32
 matrix topology.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Software Name | NI PXI-2530B Connector Pin Number | NI TB-2631B Terminal Name |
| --- | --- | --- |
| r0 | 51 | ROW 0 |
| r1 | 5 | ROW 2 |
| r2 | 110 | ROW 4 |
| r3 | 156 | ROW 6 |
| c0 | 120, 94, 67, 41 | COLUMN 0 |
| c1 | 121, 149, 15, 40 | COLUMN 1 |
| c2 | 119, 91, 12, 42 | COLUMN 2 |
| c3 | 122, 150, 11, 39 | COLUMN 3 |
| c4 | 118, 146, 70, 43 | COLUMN 4 |
| c5 | 123, 100, 61, 38 | COLUMN 5 |
| c6 | 117, 141, 20, 44 | COLUMN 6 |
| c7 | 124, 99, 62, 37 | COLUMN 7 |
| c8 | 116, 142, 19, 45 | COLUMN 8 |
| c9 | 125, 98, 63, 36 | COLUMN 9 |
| c10 | 115, 143, 18, 46 | COLUMN 10 |
| c11 | 126, 97, 64, 35 | COLUMN 11 |
| c12 | 114, 144, 17, 47 | COLUMN 12 |
| c13 | 127, 96, 65, 34 | COLUMN 13 |
| c14 | 113, 145, 16, 48 | COLUMN 14 |
| c15 | 128, 95, 66, 33 | COLUMN 15 |
| c16 | 111, 147, 14, 50 | COLUMN 16 |
| c17 | 130, 93, 68, 31 | COLUMN 17 |
| c18 | 112, 148, 13, 49 | COLUMN 18 |
| c19 | 129, 92, 69, 32 | COLUMN 19 |
| c20 | 109, 85, 1, 52 | COLUMN 20 |
| c21 | 132, 81, 4, 29 | COLUMN 21 |
| c22 | 108, 157, 3, 53 | COLUMN 22 |
| c23 | 133, 90, 71, 28 | COLUMN 23 |
| c24 | 107, 151, 10, 54 | COLUMN 24 |
| c25 | 134, 89, 72, 27 | COLUMN 25 |
| c26 | 106, 152, 9, 55 | COLUMN 26 |
| c27 | 135, 88, 73, 26 | COLUMN 27 |
| c28 | 105, 153, 8, 56 | COLUMN 28 |
| c29 | 136, 87, 74, 25 | COLUMN 29 |
| c30 | 104, 154, 7, 57 | COLUMN 30 |
| c31 | 137, 86, 75, 24 | COLUMN 31 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-1-wire-8x16-matrix-topology.html language=enus -->
## TOPIC 00180: NI PXI-2530B 1-Wire 8x16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-1-wire-8x16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-1-wire-8x16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 1-wire 8x16 matrix topology. Software Name NI PXI-2530B Connector Pin Number NI TB-2632B Terminal Name r0 51 ROW 0 r1 30 ROW 1 r2 5 ROW 2 r3 76 ROW 3 r4 110 ROW 4 r5 131 ROW 5 r6 156 ROW 6 r7 84 ROW 7 c0 120, 94, 67, 41, 11

### NI PXI-2530B 1-Wire 8x16 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530B in the 1-wire 8x16
 matrix topology.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Software Name | NI PXI-2530B Connector Pin Number | NI TB-2632B Terminal Name |
| --- | --- | --- |
| r0 | 51 | ROW 0 |
| r1 | 30 | ROW 1 |
| r2 | 5 | ROW 2 |
| r3 | 76 | ROW 3 |
| r4 | 110 | ROW 4 |
| r5 | 131 | ROW 5 |
| r6 | 156 | ROW 6 |
| r7 | 84 | ROW 7 |
| c0 | 120, 94, 67, 41, 111, 147, 14, 50 | COLUMN 0 |
| c1 | 121, 149, 15, 40, 130, 93, 68, 31 | COLUMN 1 |
| c2 | 119, 91, 12, 42, 112, 148, 13, 49 | COLUMN 2 |
| c3 | 122, 150, 11, 39, 129, 92, 69, 32 | COLUMN 3 |
| c4 | 118, 146, 70, 43, 109, 85, 1, 52 | COLUMN 4 |
| c5 | 123, 100, 61, 38, 132, 81, 4, 29 | COLUMN 5 |
| c6 | 117, 141, 20, 44, 108, 157, 3, 53 | COLUMN 6 |
| c7 | 124, 99, 62, 37, 133, 90, 71, 28 | COLUMN 7 |
| c8 | 116, 142, 19, 45, 107, 151, 10, 54 | COLUMN 8 |
| c9 | 125, 98, 63, 36, 134, 89, 72, 27 | COLUMN 9 |
| c10 | 115, 143, 18, 46, 106, 152, 9, 55 | COLUMN 10 |
| c11 | 126, 97, 64, 35, 135, 88, 73, 26 | COLUMN 11 |
| c12 | 114, 144, 17, 47, 105, 153, 8, 56 | COLUMN 12 |
| c13 | 127, 96, 65, 34, 136, 87, 74, 25 | COLUMN 13 |
| c14 | 113, 145, 16, 48, 104, 154, 7, 57 | COLUMN 14 |
| c15 | 128, 95, 66, 33, 137, 86, 75, 24 | COLUMN 15 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-1-wire-multiplexer-and-independe.html language=enus -->
## TOPIC 00181: NI PXI-2530B 1-Wire Multiplexer and Independent Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-1-wire-multiplexer-and-independe.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-1-wire-multiplexer-and-independe.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 1-wire multiplexer and independent topologies. Single128x1 Dual64x1 Quad32x1 Octal16x1 Independent NI PXI-2530B Connector Pin Number NI TB-2630B Terminal Name com0 com0 com0 com0 com0 51 Bank 0, Pin 18 ── ── ── com1 com1 30

### NI PXI-2530B 1-Wire Multiplexer and Independent Topologies

The following figure and table identify the pins for the NI PXI-2530B in the 1-wire
 multiplexer and independent topologies.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Single128x1 | Dual64x1 | Quad32x1 | Octal16x1 | Independent | NI PXI-2530B Connector Pin Number | NI TB-2630B Terminal Name |
| --- | --- | --- | --- | --- | --- | --- |
| com0 | com0 | com0 | com0 | com0 | 51 | Bank 0, Pin 18 |
| ── | ── | ── | com1 | com1 | 30 | Bank 1, Pin 18 |
| ── | ── | com2 | com2 | com2 | 5 | Bank 2, Pin 18 |
| ── | ── | ── | com3 | com3 | 76 | Bank 3, Pin 18 |
| ── | com4 | com4 | com4 | com4 | 110 | Bank 4, Pin 18 |
| ── | ── | ── | com5 | com5 | 131 | Bank 5, Pin 18 |
| ── | ── | com6 | com6 | com6 | 156 | Bank 6, Pin 18 |
| ── | ── | ── | com7 | com7 | 84 | Bank 7, Pin 18 |
| ── | ── | ── | ── | 1wref0 | 58 | Bank 0-1, Pin 17 |
| ── | ── | ── | ── | 1wref1 | 6 | Bank 2-3, Pin 17 |
| ── | ── | ── | ── | 1wref2 | 103 | Bank 4-5, Pin 17 |
| ── | ── | ── | ── | 1wref3 | 155 | Bank 6-7, Pin 17 |
| ch0 |  |  |  |  | 41 | Bank 0, Pin 1 |
| ch1 |  |  |  |  | 40 | Bank 0, Pin 2 |
| ch2 |  |  |  |  | 42 | Bank 0, Pin 3 |
| ch3 |  |  |  |  | 39 | Bank 0, Pin 4 |
| ch4 |  |  |  |  | 43 | Bank 0, Pin 5 |
| ch5 |  |  |  |  | 38 | Bank 0, Pin 6 |
| ch6 |  |  |  |  | 44 | Bank 0, Pin 7 |
| ch7 |  |  |  |  | 37 | Bank 0, Pin 8 |
| ch8 |  |  |  |  | 45 | Bank 0, Pin 9 |
| ch9 |  |  |  |  | 36 | Bank 0, Pin 10 |
| ch10 |  |  |  |  | 46 | Bank 0, Pin 11 |
| ch11 |  |  |  |  | 35 | Bank 0, Pin 12 |
| ch12 |  |  |  |  | 47 | Bank 0, Pin 13 |
| ch13 |  |  |  |  | 34 | Bank 0, Pin 14 |
| ch14 |  |  |  |  | 48 | Bank 0, Pin 15 |
| ch15 |  |  |  |  | 33 | Bank 0, Pin 16 |
| ch16 |  |  |  |  | 50 | Bank 1, Pin 1 |
| ch17 |  |  |  |  | 31 | Bank 1, Pin 2 |
| ch18 |  |  |  |  | 49 | Bank 1, Pin 3 |
| ch19 |  |  |  |  | 32 | Bank 1, Pin 4 |
| ch20 |  |  |  |  | 52 | Bank 1, Pin 5 |
| ch21 |  |  |  |  | 29 | Bank 1, Pin 6 |
| ch22 |  |  |  |  | 53 | Bank 1, Pin 7 |
| ch23 |  |  |  |  | 28 | Bank 1, Pin 8 |
| ch24 |  |  |  |  | 54 | Bank 1, Pin 9 |
| ch25 |  |  |  |  | 27 | Bank 1, Pin 10 |
| ch26 |  |  |  |  | 55 | Bank 1, Pin 11 |
| ch27 |  |  |  |  | 26 | Bank 1, Pin 12 |
| ch28 |  |  |  |  | 56 | Bank 1, Pin 13 |
| ch29 |  |  |  |  | 25 | Bank 1, Pin 14 |
| ch30 |  |  |  |  | 57 | Bank 1, Pin 15 |
| ch31 |  |  |  |  | 24 | Bank 1, Pin 16 |
| ch32 |  |  |  |  | 67 | Bank 2, Pin 1 |
| ch33 |  |  |  |  | 15 | Bank 2, Pin 2 |
| ch34 |  |  |  |  | 12 | Bank 2, Pin 3 |
| ch35 |  |  |  |  | 11 | Bank 2, Pin 4 |
| ch36 |  |  |  |  | 70 | Bank 2, Pin 5 |
| ch37 |  |  |  |  | 61 | Bank 2, Pin 6 |
| ch38 |  |  |  |  | 20 | Bank 2, Pin 7 |
| ch39 |  |  |  |  | 62 | Bank 2, Pin 8 |
| ch40 |  |  |  |  | 19 | Bank 2, Pin 9 |
| ch41 |  |  |  |  | 63 | Bank 2, Pin 10 |
| ch42 |  |  |  |  | 18 | Bank 2, Pin 11 |
| ch43 |  |  |  |  | 64 | Bank 2, Pin 12 |
| ch44 |  |  |  |  | 17 | Bank 2, Pin 13 |
| ch45 |  |  |  |  | 65 | Bank 2, Pin 14 |
| ch46 |  |  |  |  | 16 | Bank 2, Pin 15 |
| ch47 |  |  |  |  | 66 | Bank 2, Pin 16 |
| ch48 |  |  |  |  | 14 | Bank 3, Pin 1 |
| ch49 |  |  |  |  | 68 | Bank 3, Pin 2 |
| ch50 |  |  |  |  | 13 | Bank 3, Pin 3 |
| ch51 |  |  |  |  | 69 | Bank 3, Pin 4 |
| ch52 |  |  |  |  | 1 | Bank 3, Pin 5 |
| ch53 |  |  |  |  | 4 | Bank 3, Pin 6 |
| ch54 |  |  |  |  | 3 | Bank 3, Pin 7 |
| ch55 |  |  |  |  | 71 | Bank 3, Pin 8 |
| ch56 |  |  |  |  | 10 | Bank 3, Pin 9 |
| ch57 |  |  |  |  | 72 | Bank 3, Pin 10 |
| ch58 |  |  |  |  | 9 | Bank 3, Pin 11 |
| ch59 |  |  |  |  | 73 | Bank 3, Pin 12 |
| ch60 |  |  |  |  | 8 | Bank 3, Pin 13 |
| ch61 |  |  |  |  | 74 | Bank 3, Pin 14 |
| ch62 |  |  |  |  | 7 | Bank 3, Pin 15 |
| ch63 |  |  |  |  | 75 | Bank 3, Pin 16 |
| ch64 |  |  |  |  | 120 | Bank 4, Pin 1 |
| ch65 |  |  |  |  | 121 | Bank 4, Pin 2 |
| ch66 |  |  |  |  | 119 | Bank 4, Pin 3 |
| ch67 |  |  |  |  | 122 | Bank 4, Pin 4 |
| ch68 |  |  |  |  | 118 | Bank 4, Pin 5 |
| ch69 |  |  |  |  | 123 | Bank 4, Pin 6 |
| ch70 |  |  |  |  | 117 | Bank 4, Pin 7 |
| ch71 |  |  |  |  | 124 | Bank 4, Pin 8 |
| ch72 |  |  |  |  | 116 | Bank 4, Pin 9 |
| ch73 |  |  |  |  | 125 | Bank 4, Pin 10 |
| ch74 |  |  |  |  | 115 | Bank 4, Pin 11 |
| ch75 |  |  |  |  | 126 | Bank 4, Pin 12 |
| ch76 |  |  |  |  | 114 | Bank 4, Pin 13 |
| ch77 |  |  |  |  | 127 | Bank 4, Pin 14 |
| ch78 |  |  |  |  | 113 | Bank 4, Pin 15 |
| ch79 |  |  |  |  | 128 | Bank 4, Pin 16 |
| ch80 |  |  |  |  | 111 | Bank 5, Pin 1 |
| ch81 |  |  |  |  | 130 | Bank 5, Pin 2 |
| ch82 |  |  |  |  | 112 | Bank 5, Pin 3 |
| ch83 |  |  |  |  | 129 | Bank 5, Pin 4 |
| ch84 |  |  |  |  | 109 | Bank 5, Pin 5 |
| ch85 |  |  |  |  | 132 | Bank 5, Pin 6 |
| ch86 |  |  |  |  | 108 | Bank 5, Pin 7 |
| ch87 |  |  |  |  | 133 | Bank 5, Pin 8 |
| ch88 |  |  |  |  | 107 | Bank 5, Pin 9 |
| ch89 |  |  |  |  | 134 | Bank 5, Pin 10 |
| ch90 |  |  |  |  | 106 | Bank 5, Pin 11 |
| ch91 |  |  |  |  | 135 | Bank 5, Pin 12 |
| ch92 |  |  |  |  | 105 | Bank 5, Pin 13 |
| ch93 |  |  |  |  | 136 | Bank 5, Pin 14 |
| ch94 |  |  |  |  | 104 | Bank 5, Pin 15 |
| ch95 |  |  |  |  | 137 | Bank 5, Pin 16 |
| ch96 |  |  |  |  | 94 | Bank 6, Pin 1 |
| ch97 |  |  |  |  | 149 | Bank 6, Pin 2 |
| ch98 |  |  |  |  | 91 | Bank 6, Pin 3 |
| ch99 |  |  |  |  | 150 | Bank 6, Pin 4 |
| ch100 |  |  |  |  | 146 | Bank 6, Pin 5 |
| ch101 |  |  |  |  | 100 | Bank 6, Pin 6 |
| ch102 |  |  |  |  | 141 | Bank 6, Pin 7 |
| ch103 |  |  |  |  | 99 | Bank 6, Pin 8 |
| ch104 |  |  |  |  | 142 | Bank 6, Pin 9 |
| ch105 |  |  |  |  | 98 | Bank 6, Pin 10 |
| ch106 |  |  |  |  | 143 | Bank 6, Pin 11 |
| ch107 |  |  |  |  | 97 | Bank 6, Pin 12 |
| ch108 |  |  |  |  | 144 | Bank 6, Pin 13 |
| ch109 |  |  |  |  | 96 | Bank 6, Pin 14 |
| ch110 |  |  |  |  | 145 | Bank 6, Pin 15 |
| ch111 |  |  |  |  | 95 | Bank 6, Pin 16 |
| ch112 |  |  |  |  | 147 | Bank 7, Pin 1 |
| ch113 |  |  |  |  | 93 | Bank 7, Pin 2 |
| ch114 |  |  |  |  | 148 | Bank 7, Pin 3 |
| ch115 |  |  |  |  | 92 | Bank 7, Pin 4 |
| ch116 |  |  |  |  | 85 | Bank 7, Pin 5 |
| ch117 |  |  |  |  | 81 | Bank 7, Pin 6 |
| ch118 |  |  |  |  | 157 | Bank 7, Pin 7 |
| ch119 |  |  |  |  | 90 | Bank 7, Pin 8 |
| ch120 |  |  |  |  | 151 | Bank 7, Pin 9 |
| ch121 |  |  |  |  | 89 | Bank 7, Pin 10 |
| ch122 |  |  |  |  | 152 | Bank 7, Pin 11 |
| ch123 |  |  |  |  | 88 | Bank 7, Pin 12 |
| ch124 |  |  |  |  | 153 | Bank 7, Pin 13 |
| ch125 |  |  |  |  | 87 | Bank 7, Pin 14 |
| ch126 |  |  |  |  | 154 | Bank 7, Pin 15 |
| ch127 |  |  |  |  | 86 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-2-wire-4x16-matrix-topology.html language=enus -->
## TOPIC 00182: NI PXI-2530B 2-Wire 4x16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-2-wire-4x16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-2-wire-4x16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 2-wire 4x16 matrix topology. Software Name Polarity NI PXI-2530B Connector Pin Number NI TB-2631B Terminal Name r0 + 51 ROW 0 r0 - 30 ROW 1 r1 + 5 ROW 2 r1 - 76 ROW 3 r2 + 110 ROW 4 r2 - 131 ROW 5 r3 + 156 ROW 6 r3 - 84 ROW

### NI PXI-2530B 2-Wire 4x16 Matrix Topology

The following figure and table identify the pins for the NI PXI-2530B in the 2-wire 4x16
 matrix topology.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Software Name | Polarity | NI PXI-2530B Connector Pin Number | NI TB-2631B Terminal Name |
| --- | --- | --- | --- |
| r0 | + | 51 | ROW 0 |
| r0 | - | 30 | ROW 1 |
| r1 | + | 5 | ROW 2 |
| r1 | - | 76 | ROW 3 |
| r2 | + | 110 | ROW 4 |
| r2 | - | 131 | ROW 5 |
| r3 | + | 156 | ROW 6 |
| r3 | - | 84 | ROW 7 |
| c0 | + | 120, 94, 67, 41 | COLUMN 0 |
| c0 | - | 121, 149, 15, 40 | COLUMN 16 |
| c1 | + | 119, 91, 12, 42 | COLUMN 1 |
| c1 | - | 122, 150, 11, 39 | COLUMN 17 |
| c2 | + | 118, 146, 70, 43 | COLUMN 2 |
| c2 | - | 123, 100, 61, 38 | COLUMN 18 |
| c3 | + | 117, 141, 20, 44 | COLUMN 3 |
| c3 | - | 124, 99, 62, 37 | COLUMN 19 |
| c4 | + | 116, 142, 19, 45 | COLUMN 4 |
| c4 | - | 125, 98, 63, 36 | COLUMN 20 |
| c5 | + | 115, 143, 18, 46 | COLUMN 5 |
| c5 | - | 126, 97, 64, 35 | COLUMN 21 |
| c6 | + | 114, 144, 17, 47 | COLUMN 6 |
| c6 | - | 127, 96, 65, 34 | COLUMN 22 |
| c7 | + | 113, 145, 16, 48 | COLUMN 7 |
| c7 | - | 128, 95, 66, 33 | COLUMN 23 |
| c8 | + | 111, 147, 14, 50 | COLUMN 8 |
| c8 | - | 130, 93, 68, 31 | COLUMN 24 |
| c9 | + | 112, 148, 13, 49 | COLUMN 9 |
| c9 | - | 129, 92, 69, 32 | COLUMN 25 |
| c10 | + | 109, 85, 1, 52 | COLUMN 10 |
| c10 | - | 132, 81, 4, 29 | COLUMN 26 |
| c11 | + | 108, 157, 3, 53 | COLUMN 11 |
| c11 | - | 133, 90, 71, 28 | COLUMN 27 |
| c12 | + | 107, 151, 10, 54 | COLUMN 12 |
| c12 | - | 134, 89, 72, 27 | COLUMN 28 |
| c13 | + | 106, 152, 9, 55 | COLUMN 13 |
| c13 | - | 135, 88, 73, 26 | COLUMN 29 |
| c14 | + | 105, 153, 8, 56 | COLUMN 14 |
| c14 | - | 136, 87, 74, 25 | COLUMN 30 |
| c15 | + | 104, 154, 7, 57 | COLUMN 15 |
| c15 | - | 137, 86, 75, 24 | COLUMN 31 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-2-wire-multiplexer-topologies.html language=enus -->
## TOPIC 00183: NI PXI-2530B 2-Wire Multiplexer Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-2-wire-multiplexer-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-2-wire-multiplexer-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 2-wire multiplexer topologies. Polarity Single 64x1 Dual 32x1 Quad 16x1 NI PXI-2530B Connector Pin Number NI TB-2630B Terminal Name + com0 com0 com0 51 Bank 0, Pin 18 - com0 com0 com0 30 Bank 1, Pin 18 + ── ── com1 5 Bank 2

### NI PXI-2530B 2-Wire Multiplexer Topologies

The following figure and table identify the pins for the NI PXI-2530B in the 2-wire
 multiplexer topologies.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Polarity | Single 64x1 | Dual 32x1 | Quad 16x1 | NI PXI-2530B Connector Pin Number | NI TB-2630B Terminal Name |
| --- | --- | --- | --- | --- | --- |
| + | com0 | com0 | com0 | 51 | Bank 0, Pin 18 |
| - | com0 | com0 | com0 | 30 | Bank 1, Pin 18 |
| + | ── | ── | com1 | 5 | Bank 2, Pin 18 |
| - | ── | ── | com1 | 76 | Bank 3, Pin 18 |
| + | ── | com1 | com2 | 110 | Bank 4, Pin 18 |
| - | ── | com1 | com2 | 131 | Bank 5, Pin 18 |
| + | ── | ── | com3 | 156 | Bank 6, Pin 18 |
| - | ── | ── | com3 | 84 | Bank 7, Pin 18 |
| + | ── | ── | ── | 58 | Bank 0-1, Pin 17 |
| - | ── | ── | ── | 6 | Bank 2-3, Pin 17 |
| + | ── | ── | ── | 103 | Bank 4-5, Pin 17 |
| - | ── | ── | ── | 155 | Bank 6-7, Pin 17 |
| + | ch0 | ch0 | ch0 | 41 | Bank 0, Pin 1 |
| - | ch0 | ch0 | ch0 | 50 | Bank 1, Pin 1 |
| + | ch1 | ch1 | ch1 | 40 | Bank 0, Pin 2 |
| - | ch1 | ch1 | ch1 | 31 | Bank 1, Pin 2 |
| + | ch2 | ch2 | ch2 | 42 | Bank 0, Pin 3 |
| - | ch2 | ch2 | ch2 | 49 | Bank 1, Pin 3 |
| + | ch3 | ch3 | ch3 | 39 | Bank 0, Pin 4 |
| - | ch3 | ch3 | ch3 | 32 | Bank 1, Pin 4 |
| + | ch4 | ch4 | ch4 | 43 | Bank 0, Pin 5 |
| - | ch4 | ch4 | ch4 | 52 | Bank 1, Pin 5 |
| + | ch5 | ch5 | ch5 | 38 | Bank 0, Pin 6 |
| - | ch5 | ch5 | ch5 | 29 | Bank 1, Pin 6 |
| + | ch6 | ch6 | ch6 | 44 | Bank 0, Pin 7 |
| - | ch6 | ch6 | ch6 | 53 | Bank 1, Pin 7 |
| + | ch7 | ch7 | ch7 | 37 | Bank 0, Pin 8 |
| - | ch7 | ch7 | ch7 | 28 | Bank 1, Pin 8 |
| + | ch8 | ch8 | ch8 | 45 | Bank 0, Pin 9 |
| - | ch8 | ch8 | ch8 | 54 | Bank 1, Pin 9 |
| + | ch9 | ch9 | ch9 | 36 | Bank 0, Pin 10 |
| - | ch9 | ch9 | ch9 | 27 | Bank 1, Pin 10 |
| + | ch10 | ch10 | ch10 | 46 | Bank 0, Pin 11 |
| - | ch10 | ch10 | ch10 | 55 | Bank 1, Pin 11 |
| + | ch11 | ch11 | ch11 | 35 | Bank 0, Pin 12 |
| - | ch11 | ch11 | ch11 | 26 | Bank 1, Pin 12 |
| + | ch12 | ch12 | ch12 | 47 | Bank 0, Pin 13 |
| - | ch12 | ch12 | ch12 | 56 | Bank 1, Pin 13 |
| + | ch13 | ch13 | ch13 | 34 | Bank 0, Pin 14 |
| - | ch13 | ch13 | ch13 | 25 | Bank 1, Pin 14 |
| + | ch14 | ch14 | ch14 | 48 | Bank 0, Pin 15 |
| - | ch14 | ch14 | ch14 | 57 | Bank 1, Pin 15 |
| + | ch15 | ch15 | ch15 | 33 | Bank 0, Pin 16 |
| - | ch15 | ch15 | ch15 | 24 | Bank 1, Pin 16 |
| + | ch16 | ch16 | ch16 | 67 | Bank 2, Pin 1 |
| - | ch16 | ch16 | ch16 | 14 | Bank 3, Pin 1 |
| + | ch17 | ch17 | ch17 | 15 | Bank 2, Pin 2 |
| - | ch17 | ch17 | ch17 | 68 | Bank 3, Pin 2 |
| + | ch18 | ch18 | ch18 | 12 | Bank 2, Pin 3 |
| - | ch18 | ch18 | ch18 | 13 | Bank 3, Pin 3 |
| + | ch19 | ch19 | ch19 | 11 | Bank 2, Pin 4 |
| - | ch19 | ch19 | ch19 | 69 | Bank 3, Pin 4 |
| + | ch20 | ch20 | ch20 | 70 | Bank 2, Pin 5 |
| - | ch20 | ch20 | ch20 | 1 | Bank 3, Pin 5 |
| + | ch21 | ch21 | ch21 | 61 | Bank 2, Pin 6 |
| - | ch21 | ch21 | ch21 | 4 | Bank 3, Pin 6 |
| + | ch22 | ch22 | ch22 | 20 | Bank 2, Pin 7 |
| - | ch22 | ch22 | ch22 | 3 | Bank 3, Pin 7 |
| + | ch23 | ch23 | ch23 | 62 | Bank 2, Pin 8 |
| - | ch23 | ch23 | ch23 | 71 | Bank 3, Pin 8 |
| + | ch24 | ch24 | ch24 | 19 | Bank 2, Pin 9 |
| - | ch24 | ch24 | ch24 | 10 | Bank 3, Pin 9 |
| + | ch25 | ch25 | ch25 | 63 | Bank 2, Pin 10 |
| - | ch25 | ch25 | ch25 | 72 | Bank 3, Pin 10 |
| + | ch26 | ch26 | ch26 | 18 | Bank 2, Pin 11 |
| - | ch26 | ch26 | ch26 | 9 | Bank 3, Pin 11 |
| + | ch27 | ch27 | ch27 | 64 | Bank 2, Pin 12 |
| - | ch27 | ch27 | ch27 | 73 | Bank 3, Pin 12 |
| + | ch28 | ch28 | ch28 | 17 | Bank 2, Pin 13 |
| - | ch28 | ch28 | ch28 | 8 | Bank 3, Pin 13 |
| + | ch29 | ch29 | ch29 | 65 | Bank 2, Pin 14 |
| - | ch29 | ch29 | ch29 | 74 | Bank 3, Pin 14 |
| + | ch30 | ch30 | ch30 | 16 | Bank 2, Pin 15 |
| - | ch30 | ch30 | ch30 | 7 | Bank 3, Pin 15 |
| + | ch31 | ch31 | ch31 | 66 | Bank 2, Pin 16 |
| - | ch31 | ch31 | ch31 | 75 | Bank 3, Pin 16 |
| + | ch32 | ch32 | ch32 | 120 | Bank 4, Pin 1 |
| - | ch32 | ch32 | ch32 | 111 | Bank 5, Pin 1 |
| + | ch33 | ch33 | ch33 | 121 | Bank 4, Pin 2 |
| - | ch33 | ch33 | ch33 | 130 | Bank 5, Pin 2 |
| + | ch34 | ch34 | ch34 | 119 | Bank 4, Pin 3 |
| - | ch34 | ch34 | ch34 | 112 | Bank 5, Pin 3 |
| + | ch35 | ch35 | ch35 | 122 | Bank 4, Pin 4 |
| - | ch35 | ch35 | ch35 | 129 | Bank 5, Pin 4 |
| + | ch36 | ch36 | ch36 | 118 | Bank 4, Pin 5 |
| - | ch36 | ch36 | ch36 | 109 | Bank 5, Pin 5 |
| + | ch37 | ch37 | ch37 | 123 | Bank 4, Pin 6 |
| - | ch37 | ch37 | ch37 | 132 | Bank 5, Pin 6 |
| + | ch38 | ch38 | ch38 | 117 | Bank 4, Pin 7 |
| - | ch38 | ch38 | ch38 | 108 | Bank 5, Pin 7 |
| + | ch39 | ch39 | ch39 | 124 | Bank 4, Pin 8 |
| - | ch39 | ch39 | ch39 | 133 | Bank 5, Pin 8 |
| + | ch40 | ch40 | ch40 | 116 | Bank 4, Pin 9 |
| - | ch40 | ch40 | ch40 | 107 | Bank 5, Pin 9 |
| + | ch41 | ch41 | ch41 | 125 | Bank 4, Pin 10 |
| - | ch41 | ch41 | ch41 | 134 | Bank 5, Pin 10 |
| + | ch42 | ch42 | ch42 | 115 | Bank 4, Pin 11 |
| - | ch42 | ch42 | ch42 | 106 | Bank 5, Pin 11 |
| + | ch43 | ch43 | ch43 | 126 | Bank 4, Pin 12 |
| - | ch43 | ch43 | ch43 | 135 | Bank 5, Pin 12 |
| + | ch44 | ch44 | ch44 | 114 | Bank 4, Pin 13 |
| - | ch44 | ch44 | ch44 | 105 | Bank 5, Pin 13 |
| + | ch45 | ch45 | ch45 | 127 | Bank 4, Pin 14 |
| - | ch45 | ch45 | ch45 | 136 | Bank 5, Pin 14 |
| + | ch46 | ch46 | ch46 | 113 | Bank 4, Pin 15 |
| - | ch46 | ch46 | ch46 | 104 | Bank 5, Pin 15 |
| + | ch47 | ch47 | ch47 | 128 | Bank 4, Pin 16 |
| - | ch47 | ch47 | ch47 | 137 | Bank 5, Pin 16 |
| + | ch48 | ch48 | ch48 | 94 | Bank 6, Pin 1 |
| - | ch48 | ch48 | ch48 | 147 | Bank 7, Pin 1 |
| + | ch49 | ch49 | ch49 | 149 | Bank 6, Pin 2 |
| - | ch49 | ch49 | ch49 | 93 | Bank 7, Pin 2 |
| + | ch50 | ch50 | ch50 | 91 | Bank 6, Pin 3 |
| - | ch50 | ch50 | ch50 | 148 | Bank 7, Pin 3 |
| + | ch51 | ch51 | ch51 | 150 | Bank 6, Pin 4 |
| - | ch51 | ch51 | ch51 | 92 | Bank 7, Pin 4 |
| + | ch52 | ch52 | ch52 | 146 | Bank 6, Pin 5 |
| - | ch52 | ch52 | ch52 | 85 | Bank 7, Pin 5 |
| + | ch53 | ch53 | ch53 | 100 | Bank 6, Pin 6 |
| - | ch53 | ch53 | ch53 | 81 | Bank 7, Pin 6 |
| + | ch54 | ch54 | ch54 | 141 | Bank 6, Pin 7 |
| - | ch54 | ch54 | ch54 | 157 | Bank 7, Pin 7 |
| + | ch55 | ch55 | ch55 | 99 | Bank 6, Pin 8 |
| - | ch55 | ch55 | ch55 | 90 | Bank 7, Pin 8 |
| + | ch56 | ch56 | ch56 | 142 | Bank 6, Pin 9 |
| - | ch56 | ch56 | ch56 | 151 | Bank 7, Pin 9 |
| + | ch57 | ch57 | ch57 | 98 | Bank 6, Pin 10 |
| - | ch57 | ch57 | ch57 | 89 | Bank 7, Pin 10 |
| + | ch58 | ch58 | ch58 | 143 | Bank 6, Pin 11 |
| - | ch58 | ch58 | ch58 | 152 | Bank 7, Pin 11 |
| + | ch59 | ch59 | ch59 | 97 | Bank 6, Pin 12 |
| - | ch59 | ch59 | ch59 | 88 | Bank 7, Pin 12 |
| + | ch60 | ch60 | ch60 | 144 | Bank 6, Pin 13 |
| - | ch60 | ch60 | ch60 | 153 | Bank 7, Pin 13 |
| + | ch61 | ch61 | ch61 | 96 | Bank 6, Pin 14 |
| - | ch61 | ch61 | ch61 | 87 | Bank 7, Pin 14 |
| + | ch62 | ch62 | ch62 | 145 | Bank 6, Pin 15 |
| - | ch62 | ch62 | ch62 | 154 | Bank 7, Pin 15 |
| + | ch63 | ch63 | ch63 | 95 | Bank 6, Pin 16 |
| - | ch63 | ch63 | ch63 | 86 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-4-wire-multiplexer-topologies.html language=enus -->
## TOPIC 00184: NI PXI-2530B 4-Wire Multiplexer Topologies

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-4-wire-multiplexer-topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-4-wire-multiplexer-topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and table identify the pins for the NI PXI-2530B in the 4-wire multiplexer topologies. Single 32x1 Dual 16x1 Polarity NI PXI-2530B Connector Pin Number NI TB-2630B Terminal Name com0 com0 A+ 51 Bank 0, Pin 18 com0 com0 A- 30 Bank 1, Pin 18 com0 com0 B+ 110 Bank 4, Pin 18 com0 co

### NI PXI-2530B 4-Wire Multiplexer Topologies

The following figure and table identify the pins for the NI PXI-2530B in the 4-wire
 multiplexer topologies.

[IMAGE alt='image' src='GUID-A28CD13B-B8E5-4418-AC0C-A0DCFF8318B9-a5.gif']

| Single 32x1 | Dual 16x1 | Polarity | NI PXI-2530B Connector Pin Number | NI TB-2630B Terminal Name |
| --- | --- | --- | --- | --- |
| com0 | com0 | A+ | 51 | Bank 0, Pin 18 |
| com0 | com0 | A- | 30 | Bank 1, Pin 18 |
| com0 | com0 | B+ | 110 | Bank 4, Pin 18 |
| com0 | com0 | B- | 131 | Bank 5, Pin 18 |
| ── | com1 | A+ | 5 | Bank 2, Pin 18 |
| ── | com1 | A- | 76 | Bank 3, Pin 18 |
| ── | com1 | B+ | 156 | Bank 6, Pin 18 |
| ── | com1 | B- | 84 | Bank 7, Pin 18 |
| ── | ── | ── | 58 | Bank 0-1, Pin 17 |
| ── | ── | ── | 6 | Bank 2-3, Pin 17 |
| ── | ── | ── | 103 | Bank 4-5, Pin 17 |
| ── | ── | ── | 155 | Bank 6-7, Pin 17 |
| ch0 | ch0 | A+ | 41 | Bank 0, Pin 1 |
| ch0 | ch0 | A- | 50 | Bank 1, Pin 1 |
| ch0 | ch0 | B+ | 120 | Bank 4, Pin 1 |
| ch0 | ch0 | B- | 111 | Bank 5, Pin 1 |
| ch1 | ch1 | A+ | 40 | Bank 0, Pin 2 |
| ch1 | ch1 | A- | 31 | Bank 1, Pin 2 |
| ch1 | ch1 | B+ | 121 | Bank 4, Pin 2 |
| ch1 | ch1 | B- | 130 | Bank 5, Pin 2 |
| ch2 | ch2 | A+ | 42 | Bank 0, Pin 3 |
| ch2 | ch2 | A- | 49 | Bank 1, Pin 3 |
| ch2 | ch2 | B+ | 119 | Bank 4, Pin 3 |
| ch2 | ch2 | B- | 112 | Bank 5, Pin 3 |
| ch3 | ch3 | A+ | 39 | Bank 0, Pin 4 |
| ch3 | ch3 | A- | 32 | Bank 1, Pin 4 |
| ch3 | ch3 | B+ | 122 | Bank 4, Pin 4 |
| ch3 | ch3 | B- | 129 | Bank 5, Pin 4 |
| ch4 | ch4 | A+ | 43 | Bank 0, Pin 5 |
| ch4 | ch4 | A- | 52 | Bank 1, Pin 5 |
| ch4 | ch4 | B+ | 118 | Bank 4, Pin 5 |
| ch4 | ch4 | B- | 109 | Bank 5, Pin 5 |
| ch5 | ch5 | A+ | 38 | Bank 0, Pin 6 |
| ch5 | ch5 | A- | 29 | Bank 1, Pin 6 |
| ch5 | ch5 | B+ | 123 | Bank 4, Pin 6 |
| ch5 | ch5 | B- | 132 | Bank 5, Pin 6 |
| ch6 | ch6 | A+ | 44 | Bank 0, Pin 7 |
| ch6 | ch6 | A- | 53 | Bank 1, Pin 7 |
| ch6 | ch6 | B+ | 117 | Bank 4, Pin 7 |
| ch6 | ch6 | B- | 108 | Bank 5, Pin 7 |
| ch7 | ch7 | A+ | 37 | Bank 0, Pin 8 |
| ch7 | ch7 | A- | 28 | Bank 1, Pin 8 |
| ch7 | ch7 | B+ | 124 | Bank 4, Pin 8 |
| ch7 | ch7 | B- | 133 | Bank 5, Pin 8 |
| ch8 | ch8 | A+ | 45 | Bank 0, Pin 9 |
| ch8 | ch8 | A- | 54 | Bank 1, Pin 9 |
| ch8 | ch8 | B+ | 116 | Bank 4, Pin 9 |
| ch8 | ch8 | B- | 107 | Bank 5, Pin 9 |
| ch9 | ch9 | A+ | 36 | Bank 0, Pin 10 |
| ch9 | ch9 | A- | 27 | Bank 1, Pin 10 |
| ch9 | ch9 | B+ | 125 | Bank 4, Pin 10 |
| ch9 | ch9 | B- | 134 | Bank 5, Pin 10 |
| ch10 | ch10 | A+ | 46 | Bank 0, Pin 11 |
| ch10 | ch10 | A- | 55 | Bank 1, Pin 11 |
| ch10 | ch10 | B+ | 115 | Bank 4, Pin 11 |
| ch10 | ch10 | B- | 106 | Bank 5, Pin 11 |
| ch11 | ch11 | A+ | 35 | Bank 0, Pin 12 |
| ch11 | ch11 | A- | 26 | Bank 1, Pin 12 |
| ch11 | ch11 | B+ | 126 | Bank 4, Pin 12 |
| ch11 | ch11 | B- | 135 | Bank 5, Pin 12 |
| ch12 | ch12 | A+ | 47 | Bank 0, Pin 13 |
| ch12 | ch12 | A- | 56 | Bank 1, Pin 13 |
| ch12 | ch12 | B+ | 114 | Bank 4, Pin 13 |
| ch12 | ch12 | B- | 105 | Bank 5, Pin 13 |
| ch13 | ch13 | A+ | 34 | Bank 0, Pin 14 |
| ch13 | ch13 | A- | 25 | Bank 1, Pin 14 |
| ch13 | ch13 | B+ | 127 | Bank 4, Pin 14 |
| ch13 | ch13 | B- | 136 | Bank 5, Pin 14 |
| ch14 | ch14 | A+ | 48 | Bank 0, Pin 15 |
| ch14 | ch14 | A- | 57 | Bank 1, Pin 15 |
| ch14 | ch14 | B+ | 113 | Bank 4, Pin 15 |
| ch14 | ch14 | B- | 104 | Bank 5, Pin 15 |
| ch15 | ch15 | A+ | 33 | Bank 0, Pin 16 |
| ch15 | ch15 | A- | 24 | Bank 1, Pin 16 |
| ch15 | ch15 | B+ | 128 | Bank 4, Pin 16 |
| ch15 | ch15 | B- | 137 | Bank 5, Pin 16 |
| ch16 | ch16 | A+ | 67 | Bank 2, Pin 1 |
| ch16 | ch16 | A- | 14 | Bank 3, Pin 1 |
| ch16 | ch16 | B+ | 94 | Bank 6, Pin 1 |
| ch16 | ch16 | B- | 147 | Bank 7, Pin 1 |
| ch17 | ch17 | A+ | 15 | Bank 2, Pin 2 |
| ch17 | ch17 | A- | 68 | Bank 3, Pin 2 |
| ch17 | ch17 | B+ | 149 | Bank 6, Pin 2 |
| ch17 | ch17 | B- | 93 | Bank 7, Pin 2 |
| ch18 | ch18 | A+ | 12 | Bank 2, Pin 3 |
| ch18 | ch18 | A- | 13 | Bank 3, Pin 3 |
| ch18 | ch18 | B+ | 91 | Bank 6, Pin 3 |
| ch18 | ch18 | B- | 148 | Bank 7, Pin 3 |
| ch19 | ch19 | A+ | 11 | Bank 2, Pin 4 |
| ch19 | ch19 | A- | 69 | Bank 3, Pin 4 |
| ch19 | ch19 | B+ | 150 | Bank 6, Pin 4 |
| ch19 | ch19 | B- | 92 | Bank 7, Pin 4 |
| ch20 | ch20 | A+ | 70 | Bank 2, Pin 5 |
| ch20 | ch20 | A- | 1 | Bank 3, Pin 5 |
| ch20 | ch20 | B+ | 146 | Bank 6, Pin 5 |
| ch20 | ch20 | B- | 85 | Bank 7, Pin 5 |
| ch21 | ch21 | A+ | 61 | Bank 2, Pin 6 |
| ch21 | ch21 | A- | 4 | Bank 3, Pin 6 |
| ch21 | ch21 | B+ | 100 | Bank 6, Pin 6 |
| ch21 | ch21 | B- | 81 | Bank 7, Pin 6 |
| ch22 | ch22 | A+ | 20 | Bank 2, Pin 7 |
| ch22 | ch22 | A- | 3 | Bank 3, Pin 7 |
| ch22 | ch22 | B+ | 141 | Bank 6, Pin 7 |
| ch22 | ch22 | B- | 157 | Bank 7, Pin 7 |
| ch23 | ch23 | A+ | 62 | Bank 2, Pin 8 |
| ch23 | ch23 | A- | 71 | Bank 3, Pin 8 |
| ch23 | ch23 | B+ | 99 | Bank 6, Pin 8 |
| ch23 | ch23 | B- | 90 | Bank 7, Pin 8 |
| ch24 | ch24 | A+ | 19 | Bank 2, Pin 9 |
| ch24 | ch24 | A- | 10 | Bank 3, Pin 9 |
| ch24 | ch24 | B+ | 142 | Bank 6, Pin 9 |
| ch24 | ch24 | B- | 151 | Bank 7, Pin 9 |
| ch25 | ch25 | A+ | 63 | Bank 2, Pin 10 |
| ch25 | ch25 | A- | 72 | Bank 3, Pin 10 |
| ch25 | ch25 | B+ | 98 | Bank 6, Pin 10 |
| ch25 | ch25 | B- | 89 | Bank 7, Pin 10 |
| ch26 | ch26 | A+ | 18 | Bank 2, Pin 11 |
| ch26 | ch26 | A- | 9 | Bank 3, Pin 11 |
| ch26 | ch26 | B+ | 143 | Bank 6, Pin 11 |
| ch26 | ch26 | B- | 152 | Bank 7, Pin 11 |
| ch27 | ch27 | A+ | 64 | Bank 2, Pin 12 |
| ch27 | ch27 | A- | 73 | Bank 3, Pin 12 |
| ch27 | ch27 | B+ | 97 | Bank 6, Pin 12 |
| ch27 | ch27 | B- | 88 | Bank 7, Pin 12 |
| ch28 | ch28 | A+ | 17 | Bank 2, Pin 13 |
| ch28 | ch28 | A- | 8 | Bank 3, Pin 13 |
| ch28 | ch28 | B+ | 144 | Bank 6, Pin 13 |
| ch28 | ch28 | B- | 153 | Bank 7, Pin 13 |
| ch29 | ch29 | A+ | 65 | Bank 2, Pin 14 |
| ch29 | ch29 | A- | 74 | Bank 3, Pin 14 |
| ch29 | ch29 | B+ | 96 | Bank 6, Pin 14 |
| ch29 | ch29 | B- | 87 | Bank 7, Pin 14 |
| ch30 | ch30 | A+ | 16 | Bank 2, Pin 15 |
| ch30 | ch30 | A- | 7 | Bank 3, Pin 15 |
| ch30 | ch30 | B+ | 145 | Bank 6, Pin 15 |
| ch30 | ch30 | B- | 154 | Bank 7, Pin 15 |
| ch31 | ch31 | A+ | 66 | Bank 2, Pin 16 |
| ch31 | ch31 | A- | 75 | Bank 3, Pin 16 |
| ch31 | ch31 | B+ | 95 | Bank 6, Pin 16 |
| ch31 | ch31 | B- | 86 | Bank 7, Pin 16 |

#### Additional Pin References

| NI PXI-2530B Connector Pin Number | Signal Name |
| --- | --- |
| 2, 21, 22, 23, 59, 60, 77, 78, 79, 80, 101, 102, 138, 140, 160 | NO CONNECT |
| 83, 158 | GND |
| 159 | TRIGIN |
| 82 | TRIGOUT |
| 139 | RESERVED |

Caution

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-relay-replacement.html language=enus -->
## TOPIC 00185: NI PXI-2530B Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2530B uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Coto 9012-05-11 Complete the following steps to replace a failed relay. Ground yourself using a grounding strap or a ground connected to your PXI chassis. Prop

### NI PXI-2530B Relay Replacement

The NI PXI-2530B uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Coto | 9012-05-11 |

Complete the following steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your switch
 module from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the back of module.
 The following table maps the relay names to the reference designator. Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatork0
 K16
 k50
 K126
 k100
 K101k1
 K15
 k51
 K116
 k101
 K108k2
 K14
 k52
 K115
 k102
 K104k3
 K13
 k53
 K113
 k103
 K107k4
 K12
 k54
 K114
 k104
 K103k5
 K11
 k55
 K125
 k105
 K106k6
 K10
 k56
 K124
 k106
 K94k7
 K9
 k57
 K123
 k107
 K105k8
 K8
 k58
 K122
 k108
 K93k9
 K7
 k59
 K121
 k109
 K95k10
 K6
 k60
 K120
 k110
 K102k11
 K5
 k61
 K119
 k111
 K96k12
 K4
 k62
 K118
 k112
 K146k13
 K3
 k63
 K112
 k113
 K144k14
 K2
 k64
 K25
 k114
 K145k15
 K1
 k65
 K32
 k115
 K143k16
 K69
 k66
 K24
 k116
 K133k17
 K68
 k67
 K33
 k117
 K131k18
 K71
 k68
 K23
 k118
 K132k19
 K70
 k69
 K31
 k119
 K142k20
 K67
 k70
 K22
 k120
 K141k21
 K66
 k71
 K30
 k121
 K140k22
 K65
 k72
 K21
 k122
 K139k23
 K64
 k73
 K29
 k123
 K138k24
 K63
 k74
 K20
 k124
 K137k25
 K62
 k75
 K28
 k125
 K136k26
 K56
 k76
 K19
 k126
 K135k27
 K57
 k77
 K27
 k127
 K134k28
 K60
 k78
 K18
 kbc01
 K55k29
 K61
 k79
 K26
 kbc02
 K73k30
 K58
 k80
 K51
 kbc04
 K17k31
 K59
 k81
 K49
 kbc13
 K128k32
 K82
 k82
 K52
 kbc15
 K34k33
 K81
 k83
 K50
 kbc23
 K111k34
 K83
 k84
 K38
 kbc45
 K36k35
 K85
 k85
 K48
 kbc46
 K92k36
 K84
 k86
 K37
 kbc57
 K90k37
 K89
 k87
 K47
 kbc67
 K130k38
 K88
 k88
 K39
 kcom1
 K54k39
 K87
 k89
 K42
 kcom3
 K110k40
 K86
 k90
 K40
 kcom5
 K35k41
 K74
 k91
 K41
 kcom7
 K129k42
 K75
 k92
 K43
 kref01
 K53k43
 K79
 k93
 K45
 kref23
 K109k44
 K78
 k94
 K44
 kref45
 K72k45
 K77
 k95
 K46
 kref67
 K91k46
 K76
 k96
 K100
 —
 —k47
 K80
 k97
 K99
 —
 —k48
 K127
 k98
 K98
 —
 —k49
 K117
 k99
 K97
 —
 —
3. Replace the relay. The NI PXI-2530B uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies and using lead solder for relay replacement on lead
 assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this condition. This rework can prevent the same unit
 from being reworked later on a lead-free solder station, because it could
 contaminate the station.
  1. Make sure you have the following items:
    - Temperature-regulated soldering iron set to 371 °C (700 °F) for
 lead-free solder rework
    - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free
 solder rework
    - Solder wick
    - Isopropyl alcohol
    - Cotton swabs
  2. Replace the relay as you would any other through-hole part.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2530/2530B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2530b-signal-connections.html language=enus -->
## TOPIC 00186: NI PXI-2530B Signal Connections

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2530b-signal-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2530b-signal-connections.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains the pinout and signal connection information for the following types of topologies of the NI PXI-2530B: 1-Wire Multiplexer Topologies 2-Wire Multiplexer Topologies 4-Wire Multiplexer Topologies 1-Wire 4x32 Matrix Topology 1-Wire 8x16 Matrix Topology 2-Wire 4x16 Matrix Topology Ind

### NI PXI-2530B Signal Connections

This book contains the pinout and signal connection information for the following types
 of topologies of the NI PXI-2530B:

- 1-Wire Multiplexer Topologies
- 2-Wire Multiplexer Topologies
- 4-Wire Multiplexer Topologies
- 1-Wire 4x32 Matrix Topology
- 1-Wire 8x16 Matrix Topology
- 2-Wire 4x16 Matrix Topology
- Independent Topology

Parent topic:

NI PXI-2530/2530B

Related concepts:

- NI PXI-2530B 1-Wire Multiplexer and Independent Topologies
- NI PXI-2530B 2-Wire Multiplexer Topologies
- NI PXI-2530B 4-Wire Multiplexer Topologies
- NI PXI-2530B 1-Wire 4x32 Matrix Topology
- NI PXI-2530B 1-Wire 8x16 Matrix Topology
- NI PXI-2530B 2-Wire 4x16 Matrix Topology

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2533-1-wire-4-64-matrix-topology.html language=enus -->
## TOPIC 00187: NI PXI-2533 1-Wire 4×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2533-1-wire-4-64-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2533-1-wire-4-64-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2533 in this topology, connect your signals using the NI TB-2633 terminal block. The following figure represents the NI PXI-2533 in the 1-wire 4×64 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI

### NI PXI-2533 1-Wire 4×64 Matrix Topology

When using the NI PXI-2533 in this topology, connect your signals using the NI TB-2633
 terminal block. The following figure represents the NI PXI-2533 in the 1-wire 4×64
 matrix topology.

[IMAGE alt='image' src='GUID-AEE648E8-A71C-4963-B1DC-28218B6B7259-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI PXI-2533.

[IMAGE alt='image' src='GUID-DD6ABC4F-5A72-4D6A-9E93-DD45E6C0576A-a5.gif']

Parent topic:

NI PXI-2533

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2533-hardware-diagram.html language=enus -->
## TOPIC 00188: NI PXI-2533 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2533-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2533-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2533. The following table lists relay names for the NI PXI-2533. Relays kR0C0...kR0C63 kR1C0...kR1C63 kR2C0...kR2C63 kR3C0...kR3C63

### NI PXI-2533 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2533.

[IMAGE alt='image' src='GUID-AEE648E8-A71C-4963-B1DC-28218B6B7259-a5.gif']

The following table lists relay names for the NI PXI-2533.

| Relays |
| --- |
| kR0C0...kR0C63 |
| kR1C0...kR1C63 |
| kR2C0...kR2C63 |
| kR3C0...kR3C63 |

Parent topic:

NI PXI-2533

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2533-triggering.html language=enus -->
## TOPIC 00189: NI PXI-2533 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2533-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2533-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2533 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2533. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2533 Triggering

The NI PXI-2533 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2533.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2533.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2533

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2533.html language=enus -->
## TOPIC 00190: NI PXI-2533

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2533.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2533.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2533 is a 256-crosspoint, high-density matrix switch module for the PXI platform. The NI PXI-2533 is composed of solid-state relays (SSRs). Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Without

### NI PXI-2533

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2533 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×64 Matrix | 2533/1-Wire 4x64 Matrix(NISWITCH_TOPOLOGY_2533_1_WIRE_4X64_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Solid-State Relays (SSR)
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2533 1-Wire 4×64 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2534-1-wire-8-32-matrix-topology.html language=enus -->
## TOPIC 00191: NI PXI-2534 1-Wire 8×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2534-1-wire-8-32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2534-1-wire-8-32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2534 in this topology, connect your signals using the NI TB-2637 terminal block. The following figure represents the NI PXI-2534 in the 1-wire 8×32 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI

### NI PXI-2534 1-Wire 8×32 Matrix Topology

When using the NI PXI-2534 in this topology, connect your signals using the NI TB-2637
 terminal block. The following figure represents the NI PXI-2534 in the 1-wire 8×32
 matrix topology.

[IMAGE alt='image' src='GUID-647F15A9-A8E0-4437-AB40-4F170CA96D08-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI PXI-2534.

[IMAGE alt='image' src='GUID-8E589FF7-442E-40B7-9D64-36965192F4E6-a5.gif']

Parent topic:

NI PXI-2534

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2534-hardware-diagram.html language=enus -->
## TOPIC 00192: NI PXI-2534 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2534-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2534-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2534. The following table lists relay names for the NI PXI-2534. Relays kR0C0...kR0C31 kR1C0...kR1C31 kR2C0...kR2C31 kR3C0...kR3C31 kR4C0...kR4C31 kR5C0...kR5C31 kR6C0...kR6C31 kR7C0...kR7C31

### NI PXI-2534 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2534.

[IMAGE alt='image' src='GUID-647F15A9-A8E0-4437-AB40-4F170CA96D08-a5.gif']

The following table lists relay names for the NI PXI-2534.

| Relays |
| --- |
| kR0C0...kR0C31 |
| kR1C0...kR1C31 |
| kR2C0...kR2C31 |
| kR3C0...kR3C31 |
| kR4C0...kR4C31 |
| kR5C0...kR5C31 |
| kR6C0...kR6C31 |
| kR7C0...kR7C31 |

Parent topic:

NI PXI-2534

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2534-triggering.html language=enus -->
## TOPIC 00193: NI PXI-2534 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2534-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2534-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2534 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2534. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2534 Triggering

The NI PXI-2534 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2534.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2534.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2534

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2534.html language=enus -->
## TOPIC 00194: NI PXI-2534

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2534.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2534.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2534 is a 256-crosspoint, high-density matrix switch module for the PXI platform. The NI PXI-2534 is composed of solid-state relays (SSRs). Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Without

### NI PXI-2534

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2534 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8×32 Matrix | 2534/1-Wire 8x32 Matrix(NISWITCH_TOPOLOGY_2534_1_WIRE_8X32_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Solid-State Relays (SSR)
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2534 1-Wire 8×32 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2535-1-wire-4-136-matrix-topology.html language=enus -->
## TOPIC 00195: NI PXI-2535 1-Wire 4×136 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2535-1-wire-4-136-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2535-1-wire-4-136-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2535 in the 1-wire 4×136 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters r2 and c1, result in the following connection: signa

### NI PXI-2535 1-Wire 4×136 Matrix Topology

The following figure represents the NI PXI-2535 in the 1-wire 4×136 matrix topology.

[IMAGE alt='image' src='GUID-0199CFD0-6017-4FE0-8E6E-81BEF4BEFD05-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI PXI-2535.

[IMAGE alt='image' src='GUID-4322C254-E856-46BD-B1B5-A93F84CC77C5-a5.gif']

Caution

Parent topic:

NI PXI-2535

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2535-hardware-diagram.html language=enus -->
## TOPIC 00196: NI PXI-2535 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2535-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2535-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2535. The following table lists relay names for the NI PXI-2535. Relays kR0C0...kR0C135 kR1C0...kR1C135 kR2C0...kR2C135 kR3C0...kR3C135

### NI PXI-2535 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2535.

[IMAGE alt='image' src='GUID-0199CFD0-6017-4FE0-8E6E-81BEF4BEFD05-a5.gif']

The following table lists relay names for the NI PXI-2535.

| Relays |
| --- |
| kR0C0...kR0C135 |
| kR1C0...kR1C135 |
| kR2C0...kR2C135 |
| kR3C0...kR3C135 |

Parent topic:

NI PXI-2535

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2535-matrix-expansion.html language=enus -->
## TOPIC 00197: NI PXI-2535 Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2535-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2535-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the matrices of the NI PXI-2535 by increasing the number of columns in the matrix using the SHC68-C68-S cable. Column Expansion on the NI PXI-2535 Complete the following steps to expand the number of columns of a matrix. Connect one end of the SHC68-C68-S cable to a row connector on t

### NI PXI-2535 Matrix Expansion

You can expand the matrices of the NI PXI-2535 by increasing the number of columns in the
 matrix using the SHC68-C68-S cable.

#### Column Expansion on the NI PXI-2535

Complete the following steps to expand the number of columns of a matrix.

1. Connect one end of the SHC68-C68-S cable to a row connector on the
 NI PXI-2535.
2. Connect the other end of the SHC68-C68-S cable to a row connector on another
 NI PXI-2535.

[IMAGE alt='image' src='GUID-C9C6A5CE-A18F-4375-A07F-EDE65C19F9BC-a5.gif']

Parent topic:

NI PXI-2535

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2535-triggering.html language=enus -->
## TOPIC 00198: NI PXI-2535 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2535-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2535-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2535 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2535. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2535 Triggering

The NI PXI-2535 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2535.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2535.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2535

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2535.html language=enus -->
## TOPIC 00199: NI PXI-2535

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2535.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2535.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2535 is a 544-crosspoint, high-density matrix switch module for the PXI platform. The NI PXI-2535 is composed of FET switches. The PXI-2535 has additional fault protection circuitry to prevent overvoltage conditions. If proper grounding is not used on certain applications, relays will app

### NI PXI-2535

The NI PXI-2535 is a 544-crosspoint, high-density matrix switch module for the PXI
 platform. The NI PXI-2535 is composed of FET switches. The PXI-2535 has additional fault
 protection circuitry to prevent overvoltage conditions. If proper grounding is not used
 on certain applications, relays will appear stuck open. For more information about FET
 fault protection circuitry, visit ni.com/info and enter the Info Code
 exfcjv.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2535 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×136 Matrix | 2535/1-Wire 4x136 Matrix(NISWITCH_TOPOLOGY_2535_1_WIRE_4X136_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- FET Switches
- Operation Modes
- NI PXI-2535 1-Wire 4×136 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2536-1-wire-8-68-matrix-topology.html language=enus -->
## TOPIC 00200: NI PXI-2536 1-Wire 8×68 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2536-1-wire-8-68-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2536-1-wire-8-68-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2536 in the 1-wire 8×68 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters r2 and c1, result in the following connection: signal

### NI PXI-2536 1-Wire 8×68 Matrix Topology

The following figure represents the NI PXI-2536 in the 1-wire 8×68 matrix topology.

[IMAGE alt='image' src='GUID-8E51A5A4-D611-4C44-B585-35D714AF04E4-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Pinout

The following figure identifies the pins for the NI PXI-2536.

[IMAGE alt='image' src='GUID-335E441B-D759-47B6-96B5-D56BD02C3912-a5.gif']

Caution

Parent topic:

NI PXI-2536

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2536-hardware-diagram.html language=enus -->
## TOPIC 00201: NI PXI-2536 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2536-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2536-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2536. The following table lists relay names for the NI PXI-2536. Relays kR0C0...kR0C67 kR1C0...kR1C67 kR2C0...kR2C67 kR3C0...kR3C67 kR4C0...kR4C67 kR5C0...kR5C67 kR6C0...kR6C67 kR7C0...kR7C67

### NI PXI-2536 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2536.

[IMAGE alt='image' src='GUID-8E51A5A4-D611-4C44-B585-35D714AF04E4-a5.gif']

The following table lists relay names for the NI PXI-2536.

| Relays |
| --- |
| kR0C0...kR0C67 |
| kR1C0...kR1C67 |
| kR2C0...kR2C67 |
| kR3C0...kR3C67 |
| kR4C0...kR4C67 |
| kR5C0...kR5C67 |
| kR6C0...kR6C67 |
| kR7C0...kR7C67 |

Parent topic:

NI PXI-2536

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2536-matrix-expansion.html language=enus -->
## TOPIC 00202: NI PXI-2536 Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2536-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2536-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the matrices of the NI PXI-2536 by increasing the number of columns in the matrix using the SHC68-C68-S cable. Column Expansion on the NI PXI-2536 Complete the following steps to expand the number of columns of a matrix. Connect one end of the SHC68-C68-S cable to a row connector on t

### NI PXI-2536 Matrix Expansion

You can expand the matrices of the NI PXI-2536 by increasing the number of columns in the
 matrix using the SHC68-C68-S cable.

#### Column Expansion on the NI PXI-2536

Complete the following steps to expand the number of columns of a matrix.

1. Connect one end of the SHC68-C68-S cable to a row connector on the
 NI PXI-2536.
2. Connect the other end of the SHC68-C68-S cable to a row connector on another
 NI PXI-2536.

[IMAGE alt='image' src='GUID-34B0C38D-1B37-4CB4-8569-C212F49623A0-a5.gif']

Parent topic:

NI PXI-2536

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2536-triggering.html language=enus -->
## TOPIC 00203: NI PXI-2536 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2536-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2536-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2536 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2536. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2536 Triggering

The NI PXI-2536 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2536.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2536.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2536

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2536.html language=enus -->
## TOPIC 00204: NI PXI-2536

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2536.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2536.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2536 is a 544-crosspoint, high-density matrix switch module for the PXI platform. The NI PXI-2536 is composed of FET switches. The PXI-2536 has additional fault protection circuitry to prevent overvoltage conditions. If proper grounding is not used on certain applications, relays will app

### NI PXI-2536

The NI PXI-2536 is a 544-crosspoint, high-density matrix switch module for the PXI
 platform. The NI PXI-2536 is composed of FET switches. The PXI-2536 has additional fault
 protection circuitry to prevent overvoltage conditions. If proper grounding is not used
 on certain applications, relays will appear stuck open. For more information about FET
 fault protection circuitry, visit ni.com/info and enter the Info Code
 exfcjv.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2536 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8×68 Matrix | 2536/1-Wire 8x68 Matrix(NISWITCH_TOPOLOGY_2536_1_WIRE_8X68_MATRIX) |  |  |

#### Related Information:

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- FET Switches
- Operation Modes
- NI PXI-2536 1-Wire 8×68 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2541-matrix-expansion.html language=enus -->
## TOPIC 00205: NI PXI-2541 Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2541-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2541-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the matrices of the NI PXI/PXIe-2541 (NI 2541) by increasing the number of columns in the matrix using the MCX Plug to MCX Plug RG316 cable. Column Expansion on the NI PXI/PXIe-2541 Complete the following steps to expand the number of columns of a matrix. Connect one end of the MCX Pl

### NI PXI-2541 Matrix Expansion

You can expand the matrices of the NI PXI/PXIe-2541 (NI 2541) by increasing the number of
 columns in the matrix using the MCX Plug to MCX Plug RG316 cable.

#### Column Expansion on the NI PXI/PXIe-2541

Complete the following steps to expand the number of columns of a matrix.

1. Connect one end of the MCX Plug to MCX Plug RG316 cable to a row out (rXout)
 connector on the NI 2541.
2. Connect the other end of the MCX Plug to MCX Plug RG316 cable to a row in (rX)
 connector on another NI 2541, or NI 2540.
3. Repeat for all rows on which column expansion is desired.

[IMAGE alt='image' src='GUID-390BF9A0-06CA-46B1-B91A-221498415D87-a5.gif']

Parent topic:

NI PXI/PXIe-2541

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2545-front-panel.html language=enus -->
## TOPIC 00206: NI PXI-2545 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2545-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2545-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2545 front panel.

### NI PXI-2545 Front Panel

The following figure illustrates the NI PXI-2545 front panel.

[IMAGE alt='image' src='GUID-C6E555FA-22DB-4C23-821A-6B4777C331C0-a5.gif']

Parent topic:

NI PXI-2545

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2545-hardware-diagram.html language=enus -->
## TOPIC 00207: NI PXI-2545 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2545-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2545-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2545.

### NI PXI-2545 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2545.

[IMAGE alt='image' src='GUID-A544E762-E1C6-4F41-A580-CF7630E147BE-a5.gif']

Parent topic:

NI PXI-2545

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2545-terminated-4-1-multiplexer-sp4t-t.html language=enus -->
## TOPIC 00208: NI PXI-2545 Terminated 4×1 Multiplexer (SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2545-terminated-4-1-multiplexer-sp4t-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2545-terminated-4-1-multiplexer-sp4t-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2545 in the terminated 4×1 multiplexer topology. The terminators on the NI PXI-2545 are rated for 1.5 W at 25 °C. When operating at ambient temperatures greater than 25 °C, a termination power derating applies. Refer the NI PXI-2545 Specifications for mor

### NI PXI-2545 Terminated 4×1 Multiplexer (SP4T) Topology

The following figure represents the NI PXI-2545 in the terminated 4×1 multiplexer
 topology.

|  |
| --- |
|  |

Caution

NI PXI-2545 Specifications

cannot

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, call the niSwitch
 Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

not

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI PXI-2545, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI-2545

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2545-triggering.html language=enus -->
## TOPIC 00209: NI PXI-2545 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2545-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2545-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2545. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2545 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2545.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2545.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2545

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2545.html language=enus -->
## TOPIC 00210: NI PXI-2545

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2545.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2545.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2545 is a terminated multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 2.7 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2545 and possible operation modes. Topology Software Name Immediate Scanning 4x1 Terminated Multiplex

### NI PXI-2545

The NI PXI-2545 is a terminated multiplexer switch module for the PXI bus that can carry
 50 Ω RF signals up to 2.7 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2545 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4x1 Terminated Multiplexer | 2545/4x1 Terminated Mux(NISWITCH_TOPOLOGY_2545_4X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2545 Terminated 4×1 Multiplexer (SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2546-dual-4-1-multiplexer-dual-sp4t-to.html language=enus -->
## TOPIC 00211: NI PXI-2546 Dual 4×1 Multiplexer (Dual SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2546-dual-4-1-multiplexer-dual-sp4t-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2546-dual-4-1-multiplexer-dual-sp4t-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2546 in the dual 4×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disc

### NI PXI-2546 Dual 4×1 Multiplexer (Dual SP4T) Topology

The following figure represents the NI PXI-2546 in the dual 4×1 multiplexer topology.

|  |
| --- |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1A and COM A and the other between CH 2B and
 COM B:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1A and comA .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1A and comA .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2B and comB .

When scanning the NI PXI-2546, a typical scan list entry might be
 ch1A->comA;. This entry routes the signal connected to CH 1A
 to COM A.

Parent topic:

NI PXI-2546

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2546-front-panel.html language=enus -->
## TOPIC 00212: NI PXI-2546 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2546-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2546-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2546 front panel.

### NI PXI-2546 Front Panel

The following figure illustrates the NI PXI-2546 front panel.

[IMAGE alt='image' src='GUID-460B53E4-0B06-4B39-AFD2-74CDD80ED30E-a5.gif']

Parent topic:

NI PXI-2546

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2546-hardware-diagram.html language=enus -->
## TOPIC 00213: NI PXI-2546 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2546-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2546-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2546.

### NI PXI-2546 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2546.

[IMAGE alt='image' src='GUID-8F50812F-A8E0-42ED-ABFD-A2FBA6EC6723-a5.gif']

Parent topic:

NI PXI-2546

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2546-triggering.html language=enus -->
## TOPIC 00214: NI PXI-2546 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2546-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2546-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2546. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2546 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2546.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2546.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2546

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2546.html language=enus -->
## TOPIC 00215: NI PXI-2546

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2546.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2546.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2546 is a multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 2.7 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2546 and possible operation modes. Topology Software Name Immediate Scanning Dual 4×1 Multiplexer 2546/Dual 4x1

### NI PXI-2546

The NI PXI-2546 is a multiplexer switch module for the PXI bus that can carry 50 Ω RF
 signals up to 2.7 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2546 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 4×1 Multiplexer | 2546/Dual 4x1 Mux(NISWITCH_TOPOLOGY_2546_DUAL_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2546 Dual 4×1 Multiplexer (Dual SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2547-8-1-multiplexer-sp8t-topology.html language=enus -->
## TOPIC 00216: NI PXI-2547 8×1 Multiplexer (SP8T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2547-8-1-multiplexer-sp8t-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2547-8-1-multiplexer-sp8t-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2547 in the 8×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconnec

### NI PXI-2547 8×1 Multiplexer (SP8T) Topology

The following figure represents the NI PXI-2547 in the 8×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI PXI-2547, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI-2547

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2547-front-panel.html language=enus -->
## TOPIC 00217: NI PXI-2547 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2547-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2547-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2547 front panel.

### NI PXI-2547 Front Panel

The following figure illustrates the NI PXI-2547 front panel.

[IMAGE alt='image' src='GUID-61CE6A15-5D35-4917-8D78-FB45CB5A85D0-a5.gif']

Parent topic:

NI PXI-2547

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2547-hardware-diagram.html language=enus -->
## TOPIC 00218: NI PXI-2547 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2547-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2547-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2547.

### NI PXI-2547 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2547.

[IMAGE alt='image' src='GUID-AFAE24CC-807B-4BE2-843A-364A07D12E2E-a5.gif']

Parent topic:

NI PXI-2547

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2547-triggering.html language=enus -->
## TOPIC 00219: NI PXI-2547 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2547-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2547-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2547. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2547 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2547.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2547.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2547

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2547.html language=enus -->
## TOPIC 00220: NI PXI-2547

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2547.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2547.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2547 is a multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 2.7 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2547 and possible operation modes. Topology Software Name Immediate Scanning 8×1 Multiplexer 2547/8x1 Mux(NISWIT

### NI PXI-2547

The NI PXI-2547 is a multiplexer switch module for the PXI bus that can carry 50 Ω RF
 signals up to 2.7 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2547 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 8×1 Multiplexer | 2547/8x1 Mux(NISWITCH_TOPOLOGY_2547_8X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2547 8×1 Multiplexer (SP8T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2548-front-panel.html language=enus -->
## TOPIC 00221: NI PXI-2548 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2548-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2548-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2548 front panel.

### NI PXI-2548 Front Panel

The following figure illustrates the NI PXI-2548 front panel.

[IMAGE alt='image' src='GUID-7645555D-B801-4237-A8F3-1AD0BFDC04E8-a5.gif']

Parent topic:

NI PXI-2548

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2548-hardware-diagram.html language=enus -->
## TOPIC 00222: NI PXI-2548 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2548-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2548-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2548.

### NI PXI-2548 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2548.

[IMAGE alt='image' src='GUID-8A7B00B1-C7CC-4BF1-8F63-D2A4BD8B7440-a5.gif']

Parent topic:

NI PXI-2548

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2548-quad-spdt-topology.html language=enus -->
## TOPIC 00223: NI PXI-2548 Quad SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2548-quad-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2548-quad-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2548 in the quad SPDT general-purpose topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch

### NI PXI-2548 Quad SPDT Topology

The following figure represents the NI PXI-2548 in the quad SPDT general-purpose
 topology.

|  |
| --- |
|  |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

x

x

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between NO 1 and COM1 and the other between NC 1 and
 COM1:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters no1 and com1 .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 no1 and com1 .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters nc1 and com1 .

When scanning the NI PXI-2548, a typical scan list entry might be
 no1->com1;. This entry routes the signal connected to NO 1
 to COM 1.

Parent topic:

NI PXI-2548

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2548-triggering.html language=enus -->
## TOPIC 00224: NI PXI-2548 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2548-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2548-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2548. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2548 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2548.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2548.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2548

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2548.html language=enus -->
## TOPIC 00225: NI PXI-2548

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2548.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2548.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2548 is a 4-channel, general-purpose switch module for the PXI bus that can carry 50 Ω RF signals up to 2.7 GHz. The NI PXI-2548 is composed of 4-SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2548 and possible operation modes. Topology Softwar

### NI PXI-2548

The NI PXI-2548 is a 4-channel, general-purpose switch module for the PXI bus that can
 carry 50 Ω RF signals up to 2.7 GHz. The NI PXI-2548 is composed of 4-SPDT relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2548 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4-SPDT | 2548/4-SPDT(NISWITCH_TOPOLOGY_2548_4_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2548 Quad SPDT Topology
- Topologies
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2549-dual-terminated-spdt-topology.html language=enus -->
## TOPIC 00226: NI PXI-2549 Dual Terminated SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2549-dual-terminated-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2549-dual-terminated-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2549 in the dual terminated SPDT general-purpose topology. The terminators on the NI PXI-2549 are rated for 1.5 W at 25 °C. When operating at ambient temperatures greater than 25 °C, a termination power derating applies. Refer the NI PXI-2549 Specificatio

### NI PXI-2549 Dual Terminated SPDT Topology

The following figure represents the NI PXI-2549 in the dual terminated SPDT
 general-purpose topology.

|  |
| --- |
|  |

Caution

NI PXI-2549 Specifications

cannot

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

x

x

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between NO 1 and COM1 and the other between NC 1 and
 COM1:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters no1 and com1 .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 no1 and com1 .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters nc1 and com1 .

When scanning the NI PXI-2549, a typical scan list entry might be
 no1->com1;. This entry routes the signal connected to NO 1
 to COM 1.

Parent topic:

NI PXI-2549

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2549-front-panel.html language=enus -->
## TOPIC 00227: NI PXI-2549 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2549-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2549-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2549 front panel.

### NI PXI-2549 Front Panel

The following figure illustrates the NI PXI-2549 front panel.

[IMAGE alt='image' src='GUID-0274792D-86CC-4CE9-A520-02AF6B5F1C06-a5.gif']

Parent topic:

NI PXI-2549

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2549-hardware-diagram.html language=enus -->
## TOPIC 00228: NI PXI-2549 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2549-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2549-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2549.

### NI PXI-2549 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2549.

[IMAGE alt='image' src='GUID-7B515340-0681-4279-AFA2-5DC7E54E760B-a5.gif']

Parent topic:

NI PXI-2549

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2549-triggering.html language=enus -->
## TOPIC 00229: NI PXI-2549 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2549-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2549-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2549. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2549 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2549.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2549.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2549

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2549.html language=enus -->
## TOPIC 00230: NI PXI-2549

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2549.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2549.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2549 is a 2-channel, general-purpose switch module for the PXI bus that can carry 50 Ω RF signals up to 2.7 GHz. The NI PXI-2549 is composed of two terminated SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2549 and possible operation modes. Top

### NI PXI-2549

The NI PXI-2549 is a 2-channel, general-purpose switch module for the PXI bus that can
 carry 50 Ω RF signals up to 2.7 GHz. The NI PXI-2549 is composed of two terminated SPDT
 relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2549 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Terminated 2-SPDT | 2549/Terminated 2-SPDT(NISWITCH_TOPOLOGY_2549_TERMINATED_2_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2549 Dual Terminated SPDT Topology
- Topologies
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2554-4-1-multiplexer-sp4t-topology.html language=enus -->
## TOPIC 00231: NI PXI-2554 4×1 Multiplexer (SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2554-4-1-multiplexer-sp4t-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2554-4-1-multiplexer-sp4t-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2554 in the 4×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconnec

### NI PXI-2554 4×1 Multiplexer (SP4T) Topology

The following figure represents the NI PXI-2554 in the 4×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI PXI-2554, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI-2554

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2554-front-panel.html language=enus -->
## TOPIC 00232: NI PXI-2554 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2554-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2554-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2554 front panel.

### NI PXI-2554 Front Panel

The following figure illustrates the NI PXI-2554 front panel.

[IMAGE alt='image' src='GUID-D1B5F54C-5C12-4847-96D9-A83F64452483-a5.gif']

Parent topic:

NI PXI-2554

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2554-hardware-diagram.html language=enus -->
## TOPIC 00233: NI PXI-2554 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2554-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2554-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2554.

### NI PXI-2554 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2554.

[IMAGE alt='image' src='GUID-87833749-5F61-454F-BCFB-EDAB6DF2E534-a5.gif']

Parent topic:

NI PXI-2554

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2554-triggering.html language=enus -->
## TOPIC 00234: NI PXI-2554 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2554-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2554-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2554. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2554 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2554.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2554.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2554

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2554.html language=enus -->
## TOPIC 00235: NI PXI-2554

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2554.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2554.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2554 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2554 and possible operation modes. Topology Software Name Immediate Scanning 4×1 Multiplexer 2554/4x1 Mux(NISWIT

### NI PXI-2554

The NI PXI-2554 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF
 signals up to 2.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2554 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4×1 Multiplexer | 2554/4x1 Mux(NISWITCH_TOPOLOGY_2554_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2554 4×1 Multiplexer (SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2555-front-panel.html language=enus -->
## TOPIC 00236: NI PXI-2555 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2555-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2555-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2555 front panel.

### NI PXI-2555 Front Panel

The following figure illustrates the NI PXI-2555 front panel.

[IMAGE alt='image' src='GUID-BFBEF610-99C0-4517-919A-2070046062E1-a5.gif']

Parent topic:

NI PXI-2555

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2555-hardware-diagram.html language=enus -->
## TOPIC 00237: NI PXI-2555 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2555-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2555-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2555.

### NI PXI-2555 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2555.

[IMAGE alt='image' src='GUID-8CB84BE0-7CF5-4D3F-9B35-1C79291C9F72-a5.gif']

Parent topic:

NI PXI-2555

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2555-terminated-4-1-multiplexer-sp4t-t.html language=enus -->
## TOPIC 00238: NI PXI-2555 Terminated 4×1 Multiplexer (SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2555-terminated-4-1-multiplexer-sp4t-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2555-terminated-4-1-multiplexer-sp4t-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2555 in the terminated 4×1 multiplexer topology. The terminators on the NI PXI-2555 are rated for 1.5 W at 25 °C. When operating at ambient temperatures greater than 25 °C, a termination power derating applies. Refer to the NI PXI-2555 Specifications for

### NI PXI-2555 Terminated 4×1 Multiplexer (SP4T) Topology

The following figure represents the NI PXI-2555 in the terminated 4×1 multiplexer
 topology.

|  |
| --- |
|  |

Caution

NI PXI-2555 Specifications

cannot

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, call the niSwitch
 Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

not

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI PXI-2555, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI-2555

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2555-triggering.html language=enus -->
## TOPIC 00239: NI PXI-2555 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2555-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2555-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2555. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2555 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2555.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2555.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2555

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2555.html language=enus -->
## TOPIC 00240: NI PXI-2555

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2555.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2555.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2555 is a terminated multiplexer switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2555 and possible operation modes. Topology Software Name Immediate Scanning 4x1 Terminated Multiplex

### NI PXI-2555

The NI PXI-2555 is a terminated multiplexer switch module for the PXI bus that can carry
 75 Ω RF signals up to 2.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2555 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4x1 Terminated Multiplexer | 2555/4x1 Terminated Mux(NISWITCH_TOPOLOGY_2555_4X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2555 Terminated 4×1 Multiplexer (SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2556-dual-4-1-multiplexer-dual-sp4t-to.html language=enus -->
## TOPIC 00241: NI PXI-2556 Dual 4×1 Multiplexer (Dual SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2556-dual-4-1-multiplexer-dual-sp4t-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2556-dual-4-1-multiplexer-dual-sp4t-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2556 in the dual 4×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disc

### NI PXI-2556 Dual 4×1 Multiplexer (Dual SP4T) Topology

The following figure represents the NI PXI-2556 in the dual 4×1 multiplexer topology.

|  |
| --- |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1A and COM A and the other between CH 2A and
 COM A:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1A and comA .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1A and comA .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2A and comA .

When scanning the NI PXI-2556, a typical scan list entry might be
 ch1A->comA;. This entry routes the signal connected to CH 1A
 to COM A.

Parent topic:

NI PXI-2556

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2556-front-panel.html language=enus -->
## TOPIC 00242: NI PXI-2556 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2556-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2556-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2556 front panel.

### NI PXI-2556 Front Panel

The following figure illustrates the NI PXI-2556 front panel.

[IMAGE alt='image' src='GUID-E4B267F0-E42C-4AFC-97E9-25982193E0D1-a5.gif']

Parent topic:

NI PXI-2556

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2556-hardware-diagram.html language=enus -->
## TOPIC 00243: NI PXI-2556 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2556-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2556-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2556.

### NI PXI-2556 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2556.

[IMAGE alt='image' src='GUID-8F50812F-A8E0-42ED-ABFD-A2FBA6EC6723-a5.gif']

Parent topic:

NI PXI-2556

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2556-triggering.html language=enus -->
## TOPIC 00244: NI PXI-2556 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2556-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2556-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2556. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2556 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2556.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2556.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2556

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2556.html language=enus -->
## TOPIC 00245: NI PXI-2556

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2556.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2556.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2556 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2556 and possible operation modes. Topology Software Name Immediate Scanning Dual 4×1 Multiplexer 2556/Dual 4x1

### NI PXI-2556

The NI PXI-2556 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF
 signals up to 2.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2556 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 4×1 Multiplexer | 2556/Dual 4x1 Mux(NISWITCH_TOPOLOGY_2556_DUAL_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2556 Dual 4×1 Multiplexer (Dual SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2557-8-1-multiplexer-sp8t-topology.html language=enus -->
## TOPIC 00246: NI PXI-2557 8×1 Multiplexer (SP8T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2557-8-1-multiplexer-sp8t-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2557-8-1-multiplexer-sp8t-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2557 in the 8×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconnec

### NI PXI-2557 8×1 Multiplexer (SP8T) Topology

The following figure represents the NI PXI-2557 in the 8×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI PXI-2557, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI-2557

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2557-front-panel.html language=enus -->
## TOPIC 00247: NI PXI-2557 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2557-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2557-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2557 front panel.

### NI PXI-2557 Front Panel

The following figure illustrates the NI PXI-2557 front panel.

[IMAGE alt='image' src='GUID-E3521491-EC05-48B5-A11F-C12680DF7D4F-a5.gif']

Parent topic:

NI PXI-2557

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2557-hardware-diagram.html language=enus -->
## TOPIC 00248: NI PXI-2557 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2557-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2557-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2557.

### NI PXI-2557 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2557.

[IMAGE alt='image' src='GUID-AFAE24CC-807B-4BE2-843A-364A07D12E2E-a5.gif']

Parent topic:

NI PXI-2557

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2557-triggering.html language=enus -->
## TOPIC 00249: NI PXI-2557 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2557-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2557-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2557. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2557 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2557.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2557.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2557

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2557.html language=enus -->
## TOPIC 00250: NI PXI-2557

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2557.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2557.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2557 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2557 and possible operation modes. Topology Software Name Immediate Scanning 8×1 Multiplexer 2557/8x1 Mux(NISWIT

### NI PXI-2557

The NI PXI-2557 is a multiplexer switch module for the PXI bus that can carry 75 Ω RF
 signals up to 2.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2557 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 8×1 Multiplexer | 2557/8x1 Mux(NISWITCH_TOPOLOGY_2557_8X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2557 8×1 Multiplexer (SP8T) Topology
- Integration and System Considerations
