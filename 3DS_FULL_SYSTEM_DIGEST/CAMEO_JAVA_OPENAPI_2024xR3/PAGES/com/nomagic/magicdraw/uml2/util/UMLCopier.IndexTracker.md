# JAVA OPENAPI: UMLCopier.IndexTracker (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/util/UMLCopier.IndexTracker.html
- source_path: `com/nomagic/magicdraw/uml2/util/UMLCopier.IndexTracker.html`
- source_sha256: `2a420b58d274cfaf9f2ba538682580e3577d867081dc0cf55ca2d3fe3a12dcca`
- captured_utc: `2026-07-14T16:56:07.731599+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class UMLCopier.IndexTracker

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.util.UMLCopier.IndexTracker

Enclosing class:
[UMLCopier](UMLCopier.html)

protected static classUMLCopier.IndexTracker
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[IndexTracker](#%3Cinit%3E(org.eclipse.emf.ecore.util.InternalEList))(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> target)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getIndex](#getIndex(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject obj)`

`void`
`[refreshOnAdd](#refreshOnAdd(org.eclipse.emf.ecore.util.InternalEList,int,org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)`

`void`
`[refreshOnMove](#refreshOnMove(org.eclipse.emf.ecore.util.InternalEList,int,int,org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 int index,
 int oldIndex,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
IndexTracker
public IndexTracker(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> target)
 ============ METHOD DETAIL ========== 
Method Details
getIndex
public int getIndex(org.eclipse.emf.ecore.EObject obj)
refreshOnAdd
public void refreshOnAdd(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)
refreshOnMove
public void refreshOnMove(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 int index,
 int oldIndex,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class UMLCopier.IndexTracker">Class UMLCopier.IndexTracker</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.util.UMLCopier.IndexTracker</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UMLCopier.html" title="class in com.nomagic.magicdraw.uml2.util">UMLCopier</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">protected static class </span><span class="element-name type-name-label">UMLCopier.IndexTracker</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(org.eclipse.emf.ecore.util.InternalEList)">IndexTracker</a><wbr/>(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; target)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex(org.eclipse.emf.ecore.EObject)">getIndex</a><wbr/>(org.eclipse.emf.ecore.EObject obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refreshOnAdd(org.eclipse.emf.ecore.util.InternalEList,int,org.eclipse.emf.ecore.EObject)">refreshOnAdd</a><wbr/>(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refreshOnMove(org.eclipse.emf.ecore.util.InternalEList,int,int,org.eclipse.emf.ecore.EObject)">refreshOnMove</a><wbr/>(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 int index,
 int oldIndex,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(org.eclipse.emf.ecore.util.InternalEList)">
<h3>IndexTracker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IndexTracker</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; target)</span></div>
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
<section class="detail" id="getIndex(org.eclipse.emf.ecore.EObject)">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject obj)</span></div>
</section>
</li>
<li>
<section class="detail" id="refreshOnAdd(org.eclipse.emf.ecore.util.InternalEList,int,org.eclipse.emf.ecore.EObject)">
<h3>refreshOnAdd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refreshOnAdd</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)</span></div>
</section>
</li>
<li>
<section class="detail" id="refreshOnMove(org.eclipse.emf.ecore.util.InternalEList,int,int,org.eclipse.emf.ecore.EObject)">
<h3>refreshOnMove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refreshOnMove</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 int index,
 int oldIndex,
 org.eclipse.emf.ecore.EObject copyReferencedEObject)</span></div>
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
