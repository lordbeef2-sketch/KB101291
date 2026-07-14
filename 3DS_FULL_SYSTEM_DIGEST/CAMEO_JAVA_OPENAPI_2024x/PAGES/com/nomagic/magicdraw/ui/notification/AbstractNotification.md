# JAVA OPENAPI: AbstractNotification (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/notification/AbstractNotification.html
- source_path: `com/nomagic/magicdraw/ui/notification/AbstractNotification.html`
- source_sha256: `184aa8d0cc091ef9bbc302beff46d4d7735742c4ea4650bd4f1c06c0e9c104b7`
- captured_utc: `2026-07-14T16:52:05.885797+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification](package-summary.html)

## Class AbstractNotification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.notification.AbstractNotification

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

Direct Known Subclasses:
`[Notification](Notification.html)`

@OpenApipublic abstract classAbstractNotification
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)

Base MagicDraw notification composed of title, message text and list HRefRunnable actions

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.ui.notification.AbstractNotification)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addHRefAction](#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable))([HRefRunnable](HRefRunnable.html) r)`
Adds href action to list of already existing list of actions.
`[HRefRunnable](HRefRunnable.html)`
`[getHRefAction](#getHRefAction(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)`
Gets href action with a given href.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns notification id.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLongText](#getLongText())()`
Returns long notification text
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`
Returns notification message text.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`
Returns notification title.
`void`
`[removeHRefAction](#removeHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable))([HRefRunnable](HRefRunnable.html) r)`
Removes given href action.
`void`
`[removeHRefAction](#removeHRefAction(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)`
Removes given href action with specified href id.
`void`
`[setLongText](#setLongText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)`
Sets notification long text
`void`
`[setText](#setText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Sets notification message text.
`void`
`[setTitle](#setTitle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Sets notification title.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getID
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns notification id.
Returns:
notification id
getTitle
@OpenApi
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()
Returns notification title.
Returns:
notification title
setTitle
@OpenApipublic void setTitle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Sets notification title.
Parameters:
`title` - notification title
getText
@OpenApi
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()
Returns notification message text.
Returns:
notification text
setText
@OpenApipublic void setText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Sets notification message text.
Parameters:
`text` - notification text
getLongText
@OpenApi
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLongText()
Returns long notification text
Returns:
long notification text
setLongText
@OpenApipublic void setLongText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)
Sets notification long text
Parameters:
`longText` - notification long text
addHRefAction
@OpenApipublic void addHRefAction([HRefRunnable](HRefRunnable.html) r)
Adds href action to list of already existing list of actions.
Parameters:
`r` - given href action
removeHRefAction
@OpenApipublic void removeHRefAction([HRefRunnable](HRefRunnable.html) r)
Removes given href action.
Parameters:
`r` - href action to remove
removeHRefAction
@OpenApipublic void removeHRefAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)
Removes given href action with specified href id.
Parameters:
`href` - href id to remove from href list
getHRefAction
@OpenApi
@CheckForNullpublic [HRefRunnable](HRefRunnable.html) getHRefAction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)
Gets href action with a given href. If action does not exist, null is returned.
Parameters:
`href` - action href
Returns:
href action if found, null otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification</a></div>
<h1 class="title" title="Class AbstractNotification">Class AbstractNotification</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.AbstractNotification</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractNotification</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Base MagicDraw notification composed of title, message text and list HRefRunnable actions</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.ui.notification.AbstractNotification">Serialized Form</a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">addHRefAction</a><wbr/>(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds href action to list of already existing list of actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHRefAction(java.lang.String)">getHRefAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets href action with a given href.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLongText()">getLongText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns long notification text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification message text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification title.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">removeHRefAction</a><wbr/>(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given href action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeHRefAction(java.lang.String)">removeHRefAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given href action with specified href id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLongText(java.lang.String)">setLongText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification long text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.String)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification message text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitle(java.lang.String)">setTitle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification title.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns notification id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<div class="block">Returns notification title.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTitle(java.lang.String)">
<h3>setTitle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Sets notification title.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>title</code> - notification title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Returns notification message text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Sets notification message text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - notification text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLongText()">
<h3>getLongText</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLongText</span>()</div>
<div class="block">Returns long notification text</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>long notification text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLongText(java.lang.String)">
<h3>setLongText</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</span></div>
<div class="block">Sets notification long text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>longText</code> - notification long text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">
<h3>addHRefAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addHRefAction</span><wbr/><span class="parameters">(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a> r)</span></div>
<div class="block">Adds href action to list of already existing list of actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - given href action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">
<h3>removeHRefAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeHRefAction</span><wbr/><span class="parameters">(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a> r)</span></div>
<div class="block">Removes given href action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - href action to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeHRefAction(java.lang.String)">
<h3>removeHRefAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeHRefAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</span></div>
<div class="block">Removes given href action with specified href id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - href id to remove from href list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHRefAction(java.lang.String)">
<h3>getHRefAction</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></span> <span class="element-name">getHRefAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</span></div>
<div class="block">Gets href action with a given href. If action does not exist, null is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - action href</dd>
<dt>Returns:</dt>
<dd>href action if found, null otherwise</dd>
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
