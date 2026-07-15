# JAVA OPENAPI: ProjectAbstractRepositoryInitializer (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/jmi/reflect/ProjectAbstractRepositoryInitializer.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/ProjectAbstractRepositoryInitializer.html`
- source_sha256: `b6af26a9a01ced80b700451ada4c842b83067c32dd9319b7c997a68d3bcb571f`
- captured_utc: `2026-07-14T16:52:38.993238+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class ProjectAbstractRepositoryInitializer<P extends com.dassault_systemes.modeler.foundation.project.ModelElementProject>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.RepositoryInitializer<P,[AbstractRepository](AbstractRepository.html)>
com.nomagic.uml2.ext.jmi.reflect.ProjectAbstractRepositoryInitializer<P>

All Implemented Interfaces:
`[Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<com.dassault_systemes.modeler.foundation.project.ModelElementProject>`

public abstract classProjectAbstractRepositoryInitializer<P extends com.dassault_systemes.modeler.foundation.project.ModelElementProject>
extends com.dassault_systemes.modeler.foundation.project.RepositoryInitializer<P,[AbstractRepository](AbstractRepository.html)>

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ProjectAbstractRepositoryInitializer](#%3Cinit%3E(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [P](ProjectAbstractRepositoryInitializer.html)> projectType)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected final com.dassault_systemes.modeler.foundation.transaction.TransactionManager`
`[createTransactionManager](#createTransactionManager(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository))([AbstractRepository](AbstractRepository.html) repository)`

`protected final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [AbstractRepository](AbstractRepository.html)>`
`[getRepositoryType](#getRepositoryType(P))([P](ProjectAbstractRepositoryInitializer.html) project)`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.RepositoryInitializer
`accept, createRepository`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.function.[Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)
`[andThen](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html#andThen(java.util.function.Consumer))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectAbstractRepositoryInitializer
protected ProjectAbstractRepositoryInitializer([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [P](ProjectAbstractRepositoryInitializer.html)> projectType)
 ============ METHOD DETAIL ========== 
Method Details
getRepositoryType
protected final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [AbstractRepository](AbstractRepository.html)> getRepositoryType([P](ProjectAbstractRepositoryInitializer.html) project)
Specified by:
`getRepositoryType` in class `com.dassault_systemes.modeler.foundation.project.RepositoryInitializer<[P](ProjectAbstractRepositoryInitializer.html) extends com.dassault_systemes.modeler.foundation.project.ModelElementProject,[AbstractRepository](AbstractRepository.html)>`
createTransactionManager
protected final com.dassault_systemes.modeler.foundation.transaction.TransactionManager createTransactionManager([AbstractRepository](AbstractRepository.html) repository)
Specified by:
`createTransactionManager` in class `com.dassault_systemes.modeler.foundation.project.RepositoryInitializer<[P](ProjectAbstractRepositoryInitializer.html) extends com.dassault_systemes.modeler.foundation.project.ModelElementProject,[AbstractRepository](AbstractRepository.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class ProjectAbstractRepositoryInitializer">Class ProjectAbstractRepositoryInitializer&lt;P extends com.dassault_systemes.modeler.foundation.project.ModelElementProject&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.RepositoryInitializer&lt;P,<wbr/><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.ProjectAbstractRepositoryInitializer&lt;P&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;com.dassault_systemes.modeler.foundation.project.ModelElementProject&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ProjectAbstractRepositoryInitializer&lt;P extends com.dassault_systemes.modeler.foundation.project.ModelElementProject&gt;</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.project.RepositoryInitializer&lt;P,<wbr/><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;</span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class)">ProjectAbstractRepositoryInitializer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a>&gt; projectType)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final com.dassault_systemes.modeler.foundation.transaction.TransactionManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTransactionManager(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">createTransactionManager</a><wbr/>(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepositoryType(P)">getRepositoryType</a><wbr/>(<a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.RepositoryInitializer">Methods inherited from class com.dassault_systemes.modeler.foundation.project.RepositoryInitializer</h3>
<code>accept, createRepository</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.function.Consumer">Methods inherited from interface java.util.function.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html#andThen(java.util.function.Consumer)" title="class or interface in java.util.function">andThen</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class)">
<h3>ProjectAbstractRepositoryInitializer</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ProjectAbstractRepositoryInitializer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a>&gt; projectType)</span></div>
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
<section class="detail" id="getRepositoryType(P)">
<h3 id="getRepositoryType(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getRepositoryType</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;</span> <span class="element-name">getRepositoryType</span><wbr/><span class="parameters">(<a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a> project)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getRepositoryType</code> in class <code>com.dassault_systemes.modeler.foundation.project.RepositoryInitializer&lt;<a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a> extends com.dassault_systemes.modeler.foundation.project.ModelElementProject,<wbr/><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTransactionManager(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">
<h3>createTransactionManager</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">com.dassault_systemes.modeler.foundation.transaction.TransactionManager</span> <span class="element-name">createTransactionManager</span><wbr/><span class="parameters">(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>createTransactionManager</code> in class <code>com.dassault_systemes.modeler.foundation.project.RepositoryInitializer&lt;<a href="ProjectAbstractRepositoryInitializer.html" title="type parameter in ProjectAbstractRepositoryInitializer">P</a> extends com.dassault_systemes.modeler.foundation.project.ModelElementProject,<wbr/><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a>&gt;</code></dd>
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
