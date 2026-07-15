# JAVA OPENAPI: ModelListener (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/transaction/ModelListener.html
- source_path: `com/nomagic/uml2/transaction/ModelListener.html`
- source_sha256: `511438003338e10d82d1241d3477e55a9b0f5124b4e89f1c70ec51bca5fde657`
- captured_utc: `2026-07-14T16:56:21.388751+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Interface ModelListener

All Superinterfaces:
`com.dassault_systemes.modeler.foundation.events.ModelListener`

public interfaceModelListenerextends com.dassault_systemes.modeler.foundation.events.ModelListener

Listener for model changes.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[beforeChange](#beforeChange(javax.jmi.reflect.RefObject,java.lang.String))(javax.jmi.reflect.RefObject abstractRefObject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)`
Method is called before model is changed.
`default void`
`[eventDeliveryRestored](#eventDeliveryRestored(com.dassault_systemes.modeler.foundation.events.ModifiedElements,java.util.List))(com.dassault_systemes.modeler.foundation.events.ModifiedElements modifiedElements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> propertyChangeEvents)`
Notifies the listener that event delivery has been restored
`void`
`[eventDeliveryRestored](#eventDeliveryRestored(com.nomagic.uml2.ext.jmi.ModifiedElements,java.util.List))(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> propertyChangeEvents)`
Notifies the listener that event delivery has been restored
Methods inherited from interface com.dassault_systemes.modeler.foundation.events.ModelListener
`beforeChange, eventDeliveryStopped, modelChanged`

============ METHOD DETAIL ========== 
Method Details
beforeChange
default void beforeChange(javax.jmi.reflect.RefObject abstractRefObject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)
Method is called before model is changed.
Parameters:
`abstractRefObject` - object which will be changed
`featureName` - feature name which will be changed
eventDeliveryRestored
void eventDeliveryRestored(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> propertyChangeEvents)
Notifies the listener that event delivery has been restored
Parameters:
`modifiedElements` - modified elements during events stopped
`propertyChangeEvents` - events generated while delivery was stopped
eventDeliveryRestored
default void eventDeliveryRestored(com.dassault_systemes.modeler.foundation.events.ModifiedElements modifiedElements,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> propertyChangeEvents)
Description copied from interface: `com.dassault_systemes.modeler.foundation.events.ModelListener`
Notifies the listener that event delivery has been restored
Specified by:
`eventDeliveryRestored` in interface `com.dassault_systemes.modeler.foundation.events.ModelListener`
Parameters:
`modifiedElements` - modified elements during events stopped
`propertyChangeEvents` - events generated while delivery was stopped

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Interface ModelListener">Interface ModelListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.events.ModelListener</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelListener</span><span class="extends-implements">
extends com.dassault_systemes.modeler.foundation.events.ModelListener</span></div>
<div class="block">Listener for model changes.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#beforeChange(javax.jmi.reflect.RefObject,java.lang.String)">beforeChange</a><wbr/>(javax.jmi.reflect.RefObject abstractRefObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method is called before model is changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#eventDeliveryRestored(com.dassault_systemes.modeler.foundation.events.ModifiedElements,java.util.List)">eventDeliveryRestored</a><wbr/>(com.dassault_systemes.modeler.foundation.events.ModifiedElements modifiedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; propertyChangeEvents)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Notifies the listener that event delivery has been restored</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#eventDeliveryRestored(com.nomagic.uml2.ext.jmi.ModifiedElements,java.util.List)">eventDeliveryRestored</a><wbr/>(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; propertyChangeEvents)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Notifies the listener that event delivery has been restored</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.events.ModelListener">Methods inherited from interface com.dassault_systemes.modeler.foundation.events.ModelListener</h3>
<code>beforeChange, eventDeliveryStopped, modelChanged</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="beforeChange(javax.jmi.reflect.RefObject,java.lang.String)">
<h3>beforeChange</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">beforeChange</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject abstractRefObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</span></div>
<div class="block">Method is called before model is changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>abstractRefObject</code> - object which will be changed</dd>
<dd><code>featureName</code> - feature name which will be changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventDeliveryRestored(com.nomagic.uml2.ext.jmi.ModifiedElements,java.util.List)">
<h3>eventDeliveryRestored</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">eventDeliveryRestored</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; propertyChangeEvents)</span></div>
<div class="block">Notifies the listener that event delivery has been restored</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modifiedElements</code> - modified elements during events stopped</dd>
<dd><code>propertyChangeEvents</code> - events generated while delivery was stopped</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventDeliveryRestored(com.dassault_systemes.modeler.foundation.events.ModifiedElements,java.util.List)">
<h3>eventDeliveryRestored</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">eventDeliveryRestored</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.events.ModifiedElements modifiedElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; propertyChangeEvents)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.events.ModelListener</code></span></div>
<div class="block">Notifies the listener that event delivery has been restored</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>eventDeliveryRestored</code> in interface <code>com.dassault_systemes.modeler.foundation.events.ModelListener</code></dd>
<dt>Parameters:</dt>
<dd><code>modifiedElements</code> - modified elements during events stopped</dd>
<dd><code>propertyChangeEvents</code> - events generated while delivery was stopped</dd>
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
