# JAVA OPENAPI: HyperlinkHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/hyperlinks/HyperlinkHandler.html
- source_path: `com/nomagic/magicdraw/hyperlinks/HyperlinkHandler.html`
- source_sha256: `2ed75f9df9a89f47ac129420051b7f137606f48059c2e321bd0d7c4033cf2394`
- captured_utc: `2026-07-14T16:45:37.134500+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.hyperlinks](package-summary.html)

## Interface HyperlinkHandler

All Superinterfaces:
`[ProtocolSupport](ProtocolSupport.html)`

@OpenApiAllpublic interfaceHyperlinkHandlerextends [ProtocolSupport](ProtocolSupport.html)

Handle the hyperlink. The handler should be registered in [`HyperlinksHandlersRegistry`](HyperlinksHandlersRegistry.html)

See Also:
[`HyperlinksHandlersRegistry`](HyperlinksHandlersRegistry.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[activate](#activate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) link)`
Activate given hyperlink.
`default [Hyperlink](Hyperlink.html)`
`[create](#create(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)`
Deprecated.
use [`create(String, String, Project)`](#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project))
`default [Hyperlink](Hyperlink.html)`
`[create](#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [Project](../core/Project.html) context)`
Create hyperlink.
`[HyperlinkEditor](ui/HyperlinkEditor.html)`
`[getEditor](#getEditor())()`
Get hyperlink editor.
`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink))([Hyperlink](Hyperlink.html) link)`
Get hyperlink icon.
Methods inherited from interface com.nomagic.magicdraw.hyperlinks.[ProtocolSupport](ProtocolSupport.html)
`[isSupportedProtocol](ProtocolSupport.html#isSupportedProtocol(java.lang.String))`

============ METHOD DETAIL ========== 
Method Details
getIcon
@CheckForNull[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) getIcon([Hyperlink](Hyperlink.html) link)
Get hyperlink icon.
Parameters:
`link` - hyperlink
Returns:
icon
create
@CheckForNulldefault [Hyperlink](Hyperlink.html) create(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 @CheckForNull
 [Project](../core/Project.html) context)
Create hyperlink.
Parameters:
`text` - hyperlink text
`url` - hyperlink URL
`context` - project
Returns:
created hyperlink
create
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)default [Hyperlink](Hyperlink.html) create(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)
Deprecated.
use [`create(String, String, Project)`](#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project))
Create hyperlink.
Parameters:
`text` - hyperlink text
`url` - hyperlink URL
Returns:
created hyperlink
getEditor
@CheckForNull[HyperlinkEditor](ui/HyperlinkEditor.html) getEditor()
Get hyperlink editor.
Returns:
hyperlink editor
activate
void activate(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Hyperlink](Hyperlink.html) link)
Activate given hyperlink.
Parameters:
`element` - hyperlink owner
`link` - hyperlink to activate

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.hyperlinks</a></div>
<h1 class="title" title="Interface HyperlinkHandler">Interface HyperlinkHandler</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ProtocolSupport.html" title="interface in com.nomagic.magicdraw.hyperlinks">ProtocolSupport</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">HyperlinkHandler</span><span class="extends-implements">
extends <a href="ProtocolSupport.html" title="interface in com.nomagic.magicdraw.hyperlinks">ProtocolSupport</a></span></div>
<div class="block">Handle the hyperlink. The handler should be registered in <a href="HyperlinksHandlersRegistry.html" title="class in com.nomagic.magicdraw.hyperlinks"><code>HyperlinksHandlersRegistry</code></a></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="HyperlinksHandlersRegistry.html" title="class in com.nomagic.magicdraw.hyperlinks"><code>HyperlinksHandlersRegistry</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#activate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">activate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Activate given hyperlink.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)"><code>create(String, String, Project)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Create hyperlink.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ui/HyperlinkEditor.html" title="interface in com.nomagic.magicdraw.hyperlinks.ui">HyperlinkEditor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEditor()">getEditor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get hyperlink editor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink)">getIcon</a><wbr/>(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get hyperlink icon.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.hyperlinks.ProtocolSupport">Methods inherited from interface com.nomagic.magicdraw.hyperlinks.<a href="ProtocolSupport.html" title="interface in com.nomagic.magicdraw.hyperlinks">ProtocolSupport</a></h3>
<code><a href="ProtocolSupport.html#isSupportedProtocol(java.lang.String)">isSupportedProtocol</a></code></div>
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
<section class="detail" id="getIcon(com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</span></div>
<div class="block">Get hyperlink icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - hyperlink</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 @CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> context)</span></div>
<div class="block">Create hyperlink.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - hyperlink text</dd>
<dd><code>url</code> - hyperlink URL</dd>
<dd><code>context</code> - project</dd>
<dt>Returns:</dt>
<dd>created hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type"><a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#create(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project)"><code>create(String, String, Project)</code></a></div>
</div>
<div class="block">Create hyperlink.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - hyperlink text</dd>
<dd><code>url</code> - hyperlink URL</dd>
<dt>Returns:</dt>
<dd>created hyperlink</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEditor()">
<h3>getEditor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ui/HyperlinkEditor.html" title="interface in com.nomagic.magicdraw.hyperlinks.ui">HyperlinkEditor</a></span> <span class="element-name">getEditor</span>()</div>
<div class="block">Get hyperlink editor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>hyperlink editor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.hyperlinks.Hyperlink)">
<h3>activate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">activate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="Hyperlink.html" title="interface in com.nomagic.magicdraw.hyperlinks">Hyperlink</a> link)</span></div>
<div class="block">Activate given hyperlink.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - hyperlink owner</dd>
<dd><code>link</code> - hyperlink to activate</dd>
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
