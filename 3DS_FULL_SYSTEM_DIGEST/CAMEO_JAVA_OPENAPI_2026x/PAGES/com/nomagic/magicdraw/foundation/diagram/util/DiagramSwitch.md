# JAVA OPENAPI: DiagramSwitch (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/foundation/diagram/util/DiagramSwitch.html
- source_path: `com/nomagic/magicdraw/foundation/diagram/util/DiagramSwitch.html`
- source_sha256: `aa62c39ebb531d012634a4edff7b2bb2ef26c913b11ba2330d2c46f8f75cc4e1`
- captured_utc: `2026-07-14T16:57:58.126538+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.diagram.util](package-summary.html)

## Class DiagramSwitch<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.eclipse.emf.ecore.util.Switch<T>
com.nomagic.magicdraw.foundation.diagram.util.DiagramSwitch<T>

public classDiagramSwitch<T>
extends org.eclipse.emf.ecore.util.Switch<T>

begin-user-doc 
 The **Switch** for the model's inheritance hierarchy.
 It supports the call `doSwitch(object)`
 to invoke the `caseXXX` method for each class of the model,
 starting with the actual class of the object
 and proceeding up the inheritance hierarchy
 until a non-null result is returned,
 which is the result of the switch.
 end-user-doc

See Also:
[`DiagramPackage`](../DiagramPackage.html)
Generated:

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static [DiagramPackage](../DiagramPackage.html)`
`[modelPackage](#modelPackage)`
The cached model package
 begin-user-doc 
 end-user-doc
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramSwitch](#%3Cinit%3E())()`
Creates an instance of the switch.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[T](DiagramSwitch.html)`
`[caseAbstractDiagramRepresentationObject](#caseAbstractDiagramRepresentationObject(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject))([AbstractDiagramRepresentationObject](../AbstractDiagramRepresentationObject.html) object)`
Returns the result of interpreting the object as an instance of '*Abstract Diagram Representation Object*'.
`[T](DiagramSwitch.html)`
`[caseDiagramContentsDescriptor](#caseDiagramContentsDescriptor(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor))([DiagramContentsDescriptor](../DiagramContentsDescriptor.html) object)`
Returns the result of interpreting the object as an instance of '*Contents Descriptor*'.
`[T](DiagramSwitch.html)`
`[defaultCase](#defaultCase(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject object)`
Returns the result of interpreting the object as an instance of '*EObject*'.
`protected [T](DiagramSwitch.html)`
`[doSwitch](#doSwitch(int,org.eclipse.emf.ecore.EObject))(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)`
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
`protected boolean`
`[isSwitchFor](#isSwitchFor(org.eclipse.emf.ecore.EPackage))(org.eclipse.emf.ecore.EPackage ePackage)`
Checks whether this is a switch for the given package.
Methods inherited from class org.eclipse.emf.ecore.util.Switch
`doSwitch, doSwitch`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
modelPackage
protected static [DiagramPackage](../DiagramPackage.html) modelPackage
The cached model package
 begin-user-doc 
 end-user-doc
Generated:
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramSwitch
public DiagramSwitch()
Creates an instance of the switch.
 begin-user-doc 
 end-user-doc
Generated:
 ============ METHOD DETAIL ========== 
Method Details
isSwitchFor
protected boolean isSwitchFor(org.eclipse.emf.ecore.EPackage ePackage)
Checks whether this is a switch for the given package.
 begin-user-doc 
 end-user-doc
Specified by:
`isSwitchFor` in class `org.eclipse.emf.ecore.util.Switch<[T](DiagramSwitch.html)>`
Returns:
whether this is a switch for the given package.
Generated:
doSwitch
protected [T](DiagramSwitch.html) doSwitch(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)
Calls `caseXXX` for each class of the model until one returns a non null result; it yields that result.
 begin-user-doc 
 end-user-doc
Overrides:
`doSwitch` in class `org.eclipse.emf.ecore.util.Switch<[T](DiagramSwitch.html)>`
Returns:
the first non-null result returned by a `caseXXX` call.
Generated:
caseAbstractDiagramRepresentationObject
public [T](DiagramSwitch.html) caseAbstractDiagramRepresentationObject([AbstractDiagramRepresentationObject](../AbstractDiagramRepresentationObject.html) object)
Returns the result of interpreting the object as an instance of '*Abstract Diagram Representation Object*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Abstract Diagram Representation Object*'.
See Also:
`doSwitch(EObject)`
Generated:
caseDiagramContentsDescriptor
public [T](DiagramSwitch.html) caseDiagramContentsDescriptor([DiagramContentsDescriptor](../DiagramContentsDescriptor.html) object)
Returns the result of interpreting the object as an instance of '*Contents Descriptor*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch.
 end-user-doc
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*Contents Descriptor*'.
See Also:
`doSwitch(EObject)`
Generated:
defaultCase
public [T](DiagramSwitch.html) defaultCase(org.eclipse.emf.ecore.EObject object)
Returns the result of interpreting the object as an instance of '*EObject*'.
 begin-user-doc 
 This implementation returns null;
 returning a non-null result will terminate the switch, but this is the last case anyway.
 end-user-doc
Overrides:
`defaultCase` in class `org.eclipse.emf.ecore.util.Switch<[T](DiagramSwitch.html)>`
Parameters:
`object` - the target of the switch.
Returns:
the result of interpreting the object as an instance of '*EObject*'.
See Also:
`Switch.doSwitch(org.eclipse.emf.ecore.EObject)`
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.diagram.util</a></div>
<h1 class="title" title="Class DiagramSwitch">Class DiagramSwitch&lt;T&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.eclipse.emf.ecore.util.Switch&lt;T&gt;
<div class="inheritance">com.nomagic.magicdraw.foundation.diagram.util.DiagramSwitch&lt;T&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramSwitch&lt;T&gt;</span>
<span class="extends-implements">extends org.eclipse.emf.ecore.util.Switch&lt;T&gt;</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Switch</b> for the model's inheritance hierarchy.
 It supports the call <code>doSwitch(object)</code>
 to invoke the <code>caseXXX</code> method for each class of the model,
 starting with the actual class of the object
 and proceeding up the inheritance hierarchy
 until a non-null result is returned,
 which is the result of the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram"><code>DiagramPackage</code></a></li>
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
<div class="col-first even-row-color"><code>protected static <a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#modelPackage">modelPackage</a></code></div>
<div class="col-last even-row-color">
<div class="block">The cached model package
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramSwitch</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the switch.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseAbstractDiagramRepresentationObject(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject)">caseAbstractDiagramRepresentationObject</a><wbr/>(<a href="../AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Abstract Diagram Representation Object</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#caseDiagramContentsDescriptor(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor)">caseDiagramContentsDescriptor</a><wbr/>(<a href="../DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>Contents Descriptor</em>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#defaultCase(org.eclipse.emf.ecore.EObject)">defaultCase</a><wbr/>(org.eclipse.emf.ecore.EObject object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the result of interpreting the object as an instance of '<em>EObject</em>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doSwitch(int,org.eclipse.emf.ecore.EObject)">doSwitch</a><wbr/>(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSwitchFor(org.eclipse.emf.ecore.EPackage)">isSwitchFor</a><wbr/>(org.eclipse.emf.ecore.EPackage ePackage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether this is a switch for the given package.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.Switch">Methods inherited from class org.eclipse.emf.ecore.util.Switch</h3>
<code>doSwitch, doSwitch</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="modelPackage">
<h3>modelPackage</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="../DiagramPackage.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramPackage</a></span> <span class="element-name">modelPackage</span></div>
<div class="block">The cached model package
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>DiagramSwitch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramSwitch</span>()</div>
<div class="block">Creates an instance of the switch.
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
<section class="detail" id="isSwitchFor(org.eclipse.emf.ecore.EPackage)">
<h3>isSwitchFor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSwitchFor</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EPackage ePackage)</span></div>
<div class="block">Checks whether this is a switch for the given package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isSwitchFor</code> in class <code>org.eclipse.emf.ecore.util.Switch&lt;<a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>whether this is a switch for the given package.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="doSwitch(int,org.eclipse.emf.ecore.EObject)">
<h3>doSwitch</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></span> <span class="element-name">doSwitch</span><wbr/><span class="parameters">(int classifierID,
 org.eclipse.emf.ecore.EObject theEObject)</span></div>
<div class="block">Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>doSwitch</code> in class <code>org.eclipse.emf.ecore.util.Switch&lt;<a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>the first non-null result returned by a <code>caseXXX</code> call.</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseAbstractDiagramRepresentationObject(com.nomagic.magicdraw.foundation.diagram.AbstractDiagramRepresentationObject)">
<h3>caseAbstractDiagramRepresentationObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></span> <span class="element-name">caseAbstractDiagramRepresentationObject</span><wbr/><span class="parameters">(<a href="../AbstractDiagramRepresentationObject.html" title="interface in com.nomagic.magicdraw.foundation.diagram">AbstractDiagramRepresentationObject</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Abstract Diagram Representation Object</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Abstract Diagram Representation Object</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>doSwitch(EObject)</code></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="caseDiagramContentsDescriptor(com.nomagic.magicdraw.foundation.diagram.DiagramContentsDescriptor)">
<h3>caseDiagramContentsDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></span> <span class="element-name">caseDiagramContentsDescriptor</span><wbr/><span class="parameters">(<a href="../DiagramContentsDescriptor.html" title="interface in com.nomagic.magicdraw.foundation.diagram">DiagramContentsDescriptor</a> object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>Contents Descriptor</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>Contents Descriptor</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>doSwitch(EObject)</code></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="defaultCase(org.eclipse.emf.ecore.EObject)">
<h3>defaultCase</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a></span> <span class="element-name">defaultCase</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject object)</span></div>
<div class="block">Returns the result of interpreting the object as an instance of '<em>EObject</em>'.
 <!-- begin-user-doc -->
 This implementation returns null;
 returning a non-null result will terminate the switch, but this is the last case anyway.
 <!-- end-user-doc --></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>defaultCase</code> in class <code>org.eclipse.emf.ecore.util.Switch&lt;<a href="DiagramSwitch.html" title="type parameter in DiagramSwitch">T</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - the target of the switch.</dd>
<dt>Returns:</dt>
<dd>the result of interpreting the object as an instance of '<em>EObject</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>Switch.doSwitch(org.eclipse.emf.ecore.EObject)</code></li>
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
