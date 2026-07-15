# JAVA OPENAPI: DropTarget (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/dnd/DropTarget.html
- source_path: `com/nomagic/magicdraw/ui/dnd/DropTarget.html`
- source_sha256: `73b19d1064dc4f9af9ec89409e89f1504fd9a9c8264d86e7992516da4c363096`
- captured_utc: `2026-07-14T16:52:03.751769+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class DropTarget

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.DropTarget

@OpenApiAllpublic classDropTarget
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class is used as a wrapper for drag and drop handler data

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DropTarget](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) target)`

`[DropTarget](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean))([PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid)`

`[DropTarget](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String))([PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`

`[DropTarget](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String,java.awt.Cursor))([PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)`

`[DropTarget](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([PresentationElement](../../uml/symbols/PresentationElement.html) target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getCursor](#getCursor())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`

`[PresentationElement](../../uml/symbols/PresentationElement.html)`
`[getTarget](#getTarget())()`

`boolean`
`[isValid](#isValid())()`

`void`
`[setCursor](#setCursor(java.awt.Cursor))([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)`
Set cursor for the drop
`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Set description of dropped target
`void`
`[setTarget](#setTarget(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../uml/symbols/PresentationElement.html) target)`
Set presentation element for the drop target
`void`
`[setValid](#setValid(boolean))(boolean valid)`
Set valid to true if drop is correct
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DropTarget
public DropTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 @CheckForNull
 [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)
Parameters:
`target` - presentation element which the drag is dropped on
`valid` - check whether the drop target is valid
`description` - to be shown on the drop
`cursor` - to be shown on the drop
DropTarget
public DropTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Parameters:
`target` - presentation element which the drag is dropped on
`valid` - check whether the drop target is valid
`description` - to be shown on the drop
DropTarget
public DropTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target,
 boolean valid)
Parameters:
`target` - presentation element which the drag is dropped on
`valid` - check whether the drop target is valid
DropTarget
public DropTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)
Parameters:
`target` - presentation element which the drag is dropped on
DropTarget
public DropTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Parameters:
`target` - presentation element which the drag is dropped on
`description` - to be shown on the drop
 ============ METHOD DETAIL ========== 
Method Details
getTarget
@CheckForNullpublic [PresentationElement](../../uml/symbols/PresentationElement.html) getTarget()
Returns:
target presentation element which the drag is dropped on
isValid
public boolean isValid()
Returns:
whether dropped target is valid or not
getDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Returns:
description of the dropped target
getCursor
@CheckForNullpublic [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getCursor()
Returns:
cursor that is shown on drop
setTarget
public void setTarget(@CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) target)
Set presentation element for the drop target
Parameters:
`target` - presentation element
setValid
public void setValid(boolean valid)
Set valid to true if drop is correct
Parameters:
`valid` - true if valid drop, otherwise false
setDescription
public void setDescription(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Set description of dropped target
Parameters:
`description` - string representation for dropped target
setCursor
public void setCursor(@CheckForNull
 [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)
Set cursor for the drop
Parameters:
`cursor` - of the drop

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class DropTarget">Class DropTarget</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.DropTarget</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DropTarget</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class is used as a wrapper for drag and drop handler data</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">DropTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">DropTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String)">DropTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String,java.awt.Cursor)">DropTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">DropTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCursor()">getCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValid()">isValid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCursor(java.awt.Cursor)">setCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set cursor for the drop</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set description of dropped target</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTarget(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setTarget</a><wbr/>(<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set presentation element for the drop target</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValid(boolean)">setValid</a><wbr/>(boolean valid)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set valid to true if drop is correct</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String,java.awt.Cursor)">
<h3>DropTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DropTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element which the drag is dropped on</dd>
<dd><code>valid</code> - check whether the drop target is valid</dd>
<dd><code>description</code> - to be shown on the drop</dd>
<dd><code>cursor</code> - to be shown on the drop</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,java.lang.String)">
<h3>DropTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DropTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element which the drag is dropped on</dd>
<dd><code>valid</code> - check whether the drop target is valid</dd>
<dd><code>description</code> - to be shown on the drop</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">
<h3>DropTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DropTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 boolean valid)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element which the drag is dropped on</dd>
<dd><code>valid</code> - check whether the drop target is valid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>DropTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DropTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element which the drag is dropped on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>DropTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DropTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element which the drag is dropped on</dd>
<dd><code>description</code> - to be shown on the drop</dd>
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
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getTarget</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target presentation element which the drag is dropped on</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValid()">
<h3>isValid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValid</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>whether dropped target is valid or not</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description of the dropped target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCursor()">
<h3>getCursor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getCursor</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>cursor that is shown on drop</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target)</span></div>
<div class="block">Set presentation element for the drop target</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - presentation element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValid(boolean)">
<h3>setValid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValid</span><wbr/><span class="parameters">(boolean valid)</span></div>
<div class="block">Set valid to true if drop is correct</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valid</code> - true if valid drop, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Set description of dropped target</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - string representation for dropped target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCursor(java.awt.Cursor)">
<h3>setCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCursor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</span></div>
<div class="block">Set cursor for the drop</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cursor</code> - of the drop</dd>
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
