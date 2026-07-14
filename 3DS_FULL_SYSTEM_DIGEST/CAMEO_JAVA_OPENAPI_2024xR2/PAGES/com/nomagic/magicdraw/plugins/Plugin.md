# JAVA OPENAPI: Plugin (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/plugins/Plugin.html
- source_path: `com/nomagic/magicdraw/plugins/Plugin.html`
- source_sha256: `cbb83dc0ee82d7afa1c82be932e585a136bdf80e2c4486f080154eed14126a27`
- captured_utc: `2026-07-14T16:55:24.813115+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.plugins](package-summary.html)

## Class Plugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.plugins.Plugin

Direct Known Subclasses:
`[BaseEmfUml2XmiPlugin](../emfuml2xmi/BaseEmfUml2XmiPlugin.html)`, `[MofPlugin](../mof/MofPlugin.html)`

@OpenApiAllpublic abstract classPlugin
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

The base abstract class for any MagicDraw plugin.
 Plugin must be extended from this class. Every plugin has it own descriptor. 

 MagicDraw calls method init() for plugin on startup. 

 MagicDraw will not exit if at least one plugin close() method returns false.

See Also:
[`init()`](#init())
[`close()`](#close())

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Plugin](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`abstract boolean`
`[close](#close())()`
MagicDraw calls this method before exiting the application.
`[PluginDescriptor](PluginDescriptor.html)`
`[getDescriptor](#getDescriptor())()`
Returns plugin descriptor.
`abstract void`
`[init](#init())()`
Plugin initialization method.
`abstract boolean`
`[isSupported](#isSupported())()`
MagicDraw calls this method to identify if this plugin is supported.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Plugin
public Plugin()
 ============ METHOD DETAIL ========== 
Method Details
getDescriptor
public [PluginDescriptor](PluginDescriptor.html) getDescriptor()
Returns plugin descriptor.
Returns:
plugin descriptor
init
public abstract void init()
Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.
close
public abstract boolean close()
MagicDraw calls this method before exiting the application.
 If at least one plugin returns 'false', MagicDraw application will not exit.
 Override this method and do any exit specific action(your plugin state saving for example).
Returns:
true, if plugin can be closed normally; false, if plugin cannot be closed and MagicDraw
 application can not exit
isSupported
public abstract boolean isSupported()
MagicDraw calls this method to identify if this plugin is supported.
 Plugin is initialized and started only if this method returns `true`.
 Override this method to check specific conditions for the plugin supportability.
Returns:
true, if plugin is supported; false, if plugin is not supported

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.plugins</a></div>
<h1 class="title" title="Class Plugin">Class Plugin</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.plugins.Plugin</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../emfuml2xmi/BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code>, <code><a href="../mof/MofPlugin.html" title="class in com.nomagic.magicdraw.mof">MofPlugin</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">Plugin</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The base abstract class for any MagicDraw plugin.
 Plugin must be extended from this class. Every plugin has it own descriptor.<br/>
 MagicDraw calls method init() for plugin on startup.<br/>
 MagicDraw will not exit if at least one plugin close() method returns false.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#init()"><code>init()</code></a></li>
<li><a href="#close()"><code>close()</code></a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Plugin</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">MagicDraw calls this method before exiting the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PluginDescriptor.html" title="class in com.nomagic.magicdraw.plugins">PluginDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptor()">getDescriptor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Plugin initialization method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSupported()">isSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">MagicDraw calls this method to identify if this plugin is supported.</div>
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
<h3>Plugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Plugin</span>()</div>
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
<section class="detail" id="getDescriptor()">
<h3>getDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PluginDescriptor.html" title="class in com.nomagic.magicdraw.plugins">PluginDescriptor</a></span> <span class="element-name">getDescriptor</span>()</div>
<div class="block">Returns plugin descriptor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>plugin descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init()">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">init</span>()</div>
<div class="block">Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.</div>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">close</span>()</div>
<div class="block">MagicDraw calls this method before exiting the application.
 If at least one plugin returns 'false', MagicDraw application will not exit.
 Override this method and do any exit specific action(your plugin state saving for example).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if plugin can be closed normally; false, if plugin cannot be closed and MagicDraw
 application can not exit</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupported()">
<h3>isSupported</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isSupported</span>()</div>
<div class="block">MagicDraw calls this method to identify if this plugin is supported.
 Plugin is initialized and started only if this method returns <code>true</code>.
 Override this method to check specific conditions for the plugin supportability.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if plugin is supported; false, if plugin is not supported</dd>
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
