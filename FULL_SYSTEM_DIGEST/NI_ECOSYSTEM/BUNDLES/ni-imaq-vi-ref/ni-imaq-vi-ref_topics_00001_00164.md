# NI DOCUMENT BUNDLE: ni-imaq-vi-ref

<!--NI_BUNDLE_CHUNK bundle=ni-imaq-vi-ref start=1 end=164 -->
<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/1473r_signal_reference.html language=enus -->
## TOPIC 00001: NI 1473R I/O Signal Reference

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/1473r_signal_reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/1473r_signal_reference.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI 1473R I/O Signal Reference

The following table describes the NI 1473R I/O signals.

| CLIP Signal Name | Data Type | Read/Write | Description |
| --- | --- | --- | --- |
| Clocks |  |  |  |
| 40 MHz Onboard Clock | Clock | N/A | A 40 MHz time base. The Camera Link UART signals must be read and written synchronously to this clock. |
| 100 MHz Image Data Clock | Clock | N/A | A 100 MHz time base. Camera Link Data signals must be read synchronously to this clock. If desired, image processing may be done on a slower clock domain by using a FIFO to bring the image data and control to a slower clock domain. Note: Because 100 MHz is faster than the fastest Camera Link pixel clock rate (85 MHz), the reading logic is guaranteed to keep up with incoming camera data. |
| Configuration Signals |  |  |  |
| Configuration Signals must be set before initializing an acquisition. They must be set using constants in the target FPGA VI before the acquisition initialization, or using controls in the target FPGA VI that are set by the host VI before the FPGA VI is run. |  |  |  |
| CL Set Signal Mapping | U8 | Write | Sets the signal mapping to use for the Camera Link connectors: 0 = Standard Camera Link 1 = Basler 10-tap 2 = Vossküler 10-tap If not driven, CL Set Signal Mapping defaults to 0 (Standard Camera Link). |
| CL Set Configuration | U8 | Write | Sets the Camera Link configuration: 0 = Base 1 = Medium 2 = Full/Extended/10-tap If not driven, CL Set Configuration defaults to 0 (Base). |
| CL Set FVAL Active High CL Set LVAL Active High CL Set DVAL Active High CL Set Spare Active High | Boolean | Write | These signals set the polarity for the indicated Camera Link flag. TRUE = Active high (high true) FALSE = Active low (low true) If not driven, CL Active High signals default to TRUE. |
| CL Set Line Scan | Boolean | Write | When this signal is TRUE, the initialization circuitry does not require a Camera Link FVAL signal to complete initialization. Set to TRUE for a line scan camera. Set to FALSE for an area scan camera. If not driven, CL Set Linescan defaults to FALSE. |
| Acquisition Initialization |  |  |  |
| CL Acq Init | Boolean | Write | This input signal initializes the Camera Link front end. This allows the front end to detect and synchronize with the Camera Link signals from the camera. Initialize this signal to FALSE at the start of your application. The procedure for initialization is as follows: Set the signal mapping, configuration, line scan mode, and flags polarity before running the FPGA, as described above After the FPGA has started, set the CL Acq Init signal to the TRUE Wait until the CL Acq Ready signal becomes TRUE Return the CL Acq Init signal to FALSE Once initialization is complete, you can begin to monitor the Camera Link data and flags signals. |
| CL Acq Ready | Boolean | Read | This output signal indicates when the acquisition initialization has completed and a valid camera source has been detected. If this signal never becomes TRUE, then a valid Camera Link signal could not be detected. |
| Camera Link Data |  |  |  |
| Camera Link Data signals must be used within single-cycle timed loop running on the 100 Mhz Image Data Clock. |  |  |  |
| CL Port A CL Port B ... CL Port J | U8 | Read | Camera Link data output ports. All image data is output on one or more of these ten ports using the Image Data Clock. These ports should be ignored during clock cycles in which CL Output Valid is false. |
| CL Frame Valid CL Line Valid CL Data Valid CL Spare | Boolean | Read | Camera Link enable flags. These signals are always output active high (high true). The enable signals should be ignored during clock cycles in which CL Output Valid is false. |
| CL Output Valid | Boolean | Read | Indicates whether or not the CL Port and CL Valid signals have active data. Because the Image Data Clock is faster than the camera's pixel clock (maximum of 85 MHz), there will be clock cycles in which the Camera Link front end has no data or flags to output. The CL Output Valid will be TRUE for clock cycles that have valid data and/or flags and FALSE during clock cycles that do not. The output of the CL Port and Valid signals should be ignored whenever CL Output Valid is FALSE. |
| Camera Control Lines |  |  |  |
| CL Control 1 CL Control 2 CL Control 3 CL Control 4 | Boolean | Write | When CL Control Enable is TRUE, these signals drive the four camera control signals on the Camera Link cable. |
| Cl Control Enable | Boolean | Write | This signal controls whether the camera control lines on the Camera Link cable are driven by the CL Control signals. TRUE = Enabled (driving) FALSE = Disabled (high impedance) |
| I/O Lines |  |  |  |
| TTL 0 | Boolean | Read/Write | This bidirectional I/O line is tied to the SMB connector on the front panel of the NI PCIe-1473R. |
| TTL 1 TTL 2 TTL 3 TTL 4 TTL 5 TTL 6 TTL 7 TTL 8 | Boolean | Read/Write | These bidirectional I/O lins are tied to the TTL lines on the NI Camera Link I/O Extension Board. |
| RTSI 0 RTSI 1 RTSI 2 RTSI 3 RTSI 4 RTSI 5 RTSI 6 RTSI 7 | Boolean | Read/Write | These bidirectional I/O lines are tied to the RTSI (Real Time System Integration) Bus connector. They can be used to trigger or receive triggers from other PCI/PCIe boards with RTSI connectors. |
| ISO In 0 ISO In 1 ISO In 2 | Boolean | Read | These signals indicate the state of the isolated input lines on the NI Camera Link I/O Extension Board. |
| ISO Out 0 ISO Out 1 ISO Out 2 | Boolean | Write | These signals set the state of the isolated output lines on the NI Camera Link I/O Extension Board. |
| QE Phase A QE Phase B | Boolean | Read | These signals indicate the state of the quadrature encoder phase A and phase B inputs on the NI Camera Link I/O Extension Board. |
| Camera Link Serial Interface (UART) |  |  |  |
| Camera Link Serial Interface (UART) signals must be used within a single-cycle timed loop running on the 40 MHz Onboard Clock. |  |  |  |
| UART Set Baud Rate | Boolean | Write | This signal is used to set the baud rate of the Camera Link serial interface. The procedure for setting the baud rate is as follows: Set the UART Baud Rate In signal to the code for the desired baud rate. Set the UART Set Baud Rate signal to TRUE. Wait until the UART Set Baud Rate Ack signal becomes TRUE. Set the UART Set Baud Rate signal to FALSE. Wait until the UART Set Baud Rate Ack signal becomes FALSE. |
| UART Set Baud Rate Ack | Boolean | Read | This signal acknowledges when the setting of the baud rate has completed. |
| UART Baud Rate In | U8 | Write | This signal is used to set which baud rate to use. It can be any of the standard Camera Link baud rates, as shown below: 1 = 9,600 baud 2 = 19,200 baud 4 = 38,400 baud 8 = 57,600 baud 16 = 115,200 baud 32 = 230,400 baud 64 = 460,800 baud 128 = 921,600 baud |
| UART RX Ready | Boolean | Read | Indicates that the UART has received data that is ready to be read. |
| UART Read Enable | Boolean | Write | This signal is used to read a received byte from the UART. When the UART RX Ready signal is TRUE, set this signal to TRUE for exactly two clock cycles then set it to FALSE for at least one clock cycle to perform the read. The byte will be output on the UART Read Data signal. |
| UART Read Data | U8 | Read | This signal provides the data byte that was received from the camera. The data on this signal is valid during the second cycle of the two-cycle assertion of the UART Read Enable signal. This signal does not have valid data before the read enable is asserted or after read enable is de-asserted. |
| UART TX Ready | Boolean | Read | Indicates that the UART is ready to accept a new byte to transmit to the camera. |
| UART Write Data | U8 | Write | Set this signal to the data value to be written to the camera over the serial interface. |
| UART Write Enable | Boolean | Write | This signal is used to write a byte to the UART for transmission to the camera. When you have a byte to send, write the data to UART Write Data then set this signal to TRUE for exactly one clock cycle. This signal is ignored unless UART TX Ready is TRUE. |
| UART Break Indicator | Boolean | Read | This signal indicates that the received byte being output on UART Read Data was received as part of a break condition. A break condition occurs when the RX serial input signal is held low by the camera for longer than the time required to send a full byte. In this case, the data byte received has the value 0 and the UART Break Indicator will be TRUE when the byte is read. |
| UART Framing Error | Boolean | Read | This signal indicates that the received byte being output on UART Read Data did not have a valid stop bit. This means that a transmission error occurred and that the received data may not be reliable. |
| UART RX Overrun Error | Boolean | Read | When this signal rises, it means that the receive buffer has filled and one or more bytes of received data have been lost. This occurs when data is not read out from the UART quickly enough. |
| Power Over Camera Link (PoCL) |  |  |  |
| PoCL Active | Boolean | Read | This signal indicates whether power is being supplied to a camera per the Power over Camera Link (PoCL) specification. The NI PCIe-1473R implements the SafePower protocol to determine if a PoCL-capable camera and cable are connected. Note: It takes about three seconds for the frame grabber to safely detect that it is safe to supply power to the camera. |
| PoCL Disable | Boolean | Write | When TRUE, this signal disables the PoCL circuit. Otherwise the PoCL circuit is enabled. Since the SafePower protocol is inherently safe, even with non-PoCL cameras and cables, it is recommended to leave this signal with its default value of FALSE. |
| PoCL Debug Port | U8 | Read | This signal provides a status code with which to debug the PoCL circuitry in case of unexpected operation. Only the highest priority code is output. The codes are as follows (listed in order of priority, highest to lowest): 3 = The PoCL power fuse is blown due to an over-current condition. The board must be returned to National Instruments for repair. 4 = PoCL is disabled because PoCL Disable is driven to TRUE. 5 = A PoCL fault (e.g., over current) has been detected. The PoCL circuit may not power a camera until after the FPGA is restarted. 6 = A non-PoCL cable or non-PoCL camera is detected. 15 = The SafePower state machine is operating normally. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/camera_control_pal.html language=enus -->
## TOPIC 00002: Camera Control

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/camera_control_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/camera_control_pal.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Camera Control

Owning Palette:

NI-IMAQ

Installed With:

Use Camera Control VIs to get and set camera-specific attributes and to control camera modes.

| Palette Object | Description |
| --- | --- |
| IMAQ Get Camera Attribute | Gets the value of camera attributes. |
| IMAQ Set Camera Attribute | Sets the value of camera attributes. |
| IMAQ Serial Read | Reads in data from the serial port on image acquisition devices that support serial communication. |
| IMAQ Serial Read Bytes | Reads in an expected number of bytes from the serial port on image acquisition devices that support serial communication. |
| IMAQ Serial Write | Writes data to the serial port. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/deprecated_vis.html language=enus -->
## TOPIC 00003: Deprecated VIs

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/deprecated_vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/deprecated_vis.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Deprecated VIs

Deprecated VIs are VIs from a previous version of NI-IMAQ that have been replaced by newer VIs. Though the current version of NI-IMAQ still supports these VIs, use the newer VIs whenever possible.

The following VIs are deprecated.

| IMAQ Configure Trigger |
| --- |
| IMAQ Configure Trigger2 |
| IMAQ Copy |
| IMAQ Generate Pulse |
| IMAQ Generate Pulse2 |
| IMAQ Occurrence Config |
| IMAQ Trigger Drive |
| IMAQ Trigger Read |
| IMAQ Trigger Route |
| IMAQ Wait Signal |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/error_codes.html language=enus -->
## TOPIC 00004: Error Codes

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/error_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/error_codes.html
- document_id: `ni-imaq-vi-ref`
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
| -1074397046 | IMG_ERR_BOARD_NOT_INITIALIZED | The image acquisition device is not yet initialized. |
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
| -1074396822 | IMG_ERR_POCL_FAULT | The Power Over CameraLink circuitry has encountered an unexpected error. |
| -1074396821 | IMG_ERR_POCL_VIDEO_LOCK | The Power Over CameraLink circuitry is unable to provide power and the device cannot detect a recognizable video source. |
| -1074396820 | IMG_ERR_POCL_BAD_FUSE | The Power Over CameraLink circuitry cannot provide power due to a blown fuse. |
| -1074396819 | IMG_ERR_POCL_NO_AUX_POWER | The Power Over CameraLink circuitry cannot provide power due to a missing auxiliary power connection |
| -1074396818 | IMG_ERR_PULSE_UPDATE_NOT_SUPPORTED | This image acquisition device does not support updating pulses. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/express_vision_acquisition.html language=enus -->
## TOPIC 00005: Vision Acquisition Express VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/express_vision_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/express_vision_acquisition.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vision Acquisition Express VI

Acquires images from cameras using NI-IMAQ or NI-IMAQdx. Refer to the *NI Vision Acquisition Express VI Help* for more information. The *NI Vision Acquisition Express VI Help* installs to the <LabVIEW>\help directory, where <LabVIEW> is the location to which you installed LabVIEW.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_avi_close-vision.html language=enus -->
## TOPIC 00006: IMAQ AVI Close

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_avi_close-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_avi_close-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ AVI Close

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_avi_create-vision.html language=enus -->
## TOPIC 00007: IMAQ AVI Create

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_avi_create-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_avi_create-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ AVI Create

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_avi_write_frame-vision.html language=enus -->
## TOPIC 00008: IMAQ AVI Write Frame

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_avi_write_frame-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_avi_write_frame-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ AVI Write Frame

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_close.html language=enus -->
## TOPIC 00009: IMAQ Close VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_close.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Close VI

Owning Palette:

NI-IMAQ

Installed With:

Stops the acquisition if one is in progress, releases resources associated with the
 acquisition, and closes the specified IMAQ session.

[IMAGE alt='IMAQ Close' src='imaq_close.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_colorimagetoarray-vision.html language=enus -->
## TOPIC 00010: IMAQ ColorImageToArray

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_colorimagetoarray-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_colorimagetoarray-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ ColorImageToArray

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_configure_buffer.html language=enus -->
## TOPIC 00011: IMAQ Configure Buffer VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_configure_buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_configure_buffer.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Configure Buffer VI

Owning Palette:

Low-Level Acquisition

Installed With:

Configures individual buffers in the buffer list.

You must call IMAQ Configure Buffer for each buffer in the buffer list. Call [IMAQ Configure List](imaq_configure_list.html) before calling IMAQ Configure Buffer.

|  | Note All images in a buffer list must have the same border size and unique names. |
| --- | --- |

[IMAGE alt='IMAQ Configure Buffer' src='imaq_configure_buffer.gif']

|  | Channel specifies the device channel to acquire from. This parameter is valid only for NI PCI/PXI-1409 and NI PCI-1410 devices. |
| --- | --- |
|  | Skipcount is the number of images to skip before the acquisition into the buffer. This parameter is not valid for line scan cameras. |
|  | IMAQ Session In identifies the device. |
|  | Image In is a reference to an image. |
|  | Buffer Number is the index of the buffer in the buffer list you want to acquire. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_configure_list.html language=enus -->
## TOPIC 00012: IMAQ Configure List VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_configure_list.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_configure_list.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Configure List VI

Owning Palette:

Low-Level Acquisition

Installed With:

Configures a buffer list to be used in an acquisition.

The buffers must be configured individually with [IMAQ Configure Buffer](imaq_configure_buffer.html) after calling IMAQ Configure List.

[IMAGE alt='IMAQ Configure List' src='imaq_configure_list.gif']

|  | Region of interest specifies a rectangular portion of the image. Region of Interest is defined by an array of four elements [Left, Top, Right, Bottom]. You must set the width [Right-Left] to a multiple of eight. If Region of Interest is not connected or empty, the entire acquisition window is captured. |
| --- | --- |
|  | IMAQ Session In identifies the device. |
|  | Continuous? specifies if the acquisition is continuous or one-shot. |
|  | Number of buffers is the number of buffers in the buffer list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Memory Location specifies if the acquired images are stored on the host or on the image acquisition device. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_configure_trigger3.html language=enus -->
## TOPIC 00013: IMAQ Configure Trigger3 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_configure_trigger3.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_configure_trigger3.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Configure Trigger3 VI

Owning Palette:

Signal I/O

Installed With:

Configures the trigger conditions for an acquisition. Use this VI before any acquisition
 VI to setup a triggered image acquisition.

[IMAGE alt='IMAQ Configure Trigger3' src='imaq_configure_trigger3.gif']

|  | Frame timeout (ms) specifies the amount of time in milliseconds that NI-IMAQ waits for the trigger to occur and an image to be captured. |
| --- | --- |
|  | Polarity specifies the polarity of the trigger signal. The following values are valid. Rising Edge (0) Sets the polarity to rising edge. Falling Edge (1) Sets the polarity to falling edge. |
| Rising Edge (0) | Sets the polarity to rising edge. |
| Falling Edge (1) | Sets the polarity to falling edge. |
|  | IMAQ Session In identifies the device. |
|  | Type specifies the type of the trigger signal. The following values are valid. Note Scaled Encoder is valid only when Trigger each line is selected for the Trigger action on the front panel. Use the Divide Factor property to configure the amount of scaling to apply to the Scaled Encoder signal. Refer to Scaled Encoder Signal for an overview of the Scaled Encoder signal. Software Trigger is valid only for the NI 17xx smart cameras. Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO In (2) Use an isolated input for the trigger. Scaled Encoder (5) Use scaled encoder counts for the trigger. Software Trigger (6) Use a software trigger for the trigger. |
|  | Note Scaled Encoder is valid only when Trigger each line is selected for the Trigger action on the front panel. Use the Divide Factor property to configure the amount of scaling to apply to the Scaled Encoder signal. Refer to Scaled Encoder Signal for an overview of the Scaled Encoder signal. Software Trigger is valid only for the NI 17xx smart cameras. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO In (2) | Use an isolated input for the trigger. |
| Scaled Encoder (5) | Use scaled encoder counts for the trigger. |
| Software Trigger (6) | Use a software trigger for the trigger. |
|  | Line Number specifies the number of the trigger. |
|  | Action specifies if an assertion edge of this trigger line should start an acquisition. The following values are valid: Note When using Trigger end of acquisition, the device will continue acquiring a variable number of post trigger buffers before stopping the acquisition. Use the Number of Post Trigger Buffers property to set the number of post trigger buffers. Disabled (0) Triggering is disabled. Trigger start of acquisition (1) When the assertion edge of the trigger is received, the acquisition is started. Trigger start of each buffer list (2) When the assertion edge of a trigger is received, the buffer list is acquired. If the acquisition is continuous, buffer index 0 always waits on a trigger before acquiring. Trigger each buffer (3) Each buffer waits for a trigger before acquiring an image into the buffer. Trigger each line (line scan) (4) Each line is triggered. This is useful when using an encoder to acquire line scan images. Trigger end of acquisition (5) When the assertion edge of the trigger is received, the acquisition is stopped. |
|  | Note When using Trigger end of acquisition, the device will continue acquiring a variable number of post trigger buffers before stopping the acquisition. Use the Number of Post Trigger Buffers property to set the number of post trigger buffers. |
| Disabled (0) | Triggering is disabled. |
| Trigger start of acquisition (1) | When the assertion edge of the trigger is received, the acquisition is started. |
| Trigger start of each buffer list (2) | When the assertion edge of a trigger is received, the buffer list is acquired. If the acquisition is continuous, buffer index 0 always waits on a trigger before acquiring. |
| Trigger each buffer (3) | Each buffer waits for a trigger before acquiring an image into the buffer. |
| Trigger each line (line scan) (4) | Each line is triggered. This is useful when using an encoder to acquire line scan images. |
| Trigger end of acquisition (5) | When the assertion edge of the trigger is received, the acquisition is stopped. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Delay specifies how long the active edge of the Trigger is delayed from the point when the Trigger is asserted. Note Only the NI 17xx smart camera supports non-zero delays. To enable a non-zero delay on the NI 17xx smart camera, set the trigger Action to Trigger each buffer. Value specifies the length of the Delay. Units specifies the Units for the Value parameter. The following values are valid: Scaled Encoder Counts (4) The delay is measured in scaled encoder counts. Milliseconds (5) The delay is measured in milliseconds. |
|  | Note Only the NI 17xx smart camera supports non-zero delays. To enable a non-zero delay on the NI 17xx smart camera, set the trigger Action to Trigger each buffer. |
|  | Value specifies the length of the Delay. |
|  | Units specifies the Units for the Value parameter. The following values are valid: Scaled Encoder Counts (4) The delay is measured in scaled encoder counts. Milliseconds (5) The delay is measured in milliseconds. |
| Scaled Encoder Counts (4) | The delay is measured in scaled encoder counts. |
| Milliseconds (5) | The delay is measured in milliseconds. |
|  | Skip trigger (linescan only) is the number of triggers to skip before acquiring a new line. This feature is useful when using an encoder to trigger lines. For example, you may have an encoder that outputs 1,000 ticks per revolution. If you need only 200 lines per revolution, set Skip trigger to 4. Note This input is valid only when using a line scan camera. |
|  | Note This input is valid only when using a line scan camera. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_copy_acquired_buffer.html language=enus -->
## TOPIC 00014: IMAQ Copy Acquired Buffer VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_copy_acquired_buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_copy_acquired_buffer.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Copy Acquired Buffer VI

Owning Palette:

Low-Level Acquisition

Installed With:

Returns a copy of an acquired image. IMAQ Copy Acquired Buffer allows you to copy an
 image from onboard memory to system memory, or from driver-allocated system memory to
 user-allocated system memory.

[IMAGE alt='IMAQ Copy Acquired Buffer' src='imaq_copy_acquired_buffer.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Image In is a reference to an image. |
|  | Buffer Number is the index of the buffer in the buffer list you want to acquire. |
|  | Overwrite Mode is applicable only when you are copying acquired buffers that have been overwritten. Get Oldest (0) Gets the oldest available buffer. Get Next Iteration (1) Gets the next available buffer, which is determined by the buffer index. The buffer index is the remainder of the buffer number divided by the number of buffers in the buffer list. Fail (2) Causes the copy to return an error when it encounters an overwritten buffer. |
| Get Oldest (0) | Gets the oldest available buffer. |
| Get Next Iteration (1) | Gets the next available buffer, which is determined by the buffer index. The buffer index is the remainder of the buffer number divided by the number of buffers in the buffer list. |
| Fail (2) | Causes the copy to return an error when it encounters an overwritten buffer. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Region of Interest specifies a rectangular portion of the image. Region of Interest is defined by an array of four elements [Left, Top, Right, Bottom]. You must set the width [Right-Left] to a multiple of eight. The [Right] and [Bottom] coordinates are exclusive. If Region of Interest is not connected or empty, the entire acquisition window is captured. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Image Out is a reference to the image. |
|  | Buffer Number Copied is the number of the copied buffer. |
|  | Buffer Index Copied is the buffer index of the copied buffer. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_create-vision.html language=enus -->
## TOPIC 00015: IMAQ Create

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_create-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_create-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Create

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

The following description contains additional information you need to know about the **Image Type** parameter when using IMAQ Create with NI-IMAQ:

**Image Type** has the following values:

| 8 bits | 8-bit unsigned image used for monochrome images. |
| --- | --- |
| 16 bits | 16-bit signed image used for 10-, 12-, and 14-bit acquisitions on the NI PCI/PXI-1409, NI PCI-1410, NI PCI/PXI-1422, NI PCI-1424, NI PCI-1426, NI PCI/PXI-1428, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, and NI PXIe-1435 devices. |
| Float | Not used with NI image acquisition devices. |
| Complex | Not used with NI image acquisition devices. |
| RGB | 32-bit standard color image used for acquisitions on the NI PCI-1405, NI PCI/PXI 1411, NI PCI-1424, NI PCI-1426, NI PCI/PXI-1428, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, and NI PXIe-1435 devices. |
| HSL | 32-bit HSL color image used for acquisitions on the NI PCI/PXI-1411 device. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_dispose-vision.html language=enus -->
## TOPIC 00016: IMAQ Dispose

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_dispose-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_dispose-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Dispose

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_extract_buffer.html language=enus -->
## TOPIC 00017: IMAQ Extract Buffer VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_extract_buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_extract_buffer.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Extract Buffer VI

Owning Palette:

Low-Level Acquisition

Installed With:

Extracts a buffer from a continuous acquisition. IMAQ Extract Buffer allows for the
 examination of the buffer during acquisition. The buffer is extracted from the
 acquisition and protected from being overwritten until IMAQ Extract Buffer is called
 again. When IMAQ Extract Buffer is called, any currently extracted buffer is reinserted
 into the buffer list.

If the buffer remains extracted long enough that the acquisition hardware wraps around
 the buffer list and encounters the extracted buffer again, the acquisition will stall,
 increment the lost frame count, and the extracted buffer will not be overwritten. To view the lost frame count, wire a property node to IMAQ Session Out, left-click the property node and select **Status Information»Lost Frames**.

[IMAGE alt='IMAQ Extract Buffer' src='imaq_extract_buffer.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Buffer to extract is the buffer to extract from the buffer list, as specified by the cumulative buffer number. Input –1 to release the currently extracted buffer without extracting a new buffer. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Actual Width is the width of the extracted image. Actual Width is also the current setting for the ROI width. |
|  | Actual Height is the height of the extracted image. In most cases, Actual Height is equal to the ROI height. When in variable height acquisition mode, this value equals the actual number of lines acquired as determined by the duration of the trigger. Refer to the NI-IMAQ Help for more information about variable height acquisition. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Image Out is a reference to the image. |
|  | Buffer Number is the cumulative buffer number of the buffer in the list that was returned in Image Out. The image number can be different from the image number requested by Buffer to Extract if the Buffer to Extract image is no longer available. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_fit_roi.html language=enus -->
## TOPIC 00018: IMAQ Fit ROI VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_fit_roi.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_fit_roi.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Fit ROI VI

Owning Palette:

Low-Level Acquisition

Installed With:

Evaluates the region of interest (ROI) you specify, and returns valid left, top,
 height, and width values.

[IMAGE alt='IMAQ Fit ROI' src='imaq_fit_roi.gif']

|  | Imaq Session in identifies the device. |
| --- | --- |
|  | Region of Interest in specifies a rectangular portion of the image to be captured. Region of Interest in is defined by an array of four elements [Left, Top, Right, Bottom]. The VI analyzes this ROI to determine if the ROI coordinates are valid. If the coordinates are not valid, the VI modifies the ROI to use valid values. |
|  | Fit Mode is the next smallest or next largest acquirable ROI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Imaq Session out has the same value as IMAQ Session In. |
|  | Region of Interest out is the fitted ROI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_generate_pulse3.html language=enus -->
## TOPIC 00019: IMAQ Generate Pulse3 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_generate_pulse3.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_generate_pulse3.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Generate Pulse3 VI

Owning Palette:

Signal I/O

Installed With:

Generates a pulse on a trigger line. IMAQ Generate Pulse3 can generate a pulse
 immediately or on the assertion edge of a status or trigger signal. Each trigger pulse
 uses a Pulse ID, which is automatically generated each time you call this VI.

[Details](#details)

[IMAGE alt='IMAQ Generate Pulse3' src='imaq_generate_pulse3.gif']

|  | Signal polarity specifies the polarity of the status or trigger signal parameter. The following values are valid: Rising Edge (0) Sets the signal polarity to rising edge. Falling Edge (1) Sets the signal polarity to falling edge. |
| --- | --- |
| Rising Edge (0) | Sets the signal polarity to rising edge. |
| Falling Edge (1) | Sets the signal polarity to falling edge. |
|  | Pulse Mode specifies if the pulse is repeated. The following values are valid: Pulse train (0) Generates a continuous pulse train on the first assertion edge of the pulse stimulus signal. Single pulse (1) Generates a single pulse on the first assertion edge of the pulse stimulus signal. Rearmed pulse (2) Generates a single pulse on all assertion edges of the pulse stimulus signal. Stop (3) Stops the pulse generation. Update (4) Updates the duty cycle on an active pulse. |
| Pulse train (0) | Generates a continuous pulse train on the first assertion edge of the pulse stimulus signal. |
| Single pulse (1) | Generates a single pulse on the first assertion edge of the pulse stimulus signal. |
| Rearmed pulse (2) | Generates a single pulse on all assertion edges of the pulse stimulus signal. |
| Stop (3) | Stops the pulse generation. |
| Update (4) | Updates the duty cycle on an active pulse. |
|  | Pulse Parameters specifies the parameters used to describe a pulse. Pulse Delay is the desired duration of the first phase of the signal in seconds. If the Units specified are seconds, the Pulse Delay should be greater than 0. If the Units specified are Scaled Encoder, the Pulse Delay uses one cycle when 0 is specified. Pulse Width is the desired duration of the second phase of the signal in seconds. If the Units specified are seconds, the Pulse Width should be greater than 0. If the Units specified are Scaled Encoder, the Pulse Width uses one cycle when 0 is specified. Pulse Polarity is the polarity of second phase (period two) of each delayed pulse. Units Specifies the units for the Pulse Delay and Pulse Width parameters. If Scaled Encoder Counts is selected, Pulse Delay and Pulse Width must be integral values. |
|  | Pulse Delay is the desired duration of the first phase of the signal in seconds. If the Units specified are seconds, the Pulse Delay should be greater than 0. If the Units specified are Scaled Encoder, the Pulse Delay uses one cycle when 0 is specified. |
|  | Pulse Width is the desired duration of the second phase of the signal in seconds. If the Units specified are seconds, the Pulse Width should be greater than 0. If the Units specified are Scaled Encoder, the Pulse Width uses one cycle when 0 is specified. |
|  | Pulse Polarity is the polarity of second phase (period two) of each delayed pulse. |
|  | Units Specifies the units for the Pulse Delay and Pulse Width parameters. If Scaled Encoder Counts is selected, Pulse Delay and Pulse Width must be integral values. |
|  | IMAQ Session In identifies the device. |
|  | Pulse ID In identifies the Pulse Id input. This parameter is used only when Mode is set to Stop. |
|  | Trigger Type specifies the type of the trigger signal. The following values are valid: Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO Out (3) Use an isolated output for the trigger. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO Out (3) | Use an isolated output for the trigger. |
|  | Trigger Number specifies the number of the trigger. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Signal Type specifies the type of signal that causes the pulse to be generated. The following values are valid: Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). External (0) Specifies the signal type as the external trigger lines. RTSI (1) Specifies the signal type as the RTSI trigger lines. ISO In (2) Specifies the signal type as the isolated input trigger lines. Status (4) Specifies the signal type as one of the Status Signal signals. |
|  | Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). |
| External (0) | Specifies the signal type as the external trigger lines. |
| RTSI (1) | Specifies the signal type as the RTSI trigger lines. |
| ISO In (2) | Specifies the signal type as the isolated input trigger lines. |
| Status (4) | Specifies the signal type as one of the Status Signal signals. |
|  | Status Signal specifies the signal that causes the pulse to be generated if Signal Type is set to Status. The following values are valid: Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. Acquisition in progress (15) Asserts when the acquisition begins. Acquisition done (8) Asserts when the entire acquisition is finished. Horizontal Synchronization Signal (18) Asserts a horizontal synchronization signal at the beginning of each line by the camera. Vertical Synchronization Signal (19) Asserts a vertical synchronization signal at the beginning of each frame by the camera. This value is not applicable to line scan acquisitions. Frame start (9) Asserts at the beginning of each frame that is captured. Frame done (10) Asserts at the end of each frame that is captured. Immediate (16) Asserts immediately. |
|  | Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. |
| Acquisition in progress (15) | Asserts when the acquisition begins. |
| Acquisition done (8) | Asserts when the entire acquisition is finished. |
| Horizontal Synchronization Signal (18) | Asserts a horizontal synchronization signal at the beginning of each line by the camera. |
| Vertical Synchronization Signal (19) | Asserts a vertical synchronization signal at the beginning of each frame by the camera. This value is not applicable to line scan acquisitions. |
| Frame start (9) | Asserts at the beginning of each frame that is captured. |
| Frame done (10) | Asserts at the end of each frame that is captured. |
| Immediate (16) | Asserts immediately. |
|  | Signal Number specifies the number of the trigger line that causes the pulse to be generated if Signal Type is set to one of the trigger types. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Pulse Id Out identifies the Pulse Id output. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### Details

Only the NI 1409, NI 1410, NI 1422, NI 1424, NI 1426, NI 1427, NI 1428, NI 1429, NI
 1430, NI 1433, NI 1435 and the NI 17xx smart cameras can generate pulses.

- The NI 1409, NI 1410, NI 1422, NI 1424, NI 1426, and NI 1428 can generate a
 maximum of 2 pulses.
- The NI 1427, NI 1429, NI 1433, and NI 1435 can generate a maximum of 3 pulses.
- The NI 1430 can generate a maximum of 6 pulses.
- The NI 17xx smart cameras can generate 2 pulses.

These pulse generators can be automatically configured by NI-IMAQ for generating
 pulses used to control the camera. In these cases, the VI returns the Exhausted
 Resources error when the total number of pulses is greater than the maximum number of
 pulses supported.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_get_buffer.html language=enus -->
## TOPIC 00020: IMAQ Get Buffer VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_get_buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_get_buffer.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Get Buffer VI

Owning Palette:

Low-Level Acquisition

Installed With:

Returns one or all acquired images from a one-shot acquisition. IMAQ Get Buffer waits
 until the requested buffer has been acquired before returning an image.

[IMAGE alt='IMAQ Get Buffer' src='imaq_get_buffer.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Buffer Number (-1:all) is the cumulative number of the acquired buffer to return. If Buffer Number is –1, the VI returns all image buffers using the Images Out output. |
|  | Timeout (ms) specifies the amount of time, in milliseconds, to wait for each buffer to be acquired. The VI returns with a timeout error is the image or images are not acquired within the specified amount of time. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Frame Numbers is reserved for future use. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Images Out is the array of image references. It contains all images in the buffer list if Buffer Number equal –1. |
|  | Image Out is a reference to the image. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_get_camera_attribute.html language=enus -->
## TOPIC 00021: IMAQ Get Camera Attribute VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_get_camera_attribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_get_camera_attribute.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Get Camera Attribute VI

Owning Palette:

Camera Control

Installed With:

Gets the value of camera attributes.

Camera attributes vary according to which camera you are using. Refer to Measurement
 & Automation Explorer (MAX) for information about valid camera attributes for
 your camera and image acquisition device.

[IMAGE alt='IMAQ Get Camera Attribute' src='imaq_get_camera_attribute.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Camera Attribute is the attribute name as documented in MAX. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Attribute Value is the current value of the attribute. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_getimageinfo-vision.html language=enus -->
## TOPIC 00022: IMAQ GetImageInfo

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_getimageinfo-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_getimageinfo-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ GetImageInfo

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_getimagesize-vision.html language=enus -->
## TOPIC 00023: IMAQ GetImageSize

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_getimagesize-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_getimagesize-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ GetImageSize

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_grab_acquire.html language=enus -->
## TOPIC 00024: IMAQ Grab Acquire VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_grab_acquire.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_grab_acquire.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Grab Acquire VI

Owning Palette:

NI-IMAQ

Installed With:

Acquires an image from a grab acquisition. Use the grab function for high-speed image
 acquisition.

IMAQ Grab Acquire returns a copy of the most recently acquired image. Use [IMAQ Grab Setup](imaq_grab_setup.html) to start the acquisition and [IMAQ Stop](imaq_stop.html) to stop the acquisition.

[IMAGE alt='IMAQ Grab Acquire' src='imaq_grab_acquire.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Image In is a reference to an image. |
|  | Immediate? determines if the system returns the image currently being acquired or the last completely acquired image. The default value is FALSE, which causes NI-IMAQ to wait until the current image is completely acquired before returning the image. TRUE returns the last acquired image. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Image Out is a reference to the image. |
|  | Acquired Buffer Number is the number of the buffer acquired in the acquisition. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_grab_setup.html language=enus -->
## TOPIC 00025: IMAQ Grab Setup VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_grab_setup.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_grab_setup.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Grab Setup VI

Owning Palette:

NI-IMAQ

Installed With:

Starts a grab acquisition. This VI performs a continuous acquisition that provides
 access to the most recently acquired image.

Use [IMAQ Grab Acquire](imaq_grab_acquire.html) to return a copy of the image. If necessary,
 this VI performs a system initialization using [IMAQ Init](imaq_init.html).

[IMAGE alt='IMAQ Grab Setup' src='imaq_grab_setup.gif']

|  | Channel specifies the device channel to acquire from. This parameter is valid only for NI PCI/PXI-1409 and NI PCI-1410 devices. |
| --- | --- |
|  | Region of Interest specifies a rectangular portion of the image. Region of Interest is defined by an array of four elements [Left, Top, Right, Bottom]. You must set the width [Right-Left] to a multiple of eight. The [Right] and [Bottom] coordinates are exclusive. If Region of Interest is not connected or empty, the current region of interest is captured. |
|  | IMAQ Session In identifies the device. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Step x is a horizontal sampling step or horizontal reduction factor. If Step x is set to 1, each column of the image is transferred. If Step x is not connected or is set to -1, the current value of the Horizontal Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Step y is a vertical sampling step or vertical reduction factor. If Step y is set to 1, each column of the image is transferred. If Step y is not connected or is set to -1, the current value of the Vertical Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_imagetoarray-vision.html language=enus -->
## TOPIC 00026: IMAQ ImageToArray

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_imagetoarray-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_imagetoarray-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ ImageToArray

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW Help* for parameter information.

The following descriptions contain additional information you need to know about the **Image Pixels (I16) and Image Pixels (Float)** parameters when using the IMAQ ImageToArray VI with NI-IMAQ:

|  | Image Pixels (U8) returns the extracted pixel values into a 2D array. The first index corresponds to the vertical axis and the second index corresponds to the horizontal axis. Use this output only when Image is an unsigned 8-bit image. The boards that have this output include the NI PCI/PXI-1409, NI PCI-1410, NI PCI/PXI-1422, NI PCI-1424, NI PCI-1426, NI PCIe-1427, NI PCI/PXI-1428, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, NI PXIe-1435, and NI 17xx smart cameras. |
| --- | --- |
|  | Image Pixels (I16) output is used with a 16-bit image type, which is used with boards that have a 10-bit output or greater. These include the NI PCI/PXI-1409, NI PCI-1410, NI PCI/PXI-1422, NI PCI-1424, NI PCI-1426, NI PCIe-1427, NI PCI/PXI-1428, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, and NI PXIe-1435 devices. |
|  | Image Pixels (Float) is not used with NI image acquisition devices. |
|  | Optional Rectangle defines a four-element array that contains the left, top, right, and bottom coordinates of the region to extract. The operation applies to the entire image if the input is empty or not connected. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_init.html language=enus -->
## TOPIC 00027: IMAQ Init VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_init.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_init.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Init VI

Owning Palette:

NI-IMAQ

Installed With:

Loads an NI-IMAQ configuration file and configures the image acquisition device.

[IMAGE alt='IMAQ Init' src='imaq_init.gif']

|  | Interface Name is the name of the interface to be loaded. The name must match the configuration file name used in Measurement & Automation Explorer (MAX). Note Interface Name always identifies a single port of an image acquisition device. A port identifies a single independent data stream from a camera. All NI image acquisition devices support at least one port. Devices that support multiple ports can sustain independent and asynchronous acquisitions from the cameras on each port. The port number may be explicitly identified by using the :: operator to append the port number suffix to the interface name. Port numbers are zero-based. For example, img0::1 opens port number 1 of the image acquisition device identified by img0. Interface names that do not have a port number suffix default to port 0. img0::0 and img0 are equivalent in meaning. |
| --- | --- |
|  | Note Interface Name always identifies a single port of an image acquisition device. A port identifies a single independent data stream from a camera. All NI image acquisition devices support at least one port. Devices that support multiple ports can sustain independent and asynchronous acquisitions from the cameras on each port. The port number may be explicitly identified by using the :: operator to append the port number suffix to the interface name. Port numbers are zero-based. For example, img0::1 opens port number 1 of the image acquisition device identified by img0. Interface names that do not have a port number suffix default to port 0. img0::0 and img0 are equivalent in meaning. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out identifies the initialized device. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_occurrence_config2.html language=enus -->
## TOPIC 00028: IMAQ Occurrence Config2 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_occurrence_config2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_occurrence_config2.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Occurrence Config2 VI

Owning Palette:

Signal I/O

Installed With:

Creates occurrences that are set by image acquisition signals such as the assertion of
 a status or trigger signal. Occurrences produced by this VI are used as inputs to the
 Wait on Occurrence LabVIEW primitive. Anything dependent on the execution of the Wait on
 Occurrence primitive will wait until the occurrence is set.

[IMAGE alt='IMAQ Occurrence Config2' src='imaq_occurrence_config2.gif']

|  | Signal polarity specifies the polarity of the status or trigger signal parameter. The following values are valid: Rising Edge (0) Sets the signal polarity to rising edge. Falling Edge (1) Sets the signal polarity to falling edge. |
| --- | --- |
| Rising Edge (0) | Sets the signal polarity to rising edge. |
| Falling Edge (1) | Sets the signal polarity to falling edge. |
|  | IMAQ Session In identifies the device. |
|  | Signal Type specifies the type of signal that causes the occurrence to be set. The following values are valid: Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). External (0) Specifies the signal type as the external trigger lines. RTSI (1) Specifies the signal type as the RTSI trigger lines. ISO In (2) Specifies the signal type as the isolated input trigger lines. ISO Out (3) Specifies the signal type as the isolated output trigger lines. Status (4) Specifies the signal type as one of the Status Signal signals. |
|  | Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). |
| External (0) | Specifies the signal type as the external trigger lines. |
| RTSI (1) | Specifies the signal type as the RTSI trigger lines. |
| ISO In (2) | Specifies the signal type as the isolated input trigger lines. |
| ISO Out (3) | Specifies the signal type as the isolated output trigger lines. |
| Status (4) | Specifies the signal type as one of the Status Signal signals. |
|  | Status Signal Signal specifies the signal that causes the occurrence to be set if Signal Type is set to Status. The following values are valid: Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. Acquisition in progress (15) Asserts when the acquisition begins. Acquisition done (8) Asserts when the entire acquisition is finished. Frame start (9) Asserts at the beginning of each frame that is captured. Frame done (10) Asserts at the end of each frame that is captured. Buffer Complete (11) Asserts when a buffer has been transferred to memory. |
|  | Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. |
| Acquisition in progress (15) | Asserts when the acquisition begins. |
| Acquisition done (8) | Asserts when the entire acquisition is finished. |
| Frame start (9) | Asserts at the beginning of each frame that is captured. |
| Frame done (10) | Asserts at the end of each frame that is captured. |
| Buffer Complete (11) | Asserts when a buffer has been transferred to memory. |
|  | Signal Number specifies the number of the trigger line that causes the occurrence to be set if Signal Type is set to one of the trigger types. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | create/clear instructs the VI to create an occurrence or to clear all occurrences that have been created for the image acquisition device specified in IMAQ Session In. The following values are valid: create an occurrence (0) Creates an occurrence. clear all occurrences (1) Clears all occurrences. |
| create an occurrence (0) | Creates an occurrence. |
| clear all occurrences (1) | Clears all occurrences. |
|  | Rearm? (FALSE : No Rearm) indicates whether the occurrence should be generated once, or each time the signal occurs. When you set this parameter to TRUE, call this VI again with the create/clear parameter set to clear all occurrences to stop the occurrence. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | occurrence is the occurrence value created. Wire this output to a Wait on Occurrence LabVIEW primitive. Wire the output of the primitive to the part of your diagram you wish to execute when an event happens and the occurrence is set. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_remote_compression-vision.html language=enus -->
## TOPIC 00029: IMAQ Remote Compression

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_remote_compression-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_remote_compression-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Remote Compression

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_reset_encoder_position.html language=enus -->
## TOPIC 00030: IMAQ Reset Encoder Position VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_reset_encoder_position.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_reset_encoder_position.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Reset Encoder Position VI

Owning Palette:

Signal I/O

Installed With:

Resets the absolute encoder position counter to 0.

Reads the position counter value by querying the [Position (U32)](prop_position_u32.html) or [Position (U64)](prop_position_u64.html)
 properties.

[IMAGE alt='IMAQ Reset Encoder Position' src='imaq_reset_encoder_position.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_rt_video_out-vision.html language=enus -->
## TOPIC 00031: IMAQ RT Video Out

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_rt_video_out-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_rt_video_out-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ RT Video Out

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_sequence.html language=enus -->
## TOPIC 00032: IMAQ Sequence VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_sequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_sequence.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Sequence VI

Owning Palette:

NI-IMAQ

Installed With:

Starts, acquires, and releases a sequence acquisition. Use this VI to capture multiple
 images with fixed or variable delays between images.

If necessary, this VI initializes the system using [IMAQ Init](imaq_init.html).

[IMAGE alt='IMAQ Sequence' src='imaq_sequence.gif']

|  | Channel specifies the device channel to acquire from. This parameter is valid only for NI PCI/PXI-1409 and NI PCI-1410 devices. |
| --- | --- |
|  | Region of interest specifies a rectangular portion of the image. Region of Interest is defined by an array of four elements [Left, Top, Right, Bottom]. You must set the width [Right-Left] to a multiple of eight. If Region of Interest is not connected or empty, the entire acquisition window is captured. |
|  | IMAQ Session In identifies the device. |
|  | Images In is an array of image references that receives the captured pixel data. Each image in the array must have the same border size, and a unique name. |
|  | Skip table is an array containing the number of frames to skip before acquiring each buffer. Each element in the array specifies the number of frames to skip before acquiring the corresponding buffer in the buffer list. Note This parameter is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, or NI 1435. Note This parameter is optional. If you choose to specify an array for Skip table, the array must contain the same number of elements as the Images In array. |
|  | Note This parameter is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, or NI 1435. |
|  | Note This parameter is optional. If you choose to specify an array for Skip table, the array must contain the same number of elements as the Images In array. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Step x is a horizontal sampling step or horizontal reduction factor. If Step x is set to 1, each column of the image is transferred. If Step x is not connected or is set to -1, the current value of the Horizontal Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Step y is a vertical sampling step or vertical reduction factor. If Step y is set to 1, each column of the image is transferred. If Step y is not connected or is set to -1, the current value of the Vertical Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Images Out is the array of captured images. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_serial_read.html language=enus -->
## TOPIC 00033: IMAQ Serial Read VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_serial_read.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_serial_read.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Serial Read VI

Owning Palette:

Camera Control

Installed With:

Reads in data from the serial port on image acquisition devices that support serial
 communication.

This VI fills the buffer with characters received from the serial port until either a
 termination character has been received or the timeout period has elapsed. The
 termination character is defined in the camera file associated with the session.

[IMAGE alt='IMAQ Serial Read' src='imaq_serial_read.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Timeout is the time, in milliseconds, to wait for the read to finish. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | String Read is the string read from the serial port. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_serial_read_bytes.html language=enus -->
## TOPIC 00034: IMAQ Serial Read Bytes VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_serial_read_bytes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_serial_read_bytes.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Serial Read Bytes VI

Owning Palette:

Camera Control

Installed With:

Reads in an expected number of bytes from the serial port on image acquisition devices
 that support serial communication.

This VI fills the buffer with characters received from the serial port until either
 the buffer is full or the timeout period has elapsed. When you use this VI, the serial
 termination string attribute is ignored.

[IMAGE alt='IMAQ Serial Read Bytes' src='imaq_serial_read_bytes.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Bytes to Read is the number of bytes to read from the serial port. |
|  | Timeout is the time, in milliseconds, to wait for the read to finish. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Byte Array returns an array of bytes read from the serial port. |
|  | Bytes Read is the number of bytes stored in Byte Array. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_serial_write.html language=enus -->
## TOPIC 00035: IMAQ Serial Write VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_serial_write.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_serial_write.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Serial Write VI

Owning Palette:

Camera Control

Installed With:

Writes data to the serial port.

Serial communication parameters, such as baud rate, are set in the camera file
 associated with the session. You can adjust these communication parameters directly in
 the camera file.

[IMAGE alt='IMAQ Serial Write' src='imaq_serial_write.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | String to write is the string write to the serial port. Complete the following steps to convert the string to hexadecimal format: Create a string constant from the String to write input. Right-click the string constant, and select Hex Display. Enter the hexadecimal value you want to pass. |
|  | Timeout is the time, in milliseconds, to wait for the read to finish. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_set_camera_attribute.html language=enus -->
## TOPIC 00036: IMAQ Set Camera Attribute VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_set_camera_attribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_set_camera_attribute.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Set Camera Attribute VI

Owning Palette:

Camera Control

Installed With:

Sets the value of camera attributes.

Camera attributes vary according to which camera you are using. Refer to Measurement
 & Automation Explorer (MAX) for information about valid camera attributes for
 your camera and image acquisition device.

[IMAGE alt='IMAQ Set Camera Attribute' src='imaq_set_camera_attribute.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Camera Attribute is the attribute name as documented in MAX. |
|  | Attribute Value is the new value of the attribute. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_set_user_lut.html language=enus -->
## TOPIC 00037: IMAQ Set User LUT VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_set_user_lut.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_set_user_lut.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Set User LUT VI

Owning Palette:

Low-Level Acquisition

Installed With:

Downloads a custom lookup table (LUT) to an image acquisition device. This VI can
 download 8-bit or 16-bit LUTs for analog or digital devices. If the image acquisition
 device has multiple LUTs, you can input all of the LUTs into this VI. Call this VI
 before starting the acquisition.

|  | Note This VI is not applicable for the NI PCI-1405, NI PCI-1426, NI PCIe-1427, NI PCIe-1429, NI PCIe-1430, NI PCIe-1433, NI PXIe-1435, or NI 17xx smart cameras. |
| --- | --- |

[IMAGE alt='IMAQ Set User LUT' src='imaq_set_user_lut.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | Tap 0 LUT (Red) is used for analog monochrome devices, the red channel for RGB digital cameras, or tap 0 on digital devices. If the bit depth is 8-bit, wire an array of 8-bit unsigned integers containing 256 elements. If the bit depth is greater than 8-bits, wire an array of 16-bit unsigned integers containing 2n elements where n is the bit depth of the camera (1,024 for 10-bit, 4,096 for 12-bit, and so on). |
|  | Tap 1 LUT (Green) is used for the green channel for RGB digital cameras or tap 1 on digital devices. If the bit depth is 8-bit, wire an array of 8-bit unsigned integers containing 256 elements. If the bit depth is greater than 8-bits, wire an array of 16-bit unsigned integers containing 2n elements where n is the bit depth of the camera (1,024 for 10-bit, 4,096 for 12-bit, and so on). |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Tap 2 LUT (Blue) is used for the blue channel for RGB digital cameras or tap 2 on digital devices. If the bit depth is 8-bit, wire an array of 8-bit unsigned integers containing 256 elements. If the bit depth is greater than 8-bits, wire an array of 16-bit unsigned integers containing 2n elements where n is the bit depth of the camera (1,024 for 10-bit, 4,096 for 12-bit, and so on). |
|  | Tap 3 LUT is used for tap 3 on digital devices. If the bit depth is 8-bit, wire an array of 8-bit unsigned integers containing 256 elements. If the bit depth is greater than 8-bits, wire an array of 16-bit unsigned integers containing 2n elements where n is the bit depth of the camera (1,024 for 10-bit, 4,096 for 12-bit, and so on). |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_setimagesize-vision.html language=enus -->
## TOPIC 00038: IMAQ SetImageSize

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_setimagesize-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_setimagesize-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ SetImageSize

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_snap.html language=enus -->
## TOPIC 00039: IMAQ Snap VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_snap.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_snap.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Snap VI

Owning Palette:

NI-IMAQ

Installed With:

Acquires a single image into **Image out**. A snap is
 appropriate for low-speed or single-capture applications where ease of programming is
 essential.

If necessary, this VI performs a system initialization using [IMAQ Init](imaq_init.html) before the acquisition. When you invoke a snap, the VI
 initializes the device and acquires the next incoming video frame to a buffer.

[IMAGE alt='IMAQ Snap' src='imaq_snap.gif']

|  | Channel specifies the device channel to acquire from. This parameter is valid only for NI PCI/PXI-1409 and NI PCI-1410 devices. |
| --- | --- |
|  | Region of Interest specifies a rectangular portion of the image. Region of Interest is defined by an array of four elements [Left, Top, Right, Bottom]. You must set the width [Right-Left] to a multiple of eight. The [Right] and [Bottom] coordinates are exclusive. If Region of Interest is not connected or empty, the current region of interest is captured. |
|  | IMAQ Session In identifies the device. |
|  | Image In is a reference to an image that receives the captured pixel data. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Step x is a horizontal sampling step or horizontal reduction factor. If Step x is set to 1, each column of the image is transferred. If Step x is not connected or is set to -1, the current value of the Horizontal Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Horizontal scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Step y is a vertical sampling step or vertical reduction factor. If Step y is set to 1, each column of the image is transferred. If Step y is not connected or is set to -1, the current value of the Vertical Scaling property is used. Step x accepts only values of -1, 1, 2, 4, or 8. Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | Note This parameter is deprecated and not available on all NI image acquisition devices. Vertical scaling is not supported on the NI 1427, NI 1429, NI 1430, NI 1433, NI 1435, or NI 17xx smart cameras. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Image Out is a reference to the image. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_start.html language=enus -->
## TOPIC 00040: IMAQ Start VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_start.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_start.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Start VI

Owning Palette:

Low-Level Acquisition

Installed With:

Starts an asynchronous image acquisition.

IMAQ Start returns immediately after the acquisition has started. Before calling this
 VI, you must configure the acquisition with [IMAQ Configure List](imaq_configure_list.html)
 and [IMAQ Configure Buffer](imaq_configure_buffer.html).

[IMAGE alt='IMAQ Start' src='imaq_start.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_status.html language=enus -->
## TOPIC 00041: IMAQ Status VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_status.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Status VI

Owning Palette:

Low-Level Acquisition

Installed With:

Returns status information about the acquisition, such as the state of the acquisition
 and the last valid buffer acquired.

[IMAGE alt='IMAQ Status' src='imaq_status.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Acquiring? specifies if the image acquisition device is acquiring images. Acquiring? is TRUE if the device is acquiring. |
|  | Last Valid Buffer Index is the buffer list index of the last acquired image. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Last Valid Buffer Number is the cumulative number of the last acquired image. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_stop.html language=enus -->
## TOPIC 00042: IMAQ Stop VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_stop.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Stop VI

Owning Palette:

Low-Level Acquisition

Installed With:

Stops the currently executing acquisition on the image acquisition device specified by
 **IMAQ Session**.

IMAQ Stop does not free the resources associated with the acquisition. Call [IMAQ Close](imaq_close.html) to free resources.

[IMAGE alt='IMAQ Stop' src='imaq_stop.gif']

|  | IMAQ Session In identifies the device. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_trigger_drive2.html language=enus -->
## TOPIC 00043: IMAQ Trigger Drive2 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_trigger_drive2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_trigger_drive2.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Trigger Drive2 VI

Owning Palette:

Signal I/O

Installed With:

Drives a trigger line with a specified signal.

[IMAGE alt='IMAQ Trigger Drive2' src='imaq_trigger_drive2.gif']

|  | Trigger polarity specifies the polarity of the trigger signal. The following values are valid: High True (0) Drives the line high when the signal is true. Low True (1) Drives the line low when the signal is true. |
| --- | --- |
| High True (0) | Drives the line high when the signal is true. |
| Low True (1) | Drives the line low when the signal is true. |
|  | IMAQ Session In identifies the device. |
|  | Trigger Type specifies the type of the trigger signal. The following values are valid: Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO Out (3) Use an isolated output for the trigger. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO Out (3) | Use an isolated output for the trigger. |
|  | Trigger Number specifies the number of the trigger. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Trigger drive specifies the signal that drives the trigger line. The following values are valid: Note Frame Start and Frame Done are not supported for line scan applications Disabled (0) The trigger line is disabled. Acquisition in Progress (1) Asserts when an acquisition is in progress. Acquisition Done (2) Asserts when the entire acquisition is completed. Pixel Clock (3) Specifies the pixel clock as the signal that drives the trigger line. Unasserted (4) Forces the trigger to its unasserted state as defined by Trigger Polarity. Asserted (5) Forces the trigger to its asserted state as defined by Trigger Polarity. Horizontal Synchronization Signal (6) Asserts a horizontal synchronization signal at the beginning of each line by the camera. Vertical Synchronization Signal (7) Asserts a vertical synchronization signal at the beginning of each frame by the camera. This value is not applicable to line scan acquisitions. Frame Start (8) Asserts when a frame is being captured. Frame Done (9) Asserts at the end of each frame that is captured. Scaled Encoder (10) Pulses for cumulative forward movement of encoder Phase A and Phase B signals after applying a scaling factor. |
|  | Note Frame Start and Frame Done are not supported for line scan applications |
| Disabled (0) | The trigger line is disabled. |
| Acquisition in Progress (1) | Asserts when an acquisition is in progress. |
| Acquisition Done (2) | Asserts when the entire acquisition is completed. |
| Pixel Clock (3) | Specifies the pixel clock as the signal that drives the trigger line. |
| Unasserted (4) | Forces the trigger to its unasserted state as defined by Trigger Polarity. |
| Asserted (5) | Forces the trigger to its asserted state as defined by Trigger Polarity. |
| Horizontal Synchronization Signal (6) | Asserts a horizontal synchronization signal at the beginning of each line by the camera. |
| Vertical Synchronization Signal (7) | Asserts a vertical synchronization signal at the beginning of each frame by the camera. This value is not applicable to line scan acquisitions. |
| Frame Start (8) | Asserts when a frame is being captured. |
| Frame Done (9) | Asserts at the end of each frame that is captured. |
| Scaled Encoder (10) | Pulses for cumulative forward movement of encoder Phase A and Phase B signals after applying a scaling factor. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_trigger_read2.html language=enus -->
## TOPIC 00044: IMAQ Trigger Read2 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_trigger_read2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_trigger_read2.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Trigger Read2 VI

Owning Palette:

Signal I/O

Installed With:

Reads the current value of a trigger line.

[IMAGE alt='IMAQ Trigger Read2' src='imaq_trigger_read2.gif']

|  | Trigger Polarity specifies the polarity of the trigger signal. The following values are valid: High True (0) Drives the line high when the signal is true. Low True (1) Drives the line low when the signal is true. |
| --- | --- |
| High True (0) | Drives the line high when the signal is true. |
| Low True (1) | Drives the line low when the signal is true. |
|  | IMAQ Session In identifies the device. |
|  | Trigger Type specifies the type of the trigger signal. The following values are valid: Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO In (2) Use an isolated input for the trigger. ISO Out (3) Use an isolated output for the trigger. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO In (2) | Use an isolated input for the trigger. |
| ISO Out (3) | Use an isolated output for the trigger. |
|  | Trigger Number specifies the number of the trigger. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | Trigger status specifies the current value on the trigger line. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_trigger_route2.html language=enus -->
## TOPIC 00045: IMAQ Trigger Route2 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_trigger_route2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_trigger_route2.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Trigger Route2 VI

Owning Palette:

Signal I/O

Installed With:

Drives the destination trigger line with the signal on the source trigger line.

[IMAGE alt='IMAQ Trigger Route2' src='imaq_trigger_route2.gif']

|  | Dst Trigger Number specifies the number of the destination trigger line. |
| --- | --- |
|  | Dst Trigger Type specifies the type of the destination trigger line. The following values are valid: Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Dst Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO Out (3) Use an isolated output for the trigger. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Dst Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO Out (3) | Use an isolated output for the trigger. |
|  | IMAQ Session In identifies the device. |
|  | Src Trigger Type specifies the type of the source trigger line. Use None to disable the trigger route. The following values are valid: Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Src Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). None (42) Disables triggering. External (0) Use an external trigger for the trigger. RTSI (1) Use an RTSI line for the trigger. ISO In (2) Use an isolated input for the trigger. |
|  | Note To use the ISO_IN or RS422_IN signals on the NI PCI-1426, select External as the Src Trigger Type for your function and choose ISO IN or RS-422 as the Signal Level for the trigger line in Measurement & Automation Explorer (MAX). |
| None (42) | Disables triggering. |
| External (0) | Use an external trigger for the trigger. |
| RTSI (1) | Use an RTSI line for the trigger. |
| ISO In (2) | Use an isolated input for the trigger. |
|  | Src Trigger Number specifies the number of the source trigger line. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_video_out_display_mode-vision.html language=enus -->
## TOPIC 00046: IMAQ Video Out Display Mode

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_video_out_display_mode-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_video_out_display_mode-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Video Out Display Mode

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_wait_signal2.html language=enus -->
## TOPIC 00047: IMAQ Wait Signal2 VI

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_wait_signal2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_wait_signal2.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ Wait Signal2 VI

Owning Palette:

Signal I/O

Installed With:

Waits for either a status or trigger signal to be asserted. IMAQ Wait Signal2 does not
 return until the specified signal is asserted or a timeout occurs.

[IMAGE alt='IMAQ Wait Signal2' src='imaq_wait_signal2.gif']

|  | Timeout (ms) specifies the amount of time to wait for the assertion edge of Signal in milliseconds. The VI returns an error is the assertion edge does not occur within the specified time. |
| --- | --- |
|  | Signal polarity specifies the polarity of the status or trigger signal parameter. The following values are valid: Rising Edge (0) Sets the signal polarity to rising edge. Falling Edge (1) Sets the signal polarity to falling edge. |
| Rising Edge (0) | Sets the signal polarity to rising edge. |
| Falling Edge (1) | Sets the signal polarity to falling edge. |
|  | IMAQ Session In identifies the device. |
|  | Signal Type specifies the type of signal that causes the occurrence to be set. The following values are valid: Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). External (0) Specifies the signal type as the external trigger lines. RTSI (1) Specifies the signal type as the RTSI trigger lines. ISO In (2) Specifies the signal type as the isolated input trigger lines. ISO Out (3) Specifies the signal type as the isolated output trigger lines. Status (4) Specifies the signal type as one of the Status Signal signals. |
|  | Note To use the ISO_IN or RS422_In signals on the NI PCI-1426, select External as the Trigger Type for your function and select either ISO In or RS-422 In as the Signal Level in Measurement & Automation Explorer (MAX). |
| External (0) | Specifies the signal type as the external trigger lines. |
| RTSI (1) | Specifies the signal type as the RTSI trigger lines. |
| ISO In (2) | Specifies the signal type as the isolated input trigger lines. |
| ISO Out (3) | Specifies the signal type as the isolated output trigger lines. |
| Status (4) | Specifies the signal type as one of the Status Signal signals. |
|  | Status Signal Signal specifies the signal that causes the occurrence to be set if Signal Type is set to Status. The following values are valid: Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. Acquisition in progress (15) Asserts when the acquisition begins. Acquisition done (8) Asserts when the entire acquisition is finished. Frame start (9) Asserts at the beginning of each frame that is captured. Frame done (10) Asserts at the end of each frame that is captured. Buffer Complete (11) Asserts when a buffer has been transferred to memory. |
|  | Note The Frame start and Frame done signals are not valid for line scan acquisitions unless each buffer is triggered. |
| Acquisition in progress (15) | Asserts when the acquisition begins. |
| Acquisition done (8) | Asserts when the entire acquisition is finished. |
| Frame start (9) | Asserts at the beginning of each frame that is captured. |
| Frame done (10) | Asserts at the end of each frame that is captured. |
| Buffer Complete (11) | Asserts when a buffer has been transferred to memory. |
|  | Signal Number specifies the number of the trigger line that causes the occurrence to be set if Signal Type is set to one of the trigger types. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | IMAQ Session Out has the same value as IMAQ Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/imaq_writefile-vision.html language=enus -->
## TOPIC 00048: IMAQ WriteFile

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/imaq_writefile-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/imaq_writefile-vision.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQ WriteFile

This VI is part of a subset of NI Vision VIs included with NI-IMAQ. Refer to the *NI Vision for LabVIEW VI Reference Help* for parameter information.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/low-level_acquisition_pal.html language=enus -->
## TOPIC 00049: Low-Level Acquisition

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/low-level_acquisition_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/low-level_acquisition_pal.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Low-Level Acquisition

Owning Palette:

NI-IMAQ

Installed With:

Use Low-Level VIs for more direct control of the image acquisition hardware.

| Palette Object | Description |
| --- | --- |
| IMAQ Configure List | Configures a buffer list to be used in an acquisition. |
| IMAQ Configure Buffer | Configures individual buffers in the buffer list. |
| IMAQ Start | Starts an asynchronous image acquisition. |
| IMAQ Fit ROI | Evaluates the region of interest (ROI) you specify, and returns valid left, top, height, and width values. |
| IMAQ Get Buffer | Returns one or all acquired images from a one-shot acquisition. IMAQ Get Buffer waits until the requested buffer has been acquired before returning an image. |
| IMAQ Extract Buffer | Extracts a buffer from a continuous acquisition. IMAQ Extract Buffer allows for the examination of the buffer during acquisition. The buffer is extracted from the acquisition and protected from being overwritten until IMAQ Extract Buffer is called again. When IMAQ Extract Buffer is called, any currently extracted buffer is reinserted into the buffer list. |
| IMAQ Copy Acquired Buffer | Returns a copy of an acquired image. IMAQ Copy Acquired Buffer allows you to copy an image from onboard memory to system memory, or from driver-allocated system memory to user-allocated system memory. |
| IMAQ Stop | Stops the currently executing acquisition on the image acquisition device specified by IMAQ Session. |
| IMAQ Status | Returns status information about the acquisition, such as the state of the acquisition and the last valid buffer acquired. |
| IMAQ Set User LUT | Downloads a custom lookup table (LUT) to an image acquisition device. This VI can download 8-bit or 16-bit LUTs for analog or digital devices. If the image acquisition device has multiple LUTs, you can input all of the LUTs into this VI. Call this VI before starting the acquisition. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/ni-imaq_pal.html language=enus -->
## TOPIC 00050: NI-IMAQ

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/ni-imaq_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/ni-imaq_pal.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI-IMAQ

Installed With:

Use NI-IMAQ VIs to set up image acquisition systems and acquire images. These VIs allow you to acquire images and open and close an interface.

| Palette Object | Description |
| --- | --- |
| IMAQ Init | Loads an NI-IMAQ configuration file and configures the image acquisition device. |
| IMAQ Close | Stops the acquisition if one is in progress, releases resources associated with the acquisition, and closes the specified IMAQ session. |
| IMAQ Snap | Acquires a single image into Image out. A snap is appropriate for low-speed or single-capture applications where ease of programming is essential. |
| IMAQ Grab Setup | Starts a grab acquisition. This VI performs a continuous acquisition that provides access to the most recently acquired image. |
| IMAQ Grab Acquire | Acquires an image from a grab acquisition. Use the grab function for high-speed image acquisition. |
| IMAQ Sequence | Starts, acquires, and releases a sequence acquisition. Use this VI to capture multiple images with fixed or variable delays between images. |

| Subpalette | Description |
| --- | --- |
| Low-Level Acquisition | Use Low-Level VIs for more direct control of the image acquisition hardware. |
| Signal I/O | Use Signal I/O VIs to control the trigger lines, generate pulses, and wait for hardware events. |
| Camera Control | Use Camera Control VIs to get and set camera-specific attributes and to control camera modes. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/ni-imaq_vi_ref_help.html language=enus -->
## TOPIC 00051: NI-IMAQ VI Reference Help

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/ni-imaq_vi_ref_help.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/ni-imaq_vi_ref_help.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### NI-IMAQ™ VI Reference Help

July 2021, 370162V-01

This help file contains reference information for NI-IMAQ virtual instruments (VIs). The NI-IMAQ VI library, a series of VIs for using LabVIEW with National Instruments image acquisition devices, is included with the NI-IMAQ driver software.

The NI-IMAQ VI library also includes several basic NI Vision VIs. NI Vision is an image processing and analysis library that consists of VIs for use with LabVIEW. If you use these included basic VIs, you can later upgrade the programs to use NI Vision without any changes to the image acquisition VIs.

NI-IMAQ VIs give you the basic tools to perform the following functions:

- Load information about devices and cameras from a configuration file.
- Select a video channel.
- Adjust the acquisition parameters.
- Start or stop an acquisition.
- Transfer an image from device memory to an NI Vision image buffer.
- Monitor and control the device trigger lines.

For more information about this help file, refer to the following topics:

[Related Documentation](bp_related_documentation.html)

[Glossary](bp_glossary.html)

[NI Services](bp_technical_support_resources.html)

© 1998–2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/ni_vision_vis.html language=enus -->
## TOPIC 00052: NI Vision VIs

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/ni_vision_vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/ni_vision_vis.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI Vision VIs

Several basic NI Vision functions are included with the NI-IMAQ software. Use these VIs to create and dispose of images and to convert images to arrays. After you convert an image to an array, use standard LabVIEW techniques to process and display the images.

[IMAQ AVI Close](imaq_avi_close-vision.html)

[IMAQ AVI Create](imaq_avi_create-vision.html)

[IMAQ AVI Write Frame](imaq_avi_write_frame-vision.html)

[IMAQ ColorImageToArray](imaq_colorimagetoarray-vision.html)

[IMAQ Create](imaq_create-vision.html)

[IMAQ Dispose](imaq_dispose-vision.html)

[IMAQ GetImageInfo](imaq_getimageinfo-vision.html)

[IMAQ GetImageSize](imaq_getimagesize-vision.html)

[IMAQ ImageToArray](imaq_imagetoarray-vision.html)

[IMAQ Remote Compression](imaq_remote_compression-vision.html)

[IMAQ RT Video Out](imaq_rt_video_out-vision.html)

[IMAQ SetImageSize](imaq_setimagesize-vision.html)

[IMAQ Video Out Display Mode](imaq_video_out_display_mode-vision.html)

[IMAQ WriteFile](imaq_writefile-vision.html)

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_24v_strobe.html language=enus -->
## TOPIC 00053: 24V Strobe

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_24v_strobe.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_24v_strobe.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### 24V Strobe

Enables/disables the 24 V external lighting strobe signal for external lighting controllers. This property is valid only for NI 17xx smart cameras.

#### Values

The following list includes possible values:

- Off —External 24 V strobe output is disabled.
- Rising —External 24 V strobe output asserts a rising edge.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_5v_strobe.html language=enus -->
## TOPIC 00054: 5V Strobe (TTL)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_5v_strobe.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_5v_strobe.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### 5V Strobe (TTL)

Enables/disables the 5 V TTL external lighting strobe signal to be used with external lighting controllers. This property is valid only for NI 17xx smart cameras.

#### Values

The following list includes possible values:

- Off —External 5 V strobe output is disabled.
- Rising —External 5 V strobe output asserts a rising edge.
- Falling —External 5 V strobe output asserts a falling edge.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquire_field.html language=enus -->
## TOPIC 00055: Acquire Field

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquire_field.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquire_field.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquire Field

Sets the field acquired when the Frame/Field property is set to Field.

#### Values

The following list includes possible values:

- Even —Acquire even fields.
- Odd —Acquire odd fields.
- All —Acquire all fields.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquisition_in_progress.html language=enus -->
## TOPIC 00056: Acquisition in Progress

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquisition_in_progress.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquisition_in_progress.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition in Progress

Returns TRUE if an acquisition is in progress on the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquisition_window_height.html language=enus -->
## TOPIC 00057: Acquisition Window Height

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquisition_window_height.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquisition_window_height.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Window Height

Gets/sets the acquisition window height of the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquisition_window_left.html language=enus -->
## TOPIC 00058: Acquisition Window Left

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquisition_window_left.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquisition_window_left.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Window Left

Gets/sets the left offset of the acquisition window for the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquisition_window_top.html language=enus -->
## TOPIC 00059: Acquisition Window Top

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquisition_window_top.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquisition_window_top.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Window Top

Gets/sets the top offset of the acquisition window for the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_acquisition_window_width.html language=enus -->
## TOPIC 00060: Acquisition Window Width

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_acquisition_window_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_acquisition_window_width.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Window Width

Gets/sets the acquisition window width of the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_antichrominance_filter.html language=enus -->
## TOPIC 00061: Antichrominance Filter

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_antichrominance_filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_antichrominance_filter.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Antichrominance Filter

Gets/sets the antichrominance filter used by the image acquisition device. This property is valid only on devices with an antichrominance filter.

#### Values

The following list includes possible values:

- Disabled —specifies no video filter
- NTSC —specifies NTSC video filter
- PAL —specifies PAL video filter

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1409 NI PCI-1410 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_binary_threshold_high.html language=enus -->
## TOPIC 00062: Binary Threshold High

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_binary_threshold_high.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_binary_threshold_high.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Binary Threshold High

The upper limit for the binary threshold LUT.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_binary_threshold_low.html language=enus -->
## TOPIC 00063: Binary Threshold Low

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_binary_threshold_low.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_binary_threshold_low.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Binary Threshold Low

The lower limit for the binary threshold LUT.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_binning.html language=enus -->
## TOPIC 00064: Binning

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_binning.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_binning.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Binning

Gets/sets the binning mode of the image sensor. This property is valid only for NI 17xx smart cameras.

#### Values

The following list includes possible values:

- Off —Pixels are not combined.
- 1×2 —Vertical pixels are combined.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_bits_per_pixel.html language=enus -->
## TOPIC 00065: Bits per Pixel

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_bits_per_pixel.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_bits_per_pixel.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Bits per Pixel

Returns the bits per pixel of the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_black_reference.html language=enus -->
## TOPIC 00066: Black Reference (Volts)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_black_reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_black_reference.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Black Reference (Volts)

Gets/sets the black reference level, in volts, of the channel associated 
with this session. Refer to the following tables for value ranges that are valid for each device.

|  | Note The black reference level must be less than the white reference level. |
| --- | --- |

#### Values

The following table includes possible values:

| Datatype | Readable | Writable | Device | Range (volts) |
| --- | --- | --- | --- | --- |
|  | Always | Configuration | NI 1405 | 0 |
|  | Always | Always | NI 1407 (PCI Rev A through D) | 0 to 1.26 |
|  | Always | Always | NI 1407 (PCI Rev E or later) | 0 to 0.5 |
|  | Always | Always | NI 1407 (PXI All Revs) | 0 to 1.26 |
|  | Always | Configuration | NI 1409 | 0 to 1.4 |
|  | Always | Configuration | NI 1410 | 0 to 1.4 |
|  | Always | Configuration | NI 1411 | 0 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_bytes_per_pixel.html language=enus -->
## TOPIC 00067: Bytes per Pixel

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_bytes_per_pixel.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_bytes_per_pixel.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Bytes per Pixel

Returns the bytes per pixel of the camera associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_calibration_date.html language=enus -->
## TOPIC 00068: Calibration Date

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_calibration_date.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_calibration_date.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Calibration Date

Returns the calibration date of the image acquisition device in a time-zone independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904, Universal Time.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_channel.html language=enus -->
## TOPIC 00069: Channel

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_channel.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Channel

Programs the current channel selected on the interface (0-3) NI 1409/1410 only.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI/PXI-1409 NI PCI-1410 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_blue_gain.html language=enus -->
## TOPIC 00070: Color Blue Gain

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_blue_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_blue_gain.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Blue Gain

Gets/sets the gain applied to the blue color plane of the RGB image. This gain also affects the blue data used to calculate the hue, saturation, and luminance planes.

#### Values

The range is 0.8 to 1.198. The default value is 1.0.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_brightness.html language=enus -->
## TOPIC 00071: Color Brightness

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_brightness.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_brightness.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Brightness

Adjusts the brightness of an image-the amount of white light added to or subtracted from each image pixel. The range is -50 to +50 IRE in steps of 1. IRE is the percentage of the white level. The default is 0 IRE.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_chroma_bandwidth.html language=enus -->
## TOPIC 00072: Color Chroma Bandwidth

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_chroma_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_chroma_bandwidth.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Chroma Bandwidth

Specifies the resulting bandwidth of the chroma information of the image.

#### Values

The following list includes possible values:

- High —Highest bandwidth (default).
- Low —Lowest bandwidth.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_chroma_comb.html language=enus -->
## TOPIC 00073: Color Chroma Comb

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_chroma_comb.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_chroma_comb.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Chroma Comb

Selects the type of comb filter used in the chroma path.

#### Values

The following list includes possible values:

- Comb Off —Comb filter disabled (default in S-Video (Y/C) mode)
- Comb 1 Line —Comb filtering using one delayed line
- Comb 2 Lines —Comb filtering using two delayed lines

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_chroma_phase.html language=enus -->
## TOPIC 00074: Color Chroma Phase

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_chroma_phase.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_chroma_phase.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Chroma Phase

Specifies the value of a correction angle that can be applied to the chroma vector (adjustment of tint). This attribute is only active when an NTSC camera is used.

#### Values

The correction angle range is -180 to 180 in degrees. The default value is 0 degrees.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_chroma_process.html language=enus -->
## TOPIC 00075: Color Chroma Process

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_chroma_process.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_chroma_process.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Chroma Process

Specifies the processing applied to the chroma signal.

#### Values

The following list includes possible values:

- Chroma Process Always Off —Used with a monochrome camera (default for CCIR or RS-170).
- Always On —Used with a color camera (default for NTSC or PAL).
- Autodetect —Used if the camera type (monochrome or color) is unknown.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_chroma_trap.html language=enus -->
## TOPIC 00076: Color Chroma Trap

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_chroma_trap.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_chroma_trap.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Chroma Trap

Enables the chroma trap filter in the luma signal path. Ensure that this property is always disabled in S-Video (Y/C) mode.

#### Values

The following list includes possible values:

- FALSE —Chroma trap filter disabled (default in S-Video (Y/C) mode.)
- TRUE —Chroma trap filter enabled, if the chroma trap filter is needed in composite mode.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_contrast.html language=enus -->
## TOPIC 00077: Color Contrast

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_contrast.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_contrast.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Contrast

Adjusts the contrast of the image. The value is a scaling factor applied to every pixel. The contrast adjustment is centered around the median pixel value.

#### Values

The range is 0.4 to 1.5. The default is 1.00.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_green_gain.html language=enus -->
## TOPIC 00078: Color Green Gain

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_green_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_green_gain.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Green Gain

Gets/sets the gain applied to the green color plane of the RGB image. This gain also affects the green data used to calculate the hue, saturation, and luminance planes.

#### Values

The range is 0.8 to 1.198. The default value is 1.0.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_hsl_coring_level.html language=enus -->
## TOPIC 00079: Color HSL Coring Level

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_hsl_coring_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_hsl_coring_level.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color HSL Coring Level

Gets/sets the HSL coring level when Image Representation is set to HSL. In HSL mode, if the saturation value (S) of on any image pixel is lower than the specified value, the Hue value (H) of the pixel is set to the Hue Replace Value.

#### Values

The range is 0 to 255 LSB. The default is 0 LSB.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_hue_offset_angle.html language=enus -->
## TOPIC 00080: Color Hue Offset Angle

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_hue_offset_angle.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_hue_offset_angle.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Hue Offset Angle

Rotates the Hue plane with a specified offset angle. The hue value of a pixel is defined as an angle in the normal color plane. You can offset this angle to move the discontinuity point (at 0 modulo 360°) to another angle value.

#### Values

The range is -180° to +180°. The default is 0°.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_hue_replace_value.html language=enus -->
## TOPIC 00081: Color Hue Replace Value

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_hue_replace_value.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_hue_replace_value.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Hue Replace Value

Gets/sets the value used to replace the hue when it is below [Color HSL Coring Level](prop_color_hsl_coring_level.html). You use this property only when the Image Representation is set to HSL.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_image_representation.html language=enus -->
## TOPIC 00082: Color Image Representation

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_image_representation.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_image_representation.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Image Representation

Specifies the type of image data that will be returned when a color image is acquired.

#### Values

Values are RGB32, Red8, Green8, Blue8, Lum8, Hue8, Sat8, Int8, Lum16, Hue16, Sat16, Int16, RGB48, RGB24, RGB16, HSL32, and HSI32. Refer to [Color Image Representation](color_image_representation.html) for descriptions of these Image Representations.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_interface.html language=enus -->
## TOPIC 00083: Color Interface

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_interface.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Interface

Returns TRUE if the image acquisition device is color capable.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_luma_bandwidth.html language=enus -->
## TOPIC 00084: Color Luma Bandwidth

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_luma_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_luma_bandwidth.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Luma Bandwidth

Selects different bandwidths for the luminance signal.

#### Values

The following list includes possible values:

- Full —All filters including decimation filter disabled. Default value in CCIR or RS-170 mode.
- High —Highest available bandwidth with decimation filter enabled. Default value for PAL or NTSC mode.
- Medium —Decimation filter enabled, medium bandwidth.
- Low —Decimation filter enabled, lowest bandwidth.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_luma_comb.html language=enus -->
## TOPIC 00085: Color Luma Comb

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_luma_comb.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_luma_comb.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Luma Comb

Selects the type of comb filter used in the luma path.

#### Values

The following list includes possible values:

- Comb Off —Comb filter disabled (default in S-Video (Y/C) mode).
- Comb 1 Line —Comb filtering using 1 delayed line.
- Comb 2 Lines —Comb filtering using 2 delayed lines.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_ntsc_setup_enable.html language=enus -->
## TOPIC 00086: Color NTSC Setup Enable

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_ntsc_setup_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_ntsc_setup_enable.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color NTSC Setup Enable

Enables the setup correction of 7.5 IRE in NTSC mode. A standard NTSC signal has a setup level that moves up the black level 7.5% of the white level (or 7.5 IRE). Perform correction for this setup during acquisition by enabling this property.

#### Values

The following list includes possible values:

- FALSE —Disables the setup correction (default in PAL or CCIR mode).
- TRUE —Enables the setup correction (default in NTSC or RS-170 mode).

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_peaking_enable.html language=enus -->
## TOPIC 00087: Color Peaking Enable

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_peaking_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_peaking_enable.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Peaking Enable

Enables the peaking filter in the luma path.

#### Values

The following list includes possible values:

- FALSE —Peaking filter disabled (default)
- TRUE —Peaking filter enabled

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_red_gain.html language=enus -->
## TOPIC 00088: Color Red Gain

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_red_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_red_gain.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Red Gain

Gets/sets the gain applied to the red color plane of the RGB image. This gain also affects the red data used to calculate the hue, saturation, and luminance planes.

#### Values

The range is 0.8 to 1.198. The default value is 1.0.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_rgb_coring_level.html language=enus -->
## TOPIC 00089: Color RGB Coring Level

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_rgb_coring_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_rgb_coring_level.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color RGB Coring Level

Selects among four different coring levels. On any image pixel, if the color saturation of the pixel is lower than the specified value, the saturation is set to zero, which results in a monochrome pixel.

#### Values

The following list includes possible values:

- NoCoring —Coring not activated.
- C1 —Coring activated for saturation equal or below 1 LSB.
- C3 —Coring activated for saturation equal or below 3 LSB.
- C7 —Coring activated for saturation equal or below 7 LSB.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_color_saturation.html language=enus -->
## TOPIC 00090: Color Saturation

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_color_saturation.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_color_saturation.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color Saturation

Adjusts the saturation of the image-a factor multiplied to the chroma information of the image.

#### Values

The range is 0.5 to 1.5. The default is 1.00.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCI-1405 NI PCI/PXI-1411 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_current_level.html language=enus -->
## TOPIC 00091: Current Level

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_current_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_current_level.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Current Level

Gets/sets the amount of current sourced by the Direct Drive lighting controller, in milliamperes (mA). This property can be set regardless of the status of the [Lighting Mode](prop_lighting_mode.html) attribute. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_current_port_number.html language=enus -->
## TOPIC 00092: Current Port Number

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_current_port_number.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_current_port_number.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Current Port Number

Returns the port number that the current session is accessing.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_divide_factor.html language=enus -->
## TOPIC 00093: Divide Factor

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_divide_factor.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_divide_factor.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Divide Factor

Specifies the divide factor to use to derive the scaled encoder signal.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1426 NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_exposure_time.html language=enus -->
## TOPIC 00094: Exposure Time

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_exposure_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_exposure_time.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Exposure Time

Gets/sets the exposure time of the image sensor in milliseconds. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_external_trigger_line_filter.html language=enus -->
## TOPIC 00095: External Trigger Line Filter

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_external_trigger_line_filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_external_trigger_line_filter.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### External Trigger Line Filter

Enables the noise filter for all external trigger lines.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_fail_led.html language=enus -->
## TOPIC 00096: Fail LED

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_fail_led.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_fail_led.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Fail LED

Enables/disables the **Fail LED**. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_frame_count.html language=enus -->
## TOPIC 00097: Frame Count

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_frame_count.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_frame_count.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Frame Count

Returns the total number of images (one-based) acquired since the start of the acquisition.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_frame_rate.html language=enus -->
## TOPIC 00098: Frame Rate

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_frame_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_frame_rate.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Frame Rate

Sets/gets the desired frame rate of the image sensor, in frames per second. Setting the frame rate automatically enables [Fixed-Frame-Rate Mode](prop_fixed_frame_rate_mode.html). This property only takes effect when no buffer trigger is configured. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_frame_timeout_ms.html language=enus -->
## TOPIC 00099: Frame Timeout (ms)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_frame_timeout_ms.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_frame_timeout_ms.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Frame Timeout (ms)

Gets/sets the frame timeout value in milliseconds.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_free_buffers.html language=enus -->
## TOPIC 00100: Free Buffers

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_free_buffers.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_free_buffers.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Free Buffers

Returns the number of reserved driver buffers currently available.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_gain.html language=enus -->
## TOPIC 00101: Gain

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_gain.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Gain

Gets/sets the gain level of the image sensor. This is a raw value. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_horizontal_scaling.html language=enus -->
## TOPIC 00102: Horizontal Scaling

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_horizontal_scaling.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_horizontal_scaling.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Horizontal Scaling

Gets/sets the horizontal hardware scaling factor for the channel associated with this session.

#### Value

The following list includes possible values:

- 1/2 —Scale by 2.
- 1/4 —Scale by 4.
- 1/8 —Scale by 8.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCI/PXI-1428 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_image_type.html language=enus -->
## TOPIC 00103: Image Type

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_image_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_image_type.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Image Type

Returns the image type used as an input to the IMAQ Create VI.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_interface_type.html language=enus -->
## TOPIC 00104: Interface Type

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_interface_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_interface_type.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Interface Type

Returns the image acquisition device associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_interlacing_mode.html language=enus -->
## TOPIC 00105: Interlacing Mode

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_interlacing_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_interlacing_mode.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Interlacing Mode

Gets/sets the current interlace mode of the acquisition.

#### Values

The following list includes possible values:

- Field —Acquires a single, non-interlaced field per image buffer.
- Frame —Acquires two interlaced fields per image buffer.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_invert.html language=enus -->
## TOPIC 00106: Invert

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_invert.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_invert.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Invert

Gets/sets the invert image mode.

#### Values

The following list includes possible values:

- NonInv —The image is rightside up in memory.
- Invert —The image is upside down in memory.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_last_valid_buffer.html language=enus -->
## TOPIC 00107: Last Valid Buffer

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_last_valid_buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_last_valid_buffer.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Last Valid Buffer

Returns the buffer list index (zero-based) that contains the last acquired image. This value is always less than or equal to *N*-1, where *N* is the number of buffers in the buffer list.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_last_valid_frame.html language=enus -->
## TOPIC 00108: Last Valid Frame

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_last_valid_frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_last_valid_frame.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Last Valid Frame

Returns the cumulative buffer number (zero-based) of the last acquired image. At the beginning of the acquisition, this value starts at xFFFFFFFF and continuously increments by 1 for each image acquired.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_lighting_mode.html language=enus -->
## TOPIC 00109: Lighting Mode

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_lighting_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_lighting_mode.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Lighting Mode

Gets/sets the operation mode of the Direct Drive lighting controller. This property is valid only for NI 17xx smart cameras.

#### Values

The following list includes possible values:

- Off —Direct Drive lighting controller is disabled.
- Continuous —Direct Drive lighting controller is continuously enabled.
- Strobed —Direct Drive lighting controller is strobed with each image acquired.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_line_scan_camera.html language=enus -->
## TOPIC 00110: Line Scan Camera

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_line_scan_camera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_line_scan_camera.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Line Scan Camera

Returns TRUE if the camera associated with this session is a line scan camera.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_lookup_table.html language=enus -->
## TOPIC 00111: Lookup Table

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_lookup_table.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_lookup_table.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Lookup Table

Programs the lookup table (LUT) for the given session.

#### Values

The following list includes possible values:

- Normal
- Inverse
- Log
- Inverse Log
- Binary
- Inverse Binary

|  | Note Normal, Inverse, Binary, and Inverse Binary are the only valid values for the NI PCIe-1427 and the NI 17xx smart cameras. |
| --- | --- |

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_lost_frames.html language=enus -->
## TOPIC 00112: Lost Frames

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_lost_frames.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_lost_frames.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Lost Frames

Returns the total number of lost frames in a continuous acquisition. 
The value increments one time for each lost frame.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_max_current_level.html language=enus -->
## TOPIC 00113: Max Current Level

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_max_current_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_max_current_level.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Max Current Level

Returns the maximum amount of current, in milliamperes (mA), that can be sourced by the Direct Drive lighting controller under the current configuration. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_max_frame_rate.html language=enus -->
## TOPIC 00114: Max Frame Rate

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_max_frame_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_max_frame_rate.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Max Frame Rate

Returns the maximum achievable frame rate, in frames per second, under the current configuration. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_maximum_horizontal_resolution.html language=enus -->
## TOPIC 00115: Maximum Horizontal Resolution

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_maximum_horizontal_resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_maximum_horizontal_resolution.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Maximum Horizontal Resolution

Returns the maximum horizontal resolution of the interface.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_maximum_vertical_resolution.html language=enus -->
## TOPIC 00116: Maximum Vertical Resolution

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_maximum_vertical_resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_maximum_vertical_resolution.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Maximum Vertical Resolution

Returns the maximum vertical resolution of the interface.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_channels.html language=enus -->
## TOPIC 00117: Number of Channels

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_channels.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of Channels

Returns the number of channels that an image acquisition device supports.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_external_trigger_lines.html language=enus -->
## TOPIC 00118: Number of External Trigger Lines

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_external_trigger_lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_external_trigger_lines.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of External Trigger Lines

Returns the number of external trigger lines available to the device.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_iso_in_trigger_lines.html language=enus -->
## TOPIC 00119: Number of Iso In Trigger Lines

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_iso_in_trigger_lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_iso_in_trigger_lines.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of Iso In Trigger Lines

Returns the maximum horizontal resolution of the interface.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_iso_out_trigger_lines.html language=enus -->
## TOPIC 00120: Number of Iso Out Trigger Lines

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_iso_out_trigger_lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_iso_out_trigger_lines.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of Iso Out Trigger Lines

Returns the number of Iso Out trigger lines available to the device.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_ports.html language=enus -->
## TOPIC 00121: Number of Ports

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_ports.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_ports.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of Ports

Returns the number of ports that an image acquisition device supports.

|  | Note A port identifies a single independent data stream from a camera. All NI image acquisition devices support at least one port. Devices that support multiple ports can sustain independent and asynchronous acquisitions from the cameras on each port. |
| --- | --- |

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_post_trigger_buffers.html language=enus -->
## TOPIC 00122: Number of Post Trigger Buffers

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_post_trigger_buffers.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_post_trigger_buffers.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of Post Trigger Buffers

After receiving the stop trigger, the image acquisition device will continue acquiring this many buffers before the acquisition stops.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_number_of_rtsi_trigger_lines.html language=enus -->
## TOPIC 00123: Number of RTSI Trigger Lines

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_number_of_rtsi_trigger_lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_number_of_rtsi_trigger_lines.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Number of RTSI Trigger Lines

Returns the number of RTSI trigger lines available to the device.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_onboard_ram.html language=enus -->
## TOPIC 00124: Onboard RAM

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_onboard_ram.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_onboard_ram.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Onboard RAM

Returns the port number that the current session is accessing.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_onboard_ram_size.html language=enus -->
## TOPIC 00125: Onboard RAM Size

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_onboard_ram_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_onboard_ram_size.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Onboard RAM Size

Returns the size of onboard RAM on the image acquisition device in bytes.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_partial_scan.html language=enus -->
## TOPIC 00126: Partial Scan

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_partial_scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_partial_scan.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Partial Scan

Gets/sets the partial scan mode of the image sensor. This property is valid only for NI 17xx smart cameras.

#### Values

The following list includes possible values:

- Off —Reads the full sensor.
- 1/2 —Reads the middle half of the sensor.
- 1/4 —Reads the middle quarter of the sensor.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Configuration | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_pass_led.html language=enus -->
## TOPIC 00127: Pass LED

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_pass_led.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_pass_led.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Pass LED

Enables/disables the **Pass LED**. This property is valid only for NI 17xx smart cameras.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_phase_a_b_filter.html language=enus -->
## TOPIC 00128: Phase A & B Filter

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_phase_a_b_filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_phase_a_b_filter.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Phase A & B Filter

When TRUE, enables a low-pass noise filter for the Phase A and Phase B inputs.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

|  | Note The NI 1426 does not support enabling the Phase A & B filter. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_phase_a_polarity.html language=enus -->
## TOPIC 00129: Phase A Polarity

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_phase_a_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_phase_a_polarity.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Phase A Polarity

Get/set the Phase A signal polarity.

#### Values

The following list includes possible values:

- Active High —Sets the phase A signal polarity to active high.
- Active Low —Sets the phase A signal polarity to active low.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1426 NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

|  | Note The NI 1426 only supports a High-True Phase A signal polarity. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_phase_b_polarity.html language=enus -->
## TOPIC 00130: Phase B Polarity

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_phase_b_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_phase_b_polarity.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Phase B Polarity

Get/set the Phase B signal polarity.

#### Values

The following list includes possible values:

- Active High —Sets the phase B signal polarity to active high.
- Active Low —Sets the phase B signal polarity to active low.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1426 NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

|  | Note The NI 1426 only supports a High-True Phase B signal polarity. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_pixel_clock_detect.html language=enus -->
## TOPIC 00131: Pixel Clock Detect

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_pixel_clock_detect.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_pixel_clock_detect.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Pixel Clock Detect

Determines if the existence of a pixel clock is checked before starting an acquisition.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_pixel_depth.html language=enus -->
## TOPIC 00132: Pixel Depth

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_pixel_depth.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_pixel_depth.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Pixel Depth

Returns the maximum pixel depth of the image acquisition device in bits.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_position_u32.html language=enus -->
## TOPIC 00133: Position (U32)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_position_u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_position_u32.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Position (U32)

Returns the absolute encoder position as an unsigned 32-bit integer.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

|  | Note The NI PCI-1426 encoder hardware does not support reading the absolute encoder position. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_position_u64.html language=enus -->
## TOPIC 00134: Position (U64)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_position_u64.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_position_u64.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Position (U64)

Returns the absolute encoder position as an unsigned 64-bit integer.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

|  | Note The NI PCI-1426 encoder hardware does not support reading the absolute encoder position. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_power_over_cameralink.html language=enus -->
## TOPIC 00135: Power Over CameraLink

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_power_over_cameralink.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_power_over_cameralink.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Power Over CameraLink

Returns the status of the Power Over Camera Link circuitry. Possible values are:

- Unknown
- Not Supported
- Bad Fuse
- No Auxiliary Power
- Disabled
- Fault
- Initializing
- Inactive
- Active

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_pulse_updates.html language=enus -->
## TOPIC 00136: Pulse Updates

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_pulse_updates.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_pulse_updates.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Pulse Updates

Returns TRUE if the image acquisition device supports updating a running pulse resource.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_region_of_interest_height.html language=enus -->
## TOPIC 00137: Region of Interest Height

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_region_of_interest_height.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_region_of_interest_height.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Region of Interest Height

Gets/sets the height offset of the region of interest for the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_region_of_interest_left.html language=enus -->
## TOPIC 00138: Region of Interest Left

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_region_of_interest_left.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_region_of_interest_left.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Region of Interest Left

Gets/sets the height offset of the region of interest for the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_region_of_interest_top.html language=enus -->
## TOPIC 00139: Region of Interest Top

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_region_of_interest_top.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_region_of_interest_top.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Region of Interest Top

Gets/sets the top offset of the region of interest for the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_region_of_interest_width.html language=enus -->
## TOPIC 00140: Region of Interest Width

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_region_of_interest_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_region_of_interest_width.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Region of Interest Width

Gets/sets the top offset of the region of interest for the camera/channel associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_rowpixels.html language=enus -->
## TOPIC 00141: Rowpixels

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_rowpixels.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_rowpixels.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Rowpixels

Gets/sets the true width (in pixels) of a horizontal line in memory. Used to calculate the memory offset of the next line.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_rtsi_trigger_line_filter.html language=enus -->
## TOPIC 00142: RTSI Trigger Line Filter

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_rtsi_trigger_line_filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_rtsi_trigger_line_filter.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### RTSI Trigger Line Filter

Enables the noise filter for all RTSI trigger lines.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCIe-1427 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_send_software_trig.html language=enus -->
## TOPIC 00143: Send Software Trigger

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_send_software_trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_send_software_trig.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Send Software Trigger

Issues a trigger for an action configured to wait for a software trigger. This property is valid only for NI 17xx smart cameras.

#### Send Software Trigger

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | NotReadable | Always | NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_serial_number.html language=enus -->
## TOPIC 00144: Serial Number

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_serial_number.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_serial_number.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Serial Number

Returns the serial number of the image acquisition device associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_start_field.html language=enus -->
## TOPIC 00145: Start Field

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_start_field.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_start_field.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Start Field

Gets/sets the start field setting of the camera associated with this session. Valid when the Frame/Field property is set to Frame.

#### Values

- Even
- Odd

|  | Note Only Frame mode is valid for the NI PCI/PXI-1422 and the NI PCI-1424. |
| --- | --- |

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_temperature.html language=enus -->
## TOPIC 00146: Temperature

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_temperature.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Temperature

Returns the current temperature of the device, in degrees Celsius.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | NotWritable | NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 NI 17xx |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_variable_height_acquisition.html language=enus -->
## TOPIC 00147: Variable Height Acquisition

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_variable_height_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_variable_height_acquisition.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Variable Height Acquisition

Gets/sets the variable height acquisition mode associated with this session.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCIe-1427 NI PCI/PXI-1428 NI PCIe-1429 NI PCIe-1430 NI PCIe-1433 NI PXIe-1435 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_vertical_scaling.html language=enus -->
## TOPIC 00148: Vertical Scaling

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_vertical_scaling.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_vertical_scaling.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vertical Scaling

Gets/sets the vertical hardware scaling factor for the channel associated with this session.

#### Values

- None —No Scaling.
- 1/2 —Scale by 2.
- 1/4 —Scale by 4.
- 1/8 —Scale by 8.
- Other —User-specified scaling factor.

#### Remarks

The following table shows when the property is readable and writable and what devices it applies to.

| Datatype | Readable | Writable | Device |
| --- | --- | --- | --- |
|  | Always | Always | NI PCI-1405 NI PCI/PXI-1407 NI PCI/PXI-1409 NI PCI-1410 NI PCI/PXI-1411 NI PCI/PXI-1422 NI PCI-1424 NI PCI-1426 NI PCI/PXI-1428 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/prop_white_reference.html language=enus -->
## TOPIC 00149: White Reference (Volts)

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/prop_white_reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/prop_white_reference.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### White Reference (Volts)

Gets/sets the white reference level, in volts, of the channel associated 
with this session. Refer to the following tables for value ranges that are valid for each device.

|  | Note The white reference level must be greater than the black reference level. |
| --- | --- |

#### Values

The following table includes possible values:

| Datatype | Readable | Writable | Device | Range (volts) |
| --- | --- | --- | --- | --- |
|  | Always | Configuration | NI 1405 | 0 to 1.26 |
|  | Always | Always | NI 1407 (PCI Rev A through E or later) | 0 to 1.26 |
|  | Always | Always | NI 1407 (PXI All Revs) | 0 to 1.26 |
|  | Always | Configuration | NI 1409 | 0 to 1.4 |
|  | Always | Configuration | NI 1410 | 0 to 1.4 |
|  | Always | Configuration | NI 1411 (PXI and PCI Rev A) | 0 to 0.08 |
|  | Always | Configuration | NI 1411 (PXI and PCI Rev B or later) | 0 to 1.26 |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties.html language=enus -->
## TOPIC 00150: Image Acquisition Properties

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Image Acquisition Properties

Image acquisition properties are divided into groups. Click the links for a description, the possible values or range, and the data type of the properties within each group.

- Analog Parameters
- Device Information
- Color
- Encoder
- Image Parameters
- Status Information

#### IMAQ Property Node

[IMAGE alt='image' src='imaq_propnode.gif']

The IMAQ Property Node gets and/or sets image acquisition properties. The node is expandable. Evaluation starts from the top and proceeds downward until an error or the final evaluation occurs. To access the property node in LabVIEW 7.*x*, select **Functions»NI Measurements»Vision»Image Acquisition»Property Node**. To access the property node in LabVIEW 8.0, select **Functions»Vision and Motion»Image Acquisition»Property Node**.

To select a specific property, right-click one of the name terminals and select **Properties**. To set property information, right-click and select **Change to Write**. To get property information, right-click and select **Change to Read**. Some properties are read-only, so **Change to Write** is not listed in the context menu. If you want to add items to the node, right-click and select **Add Element** or click and drag the node to expand the number of items in the node.

The properties are changed in order from top to bottom. If an error occurs on one of the properties, the node stops at that property and returns an error. No further properties are handled. The error string reports which property caused the error.

If the small direction arrow on a property is on the left, you are setting the property value. If the small direction arrow on the property is on the right, you are getting the property value. Each property name has a short or long name that you can select by right-clicking and changing **Name Format**.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_acquisition_parameters.html language=enus -->
## TOPIC 00151: Acquisition Parameters

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_acquisition_parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_acquisition_parameters.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Parameters

Acquisition parameters define properties that describe the timing, trigger, and image size for an acquisition.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices to which the property applies. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_analog_parameters.html language=enus -->
## TOPIC 00152: Analog

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_analog_parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_analog_parameters.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Analog

Analog properties allow you to set analog device parameters such as antichrominance filter and input range.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_color.html language=enus -->
## TOPIC 00153: Color

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_color.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_color.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Color

Color properties set parameters associated with a color acquisition. You can only use the NI PCI-1405 and NI PCI/PXI-1411 for color acquisitions.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_device_information.html language=enus -->
## TOPIC 00154: Device Information

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_device_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_device_information.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Device Information

Device information properties return information concerning the image acquisition device.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_encoder.html language=enus -->
## TOPIC 00155: Encoder

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_encoder.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_encoder.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Encoder

Encoder properties return information concerning the encoder.

|  | Note Refer to the Quadrature Encoder Overview for more information about quadrature encoders. |
| --- | --- |

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_image_parameters.html language=enus -->
## TOPIC 00156: Image Parameters

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_image_parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_image_parameters.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Image Parameters

Image parameters define properties that affect the image appearance.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices to which the property applies. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_lighting.html language=enus -->
## TOPIC 00157: Lighting

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_lighting.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_lighting.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Lighting

Lighting parameters define properties that affect the Direct Drive lighting controller and external lighting strobe pins.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices to which the property applies. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/properties_status_information.html language=enus -->
## TOPIC 00158: Status Information Properties

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/properties_status_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/properties_status_information.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Status Information Properties

Status information properties return status information about an acquisition.

| Readable | Writable | Devices |
| --- | --- | --- |
| Indicates when the property is readable: Always—Property is readable both during acquisition and during configuration. Running—Property is readable only during acquisition. Configuration—Property is readable only during configuration. NotReadable—Property is never readable. | Indicates when the property is writable: Always—Property is writable both during acquisition and during configuration. Running—Property is writable only during acquisition. Configuration—Property is writable only during configuration. NotWritable—Property is never writable. | Indicates the devices that the property applies to. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/quadrature_encoder_overview.html language=enus -->
## TOPIC 00159: Quadrature Encoder Overview

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/quadrature_encoder_overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/quadrature_encoder_overview.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Quadrature Encoder Overview

A quadrature encoder uses two output channels, Phase A and Phase B, to track the position of a rotary shaft. Generally, this shaft is coupled to a motor drive that controls the movement of an object of interest. By monitoring the encoder Phase A and Phase B signals, you can obtain a precise measurement of the object's position.

To generate Phase A and Phase B signals, the quadrature encoder uses two code tracks with sectors positioned 90 degrees out of phase. The phase difference indicates the position and direction of rotation. If Phase A leads Phase B, the shaft is rotating in a clockwise direction. If Phase B leads Phase A, the shaft is rotating in a counter-clockwise direction. The following figure illustrates the Phase A signal leading the Phase B signal.

|  |
| --- |
| 1 Phase A Signal |
| 2 Phase B Signal |

Compatible NI image acquisition devices include hardware that can be used to track both the position and direction of rotation of the Phase A and Phase B signals. For example, this information can be used in conjunction with a line scan camera to acquire lines synchronous to the movement of a conveyor belt, giving you the ability to specify your line rate in terms of positional units (such as inches or centimeters) rather than time.

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/reference.html language=enus -->
## TOPIC 00160: Reference

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/reference.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Reference

[Error Codes](error_codes.html)

[Quadrature Encoder Overview](quadrature_encoder_overview.html)

[Scaled Encoder Signal](scaled_encoder_signal.html)

[Deprecated VIs](deprecated_vis.html)

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/scaled_encoder_signal.html language=enus -->
## TOPIC 00161: Scaled Encoder Signal

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/scaled_encoder_signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/scaled_encoder_signal.html
- document_id: `ni-imaq-vi-ref`
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

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/signal_i_o_pal.html language=enus -->
## TOPIC 00162: Signal I/O

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/signal_i_o_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/signal_i_o_pal.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Signal I/O

Owning Palette:

NI-IMAQ

Installed With:

Use Signal I/O VIs to control the trigger lines, generate pulses, and wait for hardware events.

| Palette Object | Description |
| --- | --- |
| IMAQ Configure Trigger3 | Configures the trigger conditions for an acquisition. Use this VI before any acquisition VI to setup a triggered image acquisition. |
| IMAQ Trigger Drive2 | Drives a trigger line with a specified signal. |
| IMAQ Trigger Read2 | Reads the current value of a trigger line. |
| IMAQ Trigger Route2 | Drives the destination trigger line with the signal on the source trigger line. |
| IMAQ Generate Pulse3 | Generates a pulse on a trigger line. IMAQ Generate Pulse3 can generate a pulse immediately or on the assertion edge of a status or trigger signal. Each trigger pulse uses a Pulse ID, which is automatically generated each time you call this VI. |
| IMAQ Occurrence Config2 | Creates occurrences that are set by image acquisition signals such as the assertion of a status or trigger signal. Occurrences produced by this VI are used as inputs to the Wait on Occurrence LabVIEW primitive. Anything dependent on the execution of the Wait on Occurrence primitive will wait until the occurrence is set. |
| IMAQ Wait Signal2 | Waits for either a status or trigger signal to be asserted. IMAQ Wait Signal2 does not return until the specified signal is asserted or a timeout occurs. |
| IMAQ Reset Encoder Position | Resets the absolute encoder position counter to 0. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/vision_express_pal.html language=enus -->
## TOPIC 00163: Vision Express VIs

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/vision_express_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/vision_express_pal.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vision Express

Use the Vision Express VIs to quickly develop common image acquisition and processing applications.

| Palette Object | Description |
| --- | --- |
| Vision Assistant Express VI | Use NI Vision Assistant from within the LabVIEW environment to perform common image processing tasks. You must install the NI Vision Development Module to use the Vision Assistant Express VI. |
| Vision Acquisition Express VI | Acquires images from cameras using NI-IMAQ or NI-IMAQdx. Refer to the NI Vision Acquisition Express VI Help for more information. |

<!--NI_TOPIC bundle=ni-imaq-vi-ref path=niimaqvireference/visionrio_reference.html language=enus -->
## TOPIC 00164: Vision-RIO Reference

- bundle_id: `ni-imaq-vi-ref`
- source_path: `niimaqvireference/visionrio_reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaq-vi-ref/raw/resource/enus/niimaqvireference/visionrio_reference.html
- document_id: `ni-imaq-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vision-RIO Reference

Use this book for information about the I/O signals available for use with your reconfigurable vision device. For more information about front panel connectors, pinouts, and specifications, refer to the User Guide and Specifications document shipped with your NI Vision device.
