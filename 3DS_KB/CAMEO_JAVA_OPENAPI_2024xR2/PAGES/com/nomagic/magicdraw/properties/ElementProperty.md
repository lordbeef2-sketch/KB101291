# JAVA OPENAPI: ElementProperty (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/properties/ElementProperty.html
- source_path: `com/nomagic/magicdraw/properties/ElementProperty.html`
- source_sha256: `9d213f0cdc80abc58ca39b5db68b2fb2995f75190c8e74ba8dc13a095e2f24d6`
- captured_utc: `2026-07-14T16:55:25.341119+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class ElementProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
com.nomagic.magicdraw.properties.ElementProperty

All Implemented Interfaces:
`com.nomagic.magicdraw.properties.ElementFilterProperty`, `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classElementProperty
extends [Property](Property.html)
implements com.nomagic.magicdraw.properties.ElementFilterProperty

Property for selecting Element of given type. Editor of this property allows to choose some
 specific Element from all existing elements in the current project.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementProperty](#%3Cinit%3E())()`
Default constructor.
`[ElementProperty](#%3Cinit%3E(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
The property constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the given visitor.
`[ElementProperty](ElementProperty.html)`
`[clone](#clone())()`
Clones the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getDisplayableTypes](#getDisplayableTypes())()`
Returns displayable elements class types.
`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Returns model element
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementID](#getElementID())()`
Returns stored element ID (real value of Property).
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getOriginalValue](#getOriginalValue())()`
Does not convert persistent value to element, but returns at it is (id of element)
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getSelectableRestrictedElements](#getSelectableRestrictedElements())()`
Returns a stereotypes and metaclasses for filtering selectable elements
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getSelectableTypes](#getSelectableTypes())()`
Returns selectable elements class types.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringRepresentation](#getStringRepresentation(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`
Returns properties value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueStringRepresentation](#getValueStringRepresentation())()`
Returns value's string representation.
`boolean`
`[isContainment](#isContainment())()`
Tests Is containment.
`boolean`
`[isOrdered](#isOrdered())()`
Check Element list property is Ordered.
`boolean`
`[isParentApplicant](#isParentApplicant())()`
Checks if selected element intends to be the parent for other element
`boolean`
`[isTypeElement](#isTypeElement())()`
Test is Type Element.
`boolean`
`[isUseUnspecified](#isUseUnspecified())()`
Returns 'use unspecified' flag for this property.
`void`
`[setContainment](#setContainment(boolean))(boolean containment)`
Set containment.
`void`
`[setDisplayableTypes](#setDisplayableTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes)`
Set Displayable types.
`void`
`[setOrdered](#setOrdered(boolean))(boolean ordered)`

`void`
`[setParentApplicant](#setParentApplicant(boolean))(boolean parentApplicant)`
Set parent applicant.
`void`
`[setProject](#setProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Set project.
`void`
`[setPropertyData](#setPropertyData(java.util.Collection,java.util.Collection,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes,
 boolean ordered,
 boolean containment)`
Sets data for property members.
`void`
`[setSelectableRestrictedElements](#setSelectableRestrictedElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements)`
Sets a stereotypes and metaclasses for filtering selectable elements
`void`
`[setSelectableTypes](#setSelectableTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes)`
Set Select table types.
`void`
`[setTypeElement](#setTypeElement(boolean))(boolean typeElement)`
Set type Element.
`void`
`[setUseUnspecified](#setUseUnspecified(boolean))(boolean useUnspecified)`
Set Use Unspecified.
`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets new property value.
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [equals](Property.html#equals(java.lang.Object)), [firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [isValueCompatible](Property.html#isValueCompatible(java.lang.Object)), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean)), [toString](Property.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementProperty
public ElementProperty()
Default constructor. Value of the property will be null.
 ID will be empty string. Property is editable.
ElementProperty
public ElementProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
The property constructor.
Parameters:
`id` - the ID of property.
`element` - some type - model Element or String.
 ============ METHOD DETAIL ========== 
Method Details
clone
public [ElementProperty](ElementProperty.html) clone()
Clones the property.
Overrides:
`[clone](Property.html#clone())` in class `[Property](Property.html)`
Returns:
the clone of this property.
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](Property.html#getClassType())` in class `[Property](Property.html)`
Returns:
PropertyID.ELEMENT_PROPERTY
See Also:
[`PropertyID.ELEMENT_PROPERTY`](PropertyID.html#ELEMENT_PROPERTY)
setSelectableTypes
public void setSelectableTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes)
Set Select table types.
Specified by:
`setSelectableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`selectableTypes` - List of select table types.
setDisplayableTypes
public void setDisplayableTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes)
Set Displayable types.
Specified by:
`setDisplayableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`displayableTypes` - List of Displayable type.
setUseUnspecified
public void setUseUnspecified(boolean useUnspecified)
Set Use Unspecified.
Parameters:
`useUnspecified` - Use Unspecified flag.
setParentApplicant
public void setParentApplicant(boolean parentApplicant)
Set parent applicant.
Parameters:
`parentApplicant` - Parent applicant.
setContainment
public void setContainment(boolean containment)
Set containment.
Specified by:
`setContainment` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`containment` - Containment value.
setTypeElement
public void setTypeElement(boolean typeElement)
Set type Element.
Parameters:
`typeElement` - The given type element.
getSelectableTypes
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getSelectableTypes()
Returns selectable elements class types.
Specified by:
`getSelectableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
selectable types.
getDisplayableTypes
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getDisplayableTypes()
Returns displayable elements class types.
Specified by:
`getDisplayableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
displayable types.
isUseUnspecified
public boolean isUseUnspecified()
Returns 'use unspecified' flag for this property.
Returns:
'use unspecified' flag for this property.
isParentApplicant
public boolean isParentApplicant()
Checks if selected element intends to be the parent for other element
Returns:
true - if selected element intends to be the parent of the other element; otherwise - false.
setValue
public void setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets new property value.
 Will fire a `PropertyChangeEvent` with propertyName - property
 ID, newValue and oldValue.
Overrides:
`[setValue](Property.html#setValue(java.lang.Object))` in class `[Property](Property.html)`
Parameters:
`value` - model element or ID.
getOriginalValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getOriginalValue()
Does not convert persistent value to element, but returns at it is (id of element)
getElementID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementID()
Returns stored element ID (real value of Property).
Returns:
value of the property.
getValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
Returns properties value.
Overrides:
`[getValue](Property.html#getValue())` in class `[Property](Property.html)`
Returns:
value of the property.
getElement
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Returns model element
Returns:
Model Element.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[Property](Property.html)`
Parameters:
`v` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueStringRepresentation()
Description copied from class: `[Property](Property.html#getValueStringRepresentation())`
Returns value's string representation.
Overrides:
`[getValueStringRepresentation](Property.html#getValueStringRepresentation())` in class `[Property](Property.html)`
Returns:
string "null" if property does not have value; `value.
 toString()` if property has value.
getStringRepresentation
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringRepresentation(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
setProject
public void setProject(@CheckForNull
 [Project](../core/Project.html) project)
Set project.
Specified by:
`setProject` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`project` - Given project.
isContainment
public boolean isContainment()
Tests Is containment.
Specified by:
`isContainment` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
boolean
isTypeElement
public boolean isTypeElement()
Test is Type Element.
getSelectableRestrictedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getSelectableRestrictedElements()
Returns a stereotypes and metaclasses for filtering selectable elements
Specified by:
`getSelectableRestrictedElements` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
setSelectableRestrictedElements
public void setSelectableRestrictedElements(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements)
Sets a stereotypes and metaclasses for filtering selectable elements
Specified by:
`setSelectableRestrictedElements` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`elements` - elements
setPropertyData
public void setPropertyData(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes,
 boolean ordered,
 boolean containment)
Sets data for property members. This method takes collections of class types. You must add into these
 collections class types from constants class ClassTypes.
Specified by:
`setPropertyData` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
isOrdered
public boolean isOrdered()
Description copied from interface: `com.nomagic.magicdraw.properties.ElementFilterProperty`
Check Element list property is Ordered.
Specified by:
`isOrdered` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
boolean.
See Also:
`ElementFilterProperty.isOrdered()`
setOrdered
public void setOrdered(boolean ordered)
Specified by:
`setOrdered` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
See Also:
`ElementFilterProperty.setOrdered(boolean)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class ElementProperty">Class ElementProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance">com.nomagic.magicdraw.properties.ElementProperty</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.properties.ElementFilterProperty</code>, <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementProperty</span>
<span class="extends-implements">extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>
implements com.nomagic.magicdraw.properties.ElementFilterProperty</span></div>
<div class="block">Property for selecting Element of given type. Editor of this property allows to choose some
 specific Element from all existing elements in the current project.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.properties.Property">Fields inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER">DEFAULT_PROPERTY_RESOURCE_PROVIDER</a>, <a href="Property.html#EDITABLE">EDITABLE</a>, <a href="Property.html#NULL">NULL</a>, <a href="Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER">NULL_ID_PROPERTY_RESOURCE_PROVIDER</a>, <a href="Property.html#TO">TO</a>, <a href="Property.html#UNDEFINED">UNDEFINED</a>, <a href="Property.html#VALUE">VALUE</a>, <a href="Property.html#VALUE_ANNOTATIONS">VALUE_ANNOTATIONS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementProperty</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object)">ElementProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color">
<div class="block">The property constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisplayableTypes()">getDisplayableTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns displayable elements class types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementID()">getElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stored element ID (real value of Property).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalValue()">getOriginalValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does not convert persistent value to element, but returns at it is (id of element)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectableRestrictedElements()">getSelectableRestrictedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a stereotypes and metaclasses for filtering selectable elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectableTypes()">getSelectableTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns selectable elements class types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringRepresentation(java.lang.Object)">getStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns properties value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueStringRepresentation()">getValueStringRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value's string representation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isContainment()">isContainment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests Is containment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Element list property is Ordered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentApplicant()">isParentApplicant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if selected element intends to be the parent for other element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeElement()">isTypeElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test is Type Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseUnspecified()">isUseUnspecified</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns 'use unspecified' flag for this property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContainment(boolean)">setContainment</a><wbr/>(boolean containment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set containment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayableTypes(java.util.Collection)">setDisplayableTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Displayable types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrdered(boolean)">setOrdered</a><wbr/>(boolean ordered)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentApplicant(boolean)">setParentApplicant</a><wbr/>(boolean parentApplicant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set parent applicant.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProject(com.nomagic.magicdraw.core.Project)">setProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyData(java.util.Collection,java.util.Collection,boolean,boolean)">setPropertyData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectableTypes,
 boolean ordered,
 boolean containment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets data for property members.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectableRestrictedElements(java.util.Collection)">setSelectableRestrictedElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a stereotypes and metaclasses for filtering selectable elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectableTypes(java.util.Collection)">setSelectableTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectableTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Select table types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTypeElement(boolean)">setTypeElement</a><wbr/>(boolean typeElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set type Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseUnspecified(boolean)">setUseUnspecified</a><wbr/>(boolean useUnspecified)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Use Unspecified.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new property value.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a>, <a href="Property.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ElementProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementProperty</span>()</div>
<div class="block">Default constructor. Value of the property will be null.
 ID will be empty string. Property is editable.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object)">
<h3>ElementProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">The property constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>element</code> - some type - model Element or String.</dd>
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
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#clone()">clone</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>the clone of this property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getClassType()">getClassType</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.ELEMENT_PROPERTY</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#ELEMENT_PROPERTY"><code>PropertyID.ELEMENT_PROPERTY</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectableTypes(java.util.Collection)">
<h3>setSelectableTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectableTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectableTypes)</span></div>
<div class="block">Set Select table types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSelectableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>selectableTypes</code> - List of select table types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayableTypes(java.util.Collection)">
<h3>setDisplayableTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayableTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes)</span></div>
<div class="block">Set Displayable types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setDisplayableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>displayableTypes</code> - List of Displayable type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseUnspecified(boolean)">
<h3>setUseUnspecified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseUnspecified</span><wbr/><span class="parameters">(boolean useUnspecified)</span></div>
<div class="block">Set Use Unspecified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useUnspecified</code> - Use Unspecified flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentApplicant(boolean)">
<h3>setParentApplicant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentApplicant</span><wbr/><span class="parameters">(boolean parentApplicant)</span></div>
<div class="block">Set parent applicant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentApplicant</code> - Parent applicant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContainment(boolean)">
<h3>setContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContainment</span><wbr/><span class="parameters">(boolean containment)</span></div>
<div class="block">Set containment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setContainment</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>containment</code> - Containment value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTypeElement(boolean)">
<h3>setTypeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTypeElement</span><wbr/><span class="parameters">(boolean typeElement)</span></div>
<div class="block">Set type Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>typeElement</code> - The given type element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectableTypes()">
<h3>getSelectableTypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getSelectableTypes</span>()</div>
<div class="block">Returns selectable elements class types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSelectableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>selectable types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDisplayableTypes()">
<h3>getDisplayableTypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getDisplayableTypes</span>()</div>
<div class="block">Returns displayable elements class types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getDisplayableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>displayable types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseUnspecified()">
<h3>isUseUnspecified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseUnspecified</span>()</div>
<div class="block">Returns 'use unspecified' flag for this property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>'use unspecified' flag for this property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentApplicant()">
<h3>isParentApplicant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParentApplicant</span>()</div>
<div class="block">Checks if selected element intends to be the parent for other element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true - if selected element intends to be the parent of the other element; otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets new property value.
 Will fire a <code>PropertyChangeEvent</code> with propertyName - property
 ID, newValue and oldValue.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#setValue(java.lang.Object)">setValue</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - model element or ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalValue()">
<h3>getOriginalValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getOriginalValue</span>()</div>
<div class="block">Does not convert persistent value to element, but returns at it is (id of element)</div>
</section>
</li>
<li>
<section class="detail" id="getElementID()">
<h3>getElementID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementID</span>()</div>
<div class="block">Returns stored element ID (real value of Property).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">Returns properties value.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getValue()">getValue</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns model element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Model Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueStringRepresentation()">
<h3>getValueStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueStringRepresentation</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#getValueStringRepresentation()">Property</a></code></span></div>
<div class="block">Returns value's string representation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getValueStringRepresentation()">getValueStringRepresentation</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>string "null" if property does not have value; <code>value.
 toString()</code> if property has value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringRepresentation(java.lang.Object)">
<h3>getStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringRepresentation</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setProject(com.nomagic.magicdraw.core.Project)">
<h3>setProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Set project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setProject</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - Given project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isContainment()">
<h3>isContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isContainment</span>()</div>
<div class="block">Tests Is containment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isContainment</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeElement()">
<h3>isTypeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeElement</span>()</div>
<div class="block">Test is Type Element.</div>
</section>
</li>
<li>
<section class="detail" id="getSelectableRestrictedElements()">
<h3>getSelectableRestrictedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getSelectableRestrictedElements</span>()</div>
<div class="block">Returns a stereotypes and metaclasses for filtering selectable elements</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSelectableRestrictedElements</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectableRestrictedElements(java.util.Collection)">
<h3>setSelectableRestrictedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectableRestrictedElements</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements)</span></div>
<div class="block">Sets a stereotypes and metaclasses for filtering selectable elements</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSelectableRestrictedElements</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyData(java.util.Collection,java.util.Collection,boolean,boolean)">
<h3>setPropertyData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyData</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectableTypes,
 boolean ordered,
 boolean containment)</span></div>
<div class="block">Sets data for property members. This method takes collections of class types. You must add into these
 collections class types from constants class ClassTypes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setPropertyData</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></span></div>
<div class="block">Check Element list property is Ordered.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isOrdered</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>boolean.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>ElementFilterProperty.isOrdered()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrdered(boolean)">
<h3>setOrdered</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrdered</span><wbr/><span class="parameters">(boolean ordered)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setOrdered</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>ElementFilterProperty.setOrdered(boolean)</code></li>
</ul>
</dd>
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
