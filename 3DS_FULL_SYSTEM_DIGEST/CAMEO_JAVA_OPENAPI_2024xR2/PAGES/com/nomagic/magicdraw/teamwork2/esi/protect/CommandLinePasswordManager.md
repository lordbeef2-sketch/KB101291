# JAVA OPENAPI: CommandLinePasswordManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/teamwork2/esi/protect/CommandLinePasswordManager.html
- source_path: `com/nomagic/magicdraw/teamwork2/esi/protect/CommandLinePasswordManager.html`
- source_sha256: `9afce28a7bce59219ee33ce481bfca667666347536ed4fea82061576a8c9fbc6`
- captured_utc: `2026-07-14T16:55:37.101252+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2.esi.protect](package-summary.html)

## Class CommandLinePasswordManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.teamwork2.esi.protect.CommandLinePasswordManager

All Implemented Interfaces:
`[PasswordManager](PasswordManager.html)`

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApiAllpublic classCommandLinePasswordManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [PasswordManager](PasswordManager.html)

Deprecated.
CommandLinePasswordManager does not add new functions to [`PasswordManager`](PasswordManager.html) and will be removed from Open API.
 Use [`PasswordManager`](PasswordManager.html) instead, create it using [`EsiUtils.getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)`](../../../esi/EsiUtils.html#getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)).

Password manager implementation for command line utilities

Version:
1.0

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected final com.nomagic.ci.persistence.ProjectDescriptor`
`[descriptor](#descriptor)`
Deprecated.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CommandLinePasswordManager](#%3Cinit%3E(com.nomagic.ci.persistence.ProjectDescriptor,com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking))(com.nomagic.ci.persistence.ProjectDescriptor descriptor,
 com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking implementation)`
Deprecated.
Creates and initializes a new `AbstractPasswordManager` from specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[askPasswordIfProtected](#askPasswordIfProtected())()`
Deprecated.
If the specified resource is password protected then the method asks the user to enter a password.
`boolean`
`[isProtected](#isProtected())()`
Deprecated.
Checks whether the project is password protected.
`boolean`
`[isValidPassword](#isValidPassword(char%5B%5D))(char[] password)`
Deprecated.
Returns true if the specified password is valid.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
descriptor
protected final com.nomagic.ci.persistence.ProjectDescriptor descriptor
Deprecated.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CommandLinePasswordManager
public CommandLinePasswordManager(com.nomagic.ci.persistence.ProjectDescriptor descriptor,
 com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking implementation)
Deprecated.
Creates and initializes a new `AbstractPasswordManager` from specified parameters.
Parameters:
`descriptor` - a project descriptor.
`implementation` - password checking implementation.
 ============ METHOD DETAIL ========== 
Method Details
askPasswordIfProtected
public boolean askPasswordIfProtected()
Deprecated.
Description copied from interface: `[PasswordManager](PasswordManager.html#askPasswordIfProtected())`
If the specified resource is password protected then the method asks the user to enter a password.
Specified by:
`[askPasswordIfProtected](PasswordManager.html#askPasswordIfProtected())` in interface `[PasswordManager](PasswordManager.html)`
Returns:
true if the resource is not package protected or the user entered a correct password, otherwise - false.
isProtected
public boolean isProtected()
 throws [PasswordProtectException](PasswordProtectException.html)
Deprecated.
Checks whether the project is password protected.
Specified by:
`[isProtected](PasswordManager.html#isProtected())` in interface `[PasswordManager](PasswordManager.html)`
Returns:
true if the project is password protected, otherwise - false.
Throws:
`[PasswordProtectException](PasswordProtectException.html)` - if checking fails.
isValidPassword
public boolean isValidPassword(char[] password)
 throws [PasswordProtectException](PasswordProtectException.html)
Deprecated.
Description copied from interface: `[PasswordManager](PasswordManager.html#isValidPassword(char%5B%5D))`
Returns true if the specified password is valid.
Specified by:
`[isValidPassword](PasswordManager.html#isValidPassword(char%5B%5D))` in interface `[PasswordManager](PasswordManager.html)`
Parameters:
`password` - the project password.
Returns:
true if valid.
Throws:
`[PasswordProtectException](PasswordProtectException.html)` - if checking whether the project password is valid fails.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2.esi.protect</a></div>
<h1 class="title" title="Class CommandLinePasswordManager">Class CommandLinePasswordManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.teamwork2.esi.protect.CommandLinePasswordManager</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CommandLinePasswordManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">CommandLinePasswordManager does not add new functions to <a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect"><code>PasswordManager</code></a> and will be removed from Open API.
 Use <a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect"><code>PasswordManager</code></a> instead, create it using <a href="../../../esi/EsiUtils.html#getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)"><code>EsiUtils.getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)</code></a>.</div>
</div>
<div class="block">Password manager implementation for command line utilities</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
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
<div class="col-first even-row-color"><code>protected final com.nomagic.ci.persistence.ProjectDescriptor</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#descriptor">descriptor</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ci.persistence.ProjectDescriptor,com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking)">CommandLinePasswordManager</a><wbr/>(com.nomagic.ci.persistence.ProjectDescriptor descriptor,
 com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking implementation)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates and initializes a new <code>AbstractPasswordManager</code> from specified parameters.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#askPasswordIfProtected()">askPasswordIfProtected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">If the specified resource is password protected then the method asks the user to enter a password.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isProtected()">isProtected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks whether the project is password protected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isValidPassword(char%5B%5D)">isValidPassword</a><wbr/>(char[] password)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns true if the specified password is valid.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="descriptor">
<h3>descriptor</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">com.nomagic.ci.persistence.ProjectDescriptor</span> <span class="element-name">descriptor</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.ci.persistence.ProjectDescriptor,com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking)">
<h3>CommandLinePasswordManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandLinePasswordManager</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.ProjectDescriptor descriptor,
 com.nomagic.magicdraw.teamwork2.esi.protect.PasswordChecking implementation)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates and initializes a new <code>AbstractPasswordManager</code> from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - a project descriptor.</dd>
<dd><code>implementation</code> - password checking implementation.</dd>
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
<section class="detail" id="askPasswordIfProtected()">
<h3>askPasswordIfProtected</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">askPasswordIfProtected</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="PasswordManager.html#askPasswordIfProtected()">PasswordManager</a></code></span></div>
<div class="block">If the specified resource is password protected then the method asks the user to enter a password.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PasswordManager.html#askPasswordIfProtected()">askPasswordIfProtected</a></code> in interface <code><a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></code></dd>
<dt>Returns:</dt>
<dd>true if the resource is not package protected or the user entered a correct password, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProtected()">
<h3>isProtected</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProtected</span>()
                    throws <span class="exceptions"><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks whether the project is password protected.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PasswordManager.html#isProtected()">isProtected</a></code> in interface <code><a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></code></dd>
<dt>Returns:</dt>
<dd>true if the project is password protected, otherwise - false.</dd>
<dt>Throws:</dt>
<dd><code><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></code> - if checking fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValidPassword(char[])">
<h3>isValidPassword</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValidPassword</span><wbr/><span class="parameters">(char[] password)</span>
                        throws <span class="exceptions"><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="PasswordManager.html#isValidPassword(char%5B%5D)">PasswordManager</a></code></span></div>
<div class="block">Returns true if the specified password is valid.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PasswordManager.html#isValidPassword(char%5B%5D)">isValidPassword</a></code> in interface <code><a href="PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>password</code> - the project password.</dd>
<dt>Returns:</dt>
<dd>true if valid.</dd>
<dt>Throws:</dt>
<dd><code><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></code> - if checking whether the project password is valid fails.</dd>
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
