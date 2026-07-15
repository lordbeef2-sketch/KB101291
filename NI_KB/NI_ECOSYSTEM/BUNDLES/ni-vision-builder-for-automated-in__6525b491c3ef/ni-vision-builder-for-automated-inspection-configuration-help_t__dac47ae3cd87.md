# NI DOCUMENT BUNDLE: ni-vision-builder-for-automated-inspection-configuration-help

<!--NI_BUNDLE_CHUNK bundle=ni-vision-builder-for-automated-inspection-configuration-help start=1 end=64 -->
<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/1dbar_controls.html language=enus -->
## TOPIC 00001: Read 1D Barcode Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/1dbar_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/1dbar_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Read 1D Barcode Controls |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_u8.gif'] [IMAGE alt='image' src='vision_i16.gif'] [IMAGE alt='image' src='vision_sgl.gif'] [IMAGE alt='image' src='vision_rgbu32.gif'] [IMAGE alt='image' src='vision_hslu32.gif'] [IMAGE alt='image' src='vision_u16.gif']

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Region of Interest**
  - Specifies the region of the image to process.
- **Reposition Region of Interest**
  - Repositions the region of interest dynamically based on a coordinate system from a previous Set Coordinate System step. Link the region of interest to a coordinate system if the position of the object under inspection changes from image to image, and you need to adjust the position of the region of interest to match the new location of the object.
- **Reference Coordinate System**
  - Specifies the coordinate system to which you want to link the region of interest.
- **Locate Barcode**
  - Automatically detects all barcodes in an image. Minimum Bar Width—Specifies the minimum bar width to read, in pixels. Minimum Edge Strength—Specifies the minimum difference in intensity values between the edge of a bar and its surroundings. Minimum Bars—Specifies the minimum number of bars in a barcode.

#### Settings Tab

- **Auto Setup**
  - Automatically detects barcode types and the number of barcodes to read. Auto setup looks for the following barcode types in an image, in the following order: EAN 13, EAN 8, UPCA, Code 128, MSI, Code 39, Code 93, Codabar, and RSS Limited. Found barcode types are added to the Types of Barcode to Search list. If you know the type of barcodes to search, or only want to locate specific types of barcodes, deselect this option and manually add the barcode to the Types of Barcode to Search list.
- **Types of Barcode to Search**
  - Deselect Auto Setup to enable this control. Click a barcode type to edit it. Click to add a barcode type. Click to remove a barcode type. Click to move a barcode type up in the list, or to move a barcode type down in the list. To optimize barcode classification, order the list of barcode types from the strictest standards to the most lenient, as in the following list: EAN 13 EAN 8 UPCA Code 128 MSI Code 39 Code 93 Codabar Interleaved 2 of 5 RSS Limited Pharmacode
- **Number of Barcodes to Read**
  - Specifies the maximum number of barcodes to read in the image.
- **Validate**
  - Validates the barcode data. If the barcode type is Codabar, Code 39, or Interleaved 2 of 5, the error correction information built into the barcode is used to validate the results. For all other barcode types, either no validation is performed or the validation is performed automatically because the barcode type requires it. Refer to the following table for the sequence of special characters, data, and checksum for each barcode type.
- **Add Special Character to Code Read**
  - Adds the special characters to the encoded data. Only Codabar, Code 128, EAN 8, EAN 13, and UPCA barcodes contain special characters.
- **Add Checksum to Code Read**
  - Adds the checksum value read with the barcode to the encoded data. Refer to the following table for the layout of special characters, data, and checksum for each type of barcode.

#### Results Tab

- **Minimum Score**
  - Specifies a minimum score for a barcode to appear in the Results tree. This value can range from 0 to 1000, where 1000 indicates a perfect score. The default is 500.
- **Results**
  - Displays the following data for each barcode: Complete Data—The complete data read from the barcode, including special character 1, 2, and checksum. Data—Data read from the barcode, not including special character 1, 2, or checksum. Special Character 1—The first character preceding the barcode, if applicable. Special Character 2—The second character preceding the barcode, if applicable. Checksum—The character following the barcode, if applicable. Barcode Type—Indicates the type of barcode read. Bounding Box—Expand to view the X and Y coordinates of each corner of the barcode bounding box.

#### Limits Tab

- **Pass Inspection if...**
  - Specifies the limits you set on each barcode.
- **Code Equals**
  - Specifies a string that the decoded barcode must match in order for the step to pass.
- **Code Contains**
  - Specifies a string that the decoded barcode must contain in order for the step to pass. You can use the following wildcard characters: Special Character Interpretation . Matches any character. ? Matches zero or one instances of the expression preceding ?. [ ] Encloses alternates. For example, [abc] matches a, b, or c. - (dash) Indicates a range when used between digits or letters enclosed in brackets. [0-5] indicates a numerical range of 0 through 5. [-g] indicates an alphabetical range of a through g. ~ Excludes the subsequent set of characters, including non-displayable characters, when it appears as the first character enclosed in brackets. [~0-9] matches any character except 0 through 9. ^ Excludes the subsequent set of characters, not including non-displayable characters, when it appears as the first character enclosed in brackets. [^0-9] matches any character, including the space character, except 0 through 9.
- **Code Read**
  - Displays the data decoded from each barcode in the step.

Parent topic:

Identify Parts Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/booleanobjects.html language=enus -->
## TOPIC 00002: Boolean Palette

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/booleanobjects.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/booleanobjects.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Boolean Palette

Boolean controls and indicators represent values that can be only true or false. 
For example, you can use a Boolean LED to indicate when an inspection fails.
Use the Boolean controls and indicators located on the Boolean to create buttons, switches, and lights.

In addition to control labels, Boolean controls and indicators have 
Boolean text labels that describe what each Boolean state indicates.

You can customize Boolean controls with one of six mechanical actions that simulate the behavior of physical switches. 
Right-click a control and select Mechanical Action to customize how the control behaves when you click it.

Parent topic:

Controls Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calculator_concepts.html language=enus -->
## TOPIC 00003: Calculator Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calculator_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calculator_concepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calculator Concepts |
| --- | --- |

Calculator

Parent topic:

Use Additional Tools Palette

Related example inspections

- Tutorial 4 - Two Cameras Inspection.vbai
- Segment Color Image Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calculator_controls.html language=enus -->
## TOPIC 00004: Calculator Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calculator_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calculator_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calculator Controls |
| --- | --- |

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Edit Inputs/Outputs**
  - Launches a tabbed dialog box in which you can change the inputs and outputs for the calculation.
- **Remove Broken Wires**
  - Removes broken wires in the calculation diagram.
- **Show Functions Palette**
  - Displays the palette that contains the numeric, comparison, Boolean, and string controls necessary to develop a calculation diagram.

#### Measurements Tab

- **Compute Results**
  - Computes the results of the diagram and displays the results in the table.

#### Limits Tab

- **Step Result Output is True**
  - Specifies that the inspection passes only when the specified Input Measurements are found and the result of the computation connected to the Step Result output terminal is True.

Parent topic:

Use Additional Tools Palette

Related example inspections

- Tutorial 4 - Two Cameras Inspection.vbai
- Segment Color Image Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calculator_faq.html language=enus -->
## TOPIC 00005: Calculator FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calculator_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calculator_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calculator FAQs |
| --- | --- |

Q: How can I make the Calculator Step Result the result for the entire inspection?

Calculator

1. Insert a Set Inspection Status step.
2. Select the Set to measurement value option for the Inspection Status control .
3. Select a measurement computed by the Calculator step from the listbox.
4. Click OK to add the step to the inspection.

Q: How do I use Formula Nodes?

Vision Builder AI Configuration Help

[IMAGE alt='Note' src='note.gif']

Note

Vision Builder AI 
 Configuration Help

Help»

Online 
 Help

Parent topic:

Use Additional Tools Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calibrate_concepts.html language=enus -->
## TOPIC 00006: Calibrate Image Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calibrate_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calibrate_concepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calibrate Image Concepts |
| --- | --- |

Calibrate images in order to return accurate measurements in real-world units.
 Vision Builder AI can calibrate images containing linear, perspective, or nonlinear distortion introduced by a rectilinear lens or sensor misalignment.

Calibration

Calibrate Image

[IMAGE alt='Tip' src='tip.gif']

Tip

Tools»

System Resource Manager

System Resource Manager

Parent topic:

Enhance Images Palette

Related example inspections

- Calibrate Image Step Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calibrate_controls.html language=enus -->
## TOPIC 00007: Calibrate Image Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calibrate_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calibrate_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calibrate Image Controls |
| --- | --- |

Supported image types:

[IMAGE alt='a' src='vision_u8.gif'] [IMAGE alt='a' src='vision_u16.gif'] [IMAGE alt='a' src='vision_i16.gif'] [IMAGE alt='a' src='vision_sgl.gif'] [IMAGE alt='a' src='vision_rgbu32.gif'] [IMAGE alt='a' src='vision_hslu32.gif']

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Calibration**
  - Lists the calibrations that you can apply to the acquired image. The available calibrations are specific to the resolution of the acquired image, and may be specific to the selected acquisition device.
- **Edit**
  - Launches the NI Calibration Training Interface so that you can edit the selected calibration.
- **Correct Image**
  - Spatially corrects the acquired image based on the calibration.
- **Interpolation Type**
  - Specifies the interpolation method used to obtain the spatially corrected image. Zero Order—Rounds to the nearest integral pixel location. Bi-Linear—Uses linear interpolation in both the x-direction and y-direction to compute the pixel location.
- **Replace Value**
  - The pixel value used to replace uncorrected regions in the spatially corrected image.
- **Save Calibrated Image to File**
  - Saves the calibrated image to the calibration file. To make this option available, select the Learn Calibration at Each Iteration checkbox on the Calibration Data tab. Note Vision Builder AI saves calibration files to the following default location: C:\\ProgramData\\National Instruments\\Vision Builder AI\\Calibration On remote targets, the calibration is saved to /var/local/natinst/vbai/Calibration/.
- **Variable Image Size**
  - Enable this option if the image acquisition step returns different image sizes; for example, when using the Variable Height Acquisition feature while acquiring from a line scan camera. When the Variable Image Size option is enabled, only Point Distance calibrations are supported and any calibration is relearned at each iteration.
- **New Calibration**
  - Launches the NI Calibration Training Interface so that you can create a new calibration for the selected acquisition device.

#### Calibration Data Tab

- **Learn Calibration at Each Iteration**
  - Computes the calibration to apply to the image each time the inspection iterates. When selected, you can edit the values in the Calibration Data list to use point, distance, or axis reference angle results from previous steps.

The contents of the Calibration Data tree vary depending on the calibration type. 
 Refer to the *NI Calibration Training Interface Help* for detailed 
 information about the items listed for each calibration summary. 
 If you enable the **Learn Calibration at Each Iteration** checkbox, you can 
 edit the calibration axis values displayed in the Calibration Data tree.

- **Relearn Grid**
  - Computes the image distortion for each iteration. This option only applies to grid images.
- **Origin**
  - Specifies the origin of the calibration axis, in pixel coordinates.
- **Angle Type**
  - Specifies the type of measurement that defines the calibration X axis. Angle Value—Specifies the angle between the calibration X axis and the image X axis, in degrees. X-Axis Point—Specifies a point along the calibrated X axis. Use the X and Y controls to adjust the exact position of the point.
- **Angle Value**
  - Specifies the angle between the calibration X axis and the image X axis, in degrees.
- **X-Axis Point**
  - Specifies a point along the calibrated X axis. Select a previous measurement, or use the X and Y controls to adjust the exact position of the point.
- **Axis Reference**
  - Specifies whether the Y axis reference is direct or indirect. The following figures illustrate X axis directions. An indirect axis orientation, as shown in figure A, corresponds to a typical coordinate system for digital images where the top left pixel serves as the origin. A direct axis orientation, as shown in figure B, corresponds to a real-world cartesian coordinate system.

Parent topic:

Enhance Images Palette

Related links

Point Distance Calibration Summary

Point Coordinate Calibration Summary

Distortion Model Calibration Summary

Camera Model Calibration Summary

Microplane Calibration Summary

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/calibrate_faq.html language=enus -->
## TOPIC 00008: Calibrate Image FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/calibrate_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/calibrate_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Calibrate Image FAQs |
| --- | --- |

Q: How do I prevent calibrated measurements from varying from part to part?

If the position of the parts in the inspection images varies considerably, enable the Learn Calibration at Each Iteration control. When this control is enabled, the inspection learns calibration information based on the specified Calibration Data values during each iteration of the inspection.

Q: Is it possible to configure Vision Builder AI to periodically recalibrate the vision system?

Yes. For example, you can recalibrate the vision system with two separate inspections.

The first inspection is dedicated to system calibration, and can locate features disposed at known locations in the image. A calibration step uses these points of reference to learn a new calibration, and saves the calibrated image to file.

The second inspection performs visual inspection tasks on calibrated images. The image acquisition steps use the calibration file saved from the first inspection to calibrate the acquired images.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/caliper_concepts.html language=enus -->
## TOPIC 00009: Caliper Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/caliper_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/caliper_concepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Caliper Concepts |
| --- | --- |

Caliper

The region of interest contains a number of search lines along which the step searches for sharp transitions in pixel 
 intensities, which typically characterize the edge of an object in the image. The step searches for two edge points 
 along each search line and computes the distance between the two detected edge points. The step returns the minimum 
 or maximum distance measurement of all the search lines as the caliper measurement.

Parent topic:

Measure Features Palette

Related example inspections

- Tutorial 3 - Decision Making.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/caliper_controls.html language=enus -->
## TOPIC 00010: Caliper Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/caliper_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/caliper_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Caliper Controls |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_u8.gif'] [IMAGE alt='image' src='vision_i16.gif'] [IMAGE alt='image' src='vision_u16.gif']

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Region of Interest**
  - Specifies the region of the image to process.
- **Reposition Region of Interest**
  - Repositions the region of interest dynamically based on a coordinate system from a previous Set Coordinate System step. Link the region of interest to a coordinate system if the position of the object under inspection changes from image to image, and you need to adjust the position of the region of interest to match the new location of the object.
- **Reference Coordinate System**
  - Specifies the coordinate system to which you want to link the region of interest.

#### Settings Tab

- **Process**
  - Specifies the type of caliper to use. Horizontal Max Caliper—Measures a distance in the horizontal direction from the vertical sides of the region of interest toward the center of the region of interest. Horizontal Min Caliper—Measures a distance in the horizontal direction from the center of the region of interest toward the vertical sides of the region of interest. Vertical Max Caliper—Measures a distance in the vertical direction from the horizontal sides of the region of interest toward the center of the region of interest. Vertical Min Caliper—Measures a distance in the vertical direction from the center of the region of interest toward the horizontal sides of the region of interest.
- **Gap**
  - Specifies the size, in pixels, of the distance between search lines.
- **Edge Strength**
  - Specifies the minimum required difference between the intensity values of the edge and surrounding pixels.
- **Smoothing**
  - Specifies the number of pixels averaged to find the contrast at either side of the edge.
- **Steepness**
  - Specifies the maximum distance within which the change of edge strength must occur. Steepness characterizes the slope of the edge. Use higher values for more gradual transitions in pixel intensities between the background and the edge.
- **Edge Strength Profile**
  - Displays a strength profile of the edges found along the search line located in the middle of the region of interest.
- **Additional Points to Log**
  - None—Does not log any additional points. First Edge of Each Search Line—Logs the first edge found in each direction of a search line. If a search line does not find an edge, the edge coordinates are logged as NaN. If a search line finds an edge in both directions, this mode returns the distance between those edges. Tip Use First Edge of Each Search Line if you need to log edges in a consistent order for your application. All Edges Found—Logs the first edge found in each direction of the search line. If a search line does not find an edge, no result is logged. Tip Use All Edges Found if you do not need to log edges in a consistent order for your application, and you want the step to return only the found edges.

#### Limits Tab

[IMAGE alt='Note' src='note.gif']

Note

Calibrate Image

- **Minimum Distance**
  - Specifies the minimum required distance. The step fails if the measured distance is less than the specified value.
- **Maximum Distance**
  - Specifies the maximum allowed distance. The step fails if the measured distance exceeds the specified value.
- **Current Distance**
  - Indicates the distance measured between the caliper arms.

Parent topic:

Measure Features Palette

Related example inspections

- Tutorial 3 - Decision Making.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/caliper_faq.html language=enus -->
## TOPIC 00011: Caliper FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/caliper_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/caliper_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Caliper FAQs |
| --- | --- |

Q: The step returns results in pixels. How can I obtain measurements expressed in a physical unit?

Calibrate the image. You can create a calibration on the Calibration tab 
 of any image acquisition step or, if you need to learn the calibration at each iteration of the inspection, you can use the 
 Calibrate Image step to define calibration parameters using results from previous steps.

Q: The Reposition Region of Interest and Reference Coordinate System controls are disabled. How can I make these options available?

Insert a Set Coordinate System step before this step to make the Reposition Region of Interest and Reference Coordinate System controls available.

Parent topic:

Measure Features Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/colorpalette_controls.html language=enus -->
## TOPIC 00012: Color Palette Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/colorpalette_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/colorpalette_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Color Palette Controls

- **Color Palette Name**
  - Specifies a unique name to identify the color palette in the inspection.
- **Image Bit Depth**
  - Specifies the number of bits used to encode the value of a pixel. The type of image acquisition device you use determines whether you can use this control.
- **Interpolation Method**
  - Specifies the interpolation technique used to color the image. Steps—Maps a grayscale value to a specific color palette sample, with no color values in between specified values. Linear—Draws a straight line between grayscale values. Spline—Draws parametric curves between grayscale values. Cubic Hermite—Uses a cubic Hermite spline to draw parametric curves between grayscale values. Lagrange—Applies Lagrange polynomial interpolation between grayscale values.
- **Color Palette Samples**
  - Configures which colors to assign to specific grayscale values. Click a sample to change the color or to highlight or change the location of the grayscale value in the Grayscale to Color Mapping Graphs. You can change the location of the grayscale values in the Grayscale Value boxes or by dragging the vertical lines in the Grayscale to Color Mapping Graphs.
- **Add**
  - Adds a color palette sample.
- **Delete**
  - Deletes the selected color palette sample.
- **Sort**
  - Reorders the color palette samples based on their grayscale values.
- **Start from Palette**
  - Selects a default palette to apply to the image. Click Apply to apply the palette, and click Preview to see the preview of the palette applied in the main display window. Grayscale—Applies a gradation from black to white. Binary—Applies a specific RGB value to each grayscale value. Gradient—Applies a gradation from red to white with a prominent range of light blue in the upper range. Rainbow—Applies a gradation from blue to red with a prominent range of greens in the middle value range. Full Rainbow—Applies a gradation from black to white with an equal amount of each color range in between. Temperature—Applies a gradation from light brown to dark brown. Iron—Applies a gradation from blue to yellow. Hot Iron (DICOM)—Applies a gradation from red to orange. This palette is often used in nuclear medicine applications. Hot Metal Blue (DICOM)—Applies a gradation from blue to orange. This palette is often used in nuclear medicine or Positron Emission Tomography (PET) applications to view differences in signal intensity. PET (DICOM)—Applies a gradation from blue to orange. This palette is often used in Positron Emission Tomography (PET) applications to color PET images superimposed onto CT images. PET 20 (DICOM)—Applies one of 20 color values to the image. This palette is often used in Positron Emission Tomography (PET) applications to view differences in signal intensity. <Previously created color palette>—Selects a previously created color palette to colorize an image.
- **Apply**
  - Applies the selected Interpolation Method, Color Palette Samples, and Start from Palette configurations to the image. Click Preview to see the a preview of the palette in the main display window.
- **Preview**
  - Generates a preview of the configured settings in the main display window.
- **Grayscale to Color Mapping Graphs**
  - Displays the red, green, and blue values of each grayscale sample. Click the vertical bars in the graphs to drag the grayscale values left or right.
- **Color Palette Preview**
  - Displays the configured color palette spectrum used to color the image.
- **OK**
  - Closes the Color Palette Editor and applies the specified color settings to the image.
- **Cancel**
  - Closes the Color Palette Editor without applying any changes to the image.

Refer to [How to Use the Color Palette Editor](colorpalette_howto.html) for information about how to add, edit, or delete a palette.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/colorpalette_faq.html language=enus -->
## TOPIC 00013: Color Palette FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/colorpalette_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/colorpalette_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Color Palette FAQs

Q: How do I change the color palette of the current image? I cannot see the color palette controls.

The color palette controls are available only in certain steps that modify the content of the image. You can change the color palette in the following steps:

- Acquire Image
- Acquire Image (Smart Camera)
- Read Image File
- Acquire Image (1394, GigE, or USB)
- Select Image
- Vision Assistant
- Run LabVIEW VI
- Segment Color Image
- Filter Image
- Custom Overlay
- Display Image
- Flat Field Correction

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/colorpalette_howto.html language=enus -->
## TOPIC 00014: How to Use the Color Palette Editor

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/colorpalette_howto.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/colorpalette_howto.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### How to Use the Color Palette Editor

The Color Palette Editor enables you to apply a specified color palette to monochrome images. This can be especially useful with 16-bit grayscale images for medical, scientific, or temperature monitoring applications.

Take the following steps to configure a color palette.

1. In the image acquisition step, click or in the toolbar above the main display window to open the Color Palette Editor . To create a new palette, click . To edit an existing palette, use the pull-down menu next to the new palette button to select a palette, and then click
2. Enter a unique name for the palette in Color Palette Name .
3. Select a default palette to apply to the image using the Start from Palette drop-down menu. Click Apply to apply the palette to the Color Palette Samples table.
4. Use the Interpolation Method pull-down menu to specify the interpolation technique used to color the image. When you select a new Interpolation Method , the Grayscale to Color Mapping Graphs change.
5. Select a sample in the Color Palette Samples table to assign a specific color to a grayscale value. You can also drag the vertical lines in the Grayscale to Color Mapping Graphs to configure grayscale values. Use the Add , Delete , and Sort buttons below the table to add, delete, or reorder samples.
6. Click Preview to view a preview of the configured settings in the main display window.
7. Close the Color Palette Editor by clicking OK or Cancel .
8. To delete a palette, select the pull-down menu next to the new palette button, and click .

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/comm_whento.html language=enus -->
## TOPIC 00015: Communicate Palette

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/comm_whento.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/comm_whento.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Communicate Palette |
| --- | --- |

This palette contains steps related to communication between the inspection application and external devices.

- **Read/Write I/O (Vision RIO)**
  - Reads and writes digital I/O lines and ports on NI PCI-8254R/PCIe-8255R, CVS-145x, IC--312x, and IC 317x devices with reconfigurable I/O.
- **Generate Pulse (Vision RIO)**
  - Generates a single pulse or a pulse train using NI PCI-8254R/PCIe-8255R, CVS-145x, IC--312x, and IC 317x devices with reconfigurable I/O.
- **Read/Write I/O**
  - Reads and writes digital I/O lines on NI Smart Cameras and NI image acquisition devices.
- **Generate Pulse**
  - Generates a single pulse or a pulse train using the digital output lines on NI Smart Cameras and NI image acquisition devices.
- **Read/Write I/O (NI-DAQmx)**
  - Read and writes digital and analog I/O lines or ports on NI data acquisition (DAQ) devices.
- **Serial I/O**
  - Communicates with external devices—such as a PLC or robot—through serial commands. You can export measurements and pass/fail results to external devices. You can also configure your system to wait for a signal from an external device to select or start an inspection.
- **TCP I/O**
  - Communicates with devices through TCP commands. You can export measurements and pass/fail results to external devices.
- **Modbus Slave**
  - Communicates with Modbus Master devices, such as touch screens and other Human Machine Interfaces (HMI) and terminals. Vision Builder AI supports both the serial and TCP/IP physical layers.
- **EtherNet/IP**
  - Communicates with targets that support unconnected messaging using Logix tag names. Valid targets include PLCs, such as the Rockwell ControlLogix series.
- **EtherNet/IP Adapter**
  - Allows Vision Builder AI to function as an adapter-class device and communicate with targets that support connected messaging. Valid targets include PLCs, such as the Rockwell ControlLogix series.
- **OPC UA**
  - Allows Vision Builder AI to communicate with an OPC UA device. Use this step to configure the items that Vision Builder AI reads and writes to a device, as well as the order in which Vision Builder AI communicates these items to a device.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/commdevicesrvr_ethernetip.html language=enus -->
## TOPIC 00016: Configuring an Ethernet/IP Server

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/commdevicesrvr_ethernetip.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/commdevicesrvr_ethernetip.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuring an Ethernet/IP Server

The following controls are available in the **Ethernet/IP Assembly Configuration** dialog box:

|  | Tip Right-click in the Registers table and select Open All Items or Close All Items to expand or collapse the tree. |
| --- | --- |

| Control Name | Description |
| --- | --- |
| Assembly Instance | Specifies the instance ID of the assembly on the following channels: Input—Corresponds to the input assembly of the PLC. Output—Corresponds to the output (producing) assembly of the PLC. |
| Size | Specifies the size of the assembly on the following channels: Input—Corresponds to the input assembly size of the PLC. Output—Corresponds to the output assembly size of the PLC. |
| Registers | Adds, deletes, reorders, and/or configures input and output register assemblies. Input Registers—Select to add a new input register. Configure the register with the Selected Register Settings below. Select a register in the tree to enable the , , and controls to delete and/or reorder registers. Output Registers—Select to add a new output register. Configure the register with the Selected Register Settings below. Select a register in the tree to enable the , , and controls to delete and/or reorder registers. Tip Click to reset all input and output registers to their default assemblies. |
|  | Tip Click to reset all input and output registers to their default assemblies. |
| Selected Register Settings | Configures the settings of the register selected in the tree above. Register Name—Specifies the name of the input or output register. Data Type—Selects the data type of the input or output register. If you create a BOOL input register, the Bind to System Signal drop-down menu allows you to use system signals to dynamically update the Boolean register. Note Booleans that are bound to system signals are not writable in the Ethernet/IP Adapter step. Array Size—Specifies the array size of the input or output register. This parameter is available only for the parent register item. Description—Enter a description for the input or output register. |
|  | Note Booleans that are bound to system signals are not writable in the Ethernet/IP Adapter step. |
| Export | Exports the configured registers as an .ini file. |
| Import | Imports a selected .ini file to configure the registers. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/commdevicesrvr_modbus.html language=enus -->
## TOPIC 00017: Configuring a Modbus Server

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/commdevicesrvr_modbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/commdevicesrvr_modbus.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuring a Modbus Server

The following controls are available in the **Modbus Server Configuration** dialog box:

| Control Name | Description |
| --- | --- |
| Enable Modbus Serial Server | Select to configure Modbus Serial Server settings. |
| COM Port | Serial communication port used for communication with the Modbus device. |
| Timeout (ms) | Specifies the period of time Vision Builder AI waits to receive a Modbus command before timing out. |
| Mode | Specifies the mode used to transmit Modbus serial commands. The following options are available: RTU—Transmits data using the Modbus RTU compact binary format. ASCII—Transmits data using a human-readable ASCII format |
| Modbus Address | Specifies the Modbus address on which Vision Builder AI receives communication. |
| Enable Modbus TCP Server | Select to configure Modbus TCP Server settings. |
| Timeout (ms) | Specifies the period of time Vision Builder AI waits to receive a Modbus command before timing out. |
| TCP Port | Indicates the TCP port on which Vision Builder AI receives communication from a Modbus device. Note The Modbus TCP standard defines port 502 as the default port to use for Modbus TCP communication. |
|  | Note The Modbus TCP standard defines port 502 as the default port to use for Modbus TCP communication. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/commdevicesrvr_opcua.html language=enus -->
## TOPIC 00018: Configuring an OPC UA Server

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/commdevicesrvr_opcua.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/commdevicesrvr_opcua.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuring an OPC UA Server

The following controls are available in the **OPC UA Server Configuration** dialog box:

| Control Name | Description |
| --- | --- |
| TCP Port | Specifies the port number to listen for a connection. |
| Server Certificate Path | Displays the file path to the server certificate (.der ). If you specify a Security Policy other than None Required on the Security tab, you must take the following actions: Copy the server certificate indicated in the Server Certificate Path to the client device Note If you configure a real-time target, the Server Certificate Path indicates a path on the target. National Instruments recommends using WebDAV to transfer files to and from a remote target. Configure the client device to use the server certificate and connect to the Vision Builder AI OPC UA server. Note Consult the client device documentation for specific instructions to configure the client device to use the server certificate and connect to the server. Copy the client certificate to the Vision Builder AI server host. Note Third party OPC UA software generates the client certificate. Add the client certificate to the list of Trusted Client Certificate Paths in Vision Builder AI. |
|  | Note If you configure a real-time target, the Server Certificate Path indicates a path on the target. National Instruments recommends using WebDAV to transfer files to and from a remote target. |
|  | Note Consult the client device documentation for specific instructions to configure the client device to use the server certificate and connect to the server. |
|  | Note Third party OPC UA software generates the client certificate. |

#### Items

The following controls are available under the **Items** tab of the OPC UA Server Configuration dialog box.

| Control Name | Description |
| --- | --- |
| OPC UA Server Items | Displays a data tree of items, folders, and properties. Click an item to configure the Selected Tree Item Settings. Right click to add items to the tree. Right click a folder to Add Folder, Add Item, or Delete the folder and all its contents. Right click an item to Add Property, or Delete the item and all its properties. Right click a property to Delete the property. Note A property and an item differ only in how they are organized in the item tree. |
|  | Note A property and an item differ only in how they are organized in the item tree. |
| Selected Tree Item Settings | Configures the following settings based on the selected tree item: Folder – Folder Name—Enter the name of the folder. Item – Item Name—Enter the name of the item. – Data Type—Specify the data type. – Access Level—Specify Read only, Write only, or Read/Write. – Description—Enter a description of the item. Property – Property Name—Specify the name of the property. – Data Type—Specify the data type. – Access Level—Specify Read only, Write only, or Read/Write. – Description—Enter a description of the property. |
| Import | Opens a dialog box to define a file path to read the server configuration. |
| Export | Opens a dialog box to define a file path to save the server configuration. |

#### Security

The following controls are available under the **Security** tab of the OPC UA Server Configuration dialog box.

| Control Name | Description |
| --- | --- |
| Security Policy | Specifies which security policies Vision Builder AI OPC UA Server accepts: None Required Sign with Basic128Rsa125 Sign and Encrypt with Basic128Rsa125 Sign with Basic256 Sign and Encrypt with Basic256 You must have an OPC UA client certificate to select a security policy other than None Required. Take the following actions to obtain an OPC UA client certificate: Copy the server certificate indicated by the Server Certificate Path to the client device. Copy the client certificate from the client device to the device where the Vision Builder AI OPC UA server runs. Note If the Vision Builder AI OPC UA server runs on a real-time target, copy the client certificate to the target. National Instruments recommends using WebDAV to transfer files to and from a remote target. After you copy the client certificate to the device where the Vision Builder AI OPC UA server runs, select a Security Policy other than None Required and use the dialog box that appears to browse to the client certificate. |
|  | Note If the Vision Builder AI OPC UA server runs on a real-time target, copy the client certificate to the target. National Instruments recommends using WebDAV to transfer files to and from a remote target. |
| Trusted Client Certificate Paths | Displays a list of client certificate file paths that Vision Builder AI accepts. The Vision Builder AI OPC UA server accepts client certificates generated by third party OPC UA software. To connect a client device to the Vision Builder OPC UA server, you must copy the client certificate to the device where the Vision Builder OPC UA server runs. Then, you can select a Security Policy other than None Required and use the dialog box that appears to browse to the client certificate. |
| Add | Opens a dialog box to define a client certificate file path. |
| Delete | Removes a client certificate file path. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/commdevicesrvr_tcp.html language=enus -->
## TOPIC 00019: Configuring a TCP Server

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/commdevicesrvr_tcp.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/commdevicesrvr_tcp.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuring a TCP Server

The following controls are available in the **TCP/IP Server Configuration** dialog box:

| Control Name | Description |
| --- | --- |
| TCP Port | Specifies the TCP port on which Vision Builder AI receives communication. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/commdevicesrvr_tools.html language=enus -->
## TOPIC 00020: Configuring Vision Builder AI Servers

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/commdevicesrvr_tools.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/commdevicesrvr_tools.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuring Vision Builder AI Servers

Select **Tools»Communication Device Manager**, then click **Configure** to launch a server configuration dialog box. The server configuration settings vary based on which server you configure. Vision Builder AI supports the following servers:

- Modbus Server
- TCP Server
- Ethernet/IP Server
- OPC UA Server
- Profinet Server

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/config_runmodes.html language=enus -->
## TOPIC 00021: Running an Inspection

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/config_runmodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/config_runmodes.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Running an Inspection

Use the **Operate** menu options or the buttons on the Vision Builder AI toolbar to run an inspection from the Configuration Interface. The following options are available:

| Icon | Run Mode | Description |
| --- | --- | --- |
|  | Run Inspection Once | Runs the inspection through one iteration of the state diagram. |
|  | Run Inspection in Loop | Runs the inspection continuously. |
|  | Run Inspection Until Failure | Runs the inspection until the Inspection Status variable has a value of FAIL. |
|  | Run Inspection Fast | Runs the inspection as quickly as possible with minimum updates. This mode opens the Inspection Interface since the main display window does not update. |
| — | Run Inspection Multiple Times | Runs the inspection a specified number of times. This option is available only from the Operate menu. |
|  | Stop Inspection | Stops the inspection. |
|  | Highlight Execution | Highlights the inspection execution when you run an inspection. If the Highlight Execution button appears framed, execution highlighting is enabled. |
|  | Pause | Pauses or resumes execution of the inspection. If the Pause button appears framed, execution is paused. |
|  | Step Into | Advance one step in the inspection. Single Step is only available when the Pause button is pressed. |
|  | Step Over | Advance to the final step in an inspection state. Step Over is only available when the Pause button is pressed. |

#### Selecting the Next Inspection Image

Use the Select Next Inspection Image buttons on the Configuration Interface toolbar to specify which image to process during the next iteration of an inspection. The Select Next Inspection Image buttons apply only to inspections that either contain a **Read Image File** step, or are using a simulated target and have an acquisition step****. The following options are available:

| Icon | Next Inspection Image | Description |
| --- | --- | --- |
|  | Use Previous Image | Uses the previous inspection image the next time the inspection executes. |
|  | Use Current Image | Uses the current inspection image the next time the inspection executes. |
|  | Use Next Image | Uses the next inspection image the next time the inspection executes. |
|  | Select Next Image | Specifies the inspection image to process the next time the inspection executes. |

#### Running a Single Inspection State

You can run only the steps in the currently selected state of an inspection by clicking the buttons on the [State Configuration window](ui_config.html) toolbar. The following options are available:

| Icon | Run State Mode | Description |
| --- | --- | --- |
|  | Run State Once | Runs the currently selected state once. |
|  | Run State in Loop | Run the currently selected state in a continuous loop. |
|  | Stop | Stops the execution of a state running in a loop. |
|  | Step Backward | Executes the previous step in the currently selected state using the current image. |
|  | Step Forward | Executes the next step in the currently selected state using the current image. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/configrt_howto.html language=enus -->
## TOPIC 00022: NI Vision Builder AI Remote Target Configuration

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/configrt_howto.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/configrt_howto.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### How to Configure NI Vision Builder AI Remote Targets

NI Vision Builder AI remote targets are field programmable devices that you add to a subnet and
run remotely. You configure a remote target from a host machine on the same subnet, defining settings such as the target name and description, network settings, and software revisions. Complete
the steps in the following sections to configure a Vision Builder AI remote target.

1. Click Start»All Programs»National Instruments»Vision Builder AI .
2. On the Vision Builder AI welcome screen, select the remote target that you want to configure from the list of targets.

 [IMAGE alt='Tip' src='tip.gif']
 **Tip** If the remote target that you want to configure is on a different subnet than the development computer, it may not appear in the list of available targets. Click **Add Target**, enter the IP address of the remote target you want to configure, and click **OK** to add the target to the table.
3. Vision Builder AI automatically checks the state of the target and displays configuration options, if necessary.
 
 [IMAGE alt='Tip' src='tip.gif']
 **Tip** If you want to configure a remote target but are not prompted, right-click the target and select **Configure**.

#### Configuring a Remote Target

Complete the following instructions to configure a remote target.

1. If prompted, click Configure Target .
2. If the remote target is password-protected, Vision Builder AI prompts you to enter the administrator password.
3. Enter a Name and Description for the remote target, and click Next .
 Device names are limited to 31 characters with no spaces or special characters, except hyphens. The first and last characters must be alphanumeric.
4. Select an IP address.
 If your remote target is on a network that has a DHCP server, you may be able to automatically obtain an 
IP address from the DHCP server. A DHCP server allocates an IP address to the remote target each time the target is restarted. If you select the DHCP Server option, you do not need to specify other information, such as the **Subnet Mask**. If you do not know if the network has a DHCP server, check with a network administrator for assistance. 

 To automatically obtain an IP address, select **Obtain IP address from DHCP Server**. 

 To assign a static IP address to the remote target, select **Edit the IP Settings** and enter the following information:
  - IP Address
  - Subnet Mask
  - Gateway
  - DNS Server 

 [IMAGE alt='image' src='note.gif']
**Note** Consult a network administrator before modifying these parameters. 

 If you want to set the IP address without a DHCP server but are uncertain about the settings, click **Suggest Values**. Vision Builder AI attempts to detect the appropriate settings. Click **Reset to Default** to revert to the original settings.
5. Click Next .

#### Installing Software to a Remote Target

Complete the following instructions to install software to a remote target.

1. If prompted, click Install Software .
2. Enable the Update Target Software checkbox. 

 [IMAGE alt='Caution' src='note.gif']
 **Note** 
 Vision Builder AI automatically selects the appropriate software image for the selected remote target. If you want to select
 a different software image, click the [IMAGE alt='image' src='browse.gif'] **Browse** button and navigate to the software image that you want to use.
3. To remove any existing software, inspections, images, and log files currently on the remote target before installing the new software, enable the Format Target Before Installing Software control.
 
 [IMAGE alt='Caution' src='caution.gif']
 **Caution** Formatting removes all data stored on the remote target. Backup any important data from the remote target before enabling the **Format Target Before Installing Software** control.
4. Click OK to install the software on the remote target.

##### Using the File System on Real-Time Targets

|  | Note You must use WebDAV to transfer files to and from a real-time target. |
| --- | --- |

The file system of NI Linux Real-Time targets follows conventions established for UNIX-style operating systems. Other LabVIEW RT targets follow Microsoft Windows-style conventions. The following table provides Vision Builder AI file path references on Real-Time targets:

|  | CVS-1458/1459, IC-312x, IC-317x |  |
| --- | --- | --- |
| User VIs | /home/lvuser/natinst/vbai/User VIs |  |
| User Images | /home/lvuser/natinst/vbai/User Images |  |

#### Setting a Password on a Remote Target

1. Open a Web browser and enter http://<Target IP Address> in the Web browser address bar to open the Web Configuration window for your target.
2. Click the Security Configuration icon on the left. The Security Configuration window appears.
3. Click Login at the top right.
4. Enter admin as the user name, leave the password field blank, and click OK .
5. Click Change Password .
6. Enter and re-enter the new password, click OK , then click Save . A message appears warning that the password is changing and you must login again. Click OK .

 [IMAGE alt='Note' src='note.gif']
**Note** If you forget the system password, you must use the information in the [Technical Support and Professional Services](technical_support_resources.html) section to contact NI and reformat the target. NI cannot recover lost system passwords.

#### Review Execution Target Information

To review the properties of an execution target to ensure that it is the remote target you want to connect to or to determine if it is configured correctly, click **Properties** and review the identification information, network settings, and installed software for the remote target.

#### Backup Execution Target Information

Vision Builder AI allows you to create a target image of a remote target. Target images contain all of the current configuration settings for a remote target and all of the inspections currently installed to the remote target. Target images are useful to backup configuration settings or to deploy the same configuration settings to multiple remote targets. Complete one of the following sets of steps to create an image of a remote target:

- If you are currently connected to a remote target —Select Target»Create Target Image to launch the Create Target Image dialog box. Enter information about the inspection and the location where you want to save the image, and click OK .
- If you are not currently connected to a remote target —On the Vision Builder AI Welcome screen, select Select Network Target from the Execution Target list. In the Select Remote Target dialog box, right-click the target for which you want to create an image. Enter information about the inspection and the location where you want to save the image, and click OK .

 [IMAGE alt='Note' src='note.gif']
**Note** You must restart the target to create an image.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/formula_node_howto.html language=enus -->
## TOPIC 00023: How to Use Formula Nodes

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/formula_node_howto.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/formula_node_howto.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### How to Use Formula Nodes

The Formula Node is a convenient, text-based node that you can use to perform mathematical operations. In addition to text-based equation expressions, the Formula Node can accept text-based versions of if statements, [switch statements](#switch), [while loops](#while), [for loops](#for), and [do loops](#do). These programming elements are similar to those found in C programming, but are not identical.

Formula Nodes are useful for complicated equations, equations that have many variables, and for using existing text-based code rather than recreating it graphically.

#### Creating a Formula Node

Complete the following steps to create a Formula Node:

1. From the Functions palette, open the Numeric functions subpalette. If the Functions palette is not visible, click Show Functions Palette on the Main tab of the Calculator step.
2. Select the Formula Node structure.
3. Click the location where you want to place the Formula Node on the Calculation diagram. Drag the structure to the desired size and click the Calculation diagram.
4. Review Formula Node syntax , functions , and operator precedence .
5. Enter the equations that you want to calculate inside the Formula Node. Each assignment must have only a single variable on the left side of the assignment ( = ). Each assignment must end with a semicolon ( ; ).

|  | Tip If a syntax error occurs, click the broken Run button to display the Error list dialog box. |
| --- | --- |

1. Add input and output terminals to the Formula Node. Variable terminals are case sensitive. There is no limit to the number of terminals or equations in a Formula Node.
  1. Create an input terminal for each input variable by right-clicking the Formula Node border and selecting Add Input from the shortcut menu. Type the variable name in the terminal that appears. You can edit the variable name at any time.
  2. Create an output terminal for each output variable by right-clicking the Formula Node border and selecting Add Output from the shortcut menu. Output variables have thicker borders than input variables.

|  | Note No two inputs and no two outputs can have the same name. However, an output can have the same name as an input. |
| --- | --- |

1. (Optional) The default data type for output terminals is double-precision, floating-point. To change the data type, create an input terminal with exactly the same name as the output terminal and wire a data type to that input terminal. Doing so also provides a default value for the terminal. You also can use the Formula Node syntax to define the variable inside the Formula Node. For example, int32 y; changes the data type of the output terminal y to 32-bit integer.
2. Wire the input and output terminals of the Formula Node to their corresponding terminals on the Calculation diagram. All input terminals must be wired. Output terminals do not have to be wired.

#### Using the Formula Node

This section contains examples for working with text-based structures inside a Formula Node. This section contains the following subsections:

- Performing Do Loops
- Performing For Loops
- Performing Switch Statements
- Performing While Loops
- Working with Variables

##### Performing Do Loops

The do statement uses the same syntax as the do statement in C. For example, you might have a statement like:

do {

int32 temp;

temp = --a[2]+y;

y=y-1;

}

while (y!=x && a[2]>=a[0]);

##### Performing For Loops

The for statement uses the same syntax as the for statement in C. For example, you might have a statement like:

for (y=5; y<x; y*=2) {

int32 temp;

temp = --a[2]+y;

x-=temp;

}

##### Performing Switch Statements in Formula Nodes

The switch statement uses the same syntax as the switch statement in C. For example, you might have a statement like:

switch(month){

case 2: days = evenyear? 29: 28; break;

case 4:case 6:case9: days = 30; break;

default: days = 31; break;

}

##### Performing While Loops Using Formula Nodes

The while statement uses the same syntax as the while statement in C. For example, you might have a statement like:

while (y!=x && a[2]>=a[0]) {

int32 temp;

temp = --a[2]+y;

y=y-1;

}

##### Working with Variables

When you work with variables, remember the following points:

- There is no limit to the number of variables or equations in a Formula Node.
- No two inputs and no two outputs can have the same name, but an output can have the same name as an input.
- Declare an input variable by right-clicking the Formula Node border and selecting Add Input from the shortcut menu. You cannot declare input variables inside the Formula Node.
- Declare an output variable by right-clicking the Formula Node border and selecting Add Output from the shortcut menu. The output variable name must match either an input variable name or the name of a variable you declare inside the Formula Node.
- You can change whether a variable is an input or an output by right-clicking it and selecting Change to Input or Change to Output from the shortcut menu.
- You can declare and use a variable inside the Formula Node without relating it to an input or output wire.
- You must wire all input terminals.
- Variables can be floating-point numeric scalars, whose precision depends on the configuration of your computer. You also can use integers and arrays of numeric values for variables.
- Variables cannot have units.

###### Scope Rules for Declaring Variables

Formula Nodes use the same scope rules for declaring variables as C.

- All variables you declare in bracketed blocks are only accessible within the bracketed block.
- All input terminals are considered variables at the outermost block (not enclosed in brackets), and cannot be declared again in the outermost block.
- Vision Builder AI tries to match variables you declare at the outermost block (not enclosed in brackets) to output terminals with the same name.
- You can declare output terminals that have no corresponding input terminal and are not declared at the outermost block.

Use the correct [Formula Node syntax](formula_node_syntax.html) when declaring variables.

Related links

Formula Node Syntax

Functions in Formula Nodes and Expression Nodes

Operator Precedence in Formula Nodes and Expression Nodes

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/scrollbarcontrols.html language=enus -->
## TOPIC 00024: Scrollbar Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/scrollbarcontrols.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/scrollbarcontrols.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Scrollbar Controls

- Click or drag the square scroll box to a new position.
- Click the increment or decrement arrow buttons.
- Click the spaces between the scroll box and the arrows.

Parent topic:

Numeric Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/segmentcolorimageconcepts.html language=enus -->
## TOPIC 00025: Segment Color Image Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/segmentcolorimageconcepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/segmentcolorimageconcepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Segment Color Image Concepts |
| --- | --- |

Segment Color Image

Parent topic:

Enhance Images Palette

Related example inspections

- Segment Color Image Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/segmentcolorimagecontrols.html language=enus -->
## TOPIC 00026: Segment Color Image Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/segmentcolorimagecontrols.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/segmentcolorimagecontrols.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Segment Color Image Controls |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_rgbu32.gif'] [IMAGE alt='image' src='vision_hslu32.gif']

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Region of Interest**
  - Specifies the region of the image to process.
- **Reposition Region of Interest**
  - Repositions the region of interest dynamically based on a coordinate system from a previous Set Coordinate System step. Link the region of interest to a coordinate system if the position of the object under inspection changes from image to image, and you need to adjust the position of the region of interest to match the new location of the object.
- **Reference Coordinate System**
  - Specifies the coordinate system to which you want to link the region of interest.
- **Classifier File Path**
  - Specifies the path to the classifier file you want to use to classify samples. A classifier file contains a label and unique representation for each trained sample.
- **New/Edit Classifier File**
  - Launches the NI Color Classification Training Interface. Use the training interface to create a new classifier file.
- **Samples**
  - Indicates the number of learned samples in the selected classifier file.
- **Color Palette**
  - Enables the user to add a color palette to monochrome images. Refer to Color Palette editor for more details.

#### Settings Tab

- **Window Size**
  - Specifies the size of the window around each pixel used to calculate the class of the pixel. The window size must be large enough to include a representative sample of the color that you want to isolate with the threshold.
- **ROI Size**
  - Indicates the size of the current region of interest. Tip ROI Size displays the size of the last ROI drawn. Click to apply the ROI Size to the Window Size.
- **Step Size**
  - Specifies the offset, in pixels, by which the step should reposition the window used to process the image. A higher value decreases the time required to process the image, but also decreases segmentation accuracy.
- **Refine Segmentation**
  - Processes the boundary pixels of each segmentation cluster using a step size of 1. Enabling Refine Segmentation increases the time required to process the image, but also increases segmentation accuracy.
- **Auto-Calculate Maximum Distance**
  - Automatically calculates the Maximum Distance value based on the selected classifier file.
- **Maximum Distance**
  - Specifies the maximum distance allowed between the color feature of a pixel and the class to which it belongs.
- **Minimum Particle Area**
  - Specifies the minimum required area for a segment cluster. A segmented cluster with an area smaller than this value is assigned the pixel value for unassigned pixels.
- **Maximum Particle Area**
  - Specifies the maximum allowed area for a segment cluster. A segmented cluster with an area larger than this value is assigned the pixel value for unassigned pixels.
- **Minimum Identification Score**
  - Specifies the minimum identification score that a pixel must have in order to be considered part of a class. Pixels with an identification score lower than this value are assigned the pixel value for unassigned pixels. The identification score indicates the degree of similarity between a pixel and samples in the class. Values range from 0 (no match) to 1000 (perfect match).
- **Display Options**
  - Controls how the color segmentation result is displayed. Show Segmented Image—Displays the segmented image returned by the color segmentation algorithm. Overlay Classes on Image—Overlays the segmentation outline on the image, along with the class labels for the identified colors. Note The output image of the step is always a segmented image.
- **Elapsed Time**
  - Indicates the amount of time the step took to segment the image on the development computer. To determine inspection benchmarks for a remote target, select Operate»Benchmark Inspection.

#### Pixel Mapping Tab

- **Select a pixel value for each color class**
  - Specifies a grayscale pixel value to represent a corresponding color class in the segmented image. You can specify different pixel values for each class, or the same pixel value for multiple classes. The step processes all segments with the same pixel value as a single color class.
- **Reset Values**
  - Assigns values to each color class in ascending order. The assigned values are equally spaced values within a range of 0 to 254.
- **Display Options**
  - Controls how the image is displayed after segmentation. Show Segmented Image—Displays the segmented image returned by the color segmentation algorithm. Overlay Classes on Image—Overlays the segmentation outline on the image, along with the class labels for the identified colors. Note The output image of the step is always a segmented image.

#### Limits Tab

- **Pass Inspection If**
  - Specifies a minimum and maximum value for each result. Each selected result must be within the specified range in order for the step to pass.
- **Sort Results By**
  - Specifies the measurement result that you want to use to sort the results displayed in the results table. Label—Sorts color segmentations by assigned class label. Percentage—Sorts color segmentations by the percentage of the ROI filled by the segmentation. Area—Sorts color segmentations by area.
- **Sort Order**
  - Specifies how the results are sorted. Ascending—Displays results from the lowest value to the highest value. Descending—Displays results from the highest value to the lowest value.
- **Color Segmentation Results**
  - Displays information about each color segmentation.

Parent topic:

Enhance Images Palette

Related example inspections

- Segment Color Image Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/segmentcolorimagefaqs.html language=enus -->
## TOPIC 00027: Segment Color Image FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/segmentcolorimagefaqs.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/segmentcolorimagefaqs.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Segment Color Image FAQs |
| --- | --- |

Q: The step does not properly segment the colors in the region of interest. How can I improve color segmentation?

You must select a color classifier file that describes the colors that you want to segment. Click Edit 
 Classifier File to launch the NI Color Classification Training Interface. If the color classifier file does not describe the colors that you want to segment, train 
 additional colors. If the color classifier file describes the colors that you want to segment, add additional color samples to the color classifier or click the Options 
 tab and select High in the Sensitivity List.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/selectinspection_controls.html language=enus -->
## TOPIC 00028: Select Inspection Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/selectinspection_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/selectinspection_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Select Inspection Controls |
| --- | --- |

- **Inspection Path/Name Value**
  - The step selects an inspection based on a previous result that contains a valid filepath to an inspection. If Vision Builder AI is running on a remote target, the previous result must contain only the inspection name.
- **Inspection Table Value**
  - The step selects an inspection based on a previous result value that corresponds to a Value listed in the Inspection Table. The previous result must contain a string or numeric value.
- **Inspection Table**
  - Lists the inspections corresponding with each value. Use—Specifies that the value should be used for inspection selection. Value—Displays the value that triggers Vision Builder AI to switch the active inspection. Inspection—Displays the name of the inspection to run for the specified value.
- **Value**
  - Specifies the value that triggers Vision Builder AI to switch the active inspection.
- **Normal Display**
  - Specifies that the selected string value displays each character as plain text.
- **Codes Display**
  - Specifies that the selected string value displays non-printable characters with a backslash (\\) before the character.
- **HEX Display**
  - Specifies that the selected string value displays each character as a hexadecimal value.
- **Inspection**
  - File path of the inspection to run for the specified value.
- **Add**
  - Adds a new value to the Inspections table.
- **Delete**
  - Removes the currently selected value from the Inspections table.
- **Sort**
  - Sorts the values in the Inspections table.
- **Enable Inspection Selection**
  - Enables inspection selection when an inspection runs in the Inspection Interface.

Parent topic:

Use Additional Tools Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/selectinspection_faq.html language=enus -->
## TOPIC 00029: Select Inspection FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/selectinspection_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/selectinspection_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Select Inspection FAQs |
| --- | --- |

Q: What values can I use to select an inspection?

You must specify a string or numeric value to select an inspection. 
A string value can specify the path or name of an inspection, or you can use a string or numeric value to 
select an inspection based on a value listed in the **Inspection Table**. 
You can select an inspection based on the value of a User-Defined System variable, Network variable, 
or result from a previous step in the **Select Inspection** state.

Parent topic:

Use Additional Tools Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialio_controls.html language=enus -->
## TOPIC 00030: Serial I/O Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialio_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialio_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Serial I/O Controls |
| --- | --- |

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Command List**
  - Lists the commands to send or receive through serial communication. Port—Specifies the name of the serial port to which an external device is connected. This name corresponds to the Ports (Serial & Parallel) names defined in the Devices and Interfaces list in Measurement & Automation Explorer (MAX). Direction—Specifies whether the command is sent or received. Command—Specifies the command to send or receive. Comment—Specifies additional information about the command. TipRight-click a command and select Move Up or Move Down to change the order of commands in the list.
- **Send Command**
  - Launches a dialog box that allows you to configure and send a command.
- **Wait for String**
  - Launches a dialog box that allows you to configure your system to wait for an incoming command.
- **Flush Port**
  - Launches a dialog box that allows you to configure your system to clear the serial communication line.
- **Wait**
  - Launches a dialog box that allows you to configure your system to wait before sending or receiving additional commands.
- **Edit**
  - Launches a dialog box that allows you to edit the selected command.
- **Delete**
  - Deletes the selected command.
- **Delete All**
  - Deletes all commands in the Command List.
- **Test**
  - Executes all commands in the Command List.
- **Show Terminal**
  - Launches a Communication Terminal that lists all of the terminals and displays the commands that are sent and received.
- **Step fails in case of error or timeout**
  - Sets the step status to FAIL when there is an error or timeout during communication.

Parent topic:

Communicate Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialio_faq.html language=enus -->
## TOPIC 00031: Serial I/O FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialio_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialio_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Serial I/O FAQs |
| --- | --- |

Q: Why does the step say "Operation Skipped"?

The step only performs the serial operations when the inspection is running. When connected to a target, use the Run State button at the top to perform the serial operations. When not connected to a target, the Run State button will also perform the serial operations specified by this step. This avoids inadvertently interacting with hardware while selecting steps.

Q: Why is my device not responding to serial commands?

1. Launch MAX.
2. Expand Devices and Interfaces .
3. Expand Ports (Serial & Parallel) .
4. Right-click your serial port name in the configuration tree to configure your port.

Target»

Target Options

Serial Port

[IMAGE alt='Note' src='note.gif']

Note

Check your device manual for the type of serial cable you need to 
 communicate with the device. Some devices require straight-through cables while others require crossover cables.

Make sure you select the serial port connected to your device 
 when sending and receiving commands.

Q: How do I send a serial command based on the result of an inspection?

Add a Set Inspection Status at the end of the inspection diagram
 and select Set to FAIL if any previous step fails. Add a second Serial I/O step after the 
 Set Inspection Status step to send a serial command based on the Inspection Status system variable.

Q: How do I change my remote target serial port configuration?

Navigate to 
 Target»Target Options»Serial Port.

Q: The Target Options for my real-time target report the Serial Interface is RS485, but my device uses RS232. How do I change the Serial Interface to match my device?

Follow the below steps to change the serial interface for a real-time target:

1. Connect a keyboard and monitor to the target and then reboot the target.

2. While the target is booting, press F10 to enter the BIOS.

3. Select **Enter Setup** using the up/down arrows on the keyboard and press Enter.

4. Use the right arrow key to select the **Advanced** tab and then use the down arrow key to select the **Serial Port Configuration** and press Enter.

5. Press Enter to open the Serial Interface selection and select the desired interface. Press Enter to exit the selection dialog.

6. Press F10 to save and exit.

7. Select Yes to save the configuration. When the target reboots, it will now be using the new serial interface.

Parent topic:

Communicate Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialiocommterm_tools.html language=enus -->
## TOPIC 00032: Serial Communication Terminal

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialiocommterm_tools.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialiocommterm_tools.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Serial Communication Terminal

Use the Serial Communication Terminal to debug the serial communications in your inspection.

#### How to Use

1. On the Serial I/O property page, click Show Terminal to launch the Serial Communication Terminal.
2. On the Serial I/O property page, click Test . Notice that the Serial Communication Terminal shows the commands being sent and received on the serial ports.

 [IMAGE alt='image' src='tip.gif']
**Tip** You can resize the Serial Communication Terminal and the widths of the table columns if you cannot see all of the information in the table.
3. In the Serial Communication Terminal, select the type of display you want from the View menu.


 You can perform the following tasks from the Serial Communication Terminal:
  - Select File»Save As to save the contents of the table to a text file.
  - Select Edit»Clear to clear the table of serial commands.
  - Select Edit»Log History to modify the number of records shown in the table. By default, the Serial Communication Terminal logs 1024 entries. The oldest entries above 1024 are erased as new commands are logged.

1. Select File»Close to close the Serial Terminal window.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialioflushport_dialog.html language=enus -->
## TOPIC 00033: Flush Serial Port

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialioflushport_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialioflushport_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Flush Serial Port

Use this dialog box to clean data out of a serial communication line before you send or receive new commands.

#### How to Use

1. Select the serial port whose line you want to clear from the Flush Port drop-down list.
2. Type a comment about your reason for flushing the line.

#### Control Descriptions

The following controls area available on the Flush Serial Port dialog box.

| Control Name | Description |
| --- | --- |
| Flush Port | Name of the serial port whose line you want to clear. |
| Comment | Comment about clearing the line. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialioinsertresult_dialog.html language=enus -->
## TOPIC 00034: Insert Result (Serial)

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialioinsertresult_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialioinsertresult_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Insert Result (Serial)

Use this dialog box to insert the result of a previous inspection step in the command you want to send.

#### How to Use

1. Select the result to send from the Measurements list.
2. Select the data format of the result to send. If you select String , set the available String Format options.
3. Select the display type to verify what you want to see displayed.

#### Control Descriptions

The following controls are found on the Insert Result dialog box.

| Control Name | Description |
| --- | --- |
| Measurements | Displays a list of step results and variables you can send. |
| Data Format | Data format of the step result to send. The following options are available: String. I8—Signed 8-bit integer. U8—Unsigned 8-bit integer. I16—Signed 16-bit integer. U16—Unsigned 16-bit integer. I32—Signed 32-bit integer. U32—Unsigned 32-bit integer. Single (4 bytes)—Single-precision floating-point number with 32-bit IEEE single-precision format. Double (8 bytes)—Double-precision floating-point number with 64-bit IEEE single-precision format. Extended (16 bytes)—Extended-precision number with 128-bit format. |
| String Format | Numbering system you want to use when expressing your serial command. The options are available: Decimal—Base 10 numbering system in which each digit can be 0–9. Hexadecimal—Base 16 numbering system in which each digit can be 0–F. Octal—Base 8 numbering system in which each digit can be 0–7. Fractional—Fractional notation, such as 4.91. |
| Width | Width of the string. |
| Precision | Number of digits after the decimal point. |
| True String | String to send when the Boolean result is True. |
| False String | String to send when the Boolean result is False. |
| Display Types | Specifies the format to use to display the string. |
| String | Previews the string to send. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialiosendcom_dialog.html language=enus -->
## TOPIC 00035: Send Serial Command

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialiosendcom_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialiosendcom_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Send Serial Command

Use this dialog box to configure your system to send a command through serial communication lines.

#### How to Use

1. Select the port on whose line you want to send a command from the Port drop-down list.
2. Type the command you want to send.
3. Click Insert HEX to insert the hexadecimal characters you want to include in the command.
4. Click Insert Result to insert the result of a previous inspection step or value of a variable in the command to send.
5. Select the display type.
6. Select the termination character you want to signal the end of the command from the Termination Character drop-down list.
7. Type a comment about the command you want to send.

#### Control Descriptions

The following controls are found on the Send Serial Command dialog box.

| Control Name | Description |
| --- | --- |
| Port | Name of the serial port on whose line you want to send a command. |
| Command | Command you want to send. |
| Insert HEX | Launches a dialog box in which you enter the hexadecimal characters you want to insert in the command. |
| Insert Result | Launches a dialog box in which you select the result of a previous inspection step or variable. |
| Display Types | Specifies the format to use to display the command. |
| Termination Character | Character that indicates the end of a command. The following options are available: None—No termination character NULL (\\00)—Null character CR (\\0D)—Carriage return LF (\\0A)—Line feed CR/LF (\\0D\\0A)—Carriage return/line feed User Defined—Enables the User-Defined Terminal Character control so that you can specify a custom termination character. |
| User-Defined Termination Character | Allows you to specify a termination character. Select User Defined from the Termination Character list to enable this control. |
| Comment | Comment about the command you want to send. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialiowait_dialog.html language=enus -->
## TOPIC 00036: Wait (Serial)

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialiowait_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialiowait_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Wait (Serial)

Use this dialog box to configure your system to wait before sending or receiving commands.

#### How to Use

1. Type the number of milliseconds to wait.
2. Type a comment about your reason for waiting.

#### Control Descriptions

The following controls are found on the Wait dialog box.

| Control Name | Description |
| --- | --- |
| Wait For | Number of milliseconds to wait. |
| Comment | Comment about your reason for waiting. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/serialiowaitstring_dialog.html language=enus -->
## TOPIC 00037: Wait for String (Serial)

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/serialiowaitstring_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/serialiowaitstring_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Wait for String (Serial)

Use this dialog box to configure your system to wait for an incoming command.

#### How to Use

1. Select the port on whose line you want to receive a command from the Port drop-down list.
2. Select whether you want to wait for a fixed number of bytes or a termination character.
3. If you selected Termination Character , select the character you want to signal the end of the command from the drop-down list. Enable the Add Termination Character to Result String to add the selected Termination Character to the string result.
4. Type the number of milliseconds to wait for the command before timing out.
5. Select the Pass condition for the step. If you want the inspection to pass only when a specific string is received, select String received before timeout matches , and enter the expected string. Also, enable the Step fails in case of error or timeout control located on the property page of the Serial I/O step.

 [IMAGE alt='image' src='tip.gif']
**Tip** You can use the following wildcard characters in the expected string: 
 


CharacterDescription
%dmatch decimal integer
%omatch octal integer
%xmatch hexadecimal integer
%bmatch binary integer
%ematch scientific real number
%fmatch floating-point real number
%gmatch floating-point or scientific real number
%%match a single % character
6. Type a comment about the command you expect to receive.

#### Control Descriptions

The following controls are found on the Wait for String dialog box.

| Control Name | Description |
| --- | --- |
| Port | Name of the serial port from which you expect to receive a command. |
| Wait For | Specifies how long the step waits for a command. The following options are available: Fixed Number of Bytes—When enabled, the step waits for the specified number bytes from the device specified in Port. Termination Char—When enabled, the step waits for the character that indicates the end of a command. The following options are available: None—No termination character NULL (\\00)—Null character CR (\\0D)—Carriage return LF (\\0A)—Line feed CR/LF (\\0D\\0A)—Carriage return/line feed User Defined—Enables the User-Defined Terminal Character control so that you can specify a custom termination character. |
| User-Defined Termination Character | Allows you to specify a termination character. Select User Defined from the Termination Character list to enable this control. |
| Add Termination Character to Result String | Adds the termination character to the result string. |
| Timeout | Number of milliseconds to wait for the string before timing out. |
| Pass Inspection If | Specifies the Pass condition for the step. The following options are available: Any string is received before timeout—Step passes if a string is received, regardless of the value, before the specified Timeout. String received before timeout matches—Step passes if the value of the string received before the specified Timeout matches the specified value. You may also specify how to display the string. |
| Comment | Comment about the command you expect to receive. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/setinspectionstatus_controls.html language=enus -->
## TOPIC 00038: Set Inspection Status Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/setinspectionstatus_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/setinspectionstatus_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Set Inspection Status Controls |
| --- | --- |

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Inspection Status**
  - Specifies the method used to update the Inspection Status variable. Set to FAIL if any previous step fails—Sets the Inspection Status variable to FAIL if any of the previous steps in the state fail. Set to FAIL if any previous step fails or if current value of Inspection Status is FAIL—Sets the Inspection Status variable to FAIL if either condition is true. Select this option when you want to check the inspection status set by a previous Set Inspection Status step, including steps in previous states. Set to measurement value—Sets the Inspection Status variable to the value of the selected measurement. Set to PASS—Sets the Inspection Status variable to PASS. Set to FAIL—Sets the Inspection Status variable to FAIL.
- **Update Number of Parts Inspected**
  - Specifies whether the step updates the # Pass, # Fail, and # Parts Inspected variables based on the Inspection Status variable value.

Parent topic:

Use Additional Tools Palette

Related example inspections

- Tutorial 1 - Coordinate System.vbai
- Tutorial 3 - Decision Making.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/setinspectionstatus_faq.html language=enus -->
## TOPIC 00039: Set Inspection Status FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/setinspectionstatus_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/setinspectionstatus_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Set Inspection Status FAQs |
| --- | --- |

Q: When are the # Pass, # Fail, and # Parts Inspected built-in system variables updated?

The # Pass, # Fail, and # Parts Inspected built-in system variables are updated 
 when the Inspection Status system variable is set and Update Number of Parts Inspected is TRUE. If there is no Set 
 Inspection Status step in your inspection, the # Pass, # Fail, and # Parts Inspected is not updated.

Parent topic:

Use Additional Tools Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/simrt_howto.html language=enus -->
## TOPIC 00040: Simulating Remote Targets

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/simrt_howto.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/simrt_howto.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Simulating Remote Targets

Simulating remote targets allows you to develop and edit Vision Builder AI inspections for a remote target using a desktop computer. In addition to the standard Vision Builder AI inspection steps, the following target-specific steps are available in simulation mode:

- Acquire Image (1394, GigE, or USB)
- Read/Write Camera Attributes
- Acquire Image (Smart Camera)
- Read/Write I/O
- Generate Pulse
- Read/Write I/O (Vision RIO)
- Generate Pulse (Vision RIO)

To use Vision Builder AI with a simulated remote target, complete the following steps:

1. On the Vision Builder AI Welcome screen click Add Simulated Target .
2. Select a remote target class to simulate and click OK . If you want to create a simulated NI Smart Camera, click Next and choose a camera model to simulate, then click OK .
3. On the Vision Builder AI Welcome screen, select the simulated remote target in the list of targets.
4. Click New Inspection .
5. Add and configure steps from the Inspection Steps palette to create your application.

#### Editing an Existing Inspection

When you open an existing inspection that has been configured for a remote target, simulation mode allows you to view and modify the inspection settings. When the inspection is redeployed to a remote target, the inspection uses the modified settings.

|  | Note When you are connected to a target in Configuration mode, and select Target»Add/Retrieve Inspections... from the menu, you can copy inspections to or from the target. Any cameras, or communication devices used by the target inspection will be saved as part of the inspection when copied to Windows. When Simulation mode is used to open this inspection on Windows, it will have access to all same cameras and communication devices the inspection was using on the target. Any changes made to the communication devices in simulation mode will update the settings in the inspection. When the inspection is copied back to the target, any changes may require reconciling when the inspection is opened on the target. |
| --- | --- |

#### Creating a New Inspection

When you create a new inspection for a remote target, simulation mode allows you to specify values for controls that can be set without connecting to a remote target. For example, while simulating an NI IC-3173, the **Acquire Image (1394, GigE, or USB)** step allows you to specify a **Step Name** and an **Acquisition Mode**, but the step does not allow you to specify camera attribute values because Vision Builder AI does not know which camera is connected to the target device where the inspection runs.

When you deploy a new inspection for the first time, Vision Builder AI prompts you to configure any hardware specific settings that were unavailable in simulation mode.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/slidecontrolsandindicators.html language=enus -->
## TOPIC 00041: Slide Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/slidecontrolsandindicators.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/slidecontrolsandindicators.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Slide Controls

- Click or drag the slider to a new position.
- Right-click the slide and select 
 Visible Items»Digital Display .
 Use the digital display to edit the slide value.

Slide objects can display more than one value. Right-click the object and select Add 
Slider to add more sliders. Right-click the object and select Fill Options 
to change how the slide fill is displayed. The data type of a control with multiple sliders is a cluster that 
contains each of the numeric values.

Parent topic:

Numeric Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/smartcamera_acquire.html language=enus -->
## TOPIC 00042: Acquire an Image with the NI Smart Camera

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/smartcamera_acquire.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/smartcamera_acquire.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Acquire an Image with a NI Smart Camera

Complete the following steps to acquire an image with an NI Smart Camera.

1. On the Vision Builder AI welcome screen, select the NI Smart Camera
in the list of targets.
2. Click Acquire Image (Smart Camera) Example to open the image acquisition example in the Vision Builder AI Configuration Interface.
3. Click the Run State Once button to acquire a single image.
4. In the State Configuration Window, double-click the Acquire Image (Smart Camera) step to open the property page.
5. Use the controls on the Main , Trigger , Lighting , and Advanced tabs
to configure any additional settings necessary for your application.
6. Click OK to save the step configuration.

To process acquired images, add additional steps to the inspection. Select **Help»Show Context Help** for information about the settings available for each step.

#### Related Information

- Troubleshoot the smart camera

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/smartcamera_troubleshoot.html language=enus -->
## TOPIC 00043: Troubleshooting the NI Smart Camera

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/smartcamera_troubleshoot.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/smartcamera_troubleshoot.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Troubleshooting the NI Smart Camera

#### The NI Smart Camera Does Not Appear in the List of Execution Targets

|  | Note On Windows devices, select My Computer as the target to run Vision Builder AI. Refer to Acquire an Image from an NI Smart Camera for instructions on acquiring an image on a Windows device. |
| --- | --- |

##### Verify that the NI Smart Camera Has Power

The Power and User LEDs are solid green.

##### Verify that the NI Smart Camera is Communicating with the Development Computer

The 100/1G LED flashes green while refreshing the list of devices in Vision Builder AI.

##### Verify that the Ethernet Cable Is Appropriate for Your Network

If you have a 1,000 Mbps link, verify that the M12 cable is X-coded and rated for 1,000 Mbps data transfer.

##### Verify the Network Settings

If the smart camera is configured to use a DHCP server and no DHCP server is present, the camera may not be visible on the network.
If you are using a static IP address, another device on the network may be using the same address. This can happen when you assign the 
same static IP to two devices, you assign a static IP that is in the range of the IP address available for DHCP use on your network, 
or the DHCP server assigns the same IP address to another device.

Connect the smart camera to the same subnet as the development computer and reconfigure the smart camera network settings. Refresh the list of targets on the Vision Builder AI Welcome screen, then reconfigure the network settings for the device.

##### Verify Firewall Settings

- Windows Firewall may have blocked Vision Builder AI from communicating with the smart camera. 
Refer to Adding a Firewall Exception for more information.
- A firewall may be blocking communication with the smart camera. 
Refer to Configuring a Firewall for Remote Targets for more information.

#### Related Information

The following documents provide complete instructions for setting up hardware, 
installing software, configuring an IP address, and contain device specifications. 
Download the documents from ni.com/manuals.

- ISC-178x Getting Started Guide
- ISC-178x User Manual

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/steps_manage.html language=enus -->
## TOPIC 00044: Managing Inspection Steps

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/steps_manage.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/steps_manage.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Managing Inspection Steps

#### Adding a Step to an Inspection

Follow these general instructions to add a step to the current inspection:

1. In the Inspection Steps palette, click the step you want to add to the inspection.
2. Configure the step according to the instructions in the Context Help window Configuration tab.
3. Click OK to add the step to the inspection.

#### Removing a Step from an Inspection

Follow one of these instructions to remove an inspection step from the State Configuration window:

- Right-click the step and select Delete .
- Click the step and select Edit»Delete .
- Click the step and click the Delete button.

#### Modifying a Step in an Inspection

Follow one of these instructions to open the property page of a step to modify its controls:

- Right-click the step, and select Edit .
- Click the step, and select Edit»Edit Step .
- Click the step, and click the Edit Step button.
- Double-click the step.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/tcpiowait_dialog.html language=enus -->
## TOPIC 00045: Wait (TCP)

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/tcpiowait_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/tcpiowait_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Wait (TCP)

Use this dialog box to configure your system to wait before sending or receiving commands.

#### How to Use

1. Type the number of milliseconds to wait.
2. Type a comment about your reason for waiting.

#### Control Descriptions

The following controls are found on the Wait dialog box.

| Control Name | Description |
| --- | --- |
| Wait For | Number of milliseconds to wait. |
| Comment | Comment about your reason for waiting. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/tcpiowaitstring_dialog.html language=enus -->
## TOPIC 00046: Wait for String (TCP)

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/tcpiowaitstring_dialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/tcpiowaitstring_dialog.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Wait for String (TCP)

Use this dialog box to configure your system to wait for an incoming command.

#### How to Use

1. Select the device you want to receive a command from the Device Name drop-down list.
2. Select whether you want to wait for a fixed number of bytes or a specified termination character or character set.
3. If you selected Termination Character , enter the termination character or character set you want to signal the end of the command. Enable the Add Termination Character to Result String to add the selected Termination Character to the string result.


 [IMAGE alt='image' src='tip.gif']
**Tip** Change the Display type to enter the termination character in hexadecimal or \ codes.
4. Type the number of milliseconds to wait for the command before timing out.
5. Select the Pass condition for the step. If you want the inspection to pass only when a specific string is received, select String received before timeout matches , and enter the expected string. Also, enable the Step fails in case of error or timeout control located on the property page for the TCP I/O step.

 [IMAGE alt='image' src='tip.gif']
**Tip** You can use the following wildcard characters in the expected string: 
 


CharacterDescription
%dmatch decimal integer
%omatch octal integer
%xmatch hexadecimal integer
%bmatch binary integer
%ematch scientific real number
%fmatch floating-point real number
%gmatch floating-point or scientific real number
%%match a single % character
6. Type a comment about the command you expect to receive.

#### Control Descriptions

The following controls are found on the Wait for String dialog box.

| Control Name | Description |
| --- | --- |
| Device Name | Name of the device from which you expect to receive a command. |
| Wait For | Specifies how long the step waits for a command. The following options are available: Fixed Number of Bytes—When enabled, the step waits for the specified number bytes from the device specified in Device Name. Termination Char—Character that indicates the end of a command. Add Termination Character to Result String—When enabled, appends the selected Termination Character to the received string. |
| Timeout | Number of milliseconds to wait for the string before timing out. For TCP slave devices, if a timeout occurs, the step returns the characters received before the timeout. For TCP master devices, if a timeout occurs, no characters are returned. |
| Pass Inspection If | Specifies the Pass condition for the step. The following options are available: Any string is received before timeout—Step passes if a string is received, regardless of the value, before the specified Timeout. String received before timeout matches—Step passes if the value of the string received before the specified Timeout matches the specified value. You may also specify how to display the string. |
| Comment | Comment about the command you expect to receive. |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/template_manage.html language=enus -->
## TOPIC 00047: Managing Images

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/template_manage.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/template_manage.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Managing Templates

#### Creating an Inspection from a Template

Complete the following steps to create a new inspection from an existing template:

1. Select File»New From Template to launch the Create New Inspection from Template dialog box.
 By default, only templates for the selected target are displayed. To view templates for all targets, select 
**Show inspection templates for all targets**.
2. Select the template that you want to use to create a new inspection.
 By default, inspection templates are installed to c:\Program Files\National Instruments\<Vision Builder AI version>\Templates. Double-click **Browse** to load an inspection template from another location.
3. Click OK .

Vision Builder AI loads the selected inspection template as an untitled inspection.

#### Saving an Inspection as a Template

Complete the following steps to save an inspection as a template.

1. Select File»Inspection Properties to open the Inspection Properties dialog box.
2. Enter a description of the template and click OK .
3. Select File»Save as Template .

By default, inspection templates are installed to c:\Program Files\National Instruments\<Vision Builder AI version>\Templates.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/thresholdimage_concepts.html language=enus -->
## TOPIC 00048: Threshold Image Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/thresholdimage_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/thresholdimage_concepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Threshold Image Concepts |
| --- | --- |

Threshold Image

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/thresholdimage_faq.html language=enus -->
## TOPIC 00049: Threshold Image FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/thresholdimage_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/thresholdimage_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Threshold Image FAQs |
| --- | --- |

**Q: What are the differences between the different local thresholding options?**

**A:**Niblack is good for display inspection or OCR applications. Sauvola is similar to Niblack but results in less noise and preserves the shape of the particles. Background correction is good for achieving the benefits of local threshold (that is, using local pixel values for thresholding) and avoiding the problems of other local thresholding algorithms (that is, large areas of common pixel values do not get thresholded). Refer to [Thresholding](/csh?topicname=nivisionconcepts/thresholding.html) for more information.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/thresholdimagecontrolscolor.html language=enus -->
## TOPIC 00050: Threshold Image Controls for Color Images

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/thresholdimagecontrolscolor.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/thresholdimagecontrolscolor.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Threshold Image Controls for Color Images |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_rgbu32.gif'] [IMAGE alt='image' src='vision_hslu32.gif']

#### Main Tab

The displayed controls vary with the selected color model.

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Color Model**
  - Specifies the color model to use for the operation. RGB—red, green, and blue HSL—hue, saturation, and luminance HSV—hue, saturation, and value HSI—hue, saturation, and intensity
- **Preview Color**
  - Specifies the color of the overlay to use for pixels that meet the threshold parameters.
- **Interval Mode**
  - Specifies whether the threshold range for the Hue color plane includes or excludes the specified range. Include Interval—Default. Threshold range: [specified minimum value, specified maximum value] Exclude Interval—Threshold range: [0, specified minimum value][specified maximum value, 255]
- **Color Plane Threshold Range Controls**
  - Specifies the threshold range for each color plane. Any pixel values not included in the specified range are ignored.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/thresholdimagecontrolsgrayscale.html language=enus -->
## TOPIC 00051: Threshold Image Controls for Grayscale Images

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/thresholdimagecontrolsgrayscale.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/thresholdimagecontrolsgrayscale.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Threshold Image Controls for Grayscale Images |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_u8.gif'] [IMAGE alt='image' src='vision_i16.gif'] [IMAGE alt='image' src='vision_u16.gif']

#### Main Tab

The displayed controls vary with the selected threshold method.

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Look For**
  - Specifies the type of objects to search for in the image. Bright Objects—Isolates pixels with intensity values between a user-specified value and 255. Dark Objects—Isolates pixels with intensity values between 0 and a user-specified value. Gray Objects—Isolates pixels with intensity values within a user-specified range. Use the Upper Limit or Lower Limit control to adjust the threshold range.
- **Method**
  - Specifies the type of threshold to use. Manual Threshold—Use this method when you want to determine the upper and lower threshold values manually. Automatic Threshold: Clustering—Use this method as a starting point for most images. Automatic Threshold: Entropy—Use this method when you are inspecting an image that contains very small objects of interest, such as small cosmetic defects. Automatic Threshold: Metric—Use this method when the object of interest and the background contain a comparable number of pixels. Automatic Threshold: Moments—Use this method for images that have poor contrast. Automatic Threshold: Inter Variance—Use this method when the object of interest and the background contain a comparable number of pixels. Local Threshold: Niblack—Use this method for images that contain non-uniform lighting conditions. Local Threshold: Background Correction—Use this method for images that contain non-uniform lighting conditions. Background correction also helps reduce noise in large, empty areas. Local Threshold: Sauvola—Use this method for images that contain non-uniform lighting conditions.

- **Deviation Factor**
  - Determines the sensitivity of the Local Threshold: Niblack or Local Threshold: Sauvola algorithm. Values range from 0 to 1, with 0 being the most sensitive to noise. The lower the Deviation Factor, the closer the pixel value must be to the mean value to be selected as part of a particle.
- **Sauvola Deviation**
  - Specifies the R constant used in the Sauvola local thresholding algorithm. The Sauvola Deviation and the Niblack or Sauvola Deviation Factor both determine the threshold calculation. The Sauvola Deviation is used to obtain better noise control in the thresholded image. The deviation is equivalent to the dynamic range of the standard deviation of the image. Valid R constants depend on the bit depth of the image. For 8-bit images, the range is 1 to 255. For 16-bit images, the range is 1 to 65,535. This value is only valid when the method is Local Threshold: Sauvola. Refer to Thresholding for more information.
- **Lower Value**
  - Specifies the lower value of the threshold range, as computed by the selected automatic threshold method. To manually specify a value, select the Manual Threshold method.
- **Upper Value**
  - Specifies the upper value of the threshold range, as computed by the selected automatic threshold method. To manually specify a value, select the Manual Threshold method.
- **Lower Limit**
  - Specifies the lowest value that an automatic threshold method can compute as the lower value for the threshold range.
- **Upper Limit**
  - Specifies the highest value that an automatic threshold method can compute as the upper value for the threshold range.
- **Kernel Size**
  - Specifies the size of the neighborhood around each pixel that a local threshold method uses compute the mean intensity value of the pixel. The kernel size is typically the same as the size of the object that you want to isolate. Tip Draw a region of interest around the object that you want to isolate, and click the Apply ROI button to use the ROI Size values.
- **ROI Size**
  - Displays the size of the of the last drawn region of interest. Click the Apply ROI button to copy the ROI Size values to the Kernel Size controls.
- **Deviation Factor**
  - Specifies the sensitivity of the Niblack thresholding algorithm. Values range from 0 to 1, with 0 being the most sensitive to noise.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/toolspalette.html language=enus -->
## TOPIC 00052: Tools Palette

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/toolspalette.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/toolspalette.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Tools Palette

The Tools palette contains the following tools:

- **Automatic Tool Selection**
  - automatically selects the appropriate tool from the Tools palette.
- **Operating**
  - Changes the value of a control.
- **Positioning**
  - Positions, resizes, and selects objects.
- **Labeling**
  - Creates fee labels and captions, edits existing labels and captions, or selects the text within a control.
- **Wiring**
  - No function.
- **Object Shortcut Menu**
  - Opens the shortcut menu of an object.
- **Scrolling**
  - Scrolls the window without using the scroll bars.
- **Breakpoint**
  - No function.
- **Probe**
  - No function.
- **Get Color**
  - Copies colors for pasting with the Coloring tool.
- **Coloring**
  - Sets the foreground and background colors.

Parent topic:

Inspection Interface Editor

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/ui_config.html language=enus -->
## TOPIC 00053: Configuration Interface

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/ui_config.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/ui_config.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Configuration Interface

Use the Configuration Interface to configure and debug an inspection.

|  |  |
| --- | --- |
| 1 Main Window | 3 Inspection Steps Palette |
| 2 Overview Window | 4 State Configuration Window |

- Main window —Displays the image being processed, property pages for some inspection steps, or the state diagram for the inspection. Use the Main window to define regions of interest in an image, configure step parameters for some steps, and create/modify the state diagram for an inspection.
- Overview window —Displays a thumbnail view of either the current inspection image, or the state diagram for the inspection.
- Inspection Steps palette —Lists and describes the steps that you use to create your inspection. When you click on a step, this palette transforms into the property page for the step.
- State Configuration window —Displays the list of steps that comprise the currently selected state in the inspection.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/updateinspectionui_controls.html language=enus -->
## TOPIC 00054: Update Inspection UI Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/updateinspectionui_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/updateinspectionui_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Update Inspection UI Controls |
| --- | --- |

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Run the VI After Updating Indicators**
  - When enabled, the selected custom Inspection Interface VI runs when the step executes. Note Run the VI After Updating Indicators is only available if the selected custom inspection interface VI contains code on the block diagram.
- **Inspection Interface Indicators and Controls**
  - Displays information about the controls and indicators on the inspection interface. Label—Indicates the name of the control or indicator. Type—Indicates whether the listed item is a control or indicator. Value—Displays the value used to update the control or indicator.
- **Operation**
  - Specifies how the currently selected control or indicator is updated. Do not Change Current Value—Does not change the control or indicator value when the step executes. Set to Constant—Sets the value of the selected variable to a user-specified constant. Set to Measurement—Sets the value of the selected variable to the value of a previous measurement result from a step in the same state as the Set Variable step. Only previous measurement results that are of the same type as the variable can be selected.
- **Edit Inspection Interface**
  - Launches the Inspection Interface Editor. Use the Inspection Interface Editor to add or remove controls, or to change the appearance of the custom inspection interface.
- **Show Inspection Interface**
  - Displays the currently selected inspection interface.

Parent topic:

Use Additional Tools Palette

Related example inspections

- Inspection Interface Example.vbai
- Inspection Interface Example - 2 images.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/updateinspectionui_faq.html language=enus -->
## TOPIC 00055: Update Inspection UI FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/updateinspectionui_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/updateinspectionui_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Update Inspection UI FAQs |
| --- | --- |

Q: Why are some of the controls or indicators on the custom 
 Inspection Interface not listed in the Inspection Interface table?

The Inspection Interface table only displays controls or indicators 
 that can be updated by the step. Vision Builder AI supports arrays of numeric, boolean, and string data types, as well as graphs, histograms, and charts.

Q: Why does the custom Inspection Interface behave differently on the development computer than it does on the remote target?

When you are connected to a remote target, Vision Builder AI uses a local copy of the 
 custom Inspection Interface VI on the remote target. This VI does not run, and any attributes that change when the VI executes or any control values that 
 change programmatically are not reflected in the interface shown on the development computer. Connect to the remote target using a Web server to fully 
 view the inspection behavior on the remote target.

Q: Why does the step use the original selected value of a shared system or network image variable that has undergone additional processing?

Processing steps do not update the value of a shared system or network variable. 
 To update a shared system or network image variable, use the **Set Variable** step to set **Current Image** as the variable value.

Q: How do I update a Histogram in a custom Inspection Interface?

Use the Get Histogram function of an **Array Operator** step to produce an array of X values and an array of Y values. Use the X and Y value arrays to update the histogram in the custom Inspection Interface. You can use the **Array Operator** step to specify a range of values, or to format values as either count or percentage values.

Q: Can I view and control the custom Inspection Interface from a Web browser?

You can enable real-time targets to control the custom Inspection Interface from a Web browser by configuring the [Vision Builder AI Remote Target Options](remotetargetoptions_tools.html) for a Web server.

Q: How can I create an inspection in which a user draws a region of interest (ROI) and the inspection uses the ROI in subsequent steps?

1. Open your custom inspection UI in LabVIEW. Place an Image Display control by right-clicking the front panel, and selecting Vision»Image Display .
2. In the block diagram, right-click the Image Display Control and select Create»Property Node»ROI .
3. Right-click on the output of the ROI property node and select Create»Indicator . Save.
4. Open Vision Builder AI, select Tools»Inspection Interface Configuration , and navigate to the location of the custom VI.
5. Open the Update Inspection UI step and enable the Run the VI after updating indicators checkbox. This ensures the VI runs when the step executes, the ROI indicator updates with the user-drawn ROI, and the inspection logs the ROI so other steps can access it.
6. Click OK to exit the step. Select View»View Custom Inspection Interface to see the custom UI. Draw an ROI on the image and run the Update Custom UI step so that it logs a valid ROI that can be used by subsequent steps.

Parent topic:

Use Additional Tools Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/updating_inspection_documentation.html language=enus -->
## TOPIC 00056: Updating Inspection Documentation

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/updating_inspection_documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/updating_inspection_documentation.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Updating Inspection Documentation

You can edit the documentation of the current inspection. Select **Edit»Edit Inspection Documentation**to edit and save any related documentation. The Tree on the left of the window lists the inspection, states, steps, and transitions for which documentation can be updated. Click items in the tree to change the selected documentation that is displayed. The title of the window and the tree selector will update to indicate which item’s documentation is currently being displayed.

|  | Note If the Ctrl-C, Ctrl-V, Delete keys are not working, use the right click popup menus for Cut/Copy/Paste operations. |
| --- | --- |

The functionality of the available buttons are as follows:

- Font Name — Changes the font of the selected text. The list of fonts is populated based on what is supported by the operating system.
- Font Size — Changes the font size of the selected text.
- Text Color — Changes the color of the selected text.
- Bold — Makes the selected text Bold.
- Italic —Makes the selected text Italic.
- Underline — Makes the selected text Underlined.
- Strikethrough — Makes the selected text strike through.
- **Insert/Remove Numbered List** — Adds or removes numbers at the beginning of each line.
- **Insert/Remove** Bulleted List —Adds or removesbullet pointsatthe beginning of each line.
- **Decrease Indent** — Decreases the indentation of the selected line.
- **Increase Indent** — In creases the indentation of the selected line.
- **Source** — Switches between displaying HTML source and formatted text .

Select **File****»Print Inspection Details**to print a table of all the states, steps, and transitions as well as their associated documentation.

|  | Note Selecting steps, states, or transitions will update the selected tree item and the associated documentation. Click on an open area of the state diagram to access the documentation for the inspection. |
| --- | --- |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/vbai_open_remote_connection.html language=enus -->
## TOPIC 00057: VBAI Open Remote Connection

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/vbai_open_remote_connection.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/vbai_open_remote_connection.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### **VBAI Open Remote Connection**

The **VBAI Open Remote Connection**step connects to the Vision Builder AI engine running on a remote target. This step can also load an inspection that can be run by the **VBAI Run Once** step. This step should be called once in the setup sequence since opening a connection may take several seconds, and you should not open or close the connection repeatedly during the run of the sequence for performance reasons. You can only open a single connection to a target but you can have the engine switch between different inspections using the **VBAI Run Once** to load a different inspection with different steps. Make sure to call the **VBAI Close Connection** step for each of the open connections.

**Select a target to connect to–** The remote target this step will connect to.

**User Name–** The user name for logging into the target. If the target does not have a user name and password configured, use the default value of "admin".

**Password****–** The password for logging into the target. If the target does not have a user name and password configured, use the default value of an empty string.

**Connect and Enumerate Inspection–** Click this button to connect to the selected target and enumerate the available inspections on the target. This will populate the Inspection list.

**Inspection–** Lists the available inspections on the target that can be selected. The first option of **Do not open an inspection** is available if you do not want the **VBAI Open Remote Connection** to load an inspection.

|  | Note Refer to C:\\Users\\Public\\Documents\\National Instruments\\<TestStand Version>\\Examples\\Vision Builder AI for examples that use this step. |
| --- | --- |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/vbai_run_once.html language=enus -->
## TOPIC 00058: VBAI Run Once

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/vbai_run_once.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/vbai_run_once.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### **VBAI Run Once**

The **VBAI Run Once**step runs a single iteration of the selected inspection from the start to the end state. You can optionally configure the step to set Vision Builder AI variables based on constants, or TestStand variables before running an iteration. After the iteration completes you can also configure TestStand variables to be updated with results from the inspection.

#### **Connection Tab**

**VBAI Open Connection Step–** The TestStand step that opens a connection to a Vision Builder AI Engine that this step will use. Only **VBAI Open Local Connection** and **VBAI Open Remote Connection** step types will be available in the drop down menu.

**Initialize Connection–** Click this button to establish a connection to the selected Vision Builder AI Engine. If a connection already exists, this button will be disabled.

**Inspection Path–** The path to the Vision Builder AI inspection to run. This is only available for local connections.

**Inspection–**The inspection to run. This is only available for remote connections.

**Reload Inspection–** Click this button to reload the inspection. This can be helpful if you are making changes to the inspection while editing this step and want to reload the inspection to get the latest updates. This is only available for local connections.

#### **Vision Builder AI Variables to Set Tab**

**Variables to Set Before Run****–** The table of Vision Builder AI variables and their values to set before this step runs the inspection once.

**Add Variable–** Adds a variable to set and allows you to configure the value to set the variable to before the inspection runs.

|  | Note The same variable cannot be set more than once before the inspection runs. |
| --- | --- |

**Remove Variable–** Removes the selected variable.

**Vision Builder AI Variable–** The Vision Builder AI variable to set before running the inspection.

**Value–** The value to set the variable to. This can either be a constant or a TestStand expression that may reference other results or variables in the sequence.

#### **Vision Builder AI Results to Get Tab**

**Results to Get After Run–** The table of Vision Builder AI results to get and the TestStand variable to update with the value after the inspection has run.

**Add Result–** Adds a result to get.

**Remove Result–** Removes the selected result.

**Vision Builder AI Result–** The Vision Builder AI result to get after running the inspection.

**TestStand Variable to Update–** The TestStand variable to update with the selected Vision Builder AI result.

**Add Variable–** Opens a dialog that can create a new TestStand variable.

**Run Inspection Once–** Runs the inspection. The inspection must be run to retrieve the available results to populate the **Vision Builder AI Result** tree.

|  | Note Any Variables to Set before Run (on the Vision Builder AI Variables to Set tab) that have been configured will always be set before running the inspection. Any TestStand variables to update will not be set when Run Inspection Once is pressed. They will only be updated when you click OK or run the sequence. |
| --- | --- |

|  | Note Refer to C:\\Users\\Public\\Documents\\National Instruments\\<TestStand Version>\\Examples\\Vision Builder AI for examples that use this step. |
| --- | --- |

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/viewmeas_tools.html language=enus -->
## TOPIC 00059: Viewing Inspection Results

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/viewmeas_tools.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/viewmeas_tools.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Viewing Inspection Results

Select **Tools»View Measurements** to open the Inspection Measurements window and view a list of all the measurements logged for each step in the inspection. The Inspection Measurements window is divided into two sections: the Results and the Selected Results.

#### Results

The Results section includes all the results from the inspection. The Results section is not updated while an inspection is running. You must pause or stop the inspection to update the results. To manually change the value of a result, right-click the result and select **Edit Value**. The value updates the next time the step runs. Use the controls at bottom of the Results table to list all results or only results from the current state.

#### Selected Results

The Selected Results update continuously, even if the inspection is running. To add results to the Selected Results, right-click a result and select **Add to Selected Results**. Hold down the <Shift> to select a range of results, or the <Ctrl> key to select multiple individual results.

The Selected Results table displays the minimum, maximum, and average values for numeric results. Right-click the Selected Results table to open a shortcut menu with options to edit values, remove results, reset statistics, and hide columns.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/visionassist_concepts.html language=enus -->
## TOPIC 00060: Vision Assistant Concepts

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/visionassist_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/visionassist_concepts.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Vision Assistant Concepts |
| --- | --- |

Use Vision Assistant to create a sequence of image processing and analysis 
 functions that can improve the quality of your image for inspection. You can 
 access the Vision Builder AI Vision Assistant Help from the 
 Help menu inside Vision Assistant.

Parent topic:

Enhance Images Palette

Related example inspections

- Classify Colors Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/visionassist_controls.html language=enus -->
## TOPIC 00061: Vision Assistant Controls

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/visionassist_controls.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/visionassist_controls.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Vision Assistant Controls |
| --- | --- |

Supported image types:

[IMAGE alt='image' src='vision_u8.gif'] [IMAGE alt='image' src='vision_u16.gif'] [IMAGE alt='image' src='vision_i16.gif'] [IMAGE alt='image' src='vision_sgl.gif'] [IMAGE alt='image' src='vision_rgbu32.gif'] [IMAGE alt='image' src='vision_hslu32.gif']

#### Main Tab

- **Step Name**
  - Specifies a unique name to identify the step in the inspection.
- **Region of Interest**
  - Specifies the region of the image to process.
- **Reposition Region of Interest**
  - Repositions the region of interest dynamically based on a coordinate system from a previous Set Coordinate System step. Link the region of interest to a coordinate system if the position of the object under inspection changes from image to image, and you need to adjust the position of the region of interest to match the new location of the object.
- **Reference Coordinate System**
  - Specifies the coordinate system to which you want to link the region of interest.
- **Image Processing Steps**
  - Lists the Vision Assistant image processing steps to apply to the region of interest. Click Edit to launch Vision Assistant and configure image processing steps.
- **Edit**
  - Launches Vision Assistant.
- **Color Palette**
  - Enables the user to add a color palette to monochrome images. Refer to Color Palette editor for more details.

Parent topic:

Enhance Images Palette

Related example inspections

- Classify Colors Example.vbai

Examples are located in the <Users>\Public\Public Documents\National Instruments\<Vision Builder AI version>\Examples directory.

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/visionassist_faq.html language=enus -->
## TOPIC 00062: Vision Assistant FAQs

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/visionassist_faq.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/visionassist_faq.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

|  | Vision Assistant FAQs |
| --- | --- |

Q: I modified an image with Vision Assistant. Can I take measurements from the original image?

Use the Select Image step to retrieve the original image and make different measurements.

Q: When I select a shared system or network image variable that has been processed with a Vision Assistant step, why does the step output an unmodified image?

Processing steps do not update the value of a shared system or network variable. 
 To update a shared system or network image variable, Add an **Image Buffer** step in Vision Assistant to set the current image as the variable value.

Q: My binary image appears black and red in Vision Assistant. Why does the same image appear black and white in Vision Builder AI?

A binary image in Vision Assistant has two pixel values: 0 (black) and 1 (shown in red for display purposes). To achieve better contrast in the image, Vision Builder AI scales the intensity value for pixels with a value of 1 in Vision Assistant to a value of 255 (white).

Q: When I return to Vision Builder AI after configuring a Vision Assistant step, why does a Lookup Table step appear at the end of the Image Processing Steps list?

When you threshold an image in Vision Assistant, the pixels in the resulting binary image have values of 0 and 1. Vision Builder AI adds a Lookup Table step to convert the pixels whose values equal 1 to 255 to visibly distinguish pixels of interest from background pixels.

Q: The Reposition Region of Interest and Reference Coordinate System controls are disabled. How can I make these options available?

Insert a Set Coordinate System step before this step to make the Reposition Region of Interest and Reference Coordinate System controls available.

Parent topic:

Enhance Images Palette

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/welcome_acquire_image.html language=enus -->
## TOPIC 00063: Help Me Acquire My First Image in Vision Builder AI

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/welcome_acquire_image.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/welcome_acquire_image.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Help Me Acquire an Image in Vision Builder AI

Select your hardware:

- NI Smart Camera
- Camera Connected to a Windows Device
- Camera Connected to a Real-Time NI Compact Vision System or Industrial Controller

<!--NI_TOPIC bundle=ni-vision-builder-for-automated-inspection-configuration-help path=vbai_config/welcome_troubleshoot_hw.html language=enus -->
## TOPIC 00064: Troubleshoot NI Hardware in Vision Builder AI

- bundle_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- source_path: `vbai_config/welcome_troubleshoot_hw.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-builder-for-automated-inspection-configuration-help/raw/resource/enus/vbai_config/welcome_troubleshoot_hw.html
- document_id: `ni-vision-builder-for-automated-inspection-configuration-help`
- page_type: `leaf`
- content_type: ``

### Troubleshoot NI Hardware in Vision Builder AI

Select the type of hardware you are using:

- Smart Camera
- Compact Vision System or Industrial Controller

For a complete list of supported hardware, refer to the *Vision Builder for Automated Inspection Readme*.
