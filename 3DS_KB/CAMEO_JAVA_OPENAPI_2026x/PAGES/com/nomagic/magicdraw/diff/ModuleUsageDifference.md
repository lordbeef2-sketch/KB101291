# JAVA OPENAPI: ModuleUsageDifference (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/diff/ModuleUsageDifference.html
- source_path: `com/nomagic/magicdraw/diff/ModuleUsageDifference.html`
- source_sha256: `79d5c167e9e0e860612c254f97c68b7dc33dad567444b4b188265c7050e200fb`
- captured_utc: `2026-07-14T16:57:54.326495+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ModuleUsageDifference

All Superinterfaces:
`[Difference](Difference.html)`, `[DifferenceLocation](DifferenceLocation.html)`

@OpenApiAllpublic interfaceModuleUsageDifferenceextends [Difference](Difference.html), [DifferenceLocation](DifferenceLocation.html)

Difference when module usage is changed, this can happen when new module is used, module is not
 longer used. Modules mounts mounted in different position. If new module version is used it will
 be find as remove old module and adding new one.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[ModuleUsageDifference.Mount](ModuleUsageDifference.Mount.html)`
Mount info.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AutoLoadKind](../core/modules/AutoLoadKind.html)`
`[getAutoLoadType](#getAutoLoadType())()`

`[ModificationKind](ModificationKind.html)`
`[getModificationKind](#getModificationKind())()`

`[ModuleInfo](ModuleInfo.html)`
`[getModule](#getModule())()`
Get module info.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsageDifference.Mount](ModuleUsageDifference.Mount.html)>`
`[getMounts](#getMounts())()`
Information where packages are mounted.
`[ModuleInfo](ModuleInfo.html)`
`[getParent](#getParent())()`
Parent module info.
`com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getStickyVersion](#getStickyVersion())()`

`boolean`
`[isEditable](#isEditable())()`

`boolean`
`[isLoadIndex](#isLoadIndex())()`

`boolean`
`[isParentEditable](#isParentEditable())()`
Is parent editable
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](DifferenceLocation.html)
`[getModuleURI](DifferenceLocation.html#getModuleURI())`

============ METHOD DETAIL ========== 
Method Details
getModule
[ModuleInfo](ModuleInfo.html) getModule()
Get module info.
Returns:
module info.
isEditable
boolean isEditable()
getAutoLoadType
[AutoLoadKind](../core/modules/AutoLoadKind.html) getAutoLoadType()
Returns:
module load type. Check [`ProjectUtilities.getAutoLoadKind(com.nomagic.ci.persistence.IProject, com.nomagic.ci.persistence.IProject)`](../core/ProjectUtilities.html#getAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject))}
isLoadIndex
boolean isLoadIndex()
Returns:
true if module has load index set to true.
getStickyVersion
@CheckForNullcom.nomagic.ci.persistence.versioning.IVersionDescriptor getStickyVersion()
Returns:
required version.
getModificationKind
[ModificationKind](ModificationKind.html) getModificationKind()
Returns:
modification kind.
getMounts
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsageDifference.Mount](ModuleUsageDifference.Mount.html)> getMounts()
Information where packages are mounted. Mount info contains only properly mount id.
 May be null for remove modification kind.
Returns:
mount info from contributor project.
getParent
@CheckForNull[ModuleInfo](ModuleInfo.html) getParent()
Parent module info. When module is used by other module, but not directly in the project. If
 module is used directly in project parent is null.
Returns:
parent module info.
isParentEditable
boolean isParentEditable()
Is parent editable

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ModuleUsageDifference">Interface ModuleUsageDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModuleUsageDifference</span><span class="extends-implements">
extends <a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a>, <a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></span></div>
<div class="block">Difference when module usage is changed, this can happen when new module is used, module is not
 longer used. Modules mounts mounted in different position. If new module version is used it will
 be find as remove old module and adding new one.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModuleUsageDifference.Mount.html" title="interface in com.nomagic.magicdraw.diff">ModuleUsageDifference.Mount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Mount info.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAutoLoadType()">getAutoLoadType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModificationKind()">getModificationKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModule()">getModule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get module info.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ModuleUsageDifference.Mount.html" title="interface in com.nomagic.magicdraw.diff">ModuleUsageDifference.Mount</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMounts()">getMounts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Information where packages are mounted.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Parent module info.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStickyVersion()">getStickyVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLoadIndex()">isLoadIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isParentEditable()">isParentEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Is parent editable</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
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
<section class="detail" id="getModule()">
<h3>getModule</h3>
<div class="member-signature"><span class="return-type"><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></span> <span class="element-name">getModule</span>()</div>
<div class="block">Get module info.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module info.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutoLoadType()">
<h3>getAutoLoadType</h3>
<div class="member-signature"><span class="return-type"><a href="../core/modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></span> <span class="element-name">getAutoLoadType</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module load type. Check <a href="../core/ProjectUtilities.html#getAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)"><code>ProjectUtilities.getAutoLoadKind(com.nomagic.ci.persistence.IProject, com.nomagic.ci.persistence.IProject)</code></a>}</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoadIndex()">
<h3>isLoadIndex</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLoadIndex</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if module has load index set to true.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStickyVersion()">
<h3>getStickyVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getStickyVersion</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationKind()">
<h3>getModificationKind</h3>
<div class="member-signature"><span class="return-type"><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getModificationKind</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMounts()">
<h3>getMounts</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsageDifference.Mount.html" title="interface in com.nomagic.magicdraw.diff">ModuleUsageDifference.Mount</a>&gt;</span> <span class="element-name">getMounts</span>()</div>
<div class="block">Information where packages are mounted. Mount info contains only properly mount id.
 May be null for remove modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>mount info from contributor project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></span> <span class="element-name">getParent</span>()</div>
<div class="block">Parent module info. When module is used by other module, but not directly in the project. If
 module is used directly in project parent is null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent module info.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentEditable()">
<h3>isParentEditable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isParentEditable</span>()</div>
<div class="block">Is parent editable</div>
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
