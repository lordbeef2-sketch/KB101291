# JAVA OPENAPI: SmartPropertyChangeEvent (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/smartlistener/SmartPropertyChangeEvent.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartPropertyChangeEvent.html`
- source_sha256: `d05298001e7a5220a4c2d681647bdba350bef421122498840fd1c20778b595bc`
- captured_utc: `2026-07-14T16:56:10.422628+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Class SmartPropertyChangeEvent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.EventObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html)
[java.beans.PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)
com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeEvent

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classSmartPropertyChangeEvent
extends [PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)

Property change event which will be fired by SmartPropertyChangeListener.

See Also:
[Serialized Form](../../../../../../serialized-form.html#com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeEvent)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.util.[EventObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html)
`[source](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html#source)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SmartPropertyChangeEvent](#%3Cinit%3E(java.beans.PropertyChangeEvent,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event,
 [Element](../../magicdraw/classes/mdkernel/Element.html) topSource)`
Creates and initializes a new `SmartPropertyChangeEvent` object from specified parameters.
`[SmartPropertyChangeEvent](#%3Cinit%3E(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 [Element](../../magicdraw/classes/mdkernel/Element.html) topSource)`
Creates and initializes a new `SmartPropertyChangeEvent` object from specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Element](../../magicdraw/classes/mdkernel/Element.html)`
`[getTopSource](#getTopSource())()`
Returns a top source of the event.
Methods inherited from class java.beans.[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)
`[getNewValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getNewValue()), [getOldValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getOldValue()), [getPropagationId](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropagationId()), [getPropertyName](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropertyName()), [setPropagationId](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#setPropagationId(java.lang.Object)), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#toString())`
Methods inherited from class java.util.[EventObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html)
`[getSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html#getSource())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SmartPropertyChangeEvent
public SmartPropertyChangeEvent([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event,
 [Element](../../magicdraw/classes/mdkernel/Element.html) topSource)
Creates and initializes a new `SmartPropertyChangeEvent` object from specified parameters.
 All properties of the specified event will be copied into new instance properties.
Parameters:
`event` - `PropertyChangeEvent` object.
`topSource` - top source of the event.
SmartPropertyChangeEvent
public SmartPropertyChangeEvent([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 [Element](../../magicdraw/classes/mdkernel/Element.html) topSource)
Creates and initializes a new `SmartPropertyChangeEvent` object from specified parameters.
Parameters:
`source` - source of the event.
`propertyName` - a name of the property.
`oldValue` - old value.
`newValue` - new value.
`topSource` - top source of the event.
 ============ METHOD DETAIL ========== 
Method Details
getTopSource
public [Element](../../magicdraw/classes/mdkernel/Element.html) getTopSource()
Returns a top source of the event.
Returns:
top source.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Class SmartPropertyChangeEvent">Class SmartPropertyChangeEvent</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html" title="class or interface in java.util">java.util.EventObject</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">java.beans.PropertyChangeEvent</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeEvent</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SmartPropertyChangeEvent</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a></span></div>
<div class="block">Property change event which will be fired by SmartPropertyChangeListener.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../serialized-form.html#com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeEvent">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.util.EventObject">Fields inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html" title="class or interface in java.util">EventObject</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html#source" title="class or interface in java.util">source</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.beans.PropertyChangeEvent,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">SmartPropertyChangeEvent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> topSource)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>SmartPropertyChangeEvent</code> object from specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">SmartPropertyChangeEvent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> topSource)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>SmartPropertyChangeEvent</code> object from specified parameters.</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTopSource()">getTopSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a top source of the event.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.beans.PropertyChangeEvent">Methods inherited from class java.beans.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getNewValue()" title="class or interface in java.beans">getNewValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getOldValue()" title="class or interface in java.beans">getOldValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropagationId()" title="class or interface in java.beans">getPropagationId</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropertyName()" title="class or interface in java.beans">getPropertyName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#setPropagationId(java.lang.Object)" title="class or interface in java.beans">setPropagationId</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#toString()" title="class or interface in java.beans">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.EventObject">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html" title="class or interface in java.util">EventObject</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventObject.html#getSource()" title="class or interface in java.util">getSource</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.beans.PropertyChangeEvent,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>SmartPropertyChangeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartPropertyChangeEvent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> topSource)</span></div>
<div class="block">Creates and initializes a new <code>SmartPropertyChangeEvent</code> object from specified parameters.
 All properties of the specified event will be copied into new instance properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - <code>PropertyChangeEvent</code> object.</dd>
<dd><code>topSource</code> - top source of the event.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>SmartPropertyChangeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartPropertyChangeEvent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> topSource)</span></div>
<div class="block">Creates and initializes a new <code>SmartPropertyChangeEvent</code> object from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source of the event.</dd>
<dd><code>propertyName</code> - a name of the property.</dd>
<dd><code>oldValue</code> - old value.</dd>
<dd><code>newValue</code> - new value.</dd>
<dd><code>topSource</code> - top source of the event.</dd>
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
<section class="detail" id="getTopSource()">
<h3>getTopSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getTopSource</span>()</div>
<div class="block">Returns a top source of the event.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>top source.</dd>
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
