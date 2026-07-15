# JAVA OPENAPI: AnnotationTargetParentProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/annotation/AnnotationTargetParentProvider.html
- source_path: `com/nomagic/magicdraw/annotation/AnnotationTargetParentProvider.html`
- source_sha256: `4f687cdfa568ec6d518569198159b52ec2bf7670199a2329e68de6117d9d547d`
- captured_utc: `2026-07-14T16:51:01.627946+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Interface AnnotationTargetParentProvider

@OpenApiAllpublic interfaceAnnotationTargetParentProvider

When retrieving annotations by a target object in [`AnnotationManager`](AnnotationManager.html), annotations of parent targets are also included (recursively).
 Implementations of this interface can define what is the parent target for some target object.
 Each implementation has to be registered by calling [`AnnotationManager.addAnnotationParentTargetProvider(AnnotationTargetParentProvider)`](AnnotationManager.html#addAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)).

 
 
Example: if [`AnnotationManager.getAnnotations(java.lang.Object)`](AnnotationManager.html#getAnnotations(java.lang.Object)) is called for for a [`ClassView`](../uml/symbols/shapes/ClassView.html) symbol
 then annotations whose [`Annotation.getTargetObject()`](Annotation.html#getTargetObject()) is the symbol's [`Class`](../../uml2/ext/magicdraw/classes/mdkernel/Class.html) element will also be included.

See Also:
[`AnnotationManager`](AnnotationManager.html)
[`Annotation`](Annotation.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[accept](#accept(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`

`void`
`[cleanup](#cleanup(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) closedProject)`
Called after project is closed to clean any project specific caches
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getParent](#getParent(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`
This method is called each time annotations are requested for **any** target in [`AnnotationManager`](AnnotationManager.html) and that happens constantly.
`[Project](../core/Project.html)`
`[getProject](#getProject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`
Project for the custom target is required to clean up the added annotations when the project is closed

============ METHOD DETAIL ========== 
Method Details
accept
boolean accept([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
getParent
@CheckForNull[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getParent([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
This method is called each time annotations are requested for **any** target in [`AnnotationManager`](AnnotationManager.html) and that happens constantly.
 So implementations of this method should be fast and avoid new object creation. 
 


 It is legal to return the same instance of the parent object for different targets. In fact, core implementations does this - uses the same instance
 but uses setters to change the object for each call.
 For that reason the returned parent objects are not and should not be cached/stored. They are only for momentary use and are in a thread safe manner used
 as key to retrieve annotations from a [`HashSet`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html).
Parameters:
`target` - annotation target
getProject
@CheckForNull[Project](../core/Project.html) getProject([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
Project for the custom target is required to clean up the added annotations when the project is closed
cleanup
void cleanup([Project](../core/Project.html) closedProject)
Called after project is closed to clean any project specific caches

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Interface AnnotationTargetParentProvider">Interface AnnotationTargetParentProvider</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AnnotationTargetParentProvider</span></div>
<div class="block">When retrieving annotations by a target object in <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationManager</code></a>, annotations of parent targets are also included (recursively).
 Implementations of this interface can define what is the parent target for some target object.
 Each implementation has to be registered by calling <a href="AnnotationManager.html#addAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)"><code>AnnotationManager.addAnnotationParentTargetProvider(AnnotationTargetParentProvider)</code></a>.

 <br/><br/>Example: if <a href="AnnotationManager.html#getAnnotations(java.lang.Object)"><code>AnnotationManager.getAnnotations(java.lang.Object)</code></a> is called for for a <a href="../uml/symbols/shapes/ClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes"><code>ClassView</code></a> symbol
 then annotations whose <a href="Annotation.html#getTargetObject()"><code>Annotation.getTargetObject()</code></a> is the symbol's <a href="../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Class</code></a> element will also be included.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationManager</code></a></li>
<li><a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation"><code>Annotation</code></a></li>
</ul>
</dd>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(java.lang.Object)">accept</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#cleanup(com.nomagic.magicdraw.core.Project)">cleanup</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> closedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after project is closed to clean any project specific caches</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParent(java.lang.Object)">getParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called each time annotations are requested for <strong>any</strong> target in <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationManager</code></a> and that happens constantly.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProject(java.lang.Object)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Project for the custom target is required to clean up the added annotations when the project is closed</div>
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
<section class="detail" id="accept(java.lang.Object)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
</section>
</li>
<li>
<section class="detail" id="getParent(java.lang.Object)">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<div class="block">This method is called each time annotations are requested for <strong>any</strong> target in <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationManager</code></a> and that happens constantly.
 So implementations of this method should be fast and avoid new object creation.<br/><br/>

 It is legal to return the same instance of the parent object for different targets. In fact, core implementations does this - uses the same instance
 but uses setters to change the object for each call.
 For that reason the returned parent objects are not and should not be cached/stored. They are only for momentary use and are in a thread safe manner used
 as key to retrieve annotations from a <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html" title="class or interface in java.util"><code>HashSet</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - annotation target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.lang.Object)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<div class="block">Project for the custom target is required to clean up the added annotations when the project is closed</div>
</section>
</li>
<li>
<section class="detail" id="cleanup(com.nomagic.magicdraw.core.Project)">
<h3>cleanup</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">cleanup</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> closedProject)</span></div>
<div class="block">Called after project is closed to clean any project specific caches</div>
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
