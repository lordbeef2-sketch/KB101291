# JAVA OPENAPI: AbstractChoiceProperty (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/properties/AbstractChoiceProperty.html
- source_path: `com/nomagic/magicdraw/properties/AbstractChoiceProperty.html`
- source_sha256: `eacd8aec58764943df8889084987faf4bce2355392b5c09b1522d085d064e383`
- captured_utc: `2026-07-14T16:45:39.176522+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class AbstractChoiceProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
com.nomagic.magicdraw.properties.AbstractChoiceProperty

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ChoiceProperty](ChoiceProperty.html)`

@OpenApiAllpublic classAbstractChoiceProperty
extends [Property](Property.html)

Extracted more common class for Choice editing

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractChoiceProperty](#%3Cinit%3E())()`

`[AbstractChoiceProperty](#%3Cinit%3E(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AbstractChoiceProperty](AbstractChoiceProperty.html)`
`[clone](#clone())()`
Clones the property.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[getChoice](#getChoice())()`
Returns list of possible values.
`boolean`
`[isEditableValue](#isEditableValue())()`
Returns editable flag.
`boolean`
`[isUndefinedStateAvailable](#isUndefinedStateAvailable())()`

`boolean`
`[isValuesTranslatable](#isValuesTranslatable())()`

`void`
`[setChoice](#setChoice(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) val)`
Sets the list of possible values for selecting.
`void`
`[setEditableValue](#setEditableValue(boolean))(boolean editable)`
Sets the editable flag..
`void`
`[setUndefinedStateAvailable](#setUndefinedStateAvailable(boolean))(boolean undefinedStateAvailable)`

`void`
`[setValuesTranslatable](#setValuesTranslatable(boolean))(boolean valuesTranslatable)`
Set true, if values of this property must be translated with property's resource provider.
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [accept](Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [equals](Property.html#equals(java.lang.Object)), [firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getClassType](Property.html#getClassType()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [getValue](Property.html#getValue()), [getValueStringRepresentation](Property.html#getValueStringRepresentation()), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [isValueCompatible](Property.html#isValueCompatible(java.lang.Object)), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean)), [setValue](Property.html#setValue(java.lang.Object)), [toString](Property.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractChoiceProperty
public AbstractChoiceProperty()
AbstractChoiceProperty
public AbstractChoiceProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
 ============ METHOD DETAIL ========== 
Method Details
setEditableValue
public void setEditableValue(boolean editable)
Sets the editable flag..
 If property is editable, then value can be selected not just from the list, but entered the new one.
Parameters:
`editable` - the editable state of the property.
isEditableValue
public boolean isEditableValue()
Returns editable flag.
Returns:
the editable flag.
getChoice
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) getChoice()
Returns list of possible values.
Returns:
list of possible values.
setChoice
public void setChoice([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) val)
Sets the list of possible values for selecting.
 Sets only mMaximum number of values from the List's beginning.
Parameters:
`val` - a new possible values list.
isValuesTranslatable
public boolean isValuesTranslatable()
Returns:
true, if values of this property must be translated with property's resource provider
setValuesTranslatable
public void setValuesTranslatable(boolean valuesTranslatable)
Set true, if values of this property must be translated with property's resource provider.
Parameters:
`valuesTranslatable` - the new value of this flag.
clone
public [AbstractChoiceProperty](AbstractChoiceProperty.html) clone()
Description copied from class: `[Property](Property.html#clone())`
Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.
Overrides:
`[clone](Property.html#clone())` in class `[Property](Property.html)`
Returns:
the cloned property.
isUndefinedStateAvailable
public boolean isUndefinedStateAvailable()
setUndefinedStateAvailable
public void setUndefinedStateAvailable(boolean undefinedStateAvailable)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class AbstractChoiceProperty">Class AbstractChoiceProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance">com.nomagic.magicdraw.properties.AbstractChoiceProperty</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AbstractChoiceProperty</span>
<span class="extends-implements">extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span></div>
<div class="block">Extracted more common class for Choice editing</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractChoiceProperty</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object)">AbstractChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoice()">getChoice</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of possible values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditableValue()">isEditableValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns editable flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUndefinedStateAvailable()">isUndefinedStateAvailable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValuesTranslatable()">isValuesTranslatable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChoice(java.util.List)">setChoice</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> val)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of possible values for selecting.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEditableValue(boolean)">setEditableValue</a><wbr/>(boolean editable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the editable flag..</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUndefinedStateAvailable(boolean)">setUndefinedStateAvailable</a><wbr/>(boolean undefinedStateAvailable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValuesTranslatable(boolean)">setValuesTranslatable</a><wbr/>(boolean valuesTranslatable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set true, if values of this property must be translated with property's resource provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getClassType()">getClassType</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#getValue()">getValue</a>, <a href="Property.html#getValueStringRepresentation()">getValueStringRepresentation</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a>, <a href="Property.html#setValue(java.lang.Object)">setValue</a>, <a href="Property.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>AbstractChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractChoiceProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object)">
<h3>AbstractChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
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
<section class="detail" id="setEditableValue(boolean)">
<h3>setEditableValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEditableValue</span><wbr/><span class="parameters">(boolean editable)</span></div>
<div class="block">Sets the editable flag..
 If property is editable, then value can be selected not just from the list, but entered the new one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>editable</code> - the editable state of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditableValue()">
<h3>isEditableValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditableValue</span>()</div>
<div class="block">Returns editable flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the editable flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChoice()">
<h3>getChoice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">getChoice</span>()</div>
<div class="block">Returns list of possible values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of possible values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChoice(java.util.List)">
<h3>setChoice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChoice</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> val)</span></div>
<div class="block">Sets the list of possible values for selecting.
 Sets only mMaximum number of values from the List's beginning.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - a new possible values list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValuesTranslatable()">
<h3>isValuesTranslatable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValuesTranslatable</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if values of this property must be translated with property's resource provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValuesTranslatable(boolean)">
<h3>setValuesTranslatable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValuesTranslatable</span><wbr/><span class="parameters">(boolean valuesTranslatable)</span></div>
<div class="block">Set true, if values of this property must be translated with property's resource provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valuesTranslatable</code> - the new value of this flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Property.html#clone()">Property</a></code></span></div>
<div class="block">Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#clone()">clone</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUndefinedStateAvailable()">
<h3>isUndefinedStateAvailable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUndefinedStateAvailable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setUndefinedStateAvailable(boolean)">
<h3>setUndefinedStateAvailable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUndefinedStateAvailable</span><wbr/><span class="parameters">(boolean undefinedStateAvailable)</span></div>
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
