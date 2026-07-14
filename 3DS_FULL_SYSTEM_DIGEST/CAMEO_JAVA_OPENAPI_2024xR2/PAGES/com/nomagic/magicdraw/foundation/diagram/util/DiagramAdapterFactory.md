# JAVA OPENAPI: DiagramAdapterFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/foundation/diagram/util/DiagramAdapterFactory.html
- source_path: `com/nomagic/magicdraw/foundation/diagram/util/DiagramAdapterFactory.html`
- source_sha256: `fd00df1c085bd590ba5d13c257087d5e6aace57173877f3a376cb7f970268318`
- captured_utc: `2026-07-14T16:55:20.573066+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.diagram.util](package-summary.html)

## Class DiagramAdapterFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
com.nomagic.magicdraw.foundation.diagram.util.DiagramAdapterFactory

All Implemented Interfaces:
`org.eclipse.emf.common.notify.AdapterFactory`

public classDiagramAdapterFactory
extends org.eclipse.emf.common.notify.impl.AdapterFactoryImpl

begin-user-doc 
 The **Adapter Factory** for the model.
 It provides an adapter `createXXX` method for each class of the model.
 end-user-doc

See Also:
[`DiagramPackage`](../DiagramPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static [DiagramPackage](../DiagramPackage.html)`
`[modelPackage](#modelPackage)`
The cached model package.
`protected [DiagramSwitch](DiagramSwitch.html)<org.eclipse.emf.common.notify.Adapter>`
`[modelSwitch](#modelSwitch)`
The switch that delegates to the `createXXX` methods.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramAdapterFactory](#%3Cinit%3E())()`
Creates an instance of the adapter factory.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.notify.Adapter`
`[createAbstractDiagramRepresentationObjectAdapter](#createAbstractDiagramRepresentationObjectAdapter())()`
Creates a new adapter for an object of class '[`*Abstract Diagram Representation Object*`](../AbstractDiagramRepresentationObject.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createAdapter](#createAdapter(org.eclipse.emf.common.notify.Notifier))(org.eclipse.emf.common.notify.Notifier target)`
Creates an adapter for the `target`.
`org.eclipse.emf.common.notify.Adapter`
`[createDiagramContentsDescriptorAdapter](#createDiagramContentsDescriptorAdapter())()`
Creates a new adapter for an object of class '[`*Contents Descriptor*`](../DiagramContentsDescriptor.html)'.
`org.eclipse.emf.common.notify.Adapter`
`[createEObjectAdapter](#createEObjectAdapter())()`
Creates a new adapter for the default case.
`boolean`
`[isFactoryForType](#isFactoryForType(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Returns whether this factory is applicable for the type of the object.
Methods inherited from class org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
`adapt, adapt, adaptAllNew, adaptNew, associate, createAdapter, resolve`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
modelPackage
protected static [DiagramPackage](../DiagramPackage.html) modelPackage
The cached model package.
 begin-user-doc 
 end-user-doc
Generated:
modelSwitch
protected [DiagramSwitch](DiagramSwitch.html)<org.eclipse.emf.common.notify.Adapter> modelSwitch
The switch that delegates to the `createXXX` methods.
 begin-user-doc 
 end-user-doc
Generated:
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramAdapterFactory
public DiagramAdapterFactory()
Creates an instance of the adapter factory.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
isFactoryForType
public boolean isFactoryForType([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Returns whether this factory is applicable for the type of the object.
 begin-user-doc 
 This implementation returns `true` if the object is either the model's package or is an instance object of the model.
 end-user-doc
Specified by:
`isFactoryForType` in interface `org.eclipse.emf.common.notify.AdapterFactory`
Overrides:
`isFactoryForType` in class `org.eclipse.emf.common.notify.impl.AdapterFactoryImpl`
Returns:
whether this factory is applicable for the type of the object.
Generated:
createAdapter
public org.eclipse.emf.common.notify.Adapter createAdapter(org.eclipse.emf.common.notify.Notifier target)
Creates an adapter for the `target`.
 begin-user-doc 
 end-user-doc
Overrides:
`createAdapter` in class `org.eclipse.emf.common.notify.impl.AdapterFactoryImpl`
Parameters:
`target` - the object to adapt.
Returns:
the adapter for the `target`.
Generated:
createAbstractDiagramRepresentationObjectAdapter
public org.eclipse.emf.common.notify.Adapter createAbstractDiagramRepresentationObjectAdapter()
Creates a new adapter for an object of class '[`*Abstract Diagram Representation Object*`](../AbstractDiagramRepresentationObject.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`AbstractDiagramRepresentationObject`](../AbstractDiagramRepresentationObject.html)
Generated:
createDiagramContentsDescriptorAdapter
public org.eclipse.emf.common.notify.Adapter createDiagramContentsDescriptorAdapter()
Creates a new adapter for an object of class '[`*Contents Descriptor*`](../DiagramContentsDescriptor.html)'.
 begin-user-doc 
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 end-user-doc
Returns:
the new adapter.
See Also:
[`DiagramContentsDescriptor`](../DiagramContentsDescriptor.html)
Generated:
createEObjectAdapter
public org.eclipse.emf.common.notify.Adapter createEObjectAdapter()
Creates a new adapter for the default case.
 begin-user-doc 
 This default implementation returns null.
 end-user-doc
Returns:
the new adapter.
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.diagram.util</a></div>
<h1 class="title" title="Class DiagramAdapterFactory">Class DiagramAdapterFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
<div class="inheritance">com.nomagic.magicdraw.foundation.diagram.util.DiagramAdapterFactory</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.eclipse.emf.common.notify.AdapterFactory</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramAdapterFactory</span>
<span class="extends-implements">extends org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Adapter Factory</b> for the model.
 It provides an adapter <code>createXXX</code> method for each class of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>DiagramPackage</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
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
<div class="col-first even-row-color"><code>protected static <a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#modelPackage">modelPackage</a></code></div>
<div class="col-last even-row-color">
<div class="block">The cached model package.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a href="DiagramSwitch.html" title="class in com.nomagic.magicdraw.foundation.diagram.util">DiagramSwitch</a>&lt;org.eclipse.emf.common.notify.Adapter&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#modelSwitch">modelSwitch</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The switch that delegates to the <code>createXXX</code> methods.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramAdapterFactory</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the adapter factory.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAbstractDiagramRepresentationObjectAdapter()">createAbstractDiagramRepresentationObjectAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Abstract Diagram Representation Object</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAdapter(org.eclipse.emf.common.notify.Notifier)">createAdapter</a><wbr/>(org.eclipse.emf.common.notify.Notifier target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates an adapter for the <code>target</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramContentsDescriptorAdapter()">createDiagramContentsDescriptorAdapter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for an object of class '<a href="../DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Contents Descriptor</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.Adapter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEObjectAdapter()">createEObjectAdapter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new adapter for the default case.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFactoryForType(java.lang.Object)">isFactoryForType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this factory is applicable for the type of the object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.AdapterFactoryImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</h3>
<code>adapt, adapt, adaptAllNew, adaptNew, associate, createAdapter, resolve</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="modelPackage">
<h3>modelPackage</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></span> <span class="element-name">modelPackage</span></div>
<div class="block">The cached model package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="modelSwitch">
<h3>modelSwitch</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="DiagramSwitch.html" title="class in com.nomagic.magicdraw.foundation.diagram.util">DiagramSwitch</a>&lt;org.eclipse.emf.common.notify.Adapter&gt;</span> <span class="element-name">modelSwitch</span></div>
<div class="block">The switch that delegates to the <code>createXXX</code> methods.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
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
<section class="detail" id="&lt;init&gt;()">
<h3>DiagramAdapterFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramAdapterFactory</span>()</div>
<div class="block">Creates an instance of the adapter factory.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
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
<section class="detail" id="isFactoryForType(java.lang.Object)">
<h3>isFactoryForType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFactoryForType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Returns whether this factory is applicable for the type of the object.
 <!-- begin-user-doc -->
 This implementation returns <code>true</code> if the object is either the model's package or is an instance object of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isFactoryForType</code> in interface <code>org.eclipse.emf.common.notify.AdapterFactory</code></dd>
<dt>Overrides:</dt>
<dd><code>isFactoryForType</code> in class <code>org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</code></dd>
<dt>Returns:</dt>
<dd>whether this factory is applicable for the type of the object.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAdapter(org.eclipse.emf.common.notify.Notifier)">
<h3>createAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAdapter</span><wbr/><span class="parameters">(org.eclipse.emf.common.notify.Notifier target)</span></div>
<div class="block">Creates an adapter for the <code>target</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createAdapter</code> in class <code>org.eclipse.emf.common.notify.impl.AdapterFactoryImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>target</code> - the object to adapt.</dd>
<dt>Returns:</dt>
<dd>the adapter for the <code>target</code>.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAbstractDiagramRepresentationObjectAdapter()">
<h3>createAbstractDiagramRepresentationObjectAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createAbstractDiagramRepresentationObjectAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Abstract Diagram Representation Object</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>AbstractDiagramRepresentationObject</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramContentsDescriptorAdapter()">
<h3>createDiagramContentsDescriptorAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createDiagramContentsDescriptorAdapter</span>()</div>
<div class="block">Creates a new adapter for an object of class '<a href="../DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code><em>Contents Descriptor</em></code></a>'.
 <!-- begin-user-doc -->
 This default implementation returns null so that we can easily ignore cases;
 it's useful to ignore a case when inheritance will catch all the cases anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>DiagramContentsDescriptor</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEObjectAdapter()">
<h3>createEObjectAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.Adapter</span> <span class="element-name">createEObjectAdapter</span>()</div>
<div class="block">Creates a new adapter for the default case.
 <!-- begin-user-doc -->
 This default implementation returns null.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new adapter.</dd>
<dt>Generated:</dt>
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
