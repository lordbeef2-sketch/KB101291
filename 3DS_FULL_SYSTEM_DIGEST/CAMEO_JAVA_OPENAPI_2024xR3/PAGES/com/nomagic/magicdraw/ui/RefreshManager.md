# JAVA OPENAPI: RefreshManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/RefreshManager.html
- source_path: `com/nomagic/magicdraw/ui/RefreshManager.html`
- source_sha256: `0160621e3e58194d54e02b111a0d523e669e675a4cc01f6979939721c9f07fcb`
- captured_utc: `2026-07-14T16:55:50.681403+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class RefreshManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.RefreshManager

@OpenApiAllpublic classRefreshManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Singleton class for registering [`RefreshManager.RefreshParticipant`](RefreshManager.RefreshParticipant.html).

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[RefreshManager.RefreshParticipant](RefreshManager.RefreshParticipant.html)`
Refresh participant
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final void`
`[addRefreshParticipant](#addRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant))([RefreshManager.RefreshParticipant](RefreshManager.RefreshParticipant.html) participant)`
Register participant
`static [RefreshManager](RefreshManager.html)`
`[getInstance](#getInstance())()`

`void`
`[refresh](#refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Call refresh for all registered participants
`final void`
`[removeRefreshParticipant](#removeRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant))([RefreshManager.RefreshParticipant](RefreshManager.RefreshParticipant.html) participant)`
Remove participant
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [RefreshManager](RefreshManager.html) getInstance()
addRefreshParticipant
public final void addRefreshParticipant([RefreshManager.RefreshParticipant](RefreshManager.RefreshParticipant.html) participant)
Register participant
Parameters:
`participant` - participant
removeRefreshParticipant
public final void removeRefreshParticipant([RefreshManager.RefreshParticipant](RefreshManager.RefreshParticipant.html) participant)
Remove participant
Parameters:
`participant` - participant
refresh
public void refresh([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
Call refresh for all registered participants
Parameters:
`project` - project
`progressStatus` - progress status

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class RefreshManager">Class RefreshManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.RefreshManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RefreshManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Singleton class for registering <a href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui"><code>RefreshManager.RefreshParticipant</code></a>.</div>
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
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a></code></div>
<div class="col-last even-row-color">
<div class="block">Refresh participant</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant)">addRefreshParticipant</a><wbr/>(<a href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register participant</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RefreshManager.html" title="class in com.nomagic.magicdraw.ui">RefreshManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus)">refresh</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call refresh for all registered participants</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant)">removeRefreshParticipant</a><wbr/>(<a href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a> participant)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove participant</div>
</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RefreshManager.html" title="class in com.nomagic.magicdraw.ui">RefreshManager</a></span> <span class="element-name">getInstance</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant)">
<h3>addRefreshParticipant</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addRefreshParticipant</span><wbr/><span class="parameters">(<a href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a> participant)</span></div>
<div class="block">Register participant</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - participant</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRefreshParticipant(com.nomagic.magicdraw.ui.RefreshManager.RefreshParticipant)">
<h3>removeRefreshParticipant</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">removeRefreshParticipant</span><wbr/><span class="parameters">(<a href="RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a> participant)</span></div>
<div class="block">Remove participant</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - participant</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus)">
<h3>refresh</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">refresh</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span></div>
<div class="block">Call refresh for all registered participants</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>progressStatus</code> - progress status</dd>
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
