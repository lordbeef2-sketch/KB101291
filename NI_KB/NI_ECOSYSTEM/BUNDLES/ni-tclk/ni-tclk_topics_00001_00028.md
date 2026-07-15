# NI DOCUMENT BUNDLE: ni-tclk

<!--NI_BUNDLE_CHUNK bundle=ni-tclk start=1 end=28 -->
<!--NI_TOPIC bundle=ni-tclk path=distributed-tclk-c-programming-flow.html language=enus -->
## TOPIC 00001: Distributed TClk C Programming Flow

- bundle_id: `ni-tclk`
- source_path: `distributed-tclk-c-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/distributed-tclk-c-programming-flow.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`

### Distributed TClk C Programming Flow

[IMAGE alt='image' src='GUID-07D5A00B-F48E-4C0F-9906-E8D5BD353BC3-a5.gif']

Parent topic:

Distributed TClk

<!--NI_TOPIC bundle=ni-tclk path=distributed-tclk-labview-programming-flow.html language=enus -->
## TOPIC 00002: Distributed TClk LabVIEW Programming Flow

- bundle_id: `ni-tclk`
- source_path: `distributed-tclk-labview-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/distributed-tclk-labview-programming-flow.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`

### Distributed TClk LabVIEW Programming Flow

[IMAGE alt='image' src='GUID-231481F4-1B5D-44FB-B246-E90C476EBE08-a5.gif']

Parent topic:

Distributed TClk

<!--NI_TOPIC bundle=ni-tclk path=distributed-tclk.html language=enus -->
## TOPIC 00003: Distributed TClk

- bundle_id: `ni-tclk`
- source_path: `distributed-tclk.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/distributed-tclk.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Distributed TClk is an advanced TClk application that synchronizes Synchronization and Memory Core (SMC) technology devices that are controlled by different hosts or controllers. Distributed TClk allows you to align SMC devices to an external synchronization event. Each group of TClk-synchronized de

### Distributed TClk

Distributed TClk is an advanced TClk application that synchronizes Synchronization and Memory
 Core (SMC)
 technology
 devices that are controlled by different hosts or controllers. Distributed TClk allows you to
 align SMC devices to an external synchronization event.

Each group of TClk-synchronized devices has a Sync Pulse Sender. The Sync Pulse Sender sends out
 a Sync Pulse to all the other devices. The driver automatically specifies the Sync Pulse
 Sender during the TClk synchronization process. You can also specify the Sync Pulse Sender by
 setting the Export Sync Pulse Output Terminal on one of the TClk-synchronized devices.
 Distributed TClk allows you to use an external signal to synchronize the Sync Pulse Senders
 from multiple groups of TClk-synchronized devices.

If you use a Timing and Synchronization device, you can share the CLK_10 Reference Clock and
 create a valid synchronization event across many chassis with different controllers, or across
 chassis that are physically separated.  To synchronize devices to an external event, all the
 devices must share the same CLK_10 Reference Clock. The event must occur at the same time in
 all the chassis and be synchronous with the same rising edge of CLK_10.

Note

| LabVIEW VI | C Function |
| --- | --- |
| niTClk Setup for Sync Pulse Sender Synchronize VI | niTClk_SetupforSyncPulseSenderSynchronize |
| niTClk Synchronize to Sync Pulse Sender VI | niTClk_SynchronizetoSyncPulseSender |
| niTClk Finish Sync Pulse Sender Synchronize VI | niTClk_FinishSyncPulseSenderSynchronize |

| LabVIEW Property | C Attribute |
| --- | --- |
| External Pulse Source | NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE |

<!--NI_TOPIC bundle=ni-tclk path=ni-services.html language=enus -->
## TOPIC 00004: NI Services

- bundle_id: `ni-tclk`
- source_path: `ni-services.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-services.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI provides global services and support as part of our commitment to your success. Take advantage of product services in addition to training and certification programs that meet your needs during each phase of the application life cycle; from planning and development through deployment and ongoing

### NI Services

NI provides global services and support as part of our commitment to your success. Take advantage of product services in addition to training and certification programs that meet your needs during each phase of the application life cycle; from planning and development through deployment and ongoing maintenance.

To get started, create an account or log in to your MyNI user profile at ni.com/myproducts and register your product.

As a registered NI product user, you are entitled to the following benefits:

- Access to applicable product services.
- Easier product management with an online account.
- Receive critical part notifications, software updates, and service expirations.

Services and Resources

- Maintenance and Hardware Services —NI helps you identify your systems' accuracy and reliability requirements and provides warranty, sparing, and calibration services to help you maintain accuracy and minimize downtime over the life of your system. Visit ni.com/services for more information.
  - Warranty and Repair —All NI hardware features a one-year standard warranty that is extendable up to five years. NI offers repair services performed in a timely manner by highly trained factory technicians using only original parts at a NI service center.
  - Calibration —Through regular calibration, you can quantify and improve the measurement performance of an instrument. NI provides state-of-the-art calibration services. If your product supports calibration, you can obtain the calibration certificate for your product at ni.com/calibration.
- System Integration —If you have time constraints, limited in-house technical resources, or other project challenges, National Instruments Alliance Partner members can help. To learn more, call your local NI office or visit ni.com/alliance.
- Training and Certification —The NI training and certification program is the most effective way to increase application development proficiency and productivity. Visit ni.com/training for more information.
  - The Skills Guide assists you in identifying the proficiency requirements of your current application and gives you options for obtaining those skills consistent with your time and budget constraints and personal learning preferences. Visit ni.com/skills-guide to see these custom paths.
  - NI offers courses in several languages and formats including instructor-led classes at facilities worldwide, courses on-site at your facility, and online courses to serve your individual needs.
- Technical Support —Support at ni.com/support includes the following resources:
  - Self-Help Technical Resources —Visit ni.com/support for software drivers and updates, a searchable KnowledgeBase, product manuals, step-by-step troubleshooting wizards, thousands of example programs, tutorials, application notes, instrument drivers, and so on. Registered users also receive access to the NI Discussion Forums at ni.com/forums. NI Applications Engineers make sure every question submitted online receives an answer.
  - Software Support Service Membership —The Standard Service Program (SSP) is a renewable one-year subscription included with almost every NI software product, including NI Developer Suite. This program entitles members to direct access to NI Applications Engineers through phone and email for one-to-one technical support, as well as exclusive access to online training modules at ni.com/self-paced-training. NI also offers flexible extended contract options that guarantee your SSP benefits are available without interruption for as long as you need them. Visit ni.com/ssp for more information.
- Declaration of Conformity (DoC) —A DoC is our claim of compliance with the Council of the European Communities using the manufacturer's declaration of conformity. This system affords the user protection for electromagnetic compatibility (EMC) and product safety. You can obtain the DoC for your product by visiting ni.com/certification.

For information about other technical support options in your area, visit ni.com/services or contact your local office at ni.com/contact.

You can also visit the Worldwide Offices section of ni.com/niglobal to access the branch office websites, which provide up-to-date contact information, support phone numbers, email addresses, and current events.

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-c-functions-programming-flow-2.html language=enus -->
## TOPIC 00005: C Functions Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-c-functions-programming-flow-2.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-c-functions-programming-flow-2.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Heterogeneous Trigger, Single Chassis or PC

### C Functions Programming Flow

#### Heterogeneous Trigger, Single Chassis or PC

[IMAGE alt='image' src='GUID-33A9ECC3-27B6-4C71-BFDF-C7801158C2CC-a5.gif']

Parent topic:

Synchronization in a Single PXI Chassis or a Single PC with Heterogeneous Triggers

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-c-functions-programming-flow-4.html language=enus -->
## TOPIC 00006: C Functions Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-c-functions-programming-flow-4.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-c-functions-programming-flow-4.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multiple Chassis

### C Functions Programming Flow

#### Multiple Chassis

[IMAGE alt='image' src='GUID-AEEC5443-BDF5-4E37-B9B0-9DF8B7B38320-a5.gif']

Parent topic:

Synchronization in Multiple PXI Chassis

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-c-functions-programming-flow.html language=enus -->
## TOPIC 00007: C Functions Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-c-functions-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-c-functions-programming-flow.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Homogeneous Trigger, Single Chassis or PC

### C Functions Programming Flow

#### Homogeneous Trigger, Single Chassis or PC

[IMAGE alt='image' src='GUID-3FC1E509-8835-47D2-9220-2167A1AB92BA-a5.gif']

Parent topic:

Synchronization in a Single PXI Chassis or a Single PC with Homogeneous Triggers

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-comparison-of-terminology-between-ni.html language=enus -->
## TOPIC 00008: Comparison of Terminology between NI-TClk, NI-HSDIO, NI-SCOPE, and NI-FGEN

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-comparison-of-terminology-between-ni.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-comparison-of-terminology-between-ni.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some of the terminology used in NI-TClk and NI-HSDIO differs from the terminology used in NI-SCOPE and NI-FGEN. The following table lists the equivalent names used by NI-TClk and these drivers. NI-TClk and NI-HSDIO Signal Names NI-SCOPE Signal Names NI-FGEN Signal NamesReference Clock Input Clock Ou

### Comparison of Terminology between NI-TClk,
 NI-HSDIO, NI-SCOPE, and NI-FGEN

Some of the terminology used in NI-TClk and NI-HSDIO differs from the terminology used in 
NI-SCOPE and NI-FGEN. The following table lists the equivalent names used by NI-TClk and these drivers.

| NI-TClk and NI-HSDIO Signal Names | NI-SCOPE Signal Names | NI-FGEN Signal Names |
| --- | --- | --- |
| Reference Clock | Input Clock Output Clock Reference Clock | Reference Clock Board Clock |
| Sample Clock | Sample Clock | Update ClockSample Clock |
| Start Trigger | Acquisition Arm Trigger Start Trigger | Trigger Start Trigger |
| Reference Trigger | Trigger Stop Trigger | N/A |
| None (no trigger configured) | Immediate Trigger | Immediate Trigger |
| RTSI 7 | RTSI_CLK | RTSI_7 |

Parent topic:

NI-TClk Overview

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-configuring-pxi-chassis-with-multiple.html language=enus -->
## TOPIC 00009: Configuring PXI Chassis with Multiple Bus Segments (18-Slot Chassis)

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-configuring-pxi-chassis-with-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-configuring-pxi-chassis-with-multiple.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: To synchronize modules in a PXI chassis with multiple bus segments, such as the PXI-1045, configure the crosspoint switches through MAX. Crosspoint switches are routing modules that drive the PXI triggers across segments. Use the niTClk Configure For Homogeneous Triggers VI or the niTClk_ConfigureFo

### Configuring PXI Chassis with Multiple Bus
 Segments (18-Slot Chassis)

To synchronize modules in a PXI chassis with multiple bus segments, such as the PXI-1045,
 configure the crosspoint switches through MAX. Crosspoint switches are routing modules that
 drive the PXI triggers across segments. Use the niTClk Configure For Homogeneous
 Triggers VI or the
 niTClk_ConfigureForHomogeneousTriggers
 function to route triggers automatically, and configure the crosspoint switches. If you want
 to manually route the triggers and the master and slave devices are in different segments (as
 is necessary in a multi-chassis system), you must manually configure the crosspoint
 switches.

Perform the following steps to manually configure the crosspoint switches in the chassis.

1. Launch MAX .
2. Identify the chassis by following the procedures that are described in the Measurement
 & Automation Explorer Help for PXI .
3. Select the identified chassis name in the configuration tree and click the
 Triggers tab in the right pane. The Triggers tab
 contains the PXI trigger line reservations and routing options for the crosspoint switches.
4. Verify routing for the crosspoint switches.
  - Click the Trigger Routing tab.
  - Verify that all the PXI trigger lines that carry manually configured triggers, driven by
 the master device, such as Start, Stop, and Exported Sync Pulse, are routed away from
 the master device. To change the configurations, select Away from Bus
 1 , Away from Bus 2 , or Away from Bus
 3 , for each manually configured trigger.
  - Verify that the PXI trigger lines, mentioned in the above step, are reserved, so that no
 other device can use them.
5. If you are using a System Timing Slot controller to resynchronize the Exported Sync Pulse from
 the master device, and send it back to all the devices as the Sync Pulse , configure
 the routing for the PXI trigger line with the Sync Pulse as away from the System
 Timing Slot.

Note

Sync Pulse

Related concepts:

- Sync Pulse and Sync Pulse Clock

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-external-sample-clock-and-external-sa.html language=enus -->
## TOPIC 00010: External Sample Clock and External Sample Clock Timebase Considerations

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-external-sample-clock-and-external-sa.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-external-sample-clock-and-external-sa.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-TClk works with internal and external Sample Clocks, and with internal and external Sample Clock timebases for the NI modular instruments that support them.If all of the sessions that you are synchronizing have external Sample Clocks or external Sample Clock timebases, then the Sample Clock or Sa

### External Sample Clock and External Sample
 Clock Timebase Considerations

NI-TClk works with internal and external Sample Clocks, and with internal and external Sample
 Clock timebases for the NI modular instruments that support them.

If all of the sessions that you are synchronizing have external Sample Clocks or external Sample
 Clock timebases, then the Sample Clock or Sample Clock timebase rates of all the sessions must
 be equal.

If some of the sessions that you are synchronizing have internal Sample Clocks and other sessions
 have external Sample Clocks or external Sample Clock timebases, then the rates of all the
 external Sample Clocks or the external Sample Clock timebases must be equal to one of the
 internal Sample Clocks.

Parent topic:

NI-TClk Overview

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-homogeneous-and-heterogeneous-trigger.html language=enus -->
## TOPIC 00011: Homogeneous and Heterogeneous Triggers

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-homogeneous-and-heterogeneous-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-homogeneous-and-heterogeneous-trigger.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-TClk provides a simplified interface for synchronizing systems with homogeneous triggers in a single PXI chassis or PC. NI-TClk also provides a flexible interface for other supported systems. Triggers Supported by NI-TClk.The following table summarizes the triggers supported by NI-TClk. Trigger A

### Homogeneous and Heterogeneous Triggers

NI-TClk provides a simplified interface for synchronizing systems with homogeneous triggers in a
 single PXI chassis or PC. NI-TClk also provides a flexible interface for other supported
 systems. Triggers Supported by NI-TClk.

The following table summarizes the triggers supported by NI-TClk.

| Trigger | Acquisition | Generation |
| --- | --- | --- |
| Start Trigger | Yes | Yes |
| Reference Trigger | Yes | N/A |
| Script Trigger 0 – 3 | N/A | Yes |
| Pause Trigger | No | Yes |

Individual instruments may support some or all of the triggers listed in the previous table.
 Instruments may also support triggers other than those listed in the previous table. These
 other triggers, as well as Pause Triggers for acquisition sessions, are not supported by
 NI-TClk and are not relevant to the definition of homogeneous triggers. For information about
 which triggers your device supports, refer to the device documentation.

#### Homogeneous Triggers

If the triggers in
 synchronized sessions are synchronized, these triggers are considered homogeneous triggers.

Note

None

Comparison of Terminology between NI-TClk, NI-HSDIO, NI-SCOPE, and NI-FGEN

For each of the other triggers
 supported by NI-TClk, one of the following conditions must be true:

- The trigger is not supported by any of the sessions.
- The trigger is configured to None by all sessions that support it.
- One of the sessions, called the trigger master session, is configured to receive the
 trigger from the external world (in case of external triggers) or to generate that trigger
 (in case of None or software triggers), and the corresponding trigger on all other
 sessions is configured so that it comes from the trigger on the trigger master
 session.

If there is a trigger master session, non-master sessions must use the triggers that
 they receive from the trigger master session for the same purpose as the trigger master
 session. For example, the Reference Trigger from the reference trigger master session must
 be used as the Reference Trigger for the non-master sessions.

The type of trigger for
 the trigger master session is not relevant for this definition. The type of trigger for
 non-master sessions must be digital edge or digital level because the trigger generated by
 the trigger master is a digital signal.

With TClk synchronization, all sessions react
 to a synchronized trigger at the same time.

#### Heterogeneous Triggers

Sessions that do not
 have homogenous triggers, have heterogeneous triggers. If the session does not fulfill any
 of the conditions that are specified in the homogeneous triggers section, these sessions
 have heterogeneous triggers.

#### Example 1: Homogeneous Triggers

Sessions A and B have triggers as indicated in the following table. Sessions A and B have homogeneous triggers.

| Trigger | Session A (Generation) | Session B (Generation) |
| --- | --- | --- |
| Start Trigger | Software Trigger | Start Trigger from session A |
| Reference Trigger | Not supported | Not supported |
| Script Trigger 0 – 3 | Not supported | Not supported |
| Pause Trigger | Not supported | Not supported |

#### Example 2: Homogeneous Triggers

Sessions A, B, C, and D have triggers as indicated in the following table. Sessions A, B, C, and D have homogeneous triggers. Notice that session A is the master session for the Start Trigger, and session B is the master session for the Reference Trigger.

| Trigger | Session A (Acquisition) | Session B (Acquisition) | Session C (Generation) | Session D (Generation) |
| --- | --- | --- | --- | --- |
| Start Trigger | None | Start trigger from session A | Start trigger from session A | Start trigger from session A |
| Reference Trigger | Reference Trigger from session B | Analog edge Trigger | Not supported | Not supported |
| Script Trigger 0–3 | Not supported | Not supported | None | None |
| Pause Trigger | Not supported | Not supported | None | None |

#### Example 3: Heterogeneous Triggers

Sessions A, B, and C have triggers as indicated in the following table. Sessions A, B, and
 C have heterogeneous triggers because neither the Script Trigger nor the Pause Trigger
 comply with any of the three required conditions to be a homogeneous trigger.

| Trigger | Session A (Generation) | Session B (Generation) | Session C (Generation) |
| --- | --- | --- | --- |
| Start Trigger | Software Trigger | Start Trigger from session A | Start Trigger from session A |
| Reference Trigger | Not supported | Not supported | Not supported |
| Script Trigger 0 | Digital edge | None | None |
| Script Trigger 1–3 | None | None | None |
| Pause Trigger | None | Digital level | Pause Trigger from session B |

Parent topic:

NI-TClk Overview

Related concepts:

- Comparison of Terminology between NI-TClk, NI-HSDIO, NI-SCOPE, and NI-FGEN

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-overview.html language=enus -->
## TOPIC 00012: NI-TClk Overview

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-overview.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file contains information about using the NI-TClk library to synchronize supported NI devices. This help file also contains programming flows and programming reference information for NI-TClk LabVIEW VIs and properties, as well as NI-TClk C functions and attributes.Use TClk synchronization

### NI-TClk Overview

This help file contains information about using the NI-TClk library to synchronize supported
 NI devices. This help file also contains programming flows and programming reference
 information for NI-TClk LabVIEW VIs and properties, as well as NI-TClk C functions and
 attributes.

Use TClk synchronization to allow multiple instruments to simultaneously respond to triggers, to
 align Sample Clocks on multiple instruments, and/or to simultaneously start multiple
 instruments.

The NI-TClk library allows you to synchronize NI modular instruments in the following
 situations:

- In a single PXI chassis or in multiple PXI chassis.
- In a single PC.
- When an individual instrument uses triggers for any purpose. For example, when you want two
 different modular instruments to share a Start Trigger or when you
 want to use the Start Trigger from one modular instrument as the
 Reference Trigger on another modular instrument.
- When Sample Clock rates are equal, and/or when the Sample Clock rates are different.

Note

NI-TClk
 External Sample Clock and External Sample Clock Timebase Considerations

NI-TClk Sample Clock Delay

#### The TClk Signal

NI-TClk does not limit
 the number of modules or chassis that you can synchronize.

The Trigger Clock
 (TClk) is a periodic signal used to synchronize triggers. The devices do not share
 the TClk signal. Each device generates the TClk signal from its Sample Clock or
 Sample Clock timebase. Use the *Sync Pulse and Sync Pulse Clock* signals
 to synchronize TClk signals on different devices.

When using an internal
 Sample Clock, devices must have a common Reference Clock. When using an external
 Sample Clock, devices must have a common Sample Clock or Sample Clock
 timebase.

Note

#### Example

The following figure shows an example of synchronizing two devices that have
 internal Sample Clocks and a common 10 MHz Reference Clock.

[IMAGE alt='image' src='GUID-63D4C65B-75EA-4CF5-9672-3EA61F335F4B-a5.gif']

Device 1 is the Start Trigger master, with a Sample Clock rate of 50 MHz. Device 2
 is the Start Trigger slave, with a Sample Clock rate of 20 MHz. The TClk frequency
 is 5 MHz.

#### The Effect of TClk on Trigger Response
 Time

Since devices react to TClk-synchronized triggers with delays and
 uncertainties that are comparable to the TClk period (200 ns or more), the trigger
 reaction time for synchronized devices is higher than that for individual devices.
 However, this condition does not impact time stamping of the Reference Triggers for
 acquisitions, so the Reference Trigger positions are correctly reported for
 TClk-synchronized devices.

#### Instrument Drivers and NI-TClk

An
 instrument driver is a library of VIs or functions that control individual devices.
 For example, NI-SCOPE, NI-FGEN, NI-RFSA, NI-RFSG, and NI-HSDIO are instrument
 drivers. NI-TClk is a library designed for use with instrument
 drivers.

High-level NI-TClk VIs or functions are different from typical
 instrument driver VIs or functions because the TClk VIs or functions accept arrays
 of sessions instead of individual sessions. A session is a software concept for
 communicating and interacting with a particular physical instrument or a subset of a
 physical instrument. For example, you can use an NI-SCOPE session to communicate
 with a digitizer, and an NI-HSDIO acquisition session to communicate with the
 acquisition subset of a digital waveform generator/analyzer.

In LabVIEW,
 obtain these sessions from your instrument driver, by using the <driver name>
 Get Session Reference VI. In C, NI-TClk accepts regular instrument driver
 sessions.

Related concepts:

- Synchronization in Multiple PXI Chassis
- External Sample Clock and External Sample Clock Timebase Considerations
- Sample Clock Delay
- Sync Pulse and Sync Pulse Clock

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-performance-optimization.html language=enus -->
## TOPIC 00013: Performance Optimization

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-performance-optimization.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-performance-optimization.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: To ensure that synchronization is correct, call the niTClk Synchronize VI or the niTClk_Synchronize function whenever you change a clocking attribute or a sample rate attribute for a TClk-synchronized device. Each call to the niTClk Synchronize VI or the niTClk_Synchronize function adds time to the

### Performance Optimization

To ensure that synchronization is correct, call the niTClk
 Synchronize VI or
 the
 niTClk_Synchronize
 function whenever you change a clocking attribute or a sample rate attribute for a
 TClk-synchronized device. Each call to the niTClk Synchronize VI or the niTClk_Synchronize
 function adds time to the application execution.

To optimize the performance of your application, set the clocking and sample rate attributes only
 once, and then call the niTClk Synchronize VI or the niTClk_Synchronize function.

You do not need to call the niTClk Synchronize VI or the niTClk_Synchronize function every time
 you start an acquisition, unless you change attributes that affect the clocking or the sample
 rate. The following table lists attributes that affect the clocking or the sample rate. For
 the 5922 digitizer, the list of attributes also includes channel-based attributes.

Caution

Tip

niTClk_ConfigureForHomogeneousTriggers

| Driver | LabVIEW Property | C Attribute | Comment |
| --- | --- | --- | --- |
| NI-FGEN | Sample Rate | NIFGEN_ATTR_ARB_SAMPLE_RATE |  |
| NI-FGEN | Sample Clock Timebase Rate | NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE |  |
| NI-FGEN | Sample Clock Timebase Source | NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE |  |
| NI-FGEN | Sample Clock Mode | NIFGEN_ATTR_CLOCK_MODE |  |
| NI-FGEN | Sample Clock Source | NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE |  |
| NI-FGEN | Reference Clock Source | NIFGEN_ATTR_REF_CLOCK_SOURCE |  |
| NI-FGEN | Reference Clock Frequency | NIFGEN_ATTR_REF_CLOCK_FREQUENCY |  |
| NI-FGEN | Frequency | NIFGEN_ATTR_FUNC_FREQUENCY | Only applies to some devices |
| NI-FGEN | Waveform | NIFGEN_ATTR_FUNC_WAVEFORM | Only applies to some devices |
| NI-FGEN | OSP Enabled | NIFGEN_ATTR_OSP_ENABLED |  |
| NI-FGEN | IQ Rate | NIFGEN_ATTR_OSP_IQ_RATE |  |
| NI-FGEN | CIC Interpolation Factor | NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION |  |
| NI-FGEN | FIR Interpolation Factor | NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION |  |
| NI-HSDIO | RefClk.Source | NIHSDIO_ATTR_REF_CLOCK_SOURCE |  |
| NI-HSDIO | RefClk.Rate | NIHSDIO_ATTR_REF_CLOCK_RATE |  |
| NI-HSDIO | RefClk.Impedance | NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE | External reference clock only |
| NI-HSDIO | SampClk.Source | NIHSDIO_ATTR_SAMPLE_CLOCK_SOURCE |  |
| NI-HSDIO | SampClk.Rate | NIHSDIO_ATTR_SAMPLE_CLOCK_RATE |  |
| NI-HSDIO | SampClk.Impedance | NIHSDIO_ATTR_SAMPLE_CLOCK_IMPEDANCE | External sample clock only |
| NI-RFSA | Digitizer Sample Clock Timebase Source | NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE |  |
| NI-RFSA | Digitizer Sample Clock Timebase Rate | NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE |  |
| NI-RFSA | Ref Clock Source | NIRFSA_ATTR_REF_CLOCK_SOURCE |  |
| NI-RFSA | Ref Clock Rate | NIRFSA_ATTR_REF_CLOCK_RATE |  |
| NI-RFSG | IO Rate | NIRFSG_ATTR_IQ_RATE |  |
| NI-RFSG | Arb Sample Clock Rate | NIRFSG_ATTR_ARB_SAMPLE_CLOCK_RATE |  |
| NI-RFSG | Arb Sample Clock Source | NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE |  |
| NI-RFSG | Reference Clock Rate | NIRFSG_ATTR_REF_CLOCK_RATE |  |
| NI-RFSG | Reference Clock Source | NIRFSG_ATTR_REF_CLOCK_SOURCE |  |
| NI-SCOPE | Min Sample Rate | NISCOPE_ATTR_MIN_SAMPLE_RATE |  |
| NI-SCOPE | Input Clock Source | NISCOPE_ATTR_CLOCK_SOURCE |  |
| NI-SCOPE | Reference Clock Rate | NISCOPE_ATTR_REF_CLK_RATE |  |
| NI-SCOPE | Sample Clock Timebase Source | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC |  |
| NI-SCOPE | Sample Clock Timebase Rate | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE |  |
| NI-SCOPE | Sample Clock Timebase Divisor | NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV |  |
| NI-SCOPE | Max Input Frequency | NISCOPE_ATTR_MAX_INPUT_FREQUENCY | Only applies to some devices |

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-programming-examples.html language=enus -->
## TOPIC 00014: Programming Examples

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-programming-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-programming-examples.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-TClk programming examples are installed with the programming examples for the instrument driver. Select Start»All Programs»National Instruments»<driver name>»Examples to access these examples.

### Programming Examples

NI-TClk programming examples are installed with the programming examples for the instrument driver. Select Start»All Programs»National Instruments»<driver name>»Examples to access these examples.

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-pxi-and-rtsi-trigger-lines.html language=enus -->
## TOPIC 00015: PXI and RTSI Trigger Lines

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-pxi-and-rtsi-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-pxi-and-rtsi-trigger-lines.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-TClk uses the PXI trigger lines and the RTSI trigger lines to share signals between devices. Using the PXI Trigger Lines Because PXI_CLK10 and the PXI trigger lines are essential for synchronization, you must use a PXI chassis. You cannot use a CompactPCI chassis that is not also a PXI chassis.Co

### PXI and RTSI Trigger Lines

NI-TClk uses the PXI trigger lines and the RTSI trigger lines to share signals between
 devices.

#### Using the PXI Trigger Lines

Caution

Configure your PXI
 system in MAX to use the routing provided by the high-level NI-TClk VIs or functions
 and to avoid getting errors.

Note

Devices and Interfaces»NI-DAQmx Devices

For more information about configuring your PXI system, refer to the
 Measurement & Automation Explorer Help for PXI. To access
 this help file, launch MAX, and select Help»Help
 Topics»PXI.

#### Using the RTSI Trigger Lines

To use the
 routing provided by the high-level NI-TClk VIs or functions and to avoid getting
 errors, connect the devices with a RTSI cable and create a new device entry for the
 RTSI cable in MAX. For information about connecting your devices with a RTSI cable,
 refer to the device documentation.

Note

not

Devices and Interfaces»NI-DAQmx Devices

For more
 information about using the RTSI trigger lines, refer to the
 Measurement & Automation Explorer Help for NI-DAQmx. To
 access this help file, launch MAX, and select Help»Help
 Topics»NI-DAQmx»MAX Help for NI-DAQmx.

Parent topic:

NI-TClk Overview

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-sample-clock-delay.html language=enus -->
## TOPIC 00016: Sample Clock Delay

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-sample-clock-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-sample-clock-delay.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using the internal Sample Clock, you can delay the Sample Clock on some sessions, relative to other sessions, by setting the Sample Clock Delay property or the NITCLK_ATTR_SAMPLE_CLOCK_DELAY attribute.

### Sample Clock Delay

If you are using the internal Sample Clock, you can delay the Sample Clock on some sessions,
 relative to other sessions, by setting the Sample Clock
 Delay
 property or the
 NITCLK_ATTR_SAMPLE_CLOCK_DELAY
 attribute.

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-sync-pulse-and-sync-pulse-clock.html language=enus -->
## TOPIC 00017: Sync Pulse and Sync Pulse Clock

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-sync-pulse-and-sync-pulse-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-sync-pulse-and-sync-pulse-clock.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sync PulseThe Sync Pulse signal is used to synchronize TClk signals on different devices. When you run the niTClk Synchronize VI or the niTClk_Synchronize function, one of the synchronized devices produces a series of Sync Pulses, which must be received by all the synchronized devices. TClk uses the

### Sync Pulse and Sync Pulse Clock

#### Sync
 Pulse

The Sync Pulse signal is used to synchronize *TClk signals*
 on different devices. When you run the niTClk Synchronize VI or the
 niTClk_Synchronize function, one of the synchronized devices
 produces a series of Sync Pulses, which must be received by all the synchronized
 devices. TClk uses the Sync Pulse to then measure the misalignment between TClks on
 different devices, as shown in the following figure.

[IMAGE alt='image' src='GUID-310F25D5-06DD-4FD7-A7B4-676BDB679D7E-a5.gif']

If all the devices are in one PXI chassis or one PC, the niTClk Synchronize VI or
 the niTClk_Synchronize function routes the Sync Pulse automatically if
 a *PXI trigger line or a RTSI line* is available.

If the devices are
 in *multiple PXI chassis*, or if the devices are in a PXI chassis with
 *multiple bus segments (18-slot chassis)*, the Sync Pulse signal is not
 automatically routed. You must configure the signal routing for the
 system.

#### Sync Pulse Clock

Sync Pulse Clock is a
 signal used during the synchronization of TClk signals on different devices. For PXI
 devices, this signal must come from PXI_CLK10. For PCI devices, the signal must come
 from RTSI 7. Typically, the Reference Clock is used as the Sync Pulse Clock, as shown in
 the previous figure.

For both PXI and PCI devices, the signal must be 10 MHz. The
 niTClk Synchronize VI or the niTClk_Synchronize function routes this
 signal automatically unless you use the Sync Pulse Clock Source property or the
 NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE attribute.

Parent topic:

NI-TClk Overview

Related concepts:

- NI-TClk Overview
- PXI and RTSI Trigger Lines
- Synchronization in Multiple PXI Chassis
- Configuring PXI Chassis with Multiple Bus Segments (18-Slot Chassis)

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-synchronization-in-a-single-pxi-chass.html language=enus -->
## TOPIC 00018: Synchronization in a Single PXI Chassis or a Single PC with Homogeneous Triggers

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-synchronization-in-a-single-pxi-chass.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-synchronization-in-a-single-pxi-chass.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: To synchronize several instrument sessions with homogeneous triggers in a single PXI chassis or a single PC, use the VIs or functions listed in the following table. Before using these NI-TClk VIs or functions, verify that your system is configured as described in the PXI Trigger Lines and RTSI Lines

### Synchronization in a Single PXI Chassis or a
 Single PC with Homogeneous Triggers

homogeneous triggers

Note

PXI Trigger Lines and RTSI Lines

| LabVIEW VI | C Function |
| --- | --- |
| niTClk Configure For Homogeneous Triggers | niTClk_ConfigureForHomogeneousTriggers |
| niTClk Synchronize | niTClk_Synchronize |
| niTClk Initiate | niTClk_Initiate |
| niTClk Is Done (optional) or niTClk Wait Until Done | niTClk_IsDone (optional) or niTClk_WaitUntilDone |
| N/A | niTClk_GetExtendedErrorInfo |

For more information on NI-TClk VIs and functions, see *NI-TClk C Function
 Reference* on *ni.com/docs*.

Related concepts:

- Homogeneous and Heterogeneous Triggers
- PXI and RTSI Trigger Lines

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-synchronization-in-a-single-pxi-chass_hetero.html language=enus -->
## TOPIC 00019: Synchronization in a Single PXI Chassis or a Single PC with Heterogeneous Triggers

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-synchronization-in-a-single-pxi-chass_hetero.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-synchronization-in-a-single-pxi-chass_hetero.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: To synchronize several NI modular instruments with heterogeneous triggers in a single PXI chassis or a single PC, use the NI-TClk VIs or functions listed in the following table. Use the instrument driver functions to route the triggers so that the triggers can be shared. Before using these NI-TClk V

### Synchronization in a Single PXI Chassis or a
 Single PC with Heterogeneous Triggers

heterogeneous triggers

Note

PXI Trigger Lines and RTSI Lines

| LabVIEW VI | C Function |
| --- | --- |
| niTClk Synchronize | niTClk_Synchronize |
| niTClk Initiate | niTClk_Initiate |
| niTClk Is Done (optional) or niTClk Wait Until Done VI | niTClk_IsDone (optional) or niTClk_WaitUntilDone |
| N/A | niTClk_GetExtendedErrorInfo |

To specify how the triggers must be shared between the devices, use the NI-TClk properties or
 attributes listed in the following table.

| LabVIEW Property | C Attribute |
| --- | --- |
| Start Trigger Master Session | NITCLK_ATTR_START_TRIGGER_MASTER_SESSION |
| Reference Trigger Master Session | NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION |
| Script Trigger Master Session | NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION |
| Pause Trigger Master Session | NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION |

If the Sample Clock rates, Sample Clock timebase rates, and/or the sample counts are different in
 different acquisition sessions sharing the Reference Trigger, set the holdoff attributes for
 the Reference Trigger master using the instrument driver.

Related concepts:

- Homogeneous and Heterogeneous Triggers
- PXI and RTSI Trigger Lines

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-synchronization-in-multiple-pxi-chass.html language=enus -->
## TOPIC 00020: Synchronization in Multiple PXI Chassis

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-synchronization-in-multiple-pxi-chass.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-synchronization-in-multiple-pxi-chass.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the devices are in multiple PXI chassis, the Sync Pulse signal is not automatically routed. Ensure that you configure the system such that the same clock source drives all the PXI_CLK10 signals in all the chassis. To minimize phase differences between the chassis, use matched-length cables to dri

### Synchronization in Multiple PXI
 Chassis

If the devices are in multiple PXI chassis, the *Sync Pulse* signal is not
 automatically routed. Ensure that you configure the system such that the same clock
 source drives all the PXI_CLK10 signals in all the chassis.

Note

#### Routing the Triggers

When you synchronize
 several NI modular instruments in multiple PXI chassis with *homogeneous or
 heterogeneous triggers*, use the instrument driver VIs or functions and
 the following TClk VIs or functions to route the triggers so that the triggers can
 be shared.

| LabVIEW VI | C Function |
| --- | --- |
| niTClk Synchronize VI | niTClk_Synchronize |
| niTClk Initiate VI | niTClk_Initiate |
| niTClk Is Done VI (optional) or niTClk Wait Until Done VI | niTClk_IsDone (optional) or niTClk_WaitUntilDone |
| N/A | niTClk_GetExtendedErrorInfo |

To specify how the triggers must be shared between the devices, use the
 NI-TClk properties or attributes listed in the following table.

| LabVIEW Property | C Attribute |
| --- | --- |
| Start Trigger Master Session | NITCLK_ATTR_START_TRIGGER_MASTER_SESSION |
| Reference Trigger Master Session | NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION |
| Script Trigger Master Session | NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION |
| Pause Trigger Master Session | NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION |

When the Sample Clock rates, Sample Clock timebase rates, and/or the sample
 counts are different in acquisition sessions sharing the Reference Trigger, you
 should also set the holdoff attributes for the Reference Trigger master using the
 instrument driver.

#### Routing the Sync Pulse Signal

To route the *Sync Pulse* signal
 in a multiple chassis system, use PXI synchronization modules, such as PXI-6653, in
 each chassis. Install these modules in the System Timing Slot to supply a common 10
 MHz clock signal to all the chassis.

To specify how to route the *Sync
 Pulse* signal, use the NI-TClk properties or attributes listed in the
 following table.

| LabVIEW Property | C Attribute |
| --- | --- |
| Sync Pulse Source | NITCLK_ATTR_SYNC_PULSE_SOURCE |
| Export Sync Pulse Output Terminal | NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL |

#### Example

If chassis A contains the device
 that exports the *Sync Pulse* signal, and chassis A is connected to
 chassis B and chassis C through the PXI synchronization modules and cables, then use
 the following signal routing.

1. Route the Sync Pulse signal from the device that exports this
 signal to the PXI synchronization module, using a PXI trigger line 
 (line X).
2. Resynchronize to PXI_CLK10 in the PXI synchronization module. Route the
 Sync Pulse signal to the following locations.
  - Another PXI trigger line (line Y) in the same chassis (where line Y is
 not the same PXI trigger line as line X).
  - The PXI synchronization modules in chassis B and chassis C.
3. Program the devices in chassis A to receive the signal from the PXI trigger line
 Y.
4. Route the Sync Pulse signal, without resynchronizing, from the PXI
 synchronization module on chassis B and chassis C to the PXI trigger line Y on
 chassis B and chassis C.
5. Program the devices in chassis B and chassis C to receive the Sync
 Pulse signal from the PXI trigger line Y.

If the PXI trigger line Y is not available in chassis B and chassis C, use any
 other available trigger line. Use the same trigger line in all the chassis to
 simplify programming.

Keep the total signal propagation delay to less than 100
 ns, for all the cables and the PXI synchronization modules.

Contact National
 Instruments technical support for more information about synchronizing multiple PXI
 chassis. Refer to *Configuring PXI Chassis with Multiple Bus Segments (18-Slot
 Chassis)* for more information about the 18-slot PXI
 chassis.

Related concepts:

- Sync Pulse and Sync Pulse Clock
- Homogeneous and Heterogeneous Triggers
- PXI and RTSI Trigger Lines
- Configuring PXI Chassis with Multiple Bus Segments (18-Slot Chassis)

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-synchronization-repeatability-optimiz.html language=enus -->
## TOPIC 00021: Synchronization Repeatability Optimization

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-synchronization-repeatability-optimiz.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-synchronization-repeatability-optimiz.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-TClk measures the time between the Sync Pulse Clock and the TClk using the niTClk Synchronize VI or the niTClk_Synchronize function. The imprecision associated with this measurement is usually very small, relative to the TClk timebase. NI-TClk adjusts the TClks and the TClk timebases on the devic

### Synchronization Repeatability
 Optimization

NI-TClk measures the time between the Sync Pulse Clock and the TClk using the niTClk
 Synchronize
 VI or the
 niTClk_Synchronize
 function. The imprecision associated with this measurement is usually very small,
 relative to the *TClk timebase*. NI-TClk adjusts the TClks and the TClk
 timebases on the devices, based on this measurement. Some devices adjust their TClk
 timebases with very fine resolution, usually using an oscillator phase DAC and a
 phase-locked loop (PLL).

These devices exhibit synchronization jitter from repeated calls to the niTClk Synchronize VI or
 the niTClk_Synchronize function. You can eliminate the jitter associated with TClk
 measurements for most devices, by setting the oscillator phase DAC value directly
 through the individual product drivers. The procedure for eliminating the jitter is
 listed in the following steps.

1. Configure the devices for acquisition or generation synchronized with the NI-TClk.
2. After acquiring or generating the signal, read the oscillator phase DAC attribute using the individual product drivers for each synchronized device.
3. Store the phase DAC attribute values.
4. Before running the program again, change the program to set the phase DAC attributes to the stored values using the individual product drivers for each synchronized device before calling the niTClk Synchronize VI or the niTClk_Synchronize function.

When you follow this procedure, NI-TClk adjusts TClks but not TClk timebases on the synchronized devices, and the synchronization jitter is minimized.

Related concepts:

- External Sample Clock and External Sample Clock Timebase Considerations

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-vi-programming-flow-1.html language=enus -->
## TOPIC 00022: VI Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-vi-programming-flow-1.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-vi-programming-flow-1.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Heterogeneous Trigger, Single Chassis or PC

### VI Programming Flow

#### Heterogeneous Trigger, Single Chassis or PC

[IMAGE alt='image' src='GUID-879E2A0C-9BF0-41C2-8F56-09C6B97A4186-a5.gif']

Parent topic:

Synchronization in a Single PXI Chassis or a Single PC with Heterogeneous Triggers

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-vi-programming-flow-3.html language=enus -->
## TOPIC 00023: VI Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-vi-programming-flow-3.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-vi-programming-flow-3.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multiple Chassis

### VI Programming Flow

#### Multiple Chassis

[IMAGE alt='image' src='GUID-ABF18F9B-7AAE-4BCC-9892-797EA76204C0-a5.gif']

Parent topic:

Synchronization in Multiple PXI Chassis

<!--NI_TOPIC bundle=ni-tclk path=ni-tclk-vi-programming-flow.html language=enus -->
## TOPIC 00024: VI Programming Flow

- bundle_id: `ni-tclk`
- source_path: `ni-tclk-vi-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/ni-tclk-vi-programming-flow.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Homogeneous Trigger, Single Chassis or PC

### VI Programming Flow

#### Homogeneous
 Trigger, Single Chassis or PC

[IMAGE alt='image' src='GUID-6466D637-5E60-4B29-9B97-3F709E3274C1-a5.gif']

Parent topic:

Synchronization in a Single PXI Chassis or a Single PC with Homogeneous Triggers

<!--NI_TOPIC bundle=ni-tclk path=related-documentation.html language=enus -->
## TOPIC 00025: Related Documentation

- bundle_id: `ni-tclk`
- source_path: `related-documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/related-documentation.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most National Instruments manuals also are available as PDFs. You must have Adobe Reader installed to view the PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to the National Instruments Product Manuals Library at ni.com/ma

### Related Documentation

Most National Instruments manuals also are available as PDFs. You must have Adobe Reader installed to view the PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to the National Instruments Product Manuals Library at ni.com/manuals for updated documentation resources.

The following documents contain information that you may find helpful as you use this help file. To access a document, navigate to ni.com/info and enter the document's Info Code:

| Document Title | Info Code |
| --- | --- |
| Synchronization Explained | ex7tdg |
| Synchronization Basics |  |

<!--NI_TOPIC bundle=ni-tclk path=user-manual-welcome.html language=enus -->
## TOPIC 00026: NI-TClk User Manual

- bundle_id: `ni-tclk`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-TClk User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-TClk
 User Manual

The NI-TClk User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ni-tclk path=using-the-standard-functionality-for-error-in.html language=enus -->
## TOPIC 00027: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-tclk`
- source_path: `using-the-standard-functionality-for-error-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/using-the-standard-functionality-for-error-in.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes, such as VIs, contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes, such as VIs, contain error in parameters you can use
 to manage errors. These parameters typically provide the same, standard functionality.
 When a node exhibits different parameter functionality, the exceptions are documented in
 the reference material for that node.

error in

Note

error in

error
 in

|  | The error in accepts error information wired from previously called VIs. Use this information to decide if any functionality must be bypassed in the event of errors from other VIs. Right-click the front panel error in control and select Explain Error or Explain Warning from the shortcut menu for more information about the error displayed. status is TRUE (X) if an error occurred before this node ran or during the running of this node, or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. code is the error or warning code. The default value is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |
| --- | --- |
|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node, or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
|  | code is the error or warning code. The default value is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-tclk path=using-the-standard-functionality-for-error-ou.html language=enus -->
## TOPIC 00028: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-tclk`
- source_path: `using-the-standard-functionality-for-error-ou.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk/raw/resource/enus/using-the-standard-functionality-for-error-ou.html
- document_id: `ni-tclk`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes, such as VIs, and functions contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that no

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes, such as VIs, and functions contain an error out
 parameter you can use to manage errors. These parameters typically provide the same,
 standard functionality. When a node exhibits different parameter functionality, the
 exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | The error out passes error or warning information out of a VI to be used by other VIs. Right-click the front panel error out indicator and select Explain Error or Explain Warning from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default value is FALSE. code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
| --- | --- |
|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default value is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
