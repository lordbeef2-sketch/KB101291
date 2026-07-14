# NI DOCUMENT BUNDLE: ni-usrp-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-usrp-lvnxg-api-ref start=1 end=40 -->
<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=fetch-rx-data.html language=enus -->
## TOPIC 00001: niUSRP Fetch Rx Data

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `fetch-rx-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/fetch-rx-data.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches data from the specified channel list.

niUSRP Fetch Rx Data

Fetches data from the specified channel list.

Rx and Tx Nodes

niUSRP Fetch Rx Data (2D CDB)

Fetches complex, double-precision floating-point data from the specified channels.

niUSRP Fetch Rx Data (2D I16)

16-bit

niUSRP Fetch Rx Data (CDB)

Fetches complex, double-precision floating-point data from the specified channel.

niUSRP Fetch Rx Data (CDB Cluster)

Fetches a cluster of complex, double-precision floating-point data from the specified channel.

niUSRP Fetch Rx Data (CDB WDT)

Fetches complex, double-precision floating-point data in a waveform data type from the specified channel.

niUSRP Fetch Rx Data (I16)

16-bit

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-abort.html language=enus -->
## TOPIC 00002: niUSRP Abort

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-abort.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops an acquisition previously started. For finite acquisitions, calling this node is optional unless you want to stop the acquisition before it completes. If the acquisition aborts successfully, the driver transitions to the Done state. session handle Instrument session. error in Error conditions

niUSRP Abort

Stops an acquisition previously started.

For finite acquisitions, calling this node is optional unless you want to stop the acquisition before it completes. If the acquisition aborts successfully, the driver transitions to the Done state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-clear-error.html language=enus -->
## TOPIC 00003: niUSRP Clear Error

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-clear-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-clear-error.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the last error code. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session handle out Reference to your instrument session to

niUSRP Clear Error

Clears the last error code.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-close-session.html language=enus -->
## TOPIC 00004: niUSRP Close Session

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-close-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-close-session.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session handle to the device. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces

niUSRP Close Session

Closes the session handle to the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-commit.html language=enus -->
## TOPIC 00005: niUSRP Commit

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-commit.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Validates any changed properties and commits the settings to the device. This node also starts the process of locking to a reference frequency if you specify a source using the Reference Frequency Source property. If the commit operation is successful, the driver transitions to the Committed state.

niUSRP Commit

Validates any changed properties and commits the settings to the device.

This node also starts the process of locking to a reference frequency if you specify a source using the Reference Frequency Source property. If the commit operation is successful, the driver transitions to the Committed state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-configure-number-of-samples.html language=enus -->
## TOPIC 00006: niUSRP Configure Number of Samples

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-configure-number-of-samples.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-configure-number-of-samples.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device operation is finite or continuous and the number of samples to acquire. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default va

niUSRP Configure Number of Samples

Specifies whether the device operation is finite or continuous and the number of samples to acquire.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### number of samples is finite

Boolean that specifies how many samples are acquired by the device.

| True | Device acquires a finite number of samples. |
| --- | --- |
| False | Device acquires samples continuously. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to acquire from the device.

number of samples is finite

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-configure-signal.html language=enus -->
## TOPIC 00007: niUSRP Configure Signal

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-configure-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-configure-signal.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures properties of the transmit (Tx) or receive (Rx) signal. The USRP devices are not calibrated. The gain value does not represent an absolute gain and does not have linear behavior. Different devices exhibit different gain curves for different carrier frequencies. You may need to experiment

niUSRP Configure Signal

Configures properties of the transmit (Tx) or receive (Rx) signal.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### IQ rate

Rate of the baseband I/Q data in samples per second (S/s).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### carrier frequency

Carrier frequency, in Hz, of the RF signal.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

Aggregate gain, in dB, applied to the RF signal.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channels to configure.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### active antenna

Antenna port to use for this channel.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced IQ rate

Actual I/Q rate, in samples per second (S/s), for this session, coerced to a value supported by the device.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced carrier frequency

Actual carrier frequency, in Hz, for this session, coerced to a value supported by the device.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced gain

Actual gain, in dB, for this session, coerced to a value supported by the device.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

#### Antenna Names

| USRP Device | Connector Name | PCB (Internal) Name |
| --- | --- | --- |
| USRP-2900/2901/2920/2922/2930/2932 | TX1, RX1 | TX/RX |
| RX2 | RX2 |  |
| USRP-2921 | RX1, TX1 | J1 |
| RX2, TX2 | J2 |  |
| USRP-2940/2942/2943/2944/2950/2952/2953/2954/2974 | TX1, RX1 | TX/RX |
| RX2 | RX2 |  |
| USRP-2945/2955 | RX1 | RX |
| RX2 | RX2 |  |

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-configure-time-start-trigger.html language=enus -->
## TOPIC 00008: niUSRP Configure Time Start Trigger

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-configure-time-start-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-configure-time-start-trigger.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger. The time Start Trigger specifies the time, according to the onboard device timer, to acquire (Rx) or generate (Tx) the first sample. This node supports the following hardware: USRP-2900/29

niUSRP Configure Time Start Trigger

Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger.

The time Start Trigger specifies the time, according to the onboard device timer, to acquire (Rx) or generate (Tx) the first sample.

[IMAGE alt='connector_pane_image' src='niUSRP_Configure_Time_Start_Trigger.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

#### start trigger time

Time the trigger occurs in seconds, interpreted as 
whole seconds.fractional seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### whole seconds

Integer number of seconds for the time of the Start Trigger, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fractional seconds

Double-precision floating-point value representing the remaining fraction of a second for the time of the Start Trigger, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

Web Server:

**Hardware Support:**

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Configure Trigger

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-configure-trigger.html language=enus -->
## TOPIC 00009: niUSRP Configure Trigger

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-configure-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-configure-trigger.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger. The time Start Trigger specifies the time, according to the onboard device timer, to acquire (Rx) or generate (Tx) the first sample.

niUSRP Configure Trigger

Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger. The time Start Trigger specifies the time, according to the onboard device timer, to acquire (Rx) or generate (Tx) the first sample.

Synchronization Nodes

niUSRP Configure Time Start Trigger

Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger.

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-disable-start-trigger.html language=enus -->
## TOPIC 00010: niUSRP Disable Start Trigger

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-disable-start-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-disable-start-trigger.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior.

niUSRP Disable Start Trigger

Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-export-signal.html language=enus -->
## TOPIC 00011: niUSRP Export Signal

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-export-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-export-signal.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a route to export the specified signal to the specified output terminal. Valid mapping is one-to-one such that Reference Frequency maps to REF OUT, Timebase Clock maps to PPS TRIG OUT, and LO maps to LO OUT. session handle Instrument session. error in Error conditions that occur before this

niUSRP Export Signal

Creates a route to export the specified signal to the specified output terminal.
 Valid mapping is one-to-one such that Reference Frequency maps to REF OUT, Timebase Clock maps to PPS TRIG OUT, and LO maps to LO OUT.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### signal

Signal to route out of the device.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### output terminal

Output terminal to which the signal will be routed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channels to configure.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-2d-cdb.html language=enus -->
## TOPIC 00012: niUSRP Fetch Rx Data (2D CDB)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-2d-cdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-2d-cdb.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data from the specified channels. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error numb

niUSRP Fetch Rx Data (2D CDB)

Fetches complex, double-precision floating-point data from the specified channels.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### data

Received baseband samples as an array of complex, double-precision floating-point data.

number of samples

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-2d-i16.html language=enus -->
## TOPIC 00013: niUSRP Fetch Rx Data (2D I16)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-2d-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-2d-i16.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, 16-bit signed integer data from the specified channels. To use niUSRP Fetch Rx Data (2D I16), you must set the Host Data Type property to I16. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to

niUSRP Fetch Rx Data (2D I16)

Fetches complex, 16-bit signed integer data from the specified channels.
 To use niUSRP Fetch Rx Data (2D I16), you must set the Host Data Type property to I16.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1di16.png']

##### data

Received baseband samples as an array of complex, 16-bit signed integer data.

number of samples

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-cdb-cluster.html language=enus -->
## TOPIC 00014: niUSRP Fetch Rx Data (CDB Cluster)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-cdb-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-cdb-cluster.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a cluster of complex, double-precision floating-point data from the specified channel. Modulation Toolkit nodes use the complex, double-precision floating-point cluster data type. Use this node in applications that use Modulation Toolkit nodes. session handle Instrument session. number of sa

niUSRP Fetch Rx Data (CDB Cluster)

Fetches a cluster of complex, double-precision floating-point data from the specified channel.
 Modulation Toolkit nodes use the complex, double-precision floating-point cluster data type. Use this node in applications that use Modulation Toolkit nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### data

Received baseband samples as complex, double-precision floating-point data in a cluster, which also includes sampling information.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the acquired Y array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time between values in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-cdb-wdt.html language=enus -->
## TOPIC 00015: niUSRP Fetch Rx Data (CDB WDT)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-cdb-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-cdb-wdt.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data in a waveform data type from the specified channel. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

niUSRP Fetch Rx Data (CDB WDT)

Fetches complex, double-precision floating-point data in a waveform data type from the specified channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

Received baseband samples as complex, double-precision floating-point data in a waveform data type, which also includes sampling information.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-cdb.html language=enus -->
## TOPIC 00016: niUSRP Fetch Rx Data (CDB)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-cdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-cdb.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data from the specified channel. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error numbe

niUSRP Fetch Rx Data (CDB)

Fetches complex, double-precision floating-point data from the specified channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### data

Received baseband samples as an array of complex, double-precision floating-point data.

data

Power Spectrum

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-fetch-rx-data-i16.html language=enus -->
## TOPIC 00017: niUSRP Fetch Rx Data (I16)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-fetch-rx-data-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-fetch-rx-data-i16.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, 16-bit signed integer data from the specified channel. To use niUSRP Fetch Rx Data (I16), you must set the Host Data Type property to I16. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to stan

niUSRP Fetch Rx Data (I16)

Fetches complex, 16-bit signed integer data from the specified channel.

To use niUSRP Fetch Rx Data (I16), you must set the Host Data Type property to I16.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of samples

Number of samples to fetch from the acquisition channel.

For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been acquired.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) from which to fetch the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1di16.png']

##### data

Received baseband samples as an array of complex, 16-bit signed integer data.

number of samples

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### timestamp

Timestamp of the first receive (Rx) sample returned and the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

Parent topic:

niUSRP Fetch Rx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-find-devices.html language=enus -->
## TOPIC 00018: niUSRP Find Devices

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-find-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-find-devices.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of USRP devices discovered in the system. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error niUSRP devices Array of niUSRP device clusters, where each niUSRP

niUSRP Find Devices

Returns a list of USRP devices discovered in the system.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niUSRP devices

Array of 
niUSRP device clusters, where each 
niUSRP device cluster represents a device discovered in the system.

niUSRP device

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### address

String containing the IP address of the device.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### serial number

String containing the serial number of the device.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### model

String containing the model name of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-get-time.html language=enus -->
## TOPIC 00019: niUSRP Get Time

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-get-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-get-time.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time value of the onboard device timer. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error when When to get the timestamp from

niUSRP Get Time

Returns the time value of the onboard device timer.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### when

When to get the timestamp from the onboard device timer.

Default value: now

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channels to configure.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### USRP Timestamp

Timestamp in the format used by USRP.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-initiate.html language=enus -->
## TOPIC 00020: niUSRP Initiate

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-initiate.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts the Rx acquisition. niUSRP Initiate starts the waveform acquisition in a receive (Rx) session. You must initiate the Rx session before you use niUSRP Fetch Rx Data to retrieve waveform data. You do not need to call niUSRP Initiate for transmit (Tx) sessions; you initiate waveform generation w

niUSRP Initiate

Starts the Rx acquisition.

niUSRP Initiate starts the waveform acquisition in a receive (Rx) session. You must initiate the Rx session before you use niUSRP Fetch Rx Data to retrieve waveform data. You do not need to call niUSRP Initiate for transmit (Tx) sessions; you initiate waveform generation when you provide data using niUSRP Write Tx Data.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-lv-timestamp-to-usrp-timestamp.html language=enus -->
## TOPIC 00021: niUSRP LV Timestamp to USRP Timestamp

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-lv-timestamp-to-usrp-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-lv-timestamp-to-usrp-timestamp.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Translates a LabVIEW timestamp to a USRP timestamp. LabVIEW Timestamp Timestamp with the format used in LabVIEW. The timestamp data is displayed in hours, minutes, seconds, and milliseconds, as well as the month, day, and year. error in Error conditions that occur before this node runs. The node res

niUSRP LV Timestamp to USRP Timestamp

Translates a LabVIEW timestamp to a USRP timestamp.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### LabVIEW Timestamp

Timestamp with the format used in LabVIEW.

The timestamp data is displayed in hours, minutes, seconds, and milliseconds, as well as the month, day, and year.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### USRP Timestamp

Timestamp in the format used by USRP.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-nodes.html language=enus -->
## TOPIC 00022: NI-USRP Nodes

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-nodes.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-USRP nodes to develop applications for USRP devices. These nodes cannot be used with USRP RIO nodes.

NI-USRP Nodes

Use NI-USRP nodes to develop applications for USRP devices. These nodes cannot be used with USRP RIO nodes.

niUSRP Properties

Gets (reads) or sets (writes) NI-USRP properties.

Rx and Tx Nodes

Synchronization Nodes

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-open-rx-session.html language=enus -->
## TOPIC 00023: niUSRP Open Rx Session

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-open-rx-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-open-rx-session.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a receive (Rx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes. device names Name(s) or IP address(es) of the device(s). error in Error conditions that occur before this node runs. The node responds to this input according to

niUSRP Open Rx Session

Opens a receive (Rx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### device names

Name(s) or IP address(es) of the device(s).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### Reset

Boolean that specifies whether to reset the device(s) to a known initialization state.

| True | Resets the device to a known initialization state. |
| --- | --- |
| False | Does not reset the device. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-open-tx-session.html language=enus -->
## TOPIC 00024: niUSRP Open Tx Session

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-open-tx-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-open-tx-session.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a transmit (Tx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes. device names Name(s) or IP address(es) of the device(s). error in Error conditions that occur before this node runs. The node responds to this input according to

niUSRP Open Tx Session

Opens a transmit (Tx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### device names

Name(s) or IP address(es) of the device(s).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### Reset

Boolean that specifies whether to reset the device(s) to a known initialization state.

| True | Resets the device to a known initialization state. |
| --- | --- |
| False | Does not reset the device. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

Rx and Tx Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-properties.html language=enus -->
## TOPIC 00025: niUSRP Properties

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-properties.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Gets (reads) or sets (writes) NI-USRP properties. When you read a property, NI-USRP analyzes the current configuration in order to return the coerced value for that property. Setting a property may transition the session to the Initialized state. This node supports the following hardware: USRP-2900/

niUSRP Properties

Gets (reads) or sets (writes) NI-USRP properties.

When you read a property, NI-USRP analyzes the current configuration in order to return the coerced value for that property. Setting a property may transition the session to the Initialized state.

[IMAGE alt='connector_pane_image' src='PropertyNode.niUSRPClass.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### niUSRP in

Reference to the niUSRP session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### Active Channel

Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you want to set the property on all channels, pass an empty string or omit setting this property.

Enter 
 0 for the first channel and 
 1 for the second channel. The order of the IP addresses sets the channel order.

**Default:**"" (empty string)

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### niUSRP out

Reference to the niUSRP session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

Web Server:

**Hardware Support:**

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

NI-USRP Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-reset.html language=enus -->
## TOPIC 00026: niUSRP Reset

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-reset.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to a known initialization state. This node aborts any existing acquisitions or generations and restores the device properties to their default states. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input acco

niUSRP Reset

Resets the device to a known initialization state.
 This node aborts any existing acquisitions or generations and restores the device properties to their default states.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-self-test.html language=enus -->
## TOPIC 00027: niUSRP Self Test

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-self-test.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test of the device. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session handle out Reference to your instrument ses

niUSRP Self Test

Performs a self-test of the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### test result

Result of the self-test.

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-set-time.html language=enus -->
## TOPIC 00028: niUSRP Set Time

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-set-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-set-time.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time value of the onboard device timer. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error apply timestamp When to apply the time

niUSRP Set Time

Sets the time value of the onboard device timer.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### apply timestamp

When to apply the timestamp to the onboard device timer.

Default value: now

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### timestamp

Time to set on the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### whole seconds

The integer number of seconds for the time to set on the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fractional seconds

The double-precision floating-point value representing the remaining fraction of a second for the time to set on the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) on which to set the time.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-usrp-timestamp-to-lv-timestamp.html language=enus -->
## TOPIC 00029: niUSRP USRP Timestamp to LV Timestamp

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-usrp-timestamp-to-lv-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-usrp-timestamp-to-lv-timestamp.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a USRP timestamp to a LabVIEW timestamp. USRP Timestamp Timestamp in the format used by USRP. whole seconds Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds Double-precision, floating-point val

niUSRP USRP Timestamp to LV Timestamp

Converts a USRP timestamp to a LabVIEW timestamp.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### USRP Timestamp

Timestamp in the format used by USRP.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### whole seconds

Integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional seconds

Double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### LV Timestamp

LabVIEW time stamp output that specifies the 1588 time since zero hours on 1 January 1904.

Note

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-wait-for-lock.html language=enus -->
## TOPIC 00030: niUSRP Wait For Lock

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-wait-for-lock.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-wait-for-lock.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the GPS to lock. GPSDO may take up to 10 minutes to lock to a satellite the first time. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Erro

niUSRP Wait For Lock

Configures the device to wait for the GPS to lock.

GPSDO may take up to 10 minutes to lock to a satellite the first time.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### device

Lock signal to wait for.

Leave this input set to the default value.

Default value: GPS

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channels to configure.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-2d-cdb.html language=enus -->
## TOPIC 00031: niUSRP Write Tx Data (2D CDB)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-2d-cdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-2d-cdb.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data to the specified channels. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error data Ba

niUSRP Write Tx Data (2D CDB)

Writes complex, double-precision floating-point data to the specified channels.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### data

Baseband samples to transmit as an array of complex, double-precision floating-point data.

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-2d-i16.html language=enus -->
## TOPIC 00032: niUSRP Write Tx Data (2D I16)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-2d-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-2d-i16.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, 16-bit signed integer data to the specified channels. To use niUSRP Write Tx Data (2D I16), you must set the Host Data Type property to I16. data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following

niUSRP Write Tx Data (2D I16)

Writes complex, 16-bit signed integer data to the specified channels. To use niUSRP Write Tx Data (2D I16), you must set the Host Data Type property to I16.

data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

=

b

i

n

a

r

y

⁢

v

a

l

u

e

32

,

768

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

=

b

i

n

a

r

y

⁢

v

a

l

u

e

32

,

768

b

i

n

a

r

y

⁢

v

a

l

u

e

=

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

×

32

,

767

b

i

n

a

r

y

⁢

v

a

l

u

e

=

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

×

32

,

767

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### data

Baseband samples to transmit as an array of complex, 16-bit signed integer data.

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

data

16-bit

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-cdb-cluster.html language=enus -->
## TOPIC 00033: niUSRP Write Tx Data (CDB Cluster)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-cdb-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-cdb-cluster.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a cluster of complex, double-precision floating-point data to the specified channel. Modulation Toolkit nodes use the complex, double-precision floating-point cluster data type. Use this node in applications that use Modulation Toolkit nodes. session handle Instrument session. error in Error

niUSRP Write Tx Data (CDB Cluster)

Writes a cluster of complex, double-precision floating-point data to the specified channel.
 Modulation Toolkit nodes use the complex, double-precision floating-point cluster data type. Use this node in applications that use Modulation Toolkit nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### data

Baseband samples to transmit as complex, double-precision floating-point data in a cluster, which also includes sampling information.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

NI-USRP ignores this value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time between values in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean that determines whether the dt element of the data waveform overrides the I/Q rate.

| True | dt element of the data waveform overrides the I/Q/ rate. |
| --- | --- |
| False | No override of the I/Q rate. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-cdb-wdt.html language=enus -->
## TOPIC 00034: niUSRP Write Tx Data (CDB WDT)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-cdb-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-cdb-wdt.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data in a waveform data type to the specified channel. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default

niUSRP Write Tx Data (CDB WDT)

Writes complex, double-precision floating-point data in a waveform data type to the specified channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### data

Baseband samples to transmit as complex, double-precision floating-point data in a waveform data type, which also includes sampling information.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean that determines whether the dt element of the data waveform overrides the I/Q rate.

| True | dt element of the data waveform overrides the I/Q/ rate. |
| --- | --- |
| False | No override of the I/Q rate. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-cdb.html language=enus -->
## TOPIC 00035: niUSRP Write Tx Data (CDB)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-cdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-cdb.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data to the specified channel. session handle Instrument session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error data Bas

niUSRP Write Tx Data (CDB)

Writes complex, double-precision floating-point data to the specified channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### data

Baseband samples to transmit as an array of complex, double-precision floating-point data.

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=niusrp-write-tx-data-i16.html language=enus -->
## TOPIC 00036: niUSRP Write Tx Data (I16)

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `niusrp-write-tx-data-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/niusrp-write-tx-data-i16.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, 16-bit signed integer data to the specified channel. To use niUSRP Write Tx Data (I16), you must set the Host Data Type property to I16. data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equ

niUSRP Write Tx Data (I16)

Writes complex, 16-bit signed integer data to the specified channel.
 To use niUSRP Write Tx Data (I16), you must set the Host Data Type property to I16.

data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

=

b

i

n

a

r

y

⁢

v

a

l

u

e

32

,

768

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

=

b

i

n

a

r

y

⁢

v

a

l

u

e

32

,

768

b

i

n

a

r

y

⁢

v

a

l

u

e

=

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

×

32

,

767

b

i

n

a

r

y

⁢

v

a

l

u

e

=

f

l

o

a

t

i

n

g

-

p

o

i

n

t

v

a

l

u

e

×

32

,

767

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### session handle

Instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### data

Baseband samples to transmit as an array of complex, 16-bit signed integer data.

The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of Configure Signal.

data

16-bit

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time to wait, in seconds, before returning an error if the requested number of samples have not been generated.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### end of data?

Boolean that determines whether this is the last call to niUSRP Write Tx Data for the current contiguous transmit operation.

| True | Indicates that this is the last call to niUSRP Write Tx Data. |
| --- | --- |
| False | No indication of the last call. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

Channel(s) to which to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session handle out

Reference to your instrument session to be passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944
- USRP-2950/2952/2953/2954

Parent topic:

niUSRP Write Tx Data

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=rx-tx-nodes.html language=enus -->
## TOPIC 00037: Rx and Tx Nodes

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `rx-tx-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/rx-tx-nodes.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Rx and Tx Nodes

NI-USRP Nodes

Use NI-USRP nodes to develop applications for USRP devices.

niUSRP Abort

Stops an acquisition previously started.

niUSRP Close Session

Closes the session handle to the device.

niUSRP Configure Number of Samples

Specifies whether the device operation is finite or continuous and the number of samples to acquire.

niUSRP Configure Signal

Configures properties of the transmit (Tx) or receive (Rx) signal.

niUSRP Fetch Rx Data

Fetches data from the specified channel list.

niUSRP Initiate

Starts the Rx acquisition.

niUSRP Open Rx Session

Opens a receive (Rx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes.

niUSRP Open Tx Session

Opens a transmit (Tx) session to the device you specify and returns the instrument session, which you use in all subsequent NI-USRP nodes.

niUSRP Write Tx Data

Writes data to the specified channel list.

Parent topic:

NI-USRP Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=synchronization-nodes.html language=enus -->
## TOPIC 00038: Synchronization Nodes

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `synchronization-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/synchronization-nodes.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Synchronization Nodes

NI-USRP Nodes

Use NI-USRP nodes to develop applications for USRP devices.

niUSRP Configure Trigger

Configures the Start Trigger generated by the onboard device timer and specifies the time to start the trigger. The time Start Trigger specifies the time, according to the onboard device timer, to acquire (Rx) or generate (Tx) the first sample.

niUSRP Disable Start Trigger

Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available.

niUSRP Export Signal

Creates a route to export the specified signal to the specified output terminal.

niUSRP Get Time

Returns the time value of the onboard device timer.

niUSRP Set Time

Sets the time value of the onboard device timer.

niUSRP Wait For Lock

Configures the device to wait for the GPS to lock.

Parent topic:

NI-USRP Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00039: Utility Nodes

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Utility Nodes

NI-USRP Nodes

Use NI-USRP nodes to develop applications for USRP devices.

niUSRP Clear Error

Clears the last error code.

niUSRP Commit

Validates any changed properties and commits the settings to the device.

niUSRP Find Devices

Returns a list of USRP devices discovered in the system.

niUSRP LV Timestamp to USRP Timestamp

Translates a LabVIEW timestamp to a USRP timestamp.

niUSRP Reset

Resets the device to a known initialization state.

niUSRP Self Test

Performs a self-test of the device.

niUSRP USRP Timestamp to LV Timestamp

Converts a USRP timestamp to a LabVIEW timestamp.

Parent topic:

NI-USRP Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-api-ref path=write-tx-data.html language=enus -->
## TOPIC 00040: niUSRP Write Tx Data

- bundle_id: `ni-usrp-lvnxg-api-ref`
- source_path: `write-tx-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-api-ref/raw/resource/enus/write-tx-data.html
- document_id: `ni-usrp-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the specified channel list.

niUSRP Write Tx Data

Writes data to the specified channel list.

Rx and Tx Nodes

niUSRP Write Tx Data (2D CDB)

Writes complex, double-precision floating-point data to the specified channels.

niUSRP Write Tx Data (2D I16)

Writes complex, 16-bit signed integer data to the specified channels.

niUSRP Write Tx Data (CDB)

Writes complex, double-precision floating-point data to the specified channel.

niUSRP Write Tx Data (CDB Cluster)

Writes a cluster of complex, double-precision floating-point data to the specified channel.

niUSRP Write Tx Data (CDB WDT)

Writes complex, double-precision floating-point data in a waveform data type to the specified channel.

niUSRP Write Tx Data (I16)

16-bit

Parent topic:

Rx and Tx Nodes
