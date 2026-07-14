# JAVA OPENAPI: EventSupporter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/util/EventSupporter.html
- source_path: `com/nomagic/magicdraw/uml2/util/EventSupporter.html`
- source_sha256: `9c3d9a49c4d2be5d4844dd48a237937edd61bccd8c02d7021b25c4be1a90cb64`
- captured_utc: `2026-07-14T16:56:06.619583+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Interface EventSupporter

All Superinterfaces:
`com.dassault_systemes.modeler.foundation.util.EventSupporter`

public interfaceEventSupporterextends com.dassault_systemes.modeler.foundation.util.EventSupporter

Interface for MD event supporter.

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[firePropertyChange](#firePropertyChange(org.eclipse.emf.ecore.EStructuralFeature.Setting,java.lang.String,java.lang.Object,java.lang.Object,int,int))(org.eclipse.emf.ecore.EStructuralFeature.Setting setting,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)`
Deprecated.
not used
`boolean`
`[isRawMode](#isRawMode(org.eclipse.emf.ecore.EStructuralFeature.Setting))(org.eclipse.emf.ecore.EStructuralFeature.Setting setting)`
Deprecated.
not used
Methods inherited from interface com.dassault_systemes.modeler.foundation.util.EventSupporter
`afterChange, beforeChange, firePropertyChange, getPropertyEventName, getPropertyEventName, startLogEvents, stopLogEvents`

============ METHOD DETAIL ========== 
Method Details
firePropertyChange
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)void firePropertyChange(org.eclipse.emf.ecore.EStructuralFeature.Setting setting,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)
Deprecated.
not used
Implementation must fire property change event.
Parameters:
`setting` - setting that uses this event supporter.
`propertyName` - name of the changed property.
`oldValue` - old value of the property.
`newValue` - new value of the property.
`index` - index of the new value.
`newIndex` - new index of the value
isRawMode
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)boolean isRawMode(org.eclipse.emf.ecore.EStructuralFeature.Setting setting)
Deprecated.
not used

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Interface EventSupporter">Interface EventSupporter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.util.EventSupporter</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">EventSupporter</span><span class="extends-implements">
extends com.dassault_systemes.modeler.foundation.util.EventSupporter</span></div>
<div class="block">Interface for MD event supporter.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#firePropertyChange(org.eclipse.emf.ecore.EStructuralFeature.Setting,java.lang.String,java.lang.Object,java.lang.Object,int,int)">firePropertyChange</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature.Setting setting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#isRawMode(org.eclipse.emf.ecore.EStructuralFeature.Setting)">isRawMode</a><wbr/>(org.eclipse.emf.ecore.EStructuralFeature.Setting setting)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.util.EventSupporter">Methods inherited from interface com.dassault_systemes.modeler.foundation.util.EventSupporter</h3>
<code>afterChange, beforeChange, firePropertyChange, getPropertyEventName, getPropertyEventName, startLogEvents, stopLogEvents</code></div>
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
<section class="detail" id="firePropertyChange(org.eclipse.emf.ecore.EStructuralFeature.Setting,java.lang.String,java.lang.Object,java.lang.Object,int,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature.Setting setting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
<div class="block">Implementation must fire property change event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>setting</code> - setting that uses this event supporter.</dd>
<dd><code>propertyName</code> - name of the changed property.</dd>
<dd><code>oldValue</code> - old value of the property.</dd>
<dd><code>newValue</code> - new value of the property.</dd>
<dd><code>index</code> - index of the new value.</dd>
<dd><code>newIndex</code> - new index of the value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRawMode(org.eclipse.emf.ecore.EStructuralFeature.Setting)">
<h3>isRawMode</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">boolean</span> <span class="element-name">isRawMode</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EStructuralFeature.Setting setting)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
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
