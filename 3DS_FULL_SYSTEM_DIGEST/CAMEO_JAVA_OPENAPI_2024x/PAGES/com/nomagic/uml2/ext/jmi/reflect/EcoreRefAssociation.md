# JAVA OPENAPI: EcoreRefAssociation (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/reflect/EcoreRefAssociation.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/EcoreRefAssociation.html`
- source_sha256: `3c42f7d892b6c938062b014d9b20f4ad12310fb138360bc78fb72fd1d641cec1`
- captured_utc: `2026-07-14T16:52:44.970317+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class EcoreRefAssociation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation
com.nomagic.uml2.ext.jmi.reflect.EcoreRefAssociation

All Implemented Interfaces:
`com.nomagic.uml2.ext.jmi.MapOwner`, `[AbstractRefBaseObject](AbstractRefBaseObject.html)`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`, `javax.jmi.reflect.RefAssociation`, `javax.jmi.reflect.RefBaseObject`

public classEcoreRefAssociation
extends com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`mMetaObject, repository`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EcoreRefAssociation](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EReference))([AbstractRepository](AbstractRepository.html) repository,
 org.eclipse.emf.ecore.EReference ref1,
 org.eclipse.emf.ecore.EReference ref2)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation
`refAddLink, refAllLinks, refLinkExists, refQuery, refQuery, refRemoveLink`
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EcoreRefAssociation
public EcoreRefAssociation([AbstractRepository](AbstractRepository.html) repository,
 org.eclipse.emf.ecore.EReference ref1,
 org.eclipse.emf.ecore.EReference ref2)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class EcoreRefAssociation">Class EcoreRefAssociation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.EcoreRefAssociation</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.uml2.ext.jmi.MapOwner</code>, <code><a href="AbstractRefBaseObject.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRefBaseObject</a></code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code>, <code>javax.jmi.reflect.RefAssociation</code>, <code>javax.jmi.reflect.RefBaseObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">EcoreRefAssociation</span>
<span class="extends-implements">extends com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>mMetaObject, repository</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EReference)">EcoreRefAssociation</a><wbr/>(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository,
 org.eclipse.emf.ecore.EReference ref1,
 org.eclipse.emf.ecore.EReference ref2)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefAssociation</h3>
<code>refAddLink, refAllLinks, refLinkExists, refQuery, refQuery, refRemoveLink</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>getRepository, mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository,org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EReference)">
<h3>EcoreRefAssociation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EcoreRefAssociation</span><wbr/><span class="parameters">(<a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a> repository,
 org.eclipse.emf.ecore.EReference ref1,
 org.eclipse.emf.ecore.EReference ref2)</span></div>
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
