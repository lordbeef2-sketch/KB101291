# JAVA OPENAPI: ExportTool2 (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/magicreport/tools/ExportTool2.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ExportTool2.html`
- source_sha256: `38137f20ae8cf8885791cd400a80b167d50825b8da39c1a6f441bf4772877bc7`
- captured_utc: `2026-07-14T16:45:37.918507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ExportTool2

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
[com.nomagic.magicreport.engine.ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)
com.nomagic.magicdraw.magicreport.tools.ExportTool2

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)
@OpenApiAllpublic classExportTool2
extends [ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)

Deprecated.

Deprecated class, use [`ExportTool3`](ExportTool3.html) instead.
 This class allow report to export element in other file format including tree folder.

Since:
Mar 14, 2012
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ExportTool2)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.[ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)
`[ConcurrentTool.ConsumeObject](../../../magicreport/engine/ConcurrentTool.ConsumeObject.html)`
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Deprecated.
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExportTool2](#%3Cinit%3E())()`
Deprecated.
Create an export tool.
`[ExportTool2](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine,java.util.Observer))([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) engine,
 [Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) observer)`
Deprecated.
Create an export tool with observer.
`[ExportTool2](#%3Cinit%3E(java.util.Observer))([Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) observer)`
Deprecated.
Create an export tool with observer.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[consume](#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))([ConcurrentTool.ConsumeObject](../../../magicreport/engine/ConcurrentTool.ConsumeObject.html) consumeObject)`
Deprecated.
Consume a object.
`protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html)`
`[createAndExportElement](#createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)`
Deprecated.
`protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html)`
`[createAndExportElement](#createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter,boolean))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter,
 boolean isSmart)`
Deprecated.
`protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html)`
`[createAndExportSmartElement](#createAndExportSmartElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)`
Deprecated.
`protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html)`
`[createAttributeAndExportElement](#createAttributeAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 boolean skipData)`
Deprecated.
Create attributes for XML element represents the `exportingElement` and offer the element to be created into file.
`protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createResourcesDir](#createResourcesDir(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourcesLocation)`
Deprecated.
Create a resource directory.
`void`
`[destroy](#destroy())()`
Deprecated.
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[exportAll](#exportAll(boolean,boolean))(boolean exportResources,
 boolean exportLinkedFile)`
Deprecated.
Export current opened project into file.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[exportCustomImageHolder](#exportCustomImageHolder(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) exportingElement)`
Deprecated.
Export the image for the element.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportDiagramImage](#exportDiagramImage(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean))([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentation,
 boolean exportResources)`
Deprecated.
`[ImageExportResult](../../export/image/ImageExportResult.html)`
`[exportDiagramImageWithResult](#exportDiagramImageWithResult(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean))([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentation,
 boolean exportResources)`
Deprecated.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElement](#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources)`
Deprecated.
Export element to XML file.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElement](#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile)`
Deprecated.
Export element to XML file.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElement](#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.export.image.ImageExportResult))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 [ImageExportResult](../../export/image/ImageExportResult.html) exportResult)`
Deprecated.
Export element to XML file.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElement](#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)`
Deprecated.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElementForTree](#exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingNodeFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources)`
Deprecated.
Export element to XML file which is used for create tree.
`[ITool.Void](../../../magicreport/engine/ITool.Void.html)`
`[exportElementForTree](#exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.ui.ElementFilter))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingNodeFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 com.nomagic.magicdraw.ui.ElementFilter filter)`
Deprecated.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[exportIcon](#exportIcon(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) exportingElement)`
Deprecated.
Export the icon for element.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getElementType](#getElementType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
Return String representing element type.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameMap)`
Deprecated.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPropertyHumanName](#getPropertyHumanName(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameMap)`
Deprecated.
Get property human name of given property name.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getResourcesLocation](#getResourcesLocation())()`
Deprecated.
Return location of resources directory.
`protected void`
`[handleIOException](#handleIOException(java.lang.Exception))([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`
Deprecated.
`protected boolean`
`[isCancel](#isCancel())()`
Deprecated.
`void`
`[setRecursive](#setRecursive(boolean))(boolean isRecursive)`
Deprecated.
`void`
`[setShowAuxiliary](#setShowAuxiliary(boolean))(boolean isShowAuxiliary)`
Deprecated.
Methods inherited from class com.nomagic.magicreport.engine.[ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)
`[getCustomPoolSize](../../../magicreport/engine/ConcurrentTool.html#getCustomPoolSize()), [isNoSpaceException](../../../magicreport/engine/ConcurrentTool.html#isNoSpaceException(java.lang.Exception)), [isRunning](../../../magicreport/engine/ConcurrentTool.html#isRunning()), [offer](../../../magicreport/engine/ConcurrentTool.html#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[clone](../../../magicreport/engine/Tool.html#clone()), [getContext](../../../magicreport/engine/Tool.html#getContext()), [getProperties](../../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[clearTool](../../../magicreport/engine/ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Deprecated.
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ExportTool2.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExportTool2
public ExportTool2()
Deprecated.
Create an export tool.
ExportTool2
public ExportTool2([Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) observer)
Deprecated.
Create an export tool with observer.
Parameters:
`observer` - Observer
ExportTool2
public ExportTool2([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) engine,
 [Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) observer)
Deprecated.
Create an export tool with observer.
Parameters:
`engine` - engine
`observer` - Observer
 ============ METHOD DETAIL ========== 
Method Details
setRecursive
public void setRecursive(boolean isRecursive)
Deprecated.
setShowAuxiliary
public void setShowAuxiliary(boolean isShowAuxiliary)
Deprecated.
consume
public void consume([ConcurrentTool.ConsumeObject](../../../magicreport/engine/ConcurrentTool.ConsumeObject.html) consumeObject)
Deprecated.
Consume a object.
Specified by:
`[consume](../../../magicreport/engine/ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))` in class `[ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)`
Parameters:
`consumeObject` - consume object.
See Also:
[`ConcurrentTool.consume(ConsumeObject)`](../../../magicreport/engine/ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))
exportElement
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElement([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources)
Deprecated.
Export element to XML file.
Parameters:
`exportingFile` - exporting file
`exportingElement` - exporting element
`exportResources` - true if you want to export resources of this element
Returns:
nothing
exportElement
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElement([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)
Deprecated.
exportElement
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElement([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile)
Deprecated.
Export element to XML file.
Parameters:
`exportingFile` - exporting file
`exportingElement` - exporting element
`exportResources` - true if you want to export resources of this element
`exportLinkedFile` - true if you want to include linked files.
Returns:
nothing
exportElement
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElement([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 [ImageExportResult](../../export/image/ImageExportResult.html) exportResult)
Deprecated.
Export element to XML file.
Parameters:
`exportingFile` - exporting file
`exportingElement` - exporting element
`exportResources` - true if you want to export resources of this element
`exportLinkedFile` - true if you want to include linked files.
`exportResult` - image export result required for calculation of element locations if image is cropped or has banners
Returns:
nothing
exportDiagramImage
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportDiagramImage([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentation,
 boolean exportResources)
Deprecated.
exportDiagramImageWithResult
@CheckForNullpublic [ImageExportResult](../../export/image/ImageExportResult.html) exportDiagramImageWithResult([DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentation,
 boolean exportResources)
Deprecated.
exportElementForTree
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElementForTree([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingNodeFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 com.nomagic.magicdraw.ui.ElementFilter filter)
Deprecated.
exportElementForTree
public [ITool.Void](../../../magicreport/engine/ITool.Void.html) exportElementForTree([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) exportingNodeFile,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources)
Deprecated.
Export element to XML file which is used for create tree.
Parameters:
`exportingNodeFile` - exporting file
`exportingElement` - export element
`exportResources` - true if you want to export resources of this element
Returns:
nothing
getResourcesLocation
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getResourcesLocation()
Deprecated.
Return location of resources directory.
Returns:
a path to resources directory.
createResourcesDir
protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createResourcesDir([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourcesLocation)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Create a resource directory.
Parameters:
`resourcesLocation` - resources location
Returns:
a File pointed to resources directory
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO error occurs.
exportIcon
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) exportIcon([BaseElement](../../uml/BaseElement.html) exportingElement)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Export the icon for element. This method should not perform graphic renderer by itself. The icon exporting
 process should be enqueue by method `offer(ConsumeObject)`.
Parameters:
`exportingElement` - target element
Returns:
path to icon
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO error occurs
exportCustomImageHolder
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) exportCustomImageHolder([BaseElement](../../uml/BaseElement.html) exportingElement)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Export the image for the element. Image for the element will be exported from strereotype CustomImageHolder.
Parameters:
`exportingElement` - target element
Returns:
path to icon
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO error occurs
createAndExportElement
protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) createAndExportElement([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
createAndExportSmartElement
protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) createAndExportSmartElement([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
createAndExportElement
protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) createAndExportElement([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter,
 boolean isSmart)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
createAttributeAndExportElement
protected [Element](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html) createAttributeAndExportElement([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 boolean skipData)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Deprecated.
Create attributes for XML element represents the `exportingElement` and offer the element to be created into file. Return
 `null` to cancel this element exporting.
Parameters:
`document` - XML document
`exportingElement` - exporting element
`exportResources` - true if you want to export resources of this element
`exportLinkedFile` - true if you want to include linked files.
`skipData` - true to create only main attribute to xml document.
Returns:
XML element for creating containment tree.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when IO error occurred.
getElementType
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getElementType([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
Return String representing element type.
Parameters:
`element` - element
Returns:
a String representing element type.
exportAll
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) exportAll(boolean exportResources,
 boolean exportLinkedFile)
Deprecated.
Export current opened project into file.
Parameters:
`exportResources` - true if you want to export resources.
`exportLinkedFile` - true if you want to include linked files.
Returns:
nothing
destroy
public void destroy()
Deprecated.
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.
Overrides:
`[destroy](../../../magicreport/engine/ConcurrentTool.html#destroy())` in class `[ConcurrentTool](../../../magicreport/engine/ConcurrentTool.html)`
See Also:
[`ConcurrentTool.destroy()`](../../../magicreport/engine/ConcurrentTool.html#destroy())
getPropertyHumanName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPropertyHumanName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameMap)
Deprecated.
Get property human name of given property name. If `nameMap` is used, human name will be resolved by
 `nameMap` then resource string.
Parameters:
`propertyName` - a property name
`nameMap` - optional provides new name map from `DSL.getPropertyNameMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)` to resolve property
 name from <<metaType>>
Returns:
human name
getHumanName
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getHumanName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameMap)
Deprecated.
isCancel
protected boolean isCancel()
Deprecated.
handleIOException
protected void handleIOException([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)
Deprecated.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ExportTool2">Class ExportTool2</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.ConcurrentTool</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ExportTool2</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExportTool2</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Deprecated class, use <a href="ExportTool3.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ExportTool3</code></a> instead.
 This class allow report to export element in other file format including tree folder.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 14, 2012</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ExportTool2">Serialized Form</a></li>
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
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></h2>
<code><a href="../../../magicreport/engine/ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a></code></div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
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
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Contains a context name.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#context">context</a>, <a href="../../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ExportTool2</a>()</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine,java.util.Observer)">ExportTool2</a><wbr/>(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> observer)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool with observer.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Observer)">ExportTool2</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> observer)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool with observer.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">consume</a><wbr/>(<a href="../../../magicreport/engine/ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Consume a object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">createAndExportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter,boolean)">createAndExportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter,
 boolean isSmart)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAndExportSmartElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">createAndExportSmartElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAttributeAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">createAttributeAndExportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 boolean skipData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create attributes for XML element represents the <code>exportingElement</code> and offer the element to be created into file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createResourcesDir(java.lang.String)">createResourcesDir</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesLocation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create a resource directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportAll(boolean,boolean)">exportAll</a><wbr/>(boolean exportResources,
 boolean exportLinkedFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export current opened project into file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportCustomImageHolder(com.nomagic.magicdraw.uml.BaseElement)">exportCustomImageHolder</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> exportingElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export the image for the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportDiagramImage(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean)">exportDiagramImage</a><wbr/>(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentation,
 boolean exportResources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportDiagramImageWithResult(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean)">exportDiagramImageWithResult</a><wbr/>(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentation,
 boolean exportResources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">exportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">exportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.export.image.ImageExportResult)">exportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 <a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a> exportResult)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">exportElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 com.nomagic.magicdraw.ui.ElementFilter filter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">exportElementForTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingNodeFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file which is used for create tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.ui.ElementFilter)">exportElementForTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingNodeFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 com.nomagic.magicdraw.ui.ElementFilter filter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#exportIcon(com.nomagic.magicdraw.uml.BaseElement)">exportIcon</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> exportingElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export the icon for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getElementType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementType</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Return String representing element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getHumanName(java.lang.String,java.util.Map)">getHumanName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPropertyHumanName(java.lang.String,java.util.Map)">getPropertyHumanName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get property human name of given property name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getResourcesLocation()">getResourcesLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Return location of resources directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#handleIOException(java.lang.Exception)">handleIOException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isCancel()">isCancel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setRecursive(boolean)">setRecursive</a><wbr/>(boolean isRecursive)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setShowAuxiliary(boolean)">setShowAuxiliary</a><wbr/>(boolean isShowAuxiliary)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></h3>
<code><a href="../../../magicreport/engine/ConcurrentTool.html#getCustomPoolSize()">getCustomPoolSize</a>, <a href="../../../magicreport/engine/ConcurrentTool.html#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a>, <a href="../../../magicreport/engine/ConcurrentTool.html#isRunning()">isRunning</a>, <a href="../../../magicreport/engine/ConcurrentTool.html#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">offer</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ExportTool2.CONTEXT_NAME">Constant Field Values</a></li>
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
<h3>ExportTool2</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExportTool2</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Observer)">
<h3>ExportTool2</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExportTool2</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> observer)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool with observer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>observer</code> - Observer</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine,java.util.Observer)">
<h3>ExportTool2</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExportTool2</span><wbr/><span class="parameters">(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> observer)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create an export tool with observer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - engine</dd>
<dd><code>observer</code> - Observer</dd>
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
<section class="detail" id="setRecursive(boolean)">
<h3>setRecursive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecursive</span><wbr/><span class="parameters">(boolean isRecursive)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowAuxiliary(boolean)">
<h3>setShowAuxiliary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowAuxiliary</span><wbr/><span class="parameters">(boolean isShowAuxiliary)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">
<h3>consume</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">consume</span><wbr/><span class="parameters">(<a href="../../../magicreport/engine/ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Consume a object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../magicreport/engine/ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">consume</a></code> in class <code><a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>consumeObject</code> - consume object.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../../magicreport/engine/ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)"><code>ConcurrentTool.consume(ConsumeObject)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>exportElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingFile</code> - exporting file</dd>
<dd><code>exportingElement</code> - exporting element</dd>
<dd><code>exportResources</code> - true if you want to export resources of this element</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">
<h3>exportElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean)">
<h3>exportElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingFile</code> - exporting file</dd>
<dd><code>exportingElement</code> - exporting element</dd>
<dd><code>exportResources</code> - true if you want to export resources of this element</dd>
<dd><code>exportLinkedFile</code> - true if you want to include linked files.</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportElement(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.export.image.ImageExportResult)">
<h3>exportElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 <a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a> exportResult)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingFile</code> - exporting file</dd>
<dd><code>exportingElement</code> - exporting element</dd>
<dd><code>exportResources</code> - true if you want to export resources of this element</dd>
<dd><code>exportLinkedFile</code> - true if you want to include linked files.</dd>
<dd><code>exportResult</code> - image export result required for calculation of element locations if image is cropped or has banners</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportDiagramImage(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean)">
<h3>exportDiagramImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportDiagramImage</span><wbr/><span class="parameters">(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentation,
 boolean exportResources)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="exportDiagramImageWithResult(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,boolean)">
<h3>exportDiagramImageWithResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../export/image/ImageExportResult.html" title="class in com.nomagic.magicdraw.export.image">ImageExportResult</a></span> <span class="element-name">exportDiagramImageWithResult</span><wbr/><span class="parameters">(<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentation,
 boolean exportResources)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.ui.ElementFilter)">
<h3>exportElementForTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElementForTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingNodeFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 com.nomagic.magicdraw.ui.ElementFilter filter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="exportElementForTree(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>exportElementForTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">exportElementForTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> exportingNodeFile,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export element to XML file which is used for create tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingNodeFile</code> - exporting file</dd>
<dd><code>exportingElement</code> - export element</dd>
<dd><code>exportResources</code> - true if you want to export resources of this element</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourcesLocation()">
<h3>getResourcesLocation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourcesLocation</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Return location of resources directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a path to resources directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createResourcesDir(java.lang.String)">
<h3>createResourcesDir</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createResourcesDir</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesLocation)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create a resource directory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourcesLocation</code> - resources location</dd>
<dt>Returns:</dt>
<dd>a File pointed to resources directory</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO error occurs.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportIcon(com.nomagic.magicdraw.uml.BaseElement)">
<h3>exportIcon</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">exportIcon</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> exportingElement)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export the icon for element. This method should not perform graphic renderer by itself. The icon exporting
 process should be enqueue by method <code>offer(ConsumeObject)</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingElement</code> - target element</dd>
<dt>Returns:</dt>
<dd>path to icon</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportCustomImageHolder(com.nomagic.magicdraw.uml.BaseElement)">
<h3>exportCustomImageHolder</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">exportCustomImageHolder</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> exportingElement)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export the image for the element. Image for the element will be exported from strereotype CustomImageHolder.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportingElement</code> - target element</dd>
<dt>Returns:</dt>
<dd>path to icon</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">
<h3>createAndExportElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></span> <span class="element-name">createAndExportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndExportSmartElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter)">
<h3>createAndExportSmartElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></span> <span class="element-name">createAndExportSmartElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,com.nomagic.magicdraw.ui.ElementFilter,boolean)">
<h3>createAndExportElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></span> <span class="element-name">createAndExportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 @CheckForNull
 com.nomagic.magicdraw.ui.ElementFilter filter,
 boolean isSmart)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAttributeAndExportElement(org.w3c.dom.Document,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,boolean,boolean)">
<h3>createAttributeAndExportElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Element.html" title="class or interface in org.w3c.dom">Element</a></span> <span class="element-name">createAttributeAndExportElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> exportingElement,
 boolean exportResources,
 boolean exportLinkedFile,
 boolean skipData)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create attributes for XML element represents the <code>exportingElement</code> and offer the element to be created into file. Return
 <code>null</code> to cancel this element exporting.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>document</code> - XML document</dd>
<dd><code>exportingElement</code> - exporting element</dd>
<dd><code>exportResources</code> - true if you want to export resources of this element</dd>
<dd><code>exportLinkedFile</code> - true if you want to include linked files.</dd>
<dd><code>skipData</code> - true to create only main attribute to xml document.</dd>
<dt>Returns:</dt>
<dd>XML element for creating containment tree.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when IO error occurred.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementType</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Return String representing element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>a String representing element type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportAll(boolean,boolean)">
<h3>exportAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">exportAll</span><wbr/><span class="parameters">(boolean exportResources,
 boolean exportLinkedFile)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Export current opened project into file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exportResources</code> - true if you want to export resources.</dd>
<dd><code>exportLinkedFile</code> - true if you want to include linked files.</dd>
<dt>Returns:</dt>
<dd>nothing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/ConcurrentTool.html#destroy()">destroy</a></code> in class <code><a href="../../../magicreport/engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../magicreport/engine/ConcurrentTool.html#destroy()"><code>ConcurrentTool.destroy()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyHumanName(java.lang.String,java.util.Map)">
<h3>getPropertyHumanName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyHumanName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameMap)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get property human name of given property name. If <code>nameMap</code> is used, human name will be resolved by
 <code>nameMap</code> then resource string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - a property name</dd>
<dd><code>nameMap</code> - optional provides new name map from <code>DSL.getPropertyNameMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)</code> to resolve property
                     name from &lt;&lt;metaType&gt;&gt;</dd>
<dt>Returns:</dt>
<dd>human name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanName(java.lang.String,java.util.Map)">
<h3>getHumanName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameMap)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isCancel()">
<h3>isCancel</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isCancel</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="handleIOException(java.lang.Exception)">
<h3>handleIOException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleIOException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
