# JAVA OPENAPI: NotificationViewConfig (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/notification/config/NotificationViewConfig.html
- source_path: `com/nomagic/magicdraw/ui/notification/config/NotificationViewConfig.html`
- source_sha256: `908649cd6d08bbad3a0c3f40d7790747ff75d7968754d3c59270bbfded738f12`
- captured_utc: `2026-07-14T16:52:04.449783+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification.config](package-summary.html)

## Class NotificationViewConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classNotificationViewConfig
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)

Helper class containing parameters that controls notification visual attributes and behavior.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NotificationViewConfig](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[NotificationViewConfig](NotificationViewConfig.html)`
`[clone](#clone())()`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getBackgroundColor](#getBackgroundColor())()`
Returns notification background color.
`int`
`[getExpirationTime](#getExpirationTime())()`
Returns time amount in seconds for how long notification will be displayed.
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns notification icon.
`void`
`[setBackgroundColor](#setBackgroundColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) backgroundColor)`
Sets notification background color.
`void`
`[setExpirationTime](#setExpirationTime(int))(int expirationTime)`
Sets time amount in seconds for how long notification will be displayed.
`void`
`[setIcon](#setIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets notification icon.
`void`
`[setShowMultipleNotifications](#setShowMultipleNotifications(boolean))(boolean showMultipleNotifications)`
Sets if same notification can be displayed many times simultaneously.
`boolean`
`[showMultipleNotifications](#showMultipleNotifications())()`
Indicates if same notification can be shown many times simultaneously.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NotificationViewConfig
public NotificationViewConfig()
 ============ METHOD DETAIL ========== 
Method Details
getIcon
public [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns notification icon.
Returns:
notification icon
setIcon
public void setIcon([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets notification icon.
Parameters:
`icon` - notification icon
getBackgroundColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getBackgroundColor()
Returns notification background color.
Returns:
notification background color
setBackgroundColor
public void setBackgroundColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) backgroundColor)
Sets notification background color.
Parameters:
`backgroundColor` - notification background color.
getExpirationTime
public int getExpirationTime()
Returns time amount in seconds for how long notification will be displayed.
Returns:
time amount in seconds
setExpirationTime
public void setExpirationTime(int expirationTime)
Sets time amount in seconds for how long notification will be displayed.
Parameters:
`expirationTime` - time amount in seconds
showMultipleNotifications
public boolean showMultipleNotifications()
Indicates if same notification can be shown many times simultaneously. If multiple request to show the
 notification are sent while this property is set to false, only first request will be honored. All others
 request will be ignored.
Returns:
true if same notification can be shown many times simultaneously.
setShowMultipleNotifications
public void setShowMultipleNotifications(boolean showMultipleNotifications)
Sets if same notification can be displayed many times simultaneously.
Parameters:
`showMultipleNotifications` - notification simultaneous display state
clone
public [NotificationViewConfig](NotificationViewConfig.html) clone()
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification.config</a></div>
<h1 class="title" title="Class NotificationViewConfig">Class NotificationViewConfig</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">NotificationViewConfig</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">Helper class containing parameters that controls notification visual attributes and behavior.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NotificationViewConfig</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBackgroundColor()">getBackgroundColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification background color.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExpirationTime()">getExpirationTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns time amount in seconds for how long notification will be displayed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification icon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBackgroundColor(java.awt.Color)">setBackgroundColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> backgroundColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification background color.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExpirationTime(int)">setExpirationTime</a><wbr/>(int expirationTime)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets time amount in seconds for how long notification will be displayed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIcon(javax.swing.Icon)">setIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification icon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowMultipleNotifications(boolean)">setShowMultipleNotifications</a><wbr/>(boolean showMultipleNotifications)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets if same notification can be displayed many times simultaneously.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMultipleNotifications()">showMultipleNotifications</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if same notification can be shown many times simultaneously.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>NotificationViewConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NotificationViewConfig</span>()</div>
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
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns notification icon.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIcon(javax.swing.Icon)">
<h3>setIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets notification icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - notification icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBackgroundColor()">
<h3>getBackgroundColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getBackgroundColor</span>()</div>
<div class="block">Returns notification background color.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification background color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBackgroundColor(java.awt.Color)">
<h3>setBackgroundColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBackgroundColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> backgroundColor)</span></div>
<div class="block">Sets notification background color.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>backgroundColor</code> - notification background color.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpirationTime()">
<h3>getExpirationTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getExpirationTime</span>()</div>
<div class="block">Returns time amount in seconds for how long notification will be displayed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>time amount in seconds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExpirationTime(int)">
<h3>setExpirationTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExpirationTime</span><wbr/><span class="parameters">(int expirationTime)</span></div>
<div class="block">Sets time amount in seconds for how long notification will be displayed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expirationTime</code> - time amount in seconds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMultipleNotifications()">
<h3>showMultipleNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showMultipleNotifications</span>()</div>
<div class="block">Indicates if same notification can be shown many times simultaneously. If multiple request to show the
 notification are sent while this property is set to false, only first request will be honored. All others
 request will be ignored.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if same notification can be shown many times simultaneously.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowMultipleNotifications(boolean)">
<h3>setShowMultipleNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowMultipleNotifications</span><wbr/><span class="parameters">(boolean showMultipleNotifications)</span></div>
<div class="block">Sets if same notification can be displayed many times simultaneously.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showMultipleNotifications</code> - notification simultaneous display state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
