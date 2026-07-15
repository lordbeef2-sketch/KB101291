# JAVA OPENAPI: SecurityFactory (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/security/SecurityFactory.html
- source_path: `com/nomagic/magicdraw/security/SecurityFactory.html`
- source_sha256: `83943d24e2cf1b9c635e38b6f7b200838b71d88e27b6ff9ad3c13a265873ccda`
- captured_utc: `2026-07-14T16:58:01.260573+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface SecurityFactory

All Superinterfaces:
`org.eclipse.emf.ecore.EFactory`, `org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceSecurityFactoryextends org.eclipse.emf.ecore.EFactory

begin-user-doc 
 The **Factory** for the model.
 It provides a create method for each non-abstract class of the model.
 end-user-doc

See Also:
[`SecurityPackage`](SecurityPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [SecurityFactory](SecurityFactory.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the factory.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[EveryonePrincipal](EveryonePrincipal.html)`
`[createEveryonePrincipal](#createEveryonePrincipal())()`
Returns a new object of class '*Everyone Principal*'.
`[GroupPrincipal](GroupPrincipal.html)`
`[createGroupPrincipal](#createGroupPrincipal())()`
Returns a new object of class '*Group Principal*'.
`[PackageAccessPermission](PackageAccessPermission.html)`
`[createPackageAccessPermission](#createPackageAccessPermission())()`
Returns a new object of class '*Package Access Permission*'.
`[PackagePermissions](PackagePermissions.html)`
`[createPackagePermissions](#createPackagePermissions())()`
Returns a new object of class '*Package Permissions*'.
`[ProjectSecurity](ProjectSecurity.html)`
`[createProjectSecurity](#createProjectSecurity())()`
Returns a new object of class '*Project Security*'.
`[RolePrincipal](RolePrincipal.html)`
`[createRolePrincipal](#createRolePrincipal())()`
Returns a new object of class '*Role Principal*'.
`[UserPrincipal](UserPrincipal.html)`
`[createUserPrincipal](#createUserPrincipal())()`
Returns a new object of class '*User Principal*'.
`[SecurityPackage](SecurityPackage.html)`
`[getSecurityPackage](#getSecurityPackage())()`
Returns the package supported by this factory.
Methods inherited from interface org.eclipse.emf.ecore.EFactory
`convertToString, create, createFromString, getEPackage, setEPackage`
Methods inherited from interface org.eclipse.emf.ecore.EModelElement
`getEAnnotation, getEAnnotations`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ FIELD DETAIL =========== 
Field Details
eINSTANCE
static final [SecurityFactory](SecurityFactory.html) eINSTANCE
The singleton instance of the factory.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
createProjectSecurity
[ProjectSecurity](ProjectSecurity.html) createProjectSecurity()
Returns a new object of class '*Project Security*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Project Security*'.
Generated:
createPackageAccessPermission
[PackageAccessPermission](PackageAccessPermission.html) createPackageAccessPermission()
Returns a new object of class '*Package Access Permission*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Package Access Permission*'.
Generated:
createPackagePermissions
[PackagePermissions](PackagePermissions.html) createPackagePermissions()
Returns a new object of class '*Package Permissions*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Package Permissions*'.
Generated:
createUserPrincipal
[UserPrincipal](UserPrincipal.html) createUserPrincipal()
Returns a new object of class '*User Principal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*User Principal*'.
Generated:
createGroupPrincipal
[GroupPrincipal](GroupPrincipal.html) createGroupPrincipal()
Returns a new object of class '*Group Principal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Group Principal*'.
Generated:
createRolePrincipal
[RolePrincipal](RolePrincipal.html) createRolePrincipal()
Returns a new object of class '*Role Principal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Role Principal*'.
Generated:
createEveryonePrincipal
[EveryonePrincipal](EveryonePrincipal.html) createEveryonePrincipal()
Returns a new object of class '*Everyone Principal*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*Everyone Principal*'.
Generated:
getSecurityPackage
[SecurityPackage](SecurityPackage.html) getSecurityPackage()
Returns the package supported by this factory.
 begin-user-doc 
 end-user-doc
Returns:
the package supported by this factory.
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.security</a></div>
<h1 class="title" title="Interface SecurityFactory">Interface SecurityFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EFactory</code>, <code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">SecurityFactory</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EFactory</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Factory</b> for the model.
 It provides a create method for each non-abstract class of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="SecurityPackage.html" title="interface in com.nomagic.magicdraw.security"><code>SecurityPackage</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="SecurityFactory.html" title="interface in com.nomagic.magicdraw.security">SecurityFactory</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eINSTANCE">eINSTANCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The singleton instance of the factory.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security">EveryonePrincipal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEveryonePrincipal()">createEveryonePrincipal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Everyone Principal</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security">GroupPrincipal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createGroupPrincipal()">createGroupPrincipal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Group Principal</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPackageAccessPermission()">createPackageAccessPermission</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Package Access Permission</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createPackagePermissions()">createPackagePermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Package Permissions</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProjectSecurity.html" title="interface in com.nomagic.magicdraw.security">ProjectSecurity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProjectSecurity()">createProjectSecurity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Project Security</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security">RolePrincipal</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createRolePrincipal()">createRolePrincipal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>Role Principal</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security">UserPrincipal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createUserPrincipal()">createUserPrincipal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>User Principal</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="SecurityPackage.html" title="interface in com.nomagic.magicdraw.security">SecurityPackage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSecurityPackage()">getSecurityPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the package supported by this factory.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EFactory">Methods inherited from interface org.eclipse.emf.ecore.EFactory</h3>
<code>convertToString, create, createFromString, getEPackage, setEPackage</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EModelElement">Methods inherited from interface org.eclipse.emf.ecore.EModelElement</h3>
<code>getEAnnotation, getEAnnotations</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="eINSTANCE">
<h3>eINSTANCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="SecurityFactory.html" title="interface in com.nomagic.magicdraw.security">SecurityFactory</a></span> <span class="element-name">eINSTANCE</span></div>
<div class="block">The singleton instance of the factory.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="createProjectSecurity()">
<h3>createProjectSecurity</h3>
<div class="member-signature"><span class="return-type"><a href="ProjectSecurity.html" title="interface in com.nomagic.magicdraw.security">ProjectSecurity</a></span> <span class="element-name">createProjectSecurity</span>()</div>
<div class="block">Returns a new object of class '<em>Project Security</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Project Security</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageAccessPermission()">
<h3>createPackageAccessPermission</h3>
<div class="member-signature"><span class="return-type"><a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a></span> <span class="element-name">createPackageAccessPermission</span>()</div>
<div class="block">Returns a new object of class '<em>Package Access Permission</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package Access Permission</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackagePermissions()">
<h3>createPackagePermissions</h3>
<div class="member-signature"><span class="return-type"><a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a></span> <span class="element-name">createPackagePermissions</span>()</div>
<div class="block">Returns a new object of class '<em>Package Permissions</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Package Permissions</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUserPrincipal()">
<h3>createUserPrincipal</h3>
<div class="member-signature"><span class="return-type"><a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security">UserPrincipal</a></span> <span class="element-name">createUserPrincipal</span>()</div>
<div class="block">Returns a new object of class '<em>User Principal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>User Principal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createGroupPrincipal()">
<h3>createGroupPrincipal</h3>
<div class="member-signature"><span class="return-type"><a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security">GroupPrincipal</a></span> <span class="element-name">createGroupPrincipal</span>()</div>
<div class="block">Returns a new object of class '<em>Group Principal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Group Principal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRolePrincipal()">
<h3>createRolePrincipal</h3>
<div class="member-signature"><span class="return-type"><a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security">RolePrincipal</a></span> <span class="element-name">createRolePrincipal</span>()</div>
<div class="block">Returns a new object of class '<em>Role Principal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Role Principal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEveryonePrincipal()">
<h3>createEveryonePrincipal</h3>
<div class="member-signature"><span class="return-type"><a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security">EveryonePrincipal</a></span> <span class="element-name">createEveryonePrincipal</span>()</div>
<div class="block">Returns a new object of class '<em>Everyone Principal</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>Everyone Principal</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecurityPackage()">
<h3>getSecurityPackage</h3>
<div class="member-signature"><span class="return-type"><a href="SecurityPackage.html" title="interface in com.nomagic.magicdraw.security">SecurityPackage</a></span> <span class="element-name">getSecurityPackage</span>()</div>
<div class="block">Returns the package supported by this factory.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the package supported by this factory.</dd>
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
