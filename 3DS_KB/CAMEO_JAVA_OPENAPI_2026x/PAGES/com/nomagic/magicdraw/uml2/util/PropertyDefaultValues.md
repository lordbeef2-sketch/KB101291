# JAVA OPENAPI: PropertyDefaultValues (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml2/util/PropertyDefaultValues.html
- source_path: `com/nomagic/magicdraw/uml2/util/PropertyDefaultValues.html`
- source_sha256: `a34a80138413fb1657b3e360d6d979b07d6eedc34dce270d21bfa79d3d5480e1`
- captured_utc: `2026-07-14T16:58:33.741242+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Interface PropertyDefaultValues

public interfacePropertyDefaultValues

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[getDefaultValues](#getDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)`
Used to return collection of default values to be set for property
`boolean`
`[isValid](#isValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)`
Check if property needs to have multiple default values

============ METHOD DETAIL ========== 
Method Details
isValid
boolean isValid([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)
Check if property needs to have multiple default values
Parameters:
`property` - to check
Returns:
true if property is valid for multiple default values
getDefaultValues
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> getDefaultValues([Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)
Used to return collection of default values to be set for property
Parameters:
`property` - to set default values for
Returns:
collection of default values to be set for property

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Interface PropertyDefaultValues">Interface PropertyDefaultValues</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PropertyDefaultValues</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getDefaultValues</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Used to return collection of default values to be set for property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isValid</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if property needs to have multiple default values</div>
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
<section class="detail" id="isValid(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isValid</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isValid</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Check if property needs to have multiple default values</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - to check</dd>
<dt>Returns:</dt>
<dd>true if property is valid for multiple default values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getDefaultValues</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getDefaultValues</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Used to return collection of default values to be set for property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - to set default values for</dd>
<dt>Returns:</dt>
<dd>collection of default values to be set for property</dd>
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
