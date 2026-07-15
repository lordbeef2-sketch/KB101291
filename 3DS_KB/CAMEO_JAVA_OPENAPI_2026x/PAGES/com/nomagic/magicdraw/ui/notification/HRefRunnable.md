# JAVA OPENAPI: HRefRunnable (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/notification/HRefRunnable.html
- source_path: `com/nomagic/magicdraw/ui/notification/HRefRunnable.html`
- source_sha256: `bbda1d1b73eb0fe96943182725dfa9d212627af898492323c88e5ad86b2210b2`
- captured_utc: `2026-07-14T16:58:25.939156+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.notification](package-summary.html)

## Class HRefRunnable

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.notification.HRefRunnable

All Implemented Interfaces:
`[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`

@OpenApiAllpublic abstract classHRefRunnable
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)

Represents action element in notification window. Action element contains id (href) and displayable text.
 CloseOnActivation flag indicates if notification message must be closed after action was selected.
 By default the element is rendered as HTML link. When action is selected the run method is called.
 Custom code can be executed by overriding run() method passing HRefRunnable to notification.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HREF_PREFIX](#HREF_PREFIX)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HRefRunnable](#%3Cinit%3E(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close)`
Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed.
`[HRefRunnable](#%3Cinit%3E(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close,
 boolean idleRequired)`
Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed.
`[HRefRunnable](#%3Cinit%3E(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close)`
Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.
`[HRefRunnable](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close,
 boolean idleRequired)`
Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [HRefRunnable](HRefRunnable.html)`
`[create](#create(java.lang.String,boolean,java.lang.Runnable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean closeOnActivation,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)`
Create href runnable
`static [HRefRunnable](HRefRunnable.html)`
`[createHRefRunnableForElement](#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static [HRefRunnable](HRefRunnable.html)`
`[createHRefRunnableForElement](#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeVersionForTW)`

`static [HRefRunnable](HRefRunnable.html)`
`[createHRefRunnableForElement](#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeVersionForTW,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branch)`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[formatHRef](#formatHRef(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href)`

`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getElementName](#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getHref](#getHref())()`
Returns runnable href id
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getHrefLink](#getHrefLink())()`
Creates HTML tags to have real hyperlink.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`
Returns href action text.
`int`
`[hashCode](#hashCode())()`

`boolean`
`[isCloseOnActivation](#isCloseOnActivation())()`
Indicates if notification will be closed after this action is selected for execution.
`boolean`
`[isIdleRequired](#isIdleRequired())()`

`boolean`
`[isVisible](#isVisible())()`
Indicates if action, representing href is rendered in notification
`boolean`
`[runIfIdle](#runIfIdle())()`
Run given runnable if application is in idle mode.
`boolean`
`[runIfIdle](#runIfIdle(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) preRun)`
Runs given runnable after preRun runnable was executed if application is in idle mode.
`void`
`[setCloseOnActivation](#setCloseOnActivation(boolean))(boolean closeOnActivation)`
Sets notification close flag for this runnable.
`void`
`[setHref](#setHref(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href)`
Sets href runnable id
`void`
`[setIdleRequired](#setIdleRequired(boolean))(boolean idleRequired)`
Set flag to indicate that idle mode is required to execute this runnable.
`void`
`[setText](#setText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Sets href action presentation text.
`void`
`[setVisible](#setVisible(boolean))(boolean visible)`
Sets visibility of action representing href.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.lang.[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)
`[run](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html#run())`

============ FIELD DETAIL =========== 
Field Details
HREF_PREFIX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HREF_PREFIX
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.notification.HRefRunnable.HREF_PREFIX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HRefRunnable
public HRefRunnable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close,
 boolean idleRequired)
Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.
Parameters:
`href` - runnable id
`text` - link text
`close` - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.
`idleRequired` - true if application must be in idle mode in order to execute this runnable
HRefRunnable
public HRefRunnable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close)
Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.
Parameters:
`href` - runnable id
`text` - link text
`close` - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.
HRefRunnable
public HRefRunnable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close)
Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed. Href id will be generated in format of http://n, where n is number.
Parameters:
`text` - link text
`close` - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.
HRefRunnable
public HRefRunnable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean close,
 boolean idleRequired)
Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed. Href id will be generated in format of http://n, where n is number.
Parameters:
`text` - link text
`close` - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.
`idleRequired` - true if application must be in idle mode in order to execute this runnable
 ============ METHOD DETAIL ========== 
Method Details
getElementName
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getElementName([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
createHRefRunnableForElement
public static [HRefRunnable](HRefRunnable.html) createHRefRunnableForElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
createHRefRunnableForElement
public static [HRefRunnable](HRefRunnable.html) createHRefRunnableForElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeVersionForTW)
createHRefRunnableForElement
public static [HRefRunnable](HRefRunnable.html) createHRefRunnableForElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean includeVersionForTW,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branch)
create
public static [HRefRunnable](HRefRunnable.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean closeOnActivation,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)
Create href runnable
Parameters:
`text` - text to display
`closeOnActivation` - true if notification should be closed clicked on text
`runnable` - runnable to run when click on text
Returns:
HRefRunnable
setHref
public void setHref(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href)
Sets href runnable id
Parameters:
`href` - runnable id
getHref
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getHref()
Returns runnable href id
Returns:
runnable href id
setCloseOnActivation
public void setCloseOnActivation(boolean closeOnActivation)
Sets notification close flag for this runnable. If set to true, notification wll be closed after href
 link was selected.
Parameters:
`closeOnActivation` - close flag. If set to true, notification wll be closed after href link was selected.
isCloseOnActivation
public boolean isCloseOnActivation()
Indicates if notification will be closed after this action is selected for execution.
Returns:
true if notification will be closed after this action is selected for execution
getText
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getText()
Returns href action text.
Returns:
href action text.
setText
public void setText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Sets href action presentation text.
Parameters:
`text` - new href action presentation text
isVisible
public boolean isVisible()
Indicates if action, representing href is rendered in notification
Returns:
true if action, representing href is rendered in notification
setVisible
public void setVisible(boolean visible)
Sets visibility of action representing href.
Parameters:
`visible` - visibility state of action representing href
getHrefLink
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getHrefLink()
Creates HTML tags to have real hyperlink.
Returns:
<a href="[`getHref()`](#getHref())">[`getText`](#getHref())t</a>.
formatHRef
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) formatHRef(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) href)
runIfIdle
public boolean runIfIdle()
Run given runnable if application is in idle mode. Otherwise show busy warning
Returns:
true if runnable was executed
runIfIdle
public boolean runIfIdle([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) preRun)
Runs given runnable after preRun runnable was executed if application is in idle mode. Otherwise show busy warning
Parameters:
`preRun` - executes before given runnable
Returns:
true if runnable was executed
setIdleRequired
public void setIdleRequired(boolean idleRequired)
Set flag to indicate that idle mode is required to execute this runnable.
Parameters:
`idleRequired` - set true if this runnable can be executed only while application is in idle mode
isIdleRequired
public boolean isIdleRequired()
Returns:
true if this runnable can be executed only while application is in idle mode
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.notification</a></div>
<h1 class="title" title="Class HRefRunnable">Class HRefRunnable</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.notification.HRefRunnable</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">HRefRunnable</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span></div>
<div class="block">Represents action element in notification window. Action element contains id (href) and displayable text.
 CloseOnActivation flag indicates if notification message must be closed after action was selected.
 By default the element is rendered as HTML link. When action is selected the run method is called.
 Custom code can be executed by overriding run() method passing HRefRunnable to notification.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HREF_PREFIX">HREF_PREFIX</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean)">HRefRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean,boolean)">HRefRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close,
 boolean idleRequired)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean)">HRefRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,boolean)">HRefRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close,
 boolean idleRequired)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,boolean,java.lang.Runnable)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean closeOnActivation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create href runnable</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createHRefRunnableForElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">createHRefRunnableForElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeVersionForTW)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String)">createHRefRunnableForElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeVersionForTW,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branch)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#formatHRef(java.lang.String)">formatHRef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHref()">getHref</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns runnable href id</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHrefLink()">getHrefLink</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates HTML tags to have real hyperlink.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns href action text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCloseOnActivation()">isCloseOnActivation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if notification will be closed after this action is selected for execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIdleRequired()">isIdleRequired</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisible()">isVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if action, representing href is rendered in notification</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runIfIdle()">runIfIdle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Run given runnable if application is in idle mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runIfIdle(java.lang.Runnable)">runIfIdle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> preRun)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Runs given runnable after preRun runnable was executed if application is in idle mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCloseOnActivation(boolean)">setCloseOnActivation</a><wbr/>(boolean closeOnActivation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets notification close flag for this runnable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHref(java.lang.String)">setHref</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets href runnable id</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIdleRequired(boolean)">setIdleRequired</a><wbr/>(boolean idleRequired)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set flag to indicate that idle mode is required to execute this runnable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.String)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets href action presentation text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisible(boolean)">setVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility of action representing href.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Runnable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html#run()" title="class or interface in java.lang">run</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="HREF_PREFIX">
<h3>HREF_PREFIX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HREF_PREFIX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.notification.HRefRunnable.HREF_PREFIX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,boolean,boolean)">
<h3>HRefRunnable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HRefRunnable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close,
 boolean idleRequired)</span></div>
<div class="block">Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - runnable id</dd>
<dd><code>text</code> - link text</dd>
<dd><code>close</code> - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.</dd>
<dd><code>idleRequired</code> - true if application must be in idle mode in order to execute this runnable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,boolean)">
<h3>HRefRunnable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HRefRunnable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close)</span></div>
<div class="block">Creates href runnable with specified href id, text as link and close boolean value indicating if notification
 must be closed after link was pressed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - runnable id</dd>
<dd><code>text</code> - link text</dd>
<dd><code>close</code> - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,boolean)">
<h3>HRefRunnable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HRefRunnable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close)</span></div>
<div class="block">Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed. Href id will be generated in format of http://n, where n is number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - link text</dd>
<dd><code>close</code> - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,boolean,boolean)">
<h3>HRefRunnable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HRefRunnable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean close,
 boolean idleRequired)</span></div>
<div class="block">Creates href runnable with specified text as link and close boolean value indicating if notification must be
 closed after link was pressed. Href id will be generated in format of http://n, where n is number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - link text</dd>
<dd><code>close</code> - indicates if notification must be closed after link was pressed. If set to true, notification will be closed.</dd>
<dd><code>idleRequired</code> - true if application must be in idle mode in order to execute this runnable</dd>
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
<section class="detail" id="getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createHRefRunnableForElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></span> <span class="element-name">createHRefRunnableForElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>createHRefRunnableForElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></span> <span class="element-name">createHRefRunnableForElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeVersionForTW)</span></div>
</section>
</li>
<li>
<section class="detail" id="createHRefRunnableForElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,java.lang.String)">
<h3>createHRefRunnableForElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></span> <span class="element-name">createHRefRunnableForElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean includeVersionForTW,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branch)</span></div>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,boolean,java.lang.Runnable)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean closeOnActivation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Create href runnable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to display</dd>
<dd><code>closeOnActivation</code> - true if notification should be closed clicked on text</dd>
<dd><code>runnable</code> - runnable to run when click on text</dd>
<dt>Returns:</dt>
<dd>HRefRunnable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHref(java.lang.String)">
<h3>setHref</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHref</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</span></div>
<div class="block">Sets href runnable id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>href</code> - runnable id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHref()">
<h3>getHref</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHref</span>()</div>
<div class="block">Returns runnable href id</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>runnable href id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCloseOnActivation(boolean)">
<h3>setCloseOnActivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCloseOnActivation</span><wbr/><span class="parameters">(boolean closeOnActivation)</span></div>
<div class="block">Sets notification close flag for this runnable. If set to true, notification wll be closed after href
 link was selected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>closeOnActivation</code> - close flag. If set to true, notification wll be closed after href link was selected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCloseOnActivation()">
<h3>isCloseOnActivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCloseOnActivation</span>()</div>
<div class="block">Indicates if notification will be closed after this action is selected for execution.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if notification will be closed after this action is selected for execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Returns href action text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>href action text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Sets href action presentation text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - new href action presentation text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisible()">
<h3>isVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVisible</span>()</div>
<div class="block">Indicates if action, representing href is rendered in notification</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if action, representing href is rendered in notification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisible(boolean)">
<h3>setVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<div class="block">Sets visibility of action representing href.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visible</code> - visibility state of action representing href</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHrefLink()">
<h3>getHrefLink</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHrefLink</span>()</div>
<div class="block">Creates HTML tags to have real hyperlink.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>&lt;a href="<a href="#getHref()"><code>getHref()</code></a>"&gt;<a href="#getHref()"><code>getText</code></a>t&lt;/a&gt;.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="formatHRef(java.lang.String)">
<h3>formatHRef</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">formatHRef</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</span></div>
</section>
</li>
<li>
<section class="detail" id="runIfIdle()">
<h3>runIfIdle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">runIfIdle</span>()</div>
<div class="block">Run given runnable if application is in idle mode. Otherwise show busy warning</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if runnable was executed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runIfIdle(java.lang.Runnable)">
<h3>runIfIdle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">runIfIdle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> preRun)</span></div>
<div class="block">Runs given runnable after preRun runnable was executed if application is in idle mode. Otherwise show busy warning</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>preRun</code> - executes before given runnable</dd>
<dt>Returns:</dt>
<dd>true if runnable was executed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIdleRequired(boolean)">
<h3>setIdleRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIdleRequired</span><wbr/><span class="parameters">(boolean idleRequired)</span></div>
<div class="block">Set flag to indicate that idle mode is required to execute this runnable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>idleRequired</code> - set true if this runnable can be executed only while application is in idle mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIdleRequired()">
<h3>isIdleRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIdleRequired</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this runnable can be executed only while application is in idle mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
