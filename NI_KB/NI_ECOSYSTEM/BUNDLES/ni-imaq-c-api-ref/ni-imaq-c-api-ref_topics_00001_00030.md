# NI DOCUMENT BUNDLE: ni-imaq-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-imaq-c-api-ref start=1 end=30 -->
<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/acquisition_functions.html language=enus -->
## TOPIC 00001: Acquisition Functions

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/acquisition_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/acquisition_functions.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Functions

Use acquisition functions to configure, start, and abort an image acquisition. These functions also let you examine a buffer during acquisition.

[imgSessionAbort](imgsessionabort.html)

[imgSessionAcquire](imgsessionacquire.html)

[imgSessionConfigure](imgsessionconfigure.html)

[imgSessionCopyArea](imgsessioncopyarea.html)

[imgSessionCopyBuffer](imgsessioncopybuffer.html)

[imgSessionExamineBuffer](imgsessionexaminebuffer.html)

[imgSessionReleaseBuffer](imgsessionreleasebuffer.html)

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attribute_functions.html language=enus -->
## TOPIC 00002: Attribute Functions

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attribute_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attribute_functions.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Attribute Functions

Use attribute functions to examine and change NI-IMAQ and camera attributes.

You can change some attributes while an acquisition is in progress. 
However, most attributes require that you call 
[imgSessionConfigure](imgsessionconfigure.html) to reconfigure 
the driver.

NI-IMAQ does not let you make any attribute changes that would have a 
detrimental effect on any acquisition in progress. If NI-IMAQ lets you change an 
attribute during a live acquisition, the effects are immediate. If NI-IMAQ does not 
let you change an attribute during a live acquisition, stop the acquisition, change 
the attribute, 
and restart the acquisition.

[imgGetAttribute](imggetattribute.html)

[imgSetAttribute](imgsetattribute.html)

[imgGetCameraAttributeString](imggetcameraattributestring.html)

[imgSetCameraAttributeString](imgsetcameraattributestring.html)

[imgGetCameraAttributeNumeric](imggetcameraattributenumeric.html)

[imgSetCameraAttributeNumeric](imgsetcameraattributenumeric.html)

[imgSessionSetUserLUT8bit](imgsessionsetuserlut8bits.html)

[imgSessionSetUserLUT16bit](imgsessionsetuserlut16bits.html)

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attributes.html language=enus -->
## TOPIC 00003: Attributes

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attributes.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Attributes

Attributes are divided into groups. Click the links for a description, the possible values or range, and the data type of the properties within each group.

- Analog
- Color
- Device Information
- Image
- Session Information
- Status Information

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attributes_device_information.html language=enus -->
## TOPIC 00004: Device Information

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attributes_device_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attributes_device_information.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Device Information

Device information attributes return information concerning the image acquisition device.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attributes_image.html language=enus -->
## TOPIC 00005: Image

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attributes_image.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attributes_image.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Image

Image attributes define parameters that affect an image acquisition, such as region of interest.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices to which the property applies. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attributes_session_information.html language=enus -->
## TOPIC 00006: Session Information

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attributes_session_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attributes_session_information.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Session Information

Session information attributes set information about the maximum possible image size for an acquisition.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices to which the property applies. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/attributes_status_information.html language=enus -->
## TOPIC 00007: Status Information

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/attributes_status_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/attributes_status_information.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Status Information

Status information attributes return status information about an acquisition.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/code_examples.html language=enus -->
## TOPIC 00008: Code Examples

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/code_examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/code_examples.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Code Examples

You can find code examples in the <CVI>\samples\IMAQ directory, where <CVI> is the directory to which you installed LabWindows/CVI. You can find source code for other development environments in the <NI-IMAQ>\Sample directory, where <NI-IMAQ> is the directory to which you installed NI-IMAQ.

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/constants.html language=enus -->
## TOPIC 00009: Constants

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/constants.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/constants.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Constants

Constants help clearly define specific function parameter values. These constants are included in the niimaq.h header file.

The following table lists the constant name, the function to which the constant applies, and a general description.

| Constant | Use With | Description |
| --- | --- | --- |
| IMG_ACQUIRE_ALL | imgGetAttributeimgSetAttribute2 | Acquire all fields. |
| IMG_ACQUIRE_EVEN | imgGetAttributeimgSetAttribute2 | Acquire only even fields. |
| IMG_ACQUIRE_ODD | imgGetAttributeimgSetAttribute2 | Acquire only odd fields. |
| IMG_AQ_DONE | imgSessionWaitSignal2imgSessionWaitSignalAsync3imgPulseCreate2 | Asserted at the end of an acquisition when the last piece of data has been transferred to memory. |
| IMG_AQ_IN_PROGRESS | imgSessionWaitSignal2imgSessionWaitSignalAsync3imgPulseCreate2 | Asserted when the device initiates an acquisition either through a software- or hardware-triggered start. |
| IMG_BAYER_PATTERN_GBGB_RGRG | imgBayerColorDecode | Specifies the following Bayer pattern:GBGBRGRG |
| IMG_BAYER_PATTERN_GRGR_BGBG | imgBayerColorDecode | Specifies the following Bayer pattern:GRGRBGBG |
| IMG_BAYER_PATTERN_BGBG_GRGR | imgBayerColorDecode | Specifies the following Bayer pattern:BGBGGRGR |
| IMG_BAYER_PATTERN_RGRG_GBGB | imgBayerColorDecode | Specifies the following Bayer pattern:RGRGGBGB |
| IMG_BUF_COMPLETE | imgSessionWaitSignal2imgSessionWaitSignalAsync3imgPulseCreate2 | Asserted when an image buffer has been transferred to memory and is available for image processing. |
| IMG_BUFF_ACTUAL_HEIGHT | imgGetBufferElement | Returns the actual height in lines of a buffer acquired in VHA mode. |
| IMG_BUFF_ADDRESS | imgGetBufferElementimgSetBufferElement2 | Specifies the buffer address portion of a buffer list element. |
| IMG_BUFF_CHANNEL | imgGetBufferElementimgSetBufferElement2 | Specifies the channel from which to acquire an image. |
| IMG_BUFF_COMMAND | imgGetBufferElementimgSetBufferElement2 | Specifies the command portion of a buffer list element. |
| IMG_BUFF_SIZE | imgGetBufferElementimgSetBufferElement2 | Specifies the size portion of a buffer list element (the buffer size). Required for user-allocated buffers. |
| IMG_BUFF_SKIPCOUNT | imgGetBufferElementimgSetBufferElement2 | Specifies the skip count portion of a buffer list element. |
| IMG_CMD_LOOP | imgGetBufferElementimgSetBufferElement2(with IMG_BUFF_COMMAND constant) | Specifies a buffer list command of LOOP. Used as the command for the last buffer element, this constant causes an acquisition to perform a continuous type of acquisition such as a ring. |
| IMG_CMD_NEXT | imgGetBufferElementimgSetBufferElement2(with IMG_BUFF_COMMAND constant) | Specifies a buffer list command of NEXT. This constant causes an acquisition to take place on the buffer and to proceed to the next buffer list element. |
| IMG_CMD_STOP | imgGetBufferElementimgSetBufferElement2(with IMG_BUFF_COMMAND constant) | Specifies a buffer list command of STOP. Used as the command for the last buffer element, this constant causes an acquisition to perform a one-shot acquisition such as a sequence. |
| IMG_COLOR_CHROMA_BANDWIDTH_HIGH | imgSetAttribute2imgGetAttribute | Highest bandwidth (default). |
| IMG_COLOR_CHROMA_BANDWIDTH_LOW | imgSetAttribute2imgGetAttribute | Lowest bandwidth. |
| IMG_COLOR_CHROMA_PROCESS_ALWAYS_OFF | imgSetAttribute2imgGetAttribute | Use when you use a monochrome camera (default for CCIR or RS-170). |
| IMG_COLOR_CHROMA_PROCESS_ALWAYS_ON | imgSetAttribute2imgGetAttribute | Use when you use a color camera (default for NTSC or PAL). |
| IMG_COLOR_CHROMA_PROCESS_AUTODETECT | imgSetAttribute2imgGetAttribute | Use if the camera type (monochrome or color) is unknown. |
| IMG_COLOR_COMB_1LINE | imgSetAttribute2imgGetAttribute | Comb filtering using one delayed line. |
| IMG_COLOR_COMB_2LINES | imgSetAttribute2imgGetAttribute | Comb filtering using two delayed lines. |
| IMG_COLOR_COMB_OFF | imgSetAttribute2imgGetAttribute | Comb filter disabled (default in S-Video (Y/C) mode). |
| IMG_COLOR_LUMA_BANDWIDTH_FULL | imgSetAttribute2imgGetAttribute | All filters, including decimation filter, are disabled. Default value in CCIR or RS-170 mode. |
| IMG_COLOR_LUMA_BANDWIDTH_HIGH | imgSetAttribute2imgGetAttribute | Highest available bandwidth with decimation filter enabled. Default value for PAL or NTSC mode. |
| IMG_COLOR_LUMA_BANDWIDTH_LOW | imgSetAttribute2imgGetAttribute | Decimation filter enabled, lowest bandwidth. |
| IMG_COLOR_LUMA_BANDWIDTH_MEDIUM | imgSetAttribute2imgGetAttribute | Decimation filter enabled, medium bandwidth. |
| IMG_COLOR_REP_BLUE8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Blue color output. |
| IMG_COLOR_REP_GREEN8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Green color output. |
| IMG_COLOR_REP_HSI32 | imgGetAttributeimgSetAttribute2 | A color image encoded in 32 bits–8 bits unused and 8 bits each for the Hue, Saturation, and Intensity planes. |
| IMG_COLOR_REP_HSL32 | imgGetAttributeimgSetAttribute2 | A color image encoded in 32 bits–8 bits unused and 8 bits each for the Hue, Saturation, and Luminance planes. |
| IMG_COLOR_REP_HUE16 | imgGetAttributeimgSetAttribute2 | Specifies 16-bit Hue color output. |
| IMG_COLOR_REP_HUE8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Hue color output. |
| IMG_COLOR_REP_INT16 | imgGetAttributeimgSetAttribute2 | Specifies 16-bit Intensity color output. |
| IMG_COLOR_REP_INT8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Intensity color output. |
| IMG_COLOR_REP_LUM16 | imgGetAttributeimgSetAttribute2 | Specifies 16-bit Luminance color output. |
| IMG_COLOR_REP_LUM8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Luminance color output. |
| IMG_COLOR_REP_RED8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Red color output. |
| IMG_COLOR_REP_RGB16 | imgGetAttributeimgSetAttribute2 | Specifies 16-bit RGB color output. |
| IMG_COLOR_REP_RGB24 | imgGetAttributeimgSetAttribute2 | Specifies 24-bit RGB color output (default). |
| IMG_COLOR_REP_RGB32 | imgGetAttributeimgSetAttribute2 | Specifies 32-bit RGB color output. |
| IMG_COLOR_REP_RGB48 | imgGetAttributeimgSetAttribute2 | Specifies 48-bit RGB color output. |
| IMG_COLOR_REP_SAT16 | imgGetAttributeimgSetAttribute2 | Specifies 16-bit Saturation color output. |
| IMG_COLOR_REP_SAT8 | imgGetAttributeimgSetAttribute2 | Specifies 8-bit Saturation color output. |
| IMG_COLOR_RGB_CORING_LEVEL_NOCORING | imgSetAttribute2imgGetAttribute | Coring function is disabled. |
| IMG_COLOR_RGB_CORING_LEVEL_C1 | imgSetAttribute2imgGetAttribute | Coring activated for saturation equal or below 1 LSB. |
| IMG_COLOR_RGB_CORING_LEVEL_C3 | imgSetAttribute2imgGetAttribute | Coring activated for saturation equal or below 3 LSB. |
| IMG_COLOR_RGB_CORING_LEVEL_C7 | imgSetAttribute2imgGetAttribute | Coring activated for saturation equal or below 7 LSB. |
| IMG_CURRENT_BUFFER | imgSessionExamineBuffer2 | Specifies to examine current buffer in a live acquisition. Waits until vertical blank to return the buffer to you. |
| IMG_DEVICE_FRAME | imgCreateBuffer | Specifies the new buffer is created in onboard memory (not supported on the NI PCI/PXI-1407, NI PCIe-1427, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, or NI PXIe-1435 devices). |
| IMG_FIELD_EVEN | imgGetAttributeimgSetAttribute2 | Specifies the start field of the acquisition as even. |
| IMG_FIELD_MODE | imgGetAttributeimgSetAttribute2 | Specifies the acquisition mode as field. |
| IMG_FIELD_ODD | imgGetAttributeimgSetAttribute2 | Specifies the start field of the acquisition as odd. |
| IMG_FILTER_NONE | imgGetAttributeimgSetAttribute2 | Specifies no video filter. |
| IMG_FILTER_NTSC | imgGetAttributeimgSetAttribute2 | Specifies the video filter is NTSC. |
| IMG_FILTER_PAL | imgGetAttributeimgSetAttribute2 | Specifies the video filter is PAL. |
| IMG_FRAME_DONE | imgSessionWaitSignal2imgSessionWaitSignalAsync3imgPulseCreate2 | Asserted at the end of acquisition into each image buffer. |
| IMG_FRAME_MODE | imgGetAttributeimgSetAttribute2 | Specifies the acquisition mode as interlaced. |
| IMG_FRAME_START | imgSessionWaitSignal2imgSessionWaitSignalAsync3imgPulseCreate2 | Asserted at the start of acquisition into each image buffer. |
| IMG_FRAME_VALID | imgPulseCreate2 | Asserted while a frame is being transferred. |
| IMG_FRAMETIME_10MINUTES | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 10 min. |
| IMG_FRAMETIME_10SECONDS | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 10 s. |
| IMG_FRAMETIME_1MINUTE | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 1 min. |
| IMG_FRAMETIME_1SECOND | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 1 s. |
| IMG_FRAMETIME_2MINUTES | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 2 min. |
| IMG_FRAMETIME_2SECONDS | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 2 s. |
| IMG_FRAMETIME_5MINUTES | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 5 min. |
| IMG_FRAMETIME_5SECONDS | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 5 s. |
| IMG_FRAMETIME_STANDARD | imgGetAttributeimgSetAttribute2 | Specifies a frame timeout value of 100 ms. |
| IMG_GAIN_0DB | imgGetAttributeimgSetAttribute2 | Specifies the gain is +0 dB. |
| IMG_GAIN_3DB | imgGetAttributeimgSetAttribute2 | Specifies the gain is +3 dB. |
| IMG_GAIN_6DB | imgGetAttributeimgSetAttribute2 | Specifies the gain is +6 dB. |
| IMG_HOST_FRAME | imgCreateBuffer | Specifies the new buffer is created in the host computer memory. |
| IMG_IMMEDIATE | imgPulseCreate2 | Causes the function to generate a pulse when the function is executed. |
| IMG_LAST_BUFFER | imgSessionExamineBuffer2 | Specifies to examine the last valid buffer in a live acquisition. |
| IMG_LINE_VALID | imgPulseCreate2 | Asserted while a line of a frame is being transferred. |
| IMG_LUT_BINARY | imgGetAttributeimgSetAttribute2 | Specifies a binary LUT, which converts the sampled data to a binary image of black and white. |
| IMG_LUT_INVERSE | imgGetAttributeimgSetAttribute2 | Specifies an inverse LUT, which inverts the gray levels. |
| IMG_LUT_INVERSE_BINARY | imgGetAttributeimgSetAttribute2 | Specifies an inverse binary LUT, which converts the sampled data into a binary image of white and black. |
| IMG_LUT_INVERSE_LOG | imgGetAttributeimgSetAttribute2 | Specifies an inverse log LUT, which converts the sampled data to a logarithmic form that produces greater contrast in the white region. |
| IMG_LUT_LOG | imgGetAttributeimgSetAttribute2 | Specifies a log LUT, which converts the sampled data to a logarithmic form that produces greater contrast in the black region. |
| IMG_LUT_NORMAL | imgGetAttributeimgSetAttribute2 | Specifies a normal LUT. |
| IMG_LUT_TYPE_DEFAULT | imgSessionSetUserLUT8bitsimgSessionSetUserLUT16bits | Default LUT used to initialize all LUTs. |
| IMG_LUT_TYPE_RED | imgSessionSetUserLUT8bits | Red channel LUT for RGB digital cameras or the PCI/PXI-1411. |
| IMG_LUT_TYPE_GREEN | imgSessionSetUserLUT8bits | Green channel LUT for RGB digital cameras or the PCI/PXI-1411. |
| IMG_LUT_TYPE_BLUE | imgSessionSetUserLUT8bits | Blue channel LUT for RGB digital cameras or the PCI/PXI-1411. |
| IMG_LUT_TYPE_TAP0 | imgSessionSetUserLUT8bitsimgSessionSetUserLUT16bits | Tap 0 LUT for digital devices. |
| IMG_LUT_TYPE_TAP1 | imgSessionSetUserLUT8bitsimgSessionSetUserLUT16bits | Tap 1 LUT for digital devices. |
| IMG_LUT_TYPE_TAP2 | imgSessionSetUserLUT8bits | Tap 2 LUT for digital devices. |
| IMG_LUT_TYPE_TAP3 | imgSessionSetUserLUT8bits | Tap 3 LUT for digital devices. |
| IMG_OVERWRITE_GET_OLDEST | imgSessionCopyBufferByNumberimgSessionCopyAreaByNumber | Retrieves the oldest image in the buffer list if requested image has been overwritten. |
| IMG_OVERWRITE_GET_NEXT_ITERATION | imgSessionCopyBufferByNumberimgSessionCopyAreaByNumber | Provides the next image with the corresponding index in the buffer list if requested image has been overwritten. |
| IMG_OVERWRITE_FAIL | imgSessionCopyBufferByNumberimgSessionCopyAreaByNumber | Fails if requested image has been overwritten. |
| IMG_OVERWRITE_GET_NEWEST | imgSessionCopyBufferByNumberimgSessionCopyAreaByNumber | Retrieves the most recently acquired image in the buffer list if requested image has been overwritten. |
| IMG_POCL_UNKNOWN | imgGetAttribute imgSetAttribute2 | The PoCL circuitry is in an unknown state. |
| IMG_POCL_NOT_SUPPORTED | imgGetAttribute imgSetAttribute2 | The PoCL circuitry does not exist on the device. |
| IMG_POCL_NO_AUX_POWER | imgGetAttribute imgSetAttribute2 | The PoCL circuitry has no power supply and thus cannot provide power. |
| IMG_POCL_BAD_FUSE | imgGetAttribute imgSetAttribute2 | The PoCL circuitry has a blown fuse and thus cannot provide power. |
| IMG_POCL_DISABLED | imgGetAttribute imgSetAttribute2 | The PoCL circuitry is disabled. |
| IMG_POCL_FAULT | imgGetAttribute imgSetAttribute2 | The PoCL circuitry has detected a fault. |
| IMG_POCL_INITIALIZING | imgGetAttribute imgSetAttribute2 | The PoCL circuitry is initializing. |
| IMG_POCL_INACTIVE | imgGetAttribute imgSetAttribute2 | The PoCL circuitry is enabled but not providing power. |
| IMG_POCL_ACTIVE | imgGetAttribute imgSetAttribute2 | The PoCL circuitry is enabled and providing power. |
| IMG_PULSE_POLAR_ACTIVEH | imgPulseCreate | Specifies the polarity of a pulse as active high. |
| IMG_PULSE_POLAR_ACTIVEL | imgPulseCreate | Specifies the polarity of a pulse as active low. |
| IMG_ROI_FIT_LARGER | imgSessionFitROI | Fits the specified ROI to the next largest alignment. If the ROI is already properly aligned, this value has no effect on the ROI. |
| IMG_ROI_FIT_SMALLER | imgSessionFitROI | Fits the specified ROI to the next smallest alignment. If the ROI is already properly aligned, this value has no effect on the ROI. |
| IMG_SCALE_DIV2 | imgGetAttributeimgSetAttribute2 | The vertical resolution is scaled down by a factor of 2. |
| IMG_SCALE_DIV4 | imgGetAttributeimgSetAttribute2 | The vertical resolution is scaled down by a factor of 4. |
| IMG_SCALE_DIV8 | imgGetAttributeimgSetAttribute2 | The vertical resolution is scaled down by a factor of 8. |
| IMG_SCALE_NONE | imgGetAttributeimgSetAttribute2 | Performs no scaling. |
| IMG_SIGNAL_EXTERNAL | imgPulseCreate2imgSessionLineTrigSource2imgSessionTriggerConfigure2imgSessionTriggerDrive2imgSessionTriggerRead2imgSessionTriggerRoute2imgSessionWaitSignal2imgSessionWaitSignalAsync3 | Specifies the signal type as the external trigger lines. |
| IMG_SIGNAL_ISO_IN | imgPulseCreate2imgSessionLineTrigSource2imgSessionTriggerConfigure2imgSessionTriggerRead2imgSessionTriggerRoute2imgSessionWaitSignal2imgSessionWaitSignalAsync3 | Specifies the signal type as the isolated input trigger lines. |
| IMG_SIGNAL_ISO_OUT | imgPulseCreate2imgSessionLineTrigSource2imgSessionTriggerConfigure2imgSessionTriggerDrive2imgSessionTriggerRead2imgSessionTriggerRoute2imgSessionWaitSignal2imgSessionWaitSignalAsync3 | Specifies the signal type as the isolated output trigger lines. |
| IMG_SIGNAL_NONE | imgSessionTriggerRoute2 | Used to disable the route. |
| IMG_SIGNAL_RTSI | imgPulseCreate2imgSessionLineTrigSource2imgSessionTriggerConfigure2imgSessionTriggerDrive2imgSessionTriggerRead2imgSessionTriggerRoute2imgSessionWaitSignal2imgSessionWaitSignalAsync3 | Specifies the signal type as the RTSI trigger lines. |
| IMG_SIGNAL_SCALED_ENCODER | imgSessionLineTrigSource2 | Specifies the signal type as the scaled encoder signal. |
| IMG_SIGNAL_STATUS | imgPulseCreate2imgSessionWaitSignal2imgSessionWaitSignalAsync3 | Specifies the signal type as one of the status signals, IMG_AQ_DONE, IMG_AQ_IN_PROGRESS, IMG_BUF_COMPLETE, IMG_FRAME_DONE, IMG_FRAME_START, IMG_IMMEDIATE. |
| IMG_TIMEOUT_INFINITE | imgSessionWaitSignal imgSessionWaitSignal2 imgSessionWaitSignalAsync3 imgSessionSerialRead imgSessionSerialReadBytes imgSessionSerialWrite imgSessionTriggerConfigure imgSessionTriggerConfigure2 (with IMG_ATTR_FRAMEWAIT_MSEC constant) | Used to wait indefinitely. |
| IMG_TRIG_ACTION_BUFFER | imgSessionTriggerConfigure2 | Specifies each buffer is acquired based on a trigger. |
| IMG_TRIG_ACTION_BUFLIST | imgSessionTriggerConfigure2 | Specifies acquisition of buffer list starts on a trigger. |
| IMG_TRIG_ACTION_CAPTURE | imgSessionTriggerConfigure2 | Specifies trigger starts acquisition. |
| IMG_TRIG_ACTION_NONE | imgSessionTriggerConfigure2 | Specifies triggering is disabled. |
| IMG_TRIG_ACTION_STOP | imgSessionTriggerConfigure2 | Specifies trigger stops acquisition. |
| IMG_TRIG_DRIVE_AQ_DONE | imgSessionTriggerDrive2 | Specifies that the trigger line is driven on AQ_DONE. |
| IMG_TRIG_DRIVE_AQ_IN_PROGRESS | imgSessionTriggerDrive2 | Specifies that the trigger line is driven on AQ_IN_PROGRESS. |
| IMG_TRIG_DRIVE_ASSERTED | imgSessionTriggerDrive2 | Specifies to immediately drive the trigger line asserted. |
| IMG_TRIG_DRIVE_DISABLED | imgSessionTriggerDrive2 | Specifies that the trigger line is not driven. |
| IMG_TRIG_DRIVE_FRAME_DONE | imgSessionTriggerDrive2 | Specifies that the trigger line is driven with frame done. |
| IMG_TRIG_DRIVE_FRAME_START | imgSessionTriggerDrive2 | Specifies that the trigger line is driven with frame start. |
| IMG_TRIG_DRIVE_HSYNC | imgSessionTriggerDrive2 | Specifies that the trigger line is driven on HSYNC. |
| IMG_TRIG_DRIVE_PIXEL_CLK | imgSessionTriggerDrive2 | Specifies that the trigger line is driven with pixel clock. |
| IMG_TRIG_DRIVE_SCALED_ENCODER | imgSessionTriggerDrive2 | Specifies that the trigger line is driven with the scaled encoder signal. |
| IMG_TRIG_DRIVE_UNASSERTED | imgSessionTriggerDrive2 | Specifies to immediately drive the trigger line unasserted. |
| IMG_TRIG_DRIVE_VSYNC | imgSessionTriggerDrive2 | Specifies that the trigger line is driven on VSYNC. |
| IMG_TRIG_POLAR_ACTIVEH | imgSessionTriggerConfigure2imgSessionTriggerDrive2imgSessionTriggerRead2 | Specifies the polarity of a trigger as active HIGH. |
| IMG_TRIG_POLAR_ACTIVEL | imgSessionTriggerConfigure2imgSessionTriggerDrive2imgSessionTriggerRead2 | Specifies the polarity of a trigger as active LOW. |
| imgPlot2_COLOR_RGB24 | imgPlot2imgPlotDC2 | Specifies a 24-bit color RGB image. |
| imgPlot2_COLOR_RGB32 | imgPlot2imgPlotDC2 | Specifies a 32-bit color RGB image. |
| imgPlot2_INVERT | imgPlot2imgPlotDC2 | Specifies to invert the image when plotted. |
| imgPlot2_MONO_10 | imgPlot2imgPlotDC2 | Specifies a 10-bit monochrome image. |
| imgPlot2_MONO_12 | imgPlot2imgPlotDC2 | Specifies a 12-bit monochrome image. |
| imgPlot2_MONO_14 | imgPlot2imgPlotDC2 | Specifies a 14-bit monochrome image. |
| imgPlot2_MONO_16 | imgPlot2imgPlotDC2 | Specifies a 16-bit monochrome image. |
| imgPlot2_MONO_32 | imgPlot2imgPlotDC2 | Specifies a 32-bit monochrome image. |
| imgPlot2_MONO_8 | imgPlot2imgPlotDC2 | Specifies an 8-bit monochrome image. |
| INTERFACE_NAME_SIZE | imgInterfaceQueryNames | Specifies the size of each array element in the interface names array. |
| PULSE_MODE_SINGLE | imgPulseCreate2 | Specifies a single pulse that generates one pulse on the assertion edge of the specified signal. |
| PULSE_MODE_SINGLE_REARM | imgPulseCreate2 | Specifies a pulse that generates a pulse on all assertion edges of the specified signal until imgPulseStop is called. |
| PULSE_MODE_TRAIN | imgPulseCreate2 | Specifies a continuous pulse train that generates a pulse until imgPulseStop is called. |
| PULSE_TIMEBASE_100KHZ | imgPulseCreate2 | Specifies a 100 kHz timebase to use for pulse generation. |
| PULSE_TIMEBASE_50MHZ | imgPulseCreate2 | Specifies a 50 MHz timebase to use for pulse generation. |
| PULSE_TIMEBASE_PIXELCLK | imgPulseCreate2 | Specifies the incoming pixel clock from the camera to use as a timebase for pulse generation. |
| PULSE_TIMEBASE_SCALED_ENCODER | imgPulseCreate2 | Specifies scaled encoder counts as units for pulse generation. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/error_codes.html language=enus -->
## TOPIC 00010: Error Codes

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/error_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/error_codes.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes

Every NI-IMAQ function is of the following form:

rval = Function_Name(parameter 1, parameter 2, ... parameter n);

Each function returns a status code (rval) that indicates the success or failure of the function. The following table describes the status codes returned by each NI-IMAQ function.

| Error Code | Status Name | Description |
| --- | --- | --- |
| -1074397183 | IMG_ERR_NCAP | NI-IMAQ cannot perform the requested operation. |
| -1074397182 | IMG_ERR_OVRN | Too many interfaces open. |
| -1074397181 | IMG_ERR_EMEM | Not enough memory to perform the operation. |
| -1074397180 | IMG_ERR_OSER | Operating system error occurred. |
| -1074397179 | IMG_ERR_PAR1 | Function-specific; see function description. |
| -1074397178 | IMG_ERR_PAR2 | Function-specific; see function description. |
| -1074397177 | IMG_ERR_PAR3 | Function-specific; see function description. |
| -1074397176 | IMG_ERR_PAR4 | Function-specific; see function description. |
| -1074397175 | IMG_ERR_PAR5 | Function-specific; see function description. |
| -1074397174 | IMG_ERR_PAR6 | Function-specific; see function description. |
| -1074397173 | IMG_ERR_PAR7 | Function-specific; see function description. |
| -1074397172 | IMG_ERR_MXBF | Too many buffers already allocated. |
| -1074397171 | IMG_ERR_DLLE | DLL internal error; bad logic state. |
| -1074397170 | IMG_ERR_BSIZ | Buffer size used is too small for minimum acquisition frame. |
| -1074397169 | IMG_ERR_MXBI | Exhausted buffer IDs. |
| -1074397168 | IMG_ERR_ELCK | Operating system unable to lock the requested amount of memory. |
| -1074397167 | IMG_ERR_DISE | Error releasing the image buffer. |
| -1074397166 | IMG_ERR_BBUF | Bad buffer pointer in list. |
| -1074397165 | IMG_ERR_NLCK | Buffer list is not locked for this acquisition. |
| -1074397164 | IMG_ERR_NCAM | No camera defined for this channel. |
| -1074397163 | IMG_ERR_BINT | The passed in interface or session is invalid. |
| -1074397162 | IMG_ERR_BROW | The bytes per row value is less than region of interest. |
| -1074397161 | IMG_ERR_BROI | Region of interest is larger than the acquisition area. |
| -1074397160 | IMG_ERR_BCMF | Camera file is missing or corrupted. |
| -1074397159 | IMG_ERR_NVBL | The hardware is incapable of performing the requested action. |
| -1074397158 | IMG_ERR_NCFG | No buffers configured for session. |
| -1074397157 | IMG_ERR_BBLF | Buffer list does not contain a valid final command. |
| -1074397156 | IMG_ERR_BBLE | Buffer list contains an invalid command. |
| -1074397155 | IMG_ERR_BBLB | One or more of the buffers in the buffer list is not configured. |
| -1074397154 | IMG_ERR_NAIP | No acquisition in progress. |
| -1074397153 | IMG_ERR_VLCK | Cannot detect recognizable video source. |
| -1074397152 | IMG_ERR_BDMA | Bad DMA transfer. |
| -1074397151 | IMG_ERR_AIOP | Cannot perform request; acquisition currently in progress. |
| -1074397150 | IMG_ERR_TIMO | A timeout error occurred while waiting for the specified event. If waiting for an image, verify that all video data is acquired within the timeout period. If waiting for a signal, verify that the signal assertion occurs within the timeout period. |
| -1074397149 | IMG_ERR_NBUF | No buffers available; too early in acquisition. |
| -1074397148 | IMG_ERR_ZBUF | The buffer has a size of zero. |
| -1074397147 | IMG_ERR_HLPR | Parameter value set lower than valid range. |
| -1074397146 | IMG_ERR_BTRG | Trigger loopback problem; cannot drive with action enabled. |
| -1074397145 | IMG_ERR_NINF | No interface found. |
| -1074397144 | IMG_ERR_NDLL | Unable to load DLL. |
| -1074397143 | IMG_ERR_NFNC | Unable to find API function in DLL. |
| -1074397142 | IMG_ERR_NOSR | Unable to allocate system resources. |
| -1074397141 | IMG_ERR_BTAC | No trigger action; acquisition will time out. |
| -1074397140 | IMG_ERR_FIFO | FIFO overflow caused acquisition to halt. |
| -1074397139 | IMG_ERR_MLCK | Operating system denied request to lock down memory. |
| -1074397138 | IMG_ERR_ILCK | Interface locked. |
| -1074397137 | IMG_ERR_NEPK | No pixel clock detected from camera. |
| -1074397136 | IMG_ERR_SCLM | Field scaling mode not supported. |
| -1074397135 | IMG_ERR_SCC1 | Channel not set to 1 when using StillColor RGB acquisition. |
| -1074397134 | IMG_ERR_SMALLALLOC | Error during small buffer allocation. |
| -1074397133 | IMG_ERR_ALLOC | Error during large buffer allocation. |
| -1074397132 | IMG_ERR_BADCAMTYPE | This camera type is not supported by this hardware. |
| -1074397131 | IMG_ERR_BADPIXTYPE | Camera not supported; must be an 8-bit camera. |
| -1074397130 | IMG_ERR_BADCAMPARAM | Bad camera parameter in configuration file. |
| -1074397129 | IMG_ERR_PALKEYDTCT | Unable to recognize color component in PAL signal. |
| -1074397128 | IMG_ERR_BFRQ | Bad clock frequency. |
| -1074397127 | IMG_ERR_BITP | Bad interface type. |
| -1074397126 | IMG_ERR_HWNC | Hardware not capable of supporting this operation. |
| -1074397125 | IMG_ERR_SERIAL | Serial port error. |
| -1074397124 | IMG_ERR_MXPI | No more pulse IDs are available. Dispose of an existing pulse first. |
| -1074397123 | IMG_ERR_BPID | Bad pulse ID. |
| -1074397122 | IMG_ERR_NEVR | DLL internal error; bad logic state. |
| -1074397121 | IMG_ERR_SERIAL_TIMO | Unable to perform the requested serial operation within the timeout period. |
| -1074397120 | IMG_ERR_PG_TOO_MANY | Too many pattern generation transitions defined. |
| -1074397119 | IMG_ERR_PG_BAD_TRANS | Bad pattern generation transition time. |
| -1074397118 | IMG_ERR_PLNS | Pulse not started. |
| -1074397117 | IMG_ERR_BPMD | Bad pulse mode. |
| -1074397116 | IMG_ERR_NSAT | This attribute cannot be set. |
| -1074397115 | IMG_ERR_HYBRID | Cannot mix system and onboard memory buffers. |
| -1074397114 | IMG_ERR_BADFILFMT | Pixel depth not supported with this file format. |
| -1074397113 | IMG_ERR_BADFILEXT | File extension is not supported. |
| -1074397112 | IMG_ERR_NRTSI | Too many RTSI triggers mapped; you can use only four RTSI lines at once. |
| -1074397111 | IMG_ERR_MXTRG | Exhausted trigger resources. |
| -1074397110 | IMG_ERR_MXRC | Exhausted resources. |
| -1074397109 | IMG_ERR_OOR | Parameter out of range. |
| -1074397108 | IMG_ERR_NPROG | FPGA not programmed. |
| -1074397107 | IMG_ERR_NEOM | Not enough onboard memory to perform the operation. |
| -1074397106 | IMG_ERR_BDTYPE | Bad display type; buffer cannot be displayed with imgPlot. |
| -1074397105 | IMG_ERR_THRDACCDEN | Thread denied access to function. |
| -1074397104 | IMG_ERR_BADFILWRT | Could not write the file. |
| -1074397103 | IMG_ERR_AEXM | This buffer is currently protected. Release it to allow new data to be written. |
| -1074397102 | IMG_ERR_BAD_LUT_TYPE | The LUT type is invalid. |
| -1074397101 | IMG_ERR_ATTRIBUTE_NOT_READABLE | The selected attribute is not readable. |
| -1074397100 | IMG_ERR_BOARD_NOT_SUPPORTED | This version of NI-IMAQ does not support this device. |
| -1074397099 | IMG_ERR_BAD_FRAME_FIELD | The value of IMG_ATTR_FRAME_FIELD is invalid. |
| -1074397098 | IMG_ERR_INVALID_ATTRIBUTE | The requested attribute is invalid. |
| -1074397097 | IMG_ERR_BAD_LINE_MAP | The physical data lines are incorrectly mapped to bit values. |
| -1074397095 | IMG_ERR_BAD_CHANNEL | The requested channel is invalid for this device. |
| -1074397094 | IMG_ERR_BAD_CHROMA_FILTER | The value of IMG_ATTR_CHROMA_FILTER is invalid. |
| -1074397093 | IMG_ERR_BAD_SCALE | The value of IMG_ATTR_HSCALE or IMG_ATTR_VSCALE is invalid. |
| -1074397091 | IMG_ERR_BAD_TRIGGER_MODE | The requested triggering mode is invalid. |
| -1074397090 | IMG_ERR_BAD_CLAMP_START | The clamp start value is invalid. |
| -1074397089 | IMG_ERR_BAD_CLAMP_STOP | The requested clamp stop value is invalid. |
| -1074397088 | IMG_ERR_BAD_BRIGHTNESS | The requested brightness level is out of range. |
| -1074397087 | IMG_ERR_BAD_CONTRAST | The requested contrast level is out of range. |
| -1074397086 | IMG_ERR_BAD_SATURATION | The requested saturation level is out of range. |
| -1074397085 | IMG_ERR_BAD_TINT | The requested tint level is out of range. |
| -1074397084 | IMG_ERR_BAD_HUE_OFF_ANGLE | The requested hue offset angle is out of range. |
| -1074397083 | IMG_ERR_BAD_ACQUIRE_FIELD | The field requested to be acquired is invalid. |
| -1074397082 | IMG_ERR_BAD_LUMA_BANDWIDTH | The requested luma bandwidth value is invalid. |
| -1074397081 | IMG_ERR_BAD_LUMA_COMB | The requested luma comb setting is invalid. |
| -1074397080 | IMG_ERR_BAD_CHROMA_PROCESS | The requested chroma processing value is invalid. |
| -1074397079 | IMG_ERR_BAD_CHROMA_BANDWIDTH | The requested chroma bandwidth value is invalid. |
| -1074397078 | IMG_ERR_BAD_CHROMA_COMB | The requested chroma comb setting value is invalid. |
| -1074397077 | IMG_ERR_BAD_RGB_CORING | The requested minimum level of saturation (coring) for the RGB color space is invalid. |
| -1074397076 | IMG_ERR_BAD_HUE_REPLACE_VALUE | The requested HSL hue replacement value is out of range. |
| -1074397075 | IMG_ERR_BAD_RED_GAIN | The requested red gain value is out of range. |
| -1074397074 | IMG_ERR_BAD_GREEN_GAIN | The requested green gain value is out of range. |
| -1074397073 | IMG_ERR_BAD_BLUE_GAIN | The requested blue gain value is out of range. |
| -1074397072 | IMG_ERR_BAD_START_FIELD | The requested start field value is invalid. |
| -1074397071 | IMG_ERR_BAD_TAP_DIRECTION | The direction of the tap scan is invalid. |
| -1074397070 | IMG_ERR_BAD_MAX_IMAGE_RECT | The maximum image rectangle value is invalid. |
| -1074397069 | IMG_ERR_BAD_TAP_TYPE | The tap configuration is invalid. |
| -1074397068 | IMG_ERR_BAD_SYNC_RECT | The synchronization rectangle is invalid. |
| -1074397067 | IMG_ERR_BAD_ACQWINDOW_RECT | The requested acquisition window is invalid. |
| -1074397066 | IMG_ERR_BAD_HSL_CORING | The requested minimum level of saturation (coring) for the HSL color space is out of range. |
| -1074397065 | IMG_ERR_BAD_TAP_0_VALID_RECT | The rectangle defined for Tap 0 is invalid. |
| -1074397064 | IMG_ERR_BAD_TAP_1_VALID_RECT | The rectangle defined for Tap 1 is invalid. |
| -1074397063 | IMG_ERR_BAD_TAP_2_VALID_RECT | The rectangle defined for Tap 2 is invalid. |
| -1074397062 | IMG_ERR_BAD_TAP_3_VALID_RECT | The rectangle defined for Tap 3 is invalid. |
| -1074397061 | IMG_ERR_BAD_TAP_RECT | The tap rectangle is invalid. |
| -1074397060 | IMG_ERR_BAD_NUM_TAPS | The number of taps is invalid. |
| -1074397059 | IMG_ERR_BAD_TAP_NUM | The tap number is invalid. |
| -1074397058 | IMG_ERR_BAD_QUAD_NUM | The scarab quadrant number is invalid. |
| -1074397057 | IMG_ERR_BAD_NUM_DATA_LINES | The number of data lines requested is invalid for this image acquisition device. |
| -1074397056 | IMG_ERR_BAD_BITS_PER_COMPONENT | The bits-per-component value is invalid. |
| -1074397055 | IMG_ERR_BAD_NUM_COMPONENTS | The number of components value is invalid. |
| -1074397054 | IMG_ERR_BAD_BIN_THRESHOLD_LOW | The requested lower binary threshold value is out of range. |
| -1074397053 | IMG_ERR_BAD_BIN_THRESHOLD_HIGH | The requested upper binary threshold value is out of range. |
| -1074397052 | IMG_ERR_BAD_BLACK_REF_VOLT | The requested black reference voltage value is out of range. |
| -1074397051 | IMG_ERR_BAD_WHITE_REF_VOLT | The requested white reference voltage value is out of range. |
| -1074397050 | IMG_ERR_BAD_FREQ_STD | The video standard frequency value selected for the 6431 chip is invalid. |
| -1074397049 | IMG_ERR_BAD_HDELAY | The HDELAY value is out of range. |
| -1074397048 | IMG_ERR_BAD_LOCK_SPEED | The setting for lock speed is invalid. |
| -1074397047 | IMG_ERR_BAD_BUFFER_LIST | The buffer list is invalid. |
| -1074397046 | IMG_ERR_BOARD_NOT_INITIALIZED | The image aquisition device is not yet initialized. |
| -1074397045 | IMG_ERR_BAD_PCLK_SOURCE | The requested pixel clock source is invalid for this image acquisition device. |
| -1074397044 | IMG_ERR_BAD_VIDEO_LOCK_CHANNEL | The selected video timing signal source is invalid for this image acquisition device. |
| -1074397043 | IMG_ERR_BAD_LOCK_SEL | The selected lock mode is invalid. |
| -1074397042 | IMG_ERR_BAD_BAUD_RATE | The selected baud rate is invalid for this image acquisition device. |
| -1074397041 | IMG_ERR_BAD_STOP_BITS | The requested serial stop bits setting is invalid for this image acquisition device. |
| -1074397040 | IMG_ERR_BAD_DATA_BITS | The requested serial data bits setting is invalid for this image acquisition device. |
| -1074397039 | IMG_ERR_BAD_PARITY | The requested serial parity setting is invalid for this image acquisition device. |
| -1074397038 | IMG_ERR_TERM_STRING_NOT_FOUND | The requested serial termination string was not found in the returned buffer. |
| -1074397037 | IMG_ERR_SERIAL_READ_TIMEOUT | The serial read did not complete within the specified timeout period. |
| -1074397036 | IMG_ERR_SERIAL_WRITE_TIMEOUT | The serial write operation could not execute within the specified timeout period. |
| -1074397035 | IMG_ERR_BAD_SYNCHRONICITY | The async setting in imgSessionAcquire is invalid. |
| -1074397034 | IMG_ERR_BAD_INTERLACING_CONFIG | This tap configuration cannot be interlaced. |
| -1074397032 | IMG_ERR_BAD_CHIP_CODE | The requested chip code is invalid. Could not find a matching chip. |
| -1074397031 | IMG_ERR_LUT_NOT_PRESENT | The LUT chip does not exist on this image acquisition device. |
| -1074397030 | IMG_ERR_DSPFILTER_NOT_PRESENT | The DSP filter does not exist on this image acquisition device. |
| -1074397029 | IMG_ERR_DEVICE_NOT_FOUND | The image acquisition device was not found. |
| -1074397028 | IMG_ERR_ONBOARD_MEM_CONFIG | An error occurred during onboard memory configuration. |
| -1074397027 | IMG_ERR_BAD_POINTER | The pointer provided is either NULL when it should not be, or is non-NULL when it should be NULL. |
| -1074397026 | IMG_ERR_BAD_BUFFER_LIST_INDEX | The requested buffer list index is invalid. |
| -1074397025 | IMG_ERR_INVALID_BUFFER_ATTRIBUTE | The requested buffer attribute is invalid. |
| -1074397024 | IMG_ERR_INVALID_BUFFER_PTR | The requested buffer was not created by the NI-IMAQ driver software. |
| -1074397023 | IMG_ERR_BUFFER_LIST_ALREADY_LOCKED | This image acquisition device already has a buffer list locked down in memory. |
| -1074397022 | IMG_ERR_BAD_DEVICE_TYPE | The type of image acquisition device requested is invalid. |
| -1074397021 | IMG_ERR_BAD_BAR_SIZE | The size of one or more Base Address Register windows is incorrect. |
| -1074397019 | IMG_ERR_NO_VALID_COUNTER_RECT | The selected region of interest is not valid for the camera tap configuration. |
| -1074397018 | IMG_ERR_ACQ_STOPPED | The wait terminated because the acquisition stopped. |
| -1074397017 | IMG_ERR_BAD_TRIGGER_ACTION | The requested trigger action is invalid. |
| -1074397016 | IMG_ERR_BAD_TRIGGER_POLARITY | The trigger polarity is invalid. |
| -1074397015 | IMG_ERR_BAD_TRIGGER_NUMBER | The requested trigger line is invalid. Please verify that this trigger line exists and is properly connected to your device. |
| -1074397014 | IMG_ERR_BUFFER_NOT_AVAILABLE | The requested buffer has been overwritten and is no longer available. |
| -1074397012 | IMG_ERR_BAD_PULSE_ID | The pulse ID is invalid. |
| -1074397011 | IMG_ERR_BAD_PULSE_TIMEBASE | The requested timebase for the pulse is invalid. |
| -1074397010 | IMG_ERR_BAD_PULSE_GATE | The gate signal for the pulse is invalid. |
| -1074397009 | IMG_ERR_BAD_PULSE_GATE_POLARITY | The polarity of the pulse gate signal is invalid. |
| -1074397008 | IMG_ERR_BAD_PULSE_OUTPUT | The output signal for the pulse is invalid. |
| -1074397007 | IMG_ERR_BAD_PULSE_OUTPUT_POLARITY | The requested polarity of the pulse output signal is invalid. |
| -1074397006 | IMG_ERR_BAD_PULSE_MODE | The requested pulse mode is invalid. |
| -1074397005 | IMG_ERR_NOT_ENOUGH_RESOURCES | There are not enough system resources to complete the requested option. |
| -1074397004 | IMG_ERR_INVALID_RESOURCE | The requested resource is invalid. |
| -1074397003 | IMG_ERR_BAD_FVAL_ENABLE | The selected FVAL enable mode is invalid. |
| -1074397002 | IMG_ERR_BAD_WRITE_ENABLE_MODE | The specified combination of enable lines is invalid. |
| -1074397001 | IMG_ERR_COMPONENT_MISMATCH | Internal Error: The installed components of the NI-IMAQ driver software are incompatible. Reinstall NI-IMAQ. |
| -1074397000 | IMG_ERR_FPGA_PROGRAMMING_FAILED | Internal Error: The attempt to download the program to an FPGA was unsuccessful. |
| -1074396999 | IMG_ERR_CONTROL_FPGA_FAILED | Internal Error: The control FPGA did not initialize properly. |
| -1074396998 | IMG_ERR_CHIP_NOT_READABLE | Internal Error: Attempted to read a write-only chip. |
| -1074396997 | IMG_ERR_CHIP_NOT_WRITABLE | Internal Error: Attempted to write to a read-only chip. |
| -1074396996 | IMG_ERR_I2C_BUS_FAILED | Internal Error: The I2C bus did not respond correctly. |
| -1074396995 | IMG_ERR_DEVICE_IN_USE | The requested image acquisition device is already in use. |
| -1074396994 | IMG_ERR_BAD_TAP_DATALANES | The requested data lanes on a particular tap are invalid. |
| -1074396993 | IMG_ERR_BAD_VIDEO_GAIN | The requested video gain value is out of range. |
| -1074396992 | IMG_ERR_VHA_MODE_NOT_ALLOWED | The current device configuration does not allow VHA mode. |
| -1074396991 | IMG_ERR_BAD_TRACKING_SPEED | The color video tracking speed is invalid. |
| -1074396990 | IMG_ERR_BAD_COLOR_INPUT_SELECT | The selected input connector is not valid. |
| -1074396989 | IMG_ERR_BAD_HAV_OFFSET | The offset value for the Horizontal Active Video color decoder setting is invalid. |
| -1074396988 | IMG_ERR_BAD_HS1_OFFSET | The Horizontal Sync 1offset value for the color decoder is invalid. |
| -1074396987 | IMG_ERR_BAD_HS2_OFFSET | The Horizontal Sync 2 offset value for the color decoder is invalid. |
| -1074396986 | IMG_ERR_BAD_IF_CHROMA | The chroma IF compensation setting is invalid. |
| -1074396985 | IMG_ERR_BAD_COLOR_OUTPUT_FORMAT | The color output format is invalid. |
| -1074396984 | IMG_ERR_BAD_SAMSUNG_SCHCMP | The phase constant specified for the color decoder is invalid. |
| -1074396983 | IMG_ERR_BAD_SAMSUNG_CDLY | The chroma path group delay setting is invalid. |
| -1074396982 | IMG_ERR_BAD_SECAM_DETECT | The SECAM detection method is invalid. |
| -1074396981 | IMG_ERR_BAD_FSC_DETECT | The FSC detection method is invalid. |
| -1074396980 | IMG_ERR_BAD_SAMSUNG_CFTC | The chroma frequency tracking time constant is invalid. |
| -1074396979 | IMG_ERR_BAD_SAMSUNG_CGTC | The chroma gain tracking time constant setting is invalid. |
| -1074396978 | IMG_ERR_BAD_SAMSUNG_SAMPLE_RATE | The pixel sampling rate is invalid. |
| -1074396977 | IMG_ERR_BAD_SAMSUNG_VSYNC_EDGE | The requested VSYNC edge to synchronize with is invalid. |
| -1074396976 | IMG_ERR_SAMSUNG_LUMA_GAIN_CTRL | The method used to control the gain setting for luminance is invalid. |
| -1074396975 | IMG_ERR_BAD_SET_COMB_COEF | The chrominance comb coefficients setting is invalid. |
| -1074396974 | IMG_ERR_SAMSUNG_CHROMA_TRACK | The method used to track chrominance is invalid. |
| -1074396973 | IMG_ERR_SAMSUNG_DROP_LINES | The algorithm for dropping video lines is invalid. |
| -1074396972 | IMG_ERR_VHA_OPTIMIZATION_NOT_ALLOWED | VHA optimization is not applicable for the current configuration. |
| -1074396971 | IMG_ERR_BAD_PG_TRANSITION | A pattern generation is invalid. |
| -1074396970 | IMG_ERR_TOO_MANY_PG_TRANSITIONS | The number of pattern generation transitions exceeds the maximum allowed for the selected image acquisition device. |
| -1074396969 | IMG_ERR_BAD_CL_DATA_CONFIG | The data configuration for the channel link chip is invalid. |
| -1074396968 | IMG_ERR_BAD_OCCURRENCE | The requested occurrence is invalid. |
| -1074396967 | IMG_ERR_BAD_PG_MODE | The pattern generation mode is invalid. |
| -1074396966 | IMG_ERR_BAD_PG_SOURCE | The pattern generation source signal is invalid. |
| -1074396965 | IMG_ERR_BAD_PG_GATE | The pattern generation gate signal is invalid. |
| -1074396964 | IMG_ERR_BAD_PG_GATE_POLARITY | The pattern generation gate polarity is invalid. |
| -1074396963 | IMG_ERR_BAD_PG_WAVEFORM_INITIAL_STATE | The initial state for the pattern generation waveform is invalid. |
| -1074396962 | IMG_ERR_INVALID_CAMERA_ATTRIBUTE | The requested camera attribute is invalid. |
| -1074396961 | IMG_ERR_BOARD_CLOSED | The request failed because the device is closed. |
| -1074396960 | IMG_ERR_FILE_NOT_FOUND | The requested file could not be found. |
| -1074396959 | IMG_ERR_BAD_1409_DSP_FILE | The dspfilter1409.bin file is corrupt or missing. |
| -1074396958 | IMG_ERR_BAD_SCARABXCV200_32_FILE | The scarabXCV200.bin file is corrupt or missing. |
| -1074396957 | IMG_ERR_BAD_SCARABXCV200_16_FILE | The scarab16bit.bin file is corrupt or missing. |
| -1074396956 | IMG_ERR_BAD_CAMERA_LINK_FILE | The Camera Link FPGA bin file is corrupt or missing. |
| -1074396955 | IMG_ERR_BAD_1411_CSC_FILE | The colorspace.bin file is corrupt or missing. |
| -1074396954 | IMG_ERR_BAD_ERROR_CODE | The error code passed into imgShowError is unknown. |
| -1074396953 | IMG_ERR_DRIVER_TOO_OLD | The image acquisition device requires a newer version of the NI-IMAQ driver software. |
| -1074396952 | IMG_ERR_INSTALLATION_CORRUPT | The NI-IMAQ driver software installation is corrupt. |
| -1074396951 | IMG_ERR_NO_ONBOARD_MEMORY | NI-IMAQ cannot perform an onboard acquisition because there is no onboard memory. |
| -1074396950 | IMG_ERR_BAD_BAYER_PATTERN | The Bayer pattern specified is invalid. |
| -1074396949 | IMG_ERR_CANNOT_INITIALIZE_BOARD | The image acquisition device is not operating correctly and cannot be initialized. |
| -1074396948 | IMG_ERR_CALIBRATION_DATA_CORRUPT | The stored calibration data has been corrupted. |
| -1074396947 | IMG_ERR_DRIVER_FAULT | NI-IMAQ attempted to perform an illegal operation. |
| -1074396946 | IMG_ERR_ADDRESS_OUT_OF_RANGE | NI-IMAQ attempted to access a chip beyond the applicable addressable range. |
| -1074396945 | IMG_ERR_ONBOARD_ACQUISITION | The requested operation is not valid for onboard acquisitions. |
| -1074396944 | IMG_ERR_NOT_AN_ONBOARD_ACQUISITION | The requested operation is valid only for onboard acquisitions. |
| -1074396943 | IMG_ERR_BOARD_ALREADY_INITIALIZED | NI-IMAQ attempted to call an initialization function on an image acquisition device that was already initialized. |
| -1074396942 | IMG_ERR_NO_SERIAL_PORT | The image acquisition device does not have a serial port. Serial functions are invalid. |
| -1074396941 | IMG_ERR_BAD_VENABLE_GATING_MODE | The VENABLE gating mode selection is invalid. |
| -1074396940 | IMG_ERR_BAD_1407_LUT_FILE | The lutfpga1407.bin file is corrupt or missing. |
| -1074396939 | IMG_ERR_BAD_SYNC_DETECT_LEVEL | The synchronization signal detection level is out of range. |
| -1074396938 | IMG_ERR_BAD_1405_GAIN_FILE | The gain1405.bin file is corrupt or missing. |
| -1074396937 | IMG_ERR_CLAMP_DAC_NOT_PRESENT | The image acquisition device does not have a clamp DAC. |
| -1074396936 | IMG_ERR_GAIN_DAC_NOT_PRESENT | The image acquisition device does not have a gain DAC. |
| -1074396935 | IMG_ERR_REF_DAC_NOT_PRESENT | The image acquisition device does not have a reference DAC. |
| -1074396934 | IMG_ERR_BAD_SCARABXC2S200_FILE | The scarabXC2S200.bin file is corrupt or missing. |
| -1074396933 | IMG_ERR_BAD_LUT_GAIN | The specified LUT gain is invalid. |
| -1074396932 | IMG_ERR_BAD_MAX_BUF_LIST_ITER | The requested number of buffer lists for an onboard acquisition is invalid. |
| -1074396931 | IMG_ERR_BAD_PG_LINE_NUM | The requested line number for pattern generation is invalid. |
| -1074396930 | IMG_ERR_BAD_BITS_PER_PIXEL | The requested number of bits per pixel is invalid. |
| -1074396929 | IMG_ERR_TRIGGER_ALARM | Triggers are coming in too fast to handle them and maintain system responsiveness. Check for noise on your trigger line. |
| -1074396928 | IMG_ERR_BAD_SCARABXC2S200_03052009_FILE | The scarabXC2S200_03052009.bin file is corrupt or missing. |
| -1074396927 | IMG_ERR_LUT_CONFIG | Internal Error: An error occurred while configuring the LUT. |
| -1074396926 | IMG_ERR_CONTROL_FPGA_REQUIRES_NEWER_DRIVER | A firmware update has been applied to the device. The image acquisition device requires a newer version of the NI-IMAQ driver software to work with the update. |
| -1074396925 | IMG_ERR_CONTROL_FPGA_PROGRAMMING_FAILED | An error occurred while updating the firmware on the device. |
| -1074396924 | IMG_ERR_BAD_TRIGGER_SIGNAL_LEVEL | The trigger line does not support the requested signaling level. |
| -1074396923 | IMG_ERR_CAMERA_FILE_REQUIRES_NEWER_DRIVER | This camera file requires a newer version of NI-IMAQ. |
| -1074396922 | IMG_ERR_DUPLICATED_BUFFER | An image cannot be placed in the same buffer list more than once. |
| -1074396921 | IMG_ERR_NO_ERROR | No error |
| -1074396920 | IMG_ERR_INTERFACE_NOT_SUPPORTED | The camera file does not support the current interface type. |
| -1074396919 | IMG_ERR_BAD_PCLK_POLARITY | The requested polarity for the pixel clock is invalid. |
| -1074396918 | IMG_ERR_BAD_ENABLE_POLARITY | The requested polarity for the enable line is invalid. |
| -1074396917 | IMG_ERR_BAD_PCLK_SIGNAL_LEVEL | The requested signaling level for the pixel clock is invalid. |
| -1074396916 | IMG_ERR_BAD_ENABLE_SIGNAL_LEVEL | The requested signaling level for the enable line is invalid. |
| -1074396915 | IMG_ERR_BAD_DATA_SIGNAL_LEVEL | The requested signaling level for the data lines is invalid. |
| -1074396914 | IMG_ERR_BAD_CTRL_SIGNAL_LEVEL | The requested signaling level for the control lines is invalid. |
| -1074396913 | IMG_ERR_BAD_WINDOW_HANDLE | The requested window handle is invalid. |
| -1074396912 | IMG_ERR_CANNOT_WRITE_FILE | Cannot open the requested file for writing. |
| -1074396911 | IMG_ERR_CANNOT_READ_FILE | Cannot open the requested file for reading. |
| -1074396910 | IMG_ERR_BAD_SIGNAL_TYPE | Cannot wait on the requested signal. |
| -1074396909 | IMG_ERR_BAD_SAMPLES_PER_LINE | The specified number of samples per line is invalid. |
| -1074396908 | IMG_ERR_BAD_SAMPLES_PER_LINE_REF | The specified reference value for samples per line is invalid. |
| -1074396907 | IMG_ERR_USE_EXTERNAL_HSYNC | The current video signal requires an external HSYNC to be used to lock the signal. |
| -1074396906 | IMG_ERR_BUFFER_NOT_ALIGNED | An image buffer is not properly aligned. All image buffers must be aligned to a 4-byte boundary. |
| -1074396905 | IMG_ERR_ROWPIXELS_TOO_SMALL | The number of pixels per row is less than the region of interest width. |
| -1074396904 | IMG_ERR_ROWPIXELS_NOT_ALIGNED | The number of pixels per row is not properly aligned. The total number of bytes per row must be aligned to a 4-byte boundary. |
| -1074396903 | IMG_ERR_ROI_WIDTH_NOT_ALIGNED | The ROI width is not properly aligned. The total number of bytes bounded by the ROI width must be aligned to a 4-byte boundary. |
| -1074396902 | IMG_ERR_LINESCAN_NOT_ALLOWED | Linescan mode is not valid for this tap configuration. |
| -1074396901 | IMG_ERR_INTERFACE_FILE_REQUIRES_NEWER_DRIVER | This interface file requires a newer version of NI-IMAQ. |
| -1074396900 | IMG_ERR_BAD_SKIP_COUNT | The requested skip count value is out of range. |
| -1074396899 | IMG_ERR_BAD_NUM_X_ZONES | The number of X zones in the tap configuration of the camera is invalid. |
| -1074396898 | IMG_ERR_BAD_NUM_Y_ZONES | The number of Y zones in the tap configuration of the camera is invalid. |
| -1074396897 | IMG_ERR_BAD_NUM_TAPS_PER_X_ZONE | The number of taps per X zone in the tap configuration of the camera is invalid. |
| -1074396896 | IMG_ERR_BAD_NUM_TAPS_PER_Y_ZONE | The number of taps per Y zone in the tap configuration of the camera is invalid. |
| -1074396895 | IMG_ERR_BAD_TEST_IMAGE_TYPE | The requested test image type is invalid. |
| -1074396894 | IMG_ERR_CANNOT_ACQUIRE_FROM_CAMERA | This firmware is not capable of acquiring from a camera. |
| -1074396893 | IMG_ERR_BAD_CTRL_LINE_SOURCE | The source for the camera control line is invalid. |
| -1074396892 | IMG_ERR_BAD_PIXEL_EXTRACTOR | The requested pixel extractor is invalid. |
| -1074396891 | IMG_ERR_BAD_NUM_TIME_SLOTS | The requested number of time slots is invalid. |
| -1074396890 | IMG_ERR_BAD_PLL_VCO_DIVIDER | The requested VCO divide down number is invalid. The only valid values are 2, 4, 8 and 16. |
| -1074396889 | IMG_ERR_CRITICAL_TEMP | The device temperature exceeded the critical temperature threshold. |
| -1074396888 | IMG_ERR_BAD_DPA_OFFSET | The requested dynamic phase aligner offset is invalid. |
| -1074396887 | IMG_ERR_BAD_NUM_POST_TRIGGER_BUFFERS | The requested number of post trigger buffers is invalid. |
| -1074396886 | IMG_ERR_BAD_DVAL_MODE | The requested DVAL mode is invalid. |
| -1074396885 | IMG_ERR_BAD_TRIG_GEN_REARM_SOURCE | The requested trigger generator rearm source signal is invalid. |
| -1074396884 | IMG_ERR_BAD_ASM_GATE_SOURCE | The requested ASM gate signal is invalid. |
| -1074396883 | IMG_ERR_TOO_MANY_BUFFERS | The requested number of buffer list buffers is not supported by this image acquisition device. |
| -1074396882 | IMG_ERR_BAD_TAP_4_VALID_RECT | The rectangle defined for Tap 4 is invalid. |
| -1074396881 | IMG_ERR_BAD_TAP_5_VALID_RECT | The rectangle defined for Tap 5 is invalid. |
| -1074396880 | IMG_ERR_BAD_TAP_6_VALID_RECT | The rectangle defined for Tap 6 is invalid. |
| -1074396879 | IMG_ERR_BAD_TAP_7_VALID_RECT | The rectangle defined for Tap 7 is invalid. |
| -1074396878 | IMG_ERR_FRONT_END_BANDWIDTH_EXCEEDED | The camera is providing image data faster than the image acquisition device can receive it. |
| -1074396877 | IMG_ERR_BAD_PORT_NUMBER | The requested port number does not exist. |
| -1074396876 | IMG_ERR_PORT_CONFIG_CONFLICT | The requested port cannot be cannot be configured due to a conflict with another port that is currently opened. |
| -1074396875 | IMG_ERR_BITSTREAM_INCOMPATIBLE | The requested bitstream is not compatible with the image acquisition device. |
| -1074396874 | IMG_ERR_SERIAL_PORT_IN_USE | The requested serial port is currently in use and is not accessible. |
| -1074396873 | IMG_ERR_BAD_ENCODER_DIVIDE_FACTOR | The requested encoder divide factor is invalid. |
| -1074396872 | IMG_ERR_ENCODER_NOT_SUPPORTED | Encoder support is not present for this image acquisition device. Please verify that this device is capable of handling encoder signals and that phase A and B are connected. |
| -1074396871 | IMG_ERR_BAD_ENCODER_POLARITY | The requested encoder phase signal polarity is invalid. |
| -1074396870 | IMG_ERR_BAD_ENCODER_FILTER | The requested encoder filter setting is invalid. |
| -1074396869 | IMG_ERR_ENCODER_POSITION_NOT_SUPPORTED | This image acquisition device does not support reading the absolute encoder position. |
| -1074396868 | IMG_ERR_IMAGE_IN_USE | The image appears to be in use. Please name the images differently to avoid this situation. |
| -1074396867 | IMG_ERR_BAD_SCARABXL4000_FILE | The scarab.bin file is corrupt or missing. |
| -1074396866 | IMG_ERR_BAD_CAMERA_ATTRIBUTE_VALUE | The requested camera attribute value is invalid. For numeric camera attributes, please ensure that the value is properly aligned and within the allowable range. |
| -1074396865 | IMG_ERR_BAD_PULSE_WIDTH | The requested pulse width is invalid. |
| -1074396864 | IMG_ERR_FPGA_FILE_NOT_FOUND | The requested FPGA bitstream file could not be found. |
| -1074396863 | IMG_ERR_FPGA_FILE_CORRUPT | The requested FPGA bitstream file is corrupt. |
| -1074396862 | IMG_ERR_BAD_PULSE_DELAY | The requested pulse delay is invalid. |
| -1074396861 | IMG_ERR_BAD_PG_IDLE_SIGNAL_LEVEL | The pattern generation (PG) idle state is invalid. Camera control lines sourced from the PG unit must be all tristate or all non-tristate. |
| -1074396860 | IMG_ERR_BAD_PG_WAVEFORM_IDLE_STATE | The idle state for the pattern generation waveform is invalid. |
| -1074396859 | IMG_ERR_64_BIT_MEMORY_NOT_SUPPORTED | This device only supports acquiring into the 32-bit address space; however, portions of the image buffer list reside outside of 32-bit physical memory. |
| -1074396858 | IMG_ERR_64_BIT_MEMORY_UPDATE_AVAILABLE | This 32-bit device is operating on a 64-bit OS with more than 3GB of physical memory. An update is available to allow acquisitions into 64-bit physical memory. Launch the updater from the menu in MAX: Tools»NI Vision»Update NI-IMAQ Device Firmware. |
| -1074396857 | IMG_ERR_32_BIT_MEMORY_LIMITATION | This 32-bit device is operating on a 64-bit OS with more than 3GB of physical memory. This configuration could allocate 64-bit memory which is unsupported by the device. To solve this problem, reduce the amount of physical memory in the system. |
| -1074396856 | IMG_ERR_KERNEL_NOT_LOADED | The kernel component of the driver, niimaqk.sys, is not loaded. Verify that an IMAQ device is in your system or reinstall the driver. |
| -1074396855 | IMG_ERR_BAD_SENSOR_SHUTTER_PERIOD | The sensor shutter period is invalid. Check the horizontal and vertical shutter period values. |
| -1074396854 | IMG_ERR_BAD_SENSOR_CCD_TYPE | The sensor CCD type is invalid. |
| -1074396853 | IMG_ERR_BAD_SENSOR_PARTIAL_SCAN | The sensor partial scan mode is invalid. |
| -1074396852 | IMG_ERR_BAD_SENSOR_BINNING | The sensor binning mode is invalid. |
| -1074396851 | IMG_ERR_BAD_SENSOR_GAIN | The sensor gain value is invalid. |
| -1074396850 | IMG_ERR_BAD_SENSOR_BRIGHTNESS | The sensor brightness value is invalid. |
| -1074396849 | IMG_ERR_BAD_LED_STATE | The LED state is invalid. |
| -1074396848 | IMG_ERR_64_BIT_NOT_SUPPORTED | The operation is not supported for 64-bit applications. |
| -1074396847 | IMG_ERR_BAD_TRIGGER_DELAY | The requested trigger delay value is not supported. |
| -1074396846 | IMG_ERR_LIGHTING_CURRENT_EXCEEDS_LIMITS | The configured lighting current level exceeds the hardware or user's configured limits. |
| -1074396845 | IMG_ERR_LIGHTING_INVALID_MODE | The configured lighting mode is invalid. |
| -1074396844 | IMG_ERR_LIGHTING_EXTERNAL_INVALID_MODE | The configured external lighting mode is invalid. |
| -1074396843 | IMG_ERR_BAD_SENSOR_EXPOSURE | The sensor exposure time is invalid. |
| -1074396842 | IMG_ERR_BAD_FRAME_RATE | The frame rate is invalid for the current configuration. |
| -1074396841 | IMG_ERR_BAD_SENSOR_PARTIAL_SCAN_BINNING_COMBINATION | The partial scan mode / binning mode combination is invalid. |
| -1074396840 | IMG_ERR_SOFTWARE_TRIGGER_NOT_CONFIGURED | The requested software trigger is not configured. |
| -1074396839 | IMG_ERR_FREE_RUN_MODE_NOT_ALLOWED | Free-run mode is not allowed in the current configuration. This is typically caused by simultaneously enabling free-run mode and a triggered acquisition. |
| -1074396838 | IMG_ERR_BAD_LIGHTING_RAMPUP | The lighting ramp-up delay is either less than the minimum value allowed or larger than the maximum time that the light is allowed to be on. |
| -1074396837 | IMG_ERR_AFE_CONFIG_TIMEOUT | Internal Error: A write to the AFEConfig register did not complete properly. |
| -1074396836 | IMG_ERR_LIGHTING_ARM_TIMEOUT | Internal Error: The arming of the lighting controller did not complete properly. |
| -1074396835 | IMG_ERR_LIGHTING_SHORT_CIRCUIT | The Direct Drive lighting controller has detected an abnormal load condition, such as a short circuit. Correct the abnormal load condition before restarting the acquisition. |
| -1074396834 | IMG_ERR_BAD_BOARD_HEALTH | The board health register has indicated an internal problem. |
| -1074396833 | IMG_ERR_LIGHTING_BAD_CONTINUOUS_CURRENT_LIMIT | The requested continuous current limit for the lighting controller is less than the minimum allowed current level. |
| -1074396832 | IMG_ERR_LIGHTING_BAD_STROBE_DUTY_CYCLE_LIMIT | The requested duty cycle limit for the lighting controller strobe mode is invalid. |
| -1074396831 | IMG_ERR_LIGHTING_BAD_STROBE_DURATION_LIMIT | The requested duration limit for the lighting controller strobe mode is invalid. |
| -1074396830 | IMG_ERR_BAD_LIGHTING_CURRENT_EXPOSURE_COMBINATION | The lighting current is invalid because the exposure time plus the lighting ramp-up time exceeds either the strobe duration limit or the strobe duty cycle limit. |
| -1074396829 | IMG_ERR_LIGHTING_HEAD_CONFIG_NOT_FOUND | The configuration for the desired light head was not found. |
| -1074396828 | IMG_ERR_LIGHTING_HEAD_DATA_CORRUPT | The data for the desired light head configuration is invalid or corrupt. |
| -1074396827 | IMG_ERR_LIGHTING_ABORT_TIMEOUT | Internal Error: The abort of the lighting controller did not complete properly. |
| -1074396826 | IMG_ERR_LIGHTING_BAD_STROBE_CURRENT_LIMIT | The requested strobe current limit for the lighting controller is less than the minimum allowed current. |
| -1074396825 | IMG_ERR_DMA_ENGINE_UNRESPONSIVE | Internal Error: The DMA engine is unresponsive. Reboot the target. If the problem persists contact National Instruments. |
| -1074396824 | IMG_ERR_IMAGE_NOT_32BYTE_ALIGNED | The image width is not a multiple of 32-bytes. The current configuration requires that the image width be a multiple of 32-bytes. |
| -1074396823 | IMG_ERR_IMAGE_BORDER_NONZERO | The image border is not zero. The current configuration requires that the image have no border. |
| -1074396822 | IMG_ERR_UNKNOWN_CAMERA_FILE | No valid camera file selected for this interface. |
| -1074396821 | IMG_ERR_ONBOARD_DECODING_NOT_CHANGEABLE_DURING_ACQ | The Bayer pattern cannot be change to None or away from None while the acquisition is running and onboard Bayer decoding is enabled. |
| -1074396820 | IMG_ERR_BAD_BAYER_GAIN_FOR_ONBOARD_DECODE | The specified Bayer gain is not supported when onboard Bayer decoding is enabled. |
| -1074396819 | IMG_ERR_BAD_BAYER_PATTERN_FOR_ONBOARD_DECODE | The specified Bayer pattern is not supported when onboard Bayer decoding is enabled. |
| -1074396818 | IMG_ERR_BAD_NUM_COMPONENTS_FOR_ONBOARD_DECODE | The number of components value in the camera file must be 1 when onboard Bayer decoding is enabled. |
| -1074396817 | IMG_ERR_BAD_NUM_PHANTOM_COMPONENTS_FOR_ONBOARD_DECODE | The number of phantom components value in the camera file must be 0 when onboard Bayer decoding is enabled. |
| -1074396816 | IMG_ERR_POCL_FAULT | The Power Over CameraLink circuitry has encountered an unexpected error. |
| -1074396815 | IMG_ERR_POCL_VIDEO_LOCK | The Power Over CameraLink circuitry is unable to provide power and the device cannot detect a recognizable video source. |
| -1074396814 | IMG_ERR_POCL_BAD_FUSE | The Power Over CameraLink circuitry cannot provide power due to a blown fuse. |
| -1074396813 | IMG_ERR_POCL_NO_AUX_POWER | The Power Over CameraLink circuitry cannot provide power due to a missing auxilliary power connection |
| -1074396812 | IMG_ERR_PULSE_UPDATE_NOT_SUPPORTED | This image acquisition device does not support updating pulses. |
| -1074396811 | IMG_ERR_BAD_BITS_PER_COMPONENT_FOR_ONBOARD_DECODE | The bits per component value in the camera file must be less than 16 when onboard Bayer decoding is enabled. |
| -1074396810 | IMG_ERR_IO_BOARD_NOT_PRESENT | The requested configuration requires the IO extension board, but the IO extension board is not connected. |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_acquire_field.html language=enus -->
## TOPIC 00011: IMG_ATTR_ACQUIRE_FIELD

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_acquire_field.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_acquire_field.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_ACQUIRE_FIELD

Gets/sets the field acquired when IMG_ATTR_FRAME_FIELD is set to FIELD_MODE. When you are using FRAME_MODE, this attribute is the first field that is acquired in time.

#### Values

The following list includes possible constant values:

- IMG_ACQUIRE_ALL —Acquires all fields.
- IMG_ACQUIRE_EVEN —Acquires only even fields.
- IMG_ACQUIRE_ODD —Acquires only odd fields.
- IMG_ACQUIRE_ALTERNATING —Acquires all fields and uses IMG_ATTR_START_FIELD to determine the first field to acquire.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_acqwindow_height.html language=enus -->
## TOPIC 00012: IMG_ATTR_ACQWINDOW_HEIGHT

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_acqwindow_height.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_acqwindow_height.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_ACQWINDOW_HEIGHT

Gets/sets the acquisition window height of the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_acqwindow_left.html language=enus -->
## TOPIC 00013: IMG_ATTR_ACQWINDOW_LEFT

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_acqwindow_left.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_acqwindow_left.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_ACQWINDOW_LEFT

Gets/sets the acquisition window left offset of the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_acqwindow_top.html language=enus -->
## TOPIC 00014: IMG_ATTR_ACQWINDOW_TOP

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_acqwindow_top.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_acqwindow_top.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_ACQWINDOW_TOP

Gets/sets the acquisition window top offset of the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_acqwindow_width.html language=enus -->
## TOPIC 00015: IMG_ATTR_ACQWINDOW_WIDTH

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_acqwindow_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_acqwindow_width.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_ACQWINDOW_WIDTH

Gets/sets the acquisition window width of the camera/channel associated 
 with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bayer_algorithm.html language=enus -->
## TOPIC 00016: IMG_ATTR_BAYER_ALGORITHM

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bayer_algorithm.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bayer_algorithm.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BAYER_ALGORITHM

The Bayer decode algorithm. This value is ignored when using onboard Bayer decoding.

#### Values

The following list includes possible values:

- Bilinear —
- VNG (Variable Number of Gradients) —

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Always | All frame grabbers |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bayer_blue_gain.html language=enus -->
## TOPIC 00017: IMG_ATTR_BAYER_BLUE_GAIN

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bayer_blue_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bayer_blue_gain.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BAYER_BLUE_GAIN

The Bayer blue gain.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| Double | Always | Always | All frame grabbers |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bayer_green_gain.html language=enus -->
## TOPIC 00018: IMG_ATTR_BAYER_GREEN_GAIN

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bayer_green_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bayer_green_gain.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BAYER_GREEN_GAIN

The Bayer green gain.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| Double | Always | Always | All frame grabbers |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bayer_onboard_decode_enable.html language=enus -->
## TOPIC 00019: IMG_ATTR_BAYER_ONBOARD_DECODE_ENABLE

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bayer_onboard_decode_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bayer_onboard_decode_enable.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BAYER_ONBOARD_DECODE_ENABLE

Determines whether to enable onboard Bayer decoding

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCIe-1437 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bayer_onboard_decode_force_rgb32.html language=enus -->
## TOPIC 00020: IMG_ATTR_BAYER_ONBOARD_DECODE_FORCE_RGB32

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bayer_onboard_decode_force_rgb32.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bayer_onboard_decode_force_rgb32.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BAYER_ONBOARD_DECODE_FORCE_RGB32

Determines whether to force the decoded RGB image to be 32 bits. By default pixel depths greater than 8 return a 64-bit RGB image.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCIe-1437 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bin_threshold_high.html language=enus -->
## TOPIC 00021: IMG_ATTR_BIN_THRESHOLD_HIGH

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bin_threshold_high.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bin_threshold_high.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BIN_THRESHOLD_HIGH

The upper limit for the binary threshold LUT.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | Configuration | NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/img_attr_bitsperpixel.html language=enus -->
## TOPIC 00022: IMG_ATTR_BITSPERPIXEL

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/img_attr_bitsperpixel.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/img_attr_bitsperpixel.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMG_ATTR_BITSPERPIXEL

Returns the bits per pixel value of the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
| uInt32 | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/imgsessionopen.html language=enus -->
## TOPIC 00023: imgSessionOpen

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/imgsessionopen.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/imgsessionopen.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### imgSessionOpen

#### Usage

rval imgSessionOpen(INTERFACE_ID ifid, SESSION_ID* psid);

#### Purpose

Opens a session and returns a session ID. 
This function inherits all data associated with the given interface.

#### Parameters

| Name | Type | Direction |
| --- | --- | --- |
| ifid | INTERFACE_ID | input |
| psid | SESSION_ID* | output |
| rval | Int32 | output |

#### Parameter Discussion

**ifid:** valid INTERFACE_ID.

**psid:** pointer to a SESSION_ID variable. If the function succeeds, 
the variable is populated with a valid SESSION_ID that you can use in subsequent functions.

#### Return Value

This function returns 0 on success. On failure, this function returns an error code. For information about the error code, call [imgShowError](imgshowerror.html).

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/imgsessionreleasebuffer.html language=enus -->
## TOPIC 00024: imgSessionReleaseBuffer

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/imgsessionreleasebuffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/imgsessionreleasebuffer.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### imgSessionReleaseBuffer

#### Usage

rval imgSessionReleaseBuffer(SESSION_ID sid);

#### Purpose

Releases an image that was previously held with 
[imgSessionExamineBuffer](imgsessionexaminebuffer.html). This 
function has the effect of re-entering an image into a continuous ring buffer 
pool after analysis.

#### Parameters

| Name | Type | Direction |
| --- | --- | --- |
| sid | SESSION_ID | input |
| rval | Int32 | output |

#### Parameter Discussion

**sid:** valid SESSION_ID.

#### Return Value

This function returns 0 on success. On failure, this function returns an error code. For information about the error code, call [imgShowError](imgshowerror.html).

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/imgsessionserialwrite.html language=enus -->
## TOPIC 00025: imgSessionSerialWrite

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/imgsessionserialwrite.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/imgsessionserialwrite.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### imgSessionSerialWrite

#### Usage

rval imgSessionSerialWrite(SESSION_ID sid, const void* buffer, uInt32* bufSize, uInt32 timeout);

#### Purpose

Writes data to the serial port. Serial communication parameters, such as baud rate, are set in the camera file associated with the session. You can adjust these communication parameters directly in the camera file.

#### Parameters

| Name | Type | Direction |
| --- | --- | --- |
| sid | SESSION_ID | input |
| buffer | const void* | input |
| bufSize | uInt32* | input/output |
| timeout | uInt32 | input |
| rval | Int32 | output |

#### Parameter Discussion

**sid:** valid SESSION_ID.

**buffer:** data to send.

**bufSize:** on input, the number of bytes to send. On return, the number of bytes written.

**timeout:** time, in milliseconds, to wait for the data to be written. Use IMG_TIMEOUT_INFINITE to wait indefinitely.

#### Return Value

This function returns 0 on success. On failure, this function returns an error code. For information about the error code, call [imgShowError](imgshowerror.html).

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/labwindows_cvi.html language=enus -->
## TOPIC 00026: LabWindows/CVI

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/labwindows_cvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/labwindows_cvi.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI

Inside the LabWindows/CVI environment, select **Libraries»NI-IMAQ** to access the NI-IMAQ functions. Each function panel represents an NI-IMAQ function, which is displayed at the bottom of the panel.

The following table shows the organization of the LabWindows/CVI function panel tree and the NI-IMAQ function name that corresponds to each function panel.

| LabWindows/CVI Function Panel | NI-IMAQ Function |
| --- | --- |
| Interface Functions |  |
| Interface Open | imgInterfaceOpen |
| Session Open | imgSessionOpen |
| Close Object | imgClose |
| Interface Query Names | imgInterfaceQueryNames |
| Interface Reset | imgInterfaceReset |
| High-Level Snap Functions |  |
| Snap | imgSnap |
| Snap Area | imgSnapArea |
| High-Level Grab Functions |  |
| Grab | imgGrab |
| Grab Area | imgGrabArea |
| Grab Setup | imgGrabSetup |
| High-Level Ring and Sequence Functions |  |
| Ring Setup | imgRingSetup |
| Sequence Setup | imgSequenceSetup |
| Session Start Acquisition | imgSessionStartAcquisition |
| Session Stop Acquisition | imgSessionStopAcquisition |
| High-Level Signal I/O Functions |  |
| Encoder Reset Position | imgEncoderResetPosition |
| Line Trigger Source | imgSessionLineTrigSource2 |
| Pulse Create | imgPulseCreate2 |
| Pulse Dispose | imgPulseDispose |
| Pulse Rate | imgPulseRate |
| Pulse Start | imgPulseStart |
| Pulse Stop | imgPulseStop |
| Trigger Configure | imgSessionTriggerConfigure2 |
| Trigger Clear | imgSessionTriggerClear |
| Trigger Drive | imgSessionTriggerDrive2 |
| Trigger Read | imgSessionTriggerRead2 |
| Trigger Route | imgSessionTriggerRoute2 |
| Wait Signal | imgSessionWaitSignal2 |
| Wait Signal Asynchronous | imgSessionWaitSignalAsync3 |
| High-Level Miscellaneous Functions |  |
| Session Get Buffer Size | imgSessionGetBufferSize |
| Session Get ROI | imgSessionGetROI |
| Session Configure ROI | imgSessionConfigureROI |
| Session Status | imgSessionStatus |
| Session Fit ROI | imgSessionFitROI |
| Low-Level Acquisition Functions |  |
| Session Abort | imgSessionAbort |
| Session Acquire | imgSessionAcquire |
| Session Configure | imgSessionConfigure |
| Session Copy Area | imgSessionCopyArea |
| Session Copy Buffer | imgSessionCopyBuffer |
| Session Examine Buffer | imgSessionExamineBuffer |
| Session Release Buffer | imgSessionReleaseBuffer |
| Low-Level Attribute Functions |  |
| Get Attribute | imgGetAttribute |
| Set Attribute | imgSetAttribute |
| Get Camera Attribute Numeric | imgGetCameraAttributeNumeric |
| Set Camera Attribute Numeric | imgSetCameraAttributeNumeric |
| Get Camera Attribute String | imgGetCameraAttributeString |
| Set Camera Attribute String | imgSetCameraAttributeString |
| Set User LUT 8 bit | imgSessionSetUserLUT8bit |
| Set User LUT 16 bit | ImgSessionSetUserLUT16bit |
| Low-Level Buffer Management Functions |  |
| Create Buffer | imgCreateBuffer |
| Create Buffer List | imgCreateBufList |
| Dispose Buffer | imgDisposeBuffer |
| Dispose Buffer List | imgDisposeBufList |
| Get Buffer Element | imgGetBufferElement |
| Set Buffer Element | imgSetBufferElement |
| Low-Level Utility Functions |  |
| Bayer Color Decode | imgBayerColorDecode |
| Calculate Bayer Color LUT | imgCalculateBayerColorLUT |
| Plot Buffer to DC | imgPlotDC |
| Plot Buffer to Window | imgPlot |
| Session Save Buffer | imgSessionSaveBufferEx |
| Show Error | imgShowError |
| Low-Level Serial Communication Functions |  |
| Session Serial Flush | imgSessionSerialFlush |
| Session Serial Read | imgSessionSerialRead |
| Session Serial Read Bytes | imgSessionSerialReadBytes |
| Session Serial Write | imgSessionSerialWrite |

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/scaled_encoder_signal.html language=enus -->
## TOPIC 00027: Scaled Encoder Signal

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/scaled_encoder_signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/scaled_encoder_signal.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Scaled Encoder Signal

The scaled encoder signal is an edge-sensitive signal that is used to track cumulative forward progression of the quadrature encoder Phase A and Phase B signals. The scaled encoder signal is derived by applying a divide factor to the raw positional signal that is encoded between Phase A and Phase B.

All NI image acquisition devices expect the raw positional signal to be encoded with quadrature encoding. The scaled encoder signal can be used as a line trigger, as a timebase for pulse generation, and it can be driven out on a trigger line for external usage. The following figure illustrates the scaled encoder signal that is produced when using a divide factor of six.

|  |  |
| --- | --- |
| 1 Phase A Signal | 3 Position |
| 2 Phase B Signal | 4 Scaled Encoder Signal |

NI image acquisition devices that support multiple ports have a unique scaler per port. The unique scaler allows you to simultaneously acquire from multiple line scan cameras using different line rates that are all synchronous to the same quadrature encoder. Some NI image acquisition devices also support querying the absolute position counter value. Refer to the image acquisition device documentation to determine if the device supports querying the absolute position counter.

Refer to the [Quadrature Encoder Overview](quadrature_encoder_overview.html) for more information about quadrature encoders.

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/signal_io_functions.html language=enus -->
## TOPIC 00028: Signal I/O Functions

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/signal_io_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/signal_io_functions.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Signal I/O Functions

Use the signal I/O functions to control the trigger lines on image acquisition devices. You can use these functions to start an acquisition based on a trigger, output status signals on a trigger line, wait for a specified signal to occur, or output pulses on the trigger lines.

[imgSessionTriggerConfigure2](imgsessiontriggerconfigure2.html)

[imgSessionLineTrigSource2](imgsessionlinetrigsource2.html)

[imgSessionTriggerClear](imgsessiontriggerclear.html)

[imgSessionTriggerDrive2](imgsessiontriggerdrive2.html)

[imgSessionTriggerRoute2](imgsessiontriggerroute2.html)

[imgSessionTriggerRead2](imgsessiontriggerread2.html)

[imgSessionWaitSignal2](imgsessionwaitsignal2.html)

[imgSessionWaitSignalAsync3](imgsessionwaitsignalasync3.html)

[imgEncoderResetPosition](imgencoderresetposition.html)

[imgPulseCreate2](imgpulsecreate2.html)

[imgPulseDispose](imgpulsedispose.html)

[imgPulseRate](imgpulserate.html)

[imgPulseStart](imgpulsestart.html)

[imgPulseStop](imgpulsestop.html)

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/utility_functions.html language=enus -->
## TOPIC 00029: Utility Functions

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/utility_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/utility_functions.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Utility Functions

Use the utility functions to display an image in a window, save an image to a file, or get detailed error information.

[imgPlot](imgplot.html)

[imgPlotDC](imgplotdc.html)

[imgSessionSaveBufferEx](imgsessionsavebufferex.html)

[imgShowError](imgshowerror.html)

[imgBayerColorDecode](imgbayercolordecode.html)

[imgCalculateBayerColorLUT](imgcalculatebayercolorlut.html)

<!--NI_TOPIC bundle=ni-imaq-c-api-ref path=niimaqfunctionreference/variable_data_types.html language=enus -->
## TOPIC 00030: Variable Data Types

- bundle_id: `ni-imaq-c-api-ref`
- source_path: `niimaqfunctionreference/variable_data_types.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-c-api-ref/raw/resource/enus/niimaqfunctionreference/variable_data_types.html
- document_id: `ni-imaq-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Variable Data Types

Every function description has a parameter table that lists the data types for each parameter. Refer to [Primary Data Types](primary_types.html) for notation descriptions used in parameter tables and throughout the documentation for variable data types.
