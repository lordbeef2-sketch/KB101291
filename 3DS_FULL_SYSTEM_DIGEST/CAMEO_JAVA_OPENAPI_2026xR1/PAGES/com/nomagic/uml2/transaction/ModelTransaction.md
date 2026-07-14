# JAVA OPENAPI: ModelTransaction (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/transaction/ModelTransaction.html
- source_path: `com/nomagic/uml2/transaction/ModelTransaction.html`
- source_sha256: `c0083d257f8172064da9c6ae5b038846ce58e89f76863b57abe5fd02ae9b4346`
- captured_utc: `2026-07-14T16:46:34.671266+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Class ModelTransaction

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.transaction.ModelTransaction

public classModelTransaction
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
One Transaction, objects of this type can be reused.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[beforeChange](#beforeChange())()`

`void`
`[commit](#commit())()`

`boolean`
`[isFirePostCommit](#isFirePostCommit())()`
Determines whether post commit events are fired
`boolean`
`[isStarted](#isStarted())()`

`boolean`
`[isValidateModel](#isValidateModel())()`

`void`
`[modelChanged](#modelChanged(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Handles model change event.
`void`
`[setFirePostCommit](#setFirePostCommit(boolean))(boolean firePostCommit)`

`void`
`[setInvalidModelHandler](#setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler))([InvalidModelHandler](InvalidModelHandler.html) handler)`

`void`
`[setModelValidator](#setModelValidator(com.nomagic.uml2.transaction.ModelValidator))([ModelValidator](ModelValidator.html) handler)`

`void`
`[setModifiedElements](#setModifiedElements(com.nomagic.uml2.ext.jmi.ModifiedElements))(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)`

`void`
`[start](#start())()`
Starts transaction.
`void`
`[start](#start(boolean,boolean))(boolean readOnly,
 boolean validateModel)`

`void`
`[start](#start(boolean,boolean,boolean))(boolean readOnly,
 boolean validateModel,
 boolean validateRecursively)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
start
public void start()
Starts transaction. After transaction started events will be recorded and analyzed.
start
public void start(boolean readOnly,
 boolean validateModel)
start
public void start(boolean readOnly,
 boolean validateModel,
 boolean validateRecursively)
commit
public void commit()
 throws [RollbackException](RollbackException.html)
Throws:
`[RollbackException](RollbackException.html)`
modelChanged
public void modelChanged([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Handles model change event.
Parameters:
`evt` - event
isStarted
public boolean isStarted()
isFirePostCommit
public boolean isFirePostCommit()
Determines whether post commit events are fired
Returns:
`true` if events are fired, `false`
 otherwise
isValidateModel
public boolean isValidateModel()
setInvalidModelHandler
public void setInvalidModelHandler([InvalidModelHandler](InvalidModelHandler.html) handler)
setModelValidator
public void setModelValidator([ModelValidator](ModelValidator.html) handler)
beforeChange
public void beforeChange()
setFirePostCommit
public void setFirePostCommit(boolean firePostCommit)
setModifiedElements
public void setModifiedElements(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Class ModelTransaction">Class ModelTransaction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.transaction.ModelTransaction</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ModelTransaction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">One Transaction, objects of this type can be reused.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeChange()">beforeChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#commit()">commit</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFirePostCommit()">isFirePostCommit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether post commit events are fired</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isStarted()">isStarted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidateModel()">isValidateModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelChanged(java.beans.PropertyChangeEvent)">modelChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handles model change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirePostCommit(boolean)">setFirePostCommit</a><wbr/>(boolean firePostCommit)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler)">setInvalidModelHandler</a><wbr/>(<a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction">InvalidModelHandler</a> handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModelValidator(com.nomagic.uml2.transaction.ModelValidator)">setModelValidator</a><wbr/>(<a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModifiedElements(com.nomagic.uml2.ext.jmi.ModifiedElements)">setModifiedElements</a><wbr/>(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start()">start</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts transaction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(boolean,boolean)">start</a><wbr/>(boolean readOnly,
 boolean validateModel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(boolean,boolean,boolean)">start</a><wbr/>(boolean readOnly,
 boolean validateModel,
 boolean validateRecursively)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="start()">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span>()</div>
<div class="block">Starts transaction. After transaction started events will be recorded and analyzed.</div>
</section>
</li>
<li>
<section class="detail" id="start(boolean,boolean)">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(boolean readOnly,
 boolean validateModel)</span></div>
</section>
</li>
<li>
<section class="detail" id="start(boolean,boolean,boolean)">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(boolean readOnly,
 boolean validateModel,
 boolean validateRecursively)</span></div>
</section>
</li>
<li>
<section class="detail" id="commit()">
<h3>commit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">commit</span>()
            throws <span class="exceptions"><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="RollbackException.html" title="class in com.nomagic.uml2.transaction">RollbackException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="modelChanged(java.beans.PropertyChangeEvent)">
<h3>modelChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">modelChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block">Handles model change event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evt</code> - event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStarted()">
<h3>isStarted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isStarted</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isFirePostCommit()">
<h3>isFirePostCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFirePostCommit</span>()</div>
<div class="block">Determines whether post commit events are fired</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if events are fired, <code>false</code>
 otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValidateModel()">
<h3>isValidateModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValidateModel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setInvalidModelHandler(com.nomagic.uml2.transaction.InvalidModelHandler)">
<h3>setInvalidModelHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInvalidModelHandler</span><wbr/><span class="parameters">(<a href="InvalidModelHandler.html" title="interface in com.nomagic.uml2.transaction">InvalidModelHandler</a> handler)</span></div>
</section>
</li>
<li>
<section class="detail" id="setModelValidator(com.nomagic.uml2.transaction.ModelValidator)">
<h3>setModelValidator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModelValidator</span><wbr/><span class="parameters">(<a href="ModelValidator.html" title="interface in com.nomagic.uml2.transaction">ModelValidator</a> handler)</span></div>
</section>
</li>
<li>
<section class="detail" id="beforeChange()">
<h3>beforeChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeChange</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFirePostCommit(boolean)">
<h3>setFirePostCommit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFirePostCommit</span><wbr/><span class="parameters">(boolean firePostCommit)</span></div>
</section>
</li>
<li>
<section class="detail" id="setModifiedElements(com.nomagic.uml2.ext.jmi.ModifiedElements)">
<h3>setModifiedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModifiedElements</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.ModifiedElements modifiedElements)</span></div>
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
