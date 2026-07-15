# JAVA OPENAPI: DiagramContentsDescriptor (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/foundation/diagram/DiagramContentsDescriptor.html
- source_path: `com/nomagic/magicdraw/foundation/diagram/DiagramContentsDescriptor.html`
- source_sha256: `2fa0c7edbc76f0ca84c10303ab6e68055ad83ad9fc1a33167045fec355fccad8`
- captured_utc: `2026-07-14T16:55:20.299065+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.diagram](package-summary.html)

## Interface DiagramContentsDescriptor

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceDiagramContentsDescriptorextends org.eclipse.emf.ecore.EObject

begin-user-doc 
 A representation of the model object '***Contents Descriptor***'.
 end-user-doc 
The following features are supported:
 [`*Representation*`](#getRepresentation())
[`*Exporter Name*`](#getExporterName())
[`*Exporter Version*`](#getExporterVersion())
[`*Used Elements*`](#getUsedElements())
[`*Binary Object*`](#getBinaryObject())
[`*Content Hash*`](#getContentHash())
[`*Used Objects*`](#getUsedObjects())

See Also:
[`DiagramPackage.getDiagramContentsDescriptor()`](DiagramPackage.html#getDiagramContentsDescriptor())
Model:
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`com.nomagic.ci.metamodel.binary.BinaryObject`
`[getBinaryObject](#getBinaryObject())()`
Returns the value of the '***Binary Object***' containment reference.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getContentHash](#getContentHash())()`
Returns the value of the '***Content Hash***' attribute.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getExporterName](#getExporterName())()`
Returns the value of the '***Exporter Name***' attribute.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getExporterVersion](#getExporterVersion())()`
Returns the value of the '***Exporter Version***' attribute.
`[AbstractDiagramRepresentationObject](AbstractDiagramRepresentationObject.html)`
`[getRepresentation](#getRepresentation())()`
Returns the value of the '***Representation***' container reference.
`org.eclipse.emf.common.util.EList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getUsedElements](#getUsedElements())()`
Returns the value of the '***Used Elements***' attribute list.
`org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject>`
`[getUsedObjects](#getUsedObjects())()`
Returns the value of the '***Used Objects***' reference list.
`void`
`[setBinaryObject](#setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject))(com.nomagic.ci.metamodel.binary.BinaryObject value)`
Sets the value of the '[`*Binary Object*`](#getBinaryObject())' containment reference.
`void`
`[setContentHash](#setContentHash(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Content Hash*`](#getContentHash())' attribute.
`void`
`[setExporterName](#setExporterName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Exporter Name*`](#getExporterName())' attribute.
`void`
`[setExporterVersion](#setExporterVersion(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Exporter Version*`](#getExporterVersion())' attribute.
`void`
`[setRepresentation](#setRepresentation(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject))([AbstractDiagramRepresentationObject](AbstractDiagramRepresentationObject.html) value)`
Sets the value of the '[`*Representation*`](#getRepresentation())' container reference.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getRepresentation
[AbstractDiagramRepresentationObject](AbstractDiagramRepresentationObject.html) getRepresentation()
Returns the value of the '***Representation***' container reference.
 It is bidirectional and its opposite is '[`*Diagram Contents*`](AbstractDiagramRepresentationObject.html#getDiagramContents())'.
 begin-user-doc 
If the meaning of the '*Representation*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Representation*' container reference.
See Also:
[`setRepresentation(AbstractDiagramRepresentationObject)`](#setRepresentation(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject))
[`DiagramPackage.getDiagramContentsDescriptor_Representation()`](DiagramPackage.html#getDiagramContentsDescriptor_Representation())
[`AbstractDiagramRepresentationObject.getDiagramContents()`](AbstractDiagramRepresentationObject.html#getDiagramContents())
Model:
opposite="diagramContents" transient="false"
Generated:
setRepresentation
void setRepresentation([AbstractDiagramRepresentationObject](AbstractDiagramRepresentationObject.html) value)
Sets the value of the '[`*Representation*`](#getRepresentation())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Representation*' container reference.
See Also:
[`getRepresentation()`](#getRepresentation())
Generated:
getExporterName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getExporterName()
Returns the value of the '***Exporter Name***' attribute.
 begin-user-doc 
If the meaning of the '*Exporter Name*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Exporter Name*' attribute.
See Also:
[`setExporterName(String)`](#setExporterName(java.lang.String))
[`DiagramPackage.getDiagramContentsDescriptor_ExporterName()`](DiagramPackage.html#getDiagramContentsDescriptor_ExporterName())
Model:
Generated:
setExporterName
void setExporterName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Exporter Name*`](#getExporterName())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Exporter Name*' attribute.
See Also:
[`getExporterName()`](#getExporterName())
Generated:
getExporterVersion
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getExporterVersion()
Returns the value of the '***Exporter Version***' attribute.
 begin-user-doc 
If the meaning of the '*Exporter Version*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Exporter Version*' attribute.
See Also:
[`setExporterVersion(String)`](#setExporterVersion(java.lang.String))
[`DiagramPackage.getDiagramContentsDescriptor_ExporterVersion()`](DiagramPackage.html#getDiagramContentsDescriptor_ExporterVersion())
Model:
Generated:
setExporterVersion
void setExporterVersion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Exporter Version*`](#getExporterVersion())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Exporter Version*' attribute.
See Also:
[`getExporterVersion()`](#getExporterVersion())
Generated:
getUsedElements
org.eclipse.emf.common.util.EList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getUsedElements()
Returns the value of the '***Used Elements***' attribute list.
 The list contents are of type [`String`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html).
 begin-user-doc 
If the meaning of the '*Used Elements*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Used Elements*' attribute list.
See Also:
[`DiagramPackage.getDiagramContentsDescriptor_UsedElements()`](DiagramPackage.html#getDiagramContentsDescriptor_UsedElements())
Model:
ordered="false"
Generated:
getBinaryObject
com.nomagic.ci.metamodel.binary.BinaryObject getBinaryObject()
Returns the value of the '***Binary Object***' containment reference.
 begin-user-doc 
If the meaning of the '*Binary Object*' containment reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Binary Object*' containment reference.
See Also:
[`setBinaryObject(BinaryObject)`](#setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject))
[`DiagramPackage.getDiagramContentsDescriptor_BinaryObject()`](DiagramPackage.html#getDiagramContentsDescriptor_BinaryObject())
Model:
containment="true" resolveProxies="true"
Generated:
setBinaryObject
void setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject value)
Sets the value of the '[`*Binary Object*`](#getBinaryObject())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Binary Object*' containment reference.
See Also:
[`getBinaryObject()`](#getBinaryObject())
Generated:
getContentHash
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getContentHash()
Returns the value of the '***Content Hash***' attribute.
 begin-user-doc 
If the meaning of the '*Content Hash*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Content Hash*' attribute.
See Also:
[`setContentHash(String)`](#setContentHash(java.lang.String))
[`DiagramPackage.getDiagramContentsDescriptor_ContentHash()`](DiagramPackage.html#getDiagramContentsDescriptor_ContentHash())
Model:
Generated:
setContentHash
void setContentHash([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Content Hash*`](#getContentHash())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Content Hash*' attribute.
See Also:
[`getContentHash()`](#getContentHash())
Generated:
getUsedObjects
org.eclipse.emf.common.util.EList<org.eclipse.emf.ecore.EObject> getUsedObjects()
Returns the value of the '***Used Objects***' reference list.
 The list contents are of type `EObject`.
 begin-user-doc 
If the meaning of the '*Used Objects*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Used Objects*' reference list.
See Also:
[`DiagramPackage.getDiagramContentsDescriptor_UsedObjects()`](DiagramPackage.html#getDiagramContentsDescriptor_UsedObjects())
Model:
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.diagram</a></div>
<h1 class="title" title="Interface DiagramContentsDescriptor">Interface DiagramContentsDescriptor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramContentsDescriptor</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Contents Descriptor</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 <ul>
<li><a href="#getRepresentation()"><code><em>Representation</em></code></a></li>
<li><a href="#getExporterName()"><code><em>Exporter Name</em></code></a></li>
<li><a href="#getExporterVersion()"><code><em>Exporter Version</em></code></a></li>
<li><a href="#getUsedElements()"><code><em>Used Elements</em></code></a></li>
<li><a href="#getBinaryObject()"><code><em>Binary Object</em></code></a></li>
<li><a href="#getContentHash()"><code><em>Content Hash</em></code></a></li>
<li><a href="#getUsedObjects()"><code><em>Used Objects</em></code></a></li>
</ul>
</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor()"><code>DiagramPackage.getDiagramContentsDescriptor()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.metamodel.binary.BinaryObject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBinaryObject()">getBinaryObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Binary Object</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContentHash()">getContentHash</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Content Hash</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExporterName()">getExporterName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Exporter Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExporterVersion()">getExporterVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Exporter Version</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentation()">getRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Representation</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUsedElements()">getUsedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Used Elements</b></em>' attribute list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUsedObjects()">getUsedObjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Used Objects</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject)">setBinaryObject</a><wbr/>(com.nomagic.ci.metamodel.binary.BinaryObject value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getBinaryObject()"><code><em>Binary Object</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContentHash(java.lang.String)">setContentHash</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getContentHash()"><code><em>Content Hash</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExporterName(java.lang.String)">setExporterName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getExporterName()"><code><em>Exporter Name</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExporterVersion(java.lang.String)">setExporterVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getExporterVersion()"><code><em>Exporter Version</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRepresentation(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject)">setRepresentation</a><wbr/>(<a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getRepresentation()"><code><em>Representation</em></code></a>' container reference.</div>
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
<section class="detail" id="getRepresentation()">
<h3>getRepresentation</h3>
<div class="member-signature"><span class="return-type"><a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a></span> <span class="element-name">getRepresentation</span>()</div>
<div class="block">Returns the value of the '<em><b>Representation</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="AbstractDiagramRepresentationObject.html#getDiagramContents()"><code><em>Diagram Contents</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Representation</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Representation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setRepresentation(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject)"><code>setRepresentation(AbstractDiagramRepresentationObject)</code></a></li>
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_Representation()"><code>DiagramPackage.getDiagramContentsDescriptor_Representation()</code></a></li>
<li><a href="AbstractDiagramRepresentationObject.html#getDiagramContents()"><code>AbstractDiagramRepresentationObject.getDiagramContents()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="diagramContents" transient="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepresentation(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject)">
<h3>setRepresentation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRepresentation</span><wbr/><span class="parameters">(<a href="AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getRepresentation()"><code><em>Representation</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Representation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getRepresentation()"><code>getRepresentation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExporterName()">
<h3>getExporterName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExporterName</span>()</div>
<div class="block">Returns the value of the '<em><b>Exporter Name</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Exporter Name</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Exporter Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setExporterName(java.lang.String)"><code>setExporterName(String)</code></a></li>
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_ExporterName()"><code>DiagramPackage.getDiagramContentsDescriptor_ExporterName()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExporterName(java.lang.String)">
<h3>setExporterName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExporterName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getExporterName()"><code><em>Exporter Name</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Exporter Name</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getExporterName()"><code>getExporterName()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExporterVersion()">
<h3>getExporterVersion</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExporterVersion</span>()</div>
<div class="block">Returns the value of the '<em><b>Exporter Version</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Exporter Version</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Exporter Version</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setExporterVersion(java.lang.String)"><code>setExporterVersion(String)</code></a></li>
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_ExporterVersion()"><code>DiagramPackage.getDiagramContentsDescriptor_ExporterVersion()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExporterVersion(java.lang.String)">
<h3>setExporterVersion</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExporterVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getExporterVersion()"><code><em>Exporter Version</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Exporter Version</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getExporterVersion()"><code>getExporterVersion()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedElements()">
<h3>getUsedElements</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getUsedElements</span>()</div>
<div class="block">Returns the value of the '<em><b>Used Elements</b></em>' attribute list.
 The list contents are of type <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang"><code>String</code></a>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Used Elements</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Used Elements</em>' attribute list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_UsedElements()"><code>DiagramPackage.getDiagramContentsDescriptor_UsedElements()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBinaryObject()">
<h3>getBinaryObject</h3>
<div class="member-signature"><span class="return-type">com.nomagic.ci.metamodel.binary.BinaryObject</span> <span class="element-name">getBinaryObject</span>()</div>
<div class="block">Returns the value of the '<em><b>Binary Object</b></em>' containment reference.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Binary Object</em>' containment reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Binary Object</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject)"><code>setBinaryObject(BinaryObject)</code></a></li>
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_BinaryObject()"><code>DiagramPackage.getDiagramContentsDescriptor_BinaryObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBinaryObject(com.nomagic.ci.metamodel.binary.BinaryObject)">
<h3>setBinaryObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBinaryObject</span><wbr/><span class="parameters">(com.nomagic.ci.metamodel.binary.BinaryObject value)</span></div>
<div class="block">Sets the value of the '<a href="#getBinaryObject()"><code><em>Binary Object</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Binary Object</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getBinaryObject()"><code>getBinaryObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentHash()">
<h3>getContentHash</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getContentHash</span>()</div>
<div class="block">Returns the value of the '<em><b>Content Hash</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Content Hash</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Content Hash</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setContentHash(java.lang.String)"><code>setContentHash(String)</code></a></li>
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_ContentHash()"><code>DiagramPackage.getDiagramContentsDescriptor_ContentHash()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContentHash(java.lang.String)">
<h3>setContentHash</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContentHash</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getContentHash()"><code><em>Content Hash</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Content Hash</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getContentHash()"><code>getContentHash()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedObjects()">
<h3>getUsedObjects</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.EList&lt;org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getUsedObjects</span>()</div>
<div class="block">Returns the value of the '<em><b>Used Objects</b></em>' reference list.
 The list contents are of type <code>EObject</code>.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Used Objects</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Used Objects</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="DiagramPackage.html#getDiagramContentsDescriptor_UsedObjects()"><code>DiagramPackage.getDiagramContentsDescriptor_UsedObjects()</code></a></li>
</ul>
</dd>
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
