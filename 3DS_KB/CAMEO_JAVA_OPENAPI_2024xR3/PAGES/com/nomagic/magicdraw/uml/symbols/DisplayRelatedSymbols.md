# JAVA OPENAPI: DisplayRelatedSymbols (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/DisplayRelatedSymbols.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DisplayRelatedSymbols.html`
- source_sha256: `f87e752fd65937b380da948865c36059b115e1b2e3e03b7084e47f8db09d56f4`
- captured_utc: `2026-07-14T16:55:55.910464+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DisplayRelatedSymbols

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbols

@OpenApiAllpublic classDisplayRelatedSymbols
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Provides API to the display related symbols functionality.
MagicDraw allows displaying symbols that are related to a given symbol via relationships.
 The [`DisplayRelatedSymbols`](DisplayRelatedSymbols.html) class provides API methods for this.
 Using this class you can control any of the following behaviors for displaying related symbols logic:
What relationship types should be included.
 Depth of a relationship tree.
 Whether or not existing symbols should be reused.
 Example: Displaying related generalizations and interface realizations
SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Display related");

 Set linkTypes = new HashSet();
 linkTypes.add(new LinkType(Generalization.class));
 linkTypes.add(new LinkType(InterfaceRealization.class));

 DisplayRelatedSymbolsInfo info = new DisplayRelatedSymbolsInfo(linkTypes);
 info.setDepthLimited(true);
 info.setDepthLimit(3);

 PresentationElement view = ...; // A symbol for which you need to invoke the displaying related symbols action.

 DisplayRelatedSymbols.displayRelatedSymbols(view, info);

 **//For multiple symbol selection to display related symbols use the code below**
 List**<**PresentationElement> viewList = ...; //List of symbols for which you need to invoke the displaying related symbols action.

 DisplayRelatedSymbols.displayRelatedSymbols(viewList, info);

 sessionManager.closeSession();

See Also:
[`DisplayRelatedSymbolsInfo`](DisplayRelatedSymbolsInfo.html)
[`LinkType`](LinkType.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DisplayRelatedSymbols](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[displayRelatedSymbols](#displayRelatedSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo))([PresentationElement](PresentationElement.html) view,
 [DisplayRelatedSymbolsInfo](DisplayRelatedSymbolsInfo.html) info)`
Displays related symbols for a given symbol.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[displayRelatedSymbols](#displayRelatedSymbols(java.util.List,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> viewList,
 [DisplayRelatedSymbolsInfo](DisplayRelatedSymbolsInfo.html) info)`
Displays related symbols for given multiple symbols.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)>`
`[getPossibleLinkTypes](#getPossibleLinkTypes(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) pe)`
Given a symbol, gets all relationship types which it has in the model.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DisplayRelatedSymbols
public DisplayRelatedSymbols()
 ============ METHOD DETAIL ========== 
Method Details
displayRelatedSymbols
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> displayRelatedSymbols([PresentationElement](PresentationElement.html) view,
 [DisplayRelatedSymbolsInfo](DisplayRelatedSymbolsInfo.html) info)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Displays related symbols for a given symbol.
Parameters:
`view` - symbol for which to display related symbols.
`info` - configuration of display related behavior.
Returns:
symbols which were displayed successfully.
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if given element is not editable (read-only).
displayRelatedSymbols
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> displayRelatedSymbols([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> viewList,
 [DisplayRelatedSymbolsInfo](DisplayRelatedSymbolsInfo.html) info)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Displays related symbols for given multiple symbols.
Parameters:
`viewList` - symbol list for which to display related symbols.
`info` - configuration of display related behavior.
Returns:
symbols which were displayed successfully.
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if given element is not editable (read-only).
getPossibleLinkTypes
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> getPossibleLinkTypes([PresentationElement](PresentationElement.html) pe)
Given a symbol, gets all relationship types which it has in the model.
Parameters:
`pe` - symbol for which to retrieve possible relationship types
Returns:
possible relationship types for a given symbol

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DisplayRelatedSymbols">Class DisplayRelatedSymbols</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbols</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DisplayRelatedSymbols</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Provides API to the display related symbols functionality.
 </p>
<p>
<p>
 MagicDraw allows displaying symbols that are related to a given symbol via relationships.
 The <a href="DisplayRelatedSymbols.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DisplayRelatedSymbols</code></a> class provides API methods for this.
 Using this class you can control any of the following behaviors for displaying related symbols logic:
 </p>
<ul>
<li> What relationship types should be included.
 <li> Depth of a relationship tree.
 <li> Whether or not existing symbols should be reused.
 <ul>
<p>
<h4>Example: Displaying related generalizations and interface realizations</h4>
<pre>
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Display related");

 Set linkTypes = new HashSet();
 linkTypes.add(new LinkType(Generalization.class));
 linkTypes.add(new LinkType(InterfaceRealization.class));

 DisplayRelatedSymbolsInfo info = new DisplayRelatedSymbolsInfo(linkTypes);
 info.setDepthLimited(true);
 info.setDepthLimit(3);

 PresentationElement view = ...; // A symbol for which you need to invoke the displaying related symbols action.

 DisplayRelatedSymbols.displayRelatedSymbols(view, info);

 <b>//For multiple symbol selection to display related symbols use the code below</b>
 List<b>&lt;</b>PresentationElement&gt; viewList = ...; //List of symbols for which you need to invoke the displaying related symbols action.

 DisplayRelatedSymbols.displayRelatedSymbols(viewList, info);

 sessionManager.closeSession();
 </pre></p></ul></li></li></li></ul></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DisplayRelatedSymbolsInfo.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DisplayRelatedSymbolsInfo</code></a></li>
<li><a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>LinkType</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DisplayRelatedSymbols</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayRelatedSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo)">displayRelatedSymbols</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="DisplayRelatedSymbolsInfo.html" title="class in com.nomagic.magicdraw.uml.symbols">DisplayRelatedSymbolsInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays related symbols for a given symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayRelatedSymbols(java.util.List,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo)">displayRelatedSymbols</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; viewList,
 <a href="DisplayRelatedSymbolsInfo.html" title="class in com.nomagic.magicdraw.uml.symbols">DisplayRelatedSymbolsInfo</a> info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays related symbols for given multiple symbols.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPossibleLinkTypes(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPossibleLinkTypes</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a symbol, gets all relationship types which it has in the model.</div>
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
<h3>DisplayRelatedSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DisplayRelatedSymbols</span>()</div>
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
<section class="detail" id="displayRelatedSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo)">
<h3>displayRelatedSymbols</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">displayRelatedSymbols</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="DisplayRelatedSymbolsInfo.html" title="class in com.nomagic.magicdraw.uml.symbols">DisplayRelatedSymbolsInfo</a> info)</span>
                                                             throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Displays related symbols for a given symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol for which to display related symbols.</dd>
<dd><code>info</code> - configuration of display related behavior.</dd>
<dt>Returns:</dt>
<dd>symbols which were displayed successfully.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable (read-only).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="displayRelatedSymbols(java.util.List,com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo)">
<h3>displayRelatedSymbols</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">displayRelatedSymbols</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; viewList,
 <a href="DisplayRelatedSymbolsInfo.html" title="class in com.nomagic.magicdraw.uml.symbols">DisplayRelatedSymbolsInfo</a> info)</span>
                                                             throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Displays related symbols for given multiple symbols.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>viewList</code> - symbol list for which to display related symbols.</dd>
<dd><code>info</code> - configuration of display related behavior.</dd>
<dt>Returns:</dt>
<dd>symbols which were displayed successfully.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable (read-only).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPossibleLinkTypes(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getPossibleLinkTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt;</span> <span class="element-name">getPossibleLinkTypes</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</span></div>
<div class="block">Given a symbol, gets all relationship types which it has in the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pe</code> - symbol for which to retrieve possible relationship types</dd>
<dt>Returns:</dt>
<dd>possible relationship types for a given symbol</dd>
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
