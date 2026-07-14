# NI DOCUMENT BUNDLE: ni-tclk-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-tclk-c-api-ref start=1 end=32 -->
<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/functions_and_attributes.html language=enus -->
## TOPIC 00001: NI-TClk C Reference Help

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/functions_and_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/functions_and_attributes.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-TClk C Reference Help

September 2016, 374258B-01

The following table summarizes the functions and attributes that you can use with different chassis and PC configurations.

|  | PXI Chassis/PC Configuration |  |  |
| --- | --- | --- | --- |
| Single PXI Chassis/PC, Homogeneous Triggers | Single PXI Chassis/PC, Heterogeneous Triggers | Multiple PXI Chassis |  |
| Functions |  |  |  |
| niTClk_ConfigureForHomogeneousTriggers | Yes | — | — |
| niTClk_Synchronize | Yes | Yes | Yes |
| niTClk_Initiate | Yes | Yes | Yes |
| niTClk_IsDone | Yes | Yes | Yes |
| niTClk_WaitUntilDone | Yes | Yes | Yes |
| niTClk_GetExtendedErrorInfo | Yes | Yes | Yes |
| Attributes |  |  |  |
| NITCLK_ATTR_START_TRIGGER_MASTER_SESSION | — | T | T |
| NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION | — | T | T |
| NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION | — | T | T |
| NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION | — | T | T |
| NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION | — | T | T |
| NITCLK_ATTR_SYNC_PULSE_SOURCE | — | — | Yes |
| NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL | — | — | Yes |
| NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE | R | R | — |
| NITCLK_ATTR_SAMPLE_CLOCK_DELAY | Optional | Optional | Optional |
| R: Devices with RTSI trigger bus only. Use these when you want to control RTSI 7 directly, instead of through NI-TClk. T: Use attributes that pertain to the triggers that you are synchronizing. |  |  |  |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_advanced_functions.html language=enus -->
## TOPIC 00002: NI-TClk Advanced Function

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_advanced_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_advanced_functions.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-TClk Advanced Function

| Is Done | niTClk_IsDone |
| --- | --- |
| Setup For Sync Pulse Sender Synchronize | niTClk_SetupForSyncPulseSenderSynchronize |
| Synchronize To Sync Pulse Sender | niTClk_SynchronizeToSyncPulseSender |
| Finish Sync Pulse Sender Synchronize | niTClk_FinishSyncPulseSenderSynchronize |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_exported_sync_pulse_output_terminal.html language=enus -->
## TOPIC 00003: NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_exported_sync_pulse_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_exported_sync_pulse_output_terminal.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL

| Data Type: | ViString |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_Synchronize |
| Description: | Specifies the destination of the Sync Pulse signal. Use this attribute to synchronize a multichassis system. |
| Valid Values |  |
| PXI Devices: | "PXI_Trig0" through "PXI_Trig7" and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7" and device-specific settings |
| Examples of Device-specific Settings: | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1","PFI4", and "PFI5"NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_exported_tclk_output_terminal.html language=enus -->
## TOPIC 00004: NITCLK_ATTR_EXPORTED_TCLK_OUTPUT_TERMINAL

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_exported_tclk_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_exported_tclk_output_terminal.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_EXPORTED_TCLK_OUTPUT_TERMINAL

| Data Type: | ViString |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | None |
| Description: | Specifies the destination for the TClk signal of the device. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_pause_trigger_master_session.html language=enus -->
## TOPIC 00005: NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_pause_trigger_master_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_pause_trigger_master_session.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION

| Data Type: | ViSession |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Pause Trigger master session. For external triggers, the NI-TClk Pause Trigger Master Session is the session configured to receive an external trigger. For None (no trigger configured) or software triggers, the NI-TClk Pause Trigger Master Session is the session that generates the trigger. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_ref_trigger_master_session.html language=enus -->
## TOPIC 00006: NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_ref_trigger_master_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_ref_trigger_master_session.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION

| Data Type: | ViSession |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Reference Trigger master session. For external triggers, the NI-TClk Reference Trigger Master Session is the session configured to receive an external trigger. For None (no trigger configured) or software triggers, the NI-TClk Reference Trigger Master Session is the session that generates the trigger. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_sample_clock_delay.html language=enus -->
## TOPIC 00007: NITCLK_ATTR_SAMPLE_CLOCK_DELAY

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_sample_clock_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_sample_clock_delay.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SAMPLE_CLOCK_DELAY

| Data Type: | ViReal64 |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | None |
| Description: | Specifies the delay, in seconds, to apply to the session Sample Clock, relative to other synchronized sessions. During synchronization, NI-TClk aligns the Sample Clocks on the synchronized devices. If you want to delay the Sample Clocks, set this attribute before calling the niTClk_Synchronize function. |
| Default Value: | 0 |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_script_trigger_master_session.html language=enus -->
## TOPIC 00008: NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_script_trigger_master_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_script_trigger_master_session.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION

| Data Type: | ViSession |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Script Trigger master session. For external triggers, the NI-TClk Script Trigger Master Session is the session configured to receive an external trigger. For None (no trigger configured) or software triggers, the NI-TClk Script Trigger Master Session is the session that generates the trigger. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_sequencer_flag_master_session.html language=enus -->
## TOPIC 00009: NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_sequencer_flag_master_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_sequencer_flag_master_session.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION

| Data Type: | ViSession |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Sequencer Flag master session. For external triggers, the NI-TClk Sequencer Flag Master Session is the session configured to receive an external trigger. For None (no trigger configured) or software triggers, the NI-TClk Start Trigger Master Session is the session that generates the trigger. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_start_trigger_master_session.html language=enus -->
## TOPIC 00010: NITCLK_ATTR_START_TRIGGER_MASTER_SESSION

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_start_trigger_master_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_start_trigger_master_session.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_START_TRIGGER_MASTER_SESSION

| Data Type: | ViSession |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Start Trigger master session. For external triggers, the NI-TClk Start Trigger Master Session is the session configured to receive an external trigger. For None (no trigger configured) or software triggers, the NI-TClk Start Trigger Master Session is the session that generates the trigger. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_sync_pulse_clock_source.html language=enus -->
## TOPIC 00011: NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_sync_pulse_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_sync_pulse_clock_source.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE

| Data Type: | ViString |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_ConfigureForHomogeneousTriggers |
| Description: | Specifies the Sync Pulse Clock source. Use this attribute when you are synchronizing PCI devices and want to control RTSI 7 yourself. Ensure that a 10 MHz clock is driven onto the RTSI 7. |
| Valid Values |  |
| PXI Devices: | "PXI_CLK10" "None" |
| PCI Devices: | "RTSI_7" "None" |
| Default Value: | "None". "None" directs the niTClk_Synchronize function to create the necessary routes. For PCI, one of the synchronized devices drives a 10 MHz clock on the RTSI 7, unless RTSI 7 is already driven. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_sync_pulse_sender_sync_pulse_source.html language=enus -->
## TOPIC 00012: NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_sync_pulse_sender_sync_pulse_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_sync_pulse_sender_sync_pulse_source.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE

| Data Type: | ViString |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | None |
| Description: | Specifies the external sync pulse source of the Sync Pulse Sender. You can use this source to synchronize the Sync Pulse Sender with an external non-TCLK event. |
| Valid Values |  |
| PXI Devices: | "PXI_Trig0" through "PXI_Trig7" and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7" and device-specific settings |
| Examples of Device-specific Settings: | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI4", and "PFI5" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_sync_pulse_source.html language=enus -->
## TOPIC 00013: NITCLK_ATTR_SYNC_PULSE_SOURCE

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_sync_pulse_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_sync_pulse_source.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_SYNC_PULSE_SOURCE

| Data Type: | ViString |
| --- | --- |
| Access: | Read/Write |
| Coercion: | None |
| High-level Functions: | niTClk_Synchronize |
| Description: | Specifies the Sync Pulse source. Use this attribute to synchronize a multichassis system. |
| Valid Values |  |
| PXI Devices: | "PXI_Trig0" through "PXI_Trig7" and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7" and device-specific settings |
| Examples of Device-specific Settings: | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI2", and "PFI3" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string directs niTClk_Synchronize to set this attribute when all the synchronized devices are in one PXI chassis. To synchronize a multichassis system, you must set this attribute before calling the niTClk_Synchronize function. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_attr_tclk_actual_period.html language=enus -->
## TOPIC 00014: NITCLK_ATTR_TCLK_ACTUAL_PERIOD

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_attr_tclk_actual_period.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_attr_tclk_actual_period.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NITCLK_ATTR_TCLK_ACTUAL_PERIOD

| Data Type: | ViReal64 |
| --- | --- |
| Access: | Read Only |
| Coercion: | None |
| High-level Functions: | None |
| Description: | Returns the computed TClk period. |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_basic_functions.html language=enus -->
## TOPIC 00015: NI-TClk High-Level Functions

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_basic_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_basic_functions.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-TClk High-Level Functions

| Configure For Homogeneous Triggers | niTClk_ConfigureForHomogeneousTriggers |
| --- | --- |
| Synchronize | niTClk_Synchronize |
| Initiate | niTClk_Initiate |
| Wait Until Done | niTClk_WaitUntilDone |
| Get Extended Error Info | niTClk_GetExtendedErrorInfo |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_configureforhomogeneoustriggers.html language=enus -->
## TOPIC 00016: niTClk_ConfigureForHomogeneousTriggers

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_configureforhomogeneoustriggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_configureforhomogeneoustriggers.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_ConfigureForHomogeneousTriggers

ViStatus niTClk_ConfigureForHomogeneousTriggers (ViUInt32 sessionCount, ViSession sessions []);

#### Purpose

Configures the attributes commonly required for the TClk synchronization of device sessions with [homogeneous triggers](/csh?topicname=nitclk/heterogeneous_triggers.html) in a [single PXI chassis or a single PC](/csh?topicname=nitclk/sync_single_chassis_homogeneous_trig.html).

Use the niTClk_ConfigureForHomogeneousTriggers function to configure attributes for the Reference Clocks, Start Triggers, Reference Triggers, Script Triggers, and Pause Triggers.

If the niTClk_ConfigureForHomogeneousTriggers function cannot perform all the steps required for the given sessions, it returns an error. If the niTClk_ConfigureForHomogeneousTriggers function returns an error, use the instrument driver functions and attributes, along with the following NI-TClk attributes, for signal routing.

- NITCLK_ATTR_START_TRIGGER_MASTER_SESSION
- NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION
- NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION
- NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION

The niTClk_ConfigureForHomogeneousTriggers function affects the following clocks and triggers:

##### [IMAGE alt='image' src='arrow_close.gif'] Reference Clocks

The niTClk_ConfigureForHomogeneousTriggers function configures the reference clocks if they are needed. Specifically, if you use the internal sample clocks or internal Sample Clock timebases, and the Reference Clock Source is either not configured—or set to None (no trigger configured), the niTClk_ConfigureForHomogeneousTriggers function configures the following:

- PXI —The Reference Clock source on all devices is set to be the 10 MHz PXI backplane clock (PXI_CLK10).
- PCI —One of the devices exports its 10 MHz onboard Reference Clock to RTSI 7. The Reference Clock source on all devices is set to be RTSI 7.

|  | Note If the Reference Clock source is set to a value other than None, the niTClk_ConfigureForHomogeneousTriggers function cannot configure the Reference Clock source. |
| --- | --- |

##### [IMAGE alt='image' src='arrow_close.gif'] Start Triggers

If the Start Trigger is set to None (no trigger configured) for all sessions, the sessions are configured to share the Start Trigger. The Start Trigger is shared by:

- Implicitly exporting the Start Trigger from one session
- Configuring the other sessions for digital-edge Start Triggers with sources corresponding to the exported Start Trigger
- Setting the NITCLK_ATTR_START_TRIGGER_MASTER_SESSION attribute to the session that is exporting the trigger for all sessions

If the Start Triggers are None for all except one session, the niTClk_ConfigureForHomogeneousTriggers function configures the sessions to share the Start Trigger from the one excepted session. The Start Trigger is shared by:

- Implicitly exporting the Start Trigger from the session in which the Start Trigger is not set to None
- Configuring the other sessions for digital-edge Start Triggers with sources corresponding to the exported Start Trigger
- Setting the NITCLK_ATTR_START_TRIGGER_MASTER_SESSION attribute to the session that is exporting the trigger for all sessions

If the Start Triggers are configured for all sessions, the niTClk_ConfigureForHomogeneousTriggers function does not affect the Start Triggers. Start Triggers are considered to be configured for all sessions if one of the following conditions is true:

- No session has a Start Trigger set to None
- One session has a Start Trigger set to None, and all other sessions have Start Triggers other than None. For the session in which the Start Trigger is set to None, the NITCLK_ATTR_START_TRIGGER_MASTER_SESSION attribute must be set to this session, which indicates that the session itself is the Start Trigger master

##### [IMAGE alt='image' src='arrow_close.gif'] Reference Triggers

For sessions that support Reference Triggers, if the Reference Triggers are set to None (no trigger configured) for all except one session, the niTClk_ConfigureForHomogeneousTriggers function configures sessions to share the Reference Triggers. The Reference Triggers are shared by:

- Implicitly exporting the Reference Trigger from the session in which the Reference Trigger is not set to None
- Configuring the other sessions that support the Reference Trigger for digital-edge Reference Triggers with sources corresponding to the exported Reference Trigger
- Setting the NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION attribute to the session that is exporting the trigger for all sessions that support Reference Trigger

If the Reference Triggers are configured for all sessions that support Reference Triggers, the niTClk_ConfigureForHomogeneousTriggers function does not affect the Reference Triggers. Reference Triggers are configured for all sessions if one of the following conditions is true:

- No session has a Reference Trigger set to None
- One session has a Reference Trigger set to None, and all other sessions have Reference Triggers other than None. The session with the None trigger must have the NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION attribute set to itself, indicating that the session itself is the Reference Trigger master

###### Reference Trigger Holdoffs

Acquisition sessions may be configured with the Reference Trigger. For acquisition sessions, when the Reference Trigger is shared, niTClk_ConfigureForHomogeneousTriggers configures the holdoff attributes (which are instrument driver specific) on the Reference Trigger master session so that the session does not recognize the Reference Trigger before the other sessions are ready. This condition is only relevant when the Sample Clock rates, Sample Clock timebase rates, sample counts, holdoffs, and/or any delays for the acquisitions are different.

When the Sample Clock rates, Sample Clock timebase rates, and/or the sample counts are different in acquisition sessions sharing the Reference Trigger, you must also set the holdoff attributes for the Reference Trigger master, using the instrument driver.

##### [IMAGE alt='image' src='arrow_close.gif'] Script Triggers

For sessions that support Script Triggers, if the Script Triggers are set to None (no trigger configured) for all except one session, the niTClk_ConfigureForHomogeneousTriggers function configures sessions to share the Script Triggers. The Script Triggers are shared by:

- Implicitly exporting the Script Trigger from the session in which the Script Trigger is not set to None
- Configuring the other sessions that support the Script Trigger for digital-edge Script Triggers with sources corresponding to the exported Script Trigger
- Setting the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute to the session that is exporting the trigger for all sessions that support Script Triggers

If the Script Triggers are configured for all sessions that support Script Triggers, niTClk_ConfigureForHomogeneousTriggers does not affect Script Triggers. Script Triggers are configured for all sessions if one of the following conditions is true:

- No session has a Script Trigger set to None
- One session has a Script Trigger set to None and all other sessions have Script Triggers other than None. The session with the None trigger must have the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute set to itself, indicating that the session itself is the Script Trigger master

##### [IMAGE alt='image' src='arrow_close.gif'] Pause Triggers

For sessions that support Pause Triggers, if the Pause Triggers are set to None (no trigger configured) for all except one session, the niTClk_ConfigureForHomogeneousTriggers function configures sessions to share the Pause Triggers. The Pause Triggers are shared by:

- Implicitly exporting the Pause Trigger from the session in which the Pause Trigger is not set to None
- Configuring the other sessions that support the Pause Trigger for digital-edge Pause Triggers with sources corresponding to the exported Pause Trigger
- Setting the NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION attribute to the session that is exporting the trigger for all sessions that support Script Triggers

If the Pause Triggers are configured for all generation sessions that support Pause Triggers, niTClk_ConfigureForHomogeneousTriggers does not affect Pause Triggers. Pause Triggers are configured for all sessions if one of the following conditions is true:

- No session has a Pause Trigger set to None
- One session has a Pause Trigger set to None and all other sessions have Pause Triggers other than None. The session with the trigger set to None must have the NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION attribute set to itself, which indicates that the session itself is the Pause Trigger master

|  | Note TClk synchronization is not supported for Pause Triggers on acquisition sessions. |
| --- | --- |

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_finishsyncpulsesendersynchronize.html language=enus -->
## TOPIC 00017: niTClk_FinishSyncPulseSenderSynchronize

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_finishsyncpulsesendersynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_finishsyncpulsesendersynchronize.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_FinishSyncPulseSenderSynchronize

#### C Function Prototype

ViStatus _VI_FUNC niTClk_FinishSyncPulseSenderSynchronize (ViUInt32 sessionCount,
 ViSession sessions[],
 ViReal64 minTime);

#### Purpose

Finishes synchronizing the Sync Pulse Sender.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| minTime | ViReal64 | Specifies the minimum TClk period, in seconds. Valid values are 0.0 to 0.050 s (50 ms), inclusive. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_get_attribute_functions.html language=enus -->
## TOPIC 00018: NI-TClk Get Attribute Functions

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_get_attribute_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_get_attribute_functions.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-TClk Get Attribute Functions

| Get Attribute ViReal64 | niTClk_GetAttributeViReal64 |
| --- | --- |
| Get Attribute ViSession | niTClk_GetAttributeViSession |
| Get Attribute ViString | niTClk_GetAttributeViString |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_getattributevireal64.html language=enus -->
## TOPIC 00019: niTClk_GetAttributeViReal64

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_getattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_getattributevireal64.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_GetAttributeViReal64

ViStatus niTClk_GetAttributeViReal64 (ViSession session, ViConstString channelName, ViAttr attributeId, ViReal64 *value);

#### Purpose

Queries the value of an NI-TClk ViReal64 attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | ViSession [] | Specifies the sessions that are being synchronized. |
| channelName | ViConstString | Pass VI_NULL or an empty string. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to query. Supported Attribute NITCLK_ATTR_SAMPLE_CLOCK_DELAY |
| Output |  |  |
| value | ViReal64 | Returns the value of the attribute. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_getattributevisession.html language=enus -->
## TOPIC 00020: niTClk_GetAttributeViSession

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_getattributevisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_getattributevisession.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_GetAttributeViSession

ViStatus niTClk_GetAttributeViSession (ViSession session, ViConstString channelName, ViAttr attributeId, ViSession *value);

#### Purpose

Queries the value of an NI-TClk ViSession attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | ViSession [] | Specifies the sessions that are being synchronized. |
| channelName | ViConstString | Pass VI_NULL or an empty string, except for the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute. For this attribute, you must specify scriptTrigger0, scriptTrigger1, scriptTrigger2, or scriptTrigger3 in the channelName parameter. VI_NULL and the empty string are treated as scriptTrigger0 for the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to query. Supported Attributes NITCLK_ATTR_START_TRIGGER_MASTER_SESSION NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION |
| Output |  |  |
| value | ViSession | Returns the value of the attribute. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_getattributevistring.html language=enus -->
## TOPIC 00021: niTClk_GetAttributeViString

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_getattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_getattributevistring.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_GetAttributeViString

ViStatus niTClk_GetAttributeViString (ViSession session, ViConstString channelName, ViAttr attributeId, ViInt32 bufSize, ViChar value []);

#### Purpose

Queries the value of an NI-TClk ViString attribute.

You must provide a ViChar array to serve as a buffer for the value. Pass the number of bytes in the buffer to the function using the **bufSize** parameter. 
 
If the current value of the attribute, including the terminating NULL byte, is larger than the size that you specify using the **bufSize** parameter, the function copies **bufSize** minus 1 bytes into the buffer. The function then places an ASCII NULL byte at the end of the buffer, and returns the array size that you must pass to get the entire value. 
 
For example, if the value is "123456" and the value that you specify in the **bufSize** parameter is 4, the function places "123" into the buffer and returns 7.

If you want to call the niTClk_GetAttributeViString function only to get the required array size, specify 0 in the **bufSize** parameter and VI_NULL in the **value** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | ViSession [] | Specifies the sessions that are being synchronized. |
| channelName | ViConstString | Pass VI_NULL or an empty string. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to query. Supported Attributes NITCLK_ATTR_SYNC_PULSE_SOURCE NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL |
| bufSize | ViInt32 | The number of bytes in the ViChar array that you specify for the value parameter. |
| Output |  |  |
| value | ViChar [] | Returns the value for the attribute. |

#### [Return Value](return_value.html)

If you pass NULL for the value or 0 for the buffer size, or if the size of value prevents the function from reporting the entire value, this function returns the number of characters needed to report the value.

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_getextendederrorinfo.html language=enus -->
## TOPIC 00022: niTClk_GetExtendedErrorInfo

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_getextendederrorinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_getextendederrorinfo.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_GetExtendedErrorInfo

#### Specific Function

ViStatus niTClk_GetExtendedErrorInfo (ViChar errorString [], ViUInt32 errorStringSize);

#### Purpose

Reports extended error information for the most recent NI-TClk function that returned an error.

To determine the function that returned an error, use the return values of the individual functions. After the niTClk_GetExtendedErrorInfo function reports an **errorString**, this function does not report an empty string again.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| errorString | ViChar [] | Extended error description. If errorString is NULL, then the string is not large enough to hold the entire error description. In this case, niTClk_GetExtendedErrorInfo returns the size of the full error string, which can be used with niTClk_GetExtendedErrorInfo to retrieve the full error string. |
| errorStringSize | ViUInt32 | Size of errorString. If errorStringSize is 0, then it is not large enough to hold the entire error description. In this case, niTClk_GetExtendedErrorInfo returns the size of the full error string, which can be used with niTClk_GetExtendedErrorInfo to retrieve the full error string. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_initiate.html language=enus -->
## TOPIC 00023: niTClk_Initiate

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_initiate.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_Initiate

#### Specific Function

ViStatus niTClk_Initiate (ViUInt32 sessionCount, ViSession sessions []);

#### Purpose

Initiates the acquisition and/or generation sessions that you specify. This function also processes any special requirements that are needed for the synchronization.

For example, the session that exports the TClk-synchronized Start Trigger is not initiated until after the niTClk_Initiate function initiates all the sessions that import the TClk-synchronized Start Trigger.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_isdone.html language=enus -->
## TOPIC 00024: niTClk_IsDone

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_isdone.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_isdone.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_IsDone

#### Specific Function

ViStatus niTClk_IsDone (ViUInt32 sessionCount, ViSession sessions [], ViBoolean *done);

#### Purpose

Reports the progress of the acquisitions and/or generations, corresponding to the sessions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| Output |  |  |
| done | ViBoolean* | Indicates whether the operation is done. The operation is done when each session has completed without any errors, or when any one of the sessions reports an error. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_set_attribute_functions.html language=enus -->
## TOPIC 00025: NI-TClk Set Attribute Functions

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_set_attribute_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_set_attribute_functions.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-TClk Set Attribute Functions

| Set Attribute ViReal64 | niTClk_SetAttributeViReal64 |
| --- | --- |
| Set Attribute ViSession | niTClk_SetAttributeViSession |
| Set Attribute ViString | niTClk_SetAttributeViString |

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_setattributevireal64.html language=enus -->
## TOPIC 00026: niTClk_SetAttributeViReal64

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_setattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_setattributevireal64.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_SetAttributeViReal64

ViStatus niTClk_SetAttributeViReal64 (ViSession session, ViConstString channelName, ViAttr attributeId, ViReal64 value);

#### Purpose

Sets the value of an NI-TClk VIReal64 attribute.

niTClk_SetAttributeViReal64 is a low-level function that you can use to set the values of NI-TClk attributes.

NI-TClk contains high-level functions that set most of the attributes. NI recommends using the high-level functions as much as possible.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| session | ViSession | Specifies the sessions that are being synchronized. |
| channelName | ViConstString | Pass VI_NULL or an empty string. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to set. Supported Attribute NITCLK_ATTR_SAMPLE_CLOCK_DELAY |
| value | ViReal64 | Specifies the value of the attribute. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_setattributevisession.html language=enus -->
## TOPIC 00027: niTClk_SetAttributeViSession

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_setattributevisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_setattributevisession.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_SetAttributeViSession

ViStatus niTClk_SetAttributeViSession (ViSession session, ViConstString channelName, ViAttr attributeId, ViSession value);

#### Purpose

Sets the value of an NI-TClk ViSession attribute.

niTClk_SetAttributeViSession is a low-level function that you can use to set the values of NI-TClk attributes.

NI-TClk contains high-level functions that set most of the attributes. NI recommends using the high-level functions as much as possible.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| session | ViSession | Specifies the references that are being synchronized. |
| channelName | ViConstString | Pass VI_NULL or an empty string, except for the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute. For this attribute, you must specify scriptTrigger0, scriptTrigger1, scriptTrigger2, or scriptTrigger3 in the channelName parameter. VI_NULL and the empty string are treated as scriptTrigger0 for the NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION attribute. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to set. Supported Attributes NITCLK_ATTR_START_TRIGGER_MASTER_SESSION NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION |
| value | ViSession | Specifies the value of the attribute. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_setattributevistring.html language=enus -->
## TOPIC 00028: niTClk_SetAttributeViString

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_setattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_setattributevistring.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_SetAttributeViString

ViStatus niTClk_SetAttributeViString (ViSession session, ViConstString channelName, ViAttr attributeId, ViConstString value);

#### Purpose

Sets the value of an NI-TClk ViString attribute.

niTClk_SetAttributeViString is a low-level function that you can use to set the values of NI-TClk attributes.

NI-TClk contains high-level functions that set most of the attributes. NI recommends using the high-level functions as much as possible.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| session | ViSession | Specifies the sessions that are being synchronized. |
| channelName | ViConstString | Specifies VI_NULL or an empty string. |
| attributeId | ViAttr | Specifies the ID of the attribute that you want to set. Supported Attributes NITCLK_ATTR_SYNC_PULSE_SOURCE NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL |
| value | ViConstString | Specifies the value of the attribute. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_setupforsyncpulsesendersynchronize.html language=enus -->
## TOPIC 00029: niTClk_SetupForSyncPulseSenderSynchronize

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_setupforsyncpulsesendersynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_setupforsyncpulsesendersynchronize.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_SetupForSyncPulseSenderSynchronize

ViStatus _VI_FUNC niTClk_SetupForSyncPulseSenderSynchronize (ViUInt32 sessionCount,
 ViSession sessions[],
 ViReal64 minTime);

#### Purpose

Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| minTime | ViReal64 | Specifies the minimum TClk period, in seconds. Valid values are 0.0 to 0.050 s (50 ms), inclusive. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_synchronize.html language=enus -->
## TOPIC 00030: niTClk_Synchronize

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_synchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_synchronize.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_Synchronize

ViStatus niTClk_Synchronize (ViUInt32 sessionCount, ViSession sessions [], ViReal64 minTime);

#### Purpose

Synchronizes the [TClk signals](/csh?topicname=nitclk/nitclk_overview.html) on the given sessions. After the niTClk_Synchronize function executes, the TClk signals from all the sessions are synchronized.

|  | Note Before using the niTClk_Synchronize function, verify that your system is configured, as described in the PXI Trigger Lines and RTSI Lines topic. |
| --- | --- |

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| minTime | ViReal64 | Specifies the minimum TClk period, in seconds. Valid values are 0.0 s to 0.050 s (50 ms), inclusive. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_synchronizetosyncpulsesender.html language=enus -->
## TOPIC 00031: niTClk_SynchronizeToSyncPulseSender

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_synchronizetosyncpulsesender.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_synchronizetosyncpulsesender.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_SynchronizeToSyncPulseSender

ViStatus _VI_FUNC niTClk_SynchronizeToSyncPulseSender (ViUInt32 sessionCount,
 ViSession sessions[],
 ViReal64 minTime);

#### Purpose

Synchronizes the other devices to the Sync Pulse Sender.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions[] | ViSession | Specifies an array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| minTime | ViReal64 | Specifies the minimum TClk period, in seconds. Valid values are 0.0 to 0.050 s (50 ms), inclusive. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. |

#### [Return Value](return_value.html)

<!--NI_TOPIC bundle=ni-tclk-c-api-ref path=nitclkcvi/nitclk_waituntildone.html language=enus -->
## TOPIC 00032: niTClk_WaitUntilDone

- bundle_id: `ni-tclk-c-api-ref`
- source_path: `nitclkcvi/nitclk_waituntildone.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-c-api-ref/raw/resource/enus/nitclkcvi/nitclk_waituntildone.html
- document_id: `ni-tclk-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niTClk_WaitUntilDone

ViStatus niTClk_WaitUntilDone (ViUInt32 sessionCount, ViSession sessions [], ViReal64 timeout);

#### Purpose

Waits until the acquisitions and/or generations corresponding to the sessions are done, or until the function returns a timeout error.

niTClk_WaitUntilDone is a blocking function that periodically checks the operation status. This function returns control to the calling program, if the operation completes successfully, or if an error occurs (including a timeout error).

This function is most useful for finite data operations that you want to complete within a certain time.

#### Parameters

| Input |
| --- |

| Name | Type | Description |
| --- | --- | --- |
| sessionCount | ViUInt32 | Specifies the number of elements in the sessions array. |
| sessions | ViSession [] | Specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference function, where <driver name> is the name of the instrument driver. Example: niScope_GetSessionReference. |
| timeout | ViReal64 | Specifies the amount of time, in seconds, that the niTClk_WaitUntilDone function waits, for the sessions to complete. If the timeout parameter is exceeded, the niTClk_WaitUntilDone function returns an error. |

#### [Return Value](return_value.html)
