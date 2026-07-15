# NI DOCUMENT BUNDLE: ni-vision-c-support-help

<!--NI_BUNDLE_CHUNK bundle=ni-vision-c-support-help start=1 end=25 -->
<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classacquisition.html language=enus -->
## TOPIC 00001: Acquisition

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classacquisition.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Acquisition

Acquisition functions let you perform common acquisition tasks, such as ring acquisitions, sequence acquisitions, and grabs, directly into an NI Vision image. To perform more advanced acquisitions, such as triggered acquisitions, see the NI-IMAQ Function Reference Help. You can use the Acquisition functions with the Signal I/O functions described in the NI-IMAQ Function Reference Help. Functions in this section require NI-IMAQ 2.2 or higher.

##### Functions

- imaqCopyFromRing
- imaqEasyAcquire
- imaqExtractFromRing
- imaqGrab
- imaqReleaseImage
- imaqSetupGrab
- imaqSetupRing
- imaqSetupSequence
- imaqSnap
- imaqStartAcquisition
- imaqStopAcquisition

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classarithmetic.html language=enus -->
## TOPIC 00002: Arithmetic

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classarithmetic.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classarithmetic.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Arithmetic

The following functions are available only with a licensed version of NI Vision.
 

 Arithmetic functions allow you to perform arithmetic operations between two images or between an image and a constant.

##### Functions

- imaqAbsoluteDifference
- imaqAbsoluteDifferenceConstant
- imaqAdd
- imaqAddConstant
- imaqAverage
- imaqAverageConstant
- imaqDivide2
- imaqDivideConstant2
- imaqMax
- imaqMaxConstant
- imaqMin
- imaqMinConstant
- imaqModulo
- imaqModuloConstant
- imaqMulDiv
- imaqMultiply
- imaqMultiplyConstant
- imaqSubtract
- imaqSubtractConstant

#### References

[Operators](classoperators.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classborder.html language=enus -->
## TOPIC 00003: Border

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classborder.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classborder.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Border

Border functions allow you to fill an image border with a set of values, get the size of an image border, and set the size of image border.

##### Functions

- imaqFillBorder
- imaqGetBorderSize
- imaqSetBorderSize

#### References

[Image Management](classimage%20management.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classcalibration.html language=enus -->
## TOPIC 00004: Calibration

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classcalibration.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Calibration

The following functions are available only with a licensed version of NI Vision.
 

 Calibration functions allow you to spatially calibrate images. Spatial calibration converts pixel coordinates to real-world coordinates while compensating for potential perspective errors or nonlinear distortions in your imaging system.

##### Functions

- imaqCalibrationCompactInformation
- imaqCalibrationCorrectionLearnSetup
- imaqCalibrationCorrectionLearnSetup2
- imaqCalibrationGetCalibrationInfo
- imaqCalibrationGetCameraParameters
- imaqCalibrationGetThumbnailImage
- imaqCalibrationSetAxisInfo
- imaqCalibrationSetAxisInfoByReferencePoints
- imaqCalibrationTargetToPoints
- imaqCalibrationTargetToPoints2
- imaqCopyCalibrationInfo2
- imaqCorrectCalibratedImage
- imaqGetCalibrationInfo2
- imaqGetCalibrationInfo3
- imaqLearnCalibrationGrid
- imaqLearnCalibrationPoints
- imaqLearnCameraModel
- imaqLearnCameraModel2
- imaqLearnDistortionModel
- imaqLearnDistortionModel2
- imaqLearnMicroPlaneCalibration
- imaqLearnPerspectiveCalibration
- imaqSetCoordinateSystem
- imaqSetSimpleCalibration
- imaqSetSimpleCalibration2
- imaqTransformPixelToRealWorld
- imaqTransformRealWorldToPixel

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classcaliper.html language=enus -->
## TOPIC 00005: Caliper

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classcaliper.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classcaliper.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Caliper

The following functions are available only with a licensed version of NI Vision.
 

 Caliper functions allow you to detect and measure features, such as edges and angles, along a path in an image.

##### Functions

- imaqCaliperTool
- imaqConcentricRake2
- imaqConcentricRake3
- imaqDetectExtremes
- imaqDetectRotation
- imaqEdgeTool4
- imaqFindEdge2
- imaqFindTransformRect2
- imaqFindTransformRects2
- imaqLineGaugeTool2
- imaqRake2
- imaqRake3
- imaqSimpleEdge
- imaqSpoke2
- imaqSpoke3
- imaqStraightEdge
- imaqStraightEdge2

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classclassification.html language=enus -->
## TOPIC 00006: Classification

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classclassification.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classclassification.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Classification

The following functions are available only with a licensed version of NI Vision.
 

 Classification functions let you identify an unknown object by comparing a set of its significant features to a set of features that conceptually represent classes of known objects.

##### Functions

- imaqAddClassifierSample
- imaqAdvanceClassify
- imaqClassificationTrainSVM
- imaqClassify
- imaqCreateClassifier
- imaqDeleteClassifierSample
- imaqGetClassifierAccuracy
- imaqGetClassifierSampleInfo
- imaqGetColorClassifierOptions
- imaqGetNearestNeighborOptions
- imaqGetParticleClassifierOptions2
- imaqReadClassifierFile
- imaqRelabelClassifierSample
- imaqSetColorClassifierOptions
- imaqSetParticleClassifierOptions2
- imaqTrainNearestNeighborClassifier
- imaqWriteClassifierFile

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classclipboard.html language=enus -->
## TOPIC 00007: Clipboard

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classclipboard.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classclipboard.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Clipboard

The following functions are available only with a licensed version of NI Vision.
 

 Clipboard functions allow you to copy images to and from the clipboard.

##### Functions

- imaqClipboardToImage
- imaqImageToClipboard

#### References

[Image Management](classimage%20management.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classcontours.html language=enus -->
## TOPIC 00008: Contours

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classcontours.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classcontours.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Contours

Contour functions allow you to create and modify individual contours of a region of interest.

##### Functions

- imaqAddAnnulusContour
- imaqAddClosedContour
- imaqAddLineContour
- imaqAddOpenContour
- imaqAddOvalContour
- imaqAddPointContour
- imaqAddRectContour
- imaqAddRotatedRectContour2
- imaqCopyContour
- imaqGetContour
- imaqGetContourColor
- imaqGetContourCount
- imaqGetContourInfo2
- imaqMoveContour
- imaqRemoveContour
- imaqSetContourColor

#### References

[Regions of Interest](classregions%20of%20interest.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classdisplay.html language=enus -->
## TOPIC 00009: Display

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classdisplay.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classdisplay.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Display

Display functions allow you to display images in image windows.

##### Classes

- Tool Window
- Window Management

##### Functions

- imaqAreToolsContextSensitive
- imaqCloseWindow
- imaqDisplayImage
- imaqGetLastKey
- imaqGetSystemWindowHandle
- imaqGetWindowCenterPos
- imaqSetToolContextSensitivity
- imaqShowWindow

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classdrawing.html language=enus -->
## TOPIC 00010: Drawing

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classdrawing.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classdrawing.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Drawing

The following functions are available only with a licensed version of NI Vision.
 

 Drawing functions allow you to draw lines, shapes, and text on images.

##### Functions

- imaqDrawLineOnImage
- imaqDrawShapeOnImage
- imaqDrawTextOnImage

#### References

[Image Management](classimage%20management.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classinspection.html language=enus -->
## TOPIC 00011: Inspection

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classinspection.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classinspection.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Inspection

The following functions are available only with a licensed version of NI Vision.
 

 Inspection functions allow you to compare images to a golden template image.

##### Functions

- imaqCompareGoldenTemplate
- imaqLearnGoldenTemplate

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classinterlacing.html language=enus -->
## TOPIC 00012: Interlacing

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classinterlacing.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classinterlacing.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Interlacing

The following functions are available only with a licensed version of NI Vision.
 

 Interlacing functions allow you to combine two fields into one image frame or separate a frame into two fields.

##### Functions

- imaqInterlaceCombine
- imaqInterlaceSeparate

#### References

[Image Management](classimage%20management.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classlcd.html language=enus -->
## TOPIC 00013: LCD

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classlcd.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classlcd.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### LCD

The following functions are available only with a licensed version of NI Vision.
 

 LCD functions allow you to isolate and read the value of a seven-segment LCD.

##### Functions

- imaqFindLCDSegments
- imaqReadLCD

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classlogical.html language=enus -->
## TOPIC 00014: Logical

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classlogical.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classlogical.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Logical

The following functions are available only with a licensed version of NI Vision.
 

 Logical functions allow you to perform logic operations between two images or between an image and a constant.

##### Functions

- imaqAnd
- imaqAndConstant
- imaqCompare
- imaqCompareConstant
- imaqLogicalDifference
- imaqLogicalDifferenceConstant
- imaqNand
- imaqNandConstant
- imaqNor
- imaqNorConstant
- imaqOr
- imaqOrConstant
- imaqXnor
- imaqXnorConstant
- imaqXor
- imaqXorConstant

#### References

[Operators](classoperators.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classmeter.html language=enus -->
## TOPIC 00015: Meter

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classmeter.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classmeter.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Meter

The following functions are available only with a licensed version of NI Vision.
 

 Meter functions allow you to identify the arc information of a meter and then read that meter.

##### Functions

- imaqGetMeterArc
- imaqReadMeter

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classmorphology.html language=enus -->
## TOPIC 00016: Morphology

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classmorphology.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classmorphology.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Morphology

The following functions are available only with a licensed version of NI Vision.
 

 Morphology functions allow you to apply standard morphological transformations, such as dilations and erosions.

##### Functions

- imaqGrayMorphology
- imaqGrayMorphology2

#### References

[Grayscale Processing](classgrayscale%20processing.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classocr.html language=enus -->
## TOPIC 00017: OCR

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classocr.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classocr.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### OCR

The following functions are available only with a licensed version of NI Vision.
 

 Use the optical character recognition (OCR) functions to develop an OCR read application.
 

 OCR is the process by which the machine vision software reads text and/or characters in an image. OCR consists of the following two procedures:
 

 Training characters
 

 Reading characters
 

 Training characters is the process by which you teach the machine vision software the types of characters and/or patterns you want to read in the image during the reading procedure. You can use NI Vision to train any number of characters, creating a character set, which is the set of characters that you later compare with objects during the reading procedure. You store the character set you create in a character set file. Training might be a one-time process, or it might be a process you repeat several times, creating several character sets to broaden the scope of characters you want to detect in an image.
 

 Reading characters is the process by which the machine vision application you create analyzes an image to determine if the objects match the characters you trained. The machine vision application reads characters in an image using the character set that you created when you trained characters.

##### Functions

- imaqCreateCharSet
- imaqDeleteChar
- imaqGetCharCount
- imaqGetCharInfo2
- imaqReadOCRFile
- imaqReadOCRFile2
- imaqReadText3
- imaqReadText4
- imaqRenameChar
- imaqSetReferenceChar
- imaqTrainChars
- imaqTrainChars2
- imaqVerifyPatterns
- imaqVerifyText
- imaqWriteOCRFile
- imaqWriteOCRFile2

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classoperators.html language=enus -->
## TOPIC 00018: Operators

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classoperators.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classoperators.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Operators

Operator functions allow you to perform arithmetic or logical operations between two images or between an image and a constant.

##### Classes

- Arithmetic
- Logical

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classoverlay.html language=enus -->
## TOPIC 00019: Overlay

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classoverlay.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classoverlay.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Overlay

Overlay functions allow you to create overlays and associate them with image windows.

##### Functions

- imaqClearOverlay
- imaqCopyOverlay
- imaqGetOverlayProperties
- imaqMergeOverlay
- imaqOverlayArc
- imaqOverlayBitmap
- imaqOverlayClosedContour
- imaqOverlayLine
- imaqOverlayLines3
- imaqOverlayMetafile
- imaqOverlayOpenContour
- imaqOverlayOval
- imaqOverlayPoints
- imaqOverlayRect
- imaqOverlayROI
- imaqOverlayText
- imaqSetOverlayProperties

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classstereo.html language=enus -->
## TOPIC 00020: Stereo

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classstereo.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classstereo.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Stereo

Use Stereo functions to develop binocular stereo vision applications. A binocular stereo vision system uses two cameras that are separated by a short distance and are mounted almost parallel to one another.

##### Functions

- imaq3DVisionCreateBinocularStereoSession
- imaq3DVisionDisposeBincocularStereoSession
- imaq3DVisionReadBincocularStereoFile
- imaq3DVisionWriteBincocularStereoFile
- imaqGetMaxDisparityFromMinDepth
- imaqInterpolateDisparityImage2
- imaqVision3DBincocularConvertPixelTo3DCoordinates
- imaqVision3DBincocularGetCalibrationInfo
- imaqVision3DBincocularStereoGetDepthImage
- imaqVision3DBincocularStereoGetDepthPlanes
- imaqVision3DBincocularStereoGetRectifiedImage
- imaqVision3DBinocularStereoCorrespondenceUsingBM2
- imaqVision3DBinocularStereoCorrespondenceUsingSGBM2
- imaqVision3DLearnBincocularStereoCalibration

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classtexture.html language=enus -->
## TOPIC 00021: Texture

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classtexture.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classtexture.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Texture

The following functions are available only with a licensed version of NI Vision.
 

 Use the Texture functions to detect defects in textured images and to extract texture features from images.

##### Functions

- imaqClassificationTextureDefectOptions
- imaqCooccurrenceMatrix
- imaqDetectTextureDefect
- imaqExtractTextureFeatures
- imaqExtractWaveletBands

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classthreshold.html language=enus -->
## TOPIC 00022: Threshold

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classthreshold.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Threshold

The following functions are available only with a licensed version of NI Vision.
 

 Threshold functions allow you to convert a grayscale image to a binary image.

##### Functions

- imaqAutoThreshold2
- imaqAutoThreshold3
- imaqLocalThreshold
- imaqMagicWand
- imaqMultithreshold
- imaqThreshold

#### References

[Grayscale Processing](classgrayscale%20processing.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classtransform.html language=enus -->
## TOPIC 00023: Transform

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classtransform.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classtransform.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Transform

The following functions are available only with a licensed version of NI Vision.
 

 Transform functions allow you to replace each pixel in an image using a transfer function.

##### Functions

- imaqBCGTransform
- imaqEqualize
- imaqInverse
- imaqLookup2
- imaqMathTransform
- imaqWatershedTransform

#### References

[Grayscale Processing](classgrayscale%20processing.html) 

 [NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/classutilities.html language=enus -->
## TOPIC 00024: Utilities

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/classutilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/classutilities.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

### Utilities

Utilities functions allow you to set up structures that you can embed in other functions to eliminate the need to declare certain types of variables such as Point, PointFloat, and Rect.

##### Functions

- imaqGetKernel
- imaqMakeAnnulus
- imaqMakePoint
- imaqMakePointFloat
- imaqMakeRect
- imaqMakeRectFromRotatedRect
- imaqMakeRotatedRect
- imaqMakeRotatedRectFromRect
- imaqMulticoreOptions

#### References

[NI Vision](ni%20vision.html) 

 [Alphabetical Function Index](alphabetical%20function%20index.html) 

 [Hierarchical Function Index](hierarchical%20function%20index.html)

<!--NI_TOPIC bundle=ni-vision-c-support-help path=nivisioncsupport/nivisioncsupport.html language=enus -->
## TOPIC 00025: NI Vision C Support Help

- bundle_id: `ni-vision-c-support-help`
- source_path: `nivisioncsupport/nivisioncsupport.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-c-support-help/raw/resource/enus/nivisioncsupport/nivisioncsupport.html
- document_id: `ni-vision-c-support-help`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### NI Vision C Support Help

July 2021, 370379Y-01

NI Vision for C is a library of C functions that you can use to develop image processing and machine vision applications.

For more information about this help file, refer to the following topics:

[Related Documentation](related_documentation.html)

[Glossary](glossary.html)

[NI Services](technical_support_resources.html)

© 2001–2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.
