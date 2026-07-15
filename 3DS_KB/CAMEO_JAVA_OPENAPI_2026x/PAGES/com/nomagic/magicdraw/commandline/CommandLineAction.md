# JAVA OPENAPI: CommandLineAction (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/commandline/CommandLineAction.html
- source_path: `com/nomagic/magicdraw/commandline/CommandLineAction.html`
- source_sha256: `b145512729f08b58ead83f059493743fd755b1b812120bb686b3a583d880d45b`
- captured_utc: `2026-07-14T16:57:51.639465+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.commandline](package-summary.html)

## Interface CommandLineAction

All Known Implementing Classes:
`[ProjectCommandLineAction](ProjectCommandLineAction.html)`

@OpenApiAllpublic interfaceCommandLineAction

Action allows to execute custom task in application command line mode.
 It must be registered via [`CommandLineActionManager.addAction(CommandLineAction)`](CommandLineActionManager.html#addAction(com.nomagic.magicdraw.commandline.CommandLineAction)).

See Also:
[`CommandLineActionManager`](CommandLineActionManager.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`byte`
`[execute](#execute(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args)`
Implement this method to execute custom task in running MagicDraw application environment.
`static void`
`[printToCommandLineConsole](#printToCommandLineConsole(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Print to commandline console.

============ METHOD DETAIL ========== 
Method Details
execute
byte execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args)
Implement this method to execute custom task in running MagicDraw application environment.
Returns:
application exit status.
printToCommandLineConsole
static void printToCommandLineConsole([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Print to commandline console. Do not use `System.out` since it might be redirected to log.
Parameters:
`text` - test to print

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.commandline</a></div>
<h1 class="title" title="Interface CommandLineAction">Interface CommandLineAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ProjectCommandLineAction.html" title="class in com.nomagic.magicdraw.commandline">ProjectCommandLineAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">CommandLineAction</span></div>
<div class="block">Action allows to execute custom task in application command line mode.
 It must be registered via <a href="CommandLineActionManager.html#addAction(com.nomagic.magicdraw.commandline.CommandLineAction)"><code>CommandLineActionManager.addAction(CommandLineAction)</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="CommandLineActionManager.html" title="class in com.nomagic.magicdraw.commandline"><code>CommandLineActionManager</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>byte</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Implement this method to execute custom task in running MagicDraw application environment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#printToCommandLineConsole(java.lang.String)">printToCommandLineConsole</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Print to commandline console.</div>
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
<section class="detail" id="execute(java.lang.String[])">
<h3>execute</h3>
<div class="member-signature"><span class="return-type">byte</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span></div>
<div class="block">Implement this method to execute custom task in running MagicDraw application environment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application exit status.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="printToCommandLineConsole(java.lang.String)">
<h3>printToCommandLineConsole</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">printToCommandLineConsole</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Print to commandline console. Do not use <code>System.out</code> since it might be redirected to log.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - test to print</dd>
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
