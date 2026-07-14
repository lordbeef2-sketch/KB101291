# JAVA OPENAPI: Annotations (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Annotations.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Annotations.html`
- source_sha256: `0342973115ce1e43aae36cd71f51522c6b784178d9f4d625aa020c3bda88adb0`
- captured_utc: `2026-07-14T16:44:47.243833+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Annotations

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Annotations

@OpenApiAllpublic classAnnotations
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Annotation`](kerml/Annotation.html) and [`AnnotatingElement`](kerml/AnnotatingElement.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Annotations](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Annotation](kerml/Annotation.html)`
`[annotate](#annotate(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement))([Element](kerml/Element.html) annotatedElement,
 [AnnotatingElement](kerml/AnnotatingElement.html) annotatingElement)`
Creates a new [`Annotation`](kerml/Annotation.html) linking the annotating element to the
 annotated element.
`static [Annotation](kerml/Annotation.html)`
`[annotateAsOwned](#annotateAsOwned(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement))([Element](kerml/Element.html) annotatedElement,
 [AnnotatingElement](kerml/AnnotatingElement.html) annotatingElement)`
Creates or reuses an [`Annotation`](kerml/Annotation.html) to annotate the given element as
 an owned annotation of the annotating element.
`static boolean`
`[canAnnotateAsOwned](#canAnnotateAsOwned(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass annotatedElementEClass)`
Checks whether the given element type can be annotated as an owned annotation.
`static <T extends [AnnotatingElement](kerml/AnnotatingElement.html)> 
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T>`
`[getAnnotatingElement](#getAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean,boolean))([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> filter,
 boolean includeOwned,
 boolean includeExternallyDefined)`
Returns all annotating elements of the given element that match the filter.
`static boolean`
`[isAnnotatingElement](#isAnnotatingElement(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents an [`AnnotatingElement`](kerml/AnnotatingElement.html).
`static boolean`
`[isApplicableAnnotatedElement](#isApplicableAnnotatedElement(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given element type is allowed to be annotated.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Annotations
public Annotations()
 ============ METHOD DETAIL ========== 
Method Details
isAnnotatingElement
public static boolean isAnnotatingElement(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents an [`AnnotatingElement`](kerml/AnnotatingElement.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is an annotating element
annotate
public static [Annotation](kerml/Annotation.html) annotate([Element](kerml/Element.html) annotatedElement,
 [AnnotatingElement](kerml/AnnotatingElement.html) annotatingElement)
Creates a new [`Annotation`](kerml/Annotation.html) linking the annotating element to the
 annotated element. The annotation is added as an owned relationship of
 the annotating element.
Parameters:
`annotatedElement` - the element being annotated
`annotatingElement` - the element providing the annotation
Returns:
created annotation
canAnnotateAsOwned
public static boolean canAnnotateAsOwned(org.eclipse.emf.ecore.EClass annotatedElementEClass)
Checks whether the given element type can be annotated as an owned annotation.
 Owned annotations cannot be applied to metadata features, associations,
 connectors, or other disallowed element types.
Parameters:
`annotatedElementEClass` - the class of the element being annotated
Returns:
true if the element can be annotated as owned
annotateAsOwned
public static [Annotation](kerml/Annotation.html) annotateAsOwned([Element](kerml/Element.html) annotatedElement,
 [AnnotatingElement](kerml/AnnotatingElement.html) annotatingElement)
Creates or reuses an [`Annotation`](kerml/Annotation.html) to annotate the given element as
 an owned annotation of the annotating element. If the annotating element
 is already owned by an annotation, that annotation is reused.
Parameters:
`annotatedElement` - the element being annotated
`annotatingElement` - the annotating element
Returns:
the annotation used or created
getAnnotatingElement
public static <T extends [AnnotatingElement](kerml/AnnotatingElement.html)> [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<T> getAnnotatingElement([Element](kerml/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> filter,
 boolean includeOwned,
 boolean includeExternallyDefined)
Returns all annotating elements of the given element that match the filter.
 Results may include:
 Owned annotations
Annotating elements owned as members of a namespace
Externally defined annotating elements
Type Parameters:
`T` - annotating element type
Parameters:
`element` - the element being annotated
`filter` - class filter for annotating elements
`includeOwned` - whether to include owned annotating elements
`includeExternallyDefined` - whether to include externally defined annotating elements
Returns:
list of matching annotating elements
isApplicableAnnotatedElement
public static boolean isApplicableAnnotatedElement(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given element type is allowed to be annotated.
 Certain element types (e.g., specializations, owning memberships,
 feature chainings, conjugations, type featuring, and annotations)
 cannot be annotated.
Parameters:
`eClass` - the class to check
Returns:
true if the element type is applicable for annotation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Annotations">Class Annotations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Annotations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Annotations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a> and <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AnnotatingElement</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Annotations</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#annotate(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">annotate</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> annotatedElement,
 <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> annotatingElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a> linking the annotating element to the
 annotated element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#annotateAsOwned(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">annotateAsOwned</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> annotatedElement,
 <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> annotatingElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates or reuses an <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a> to annotate the given element as
 an owned annotation of the annotating element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#canAnnotateAsOwned(org.eclipse.emf.ecore.EClass)">canAnnotateAsOwned</a><wbr/>(org.eclipse.emf.ecore.EClass annotatedElementEClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element type can be annotated as an owned annotation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean,boolean)">getAnnotatingElement</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; filter,
 boolean includeOwned,
 boolean includeExternallyDefined)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all annotating elements of the given element that match the filter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnnotatingElement(org.eclipse.emf.ecore.EClass)">isAnnotatingElement</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents an <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AnnotatingElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isApplicableAnnotatedElement(org.eclipse.emf.ecore.EClass)">isApplicableAnnotatedElement</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element type is allowed to be annotated.</div>
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
<h3>Annotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Annotations</span>()</div>
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
<section class="detail" id="isAnnotatingElement(org.eclipse.emf.ecore.EClass)">
<h3>isAnnotatingElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnnotatingElement</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents an <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>AnnotatingElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is an annotating element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="annotate(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">
<h3>annotate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></span> <span class="element-name">annotate</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> annotatedElement,
 <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> annotatingElement)</span></div>
<div class="block">Creates a new <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a> linking the annotating element to the
 annotated element. The annotation is added as an owned relationship of
 the annotating element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotatedElement</code> - the element being annotated</dd>
<dd><code>annotatingElement</code> - the element providing the annotation</dd>
<dt>Returns:</dt>
<dd>created annotation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAnnotateAsOwned(org.eclipse.emf.ecore.EClass)">
<h3>canAnnotateAsOwned</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">canAnnotateAsOwned</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass annotatedElementEClass)</span></div>
<div class="block">Checks whether the given element type can be annotated as an owned annotation.
 Owned annotations cannot be applied to metadata features, associations,
 connectors, or other disallowed element types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotatedElementEClass</code> - the class of the element being annotated</dd>
<dt>Returns:</dt>
<dd>true if the element can be annotated as owned</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="annotateAsOwned(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">
<h3>annotateAsOwned</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Annotation</a></span> <span class="element-name">annotateAsOwned</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> annotatedElement,
 <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> annotatingElement)</span></div>
<div class="block">Creates or reuses an <a href="kerml/Annotation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Annotation</code></a> to annotate the given element as
 an owned annotation of the annotating element. If the annotating element
 is already owned by an annotation, that annotation is reused.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotatedElement</code> - the element being annotated</dd>
<dd><code>annotatingElement</code> - the annotating element</dd>
<dt>Returns:</dt>
<dd>the annotation used or created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.lang.Class,boolean,boolean)">
<h3>getAnnotatingElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">getAnnotatingElement</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; filter,
 boolean includeOwned,
 boolean includeExternallyDefined)</span></div>
<div class="block">Returns all annotating elements of the given element that match the filter.
 Results may include:
 <ul>
<li>Owned annotations</li>
<li>Annotating elements owned as members of a namespace</li>
<li>Externally defined annotating elements</li>
</ul></div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - annotating element type</dd>
<dt>Parameters:</dt>
<dd><code>element</code> - the element being annotated</dd>
<dd><code>filter</code> - class filter for annotating elements</dd>
<dd><code>includeOwned</code> - whether to include owned annotating elements</dd>
<dd><code>includeExternallyDefined</code> - whether to include externally defined annotating elements</dd>
<dt>Returns:</dt>
<dd>list of matching annotating elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isApplicableAnnotatedElement(org.eclipse.emf.ecore.EClass)">
<h3>isApplicableAnnotatedElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isApplicableAnnotatedElement</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given element type is allowed to be annotated.
 Certain element types (e.g., specializations, owning memberships,
 feature chainings, conjugations, type featuring, and annotations)
 cannot be annotated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the element type is applicable for annotation</dd>
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
