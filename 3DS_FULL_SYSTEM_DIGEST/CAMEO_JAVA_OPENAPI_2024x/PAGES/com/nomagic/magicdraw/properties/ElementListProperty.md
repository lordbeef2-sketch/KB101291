# JAVA OPENAPI: ElementListProperty (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/properties/ElementListProperty.html
- source_path: `com/nomagic/magicdraw/properties/ElementListProperty.html`
- source_sha256: `d6762566dd071c2eb966821d71d8110505f251da145cdaf209bd293d6ff86f45`
- captured_utc: `2026-07-14T16:51:26.471272+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class ElementListProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
[com.nomagic.magicdraw.properties.ListProperty](ListProperty.html)
com.nomagic.magicdraw.properties.ElementListProperty

All Implemented Interfaces:
`com.nomagic.magicdraw.properties.ElementFilterProperty`, `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classElementListProperty
extends [ListProperty](ListProperty.html)
implements com.nomagic.magicdraw.properties.ElementFilterProperty

Property for selecting a list of Elements of given type. Editor of this property allows to choose some
 specific Elements from all existing elements in the current project

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementListProperty](#%3Cinit%3E())()`
Creates and initializes a new `ModelElementListProperty` object.
`[ElementListProperty](#%3Cinit%3E(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Creates and initializes a new `ModelElementListProperty` object
 from specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the given visitor.
`[ElementListProperty](ElementListProperty.html)`
`[clone](#clone())()`
Clones the property.
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns a class type of the property.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getDisplayableTypes](#getDisplayableTypes())()`
Returns displayable elements class types.
`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[]`
`[getElements](#getElements())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[getElementsIDs](#getElementsIDs())()`
ID's of stored Elements.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[]`
`[getOriginalValue](#getOriginalValue())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getSelectableRestrictedElements](#getSelectableRestrictedElements())()`
Returns a stereotypes and metaclasses for filtering selectable elements
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getSelectableTypes](#getSelectableTypes())()`
Returns selectable elements class types.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSortableValueStringRepresentation](#getSortableValueStringRepresentation())()`

`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Deprecated.
This is a deprecated methods and you must use collection of restricted elements, not single stereotype
`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[]`
`[getValue](#getValue())()`
Returns an array of model elements.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueStringRepresentation](#getValueStringRepresentation())()`
Returns value's string representation.
`boolean`
`[isContainment](#isContainment())()`
Check Element list property is Containment.
`boolean`
`[isLoadedUserData](#isLoadedUserData())()`

`boolean`
`[isOrdered](#isOrdered())()`
Check Element list property is Ordered.
`void`
`[setContainment](#setContainment(boolean))(boolean containment)`

`void`
`[setDisplayableTypes](#setDisplayableTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes)`

`void`
`[setLoadedUserData](#setLoadedUserData(boolean))(boolean loadedUserData)`

`void`
`[setOrdered](#setOrdered(boolean))(boolean ordered)`

`void`
`[setProject](#setProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Set project (scope for property)
`void`
`[setPropertyData](#setPropertyData(java.util.Collection,java.util.Collection,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes,
 boolean ordered,
 boolean containment)`
Sets data for property members.
`void`
`[setSelectableRestrictedElements](#setSelectableRestrictedElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) stereotypes)`
Sets a stereotypes and metaclasses for filtering selectable elements
`void`
`[setSelectableTypes](#setSelectableTypes(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes)`

`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets a value of the property.
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [createCellEditor](Property.html#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)), [createTableCellRenderer](Property.html#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)), [equals](Property.html#equals(java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [isValueCompatible](Property.html#isValueCompatible(java.lang.Object)), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean)), [toString](Property.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementListProperty
public ElementListProperty()
Creates and initializes a new `ModelElementListProperty` object.
ElementListProperty
public ElementListProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Creates and initializes a new `ModelElementListProperty` object
 from specified parameters.
Parameters:
`id` - - id of the property.
`value` - - a value of the property.
 ============ METHOD DETAIL ========== 
Method Details
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns a class type of the property.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](ListProperty.html#getClassType())` in class `[ListProperty](ListProperty.html)`
Returns:
PropertyID.ELEMENT_LIST_PROPERTY
See Also:
[`PropertyID.ELEMENT_LIST_PROPERTY`](PropertyID.html#ELEMENT_LIST_PROPERTY)
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
isContainment
public boolean isContainment()
Check Element list property is Containment.
Specified by:
`isContainment` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
boolean.
isOrdered
public boolean isOrdered()
Check Element list property is Ordered.
Specified by:
`isOrdered` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
boolean.
setValue
public void setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Description copied from class: `[ListProperty](ListProperty.html#setValue(java.lang.Object))`
Sets a value of the property.
Overrides:
`[setValue](ListProperty.html#setValue(java.lang.Object))` in class `[ListProperty](ListProperty.html)`
Parameters:
`value` - a value.
getElements
public [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] getElements()
getOriginalValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] getOriginalValue()
firePropertyChange
public void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Description copied from class: `[Property](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new are equal and non-null.
Overrides:
`[firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in class `[Property](Property.html)`
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
getElementsIDs
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] getElementsIDs()
ID's of stored Elements. Real value of project.
Returns:
id's of elements
getValue
public [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)[] getValue()
Returns an array of model elements.
Overrides:
`[getValue](ListProperty.html#getValue())` in class `[ListProperty](ListProperty.html)`
Returns:
an array of ModelElement.
clone
public [ElementListProperty](ElementListProperty.html) clone()
Clones the property.
Overrides:
`[clone](ListProperty.html#clone())` in class `[ListProperty](ListProperty.html)`
Returns:
the clone of this property.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](ListProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[ListProperty](ListProperty.html)`
Parameters:
`v` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueStringRepresentation()
Description copied from class: `[Property](Property.html#getValueStringRepresentation())`
Returns value's string representation.
Overrides:
`[getValueStringRepresentation](ListProperty.html#getValueStringRepresentation())` in class `[ListProperty](ListProperty.html)`
Returns:
string "null" if property does not have value; `value.
 toString()` if property has value.
getSortableValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSortableValueStringRepresentation()
Overrides:
`[getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation())` in class `[Property](Property.html)`
setProject
public void setProject(@CheckForNull
 [Project](../core/Project.html) project)
Description copied from interface: `com.nomagic.magicdraw.properties.ElementFilterProperty`
Set project (scope for property)
Specified by:
`setProject` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`project` - project.
getSelectableRestrictedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getSelectableRestrictedElements()
Description copied from interface: `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns a stereotypes and metaclasses for filtering selectable elements
Specified by:
`getSelectableRestrictedElements` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Returns:
stereotypes and metaclasses for filtering selectable elements
setSelectableRestrictedElements
public void setSelectableRestrictedElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) stereotypes)
Sets a stereotypes and metaclasses for filtering selectable elements
Specified by:
`setSelectableRestrictedElements` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
Parameters:
`stereotypes` - stereotypes
getStereotype
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Deprecated.
This is a deprecated methods and you must use collection of restricted elements, not single stereotype
Returns a first stereotype from selectable restricted elements.
Returns:
first stereotype
See Also:
[`getSelectableRestrictedElements()`](#getSelectableRestrictedElements())
setSelectableTypes
public void setSelectableTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectableTypes)
Specified by:
`setSelectableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
setDisplayableTypes
public void setDisplayableTypes(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayableTypes)
Specified by:
`setDisplayableTypes` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
setContainment
public void setContainment(boolean containment)
Specified by:
`setContainment` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
setOrdered
public void setOrdered(boolean ordered)
Specified by:
`setOrdered` in interface `com.nomagic.magicdraw.properties.ElementFilterProperty`
setLoadedUserData
public void setLoadedUserData(boolean loadedUserData)
isLoadedUserData
public boolean isLoadedUserData()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class ElementListProperty">Class ElementListProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance"><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.ListProperty</a>
<div class="inheritance">com.nomagic.magicdraw.properties.ElementListProperty</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.properties.ElementFilterProperty</code>, <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementListProperty</span>
<span class="extends-implements">extends <a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a>
implements com.nomagic.magicdraw.properties.ElementFilterProperty</span></div>
<div class="block">Property for selecting a list of Elements of given type. Editor of this property allows to choose some
 specific Elements from all existing elements in the current project</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementListProperty</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>ModelElementListProperty</code> object.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object)">ElementListProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>ModelElementListProperty</code> object
 from specified parameters.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a class type of the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDisplayableTypes()">getDisplayableTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns displayable elements class types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElements()">getElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsIDs()">getElementsIDs</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">ID's of stored Elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalValue()">getOriginalValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectableRestrictedElements()">getSelectableRestrictedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a stereotypes and metaclasses for filtering selectable elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectableTypes()">getSelectableTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns selectable elements class types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">This is a deprecated methods and you must use collection of restricted elements, not single stereotype</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an array of model elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueStringRepresentation()">getValueStringRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value's string representation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isContainment()">isContainment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Element list property is Containment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoadedUserData()">isLoadedUserData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Element list property is Ordered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContainment(boolean)">setContainment</a><wbr/>(boolean containment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayableTypes(java.util.Collection)">setDisplayableTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadedUserData(boolean)">setLoadedUserData</a><wbr/>(boolean loadedUserData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrdered(boolean)">setOrdered</a><wbr/>(boolean ordered)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProject(com.nomagic.magicdraw.core.Project)">setProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project (scope for property)</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectableRestrictedElements(java.util.Collection)">setSelectableRestrictedElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a stereotypes and metaclasses for filtering selectable elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectableTypes(java.util.Collection)">setSelectableTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectableTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a value of the property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createCellEditor</a>, <a href="Property.html#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createTableCellRenderer</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a>, <a href="Property.html#toString()">toString</a></code></div>
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
<h3>ElementListProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementListProperty</span>()</div>
<div class="block">Creates and initializes a new <code>ModelElementListProperty</code> object.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object)">
<h3>ElementListProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementListProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Creates and initializes a new <code>ModelElementListProperty</code> object
 from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - - id of the property.</dd>
<dd><code>value</code> - - a value of the property.</dd>
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
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns a class type of the property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ListProperty.html#getClassType()">getClassType</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.ELEMENT_LIST_PROPERTY</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="PropertyID.html#ELEMENT_LIST_PROPERTY"><code>PropertyID.ELEMENT_LIST_PROPERTY</code></a></li>
</ul>
</dd>
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
<section class="detail" id="isContainment()">
<h3>isContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isContainment</span>()</div>
<div class="block">Check Element list property is Containment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isContainment</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<div class="block">Check Element list property is Ordered.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isOrdered</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ListProperty.html#setValue(java.lang.Object)">ListProperty</a></code></span></div>
<div class="block">Sets a value of the property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ListProperty.html#setValue(java.lang.Object)">setValue</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - a value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElements()">
<h3>getElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[]</span> <span class="element-name">getElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOriginalValue()">
<h3>getOriginalValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[]</span> <span class="element-name">getOriginalValue</span>()</div>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">Property</a></code></span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new are equal and non-null.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsIDs()">
<h3>getElementsIDs</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getElementsIDs</span>()</div>
<div class="block">ID's of stored Elements. Real value of project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id's of elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>[]</span> <span class="element-name">getValue</span>()</div>
<div class="block">Returns an array of model elements.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ListProperty.html#getValue()">getValue</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
<dt>Returns:</dt>
<dd>an array of ModelElement.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ListProperty.html#clone()">clone</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
<dt>Returns:</dt>
<dd>the clone of this property.</dd>
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
<dd><code><a href="ListProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
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
<dd><code><a href="ListProperty.html#getValueStringRepresentation()">getValueStringRepresentation</a></code> in class <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code></dd>
<dt>Returns:</dt>
<dd>string "null" if property does not have value; <code>value.
 toString()</code> if property has value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortableValueStringRepresentation()">
<h3>getSortableValueStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSortableValueStringRepresentation</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProject(com.nomagic.magicdraw.core.Project)">
<h3>setProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></span></div>
<div class="block">Set project (scope for property)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setProject</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectableRestrictedElements()">
<h3>getSelectableRestrictedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getSelectableRestrictedElements</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></span></div>
<div class="block">Returns a stereotypes and metaclasses for filtering selectable elements</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSelectableRestrictedElements</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Returns:</dt>
<dd>stereotypes and metaclasses for filtering selectable elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectableRestrictedElements(java.util.Collection)">
<h3>setSelectableRestrictedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectableRestrictedElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> stereotypes)</span></div>
<div class="block">Sets a stereotypes and metaclasses for filtering selectable elements</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSelectableRestrictedElements</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - stereotypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">This is a deprecated methods and you must use collection of restricted elements, not single stereotype</div>
</div>
<div class="block">Returns a first stereotype from selectable restricted elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first stereotype</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSelectableRestrictedElements()"><code>getSelectableRestrictedElements()</code></a></li>
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
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSelectableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayableTypes(java.util.Collection)">
<h3>setDisplayableTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayableTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayableTypes)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setDisplayableTypes</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContainment(boolean)">
<h3>setContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContainment</span><wbr/><span class="parameters">(boolean containment)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setContainment</code> in interface <code>com.nomagic.magicdraw.properties.ElementFilterProperty</code></dd>
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
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoadedUserData(boolean)">
<h3>setLoadedUserData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoadedUserData</span><wbr/><span class="parameters">(boolean loadedUserData)</span></div>
</section>
</li>
<li>
<section class="detail" id="isLoadedUserData()">
<h3>isLoadedUserData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoadedUserData</span>()</div>
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
