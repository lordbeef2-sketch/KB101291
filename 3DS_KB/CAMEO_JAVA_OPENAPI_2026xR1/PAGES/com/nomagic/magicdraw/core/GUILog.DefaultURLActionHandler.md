# JAVA OPENAPI: GUILog.DefaultURLActionHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/GUILog.DefaultURLActionHandler.html
- source_path: `com/nomagic/magicdraw/core/GUILog.DefaultURLActionHandler.html`
- source_sha256: `1b13eb0df4f21c6b55afecc5669dceca4abf84749852eaa2d4cfbe64ce39db59`
- captured_utc: `2026-07-14T16:45:28.938388+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class GUILog.DefaultURLActionHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.GUILog.DefaultURLActionHandler

All Implemented Interfaces:
`[GUILog.URLActionHandler](GUILog.URLActionHandler.html)`

Enclosing class:
`[GUILog](GUILog.html)`

@OpenApiAllpublic static classGUILog.DefaultURLActionHandler
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [GUILog.URLActionHandler](GUILog.URLActionHandler.html)

Default implementation for URLActionHandler

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.magicdraw.core.[GUILog.URLActionHandler](GUILog.URLActionHandler.html)
`[ACTION_URL_PROTOCOL](GUILog.URLActionHandler.html#ACTION_URL_PROTOCOL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DefaultURLActionHandler](#%3Cinit%3E(com.nomagic.actions.NMAction))([NMAction](../../actions/NMAction.html) action)`
Constructor for a handler with a single action
`[DefaultURLActionHandler](#%3Cinit%3E(com.nomagic.actions.NMAction,boolean))([NMAction](../../actions/NMAction.html) action,
 boolean closeWindow)`
Constructor for a handler with a single action
`[DefaultURLActionHandler](#%3Cinit%3E(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [NMAction](../../actions/NMAction.html)> actions)`
Constructor for a handler with many actions
`[DefaultURLActionHandler](#%3Cinit%3E(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [NMAction](../../actions/NMAction.html)> actions,
 boolean closeWindow)`
Constructor for a handler with many actions
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[openURL](#openURL(java.lang.String,java.awt.event.InputEvent))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [InputEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html) event)`
Opens given url.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultURLActionHandler
public DefaultURLActionHandler(@Nonnull
 [NMAction](../../actions/NMAction.html) action)
Constructor for a handler with a single action
Parameters:
`action` - action
DefaultURLActionHandler
public DefaultURLActionHandler(@Nonnull
 [NMAction](../../actions/NMAction.html) action,
 boolean closeWindow)
Constructor for a handler with a single action
Parameters:
`action` - action
`closeWindow` - close window in which hyperlink was activated
DefaultURLActionHandler
public DefaultURLActionHandler(@Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [NMAction](../../actions/NMAction.html)> actions)
Constructor for a handler with many actions
Parameters:
`actions` - actions
DefaultURLActionHandler
public DefaultURLActionHandler(@Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [NMAction](../../actions/NMAction.html)> actions,
 boolean closeWindow)
Constructor for a handler with many actions
Parameters:
`actions` - actions
`closeWindow` - close window in which hyperlink was activated
 ============ METHOD DETAIL ========== 
Method Details
openURL
public boolean openURL([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [InputEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html) event)
Description copied from interface: `[GUILog.URLActionHandler](GUILog.URLActionHandler.html#openURL(java.lang.String,java.awt.event.InputEvent))`
Opens given url.
Specified by:
`[openURL](GUILog.URLActionHandler.html#openURL(java.lang.String,java.awt.event.InputEvent))` in interface `[GUILog.URLActionHandler](GUILog.URLActionHandler.html)`
Parameters:
`url` - url
`event` - event
Returns:
true if url was handled, false if not

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class GUILog.DefaultURLActionHandler">Class GUILog.DefaultURLActionHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.GUILog.DefaultURLActionHandler</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">GUILog.DefaultURLActionHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a></span></div>
<div class="block">Default implementation for URLActionHandler</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.GUILog.URLActionHandler">Fields inherited from interface com.nomagic.magicdraw.core.<a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a></h3>
<code><a href="GUILog.URLActionHandler.html#ACTION_URL_PROTOCOL">ACTION_URL_PROTOCOL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.actions.NMAction)">DefaultURLActionHandler</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor for a handler with a single action</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.actions.NMAction,boolean)">DefaultURLActionHandler</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 boolean closeWindow)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor for a handler with a single action</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection)">DefaultURLActionHandler</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor for a handler with many actions</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,boolean)">DefaultURLActionHandler</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 boolean closeWindow)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor for a handler with many actions</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openURL(java.lang.String,java.awt.event.InputEvent)">openURL</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html" title="class or interface in java.awt.event">InputEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens given url.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.actions.NMAction)">
<h3>DefaultURLActionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultURLActionHandler</span><wbr/><span class="parameters">(@Nonnull
 <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Constructor for a handler with a single action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.actions.NMAction,boolean)">
<h3>DefaultURLActionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultURLActionHandler</span><wbr/><span class="parameters">(@Nonnull
 <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 boolean closeWindow)</span></div>
<div class="block">Constructor for a handler with a single action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
<dd><code>closeWindow</code> - close window in which hyperlink was activated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection)">
<h3>DefaultURLActionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultURLActionHandler</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions)</span></div>
<div class="block">Constructor for a handler with many actions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actions</code> - actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,boolean)">
<h3>DefaultURLActionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultURLActionHandler</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; actions,
 boolean closeWindow)</span></div>
<div class="block">Constructor for a handler with many actions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actions</code> - actions</dd>
<dd><code>closeWindow</code> - close window in which hyperlink was activated</dd>
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
<section class="detail" id="openURL(java.lang.String,java.awt.event.InputEvent)">
<h3>openURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">openURL</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html" title="class or interface in java.awt.event">InputEvent</a> event)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="GUILog.URLActionHandler.html#openURL(java.lang.String,java.awt.event.InputEvent)">GUILog.URLActionHandler</a></code></span></div>
<div class="block">Opens given url.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="GUILog.URLActionHandler.html#openURL(java.lang.String,java.awt.event.InputEvent)">openURL</a></code> in interface <code><a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a></code></dd>
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dd><code>event</code> - event</dd>
<dt>Returns:</dt>
<dd>true if url was handled, false if not</dd>
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
