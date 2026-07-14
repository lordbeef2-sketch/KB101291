# NI DOCUMENT BUNDLE: ni-imaqdx-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-imaqdx-c-api-ref start=1 end=83 -->
<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/attribute_name.html language=enus -->
## TOPIC 00001: Attributes by Name

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/attribute_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/attribute_name.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Attributes by Name

The following table, sorted by attribute name, describes the attributes you can use with the attribute functions.

| Attribute Name | Attribute | Type | Description |
| --- | --- | --- | --- |
| IMAQdxAttributeBaseAddress | CameraInformation::BaseAddress | U32 | Read only. Gets the base address of the camera registers. |
| IMAQdxAttributeBusType | CameraInformation::BusType | Enum | Read only. Gets the bus type of the camera. |
| IMAQdxAttributeModelName | CameraInformation::ModelName | String | Read only. Returns the model name. |
| IMAQdxAttributeSerialNumberHigh | CameraInformation::SerialNumberHigh | U32 | Read only. Gets the upper 32-bits of the camera 64-bit serial number. |
| IMAQdxAttributeSerialNumberLow | CameraInformation::SerialNumberLow | U32 | Read only. Gets the lower 32-bits of the camera 64-bit serial number. |
| IMAQdxAttributeVendorName | CameraInformation::VendorName | String | Read only. Returns the vendor name. |
| IMAQdxAttributeHostIPAddress | CameraInformation::HostIPAddress | String | Read only. Returns the host adapter IP address. |
| IMAQdxAttributeIPAddress | CameraInformation::IPAddress | String | Read only. Returns the IP address. |
| IMAQdxAttributePrimaryURLString | CameraInformation::PrimaryURLString | String | Read only. Gets the camera's primary URL string. |
| IMAQdxAttributeSecondaryURLString | CameraInformation::SecondaryURLString | String | Read only. Gets the camera's secondary URL string. |
| IMAQdxAttributeAcqInProgress | StatusInformation::AcqInProgress | Bool | Read only. Gets the current state of the acquisition. TRUE if acquiring; otherwise FALSE. |
| IMAQdxAttributeHandledEventCount | StatusInformation::HandledEventCount | U32 | Read only. Gets the number of handled events during an acquisition session. |
| IMAQdxAttributeLastBufferCount | StatusInformation::LastBufferCount | U32 | Read only. Gets the number of transferred buffers. |
| IMAQdxAttributeLastBufferNumber | StatusInformation::LastBufferNumber | U32 | Read only. Gets the last cumulative buffer number transferred. |
| IMAQdxAttributeLostBufferCount | StatusInformation::LostBufferCount | U32 | Read only. Gets the number of lost buffers during an acquisition session. |
| IMAQdxAttributeLostEventCount | StatusInformation::LostEventCount | U32 | Read only. Gets the number of lost events during an acquisition session. |
| IMAQdxAttributeLostPacketCount | StatusInformation::LostPacketCount | U32 | Read only. Gets the number of lost packets during an acquisition session. |
| IMAQdxAttributeRequestedResendPackets | StatusInformation::RequestedResendPacketCount | U32 | Read only. Gets the number of packets requested to be resent during an acquisition session. |
| IMAQdxAttributeReceivedResendPackets | StatusInformation::ReceivedResendPackets | U32 | Read only. Gets the number of packets that were requested to be resent during an acquisition session and were completed. |
| IMAQdxAttributeBayerGainB | AcquisitionAttributes::Bayer::GainB | F64 | Sets/gets the white balance gain for the blue component of the Bayer conversion. |
| IMAQdxAttributeBayerGainG | AcquisitionAttributes::Bayer::GainG | F64 | Sets/gets the white balance gain for the green component of the Bayer conversion. |
| IMAQdxAttributeBayerGainR | AcquisitionAttributes::Bayer::GainR | F64 | Sets/gets the white balance gain for the red component of the Bayer conversion. |
| IMAQdxAttributeBayerPattern | AcquisitionAttributes::Bayer::Pattern | Enum | Sets/gets the Bayer pattern to use. |
| IMAQdxAttributeStreamChannelMode | AcquisitionAttributes::Controller::StreamChannelMode | Enum | Gets/sets the mode for allocating a FireWire stream channel. |
| IMAQdxAttributeDesiredStreamChannel | AcquisitionAttributes::Controller::DesiredStreamChannel | U32 | Gets/sets the stream channel to manually allocate. |
| IMAQdxAttributeFrameInterval | AcquisitionAttributes::FrameInterval | U32 | Read only. Gets the duration in milliseconds between successive frames. |
| IMAQdxAttributeIgnoreFirstFrame | AcquisitionAttributes::IgnoreFirstFrame | Bool | Gets/sets the video delay of one frame between starting the camera and receiving the video feed. |
| IMAQdxAttributeOffsetX | OffsetX | U32 | Gets/sets the left offset of the image. |
| IMAQdxAttributeOffsetY | OffsetY | U32 | Gets/sets the top offset of the image. |
| IMAQdxAttributeWidth | Width | U32 | Gets/sets the width of the image. |
| IMAQdxAttributeHeight | Height | U32 | Gets/sets the height of the image. |
| IMAQdxAttributePixelFormat | PixelFormat | U32 | Gets/sets the pixel format of the source sensor. |
| IMAQdxAttributePixelSignedness | AcquisitionAttributes::PixelSignedness | Enum | Gets/sets the signedness of the pixel. For 16-bit components, this represents the actual pixel signedness (Signed, or Unsigned). |
| IMAQdxAttributePacketSize | PacketSize | U32 | Gets/sets the packet size in bytes. |
| IMAQdxAttributePayloadSize | PayloadSize | U32 | Gets/sets the frame size in bytes. |
| IMAQdxAttributeSpeed | AcquisitionAttributes::Speed | Enum | Gets/sets the transfer speed in Mbps for a FireWire packet. |
| IMAQdxAttributeShiftPixelBits | AcquisitionAttributes::ShiftPixelBits | Bool | Gets/sets the alignment of 16-bit cameras. Downshift the pixel bits if the camera returns most significant bit-aligned data. |
| IMAQdxAttributeSwapPixelBytes | AcquisitionAttributes::SwapPixelBytes | Bool | Gets/sets the endianness of 16-bit cameras. Swap the pixel bytes if the camera returns little endian data. |
| IMAQdxAttributeOverwriteMode | AcquisitionAttributes::OverwriteMode | Enum | Gets/sets the overwrite mode, used to determine acquisition when an image transfer cannot be completed due to an overwritten internal buffer. |
| IMAQdxAttributeTimeout | AcquisitionAttributes::Timeout | U32 | Gets/sets the timeout value in milliseconds, used to abort an acquisition when the image transfer cannot be completed within the delay. |
| IMAQdxAttributeVideoMode | AcquisitionAttributes::VideoMode | U32 | Gets/sets the video mode for a camera. |
| IMAQdxAttributeBitsPerPixel | AcquisitionAttributes::BitsPerPixel | Enum | Gets/sets the actual bits per pixel. For 16-bit components, this represents the actual bit depth (10-, 12-, 14-, or 16-bit). |
| IMAQdxAttributeReserveDualPackets | AcquisitionAttributes::ReserveDualPackets | Bool | Gets/sets if dual packets will be reserved for a very large FireWire packet. |
| IMAQdxAttributeReceiveTimestampMode | AcquisitionAttributes::ReceiveTimestampMode | Enum | Gets/sets the mode for timestamping images received by the driver. |
| IMAQdxAttributeActualPeakBandwidth | AcquisitionAttributes::AdvancedEthernet::BandwidthControl::ActualPeakBandwidth | F64 | Read only. Returns the actual maximum peak bandwidth the camera will be configured to use. |
| IMAQdxAttributeDesiredPeakBandwidth | AcquisitionAttributes::AdvancedEthernet::BandwidthControl::DesiredPeakBandwidth | F64 | Gets/sets the desired maximum peak bandwidth the camera should use. |
| IMAQdxAttributeDestinationMode | AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMode | Enum | Gets/Sets where the camera is instructed to send the image stream. |
| IMAQdxAttributeDestinationMulticastAddress | AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMulticastAddress | String | Gets/Sets the multicast address the camera should send data in multicast mode. |
| IMAQdxAttributeEventsEnabled | AcquisitionAttributes::AdvancedEthernet::EventParameters::EventsEnabled | Bool | Gets/Sets if events will be handled. |
| IMAQdxAttributeMaxOutstandingEvents | AcquisitionAttributes::AdvancedEthernet::EventParameters::MaxOutstandingEvents | U32 | Gets/Sets the maximum number of outstanding events to queue. |
| IMAQdxAttributeLostPacketMode | AcquisitionAttributes::AdvancedEthernet::LostPacketMode | Enum | Gets/sets the behavior when the user extracts a buffer that has missing packets. |
| IMAQdxAttributeMemoryWindowSize | AcquisitionAttributes::AdvancedEthernet::ResendParameters::MemoryWindowSize | U32 | Gets/sets the size of the memory window of the camera in kilobytes. Should match the camera's internal buffer size. |
| IMAQdxAttributeResendsEnabled | AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendsEnabled | Bool | Gets/sets if resends will be issued for missing packets. |
| IMAQdxAttributeResendThresholdPercentage | AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendThresholdPercentage | U32 | Gets/sets the threshold of the packet processing window that will trigger packets to be resent. |
| IMAQdxAttributeResendBatchingPercentage | AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendBatchingPercentage | U32 | Gets/sets the percent of the packet resend threshold that will be issued as one group past the initial threshold sent in a single request. |
| IMAQdxAttributeMaxResendsPerPacket | AcquisitionAttributes::AdvancedEthernet::ResendParameters::MaxResendsPerPacket | U32 | Gets/sets the maximum number of resend requests that will be issued for a missing packet. |
| IMAQdxAttributeResendResponseTimeout | AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendResponseTimeout | U32 | Gets/sets the time to wait for a resend request to be satisfied before sending another. |
| IMAQdxAttributeNewPacketTimeout | AcquisitionAttributes::AdvancedEthernet::ResendParameters::NewPacketTimeout | U32 | Gets/sets the time to wait for new packets to arrive in a partially completed image before assuming the rest of the image was lost. |
| IMAQdxAttributeMissingPacketTimeout | AcquisitionAttributes::AdvancedEthernet::ResendParameters::MissingPacketTimeout | U32 | Gets/sets the time to wait for a missing packet before issuing a resend. |
| IMAQdxAttributeResendTimerResolution | AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendTimerResolution | U32 | Gets/sets the resolution of the packet processing system that is used for all packet-related timeouts. |
| IMAQdxAttributeTestPacketEnabled | AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketEnabled | Bool | Gets/Sets whether the driver will validate the image streaming settings using test packets prior to an acquisition |
| IMAQdxAttributeTestPacketTimeout | AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketTimeout | U32 | Gets/Sets the timeout for validating test packet reception (if enabled) |
| IMAQdxAttributeMaxTestPacketRetries | AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::MaxTestPacketRetries | U32 | Gets/Sets the number of retries for validating test packet reception (if enabled) |
| IMAQdxAttributeChunkDataDecodingEnabled | AcquisitionAttributes::ChunkDataDecoding::ChunkDataDecodingEnabled | Bool | Gets/Sets whether the driver will decode any chunk data in the image stream |
| IMAQdxAttributeChunkDataDecodingMaxElementSize | AcquisitionAttributes::ChunkDataDecoding::MaximumChunkCopySize | U32 | Gets/Sets the maximum size of any single chunk data element that will be made available |

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/conventions.html language=enus -->
## TOPIC 00002: Conventions

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/conventions.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/conventions.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Conventions

This help file uses the following conventions:

| < > | Angle brackets that contain numbers separated by an ellipsis represent a range of values associated with a bit or signal name—for example, DBIO<3..0>. |
| --- | --- |
| » | The » symbol leads you through nested menu items and dialog box options to a final action. The sequence File»Page Setup»Options directs you to pull down the File menu, select the Page Setup item, and select Options from the last dialog box. |
|  | This icon denotes a note, which alerts you to important information. |
| bold | Bold text denotes items that you must select or click in the software, such as menu items and dialog box options. Bold text also denotes parameter names, emphasis, or an introduction to a key concept. |
| green | Underlined text in this color denotes a link to a help topic, help file, or Web address. |
| monospace | Text in this font denotes text or characters that you should enter from the keyboard, sections of code, programming examples, and syntax examples. This font is also used for the proper names of disk drives, paths, directories, programs, subprograms, subroutines, device names, functions, operations, variables, filenames, and extensions. |
| monospace bold | Bold text in this font denotes the messages and responses that the computer automatically prints to the screen. This font also emphasizes lines of code that are different from the other examples. |

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/cvi_function_tree.html language=enus -->
## TOPIC 00003: LabWindows/CVI Function Tree

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/cvi_function_tree.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/cvi_function_tree.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI Function Tree

The following table shows the LabWindows/CVI function panel that corresponds to each NI-IMAQdx function.

| Class/Panel Name | Function Name | Description |
| --- | --- | --- |
| High-Level Acquisition |  |  |
| Snap | IMAQdxSnap | Configures, starts, acquires, and unconfigures a snap acquisition. |
| Configure Grab | IMAQdxConfigureGrab | Configures and starts a grab acquisition. A grab performs an acquisition that loops continually on a ring of buffers. |
| Grab | IMAQdxGrab | Acquires the most current frame into image. |
| Sequence | IMAQdxSequence | Configures, starts, acquires, stops, and unconfigures a sequence acquisition. Use this function to capture multiple images. |
| Low-Level Session |  |  |
| Reset Ethernet Camera Address | IMAQdxResetEthernetCameraAddress | Use this function to reset Ethernet cameras on the network with a local subnet. This function will be blocked and will return when the reset is complete or after the specified timeout. |
| Discover Ethernet Cameras | IMAQdxDiscoverEthernetCameras | Initiates a round of Ethernet camera discovery. Use this function to find Ethernet cameras on the network with a remote subnet. |
| Enumerate Cameras | IMAQdxEnumerateCameras | Returns a list of all cameras on the host computer. |
| Reset Camera | IMAQdxResetCamera | Performs a manual reset on a camera. Stops any ongoing acquisitions. |
| Open Camera | IMAQdxOpenCamera | Opens a camera, queries the camera for its capabilities, loads a camera configuration file, and creates a unique reference to the camera. |
| Close Camera | IMAQdxCloseCamera | Stops an acquisition in progress, releases resources associated with an acquisition, and closes the specified Camera Session. |
| Low-Level Acquisition |  |  |
| Configure Acquisition | IMAQdxConfigureAcquisition | Configures a low-level acquisition previously opened with IMAQdxOpenCamera. |
| Start Acquisition | IMAQdxStartAcquisition | Starts an acquisition that was previously configured with IMAQdxConfigureAcquisition. |
| Get Image | IMAQdxGetImage | Acquires the specified frame into image. Call this function only after calling IMAQdxConfigureAcquisition. |
| Get Image Data | IMAQdxGetImageData | Copies the raw data of the specified frame into buffer. Call this function only after calling IMAQdxConfigureAcquisition. |
| Stop Acquisition | IMAQdxStopAcquisition | Stops an acquisition previously started with IMAQdxStartAcquisition. |
| Unconfigure Acquisition | IMAQdxUnconfigureAcquisition | Unconfigures an acquisition previously configured with IMAQdxConfigureAcquisition. |
| Low-Level Attribute |  |  |
| Enumerate Video Modes | IMAQdxEnumerateVideoModes | Returns a list of video modes supported by the camera. |
| Enumerate Attributes | IMAQdxEnumerateAttributes2 | Gets the attributes supported by the camera. |
| Get Attribute | IMAQdxGetAttribute | Gets the current value for a camera attribute. |
| Set Attribute | IMAQdxSetAttribute | Sets the value for a camera attribute. |
| Get Attribute Minimum | IMAQdxGetAttributeMinimum | Gets the minimum for a camera attribute. |
| Get Attribute Maximum | IMAQdxGetAttributeMaximum | Gets the maximum for a camera attribute. |
| Get Attribute Increment | IMAQdxGetAttributeIncrement | Gets the increment for a camera attribute. |
| Get Attribute Type | IMAQdxGetAttributeType | Gets the attribute type for a camera. |
| Is Attribute Readable | IMAQdxIsAttributeReadable | Gets the read permissions for a camera attribute. |
| Is Attribute Writable | IMAQdxIsAttributeWritable | Gets the write permissions for a camera attribute. |
| Enumerate Attribute Values | IMAQdxEnumerateAttributeValues | Gets the values supported by the camera attribute. |
| Get Attribute Tooltip | IMAQdxGetAttributeTooltip | Gets the tooltip for the camera attribute. |
| Get Attribute Units | IMAQdxGetAttributeUnits | Gets the attribute units for a camera. |
| Get Attribute Visibility | IMAQdxGetAttributeVisibility | Gets the visibility for a camera attribute. |
| Get Attribute Description | IMAQdxGetAttributeDescription | Gets the description for the camera attribute. |
| Get Attribute Display Name | IMAQdxGetAttributeDisplayName | Gets the display name for the camera attribute. |
| Write Attributes | IMAQdxWriteAttributes | Saves a configuration file for a camera. |
| Read Attributes | IMAQdxReadAttributes | Loads a configuration file for a camera. |
| Low-Level Event |  |  |
| Register Frame Done Event | IMAQdxRegisterFrameDoneEvent | Configures the NI-IMAQdx driver to execute a callback function when a frame done event occurs. |
| Register Plug and Play Event | IMAQdxRegisterPnpEvent | Configures the NI-IMAQdx driver to execute a callback function when a plug and play event occurs. |
| Low-Level Register |  |  |
| Write Register | IMAQdxWriteRegister | Accesses registers on the camera and writes a 32-bit value to the camera. Data is byte-swapped for big endian alignment before transfer. |
| Read Register | IMAQdxReadRegister | Accesses registers on the camera and reads a 32-bit value from the camera. Data is byte-swapped for little endian alignment after transfer. |
| Write Memory | IMAQdxWriteMemory | Accesses registers on the camera and writes a string to the camera. |
| Read Memory | IMAQdxReadMemory | Accesses registers on the camera and reads a string from the camera. |
| Low-Level Utility |  |  |
| Get Error String | IMAQdxGetErrorString | Returns a string describing the error code. |

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/error_codes.html language=enus -->
## TOPIC 00004: Error Codes

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/error_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/error_codes.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes

The following table describes the error codes used in NI-IMAQdx.

| Error Code | Status Name | Description |
| --- | --- | --- |
| -1074360320 | IMAQdxErrorSystemMemoryFull | Not enough memory |
| -1074360319 | IMAQdxErrorInternal | Internal error |
| -1074360318 | IMAQdxErrorInvalidParameter | Invalid parameter |
| -1074360317 | IMAQdxErrorInvalidPointer | Invalid pointer |
| -1074360316 | IMAQdxErrorInvalidInterface | Invalid camera session |
| -1074360315 | IMAQdxErrorInvalidRegistryKey | Invalid registry key |
| -1074360314 | IMAQdxErrorInvalidAddress | Invalid address |
| -1074360313 | IMAQdxErrorInvalidDeviceType | Invalid device type |
| -1074360312 | IMAQdxErrorNotImplemented | Not implemented yet |
| -1074360311 | IMAQdxErrorCameraNotFound | Camera not found |
| -1074360310 | IMAQdxErrorCameraInUse | Camera is already in use. |
| -1074360309 | IMAQdxErrorCameraNotInitialized | Camera is not initialized. |
| -1074360308 | IMAQdxErrorCameraRemoved | Camera has been removed. |
| -1074360307 | IMAQdxErrorCameraRunning | Acquisition in progress. |
| -1074360306 | IMAQdxErrorCameraNotRunning | No acquisition in progress. |
| -1074360305 | IMAQdxErrorAttributeNotSupported | Attribute not supported by the camera. |
| -1074360304 | IMAQdxErrorAttributeNotSettable | Unable to set attribute. |
| -1074360303 | IMAQdxErrorAttributeNotReadable | Unable to get attribute. |
| -1074360302 | IMAQdxErrorAttributeOutOfRange | Attribute value is out of range. |
| -1074360301 | IMAQdxErrorBufferNotAvailable | Requested buffer is unavailable. |
| -1074360300 | IMAQdxErrorBufferListEmpty | Buffer list is empty. Add one or more buffers. |
| -1074360299 | IMAQdxErrorBufferListLocked | Buffer list is already locked. Reconfigure acquisition and try again. |
| -1074360298 | IMAQdxErrorBufferListNotLocked | No buffer list. Reconfigure acquisition and try again. |
| -1074360297 | IMAQdxErrorResourcesAllocated | Transfer engine resources already allocated. Reconfigure acquisition and try again. |
| -1074360296 | IMAQdxErrorResourcesUnavailable | Insufficient transfer engine resources. |
| -1074360295 | IMAQdxErrorAsyncWrite | Unable to perform asynchronous register write. |
| -1074360294 | IMAQdxErrorAsyncRead | Unable to perform asynchronous register read. |
| -1074360293 | IMAQdxErrorTimeout | Timeout |
| -1074360292 | IMAQdxErrorBusReset | Bus reset occurred during a transaction. |
| -1074360291 | IMAQdxErrorInvalidXML | Unable to load camera's XML file. |
| -1074360290 | IMAQdxErrorFileAccess | Unable to read/write to file. |
| -1074360289 | IMAQdxErrorInvalidCameraURLString | Camera has malformed URL string. |
| -1074360288 | IMAQdxErrorInvalidCameraFile | Invalid camera file. |
| -1074360287 | IMAQdxErrorGenICamError | Unknown Genicam error. |
| -1074360286 | IMAQdxErrorFormat7Parameters | For format 7: The combination of speed, image position, image size, and color coding is incorrect. |
| -1074360285 | IMAQdxErrorInvalidAttributeType | The attribute type is not compatible with the passed variable type. |
| -1074360284 | IMAQdxErrorDLLNotFound | The DLL could not be found. |
| -1074360283 | IMAQdxErrorFunctionNotFound | The function could not be found. |
| -1074360282 | IMAQdxErrorLicenseNotActivated | License not activated. |
| -1074360281 | IMAQdxErrorCameraNotConfiguredForListener | The camera is not configured properly to support a listener. |
| -1074360280 | IMAQdxErrorCameraMulticastNotAvailable | Unable to configure the system for multicast support. |
| -1074360279 | IMAQdxErrorBufferHasLostPackets | The requested buffer has lost packets and the user requested an error to be generated. |
| -1074360278 | IMAQdxErrorGiGEVisionError | Unknown GiGE Vision error. |
| -1074360277 | IMAQdxErrorNetworkError | Unknown network error. |
| -1074360276 | IMAQdxErrorCameraUnreachable | Unable to connect to the camera |
| -1074360275 | IMAQdxErrorHighPerformanceNotSupported | High performance acquisition is not supported on the specified network interface. Connect the camera to a network interface running the high performance driver. |
| -1074360274 | IMAQdxErrorInterfaceNotRenamed | Unable to rename interface. Invalid or duplicate name specified. |
| -1074360273 | IMAQdxErrorNoSupportedVideoModes | The camera does not have any video modes which are supported. |
| -1074360272 | IMAQdxErrorSoftwareTriggerOverrun | Software trigger overrun. |
| -1074360271 | IMAQdxErrorTestPacketNotReceived | The system cannot acquire images. The packet size may be too large for the network setup or a firewall may be blocking the network traffic from the camera. For more information, visit ni.com/info and enter 'GigEVisionNetworkConnectivity'. |
| -1074360270 | IMAQdxErrorCorruptedImageReceived | The camera returned a corrupted image. |
| -1074360269 | IMAQdxErrorCameraConfigurationHasChanged | The camera did not return an image of the correct type it was configured for previously. |
| -1074360268 | IMAQdxErrorCameraInvalidAuthentication | The camera is configured with password authentication and either the user name and password were not configured or they are incorrect. |
| -1074360267 | IMAQdxErrorUnknownHTTPError | The camera returned an unknown HTTP error. |
| -1074360266 | IMAQdxErrorKernelDriverUnavailable | Unable to attach to the kernel mode driver. |
| -1074360265 | IMAQdxErrorPixelFormatDecoderUnavailable | No decoder available for selected pixel format. |
| -1074360264 | IMAQdxErrorFirmwareUpdateNeeded | The acquisition hardware needs a firmware update before it can be used. |
| -1074360263 | IMAQdxErrorFirmwareUpdateRebootNeeded | The firmware on the acquisition hardware has been updated and the system must be rebooted before use. |
| -1074360262 | IMAQdxErrorLightingCurrentOutOfRange | The requested current level from the lighting controller is not possible. |
| -1074360261 | IMAQdxErrorUSB3VisionError | Unknown USB3 Vision error. |
| -1074360260 | IMAQdxErrorInvalidU3VUSBDescriptor | The camera has a USB descriptor that is incompatible with the USB3 Vision specification. |
| -1074360259 | IMAQdxErrorU3VInvalidControlInterface | The USB3 Vision control interface is not implemented or is invalid on this camera. |
| -1074360258 | IMAQdxErrorU3VControlInterfaceError | There was an error from the control interface of the USB3 Vision camera. |
| -1074360257 | IMAQdxErrorU3VInvalidEventInterface | The USB3 Vision event interface is not implemented or is invalid on this camera. |
| -1074360256 | IMAQdxErrorU3VEventInterfaceError | There was an error from the event interface of the USB3 Vision camera. |
| -1074360255 | IMAQdxErrorU3VInvalidStreamInterface | The USB3 Vision stream interface is not implemented or is invalid on this camera. |
| -1074360254 | IMAQdxErrorU3VStreamInterfaceError | There was an error from the stream interface of the USB3 Vision camera. |
| -1074360253 | IMAQdxErrorU3VUnsupportedConnectionSpeed | The USB connection speed is not supported by the camera. Check whether the camera is plugged into a USB 2.0 port instead of a USB 3.0 port. If so, verify that the camera supports this use case. |
| -1074360252 | IMAQdxErrorU3VInsufficientPower | The USB3 Vision camera requires more current than can be supplied by the USB port in use. |
| -1074360251 | IMAQdxErrorU3VInvalidMaxCurrent | The U3V_MaximumCurrentUSB20_mA registry value is not valid for the connected USB3 Vision camera. |
| -1074360250 | IMAQdxErrorBufferIncompleteData | The requested buffer has incomplete data and the user requested an error to be generated. |
| -1074360249 | IMAQdxErrorCameraAcquisitionConfigFailed | The camera returned an error starting the acquisition. |
| -1074360248 | IMAQdxErrorCameraClosePending | The camera still has outstanding references and will be closed when these operations complete. |
| -1074360247 | IMAQdxErrorSoftwareFault | An unexpected software error occurred. |
| -1074360246 | IMAQdxErrorCameraPropertyInvalid | The value for an invalid camera property was requested. |
| -1074360245 | IMAQdxErrorJumboFramesNotEnabled | Jumbo frames are not enabled on the host. Maximum packet size is 1500 bytes. |
| -1074360244 | IMAQdxErrorBayerPixelFormatNotSelected | This operation requires that the camera has a Bayer pixel format selected. |
| -1074360243 | IMAQdxErrorRingAcqImageSizeNotAligned | For a ring acquisition with both image and chunk data, the total image size in bytes must be a multiple of the size alignment specified by the Required Payload Size Alignment attribute. |
| -1074360242 | IMAQdxErrorRingAcqChunkDataSizeTooBig | For a ring acquisition, the chunk data size must be less than the maximum payload transfer size specified by the Actual Maximum Payload Transfer Size attribute. |
| -1074360241 | IMAQdxErrorBufferNotExtracted | The requested buffer to release is not currently extracted. |
| -1074360240 | IMAQdxErrorDuplicateImageInRing | Duplicate images were found in the ring acquisition configuration. |
| -1074360239 | IMAQdxErrorImageNotConfiguredInRing | The image passed is not currently configured in the ring. |
| -1074360238 | IMAQdxErrorMismatchedBorders | The ring acquisition is configured to use images with different border sizes. All images in a ring acquisition must have the same border size. |
| -1074360237 | IMAQdxErrorRingAcqDecodeRequired | For ring acquisitions, manipulating the image data prior to extraction is not allowed. The combination of the Pixel Format, Output Image Type, Pixel Signedness, Swap Pixel Bytes, and Shift Pixel Bits attributes requires the image data to be altered. |
| -1074360236 | IMAQdxErrorRingAcqNonZeroBorder | For a ring acquisition with this camera, the images must have a border size of 0 pixels. |
| -1074360235 | IMAQdxErrorRingAcqWidthNotAligned | For a ring acquisition with this camera, the image width must be a multiple of the image's required line alignment. |
| -1074360234 | IMAQdxErrorRingAcqOnly | This function can only be called within the context of a ring acquisition. |
| -1074360233 | IMAQdxErrorRingAcqNotEnoughImages | The ring acquisition was not configured with enough images to meet the minimum requirements for a continuous acquisition. |
| -1074360232 | IMAQdxErrorImageDisposed | The requested image has been disposed and is no longer valid. |
| -1074360231 | IMAQdxErrorRingAcqPaddingCapabilityExceeded | The padding necessary to transfer the configured image using a ring acquisition is more than the camera can provide. Reduce the amount of padding required by reducing the image border size or changing the image width. |
| -1074360230 | IMAQdxErrorNIGEVUpdateRequired | The NI-GEV driver is too old to support this functionality. Please update it to a newer version. |
| -1074360229 | IMAQdxErrorPacketSizeOver9000 | The desired packet size is larger than the maximum value of 9000 supported by the network interface. |
| -1074360228 | IMAQdxErrorAttributeSetFailure | There was a failure when trying to set the value of a writeable camera attribute. |
| -1074360227 | IMAQdxErrorFirmwareUpdatePowerCycleNeeded | The firmware on the acquisition hardware has been updated. Shutdown the system, disconnect power, and then reconnect power before use. |
| -1074360226 | IMAQdxErrorLensCommunicationFailure | An error occurred while communicating with the lens. |
| -1074360225 | IMAQdxErrorBIOSIncompatible | The BIOS version is incompatible with the installed version of NI-IMAQdx. |
| -1074360224 | IMAQdxErrorAdministrativePrivilegesRequired | The requested operation requires administrative privileges. |
| -1074360223 | IMAQdxErrorNIIMAQUpdateRequired | The NI-IMAQ driver is too old to support the NI-IMAQdx API. Please update it to a newer version. |
| -1074360222 | IMAQdxErrorCannotRenameBoardWhileSessionOpen | The board cannot be renamed while there are open sessions to any of its acquisition units. |
| -1074360221 | IMAQdxErrorRingAcqInvalidPacketSize | For a ring acquisition with this camera, the Payload Size must be a multiple of the Packet Size. Adjust the Packet Size attribute accordingly. |
| -1074360220 | IMAQdxErrorBufferNumberOutOfRange | The requested buffer number is outside of the range of acquirable buffer numbers for this one-shot acquisition. |
| -1074360219 | IMAQdxErrorUnknownTapGeometry | The DeviceTapGeometry attribute setting does not match the expected format. |
| -1074360218 | IMAQdxErrorCLGenICamProbeTimeout | Cannot communicate with the camera. Ensure the Camera Link cables are connected properly. If using PoCL to power the camera, it is possible that the camera did not fully power on before the timeout expired. Retry opening a session to the camera. |
| -1074360217 | IMAQdxErrorAcquisitionTerminated | An error occurred while acquiring from the camera so the acquisition has been terminated. |
| -1074360216 | IMAQdxErrorInvalidDynamicImageChange | The camera returned an image that was incompatible with the acquisition configuration. Dynamic changes to the image dimensions are not supported. |
| -1074360215 | IMAQdxErrorIncompatibleImageDataRing | The camera returned an image that was incompatible with the buffer that was allocated for it. With these settings, a Grab acquisition must be used instead of a Ring. |
| -1074360214 | IMAQdxErrorGenICamPersistence | An error occurred while persisting camera attributes with GenICam software. Change the PersistenceAlgorithm attribute to Auto or NI-IMAQdx to see whether the internal algorithm provides better results. |
| -1074360213 | IMAQdxErrorAcquisitionNotSupported | Acquisition is not supported on this device. |
| -1074360212 | IMAQdxErrorFirmwareVersionMismatch | The version of the firmware is not compatible with this version of NI-IMAQdx. |

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxclosecamera.html language=enus -->
## TOPIC 00005: IMAQdxCloseCamera

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxclosecamera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxclosecamera.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxCloseCamera

#### Format

rval = IMAQdxCloseCamera (IMAQdxSession id);

#### Purpose

Stops an acquisition in progress, releases resources associated with an acquisition, and closes the specified session.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxconfigureacquisition.html language=enus -->
## TOPIC 00006: IMAQdxConfigureAcquisition

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxconfigureacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxconfigureacquisition.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxConfigureAcquisition

#### Format

rval = IMAQdxConfigureAcquisition (IMAQdxSession id, unsigned int continuous, unsigned int bufferCount)

#### Purpose

Configures a low-level acquisition previously opened with [IMAQdxOpenCamera](imaqdxopencamera.html). Specify the acquisition type using the **continuous** and **bufferCount** parameters.

| Snap | Continuous = 0 | Buffer Count = 1 |
| --- | --- | --- |
| Sequence | Continuous = 0 | Buffer Count > 1 |
| Grab | Continuous = 1 | Buffer Count ³ 1 |

Use [IMAQdxUnconfigureAcquisition](imaqdxunconfigureacquisition.html) to unconfigure the acquisition.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| continuous | unsigned int | Specifies whether the acquisition is continuous or one-shot. |
| bufferCount | unsigned int | For a one-shot acquisition, this parameter specifies the number of images to acquire. For a continuous acquisition, this parameter specifies the number of buffers the driver uses internally. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxconfiguregrab.html language=enus -->
## TOPIC 00007: IMAQdxConfigureGrab

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxconfiguregrab.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxconfiguregrab.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxConfigureGrab

#### Format

rval = IMAQdxConfigureGrab (IMAQdxSession id);

#### Purpose

Configures and starts an acquisition. A grab performs an acquisition that loops continually on a ring of buffers. Use a grab for high-speed image acquisition. Use [IMAQdxGrab](imaqdxgrab.html) to copy an image out of the buffer. If you call this function before calling [IMAQdxOpenCamera](imaqdxopencamera.html), IMAQdxConfigureGrab uses cam0 by default. Use [IMAQdxUnconfigureAcquisition](imaqdxunconfigureacquisition.html) to unconfigure the acquisition.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxdiscoverethernetcameras.html language=enus -->
## TOPIC 00008: IMAQdxDiscoverEthernetCameras

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxdiscoverethernetcameras.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxdiscoverethernetcameras.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxDiscoverEthernetCameras

#### Format

rval = IMAQdxDiscoverEthernetCameras (const char *address, unsigned int timeout);

#### Purpose

Detects Ethernet cameras on a network. Use this function to detect Ethernet cameras on a network with a remote subnet. During discovery, this function is blocked and returns after the specified timeout. The address specifies the destination address for the discovery command. The default address is 255.255.255.255. Call this function before calling [IMAQdxEnumerateCameras](imaqdxenumeratecameras.html) or [IMAQdxOpenCamera](imaqdxopencamera.html).

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| address | const char * | Address specifies the destination address for the discovery command. The default address is 255.255.255.255. |
| timeout | unsigned int | Timeout specifies the time, in milliseconds, allowed for the Ethernet camera discovery to complete. The default timeout is 1000 ms. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumerateattributes2.html language=enus -->
## TOPIC 00009: IMAQdxEnumerateAttributes2

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumerateattributes2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumerateattributes2.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateAttributes2

#### Format

rval = IMAQdxEnumerateAttributes2 (IMAQdxSession id, IMAQdxAttributeInformation attributeInformationArray[], unsigned int *count, const char *root, IMAQdxAttributeVisibility visibility)

#### Purpose

Gets the attributes supported by the camera. If you do not know in advance the number of features, complete the following steps:

1. Call this function with the attributeInformationArray parameter set to NULL. The necessary size is then stored in count .
2. Allocate attributeInformationArray with the given size.
3. Call this function again using the previously allocated array.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| attributeInformationArray | IMAQdxAttributeInformationArray [] | Contains a pointer to an array of attribute information structures in which the attributes supported by the camera are stored. Set this parameter to NULL to get the size needed by the array in the count parameter. |
| count | unsigned int (passed by reference) | Contains the size of the array used to store the attributes. If the user passes NULL as the attributeInformationArray parameter, this parameter contains the needed size. |
| root | const char * | Specifies the branch of the attribute tree to enumerate. Specify an empty string to enumerate the entire attribute tree. |
| visibility | IMAQdxAttributeVisibility | Specifies the visibility of the attribute to enumerate. Only attributes with the specified visibility will be returned. Available options are the same as IMAQdxGetAttributeVisibility. Specify IMAQdxAttributeVisibilityAdvanced to return all the visible attributes. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumerateattributes2cw.html language=enus -->
## TOPIC 00010: IMAQdxEnumerateAttributes2CW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumerateattributes2cw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumerateattributes2cw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateAttributes2CW

#### Format

IMAQdxEnumerateAttributes2CW(id As IMAQdxSession, attributeInformationArray() As IMAQdxAttributeInformation, root As String, visibility As IMAQdxAttributeVisibility) As IMAQdxError

#### Purpose

Gets the attributes supported by the camera.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| attributeInformationArray | IMAQdxAttributeInformationArray [] | Contains a pointer to an array of attribute information structures in which the attributes supported by the camera are stored. |
| root | String | Specifies the branch of the attribute tree to enumerate. Specify an empty string to enumerate the entire attribute tree. |
| visibility | IMAQdxAttributeVisibility | Specifies the visibility of the attribute to enumerate. Only attributes with the specified visibility will be returned. Available options are the same as IMAQdxGetAttributeVisibility. Specify IMAQdxAttributeVisibilityAdvanced to return all the visible attributes. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumerateattributevalues.html language=enus -->
## TOPIC 00011: IMAQdxEnumerateAttributeValues

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumerateattributevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumerateattributevalues.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateAttributeValues

#### Format

rval = IMAQdxEnumerateAttributeValues(IMAQdxSession id, const char *name, IMAQdxEnumItem list [], unsigned int *size);

#### Purpose

Gets the values supported by the camera attribute.

|  | Note This function applies only to attributes of type IMAQdxAttributeTypeEnum. Use IMAQdxGetAttributeType to get your attribute type. |
| --- | --- |

If you do not know in advance the number of attribute values, complete the following steps:

1. Call this function with the list parameter set to NULL. The necessary size is then stored in size .
2. Allocate list with the given size.
3. Call this function again using the previously allocated array.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | cont char * | The name of the attribute whose values you want to enumerate. Refer to Attribute Name for a list of attributes. |
| list | IMAQdxEnumItem [] | The list of attribute values for the attribute specified by name. Set this parameter to NULL to get the size needed by the array in the size parameter. |
| size | unsigned int (passed by reference) | The size of attribute values for the attribute specified by name. If the user passes NULL as the list parameter, this parameter contains the needed size. |

#### Parameter Discussion

**name** specifies the attribute name whose value you want to obtain. In the LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumerateattributevaluescw.html language=enus -->
## TOPIC 00012: IMAQdxEnumerateAttributeValuesCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumerateattributevaluescw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumerateattributevaluescw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateAttributeValuesCW

#### Format

IMAQdxEnumerateAttributeValuesCW (id As IMAQdxSession, name As String, enumItemArray() As IMAQdxEnumItem) As IMAQdxError

#### Purpose

Gets the values supported by the camera attribute.

|  | Note This function applies only to attributes of type IMAQdxAttributeTypeEnum. Use IMAQdxGetAttributeType to get your attribute type. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose values you want to enumerate. Refer to Attribute Name for a list of attributes. |
| enumItemArray | IMAQdxEnumItem [] | The list of attribute values for the attribute specified by name. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumeratecameras.html language=enus -->
## TOPIC 00013: IMAQdxEnumerateCameras

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumeratecameras.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumeratecameras.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateCameras

#### Format

rval = IMAQdxEnumerateCameras (IMAQdxCameraInformation cameraInformationArray[], unsigned int *count, unsigned int connectedOnly);

#### Purpose

Returns a list of all cameras on the host computer. If you do not know in advance the number of cameras, complete the following steps:

1. Call this function with the cameraInformationArray parameter set to NULL. The necessary size is then stored in count .
2. Allocate cameraInformationArray with the given size.
3. Call this function again using the previously allocated array.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| cameraInformationArray | IMAQdxCameraInformation [] | An array of IMAQdxCameraInformation structure elements in which the interfaces supported by the system are stored. Set this parameter to NULL to get the size needed by the array in the count parameter. |
| count | unsigned int (passed by reference) | The size of the array used to store the camera information. If the user passes NULL as the cameraInformationArray parameter, this parameter contains the needed size. |
| connectedOnly | unsigned int | If the connectedOnly value is true, then the cameraInformationArray only contains cameras that are currently connected to the host computer. If the connectedOnly value is false, then the cameraInformationArray contains cameras that are currently connected, and were previously connected, to the host computer. |

#### Parameter Discussion

The IMAQdxCameraInformation structure contains information about currently and previously connected interfaces. Once enumerated, check the Flags member of the **IMAQdxCameraInformation** structure. If the value of Flags is 0, the camera is not currently connected. If the value of Flags is 1, the camera is currently connected.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumeratecamerascw.html language=enus -->
## TOPIC 00014: IMAQdxEnumerateCamerasCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumeratecamerascw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumeratecamerascw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateCamerasCW

#### Format

IMAQdxEnumerateCamerasCW (cameraInformationArray() As IMAQdxCameraInformation, connectedOnly As VARIANT_BOOL) As IMAQdxError

#### Purpose

Returns a list of all cameras on the host computer.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| cameraInformationArray | IMAQdxCameraInformation [] | An array of IMAQdxCameraInformation structure elements in which the interfaces supported by the system are stored. |
| connectedOnly | VARIANT_BOOL | If the connectedOnly value is true, then the cameraInformationArray only contains cameras that are currently connected to the host computer. If the connectedOnly value is false, then the cameraInformationArray contains cameras that are currently connected, and were previously connected, to the host computer. |

#### Parameter Discussion

The IMAQdxCameraInformation structure contains information about currently and previously connected interfaces. Once enumerated, check the Flags member of the **IMAQdxCameraInformation** structure. If the value of Flags is 0, the camera is not currently connected. If the value of Flags is 1, the camera is currently connected.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumeratevideomodes.html language=enus -->
## TOPIC 00015: IMAQdxEnumerateVideoModes

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumeratevideomodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumeratevideomodes.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateVideoModes

#### Format

rval = IMAQdxEnumerateVideoModes (IMAQdxSession id, IMAQdxVideoMode videoModeArray[], unsigned int *count, unsigned int *currentMode);

#### Purpose

Returns a list of video modes supported by the camera.

|  | Note This function applies only to cameras of bus type IMAQdxBusTypeFireWire. Use IMAQdxGetAttribute with attribute IMAQdxAttributeBusType to get your bus type. |
| --- | --- |

If the number of video modes is not known in advance, complete the following steps:

1. Call this function with the videoModeArray parameter set to NULL. The necessary size is then stored in videoModeArraySize .
2. Allocate the videoModeArray with the given size.
3. Call this function again using with the previously allocated array.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| videoModeArray | IMAQdxVideoMode [] | Contains an array of video modes supported by the current camera. Set this parameter to NULL to get the size needed by the array in the count parameter. |
| count | unsigned int (passed by reference) | The size of the array used to store the video modes. If the user passes NULL as the videoModeArray parameter, this parameter then contains the needed size. |
| currentMode | unsigned int (passed by reference) | The index into the videoModeArray of the current mode used by the camera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxenumeratevideomodescw.html language=enus -->
## TOPIC 00016: IMAQdxEnumerateVideoModesCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxenumeratevideomodescw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxenumeratevideomodescw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxEnumerateVideoModesCW

#### Format

IMAQdxEnumerateVideoModesCW(id As IMAQdxSession, videoModeArray() As IMAQdxVideoMode, currentMode As Long) As IMAQdxError

#### Purpose

Returns a list of video modes supported by the camera.

|  | Note This function applies only to cameras of bus type IMAQdxBusTypeFireWire. Use IMAQdxGetAttributeCW with attribute IMAQdxAttributeBusType to get your bus type. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| videoModeArray | IMAQdxVideoModeArray[] | Contains an array of video modes supported by the current camera. |
| currentMode | Long (passed by reference) | The index of the current mode used by the camera in videoModeArray. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattribute.html language=enus -->
## TOPIC 00017: IMAQdxGetAttribute

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattribute.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttribute

#### Format

rval = IMAQdxGetAttribute(IMAQdxSession id, char *name, IMAQdxValueType type, void *value);

#### Purpose

Gets the current value for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | char * | The name of the attribute whose value you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | void * (passed by reference) | The value of the specified attribute when the function returns. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, IMAQdxValueTypeF64, IMAQdxValueTypeString, IMAQdxValueTypeEnumItem, and IMAQdxValueTypeBool.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributecw.html language=enus -->
## TOPIC 00018: IMAQdxGetAttributeCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeCW

#### Format

IMAQdxGetAttributeCW (id As IMAQdxSession, name As String, type As IMAQdxValueType, value As VARIANT) As IMAQdxError

#### Purpose

Gets the current value for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose value you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | VARIANT (passed by reference) | The value of the specified attributes when the function returns. |

#### Parameter Discussion

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, IMAQdxValueTypeF64, IMAQdxValueTypeString, IMAQdxValueTypeEnumItem, and IMAQdxValueTypeBool.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributedescription.html language=enus -->
## TOPIC 00019: IMAQdxGetAttributeDescription

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributedescription.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributedescription.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeDescription

#### Format

rval = IMAQdxGetAttributeDescription(IMAQdxSession id, const char *name, char *description, unsigned int length)

#### Purpose

Gets the description for the camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute for which you want to get the description. Refer to Attribute Name for a list of attributes. |
| description | char * | A pointer to an area of memory reserved for a tooltip. The reserved memory must be at least the size specified by the length parameter. |
| length | unsigned int | The maximum length of the C string passed as the description parameter. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In the LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributedescriptioncw.html language=enus -->
## TOPIC 00020: IMAQdxGetAttributeDescriptionCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributedescriptioncw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributedescriptioncw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeDescriptionCW

#### Format

IMAQdxGetAttributeDescriptionCW (id As IMAQdxSession, name As String, description As String) As IMAQdxError

#### Purpose

Gets the description for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose description you want to get. Refer to Attribute Name for a list of attributes. |
| description | String (passed by reference) | The description of the specified attributes when the function returns. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributedisplayname.html language=enus -->
## TOPIC 00021: IMAQdxGetAttributeDisplayName

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributedisplayname.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributedisplayname.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeDisplayName

#### Format

rval = IMAQdxGetAttributeDisplayName(IMAQdxSession id, const char *name, char *displayName, unsigned int length)

#### Purpose

Gets the display name for the camera attribute. The display name is a human readable version of the attribute name.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose tooltip you want to get. Refer to Attribute Name for a list of attributes. |
| display name | char * | A pointer to an area of memory reserved for a display name. The reserved memory must be at least the size specified by the length parameter. |
| length | unsigned int | The maximum length of the C string passed as the display name parameter. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributedisplaynamecw.html language=enus -->
## TOPIC 00022: IMAQdxGetAttributeDisplayNameCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributedisplaynamecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributedisplaynamecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeDisplayNameCW

#### Format

IMAQdxGetAttributeDisplayNameCW (id As IMAQdxSession, name As String, displayName As String) As IMAQdxError

#### Purpose

Gets the display name for the camera attribute. The display name is a human readable version of the attribute name.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose display name you want to get. Refer to Attribute Name for a list of attributes. |
| displayName | String (passed by reference) | The display name of the specified attributes when the function returns. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeincrement.html language=enus -->
## TOPIC 00023: IMAQdxGetAttributeIncrement

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeincrement.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeincrement.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeIncrement

#### Format

rval = IMAQdxGetAttributeIncrement(IMAQdxSession id, char *name, IMAQdxValueType type, void *value);

#### Purpose

Gets the increment for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | char * | The name of the attribute whose increment you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | void * (passed by reference) | The increment of the specified attribute when the function returns. |

#### Parameter Discussion

**name** specifies the attribute whose increment you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeincrementcw.html language=enus -->
## TOPIC 00024: IMAQdxGetAttributeIncrementCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeincrementcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeincrementcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeIncrementCW

#### Format

IMAQdxGetAttributeIncrementCW (id As IMAQdxSession, name As String, type As IMAQdxValueType, value As VARIANT) As IMAQdxError

#### Purpose

Gets the increment for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose increment you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | VARIANT (passed by reference) | The increment of the specified attributes when the function returns. |

#### Parameter Discussion

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributemaximum.html language=enus -->
## TOPIC 00025: IMAQdxGetAttributeMaximum

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributemaximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributemaximum.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeMaximum

#### Format

rval = IMAQdxGetAttributeMaximum(IMAQdxSession id, char *name, IMAQdxValueType type, void *value);

#### Purpose

Gets the maximum for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | char * | The name of the attribute whose maximum you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | void * (passed by reference) | The maximum of the specified attribute when the function returns. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributemaximumcw.html language=enus -->
## TOPIC 00026: IMAQdxGetAttributeMaximumCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributemaximumcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributemaximumcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeMaximumCW

#### Format

IMAQdxGetAttributeMaximumCW (id As IMAQdxSession, name As String, type As IMAQdxValueType, value As VARIANT) As IMAQdxError

#### Purpose

Gets the maximum for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose maximum you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | VARIANT (passed by reference) | The maximum of the specified attributes when the function returns. |

#### Parameter Discussion

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeminimum.html language=enus -->
## TOPIC 00027: IMAQdxGetAttributeMinimum

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeminimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeminimum.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeMinimum

#### Format

rval = IMAQdxGetAttributeMinimum(IMAQdxSession id, const char *name, IMAQdxValueType type, void *value);

#### Purpose

Gets the minimum for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose minimum you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | void * (passed by reference) | The minimum of the specified attribute when the function returns. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeminimumcw.html language=enus -->
## TOPIC 00028: IMAQdxGetAttributeMinimumCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeminimumcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeminimumcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeMinimumCW

#### Format

IMAQdxGetAttributeMinimumCW (id As IMAQdxSession, name As String, type As IMAQdxValueType, value As VARIANT) As IMAQdxError

#### Purpose

Gets the minimum for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose minimum you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the value you want to get. |
| value | VARIANT (passed by reference) | The minimum of the specified attributes when the function returns. |

#### Parameter Discussion

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, and IMAQdxValueTypeF64.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributetooltip.html language=enus -->
## TOPIC 00029: IMAQdxGetAttributeTooltip

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributetooltip.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributetooltip.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeTooltip

#### Format

rval = IMAQdxGetAttributeTooltip(IMAQdxSession id, const char *name, char *tooltip, unsigned int length);

#### Purpose

Gets the tooltip for the camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose tooltip you want to get. Refer to Attribute Name for a list of attributes. |
| tooltip | char * | A pointer to an area of memory reserved for a tooltip. The reserved memory must be at least the size specified by the length parameter. |
| length | unsigned int | The maximum length of the C string passed as the tooltip parameter. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributetooltipcw.html language=enus -->
## TOPIC 00030: IMAQdxGetAttributeTooltipCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributetooltipcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributetooltipcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeTooltipCW

#### Format

IMAQdxGetAttributeTooltipCW (id As IMAQdxSession, name As String, tooltip As String) As IMAQdxError

#### Purpose

Gets the tooltip for the camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose tooltip you want to get. Refer to Attribute Name for a list of attributes. |
| tooltip | String (passed by reference) | The tooltip of the specified attributes when the function returns. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributetype.html language=enus -->
## TOPIC 00031: IMAQdxGetAttributeType

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributetype.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeType

#### Format

rval = IMAQdxGetAttributeType (IMAQdxSession id, const char *name, IMAQdxAttributeType *type);

#### Purpose

Gets the attribute type for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose value you want to get. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxAttributeType (passed by reference) | The type of the attribute whose value you want to get. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, IMAQdxValueTypeF64, IMAQdxValueTypeString, IMAQdxValueTypeEnumItem, and IMAQdxValueTypeBool.

|  | Note The value type must be compatible with the attribute type. Refer to the NI-IMAQdx Help for more information about camera attributes. |
| --- | --- |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeunits.html language=enus -->
## TOPIC 00032: IMAQdxGetAttributeUnits

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeunits.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeUnits

#### Format

rval = IMAQdxGetAttributeUnits (IMAQdxSession id, const char *name, char *units, unsigned int length);

#### Purpose

Gets the attribute units for a camera.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose units you want to get. Refer to Attribute Name for a list of attributes. |
| units | char * | A pointer to an area of memory reserved for an error string. The reserved memory must be at least the size specified by the length parameter. |
| length | unsigned int | The maximum length of the C string passed as the units parameter. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributeunitscw.html language=enus -->
## TOPIC 00033: IMAQdxGetAttributeUnitsCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributeunitscw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributeunitscw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeUnitsCW

#### Format

IMAQdxGetAttributeUnitsCW (id As IMAQdxSession, name As String, unit As String) As IMAQdxError

#### Purpose

Gets the attribute units for a camera.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute whose units you want to get. Refer to Attribute Name for a list of attributes. |
| units | String (passed by reference) | The units of the specified attributes when the function returns. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributevisibility.html language=enus -->
## TOPIC 00034: IMAQdxGetAttributeVisibility

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributevisibility.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributevisibility.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeVisibility

#### Format

rval = IMAQdxGetAttributeVisibility(IMAQdxSession id, const char *name, IMAQdxAttributeVisibility* visibility)

#### Purpose

Gets the visibility for the camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose visibility you want to get. Refer to Attribute Name for a list of attributes. |
| visibility | IMAQdxAttributeVisibility (passed by reference) | On return contains the visibility for the current attribute. Choose from one of the following options: IMAQdxAttributeVisibilitySimple IMAQdxAttributeVisibilityIntermediate IMAQdxAttributeVisibilityAdvanced |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetattributevisibilitycw.html language=enus -->
## TOPIC 00035: IMAQdxGetAttributeVisibility

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetattributevisibilitycw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetattributevisibilitycw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetAttributeVisibility

#### Format

rval = IMAQdxGetAttributeVisibility(IMAQdxSession id, const char *name, IMAQdxAttributeVisibility* visibility)

#### Purpose

Gets the visibility for the camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute whose visibility you want to get. Refer to Attribute Name for a list of attributes. |
| visibility | IMAQdxAttributeVisibility (passed by reference) | On return contains the visibility for the current attribute. Choose from one of the following options:: IMAQdxAttributeVisibilitySimple IMAQdxAttributeVisibilityIntermediate IMAQdxAttributeVisibilityAdvanced |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgeterrorstring.html language=enus -->
## TOPIC 00036: IMAQdxGetErrorString

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgeterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgeterrorstring.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetErrorString

#### Format

rval = IMAQdxGetErrorString (IMAQdxError error, char *message, unsigned int messageLength);

#### Purpose

Returns a string describing the error code.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| error | IMAQdxError | A valid NI-IMAQdx error code. Refer to the Error Codes topic in this help file for a complete error code list. |
| message | char * | A pointer to an area of memory reserved for an error string. The reserved memory must be at least the size specified by the messageLength parameter. |
| messageLength | unsigned int | The maximum length of the C string passed as the message parameter. |

#### Return Value

Refer to [Error Codes](error_codes.html) for a complete error code list.

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgeterrorstringcw.html language=enus -->
## TOPIC 00037: IMAQdxGetErrorStringCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgeterrorstringcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgeterrorstringcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetErrorStringCW

#### Format

IMAQdxGetErrorStringCW (errorCode As IMAQdxError, errorMessage As String) As IMAQdxError

#### Purpose

Returns a string describing the error code.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| errorCode | IMAQdxError | A valid NI-IMAQdx error code. Refer to Error Codes for a complete error code list. |
| errorMessage | String | The string describing the error that occurred. |

#### Return Value

Refer to [Error Codes](error_codes.html) for a complete error code list.

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetimage.html language=enus -->
## TOPIC 00038: IMAQdxGetImage

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetimage.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetimage.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetImage

#### Format

rval = IMAQdxGetImage (IMAQdxSession id, Image *image, IMAQdxBufferNumberMode mode, unsigned int desiredBufferNumber, unsigned int *actualBufferNumber);

#### Purpose

Acquires the specified frame into **image**. Call this function only after calling [IMAQdxConfigureAcquisition](imaqdxconfigureacquisition.html). If the image type does not match the video format of the camera, the function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| image | Image * | The image that receives the captured pixel data. |
| mode | IMAQdxBufferNumberMode | The buffer number mode of the image to retrieve. Set this parameter to IMAQdxBufferNumberModeNext to get the next buffer, or set this parameter to IMAQdxBufferNumberLast to get the last acquired buffer, or set this parameter IMAQdxBufferNumberModeBufferNumber to acquire a specific cumulative buffer number. |
| desiredBufferNumber | unsigned int | The cumulative buffer number of the image to retrieve. This parameter is only needed if mode is set to IMAQdxBufferNumberModeBufferNumber. |
| actualBufferNumber | unsigned int (passed by reference) | On return, the actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetimagecw.html language=enus -->
## TOPIC 00039: IMAQdxGetImageCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetimagecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetimagecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetImageCW

#### Format

IMAQdxGetImageCW (id As IMAQdxSession, image As CWIMAQImage, mode as IMAQdxBufferNumberMode, desiredBufferNumber As Long, actualBufferNumber As Long) As IMAQdxError

#### Purpose

Acquires the specified frame into **image**. If the image type does not match the video format of the camera, the function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain with the function IMAQdxOpenCamera. |
| image | CWIMAQImage | The image that receives the captured pixel data. |
| mode | IMAQdxBufferNumberMode | The buffer number mode of the image to retrieve. Set this parameter to IMAQdxBufferNumberModeNext to get the next buffer, or set this parameter to IMAQdxBufferNumberLast to get the last acquired buffer, or set this parameter IMAQdxBufferNumberModeBufferNumber to acquire a specific cumulative buffer number. |
| desiredBufferNumber | Long | The cumulative buffer number of the image to retrieve. This parameter is only needed if mode is set to IMAQdxBufferNumberModeBufferNumber. |
| actualBufferNumber | Long (passed by reference) | The actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetimagedata.html language=enus -->
## TOPIC 00040: IMAQdxGetImageData

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetimagedata.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetimagedata.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetImageData

#### Format

rval = IMAQdxGetImageData (IMAQdxSession id, void *buffer, unsigned int bufferSize, IMAQdxBufferNumberMode mode, unsigned int desiredBufferNumber, unsigned int *actualBufferNumber);

#### Purpose

Copies the raw data of the specified frame into **buffer**. Call this function only after calling [IMAQdxConfigureAcquisition](imaqdxconfigureacquisition.html).

|  | Note This function allows you to access raw image data. For many uncompressed formats like YUV or RGB, buffer is not compatible with NI Vision. To use the NI Vision functions, use IMAQdxGetImage instead of this function. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| buffer | void * | The buffer that contains the raw data for the image when the function returns. |
| bufferSize | unsigned int | The maximum size of the buffer. |
| mode | IMAQdxBufferNumberMode | The buffer number mode of the image to retrieve. Set this parameter to IMAQdxBufferNumberModeNext to get the next buffer, or set this parameter to IMAQdxBufferNumberLast to get the last acquired buffer, or set this parameter IMAQdxBufferNumberModeBufferNumber to acquire a specific cumulative buffer number. |
| desiredBufferNumber | unsigned int | The cumulative buffer number of the image to retrieve. This parameter is only needed if mode is set to IMAQdxBufferNumberModeBufferNumber. |
| actualBufferNumber | unsigned int (passed by reference) | On return, the actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgetimagedatacw.html language=enus -->
## TOPIC 00041: IMAQdxGetImageDataCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgetimagedatacw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgetimagedatacw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGetImageDataCW

#### Format

rval = IMAQdxGetImageDataCW (id As IMAQdxSession, buffer As VARIANT, mode As IMAQdxBufferNumberMode, desiredBufferNumber As Long, actualBufferNumber As Long);

#### Purpose

Copies the raw data of the specified frame into **buffer**.

|  | Note This function allows you to access raw image data. For many uncompressed formats like YUV or RGB, buffer is not compatible with NI Vision. To use the NI Vision functions, use IMAQdxGetImage instead of this function. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| buffer | VARIANT * | The data of the specified attributes when the function returns. |
| mode | IMAQdxBufferNumberMode | The buffer number mode of the image to retrieve. Set this parameter to IMAQdxBufferNumberModeNext to get the next buffer, or set this parameter to IMAQdxBufferNumberLast to get the last acquired buffer, or set this parameter IMAQdxBufferNumberModeBufferNumber to acquire a specific cumulative buffer number. |
| desiredBufferNumber | Long | The cumulative buffer number of the image to retrieve. This parameter is only needed if mode is set to IMAQdxBufferNumberModeBufferNumber. |
| actualBufferNumber | Long (passed by reference) | On return, the actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgrab.html language=enus -->
## TOPIC 00042: IMAQdxGrab

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgrab.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgrab.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGrab

#### Format

rval = IMAQdxGrab (IMAQdxSession id, Image *image, unsigned int waitForNextBuffer, unsigned int *actualBufferNumber);

#### Purpose

Acquires the most current frame into **image**. Call this function only after calling [IMAQdxConfigureGrab](imaqdxconfiguregrab.html). If the image type does not match the video format of the camera, this function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| image | Image * | The image that receives the captured pixel data. |
| waitForNextBuffer | unsigned int | If the waitForNextBuffer value is true, the driver will wait for the next available buffer. If the waitForNextBuffer value is false, the driver will not wait for the next available buffer, and will instead return the last acquired buffer. |
| actualBufferNumber | unsigned int (passed by reference) | On return, the actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxgrabcw.html language=enus -->
## TOPIC 00043: IMAQdxGrabCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxgrabcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxgrabcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxGrabCW

#### Format

IMAQdxGrabCW(id As IMAQdxSession, image As CWIMAQImage, waitForNextBuffer As Long, actualBufferNumber As Long) As IMAQdxError

#### Purpose

Acquires the most current frame into **image**. Call this function only after calling [IMAQdxConfigureGrab](imaqdxconfiguregrab.html). If the image type does not match the video format of the camera, this function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| image | CWIMAQImage | The image that receives the captured pixel data. |
| waitForNextBuffer | Long | If the waitForNextBuffer value is true, the driver will wait for the next available buffer. If the waitForNextBuffer value is false, the driver will not wait for the next available buffer, and will instead return the last acquired buffer. |
| actualBufferNumber | Long (passed by reference) | On return, the actual cumulative buffer number of the image retrieved. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxisattributereadable.html language=enus -->
## TOPIC 00044: IMAQdxIsAttributeReadable

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxisattributereadable.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxisattributereadable.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxIsAttributeReadable

#### Format

rval = IMAQdxIsAttributeReadable (IMAQdxSession id, const char *name, unsigned int *readable);

#### Purpose

Gets the read permissions for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the camera attribute whose read permission you want to get. Refer to Attribute Name for a list of attributes. |
| readable | unsigned int (passed by reference) | Returns true if the attribute is readable, otherwise false. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxisattributereadablecw.html language=enus -->
## TOPIC 00045: IMAQdxIsAttributeReadableCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxisattributereadablecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxisattributereadablecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxIsAttributeReadableCW

#### Format

IMAQdxIsAttributeReadableCW (id As IMAQdxSession, name As String, readable as VARIANT_BOOL) As IMAQdxError

#### Purpose

Gets the read permissions for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the camera attribute whose read permission you want to get. Refer to Attribute Name for a list of attributes. |
| readable | VARIANT_BOOL (passed by reference) | Returns true if the attribute is readable, otherwise false. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxisattributewritable.html language=enus -->
## TOPIC 00046: IMAQdxIsAttributeWritable

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxisattributewritable.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxisattributewritable.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxIsAttributeWritable

#### Format

rval = IMAQdxIsAttributeWritable (IMAQdxSession id, const char *name, unsigned int *writable);

#### Purpose

Gets the write permissions for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the camera attribute whose write permission you want to get. Refer to Attribute Name for a list of attributes. |
| writable | unsigned int (passed by reference) | Returns true if the attribute is writable, otherwise false. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxisattributewritablecw.html language=enus -->
## TOPIC 00047: IMAQdxIsAttributeWritableCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxisattributewritablecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxisattributewritablecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxIsAttributeWritableCW

#### Format

IMAQdxIsAttributeWritableCW (id As IMAQdxSession, name As String, writable as VARIANT_BOOL) As IMAQdxError

#### Purpose

Gets the write permissions for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the camera attribute whose write permission you want to get. Refer to Attribute Name for a list of attributes. |
| writable | VARIANT_BOOL (passed by reference) | Returns true if the attribute is writable, otherwise false. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxopencamera.html language=enus -->
## TOPIC 00048: IMAQdxOpenCamera

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxopencamera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxopencamera.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxOpenCamera

#### Format

rval = IMAQdxOpenCamera (const char *name, IMAQdxCameraControlMode mode, IMAQdxSession *id);

#### Purpose

Opens a camera, queries the camera for its capabilities, loads a camera configuration file, and creates a unique reference to the camera. Use [IMAQdxCloseCamera](imaqdxclosecamera.html) when you are finished with the reference.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| name | const char * | The name of the camera you want to open. name (cam0, cam1, ..., camN) must match the configuration file name you used to configure the camera in MAX. You can also open a camera using its 64-bit serial number (uuid:XXXXXXXXXXXXXXXX), where the number following uuid must be a 64-bit hexadecimal number representing the internal serial number of the camera. Note Specify " uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |
|  | Note Specify " uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |  |
| mode | IMAQdxCameraControlMode | Camera Control Mode is the control mode of the camera used during image broadcasting. Open a camera in controller mode to actively configure and acquire image data. Open a camera in listener mode to passively acquire image data from a session that was opened in controller mode on a different host or target computer. The default value is Controller. |
| id | IMAQdxSession (passed by reference) | On return, a valid Session ID. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxreadattributes.html language=enus -->
## TOPIC 00049: IMAQdxReadAttributes

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxreadattributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxreadattributes.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxReadAttributes

#### Format

rval = IMAQdxReadAttributes (IMAQdxSession id, const char* filename)

#### Purpose

Reads attributes from file and applies to current session. This function is only required if you wish to load parameters. By default the attributes are loaded from file when the camera is opened.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| Filename | const char* | The filename to load the attributes from. Specify NULL to load from the default camera file. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxreadmemory.html language=enus -->
## TOPIC 00050: IMAQdxReadMemory

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxreadmemory.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxreadmemory.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxReadMemory

#### Format

rval = IMAQdxReadMemory (IMAQdxSession id, unsigned int offset, const char *values, unsigned int count);

#### Purpose

Accesses registers on the camera and reads a string from the camera.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| offset | unsigned int | The register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use attribute IMAQdxAttributeBaseAddress to obtain the base address for the camera. |
| values | const char * | Specifies the string read from the memory offset. |
| count | unsigned int | Specifies the maximum length of the string read from the memory offset. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxreadregister.html language=enus -->
## TOPIC 00051: IMAQdxReadRegister

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxreadregister.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxreadregister.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxReadRegister

#### Format

rval = IMAQdxReadRegister (IMAQdxSession id, unsigned int offset, unsigned int *value);

#### Purpose

Accesses registers on the camera and reads a 32-bit value from the camera. Data is byte-swapped for little endian alignment after transfer.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| offset | unsigned int | The register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use attribute IMAQdxAttributeBaseAddress to obtain the base address for the camera. |
| value | unsigned int (passed by reference) | Specifies the value to read from the memory offset. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxregisterframedoneevent.html language=enus -->
## TOPIC 00052: IMAQdxRegisterFrameDoneEvent

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxregisterframedoneevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxregisterframedoneevent.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxRegisterFrameDoneEvent

#### Format

rval = IMAQdxRegisterFrameDoneEvent (IMAQdxSession id, unsigned int bufferInterval, FrameDoneEventCallbackPtr callbackFunction, void *callbackData);

#### Purpose

Configures the NI-IMAQdx driver to execute a callback function when a frame done event occurs.

|  | Note Make sure that the code inside the callback is thread safe since the callback executes in a different thread. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| bufferInterval | unsigned int | The number of images to acquire before executing the callback function. Specify a buffer interval of 1 to receive a callback for every buffer. |
| callbackFunction | FrameDoneEventCallbackPtr | The address of the callback function. |
| callbackData | void * | A pointer to user-defined data passed to the event function. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxregisteriosignaledgeevent.html language=enus -->
## TOPIC 00053: IMAQdxRegisterIOSignalEdgeEvent

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxregisteriosignaledgeevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxregisteriosignaledgeevent.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxRegisterIOSignalEdgeEvent

#### Format

rval = IMAQdxRegisterIOSignalEdgeEvent(IMAQdxSession id, IMAQdxIOSignalType signalType, uInt32 signalNumber, IMAQdxEdge signalEdge, IOSignalEdgeEventCallbackPtr callbackFunction, void* callbackData);

#### Purpose

Registers an asynchronous event handler for detecting an edge on an IO signal.

|  | Note Make sure that the code inside the callback is thread safe since the callback executes in a different thread. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| signalType | IMAQdxIOSignalType | The IO signal type to wait for. Choose from one of the following options: IMAQdxIOSignalTypeTTL IMAQdxIOSignalTypeRTSI IMAQdxIOSignalTypeIsoIn IMAQdxIOSignalTypeIsoOut |
| signalNumber | uInt32 | The line number of the IO signal type to wait for. |
| signalEdge | IMAQdxEdge | The edge of the IO signal to wait for. Choose from one of the following options: IMAQdxEdgeRising IMAQdxEdgeFalling |
| callbackFunction | IOSignalEdgeEventCallbackPtr | The address of the callback function. |
| callbackData | void* | A pointer to user-defined data passed to the event function. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxregisterpnpevent.html language=enus -->
## TOPIC 00054: IMAQdxRegisterPnpEvent

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxregisterpnpevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxregisterpnpevent.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxRegisterPnpEvent

#### Format

rval = IMAQdxRegisterPnpEvent (IMAQdxSession id, IMAQdxPnpEvent event, PnpEventCallbackPtr callbackFunction, void *callbackData);

#### Purpose

Configures the NI-IMAQdx driver to execute a callback function when a plug and play event occurs.

|  | Note Make sure that the code inside the callback is thread safe since the callback executes in a different thread. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| event | IMAQdxPnpEvent | The plug and play event to monitor. The following events are valid: IMAQdxPnpEventCameraAttached: Callback fired when a new camera is attached. IMAQdxPnpEventCameraDetached: Callback fired when the camera is detached. IMAQdxPnpEventBusReset: Callback fired when a FireWire bus reset occurs. |
| callbackFunction | PnpEventCallbackPtr | The address of the callback function. |
| callback Data | void * | A pointer to user-defined data passed to the event function. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxregisterstatussignalevent.html language=enus -->
## TOPIC 00055: IMAQdxRegisterStatusSignalEvent

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxregisterstatussignalevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxregisterstatussignalevent.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxRegisterStatusSignalEvent

#### Format

rval = IMAQdxRegisterStatusSignalEvent(IMAQdxSession id, IMAQdxStatusSignalType statusSignalType, StatusSignalEventCallbackPtr callbackFunction, void* callbackData);

#### Purpose

Registers asynchronous event handler for detecting an edge on an IO signal.

|  | Note Make sure that the code inside the callback is thread safe since the callback executes in a different thread. |
| --- | --- |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| statusSignalType | IMAQdxStatusSignalType | The status signal to wait for. Choose from one of the following options: IMAQdxStatusSignalTypeAcquisitionActive IMAQdxStatusSignalTypeAcquisitionDone IMAQdxStatusSignalTypeFrameStart IMAQdxStatusSignalTypeFrameDone IMAQdxStatusSignalTypeBufferComplete |
| callbackFunction | StatusSignalEventCallbackPtr | The address of the callback function. |
| callbackData | void* | A pointer to user-defined data passed to the event function. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxresetcamera.html language=enus -->
## TOPIC 00056: IMAQdxResetCamera

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxresetcamera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxresetcamera.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxResetCamera

#### Format

rval = IMAQdxResetCamera (const char *name, unsigned int resetALL);

#### Purpose

Performs a manual reset on a camera. Stops any ongoing acquisitions.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| name | const char * | The name of the camera you want to open. name (cam0, cam1, ..., camN) must match the configuration file name you used to configure the camera in MAX. You can also open a camera using its 64-bit serial number (uuid:XXXXXXXXXXXXXXXX), where the number following uuid must be a 64-bit hexadecimal number representing the internal serial number of the camera. Note Specify "uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |
|  | Note Specify "uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |  |
| resetALL | unsigned int | If the resetALL value is false, then only the specified camera will be reset. If the resetALL value is true, then all of the connected cameras will be reset. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxresetethernetcameraaddress.html language=enus -->
## TOPIC 00057: IMAQdxResetEthernetCameraAddress

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxresetethernetcameraaddress.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxresetethernetcameraaddress.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxResetEthernetCameraAddress

#### Format

rval = IMAQdxError ResetEthernetCameraAddress(const char* name, const char* address, const char* subnet, const char* gateway, u32 timeout)

#### Purpose

Force a new static IP address for the specified camera. Use IMAQdxResetEthernetCameraAddress when the camera is configured for a different subnet than your network. The code execution will suspend for the current thread and will resume after the specified timeout or as soon as it completes. Call this function before calling 
[IMAQdxDiscoverEthernetCameras](imaqdxdiscoverethernetcameras.html). Resetting the Ethernet Address is optional for cameras not on the local subnet.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| name | const char * | The name of the camera you want to open. name (cam0, cam1, ..., camN) must match the configuration file name you used to configure the camera in MAX. You can also open a camera using its 64-bit serial number (uuid:XXXXXXXXXXXXXXXX), where the number following uuid must be a 64-bit hexadecimal number representing the internal serial number of the camera. Note Specify "uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |
|  | Note Specify "uuid:serial number in hexadecimal representation" for the camera name when opening in listening mode. The serial number must match the serial number used in MAX. |  |
| address | const char* | Network address for the camera. |
| subnet | const char* | Subnet mask for the camera. |
| gateway | const char* | Gateway for the camera. |
| timeout | unsigned int | Time, in milliseconds, allowed for the Ethernet camera to reset its network address. The default timeout is 1000 ms. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsequence.html language=enus -->
## TOPIC 00058: IMAQdxSequence

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsequence.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSequence

#### Format

rval = IMAQdxSequence (IMAQdxSession id, Image *images[], unsigned int count);

#### Purpose

Configures, starts, acquires, stops, and unconfigures a sequence acquisition. Use this function to capture multiple images. If you call this function before calling [IMAQdxOpenCamera](imaqdxopencamera.html), IMAQdxSequence uses cam0 by default.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| images | Image *[] | The image array that receives the captured pixel data. |
| count | unsigned int | The number of images in the image array. This value must be less than or equal to the number of allocated images in the image array. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsequencecw.html language=enus -->
## TOPIC 00059: IMAQdxSequenceCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsequencecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsequencecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSequenceCW

#### Format

IMAQdxSequenceCW (id As IMAQdxSession, images() As CWIMAQImage, count As Long) As IMAQdxError

#### Purpose

Configures, starts, acquires, stops, and unconfigures a sequence acquisition. Use this function to capture multiple images. If you call this function before calling [IMAQdxOpenCamera](imaqdxopencamera.html), IMAQdxSequence uses cam0 by default.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| images | CWIMAQImage [] | The image array that receives the captured pixel data. |
| count | Long | The number of images in the image array. This value must be less than or equal to the number of allocated images in the image array. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxserialflush.html language=enus -->
## TOPIC 00060: IMAQdxSerialFlush

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxserialflush.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxserialflush.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSerialFlush

#### Format

rval = IMAQdxSerialFlush(IMAQdxSession id);

#### Purpose

Clears the internal serial read buffer. In a serial write/read sequence, call IMAQdxSerialFlush before calling [IMAQdxSerialWrite](imaqdxserialflush.html).

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxserialread.html language=enus -->
## TOPIC 00061: IMAQdxSerialRead

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxserialread.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxserialread.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSerialRead

#### Format

rval = IMAQdxSerialRead(IMAQdxSession id, Int8* buffer, uInt32* bufferSize, uInt32 timeoutMs);

#### Purpose

Reads in data from the serial port on devices that support serial communication. This function fills the buffer with characters received from the serial port until either a termination character has been received or the timeout period has elapsed. The termination character is defined in the camera file associated with the session.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| buffer | Int8* | A buffer to receive the data from the serial port. |
| bufferSize | uInt32* | On input, the size of the buffer. On output, the number of bytes read into the buffer. |
| timeoutMs | uInt32 | This is time, in milliseconds, to wait for the data to be read. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxserialreadbytes.html language=enus -->
## TOPIC 00062: IMAQdxSerialReadBytes

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxserialreadbytes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxserialreadbytes.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSerialReadBytes

#### Format

rval = IMAQdxSerialReadBytes(IMAQdxSession id, Int8* buffer, uInt32* bufferSize, uInt32 timeoutMs);

#### Purpose

Reads in an expected number of bytes from the serial port on image acquisition devices that support serial communication. This function fills the buffer with characters received from the serial port until either the buffer is full or the timeout period has elapsed. When you use this function, the serial termination string attribute is ignored.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| buffer | Int8* | A buffer to receive the data from the serial port. |
| bufferSize | uInt32* | On input, the size of the buffer. On output, the number of bytes read into the buffer. |
| timeoutMs | uInt32 | This is time, in milliseconds, to wait for the data to be read. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxserialwrite.html language=enus -->
## TOPIC 00063: IMAQdxSerialWrite

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxserialwrite.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxserialwrite.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSerialWrite

#### Format

rval = IMAQdxSerialWrite(IMAQdxSession id, Int8* buffer, uInt32* bufferSize, uInt32 timeoutMs);

#### Purpose

Writes data to the serial port.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| buffer | Int8* | A buffer to receive the data from the serial port. |
| bufferSize | uInt32* | On input, the size of the buffer. On output, the number of bytes read into the buffer. |
| timeoutMs | uInt32 | This is time, in milliseconds, to wait for the data to be written. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsetattribute.html language=enus -->
## TOPIC 00064: IMAQdxSetAttribute

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsetattribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsetattribute.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSetAttribute

#### Format

rval = IMAQdxSetAttribute (IMAQdxSession id, const char *name, IMAQdxValueType type, ...);

#### Purpose

Sets the value for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char * | The name of the attribute you want to set. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the attribute value you want to set. |
| ... | variable argument | Data is passed by value. The data type should match type. |

#### Parameter Discussion

**name** specifies the attribute whose value you want to obtain. In LabWindows/CVI function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box opens containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. You can access function help text for each attribute by double-clicking an attribute or by selecting the attribute and pressing <Enter>.

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, IMAQdxValueTypeF64, IMAQdxValueTypeString, IMAQdxValueTypeEnumItem, and IMAQdxValueTypeBool.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsetattributecw.html language=enus -->
## TOPIC 00065: IMAQdxSetAttributeCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsetattributecw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsetattributecw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSetAttributeCW

#### Format

IMAQdxSetAttributeCW (id As IMAQdxSession, name As String, type As IMAQdxValueType, value As VARIANT) As IMAQdxError

#### Purpose

Sets the value for a camera attribute.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | String | The name of the attribute you want to set. Refer to Attribute Name for a list of attributes. |
| type | IMAQdxValueType | The type of the attribute you want to set. |
| value | VARIANT (passed by reference) | The value of the specified attribute. |

#### Parameter Discussion

**type** specifies the type of the value parameter. The following types are supported: IMAQdxValueTypeU32, IMAQdxValueTypeI64, IMAQdxValueTypeF64, IMAQdxValueTypeString, IMAQdxValueTypeEnumItem, and IMAQdxValueTypeBool.

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsnap.html language=enus -->
## TOPIC 00066: IMAQdxSnap

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsnap.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsnap.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSnap

#### Format

rval = IMAQdxSnapImage (IMAQdxSession id, Image *image);

#### Purpose

Configures, starts, acquires, and unconfigures a snap acquisition. Use a snap for low-speed or single-capture applications where ease of programming is essential. If you call this function before calling [IMAQdxOpenCamera](imaqdxopencamera.html), IMAQdxSnap uses cam0 by default. If the image type does not match the video format of the camera, this function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| image | Image * | The image that receives the captured pixel data. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxsnapcw.html language=enus -->
## TOPIC 00067: IMAQdxSnapCW

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxsnapcw.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxsnapcw.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxSnapCW

#### Format

IMAQdxSnapCW (id As IMAQdxSession, image As CWIMAQImage) As IMAQdxError

#### Purpose

Configures, starts, acquires, and unconfigures a snap acquisition. Use a snap for low-speed or single-capture applications where ease of programming is essential. If you call this function before calling [IMAQdxOpenCamera](imaqdxopencamera.html), IMAQdxSnap uses cam0 by default. If the image type does not match the video format of the camera, this function changes the image type to a suitable format.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| image | CWIMAQImage | The image that receives the captured pixel data. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxstartacquisition.html language=enus -->
## TOPIC 00068: IMAQdxStartAcquisition

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxstartacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxstartacquisition.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxStartAcquisition

#### Format

rval = IMAQdxStartAcquisition (IMAQdxSession id);

#### Purpose

Starts an acquisition that was previously configured with [IMAQdxConfigureAcquisition](imaqdxconfigureacquisition.html). Use [IMAQdxStopAcquisition](imaqdxstopacquisition.html) to stop the acquisition.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxstopacquisition.html language=enus -->
## TOPIC 00069: IMAQdxStopAcquisition

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxstopacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxstopacquisition.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxStopAcquisition

#### Format

rval = IMAQdxStopAcquisition (IMAQdxSession id);

#### Purpose

Stops an acquisition previously started with [IMAQdxStartAcquisition](imaqdxstartacquisition.html).

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxunconfigureacquisition.html language=enus -->
## TOPIC 00070: IMAQdxUnconfigureAcquisition

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxunconfigureacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxunconfigureacquisition.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxUnconfigureAcquisition

#### Format

rval = IMAQdxUnconfigureAcquisition (IMAQdxSession id);

#### Purpose

Unconfigures an acquisition previously configured with [IMAQdxConfigureAcquisition](imaqdxconfigureacquisition.html).

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwaitforattributeupdated.html language=enus -->
## TOPIC 00071: IMAQdxWaitForAttributeUpdated

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwaitforattributeupdated.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwaitforattributeupdated.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWaitForAttributeUpdated

#### Format

rval = IMAQdxWaitForAttributeUpdated(IMAQdxSession id, const char* name, Int32 timeout);

#### Purpose

Synchronous wait for an attribute value change event.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| name | const char* | The name of the attribute to wait on. |
| timeout | Int32 | The maximum time to wait in milliseconds for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwaitforframedone.html language=enus -->
## TOPIC 00072: IMAQdxWaitForFrameDone

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwaitforframedone.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwaitforframedone.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWaitForFrameDone

#### Format

rval = IMAQdxWaitForFrameDone(IMAQdxSession id, Int32 timeout, uInt32* bufferNumber);

#### Purpose

Synchronous wait for the next Frame Done event.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| timeout | Int32 | The maximum time to wait in milliseconds for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| bufferNumber | uInt32* | On return, the buffer number that corresponds to the Frame Done event. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwaitforiosignaledge.html language=enus -->
## TOPIC 00073: IMAQdxWaitForIOSignalEdge

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwaitforiosignaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwaitforiosignaledge.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWaitForIOSignalEdge

#### Format

rval = IMAQdxWaitForIOSignalEdge(IMAQdxSession id, IMAQdxIOSignalType signalType, uInt32 signalNum ber, IMAQdxEdge signalEdge, Int32 timeout);

#### Purpose

Synchronous wait for an edge on an IO signal.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| signalType | IMAQdxIOSignalType | The IO signal type to wait for. Choose from the following options: IMAQdxIOSignalTypeTTL IMAQdxIOSignalTypeRTSI IMAQdxIOSignalTypeIsoIn IMAQdxIOSignalTypeIsoOut |
| signalNumber | uInt32 | The line number of the IO signal type to wait for. |
| signalEdge | IMAQdxEdge | The edge of the IO signal to wait for. Choose from the following options: IMAQdxEdgeRising IMAQdxEdgeFalling |
| timeout | Int32 | The maximum time to wait in milliseconds for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwaitforpnpevent.html language=enus -->
## TOPIC 00074: IMAQdxWaitForPnpEvent

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwaitforpnpevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwaitforpnpevent.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWaitForPnpEvent

#### Format

rval = IMAQdxWaitForPnpEvent(IMAQdxSession id, IMAQdxPnpEvent event, Int32 timeout);

#### Purpose

Synchronous wait for a Plug-n-Play event.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| event | IMAQdxPnpEvent | The plug and play event to monitor. The following events are valid: IMAQdxPnpEventCameraAttached: Callback fired when a new camera is attached. IMAQdxPnpEventCameraDetached: Callback fired when the camera is detached. IMAQdxPnpEventBusReset: Callback fired when a FireWire bus reset occurs. |
| timeout | Int32 | The maximum time to wait in milliseconds for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwaitforstatussignal.html language=enus -->
## TOPIC 00075: IMAQdxWaitForStatusSignal

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwaitforstatussignal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwaitforstatussignal.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWaitForStatusSignal

#### Format

rval = IMAQdxWaitForStatusSignal(IMAQdxSession id, IMAQdxStatusSignalType statusSignalType, Int32 timeout);

#### Purpose

Synchronous wait for a Status event.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| statusSignalType | IMAQdxStatusSignalType | The status signal to wait for. Choose from the following options: IMAQdxStatusSignalTypeAcquisitionActive IMAQdxStatusSignalTypeAcquisitionDone IMAQdxStatusSignalTypeFrameStart IMAQdxStatusSignalTypeFrameDone IMAQdxStatusSignalTypeBufferComplete |
| timeout | Int32 | The maximum time to wait in milliseconds for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwriteattributes.html language=enus -->
## TOPIC 00076: IMAQdxWriteAttributes

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwriteattributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwriteattributes.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWriteAttributes

#### Format

rval = IMAQdxWriteAttributes (IMAQdxSession id, const char* filename)

#### Purpose

Writes current attributes to the camera file. This function is only required if you wish to save parameters.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID. |
| Filename | Const char* | The filename to load the attributes from. Specify NULL to load from the default camera file. Specify a valid filename to override the default camera file. The driver locates camera files in the <NI-IMAQdx\\Data> folder if no path information is specified. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html) or, if you are using Microsoft Visual Basic, [IMAQdxGetErrorStringCW](imaqdxgeterrorstringcw.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwritememory.html language=enus -->
## TOPIC 00077: IMAQdxWriteMemory

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwritememory.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwritememory.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWriteMemory

#### Format

rval = IMAQdxWriteMemory (IMAQdxSession id, unsigned int offset, char *value, unsigned int count);

#### Purpose

Accesses registers on the camera and writes a string to the camera.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| offset | unsigned int | The register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use attribute IMAQdxAttributeBaseAddress to obtain the base address for the camera. |
| value | char * | Specifies the string to write to the memory offset. |
| count | unsigned int | Specifies the length of the string to write to the memory offset. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/imaqdxwriteregister.html language=enus -->
## TOPIC 00078: IMAQdxWriteRegister

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/imaqdxwriteregister.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/imaqdxwriteregister.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdxWriteRegister

#### Format

rval = IMAQdxWriteRegister(IMAQdxSession id, unsigned int offset, unsigned int value);

#### Purpose

Accesses registers on the camera and writes a 32-bit value to the camera. Data is byte-swapped for big endian alignment before transfer.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | IMAQdxSession | A valid Session ID, which you can obtain using IMAQdxOpenCamera. |
| offset | unsigned int | The register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use attribute IMAQdxAttributeBaseAddress to obtain the base address for the camera. |
| value | unsigned int | Specifies the value to write to the memory offset. |

#### Return Value

On success, this function returns IMAQdxErrorSuccess. On failure, this function returns an error code. You can obtain a more detailed error message with [IMAQdxGetErrorString](imaqdxgeterrorstring.html).

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/info.html language=enus -->
## TOPIC 00079: Using Help

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/info.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/info.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Help

[Conventions](conventions.html)

[Navigating Help](navigating.html)

[Searching Help](searching.html)

[Printing Help File Topics](printing_this_help_file.html)

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/navigating.html language=enus -->
## TOPIC 00080: Navigating Help (Windows Only)

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/navigating.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/navigating.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Navigating Help (Windows Only)

To navigate this help file, use the **Contents**, **Index**, and **Search** tabs to the left of this window or use the following toolbar buttons located above the tabs:

- Hide —Hides the navigation pane from view.
- Locate —Locates the currently displayed topic in the Contents tab, allowing you to view related topics.
- Back —Displays the previously viewed topic.
- Forward —Displays the topic you viewed before clicking the Back button.
- Options —Displays a list of commands and viewing options for the help file.

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/ni-imaqdx_function_reference_help.html language=enus -->
## TOPIC 00081: NI-IMAQdx Function Reference Help

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/ni-imaqdx_function_reference_help.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/ni-imaqdx_function_reference_help.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### NI-IMAQdx Function Reference Help

July 2021, 371968F-01

NI-IMAQdx driver software gives you the ability to acquire images from:

- Camera Link cameras in Windows using supported NI PCIe and PXIe frame grabbers
- ISC-178x smart cameras
- GigE Vision-compliant cameras
- USB3 Vision-compliant cameras
- DirectShow compatible cameras (Windows), UVC-compliant webcams (Linux RT)

This help file describes the functions included in the NI-IMAQdx driver software.

For more information about this help file, refer to the following topics:

[Related Documentation](related_documentation.html)

[Glossary](glossary.html)

[NI Services](technical_support_resources.html)

© 2006—2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/printing_this_help_file.html language=enus -->
## TOPIC 00082: Printing Help File Topics (Windows Only)

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/printing_this_help_file.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/printing_this_help_file.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Printing Help File Topics (Windows Only)

Complete the following steps to print an entire book from the **Contents** tab:

1. Right-click the book.
2. Select Print from the shortcut menu to display the Print Topics dialog box.
3. Select the Print the selected heading and all subtopics option.
 [IMAGE alt='Note' src='note.gif']
**Note** Select **Print the selected topic** if you want to print the single topic you have selected in the **Contents** tab.
4. Click the OK button.

#### Printing PDF Documents

This help file may contain links to PDF documents. To print PDF documents, click the print button located on the Adobe Acrobat Viewer toolbar.

<!--NI_TOPIC bundle=ni-imaqdx-c-api-ref path=ni-imaqdx_function_reference/searching.html language=enus -->
## TOPIC 00083: Searching Help (Windows Only)

- bundle_id: `ni-imaqdx-c-api-ref`
- source_path: `ni-imaqdx_function_reference/searching.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-c-api-ref/raw/resource/enus/ni-imaqdx_function_reference/searching.html
- document_id: `ni-imaqdx-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Searching Help (Windows Only)

Use the **Search** tab to the left of this window to locate content in this help file. If you want to search for words in a certain order, such as "related documentation," add quotation marks around the search words as shown in the example. Searching for terms on the **Search** tab allows you to quickly locate specific information and information in topics that are not included on the **Contents** tab.

#### Wildcards

You also can search using asterisk (*) or question mark (?) wildcards. Use the asterisk wildcard to return topics that contain a certain string. For example, a search for "prog*" lists topics that contain the words "program," "programmatically," "progress," and so on.

Use the question mark wildcard as a substitute for a single character in a search term. For example, "?ext" lists topics that contain the words "next," "text," and so on.

|  | Note Wildcard searching will not work on Simplified Chinese, Traditional Chinese, Japanese, and Korean systems. |
| --- | --- |

#### Nested Expressions

Use nested expressions to combine searches to further refine a search. You can use Boolean expressions and wildcards in a nested expression. For example, "example AND (program OR VI)" lists topics that contain "example program" or "example VI." You cannot nest expressions more than five levels.

#### Boolean Expressions

Click the [IMAGE alt='Boolean Button' src='bool.gif'] button to add Boolean expressions to a search. The following Boolean operators are available:

- AND (default)—Returns topics that contain both search terms. You do not need to specify this operator unless you are using nested expressions.
- OR —Returns topics that contain either the first or second term.
- NOT —Returns topics that contain the first term without the second term.
- NEAR —Returns topics that contain both terms within eight words of each other.

#### Search Options

Use the following checkboxes on the **Search** tab to customize a search:

- Search previous results —Narrows the results from a search that returned too many topics. You must remove the checkmark from this checkbox to search all topics.
- Match similar words —Broadens a search to return topics that contain words similar to the search terms. For example, a search for "program" lists topics that include the words "programs," "programming," and so on.
- Search titles only —Searches only in the titles of topics.
