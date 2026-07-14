# JAVA OPENAPI: BaseEmfUml2Helper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2Helper.html`
- source_sha256: `7f80d042ea0d013bc6ec3ac990380c08da4e584f7e0fcba51d1b3327c1c67b33`
- captured_utc: `2026-07-14T16:55:17.865037+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi](package-summary.html)

## Class BaseEmfUml2Helper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper

All Implemented Interfaces:
`[BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`

Direct Known Subclasses:
`[EmfUml2Helper](v2/EmfUml2Helper.html)`

@OpenApipublic abstract classBaseEmfUml2Helper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)

Eclipse UML2 XMI helper.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MAGICDRAW_SOURCE](#MAGICDRAW_SOURCE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MD_ID](#MD_ID)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MD_PROPERTY_NAME](#MD_PROPERTY_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseEmfUml2Helper](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger))([Project](../core/Project.html) project,
 com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](EmfUml2Logger.html) logger)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addCreatedElementIDData](#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) relatedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)`

`void`
`[addFinalizeActivity](#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity))([FinalizeActivity](FinalizeActivity.html) activity)`

`void`
`[clearCreatedElementsIDData](#clearCreatedElementsIDData())()`

`protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap`
`[createDataTypeMap](#createDataTypeMap())()`

`protected abstract [BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html)`
`[createEElementNameRetriever](#createEElementNameRetriever())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getCreatedElementsIDData](#getCreatedElementsIDData())()`

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEElementName](#getEElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Returns element human name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementName](#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 boolean qualifiedName)`
Returns element human name.
`[BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html)`
`[getEmfOptionsGroup](#getEmfOptionsGroup())()`
Deprecated.
Use [`BaseEmfUml2Helper.getOptions()`](helpers/BaseEmfUml2Helper.html#getOptions())
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FinalizeActivity](FinalizeActivity.html)>`
`[getFinalizeActivities](#getFinalizeActivities())()`

`[EmfUml2Logger](EmfUml2Logger.html)`
`[getLogger](#getLogger())()`
Returns logger.
`abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getMagicDrawAnnotationDetails](#getMagicDrawAnnotationDetails(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getMDProjectBuiltinProfiles](#getMDProjectBuiltinProfiles())()`
Returns profiles that are "built-in" in MagicDraw project
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getMDStandardProfiles](#getMDStandardProfiles())()`

`[BaseOptions](envoptions/BaseOptions.html)`
`[getOptions](#getOptions())()`

`com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
`[getPersistenceHelper](#getPersistenceHelper())()`

`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Returns current project
`com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap`
`[getUml2DataTypeMap](#getUml2DataTypeMap())()`
Returns datatype map
`abstract [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getUml2MetaModel](#getUml2MetaModel())()`

`static void`
`[initProgressStatus](#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean))([ProgressStatus](../../task/ProgressStatus.html) progress,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean indeterminate)`

`boolean`
`[isMappedElement](#isMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is mapped.
`boolean`
`[isRemovableElement](#isRemovableElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if element will be removed or already disposed.
`boolean`
`[isSkippedElement](#isSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is skipped.
`void`
`[markMappedElement](#markMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Marks that element is mapped.
`void`
`[markRemovableElement](#markRemovableElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Mark element that will be removed or already disposed
`void`
`[markSkippedElement](#markSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Mark skipped element.
`static void`
`[removeElement](#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection)`

`void`
`[setMDElementID](#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))([BaseElement](../uml/BaseElement.html) mdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Set MD element id according given EMF element id.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
MAGICDRAW_SOURCE
protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MAGICDRAW_SOURCE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MAGICDRAW_SOURCE)
MD_ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MD_ID
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MD_ID)
MD_PROPERTY_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MD_PROPERTY_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MD_PROPERTY_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseEmfUml2Helper
public BaseEmfUml2Helper([Project](../core/Project.html) project,
 com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](EmfUml2Logger.html) logger)
 ============ METHOD DETAIL ========== 
Method Details
getUml2DataTypeMap
public com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap getUml2DataTypeMap()
Returns datatype map
Specified by:
`[getUml2DataTypeMap](helpers/BaseEmfUml2Helper.html#getUml2DataTypeMap())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
datatypes map
createDataTypeMap
protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap createDataTypeMap()
createEElementNameRetriever
protected abstract [BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html) createEElementNameRetriever()
getMagicDrawAnnotationDetails
public abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getMagicDrawAnnotationDetails([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)
Specified by:
`[getMagicDrawAnnotationDetails](helpers/BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
getProject
@OpenApipublic [Project](../core/Project.html) getProject()
Returns current project
Specified by:
`[getProject](helpers/BaseEmfUml2Helper.html#getProject())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
project
getMDStandardProfiles
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getMDStandardProfiles()
getMDProjectBuiltinProfiles
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getMDProjectBuiltinProfiles()
Description copied from interface: `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles())`
Returns profiles that are "built-in" in MagicDraw project
Specified by:
`[getMDProjectBuiltinProfiles](helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
getLogger
@OpenApipublic [EmfUml2Logger](EmfUml2Logger.html) getLogger()
Returns logger.
Specified by:
`[getLogger](helpers/BaseEmfUml2Helper.html#getLogger())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
logger
markMappedElement
@OpenApipublic void markMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.
Specified by:
`[markMappedElement](helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
isMappedElement
@OpenApipublic boolean isMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is mapped.
Specified by:
`[isMappedElement](helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
Returns:
true - if mapped.
markSkippedElement
@OpenApipublic void markSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Mark skipped element.
Specified by:
`[markSkippedElement](helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
isRemovableElement
@OpenApipublic boolean isRemovableElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)
Specified by:
`[isRemovableElement](helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
Returns:
true - if will element should be removed or are alredy removed.
markRemovableElement
public void markRemovableElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Mark element that will be removed or already disposed
Specified by:
`[markRemovableElement](helpers/BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
getFinalizeActivities
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FinalizeActivity](FinalizeActivity.html)> getFinalizeActivities()
Specified by:
`[getFinalizeActivities](helpers/BaseEmfUml2Helper.html#getFinalizeActivities())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
isSkippedElement
@OpenApipublic boolean isSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is skipped.
Specified by:
`[isSkippedElement](helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
getPersistenceHelper
public com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper getPersistenceHelper()
Specified by:
`[getPersistenceHelper](helpers/BaseEmfUml2Helper.html#getPersistenceHelper())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
addCreatedElementIDData
public void addCreatedElementIDData([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) relatedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)
Specified by:
`[addCreatedElementIDData](helpers/BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
getCreatedElementsIDData
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getCreatedElementsIDData()
Specified by:
`[getCreatedElementsIDData](helpers/BaseEmfUml2Helper.html#getCreatedElementsIDData())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
clearCreatedElementsIDData
public void clearCreatedElementsIDData()
Specified by:
`[clearCreatedElementsIDData](helpers/BaseEmfUml2Helper.html#clearCreatedElementsIDData())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
getElementName
@OpenApipublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 boolean qualifiedName)
Returns element human name.
Parameters:
`mdElement` -
`qualifiedName` -
Returns:
element type + [qualified] name
initProgressStatus
public static void initProgressStatus([ProgressStatus](../../task/ProgressStatus.html) progress,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 boolean indeterminate)
removeElement
public static void removeElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection)
setMDElementID
public void setMDElementID([BaseElement](../uml/BaseElement.html) mdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Set MD element id according given EMF element id. If there is id's conflict id is not changed.
Specified by:
`[setMDElementID](helpers/BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`mdElement` - MD element
`eElement` - EMF element
getEmfOptionsGroup
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html) getEmfOptionsGroup()
Deprecated.
Use [`BaseEmfUml2Helper.getOptions()`](helpers/BaseEmfUml2Helper.html#getOptions())
Returns:
getOptions
public [BaseOptions](envoptions/BaseOptions.html) getOptions()
Specified by:
`[getOptions](helpers/BaseEmfUml2Helper.html#getOptions())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
getEElementName
@OpenApipublic final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEElementName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Returns element human name.
Specified by:
`[getEElementName](helpers/BaseEElementNameRetriever.html#getEElementName(java.lang.Object))` in interface `[BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html)`
Specified by:
`[getEElementName](helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`eElement` -
Returns:
element type + qualified name
addFinalizeActivity
public void addFinalizeActivity([FinalizeActivity](FinalizeActivity.html) activity)
Specified by:
`[addFinalizeActivity](helpers/BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
getUml2MetaModel
public abstract [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getUml2MetaModel()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi</a></div>
<h1 class="title" title="Class BaseEmfUml2Helper">Class BaseEmfUml2Helper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="v2/EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">BaseEmfUml2Helper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></span></div>
<div class="block">Eclipse UML2 XMI helper.</div>
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
<div class="col-first even-row-color"><code>protected static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAGICDRAW_SOURCE">MAGICDRAW_SOURCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MD_ID">MD_ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_PROPERTY_NAME">MD_PROPERTY_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger)">BaseEmfUml2Helper</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> createdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> relatedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a><wbr/>(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDataTypeMap()">createDataTypeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEElementNameRetriever()">createEElementNameRetriever</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatedElementsIDData()">getCreatedElementsIDData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEElementName(java.lang.Object)">getEElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 boolean qualifiedName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEmfOptionsGroup()">getEmfOptionsGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="helpers/BaseEmfUml2Helper.html#getOptions()"><code>BaseEmfUml2Helper.getOptions()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFinalizeActivities()">getFinalizeActivities</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLogger()">getLogger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns logger.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns profiles that are "built-in" in MagicDraw project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMDStandardProfiles()">getMDStandardProfiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPersistenceHelper()">getPersistenceHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUml2DataTypeMap()">getUml2DataTypeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns datatype map</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUml2MetaModel()">getUml2MetaModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)">initProgressStatus</a><wbr/>(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean indeterminate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMappedElement(java.lang.Object)">isMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element is mapped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemovableElement(java.lang.Object)">isRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if element will be removed or already disposed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSkippedElement(java.lang.Object)">isSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element is skipped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markMappedElement(java.lang.Object)">markMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks that element is mapped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markRemovableElement(java.lang.Object)">markRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Mark element that will be removed or already disposed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markSkippedElement(java.lang.Object)">markSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Mark skipped element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">removeElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> mdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set MD element id according given EMF element id.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="MAGICDRAW_SOURCE">
<h3>MAGICDRAW_SOURCE</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MAGICDRAW_SOURCE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MAGICDRAW_SOURCE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_ID">
<h3>MD_ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MD_ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MD_ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MD_PROPERTY_NAME">
<h3>MD_PROPERTY_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MD_PROPERTY_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper.MD_PROPERTY_NAME">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger)">
<h3>BaseEmfUml2Helper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BaseEmfUml2Helper</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</span></div>
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
<section class="detail" id="getUml2DataTypeMap()">
<h3>getUml2DataTypeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</span> <span class="element-name">getUml2DataTypeMap</span>()</div>
<div class="block">Returns datatype map</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>datatypes map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDataTypeMap()">
<h3>createDataTypeMap</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</span> <span class="element-name">createDataTypeMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createEElementNameRetriever()">
<h3>createEElementNameRetriever</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></span> <span class="element-name">createEElementNameRetriever</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMagicDrawAnnotationDetails(java.lang.Object,boolean)">
<h3>getMagicDrawAnnotationDetails</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getMagicDrawAnnotationDetails</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns current project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getProject()">getProject</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDStandardProfiles()">
<h3>getMDStandardProfiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getMDStandardProfiles</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMDProjectBuiltinProfiles()">
<h3>getMDProjectBuiltinProfiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getMDProjectBuiltinProfiles</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">BaseEmfUml2Helper</a></code></span></div>
<div class="block">Returns profiles that are "built-in" in MagicDraw project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLogger()">
<h3>getLogger</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></span> <span class="element-name">getLogger</span>()</div>
<div class="block">Returns logger.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getLogger()">getLogger</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>logger</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markMappedElement(java.lang.Object)">
<h3>markMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">markMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMappedElement(java.lang.Object)">
<h3>isMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is mapped.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
<dt>Returns:</dt>
<dd>true - if mapped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markSkippedElement(java.lang.Object)">
<h3>markSkippedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">markSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Mark skipped element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemovableElement(java.lang.Object)">
<h3>isRemovableElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
<dt>Returns:</dt>
<dd>true - if will element should be removed or are alredy removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markRemovableElement(java.lang.Object)">
<h3>markRemovableElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">markRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Mark element that will be removed or already disposed</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFinalizeActivities()">
<h3>getFinalizeActivities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a>&gt;</span> <span class="element-name">getFinalizeActivities</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSkippedElement(java.lang.Object)">
<h3>isSkippedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is skipped.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPersistenceHelper()">
<h3>getPersistenceHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</span> <span class="element-name">getPersistenceHelper</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">
<h3>addCreatedElementIDData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCreatedElementIDData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> createdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> relatedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreatedElementsIDData()">
<h3>getCreatedElementsIDData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getCreatedElementsIDData</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCreatedElementsIDData()">
<h3>clearCreatedElementsIDData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCreatedElementsIDData</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 boolean qualifiedName)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdElement</code> - </dd>
<dd><code>qualifiedName</code> - </dd>
<dt>Returns:</dt>
<dd>element type + [qualified] name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)">
<h3>initProgressStatus</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initProgressStatus</span><wbr/><span class="parameters">(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 boolean indeterminate)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>removeElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
</section>
</li>
<li>
<section class="detail" id="setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">
<h3>setMDElementID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMDElementID</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> mdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Set MD element id according given EMF element id. If there is id's conflict id is not changed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>mdElement</code> - MD element</dd>
<dd><code>eElement</code> - EMF element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEmfOptionsGroup()">
<h3>getEmfOptionsGroup</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></span> <span class="element-name">getEmfOptionsGroup</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="helpers/BaseEmfUml2Helper.html#getOptions()"><code>BaseEmfUml2Helper.getOptions()</code></a></div>
</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></span> <span class="element-name">getOptions</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getOptions()">getOptions</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEElementName(java.lang.Object)">
<h3>getEElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEElementNameRetriever.html#getEElementName(java.lang.Object)">getEElementName</a></code> in interface <code><a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>eElement</code> - </dd>
<dt>Returns:</dt>
<dd>element type + qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">
<h3>addFinalizeActivity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addFinalizeActivity</span><wbr/><span class="parameters">(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUml2MetaModel()">
<h3>getUml2MetaModel</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getUml2MetaModel</span>()</div>
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
