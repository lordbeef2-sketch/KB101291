# JAVA OPENAPI: ConvertElementInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/ConvertElementInfo.html
- source_path: `com/nomagic/magicdraw/uml/ConvertElementInfo.html`
- source_sha256: `d27bcecec7a1f535509e38785ace825930a35e140a6636c351883bfb2b3a5df0`
- captured_utc: `2026-07-14T16:55:54.476447+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class ConvertElementInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.ConvertElementInfo

All Implemented Interfaces:
`[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[ConvertElementInfo](ConvertElementInfo.html)>`

@OpenApiAllpublic classConvertElementInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[ConvertElementInfo](ConvertElementInfo.html)>

Holds information which controls the process of element conversion,
 for example allows to define target element type and preferred symbol type.

See Also:
[`Refactoring`](Refactoring.html)
[`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
[`PresentationElement`](symbols/PresentationElement.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[ConvertElementInfo.DisposeSourceValidator](ConvertElementInfo.DisposeSourceValidator.html)`
Validates whether source should be disposed after conversion.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ConvertElementInfo](#%3Cinit%3E(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType)`
Constructs this info.
`[ConvertElementInfo](#%3Cinit%3E(java.lang.Class,boolean))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 boolean canInfoBeLost)`
Constructs this info.
`[ConvertElementInfo](#%3Cinit%3E(java.lang.Class,java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)> symbolType)`
Constructs this info.
`[ConvertElementInfo](#%3Cinit%3E(java.lang.String,java.lang.Class,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 boolean createSymbol)`
Constructs this info.
`[ConvertElementInfo](#%3Cinit%3E(java.lang.String,java.lang.Class,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)> symbolType)`
Constructs this info.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[canChangeElement](#canChangeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Indicates if element can be changed by conversion.
`boolean`
`[canConvert](#canConvert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Indicates if element can be converted.
`boolean`
`[canInfoBeLost](#canInfoBeLost(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source)`
Indicates if info can be lost for a given source element.
`int`
`[compareTo](#compareTo(com.nomagic.magicdraw.uml.ConvertElementInfo))([ConvertElementInfo](ConvertElementInfo.html) o)`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[getAdditionalStereotypes](#getAdditionalStereotypes())()`

`[ConvertElementInfoCategory](ConvertElementInfoCategory.html)`
`[getCategory](#getCategory())()`

`[ConvertElementInfo.DisposeSourceValidator](ConvertElementInfo.DisposeSourceValidator.html)`
`[getDisposeSourceValidator](#getDisposeSourceValidator())()`
Gets dispose source validator.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementIDSuffix](#getElementIDSuffix())()`
Gets element ID suffix.
`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElementType](#getElementType())()`
Gets type of the element to which to convert.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Gets human-readable format of the conversion.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets name of conversion.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject>`
`[getPendingMapping](#getPendingMapping())()`

`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)>`
`[getSymbolType](#getSymbolType())()`
Type of the symbol to which to convert.
`int`
`[hashCode](#hashCode())()`

`boolean`
`[isCanChangeElementName](#isCanChangeElementName())()`
Gets can change element name flag value.
`boolean`
`[isConvertingSourceEditable](#isConvertingSourceEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source)`
Indicates if source element is editable
`boolean`
`[isConvertOnlyIncomingReferences](#isConvertOnlyIncomingReferences())()`
Gets convert only incoming references flag value.
`boolean`
`[isConvertRelatedElements](#isConvertRelatedElements())()`

`boolean`
`[isCreateSymbol](#isCreateSymbol())()`
Gets create symbol flag value.
`boolean`
`[isDisposeSource](#isDisposeSource())()`
Indicates if source should be disposed after conversion.
`boolean`
`[isPreserveElementID](#isPreserveElementID())()`
Gets preserve element ID flag value.
`boolean`
`[isRemoveFromCollections](#isRemoveFromCollections())()`
If the method returns true then convert should remove a value from the source element collection.
`boolean`
`[isReplaceSourcePresentationElement](#isReplaceSourcePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](symbols/PresentationElement.html) sourcePresentationElement)`
Check if source presentation element may be replaced.
`void`
`[setAdditionalStereotypes](#setAdditionalStereotypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Set stereotypes to apply to converted element after conversion
`void`
`[setCanChangeElementName](#setCanChangeElementName(boolean))(boolean canChangeElementName)`
Sets can change element name flag value.
`void`
`[setCanInfoBeLost](#setCanInfoBeLost(boolean))(boolean canInfoBeLost)`
Sets info can be lost flag value.
`void`
`[setCategory](#setCategory(com.nomagic.magicdraw.uml.ConvertElementInfoCategory))([ConvertElementInfoCategory](ConvertElementInfoCategory.html) category)`
Set category of info used for grouping of targets in UI.
`void`
`[setConvertOnlyIncomingReferences](#setConvertOnlyIncomingReferences(boolean))(boolean convertOnlyIncomingReferences)`
Sets convert only incoming references flag value.
`void`
`[setConvertRelatedElements](#setConvertRelatedElements(boolean))(boolean convertRelatedElements)`
Set flag for related elements converting
`void`
`[setCreateSymbol](#setCreateSymbol(boolean))(boolean createSymbol)`
Sets create symbol flag value.
`void`
`[setDisposeSourceValidator](#setDisposeSourceValidator(com.nomagic.magicdraw.uml.ConvertElementInfo.DisposeSourceValidator))([ConvertElementInfo.DisposeSourceValidator](ConvertElementInfo.DisposeSourceValidator.html) disposeSourceValidator)`
Sets dispose source validator.
`void`
`[setElementIDSuffix](#setElementIDSuffix(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementIDSuffix)`
Sets element ID suffix.
`void`
`[setPendingMapping](#setPendingMapping(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject> pendingMapping)`
Sets mapping for elements which will be converted later
`void`
`[setPreserveElementID](#setPreserveElementID(boolean))(boolean preserveElementID)`
Deprecated.
it is not recommended to use this setting as preserving ids can break model consistency if some situations
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ConvertElementInfo
public ConvertElementInfo(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)> symbolType)
Constructs this info.
Parameters:
`name` - name of conversion.
`elementType` - type to which to convert.
`symbolType` - preferred symbol type to which to convert.
ConvertElementInfo
public ConvertElementInfo([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)> symbolType)
Constructs this info.
Parameters:
`elementType` - type to which to convert.
`symbolType` - preferred symbol type to which to convert.
ConvertElementInfo
public ConvertElementInfo(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 boolean createSymbol)
Constructs this info.
Parameters:
`name` - name of conversion.
`elementType` - type to which to convert.
`createSymbol` - indicates if symbol should be created with this conversion.
ConvertElementInfo
public ConvertElementInfo([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType)
Constructs this info.
Parameters:
`elementType` - type to which to convert.
ConvertElementInfo
public ConvertElementInfo([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementType,
 boolean canInfoBeLost)
Constructs this info.
Parameters:
`elementType` - type to which to convert.
`canInfoBeLost` - indicates if info can be lost by conversion.
 ============ METHOD DETAIL ========== 
Method Details
getName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Gets name of conversion.
Returns:
name of conversion.
getElementType
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElementType()
Gets type of the element to which to convert.
Returns:
type of the element to which to convert.
getSymbolType
@CheckForNullpublic [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](symbols/PresentationElement.html)> getSymbolType()
Type of the symbol to which to convert.
Returns:
type of the symbol to which to convert.
getHumanName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Gets human-readable format of the conversion.
Returns:
human-readable format of the conversion.
compareTo
public int compareTo(@Nonnull
 [ConvertElementInfo](ConvertElementInfo.html) o)
Specified by:
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))` in interface `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[ConvertElementInfo](ConvertElementInfo.html)>`
isCreateSymbol
public boolean isCreateSymbol()
Gets create symbol flag value.
Returns:
create symbol flag value.
setCreateSymbol
public void setCreateSymbol(boolean createSymbol)
Sets create symbol flag value.
Parameters:
`createSymbol` - create symbol flag value.
canInfoBeLost
public boolean canInfoBeLost([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source)
Indicates if info can be lost for a given source element.
Parameters:
`source` - element being converted.
Returns:
true if info can be lost, false otherwise.
setCanInfoBeLost
public void setCanInfoBeLost(boolean canInfoBeLost)
Sets info can be lost flag value.
Parameters:
`canInfoBeLost` - info can be lost flag value.
canConvert
public boolean canConvert([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Indicates if element can be converted.
Parameters:
`element` - element to convert.
Returns:
true if element can be converted, false otherwise.
isConvertingSourceEditable
public boolean isConvertingSourceEditable([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source)
Indicates if source element is editable
Parameters:
`source` - source to convert
Returns:
true if element is editable and can be converted, false otherwise.
isConvertOnlyIncomingReferences
public boolean isConvertOnlyIncomingReferences()
Gets convert only incoming references flag value.
Returns:
convert only incoming references flag value.
setConvertOnlyIncomingReferences
public void setConvertOnlyIncomingReferences(boolean convertOnlyIncomingReferences)
Sets convert only incoming references flag value.
Parameters:
`convertOnlyIncomingReferences` - convert only incoming references flag value.
isDisposeSource
public boolean isDisposeSource()
Indicates if source should be disposed after conversion.
Returns:
true if source should be disposed, false otherwise.
isCanChangeElementName
public boolean isCanChangeElementName()
Gets can change element name flag value.
Returns:
can change element name flag value.
setCanChangeElementName
public void setCanChangeElementName(boolean canChangeElementName)
Sets can change element name flag value.
Parameters:
`canChangeElementName` - can change element name flag value.
canChangeElement
public boolean canChangeElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Indicates if element can be changed by conversion.
Parameters:
`element` - element being converted.
Returns:
true if element can be changed by conversion.
isPreserveElementID
public boolean isPreserveElementID()
Gets preserve element ID flag value.
Returns:
preserve element ID flag value
setPreserveElementID
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setPreserveElementID(boolean preserveElementID)
Deprecated.
it is not recommended to use this setting as preserving ids can break model consistency if some situations
Sets preserve element ID flag value.
Parameters:
`preserveElementID` - preserve element ID flag value
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
getCategory
public [ConvertElementInfoCategory](ConvertElementInfoCategory.html) getCategory()
Returns:
category of info used for grouping
setCategory
public void setCategory([ConvertElementInfoCategory](ConvertElementInfoCategory.html) category)
Set category of info used for grouping of targets in UI.
Parameters:
`category` - category
getElementIDSuffix
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementIDSuffix()
Gets element ID suffix.
Returns:
element ID suffix.
setElementIDSuffix
public void setElementIDSuffix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementIDSuffix)
Sets element ID suffix.
Parameters:
`elementIDSuffix` - suffix to set.
isRemoveFromCollections
public boolean isRemoveFromCollections()
If the method returns true then convert should remove a value from the source element collection.
 Default implementation does not remove the collections.
Returns:
false.
setAdditionalStereotypes
public void setAdditionalStereotypes(@Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Set stereotypes to apply to converted element after conversion
Parameters:
`stereotypes` - stereotypes
getAdditionalStereotypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> getAdditionalStereotypes()
Returns:
some stereotypes to apply to converted element after conversion
getDisposeSourceValidator
public [ConvertElementInfo.DisposeSourceValidator](ConvertElementInfo.DisposeSourceValidator.html) getDisposeSourceValidator()
Gets dispose source validator.
Returns:
dispose source validator.
setDisposeSourceValidator
public void setDisposeSourceValidator([ConvertElementInfo.DisposeSourceValidator](ConvertElementInfo.DisposeSourceValidator.html) disposeSourceValidator)
Sets dispose source validator.
Parameters:
`disposeSourceValidator` - dispose source validator to set.
isConvertRelatedElements
public boolean isConvertRelatedElements()
Returns:
true if related elements should be converted also. Default is true
setConvertRelatedElements
public void setConvertRelatedElements(boolean convertRelatedElements)
Set flag for related elements converting
Parameters:
`convertRelatedElements` - convert related elements
getPendingMapping
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject> getPendingMapping()
Returns:
mapping for other elements that will be converted later
setPendingMapping
public void setPendingMapping([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject> pendingMapping)
Sets mapping for elements which will be converted later
Parameters:
`pendingMapping` - mapping of elements will be done later
isReplaceSourcePresentationElement
public boolean isReplaceSourcePresentationElement([PresentationElement](symbols/PresentationElement.html) sourcePresentationElement)
Check if source presentation element may be replaced.
 Default implementation checks is symbol is readonly
Parameters:
`sourcePresentationElement` - presentation element to check
Returns:
true if presentation element may be replaced

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class ConvertElementInfo">Class ConvertElementInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.ConvertElementInfo</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ConvertElementInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a>&gt;</span></div>
<div class="block">Holds information which controls the process of element conversion,
 for example allows to define target element type and preferred symbol type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Refactoring.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring</code></a></li>
<li><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></li>
<li><a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a></li>
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
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ConvertElementInfo.DisposeSourceValidator.html" title="interface in com.nomagic.magicdraw.uml">ConvertElementInfo.DisposeSourceValidator</a></code></div>
<div class="col-last even-row-color">
<div class="block">Validates whether source should be disposed after conversion.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class)">ConvertElementInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs this info.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,boolean)">ConvertElementInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 boolean canInfoBeLost)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs this info.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.Class)">ConvertElementInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; symbolType)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs this info.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Class,boolean)">ConvertElementInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 boolean createSymbol)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs this info.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Class,java.lang.Class)">ConvertElementInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; symbolType)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs this info.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canChangeElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if element can be changed by conversion.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canConvert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canConvert</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if element can be converted.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canInfoBeLost(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canInfoBeLost</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if info can be lost for a given source element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareTo(com.nomagic.magicdraw.uml.ConvertElementInfo)">compareTo</a><wbr/>(<a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalStereotypes()">getAdditionalStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ConvertElementInfoCategory.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfoCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategory()">getCategory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ConvertElementInfo.DisposeSourceValidator.html" title="interface in com.nomagic.magicdraw.uml">ConvertElementInfo.DisposeSourceValidator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisposeSourceValidator()">getDisposeSourceValidator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets dispose source validator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementIDSuffix()">getElementIDSuffix</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets element ID suffix.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementType()">getElementType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets type of the element to which to convert.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanName()">getHumanName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets human-readable format of the conversion.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets name of conversion.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPendingMapping()">getPendingMapping</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolType()">getSymbolType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Type of the symbol to which to convert.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCanChangeElementName()">isCanChangeElementName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets can change element name flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConvertingSourceEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isConvertingSourceEditable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if source element is editable</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConvertOnlyIncomingReferences()">isConvertOnlyIncomingReferences</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets convert only incoming references flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConvertRelatedElements()">isConvertRelatedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateSymbol()">isCreateSymbol</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets create symbol flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisposeSource()">isDisposeSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if source should be disposed after conversion.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPreserveElementID()">isPreserveElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets preserve element ID flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemoveFromCollections()">isRemoveFromCollections</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If the method returns true then convert should remove a value from the source element collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReplaceSourcePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isReplaceSourcePresentationElement</a><wbr/>(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourcePresentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if source presentation element may be replaced.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAdditionalStereotypes(java.util.Collection)">setAdditionalStereotypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set stereotypes to apply to converted element after conversion</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanChangeElementName(boolean)">setCanChangeElementName</a><wbr/>(boolean canChangeElementName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets can change element name flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanInfoBeLost(boolean)">setCanInfoBeLost</a><wbr/>(boolean canInfoBeLost)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets info can be lost flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCategory(com.nomagic.magicdraw.uml.ConvertElementInfoCategory)">setCategory</a><wbr/>(<a href="ConvertElementInfoCategory.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfoCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set category of info used for grouping of targets in UI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConvertOnlyIncomingReferences(boolean)">setConvertOnlyIncomingReferences</a><wbr/>(boolean convertOnlyIncomingReferences)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets convert only incoming references flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConvertRelatedElements(boolean)">setConvertRelatedElements</a><wbr/>(boolean convertRelatedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set flag for related elements converting</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateSymbol(boolean)">setCreateSymbol</a><wbr/>(boolean createSymbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets create symbol flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisposeSourceValidator(com.nomagic.magicdraw.uml.ConvertElementInfo.DisposeSourceValidator)">setDisposeSourceValidator</a><wbr/>(<a href="ConvertElementInfo.DisposeSourceValidator.html" title="interface in com.nomagic.magicdraw.uml">ConvertElementInfo.DisposeSourceValidator</a> disposeSourceValidator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets dispose source validator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementIDSuffix(java.lang.String)">setElementIDSuffix</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementIDSuffix)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element ID suffix.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPendingMapping(java.util.Map)">setPendingMapping</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt; pendingMapping)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets mapping for elements which will be converted later</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPreserveElementID(boolean)">setPreserveElementID</a><wbr/>(boolean preserveElementID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">it is not recommended to use this setting as preserving ids can break model consistency if some situations</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Class,java.lang.Class)">
<h3>ConvertElementInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConvertElementInfo</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; symbolType)</span></div>
<div class="block">Constructs this info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of conversion.</dd>
<dd><code>elementType</code> - type to which to convert.</dd>
<dd><code>symbolType</code> - preferred symbol type to which to convert.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.Class)">
<h3>ConvertElementInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConvertElementInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; symbolType)</span></div>
<div class="block">Constructs this info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementType</code> - type to which to convert.</dd>
<dd><code>symbolType</code> - preferred symbol type to which to convert.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Class,boolean)">
<h3>ConvertElementInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConvertElementInfo</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 boolean createSymbol)</span></div>
<div class="block">Constructs this info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of conversion.</dd>
<dd><code>elementType</code> - type to which to convert.</dd>
<dd><code>createSymbol</code> - indicates if symbol should be created with this conversion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class)">
<h3>ConvertElementInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConvertElementInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType)</span></div>
<div class="block">Constructs this info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementType</code> - type to which to convert.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,boolean)">
<h3>ConvertElementInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConvertElementInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementType,
 boolean canInfoBeLost)</span></div>
<div class="block">Constructs this info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementType</code> - type to which to convert.</dd>
<dd><code>canInfoBeLost</code> - indicates if info can be lost by conversion.</dd>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Gets name of conversion.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of conversion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementType()">
<h3>getElementType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElementType</span>()</div>
<div class="block">Gets type of the element to which to convert.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of the element to which to convert.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolType()">
<h3>getSymbolType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSymbolType</span>()</div>
<div class="block">Type of the symbol to which to convert.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of the symbol to which to convert.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanName()">
<h3>getHumanName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span>()</div>
<div class="block">Gets human-readable format of the conversion.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human-readable format of the conversion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareTo(com.nomagic.magicdraw.uml.ConvertElementInfo)">
<h3>compareTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr/><span class="parameters">(@Nonnull
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> o)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateSymbol()">
<h3>isCreateSymbol</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateSymbol</span>()</div>
<div class="block">Gets create symbol flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>create symbol flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateSymbol(boolean)">
<h3>setCreateSymbol</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateSymbol</span><wbr/><span class="parameters">(boolean createSymbol)</span></div>
<div class="block">Sets create symbol flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createSymbol</code> - create symbol flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canInfoBeLost(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canInfoBeLost</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canInfoBeLost</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source)</span></div>
<div class="block">Indicates if info can be lost for a given source element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - element being converted.</dd>
<dt>Returns:</dt>
<dd>true if info can be lost, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCanInfoBeLost(boolean)">
<h3>setCanInfoBeLost</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanInfoBeLost</span><wbr/><span class="parameters">(boolean canInfoBeLost)</span></div>
<div class="block">Sets info can be lost flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canInfoBeLost</code> - info can be lost flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canConvert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canConvert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canConvert</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Indicates if element can be converted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to convert.</dd>
<dt>Returns:</dt>
<dd>true if element can be converted, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConvertingSourceEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isConvertingSourceEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isConvertingSourceEditable</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source)</span></div>
<div class="block">Indicates if source element is editable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source to convert</dd>
<dt>Returns:</dt>
<dd>true if element is editable and can be converted, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConvertOnlyIncomingReferences()">
<h3>isConvertOnlyIncomingReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isConvertOnlyIncomingReferences</span>()</div>
<div class="block">Gets convert only incoming references flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>convert only incoming references flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConvertOnlyIncomingReferences(boolean)">
<h3>setConvertOnlyIncomingReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConvertOnlyIncomingReferences</span><wbr/><span class="parameters">(boolean convertOnlyIncomingReferences)</span></div>
<div class="block">Sets convert only incoming references flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>convertOnlyIncomingReferences</code> - convert only incoming references flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisposeSource()">
<h3>isDisposeSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisposeSource</span>()</div>
<div class="block">Indicates if source should be disposed after conversion.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if source should be disposed, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCanChangeElementName()">
<h3>isCanChangeElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCanChangeElementName</span>()</div>
<div class="block">Gets can change element name flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>can change element name flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCanChangeElementName(boolean)">
<h3>setCanChangeElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanChangeElementName</span><wbr/><span class="parameters">(boolean canChangeElementName)</span></div>
<div class="block">Sets can change element name flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canChangeElementName</code> - can change element name flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canChangeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Indicates if element can be changed by conversion.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element being converted.</dd>
<dt>Returns:</dt>
<dd>true if element can be changed by conversion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPreserveElementID()">
<h3>isPreserveElementID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPreserveElementID</span>()</div>
<div class="block">Gets preserve element ID flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>preserve element ID flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreserveElementID(boolean)">
<h3>setPreserveElementID</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreserveElementID</span><wbr/><span class="parameters">(boolean preserveElementID)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">it is not recommended to use this setting as preserving ids can break model consistency if some situations</div>
</div>
<div class="block">Sets preserve element ID flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>preserveElementID</code> - preserve element ID flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategory()">
<h3>getCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ConvertElementInfoCategory.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfoCategory</a></span> <span class="element-name">getCategory</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>category of info used for grouping</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCategory(com.nomagic.magicdraw.uml.ConvertElementInfoCategory)">
<h3>setCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCategory</span><wbr/><span class="parameters">(<a href="ConvertElementInfoCategory.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfoCategory</a> category)</span></div>
<div class="block">Set category of info used for grouping of targets in UI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementIDSuffix()">
<h3>getElementIDSuffix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementIDSuffix</span>()</div>
<div class="block">Gets element ID suffix.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element ID suffix.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElementIDSuffix(java.lang.String)">
<h3>setElementIDSuffix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementIDSuffix</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementIDSuffix)</span></div>
<div class="block">Sets element ID suffix.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementIDSuffix</code> - suffix to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemoveFromCollections()">
<h3>isRemoveFromCollections</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemoveFromCollections</span>()</div>
<div class="block">If the method returns true then convert should remove a value from the source element collection.
 Default implementation does not remove the collections.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAdditionalStereotypes(java.util.Collection)">
<h3>setAdditionalStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAdditionalStereotypes</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Set stereotypes to apply to converted element after conversion</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalStereotypes()">
<h3>getAdditionalStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAdditionalStereotypes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>some stereotypes to apply to converted element after conversion</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDisposeSourceValidator()">
<h3>getDisposeSourceValidator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ConvertElementInfo.DisposeSourceValidator.html" title="interface in com.nomagic.magicdraw.uml">ConvertElementInfo.DisposeSourceValidator</a></span> <span class="element-name">getDisposeSourceValidator</span>()</div>
<div class="block">Gets dispose source validator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>dispose source validator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisposeSourceValidator(com.nomagic.magicdraw.uml.ConvertElementInfo.DisposeSourceValidator)">
<h3>setDisposeSourceValidator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisposeSourceValidator</span><wbr/><span class="parameters">(<a href="ConvertElementInfo.DisposeSourceValidator.html" title="interface in com.nomagic.magicdraw.uml">ConvertElementInfo.DisposeSourceValidator</a> disposeSourceValidator)</span></div>
<div class="block">Sets dispose source validator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>disposeSourceValidator</code> - dispose source validator to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConvertRelatedElements()">
<h3>isConvertRelatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isConvertRelatedElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if related elements should be converted also. Default is true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConvertRelatedElements(boolean)">
<h3>setConvertRelatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConvertRelatedElements</span><wbr/><span class="parameters">(boolean convertRelatedElements)</span></div>
<div class="block">Set flag for related elements converting</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>convertRelatedElements</code> - convert related elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPendingMapping()">
<h3>getPendingMapping</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getPendingMapping</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>mapping for other elements that will be converted later</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPendingMapping(java.util.Map)">
<h3>setPendingMapping</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPendingMapping</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt; pendingMapping)</span></div>
<div class="block">Sets mapping for elements which will be converted later</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pendingMapping</code> - mapping of elements will be done later</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReplaceSourcePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isReplaceSourcePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReplaceSourcePresentationElement</span><wbr/><span class="parameters">(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourcePresentationElement)</span></div>
<div class="block">Check if source presentation element may be replaced.
 Default implementation checks is symbol is readonly</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourcePresentationElement</code> - presentation element to check</dd>
<dt>Returns:</dt>
<dd>true if presentation element may be replaced</dd>
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
