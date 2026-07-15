# JAVA OPENAPI: ProxyManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/core/proxy/ProxyManager.html
- source_path: `com/nomagic/magicdraw/core/proxy/ProxyManager.html`
- source_sha256: `df7afd853a2846bab92cef0035b7516b4bd2151af81f4a5b9a797811ebd5f24f`
- captured_utc: `2026-07-14T16:57:52.860479+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.proxy](package-summary.html)

## Interface ProxyManager

@OpenApiAllpublic interfaceProxyManager
Manager for working with proxy.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`com.nomagic.ci.persistence.IAttachedProject`
`[getModuleWithMissingShare](#getModuleWithMissingShare(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement proxy)`
Return module in which element exists is not shared, and used by module shared part.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getProxies](#getProxies())()`
Returns all registered proxies.
`long`
`[getStateId](#getStateId())()`
Returns state if of proxy manager.
`boolean`
`[isElementProxy](#isElementProxy(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement el)`
Return true if element is proxy.
`boolean`
`[isGhostProxy](#isGhostProxy(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement el)`
returns true if proxy was not resolved by loading module.
`void`
`[makeNotProxy](#makeNotProxy(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Marks element as normal.
`void`
`[markProxy](#markProxy(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Just marks this element as proxy.

============ METHOD DETAIL ========== 
Method Details
isElementProxy
boolean isElementProxy(com.dassault_systemes.modeler.foundation.model.ModelElement el)
Return true if element is proxy. If element is ghost proxy it returns also true.
Parameters:
`el` - element to check
Returns:
true if element is proxy. If element is ghost proxy it returns also true
isGhostProxy
boolean isGhostProxy(com.dassault_systemes.modeler.foundation.model.ModelElement el)
returns true if proxy was not resolved by loading module.
 Method makes sense only when element is proxy.
Parameters:
`el` - element to check
Returns:
true if proxy was not resolved by loading module.
getModuleWithMissingShare
@CheckForNullcom.nomagic.ci.persistence.IAttachedProject getModuleWithMissingShare(com.dassault_systemes.modeler.foundation.model.ModelElement proxy)
Return module in which element exists is not shared, and used by module shared part.
Parameters:
`proxy` - element which is ghost proxy because it is not shared (wrong dependencies on sharing).
Returns:
module which should share this proxy to make it non proxy.
markProxy
void markProxy(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Just marks this element as proxy.
Parameters:
`element` - element to mark as proxy
makeNotProxy
void makeNotProxy(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Marks element as normal.
Parameters:
`element` - element to mark as not proxy
getProxies
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getProxies()
Returns all registered proxies.
Returns:
proxies
getStateId
long getStateId()
Returns state if of proxy manager. Manager state changes if proxies are added or removed.
Returns:
state if

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.proxy</a></div>
<h1 class="title" title="Interface ProxyManager">Interface ProxyManager</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProxyManager</span></div>
<div class="block">Manager for working with proxy.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModuleWithMissingShare(com.dassault_systemes.modeler.foundation.model.ModelElement)">getModuleWithMissingShare</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement proxy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return module in which element exists is not shared, and used by module shared part.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProxies()">getProxies</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all registered proxies.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStateId()">getStateId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns state if of proxy manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isElementProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">isElementProxy</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement el)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return true if element is proxy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isGhostProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">isGhostProxy</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement el)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">returns true if proxy was not resolved by loading module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#makeNotProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">makeNotProxy</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Marks element as normal.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">markProxy</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Just marks this element as proxy.</div>
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
<section class="detail" id="isElementProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>isElementProxy</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isElementProxy</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement el)</span></div>
<div class="block">Return true if element is proxy. If element is ghost proxy it returns also true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>el</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if element is proxy. If element is ghost proxy it returns also true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isGhostProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>isGhostProxy</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isGhostProxy</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement el)</span></div>
<div class="block">returns true if proxy was not resolved by loading module.
 Method makes sense only when element is proxy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>el</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if proxy was not resolved by loading module.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModuleWithMissingShare(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>getModuleWithMissingShare</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">getModuleWithMissingShare</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement proxy)</span></div>
<div class="block">Return module in which element exists is not shared, and used by module shared part.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>proxy</code> - element which is ghost proxy because it is not shared (wrong dependencies on sharing).</dd>
<dt>Returns:</dt>
<dd>module which should share this proxy to make it non proxy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>markProxy</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">markProxy</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Just marks this element as proxy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to mark as proxy</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeNotProxy(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>makeNotProxy</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">makeNotProxy</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Marks element as normal.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to mark as not proxy</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProxies()">
<h3>getProxies</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getProxies</span>()</div>
<div class="block">Returns all registered proxies.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>proxies</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateId()">
<h3>getStateId</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getStateId</span>()</div>
<div class="block">Returns state if of proxy manager. Manager state changes if proxies are added or removed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>state if</dd>
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
