# JAVA OPENAPI: PersistenceManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/dependencymatrix/persistence/PersistenceManager.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/PersistenceManager.html`
- source_sha256: `6b788a2166389cbeb516f2e827e31bf0e6fa10a889b54ecf4e8929461a9468f3`
- captured_utc: `2026-07-14T16:55:14.222995+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Class PersistenceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager

@OpenApiAllpublic classPersistenceManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
All main matrix settings holder, which holds the references to the row, column and all
 general Dependency Matrix settings

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[PersistenceManager](#%3Cinit%3E())()`
Used to initialize quick tests.
``
`[PersistenceManager](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Initializes matrix settings component from provided Diagram element
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[FilterSettings](FilterSettings.html)`
`[getColumnSettings](#getColumnSettings())()`
Column filter settings
`[MatrixSettings](MatrixSettings.html)`
`[getMatrixSettings](#getMatrixSettings())()`
General matrix settings
`[Project](../../core/Project.html)`
`[getProject](#getProject())()`
Returns project of this matrix
`[FilterSettings](FilterSettings.html)`
`[getRowSettings](#getRowSettings())()`
Row filter settings
`boolean`
`[isMainCriteriaDefined](#isMainCriteriaDefined())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PersistenceManager
public PersistenceManager([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Initializes matrix settings component from provided Diagram element
Parameters:
`diagram` - Matrix element
PersistenceManager
protected PersistenceManager()
Used to initialize quick tests.
 ============ METHOD DETAIL ========== 
Method Details
getMatrixSettings
public [MatrixSettings](MatrixSettings.html) getMatrixSettings()
General matrix settings
Returns:
settings for whole dependency matrix
getRowSettings
public [FilterSettings](FilterSettings.html) getRowSettings()
Row filter settings
Returns:
settings of the row filter
getColumnSettings
public [FilterSettings](FilterSettings.html) getColumnSettings()
Column filter settings
Returns:
settings of the column filter
getProject
public [Project](../../core/Project.html) getProject()
Returns project of this matrix
Returns:
project instance
isMainCriteriaDefined
public boolean isMainCriteriaDefined()
Returns:
true if row element type, row scope, column element type, column scope and dependency criteria
 are all defined in these settings

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Class PersistenceManager">Class PersistenceManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PersistenceManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">All main matrix settings holder, which holds the references to the row, column and all
 general Dependency Matrix settings</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PersistenceManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Used to initialize quick tests.</div>
</div>
<div class="col-first odd-row-color"><code> </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">PersistenceManager</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color">
<div class="block">Initializes matrix settings component from provided Diagram element</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FilterSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">FilterSettings</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnSettings()">getColumnSettings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column filter settings</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMatrixSettings()">getMatrixSettings</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">General matrix settings</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project of this matrix</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FilterSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">FilterSettings</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowSettings()">getRowSettings</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row filter settings</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMainCriteriaDefined()">isMainCriteriaDefined</a>()</code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>PersistenceManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PersistenceManager</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Initializes matrix settings component from provided Diagram element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - Matrix element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>PersistenceManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">PersistenceManager</span>()</div>
<div class="block">Used to initialize quick tests.</div>
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
<section class="detail" id="getMatrixSettings()">
<h3>getMatrixSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings</a></span> <span class="element-name">getMatrixSettings</span>()</div>
<div class="block">General matrix settings</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>settings for whole dependency matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowSettings()">
<h3>getRowSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FilterSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">FilterSettings</a></span> <span class="element-name">getRowSettings</span>()</div>
<div class="block">Row filter settings</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>settings of the row filter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnSettings()">
<h3>getColumnSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FilterSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">FilterSettings</a></span> <span class="element-name">getColumnSettings</span>()</div>
<div class="block">Column filter settings</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>settings of the column filter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns project of this matrix</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMainCriteriaDefined()">
<h3>isMainCriteriaDefined</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMainCriteriaDefined</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if row element type, row scope, column element type, column scope and dependency criteria
 are all defined in these settings</dd>
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
