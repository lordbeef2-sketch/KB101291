# JAVA OPENAPI: ProjectSecurity (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/security/ProjectSecurity.html
- source_path: `com/nomagic/magicdraw/security/ProjectSecurity.html`
- source_sha256: `67cc757e7ac4762b1a475b336cceba87798de129351cd0b4ba6f181b74de8693`
- captured_utc: `2026-07-14T16:45:40.451539+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface ProjectSecurity

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `com.nomagic.esi.api.EsiObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceProjectSecurityextends com.nomagic.esi.api.EsiObject

begin-user-doc 
 A representation of the model object '***Project Security***'.
 end-user-doc 
The following features are supported:
[`*Package Permissions*`](#getPackagePermissions())
[`*Principals*`](#getPrincipals())

See Also:
[`SecurityPackage.getProjectSecurity()`](SecurityPackage.html#getProjectSecurity())
Model:
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.util.EMap<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[PackagePermissions](PackagePermissions.html)>`
`[getPackagePermissions](#getPackagePermissions())()`
Returns the value of the '***Package Permissions***' map.
`org.eclipse.emf.common.util.EList<[Principal](Principal.html)>`
`[getPrincipals](#getPrincipals())()`
Returns the value of the '***Principals***' containment reference list.
`boolean`
`[isEmpty](#isEmpty())()`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.esi.api.EsiObject
`esiID, esiState`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getPackagePermissions
org.eclipse.emf.common.util.EMap<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[PackagePermissions](PackagePermissions.html)> getPackagePermissions()
Returns the value of the '***Package Permissions***' map.
 The key is of type [`String`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),
 and the value is of type [`PackagePermissions`](PackagePermissions.html),
 begin-user-doc 
If the meaning of the '*Package Permissions*' map isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Package Permissions*' map.
See Also:
[`SecurityPackage.getProjectSecurity_PackagePermissions()`](SecurityPackage.html#getProjectSecurity_PackagePermissions())
Model:
mapType="com.nomagic.magicdraw.security.StringToPackagePermissionsMapinvalid input: '<'org.eclipse.emf.ecore.EString, com.nomagic.magicdraw.security.PackagePermissions>"
Generated:
getPrincipals
org.eclipse.emf.common.util.EList<[Principal](Principal.html)> getPrincipals()
Returns the value of the '***Principals***' containment reference list.
 The list contents are of type [`Principal`](Principal.html).
 begin-user-doc 
If the meaning of the '*Principals*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Principals*' containment reference list.
See Also:
[`SecurityPackage.getProjectSecurity_Principals()`](SecurityPackage.html#getProjectSecurity_Principals())
Model:
containment="true" resolveProxies="true"
Generated:
isEmpty
boolean isEmpty()
begin-user-doc 
 end-user-doc
Model:
kind="operation"
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.security</a></div>
<h1 class="title" title="Interface ProjectSecurity">Interface ProjectSecurity</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>com.nomagic.esi.api.EsiObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectSecurity</span><span class="extends-implements">
extends com.nomagic.esi.api.EsiObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Project Security</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 </p>
<ul>
<li><a href="#getPackagePermissions()"><code><em>Package Permissions</em></code></a></li>
<li><a href="#getPrincipals()"><code><em>Principals</em></code></a></li>
</ul></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SecurityPackage.html#getProjectSecurity()"><code>SecurityPackage.getProjectSecurity()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EMap<wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions()">getPackagePermissions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Package Permissions</b></em>' map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList<wbr/>&lt;<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipals()">getPrincipals</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Principals</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"></div>
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
<section class="detail" id="getPackagePermissions()">
<h3>getPackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EMap&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a>&gt;</span> <span class="element-name">getPackagePermissions</span>()</div>
<div class="block">Returns the value of the '<em><b>Package Permissions</b></em>' map.
 The key is of type <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang"><code>String</code></a>,
 and the value is of type <a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security"><code>PackagePermissions</code></a>,
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Package Permissions</em>' map isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Package Permissions</em>' map.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SecurityPackage.html#getProjectSecurity_PackagePermissions()"><code>SecurityPackage.getProjectSecurity_PackagePermissions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>mapType="com.nomagic.magicdraw.security.StringToPackagePermissionsMap<span class="invalid-tag">invalid input: '&lt;'</span>org.eclipse.emf.ecore.EString, com.nomagic.magicdraw.security.PackagePermissions&gt;"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipals()">
<h3>getPrincipals</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a>&gt;</span> <span class="element-name">getPrincipals</span>()</div>
<div class="block">Returns the value of the '<em><b>Principals</b></em>' containment reference list.
 The list contents are of type <a href="Principal.html" title="interface in com.nomagic.magicdraw.security"><code>Principal</code></a>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Principals</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Principals</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SecurityPackage.html#getProjectSecurity_Principals()"><code>SecurityPackage.getProjectSecurity_Principals()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<div class="block"><!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Model:</dt>
<dd>kind="operation"</dd>
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
