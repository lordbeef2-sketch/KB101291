# JAVA OPENAPI: PasswordManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/teamwork2/esi/protect/PasswordManager.html
- source_path: `com/nomagic/magicdraw/teamwork2/esi/protect/PasswordManager.html`
- source_sha256: `2d6774002a3d0fc089af704906bea342a404feb39f1023575daa04d54a5854e3`
- captured_utc: `2026-07-14T16:45:47.595637+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2.esi.protect](package-summary.html)

## Interface PasswordManager

@OpenApiAllpublic interfacePasswordManager

Defines interface that allows to check whether a project is password protected and initiate
 password enter via GUI.

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[askPasswordIfProtected](#askPasswordIfProtected())()`
If the specified resource is password protected then the method asks the user to enter a password.
`boolean`
`[isProtected](#isProtected())()`
Checks whether the project is password protected.
`boolean`
`[isValidPassword](#isValidPassword(char%5B%5D))(char[] password)`
Returns true if the specified password is valid.

============ METHOD DETAIL ========== 
Method Details
askPasswordIfProtected
boolean askPasswordIfProtected()
If the specified resource is password protected then the method asks the user to enter a password.
Returns:
true if the resource is not package protected or the user entered a correct password, otherwise - false.
isProtected
boolean isProtected()
 throws [PasswordProtectException](PasswordProtectException.html)
Checks whether the project is password protected.
Returns:
true if the project is password protected, otherwise - false.
Throws:
`[PasswordProtectException](PasswordProtectException.html)` - if checking fails.
isValidPassword
boolean isValidPassword(char[] password)
 throws [PasswordProtectException](PasswordProtectException.html)
Returns true if the specified password is valid.
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
<h1 class="title" title="Interface PasswordManager">Interface PasswordManager</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PasswordManager</span></div>
<div class="block">Defines interface that allows to check whether a project is password protected and initiate
 password enter via GUI.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#askPasswordIfProtected()">askPasswordIfProtected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the specified resource is password protected then the method asks the user to enter a password.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isProtected()">isProtected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks whether the project is password protected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isValidPassword(char%5B%5D)">isValidPassword</a><wbr/>(char[] password)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true if the specified password is valid.</div>
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
<section class="detail" id="askPasswordIfProtected()">
<h3>askPasswordIfProtected</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">askPasswordIfProtected</span>()</div>
<div class="block">If the specified resource is password protected then the method asks the user to enter a password.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the resource is not package protected or the user entered a correct password, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProtected()">
<h3>isProtected</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isProtected</span>()
             throws <span class="exceptions"><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></span></div>
<div class="block">Checks whether the project is password protected.</div>
<dl class="notes">
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
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isValidPassword</span><wbr/><span class="parameters">(char[] password)</span>
                 throws <span class="exceptions"><a href="PasswordProtectException.html" title="class in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordProtectException</a></span></div>
<div class="block">Returns true if the specified password is valid.</div>
<dl class="notes">
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
