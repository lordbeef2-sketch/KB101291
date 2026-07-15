# JAVA OPENAPI: ChoiceProperty (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/properties/ChoiceProperty.html
- source_path: `com/nomagic/magicdraw/properties/ChoiceProperty.html`
- source_sha256: `6f82a14bc5b53f25da69f6dd3f5a83bec86f054ce97b2c140f90fda83608906e`
- captured_utc: `2026-07-14T16:51:26.703275+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class ChoiceProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
[com.nomagic.magicdraw.properties.AbstractChoiceProperty](AbstractChoiceProperty.html)
com.nomagic.magicdraw.properties.ChoiceProperty

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[LocaleProperty](LocaleProperty.html)`

@OpenApiAllpublic classChoiceProperty
extends [AbstractChoiceProperty](AbstractChoiceProperty.html)

The property selecting some value from a list of possible values or entering a new String value.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ChoiceProperty](#%3Cinit%3E())()`
Default constructor.
`[ChoiceProperty](#%3Cinit%3E(java.lang.String,int,java.util.List))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int index,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice)`
The constructor.
`[ChoiceProperty](#%3Cinit%3E(java.lang.String,int,java.util.List,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int index,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice,
 int max)`
The constructor.
`[ChoiceProperty](#%3Cinit%3E(java.lang.String,java.lang.Object,java.util.List))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice)`
The constructor.
`[ChoiceProperty](#%3Cinit%3E(java.lang.String,java.lang.Object,java.util.List,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice,
 int max)`
The constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the `PropertyVisitor`.
`[ChoiceProperty](ChoiceProperty.html)`
`[clone](#clone())()`
Clones the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`int`
`[getIndex](#getIndex())()`
Returns the index of value in the choice list.
`boolean`
`[isAppendValue](#isAppendValue())()`
Return append value flag.
`void`
`[setAppendValue](#setAppendValue(boolean))(boolean appendValue)`
Sets the append value flag.
`void`
`[setChoice](#setChoice(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) val)`
Sets the list of possible values for selecting.
`void`
`[setIndex](#setIndex(int))(int val)`
Sets index of selected value.
`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets value of the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
The string representation of the property.
Methods inherited from class com.nomagic.magicdraw.properties.[AbstractChoiceProperty](AbstractChoiceProperty.html)
`[getChoice](AbstractChoiceProperty.html#getChoice()), [isEditableValue](AbstractChoiceProperty.html#isEditableValue()), [isUndefinedStateAvailable](AbstractChoiceProperty.html#isUndefinedStateAvailable()), [isValuesTranslatable](AbstractChoiceProperty.html#isValuesTranslatable()), [setEditableValue](AbstractChoiceProperty.html#setEditableValue(boolean)), [setUndefinedStateAvailable](AbstractChoiceProperty.html#setUndefinedStateAvailable(boolean)), [setValuesTranslatable](AbstractChoiceProperty.html#setValuesTranslatable(boolean))`
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [equals](Property.html#equals(java.lang.Object)), [firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [getValue](Property.html#getValue()), [getValueStringRepresentation](Property.html#getValueStringRepresentation()), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [isValueCompatible](Property.html#isValueCompatible(java.lang.Object)), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ChoiceProperty
public ChoiceProperty()
Default constructor. Value of the property will be null.
 ID will be empty string.
ChoiceProperty
public ChoiceProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice)
The constructor.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`choice` - the list of possible values.
ChoiceProperty
public ChoiceProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice,
 int max)
The constructor.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`choice` - the list of possible values.
`max` - the maximum size of possible values list.
ChoiceProperty
public ChoiceProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int index,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice,
 int max)
The constructor.
Parameters:
`id` - the ID of property.
`index` - the index in choice of selected value.
`choice` - the list of possible values.
`max` - the maximum size of possible values list.
ChoiceProperty
public ChoiceProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int index,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) choice)
The constructor.
Parameters:
`id` - the ID of property.
`index` - the index in choice of selected value.
`choice` - the list of possible values.
 ============ METHOD DETAIL ========== 
Method Details
isAppendValue
public boolean isAppendValue()
Return append value flag.
Returns:
the appendValue flag.
setAppendValue
public void setAppendValue(boolean appendValue)
Sets the append value flag.
 If property is editable, entered value is appended to the choice.
Parameters:
`appendValue` - the append state of the property.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the `PropertyVisitor`.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[Property](Property.html)`
Parameters:
`v` - the given visitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getIndex
public int getIndex()
Returns the index of value in the choice list.
Returns:
index of value in the choice list; if value is not in the choice
 list, return -1.
setChoice
public void setChoice([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) val)
Sets the list of possible values for selecting.
 Sets only mMaximum number of values from the List's beginning.
Overrides:
`[setChoice](AbstractChoiceProperty.html#setChoice(java.util.List))` in class `[AbstractChoiceProperty](AbstractChoiceProperty.html)`
Parameters:
`val` - a new possible values list.
setIndex
public void setIndex(int val)
Sets index of selected value.
 The index in possible values' list of new property value.
Parameters:
`val` - a new index.
setValue
public void setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets value of the property.
Overrides:
`[setValue](Property.html#setValue(java.lang.Object))` in class `[Property](Property.html)`
Parameters:
`value` - a new value.
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](Property.html#getClassType())` in class `[Property](Property.html)`
Returns:
PropertyID.CHOICE_PROPERTY.
See Also:
[`PropertyID.CHOICE_PROPERTY`](PropertyID.html#CHOICE_PROPERTY)
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
The string representation of the property. Used for debugging purposes only.
Overrides:
`[toString](Property.html#toString())` in class `[Property](Property.html)`
Returns:
the string representation.
clone
public [ChoiceProperty](ChoiceProperty.html) clone()
Description copied from class: `[Property](Property.html#clone())`
Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.
Overrides:
`[clone](AbstractChoiceProperty.html#clone())` in class `[AbstractChoiceProperty](AbstractChoiceProperty.html)`
Returns:
the cloned property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class ChoiceProperty">Class ChoiceProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance"><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.AbstractChoiceProperty</a>
<div class="inheritance">com.nomagic.magicdraw.properties.ChoiceProperty</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ChoiceProperty</span>
<span class="extends-implements">extends <a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></span></div>
<div class="block">The property selecting some value from a list of possible values or entering a new String value.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ChoiceProperty</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,int,java.util.List)">ChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice)</code></div>
<div class="col-last odd-row-color">
<div class="block">The constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,int,java.util.List,int)">ChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice,
 int max)</code></div>
<div class="col-last even-row-color">
<div class="block">The constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object,java.util.List)">ChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice)</code></div>
<div class="col-last odd-row-color">
<div class="block">The constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object,java.util.List,int)">ChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice,
 int max)</code></div>
<div class="col-last even-row-color">
<div class="block">The constructor.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the <code>PropertyVisitor</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex()">getIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the index of value in the choice list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAppendValue()">isAppendValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return append value flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAppendValue(boolean)">setAppendValue</a><wbr/>(boolean appendValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the append value flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChoice(java.util.List)">setChoice</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of possible values for selecting.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIndex(int)">setIndex</a><wbr/>(int val)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets index of selected value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value of the property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The string representation of the property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.AbstractChoiceProperty">Methods inherited from class com.nomagic.magicdraw.properties.<a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></h3>
<code><a href="AbstractChoiceProperty.html#getChoice()">getChoice</a>, <a href="AbstractChoiceProperty.html#isEditableValue()">isEditableValue</a>, <a href="AbstractChoiceProperty.html#isUndefinedStateAvailable()">isUndefinedStateAvailable</a>, <a href="AbstractChoiceProperty.html#isValuesTranslatable()">isValuesTranslatable</a>, <a href="AbstractChoiceProperty.html#setEditableValue(boolean)">setEditableValue</a>, <a href="AbstractChoiceProperty.html#setUndefinedStateAvailable(boolean)">setUndefinedStateAvailable</a>, <a href="AbstractChoiceProperty.html#setValuesTranslatable(boolean)">setValuesTranslatable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#getValue()">getValue</a>, <a href="Property.html#getValueStringRepresentation()">getValueStringRepresentation</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a></code></div>
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
<h3>ChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChoiceProperty</span>()</div>
<div class="block">Default constructor. Value of the property will be null.
 ID will be empty string.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object,java.util.List)">
<h3>ChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice)</span></div>
<div class="block">The constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>choice</code> - the list of possible values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object,java.util.List,int)">
<h3>ChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice,
 int max)</span></div>
<div class="block">The constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>choice</code> - the list of possible values.</dd>
<dd><code>max</code> - the maximum size of possible values list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,int,java.util.List,int)">
<h3>ChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice,
 int max)</span></div>
<div class="block">The constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>index</code> - the index in choice of selected value.</dd>
<dd><code>choice</code> - the list of possible values.</dd>
<dd><code>max</code> - the maximum size of possible values list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,int,java.util.List)">
<h3>ChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> choice)</span></div>
<div class="block">The constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>index</code> - the index in choice of selected value.</dd>
<dd><code>choice</code> - the list of possible values.</dd>
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
<section class="detail" id="isAppendValue()">
<h3>isAppendValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAppendValue</span>()</div>
<div class="block">Return append value flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the appendValue flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAppendValue(boolean)">
<h3>setAppendValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAppendValue</span><wbr/><span class="parameters">(boolean appendValue)</span></div>
<div class="block">Sets the append value flag.
 If property is editable, entered value is appended to the choice.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>appendValue</code> - the append state of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the <code>PropertyVisitor</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - the given visitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex()">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span>()</div>
<div class="block">Returns the index of value in the choice list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>index of value in the choice list; if value is not in the choice
 list, return -1.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChoice(java.util.List)">
<h3>setChoice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChoice</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> val)</span></div>
<div class="block">Sets the list of possible values for selecting.
 Sets only mMaximum number of values from the List's beginning.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractChoiceProperty.html#setChoice(java.util.List)">setChoice</a></code> in class <code><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></code></dd>
<dt>Parameters:</dt>
<dd><code>val</code> - a new possible values list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndex(int)">
<h3>setIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndex</span><wbr/><span class="parameters">(int val)</span></div>
<div class="block">Sets index of selected value.
 The index in possible values' list of new property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - a new index.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets value of the property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#setValue(java.lang.Object)">setValue</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - a new value.</dd>
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
<dd>PropertyID.CHOICE_PROPERTY.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#CHOICE_PROPERTY"><code>PropertyID.CHOICE_PROPERTY</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">The string representation of the property. Used for debugging purposes only.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#toString()">toString</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>the string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#clone()">Property</a></code></span></div>
<div class="block">Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractChoiceProperty.html#clone()">clone</a></code> in class <code><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned property.</dd>
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
