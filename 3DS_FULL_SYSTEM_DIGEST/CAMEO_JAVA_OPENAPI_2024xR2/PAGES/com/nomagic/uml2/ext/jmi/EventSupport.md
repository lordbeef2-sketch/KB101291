# JAVA OPENAPI: EventSupport (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/EventSupport.html
- source_path: `com/nomagic/uml2/ext/jmi/EventSupport.html`
- source_sha256: `265af5b98f8cfb42cb831469b3537fa8f115e7d5d7271c4ea797f2215a8713f8`
- captured_utc: `2026-07-14T16:56:07.909598+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi](package-summary.html)

## Class EventSupport

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>
com.nomagic.uml2.ext.jmi.EventSupport

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.events.RepositoryListenerRegistry<javax.jmi.reflect.RefObject>`, `[RepositoryListenerRegistry](RepositoryListenerRegistry.html)`

public classEventSupport
extends com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>
implements [RepositoryListenerRegistry](RepositoryListenerRegistry.html)

Class for firing events and handling event listeners.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final org.apache.logging.log4j.Logger`
`[LOG](#LOG)`
Fields inherited from class com.dassault_systemes.modeler.foundation.events.EventSupport
`EVENT_FIRE_START, EVENT_FIRE_STOP`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EventSupport](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository))([AbstractRepository](reflect/AbstractRepository.html) abstractRepository)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected com.nomagic.uml2.ext.jmi.IndexedPropertyChangeEvent`
`[createIndexedPropertyChangeEvent](#createIndexedPropertyChangeEvent(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,int))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)`

`void`
`[fireInstanceDeletedEvent](#fireInstanceDeletedEvent(javax.jmi.reflect.RefBaseObject,java.lang.Object,java.lang.Object))(javax.jmi.reflect.RefBaseObject source,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) deleted,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldDirectContainer)`
Fires event about an instance delete.
`void`
`[fireModelElementDisposeEvent](#fireModelElementDisposeEvent(javax.jmi.reflect.RefObject,java.lang.Object))(javax.jmi.reflect.RefObject disposed,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldDirectContainer)`
Fires event about an instance disposal.
`void`
`[firePropertyChange](#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object))(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`

`void`
`[firePropertyChange](#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int))(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)`

`void`
`[firePropertyChange](#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int,int))(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)`

`com.nomagic.uml2.ext.jmi.NonMaskedEventSupport`
`[getNonMaskedModelListeners](#getNonMaskedModelListeners())()`

`protected boolean`
`[isDeveloper](#isDeveloper())()`

`protected boolean`
`[isNotDeliveredEventElement](#isNotDeliveredEventElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`

`void`
`[restoreEventDelivery](#restoreEventDelivery(com.nomagic.uml2.ext.jmi.ModifiedElements))(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)`
Restores event delivery.
Methods inherited from class com.dassault_systemes.modeler.foundation.events.EventSupport
`addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addRepositoryListener, callModelListener, fireCountedPropertyChange, firePropertyChange, firePropertyChange, fireRepositoryPropertyChange, getEventsCount, internalFireUncountedPropertyChange, invokeAfterTransaction, isEnableEventFiring, isModelCleanAfterEventsStopped, removeAllPropertyChangeListeners, removeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removeRepositoryListener, restoreEventDelivery, setEnableEventFiring, setModelListener, startLogEvents, stopEventDelivery, stopLogEvents`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.events.RepositoryListenerRegistry
`addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, removeAllPropertyChangeListeners, removeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener`

============ FIELD DETAIL =========== 
Field Details
LOG
public static final org.apache.logging.log4j.Logger LOG
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EventSupport
public EventSupport([AbstractRepository](reflect/AbstractRepository.html) abstractRepository)
 ============ METHOD DETAIL ========== 
Method Details
isNotDeliveredEventElement
protected boolean isNotDeliveredEventElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Specified by:
`isNotDeliveredEventElement` in class `com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>`
createIndexedPropertyChangeEvent
protected com.nomagic.uml2.ext.jmi.IndexedPropertyChangeEvent createIndexedPropertyChangeEvent([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)
Overrides:
`createIndexedPropertyChangeEvent` in class `com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>`
firePropertyChange
public void firePropertyChange(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
fireModelElementDisposeEvent
public void fireModelElementDisposeEvent(javax.jmi.reflect.RefObject disposed,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldDirectContainer)
Description copied from class: `com.dassault_systemes.modeler.foundation.events.EventSupport`
Fires event about an instance disposal.
Overrides:
`fireModelElementDisposeEvent` in class `com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>`
Parameters:
`disposed` - element that was disposed.
`oldDirectContainer` - old direct container (feature data set or resource).
fireInstanceDeletedEvent
public void fireInstanceDeletedEvent(javax.jmi.reflect.RefBaseObject source,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) deleted,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldDirectContainer)
Fires event about an instance delete.
Parameters:
`source` - source of the event.
`deleted` - element that was deleted.
`oldDirectContainer` - old direct container (feature data set or resource).
firePropertyChange
public void firePropertyChange(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)
firePropertyChange
public void firePropertyChange(javax.jmi.reflect.RefBaseObject source,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)
isDeveloper
protected boolean isDeveloper()
Specified by:
`isDeveloper` in class `com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>`
restoreEventDelivery
public void restoreEventDelivery(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)
Restores event delivery. Non-masked event listeners will start getting
 events again. If event firing was not disabled via
 `EventSupport.setEnableEventFiring(boolean)` then other event listeners will
 start getting events and [`UML2MetamodelConstants.EVENT_FIRE_START`](UML2MetamodelConstants.html#EVENT_FIRE_START)
 will be fired for repository property change listeners
Parameters:
`modifiedElements` - provider for changed elements
getNonMaskedModelListeners
public com.nomagic.uml2.ext.jmi.NonMaskedEventSupport getNonMaskedModelListeners()
Overrides:
`getNonMaskedModelListeners` in class `com.dassault_systemes.modeler.foundation.events.EventSupport<javax.jmi.reflect.RefObject>`
Returns:
ModelListener which sends notification even event fire is disabled.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi</a></div>
<h1 class="title" title="Class EventSupport">Class EventSupport</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;
<div class="inheritance">com.nomagic.uml2.ext.jmi.EventSupport</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.events.RepositoryListenerRegistry&lt;javax.jmi.reflect.RefObject&gt;</code>, <code><a href="RepositoryListenerRegistry.html" title="interface in com.nomagic.uml2.ext.jmi">RepositoryListenerRegistry</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">EventSupport</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;
implements <a href="RepositoryListenerRegistry.html" title="interface in com.nomagic.uml2.ext.jmi">RepositoryListenerRegistry</a></span></div>
<div class="block">Class for firing events and handling event listeners.</div>
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
<div class="col-first even-row-color"><code>static final org.apache.logging.log4j.Logger</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOG">LOG</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.dassault_systemes.modeler.foundation.events.EventSupport">Fields inherited from class com.dassault_systemes.modeler.foundation.events.EventSupport</h3>
<code>EVENT_FIRE_START, EVENT_FIRE_STOP</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">EventSupport</a><wbr/>(<a href="reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> abstractRepository)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.uml2.ext.jmi.IndexedPropertyChangeEvent</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createIndexedPropertyChangeEvent(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,int)">createIndexedPropertyChangeEvent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireInstanceDeletedEvent(javax.jmi.reflect.RefBaseObject,java.lang.Object,java.lang.Object)">fireInstanceDeletedEvent</a><wbr/>(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> deleted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldDirectContainer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fires event about an instance delete.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireModelElementDisposeEvent(javax.jmi.reflect.RefObject,java.lang.Object)">fireModelElementDisposeEvent</a><wbr/>(javax.jmi.reflect.RefObject disposed,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldDirectContainer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fires event about an instance disposal.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int)">firePropertyChange</a><wbr/>(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int,int)">firePropertyChange</a><wbr/>(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.uml2.ext.jmi.NonMaskedEventSupport</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNonMaskedModelListeners()">getNonMaskedModelListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDeveloper()">isDeveloper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNotDeliveredEventElement(java.lang.Object)">isNotDeliveredEventElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#restoreEventDelivery(com.nomagic.uml2.ext.jmi.ModifiedElements)">restoreEventDelivery</a><wbr/>(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Restores event delivery.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.events.EventSupport">Methods inherited from class com.dassault_systemes.modeler.foundation.events.EventSupport</h3>
<code>addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addRepositoryListener, callModelListener, fireCountedPropertyChange, firePropertyChange, firePropertyChange, fireRepositoryPropertyChange, getEventsCount, internalFireUncountedPropertyChange, invokeAfterTransaction, isEnableEventFiring, isModelCleanAfterEventsStopped, removeAllPropertyChangeListeners, removeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removeRepositoryListener, restoreEventDelivery, setEnableEventFiring, setModelListener, startLogEvents, stopEventDelivery, stopLogEvents</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.events.RepositoryListenerRegistry">Methods inherited from interface com.dassault_systemes.modeler.foundation.events.RepositoryListenerRegistry</h3>
<code>addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, addPropertyChangeListener, removeAllPropertyChangeListeners, removeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener, removePropertyChangeListener</code></div>
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
<section class="detail" id="LOG">
<h3>LOG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">org.apache.logging.log4j.Logger</span> <span class="element-name">LOG</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">
<h3>EventSupport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EventSupport</span><wbr/><span class="parameters">(<a href="reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> abstractRepository)</span></div>
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
<section class="detail" id="isNotDeliveredEventElement(java.lang.Object)">
<h3>isNotDeliveredEventElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNotDeliveredEventElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isNotDeliveredEventElement</code> in class <code>com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIndexedPropertyChangeEvent(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object,int)">
<h3>createIndexedPropertyChangeEvent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.uml2.ext.jmi.IndexedPropertyChangeEvent</span> <span class="element-name">createIndexedPropertyChangeEvent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createIndexedPropertyChangeEvent</code> in class <code>com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
</section>
</li>
<li>
<section class="detail" id="fireModelElementDisposeEvent(javax.jmi.reflect.RefObject,java.lang.Object)">
<h3>fireModelElementDisposeEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireModelElementDisposeEvent</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject disposed,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldDirectContainer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.events.EventSupport</code></span></div>
<div class="block">Fires event about an instance disposal.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>fireModelElementDisposeEvent</code> in class <code>com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>disposed</code> - element that was disposed.</dd>
<dd><code>oldDirectContainer</code> - old direct container (feature data set or resource).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireInstanceDeletedEvent(javax.jmi.reflect.RefBaseObject,java.lang.Object,java.lang.Object)">
<h3>fireInstanceDeletedEvent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireInstanceDeletedEvent</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> deleted,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldDirectContainer)</span></div>
<div class="block">Fires event about an instance delete.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source of the event.</dd>
<dd><code>deleted</code> - element that was deleted.</dd>
<dd><code>oldDirectContainer</code> - old direct container (feature data set or resource).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</span></div>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(javax.jmi.reflect.RefBaseObject,java.lang.String,java.lang.Object,java.lang.Object,int,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDeveloper()">
<h3>isDeveloper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isDeveloper</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isDeveloper</code> in class <code>com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="restoreEventDelivery(com.nomagic.uml2.ext.jmi.ModifiedElements)">
<h3>restoreEventDelivery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">restoreEventDelivery</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)</span></div>
<div class="block">Restores event delivery. Non-masked event listeners will start getting
 events again. If event firing was not disabled via
 <code>EventSupport.setEnableEventFiring(boolean)</code> then other event listeners will
 start getting events and <a href="UML2MetamodelConstants.html#EVENT_FIRE_START"><code>UML2MetamodelConstants.EVENT_FIRE_START</code></a>
 will be fired for repository property change listeners</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modifiedElements</code> - provider for changed elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNonMaskedModelListeners()">
<h3>getNonMaskedModelListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.uml2.ext.jmi.NonMaskedEventSupport</span> <span class="element-name">getNonMaskedModelListeners</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getNonMaskedModelListeners</code> in class <code>com.dassault_systemes.modeler.foundation.events.EventSupport&lt;javax.jmi.reflect.RefObject&gt;</code></dd>
<dt>Returns:</dt>
<dd>ModelListener which sends notification even event fire is disabled.</dd>
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
