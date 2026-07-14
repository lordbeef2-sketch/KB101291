# JAVA OPENAPI: ElementReferencingInTexts (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/elementreferenceintext/ElementReferencingInTexts.html
- source_path: `com/nomagic/magicdraw/elementreferenceintext/ElementReferencingInTexts.html`
- source_sha256: `934af8a00f23b4e62a365efb3beafc8236720c1ce0b880878758c09871116993`
- captured_utc: `2026-07-14T16:51:18.280165+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.elementreferenceintext](package-summary.html)

## Class ElementReferencingInTexts

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.elementreferenceintext.ElementReferencingInTexts

@OpenApiAllpublic classElementReferencingInTexts
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class responsible for creating rich texts(with references to other elements).
 For more information on usage refer to the examples.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementReferencingInTexts](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReferencingText](#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Creates text referencing an element using default settings([`DisplayMode.CUSTOM_TEXT`](DisplayMode.html#CUSTOM_TEXT), [`UpdateMode.AUTOMATIC_UPDATE`](UpdateMode.html#AUTOMATIC_UPDATE))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReferencingText](#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode))([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [DisplayMode](DisplayMode.html) displayMode)`
Creates text referencing an element using provided display mode and [`UpdateMode.AUTOMATIC_UPDATE`](UpdateMode.html#AUTOMATIC_UPDATE) mode
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createReferencingText](#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode,com.nomagic.magicdraw.elementreferenceintext.UpdateMode))([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [DisplayMode](DisplayMode.html) display,
 [UpdateMode](UpdateMode.html) update)`
Creates text referencing an element using provided display mode and update mode
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getReferredElements](#getReferredElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) referringElement)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementReferencingInTexts
public ElementReferencingInTexts()
 ============ METHOD DETAIL ========== 
Method Details
createReferencingText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReferencingText([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Creates text referencing an element using default settings([`DisplayMode.CUSTOM_TEXT`](DisplayMode.html#CUSTOM_TEXT), [`UpdateMode.AUTOMATIC_UPDATE`](UpdateMode.html#AUTOMATIC_UPDATE))
Parameters:
`referencedElement` - element referenced in text
`text` - text to display
Returns:
text that refers provided element
createReferencingText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReferencingText([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [DisplayMode](DisplayMode.html) displayMode)
Creates text referencing an element using provided display mode and [`UpdateMode.AUTOMATIC_UPDATE`](UpdateMode.html#AUTOMATIC_UPDATE) mode
Parameters:
`referencedElement` - element referenced by text
`text` - text to display(only affective if display mode is [`DisplayMode.CUSTOM_TEXT`](DisplayMode.html#CUSTOM_TEXT))
`displayMode` - the reference display mode. Must not be null.
Returns:
text referring provided element
createReferencingText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createReferencingText([BaseElement](../uml/BaseElement.html) referencedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [DisplayMode](DisplayMode.html) display,
 [UpdateMode](UpdateMode.html) update)
Creates text referencing an element using provided display mode and update mode
Parameters:
`referencedElement` - element referenced by text
`text` - text to display
`display` - the reference display mode. Must not be null.
`update` - the reference update mode. Must not be null.
Returns:
text referring provided element
getReferredElements
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getReferredElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) referringElement)
Parameters:
`referringElement` - the element that is referring to other elements
Returns:
a collection of elements that are referred by provided element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.elementreferenceintext</a></div>
<h1 class="title" title="Class ElementReferencingInTexts">Class ElementReferencingInTexts</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.elementreferenceintext.ElementReferencingInTexts</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementReferencingInTexts</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class responsible for creating rich texts(with references to other elements).
 For more information on usage refer to the examples.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementReferencingInTexts</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">createReferencingText</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates text referencing an element using default settings(<a href="DisplayMode.html#CUSTOM_TEXT"><code>DisplayMode.CUSTOM_TEXT</code></a>, <a href="UpdateMode.html#AUTOMATIC_UPDATE"><code>UpdateMode.AUTOMATIC_UPDATE</code></a>)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode)">createReferencingText</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="DisplayMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">DisplayMode</a> displayMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates text referencing an element using provided display mode and <a href="UpdateMode.html#AUTOMATIC_UPDATE"><code>UpdateMode.AUTOMATIC_UPDATE</code></a> mode</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode,com.nomagic.magicdraw.elementreferenceintext.UpdateMode)">createReferencingText</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="DisplayMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">DisplayMode</a> display,
 <a href="UpdateMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">UpdateMode</a> update)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates text referencing an element using provided display mode and update mode</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferredElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getReferredElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> referringElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<h3>ElementReferencingInTexts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementReferencingInTexts</span>()</div>
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
<section class="detail" id="createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>createReferencingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReferencingText</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Creates text referencing an element using default settings(<a href="DisplayMode.html#CUSTOM_TEXT"><code>DisplayMode.CUSTOM_TEXT</code></a>, <a href="UpdateMode.html#AUTOMATIC_UPDATE"><code>UpdateMode.AUTOMATIC_UPDATE</code></a>)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referencedElement</code> - element referenced in text</dd>
<dd><code>text</code> - text to display</dd>
<dt>Returns:</dt>
<dd>text that refers provided element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode)">
<h3>createReferencingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReferencingText</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="DisplayMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">DisplayMode</a> displayMode)</span></div>
<div class="block">Creates text referencing an element using provided display mode and <a href="UpdateMode.html#AUTOMATIC_UPDATE"><code>UpdateMode.AUTOMATIC_UPDATE</code></a> mode</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referencedElement</code> - element referenced by text</dd>
<dd><code>text</code> - text to display(only affective if display mode is <a href="DisplayMode.html#CUSTOM_TEXT"><code>DisplayMode.CUSTOM_TEXT</code></a>)</dd>
<dd><code>displayMode</code> - the reference display mode. Must not be null.</dd>
<dt>Returns:</dt>
<dd>text referring provided element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReferencingText(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,com.nomagic.magicdraw.elementreferenceintext.DisplayMode,com.nomagic.magicdraw.elementreferenceintext.UpdateMode)">
<h3>createReferencingText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createReferencingText</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> referencedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="DisplayMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">DisplayMode</a> display,
 <a href="UpdateMode.html" title="enum class in com.nomagic.magicdraw.elementreferenceintext">UpdateMode</a> update)</span></div>
<div class="block">Creates text referencing an element using provided display mode and update mode</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referencedElement</code> - element referenced by text</dd>
<dd><code>text</code> - text to display</dd>
<dd><code>display</code> - the reference display mode. Must not be null.</dd>
<dd><code>update</code> - the reference update mode. Must not be null.</dd>
<dt>Returns:</dt>
<dd>text referring provided element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferredElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getReferredElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getReferredElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> referringElement)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referringElement</code> - the element that is referring to other elements</dd>
<dt>Returns:</dt>
<dd>a collection of elements that are referred by provided element</dd>
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
