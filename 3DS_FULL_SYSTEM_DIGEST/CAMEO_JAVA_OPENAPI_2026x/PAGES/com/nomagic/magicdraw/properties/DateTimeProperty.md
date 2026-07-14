# JAVA OPENAPI: DateTimeProperty (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/properties/DateTimeProperty.html
- source_path: `com/nomagic/magicdraw/properties/DateTimeProperty.html`
- source_sha256: `ae4206db8163433d06912ef56ef95441576c8352485f5abd8a53195f301d9334`
- captured_utc: `2026-07-14T16:58:00.304561+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class DateTimeProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
[com.nomagic.magicdraw.properties.StringProperty](StringProperty.html)
com.nomagic.magicdraw.properties.DateTimeProperty

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classDateTimeProperty
extends [StringProperty](StringProperty.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DateTimeProperty](#%3Cinit%3E())()`
Default constructor.
`[DateTimeProperty](#%3Cinit%3E(java.lang.String,java.lang.Object,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 boolean multiline,
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)`
Deprecated.
use [`DateTimeProperty(String, String, boolean, Type)`](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))
`[DateTimeProperty](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 boolean multiline,
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the given visitor.
`[DateTimeProperty](DateTimeProperty.html)`
`[clone](#clone())()`
Clones the property.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html)`
`[getType](#getType())()`
Returns type of property
Methods inherited from class com.nomagic.magicdraw.properties.[StringProperty](StringProperty.html)
`[getString](StringProperty.html#getString()), [getValueStringRepresentation](StringProperty.html#getValueStringRepresentation()), [isMultiline](StringProperty.html#isMultiline()), [setMultiline](StringProperty.html#setMultiline(boolean)), [setValue](StringProperty.html#setValue(java.lang.Object))`
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [equals](Property.html#equals(java.lang.Object)), [firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [getValue](Property.html#getValue()), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [isValueCompatible](Property.html#isValueCompatible(java.lang.Object)), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean)), [toString](Property.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DateTimeProperty
public DateTimeProperty()
Default constructor. Value of the property will be null. ID will be empty string. Property is editable.
DateTimeProperty
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public DateTimeProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 boolean multiline,
 @CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)
Deprecated.
use [`DateTimeProperty(String, String, boolean, Type)`](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))
DateTimeProperty
public DateTimeProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 boolean multiline,
 @CheckForNull
 [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)
 ============ METHOD DETAIL ========== 
Method Details
getType
@CheckForNullpublic [Type](../../uml2/ext/magicdraw/classes/mdkernel/Type.html) getType()
Returns type of property
Returns:
type of property
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Description copied from class: `[StringProperty](StringProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))`
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](StringProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[StringProperty](StringProperty.html)`
Parameters:
`v` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
getClassType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getClassType()
Description copied from class: `[StringProperty](StringProperty.html#getClassType())`
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](StringProperty.html#getClassType())` in class `[StringProperty](StringProperty.html)`
Returns:
PropertyID.STRING_PROPERTY
See Also:
[`PropertyID.STRING_PROPERTY`](PropertyID.html#STRING_PROPERTY)
clone
public [DateTimeProperty](DateTimeProperty.html) clone()
Description copied from class: `[Property](Property.html#clone())`
Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.
Overrides:
`[clone](StringProperty.html#clone())` in class `[StringProperty](StringProperty.html)`
Returns:
the cloned property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class DateTimeProperty">Class DateTimeProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance"><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.StringProperty</a>
<div class="inheritance">com.nomagic.magicdraw.properties.DateTimeProperty</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DateTimeProperty</span>
<span class="extends-implements">extends <a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DateTimeProperty</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">DateTimeProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean multiline,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)"><code>DateTimeProperty(String, String, boolean, Type)</code></a></div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">DateTimeProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 boolean multiline,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns type of property</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.StringProperty">Methods inherited from class com.nomagic.magicdraw.properties.<a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></h3>
<code><a href="StringProperty.html#getString()">getString</a>, <a href="StringProperty.html#getValueStringRepresentation()">getValueStringRepresentation</a>, <a href="StringProperty.html#isMultiline()">isMultiline</a>, <a href="StringProperty.html#setMultiline(boolean)">setMultiline</a>, <a href="StringProperty.html#setValue(java.lang.Object)">setValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#getValue()">getValue</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a>, <a href="Property.html#toString()">toString</a></code></div>
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
<h3>DateTimeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DateTimeProperty</span>()</div>
<div class="block">Default constructor. Value of the property will be null. ID will be empty string. Property is editable.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>DateTimeProperty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">DateTimeProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean multiline,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)"><code>DateTimeProperty(String, String, boolean, Type)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,boolean,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>DateTimeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DateTimeProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 boolean multiline,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns type of property</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="StringProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">StringProperty</a></code></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="StringProperty.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="StringProperty.html#getClassType()">StringProperty</a></code></span></div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="StringProperty.html#getClassType()">getClassType</a></code> in class <code><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.STRING_PROPERTY</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PropertyID.html#STRING_PROPERTY"><code>PropertyID.STRING_PROPERTY</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Property.html#clone()">Property</a></code></span></div>
<div class="block">Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="StringProperty.html#clone()">clone</a></code> in class <code><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></code></dd>
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
