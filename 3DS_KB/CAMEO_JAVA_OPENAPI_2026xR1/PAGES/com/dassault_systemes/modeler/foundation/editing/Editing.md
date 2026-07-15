# JAVA OPENAPI: Editing (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/editing/Editing.html
- source_path: `com/dassault_systemes/modeler/foundation/editing/Editing.html`
- source_sha256: `83b9628db9a30a2d075e8541ae4049db8ff65a49386907f92808d50c62028052`
- captured_utc: `2026-07-14T16:44:44.781799+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.editing](package-summary.html)

## Interface Editing

@OpenApiAllpublic interfaceEditing
Provides an API for executing and managing model editing operations with
 transaction and undo/redo support.

 This framework:
 Executes model modifications within `Transactions`
Records changes as [`commands`](Command.html) for undo/redo
Maintains command history and supports redo after undo

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`static void`
`[appendIfPossible](#appendIfPossible(com.dassault_systemes.modeler.foundation.project.ModelElementProject,com.dassault_systemes.modeler.foundation.editing.Command))([ModelElementProject](../project/ModelElementProject.html) project,
 [Command](Command.html) command)`
Append a given command to command for appending
`<V> V`
`[call](#call(java.lang.String,java.util.concurrent.Callable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)`
Executes given [`Callable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html) inside already started or starts a new editing command.
`void`
`[clearHistory](#clearHistory())()`
Discards all commands in the history.
`void`
`[compactHistoryUntil](#compactHistoryUntil(com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([CompositeCommand](CompositeCommand.html) command)`
Merges all commands till the end from the specified command.
`void`
`[discardCurrent](#discardCurrent())()`
Discards the current command and remove it from the history.
`default void`
`[execute](#execute(java.lang.String,java.lang.Runnable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)`
Executes given [`Runnable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) inside already started or starts a new editing command.
`[CompositeCommand](CompositeCommand.html)`
`[getCommandForAppending](#getCommandForAppending())()`
Returns the current command from the command history for others commands appending.
`[CompositeCommand](CompositeCommand.html)`
`[getCommandForRedo](#getCommandForRedo())()`

`[CompositeCommand](CompositeCommand.html)`
`[getCommandForUndo](#getCommandForUndo())()`

`[CompositeCommand](CompositeCommand.html)`
`[getCurrentCommand](#getCurrentCommand())()`

`static [Editing](Editing.html)`
`[getInstance](#getInstance(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../project/ModelElementProject.html) project)`
Returns the [`Editing`](Editing.html) instance for the given project.
`default boolean`
`[isBusy](#isBusy())()`
If history is doing something - complete, undo, redo or cancel.
`boolean`
`[isCanceling](#isCanceling())()`

`boolean`
`[isCompleting](#isCompleting())()`

`boolean`
`[isRedoing](#isRedoing())()`
If history doing redo.
`boolean`
`[isUndoing](#isUndoing())()`

`default boolean`
`[isUndoingOrRedoing](#isUndoingOrRedoing())()`
If command history undoing or redoing at the moment.
`void`
`[redo](#redo())()`
Redo command next to current.
`default <V> V`
`[supply](#supply(java.lang.String,java.util.function.Supplier))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<V> supplier)`
Executes given [`Supplier`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html) inside already started or starts a new editing command.
`void`
`[undo](#undo())()`
Undo the current command.

============ METHOD DETAIL ========== 
Method Details
getInstance
static [Editing](Editing.html) getInstance([ModelElementProject](../project/ModelElementProject.html) project)
Returns the [`Editing`](Editing.html) instance for the given project.
Parameters:
`project` - the project
Returns:
editing instance
execute
default void execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)
Executes given [`Runnable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) inside already started or starts a new editing command.
 Wraps it in a [`CompositeCommand`](CompositeCommand.html). Records all changes in the model during execution for undo.
 Discards newly started command if [`Runnable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) throws `EditingCanceledException`
Parameters:
`commandName` - command name
`runnable` - runnable
supply
default <V> V supply([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<V> supplier)
Executes given [`Supplier`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html) inside already started or starts a new editing command.
 Wraps it in a [`CompositeCommand`](CompositeCommand.html). Records all changes in the model during execution for undo.
 Discards newly started command if [`Supplier`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html) throws `EditingCanceledException`.
Parameters:
`commandName` - command name
`supplier` - supplier
Returns:
value from supplier or null if [`Supplier`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html) threw `EditingCanceledException`
call
<V> V call([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commandName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Executes given [`Callable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html) inside already started or starts a new editing command.
 Wraps it in a [`CompositeCommand`](CompositeCommand.html). Records all changes in the model during execution for undo.
 Discards newly started command if [`Callable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html) throws `EditingCanceledException`.
Parameters:
`commandName` - command name
`callable` - supplier
Returns:
value from callable or null if [`Callable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html) threw `EditingCanceledException`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
redo
void redo()
Redo command next to current. The current command needs to be complete.
undo
void undo()
Undo the current command. It needs to be completed.
discardCurrent
void discardCurrent()
Discards the current command and remove it from the history. Command needs to be executed.
compactHistoryUntil
void compactHistoryUntil([CompositeCommand](CompositeCommand.html) command)
Merges all commands till the end from the specified command.
 All commands must be executed. If non-executed commands are found, merge is not performed.
Parameters:
`command` - the command to merge up to (including it)
clearHistory
void clearHistory()
Discards all commands in the history. History will be empty.
isCompleting
boolean isCompleting()
Returns:
true if history is executing some command at this moment
isUndoing
boolean isUndoing()
Returns:
true if history is undoing some command at this moment
isCanceling
boolean isCanceling()
Returns:
true if history is canceling some command at this moment
isRedoing
boolean isRedoing()
If history doing redo.
Returns:
true if now doing redo.
isUndoingOrRedoing
default boolean isUndoingOrRedoing()
If command history undoing or redoing at the moment.
Returns:
true if undo or redo operations are in progress.
isBusy
default boolean isBusy()
If history is doing something - complete, undo, redo or cancel.
Returns:
true if now doing redo.
getCommandForAppending
[CompositeCommand](CompositeCommand.html) getCommandForAppending()
Returns the current command from the command history for others commands appending.
 Such a command is available only if the current command in the project's command history is not executed yet.
Returns:
the command for other commands appending
getCurrentCommand
@CheckForNull[CompositeCommand](CompositeCommand.html) getCurrentCommand()
Returns:
current history command. It can be executed or not.
getCommandForUndo
@CheckForNull[CompositeCommand](CompositeCommand.html) getCommandForUndo()
Returns:
the command that can be undone
getCommandForRedo
@CheckForNull[CompositeCommand](CompositeCommand.html) getCommandForRedo()
Returns:
the command for redo (next to the current command)
appendIfPossible
static void appendIfPossible([ModelElementProject](../project/ModelElementProject.html) project,
 [Command](Command.html) command)
Append a given command to command for appending
Parameters:
`project` - project
`command` - command
See Also:
[`getCommandForAppending()`](#getCommandForAppending())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.editing</a></div>
<h1 class="title" title="Interface Editing">Interface Editing</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Editing</span></div>
<div class="block">Provides an API for executing and managing model editing operations with
 transaction and undo/redo support.

 <p>
 This framework:
 <ul>
<li>Executes model modifications within <code>Transactions</code></li>
<li>Records changes as <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>commands</code></a> for undo/redo</li>
<li>Maintains command history and supports redo after undo</li>
</ul>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#appendIfPossible(com.dassault_systemes.modeler.foundation.project.ModelElementProject,com.dassault_systemes.modeler.foundation.editing.Command)">appendIfPossible</a><wbr/>(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Append a given command to command for appending</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>&lt;V&gt; V</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#call(java.lang.String,java.util.concurrent.Callable)">call</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent"><code>Callable</code></a> inside already started or starts a new editing command.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#clearHistory()">clearHistory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Discards all commands in the history.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#compactHistoryUntil(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">compactHistoryUntil</a><wbr/>(<a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a> command)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Merges all commands till the end from the specified command.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#discardCurrent()">discardCurrent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Discards the current command and remove it from the history.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.Runnable)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> inside already started or starts a new editing command.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommandForAppending()">getCommandForAppending</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current command from the command history for others commands appending.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommandForRedo()">getCommandForRedo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommandForUndo()">getCommandForUndo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCurrentCommand()">getCurrentCommand</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Editing</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getInstance(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstance</a><wbr/>(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Returns the <a href="Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> instance for the given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isBusy()">isBusy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">If history is doing something - complete, undo, redo or cancel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCanceling()">isCanceling</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCompleting()">isCompleting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isRedoing()">isRedoing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If history doing redo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUndoing()">isUndoing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isUndoingOrRedoing()">isUndoingOrRedoing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">If command history undoing or redoing at the moment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#redo()">redo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Redo command next to current.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default &lt;V&gt; V</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#supply(java.lang.String,java.util.function.Supplier)">supply</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;V&gt; supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function"><code>Supplier</code></a> inside already started or starts a new editing command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#undo()">undo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Undo the current command.</div>
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
<section class="detail" id="getInstance(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Editing</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the <a href="Editing.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Editing</code></a> instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>editing instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.lang.Runnable)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> inside already started or starts a new editing command.
 Wraps it in a <a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>CompositeCommand</code></a>. Records all changes in the model during execution for undo.
 Discards newly started command if <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> throws <code>EditingCanceledException</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>commandName</code> - command name</dd>
<dd><code>runnable</code> - runnable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supply(java.lang.String,java.util.function.Supplier)">
<h3>supply</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">supply</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;V&gt; supplier)</span></div>
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function"><code>Supplier</code></a> inside already started or starts a new editing command.
 Wraps it in a <a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>CompositeCommand</code></a>. Records all changes in the model during execution for undo.
 Discards newly started command if <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function"><code>Supplier</code></a> throws <code>EditingCanceledException</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>commandName</code> - command name</dd>
<dd><code>supplier</code> - supplier</dd>
<dt>Returns:</dt>
<dd>value from supplier or null if <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function"><code>Supplier</code></a> threw <code>EditingCanceledException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="call(java.lang.String,java.util.concurrent.Callable)">
<h3>call</h3>
<div class="member-signature"><span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">call</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commandName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Executes given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent"><code>Callable</code></a> inside already started or starts a new editing command.
 Wraps it in a <a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>CompositeCommand</code></a>. Records all changes in the model during execution for undo.
 Discards newly started command if <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent"><code>Callable</code></a> throws <code>EditingCanceledException</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>commandName</code> - command name</dd>
<dd><code>callable</code> - supplier</dd>
<dt>Returns:</dt>
<dd>value from callable or null if <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent"><code>Callable</code></a> threw <code>EditingCanceledException</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="redo()">
<h3>redo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">redo</span>()</div>
<div class="block">Redo command next to current. The current command needs to be complete.</div>
</section>
</li>
<li>
<section class="detail" id="undo()">
<h3>undo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">undo</span>()</div>
<div class="block">Undo the current command. It needs to be completed.</div>
</section>
</li>
<li>
<section class="detail" id="discardCurrent()">
<h3>discardCurrent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">discardCurrent</span>()</div>
<div class="block">Discards the current command and remove it from the history. Command needs to be executed.</div>
</section>
</li>
<li>
<section class="detail" id="compactHistoryUntil(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>compactHistoryUntil</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">compactHistoryUntil</span><wbr/><span class="parameters">(<a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a> command)</span></div>
<div class="block">Merges all commands till the end from the specified command.
 All commands must be executed. If non-executed commands are found, merge is not performed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>command</code> - the command to merge up to (including it)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearHistory()">
<h3>clearHistory</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">clearHistory</span>()</div>
<div class="block">Discards all commands in the history. History will be empty.</div>
</section>
</li>
<li>
<section class="detail" id="isCompleting()">
<h3>isCompleting</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCompleting</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if history is executing some command at this moment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUndoing()">
<h3>isUndoing</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isUndoing</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if history is undoing some command at this moment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCanceling()">
<h3>isCanceling</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCanceling</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if history is canceling some command at this moment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRedoing()">
<h3>isRedoing</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isRedoing</span>()</div>
<div class="block">If history doing redo.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if now doing redo.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUndoingOrRedoing()">
<h3>isUndoingOrRedoing</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isUndoingOrRedoing</span>()</div>
<div class="block">If command history undoing or redoing at the moment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if undo or redo operations are in progress.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBusy()">
<h3>isBusy</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isBusy</span>()</div>
<div class="block">If history is doing something - complete, undo, redo or cancel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if now doing redo.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommandForAppending()">
<h3>getCommandForAppending</h3>
<div class="member-signature"><span class="return-type"><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></span> <span class="element-name">getCommandForAppending</span>()</div>
<div class="block">Returns the current command from the command history for others commands appending.
 Such a command is available only if the current command in the project's command history is not executed yet.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the command for other commands appending</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentCommand()">
<h3>getCurrentCommand</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></span> <span class="element-name">getCurrentCommand</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current history command. It can be executed or not.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommandForUndo()">
<h3>getCommandForUndo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></span> <span class="element-name">getCommandForUndo</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the command that can be undone</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommandForRedo()">
<h3>getCommandForRedo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CompositeCommand.html" title="interface in com.dassault_systemes.modeler.foundation.editing">CompositeCommand</a></span> <span class="element-name">getCommandForRedo</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the command for redo (next to the current command)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendIfPossible(com.dassault_systemes.modeler.foundation.project.ModelElementProject,com.dassault_systemes.modeler.foundation.editing.Command)">
<h3>appendIfPossible</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">appendIfPossible</span><wbr/><span class="parameters">(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</span></div>
<div class="block">Append a given command to command for appending</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>command</code> - command</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getCommandForAppending()"><code>getCommandForAppending()</code></a></li>
</ul>
</dd>
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
