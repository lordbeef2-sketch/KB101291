# JAVA OPENAPI: StyledDocument (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/html/StyledDocument.html
- source_path: `com/nomagic/magicreport/format/html/StyledDocument.html`
- source_sha256: `4e5c2195af18bb2dd4bb6c14de240b4e5e715902e961acdfe57c6f73593d2f37`
- captured_utc: `2026-07-14T16:46:14.372992+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Interface StyledDocument

All Known Implementing Classes:
`[DOCXEngine](../../engine/velocity/DOCXEngine.html)`, `[PPTXEngine](../../engine/velocity/PPTXEngine.html)`, `[RTFEngine](../../engine/velocity/RTFEngine.html)`, `[XLSXEngine](../../engine/velocity/XLSXEngine.html)`

@OpenApiAllpublic interfaceStyledDocument

The interface of object which support document format.

Since:
Jul 23, 2008 11:48:14 AM

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[CHARACTER](#CHARACTER)`
The type signature that is expected to be present on any attribute key that contributes to character level
 presentation.
`static final int`
`[COLOR](#COLOR)`
The type signature that is expected to be present on any attribute key that contributes to presentation of
 color.
`static final int`
`[FONT](#FONT)`
The type signature that is expected to be present on any attribute key that contributes to the determination
 of what font to use to render some text.
`static final int`
`[PARAGRAPH](#PARAGRAPH)`
The type signature that is expected to be present on any attribute key that contributes to the paragraph
 level presentation.
`static final int`
`[TABLE](#TABLE)`
The type signature that is expected to be present on any attribute key that contributes to the table
 presentation.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[addColor](#addColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)`
Appends the specified color to the document's color table.
`int`
`[addFont](#addFont(java.awt.Font))([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)`
Appends the specified font to the document's font table.
`int`
`[addList](#addList(com.nomagic.magicreport.format.html.List))([List](List.html) list)`
Appends the specified list item to the document's style table.
`int`
`[addObject](#addObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)`
Appends object content into the document.
`int`
`[addStyle](#addStyle(javax.swing.text.Style))([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)`
Appends the specified style to the document's style table.

============ FIELD DETAIL =========== 
Field Details
CHARACTER
static final int CHARACTER
The type signature that is expected to be present on any attribute key that contributes to character level
 presentation.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.CHARACTER)
COLOR
static final int COLOR
The type signature that is expected to be present on any attribute key that contributes to presentation of
 color.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.COLOR)
FONT
static final int FONT
The type signature that is expected to be present on any attribute key that contributes to the determination
 of what font to use to render some text.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.FONT)
PARAGRAPH
static final int PARAGRAPH
The type signature that is expected to be present on any attribute key that contributes to the paragraph
 level presentation.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.PARAGRAPH)
TABLE
static final int TABLE
The type signature that is expected to be present on any attribute key that contributes to the table
 presentation.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.TABLE)
 ============ METHOD DETAIL ========== 
Method Details
addColor
int addColor([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)
Appends the specified color to the document's color table. Returns an index of color from table.
Parameters:
`color` - specified color.
Returns:
index of color from color table in document.
addFont
int addFont([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)
Appends the specified font to the document's font table. Returns an index of font from table.
Parameters:
`font` - specified font.
Returns:
index of font from font table in document.
addList
int addList([List](List.html) list)
Appends the specified list item to the document's style table. Returns an index of list from table.
Parameters:
`list` - specified list.
Returns:
index of list from style table in document.
addStyle
int addStyle([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)
Appends the specified style to the document's style table. Return an index of style from table.
Parameters:
`style` - a style. Reproduce from StyleContext.NamedStyle
Returns:
index of style from style table in document.
addObject
int addObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)
Appends object content into the document.
Parameters:
`object` - adding object
Returns:
index to object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Interface StyledDocument">Interface StyledDocument</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../engine/velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a></code>, <code><a href="../../engine/velocity/PPTXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">PPTXEngine</a></code>, <code><a href="../../engine/velocity/RTFEngine.html" title="class in com.nomagic.magicreport.engine.velocity">RTFEngine</a></code>, <code><a href="../../engine/velocity/XLSXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XLSXEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">StyledDocument</span></div>
<div class="block">The interface of object which support document format.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jul 23, 2008 11:48:14 AM</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHARACTER">CHARACTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">The type signature that is expected to be present on any attribute key that contributes to character level
 presentation.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLOR">COLOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The type signature that is expected to be present on any attribute key that contributes to presentation of
 color.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FONT">FONT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the determination
 of what font to use to render some text.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PARAGRAPH">PARAGRAPH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the paragraph
 level presentation.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TABLE">TABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the table
 presentation.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addColor(java.awt.Color)">addColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Appends the specified color to the document's color table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFont(java.awt.Font)">addFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Appends the specified font to the document's font table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addList(com.nomagic.magicreport.format.html.List)">addList</a><wbr/>(<a href="List.html" title="interface in com.nomagic.magicreport.format.html">List</a> list)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Appends the specified list item to the document's style table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addObject(java.lang.Object)">addObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Appends object content into the document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addStyle(javax.swing.text.Style)">addStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Appends the specified style to the document's style table.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="CHARACTER">
<h3>CHARACTER</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CHARACTER</span></div>
<div class="block">The type signature that is expected to be present on any attribute key that contributes to character level
 presentation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.CHARACTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLOR">
<h3>COLOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">COLOR</span></div>
<div class="block">The type signature that is expected to be present on any attribute key that contributes to presentation of
 color.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FONT">
<h3>FONT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FONT</span></div>
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the determination
 of what font to use to render some text.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.FONT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PARAGRAPH">
<h3>PARAGRAPH</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PARAGRAPH</span></div>
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the paragraph
 level presentation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.PARAGRAPH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TABLE">
<h3>TABLE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TABLE</span></div>
<div class="block">The type signature that is expected to be present on any attribute key that contributes to the table
 presentation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledDocument.TABLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="addColor(java.awt.Color)">
<h3>addColor</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">addColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="block">Appends the specified color to the document's color table. Returns an index of color from table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - specified color.</dd>
<dt>Returns:</dt>
<dd>index of color from color table in document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFont(java.awt.Font)">
<h3>addFont</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">addFont</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</span></div>
<div class="block">Appends the specified font to the document's font table. Returns an index of font from table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>font</code> - specified font.</dd>
<dt>Returns:</dt>
<dd>index of font from font table in document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addList(com.nomagic.magicreport.format.html.List)">
<h3>addList</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">addList</span><wbr/><span class="parameters">(<a href="List.html" title="interface in com.nomagic.magicreport.format.html">List</a> list)</span></div>
<div class="block">Appends the specified list item to the document's style table. Returns an index of list from table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>list</code> - specified list.</dd>
<dt>Returns:</dt>
<dd>index of list from style table in document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStyle(javax.swing.text.Style)">
<h3>addStyle</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">addStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> style)</span></div>
<div class="block">Appends the specified style to the document's style table. Return an index of style from table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - a style. Reproduce from <tt>StyleContext.NamedStyle</tt></dd>
<dt>Returns:</dt>
<dd>index of style from style table in document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addObject(java.lang.Object)">
<h3>addObject</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">addObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Appends object content into the document.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - adding object</dd>
<dt>Returns:</dt>
<dd>index to object</dd>
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
