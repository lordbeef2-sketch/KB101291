# JAVA OPENAPI: PathEndRenderer (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/symbols/paths/PathEndRenderer.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/PathEndRenderer.html`
- source_sha256: `1481e8b74d1de243ad49f7b64354c5d426873985b61c0169c4920a7b27950439`
- captured_utc: `2026-07-14T16:58:31.061213+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class PathEndRenderer

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.paths.PathEndRenderer

@OpenApiAllpublic classPathEndRenderer
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Renders the end of the path.
 Allows to specifie custom adorment for the path end (e.g. path with arrow at the end or specific icon on the end).

See Also:
[`PathElementRenderer`](PathElementRenderer.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PathEndRenderer](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment))([PathEndAdornment](PathEndAdornment.html) adornment)`
Constructor.
`[PathEndRenderer](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment,com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornmentModifier))([PathEndAdornment](PathEndAdornment.html) adornment,
 [PathEndAdornmentModifier](PathEndAdornmentModifier.html) modifier)`
Constructor.
`[PathEndRenderer](#%3Cinit%3E(com.nomagic.ui.ResizableIcon))([ResizableIcon](../../../../ui/ResizableIcon.html) icon)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final [ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getIcon](#getIcon())()`
return path end icon
`final int`
`[getStyle](#getStyle())()`
return path end style
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PathEndRenderer
public PathEndRenderer([PathEndAdornment](PathEndAdornment.html) adornment,
 @CheckForNull
 [PathEndAdornmentModifier](PathEndAdornmentModifier.html) modifier)
Constructor. The specified end adornment with modifier will be used to render the path end.
Parameters:
`adornment` - predefined end adornment.
`modifier` - adornment modifier.
See Also:
[`PathEndAdornment`](PathEndAdornment.html)
[`PathEndAdornmentModifier`](PathEndAdornmentModifier.html)
PathEndRenderer
public PathEndRenderer([PathEndAdornment](PathEndAdornment.html) adornment)
Constructor. The specified end adornment will be used to render the path end.
Parameters:
`adornment` - predefined end adornment.
See Also:
[`PathEndAdornment`](PathEndAdornment.html)
PathEndRenderer
public PathEndRenderer([ResizableIcon](../../../../ui/ResizableIcon.html) icon)
Constructor. The specified icon will be used to render the path end.
Parameters:
`icon` - end adornment icon.
 ============ METHOD DETAIL ========== 
Method Details
getStyle
public final int getStyle()
return path end style
getIcon
public final [ResizableIcon](../../../../ui/ResizableIcon.html) getIcon()
return path end icon

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class PathEndRenderer">Class PathEndRenderer</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.PathEndRenderer</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PathEndRenderer</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Renders the end of the path.
 Allows to specifie custom adorment for the path end (e.g. path with arrow at the end or specific icon on the end).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PathElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathElementRenderer</code></a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment)">PathEndRenderer</a><wbr/>(<a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornment</a> adornment)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment,com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornmentModifier)">PathEndRenderer</a><wbr/>(<a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornment</a> adornment,
 <a href="PathEndAdornmentModifier.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornmentModifier</a> modifier)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon)">PathEndRenderer</a><wbr/>(<a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">return path end icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">return path end style</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment,com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornmentModifier)">
<h3>PathEndRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathEndRenderer</span><wbr/><span class="parameters">(<a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornment</a> adornment,
 @CheckForNull
 <a href="PathEndAdornmentModifier.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornmentModifier</a> modifier)</span></div>
<div class="block">Constructor. The specified end adornment with modifier will be used to render the path end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - predefined end adornment.</dd>
<dd><code>modifier</code> - adornment modifier.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathEndAdornment</code></a></li>
<li><a href="PathEndAdornmentModifier.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathEndAdornmentModifier</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.paths.PathEndAdornment)">
<h3>PathEndRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathEndRenderer</span><wbr/><span class="parameters">(<a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndAdornment</a> adornment)</span></div>
<div class="block">Constructor. The specified end adornment will be used to render the path end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adornment</code> - predefined end adornment.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PathEndAdornment.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathEndAdornment</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.ui.ResizableIcon)">
<h3>PathEndRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathEndRenderer</span><wbr/><span class="parameters">(<a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Constructor. The specified icon will be used to render the path end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - end adornment icon.</dd>
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
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getStyle</span>()</div>
<div class="block">return path end style</div>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">return path end icon</div>
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
