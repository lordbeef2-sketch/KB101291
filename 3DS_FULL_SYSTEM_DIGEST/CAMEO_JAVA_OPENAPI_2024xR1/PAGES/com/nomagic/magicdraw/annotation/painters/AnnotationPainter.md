# JAVA OPENAPI: AnnotationPainter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/annotation/painters/AnnotationPainter.html
- source_path: `com/nomagic/magicdraw/annotation/painters/AnnotationPainter.html`
- source_sha256: `cccef2abd4fdee40f7d5f700429cd33b3f50fdd8e8b0d0f5c0a388278fe011ff`
- captured_utc: `2026-07-14T16:51:01.633943+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation.painters](package-summary.html)

## Interface AnnotationPainter

@OpenApiAllpublic interfaceAnnotationPainter
An interface for annotation painter.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[disposeOn](#disposeOn(com.nomagic.magicdraw.annotation.Annotation))([Annotation](../Annotation.html) annotation)`
Dispose this painter on the given annotation.
`boolean`
`[isSuitable](#isSuitable(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`
Check if this painter is suitable to paint annotation on the given target
`void`
`[paint](#paint(com.nomagic.magicdraw.annotation.Annotation,java.awt.Graphics2D,java.lang.Object))([Annotation](../Annotation.html) annotation,
 [Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`
Paint annotation

============ METHOD DETAIL ========== 
Method Details
isSuitable
boolean isSuitable([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
Check if this painter is suitable to paint annotation on the given target
Parameters:
`target` - target object
Returns:
true if painter should be used to paint the annotation
paint
void paint([Annotation](../Annotation.html) annotation,
 [Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
Paint annotation
Parameters:
`annotation` - annotation
`g` - graphics
`target` - target object
disposeOn
void disposeOn([Annotation](../Annotation.html) annotation)
Dispose this painter on the given annotation. This method is called if painter is replaced on Annotation.
Parameters:
`annotation` - annotation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation.painters</a></div>
<h1 class="title" title="Interface AnnotationPainter">Interface AnnotationPainter</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AnnotationPainter</span></div>
<div class="block">An interface for annotation painter.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#disposeOn(com.nomagic.magicdraw.annotation.Annotation)">disposeOn</a><wbr/>(<a href="../Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Dispose this painter on the given annotation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSuitable(java.lang.Object)">isSuitable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if this painter is suitable to paint annotation on the given target</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#paint(com.nomagic.magicdraw.annotation.Annotation,java.awt.Graphics2D,java.lang.Object)">paint</a><wbr/>(<a href="../Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Paint annotation</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="isSuitable(java.lang.Object)">
<h3>isSuitable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSuitable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<div class="block">Check if this painter is suitable to paint annotation on the given target</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target object</dd>
<dt>Returns:</dt>
<dd>true if painter should be used to paint the annotation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paint(com.nomagic.magicdraw.annotation.Annotation,java.awt.Graphics2D,java.lang.Object)">
<h3>paint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">paint</span><wbr/><span class="parameters">(<a href="../Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<div class="block">Paint annotation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation</dd>
<dd><code>g</code> - graphics</dd>
<dd><code>target</code> - target object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeOn(com.nomagic.magicdraw.annotation.Annotation)">
<h3>disposeOn</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">disposeOn</span><wbr/><span class="parameters">(<a href="../Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</span></div>
<div class="block">Dispose this painter on the given annotation. This method is called if painter is replaced on Annotation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation</dd>
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
