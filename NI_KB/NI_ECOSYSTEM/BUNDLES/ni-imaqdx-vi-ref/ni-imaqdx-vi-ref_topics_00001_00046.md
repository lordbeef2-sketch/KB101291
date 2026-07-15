# NI DOCUMENT BUNDLE: ni-imaqdx-vi-ref

<!--NI_BUNDLE_CHUNK bundle=ni-imaqdx-vi-ref start=1 end=46 -->
<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/bp_nilm.html language=enus -->
## TOPIC 00001: Activating Your Software

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/bp_nilm.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/bp_nilm.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### Activating Your Software

##### How Do I Activate My Software?

Before using your product, you must activate it in accordance with its license agreement. To activate a product, you must first purchase a license. For information on purchasing licenses, contact your local NI sales representative or visit ni.com/niglobal.

Complete the following steps to activate your NI products:

1. Select Start»National Instruments»NI License Manager to open NI License Manager.
2. Select one of the following methods to launch the Activate Software window:
  - Click Activate Software on the ribbon.
  - When in the Local Licenses view, right-click the product in the License tree and select Activate .
3. If requested, log in to your NI User Account. If you do not have a User Account, you must create one.
4. Select one of the following methods to activate your products.
  - Check my account for licenses 
 Licenses associated with your account are verified successfully, activation completes. If your account lacks the appropriate licenses for a particular product, proceed to activate the product using either a activation code or a serial number.
  - Enter a serial number 
 You can find your serial numbers in the following locations:
    - On the Certificate of Ownership included in your software kit
    - On the product packing slip or shipping label
    - Visit ni.com/info and enter the Info Code SerialNumbers_en.
    - If you have installed a previous version of your application software using your serial number, you can find the serial number by selecting Help»About within the application.
    - Contact your local NI branch.
  - Enter activation codes 
 Click on **Generate an activation code** or visit ni.com/activate to obtain an activation code.
  - Connect to a volume license server 
 Enter the name of the volume license server on which your NI products should check for licenses.
5. Follow the prompts in the Activate Software window to complete activation.

If you activated through your NI software, you can use the product immediately after successful activation.

|  | Notes If you were using NI software before you began the activation process, you may need to restart the software for the change to take effect. If your NI software is licensed through a volume license agreement, you do not need to activate your product. Instead, you need to point NI License Manager to a volume license server. For more information, refer to the Using a Volume License Server topic of the NI License Manager Help. |
| --- | --- |

##### What Is Activation?

Activation is the process of obtaining an activation code to enable your software to run on your computer. An *activation code* is an alphanumeric string that verifies the software, version, and computer ID to enable features on your computer. Activation codes are unique and are valid on only one computer.

##### What Information Do I Need to Activate My NI Software?

You need your NI User account log-in, the product version and serial number, and a computer ID that uniquely identifies your computer. Certain activation methods may require additional information for delivery. This information is used only to activate your product. Complete disclosure of the NI software licensing information privacy policy is available at ni.com/activate/privacy. If you optionally choose to register your software, your information is protected under the NI privacy policy, available at ni.com/privacy.

##### How Do I Find My Product Serial Number?

Your serial number uniquely identifies your purchase of NI software. You can find your serial number on the Certificate of Ownership included in your software kit, or you can visit ni.com/info and enter the Info Code SerialNumbers_en.

If you have installed a previous version using your serial number, you can find the serial number by selecting **Help»About** within the application. You can also contact your local NI branch at ni.com/contact.

##### What Is a Computer ID?

The computer ID is a 16-character value that uniquely identifies your computer. NI requires this information to enable your software. You can find your computer ID through the NI Licensing Wizard or by using NI License Manager, as follows:

1. Launch the NI License Manager.
2. Click Computer Information in the ribbon.

For more information about product activation and licensing, refer to ni.com/activate.

##### How Can I Evaluate NI Software?

You can evaluate most NI products, in accordance with the license agreement. Evaluation terms vary, depending on which product you want to evaluate. Refer to your product documentation for specific information on the product's evaluation mode.

##### Moving Software after Activation

To transfer your software to another computer, uninstall the software on the first computer, then install and activate it on the second computer. You can transfer your software from one computer to another; you do not need to contact or inform NI of the transfer. Because activation codes are unique to each computer, you will need a new activation code. Refer to the [How do I Activate my Software?](#activate) section of this topic to learn how to acquire a new activation code and reactivate your software.

##### Deactivating a Product

To deactivate a product and return it to its preactivation state, navigate to the **Local Licenses** view, select the product to be deactivated, and click **Deactivate** from the ribbon. Alternatively, navigate to the **Local Licenses** view, right-click the product in the License tree, and click **Deactivate**. If the product was in evaluation mode before you activated it, the properties of the evaluation mode may not be restored.

##### Using Windows Guest Accounts

NI License Manager does not support Microsoft Windows Guest accounts. You must log in to a non-Guest account to run licensed NI application software.

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/error_codes.html language=enus -->
## TOPIC 00002: Error Codes

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/error_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/error_codes.html
- document_id: `ni-imaqdx-vi-ref`
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
| -1074360312 | IMAQdxErrorNotImplemented | Not implemented |
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
| -1074360295 | IMAQdxErrorAsyncWrite | Unable to perform asychronous register write. |
| -1074360294 | IMAQdxErrorAsyncRead | Unable to perform asychronous register read. |
| -1074360293 | IMAQdxErrorTimeout | Timeout. |
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
| -1074360276 | IMAQdxErrorCameraUnreachable | Unable to connect to the camera. |
| -1074360275 | IMAQdxErrorHighPerformanceNotSupported | High performance acquisition is not supported on the specified network interface. Connect the camera to a network interface running the high performance driver. |
| -1074360274 | IMAQdxErrorInterfaceNotRenamed | Unable to rename interface. Invalid or duplicate name specified. |
| -1074360273 | IMAQdxErrorNoSupportedVideoModes | The camera does not have any video modes which are supported. |
| -1074360272 | IMAQdxErrorSoftwareTriggerOverrun | Software trigger overrun. |
| -1074360271 | IMAQdxErrorTestPacketNotReceived | The system did not receive a test packet from the camera. The packet size may be too large for the network configuration or a firewall may be enabled. |
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
| -1074360231 | IMAQdxErrorRingAcqPaddingCapabilityExceeded | The padding necessary to transfer the configured image using a ring acquisition is more than the camera is capable of providing. Reduce the amount of padding required by reducing the image border size or changing the image width. |
| -1074360230 | IMAQdxErrorNIGEVUpdateRequired | The NI-GEV driver is too old to support this functionality. Please update it to a newer version. |
| -1074360229 | IMAQdxErrorPacketSizeOver9000 | The desired packet size is larger than the maximum value of 9000 supported by the network interface. |
| -1074360228 | IMAQdxErrorAttributeSetFailure | There was a failure when trying to set the value of a writeable camera attribute. |
| -1074360227 | IMAQdxErrorFirmwareUpdatePowerCycleNeeded | The firmware on the acquisition hardware has been updated. Shutdown the system, disconnect power, and then reconnect power before use. |
| -1074360226 | IMAQdxErrorLensCommunicationFailure | An error occured while communicating with the lens. |
| -1074360225 | IMAQdxErrorBIOSIncompatible | The BIOS version is incompatible with the installed version of NI-IMAQdx. |
| -1074360224 | IMAQdxErrorAdministrativePrivilegesRequired | The requested operation requires administrative privileges. |
| -1074360223 | IMAQdxErrorNIIMAQUpdateRequired | The NI-IMAQ driver is too old to support the NI-IMAQdx API. Please update it to a newer version. |
| -1074360222 | IMAQdxErrorCannotRenameBoardWhileSessionOpen | The board cannot be renamed while there are open sessions to any of its acquisition units. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/error_handling.html language=enus -->
## TOPIC 00003: LabVIEW VI Error Handling

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/error_handling.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/error_handling.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### LabVIEW VI Error Handling

Every NI-IMAQdx VI contains an **error in** input cluster and an **error out** output cluster. The clusters contain a Boolean that indicates whether an error occurred, the code for the error, and the source or name of the VI that returned the error. If **error in** indicates an error, the VI passes the error information to **error out** and does not execute any NI-IMAQ function.

You can use the Simple Error Handler VI (**Functions»Time&Dialog**) to check for errors that occur while executing a VI. If you wire an error cluster to the Simple Error Handler VI, the VI deciphers the error information and displays a dialog box that describes the error. If no error occurred, the Simple Error Handler VI does nothing.

[Error Codes](error_codes.html)

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/express_vision_acquisition.html language=enus -->
## TOPIC 00004: Vision Acquisition Express VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/express_vision_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/express_vision_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vision Acquisition Express VI

Acquires images from cameras using NI-IMAQ or NI-IMAQdx. Refer to the *NI Vision Acquisition Express VI Help* for more information. The *NI Vision Acquisition Express VI Help* installs to the <LabVIEW>\help directory, where <LabVIEW> is the location to which you installed LabVIEW.

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_calculate_frames_per_second.html language=enus -->
## TOPIC 00005: IMAQdx Calculate Frames Per Second VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_calculate_frames_per_second.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_calculate_frames_per_second.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Calculate Frames Per Second VI

Owning Palette:

NI-IMAQdx

Installed With:

Calculates the acquired and processing frame rate, the images behind, and images missed. This VI operates on a per-session basis, so it can be called with different IMAQdx camera sessions in parallel and it will return the calculated values for the session passed in.

[IMAGE alt='IMAQdx Calculate Frames Per Second' src='imaqdx_calculate_frames_per_second.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Buffer Number is the image buffer number returned when acquiring an image from IMAQdx Grab or IMAQdx Get Image VIs. |
|  | Minimum Display Update Interval (ms) specifies the minimum rate to update the display. This control affects how often the Update Display indicator is true. |
|  | Frames per Second Interval (ms) specifies the interval in milliseconds to update the Acquired Frames per Second and Processed Frames per Second indicators. |
|  | Reset Counters specifies whether the Images Behind, Images Missed, and frame rate counters should be reset. Specify true when the acquisition is reconfigured because the buffer number returned by the driver will also be reset. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Acquired Frames per Second indicates the frame rate of the camera. This value is updated on an interval specified by the Frames per Second Update Interval (ms). |
|  | Processed Frames per Second indicates the rate that this VI is called. This value is updated on an interval specified by the Frames per Second Update Interval (ms). |
|  | Images Behind indicates how many images behind the Buffer Number passed to this VI is compared to the current image the driver has acquired. This indicator is useful only when IMAQdx Get Image is used with the Buffer Number Mode parameter set to Every because other modes may skip images and will never be behind. |
|  | Images Missed indicates how many cumulative images have been missed. An image is missed when the Buffer Number passed to this VI is more than 1 greater than the previous iteration's buffer number. This indicator is useful only when IMAQdx Get Image is used with the Buffer Number Mode parameter set to Every. |
|  | Update Display indicates that the image display control can be updated to help avoid getting behind in the acquisition loop. This control is always true if the acquisition is not behind (i.e. Images Behind is 0). If the acquisition is behind, it will be true based on the Minimum Display Update Interval (ms). |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_close_camera.html language=enus -->
## TOPIC 00006: IMAQdx Close Camera VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_close_camera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_close_camera.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Close Camera VI

Owning Palette:

NI-IMAQdx

Installed With:

Stops an acquisition in progress, releases resources associated with an acquisition, and closes the specified Camera Session.

[IMAGE alt='IMAQdx Close Camera' src='imaqdx_close_camera.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_configure_acquisition.html language=enus -->
## TOPIC 00007: IMAQdx Configure Acquisition VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_configure_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_configure_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Configure Acquisition VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Configures a low-level acquisition previously opened with IMAQdx Open Camera VI. Specify the acquisition type with the **Continuous?** and **Number of Buffers** parameters.

Snap: Continuous = 0; Buffer Count = 1

Sequence: Continuous = 0; Buffer Count > 1

Grab: Continuous = 1; Buffer Count > 1

[IMAGE alt='IMAQdx Configure Acquisition' src='imaqdx_configure_acquisition.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Continuous? specifies whether the acquisition is continuous or one shot. |
|  | Number of Buffers specifies the number of images to acquire for a one shot acquisition. For a continuous acquisition, this parameter specifies the number of buffers the driver uses internally. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_configure_grab.html language=enus -->
## TOPIC 00008: IMAQdx Configure Grab VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_configure_grab.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_configure_grab.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Configure Grab VI

Owning Palette:

NI-IMAQdx

Installed With:

Configures and starts a grab acquisition. A grab performs an acquisition that loops continually on a ring of buffers. Use the grab VI for high-speed image acquisition. Use the IMAQdx Grab VI to copy an image out of the buffer. If you call this VI before calling the IMAQdx Open Camera VI, the IMAQdx Configure Grab VI uses cam0 by default. Use the IMAQdx Unconfigure Acquisition VI to unconfigure the acquisition.

[IMAGE alt='IMAQdx Configure Grab' src='imaqdx_configure_grab.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Number of Buffers specifies the number of buffers the driver uses internally for the continuous acquisition. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_configure_ring_acquisition.html language=enus -->
## TOPIC 00009: IMAQdx Configure Ring Acquisition VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_configure_ring_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_configure_ring_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Configure Ring Acquisition VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Configures a ring acquisition. A ring acquisition is an acquisition in which the image is acquired directly into the images in the **Images** array.

You can retrieve the acquired images directly by using the [IMAQdx Extract Image](imaqdx_extract_image.html) VI.
The driver cannot acquire a new image into an image that is being extracted. To allow the acquisition to proceed, release the image by calling the [IMAQdx Release Image](imaqdx_release_image.html) VI or by calling the [IMAQdx Extract Image](imaqdx_extract_image.html) VI with the **Release Previous** control set to TRUE.

[IMAGE alt='IMAQdx Configure Ring Acquisition' src='imaqdx_configure_ring_acquisition.gif']

|  | Mode specifies whether the acquisition is continuous or one shot. One Shot (0) Acquire a finite number of consecutive images from the camera. Continuous (1) Continuously acquire images from the camera. |
| --- | --- |
| One Shot (0) | Acquire a finite number of consecutive images from the camera. |
| Continuous (1) | Continuously acquire images from the camera. |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Images is an array of image references to use in a circular buffer list to acquire images from the camera. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Images Out is an array of image references that are configured to serve as the buffers for the ring acquisition. Images Out is the same as Images. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_discover_ethernet_cameras.html language=enus -->
## TOPIC 00010: IMAQdx Discover Ethernet Cameras VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_discover_ethernet_cameras.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_discover_ethernet_cameras.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Discover Ethernet Cameras VI

Owning Palette:

NI-IMAQdx

Installed With:

Initiates a round of Ethernet camera discovery. Use this VI to find Ethernet cameras on the network with a remote subnet. This VI will be blocked and will return after the specified timeout. The address specifies the destination address for the discovery command. The default address is 255.255.255.255. Call this VI before calling IMAQdx Enumerate Cameras VI or IMAQdx Open Camera VI.

[IMAGE alt='IMAQdx Discover Ethernet Cameras' src='imaqdx_discover_ethernet_cameras.gif']

|  | Timeout (1000 ms) specifies the time, in milliseconds, allowed for the Ethernet camera discovery to complete. |
| --- | --- |
|  | Address (Broadcast) specifies the destination address for the discovery command. The default address is 255.255.255.255. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_enumerate_attributes.html language=enus -->
## TOPIC 00011: IMAQdx Enumerate Attributes VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_enumerate_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_enumerate_attributes.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Enumerate Attributes VI

Owning Palette:

NI-IMAQdx

Installed With:

Gets the attributes supported by the camera.

[IMAGE alt='IMAQdx Enumerate Attributes' src='imaqdx_enumerate_attributes.gif']

|  | Visibility specifies the branch of the attributes to enumerate. Simple and Intermediate visibility enumerate a reduced list of attributes. Advanced visibility enumerates all available attributes. |
| --- | --- |
|  | Root specifies the branch of the attribute tree to enumerate. Specify an empty string to enumerate the entire attribute tree. |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Attribute Information Array is an array of possible features supported by the camera. Attribute Type specifies the type of attribute. Possible attribute type values include U32, I64, DBL, String, Enum, Bool, and Command. Readable returns True if readable. Writable returns True if writable. Attribute Name specifies the fully qualified name of the attribute located in the attribute tree. |
|  | Attribute Type specifies the type of attribute. Possible attribute type values include U32, I64, DBL, String, Enum, Bool, and Command. |
|  | Readable returns True if readable. |
|  | Writable returns True if writable. |
|  | Attribute Name specifies the fully qualified name of the attribute located in the attribute tree. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_enumerate_cameras.html language=enus -->
## TOPIC 00012: IMAQdx Enumerate Cameras VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_enumerate_cameras.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_enumerate_cameras.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Enumerate Cameras VI

Owning Palette:

NI-IMAQdx

Installed With:

Returns a list of all cameras on the host computer.

[IMAGE alt='IMAQdx Enumerate Cameras' src='imaqdx_enumerate_cameras.gif']

|  | Connected Only? (Yes) If the Connected Only? value is Yes, then the Camera Information Array only contains cameras that are currently connected to the host computer. If the Connected Only? value is No, then the Camera Information Array contains cameras that are currently connected, and were previously connected, to the host computer. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Camera Information Array is an array of interface files that are on the host computer. This includes cameras that are currently connected or that were previously connected. Type has a value of 3. This designates an NI-IMAQdx interface file. Version is the version of the interface file. This number may increment with different versions of the driver as the format of the interface file changes. Flags is a bitwise mask of the current interface status. If bit 0 is on (value = 1), the interface represents a camera that is currently connected. If bit 0 is off (value = 0) , the interface represents a disconnected camera. SerialNumberHigh is the upper 32-bits of the interface serial number. Every camera has a unique value for SerialNumberHigh. SerialNumberLow is the lower 32-bits of the interface serial number. Every camera has a unique value for SerialNumberLow. BusType specifies the bus type for the camera. InterfaceName is the name of the interface. Use this name when opening the interface. VendorName is the vendor name of the camera designated for this interface. VendorName varies from camera to camera. ModelName is the model name of the camera designated for this interface. ModelName varies from camera to camera. CameraFileName is the name of the camera file that this interface uses. The camera file contains all the settings for a given camera. You can configure and save these settings from Measurement & Automation Explorer (MAX). CameraAttributeURL is the URL of the XML file that describes the camera attributes. |
|  | Type has a value of 3. This designates an NI-IMAQdx interface file. |
|  | Version is the version of the interface file. This number may increment with different versions of the driver as the format of the interface file changes. |
|  | Flags is a bitwise mask of the current interface status. If bit 0 is on (value = 1), the interface represents a camera that is currently connected. If bit 0 is off (value = 0) , the interface represents a disconnected camera. |
|  | SerialNumberHigh is the upper 32-bits of the interface serial number. Every camera has a unique value for SerialNumberHigh. |
|  | SerialNumberLow is the lower 32-bits of the interface serial number. Every camera has a unique value for SerialNumberLow. |
|  | BusType specifies the bus type for the camera. |
|  | InterfaceName is the name of the interface. Use this name when opening the interface. |
|  | VendorName is the vendor name of the camera designated for this interface. VendorName varies from camera to camera. |
|  | ModelName is the model name of the camera designated for this interface. ModelName varies from camera to camera. |
|  | CameraFileName is the name of the camera file that this interface uses. The camera file contains all the settings for a given camera. You can configure and save these settings from Measurement & Automation Explorer (MAX). |
|  | CameraAttributeURL is the URL of the XML file that describes the camera attributes. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_enumerate_video_modes.html language=enus -->
## TOPIC 00013: IMAQdx Enumerate Video Modes VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_enumerate_video_modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_enumerate_video_modes.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Enumerate Video Modes VI

Owning Palette:

NI-IMAQdx

Installed With:

Returns a list of video modes supported by the camera.

[IMAGE alt='IMAQdx Enumerate Video Modes' src='imaqdx_enumerate_video_modes.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Video Modes is an array of video modes supported by the current camera. Video Mode is the index for this video mode. Video Mode Name VideoMode Name is the name of the video mode, such as 640 x 480 Mono8. |
|  | Video Mode is the index for this video mode. |
|  | Video Mode Name VideoMode Name is the name of the video mode, such as 640 x 480 Mono8. |
|  | Current Mode is the index into the Video Modes array of the current mode used by the camera. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_extract_image.html language=enus -->
## TOPIC 00014: IMAQdx Extract Image VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_extract_image.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_extract_image.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Extract Image VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Retrieves an acquired image directly from the circular buffer list, and does not make a copy of the image. This function is valid only within the context of a ring acquisition.

The driver cannot acquire a new image into an image that is being extracted. To allow the acquisition to proceed, release the image by calling the [IMAQdx Release Image](imaqdx_release_image.html) VI or by calling the IMAQdx Extract Image VI with the **Release Previous** control set to TRUE.

[IMAGE alt='IMAQdx Extract Image' src='imaqdx_extract_image.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Buffer Number Mode (Next) specifies the buffer number mode. The default value is Next, which specifies that the driver waits for the next acquired buffer. Other possible values are Last, Buffer Number, Every, and Last New. Last specifies that the driver does not wait for the next buffer but instead returns the last acquired buffer. Buffer Number specifies an exact buffer number to wait for. Every returns all sequential images in memory. Last New returns the last acquired buffer if the buffer has not been returned before, to avoid returning duplicate images. Use Buffer Number Mode in conjunction with Buffer Number In. |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Buffer Number In is the cumulative image number to get. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Release Previous (true) specifies whether to release any previously extracted images before extracting the requested buffer. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Image Out is the reference to the captured image. |
|  | Buffer Number Out is the actual acquired buffer number returned. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_get_bayer_parameters_for_fpga.html language=enus -->
## TOPIC 00015: IMAQdx Get Bayer Parameters for FPGA VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_get_bayer_parameters_for_fpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_get_bayer_parameters_for_fpga.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Get Bayer Parameters for FPGA VI

Owning Palette:

NI-IMAQdx FPGA

Installed With:

Queries the host machine for the Bayer algorithm, pattern, and the red, green and blue color gains used to create an image. Outputs a raw Bayer image with information about how to decode it on the FPGA target. Use this VI to produce a color image that the FPGA target can process.

[Details](#details)

[IMAGE alt='IMAQdx Get Bayer Parameters for FPGA' src='imaqdx_get_bayer_parameters_for_fpga.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Bayer Parameters specifies the Bayer settings to use to create the image. Pattern specifies the variation of the Bayer encoding pattern to use. Red Gain is the gain to be applied to the red pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. Green Gain is the gain to be applied to the green pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. Blue Gain is the gain to be applied to the blue pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. |
|  | Pattern specifies the variation of the Bayer encoding pattern to use. |
|  | Red Gain is the gain to be applied to the red pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. |
|  | Green Gain is the gain to be applied to the green pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. |
|  | Blue Gain is the gain to be applied to the blue pixels in a Bayer-encoded image. The valid range for this parameter is 0 to 3.999. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### Details

The following block diagram shows an example of how to use this VI.

[IMAGE alt='image' src='getbayerparams.gif']

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_get_image2.html language=enus -->
## TOPIC 00016: IMAQdx Get Image2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_get_image2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_get_image2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Get Image2 VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Acquires the specified frame into **Image Out**. Call this VI only after calling the IMAQdx Configure Acquisition VI. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format.

[IMAGE alt='IMAQdx Get Image2' src='imaqdx_get_image2.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested image to become available. The default value is 5000. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Buffer Number Mode (Next) specifies the buffer number mode. The default value is Next, which specifies that the driver waits for the next acquired buffer. Other possible values are Last, Buffer Number, Every, and Last New. Last specifies that the driver does not wait for the next buffer but instead returns the last acquired buffer. Buffer Number specifies an exact buffer number to wait for. Every returns all sequential images in memory. Last New returns the last acquired buffer if the buffer has not been returned before, to avoid returning duplicate images. Use Buffer Number Mode in conjunction with Buffer Number In. |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Image In is the reference to the image that receives the captured pixel data. |
|  | Buffer Number In is the cumulative image number to get. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Image Out is the reference to the captured image. |
|  | Buffer Number Out is the actual acquired buffer number returned. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_get_image_data.html language=enus -->
## TOPIC 00017: IMAQdx Get Image Data VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_get_image_data.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_get_image_data.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Get Image Data VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Copies the raw data of the specified frame into **Image Data Array**. Call this VI only after calling the IMAQdx Configure Acquisition VI.

[IMAGE alt='IMAQdx Get Image Data' src='imaqdx_get_image_data.gif']

|  | Buffer Number Mode (Next) specifies the buffer number mode. The default value is Next, which specifies that the driver waits for the next acquired buffer. Other possible values are Last, Buffer Number, Every, and Last New. Last specifies that the driver does not wait for the next buffer but instead returns the last acquired buffer. Buffer Number specifies an exact buffer number to wait for. Every returns all sequential images in memory. Last New returns the last acquired buffer if the buffer has not been returned before, to avoid returning duplicate images. Use Buffer Number Mode in conjunction with Buffer Number In. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Buffer Number In is the cumulative image number to get. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Image Data Array is an array of unsigned bytes that represent the raw image data as transferred from the camera. |
|  | Buffer Number Out is the actual acquired buffer number returned. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_grab2.html language=enus -->
## TOPIC 00018: IMAQdx Grab2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_grab2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_grab2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Grab2 VI

Owning Palette:

NI-IMAQdx

Installed With:

Acquires the most current frame into Image Out. Call this VI only after calling IMAQdx Configure Grab.vi. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format.

[IMAGE alt='IMAQdx Grab2' src='imaqdx_grab2.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested image to become available. The default value is 5000. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Image In is the reference to the image that receives the captured pixel data. |
|  | Wait for Next Buffer? (Yes) if the value is Yes, the driver will wait for the next available buffer. If the Wait for Next Buffer? value is No, the driver will not wait for the next available buffer, and will instead return the last acquired buffer. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Image Out is the reference to the captured image. |
|  | Buffer Number Out is the actual acquired buffer number returned. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_open_camera.html language=enus -->
## TOPIC 00019: IMAQdx Open Camera VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_open_camera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_open_camera.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Open Camera VI

Owning Palette:

NI-IMAQdx

Installed With:

Opens a camera, queries the camera for its capabilities, loads a camera configuration file, and creates a unique reference to the camera. Use the IMAQdx Close Camera VI when you are finished with the reference.

[IMAGE alt='IMAQdx Open Camera' src='imaqdx_open_camera.gif']

|  | Camera Control Mode is the control mode of the camera used during image broadcasting. Open a camera in controller mode to actively configure and acquire image data. Open a camera in listener mode to passively acquire image data from a session that was opened in controller mode on a different host or target computer. The default value is Controller. |
| --- | --- |
|  | Session In specifies the name of the camera you wish to open. The default value is cam0. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_properties.html language=enus -->
## TOPIC 00020: NI-IMAQdx Properties

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_properties.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI-IMAQdx Properties

Refer to the class name below for the properties associated with each NI-IMAQdx class. Refer to the *NI-IMAQdx Function Reference Help* for more information about NI-IMAQdx properties and attributes.

| Attribute | Long Name | Type | Description |
| --- | --- | --- | --- |
| BaseAddress | Camera Information : Base Address |  | Read only. Gets the base address of the camera registers. |
| BusType | Camera Information : Bus Type |  | Read only. Gets the bus type of the camera. |
| ModelName | Camera Information : Model Name |  | Read only. Returns the model name. |
| SerialNumberHigh | Camera Information : Serial Number High |  | Read only. Gets the upper 32-bits of the camera 64-bit serial number. |
| SerialNumberLow | Camera Information : Serial Number Low |  | Read only. Gets the lower 32-bits of the camera 64-bit serial number. |
| VendorName | Camera Information : Vendor Name |  | Read only. Returns the vendor name. |
| HostIPAddress | Camera Information : Host IP Address |  | Read only. Returns the host adapter IP address. |
| IPAddress | Camera Information : IP Address |  | Read only. Returns the IP address. |
| PrimaryURLString | Camera Information : Primary URL String |  | Read only. Gets the camera's primary URL string. |
| SecondaryURLString | Camera Information : Secondary URL String |  | Read only. Gets the camera's secondary URL string. |
| AcquisitionInProgress | Status Information : Acquisition In Progress |  | Read only. Gets the current state of the acquisition. TRUE if acquiring; otherwise FALSE. |
| AttributeHandledEventCount | StatusInformation : HandledEventCount |  | Read only. Gets the number of handled events during an acquisition session. |
| BufferCount | Status Information : Last Buffer Count |  | Read only. Gets the number of transferred buffers. |
| LastBufferNumber | Status Information : Last Buffer Number |  | Read only. Gets the last cumulative buffer number transferred. |
| LostBufferCount | Status Information : Lost Buffer Count |  | Read only. Gets the number of lost buffers during an acquisition session. |
| LostEventCount | Status Information : Lost Event Count |  | Read only. Gets the number of lost events during an acquisition session. |
| LostPacketCount | Status Information : Lost Packet Count |  | Read only. Gets the number of lost packets during an acquisition session. |
| RequestedResendPackets | Status Information : Requested Resend Packet Count |  | Read only. Gets the number of packets requested to be resent during an acquisition session. |
| ReceivedResendPackets | Status Information : Received Resend Packets |  | Read only. Gets the number of packets that were requested to be resent during an acquisition session and were completed. |
| BayerGainB | Acquisition Attributes : Bayer : Gain B |  | Sets/gets the white balance gain for the blue component of the Bayer conversion. |
| BayerGainG | Acquisition Attributes : Bayer : Gain G |  | Sets/gets the white balance gain for the green component of the Bayer conversion. |
| BayerGainR | Acquisition Attributes : Bayer : Gain R |  | Sets/gets the white balance gain for the red component of the Bayer conversion. |
| BayerPattern | Acquisition Attributes : Bayer : Pattern |  | Sets/gets the Bayer pattern to use. |
| StreamChannelMode | Acquisition Attributes : Controller : Stream Channel Mode |  | Gets/sets the mode for allocating a FireWire stream channel. |
| DesiredStreamChannel | Acquisition Attributes : Controller : Desired Stream Channel |  | Gets/sets the stream channel to manually allocate. |
| FrameInterval | Acquisition Attributes : Frame Interval |  | Read only. Gets the duration in milliseconds between successive frames. |
| IgnoreFirstFrame | Acquisition Attributes : Ignore First Frame |  | Gets/sets the video delay of one frame between starting the camera and receiving the video feed. |
| OffsetX | Acquisition Attributes : Offset X |  | Gets/sets the left offset of the image. |
| OffsetY | Acquisition Attributes : Offset Y |  | Gets/sets the top offset of the image. |
| Width | Acquisition Attributes : Width |  | Gets/sets the width of the image. |
| Height | Acquisition Attributes : Height |  | Gets/sets the height of the image. |
| PixelFormat | Acquisition Attributes : Pixel Format |  | Gets/sets the pixel format of the source sensor. |
| AttributePixelSignedness | Acquisition Attributes : Pixel Signedness |  | Gets/sets the signedness of the pixel. For 16-bit components, this represents the actual pixel signedness (Signed, or Unsigned). |
| PacketSize | Acquisition Attributes : Packet Size |  | Gets/sets the packet size in bytes. |
| PayloadSize | Acquisition Attributes : Payload Size |  | Gets/sets the frame size in bytes. |
| Speed | Acquisition Attributes : Speed |  | Gets/sets the transfer speed in Mbps for a FireWire packet. |
| ShiftPixelBits | Acquisition Attributes : Shift Pixel Bits |  | Gets/sets the alignment of 16-bit cameras. Downshift the pixel bits if the camera returns most significant bit-aligned data. |
| SwapPixelBytes | Acquisition Attributes : Swap Pixel Bytes |  | Gets/sets the endianness of 16-bit cameras. Swap the pixel bytes if the camera returns little endian data. |
| OverwriteMode | Acquisition Attributes : Overwrite Mode |  | Gets/sets the overwrite mode, used to determine acquisition when an image transfer cannot be completed due to an overwritten internal buffer. |
| Timeout | Acquisition Attributes : Timeout |  | Gets/sets the timeout value in milliseconds, used to abort an acquisition when the image transfer cannot be completed within the delay. |
| VideoMode | Acquisition Attributes : Video Mode |  | Gets/sets the video mode for a camera. |
| BitsPerPixel | Acquisition Attributes : Bits Per Pixel |  | Gets/sets the actual bits per pixel. For 16-bit components, this represents the actual bit depth (10-, 12-, 14-, or 16-bit). |
| ReserveDualPackets | Acquisition Attributes : Reserve Dual Packets |  | Gets/sets if dual packets will be reserved for a very large FireWire packet. |
| ReceiveTimestampMode | Acquisition Attributes : Receive Timestamp Mode |  | Gets/sets the mode for timestamping images received by the driver. |
| ActualPeakBandwidth | Acquisition Attributes : Advanced Ethernet : Bandwidth Control : Actual Peak Bandwidth |  | Read only. Returns the actual maximum peak bandwidth the camera will be configured to use. |
| DesiredPeakBandwidth | Acquisition Attributes : Advanced Ethernet : Bandwidth Control : Desired Peak Bandwidth |  | Gets/sets the desired maximum peak bandwidth the camera should use. |
| DestinationMode | Acquisition Attributes : Advanced Ethernet : Controller : Destination Mode |  | Gets/Sets where the camera is instructed to send the image stream. |
| DestinationMulticastAddress | Acquisition Attributes : Advanced Ethernet : Controller : Destination Multicast Address |  | Gets/Sets the multicast address the camera should send data in multicast mode. |
| AttributeEventsEnabled | Acquisition Attributes : Advanced Ethernet : EventsEnabled |  | Gets/Sets if events will be handled. |
| AttributeMaxOutstandingEvents | Acquisition Attributes : Advanced Ethernet : MaxOutstandingEvents |  | Gets/Sets the maximum number of outstanding events to queue. |
| LostPacketMode | Acquisition Attributes : Advanced Ethernet : Lost Packet Mode |  | Gets/sets the behavior when the user extracts a buffer that has missing packets. |
| MemoryWindowSize | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Memory Window Size |  | Gets/sets the size of the memory window of the camera in kilobytes. Should match the camera's internal buffer size. |
| ResendsEnabled | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Resends Enabled |  | Gets/sets if resends will be issued for missing packets. |
| ResendThresholdPercentage | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Resend Threshold Percentage |  | Gets/sets the threshold of the packet processing window that will trigger packets to be resent. |
| ResendBatchingPercentage | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Resend Batching Percentage |  | Gets/sets the percent of the packet resend threshold that will be issued as one group past the initial threshold sent in a single request. |
| MaxResendsPerPacket | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Max Resends Per Packet |  | Gets/sets the maximum number of resend requests that will be issued for a missing packet. |
| ResendResponseTimeout | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Resend Response Timeout |  | Gets/sets the time to wait for a resend request to be satisfied before sending another. |
| NewPacketTimeout | Acquisition Attributes : Advanced Ethernet : Resend Parameters : New Packet Timeout |  | Gets/sets the time to wait for new packets to arrive in a partially completed image before assuming the rest of the image was lost. |
| MissingPacketTimeout | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Missing Packet Timeout |  | Gets/sets the time to wait for a missing packet before issuing a resend. |
| ResendTimerResolution | Acquisition Attributes : Advanced Ethernet : Resend Parameters : Resend Timer Resolution |  | Gets/sets the resolution of the packet processing system that is used for all packet-related timeouts. |
| AttributeTestPacketEnabled | Acquisition Attributes : Advanced Ethernet : TestPacketParameters : TestPacketEnabled |  |  |
| AttributeTestPacketTimeout | Acquisition Attributes : Advanced Ethernet : TestPacketParameters : TestPacketTimeout |  |  |
| AttributeMaxTestPacketRetries | Acquisition Attributes : Advanced Ethernet : TestPacketParameters : MaxTestPacketRetries |  |  |
| AttributeChunkDataDecodingEnabled | AcquisitionAttributes : ChunkDataDecoding : ChunkDataDecodingEnabled |  |  |
| AttributeChunkDataDecodingMaxElementSize | AcquisitionAttributes : ChunkDataDecoding : MaximumChunkCopySize |  |  |
| ActiveAttribute | Camera Attributes : Active Attribute |  | Gets/sets the active attribute |
| ValueU32 | Camera Attributes : Value : U32 |  | Gets/sets the current value as an integer for the active attribute. |
| ValueI64 | Camera Attributes : Value : I64 |  | Gets/sets the current value as a 64-bit integer for the active attribute. |
| ValueDBL | Camera Attributes : Value : DBL |  | Gets/sets the current value as a double precision floating point number for the active attribute. |
| ValueString | Camera Attributes : Value : String |  | Gets/sets the current value as a string for the active attribute. |
| ValueBool | Camera Attributes : Value : Bool |  | Gets/sets the current value as a boolean for the active attribute. |
| MinU32 | Camera Attributes : Minimum : U32 |  | Read only. Gets the current minimum as an integer for the active attribute. |
| MinI64 | Camera Attributes : Minimum : I64 |  | Read only. Gets the current minimum as a 64-bit integer for the active attribute. |
| MinDBL | Camera Attributes : Minimum : DBL |  | Read only. Gets the current minimum as a double precision floating point number for the active attribute. |
| MinString | Camera Attributes : Minimum : String |  | Read only. Gets the current minimum as a string for the active attribute. |
| MaxU32 | Camera Attributes : Maximum : U32 |  | Read only. Gets the current maximum as an integer for the active attribute. |
| MaxI64 | Camera Attributes : Maximum : I64 |  | Read only. Gets the current maximum as a 64-bit integer for the active attribute. |
| MaxDBL | Camera Attributes : Maximum : DBL |  | Read only. Gets the current maximum as a double precision floating point number for the active attribute. |
| MaxString | Camera Attributes : Maximum : String |  | Read only. Gets the current maximum as a string for the active attribute.- |
| Type | Camera Attributes : Type |  | Read only. Gets the active type for the active attribute. |
| EnumValues[] | Camera Attributes : Enum : Values[] |  | Read only. Returns an array of enum attribute values for the active attribute. |
| EnumStrings[] | Camera Attributes : Enum : Strings[] |  | Read only. Returns an array of enum attribute strings for the active attribute. |
| IsReadable | Camera Attributes : Is Readable |  | Read only. Gets the read access for the active attribute. TRUE if readable; otherwise FALSE. |
| IsWritable | Camera Attributes : Is Writable |  | Read only. Gets the write access for the active attribute. TRUE if writable; otherwise FALSE. |
| IncU32 | Camera Attributes : Increment : U32 |  | Read only. Gets the increment as an integer for the active attribute. |
| IncI64 | Camera Attributes : Increment : I64 |  | Read only. Gets the increment as a 64-bit integer for the active attribute. |
| IncDBL | Camera Attributes : Increment : DBL |  | Read only. Gets the increment as a double precision floating point number for the active attribute. |
| IncString | Camera Attributes : Increment : String |  | Read only. Gets the increment as a string for the active attribute. |
| Tooltip | Camera Attributes : Tooltip |  | Read only. Gets the tooltip for the active attribute. |
| Units | Camera Attributes : Units |  | Read only. Gets the units for the active attribute. |
| Visibility | Camera Attributes : Visibility |  | Read only. Gets the visibility for the active attribute. |
| Description | Camera Attributes : Description |  | Read only. Gets the description for the active attribute. |
| DisplayName | Camera Attributes : Display Name |  | Read only. Gets the display name for the active attribute. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_property_node.html language=enus -->
## TOPIC 00021: Property Node

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_property_node.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_property_node.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### Property Node

Gets (reads) and/or sets (writes) properties of a reference. The Property Node automatically adapts to the class of the object that you **reference**. LabVIEW includes Property Nodes preconfigured to access VISA properties, .NET properties, and ActiveX properties. [Details](#details)

[IMAGE alt='image' src='propnode.gif']

|  | reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node. |
| --- | --- |
|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source specifies the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | property 2..n are examples of properties you want to set (write). |
|  | reference out returns reference unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. |
|  | property 1..n are examples of properties you want to get (read). |

#### Property Node Details

To select the class on which to execute the property, wire the refnum to the **reference** input. For example, to select the VI, Generic, or Application class, wire the VI, VI object, or application refnum to the **reference** input. The node adapts to the class automatically. You also can right-click the node and select a class from the shortcut menu.

Move the cursor over terminals in the Property Node to display more information about the property in the Context Help window. You also can right-click a property terminal and select **Help For *Property*** from the shortcut menu, where ***Property*** is the name of the property.

To get property information, right-click the node and select **Change All to Read** from the shortcut menu. To set property information, right-click the node and select **Change All to Write** from the shortcut menu. If a property is read only, **Change to Write** is dimmed in the shortcut menu.

The node executes each terminal in order from top to bottom. If an error occurs on a terminal, the node stops at that terminal, returns an error, and does not execute any further terminals. You can right-click the node and select **Ignore Errors Inside Node** from the shortcut menu to ignore any errors and continue executing further terminals. If an error occurs when **Ignore Errors Inside Node** is set, the property node still returns that error. The **error out** cluster reports which property caused the error.

If the small direction arrow on the property is on the right, you are getting the property value. If the small direction arrow on a property is on the left, you are setting the property value. Properties have a short or long name that you can change by right-clicking and selecting **Name Format** from the shortcut menu. The **No Names** format displays only the data type for each property.

##### ActiveX Property Node (Windows)

If the property you want to write is variant, you can wire in LabVIEW data types and they automatically convert to variant data types indicated by a coercion dot. ActiveX does not support 64-bit integer data types. If you wire a 64-bit integer data type to a variant parameter of an ActiveX Property Node, LabVIEW converts the data type to a double-precision, floating-point number. If the property is variant, use the Variant To Data function to convert to a LabVIEW data type, if needed. If you right-click the Property Node and select **Select Class»ActiveX»Browse** from the shortcut menu, LabVIEW displays the Select Object From Type Library dialog box.

On the front panel or block diagram, right-click an ActiveX object, select **Create»Property Node**, and select a property from the shortcut menu to set a property for the object. You also can select ActiveX-specific properties for an ActiveX object. On the block diagram, right-click an ActiveX object, select **Create»Property Node**, and select an ActiveX-specific property from the shortcut menu.

##### .NET Property Node (Windows)

If you right-click the Property Node and select **Select Class».NET»Browse** from the shortcut menu, LabVIEW displays the Select Object From Assembly dialog box.

On the front panel or block diagram, right-click a .NET object, select **Create»Property Node**, and select a property from the shortcut menu to set a property for the object. You also can select .NET-specific properties for a .NET object. On the block diagram, right-click a .NET object, select **Create»Property Node**, and select a .NET-specific property from the shortcut menu.

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_read_attributes.html language=enus -->
## TOPIC 00022: IMAQdx Read Attributes VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_read_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_read_attributes.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Read Attributes VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Loads a configuration file for a camera.

[IMAGE alt='IMAQdx Read Attributes' src='imaqdx_read_attributes.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Filename specifies the name of the source file to read from. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_read_memory2.html language=enus -->
## TOPIC 00023: IMAQdx Read Memory2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_read_memory2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_read_memory2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Read Memory2 VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Accesses registers on the camera and reads a string from the camera.

[IMAGE alt='IMAQdx Read Memory2' src='imaqdx_read_memory2.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Offset is the register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use the Property Node Properties»Camera Information»Base Address to get the base address for your camera. |
|  | Memory Size specifies the number of bytes to read. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Value specifies the string read from the memory offset. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_read_register2.html language=enus -->
## TOPIC 00024: IMAQdx Read Register2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_read_register2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_read_register2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Read Register2 VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Accesses registers on the camera and reads a 32-bit value from the camera. Data is byte-swapped for little endian alignment after transfer.

[IMAGE alt='IMAQdx Read Register2' src='imaqdx_read_register2.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Offset is the register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use the Property Node Properties»Camera Information»Base Address to get the base address for your camera. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Value specifies the 32-bits of data read from the register offset. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_register_events.html language=enus -->
## TOPIC 00025: Register For Events

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_register_events.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_register_events.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### Register For Events

Dynamically registers events. The events for which you can register depend on the type of the reference you wire to each **event source** input. Refer to the [Details](#details) section for information about NI-IMAQdx events. Wire the **event reg refnum out** output to an Event structure or to another Register For Events function.

[Details](#details)

[IMAGE alt='image' src='regevent.gif']

|  | event registration refnum is a reference to an existing event registration a Register For Events function created. |
| --- | --- |
|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source specifies the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | event source 1..n is a reference to an application, VI, control, or user event. References must be to local objects. You cannot wire a reference to a remote object. If you wire an array or cluster of refnums to this input, LabVIEW registers all elements of the array or cluster for the event. |
|  | event reg refnum out returns the reference to a new or existing event registration. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. |

#### Details

NI-IMAQdx includes the following events:

- AttributeUpdated —Occurs when an attribute value changes. Wire a constant to the Name parameter and enter the name of the attribute you want to monitor.
- FrameDone —Occurs when a frame arrives in memory. Wire a constant to the BufferInterval parameter to specify the number of images to acquire before executing the callback function. Specify a BufferInterval of 1 to receive a callback for every buffer.
- IOSignalEdge —Waits for the desired IO signal.
  - Signal Type
    - TTL
    - RTSI
    - Iso In
    - Iso Out
  - Signal Number
  - Signal Edge
    - Rising Edge
    - Falling Edge
- Plug and Play —Occurs when a Plug and Play event occurs. The following events are valid:
  - Camera Attached —Callback fired when a new camera is attached.
  - Camera Detached —Callback fired when the camera is detached.
  - Bus Reset —Callback fired when a FireWire bus reset occurs.
- Status Signal —Waits for the specified status signal.
  - Acquisition Active
  - Acquisition Done
  - Frame Start
  - Frame Done
  - Buffer Complete

Each **event source** input is a reference to an application, VI, control, or user event. You can right-click each data item and select which event to register for that event source. You can wire the **event reg refnum out** terminal of the Register For Events function to the dynamic event terminals on the Event structure border, to the Unregister For Events function, or to the top left input of another Register For Events function. If you wire the top left input of the Register For Events function, the function modifies the existing registration information associated with that refnum instead of registering the event again.

Registered events stay registered until you explicitly unregister them or until the VI that registered the events finishes running or you abort the VI. If the VI which registered for events was a subVI, events are unregistered when that VI's top-level VI finishes execution or is aborted. If you use the Run VI method to execute a subVI that registered for events, events are unregistered when the subVI finishes execution or is aborted.

|  | Note LabVIEW does not include an event registration refnum on the Controls palette because the event registration refnum is strictly typed and a generic version does not exist. You can create an event registration refnum by configuring a Register For Events function or right-clicking the function and creating a control or indicator from the shortcut menu. You also can select the part of the application that includes the event registration refnum and selecting Edit»Create SubVI to create a subVI from the selection. If you later modify the Register For Events function and change the type of the event registration refnum, you must recreate the control or indicator to match. |
| --- | --- |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_release_image.html language=enus -->
## TOPIC 00026: IMAQdx Release Image VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_release_image.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_release_image.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Release Image VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Releases the specified extracted image, thus allowing the acquisition to proceed.

You can specify the image to release with the **Image** or **Buffer Number In** input. This function is valid only within the context of a ring acquisition.

[IMAGE alt='IMAQdx Release Image' src='imaqdx_release_image.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Image is the reference to the extracted image to release. Image takes precedence over Buffer Number In. |
|  | Buffer Number In is the cumulative image number to release. Use only if Image is unspecified. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_reset_camera.html language=enus -->
## TOPIC 00027: IMAQdx Reset Camera VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_reset_camera.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_reset_camera.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Reset Camera VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Performs a manual reset on a camera. Stops any ongoing acquisitions.

[IMAGE alt='IMAQdx Reset Camera' src='imaqdx_reset_camera.gif']

|  | Reset All? (No) If the value is No, then only the specified camera will be reset. If the Reset All? value is Yes, then all of the connected cameras will be reset. |
| --- | --- |
|  | Session In specifies the name of the camera you wish to reset. The default value is cam0. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_reset_ethernet_camera_address.html language=enus -->
## TOPIC 00028: IMAQdx Reset Ethernet Camera Address VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_reset_ethernet_camera_address.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_reset_ethernet_camera_address.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Reset Ethernet Camera Address VI

Owning Palette:

NI-IMAQdx

Installed With:

Reset Ethernet camera address. Use this function to reset Ethernet cameras on the network with a local subnet. This function will be blocked and will return when the reset is complete or after the specified timeout.

[IMAGE alt='IMAQdx Reset Ethernet Camera Address' src='imaqdx_reset_ethernet_camera_address.gif']

|  | Timeout (1000 ms) specifies the time, in milliseconds, allowed for the Ethernet camera reset to complete. The default timeout is 1000 ms. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Camera Address (0.0.0.0) specifies the new address, subnet and gateway for the Ethernet camera to reset to. Specify a valid address to configure the camera's new address. Specify an empty address to merely reset the camera Ethernet address. The default address is 0.0.0.0. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_sequence2.html language=enus -->
## TOPIC 00029: IMAQdx Sequence2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_sequence2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_sequence2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Sequence2 VI

Owning Palette:

NI-IMAQdx

Installed With:

Configures, starts, acquires, stops, and unconfigures a sequence acquisition. Use this VI to capture multiple images. If you call this VI before calling the IMAQdx Open Camera VI, the IMAQdx Sequence2 VI uses cam0 by default.

[IMAGE alt='IMAQdx Sequence2' src='imaqdx_sequence2.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested image to become available. The default value is 5000. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Images In is the reference to the array of images that receives the captured pixel data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Images Out is the reference to the array of captured images. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_serial_flush.html language=enus -->
## TOPIC 00030: IMAQdx Serial Flush VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_serial_flush.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_serial_flush.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Serial Flush VI

Installed With:

Flushes data from the serial port read buffer on image acquisition devices that support serial communication.

[IMAGE alt='IMAQdx Serial Flush' src='imaqdx_serial_flush.gif']

|  | Session In specifies the name of the camera you wish to open. The default value is cam0. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_serial_read.html language=enus -->
## TOPIC 00031: IMAQdx Serial Read VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_serial_read.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_serial_read.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Serial Read VI

Installed With:

Reads in data from the serial port on image acquisition devices that support serial communication.

[IMAGE alt='IMAQdx Serial Read' src='imaqdx_serial_read.gif']

|  | Timeout (ms) is the time, in milliseconds, to wait for the read to finish. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Data is the string read from the serial port. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_serial_read_bytes.html language=enus -->
## TOPIC 00032: IMAQdx Serial Read Bytes VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_serial_read_bytes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_serial_read_bytes.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Serial Read Bytes VI

Installed With:

Reads in an expected number of bytes from the serial port on image acquisition devices that support serial communication.

[IMAGE alt='IMAQdx Serial Read Bytes' src='imaqdx_serial_read_bytes.gif']

|  | Timeout (ms) is the time, in milliseconds, to wait for the read to finish. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Bytes to Read is the number of bytes to read from the serial port. |
|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Data Bytes is the output of data bytes. |
|  | Bytes Read is the number of bytes stored in Byte Array. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_serial_write.html language=enus -->
## TOPIC 00033: IMAQdx Serial Write VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_serial_write.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_serial_write.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Serial Write VI

Installed With:

Writes data to the serial port.

[IMAGE alt='IMAQdx Serial Write' src='imaqdx_serial_write.gif']

|  | Timeout is the time, in milliseconds, to wait for the write to finish. |
| --- | --- |
|  | Session In specifies the name of the camera you wish to reset. The default value is cam0. |
|  | The Data is the string written to the serial port. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code code is the number identifying an error or warning. If status is TRUE, code is a non-zero error code. If status is FALSE, code can be zero or a warning code. Use the error handler VIs to look up the meaning of this code and to display the corresponding error message. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_snap2.html language=enus -->
## TOPIC 00034: IMAQdx Snap2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_snap2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_snap2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Snap2 VI

Owning Palette:

NI-IMAQdx

Installed With:

Configures, starts, acquires, and unconfigures a snap acquisition. Use a snap for low-speed or single-capture applications where ease of programming is essential. If you call this VI before calling IMAQdx Open Camera.vi, IMAQdx Snap2.vi uses cam0 by default. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format.

[IMAGE alt='IMAQdx Snap2' src='imaqdx_snap2.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested image to become available. The default value is 5000. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Image In is the reference to the image that receives the captured pixel data. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Image Out is the reference to the captured image. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_start_acquisition.html language=enus -->
## TOPIC 00035: IMAQdx Start Acquisition VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_start_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_start_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Start Acquisition VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Starts an acquisition that was previously configured with the [IMAQdx Configure Acquisition](imaqdx_configure_acquisition.html) VI. Use the [IMAQdx Stop Acquisition](imaqdx_stop_acquisition.html) VI to stop the acquisition.

[IMAGE alt='IMAQdx Start Acquisition' src='imaqdx_start_acquisition.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_stop_acquisition.html language=enus -->
## TOPIC 00036: IMAQdx Stop Acquisition VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_stop_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_stop_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Stop Acquisition VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Stops an acquisition previously started with the IMAQdx Start Acquisition VI.

[IMAGE alt='IMAQdx Stop Acquisition' src='imaqdx_stop_acquisition.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_unconfigure_acquisition.html language=enus -->
## TOPIC 00037: IMAQdx Unconfigure Acquisition VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_unconfigure_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_unconfigure_acquisition.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Unconfigure Acquisition VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Unconfigures an acquisition previously configured with the [IMAQdx Configure Acquisition](imaqdx_configure_acquisition.html) VI.

[IMAGE alt='IMAQdx Unconfigure Acquisition' src='imaqdx_unconfigure_acquisition.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_wait.html language=enus -->
## TOPIC 00038: IMAQdx Wait VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_wait.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_wait.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Wait VI

Installed With:

Performs a synchronous wait on the specified event.

#### IMAQdx Wait for Attribute Updated

Synchronous wait for an attribute value change event.

[IMAGE alt='IMAQdx Wait for Attribute Updated' src='imaqdx_wait_for_attribute_updated.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Name specifies the name of the attribute to wait on. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### IMAQdx Wait for Status Signal

Synchronous wait for a Status event.

[IMAGE alt='IMAQdx Wait for Status Signal' src='imaqdx_wait_for_status_signal.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Signal Type specifies the status signal to wait for. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### IMAQdx Wait for IO Signal Edge

Synchronous wait for an edge on an IO signal.

[IMAGE alt='IMAQdx Wait for IO Signal Edge' src='imaqdx_wait_for_io_signal_edge.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Signal Type specifies the IO signal type to wait for. |
|  | Signal Number specifies the line number of the IO signal type to wait for. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Signal Edge lists the Signal Edge. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### IMAQdx Wait for PnP Event

Synchronous wait for a Plug-and-Play event.

[IMAGE alt='IMAQdx Wait for PnP Event' src='imaqdx_wait_for_pnp_event.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | Event specifies the event to wait for. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### IMAQdx Wait for Frame Done

Synchronous wait for the next Frame Done event.

[IMAGE alt='IMAQdx Wait for Frame Done' src='imaqdx_wait_for_frame_done.gif']

|  | Timeout (ms) specifies the time, in milliseconds, to wait for the requested buffer to become available. A value of -1 indicates to wait indefinitely. A value of -2 indicates to use the value of the Timeout attribute in place of this parameter. |
| --- | --- |
|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | Buffer Number specifies on return, the buffer number that corresponds to the Frame Done event. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_write_attributes.html language=enus -->
## TOPIC 00039: IMAQdx Write Attributes VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_write_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_write_attributes.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Write Attributes VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Saves a configuration file for a camera.

[IMAGE alt='IMAQdx Write Attributes' src='imaqdx_write_attributes.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Filename specifies the name of the destination file to write all attributes to. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_write_memory2.html language=enus -->
## TOPIC 00040: IMAQdx Write Memory2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_write_memory2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_write_memory2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Write Memory2 VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Accesses registers on the camera and writes a string to the camera.

[IMAGE alt='IMAQdx Write Memory2' src='imaqdx_write_memory2.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Offset is the register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use the Property Node Properties»Camera Information»Base Address to get the base address for your camera. |
|  | Value specifies the string to write to the memory offset. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/imaqdx_write_register2.html language=enus -->
## TOPIC 00041: IMAQdx Write Register2 VI

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/imaqdx_write_register2.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/imaqdx_write_register2.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### IMAQdx Write Register2 VI

Owning Palette:

NI-IMAQdx Low-Level

Installed With:

Accesses registers on the camera and writes a 32-bit value to the camera. Data is byte-swapped for big endian alignment before transfer.

[IMAGE alt='IMAQdx Write Register2' src='imaqdx_write_register2.gif']

|  | Session In is a unique reference to the camera, which you can obtain with the IMAQdx Open Camera VI. |
| --- | --- |
|  | Offset is the register location to access. Refer to the camera documentation for more information about camera-specific register ranges. Use the Property Node Properties»Camera Information»Base Address to get the base address for your camera. |
|  | Value specifies the 32-bits of data to write to the register offset. |
|  | error in describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Explain Error (or Explain Warning) gives more information about the error displayed. status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Session Out is a unique reference to the camera. Session Out is the same as Session In. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI produces. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/ni-imaqdx_fpga_pal.html language=enus -->
## TOPIC 00042: NI-IMAQdx FPGA

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/ni-imaqdx_fpga_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/ni-imaqdx_fpga_pal.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI-IMAQdx FPGA

Owning Palette:

NI-IMAQdx

Installed With:

Use NI-IMAQdx FPGA VIs to configure and transfer images aquired with NI-IMAQdx to an FPGA target.

| Palette Object | Description |
| --- | --- |
| IMAQdx Get Bayer Parameters for FPGA | Queries the host machine for the Bayer algorithm, pattern, and the red, green and blue color gains used to create an image. Outputs a raw Bayer image with information about how to decode it on the FPGA target. Use this VI to produce a color image that the FPGA target can process. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/ni-imaqdx_low-level_pal.html language=enus -->
## TOPIC 00043: NI-IMAQdx Low-Level

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/ni-imaqdx_low-level_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/ni-imaqdx_low-level_pal.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI-IMAQdx Low-Level

Owning Palette:

NI-IMAQdx

Installed With:

Use the NI-IMAQdx low-level VIs to set up image acquisition systems and acquire images. These VIs allow you to acquire images and open and close an interface.

| Palette Object | Description |
| --- | --- |
| IMAQdx Configure Acquisition | Configures a low-level acquisition previously opened with IMAQdx Open Camera VI. Specify the acquisition type with the Continuous? and Number of Buffers parameters. Snap: Continuous = 0; Buffer Count = 1 Sequence: Continuous = 0; Buffer Count > 1 Grab: Continuous = 1; Buffer Count > 1 |
| IMAQdx Configure Ring Acquisition | Configures a ring acquisition. A ring acquisition is an acquisition in which the image is acquired directly into the images in the Images array. |
| IMAQdx Start Acquisition | Starts an acquisition that was previously configured with the IMAQdx Configure Acquisition VI. Use the IMAQdx Stop Acquisition VI to stop the acquisition. |
| IMAQdx Stop Acquisition | Stops an acquisition previously started with the IMAQdx Start Acquisition VI. |
| IMAQdx Unconfigure Acquisition | Unconfigures an acquisition previously configured with the IMAQdx Configure Acquisition VI. |
| IMAQdx Get Image2 | Acquires the specified frame into Image Out. Call this VI only after calling the IMAQdx Configure Acquisition VI. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format. |
| IMAQdx Get Image Data | Copies the raw data of the specified frame into Image Data Array. Call this VI only after calling the IMAQdx Configure Acquisition VI. |
| IMAQdx Extract Image | Retrieves an acquired image directly from the circular buffer list, and does not make a copy of the image. This function is valid only within the context of a ring acquisition. |
| IMAQdx Release Image | Releases the specified extracted image, thus allowing the acquisition to proceed. |
| IMAQdx Read Register2 | Accesses registers on the camera and reads a 32-bit value from the camera. Data is byte-swapped for little endian alignment after transfer. |
| IMAQdx Write Register2 | Accesses registers on the camera and writes a 32-bit value to the camera. Data is byte-swapped for big endian alignment before transfer. |
| IMAQdx Read Memory2 | Accesses registers on the camera and reads a string from the camera. |
| IMAQdx Write Memory2 | Accesses registers on the camera and writes a string to the camera. |
| IMAQdx Read Attributes | Loads a configuration file for a camera. |
| IMAQdx Write Attributes | Saves a configuration file for a camera. |
| IMAQdx Reset Camera | Performs a manual reset on a camera. Stops any ongoing acquisitions. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/ni-imaqdx_pal.html language=enus -->
## TOPIC 00044: NI-IMAQdx

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/ni-imaqdx_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/ni-imaqdx_pal.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### NI-IMAQdx

Installed With:

Use NI-IMAQdx VIs to set up your Vision system and acquire images. The high-level NI-IMAQdx VIs allow you to acquire images, open and close an interface, get/set attributes, get camera features and video modes, transfer images to an FPGA target, and configure triggered acquisitions.

| Palette Object | Description |
| --- | --- |
| IMAQdx Snap2 | Configures, starts, acquires, and unconfigures a snap acquisition. Use a snap for low-speed or single-capture applications where ease of programming is essential. If you call this VI before calling IMAQdx Open Camera.vi, IMAQdx Snap2.vi uses cam0 by default. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format. |
| IMAQdx Configure Grab | Configures and starts a grab acquisition. A grab performs an acquisition that loops continually on a ring of buffers. Use the grab VI for high-speed image acquisition. Use the IMAQdx Grab VI to copy an image out of the buffer. If you call this VI before calling the IMAQdx Open Camera VI, the IMAQdx Configure Grab VI uses cam0 by default. Use the IMAQdx Unconfigure Acquisition VI to unconfigure the acquisition. |
| IMAQdx Grab2 | Acquires the most current frame into Image Out. Call this VI only after calling IMAQdx Configure Grab.vi. If the image type does not match the video format of the camera, this VI changes the image type to a suitable format. |
| IMAQdx Sequence2 | Configures, starts, acquires, stops, and unconfigures a sequence acquisition. Use this VI to capture multiple images. If you call this VI before calling the IMAQdx Open Camera VI, the IMAQdx Sequence2 VI uses cam0 by default. |
| IMAQdx Open Camera | Opens a camera, queries the camera for its capabilities, loads a camera configuration file, and creates a unique reference to the camera. Use the IMAQdx Close Camera VI when you are finished with the reference. |
| IMAQdx Close Camera | Stops an acquisition in progress, releases resources associated with an acquisition, and closes the specified Camera Session. |
| IMAQdx Enumerate Cameras | Returns a list of all cameras on the host computer. |
| IMAQdx Enumerate Attributes | Gets the attributes supported by the camera. |
| IMAQdx Enumerate Video Modes | Returns a list of video modes supported by the camera. |
| IMAQdx Discover Ethernet Cameras | Initiates a round of Ethernet camera discovery. Use this VI to find Ethernet cameras on the network with a remote subnet. This VI will be blocked and will return after the specified timeout. The address specifies the destination address for the discovery command. The default address is 255.255.255.255. Call this VI before calling IMAQdx Enumerate Cameras VI or IMAQdx Open Camera VI. |
| IMAQdx Reset Ethernet Camera Address | Reset Ethernet camera address. Use this function to reset Ethernet cameras on the network with a local subnet. This function will be blocked and will return when the reset is complete or after the specified timeout. |
| IMAQdx Calculate Frames Per Second | Calculates the acquired and processing frame rate, the images behind, and images missed. This VI operates on a per-session basis, so it can be called with different IMAQdx camera sessions in parallel and it will return the calculated values for the session passed in. |

| Subpalette | Description |
| --- | --- |
| NI-IMAQdx Low-Level | Use the NI-IMAQdx low-level VIs to set up image acquisition systems and acquire images. These VIs allow you to acquire images and open and close an interface. |
| NI-IMAQdx FPGA | Use NI-IMAQdx FPGA VIs to configure and transfer images aquired with NI-IMAQdx to an FPGA target. |

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/ni-imaqdx_vi_reference_help.html language=enus -->
## TOPIC 00045: NI-IMAQdx VI Reference Help

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/ni-imaqdx_vi_reference_help.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/ni-imaqdx_vi_reference_help.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### NI-IMAQdx VI Reference Help

July 2021, 371969N-01

NI-IMAQdx is driver software that supports NI 177x smart cameras, as well as IEEE 1394, GigE Vision, DirectShow-compatible USB, USB3 Vision, and IP cameras. This help file describes the VIs included in the NI-IMAQdx driver software.

For more information about this help file, refer to the following topics:

[Related Documentation](bp_related_documentation.html)

[Glossary](bp_glossary.html)

[NI Services](bp_technical_support_resources.html)

© 2006–2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=ni-imaqdx-vi-ref path=ni-imaqdx_vi_reference/vision_express_pal.html language=enus -->
## TOPIC 00046: Vision Express VIs

- bundle_id: `ni-imaqdx-vi-ref`
- source_path: `ni-imaqdx_vi_reference/vision_express_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-imaqdx-vi-ref/raw/resource/enus/ni-imaqdx_vi_reference/vision_express_pal.html
- document_id: `ni-imaqdx-vi-ref`
- page_type: `leaf`
- content_type: ``

### Vision Express

Use the Vision Express VIs to quickly develop common image acquisition and processing applications.

| Palette Object | Description |
| --- | --- |
| Vision Assistant Express VI | Use NI Vision Assistant from within the LabVIEW environment to perform common image processing tasks. You must install the NI Vision Development Module to use the Vision Assistant Express VI. |
| Vision Acquisition Express VI | Acquires images from cameras using NI-IMAQ or NI-IMAQdx. Refer to the NI Vision Acquisition Express VI Help for more information. |
