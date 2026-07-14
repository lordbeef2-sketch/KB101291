# JAVA OPENAPI: Cases (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Cases.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Cases.html`
- source_sha256: `824f2a2f04a79af585554e1dbcc915d209bc4a40f78fdb5d1b5ccb65a0e63c7e`
- captured_utc: `2026-07-14T16:45:02.224032+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Cases

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Cases

@OpenApiAllpublic classCases
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for identifying case-related usages and definitions,
 including general cases, use cases, analysis cases, and verification cases.
 These helpers centralize common type checks based on `EClass`,
 [`Element`](../../kerml/model/kerml/Element.html), and owning-type relationships.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Cases](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isAnalysisCaseUsageOrDefinition](#isAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is an [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html) or
 [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
`static boolean`
`[isCaseUsageOrDefinition](#isCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is a [`CaseUsage`](sysml/CaseUsage.html) or
 [`CaseDefinition`](sysml/CaseDefinition.html).
`static boolean`
`[isCaseUsageOrDefinition](#isCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a
 [`CaseUsage`](sysml/CaseUsage.html) or [`CaseDefinition`](sysml/CaseDefinition.html).
`static boolean`
`[isOwningTypeAnalysisCaseUsageOrDefinition](#isOwningTypeAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Returns whether the owning type of the given feature is an
 [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html) or [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
`static boolean`
`[isOwningTypeCaseUsageOrDefinition](#isOwningTypeCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Returns whether the owning type of the given feature is a
 [`CaseUsage`](sysml/CaseUsage.html) or [`CaseDefinition`](sysml/CaseDefinition.html).
`static boolean`
`[isOwningTypeUseCaseUsageOrDefinition](#isOwningTypeUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Returns whether the owning type of the given feature is a
 [`UseCaseUsage`](sysml/UseCaseUsage.html) or [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
`static boolean`
`[isOwningTypeVerificationCaseUsageOrDefinition](#isOwningTypeVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Returns whether the owning type of the given feature is a
 [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html) or [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
`static boolean`
`[isUseCaseUsageOrDefinition](#isUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is a [`UseCaseUsage`](sysml/UseCaseUsage.html) or
 [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
`static boolean`
`[isUseCaseUsageOrDefinition](#isUseCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a
 [`UseCaseUsage`](sysml/UseCaseUsage.html) or [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
`static boolean`
`[isVerificationCaseUsageOrDefinition](#isVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is a [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html) or
 [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Cases
public Cases()
 ============ METHOD DETAIL ========== 
Method Details
isOwningTypeCaseUsageOrDefinition
public static boolean isOwningTypeCaseUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Returns whether the owning type of the given feature is a
 [`CaseUsage`](sysml/CaseUsage.html) or [`CaseDefinition`](sysml/CaseDefinition.html).
Parameters:
`feature` - the feature whose owning type is tested
Returns:
`true` if the owning type is a case usage or definition
isCaseUsageOrDefinition
public static boolean isCaseUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is a [`CaseUsage`](sysml/CaseUsage.html) or
 [`CaseDefinition`](sysml/CaseDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is a case usage or definition
isCaseUsageOrDefinition
public static boolean isCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a
 [`CaseUsage`](sysml/CaseUsage.html) or [`CaseDefinition`](sysml/CaseDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a case usage or definition
isOwningTypeUseCaseUsageOrDefinition
public static boolean isOwningTypeUseCaseUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Returns whether the owning type of the given feature is a
 [`UseCaseUsage`](sysml/UseCaseUsage.html) or [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
Parameters:
`feature` - the feature whose owning type is tested
Returns:
`true` if the owning type is a use case usage or definition
isUseCaseUsageOrDefinition
public static boolean isUseCaseUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is a [`UseCaseUsage`](sysml/UseCaseUsage.html) or
 [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is a use case usage or definition
isUseCaseUsageOrDefinition
public static boolean isUseCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a
 [`UseCaseUsage`](sysml/UseCaseUsage.html) or [`UseCaseDefinition`](sysml/UseCaseDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a use case usage or definition
isOwningTypeAnalysisCaseUsageOrDefinition
public static boolean isOwningTypeAnalysisCaseUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Returns whether the owning type of the given feature is an
 [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html) or [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
Parameters:
`feature` - the feature whose owning type is tested
Returns:
`true` if the owning type is an analysis case usage or definition
isAnalysisCaseUsageOrDefinition
public static boolean isAnalysisCaseUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is an [`AnalysisCaseUsage`](sysml/AnalysisCaseUsage.html) or
 [`AnalysisCaseDefinition`](sysml/AnalysisCaseDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is an analysis case usage or definition
isOwningTypeVerificationCaseUsageOrDefinition
public static boolean isOwningTypeVerificationCaseUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Returns whether the owning type of the given feature is a
 [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html) or [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
Parameters:
`feature` - the feature whose owning type is tested
Returns:
`true` if the owning type is a verification case usage or definition
isVerificationCaseUsageOrDefinition
public static boolean isVerificationCaseUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is a [`VerificationCaseUsage`](sysml/VerificationCaseUsage.html) or
 [`VerificationCaseDefinition`](sysml/VerificationCaseDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is a verification case usage or definition

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Cases">Class Cases</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Cases</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Cases</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for identifying case-related usages and definitions,
 including general cases, use cases, analysis cases, and verification cases.
 <p>
 These helpers centralize common type checks based on <code>EClass</code>,
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>, and owning-type relationships.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Cases</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isAnalysisCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is an <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a> or
 <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or
 <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isCaseUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a
 <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeAnalysisCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the owning type of the given feature is an
 <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a> or <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeUseCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeVerificationCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a> or <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isUseCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or
 <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isUseCaseUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a
 <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isVerificationCaseUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a> or
 <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Cases</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Cases</span>()</div>
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
<section class="detail" id="isOwningTypeCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeCaseUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is tested</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the owning type is a case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCaseUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or
 <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCaseUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a
 <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeUseCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeUseCaseUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is tested</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the owning type is a use case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isUseCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUseCaseUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or
 <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a use case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseCaseUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isUseCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUseCaseUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a
 <a href="sysml/UseCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseUsage</code></a> or <a href="sysml/UseCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>UseCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a use case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeAnalysisCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeAnalysisCaseUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns whether the owning type of the given feature is an
 <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a> or <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is tested</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the owning type is an analysis case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAnalysisCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isAnalysisCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnalysisCaseUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is an <a href="sysml/AnalysisCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseUsage</code></a> or
 <a href="sysml/AnalysisCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AnalysisCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is an analysis case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeVerificationCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeVerificationCaseUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns whether the owning type of the given feature is a
 <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a> or <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is tested</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the owning type is a verification case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVerificationCaseUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isVerificationCaseUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isVerificationCaseUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/VerificationCaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseUsage</code></a> or
 <a href="sysml/VerificationCaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VerificationCaseDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a verification case usage or definition</dd>
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
