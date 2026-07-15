# JAVA OPENAPI: ActionsCommandBarCreator.ButtonFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/actions/ActionsCommandBarCreator.ButtonFactory.html
- source_path: `com/nomagic/actions/ActionsCommandBarCreator.ButtonFactory.html`
- source_sha256: `78fb6a39004e053e980749af4f08a2a283a447659fea74dfe7d0fc09efe8c9ef`
- captured_utc: `2026-07-14T16:50:58.543901+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Interface ActionsCommandBarCreator.ButtonFactory

All Known Implementing Classes:
`[ActionsCommandBarCreator.NMJideButtonFactory](ActionsCommandBarCreator.NMJideButtonFactory.html)`

Enclosing class:
[ActionsCommandBarCreator](ActionsCommandBarCreator.html)

public static interfaceActionsCommandBarCreator.ButtonFactory

Buttons factory used to create a button

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
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

============ METHOD DETAIL ========== 
Method Details
createButton
[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMStateAction](NMStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)
createButton
[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMTriStateAction](NMTriStateAction.html) action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)
createButton
[AbstractButton](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html) createButton([NMAction](NMAction.html) action,
 @CheckForNull
 com.nomagic.awt.HelpListener listener,
 @CheckForNull
 com.nomagic.awt.ActionIconProvider iconProvider)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Interface ActionsCommandBarCreator.ButtonFactory">Interface ActionsCommandBarCreator.ButtonFactory</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ActionsCommandBarCreator.NMJideButtonFactory.html" title="class in com.nomagic.actions">ActionsCommandBarCreator.NMJideButtonFactory</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="ActionsCommandBarCreator.html" title="class in com.nomagic.actions">ActionsCommandBarCreator</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">ActionsCommandBarCreator.ButtonFactory</span></div>
<div class="block">Buttons factory used to create a button</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">createButton</a><wbr/>(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="createButton(com.nomagic.actions.NMStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMStateAction.html" title="class in com.nomagic.actions">NMStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="createButton(com.nomagic.actions.NMTriStateAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMTriStateAction.html" title="class in com.nomagic.actions">NMTriStateAction</a> action,
 com.nomagic.awt.HelpListener listener,
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="createButton(com.nomagic.actions.NMAction,com.nomagic.awt.HelpListener,com.nomagic.awt.ActionIconProvider)">
<h3>createButton</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/AbstractButton.html" title="class or interface in javax.swing">AbstractButton</a></span> <span class="element-name">createButton</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 @CheckForNull
 com.nomagic.awt.HelpListener listener,
 @CheckForNull
 com.nomagic.awt.ActionIconProvider iconProvider)</span></div>
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
