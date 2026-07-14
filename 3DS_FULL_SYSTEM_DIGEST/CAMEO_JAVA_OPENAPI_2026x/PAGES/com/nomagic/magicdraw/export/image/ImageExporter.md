# JAVA OPENAPI: ImageExporter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/export/image/ImageExporter.html
- source_path: `com/nomagic/magicdraw/export/image/ImageExporter.html`
- source_sha256: `0e3a4bd6946bb595d1bf82f95cdc675bbb7b9ec1a5b924609e93f0aed72c9da7`
- captured_utc: `2026-07-14T16:57:57.917536+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.export.image](package-summary.html)

## Class ImageExporter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.export.image.ImageExporter

@OpenApiAllpublic classImageExporter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
The exporter of diagrams to various images formats.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[EMF](#EMF)`
EMF image format.
`static final int`
`[EPS](#EPS)`
EPS image format.
`static final int`
`[JPEG](#JPEG)`
JPEG image format.
`static final int`
`[PNG](#PNG)`
PNG image format.
`static final int`
`[SVG](#SVG)`
SVG image format.
`static final int`
`[SVG_NO_BOUNDS_CHANGE](#SVG_NO_BOUNDS_CHANGE)`
.
`static final int`
`[TIFF](#TIFF)`
TIFF image format.
`static final int`
`[WMF](#WMF)`
WMF image format.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImageExporter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 boolean justSelected)`
Exports diagram into the BufferedImage.
`static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,int))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 boolean justSelected,
 int scalePercent)`
Exports diagram into the BufferedImage.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Exports diagram into given format image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected)`
Exports diagram into given format image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,boolean))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 boolean saveBackground)`
Exports diagram into given format image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 int dpi,
 int scalePercent)`
Exports diagram into given format image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus)`
Exports diagram into given format image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.apache.batik.svggen.SVGIDGenerator> idGeneratorSupplier)`
Exports diagram into given format image.
`static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int scalePercent)`
Exports single PresentationElement (for example Class) into the BufferedImage.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[export](#export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int))([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 int dpi,
 int scalePercent)`
Exports single PresentationElement(for example Class) into the given format image.
`static [ImageExportResult](ImageExportResult.html)`
`[exportForResult](#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Exports diagram into given format image.
`static [ImageExportResult](ImageExportResult.html)`
`[exportForResult](#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 int dpi,
 int scalePercent)`
Exports diagram into given format image.
`static [ImageExportResult](ImageExportResult.html)`
`[exportForResult](#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus)`
Exports diagram into given format image.
`static [ImageExportResult](ImageExportResult.html)`
`[exportForResult](#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.apache.batik.svggen.SVGIDGenerator> idGeneratorSupplier)`
Exports diagram into given format image.
`static [ImageExportResult](ImageExportResult.html)`
`[exportForResult](#exportForResult(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int))([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 int dpi,
 int scalePercent)`
Exports single PresentationElement(for example Class) into the given format image.
`static boolean`
`[isSelectedSymbolsExportable](#isSelectedSymbolsExportable(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Checks if any selected symbol (in given diagram) can be exported into image.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
JPEG
public static final int JPEG
JPEG image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.JPEG)
PNG
public static final int PNG
PNG image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.PNG)
WMF
public static final int WMF
WMF image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.WMF)
EPS
public static final int EPS
EPS image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.EPS)
SVG
public static final int SVG
SVG image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.SVG)
EMF
public static final int EMF
EMF image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.EMF)
TIFF
public static final int TIFF
TIFF image format.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.TIFF)
SVG_NO_BOUNDS_CHANGE
public static final int SVG_NO_BOUNDS_CHANGE
.
 SVG image format without bounds change. Used to preview changes in diagrams in merge dialog.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.SVG_NO_BOUNDS_CHANGE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImageExporter
public ImageExporter()
 ============ METHOD DETAIL ========== 
Method Details
export
@CheckForNullpublic static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 boolean justSelected)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into the BufferedImage. Exports all symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
Returns:
the BufferedImage instance of the diagram.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
@CheckForNullpublic static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 boolean justSelected,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into the BufferedImage. Exports all symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image.
Returns:
the BufferedImage instance of the diagram.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
public static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
exportForResult
public static [ImageExportResult](ImageExportResult.html) exportForResult([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
Returns:
Image export result.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
public static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
@CheckForNullpublic static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`progressStatus` - instance of [`ProgressStatus`](../../../task/ProgressStatus.html) can be null.
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
@CheckForNullpublic static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus,
 @CheckForNull
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.apache.batik.svggen.SVGIDGenerator> idGeneratorSupplier)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`progressStatus` - instance of [`ProgressStatus`](../../../task/ProgressStatus.html) can be null.
`idGeneratorSupplier` - supplier for custom SVGIDGenerator. Used to prevent id conflicts when exported SVG files are embedded in one HTML
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
exportForResult
@CheckForNullpublic static [ImageExportResult](ImageExportResult.html) exportForResult([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`progressStatus` - instance of [`ProgressStatus`](../../../task/ProgressStatus.html) can be null.
Returns:
Image export result.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
exportForResult
@CheckForNullpublic static [ImageExportResult](ImageExportResult.html) exportForResult([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progressStatus,
 @CheckForNull
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.apache.batik.svggen.SVGIDGenerator> idGeneratorSupplier)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`progressStatus` - instance of [`ProgressStatus`](../../../task/ProgressStatus.html) can be null.
`idGeneratorSupplier` - supplier for custom SVGIDGenerator. Used to prevent id conflicts when exported SVG files are embedded in one HTML
Returns:
Image export result.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
public static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 boolean saveBackground)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`saveBackground` - save diagram background in image.
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
exportForResult
public static [ImageExportResult](ImageExportResult.html) exportForResult([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 int dpi,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`dpi` - sets the DPI flag in output image. Parameter is ignored for vector images.
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.
Returns:
Image export result.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
public static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 boolean justSelected,
 int dpi,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.
Parameters:
`diagram` - the given diagram.
`format` - format of the image.
`file` - the output file
`justSelected` - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported
`dpi` - sets the DPI flag in output image. Parameter is ignored for vector images.
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
isSelectedSymbolsExportable
public static boolean isSelectedSymbolsExportable([AbstractDiagramPresentationElement](../../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Checks if any selected symbol (in given diagram) can be exported into image.
 E.g. the selected link can not be exported if the connected elements symbols are not selected.
Parameters:
`diagram` - given diagram.
Returns:
`true` - if any of selected symbols can be exported; otherwise - `false`.
export
@CheckForNullpublic static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) export([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 int dpi,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports single PresentationElement(for example Class) into the given format image. Writes this image into the given file.
Parameters:
`element` - the given presentation element.
`format` - format of the image.
`file` - the output file
`dpi` - sets the DPI flag in output image. Parameter is ignored for vector images.
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.
Returns:
saved image bounds(start point in the diagram and dimension of image).
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
exportForResult
@CheckForNullpublic static [ImageExportResult](ImageExportResult.html) exportForResult([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int format,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 int dpi,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports single PresentationElement(for example Class) into the given format image. Writes this image into the given file.
Parameters:
`element` - the given presentation element.
`format` - format of the image.
`file` - the output file
`dpi` - sets the DPI flag in output image. Parameter is ignored for vector images.
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.
Returns:
Image export result.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.
export
@CheckForNullpublic static [BufferedImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html) export([PresentationElement](../../uml/symbols/PresentationElement.html) element,
 int scalePercent)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Exports single PresentationElement (for example Class) into the BufferedImage.
Parameters:
`element` - the given element.
`scalePercent` - defines scaling the output image to given percentage. Value of 100 does not scale image.
Returns:
the BufferedImage instance of the diagram.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - in case of some io error.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.export.image</a></div>
<h1 class="title" title="Class ImageExporter">Class ImageExporter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.export.image.ImageExporter</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ImageExporter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The exporter of diagrams to various images formats.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMF">EMF</a></code></div>
<div class="col-last even-row-color">
<div class="block">EMF image format.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EPS">EPS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">EPS image format.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#JPEG">JPEG</a></code></div>
<div class="col-last even-row-color">
<div class="block">JPEG image format.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PNG">PNG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">PNG image format.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SVG">SVG</a></code></div>
<div class="col-last even-row-color">
<div class="block">SVG image format.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SVG_NO_BOUNDS_CHANGE">SVG_NO_BOUNDS_CHANGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TIFF">TIFF</a></code></div>
<div class="col-last even-row-color">
<div class="block">TIFF image format.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#WMF">WMF</a></code></div>
<div class="col-last odd-row-color">
<div class="block">WMF image format.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ImageExporter</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 boolean justSelected)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into the BufferedImage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,int)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 boolean justSelected,
 int scalePercent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into the BufferedImage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,boolean)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 boolean saveBackground)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 int dpi,
 int scalePercent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier)">export</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.apache.batik.svggen.SVGIDGenerator&gt; idGeneratorSupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">export</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int scalePercent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports single PresentationElement (for example Class) into the BufferedImage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int)">export</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int dpi,
 int scalePercent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports single PresentationElement(for example Class) into the given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File)">exportForResult</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int)">exportForResult</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 int dpi,
 int scalePercent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus)">exportForResult</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier)">exportForResult</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.apache.batik.svggen.SVGIDGenerator&gt; idGeneratorSupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports diagram into given format image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportForResult(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int)">exportForResult</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int dpi,
 int scalePercent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports single PresentationElement(for example Class) into the given format image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSelectedSymbolsExportable(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">isSelectedSymbolsExportable</a><wbr/>(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if any selected symbol (in given diagram) can be exported into image.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="JPEG">
<h3>JPEG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">JPEG</span></div>
<div class="block">JPEG image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.JPEG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PNG">
<h3>PNG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PNG</span></div>
<div class="block">PNG image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.PNG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WMF">
<h3>WMF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">WMF</span></div>
<div class="block">WMF image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.WMF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EPS">
<h3>EPS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EPS</span></div>
<div class="block">EPS image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.EPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SVG">
<h3>SVG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SVG</span></div>
<div class="block">SVG image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.SVG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EMF">
<h3>EMF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EMF</span></div>
<div class="block">EMF image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.EMF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIFF">
<h3>TIFF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TIFF</span></div>
<div class="block">TIFF image format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.TIFF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SVG_NO_BOUNDS_CHANGE">
<h3>SVG_NO_BOUNDS_CHANGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SVG_NO_BOUNDS_CHANGE</span></div>
<div class="block">.
 SVG image format without bounds change. Used to preview changes in diagrams in merge dialog.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.export.image.ImageExporter.SVG_NO_BOUNDS_CHANGE">Constant Field Values</a></li>
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
<h3>ImageExporter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImageExporter</span>()</div>
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
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 boolean justSelected)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into the BufferedImage. Exports all symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dt>Returns:</dt>
<dd>the BufferedImage instance of the diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,int)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 boolean justSelected,
 int scalePercent)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into the BufferedImage. Exports all symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image.</dd>
<dt>Returns:</dt>
<dd>the BufferedImage instance of the diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File)">
<h3>export</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File)">
<h3>exportForResult</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportForResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dt>Returns:</dt>
<dd>Image export result.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean)">
<h3>export</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>progressStatus</code> - instance of <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a> can be null.</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.apache.batik.svggen.SVGIDGenerator&gt; idGeneratorSupplier)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>progressStatus</code> - instance of <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a> can be null.</dd>
<dd><code>idGeneratorSupplier</code> - supplier for custom SVGIDGenerator. Used to prevent id conflicts when exported SVG files are embedded in one HTML</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus)">
<h3>exportForResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportForResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>progressStatus</code> - instance of <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a> can be null.</dd>
<dt>Returns:</dt>
<dd>Image export result.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,com.nomagic.task.ProgressStatus,java.util.function.Supplier)">
<h3>exportForResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportForResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.apache.batik.svggen.SVGIDGenerator&gt; idGeneratorSupplier)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>progressStatus</code> - instance of <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task"><code>ProgressStatus</code></a> can be null.</dd>
<dd><code>idGeneratorSupplier</code> - supplier for custom SVGIDGenerator. Used to prevent id conflicts when exported SVG files are embedded in one HTML</dd>
<dt>Returns:</dt>
<dd>Image export result.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,boolean)">
<h3>export</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 boolean saveBackground)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>saveBackground</code> - save diagram background in image.</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportForResult(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int)">
<h3>exportForResult</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportForResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 int dpi,
 int scalePercent)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>dpi</code> - sets the DPI flag in output image. Parameter is ignored for vector images.</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.</dd>
<dt>Returns:</dt>
<dd>Image export result.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,int,java.io.File,boolean,int,int)">
<h3>export</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 boolean justSelected,
 int dpi,
 int scalePercent)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports diagram into given format image. Writes this image into given file. Exports all or just selected symbols from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>justSelected</code> - export only selected symbols in the diagram. If diagram does not have selected symbols, all symbols are exported</dd>
<dd><code>dpi</code> - sets the DPI flag in output image. Parameter is ignored for vector images.</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSelectedSymbolsExportable(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>isSelectedSymbolsExportable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSelectedSymbolsExportable</span><wbr/><span class="parameters">(<a href="../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Checks if any selected symbol (in given diagram) can be exported into image.
 E.g. the selected link can not be exported if the connected elements symbols are not selected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - given diagram.</dd>
<dt>Returns:</dt>
<dd><code>true</code> - if any of selected symbols can be exported; otherwise - <code>false</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int dpi,
 int scalePercent)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports single PresentationElement(for example Class) into the given format image. Writes this image into the given file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given presentation element.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>dpi</code> - sets the DPI flag in output image. Parameter is ignored for vector images.</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.</dd>
<dt>Returns:</dt>
<dd>saved image bounds(start point in the diagram and dimension of image).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportForResult(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,java.io.File,int,int)">
<h3>exportForResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportForResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int dpi,
 int scalePercent)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports single PresentationElement(for example Class) into the given format image. Writes this image into the given file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given presentation element.</dd>
<dd><code>format</code> - format of the image.</dd>
<dd><code>file</code> - the output file</dd>
<dd><code>dpi</code> - sets the DPI flag in output image. Parameter is ignored for vector images.</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image. Is ignored by WMF file format.</dd>
<dt>Returns:</dt>
<dd>Image export result.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="export(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>export</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">export</span><wbr/><span class="parameters">(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int scalePercent)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Exports single PresentationElement (for example Class) into the BufferedImage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element.</dd>
<dd><code>scalePercent</code> - defines scaling the output image to given percentage. Value of 100 does not scale image.</dd>
<dt>Returns:</dt>
<dd>the BufferedImage instance of the diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - in case of some io error.</dd>
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
