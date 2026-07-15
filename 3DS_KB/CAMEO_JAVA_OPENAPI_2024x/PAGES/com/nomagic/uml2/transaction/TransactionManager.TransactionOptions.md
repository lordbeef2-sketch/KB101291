# JAVA OPENAPI: TransactionManager.TransactionOptions (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/transaction/TransactionManager.TransactionOptions.html
- source_path: `com/nomagic/uml2/transaction/TransactionManager.TransactionOptions.html`
- source_sha256: `ac065eb8731d544329732360c54b4c58698746ca4a8b337c1d537124e0486911`
- captured_utc: `2026-07-14T16:53:16.351676+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Class TransactionManager.TransactionOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.transaction.TransactionManager.TransactionOptions

Enclosing interface:
[TransactionManager](TransactionManager.html)

public static classTransactionManager.TransactionOptions
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Transaction options. ReadOnly - if transaction is readonly any model modification throws
 [`ReadOnlyModelException`](ReadOnlyModelException.html) default value is false; FirePostCommit fires events when
 transaction is done. Default value is true.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html)`
`[DEFAULT](#DEFAULT)`
Read write, with post commit events.
`static [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html)`
`[NO_NOTIFICATION](#NO_NOTIFICATION)`
Read write without any notification.
`static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html)`
`[NO_POSTCOMMIT](#NO_POSTCOMMIT)`
Read write without post commit.
`static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html)`
`[READONLY](#READONLY)`
Readonly transaction with post commit.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TransactionOptions](#%3Cinit%3E(boolean,boolean,boolean))(boolean readonly,
 boolean firePostCommit,
 boolean validateModel)`

`[TransactionOptions](#%3Cinit%3E(boolean,boolean,boolean,boolean))(boolean readonly,
 boolean firePostCommit,
 boolean fireAllTransactionsCommitted,
 boolean validateModel)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
DEFAULT
public static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) DEFAULT
Read write, with post commit events.
READONLY
public static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) READONLY
Readonly transaction with post commit.
NO_POSTCOMMIT
public static final [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) NO_POSTCOMMIT
Read write without post commit.
NO_NOTIFICATION
public static [TransactionManager.TransactionOptions](TransactionManager.TransactionOptions.html) NO_NOTIFICATION
Read write without any notification. Use this only for the temporary model modification - after the transaction the model must be the same as before,
 i.e. if element is created in transaction it must be removed in the same transaction, etc.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TransactionOptions
public TransactionOptions(boolean readonly,
 boolean firePostCommit,
 boolean validateModel)
TransactionOptions
public TransactionOptions(boolean readonly,
 boolean firePostCommit,
 boolean fireAllTransactionsCommitted,
 boolean validateModel)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Class TransactionManager.TransactionOptions">Class TransactionManager.TransactionOptions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.transaction.TransactionManager.TransactionOptions</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing interface:</dt>
<dd><a href="TransactionManager.html" title="interface in com.nomagic.uml2.transaction">TransactionManager</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">TransactionManager.TransactionOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Transaction options. ReadOnly - if transaction is readonly any model modification throws
 <a href="ReadOnlyModelException.html" title="class in com.nomagic.uml2.transaction"><code>ReadOnlyModelException</code></a> default value is false; FirePostCommit fires events when
 transaction is done. Default value is true.</div>
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
<div class="col-first even-row-color"><code>static final <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT">DEFAULT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Read write, with post commit events.</div>
</div>
<div class="col-first odd-row-color"><code>static <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NO_NOTIFICATION">NO_NOTIFICATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Read write without any notification.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NO_POSTCOMMIT">NO_POSTCOMMIT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Read write without post commit.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#READONLY">READONLY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Readonly transaction with post commit.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean,boolean)">TransactionOptions</a><wbr/>(boolean readonly,
 boolean firePostCommit,
 boolean validateModel)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean,boolean,boolean)">TransactionOptions</a><wbr/>(boolean readonly,
 boolean firePostCommit,
 boolean fireAllTransactionsCommitted,
 boolean validateModel)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="DEFAULT">
<h3>DEFAULT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></span> <span class="element-name">DEFAULT</span></div>
<div class="block">Read write, with post commit events.</div>
</section>
</li>
<li>
<section class="detail" id="READONLY">
<h3>READONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></span> <span class="element-name">READONLY</span></div>
<div class="block">Readonly transaction with post commit.</div>
</section>
</li>
<li>
<section class="detail" id="NO_POSTCOMMIT">
<h3>NO_POSTCOMMIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></span> <span class="element-name">NO_POSTCOMMIT</span></div>
<div class="block">Read write without post commit.</div>
</section>
</li>
<li>
<section class="detail" id="NO_NOTIFICATION">
<h3>NO_NOTIFICATION</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TransactionManager.TransactionOptions.html" title="class in com.nomagic.uml2.transaction">TransactionManager.TransactionOptions</a></span> <span class="element-name">NO_NOTIFICATION</span></div>
<div class="block">Read write without any notification. Use this only for the temporary model modification - after the transaction the model must be the same as before,
 i.e. if element is created in transaction it must be removed in the same transaction, etc.</div>
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
<section class="detail" id="&lt;init&gt;(boolean,boolean,boolean)">
<h3>TransactionOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TransactionOptions</span><wbr/><span class="parameters">(boolean readonly,
 boolean firePostCommit,
 boolean validateModel)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean,boolean,boolean,boolean)">
<h3>TransactionOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TransactionOptions</span><wbr/><span class="parameters">(boolean readonly,
 boolean firePostCommit,
 boolean fireAllTransactionsCommitted,
 boolean validateModel)</span></div>
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
