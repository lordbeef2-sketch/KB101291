# NI DOCUMENT BUNDLE: ni-io-trace-api-reference

<!--NI_BUNDLE_CHUNK bundle=ni-io-trace-api-reference start=1 end=6 -->
<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/closeiotracevi.html language=enus -->
## TOPIC 00001: Close IO Trace VI

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/closeiotracevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/closeiotracevi.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### Close IO Trace VI

Closes NI I/O Trace. To start logging again, restart NI I/O Trace.

[IMAGE alt='image' src='closeiotrace.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/launchiotracevi.html language=enus -->
## TOPIC 00002: Launch IO Trace VI

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/launchiotracevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/launchiotracevi.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### Launch IO Trace VI

Launches NI I/O Trace if it is not currently running.

|  | Note Only one instance of NI I/O Trace can run at a time. |
| --- | --- |

[IMAGE alt='image' src='launchiotrace.gif']

|  | launch method specifies the format in which NI I/O Trace is launched: ValueFormat 0 standard—Launches NI I/O Trace in the default window size. 1 maximized—Launches NI I/O Trace in a maximized window. 2 minimized—Launches NI I/O Trace in a minimized window. 3 hidden—Launches a hidden instance of NI I/O Trace. |
| --- | --- |
| Value | Format |
| 0 | standard—Launches NI I/O Trace in the default window size. |
| 1 | maximized—Launches NI I/O Trace in a maximized window. |
| 2 | minimized—Launches NI I/O Trace in a minimized window. |
| 3 | hidden—Launches a hidden instance of NI I/O Trace. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/logmessagevi.html language=enus -->
## TOPIC 00003: Log Message VI

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/logmessagevi.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/logmessagevi.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### Log Message VI

Writes a message to NI I/O Trace. Use this VI to log custom debug messages to NI I/O Trace.

|  | Note The message is captured only if NI I/O Trace is currently capturing. |
| --- | --- |

[IMAGE alt='image' src='logmessage.gif']

|  | message is the message logged in NI I/O Trace. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/niiotracevis.html language=enus -->
## TOPIC 00004: NI I/O Trace VIs

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/niiotracevis.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/niiotracevis.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### NI I/O Trace VIs

December 2020, 373358B-01

**Requires:** NI I/O Trace

Use the I/O Trace VIs to gather information and perform tasks programmatically. You can find the NI I/O Trace palette on the functions palette under **Measurement I/O**.

| Palette Object | Description |
| --- | --- |
| Close IO Trace | Closes NI I/O Trace. To start logging again, restart NI I/O Trace. |
| Launch IO Trace | Launches NI I/O Trace if is not currently running. |
| Log Message | Writes a message to NI I/O Trace. Use this VI to log custom debug messages to NI I/O Trace. |
| Start Tracing | Commands NI I/O Trace to start logging. |
| Stop Tracing | Commands NI I/O Trace to stop logging calls. To start logging again, use the Start IO Tracing VI or click the start button in NI I/O Trace. |

© 2020 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/starttracingvi.html language=enus -->
## TOPIC 00005: Start Tracing VI

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/starttracingvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/starttracingvi.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### Start Tracing VI

Commands NI I/O Trace to start logging.

To store the capture for later use, use the default **Capture to File** instance. Otherwise, use the **Capture to Memory** instance for ad-hoc debugging.

Use the pull-down menu to select an instance of this VI.

Select an instance

Start Tracing–Capture to File

Start Tracing–Capture to Memory

#### Start Tracing–Capture to File

[IMAGE alt='image' src='starttracingcapturetofile.gif']

|  | log file path is the absolute path where NI I/O Trace stores the log. If the node is not connected, NI I/O Trace does not save the log. Three file formats are available: .nitrace, .txt, and .csv. If the file path does not match any of the extensions, the VI returns an error. |
| --- | --- |
|  | file write mode specifies how to write the file (the default is create): ValueMode 0 create—Creates a new file. An error occurs if the file already exists. 1 append or create—Creates a new file or appends to an existing file. 2 replace or create—Creates a new file or replaces an existing file. |
| Value | Mode |
| 0 | create—Creates a new file. An error occurs if the file already exists. |
| 1 | append or create—Creates a new file or appends to an existing file. |
| 2 | replace or create—Creates a new file or replaces an existing file. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Start Tracing–Capture to Memory

[IMAGE alt='image' src='starttracingcapturetomemory.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-io-trace-api-reference path=iotraceapi/stoptracingvi.html language=enus -->
## TOPIC 00006: Stop Tracing VI

- bundle_id: `ni-io-trace-api-reference`
- source_path: `iotraceapi/stoptracingvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-io-trace-api-reference/raw/resource/enus/iotraceapi/stoptracingvi.html
- document_id: `ni-io-trace-api-reference`
- page_type: `leaf`
- content_type: ``

### Stop Tracing VI

Commands NI I/O Trace to stop logging calls. To start logging again, use the Start Tracing VI or click the start button in NI I/O Trace.

[IMAGE alt='image' src='stoptracing.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |
