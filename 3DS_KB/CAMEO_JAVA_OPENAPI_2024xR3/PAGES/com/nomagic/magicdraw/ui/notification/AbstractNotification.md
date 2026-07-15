# JAVA OPENAPI: AbstractNotification (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/notification/AbstractNotification.html
- source_path: `com/nomagic/magicdraw/ui/notification/AbstractNotification.html`
- source_sha256: `ffacada75975262bc0ea77c956ed72d152c03a2a294dd27559fc708a1262ccbd`
- captured_utc: `2026-07-14T16:55:53.069430+00:00`

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

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractNotification](#%3Cinit%3E())()`

`[AbstractNotification](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Defines notification constructor with unique id, text and empty title.
`[AbstractNotification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Defines notification constructor with unique id, title and text.
`[AbstractNotification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [HRefRunnable](HRefRunnable.html)[] actions)`
Defines notification constructor with unique id, title, text and list of href actions.
`[AbstractNotification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)`
Defines notification constructor with unique id, title, short and long description.
`[AbstractNotification](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 [HRefRunnable](HRefRunnable.html)[] actions)`
Defines notification constructor with unique id, title, text and list of href actions.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final void`
`[addAllHRefActions](#addAllHRefActions(com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D))([HRefRunnable](HRefRunnable.html)[] hrefActions)`
Adds array of href actions to already existing list of actions.
`void`
`[addHRefAction](#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable))([HRefRunnable](HRefRunnable.html) r)`
Adds href action to list of already existing list of actions.
`boolean`
`[canDisable](#canDisable())()`
Indicates if notification message can be disabled and will not be displayed anymore.
`protected void`
`[clearAllHRefActions](#clearAllHRefActions())()`
Removes all href actions from notification.
`[HRefRunnable](HRefRunnable.html)[]`
`[getAllHRefActions](#getAllHRefActions())()`
Returns array of all href actions.
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
`[setCanDisable](#setCanDisable(boolean))(boolean canDisable)`
Sets notification ability to be disabled permanently by user.
`void`
`[setCanDisable](#setCanDisable(boolean,com.nomagic.magicdraw.ui.notification.HideNotificationRunnable))(boolean canDisable,
 com.nomagic.magicdraw.ui.notification.HideNotificationRunnable actionOnDisable)`
Sets notification ability to be disabled permanently by user.
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

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractNotification
public AbstractNotification()
AbstractNotification
public AbstractNotification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Defines notification constructor with unique id, text and empty title.
Parameters:
`id` - notification unique id
`text` - notification message text
AbstractNotification
public AbstractNotification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Defines notification constructor with unique id, title and text.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification message text
AbstractNotification
public AbstractNotification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText)
Defines notification constructor with unique id, title, short and long description.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification short message text
`longText` - notification long message text
AbstractNotification
public AbstractNotification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions)
Defines notification constructor with unique id, title, text and list of href actions.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification message text
`actions` - list of href controls
AbstractNotification
public AbstractNotification([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) longText,
 @CheckForNull
 [HRefRunnable](HRefRunnable.html)[] actions)
Defines notification constructor with unique id, title, text and list of href actions.
Parameters:
`id` - notification unique id
`title` - notification title
`text` - notification message text
`longText` - notification long text
`actions` - list of href controls
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
addAllHRefActions
public final void addAllHRefActions(@CheckForNull
 [HRefRunnable](HRefRunnable.html)[] hrefActions)
Adds array of href actions to already existing list of actions.
Parameters:
`hrefActions` - array of href actions to add
getAllHRefActions
public [HRefRunnable](HRefRunnable.html)[] getAllHRefActions()
Returns array of all href actions.
Returns:
array of href actions
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
clearAllHRefActions
protected void clearAllHRefActions()
Removes all href actions from notification.
canDisable
public boolean canDisable()
Indicates if notification message can be disabled and will not be displayed anymore. If the flag is set to true,
 when notification is shown, user will be present with ability to disable it. Disabled notification id will be
 saved in environment options and not shown anymore.
Returns:
true if notification can be disabled
setCanDisable
public void setCanDisable(boolean canDisable)
Sets notification ability to be disabled permanently by user. If canDisabled property is set to true, when
 notification is shown, user will be present with ability to disable it.
Parameters:
`canDisable` - notification disable status.
setCanDisable
public void setCanDisable(boolean canDisable,
 com.nomagic.magicdraw.ui.notification.HideNotificationRunnable actionOnDisable)
Sets notification ability to be disabled permanently by user. If canDisabled property is set to true, when
 notification is shown, user will be presented with ability to disable it.
Parameters:
`canDisable` - notification disable status.
`actionOnDisable` - action to be executed when notification is disabled and closed.

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
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractNotification</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">AbstractNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color">
<div class="block">Defines notification constructor with unique id, text and empty title.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">AbstractNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color">
<div class="block">Defines notification constructor with unique id, title and text.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D)">AbstractNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</code></div>
<div class="col-last odd-row-color">
<div class="block">Defines notification constructor with unique id, title, text and list of href actions.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">AbstractNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</code></div>
<div class="col-last even-row-color">
<div class="block">Defines notification constructor with unique id, title, short and long description.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D)">AbstractNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</code></div>
<div class="col-last odd-row-color">
<div class="block">Defines notification constructor with unique id, title, text and list of href actions.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAllHRefActions(com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D)">addAllHRefActions</a><wbr/>(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] hrefActions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds array of href actions to already existing list of actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHRefAction(com.nomagic.magicdraw.ui.notification.HRefRunnable)">addHRefAction</a><wbr/>(<a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds href action to list of already existing list of actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDisable()">canDisable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if notification message can be disabled and will not be displayed anymore.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAllHRefActions()">clearAllHRefActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all href actions from notification.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllHRefActions()">getAllHRefActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns array of all href actions.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanDisable(boolean)">setCanDisable</a><wbr/>(boolean canDisable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification ability to be disabled permanently by user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanDisable(boolean,com.nomagic.magicdraw.ui.notification.HideNotificationRunnable)">setCanDisable</a><wbr/>(boolean canDisable,
 com.nomagic.magicdraw.ui.notification.HideNotificationRunnable actionOnDisable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification ability to be disabled permanently by user.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Defines notification constructor with unique id, text and empty title.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>text</code> - notification message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Defines notification constructor with unique id, title and text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText)</span></div>
<div class="block">Defines notification constructor with unique id, title, short and long description.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification short message text</dd>
<dd><code>longText</code> - notification long message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[])">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</span></div>
<div class="block">Defines notification constructor with unique id, title, text and list of href actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification message text</dd>
<dd><code>actions</code> - list of href controls</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[])">
<h3>AbstractNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractNotification</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> longText,
 @CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions)</span></div>
<div class="block">Defines notification constructor with unique id, title, text and list of href actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - notification unique id</dd>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification message text</dd>
<dd><code>longText</code> - notification long text</dd>
<dd><code>actions</code> - list of href controls</dd>
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
<section class="detail" id="addAllHRefActions(com.nomagic.magicdraw.ui.notification.HRefRunnable[])">
<h3>addAllHRefActions</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addAllHRefActions</span><wbr/><span class="parameters">(@CheckForNull
 <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] hrefActions)</span></div>
<div class="block">Adds array of href actions to already existing list of actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hrefActions</code> - array of href actions to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllHRefActions()">
<h3>getAllHRefActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[]</span> <span class="element-name">getAllHRefActions</span>()</div>
<div class="block">Returns array of all href actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>array of href actions</dd>
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
<li>
<section class="detail" id="clearAllHRefActions()">
<h3>clearAllHRefActions</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearAllHRefActions</span>()</div>
<div class="block">Removes all href actions from notification.</div>
</section>
</li>
<li>
<section class="detail" id="canDisable()">
<h3>canDisable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDisable</span>()</div>
<div class="block">Indicates if notification message can be disabled and will not be displayed anymore. If the flag is set to true,
 when notification is shown, user will be present with ability to disable it. Disabled notification id will be
 saved in environment options and not shown anymore.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if notification can be disabled</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCanDisable(boolean)">
<h3>setCanDisable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanDisable</span><wbr/><span class="parameters">(boolean canDisable)</span></div>
<div class="block">Sets notification ability to be disabled permanently by user. If canDisabled property is set to true, when
 notification is shown, user will be present with ability to disable it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canDisable</code> - notification disable status.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCanDisable(boolean,com.nomagic.magicdraw.ui.notification.HideNotificationRunnable)">
<h3>setCanDisable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanDisable</span><wbr/><span class="parameters">(boolean canDisable,
 com.nomagic.magicdraw.ui.notification.HideNotificationRunnable actionOnDisable)</span></div>
<div class="block">Sets notification ability to be disabled permanently by user. If canDisabled property is set to true, when
 notification is shown, user will be presented with ability to disable it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canDisable</code> - notification disable status.</dd>
<dd><code>actionOnDisable</code> - action to be executed when notification is disabled and closed.</dd>
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
