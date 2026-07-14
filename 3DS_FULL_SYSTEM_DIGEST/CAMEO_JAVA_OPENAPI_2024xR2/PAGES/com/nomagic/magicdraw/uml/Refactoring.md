# JAVA OPENAPI: Refactoring (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/Refactoring.html
- source_path: `com/nomagic/magicdraw/uml/Refactoring.html`
- source_sha256: `23ede3ca0761d246351789ae1809ae687417ffb36afa638895bb15751da0810a`
- captured_utc: `2026-07-14T16:55:53.971442+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Refactoring

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Refactoring

@OpenApiAllpublic classRefactoring
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

To refactor an element in a model, use the [`Refactoring`](Refactoring.html) class.
Example 1: Converting an element to an interface
Element elementToConvert = ...;
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Convert");

 // Converts the element to an interface.
 ConvertElementInfo info = new ConvertElementInfo(Interface.class);

 // Preserves the old element ID for the new element.
 info.setPreserveElementID(true);

 Element conversionTarget = Refactoring.Converting.convert(elementToConvert, info);

 sessionManager.closeSession();
Example 2: Replacing an element with another element
Element elementToReplace = ...;

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Replace");

 ConvertElementInfo info = new ConvertElementInfo(elementToReplace.getClassType());
 info.setConvertOnlyIncomingReferences(true);

 Refactoring.Replacing.replace(element, elementToReplace, info);

 sessionManager.closeSession();

See Also:
[`ConvertElementInfo`](ConvertElementInfo.html)
[`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
[`SessionManager`](../openapi/uml/SessionManager.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[Refactoring.Converting](Refactoring.Converting.html)`
Converts elements in the model.
`static class`
`[Refactoring.Extracting](Refactoring.Extracting.html)`
Extracts part of the model into a new reusable piece of model.
`static class`
`[Refactoring.Moving](Refactoring.Moving.html)`
Moves elements in model to a new owner element with or without connected relations
 An example how to move elements together with their relations:
`static final class`
`[Refactoring.RelationReconnecting](Refactoring.RelationReconnecting.html)`
Reconnects one relation so that it skips selected part of the model.
`static class`
`[Refactoring.RelationReversing](Refactoring.RelationReversing.html)`
Reverses direction of a relationship.
`static class`
`[Refactoring.Replacing](Refactoring.Replacing.html)`
Replaces elements in the model.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Refactoring](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Refactoring
public Refactoring()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Refactoring">Class Refactoring</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Refactoring</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Refactoring</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 To refactor an element in a model, use the <a href="Refactoring.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring</code></a> class.
 </p>
<p>
<h4>Example 1: Converting an element to an interface</h4>
<pre>
 Element elementToConvert = ...;
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Convert");

 // Converts the element to an interface.
 ConvertElementInfo info = new ConvertElementInfo(Interface.class);

 // Preserves the old element ID for the new element.
 info.setPreserveElementID(true);

 Element conversionTarget = Refactoring.Converting.convert(elementToConvert, info);

 sessionManager.closeSession();
 </pre>
<h4>Example 2: Replacing an element with another element</h4>
<pre>
 Element elementToReplace = ...;

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Replace");

 ConvertElementInfo info = new ConvertElementInfo(elementToReplace.getClassType());
 info.setConvertOnlyIncomingReferences(true);

 Refactoring.Replacing.replace(element, elementToReplace, info);

 sessionManager.closeSession();
 </pre></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml"><code>ConvertElementInfo</code></a></li>
<li><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></li>
<li><a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Refactoring.Converting.html" title="class in com.nomagic.magicdraw.uml">Refactoring.Converting</a></code></div>
<div class="col-last even-row-color">
<div class="block">Converts elements in the model.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Refactoring.Extracting.html" title="class in com.nomagic.magicdraw.uml">Refactoring.Extracting</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Extracts part of the model into a new reusable piece of model.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Refactoring.Moving.html" title="class in com.nomagic.magicdraw.uml">Refactoring.Moving</a></code></div>
<div class="col-last even-row-color">
<div class="block">Moves elements in model to a new owner element with or without connected relations
 An example how to move elements together with their relations:</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Refactoring.RelationReconnecting.html" title="class in com.nomagic.magicdraw.uml">Refactoring.RelationReconnecting</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Reconnects one relation so that it skips selected part of the model.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Refactoring.RelationReversing.html" title="class in com.nomagic.magicdraw.uml">Refactoring.RelationReversing</a></code></div>
<div class="col-last even-row-color">
<div class="block">Reverses direction of a relationship.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Refactoring.Replacing.html" title="class in com.nomagic.magicdraw.uml">Refactoring.Replacing</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Replaces elements in the model.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Refactoring</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
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
<h3>Refactoring</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Refactoring</span>()</div>
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
