# NI DOCUMENT BUNDLE: ni-tclk-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-tclk-labview-api-ref start=1 end=27 -->
<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/advanced-mnu.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/advanced-mnu.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced VIs and functions to access advanced and miscellaneous features of NI-TClk. icon

### Advanced

Use the Advanced VIs and functions to access advanced and miscellaneous features of NI-TClk.

[IMAGE alt='icon' src='advanced-mnu.png']

- [niTClk Is Done VI](../../instr-lib/nitclk/nitclk-llb/nitclk-is-done-vi.html) Reports the progress of the acquisitions and/or generations, corresponding to sessions.
- [niTClk Setup For Sync Pulse Sender Synchronize VI](../../instr-lib/nitclk/nitclk-llb/nitclk-setup-for-sync-pulse-sender-synchronize-vi.html) Configures the TClks on all devices and prepares the Sync Pulse Sender for synchronization.
- [niTClk Synchronize To Sync Pulse Sender VI](../../instr-lib/nitclk/nitclk-llb/nitclk-synchronize-to-sync-pulse-sender-vi.html) Synchronizes the other devices to the Sync Pulse Sender.
- [niTClk Finish Sync Pulse Sender Synchronize VI](../../instr-lib/nitclk/nitclk-llb/nitclk-finish-sync-pulse-sender-synchronize-vi.html) Synchronizes the Sync Pulse Senders. After this VI executes, TClk signals for all Sync Pulse Senders are synchronized.
- [niTClk Property Node VI](../../instr-lib/nitclk/nitclk-llb/nitclk-property-node-vi.html) A LabVIEW Property Node with the NI-TClk class preselected. Gets (reads) and/or sets (writes) properties of a session reference.

Parent topic:

NI-TClk Synchronization

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/dir-mnu.html language=enus -->
## TOPIC 00002: NI-TClk Synchronization

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/dir-mnu.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: August 2016, 372532G-01 Use the NI-TClk VIs to configure, initiate, and synchronize multiple devices. © 2003 – 2013 National Instruments. All rights reserved. icon

### NI-TClk Synchronization

August 2016, 372532G-01

Use the NI-TClk VIs to configure, initiate, and synchronize multiple devices.

© 2003 – 2013 National Instruments. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [niTClk Configure For Homogeneous Triggers VI](../../instr-lib/nitclk/nitclk-llb/nitclk-configure-for-homogeneous-triggers-vi.html) Configures the properties commonly required for the TClk synchronization of device sessions with homogeneous triggers in a single PXI chassis or a single PC .
- [niTClk Synchronize VI](../../instr-lib/nitclk/nitclk-llb/nitclk-synchronize-vi.html) Synchronizes the TClk signals on the given sessions. After the niTClk Synchronize VI executes, the TClk signals from all the sessions are synchronized.
- [niTClk Initiate VI](../../instr-lib/nitclk/nitclk-llb/nitclk-initiate-vi.html) Initiates the acquisition and/or generation sessions that you specify. This VI also processes any special requirements that are needed for the synchronization.
- [niTClk Wait Until Done VI](../../instr-lib/nitclk/nitclk-llb/nitclk-wait-until-done-vi.html) Waits until the acquisitions and/or generations corresponding to sessions are done, or until the VI returns a timeout error.
- [Advanced](../../instr-lib/nitclk/advanced-mnu.html) Use the Advanced VIs and functions to access advanced and miscellaneous features of NI-TClk.

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-configure-for-homogeneous-triggers-vi.html language=enus -->
## TOPIC 00003: niTClk Configure For Homogeneous Triggers VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-configure-for-homogeneous-triggers-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-configure-for-homogeneous-triggers-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties commonly required for the TClk synchronization of device sessions with homogeneous triggers in a single PXI chassis or a single PC. Use the niTClk Configure For Homogeneous Triggers VI to configure properties for the Reference Clocks, Start Triggers, Reference Triggers, Scr

### niTClk Configure For Homogeneous Triggers VI

Configures the properties commonly required for the TClk synchronization of device sessions with [homogeneous triggers](/csh?context=nitclk_nitclk_heterogeneous_triggers) in a [single PXI chassis or a single PC](/csh?context=nitclk_nitclk_sync_single_chassis_homogeneous_trig).

Use the niTClk Configure For Homogeneous Triggers VI to configure properties for the **Reference Clocks**, **Start Triggers**, **Reference Triggers**, **Script Triggers**, and **Pause Triggers**.

If the niTClk Configure For Homogeneous Triggers VI cannot perform all the steps required for the given sessions, it returns an error. If the niTClk Configure For Homogeneous Triggers VI returns an error, use the instrument driver VIs and properties, along with the following NI-TClk properties, for signal routing.

- Start Trigger Master Session
- Reference Trigger Master Session
- Script Trigger Master Session
- Pause Trigger Master Session

[IMAGE alt='icon' src='nitclk-configure-for-homogeneous-triggers-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Configure For Homogeneous Triggers Details**

**Reference Clocks**

The niTClk Configure For Homogeneous Triggers VI configures the Reference Clocks if they are needed. Specifically, if you use the internal Sample Clocks or internal Sample Clock timebases, and the Reference Clock Source is either not configured or is set to None (no trigger configured), the niTClk Configure For Homogeneous Triggers VI configures the following:

- PXI— The Reference Clock Source on all devices is set to be the 10 MHz PXI backplane clock (PXI_CLK10).
- PCI— One of the devices exports its 10 MHz onboard Reference Clock to RTSI 7. The Reference Clock Source on all devices is set to be RTSI 7.

Note

None

**Start Triggers**

If the Start Trigger is set to None (no trigger configured) for all sessions, the sessions are configured to share the Start Trigger. The VI performs the following actions to share the Start Trigger:

- Implicitly exports the Start Trigger from one session
- Configures the other sessions for digital edge Start Triggers with sources corresponding to the exported Start Trigger
- Sets the Start Trigger Master Session property to the session that is exporting the trigger for all sessions

If the Start Triggers are set to None for all except one session, the niTClk Configure For Homogeneous Triggers VI configures the sessions to share the Start Trigger from the one excepted session. The VI performs the following actions to share the Start Trigger:

- Implicitly exports the Start Trigger from the session in which the Start Trigger is not set to None
- Configures the other sessions for digital edge Start Triggers with sources corresponding to the exported Start Trigger
- Sets the Start Trigger Master Session property to the session that is exporting the trigger for all sessions

If the Start Triggers are configured for all sessions, the niTClk Configure For Homogeneous Triggers VI does not affect the Start Triggers. Start Triggers are configured for all sessions if either of the following conditions is true:

- No session has a Start Trigger set to None
- One session has a Start Trigger set to None , and all other sessions have Start Triggers other than None . For the session in which the Start Trigger is set to None, the Start Trigger Master Session property must be set to this session, indicating that the session itself is the Start Trigger master

**Reference Triggers**

For sessions that support Reference Triggers, if the Reference Triggers are set to None (no trigger configured) for all except one session, the niTClk Configure For Homogeneous Triggers VI configures these sessions to share the Reference Triggers sessions. The VI performs the following actions to share the Reference Triggers:

- Implicitly exports the Reference Trigger from the session in which the Reference Trigger is not set to None
- Configures the other sessions that support the Reference Trigger for digital-edge Reference Triggers with sources corresponding to the exported Reference Trigger
- Sets the Reference Trigger Master Session property to the session that is exporting the trigger for all sessions that support the Reference Triggers.

Calling the niTClk Configure For Homogeneous Triggers VI will not affect the Reference Triggers if either of the following conditions is true:

- No session has a Reference Trigger set to None
- One session has a Reference Trigger set to None , and all other sessions have Reference Triggers other than None . For the session in which the Reference Trigger is set to None, the Reference Trigger Master Session property must be set to this session, indicating that the session itself is the Reference Trigger master

**Reference Trigger Holdoffs**

For acquisition sessions, the niTClk Configure For Homogeneous Triggers VI configures the holdoff attributes, which are instrument driver specific, on the Reference Trigger master session so that the session does not recognize the Reference Trigger before the other sessions are ready. This condition is only relevant when the Sample Clock rates, Sample Clock timebase rates, sample counts, holdoffs, and/or any delays for the acquisitions are different.

**Script Triggers 0, 1, 2, and 3**

Note

For sessions that support Script Triggers, if the Script Triggers are set to None (no trigger configured) for all except one session, the niTClk Configure For Homogeneous Triggers VI configures these sessions to share the Script Triggers. The VI performs the following actions to share the Script Triggers.

- Implicitly exports the Script Trigger from the session with the Script Trigger that is not set to None .
- Configures the other sessions that support the Script Trigger for digital-edge Script Triggers with sources corresponding to the exported Script Trigger
- Sets the Script Trigger Master Session property to the session that is exporting the trigger for all sessions that support Script Triggers

If the Script Triggers are configured for all sessions that support Script Triggers, the niTClk Configure For Homogeneous Triggers VI does not affect Script Triggers. Script Triggers are configured for all sessions if either of the following conditions is true:

- No session has a Script Trigger set to None
- One session has a Script Trigger set to None and all other sessions have Script Triggers other than None . The session with the None trigger must have the Script Trigger Master Session property set to itself, indicating that the session itself is the Script Trigger master

**Pause Triggers**

For sessions that support Pause Triggers, if the Pause Triggers are set to None (no trigger configured) for all except one session, the niTClk Configure For Homogeneous Triggers VI configures the generation sessions to share the Pause Triggers. The VI performs the following actions to share the Pause Triggers:

- Implicitly exports the Pause Trigger from the session with the Pause Trigger that is not set to None
- Configures the other sessions that support the Pause Trigger for digital-edge Pause Triggers with sources corresponding to the exported Pause Trigger
- Sets the Pause Trigger Master Session property to the session that is exporting the trigger for all sessions that support Pause Triggers

If the Pause Triggers are configured for all generation sessions that support Pause Triggers, the niTClk Configure For Homogeneous Triggers VI does not affect Pause Triggers. Pause Triggers are configured for all sessions if either of the following conditions is true:

- No session has a Pause Trigger set to None
- One session has a Pause Trigger set to None and all other sessions have Pause Triggers other than None . The session with the None trigger must have the Pause Trigger Master Session property set to itself, indicating that the session itself is the Pause Trigger master

Note

Parent topic:

NI-TClk Synchronization

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-finish-sync-pulse-sender-synchronize-vi.html language=enus -->
## TOPIC 00004: niTClk Finish Sync Pulse Sender Synchronize VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-finish-sync-pulse-sender-synchronize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-finish-sync-pulse-sender-synchronize-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the Sync Pulse Senders. After this VI executes, TClk signals for all Sync Pulse Senders are synchronized. icon Inputs/Outputs c1dgenclassrn.png sessions sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver b

### niTClk Finish Sync Pulse Sender Synchronize VI

Synchronizes the Sync Pulse Senders. After this VI executes, TClk signals for all Sync Pulse Senders are synchronized.

[IMAGE alt='icon' src='nitclk-finish-sync-pulse-sender-synchronize-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. minimum T clock period — minimum T clock period specifies the minimum TClk period, in seconds. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. Valid values are 0.0 s to 0.050 s (50 ms), inclusive. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-initiate-vi.html language=enus -->
## TOPIC 00005: niTClk Initiate VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-initiate-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates the acquisition and/or generation sessions that you specify. This VI also processes any special requirements that are needed for the synchronization. For example, the session that exports the TClk-synchronized Start Trigger is not initiated until after the niTClk Initiate VI initiates all

### niTClk Initiate VI

Initiates the acquisition and/or generation sessions that you specify. This VI also processes any special requirements that are needed for the synchronization.

For example, the session that exports the TClk-synchronized Start Trigger is not initiated until after the niTClk Initiate VI initiates all the sessions that import the TClk-synchronized Start Trigger.

[IMAGE alt='icon' src='nitclk-initiate-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-TClk Synchronization

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-is-done-vi.html language=enus -->
## TOPIC 00006: niTClk Is Done VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-is-done-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-is-done-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the progress of the acquisitions and/or generations, corresponding to sessions. icon Inputs/Outputs c1dgenclassrn.png sessions sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get S

### niTClk Is Done VI

Reports the progress of the acquisitions and/or generations, corresponding to sessions.

[IMAGE alt='icon' src='nitclk-is-done-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. done — done indicates whether the operation is done. The operation is done when each session has completed without any errors, or when any one of the sessions reports an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-property-node-vi.html language=enus -->
## TOPIC 00007: niTClk Property Node VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-property-node-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A LabVIEW Property Node with the NI-TClk class preselected. Gets (reads) and/or sets (writes) properties of a session reference. icon Inputs/Outputs cgenclassrn.png session reference session reference refers to the instrument session. Obtain the session reference from the instrument driver by using

### niTClk Property Node VI

A LabVIEW Property Node with the NI-TClk class preselected. Gets (reads) and/or sets (writes) properties of a session reference.

[IMAGE alt='icon' src='nitclk-property-node-vi.png']

#### Inputs/Outputs

| session reference — session reference refers to the instrument session. Obtain the session reference from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — session reference — session reference returns the session reference input unchanged. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-setup-for-sync-pulse-sender-synchronize-vi.html language=enus -->
## TOPIC 00008: niTClk Setup For Sync Pulse Sender Synchronize VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-setup-for-sync-pulse-sender-synchronize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-setup-for-sync-pulse-sender-synchronize-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TClks on all devices and prepares the Sync Pulse Sender for synchronization. icon Inputs/Outputs c1dgenclassrn.png sessions sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> G

### niTClk Setup For Sync Pulse Sender Synchronize VI

Configures the TClks on all devices and prepares the Sync Pulse Sender for synchronization.

[IMAGE alt='icon' src='nitclk-setup-for-sync-pulse-sender-synchronize-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. minimum T clock period — minimum T clock period specifies the minimum TClk period, in seconds. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. Valid values are 0.0 s to 0.050 s (50 ms), inclusive. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-synchronize-to-sync-pulse-sender-vi.html language=enus -->
## TOPIC 00009: niTClk Synchronize To Sync Pulse Sender VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-synchronize-to-sync-pulse-sender-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-synchronize-to-sync-pulse-sender-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the other devices to the Sync Pulse Sender. icon Inputs/Outputs c1dgenclassrn.png sessions sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <dri

### niTClk Synchronize To Sync Pulse Sender VI

Synchronizes the other devices to the Sync Pulse Sender.

[IMAGE alt='icon' src='nitclk-synchronize-to-sync-pulse-sender-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. minimum T clock period — minimum T clock period specifies the minimum TClk period, in seconds. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. Valid values are 0.0 s to 0.050 s (50 ms), inclusive. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-synchronize-vi.html language=enus -->
## TOPIC 00010: niTClk Synchronize VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-synchronize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-synchronize-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the TClk signals on the given sessions. After the niTClk Synchronize VI executes, the TClk signals from all the sessions are synchronized. Before using the niTClk Synchronize VI, verify that your system is configured, as described in the PXI Trigger Lines and RTSI Lines topic. icon Inpu

### niTClk Synchronize VI

Synchronizes the [TClk signals](/csh?context=nitclk_nitclk_nitclk_overview) on the given sessions. After the niTClk Synchronize VI executes, the TClk signals from all the sessions are synchronized.

Note

PXI Trigger Lines and RTSI Lines

[IMAGE alt='icon' src='nitclk-synchronize-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. minimum T clock period — minimum T clock period specifies the minimum TClk period, in seconds. The minimum period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, NI-TClk automatically coerces the minimum TClk period to 200 ns. For multichassis synchronization, adjust this value to account for the propagation delays through the various devices and cables. Valid values are 0.0 s to 0.050 s (50 ms), inclusive. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-TClk Synchronization

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/nitclk-wait-until-done-vi.html language=enus -->
## TOPIC 00011: niTClk Wait Until Done VI

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/nitclk-wait-until-done-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/nitclk-wait-until-done-vi.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the acquisitions and/or generations corresponding to sessions are done, or until the VI returns a timeout error. The niTClk Wait Until Done VI is a blocking VI that periodically checks the operation status. This VI returns control to the program if the operation completes successfully, o

### niTClk Wait Until Done VI

Waits until the acquisitions and/or generations corresponding to sessions are done, or until the VI returns a timeout error.

The niTClk Wait Until Done VI is a blocking VI that periodically checks the operation status. This VI returns control to the program if the operation completes successfully, or if an error occurs (including a timeout error). This VI is most useful for finite data operations that you want to complete within a certain time.

[IMAGE alt='icon' src='nitclk-wait-until-done-vi.png']

#### Inputs/Outputs

| sessions — sessions specifies the array of session references that are being synchronized. Obtain session references from the instrument driver by using the <driver name> Get Session Reference VI, where <driver name> is the name of the instrument driver, for example, the niScope Get Session Reference VI. timeout (seconds) — timeout (seconds) specifies the amount of time, in seconds, that the niTClk Wait Until Done VI waits for the sessions to complete. If the timeout (seconds) parameter is exceeded, the niTClk Wait Until Done VI returns an error. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. sessions out — sessions out passes the array of session references to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-TClk Synchronization

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00012: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-in-parameters.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00013: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/instr-lib/nitclk/nitclk-llb/standard-functionality-for-error-out-parameters.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk-p.html language=enus -->
## TOPIC 00014: NI-TClk Properties

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk-p.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) and/or sets (writes) properties of a session reference.

### NI-TClk Properties

Gets (reads) and/or sets (writes) properties of a session reference.

- [Active Channels](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-activechannelsproperty.html) Use this property in conjunction with the Script Trigger Master Session property to specify which Script Trigger ( scriptTrigger0 , scriptTrigger1 , scriptTrigger2 , scriptTrigger3 ) the Script Trigger Master Session applies to.
- [Actual TClk:Output Terminal](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-outputterminal.html) Specifies the destination for the TClk signal of the device.
- [Actual TClk:Period](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-period.html) Returns the computed TClk period.
- [Advanced:Sync Pulse Sender:External Pulse Source](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-externalpulsesource.html) Specifies the external sync pulse source of the Sync Pulse Sender. You can use this source to synchronize the Sync Pulse Sender with an external non-TClk event.
- [Export Sync Pulse Output Terminal](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-exportsyncpulseoutputterminal.html)
- [Pause Trigger Master Session](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-pausetriggermastersession.html) Specifies the Pause Trigger master session.
- [Reference Trigger Master Session](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-referencetriggermastersession.html)
- [Sample Clock Delay](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-sampleclockdelay.html)
- [Script Trigger Master Session](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-scripttriggermastersession.html)
- [Sequencer Flag Master Session](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-sequencerflagmastersession.html)
- [Start Trigger Master Session](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-starttriggermastersession.html)
- [Sync Pulse Clock Source](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulseclocksource.html)
- [Sync Pulse Source](../../../resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulsesource.html)

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-activechannelsproperty.html language=enus -->
## TOPIC 00015: Active Channels

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-activechannelsproperty.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-activechannelsproperty.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this property in conjunction with the Script Trigger Master Session property to specify which Script Trigger (scriptTrigger0, scriptTrigger1, scriptTrigger2, scriptTrigger3) the Script Trigger Master Session applies to. To specify the Script Trigger Master Session for more than one Script Trigge

### Active Channels

Use this property in conjunction with the [Script Trigger Master Session](pnitclk-scripttriggermastersession.html) property to specify which Script Trigger (scriptTrigger0, scriptTrigger1, scriptTrigger2, scriptTrigger3) the Script Trigger Master Session applies to.

To specify the Script Trigger Master Session for more than one Script Trigger, specify the Active Channel and the Script Trigger Master Session properties multiple times. The following example shows how to specify Script Trigger Master Session for scriptTrigger0 and scriptTrigger1.

[IMAGE alt='image' src='multi_script.gif']

The property is named Active Channels for consistency with similar properties in NI-SCOPE, NI-HSDIO, and NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveChans |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-exportsyncpulseoutputterminal.html language=enus -->
## TOPIC 00016: Export Sync Pulse Output Terminal

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-exportsyncpulseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-exportsyncpulseoutputterminal.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: ExportSyncPulseOutputTerm Description: Specifies the destination of the Sync Pulse signal. This property is most often used when synchronizing a multichassis system. Values PXI Devices: "PXI_Trig0" through "PXI_Trig7", "PXI_STAR" (Slots 3 through 15), and device-specific settings PCI Dev

### Export Sync Pulse Output Terminal

| Short Name: | ExportSyncPulseOutputTerm |
| --- | --- |
| Description: | Specifies the destination of the Sync Pulse signal. This property is most often used when synchronizing a multichassis system. |
| Values |  |
| PXI Devices: | "PXI_Trig0" through "PXI_Trig7", "PXI_STAR" (Slots 3 through 15), and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7", and device-specific settings |
| Examples of Device-specific Settings: | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI4", and "PFI5" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExportSyncPulseOutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-externalpulsesource.html language=enus -->
## TOPIC 00017: Advanced:Sync Pulse Sender:External Pulse Source

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-externalpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-externalpulsesource.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the external sync pulse source of the Sync Pulse Sender. You can use this source to synchronize the Sync Pulse Sender with an external non-TClk event. Remarks The following table lists the characteristics of this property. Short Name SyncPulseSender.ExternalPulseSrc Data type cstr.png Perm

### Advanced:Sync Pulse Sender:External Pulse Source

Specifies the external sync pulse source of the Sync Pulse Sender. You can use this source to synchronize the Sync Pulse Sender with an external non-TClk event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulseSender.ExternalPulseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-outputterminal.html language=enus -->
## TOPIC 00018: Actual TClk:Output Terminal

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-outputterminal.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination for the TClk signal of the device. Remarks The following table lists the characteristics of this property. Short Name TClk.OutputTerm Data type cstr.png Permissions Read/Write Corresponding Active Channels N/A

### Actual TClk:Output Terminal

Specifies the destination for the TClk signal of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TClk.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-pausetriggermastersession.html language=enus -->
## TOPIC 00019: Pause Trigger Master Session

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-pausetriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-pausetriggermastersession.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Pause Trigger master session. For external triggers, the NI-TClk Pause Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Pause Trigger Master Session is the session that generates the trigger. Remarks The foll

### Pause Trigger Master Session

Specifies the Pause Trigger master session.

For external triggers, the NI-TClk Pause Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Pause Trigger Master Session is the session that generates the trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PauseTrigMasterSession |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-period.html language=enus -->
## TOPIC 00020: Actual TClk:Period

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-period.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the computed TClk period. Remarks The following table lists the characteristics of this property. Short Name TClk.Period Data type cdbl.png Permissions Read Only Corresponding Active Channels N/A

### Actual TClk:Period

Returns the computed TClk period.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TClk.Period |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-referencetriggermastersession.html language=enus -->
## TOPIC 00021: Reference Trigger Master Session

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-referencetriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-referencetriggermastersession.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: RefTrigMasterSession Description: Specifies the Reference Trigger master session. For external triggers, the NI-TClk Reference Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Reference Trigger Master Session i

### Reference Trigger Master Session

| Short Name: | RefTrigMasterSession |
| --- | --- |
| Description: | Specifies the Reference Trigger master session. For external triggers, the NI-TClk Reference Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Reference Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RefTrigMasterSession |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-sampleclockdelay.html language=enus -->
## TOPIC 00022: Sample Clock Delay

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-sampleclockdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-sampleclockdelay.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name SampleClkDelay Description Specifies the delay, in seconds, to apply to the session Sample Clock, relative to the other synchronized sessions. During synchronization, NI-TClk aligns the Sample Clocks on the synchronized devices. To delay the Sample Clocks, set this property before calling

### Sample Clock Delay

| Short Name | SampleClkDelay |
| --- | --- |
| Description | Specifies the delay, in seconds, to apply to the session Sample Clock, relative to the other synchronized sessions. During synchronization, NI-TClk aligns the Sample Clocks on the synchronized devices. To delay the Sample Clocks, set this property before calling the niTClk Synchronize VI. |
| Values |  |
| Default Value | 0 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClkDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-scripttriggermastersession.html language=enus -->
## TOPIC 00023: Script Trigger Master Session

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-scripttriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-scripttriggermastersession.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name ScriptTrigMasterSession Description Specifies the Script Trigger master session. For external triggers, the NI-TClk Script Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Script Trigger Master Session is the se

### Script Trigger Master Session

| Short Name | ScriptTrigMasterSession |
| --- | --- |
| Description | Specifies the Script Trigger master session. For external triggers, the NI-TClk Script Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Script Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ScriptTrigMasterSession |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | scriptTrigger0, scriptTrigger1, scriptTrigger2, and scriptTrigger3 |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-sequencerflagmastersession.html language=enus -->
## TOPIC 00024: Sequencer Flag Master Session

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-sequencerflagmastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-sequencerflagmastersession.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: SequencerFlagMasterSession Description: Specifies the Sequencer Flag master session. For external triggers, the NI-TClk Sequencer Flag Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Sequencer Flag Master Session is t

### Sequencer Flag Master Session

| Short Name: | SequencerFlagMasterSession |
| --- | --- |
| Description: | Specifies the Sequencer Flag master session. For external triggers, the NI-TClk Sequencer Flag Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Sequencer Flag Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SequencerFlagMasterSession |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-starttriggermastersession.html language=enus -->
## TOPIC 00025: Start Trigger Master Session

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-starttriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-starttriggermastersession.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: StartTrigMasterSession Description: Specifies the Start Trigger master session. For external triggers, the NI-TClk Start Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Start Trigger Master Session is the sess

### Start Trigger Master Session

| Short Name: | StartTrigMasterSession |
| --- | --- |
| Description: | Specifies the Start Trigger master session. For external triggers, the NI-TClk Start Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Start Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | StartTrigMasterSession |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulseclocksource.html language=enus -->
## TOPIC 00026: Sync Pulse Clock Source

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulseclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulseclocksource.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: SyncPulseClkSrc Description: Specifies the source for the 10 MHz clock signal used as the Sync Pulse Clock. If you want to control this yourself when synchronizing PCI devices, then drive a 10 MHz clock onto RTSI 7 and set this property accordingly. Values PXI Devices: "PXI_CLK10", "None

### Sync Pulse Clock Source

| Short Name: | SyncPulseClkSrc |
| --- | --- |
| Description: | Specifies the source for the 10 MHz clock signal used as the Sync Pulse Clock. If you want to control this yourself when synchronizing PCI devices, then drive a 10 MHz clock onto RTSI 7 and set this property accordingly. |
| Values |  |
| PXI Devices: | "PXI_CLK10", "None" |
| PCI Devices: | "RTSI_7", "None" |
| Default Value: | "None". "None" directs the niTClk Synchronize VI to create the necessary routes. For PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7, unless RTSI 7 is already being driven. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulseClkSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties

<!--NI_TOPIC bundle=ni-tclk-labview-api-ref path=resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulsesource.html language=enus -->
## TOPIC 00027: Sync Pulse Source

- bundle_id: `ni-tclk-labview-api-ref`
- source_path: `resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-labview-api-ref/raw/resource/enus/resource/objmgr/sessionreference-rc/nitclk/pnitclk-syncpulsesource.html
- document_id: `ni-tclk-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short Name: SyncPulseClk Description: Specifies the source for the Sync Pulse. This property is most often used when synchronizing a multichassis system. Values PXI Devices: "PXI_Trig0", "PXI_Trig7", and device-specific settings PCI Devices: "RTSI_0" through "RTSI_7", and device-specific settings Ex

### Sync Pulse Source

| Short Name: | SyncPulseClk |
| --- | --- |
| Description: | Specifies the source for the Sync Pulse. This property is most often used when synchronizing a multichassis system. |
| Values |  |
| PXI Devices: | "PXI_Trig0", "PXI_Trig7", and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7", and device-specific settings |
| Examples of Device-specific Settings | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI4", and "PFI5" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. The default value (empty string) directs the niTClk Synchronize VI to set this property when all the synchronized devices are in one PXI chassis or in one PC. To synchronize a multichassis system, you must set this property before calling the niTClk Synchronize VI. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Corresponding Active Channels | N/A |

Parent topic:

NI-TClk Properties
