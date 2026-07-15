# JAVA OPENAPI: LanguageBodyEditor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/languagebody/LanguageBodyEditor.html
- source_path: `com/nomagic/magicdraw/ui/languagebody/LanguageBodyEditor.html`
- source_sha256: `5cc569c3b13e688c8e6272fa590c1a0fe1828a524d435ded0dfa8d99c00fad12`
- captured_utc: `2026-07-14T16:55:52.752428+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.languagebody](package-summary.html)

## Interface LanguageBodyEditor

@OpenApiAllpublic interfaceLanguageBodyEditor

Language body editor - allows to have a custom editor for the body of the language.
 Should be created by [`LanguageBodyEditorFactory`](LanguageBodyEditorFactory.html).

See Also:
[`LanguageBodyEditorFactory`](LanguageBodyEditorFactory.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getBody](#getBody())()`
Get editing body.
`[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)`
`[getComponent](#getComponent())()`
Get editor component.
`void`
`[setBody](#setBody(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) body)`
Set body to edit.
`void`
`[setEditable](#setEditable(boolean))(boolean editable)`
Change editor editing state.

============ METHOD DETAIL ========== 
Method Details
getComponent
[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) getComponent()
Get editor component.
Returns:
editor component.
getBody
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getBody()
Get editing body.
Returns:
body.
setBody
void setBody([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) body)
Set body to edit.
Parameters:
`body` - body to edit.
setEditable
void setEditable(boolean editable)
Change editor editing state.
Parameters:
`editable` - if editable.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.languagebody</a></div>
<h1 class="title" title="Interface LanguageBodyEditor">Interface LanguageBodyEditor</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">LanguageBodyEditor</span></div>
<div class="block">Language body editor - allows to have a custom editor for the body of the language.
 Should be created by <a href="LanguageBodyEditorFactory.html" title="interface in com.nomagic.magicdraw.ui.languagebody"><code>LanguageBodyEditorFactory</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="LanguageBodyEditorFactory.html" title="interface in com.nomagic.magicdraw.ui.languagebody"><code>LanguageBodyEditorFactory</code></a></li>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBody()">getBody</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get editing body.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getComponent()">getComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get editor component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBody(java.lang.String)">setBody</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> body)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set body to edit.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEditable(boolean)">setEditable</a><wbr/>(boolean editable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Change editor editing state.</div>
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
<section class="detail" id="getComponent()">
<h3>getComponent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">getComponent</span>()</div>
<div class="block">Get editor component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>editor component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBody()">
<h3>getBody</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBody</span>()</div>
<div class="block">Get editing body.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>body.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBody(java.lang.String)">
<h3>setBody</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBody</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> body)</span></div>
<div class="block">Set body to edit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>body</code> - body to edit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEditable(boolean)">
<h3>setEditable</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEditable</span><wbr/><span class="parameters">(boolean editable)</span></div>
<div class="block">Change editor editing state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>editable</code> - if editable.</dd>
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
