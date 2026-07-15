# JAVA OPENAPI: Commandline (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/license/utils/exec/Commandline.html
- source_path: `com/nomagic/license/utils/exec/Commandline.html`
- source_sha256: `d18d1ae5d8f4559188e621f936b2920798fda5901bd40e49f8b1e0097cd5c09d`
- captured_utc: `2026-07-14T16:50:59.515915+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.license.utils.exec](package-summary.html)

## Interface Commandline

All Known Implementing Classes:
`[CommandlineImpl](CommandlineImpl.html)`

@OpenApiAllpublic interfaceCommandline

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final long`
`[DEFAULT_TIMEOUT](#DEFAULT_TIMEOUT)`
Default process timeout = 1 minute
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String%5B%5D,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String%5B%5D,java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String,java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)`
Execute command line
`[ProcessOutput](ProcessOutput.html)`
`[execute](#execute(java.lang.String,java.lang.String%5B%5D,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`
Execute command line
`long`
`[getTimeout](#getTimeout())()`

`boolean`
`[isLogEnabled](#isLogEnabled())()`

`void`
`[log](#log(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Print some log information.
`void`
`[setTimeout](#setTimeout(long))(long timeout)`

============ FIELD DETAIL =========== 
Field Details
DEFAULT_TIMEOUT
static final long DEFAULT_TIMEOUT
Default process timeout = 1 minute
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.license.utils.exec.Commandline.DEFAULT_TIMEOUT)
 ============ METHOD DETAIL ========== 
Method Details
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
[ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
getTimeout
long getTimeout()
Returns:
setTimeout
void setTimeout(long timeout)
isLogEnabled
boolean isLogEnabled()
Returns:
log
void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Print some log information.
Parameters:
`text` -

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.license.utils.exec</a></div>
<h1 class="title" title="Interface Commandline">Interface Commandline</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="CommandlineImpl.html" title="class in com.nomagic.license.utils.exec">CommandlineImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Commandline</span></div>
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
<div class="col-first even-row-color"><code>static final long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_TIMEOUT">DEFAULT_TIMEOUT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default process timeout = 1 minute</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTimeout()">getTimeout</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLogEnabled()">isLogEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#log(java.lang.String)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Print some log information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTimeout(long)">setTimeout</a><wbr/>(long timeout)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
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
<section class="detail" id="DEFAULT_TIMEOUT">
<h3>DEFAULT_TIMEOUT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">long</span> <span class="element-name">DEFAULT_TIMEOUT</span></div>
<div class="block">Default process timeout = 1 minute</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.license.utils.exec.Commandline.DEFAULT_TIMEOUT">Constant Field Values</a></li>
</ul>
</dd>
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
<section class="detail" id="execute(java.lang.String,java.lang.String[],java.io.File)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir</code> - file working directory</dd>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.lang.String[])">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.io.File)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir</code> - file working directory</dd>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String[],java.lang.String[],java.io.File)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir</code> - file working directory</dd>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String[],java.lang.String[])">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String[],java.io.File)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir</code> - file working directory</dd>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String[])">
<h3>execute</h3>
<div class="member-signature"><span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cmd</code> - command line</dd>
<dt>Returns:</dt>
<dd>output of command</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeout()">
<h3>getTimeout</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getTimeout</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeout(long)">
<h3>setTimeout</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTimeout</span><wbr/><span class="parameters">(long timeout)</span></div>
</section>
</li>
<li>
<section class="detail" id="isLogEnabled()">
<h3>isLogEnabled</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLogEnabled</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String)">
<h3>log</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Print some log information.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - </dd>
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
