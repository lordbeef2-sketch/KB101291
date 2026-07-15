# JAVA OPENAPI: CompositeCommand (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/editing/CompositeCommand.html
- source_path: `com/dassault_systemes/modeler/foundation/editing/CompositeCommand.html`
- source_sha256: `ff535e886b443ddb245d63b700362cca58105cf61fc65ae8ec636baec5685e02`
- captured_utc: `2026-07-14T16:44:44.635797+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.editing](package-summary.html)

## Interface CompositeCommand

All Superinterfaces:
`[Command](Command.html)`

@OpenApiAllpublic interfaceCompositeCommandextends [Command](Command.html)

A [`Command`](Command.html) that aggregates multiple commands and executes them as a single unit.

 A composite command allows grouping of multiple operations so they can be
 executed, undone, or canceled together.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[add](#add(com.dassault_systemes.modeler.foundation.editing.Command))([Command](Command.html) command)`
Adds a command to the end of this composite.
`void`
`[add](#add(com.dassault_systemes.modeler.foundation.editing.Command,int))([Command](Command.html) command,
 int index)`
Adds a command at the specified position.
`void`
`[forEach](#forEach(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Command](Command.html)> consumer)`
Applies the given action to each contained command.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Command](Command.html)>`
`[getCommands](#getCommands())()`
Returns the list of contained commands.
`void`
`[insert](#insert(com.dassault_systemes.modeler.foundation.editing.Command))([Command](Command.html) command)`
Inserts a command according to implementation-defined ordering.
`boolean`
`[isEmpty](#isEmpty())()`
Returns whether this composite contains no commands.
`void`
`[remove](#remove(com.dassault_systemes.modeler.foundation.editing.Command))([Command](Command.html) command)`
Removes a command from this composite.
Methods inherited from interface com.dassault_systemes.modeler.foundation.editing.[Command](Command.html)
`[cancel](Command.html#cancel()), [count](Command.html#count()), [execute](Command.html#execute()), [getElementOfThisCommand](Command.html#getElementOfThisCommand()), [getName](Command.html#getName()), [setName](Command.html#setName(java.lang.String)), [setWasExecuted](Command.html#setWasExecuted(boolean)), [undo](Command.html#undo()), [wasExecuted](Command.html#wasExecuted())`

============ METHOD DETAIL ========== 
Method Details
add
void add([Command](Command.html) command)
Adds a command to the end of this composite.
Parameters:
`command` - command to add
add
void add([Command](Command.html) command,
 int index)
Adds a command at the specified position.
Parameters:
`command` - command to add
`index` - position to insert at
remove
void remove([Command](Command.html) command)
Removes a command from this composite.
Parameters:
`command` - command to remove
forEach
void forEach([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Command](Command.html)> consumer)
Applies the given action to each contained command.
Parameters:
`consumer` - action to apply
isEmpty
boolean isEmpty()
Returns whether this composite contains no commands.
Returns:
`true` if empty, otherwise `false`
insert
void insert([Command](Command.html) command)
Inserts a command according to implementation-defined ordering.
Parameters:
`command` - command to insert
getCommands
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Command](Command.html)> getCommands()
Returns the list of contained commands.
Returns:
list of commands

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.editing</a></div>
<h1 class="title" title="Interface CompositeCommand">Interface CompositeCommand</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">CompositeCommand</span><span class="extends-implements">
extends <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a></span></div>
<div class="block">A <a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing"><code>Command</code></a> that aggregates multiple commands and executes them as a single unit.

 <p>
 A composite command allows grouping of multiple operations so they can be
 executed, undone, or canceled together.
 </p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#add(com.dassault_systemes.modeler.foundation.editing.Command)">add</a><wbr/>(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a command to the end of this composite.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#add(com.dassault_systemes.modeler.foundation.editing.Command,int)">add</a><wbr/>(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a command at the specified position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#forEach(java.util.function.Consumer)">forEach</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Applies the given action to each contained command.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommands()">getCommands</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the list of contained commands.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#insert(com.dassault_systemes.modeler.foundation.editing.Command)">insert</a><wbr/>(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Inserts a command according to implementation-defined ordering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns whether this composite contains no commands.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#remove(com.dassault_systemes.modeler.foundation.editing.Command)">remove</a><wbr/>(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a command from this composite.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.editing.Command">Methods inherited from interface com.dassault_systemes.modeler.foundation.editing.<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a></h3>
<code><a href="Command.html#cancel()">cancel</a>, <a href="Command.html#count()">count</a>, <a href="Command.html#execute()">execute</a>, <a href="Command.html#getElementOfThisCommand()">getElementOfThisCommand</a>, <a href="Command.html#getName()">getName</a>, <a href="Command.html#setName(java.lang.String)">setName</a>, <a href="Command.html#setWasExecuted(boolean)">setWasExecuted</a>, <a href="Command.html#undo()">undo</a>, <a href="Command.html#wasExecuted()">wasExecuted</a></code></div>
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
<section class="detail" id="add(com.dassault_systemes.modeler.foundation.editing.Command)">
<h3>add</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</span></div>
<div class="block">Adds a command to the end of this composite.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>command</code> - command to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.dassault_systemes.modeler.foundation.editing.Command,int)">
<h3>add</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command,
 int index)</span></div>
<div class="block">Adds a command at the specified position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>command</code> - command to add</dd>
<dd><code>index</code> - position to insert at</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.dassault_systemes.modeler.foundation.editing.Command)">
<h3>remove</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</span></div>
<div class="block">Removes a command from this composite.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>command</code> - command to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEach(java.util.function.Consumer)">
<h3>forEach</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a>&gt; consumer)</span></div>
<div class="block">Applies the given action to each contained command.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumer</code> - action to apply</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<div class="block">Returns whether this composite contains no commands.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if empty, otherwise <code>false</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insert(com.dassault_systemes.modeler.foundation.editing.Command)">
<h3>insert</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">insert</span><wbr/><span class="parameters">(<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a> command)</span></div>
<div class="block">Inserts a command according to implementation-defined ordering.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>command</code> - command to insert</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommands()">
<h3>getCommands</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Command.html" title="interface in com.dassault_systemes.modeler.foundation.editing">Command</a>&gt;</span> <span class="element-name">getCommands</span>()</div>
<div class="block">Returns the list of contained commands.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of commands</dd>
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
