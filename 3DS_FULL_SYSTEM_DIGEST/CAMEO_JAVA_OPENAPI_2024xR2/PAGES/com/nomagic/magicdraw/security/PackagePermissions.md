# JAVA OPENAPI: PackagePermissions (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/security/PackagePermissions.html
- source_path: `com/nomagic/magicdraw/security/PackagePermissions.html`
- source_sha256: `5dba8dd70ff092f6847b3ba45e7e6dabeaae0f0c4592fb8398cfa585cef673a4`
- captured_utc: `2026-07-14T16:55:27.533146+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface PackagePermissions

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `com.nomagic.esi.api.EsiObject`, `org.eclipse.emf.common.notify.Notifier`

public interfacePackagePermissionsextends com.nomagic.esi.api.EsiObject

begin-user-doc 
 A representation of the model object '***Package Permissions***'.
 end-user-doc 
The following features are supported:
[`*Access Permissions*`](#getAccessPermissions())
[`*Use Parent Permissions*`](#isUseParentPermissions())

See Also:
[`SecurityPackage.getPackagePermissions()`](SecurityPackage.html#getPackagePermissions())
Model:
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.util.EList<[PackageAccessPermission](PackageAccessPermission.html)>`
`[getAccessPermissions](#getAccessPermissions())()`
Returns the value of the '***Access Permissions***' containment reference list.
`boolean`
`[isDefaultState](#isDefaultState())()`
Returns true if all values are default.
`boolean`
`[isSame](#isSame(com.nomagic.magicdraw.security.PackagePermissions))([PackagePermissions](PackagePermissions.html) other)`

`boolean`
`[isUseParentPermissions](#isUseParentPermissions())()`
Returns the value of the '***Use Parent Permissions***' attribute.
`void`
`[setUseParentPermissions](#setUseParentPermissions(boolean))(boolean value)`
Sets the value of the '[`*Use Parent Permissions*`](#isUseParentPermissions())' attribute.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.esi.api.EsiObject
`esiID, esiState`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getAccessPermissions
org.eclipse.emf.common.util.EList<[PackageAccessPermission](PackageAccessPermission.html)> getAccessPermissions()
Returns the value of the '***Access Permissions***' containment reference list.
 The list contents are of type [`PackageAccessPermission`](PackageAccessPermission.html).
 begin-user-doc 
If the meaning of the '*Access Permissions*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Access Permissions*' containment reference list.
See Also:
[`SecurityPackage.getPackagePermissions_AccessPermissions()`](SecurityPackage.html#getPackagePermissions_AccessPermissions())
Model:
containment="true" resolveProxies="true"
Generated:
isUseParentPermissions
boolean isUseParentPermissions()
Returns the value of the '***Use Parent Permissions***' attribute.
 The default value is `"true"`.
 begin-user-doc 
If the meaning of the '*Use Parent Permissions*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Use Parent Permissions*' attribute.
See Also:
[`setUseParentPermissions(boolean)`](#setUseParentPermissions(boolean))
[`SecurityPackage.getPackagePermissions_UseParentPermissions()`](SecurityPackage.html#getPackagePermissions_UseParentPermissions())
Model:
default="true"
Generated:
setUseParentPermissions
void setUseParentPermissions(boolean value)
Sets the value of the '[`*Use Parent Permissions*`](#isUseParentPermissions())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Use Parent Permissions*' attribute.
See Also:
[`isUseParentPermissions()`](#isUseParentPermissions())
Generated:
isSame
boolean isSame([PackagePermissions](PackagePermissions.html) other)
begin-user-doc 
 end-user-doc
Model:
Generated:
isDefaultState
boolean isDefaultState()
Returns true if all values are default.
Returns:
true if all values are default, otherwise - false
Generated:
NOT

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.security</a></div>
<h1 class="title" title="Interface PackagePermissions">Interface PackagePermissions</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>com.nomagic.esi.api.EsiObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PackagePermissions</span><span class="extends-implements">
extends com.nomagic.esi.api.EsiObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Package Permissions</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 </p>
<ul>
<li><a href="#getAccessPermissions()"><code><em>Access Permissions</em></code></a></li>
<li><a href="#isUseParentPermissions()"><code><em>Use Parent Permissions</em></code></a></li>
</ul></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SecurityPackage.html#getPackagePermissions()"><code>SecurityPackage.getPackagePermissions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList&lt;<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAccessPermissions()">getAccessPermissions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Access Permissions</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDefaultState()">isDefaultState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true if all values are default.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSame(com.nomagic.magicdraw.security.PackagePermissions)">isSame</a><wbr/>(<a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a> other)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"></div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUseParentPermissions()">isUseParentPermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Use Parent Permissions</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUseParentPermissions(boolean)">setUseParentPermissions</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isUseParentPermissions()"><code><em>Use Parent Permissions</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.esi.api.EsiObject">Methods inherited from interface com.nomagic.esi.api.EsiObject</h3>
<code>esiID, esiState</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
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
<section class="detail" id="getAccessPermissions()">
<h3>getAccessPermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a>&gt;</span> <span class="element-name">getAccessPermissions</span>()</div>
<div class="block">Returns the value of the '<em><b>Access Permissions</b></em>' containment reference list.
 The list contents are of type <a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>PackageAccessPermission</code></a>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Access Permissions</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Access Permissions</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SecurityPackage.html#getPackagePermissions_AccessPermissions()"><code>SecurityPackage.getPackagePermissions_AccessPermissions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseParentPermissions()">
<h3>isUseParentPermissions</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isUseParentPermissions</span>()</div>
<div class="block">Returns the value of the '<em><b>Use Parent Permissions</b></em>' attribute.
 The default value is <code>"true"</code>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Use Parent Permissions</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Use Parent Permissions</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUseParentPermissions(boolean)"><code>setUseParentPermissions(boolean)</code></a></li>
<li><a href="SecurityPackage.html#getPackagePermissions_UseParentPermissions()"><code>SecurityPackage.getPackagePermissions_UseParentPermissions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseParentPermissions(boolean)">
<h3>setUseParentPermissions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUseParentPermissions</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isUseParentPermissions()"><code><em>Use Parent Permissions</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Use Parent Permissions</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isUseParentPermissions()"><code>isUseParentPermissions()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSame(com.nomagic.magicdraw.security.PackagePermissions)">
<h3>isSame</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSame</span><wbr/><span class="parameters">(<a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a> other)</span></div>
<div class="block"><!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDefaultState()">
<h3>isDefaultState</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDefaultState</span>()</div>
<div class="block">Returns true if all values are default.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if all values are default, otherwise - false</dd>
<dt>Generated:</dt>
<dd>NOT</dd>
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
