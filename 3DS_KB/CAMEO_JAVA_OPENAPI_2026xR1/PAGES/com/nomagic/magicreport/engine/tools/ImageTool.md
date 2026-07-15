# JAVA OPENAPI: ImageTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/tools/ImageTool.html
- source_path: `com/nomagic/magicreport/engine/tools/ImageTool.html`
- source_sha256: `f6b4d1315a8d54d2435866c798a4eb20a8e80f2e9473baa6344b84118b605a45`
- captured_utc: `2026-07-14T16:46:12.690972+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class ImageTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../Tool.html)
com.nomagic.magicreport.engine.tools.ImageTool

All Implemented Interfaces:
`[ITool](../ITool.html)`, `[IVariable](../../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classImageTool
extends [Tool](../Tool.html)

A tool provides functions for manipulate image.

Since:
July 02, 2008
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.ImageTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`class`
`[ImageTool.ImageProperty](ImageTool.ImageProperty.html)`
Class that store image and its properties e.g., format, path ect.
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[ITool.HTMLString](../ITool.HTMLString.html), [ITool.RetainedString](../ITool.RetainedString.html), [ITool.Void](../ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
`static final int`
`[DEFAULT_DPI](#DEFAULT_DPI)`
The default DPI which is 96.
`static final int`
`[HIGH](#HIGH)`
The scaling quality high.
`static final int`
`[HIGHEST](#HIGHEST)`
The scaling quality highest.
`static final int`
`[LOW](#LOW)`
The scaling quality low.
`static final int`
`[LOWEST](#LOWEST)`
The scaling quality lowest.
`static final int`
`[MEDIUM](#MEDIUM)`
The scaling quality medium.
`static final int`
`[PAPER_SIZE](#PAPER_SIZE)`
Constant value for paper size.
`static final int`
`[REDUCE_TO_PAPER_SIZE](#REDUCE_TO_PAPER_SIZE)`
Constant value for paper size.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[context](../Tool.html#context), [properties](../Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[VOID](../ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImageTool](#%3Cinit%3E())()`
Prevent empty initiate.
`[ImageTool](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../ITemplateEngine.html) engine)`
Create an image tool with engine.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected float[]`
`[calculatePaperWidthHeight](#calculatePaperWidthHeight())()`
Deprecated.
see [`getPaperBounds()`](#getPaperBounds())
`[Image](../../Image.html)`
`[copy](#copy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)`
Copy an external image from local file or URL into report.
`protected [IFormatterWrapper](IFormatterWrapper.html)`
`[createFormatterWrapper](#createFormatterWrapper(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> engineClass)`
Create the formatter wrapper from given engine class.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[createImageWithAbsolutePath](#createImageWithAbsolutePath(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Export image and return absolute path of the file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return absolute path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[createImageWithAbsolutePath](#createImageWithAbsolutePath(com.nomagic.magicreport.Image,boolean))([Image](../../Image.html) image,
 boolean includeURI)`
Export image and return absolute path of the file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return absolute path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[createImageWithRelativePath](#createImageWithRelativePath(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Export image and return relative path of image file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return relative path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
`[ITool.Void](../ITool.Void.html)`
`[createSilentImage](#createSilentImage(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Create image and do not return any path.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[getAbsolutePath](#getAbsolutePath(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Return an absolute path of image file.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[getAbsolutePath](#getAbsolutePath(com.nomagic.magicreport.Image,boolean))([Image](../../Image.html) image,
 boolean includeURI)`
Return an absolute path of image file.
`int`
`[getDPI](#getDPI())()`

`[ImageTool.ImageProperty](ImageTool.ImageProperty.html)`
`[getImageProperty](#getImageProperty(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Get ImageProperty object
`protected [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getPaperBounds](#getPaperBounds())()`
Calculate the paper bounds.
`protected [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getPaperBounds](#getPaperBounds(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Calculate the paper bounds.
`[ITool.RetainedString](../ITool.RetainedString.html)`
`[getRelativePath](#getRelativePath(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Return a possible relative path of image file.
`[Image](../../Image.html)`
`[include](#include(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)`
Include an external image from local file or URL into report.
`[Image](../../Image.html)`
`[limitImageSize](#limitImageSize(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Limit image size to paper page size.
`[Image](../../Image.html)`
`[limitImageSize](#limitImageSize(com.nomagic.magicreport.Image,int,int))([Image](../../Image.html) image,
 int maximumWidthPixel,
 int maximumHeightPixel)`
Limit image size to paper page size and maximum size.
`[Image](../../Image.html)`
`[limitImageSize](#limitImageSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) maximumWidth,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) maximumHeight)`
Limit image size to paper page size and maximum size.
`int`
`[measureToPixel](#measureToPixel(com.nomagic.magicreport.Image,java.lang.String))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) measure)`
Transforms measurements into pixel count.
`int`
`[measureToPixel](#measureToPixel(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) measure)`

`[Image](../../Image.html)`
`[rotateLeft](#rotateLeft(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Return the image transform with clockwise rotation transformation.
`[Image](../../Image.html)`
`[rotateRight](#rotateRight(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Return the image transformed with clockwise rotation transformation.
`[Image](../../Image.html)`
`[scale](#scale(com.nomagic.magicreport.Image,double))([Image](../../Image.html) image,
 double sxy)`
Convenience method to scale equally in height and width.
`[Image](../../Image.html)`
`[scale](#scale(com.nomagic.magicreport.Image,double,double))([Image](../../Image.html) image,
 double sx,
 double sy)`
Return the image after scaling transformation.
`[ITool.Void](../ITool.Void.html)`
`[setDPI](#setDPI(int))(int newDpi)`
Sets the DPI value for this document.
`[Image](../../Image.html)`
`[setHeight](#setHeight(com.nomagic.magicreport.Image,int))([Image](../../Image.html) image,
 int height)`
Return the image from specified height.
`[Image](../../Image.html)`
`[setHeight](#setHeight(com.nomagic.magicreport.Image,int,boolean))([Image](../../Image.html) image,
 int height,
 boolean keepratio)`
Return the image from specified height.
`[Image](../../Image.html)`
`[setHeight](#setHeight(com.nomagic.magicreport.Image,java.lang.String))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height)`
Scale the image by the given height measurement, keeping the ratio.
`[Image](../../Image.html)`
`[setHeight](#setHeight(com.nomagic.magicreport.Image,java.lang.String,boolean))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height,
 boolean keepRatio)`
Scale the image by the given height measurement, and keep ratio if set.
`[ITool.Void](../ITool.Void.html)`
`[setScalingQuality](#setScalingQuality(int))(int quality)`
Sets the image scaling quality.
`void`
`[setSeparateChar](#setSeparateChar(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separateChar)`
Set separate character for printing image path. 

 For example. 

 "/" or "\"
`[Image](../../Image.html)`
`[setSize](#setSize(com.nomagic.magicreport.Image,int,int))([Image](../../Image.html) image,
 int width,
 int height)`
Return the image from specified width and height.
`[Image](../../Image.html)`
`[setSize](#setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height)`
Scale the image by the given width/height measurements.
`[Image](../../Image.html)`
`[setSize](#setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String,boolean))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height,
 boolean overrideAutoSizing)`
Scale the image by the given width/height measurements.
`[Image](../../Image.html)`
`[setWidth](#setWidth(com.nomagic.magicreport.Image,int))([Image](../../Image.html) image,
 int width)`
Return the image from specified width.
`[Image](../../Image.html)`
`[setWidth](#setWidth(com.nomagic.magicreport.Image,int,boolean))([Image](../../Image.html) image,
 int width,
 boolean keepratio)`
Return the image from specified width.
`[Image](../../Image.html)`
`[setWidth](#setWidth(com.nomagic.magicreport.Image,java.lang.String))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width)`
Scale the image by the given width measurements, keeping the ratio.
`[Image](../../Image.html)`
`[setWidth](#setWidth(com.nomagic.magicreport.Image,java.lang.String,boolean))([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 boolean keepRatio)`
Scale the image by the given width measurement, and keep ratio if set.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Image](../../Image.html)>`
`[split](#split(com.nomagic.magicreport.Image))([Image](../../Image.html) image)`
Split the image into rows and columns with automatic number of rows and columns, and draw each chunked image
 from left-to-right and top-to-bottom.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Image](../../Image.html)>`
`[split](#split(com.nomagic.magicreport.Image,int,int))([Image](../../Image.html) image,
 int cols,
 int rows)`
Split the image into rows and columns, and draw each chunked image from left-to-right and top-to-bottom.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[clone](../Tool.html#clone()), [getContext](../Tool.html#getContext()), [getProperties](../Tool.html#getProperties()), [getProperty](../Tool.html#getProperty(java.lang.String)), [getProperty](../Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../Tool.html#notifyObservers(java.lang.Object)), [setContext](../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[clearTool](../ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.CONTEXT_NAME)
LOWEST
public static final int LOWEST
The scaling quality lowest. Current implementation is interpolation nearest neighbor.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.LOWEST)
LOW
public static final int LOW
The scaling quality low. Current implementation is one step interpolation bi-linear.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.LOW)
MEDIUM
public static final int MEDIUM
The scaling quality medium. Current implementation is interpolation bi-cubic.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.MEDIUM)
HIGH
public static final int HIGH
The scaling quality high. Current implementation is multi-steps interpolation bi-linear.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.HIGH)
HIGHEST
public static final int HIGHEST
The scaling quality highest. Current implementation is area average image scaling algorithm. (Default value)
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.HIGHEST)
PAPER_SIZE
public static final int PAPER_SIZE
Constant value for paper size. Use this value to set image dimension to paper size.
 

 Example: `$image.setWidth($diagram.image, -1)`
See Also:
[`setWidth(com.nomagic.magicreport.Image, int)`](#setWidth(com.nomagic.magicreport.Image,int))
[`setWidth(com.nomagic.magicreport.Image, int, boolean)`](#setWidth(com.nomagic.magicreport.Image,int,boolean))
[`setHeight(com.nomagic.magicreport.Image, int)`](#setHeight(com.nomagic.magicreport.Image,int))
[`setHeight(com.nomagic.magicreport.Image, int, boolean)`](#setHeight(com.nomagic.magicreport.Image,int,boolean))
[`setSize(com.nomagic.magicreport.Image, int, int)`](#setSize(com.nomagic.magicreport.Image,int,int))
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.PAPER_SIZE)
DEFAULT_DPI
public static final int DEFAULT_DPI
The default DPI which is 96.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.DEFAULT_DPI)
REDUCE_TO_PAPER_SIZE
public static final int REDUCE_TO_PAPER_SIZE
Constant value for paper size. Use this value to automatic reduce image bounds to fit the paper size if and
 only if image bounds is larger than the paper size.
 

 Example: `$image.setWidth($diagram.image, -2)`
See Also:
[`setWidth(com.nomagic.magicreport.Image, int)`](#setWidth(com.nomagic.magicreport.Image,int))
[`setWidth(com.nomagic.magicreport.Image, int, boolean)`](#setWidth(com.nomagic.magicreport.Image,int,boolean))
[`setHeight(com.nomagic.magicreport.Image, int)`](#setHeight(com.nomagic.magicreport.Image,int))
[`setHeight(com.nomagic.magicreport.Image, int, boolean)`](#setHeight(com.nomagic.magicreport.Image,int,boolean))
[`setSize(com.nomagic.magicreport.Image, int, int)`](#setSize(com.nomagic.magicreport.Image,int,int))
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.REDUCE_TO_PAPER_SIZE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImageTool
public ImageTool()
Prevent empty initiate.
ImageTool
public ImageTool([ITemplateEngine](../ITemplateEngine.html) engine)
Create an image tool with engine.
Parameters:
`engine` - default global engine
 ============ METHOD DETAIL ========== 
Method Details
setSeparateChar
public void setSeparateChar([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) separateChar)
Set separate character for printing image path. 

 For example. 

 "/" or "\"
Parameters:
`separateChar` - character for printing image path.
scale
public [Image](../../Image.html) scale([Image](../../Image.html) image,
 double sxy)
Convenience method to scale equally in height and width.
Parameters:
`image` - the image to be scaled.
`sxy` - the scaling factor for both height and width
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
scale
public [Image](../../Image.html) scale([Image](../../Image.html) image,
 double sx,
 double sy)
Return the image after scaling transformation. Subsequent rendering is resized according to the specified
 scaling factors relative to the previous scaling.
 Note: new image id is ${old.id}-${sx},${sy}
Parameters:
`image` - report image
`sx` - the amount by which X coordinates in subsequent rendering operations are multiplied relative to
 previous rendering operations.
`sy` - the amount by which Y coordinates in subsequent rendering operations are multiplied relative to
 previous rendering operations.
Returns:
the image after scaling transformation.
See Also:
[`Image`](../../Image.html)
setSize
public [Image](../../Image.html) setSize([Image](../../Image.html) image,
 int width,
 int height)
Return the image from specified width and height.
Parameters:
`image` - report image
`width` - the new width for this image object
`height` - the new height for this image object
Returns:
the image with new size
See Also:
[`Image`](../../Image.html)
setSize
public [Image](../../Image.html) setSize([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height)
Scale the image by the given width/height measurements.
Parameters:
`image` - the image to be scaled.
`width` - the width as in, cm, mm, pt or px
`height` - the height as in, cm, mm, pt or px
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
setSize
public [Image](../../Image.html) setSize([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height,
 boolean overrideAutoSizing)
Scale the image by the given width/height measurements.
Parameters:
`image` - the image to be scaled.
`width` - the width as in, cm, mm, pt or px
`height` - the height as in, cm, mm, pt or px
`overrideAutoSizing` - setSize function will override AutoImageResizing function when true; otherwise, AutoImageResizing option will override set size.
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
setWidth
public [Image](../../Image.html) setWidth([Image](../../Image.html) image,
 int width)
Return the image from specified width. Keep image ratio when transform.
Parameters:
`image` - report image
`width` - the new width for this image object
Returns:
the image with new size
setWidth
public [Image](../../Image.html) setWidth([Image](../../Image.html) image,
 int width,
 boolean keepratio)
Return the image from specified width. If keep ratio is specified, the image will be scaled with proper
 ratio.
Parameters:
`image` - report image
`width` - the new width for this image object
`keepratio` - keep image ratio when true; otherwise false
Returns:
the image with new size
See Also:
[`Image`](../../Image.html)
setWidth
public [Image](../../Image.html) setWidth([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width)
Scale the image by the given width measurements, keeping the ratio.
Parameters:
`image` - the image to be scaled.
`width` - the width as in, cm, mm, pt or px
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
setWidth
public [Image](../../Image.html) setWidth([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) width,
 boolean keepRatio)
Scale the image by the given width measurement, and keep ratio if set.
Parameters:
`image` - the image to be scaled.
`width` - the width as in, cm, mm, pt or px
`keepRatio` - keeps image ratio if set to true
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
setHeight
public [Image](../../Image.html) setHeight([Image](../../Image.html) image,
 int height)
Return the image from specified height. Keep image ratio when transform.
Parameters:
`image` - report image
`height` - the new height for this image object
Returns:
the image with new size
See Also:
[`Image`](../../Image.html)
setHeight
public [Image](../../Image.html) setHeight([Image](../../Image.html) image,
 int height,
 boolean keepratio)
Return the image from specified height. If keep ratio is specified, the image will be scaled with proper
 ratio.
Parameters:
`image` - report image
`height` - the new height for this image object
`keepratio` - keep image ratio when true; otherwise false
Returns:
the image with new size
See Also:
[`Image`](../../Image.html)
setHeight
public [Image](../../Image.html) setHeight([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height)
Scale the image by the given height measurement, keeping the ratio.
Parameters:
`image` - the image to be scaled.
`height` - the height as in, cm, mm, pt or px
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
setHeight
public [Image](../../Image.html) setHeight([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) height,
 boolean keepRatio)
Scale the image by the given height measurement, and keep ratio if set.
Parameters:
`image` - the image to be scaled.
`height` - the height as in, cm, mm, pt or px
`keepRatio` - keeps image ratio if set to true
Returns:
the scaled image
See Also:
[`Image`](../../Image.html)
rotateRight
public [Image](../../Image.html) rotateRight([Image](../../Image.html) image)
Return the image transformed with clockwise rotation transformation.
Parameters:
`image` - report image
Returns:
the transformed image
See Also:
[`Image`](../../Image.html)
rotateLeft
public [Image](../../Image.html) rotateLeft([Image](../../Image.html) image)
Return the image transform with clockwise rotation transformation.
Parameters:
`image` - report image
Returns:
the transformed image
See Also:
[`Image`](../../Image.html)
setDPI
public [ITool.Void](../ITool.Void.html) setDPI(int newDpi)
Sets the DPI value for this document.
Parameters:
`newDpi` - the new dpi value, default is 96.
Returns:
nothing
getDPI
public int getDPI()
setScalingQuality
public [ITool.Void](../ITool.Void.html) setScalingQuality(int quality)
Sets the image scaling quality.
Parameters:
`quality` - a quality level value from 1-5;
Returns:
nothing
See Also:
[`LOWEST`](#LOWEST)
[`LOW`](#LOW)
[`MEDIUM`](#MEDIUM)
[`HIGH`](#HIGH)
[`HIGHEST`](#HIGHEST)
measureToPixel
public int measureToPixel([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) measure)
measureToPixel
public int measureToPixel([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) measure)
Transforms measurements into pixel count.
Parameters:
`measure` - the measurement in inches, cm, mm or pixels
Returns:
the measure in pixels
include
public [Image](../../Image.html) include([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)
 throws [MalformedURLException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html)
Include an external image from local file or URL into report.
 

`$image.include('c:/my document/logo.gif')
 $image.include('http://www.magicdraw.com/images/product_boxes/MD.gif')`
Parameters:
`location` - an image location. Location format can be either URI or system file.
Returns:
the report image
Throws:
`[MalformedURLException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html)` - invalid location format
copy
public [Image](../../Image.html) copy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)
 throws [MalformedURLException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html)
Copy an external image from local file or URL into report.
 

`$image.copy('c:/my document/logo.gif')
 $image.copy('http://www.magicdraw.com/images/product_boxes/MD.gif')`
Parameters:
`location` - an image location. Location format can be either URI or system file.
Returns:
the report image
Throws:
`[MalformedURLException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html)` - invalid location format
calculatePaperWidthHeight
protected float[] calculatePaperWidthHeight()
Deprecated.
see [`getPaperBounds()`](#getPaperBounds())
Calculate the paper width and height.
Returns:
array of paper width and height
getPaperBounds
protected [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getPaperBounds()
Calculate the paper bounds.
Returns:
the bounds of paper
getPaperBounds
protected [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getPaperBounds([Image](../../Image.html) image)
Calculate the paper bounds.
Returns:
the bounds of paper
createFormatterWrapper
protected [IFormatterWrapper](IFormatterWrapper.html) createFormatterWrapper([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> engineClass)
Create the formatter wrapper from given engine class.
Parameters:
`engineClass` - the engine class
Returns:
[`IFormatterWrapper`](IFormatterWrapper.html)
split
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Image](../../Image.html)> split([Image](../../Image.html) image)
Split the image into rows and columns with automatic number of rows and columns, and draw each chunked image
 from left-to-right and top-to-bottom.
Parameters:
`image` - the original image.
Returns:
the array of splitted image order by left-to-right and top-to-bottom.
See Also:
[`split(Image, int, int)`](#split(com.nomagic.magicreport.Image,int,int))
split
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Image](../../Image.html)> split([Image](../../Image.html) image,
 int cols,
 int rows)
Split the image into rows and columns, and draw each chunked image from left-to-right and top-to-bottom. *
 Note:
 new image id is ${old.id};${col},${row}
The [`PAPER_SIZE`](#PAPER_SIZE) will be determined from property [`TemplateConstants.TEMPLATE_INPUT_FORMAT`](../TemplateConstants.html#TEMPLATE_INPUT_FORMAT)
 .
If the [`PAPER_SIZE`](#PAPER_SIZE) is specified but cannot be determined that specific cols or rows won't be
 split.
Parameters:
`image` - the original image.
`cols` - number of columns. Specifies [`PAPER_SIZE`](#PAPER_SIZE) to automatic calculate number of columns from
 paper width.
`rows` - number of rows. Specifies [`PAPER_SIZE`](#PAPER_SIZE) to automatic calculate number of rows from paper
 height.
Returns:
the array of splitted image order by left-to-right and top-to-bottom.
createSilentImage
public [ITool.Void](../ITool.Void.html) createSilentImage([Image](../../Image.html) image)
Create image and do not return any path.
Parameters:
`image` - an image to be created
Returns:
Void
createImageWithRelativePath
public [ITool.RetainedString](../ITool.RetainedString.html) createImageWithRelativePath([Image](../../Image.html) image)
Export image and return relative path of image file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return relative path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
Parameters:
`image` - an image to be created
Returns:
relative path of image file
createImageWithAbsolutePath
public [ITool.RetainedString](../ITool.RetainedString.html) createImageWithAbsolutePath([Image](../../Image.html) image)
Export image and return absolute path of the file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return absolute path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
Parameters:
`image` - an image to be created
Returns:
absolute path and image file
createImageWithAbsolutePath
public [ITool.RetainedString](../ITool.RetainedString.html) createImageWithAbsolutePath([Image](../../Image.html) image,
 boolean includeURI)
Export image and return absolute path of the file. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, the image would be exported on a file system and return absolute path. 

 Use the method with other template types, the image would be exported in a report output and return INVALID path.
Parameters:
`image` - an image to be created
`includeURI` - true to include uri in path
Returns:
absolute path and image file
getRelativePath
public [ITool.RetainedString](../ITool.RetainedString.html) getRelativePath([Image](../../Image.html) image)
Return a possible relative path of image file. 

 This method does not export an image. 

 It returns a possible relative path that the image should be exported to. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, it will return relative path. 

 Use the method with other template types, it will return INVALID path.
Parameters:
`image` - an image
Returns:
relative path of image
getAbsolutePath
public [ITool.RetainedString](../ITool.RetainedString.html) getAbsolutePath([Image](../../Image.html) image)
Return an absolute path of image file. 

 This method does not export an image. 

 It return a possible absolute path that the image should be exported to. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, it will return absolute path. 

 Use the method with other template types, it will return INVALID path.
Parameters:
`image` - an image
Returns:
absolute path of image
getAbsolutePath
public [ITool.RetainedString](../ITool.RetainedString.html) getAbsolutePath([Image](../../Image.html) image,
 boolean includeURI)
Return an absolute path of image file. 

 This method does not export an image. 

 It return a possible absolute path that the image should be exported to. 

 This method is suitable for TXT, HTML and XML template only. 

 Use the method with above template types, it will return absolute path. 

 Use the method with other template types, it will return INVALID path.
Parameters:
`image` - an image
`includeURI` - true to include uri in path
Returns:
absolute path of image
getImageProperty
public [ImageTool.ImageProperty](ImageTool.ImageProperty.html) getImageProperty([Image](../../Image.html) image)
Get ImageProperty object
Parameters:
`image` - current image
Returns:
image with its properties
limitImageSize
public [Image](../../Image.html) limitImageSize([Image](../../Image.html) image)
Limit image size to paper page size.
Parameters:
`image` - image
Returns:
resized image
limitImageSize
public [Image](../../Image.html) limitImageSize([Image](../../Image.html) image,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) maximumWidth,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) maximumHeight)
Limit image size to paper page size and maximum size.
Parameters:
`image` - image
`maximumWidth` - maximum width of image as in, cm, mm, pt or px
`maximumHeight` - maximum height of image as in, cm, mm, pt or px
Returns:
resized image
limitImageSize
public [Image](../../Image.html) limitImageSize([Image](../../Image.html) image,
 int maximumWidthPixel,
 int maximumHeightPixel)
Limit image size to paper page size and maximum size.
Parameters:
`image` - image
`maximumWidthPixel` - maximum width of image as pixel number
`maximumHeightPixel` - maximum height of image as pixel number
Returns:
resized image

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class ImageTool">Class ImageTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.ImageTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ImageTool</span>
<span class="extends-implements">extends <a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">A tool provides functions for manipulate image.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>July 02, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.ImageTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ImageTool.ImageProperty.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool.ImageProperty</a></code></div>
<div class="col-last even-row-color">
<div class="block">Class that store image and its properties e.g., format, path ect.</div>
</div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains a context name.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_DPI">DEFAULT_DPI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The default DPI which is 96.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HIGH">HIGH</a></code></div>
<div class="col-last even-row-color">
<div class="block">The scaling quality high.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HIGHEST">HIGHEST</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The scaling quality highest.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOW">LOW</a></code></div>
<div class="col-last even-row-color">
<div class="block">The scaling quality low.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOWEST">LOWEST</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The scaling quality lowest.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MEDIUM">MEDIUM</a></code></div>
<div class="col-last even-row-color">
<div class="block">The scaling quality medium.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PAPER_SIZE">PAPER_SIZE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constant value for paper size.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REDUCE_TO_PAPER_SIZE">REDUCE_TO_PAPER_SIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constant value for paper size.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#context">context</a>, <a href="../Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#VOID">VOID</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ImageTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Prevent empty initiate.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">ImageTool</a><wbr/>(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create an image tool with engine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected float[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#calculatePaperWidthHeight()">calculatePaperWidthHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">see <a href="#getPaperBounds()"><code>getPaperBounds()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.lang.String)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an external image from local file or URL into report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="IFormatterWrapper.html" title="interface in com.nomagic.magicreport.engine.tools">IFormatterWrapper</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFormatterWrapper(java.lang.Class)">createFormatterWrapper</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; engineClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create the formatter wrapper from given engine class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageWithAbsolutePath(com.nomagic.magicreport.Image)">createImageWithAbsolutePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Export image and return absolute path of the file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return absolute path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageWithAbsolutePath(com.nomagic.magicreport.Image,boolean)">createImageWithAbsolutePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 boolean includeURI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Export image and return absolute path of the file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return absolute path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageWithRelativePath(com.nomagic.magicreport.Image)">createImageWithRelativePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Export image and return relative path of image file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return relative path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSilentImage(com.nomagic.magicreport.Image)">createSilentImage</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create image and do not return any path.<br/></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbsolutePath(com.nomagic.magicreport.Image)">getAbsolutePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an absolute path of image file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbsolutePath(com.nomagic.magicreport.Image,boolean)">getAbsolutePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 boolean includeURI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an absolute path of image file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDPI()">getDPI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ImageTool.ImageProperty.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool.ImageProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageProperty(com.nomagic.magicreport.Image)">getImageProperty</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get ImageProperty object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPaperBounds()">getPaperBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate the paper bounds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPaperBounds(com.nomagic.magicreport.Image)">getPaperBounds</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate the paper bounds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelativePath(com.nomagic.magicreport.Image)">getRelativePath</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a possible relative path of image file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#include(java.lang.String)">include</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Include an external image from local file or URL into report.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#limitImageSize(com.nomagic.magicreport.Image)">limitImageSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Limit image size to paper page size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#limitImageSize(com.nomagic.magicreport.Image,int,int)">limitImageSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int maximumWidthPixel,
 int maximumHeightPixel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Limit image size to paper page size and maximum size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#limitImageSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String)">limitImageSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maximumWidth,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maximumHeight)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Limit image size to paper page size and maximum size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#measureToPixel(com.nomagic.magicreport.Image,java.lang.String)">measureToPixel</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> measure)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Transforms measurements into pixel count.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#measureToPixel(java.lang.String)">measureToPixel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> measure)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rotateLeft(com.nomagic.magicreport.Image)">rotateLeft</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image transform with clockwise rotation transformation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rotateRight(com.nomagic.magicreport.Image)">rotateRight</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image transformed with clockwise rotation transformation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#scale(com.nomagic.magicreport.Image,double)">scale</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sxy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convenience method to scale equally in height and width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#scale(com.nomagic.magicreport.Image,double,double)">scale</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sx,
 double sy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image after scaling transformation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDPI(int)">setDPI</a><wbr/>(int newDpi)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the DPI value for this document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(com.nomagic.magicreport.Image,int)">setHeight</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image from specified height.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(com.nomagic.magicreport.Image,int,boolean)">setHeight</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int height,
 boolean keepratio)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image from specified height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(com.nomagic.magicreport.Image,java.lang.String)">setHeight</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given height measurement, keeping the ratio.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(com.nomagic.magicreport.Image,java.lang.String,boolean)">setHeight</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height,
 boolean keepRatio)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given height measurement, and keep ratio if set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setScalingQuality(int)">setScalingQuality</a><wbr/>(int quality)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the image scaling quality.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeparateChar(java.lang.String)">setSeparateChar</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separateChar)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set separate character for printing image path.<br/>
 For example.<br/>
 "/" or "\"</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(com.nomagic.magicreport.Image,int,int)">setSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image from specified width and height.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String)">setSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given width/height measurements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String,boolean)">setSize</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height,
 boolean overrideAutoSizing)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given width/height measurements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(com.nomagic.magicreport.Image,int)">setWidth</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image from specified width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(com.nomagic.magicreport.Image,int,boolean)">setWidth</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width,
 boolean keepratio)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the image from specified width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(com.nomagic.magicreport.Image,java.lang.String)">setWidth</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given width measurements, keeping the ratio.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(com.nomagic.magicreport.Image,java.lang.String,boolean)">setWidth</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 boolean keepRatio)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scale the image by the given width measurement, and keep ratio if set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#split(com.nomagic.magicreport.Image)">split</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Split the image into rows and columns with automatic number of rows and columns, and draw each chunked image
 from left-to-right and top-to-bottom.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#split(com.nomagic.magicreport.Image,int,int)">split</a><wbr/>(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int cols,
 int rows)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Split the image into rows and columns, and draw each chunked image from left-to-right and top-to-bottom.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#clone()">clone</a>, <a href="../Tool.html#getContext()">getContext</a>, <a href="../Tool.html#getProperties()">getProperties</a>, <a href="../Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#clearTool()">clearTool</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="CONTEXT_NAME">
<h3>CONTEXT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.CONTEXT_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOWEST">
<h3>LOWEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LOWEST</span></div>
<div class="block">The scaling quality lowest. Current implementation is interpolation nearest neighbor.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.LOWEST">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOW">
<h3>LOW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LOW</span></div>
<div class="block">The scaling quality low. Current implementation is one step interpolation bi-linear.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.LOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEDIUM">
<h3>MEDIUM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MEDIUM</span></div>
<div class="block">The scaling quality medium. Current implementation is interpolation bi-cubic.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.MEDIUM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIGH">
<h3>HIGH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">HIGH</span></div>
<div class="block">The scaling quality high. Current implementation is multi-steps interpolation bi-linear.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.HIGH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIGHEST">
<h3>HIGHEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">HIGHEST</span></div>
<div class="block">The scaling quality highest. Current implementation is area average image scaling algorithm. (Default value)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.HIGHEST">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PAPER_SIZE">
<h3>PAPER_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PAPER_SIZE</span></div>
<div class="block">Constant value for paper size. Use this value to set image dimension to paper size.
 <br/>
 Example: <pre><code>
    $image.setWidth($diagram.image, -1)
 </code></pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setWidth(com.nomagic.magicreport.Image,int)"><code>setWidth(com.nomagic.magicreport.Image, int)</code></a></li>
<li><a href="#setWidth(com.nomagic.magicreport.Image,int,boolean)"><code>setWidth(com.nomagic.magicreport.Image, int, boolean)</code></a></li>
<li><a href="#setHeight(com.nomagic.magicreport.Image,int)"><code>setHeight(com.nomagic.magicreport.Image, int)</code></a></li>
<li><a href="#setHeight(com.nomagic.magicreport.Image,int,boolean)"><code>setHeight(com.nomagic.magicreport.Image, int, boolean)</code></a></li>
<li><a href="#setSize(com.nomagic.magicreport.Image,int,int)"><code>setSize(com.nomagic.magicreport.Image, int, int)</code></a></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.PAPER_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_DPI">
<h3>DEFAULT_DPI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_DPI</span></div>
<div class="block">The default DPI which is 96.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.DEFAULT_DPI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REDUCE_TO_PAPER_SIZE">
<h3>REDUCE_TO_PAPER_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">REDUCE_TO_PAPER_SIZE</span></div>
<div class="block">Constant value for paper size. Use this value to automatic reduce image bounds to fit the paper size if and
 only if image bounds is larger than the paper size.
 <br/>
 Example: <pre><code>
    $image.setWidth($diagram.image, -2)
 </code></pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setWidth(com.nomagic.magicreport.Image,int)"><code>setWidth(com.nomagic.magicreport.Image, int)</code></a></li>
<li><a href="#setWidth(com.nomagic.magicreport.Image,int,boolean)"><code>setWidth(com.nomagic.magicreport.Image, int, boolean)</code></a></li>
<li><a href="#setHeight(com.nomagic.magicreport.Image,int)"><code>setHeight(com.nomagic.magicreport.Image, int)</code></a></li>
<li><a href="#setHeight(com.nomagic.magicreport.Image,int,boolean)"><code>setHeight(com.nomagic.magicreport.Image, int, boolean)</code></a></li>
<li><a href="#setSize(com.nomagic.magicreport.Image,int,int)"><code>setSize(com.nomagic.magicreport.Image, int, int)</code></a></li>
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.ImageTool.REDUCE_TO_PAPER_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ImageTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageTool</span>()</div>
<div class="block">Prevent empty initiate.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>ImageTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageTool</span><wbr/><span class="parameters">(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</span></div>
<div class="block">Create an image tool with engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - default global engine</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="setSeparateChar(java.lang.String)">
<h3>setSeparateChar</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeparateChar</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separateChar)</span></div>
<div class="block">Set separate character for printing image path.<br/>
 For example.<br/>
 "/" or "\"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>separateChar</code> - character for printing image path.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scale(com.nomagic.magicreport.Image,double)">
<h3>scale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">scale</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sxy)</span></div>
<div class="block">Convenience method to scale equally in height and width.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>sxy</code> - the scaling factor for both height and width</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scale(com.nomagic.magicreport.Image,double,double)">
<h3>scale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">scale</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 double sx,
 double sy)</span></div>
<div class="block">Return the image after scaling transformation. Subsequent rendering is resized according to the specified
 scaling factors relative to the previous scaling.
 <p>
 Note: new image id is ${old.id}-${sx},${sy}</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>sx</code> - the amount by which X coordinates in subsequent rendering operations are multiplied relative to
           previous rendering operations.</dd>
<dd><code>sy</code> - the amount by which Y coordinates in subsequent rendering operations are multiplied relative to
           previous rendering operations.</dd>
<dt>Returns:</dt>
<dd>the image after scaling transformation.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSize(com.nomagic.magicreport.Image,int,int)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width,
 int height)</span></div>
<div class="block">Return the image from specified width and height.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>width</code> - the new width for this image object</dd>
<dd><code>height</code> - the new height for this image object</dd>
<dt>Returns:</dt>
<dd>the image with new size</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height)</span></div>
<div class="block">Scale the image by the given width/height measurements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>width</code> - the width as in, cm, mm, pt or px</dd>
<dd><code>height</code> - the height as in, cm, mm, pt or px</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String,boolean)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height,
 boolean overrideAutoSizing)</span></div>
<div class="block">Scale the image by the given width/height measurements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>width</code> - the width as in, cm, mm, pt or px</dd>
<dd><code>height</code> - the height as in, cm, mm, pt or px</dd>
<dd><code>overrideAutoSizing</code> - setSize function will override AutoImageResizing function when true; otherwise, AutoImageResizing option will override set size.</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(com.nomagic.magicreport.Image,int)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width)</span></div>
<div class="block">Return the image from specified width. Keep image ratio when transform.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>width</code> - the new width for this image object</dd>
<dt>Returns:</dt>
<dd>the image with new size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(com.nomagic.magicreport.Image,int,boolean)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int width,
 boolean keepratio)</span></div>
<div class="block">Return the image from specified width. If keep ratio is specified, the image will be scaled with proper
 ratio.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>width</code> - the new width for this image object</dd>
<dd><code>keepratio</code> - keep image ratio when true; otherwise false</dd>
<dt>Returns:</dt>
<dd>the image with new size</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(com.nomagic.magicreport.Image,java.lang.String)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width)</span></div>
<div class="block">Scale the image by the given width measurements, keeping the ratio.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>width</code> - the width as in, cm, mm, pt or px</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(com.nomagic.magicreport.Image,java.lang.String,boolean)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> width,
 boolean keepRatio)</span></div>
<div class="block">Scale the image by the given width measurement, and keep ratio if set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>width</code> - the width as in, cm, mm, pt or px</dd>
<dd><code>keepRatio</code> - keeps image ratio if set to true</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(com.nomagic.magicreport.Image,int)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int height)</span></div>
<div class="block">Return the image from specified height. Keep image ratio when transform.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>height</code> - the new height for this image object</dd>
<dt>Returns:</dt>
<dd>the image with new size</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(com.nomagic.magicreport.Image,int,boolean)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int height,
 boolean keepratio)</span></div>
<div class="block">Return the image from specified height. If keep ratio is specified, the image will be scaled with proper
 ratio.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dd><code>height</code> - the new height for this image object</dd>
<dd><code>keepratio</code> - keep image ratio when true; otherwise false</dd>
<dt>Returns:</dt>
<dd>the image with new size</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(com.nomagic.magicreport.Image,java.lang.String)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height)</span></div>
<div class="block">Scale the image by the given height measurement, keeping the ratio.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>height</code> - the height as in, cm, mm, pt or px</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(com.nomagic.magicreport.Image,java.lang.String,boolean)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> height,
 boolean keepRatio)</span></div>
<div class="block">Scale the image by the given height measurement, and keep ratio if set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the image to be scaled.</dd>
<dd><code>height</code> - the height as in, cm, mm, pt or px</dd>
<dd><code>keepRatio</code> - keeps image ratio if set to true</dd>
<dt>Returns:</dt>
<dd>the scaled image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotateRight(com.nomagic.magicreport.Image)">
<h3>rotateRight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">rotateRight</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Return the image transformed with clockwise rotation transformation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dt>Returns:</dt>
<dd>the transformed image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotateLeft(com.nomagic.magicreport.Image)">
<h3>rotateLeft</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">rotateLeft</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Return the image transform with clockwise rotation transformation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - report image</dd>
<dt>Returns:</dt>
<dd>the transformed image</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../Image.html" title="class in com.nomagic.magicreport"><code>Image</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDPI(int)">
<h3>setDPI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">setDPI</span><wbr/><span class="parameters">(int newDpi)</span></div>
<div class="block">Sets the DPI value for this document.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newDpi</code> - the new dpi value, default is 96.</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDPI()">
<h3>getDPI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDPI</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setScalingQuality(int)">
<h3>setScalingQuality</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">setScalingQuality</span><wbr/><span class="parameters">(int quality)</span></div>
<div class="block">Sets the image scaling quality.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>quality</code> - a quality level value from 1-5;</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#LOWEST"><code>LOWEST</code></a></li>
<li><a href="#LOW"><code>LOW</code></a></li>
<li><a href="#MEDIUM"><code>MEDIUM</code></a></li>
<li><a href="#HIGH"><code>HIGH</code></a></li>
<li><a href="#HIGHEST"><code>HIGHEST</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="measureToPixel(java.lang.String)">
<h3>measureToPixel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">measureToPixel</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> measure)</span></div>
</section>
</li>
<li>
<section class="detail" id="measureToPixel(com.nomagic.magicreport.Image,java.lang.String)">
<h3>measureToPixel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">measureToPixel</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> measure)</span></div>
<div class="block">Transforms measurements into pixel count.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>measure</code> - the measurement in inches, cm, mm or pixels</dd>
<dt>Returns:</dt>
<dd>the measure in pixels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="include(java.lang.String)">
<h3>include</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">include</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span>
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html" title="class or interface in java.net">MalformedURLException</a></span></div>
<div class="block">Include an external image from local file or URL into report.
 <br/>
<pre><code>
    $image.include('c:/my document/logo.gif')
    $image.include('http://www.magicdraw.com/images/product_boxes/MD.gif')
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - an image location. Location format can be either URI or system file.</dd>
<dt>Returns:</dt>
<dd>the report image</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html" title="class or interface in java.net">MalformedURLException</a></code> - invalid location format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html" title="class or interface in java.net">MalformedURLException</a></span></div>
<div class="block">Copy an external image from local file or URL into report.
 <br/>
<pre><code>
 $image.copy('c:/my document/logo.gif')
 $image.copy('http://www.magicdraw.com/images/product_boxes/MD.gif')
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - an image location. Location format can be either URI or system file.</dd>
<dt>Returns:</dt>
<dd>the report image</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/MalformedURLException.html" title="class or interface in java.net">MalformedURLException</a></code> - invalid location format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculatePaperWidthHeight()">
<h3>calculatePaperWidthHeight</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">float[]</span> <span class="element-name">calculatePaperWidthHeight</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">see <a href="#getPaperBounds()"><code>getPaperBounds()</code></a></div>
</div>
<div class="block">Calculate the paper width and height.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>array of paper width and height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaperBounds()">
<h3>getPaperBounds</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getPaperBounds</span>()</div>
<div class="block">Calculate the paper bounds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the bounds of paper</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaperBounds(com.nomagic.magicreport.Image)">
<h3>getPaperBounds</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getPaperBounds</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Calculate the paper bounds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the bounds of paper</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFormatterWrapper(java.lang.Class)">
<h3>createFormatterWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="IFormatterWrapper.html" title="interface in com.nomagic.magicreport.engine.tools">IFormatterWrapper</a></span> <span class="element-name">createFormatterWrapper</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; engineClass)</span></div>
<div class="block">Create the formatter wrapper from given engine class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineClass</code> - the engine class</dd>
<dt>Returns:</dt>
<dd><a href="IFormatterWrapper.html" title="interface in com.nomagic.magicreport.engine.tools"><code>IFormatterWrapper</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="split(com.nomagic.magicreport.Image)">
<h3>split</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a>&gt;</span> <span class="element-name">split</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Split the image into rows and columns with automatic number of rows and columns, and draw each chunked image
 from left-to-right and top-to-bottom.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the original image.</dd>
<dt>Returns:</dt>
<dd>the array of splitted image order by left-to-right and top-to-bottom.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#split(com.nomagic.magicreport.Image,int,int)"><code>split(Image, int, int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="split(com.nomagic.magicreport.Image,int,int)">
<h3>split</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a>&gt;</span> <span class="element-name">split</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int cols,
 int rows)</span></div>
<div class="block">Split the image into rows and columns, and draw each chunked image from left-to-right and top-to-bottom. *
 <p>
 Note:
 <ul>
<li>new image id is ${old.id};${col},${row}</li>
<li>The <a href="#PAPER_SIZE"><code>PAPER_SIZE</code></a> will be determined from property <a href="../TemplateConstants.html#TEMPLATE_INPUT_FORMAT"><code>TemplateConstants.TEMPLATE_INPUT_FORMAT</code></a>
 .</li>
<li>If the <a href="#PAPER_SIZE"><code>PAPER_SIZE</code></a> is specified but cannot be determined that specific cols or rows won't be
 split.
 </li></ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the original image.</dd>
<dd><code>cols</code> - number of columns. Specifies <a href="#PAPER_SIZE"><code>PAPER_SIZE</code></a> to automatic calculate number of columns from
           paper width.</dd>
<dd><code>rows</code> - number of rows. Specifies <a href="#PAPER_SIZE"><code>PAPER_SIZE</code></a> to automatic calculate number of rows from paper
           height.</dd>
<dt>Returns:</dt>
<dd>the array of splitted image order by left-to-right and top-to-bottom.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSilentImage(com.nomagic.magicreport.Image)">
<h3>createSilentImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">createSilentImage</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Create image and do not return any path.<br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image to be created</dd>
<dt>Returns:</dt>
<dd>Void</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageWithRelativePath(com.nomagic.magicreport.Image)">
<h3>createImageWithRelativePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">createImageWithRelativePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Export image and return relative path of image file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return relative path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image to be created</dd>
<dt>Returns:</dt>
<dd>relative path of image file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageWithAbsolutePath(com.nomagic.magicreport.Image)">
<h3>createImageWithAbsolutePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">createImageWithAbsolutePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Export image and return absolute path of the file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return absolute path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image to be created</dd>
<dt>Returns:</dt>
<dd>absolute path and image file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageWithAbsolutePath(com.nomagic.magicreport.Image,boolean)">
<h3>createImageWithAbsolutePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">createImageWithAbsolutePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 boolean includeURI)</span></div>
<div class="block">Export image and return absolute path of the file.<br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, the image would be exported on a file system and return absolute path.<br/>
 Use the method with other template types, the image would be exported in a report output and return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image to be created</dd>
<dd><code>includeURI</code> - true to include uri in path</dd>
<dt>Returns:</dt>
<dd>absolute path and image file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelativePath(com.nomagic.magicreport.Image)">
<h3>getRelativePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">getRelativePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Return a possible relative path of image file. <br/>
 This method does not export an image. <br/>
 It returns a possible relative path that the image should be exported to. <br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, it will return relative path.<br/>
 Use the method with other template types, it will return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image</dd>
<dt>Returns:</dt>
<dd>relative path of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbsolutePath(com.nomagic.magicreport.Image)">
<h3>getAbsolutePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">getAbsolutePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Return an absolute path of image file. <br/>
 This method does not export an image. <br/>
 It return a possible absolute path that the image should be exported to. <br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, it will return absolute path.<br/>
 Use the method with other template types, it will return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image</dd>
<dt>Returns:</dt>
<dd>absolute path of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbsolutePath(com.nomagic.magicreport.Image,boolean)">
<h3>getAbsolutePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">getAbsolutePath</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 boolean includeURI)</span></div>
<div class="block">Return an absolute path of image file. <br/>
 This method does not export an image. <br/>
 It return a possible absolute path that the image should be exported to. <br/>
 This method is suitable for TXT, HTML and XML template only.<br/>
 Use the method with above template types, it will return absolute path.<br/>
 Use the method with other template types, it will return INVALID path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - an image</dd>
<dd><code>includeURI</code> - true to include uri in path</dd>
<dt>Returns:</dt>
<dd>absolute path of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageProperty(com.nomagic.magicreport.Image)">
<h3>getImageProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ImageTool.ImageProperty.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool.ImageProperty</a></span> <span class="element-name">getImageProperty</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Get ImageProperty object</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - current image</dd>
<dt>Returns:</dt>
<dd>image with its properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="limitImageSize(com.nomagic.magicreport.Image)">
<h3>limitImageSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">limitImageSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image)</span></div>
<div class="block">Limit image size to paper page size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
<dt>Returns:</dt>
<dd>resized image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="limitImageSize(com.nomagic.magicreport.Image,java.lang.String,java.lang.String)">
<h3>limitImageSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">limitImageSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maximumWidth,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> maximumHeight)</span></div>
<div class="block">Limit image size to paper page size and maximum size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
<dd><code>maximumWidth</code> - maximum width of image as in, cm, mm, pt or px</dd>
<dd><code>maximumHeight</code> - maximum height of image as in, cm, mm, pt or px</dd>
<dt>Returns:</dt>
<dd>resized image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="limitImageSize(com.nomagic.magicreport.Image,int,int)">
<h3>limitImageSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">limitImageSize</span><wbr/><span class="parameters">(<a href="../../Image.html" title="class in com.nomagic.magicreport">Image</a> image,
 int maximumWidthPixel,
 int maximumHeightPixel)</span></div>
<div class="block">Limit image size to paper page size and maximum size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
<dd><code>maximumWidthPixel</code> - maximum width of image as pixel number</dd>
<dd><code>maximumHeightPixel</code> - maximum height of image as pixel number</dd>
<dt>Returns:</dt>
<dd>resized image</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
