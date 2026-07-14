# JAVA OPENAPI: TransactionManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/transaction/TransactionManager.html
- source_path: `com/nomagic/uml2/transaction/TransactionManager.html`
- source_sha256: `d1847ab63b86492e8ea0c6acc69e21e5661fa7902846ec48fd310e0fdd6fa02c`
- captured_utc: `2026-07-14T16:59:00.518544+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Interface TransactionManager

public interfaceTransactionManager
Transaction provides framework to keep consistent model after model modification.
 All model modifications during transaction is recorded and later these modifications are verified to check if they do not break model integrity.
 Model verification and fixing must be implemented outside, and hooks must be passed to transaction.
 Transaction can be read only - during such transaction no model modifications are allowed and any of model modification throws [`ReadOnlyModelException`](ReadOnlyModelException.html)
Transaction managers offers three ways to attach the listeners. 

 1. Synchronize model changes - see [`addTransactionCommitListenerForExecute(TransactionCommitListener)`](#addTransactionCommitListenerForExecute(com.nomagic.uml2.transaction.TransactionCommitListener))

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static class`
`[TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html)`
Transaction options.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addNotDeliveredEventsListener](#addNotDeliveredEventsListener(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
Adds transaction commit listener which will be invoked if event delivery is turned off.
`void`
`[addTransactionCommitListener](#addTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
Adds transaction commit listener which will be invoked on first command execution or on direct transaction execution
 (not called on command/session undo/redo).
`void`
`[addTransactionCommitListenerForExecute](#addTransactionCommitListenerForExecute(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
Adds transaction commit listener which will be invoked only on the first command/session execution
 (not called on command/session undo/redo nor direct transaction execution).
`void`
`[addTransactionCommitListenerIncludingUndoAndRedo](#addTransactionCommitListenerIncludingUndoAndRedo(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
Adds transaction commit listener which will be invoked on command/session execution/undo/redo or direct transaction execution.
`void`
`[commit](#commit())()`
Commits transaction.
`void`
`[commitExecute](#commitExecute())()`
Commits transaction during execute operation.
`void`
`[commitUndoOrRedo](#commitUndoOrRedo())()`
Commits transaction during undo or redo operation.
`void`
`[executeInTransaction](#executeInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)`
Runs given code in new transaction by calling [`commitExecute()`](#commitExecute())
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TransactionCommitListener](TransactionCommitListener.html)>`
`[getListeners](#getListeners())()`

`[ModelValidator](ModelValidator.html)`
`[getModelValidator](#getModelValidator())()`
Get validation hook which validates model integrity.
`boolean`
`[isStarted](#isStarted())()`

`void`
`[removeTransactionCommitListener](#removeTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
Removes listener from transaction commit listeners.
`void`
`[runInTransaction](#runInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)`
Runs given code in a transaction.
`void`
`[runTransaction](#runTransaction(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r)`
Runs given code in new transaction by calling [`commit()`](#commit())
`void`
`[runTransaction](#runTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)`
Runs given code in new transaction by calling [`commit()`](#commit())
`void`
`[setInvalidModelHandler](#setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler))([InvalidModelHandler](InvalidModelHandler.html) handler)`
Sets handler which fixes model with verification errors.
`void`
`[setModelValidator](#setModelValidator(com.nomagic.uml2.transaction.ModelValidator))([ModelValidator](ModelValidator.html) validator)`
Sets validation hook which validates model integrity.
`void`
`[start](#start())()`
Starts transaction.
`void`
`[start](#start(com.nomagic.uml2.transaction.TransactionManager.TransactionOptions))([TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)`
Starts with given options.

============ METHOD DETAIL ========== 
Method Details
runTransaction
void runTransaction([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)
 throws [RollbackException](RollbackException.html),
[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)
Runs given code in new transaction by calling [`commit()`](#commit())
Parameters:
`r` - code to run.
`options` - transaction options to run
Throws:
`[RollbackException](RollbackException.html)` - when model verification fails, and [`InvalidModelHandler`](InvalidModelHandler.html)
`[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)` - when transaction already running
runTransaction
void runTransaction([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r)
 throws [RollbackException](RollbackException.html),
[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)
Runs given code in new transaction by calling [`commit()`](#commit())
Parameters:
`r` - code to run
Throws:
`[RollbackException](RollbackException.html)` - when model verification fails, and [`InvalidModelHandler`](InvalidModelHandler.html)
`[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)` - If currently transaction is running
executeInTransaction
void executeInTransaction([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)
 throws [RollbackException](RollbackException.html)
Runs given code in new transaction by calling [`commitExecute()`](#commitExecute())
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.
 If transaction is already started then simply runs the code.
Parameters:
`r` - code to run.
`options` - transaction options to run
Throws:
`[RollbackException](RollbackException.html)` - when model verification fails, and [`InvalidModelHandler`](InvalidModelHandler.html)
runInTransaction
void runInTransaction([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r,
 [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)
 throws [RollbackException](RollbackException.html)
Runs given code in a transaction.
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.
 If transaction is already started then simply runs the code.
Parameters:
`r` - code to run.
`options` - transaction options to run
Throws:
`[RollbackException](RollbackException.html)` - when model verification fails, and [`InvalidModelHandler`](InvalidModelHandler.html)
start
void start()
 throws [TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)
Starts transaction. Any model modification after transaction is started is recorded.
Throws:
`[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)` - when there is running transaction
isStarted
boolean isStarted()
Returns:
true if transaction is started
commit
void commit()
 throws [RollbackException](RollbackException.html),
[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)
Commits transaction. During commit, model is verified and in case verification failed model is fixed.
 If the only one fix is to rollback model to previous state which was before transaction [`RollbackException`](RollbackException.html) is thrown
Throws:
`[RollbackException](RollbackException.html)` - when transaction validation fails, and there is no way to fix model except undoing last action
`[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)` - when transaction is not started
commitUndoOrRedo
void commitUndoOrRedo()
 throws [RollbackException](RollbackException.html),
[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)
Commits transaction during undo or redo operation.
Throws:
`[RollbackException](RollbackException.html)`
`[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)`
See Also:
[`commit()`](#commit())
commitExecute
void commitExecute()
 throws [RollbackException](RollbackException.html),
[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)
Commits transaction during execute operation.
Throws:
`[RollbackException](RollbackException.html)`
`[TransactionAlreadyCommitedException](TransactionAlreadyCommitedException.html)`
See Also:
[`commit()`](#commit())
start
void start([TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) options)
 throws [TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)
Starts with given options. If transaction is read only any model modification after
 transaction is started throws [`ReadOnlyModelException`](ReadOnlyModelException.html)
If transaction
 Read only transactions are deprecated - normally queries on model can be done without
 transaction, and all modifications must be done through transaction.
Parameters:
`options` - transaction options
Throws:
`[TransactionAlreadyStartedException](TransactionAlreadyStartedException.html)` - if transaction is already started
setInvalidModelHandler
void setInvalidModelHandler([InvalidModelHandler](InvalidModelHandler.html) handler)
Sets handler which fixes model with verification errors.
Parameters:
`handler` - handler which fixes model
setModelValidator
void setModelValidator([ModelValidator](ModelValidator.html) validator)
Sets validation hook which validates model integrity.
Parameters:
`validator` - which validates model integrity
getModelValidator
[ModelValidator](ModelValidator.html) getModelValidator()
Get validation hook which validates model integrity.
Returns:
validator which validates model integrity
addTransactionCommitListener
void addTransactionCommitListener([TransactionCommitListener](TransactionCommitListener.html) listener)
Adds transaction commit listener which will be invoked on first command execution or on direct transaction execution
 (not called on command/session undo/redo).
Parameters:
`listener` - listener to add
addTransactionCommitListenerIncludingUndoAndRedo
void addTransactionCommitListenerIncludingUndoAndRedo([TransactionCommitListener](TransactionCommitListener.html) listener)
Adds transaction commit listener which will be invoked on command/session execution/undo/redo or direct transaction execution.
Parameters:
`listener` - listener
addTransactionCommitListenerForExecute
void addTransactionCommitListenerForExecute([TransactionCommitListener](TransactionCommitListener.html) listener)
Adds transaction commit listener which will be invoked only on the first command/session execution
 (not called on command/session undo/redo nor direct transaction execution).
Parameters:
`listener` - listener
addNotDeliveredEventsListener
void addNotDeliveredEventsListener([TransactionCommitListener](TransactionCommitListener.html) listener)
Adds transaction commit listener which will be invoked if event delivery is turned off.
 Usual transaction listeners will be not notified about such events.
Parameters:
`listener` - which is notified for events happened only when event delivery was turned off. Notification is done on event delivery restore.
removeTransactionCommitListener
void removeTransactionCommitListener([TransactionCommitListener](TransactionCommitListener.html) listener)
Removes listener from transaction commit listeners.
Parameters:
`listener` - listener to remove
getListeners
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[TransactionCommitListener](TransactionCommitListener.html)> getListeners()
Returns:
all registered transaction commit listeners.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Interface TransactionManager">Interface TransactionManager</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TransactionManager</span></div>
<div class="block">Transaction provides framework to keep consistent model after model modification.
 All model modifications during transaction is recorded and later these modifications are verified to check if they do not break model integrity.
 <p>
 Model verification and fixing must be implemented outside, and hooks must be passed to transaction.
 <p>
 Transaction can be read only - during such transaction no model modifications are allowed and any of model modification throws <a href="ReadOnlyModelException.html" title="class in com.nomagic.uml2.transaction"><code>ReadOnlyModelException</code></a>
<p>
 Transaction managers offers three ways to attach the listeners.<br/>
 1. Synchronize model changes - see <a href="#addTransactionCommitListenerForExecute(com.nomagic.uml2.transaction.TransactionCommitListener)"><code>addTransactionCommitListenerForExecute(TransactionCommitListener)</code></a><br>
 2. "Pseudo" synchronize model changes - see <a href="#addTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener)"><code>addTransactionCommitListener(TransactionCommitListener)</code></a><br/>
 3. Regular transaction commit - see  <a href="#addTransactionCommitListenerIncludingUndoAndRedo(com.nomagic.uml2.transaction.TransactionCommitListener)"><code>addTransactionCommitListenerIncludingUndoAndRedo(TransactionCommitListener)</code></a>.</br></p></p></p></div>
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
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Transaction options.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addNotDeliveredEventsListener(com.nomagic.uml2.transaction.TransactionCommitListener)">addNotDeliveredEventsListener</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds transaction commit listener which will be invoked if event delivery is turned off.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener)">addTransactionCommitListener</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds transaction commit listener which will be invoked on first command execution or on direct transaction execution
 (not called on command/session undo/redo).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addTransactionCommitListenerForExecute(com.nomagic.uml2.transaction.TransactionCommitListener)">addTransactionCommitListenerForExecute</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds transaction commit listener which will be invoked only on the first command/session execution
 (not called on command/session undo/redo nor direct transaction execution).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addTransactionCommitListenerIncludingUndoAndRedo(com.nomagic.uml2.transaction.TransactionCommitListener)">addTransactionCommitListenerIncludingUndoAndRedo</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds transaction commit listener which will be invoked on command/session execution/undo/redo or direct transaction execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#commit()">commit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Commits transaction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#commitExecute()">commitExecute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Commits transaction during execute operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#commitUndoOrRedo()">commitUndoOrRedo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Commits transaction during undo or redo operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#executeInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">executeInTransaction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Runs given code in new transaction by calling <a href="#commitExecute()"><code>commitExecute()</code></a>
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getListeners()">getListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModelValidator()">getModelValidator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get validation hook which validates model integrity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isStarted()">isStarted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener)">removeTransactionCommitListener</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes listener from transaction commit listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#runInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">runInTransaction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Runs given code in a transaction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#runTransaction(java.lang.Runnable)">runTransaction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Runs given code in new transaction by calling <a href="#commit()"><code>commit()</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#runTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">runTransaction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Runs given code in new transaction by calling <a href="#commit()"><code>commit()</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler)">setInvalidModelHandler</a><wbr/>(<a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction">InvalidModelHandler</a> handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets handler which fixes model with verification errors.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setModelValidator(com.nomagic.uml2.transaction.ModelValidator)">setModelValidator</a><wbr/>(<a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a> validator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets validation hook which validates model integrity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#start()">start</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Starts transaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#start(com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">start</a><wbr/>(<a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Starts with given options.</div>
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
<section class="detail" id="runTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">
<h3>runTransaction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">runTransaction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</span>
             throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a>,
<a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></span></div>
<div class="block">Runs given code in new transaction by calling <a href="#commit()"><code>commit()</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - code to run.</dd>
<dd><code>options</code> - transaction options to run</dd>
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code> - when model verification fails, and <a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction"><code>InvalidModelHandler</code></a></dd>
<dd><code><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></code> - when transaction already running</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runTransaction(java.lang.Runnable)">
<h3>runTransaction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">runTransaction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span>
             throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a>,
<a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></span></div>
<div class="block">Runs given code in new transaction by calling <a href="#commit()"><code>commit()</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - code to run</dd>
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code> - when model verification fails, and <a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction"><code>InvalidModelHandler</code></a></dd>
<dd><code><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></code> - If currently transaction is running</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">
<h3>executeInTransaction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">executeInTransaction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</span>
                   throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></span></div>
<div class="block">Runs given code in new transaction by calling <a href="#commitExecute()"><code>commitExecute()</code></a>
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.
 If transaction is already started then simply runs the code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - code to run.</dd>
<dd><code>options</code> - transaction options to run</dd>
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code> - when model verification fails, and <a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction"><code>InvalidModelHandler</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runInTransaction(java.lang.Runnable,com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">
<h3>runInTransaction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">runInTransaction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r,
 <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</span>
               throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></span></div>
<div class="block">Runs given code in a transaction.
 If transaction is not yet started, then starts a new, runs the code, and commits the transaction.
 If transaction is already started then simply runs the code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - code to run.</dd>
<dd><code>options</code> - transaction options to run</dd>
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code> - when model verification fails, and <a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction"><code>InvalidModelHandler</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start()">
<h3>start</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">start</span>()
    throws <span class="exceptions"><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></span></div>
<div class="block">Starts transaction. Any model modification after transaction is started is recorded.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></code> - when there is running transaction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStarted()">
<h3>isStarted</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isStarted</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transaction is started</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="commit()">
<h3>commit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">commit</span>()
     throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a>,
<a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></span></div>
<div class="block">Commits transaction. During commit, model is verified and in case verification failed model is fixed.
 If the only one fix is to rollback model to previous state which was before transaction <a href="RollbackException.html" title="class in com.nomagic.uml2.transaction"><code>RollbackException</code></a> is thrown</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code> - when transaction validation fails, and there is no way to fix model except undoing last action</dd>
<dd><code><a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></code> - when transaction is not started</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="commitUndoOrRedo()">
<h3>commitUndoOrRedo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">commitUndoOrRedo</span>()
               throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a>,
<a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></span></div>
<div class="block">Commits transaction during undo or redo operation.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code></dd>
<dd><code><a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#commit()"><code>commit()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="commitExecute()">
<h3>commitExecute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">commitExecute</span>()
            throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a>,
<a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></span></div>
<div class="block">Commits transaction during execute operation.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code></dd>
<dd><code><a href="TransactionAlreadyCommitedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyCommitedException</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#commit()"><code>commit()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(com.nomagic.uml2.transaction.TransactionManager.TransactionOptions)">
<h3>start</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(<a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a> options)</span>
    throws <span class="exceptions"><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></span></div>
<div class="block">Starts with given options. If transaction is read only any model modification after
 transaction is started throws <a href="ReadOnlyModelException.html" title="class in com.nomagic.uml2.transaction"><code>ReadOnlyModelException</code></a>
<p>
 If transaction
 <p>
 Read only transactions are deprecated - normally queries on model can be done without
 transaction, and all modifications must be done through transaction.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - transaction options</dd>
<dt>Throws:</dt>
<dd><code><a href="TransactionAlreadyStartedException.html" title="class in com.nomagic.uml2.transaction">TransactionAlreadyStartedException</a></code> - if transaction is already started</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler)">
<h3>setInvalidModelHandler</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInvalidModelHandler</span><wbr/><span class="parameters">(<a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction">InvalidModelHandler</a> handler)</span></div>
<div class="block">Sets handler which fixes model with verification errors.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>handler</code> - handler which fixes model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModelValidator(com.nomagic.uml2.transaction.ModelValidator)">
<h3>setModelValidator</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setModelValidator</span><wbr/><span class="parameters">(<a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a> validator)</span></div>
<div class="block">Sets validation hook which validates model integrity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>validator</code> - which validates model integrity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelValidator()">
<h3>getModelValidator</h3>
<div class="member-signature"><span class="return-type"><a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a></span> <span class="element-name">getModelValidator</span>()</div>
<div class="block">Get validation hook which validates model integrity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>validator which validates model integrity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>addTransactionCommitListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addTransactionCommitListener</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
<div class="block">Adds transaction commit listener which will be invoked on first command execution or on direct transaction execution
 (not called on command/session undo/redo).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTransactionCommitListenerIncludingUndoAndRedo(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>addTransactionCommitListenerIncludingUndoAndRedo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addTransactionCommitListenerIncludingUndoAndRedo</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
<div class="block">Adds transaction commit listener which will be invoked on command/session execution/undo/redo or direct transaction execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTransactionCommitListenerForExecute(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>addTransactionCommitListenerForExecute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addTransactionCommitListenerForExecute</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
<div class="block">Adds transaction commit listener which will be invoked only on the first command/session execution
 (not called on command/session undo/redo nor direct transaction execution).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNotDeliveredEventsListener(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>addNotDeliveredEventsListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addNotDeliveredEventsListener</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
<div class="block">Adds transaction commit listener which will be invoked if event delivery is turned off.
 Usual transaction listeners will be not notified about such events.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - which is notified for events happened only when event delivery was turned off. Notification is done on event delivery restore.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTransactionCommitListener(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>removeTransactionCommitListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeTransactionCommitListener</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
<div class="block">Removes listener from transaction commit listeners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getListeners()">
<h3>getListeners</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a>&gt;</span> <span class="element-name">getListeners</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all registered transaction commit listeners.</dd>
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
