# JAVA OPENAPI: Image (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/Image.html
- source_path: `com/nomagic/magicreport/Image.html`
- source_sha256: `b46608ef333d8beef6c7f748e7cb8d87a70b2db352b65ba2c5839da5e0b3c311`
- captured_utc: `2026-07-14T16:46:11.393952+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class Image

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.Image

All Implemented Interfaces:
`[IObserverMessage](engine/IObserverMessage.html)`, `[IVariable](IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ReportSVGIcon](ReportSVGIcon.html)`, `[SVGIcon](SVGIcon.html)`

@OpenApiAllpublic classImage
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IObserverMessage](engine/IObserverMessage.html), [IVariable](IVariable.html), [Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)

An bean represent image object for template. If dispose was set, the engine will dispose image data after image
 has been exported to report.

Since:
Jul 2, 2007
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.Image)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[FIT_PAPER](#FIT_PAPER)`
Constants bit for image transformation (auto fit).
`static final int`
`[FORCE_ROTATE](#FORCE_ROTATE)`
Constants bit for force rotate
`static final int`
`[FORCE_ROTATE_LEFT](#FORCE_ROTATE_LEFT)`
Constants bit for force rotate (rotate left).
`static final int`
`[FORCE_ROTATE_RIGHT](#FORCE_ROTATE_RIGHT)`
Constants bit for force rotate (rotate right).
`static final int`
`[IMAGE_TYPE_ICON](#IMAGE_TYPE_ICON)`

`static final int`
`[IMAGE_TYPE_IMAGE](#IMAGE_TYPE_IMAGE)`
Constants for image type that is created as icon or image
`static final int`
`[LARGE_ONLY](#LARGE_ONLY)`
Constants bit for image transformation (perform operation only when image is large only).
`static final int`
`[MAINTAIN_RATIO](#MAINTAIN_RATIO)`
Constants bit for image transformation (maintain ratio).
`static final int`
`[ROTATE_LEFT](#ROTATE_LEFT)`
Constants bit for image transformation (rotate left).
`static final int`
`[ROTATE_RIGHT](#ROTATE_RIGHT)`
Constants bit for image transformation (rotate right).
`static final int`
`[TRUE_TRANSFORM](#TRUE_TRANSFORM)`
Constants bit for image transformation (physically transform image instead of use document feature).
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Image](#%3Cinit%3E(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 boolean disposeAfterUse)`
Create a new image from buffered image.
`[Image](#%3Cinit%3E(java.lang.String,java.io.File,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile,
 boolean disposeAfterUse)`
Create a new image from file.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
Creates and returns a copy of this object.
`[Image](Image.html)`
`[createOriginal](#createOriginal())()`
Create a new instance of original image.
`void`
`[dispose](#dispose())()`
Disposes of this image buffer context and releases any system resources that it is using.
`void`
`[ensureOriginal](#ensureOriginal())()`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Indicates whether some other object is "equal to" this one.
`void`
`[flush](#flush())()`
Flush current buffered image from [`getData()`](#getData()) into file stream.
`void`
`[flush](#flush(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) track)`
Flush current buffered image from [`getData()`](#getData()) into file stream.
`[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Returns the bounding Rectangle of this Image.
`[BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[getData](#getData())()`
Return a data.
`int`
`[getDpi](#getDpi())()`

`int`
`[getHeight](#getHeight())()`
Return the height of image in pixels.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`
Return a id.
`[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getImageFile](#getImageFile())()`
Return a imageFile.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getImageFormat](#getImageFormat())()`
Return an image format.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getImageFormatToWrite](#getImageFormatToWrite())()`

`int`
`[getImageType](#getImageType())()`
Get image type.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Return a name.
`[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getOriginalBounds](#getOriginalBounds())()`
Returns the original bounding Rectangle of this Image.
`int`
`[getOriginalHeight](#getOriginalHeight())()`
Return a original height.
`[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getOriginalImageFile](#getOriginalImageFile())()`
Return an original image file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOriginalImageFormat](#getOriginalImageFormat())()`
Return an original image format.
`int`
`[getOriginalWidth](#getOriginalWidth())()`
Return a original width.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[getProperties](#getProperties())()`

`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Searches for the property with the specified key in this property list.
`int`
`[getSize](#getSize())()`
Returns the size of image in pixels.
`int`
`[getTransformationOption](#getTransformationOption())()`
Return a transformation flag.
`int`
`[getWidth](#getWidth())()`
Return the width of image in pixels.
`int`
`[hashCode](#hashCode())()`
Returns a hash code value for the object.
`boolean`
`[isChanged](#isChanged())()`
Return a changed.
`boolean`
`[isDisposeAfterUse](#isDisposeAfterUse())()`
Return a dispose setting.
`boolean`
`[isTransformWithOption](#isTransformWithOption(int))(int option)`
Test if image transformation option is set to given option.
`[BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[readData](#readData())()`
Read a buffered image from this instance.
`void`
`[rotate](#rotate(boolean))(boolean clockwise)`
Rotate image in clockwise or anti-clockwise.
`void`
`[setChanged](#setChanged(boolean))(boolean changed)`
If `false`, dispose image buffer and mark a status.
`void`
`[setData](#setData(java.awt.image.BufferedImage))([BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data)`
Set a data.
`void`
`[setDisposeAfterUse](#setDisposeAfterUse(boolean))(boolean disposeAfterUse)`
Set image data to be disposed after generating report.
`void`
`[setDpi](#setDpi(int))(int dpi)`

`void`
`[setHeight](#setHeight(int))(int height)`
Set height of image in pixels.
`void`
`[setId](#setId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Set a id.
`void`
`[setImageFile](#setImageFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile)`
Set a imageFile.
`void`
`[setImageFormat](#setImageFormat(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat)`
Set an image format.
`void`
`[setImageType](#setImageType(int))(int imageType)`
Set image type.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Set a name.
`void`
`[setOriginalHeight](#setOriginalHeight(int))(int originalHeight)`

`void`
`[setOriginalImageFile](#setOriginalImageFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) originalImageFile)`

`void`
`[setOriginalImageFormat](#setOriginalImageFormat(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) originalImageFormat)`
Set an original image format.
`void`
`[setOriginalWidth](#setOriginalWidth(int))(int originalWidth)`

`void`
`[setProperties](#setProperties(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> properties)`

`void`
`[setProperty](#setProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set an image property.
`void`
`[setTransformationOption](#setTransformationOption(int))(int transformationOption)`
Set a transformation option.
`void`
`[setWidth](#setWidth(int))(int width)`
Set width of image in pixels.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns a string representation of the object.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
FIT_PAPER
public static final int FIT_PAPER
Constants bit for image transformation (auto fit).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.FIT_PAPER)
MAINTAIN_RATIO
public static final int MAINTAIN_RATIO
Constants bit for image transformation (maintain ratio).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.MAINTAIN_RATIO)
ROTATE_LEFT
public static final int ROTATE_LEFT
Constants bit for image transformation (rotate left).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.ROTATE_LEFT)
ROTATE_RIGHT
public static final int ROTATE_RIGHT
Constants bit for image transformation (rotate right).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.ROTATE_RIGHT)
LARGE_ONLY
public static final int LARGE_ONLY
Constants bit for image transformation (perform operation only when image is large only).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.LARGE_ONLY)
IMAGE_TYPE_IMAGE
public static final int IMAGE_TYPE_IMAGE
Constants for image type that is created as icon or image
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.IMAGE_TYPE_IMAGE)
IMAGE_TYPE_ICON
public static final int IMAGE_TYPE_ICON
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.IMAGE_TYPE_ICON)
TRUE_TRANSFORM
public static final int TRUE_TRANSFORM
Constants bit for image transformation (physically transform image instead of use document feature).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.TRUE_TRANSFORM)
FORCE_ROTATE_LEFT
public static final int FORCE_ROTATE_LEFT
Constants bit for force rotate (rotate left).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE_LEFT)
FORCE_ROTATE_RIGHT
public static final int FORCE_ROTATE_RIGHT
Constants bit for force rotate (rotate right).
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE_RIGHT)
FORCE_ROTATE
public static final int FORCE_ROTATE
Constants bit for force rotate
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Image
public Image([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile,
 boolean disposeAfterUse)
Create a new image from file. If `disposeAfterUse` is true, image will be disposed immediately
 after print into report.
 Generally, same image will be used only once in the template, it's recommend to set
 `disposeAfterUse` to true.
Parameters:
`id` - image id
`imageFile` - image file.
`disposeAfterUse` - if true, dispose an image after use.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if image file is null
Image
public Image([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat,
 boolean disposeAfterUse)
Create a new image from buffered image. If `disposeAfterUse` is true, image will be disposed
 immediately after print into report.
 Generally, same image will be used only once in the template, it's recommend to set
 `disposeAfterUse` to true.
 `data` can be null.
Parameters:
`id` - image id
`data` - the image data
`imageFormat` - the image format.
`disposeAfterUse` - if true, dispose an image after use.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if image format is null
 ============ METHOD DETAIL ========== 
Method Details
getProperties
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> getProperties()
setProperties
public void setProperties([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> properties)
setOriginalImageFile
public void setOriginalImageFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) originalImageFile)
setOriginalWidth
public void setOriginalWidth(int originalWidth)
setOriginalHeight
public void setOriginalHeight(int originalHeight)
getId
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getId()
Return a id.
Returns:
the id
setId
public void setId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Set a id.
Parameters:
`id` - the id to set
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Return a name.
Specified by:
`[getName](engine/IObserverMessage.html#getName())` in interface `[IObserverMessage](engine/IObserverMessage.html)`
Returns:
the name
setName
public void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Set a name.
Parameters:
`name` - the name to set
getData
public [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) getData()
Return a data.
Returns:
the data
setData
public void setData([BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) data)
Set a data.
Parameters:
`data` - the data to set
getImageFormat
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getImageFormat()
Return an image format.
Returns:
the image format
setImageFormat
public void setImageFormat([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageFormat)
Set an image format.
Parameters:
`imageFormat` - the image format to set
getOriginalImageFormat
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOriginalImageFormat()
Return an original image format.
 For external image file, it may have real format that different to file extension
Returns:
the original image format
setOriginalImageFormat
public void setOriginalImageFormat([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) originalImageFormat)
Set an original image format.
 For external image file, it may have real format that different to file extension
Parameters:
`originalImageFormat` - the original image format to set
setProperty
public void setProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set an image property.
Parameters:
`key` - the key to be placed into this property list.
`value` - the value corresponding to key.
getProperty
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Searches for the property with the specified key in this property list. The method returns `null`
 if the property is not found.
Parameters:
`key` - the property key.
Returns:
the value in this property list with the specified key value.
See Also:
[`setProperty(String, Object)`](#setProperty(java.lang.String,java.lang.Object))
isChanged
public boolean isChanged()
Return a changed.
Returns:
the changed
setChanged
public void setChanged(boolean changed)
If `false`, dispose image buffer and mark a status. Developer should detect an image status
 before retrieve a new buffer from [`getData()`](#getData()).
Parameters:
`changed` - the changed to set
See Also:
[`isChanged()`](#isChanged())
readData
public [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) readData()
Read a buffered image from this instance. Return BufferedImage if [`getData()`](#getData()) contains data or read
 from [`getImageFile()`](#getImageFile()).
Returns:
a buffered image from [`getData()`](#getData()) or [`getImageFile()`](#getImageFile())
flush
public void flush()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Flush current buffered image from [`getData()`](#getData()) into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when this object is garbage collected.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to flush the data.
See Also:
[`getData()`](#getData())
[`getImageFile()`](#getImageFile())
[`flush(Object)`](#flush(java.lang.Object))
flush
public void flush([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) track)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Flush current buffered image from [`getData()`](#getData()) into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when tracked object is garbage collected.
Parameters:
`track` - the marker object track flushed file, deleting the file when the marker instance is garbage
 collected.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to flush the data.
See Also:
[`getData()`](#getData())
[`getImageFile()`](#getImageFile())
[`flush()`](#flush())
dispose
public void dispose()
Disposes of this image buffer context and releases any system resources that it is using.
getSize
public int getSize()
Returns the size of image in pixels.
Returns:
the size of image in pixels.
getBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Returns the bounding Rectangle of this Image.
 If image contains no data buffer [`readData()`](#readData()) return null, the bounds will be calculated
 from [`getWidth()`](#getWidth()) and [`getHeight()`](#getHeight()). 

 If image contains buffer data, calculate the bounds from buffer data.
Returns:
the bounding box of this image.
setWidth
public void setWidth(int width)
Set width of image in pixels.
Parameters:
`width` - width of image
getWidth
public int getWidth()
Return the width of image in pixels.
Returns:
the width of image in pixels
setHeight
public void setHeight(int height)
Set height of image in pixels.
Parameters:
`height` - height of image in pixels
getHeight
public int getHeight()
Return the height of image in pixels.
Returns:
the height of image in pixels
getImageFile
public [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getImageFile()
Return a imageFile.
Returns:
the imageFile
setImageFile
public void setImageFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) imageFile)
Set a imageFile.
Parameters:
`imageFile` - the imageFile to set
isDisposeAfterUse
public boolean isDisposeAfterUse()
Return a dispose setting.
Returns:
the dispose setting
setDisposeAfterUse
public void setDisposeAfterUse(boolean disposeAfterUse)
Set image data to be disposed after generating report.
Parameters:
`disposeAfterUse` - set value to true to allow engine to dispose image data.
getOriginalImageFile
public [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getOriginalImageFile()
Return an original image file.
Returns:
the original image file
getOriginalWidth
public int getOriginalWidth()
Return a original width.
Returns:
the original width
getOriginalHeight
public int getOriginalHeight()
Return a original height.
Returns:
the original height
getOriginalBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getOriginalBounds()
Returns the original bounding Rectangle of this Image.
Returns:
the original bounding box of this image.
getTransformationOption
public int getTransformationOption()
Return a transformation flag.
Returns:
the transformation flag
setTransformationOption
public void setTransformationOption(int transformationOption)
Set a transformation option.
Parameters:
`transformationOption` - the transformation option to set
isTransformWithOption
public boolean isTransformWithOption(int option)
Test if image transformation option is set to given option.
Parameters:
`option` - test option
Returns:
true if image transformation option is set to given option.
rotate
public void rotate(boolean clockwise)
Rotate image in clockwise or anti-clockwise.
Parameters:
`clockwise` - true for clockwise; false for anti-clockwise
createOriginal
public [Image](Image.html) createOriginal()
Create a new instance of original image.
Returns:
a new instance of original image.
ensureOriginal
public void ensureOriginal()
hashCode
public int hashCode()
Returns a hash code value for the object.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a hash code value for this object.
See Also:
[`Object.hashCode()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Indicates whether some other object is "equal to" this one.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Parameters:
`obj` - the reference object with which to compare.
Returns:
`true` if this object is the same as the obj argument; `false` otherwise.
See Also:
[`Object.equals(java.lang.Object)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))
clone
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) clone()
 throws [CloneNotSupportedException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html)
Creates and returns a copy of this object.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a copy of this instance
Throws:
`[CloneNotSupportedException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html)` - if the object's class does not support the `Cloneable`
 interface.
See Also:
[`Object.clone()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Returns a string representation of the object.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a string representation of the object.
getImageType
public int getImageType()
Get image type. For example : icon image from $report.getIconFor(), image from $element.image
Returns:
image type
setImageType
public void setImageType(int imageType)
Set image type. For example : icon image from $report.getIconFor(), image from $element.image
Parameters:
`imageType` - image type
getImageFormatToWrite
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getImageFormatToWrite()
getDpi
public int getDpi()
setDpi
public void setDpi(int dpi)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class Image">Class Image</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.Image</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code>, <code><a href="IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ReportSVGIcon.html" title="class in com.nomagic.magicreport">ReportSVGIcon</a></code>, <code><a href="SVGIcon.html" title="class in com.nomagic.magicreport">SVGIcon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Image</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a>, <a href="IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">An bean represent image object for template. If dispose was set, the engine will dispose image data after image
 has been exported to report.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jul 2, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.Image">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FIT_PAPER">FIT_PAPER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants bit for image transformation (auto fit).</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FORCE_ROTATE">FORCE_ROTATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants bit for force rotate</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FORCE_ROTATE_LEFT">FORCE_ROTATE_LEFT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants bit for force rotate (rotate left).</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FORCE_ROTATE_RIGHT">FORCE_ROTATE_RIGHT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants bit for force rotate (rotate right).</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IMAGE_TYPE_ICON">IMAGE_TYPE_ICON</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IMAGE_TYPE_IMAGE">IMAGE_TYPE_IMAGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for image type that is created as icon or image</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LARGE_ONLY">LARGE_ONLY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants bit for image transformation (perform operation only when image is large only).</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAINTAIN_RATIO">MAINTAIN_RATIO</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants bit for image transformation (maintain ratio).</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROTATE_LEFT">ROTATE_LEFT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants bit for image transformation (rotate left).</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROTATE_RIGHT">ROTATE_RIGHT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants bit for image transformation (rotate right).</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRUE_TRANSFORM">TRUE_TRANSFORM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants bit for image transformation (physically transform image instead of use document feature).</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean)">Image</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 boolean disposeAfterUse)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a new image from buffered image.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.io.File,boolean)">Image</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 boolean disposeAfterUse)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a new image from file.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates and returns a copy of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOriginal()">createOriginal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create a new instance of original image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disposes of this image buffer context and releases any system resources that it is using.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureOriginal()">ensureOriginal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether some other object is "equal to" this one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#flush()">flush</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Flush current buffered image from <a href="#getData()"><code>getData()</code></a> into file stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#flush(java.lang.Object)">flush</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> track)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Flush current buffered image from <a href="#getData()"><code>getData()</code></a> into file stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the bounding Rectangle of this Image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getData()">getData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDpi()">getDpi</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeight()">getHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the height of image in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFile()">getImageFile</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a imageFile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFormat()">getImageFormat</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an image format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFormatToWrite()">getImageFormatToWrite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageType()">getImageType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get image type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalBounds()">getOriginalBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the original bounding Rectangle of this Image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalHeight()">getOriginalHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a original height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalImageFile()">getOriginalImageFile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an original image file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalImageFormat()">getOriginalImageFormat</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an original image format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalWidth()">getOriginalWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a original width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches for the property with the specified key in this property list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSize()">getSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the size of image in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationOption()">getTransformationOption</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a transformation flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWidth()">getWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the width of image in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a hash code value for the object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChanged()">isChanged</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisposeAfterUse()">isDisposeAfterUse</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a dispose setting.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransformWithOption(int)">isTransformWithOption</a><wbr/>(int option)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test if image transformation option is set to given option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#readData()">readData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read a buffered image from this instance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rotate(boolean)">rotate</a><wbr/>(boolean clockwise)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Rotate image in clockwise or anti-clockwise.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChanged(boolean)">setChanged</a><wbr/>(boolean changed)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If <code>false</code>, dispose image buffer and mark a status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setData(java.awt.image.BufferedImage)">setData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisposeAfterUse(boolean)">setDisposeAfterUse</a><wbr/>(boolean disposeAfterUse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set image data to be disposed after generating report.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDpi(int)">setDpi</a><wbr/>(int dpi)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(int)">setHeight</a><wbr/>(int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set height of image in pixels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setId(java.lang.String)">setId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageFile(java.io.File)">setImageFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a imageFile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageFormat(java.lang.String)">setImageFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an image format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageType(int)">setImageType</a><wbr/>(int imageType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set image type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOriginalHeight(int)">setOriginalHeight</a><wbr/>(int originalHeight)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOriginalImageFile(java.io.File)">setOriginalImageFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> originalImageFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOriginalImageFormat(java.lang.String)">setOriginalImageFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> originalImageFormat)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an original image format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOriginalWidth(int)">setOriginalWidth</a><wbr/>(int originalWidth)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Map)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperty(java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an image property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformationOption(int)">setTransformationOption</a><wbr/>(int transformationOption)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a transformation option.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(int)">setWidth</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set width of image in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string representation of the object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="FIT_PAPER">
<h3>FIT_PAPER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FIT_PAPER</span></div>
<div class="block">Constants bit for image transformation (auto fit).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.FIT_PAPER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAINTAIN_RATIO">
<h3>MAINTAIN_RATIO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MAINTAIN_RATIO</span></div>
<div class="block">Constants bit for image transformation (maintain ratio).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.MAINTAIN_RATIO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROTATE_LEFT">
<h3>ROTATE_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ROTATE_LEFT</span></div>
<div class="block">Constants bit for image transformation (rotate left).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.ROTATE_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROTATE_RIGHT">
<h3>ROTATE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ROTATE_RIGHT</span></div>
<div class="block">Constants bit for image transformation (rotate right).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.ROTATE_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LARGE_ONLY">
<h3>LARGE_ONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LARGE_ONLY</span></div>
<div class="block">Constants bit for image transformation (perform operation only when image is large only).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.LARGE_ONLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMAGE_TYPE_IMAGE">
<h3>IMAGE_TYPE_IMAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">IMAGE_TYPE_IMAGE</span></div>
<div class="block">Constants for image type that is created as icon or image</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.IMAGE_TYPE_IMAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMAGE_TYPE_ICON">
<h3>IMAGE_TYPE_ICON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">IMAGE_TYPE_ICON</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.IMAGE_TYPE_ICON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRUE_TRANSFORM">
<h3>TRUE_TRANSFORM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TRUE_TRANSFORM</span></div>
<div class="block">Constants bit for image transformation (physically transform image instead of use document feature).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.TRUE_TRANSFORM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FORCE_ROTATE_LEFT">
<h3>FORCE_ROTATE_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FORCE_ROTATE_LEFT</span></div>
<div class="block">Constants bit for force rotate (rotate left).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FORCE_ROTATE_RIGHT">
<h3>FORCE_ROTATE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FORCE_ROTATE_RIGHT</span></div>
<div class="block">Constants bit for force rotate (rotate right).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FORCE_ROTATE">
<h3>FORCE_ROTATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FORCE_ROTATE</span></div>
<div class="block">Constants bit for force rotate</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.magicreport.Image.FORCE_ROTATE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.io.File,boolean)">
<h3>Image</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Image</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile,
 boolean disposeAfterUse)</span></div>
<div class="block">Create a new image from file. If <code>disposeAfterUse</code> is true, image will be disposed immediately
 after print into report.
 <p>
 Generally, same image will be used only once in the template, it's recommend to set
 <code>disposeAfterUse</code> to true.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - image id</dd>
<dd><code>imageFile</code> - image file.</dd>
<dd><code>disposeAfterUse</code> - if true, dispose an image after use.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if image file is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.awt.image.BufferedImage,java.lang.String,boolean)">
<h3>Image</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Image</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat,
 boolean disposeAfterUse)</span></div>
<div class="block">Create a new image from buffered image. If <code>disposeAfterUse</code> is true, image will be disposed
 immediately after print into report.
 <p>
 Generally, same image will be used only once in the template, it's recommend to set
 <code>disposeAfterUse</code> to true.
 <p>
<code>data</code> can be null.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - image id</dd>
<dd><code>data</code> - the image data</dd>
<dd><code>imageFormat</code> - the image format.</dd>
<dd><code>disposeAfterUse</code> - if true, dispose an image after use.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if image format is null</dd>
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
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.Map)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; properties)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOriginalImageFile(java.io.File)">
<h3>setOriginalImageFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOriginalImageFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> originalImageFile)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOriginalWidth(int)">
<h3>setOriginalWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOriginalWidth</span><wbr/><span class="parameters">(int originalWidth)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOriginalHeight(int)">
<h3>setOriginalHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOriginalHeight</span><wbr/><span class="parameters">(int originalHeight)</span></div>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block">Return a id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setId(java.lang.String)">
<h3>setId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Set a id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Return a name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="engine/IObserverMessage.html#getName()">getName</a></code> in interface <code><a href="engine/IObserverMessage.html" title="interface in com.nomagic.magicreport.engine">IObserverMessage</a></code></dd>
<dt>Returns:</dt>
<dd>the name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set a name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getData()">
<h3>getData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">getData</span>()</div>
<div class="block">Return a data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setData(java.awt.image.BufferedImage)">
<h3>setData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a> data)</span></div>
<div class="block">Set a data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - the data to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFormat()">
<h3>getImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getImageFormat</span>()</div>
<div class="block">Return an image format.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the image format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImageFormat(java.lang.String)">
<h3>setImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageFormat)</span></div>
<div class="block">Set an image format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageFormat</code> - the image format to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalImageFormat()">
<h3>getOriginalImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOriginalImageFormat</span>()</div>
<div class="block">Return an original image format.
 For external image file, it may have real format that different to file extension</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the original image format</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOriginalImageFormat(java.lang.String)">
<h3>setOriginalImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOriginalImageFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> originalImageFormat)</span></div>
<div class="block">Set an original image format.
 For external image file, it may have real format that different to file extension</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>originalImageFormat</code> - the original image format to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set an image property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the key to be placed into this property list.</dd>
<dd><code>value</code> - the value corresponding to key.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Searches for the property with the specified key in this property list. The method returns <code>null</code>
 if the property is not found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the property key.</dd>
<dt>Returns:</dt>
<dd>the value in this property list with the specified key value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setProperty(java.lang.String,java.lang.Object)"><code>setProperty(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChanged()">
<h3>isChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChanged</span>()</div>
<div class="block">Return a changed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChanged(boolean)">
<h3>setChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChanged</span><wbr/><span class="parameters">(boolean changed)</span></div>
<div class="block">If <code>false</code>, dispose image buffer and mark a status. Developer should detect an image status
 before retrieve a new buffer from <a href="#getData()"><code>getData()</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changed</code> - the changed to set</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isChanged()"><code>isChanged()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readData()">
<h3>readData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">readData</span>()</div>
<div class="block">Read a buffered image from this instance. Return BufferedImage if <a href="#getData()"><code>getData()</code></a> contains data or read
 from <a href="#getImageFile()"><code>getImageFile()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a buffered image from <a href="#getData()"><code>getData()</code></a> or <a href="#getImageFile()"><code>getImageFile()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flush()">
<h3>flush</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flush</span>()
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Flush current buffered image from <a href="#getData()"><code>getData()</code></a> into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when this object is garbage collected.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to flush the data.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getData()"><code>getData()</code></a></li>
<li><a href="#getImageFile()"><code>getImageFile()</code></a></li>
<li><a href="#flush(java.lang.Object)"><code>flush(Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flush(java.lang.Object)">
<h3>flush</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flush</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> track)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Flush current buffered image from <a href="#getData()"><code>getData()</code></a> into file stream. This method will set a new image file
 and dispose the data. The image file will be deleted when tracked object is garbage collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>track</code> - the marker object track flushed file, deleting the file when the marker instance is garbage
           collected.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to flush the data.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getData()"><code>getData()</code></a></li>
<li><a href="#getImageFile()"><code>getImageFile()</code></a></li>
<li><a href="#flush()"><code>flush()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Disposes of this image buffer context and releases any system resources that it is using.</div>
</section>
</li>
<li>
<section class="detail" id="getSize()">
<h3>getSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSize</span>()</div>
<div class="block">Returns the size of image in pixels.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the size of image in pixels.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<div class="block">Returns the bounding Rectangle of this Image.
 <p>
 If image contains no data buffer <a href="#readData()"><code>readData()</code></a> return <tt>null</tt>, the bounds will be calculated
 from <a href="#getWidth()"><code>getWidth()</code></a> and <a href="#getHeight()"><code>getHeight()</code></a>.<br/>
 If image contains buffer data, calculate the bounds from buffer data.
 </p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the bounding box of this image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(int)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(int width)</span></div>
<div class="block">Set width of image in pixels.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width of image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWidth()">
<h3>getWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getWidth</span>()</div>
<div class="block">Return the width of image in pixels.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the width of image in pixels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(int)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(int height)</span></div>
<div class="block">Set height of image in pixels.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>height</code> - height of image in pixels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHeight()">
<h3>getHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getHeight</span>()</div>
<div class="block">Return the height of image in pixels.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the height of image in pixels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFile()">
<h3>getImageFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getImageFile</span>()</div>
<div class="block">Return a imageFile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the imageFile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImageFile(java.io.File)">
<h3>setImageFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> imageFile)</span></div>
<div class="block">Set a imageFile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageFile</code> - the imageFile to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisposeAfterUse()">
<h3>isDisposeAfterUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisposeAfterUse</span>()</div>
<div class="block">Return a dispose setting.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the dispose setting</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisposeAfterUse(boolean)">
<h3>setDisposeAfterUse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisposeAfterUse</span><wbr/><span class="parameters">(boolean disposeAfterUse)</span></div>
<div class="block">Set image data to be disposed after generating report.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>disposeAfterUse</code> - set value to true to allow engine to dispose image data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalImageFile()">
<h3>getOriginalImageFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getOriginalImageFile</span>()</div>
<div class="block">Return an original image file.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the original image file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalWidth()">
<h3>getOriginalWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOriginalWidth</span>()</div>
<div class="block">Return a original width.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the original width</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalHeight()">
<h3>getOriginalHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOriginalHeight</span>()</div>
<div class="block">Return a original height.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the original height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalBounds()">
<h3>getOriginalBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getOriginalBounds</span>()</div>
<div class="block">Returns the original bounding Rectangle of this Image.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the original bounding box of this image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformationOption()">
<h3>getTransformationOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getTransformationOption</span>()</div>
<div class="block">Return a transformation flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the transformation flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTransformationOption(int)">
<h3>setTransformationOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformationOption</span><wbr/><span class="parameters">(int transformationOption)</span></div>
<div class="block">Set a transformation option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformationOption</code> - the transformation option to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTransformWithOption(int)">
<h3>isTransformWithOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTransformWithOption</span><wbr/><span class="parameters">(int option)</span></div>
<div class="block">Test if image transformation option is set to given option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>option</code> - test option</dd>
<dt>Returns:</dt>
<dd>true if image transformation option is set to given option.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotate(boolean)">
<h3>rotate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rotate</span><wbr/><span class="parameters">(boolean clockwise)</span></div>
<div class="block">Rotate image in clockwise or anti-clockwise.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clockwise</code> - true for clockwise; false for anti-clockwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOriginal()">
<h3>createOriginal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></span> <span class="element-name">createOriginal</span>()</div>
<div class="block">Create a new instance of original image.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new instance of original image.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureOriginal()">
<h3>ensureOriginal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureOriginal</span>()</div>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hash code value for the object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang"><code>Object.hashCode()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Indicates whether some other object is "equal to" this one.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the reference object with which to compare.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this object is the same as the obj argument; <code>false</code> otherwise.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang"><code>Object.equals(java.lang.Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()
             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></span></div>
<div class="block">Creates and returns a copy of this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a copy of this instance</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></code> - if the object's class does not support the <code>Cloneable</code>
            interface.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang"><code>Object.clone()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of the object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of the object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageType()">
<h3>getImageType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getImageType</span>()</div>
<div class="block">Get image type. For example : icon image from $report.getIconFor(), image from $element.image</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>image type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImageType(int)">
<h3>setImageType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageType</span><wbr/><span class="parameters">(int imageType)</span></div>
<div class="block">Set image type. For example : icon image from $report.getIconFor(), image from $element.image</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageType</code> - image type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImageFormatToWrite()">
<h3>getImageFormatToWrite</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getImageFormatToWrite</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDpi()">
<h3>getDpi</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDpi</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDpi(int)">
<h3>setDpi</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDpi</span><wbr/><span class="parameters">(int dpi)</span></div>
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
