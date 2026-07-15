# JAVA OPENAPI: PackageAccessPermission (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/security/PackageAccessPermission.html
- source_path: `com/nomagic/magicdraw/security/PackageAccessPermission.html`
- source_sha256: `8de59d048475a66fdff5a72cf1c2c675808a0fc207965f3c9e1c22669f8b3c44`
- captured_utc: `2026-07-14T16:55:30.355177+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface PackageAccessPermission

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `com.nomagic.esi.api.EsiObject`, `org.eclipse.emf.common.notify.Notifier`

public interfacePackageAccessPermissionextends com.nomagic.esi.api.EsiObject

begin-user-doc 
 A representation of the model object '***Package Access Permission***'.
 end-user-doc 
The following features are supported:
[`*Action*`](#getAction())
[`*Application*`](#getApplication())
[`*Principal*`](#getPrincipal())

See Also:
[`SecurityPackage.getPackageAccessPermission()`](SecurityPackage.html#getPackageAccessPermission())
Model:
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Action](Action.html)`
`[getAction](#getAction())()`
Returns the value of the '***Action***' attribute.
`[Application](Application.html)`
`[getApplication](#getApplication())()`
Returns the value of the '***Application***' attribute.
`[Principal](Principal.html)`
`[getPrincipal](#getPrincipal())()`
Returns the value of the '***Principal***' reference.
`boolean`
`[isSame](#isSame(com.nomagic.magicdraw.security.PackageAccessPermission))([PackageAccessPermission](PackageAccessPermission.html) other)`

`void`
`[setAction](#setAction(com.nomagic.magicdraw.security.Action))([Action](Action.html) value)`
Sets the value of the '[`*Action*`](#getAction())' attribute.
`void`
`[setApplication](#setApplication(com.nomagic.magicdraw.security.Application))([Application](Application.html) value)`
Sets the value of the '[`*Application*`](#getApplication())' attribute.
`void`
`[setPrincipal](#setPrincipal(com.nomagic.magicdraw.security.Principal))([Principal](Principal.html) value)`
Sets the value of the '[`*Principal*`](#getPrincipal())' reference.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.esi.api.EsiObject
`esiID, esiState`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getAction
[Action](Action.html) getAction()
Returns the value of the '***Action***' attribute.
 The literals are from the enumeration [`Action`](Action.html).
 begin-user-doc 
If the meaning of the '*Action*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Action*' attribute.
See Also:
[`Action`](Action.html)
[`setAction(Action)`](#setAction(com.nomagic.magicdraw.security.Action))
[`SecurityPackage.getPackageAccessPermission_Action()`](SecurityPackage.html#getPackageAccessPermission_Action())
Model:
Generated:
setAction
void setAction([Action](Action.html) value)
Sets the value of the '[`*Action*`](#getAction())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Action*' attribute.
See Also:
[`Action`](Action.html)
[`getAction()`](#getAction())
Generated:
getApplication
[Application](Application.html) getApplication()
Returns the value of the '***Application***' attribute.
 The literals are from the enumeration [`Application`](Application.html).
 begin-user-doc 
If the meaning of the '*Application*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Application*' attribute.
See Also:
[`Application`](Application.html)
[`setApplication(Application)`](#setApplication(com.nomagic.magicdraw.security.Application))
[`SecurityPackage.getPackageAccessPermission_Application()`](SecurityPackage.html#getPackageAccessPermission_Application())
Model:
Generated:
setApplication
void setApplication([Application](Application.html) value)
Sets the value of the '[`*Application*`](#getApplication())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Application*' attribute.
See Also:
[`Application`](Application.html)
[`getApplication()`](#getApplication())
Generated:
getPrincipal
[Principal](Principal.html) getPrincipal()
Returns the value of the '***Principal***' reference.
 It is bidirectional and its opposite is '[`*Package Permissions*`](Principal.html#getPackagePermissions())'.
 begin-user-doc 
If the meaning of the '*Principal*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Principal*' reference.
See Also:
[`setPrincipal(Principal)`](#setPrincipal(com.nomagic.magicdraw.security.Principal))
[`SecurityPackage.getPackageAccessPermission_Principal()`](SecurityPackage.html#getPackageAccessPermission_Principal())
[`Principal.getPackagePermissions()`](Principal.html#getPackagePermissions())
Model:
opposite="packagePermissions"
Generated:
setPrincipal
void setPrincipal([Principal](Principal.html) value)
Sets the value of the '[`*Principal*`](#getPrincipal())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Principal*' reference.
See Also:
[`getPrincipal()`](#getPrincipal())
Generated:
isSame
boolean isSame([PackageAccessPermission](PackageAccessPermission.html) other)
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
<h1 class="title" title="Interface PackageAccessPermission">Interface PackageAccessPermission</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>com.nomagic.esi.api.EsiObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PackageAccessPermission</span><span class="extends-implements">
extends com.nomagic.esi.api.EsiObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Package Access Permission</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 </p>
<ul>
<li><a href="#getAction()"><code><em>Action</em></code></a></li>
<li><a href="#getApplication()"><code><em>Application</em></code></a></li>
<li><a href="#getPrincipal()"><code><em>Principal</em></code></a></li>
</ul></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SecurityPackage.html#getPackageAccessPermission()"><code>SecurityPackage.getPackageAccessPermission()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Action.html" title="enum class in com.nomagic.magicdraw.security">Action</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAction()">getAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Action</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Application.html" title="enum class in com.nomagic.magicdraw.security">Application</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getApplication()">getApplication</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Application</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal()">getPrincipal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Principal</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSame(com.nomagic.magicdraw.security.PackageAccessPermission)">isSame</a><wbr/>(<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a> other)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"></div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAction(com.nomagic.magicdraw.security.Action)">setAction</a><wbr/>(<a href="Action.html" title="enum class in com.nomagic.magicdraw.security">Action</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAction()"><code><em>Action</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setApplication(com.nomagic.magicdraw.security.Application)">setApplication</a><wbr/>(<a href="Application.html" title="enum class in com.nomagic.magicdraw.security">Application</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getApplication()"><code><em>Application</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPrincipal(com.nomagic.magicdraw.security.Principal)">setPrincipal</a><wbr/>(<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getPrincipal()"><code><em>Principal</em></code></a>' reference.</div>
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
<section class="detail" id="getAction()">
<h3>getAction</h3>
<div class="member-signature"><span class="return-type"><a href="Action.html" title="enum class in com.nomagic.magicdraw.security">Action</a></span> <span class="element-name">getAction</span>()</div>
<div class="block">Returns the value of the '<em><b>Action</b></em>' attribute.
 The literals are from the enumeration <a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code>Action</code></a>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Action</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Action</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code>Action</code></a></li>
<li><a href="#setAction(com.nomagic.magicdraw.security.Action)"><code>setAction(Action)</code></a></li>
<li><a href="SecurityPackage.html#getPackageAccessPermission_Action()"><code>SecurityPackage.getPackageAccessPermission_Action()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAction(com.nomagic.magicdraw.security.Action)">
<h3>setAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAction</span><wbr/><span class="parameters">(<a href="Action.html" title="enum class in com.nomagic.magicdraw.security">Action</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAction()"><code><em>Action</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Action</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code>Action</code></a></li>
<li><a href="#getAction()"><code>getAction()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplication()">
<h3>getApplication</h3>
<div class="member-signature"><span class="return-type"><a href="Application.html" title="enum class in com.nomagic.magicdraw.security">Application</a></span> <span class="element-name">getApplication</span>()</div>
<div class="block">Returns the value of the '<em><b>Application</b></em>' attribute.
 The literals are from the enumeration <a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code>Application</code></a>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Application</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Application</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code>Application</code></a></li>
<li><a href="#setApplication(com.nomagic.magicdraw.security.Application)"><code>setApplication(Application)</code></a></li>
<li><a href="SecurityPackage.html#getPackageAccessPermission_Application()"><code>SecurityPackage.getPackageAccessPermission_Application()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplication(com.nomagic.magicdraw.security.Application)">
<h3>setApplication</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setApplication</span><wbr/><span class="parameters">(<a href="Application.html" title="enum class in com.nomagic.magicdraw.security">Application</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getApplication()"><code><em>Application</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Application</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code>Application</code></a></li>
<li><a href="#getApplication()"><code>getApplication()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal()">
<h3>getPrincipal</h3>
<div class="member-signature"><span class="return-type"><a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a></span> <span class="element-name">getPrincipal</span>()</div>
<div class="block">Returns the value of the '<em><b>Principal</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Principal.html#getPackagePermissions()"><code><em>Package Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Principal</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Principal</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setPrincipal(com.nomagic.magicdraw.security.Principal)"><code>setPrincipal(Principal)</code></a></li>
<li><a href="SecurityPackage.html#getPackageAccessPermission_Principal()"><code>SecurityPackage.getPackageAccessPermission_Principal()</code></a></li>
<li><a href="Principal.html#getPackagePermissions()"><code>Principal.getPackagePermissions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="packagePermissions"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPrincipal(com.nomagic.magicdraw.security.Principal)">
<h3>setPrincipal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPrincipal</span><wbr/><span class="parameters">(<a href="Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getPrincipal()"><code><em>Principal</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Principal</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getPrincipal()"><code>getPrincipal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSame(com.nomagic.magicdraw.security.PackageAccessPermission)">
<h3>isSame</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSame</span><wbr/><span class="parameters">(<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security">PackageAccessPermission</a> other)</span></div>
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
