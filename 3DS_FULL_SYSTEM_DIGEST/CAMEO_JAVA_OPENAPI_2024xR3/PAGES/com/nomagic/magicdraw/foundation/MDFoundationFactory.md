# JAVA OPENAPI: MDFoundationFactory (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/foundation/MDFoundationFactory.html
- source_path: `com/nomagic/magicdraw/foundation/MDFoundationFactory.html`
- source_sha256: `86baedf15ad3b61f530edd46efc9b06c1dd92cedfd7b4242e79a870db2d9f0c7`
- captured_utc: `2026-07-14T16:55:21.796081+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation](package-summary.html)

## Interface MDFoundationFactory

All Superinterfaces:
`org.eclipse.emf.ecore.EFactory`, `org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceMDFoundationFactoryextends org.eclipse.emf.ecore.EFactory

begin-user-doc 
 The **Factory** for the model.
 It provides a create method for each non-abstract class of the model.
 end-user-doc

See Also:
[`MDFoundationPackage`](MDFoundationPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [MDFoundationFactory](MDFoundationFactory.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the factory.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[MDExtension](MDExtension.html)`
`[createMDExtension](#createMDExtension())()`
Returns a new object of class '*MD Extension*'.
`[MDFoundationPackage](MDFoundationPackage.html)`
`[getMDFoundationPackage](#getMDFoundationPackage())()`
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
static final [MDFoundationFactory](MDFoundationFactory.html) eINSTANCE
The singleton instance of the factory.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
createMDExtension
[MDExtension](MDExtension.html) createMDExtension()
Returns a new object of class '*MD Extension*'.
 begin-user-doc 
 end-user-doc
Returns:
a new object of class '*MD Extension*'.
Generated:
getMDFoundationPackage
[MDFoundationPackage](MDFoundationPackage.html) getMDFoundationPackage()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation</a></div>
<h1 class="title" title="Interface MDFoundationFactory">Interface MDFoundationFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EFactory</code>, <code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MDFoundationFactory</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EFactory</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Factory</b> for the model.
 It provides a create method for each non-abstract class of the model.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MDFoundationPackage.html" title="interface in com.nomagic.magicdraw.foundation"><code>MDFoundationPackage</code></a></li>
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
<div class="col-first even-row-color"><code>static final <a href="MDFoundationFactory.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationFactory</a></code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createMDExtension()">createMDExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a new object of class '<em>MD Extension</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDFoundationPackage.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationPackage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDFoundationPackage()">getMDFoundationPackage</a>()</code></div>
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
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="MDFoundationFactory.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationFactory</a></span> <span class="element-name">eINSTANCE</span></div>
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
<section class="detail" id="createMDExtension()">
<h3>createMDExtension</h3>
<div class="member-signature"><span class="return-type"><a href="MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></span> <span class="element-name">createMDExtension</span>()</div>
<div class="block">Returns a new object of class '<em>MD Extension</em>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new object of class '<em>MD Extension</em>'.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDFoundationPackage()">
<h3>getMDFoundationPackage</h3>
<div class="member-signature"><span class="return-type"><a href="MDFoundationPackage.html" title="interface in com.nomagic.magicdraw.foundation">MDFoundationPackage</a></span> <span class="element-name">getMDFoundationPackage</span>()</div>
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
