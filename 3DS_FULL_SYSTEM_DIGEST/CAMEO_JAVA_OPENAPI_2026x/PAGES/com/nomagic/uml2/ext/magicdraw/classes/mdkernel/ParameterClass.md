# JAVA OPENAPI: ParameterClass (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ParameterClass.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ParameterClass.html`
- source_sha256: `a90ea8218d0d9d95d42a02494a99fffc0bbc913d0cff2190ebeeed24a01bd933`
- captured_utc: `2026-07-14T16:58:54.115472+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface ParameterClass

All Superinterfaces:
`javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefClass`, `javax.jmi.reflect.RefFeatured`

public interfaceParameterClassextends javax.jmi.reflect.RefClass

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Parameter](Parameter.html)`
`[createParameter](#createParameter())()`

`[Parameter](Parameter.html)`
`[createParameter](#createParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))([ParameterDirectionKind](ParameterDirectionKind.html) direction,
 [ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html) effect,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isException,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isOrdered,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isStream,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isUnique,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [VisibilityKind](VisibilityKind.html) visibility)`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefClass
`refAllOfClass, refAllOfType, refCreateInstance, refCreateStruct, refCreateStruct, refGetEnum, refGetEnum`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refGetValue, refInvokeOperation, refInvokeOperation, refSetValue, refSetValue`

============ METHOD DETAIL ========== 
Method Details
createParameter
[Parameter](Parameter.html) createParameter()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
createParameter
[Parameter](Parameter.html) createParameter([ParameterDirectionKind](ParameterDirectionKind.html) direction,
 [ParameterEffectKind](../../activities/mdcompleteactivities/ParameterEffectKind.html) effect,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isException,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isOrdered,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isStream,
 [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isUnique,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [VisibilityKind](VisibilityKind.html) visibility)
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface ParameterClass">Interface ParameterClass</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefClass</code>, <code>javax.jmi.reflect.RefFeatured</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ParameterClass</span><span class="extends-implements">
extends javax.jmi.reflect.RefClass</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createParameter()">createParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">createParameter</a><wbr/>(<a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> direction,
 <a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a> effect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isException,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isOrdered,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isStream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isUnique,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefClass">Methods inherited from interface javax.jmi.reflect.RefClass</h3>
<code>refAllOfClass, refAllOfType, refCreateInstance, refCreateStruct, refCreateStruct, refGetEnum, refGetEnum</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refGetValue, refInvokeOperation, refInvokeOperation, refSetValue, refSetValue</code></div>
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
<section class="detail" id="createParameter()">
<h3>createParameter</h3>
<div class="member-signature"><span class="return-type"><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">createParameter</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ParameterDirectionKind,com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterEffectKind,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.Boolean,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">
<h3>createParameter</h3>
<div class="member-signature"><span class="return-type"><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">createParameter</span><wbr/><span class="parameters">(<a href="ParameterDirectionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ParameterDirectionKind</a> direction,
 <a href="../../activities/mdcompleteactivities/ParameterEffectKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterEffectKind</a> effect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isException,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isOrdered,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isStream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> isUnique,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</span>
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
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
