# JAVA OPENAPI: AnyToAnyModelTransformation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/modeltransformations/impl/any_to_any/AnyToAnyModelTransformation.html
- source_path: `com/nomagic/magicdraw/modeltransformations/impl/any_to_any/AnyToAnyModelTransformation.html`
- source_sha256: `7cfcd5b17a48575f3d50d6bb59a8e815aa9babe89557f6f40eb52a29621f2653`
- captured_utc: `2026-07-14T16:51:25.922265+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations.impl.any_to_any](package-summary.html)

## Class AnyToAnyModelTransformation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformation

All Implemented Interfaces:
`[ModelTransformation](../../ModelTransformation.html)`

@OpenApiAllpublic classAnyToAnyModelTransformation
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ModelTransformation](../../ModelTransformation.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>>`
`[mTransformationMap](#mTransformationMap)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AnyToAnyModelTransformation](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[afterTransformation](#afterTransformation())()`
Method invoked after all custom transformations.
`protected void`
`[changeDiagramType](#changeDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.DiagramType))([DiagramPresentationElement](../../../uml/symbols/DiagramPresentationElement.html) dpe,
 [DiagramType](../../../uml/DiagramType.html) createDiagramType)`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[collectInnerElements](#collectInnerElements(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects,
 boolean update)`

`protected [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[copyElementInto](#copyElementInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)`
Copies and pastes given element.
`protected com.nomagic.magicdraw.commands.MacroCommand`
`[copyElements](#copyElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects)`
Copies elements
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[createDefaultDoNotCopyTypes](#createDefaultDoNotCopyTypes())()`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[createDefaultDoNotReconnectTypes](#createDefaultDoNotReconnectTypes())()`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[createDefaultDoNotSettableProperties](#createDefaultDoNotSettableProperties())()`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[createDefaultMappedTypes](#createDefaultMappedTypes())()`

`protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.ElementUpdater`
`[createElementUpdater](#createElementUpdater())()`

`protected void`
`[customTransformationForElement](#customTransformationForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mapped)`
Custom transformations should override this method to add additional functionality.
`protected void`
`[customTransformations](#customTransformations())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getMappedElements](#getMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)`
Returns transformed elements for given original element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[getNotSettableProperties](#getNotSettableProperties())()`

`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../../uml/BaseElement.html),[BaseElement](../../../uml/BaseElement.html)>`
`[getOneToOneMap](#getOneToOneMap())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOriginalElement](#getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped)`
Returns original elements which are mapped to given mapped element.
`<T extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[getOriginalElement](#getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)`
Returns original elements which are mapped to given mapped element.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOriginalElements](#getOriginalElements())()`

`protected [ProgressStatus](../../../../task/ProgressStatus.html)`
`[getProgressStatus](#getProgressStatus())()`

`[PropertyManager](../../../properties/PropertyManager.html)`
`[getPropertyManager](#getPropertyManager())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRemovedByCustomTransformation](#getRemovedByCustomTransformation())()`

`<T extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[getTarget](#getTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)`
Returns transformed element that's transformation source is 'original' element and it's type is specified in 'type'
`[Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getTransformationsPackage](#getTransformationsPackage())()`

`protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.TypeMapper`
`[getTypeMapper](#getTypeMapper())()`

`void`
`[invokeCustomTransformation](#invokeCustomTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)`
Invokes custom transformation for element.
`void`
`[invokeCustomTransformation](#invokeCustomTransformation(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> original)`
Invokes custom transformation for collection.
`protected boolean`
`[isAlreadyVisited](#isAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`protected boolean`
`[isElementCopied](#isElementCopied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`protected boolean`
`[isMappableElement](#isMappableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`protected boolean`
`[isSkipElement](#isSkipElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if element should be skipped
`boolean`
`[isTransformationInPlace](#isTransformationInPlace())()`

`boolean`
`[isTypeMapSet](#isTypeMapSet())()`

`protected void`
`[markAsAlreadyVisited](#markAsAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`protected void`
`[processMappedElements](#processMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> originalMappedElements)`

`protected void`
`[processMappingResult](#processMappingResult(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> originalMappedElements)`

`void`
`[setTask](#setTask(com.nomagic.task.Task))([Task](../../../../task/Task.html) task)`
Sets task for transformation.
`protected void`
`[setTransformationMapValue](#setTransformationMapValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements)`

`protected void`
`[sortOriginalElements](#sortOriginalElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects)`
Sorts elements before invoking custom transformation
`[Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[transform](#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectedObjects,
 [ModelTransformationInfo](../../ModelTransformationInfo.html) info,
 [TypeMapProfile](../../TypeMapProfile.html) typeMap,
 [PropertyManager](../../../properties/PropertyManager.html) propertyManager,
 [Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)`
Performs transformation on specific set of objects
`protected com.nomagic.magicdraw.commands.MacroCommand`
`[updateDiagrams](#updateDiagrams())()`
Updates diagram with newly added elements during transformation update phase.
`void`
`[updateTransform](#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean))([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformationPackage,
 [TypeMapProfile](../../TypeMapProfile.html) typeMap,
 [PropertyManager](../../../properties/PropertyManager.html) propertyManager,
 boolean syncDestination)`
Updates transformation on specific set of objects
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
mTransformationMap
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> mTransformationMap
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AnyToAnyModelTransformation
public AnyToAnyModelTransformation()
 ============ METHOD DETAIL ========== 
Method Details
createDefaultDoNotCopyTypes
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> createDefaultDoNotCopyTypes()
createDefaultDoNotReconnectTypes
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> createDefaultDoNotReconnectTypes()
createDefaultDoNotSettableProperties
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> createDefaultDoNotSettableProperties()
createDefaultMappedTypes
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> createDefaultMappedTypes()
transform
@CheckForNullpublic [Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transform(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectedObjects,
 @CheckForNull
 [ModelTransformationInfo](../../ModelTransformationInfo.html) info,
 [TypeMapProfile](../../TypeMapProfile.html) typeMap,
 [PropertyManager](../../../properties/PropertyManager.html) propertyManager,
 [Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)
 throws [ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)
Description copied from interface: `[ModelTransformation](../../ModelTransformation.html#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`
Performs transformation on specific set of objects
Specified by:
`[transform](../../ModelTransformation.html#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))` in interface `[ModelTransformation](../../ModelTransformation.html)`
Parameters:
`selectedObjects` - set of objects to transform
`info` - model transformation info
`typeMap` - type map profile to use for transformation, null for none
`propertyManager` - transformation properties
`destination` - destination model packages, null for transformation in place
Returns:
transformation model package (where transformation links are stored)
Throws:
`[ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)` - in case target model elements are read-only
afterTransformation
protected void afterTransformation()
 throws [ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)
Method invoked after all custom transformations.
Throws:
`[ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)` - in case of error
customTransformations
protected void customTransformations()
isSkipElement
protected boolean isSkipElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if element should be skipped
Parameters:
`element` - element
Returns:
true if element can not be processed by custom transformation
invokeCustomTransformation
public void invokeCustomTransformation([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> original)
Invokes custom transformation for collection.
Parameters:
`original` - original elements
See Also:
[`invokeCustomTransformation(Element)`](#invokeCustomTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))
invokeCustomTransformation
public void invokeCustomTransformation([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)
Invokes custom transformation for element. If custom transformation was already invoked, this method does nothing.
Parameters:
`original` - original element for which custom transformation is invoked.
processMappingResult
protected void processMappingResult([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> originalMappedElements)
processMappedElements
protected void processMappedElements([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> originalMappedElements)
setTransformationMapValue
protected void setTransformationMapValue([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mappedElements)
customTransformationForElement
protected void customTransformationForElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> mapped)
 throws [ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)
Custom transformations should override this method to add additional functionality.
Parameters:
`original` - original element.
`mapped` - collection of current mapped elements. Custom transformation can modify this collection. In case custom transformation needs to remove current mapping, it should remove element from this collection. In case it needs to map more elements it should add new elements to this collection.
Throws:
`[ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)` - in case of error
getMappedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getMappedElements([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original)
Returns transformed elements for given original element.
Parameters:
`original` - original element.
Returns:
mapped elements if original was mapped; empty collection if original was mapped to nothing;
updateTransform
public void updateTransform([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformationPackage,
 [TypeMapProfile](../../TypeMapProfile.html) typeMap,
 [PropertyManager](../../../properties/PropertyManager.html) propertyManager,
 boolean syncDestination)
 throws [ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)
Description copied from interface: `[ModelTransformation](../../ModelTransformation.html#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean))`
Updates transformation on specific set of objects
Specified by:
`[updateTransform](../../ModelTransformation.html#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean))` in interface `[ModelTransformation](../../ModelTransformation.html)`
Parameters:
`transformationPackage` - package containing transformation links
`typeMap` - type map profile to use for transformation, null for none
`propertyManager` - transformation properties
`syncDestination` - true for destination overwrite
Throws:
`[ReadOnlyElementException](../../../openapi/uml/ReadOnlyElementException.html)` - in case target model elements are read-only
getOriginalElements
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOriginalElements()
Returns:
all original elements.
getOriginalElement
public <T extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> getOriginalElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)
Returns original elements which are mapped to given mapped element.
Parameters:
`mapped` - original elements that are mapped to this element will be returned
`type` - only this type of elements will be returned.
Returns:
collection of original elements. If there is no original elements returns empty list.
getOriginalElement
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOriginalElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mapped)
Returns original elements which are mapped to given mapped element.
Parameters:
`mapped` - mapped element
Returns:
collection of original elements. If there is no original elements returns empty list.
copyElements
protected com.nomagic.magicdraw.commands.MacroCommand copyElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects)
Copies elements
Parameters:
`objects` - objects
Returns:
command for copying
createElementUpdater
protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.ElementUpdater createElementUpdater()
Returns:
element updater.
getOneToOneMap
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[BaseElement](../../../uml/BaseElement.html),[BaseElement](../../../uml/BaseElement.html)> getOneToOneMap()
Returns:
map where one key is mapped only to one element
getTypeMapper
protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.TypeMapper getTypeMapper()
Returns:
type mapper.
getTarget
@CheckForNullpublic <T extends [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T getTarget([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) original,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)
Returns transformed element that's transformation source is 'original' element and it's type is specified in 'type'
Parameters:
`original` - source model element.
`type` - type of returned element.
Returns:
transformed element. If no element found - null is returned.
updateDiagrams
protected com.nomagic.magicdraw.commands.MacroCommand updateDiagrams()
Updates diagram with newly added elements during transformation update phase.
Returns:
update macro command
sortOriginalElements
protected void sortOriginalElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects)
Sorts elements before invoking custom transformation
Parameters:
`objects` - objects
collectInnerElements
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collectInnerElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> objects,
 boolean update)
isMappableElement
protected boolean isMappableElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Parameters:
`element` - element to check.
Returns:
true if transformation can be applied for this element.
getTransformationsPackage
public [Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getTransformationsPackage()
Returns:
package where transformation information is stored
isTransformationInPlace
public boolean isTransformationInPlace()
Returns:
true if transformation is in place (not copying)
getPropertyManager
public [PropertyManager](../../../properties/PropertyManager.html) getPropertyManager()
Returns:
property manager for additional transformation properties
copyElementInto
protected [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) copyElementInto([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)
Copies and pastes given element.
Parameters:
`source` - element to copy.
`parent` - parent where place copied element.
Returns:
copied element.
setTask
public void setTask([Task](../../../../task/Task.html) task)
Description copied from interface: `[ModelTransformation](../../ModelTransformation.html#setTask(com.nomagic.task.Task))`
Sets task for transformation. Transformation can use Task for accesing progress status and etc.
Specified by:
`[setTask](../../ModelTransformation.html#setTask(com.nomagic.task.Task))` in interface `[ModelTransformation](../../ModelTransformation.html)`
Parameters:
`task` - transformation task
getProgressStatus
protected [ProgressStatus](../../../../task/ProgressStatus.html) getProgressStatus()
isElementCopied
protected boolean isElementCopied([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isTypeMapSet
public boolean isTypeMapSet()
getNotSettableProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) getNotSettableProperties()
changeDiagramType
protected void changeDiagramType([DiagramPresentationElement](../../../uml/symbols/DiagramPresentationElement.html) dpe,
 [DiagramType](../../../uml/DiagramType.html) createDiagramType)
getRemovedByCustomTransformation
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRemovedByCustomTransformation()
markAsAlreadyVisited
protected void markAsAlreadyVisited([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAlreadyVisited
protected boolean isAlreadyVisited([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations.impl.any_to_any</a></div>
<h1 class="title" title="Class AnyToAnyModelTransformation">Class AnyToAnyModelTransformation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformation</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AnyToAnyModelTransformation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></span></div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mTransformationMap">mTransformationMap</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AnyToAnyModelTransformation</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterTransformation()">afterTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method invoked after all custom transformations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changeDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.DiagramType)">changeDiagramType</a><wbr/>(<a href="../../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> dpe,
 <a href="../../../uml/DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> createDiagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInnerElements(java.util.Collection,boolean)">collectInnerElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects,
 boolean update)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copyElementInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">copyElementInto</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copies and pastes given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.commands.MacroCommand</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copyElements(java.util.List)">copyElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copies elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultDoNotCopyTypes()">createDefaultDoNotCopyTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultDoNotReconnectTypes()">createDefaultDoNotReconnectTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultDoNotSettableProperties()">createDefaultDoNotSettableProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultMappedTypes()">createDefaultMappedTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.ElementUpdater</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementUpdater()">createElementUpdater</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#customTransformationForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">customTransformationForElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mapped)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Custom transformations should override this method to add additional functionality.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#customTransformations()">customTransformations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getMappedElements</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transformed elements for given original element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotSettableProperties()">getNotSettableProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOneToOneMap()">getOneToOneMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOriginalElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns original elements which are mapped to given mapped element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">getOriginalElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns original elements which are mapped to given mapped element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalElements()">getOriginalElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProgressStatus()">getProgressStatus</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyManager()">getPropertyManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemovedByCustomTransformation()">getRemovedByCustomTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">getTarget</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transformed element that's transformation source is 'original' element and it's type is specified in 'type'</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationsPackage()">getTransformationsPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.modeltransformations.impl.any_to_any.TypeMapper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeMapper()">getTypeMapper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeCustomTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">invokeCustomTransformation</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invokes custom transformation for element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeCustomTransformation(java.util.Collection)">invokeCustomTransformation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; original)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invokes custom transformation for collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAlreadyVisited</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementCopied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementCopied</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMappableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isMappableElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSkipElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSkipElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if element should be skipped</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransformationInPlace()">isTransformationInPlace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeMapSet()">isTypeMapSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markAsAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">markAsAlreadyVisited</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection)">processMappedElements</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; originalMappedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processMappingResult(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection)">processMappingResult</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; originalMappedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTask(com.nomagic.task.Task)">setTask</a><wbr/>(<a href="../../../../task/Task.html" title="class in com.nomagic.task">Task</a> task)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets task for transformation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformationMapValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setTransformationMapValue</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortOriginalElements(java.util.List)">sortOriginalElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sorts elements before invoking custom transformation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">transform</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectedObjects,
 <a href="../../ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info,
 <a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs transformation on specific set of objects</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.commands.MacroCommand</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDiagrams()">updateDiagrams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates diagram with newly added elements during transformation update phase.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">updateTransform</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformationPackage,
 <a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean syncDestination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates transformation on specific set of objects</div>
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
<section class="detail" id="mTransformationMap">
<h3>mTransformationMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt;</span> <span class="element-name">mTransformationMap</span></div>
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
<h3>AnyToAnyModelTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnyToAnyModelTransformation</span>()</div>
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
<section class="detail" id="createDefaultDoNotCopyTypes()">
<h3>createDefaultDoNotCopyTypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">createDefaultDoNotCopyTypes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultDoNotReconnectTypes()">
<h3>createDefaultDoNotReconnectTypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">createDefaultDoNotReconnectTypes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultDoNotSettableProperties()">
<h3>createDefaultDoNotSettableProperties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">createDefaultDoNotSettableProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createDefaultMappedTypes()">
<h3>createDefaultMappedTypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">createDefaultMappedTypes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>transform</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">transform</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectedObjects,
 @CheckForNull
 <a href="../../ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info,
 <a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</span>
                  throws <span class="exceptions"><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformation.html#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">ModelTransformation</a></code></span></div>
<div class="block">Performs transformation on specific set of objects</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ModelTransformation.html#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">transform</a></code> in interface <code><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></dd>
<dt>Parameters:</dt>
<dd><code>selectedObjects</code> - set of objects to transform</dd>
<dd><code>info</code> - model transformation info</dd>
<dd><code>typeMap</code> - type map profile to use for transformation, null for none</dd>
<dd><code>propertyManager</code> - transformation properties</dd>
<dd><code>destination</code> - destination model packages, null for transformation in place</dd>
<dt>Returns:</dt>
<dd>transformation model package (where transformation links are stored)</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case target model elements are read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterTransformation()">
<h3>afterTransformation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterTransformation</span>()
                            throws <span class="exceptions"><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Method invoked after all custom transformations.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case of error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="customTransformations()">
<h3>customTransformations</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">customTransformations</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSkipElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSkipElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSkipElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if element should be skipped</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element can not be processed by custom transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeCustomTransformation(java.util.Collection)">
<h3>invokeCustomTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">invokeCustomTransformation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; original)</span></div>
<div class="block">Invokes custom transformation for collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#invokeCustomTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>invokeCustomTransformation(Element)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeCustomTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>invokeCustomTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">invokeCustomTransformation</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</span></div>
<div class="block">Invokes custom transformation for element. If custom transformation was already invoked, this method does nothing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original element for which custom transformation is invoked.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="processMappingResult(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection)">
<h3>processMappingResult</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">processMappingResult</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; originalMappedElements)</span></div>
</section>
</li>
<li>
<section class="detail" id="processMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Collection)">
<h3>processMappedElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">processMappedElements</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; originalMappedElements)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTransformationMapValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setTransformationMapValue</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setTransformationMapValue</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mappedElements)</span></div>
</section>
</li>
<li>
<section class="detail" id="customTransformationForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>customTransformationForElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">customTransformationForElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; mapped)</span>
                                       throws <span class="exceptions"><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Custom transformations should override this method to add additional functionality.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original element.</dd>
<dd><code>mapped</code> - collection of current mapped elements. Custom transformation can modify this collection. In case custom transformation needs to remove current mapping, it should remove element from this collection. In case it needs to map more elements it should add new elements to this collection.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case of error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMappedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getMappedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getMappedElements</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original)</span></div>
<div class="block">Returns transformed elements for given original element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - original element.</dd>
<dt>Returns:</dt>
<dd>mapped elements if original was mapped; empty collection if original was mapped to nothing;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">
<h3>updateTransform</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateTransform</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformationPackage,
 <a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean syncDestination)</span>
                     throws <span class="exceptions"><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformation.html#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">ModelTransformation</a></code></span></div>
<div class="block">Updates transformation on specific set of objects</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ModelTransformation.html#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">updateTransform</a></code> in interface <code><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></dd>
<dt>Parameters:</dt>
<dd><code>transformationPackage</code> - package containing transformation links</dd>
<dd><code>typeMap</code> - type map profile to use for transformation, null for none</dd>
<dd><code>propertyManager</code> - transformation properties</dd>
<dd><code>syncDestination</code> - true for destination overwrite</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case target model elements are read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalElements()">
<h3>getOriginalElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOriginalElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all original elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>getOriginalElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">getOriginalElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Returns original elements which are mapped to given mapped element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapped</code> - original elements that are mapped to this element will be returned</dd>
<dd><code>type</code> - only this type of elements will be returned.</dd>
<dt>Returns:</dt>
<dd>collection of original elements. If there is no original elements returns empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOriginalElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOriginalElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mapped)</span></div>
<div class="block">Returns original elements which are mapped to given mapped element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapped</code> - mapped element</dd>
<dt>Returns:</dt>
<dd>collection of original elements. If there is no original elements returns empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyElements(java.util.List)">
<h3>copyElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.commands.MacroCommand</span> <span class="element-name">copyElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects)</span></div>
<div class="block">Copies elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objects</code> - objects</dd>
<dt>Returns:</dt>
<dd>command for copying</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createElementUpdater()">
<h3>createElementUpdater</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.modeltransformations.impl.any_to_any.ElementUpdater</span> <span class="element-name">createElementUpdater</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element updater.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOneToOneMap()">
<h3>getOneToOneMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>,<wbr/><a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getOneToOneMap</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map where one key is mapped only to one element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeMapper()">
<h3>getTypeMapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.modeltransformations.impl.any_to_any.TypeMapper</span> <span class="element-name">getTypeMapper</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type mapper.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getTarget</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
<div class="block">Returns transformed element that's transformation source is 'original' element and it's type is specified in 'type'</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>original</code> - source model element.</dd>
<dd><code>type</code> - type of returned element.</dd>
<dt>Returns:</dt>
<dd>transformed element. If no element found - null is returned.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateDiagrams()">
<h3>updateDiagrams</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.commands.MacroCommand</span> <span class="element-name">updateDiagrams</span>()</div>
<div class="block">Updates diagram with newly added elements during transformation update phase.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>update macro command</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortOriginalElements(java.util.List)">
<h3>sortOriginalElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">sortOriginalElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects)</span></div>
<div class="block">Sorts elements before invoking custom transformation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objects</code> - objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInnerElements(java.util.Collection,boolean)">
<h3>collectInnerElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectInnerElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; objects,
 boolean update)</span></div>
</section>
</li>
<li>
<section class="detail" id="isMappableElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isMappableElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isMappableElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check.</dd>
<dt>Returns:</dt>
<dd>true if transformation can be applied for this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformationsPackage()">
<h3>getTransformationsPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getTransformationsPackage</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>package where transformation information is stored</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTransformationInPlace()">
<h3>isTransformationInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTransformationInPlace</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transformation is in place (not copying)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyManager()">
<h3>getPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getPropertyManager</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property manager for additional transformation properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyElementInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>copyElementInto</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">copyElementInto</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</span></div>
<div class="block">Copies and pastes given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - element to copy.</dd>
<dd><code>parent</code> - parent where place copied element.</dd>
<dt>Returns:</dt>
<dd>copied element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTask(com.nomagic.task.Task)">
<h3>setTask</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTask</span><wbr/><span class="parameters">(<a href="../../../../task/Task.html" title="class in com.nomagic.task">Task</a> task)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformation.html#setTask(com.nomagic.task.Task)">ModelTransformation</a></code></span></div>
<div class="block">Sets task for transformation. Transformation can use Task for accesing progress status and etc.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ModelTransformation.html#setTask(com.nomagic.task.Task)">setTask</a></code> in interface <code><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></dd>
<dt>Parameters:</dt>
<dd><code>task</code> - transformation task</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProgressStatus()">
<h3>getProgressStatus</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a></span> <span class="element-name">getProgressStatus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isElementCopied(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isElementCopied</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isElementCopied</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTypeMapSet()">
<h3>isTypeMapSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeMapSet</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNotSettableProperties()">
<h3>getNotSettableProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getNotSettableProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="changeDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.DiagramType)">
<h3>changeDiagramType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">changeDiagramType</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> dpe,
 <a href="../../../uml/DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> createDiagramType)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRemovedByCustomTransformation()">
<h3>getRemovedByCustomTransformation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRemovedByCustomTransformation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="markAsAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>markAsAlreadyVisited</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">markAsAlreadyVisited</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAlreadyVisited(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAlreadyVisited</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isAlreadyVisited</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
