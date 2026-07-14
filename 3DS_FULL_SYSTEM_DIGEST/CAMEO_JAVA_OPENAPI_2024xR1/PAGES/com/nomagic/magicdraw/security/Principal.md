# JAVA OPENAPI: Principal (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/security/Principal.html
- source_path: `com/nomagic/magicdraw/security/Principal.html`
- source_sha256: `13daca13059e14339b6befc0e0e9b474654b45bb06de64d73529867ce5b2b24f`
- captured_utc: `2026-07-14T16:51:28.648302+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface Principal

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `com.nomagic.esi.api.EsiObject`, `org.eclipse.emf.common.notify.Notifier`

All Known Subinterfaces:
`[EveryonePrincipal](EveryonePrincipal.html)`, `[GroupPrincipal](GroupPrincipal.html)`, `[RolePrincipal](RolePrincipal.html)`, `[UserPrincipal](UserPrincipal.html)`

public interfacePrincipalextends com.nomagic.esi.api.EsiObject

begin-user-doc 
 A representation of the model object '***Principal***'.
 end-user-doc 
The following features are supported:
[`*Name*`](#getName())
[`*Package Permissions*`](#getPackagePermissions())

See Also:
[`SecurityPackage.getPrincipal()`](SecurityPackage.html#getPrincipal())
Model:
abstract="true"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns the value of the '***Name***' attribute.
`org.eclipse.emf.common.util.EList<[PackageAccessPermission](PackageAccessPermission.html)>`
`[getPackagePermissions](#getPackagePermissions())()`
Returns the value of the '***Package Permissions***' reference list.
`boolean`
`[isSame](#isSame(com.nomagic.magicdraw.security.Principal))([Principal](Principal.html) other)`

`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Name*`](#getName())' attribute.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.esi.api.EsiObject
`esiID, esiState`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns the value of the '***Name***' attribute.
 begin-user-doc 
If the meaning of the '*Name*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Name*' attribute.
See Also:
[`setName(String)`](#setName(java.lang.String))
[`SecurityPackage.getPrincipal_Name()`](SecurityPackage.html#getPrincipal_Name())
Model:
Generated:
setName
void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Name*`](#getName())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Name*' attribute.
See Also:
[`getName()`](#getName())
Generated:
getPackagePermissions
org.eclipse.emf.common.util.EList<[PackageAccessPermission](PackageAccessPermission.html)> getPackagePermissions()
Returns the value of the '***Package Permissions***' reference list.
 The list contents are of type [`PackageAccessPermission`](PackageAccessPermission.html).
 It is bidirectional and its opposite is '[`*Principal*`](PackageAccessPermission.html#getPrincipal())'.
 begin-user-doc 
If the meaning of the '*Package Permissions*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Package Permissions*' reference list.
See Also:
[`SecurityPackage.getPrincipal_PackagePermissions()`](SecurityPackage.html#getPrincipal_PackagePermissions())
[`PackageAccessPermission.getPrincipal()`](PackageAccessPermission.html#getPrincipal())
Model:
opposite="principal"
Generated:
isSame
boolean isSame([Principal](Principal.html) other)
begin-user-doc 
 end-user-doc
Model:
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.security</a></div>
<h1 class="title" title="Interface Principal">Interface Principal</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>com.nomagic.esi.api.EsiObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security">EveryonePrincipal</a></code>, <code><a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security">GroupPrincipal</a></code>, <code><a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security">RolePrincipal</a></code>, <code><a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security">UserPrincipal</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Principal</span><span class="extends-implements">
extends com.nomagic.esi.api.EsiObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Principal</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 </p>
<ul>
<li><a href="#getName()"><code><em>Name</em></code></a></li>
<li><a href="#getPackagePermissions()"><code><em>Package Permissions</em></code></a></li>
</ul></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="SecurityPackage.html#getPrincipal()"><code>SecurityPackage.getPrincipal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"</dd>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList&lt;<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions()">getPackagePermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSame(com.nomagic.magicdraw.security.Principal)">isSame</a><wbr/>(<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a> other)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"></div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getName()"><code><em>Name</em></code></a>' attribute.</div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns the value of the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Name</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setName(java.lang.String)"><code>setName(String)</code></a></li>
<li><a href="SecurityPackage.html#getPrincipal_Name()"><code>SecurityPackage.getPrincipal_Name()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getName()"><code><em>Name</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getName()"><code>getName()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagePermissions()">
<h3>getPackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a>&gt;</span> <span class="element-name">getPackagePermissions</span>()</div>
<div class="block">Returns the value of the '<em><b>Package Permissions</b></em>' reference list.
 The list contents are of type <a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>PackageAccessPermission</code></a>.
 It is bidirectional and its opposite is '<a href="PackageAccessPermission.html#getPrincipal()"><code><em>Principal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Package Permissions</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Package Permissions</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SecurityPackage.html#getPrincipal_PackagePermissions()"><code>SecurityPackage.getPrincipal_PackagePermissions()</code></a></li>
<li><a href="PackageAccessPermission.html#getPrincipal()"><code>PackageAccessPermission.getPrincipal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="principal"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSame(com.nomagic.magicdraw.security.Principal)">
<h3>isSame</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSame</span><wbr/><span class="parameters">(<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a> other)</span></div>
<div class="block"><!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Model:</dt>
<dt>Generated:</dt>
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
