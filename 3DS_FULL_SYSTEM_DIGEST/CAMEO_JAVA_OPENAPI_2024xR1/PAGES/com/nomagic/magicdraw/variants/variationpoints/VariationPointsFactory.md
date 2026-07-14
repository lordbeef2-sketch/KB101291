# JAVA OPENAPI: VariationPointsFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/variants/variationpoints/VariationPointsFactory.html
- source_path: `com/nomagic/magicdraw/variants/variationpoints/VariationPointsFactory.html`
- source_sha256: `e05b7f829ce3ee0839e8b5ca0730aea2ea9fccaec6f1571378551fed75e5fdab`
- captured_utc: `2026-07-14T16:52:21.110999+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.variationpoints](package-summary.html)

## Class VariationPointsFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.variationpoints.VariationPointsFactory

@OpenApiAllpublic classVariationPointsFactory
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Factory to create all possible types of variation points
 Created variation point defines how some element will be transformed during variant realization

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[VariationPointsFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[VariationPoint](VariationPoint.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[createActivityBranchExistenceVariationPoint](#createActivityBranchExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [BooleanEvaluator](../evaluation/BooleanEvaluator.html) evaluator)`

`[PropertyVariationPoint](PropertyVariationPoint.html)`
`[createBehaviorVariationPoint](#createBehaviorVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)> evaluator)`

`[PropertyVariationPoint](PropertyVariationPoint.html)`
`[createDefaultValueVariationPoint](#createDefaultValueVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)`

`[VariationPoint](VariationPoint.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[createExistenceVariationPoint](#createExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [BooleanEvaluator](../evaluation/BooleanEvaluator.html) evaluator)`

`[PropertyVariationPoint](PropertyVariationPoint.html)`
`[createMultiplicityVariationPoint](#createMultiplicityVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> evaluator)`

`[PropertyVariationPoint](PropertyVariationPoint.html)`
`[createPropertyVariationPoint](#createPropertyVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)`

`com.nomagic.magicdraw.variants.variationpoints.TagVariationPoint`
`[createTagVariationPoint](#createTagVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)`

`[PropertyVariationPoint](PropertyVariationPoint.html)`
`[createTypeVariationPoint](#createTypeVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html)> evaluator)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
VariationPointsFactory
public VariationPointsFactory()
 ============ METHOD DETAIL ========== 
Method Details
createExistenceVariationPoint
public [VariationPoint](VariationPoint.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> createExistenceVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [BooleanEvaluator](../evaluation/BooleanEvaluator.html) evaluator)
createActivityBranchExistenceVariationPoint
public [VariationPoint](VariationPoint.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> createActivityBranchExistenceVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [BooleanEvaluator](../evaluation/BooleanEvaluator.html) evaluator)
createPropertyVariationPoint
public [PropertyVariationPoint](PropertyVariationPoint.html) createPropertyVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)
createTagVariationPoint
public com.nomagic.magicdraw.variants.variationpoints.TagVariationPoint createTagVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tagName,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)
createMultiplicityVariationPoint
public [PropertyVariationPoint](PropertyVariationPoint.html) createMultiplicityVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> evaluator)
createDefaultValueVariationPoint
public [PropertyVariationPoint](PropertyVariationPoint.html) createDefaultValueVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> evaluator)
createTypeVariationPoint
public [PropertyVariationPoint](PropertyVariationPoint.html) createTypeVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html)> evaluator)
createBehaviorVariationPoint
public [PropertyVariationPoint](PropertyVariationPoint.html) createBehaviorVariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html)> evaluator)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.variationpoints</a></div>
<h1 class="title" title="Class VariationPointsFactory">Class VariationPointsFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.variationpoints.VariationPointsFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">VariationPointsFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Factory to create all possible types of variation points
 Created variation point defines how some element will be transformed during variant realization</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">VariationPointsFactory</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityBranchExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator)">createActivityBranchExistenceVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/BooleanEvaluator.html" title="class in com.nomagic.magicdraw.variants.evaluation">BooleanEvaluator</a> evaluator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBehaviorVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createBehaviorVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt; evaluator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultValueVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createDefaultValueVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator)">createExistenceVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/BooleanEvaluator.html" title="class in com.nomagic.magicdraw.variants.evaluation">BooleanEvaluator</a> evaluator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createMultiplicityVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; evaluator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createPropertyVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.variants.variationpoints.TagVariationPoint</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTagVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createTagVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypeVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">createTypeVariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; evaluator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>VariationPointsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VariationPointsFactory</span>()</div>
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
<section class="detail" id="createExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator)">
<h3>createExistenceVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">createExistenceVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/BooleanEvaluator.html" title="class in com.nomagic.magicdraw.variants.evaluation">BooleanEvaluator</a> evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createActivityBranchExistenceVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.BooleanEvaluator)">
<h3>createActivityBranchExistenceVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">createActivityBranchExistenceVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/BooleanEvaluator.html" title="class in com.nomagic.magicdraw.variants.evaluation">BooleanEvaluator</a> evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createPropertyVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createPropertyVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></span> <span class="element-name">createPropertyVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createTagVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createTagVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.variants.variationpoints.TagVariationPoint</span> <span class="element-name">createTagVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createMultiplicityVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></span> <span class="element-name">createMultiplicityVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createDefaultValueVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createDefaultValueVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></span> <span class="element-name">createDefaultValueVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createTypeVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createTypeVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></span> <span class="element-name">createTypeVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; evaluator)</span></div>
</section>
</li>
<li>
<section class="detail" id="createBehaviorVariationPoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>createBehaviorVariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></span> <span class="element-name">createBehaviorVariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt; evaluator)</span></div>
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
