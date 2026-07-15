# JAVA OPENAPI: Notification (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/notification/Notification.html
- source_path: `com/nomagic/magicdraw/ui/notification/Notification.html`
- source_sha256: `10f77a659980189e40534dc4b0d69ec170da52517599a1cc1b71a4830bb06f3b`
- captured_utc: `2026-07-14T16:52:04.517779+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification](package-summary.html)

## Class Notification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.ui.notification.AbstractNotification](AbstractNotification.html)
com.nomagic.magicdraw.ui.notification.Notification

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classNotification
extends [AbstractNotification](AbstractNotification.html)
implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)

This class contains data used to construct and display MagicDraw notification. Notification can
 be displayed as separate popup in lower right corner or in designated area of control.

**NOTE:** although HTML tags are supported, the notification title/text should not be wrapped
 into <html><body></body></html> tags as during the construction of the
 notification's popup, such wrapping is already done by the notification manager.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.ui.notification.Notification)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[Notification.Context](Notification.Context.html)`
Context enum indicates notification origin.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Notification](#%3Cinit%3E())()`

`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Constructs notification with specified id and title.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Constructs notification with specified id, title and text.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [HRefRunnable](HRefRunnable.html)[] actions)`
Constructs notification with specified id, title, text and list of actions user can perform
 upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity)`
Constructs notification with specified id, title, text, severity and list of actions user can perform
 upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity,
 [Notification.Context](Notification.Context.html) context)`
Constructs notification with specified id, title, text, severity, context and list of actions user can perform
 upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](NotificationSeverity.html) severity)`
Constructs notification with specified id, title, text and severity.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)`
Constructs notification with specified id, title, short and long text description.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [HRefRunnable](HRefRunnable.html)[] actions)`
Constructs notification with specified id, title, short description, long description and list of actions user
 can perform upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity)`
Constructs notification with specified id, title, short text, long text, severity and list of actions user
 can perform upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity,
 [Notification.Context](Notification.Context.html) context)`
Constructs notification with specified id, title, short text, long text, severity, context and list of actions user can perform
 upon notification.
`[Notification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [NotificationSeverity](NotificationSeverity.html) severity)`
Constructs notification with specified id, title, short description, long description and severity.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`[Notification.Context](Notification.Context.html)`
`[getContext](#getContext())()`
Returns notification context
`[NotificationSeverity](NotificationSeverity.html)`
`[getSeverity](#getSeverity())()`
Returns notification severity
`int`
`[hashCode](#hashCode())()`

`boolean`
`[isLogExpanded](#isLogExpanded())()`

`void`
`[setContext](#setContext(com.nomagic.magicdraw.ui.notification.Notification.Context))([Notification.Context](Notification.Context.html) context)`
Sets new notification context
`void`
`[setLogExpanded](#setLogExpanded(boolean))(boolean logExpanded)`

`void`
`[setLongText](#setLongText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)`
Sets notification long text
`void`
`[setSeverity](#setSeverity(com.nomagic.magicdraw.ui.notification.NotificationSeverity))([NotificationSeverity](NotificationSeverity.html) severity)`
Sets notification severity
Methods inherited from class com.nomagic.magicdraw.ui.notification.[AbstractNotification](AbstractNotification.html)
`[addHRefAction](AbstractNotification.html#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)), [getHRefAction](AbstractNotification.html#getHRefAction(java.lang.String)), [getID](AbstractNotification.html#getID()), [getLongText](AbstractNotification.html#getLongText()), [getText](AbstractNotification.html#getText()), [getTitle](AbstractNotification.html#getTitle()), [removeHRefAction](AbstractNotification.html#removeHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)), [removeHRefAction](AbstractNotification.html#removeHRefAction(java.lang.String)), [setText](AbstractNotification.html#setText(java.lang.String)), [setTitle](AbstractNotification.html#setTitle(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Notification
public Notification()
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Constructs notification with specified id and title. Default ENVIRONMENT context and INFO
 severity is used while creating notification. No actions or text is set for this notification
Parameters:
`id` - notification unique id
`title` - notification title
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Constructs notification with specified id, title and text. Default ENVIRONMENT context and INFO
 severity is used while creating notification. No actions are set for this notification
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)
Constructs notification with specified id, title, short and long text description. Default ENVIRONMENT context
 and INFO severity is used while creating notification. No actions are set for this notification
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`longText` - notification long text
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](NotificationSeverity.html) severity)
Constructs notification with specified id, title, text and severity. Default ENVIRONMENT context is used
 while creating notification. No actions are set for this notification
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`severity` - notification severity
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [NotificationSeverity](NotificationSeverity.html) severity)
Constructs notification with specified id, title, short description, long description and severity.
 Default ENVIRONMENT context is used while creating notification. No actions are set for this notification
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`longText` - notification long text
`severity` - notification severity
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions)
Constructs notification with specified id, title, text and list of actions user can perform
 upon notification. Default ENVIRONMENT context and severity INFO is set while creating notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`actions` - list of actions user can take
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions)
Constructs notification with specified id, title, short description, long description and list of actions user
 can perform upon notification. Default ENVIRONMENT context and severity INFO is set while creating notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`longText` - notification long text
`actions` - list of actions user can take
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity)
Constructs notification with specified id, title, text, severity and list of actions user can perform
 upon notification. Default ENVIRONMENT context is set while creating notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`actions` - list of actions user can take
`severity` - notification severity level
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity)
Constructs notification with specified id, title, short text, long text, severity and list of actions user
 can perform upon notification. Default ENVIRONMENT context is set while creating notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`actions` - list of actions user can take
`severity` - notification severity level
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity,
 [Notification.Context](Notification.Context.html) context)
Constructs notification with specified id, title, text, severity, context and list of actions user can perform
 upon notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`actions` - list of actions user can take
`severity` - notification severity level
`context` - notification context
Notification
public Notification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions,
 [NotificationSeverity](NotificationSeverity.html) severity,
 [Notification.Context](Notification.Context.html) context)
Constructs notification with specified id, title, short text, long text, severity, context and list of actions user can perform
 upon notification.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification text
`longText` - notification long text
`actions` - list of actions user can take
`severity` - notification severity level
`context` - notification context
 ============ METHOD DETAIL ========== 
Method Details
getSeverity
public [NotificationSeverity](NotificationSeverity.html) getSeverity()
Returns notification severity
Returns:
notification severity
setSeverity
public void setSeverity([NotificationSeverity](NotificationSeverity.html) severity)
Sets notification severity
Parameters:
`severity` - new notification severity
getContext
public [Notification.Context](Notification.Context.html) getContext()
Returns notification context
Returns:
notification context
setContext
public void setContext([Notification.Context](Notification.Context.html) context)
Sets new notification context
Parameters:
`context` - notification context
setLongText
public void setLongText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)
Description copied from class: `[AbstractNotification](AbstractNotification.html#setLongText(java.lang.String))`
Sets notification long text
Overrides:
`[setLongText](AbstractNotification.html#setLongText(java.lang.String))` in class `[AbstractNotification](AbstractNotification.html)`
Parameters:
`longText` - notification long text
isLogExpanded
public boolean isLogExpanded()
setLogExpanded
public void setLogExpanded(boolean logExpanded)
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification</a></div>
<h1 class="title" title="Class Notification">Class Notification</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">com.nomagic.magicdraw.ui.notification.AbstractNotification</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.Notification</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Notification</span>
<span class="extends-implements">extends <a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block"><p>
 This class contains data used to construct and display MagicDraw notification. Notification can
 be displayed as separate popup in lower right corner or in designated area of control.

<b>NOTE:</b> although HTML tags are supported, the notification title/text should not be wrapped
 into &lt;html&gt;&lt;body&gt;&lt;/body&gt;&lt;/html&gt; tags as during the construction of the
 notification's popup, such wrapping is already done by the notification manager.
 </p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.ui.notification.Notification">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a></code></div>
<div class="col-last even-row-color">
<div class="block">Context enum indicates notification origin.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Notification</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id and title.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs notification with specified id, title and text.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id, title, text and list of actions user can perform
 upon notification.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs notification with specified id, title, text, severity and list of actions user can perform
 upon notification.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id, title, text, severity, context and list of actions user can perform
 upon notification.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs notification with specified id, title, text and severity.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id, title, short and long text description.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs notification with specified id, title, short description, long description and list of actions user
 can perform upon notification.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id, title, short text, long text, severity and list of actions user
 can perform upon notification.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs notification with specified id, title, short text, long text, severity, context and list of actions user can perform
 upon notification.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">Notification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs notification with specified id, title, short description, long description and severity.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification context</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverity()">getSeverity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification severity</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLogExpanded()">isLogExpanded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContext(com.nomagic.magicdraw.ui.notification.Notification.Context)">setContext</a><wbr/>(<a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new notification context</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLogExpanded(boolean)">setLogExpanded</a><wbr/>(boolean logExpanded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLongText(java.lang.String)">setLongText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification long text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeverity(com.nomagic.magicdraw.ui.notification.NotificationSeverity)">setSeverity</a><wbr/>(<a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification severity</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.notification.AbstractNotification">Methods inherited from class com.nomagic.magicdraw.ui.notification.<a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a></h3>
<code><a href="AbstractNotification.html#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">addHRefAction</a>, <a href="AbstractNotification.html#getHRefAction(java.lang.String)">getHRefAction</a>, <a href="AbstractNotification.html#getID()">getID</a>, <a href="AbstractNotification.html#getLongText()">getLongText</a>, <a href="AbstractNotification.html#getText()">getText</a>, <a href="AbstractNotification.html#getTitle()">getTitle</a>, <a href="AbstractNotification.html#removeHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">removeHRefAction</a>, <a href="AbstractNotification.html#removeHRefAction(java.lang.String)">removeHRefAction</a>, <a href="AbstractNotification.html#setText(java.lang.String)">setText</a>, <a href="AbstractNotification.html#setTitle(java.lang.String)">setTitle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Constructs notification with specified id and title. Default ENVIRONMENT context and INFO
 severity is used while creating notification. No actions or text is set for this notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Constructs notification with specified id, title and text. Default ENVIRONMENT context and INFO
 severity is used while creating notification. No actions are set for this notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</span></div>
<div class="block">Constructs notification with specified id, title, short and long text description. Default ENVIRONMENT context
 and INFO severity is used while creating notification. No actions are set for this notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>longText</code> - notification long text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</span></div>
<div class="block">Constructs notification with specified id, title, text and severity. Default ENVIRONMENT context is used
 while creating notification. No actions are set for this notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>severity</code> - notification severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</span></div>
<div class="block">Constructs notification with specified id, title, short description, long description and severity.
 Default ENVIRONMENT context is used while creating notification. No actions are set for this notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>longText</code> - notification long text</dd>
<dd><code>severity</code> - notification severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[])">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</span></div>
<div class="block">Constructs notification with specified id, title, text and list of actions user can perform
 upon notification. Default ENVIRONMENT context and severity INFO is set while creating notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[])">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</span></div>
<div class="block">Constructs notification with specified id, title, short description, long description and list of actions user
 can perform upon notification. Default ENVIRONMENT context and severity INFO is set while creating notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>longText</code> - notification long text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[],com.nomagic.magicdraw.ui.notification.NotificationSeverity)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</span></div>
<div class="block">Constructs notification with specified id, title, text, severity and list of actions user can perform
 upon notification. Default ENVIRONMENT context is set while creating notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
<dd><code>severity</code> - notification severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[],com.nomagic.magicdraw.ui.notification.NotificationSeverity)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</span></div>
<div class="block">Constructs notification with specified id, title, short text, long text, severity and list of actions user
 can perform upon notification. Default ENVIRONMENT context is set while creating notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
<dd><code>severity</code> - notification severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[],com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Constructs notification with specified id, title, text, severity, context and list of actions user can perform
 upon notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
<dd><code>severity</code> - notification severity level</dd>
<dd><code>context</code> - notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[],com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>Notification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Notification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Constructs notification with specified id, title, short text, long text, severity, context and list of actions user can perform
 upon notification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>longText</code> - notification long text</dd>
<dd><code>actions</code> - list of actions user can take</dd>
<dd><code>severity</code> - notification severity level</dd>
<dd><code>context</code> - notification context</dd>
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
<section class="detail" id="getSeverity()">
<h3>getSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a></span> <span class="element-name">getSeverity</span>()</div>
<div class="block">Returns notification severity</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSeverity(com.nomagic.magicdraw.ui.notification.NotificationSeverity)">
<h3>setSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeverity</span><wbr/><span class="parameters">(<a href="NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity)</span></div>
<div class="block">Sets notification severity</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>severity</code> - new notification severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Returns notification context</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContext(com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>setContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContext</span><wbr/><span class="parameters">(<a href="Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Sets new notification context</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLongText(java.lang.String)">
<h3>setLongText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractNotification.html#setLongText(java.lang.String)">AbstractNotification</a></code></span></div>
<div class="block">Sets notification long text</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractNotification.html#setLongText(java.lang.String)">setLongText</a></code> in class <code><a href="AbstractNotification.html" title="class in com.nomagic.magicdraw.ui.notification">AbstractNotification</a></code></dd>
<dt>Parameters:</dt>
<dd><code>longText</code> - notification long text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLogExpanded()">
<h3>isLogExpanded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLogExpanded</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLogExpanded(boolean)">
<h3>setLogExpanded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLogExpanded</span><wbr/><span class="parameters">(boolean logExpanded)</span></div>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
