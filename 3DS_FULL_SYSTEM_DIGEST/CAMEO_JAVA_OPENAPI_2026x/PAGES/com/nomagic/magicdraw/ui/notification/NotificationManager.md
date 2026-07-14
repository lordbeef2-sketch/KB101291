# JAVA OPENAPI: NotificationManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/notification/NotificationManager.html
- source_path: `com/nomagic/magicdraw/ui/notification/NotificationManager.html`
- source_sha256: `074b4d7533c9fca19c992fda99e7ae8cb202d9611c3ee6b4b72c1dc921e3a547`
- captured_utc: `2026-07-14T16:58:26.000157+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification](package-summary.html)

## Class NotificationManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.notification.NotificationManager

@OpenApiAllpublic classNotificationManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Entry point to display notifications in MagicDraw. Two types of notifications can be displayed: application level and
 container level. Container lever notifications are displayed in special container that implements
 NotificationsContainer interface. When show notification method is called component owner parameter should point
 to notification container. If application level notification must be displayed, null parameter should be passed as
 component owner.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[NotificationManager](#%3Cinit%3E())()`
Creates new Notification manager instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addNotificationShowingConfigurator](#addNotificationShowingConfigurator(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Notification](Notification.html)> notificationShowingConfigurator)`
Adds custom logic configurator in order to limit shown notifications.
`[NotificationViewBuilder](NotificationViewBuilder.html)`
`[getApplicationNotificationGroupBuilder](#getApplicationNotificationGroupBuilder())()`
Returns builder that creates and displays grouped application notifications
`[NotificationViewBuilder](NotificationViewBuilder.html)`
`[getApplicationNotificationsBuilder](#getApplicationNotificationsBuilder())()`
Returns builder that creates and displays application notifications
`[NotificationViewConfig](config/NotificationViewConfig.html)`
`[getConfig](#getConfig(com.nomagic.magicdraw.ui.notification.Notification))([Notification](Notification.html) notification)`
Helper method that returns predefined display parameters determined by notification severity level.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AbstractNotification](AbstractNotification.html)>`
`[getContainerNotifications](#getContainerNotifications(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)`

`[NotificationViewBuilder](NotificationViewBuilder.html)`
`[getContainerNotificationsBuilder](#getContainerNotificationsBuilder())()`
Returns builder that creates and displays container notifications
`[NotificationViewConfig](config/NotificationViewConfig.html)`
`[getErrorConfig](#getErrorConfig())()`
Returns display parameters for notification with severity error
`[NotificationViewConfig](config/NotificationViewConfig.html)`
`[getInfoConfig](#getInfoConfig())()`
Returns display parameters for notification with severity info
`static [NotificationManager](NotificationManager.html)`
`[getInstance](#getInstance())()`
Returns single Notification manger instance
`[NotificationViewConfig](config/NotificationViewConfig.html)`
`[getWarningConfig](#getWarningConfig())()`
Returns display parameters for notification with severity warning
`static boolean`
`[hasNewMessages](#hasNewMessages())()`

`void`
`[hideNotifications](#hideNotifications(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)`
Hides all notifications for component.
`void`
`[hideNotifications](#hideNotifications(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)`
Hides notifications with specified id
`boolean`
`[isNotificationVisible](#isNotificationVisible(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)`
Returns true if notification with specified id is shown
`static boolean`
`[isOpenWindowAfterLoad](#isOpenWindowAfterLoad())()`

`void`
`[logHyperlinkedTextNotifications](#logHyperlinkedTextNotifications(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> callbacks)`
Logs hyperlinked text to Notification window without displaying balloon message.
`void`
`[openNotificationWindow](#openNotificationWindow(com.nomagic.magicdraw.ui.notification.Notification,boolean))([Notification](Notification.html) notification,
 boolean openWindow)`
Shows notification in notification window
`void`
`[setApplicationNotificationGroupBuilder](#setApplicationNotificationGroupBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder))([NotificationViewBuilder](NotificationViewBuilder.html) applicationNotificationGroupBuilder)`
Sets builder that creates and displays grouped application notifications
`void`
`[setApplicationNotificationsBuilder](#setApplicationNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder))([NotificationViewBuilder](NotificationViewBuilder.html) applicationNotificationsBuilder)`
Sets builder that creates and displays application notifications
`void`
`[setContainerNotificationsBuilder](#setContainerNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder))([NotificationViewBuilder](NotificationViewBuilder.html) containerNotificationsBuilder)`
Sets builder that creates and displays container notifications
`static void`
`[setHasNewMessages](#setHasNewMessages(boolean))(boolean hasNewMessages)`

`static void`
`[setOpenWindowAfterLoad](#setOpenWindowAfterLoad(boolean))(boolean openWindowAfterLoad)`

`void`
`[showNotification](#showNotification(com.nomagic.magicdraw.ui.notification.Notification))([Notification](Notification.html) notification)`
Shows application level notification in right bottom corner with default display parameters.
`void`
`[showNotification](#showNotification(com.nomagic.magicdraw.ui.notification.Notification,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig))([Notification](Notification.html) notification,
 [NotificationViewConfig](config/NotificationViewConfig.html) config)`
Shows application level notification in right bottom corner with display parameters specified in config object.
`void`
`[showNotification](#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component))([Notification](Notification.html) notification,
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)`
Shows application or container level notification with default display parameters.
`void`
`[showNotification](#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig))([Notification](Notification.html) notification,
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 [NotificationViewConfig](config/NotificationViewConfig.html) config)`
Shows application or container level notification with specified display parameters.
`void`
`[showNotification](#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig,boolean))([Notification](Notification.html) notification,
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 [NotificationViewConfig](config/NotificationViewConfig.html) config,
 boolean showInLog)`
Shows application or container level notification with specified display parameters.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NotificationManager
protected NotificationManager()
Creates new Notification manager instance.
 Constructor made protected to implement singleton pattern
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [NotificationManager](NotificationManager.html) getInstance()
Returns single Notification manger instance
Returns:
Notification manager instance
openNotificationWindow
public void openNotificationWindow([Notification](Notification.html) notification,
 boolean openWindow)
Shows notification in notification window
Parameters:
`notification` - notification
`openWindow` - flag, if true opens notification window
setOpenWindowAfterLoad
public static void setOpenWindowAfterLoad(boolean openWindowAfterLoad)
isOpenWindowAfterLoad
public static boolean isOpenWindowAfterLoad()
setHasNewMessages
public static void setHasNewMessages(boolean hasNewMessages)
hasNewMessages
public static boolean hasNewMessages()
showNotification
public void showNotification([Notification](Notification.html) notification)
Shows application level notification in right bottom corner with default display parameters.
Parameters:
`notification` - notification to show
showNotification
public void showNotification([Notification](Notification.html) notification,
 [NotificationViewConfig](config/NotificationViewConfig.html) config)
Shows application level notification in right bottom corner with display parameters specified in config object.
Parameters:
`notification` - notification to show
`config` - notification display parameters
showNotification
public void showNotification([Notification](Notification.html) notification,
 @CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)
Shows application or container level notification with default display parameters. If owner is not null and
 implements NotificationsContainer interface, the notification is displayed in owner's specific display area.
Parameters:
`notification` - notification to show
`owner` - notification display container
showNotification
public void showNotification([Notification](Notification.html) notification,
 @CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 @CheckForNull
 [NotificationViewConfig](config/NotificationViewConfig.html) config)
Shows application or container level notification with specified display parameters. If owner is not null
 and implements NotificationsContainer interface, the notification is displayed in owner's specific display area.
Parameters:
`notification` - notification to show
`owner` - notification display container
`config` - notification display parameters
showNotification
public void showNotification([Notification](Notification.html) notification,
 @CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner,
 @CheckForNull
 [NotificationViewConfig](config/NotificationViewConfig.html) config,
 boolean showInLog)
Shows application or container level notification with specified display parameters. If owner is not null
 and implements NotificationsContainer interface, the notification is displayed in owner's specific display area.
Parameters:
`notification` - notification to show
`owner` - notification display container
`config` - notification display parameters
`showInLog` - determines if the notification will be logged in the Notification Window
hideNotifications
public void hideNotifications([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)
Hides notifications with specified id
Parameters:
`notificationID` - notification id
hideNotifications
public void hideNotifications(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) owner)
Hides all notifications for component.
isNotificationVisible
public boolean isNotificationVisible([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)
Returns true if notification with specified id is shown
Parameters:
`notificationID` - notification id
logHyperlinkedTextNotifications
public void logHyperlinkedTextNotifications([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> callbacks)
Logs hyperlinked text to Notification window without displaying balloon message.
Parameters:
`text` - text with hyper links.
`callbacks` - callbacks that will be executed when link in text is selected
getApplicationNotificationsBuilder
public [NotificationViewBuilder](NotificationViewBuilder.html) getApplicationNotificationsBuilder()
Returns builder that creates and displays application notifications
Returns:
builder that creates and displays application notifications
setApplicationNotificationsBuilder
public void setApplicationNotificationsBuilder([NotificationViewBuilder](NotificationViewBuilder.html) applicationNotificationsBuilder)
Sets builder that creates and displays application notifications
Parameters:
`applicationNotificationsBuilder` - builder that creates and displays application notifications
getContainerNotificationsBuilder
public [NotificationViewBuilder](NotificationViewBuilder.html) getContainerNotificationsBuilder()
Returns builder that creates and displays container notifications
Returns:
builder that creates and displays container notifications
getContainerNotifications
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AbstractNotification](AbstractNotification.html)> getContainerNotifications([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) notificationID)
setContainerNotificationsBuilder
public void setContainerNotificationsBuilder([NotificationViewBuilder](NotificationViewBuilder.html) containerNotificationsBuilder)
Sets builder that creates and displays container notifications
Parameters:
`containerNotificationsBuilder` - builder that creates and displays container notifications
getApplicationNotificationGroupBuilder
public [NotificationViewBuilder](NotificationViewBuilder.html) getApplicationNotificationGroupBuilder()
Returns builder that creates and displays grouped application notifications
Returns:
builder that creates and displays grouped application notifications
setApplicationNotificationGroupBuilder
public void setApplicationNotificationGroupBuilder([NotificationViewBuilder](NotificationViewBuilder.html) applicationNotificationGroupBuilder)
Sets builder that creates and displays grouped application notifications
Parameters:
`applicationNotificationGroupBuilder` - builder that creates and displays grouped application notifications
getErrorConfig
public [NotificationViewConfig](config/NotificationViewConfig.html) getErrorConfig()
Returns display parameters for notification with severity error
Returns:
display parameters for notification with severity error
getWarningConfig
public [NotificationViewConfig](config/NotificationViewConfig.html) getWarningConfig()
Returns display parameters for notification with severity warning
Returns:
display parameters for notification with severity warning
getInfoConfig
public [NotificationViewConfig](config/NotificationViewConfig.html) getInfoConfig()
Returns display parameters for notification with severity info
Returns:
display parameters for notification with severity info
getConfig
public [NotificationViewConfig](config/NotificationViewConfig.html) getConfig([Notification](Notification.html) notification)
Helper method that returns predefined display parameters determined by notification severity level.
Parameters:
`notification` - notification for which display parameters should be returned
Returns:
notification display parameters specific to its severity
addNotificationShowingConfigurator
public void addNotificationShowingConfigurator([Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Notification](Notification.html)> notificationShowingConfigurator)
Adds custom logic configurator in order to limit shown notifications.
Parameters:
`notificationShowingConfigurator` - configurator which limits shown notifications. Should return true
 if notification should be shown.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification</a></div>
<h1 class="title" title="Class NotificationManager">Class NotificationManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.NotificationManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">NotificationManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Entry point to display notifications in MagicDraw. Two types of notifications can be displayed: application level and
 container level. Container lever notifications are displayed in special container that implements
 NotificationsContainer interface. When show notification method is called component owner parameter should point
 to notification container. If application level notification must be displayed, null parameter should be passed as
 component owner.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NotificationManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new Notification manager instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addNotificationShowingConfigurator(java.util.function.Predicate)">addNotificationShowingConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a>&gt; notificationShowingConfigurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds custom logic configurator in order to limit shown notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getApplicationNotificationGroupBuilder()">getApplicationNotificationGroupBuilder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns builder that creates and displays grouped application notifications</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getApplicationNotificationsBuilder()">getApplicationNotificationsBuilder</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns builder that creates and displays application notifications</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfig(com.nomagic.magicdraw.ui.notification.Notification)">getConfig</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Helper method that returns predefined display parameters determined by notification severity level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainerNotifications(java.lang.String)">getContainerNotifications</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainerNotificationsBuilder()">getContainerNotificationsBuilder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns builder that creates and displays container notifications</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorConfig()">getErrorConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns display parameters for notification with severity error</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInfoConfig()">getInfoConfig</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns display parameters for notification with severity info</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="NotificationManager.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns single Notification manger instance</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWarningConfig()">getWarningConfig</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns display parameters for notification with severity warning</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasNewMessages()">hasNewMessages</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hideNotifications(java.awt.Component)">hideNotifications</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hides all notifications for component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hideNotifications(java.lang.String)">hideNotifications</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hides notifications with specified id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNotificationVisible(java.lang.String)">isNotificationVisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if notification with specified id is shown</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOpenWindowAfterLoad()">isOpenWindowAfterLoad</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#logHyperlinkedTextNotifications(java.lang.String,java.util.Map)">logHyperlinkedTextNotifications</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; callbacks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs hyperlinked text to Notification window without displaying balloon message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openNotificationWindow(com.nomagic.magicdraw.ui.notification.Notification,boolean)">openNotificationWindow</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 boolean openWindow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows notification in notification window</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplicationNotificationGroupBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">setApplicationNotificationGroupBuilder</a><wbr/>(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> applicationNotificationGroupBuilder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets builder that creates and displays grouped application notifications</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplicationNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">setApplicationNotificationsBuilder</a><wbr/>(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> applicationNotificationsBuilder)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets builder that creates and displays application notifications</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContainerNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">setContainerNotificationsBuilder</a><wbr/>(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> containerNotificationsBuilder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets builder that creates and displays container notifications</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setHasNewMessages(boolean)">setHasNewMessages</a><wbr/>(boolean hasNewMessages)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpenWindowAfterLoad(boolean)">setOpenWindowAfterLoad</a><wbr/>(boolean openWindowAfterLoad)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showNotification(com.nomagic.magicdraw.ui.notification.Notification)">showNotification</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows application level notification in right bottom corner with default display parameters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showNotification(com.nomagic.magicdraw.ui.notification.Notification,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">showNotification</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows application level notification in right bottom corner with display parameters specified in config object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component)">showNotification</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows application or container level notification with default display parameters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">showNotification</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows application or container level notification with specified display parameters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig,boolean)">showNotification</a><wbr/>(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config,
 boolean showInLog)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows application or container level notification with specified display parameters.</div>
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
<h3>NotificationManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">NotificationManager</span>()</div>
<div class="block">Creates new Notification manager instance.
 Constructor made protected to implement singleton pattern</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="NotificationManager.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns single Notification manger instance</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Notification manager instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openNotificationWindow(com.nomagic.magicdraw.ui.notification.Notification,boolean)">
<h3>openNotificationWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openNotificationWindow</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 boolean openWindow)</span></div>
<div class="block">Shows notification in notification window</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification</dd>
<dd><code>openWindow</code> - flag, if true opens notification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpenWindowAfterLoad(boolean)">
<h3>setOpenWindowAfterLoad</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOpenWindowAfterLoad</span><wbr/><span class="parameters">(boolean openWindowAfterLoad)</span></div>
</section>
</li>
<li>
<section class="detail" id="isOpenWindowAfterLoad()">
<h3>isOpenWindowAfterLoad</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOpenWindowAfterLoad</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHasNewMessages(boolean)">
<h3>setHasNewMessages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setHasNewMessages</span><wbr/><span class="parameters">(boolean hasNewMessages)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasNewMessages()">
<h3>hasNewMessages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasNewMessages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="showNotification(com.nomagic.magicdraw.ui.notification.Notification)">
<h3>showNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showNotification</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification)</span></div>
<div class="block">Shows application level notification in right bottom corner with default display parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification to show</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNotification(com.nomagic.magicdraw.ui.notification.Notification,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">
<h3>showNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showNotification</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</span></div>
<div class="block">Shows application level notification in right bottom corner with display parameters specified in config object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification to show</dd>
<dd><code>config</code> - notification display parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component)">
<h3>showNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showNotification</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</span></div>
<div class="block">Shows application or container level notification with default display parameters. If owner is not null and
 implements NotificationsContainer interface, the notification is displayed in owner's specific display area.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification to show</dd>
<dd><code>owner</code> - notification display container</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig)">
<h3>showNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showNotification</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 @CheckForNull
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config)</span></div>
<div class="block">Shows application or container level notification with specified display parameters. If owner is not null
 and implements NotificationsContainer interface, the notification is displayed in owner's specific display area.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification to show</dd>
<dd><code>owner</code> - notification display container</dd>
<dd><code>config</code> - notification display parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showNotification(com.nomagic.magicdraw.ui.notification.Notification,java.awt.Component,com.nomagic.magicdraw.ui.notification.config.NotificationViewConfig,boolean)">
<h3>showNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showNotification</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner,
 @CheckForNull
 <a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a> config,
 boolean showInLog)</span></div>
<div class="block">Shows application or container level notification with specified display parameters. If owner is not null
 and implements NotificationsContainer interface, the notification is displayed in owner's specific display area.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification to show</dd>
<dd><code>owner</code> - notification display container</dd>
<dd><code>config</code> - notification display parameters</dd>
<dd><code>showInLog</code> - determines if the notification will be logged in the Notification Window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideNotifications(java.lang.String)">
<h3>hideNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">hideNotifications</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</span></div>
<div class="block">Hides notifications with specified id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notificationID</code> - notification id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideNotifications(java.awt.Component)">
<h3>hideNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">hideNotifications</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> owner)</span></div>
<div class="block">Hides all notifications for component.</div>
</section>
</li>
<li>
<section class="detail" id="isNotificationVisible(java.lang.String)">
<h3>isNotificationVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNotificationVisible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</span></div>
<div class="block">Returns true if notification with specified id is shown</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notificationID</code> - notification id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logHyperlinkedTextNotifications(java.lang.String,java.util.Map)">
<h3>logHyperlinkedTextNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">logHyperlinkedTextNotifications</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; callbacks)</span></div>
<div class="block">Logs hyperlinked text to Notification window without displaying balloon message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text with hyper links.</dd>
<dd><code>callbacks</code> - callbacks that will be executed when link in text is selected</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplicationNotificationsBuilder()">
<h3>getApplicationNotificationsBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></span> <span class="element-name">getApplicationNotificationsBuilder</span>()</div>
<div class="block">Returns builder that creates and displays application notifications</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>builder that creates and displays application notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplicationNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">
<h3>setApplicationNotificationsBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplicationNotificationsBuilder</span><wbr/><span class="parameters">(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> applicationNotificationsBuilder)</span></div>
<div class="block">Sets builder that creates and displays application notifications</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>applicationNotificationsBuilder</code> - builder that creates and displays application notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainerNotificationsBuilder()">
<h3>getContainerNotificationsBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></span> <span class="element-name">getContainerNotificationsBuilder</span>()</div>
<div class="block">Returns builder that creates and displays container notifications</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>builder that creates and displays container notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainerNotifications(java.lang.String)">
<h3>getContainerNotifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a>&gt;</span> <span class="element-name">getContainerNotifications</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationID)</span></div>
</section>
</li>
<li>
<section class="detail" id="setContainerNotificationsBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">
<h3>setContainerNotificationsBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContainerNotificationsBuilder</span><wbr/><span class="parameters">(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> containerNotificationsBuilder)</span></div>
<div class="block">Sets builder that creates and displays container notifications</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>containerNotificationsBuilder</code> - builder that creates and displays container notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplicationNotificationGroupBuilder()">
<h3>getApplicationNotificationGroupBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a></span> <span class="element-name">getApplicationNotificationGroupBuilder</span>()</div>
<div class="block">Returns builder that creates and displays grouped application notifications</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>builder that creates and displays grouped application notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplicationNotificationGroupBuilder(com.nomagic.magicdraw.ui.notification.NotificationViewBuilder)">
<h3>setApplicationNotificationGroupBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplicationNotificationGroupBuilder</span><wbr/><span class="parameters">(<a href="NotificationViewBuilder.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationViewBuilder</a> applicationNotificationGroupBuilder)</span></div>
<div class="block">Sets builder that creates and displays grouped application notifications</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>applicationNotificationGroupBuilder</code> - builder that creates and displays grouped application notifications</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getErrorConfig()">
<h3>getErrorConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></span> <span class="element-name">getErrorConfig</span>()</div>
<div class="block">Returns display parameters for notification with severity error</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>display parameters for notification with severity error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarningConfig()">
<h3>getWarningConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></span> <span class="element-name">getWarningConfig</span>()</div>
<div class="block">Returns display parameters for notification with severity warning</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>display parameters for notification with severity warning</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInfoConfig()">
<h3>getInfoConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></span> <span class="element-name">getInfoConfig</span>()</div>
<div class="block">Returns display parameters for notification with severity info</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>display parameters for notification with severity info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfig(com.nomagic.magicdraw.ui.notification.Notification)">
<h3>getConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="config/NotificationViewConfig.html" title="class in com.nomagic.magicdraw.ui.notification.config">NotificationViewConfig</a></span> <span class="element-name">getConfig</span><wbr/><span class="parameters">(<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification)</span></div>
<div class="block">Helper method that returns predefined display parameters determined by notification severity level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification for which display parameters should be returned</dd>
<dt>Returns:</dt>
<dd>notification display parameters specific to its severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNotificationShowingConfigurator(java.util.function.Predicate)">
<h3>addNotificationShowingConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addNotificationShowingConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a>&gt; notificationShowingConfigurator)</span></div>
<div class="block">Adds custom logic configurator in order to limit shown notifications.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notificationShowingConfigurator</code> - configurator which limits shown notifications. Should return true
                                        if notification should be shown.</dd>
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
