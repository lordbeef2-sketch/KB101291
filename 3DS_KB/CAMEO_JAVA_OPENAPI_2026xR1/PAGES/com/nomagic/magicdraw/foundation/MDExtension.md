# JAVA OPENAPI: MDExtension (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/foundation/MDExtension.html
- source_path: `com/nomagic/magicdraw/foundation/MDExtension.html`
- source_sha256: `6752eaf513f3191fbdc8d97b80a535ad90aea56bc9c27a4d7d8d16fde6ffbef6`
- captured_utc: `2026-07-14T16:45:36.399488+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation](package-summary.html)

## Interface MDExtension

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceMDExtensionextends org.eclipse.emf.ecore.EObject

begin-user-doc 
 A representation of the model object '***MD Extension***'.
 end-user-doc 
 begin-model-doc 
 Defines an extension to the model.
 end-model-doc 
The following features are supported:
 [`*Source*`](#getSource())
[`*Contents*`](#getContents())
[`*References*`](#getReferences())
[`*Element*`](#getElement())
[`*Details*`](#getDetails())

See Also:
[`MDFoundationPackage.getMDExtension()`](MDFoundationPackage.html#getMDExtension())
Model:
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject>`
`[getContents](#getContents())()`
Returns the value of the '***Contents***' containment reference list.
`org.eclipse.emf.common.util.EMap<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getDetails](#getDetails())()`
Returns the value of the '***Details***' map.
`[MDObject](MDObject.html)`
`[getElement](#getElement())()`
Returns the value of the '***Element***' container reference.
`org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject>`
`[getReferences](#getReferences())()`
Returns the value of the '***References***' reference list.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSource](#getSource())()`
Returns the value of the '***Source***' attribute.
`void`
`[setElement](#setElement(com.nomagic.magicdraw.foundation.MDObject))([MDObject](MDObject.html) value)`
Sets the value of the '[`*Element*`](#getElement())' container reference.
`void`
`[setSource](#setSource(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Source*`](#getSource())' attribute.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getSource
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSource()
Returns the value of the '***Source***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This will typically be a full URI representing the type of the extension.
 end-model-doc
Returns:
the value of the '*Source*' attribute.
See Also:
[`setSource(String)`](#setSource(java.lang.String))
[`MDFoundationPackage.getMDExtension_Source()`](MDFoundationPackage.html#getMDExtension_Source())
Model:
Generated:
setSource
void setSource([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Source*`](#getSource())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Source*' attribute.
See Also:
[`getSource()`](#getSource())
Generated:
getContents
org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject> getContents()
Returns the value of the '***Contents***' containment reference list.
 The list contents are of type `EObject`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This represents arbitrary contained objects.
 end-model-doc
Returns:
the value of the '*Contents*' containment reference list.
See Also:
[`MDFoundationPackage.getMDExtension_Contents()`](MDFoundationPackage.html#getMDExtension_Contents())
Model:
containment="true" resolveProxies="true"
Generated:
getReferences
org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject> getReferences()
Returns the value of the '***References***' reference list.
 The list contents are of type `EObject`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This represents arbitrary referenced objects.
 end-model-doc
Returns:
the value of the '*References*' reference list.
See Also:
[`MDFoundationPackage.getMDExtension_References()`](MDFoundationPackage.html#getMDExtension_References())
Model:
Generated:
getElement
[MDObject](MDObject.html) getElement()
Returns the value of the '***Element***' container reference.
 It is bidirectional and its opposite is '[`*Md Extensions*`](MDObject.html#getMdExtensions())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The element that owns this extension.
 end-model-doc
Returns:
the value of the '*Element*' container reference.
See Also:
[`setElement(MDObject)`](#setElement(com.nomagic.magicdraw.foundation.MDObject))
[`MDFoundationPackage.getMDExtension_Element()`](MDFoundationPackage.html#getMDExtension_Element())
[`MDObject.getMdExtensions()`](MDObject.html#getMdExtensions())
Model:
opposite="mdExtensions" transient="false"
Generated:
setElement
void setElement([MDObject](MDObject.html) value)
Sets the value of the '[`*Element*`](#getElement())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Element*' container reference.
See Also:
[`getElement()`](#getElement())
Generated:
getDetails
org.eclipse.emf.common.util.EMap<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getDetails()
Returns the value of the '***Details***' map.
 The key is of type [`String`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),
 and the value is of type [`String`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 This represents tagged values.
 end-model-doc
Returns:
the value of the '*Details*' map.
See Also:
[`MDFoundationPackage.getMDExtension_Details()`](MDFoundationPackage.html#getMDExtension_Details())
Model:
mapType="com.nomagic.magicdraw.foundation.StringToStringMapEntryinvalid input: '<'org.eclipse.emf.ecore.EString, org.eclipse.emf.ecore.EString>"
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation</a></div>
<h1 class="title" title="Interface MDExtension">Interface MDExtension</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MDExtension</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>MD Extension</b></em>'.
 <!-- end-user-doc -->
<!-- begin-model-doc -->
 Defines an extension to the model.
 <!-- end-model-doc -->
<p>
 The following features are supported:
 <ul>
<li><a href="#getSource()"><code><em>Source</em></code></a></li>
<li><a href="#getContents()"><code><em>Contents</em></code></a></li>
<li><a href="#getReferences()"><code><em>References</em></code></a></li>
<li><a href="#getElement()"><code><em>Element</em></code></a></li>
<li><a href="#getDetails()"><code><em>Details</em></code></a></li>
</ul>
</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MDFoundationPackage.html#getMDExtension()"><code>MDFoundationPackage.getMDExtension()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList<wbr/>&lt;org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContents()">getContents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Contents</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EMap<wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDetails()">getDetails</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Details</b></em>' map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Element</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList<wbr/>&lt;org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReferences()">getReferences</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>References</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Source</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setElement(com.nomagic.magicdraw.foundation.MDObject)">setElement</a><wbr/>(<a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getElement()"><code><em>Element</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSource(java.lang.String)">setSource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSource</span>()</div>
<div class="block">Returns the value of the '<em><b>Source</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This will typically be a full URI representing the type of the extension.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Source</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSource(java.lang.String)"><code>setSource(String)</code></a></li>
<li><a href="MDFoundationPackage.html#getMDExtension_Source()"><code>MDFoundationPackage.getMDExtension_Source()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSource(java.lang.String)">
<h3>setSource</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Source</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSource()"><code>getSource()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContents()">
<h3>getContents</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getContents</span>()</div>
<div class="block">Returns the value of the '<em><b>Contents</b></em>' containment reference list.
 The list contents are of type <code>EObject</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This represents arbitrary contained objects.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Contents</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MDFoundationPackage.html#getMDExtension_Contents()"><code>MDFoundationPackage.getMDExtension_Contents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferences()">
<h3>getReferences</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getReferences</span>()</div>
<div class="block">Returns the value of the '<em><b>References</b></em>' reference list.
 The list contents are of type <code>EObject</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This represents arbitrary referenced objects.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>References</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MDFoundationPackage.html#getMDExtension_References()"><code>MDFoundationPackage.getMDExtension_References()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="return-type"><a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Element</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="MDObject.html#getMdExtensions()"><code><em>Md Extensions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The element that owns this extension.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Element</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setElement(com.nomagic.magicdraw.foundation.MDObject)"><code>setElement(MDObject)</code></a></li>
<li><a href="MDFoundationPackage.html#getMDExtension_Element()"><code>MDFoundationPackage.getMDExtension_Element()</code></a></li>
<li><a href="MDObject.html#getMdExtensions()"><code>MDObject.getMdExtensions()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="mdExtensions" transient="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElement(com.nomagic.magicdraw.foundation.MDObject)">
<h3>setElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setElement</span><wbr/><span class="parameters">(<a href="MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getElement()"><code><em>Element</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Element</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getElement()"><code>getElement()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDetails()">
<h3>getDetails</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EMap&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDetails</span>()</div>
<div class="block">Returns the value of the '<em><b>Details</b></em>' map.
 The key is of type <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang"><code>String</code></a>,
 and the value is of type <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang"><code>String</code></a>,
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 This represents tagged values.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Details</em>' map.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MDFoundationPackage.html#getMDExtension_Details()"><code>MDFoundationPackage.getMDExtension_Details()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>mapType="com.nomagic.magicdraw.foundation.StringToStringMapEntry<span class="invalid-tag">invalid input: '&lt;'</span>org.eclipse.emf.ecore.EString, org.eclipse.emf.ecore.EString&gt;"</dd>
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
