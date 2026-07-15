# JAVA OPENAPI: SmartEventSupport (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/jmi/smartlistener/SmartEventSupport.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartEventSupport.html`
- source_sha256: `585d4777e696b41491bcc3d53a1406965c95a8e8a24f8876a11bc8193e5ae71e`
- captured_utc: `2026-07-14T16:46:22.959106+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Interface SmartEventSupport

@OpenApipublic interfaceSmartEventSupport
Defines an interface form registering smart listeners.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[register](#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration))([Registration](Registration.html) registration)`
Registers smart listener configurations to the specified type objects.
`void`
`[unregister](#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration))([Registration](Registration.html) registration)`
Unregisters smart listener configurations from the specified type of objects.

============ METHOD DETAIL ========== 
Method Details
register
@OpenApivoid register([Registration](Registration.html) registration)
Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.
Parameters:
`registration` - registration object.
unregister
@OpenApivoid unregister([Registration](Registration.html) registration)
Unregisters smart listener configurations from the specified type of objects.
Parameters:
`registration` - registration.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Interface SmartEventSupport">Interface SmartEventSupport</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SmartEventSupport</span></div>
<div class="block">Defines an interface form registering smart listeners.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">register</a><wbr/>(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers smart listener configurations to the specified type objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">unregister</a><wbr/>(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unregisters smart listener configurations from the specified type of objects.</div>
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
<section class="detail" id="register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">
<h3>register</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</span></div>
<div class="block">Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>registration</code> - registration object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">
<h3>unregister</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">unregister</span><wbr/><span class="parameters">(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</span></div>
<div class="block">Unregisters smart listener configurations from the specified type of objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>registration</code> - registration.</dd>
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
