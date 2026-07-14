# JAVA OPENAPI: Refactoring.Converting (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/Refactoring.Converting.html
- source_path: `com/nomagic/magicdraw/uml/Refactoring.Converting.html`
- source_sha256: `ab17300e2ae54b7ea9a24aa78124efa1979c8f4355c45435875b68722e0ee664`
- captured_utc: `2026-07-14T16:52:07.833823+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Refactoring.Converting

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Refactoring.Converting

Enclosing class:
[Refactoring](Refactoring.html)

@OpenApiAllpublic static classRefactoring.Converting
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Converts elements in the model.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Converting](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[convert](#convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 [ConvertElementInfo](ConvertElementInfo.html) info)`
Converts given element according given conversion info.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[convert](#convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [ConvertElementInfo](ConvertElementInfo.html) info)`
Converts element with another element according given conversion info.
`static [ShapeElement](symbols/shapes/ShapeElement.html)`
`[convertCommentToNote](#convertCommentToNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](symbols/shapes/ShapeElement.html) comment)`
Converts Comment into Note.
`static [ShapeElement](symbols/shapes/ShapeElement.html)`
`[convertNoteToComment](#convertNoteToComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([ShapeElement](symbols/shapes/ShapeElement.html) note,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) commentStereotype)`
Converts Note into Comment.
`static [PartView](symbols/shapes/PartView.html)`
`[convertPortToPart](#convertPortToPart(com.nomagic.magicdraw.uml.symbols.shapes.PortView))([PortView](symbols/shapes/PortView.html) portView)`
Converts Port symbol to Part symbol
`static [PartView](symbols/shapes/PartView.html)`
`[convertPortToPartAndRemovePortSymbol](#convertPortToPartAndRemovePortSymbol(com.nomagic.magicdraw.uml.symbols.shapes.PortView))([PortView](symbols/shapes/PortView.html) portView)`
Convert port symbol to part symbol by creating new part symbol for port element
 After that remove unused port symbol
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Converting
public Converting()
 ============ METHOD DETAIL ========== 
Method Details
convert
public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) convert([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 [ConvertElementInfo](ConvertElementInfo.html) info)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Converts given element according given conversion info.
Parameters:
`source` - element to convert.
`info` - conversion rules.
Returns:
newly created element after conversion, null if conversion didn't succeed.
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given element is not editable (read-only).
convert
public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) convert([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) source,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [ConvertElementInfo](ConvertElementInfo.html) info)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Converts element with another element according given conversion info.
Parameters:
`source` - element to convert.
`target` - element with which to convert, can be null, in this case a new element will be created.
`info` - conversion rules.
Returns:
target element.
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given element is not editable (read-only).
convertNoteToComment
public static [ShapeElement](symbols/shapes/ShapeElement.html) convertNoteToComment([ShapeElement](symbols/shapes/ShapeElement.html) note,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) commentStereotype)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Converts Note into Comment.
Parameters:
`note` - note shape
`commentStereotype` - apply given stereotypes to created Comment
Returns:
Comment shape
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given Note symbol is not editable (read-only) or diagram owner is not editable
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given symbol is not a Note symbol
convertCommentToNote
public static [ShapeElement](symbols/shapes/ShapeElement.html) convertCommentToNote([ShapeElement](symbols/shapes/ShapeElement.html) comment)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Converts Comment into Note.
Parameters:
`comment` - comment shape
Returns:
Note shape
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given Comment symbol is not editable (read-only) or Comment is not editable
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given symbol is not a Comment symbol
convertPortToPartAndRemovePortSymbol
public static [PartView](symbols/shapes/PartView.html) convertPortToPartAndRemovePortSymbol([PortView](symbols/shapes/PortView.html) portView)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Convert port symbol to part symbol by creating new part symbol for port element
 After that remove unused port symbol
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)`
convertPortToPart
public static [PartView](symbols/shapes/PartView.html) convertPortToPart([PortView](symbols/shapes/PortView.html) portView)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Converts Port symbol to Part symbol
Parameters:
`portView` - port symbol
Returns:
part symbol
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given port symbol is not editable (read-only)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Refactoring.Converting">Class Refactoring.Converting</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Refactoring.Converting</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="Refactoring.html" title="class in com.nomagic.magicdraw.uml">Refactoring</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">Refactoring.Converting</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Converts elements in the model.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Converting</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">convert</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts given element according given conversion info.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">convert</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts element with another element according given conversion info.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertCommentToNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">convertCommentToNote</a><wbr/>(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> comment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts Comment into Note.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertNoteToComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">convertNoteToComment</a><wbr/>(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> note,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> commentStereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts Note into Comment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertPortToPart(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">convertPortToPart</a><wbr/>(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> portView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts Port symbol to Part symbol</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertPortToPartAndRemovePortSymbol(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">convertPortToPartAndRemovePortSymbol</a><wbr/>(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> portView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert port symbol to part symbol by creating new part symbol for port element
 After that remove unused port symbol</div>
</div>
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
<h3>Converting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Converting</span>()</div>
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
<section class="detail" id="convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</span>
                       throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Converts given element according given conversion info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - element to convert.</dd>
<dd><code>info</code> - conversion rules.</dd>
<dt>Returns:</dt>
<dd>newly created element after conversion, null if conversion didn't succeed.</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable (read-only).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> source,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</span>
                       throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Converts element with another element according given conversion info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - element to convert.</dd>
<dd><code>target</code> - element with which to convert, can be null, in this case a new element will be created.</dd>
<dd><code>info</code> - conversion rules.</dd>
<dt>Returns:</dt>
<dd>target element.</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable (read-only).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertNoteToComment(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>convertNoteToComment</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">convertNoteToComment</span><wbr/><span class="parameters">(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> note,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> commentStereotype)</span>
                                         throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Converts Note into Comment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>note</code> - note shape</dd>
<dd><code>commentStereotype</code> - apply given stereotypes to created Comment</dd>
<dt>Returns:</dt>
<dd>Comment shape</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given Note symbol is not editable (read-only) or diagram owner is not editable</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given symbol is not a Note symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertCommentToNote(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>convertCommentToNote</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">convertCommentToNote</span><wbr/><span class="parameters">(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> comment)</span>
                                         throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Converts Comment into Note.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>comment</code> - comment shape</dd>
<dt>Returns:</dt>
<dd>Note shape</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given Comment symbol is not editable (read-only) or Comment is not editable</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given symbol is not a Comment symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertPortToPartAndRemovePortSymbol(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">
<h3>convertPortToPartAndRemovePortSymbol</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></span> <span class="element-name">convertPortToPartAndRemovePortSymbol</span><wbr/><span class="parameters">(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> portView)</span>
                                                     throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Convert port symbol to part symbol by creating new part symbol for port element
 After that remove unused port symbol</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertPortToPart(com.nomagic.magicdraw.uml.symbols.shapes.PortView)">
<h3>convertPortToPart</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="symbols/shapes/PartView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PartView</a></span> <span class="element-name">convertPortToPart</span><wbr/><span class="parameters">(<a href="symbols/shapes/PortView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">PortView</a> portView)</span>
                                  throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Converts Port symbol to Part symbol</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>portView</code> - port symbol</dd>
<dt>Returns:</dt>
<dd>part symbol</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given port symbol is not editable (read-only)</dd>
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
