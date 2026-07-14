# JAVA OPENAPI: NotificationViewBuilder (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/notification/NotificationViewBuilder.html
- source_path: `com/nomagic/magicdraw/ui/notification/NotificationViewBuilder.html`
- source_sha256: `f8c7bd1d84a0f97fe3a44cc80d6d566e20664d45b28cf17d85625439e3f29b0c`
- captured_utc: `2026-07-14T16:58:26.039156+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification](package-summary.html)

## Class NotificationViewBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.notification.NotificationViewBuilder

@OpenApiAllpublic abstract classNotificationViewBuilder
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Base class for MagicDraw notification builders, that creates and shows notification popups.
 User who wants to display his own notification popups in MagicDraw, must create builder implementing
 this interface and register it with NotificationManager

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NotificationViewBuilder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`abstract [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html)`
`[createNotificationView](#createNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig))([AbstractNotification](AbstractNotification.html) notification,
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 [NotificationViewConfig](config/NotificationViewConfig.html) config)`
Constructs popup that displays message to the user
`abstract void`
`[hideNotification](#hideNotification(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)`
Closes all notifications with specified id
`abstract void`
`[hideNotifications](#hideNotifications(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)`
Closes notifications that belong to provided component
`abstract boolean`
`[isVisible](#isVisible(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)`
Returns true if notification with specified id is still visible.
`abstract [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html)`
`[showNotificationView](#showNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig))([AbstractNotification](AbstractNotification.html) notification,
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 [NotificationViewConfig](config/NotificationViewConfig.html) config)`
Shows popup that displays message to the user
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NotificationViewBuilder
public NotificationViewBuilder()
 ============ METHOD DETAIL ========== 
Method Details
createNotificationView
public abstract [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) createNotificationView([AbstractNotification](AbstractNotification.html) notification,
 @CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 @CheckForNull
 [NotificationViewConfig](config/NotificationViewConfig.html) config)
Constructs popup that displays message to the user
Parameters:
`notification` - notification data
`owner` - newly created popup owner
`config` - notification view configuration parameters
Returns:
created popup that displays message to the user
showNotificationView
@CheckForNullpublic abstract [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) showNotificationView([AbstractNotification](AbstractNotification.html) notification,
 @CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 @CheckForNull
 [NotificationViewConfig](config/NotificationViewConfig.html) config)
Shows popup that displays message to the user
Parameters:
`notification` - notification data
`owner` - newly created popup owner
`config` - notification view configuration parameters
Returns:
popup that displays message to the user
hideNotification
public abstract void hideNotification(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)
Closes all notifications with specified id
Parameters:
`notificationID` - notification id
hideNotifications
public abstract void hideNotifications(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)
Closes notifications that belong to provided component
isVisible
public abstract boolean isVisible(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)
Returns true if notification with specified id is still visible.
Parameters:
`notificationID` - notification id

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification</a></div>
<h1 class="title" title="Class NotificationViewBuilder">Class NotificationViewBuilder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.NotificationViewBuilder</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">NotificationViewBuilder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Base class for MagicDraw notification builders, that creates and shows notification popups.
 User who wants to display his own notification popups in MagicDraw, must create builder implementing
 this interface and register it with NotificationManager</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NotificationViewBuilder</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">createNotificationView</a><wbr/>(<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a> notification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Constructs popup that displays message to the user</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hideNotification(java.lang.String)">hideNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Closes all notifications with specified id</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hideNotifications(java.awt.Component)">hideNotifications</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Closes notifications that belong to provided component</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVisible(java.lang.String)">isVisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true if notification with specified id is still visible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#showNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">showNotificationView</a><wbr/>(<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a> notification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Shows popup that displays message to the user</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>NotificationViewBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NotificationViewBuilder</span>()</div>
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
<section class="detail" id="createNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">
<h3>createNotificationView</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">createNotificationView</span><wbr/><span class="parameters">(<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a> notification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 @CheckForNull
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</span></div>
<div class="block">Constructs popup that displays message to the user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification data</dd>
<dd><code>owner</code> - newly created popup owner</dd>
<dd><code>config</code> - notification view configuration parameters</dd>
<dt>Returns:</dt>
<dd>created popup that displays message to the user</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNotificationView(com.nomagic.magicdraw.ui.notification.AbstractNotification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">
<h3>showNotificationView</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">showNotificationView</span><wbr/><span class="parameters">(<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a> notification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 @CheckForNull
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</span></div>
<div class="block">Shows popup that displays message to the user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification data</dd>
<dd><code>owner</code> - newly created popup owner</dd>
<dd><code>config</code> - notification view configuration parameters</dd>
<dt>Returns:</dt>
<dd>popup that displays message to the user</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideNotification(java.lang.String)">
<h3>hideNotification</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">hideNotification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</span></div>
<div class="block">Closes all notifications with specified id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notificationID</code> - notification id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideNotifications(java.awt.Component)">
<h3>hideNotifications</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">hideNotifications</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</span></div>
<div class="block">Closes notifications that belong to provided component</div>
</section>
</li>
<li>
<section class="detail" id="isVisible(java.lang.String)">
<h3>isVisible</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isVisible</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</span></div>
<div class="block">Returns true if notification with specified id is still visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notificationID</code> - notification id</dd>
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
