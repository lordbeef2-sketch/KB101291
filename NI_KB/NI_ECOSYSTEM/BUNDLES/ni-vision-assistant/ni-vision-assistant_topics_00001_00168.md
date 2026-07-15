# NI DOCUMENT BUNDLE: ni-vision-assistant

<!--NI_BUNDLE_CHUNK bundle=ni-vision-assistant start=1 end=168 -->
<!--NI_TOPIC bundle=ni-vision-assistant path=access-images-from-the-reference-window.html language=enus -->
## TOPIC 00001: Access Images from the Reference Window

- bundle_id: `ni-vision-assistant`
- source_path: `access-images-from-the-reference-window.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/access-images-from-the-reference-window.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Reference Window controls to navigate the images in the Image Browser and select one to process. Click the Make Image Active button to process the image shown in the Reference window.

### Access Images from the Reference Window

1. Use the Reference Window controls to navigate the images in the Image Browser and select one to process.
2. Click the Make Image Active 
 button
 to process the image shown in the
 Reference window.

Parent topic:

Managing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=acquire-images-in-color.html language=enus -->
## TOPIC 00002: Acquire Images in Color

- bundle_id: `ni-vision-assistant`
- source_path: `acquire-images-in-color.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquire-images-in-color.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Acquire Image. Vision Assistant displays the Acquisition window. Click the appropriate acquisition step. The Devices window displays all image acquisition devices and channels or ports available for the computer. Select an image acquisition device in the Parameter window. You must have a

### Acquire Images in Color

1. Click File»Acquire Image . Vision Assistant displays the
 Acquisition window.
2. Click the appropriate acquisition step. The Devices window displays all
 image acquisition devices and channels or ports
 available for the computer.
3. Select an image acquisition device in the Parameter window. Note You must have a
 PCI/PXI-1411, PCI/PXI-1422, PCI-1424, PCI/PXI-1428, or PCIe-1430 device
 installed to acquire color images. The PCI/PXI-1422 and PCI-1424 must be
 attached to a color digital camera to acquire color images.
4. Click the Acquire Single Image button, Acquire Continuous Image button, or Sequence Acquisition button.
5. Process the images as you would any other image in Vision Assistant.

Parent topic:

Acquiring Images

Related concepts:

- Snapping an Image (Single Image Acquisition)
- Grabbing an Image (Continuous Image Acquisition)
- Acquiring a Sequence of Images
- Acquire Images

<!--NI_TOPIC bundle=ni-vision-assistant path=acquire-images-on-a-remote-target.html language=enus -->
## TOPIC 00003: Acquire Images on a Remote Target

- bundle_id: `ni-vision-assistant`
- source_path: `acquire-images-on-a-remote-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquire-images-on-a-remote-target.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Target, select the computer you want to use to acquire images. Select the device you want to use to acquire the image. Click the Parameters tab. If you want to compress the acquired images, select Compress Images and set the Image Quality. Click Acquire Single Image or click Acquire Continuous Im

### Acquire Images on a Remote Target

1. In Target , select the computer you want to use to acquire images.
2. Select the device you want to use to acquire the image.
3. Click the Parameters tab.
4. If you want to compress the acquired images, select Compress Images and set the Image Quality .
5. Click Acquire Single Image or click Acquire Continuous Images .
6. Click Close to exit the Setup window.

Parent topic:

Acquiring Images

<!--NI_TOPIC bundle=ni-vision-assistant path=acquire-images-with-an-ieee-1394-gige-vision.html language=enus -->
## TOPIC 00004: Acquire Images with an IEEE 1394, GigE Vision, or DirectShow-Compatible USB Camera

- bundle_id: `ni-vision-assistant`
- source_path: `acquire-images-with-an-ieee-1394-gige-vision.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquire-images-with-an-ieee-1394-gige-vision.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Target control, select the computer you want to use to acquire images. In the Devices list, select the device you want to use to acquire an image. For IEEE 1394 cameras, select the IEEE 1394 Video Mode you want to use. Attributes Tab Select and configure each camera feature you want

### Acquire Images with an IEEE 1394, GigE Vision, or DirectShow-Compatible USB Camera

#### Main Tab

1. In the Target control, select the computer you want to
 use to acquire images.
2. In the Devices list, select the device you want to use to
 acquire an image.
3. For IEEE 1394 cameras, select the IEEE 1394 Video Mode 
 you want to use.

#### Attributes Tab

1. Select and configure each camera feature you want to use for the
 acquisition.
2. Click the Acquire Single Image , Acquire Continuous
 Images , or Sequence Acquisition button.
3. Click Close to exit the Setup 
 window.

Parent topic:

Acquiring Images

Related concepts:

- Snapping an Image (Single Image Acquisition)
- Grabbing an Image (Continuous Image Acquisition)
- Acquiring a Sequence of Images

<!--NI_TOPIC bundle=ni-vision-assistant path=acquire-images-with-an-ni-smart-camera.html language=enus -->
## TOPIC 00005: Acquire Images with a Smart Camera

- bundle_id: `ni-vision-assistant`
- source_path: `acquire-images-with-an-ni-smart-camera.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquire-images-with-an-ni-smart-camera.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main TabIn the Target drop-down listbox, choose Select Network Target or select a configured smart camera to acquire images from. Trigger Tab Select Triggered Acquisition if you want to start the image capture with a trigger. The trigger signal must be connected to the trigger line of the 17xx. Refe

### Acquire Images with a Smart Camera

#### Main
 Tab

In the Target drop-down listbox, choose
 Select Network Target or select a configured smart camera
 to acquire images from.

#### Trigger Tab

1. Select Triggered Acquisition if you want to start the
 image capture with a trigger. Note The trigger signal must be
 connected to the trigger line of the 17xx. Refer to the 17xx User Manual for
 information about connecting signals to the 17xx.
2. Select the trigger polarity. Select Rising Edge if you
 want to start the acquisition of a new image on the rising edge of the trigger
 signal. Select Falling Edge if you want to start the
 acquisition of a new image on the falling edge of the trigger signal.
3. Enter a Timeout value. If a trigger signal is not
 received within the timeout period, the step fails.
4. Select the Acquisition Mode you want to use for the
 acquisition.

#### Lighting Tab

- If you want to use the internal Direct Drive lighting controller, enable the
 Enable Direct Drive control and select the
 light connected to the smart camera.
- If you want to use an external lighting controller with the 17xx, use the
 5 V TTL Strobe or 24 V Strobe 
 control, depending on the voltage your lighting controller requires, to generate
 strobe signals for the lighting controller.

#### Compression Tab

Select the level of compression to apply to
 images.

Parent topic:

Acquiring Images

Related information:

- Select the Light

<!--NI_TOPIC bundle=ni-vision-assistant path=acquire-images.html language=enus -->
## TOPIC 00006: Acquire Images

- bundle_id: `ni-vision-assistant`
- source_path: `acquire-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquire-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Target, select the computer you want to use to acquire images. Select the device you want to use to acquire the image. Click the Parameters tab. If you want to start the image capture with a trigger, enable the Triggered Acquisition checkbox. The trigger signal must be connected to a trigger line

### Acquire Images

1. In Target , select the computer you want to use to acquire images.
2. Select the device you want to use to acquire the image.
3. Click the Parameters tab.
4. If you want to start the image capture with a trigger, enable the Triggered
 Acquisition checkbox. Note The trigger signal must be
 connected to a trigger line of the image acquisition device. 
 Caution The trigger
 input lines of image acquisition devices expect TTL signals and are not
 isolated. Do not provide anything other than TTL signals on these lines. Doing
 so could permanently damage the image acquisition device.
5. If you want to compress the acquired images, select Compress Images and set the Image Quality .
6. Click Acquire Single Image or click Acquire Continuous Images .
7. Click Close to exit the Setup window.

Parent topic:

Acquiring Images

Related concepts:

- Acquire Images in Color

<!--NI_TOPIC bundle=ni-vision-assistant path=acquiring-a-sequence-of-images.html language=enus -->
## TOPIC 00007: Acquiring a Sequence of Images

- bundle_id: `ni-vision-assistant`
- source_path: `acquiring-a-sequence-of-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquiring-a-sequence-of-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Acquire Image. Vision Assistant displays the Acquisition Interface window and acquisition property pages. Click the appropriate acquisition step. The Devices window displays all image acquisition devices and channels or ports available for the computer. Select the device and channel or po

### Acquiring a Sequence of Images

1. Click File»Acquire Image . Vision Assistant displays the
 Acquisition Interface window and
 acquisition property pages.
2. Click the appropriate acquisition step. The Devices window displays all
 image acquisition devices and channels or ports available for the
 computer.
3. Select the device and channel or port you want to use to acquire an image.
4. Select Sequence Acquisition 
 to view the
 Sequence Acquisition Wizard.
5. Set the following properties in the Sequence Acquisition Wizard:
 
 For example, if you have a camera that acquires 30 frames per second (f/s) and you want to acquire an image every second until you acquire 10 images in the sequence, set Number of Frames to 10 and Skip Count to 29 (30 f/s–1 frame acquired in the sequence).
  - Number of Frames — Number of frames you want to acquire.
  - Skip Count — Number of frames you want to skip between acquisitions.
  - Action — Triggering action. Select Disabled ,
 Trigger start of acquisition , or
 Trigger each image .
  - Line — Physical trigger line.
  - Timeout — Time, in milliseconds, within which the trigger must
 occur.
  - Polarity — Edge of the signal at which the trigger occurs.
6. Click Next , Next , and Finish to complete the sequence acquisition. Vision Assistant sends acquired images to the Image Browser.
7. Process the images as you would any other image in Vision Assistant.

Parent topic:

Acquiring Images

Related concepts:

- Acquire Images in Color
- Grabbing an Image (Continuous Image Acquisition)
- Image Acquisition in Vision Assistant
- Snapping an Image (Single Image Acquisition)

<!--NI_TOPIC bundle=ni-vision-assistant path=acquiringimages.html language=enus -->
## TOPIC 00008: Acquiring Images

- bundle_id: `ni-vision-assistant`
- source_path: `acquiringimages.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/acquiringimages.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`

### Acquiring Images

- [Image Acquisition in Vision Assistant](image-acquisition-in-vision-assistant.html)
- [Acquire Images](acquire-images.html)
- [Acquire Images in Color](acquire-images-in-color.html)
- [Acquire Images with an IEEE 1394, GigE Vision, or DirectShow-Compatible USB Camera](acquire-images-with-an-ieee-1394-gige-vision.html)
- [Acquire Images on a Remote Target](acquire-images-on-a-remote-target.html)
- [Acquire Images with a Smart Camera](acquire-images-with-an-ni-smart-camera.html)
- [Acquiring a Sequence of Images](acquiring-a-sequence-of-images.html)
- [Snapping an Image (Single Image Acquisition)](snapping-an-image-single-image-acquisition.html)
- [Grabbing an Image (Continuous Image Acquisition)](grabbing-an-image-continuous-image-acquisitio.html)
- [Configuring Remote Targets](configuring-remote-targets.html)
- [How to Acquire Images with a USB Device](how-to-acquire-images-with-a-usb-device.html)
- [How to Simulate an Image Acquisition](how-to-simulate-an-image-acquisition.html)

<!--NI_TOPIC bundle=ni-vision-assistant path=activating-your-software.html language=enus -->
## TOPIC 00009: Activating Your Software

- bundle_id: `ni-vision-assistant`
- source_path: `activating-your-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/activating-your-software.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: How Do I Activate My Software? Before using your product, you must activate it in accordance with its license agreement. To activate a product, you must first purchase a license. For information on purchasing licenses, contact your local NI sales representative or visit ni.com/niglobal. Complete the

### Activating Your Software

#### How Do I Activate My
 Software?

Before using your product, you must activate it in accordance with its license
 agreement. To
 activate a product, you must first purchase a license. For information on purchasing
 licenses, contact your local NI sales representative or visit
 ni.com/niglobal.

Complete the following steps to activate your NI products:

1. Select Start»National Instruments»NI License Manager to
 open NI License Manager.
2. Select one of the following methods to launch the Activate Software window: 
 Note The first time
 you open NI software, the license activation window launches automatically.
  - Click Activate Software on the ribbon.
  - When in the Local Licenses view, right-click the
 product in the License tree and select
 Activate .
3. If requested, log in to your NI User Account. If you do not have a User Account,
 you must create one.
4. Select one of the following methods to activate your products.
  - Check my account for licenses 
 Licenses associated with your account are verified successfully,
 activation completes. If your account lacks the appropriate licenses
 for a particular product, proceed to activate the product using
 either a activation code or a serial number.
  - Enter a serial number 
 You can find your serial numbers in the following locations:
    - On the Certificate of Ownership included in your software
 kit
    - On the product packing slip or shipping label
    - Visit ni.com/info and enter the Info Code
 SerialNumbers_en.
    - If you have installed a previous version of your application
 software using your serial number, you can find the serial
 number by selecting Help»About within the
 application.
    - Contact your local NI
 branch.
  - Enter activation codes 
 Click on Generate an activation code or visit
 ni.com/activate to obtain an activation code.
  - Connect to a volume license server 
 Enter the name of the volume license server on which your NI products
 should check for licenses.
5. Follow the prompts in the Activate Software window to
 complete activation.

If you activated through your NI software, you can use the product immediately after
 successful activation.

Note

- If you were using NI software before you began the activation process, you
 may need to restart the software for the change to take effect.
- If your NI software is licensed through a volume license agreement, you do
 not need to activate your product. Instead, you need to point NI License
 Manager to a volume license server. For more information, refer to the
 Using a Volume License Server topic of the
 NI License Manager Help .

#### What Is Activation?

Activation is the process of obtaining an activation code to enable your software to run on your computer. An activation code is an alphanumeric string that verifies the software, version, and computer ID to enable features on your computer. Activation codes are unique and are valid on only one computer.

#### What Information Do I Need to Activate My NI Software?

You need your NI User account log-in, the product version and serial number, and a computer ID that uniquely identifies your computer. Certain activation methods may require additional information for delivery. This information is used only to activate your product. Complete disclosure of the NI software licensing information privacy policy is available at ni.com/activate/privacy. If you optionally choose to register your software, your information is protected under the NI privacy policy, available at ni.com/privacy.

#### How Do I Find My Product Serial Number?

Your serial number uniquely identifies your purchase of NI software. You can find your serial number on the Certificate of Ownership included in your software kit, or you can visit ni.com/info and enter the Info Code SerialNumbers_en.

If you have installed a previous version using your serial number, you can find the serial number by selecting Help»About within the application. You can also contact your local NI branch at ni.com/contact.

#### What Is a Computer ID?

The computer ID is a 16-character value that uniquely identifies your computer. NI requires this information to enable your software. You can find your computer ID through the NI Licensing Wizard or by using NI License Manager, as follows:

1. Launch the NI License Manager.
2. Click Computer Information in the ribbon.

For more information about product activation and licensing, refer to ni.com/activate.

#### How Can I Evaluate NI Software?

You can evaluate most NI products, in accordance with the license agreement. Evaluation terms vary, depending on which product you want to evaluate. Refer to your product documentation for specific information on the product's evaluation mode.

#### Moving Software after Activation

To transfer your software to another computer, uninstall the software on the first computer, then install and activate it on the second computer. You can transfer your software from one computer to another; you do not need to contact or inform NI of the transfer. Because activation codes are unique to each computer, you will need a new activation code. Refer to the How do I Activate my Software? section of this topic to learn how to acquire a new activation code and reactivate your software.

#### Deactivating a Product

To deactivate a product and return it to its preactivation state, navigate to the Local Licenses view, select the product to be deactivated, and click Deactivate from the ribbon. Alternatively, navigate to the Local Licenses view, right-click the product in the License tree, and click Deactivate. If the product was in evaluation mode before you activated it, the properties of the evaluation mode may not be restored.

#### Using Windows Guest Accounts

NI License Manager does not support Microsoft Windows Guest accounts. You must log in to a non-Guest account to run licensed NI application software.

<!--NI_TOPIC bundle=ni-vision-assistant path=add-a-step-to-a-script.html language=enus -->
## TOPIC 00010: Add a Step to a Script

- bundle_id: `ni-vision-assistant`
- source_path: `add-a-step-to-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/add-a-step-to-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can insert a new step anywhere in an existing script. In the Script window, select the step that you want to precede the new step. Select the image processing function that you want to apply. Set the function parameters. Click OK. Vision Assistant adds the step to the script after the selected s

### Add a Step to a Script

You can insert a new step anywhere in an existing script.

1. In the Script window, select the step that you want to precede the new
 step.
2. Select the image processing function that you want to apply.
3. Set the function parameters.
4. Click OK . Vision Assistant adds the step to the script after the selected step.

Parent topic:

Creating Scripts

Related concepts:

- Remove a Step from a Script
- Run a Script
- Save a Script
- Edit a Step in a Script

<!--NI_TOPIC bundle=ni-vision-assistant path=add-new-images-to-the-image-browser.html language=enus -->
## TOPIC 00011: Add New Images to the Image Browser

- bundle_id: `ni-vision-assistant`
- source_path: `add-new-images-to-the-image-browser.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/add-new-images-to-the-image-browser.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you open an image file and there are already images in the Image Browser, Vision Assistant prompts you to remove the existing images from the Image Browser. Click No to retain the existing images and add the new image to the Image Browser. Click Yes to remove the existing images from the Image

### Add New Images to the Image Browser

Note

No

Yes

#### Add
 New Images to the Image Browser in Processing Mode

You can add images to
 the Image Browser when you are processing images or when you are browsing
 images.

#### Add
 New Images to the Image Browser in Browsing Mode

When you are browsing
 images in the Image Browser, click Open Image
 [IMAGE alt='image' src='GUID-E8793EF8-D57F-4F29-8B93-28E3084E70D7-a5.gif'] or select File»Open Image to open
 new images in the Image Browser.

Parent topic:

Managing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=add-processed-images-to-the-image-browser.html language=enus -->
## TOPIC 00012: Add Processed Images to the Image Browser

- bundle_id: `ni-vision-assistant`
- source_path: `add-processed-images-to-the-image-browser.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/add-processed-images-to-the-image-browser.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can keep a copy of the image you are currently processing by sending a copy to the Image Browser. Click Store Image in Browser to send the image to the Image Browser.

### Add Processed Images to the Image Browser

You can keep a copy of the image you are currently processing by sending a copy to the Image
 Browser. Click Store Image in Browser
 [IMAGE alt='image' src='GUID-87B31F1C-1AC0-4F97-AA06-1CB28C85DF2A-a5.gif'] to send the image to the Image Browser.

Parent topic:

Managing Images

Related concepts:

- Browse Images in the Image Browser
- Open Images in Vision Assistant
- Print Images
- Save Images

<!--NI_TOPIC bundle=ni-vision-assistant path=apply-a-lookup-table-transformation.html language=enus -->
## TOPIC 00013: Apply a Lookup Table Transformation

- bundle_id: `ni-vision-assistant`
- source_path: `apply-a-lookup-table-transformation.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/apply-a-lookup-table-transformation.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the lookup table that you want to apply to the image. Click OK to apply the lookup table and add this step to the script.

### Apply a Lookup Table Transformation

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the lookup table that you want to apply to the image.
3. Click OK to apply the lookup table and add this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=apply-an-fft-filter-to-an-image.html language=enus -->
## TOPIC 00014: Apply an FFT Filter to an Image

- bundle_id: `ni-vision-assistant`
- source_path: `apply-an-fft-filter-to-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/apply-an-fft-filter-to-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the Truncate or Attenuate option. Select the Mode. Low Pass removes or attenuates high frequencies, and High Pass removes or attenuates low frequencies. If you selected Truncate, set the Truncation Frequency %. Otherwise, procee

### Apply an FFT Filter to an Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the Truncate or Attenuate option.
3. Select the Mode . Low Pass removes or attenuates high frequencies, and High Pass removes or attenuates low frequencies.
4. If you selected Truncate , set the Truncation Frequency % . Otherwise, proceed to the next step.
5. Click OK to apply the FFT Filter, add this step to the script, and close
 the Parameter window.

Note

Tip

Display
 FFT

Display Color Palette

Parent topic:

Analyzing and Processing Images

Related information:

- Concepts

<!--NI_TOPIC bundle=ni-vision-assistant path=apply-calibration-information-from-one-image.html language=enus -->
## TOPIC 00015: Apply Calibration Information from One Image to Another

- bundle_id: `ni-vision-assistant`
- source_path: `apply-calibration-information-from-one-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/apply-calibration-information-from-one-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Click Load Calibration from Image File. Navigate to a calibrated image file and click Open. Navigate through the tabs to see the calibration values. Click OK to add this step to the script and close the Parameter window. The size of th

### Apply Calibration Information from One Image to Another

1. In the Step Name textbox, enter a descriptive name for the step.
2. Click Load Calibration from Image File .
3. Navigate to a calibrated image file and click Open .
4. Navigate through the tabs to see the calibration values.
5. Click OK to add this step to the script and close the
 Parameter window.

Note

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=apply-grayscale-morphological-operations.html language=enus -->
## TOPIC 00016: Apply Grayscale Morphological Operations

- bundle_id: `ni-vision-assistant`
- source_path: `apply-grayscale-morphological-operations.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/apply-grayscale-morphological-operations.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the functions from the morphology list. Set the parameters for the function, if needed. You might need to set parameters for the structuring element, connectivity, or pixel frame. Click OK to apply the morphology and add

### Apply Grayscale Morphological Operations

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the functions from the morphology list.
3. Set the parameters for the function, if needed. You might need to set parameters for the structuring element, connectivity, or pixel frame.
4. Click OK to apply the morphology and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Reduce (Erode) Objects in Grayscale Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Remove Small Objects (Open) from Grayscale Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=apply-morphological-operations.html language=enus -->
## TOPIC 00017: Apply Morphological Operations

- bundle_id: `ni-vision-assistant`
- source_path: `apply-morphological-operations.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/apply-morphological-operations.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the functions from the morphology list. Set the parameters for the function, if needed. You may need to set parameters for the structuring element, connectivity, or pixel frame. Click OK to apply the morphology and add th

### Apply Morphological Operations

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the functions from the morphology list.
3. Set the parameters for the function, if needed. You may need to set parameters for the structuring element, connectivity, or pixel frame.
4. Click OK to apply the morphology and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Remove Small Objects
- Remove Large Objects
- Remove Objects Touching the Image Border
- Fill Gaps and Holes (Close) in Binary Images
- Compute the Convex Hull of Objects
- Reduce Objects to Skeletons
- Separate Objects
- Label Objects
- Create a Distance Map
- Segment an Image
- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Holes
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=browse-images-in-the-image-browser.html language=enus -->
## TOPIC 00018: Browse Images in the Image Browser

- bundle_id: `ni-vision-assistant`
- source_path: `browse-images-in-the-image-browser.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/browse-images-in-the-image-browser.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Image Browser displays thumbnail images in groups of 20. If there are more than 20 images open in the Image Browser, use the image browser controls to navigate the images. When you are viewing images in thumbnail view, you can begin processing an image by selecting the image and clicking Process

### Browse Images in the Image Browser

The Image Browser displays thumbnail images in groups of 20. If there are more than 20 images
 open in the Image Browser, use the *image browser controls* to navigate the
 images. When you are viewing images in thumbnail view, you can begin processing an image
 by selecting the image and clicking Process Images or by
 double-clicking the image.

You can view the thumbnail images in full size by clicking the Thumbnail/Full-Size
 View
 [IMAGE alt='image' src='GUID-40DBD139-54C5-4EA1-9A18-407FB32D9F11-a5.gif'] toggle button at the bottom of the Image Browser. When you
 are viewing the image in full-size view, use the *image browser controls* to
 navigate the images. You can use these buttons to scan the images in reverse or forward
 order and view the images continuously. Vision Assistant displays the current location,
 image size and type, and the file type below the image.

#### Remove Images from the Image Browser

Caution

- If you select Close Selected Image 
 while in thumbnail view
 without selecting an image, Vision Assistant prompts you to close all
 images in the Image Browser.
- If you remove images that you acquired and sent to the Image Browser,
 the images are deleted from memory and you cannot retrieve them.

To remove an image from the Image Browser in thumbnail view, select the image and
 click Close Selected Image. To remove multiple images from
 the Image Browser, click each image that you want to close, and then click
 Close Selected Image.

To remove an image from the
 Image Browser in full-size view, click Close Selected Image
 while the image is visible.

Note

Parent topic:

Managing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=calculate-roi-measurements.html language=enus -->
## TOPIC 00019: Calculate ROI Measurements

- bundle_id: `ni-vision-assistant`
- source_path: `calculate-roi-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/calculate-roi-measurements.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Calculate ROI Measurements

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Measure Tab

1. Select the type of measurement that you want to calculate.
2. Draw an ROI on the image. Vision Assistant displays the results for that
 measurement in the Results table. 
 Note 
 The Measure function analyzes the image and displays information for
 you to review. This function does not modify the image.
 Angles are measured in degrees, counterclockwise. 
 Tip 
 To save the data, click the Send Data to
 Excel button or the Save
 Results button.
 To remove the selected row, click Delete
 Selection. To delete all results, click
 Delete All Results.
3. Click OK to add the step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Selecting a Region of Interest (ROI)

<!--NI_TOPIC bundle=ni-vision-assistant path=calibrate-images.html language=enus -->
## TOPIC 00020: Calibrate Images

- bundle_id: `ni-vision-assistant`
- source_path: `calibrate-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/calibrate-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Assistant can calibrate images containing distortion in order to return accurate measurements. The Image Calibration step calibrates images so that inspection results are returned in real-world units.Calibrating an image is a two-step process. Use the Calibration Training Interface to specify

### Calibrate Images

Vision Assistant can calibrate images containing distortion in order to return accurate
 measurements. The Image Calibration step calibrates images so
 that inspection results are returned in real-world units.

Calibrating an image is a two-step process.

1. Use the Calibration Training Interface to specify the type of calibration, the calibration
 parameters, and the real-world unit in which you want to express measurements.
2. Use the Image Calibration step to apply the computed calibration to the
 image during the inspection process.

Tip

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=classify-color-samples.html language=enus -->
## TOPIC 00021: Classify Color Samples

- bundle_id: `ni-vision-assistant`
- source_path: `classify-color-samples.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/classify-color-samples.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow these instructions to classify a color sample in a given region of interest (ROI): Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a p

### Classify Color Samples

Follow these instructions to classify a color sample in a given region of interest (ROI):

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. Browse to the classifier file you want to use, select the file, and click
 Open .
5. If you want to create a new classifier file, click New Classifier
 File . In the Save Classifier File As 
 window, enter the file name for the file you want to create.
6. Click OK to open the Color Classification Training
 Interface. Tip Refer
 to the Color Classification Training Interface Help for more information
 about how to train and classify samples in the Classification Training
 Interface. 
 Note If necessary,
 click Edit Classifier File to classify additional
 samples in the Color Classification Training Interface.
7. Draw an ROI around the sample you want to classify. Tip You can classify multiple
 areas of the image by pressing the <Ctrl> key and drawing a new
 ROI.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=classify-particle-samples.html language=enus -->
## TOPIC 00022: Classify Particle Samples

- bundle_id: `ni-vision-assistant`
- source_path: `classify-particle-samples.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/classify-particle-samples.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow these instructions to classify a sample in a given region of interest (ROI): Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previou

### Classify Particle Samples

Follow these instructions to classify a sample in a given region of interest (ROI):

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Train Tab

1. Browse to the classifier file you want to use, select the file, and click
 Open .
2. If you want to create a new classifier file, click New Classifier
 File . In the Save Classifier File As window, enter the file name
 for the file you want to create.
3. Click OK to open the Particle Classification Training
 Interface. Tip Refer
 to the Particle Classification Training Interface Help for more information
 about how to train and classify samples in the Classification Training
 Interface. 
 Note If necessary,
 click Edit Classifier File to classify additional
 samples in the NI Particle Classification Training Interface.
4. Draw an ROI around the sample you want to classify. Vision Assistant segments
 samples in the ROI by drawing particle bounding rectangles around the samples
 according to the current settings in the Main ,
 Threshold , Engine Options , and
 Parameters tabs.

#### Threshold Tab

Note

Threshold

1. Select a threshold type from the Method list. When you
 select Manual Threshold , you must set the threshold range
 with the Min and Max boxes.
2. Select the type of objects you want to classify in the sample from the
 Look For list. You can classify Bright
 Objects , Dark Objects , or Gray
 Objects .
3. Enable the Ignore Objects Touching Region Borders 
 checkbox to ignore objects in the sample that touch the border of the ROI.
4. In Remove Small Objects (# of Erosions) , select the
 number of erosions to remove small objects in the sample from the ROI. The
 classification engine displays segmented objects in blue.

#### Options Tab

Select values from the
 Method and Metric lists that the
 classification engine should use for sample recognition.

#### Parameters Tab

1. Enable the Scale Dependent checkbox to determine the
 relative importance of scale when classifying samples. Enter the numerical scale
 value (between 0 and 1000) in the Scale Factor box. If
 the value is 0, samples are classified independent of scale.
2. Enable the Mirror Dependent to determine the relative
 importance of mirror symmetry when classifying samples. Enter the numerical
 value of importance (between 0 and 1000) for the mirror symmetry in the
 Mirror Factor box. If the value is 0, samples are
 classified independent of mirror symmetry.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=compute-the-convex-hull-of-objects.html language=enus -->
## TOPIC 00023: Compute the Convex Hull of Objects

- bundle_id: `ni-vision-assistant`
- source_path: `compute-the-convex-hull-of-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/compute-the-convex-hull-of-objects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Convex. Click OK to close objects and add this step to the script. This function is computer-intensive and can take several seconds. Use this function to close particles so you can mak

### Compute the Convex Hull of Objects

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Convex .
3. Click OK to close objects and add this step to the script.

Note

Tip

Parent topic:

Analyzing and Processing Images

Related concepts:

- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=compute-the-energy-center-of-an-image.html language=enus -->
## TOPIC 00024: Compute the Energy Center of an Image

- bundle_id: `ni-vision-assistant`
- source_path: `compute-the-energy-center-of-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/compute-the-energy-center-of-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Assistant calculates the energy center (centroid) of the image and returns the coordinates. In the Step Name textbox, enter a descriptive name for the step. Click OK to add this step to the script. You can compute the centroid of a portion of the image by drawing an ROI.

### Compute the Energy Center of an Image

1. Vision Assistant calculates the energy center (centroid) of the image and returns the coordinates.
2. In the Step Name textbox, enter a descriptive name for the step.
3. Click OK to add this step to the script.

Tip

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=compute-the-symmetry-of-an-image.html language=enus -->
## TOPIC 00025: Compute the Symmetry of an Image

- bundle_id: `ni-vision-assistant`
- source_path: `compute-the-symmetry-of-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/compute-the-symmetry-of-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Compute the Symmetry of an Image

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Geometry Tab

1. Select Symmetry .
2. Select a type of symmetry.
3. Click OK to add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Resample an Image
- Rotate an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=configuring-remote-targets.html language=enus -->
## TOPIC 00026: Configuring Remote Targets

- bundle_id: `ni-vision-assistant`
- source_path: `configuring-remote-targets.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/configuring-remote-targets.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Remote targets are field programmable devices that you add to a subnet and run remotely. You configure a remote target from a host machine on the same subnet, defining settings such as the target name and description, network settings, and software revisions.If the remote target you want to select i

### Configuring Remote Targets

Remote targets are field programmable devices that you add to a subnet and run remotely. You
 configure a remote target from a host machine on the same subnet, defining settings such
 as the target name and description, network settings, and software revisions.

If the remote target you want to select is on a different subnet than the development computer,
 it may not appear in the list of available targets. Click Add
 Target, enter the IP address of the remote target you want to configure,
 and click OK to add the target to the table.

Parent topic:

Acquiring Images

<!--NI_TOPIC bundle=ni-vision-assistant path=contour-analysis-3.html language=enus -->
## TOPIC 00027: Contour Analysis

- bundle_id: `ni-vision-assistant`
- source_path: `contour-analysis-3.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/contour-analysis-3.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Contour analysis involves three steps. First, curves are extracted from the image. Next, the curves are connected based on the connection parameters. Finally, the step selects a single connected curve to represent the contour. Refer to the Vision Concepts Help for more information about the process

### Contour Analysis

Contour analysis involves three steps. First, curves are extracted from the image. Next, the
 curves are connected based on the connection parameters. Finally, the step selects a
 single connected curve to represent the contour. Refer to the Vision Concepts Help for
 more information about the process of contour analysis.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is enabled if
 you want to link the region of interest specified in this step to a previously
 defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. Draw a ROI around an object in the image with contours that you want to
 analyze.

#### Extract Contour

1. Modify the Curve Extraction controls to improve curve
 detection, if necessary.
2. Modify the Contour Selection controls, if necessary, so
 that the step selects the correct contour for your application.
3. Modify the Curve End Point Connection controls, if
 necessary, to change how the step connects individual curves to produce
 contours.
  1. Modify the Distance Range control to only connect
 curves with end points separated by a distance within the specified
 range. The following figure illustrates distance between end points:
 [IMAGE alt='image' src='GUID-5F5F169B-BC49-4A93-AABE-DE55F9A6558D-a5.gif']
 Distance
  2. Modify the Angle Range control to only connect
 curves when the difference between the angle of the curves, measured at
 the end points, is within the specified range. Values range from 0
 degrees to 180 degrees. The following figures illustrate how the angle
 of a curve is calculated: [IMAGE alt='image' src='GUID-101F4097-7B85-4191-8AD8-4DE1E2210272-a5.gif']
 [IMAGE alt='image' src='GUID-FE4E187C-805A-4E8C-8D7C-00CFBB3EF22A-a5.gif']
 A
 B 
 In Figure A, the difference between angle A and angle B is close to
 0. In Figure B, the difference between angle A and angle C is close
 to 90 degrees.
  3. Modify the Connectivity Range control to only
 connect curves when a line extended from the end point of one curve
 passes the end point of another curve within the specified distance. The
 following figure illustrates how connectivity is calculated: [IMAGE alt='image' src='GUID-6E545F34-E81C-4551-A067-61CF2FA0B61A-a5.gif']
 Distance between end point A and aline
 extended from end point B
 Distance between end point A and endpoint
 C 
 End point A is closer to end point C than to end point B. Specify a
 connectivity range to connect end point A to end point B instead of
 end point C.
  4. Modify the Gradient Direction Range control to
 only connect curves when the difference between the gradient angle of
 each curve is within the specified range. The following figure
 illustrates two curves with opposite gradient angles: [IMAGE alt='image' src='GUID-14EC6F31-A876-41D7-98D4-3F31CBF059F5-a5.gif'] 
 Specify a high gradient range to connect the curves.

Note

Contour Selected

#### Analyze Curvature

1. Enable the Compute Curvature checkbox if you want to
 compute the curvature of the selected contour. Adjust the Kernel
 Size value to change the size of the kernel used to compute the
 curvature profile of the contour. The Curvature Profile 
 table displays the curvature profile for the selected contour. Refer to the NI
 Vision Concepts Help for more information about how the contour analysis
 algorithm computes curvature.
2. Complete the following steps if you want to classify individual curves along the
 selected contour:
  1. Click the Add Range 
 button to create a new
 curvature range.
  2. Refer to the Curvature Profile and identify the
 curvature range that you want to classify. Tip A red line indicates
 the currently selected position in the curvature profile. A cross
 indicates the currently selected position on the selected contour in
 the displayed image. Use these indicators to identify the curvature
 range that you want to classify.
  3. Adjust the Min and Max 
 values to include the curvature range that you want to classify.
  4. Click the Color for the selected curvature range
 to change the color used to indicate the class in the image.

#### Compare Contours

1. Enable the Compare Contour checkbox if you want to
 compare the selected contour to a fitted contour or a template contour.
2. Select To Fitted Contour to compare the selected contour
 to a fitted contour.
  - Select Line , Circle , or
 Ellipse to fit an ideally shaped contour to
 data points in the selected contour. Modify the Pixel
 Radius to control how the contour is fitted to the
 selected contour. Tip The step uses the
 following process to fit a contour. The step assumes that a point is
 part of the fitted contour if the point lies within a user-defined
 pixel radius from the fitted contour. Then the step fits a line to a
 subset of points that best describe the selected shape.
  - Select B-Spline or
 Polynomial to fit a contour to data points in
 the selected contour. Modify the Control Points ,
 Degree , or Order 
 settings to control how the contour is fitted to the selected
 contour.
3. Select To Template Contour to compare the selected
 contour to a template contour image. Draw a ROI around the contour in the image
 and click New to create a new template contour image.
  - If the orientation angle of the selected contour can differ from the
 template contour, enable the Rotation 
 checkbox.
  - If the scale of the selected contour can differ from the template
 contour, enable the Scale checkbox.
  - If the object outlined by the selected contour can be occluded in the
 image, enable the Occlusion checkbox.
  - Specify a Smoothing Kernel size, if necessary.
 Smoothing reduces the distance between the selected contour and the
 template contour.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=convert-grayscale-images.html language=enus -->
## TOPIC 00028: Convert Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `convert-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/convert-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the data type that you want to convert the current image to. If you are converting the image to a smaller data type, select the method of conversion. Click OK to convert the image, add this step to the script, and close the Conv

### Convert Grayscale Images

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the data type that you want to convert the current image to. If you are converting the image to a smaller data type, select the method of conversion.
3. Click OK to convert the image, add this step to the script, and close the
 Conversion window.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=copyright.html language=enus -->
## TOPIC 00029: Copyright

- bundle_id: `ni-vision-assistant`
- source_path: `copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/copyright.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of Emerson Electric Corporation

### Copyright

Under the copyright laws, this publication may not be reproduced or transmitted in any form,
 electronic or mechanical, including photocopying, recording, storing in an information
 retrieval system, or translating, in whole or in part, without the prior written consent
 of Emerson Electric Corporation.

NI respects the intellectual property of others, and we ask our users to do the same. NI software is protected by copyright and other intellectual property laws. Where NI software may be used to reproduce software or other materials belonging to others, you may use NI software only to reproduce materials that you may reproduce in accordance with the terms of any applicable license or other legal restriction.
End-User License Agreements and Third-Party Legal Notices

You can find end-user license agreements (EULAs) and third-party legal notices in the following locations:

- Notices are located in the <National Instruments>\_Legal Information and <National Instruments> directories.
- EULAs are located in the <National Instruments>\Shared\MDF\Legal\license directory.
- Review <National Instruments>\_Legal Information.txt for information on including legal information in installers built with NI products.

U.S. Government Restricted Rights

If you are an agency, department, or other entity of the United States Government ("Government"), the use, duplication, reproduction, release, modification, disclosure or transfer of the technical data included in this manual is governed by the Restricted Rights provisions under Federal Acquisition Regulation 52.227-14 for civilian agencies and Defense Federal Acquisition Regulation Supplement Section 252.227-7014 and 252.227-7015 for military agencies.
IVI Foundation Copyright Notice

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

Parent topic:

Important Information

<!--NI_TOPIC bundle=ni-vision-assistant path=correct-images.html language=enus -->
## TOPIC 00030: Correct Images

- bundle_id: `ni-vision-assistant`
- source_path: `correct-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/correct-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the Interpolation Type you want to use to rescale the image. A Zero-Order interpolation is faster, but provides lower-quality results than a Bi-Linear interpolation. Click OK to add this step to the script and close the Paramete

### Correct Images

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the Interpolation Type you want to use to rescale the image. A Zero-Order interpolation is faster, but provides lower-quality results than a Bi-Linear interpolation.
3. Click OK to add this step to the script and close the
 Parameter window.

Note

Calibration from Image

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=correcting-flat-field-images.html language=enus -->
## TOPIC 00031: Correcting Flat Field Images

- bundle_id: `ni-vision-assistant`
- source_path: `correcting-flat-field-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/correcting-flat-field-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Flat field correction uses one bright field image and one optional dark field image to correct uneven background intensity. You can specify or create or a single bright field image, or you can create a bright field image iteratively at each inspection.The following figure illustrates use cases for v

### Correcting Flat Field Images

Flat field correction uses one bright field image and one optional dark field image to correct
 uneven background intensity. You can specify or create or a single bright field image,
 or you can create a bright field image iteratively at each inspection.

The following figure illustrates use cases for various types of flat field correction:

[IMAGE alt='image' src='GUID-04E68F22-47FC-44E7-BC2F-BA472F38BCEA-a5.gif']

#### Using a Specified Bright Field Image for Flat Field Correction

Select
 Correction with specified bright field image to use one
 image as the bright field for flat field correction. Click [IMAGE alt='image' src='GUID-37FC0F09-A489-46F1-A3AE-75ED46E9B9BF-a5.gif'] to specify a path to an existing image. Click
 Browse
 [IMAGE alt='image' src='GUID-C0EE8697-63F6-4BFB-AE5A-0391C62D9A16-a5.gif'] to launch the Flat Field Creation
 Wizard to create a new bright field image.

Use this option if
 you can acquire an image of the background only.

#### Using Bright Field Images for Iterative Flat Field
 Correction

Select Online Correction Using Modeling
 for the inspection to relearn the bright field at each iteration. Use the
 Estimate Background controls to configure how the
 algorithm computes the bright field.

This option is recommended when
 background variations are inconsistent across images.

#### Creating a Bright Field Image Using Vision
 Assistant Steps

To create a bright field image in Vision Assistant, make a
 script with the following steps:

1. Acquire an image.
2. Add an Image Buffer step to save the acquired image.
3. Add a Filters step. Select a Smoothing - Low
 Pass filter with a large Filter Size , or
 a Smoothing - Gaussian filter with a large
 Kernel Size . You can also use your own algorithm.
 This creates a bright field image.
4. Add an Image Buffer step to save the bright field
 image.
5. Add an Image Buffer step to retrieve the original
 acquired image stored in the first buffer step you created.
6. Add a Flat Field Correction step. Select the
 Correction with specified bright field image option
 and set the Image Buffer to retrieve the bright field
 image.

The script should resemble the following image:

[IMAGE alt='image' src='GUID-8A192130-3F6E-45C4-9ACA-94D822DB4199-a5.gif']

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=create-a-distance-map.html language=enus -->
## TOPIC 00032: Create a Distance Map

- bundle_id: `ni-vision-assistant`
- source_path: `create-a-distance-map.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/create-a-distance-map.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Distance or Danielsson. Click OK to add this step to the script. This function assigns, to each pixel, a grayscale value equal to the shortest distance to the border of the object. The

### Create a Distance Map

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Distance or Danielsson .
3. Click OK to add this step to the script.

Note

Danielsson

Distance

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=creating-a-labview-vi.html language=enus -->
## TOPIC 00033: Creating a LabVIEW VI

- bundle_id: `ni-vision-assistant`
- source_path: `creating-a-labview-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creating-a-labview-vi.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Tools»Create LabVIEW VI.If Create LabVIEW VI is disabled in the Tools menu, insert a step in Vision Assistant script prior to creating the LabVIEW VI. Select the version of LabVIEW that you want to use to create the VI. If you have several versions of LabVIEW installed, the wizard displays a

### Creating a LabVIEW VI

1. Select Tools»Create LabVIEW VI . Note If Create LabVIEW VI
 is disabled in the Tools menu, insert a step in Vision Assistant
 script prior to creating the LabVIEW VI.
2. Select the version of LabVIEW that you want to use to create the VI. 
 If you have several versions of LabVIEW installed, the wizard displays a list of
 available LabVIEW versions that you can use to create the VI. 
 
 If you select Add VI to New Project, Vision Assistant will launch a new LabVIEW NXG
 window and create a new project.
  1. 
    - If you select 32 or 64-bit LabVIEW 201x, browse to the location to which you want
 to save the VI.
    - Select Optimize Code for Parallel Execution if the
 performance of your task could benefit from parallelization.
  2. If you select LabVIEW NXG, the wizard displays two options:
    - Add VI to Current Project
    - Add VI to New Project
3. Click Next .
4. Select the image source for the VI.
  - Image Control — Creates an Image In control and Image Out
 indicator, allowing you to use the created VI as a sub-VI.
  - Image File — Creates the diagram to open an image file from the
 hard drive.
  - Image Acquisition — Creates the diagram to acquire an image
 from a camera connected to an NI image acquisition device.
5. Click Next .
6. Select the controls and indicators that you want to appear on the front panel of the
 generated VI. Items selected will also be connected to the connector pane of the VI. Items
 not selected will appear as constants on the diagram, with values set to the same values
 configured in the property page of each step.
7. Click Finish to create the VI .

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=creating-a-new-script.html language=enus -->
## TOPIC 00034: Creating a New Script

- bundle_id: `ni-vision-assistant`
- source_path: `creating-a-new-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creating-a-new-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You create a script as you process an image. To create a new script, select File»New Script or click the New button in the Script window. Vision Assistant prompts you to save the current script before creating a new script.

### Creating a New Script

You create a script as you *process an image*. To create a new script, select
 File»New Script or click the New
 [IMAGE alt='image' src='GUID-61B69D86-C8FB-4084-8D68-484393816D11-a5.gif'] button in the *Script window*. Vision Assistant
 prompts you to save the current script before creating a new script.

Parent topic:

Creating Scripts

Related concepts:

- Processing an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=creating-c-code.html language=enus -->
## TOPIC 00035: Creating C Code

- bundle_id: `ni-vision-assistant`
- source_path: `creating-c-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creating-c-code.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Tools»Create C Code. If Create C Code is disabled in the Tools menu, select File»Preferences and select the General tab, then select C Code in the Language for Generated Code list. You can also select a C target from the startup screen the next time you launch Vision Assistant. Enter the file

### Creating C Code

1. Select Tools»Create C Code .

Note

Create C
 Code

Tools

File»Preferences

General

C Code

Language for Generated Code

1. Enter the file name under which you want to save the C code in the Implementation File Name textbox.
2. If you would like the C Code Creation Wizard to generate a main function, which acquires an image from a source, enable the Create Main Function option. Enter the name of the main function file in the Main File Name textbox.
3. Select the Image Source for the C Code creation. The following image
 source options are available: 
 Note You must have
 NI-IMAQ for IEEE 1394 Cameras installed to create the code to acquire images
 from IEEE 1394 cameras.
  - Image File —Creates the C code to open an image file
 from the hard drive.
  - Acquisition from an NI Image Acquisition device —
 Creates the C code to acquire an image from a camera connected to an NI
 image acquisition device.
  - Triggered Acquisition from an NI Image Acquisition
 device — Creates the C code that performs a triggered image
 acquisition with an NI image acquisition device.
  - Acquisition from an IEEE 1394 Camera — Creates the C
 code to acquire an image with NI-IMAQ for IEEE 1394 Cameras.
4. Browse to the location to which you want to save the generated files.
5. If you would like to add the generated files to a LabWindows/CVI project, enable the
 Add Files to LabWindows/CVI project option. If you have a
 LabWindows/CVI Project open to which you want to add the generated files, enable the
 Use Currently Open Project option. Enable the
 Create New Project option to add the files to a new
 project. Note This
 option is available only if LabWindows/CVI is installed on your computer.

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=creating-labview-fpga-code.html language=enus -->
## TOPIC 00036: Creating LabVIEW FPGA Code

- bundle_id: `ni-vision-assistant`
- source_path: `creating-labview-fpga-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creating-labview-fpga-code.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Tools»Create LabVIEW FPGA Code. If Create LabVIEW FPGA Code is disabled in the Tools menu, select File»Preferences, select the General tab, and select the target device from Target for Generated Code. You can also select a LabVIEW FPGA target from the startup screen the next time you launch V

### Creating LabVIEW FPGA Code

1. Select Tools»Create LabVIEW FPGA Code .

Note

Create LabVIEW FPGA
 Code

Tools

File»Preferences

General

Target for Generated Code

1. Browse to the location to which you want to save the FPGA code.
2. Select all options that apply:
  - Create LabVIEW Project creates the FPGA code under a new LabVIEW project. Specify the project name in the text box.
  - Create Host VI creates a VI on the host machine. This VI shows how images are transferred to and from the FPGA. Specify the host VI name in the text box.
  - Create FPGA Main VI creates a VI on the FPGA target. This VI shows how the pixels are retrieved from the host, processed on the FPGA, and transferred back to the host. Specify the FPGA main VI name in the text box.
    - Transfer Image Back to Host transfers images from the FPGA target to the host machine.
  - Bayer Decoding specifies how to decode Bayer pixel formats in a color image.
    - Disable does not perform Bayer decoding.
    - Bilinear selects the Bilinear Bayer decoding algorithm, which provides fast, basic Bayer decoding.
    - VNG selects the VNG Bayer decoding algorithm, which is recommended if the image contains many edges, or if the quality of the edges is important. VNG Bayer decoding takes longer than Bilinear.
3. Enter a VI name in the FPGA Implementation VI Name text box.
4. Click Next .
5. Use the Controls tree to select which controls appear on the front panel of the FPGA implementation VI. Selected controls also appear on connector pane of the FPGA implementation VI. These controls can be modified while the VI is running if you create the corresponding controls on the FPGA main VI. 
 Controls that are not selected become constants on the block diagram with values from the Vision Assistant step.
6. Use the Indicators tree to select which indicators appear on the front panel of the FPGA implementation VI. Selected indicators also appear on the connector pane of the FPGA image processing VI.


You can then create the corresponding indicators on the FPGA main VI. To access these indicators from the host VI, connect a property node to the FPGA VI reference.
7. Click Finish .

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=creating-net-code.html language=enus -->
## TOPIC 00037: Creating .NET Code

- bundle_id: `ni-vision-assistant`
- source_path: `creating-net-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creating-net-code.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create .NET code that implements the steps of the current script. Select Tools»Create .NET Code.If Create .NET Code is disabled in the Tools menu, select File»Preferences and select the General tab, then select .NET Code in the Language for Generated Code list. You ca

### Creating .NET Code

Complete the following steps to create .NET code that implements the steps of the current
 script.

1. Select Tools»Create .NET Code . Note If Create .NET
 Code is disabled in the Tools menu,
 select File»Preferences and select the
 General tab, then select .NET
 Code in the Language for Generated Code
 list. You can also select a .NET target from the startup screen the next time
 you launch Vision Assistant.
2. Select the programming language in which you want the generated code to be
 written.
3. If you would like the .NET Code Creation Wizard to generate a Visual Studio Project,
 enable the Create Visual Studio Project option.
4. Select the programming environment that you will use to create the Visual Studio
 project.
5. Enter the file name under which you want to save the .NET code in the Implementation
 File Name textbox. Note You cannot specify a file name if the Create Visual Studio
 Project option is enabled.
6. Complete the following steps to select the location to which you want to save the
 generated files.
  1. Click the Browse 
 button to browse to the
 location to which you want to save the generated files.
  2. Click Current Folder .
7. Click OK .

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=creatingscripts.html language=enus -->
## TOPIC 00038: Creating Scripts

- bundle_id: `ni-vision-assistant`
- source_path: `creatingscripts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/creatingscripts.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`

### Creating Scripts

- [Scripting Concepts](scripting-concepts.html)
- [Creating a New Script](creating-a-new-script.html)
- [Open a Script](open-a-script.html)
- [Save a Script](save-a-script.html)
- [Run a Script](run-a-script.html)
- [Edit a Step in a Script](edit-a-step-in-a-script.html)
- [Add a Step to a Script](add-a-step-to-a-script.html)
- [Remove a Step from a Script](remove-a-step-from-a-script.html)
- [Perform Batch Processing](perform-batch-processing.html)
- [Performance Meter](performance-meter.html)
- [Estimating FPGA Device Utilization](estimating-fpga-device-utilization.html)

<!--NI_TOPIC bundle=ni-vision-assistant path=defining-a-weight-map.html language=enus -->
## TOPIC 00039: Defining a Weight Map

- bundle_id: `ni-vision-assistant`
- source_path: `defining-a-weight-map.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/defining-a-weight-map.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to define a weight map. Enable Attenuate Edge Regions if you want to attenuate the defects along the edges of the object. Adjust the Edge Threshold and Edge Thickness to ensure that the red highlighted curves accurately reflect the part of the image you want to ignore. C

### Defining a Weight Map

Complete the following steps to define a weight map.

1. Enable Attenuate Edge Regions if you want to attenuate the defects along the edges of the object.
2. Adjust the Edge Threshold and Edge Thickness to ensure that the red highlighted curves accurately reflect the part of the image you want to ignore.
3. Customize the regions to ignore using the Draw Additional Regions to Ignore tools. Select a tool, and draw additional regions to ignore in the image. The additional regions to ignore are shown in blue on the template.
4. If necessary, use the Erase Area tool to erase customizations at specific locations of the template. Click Clear All Additional Regions to erase additional regions to ignore. Press <Ctrl-Z> to undo the last customization. Press <Ctrl-Shift-Z> to redo the last customization that you undid.
5. Click OK to define the weight map.

#### Controls

The following controls are
 available.

- Attenuate Edge Regions —Specifies whether to enable or
 disable attenuation of edge regions.
  - Edge Threshold — Uses a Sobel algorithm to find
 the edges of objects in the template. Edge Threshold is the threshold
 value applied to the grayscale Sobel image. The threshold results in a
 binary image containing only the object edges. This binary image is used
 to mask the edges you want to ignore during golden template comparison.
 Note If
 the inspection image exhibits little contrast between edges and the
 background, the image resulting from the Sobel algorithm can be
 dark. Dark Sobel images require a low value for Edge Threshold. The
 default value is 15.
  - Edge Thickness — Specifies the thickness of the
 edges to ignore. Note Edge Thickness is a
 run-time parameter. The modification of this parameter in the Define
 Weight Map window is for display purposes. The Weight Map is always
 saved with an edge thickness of 1.
- Draw Additional Regions to Ignore — Controls that allow
 you to draw additional regions to ignore by the map defects algorithm.
  - Pen Tool — Manually draws any shape areas using
 this tool. You can set the width of the pen with the Pen
 Width control.
  - Rectangle Tool — Draws a rectangular region to
 ignore.
  - Oval Tool — Draws an oval to ignore.
  - Polygon Tool — Draws a polygon to ignore. Click
 to add polygon vertices. Double-click to add the last vertex and close
 the polygon.
  - Free Hand Tool — Draws a closed shape to
 ignore.
  - Eraser — Erases customization at specific
 locations of the template.
- Pen Width — Specifies the width of the Pen or Eraser
 tools.
- Clear All Additional Regions — Erases all
 customization.
- Weight Map Edges — Indicates the color used to highlight
 the edges of the objects in the image using the current Edge Threshold and Edge
 Thickness settings.
- Additional Regions to Ignore — Indicates the color used
 to highlight additional regions to ignore by the map defects algorithm.
- Display — Specifies whether to display the template image
 or the weight map.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-circles.html language=enus -->
## TOPIC 00040: Detect Circles

- bundle_id: `ni-vision-assistant`
- source_path: `detect-circles.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-circles.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Assistant finds the best circular fit in each particle and displays the results. In the Step Name textbox, enter a descriptive name for the step. Set up the Minimum Radius and Maximum Radius of the circles to be detected. Click OK to add this step to the script. This algorithm is dedicated to

### Detect Circles

1. Vision Assistant finds the best circular fit in each particle and displays the results.
2. In the Step Name textbox, enter a descriptive name for the step.
3. Set up the Minimum Radius and Maximum Radius of the circles to be detected.
4. Click OK to add this step to the script.

Note

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-circular-edges-in-grayscale-images.html language=enus -->
## TOPIC 00041: Detect Circular Edges in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `detect-circular-edges-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-circular-edges-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Circular Edge (Spoke) function works only with 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordin

### Detect Circular Edges in Grayscale Images

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Settings Tab

1. Draw and adjust a region of interest using the annulus tool that includes the
 circular edge you want to find. When you specify a region of interest, the
 step automatically tries to locate a circular edge in the region. If the
 automatically-located edge corresponds to the edge you expected to find,
 skip the next step. Otherwise, go to the next step.
2. Disable the Auto Setup checkbox and manually adjust the
 edge location parameters.
  1. Select the direction properties of the search lines. Select the search
 direction along the lines that has the least number of obstacles between
 the edge of the region and the object edge you want to find.
  2. If the Edge Strength Profile contains a strong peak that corresponds to
 the edge you want to find, adjust the yellow edge strength line so that
 it lies slightly below the top of the edge peak but above all of the
 other peaks.
  3. If the Edge Strength Profile does not contain a strong edge peak,
 adjust the values in the Smoothing and
 Steepness boxes until a peak appears. 
 If the step still cannot find the edge or the location of the
 detected edge is inaccurate, adjust the gap between the search lines
 until you achieve the expected result.

#### Results Tab

1. Click the Results tab to view information about the
 center and radius of the circular edge the step found on the image.
2. Click OK to add this step to the script and close the
 Parameter window.

Tip

Parent topic:

Analyzing and Processing Images

Related concepts:

- Detect Circular Edges
- Edge Detector

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-circular-edges.html language=enus -->
## TOPIC 00042: Detect Circular Edges

- bundle_id: `ni-vision-assistant`
- source_path: `detect-circular-edges.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-circular-edges.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Find Circular Edge step searches for a circular edge in a two-dimensional, annulus-shaped region of interest. The region of interest contains a number of search lines along which the step searches for sharp transitions in pixel intensities. A sharp transition typically characterizes the edge of

### Detect Circular Edges

The Find Circular Edge step searches for a circular edge in a
 two-dimensional, annulus-shaped region of interest. The region of interest contains a
 number of search lines along which the step searches for sharp transitions in pixel
 intensities. A sharp transition typically characterizes the edge of an object in the
 image. The step fits a circle through the individual edge points of each search line to
 determine a circular edge on the object under inspection.

#### Main Tab

1. In the Step Name control, enter a descriptive name for
 the step.
2. Choose one of the following methods to specify the region of interest for the step: When you specify a region of interest, the step automatically tries to
 locate a circular edge in the region. If the automatically located edge is
 not the edge you expect to find, complete the steps below to configure the
 controls on the Settings tab.
  - Create a new region of interest.
    1. Select a tool from the menu toolbar that matches the type of
 region of interest you want to specify.
    2. Draw a region of interest on the image. For the best results,
 ensure that the region of interest encloses the entire edge that
 you want to find but excludes as many edges of no interest as
 possible. Make sure the edge fills up most of the region length.
 Also, make sure that the region is at least 20 pixels wide on
 either side of the edge to accurately detect the points along
 the edge.
  - Select a previously defined region of interest from the
 Region of Interest listbox.

#### Settings Tab

1. Select the Direction property of the search lines. Select
 the search direction along the lines that has the least number of obstacles
 between the edge of the region and the object edge you want to find.
2. Select the Edge Polarity of the circular edge you want to
 find.
3. Choose the type of edges you want to detect from the Look
 For control. You can choose from First
 Edge or Best Edge .
4. If the automatically located circular edge is not the edge you expect to find, disable the
 Auto Setup control and manually adjust the edge
 location parameters. Use the edge information on the Advanced tab to determine
 appropriate settings for the edge location parameters.
5. If the Edge Strength Profile contains a strong peak that corresponds to the
 edge you want to find, adjust the blue edge strength line so that it lies
 slightly below the top of the edge peak but above all of the other peaks.
 Use the Search Line Index control to display edge
 profile information for each search line in the region of interest. 
 If the Edge Strength Profile does not contain peaks that correspond to all
 the edges, adjust the Kernel Size and
 Projection Width controls until distinct peaks
 appear. If the step still cannot find the edge or the location of the
 detected edge is inaccurate, adjust the Gap between
 the search lines until you achieve the expected result.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-edges-in-grayscale-images.html language=enus -->
## TOPIC 00043: Detect Edges in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `detect-edges-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-edges-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Detect Edges in Grayscale Images

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Edge Detector Tab

You can find edges in
 grayscale images using the *Simple Edge Tool* or the *Advanced Edge
 Tool*.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Detect Edges with the Simple Edge Tool
- Detect Edges with the Advanced Edge Tool

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-edges-with-filters.html language=enus -->
## TOPIC 00044: Detect Edges with Filters

- bundle_id: `ni-vision-assistant`
- source_path: `detect-edges-with-filters.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-edges-with-filters.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette. Select one of the edge detection filters from the Filters list. If you are using the Laplacian filter, set the Kernel Size and coefficients. Click OK to filter the image and add this step to the script

### Detect Edges with Filters

1. Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette.
2. Select one of the edge detection filters from the Filters list. If you are using the Laplacian filter, set the Kernel Size and coefficients.
3. Click OK to filter the image and add this step to the script.

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Filter an Image with a Custom Convolution Filter
- Highlight Details in an Image
- Smooth an Image with Filtering

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-edges-with-the-advanced-edge-tool.html language=enus -->
## TOPIC 00045: Detect Edges with the Advanced Edge Tool

- bundle_id: `ni-vision-assistant`
- source_path: `detect-edges-with-the-advanced-edge-tool.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-edges-with-the-advanced-edge-tool.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the Advanced Edge Tool from the Edge Detector list. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays the strength of the edges along the ROI and lists the number of edges found along that path. Select the option from Look For that specif

### Detect Edges with the Advanced Edge Tool

1. Select the Advanced Edge Tool from the Edge Detector list.
2. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays the strength of the edges along the ROI and lists the number of edges found along that path.
3. Select the option from Look For that specifies which edges you are looking for.
4. Set the Edge Polarity , Interpolation Type , Kernel Size , Width , and Min Edge Strength parameters to define which edges you are looking for.
5. Click OK to add this step to the script and close the
 Parameter window.

Tip

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-edges-with-the-edge-tool.html language=enus -->
## TOPIC 00046: Detect Edges with the Edge Tool

- bundle_id: `ni-vision-assistant`
- source_path: `detect-edges-with-the-edge-tool.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-edges-with-the-edge-tool.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the Edge Tool from the Edge Detector list. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays the strength of the edges along the ROI and lists the number of edges found along that path. Select the option from Look For that specifies which

### Detect Edges with the Edge Tool

1. Select the Edge Tool from the Edge Detector list.
2. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays the strength of the edges along the ROI and lists the number of edges found along that path.
3. Select the option from Look For that specifies which edges you are looking for.
4. Set the Min Edge Strength , Filter Width , and Steepness parameters to define which edges you are looking for.
5. Click OK to add this step to the script and close the
 Parameter window.

Tip

Parent topic:

Analyzing and Processing Images

Related concepts:

- Highlight Details in an Image
- Selecting a Region of Interest (ROI)
- Detect Edges with Filters

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-edges-with-the-simple-edge-tool.html language=enus -->
## TOPIC 00047: Detect Edges with the Simple Edge Tool

- bundle_id: `ni-vision-assistant`
- source_path: `detect-edges-with-the-simple-edge-tool.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-edges-with-the-simple-edge-tool.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the Simple Edge Tool from the Edge Detector list. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays a line profile describing the path and lists the number of edges found along that path. Select the option from Look For that specifies whi

### Detect Edges with the Simple Edge Tool

1. Select the Simple Edge Tool from the Edge Detector list.
2. In the image, click and drag to select a path along which to search for edges. Vision Assistant displays a line profile describing the path and lists the number of edges found along that path.
3. Select the option from Look For that specifies which edges you are looking for.
4. Set the Level Type . Absolute Value specifies the threshold level in pixel intensities, and Relative Value specifies the threshold level as a percentage of the intensity range found in the line of pixels.
5. Set the Threshold Level (intensity level that you expect to constitute an edge) or click and drag the cursor on the line profile to position the cursor at the appropriate threshold level.
6. Click OK to add this step to the script and close the
 Setup window.

Tip

Parent topic:

Analyzing and Processing Images

Related concepts:

- Highlight Details in an Image
- Selecting a Region of Interest (ROI)
- Detect Edges with Filters

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-straight-edges.html language=enus -->
## TOPIC 00048: Detect Straight Edges

- bundle_id: `ni-vision-assistant`
- source_path: `detect-straight-edges.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-straight-edges.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Find Straight Edge step searches for a straight edge in a two-dimensional region of interest. The region of interest contains a number of search lines along which the step searches for sharp transitions in pixel intensities. A sharp transition typically characterizes the edge of an object in the

### Detect Straight Edges

The Find Straight Edge step searches for a straight edge in a
 two-dimensional region of interest. The region of interest contains a number of search
 lines along which the step searches for sharp transitions in pixel intensities. A sharp
 transition typically characterizes the edge of an object in the image. The step fits a
 straight line through the individual edge points of each search line to determine a
 straight edge on the object under inspection.

#### Main Tab

1. In the Step Name control, enter a descriptive name for
 the step.
2. Choose one of the following methods to specify the region of interest for the
 step:
  - Create a new region of interest.
    1. Select a tool from the menu toolbar that matches the type of
 region of interest you want to specify.
    2. Draw a region of interest on the image. Draw the region of
 interest so that it encloses the entire edge that you want to
 find but excludes as many edges of no interest as possible. Make
 sure the edge fills up most of the region length. Also, make
 sure that the region is at least 20 pixels wide on either side
 of the edge to accurately detect the points along the edge.
  - Select a previously defined region of interest from the
 Region of Interest listbox.

#### Settings Tab

1. Select the Direction property of the search lines. Select a search
 line orientation that is perpendicular to the edge. For example, the orientation
 of the edge in the following figure is vertical. Therefore, the search lines are
 horizontal. Also, select the search direction along the lines that has the
 least number of obstacles between the edge of the region and the object edge
 you want to find. In the following figure, the search direction is right to
 left so that the step avoids detecting the edges of miscellaneous
 objects. [IMAGE alt='image' src='GUID-330A3FD3-EB3F-4AE8-90F8-09363F67322E-a5.gif'] (1) Edge to
 Locate.
 (2) Search
 Region.
 (3) Search
 Lines.
 (4) Miscellaneous
 Objects in the Image.
2. Select the Edge Polarity of the edges you want to
 locate.
3. Choose the type of edges you want to detect from the Look
 For control. You can choose from First
 Edge or Best Edge .
4. If the automatically located straight edge does not correspond to the edge you expected to
 find, disable the Auto Setup control and manually adjust
 the edge location parameters. Use the edge information on the Advanced tab to
 determine appropriate settings for the edge location parameters.
5. If the Edge Strength Profile contains a strong peak that corresponds to the
 edge you want to find, adjust the blue edge strength line so that it lies
 slightly below the top of the edge peak but above all of the other peaks.
 Use the Search Line Index control to display edge
 profile information for each search line in the region of interest. 
 If the Edge Strength Profile does not contain peaks that correspond to all
 the edges, adjust the Kernel Size and
 Projection Width controls until distinct peaks
 appear. If the step still cannot find the edge or the location of the
 detected edge is inaccurate, adjust the Gap between
 the search lines until you achieve the expected result.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detect-texture-defects-2.html language=enus -->
## TOPIC 00049: Detect Texture Defects

- bundle_id: `ni-vision-assistant`
- source_path: `detect-texture-defects-2.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detect-texture-defects-2.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Detect Texture Defects

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. If you have not trained the software for the textures in which you want to
 detect defects, click New to launch the Texture Training
 Interface. Refer to the Texture Training Interface Help for more information
 about how to train textures in the Texture Training Interface.
5. If you have trained the software for the textures in which you want to detect
 defects, click the Browse 
 button to select the path to the classifier file. When
 you have selected the classifier file, the path to the file appears in the
 Texture Classifier File Path control. Note Click
 Edit to launch the Texture Training Interface
 and edit the classifier file.
6. Select a display mode. The Defects Only display mode
 displays a binary image of the defects detected in the image. The
 Overlay Defects display mode overlays the detected
 defects on the original image.

#### Segmentation Tab

The step automatically
 loads the setting specified in the classifier file.

1. Adjust the Initial Step Size to specify the offset
 between search windows when searching the entire image during the initial stage
 of defect detection. The default value of 0 indicates no overlap between
 windows. A smaller, non-zero step size processes the image in more detail, but
 increases the time required to process the image.
2. Adjust the Final Step Size to specify the offset between
 search windows when searching the regions that contain potential defects during
 the final stage of defect detection. The default value of 1 indicates that the
 classifier will reposition the window by 1 pixel as it searches for defects.
 Final Step Size cannot exceed the specified
 Initial Step Size value, unless Initial
 Step Size is 0.
3. Adjust the Min Defect Classification Score if the step
 does not detect the expected number of defects, or if the step identifies a
 texture region as a texture defect.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=detecting-features.html language=enus -->
## TOPIC 00050: Detecting Features

- bundle_id: `ni-vision-assistant`
- source_path: `detecting-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/detecting-features.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Take the following steps to configure how the step detects features. Enter a descriptive name for the step in the Step Name text box on the Main tab. Draw a region of interest where you want perform feature detection. Use the controls in the Feature Detection tab to configure the algorithm to detect

### Detecting Features

Take the following steps to configure how the step detects features.

1. Enter a descriptive name for the step in the Step Name text box on the Main tab.
2. Draw a region of interest where you want perform feature detection.
3. Use the controls in the Feature Detection tab to configure the algorithm to detect features and set the parameters the algorithm uses to determine feature points.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=edit-a-step-in-a-script.html language=enus -->
## TOPIC 00051: Edit a Step in a Script

- bundle_id: `ni-vision-assistant`
- source_path: `edit-a-step-in-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/edit-a-step-in-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to edit a script: Select the appropriate step in the Script window and click Edit Step or double-click the step that you want to edit. Change the function parameters in the Setup window. Click OK. If you modify the image and then decide that you do not want to save the c

### Edit a Step in a Script

Complete the following steps to edit a script:

1. Select the appropriate step in the Script window and click
 Edit Step 
 or double-click the step that you want to edit.
2. Change the function parameters in the Setup window.
3. Click OK .

Tip

- If you modify the image and then decide that you do not want to save the
 changes, click Cancel in the Setup window.
- You also can use Edit Step to modify the currently
 selected step.

Parent topic:

Creating Scripts

Related concepts:

- Add a Step to a Script
- Remove a Step from a Script
- Run a Script
- Save a Script

<!--NI_TOPIC bundle=ni-vision-assistant path=estimating-fpga-device-utilization.html language=enus -->
## TOPIC 00052: Estimating FPGA Device Utilization

- bundle_id: `ni-vision-assistant`
- source_path: `estimating-fpga-device-utilization.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/estimating-fpga-device-utilization.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Device Utilization Estimate table provides rough estimates of the amount of FPGA resources each Vision Assistant step uses, the total resources used by the script, and the resources available on the device. Refer to LabVIEW FPGA Module help for more information on FPGA resources. Total Used — Es

### Estimating FPGA Device Utilization

The Device Utilization Estimate table provides rough estimates of the amount of FPGA resources each Vision Assistant step uses, the total resources used by the script, and the resources available on the device.

Refer to LabVIEW FPGA Module help for more information on FPGA resources.

- Total Used — Estimates the amount of each resource used by all the steps
 in the script.

Note

- Total Available — Indicates the total amount of each resource available
 on the FPGA target.

The Device Utilization Estimate depends on the selected FPGA target.
 Select an FPGA target in Vision Assistant or in LabVIEW for the Vision Assistant Express
 VI.

#### Selecting an FPGA Target

The
 Device Utilization Estimate depends on the selected FPGA
 target. Select an FPGA target in Vision Assistant or in LabVIEW for the Vision
 Assistant Express VI.

#### Selecting an FPGA Target in Vision
 Assistant

There are two ways to select an FPGA target in Vision Assistant.

- Select an FPGA target from the startup screen when you launch Vision
 Assistant.
- Select File»Preferences , select the
 General tab, and select the target device from
 Target for Generated Code .

#### Selecting an FPGA Target for the
 Vision Assistant Express VI

1. Create a VI and add it to the LabVIEW project under an FPGA target.
2. Open the VI you created and drop the Vision Assistant Express VI on the block
 diagram.

Note

Pixel Bus Width

Pixel Bus Width

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=expand-dilate-objects-in-binary-images.html language=enus -->
## TOPIC 00053: Expand (Dilate) Objects in Binary Images

- bundle_id: `ni-vision-assistant`
- source_path: `expand-dilate-objects-in-binary-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/expand-dilate-objects-in-binary-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Dilate objects from the Basic Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Enter the numb

### Expand (Dilate) Objects in Binary Images

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Dilate objects from the Basic Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Enter the number of times that you want the dilation applied to the image in Iterations .
6. Click OK to apply the dilation and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images
- Expand (Dilate) Objects in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=expand-dilate-objects-in-grayscale-images.html language=enus -->
## TOPIC 00054: Expand (Dilate) Objects in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `expand-dilate-objects-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/expand-dilate-objects-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette. Select Dilate from the Gray Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Enter the number of

### Expand (Dilate) Objects in Grayscale Images

1. Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette.
2. Select Dilate from the Gray Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Enter the number of times that you want the dilation applied to the image in Iterations .
6. Click OK to apply the dilation and add this step to the script.

Tip

- The structuring element is a 2D array used as a binary mask to define the
 neighborhood of a pixel. You can modify the structuring element by clicking
 its cells. If a cell is black, it has a value of 1. If a cell is white
 (empty), it has a value of 0.
- Experiment with different coefficients and the Kernel
 Size to get the results you want.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Reduce (Erode) Objects in Grayscale Images
- Remove Small Objects (Open) from Grayscale Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=extract-color-planes-from-an-image.html language=enus -->
## TOPIC 00055: Extract Color Planes from an Image

- bundle_id: `ni-vision-assistant`
- source_path: `extract-color-planes-from-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/extract-color-planes-from-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the color plane that you want to extract. Click OK to add this step to the script. Because each color plane is made up of 8 bits, the color plane you extract is an 8-bit grayscale image.

### Extract Color Planes from an Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the color plane that you want to extract.
3. Click OK to add this step to the script.

Note

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=extract-the-contours-of-a-particle.html language=enus -->
## TOPIC 00056: Extract the Contours of a Particle

- bundle_id: `ni-vision-assistant`
- source_path: `extract-the-contours-of-a-particle.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/extract-the-contours-of-a-particle.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Gradient In to extract the interior contours of a particle or Gradient Out to extract the exterior contours of a particle. Set the Size of the Structuring Element. Click the cells o

### Extract the Contours of a Particle

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Gradient In to extract the interior contours of a particle or Gradient Out to extract the exterior contours of a particle.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the function and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=fill-gaps-and-holes-close-in-binary-images.html language=enus -->
## TOPIC 00057: Fill Gaps and Holes (Close) in Binary Images

- bundle_id: `ni-vision-assistant`
- source_path: `fill-gaps-and-holes-close-in-binary-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/fill-gaps-and-holes-close-in-binary-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Close objects from the Basic Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Click OK to app

### Fill Gaps and Holes (Close) in Binary Images

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Close objects from the Basic Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the closing and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Grayscale Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=fill-gaps-and-holes-close-in-grayscale-images.html language=enus -->
## TOPIC 00058: Fill Gaps and Holes (Close) in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `fill-gaps-and-holes-close-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/fill-gaps-and-holes-close-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette. Select Close from the Gray Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Click OK to apply th

### Fill Gaps and Holes (Close) in Grayscale Images

1. Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette.
2. Select Close from the Gray Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the closing and add this step to the script.

Tip

- The structuring element is a 2D array used as a binary mask to define the
 neighborhood of a pixel. You can modify the structuring element by clicking
 its cells. If a cell is black, it has a value of 1. If a cell is white
 (empty), it has a value of 0.
- Experiment with different coefficients and the Kernel
 Size to get the results you want.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Fill Gaps and Holes (Close) in Binary Images
- Reduce (Erode) Objects in Grayscale Images
- Remove Small Objects (Open) from Grayscale Images
- Smooth Object Boundaries in Grayscale Images
- Expand (Dilate) Objects in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=fill-holes-and-smooth-right-angles.html language=enus -->
## TOPIC 00059: Fill Holes and Smooth Right Angles

- bundle_id: `ni-vision-assistant`
- source_path: `fill-holes-and-smooth-right-angles.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/fill-holes-and-smooth-right-angles.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Thick to alter the shape of objects by adding parts to the object that match the pattern specified in the structuring element. Set the Size of the Structuring Element. Click the cel

### Fill Holes and Smooth Right Angles

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Thick to alter the shape of objects by adding parts to the object that match the pattern specified in the structuring element.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the thickening and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Fill Holes
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth an Image with Filtering
- Smooth Object Boundaries in Binary Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=fill-holes.html language=enus -->
## TOPIC 00060: Fill Holes

- bundle_id: `ni-vision-assistant`
- source_path: `fill-holes.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/fill-holes.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Fill holes. Click OK to fill the holes and add this step to the script.

### Fill Holes

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Fill holes .
3. Click OK to fill the holes and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Gaps and Holes (Close) in Binary Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Fill Holes and Smooth Right Angles
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=filter-an-image-with-a-custom-convolution-fil.html language=enus -->
## TOPIC 00061: Filter an Image with a Custom Convolution Filter

- bundle_id: `ni-vision-assistant`
- source_path: `filter-an-image-with-a-custom-convolution-fil.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/filter-an-image-with-a-custom-convolution-fil.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette. Select Convolution – Custom from the Filters list. Set the Kernel Size and coefficients. Click OK to filter the image and add this step to the script. Experiment with different coefficients and the Ker

### Filter an Image with a Custom Convolution Filter

1. Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette.
2. Select Convolution – Custom from the Filters list.
3. Set the Kernel Size and coefficients.
4. Click OK to filter the image and add this step to the script.

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Detect Edges with Filters
- Highlight Details in an Image
- Smooth an Image with Filtering

<!--NI_TOPIC bundle=ni-vision-assistant path=filter-objects-based-on-particle-measurements.html language=enus -->
## TOPIC 00062: Filter Objects Based on Particle Measurements

- bundle_id: `ni-vision-assistant`
- source_path: `filter-objects-based-on-particle-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/filter-objects-based-on-particle-measurements.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Double-click each object measurement in the Particle Filter list that you want the particle filter to include as criteria. Enter the parameter range for each filter criteria. Select the action you want to perform. Remove removes partic

### Filter Objects Based on Particle Measurements

1. In the Step Name textbox, enter a descriptive name for the step.
2. Double-click each object measurement in the Particle Filter list that you want the particle filter to include as criteria.
3. Enter the parameter range for each filter criteria.
4. Select the action you want to perform. Remove removes particles that do not fit in the range bounded by the minimum and maximum values for the selected measurement. Keep keeps particles that fit in the range bounded by the minimum and maximum values for the selected measurement.
5. Click OK to filter the image and add this step to the script.

Tip

Exclude Interval

Parent topic:

Analyzing and Processing Images

Related information:

- Filter Criteria Concepts
- Particle Filter

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-angle-made-by-three-or-four-points.html language=enus -->
## TOPIC 00063: Find the Angle Made by Three or Four Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-angle-made-by-three-or-four-points.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-angle-made-by-three-or-four-points.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Angle Made by Three or Four Points

1. Click Machine Vision»Caliper or select Caliper 
 from the Machine Vision tab in the Processing Functions
 palette. Vision Assistant displays and numerically labels all points that you have
 located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid,
 Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle
 Analysis, or Circle Detection functions.
2. Select Angle Defined by 3 Points or Angle Defined by 4 Points .
3. Select three or four points on the image by clicking them. If you select three points, the
 second point is used as the common vertex, and the angle is measured between (1,2)
 and (2,3). If you select four points, the angle is measured between (1,2) and
 (3,4).
4. Click Measure .
5. Click OK to add this step to the script.

Note

- You must have already located the position of objects in the image using one
 or more of the following functions: Edge Detector, Find Straight Edge, Find
 Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color
 Location, Shape Matching, Particle Analysis, or Circle Detection.
- The angle is measured in degrees, counterclockwise.

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-angle-made-by-two-points.html language=enus -->
## TOPIC 00064: Find the Angle Made by Two Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-angle-made-by-two-points.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-angle-made-by-two-points.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Angle Made by Two Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select either Angle from Horizontal or Angle from Vertical , depending on the type of angle you want.
3. Select two points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

- You must have already located the position of objects in the image using one
 or more of the following functions: Edge Detector, Find Straight Edge, Find
 Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color
 Location, Shape Matching, Particle Analysis, or Circle Detection.
- The angle is measured in degrees, counterclockwise.

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-area-enclosed-by-three-or-more-point.html language=enus -->
## TOPIC 00065: Find the Area Enclosed by Three or More Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-area-enclosed-by-three-or-more-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-area-enclosed-by-three-or-more-point.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Area Enclosed by Three or More Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Area .
3. Select three or more points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-center-of-mass-using-three-or-more-p.html language=enus -->
## TOPIC 00066: Find the Center of Mass Using Three or More Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-center-of-mass-using-three-or-more-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-center-of-mass-using-three-or-more-p.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Center of Mass Using Three or More Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Center of Mass .
3. Select three or more points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- The center point is available for new measurements when you close the
 caliper parameter window and re-open it.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-center-of-two-points.html language=enus -->
## TOPIC 00067: Find the Center of Two Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-center-of-two-points.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-center-of-two-points.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Center of Two Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Mid Point .
3. Select two points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- The center point is available for new measurements when you close the
 caliper parameter window and re-open it.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-circular-fit-using-three-or-more-poi.html language=enus -->
## TOPIC 00068: Find the Circular Fit Using Three or More Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-circular-fit-using-three-or-more-poi.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-circular-fit-using-three-or-more-poi.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Circular Fit Using Three or More Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Circle Fit .
3. Select three or more points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- The center of the circle is available for new measurements when you close
 the caliper parameter window and re-open it.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-distance-between-two-points.html language=enus -->
## TOPIC 00069: Find the Distance Between Two Points

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-distance-between-two-points.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-distance-between-two-points.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern

### Find the Distance Between Two Points

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you have located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Distance .
3. Select two points on the image by clicking them.
4. Click Measure .
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-intersection-of-two-lines.html language=enus -->
## TOPIC 00070: Find the Intersection of Two Lines

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-intersection-of-two-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-intersection-of-two-lines.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Match

### Find the Intersection of Two Lines

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Line Intersections in Geometric Feature .
3. Select four points (for example, points 1, 2, 3, and 4) on the image by clicking them.
4. Click Measure . Vision Assistant computes the location of the intersection of the lines represented by the lines (point 1, point 2) and (point 3, point 4).
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=find-the-perpendicular-projection-of-a-point.html language=enus -->
## TOPIC 00071: Find the Perpendicular Projection of a Point on a Line

- bundle_id: `ni-vision-assistant`
- source_path: `find-the-perpendicular-projection-of-a-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/find-the-perpendicular-projection-of-a-point.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Match

### Find the Perpendicular Projection of a Point on a Line

1. Click Machine Vision»Caliper or select Caliper from the Machine Vision tab in the Processing Functions palette. Vision Assistant displays and numerically labels all points that you located with the Edge Detector, Find Straight Edge, Find Circular Edge, Centroid, Pattern Matching, Color Pattern Matching, Color Location, Shape Matching, Particle Analysis, or Circle Detection functions.
2. Select Perpendicular Projection in Geometric Feature .
3. Select three points (for example, points 1, 2, and 3) on the image by clicking them.
4. Click Measure . Vision Assistant computes the location of the perpendicular projection of point 3 on the line (point 1, point 2).
5. Click OK to add this step to the script.

Note

Tip

- You also can select points on the image by double-clicking them in the
 Points list. When a point is selected,
 Vision Assistant places a check mark to the left of the item.
- To save the data, click the Send Data to Excel button
 or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines

<!--NI_TOPIC bundle=ni-vision-assistant path=get-an-image.html language=enus -->
## TOPIC 00072: Get an Image

- bundle_id: `ni-vision-assistant`
- source_path: `get-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/get-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Click the Browse button to navigate to the image you want the script to open. Click Open. Click OK to add this step to the script and close the Parameter window. You can use only the Image»Get Image or select Get Image in the Image tab

### Get an Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Click the Browse 
 button to navigate to the image you
 want the script to open.
3. Click Open .
4. Click OK to add this step to the script and close the
 Parameter window.

Note

Image»Get Image

Get
 Image

Image

Parent topic:

Analyzing and Processing Images

Related concepts:

- Acquiring a Sequence of Images
- Acquire Images in Color
- Add New Images to the Image Browser
- Add Processed Images to the Image Browser
- Grabbing an Image (Continuous Image Acquisition)
- Open Images in Vision Assistant
- Image Acquisition in Vision Assistant
- Snapping an Image (Single Image Acquisition)

<!--NI_TOPIC bundle=ni-vision-assistant path=getting-help-in-vision-assistant.html language=enus -->
## TOPIC 00073: Getting Help in Vision Assistant

- bundle_id: `ni-vision-assistant`
- source_path: `getting-help-in-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/getting-help-in-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can get help in Vision Assistant in any of the following ways: Click the Context Help button on the Vision Assistant toolbar to launch the Context Help window. The content of the Context Help window automatically updates to reflect what is currently selected in Vision Assistant. Move the mouse p

### Getting Help in Vision Assistant

You can get help in Vision Assistant in any of the following ways:

- Click the Context Help 
 button on the Vision Assistant toolbar to launch the
 Context Help window. The content of the
 Context Help window automatically updates to reflect what
 is currently selected in Vision Assistant. Move the mouse pointer over the buttons
 in the toolbar, Script window,
 Reference window, Acquisition 
 window, or Image Browser for tooltips that describe what each
 button does.
- Click Help»Solution Wizard in the Vision Assistant menu to launch the
 Vision Assistant Solution Wizard and view typical uses of Vision in imaging and
 machine vision applications.
- Click Start»All Programs»National Instruments»Vision Assistant
 Documentation to launch the Vision Assistant Tutorial. This manual
 is designed to teach you the fundamental features of Vision Assistant through
 interactive discussions and examples, including particle analysis and part gauging
 examples.
- Click Start»All Programs»National Instruments»Vision Documentation and
 select NIVisionConcepts.chm to launch the Vision Concepts Help. This help file
 contains information about the algorithms, utilities, and tools available in
 Vision Assistant and the Vision Development Module library.
- Refer to the Vision Acquisition Software Release Notes for more information
 about configuring NI-IMAQ driver software, image acquisition devices, and cameras
 using Measurement & Automation Explorer (MAX).

Tip

- The National Instruments Web site provides information about Vision hardware
 and software. Visit Machine Vision at ni.com/vision .
- Several example scripts are installed with Vision Assistant. You can run
 these scripts to learn more about Vision Assistant scripting capabilities.
 You also can customize these scripts for your own applications. By default,
 the scripts are installed at
 <Vision Assistant>\Examples , where
 <Vision Assistant> is the location to which
 Vision Assistant is installed.
- Read the Technical Support and Professional Services page for
 more ways to get help.

Related concepts:

- Technical Support and Professional Services
- Using the Solution Wizard

<!--NI_TOPIC bundle=ni-vision-assistant path=grabbing-an-image-continuous-image-acquisitio.html language=enus -->
## TOPIC 00074: Grabbing an Image (Continuous Image Acquisition)

- bundle_id: `ni-vision-assistant`
- source_path: `grabbing-an-image-continuous-image-acquisitio.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/grabbing-an-image-continuous-image-acquisitio.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Acquire Image. Vision Assistant displays the Acquire Images Processing Functions palette. Click the appropriate acquisition step. The Devices window displays all image acquisition devices and channels or ports available for the computer. Select the device and channel or port you want to u

### Grabbing an Image (Continuous Image
 Acquisition)

1. Click File»Acquire Image . Vision Assistant displays the Acquire Images Processing Functions palette.
2. Click the appropriate acquisition step. The Devices window displays all
 image acquisition devices and channels or ports available for the computer.
3. Select the device and channel or port you want to use to acquire an image.
4. Select Acquire Continuous Images 
 to acquire and display images in continuous mode at the
 maximum rate. This operation is known as a grab.
5. Select Acquire Continuous Images again to stop the acquisition and
 display the last acquired image.
6. Select Store Acquired Image in Browser 
 to send the image to the Image Browser.
7. Process the image as you would any other image in Vision Assistant.

Tip

Parent topic:

Acquiring Images

Related concepts:

- Acquiring a Sequence of Images
- Acquire Images in Color
- Image Acquisition in Vision Assistant
- Snapping an Image (Single Image Acquisition)

<!--NI_TOPIC bundle=ni-vision-assistant path=highlight-details-in-an-image.html language=enus -->
## TOPIC 00075: Highlight Details in an Image

- bundle_id: `ni-vision-assistant`
- source_path: `highlight-details-in-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/highlight-details-in-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette. Select Convolution-Highlight Details from the Filters list. Adjust the Kernel Size and coefficients, if necessary. Click OK to filter the image and add this step to the script. Experiment with differen

### Highlight Details in an Image

1. Click Grayscale»Filters or click Filters in the Grayscale tab of the Processing Functions palette.
2. Select Convolution-Highlight Details from the Filters list.
3. Adjust the Kernel Size and coefficients, if necessary.
4. Click OK to filter the image and add this step to the script.

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Detect Edges with Filters
- Filter an Image with a Custom Convolution Filter
- Smooth an Image with Filtering

<!--NI_TOPIC bundle=ni-vision-assistant path=how-to-acquire-images-with-a-usb-device.html language=enus -->
## TOPIC 00076: How to Acquire Images with a USB Device

- bundle_id: `ni-vision-assistant`
- source_path: `how-to-acquire-images-with-a-usb-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/how-to-acquire-images-with-a-usb-device.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Devices, select the USB device you want to use to acquire the image. Click the Acquire Single Image, Acquire Continuous Images, or Sequence Acquisition button. Click Close to exit the Setup window.

### How to Acquire Images with a USB Device

1. In Devices , select the USB device you want to use to acquire the
 image.
2. Click the Acquire Single Image , Acquire Continuous Images , or Sequence Acquisition button.
3. Click Close to exit the Setup window.

Parent topic:

Acquiring Images

Related concepts:

- Snapping an Image (Single Image Acquisition)
- Grabbing an Image (Continuous Image Acquisition)
- Acquiring a Sequence of Images

<!--NI_TOPIC bundle=ni-vision-assistant path=how-to-simulate-an-image-acquisition.html language=enus -->
## TOPIC 00077: How to Simulate an Image Acquisition

- bundle_id: `ni-vision-assistant`
- source_path: `how-to-simulate-an-image-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/how-to-simulate-an-image-acquisition.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Acquire Image or click Acquire Images. Click Simulate Acquisition in the Acquisition functions list. Click the Browse button to select a path to a directory of images, and click Select Cur Dir. Click the Acquire Single Image, Acquire Continuous Images, or Sequence Acquisition button. Clic

### How to Simulate an Image Acquisition

1. Click File»Acquire Image or click Acquire Images .
2. Click Simulate Acquisition in the Acquisition functions list.
3. Click the Browse 
 
 button to select a path to a directory of images, and click Select Cur
 Dir .
4. Click the Acquire Single Image , Acquire Continuous Images , or Sequence Acquisition button.
5. Click Close to exit the Setup window.

Parent topic:

Acquiring Images

Related concepts:

- Snapping an Image (Single Image Acquisition)
- Grabbing an Image (Continuous Image Acquisition)
- Acquiring a Sequence of Images

<!--NI_TOPIC bundle=ni-vision-assistant path=image-acquisition-in-vision-assistant.html language=enus -->
## TOPIC 00078: Image Acquisition in Vision Assistant

- bundle_id: `ni-vision-assistant`
- source_path: `image-acquisition-in-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/image-acquisition-in-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: To start acquiring images, select File»Acquire Image or click Acquire Images. If Vision Assistant is launched from LabVIEW using the Vision Assistant Express VI, the acquisition is done by using the Vision Acquisition Express VI and not from the path specified above. You can acquire live images in V

### Image Acquisition in Vision Assistant

To start acquiring images, select File»Acquire Image or click
 Acquire Images.

Note

You can acquire live images in Vision Assistant with various National Instruments Smart Cameras,
 digital and analog frame grabbers, DCAM-compliant IEEE 1394 cameras, and Gigabit
 Ethernet (GigE) Vision cameras. For information about driver software, refer to the
 Vision Acquisition Software Release Notes.

If the computer does not have an image acquisition device, you can simulate a live acquisition
 with the *Simulate Acquisition* function. You can interact with the simulated
 acquisition as you would with a live acquisition.

Vision Assistant offers three types of acquisitions: snap, grab, and sequence.

- A snap acquires and displays a single image.
- A grab acquires and displays images in a continuous mode at maximum rate, which is useful when you need to focus the camera.
- A sequence acquires images according to settings that you specify in the
 Sequence tab of the Acquisition
 Interface window and sends the images to the Image Browser.

Parent topic:

Acquiring Images

Related concepts:

- How to Simulate an Image Acquisition
- Snapping an Image (Single Image Acquisition)
- Grabbing an Image (Continuous Image Acquisition)
- Acquiring a Sequence of Images
- Acquire Images in Color

<!--NI_TOPIC bundle=ni-vision-assistant path=important-information.html language=enus -->
## TOPIC 00079: Important Information

- bundle_id: `ni-vision-assistant`
- source_path: `important-information.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/important-information.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`

### Important Information

- [Warranty](warranty.html)
- [Copyright](copyright.html)
- [Trademarks](trademarks.html)
- [Patents](patents.html)
- [WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS](warning-regarding-use-of-national-instruments.html)

<!--NI_TOPIC bundle=ni-vision-assistant path=invert-a-binary-image.html language=enus -->
## TOPIC 00080: Invert a Binary Image

- bundle_id: `ni-vision-assistant`
- source_path: `invert-a-binary-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/invert-a-binary-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Click OK to reverse the dynamic of an image containing two different grayscale populations.

### Invert a Binary Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Click OK to reverse the dynamic of an image containing two different
 grayscale populations.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=label-objects.html language=enus -->
## TOPIC 00081: Label Objects

- bundle_id: `ni-vision-assistant`
- source_path: `label-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/label-objects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Label objects. Click OK to add this step to the script. Labeling is especially useful when viewing images containing many objects that are not clearly separated.

### Label Objects

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Label objects .
3. Click OK to add this step to the script.

Tip

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=managingimages.html language=enus -->
## TOPIC 00082: Managing Images

- bundle_id: `ni-vision-assistant`
- source_path: `managingimages.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/managingimages.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`

### Managing Images

- [Open Images in Vision Assistant](open-images-in-vision-assistant.html)
- [Open AVI Files in Vision Assistant](open-avi-files-in-vision-assistant.html)
- [Add New Images to the Image Browser](add-new-images-to-the-image-browser.html)
- [Processing an Image](processing-an-image.html)
- [Add Processed Images to the Image Browser](add-processed-images-to-the-image-browser.html)
- [Browse Images in the Image Browser](browse-images-in-the-image-browser.html)
- [Access Images from the Reference Window](access-images-from-the-reference-window.html)
- [Save Images](save-images.html)
- [Print Images](print-images.html)

<!--NI_TOPIC bundle=ni-vision-assistant path=mask-an-image.html language=enus -->
## TOPIC 00083: Mask an Image

- bundle_id: `ni-vision-assistant`
- source_path: `mask-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/mask-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Mask an Image

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Mask Tab

Choose one of the following
 methods to mask an image:

- Mask an image from a ROI . 
 Tip You can select a
 new region of interest by selecting an ROI tool and selecting a new area in
 the image.
  1. Select Create from ROI .
  2. Select an ROI tool from the toolbar and draw the region of
 interest.
  3. Click Set ROI .
  4. Select mask options.
  5. Click OK to add this step to the script.
- Mask an Image from an image file.
  1. Select Create from Image File .
  2. Click the Browse button, navigate to the location
 of the image file, select the file, and click
 OK .
  3. Select mask options.
  4. Click OK to add this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=match-colors-in-an-image-to-a-template.html language=enus -->
## TOPIC 00084: Match Colors in an Image to a Template

- bundle_id: `ni-vision-assistant`
- source_path: `match-colors-in-an-image-to-a-template.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/match-colors-in-an-image-to-a-template.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Match Colors in an Image to a Template

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Template Tab

1. Create or select the template you want to use for comparison. 
 By default, the center of the template is used as the focal point of the
 template. You can change the location of the focal point to any position in
 the template. Change the focal point of the template by dragging the red
 pointer in the template image or adjusting the Match
 Offset values.
  - To create a new template, complete the following steps:
    1. Click Create Template .
    2. Select an ROI and click OK .
    3. Enter a File Name for the template and
 click OK .
  - To use an existing template, complete the following steps:
    1. Click Load from File .
    2. Browse to the appropriate template image and click
 OK .
2. Modify the Ignore Black and White and Sat.
 Threshold parameters as necessary.

#### Settings Tab

1. Set the Minimum Match Score .
2. Click OK to add the step to the script and exit the
 Parameter window.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=measure-distances-between-edges-using-the-cla.html language=enus -->
## TOPIC 00085: Measure Distances Between Edges Using the Clamp (Rake-Based) Tool

- bundle_id: `ni-vision-assistant`
- source_path: `measure-distances-between-edges-using-the-cla.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/measure-distances-between-edges-using-the-cla.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Clamp function works only with 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link

### Measure Distances Between Edges Using the Clamp (Rake-Based) Tool

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Clamp Tab

1. Select one of the ROI tools. Click and drag to select a path along which to
 search for edges and find the distance.
2. Select the appropriate Process . In the Edge
 Strength Profile , Vision Assistant displays the average of the
 line profiles of all the lines used for edge detection.
3. Adjust the Gap , Edge 
 Strength , Smoothing , and
 Steepness parameters until the
 Process window indicates that the step has correctly
 detected the edges of the object you want to measure.
4. Click OK to add this step to the script and close the
 Parameter window.

Tip

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=measure-distances-between-edges-using-the-max.html language=enus -->
## TOPIC 00086: Measure Distances Between Edges Using the Max Clamp Tool

- bundle_id: `ni-vision-assistant`
- source_path: `measure-distances-between-edges-using-the-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/measure-distances-between-edges-using-the-max.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Contour-Based Max Clamp function works with RGB, HSL, and 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defi

### Measure Distances Between Edges Using the Max Clamp Tool

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Clamp Tab

1. Select one of the ROI tools. Click and drag to select a path along which to
 search for edges and find the distance.
2. Adjust the Edge Threshold , Minimum
 Length , and Search Step Size parameters
 until the Process window indicates that the step has correctly detected the
 contours of the object you want to measure.
3. Adjust the Search Direction , Angle
 Range , Start Edge Polarity , and
 End Edge Polarity parameters until the Process window indicates that the clamp addresses the detected
 edges correctly.
4. Click OK to add this step to the script and close the
 Parameter window.

Tip

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=migrating-to-a-development-environment.html language=enus -->
## TOPIC 00087: Migrating to a Development Environment

- bundle_id: `ni-vision-assistant`
- source_path: `migrating-to-a-development-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/migrating-to-a-development-environment.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating a LabVIEW VIYou can create a LabVIEW VI using Vision Assistant. Refer to LabVIEW VI Creation (Tools»Create LabVIEW VI) for more information about creating a LabVIEW VI. Creating C CodeYou can create C code using Vision Assistant. Refer to C Code Creation (Tools»Create C Code) for more infor

### Migrating to a Development Environment

#### Creating a LabVIEW VI

You can create a
 LabVIEW VI using Vision Assistant. Refer to *LabVIEW VI Creation (Tools»Create
 LabVIEW VI)* for more information about creating a LabVIEW
 VI.

#### Creating C Code

You can create C code
 using Vision Assistant. Refer to *C Code Creation (Tools»Create C Code)*
 for more information about creating C code.

#### Creating .NET Code

You can create .NET
 code using Vision Assistant. Refer to *.NET Code Creation (Tools»Create .NET
 Code)* for more information about creating .NET code.

Related concepts:

- Creating C Code
- Creating .NET Code
- Creating a LabVIEW VI

<!--NI_TOPIC bundle=ni-vision-assistant path=modify-brightness-contrast-and-gamma-values-o.html language=enus -->
## TOPIC 00088: Modify Brightness, Contrast, and Gamma Values of an Image

- bundle_id: `ni-vision-assistant`
- source_path: `modify-brightness-contrast-and-gamma-values-o.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/modify-brightness-contrast-and-gamma-values-o.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Modify the Brightness, Contrast, and Gamma values with the slide or by manually entering the value. When you process a color image, you can apply Brightness, Contrast, and Gamma modifications to each Color Plane separately, or you can

### Modify Brightness, Contrast, and Gamma Values of an Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Modify the Brightness , Contrast , and Gamma values with the slide or by manually entering the value. When you process a color image, you can apply Brightness , Contrast , 
and Gamma modifications to each Color Plane separately, or you can apply the same transformation to all color planes at the same time.
3. Click OK to add the step to the script.

Tip

- If you modify the values and want to return to the source image, click the
 Reset button.
- You can modify the brightness of a portion of an image by drawing an
 ROI.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=open-a-script.html language=enus -->
## TOPIC 00089: Open a Script

- bundle_id: `ni-vision-assistant`
- source_path: `open-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/open-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to open a script: SelectFile»Open Script or click the Open button in the Script window. Browse to the script you want to open. Select the script. Click OK.

### Open a Script

Complete the following steps to open a script:

1. Select File»Open Script or click the Open 
 
 button in the Script window.
2. Browse to the script you want to open.
3. Select the script.
4. Click OK .

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=open-avi-files-in-vision-assistant.html language=enus -->
## TOPIC 00090: Open AVI Files in Vision Assistant

- bundle_id: `ni-vision-assistant`
- source_path: `open-avi-files-in-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/open-avi-files-in-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Open AVI File. Audio Video Interleaved (AVI) files are movie files that include a collection of images. From the Look In list, select the drive on which the AVI file is located. Browse to the file and click OK. Vision Assistant loads the AVI file into the Image Browser. When you select a

### Open AVI Files in Vision Assistant

1. Click File»Open AVI File . Audio Video Interleaved (AVI)
 files are movie files that include a collection of images.
2. From the Look In list, select the drive on which the AVI
 file is located.
3. Browse to the file and click OK . Vision Assistant loads the
 AVI file into the Image Browser. Tip When you select a file from the
 list, the Preview Image window plays the AVI
 movie file. To view the sequence in a continuous play mode,
 enable the Continuous Play option. To view individual
 images of the AVI file, disable the Continuous
 Play option and adjust the slide below the Preview
 Image window. The Frame # indicator
 displays the index of the image in the Preview Image
 window. You can select all images by clicking the All
 Images radio button in the Images Selection section of the
 window, or you can enter a range of frames to select by entering values in the
 From, To, and
 Step controls.
4. Double-click the image to begin processing it.

Parent topic:

Managing Images

Related concepts:

- Add Processed Images to the Image Browser
- Browse Images in the Image Browser
- Print Images
- Save Images

<!--NI_TOPIC bundle=ni-vision-assistant path=open-images-in-vision-assistant.html language=enus -->
## TOPIC 00091: Open Images in Vision Assistant

- bundle_id: `ni-vision-assistant`
- source_path: `open-images-in-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/open-images-in-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select File»Open Image or click Open Image . From the Look In list, select the drive on which the image is located. Browse to the image and click OK. Vision Assistant loads the image file into the Image Browser. Double-click the image to start processing it. You can select all files in a folder by e

### Open Images in Vision Assistant

1. Select File»Open Image or click Open Image 
 .
2. From the Look In list, select the drive on which the image is located.
3. Browse to the image and click OK . Vision Assistant loads the image file into the Image Browser.
4. Double-click the image to start processing it.

Tip

Select all files

Preview Image

Preview
 Image

Parent topic:

Managing Images

Related concepts:

- Add Processed Images to the Image Browser
- Browse Images in the Image Browser
- Print Images
- Save Images

<!--NI_TOPIC bundle=ni-vision-assistant path=overlay-figures-text-or-bitmaps-on-an-image.html language=enus -->
## TOPIC 00092: Overlay Figures, Text, or Bitmaps on an Image

- bundle_id: `ni-vision-assistant`
- source_path: `overlay-figures-text-or-bitmaps-on-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/overlay-figures-text-or-bitmaps-on-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main TabIn the Step Name textbox, enter a descriptive name for the step. Overlay Tab Select the type of overlay you want to add to the image from the tools palette. Draw the overlay in the image. Vision Assistant adds the element to the Overlays drop-down list. You can adjust the size and position o

### Overlay Figures, Text, or Bitmaps on an Image

#### Main
 Tab

In the Step Name textbox, enter a descriptive
 name for the step.

#### Overlay Tab

1. Select the type of overlay you want to add to the image from the tools
 palette.
2. Draw the overlay in the image. Vision Assistant adds the element to the
 Overlays drop-down list. You can adjust the size and position of the element
 by using the Selection Tool
 [IMAGE alt='image' src='GUID-B1845C3D-20E4-4A4C-A389-1F6ED6DBD3E8-a5.gif'] or by modifying the element
 Parameters. 
 Note To delete an
 overlay element, select the element in the Overlays drop-down list and click
 Delete.
3. Set the overlay color.
4. Set any Parameters specific to the element you created,
 such as the overlay text.

#### Layer Management Tab

1. Use the Layer Management controls to set the order in which Vision Assistant
 overlays elements on the image. The Overlay Elements table lists all the
 overlays in the reverse order they were created. The first overlay in the table
 is the topmost layer. To move an element up or down the stack of layers,
 select the element in the Overlay Elements table and click either
 Up or Down.
2. Click OK to add the step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=overview.html language=enus -->
## TOPIC 00093: Vision Assistant Overview

- bundle_id: `ni-vision-assistant`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/overview.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Vision Assistant to prototype and test image processing algorithms or applications. After prototyping and testing the algorithm, use the following applications: LabVIEW VI Creation Wizard to create a block diagram of the algorithm. LabVIEW FPGA VI Creation Wizard to create a block diagram to run

### Vision Assistant
 Overview

Use Vision Assistant to prototype and test image processing algorithms or
 applications.

After prototyping and testing the algorithm, use the following applications:

- LabVIEW VI Creation Wizard to create a block diagram of the algorithm.
- LabVIEW FPGA VI Creation Wizard to create a block diagram to run the algorithm on an
 FPGA target.
- C Code Creation Wizard to create the C code of the algorithm.
- .NET Code Creation wizard to create C# or Visual Basic .NET code of the
 algorithm.
- Vision machine vision and image processing libraries to implement the solution in
 LabVIEW, LabVIEW FPGA, LabWindows™/CVI™, or in Visual Studio .NET.

<!--NI_TOPIC bundle=ni-vision-assistant path=patents.html language=enus -->
## TOPIC 00094: Patents

- bundle_id: `ni-vision-assistant`
- source_path: `patents.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/patents.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: For patents covering the NI products/technology, refer to the appropriate location: Help»Patents in your software, the patents.txt file on your media, or the Patent Notice at ni.com/patents.

### Patents

For patents covering the NI products/technology, refer to the appropriate location: Help»Patents in your software, the patents.txt file on your media, or the Patent Notice at ni.com/patents.

Parent topic:

Important Information

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-a-grid-calibration.html language=enus -->
## TOPIC 00095: Perform a Grid Calibration

- bundle_id: `ni-vision-assistant`
- source_path: `perform-a-grid-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-a-grid-calibration.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette. Select Grid Calibration and click OK. Select the type of Distortion that applies to the image. Click Next. Select Threshold Range values to separate the dots of the grid from the rest of t

### Perform a Grid Calibration

1. Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette.
2. Select Grid Calibration and click OK .
3. Select the type of Distortion that applies to the image.
4. Click Next .
5. Select Threshold Range values to separate the dots of the grid from the rest of the image. When you select the Threshold Range , the following operations are performed on the image:
  - The image is thresholded using the range you provide in Threshold Range .
  - Particles that are touching the image borders are removed using the Remove border objects function.
  - Particles that are too small or that are larger than the largest dot are rejected using the Particle Filter function.
6. Click Next .
7. Select the real-world distance between the grid dots in the x and y directions. If the grid
 does not cover the entire image, draw a region of interest around the grid or a
 portion of the grid to learn the calibration information only in this area. 
 Tip Double-click the
 last point of the polygonal region of interest to close the region.
8. Click Next .
9. Select the origin of the calibration axis by entering the X - and Y -coordinates or by selecting an Existing Point from the list.
10. Select the User-Defined Angle of the calibration or select an Existing Angle . If you choose an Existing Angle from the list, you can add 90°, 180°, or 270° to the value.
11. Select an Axis Reference .
12. Click OK to learn the calibration.
13. Browse to the directory you want to save the calibration information in, enter a File name , and click OK .
14. Click OK to save the step in the script and close the Parameter window.

#### Control Descriptions

- Open Image — Grid image on which to base the calibration.
 This image must be the same size as the image you want to calibrate.
- Distortion — Type of image distortion.
- Threshold Range — Minimum and maximum intensity values to
 include in the threshold range.
- X Spacing — Distance between two dots in the x
 direction.
- Y Spacing — Distance between two dots in the y
 direction.
- Unit — Real-world unit of the distances.
- Axis Origin
  - User Defined — X- and y-coordinates of the pixel
 that you want to use as the calibration axis origin.
  - Existing Point — Point defined in a previous step
 that you want to use as the calibration axis origin.
- X Axis Angle
  - User Defined — Angle you want to use between the
 x-axis of the calibration axes and the horizontal axis of the
 image.
  - Existing Angle — Angle defined in a previous step
 that you want to use between the x-axis of the calibration axes and the
 horizontal axis of the image. You can select a value from the
 + list to add to the
 Angle value.
- Axis Reference — Direction of the y-axis.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Threshold a Grayscale Image
- Remove Objects Touching the Image Border
- Filter Objects Based on Particle Measurements

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-a-histogram.html language=enus -->
## TOPIC 00096: Perform a Histogram

- bundle_id: `ni-vision-assistant`
- source_path: `perform-a-histogram.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-a-histogram.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Perform a Histogram

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Histogram Tab

1. If you want to perform a histogram for a portion of the image, select an ROI
 tool and draw an ROI on the image. The histogram displays data for the currently
 selected region.
2. Click OK to add the step to the script.

Note

Tip

- To display the histogram for the entire image after you selected an ROI
 or to delete the selected ROI, click the image or press the
 <Delete> key.
- If you want to save the histogram data, click the Send Data
 to Excel button or the Save
 Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Selecting a Region of Interest (ROI)

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-a-line-profile.html language=enus -->
## TOPIC 00097: Perform a Line Profile

- bundle_id: `ni-vision-assistant`
- source_path: `perform-a-line-profile.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-a-line-profile.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Perform a Line Profile

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Line Profile Tab

1. Select one of the line tools from the toolbar and draw a line on the image. The
 line profile displays data for the currently selected pixels.
2. Click OK to add the step to the script.

Note

Tip

- Use the arrow keys (←, ↑, →, ↓) to move the line one pixel in the
 corresponding direction.
- To save the data, click the Send Data to Excel 
 button or the Save Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Selecting a Region of Interest (ROI)

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-a-particle-analysis.html language=enus -->
## TOPIC 00098: Perform a Particle Analysis

- bundle_id: `ni-vision-assistant`
- source_path: `perform-a-particle-analysis.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-a-particle-analysis.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Assistant calculates measurements for every particle in the image and displays the results. In the Step Name textbox, enter a descriptive name for the step. Click OK to add this step to the script. Vision Assistant assigns numerical labels to all particles in the particle analysis. Select Sho

### Perform a Particle Analysis

1. Vision Assistant calculates measurements for every particle in the image and displays the results.
2. In the Step Name textbox, enter a descriptive name for the step.
3. Click OK to add this step to the script.

Tip

- Vision Assistant assigns numerical labels to all particles in the particle
 analysis. Select Show Labels to display labels. When
 you click a labeled particle, Vision Assistant highlights the particle and
 the corresponding results in the table. You also can click the results to
 highlight the corresponding particle in the image.
- To remove or add particle measurements displayed in the
 Results table, click the Select
 Measurements button and click the object measurements to
 select or deselect them. Vision Assistant places a check mark to the left of
 the measurements currently displayed.
- To save the data, click the Send Data to Excel 
 button or the Save
 Results 
 button.

Parent topic:

Analyzing and Processing Images

Related information:

- Filter Criteria Concepts
- Particle Filter

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-a-simple-calibration.html language=enus -->
## TOPIC 00099: Perform a Simple Calibration

- bundle_id: `ni-vision-assistant`
- source_path: `perform-a-simple-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-a-simple-calibration.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette. Select Simple Calibration and click OK. Select the Pixel Type that applies to the camera. Click Next. Select two points. You can select points that were defined by previous inspection step

### Perform a Simple Calibration

1. Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette.
2. Select Simple Calibration and click OK .
3. Select the Pixel Type that applies to the camera.
4. Click Next .
5. Select two points. You can select points that were defined by previous inspection steps by double-clicking the point 
in the list or clicking the point in the image. You also can define new points by clicking unspecified 
pixels in the image.
  - If you selected square pixels in the previous wizard step, enter the distance between the two selected points in real-world units 
and specify the correct unit. Proceed to the next step.
  - If you selected nonsquare pixels in the previous step, follow these instructions:
    1. Enter the x projection of the two points in real-world units and specify the correct unit.
    2. Click Next .
    3. If you want to use different points to specify the pixel ratio along the y-axis, select two other points. Otherwise, go to the next substep.
    4. Enter the y projection of the two points in real-world units and specify the correct unit.
6. Click Next .
7. Select the origin of the calibration axis by entering the X - and Y -coordinates or by selecting an Existing Point from the list.
8. Select the User-Defined Angle of the calibration or select an Existing Angle . If you choose an Existing Angle from the list, you can add 90°, 180°, or 270° to the value.
9. Select an Axis Reference .
10. Click OK to apply the calibration.
11. Click OK to save the step in the script and close the
 Setup window.

Note

1. Click File»Save Image .
2. In the Save Image window, select a location to save the image.
3. Enter a name in the File Name textbox.
4. Enable the Save Extra Information checkbox.
5. Click Save .

#### Control Descriptions

- Open Image — Image on which you specify points to base
 the calibration. This image must be the same size as the image you want to
 calibrate. Vision Assistant does not run the script on this image.
- Pixel Type — Square or nonsquare pixels.
- List of points — Points defined in the image that you can
 use to calibrate the image.
- Point X and Y — Coordinates of the
 selected points.
- Length — Distance, in pixels, between the two selected
 points. This control appears only when you set Pixel Type 
 to Square .
- dX — Projection of the segment specified by the two
 points onto the x-axis. This control appears only when you set Pixel
 Type to Nonsquare .
- dY — Projection of the segment specified by the two
 points onto the y-axis. This control appears only when you set Pixel
 Type to Nonsquare .
- Unit — Real-world unit of the measurement.
- Axis Origin
  - User Defined — X- and y-coordinates of the pixel
 that you want to use as the calibration axis origin.
  - Existing Point — Point defined in a previous step
 that you want to use as the calibration axis origin.
- X Axis Angle
  - User Defined — Angle you want to use between the
 x-axis of the calibration axes and the horizontal axis of the
 image.
  - Existing Angle — Angle defined in a previous step
 that you want to use between the x-axis of the calibration axes and the
 horizontal axis of the image. You can select a value from the
 + list to add to the
 Angle value.
- Axis Reference — Direction of the y-axis.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-batch-processing.html language=enus -->
## TOPIC 00100: Perform Batch Processing

- bundle_id: `ni-vision-assistant`
- source_path: `perform-batch-processing.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-batch-processing.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Tools»Batch Processing. Select an image source. If you select Hard Disk, browse to the folder containing the images you want to process. If you select Acquisition, complete the following steps: Specify the acquisition module you want to use. You must have previously defined the parameters for

### Perform Batch Processing

1. Select Tools»Batch Processing .
2. Select an image source.
  - If you select Hard Disk , browse to the folder containing the images you want to process.
  - If you select Acquisition , complete the following steps:
    1. Specify the acquisition module you want to use. Note You must have
 previously defined the parameters for the acquisition module you
 select. Vision Assistant uses the parameter settings you defined
 the last time you used a particular acquisition module. For
 example, if you select Image Capture RT,
 you must have previously used the Acquire Image (RT) function in
 the Acquire Images tab of the Processing
 Functions. If you select an acquisition module you have not used
 previously, Vision Assistant prompts you to exit batch
 processing setup and acquire an image using the module you
 selected in Acquisition
 Modules.
    2. In Iterations , specify the number of times you want to acquire an image during batch processing.
    3. In Period (s.) , specify the length of the delay, in seconds, between acquisitions.
3. Select a step in the Script Steps list.
  - If the step processes the image under inspection, select one of the Process Mode options: Open Process Interface, Display Result Image, or Save Result Image.
  - If the step analyzes the image under inspection, select one of the Analysis Mode options: Open Results Panel or Save Results.
4. If you selected Save Results or Save Result Image in step 3, click Setup and configure the save options . Otherwise, proceed to step 6.
5. Click OK to close the save setup dialog box.
6. Click Run to start the batch process.
7. Click Return to exit batch processing mode.

Tip

- The progress window displays the current process, the number of iterations
 completed, the starting time, and an estimation of the time remaining.
- To stop batch processing, click the Cancel button in
 the progress window. Vision Assistant stops the batch process when the
 current step is complete or is cancelled from the Parameter window.

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=perform-calibration-with-user-defined-points.html language=enus -->
## TOPIC 00101: Perform Calibration with User-Defined Points

- bundle_id: `ni-vision-assistant`
- source_path: `perform-calibration-with-user-defined-points.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/perform-calibration-with-user-defined-points.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette. Select Calibration Using User-Defined Points and click OK. Select the type of Distortion that applies to the image. Select a point. You can select a point that was defined by a previous in

### Perform Calibration with User-Defined Points

1. Click Image»Image Calibration or select Image Calibration in the Image tab of the Processing Functions palette.
2. Select Calibration Using User-Defined Points and click OK .
3. Select the type of Distortion that applies to the image.
4. Select a point. You can select a point that was defined by a previous inspection step by double-clicking the point in the list or clicking the point in the image. You also can define a new point by clicking an unspecified pixel in the image.
5. Enter the Real-World Coordinates of the point you selected.
6. Select at least three more points.
7. Click OK .
8. Click the Specify Calibration Axis tab.
9. Select the origin of the calibration axis by entering the X - and Y -coordinates or by selecting an Existing Point from the list.
10. Select the User-Defined Angle of the calibration or select an Existing Angle . If you choose an Existing Angle from the list, you can add 90°, 180°, or 270° to the value.
11. Select an Axis Reference .
12. Click OK to learn the calibration.
13. Browse to the directory you want to save the calibration information in, enter a File name , and click OK .
14. Click OK to save the step in the script and close the
 Parameter window.

#### Define Reference Points Tab

- Open Image — Image on which you specify points to base the calibration.
 This image must be the same size as the image you want to calibrate. Vision
 Assistant does not run the script on this image.
- Distortion — Type of image distortion.
- Select at least 4 points — Points defined in the image that you can use
 to calibrate the image.
- Reset — Option to deselect all points.
- Unit — Real-world unit of the measurement.
- Image Coordinates — Pixel coordinates of the selected point.
- Real-World Coordinates — Real-world coordinates of the selected
 point.

#### Specify Calibration Axis Tab

- Axis Origin
  - User Defined — X- and y-coordinates of the pixel that you want to use as
 the calibration axis origin.
  - Existing Point — Point defined in a previous step that you want to use as
 the calibration axis origin.
- X Axis Angle
  - User Defined — Angle you want to use between the x-axis of the
 calibration axes and the horizontal axis of the image.
  - Existing Angle — Angle defined in a previous step that you want to use
 between the x-axis of the calibration axes and the horizontal axis of
 the image. You can select a value from the + list
 to add to the Angle value.
- Axis Reference — Direction of the y-axis.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=performance-meter.html language=enus -->
## TOPIC 00102: Performance Meter

- bundle_id: `ni-vision-assistant`
- source_path: `performance-meter.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/performance-meter.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Performance Meter to estimate how long (in milliseconds and frames/second) the script takes to complete in the Vision Development Module on a given image. The speed of some functions in the script varies depending on the image you process. Open the script you want to test. Select Too

### Performance Meter

You can use the Performance Meter to estimate how long (in milliseconds and frames/second) the
 script takes to complete in the Vision Development Module on a given image.

Note

1. Open the script you want to test.
2. Select Tools»Performance Meter . Vision Assistant evaluates the performance of the functions in the script and displays an estimate of the total time the Vision Development Module would take to complete the script.
3. Click Details to view an estimate of the time the Vision Development Module would take to complete each function in the script.
4. Click OK to close the Performance Meter.

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=print-images.html language=enus -->
## TOPIC 00103: Print Images

- bundle_id: `ni-vision-assistant`
- source_path: `print-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/print-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the image that you want to print. Click File»Print Image. Type the title of the image and comments, if necessary. You can leave these options blank if you do not need them. Enable the Print Results Overlaid on the Image option to print overlay information such as templates you use for pattern

### Print Images

1. Select the image that you want to print.
2. Click File»Print Image .
3. Type the title of the image and comments, if necessary. You can leave these options blank if you do not need them.
4. Enable the Print Results Overlaid on the Image option to print overlay information such as templates you use for pattern matching and lines drawn with the Edge Detector function.
5. Click Set Printer to select a printer.
6. Click OK .

Parent topic:

Managing Images

Related concepts:

- Add Processed Images to the Image Browser
- Browse Images in the Image Browser
- Open Images in Vision Assistant
- Save Images

<!--NI_TOPIC bundle=ni-vision-assistant path=processing-an-image.html language=enus -->
## TOPIC 00104: Processing an Image

- bundle_id: `ni-vision-assistant`
- source_path: `processing-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/processing-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Image Preview Window. Main Window. Navigation Buttons. Processing Functions Palette. Script Winfow Load the image into the Processing window. Select the appropriate function from the Image, Color, Grayscale, Binary, Machine Vision, or Identification menu. You can run a particular step of a script by

### Processing an Image

[IMAGE alt='image' src='GUID-B29BB1D8-F627-4B63-8D98-8101F2DADE2A-a5.gif']

1. Image Preview Window.
2. Main Window.
3. Navigation Buttons.
4. Processing Functions Palette.
5. Script Winfow

1. Load the image into the Processing window.
2. Select the appropriate function from the Image , Color , Grayscale , Binary , Machine Vision , or Identification menu.

Tip

Script

Parent topic:

Managing Images

Related concepts:

- Add Processed Images to the Image Browser
- Browse Images in the Image Browser
- Open Images in Vision Assistant
- Print Images
- Save Images

<!--NI_TOPIC bundle=ni-vision-assistant path=processingimages.html language=enus -->
## TOPIC 00105: Analyzing and Processing Images

- bundle_id: `ni-vision-assistant`
- source_path: `processingimages.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/processingimages.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`

### Analyzing and Processing Images

- [Perform a Histogram](perform-a-histogram.html)
- [Perform a Line Profile](perform-a-line-profile.html)
- [Selecting a Region of Interest (ROI)](selecting-a-region-of-interest-roi.html)
- [Calculate ROI Measurements](calculate-roi-measurements.html)
- [View an Image in 3D](view-an-image-in-3d.html)
- [Modify Brightness, Contrast, and Gamma Values of an Image](modify-brightness-contrast-and-gamma-values-o.html)
- [Set a Coordinate System](set-a-coordinate-system.html)
- [Mask an Image](mask-an-image.html)
- [Compute the Symmetry of an Image](compute-the-symmetry-of-an-image.html)
- [Rotate an Image](rotate-an-image.html)
- [Resample an Image](resample-an-image.html)
- [Store an Image in an Image Buffer](store-an-image-in-an-image-buffer.html)
- [Retrieve an Image from an Image Buffer](retrieve-an-image-from-an-image-buffer.html)
- [Get an Image](get-an-image.html)
- [Calibrate Images](calibrate-images.html)
- [Correct Images](correct-images.html)
- [Correcting Flat Field Images](correcting-flat-field-images.html)
- [Overlay Figures, Text, or Bitmaps on an Image](overlay-figures-text-or-bitmaps-on-an-image.html)
- [Run a LabVIEW VI from Vision Assistant](run-a-labview-vi-from-vision-assistant.html)
- [Use the Color Operators Function](use-the-color-operators-function.html)
- [Extract Color Planes from an Image](extract-color-planes-from-an-image.html)
- [Classify Color Samples](classify-color-samples.html)
- [Segment Colors](segment-colors.html)
- [Threshold a Color Image](threshold-a-color-image.html)
- [Search for Colors](search-for-colors.html)
- [Use Color Pattern Matching](use-color-pattern-matching.html)
- [Match Colors in an Image to a Template](match-colors-in-an-image-to-a-template.html)
- [Use Object Tracking Setup](use-object-tracking-setup.html)
- [Apply a Lookup Table Transformation](apply-a-lookup-table-transformation.html)
- [Smooth an Image with Filtering](smooth-an-image-with-filtering.html)
- [Highlight Details in an Image](highlight-details-in-an-image.html)
- [Filter an Image with a Custom Convolution Filter](filter-an-image-with-a-custom-convolution-fil.html)
- [Expand (Dilate) Objects in Grayscale Images](expand-dilate-objects-in-grayscale-images.html)
- [Reduce (Erode) Objects in Grayscale Images](reduce-erode-objects-in-grayscale-images.html)
- [Fill Gaps and Holes (Close) in Grayscale Images](fill-gaps-and-holes-close-in-grayscale-images.html)
- [Remove Small Objects (Open) from Grayscale Images](remove-small-objects-open-from-grayscale-imag.html)
- [Smooth Object Boundaries in Grayscale Images](smooth-object-boundaries-in-grayscale-images.html)
- [Reconstruct a Grayscale Image](reconstruct-a-grayscale-image.html)
- [Apply an FFT Filter to an Image](apply-an-fft-filter-to-an-image.html)
- [Threshold a Grayscale Image](threshold-a-grayscale-image.html)
- [Segment an Image Using a Watershed Transform](segment-an-image-using-a-watershed-transform.html)
- [Use the Operators Function](use-the-operators-function.html)
- [Convert Grayscale Images](convert-grayscale-images.html)
- [Quantify an ROI in an Image](quantify-an-roi-in-an-image.html)
- [Compute the Energy Center of an Image](compute-the-energy-center-of-an-image.html)
- [Detect Texture Defects](detect-texture-defects-2.html)
- [Reduce (Erode) Objects in Binary Images](reduce-erode-objects-in-binary-images.html)
- [Expand (Dilate) Objects in Binary Images](expand-dilate-objects-in-binary-images.html)
- [Remove Small Objects (Open) from Binary Images](remove-small-objects-open-from-binary-images.html)
- [Fill Gaps and Holes (Close) in Binary Images](fill-gaps-and-holes-close-in-binary-images.html)
- [Smooth Object Boundaries in Binary Images](smooth-object-boundaries-in-binary-images.html)
- [Extract the Contours of a Particle](extract-the-contours-of-a-particle.html)
- [Fill Holes and Smooth Right Angles](fill-holes-and-smooth-right-angles.html)
- [Remove Single Pixels and Right Angles](remove-single-pixels-and-right-angles.html)
- [Remove Small Objects](remove-small-objects.html)
- [Remove Large Objects](remove-large-objects.html)
- [Remove Objects Touching the Image Border](remove-objects-touching-the-image-border.html)
- [Fill Holes](fill-holes.html)
- [Compute the Convex Hull of Objects](compute-the-convex-hull-of-objects.html)
- [Reduce Objects to Skeletons](reduce-objects-to-skeletons.html)
- [Separate Objects](separate-objects.html)
- [Label Objects](label-objects.html)
- [Create a Distance Map](create-a-distance-map.html)
- [Segment an Image](segment-an-image.html)
- [Reconstruct a Binary Image](reconstruct-a-binary-image.html)
- [Filter Objects Based on Particle Measurements](filter-objects-based-on-particle-measurements.html)
- [Invert a Binary Image](invert-a-binary-image.html)
- [Perform a Particle Analysis](perform-a-particle-analysis.html)
- [Search a Binary Image for a Shape](search-a-binary-image-for-a-shape.html)
- [Detect Edges with Filters](detect-edges-with-filters.html)
- [Detect Edges with the Edge Tool](detect-edges-with-the-edge-tool.html)
- [Detect Edges with the Simple Edge Tool](detect-edges-with-the-simple-edge-tool.html)
- [Detect Edges with the Advanced Edge Tool](detect-edges-with-the-advanced-edge-tool.html)
- [Detect Edges in Grayscale Images](detect-edges-in-grayscale-images.html)
- [Detect Straight Edges](detect-straight-edges.html)
- [Detect Circular Edges](detect-circular-edges.html)
- [Detect Circular Edges in Grayscale Images](detect-circular-edges-in-grayscale-images.html)
- [Detect Circles](detect-circles.html)
- [Detecting Features](detecting-features.html)
- [Measure Distances Between Edges Using the Max Clamp Tool](measure-distances-between-edges-using-the-max.html)
- [Measure Distances Between Edges Using the Clamp (Rake-Based) Tool](measure-distances-between-edges-using-the-cla.html)
- [Search for Templates Using Pattern Matching](search-for-templates-using-pattern-matching.html)
- [Use Object Tracking Setup](use-object-tracking-setup_2.html)
- [Contour Analysis](contour-analysis-3.html)
- [Search for Shapes Using Shape Detection](search-for-shapes-using-shape-detection.html)
- [Search for Defects Using Map Defects](search-for-defects-using-map-defects.html)
- [Defining a Weight Map](defining-a-weight-map.html)
- [Search for Defects Using Golden Template Comparison](search-for-defects-using-golden-template-comp.html)
- [Use the Caliper Tool](use-the-caliper-tool.html)
- [Find the Distance Between Two Points](find-the-distance-between-two-points.html)
- [Find the Center of Two Points](find-the-center-of-two-points.html)
- [Find the Perpendicular Projection of a Point on a Line](find-the-perpendicular-projection-of-a-point.html)
- [Find the Intersection of Two Lines](find-the-intersection-of-two-lines.html)
- [Find the Angle Made by Two Points](find-the-angle-made-by-two-points.html)
- [Find the Angle Made by Three or Four Points](find-the-angle-made-by-three-or-four-points.html)
- [Find the Center of Mass Using Three or More Points](find-the-center-of-mass-using-three-or-more-p.html)
- [Find the Area Enclosed by Three or More Points](find-the-area-enclosed-by-three-or-more-point.html)
- [Find the Circular Fit Using Three or More Points](find-the-circular-fit-using-three-or-more-poi.html)
- [Read and Verify Text in Images](read-and-verify-text-in-images.html)
- [Classify Particle Samples](classify-particle-samples.html)
- [Read Barcodes in Images](read-barcodes-in-images.html)
- [Read 2D Barcodes in Images](read-2d-barcodes-in-images.html)
- [Read QR Codes in Images](read-qr-codes-in-images.html)
- [Using the Vision Assistant Express VI](using-the-vision-assistant-express-vi.html)
- [Vision Assistant Express VI Image Caching](vision-assistant-express-vi-image-caching.html)
- [Use Coordinate Systems with Vision Assistant Express VIs](use-coordinate-systems-with-vision-assistant.html)
- [Perform a Grid Calibration](perform-a-grid-calibration.html)
- [Perform a Simple Calibration](perform-a-simple-calibration.html)
- [Perform Calibration with User-Defined Points](perform-calibration-with-user-defined-points.html)
- [Apply Calibration Information from One Image to Another](apply-calibration-information-from-one-image.html)
- [Search for Templates Using Geometric Matching](search-for-templates-using-geometric-matching.html)
- [Apply Morphological Operations](apply-morphological-operations.html)
- [Apply Grayscale Morphological Operations](apply-grayscale-morphological-operations.html)

<!--NI_TOPIC bundle=ni-vision-assistant path=quantify-an-roi-in-an-image.html language=enus -->
## TOPIC 00106: Quantify an ROI in an Image

- bundle_id: `ni-vision-assistant`
- source_path: `quantify-an-roi-in-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/quantify-an-roi-in-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the ROI tools from the toolbar. Select a region of interest from the image. Vision Assistant lists the intensity measurements for that ROI in the Results table. Click OK to add this step to the script. You can select mult

### Quantify an ROI in an Image

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the ROI tools from the toolbar.
3. Select a region of interest from the image. Vision Assistant lists the intensity measurements for that ROI in the Results table.
4. Click OK to add this step to the script.

Tip

- You can select multiple regions of interest on the image. Vision Assistant
 numerically labels all of the ROIs selected and the corresponding
 measurements.
- To save the data, click the Send Data to Excel button
 or the Save Results button.
- You can remove the selected data with the Delete
 Selection button or delete all results with the
 Delete All Results button.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Selecting a Region of Interest (ROI)

<!--NI_TOPIC bundle=ni-vision-assistant path=read-2d-barcodes-in-images.html language=enus -->
## TOPIC 00107: Read 2D Barcodes in Images

- bundle_id: `ni-vision-assistant`
- source_path: `read-2d-barcodes-in-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/read-2d-barcodes-in-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the 2D Barcode Reader step to decode a 2D barcode. Main Tab In the Step Name textbox, enter a descriptive name for the step. In the Barcode Type box, select the type of 2D Barcode you want to read. Verify that the Reposition Region of Interest option is enabled if you want to link the region of

### Read 2D Barcodes in Images

Use the 2D Barcode Reader step to decode a 2D barcode.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. In the Barcode Type box, select the type of 2D Barcode
 you want to read.
3. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
4. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Settings Tab

Set the controls to specify
 the shape of the 2D barcode and to improve the performance of the
 step.

#### Grading Tab

Select the checkbox for the
 grading standard you want to use for your 2D barcodes. If you do not need grading
 information for your application, leave all checkboxes unselected to decrease the
 amount of time the step takes to complete.

The decoded characters read during
 the step are shown in the Code Read box.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=read-and-verify-text-in-images.html language=enus -->
## TOPIC 00108: Read and Verify Text in Images

- bundle_id: `ni-vision-assistant`
- source_path: `read-and-verify-text-in-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/read-and-verify-text-in-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest (ROI) specified in this step to a previously defined coordinate system. This option is disabled if you have not previou

### Read and Verify Text in Images

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest (ROI) specified in this step
 to a previously defined coordinate system. Note This option is disabled if
 you have not previously defined a coordinate system.
3. Link the ROI to a coordinate system if the position of the object under
 inspection changes from image to image, and you need to adjust the position of
 the ROI to match the new location of the object.

#### Train Tab

Follow these instructions to
 compare objects in an image to a trained set of characters and determine if the
 characters match a given string:

1. Browse to the character set file you want to open via Character Set
 Path , select the file, and click OK .
 If necessary, click New Character Set File to
 train additional characters in the OCR Training Interface.
2. Draw an ROI around the characters you want to read. Vision Assistant segments
 objects in the ROI by drawing character bounding rectangles around the
 objects according to the current settings in the
 Threshold, Size, and
 Read Options tabs.

#### Threshold Tab

Note

Threshold

1. Select a threshold type from the Mode control.
  - If you select Manual , use
 Min and Max or the
 slider at the bottom of the histogram to determine the threshold
 value.
  - If you select Auto: Uniform , Auto:
 Linear , Auto: Non Linear , or
 Local: BG Correction in
 Mode , select Dark on
 Light in Characters if the image
 contains dark characters on a light background. Select Light
 on Dark in Characters if the
 image contains light characters on a dark background.
  - If you select Auto: Linear or Auto:
 Non Linear , set # of Blocks to at
 least the number of characters in the ROI.
  - If you select Local: BG Correction , set the
 Width and Height of
 the Character Size within the ROI. Press to make the Character
 Size settings the same as the ROI
 Size settings.
  - If you select Color , set the Color
 Model to RGB ,
 HSL , HSV , or
 HSI . Use the sliders to set the
 Min and Max threshold
 value for each color component. For color models with a hue component,
 select Include Interval or Exclude
 Interval .
2. Enable the Ignore Objects Touching Region Borders control
 to ignore objects that touch the border of the ROI.
3. In Remove Small Objects (# of Erosions) , select the
 number of erosions to remove small objects from the ROI. The OCR Training
 Interface displays segmented objects in blue.

Tip

Preview Color

#### Size Tab

Use the
 Size tab to configure the algorithm, character size, and
 spacing values required for character recognition. OCR does not recognize any
 characters in the ROI that do not meet the criteria you set here. Refer to OCR/OCV
 Control Descriptions for information about each control.

#### Read Options Tab

1. Set Read Strategy to Aggressive or
 Conservative to determine whether the step uses
 strict criteria (Conservative) or fewer criteria (Aggressive) to match
 characters.
2. Set the Read Resolution to Low ,
 Medium , or High to select the
 level of character detail the step uses to determine if an object matches a
 trained character.
3. Select an Acceptance Level value to specify how closely
 an object must match a trained character to be recognized.
4. Enter the Substitution Character you want to appear in
 the string to indicate objects that are not trained and recognized.
5. Select Aspect Ratio Dependant to configure OCR to read
 larger characters. Enter an Aspect Ratio value to
 indicate the allowable percentage of size difference between the training and
 reading characters.
6. Click Use Text Pattern , then Specify Text
 Pattern if you know that the text to read always has the same
 pattern. For example, you can specify that the first character should be a
 letter and the second character should be a digit. Specifying a pattern
 increases the speed and accuracy of recognition.
7. Select Auto Detect Multiline and Rotation if the text
 spans multiple lines and/or has minor rotations. Set the # of Lines
 Expected to Auto Detect or
 Enter Numeric Value .
8. Click OK to add this step to the script and close the
 Parameter window.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=read-barcodes-in-images.html language=enus -->
## TOPIC 00109: Read Barcodes in Images

- bundle_id: `ni-vision-assistant`
- source_path: `read-barcodes-in-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/read-barcodes-in-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Barcode Reader function to decode a 1D barcode. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate syste

### Read Barcodes in Images

Use the Barcode Reader function to decode a 1D barcode.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. Select Locate Barcode for the step to automatically
 detect the barcode in the image. Specify detection parameters with the
 Minimum Bar Width , Minimum Edge
 Strength , and Minimum Bars controls.

#### Read 1D Barcode Tab

By default, the
 Auto Setup, Add Special Characters to Code
 Read, and Add Checksum to Code Read
 checkboxes are enabled. This configuration enables automatic barcode
 detection.

If automatic barcode detection does not produce expected results,
 you can manually configure the step:

1. Deselect Auto Setup .
2. Click to add a barcode type.
3. Select a barcode type in the Types of Barcode to Search 
 box. Click a barcode type to edit it.
4. Click to remove a barcode type.
5. Click to move a barcode type up in the
 list, or to move a barcode type down in
 the list. To optimize barcode classification, order the list of barcode types
 from the strictest standards to the most lenient, as in the following
 list:
  1. EAN 13
  2. EAN 8
  3. UPCA
  4. Code 128
  5. MSI
  6. Code 39
  7. Code 93
  8. Codabar
  9. Interleaved 2 of 5
  10. RSS Limited
  11. Pharmacode
6. Specify the Number of Barcodes to Read .
7. If the barcode types include Codabar, Code 39, or Interleaved 2 of 5, you can
 enable the Validate checkbox to use the encoded error
 correction information to validate the results. If the validation fails, the
 step also fails.
8. If the barcode types include Codabar, Code 128, EAN 8, EAN 13, or UPCA, you can
 enable the Add Special Character to Code Read checkbox to
 add the special characters of the code to the encoded data. You also can add the
 checksum to the encoded data by checking the Add Checksum to Code
 Read checkbox.

#### Results Tab

1. Specify a Minimum Score for a barcode to appear in the
 Results tree. The default score is 500.
2. Enable the Grade Barcodes checkbox for the step to grade
 each barcode. Specify a Scan Width , in pixels, for the
 width of the scanning line. The default Scan Width is
 1 . The results appear under Grading 
 in the Results tree.
3. Use the Results tree to view the following data for each
 barcode:
  - Complete Data — The complete data read from the barcode, including
 special character 1, 2, and checksum.
  - Data — Data read from the barcode, not including special character 1, 2,
 or checksum.
  - Special Character 1 — The first character preceding the barcode, if
 applicable.
  - Special Character 2 — The second character preceding the barcode, if
 applicable.
  - Checksum — The character following the barcode, if applicable.
  - Barcode Type — Indicates the type of barcode read.
  - Bounding Box — Expand to view the X and Y coordinates of each corner of
 the barcode bounding box.
  - Grading — Appears when you enable the Grade
 Barcodes checkbox. Expand to view the barcode grading
 results.
4. Click OK to add this step to the script and close the
 Parameter window.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=read-qr-codes-in-images.html language=enus -->
## TOPIC 00110: Read QR Codes in Images

- bundle_id: `ni-vision-assistant`
- source_path: `read-qr-codes-in-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/read-qr-codes-in-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the QR Code Reader step to decode a QR code. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link

### Read QR Codes in Images

Use the QR Code Reader step to decode a QR code.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Basic Tab

Set the controls on the
 Basic tab to specify the shape of the QR code and to
 improve the performance of the step. Enable the Suggest
 Value? checkbox if you want the step to suggest values for the
 controls when you click the Suggest Values
 button.

#### Advanced Search Tab

Set the controls on
 the Advanced Search tab. Enable the Suggest
 Value? checkbox if you want the step to suggest values for the
 controls when you click the Suggest Values
 button.

#### Cell Sampling Tab

Set the controls on the
 Cell Sampling tab if the step cannot consistently read
 the matrix because of variations in lighting or matrix quality. Otherwise, use the
 default values for the controls on this tab.

The decoded characters read
 during the step are shown in the Code Read box.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=reconstruct-a-binary-image.html language=enus -->
## TOPIC 00111: Reconstruct a Binary Image

- bundle_id: `ni-vision-assistant`
- source_path: `reconstruct-a-binary-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/reconstruct-a-binary-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: This procedure assumes your image is already in a binary state. Use the Image Buffer step to store the image to reconstruct. Process the image to create a marker image. Remove extraneous information from the image using various binary morphology operations from the Advanced Morphology, Basic Morphol

### Reconstruct a Binary Image

Note

1. Use the Image Buffer step to store the image to reconstruct.
2. Process the image to create a marker image. Remove extraneous information from the image using various binary morphology operations from the Advanced Morphology, Basic Morphology, and Particle Filter steps. Create an image containing only the seed points for the particles you want to reconstruct.
3. Select Binary Morphological Reconstruction in the Binary tab of the Processing Functions palette.
4. In the Step Name textbox, enter a descriptive name for the step.
5. Select the image to reconstruct from the buffer list.
6. Select the element to reconstruct. You can reconstruct particles or the background of the image.
7. Select the type of connectivity to use.
8. Select the image to display in the main window. The default view is the reconstructed image.
9. Click OK to apply the reconstruction and add this step to the script.

Refer to the Vision Concepts Help for more information about morphological reconstruction.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Store an Image in an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=reconstruct-a-grayscale-image.html language=enus -->
## TOPIC 00112: Reconstruct a Grayscale Image

- bundle_id: `ni-vision-assistant`
- source_path: `reconstruct-a-grayscale-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/reconstruct-a-grayscale-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Image Buffer step to store the image to reconstruct. Create a marker image. One method of creating a marker image is subtracting a constant value from the source image: Select Operators in the Grayscale tab of the Processing Functions palette. Select Subtract from the list of operators. Sele

### Reconstruct a Grayscale Image

1. Use the Image Buffer step to store the image to reconstruct.
2. Create a marker image. One method of creating a marker image is subtracting a constant value from the source image:
  1. Select Operators in the Grayscale tab of the Processing Functions palette.
  2. Select Subtract from the list of operators.
  3. Select a constant value to subtract from the source image.
  4. Click OK to perform the operation.
3. Select Gray Morphological Reconstruction in the Grayscale tab of the Processing Functions palette.
4. In the Step Name textbox, enter a descriptive name for the step.
5. Select the image to reconstruct from the buffer list.
6. Select the size of the structuring element. You can modify the structuring element by clicking its cells or using the Size X and Size Y controls.
7. Select whether to reconstruct Bright Regions or Dark Regions .
8. Select the image to display in the main window. The default view is the reconstructed image.
9. Click OK to apply the reconstruction and add this step to the script.

Refer to the Vision Concepts Help for more information about morphological reconstruction.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Store an Image in an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=reduce-erode-objects-in-binary-images.html language=enus -->
## TOPIC 00113: Reduce (Erode) Objects in Binary Images

- bundle_id: `ni-vision-assistant`
- source_path: `reduce-erode-objects-in-binary-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/reduce-erode-objects-in-binary-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Erode objects from the Basic Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Enter the numbe

### Reduce (Erode) Objects in Binary Images

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Erode objects from the Basic Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Enter the number of times that you want the erosion applied to the image in Iterations .
6. Click OK to apply the erosion and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Grayscale Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=reduce-erode-objects-in-grayscale-images.html language=enus -->
## TOPIC 00114: Reduce (Erode) Objects in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `reduce-erode-objects-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/reduce-erode-objects-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette. Select Erode from the Gray Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Enter the number of

### Reduce (Erode) Objects in Grayscale Images

1. Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette.
2. Select Erode from the Gray Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Enter the number of times that you want the erosion applied to the image in Iterations .
6. Click OK to apply the erosion and add this step to the script.

Tip

- The structuring element is a 2D array used as a binary mask. You can modify
 the structuring element by clicking its cells. If a cell is black, it has a
 value of 1. If a cell is white (empty), it has a value of 0.
- Experiment with different coefficients and the Kernel
 Size to get the results you want.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Reduce (Erode) Objects in Binary Images
- Remove Small Objects (Open) from Grayscale Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=reduce-objects-to-skeletons.html language=enus -->
## TOPIC 00115: Reduce Objects to Skeletons

- bundle_id: `ni-vision-assistant`
- source_path: `reduce-objects-to-skeletons.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/reduce-objects-to-skeletons.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Skeleton. Select the type of skeleton you want to see. Skeleton L — Uses an L-shaped structuring element. Skeleton M — Extracts the skeleton with more dendrites. Skiz — Uses an L-shape

### Reduce Objects to Skeletons

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Skeleton .
3. Select the type of skeleton you want to see.
  - Skeleton L — Uses an L-shaped structuring element.
  - Skeleton M — Extracts the skeleton with more dendrites.
  - Skiz — Uses an L-shaped structuring element that affects background
 regions, extracting the watershed line in an image.
4. Click OK to add this step to the script.

Note

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-a-step-from-a-script.html language=enus -->
## TOPIC 00116: Remove a Step from a Script

- bundle_id: `ni-vision-assistant`
- source_path: `remove-a-step-from-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-a-step-from-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the step that you want to remove from the script and click Edit»Delete or click the step and select Delete . Removing steps from a script can dramatically alter the final result of the script. As you delete steps, especially steps that change image type (such as conversion and color threshold

### Remove a Step from a Script

Edit»Delete

Delete

[IMAGE alt='image' src='GUID-D83690D7-BFA4-4F5D-AB2C-A7B6A950DEE3-a5.gif']

Note

conversion

color
 threshold

Tip

Step Backward

[IMAGE alt='image' src='GUID-B44E1624-5FA8-4FC7-B479-4003B26ED3DC-a5.gif']

Step Forward

[IMAGE alt='image' src='GUID-2107AE59-8026-4DFD-A86D-ED39F89D23D4-a5.gif']

step through the script

Parent topic:

Creating Scripts

Related concepts:

- Add a Step to a Script
- Run a Script
- Edit a Step in a Script
- Save a Script

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-large-objects.html language=enus -->
## TOPIC 00117: Remove Large Objects

- bundle_id: `ni-vision-assistant`
- source_path: `remove-large-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-large-objects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Remove large objects. Specify the number of 3 x 3 erosions to apply in Iterations. The particles that remain after the erosion operations are removed from the image and the rest of the

### Remove Large Objects

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Remove large objects .
3. Specify the number of 3 x 3 erosions to apply in Iterations . The particles that remain after the erosion operations are removed from the image and the rest of the particles are restored.
4. Click OK to remove large objects and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-objects-touching-the-image-border.html language=enus -->
## TOPIC 00118: Remove Objects Touching the Image Border

- bundle_id: `ni-vision-assistant`
- source_path: `remove-objects-touching-the-image-border.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-objects-touching-the-image-border.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Remove border objects. Click OK to remove all objects touching the border of the object and add this step to the script.

### Remove Objects Touching the Image Border

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Remove border objects .
3. Click OK to remove all objects touching the border of the object and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Small Objects
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-single-pixels-and-right-angles.html language=enus -->
## TOPIC 00119: Remove Single Pixels and Right Angles

- bundle_id: `ni-vision-assistant`
- source_path: `remove-single-pixels-and-right-angles.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-single-pixels-and-right-angles.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Thin to alter the shape of objects by eliminating parts to the object that match the pattern specified in the structuring element. Set the Size of the Structuring Element. Click the

### Remove Single Pixels and Right Angles

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Thin to alter the shape of objects by eliminating parts to the object that match the pattern specified in the structuring element.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the thinning and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-small-objects-open-from-binary-images.html language=enus -->
## TOPIC 00120: Remove Small Objects (Open) from Binary Images

- bundle_id: `ni-vision-assistant`
- source_path: `remove-small-objects-open-from-binary-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-small-objects-open-from-binary-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select Open objects from the Basic Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Click OK to appl

### Remove Small Objects (Open) from Binary Images

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select Open objects from the Basic Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the opening and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Grayscale Images
- Smooth Object Boundaries in Binary Images

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-small-objects-open-from-grayscale-imag.html language=enus -->
## TOPIC 00121: Remove Small Objects (Open) from Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `remove-small-objects-open-from-grayscale-imag.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-small-objects-open-from-grayscale-imag.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette. Select Open from the Gray Morphology list. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Click OK to apply the

### Remove Small Objects (Open) from Grayscale Images

1. Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette.
2. Select Open from the Gray Morphology list.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the opening and add this step to the script.

Tip

- The structuring element is a 2D array used as a binary mask to define the
 neighborhood of a pixel. You can modify the structuring element by clicking
 its cells. If a cell is black, it has a value of 1. If a cell is white
 (empty), it has a value of 0.

- Experiment with different coefficients and the Kernel
 Size to get the results you want.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Fill Gaps and Holes (Close) in Grayscale Images
- Reduce (Erode) Objects in Grayscale Images
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=remove-small-objects.html language=enus -->
## TOPIC 00122: Remove Small Objects

- bundle_id: `ni-vision-assistant`
- source_path: `remove-small-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/remove-small-objects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Remove small objects. Specify the number of 3 x 3 erosions that need to be applied to completely remove a small object in Iterations. Click OK to remove small objects and add this step

### Remove Small Objects

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Remove small objects .
3. Specify the number of 3 x 3 erosions that need to be applied to completely remove a small object in Iterations .
4. Click OK to remove small objects and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Segment an Image
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=resample-an-image.html language=enus -->
## TOPIC 00123: Resample an Image

- bundle_id: `ni-vision-assistant`
- source_path: `resample-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/resample-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Image»Geometry or select Geometry in the Image tab of the Processing Functions palette. Select Resampling. Select Keep Image Ratio to maintain the original image ratio. Deselect this option to change the image aspect ratio. Set the Interpolation Type. Set X Resolution and Y Resolution. Click O

### Resample an Image

1. Click Image»Geometry or select Geometry in the Image tab of the Processing Functions palette.
2. Select Resampling .
3. Select Keep Image Ratio to maintain the original image ratio. Deselect this option to change the image aspect ratio.
4. Set the Interpolation Type .
5. Set X Resolution and Y Resolution .
6. Click OK to add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Symmetry of an Image
- Rotate an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=retrieve-an-image-from-an-image-buffer.html language=enus -->
## TOPIC 00124: Retrieve an Image from an Image Buffer

- bundle_id: `ni-vision-assistant`
- source_path: `retrieve-an-image-from-an-image-buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/retrieve-an-image-from-an-image-buffer.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select Retrieve. Select the image buffer that contains the image you want to restore. Click OK to restore the image and add this step to the script. You must already have an image stored in an image buffer before you can restore it.

### Retrieve an Image from an Image Buffer

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select Retrieve .
3. Select the image buffer that contains the image you want to restore.
4. Click OK to restore the image and add this step to the script.

Note

Parent topic:

Analyzing and Processing Images

Related concepts:

- Store an Image in an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=rotate-an-image.html language=enus -->
## TOPIC 00125: Rotate an Image

- bundle_id: `ni-vision-assistant`
- source_path: `rotate-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/rotate-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Image»Geometry or select Geometry in the Image tab of the Processing Functions palette. Select Rotation. Turn the knob to select the angle of rotation or manually enter an angle. Click OK to add this step to the script.

### Rotate an Image

1. Click Image»Geometry or select Geometry in the Image tab of the Processing Functions palette.
2. Select Rotation .
3. Turn the knob to select the angle of rotation or manually enter an angle.
4. Click OK to add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Symmetry of an Image
- Resample an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=run-a-labview-vi-from-vision-assistant.html language=enus -->
## TOPIC 00126: Run a LabVIEW VI from Vision Assistant

- bundle_id: `ni-vision-assistant`
- source_path: `run-a-labview-vi-from-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/run-a-labview-vi-from-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Click Browse to select the path to the VI you want to run. The Run LabVIEW VI step works only with VIs saved using LabVIEW 8.6. To share or redistribute a VI, you must first save the VI for distribution. VI Controls Tab Click

### Run a LabVIEW VI from Vision Assistant

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Click Browse 
 to select the path to the VI you want to run.

Note

Run
 LabVIEW VI

save the VI for
 distribution

#### VI Controls Tab

1. Click Configure to launch the Select VI
 Value window.
2. Select a VI control name from the VI Controls list.
3. Specify a value for the control.
4. Repeat steps 2 and 3 as necessary.
5. Click OK to save the specified values and close the
 Select VI window.

Note

Select VI Value

Parent topic:

Analyzing and Processing Images

Related concepts:

- Saving a VI for Distribution

<!--NI_TOPIC bundle=ni-vision-assistant path=run-a-script.html language=enus -->
## TOPIC 00127: Run a Script

- bundle_id: `ni-vision-assistant`
- source_path: `run-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/run-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: To run a script, click Run Once in the Script window. Running a script applies all steps in the script to the current image. If the last step is an analysis function, the results are automatically displayed.

### Run a Script

To run a script, click Run Once
 [IMAGE alt='image' src='GUID-1C876A2E-0CC2-488C-9185-4399908F30B3-a5.gif'] in the
 Script window. Running a script applies all steps in the
 script to the current image. If the last step is an analysis function, the results are
 automatically displayed.

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=save-a-script.html language=enus -->
## TOPIC 00128: Save a Script

- bundle_id: `ni-vision-assistant`
- source_path: `save-a-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/save-a-script.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to save a script: Select File»Save Script or click the Save button in the Script window. Type the name of the script file. Click OK.

### Save a Script

Complete the following steps to save a script:

1. Select File»Save Script or click the Save 
 button
 in the Script window.
2. Type the name of the script file.
3. Click OK .

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=save-images.html language=enus -->
## TOPIC 00129: Save Images

- bundle_id: `ni-vision-assistant`
- source_path: `save-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/save-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can save one or several images you acquired and processed to separate image files, or you can create an AVI file containing a sequence of images. Click File»Save Image. Browse to the location to which you want to save the file and type the filename for the image. If you are saving a calibrated i

### Save Images

You can save one or several images you acquired and processed to separate image files, or you can create an AVI file containing a sequence of images.

1. Click File»Save Image .
2. Browse to the location to which you want to save the file and type the filename for the image.
3. If you are saving a calibrated image and want to save the calibration information with the image, select
 Save Image Calibration .
4. Select the File Format for the image.
  - If you have calibrated the image and enable the Save Image Calibration checkbox, only the PNG - Portable Network format is available in the File Format list.
  - If you select AVI - AVI Movie File from the File Format list, select a filter and a frame rate for the movie.
  - If you select JP2 - JPEG 2000 File Format from the File Format list, enable the Lossless checkbox if you want lossless compression, and specify a compression ratio.
5. Click Save .

Note

Expand Dynamic of Binary Images

Tip

- You can save a collection of images using the All
 Images or From ,
 To , Step options.
  - All Images saves each image in the Image
 Browser with the specified filename and a number describing its
 position in the Image Browser.
  - The From , To ,
 Step option saves images starting with
 the From parameter and ending with the
 To parameter. Step 
 specifies if you want to repetitively skip images in the Image
 Browser. For example, if you set From =2,
 To =10, and Step =2,
 Vision Assistant saves the second, fourth, sixth, eighth, and tenth
 images from the Image Browser.

Parent topic:

Managing Images

Related concepts:

- Add Processed Images to the Image Browser
- Browse Images in the Image Browser
- Open Images in Vision Assistant
- Print Images

<!--NI_TOPIC bundle=ni-vision-assistant path=saving-a-vi-for-distribution.html language=enus -->
## TOPIC 00130: Saving a VI for Distribution

- bundle_id: `ni-vision-assistant`
- source_path: `saving-a-vi-for-distribution.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/saving-a-vi-for-distribution.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to save a LabVIEW VI for distribution: Launch LabVIEW. Open the VI. If the VI is already open, save the VI. Select File»New Project. Add the VI and any dependencies to the project. If you want to run the VI on a remote target, you must first add the target to the project

### Saving a VI for Distribution

Complete the following steps to save a LabVIEW VI for distribution:

1. Launch LabVIEW.
2. Open the VI. If the VI is already open, save the VI.
3. Select File»New Project .
4. Add the VI and any dependencies to the project. If you want to run the VI on a remote target, you must first add the target to the project. Compete the following steps to add a remote target to the LabVIEW project:
  1. In the Project Explorer window, right-click the project root and select New»Targets and Devices .
  2. Select the target you want to add from the Targets and Devices section of the Add Targets and Devices dialog box.
  3. Click OK to add the target to the project.
5. Save the project by selecting File»Save Project .
6. Right-click Build Specifications underneath the VI you added to the project and select New»Source Distribution from the shortcut menu to display the Source Distribution Properties dialog box.
7. Enter a Build Specification Name and Destination Directory .
8. Select the Source Files category.
9. In the Project Files list, select the top-level VI and any dependencies, and add the files to the Always Included list.
10. Select the Destinations category.
11. In the Destination type control, select LLB .
12. Select the Source Files Settings category.
13. In the Project Files list, click Dependencies .
14. Enable the Apply prefix to all contained items checkbox and enter a prefix.
15. Select the Additional Exclusions category.
16. Enable the Disconnect type definitions , Remove unused polymorphic VI instances , and Remove unused members of project libraries checkboxes. Do not enable the Modify project library file after removing unused members checkbox.
17. Disable the Exclude files from vi.lib , Exclude files from instr.lib , and Exclude files from user.lib checkboxes.
18. Select the Preview category. Click Generate Preview to review the generated file hierarchy for the source distribution. To ensure the preview is accurate, save changes to VIs in memory before you create or edit a build specification.
19. Click Build . You can find the resulting source distribution in the
 directory specified in the Destination directory control in
 the Information category of the build specification. Note Before you can use
 the new LLB on a remote target, you must first download the LLB to the target
 using FTP.

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=scripting-concepts.html language=enus -->
## TOPIC 00131: Scripting Concepts

- bundle_id: `ni-vision-assistant`
- source_path: `scripting-concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/scripting-concepts.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Vision Assistant scripting feature records a series of image processing steps and the parameters you specified for each of those steps. You can run scripts on single images or image collections (batch processing). You also can modify and save scripts.A script is a list of image processing and an

### Scripting Concepts

The Vision Assistant scripting feature records a series of image processing steps and the
 parameters you specified for each of those steps. You can run scripts on single images
 or image collections (batch processing). You also can modify and save scripts.

A script is a list of image processing and analysis functions and the parameters for each of
 those functions. As you prototype the image processing application, Vision Assistant
 records each function and its parameters.

Complete the following steps to develop a script:

1. Process an image.When you finish processing the image and exit the Parameter window, Vision Assistant
adds the processing step to the current script.
2. Save the script.

You can use the script to implement the image processing application using the Vision machine
 vision and image processing library in LabVIEW, LabWindows™/CVI™, or in Visual Studio
 .NET.

If you have a supported version of LabVIEW and the Vision Development Module installed, you can
 use Vision Assistant to create the LabVIEW VI implementing the image processing steps
 you prototyped. Refer to the Vision Development Module Readme for a list of supported
 LabVIEW versions.

Parent topic:

Creating Scripts

<!--NI_TOPIC bundle=ni-vision-assistant path=search-a-binary-image-for-a-shape.html language=enus -->
## TOPIC 00132: Search a Binary Image for a Shape

- bundle_id: `ni-vision-assistant`
- source_path: `search-a-binary-image-for-a-shape.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-a-binary-image-for-a-shape.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Create a new template or select an existing template to use for shape matching: Click Create Template, select an ROI, and click OK. Enter a File name for the template and click OK. or Click Load from File, browse to the appropriate tem

### Search a Binary Image for a Shape

1. In the Step Name textbox, enter a descriptive name for the step.
2. Create a new template or select an existing template to use for shape matching:
  - Click Create Template , select an ROI, and click OK . Enter a File name for the template and click OK .
 or
  - Click Load from File , browse to the appropriate template file, and click OK .
3. Set Minimum Score , which is a threshold parameter between 0 and 1000. Shapes scoring above the specified value are considered matching shapes.
4. If you want all matching shapes returned regardless of size, select Scale Invariance .
5. Click OK to save this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-colors.html language=enus -->
## TOPIC 00133: Search for Colors

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-colors.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-colors.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Search for Colors

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is enabled if
 you want to link the region of interest specified in this step to a previously
 defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Template Tab

1. Create or select the template you want to use for comparison.
  - To create a new template, complete the following steps:
    1. Click Create Template .
    2. Select an ROI and click OK .
    3. Enter a File Name for the template and
 click OK .
  - To use an existing template, complete the following steps:
    1. Click Load from File .
    2. Browse to the appropriate template image and click
 OK .
2. Modify the Ignore Black and White and Sat.
 Threshold parameters as necessary.

#### Settings Tab

1. Select the Number of Matches to Find and a
 Minimum Score .
2. Select the appropriate Search Strategy and
 Color Sensitivity .
3. Click OK to save this step to the script and exit the
 Parameter window.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-defects-using-golden-template-comp.html language=enus -->
## TOPIC 00134: Search for Defects Using Golden Template Comparison

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-defects-using-golden-template-comp.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-defects-using-golden-template-comp.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Define the golden template to compare to the inspection image using one of the following methods: To create a new golden template, complete the following steps: Click New Template to launch the Vision Template editor. Complete

### Search for Defects Using Golden Template Comparison

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Define the golden template to compare to the inspection image using one of the
 following methods:
  - To create a new golden template, complete the following steps:
    1. Click New Template to launch the Vision
 Template editor.
    2. Complete the steps in the Vision Template Editor to create a
 golden template. Refer to the Vision Template Editor Help for
 specific instructions about how to define a golden
 template.
    3. Click Finish to validate the new
 template.
    4. In the Save Template As dialog box, browse to the location where
 you want to save the template file, enter a File
 Name , and click OK .
  - To use an existing image as the golden template, complete the following
 steps: 
 If the image you selected is not a valid golden template file,
 complete the following steps to create a golden template based on
 the image you selected:
    1. Click Load from File .
    2. Browse to the image you want to use as the golden template.
    3. Click Open .
    1. Click Yes to launch the Vision Template
 Editor.
    2. Adjust the Edge Threshold value until
 only the edges you want to exclude during the golden template
 comparison remain.
    3. Click OK .
    4. In the Save Template As dialog box, browse to the location where
 you want to save the template file, enter a File
 Name , and click OK .

Tip

Edit Template

#### Alignment Tab

1. If necessary, adjust the position of the region of interest to correspond with
 the area of the image you want to search for defects. For rough alignment of
 the region of interest within the inspection image, use the mouse to adjust
 the center of the position of the region of interest. For fine adjustments
 in the position of the region of interest, use the arrow keys or the
 Center X, Center Y, and
 Angle controls. The size of the region of
 interest cannot be adjusted because the size of the region of interest is
 based on the size of the specified golden template.
2. Verify that the Reposition Region of Interest checkbox is enabled if
 you want to link the region of interest specified in this step to a previously
 defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. Specify a Scale value to apply to the golden template if
 the area in the image you want to compare to the golden template is larger or
 smaller than the golden template image.
5. Select the type of Alignment Correction you want to use
 to when the golden template is applied to the image.

#### Settings Tab

1. Select the type of defects to detect from the Look For 
 list.
2. Use the Intensity , Ignore Edges ,
 and Edge Thickness controls to adjust for variations in
 lighting and minor differences along the edges of the image that you want to
 ignore.
3. Use the Threshold Defect Image , Bright
 Level , and Dark Level controls to set the
 threshold limits for defects in the image.
4. Click OK to save this step to the script.

Tip

Display

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-defects-using-map-defects.html language=enus -->
## TOPIC 00135: Search for Defects Using Map Defects

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-defects-using-map-defects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-defects-using-map-defects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest checkbox is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system

### Search for Defects Using Map Defects

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest checkbox is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Specifications Tab

1. Click New Template , select an ROI around the template you
 want to find in the image. Enter a File name for the
 template and click OK .
2. Click Next to define the regions to ignore.
3. Click Next to define the Match Offset and Pyramid Level
 to store in the template.
4. Click Finish to learn the template. or
5. Click Load from File , browse to the appropriate template
 file, and click OK . By default, the center of the
 template is used as the focal point of the template. You can change the location
 of the focal point to any position in the template.
6. Click Edit Template to change the location of the Match
 Offset.
7. Enable Rotated to indicate that the match can be a
 rotated version of the template. You can restrict the amount of rotation you
 want to allow by specifying an acceptable angle range.
8. Enable Scaled to search for matches that are larger or
 smaller than the template.
9. Enable Occluded to search for matches that are partially
 hidden by other objects in the image. Enter the occlusion range.
10. Select Use Preset Parameters check box to use the
 predefined advanced parameters corresponding to different use cases and
 priorities. Selecting Use Preset Parameters sets the
 value of the parameters in the Options tab to predefined
 values that should work best for your specific application. Select the
 Priority as
 Accurate , Fast , and
 Very Fast as necessary.
11. Select the Options tab to specify additional
 parameters.

Tip

Edit Template

Define Weight Map

Optionally, define a weight map to attenuate defects in some areas of the images,
 such as the borders of the part under inspection.

1. Click Define Weight Map to attenuate defects in some
 areas.
2. Enable Attenuate Edge if you want to attenuate defects
 along edges in the image.
3. Enter the Edge Threshold to fine tune the detection of
 edges.
4. Enter the Edge Thickness to specify the width of the area
 around the edges that you want to attenuate. You can also attenuate custom
 regions by selecting a tool and directly drawing in the image.
5. Click Clear All Additional Regions to erase all areas to
 attenuate.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Defining a Weight Map

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-shapes-using-shape-detection.html language=enus -->
## TOPIC 00136: Search for Shapes Using Shape Detection

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-shapes-using-shape-detection.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-shapes-using-shape-detection.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The shape detection step works only with 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system

### Search for Shapes Using Shape Detection

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Curve Settings Tab

Modify the
 Extraction Mode, Edge Threshold,
 Edge Filter Size, Minimum Length,
 Row Search Step Size, and Column Search Step
 Size to improve edge detection, if necessary.

#### Shape Tab

1. Select the type of shape you want to detect.
2. Set the Descriptor values to indicate the size of the shapes to return.

#### Settings Tab

1. Specify the minimum score a detected shape can have to be considered a valid
 match. This value can range from 0 to 1000, where a score of 1000 indicates a
 perfect match.
2. Enable Search for Matches that are Rotated, Scaled, or
 Occluded to indicate that a match may be a rotated, scaled, or
 occluded version of the shape you want to detect. Specify an acceptable range
 for each parameter to restrict the amount of rotation, scale, or occlusion
 allowed in a valid shape.
3. Click OK to save this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-templates-using-geometric-matching.html language=enus -->
## TOPIC 00137: Search for Templates Using Geometric Matching

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-templates-using-geometric-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-templates-using-geometric-matching.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The geometric matching function works only with 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate

### Search for Templates Using Geometric Matching

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Template Tab

Choose one of the following methods to specify the template
 for the step:

- Click New Template to launch the Vision Template Editor.
 Refer to the Vision Template Editor Help for instructions on how to create a
 geometric template. After creating a template, click
 Finish in the training interface to validate the
 template. Enter a File name , and click
 OK . or
- Click Load from File , browse to the appropriate template
 file, and click OK .

#### Curve Settings Tab

By default, the values
 of the parameters in this tab are initialized to the values you selected in the
 training interface. You can adjust these values to improve edge detection in the
 inspection image.

Modify the Extraction Mode,
 Edge Threshold, Edge Filter Size,
 Minimum Length, Row Search Step
 Size, and Column Search Step Size to improve
 edge detection, if necessary.

#### Settings Tab

1. Set the Number of Matches to Find , Minimum
 Score , and Subpixel Accuracy .
2. Enable Search for matches that are: Rotated, Scaled, or
 Occluded to indicate that a match may be a rotated, scaled, or
 occluded version of the template. Specify an acceptable range for each parameter
 to restrict the amount of rotation, scale, or occlusion allowed in a valid
 match.
3. Click OK to save this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=search-for-templates-using-pattern-matching.html language=enus -->
## TOPIC 00138: Search for Templates Using Pattern Matching

- bundle_id: `ni-vision-assistant`
- source_path: `search-for-templates-using-pattern-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/search-for-templates-using-pattern-matching.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Pattern Matching function works only with 8-bit images. Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate s

### Search for Templates Using Pattern Matching

Note

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Specifications Tab

Choose one of the
 following methods to specify the template for the step:

1. Click New Template , select an ROI around the template you
 want to find in the image. Enter a File name for the
 template and click OK .
2. Click Next to define the regions to ignore.
3. Click Next to define the Match Offset and Pyramid Level
 to store in the template.
4. Click Finish to learn the template. or
5. Click Load from File , browse to the appropriate template
 file, and click OK . By default, the center of the
 template is used as the focal point of the template. You can change the location
 of the focal point to any position in the template.
6. Click Edit Template to change the location of the Match
 Offset.
7. Modify Number of Matches to Find as necessary.
8. Enable Rotated to indicate that the match can be a
 rotated version of the template. You can restrict the amount of rotation you
 want to allow by specifying an acceptable angle range.
9. Enable Scaled to search for matches that are larger or
 smaller than the template.
10. Enable Occluded to search for matches that are partially
 hidden by other objects in the image. Enter the occlusion range.
11. Select Use Preset Parameters check box to use the
 predefined advanced parameters corresponding to different use cases and
 priorities. Selecting Use Preset Parameters sets the
 value of the Default parameters in the Options tab to
 predefined values that should work best for your specific application. Select
 the Priority as
 Accurate , Fast , and
 Very Fast as necessary.
12. Select the Options tab to specify additional
 parameters.

#### Options Tab

The following controls are
 available in the Options tab:

1. Specify the View to change the parameters that are
 displayed in the tree. If Use Preset Parameters is
 selected in the Specifications tab, the predefined
 parameter values corresponding to the use case and priority are grayed out.
2. Clear the Use Preset Parameters checkbox to enable all
 parameters and enter custom values.
3. Click the parameter that needs to be modified. Enter the new value in the
 control displayed in the Value column.
4. Click Reset to Default Preset Values to reinitialize the
 parameters to the predefined values corresponding to the use case and priority
 defined in the Specifications tab.
5. Click OK to insert the step into the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=segment-an-image-using-a-watershed-transform.html language=enus -->
## TOPIC 00139: Segment an Image Using a Watershed Transform

- bundle_id: `ni-vision-assistant`
- source_path: `segment-an-image-using-a-watershed-transform.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/segment-an-image-using-a-watershed-transform.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The watershed function works only with 8-bit and 16-bit images. The following steps illustrate one method of segmenting objects. Threshold — (Grayscale»Threshold) Threshold the image to isolate the objects you want to segment from the rest of the image. Remove Noise — (Binary»Advanced Morphology or

### Segment an Image Using a Watershed Transform

Note

The following steps illustrate one method of segmenting objects.

1. Threshold — ( Grayscale»Threshold ) Threshold the image to
 isolate the objects you want to segment from the rest of the
 image.
2. Remove Noise — ( Binary»Advanced Morphology or Binary»Particle
 Filter ) Remove extraneous information from the
 binary image using various morphology operations. For example, you
 can fill in holes with the Advanced Morphology option Fill
 holes or remove noise with the Particle
 Filter function.
3. Create Distance Map — ( Binary»Advanced Morphology ) Use the
 Danielsson option to transform the binary image
 into a grayscale image in which the center of each object represents
 a local maximum in the image. If you were to look at the
 topographical surface of the image after applying the distance map,
 each object would appear as a smooth, gradual peak.
4. Apply Watershed Transform — ( Grayscale»Watershed Segmentation ) Apply the
 watershed transform to segment the image into local zones. A zone is
 determined by the watershed line that separates the influence zone
 of each peak.

Refer to the Vision Concepts Help for more information about thresholding, morphology, distance
 transforms, or watershed transforms.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Threshold a Grayscale Image
- Fill Holes
- Filter Objects Based on Particle Measurements
- Create a Distance Map

<!--NI_TOPIC bundle=ni-vision-assistant path=segment-an-image.html language=enus -->
## TOPIC 00140: Segment an Image

- bundle_id: `ni-vision-assistant`
- source_path: `segment-an-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/segment-an-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette. Select Segment image. Click OK to add this step to the script. This function partitions an image into segments, each centered on an object, so that the segments do not overlap and leave empty

### Segment an Image

1. Click Binary»Adv. Morphology or click Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Segment image .
3. Click OK to add this step to the script.

Note

- This function partitions an image into segments, each centered on an object,
 so that the segments do not overlap and leave empty zones.
- This function is computer-intensive and can take several seconds.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Separate Objects

<!--NI_TOPIC bundle=ni-vision-assistant path=segment-colors.html language=enus -->
## TOPIC 00141: Segment Colors

- bundle_id: `ni-vision-assistant`
- source_path: `segment-colors.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/segment-colors.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow these instructions to segment colors in a given region of interest (ROI): Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously

### Segment Colors

Follow these instructions to segment colors in a given region of interest (ROI):

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is
 enabled if you want to link the region of interest specified in this step to a
 previously defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.
4. If you have not trained the software for the classes you want to segment, click
 New Classifier File to launch the Color
 Classification Training Interface. Follow the instructions on the training
 interface to learn the classes you want to segment. Note Refer to the Color Classification Training Interface Help for more
 information about how to train and classify colors in the Color
 Classification Training Interface.
5. If you have trained the software for the classes you want to segment, click the
 Browse 
 button to select the path to the classifier file. When
 you have selected the classifier file, the path to the file appears in the
 Classifier File Path control.

Note

Edit Classifier File

#### Settings Tab

Adjust the values in the
 Settings tab and refer to the Elapsed
 Time indicator to adjust the performance of the color segmentation
 step to meet the requirements of your application.

#### Pixel Mapping Tab

Reset Values

Note

Settings

Unassigned pixels

Note

Class
 Assignment of Pixel Values

Class Assignment of Pixel Values

Click OK to add this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=selecting-a-development-environment.html language=enus -->
## TOPIC 00142: Selecting a Development Environment

- bundle_id: `ni-vision-assistant`
- source_path: `selecting-a-development-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/selecting-a-development-environment.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Vision Assistant to create a LabVIEW VI, LabVIEW FPGA VI, C code, or .NET code. Select the type of code that you would like to generate on the Vision Assistant welcome screen. To change the selected code type, select File»Preferences and select the General tab.

### Selecting a Development Environment

You can use Vision Assistant to create a LabVIEW VI, LabVIEW FPGA VI, C code, or .NET code.
 Select the type of code that you would like to generate on the Vision Assistant welcome
 screen. To change the selected code type, select File»Preferences
 and select the General tab.

Parent topic:

Migrating to a Development Environment

<!--NI_TOPIC bundle=ni-vision-assistant path=selecting-a-region-of-interest-roi.html language=enus -->
## TOPIC 00143: Selecting a Region of Interest (ROI)

- bundle_id: `ni-vision-assistant`
- source_path: `selecting-a-region-of-interest-roi.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/selecting-a-region-of-interest-roi.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select an ROI tool from the toolbar. Using the mouse, click and drag on the image to select the ROI. The ROI tools are accessible only for particular functions. If you want to select an ROI on an image and save it, click Image»Image Mask or select Image Mask in the Image tab of the Processing Functi

### Selecting a Region of Interest (ROI)

1. Select an ROI tool from the toolbar.
2. Using the mouse, click and drag on the image to select the ROI.

Note

Tip

Image»Image Mask

Image Mask

Image

Parent topic:

Analyzing and Processing Images

Related information:

- Regions of Interest

<!--NI_TOPIC bundle=ni-vision-assistant path=separate-objects.html language=enus -->
## TOPIC 00144: Separate Objects

- bundle_id: `ni-vision-assistant`
- source_path: `separate-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/separate-objects.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Binary»Adv. Morphology or select Adv. Morphology in the Binary tab of the Processing Functions palette. Select Separate objects. Set the Size of the Structuring Element. Click the cells of the structuring element that you want to have a value of 0. Enter the number of erosions that you want t

### Separate Objects

1. Select Binary»Adv. Morphology or select Adv. Morphology in the Binary tab of the Processing Functions palette.
2. Select Separate objects .
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Enter the number of erosions that you want the function to apply to the image in Iterations .
6. Click OK to separate objects and add this step to the script.

Note

- The structuring element is a 2D array used as a binary mask. You can modify
 the structuring element by clicking its cells. If a cell is black, it has a
 value of 1. If a cell is white (empty), it has a value of 0.
- This function is computer-intensive and can take several seconds to
 process.

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Compute the Convex Hull of Objects
- Create a Distance Map
- Fill Holes
- Label Objects
- Reduce Objects to Skeletons
- Remove Large Objects
- Remove Objects Touching the Image Border
- Remove Small Objects
- Segment an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=set-a-coordinate-system.html language=enus -->
## TOPIC 00145: Set a Coordinate System

- bundle_id: `ni-vision-assistant`
- source_path: `set-a-coordinate-system.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/set-a-coordinate-system.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Coordinate System Name textbox, enter a descriptive name for the step. Select the mode that best represents the position of the object under inspection. Take into account the position of the camera, lighting, and the type of synchronization between the image acquisition and the motion of the

### Set a Coordinate System

1. In the Coordinate System Name textbox, enter a descriptive name for the step.
2. Select the mode that best represents the position of the object under inspection. Take into
 account the position of the camera, lighting, and the type of synchronization
 between the image acquisition and the motion of the object under inspection.
3. Select the feature whose location and angle measurement you want to use to specify the origin and angle of the coordinate system.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=smooth-an-image-with-filtering.html language=enus -->
## TOPIC 00146: Smooth an Image with Filtering

- bundle_id: `ni-vision-assistant`
- source_path: `smooth-an-image-with-filtering.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/smooth-an-image-with-filtering.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the smoothing functions from the Filters list. Set the Kernel Size and coefficients if you are using a Local Average or Gaussian filter. Set the filter size if you are using the Lowpass or Median filter. Click OK to filte

### Smooth an Image with Filtering

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the smoothing functions from the Filters list.
3. Set the Kernel Size and coefficients if you are using a Local Average or Gaussian filter. Set the filter size if you are using the Lowpass or Median filter.
4. Click OK to filter the image and add this step to the script.

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Detect Edges with Filters
- Filter an Image with a Custom Convolution Filter
- Highlight Details in an Image

<!--NI_TOPIC bundle=ni-vision-assistant path=smooth-object-boundaries-in-binary-images.html language=enus -->
## TOPIC 00147: Smooth Object Boundaries in Binary Images

- bundle_id: `ni-vision-assistant`
- source_path: `smooth-object-boundaries-in-binary-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/smooth-object-boundaries-in-binary-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette. Select a function from the Basic Morphology list. You can use one of three morphological functions to smooth the boundaries of objects: Proper Open — Smoothes boundaries of objects and fil

### Smooth Object Boundaries in Binary Images

1. Click Binary»Basic Morphology or select Basic Morphology in the Binary tab of the Processing Functions palette.
2. Select a function from the Basic Morphology list. You can use one of three morphological functions to smooth the boundaries of objects:
  - Proper Open — Smoothes boundaries of objects and fills small holes.
  - Proper Close — Smoothes boundaries of objects and removes small
 particles.
  - Auto Median — Smoothes boundaries of objects.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the smoothing function and add this step to the script.

Note

Tip

Kernel Size

Parent topic:

Analyzing and Processing Images

Related concepts:

- Expand (Dilate) Objects in Binary Images
- Extract the Contours of a Particle
- Fill Gaps and Holes (Close) in Binary Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Binary Images
- Remove Single Pixels and Right Angles
- Remove Small Objects (Open) from Binary Images
- Smooth Object Boundaries in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=smooth-object-boundaries-in-grayscale-images.html language=enus -->
## TOPIC 00148: Smooth Object Boundaries in Grayscale Images

- bundle_id: `ni-vision-assistant`
- source_path: `smooth-object-boundaries-in-grayscale-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/smooth-object-boundaries-in-grayscale-images.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette. Select one of the three following morphological functions from the Gray Morphology list: Proper Open — Smoothes boundaries of objects and fills small holes. Proper Close — Smoothes bou

### Smooth Object Boundaries in Grayscale Images

1. Click Grayscale»Gray Morphology or select Gray Morphology in the Grayscale tab of the Processing Functions palette.
2. Select one of the three following morphological functions from the Gray Morphology list:
  - Proper Open — Smoothes boundaries of objects and fills small holes.
  - Proper Close — Smoothes boundaries of objects and removes small
 particles.
  - Auto Median — Smoothes boundaries of objects.
3. Set the Size of the Structuring Element .
4. Click the cells of the structuring element that you want to have a value of 0.
5. Click OK to apply the morphology and add this step to the script.

Tip

- The structuring element is a 2D array used as
 a binary mask to define the neighborhood of a
 pixel. You can modify the structuring element by
 clicking its cells. If a cell is black, it has a
 value of 1. If a cell is white (empty), it has a
 value of 0.
- Experiment with different coefficients and the
 Kernel Size to get the
 results you want.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Fill Gaps and Holes (Close) in Grayscale Images
- Fill Holes and Smooth Right Angles
- Reduce (Erode) Objects in Grayscale Images
- Remove Small Objects (Open) from Grayscale Images
- Smooth an Image with Filtering
- Smooth Object Boundaries in Binary Images
- Expand (Dilate) Objects in Grayscale Images

<!--NI_TOPIC bundle=ni-vision-assistant path=snapping-an-image-single-image-acquisition.html language=enus -->
## TOPIC 00149: Snapping an Image (Single Image Acquisition)

- bundle_id: `ni-vision-assistant`
- source_path: `snapping-an-image-single-image-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/snapping-an-image-single-image-acquisition.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click File»Acquire Image. Vision Assistant displays the Acquisition Functions palette. Click the appropriate acquisition step. The Devices window displays all image acquisition devices and channels or ports available for the computer. Select the device and channel or port you want to use to acquire

### Snapping an Image (Single Image
 Acquisition)

1. Click File»Acquire Image . Vision Assistant displays the Acquisition Functions palette.
2. Click the appropriate acquisition step. The Devices window displays all
 image acquisition devices and channels or ports available for the computer.
3. Select the device and channel or port you want to use to acquire an image.
4. Select Acquire Single Image 
 to acquire a single image with the image acquisition
 device and display it. This operation is known as a snap.
5. Select Store Acquired Image in Browser 
 to send the image to the Image Browser.
6. Click Close to add the acquisition step and close the
 Setup window.
7. Process the image as you would any other image in Vision Assistant.

Parent topic:

Acquiring Images

Related concepts:

- How to Simulate an Image Acquisition
- Acquiring a Sequence of Images
- Acquire Images in Color
- Grabbing an Image (Continuous Image Acquisition)
- Image Acquisition in Vision Assistant

<!--NI_TOPIC bundle=ni-vision-assistant path=store-an-image-in-an-image-buffer.html language=enus -->
## TOPIC 00150: Store an Image in an Image Buffer

- bundle_id: `ni-vision-assistant`
- source_path: `store-an-image-in-an-image-buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/store-an-image-in-an-image-buffer.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select Store. Select an empty image buffer from the Image Buffer list. If you do not have an empty buffer, select a buffer that contains an image that you no longer need. Click OK to save the image to the selected image buffer and add

### Store an Image in an Image Buffer

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select Store .
3. Select an empty image buffer from the Image Buffer list. If you do not have an empty buffer, select a buffer that contains an image that you no longer need.
4. Click OK to save the image to the selected image buffer and add this step to the script.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Retrieve an Image from an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=technical-support-and-professional-services.html language=enus -->
## TOPIC 00151: Technical Support and Professional Services

- bundle_id: `ni-vision-assistant`
- source_path: `technical-support-and-professional-services.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/technical-support-and-professional-services.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI website is your complete resource for technical support. At ni.com/support, you have access to everything from troubleshooting and application development self-help resources to email and phone assistance from NI Technical Support Engineers. Visit ni.com/services for information about the ser

### Technical Support and Professional Services

The NI website is your complete resource for technical support. At ni.com/support, you have access to everything from troubleshooting and application development self-help resources to email and phone assistance from NI Technical Support Engineers.

Visit ni.com/services for information about the services NI offers.

Visit ni.com/register to register your NI product. Product registration facilitates technical support and ensures that you receive important information updates from NI.

NI corporate headquarters is located at 11500 North Mopac Expressway, Austin, Texas, 78759-3504, USA. For up-to-date contact information for your location, visit ni.com/contact.

<!--NI_TOPIC bundle=ni-vision-assistant path=threshold-a-color-image.html language=enus -->
## TOPIC 00152: Threshold a Color Image

- bundle_id: `ni-vision-assistant`
- source_path: `threshold-a-color-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/threshold-a-color-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main TabIn the Step Name textbox, enter a descriptive name for the step. Color Threshold Tab Select the color model (RGB, HSL, HSV, or HSI) you want to use to process the image. Adjust the blue and red lines on the Red (Hue), Green (Saturation), and Blue (Luminance/Value/Intensity) histograms until

### Threshold a Color Image

#### Main Tab

In the Step
 Name textbox, enter a descriptive name for the step.

#### Color Threshold Tab

1. Select the color model (RGB, HSL, HSV, or HSI) you want to use to process the
 image.
2. Adjust the blue and red lines on the Red (Hue) ,
 Green (Saturation) , and Blue
 (Luminance/Value/Intensity) histograms until all of the
 particles of interest are highlighted with the color specified in
 Preview Color .
3. Click OK to threshold the image and add this step to the
 script.

Tip

- If you have trouble finding a threshold range that selects all of the
 pixels in the range, draw an ROI around the portion of the image that
 you want to keep. The histogram displays the intensities of the ROI
 only. Use the minimum and maximum values for the threshold.
- You can display the histogram in either linear or logarithmic form.

Parent topic:

Analyzing and Processing Images

Related information:

- Color Thresholding

<!--NI_TOPIC bundle=ni-vision-assistant path=threshold-a-grayscale-image.html language=enus -->
## TOPIC 00153: Threshold a Grayscale Image

- bundle_id: `ni-vision-assistant`
- source_path: `threshold-a-grayscale-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/threshold-a-grayscale-image.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main TabIn the Step Name textbox, enter a descriptive name for the step. Threshold Tab Select whether you want the function to look for bright, dark, or gray objects. Select the type of threshold you want to perform.You cannot adjust the threshold levels of the local and automatic thresholds. If non

### Threshold a Grayscale Image

#### Main Tab

In the Step
 Name textbox, enter a descriptive name for the step.

#### Threshold Tab

1. Select whether you want the function to look for bright, dark, or gray
 objects.
2. Select the type of threshold you want to perform. Note You cannot adjust the
 threshold levels of the local and automatic thresholds. If none of the local
 or automatic thresholding options work for the image, select
 Manual Threshold and adjust the pointers on the
 histogram until all of the particles of interest are highlighted in
 red.
3. Click OK to threshold the image and add this step to the
 script.

Tip

Parent topic:

Analyzing and Processing Images

Related information:

- Color Thresholding

<!--NI_TOPIC bundle=ni-vision-assistant path=trademarks.html language=enus -->
## TOPIC 00154: Trademarks

- bundle_id: `ni-vision-assistant`
- source_path: `trademarks.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/trademarks.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the NI Trademarks and Logo Guidelines at ni.com/trademarks for more information on NI trademarks. ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries. LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group. TETRIX by Pitsco is a trademark o

### Trademarks

Refer to the NI Trademarks and Logo Guidelines at ni.com/trademarks for more information on NI trademarks.

ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries.

LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group.

TETRIX by Pitsco is a trademark of Pitsco, Inc.

FIELDBUS FOUNDATION™ and FOUNDATION™ are trademarks of the Fieldbus Foundation.

EtherCAT® is a registered trademark of and licensed by Beckhoff Automation GmbH.

CANopen® is a registered Community Trademark of CAN in Automation e.V.

DeviceNet™ and EtherNet/IP™ are trademarks of ODVA.

Go!, SensorDAQ, and Vernier are registered trademarks of Vernier Software & Technology. Vernier Software & Technology and vernier.com are trademarks or trade dress.

Xilinx is the registered trademark of Xilinx, Inc.

Taptite and Trilobular are registered trademarks of Research Engineering & Manufacturing Inc.

FireWire® is the registered trademark of Apple Inc.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Handle Graphics®, MATLAB®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and Simulink Coder™, TargetBox™, and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix®, Tek, and Tektronix, Enabling Technology are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

The ExpressCard™ word mark and logos are owned by PCMCIA and any use of such marks by National Instruments is under license.

The mark LabWindows is used under a license from Microsoft Corporation. Windows is a registered trademark of Microsoft Corporation in the United States and other countries.

Other product and company names mentioned herein are trademarks or trade names of their respective companies.

An NI Partner is a business entity independent from NI and has no agency, partnership, or joint-venture relationship with NI.

Parent topic:

Important Information

<!--NI_TOPIC bundle=ni-vision-assistant path=use-color-pattern-matching.html language=enus -->
## TOPIC 00155: Use Color Pattern Matching

- bundle_id: `ni-vision-assistant`
- source_path: `use-color-pattern-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-color-pattern-matching.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Tab In the Step Name textbox, enter a descriptive name for the step. Verify that the Reposition Region of Interest option is enabled if you want to link the region of interest specified in this step to a previously defined coordinate system. Link the region of interest to a coordinate system if

### Use Color Pattern Matching

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Verify that the Reposition Region of Interest option is enabled if
 you want to link the region of interest specified in this step to a previously
 defined coordinate system.
3. Link the region of interest to a coordinate system if the position of the object
 under inspection changes from image to image, and you need to adjust the
 position of the region of interest to match the new location of the object.

#### Template Tab

1. Create or select the template you want to use for comparison. 
 By default, the center of the template is used as the focal point of the
 template. You can change the location of the focal point to any position in
 the template. Change the focal point of the template by dragging the red
 pointer in the template image or adjusting the Match
 Offset values.
  - To create a new template, complete the following steps:
    1. Click Create Template .
    2. Select an ROI and click OK .
    3. Enter a File Name for the template and
 click OK .
  - To use an existing template, complete the following steps:
    1. Click Load from File .
    2. Browse to the appropriate template image and click
 OK .
2. Modify the Ignore Black and White and Sat.
 Threshold parameters as necessary.

#### Settings Tab

1. Modify Number of Matches to Find , Minimum
 Score , Color Score Weight ,
 Color Sensitivity , and Search
 Strategy as necessary.
2. Select Search for Rotated Patterns to indicate that the
 match can be a rotated version of the template. You can restrict the amount of
 rotation you want to allow by specifying an acceptable angle range. You also can
 include the mirrored angle range by enabling Mirror
 Angle .
3. Click OK to save this step to the script.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=use-coordinate-systems-with-vision-assistant.html language=enus -->
## TOPIC 00156: Use Coordinate Systems with Vision Assistant Express VIs

- bundle_id: `ni-vision-assistant`
- source_path: `use-coordinate-systems-with-vision-assistant.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-coordinate-systems-with-vision-assistant.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a coordinate system in one instance of a Vision Assistant Express VI and reference that coordinate system in a second instance of a Vision Assistant Express VI.Complete the following steps to set up a reference coordinate system using the Vision Assistant Express VI. Place the Vision

### Use Coordinate Systems with Vision Assistant Express VIs

You can create a coordinate system in one instance of a Vision Assistant Express VI and reference
 that coordinate system in a second instance of a Vision Assistant Express VI.

Complete the following steps to set up a reference coordinate system using the Vision Assistant
 Express VI.

1. Place the Vision Assistant Express VI on the LabVIEW block diagram.
2. Develop your vision application using the Vision Assistant processing functions.
3. Set up a coordinate system using the Set Coordinate System step . Coordinate system origins are based on feature locations. You can locate features using the following steps: Edge Detector, Find Straight Edge, Adv. Straight Edge, Find Circular Edge, Pattern Matching, Geometric Matching, Clamp.
4. When you have finished developing your application, click Select Controls.
5. Select the controls and indicators that you want to be able to programmatically set in LabVIEW. To use a reference coordinate system in another Express VI instance, you must select the Coordinate System Out control.
6. Click Finish to return to LabVIEW and update the Express VI.
7. Place a second instance of the Vision Assistant Express VI on the LabVIEW block diagram. If you configured a Set Coordinate System step in the first instance of the Vision Assistant Express VI, the Select Coordinate System dialog will open.
8. If you want to use the coordinate system defined in the first instance of the Vision Assistant Express VI as a reference coordinate system in the second instance of the Vision Assistant Express VI, select I want to use a coordinate system defined in the following VI in this Express VI .
9. Select the VI that creates the coordinate system from the drop-down listbox.
10. When the second instance of the Vision Assistant Express VI dialog opens, you will see a Set Coordinate System step in your script. You cannot edit the step in the second instance, but you can delete the step from the script. The Express VI will be created with a Coordinate System in input control. It is your responsibility to manually wire the Coordinate System Out from the first Express VI to the Coordinate System in of the second Express VI.

#### Considerations

- When you open an instance of the Vision Assistant Express VI that references a
 coordinate system from a previous instance of an Express VI, Vision Assistant
 opens with the last image used to configure the coordinate system. You cannot
 modify the image because the regions of interest you define in subsequent steps
 must be able to reference the image.
- The image used to define the coordinate system must be available when you edit
 the Express VI that references that coordinate system. This means you must edit
 or run the Express VI that defines the coordinate system before editing the
 Express VI that references the coordinate system.
- If you try to edit the Express VI when an image is not available, Vision
 Assistant prompts you to either run the VI that defines the coordinate system or
 disable the repositioning of regions of interest in the steps that reference
 that specific coordinate system.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=use-object-tracking-setup.html language=enus -->
## TOPIC 00157: Use Object Tracking Setup

- bundle_id: `ni-vision-assistant`
- source_path: `use-object-tracking-setup.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-object-tracking-setup.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: This function allows tracking objects from frame to frame. Main Tab In the Step Name textbox, enter a descriptive name for the step. Create or open an object tracking file. Click New Object Tracking File or Edit Object Tracking File to launch the Object Tracking Training Interface. Objects Tab Selec

### Use Object Tracking Setup

This function allows tracking objects from frame to frame.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Create or open an object tracking file. Click New Object Tracking
 File or Edit Object Tracking File to
 launch the Object Tracking Training Interface.

#### Objects Tab

1. Select an object in the Objects to Track list box.
2. Set Initial Position to
 User-Defined or a measurement defined in a previous
 step. Measurements are available if the script contains previous steps that
 produce points or angles, such as a pattern matching step.
3. If you select User-Defined , use the
 X and Y form fields or click
 the object in the image to set the initial position of the object.
4. Set the Initial Angle of the object. Note Select a different object in
 the Objects to Track list box to set the
 Initial Position and Initial
 Angle of the object.
5. Select Run Once 
 to track an object on subsequent images, or to advance
 frames until an object appears in the image.
6. If the algorithm does not return the correct position of the objects, click
 Auto Detect Objects to locate the objects in the
 current image.

#### Settings Tab

1. Set the Minimum Score for the object on a scale of
 0 to 1,000 , where 1,000 
 indicates a perfect match.
2. Set Algorithm to Shape Adapted Mean
 Shift or Traditional Mean Shift .
  - Traditional Mean Shift tracks changes in object
 position, but not changes in shape, size, or rotation.
  - Shape Adapted Mean Shift tracks changes in object
 position, shape, size, and rotation.
3. Set the maximum acceptable scale, rotation, and shape changes.

The results table indicates if the object was found or not found, the X and Y
 coordinates, the angle, and the score of an object on a scale of 0
 to 1,000, where 1,000 indicates a perfect
 match.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=use-object-tracking-setup_2.html language=enus -->
## TOPIC 00158: Use Object Tracking Setup

- bundle_id: `ni-vision-assistant`
- source_path: `use-object-tracking-setup_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-object-tracking-setup_2.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: This function allows tracking objects from frame to frame. Main Tab In the Step Name textbox, enter a descriptive name for the step. Create or open an object tracking file. Click New Object Tracking File or Edit Object Tracking File to launch the Object Tracking Training Interface. Objects Tab Selec

### Use Object Tracking Setup

This function allows tracking objects from frame to frame.

#### Main Tab

1. In the Step Name textbox, enter a descriptive name for
 the step.
2. Create or open an object tracking file. Click New Object Tracking
 File or Edit Object Tracking File to
 launch the Object Tracking Training Interface.

#### Objects Tab

1. Select an object in the Objects to Track list box.
2. Set Initial Position to
 User-Defined or a measurement defined in a previous
 step. Measurements are available if the script contains previous steps that
 produce points or angles, such as a pattern matching step.
3. If you select User-Defined , use the
 X and Y form fields or click
 the object in the image to set the initial position of the object.
4. Set the Initial Angle of the object. Note Select a different object in
 the Objects to Track list box to set the
 Initial Position and Initial
 Angle of the object.
5. Select Run Once 
 to track an object on subsequent images, or to advance
 frames until an object appears in the image.
6. If the algorithm does not return the correct position of the objects, click
 Auto Detect Objects to locate the objects in the
 current image.

#### Settings Tab

1. Set the Minimum Score for the object on a scale of
 0 to 1,000 , where 1,000 
 indicates a perfect match.
2. Set Algorithm to Shape Adapted Mean
 Shift or Traditional Mean Shift .
  - Traditional Mean Shift tracks changes in object
 position, but not changes in shape, size, or rotation.
  - Shape Adapted Mean Shift tracks changes in object
 position, shape, size, and rotation.
3. Set the maximum acceptable scale, rotation, and shape changes.

The results table indicates if the object was found or not found, the X and Y
 coordinates, the angle, and the score of an object on a scale of 0
 to 1,000, where 1,000 indicates a perfect
 match.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=use-the-caliper-tool.html language=enus -->
## TOPIC 00159: Use the Caliper Tool

- bundle_id: `ni-vision-assistant`
- source_path: `use-the-caliper-tool.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-the-caliper-tool.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select the type of geometric feature you want to compute. When you select a geometric feature, the step displays the minimum number of points you need to select to compute the feature. Select the points that define the geometric featur

### Use the Caliper Tool

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select the type of geometric feature you want to compute. Note When you select a geometric
 feature, the step displays the minimum number of points you need to select to
 compute the feature.
3. Select the points that define the geometric feature using one of the following methods:
  - Click the points overlaid on the image.
  - Select the checkboxes in the Available Points list.
  - Double-click the point names in the Available Points list.

Tip

- If a measurement creates a new point, the new point is
 available for new measurements when you close the
 caliper parameter window and re-open it.
- To save the data, click the Send Data to
 Excel button or the Save
 Results button.
- To deselect all points on the image, click
 Reset .

Parent topic:

Analyzing and Processing Images

Related concepts:

- Find the Angle Made by Three or Four Points
- Find the Angle Made by Two Points
- Find the Area Enclosed by Three or More Points
- Find the Center of Mass Using Three or More Points
- Find the Center of Two Points
- Find the Circular Fit Using Three or More Points
- Find the Distance Between Two Points
- Find the Intersection of Two Lines
- Find the Perpendicular Projection of a Point on a Line

<!--NI_TOPIC bundle=ni-vision-assistant path=use-the-color-operators-function.html language=enus -->
## TOPIC 00160: Use the Color Operators Function

- bundle_id: `ni-vision-assistant`
- source_path: `use-the-color-operators-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-the-color-operators-function.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the operators from the Operators list. Select either the Constant or Image option. The Constant option uses a constant and the current image in the operation. The Image option uses the current image and an image stored in

### Use the Color Operators Function

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the operators from the Operators list.
3. Select either the Constant or Image option. The
 Constant option uses a constant and the current image in
 the operation. The Image option uses the current image and an
 image stored in an image buffer. Note For the Mask operator, you can
 select only the Image option. For the Multiply Divide
 operator, you must specify an Image and a
 Constant.
4. Enter the constant or select the image buffer that contains the image you are adding to the source image or enter the constant value.
5. Click OK to add the step to the script and close the
 Parameters window.

Note

Parent topic:

Analyzing and Processing Images

Related concepts:

- Retrieve an Image from an Image Buffer
- Store an Image in an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=use-the-operators-function.html language=enus -->
## TOPIC 00161: Use the Operators Function

- bundle_id: `ni-vision-assistant`
- source_path: `use-the-operators-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/use-the-operators-function.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Step Name textbox, enter a descriptive name for the step. Select one of the operators from the Operators list. Select either the Constant or Image option. The Constant option uses a constant and the current image in the operation. The Image option uses the current image and an image stored in

### Use the Operators Function

1. In the Step Name textbox, enter a descriptive name for the step.
2. Select one of the operators from the Operators list.
3. Select either the Constant or Image option. The
 Constant option uses a constant and the current image in
 the operation. The Image option uses the current image and an
 image stored in an image buffer. Note For the Mask operator, you can
 select only the Image option. For the Multiply Divide
 operator, you must specify an Image and a
 Constant.
4. Enter the constant or select the image buffer that contains the image you are combining with the source image.
5. Click OK to perform the operation. Note You must already have an image
 stored in an image buffer before you can perform an operation using the current
 image and another image. The buffered image must have the same size and type as
 the source image.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Retrieve an Image from an Image Buffer
- Store an Image in an Image Buffer

<!--NI_TOPIC bundle=ni-vision-assistant path=user-manual-welcome.html language=enus -->
## TOPIC 00162: Vision Assistant User Manual

- bundle_id: `ni-vision-assistant`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Vision Assistant User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### Vision Assistant
 User Manual

The Vision Assistant User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ni-vision-assistant path=using-the-solution-wizard.html language=enus -->
## TOPIC 00163: Using the Solution Wizard

- bundle_id: `ni-vision-assistant`
- source_path: `using-the-solution-wizard.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/using-the-solution-wizard.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Solution Wizard to view typical uses of Vision in imaging and machine vision applications. Select Help»Solution Wizard. Select an industry and an application from the list in the left window. Look at the image representing the application and read the brief problem description. Click Load So

### Using the Solution Wizard

Use the Solution Wizard to view typical uses of Vision in imaging and machine vision
 applications.

1. Select Help»Solution Wizard .
2. Select an industry and an application from the list in the left window.
3. Look at the image representing the application and read the brief problem description.
4. Click Load Solution to load images and a solution script into Vision Assistant. When you load the solution into Vision Assistant, run the script on the Solution Wizard images or on the own images. You also can alter the script to experiment with different functions and parameters.

Related concepts:

- Getting Help in Vision Assistant

<!--NI_TOPIC bundle=ni-vision-assistant path=using-the-vision-assistant-express-vi.html language=enus -->
## TOPIC 00164: Using the Vision Assistant Express VI

- bundle_id: `ni-vision-assistant`
- source_path: `using-the-vision-assistant-express-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/using-the-vision-assistant-express-vi.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Vision Assistant Express VI to quickly create a vision application and to select the controls and indicators that you want to be able to programmatically change in LabVIEW.Complete the following steps if you are using the Vision Assistant Express VI for the first time in your VI. If you are

### Using the Vision Assistant Express VI

Use the Vision Assistant Express VI to quickly create a vision application and to select the
 controls and indicators that you want to be able to programmatically change in
 LabVIEW.

Complete the following steps if you are using the Vision Assistant Express VI for the first time
 in your VI. If you are using the Vision Acquisition Express VI, skip this section and
 proceed to the Using the Vision Assistant Express VI with the Vision Acquisition Express
 VI section.

Tip

1. Create a VI and add it to the LabVIEW project under the FPGA target.
2. Open the VI you created and drop the Vision Assistant Express VI on the
 block diagram. The code generated inside the Express VI is LabVIEW FPGA
 code.

1. Open an image to process from the Vision Assistant environment. Click Open
 Image 
 or click File » Open
 Image . Browse to the image you want to open and click
 Open .
2. Develop your vision application using the Vision Assistant processing functions.
3. When you have finished developing your application, click Select Controls .
4. Select the controls and indicators that you want to be able to programmatically set in LabVIEW.
 The Required Controls and Required
 Indicators appear on the Express VI connector pane by default. Tip To process color
 images faster, you may want to transfer the Bayer encoded 8-bit image to an FPGA
 target and enable Perform Bayer Decoding on the FPGA.
 Performing the Bayer decoding on the FPGA frees processor resources and
 bandwidth since an 8-bit image is transferred to the FPGA. The selected
 controls and indicators appear on the Express VI connector pane after you exit the
 configuration interface.
5. When you are finished selecting controls and indicators, complete one of the following options:
  - Click Finish to return to LabVIEW and update the Express VI.
  - Click Cancel to return to LabVIEW without modifying the Express VI.
  - Click Process Images to modify your application.
6. To edit the Vision Assistant Express VI, double-click the Express VI on the block diagram. Note Any changes you make
 in the Express VI dialog box could result in broken wires on the block diagram.

#### Use the
 Vision Assistant Express VI with the Vision Acquisition Express VI

Note

Use the Vision Acquisition Express VI to easily configure acquisitions
 from a camera or to simulate an acquisition. Use the Vision Assistant Express VI to
 process the image acquired with the Vision Acquisition Express VI.

1. Place the Vision Acquisition Express VI on the block diagram and configure your
 acquisition. Refer to the Vision Acquisition Express VI Help for more
 information. Note You must click the Test button in the
 Configure Acquisition Settings step of the Vision
 Acquisition Express VI wizard to be able to use the acquired image in Vision
 Assistant.
2. Place the Vision Assistant Express VI on the block diagram. Vision Assistant
 will automatically open the image acquired from the Configure
 Acquisition Settings step of the Vision Acquisition Express VI
 wizard. Note This
 feature only works when the Vision Assistant Express VI is placed on the
 block diagram. Otherwise, Vision Assistant follows the behavior described in
 *Vision Assistant Express VI Image Caching*.
3. Develop your vision application using the Vision Assistant processing
 functions.
4. When you have finished developing your application, click Select
 Controls .
5. Select the controls and indicators that you want to be able to programmatically
 set in LabVIEW. The selected controls and indicators appear on the Express VI
 connector pane after you exit the configuration interface. Note The Required
 Controls and Required Indicators
 appear on the Express VI connector pane by default.
6. When you are finished selecting controls and indicators, complete one of the
 following options:
  - Click Finish to return to LabVIEW and update the
 Express VI.
  - Click Cancel to return to LabVIEW without
 modifying the Express VI.
  - Click Process Images to modify your
 application.
7. To edit the Vision Assistant Express VI, double-click the Express VI on the
 block diagram. Note Any changes you make in the Express VI dialog box could result in broken
 wires on the block diagram.

Parent topic:

Analyzing and Processing Images

Related concepts:

- Vision Assistant Express VI Image Caching
- Use Coordinate Systems with Vision Assistant Express VIs

<!--NI_TOPIC bundle=ni-vision-assistant path=view-an-image-in-3d.html language=enus -->
## TOPIC 00165: View an Image in 3D

- bundle_id: `ni-vision-assistant`
- source_path: `view-an-image-in-3d.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/view-an-image-in-3d.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 3D View function analyzes the image and displays information for you to review. This function does not modify the image. The 3D View function works only with 8-bit images. Set the direction orientation. Specify the maximum Height of a 3D pixel. Specify the angle between the horizontal axis and b

### View an Image in 3D

Note

- The 3D View function analyzes the image and displays
 information for you to review. This function does
 not modify the image.
- The 3D View function works only with 8-bit images.

1. Set the direction orientation.
2. Specify the maximum Height of a 3D pixel.
3. Specify the angle between the horizontal axis and baseline in .
4. Define the angle between the horizontal axis and second baseline in .
5. Set the size Reduction .
6. Click OK to close the Parameter window.

Tip

Invert

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=vision-assistant-express-vi-image-caching.html language=enus -->
## TOPIC 00166: Vision Assistant Express VI Image Caching

- bundle_id: `ni-vision-assistant`
- source_path: `vision-assistant-express-vi-image-caching.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/vision-assistant-express-vi-image-caching.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: When image caching is enabled, the Vision Assistant Express VI automatically gets the last image used when the VI was run. To disable/enable image caching, right-click the Vision Assistant Express VI in the block diagram and select Disable Image Caching or Enable Image Caching. Image caching is enab

### Vision Assistant Express VI Image Caching

When image caching is enabled, the Vision Assistant Express VI automatically gets the last image
 used when the VI was run. To disable/enable image caching, right-click the Vision
 Assistant Express VI in the block diagram and select Disable Image
 Caching or Enable Image Caching. Image caching is
 enabled by default.

When you double-click the Vision Assistant Express VI to edit it, Vision Assistant opens the last
 image used when the VI was run. If you have not run the VI, the Vision Assistant Express
 VI will re-open the last image that was opened.

If you are using the Vision Assistant Express VI with the Vision Acquisition Express VI, the
 first time you place the Vision Assistant Express VI on the block diagram, Vision
 Assistant will automatically open the image acquired from the Configure
 Acquisition Settings step of the Vision Acquisition Express VI
 wizard.

Parent topic:

Analyzing and Processing Images

<!--NI_TOPIC bundle=ni-vision-assistant path=warning-regarding-use-of-national-instruments.html language=enus -->
## TOPIC 00167: WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

- bundle_id: `ni-vision-assistant`
- source_path: `warning-regarding-use-of-national-instruments.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/warning-regarding-use-of-national-instruments.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: YOU ARE ULTIMATELY RESPONSIBLE FOR VERIFYING AND VALIDATING THE SUITABILITY AND RELIABILITY OF THE PRODUCTS WHENEVER THE PRODUCTS ARE INCORPORATED IN YOUR SYSTEM OR APPLICATION, INCLUDING THE APPROPRIATE DESIGN, PROCESS, AND SAFETY LEVEL OF SUCH SYSTEM OR APPLICATION. PRODUCTS ARE NOT DESIGNED, MANU

### WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

YOU ARE ULTIMATELY RESPONSIBLE FOR VERIFYING AND VALIDATING THE SUITABILITY AND RELIABILITY OF THE PRODUCTS WHENEVER THE PRODUCTS ARE INCORPORATED IN YOUR SYSTEM OR APPLICATION, INCLUDING THE APPROPRIATE DESIGN, PROCESS, AND SAFETY LEVEL OF SUCH SYSTEM OR APPLICATION.

PRODUCTS ARE NOT DESIGNED, MANUFACTURED, OR TESTED FOR USE IN LIFE OR SAFETY CRITICAL SYSTEMS, HAZARDOUS ENVIRONMENTS OR ANY OTHER ENVIRONMENTS REQUIRING FAIL-SAFE PERFORMANCE, INCLUDING IN THE OPERATION OF NUCLEAR FACILITIES; AIRCRAFT NAVIGATION; AIR TRAFFIC CONTROL SYSTEMS; LIFE SAVING OR LIFE SUSTAINING SYSTEMS OR SUCH OTHER MEDICAL DEVICES; OR ANY OTHER APPLICATION IN WHICH THE FAILURE OF THE PRODUCT OR SERVICE COULD LEAD TO DEATH, PERSONAL INJURY, SEVERE PROPERTY DAMAGE OR ENVIRONMENTAL HARM (COLLECTIVELY, "HIGH-RISK USES"). FURTHER, PRUDENT STEPS MUST BE
 TAKEN TO PROTECT AGAINST FAILURES, INCLUDING PROVIDING BACK-UP AND SHUT-DOWN MECHANISMS. NI EXPRESSLY DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTY OF FITNESS OF THE PRODUCTS OR SERVICES FOR HIGH-RISK USES.

Parent topic:

Important Information

<!--NI_TOPIC bundle=ni-vision-assistant path=warranty.html language=enus -->
## TOPIC 00168: Warranty

- bundle_id: `ni-vision-assistant`
- source_path: `warranty.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-assistant/raw/resource/enus/warranty.html
- document_id: `ni-vision-assistant`
- page_type: `leaf`
- content_type: `concept`
- source_description: The media on which you receive National Instruments software are warranted not to fail to execute programming instructions, due to defects in materials and workmanship, for a period of 90 days from date of shipment, as evidenced by receipts or other documentation. National Instruments will, at its o

### Warranty

The media on which you receive National Instruments software are warranted not to fail to execute programming instructions, due to defects in materials and workmanship, for a period of 90 days from date of shipment, as evidenced by receipts or other documentation. National Instruments will, at its option, repair or replace software media that do not execute programming instructions if National Instruments receives notice of such defects during the warranty period. National Instruments does not warrant that the operation of the software shall be uninterrupted or error free.

A Return Material Authorization (RMA) number must be obtained from the factory and clearly marked on the outside of the package before any equipment will be accepted for warranty work. National Instruments will pay the shipping costs of returning to the owner parts which are covered by warranty.

National Instruments believes that the information in this document is accurate. The document has been carefully reviewed for technical accuracy. In the event that technical or typographical errors exist, National Instruments reserves the right to make changes to subsequent editions of this document without prior notice to holders of this edition. The reader should consult National Instruments if errors are suspected. In no event shall National Instruments be liable for any damages arising out of or related to this document or the information contained in it.

EXCEPT AS SPECIFIED HEREIN, NATIONAL INSTRUMENTS MAKES NO WARRANTIES, EXPRESS OR IMPLIED, AND SPECIFICALLY DISCLAIMS ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. CUSTOMER'S RIGHT TO RECOVER DAMAGES CAUSED BY FAULT OR NEGLIGENCE ON THE PART OF NATIONAL INSTRUMENTS SHALL BE LIMITED TO THE AMOUNT THERETOFORE PAID BY THE CUSTOMER. NATIONAL INSTRUMENTS WILL NOT BE LIABLE FOR DAMAGES RESULTING FROM LOSS OF DATA, PROFITS, USE OF PRODUCTS, OR INCIDENTAL OR CONSEQUENTIAL DAMAGES, EVEN IF ADVISED OF THE POSSIBILITY THEREOF. This limitation of the liability of National Instruments will apply regardless of the form of action, whether in contract or tort, including negligence. Any action against National Instruments must be brought within one year after the cause of action accrues. National Instruments shall not be liable for any delay in performance due to causes beyond its reasonable control. The warranty provided herein does not cover damages, defects, malfunctions, or service failures caused by owner's failure to follow the National Instruments installation, operation, or maintenance instructions; owner's modification of the product; owner's abuse, misuse, or negligent acts; and power failure or surges, fire, flood, accident, actions of third parties, or other events outside reasonable control.

Parent topic:

Important Information
