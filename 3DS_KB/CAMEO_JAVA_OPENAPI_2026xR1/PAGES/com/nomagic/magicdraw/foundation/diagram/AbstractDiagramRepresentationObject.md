# JAVA OPENAPI: AbstractDiagramRepresentationObject (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/foundation/diagram/AbstractDiagramRepresentationObject.html
- source_path: `com/nomagic/magicdraw/foundation/diagram/AbstractDiagramRepresentationObject.html`
- source_sha256: `ff47be7b5421f6b68f7eeaf11d951957ad401b4d12ceceae08a6c303be2b1f33`
- captured_utc: `2026-07-14T16:45:37.093498+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.diagram](package-summary.html)

## Interface AbstractDiagramRepresentationObject

All Superinterfaces:
`org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.common.notify.Notifier`

public interfaceAbstractDiagramRepresentationObjectextends org.eclipse.emf.ecore.EObject

begin-user-doc 
 A representation of the model object '***Abstract Diagram Representation Object***'.
 end-user-doc 
The following features are supported:
 [`*ID*`](#getID())
[`*Type*`](#getType())
[`*Uml Type*`](#getUmlType())
[`*Diagram Properties*`](#getDiagramProperties())
[`*Initial Frame Size Set*`](#isInitialFrameSizeSet())
[`*Required Feature*`](#getRequiredFeature())
[`*Diagram Contents*`](#getDiagramContents())
[`*Diagram Style ID*`](#getDiagramStyleID())

See Also:
[`DiagramPackage.getAbstractDiagramRepresentationObject()`](DiagramPackage.html#getAbstractDiagramRepresentationObject())
Model:
abstract="true"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[DiagramContentsDescriptor](DiagramContentsDescriptor.html)`
`[getDiagramContents](#getDiagramContents())()`
Returns the value of the '***Diagram Contents***' containment reference.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramProperties](#getDiagramProperties())()`
Returns the value of the '***Diagram Properties***' attribute.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramStyleID](#getDiagramStyleID())()`
Returns the value of the '***Diagram Style ID***' attribute.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns the value of the '***ID***' attribute.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRequiredFeature](#getRequiredFeature())()`
Returns the value of the '***Required Feature***' attribute.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Returns the value of the '***Type***' attribute.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getUmlType](#getUmlType())()`
Returns the value of the '***Uml Type***' attribute.
`boolean`
`[isInitialFrameSizeSet](#isInitialFrameSizeSet())()`
Returns the value of the '***Initial Frame Size Set***' attribute.
`void`
`[setDiagramContents](#setDiagramContents(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor))([DiagramContentsDescriptor](DiagramContentsDescriptor.html) value)`
Sets the value of the '[`*Diagram Contents*`](#getDiagramContents())' containment reference.
`void`
`[setDiagramProperties](#setDiagramProperties(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Diagram Properties*`](#getDiagramProperties())' attribute.
`void`
`[setDiagramStyleID](#setDiagramStyleID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Diagram Style ID*`](#getDiagramStyleID())' attribute.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*ID*`](#getID())' attribute.
`void`
`[setInitialFrameSizeSet](#setInitialFrameSizeSet(boolean))(boolean value)`
Sets the value of the '[`*Initial Frame Size Set*`](#isInitialFrameSizeSet())' attribute.
`void`
`[setRequiredFeature](#setRequiredFeature(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Required Feature*`](#getRequiredFeature())' attribute.
`void`
`[setType](#setType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Type*`](#getType())' attribute.
`void`
`[setUmlType](#setUmlType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Uml Type*`](#getUmlType())' attribute.
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ METHOD DETAIL ========== 
Method Details
getID
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getID()
Returns the value of the '***ID***' attribute.
 begin-user-doc 
If the meaning of the '*ID*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*ID*' attribute.
See Also:
[`setID(String)`](#setID(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_ID()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_ID())
Model:
Generated:
setID
void setID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*ID*`](#getID())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*ID*' attribute.
See Also:
[`getID()`](#getID())
Generated:
getType
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType()
Returns the value of the '***Type***' attribute.
 begin-user-doc 
If the meaning of the '*Type*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Type*' attribute.
See Also:
[`setType(String)`](#setType(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_Type()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_Type())
Model:
Generated:
setType
void setType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Type*`](#getType())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Type*' attribute.
See Also:
[`getType()`](#getType())
Generated:
getUmlType
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getUmlType()
Returns the value of the '***Uml Type***' attribute.
 begin-user-doc 
If the meaning of the '*Uml Type*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Uml Type*' attribute.
See Also:
[`setUmlType(String)`](#setUmlType(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_UmlType()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_UmlType())
Model:
Generated:
setUmlType
void setUmlType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Uml Type*`](#getUmlType())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Uml Type*' attribute.
See Also:
[`getUmlType()`](#getUmlType())
Generated:
getDiagramProperties
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramProperties()
Returns the value of the '***Diagram Properties***' attribute.
 begin-user-doc 
If the meaning of the '*Diagram Properties*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Diagram Properties*' attribute.
See Also:
[`setDiagramProperties(String)`](#setDiagramProperties(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_DiagramProperties()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramProperties())
Model:
annotation="http://www.eclipse.org/CDO/DBStore columnType='CLOB'"
Generated:
setDiagramProperties
void setDiagramProperties([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Diagram Properties*`](#getDiagramProperties())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Diagram Properties*' attribute.
See Also:
[`getDiagramProperties()`](#getDiagramProperties())
Generated:
isInitialFrameSizeSet
boolean isInitialFrameSizeSet()
Returns the value of the '***Initial Frame Size Set***' attribute.
 begin-user-doc 
If the meaning of the '*Initial Frame Size Set*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Initial Frame Size Set*' attribute.
See Also:
[`setInitialFrameSizeSet(boolean)`](#setInitialFrameSizeSet(boolean))
[`DiagramPackage.getAbstractDiagramRepresentationObject_InitialFrameSizeSet()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_InitialFrameSizeSet())
Model:
Generated:
setInitialFrameSizeSet
void setInitialFrameSizeSet(boolean value)
Sets the value of the '[`*Initial Frame Size Set*`](#isInitialFrameSizeSet())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Initial Frame Size Set*' attribute.
See Also:
[`isInitialFrameSizeSet()`](#isInitialFrameSizeSet())
Generated:
getRequiredFeature
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRequiredFeature()
Returns the value of the '***Required Feature***' attribute.
 begin-user-doc 
If the meaning of the '*Required Feature*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Required Feature*' attribute.
See Also:
[`setRequiredFeature(String)`](#setRequiredFeature(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_RequiredFeature()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_RequiredFeature())
Model:
Generated:
setRequiredFeature
void setRequiredFeature([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Required Feature*`](#getRequiredFeature())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Required Feature*' attribute.
See Also:
[`getRequiredFeature()`](#getRequiredFeature())
Generated:
getDiagramContents
[DiagramContentsDescriptor](DiagramContentsDescriptor.html) getDiagramContents()
Returns the value of the '***Diagram Contents***' containment reference.
 It is bidirectional and its opposite is '[`*Representation*`](DiagramContentsDescriptor.html#getRepresentation())'.
 begin-user-doc 
If the meaning of the '*Diagram Contents*' containment reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Diagram Contents*' containment reference.
See Also:
[`setDiagramContents(DiagramContentsDescriptor)`](#setDiagramContents(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor))
[`DiagramPackage.getAbstractDiagramRepresentationObject_DiagramContents()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramContents())
[`DiagramContentsDescriptor.getRepresentation()`](DiagramContentsDescriptor.html#getRepresentation())
Model:
opposite="representation" containment="true" resolveProxies="true"
Generated:
setDiagramContents
void setDiagramContents([DiagramContentsDescriptor](DiagramContentsDescriptor.html) value)
Sets the value of the '[`*Diagram Contents*`](#getDiagramContents())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Diagram Contents*' containment reference.
See Also:
[`getDiagramContents()`](#getDiagramContents())
Generated:
getDiagramStyleID
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramStyleID()
Returns the value of the '***Diagram Style ID***' attribute.
 begin-user-doc 
If the meaning of the '*Diagram Style ID*' attribute isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Diagram Style ID*' attribute.
See Also:
[`setDiagramStyleID(String)`](#setDiagramStyleID(java.lang.String))
[`DiagramPackage.getAbstractDiagramRepresentationObject_DiagramStyleID()`](DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramStyleID())
Model:
Generated:
setDiagramStyleID
void setDiagramStyleID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Diagram Style ID*`](#getDiagramStyleID())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Diagram Style ID*' attribute.
See Also:
[`getDiagramStyleID()`](#getDiagramStyleID())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.diagram</a></div>
<h1 class="title" title="Interface AbstractDiagramRepresentationObject">Interface AbstractDiagramRepresentationObject</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">AbstractDiagramRepresentationObject</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EObject</span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Abstract Diagram Representation Object</b></em>'.
 <!-- end-user-doc -->
<p>
 The following features are supported:
 <ul>
<li><a href="#getID()"><code><em>ID</em></code></a></li>
<li><a href="#getType()"><code><em>Type</em></code></a></li>
<li><a href="#getUmlType()"><code><em>Uml Type</em></code></a></li>
<li><a href="#getDiagramProperties()"><code><em>Diagram Properties</em></code></a></li>
<li><a href="#isInitialFrameSizeSet()"><code><em>Initial Frame Size Set</em></code></a></li>
<li><a href="#getRequiredFeature()"><code><em>Required Feature</em></code></a></li>
<li><a href="#getDiagramContents()"><code><em>Diagram Contents</em></code></a></li>
<li><a href="#getDiagramStyleID()"><code><em>Diagram Style ID</em></code></a></li>
</ul>
</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject()"><code>DiagramPackage.getAbstractDiagramRepresentationObject()</code></a></li>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContents()">getDiagramContents</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Diagram Contents</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramProperties()">getDiagramProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Diagram Properties</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramStyleID()">getDiagramStyleID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Diagram Style ID</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>ID</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRequiredFeature()">getRequiredFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Required Feature</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Type</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUmlType()">getUmlType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Uml Type</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isInitialFrameSizeSet()">isInitialFrameSizeSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Initial Frame Size Set</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDiagramContents(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor)">setDiagramContents</a><wbr/>(<a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDiagramContents()"><code><em>Diagram Contents</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDiagramProperties(java.lang.String)">setDiagramProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDiagramProperties()"><code><em>Diagram Properties</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDiagramStyleID(java.lang.String)">setDiagramStyleID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDiagramStyleID()"><code><em>Diagram Style ID</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getID()"><code><em>ID</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInitialFrameSizeSet(boolean)">setInitialFrameSizeSet</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isInitialFrameSizeSet()"><code><em>Initial Frame Size Set</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRequiredFeature(java.lang.String)">setRequiredFeature</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getRequiredFeature()"><code><em>Required Feature</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setType(java.lang.String)">setType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUmlType(java.lang.String)">setUmlType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUmlType()"><code><em>Uml Type</em></code></a>' attribute.</div>
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
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns the value of the '<em><b>ID</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>ID</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setID(java.lang.String)"><code>setID(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_ID()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_ID()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getID()"><code><em>ID</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getID()"><code>getID()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the value of the '<em><b>Type</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Type</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setType(java.lang.String)"><code>setType(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_Type()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_Type()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(java.lang.String)">
<h3>setType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getType()"><code><em>Type</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getType()"><code>getType()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUmlType()">
<h3>getUmlType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUmlType</span>()</div>
<div class="block">Returns the value of the '<em><b>Uml Type</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Uml Type</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Uml Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setUmlType(java.lang.String)"><code>setUmlType(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_UmlType()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_UmlType()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUmlType(java.lang.String)">
<h3>setUmlType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUmlType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUmlType()"><code><em>Uml Type</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Uml Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getUmlType()"><code>getUmlType()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramProperties()">
<h3>getDiagramProperties</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramProperties</span>()</div>
<div class="block">Returns the value of the '<em><b>Diagram Properties</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Diagram Properties</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Diagram Properties</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDiagramProperties(java.lang.String)"><code>setDiagramProperties(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramProperties()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_DiagramProperties()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="http://www.eclipse.org/CDO/DBStore columnType='CLOB'"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramProperties(java.lang.String)">
<h3>setDiagramProperties</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDiagramProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDiagramProperties()"><code><em>Diagram Properties</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Diagram Properties</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getDiagramProperties()"><code>getDiagramProperties()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInitialFrameSizeSet()">
<h3>isInitialFrameSizeSet</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isInitialFrameSizeSet</span>()</div>
<div class="block">Returns the value of the '<em><b>Initial Frame Size Set</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Initial Frame Size Set</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Initial Frame Size Set</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setInitialFrameSizeSet(boolean)"><code>setInitialFrameSizeSet(boolean)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_InitialFrameSizeSet()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_InitialFrameSizeSet()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialFrameSizeSet(boolean)">
<h3>setInitialFrameSizeSet</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInitialFrameSizeSet</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isInitialFrameSizeSet()"><code><em>Initial Frame Size Set</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Initial Frame Size Set</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isInitialFrameSizeSet()"><code>isInitialFrameSizeSet()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredFeature()">
<h3>getRequiredFeature</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredFeature</span>()</div>
<div class="block">Returns the value of the '<em><b>Required Feature</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Required Feature</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Required Feature</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setRequiredFeature(java.lang.String)"><code>setRequiredFeature(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_RequiredFeature()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_RequiredFeature()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiredFeature(java.lang.String)">
<h3>setRequiredFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRequiredFeature</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getRequiredFeature()"><code><em>Required Feature</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Required Feature</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getRequiredFeature()"><code>getRequiredFeature()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContents()">
<h3>getDiagramContents</h3>
<div class="member-signature"><span class="return-type"><a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a></span> <span class="element-name">getDiagramContents</span>()</div>
<div class="block">Returns the value of the '<em><b>Diagram Contents</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="DiagramContentsDescriptor.html#getRepresentation()"><code><em>Representation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Diagram Contents</em>' containment reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Diagram Contents</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDiagramContents(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor)"><code>setDiagramContents(DiagramContentsDescriptor)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramContents()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_DiagramContents()</code></a></li>
<li><a href="DiagramContentsDescriptor.html#getRepresentation()"><code>DiagramContentsDescriptor.getRepresentation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="representation" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramContents(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor)">
<h3>setDiagramContents</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDiagramContents</span><wbr/><span class="parameters">(<a href="DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDiagramContents()"><code><em>Diagram Contents</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Diagram Contents</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getDiagramContents()"><code>getDiagramContents()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramStyleID()">
<h3>getDiagramStyleID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramStyleID</span>()</div>
<div class="block">Returns the value of the '<em><b>Diagram Style ID</b></em>' attribute.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Diagram Style ID</em>' attribute isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Diagram Style ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDiagramStyleID(java.lang.String)"><code>setDiagramStyleID(String)</code></a></li>
<li><a href="DiagramPackage.html#getAbstractDiagramRepresentationObject_DiagramStyleID()"><code>DiagramPackage.getAbstractDiagramRepresentationObject_DiagramStyleID()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDiagramStyleID(java.lang.String)">
<h3>setDiagramStyleID</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDiagramStyleID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDiagramStyleID()"><code><em>Diagram Style ID</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Diagram Style ID</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getDiagramStyleID()"><code>getDiagramStyleID()</code></a></li>
</ul>
</dd>
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
