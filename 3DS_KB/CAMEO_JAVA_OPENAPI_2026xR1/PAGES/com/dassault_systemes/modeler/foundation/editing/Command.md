# JAVA OPENAPI: Command (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/editing/Command.html
- source_path: `com/dassault_systemes/modeler/foundation/editing/Command.html`
- source_sha256: `41edd01832615caa2d0bb66edbb7312faf6b17c428aa2f20468427efa45715bd`
- captured_utc: `2026-07-14T16:44:44.598797+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.editing](package-summary.html)

## Interface Command

All Known Subinterfaces:
`[CompositeCommand](CompositeCommand.html)`

@OpenApiAllpublic interfaceCommand

Represents an executable operation with undo/redo support.

 A command encapsulates a model modification that can be executed,
 undone, or canceled. Canceled commands cannot be undone.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[cancel](#cancel())()`
Cancels the command.
`default int`
`[count](#count())()`

`void`
`[execute](#execute())()`
Executes the command.
`default [BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html)`
`[getElementOfThisCommand](#getElementOfThisCommand())()`
Returns the element affected by this command, if any.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns the user-visible name of the command.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNameOfEditCommand](#getNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Retrieves the name of the editing command associated with the given element.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Sets the user-visible name of the command.
`static void`
`[setNameOfEditCommand](#setNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.foundation.editing.Command))([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element,
 [Command](Command.html) cmd)`
Associates a name with the given editing command for the specified element.
`void`
`[setWasExecuted](#setWasExecuted(boolean))(boolean wasExecuted)`
Sets the execution state of the command.
`void`
`[undo](#undo())()`
Reverts the effects of a previously executed command.
`boolean`
`[wasExecuted](#wasExecuted())()`
Indicates whether the command has been executed.

============ METHOD DETAIL ========== 
Method Details
execute
void execute()
Executes the command.
undo
void undo()
Reverts the effects of a previously executed command.
cancel
void cancel()
Cancels the command.
setName
void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Sets the user-visible name of the command.
Parameters:
`name` - command name
getName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Returns the user-visible name of the command.
Returns:
command name
wasExecuted
boolean wasExecuted()
Indicates whether the command has been executed.
Returns:
`true` if executed, otherwise `false`
setWasExecuted
void setWasExecuted(boolean wasExecuted)
Sets the execution state of the command.
Parameters:
`wasExecuted` - execution flag
getElementOfThisCommand
@CheckForNulldefault [BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) getElementOfThisCommand()
Returns the element affected by this command, if any.
Returns:
associated element, or `null` if not applicable
count
default int count()
setNameOfEditCommand
static void setNameOfEditCommand([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element,
 [Command](Command.html) cmd)
Associates a name with the given editing command for the specified element.
Parameters:
`element` - the related element
`cmd` - the editing command
getNameOfEditCommand
static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNameOfEditCommand([BaseElement](../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Retrieves the name of the editing command associated with the given element.
Parameters:
`element` - the related element
Returns:
command name, or `null` if not set

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.editing</a></div>
<h1 class="title" title="Interface Command">Interface Command</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Command</span></div>
<div class="block">Represents an executable operation with undo/redo support.

 <p>
 A command encapsulates a model modification that can be executed,
 undone, or canceled. Canceled commands cannot be undone.
 </p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#cancel()">cancel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Cancels the command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#count()">count</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute()">execute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes the command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getElementOfThisCommand()">getElementOfThisCommand</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns the element affected by this command, if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the user-visible name of the command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement)">getNameOfEditCommand</a><wbr/>(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Retrieves the name of the editing command associated with the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the user-visible name of the command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#setNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.foundation.editing.Command)">setNameOfEditCommand</a><wbr/>(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> cmd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Associates a name with the given editing command for the specified element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setWasExecuted(boolean)">setWasExecuted</a><wbr/>(boolean wasExecuted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the execution state of the command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#undo()">undo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reverts the effects of a previously executed command.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#wasExecuted()">wasExecuted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates whether the command has been executed.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="execute()">
<h3>execute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">execute</span>()</div>
<div class="block">Executes the command.</div>
</section>
</li>
<li>
<section class="detail" id="undo()">
<h3>undo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">undo</span>()</div>
<div class="block">Reverts the effects of a previously executed command.</div>
</section>
</li>
<li>
<section class="detail" id="cancel()">
<h3>cancel</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">cancel</span>()</div>
<div class="block">Cancels the command.</div>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets the user-visible name of the command.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - command name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns the user-visible name of the command.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>command name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wasExecuted()">
<h3>wasExecuted</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">wasExecuted</span>()</div>
<div class="block">Indicates whether the command has been executed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if executed, otherwise <code>false</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWasExecuted(boolean)">
<h3>setWasExecuted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setWasExecuted</span><wbr/><span class="parameters">(boolean wasExecuted)</span></div>
<div class="block">Sets the execution state of the command.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>wasExecuted</code> - execution flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementOfThisCommand()">
<h3>getElementOfThisCommand</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElementOfThisCommand</span>()</div>
<div class="block">Returns the element affected by this command, if any.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>associated element, or <code>null</code> if not applicable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="count()">
<h3>count</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">count</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement,com.dassault_systemes.modeler.foundation.editing.Command)">
<h3>setNameOfEditCommand</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">setNameOfEditCommand</span><wbr/><span class="parameters">(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> cmd)</span></div>
<div class="block">Associates a name with the given editing command for the specified element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the related element</dd>
<dd><code>cmd</code> - the editing command</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameOfEditCommand(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getNameOfEditCommand</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameOfEditCommand</span><wbr/><span class="parameters">(<a href="../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Retrieves the name of the editing command associated with the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the related element</dd>
<dt>Returns:</dt>
<dd>command name, or <code>null</code> if not set</dd>
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
