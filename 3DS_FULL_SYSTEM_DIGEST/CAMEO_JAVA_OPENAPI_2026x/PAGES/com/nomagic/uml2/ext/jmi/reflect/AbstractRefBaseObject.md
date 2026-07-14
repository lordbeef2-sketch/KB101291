# JAVA OPENAPI: AbstractRefBaseObject (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/jmi/reflect/AbstractRefBaseObject.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/AbstractRefBaseObject.html`
- source_sha256: `8c6e0e73aec7f99071283478ed1c86811242529764061231cbc0ec1037080fbe`
- captured_utc: `2026-07-14T16:58:46.753395+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Interface AbstractRefBaseObject

All Superinterfaces:
`com.nomagic.uml2.ext.jmi.MapOwner`, `javax.jmi.reflect.RefBaseObject`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`

All Known Implementing Classes:
`com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation`, `com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl`, `[AbstractRefPackage](AbstractRefPackage.html)`, `[AbstractRepository](AbstractRepository.html)`, `[EcoreRefAssociation](EcoreRefAssociation.html)`, `[EcoreRefPackage](EcoreRefPackage.html)`

public interfaceAbstractRefBaseObjectextends javax.jmi.reflect.RefBaseObject, com.nomagic.uml2.ext.jmi.MapOwner, com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AbstractRepository](AbstractRepository.html)`
`[getRepository](#getRepository())()`
Get repository.
`[AbstractRepository](AbstractRepository.html)`
`[mof_getRepository](#mof_getRepository())()`

`void`
`[setMofID](#setMofID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) mofID)`

`void`
`[setOwner](#setOwner(com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage))([AbstractRefPackage](AbstractRefPackage.html) pack)`

`void`
`[setRepository](#setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository))([AbstractRepository](AbstractRepository.html) repository)`
Methods inherited from interface com.nomagic.uml2.ext.jmi.MapOwner
`mapClear, mapPut, mapPutAll, mapRemove`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`

============ METHOD DETAIL ========== 
Method Details
setRepository
void setRepository([AbstractRepository](AbstractRepository.html) repository)
mof_getRepository
[AbstractRepository](AbstractRepository.html) mof_getRepository()
getRepository
[AbstractRepository](AbstractRepository.html) getRepository()
Description copied from interface: `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Get repository.
Specified by:
`getRepository` in interface `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Returns:
repository.
setMofID
void setMofID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) mofID)
setOwner
void setOwner([AbstractRefPackage](AbstractRefPackage.html) pack)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Interface AbstractRefBaseObject">Interface AbstractRefBaseObject</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.nomagic.uml2.ext.jmi.MapOwner</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation</code>, <code>com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</code>, <code><a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></code>, <code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code>, <code><a href="EcoreRefAssociation.html" title="class in com.nomagic.uml2.ext.jmi.reflect">EcoreRefAssociation</a></code>, <code><a href="EcoreRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">EcoreRefPackage</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">AbstractRefBaseObject</span><span class="extends-implements">
extends javax.jmi.reflect.RefBaseObject, com.nomagic.uml2.ext.jmi.MapOwner, com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepository()">getRepository</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get repository.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#mof_getRepository()">mof_getRepository</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMofID(java.lang.String)">setMofID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mofID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwner(com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage)">setOwner</a><wbr/>(<a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a> pack)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">setRepository</a><wbr/>(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.MapOwner">Methods inherited from interface com.nomagic.uml2.ext.jmi.MapOwner</h3>
<code>mapClear, mapPut, mapPutAll, mapRemove</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
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
<section class="detail" id="setRepository(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository)">
<h3>setRepository</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRepository</span><wbr/><span class="parameters">(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository)</span></div>
</section>
</li>
<li>
<section class="detail" id="mof_getRepository()">
<h3>mof_getRepository</h3>
<div class="member-signature"><span class="return-type"><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></span> <span class="element-name">mof_getRepository</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRepository()">
<h3>getRepository</h3>
<div class="member-signature"><span class="return-type"><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></span> <span class="element-name">getRepository</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></span></div>
<div class="block">Get repository.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getRepository</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></dd>
<dt>Returns:</dt>
<dd>repository.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMofID(java.lang.String)">
<h3>setMofID</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMofID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mofID)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOwner(com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage)">
<h3>setOwner</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwner</span><wbr/><span class="parameters">(<a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a> pack)</span></div>
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
