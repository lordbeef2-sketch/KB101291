# JAVA OPENAPI: ActionsCommandBarCreator.NMJideButtonFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/actions/ActionsCommandBarCreator.NMJideButtonFactory.html
- source_path: `com/nomagic/actions/ActionsCommandBarCreator.NMJideButtonFactory.html`
- source_sha256: `f8b2e2d4c084adbb7b8bfe265a2ada765cb03e30f16744d45420f8735ede724e`
- captured_utc: `2026-07-14T16:50:58.079895+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ActionsCommandBarCreator.NMJideButtonFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.actions.ActionsCommandBarCreator.NMJideButtonFactory

All Implemented Interfaces:
`[ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)`

Enclosing class:
[ActionsCommandBarCreator](ActionsCommandBarCreator.html)

public static classActionsCommandBarCreator.NMJideButtonFactory
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NMJideButtonFactory](#%3Cinit%3E())()`

`[NMJideButtonFactory](#%3Cinit%3E(boolean))(boolean popupClosable)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createButton](#createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))([NMAction](NMAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)`

`[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createButton](#createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))([NMStateAction](NMStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)`

`[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html)`
`[createButton](#createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))([NMTriStateAction](NMTriStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)`

`protected void`
`[initJideButton](#initJideButton(com.jidesoft.swing.JideButton))(com.jidesoft.swing.JideButton jideButton)`
Initialize created JideButton.
`boolean`
`[isShowButtonText](#isShowButtonText())()`

`void`
`[setShowButtonText](#setShowButtonText(boolean))(boolean showButtonText)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NMJideButtonFactory
public NMJideButtonFactory()
NMJideButtonFactory
public NMJideButtonFactory(boolean popupClosable)
 ============ METHOD DETAIL ========== 
Method Details
isShowButtonText
public boolean isShowButtonText()
setShowButtonText
public void setShowButtonText(boolean showButtonText)
createButton
public [AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMStateAction](NMStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)
Specified by:
`[createButton](ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))` in interface `[ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)`
createButton
public [AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMTriStateAction](NMTriStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)
Specified by:
`[createButton](ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))` in interface `[ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)`
createButton
public [AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMAction](NMAction.html) action,
 @CheckForNull
 com.nomagic.awt.HelpListener listener,
 @CheckForNull
 com.nomagic.awt.ActionIconProvider iconProvider)
Specified by:
`[createButton](ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider))` in interface `[ActionsCommandBarCreator.ButtonFactory](ActionsCommandBarCreator.ButtonFactory.html)`
initJideButton
protected void initJideButton(com.jidesoft.swing.JideButton jideButton)
Initialize created JideButton.
Parameters:
`jideButton` - button to initialize.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ActionsCommandBarCreator.NMJideButtonFactory">Class ActionsCommandBarCreator.NMJideButtonFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.actions.ActionsCommandBarCreator.NMJideButtonFactory</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="ActionsCommandBarCreator.html" title="class in com.nomagic.actions">ActionsCommandBarCreator</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">ActionsCommandBarCreator.NMJideButtonFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NMJideButtonFactory</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">NMJideButtonFactory</a><wbr/>(boolean popupClosable)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initJideButton(com.jidesoft.swing.JideButton)">initJideButton</a><wbr/>(com.jidesoft.swing.JideButton jideButton)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize  created JideButton.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowButtonText()">isShowButtonText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowButtonText(boolean)">setShowButtonText</a><wbr/>(boolean showButtonText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<h3>NMJideButtonFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMJideButtonFactory</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>NMJideButtonFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NMJideButtonFactory</span><wbr/><span class="parameters">(boolean popupClosable)</span></div>
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
<section class="detail" id="isShowButtonText()">
<h3>isShowButtonText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowButtonText</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setShowButtonText(boolean)">
<h3>setShowButtonText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowButtonText</span><wbr/><span class="parameters">(boolean showButtonText)</span></div>
</section>
</li>
<li>
<section class="detail" id="createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a></code> in interface <code><a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a></code> in interface <code><a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 @CheckForNull
 com.nomagic.awt.HelpListener listener,
 @CheckForNull
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ActionsCommandBarCreator.ButtonFactory.html#createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a></code> in interface <code><a href="ActionsCommandBarCreator.ButtonFactory.html" title="interface in com.nomagic.actions">ActionsCommandBarCreator.ButtonFactory</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initJideButton(com.jidesoft.swing.JideButton)">
<h3>initJideButton</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initJideButton</span><wbr/><span class="parameters">(com.jidesoft.swing.JideButton jideButton)</span></div>
<div class="block">Initialize  created JideButton.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>jideButton</code> - button to initialize.</dd>
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
