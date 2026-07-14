# JAVA OPENAPI: HyperlinkEditor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/hyperlinks/ui/HyperlinkEditor.html
- source_path: `com/nomagic/magicdraw/hyperlinks/ui/HyperlinkEditor.html`
- source_sha256: `cec0fd9906ee23794fd53a90f43e6936b1d48658a704c9f18a0b709f92dc3e17`
- captured_utc: `2026-07-14T16:45:37.261497+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.hyperlinks.ui](package-summary.html)

## Interface HyperlinkEditor

All Known Implementing Classes:
`[HyperlinkEditorPanel](HyperlinkEditorPanel.html)`

@OpenApiAllpublic interfaceHyperlinkEditor

Hyperlink editor.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html)`
`[getComponent](#getComponent())()`
Get editor component.
`[Hyperlink](../Hyperlink.html)`
`[getHyperlink](#getHyperlink(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Get edited hyperlink.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`
Get editor title.
`boolean`
`[isProjectScope](#isProjectScope())()`
If edited hyperlink is of project scope.
`void`
`[setFavorites](#setFavorites(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Hyperlink](../Hyperlink.html)> favorites)`
Deprecated.
`void`
`[setHyperlink](#setHyperlink(com.nomagic.magicdraw.hyperlinks.Hyperlink))([Hyperlink](../Hyperlink.html) link)`
Set hyperlink to edit.
`default void`
`[setOptions](#setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions))([HyperlinkEditorOptions](HyperlinkEditorOptions.html) options)`
Set options which can be used in editor editor;

============ METHOD DETAIL ========== 
Method Details
getTitle
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTitle()
Get editor title.
Returns:
title string.
getComponent
[Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) getComponent()
Get editor component.
Returns:
component.
getHyperlink
@CheckForNull[Hyperlink](../Hyperlink.html) getHyperlink([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Get edited hyperlink.
Parameters:
`text` - hyperlink text.
Returns:
hyperlink.
setHyperlink
void setHyperlink([Hyperlink](../Hyperlink.html) link)
Set hyperlink to edit.
Parameters:
`link` - hyperlink.
setFavorites
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)void setFavorites([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Hyperlink](../Hyperlink.html)> favorites)
Deprecated.
Set favorite hyperlinks. Editor can show favorite hyperlinks.
 Deprecated
 Use [`setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions)`](#setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions))
Parameters:
`favorites` - favorite hyperlinks.
setOptions
default void setOptions(@CheckForNull
 [HyperlinkEditorOptions](HyperlinkEditorOptions.html) options)
Set options which can be used in editor editor;
Parameters:
`options` - hyperlink editor options
isProjectScope
boolean isProjectScope()
If edited hyperlink is of project scope. Used to calculate favorite hyperlinks storage - project hyperlink is stored in project, non project hyperlink is stored in environment.
Returns:
true if hyperlink is project specific, false - environment specific.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.hyperlinks.ui</a></div>
<h1 class="title" title="Interface HyperlinkEditor">Interface HyperlinkEditor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="HyperlinkEditorPanel.html" title="class in com.nomagic.magicdraw.hyperlinks.ui">HyperlinkEditorPanel</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">HyperlinkEditor</span></div>
<div class="block">Hyperlink editor.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getComponent()">getComponent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get editor component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHyperlink(java.lang.String)">getHyperlink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get edited hyperlink.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get editor title.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isProjectScope()">isProjectScope</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If edited hyperlink is of project scope.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#setFavorites(java.util.List)">setFavorites</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt; favorites)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setHyperlink(com.nomagic.magicdraw.hyperlinks.Hyperlink)">setHyperlink</a><wbr/>(<a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set hyperlink to edit.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions)">setOptions</a><wbr/>(<a href="HyperlinkEditorOptions.html" title="class in com.nomagic.magicdraw.hyperlinks.ui">HyperlinkEditorOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Set options which can be used in editor editor;</div>
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
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<div class="block">Get editor title.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>title string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComponent()">
<h3>getComponent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">getComponent</span>()</div>
<div class="block">Get editor component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHyperlink(java.lang.String)">
<h3>getHyperlink</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">getHyperlink</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Get edited hyperlink.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - hyperlink text.</dd>
<dt>Returns:</dt>
<dd>hyperlink.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHyperlink(com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>setHyperlink</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setHyperlink</span><wbr/><span class="parameters">(<a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</span></div>
<div class="block">Set hyperlink to edit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - hyperlink.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFavorites(java.util.List)">
<h3>setFavorites</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">setFavorites</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a>&gt; favorites)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set favorite hyperlinks. Editor can show favorite hyperlinks.
 <p>
 Deprecated
 Use <a href="#setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions)"><code>setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions)</code></a></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>favorites</code> - favorite hyperlinks.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOptions(com.nomagic.magicdraw.hyperlinks.ui.HyperlinkEditorOptions)">
<h3>setOptions</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">setOptions</span><wbr/><span class="parameters">(@CheckForNull
 <a href="HyperlinkEditorOptions.html" title="class in com.nomagic.magicdraw.hyperlinks.ui">HyperlinkEditorOptions</a> options)</span></div>
<div class="block">Set options which can be used in editor editor;</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - hyperlink editor options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectScope()">
<h3>isProjectScope</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isProjectScope</span>()</div>
<div class="block">If edited hyperlink is of project scope. Used to calculate favorite hyperlinks storage - project hyperlink is stored in project, non project hyperlink is stored in environment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if hyperlink is project specific, false - environment specific.</dd>
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
