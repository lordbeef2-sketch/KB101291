# JAVA OPENAPI: EnvironmentOptions.EnvironmentChangeListener (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/options/EnvironmentOptions.EnvironmentChangeListener.html
- source_path: `com/nomagic/magicdraw/core/options/EnvironmentOptions.EnvironmentChangeListener.html`
- source_sha256: `fac93ed282cf6b2b3c7dfdeee40f98e06be30567929fcc20c807526f7b54c90e`
- captured_utc: `2026-07-14T16:55:11.904975+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Interface EnvironmentOptions.EnvironmentChangeListener

All Known Implementing Classes:
`[MainFrame](../../ui/MainFrame.html)`

Enclosing class:
[EnvironmentOptions](EnvironmentOptions.html)

@OpenApiAllpublic static interfaceEnvironmentOptions.EnvironmentChangeListener

Receives events when environment options change
 in the environment options dialog after "Ok" is pressed.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[updateByEnvironmentProperties](#updateByEnvironmentProperties(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> properties)`
Event comes when environment options change.

============ METHOD DETAIL ========== 
Method Details
updateByEnvironmentProperties
void updateByEnvironmentProperties([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> properties)
Event comes when environment options change.
Parameters:
`properties` - properties which have changed. Properties have previous values. You need to take new values from Environment Options.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Interface EnvironmentOptions.EnvironmentChangeListener">Interface EnvironmentOptions.EnvironmentChangeListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options">EnvironmentOptions</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">EnvironmentOptions.EnvironmentChangeListener</span></div>
<div class="block">Receives events when environment options change
 in the environment options dialog after "Ok" is pressed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateByEnvironmentProperties(java.util.List)">updateByEnvironmentProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Event comes when environment options change.</div>
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
<section class="detail" id="updateByEnvironmentProperties(java.util.List)">
<h3>updateByEnvironmentProperties</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">updateByEnvironmentProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Event comes when environment options change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - properties which have changed. Properties have previous values. You need to take new values from Environment Options.</dd>
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
