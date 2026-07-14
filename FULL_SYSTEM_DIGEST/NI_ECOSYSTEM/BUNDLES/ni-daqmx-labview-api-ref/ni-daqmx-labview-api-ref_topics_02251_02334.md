# NI DOCUMENT BUNDLE: ni-daqmx-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-labview-api-ref start=2251 end=2334 -->
<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-1chan-nsamp-vi.html language=enus -->
## TOPIC 02251: DAQmx Read (Digital 1D U32 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from a task that contains a single digital input channel. Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task o

### DAQmx Read (Digital 1D U32 1Chan NSamp) VI

Reads one or more 32-bit unsigned integer samples from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-1d-u32-1chan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of 32-bit unsigned integer samples. Each element in the array corresponds to a sample from the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-nchan-1samp-vi.html language=enus -->
## TOPIC 02252: DAQmx Read (Digital 1D U32 NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit unsigned integer sample from each channel in a task that contains one or more digital input channels. Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the na

### DAQmx Read (Digital 1D U32 NChan 1Samp) VI

Reads a single 32-bit unsigned integer sample from each channel in a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-1d-u32-nchan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of 32-bit unsigned integer samples. Each element in the array corresponds to a channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-1chan-nsamp-vi.html language=enus -->
## TOPIC 02253: DAQmx Read (Digital 1D U8 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from a task that contains a single digital input channel. Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task

### DAQmx Read (Digital 1D U8 1Chan NSamp) VI

Reads one or more 8-bit unsigned integer samples from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-1d-u8-1chan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of 8-bit unsigned integer samples. Each element in the array corresponds to a sample from the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-nchan-1samp-vi.html language=enus -->
## TOPIC 02254: DAQmx Read (Digital 1D U8 NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 8-bit unsigned integer sample from each channel in a task that contains one or more digital input channels. Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the n

### DAQmx Read (Digital 1D U8 NChan 1Samp) VI

Reads a single 8-bit unsigned integer sample from each channel in a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-1d-u8-nchan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of 8-bit unsigned integer samples. Each element in the array corresponds to a channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-1samp-vi.html language=enus -->
## TOPIC 02255: DAQmx Read (Digital 1D Wfm NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform that contains a single sample from each channel in a task that contains one or more digital input channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a

### DAQmx Read (Digital 1D Wfm NChan 1Samp) VI

Reads a waveform that contains a single sample from each channel in a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-1d-wfm-nchan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of digital waveforms that each contain a single sample. Each element in the array corresponds to a channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-duration-vi.html language=enus -->
## TOPIC 02256: DAQmx Read (Digital 1D Wfm NChan NSamp Duration) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-duration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-duration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveforms from a task that contains one or more digital input channels for a specified amount of time. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provi

### DAQmx Read (Digital 1D Wfm NChan NSamp Duration) VI

Reads one or more digital waveforms from a task that contains one or more [digital input channels for a specified amount of time](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-1d-wfm-nchan-nsamp-duration-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. duration — duration specifies the amount of time in seconds to read samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of digital waveforms. Each element in the array corresponds to a channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-vi.html language=enus -->
## TOPIC 02257: DAQmx Read (Digital 1D Wfm NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveforms from a task that contains one or more digital input channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels,

### DAQmx Read (Digital 1D Wfm NChan NSamp) VI

Reads one or more digital waveforms from a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-1d-wfm-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of digital waveforms. Each element in the array corresponds to a channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-2d-bool-nchan-1samp-nline-vi.html language=enus -->
## TOPIC 02258: DAQmx Read (Digital 2D Bool NChan 1Samp NLine) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-2d-bool-nchan-1samp-nline-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-2d-bool-nchan-1samp-nline-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single sample that contains Boolean values from each channel in a task that contains one or more digital input channels. Each channel can contain multiple digital lines. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual chan

### DAQmx Read (Digital 2D Bool NChan 1Samp NLine) VI

Reads a single sample that contains Boolean values from each channel in a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Each channel can contain multiple digital lines.

[IMAGE alt='icon' src='daqmx-read-digital-2d-bool-nchan-1samp-nline-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 2D array of Boolean samples. Each row corresponds to a channel in the task. Each column corresponds to a line in that channel. The order of the channels in the array corresponds to the order that you add the channels to the task or to the order of the channels you specify in the Channels to Read property. The order of the lines in each channel corresponds to the order that you add the lines to the channel. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u16-nchan-nsamp-vi.html language=enus -->
## TOPIC 02259: DAQmx Read (Digital 2D U16 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u16-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u16-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from a task that contains one or more digital input channels. Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the ta

### DAQmx Read (Digital 2D U16 NChan NSamp) VI

Reads one or more 16-bit unsigned integer samples from a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-2d-u16-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 2D array of 16-bit unsigned integer samples. Each row corresponds to a channel in the task. Each column corresponds to a sample from each channel. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u32-nchan-nsamp-vi.html language=enus -->
## TOPIC 02260: DAQmx Read (Digital 2D U32 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u32-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u32-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from a task that contains one or more digital input channels. Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the ta

### DAQmx Read (Digital 2D U32 NChan NSamp) VI

Reads one or more 32-bit unsigned integer samples from a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-2d-u32-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 2D array of 32-bit unsigned integer samples. Each row corresponds to a channel in the task. Each column corresponds to a sample from each channel. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u8-nchan-nsamp-vi.html language=enus -->
## TOPIC 02261: DAQmx Read (Digital 2D U8 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u8-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u8-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from a task that contains one or more digital input channels. Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the t

### DAQmx Read (Digital 2D U8 NChan NSamp) VI

Reads one or more 8-bit unsigned integer samples from a task that contains one or more [digital input channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-2d-u8-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 2D array of 8-bit unsigned integer samples. Each row corresponds to a channel in the task. Each column corresponds to a sample from each channel. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-bool-1line-1point-vi.html language=enus -->
## TOPIC 02262: DAQmx Read (Digital Bool 1Line 1Point) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-bool-1line-1point-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-bool-1line-1point-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Boolean sample from a task that contains a digital input channel composed of a single line. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual c

### DAQmx Read (Digital Bool 1Line 1Point) VI

Reads a single Boolean sample from a task that contains a [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes) composed of a single line.

[IMAGE alt='icon' src='daqmx-read-digital-bool-1line-1point-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a Boolean sample. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-u16-1chan-1samp-vi.html language=enus -->
## TOPIC 02263: DAQmx Read (Digital U16 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-u16-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-u16-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 16-bit unsigned integer sample from a task that contains a single digital input channel. Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a

### DAQmx Read (Digital U16 1Chan 1Samp) VI

Reads a single 16-bit unsigned integer sample from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-u16-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 16-bit unsigned integer sample. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-u32-1chan-1samp-vi.html language=enus -->
## TOPIC 02264: DAQmx Read (Digital U32 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-u32-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-u32-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit unsigned integer sample from a task that contains a single digital input channel. Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a

### DAQmx Read (Digital U32 1Chan 1Samp) VI

Reads a single 32-bit unsigned integer sample from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-u32-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 32-bit unsigned integer sample. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-u8-1chan-1samp-vi.html language=enus -->
## TOPIC 02265: DAQmx Read (Digital U8 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-u8-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-u8-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 8-bit unsigned integer sample from a task that contains a single digital input channel. Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a

### DAQmx Read (Digital U8 1Chan 1Samp) VI

Reads a single 8-bit unsigned integer sample from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-read-digital-u8-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns an 8-bit unsigned integer sample. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-1samp-vi.html language=enus -->
## TOPIC 02266: DAQmx Read (Digital Wfm 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a digital waveform that contains a single sample from a task that contains a single digital input channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of vir

### DAQmx Read (Digital Wfm 1Chan 1Samp) VI

Reads a digital waveform that contains a single sample from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-wfm-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a digital waveform. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-duration-vi.html language=enus -->
## TOPIC 02267: DAQmx Read (Digital Wfm 1Chan NSamp Duration) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-duration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-duration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a digital waveform from a task that contains a single digital input channel for a specified amount of time. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of vi

### DAQmx Read (Digital Wfm 1Chan NSamp Duration) VI

Reads a digital waveform from a task that contains a single [digital input channel for a specified amount of time](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-wfm-1chan-nsamp-duration-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. duration — duration specifies the amount of time in seconds to read samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a digital waveform. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-vi.html language=enus -->
## TOPIC 02268: DAQmx Read (Digital Wfm 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a digital waveform from a task that contains a single digital input channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx create

### DAQmx Read (Digital Wfm 1Chan NSamp) VI

Reads a digital waveform from a task that contains a single [digital input channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-read-digital-wfm-1chan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a digital waveform. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-1chan-nsamp-vi.html language=enus -->
## TOPIC 02269: DAQmx Read (Power 1D DBL 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from a task that contains a single power channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQm

### DAQmx Read (Power 1D DBL 1Chan NSamp) VI

Reads one or more floating-point samples from a task that contains a single power channel.

[IMAGE alt='icon' src='daqmx-read-power-1d-dbl-1chan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-nchan-1samp-vi.html language=enus -->
## TOPIC 02270: DAQmx Read (Power 1D DBL NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one floating-point sample from a task that contains one or more power channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx cre

### DAQmx Read (Power 1D DBL NChan 1Samp) VI

Reads one floating-point sample from a task that contains one or more power channels.

[IMAGE alt='icon' src='daqmx-read-power-1d-dbl-nchan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-1samp-vi.html language=enus -->
## TOPIC 02271: DAQmx Read (Power 1D Wfm NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform that contains a single floating-point sample from each channel in a task that contains one or more power channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you pr

### DAQmx Read (Power 1D Wfm NChan 1Samp) VI

Reads a waveform that contains a single floating-point sample from each channel in a task that contains one or more power channels.

[IMAGE alt='icon' src='daqmx-read-power-1d-wfm-nchan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-nsamp-vi.html language=enus -->
## TOPIC 02272: DAQmx Read (Power 1D Wfm NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more waveforms that contains one or more floating-point samples from a task that contains one or more power channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you pro

### DAQmx Read (Power 1D Wfm NChan NSamp) VI

Reads one or more waveforms that contains one or more floating-point samples from a task that contains one or more power channels.

[IMAGE alt='icon' src='daqmx-read-power-1d-wfm-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-2d-dbl-nchan-nsamp-vi.html language=enus -->
## TOPIC 02273: DAQmx Read (Power 2D DBL NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-2d-dbl-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-2d-dbl-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from a task that contains one or more power channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-D

### DAQmx Read (Power 2D DBL NChan NSamp) VI

Reads one or more floating-point samples from a task that contains one or more power channel.

[IMAGE alt='icon' src='daqmx-read-power-2d-dbl-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-2d-i16-nchan-nsamp-vi.html language=enus -->
## TOPIC 02274: DAQmx Read (Power 2D I16 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-2d-i16-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-2d-i16-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 16-bit signed integer samples from a task that contains one or more power channels. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtu

### DAQmx Read (Power 2D I16 NChan NSamp) VI

Reads one or more unscaled 16-bit signed integer samples from a task that contains one or more power channels.

[IMAGE alt='icon' src='daqmx-read-power-2d-i16-nchan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-dbl-1chan-1samp-vi.html language=enus -->
## TOPIC 02275: DAQmx Read (Power DBL 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-dbl-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-dbl-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one floating-point sample from a task that contains a single power channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates

### DAQmx Read (Power DBL 1Chan 1Samp) VI

Reads one floating-point sample from a task that contains a single power channel.

[IMAGE alt='icon' src='daqmx-read-power-dbl-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-1samp-vi.html language=enus -->
## TOPIC 02276: DAQmx Read (Power Wfm 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform that contains a single floating-point sample from a task that contains a single power channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virt

### DAQmx Read (Power Wfm 1Chan 1Samp) VI

Reads a waveform that contains a single floating-point sample from a task that contains a single power channel.

[IMAGE alt='icon' src='daqmx-read-power-wfm-1chan-1samp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-nsamp-vi.html language=enus -->
## TOPIC 02277: DAQmx Read (Power Wfm 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform that contains one or more floating-point samples from a task that contains a single power channel. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of

### DAQmx Read (Power Wfm 1Chan NSamp) VI

Reads a waveform that contains one or more floating-point samples from a task that contains a single power channel.

[IMAGE alt='icon' src='daqmx-read-power-wfm-1chan-nsamp-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. voltage — voltage contains the read voltage value data. current — current contains the read current value data. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-property-node-vi.html language=enus -->
## TOPIC 02278: DAQmx Read Property Node

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-property-node-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the DAQmx Read class preselected. Right-click the Property Node and choose Select Filter from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in the system. ic

### DAQmx Read Property Node

A Property Node with the [DAQmx Read](/csh?context=nidaqmx_nidaq_daqmx_read_p) class preselected. Right-click the Property Node and choose **Select Filter** from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in the system.

[IMAGE alt='icon' src='daqmx-read-property-node-vi.png']

#### Inputs/Outputs

| task — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. error in (no error) — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. RelativeTo — RelativeTo is an example of a property you want to get (read) or set (write). task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx - Data Acquisition

Parent topic:

DAQmx Constants & Property Nodes

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i16-vi.html language=enus -->
## TOPIC 02279: DAQmx Read (Raw 1D I16) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i16-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 16-bit signed integer samples from a task. Use this instance with devices that use 16-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels

### DAQmx Read (Raw 1D I16) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 16-bit signed integer samples from a task. Use this instance with devices that use 16-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-i16-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 16-bit signed integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i32-vi.html language=enus -->
## TOPIC 02280: DAQmx Read (Raw 1D I32) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i32-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 32-bit signed integer samples from a task. Use this instance with devices that use 32-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels

### DAQmx Read (Raw 1D I32) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 32-bit signed integer samples from a task. Use this instance with devices that use 32-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-i32-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 32-bit signed integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i8-vi.html language=enus -->
## TOPIC 02281: DAQmx Read (Raw 1D I8) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i8-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 8-bit signed integer samples from a task. Use this instance with devices that use 8-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channels to

### DAQmx Read (Raw 1D I8) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 8-bit signed integer samples from a task. Use this instance with devices that use 8-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-i8-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 8-bit signed integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u16-vi.html language=enus -->
## TOPIC 02282: DAQmx Read (Raw 1D U16) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u16-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 16-bit unsigned integer samples from a task. Use this instance with devices that use 16-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual chann

### DAQmx Read (Raw 1D U16) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 16-bit unsigned integer samples from a task. Use this instance with devices that use 16-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-u16-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 16-bit unsigned integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u32-vi.html language=enus -->
## TOPIC 02283: DAQmx Read (Raw 1D U32) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u32-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 32-bit unsigned integer samples from a task. Use this instance with devices that use 32-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual chann

### DAQmx Read (Raw 1D U32) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 32-bit unsigned integer samples from a task. Use this instance with devices that use 32-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-u32-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 32-bit unsigned integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u8-vi.html language=enus -->
## TOPIC 02284: DAQmx Read (Raw 1D U8) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u8-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more raw, 8-bit unsigned integer samples from a task. Use this instance with devices that use 8-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cgenclassrntag.png task/channels in task/channels in is the name of the task or a list of virtual channel

### DAQmx Read (Raw 1D U8) VI

Reads one or more [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 8-bit unsigned integer samples from a task. Use this instance with devices that use 8-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-read-raw-1d-u8-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. number of samples per channel — number of samples per channel specifies the number of samples to read. If you leave this input unwired or set it to -1, NI-DAQmx determines how many samples to read based on if the task acquires samples continuously or acquires a finite number of samples. If the task acquires samples continuously and you set this input to -1, this VI reads all the samples currently available in the buffer. If the task acquires a finite number of samples and you set this input to -1, the VI waits for the task to acquire all requested samples, then reads those samples. If you set the Read All Available Samples property to TRUE, the VI reads the samples currently available in the buffer and does not wait for the task to acquire all requested samples. timeout — timeout specifies the amount of time in seconds to wait for samples to become available. If the time elapses, the VI returns an error and any samples read before the timeout elapsed. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read the requested samples and returns an error if it is unable to. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. data — data returns a 1D array of raw 8-bit unsigned integer samples. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Read VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/read-llb/daqmx-read-vi.html language=enus -->
## TOPIC 02285: DAQmx Read VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/read-llb/daqmx-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/read-llb/daqmx-read-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads samples from the task or virtual channels you specify. The instances of this polymorphic VI specify what format of samples to return, whether to read a single sample or multiple samples at once, and whether to read from one or multiple channels. The DAQmx Read properties include additional con

### DAQmx Read VI

Reads samples from the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) or [virtual channels](/csh?context=nidaqmx_mxcncpts_chans) you specify. The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) specify what format of samples to return, whether to read a single sample or multiple samples at once, and whether to read from one or multiple channels.

The [DAQmx Read](/csh?context=nidaqmx_nidaq_daqmx_read_p) properties include additional configuration options for read operations.

[IMAGE alt='icon' src='daqmx-read-vi.png']

- [DAQmx Read (Analog DBL 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-dbl-1chan-1samp-vi.html) Reads a single floating-point sample from a task that contains a single analog input channel .
- [DAQmx Read (Analog Wfm 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-wfm-1chan-1samp-vi.html) Reads a waveform that contains a single sample from a task that contains a single analog input channel .
- [DAQmx Read (Analog 1D DBL 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-1d-dbl-1chan-nsamp-vi.html) Reads one or more floating-point samples from a task that contains a single analog input channel .
- [DAQmx Read (Analog Wfm 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-wfm-1chan-nsamp-vi.html) Reads a waveform from a task that contains a single analog input channel .
- [DAQmx Read (Analog Wfm 1Chan NSamp Duration) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-wfm-1chan-nsamp-duration-vi.html) Reads a waveform from a task that contains a single analog input channel for a specified amount of time .
- [DAQmx Read (Analog 1D DBL NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-1d-dbl-nchan-1samp-vi.html) Reads a single floating-point sample from each channel in a task that contains one or more analog input channels .
- [DAQmx Read (Analog 1D Wfm NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-1d-wfm-nchan-1samp-vi.html) Reads a waveform that contains a single sample from each channel in a task that contains one or more analog input channels .
- [DAQmx Read (Analog 2D DBL NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-2d-dbl-nchan-nsamp-vi.html) Reads one or more floating-point samples from a task that contains one or more analog input channels .
- [DAQmx Read (Analog 1D Wfm NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-1d-wfm-nchan-nsamp-vi.html) Reads one or more waveforms from a task that contains one or more analog input channels .
- [DAQmx Read (Analog 1D Wfm NChan NSamp Duration) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-1d-wfm-nchan-nsamp-duration-vi.html) Reads one or more waveforms from a task that contains one or more analog input channels for a specified amount of time .
- [DAQmx Read (Analog 2D I16 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-2d-i16-nchan-nsamp-vi.html) Reads one or more unscaled 16-bit signed integer samples from a task that contains one or more analog input channels .
- [DAQmx Read (Analog 2D I32 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-2d-i32-nchan-nsamp-vi.html) Reads one or more unscaled 32-bit signed integer samples from a task that contains one or more analog input channels .
- [DAQmx Read (Analog 2D U16 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-2d-u16-nchan-nsamp-vi.html) Reads one or more unscaled 16-bit unsigned integer samples from a task that contains one or more analog input channels .
- [DAQmx Read (Analog 2D U32 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-analog-2d-u32-nchan-nsamp-vi.html) Reads one or more unscaled 32-bit unsigned integer samples from a task that contains one or more analog input channels .
- [DAQmx Read (Digital Bool 1Line 1Point) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-bool-1line-1point-vi.html) Reads a single Boolean sample from a task that contains a digital input channel composed of a single line.
- [DAQmx Read (Digital 1D Bool 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-bool-1chan-1samp-vi.html) Reads an array of Boolean values from a task that contains a single digital input channel .
- [DAQmx Read (Digital U8 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-u8-1chan-1samp-vi.html) Reads a single 8-bit unsigned integer sample from a task that contains a single digital input channel . Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Read (Digital U16 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-u16-1chan-1samp-vi.html) Reads a single 16-bit unsigned integer sample from a task that contains a single digital input channel . Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Read (Digital U32 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-u32-1chan-1samp-vi.html) Reads a single 32-bit unsigned integer sample from a task that contains a single digital input channel . Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Read (Digital Wfm 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-1samp-vi.html) Reads a digital waveform that contains a single sample from a task that contains a single digital input channel .
- [DAQmx Read (Digital 1D U8 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-1chan-nsamp-vi.html) Reads one or more 8-bit unsigned integer samples from a task that contains a single digital input channel . Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Read (Digital 1D U16 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u16-1chan-nsamp-vi.html) Reads one or more 16-bit unsigned integer samples from a task that contains a single digital input channel . Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Read (Digital 1D U32 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-1chan-nsamp-vi.html) Reads one or more 32-bit unsigned integer samples from a task that contains a single digital input channel . Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Read (Digital Wfm 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-vi.html) Reads a digital waveform from a task that contains a single digital input channel .
- [DAQmx Read (Digital Wfm 1Chan NSamp Duration) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-wfm-1chan-nsamp-duration-vi.html) Reads a digital waveform from a task that contains a single digital input channel for a specified amount of time .
- [DAQmx Read (Digital 1D Bool NChan 1Samp 1Line) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-bool-nchan-1samp-1line-vi.html) Reads a single Boolean sample from each channel in a task that contains one or more digital input channels . Each channel must contain only a single digital line.
- [DAQmx Read (Digital 2D Bool NChan 1Samp NLine) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-2d-bool-nchan-1samp-nline-vi.html) Reads a single sample that contains Boolean values from each channel in a task that contains one or more digital input channels . Each channel can contain multiple digital lines.
- [DAQmx Read (Digital 1D U8 NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u8-nchan-1samp-vi.html) Reads a single 8-bit unsigned integer sample from each channel in a task that contains one or more digital input channels . Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Read (Digital 1D U16 NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u16-nchan-1samp-vi.html) Reads a single 16-bit unsigned integer sample from each channel in a task that contains one or more digital input channels . Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Read (Digital 1D U32 NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-u32-nchan-1samp-vi.html) Reads a single 32-bit unsigned integer sample from each channel in a task that contains one or more digital input channels . Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Read (Digital 1D Wfm NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-1samp-vi.html) Reads a waveform that contains a single sample from each channel in a task that contains one or more digital input channels .
- [DAQmx Read (Digital 2D U8 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u8-nchan-nsamp-vi.html) Reads one or more 8-bit unsigned integer samples from a task that contains one or more digital input channels . Use an instance that reads 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Read (Digital 2D U16 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u16-nchan-nsamp-vi.html) Reads one or more 16-bit unsigned integer samples from a task that contains one or more digital input channels . Use an instance that reads 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Read (Digital 2D U32 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-2d-u32-nchan-nsamp-vi.html) Reads one or more 32-bit unsigned integer samples from a task that contains one or more digital input channels . Use an instance that reads 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Read (Digital 1D Wfm NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-vi.html) Reads one or more digital waveforms from a task that contains one or more digital input channels .
- [DAQmx Read (Digital 1D Wfm NChan NSamp Duration) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-digital-1d-wfm-nchan-nsamp-duration-vi.html) Reads one or more digital waveforms from a task that contains one or more digital input channels for a specified amount of time .
- [DAQmx Read (Counter DBL 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-dbl-1chan-1samp-vi.html) Reads a single floating-point sample from a counter task. Use an instance that reads floating-point values when NI-DAQmx scales counter samples to a floating-point value, such as for frequency and period measurement.
- [DAQmx Read (Counter U32 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-u32-1chan-1samp-vi.html) Reads a 32-bit unsigned integer sample from a counter task. Use an instance that reads 32-bit unsigned integers when NI-DAQmx returns counter samples unscaled, such as for event counting.
- [DAQmx Read (Counter Pulse Freq 1 Chan 1 Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-pulse-freq-1-chan-1-samp-vi.html) Reads a single pair of pulse frequency and duty cycle from a counter input task.
- [DAQmx Read (Counter Pulse Time 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-pulse-time-1chan-1samp-vi.html) Reads a single pair of pulse high and low times from a counter input task.
- [DAQmx Read (Counter Pulse Ticks 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-pulse-ticks-1chan-1samp-vi.html) Reads a single pair of pulse high and low tick counts from a counter input task.
- [DAQmx Read (Counter 1D DBL 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-dbl-1chan-nsamp-vi.html) Reads one or more floating-point samples from a counter task. Use an instance that reads a floating-point value when NI-DAQmx scales counter samples to a floating-point value, such as for frequency and period measurement.
- [DAQmx Read (Counter 1D U32 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-u32-1chan-nsamp-vi.html) Reads one or more 32-bit unsigned integer samples from a counter task. Use an instance that reads 32-bit unsigned integers when NI-DAQmx returns counter samples unscaled, such as for event counting.
- [DAQmx Read (Counter 1D Pulse Freq 1 Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-pulse-freq-1-chan-nsamp-vi.html) Reads one or more pairs of pulse frequency and duty cycle from a counter input task.
- [DAQmx Read (Counter 1D Pulse Time 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-pulse-time-1chan-nsamp-vi.html) Reads one or more pairs of pulse high and low times from a counter input task.
- [DAQmx Read (Counter 1D Pulse Ticks 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-pulse-ticks-1chan-nsamp-vi.html) Reads one or more pairs of pulse high and low tick counts from a counter input task.
- [DAQmx Read (Counter 1D DBL NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-dbl-nchan-1samp-vi.html) Reads one floating-point sample from one or more counter tasks. Use an instance that reads a floating-point value when NI-DAQmx scales counter samples to a floating-point value.
- [DAQmx Read (Counter 1D U32 NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-1d-u32-nchan-1samp-vi.html) Reads an unscaled 32-bit unsigned integer sample from one or more counter tasks.
- [DAQmx Read (Counter 2D DBL NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-2d-dbl-nchan-nsamp-vi.html) Reads one or more floating-point samples from one or more counter tasks. Use an instance that reads a floating-point value when NI-DAQmx scales counter samples to a floating-point value.
- [DAQmx Read (Counter 2D U32 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-counter-2d-u32-nchan-nsamp-vi.html) Reads one or more unscaled 32-bit unsigned integer samples from one or more counter tasks.
- [DAQmx Read (Power DBL 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-dbl-1chan-1samp-vi.html) Reads one floating-point sample from a task that contains a single power channel.
- [DAQmx Read (Power Wfm 1Chan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-1samp-vi.html) Reads a waveform that contains a single floating-point sample from a task that contains a single power channel.
- [DAQmx Read (Power 1D DBL 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-1chan-nsamp-vi.html) Reads one or more floating-point samples from a task that contains a single power channel.
- [DAQmx Read (Power Wfm 1Chan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-wfm-1chan-nsamp-vi.html) Reads a waveform that contains one or more floating-point samples from a task that contains a single power channel.
- [DAQmx Read (Power 1D DBL NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-1d-dbl-nchan-1samp-vi.html) Reads one floating-point sample from a task that contains one or more power channels.
- [DAQmx Read (Power 1D Wfm NChan 1Samp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-1samp-vi.html) Reads a waveform that contains a single floating-point sample from each channel in a task that contains one or more power channels.
- [DAQmx Read (Power 2D DBL NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-2d-dbl-nchan-nsamp-vi.html) Reads one or more floating-point samples from a task that contains one or more power channel.
- [DAQmx Read (Power 1D Wfm NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-1d-wfm-nchan-nsamp-vi.html) Reads one or more waveforms that contains one or more floating-point samples from a task that contains one or more power channels.
- [DAQmx Read (Power 2D I16 NChan NSamp) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-power-2d-i16-nchan-nsamp-vi.html) Reads one or more unscaled 16-bit signed integer samples from a task that contains one or more power channels.
- [DAQmx Read (Raw 1D U8) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u8-vi.html) Reads one or more raw , 8-bit unsigned integer samples from a task. Use this instance with devices that use 8-bit unsigned integers as the internal representation of a sample.
- [DAQmx Read (Raw 1D U16) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u16-vi.html) Reads one or more raw , 16-bit unsigned integer samples from a task. Use this instance with devices that use 16-bit unsigned integers as the internal representation of a sample.
- [DAQmx Read (Raw 1D U32) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-u32-vi.html) Reads one or more raw , 32-bit unsigned integer samples from a task. Use this instance with devices that use 32-bit unsigned integers as the internal representation of a sample.
- [DAQmx Read (Raw 1D I8) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i8-vi.html) Reads one or more raw , 8-bit signed integer samples from a task. Use this instance with devices that use 8-bit signed integers as the internal representation of a sample.
- [DAQmx Read (Raw 1D I16) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i16-vi.html) Reads one or more raw , 16-bit signed integer samples from a task. Use this instance with devices that use 16-bit signed integers as the internal representation of a sample.
- [DAQmx Read (Raw 1D I32) VI](../../../vi-lib/daqmx/read-llb/daqmx-read-raw-1d-i32-vi.html) Reads one or more raw , 32-bit signed integer samples from a task. Use this instance with devices that use 32-bit signed integers as the internal representation of a sample.

Parent topic:

DAQmx - Data Acquisition

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-1chan-nsamp-vi.html language=enus -->
## TOPIC 02286: DAQmx Write (Analog 1D DBL 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more floating-point samples to a task that contains a single analog output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels i

### DAQmx Write (Analog 1D DBL 1Chan NSamp) VI

Writes one or more floating-point samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [analog output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-1d-dbl-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of samples to write to the task. Each element of the array corresponds to a sample to write. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-nchan-1samp-vi.html language=enus -->
## TOPIC 02287: DAQmx Write (Analog 1D DBL NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single floating-point sample to each channel in a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png

### DAQmx Write (Analog 1D DBL NChan 1Samp) VI

Writes a single floating-point sample to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-1d-dbl-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-1samp-vi.html language=enus -->
## TOPIC 02288: DAQmx Write (Analog 1D Wfm NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a waveform that contains a single sample to each channel in a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclas

### DAQmx Write (Analog 1D Wfm NChan 1Samp) VI

Writes a waveform that contains a single sample to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-1d-wfm-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of waveforms to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-nsamp-vi.html language=enus -->
## TOPIC 02289: DAQmx Write (Analog 1D Wfm NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more waveforms to a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels in task/ch

### DAQmx Write (Analog 1D Wfm NChan NSamp) VI

Writes one or more waveforms to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-1d-wfm-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of waveforms to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-2d-dbl-nchan-nsamp-vi.html language=enus -->
## TOPIC 02290: DAQmx Write (Analog 2D DBL NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-2d-dbl-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-2d-dbl-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more floating-point samples to a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channe

### DAQmx Write (Analog 2D DBL NChan NSamp) VI

Writes one or more floating-point samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-2d-dbl-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i16-nchan-nsamp-vi.html language=enus -->
## TOPIC 02291: DAQmx Write (Analog 2D I16 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i16-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i16-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled, 16-bit signed integer samples to a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrnta

### DAQmx Write (Analog 2D I16 NChan NSamp) VI

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata), 16-bit signed integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-2d-i16-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 16-bit signed integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i32-nchan-nsamp-vi.html language=enus -->
## TOPIC 02292: DAQmx Write (Analog 2D I32 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i32-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i32-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled, 32-bit signed integer samples to a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrnta

### DAQmx Write (Analog 2D I32 NChan NSamp) VI

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata), 32-bit signed integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-2d-i32-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 32-bit signed integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-2d-u16-nchan-nsamp-vi.html language=enus -->
## TOPIC 02293: DAQmx Write (Analog 2D U16 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-2d-u16-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-2d-u16-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled 16-bit unsigned integer samples to a task that contains one or more analog output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrnt

### DAQmx Write (Analog 2D U16 NChan NSamp) VI

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [analog output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-2d-u16-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 16-bit unsigned integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-dbl-1chan-1samp-vi.html language=enus -->
## TOPIC 02294: DAQmx Write (Analog DBL 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-dbl-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-dbl-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a floating-point sample to a task that contains a single analog output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels in task/chan

### DAQmx Write (Analog DBL 1Chan 1Samp) VI

Writes a floating-point sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [analog output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-dbl-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a sample to write to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-1samp-vi.html language=enus -->
## TOPIC 02295: DAQmx Write (Analog Wfm 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a waveform that contains a single sample to a task that contains a single analog output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/chan

### DAQmx Write (Analog Wfm 1Chan 1Samp) VI

Writes a waveform that contains a single sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [analog output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-wfm-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a waveform to write to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-nsamp-vi.html language=enus -->
## TOPIC 02296: DAQmx Write (Analog Wfm 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a waveform to a task that contains a single analog output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels in task/channels in is th

### DAQmx Write (Analog Wfm 1Chan NSamp) VI

Writes a waveform to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [analog output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-analog-wfm-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a waveform to write to the task. The data you write must be in the units of the generation, including any custom scales. Use the DAQmx Create Virtual Channel VI or the DAQ Assistant to specify these units. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-1chan-nsamp-vi.html language=enus -->
## TOPIC 02297: DAQmx Write (Counter 1D Frequency 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes new pulse frequency and duty cycle pairs to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/cha

### DAQmx Write (Counter 1D Frequency 1Chan NSamp) VI

Writes new pulse frequency and duty cycle pairs to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-1d-frequency-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse frequency and duty cycle pairs to write. Each element of the array corresponds to a sample to write. duty cycle — duty cycle is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses. frequency — frequency specifies at what frequency to generate pulses. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| duty cycle — duty cycle is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses. frequency — frequency specifies at what frequency to generate pulses. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-nchan-1samp-vi.html language=enus -->
## TOPIC 02298: DAQmx Write (Counter 1D Frequency NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a new pulse frequency and duty cycle to each channel in a counter output task that contains one or more channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrn

### DAQmx Write (Counter 1D Frequency NChan 1Samp) VI

Writes a new pulse frequency and duty cycle to each channel in a counter output task that contains one or more channels.

[IMAGE alt='icon' src='daqmx-write-counter-1d-frequency-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse frequency and duty cycle to write. Each element of the array corresponds to a channel in the task. duty cycle — duty cycle is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses. frequency — frequency specifies at what frequency to generate pulses. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| duty cycle — duty cycle is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses. frequency — frequency specifies at what frequency to generate pulses. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1d-ticks-1chan-nsamp-vi.html language=enus -->
## TOPIC 02299: DAQmx Write (Counter 1D Ticks 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1d-ticks-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1d-ticks-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes new pulse high tick counts and low tick counts to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png ta

### DAQmx Write (Counter 1D Ticks 1Chan NSamp) VI

Writes new pulse high tick counts and low tick counts to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-1d-ticks-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse high ticks and low ticks to write to the task. Each element of the array corresponds to a channel in the task. high ticks — high ticks is the number of ticks the pulse is high. low ticks — low ticks is the number of ticks the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| high ticks — high ticks is the number of ticks the pulse is high. low ticks — low ticks is the number of ticks the pulse is low. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-1chan-nsamp-vi.html language=enus -->
## TOPIC 02300: DAQmx Write (Counter 1D Time 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes new pulse high times and low times to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels

### DAQmx Write (Counter 1D Time 1Chan NSamp) VI

Writes new pulse high times and low times to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-1d-time-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse high times and low times to write to the task. Each element of the array corresponds to a sample to write. high time — high time is the amount of time the pulse is high. low time — low time is the amount of time the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| high time — high time is the amount of time the pulse is high. low time — low time is the amount of time the pulse is low. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-nchan-1samp-vi.html language=enus -->
## TOPIC 02301: DAQmx Write (Counter 1D Time NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a new pulse high time and low time to each channel in a counter output task that contains one or more channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrnta

### DAQmx Write (Counter 1D Time NChan 1Samp) VI

Writes a new pulse high time and low time to each channel in a counter output task that contains one or more channels.

[IMAGE alt='icon' src='daqmx-write-counter-1d-time-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse high time and low time to write to the task. Each element of the array corresponds to a channel in the task. high time — high time is the amount of time the pulse is high. low time — low time is the amount of time the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| high time — high time is the amount of time the pulse is high. low time — low time is the amount of time the pulse is low. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-1dticks-nchan-1samp-vi.html language=enus -->
## TOPIC 02302: DAQmx Write (Counter 1DTicks NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-1dticks-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-1dticks-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes new pulse high tick counts and low tick counts to each channel in a counter output task that contains one or more channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. c

### DAQmx Write (Counter 1DTicks NChan 1Samp) VI

Writes new pulse high tick counts and low tick counts to each channel in a counter output task that contains one or more channels.

[IMAGE alt='icon' src='daqmx-write-counter-1dticks-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains the pulse high ticks and low ticks to write to the task. Each element of the array corresponds to a channel in the task. high ticks — high ticks is the number of ticks the pulse is high. low ticks — low ticks is the number of ticks the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| high ticks — high ticks is the number of ticks the pulse is high. low ticks — low ticks is the number of ticks the pulse is low. |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-frequency-1chan-1samp-vi.html language=enus -->
## TOPIC 02303: DAQmx Write (Counter Frequency 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-frequency-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-frequency-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a new pulse frequency and duty cycle to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channel

### DAQmx Write (Counter Frequency 1Chan 1Samp) VI

Writes a new pulse frequency and duty cycle to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-frequency-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. frequency — frequency specifies at what frequency to generate pulses. duty cycle — duty cycle is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-ticks-1chan-1samp-vi.html language=enus -->
## TOPIC 02304: DAQmx Write (Counter Ticks 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-ticks-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-ticks-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a new pulse high tick count and low tick count to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png ta

### DAQmx Write (Counter Ticks 1Chan 1Samp) VI

Writes a new pulse high tick count and low tick count to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-ticks-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. high ticks — high ticks is the number of ticks the pulse is high. low ticks — low ticks is the number of ticks the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-counter-time-1chan-1samp-vi.html language=enus -->
## TOPIC 02305: DAQmx Write (Counter Time 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-counter-time-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-counter-time-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a new pulse high time and low time to a counter output task that contains a single channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels

### DAQmx Write (Counter Time 1Chan 1Samp) VI

Writes a new pulse high time and low time to a counter output task that contains a single channel.

[IMAGE alt='icon' src='daqmx-write-counter-time-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. high time — high time is the amount of time the pulse is high. low time — low time is the amount of time the pulse is low. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-1chan-1samp-vi.html language=enus -->
## TOPIC 02306: DAQmx Write (Digital 1D Bool 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single sample of Boolean values to a task that contains a single digital output channel. The channel can contain one or more digital lines. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQm

### DAQmx Write (Digital 1D Bool 1Chan 1Samp) VI

Writes a single sample of Boolean values to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). The channel can contain one or more digital lines.

[IMAGE alt='icon' src='daqmx-write-digital-1d-bool-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of Boolean values to write to the task. Each element of the array corresponds to a digital line within the channel. The order of the lines in the array corresponds to the order in which you add the lines to the channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-nchan-1samp-1line-vi.html language=enus -->
## TOPIC 02307: DAQmx Write (Digital 1D Bool NChan 1Samp 1Line) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-nchan-1samp-1line-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-nchan-1samp-1line-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single sample of Boolean values to each channel in a task that contains multiple digital output channels. Each channel in the task can contain only one digital line. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explici

### DAQmx Write (Digital 1D Bool NChan 1Samp 1Line) VI

Writes a single sample of Boolean values to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains multiple [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Each channel in the task can contain only one digital line.

[IMAGE alt='icon' src='daqmx-write-digital-1d-bool-nchan-1samp-1line-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of Boolean samples to write to the task. Each element of the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-1chan-nsamp-vi.html language=enus -->
## TOPIC 02308: DAQmx Write (Digital 1D U16 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit unsigned integer samples to a task that contains a single digital output channel. Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the

### DAQmx Write (Digital 1D U16 1Chan NSamp) VI

Writes one or more 16-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u16-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a point of data to write to the channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-nchan-1samp-vi.html language=enus -->
## TOPIC 02309: DAQmx Write (Digital 1D U16 NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 16-bit unsigned integer sample to a task that contains one or more digital output channels. Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the

### DAQmx Write (Digital 1D U16 NChan 1Samp) VI

Writes a single 16-bit unsigned integer sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u16-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-1chan-nsamp-vi.html language=enus -->
## TOPIC 02310: DAQmx Write (Digital 1D U32 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit unsigned integer samples to a task that contains a single digital output channel. Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the

### DAQmx Write (Digital 1D U32 1Chan NSamp) VI

Writes one or more 32-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u32-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a point of data to write to the channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-nchan-1samp-vi.html language=enus -->
## TOPIC 02311: DAQmx Write (Digital 1D U32 NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit unsigned integer sample to a task that contains one or more digital output channels. Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the

### DAQmx Write (Digital 1D U32 NChan 1Samp) VI

Writes a single 32-bit unsigned integer sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u32-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-1chan-nsamp-vi.html language=enus -->
## TOPIC 02312: DAQmx Write (Digital 1D U8 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 8-bit unsigned integer samples to a task that contains a single digital output channel. Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts th

### DAQmx Write (Digital 1D U8 1Chan NSamp) VI

Writes one or more 8-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u8-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a point of data to write. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-nchan-1samp-vi.html language=enus -->
## TOPIC 02313: DAQmx Write (Digital 1D U8 NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 8-bit unsigned integer sample to each channel in a task that contains one or more digital output channels. Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automat

### DAQmx Write (Digital 1D U8 NChan 1Samp) VI

Writes a single 8-bit unsigned integer sample to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-1d-u8-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-1samp-vi.html language=enus -->
## TOPIC 02314: DAQmx Write (Digital 1D Wfm NChan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a digital waveform that contains a single sample to each channel in a task that contains one or more digital output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI.

### DAQmx Write (Digital 1D Wfm NChan 1Samp) VI

Writes a digital waveform that contains a single sample to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-digital-1d-wfm-nchan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of waveforms to write to the task. Each element in the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-nsamp-vi.html language=enus -->
## TOPIC 02315: DAQmx Write (Digital 1D Wfm NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more digital waveforms to a task that contains one or more digital output channels. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels i

### DAQmx Write (Digital 1D Wfm NChan NSamp) VI

Writes one or more digital waveforms to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels.](/csh?context=nidaqmx_mxcncpts_virtchantypes)

[IMAGE alt='icon' src='daqmx-write-digital-1d-wfm-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of waveforms to write to the task. Each element in the array corresponds to a channel in the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-2d-bool-nchan-1samp-nline-vi.html language=enus -->
## TOPIC 02316: DAQmx Write (Digital 2D Bool NChan 1Samp NLine) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-2d-bool-nchan-1samp-nline-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-2d-bool-nchan-1samp-nline-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single sample of Boolean values to each channel in a task that contains one or more digital output channels. The channels can contain one or more digital lines. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly s

### DAQmx Write (Digital 2D Bool NChan 1Samp NLine) VI

Writes a single sample of Boolean values to each channel in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). The channels can contain one or more digital lines.

[IMAGE alt='icon' src='daqmx-write-digital-2d-bool-nchan-1samp-nline-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of Boolean samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u16-nchan-nsamp-vi.html language=enus -->
## TOPIC 02317: DAQmx Write (Digital 2D U16 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u16-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u16-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit unsigned integer samples to a task that contains one or more digital output channels. Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts

### DAQmx Write (Digital 2D U16 NChan NSamp) VI

Writes one or more 16-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-2d-u16-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 16-bit unsigned integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u32-nchan-nsamp-vi.html language=enus -->
## TOPIC 02318: DAQmx Write (Digital 2D U32 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u32-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u32-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit unsigned integer samples to a task that contains one or more digital output channels. Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts

### DAQmx Write (Digital 2D U32 NChan NSamp) VI

Writes one or more 32-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-2d-u32-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 32-bit unsigned integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u8-nchan-nsamp-vi.html language=enus -->
## TOPIC 02319: DAQmx Write (Digital 2D U8 NChan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u8-nchan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u8-nchan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 8-bit unsigned integer samples to a task that contains one or more digital output channels. Use an instance that writes 8-bit unsigned integers for devices that have up to eight lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically

### DAQmx Write (Digital 2D U8 NChan NSamp) VI

Writes one or more 8-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains one or more [digital output channels](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 8-bit unsigned integers for devices that have up to eight lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-2d-u8-nchan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 2D array of 8-bit unsigned integer samples to write to the task. Each row corresponds to a channel in the task. Each column corresponds to a sample to write to each channel. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-bool-1line-1point-vi.html language=enus -->
## TOPIC 02320: DAQmx Write (Digital Bool 1Line 1Point) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-bool-1line-1point-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-bool-1line-1point-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single Boolean sample to a task that contains a digital output channel composed of a single line. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/c

### DAQmx Write (Digital Bool 1Line 1Point) VI

Writes a single Boolean sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes) composed of a single line.

[IMAGE alt='icon' src='daqmx-write-digital-bool-1line-1point-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a Boolean sample to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-u16-1chan-1samp-vi.html language=enus -->
## TOPIC 02321: DAQmx Write (Digital U16 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-u16-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-u16-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 16-bit unsigned integer sample to a task that contains a single digital output channel. Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the tas

### DAQmx Write (Digital U16 1Chan 1Samp) VI

Writes a single 16-bit unsigned integer sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-u16-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains an 16-bit unsigned integer sample to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-u32-1chan-1samp-vi.html language=enus -->
## TOPIC 02322: DAQmx Write (Digital U32 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-u32-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-u32-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit unsigned integer sample to a task that contains a single digital output channel. Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the tas

### DAQmx Write (Digital U32 1Chan 1Samp) VI

Writes a single 32-bit unsigned integer sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-u32-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 32-bit unsigned integer sample to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-u8-1chan-1samp-vi.html language=enus -->
## TOPIC 02323: DAQmx Write (Digital U8 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-u8-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-u8-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 8-bit unsigned integer sample to a task that contains a single digital output channel. Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the ta

### DAQmx Write (Digital U8 1Chan 1Samp) VI

Writes a single 8-bit unsigned integer sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes). Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.

[IMAGE alt='icon' src='daqmx-write-digital-u8-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains an 8-bit unsigned integer sample to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-1samp-vi.html language=enus -->
## TOPIC 02324: DAQmx Write (Digital Wfm 1Chan 1Samp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-1samp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-1samp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a digital waveform that contains a single sample to a task that contains a single digital output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png

### DAQmx Write (Digital Wfm 1Chan 1Samp) VI

Writes a digital waveform that contains a single sample to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-digital-wfm-1chan-1samp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a digital waveform to write to the task. The data is written in the order that the lines are added to the task. The most significant bit is the first line added, and the least significant bit is the last line added. Therefore, if the data you specify to write is 110, and the line order you specify is Dev1/port0/line0:2, the output is: Dev1/port0/line0 1 Dev1/port0/line1 1 Dev1/port0/line2 0 If the data you specify to write is 110 and the line order you specify is Dev1/port0/line2:0, the output is: Dev1/port0/line0 0 Dev1/port0/line1 1 Dev1/port0/line2 1 timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Dev1/port0/line0 | 1 |
| Dev1/port0/line1 | 1 |
| Dev1/port0/line2 | 0 |
| Dev1/port0/line0 | 0 |
| Dev1/port0/line1 | 1 |
| Dev1/port0/line2 | 1 |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-nsamp-vi.html language=enus -->
## TOPIC 02325: DAQmx Write (Digital Wfm 1Chan NSamp) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-nsamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-nsamp-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a digital waveform to a task that contains a single digital output channel. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. cgenclassrntag.png task/channels in task/channels

### DAQmx Write (Digital Wfm 1Chan NSamp) VI

Writes a digital waveform to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that contains a single [digital output channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

[IMAGE alt='icon' src='daqmx-write-digital-wfm-1chan-nsamp-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a digital waveform to write to the task. The data is written in the order that the lines are added to the task. The most significant bit is the first line added, and the least significant bit is the last line added. Therefore, if the data you specify to write is 110, and the line order you specify is Dev1/port0/line0:2, the output is: Dev1/port0/line0 1 Dev1/port0/line1 1 Dev1/port0/line2 0 If the data you specify to write is 110 and the line order you specify is Dev1/port0/line2:0, the output is: Dev1/port0/line0 0 Dev1/port0/line1 1 Dev1/port0/line2 1 timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Dev1/port0/line0 | 1 |
| Dev1/port0/line1 | 1 |
| Dev1/port0/line2 | 0 |
| Dev1/port0/line0 | 0 |
| Dev1/port0/line1 | 1 |
| Dev1/port0/line2 | 1 |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-property-node-vi.html language=enus -->
## TOPIC 02326: DAQmx Write Property Node

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-property-node-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the DAQmx Write class preselected. Right-click the Property Node and choose Select Filter from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in the system. i

### DAQmx Write Property Node

A Property Node with the [DAQmx Write](/csh?context=nidaqmx_nidaq_daqmx_write_p) class preselected. Right-click the Property Node and choose **Select Filter** from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in the system.

[IMAGE alt='icon' src='daqmx-write-property-node-vi.png']

#### Inputs/Outputs

| task — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. error in (no error) — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Relative To — RelativeTo is an example of a property you want to get (read) or set (write). task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx - Data Acquisition

Parent topic:

DAQmx Constants & Property Nodes

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i16-vi.html language=enus -->
## TOPIC 02327: DAQmx Write (Raw 1D I16) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i16-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 16-bit signed integer samples to a task. Use this instance for devices that use 16-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly sta

### DAQmx Write (Raw 1D I16) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 16-bit signed integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 16-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-i16-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i32-vi.html language=enus -->
## TOPIC 02328: DAQmx Write (Raw 1D I32) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i32-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 32-bit signed integer samples to a task. Use this instance for devices that use 32-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly sta

### DAQmx Write (Raw 1D I32) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 32-bit signed integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 32-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-i32-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i8-vi.html language=enus -->
## TOPIC 02329: DAQmx Write (Raw 1D I8) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i8-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 8-bit signed integer samples to a task. Use this instance for devices that use 8-bit signed integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly start

### DAQmx Write (Raw 1D I8) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 8-bit signed integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 8-bit signed integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-i8-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u16-vi.html language=enus -->
## TOPIC 02330: DAQmx Write (Raw 1D U16) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u16-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 16-bit unsigned integer samples to a task. Use this instance for devices that use 16-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly

### DAQmx Write (Raw 1D U16) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 16-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 16-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-u16-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u32-vi.html language=enus -->
## TOPIC 02331: DAQmx Write (Raw 1D U32) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u32-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 32-bit unsigned integer samples to a task. Use this instance for devices that use 32-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly

### DAQmx Write (Raw 1D U32) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 32-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 32-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-u32-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u8-vi.html language=enus -->
## TOPIC 02332: DAQmx Write (Raw 1D U8) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u8-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes multiple raw, 8-bit unsigned integer samples to a task. Use this instance for devices that use 8-bit unsigned integers as the internal representation of a sample. icon Inputs/Outputs cbool.png auto start auto start specifies if this VI automatically starts the task if you did not explicitly s

### DAQmx Write (Raw 1D U8) VI

Writes multiple [raw](/csh?context=nidaqmx_mxcncpts_rawdata), 8-bit unsigned integer samples to a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). Use this instance for devices that use 8-bit unsigned integers as the internal representation of a sample.

[IMAGE alt='icon' src='daqmx-write-raw-1d-u8-vi.png']

#### Inputs/Outputs

| auto start — auto start specifies if this VI automatically starts the task if you did not explicitly start it with the DAQmx Start Task VI. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. data — data contains a 1D array of raw samples to write to the task. timeout — timeout specifies the amount of time in seconds to wait for the VI to write all samples. NI-DAQmx performs a timeout check only if the VI must wait before it writes data. This VI returns an error if the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to write the submitted samples. If the VI could not write all the submitted samples, it returns an error and the number of samples successfully written in the number of samples written per channel output. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. number of samples written per channel — number of samples written per channel is the actual number of samples this VI successfully wrote to each channel in the task. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Write VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/write-llb/daqmx-write-vi.html language=enus -->
## TOPIC 02333: DAQmx Write VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/write-llb/daqmx-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/write-llb/daqmx-write-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes samples to the task or virtual channels you specify. The instances of this polymorphic VI specify the format of the samples to write, whether to write one or multiple samples, and whether to write to one or multiple channels. If the task uses on-demand timing, this VI returns only after the d

### DAQmx Write VI

Writes samples to the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) or [virtual channels](/csh?context=nidaqmx_mxcncpts_chans) you specify. The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) specify the format of the samples to write, whether to write one or multiple samples, and whether to write to one or multiple channels.

If the task uses on-demand timing, this VI returns only after the device generates all samples. On-demand is the default timing type if you do not use the [DAQmx Timing](/csh?context=nidaqmx_lvdaqmx_mxtiming) VI. If the task uses any timing type other than on-demand, this VI returns immediately and does not wait for the device to generate all samples. Your application must determine if the task is done to ensure that the device generated all samples.

The [DAQmx Write](/csh?context=nidaqmx_nidaq_daqmx_write_p) properties include additional configuration options for write operations.

[IMAGE alt='icon' src='daqmx-write-vi.png']

- [DAQmx Write (Analog DBL 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-dbl-1chan-1samp-vi.html) Writes a floating-point sample to a task that contains a single analog output channel .
- [DAQmx Write (Analog Wfm 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-1samp-vi.html) Writes a waveform that contains a single sample to a task that contains a single analog output channel .
- [DAQmx Write (Analog 1D DBL 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-1chan-nsamp-vi.html) Writes one or more floating-point samples to a task that contains a single analog output channel .
- [DAQmx Write (Analog Wfm 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-wfm-1chan-nsamp-vi.html) Writes a waveform to a task that contains a single analog output channel .
- [DAQmx Write (Analog 1D DBL NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-1d-dbl-nchan-1samp-vi.html) Writes a single floating-point sample to each channel in a task that contains one or more analog output channels .
- [DAQmx Write (Analog 1D Wfm NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-1samp-vi.html) Writes a waveform that contains a single sample to each channel in a task that contains one or more analog output channels .
- [DAQmx Write (Analog 2D DBL NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-2d-dbl-nchan-nsamp-vi.html) Writes one or more floating-point samples to a task that contains one or more analog output channels .
- [DAQmx Write (Analog 1D Wfm NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-1d-wfm-nchan-nsamp-vi.html) Writes one or more waveforms to a task that contains one or more analog output channels .
- [DAQmx Write (Analog 2D I16 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i16-nchan-nsamp-vi.html) Writes one or more unscaled , 16-bit signed integer samples to a task that contains one or more analog output channels .
- [DAQmx Write (Analog 2D I32 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-2d-i32-nchan-nsamp-vi.html) Writes one or more unscaled , 32-bit signed integer samples to a task that contains one or more analog output channels .
- [DAQmx Write (Analog 2D U16 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-analog-2d-u16-nchan-nsamp-vi.html) Writes one or more unscaled 16-bit unsigned integer samples to a task that contains one or more analog output channels .
- [DAQmx Write (Digital Bool 1Line 1Point) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-bool-1line-1point-vi.html) Writes a single Boolean sample to a task that contains a digital output channel composed of a single line.
- [DAQmx Write (Digital 1D Bool 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-1chan-1samp-vi.html) Writes a single sample of Boolean values to a task that contains a single digital output channel . The channel can contain one or more digital lines.
- [DAQmx Write (Digital U8 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-u8-1chan-1samp-vi.html) Writes a single 8-bit unsigned integer sample to a task that contains a single digital output channel . Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Write (Digital U16 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-u16-1chan-1samp-vi.html) Writes a single 16-bit unsigned integer sample to a task that contains a single digital output channel . Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Write (Digital U32 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-u32-1chan-1samp-vi.html) Writes a single 32-bit unsigned integer sample to a task that contains a single digital output channel . Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Write (Digital Wfm 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-1samp-vi.html) Writes a digital waveform that contains a single sample to a task that contains a single digital output channel .
- [DAQmx Write (Digital 1D U8 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-1chan-nsamp-vi.html) Writes one or more 8-bit unsigned integer samples to a task that contains a single digital output channel . Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Write (Digital 1D U16 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-1chan-nsamp-vi.html) Writes one or more 16-bit unsigned integer samples to a task that contains a single digital output channel . Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Write (Digital 1D U32 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-1chan-nsamp-vi.html) Writes one or more 32-bit unsigned integer samples to a task that contains a single digital output channel . Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Write (Digital Wfm 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-wfm-1chan-nsamp-vi.html) Writes a digital waveform to a task that contains a single digital output channel .
- [DAQmx Write (Digital 1D Bool NChan 1Samp 1Line) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-bool-nchan-1samp-1line-vi.html) Writes a single sample of Boolean values to each channel in a task that contains multiple digital output channels . Each channel in the task can contain only one digital line.
- [DAQmx Write (Digital 2D Bool NChan 1Samp NLine) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-2d-bool-nchan-1samp-nline-vi.html) Writes a single sample of Boolean values to each channel in a task that contains one or more digital output channels . The channels can contain one or more digital lines.
- [DAQmx Write (Digital 1D U8 NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u8-nchan-1samp-vi.html) Writes a single 8-bit unsigned integer sample to each channel in a task that contains one or more digital output channels . Use an instance that writes 8-bit unsigned integers for devices with up to eight lines per port.
- [DAQmx Write (Digital 1D U16 NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u16-nchan-1samp-vi.html) Writes a single 16-bit unsigned integer sample to a task that contains one or more digital output channels . Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Write (Digital 1D U32 NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-u32-nchan-1samp-vi.html) Writes a single 32-bit unsigned integer sample to a task that contains one or more digital output channels . Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Write (Digital 1D Wfm NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-1samp-vi.html) Writes a digital waveform that contains a single sample to each channel in a task that contains one or more digital output channels .
- [DAQmx Write (Digital 2D U8 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u8-nchan-nsamp-vi.html) Writes one or more 8-bit unsigned integer samples to a task that contains one or more digital output channels . Use an instance that writes 8-bit unsigned integers for devices that have up to eight lines per port.
- [DAQmx Write (Digital 2D U16 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u16-nchan-nsamp-vi.html) Writes one or more 16-bit unsigned integer samples to a task that contains one or more digital output channels . Use an instance that writes 16-bit unsigned integers for devices with up to 16 lines per port.
- [DAQmx Write (Digital 2D U32 NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-2d-u32-nchan-nsamp-vi.html) Writes one or more 32-bit unsigned integer samples to a task that contains one or more digital output channels . Use an instance that writes 32-bit unsigned integers for devices with up to 32 lines per port.
- [DAQmx Write (Digital 1D Wfm NChan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-digital-1d-wfm-nchan-nsamp-vi.html) Writes one or more digital waveforms to a task that contains one or more digital output channels.
- [DAQmx Write (Counter Frequency 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-frequency-1chan-1samp-vi.html) Writes a new pulse frequency and duty cycle to a counter output task that contains a single channel.
- [DAQmx Write (Counter Time 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-time-1chan-1samp-vi.html) Writes a new pulse high time and low time to a counter output task that contains a single channel.
- [DAQmx Write (Counter Ticks 1Chan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-ticks-1chan-1samp-vi.html) Writes a new pulse high tick count and low tick count to a counter output task that contains a single channel.
- [DAQmx Write (Counter 1D Frequency 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-1chan-nsamp-vi.html) Writes new pulse frequency and duty cycle pairs to a counter output task that contains a single channel.
- [DAQmx Write (Counter 1D Time 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-1chan-nsamp-vi.html) Writes new pulse high times and low times to a counter output task that contains a single channel.
- [DAQmx Write (Counter 1D Ticks 1Chan NSamp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1d-ticks-1chan-nsamp-vi.html) Writes new pulse high tick counts and low tick counts to a counter output task that contains a single channel.
- [DAQmx Write (Counter 1D Frequency NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1d-frequency-nchan-1samp-vi.html) Writes a new pulse frequency and duty cycle to each channel in a counter output task that contains one or more channels.
- [DAQmx Write (Counter 1D Time NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1d-time-nchan-1samp-vi.html) Writes a new pulse high time and low time to each channel in a counter output task that contains one or more channels.
- [DAQmx Write (Counter 1DTicks NChan 1Samp) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-counter-1dticks-nchan-1samp-vi.html) Writes new pulse high tick counts and low tick counts to each channel in a counter output task that contains one or more channels.
- [DAQmx Write (Raw 1D U8) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u8-vi.html) Writes multiple raw , 8-bit unsigned integer samples to a task . Use this instance for devices that use 8-bit unsigned integers as the internal representation of a sample.
- [DAQmx Write (Raw 1D U16) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u16-vi.html) Writes multiple raw , 16-bit unsigned integer samples to a task . Use this instance for devices that use 16-bit unsigned integers as the internal representation of a sample.
- [DAQmx Write (Raw 1D U32) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-u32-vi.html) Writes multiple raw , 32-bit unsigned integer samples to a task . Use this instance for devices that use 32-bit unsigned integers as the internal representation of a sample.
- [DAQmx Write (Raw 1D I8) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i8-vi.html) Writes multiple raw , 8-bit signed integer samples to a task . Use this instance for devices that use 8-bit signed integers as the internal representation of a sample.
- [DAQmx Write (Raw 1D I16) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i16-vi.html) Writes multiple raw , 16-bit signed integer samples to a task . Use this instance for devices that use 16-bit signed integers as the internal representation of a sample.
- [DAQmx Write (Raw 1D I32) VI](../../../vi-lib/daqmx/write-llb/daqmx-write-raw-1d-i32-vi.html) Writes multiple raw , 32-bit signed integer samples to a task . Use this instance for devices that use 32-bit signed integers as the internal representation of a sample.

Parent topic:

DAQmx - Data Acquisition

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/express/daqmx/daqassistantblock-llb/daqmx-assistant-block-vi.html language=enus -->
## TOPIC 02334: DAQ Assistant

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/express/daqmx/daqassistantblock-llb/daqmx-assistant-block-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/express/daqmx/daqassistantblock-llb/daqmx-assistant-block-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates, edits, and runs tasks using NI-DAQmx. Refer to the NI-DAQmx Readme for a complete listing of devices NI-DAQmx supports. When you place this Express VI on the block diagram, the DAQ Assistant launches to create a new task. After you create a task, you can double-click the DAQ Assistant Expre

### DAQ Assistant

Creates, edits, and runs [tasks](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) using NI-DAQmx. Refer to the *NI-DAQmx Readme* for a complete listing of devices NI-DAQmx supports.

When you place this Express VI on the block diagram, the [DAQ Assistant](/csh?context=nidaqmx_expdaqmx_daqassistant) launches to create a new task. After you create a task, you can double-click the DAQ Assistant Express VI to edit that task. For continuous measurement or generation, place a while loop around the DAQ Assistant Express VI.

Using the DAQ Assistant Express VI creates a task accessible only to the Express VI. To make the task globally accessible from any application, you must [convert](/csh?context=nidaqmx_lvdaqmx_expressvicnvrt) the Express VI to an NI-DAQmx task saved in MAX

You can generate NI-DAQmx API code from a DAQ Assistant Express VI. Right-click the DAQ Assistant Express VI and select **Generate NI-DAQmx Code** from the shortcut menu to generate both configuration and example code for the task.

For continuous single-point input or output, the DAQ Assistant Express VI might not provide optimal performance. Refer to the Cont Acq&Graph Voltage-Single Point Optimization VI in examples\DAQmx\Analog In\Measure Voltage.llb for an example of techniques to create higher-performance, single-point I/O applications.

Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| data | Contains samples to write to the task. data is an output for measurement tasks and an input for analog and digital output tasks. data does not appear for counter output tasks. |
| error in | Describes error conditions that occur before this Express VI runs. |
| number of samples | Specifies the number of samples to acquire or generate for each channel in a finite task. For finite tasks, this VI ignores all settings for this input other than the initial input. For example, if you use this VI in a loop, specifying a new value in each iteration, NI-DAQmx ignores all values other than the one specified in the first loop iteration. If you want to to run multiple finite operations in a loop, such as to generate multiple pulse trains, each with a varying number of pulses, generate code for this VI. For continuous tasks, NI-DAQmx uses this value to determine the buffer size and the number of samples to read from the buffer. This input does not appear for all channel types and sample timing types. |
| rate | Specifies the sampling rate in samples per channel per second. This input does not appear for some channel types and sample timing types. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock. |
| stop | Specifies to stop the task and release device resources when this Express VI completes execution. For continuous tasks, this input is FALSE by default, meaning the task continues to run until the application stops. To stop the task so you can use the device again in the same application, wire this input to the same stop control you wire to the conditional terminal of the while loop. For single-point and finite tasks, this input is TRUE by default, meaning the task stops after all samples are acquired. To optimize single-point performance when using this Express VI in a loop, wire this input to the same stop control you wire to the conditional terminal of the while loop. |
| timeout | Specifies the amount of time in seconds to wait for the VI to read or write all samples. This VI returns an error if the time elapses. For input operations, the VI also returns any samples read before the time elapses. The default timeout is 10 seconds. If you set timeout to -1, the VI waits indefinitely. If you set timeout to 0, the VI tries once to read or write the samples and returns an error if unsuccessful. NI-DAQmx performs a timeout check only if the VI must wait to read or write samples. This input does not appear for all channel types and sample timing types. |

Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| data | Contains samples read from the task. data is an output for measurement tasks and an input for analog and digital output tasks. data does not appear for counter output tasks. |
| error out | Contains error information. If error in indicates that an error occurred before this Express VI ran, error out contains the same error information. Otherwise, it describes the error status that this Express VI produces. |
| stopped | Indicates whether the task stopped. The task stops if the stop input is set to TRUE or an error occurs. This output appears for continuous or hardware-timed single-point tasks only. |
| task out | Contains a reference to the task after this VI completes execution. Wire this output to other NI-DAQmx VIs to perform other operations with this task. |

[IMAGE alt='icon' src='daqmx-assistant-block-vi.png']

#### Dialog Box Options

Parent topic:

DAQmx - Data Acquisition
