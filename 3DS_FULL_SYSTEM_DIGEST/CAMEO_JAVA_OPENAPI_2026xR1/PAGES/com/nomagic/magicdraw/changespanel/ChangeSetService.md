# JAVA OPENAPI: ChangeSetService (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/changespanel/ChangeSetService.html
- source_path: `com/nomagic/magicdraw/changespanel/ChangeSetService.html`
- source_sha256: `3687c230e1948b66a720fa0c51bcbdbab6252d687e4626bc3e70698b25deffbe`
- captured_utc: `2026-07-14T16:45:28.460380+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.changespanel](package-summary.html)

## Interface ChangeSetService

@OpenApiAllpublic interfaceChangeSetService
Service to get information about Change Sets tab content.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static enum`
`[ChangeSetService.ChangeSetState](ChangeSetService.ChangeSetState.html)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getActiveChangeSet](#getActiveChangeSet())()`
Gets active change set and returns its name.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ChangeSetRepresentation](ChangeSetRepresentation.html)>`
`[getChangeSetContent](#getChangeSetContent(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)`
Returns collection of specific change set content.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getChangeSetNames](#getChangeSetNames())()`
Gets all change sets names displayed in Change Set tab.
`[ChangeSetService.ChangeSetState](ChangeSetService.ChangeSetState.html)`
`[getChangeSetState](#getChangeSetState(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)`
Returns the state of specific change set which could be "Active" or "Suspended".
`boolean`
`[isSetTagOnCommit](#isSetTagOnCommit(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)`
Checks if 'Tag version with Change ID after commit' is selected.

============ METHOD DETAIL ========== 
Method Details
getChangeSetNames
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getChangeSetNames()
Gets all change sets names displayed in Change Set tab.
Returns:
collection of change sets names
getChangeSetContent
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ChangeSetRepresentation](ChangeSetRepresentation.html)> getChangeSetContent([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Returns collection of specific change set content. Each item in collection represents hierarchical change set tab row.
Parameters:
`changeSetName` - change set name
Returns:
change set hierarchical content
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - in case of incorrect or not existing change set name was passed.
getChangeSetState
[ChangeSetService.ChangeSetState](ChangeSetService.ChangeSetState.html) getChangeSetState([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Returns the state of specific change set which could be "Active" or "Suspended".
Parameters:
`changeSetName` - change set name
Returns:
change set state
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - in case of incorrect or not existing change set name was passed.
getActiveChangeSet
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getActiveChangeSet()
Gets active change set and returns its name.
Returns:
change set name
isSetTagOnCommit
boolean isSetTagOnCommit([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) changeSetName)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Checks if 'Tag version with Change ID after commit' is selected.
 If true - change set name will be set as 'Version Tag' after commit.
Parameters:
`changeSetName` - change set name
Returns:
`true` if 'Tag version with Change ID after commit' is selected, otherwise `false`
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - in case of incorrect or not existing change set name was passed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.changespanel</a></div>
<h1 class="title" title="Interface ChangeSetService">Interface ChangeSetService</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ChangeSetService</span></div>
<div class="block">Service to get information about Change Sets tab content.</div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ChangeSetService.ChangeSetState.html" title="enum class in com.nomagic.magicdraw.changespanel">ChangeSetService.ChangeSetState</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActiveChangeSet()">getActiveChangeSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets active change set and returns its name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ChangeSetRepresentation.html" title="class in com.nomagic.magicdraw.changespanel">ChangeSetRepresentation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangeSetContent(java.lang.String)">getChangeSetContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns collection of specific change set content.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangeSetNames()">getChangeSetNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets all change sets names displayed in Change Set tab.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ChangeSetService.ChangeSetState.html" title="enum class in com.nomagic.magicdraw.changespanel">ChangeSetService.ChangeSetState</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangeSetState(java.lang.String)">getChangeSetState</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the state of specific change set which could be "Active" or "Suspended".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSetTagOnCommit(java.lang.String)">isSetTagOnCommit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if 'Tag version with Change ID after commit' is selected.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="getChangeSetNames()">
<h3>getChangeSetNames</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getChangeSetNames</span>()</div>
<div class="block">Gets all change sets names displayed in Change Set tab.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of change sets names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeSetContent(java.lang.String)">
<h3>getChangeSetContent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ChangeSetRepresentation.html" title="class in com.nomagic.magicdraw.changespanel">ChangeSetRepresentation</a>&gt;</span> <span class="element-name">getChangeSetContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</span>
                                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Returns collection of specific change set content. Each item in collection represents hierarchical change set tab row.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changeSetName</code> - change set name</dd>
<dt>Returns:</dt>
<dd>change set hierarchical content</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - in case of incorrect or not existing change set name was passed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeSetState(java.lang.String)">
<h3>getChangeSetState</h3>
<div class="member-signature"><span class="return-type"><a href="ChangeSetService.ChangeSetState.html" title="enum class in com.nomagic.magicdraw.changespanel">ChangeSetService.ChangeSetState</a></span> <span class="element-name">getChangeSetState</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</span>
                                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Returns the state of specific change set which could be "Active" or "Suspended".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changeSetName</code> - change set name</dd>
<dt>Returns:</dt>
<dd>change set state</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - in case of incorrect or not existing change set name was passed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveChangeSet()">
<h3>getActiveChangeSet</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getActiveChangeSet</span>()</div>
<div class="block">Gets active change set and returns its name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>change set name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSetTagOnCommit(java.lang.String)">
<h3>isSetTagOnCommit</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSetTagOnCommit</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> changeSetName)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Checks if 'Tag version with Change ID after commit' is selected.
 If true - change set name will be set as 'Version Tag' after commit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changeSetName</code> - change set name</dd>
<dt>Returns:</dt>
<dd><code>true</code> if 'Tag version with Change ID after commit' is selected, otherwise <code>false</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - in case of incorrect or not existing change set name was passed.</dd>
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
