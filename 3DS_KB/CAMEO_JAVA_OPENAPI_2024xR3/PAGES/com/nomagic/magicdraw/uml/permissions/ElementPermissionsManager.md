# JAVA OPENAPI: ElementPermissionsManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/permissions/ElementPermissionsManager.html
- source_path: `com/nomagic/magicdraw/uml/permissions/ElementPermissionsManager.html`
- source_sha256: `66785da5ac6bac1320037eb89fa806c240758a7a8907a1d22f3e6bd4a36ed6fe`
- captured_utc: `2026-07-14T16:55:55.535460+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.permissions](package-summary.html)

## Class ElementPermissionsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.permissions.ElementPermissionsManager

@OpenApipublic final classElementPermissionsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class responsible for managing permissions of @[`BaseElement`](../BaseElement.html) : readonly, can add children.
 This manager does not contain any logic, external [`ElementPermissions`](ElementPermissions.html) should be registered to handle permissions.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addPermisionsHandler](#addPermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions))([ElementPermissions](ElementPermissions.html) permissions)`
Deprecated.
spelling error.
`void`
`[addPermissionsHandler](#addPermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions))([ElementPermissions](ElementPermissions.html) permissions)`
Register custom permission handler
`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element,
 [BaseElement](../BaseElement.html) child)`
Checks if child can be added into a given element.
`boolean`
`[canCreateChildIn](#canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Checks if child can be created in a given element.
`boolean`
`[canDelete](#canDelete(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Checks is element can be deleted.
`static [ElementPermissionsManager](ElementPermissionsManager.html)`
`[getElementPermissionsManager](#getElementPermissionsManager())()`
Singleton getter
`boolean`
`[isElementEditable](#isElementEditable(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Checks if an element is editable
`boolean`
`[isElementEditableNoCacheCheck](#isElementEditableNoCacheCheck(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Forces isElementEditable check without a cache.
`void`
`[removePermisionsHandler](#removePermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions))([ElementPermissions](ElementPermissions.html) permissions)`
Deprecated.
spelling error.
`void`
`[removePermissionsHandler](#removePermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions))([ElementPermissions](ElementPermissions.html) permissions)`
Unregister custom permission handler
`static void`
`[runWithCacheEnabled](#runWithCacheEnabled(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)`
Enable cache and run runnable, then cache enabling flag is restored.
`static <T> T`
`[supplyWithCacheEnabled](#supplyWithCacheEnabled(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> supplier)`
Enable cache and call supplier, then cache's enabling flag is restored.
`static <T> T`
`[supplyWithEditionElementPermissionsDisabled](#supplyWithEditionElementPermissionsDisabled(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> supplier)`
Disable usage of `EditionElementPermissions` and supply a value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getElementPermissionsManager
@OpenApipublic static [ElementPermissionsManager](ElementPermissionsManager.html) getElementPermissionsManager()
Singleton getter
Returns:
instance
addPermisionsHandler
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void addPermisionsHandler([ElementPermissions](ElementPermissions.html) permissions)
Deprecated.
spelling error. Use #addPermissionsHandler
Register custom permission handler
Parameters:
`permissions` - permissions handler
addPermissionsHandler
@OpenApipublic void addPermissionsHandler([ElementPermissions](ElementPermissions.html) permissions)
Register custom permission handler
Parameters:
`permissions` - permissions handler
removePermisionsHandler
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void removePermisionsHandler([ElementPermissions](ElementPermissions.html) permissions)
Deprecated.
spelling error. Use #removePermissionsHandler
Unregister custom permission handler
Parameters:
`permissions` - permissions handler
removePermissionsHandler
@OpenApipublic void removePermissionsHandler([ElementPermissions](ElementPermissions.html) permissions)
Unregister custom permission handler
Parameters:
`permissions` - permissions handler
isElementEditable
public boolean isElementEditable([BaseElement](../BaseElement.html) element)
Checks if an element is editable
Parameters:
`element` - element
Returns:
true if editable
isElementEditableNoCacheCheck
public boolean isElementEditableNoCacheCheck([BaseElement](../BaseElement.html) element)
Forces isElementEditable check without a cache.
 Does not clear or update cache if one is in use.
 To be used with element permission handlers that can become disabled.
Parameters:
`element` - element to check
Returns:
returns true if element is editable
canCreateChildIn
public boolean canCreateChildIn([BaseElement](../BaseElement.html) element)
Checks if child can be created in a given element.
Parameters:
`element` - element
Returns:
true if can
canDelete
public boolean canDelete([BaseElement](../BaseElement.html) element)
Checks is element can be deleted.
Parameters:
`element` - element
Returns:
true if can
canAddChild
public boolean canAddChild([BaseElement](../BaseElement.html) element,
 [BaseElement](../BaseElement.html) child)
Checks if child can be added into a given element.
Parameters:
`element` - element
`child` - child of an element
Returns:
true if can
runWithCacheEnabled
public static void runWithCacheEnabled([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)
Enable cache and run runnable, then cache enabling flag is restored.
Parameters:
`runnable` - runnable to run
supplyWithCacheEnabled
public static <T> T supplyWithCacheEnabled([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> supplier)
Enable cache and call supplier, then cache's enabling flag is restored.
Parameters:
`supplier` - supplier
supplyWithEditionElementPermissionsDisabled
public static <T> T supplyWithEditionElementPermissionsDisabled([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> supplier)
Disable usage of `EditionElementPermissions` and supply a value.
Parameters:
`supplier` - supplier

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.permissions</a></div>
<h1 class="title" title="Class ElementPermissionsManager">Class ElementPermissionsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.permissions.ElementPermissionsManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ElementPermissionsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class responsible for managing permissions of @<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml"><code>BaseElement</code></a> : readonly, can add children.
 This manager does not contain any logic, external <a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions"><code>ElementPermissions</code></a> should be registered to handle permissions.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addPermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">addPermisionsHandler</a><wbr/>(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">addPermissionsHandler</a><wbr/>(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register custom permission handler</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if child can be added into a given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement)">canCreateChildIn</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if child can be created in a given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDelete(com.nomagic.magicdraw.uml.BaseElement)">canDelete</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks is element can be deleted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementPermissionsManager.html" title="class in com.nomagic.magicdraw.uml.permissions">ElementPermissionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementPermissionsManager()">getElementPermissionsManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Singleton getter</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementEditable(com.nomagic.magicdraw.uml.BaseElement)">isElementEditable</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if an element is editable</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementEditableNoCacheCheck(com.nomagic.magicdraw.uml.BaseElement)">isElementEditableNoCacheCheck</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Forces isElementEditable check without a cache.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removePermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">removePermisionsHandler</a><wbr/>(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">removePermissionsHandler</a><wbr/>(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister custom permission handler</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runWithCacheEnabled(java.lang.Runnable)">runWithCacheEnabled</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Enable cache and run runnable, then cache enabling flag is restored.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#supplyWithCacheEnabled(java.util.function.Supplier)">supplyWithCacheEnabled</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; supplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Enable cache and call supplier, then cache's enabling flag is restored.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#supplyWithEditionElementPermissionsDisabled(java.util.function.Supplier)">supplyWithEditionElementPermissionsDisabled</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disable usage of <code>EditionElementPermissions</code> and supply a value.</div>
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
<section class="detail" id="getElementPermissionsManager()">
<h3>getElementPermissionsManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementPermissionsManager.html" title="class in com.nomagic.magicdraw.uml.permissions">ElementPermissionsManager</a></span> <span class="element-name">getElementPermissionsManager</span>()</div>
<div class="block">Singleton getter</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">
<h3>addPermisionsHandler</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPermisionsHandler</span><wbr/><span class="parameters">(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error. Use #addPermissionsHandler</div>
</div>
<div class="block">Register custom permission handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>permissions</code> - permissions handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">
<h3>addPermissionsHandler</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPermissionsHandler</span><wbr/><span class="parameters">(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</span></div>
<div class="block">Register custom permission handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>permissions</code> - permissions handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePermisionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">
<h3>removePermisionsHandler</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePermisionsHandler</span><wbr/><span class="parameters">(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error. Use #removePermissionsHandler</div>
</div>
<div class="block">Unregister custom permission handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>permissions</code> - permissions handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePermissionsHandler(com.nomagic.magicdraw.uml.permissions.ElementPermissions)">
<h3>removePermissionsHandler</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePermissionsHandler</span><wbr/><span class="parameters">(<a href="ElementPermissions.html" title="interface in com.nomagic.magicdraw.uml.permissions">ElementPermissions</a> permissions)</span></div>
<div class="block">Unregister custom permission handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>permissions</code> - permissions handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementEditable(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isElementEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementEditable</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if an element is editable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementEditableNoCacheCheck(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isElementEditableNoCacheCheck</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isElementEditableNoCacheCheck</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Forces isElementEditable check without a cache.
 Does not clear or update cache if one is in use.
 To be used with element permission handlers that can become disabled.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>returns true if element is editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canCreateChildIn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canCreateChildIn</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if child can be created in a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if can</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDelete(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDelete</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks is element can be deleted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if can</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</span></div>
<div class="block">Checks if child can be added into a given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>child</code> - child of an element</dd>
<dt>Returns:</dt>
<dd>true if can</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runWithCacheEnabled(java.lang.Runnable)">
<h3>runWithCacheEnabled</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">runWithCacheEnabled</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Enable cache and run runnable, then cache enabling flag is restored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnable to run</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supplyWithCacheEnabled(java.util.function.Supplier)">
<h3>supplyWithCacheEnabled</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">supplyWithCacheEnabled</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; supplier)</span></div>
<div class="block">Enable cache and call supplier, then cache's enabling flag is restored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>supplier</code> - supplier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supplyWithEditionElementPermissionsDisabled(java.util.function.Supplier)">
<h3>supplyWithEditionElementPermissionsDisabled</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">supplyWithEditionElementPermissionsDisabled</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; supplier)</span></div>
<div class="block">Disable usage of <code>EditionElementPermissions</code> and supply a value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>supplier</code> - supplier</dd>
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
